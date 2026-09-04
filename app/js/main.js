// main.js — point d'entrée : routeur (#/…) et écrans (voir docs/SPEC.md §8)
import { h, clear } from './dom.js';
import * as store from './store.js';
import { todayStr } from './dates.js';
import { grade as gradeItem } from './scheduler.js';
import * as prog from './progression.js';
import * as sess from './session.js';
import { renderRich, renderLesson } from './render.js';
import { EXERCISES } from './exercises/index.js';
import { GRADE_LABELS } from './exercises/flashcard.js';

window.__RS_STARTED = true; // signale à index.html que le module a bien démarré

const content = window.CONTENT;
const figures = (content && content.figures) || {};
let progress = store.load();
let session = null;      // séance en cours (perdue si la page est rechargée)
let lastSummary = null;  // bilan de la dernière séance terminée

// ---------------------------------------------------------------- routeur
function parseHash() {
  const raw = (location.hash || '#/').slice(1);
  const [pathStr, queryStr = ''] = raw.split('?');
  return { path: pathStr.split('/').filter(Boolean), query: new URLSearchParams(queryStr) };
}

function navigate(hash) {
  if (location.hash === hash) route(); else location.hash = hash;
}

function route() {
  const root = document.getElementById('app');
  clear(root);
  window.scrollTo(0, 0);
  if (!content || !Array.isArray(content.units)) {
    root.append(h('p', { class: 'error' }, 'Contenu introuvable : le fichier content.js est manquant ou invalide.'));
    return;
  }
  const { path, query } = parseHash();
  const [screen, arg] = path;
  try {
    switch (screen) {
      case undefined: renderHome(root); break;
      case 'skill': renderSkill(root, arg); break;
      case 'session': renderSessionEntry(root, arg, query); break;
      case 'review': renderReviewEntry(root, query); break;
      case 'summary': renderSummary(root); break;
      case 'progress': renderProgress(root); break;
      case 'settings': renderSettings(root); break;
      default: renderHome(root);
    }
  } catch (err) {
    console.error(err);
    root.append(h('p', { class: 'error' }, `Erreur : ${err.message}`), h('a', { class: 'btn', href: '#/' }, 'Accueil'));
  }
}

// ---------------------------------------------------------------- composants
function topbar({ back = null, title = '' } = {}) {
  return h('header', { class: 'topbar' },
    back ? h('a', { class: 'icon-btn', href: back, 'aria-label': 'Retour' }, '←') : null,
    h('h1', {}, title));
}

function bottomNav(active) {
  const link = (id, href, label) => h('a', { class: `nav-link${active === id ? ' active' : ''}`, href }, label);
  return h('nav', { class: 'bottom-nav' },
    link('home', '#/', '🏠 Accueil'), link('progress', '#/progress', '📈 Progrès'), link('settings', '#/settings', '⚙️ Réglages'));
}

function bar(fraction, cls = '') {
  const pct = Math.max(0, Math.min(100, Math.round(100 * fraction)));
  return h('div', { class: `bar ${cls}`, role: 'progressbar', 'aria-valuenow': pct, 'aria-valuemin': 0, 'aria-valuemax': 100 },
    h('div', { class: 'bar-fill', style: `width:${pct}%` }));
}

/** Pastilles de niveau : ● atteint, ◐ en cours, ○ à faire. */
function levelRing(state, levels) {
  const st = { ...prog.newSkillState(), ...(state || {}) };
  const dots = [];
  for (let i = 0; i < levels; i++) {
    const cls = i < st.level ? 'dot done' : i === st.level && st.progress > 0 ? 'dot half' : 'dot';
    dots.push(h('span', { class: cls }));
  }
  return h('span', { class: 'ring', title: `Niveau ${st.level}/${levels}` }, ...dots, h('span', { class: 'ring-text' }, `${st.level}/${levels}`));
}

function prereqTitles(skill) {
  return (skill.prerequisites || []).map((id) => (sess.findSkill(content, id) || { title: id }).title).join(', ');
}

function plural(n, one, many) {
  return `${n} ${n > 1 ? many : one}`;
}

