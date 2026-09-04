// tour.mjs — parcours générique de l'application avec le contenu CONSTRUIT (dist/) :
// accueil, chaque compétence (leçon dépliée), un exercice de chaque type avec sa correction,
// puis une séance complète jouée par le solveur. Sert à vérifier visuellement le vrai contenu.
// Usage : node app/dev/tour.mjs [dossier_dist] [dossier_de_sortie]   (Google Chrome requis)
import path from 'node:path';
import { launch, SOLVER, sleep } from './browser.mjs';

const HERE = path.dirname(new URL(import.meta.url).pathname);
const DIR = path.resolve(process.argv[2] || path.join(HERE, '..', '..', 'dist'));
const OUT = path.resolve(process.argv[3] || path.join(HERE, 'shots-tour'));
const b = await launch({ dir: DIR, out: OUT });
const today = new Date().toISOString().slice(0, 10);

try {
  await b.goto('#/');
  const skills = JSON.parse(await b.evaluate('JSON.stringify(window.CONTENT.units.flatMap((u) => u.skills.map((s) => ({ id: s.id, items: s.items }))))'));
  const items = JSON.parse(await b.evaluate('JSON.stringify(Object.values(window.CONTENT.items).map((i) => ({ id: i.id, type: i.type, skill: i.skill, layout: i.payload.layout, labels: !!i.payload.labels })))'));
  // progression : tout déverrouillé (niveau 1), aucune carte vue
  await b.evaluate(`localStorage.setItem('revise-sti2d.progress.v1', JSON.stringify({ version: 1, xp: 42, streak: { count: 2, last: '${today}' }, history: [],
    settings: { dailyGoal: 30 }, items: {}, skills: ${JSON.stringify(Object.fromEntries(skills.map((s) => [s.id, { level: 1, progress: 0.5, sessions: 2, xp: 20 }])))} }))`);
  await b.reload();
  await b.shot('01-home', true);
  for (const s of skills) {
    await b.goto(`#/skill/${s.id}`);
    await b.evaluate('document.querySelector("details.lesson") && (document.querySelector("details.lesson").open = true)');
    await sleep(150);
    await b.shot(`02-skill-${s.id}`, true);
  }
  // un exercice de chaque « forme » : premier item correspondant, capture avant et après correction
  const wanted = [
    ['mcq-liste', (i) => i.type === 'mcq' && i.layout !== 'grid'],
    ['mcq-grille', (i) => i.type === 'mcq' && i.layout === 'grid'],
    ['flashcard', (i) => i.type === 'flashcard'],
    ['match', (i) => i.type === 'match'],
    ['grid-ddl', (i) => i.type === 'grid' && !i.labels],
    ['grid-efforts', (i) => i.type === 'grid' && i.labels],
    ['order', (i) => i.type === 'order'],
    ['input', (i) => i.type === 'input'],
  ];
  let n = 10;
  for (const [name, pred] of wanted) {
    const it = items.find(pred);
    if (!it) { console.log('aucun item pour', name); continue; }
    await b.goto(`#/session/${it.skill}?item=${encodeURIComponent(it.id)}&seed=1`);
    await b.shot(`${n}-${name}`, true);
    await b.evaluate(SOLVER);
    const res = await b.evaluate('window.__solve()');
    if (res.startsWith('item-not-found') || res.startsWith('unknown')) throw new Error(`${name}: ${res}`);
    await sleep(200);
    await b.shot(`${n}-${name}-corrige`, true);
    n += 1;
  }
  // séance complète sur la première compétence ayant des figures dans ses exercices
  const target = skills.find((s) => s.id === 'symboles') || skills[0];
  await b.goto(`#/session/${target.id}?seed=3`);
  await b.evaluate(SOLVER);
  let steps = 0;
  for (let i = 0; i < 60; i++) {
    const res = await b.evaluate('window.__solve()');
    if (res === 'no-exercise') break;
    if (res.startsWith('item-not-found') || res.startsWith('unknown')) throw new Error(res);
    steps += 1;
    await sleep(100);
    await b.click('.btn-continue');
    await sleep(100);
    if (await b.evaluate('location.hash') === '#/summary') break;
  }
  if (await b.evaluate('location.hash') !== '#/summary') throw new Error('séance non terminée');
  await b.shot('30-bilan');
  await b.goto('#/'); await b.shot('31-accueil-apres', true);
  await b.goto('#/progress'); await b.shot('40-progres', true);
  const errors = await b.evaluate('document.querySelectorAll(".error").length');
  console.log(`OK — ${steps} exercices joués dans la séance « ${target.id} » ; captures dans ${OUT} ; éléments .error : ${errors}`);
} finally {
  await b.close();
}
