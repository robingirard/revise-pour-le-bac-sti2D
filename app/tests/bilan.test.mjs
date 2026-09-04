import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildBilan, encodeBilan, decodeBilan, bilanText, bilanUrl, tagLabel } from '../js/bilan.js';
import { makeContent, makeProgress } from './helpers.mjs';

const content = makeContent();
content.items['s1-l1-1'].tags = ['pivot-glissant'];
content.items['s1-l1-1'].payload.choices = ['Pivot glissant', 'Pivot'];
content.items['s1-l1-2'].tags = ['pivot-glissant', 'serre-joint'];
content.items['s1-l1-3'].tags = ['rotule'];

function fixture() {
  return makeProgress({
    xp: 420,
    streak: { count: 5, last: '2026-09-04' },
    settings: { dailyGoal: 30, name: 'Tom' },
    skills: { s1: { level: 2, progress: 0.5, sessions: 5, xp: 200 } },
    history: [
      { date: '2026-08-20', kind: 'skill', skill: 's1', correct: 5, total: 10, xp: 20 },   // hors semaine, hors « 3 dernières »
      { date: '2026-08-30', kind: 'skill', skill: 's1', correct: 6, total: 10, xp: 22 },
      { date: '2026-09-01', kind: 'skill', skill: 's1', correct: 8, total: 10, xp: 26 },
      { date: '2026-09-03', kind: 'review', skill: null, correct: 9, total: 10, xp: 28 },
      { date: '2026-09-04', kind: 'skill', skill: 's1', correct: 10, total: 10, xp: 30 },
    ],
    items: {
      's1-l1-1': { reps: 0, ease: 2.1, interval: 0, due: '2026-09-04', lapses: 3, last: '2026-09-04' }, // dû, raté 3 fois
      's1-l1-2': { reps: 4, ease: 2.5, interval: 25, due: '2026-09-29', lapses: 1, last: '2026-09-04' }, // maîtrisé
      's1-l1-3': { reps: 1, ease: 2.5, interval: 1, due: '2026-09-02', lapses: 2, last: '2026-09-01' },  // en retard
      'inconnu': { reps: 1, ease: 2.5, interval: 1, due: '2026-09-02', lapses: 9, last: '2026-09-01' },  // item absent du contenu : ignoré
    },
  });
}

test('buildBilan : compteurs, réussite, semaine, points faibles', () => {
  const b = buildBilan(fixture(), content, '2026-09-04');
  assert.equal(b.v, 1); assert.equal(b.date, '2026-09-04'); assert.equal(b.name, 'Tom');
  assert.equal(b.xp, 420); assert.equal(b.streak, 5);
  assert.equal(b.sessions7d, 4);                 // depuis le 29/08 : 30/08, 01/09, 03/09, 04/09
  assert.equal(b.accuracy7d, Math.round(100 * 33 / 40));
  const s1 = b.skills.find((s) => s.id === 's1');
  assert.equal(s1.level, 2); assert.equal(s1.sessions, 5);
  assert.equal(s1.acc, 80);                      // 3 dernières séances de s1 : 6 + 8 + 10 sur 30
  assert.equal(s1.total, 14); assert.equal(s1.seen, 3); assert.equal(s1.mastered, 1); assert.equal(s1.due, 2);
  const s2 = b.skills.find((s) => s.id === 's2');
  assert.equal(s2.acc, null); assert.equal(s2.seen, 0); assert.equal(s2.level, 0);
  assert.equal(b.recent.length, 5);
  assert.equal(b.recent[0].date, '2026-09-04');  // la plus récente d'abord
  assert.equal(b.recent[1].skill, null);
  assert.deepEqual(b.weak, [{ tag: 'pivot-glissant', lapses: 4 }, { tag: 'rotule', lapses: 2 }, { tag: 'serre-joint', lapses: 1 }]);
});

test('buildBilan : progression vide', () => {
  const b = buildBilan(makeProgress(), content, '2026-09-04');
  assert.equal(b.name, ''); assert.equal(b.sessions7d, 0); assert.equal(b.accuracy7d, null);
  assert.equal(b.skills.length, 3); assert.deepEqual(b.weak, []); assert.deepEqual(b.recent, []);
});

test('encodeBilan / decodeBilan : aller-retour avec accents, forme validée', () => {
  const p = fixture();
  p.settings.name = 'Léa Ñoño 🚀';
  const b = buildBilan(p, content, '2026-09-04');
  const enc = encodeBilan(b);
  assert.match(enc, /^[A-Za-z0-9_-]+$/);
  assert.deepEqual(decodeBilan(enc), b);
  assert.match(bilanUrl(b, 'https://x.test/app/'), /^https:\/\/x\.test\/app\/#\/bilan\?d=[A-Za-z0-9_-]+$/);
});

test('decodeBilan refuse les données invalides', () => {
  assert.throws(() => decodeBilan('pas du base64 !'), /bilan valide/);
  assert.throws(() => decodeBilan(''), /bilan valide/);
  assert.throws(() => decodeBilan(btoa('{"v":2}')), /bilan valide/);
  assert.throws(() => decodeBilan(btoa('[1,2]')), /bilan valide/);
  assert.throws(() => decodeBilan(btoa('{"v":1,"date":"hier","skills":[],"recent":[],"weak":[]}')), /bilan valide/);
  // forme valide mais champs suspects : nettoyés, jamais évalués
  const b = decodeBilan(btoa(JSON.stringify({ v: 1, date: '2026-09-04', name: '<b>x</b>', xp: '12', skills: [{ id: 's1', level: '1' }, null], recent: [{ date: 'x' }], weak: [{ tag: 'a', lapses: 'b' }] })));
  assert.equal(b.name, '<b>x</b>'); assert.equal(b.xp, 12);
  assert.deepEqual(b.skills, [{ id: 's1', level: 1, progress: 0, sessions: 0, acc: null, total: 0, seen: 0, mastered: 0, due: 0 }]);
  assert.deepEqual(b.recent, []); assert.deepEqual(b.weak, [{ tag: 'a', lapses: 0 }]);
});

test('bilanText et tagLabel', () => {
  const b = buildBilan(fixture(), content, '2026-09-04');
  const txt = bilanText(b, content);
  assert.match(txt, /Bilan Révise STI2D de Tom/);
  assert.match(txt, /Série : 5 jours · 420 XP/);
  assert.match(txt, /4 séances, 83 % de bonnes réponses/);
  assert.match(txt, /- S1 : niveau 2\/2, réussite 80 %, 3\/14 vus, 1 maîtrisé/);
  assert.match(txt, /- S2 : pas encore commencé/);
  assert.match(txt, /Points faibles : Pivot glissant \(4 erreurs\), Rotule \(2 erreurs\), Serre joint \(1 erreur\)/);
  assert.equal(tagLabel('s2', content), 'S2');           // compétence
  assert.equal(tagLabel('pivot-glissant', content), 'Pivot glissant'); // trouvé dans un QCM
  assert.equal(tagLabel('bielle-manivelle', content), 'Bielle manivelle'); // embelli
});
