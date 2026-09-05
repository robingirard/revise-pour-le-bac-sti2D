import { test } from 'node:test';
import assert from 'node:assert/strict';
import * as packs from '../js/packs.js';

/** Index tel que le produit build_content.py : fiches sans id ni skill, leçons hors de l'index. */
function indexFactice() {
  return {
    units: [
      { id: 'liaisons', title: 'Liaisons', skills: [{ id: 'symboles', title: 'Symboles', items: ['symboles.a', 'symboles.b'] }] },
      { id: 'maths', title: 'Maths', skills: [{ id: 'suites', title: 'Suites', items: ['suites.a'] }] },
    ],
    items: {
      'symboles.a': { type: 'mcq', level: 1, tags: ['pivot'] },
      'symboles.b': { type: 'guided', level: 2 },
      'suites.a': { type: 'input', level: 1 },
    },
  };
}

/** Injection factice : retient les URL demandées et livre le paquet comme le ferait le script. */
function injecteur(paquets) {
  const demandes = [];
  const inject = (url) => {
    demandes.push(url);
    const id = url.replace('content/', '').replace('.js', '');
    if (!(id in paquets)) return Promise.reject(new Error(`Contenu introuvable : ${url}`));
    globalThis.REVISE_UNIT(id, paquets[id]);
    return Promise.resolve();
  };
  return { demandes, inject };
}

test('configure recolle l\'identifiant et la compétence sur chaque fiche', () => {
  const content = indexFactice();
  packs.configure({ content, inject: () => Promise.resolve() });
  assert.equal(content.items['symboles.a'].id, 'symboles.a');
  assert.equal(content.items['symboles.a'].skill, 'symboles');
  assert.equal(content.items['suites.a'].skill, 'suites');
  assert.equal(packs.unitOf('symboles'), 'liaisons');
  assert.equal(packs.unitOfItem('suites.a'), 'maths');
  assert.equal(packs.unitOf('inconnue'), null);
});

test('charger une unité complète les fiches sans perdre id ni compétence', async () => {
  const content = indexFactice();
  const { inject } = injecteur({
    liaisons: { items: { 'symboles.a': { type: 'mcq', level: 1, payload: { prompt: 'Quelle liaison ?' } } },
                lessons: { symboles: '# Les symboles' } },
  });
  packs.configure({ content, inject });

  assert.equal(packs.hasPayload('symboles.a'), false);
  assert.equal(packs.lessonOf('symboles'), null);
  await packs.load('liaisons');
  assert.equal(packs.hasPayload('symboles.a'), true);
  assert.equal(content.items['symboles.a'].payload.prompt, 'Quelle liaison ?');
  assert.equal(content.items['symboles.a'].id, 'symboles.a');
  assert.equal(content.items['symboles.a'].skill, 'symboles');
  assert.equal(packs.lessonOf('symboles'), '# Les symboles');
  assert.equal(packs.isLoaded('liaisons'), true);
  assert.equal(packs.isLoaded('maths'), false);
});

test('une unité n\'est demandée qu\'une fois, même en cas d\'appels simultanés', async () => {
  const content = indexFactice();
  const { demandes, inject } = injecteur({ liaisons: { items: {}, lessons: {} } });
  packs.configure({ content, inject });
  await Promise.all([packs.load('liaisons'), packs.load('liaisons')]);
  await packs.load('liaisons');
  assert.deepEqual(demandes, ['content/liaisons.js']);
});

test('loadForItems dédoublonne les unités et ignore les exercices inconnus', async () => {
  const content = indexFactice();
  const { demandes, inject } = injecteur({ liaisons: { items: {} }, maths: { items: {} } });
  packs.configure({ content, inject });
  await packs.loadForItems(['symboles.a', 'symboles.b', 'suites.a', 'inexistant']);
  assert.deepEqual(demandes.sort(), ['content/liaisons.js', 'content/maths.js']);
});

test('une unité absente remonte une erreur lisible', async () => {
  const content = indexFactice();
  const { inject } = injecteur({});
  packs.configure({ content, inject });
  await assert.rejects(() => packs.load('liaisons'), /Contenu introuvable/);
});
