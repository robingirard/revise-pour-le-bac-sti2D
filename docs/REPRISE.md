# Reprise du travail (état au 6 sept. 2026, fin de la 5e session)

## Publié (6 sept. 2026)
19 unités, 84 compétences, 2 081 exercices dont 81 exercices complets guidés, 303 figures, 7 mécanismes animés
(serre-joint, étau, bielle-manivelle, pompe à main, essuie-glace, benne à vérin, cric losange), 6 figures de
transmission animées, symboles des 10 liaisons en perspective (3D), 13 annales.
Site : https://www.robingirard.eu/Revise.html — l'application en https://www.robingirard.eu/assets/revise/sti2d/v1.0/index.html

Unités : ingénierie (liaisons, schéma cinématique, transmission, cinématique, statique-RDM, information 1re+Tle,
2I2D Tle : analyse fonctionnelle, énergie électrique, bâtiment, structures-matériaux), physique-chimie (électricité,
thermique, chimie, ondes, mécanique, compléments Tle), maths (1re ; Tle spécialité PCM ; Tle enseignement commun).

## Où en est la publication (6 sept. 2026)
Une seule adresse publique : **https://www.robingirard.eu/Revise.html**, l'application en
`assets/revise/sti2d/v1.0/`. `make deploy` y publie via `publish.py` du moteur ; la branche
`gh-pages` a été supprimée et l'ancienne adresse GitHub ne répond plus.

Deux dépôts : le **moteur** `revise-core` (GitLab persee, MIT) et ce **paquet de contenu**
(GitHub, CC BY). À décider : déplacer le paquet sur GitLab sous un nom sans « pour-le-bac »
— Robin doit créer le projet vide, le reste suit.

## Où va le projet
`docs/PLAN-V2.md` — plan arrêté le 5 sept. 2026 : moteur et contenu dans deux dépôts, contenu
découpé par matière et chargé à la demande, profils d'élèves avec carte d'identité exportable,
retours par mail, index sur robingirard.eu, bibliothèque de figures partagée. L'ordre de travail
est en §7. Rien n'est encore fait.

