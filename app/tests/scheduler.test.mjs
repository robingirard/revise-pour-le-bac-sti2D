import { test } from 'node:test';
import assert from 'node:assert/strict';
import { grade, newState, isDue, isNew, isMastered } from '../js/scheduler.js';
import { addDays, diffDays, todayStr } from '../js/dates.js';

const T = '2026-09-04';

test('dates : addDays / diffDays / todayStr', () => {
  assert.equal(addDays(T, 1), '2026-09-05');
  assert.equal(addDays('2026-12-31', 1), '2027-01-01');
  assert.equal(addDays('2026-03-01', -1), '2026-02-28');
  assert.equal(diffDays('2026-09-01', T), 3);
  assert.match(todayStr(new Date(2026, 0, 5)), /^2026-01-05$/);
});

test('un item nouveau n\'est ni dû ni maîtrisé', () => {
  assert.equal(isNew(undefined), true);
  assert.equal(isNew(newState()), true);
  assert.equal(isDue(undefined, T), false);
  assert.equal(isMastered(undefined), false);
});

test('good : 1 jour, puis 3 jours, puis intervalle × ease', () => {
  let s = grade(undefined, 'good', T);
  assert.equal(s.interval, 1); assert.equal(s.due, addDays(T, 1)); assert.equal(s.reps, 1);
  s = grade(s, 'good', s.due);
  assert.equal(s.interval, 3); assert.equal(s.reps, 2);
  s = grade(s, 'good', s.due);
  assert.equal(s.interval, Math.round(3 * 2.5)); // 8
  assert.equal(s.ease, 2.5);
  assert.equal(isNew(s), false);
});

test('again : remise à zéro, ease −0.2 (min 1.3), lapses +1, dû aujourd\'hui', () => {
  let s = grade(undefined, 'good', T);
  s = grade(s, 'good', addDays(T, 1));
  s = grade(s, 'again', addDays(T, 4));
  assert.equal(s.reps, 0); assert.equal(s.interval, 0); assert.equal(s.lapses, 1);
  assert.equal(s.ease, 2.3); assert.equal(s.due, addDays(T, 4));
  assert.equal(isDue(s, addDays(T, 4)), true);
  for (let i = 0; i < 10; i++) s = grade(s, 'again', T);
  assert.equal(s.ease, 1.3);
});

test('hard : intervalle max(1, ×1.2), ease −0.15', () => {
  let s = grade(undefined, 'hard', T);
  assert.equal(s.interval, 1); assert.equal(s.ease, 2.35); assert.equal(s.reps, 1);
  s = { ...s, interval: 10 };
  s = grade(s, 'hard', T);
  assert.equal(s.interval, 12); assert.equal(s.ease, 2.2);
});

test('easy : 3 jours au départ, puis ×ease×1.3, ease +0.15', () => {
  let s = grade(undefined, 'easy', T);
  assert.equal(s.interval, 3); assert.equal(s.ease, 2.65);
  s = grade(s, 'easy', s.due);
  assert.equal(s.interval, Math.round(3 * 2.65 * 1.3)); // 10
  assert.equal(s.ease, 2.8);
});

test('isDue / isMastered', () => {
  const s = { ...newState(), interval: 21, due: '2026-09-10', last: T };
  assert.equal(isDue(s, '2026-09-09'), false);
  assert.equal(isDue(s, '2026-09-10'), true);
  assert.equal(isDue(s, '2026-09-11'), true);
  assert.equal(isMastered(s), true);
  assert.equal(isMastered({ ...s, interval: 20 }), false);
});

test('grade ne modifie pas l\'état d\'entrée et rejette une note inconnue', () => {
  const s0 = grade(undefined, 'good', T);
  const copy = JSON.stringify(s0);
  grade(s0, 'easy', T);
  assert.equal(JSON.stringify(s0), copy);
  assert.throws(() => grade(s0, 'bof', T), /Note inconnue/);
});
