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

import { mcqDetail, gridDetail, orderDetail } from '../js/answers.js';

test('mcqDetail : feedback du mauvais choix, sinon de la bonne réponse oubliée', () => {
  const fb = ['ok', 'non : b', null, 'non : d'];
  assert.equal(mcqDetail([1], [0], fb), 'non : b');
  assert.equal(mcqDetail([2], [0], fb), null);            // pas de feedback prévu pour ce choix
  assert.equal(mcqDetail([3, 1], [0], fb), 'non : b');    // premier mauvais choix par indice croissant
  assert.equal(mcqDetail([0], [0], fb), null);            // juste
  assert.equal(mcqDetail([0], [0, 1], fb), 'non : b');    // réponse multiple : bonne réponse oubliée
  assert.equal(mcqDetail([1], [0], undefined), null);
});

test('gridDetail : cases en trop et oubliées, avec étiquettes et ordre d\'affichage', () => {
  const labels = { Fx: 'X', Mx: 'L', Fy: 'Y' };
  assert.equal(gridDetail(['Fx', 'Mx'], ['Fy', 'Mx'], labels, ['Fx', 'Mx', 'Fy']), 'Coché(s) à tort : X · Oublié(s) : Y');
  assert.equal(gridDetail(['Tx'], ['Tx', 'Rx']), 'Oublié(s) : Rx');
  assert.equal(gridDetail(['Tx', 'Ty'], ['Tx']), 'Coché(s) à tort : Ty');
  assert.equal(gridDetail(['Tx'], ['Tx']), null);
  assert.equal(gridDetail([], []), null);
});

test('orderDetail : première étape mal placée', () => {
  assert.equal(orderDetail([1, 0, 2], ['A', 'B', 'C']), 'L\'étape n°1 devait être : A');
  assert.equal(orderDetail([0, 2, 1], ['A', 'B', 'C']), 'L\'étape n°2 devait être : B');
  assert.equal(orderDetail([0, 1, 2], ['A', 'B', 'C']), null);
});