// ---------------------------------------------------------------- accueil
function renderHome(root) {
  const today = todayStr();
  const streak = prog.currentStreak(progress.streak, today);
  const xpToday = prog.xpOnDay(progress.history, today);
  const goal = progress.settings.dailyGoal || prog.DEFAULT_DAILY_GOAL;
  const dueCount = sess.countDue(content, progress, today);
  root.append(
    topbar({ title: content.title || 'Révise STI2D' }),
    h('section', { class: 'stats' },
      h('div', { class: 'stat' }, h('span', { class: 'stat-value' }, `🔥 ${streak}`), h('span', { class: 'stat-label' }, plural(streak, 'jour de série', 'jours de série').replace(/^\d+ /, ''))),
      h('div', { class: 'stat stat-wide' },
        h('span', { class: 'stat-value' }, `⭐ ${xpToday} / ${goal} XP`),
        h('span', { class: 'stat-label' }, xpToday >= goal ? 'objectif du jour atteint !' : 'objectif du jour'),
        bar(xpToday / goal, 'bar-small'))),
    dueCount > 0
      ? h('a', { class: 'btn btn-primary btn-block', href: '#/review' }, `Réviser (${dueCount})`)
      : h('div', { class: 'btn btn-block btn-muted', 'aria-disabled': 'true' }, 'Rien à réviser aujourd\'hui 🎉'),
    ...content.units.map((unit) => renderUnit(unit, today)),
    bottomNav('home'),
  );
}

function renderUnit(unit, today) {
  return h('section', { class: 'unit' },
    h('h2', {}, unit.title),
    unit.description ? h('p', { class: 'muted' }, unit.description) : null,
    h('div', { class: 'skills' }, ...(unit.skills || []).map((skill) => renderSkillCard(skill, today))));
}

function renderSkillCard(skill, today) {
  const st = progress.skills[skill.id];
  const unlocked = prog.isUnlocked(skill, progress);
  const levels = prog.skillLevels(skill);
  const counts = sess.skillCounts(content, progress, skill.id, today);
  const state = !unlocked ? 'locked' : prog.isCompleted(skill, progress) ? 'done' : 'open';
  const meta = unlocked
    ? `${plural(counts.due, 'à revoir', 'à revoir')} · ${plural(counts.fresh, 'nouveau', 'nouveaux')} · ${counts.mastered}/${counts.total} maîtrisés`
    : `🔒 Termine d'abord : ${prereqTitles(skill)}`;
  return h('a', { class: `skill skill-${state}`, href: `#/skill/${skill.id}` },
    h('span', { class: 'skill-icon' }, skill.icon || '📘'),
    h('span', { class: 'skill-body' }, h('span', { class: 'skill-title' }, skill.title), h('span', { class: 'skill-meta' }, meta)),
    levelRing(st, levels));
}

// ---------------------------------------------------------------- compétence
function renderSkill(root, skillId) {
  const skill = sess.findSkill(content, skillId);
  if (!skill) return renderNotFound(root);
  const unit = sess.findUnit(content, skillId);
  const today = todayStr();
  const st = { ...prog.newSkillState(), ...(progress.skills[skillId] || {}) };
  const levels = prog.skillLevels(skill);
  const unlocked = prog.isUnlocked(skill, progress);
  const counts = sess.skillCounts(content, progress, skillId, today);
  const stat = (label, value) => h('div', { class: 'count' }, h('span', { class: 'count-value' }, value), h('span', { class: 'count-label' }, label));

  root.append(
    topbar({ back: '#/', title: unit ? unit.title : '' }),
    h('section', { class: 'skill-head' },
      h('div', { class: 'skill-icon big' }, skill.icon || '📘'),
      h('h2', {}, skill.title),
      skill.description ? h('p', { class: 'muted' }, skill.description) : null,
      levelRing(st, levels),
      st.level < levels ? bar(st.progress, 'bar-small') : h('p', { class: 'muted' }, 'Compétence terminée ✔'),
    ),
    h('section', { class: 'counts' },
      stat('nouveaux', counts.fresh), stat('à revoir', counts.due), stat('maîtrisés', counts.mastered), stat('exercices', counts.total)),
    skill.lesson
      ? h('details', { class: 'lesson', open: st.sessions === 0 }, h('summary', {}, '📖 Leçon'), h('div', { class: 'lesson-body', html: renderLesson(skill.lesson, figures) }))
      : null,
    !unlocked
      ? h('p', { class: 'locked-msg' }, `🔒 Cette compétence se débloque quand « ${prereqTitles(skill)} » atteint le niveau 1.`)
      : counts.total === 0
        ? h('p', { class: 'muted' }, 'Aucun exercice n\'est encore disponible pour cette compétence.')
        : h('a', { class: 'btn btn-primary btn-block', href: `#/session/${skill.id}` }, st.sessions === 0 ? 'Commencer' : 'Nouvelle séance'),
    bottomNav(null),
  );
}

