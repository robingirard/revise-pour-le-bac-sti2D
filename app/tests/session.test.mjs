import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildSkillSession, buildReviewSession, answer, summary, isFinished, currentItemId, mulberry32, shuffle, skillCounts, countDue } from '../js/session.js';
import { grade } from '../js/scheduler.js';
import { addDays } from '../js/dates.js';
import { makeContent, makeProgress } from './helpers.mjs';

const T = '2026-09-04';

test('mulberry32 est déterministe et shuffle conserve les éléments', () => {
  const a = mulberry32(42), b = mulberry32(42);
  assert.equal(a(), b());
  const arr = [1, 2, 3, 4, 5, 6, 7, 8];
  const s = shuffle(arr, mulberry32(1));
  assert.deepEqual([...s].sort((x, y) => x - y), arr);
  assert.deepEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8]); // copie
});

test('séance de compétence : nouveaux de niveau ≤ niveau+1, 10 max', () => {
  const content = makeContent();
  const p = makeProgress();
  const s = buildSkillSession(content, p, 's1', { today: T, rng: mulberry32(3) });
  assert.equal(s.queue.length, 8); // 8 items de niveau 1 seulement (niveau 2 inaccessible au niveau 0)
  assert.ok(s.queue.every((id) => content.items[id].level === 1));
  p.skills.s1 = { level: 1, progress: 0, sessions: 2, xp: 0 };
  const s2 = buildSkillSession(content, p, 's1', { today: T, rng: mulberry32(3) });
  assert.equal(s2.queue.length, 10);
  assert.equal(new Set(s2.queue).size, 10);
});

test('les items dus passent avant les nouveaux ; les déjà vus complètent', () => {
  const content = makeContent();
  const p = makeProgress();
  // 3 items dus (vus il y a longtemps), 2 items vus mais pas dus, le reste nouveau
  for (const id of ['s1-l1-1', 's1-l1-2', 's1-l1-3']) p.items[id] = grade(undefined, 'good', addDays(T, -5));
  for (const id of ['s1-l1-4', 's1-l1-5']) p.items[id] = grade(undefined, 'easy', T); // dus dans 3 jours
  const s = buildSkillSession(content, p, 's1', { today: T, rng: mulberry32(7) });
  const ids = new Set(s.queue);
  assert.ok(['s1-l1-1', 's1-l1-2', 's1-l1-3'].every((id) => ids.has(id)));
  assert.equal(s.queue.length, 8); // 3 dus + 3 nouveaux (6,7,8) + 2 déjà vus = 8 disponibles
  assert.ok(ids.has('s1-l1-4') && ids.has('s1-l1-5'));
  const counts = skillCounts(content, p, 's1', T);
  assert.deepEqual(counts, { total: 14, due: 3, fresh: 9, mastered: 0 });
});

test('forceItemId place l\'item demandé en premier', () => {
  const content = makeContent();
  const s = buildSkillSession(content, makeProgress(), 's1', { today: T, rng: mulberry32(1), forceItemId: 's1-l1-7' });
  assert.equal(s.queue[0], 's1-l1-7');
  assert.equal(new Set(s.queue).size, s.queue.length);
});

test('un item raté est remis en fin de file ; seule la 1re tentative compte', () => {
  const content = makeContent();
  let s = buildSkillSession(content, makeProgress(), 's1', { today: T, rng: mulberry32(5), size: 3 });
  assert.equal(s.queue.length, 3);
  const first = currentItemId(s);
  let r = answer(s, { correct: false });
  s = r.session;
  assert.equal(r.schedulerGrade, 'again'); assert.equal(r.firstAttempt, true);
  assert.equal(s.queue.length, 4); assert.equal(s.queue[3], first);
  r = answer(s, { correct: true }); s = r.session; assert.equal(r.schedulerGrade, 'good');
  r = answer(s, { correct: true, grade: 'easy' }); s = r.session; assert.equal(r.schedulerGrade, 'easy');
  assert.equal(currentItemId(s), first);
  r = answer(s, { correct: true }); s = r.session;
  assert.equal(r.schedulerGrade, null); assert.equal(r.firstAttempt, false);
  assert.equal(isFinished(s), true);
  assert.deepEqual(summary(s), { total: 3, correct: 2, accuracy: 2 / 3 });
  assert.throws(() => answer(s, { correct: true }), /terminée/);
});

test('séance de révision : items dus des compétences déverrouillées, 20 max', () => {
  const content = makeContent();
  const p = makeProgress();
  p.skills.s1 = { level: 1, progress: 0, sessions: 2, xp: 0 }; // s2 déverrouillée, s3 non
  for (let i = 1; i <= 25; i++) p.items[`s2-l1-${i}`] = grade(undefined, 'good', addDays(T, -2));
  for (let i = 1; i <= 4; i++) p.items[`s3-l1-${i}`] = grade(undefined, 'good', addDays(T, -2)); // verrouillée
  p.items['s1-l1-1'] = grade(undefined, 'good', addDays(T, -10)); // la plus ancienne
  assert.equal(countDue(content, p, T), 26);
  const s = buildReviewSession(content, p, { today: T, rng: mulberry32(9) });
  assert.equal(s.kind, 'review'); assert.equal(s.queue.length, 20);
  assert.ok(s.queue.includes('s1-l1-1'));
  assert.ok(s.queue.every((id) => !id.startsWith('s3-')));
  const empty = buildReviewSession(content, makeProgress(), { today: T });
  assert.equal(empty.queue.length, 0);
});
