# Reprise du travail (état au 17 sept. 2026, fin de la 11e session)

## Publié (17 sept. 2026)
22 unités, 98 compétences, 2 406 exercices dont 101 exercices complets guidés, 379 figures, 7 mécanismes animés
(serre-joint, étau, bielle-manivelle, pompe à main, essuie-glace, benne à vérin, cric losange), 6 figures de
transmission animées, symboles des 10 liaisons en perspective (3D), 13 annales.
Site : https://www.robingirard.eu/Revise.html — l'application en https://www.robingirard.eu/assets/revise/sti2d/v1.0/index.html

Unités : ingénierie (liaisons, schéma cinématique, transmission, cinématique, **unités et conversions**,
**solutions constructives et cotation**, statique-RDM, information 1re+Tle, 2I2D Tle : analyse fonctionnelle,
énergie électrique, bâtiment, structures-matériaux), physique-chimie (électricité, thermique, chimie, ondes,
mécanique, compléments Tle), maths (1re ; Tle spécialité PCM ; Tle enseignement commun).

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
6. Côté site (`~/Documents/Communication/robingirarddoteu`) : reconstruire avec
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

## Fait à la 7e session (7 sept. 2026) — la fiche de dérivation du cours

Robin a déposé dans `~/Documents/Enseignement/STI2D/fiches_exos_encours/` la fiche distribuée en
classe le jour même (« BO Dérivation », cours à trous en 4 pages). Décision : compléter la
compétence `maths-derivee` avec ce qui y figurait et manquait, en **gardant les valeurs de la
fiche** pour que le fils retrouve son cours (les PDF restent hors dépôt ; on n'en recopie pas le
texte, voir `docs/notes/fiches-classe.md`).

- **La tangente par trois méthodes**, comme au tableau : lecture graphique de
  $m=\dfrac{\Delta y}{\Delta x}$ (nouvelle figure `maths-tangente-lecture`, quadrillage au pas de
  1 et triangle à compter), la formule, et la forme $y=mx+p$ où $p$ vient d'une équation.
- **Lecture d'un écran de calculatrice en mode tangente** (nouvelle figure
  `maths-tangente-calculatrice`, sans marque) : la machine donne $x$, $f(x)$ et $f'(x)$, l'équation
  reste à écrire. Les deux figures ont leur variante muette (`\rappel`), l'énoncé ne donne donc
  jamais la formule ni le résultat.
- **Composées et inverse** : $(ax+b)^n$, un `match` de cinq composées, et $\left(\dfrac1v\right)'$.
- **Les trois tangentes de la fiche** ($-x^2+2x+4$ en $3$, $x^3+1$ en $-2$, $x\sqrt x$ en $4$).
- **Exercice guidé en 8 étapes** sur l'étude globale de la fiche, $f(x)=\sqrt x\,(x-3)$ :
  non-dérivabilité en $0$, dérivée d'un produit avec $\sqrt x$, factorisation
  $f'(x)=\dfrac{3(x-1)}{2\sqrt x}$, signe, tableau de variations, minimum $-2$.
- Leçon `maths-derivee.md` complétée (section « trois méthodes », formule $(ax+b)^n$, $1/v$).

