import { test } from 'node:test';
import assert from 'node:assert/strict';
import { load, save, reset, exportJson, importJson, emptyProgress, STORAGE_KEY } from '../js/store.js';
import { MemoryStorage } from './helpers.mjs';

test('load renvoie une progression vide si rien n\'est stocké ou si le JSON est corrompu', () => {
  const st = new MemoryStorage();
  assert.deepEqual(load(st), emptyProgress());
  st.setItem(STORAGE_KEY, '{oops');
  assert.deepEqual(load(st), emptyProgress());
  assert.deepEqual(load(null), emptyProgress());
});

test('save / load / reset', () => {
  const st = new MemoryStorage();
  const p = emptyProgress();
  p.xp = 42; p.items.a = { reps: 1 };
  assert.equal(save(p, st), true);
  assert.equal(load(st).xp, 42);
  assert.deepEqual(reset(st), emptyProgress());
  assert.equal(st.getItem(STORAGE_KEY), null);
  assert.equal(save(p, null), false);
});

test('export / import : aller-retour, champs manquants complétés, refus des textes invalides', () => {
  const p = emptyProgress();
  p.skills.s1 = { level: 1, progress: 0.5, sessions: 3, xp: 60 };
  const back = importJson(exportJson(p));
  assert.deepEqual(back, p);
  const partial = importJson('{"items":{},"skills":{"s1":{"level":2}}}');
  assert.equal(partial.settings.dailyGoal, 30);
  assert.equal(partial.streak.count, 0);
  assert.throws(() => importJson('pas du json'), /JSON valide/);
  assert.throws(() => importJson('{"foo":1}'), /progression/);
  assert.throws(() => importJson('[1,2]'), /progression|invalide/);
});
