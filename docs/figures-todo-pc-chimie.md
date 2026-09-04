# Figures à dessiner — unité « Chimie : matière, combustions, piles »

Dix figures TikZ sont référencées par l'unité `pc-chimie` (`content/units/60-pc-chimie.yaml` et
`content/lessons/pc-matiere.md`, `pc-energie-chimique.md`, `pc-combustions.md`,
`pc-oxydoreduction.md`). Tant qu'elles n'existent pas dans `figures/tikz/`, `make content` échoue
avec « figure inconnue » : ces dix fichiers sont donc un **prérequis de build**.

Sources : manuel « Objectif Bac » 1re/Tle STI2D, physique-chimie 1re, p. 15-16, 38-40 et 42-46
(transcriptions : `docs/notes/pc-1re-cours-a.md`, `-b.md`, `-c.md`).

## Conventions communes

- un fichier par figure : `figures/tikz/<ID>.tex`, `\documentclass[tikz,border=4pt]{standalone}` +
  `\usepackage{liaisons}` ;
- couleurs de la bibliothèque : `solideA` (rouge), `solideB` (bleu), `solideC` (rose),
  `solideD` (orange), `solideE` (vert), `solideF` (violet) ;
- **code couleur de l'unité** : oxydation / réducteur = `solideA` (rouge), réduction / oxydant =
  `solideB` (bleu), électrons = `solideE` (vert), feu et combustion = `solideD` (orange) ;
- textes en `\small` / `\scriptsize`, en **français**, avec les notations du livre ($\rho$,
  $R_{\mathrm{th}}$, $M$, $C$, $C_m$, $n$, $x$, $x_{\max}$, $\mathrm{ox}$, $\mathrm{red}$) ;