function renderNotFound(root) {
  root.append(topbar({ back: '#/', title: 'Introuvable' }), h('p', { class: 'muted' }, 'Cette page n\'existe pas.'));
}

// ---------------------------------------------------------------- séance
function renderSessionEntry(root, skillId, query) {
  const skill = sess.findSkill(content, skillId);
  if (!skill) return renderNotFound(root);
  if (!prog.isUnlocked(skill, progress)) return navigate(`#/skill/${skillId}`);
  const forced = query.has('item') || query.has('seed');
  const reuse = !forced && session && session.kind === 'skill' && session.skillId === skillId && !sess.isFinished(session);
  if (!reuse) {
    const seed = query.get('seed');
    const rng = seed != null ? sess.mulberry32(Number(seed)) : Math.random;
    session = sess.buildSkillSession(content, progress, skillId, { today: todayStr(), rng, forceItemId: query.get('item') });
  }
  if (session.queue.length === 0) {
    session = null;
    root.append(topbar({ back: `#/skill/${skillId}`, title: skill.title }), h('p', { class: 'muted' }, 'Aucun exercice disponible.'));
    return;
  }
  renderSessionScreen(root);
}

function renderReviewEntry(root, query) {
  const reuse = !query.has('seed') && session && session.kind === 'review' && !sess.isFinished(session);
  if (!reuse) {
    const seed = query.get('seed');
    const rng = seed != null ? sess.mulberry32(Number(seed)) : Math.random;
    session = sess.buildReviewSession(content, progress, { today: todayStr(), rng });
  }
  if (session.queue.length === 0) {
    session = null;
    root.append(topbar({ back: '#/', title: 'Révision' }), h('p', { class: 'muted' }, 'Rien à réviser aujourd\'hui 🎉'), bottomNav('home'));
    return;
  }
  renderSessionScreen(root);
}

function renderSessionScreen(root) {
  clear(root);
  const itemId = sess.currentItemId(session);
  const item = content.items[itemId];
  const total = session.queue.length;
  const skill = session.skillId ? sess.findSkill(content, session.skillId) : null;
  const quit = h('button', { class: 'icon-btn', type: 'button', 'aria-label': 'Quitter la séance', onClick: () => {
    if (confirm('Quitter la séance ? Ce qui a déjà été répondu est conservé, mais la séance ne comptera pas.')) {
      session = null;
      navigate('#/');
    }
  } }, '✕');
  const exerciseBox = h('div', { class: `exercise exercise-${item.type}` });
  root.append(
    h('header', { class: 'topbar session-top' }, quit, bar(session.index / total, 'session-bar'), h('span', { class: 'counter' }, `${session.index + 1}/${total}`)),
    h('main', { class: 'session-main' },
      skill ? h('p', { class: 'session-skill muted' }, `${skill.icon || ''} ${skill.title}`) : h('p', { class: 'session-skill muted' }, '🔁 Révision'),
      exerciseBox),
  );
  const mod = EXERCISES[item.type];
  if (!mod) {
    exerciseBox.append(
      h('p', { class: 'error' }, `Type d'exercice inconnu : ${item.type}`),
      h('button', { class: 'btn', type: 'button', onClick: () => { session = sess.answer(session, { correct: true }).session; next(root); } }, 'Passer'));
    return;
  }
  let answered = false;
  mod.mount(exerciseBox, item, {
    figures,
    rng: Math.random,
    onAnswer: (res) => {
      if (answered) return;
      answered = true;
      handleAnswer(root, item, res);
    },
  });
}

function handleAnswer(root, item, res) {
  const today = todayStr();
  const { session: next, schedulerGrade } = sess.answer(session, res);
  session = next;
  let nextInfo = '';
  if (schedulerGrade) {
    const st = gradeItem(progress.items[item.id], schedulerGrade, today);
    progress.items[item.id] = st;
    store.save(progress);
    nextInfo = st.interval === 0 ? 'On le revoit dans cette séance.' : `Prochaine révision dans ${plural(st.interval, 'jour', 'jours')}.`;
  } else if (!res.correct) {
    nextInfo = 'On le revoit dans cette séance.';
  }
  const isCard = item.type === 'flashcard';
  const cls = isCard ? 'feedback neutral' : res.correct ? 'feedback ok' : 'feedback ko';
  const title = isCard ? `Carte notée « ${GRADE_LABELS[res.grade] || res.grade} »` : res.correct ? 'Bravo, c\'est juste !' : 'Pas tout à fait…';
  const explanation = item.payload.explanation;
  const finished = sess.isFinished(session);
  const panel = h('div', { class: cls, role: 'status' },
    h('div', { class: 'feedback-title' }, title),
    explanation ? h('div', { class: 'feedback-expl', html: renderRich(explanation, figures) }) : null,
    nextInfo ? h('div', { class: 'feedback-next' }, nextInfo) : null,
    h('button', { class: 'btn btn-block btn-continue', type: 'button', onClick: () => nextStep(root) }, finished ? 'Voir le bilan' : 'Continuer'));
  root.append(panel);
  panel.querySelector('button').focus();
}

