// Banc d'animation : capture des figures animées données (ids séparés par des virgules) à quatre instants.
// Usage : node app/dev/mech-bench.mjs mecanisme-pompe-a-main-schema,transmission-poulies <dossier de sortie>
// Construit un site minimal (liens symboliques vers dist/) autour de dev/mech-bench.html, puis lance Chrome headless.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launch, sleep } from './browser.mjs';
const HERE = path.dirname(fileURLToPath(import.meta.url));
const DIST = path.resolve(HERE, '..', '..', 'dist');
const [ids, OUT] = [process.argv[2], process.argv[3] || path.join(HERE, 'shots-bench')];
const site = fs.mkdtempSync(path.join(os.tmpdir(), 'mech-bench-'));
for (const d of ['js', 'figures', 'css', 'content.js']) fs.symlinkSync(path.join(DIST, d), path.join(site, d));
fs.copyFileSync(path.join(HERE, 'mech-bench.html'), path.join(site, 'index.html'));
const b = await launch({ dir: site, out: OUT, width: 430, height: 1400 });
const { goto, shot, evaluate } = b;
try {
  await goto('?ids=' + ids);
  for (let i = 0; i < 30 && !(await evaluate('window.ready === true')); i++) await sleep(200);
  console.log('svg animables :', await evaluate('[...document.querySelectorAll("svg[data-mech]")].map((s) => s.dataset.mech).join(" ")'));
  console.log('lancés :', await evaluate('JSON.stringify(window.playAll())'));
  for (const i of [1, 2, 3, 4]) { await sleep(i === 1 ? 200 : 950); await shot(`bench-${i}`); }
} finally { await b.close(); fs.rmSync(site, { recursive: true, force: true }); }
