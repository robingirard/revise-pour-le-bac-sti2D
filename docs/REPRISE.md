# Reprise du travail (état au 4 sept. 2026, fin de session)

## Ce qui est publié
Site : https://robingirard.github.io/revise-pour-le-bac-sti2D/ — dernière publication = 4 unités
(liaisons, schéma cinématique, transmission/transformation, cinématique), KaTeX, annales, bilan parent.

## Ce qui est écrit mais pas encore publié
- 9 unités supplémentaires validées (`python3 tools/check_unit.py <fichier>`), dans `content/units/` :
  10-statique-rdm (68 ex.), 20-information (83), 30-maths-1re (87), 40-pc-electricite (71),
  50-pc-thermique (59), 60-pc-chimie (77), 70-pc-ondes (73), 80-pc-mecanique (76),
  90-pc-tle-complements (74) — avec leurs leçons `content/lessons/*.md`.
- Leurs figures TikZ étaient en cours de dessin par des agents (fiches `docs/figures-todo-*.md`) :
  certaines existent dans `figures/tikz/`, d'autres manquent encore.
- `content/annales.yaml` : 8 sujets (6 éduscol 2I2D, 2 APMEP physique-maths) ; les 2 derniers ont des
  prérequis sur les nouvelles compétences.
- Appli : regroupement de l'accueil par matière (`matiere: ingenierie|physique|maths` sur chaque unité)
  était en cours d'implémentation dans `app/` (tests verts au moment du commit, à vérifier visuellement).

## Pour reprendre (dans l'ordre)
1. `make figures` puis, pour chaque unité : `python3 tools/check_unit.py content/units/NN-*.yaml docs/figures-todo-*.md`
   → liste des figures manquantes.
2. Pour les figures manquantes : relancer un agent « complex-figure-builder » (sans droit de lancer
   d'agents) avec la fiche `docs/figures-todo-<unité>.md`, ou les dessiner à la main dans `figures/tikz/<id>.tex`
   (conventions : `\documentclass[tikz,border=4pt]{standalone}`, `\usepackage{liaisons}`, `\hachures{}`,
   pas de `pattern=`, largeur 6-8 cm).
3. `make content` (échoue tant qu'une figure référencée manque) → `make check` → `make test`
   → `node app/dev/tour.mjs dist <dossier>` pour les captures → `git commit` → `make deploy`.
4. Vérifier l'accueil par matière (captures 90/91 de `app/dev/shots.mjs`), le rendu KaTeX et des blocs de code.

## Notes et archive
- `docs/notes/` (gitignoré, local) : 23 notes de transcription des deux manuels (index `docs/notes/README.md`).
- `../scans/` : pages en images des deux manuels + `INDEX.md` (pages manquantes : 88-93, 126-127 du livre PC-maths).
- `docs/biblio.md` : annales officielles, sites de profs, programmes.

## Idées suivantes
- Exercices guidés tirés des exercices du livre (notes `exercices-*.md`, `pc-*-exercices*.md`) et des annales.
- Mécanismes supplémentaires (pompe, vérin-levier, sécateur, cric…), symboles 3D.
- Maths de Terminale (non scanné), corrigés manquants.
