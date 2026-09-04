# Reprise du travail (état au 4 sept. 2026, fin de la 3e session)

## Publié (gh-pages, depuis le commit 60f8eff)
18 unités, 78 compétences, 1 834 exercices dont 74 exercices complets guidés, 269 figures, 6 mécanismes animés
(serre-joint, étau, bielle-manivelle, pompe à main, essuie-glace, benne à vérin), 6 figures de transmission animées,
13 annales (2I2D + physique-chimie et maths 2020-2026). Site : https://robingirard.github.io/revise-pour-le-bac-sti2D/

Unités : ingénierie (liaisons, schéma cinématique, transmission, cinématique, statique-RDM, information, 2I2D Tle :
analyse fonctionnelle, énergie électrique, bâtiment, structures-matériaux), physique-chimie (électricité, thermique,
chimie, ondes, mécanique, compléments Tle), maths (1re, Tle spécialité).

## Comment vérifier / publier
1. Pour chaque unité : `python3 tools/check_unit.py content/units/<fichier> docs/figures-todo-<fiche>.md`.
2. `make content` (échoue tant qu'une figure référencée manque) → `make check` → `make test`.
3. Animations : `node app/dev/mech-bench.mjs <ids de figures séparés par des virgules> <dossier>` (4 captures).
4. `node app/dev/tour.mjs dist <dossier>` (captures de l'appli), incrémenter `VERSION` dans `app/sw.js`,
   `git commit`, `make deploy`, vérifier le site (content.js, une figure, sw.js).

## Notes et archive
- `docs/notes/` (gitignoré, local) : 24 notes (transcriptions des manuels + `maths-tle-programme.md` : programme
  officiel de la spécialité, épreuve, annales APMEP). Index `docs/notes/README.md`.
- `../scans/` : pages des deux manuels ; pages non scannées 88-93 et 126-127 = corrigés seulement.

## Idées suivantes
- Tronc commun de maths Tle (§ 4 de la note maths : hors épreuve écrite, contrôle continu).
- Retours d'usage du fils : longueur des séances, difficulté, figures trop larges sur mobile (quelques diagrammes
  SysML et le treillis dépassent 8 cm : à resserrer si gênant).
- Relecture par Robin des points « à vérifier » listés dans les notes et des données introduites hors manuel
  (signalées dans les rapports des agents : valeurs de bâtiment, lectures graphiques de courbes de batteries).
- Symboles 3D, autres mécanismes, corrigé Polynésie 2025 (URL à relever sur https://www.apmep.fr/STI2D-2025).