function nextStep(root) {
  if (sess.isFinished(session)) finishSession(); else renderSessionScreen(root);
}

function finishSession() {
  const today = todayStr();
  const result = sess.summary(session);
  let xp = prog.sessionXp(result), passed = null, leveledUp = false, skill = null, skillState = null;
  if (session.kind === 'skill') {
    skill = sess.findSkill(content, session.skillId);
    const r = prog.applySession(progress.skills[session.skillId], skill, result);
    progress.skills[session.skillId] = r.state;
    ({ xp, passed, leveledUp } = r);
    skillState = r.state;
  }
  progress.xp += xp;
  progress.streak = prog.updateStreak(progress.streak, today);
  progress.history.push({ date: today, kind: session.kind, skill: session.skillId, correct: result.correct, total: result.total, xp });
  store.save(progress);
  lastSummary = { kind: session.kind, skill, skillState, result, xp, passed, leveledUp };
  session = null;
  navigate('#/summary');
}


// ---------------------------------------------------------------- bilan
function renderSummary(root) {
  if (!lastSummary) return navigate('#/');
  const { kind, skill, skillState, result, xp, passed, leveledUp } = lastSummary;
  const pct = Math.round(100 * result.accuracy);
  const levels = skill ? prog.skillLevels(skill) : 0;
  root.append(
    topbar({ title: 'Bilan de la séance' }),
    h('section', { class: 'summary' },
      h('div', { class: 'summary-emoji' }, pct >= 80 ? '🎉' : pct >= 50 ? '💪' : '📚'),
      h('h2', {}, kind === 'review' ? 'Révision terminée' : `${skill.title}`),
      h('p', { class: 'summary-score' }, `${result.correct} / ${result.total} du premier coup (${pct} %)`),
      h('p', { class: 'summary-xp' }, `+${xp} XP`),
      skill
        ? h('div', { class: 'summary-level' },
          leveledUp ? h('p', { class: 'ok-text' }, `Niveau ${skillState.level} atteint !`) : null,
          passed === false ? h('p', { class: 'muted' }, 'Il faut au moins 80 % de bonnes réponses pour progresser de niveau.') : null,
          levelRing(skillState, levels),
          skillState.level < levels ? bar(skillState.progress, 'bar-small') : null)
        : null,
      h('div', { class: 'actions' },
        skill && prog.isUnlocked(skill, progress) ? h('a', { class: 'btn btn-primary btn-block', href: `#/session/${skill.id}` }, 'Encore une séance') : null,
        h('a', { class: 'btn btn-block', href: '#/' }, 'Retour à l\'accueil'))),
  );
}

