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

test('pictogramme {{emoji:…}} : en ligne, ou en bloc s\'il est seul', () => {
  assert.equal(renderRich('{{emoji:🚪}} **La porte**'), '<span class="emoji-big">🚪</span> <strong>La porte</strong>');
  assert.equal(renderRich('{{emoji:🚪}}'), '<span class="emoji-big emoji-block">🚪</span>');
  assert.equal(renderRich('{{emoji:<b>}}'), '{{emoji:&lt;b&gt;}}'); // pas de HTML : non substitué, échappé
});

// ---- formules mathématiques (KaTeX embarqué dans vendor/, chargé ici dans un bac à sable) ----
import { readFileSync } from 'node:fs';
import vm from 'node:vm';
import { mathHtml } from '../js/render.js';

function loadKatex() {
  const code = readFileSync(new URL('../vendor/katex/katex.min.js', import.meta.url), 'utf8');
  const sandbox = { self: {} };
  vm.runInNewContext(code, sandbox); // UMD : sans `module`/`exports`, KaTeX s'accroche à `self.katex`
  return sandbox.self.katex;
}

test('maths sans KaTeX : repli en italique, échappé', () => {
  delete globalThis.katex;
  assert.equal(renderRich('a $x<1$ b'), 'a <span class="math">x&lt;1</span> b');
  assert.equal(renderRich('$$E = m c^2$$'), '<div class="math-display"><span class="math">E = m c^2</span></div>');
});

test('maths avec KaTeX : en ligne, affichée, \\( \\), \\[ \\]', () => {
  globalThis.katex = loadKatex();
  try {
    const inline = renderRich('R = $\\frac{Z_1}{Z_2}$ ok');
    assert.match(inline, /^R = <span class="katex">.*<\/span> ok$/s);
    assert.doesNotMatch(inline, /katex-display/);
    const display = renderRich('$$x(t) = \\tfrac12 a t^2 + v_0 t$$');
    assert.match(display, /^<div class="math-display"><span class="katex-display">/);
    assert.match(renderRich('\\(a^2\\) et \\[b^2\\]'), /katex".*katex-display/s);
    assert.match(renderRich('Voir $\\omega = 2\\pi f$ sur {{fig:pivot}}', figures), /class="katex".*fig-inline/s);
    assert.match(renderRich('**gras** et $x$'), /<strong>gras<\/strong> et <span class="katex">/);
  } finally {
    delete globalThis.katex;
  }
});

test('maths : un dollar isolé reste un dollar, HTML non exécuté dans une formule', () => {
  globalThis.katex = loadKatex();
  try {
    assert.equal(renderRich('prix : 5 $ la pièce'), 'prix : 5 $ la pièce');
    const bad = renderRich('$<img src=x onerror=alert(1)>$');
    assert.doesNotMatch(bad, /<img/);
    assert.match(bad, /&lt;img|class="katex/);
    const err = mathHtml('\\frac{'); // erreur de syntaxe : throwOnError:false → rendu d'erreur, pas d'exception
    assert.match(err, /katex-error|class="math"/);
  } finally {
    delete globalThis.katex;
  }
});

test('leçon : maths dans une cellule de tableau, une liste et une ligne $$…$$ seule', () => {
  globalThis.katex = loadKatex();
  try {
    const html = renderLesson('| Grandeur | Formule |\n|---|---|\n| Puissance | $P = C \\omega$ |\n\n- vitesse $v = R\\omega$\n\n$$\\eta = \\frac{P_s}{P_e}$$', figures);
    assert.match(html, /<td><span class="katex">/);
    assert.match(html, /<li>vitesse <span class="katex">/);
    assert.match(html, /<div class="math-display"><span class="katex-display">/);
    assert.doesNotMatch(html, /<p><div/); // la formule seule n'est pas dans un paragraphe
  } finally {
    delete globalThis.katex;
  }
});