## Comment vérifier / publier
1. Pour chaque unité : `python3 tools/check_unit.py content/units/<fichier> docs/figures-todo-<fiche>.md`.
2. `make content` (échoue tant qu'une figure référencée manque) → `make check` → `make test`.
3. Animations : `node app/dev/mech-bench.mjs <ids de figures séparés par des virgules> <dossier>` (4 captures).
4. `node app/dev/tour.mjs dist <dossier>` (captures de l'appli, signale les éléments `.error`).
   Ciblé : `node app/dev/shot-items.mjs dist <dossier> "<compétence>::<id d'exercice>"` ;
   grilles : `node app/dev/grid-fit.mjs dist` ; formules : `node app/dev/math-overflow.mjs dist`.
   **Ces scripts écrivent la progression dans localStorage puis rechargent : sans le `reload()`,
   les compétences restent verrouillées et on capture la leçon au lieu de l'exercice.**
5. Incrémenter `VERSION` dans `revise-core/app/sw.js`, `git commit`, `make deploy`.
   Une **correction** se republie avec `publish.py --force` (réécrit v1.0) : passer à une v1.1
   laisserait les téléphones déjà installés sur l'ancienne version.
6. Côté site (`~/Documents/Recherche/robingirarddoteu`) : reconstruire avec
   `export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"` puis `bundle _2.3.19_ exec jekyll build`
   (le `bundle` du système échoue), relire le diff, commiter, pousser.
7. **Vérifier sur l'adresse publique, pas seulement sur `dist/`.** Le 6 sept., KaTeX n'était jamais
   parti en ligne (`vendor/` du `.gitignore` du site) : toutes les formules s'affichaient en code
   source et le service worker ne s'installait plus, alors que tout était juste en local.
   `publish.py` s'arrête maintenant si le site ignore un fichier publié, mais un chargement de
   `https://www.robingirard.eu/assets/revise/sti2d/v1.0/` en Chrome headless (compter `.katex`
   contre `span.math`) reste la vérification qui tranche.

## Notes et archive
- `docs/notes/` (gitignoré, local) : 25 notes (transcriptions des manuels + `maths-tle-programme.md` : programme
  officiel de la spécialité, épreuve, annales APMEP). Index `docs/notes/README.md`.
- `../scans/` : pages des deux manuels ; pages non scannées 88-93 et 126-127 = corrigés seulement.

## Fait à la 5e session (6 sept. 2026)
- **Grilles** : les en-têtes de lignes/colonnes passent par `renderRich` (en maths, une ligne de grille
  est une formule — elles s'affichaient en code source). Le code de case n'est plus écrit dans le tableau
  sauf s'il est bref (mobilités `Tx`, efforts `X`) ; il sert au commentaire d'erreur, où la case se nomme
  sinon « ligne → colonne ». CSS resserré avec `hyphens: auto` (jamais `overflow-wrap: anywhere`, qui coupe
  en plein mot). 39 grilles sur 79 débordaient d'un écran de téléphone, il en reste 2
  (`pc-puissance-electrique`, `pc-dynamique`, à 4 colonnes : elles défilent).
- **Renvois au manuel** : 377 supprimés dans toutes les matières et 74 passages sortis des guillemets
  (la formulation reste, elle n'est plus présentée comme une citation). Les seuls « livre » restants sont
  l'objet posé sur la table en statique. 29 exercices changent d'identifiant (leur **énoncé** nommait le
  manuel) — rappel : l'id se calcule sur `type + prompt`, réécrire une correction ou une leçon ne coûte
  aucune progression.
- **KaTeX publié** : voir le point 7 ci-dessus.

## Fait à la 6e session (6 sept. 2026) — l'énoncé ne donne plus la réponse

Retour de Robin : « sur les chaînes de rendement, tu donnes le résultat avec le schéma ; pareil en maths
pour la formule du produit scalaire — c'est trop facile ».

- **Figures muettes (moteur 1.1.0)** : dans une source TikZ, `\rappel{…}` enveloppe ce qui donne la réponse ;
  `build_figures.py` compile en plus `nom-muet`, où `\rappel` n'affiche rien. La figure complète reste pour
  les **leçons** et les **explications**, la muette va dans les **énoncés**. `\rappel` est défini par
  `figures/tikz/liaisons.sty`. Voir `docs/SPEC.md` §3.1 et la 4e règle du §4 bis.
- **19 figures muselées** : chaîne de rendements en cascade, bilan d'un convertisseur, coefficient U, flux à
  travers une paroi, résistances en série, double périodicité d'une onde, réflexion/transmission, photon,
  produit scalaire, Al-Kashi, sinusoïde, statique (trois forces, couple), basculement, associations de
  batteries et de cellules PV, orientation des panneaux, vérin double effet, éclairement.
- **7 exercices** dont la figure *était* la réponse (tableau des convertisseurs, courbe de chauffage dont la
  légende numérote les étapes à ordonner, demi-équations des piles) : la figure passe de l'énoncé à
  l'`explanation`, où elle sert de correction visuelle.
- **Nouvelle compétence `maths-derivee` (« Dérivation », 23 exercices)** en tête de l'unité maths 1re — il
  manquait la dérivée, pourtant prérequis des primitives (`maths-primitives` en dépend désormais). Nombre
  dérivé, tangente, dérivées usuelles, produit/quotient, composées, signe de $f'$ et variations, extremums,
  applications techniques, exercice guidé d'optimisation. Leçon `content/lessons/maths-derivee.md`,
  figures `maths-nombre-derive`, `maths-tangente-variations`, `guide-maths-bac-tole`.
- **Positionner avant de calculer (angles)** : 4 exercices ajoutés en tête de `maths-cercle-trigo` —
  association mesure ↔ point repéré par une lettre (`maths-cercle-reperage`), grille mesure ↔ quadrant
  (`maths-cercle-quadrants-muet`), signe de $\cos$/$\sin$ ↔ quadrant, remise en ordre dans le sens direct.
- Une soixantaine d'exercices changent d'identifiant (leur énoncé perd la référence de figure) : leur
  progression repart de zéro, ce qui est sans conséquence sur le reste.

## Idées suivantes
- Retours d'usage du fils : longueur des séances, difficulté, figures trop larges sur mobile (quelques diagrammes
  SysML et le treillis dépassent 8 cm : à resserrer si gênant).
- Relecture par Robin des points « à vérifier » listés dans les notes et des données introduites hors manuel
  (signalées dans les rapports des agents : valeurs de bâtiment, lectures graphiques de courbes de batteries).
- Autres mécanismes (pince de robot, table élévatrice…) ; le corrigé APMEP de Polynésie 2025 n'existe pas.
