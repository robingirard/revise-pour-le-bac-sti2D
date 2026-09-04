import { test } from 'node:test';
import assert from 'node:assert/strict';
import { setEquals, normalizeAnswer, checkInput } from '../js/answers.js';

test('setEquals', () => {
  assert.equal(setEquals(['Tx', 'Rx'], new Set(['Rx', 'Tx'])), true);
  assert.equal(setEquals(['Tx'], ['Tx', 'Rx']), false);
  assert.equal(setEquals([], []), true);
});

test('normalisation : minuscules, accents, espaces, virgule décimale', () => {
  assert.equal(normalizeAnswer('  Liaison Hélicoïdale '), 'liaisonhelicoidale');
  assert.equal(normalizeAnswer('3,5'), '3.5');
  assert.equal(normalizeAnswer(undefined), '');
});

test('checkInput texte : réponse et variantes acceptées', () => {
  const p = { answer: 'hélicoïdale', accept: ['liaison hélicoïdale'] };
  assert.equal(checkInput(p, 'Helicoidale'), true);
  assert.equal(checkInput(p, 'liaison  hélicoïdale'), true);
  assert.equal(checkInput(p, 'pivot'), false);
  assert.equal(checkInput(p, ''), false);
});

test('checkInput numérique : tolérance et virgule', () => {
  assert.equal(checkInput({ answer: '6', numeric: true }, '6'), true);
  assert.equal(checkInput({ answer: '6', numeric: true }, '6,0'), true);
  assert.equal(checkInput({ answer: '3.14', numeric: true, tolerance: 0.01 }, '3,15'), true);
  assert.equal(checkInput({ answer: '3.14', numeric: true, tolerance: 0.001 }, '3.15'), false);
  assert.equal(checkInput({ answer: '6', numeric: true }, 'six'), false);
});
