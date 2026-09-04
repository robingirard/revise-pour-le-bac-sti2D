// browser.mjs — infrastructure partagée des scripts de vérification visuelle :
// serveur statique minimal + Chrome headless piloté par le protocole CDP (aucune dépendance).
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';

const MIME = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json',
  '.webmanifest': 'application/manifest+json', '.png': 'image/png', '.svg': 'image/svg+xml' };
export const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

/** Lance le serveur (dossier `dir`) et Chrome ; retourne des aides { goto, reload, shot, click, evaluate, close }. */
export async function launch({ dir, out, port = 8766, debugPort = 9333, width = 390, height = 844,
  chrome = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' }) {
  fs.mkdirSync(out, { recursive: true });
  const server = http.createServer((req, res) => {
    let p = decodeURIComponent(new URL(req.url, 'http://x').pathname);
    if (p.endsWith('/')) p += 'index.html';
    fs.readFile(path.join(dir, p), (err, data) => {
      if (err) { res.writeHead(404); res.end('not found'); return; }
      res.writeHead(200, { 'Content-Type': MIME[path.extname(p)] || 'application/octet-stream' });
      res.end(data);
    });
  });
  await new Promise((r) => server.listen(port, '127.0.0.1', r));

  const profile = fs.mkdtempSync(path.join(out, '.chrome-'));
  const proc = spawn(chrome, ['--headless=new', `--remote-debugging-port=${debugPort}`, `--window-size=${width},${height}`, '--hide-scrollbars',
    '--no-first-run', '--no-default-browser-check', `--user-data-dir=${profile}`, 'about:blank'], { stdio: 'ignore' });
  let version = null;
  for (let i = 0; i < 60 && !version; i++) {
    try { const r = await fetch(`http://127.0.0.1:${debugPort}/json/version`); if (r.ok) version = await r.json(); } catch { await sleep(250); }
  }
  if (!version) throw new Error('Chrome ne répond pas');
  const targets = await (await fetch(`http://127.0.0.1:${debugPort}/json`)).json();
  const page = targets.find((t) => t.type === 'page');
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  const pending = new Map();
  let seq = 0;
  ws.onmessage = (ev) => { const m = JSON.parse(ev.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); } };
  await new Promise((r) => { ws.onopen = r; });
  const send = (method, params = {}) => new Promise((resolve) => { const id = ++seq; pending.set(id, resolve); ws.send(JSON.stringify({ id, method, params })); });
  const evaluate = async (expression) => {
    const r = await send('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
    if (r.result?.exceptionDetails) throw new Error(`evaluate: ${r.result.exceptionDetails.text} ${r.result.exceptionDetails.exception?.description || ''}`);
    return r.result?.result?.value;
  };
  await send('Page.enable');
  await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 2, mobile: true });

  const base = `http://127.0.0.1:${port}/index.html`;
  const goto = async (hash) => { await send('Page.navigate', { url: base + hash }); await sleep(500); };
  const reload = async () => { await send('Page.reload'); await sleep(700); };
  const shot = async (name, fullPage = false) => {
    const params = { format: 'png' };
    if (fullPage) {
      const h = await evaluate('document.documentElement.scrollHeight');
      params.clip = { x: 0, y: 0, width, height: Math.min(h, 4000), scale: 1 };
      params.captureBeyondViewport = true;
    }
    const r = await send('Page.captureScreenshot', params);
    fs.writeFileSync(path.join(out, `${name}.png`), Buffer.from(r.result.data, 'base64'));
    console.log('capture', name);
  };
  const click = async (selector, index = 0) => {
    const ok = await evaluate(`(() => { const els = document.querySelectorAll(${JSON.stringify(selector)}); const el = els[${index}]; if (!el) return false; el.click(); return true; })()`);
    if (!ok) throw new Error(`introuvable : ${selector}[${index}]`);
    await sleep(150);
  };
  const close = async () => {
    ws.close();
    server.close();
    const exited = new Promise((r) => proc.once('exit', r));
    proc.kill();
    await Promise.race([exited, sleep(3000)]);
    try { fs.rmSync(profile, { recursive: true, force: true, maxRetries: 5, retryDelay: 200 }); } catch { /* profil temporaire */ }
  };
  return { send, evaluate, goto, reload, shot, click, close, base };
}

// « Solveur » injecté dans la page : répond juste à l'exercice affiché, à partir de window.CONTENT.
export const SOLVER = `
window.__solve = function () {
  const plain = (s) => String(s).replace(/\\*\\*|\\*|\\$/g, '').replace(/\\{\\{fig:[^}]+\\}\\}/g, '').replace(/\\s+/g, ' ').trim();
  const norm = (el) => el.textContent.replace(/\\s+/g, ' ').trim();
  const figOf = (s) => (/\\{\\{fig:([\\w.-]+)\\}\\}/.exec(String(s)) || [])[1];
  const findBtn = (buttons, rich) => {
    const fig = figOf(rich), text = plain(rich);
    return [...buttons].find((b) => (fig ? b.querySelector('[data-fig="' + fig + '"]') : true) && (text ? norm(b) === text : true));
  };
  const box = document.querySelector('.exercise');
  if (!box) return 'no-exercise';
  const type = [...box.classList].find((c) => c.startsWith('exercise-')).slice(9);
  const prompt = box.querySelector('.prompt, .card-front');
  const items = Object.values(window.CONTENT.items).filter((it) => it.type === type);
  const text = (it) => it.payload.prompt ?? it.payload.front;
  const item = box.dataset.item ? window.CONTENT.items[box.dataset.item]
    : items.find((it) => plain(text(it)) === norm(prompt) && (!figOf(text(it)) || prompt.querySelector('[data-fig="' + figOf(text(it)) + '"]')));
  if (!item) return 'item-not-found:' + type;
  const p = item.payload;
  if (type === 'flashcard') { box.querySelector('.btn-primary').click(); box.querySelector('.grade-good').click(); return 'flashcard'; }
  if (type === 'mcq') { for (const i of p.answer) findBtn(box.querySelectorAll('.choice'), p.choices[i]).click(); box.querySelector('.btn-verify').click(); return 'mcq'; }
  if (type === 'grid') { for (const id of p.answer) box.querySelector('input[data-cell="' + id + '"], input[aria-label="' + ((p.labels && p.labels[id]) || id) + '"]').click(); box.querySelector('.btn-verify').click(); return 'grid'; }
  if (type === 'order') { for (const s of p.steps) findBtn(box.querySelectorAll('.order-pool .choice'), s).click(); box.querySelector('.btn-verify').click(); return 'order'; }
  if (type === 'input') { const inp = box.querySelector('.text-input'); inp.value = p.answer; inp.dispatchEvent(new Event('input')); box.querySelector('.btn-verify').click(); return 'input'; }
  if (type === 'match') {
    const cols = box.querySelectorAll('.match-col');
    for (const pair of p.pairs) { findBtn(cols[0].querySelectorAll('.match-btn'), pair.left).click(); findBtn(cols[1].querySelectorAll('.match-btn'), pair.right).click(); }
    return 'match';
  }
  return 'unknown:' + type;
};`;
