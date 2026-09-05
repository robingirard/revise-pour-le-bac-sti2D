import { test } from 'node:test';
import assert from 'node:assert/strict';
import * as prof from '../js/profiles.js';
import { load, save, use, activeKey, progressKey, emptyProgress, STORAGE_KEY } from '../js/store.js';
import { MemoryStorage } from './helpers.mjs';

/** Stockage qui refuse tout, comme en navigation privée stricte. */
class StockageInterdit {
  getItem() { throw new Error('accès refusé'); }
  setItem() { throw new Error('accès refusé'); }
  removeItem() { throw new Error('accès refusé'); }
}

test('création : identifiant lisible, emoji par défaut, premier profil courant', () => {
  const st = new MemoryStorage();
  assert.deepEqual(prof.list(st), []);
  assert.equal(prof.current(st), null);

  const tom = prof.create({ nom: '  Tom  ' }, st, '2026-09-05');
  assert.match(tom.id, /^tom-[0-9a-z]+$/);
  assert.equal(tom.nom, 'Tom');
  assert.equal(tom.emoji, prof.EMOJI_DEFAUT);
  assert.equal(tom.cree, '2026-09-05');
  assert.equal(tom.vu, null);
  assert.equal(prof.current(st), tom.id);

  const lea = prof.create({ nom: 'Léa', emoji: '🦊' }, st, '2026-09-05');
  assert.match(lea.id, /^lea-/, 'l\'identifiant est sans accent');
  assert.equal(lea.emoji, '🦊');
  assert.equal(prof.current(st), tom.id, 'créer un second profil ne change pas de courant');
  assert.deepEqual(prof.list(st).map((p) => p.nom), ['Tom', 'Léa']);
});

test('deux prénoms identiques donnent deux profils distincts', () => {
  const st = new MemoryStorage();
  const a = prof.create({ nom: 'Tom' }, st, '2026-09-05');
  const b = prof.create({ nom: 'Tom' }, st, '2026-09-05');
  assert.notEqual(a.id, b.id);
  assert.equal(prof.list(st).length, 2);
});

test('un prénom vide est refusé, un prénom sans lettre reste utilisable', () => {
  const st = new MemoryStorage();
  assert.throws(() => prof.create({ nom: '   ' }, st), /prénom ne peut pas être vide/);
  assert.throws(() => prof.create({}, st), /prénom ne peut pas être vide/);
  const emoji = prof.create({ nom: '🐧' }, st, '2026-09-05');
  assert.match(emoji.id, /^eleve-/, 'un prénom sans lettre latine retombe sur « eleve »');
});

test('renommer garde l\'identifiant, donc la progression', () => {
  const st = new MemoryStorage();
  const p = prof.create({ nom: 'Tom' }, st, '2026-09-05');
  const renomme = prof.rename(p.id, { nom: 'Thomas', emoji: '🚀' }, st);
  assert.equal(renomme.id, p.id);
  assert.equal(renomme.nom, 'Thomas');
  assert.equal(renomme.emoji, '🚀');
  assert.equal(prof.rename('inconnu', { nom: 'X' }, st), null);
  assert.throws(() => prof.rename(p.id, { nom: '' }, st), /vide/);
});

test('changer de profil ; un identifiant inconnu est ignoré', () => {
  const st = new MemoryStorage();
  const a = prof.create({ nom: 'Tom' }, st, '2026-09-05');
  const b = prof.create({ nom: 'Léa' }, st, '2026-09-05');
  assert.equal(prof.setCurrent(b.id, st), b.id);
  assert.equal(prof.current(st), b.id);
  assert.equal(prof.setCurrent('nawak', st), b.id);
  assert.equal(prof.current(st), b.id);
  assert.equal(prof.currentProfile(st).nom, 'Léa');
  assert.equal(prof.get(a.id, st).nom, 'Tom');
  assert.equal(prof.get('nawak', st), null);
});

