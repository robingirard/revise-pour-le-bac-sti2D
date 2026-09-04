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
  const items = JSON.parse(await b.evaluate('JSON.stringify(Object.values(window.CONTENT.items).map((i) => ({ id: i.id, type: i.type, skill: i.skill, layout: i.payload.layout, labels: !!i.payload.labels, tags: i.tags || [] })))'));
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

  // Bilan parent : on enrichit l'historique et quelques items ratés, puis captures
  const firstItems = items.filter((i) => i.tags.length).slice(0, 6).map((i) => i.id); // items étiquetés : les points faibles ont un nom
  await b.evaluate(`(() => { const p = JSON.parse(localStorage.getItem('revise-sti2d.progress.v1')); p.settings.name = 'Tom';
    const d = new Date(); const day = (n) => { const x = new Date(d); x.setDate(d.getDate() - n); return x.toISOString().slice(0, 10); };
    const sk = ${JSON.stringify(skills.slice(0, 3).map((s) => s.id))};
    p.history = [6, 5, 4, 2, 1, 0].map((n, i) => ({ date: day(n), kind: i === 3 ? 'review' : 'skill', skill: i === 3 ? null : sk[i % sk.length], correct: 5 + i, total: 10, xp: 20 + 2 * i })).concat(p.history);
    for (const [k, id] of ${JSON.stringify(firstItems)}.entries()) p.items[id] = { reps: 0, ease: 2.1, interval: 0, due: day(0), lapses: 1 + (k % 3), last: day(k % 2) };
    localStorage.setItem('revise-sti2d.progress.v1', JSON.stringify(p)); })()`);
  await b.goto('#/progress'); await b.reload(); await b.shot('50-progres-bilan', true);
  await b.goto('#/bilan'); await b.shot('51-bilan', true);
  await b.goto('#/progress'); // la carte Bilan (et son lien mailto) est sur l'écran Progrès
  const link = await b.evaluate(`(() => { const a = document.querySelector('.bilan-card a[href^="mailto:"]'); const body = decodeURIComponent(a.getAttribute('href').split('body=')[1] || ''); const i = body.indexOf('#/bilan?d='); return i < 0 ? null : body.slice(i).trim(); })()`);
  await b.goto(link.slice(link.indexOf('#'))); await b.shot('52-bilan-recu', true);
  // QCM répondu faux exprès (un item avec feedback si possible), grille fausse exprès
  const mcqFb = await b.evaluate(`(() => { const it = Object.values(window.CONTENT.items).find((i) => i.type === 'mcq' && i.payload.layout !== 'grid' && Array.isArray(i.payload.feedback) && i.payload.feedback.some(Boolean)) || Object.values(window.CONTENT.items).find((i) => i.type === 'mcq' && i.payload.layout !== 'grid'); return it ? JSON.stringify({ id: it.id, skill: it.skill }) : null; })()`);
  if (mcqFb) {
    const it = JSON.parse(mcqFb);
    await b.goto(`#/session/${it.skill}?item=${encodeURIComponent(it.id)}&seed=1`);
    await b.evaluate(`(() => { const it = window.CONTENT.items[${JSON.stringify(it.id)}]; const plain = (s) => String(s).replace(/\\*\\*|\\*/g, '').replace(/\\s+/g, ' ').trim();
      const ok = new Set(it.payload.answer.map((i) => plain(it.payload.choices[i])));
      const btn = [...document.querySelectorAll('.choice')].find((b) => !ok.has(b.textContent.replace(/\\s+/g, ' ').trim())); btn.click(); })()`);
    await b.click('.btn-verify'); await b.shot('53-mcq-feedback-erreur', true);
  }
  const gridIt = items.find((i) => i.type === 'grid');
  if (gridIt) {
    await b.goto(`#/session/${gridIt.skill}?item=${encodeURIComponent(gridIt.id)}&seed=1`);
    await b.evaluate(`(() => { const it = window.CONTENT.items[${JSON.stringify(gridIt.id)}]; const ans = new Set(it.payload.answer);
      const inputs = [...document.querySelectorAll('.grid-table input')]; const wrong = inputs.find((i) => !ans.has(i.dataset.cell || i.getAttribute('aria-label')));
      if (wrong) wrong.click(); })()`);
    await b.click('.btn-verify'); await b.shot('54-grid-erreur', true);
  }
  await b.goto('#/settings'); await b.shot('56-reglages', true);

  // Exercices complets (guided) et annales, s'il y en a dans le contenu
  const guided = items.find((i) => i.type === 'guided');
  if (guided) {
    await b.evaluate(`(() => { const p = JSON.parse(localStorage.getItem('revise-sti2d.progress.v1')); p.skills[${JSON.stringify(guided.skill)}] = { level: 2, progress: 0, sessions: 4, xp: 40 }; localStorage.setItem('revise-sti2d.progress.v1', JSON.stringify(p)); })()`);
    await b.goto(`#/skill/${guided.skill}`); await b.reload(); await b.shot('60-skill-complets', true);
    await b.goto(`#/session/${guided.skill}?item=${encodeURIComponent(guided.id)}&seed=1`); await b.shot('61-guided-step1', true);
    await b.evaluate(SOLVER);
    for (let i = 0; i < 12; i++) {
      const r = await b.evaluate('window.__solve()');
      if (!r.startsWith('guided:')) throw new Error('exercice complet : ' + r);
      await sleep(150);
      if (i === 0) await b.shot('62-guided-feedback', true);
      await b.click('.btn-next-step'); await sleep(150);
      if (await b.evaluate('!!document.querySelector(".btn-continue")')) break;
    }
    await b.shot('63-guided-end', true);
  } else {
    console.log('aucun exercice complet (guided) dans le contenu : captures 60-63 sautées');
  }
  if (await b.evaluate('Array.isArray(window.CONTENT.annales) && window.CONTENT.annales.length > 0')) {
    await b.goto('#/'); await b.shot('70-home-annales', true);
  } else {
    console.log('aucune annale dans le contenu : capture 70 sautée');
  }
  const errors = await b.evaluate('document.querySelectorAll(".error").length');
  console.log(`OK — ${steps} exercices joués dans la séance « ${target.id} » ; captures dans ${OUT} ; éléments .error : ${errors}`);
} finally {
  await b.close();
}
