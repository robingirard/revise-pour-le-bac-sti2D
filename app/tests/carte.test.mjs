import { test } from 'node:test';
import assert from 'node:assert/strict';
import {
  FORMAT, VERSION, LIMITE_LIEN, build, toJson, parse, nomDeFichier, versLien, depuisLien,
  compacter, etendre,
} from '../js/carte.js';
import { MASTERED_INTERVAL, isMastered } from '../js/scheduler.js';

/** Progression telle que store.exportJson la produit. */
function progressionFactice(nbItems = 3) {
  const items = {};
  for (let i = 0; i < nbItems; i++) {
    items[`symboles.gen_${i}.pivot.bout`] = {
      reps: i % 5, ease: 2.5 - (i % 7) * 0.1, interval: (i * 3) % 21,
      due: `2026-09-${String((i % 28) + 1).padStart(2, '0')}`, lapses: i % 4,
      last: `2026-08-${String((i % 28) + 1).padStart(2, '0')}`,
    };
  }
  return {
    version: 1, items, skills: { symboles: { level: 2, progress: 0.4, sessions: 6, xp: 120 } },
    xp: 420, streak: { count: 3, last: '2026-09-05' },
    history: [{ date: '2026-09-05', kind: 'skill', skill: 'symboles', correct: 7, total: 8 }],
    settings: { dailyGoal: 30, name: 'Tom' },
  };
}

const profil = { nom: 'Tom', emoji: '🚴' };

test('aller-retour build → toJson → parse', () => {
  const progres = progressionFactice();
  const carte = build(profil, progres, '2026-09-05');
  assert.equal(carte.format, FORMAT);
  assert.equal(carte.version, VERSION);
  assert.equal(carte.genere, '2026-09-05');

  const relu = parse(toJson(carte));
  assert.deepEqual(relu.profil, profil);
  assert.deepEqual(relu.progres, progres);
});

test('toJson reste lisible : indenté et terminé par une ligne', () => {
  const texte = toJson(build(profil, progressionFactice(), '2026-09-05'));
  assert.ok(texte.includes('\n  "format": "revise.carte"'));
  assert.ok(texte.endsWith('\n'));
});

test('le profil est nettoyé, et absent quand il n\'y a rien à retenir', () => {
  const long = build({ nom: `  ${'a'.repeat(80)}  `, emoji: '🚴' }, {}, '2026-09-05');
  assert.equal(long.profil.nom.length, 40);
  assert.equal(build(null, {}, '2026-09-05').profil, null);
  assert.equal(build({ nom: '   ' }, {}, '2026-09-05').profil, null);
});

test('aller-retour versLien → depuisLien', async () => {
  const carte = build(profil, progressionFactice(20), '2026-09-05');
  const { url, octets, tient } = await versLien(carte, 'https://exemple.fr/revise/');
  assert.ok(url.startsWith('https://exemple.fr/revise/#/carte?d='));
  assert.ok(tient, `une petite carte doit tenir dans un lien (${octets} octets)`);
  assert.equal(octets, url.length);

  const relu = await depuisLien(url);
  assert.deepEqual(relu.profil, profil);
  assert.deepEqual(relu.progres, carte.progres);
  assert.equal(relu.genere, '2026-09-05');
});

test('depuisLien accepte l\'URL entière, le fragment seul ou la valeur encodée', async () => {
  const carte = build(profil, progressionFactice(5), '2026-09-05');
  const { url } = await versLien(carte, 'https://exemple.fr/revise/');
  const fragment = url.slice(url.indexOf('#'));
  const encode = url.slice(url.indexOf('d=') + 2);
  for (const entree of [url, fragment, encode]) {
    assert.deepEqual((await depuisLien(entree)).progres, carte.progres);
  }
});

test('une progression volumineuse ne tient pas dans un lien', async () => {
  const carte = build(profil, progressionFactice(2058), '2026-09-05');   // tout le contenu parcouru
  const { url, octets, tient } = await versLien(carte, 'https://robingirard.github.io/revise-pour-le-bac-sti2D/');
  assert.equal(tient, false);
  assert.ok(octets > LIMITE_LIEN, `${octets} octets attendus au-dessus de ${LIMITE_LIEN}`);
  // le lien reste techniquement lisible : c'est la taille, pas le contenu, qui le disqualifie
  assert.deepEqual((await depuisLien(url)).progres, carte.progres);
});

test('un ancien export de progression nue se relit sans profil', () => {
  const progres = progressionFactice();
  const relu = parse(JSON.stringify(progres, null, 2));   // exactement store.exportJson
  assert.equal(relu.profil, null);
  assert.deepEqual(relu.progres, progres);
});

