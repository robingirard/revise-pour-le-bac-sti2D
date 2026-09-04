import { test, beforeEach } from 'node:test';
import assert from 'node:assert/strict';
import * as figs from '../js/figures.js';
import { renderRich, renderLesson } from '../js/render.js';

const SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><circle r="1"/></svg>';

/** fetch factice : compte les appels, répond selon `responses[url]` (texte, ou Error pour échouer). */
function fakeFetch(responses) {
  const calls = [];
  const fn = (url) => {
    calls.push(url);
    const r = responses[url];
    if (r instanceof Error) return Promise.reject(r);
    if (r == null) return Promise.resolve({ ok: false, status: 404, text: async () => 'not found' });
    return Promise.resolve({ ok: true, status: 200, text: async () => r, json: async () => JSON.parse(r) });
  };
  fn.calls = calls;
  return fn;
}

beforeEach(() => figs.resetForTests());

test('gabarit : dimensions issues de l’index, bloc ou en ligne, inconnu → null', () => {
  figs.configure({ index: { a: { w: 72, h: 36, bytes: 10 }, b: {} } });
  const inl = figs.placeholderHtml('a');
  assert.match(inl, /^<span class="fig fig-inline fig-lazy" data-fig="a" style="width: min\(100%, 96px\); aspect-ratio: 72 \/ 36;" aria-busy="true"><\/span>$/);
  assert.match(figs.placeholderHtml('a', { block: true }), /^<figure class="fig fig-block fig-lazy"/);
  assert.match(figs.placeholderHtml('b'), /aspect-ratio: 4 \/ 3/); // sans dimensions : gabarit par défaut
  assert.equal(figs.placeholderHtml('zz'), null);
  assert.equal(figs.isLazy('a'), true);
  assert.equal(figs.isLazy('zz'), false);
});

test('render : figure en ligne si fournie, gabarit si connue de l’index, manquante sinon', () => {
  figs.configure({ index: { lazy: { w: 10, h: 10, bytes: 1 } } });
  const figures = { inline: SVG };
  assert.equal(renderRich('{{fig:inline}}', figures), `<figure class="fig fig-block" data-fig="inline">${SVG}</figure>`);
  assert.match(renderRich('voir {{fig:lazy}} ici', figures), /<span class="fig fig-inline fig-lazy" data-fig="lazy"/);
  assert.match(renderRich('{{fig:lazy}}', figures), /<figure class="fig fig-block fig-lazy" data-fig="lazy"/);
  assert.match(renderRich('{{fig:absente}}', figures), /fig-missing/);
  assert.match(renderLesson('# T\n\n{{fig:lazy}}', figures), /<figure class="fig fig-block fig-lazy" data-fig="lazy"/);
});

test('chargement : un seul téléchargement par figure, cache, chemin relatif', async () => {
  const fetch = fakeFetch({ './figures/a.svg': SVG });
  figs.configure({ index: { a: { w: 1, h: 1, bytes: 1 } }, fetch });
  const [x, y] = await Promise.all([figs.load('a'), figs.load('a')]);
  assert.equal(x, SVG); assert.equal(y, SVG);
  assert.equal(fetch.calls.length, 1);
  assert.equal(await figs.load('a'), SVG);
  assert.equal(fetch.calls.length, 1); // servi par le cache
  assert.equal(figs.isCached('a'), true);
});

test('chargement : échec signalé puis réessai possible ; réponse non SVG rejetée', async () => {
  const fetch = fakeFetch({ './figures/a.svg': new Error('réseau'), './figures/b.svg': '<html>oops</html>' });
  figs.configure({ index: { a: {}, b: {} }, fetch });
  await assert.rejects(figs.load('a'), /réseau/);
  assert.equal(figs.failureOf('a'), 'réseau');
  await assert.rejects(figs.load('b'), /pas un SVG/);
  fetch.calls.length = 0;
  figs.configure({ fetch: fakeFetch({ './figures/a.svg': SVG }) });
  assert.equal(await figs.load('a'), SVG); // nouvel essai après correction
  assert.equal(figs.failureOf('a'), null);
});

test('prefetch : ignore les figures inconnues ou déjà en cache, ne rejette jamais', async () => {
  const fetch = fakeFetch({ './figures/a.svg': SVG, './figures/b.svg': new Error('x') });
  figs.configure({ index: { a: {}, b: {} }, fetch });
  await figs.prefetch(['a', 'b', 'zz', 'a']);
  assert.deepEqual(fetch.calls.sort(), ['./figures/a.svg', './figures/b.svg']);
  await figs.prefetch(['a']);
  assert.equal(fetch.calls.length, 2);
});

test('figureIdsOf : identifiants cités dans un payload', () => {
  const ids = figs.figureIdsOf({ prompt: 'x {{fig:a}} y', choices: ['{{fig:b}}', 'texte'], nested: { z: '{{fig:a}} {{fig:c-1}}' } });
  assert.deepEqual(ids.sort(), ['a', 'b', 'c-1']);
});

test('prefetchAll : progression, concurrence bornée, total en octets et format Mo', async () => {
  const responses = {}; const index = {};
  for (let i = 0; i < 10; i++) { responses[`./figures/f${i}.svg`] = SVG; index[`f${i}`] = { w: 1, h: 1, bytes: 250000 }; }
  responses['./figures/f3.svg'] = new Error('x');
  const fetch = fakeFetch(responses);
  figs.configure({ index, fetch });
  const steps = [];
  const r = await figs.prefetchAll({ concurrency: 3, onProgress: (k, n) => steps.push([k, n]) });
  assert.deepEqual(r, { done: 10, ok: 9, total: 10 });
  assert.equal(steps.length, 10);
  assert.deepEqual(steps[9], [10, 10]);
  assert.equal(figs.totalBytes(), 2500000);
  assert.equal(figs.formatMo(2500000), '2,5 Mo');
  assert.equal(figs.formatMo(12345678), '12 Mo');
  assert.equal(figs.formatMo(1587), '2 ko');
});

test('ensureIndex : lit figures/index.json quand CONTENT ne fournit pas l’index', async () => {
  const fetch = fakeFetch({ './figures/index.json': '{"k":{"w":5,"h":5,"bytes":9}}' });
  figs.configure({ fetch });
  assert.equal(figs.getIndex(), null);
  assert.deepEqual(await figs.ensureIndex(), { k: { w: 5, h: 5, bytes: 9 } });
  assert.equal(figs.isLazy('k'), true);
});

test('fig-anim : les figures en ligne animables portent la classe (render)', async () => {
  const { renderRich } = await import('../js/render.js');
  const figures = { anim: '<svg xmlns="http://www.w3.org/2000/svg" data-anim="rot" style="--cx:10px;--cy:10px"><circle class="s1" r="1"/></svg>',
                    plain: '<svg xmlns="http://www.w3.org/2000/svg"></svg>' };
  assert.match(renderRich('{{fig:anim}}', figures), /<figure class="fig fig-block fig-anim" data-fig="anim"/);
  assert.match(renderRich('a {{fig:anim}} b', figures), /<span class="fig fig-inline fig-anim" data-fig="anim"/);
  assert.doesNotMatch(renderRich('{{fig:plain}}', figures), /fig-anim/);
});
