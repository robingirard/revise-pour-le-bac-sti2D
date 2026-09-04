import { test } from 'node:test';
import assert from 'node:assert/strict';
import { lessonButtonLabel, togglePlaying, toggleLesson, refreshLessonButtons } from '../js/anim.js';

class FakeClassList {
  constructor() { this.set = new Set(); }
  toggle(c) { if (this.set.has(c)) { this.set.delete(c); return false; } this.set.add(c); return true; }
  contains(c) { return this.set.has(c); }
}

test('togglePlaying bascule la classe playing', () => {
  const svg = { classList: new FakeClassList() };
  assert.equal(togglePlaying(svg), true);
  assert.ok(svg.classList.contains('playing'));
  assert.equal(togglePlaying(svg), false);
  assert.equal(togglePlaying(null), false);
});

test('toggleLesson bascule playing-all et met à jour le bouton', () => {
  const body = { classList: new FakeClassList() };
  const btn = { textContent: '', attrs: {}, setAttribute(k, v) { this.attrs[k] = v; } };
  assert.equal(toggleLesson(body, btn), true);
  assert.equal(btn.textContent, lessonButtonLabel(true));
  assert.equal(btn.attrs['aria-pressed'], 'true');
  assert.equal(toggleLesson(body, btn), false);
  assert.equal(btn.textContent, '▶ Voir les liaisons bouger');
});

test('refreshLessonButtons masque le bouton sans figure animable', () => {
  const mk = (hasAnim) => {
    const body = { querySelector: (sel) => (sel === 'svg[data-anim]' && hasAnim ? {} : null) };
    const details = { querySelector: (sel) => (sel === '.lesson-body' ? body : null) };
    const btn = { hidden: undefined, closest: (sel) => (sel === 'details.lesson' ? details : null) };
    return btn;
  };
  const a = mk(true), b = mk(false);
  refreshLessonButtons({ querySelectorAll: () => [a, b] });
  assert.equal(a.hidden, false);
  assert.equal(b.hidden, true);
});