test('parse refuse proprement, avec un message lisible', () => {
  assert.throws(() => parse('pas du json'), /n'est pas du JSON valide/);
  assert.throws(() => parse('[]'), /ne contient pas une carte/);
  assert.throws(() => parse('{"a":1}'), /ni une carte d'identité ni une progression/);
  assert.throws(
    () => parse(JSON.stringify({ format: FORMAT, version: VERSION + 1, progres: {} })),
    /version plus récente/,
  );
  assert.throws(
    () => parse(JSON.stringify({ format: FORMAT, version: VERSION })),
    /ne contient aucune progression/,
  );
  assert.throws(
    () => parse(JSON.stringify({ format: FORMAT, version: 'x', progres: {} })),
    /n'indique pas sa version/,
  );
});

test('depuisLien refuse proprement', async () => {
  await assert.rejects(() => depuisLien(''), /Ce lien est vide/);
  await assert.rejects(() => depuisLien('https://exemple.fr/#/carte'), /il manque la partie/);
  await assert.rejects(() => depuisLien('#/carte?d=!!!!'), /il manque la partie/);
  await assert.rejects(() => depuisLien('#/carte?d=AAAAAAAA'), /abîmé/);
});

test('nomDeFichier : prénom accentué, et repli quand il n\'y a pas de nom', () => {
  assert.equal(nomDeFichier(build({ nom: 'Chloé' }, {}, '2026-09-05')), 'revise-chloe-2026-09-05.json');
  assert.equal(nomDeFichier(build({ nom: 'Jean-Luc' }, {}, '2026-09-05')), 'revise-jean-luc-2026-09-05.json');
  assert.equal(nomDeFichier(build(null, {}, '2026-09-05')), 'revise-2026-09-05.json');
  assert.equal(nomDeFichier(build(null, {}, null)), 'revise.json');
});

// ---- compaction des chapitres refermés

/** Un exercice maîtrisé (intervalle long) et un en cours, pour éprouver les deux traitements. */
function progressionMixte() {
  return {
    version: 1,
    items: {
      'symboles.acquis': { reps: 6, ease: 2.7, interval: 34, due: '2026-10-12', lapses: 0, last: '2026-09-08' },
      'symboles.acquis-avec-rechutes': { reps: 5, ease: 1.9, interval: 21, due: '2026-09-30', lapses: 3, last: '2026-09-09' },
      'symboles.en-cours': { reps: 1, ease: 2.5, interval: 3, due: '2026-09-08', lapses: 1, last: '2026-09-05' },
      'symboles.jamais-vu': { reps: 0, ease: 2.5, interval: 0, due: null, lapses: 0, last: null },
    },
    skills: {}, xp: 100, streak: { count: 2, last: '2026-09-05' }, history: [], settings: {},
  };
}

test('compacter réduit les exercices maîtrisés et laisse les autres intacts', () => {
  const avant = progressionMixte();
  const apres = compacter(avant);
  assert.equal(apres.items['symboles.acquis'], '2026-10-12');
  assert.deepEqual(apres.items['symboles.acquis-avec-rechutes'], ['2026-09-30', 3]);
  assert.deepEqual(apres.items['symboles.en-cours'], avant.items['symboles.en-cours']);
  assert.deepEqual(apres.items['symboles.jamais-vu'], avant.items['symboles.jamais-vu']);
  assert.deepEqual(avant, progressionMixte(), 'compacter ne doit pas modifier son entrée');
  assert.equal(apres.xp, 100, 'le reste de la progression est conservé');
});

test('etendre rebâtit un état que le planificateur considère comme maîtrisé', () => {
  const rendu = etendre(compacter(progressionMixte()));
  const acquis = rendu.items['symboles.acquis'];
  assert.equal(acquis.due, '2026-10-12');
  assert.equal(acquis.interval, MASTERED_INTERVAL);
  assert.ok(isMastered(acquis), 'l\'exercice doit rester compté comme maîtrisé');
  assert.equal(acquis.lapses, 0);
  assert.equal(acquis.last, '2026-09-21', 'last + interval doit retomber sur due');
  assert.equal(rendu.items['symboles.acquis-avec-rechutes'].lapses, 3, 'les rechutes nourrissent le bilan');
  assert.deepEqual(rendu.items['symboles.en-cours'], progressionMixte().items['symboles.en-cours']);
});

test('compacter et etendre sont idempotents', () => {
  const c = compacter(progressionMixte());
  assert.deepEqual(compacter(c), c);
  const e = etendre(c);
  assert.deepEqual(etendre(e), e);
});

test('le fichier garde tout, seul le lien compacte', async () => {
  const carte = build(profil, progressionMixte(), '2026-09-05');
  // l'archive est fidèle : l'état complet de l'exercice maîtrisé s'y retrouve mot pour mot
  assert.deepEqual(parse(toJson(carte)).progres.items['symboles.acquis'],
    progressionMixte().items['symboles.acquis']);
  // le lien, lui, transporte la forme réduite — et rend une progression rejouable
  const { url } = await versLien(carte, 'https://exemple.fr/revise/');
  const relu = await depuisLien(url);
  assert.equal(relu.progres.items['symboles.acquis'].interval, MASTERED_INTERVAL);
  assert.equal(relu.progres.items['symboles.acquis'].due, '2026-10-12');
  assert.deepEqual(relu.progres.items['symboles.en-cours'], progressionMixte().items['symboles.en-cours']);
});

test('parse relit une carte déjà compactée', () => {
  const compactee = build(profil, compacter(progressionMixte()), '2026-09-05');
  const relu = parse(toJson(compactee));
  assert.equal(relu.progres.items['symboles.acquis'].interval, MASTERED_INTERVAL);
  assert.equal(relu.progres.items['symboles.acquis'].due, '2026-10-12');
});
