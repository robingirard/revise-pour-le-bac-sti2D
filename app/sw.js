// sw.js — service worker : cache-first pour l'enveloppe de l'appli et le contenu.
// Incrémenter VERSION à chaque mise en ligne pour forcer la mise à jour chez les utilisateurs.
const VERSION = '2026-09-04.12';
const CACHE = `revise-sti2d-${VERSION}`;
const ASSETS = [
  './', './index.html', './manifest.webmanifest', './content.js', './css/app.css',
  './js/main.js', './js/dom.js', './js/dates.js', './js/scheduler.js', './js/progression.js',
  './js/session.js', './js/store.js', './js/render.js', './js/answers.js', './js/bilan.js', './js/guided-logic.js', './js/home.js', './js/anim.js', './js/mech-anim.js',
  './js/exercises/index.js', './js/exercises/common.js', './js/exercises/flashcard.js',
  './js/exercises/mcq.js', './js/exercises/match.js', './js/exercises/grid.js',
  './js/exercises/order.js', './js/exercises/input.js', './js/exercises/guided.js',
  './icons/icon.svg', './icons/icon-192.png', './icons/icon-512.png', './icons/apple-touch-icon.png',
  './vendor/katex/katex.min.js', './vendor/katex/katex.min.css',
  './vendor/katex/fonts/KaTeX_AMS-Regular.woff2', './vendor/katex/fonts/KaTeX_Caligraphic-Bold.woff2', './vendor/katex/fonts/KaTeX_Caligraphic-Regular.woff2', './vendor/katex/fonts/KaTeX_Fraktur-Bold.woff2', './vendor/katex/fonts/KaTeX_Fraktur-Regular.woff2', './vendor/katex/fonts/KaTeX_Main-Bold.woff2', './vendor/katex/fonts/KaTeX_Main-BoldItalic.woff2', './vendor/katex/fonts/KaTeX_Main-Italic.woff2', './vendor/katex/fonts/KaTeX_Main-Regular.woff2', './vendor/katex/fonts/KaTeX_Math-BoldItalic.woff2', './vendor/katex/fonts/KaTeX_Math-Italic.woff2', './vendor/katex/fonts/KaTeX_SansSerif-Bold.woff2', './vendor/katex/fonts/KaTeX_SansSerif-Italic.woff2', './vendor/katex/fonts/KaTeX_SansSerif-Regular.woff2', './vendor/katex/fonts/KaTeX_Script-Regular.woff2', './vendor/katex/fonts/KaTeX_Size1-Regular.woff2', './vendor/katex/fonts/KaTeX_Size2-Regular.woff2', './vendor/katex/fonts/KaTeX_Size3-Regular.woff2', './vendor/katex/fonts/KaTeX_Size4-Regular.woff2', './vendor/katex/fonts/KaTeX_Typewriter-Regular.woff2',
];

// Fichiers facultatifs (absents dans certaines versions) : mis en cache s'ils existent, sans faire échouer l'installation.
const OPTIONAL = ['./figures/index.json'];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE)
      .then((cache) => cache.addAll(ASSETS).then(() => Promise.all(OPTIONAL.map((u) => cache.add(u).catch(() => null)))))
      .then(() => self.skipWaiting()),
  );
});
// Les figures (./figures/<id>.svg) sont mises en cache au fil des consultations par le gestionnaire fetch ci-dessous.

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim()),
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  event.respondWith(
    caches.match(req, { ignoreSearch: true }).then((hit) => hit || fetch(req).then((res) => {
      if (res && res.ok) {
        const copy = res.clone();
        caches.open(CACHE).then((cache) => cache.put(req, copy));
      }
      return res;
    }).catch(() => (req.mode === 'navigate' ? caches.match('./index.html') : undefined))),
  );
});