`maths-derivee` passe de 23 à 34 exercices ; total **2 119 exercices**, 338 figures. Vérifié :
`check_unit.py`, `make check`, `make test` (119), `tour.mjs` (0 erreur), `grid-fit` (2 débordements,
les mêmes qu'avant), `math-overflow` (0 erreur KaTeX), captures des nouveaux exercices sur mobile. **Publié** : `sw.js`
en `2026-09-07.1`, v1.0 réécrite (`publish.py --force`), commits poussés sur les trois dépôts, site
reconstruit et vérifié sur l'adresse publique (2 119 exercices, figures servies, KaTeX rendu).
Le `jekyll build` a aussi rattrapé les pages **netzerogame** restées en retard dans `_site/` :
non commitées, à reconstruire et relire à part.

## Défaut de mise à jour trouvé le soir même (7 sept.) — et corrigé

Robin ouvre l'adresse publique après la publication : « L'application n'a pas pu démarrer… (file://) ».
Le site était sain (un navigateur neuf chargeait l'appli sans erreur, trois fois de suite) ; le défaut
était dans la **bascule de version** du service worker. `caches.match()` sans portée interroge **tous**
les caches, y compris celui de la version précédente que l'activation n'a pas encore supprimé : pendant
la fenêtre de mise à jour, un client pouvait recevoir l'ancien `content.js` avec le nouveau `main.js`.

- `sw.js` : le gestionnaire `fetch` n'interroge plus que le cache de **sa** version
  (`caches.open(CACHE).then((c) => c.match(...))`).
- `index.html` : le garde-fou de démarrage ne sert plus en ligne un conseil écrit pour `file://`. En
  http(s) il attend 8 s (téléphone lent) puis propose un bouton **« Réparer et recharger »** qui
  désinscrit le service worker, vide les caches et recharge ; `localStorage` (la progression) est intact.
- Vérifié par `app/dev/` + un scénario de **mise à jour rejouée** : client avec l'ancienne version
  installée, fichiers du serveur remplacés, deux rechargements — l'application démarre, 0 erreur.
  Ce scénario est maintenant un script du moteur, `app/dev/maj.mjs` (ajouté le 11 sept.) :
  `node app/dev/maj.mjs <ancienne version> <nouvelle version> [sortie]`, les deux dossiers étant des
  versions publiées du site. Pour extraire l'ancienne :
  `git archive HEAD~1 assets/revise/sti2d/v1.0 | tar -x -C /tmp/ancienne --strip-components=4`.
  **À rejouer à chaque changement de `sw.js`.** Deux pièges du test lui-même, déjà réglés dedans :
  `Page.navigate` vers la même URL ne recharge que le fragment (il faut `reload()`), et le navigateur
  ne revérifie `sw.js` que quand le cache HTTP le permet — le script force donc l'`update()` qu'il
  finirait par faire.

Publié en `sw 2026-09-07.2`. **Leçon : après un `make deploy`, vérifier non seulement un chargement
neuf, mais un chargement depuis un client qui avait déjà l'ancienne version.**

## Fait à la 8e session (11 sept. 2026) — les limites arrivent, et un lien pour amorcer

Robin dépose quatre photos du tableau (10 et 11 sept.) et le corrigé partiel de « BO Dérivation »,
et signale que **le fils n'a toujours pas ouvert l'application**. Choix arrêté avec lui : intégrer
le contenu du cours **et** fournir un lien de séance à lui envoyer, le devoir de lundi 14/09
(exercices 5 et 9 p. 41, noté au tableau) servant de prétexte.

- **`maths-derivee` : 34 → 41 exercices.** Les cinq exemples traités au tableau le 11 sept., avec
  leurs valeurs — $\dfrac{2x-5}{x+1}$, $\sqrt x(2x+1)$, $\cos(3x+7)$, $\dfrac{x^2}{2-x}$,
  $\dfrac{1-3x}{7x-2}$ (celui-ci en `input` : le numérateur $u'v-uv'$ se réduit à $-1$, ce qui donne
  un contrôle gratuit). S'y ajoutent un `match` « reconnaître la forme avant de dériver » et un
  `order` sur la méthode du quotient. Leçon complétée d'une section « La méthode qui évite les
  erreurs » : accolade $u$/$v$/$u'$/$v'$ à part, dénominateur jamais développé, signe devant $uv'$.
- **`mathstc-inverse-derivation` : 20 → 26 exercices**, renommée « Fonction inverse, limites et
  lecture de courbes ». Notation `lim`, grille des quatre limites ($\pm\infty$ et les deux côtés de
  $0$), lecture d'un tableau de valeurs, pourquoi la limite en $0$ exige de préciser le côté, et
  l'algorithme de seuil (`order` sur les quatre lignes du corps + `input` : $A=350\,000$ → $N=6$).
  Leçon complétée de deux sections. Le programme du tronc commun restant en approche intuitive,
  aucune définition d'asymptote n'est donnée.
- **Défaut du moteur corrigé** : `shot-items.mjs` documentait « compétence::exercice » mais
  `buildSkillSession` attend l'identifiant **complet** (`compétence.hXXXXXXXX`) ; la partie courte
  lançait une séance ordinaire et capturait le mauvais exercice **sans rien signaler**. Le script
  accepte les deux écritures et échoue maintenant sur un exercice inconnu.

2 119 → **2 132 exercices**. Vérifié : `check_unit.py`, `make check` (aucune reprise non admise),
`make test` (119), `tour.mjs` (0 erreur), `grid-fit` (2 débordements, les mêmes qu'avant),
`math-overflow` (0 erreur KaTeX — `\substack` et `\displaystyle` passent), captures mobiles des
13 nouveaux exercices. **Publié** : `sw.js` en `2026-09-11.1`, v1.0 réécrite (`publish.py --force`),
poussé sur les trois dépôts, site reconstruit (diff propre, 14 fichiers, rien de netzerogame).

- **Défaut du moteur trouvé en relisant la leçon en ligne** : un `**gras**` qui **enjambe une
  formule** n'était pas rendu, les astérisques s'affichaient telles quelles. `renderRich` extrayait
  les jetons (code, figure, maths) et appliquait la mise en forme à chaque morceau séparément : les
  deux moitiés de la paire tombaient dans deux morceaux différents. Les jetons sont maintenant mis
  de côté derrière un marqueur, la mise en forme s'applique à la chaîne entière, puis les jetons
  reviennent. **13 textes du paquet étaient touchés depuis l'origine** (« pivot d'axe $(A,\vec y)$ »,
  « signe de $k$ », « variations de $f$ », « au point $A$ »…) et sont réparés — sans changement
  d'identifiant, la mise en forme ne touchant pas la source. Test de non-régression, 120 tests.
  Republié en `sw 2026-09-11.2`.

**Liens directs** (à envoyer par SMS). Vérifiés sur l'adresse publique depuis un navigateur neuf :

- séance de dérivation, celle du devoir de lundi — démarre l'exercice sans rien toucher :
  `https://www.robingirard.eu/assets/revise/sti2d/v1.0/index.html#/session/maths-derivee`
- les limites — `#/session/…` **retombe sur l'écran de la compétence**, car
  `mathstc-inverse-derivation` a `mathstc-exp-log` pour prérequis et reste verrouillée pour un profil
  neuf. Donner directement l'écran de compétence, qui affiche la **leçon** complète (limites et
  algorithme de seuil), lisible même verrouillée :
  `…/index.html#/skill/mathstc-inverse-derivation`

Règle générale : `#/session/<compétence>` ne démarre une séance que si la compétence est
déverrouillée ; sinon `renderSessionEntry` renvoie sur `#/skill/<compétence>` (sans erreur).

## Idées suivantes
- Retours d'usage du fils : longueur des séances, difficulté, figures trop larges sur mobile (quelques diagrammes
  SysML et le treillis dépassent 8 cm : à resserrer si gênant).
