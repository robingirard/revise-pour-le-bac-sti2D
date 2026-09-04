import { test } from 'node:test';
import assert from 'node:assert/strict';
import { escapeHtml, renderRich, renderLesson } from '../js/render.js';

const figures = { pivot: '<svg xmlns="http://www.w3.org/2000/svg"><circle r="1"/></svg>' };

test('échappement du HTML', () => {
  assert.equal(escapeHtml('<b a="1">&\'</b>'), '&lt;b a=&quot;1&quot;&gt;&amp;&#39;&lt;/b&gt;');
  assert.equal(renderRich('<script>alert(1)</script>'), '&lt;script&gt;alert(1)&lt;/script&gt;');
});

test('texte riche : gras, italique, math, retours à la ligne', () => {
  assert.equal(renderRich('a **b** c'), 'a <strong>b</strong> c');
  assert.equal(renderRich('a *b* c'), 'a <em>b</em> c');
  assert.equal(renderRich('x $\\vec{z}$ y'), 'x <span class="math">\\vec{z}</span> y');
  assert.equal(renderRich('l1\nl2'), 'l1<br>l2');
  assert.equal(renderRich(null), '');
  assert.equal(renderRich('2 * 3 * 4'), '2 * 3 * 4'); // astérisques isolés conservés
});

test('figures : substitution en ligne, bloc si seule, manquante signalée', () => {
  assert.equal(renderRich('voir {{fig:pivot}} ici', figures), `voir <span class="fig fig-inline" data-fig="pivot">${figures.pivot}</span> ici`);
  assert.equal(renderRich('{{fig:pivot}}', figures), `<figure class="fig fig-block" data-fig="pivot">${figures.pivot}</figure>`);
  assert.match(renderRich('{{fig:absente}}', figures), /fig-missing.*absente/);
  assert.match(renderRich('{{fig:<x>}}'), /\{\{fig:&lt;x&gt;\}\}/); // id invalide : pas substitué, échappé
});

test('leçon : titres, paragraphes, listes, tableaux, figure', () => {
  const md = `# Titre
Un paragraphe
sur deux lignes.

- item **un**
- item deux

| A | B |
|---|---|
| 1 | 2 |

{{fig:pivot}}
## Sous-titre`;
  const html = renderLesson(md, figures);
  assert.match(html, /<h2>Titre<\/h2>/);
  assert.match(html, /<p>Un paragraphe sur deux lignes\.<\/p>/);
  assert.match(html, /<ul><li>item <strong>un<\/strong><\/li><li>item deux<\/li><\/ul>/);
  assert.match(html, /<table><thead><tr><th>A<\/th><th>B<\/th><\/tr><\/thead><tbody><tr><td>1<\/td><td>2<\/td><\/tr><\/tbody><\/table>/);
  assert.match(html, /<figure class="fig fig-block" data-fig="pivot">/);
  assert.match(html, /<h3>Sous-titre<\/h3>/);
  assert.equal(renderLesson(''), '');
  assert.equal(renderLesson('1. un\n2. deux'), '<ol><li>un</li><li>deux</li></ol>');
  assert.equal(renderLesson('- a\n1. b'), '<ul><li>a</li></ul>\n<ol><li>b</li></ol>');
});
