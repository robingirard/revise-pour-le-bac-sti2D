# Révise STI2D — spécification technique (v1)

Outil d'entraînement pour le bac STI2D (2I2D, physique-chimie, maths) fondé sur
la **répétition espacée** (planificateur type SM-2/Leitner) et une **progression
par compétences** (arbre de compétences à la Duolingo).

## 1. Choix de plateforme

**Application web statique installable (PWA)** :

- un seul code (HTML/CSS/JS sans framework, sans bundler) ;
- fonctionne dans Safari/Chrome sur iPhone, iPad et MacBook ; « Ajouter à l'écran
  d'accueil » l'installe comme une app (plein écran, hors-ligne grâce au service worker) ;
- hébergeable sur GitHub Pages (ou n'importe quel serveur statique) ; ouvrable aussi
  en local (double-clic sur `dist/index.html`) ;
- la progression est stockée dans le navigateur (`localStorage`) avec export/import JSON.

Une enveloppe native (SwiftUI + WKWebView, ou Capacitor) reste possible plus tard
sans rien changer au contenu.

## 2. Arborescence du dépôt

```
revise-sti2d/
├── content/               # SOURCE de vérité pédagogique (YAML, Markdown)
│   ├── liaisons.yaml      # base de connaissances : les 10 liaisons normalisées
│   ├── mecanismes/*.yaml  # mécanismes étudiés (classes d'équivalence, liaisons, graphe)
│   ├── units.yaml         # arbre de compétences : unités → compétences → générateurs
│   └── lessons/*.md       # textes de leçon (Markdown, figures via {{fig:id}})
├── figures/
│   ├── tikz/liaisons.sty  # bibliothèque TikZ : symboles normalisés des liaisons (pics)
│   ├── tikz/*.tex         # figures standalone (compilées en SVG par le build)
│   └── build/             # PDF/SVG générés (non versionnés)
├── tools/
│   ├── build_figures.py   # .tex → PDF (lualatex) → SVG (pdftocairo)
│   ├── build_content.py   # YAML + générateurs → dist/content.json (+ content.js)
│   ├── validate.py        # invariants (ddl + efforts = 6, ids uniques, figures existantes…)
│   └── serve.py           # serveur local de développement
├── app/                   # code de l'application (copié tel quel dans dist/)
│   ├── index.html, manifest.webmanifest, sw.js, icons/
│   ├── css/app.css
│   └── js/ (main.js, scheduler.js, session.js, store.js, render.js, exercises/*.js)
├── dist/                  # SORTIE du build (app + content.json + content.js)
├── Makefile               # make figures | content | app | check | serve | clean
└── README.md
```

Règle : **tout ce qui est dans `dist/` et `figures/build/` est régénéré** par `make`.

## 3. Format `content.json` (contrat entre le build et l'appli)

```jsonc
{
  "version": 1,
  "generatedAt": "2026-09-04T10:00:00Z",
  "title": "Révise STI2D",
  "figures": { "liaison-pivot-axe": "<svg …>…</svg>", "…": "…" },
  "units": [
    {
      "id": "liaisons",
      "matiere": "ingenierie",           // ingenierie | physique | maths : regroupement sur l'accueil
      "title": "Les liaisons mécaniques",
      "description": "…",
      "skills": [
        {
          "id": "liaisons-symboles",
          "title": "Reconnaître les symboles",
          "icon": "🔩",                    // emoji ou id de figure
          "description": "…",
          "prerequisites": ["liaisons-mobilites"],   // ids de compétences
          "lesson": "## …markdown…",       // leçon (Markdown restreint, voir §5)
          "levels": 3,                     // nombre de niveaux (couronnes)
          "items": ["liaisons-symboles-pivot-nom", "…"]  // ids d'exercices
        }
      ]
    }
  ],
  "items": {
    "liaisons-symboles-pivot-nom": {
      "id": "liaisons-symboles-pivot-nom",
      "skill": "liaisons-symboles",
      "type": "mcq",                       // flashcard | mcq | match | grid | order | input
      "level": 1,                          // niveau à partir duquel l'exercice apparaît (1..levels)
      "tags": ["pivot"],
      "payload": { … }                     // dépend du type, voir §4
    }
  }
}
```

`dist/content.js` contient exactement le même objet, sous la forme
`window.CONTENT = {...};`. **Les figures ne sont plus incluses** dans `content.json`
(`"figures": {}`) : chaque figure est un fichier `dist/figures/<id>.svg` chargé à la demande
par l'appli (`fetch`), avec `dist/figures/index.json` = `{ "<id>": { "w", "h", "bytes" } }`
(dimensions en pt, pour réserver l'espace avant chargement ; aussi présent dans
`content.figureIndex`). L'appli garde la compatibilité : si `content.figures[id]` existe,
elle l'insère directement. Le service worker met en cache les figures au fur et à mesure ;
un bouton des Réglages « Préparer le mode hors-ligne » télécharge toutes les figures listées
dans `index.json` (avec une barre de progression).

## 4. Types d'exercices (payloads)

Un « texte riche » (`rich`) est une chaîne pouvant contenir :
`**gras**`, `*italique*`, retours à la ligne `\n`, `{{fig:ID}}` (SVG inséré en ligne,
depuis `figures`), `{{emoji:🚪}}` (pictogramme affiché en grand, pour illustrer une
question sans figure), `$…$` (math : affiché tel quel en italique pour l'instant,
KaTeX plus tard).

**Correction adaptée à l'erreur.** Chaque exercice auto-corrigé fournit, en plus de
l'`explanation` générale, un **détail propre à l'erreur commise**, affiché en premier dans le
bandeau rouge (`onAnswer({ correct, grade, detail })`, `detail` = rich ou null) :

- `mcq` : `payload.feedback[i]` (facultatif, aligné sur `choices`, `null` autorisé) = ce qu'il
  faut dire si le choix *i* est sélectionné à tort ; le détail est le feedback du (premier)
  mauvais choix sélectionné ;
- `grid` : détail automatique « Coché(s) à tort : … · Oublié(s) : … » (avec les `labels`),
  complété par `payload.cellFeedback[id]` (facultatif) pour chaque case fautive ;
- `match` : « Erreur : *gauche* ↔ *droite choisie* » pour la première association fausse ;
- `order` : la première étape mal placée (« L'étape n°k devait être : … ») ;
- `input` : la réponse attendue.

Les exercices d'auto-évaluation (`flashcard`) restent supportés par l'appli mais ne sont plus
utilisés par le contenu : on préfère des QCM avec distracteurs et feedback ciblé.

| type | payload | correction |
|---|---|---|
| `flashcard` | `{ "front": rich, "back": rich }` | auto-évaluation : *À revoir* / *Difficile* / *Facile* |
| `mcq` | `{ "prompt": rich, "choices": [rich], "answer": [idx], "multiple": false, "layout": "list"\|"grid", "explanation": rich, "feedback": [rich\|null] }` | ensemble d'indices sélectionnés == `answer` |
| `match` | `{ "prompt": rich, "pairs": [{"left": rich, "right": rich}] }` (3 à 6 paires) | toutes les paires appariées ; une erreur = item raté |
| `grid` | `{ "prompt": rich, "rows": [{"id":"x","label":"x"}…], "cols": [{"id":"T","label":"Translation"},{"id":"R","label":"Rotation"}], "answer": ["Tx","Rx"], "labels": {"Tx":"X"}, "hint": "…", "explanation": rich }` — id de case = `col.id + row.id` ; `labels` (facultatif) remplace le texte affiché dans une case (efforts : Fx → X, Mx → L) ; `hint` (facultatif) remplace la consigne ; `cellFeedback` (facultatif) = `{id: rich}` explication par case fautive | ensemble de cases cochées == `answer` |
| `order` | `{ "prompt": rich, "steps": [rich] }` (dans le bon ordre ; l'appli mélange) | ordre reconstitué == `steps` |
| `input` | `{ "prompt": rich, "answer": "3", "accept": ["trois"], "numeric": true, "tolerance": 0.01, "unit": "m", "explanation": rich }` | texte normalisé (minuscules, sans accents/espaces) ∈ {answer}∪accept, ou |x−answer| ≤ tolerance si numeric |

Les choix de `mcq` en `layout:"grid"` sont typiquement des figures (2×2).

### Exercice guidé (`guided`)

Un **exercice complet de fin de chapitre** enchaîne plusieurs étapes autour d'un même système
(par exemple : du dessin d'ensemble au schéma cinématique). Payload :

```jsonc
{ "title": "Le serre-joint : du mécanisme au schéma",
  "intro": rich,                       // contexte + figure, affiché en tête de chaque étape (repliable)
  "steps": [                           // chaque étape = un exercice auto-corrigé, même payload qu'un item
    { "kind": "mcq",   "prompt": rich, "choices": [rich], "answer": [0], "feedback": [...], "explanation": rich },
    { "kind": "input", "prompt": rich, "answer": "4", "numeric": true, "explanation": rich },
    { "kind": "grid",  "prompt": rich, "rows": [...], "cols": [...], "answer": [...], "explanation": rich },
    { "kind": "order", "prompt": rich, "steps": [rich], "explanation": rich },
    { "kind": "match", "prompt": rich, "pairs": [...] }
  ] }
```

Déroulement : les étapes sont jouées dans l'ordre, chacune corrigée immédiatement (bandeau vert/rouge
avec le détail de l'erreur, puis « Étape suivante »). Un item `guided` compte pour **un** exercice dans la
séance : `correct` = toutes les étapes justes du premier coup ; note `good` si tout juste, `hard` si au moins
la moitié, `again` sinon ; XP : 2 par étape juste du premier coup. Les items `guided` sont toujours de niveau 3
et ne sont jamais tirés dans une séance ordinaire : ils apparaissent sur l'écran de la compétence dans une
carte « Exercices complets », lançables (`#/session/SKILL?item=ID`) quand la compétence est au niveau ≥ 2,
sinon verrouillés avec le message « Atteins le niveau 2 pour débloquer ».

### Symboles animés

Les SVG `liaison-<id>-<vue>` dont le mouvement du solide 1 est visible dans la vue portent
`data-anim="rot|rock|tx|ty"` et `style="--cx:…px;--cy:…px"` (centre A en unités utilisateur du
SVG) ; les éléments du solide 1 (rouge) ont la classe `s1`. L'appli anime ces éléments
(`transform-box: view-box; transform-origin: var(--cx) var(--cy)`) : rotation continue (`rot`),
oscillation ±25° (`rock`), va-et-vient horizontal ou vertical de ±10 unités (`tx`, `ty`).
Déclenchement : survol de la souris ou toucher sur la figure (bascule), et un bouton
« ▶ Voir les liaisons bouger » dans les leçons qui anime toutes les figures de la page.

### Schémas cinématiques animés

`content.animations[<id de figure>]` décrit le mouvement des classes d'équivalence d'un schéma
(sources : bloc `animation:` du YAML d'un mécanisme, ou `content/animations.yaml` pour les figures de
transmission / transformation, où chaque classe indique en plus sa couleur TikZ `couleur:`).
Le SVG du schéma porte `data-mech="<id de figure>"`
et chaque tracé d'une classe est enveloppé dans `<g class="mech" data-class="E1">` (classement par
couleur au build). Spécification :

```jsonc
{ "mecanisme": "bielle-manivelle", "bbox": [x0, y0, x1, y1], "border": 4, "duration": 4,
  "legende": "…",
  "classes": {
    "E0": { "motion": "fixed" },
    "E1": { "motion": "rotate", "center": [0, 0], "turns": 1 },            // ou "amplitude": deg, "phase"
    "E2": { "motion": "coupler", "crank": "E1", "a": [0.9, 1.5], "slider": "E3", "b": [5, 0] },
    "E3": { "motion": "slider", "dir": [1, 0], "coupler": "E2" },
    "E4": { "motion": "translate", "dir": [0, 1], "amplitude": 0.4, "phase": 0.25 },
    "E5": { "motion": "follow", "of": "E3", "then": { "motion": "translate", … } },
    "courroie": { "motion": "dash", "speed": 29 },                         // tirets défilants (pt/s)
    "E6": { "motion": "rocker", "pivot": [4, 0], "coupler": "E2" },         // balancier d'un quadrilatère articulé
    "E7": { "motion": "aim", "pivot": [1.2, 0], "at": "E1", "point": [2.6, 1.9] },              // corps de vérin
    "E8": { "motion": "aim", "pivot": [1.2, 0], "at": "E1", "point": [2.6, 1.9], "slide": true } } }   // tige de vérin
```

Coordonnées en **cm** dans le repère du dessin TikZ ; conversion vers les unités utilisateur du SVG :
`k = 72 / 2.54`, `X = border + (x − x0)·k`, `Y = border + (y1 − y)·k` (l'axe y est inversé). Le temps
`t ∈ [0, 1)` parcourt un cycle de `duration` secondes ; `rotate` avec `turns` = rotation continue
(sens trigonométrique : angle SVG négatif), sinon oscillation sinusoïdale `amplitude·sin(2π(t + phase))`
(degrés), plus un angle moyen `offset` facultatif (degrés) ; `translate` = déplacement sinusoïdal `amplitude·sin(2π(t + phase))` (cm) le long de `dir` ;
`follow` = même transformation que la classe `of`, composée avec `then` ; `coupler` (bielle) : le point
`a` (dessiné, solidaire de `crank`) suit la manivelle, le point `b` reste sur la droite de `slider`
(direction `dir`) à distance `|ab|` de `a(t)`, la bielle est déplacée rigidement de `a→b` vers `a(t)→b(t)` ;
`slider` : translation `b(t) − b` calculée par sa bielle ; `rocker` (balancier d'un quadrilatère articulé) :
la bielle `coupler` a son point `b` sur le balancier, qui tourne autour de `pivot` (fixe) : `b(t)` = intersection
du cercle de centre `a(t)` et de rayon `|ab|` avec le cercle de centre `pivot` et de rayon `|pivot b|`, du même
côté que la position dessinée ; `aim` (corps de vérin) : rotation autour de `pivot` (fixe) de l'angle qui amène
la direction `pivot → point` sur `pivot → point(t)`, où `point` est solidaire de la classe `at` ; avec
`slide: true` (tige de vérin), la pièce est en plus translatée le long de cet axe pour rester attachée en
`point(t)` ; `dash` (courroie, chaîne) : pas de transformation,
le groupe reçoit `stroke-dasharray` et un `stroke-dashoffset` qui décroît de `speed` unités SVG par seconde
(sens de tracé du chemin ; distance par cycle arrondie à un nombre entier de motifs). Les transformations
sont des matrices affines
appliquées (attribut `transform="matrix(…)"`) aux groupes `g.mech[data-class]`. Déclenchement identique
aux symboles (survol, toucher, bouton de leçon) ; boucle `requestAnimationFrame` uniquement pendant la
lecture ; la `legende` est affichée sous la figure pendant la lecture. Dans le `.tex`, la boîte fixe
`\useasboundingbox` doit être égale à `bbox`, les flèches et annotations fixes utilisent une teinte
différente de la pièce (`solideA!60`) pour ne pas être regroupées avec elle, et les étiquettes restent
des glyphes (jamais animés).

## 5. Leçon (Markdown restreint)

Titres `#`/`##`/`###`, paragraphes, `**gras**`, `*italique*`, listes `- `, tableaux
simples `| a | b |`, `{{fig:ID}}` sur une ligne (figure centrée), `$…$`.
Rendu par une fonction maison (pas de dépendance).

## 6. Planificateur de répétition espacée (SM-2 simplifié)

État par item : `{ "reps": 0, "ease": 2.5, "interval": 0, "due": null, "lapses": 0, "last": null }`
(`interval` en jours, `due`/`last` en ISO date `YYYY-MM-DD`). Un item sans état est **nouveau**.

Notes : `again | hard | good | easy` (les exercices auto-corrigés donnent `again`
si faux, `good` si juste du premier coup ; les flashcards proposent les 3 boutons
*À revoir* = again, *Difficile* = hard, *Facile* = easy… et *Bien* = good).

```
again : reps=0 ; interval=0 (dû aujourd'hui) ; ease=max(1.3, ease−0.2) ; lapses+1
hard  : interval=max(1, round(interval×1.2)) ; ease=max(1.3, ease−0.15) ; reps+1
good  : interval = reps==0 ? 1 : reps==1 ? 3 : round(interval×ease) ; reps+1
easy  : interval = reps==0 ? 3 : round(interval×ease×1.3) ; ease+=0.15 ; reps+1
due = aujourd'hui + interval
```

Un item est **dû** si `due ≤ aujourd'hui`. **Maîtrisé** si `interval ≥ 21`.

## 7. Progression (Duolingo-like)

- Une **compétence** est *verrouillée* tant que tous ses `prerequisites` n'ont pas
  atteint le niveau ≥ 1. Elle a `levels` niveaux (défaut 3).
- État : `{ "level": 0, "progress": 0, "sessions": 0, "xp": 0 }`.
  Chaque **séance réussie** (≥ 80 % de bonnes réponses au premier essai) fait
  `progress += 1/2` ; à `progress ≥ 1` → `level += 1`, `progress = 0`.
  Une séance < 80 % ne fait pas progresser mais compte dans `sessions`.
- **Séance de compétence** (8 exercices) : d'abord les items **dus** de la
  compétence, puis les items **nouveaux** de niveau ≤ `level + 1`, puis (s'il en
  manque) des items déjà vus, au hasard. Les items dus restent avant les nouveaux ; chaque bloc
  est mélangé puis **diversifié** (jamais deux exercices consécutifs du même générateur). Un item raté est **remis
  en fin de file** jusqu'à réussite (il est noté `again` la première fois seulement).
- **Séance de révision** (bouton « Réviser ») : tous les items dus des compétences
  déverrouillées, 20 max, toutes compétences mélangées.
- **XP** : 10 par séance terminée + 2 par bonne réponse au premier essai.
  **Série** (streak) : jours consécutifs avec ≥ 1 séance terminée.
  Objectif quotidien : 30 XP (réglable).

## 8. Stockage et écrans

- `localStorage["revise-sti2d.progress.v1"]` =
  `{ "version":1, "items":{id:état}, "skills":{id:état}, "xp":0, "streak":{"count":0,"last":"YYYY-MM-DD"}, "history":[{"date","skill","correct","total","xp"}], "settings":{"dailyGoal":30} }`.
- Écrans : **Accueil** (série, XP du jour, bouton Réviser avec nombre d'items dus,
  arbre des unités/compétences avec niveau et verrouillage, unités regroupées par **matière**
  — Ingénierie 2I2D, Physique-chimie, Mathématiques — dans des sections repliables dont l'état
  est mémorisé, chaque section affichant sa progression : compétences au niveau ≥ 1 / total) → **Compétence**
  (leçon repliable, stats, bouton *Commencer*) → **Séance** (barre de progression,
  exercice, retour immédiat vert/rouge + explication, bouton *Continuer*) →
  **Bilan** (score, XP, niveau) ; **Progrès** (tableau par compétence : dus, nouveaux,
  maîtrisés) ; **Réglages** (objectif, export/import JSON de la progression, remise à zéro).
- Interface **en français**, mobile d'abord, boutons larges, thème clair/sombre
  automatique, accessibilité clavier.
- `settings` contient aussi `name` (prénom de l'élève, facultatif) et `unlockAll`
  (« mode découverte » : toutes les compétences déverrouillées, pour explorer ou pour un parent).

## 10. Annales

`content.annales` (construit depuis `content/annales.yaml`) liste des sujets d'examen officiels :

```jsonc
{ "id": "2i2d-2024-metropole", "titre": "Bac 2024 — 2I2D, métropole", "session": "2024",
  "epreuve": "2I2D", "partie": "Partie commune, exercice 1 : …", "url": "https://…/sujet.pdf",
  "corrige": "https://…" | null, "themes": ["schéma cinématique", "statique"],
  "prerequis": [ { "skill": "schema-2d", "level": 2 } ],   // tous requis pour déverrouiller
  "guided": "annales.2i2d-2024-metropole" | null }         // item guided adapté, s'il existe
```

Écran **Accueil** : après les unités, une section « Annales » liste ces sujets ; un sujet est verrouillé
tant que ses prérequis ne sont pas atteints (message indiquant la compétence et le niveau manquants) ;
déverrouillé, il montre les liens (sujet, corrigé, ouverts dans un nouvel onglet) et, s'il y en a un,
un bouton « S'entraîner » qui lance l'item guided. Le mode découverte déverrouille aussi les annales.

## 9. Bilan pour le parent

Objet **bilan** (calculé par une fonction pure `buildBilan(progress, content, today)`) :

```jsonc
{ "v": 1, "date": "2026-09-04", "name": "Tom", "xp": 420, "streak": 5,
  "sessions7d": 6, "accuracy7d": 84,               // séances et % de bonnes réponses sur 7 jours
  "skills": [ { "id": "symboles", "level": 2, "progress": 0.5, "sessions": 5,
                "acc": 80,                          // % de bonnes réponses (3 dernières séances)
                "total": 49, "seen": 30, "mastered": 12, "due": 4 } ],
  "recent": [ { "date": "2026-09-04", "skill": "symboles", "correct": 8, "total": 10 } ],  // 10 dernières
  "weak": [ { "tag": "pivot-glissant", "lapses": 4 } ] }                                  // 5 tags les plus ratés
```

Les `tags` des exercices (identifiants de liaison, de mécanisme) servent à repérer les points
faibles ; l'appli affiche le nom lisible (nom de la liaison via les exercices, sinon le tag).

- Écran **Progrès** : en tête, une carte « Bilan » avec le résumé et le bouton
  **« Partager le bilan »** : `navigator.share({ title, text, url })` si disponible, sinon une
  zone de texte à copier + un lien `mailto:` ; `url` = adresse de l'appli + `#/bilan?d=<base64url(JSON du bilan)>`
  et `text` = résumé lisible (prénom, date, série, XP, séances de la semaine, niveaux, points faibles).
- Route `#/bilan` : le bilan courant, mis en page (tableau par compétence, séances récentes,
  points faibles). Route `#/bilan?d=…` : **bilan reçu** (lecture seule, bandeau « Bilan reçu,
  daté du … ») — c'est ce que le parent ouvre. Le paramètre `d` est décodé sans jamais être
  exécuté ; un `d` invalide affiche un message d'erreur.
- Bouton **« Tout déverrouiller (mode découverte) »** dans Réglages, réversible.
