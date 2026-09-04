# Révise STI2D

Application d'entraînement pour le bac STI2D (ingénierie 2I2D, puis physique-chimie et maths),
fondée sur la **répétition espacée** (planificateur type Leitner/SM-2) et une **progression par
compétences** (arbre à la Duolingo : niveaux, XP, série de jours).

Tout est reproductible : le contenu pédagogique est écrit en YAML/Markdown, les figures sont des
sources TikZ compilées en SVG, et `make` reconstruit l'application complète dans `dist/`.

Première unité couverte : **le schéma cinématique** (manuel I2D 1re, chapitre 2, p. 30-33) —
les 10 liaisons normalisées, leurs symboles, degrés de liberté, surfaces de contact, efforts
transmissibles, puis classes d'équivalence, graphe des liaisons et lecture/tracé du schéma
(serre-joint, bielle-manivelle, étau).

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
  captures d'écran automatiques `app/dev/shots.mjs`).

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

## Feuille de route

1. ✅ Liaisons, classes d'équivalence, graphe, lecture de schéma (serre-joint, bielle-manivelle, étau).
2. Mécanismes supplémentaires de complexité croissante (pompe, vérin/levier, pince, cric, essuie-glace…),
   symboles 3D, exercice de construction guidée du schéma.
3. Chapitres suivants du manuel (mouvements et cinématique, chaîne d'information, matériaux et
   structures), puis physique-chimie et maths (rendu des formules avec KaTeX).
4. Tableau de bord parent (progression exportée) et publication automatique sur GitHub Pages.
