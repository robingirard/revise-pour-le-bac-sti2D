# Revise STI2D — le contenu

Entraînement au baccalauréat STI2D : **ingénierie et 2I2D**, **physique-chimie**, **mathématiques**.
Répétition espacée, progression par compétences, figures et mécanismes animés.

**[Ouvrir l'application](https://www.robingirard.eu/assets/revise/sti2d/v1.0/index.html)** — elle tourne
entièrement dans le navigateur, fonctionne hors connexion une fois chargée, et **n'envoie rien
nulle part** : la progression reste sur l'appareil de l'élève.

Ce dépôt est un **paquet de contenu**. Le moteur qui le fait tourner vit à côté, dans `revise-core` :
il ne connaît aucune matière, et ce paquet lui fournit son contenu et ses générateurs d'exercices.
Voir `docs/PLAN-V2.md` pour le pourquoi de ce découpage.

## Ce que couvre le paquet

19 unités, 84 compétences, **2 058 exercices** dont 81 exercices complets guidés, 296 figures,
7 mécanismes animés, 13 annales référencées.

- **Ingénierie et 2I2D** — liaisons mécaniques, schéma cinématique, transmission et transformation
  du mouvement, mouvements et cinématique, statique et résistance des matériaux, chaîne
  d'information ; en Terminale : analyse fonctionnelle, énergie électrique, bâtiment, structures
  et matériaux.
- **Physique-chimie** — électricité, thermique, chimie, ondes et lumière, mécanique, et les
  compléments de Terminale (radioactivité, piles et accumulateurs, acido-basique, spectres).
- **Mathématiques** — première ; Terminale spécialité PCM ; Terminale enseignement commun
  (automatismes, suites, exponentielle et logarithme, dérivation, statistiques à deux variables,
  probabilités).

Les exercices sont des **QCM à distracteurs** — chaque mauvaise réponse a son explication propre —
des saisies numériques, des grilles, des remises en ordre, des associations, et des **exercices
complets** en plusieurs étapes comme en fin de chapitre.

## Reconstruire

```bash
make            # figures TikZ → SVG, contenu, application assemblée dans dist/
make serve      # http://localhost:8000/
make check      # invariants du contenu, et contrôle des droits
make test       # tests du moteur
make droits     # le détail de la comparaison aux transcriptions des manuels
make deploy     # publication sur robingirard.eu, en version figée
```

Prérequis : TeX Live avec `lualatex` et TikZ ; Poppler (`pdftocairo`) ; Python 3 avec PyYAML ;
Node ≥ 18 pour les tests ; Google Chrome pour les captures automatiques.

## Organisation

```
pack.yaml              ce qu'est ce paquet, et quelle version de moteur il sait consommer
content/
  units.yaml           unités « liaisons » et « schéma », qui emploient les générateurs
  units/*.yaml         les 18 autres unités, exercices écrits explicitement
  lessons/*.md         les leçons (Markdown restreint, figures {{fig:…}}, tables {{table:…}})
  liaisons.yaml        les 10 liaisons : ddl, efforts, contacts, exemples, symboles, animations
  mecanismes/*.yaml    un mécanisme = pièces, classes d'équivalence, liaisons, animation
  animations.yaml      mouvements des figures de transmission
  annales.yaml         sujets officiels, référencés par lien
  droits-admis.yaml    formulations reprises des manuels et jugées non protégeables
generators/            les générateurs d'exercices propres à ce paquet (liaisons, mécanismes)
figures/tikz/          les sources TikZ, dont liaisons.sty (symboles normalisés, hachures)
docs/SPEC.md           format du contenu, planificateur, progression
docs/PLAN-V2.md        où va le projet
docs/REPRISE.md        par où reprendre le travail
```

`docs/notes/` — les transcriptions des manuels — est **exclu de git** : voir `LICENSE`.

## Ajouter du contenu

- **Une unité** : un fichier dans `content/units/`, vérifié par `make check`.
- **Une liaison, un exemple** : éditer `content/liaisons.yaml` ; les exercices sont **engendrés**.
- **Un mécanisme** : `content/mecanismes/<id>.yaml` plus ses quatre figures ; un bloc `animation`
  le fait bouger.
- **Une figure** : une source TikZ dans `figures/tikz/`, appelée par `{{fig:<id>}}`.

Les identifiants d'exercices sont stables : reconstruire ne remet aucune progression à zéro.

## Droits

Contenu en **CC BY 4.0**, code en **MIT**, détail dans `LICENSE`. Aucun texte de manuel n'est
redistribué : `make check` compare ce qui part en ligne aux transcriptions locales et **échoue**
dès qu'une reprise littérale n'a pas été examinée.

## Comment c'est fait, et pourquoi ça se critique

L'essentiel de ce contenu a été écrit **avec Claude**, sous relecture. Cela vaut pour la justesse
scientifique comme pour l'ergonomie : une erreur de physique, un énoncé ambigu, une figure fausse
ou un enchaînement pénible sur téléphone sont des défauts possibles, et attendus.

La critique des utilisateurs est le mécanisme de correction prévu, pas un service après-vente.
Si un exercice vous paraît faux, c'est une contribution — écrivez à robin.girard@minesparis.psl.eu.