// ---------------------------------------------------------------- progrès
function renderProgress(root) {
  const today = todayStr();
  const rows = [];
  for (const unit of content.units) {
    for (const skill of unit.skills || []) {
      const st = { ...prog.newSkillState(), ...(progress.skills[skill.id] || {}) };
      const c = sess.skillCounts(content, progress, skill.id, today);
      const unlocked = prog.isUnlocked(skill, progress);
      rows.push(h('tr', { class: unlocked ? '' : 'locked' },
        h('td', {}, h('a', { href: `#/skill/${skill.id}` }, `${skill.icon || ''} ${skill.title}`)),
        h('td', {}, unlocked ? `${st.level}/${prog.skillLevels(skill)}` : '🔒'),
        h('td', {}, c.fresh), h('td', {}, c.due), h('td', {}, c.mastered), h('td', {}, c.total)));
    }
  }
  const sessions = progress.history.length;
  root.append(
    topbar({ back: '#/', title: 'Progrès' }),
    h('section', { class: 'stats' },
      h('div', { class: 'stat' }, h('span', { class: 'stat-value' }, `⭐ ${progress.xp}`), h('span', { class: 'stat-label' }, 'XP au total')),
      h('div', { class: 'stat' }, h('span', { class: 'stat-value' }, `📚 ${sessions}`), h('span', { class: 'stat-label' }, plural(sessions, 'séance', 'séances').replace(/^\d+ /, ''))),
      h('div', { class: 'stat' }, h('span', { class: 'stat-value' }, `🔥 ${prog.currentStreak(progress.streak, today)}`), h('span', { class: 'stat-label' }, 'jours de série'))),
    h('div', { class: 'table-wrap' }, h('table', { class: 'progress-table' },
      h('thead', {}, h('tr', {}, h('th', {}, 'Compétence'), h('th', { title: 'Niveau' }, 'Niv.'), h('th', { title: 'Nouveaux' }, 'Nouv.'), h('th', { title: 'À revoir' }, 'Dus'), h('th', { title: 'Maîtrisés' }, 'Maîtr.'), h('th', {}, 'Total'))),
      h('tbody', {}, ...rows))),
    h('p', { class: 'muted small' }, 'Un exercice est « maîtrisé » quand sa prochaine révision est prévue dans 21 jours ou plus.'),
    bottomNav('progress'),
  );
}

// ---------------------------------------------------------------- réglages
function renderSettings(root) {
  const goalInput = h('input', { class: 'text-input', type: 'number', min: 10, max: 500, step: 10, value: progress.settings.dailyGoal || prog.DEFAULT_DAILY_GOAL, 'aria-label': 'Objectif quotidien en XP' });
  goalInput.addEventListener('change', () => {
    const v = Math.max(10, Math.min(500, Number(goalInput.value) || prog.DEFAULT_DAILY_GOAL));
    goalInput.value = v;
    progress.settings.dailyGoal = v;
    store.save(progress);
  });
  const exportArea = h('textarea', { class: 'json-area', readonly: true, rows: 6, 'aria-label': 'Progression exportée' });
  exportArea.value = store.exportJson(progress);
  const copyBtn = h('button', { class: 'btn', type: 'button', onClick: async () => {
    try {
      await navigator.clipboard.writeText(exportArea.value);
      copyBtn.textContent = 'Copié ✔';
    } catch {
      exportArea.select();
      copyBtn.textContent = 'Sélectionné : copie avec ⌘C';
    }
  } }, 'Copier');
  const importArea = h('textarea', { class: 'json-area', rows: 6, placeholder: 'Colle ici une progression exportée…', 'aria-label': 'Progression à importer' });
  const importMsg = h('p', { class: 'muted small' });
  const importBtn = h('button', { class: 'btn', type: 'button', onClick: () => {
    try {
      progress = store.importJson(importArea.value);
      store.save(progress);
      importMsg.textContent = 'Progression importée ✔';
      importMsg.className = 'ok-text small';
      exportArea.value = store.exportJson(progress);
    } catch (err) {
      importMsg.textContent = err.message;
      importMsg.className = 'error small';
    }
  } }, 'Importer');
  const resetBtn = h('button', { class: 'btn btn-danger', type: 'button', onClick: () => {
    if (confirm('Tout remettre à zéro ? La progression sera définitivement effacée.')) {
      progress = store.reset();
      store.save(progress);
      session = null;
      navigate('#/');
    }
  } }, 'Tout remettre à zéro');

  root.append(
    topbar({ back: '#/', title: 'Réglages' }),
    h('section', { class: 'settings' },
      h('h2', {}, 'Objectif quotidien'),
      h('div', { class: 'input-row' }, goalInput, h('span', { class: 'unit' }, 'XP / jour')),
      h('h2', {}, 'Exporter la progression'),
      h('p', { class: 'muted small' }, 'Copie ce texte pour le sauvegarder ou le transférer sur un autre appareil.'),
      exportArea, h('div', { class: 'row-right' }, copyBtn),
      h('h2', {}, 'Importer une progression'),
      importArea, h('div', { class: 'row-right' }, importBtn), importMsg,
      h('h2', {}, 'Zone dangereuse'),
      h('div', { class: 'row-right' }, resetBtn),
      h('p', { class: 'muted small' }, `Contenu généré le ${content.generatedAt ? new Date(content.generatedAt).toLocaleString('fr-FR') : '—'} · version ${content.version || '?'}`)),
    bottomNav('settings'),
  );
}

// ---------------------------------------------------------------- démarrage
window.addEventListener('hashchange', route);
route();
