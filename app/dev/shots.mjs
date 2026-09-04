// shots.mjs — vérification visuelle automatisée : sert app/, pilote Chrome headless (CDP) et
// enregistre des captures d'écran de chaque écran / type d'exercice, puis joue une séance complète.
// Usage : node dev/shots.mjs [dossier_de_sortie]   (nécessite Google Chrome installé)
import path from 'node:path';
import { launch, SOLVER, sleep } from './browser.mjs';

const APP_DIR = path.resolve(new URL('..', import.meta.url).pathname);
const OUT = path.resolve(process.argv[2] || path.join(APP_DIR, 'dev', 'shots'));
const b = await launch({ dir: APP_DIR, out: OUT });
const { goto, reload, shot, click, evaluate } = b;

try {
  // Progression de départ : toutes les compétences déverrouillées, quelques items dus.
  await goto('#/');
  await evaluate(`localStorage.setItem('revise-sti2d.progress.v1', JSON.stringify({
    version: 1, xp: 128, streak: { count: 3, last: new Date().toISOString().slice(0, 10) },
    history: [{ date: new Date().toISOString().slice(0, 10), kind: 'skill', skill: 'liaisons-mobilites', correct: 8, total: 10, xp: 26 }],
    settings: { dailyGoal: 30 },
    skills: { 'liaisons-mobilites': { level: 1, progress: 0.5, sessions: 3, xp: 80 }, 'liaisons-symboles': { level: 1, progress: 0, sessions: 2, xp: 48 }, 'liaisons-ddl': { level: 1, progress: 0, sessions: 2, xp: 0 } },
    items: { 'mob-fc-1': { reps: 2, ease: 2.5, interval: 3, due: '2026-01-01', lapses: 0, last: '2025-12-29' }, 'mob-mcq-1': { reps: 1, ease: 2.5, interval: 1, due: '2026-01-01', lapses: 0, last: '2025-12-31' }, 'sym-mcq-1': { reps: 5, ease: 2.6, interval: 30, due: '2027-01-01', lapses: 0, last: '2026-01-01' } }
  }))`);
  await reload();
  await shot('01-home');
  await goto('#/skill/liaisons-symboles'); await shot('02-skill');
  await goto('#/skill/schema-demarche'); await shot('03-skill-locked');

  await goto('#/session/liaisons-mobilites?item=mob-mcq-1&seed=1'); await shot('10-mcq');
  await click('.choice', 1); await click('.btn-verify'); await shot('11-mcq-feedback');
  await goto('#/session/liaisons-symboles?item=sym-mcq-grid-1&seed=1'); await shot('12-mcq-grid');
  await goto('#/session/liaisons-mobilites?item=mob-fc-1&seed=1'); await shot('13-flashcard');
  await click('.exercise .btn-primary'); await shot('14-flashcard-back');
  await click('.grade-good'); await shot('15-flashcard-feedback');
  await goto('#/session/liaisons-symboles?item=sym-match-1&seed=2'); await shot('16-match');
  await click('.match-col:first-child .match-btn', 0); await shot('17-match-selected');
  await goto('#/session/liaisons-ddl?item=ddl-grid-1&seed=1'); await shot('18-grid');
  await click('input[aria-label="Rx"]'); await click('input[aria-label="Ty"]'); await click('.btn-verify'); await shot('19-grid-feedback');
  await goto('#/session/schema-demarche?item=dem-order-1&seed=1'); await shot('20-order');
  await click('.order-pool .choice', 0); await click('.order-pool .choice', 0); await shot('21-order-partial');
  await goto('#/session/liaisons-symboles?item=sym-input-1&seed=1');
  await evaluate(`(() => { const i = document.querySelector('.text-input'); i.value = 'helicoidale'; i.dispatchEvent(new Event('input')); })()`);
  await shot('22-input'); await click('.btn-verify'); await shot('23-input-feedback');

  // Séance complète jouée par le solveur → bilan
  await goto('#/session/liaisons-ddl?seed=4');
  await evaluate(SOLVER);
  for (let i = 0; i < 40; i++) {
    const res = await evaluate('window.__solve()');
    if (res === 'no-exercise') break;
    if (res.startsWith('item-not-found') || res.startsWith('unknown')) throw new Error(res);
    await sleep(100);
    await click('.btn-continue');
    await sleep(100);
    if (await evaluate('location.hash') === '#/summary') break;
  }
  const finalHash = await evaluate('location.hash');
  if (finalHash !== '#/summary') throw new Error(`séance non terminée (${finalHash})`);
  await shot('30-summary');
  await goto('#/review?seed=1'); await shot('31-review');
  await goto('#/progress'); await shot('40-progress');
  await goto('#/settings'); await shot('41-settings');

  // Bilan parent, détail d'erreur
  await evaluate(`(() => { const p = JSON.parse(localStorage.getItem('revise-sti2d.progress.v1')); p.settings.name = 'Tom';
    const d = new Date(); const day = (n) => { const x = new Date(d); x.setDate(d.getDate() - n); return x.toISOString().slice(0, 10); };
    p.history = [5, 4, 2, 1, 0].map((n, i) => ({ date: day(n), kind: i === 2 ? 'review' : 'skill', skill: i === 2 ? null : 'liaisons-mobilites', correct: 6 + i, total: 10, xp: 22 + 2 * i }));
    p.items['sym-mcq-grid-1'] = { reps: 0, ease: 2.1, interval: 0, due: day(0), lapses: 3, last: day(0) };
    p.items['ddl-grid-1'] = { reps: 0, ease: 2.3, interval: 0, due: day(1), lapses: 2, last: day(1) };
    localStorage.setItem('revise-sti2d.progress.v1', JSON.stringify(p)); })()`);
  await goto('#/progress'); await reload(); await shot('50-progres-bilan');
  await goto('#/bilan'); await shot('51-bilan');
  await goto('#/progress'); // la carte Bilan (et son lien mailto) est sur l'écran Progrès
  const link = await evaluate(`(() => { const a = document.querySelector('.bilan-card a[href^="mailto:"]'); const body = decodeURIComponent(a.getAttribute('href').split('body=')[1] || ''); const i = body.indexOf('#/bilan?d='); return i < 0 ? null : body.slice(i).trim(); })()`);
  await goto(link.slice(link.indexOf('#'))); await shot('52-bilan-recu');
  await goto('#/bilan?d=pasunbilan'); await shot('52b-bilan-invalide');
  await goto('#/session/liaisons-mobilites?item=mob-mcq-3&seed=1');
  await evaluate(`(() => { const btns = [...document.querySelectorAll('.choice')]; btns.find((b) => b.textContent.trim() === 'Tz').click(); })()`);
  await click('.btn-verify'); await shot('53-mcq-feedback-erreur');
  await goto('#/session/liaisons-ddl?item=ddl-grid-1&seed=1');
  await click('input[aria-label="Tx"]'); await click('input[aria-label="Ry"]'); await click('.btn-verify'); await shot('54-grid-erreur');
  await goto('#/session/liaisons-symboles?item=sym-match-1&seed=2');
  await evaluate(`(() => { const cols = document.querySelectorAll('.match-col'); cols[0].querySelectorAll('.match-btn')[0].click(); const r = [...cols[1].querySelectorAll('.match-btn')]; r[r.length - 1].click(); })()`);
  await shot('55-match-erreur-flash');
  await goto('#/settings'); await shot('56-settings');
  const errors = await evaluate('document.querySelectorAll(".error").length');
  console.log('OK — captures dans', OUT, '; éléments .error visibles :', errors);
} finally {
  await b.close();
}
