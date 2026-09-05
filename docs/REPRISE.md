# Reprise du travail (état au 4 sept. 2026, fin de la 3e session)

## Publié (gh-pages, 5 sept. 2026)
19 unités, 84 compétences, 2 058 exercices dont 80 exercices complets guidés, 296 figures, 7 mécanismes animés
(serre-joint, étau, bielle-manivelle, pompe à main, essuie-glace, benne à vérin, cric losange), 6 figures de
transmission animées, symboles des 10 liaisons en perspective (3D), 13 annales.
Site : https://robingirard.github.io/revise-pour-le-bac-sti2D/

Unités : ingénierie (liaisons, schéma cinématique, transmission, cinématique, statique-RDM, information 1re+Tle,
2I2D Tle : analyse fonctionnelle, énergie électrique, bâtiment, structures-matériaux), physique-chimie (électricité,
thermique, chimie, ondes, mécanique, compléments Tle), maths (1re ; Tle spécialité PCM ; Tle enseignement commun).

## Où va le projet
`docs/PLAN-V2.md` — plan arrêté le 5 sept. 2026 : moteur et contenu dans deux dépôts, contenu
découpé par matière et chargé à la demande, profils d'élèves avec carte d'identité exportable,
retours par mail, index sur robingirard.eu, bibliothèque de figures partagée. L'ordre de travail
est en §7. Rien n'est encore fait.

## Comment vérifier / publier
1. Pour chaque unité : `python3 tools/check_unit.py content/units/<fichier> docs/figures-todo-<fiche>.md`.
2. `make content` (échoue tant qu'une figure référencée manque) → `make check` → `make test`.
3. Animations : `node app/dev/mech-bench.mjs <ids de figures séparés par des virgules> <dossier>` (4 captures).
4. `node app/dev/tour.mjs dist <dossier>` (captures de l'appli), incrémenter `VERSION` dans `app/sw.js`,
   `git commit`, `make deploy`, vérifier le site (content.js, une figure, sw.js).

## Notes et archive
- `docs/notes/` (gitignoré, local) : 25 notes (transcriptions des manuels + `maths-tle-programme.md` : programme
  officiel de la spécialité, épreuve, annales APMEP). Index `docs/notes/README.md`.
- `../scans/` : pages des deux manuels ; pages non scannées 88-93 et 126-127 = corrigés seulement.

## Idées suivantes
- Retours d'usage du fils : longueur des séances, difficulté, figures trop larges sur mobile (quelques diagrammes
  SysML et le treillis dépassent 8 cm : à resserrer si gênant).
- Relecture par Robin des points « à vérifier » listés dans les notes et des données introduites hors manuel
  (signalées dans les rapports des agents : valeurs de bâtiment, lectures graphiques de courbes de batteries).
- Autres mécanismes (pince de robot, table élévatrice…) ; le corrigé APMEP de Polynésie 2025 n'existe pas.
