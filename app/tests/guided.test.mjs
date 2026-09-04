import { test } from 'node:test';
import assert from 'node:assert/strict';
import { guidedGrade, guidedResult, nextStepIndex, guidedUnlocked, annaleStatus, guidedSteps, isGuided, XP_PER_STEP } from '../js/guided-logic.js';
import { buildSkillSession, buildReviewSession, answer, skillCounts, dueItems, mulberry32, guidedItems, findSkill } from '../js/session.js';
import { applySession, sessionXp } from '../js/progression.js';
import { grade } from '../js/scheduler.js';
import { addDays } from '../js/dates.js';
import { makeContent, makeProgress } from './helpers.mjs';

const T = '2026-09-04';

function withGuided(content = makeContent()) {
  const s1 = content.units[0].skills[0];
  content.items['s1-guided'] = { id: 's1-guided', skill: 's1', type: 'guided', level: 3, tags: [], payload: {
    title: 'Exercice complet', intro: 'Contexte',
    steps: [{ kind: 'mcq', prompt: 'q', choices: ['a', 'b'], answer: [0] }, { prompt: 'q2', choices: ['a', 'b'], answer: [1] }, { kind: 'input', prompt: 'q3', answer: '4', numeric: true }],
  } };
  s1.items.push('s1-guided');
  return content;
}

test('note et résultat d\'un exercice complet', () => {
  assert.equal(guidedGrade(4, 4), 'good');
  assert.equal(guidedGrade(2, 4), 'hard');
  assert.equal(guidedGrade(3, 5), 'hard');
  assert.equal(guidedGrade(1, 4), 'again');
  assert.equal(guidedGrade(0, 0), 'again');
  const r = guidedResult(3, 4);
  assert.deepEqual(r, { correct: false, grade: 'hard', detail: '3 / 4 étapes justes du premier coup.', xpBonus: 3 * XP_PER_STEP, requeue: false });
  assert.equal(guidedResult(4, 4).correct, true);
  assert.equal(guidedResult(4, 4).grade, 'good');
  assert.equal(nextStepIndex(0, 3), 1);
  assert.equal(nextStepIndex(2, 3), null);
});

test('étapes : kind par défaut mcq ; isGuided', () => {
  const content = withGuided();
  const steps = guidedSteps(content.items['s1-guided']);
  assert.equal(steps.length, 3);
  assert.equal(steps[1].kind, 'mcq');
  assert.equal(steps[2].kind, 'input');
  assert.equal(isGuided(content.items['s1-guided']), true);
  assert.equal(isGuided(content.items['s1-l1-1']), false);
  assert.deepEqual(guidedSteps({ id: 'x', type: 'guided', payload: {} }), []);
});

test('déverrouillage : niveau ≥ 2 ou mode découverte', () => {
  assert.equal(guidedUnlocked({ level: 1 }, {}), false);
  assert.equal(guidedUnlocked({ level: 2 }, {}), true);
  assert.equal(guidedUnlocked(undefined, { unlockAll: true }), true);
  assert.equal(guidedUnlocked(undefined, {}), false);
});

test('annales : prérequis manquants et mode découverte', () => {
  const a = { id: 'a', prerequis: [{ skill: 's1', level: 2 }, { skill: 's2', level: 1 }] };
  const p = makeProgress({ skills: { s1: { level: 2, progress: 0, sessions: 4, xp: 0 } } });
  let st = annaleStatus(a, p);
  assert.equal(st.locked, true);
  assert.deepEqual(st.missing, [{ skill: 's2', level: 1 }]);
  p.skills.s2 = { level: 1, progress: 0, sessions: 2, xp: 0 };
  assert.equal(annaleStatus(a, p).locked, false);
  p.skills.s2.level = 0;
  p.settings.unlockAll = true;
  st = annaleStatus(a, p);
  assert.equal(st.locked, false);
  assert.equal(st.missing.length, 1); // toujours listé, mais pas bloquant
  assert.equal(annaleStatus({ id: 'b' }, makeProgress()).locked, false); // sans prérequis
});

test('les exercices complets sont exclus des séances ordinaires, des comptes et des révisions', () => {
  const content = withGuided();
  const p = makeProgress();
  p.skills.s1 = { level: 2, progress: 0, sessions: 4, xp: 0 };
  const s = buildSkillSession(content, p, 's1', { today: T, rng: mulberry32(2) });
  assert.ok(!s.queue.includes('s1-guided'));
  assert.equal(skillCounts(content, p, 's1', T).total, 14);
  p.items['s1-guided'] = grade(undefined, 'good', addDays(T, -5)); // dû, mais jamais tiré en révision
  assert.ok(!dueItems(content, p, T).some((it) => it.id === 's1-guided'));
  assert.ok(!buildReviewSession(content, p, { today: T, rng: mulberry32(1) }).queue.includes('s1-guided'));
  assert.deepEqual(guidedItems(content, findSkill(content, 's1')).map((it) => it.id), ['s1-guided']);
});

test('forcé via ?item=, un exercice complet est seul dans sa séance', () => {
  const content = withGuided();
  const s = buildSkillSession(content, makeProgress(), 's1', { today: T, rng: mulberry32(1), forceItemId: 's1-guided' });
  assert.deepEqual(s.queue, ['s1-guided']);
  assert.equal(s.xpBonus, 0);
});

test('réponse d\'un exercice complet : bonus d\'XP, pas de remise en file', () => {
  const content = withGuided();
  let s = buildSkillSession(content, makeProgress(), 's1', { today: T, forceItemId: 's1-guided' });
  const r = answer(s, guidedResult(2, 3));
  s = r.session;
  assert.equal(r.schedulerGrade, 'again');
  assert.equal(s.queue.length, 1); // requeue: false
  assert.equal(s.xpBonus, 4);
  assert.equal(s.index, 1);
  // bonus ajouté aux XP de la séance et à ceux de la compétence
  const skill = findSkill(content, 's1');
  const res = applySession(undefined, skill, { correct: 1, total: 1 }, s.xpBonus);
  assert.equal(res.xp, sessionXp({ correct: 1, total: 1 }) + 4);
  assert.equal(res.state.xp, res.xp);
  assert.equal(applySession(undefined, skill, { correct: 1, total: 1 }).xp, sessionXp({ correct: 1, total: 1 }));
});
