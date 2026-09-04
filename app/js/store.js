// store.js — persistance de la progression dans localStorage (voir docs/SPEC.md §8)
import { DEFAULT_DAILY_GOAL } from './progression.js';

export const STORAGE_KEY = 'revise-sti2d.progress.v1';
export const VERSION = 1;

export function emptyProgress() {
  return {
    version: VERSION,
    items: {},
    skills: {},
    xp: 0,
    streak: { count: 0, last: null },
    history: [],
    settings: { dailyGoal: DEFAULT_DAILY_GOAL },
  };
}

/** Complète les champs manquants (et migrera les anciennes versions). */
export function migrate(obj) {
  if (!obj || typeof obj !== 'object' || Array.isArray(obj)) throw new Error('Format de progression invalide.');
  const base = emptyProgress();
  const p = {
    ...base,
    ...obj,
    items: obj.items && typeof obj.items === 'object' ? obj.items : {},
    skills: obj.skills && typeof obj.skills === 'object' ? obj.skills : {},
    streak: { ...base.streak, ...(obj.streak || {}) },
    history: Array.isArray(obj.history) ? obj.history : [],
    settings: { ...base.settings, ...(obj.settings || {}) },
  };
  p.xp = Number(p.xp) || 0;
  p.version = VERSION;
  return p;
}

function defaultStorage() {
  try {
    return globalThis.localStorage || null;
  } catch {
    return null; // accès interdit (navigation privée stricte, etc.)
  }
}

export function load(storage = defaultStorage()) {
  try {
    const raw = storage && storage.getItem(STORAGE_KEY);
    return raw ? migrate(JSON.parse(raw)) : emptyProgress();
  } catch {
    return emptyProgress();
  }
}

export function save(progress, storage = defaultStorage()) {
  try {
    if (!storage) return false;
    storage.setItem(STORAGE_KEY, JSON.stringify(progress));
    return true;
  } catch {
    return false;
  }
}

export function reset(storage = defaultStorage()) {
  try {
    if (storage) storage.removeItem(STORAGE_KEY);
  } catch {
    /* ignoré */
  }
  return emptyProgress();
}

export function exportJson(progress) {
  return JSON.stringify(progress, null, 2);
}

/** Lit un export JSON ; lève une erreur lisible si le texte n'est pas une progression. */
export function importJson(text) {
  let obj;
  try {
    obj = JSON.parse(text);
  } catch {
    throw new Error('Ce texte n\'est pas du JSON valide.');
  }
  if (!obj || typeof obj !== 'object' || !('items' in obj) || !('skills' in obj)) {
    throw new Error('Ce JSON ne ressemble pas à une progression exportée.');
  }
  return migrate(obj);
}
