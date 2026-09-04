// home.test.mjs — regroupement par matière et état des sections de l'accueil
import test from 'node:test';
import assert from 'node:assert/strict';
import * as home from '../js/home.js';
import { MemoryStorage } from './helpers.mjs';

const content = {
  units: [
    { id: 'u-ing', matiere: 'ingenierie', skills: [{ id: 'a' }, { id: 'b' }] },
    { id: 'u-maths', matiere: 'maths', skills: [{ id: 'm1' }] },
    { id: 'u-sans', skills: [{ id: 'c' }] },                 // matière absente → ingénierie
    { id: 'u-pc', matiere: 'physique', skills: [{ id: 'p1' }, { id: 'p2' }, { id: 'p3' }] },
    { id: 'u-bizarre', matiere: 'histoire', skills: [{ id: 'd' }] }, // matière inconnue → ingénierie
  ],
};

test('groupUnitsBySubject : ordre des matières, comptes, repli sur ingénierie', () => {
  const groups = home.groupUnitsBySubject(content);
  assert.deepEqual(groups.map((g) => g.id), ['ingenierie', 'physique', 'maths']);
  assert.deepEqual(groups[0].units.map((u) => u.id), ['u-ing', 'u-sans', 'u-bizarre']);
  assert.equal(groups[0].skillCount, 4);
  assert.equal(groups[1].skillCount, 3);
  assert.equal(groups[2].skillCount, 1);
  assert.equal(groups[0].label, 'Ingénierie 2I2D');
});

test('groupUnitsBySubject : les matières sans unité sont omises, contenu vide → aucun groupe', () => {
  const groups = home.groupUnitsBySubject({ units: [{ id: 'x', matiere: 'maths', skills: [] }] });
  assert.deepEqual(groups.map((g) => g.id), ['maths']);
  assert.deepEqual(home.groupUnitsBySubject({}), []);
  assert.deepEqual(home.groupUnitsBySubject(null), []);
});

test('reachedCount : compétences au niveau ≥ 1', () => {
  const [ing, pc] = home.groupUnitsBySubject(content);
  const progress = { skills: { a: { level: 2 }, b: { level: 0 }, c: { level: 1 }, p1: { level: 1 } } };
  assert.equal(home.reachedCount(ing, progress), 2);
  assert.equal(home.reachedCount(pc, progress), 1);
  assert.equal(home.reachedCount(pc, null), 0);
});

test('subjectOfSkill et groupSkillRows : en-têtes seulement s\'il y a plusieurs groupes, inconnus à la fin', () => {
  assert.equal(home.subjectOfSkill('m1', content), 'maths');
  assert.equal(home.subjectOfSkill('c', content), 'ingenierie');
  assert.equal(home.subjectOfSkill('zzz', content), null);
  const rows = [{ id: 'm1' }, { id: 'a' }, { id: 'zzz' }, { id: 'p2' }];
  const groups = home.groupSkillRows(rows, content);
  assert.deepEqual(groups.map((g) => [g.id, g.rows.map((r) => r.id), g.header]),
    [['ingenierie', ['a'], true], ['physique', ['p2'], true], ['maths', ['m1'], true], ['autres', ['zzz'], true]]);
  // bilan reçu sans correspondance dans le contenu : un seul groupe, sans en-tête
  const alone = home.groupSkillRows([{ id: 'q1' }, { id: 'q2' }], content);
  assert.equal(alone.length, 1);
  assert.equal(alone[0].header, false);
  assert.deepEqual(alone[0].rows.map((r) => r.id), ['q1', 'q2']);
  // pas de contenu du tout
  assert.equal(home.groupSkillRows([{ id: 'a' }], null)[0].id, 'autres');
});

test('état des sections : tout déplié par défaut, bascule immuable, persistance', () => {
  const st = home.defaultUiState();
  assert.equal(home.isExpanded(st, 'maths'), true);
  const collapsed = home.toggleSection(st, 'maths');
  assert.equal(home.isExpanded(collapsed, 'maths'), false);
  assert.equal(home.isExpanded(st, 'maths'), true, 'l\'état initial n\'est pas modifié');
  assert.equal(home.isExpanded(home.toggleSection(collapsed, 'maths'), 'maths'), true);
  assert.equal(home.isExpanded(home.toggleSection(collapsed, 'maths', false), 'maths'), false, 'forçage');
  const storage = new MemoryStorage();
  assert.equal(home.saveUiState(collapsed, storage), true);
  const loaded = home.loadUiState(storage);
  assert.equal(home.isExpanded(loaded, 'maths'), false);
  assert.equal(home.isExpanded(loaded, 'physique'), true);
});

test('état des sections : stockage absent, corrompu ou en erreur → état par défaut', () => {
  assert.deepEqual(home.loadUiState(null), { collapsed: {} });
  const bad = new MemoryStorage();
  bad.setItem(home.UI_KEY, '{not json');
  assert.deepEqual(home.loadUiState(bad), { collapsed: {} });
  bad.setItem(home.UI_KEY, JSON.stringify({ collapsed: 'oui' }));
  assert.deepEqual(home.loadUiState(bad), { collapsed: {} });
  const throwing = { getItem() { throw new Error('quota'); }, setItem() { throw new Error('quota'); } };
  assert.deepEqual(home.loadUiState(throwing), { collapsed: {} });
  assert.equal(home.saveUiState({ collapsed: { maths: true } }, throwing), false);
  assert.equal(home.saveUiState({ collapsed: {} }, null), false);
});