test('supprimer un profil efface sa progression et bascule le courant', () => {
  const st = new MemoryStorage();
  const a = prof.create({ nom: 'Tom' }, st, '2026-09-05');
  const b = prof.create({ nom: 'Léa' }, st, '2026-09-05');
  use(a.id);
  save({ ...emptyProgress(), xp: 120 }, st);
  assert.equal(st.getItem(progressKey(a.id)) !== null, true);

  assert.equal(prof.remove(a.id, st), b.id, 'le courant bascule sur celui qui reste');
  assert.equal(st.getItem(progressKey(a.id)), null, 'la progression part avec le profil');
  assert.deepEqual(prof.list(st).map((p) => p.nom), ['Léa']);

  assert.equal(prof.remove(b.id, st), null, 'plus aucun profil courant');
  assert.deepEqual(prof.list(st), []);
  assert.equal(prof.remove('inconnu', st), null);
  use(null);
});

test('touch note la date de dernière séance', () => {
  const st = new MemoryStorage();
  const p = prof.create({ nom: 'Tom' }, st, '2026-09-05');
  assert.equal(prof.touch(p.id, '2026-09-06', st).vu, '2026-09-06');
  assert.equal(prof.list(st)[0].vu, '2026-09-06');
  assert.equal(prof.touch('inconnu', '2026-09-06', st), null);
});

test('migration : la progression d\'avant les profils est recopiée, jamais détruite', () => {
  const st = new MemoryStorage();
  const ancienne = { ...emptyProgress(), xp: 250, settings: { dailyGoal: 30, name: 'Tom' } };
  st.setItem(STORAGE_KEY, JSON.stringify(ancienne));

  const p = prof.migrate('2026-09-05', st);
  assert.equal(p.nom, 'Tom', 'le prénom vient des réglages');
  assert.equal(st.getItem(STORAGE_KEY) !== null, true, 'l\'ancienne clé est conservée');
  use(p.id);
  assert.equal(load(st).xp, 250, 'la progression est bien celle du profil');
  use(null);

  assert.equal(prof.migrate('2026-09-06', st), null, 'migration idempotente');
  assert.equal(prof.list(st).length, 1);
});

test('migration : sans prénom, sans ancienne progression, ou sur un JSON abîmé', () => {
  const vide = new MemoryStorage();
  assert.equal(prof.migrate('2026-09-05', vide), null, 'rien à reprendre');
  assert.deepEqual(prof.list(vide), []);

  const sansNom = new MemoryStorage();
  sansNom.setItem(STORAGE_KEY, JSON.stringify(emptyProgress()));
  assert.equal(prof.migrate('2026-09-05', sansNom).nom, 'Élève');

  const casse = new MemoryStorage();
  casse.setItem(STORAGE_KEY, '{oops');
  const p = prof.migrate('2026-09-05', casse);
  assert.equal(p.nom, 'Élève');
  assert.equal(casse.getItem(progressKey(p.id)), '{oops', 'les octets sont recopiés tels quels');
  use(p.id);
  assert.deepEqual(load(casse), emptyProgress(), 'et relus comme une progression vide');
  use(null);
});

test('un stockage indisponible dégrade sans jamais lever', () => {
  const ko = new StockageInterdit();
  assert.deepEqual(prof.list(ko), []);
  assert.equal(prof.current(ko), null);
  assert.equal(prof.currentProfile(ko), null);
  assert.equal(prof.migrate('2026-09-05', ko), null);
  assert.equal(prof.setCurrent('x', ko), null);
  assert.doesNotThrow(() => prof.create({ nom: 'Tom' }, ko, '2026-09-05'));
  assert.deepEqual(prof.list(null), []);
  assert.equal(prof.migrate('2026-09-05', null), null);
});

test('la clé active suit le profil choisi', () => {
  const st = new MemoryStorage();
  use(null);
  assert.equal(activeKey(), STORAGE_KEY);
  const p = prof.create({ nom: 'Tom' }, st, '2026-09-05');
  use(p.id);
  assert.equal(activeKey(), `revise.progres.${p.id}.v1`);

  save({ ...emptyProgress(), xp: 7 }, st);
  assert.equal(load(st).xp, 7);
  use(null);
  assert.equal(load(st).xp, 0, 'l\'ancienne clé est bien un autre casier');
});