- Relecture par Robin des points « à vérifier » listés dans les notes et des données introduites hors manuel
  (signalées dans les rapports des agents : valeurs de bâtiment, lectures graphiques de courbes de batteries).
- Autres mécanismes (pince de robot, table élévatrice…) ; le corrigé APMEP de Polynésie 2025 n'existe pas.


## Fait à la 9e session (17 sept. 2026) — le DS de conversions, et trois chapitres du lot de scans

Robin dépose 24 photos de documents de classe (`../scans/sources/scan-20260917/`, originaux HEIC +
copies lisibles dans `jpg/`) et signale un **DS de SI sur les conversions le mercredi 23 sept.**
Contenu des photos et ce qui en a été tiré : `docs/notes/fiches-classe.md`, section du 14 sept.
Décision de Robin : tout intégrer, publier une seule fois.

### Nouvelle unité « Unités et conversions » (`content/units/05-conversions.yaml`, 109 exercices)
Cinq compétences, transversales à toutes les matières :
`conv-prefixes` (préfixes n/µ/m/k/M/G, écriture scientifique, loi d'Ohm avec conversion préalable),
`conv-surfaces` (facteur 100, are et hectare, aire du disque), `conv-volumes` (facteur 1000, le pont
$1\ \ell = 1\ \mathrm{dm^3}$, cylindre), `conv-temps-vitesses` (sexagésimal contre décimal, le facteur 3,6
retrouvé comme $3\,600/1\,000$), `conv-grandeurs-composees` (débits, masses volumiques, kWh, MPa, homogénéité).
Cinq exercices guidés dont les deux problèmes de la fiche : le robinet et la citerne, le chasse-neige.
**Les valeurs des fiches sont conservées** (documents du professeur, règle des 7e et 8e sessions) : le fils
doit pouvoir vérifier ses propres réponses. Prérequis volontairement plats — tout part de `conv-prefixes`,
pour qu'aucune compétence ne soit à plus d'un cran avant le DS.
Huit figures : `conv-escalier-prefixes`, `conv-tableau-surfaces`, `conv-cube-metre`, `conv-cercle-cylindre`,
`conv-loi-ohm`, `conv-vitesses-passage`, `conv-chasse-neige`, `conv-debit-citerne` (six avec variante muette).

### Nouvelle compétence `2i2d-energie-puissance-instantanee` (20 exercices)
Le chapitre 1 « Énergie, puissance et rendement » du cours de TSTI2D, qui fait le pont entre les
mathématiques et la chaîne d'énergie : la puissance moyenne comme **pente d'une sécante**, la puissance
instantanée comme **dérivée** $p(t)=\mathrm{d}E/\mathrm{d}t$, l'énergie comme **aire sous $p(t)$** approchée par
des rectangles, le formulaire de dérivées écrit en $t$, le bilan $E_a=E_u+E_p$ et le rendement.
Guidé : le relevé d'une habitation sur 24 h, avec le tracé de $p(t)$ en escalier.
Figures `2i2d-velo-energie`, `2i2d-puissance-aire-rectangles`, `2i2d-habitation-releve`, `2i2d-habitation-puissance`.

### Nouvelle unité « Solutions constructives et cotation » (`content/units/15-solutions-constructives.yaml`, 58 exercices)
`sc-liaison-complete` (surfaces fonctionnelles, positionnement radial/axial, association de deux liaisons
simples, MAP contre MEP — « une surface positionne, un organe maintient »), `sc-assemblages` (démontables
et non démontables, transmission d'action par clavette, cannelures, goupille), `sc-ajustements` (CN, ES/EI
et es/ei, IT, cotes limites, jeu et serrage, H7/g6, H7/m6, H7/p6). Valeurs vérifiées sur les tables :
$\varnothing20$ H7 $= 20{,}021/20{,}000$, m6 $= 20{,}021/20{,}008$ (incertain) ; $\varnothing18$ H7/g6 (avec jeu).
Figures `sc-liaison-complete`, `sc-tolerances`, `sc-jeu-serrage`.

### Maths : les erreurs réelles du devoir corrigé
Le devoir « Automatismes » rendu noté montre deux trous précis, repris en exercices ciblés :
l'équation de la tangente écrite **en $a=1$ alors que l'énoncé demandait $a=0$**, puis rendue comme un
**nombre** au lieu d'une droite (4 exercices dans `maths-derivee`, sur $f(x)=2x^3-x^2-3x+9$, la fonction du
devoir) ; et les **quatre limites de $1/x$** laissées vides, notées 0/1 (4 exercices dans
`mathstc-inverse-derivation`, dont le repérage des écritures fautives).