- formules chimiques en **LaTeX standard** (pas de `mhchem` : l'application charge KaTeX sans
  l'extension `\ce{}`), indices et exposants explicites : `$\mathrm{CO_2}$`, `$\mathrm{Cu^{2+}}$`,
  `$2\,\mathrm{e^-}$` ;
- demi-équations écrites avec le signe **=** (convention du livre), équations-bilan avec
  **$\rightarrow$** ;
- largeur cible ≈ 8 cm (affichage mobile), hauteur ≤ 6 cm ; pas de photo.

---

## 1. `pc-familles-materiaux` — les quatre familles de matériaux

*Utilisée par* : leçon `pc-matiere` (compétence `pc-matiere`, exercices sur les familles).

Quatre **cartouches rectangulaires** en 2 × 2, chacune avec un titre en gras, une icône schématique
et deux ou trois exemples :

- **Matériaux métalliques** (gris) : barre/lingot ; « fer, or ; alliages : bronze, laiton » ;
- **Matériaux organiques** (`solideE`) : feuille + granulé de plastique ; « bois, papier, plastiques » ;
- **Matériaux minéraux** (`solideB`) : cristal ; « roches, verre, céramique, diamant » ;
- **Matériaux composites** (`solideF`) : deux hachures croisées superposées (fibres dans une
  matrice) ; mention « au moins deux matériaux **non miscibles** ».

Sous la cartouche « composites », une accolade vers les trois autres, légendée « assemblage d'au
moins deux familles ». Aucun chiffre : le tableau des densités figure dans la leçon.

## 2. `pc-lewis-molecules` — schémas de Lewis de quatre molécules

*Utilisée par* : leçon `pc-matiere` (exercices sur les doublets liants et non liants).

Quatre schémas alignés, séparés par un filet fin, chacun surmonté du nom et de la formule brute :

- **Eau $\mathrm{H_2O}$** : O au sommet, deux liaisons simples obliques vers deux H (molécule
  **coudée**, angle nettement inférieur à 180°), **deux doublets non liants** sur l'oxygène ;
- **Dioxygène $\mathrm{O_2}$** : `O = O` (double trait), **deux doublets non liants** par atome ;
- **Dioxyde de carbone $\mathrm{CO_2}$** : `O = C = O` **aligné**, deux doublets non liants sur
  chaque O, **aucun** sur le carbone ;
- **Chlorure d'hydrogène $\mathrm{HCl}$** : `H — Cl`, **trois doublets non liants** sur le chlore.

Doublets représentés par des **tirets** (pas des paires de points), traits noirs, symboles en
capitales droites. Légende en `\scriptsize` : « doublet liant = 2 électrons mis en commun ; doublet
non liant = paire restante ».

*Note de source* : le nombre de doublets non liants du chlore n'était pas lisible avec certitude sur
le scan de la p. 39 (`[VERIFY]` dans `pc-1re-cours-b.md`) ; la valeur chimiquement correcte est 3,
c'est celle à dessiner.

## 3. `pc-representations-molecule` — les quatre conventions d'écriture

*Utilisée par* : leçon `pc-matiere` (exercice `order` sur le classement des représentations).

Quatre colonnes titrées **Schéma de Lewis**, **Formule développée**, **Formule semi-développée**,
**Formule brute** (dans cet ordre, du plus complet au plus condensé, comme la leçon), toutes portant
la **même molécule**, l'**acide méthanoïque** :

- **Lewis** : squelette `H — C — O — H` en ligne, un **O au-dessus du C relié par une double liaison
  verticale**, cet O portant deux doublets non liants, l'O de droite en portant deux également ;
- **développée** : même squelette, **sans aucun doublet non liant** ;
- **semi-développée** : `HC(=O) — OH`, les liaisons C–H et O–H ne sont plus tracées ;
- **brute** : $\mathrm{CH_2O_2}$.

Une **flèche horizontale** sous les colonnes, orientée vers la droite, étiquetée « de la plus
complète à la plus condensée ».

*Note de source* : le manuel imprime la semi-développée sous une forme hybride ; l'écriture usuelle
est HCOOH. Conserver la forme du manuel, l'écart est signalé dans les notes.

## 4. `pc-triangle-feu` — le triangle du feu

*Utilisée par* : leçon `pc-energie-chimique` (exercices sur les trois composantes et les extincteurs).

Un **triangle équilatéral** pointe en haut, traits épais `solideD`, chaque **côté** portant une
étiquette écrite parallèlement au côté :

- côté gauche : **Combustible** (en `\scriptsize` : essence, gaz, bois) ;
- côté droit : **Comburant** (dioxygène $\mathrm{O_2}$ de l'air) ;
- côté du bas : **Énergie d'activation** (étincelle, flamme).

Au centre, une **flamme** stylisée. Légende sous le triangle : « les trois composantes doivent être
présentes **simultanément** ». À droite, une **variante grisée** du même triangle avec un côté
**barré d'une croix** `solideA` et la flamme en pointillés : c'est l'action d'un extincteur.

## 5. `pc-classes-extincteurs` — les cinq classes de feux

*Utilisée par* : leçon `pc-energie-chimique` (exercice `grid` d'association feu ↔ agent).

Cinq **panneaux** de structure identique, 3 en haut / 2 en bas. Chaque panneau :

- bandeau supérieur `solideA` (rouge) avec, en blanc, une silhouette d'**extincteur** (bouteille,
  poignée, lance) à gauche et une **flamme** à droite ;
- bande blanche portant **EXTINCTEUR** en `solideB` ;
- partie basse en deux colonnes : à gauche, deux cases empilées `CLASSE X` puis l'**agent
  extincteur** ; à droite, une case haute donnant le **type de feux**.

| Panneau | Agent | Type de feux | Couleur |
|---|---|---|---|
| CLASSE A | EAU PULVÉRISÉE | feux de matériaux solides (bois, papiers, tissu) | vert |
| CLASSE B | CO₂ | feux de solides ou liquides liquéfiables (essence, alcool, huile) | bleu |
| CLASSE C | POUDRE | feux de gaz (butane, propane) | rouge/rose |
| CLASSE D | POUDRE | feux de métaux (aluminium) | bleu |
| CLASSE F | MOUSSE | feux d'huile ou de graisse de cuisson | violet |

*Indication TikZ* : un seul `\newcommand` de panneau paramétré par (classe, agent, feux, couleur).
Écrire « CO₂ » avec un indice, jamais « CO2 ».

## 6. `pc-formules-developpees` — alcanes, alcènes, alcools

*Utilisée par* : leçon `pc-combustions` (exercices sur les formules brutes générales).

Trois blocs superposés, titrés, avec nom + formule brute au-dessus de chaque formule développée
(traits noirs simples, atomes en capitales) :

- **Alcanes** : **méthane** (un C central, un H en haut, un H en bas, un H à gauche, un H à droite) ;
  **propane** (chaîne H–C–C–C–H, chaque C portant un H au-dessus et un H au-dessous) ; **butane**
  (idem avec quatre C) — toutes liaisons **simples** ;
- **Alcènes** : **éthène** (deux C reliés par un **double trait horizontal**, chaque C portant deux H
  en liaisons obliques, disposition symétrique) ; **propène** (groupe C=C horizontal, le C de droite
  portant en plus une liaison simple verticale vers un C qui porte 3 H) ;
- **Alcools** : **méthanol** (chaîne H–C–O–H, le C portant un H au-dessus et un H au-dessous) ;
  **éthanol** (chaîne H–C–C–O–H, chacun des deux C portant un H au-dessus et un H au-dessous).

Souligner d'un liseré `solideD` la liaison double C=C des alcènes et le groupe $-\mathrm{OH}$ des
alcools ; le reste en noir. Sous chaque bloc, rappeler la formule générale ($\mathrm{C_nH_{2n+2}}$,
$\mathrm{C_nH_{2n}}$, $\mathrm{C_nH_{2n+1}OH}$).

*Note de source* : le manuel ne donne pas l'éthane ($n = 2$) dans la série des alcanes (méthane,
propane, butane) alors que les alcènes commencent bien à l'éthène. **Ne pas l'ajouter** : le dessin
reste fidèle au manuel, l'absence est signalée dans les notes.

## 7. `pc-tableau-avancement` — tableau d'avancement type

*Utilisée par* : leçon `pc-combustions` (exercices sur $x_{\max}$, le réactif limitant et l'état final,
et exercice guidé « camping-car »).

Tableau **dessiné** (pas un tableau Markdown), en-tête `solideB` très clair, reprenant l'exemple du
manuel :

- en-tête : l'équation répartie sur quatre colonnes — $\mathrm{CH_4}$ | $+\ 2\,\mathrm{O_2}$ |
  $\rightarrow\ \mathrm{CO_2}$ | $+\ 2\,\mathrm{H_2O}$ ;
- colonne de gauche : « État du système » et « $x$ (mol) » ; titre fusionné au-dessus des quatre
  colonnes de droite : « Quantités de matière (mol) » ;
- **initial** ($x = 0$) : 2 | 10 | 0 | 0 ; **intermédiaire** ($0 < x < x_{\max}$) : $2-x$ |
  $10-2x$ | $x$ | $2x$ ; **final** ($x_{\max} = 2$ mol) : 0 | 6 | 2 | 4.

Mettre en `solideA` les coefficients stœchiométriques repris dans les expressions (le 2 de $10-2x$ et
celui de $2x$), avec deux petites flèches courbes partant des coefficients de l'équation. Encadré à
droite : « $2 - x_{\max} = 0 \Rightarrow x_{\max} = 2$ ; $10 - 2x_{\max} = 0 \Rightarrow x_{\max} = 5$ ;
on retient la **plus petite** valeur ⇒ $\mathrm{CH_4}$ limitant ».

## 8. `pc-couple-oxydant-reducteur` — oxydant, réducteur et sens des électrons

*Utilisée par* : leçon `pc-oxydoreduction` (exercice `grid` oxydation / réduction).

Au centre, la demi-équation générale en grand : $\mathrm{ox} + n\,\mathrm{e^-} = \mathrm{red}$.

- flèche `solideB` au-dessus, de gauche à droite : « **RÉDUCTION** : l'oxydant **capte** $n$
  électrons » ;
- flèche `solideA` en dessous, de droite à gauche : « **OXYDATION** : le réducteur **cède** $n$
  électrons » ;
- pastille « ox » (bleu) à gauche, pastille « red » (rouge) à droite, mention « couple
  $\mathrm{ox}/\mathrm{red}$ » sous l'ensemble.

En bas, deux exemples avec les électrons surlignés : $\mathrm{Cu^{2+}} + 2\,\mathrm{e^-} =
\mathrm{Cu}$ (électrons **à gauche** ⇒ réduction) et $\mathrm{Zn} = \mathrm{Zn^{2+}} +
2\,\mathrm{e^-}$ (électrons **à droite** ⇒ oxydation).

## 9. `pc-pile-daniell` — schéma de principe de la pile Daniell

*Utilisée par* : leçon `pc-oxydoreduction` (exercices sur la pile, le pont salin, le sens des
électrons et la polarité).

Deux **béchers** côte à côte, reliés en haut par un **pont salin** (tube en U inversé, gris,
étiqueté « Pont salin ») :

- **gauche** : solution bleu très clair ; **lame de zinc** verticale grise, étiquetée « Lame de
  zinc » par un trait de rappel ; sur la lame, en `solideB` : **Zn** en haut, **flèche courbe
  descendante**, **Zn²⁺** en bas (l'oxydation libère des ions en solution) ;
- **droite** : solution bleue ; **lame de cuivre** verticale cuivrée, étiquetée « Lame de cuivre » ;
  sur la lame, en `solideA` : **Cu²⁺** en bas, **flèche courbe montante**, **Cu** en haut (la
  réduction dépose du cuivre) ;
- **circuit extérieur** : deux fils verticaux depuis le haut de chaque lame, reliés par un fil
  horizontal portant, de gauche à droite, une **résistance R** (rectangle) et un **ampèremètre A**
  (cercle) ;
- **électrons** : étiquettes `solideE` « 2 e⁻ » et flèches vertes indiquant le trajet **de la lame de
  zinc vers la lame de cuivre** (montée à gauche, parcours vers la droite, descente à droite) ;
- **courant** : flèche `solideA` étiquetée « $I$ » sur le fil horizontal, dirigée **de la droite vers
  la gauche** (sens conventionnel, opposé aux électrons) ;
- **bornes** : « – » près de la lame de zinc, « + » près de la lame de cuivre.

Légende : oxydation $\mathrm{Zn} = \mathrm{Zn^{2+}} + 2\,\mathrm{e^-}$ (gauche), réduction
$\mathrm{Cu^{2+}} + 2\,\mathrm{e^-} = \mathrm{Cu}$ (droite), bilan $\mathrm{Zn} + \mathrm{Cu^{2+}}
\rightarrow \mathrm{Zn^{2+}} + \mathrm{Cu}$, tension théorique **1,1 V**.

*Note de source* : sur le scan de la p. 46, le sens des deux flèches vertes « 2 e⁻ » n'est pas
lisible avec certitude, mais le texte est explicite (« les électrons libérés par cette oxydation
transitent dans le circuit extérieur pour parvenir dans l'autre compartiment ») : c'est ce sens qui
doit être dessiné. La **polarité** (– sur le zinc, + sur le cuivre) n'est **pas écrite dans le
manuel** : elle se déduit du sens des électrons.

## 10. `pc-corrosion-protection` — quatre méthodes de protection

*Utilisée par* : leçon `pc-oxydoreduction` (exercices sur la passivation et l'anode sacrificielle).

Quatre vignettes carrées alignées, titrées, autour du même objet de base (une **barre** ou une
**canalisation** grise) :

1. **Alliage** : coupe montrant un mélange homogène de deux nuances (points de deux couleurs) ;
   légende « acier inoxydable : fer + chrome + carbone » ;
2. **Revêtement** : barre entourée d'une **couche jaune** continue ; une flèche « $\mathrm{O_2}$ »
   venant de l'extérieur est **arrêtée** par la couche ; légende « peinture, placage or, laiton » ;
3. **Passivation** : barre d'aluminium portant une **fine couche gris clair** étiquetée « alumine » ;
   légende « la couche d'oxyde protège le métal et ne s'oxyde pas dans l'air humide » ;
4. **Anode sacrificielle** : canalisation horizontale enterrée avec un **bloc de zinc** fixé dessus ;
   flèche partant du zinc étiquetée $\mathrm{Zn} = \mathrm{Zn^{2+}} + 2\,\mathrm{e^-}$ ; légende « le
   zinc est oxydé **à la place** du fer ; il faut le remplacer périodiquement ».

Même échelle et même style de trait pour les quatre vignettes ; couleurs réservées au métal protégé
(gris), à la couche protectrice (jaune / gris clair) et au métal sacrifié (`solideB`).
