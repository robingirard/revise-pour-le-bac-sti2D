// render.js — texte riche et Markdown restreint → HTML (voir docs/SPEC.md §4-§5)
// Tout le texte est échappé ; seules les figures SVG (de confiance, générées par le build) sont insérées telles quelles.

const FIG_RE = /\{\{fig:([\w.-]+)\}\}/g;
const FIG_ONLY_RE = /^\s*\{\{fig:([\w.-]+)\}\}\s*$/;
const EMOJI_RE = /\{\{emoji:([^{}<>&]{1,16})\}\}/g;          // appliqué sur le texte déjà échappé
const EMOJI_ONLY_RE = /^\s*\{\{emoji:[^{}<>&]{1,16}\}\}\s*$/;

export function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

export function figureHtml(id, figures = {}, { block = false } = {}) {
  const svg = figures && figures[id];
  if (!svg) return `<span class="fig-missing">[figure manquante : ${escapeHtml(id)}]</span>`;
  const attr = `data-fig="${escapeHtml(id)}"`;
  return block ? `<figure class="fig fig-block" ${attr}>${svg}</figure>` : `<span class="fig fig-inline" ${attr}>${svg}</span>`;
}

/** Mise en forme en ligne d'un texte déjà échappé. */
function inline(escaped, { emojiBlock = false } = {}) {
  const emojiClass = emojiBlock ? 'emoji-big emoji-block' : 'emoji-big';
  return escaped
    .replace(EMOJI_RE, `<span class="${emojiClass}">$1</span>`)
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/(^|[^*\w])\*(\S(?:[^*\n]*?\S)?)\*(?!\w)/g, '$1<em>$2</em>')
    .replace(/\$([^$\n]+?)\$/g, '<span class="math">$1</span>')
    .replace(/\n/g, '<br>');
}

/** Texte riche : **gras**, *italique*, \n, {{fig:ID}}, {{emoji:🚪}}, $math$. */
export function renderRich(text, figures = {}) {
  if (text == null) return '';
  const str = String(text);
  const block = FIG_ONLY_RE.test(str);
  const emojiBlock = EMOJI_ONLY_RE.test(str); // un pictogramme seul : affiché en grand, centré
  const parts = str.split(FIG_RE); // [texte, id, texte, id, …]
  let out = '';
  for (let i = 0; i < parts.length; i++) {
    out += i % 2 === 0 ? inline(escapeHtml(parts[i]), { emojiBlock }) : figureHtml(parts[i], figures, { block });
  }
  return out;
}

const isSeparatorRow = (cells) => cells.every((c) => /^:?-{2,}:?$/.test(c));

/** Markdown restreint : titres, paragraphes, listes, tableaux, figures, texte riche. */
export function renderLesson(md, figures = {}) {
  const lines = String(md || '').replace(/\r\n?/g, '\n').split('\n');
  const out = [];
  let para = [], list = null, olist = null, table = null;
  const flushPara = () => {
    if (para.length) out.push(`<p>${renderRich(para.join(' '), figures)}</p>`);
    para = [];
  };
  const flushList = () => {
    if (list) out.push(`<ul>${list.map((li) => `<li>${renderRich(li, figures)}</li>`).join('')}</ul>`);
    if (olist) out.push(`<ol>${olist.map((li) => `<li>${renderRich(li, figures)}</li>`).join('')}</ol>`);
    list = null; olist = null;
  };
  const flushTable = () => {
    if (table && table.length) {
      const [head, ...rows] = table;
      const th = head.map((c) => `<th>${renderRich(c, figures)}</th>`).join('');
      const tr = rows.map((r) => `<tr>${r.map((c) => `<td>${renderRich(c, figures)}</td>`).join('')}</tr>`).join('');
      out.push(`<div class="table-wrap"><table><thead><tr>${th}</tr></thead><tbody>${tr}</tbody></table></div>`);
    }
    table = null;
  };
  const flushAll = () => { flushPara(); flushList(); flushTable(); };

  for (const raw of lines) {
    const t = raw.trim();
    if (t === '') { flushAll(); continue; }
    const heading = /^(#{1,3})\s+(.+)$/.exec(t);
    if (heading) {
      flushAll();
      const level = heading[1].length + 1; // '#' → h2 : le h1 est le titre de l'écran
      out.push(`<h${level}>${renderRich(heading[2], figures)}</h${level}>`);
      continue;
    }
    const fig = FIG_ONLY_RE.exec(t);
    if (fig) { flushAll(); out.push(figureHtml(fig[1], figures, { block: true })); continue; }
    if (/^[-*]\s+/.test(t)) {
      flushPara(); flushTable();
      if (olist) flushList();
      (list ||= []).push(t.replace(/^[-*]\s+/, ''));
      continue;
    }
    if (/^\d+[.)]\s+/.test(t)) {
      flushPara(); flushTable();
      if (list) flushList();
      (olist ||= []).push(t.replace(/^\d+[.)]\s+/, ''));
      continue;
    }
    if (t.startsWith('|')) {
      flushPara(); flushList();
      const cells = t.replace(/^\|/, '').replace(/\|$/, '').split('|').map((c) => c.trim());
      if (!isSeparatorRow(cells)) (table ||= []).push(cells);
      continue;
    }
    flushList(); flushTable();
    para.push(t);
  }
  flushAll();
  return out.join('\n');
}
