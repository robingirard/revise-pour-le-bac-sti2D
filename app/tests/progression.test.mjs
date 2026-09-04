import { test } from 'node:test';
import assert from 'node:assert/strict';
import { isUnlocked, applySession, updateStreak, currentStreak, xpOnDay, sessionXp, newSkillState, isCompleted } from '../js/progression.js';
import { makeContent, makeProgress } from './helpers.mjs';

const content = makeContent();
const [s1, s2] = content.units[0].skills;
const s3 = content.units[1].skills[0];

test('déverrouillage : prérequis au niveau ≥ 1', () => {
  const p = makeProgress();
  assert.equal(isUnlocked(s1, p), true);
  assert.equal(isUnlocked(s2, p), false);
  p.skills.s1 = { ...newSkillState(), level: 1 };
  assert.equal(isUnlocked(s2, p), true);
  assert.equal(isUnlocked(s3, p), false);
  p.skills.s2 = { ...newSkillState(), level: 1 };
  assert.equal(isUnlocked(s3, p), true);
});

test('montée de niveau : 2 séances à ≥ 80 %', () => {
  let r = applySession(undefined, s2, { correct: 8, total: 10 });
  assert.equal(r.passed, true); assert.equal(r.leveledUp, false);
  assert.equal(r.state.progress, 0.5); assert.equal(r.state.level, 0); assert.equal(r.state.sessions, 1);
  assert.equal(r.xp, 10 + 2 * 8);
  r = applySession(r.state, s2, { correct: 10, total: 10 });
  assert.equal(r.leveledUp, true); assert.equal(r.state.level, 1); assert.equal(r.state.progress, 0);
  assert.equal(r.state.xp, 26 + 30);
});

test('une séance < 80 % compte mais ne fait pas progresser', () => {
  const r = applySession(undefined, s1, { correct: 7, total: 10 });
  assert.equal(r.passed, false); assert.equal(r.state.progress, 0); assert.equal(r.state.sessions, 1);
  assert.equal(r.xp, 24);
  const empty = applySession(undefined, s1, { correct: 0, total: 0 });
  assert.equal(empty.passed, false);
});

test('niveau plafonné au nombre de niveaux de la compétence', () => {
  let st = { ...newSkillState(), level: 2 }; // s1 a 2 niveaux
  const r = applySession(st, s1, { correct: 10, total: 10 });
  assert.equal(r.state.level, 2); assert.equal(r.leveledUp, false);
  assert.equal(isCompleted(s1, { skills: { s1: r.state } }), true);
});

test('série : jours consécutifs, même jour idempotent, rupture', () => {
  let st = updateStreak(undefined, '2026-09-01');
  assert.deepEqual(st, { count: 1, last: '2026-09-01' });
  st = updateStreak(st, '2026-09-01');
  assert.equal(st.count, 1);
  st = updateStreak(st, '2026-09-02');
  assert.equal(st.count, 2);
  assert.equal(currentStreak(st, '2026-09-02'), 2);
  assert.equal(currentStreak(st, '2026-09-03'), 2); // encore vivante (hier)
  assert.equal(currentStreak(st, '2026-09-04'), 0); // rompue
  st = updateStreak(st, '2026-09-05');
  assert.equal(st.count, 1);
});

test('XP du jour d\'après l\'historique', () => {
  const history = [{ date: '2026-09-04', xp: 12 }, { date: '2026-09-04', xp: 20 }, { date: '2026-09-03', xp: 50 }];
  assert.equal(xpOnDay(history, '2026-09-04'), 32);
  assert.equal(xpOnDay(history, '2026-09-05'), 0);
  assert.equal(sessionXp({ correct: 0, total: 5 }), 10);
});
