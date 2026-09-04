// helpers.mjs — contenu minimal partagé par les tests
export function makeContent() {
  const items = {};
  const add = (id, skill, level, type = 'mcq') => {
    items[id] = { id, skill, type, level, tags: [], payload: { prompt: id, choices: ['a', 'b'], answer: [0] } };
    return id;
  };
  const content = {
    version: 1, title: 'Test', figures: { f1: '<svg xmlns="http://www.w3.org/2000/svg"></svg>' },
    units: [
      { id: 'u1', title: 'U1', skills: [
        { id: 's1', title: 'S1', prerequisites: [], levels: 2, items: [] },
        { id: 's2', title: 'S2', prerequisites: ['s1'], levels: 3, items: [] },
      ] },
      { id: 'u2', title: 'U2', skills: [
        { id: 's3', title: 'S3', prerequisites: ['s1', 's2'], levels: 3, items: [] },
      ] },
    ],
    items,
  };
  const s1 = content.units[0].skills[0], s2 = content.units[0].skills[1], s3 = content.units[1].skills[0];
  for (let i = 1; i <= 8; i++) s1.items.push(add(`s1-l1-${i}`, 's1', 1));
  for (let i = 1; i <= 6; i++) s1.items.push(add(`s1-l2-${i}`, 's1', 2));
  for (let i = 1; i <= 25; i++) s2.items.push(add(`s2-l1-${i}`, 's2', 1));
  for (let i = 1; i <= 4; i++) s3.items.push(add(`s3-l1-${i}`, 's3', 1));
  return content;
}

export function makeProgress(overrides = {}) {
  return { version: 1, items: {}, skills: {}, xp: 0, streak: { count: 0, last: null }, history: [], settings: { dailyGoal: 30 }, ...overrides };
}

/** Faux localStorage. */
export class MemoryStorage {
  constructor() { this.map = new Map(); }
  getItem(k) { return this.map.has(k) ? this.map.get(k) : null; }
  setItem(k, v) { this.map.set(k, String(v)); }
  removeItem(k) { this.map.delete(k); }
}
