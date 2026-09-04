# Révise STI2D

Application d'entraînement pour le bac STI2D (ingénierie 2I2D, puis physique-chimie et maths),
fondée sur la **répétition espacée** (planificateur type Leitner/SM-2) et une **progression par
compétences** (arbre à la Duolingo : niveaux, XP, série de jours).

Tout est reproductible : le contenu pédagogique est écrit en YAML/Markdown, les figures sont des
sources TikZ compilées en SVG, et `make` reconstruit l'application complète dans `dist/`.

Contenu couvert (13 unités, 51 compétences, environ 1 100 exercices, 170 figures TikZ) :

- **Ingénierie 2I2D** : les liaisons mécaniques ; le schéma cinématique (serre-joint, bielle-manivelle,
  étau) ; transmettre et transformer le mouvement ; mouvements et cinématique ; statique et résistance
  des matériaux ; chaîne d'information et numérique (signaux, CAN, numération, logique, algorithmes).
- **Physique-chimie** : énergie électrique ; énergie thermique ; chimie (matière, combustions, piles) ;
  ondes et lumière ; forces, énergie et dynamique ; compléments de Terminale (radioactivité, piles et
  accumulateurs, acido-basique, signaux et spectres).
- **Mathématiques** : primitives, cercle trigonométrique, fonctions trigonométriques, produit scalaire,
  nombres complexes.

Les formules sont rendues avec KaTeX (embarqué, hors ligne) ; les figures sont chargées à la demande.

## Utilisation

### Sur un ordinateur

```bash
make            # compile les figures, génère le contenu, assemble dist/
make serve      # http://localhost:8000/
```

(Ouvrir directement `dist/index.html` par double-clic fonctionne dans Safari ; Chrome bloque les
modules JavaScript en `file://`, d'où le petit serveur `make serve`.)

### Sur un iPhone / iPad (comme une application)

1. Publier `dist/` sur un serveur statique (GitHub Pages par exemple).
2. Ouvrir l'adresse dans **Safari**, puis *Partager* → **« Sur l'écran d'accueil »**.
3. L'application s'ouvre ensuite en plein écran et fonctionne hors connexion.

La progression est enregistrée dans le navigateur de l'appareil. L'écran *Progrès* propose un
**bilan à partager** avec un parent (résumé + lien qui affiche le bilan complet) ; l'écran *Réglages*
permet d'**exporter** et d'**importer** la progression complète, de saisir un prénom et d'activer le
**mode découverte** (toutes les compétences déverrouillées).

## Principes pédagogiques

- Des **QCM avec distracteurs** plutôt que de l'auto-évaluation ; chaque mauvaise réponse a sa
  propre explication (« pourquoi ce n'est pas ça »), générée à partir des mobilités des liaisons.
- Des **figures** partout : symboles normalisés (deux vues), surfaces de contact, mobilités,
  dessins d'ensemble et schémas des mécanismes, pictogrammes pour les objets du quotidien.
- **Répétition espacée** (SM-2) : un exercice raté revient vite, un exercice réussi s'espace ;
  **progression** par compétences avec prérequis, niveaux, XP et série de jours.

## Prérequis pour reconstruire

- TeX Live (avec `lualatex`, TikZ, `standalone`) — testé avec TeX Live 2026 ;
- Poppler (`pdftocairo`) : `brew install poppler` ;
- Python 3 avec `pyyaml` ;
- Node ≥ 18 (uniquement pour les tests de l'application) ; Google Chrome (uniquement pour les
  captures d'écran automatiques `app/dev/shots.mjs` et `app/dev/tour.mjs`).
- KaTeX est embarqué dans `app/vendor/katex/` (version et origine dans `VERSION.txt`).

## Organisation

```
content/               sources pédagogiques (la « vérité »)
  liaisons.yaml        les 10 liaisons : désignation, ddl, efforts, contacts, exemples, symboles
  mecanismes/*.yaml    un mécanisme = pièces, classes d'équivalence, liaisons, questions
  units.yaml           arbre de compétences : unités → compétences → générateurs d'exercices
  lessons/*.md         leçons (Markdown restreint, figures via {{fig:id}}, tables via {{table:…}})
figures/tikz/          liaisons.sty (symboles normalisés, hachures) + contacts, mobilités, mécanismes
figures/build/         PDF et SVG compilés (non versionnés) — dont planche-liaisons.pdf à imprimer
tools/                 build_figures.py, build_content.py, validate.py, serve.py
app/                   l'application (HTML/CSS/JS sans dépendance) + tests + fixture de dev
dist/                  résultat du build : app + content.json/content.js (non versionné)
docs/SPEC.md           spécification technique (format du contenu, planificateur, progression)
```

### Ajouter du contenu

- **Une liaison / un exemple** : éditer `content/liaisons.yaml` ; les exercices (QCM, flashcards,
  grilles, associations) sont **générés** automatiquement par `tools/build_content.py`.
- **Un mécanisme** : créer `content/mecanismes/<id>.yaml` (pièces, classes, liaisons, questions)
  et ses figures `figures/tikz/mecanisme-<id>-{dessin,classes,graphe,schema}.tex` en utilisant les
  symboles de `liaisons.sty` (`\pic[s1=couleur1, s2=couleur2] at (A) {pivot face};`).
- **Une compétence** : ajouter une entrée dans `content/units.yaml` (prérequis, leçon, générateurs
  et/ou exercices écrits à la main) — types : `flashcard`, `mcq`, `match`, `grid`, `order`, `input`.

Les identifiants d'exercices sont stables : reconstruire le contenu ne remet pas la progression à zéro.

### Vérifier

```bash
make check      # invariants du contenu (ddl + efforts = 6, prérequis, figures référencées…)
make test       # tests unitaires de l'application (planificateur, progression, séances, rendu)
```

## Exercices complets et annales

- Chaque mécanisme donne automatiquement un **exercice complet de fin de chapitre** (type `guided`) :
  classes → contacts et liaisons → graphe → symbole → lecture du schéma, débloqué au niveau 2 de
  la compétence « Tracer le schéma ».
- `content/annales.yaml` référence des **sujets d'examen officiels** (liens vers les PDF) avec des
  prérequis de niveau ; ils apparaissent sur l'accueil, verrouillés tant que les niveaux ne sont pas atteints.
- `docs/notes/` contient les notes structurées tirées du manuel (plan, formules, figures à redessiner,
  propositions de questions) qui servent à écrire les unités suivantes ; `docs/biblio.md` recense
  les annales et sites utiles.

## Feuille de route

1. ✅ Les deux manuels (ingénierie 1re/Tle, physique-chimie 1re/Tle, maths 1re) transcrits en notes
   et transformés en 13 unités avec exercices à feedback, exercices complets, annales, bilan parent, KaTeX.
2. Exercices guidés supplémentaires tirés des exercices des manuels et des annales ; maths de Terminale
   (non scannées) ; mécanismes supplémentaires et symboles 3D.
3. Relecture pédagogique par un enseignant des points signalés « à vérifier » dans `docs/notes/`.