### Un outil de plus : `lesson-fit`
`math-overflow.mjs` ne voit pas les formules **d'affichage** (`$$…$$`) des leçons : il mesure les chaînes
avec `renderRich`, qui ne les rend pas. Un script ad hoc rendant chaque leçon avec `renderLesson` à 390 px
et mesurant `scrollWidth` des `.katex-display` a révélé 14 formules débordant dans les leçons neuves
(jusqu'à 320 px) — toutes coupées en deux depuis. Le corpus ancien en compte 43, jamais signalées : elles
défilent horizontalement (`.math-display` est en `overflow-x: auto`), mais c'est une gêne de lecture sur
téléphone. **Candidat à ajouter dans `revise-core/app/dev/`.**

Autre piège rencontré : dans une carte « Contexte » d'exercice guidé, une figure est en `.fig-block`
(`max-height: 240px; width: auto`) et non en `.prompt .fig`. Une figure presque carrée y est donc bridée
par sa **hauteur** et s'affiche minuscule. Les graphes doivent viser un rapport d'environ **2:1** et des
étiquettes en `\small`, sans quoi elles sont illisibles sur un téléphone.

Vérifié : `check_unit.py` sur les trois fichiers, `make check`, `make test` (120), `tour.mjs` (0 erreur),
`grid-fit` (92 grilles, les 2 débordements connus), `math-overflow` (0 erreur KaTeX), `lesson-fit`,
captures mobiles des nouveaux guidés. **Publié** : `sw.js` en `2026-09-17.1`, v1.0 réécrite
(`publish.py --force`), poussé sur les trois dépôts, site reconstruit et vérifié en ligne.
Au passage, le `jekyll build` a rattrapé `_site/index.html` et `_site/print.html`, restés en retard sur le
lien « LinkedIn posts » ; `.sass-cache/` est passé dans le `.gitignore` du site.

### Défaut trouvé juste après la publication (17 sept., par Robin sur le lien envoyé)
Robin ouvre `#/session/conv-prefixes` et reçoit **« Introuvable — Cette page n'existe pas »**, alors
que le serveur est sain (`liste.json` contient `conversions`, `content/conversions.js` répond 200, un
navigateur neuf ouvre l'exercice). Cause : son navigateur exécutait encore la version du 11 sept., dont
le `content.js` ignore la compétence — `sess.findSkill` rend `undefined`, et le routeur tombait sur son
404 générique. `maj.mjs` le montre : **au premier rechargement après un déploiement, le client sert
encore l'ancien contenu** ; c'est au deuxième que la bascule se fait.

Corrigé dans le moteur (`sw 2026-09-17.2`) : `renderNotFound` reçoit la compétence demandée et, quand il
y en a une, explique que **cette version ne la connaît pas** et propose **« Mettre à jour et réessayer »**
(désinscrit le service worker, vide les caches, recharge — le fragment d'URL survit, donc le lien
aboutit ; `localStorage` n'est pas touché). Même geste que le bouton « Réparer et recharger »
d'`index.html`, qui ne se déclenche lui que sur un écran blanc, pas sur une route inconnue.

**Le correctif ne sauve pas les clients déjà en retard** (ils exécutent l'ancien `main.js`) : pour
eux, **deux rechargements**. Il vaut pour toutes les publications suivantes.
**Règle à retenir : un lien vers une compétence NOUVELLE ne marche pas du premier coup sur un
téléphone qui a déjà l'application** — le dire en envoyant le lien, ou envoyer d'abord l'adresse nue
pour laisser la mise à jour se faire.

## Fait à la 10e session (17 sept. 2026) — ITEC, la spécialité enfin connue

**Robin confirme : la spécialité 2I2D de son fils est ITEC** (innovation technologique et
éco-conception). C'était le point 1 de LA SUITE, ouvert depuis le 5 sept. Classe : T STI2D B.

Ce que les quatre sujets ITEC d'éduscol déjà référencés dans `content/annales.yaml` demandent en
partie spécifique (vélodrome 2023, PV flottant 2024, éolienne 2025, Hélilock 2026) : **modélisation
et comportement mécanique** — schéma cinématique, liaisons, cinématique, statique, RDM, matériaux.
Tout cela est déjà couvert. Ce qui manquait relève plutôt du **cours du professeur**, dont les scans
du 14 sept. montrent qu'il va bien au-delà de l'épreuve. Quatre compétences ajoutées :

- **`sc-guidages`** (18 ex.) dans l'unité « Solutions constructives et cotation » — palier lisse
  contre roulement, types de roulements, la règle des ajustements (bague tournante **par rapport à
  la charge** $\rightarrow$ serrée), les arrêts axiaux des deux côtés, côté fixe et côté libre pour
  la dilatation, lubrification, guidage en translation. Guidé : l'arbre d'un treuil.
- **`sc-chaines-cotes`** (19 ex.), même unité — condition fonctionnelle, tracé de la chaîne, règle
  des signes, calcul au **pire cas**, $IT(J_a)=\sum IT$, et la règle de conception qui en découle
  (une chaîne courte est une chaîne précise). Guidé : le jeu de montage d'une roue.
- **`sc-dessin-technique`** (19 ex.) — nouvelle unité `16-dessin-procedes.yaml` — dessin de
  définition contre dessin d'ensemble, cartouche et nomenclature, **projection européenne**
  (dessus en dessous, gauche à droite), les quatre types de traits, coupes et sections, la règle des
  hachures, les pièces jamais coupées, et le piège de l'échelle (une cote donne toujours la
  dimension réelle). Guidé : lire l'équerre percée.
- **`sc-procedes`** (19 ex.), même unité — enlèvement / déformation / ajout, tournage contre
  fraisage, le trio **forme–matériau–quantité**, le **point d'équilibre** entre outillage et coût
  unitaire (calculé, jamais appris par cœur), obtenir puis reprendre, fabrication additive et
  prototypage. Guidé : choisir le procédé d'un support de capteur.

Six figures : `sc-roulement`, `sc-montage-roulements`, `sc-chaine-cotes`, `sc-projections`,
`sc-coupe` (cinq avec variante muette). **2 402 exercices, 98 compétences, 372 figures.**

**Le piège de la taille des figures, confirmé et généralisé.** Un SVG s'affiche à sa taille
**intrinsèque** (celle du `.tex`, en cm) tant qu'il ne dépasse ni `max-width: 100%` ni
`max-height: 240px` : il n'est jamais agrandi. Une figure de 9 cm de large rendue dans une carte de
440 px occupe donc environ 355 px, et des étiquettes en `\footnotesize` y deviennent illisibles.
**Règle : viser 9-10 cm de large, un rapport d'environ 2:1, et des étiquettes en `\small` au
minimum.** Les figures des sessions 9 et 10 ont toutes été reprises sur ce critère.

Vérifié : `check_unit.py` sur les deux fichiers, `make check`, `make test` (120), `tour.mjs`
(0 erreur), `grid-fit` (97 grilles, les 2 débordements connus), `math-overflow` (0 erreur KaTeX),
`lesson-fit` (0 débordement sur les leçons neuves), captures mobiles des guidés.

**Reste à faire pour ITEC** (LA SUITE point 5) : des **exercices guidés « à la manière des » sujets
ITEC**, qui ré-emploient les compétences existantes dans le format long de l'épreuve — c'est là que
se joue l'entraînement au bac, plus que dans de nouvelles connaissances.

## Fait à la 11e session (17 sept. 2026) — les sujets type bac ITEC (LA SUITE, point 5)

Les 90 exercices guidés d'alors faisaient 6 à 8 étapes et restaient dans **une** compétence.
Ce qui manquait pour le bac, c'est le **format de l'épreuve** : la partie spécifique de 2I2D
enchaîne 10 à 15 questions sur **un seul système**, traverse plusieurs compétences et se termine
par un « conclure ». Les quatre sujets ITEC d'éduscol ont donc été lus (le texte des PDF
**s'extrait bien avec `pdftotext`** — contrairement à ce que dit `docs/biblio.md` §6, qui parlait
du lecteur d'un outil web), puis **ré-écrits avec un autre support et d'autres valeurs**. Rien
n'est recopié : les agents rédacteurs n'ont jamais vu le texte des sujets, seulement une fiche de
mission décrivant le système inventé, les données et la chaîne de questions.

**Quatre « sujets type bac ITEC » de 12 étapes**, rattachés au champ `guided:` de
`content/annales.yaml`, resté vide sur les 13 annales depuis l'origine — le bouton
« S'entraîner » de l'écran Annales existait dans le moteur et ne servait jamais :

| annale | sujet type | compétence d'accueil | fil |
|---|---|---|---|
| 2026 ITEC, Hélilock | centrage automatique de tubes sur une découpeuse laser | `schema-2d` | 4 classes d'équivalence, grille des liaisons, chaîne fonctionnelle, double filetage, $v$ puis $P$, traction, $S$, $\sigma$, $s = 6{,}4$ |
| 2025 ITEC, ferme éolienne | hydrolienne fluviale | `vitesses` | mouvement, trajectoire, $\omega$, $V_t$, km·h⁻¹, conclure, $\lambda$, poids, force centrifuge, position dimensionnante, effort, conclure |
| 2024 ITEC, PV flottant | ombrière photovoltaïque de parking | `2i2d-materiaux-choix` | $\alpha = 15{,}2°$, conformité, 4 actions, solide à 2 forces, 4 800 N, traction, $S$, $\sigma$, $s = 3{,}8$, conclure, grille de 3 matériaux, choix argumenté |
| 2023 ITEC, vélodrome | circuit de karting : virage relevé et monte-charge | `acceleration` | angle de frottement, non-glissement, inclinaison et vitesse, $V_e = 50{,}6$ km·h⁻¹, rôle du dévers, roulement sans glissement, $\omega$, rayon primitif, $0{,}075$ m·s⁻¹, conclure |

Cinq figures : `guide-bac-centrage-tube`, `guide-bac-hydrolienne`,
`guide-bac-hydrolienne-positions`, `guide-bac-ombriere`, `guide-bac-virage-releve` — toutes avec
leur variante muette (`\rappel`). **2 402 → 2 406 exercices, 101 guidés, 379 figures.**

### Le prérequis d'une annale doit nommer la compétence d'accueil de son guidé

`renderSessionEntry` renvoie sur l'écran de compétence si celle-ci est verrouillée : un bouton
« S'entraîner » qui lance une séance sur une compétence non déverrouillée n'ouvre donc pas
l'exercice. Trois annales avaient déjà le bon prérequis ; celle de 2024 demandait `ddl` + `contacts`,
qui n'impliquent pas `2i2d-materiaux-choix` — elle demande maintenant
`{skill: 2i2d-materiaux-choix, level: 2}`, ce qui colle mieux à ce que le sujet demande
(statique, RDM, choix de matériau).

### DÉFAUT DU MOTEUR : deux copies d'une figure sur le même écran cassaient le détourage

Trouvé en relisant les captures mobiles : dans le sujet du karting, la coupe du virage arrivait
**hachurée sur toute sa surface**, alors que le PDF ne hachure que le sol. Reproduit hors de
l'application : une figure insérée **deux fois** dans la même page porte deux fois les mêmes `id`,
`url(#…-clip-0)` résout sur la **première** copie — celle du « Contexte », replié dès l'étape 2 —
et Chrome ignore un `clipPath` pris dans un sous-arbre masqué. Les hachures de `\hachures`
débordaient alors sur toute la figure.

Corrigé dans `revise-core/app/js/figures.js` : `uniquifyIds(svg, suffixe)` suffixe les `id` et
leurs références (`url(#…)`, `href="#…"`) à chaque injection, `inject()` l'applique avec un
compteur d'instance. Deux tests de non-régression (122 tests).

**Le défaut ne touchait pas que le contenu neuf : dix étapes déjà en ligne étaient cassées**, les
sept exercices « du mécanisme au schéma » (`schema-2d.complet.*`, serre-joint, étau, cric losange,
essuie-glace, benne à vérin, pompe à main, bielle-manivelle), où le dessin d'ensemble est rappelé
dans une étape. Vérifié réparé sur le serre-joint.

### Deux conventions à connaître

- **La virgule décimale dans `answer:`.** Les 280 réponses numériques existantes utilisent le
  point ; le contenu neuf écrit `answer: '13,2'`. `normalizeAnswer` convertit la virgule en point
  **des deux côtés** avant comparaison, donc les deux écritures marchent — et le bandeau affiche
  « Réponse attendue : 50,3 mm² » à la française. On garde la virgule pour le neuf sans reprendre
  l'ancien.
- **Le contexte d'un guidé n'est déplié qu'à la première étape** (`intro.open = index === 0`) :
  une figure dont une étape tardive a besoin doit être **répétée dans son énoncé**, sans quoi
  l'élève doit déplier le contexte pour lire une cote.

### Un outil de plus : `guided-walk`

`revise-core/app/dev/guided-walk.mjs` parcourt un exercice guidé étape par étape et capture
chacune, énoncé puis correction, sur un écran de 390 px :
`node app/dev/guided-walk.mjs <dist> <sortie> "<compétence>::<id complet>" …` C'est lui qui a rendu le défaut des hachures visible : `tour.mjs` ne joue que
la première étape d'un guidé. Il bloque sur les étapes `match`, qui demandent d'apparier les deux
colonnes.

Vérifié : `make check` (aucune reprise non admise), `make test` (122), `tour.mjs` (0 erreur),
`grid-fit` (97 grilles, les 2 débordements connus), `math-overflow` (0 erreur KaTeX, 6
débordements connus), captures mobiles des quatre sujets et d'un guidé ancien.
**Publié** : `sw.js` en `2026-09-17.4`, v1.0 réécrite (`publish.py --force`), `maj.mjs` passe
(0 erreur ; 2 402 exercices au 1er rechargement, 2 406 au 2e, comme attendu), site reconstruit
(diff propre, 40 fichiers, rien d'étranger) et poussé sur les trois dépôts.

**Vérifié sur l'adresse publique** : 2 406 exercices, les dix SVG `guide-bac-*` servis (200),
service worker actif, 0 erreur ; l'écran Annales affiche **4 boutons « S'entraîner »**, celui de
l'annale 2026 mène à `#/session/schema-2d?item=schema-2d.h92bbc17a&seed=1` et ouvre bien
« Étape 1 / 12 » avec KaTeX rendu (0 repli `span.math`) et les hachures correctement détourées.

**Piège rencontré pendant cette vérification, déjà connu mais oublié** : `location.href` vers la
même URL ne change que le **fragment**, la page ne recharge pas — un `localStorage` écrit juste
avant n'est donc jamais relu. Il faut un `location.reload()`, comme le fait `maj.mjs`.

### Ce qui reste du point 5
Les neuf autres annales (EE, SIN, et les six « physique-chimie et mathématiques » de l'APMEP)
n'ont pas encore de sujet type. Les plus utiles ensuite : `mathstle-equadiff` (2026,
refroidissement), `mathstle-integrale` (2025, puissance sinusoïdale et primitive),
`mathstle-exp-ln` (2024, niveau sonore) et `mathstle-complexes-exp` (2025 Polynésie, aire sous
$v(t)$).
