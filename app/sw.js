// sw.js — service worker : cache-first pour l'enveloppe de l'appli et le contenu.
// Incrémenter VERSION à chaque mise en ligne pour forcer la mise à jour chez les utilisateurs.
const VERSION = '2026-09-04.4';
const CACHE = `revise-sti2d-${VERSION}`;
const ASSETS = [
  './', './index.html', './manifest.webmanifest', './content.js', './css/app.css',
  './js/main.js', './js/dom.js', './js/dates.js', './js/scheduler.js', './js/progression.js',
  './js/session.js', './js/store.js', './js/render.js', './js/answers.js', './js/bilan.js',
  './js/exercises/index.js', './js/exercises/common.js', './js/exercises/flashcard.js',
  './js/exercises/mcq.js', './js/exercises/match.js', './js/exercises/grid.js',
  './js/exercises/order.js', './js/exercises/input.js',
  './icons/icon.svg', './icons/icon-192.png', './icons/icon-512.png', './icons/apple-touch-icon.png',
];

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE).then((cache) => cache.addAll(ASSETS)).then(() => self.skipWaiting()));
});

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
