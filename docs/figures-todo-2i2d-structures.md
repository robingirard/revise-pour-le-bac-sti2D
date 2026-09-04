# Figures à dessiner — unité « 2I2D Tle : statique graphique, structures et matériaux »

Liste des **13 figures nouvelles** référencées par `content/units/130-2i2d-structures.yaml` et par les
cinq leçons `content/lessons/2i2d-structures-*.md`. Tant qu'elles ne sont pas créées,
`tools/validate.py` signalera « référence la figure inconnue … ».

## Conventions communes

- un fichier `figures/tikz/<id>.tex` par figure, `\documentclass[tikz,border=4pt]{standalone}` +
  `\usepackage{liaisons}` (modèle : `figures/tikz/statique-trois-forces.tex`) ;
- couleurs de `liaisons.sty` : `solideA` (rouge) pour les **efforts et forces**, `solideB` (bleu) pour les
  **pièces et barres isolées**, `solideD` (orange) pour les **cotes, bras de levier et constructions
  auxiliaires**, `solideE` (vert) pour les **appuis et le sol**, `solideF` (violet) pour les **repères,
  axes et inconnues** ;
- gabarit : largeur utile **≈ 8 cm**, hauteur ≤ 5 cm (l'appli plafonne les figures à 240 px de haut) ;
- étiquettes en `\small` (`\scriptsize` pour les cotes), notations identiques à celles des leçons
  ($\vec{F}$, $\vec{P}$, $\vec{R_A}$, $I$, $G$, $d$, $h$, $M$, $\sigma$, $\varepsilon$, $R_e$, $R_r$) ;
- sol / bâti : trait plein + hachures obliques (macro locale `\batihoriz`) ;
- **toutes les coordonnées ci-dessous sont en centimètres**, repère direct, $y$ vers le haut ;
- ⚠️ **Ne pas reproduire le symbole d'appui de la p. 272 du manuel** (triangle pointe en bas, incohérent
  avec le texte). On retient partout la convention **triangle pointe en haut**, base au sol, déjà employée
  par `statique-appuis`.

---

## Compétence `2i2d-statique-graphique`

### 1. `2i2d-trois-forces-methode` — construction du point de concours

Schéma unique (8 × 4,5 cm) montrant la **première moitié** de la méthode : trouver la direction manquante.

- Sol hachuré `solideE` de $(0,0)$ à $(8,0)$, trait horizontal en $y = 0$.
- Une barre `solideB` épaisse (0,9 pt), bouts arrondis, de $A = (1{,}2 ; 0{,}5)$ à $(5{,}6 ; 2{,}3)$.
- En $A$ : un petit **triangle d'appui pointe en haut** `solideE` (base 0,5 cm, hauteur 0,4 cm), sommet
  au contact de la barre, base posée sur le sol hachuré. Étiquette $A$ à gauche du triangle.
- Au milieu de la barre, point noir $G = (3{,}4 ; 1{,}4)$, étiquette $G$ au-dessus à gauche ; flèche
  `solideA` (1 pt) verticale descendante de $G$ à $(3{,}4 ; 0{,}3)$, étiquetée $\vec{P}$ à droite.
- À l'extrémité droite, point $B = (5{,}6 ; 2{,}3)$ ; flèche `solideA` **horizontale vers la droite**
  de $B$ à $(6{,}6 ; 2{,}3)$, étiquetée $\vec{B_{0 \rightarrow S}}$ au-dessus.
- **Constructions auxiliaires** en `solideD`, tirets fins (0,4 pt) :
  - verticale par $G$, de $(3{,}4 ; 0{,}2)$ à $(3{,}4 ; 3{,}6)$ ;
  - horizontale par $B$, de $(1{,}0 ; 2{,}3)$ à $(6{,}9 ; 2{,}3)$ ;
  - leur intersection $I = (3{,}4 ; 2{,}3)$ : petit cercle `solideD` de rayon 0,08 cm, étiquette
    « $I$ — point de concours » posée au-dessus à droite ;
  - la droite $(AI)$ prolongée en tirets `solideF` de $(0{,}6 ; 0{,}17)$ à $(4{,}5 ; 2{,}83)$.
- Sur la droite $(AI)$, une flèche `solideF` de $A$ vers $(2{,}4 ; 1{,}3)$, étiquetée $\vec{R_A}$
  (« direction trouvée »).
- Cartouche en bas à droite, encadré à coins arrondis :
  « **1.** les 3 supports sont concourants en $I$ » puis « **2.** le dynamique se ferme ».

### 2. `2i2d-dynamique-echelle` — triangle des forces et échelle

Deux vignettes côte à côte séparées par un filet vertical fin (total 8 × 4,5 cm).

- **Gauche (le dynamique)** : triangle fermé tracé en `solideA` (1,1 pt), sommets marqués par de petits
  carrés pleins de 0,08 cm. Sommets $S_1 = (0{,}4 ; 0{,}4)$, $S_2 = (0{,}4 ; 3{,}15)$,
  $S_3 = (0{,}67 ; 0{,}4)$ — *soit un triangle très aplati, image fidèle du cas « poids 55 kN, vent
  5,4 kN »*. Comme ce triangle serait illisible, **on l'exagère** : prendre
  $S_1 = (0{,}5 ; 0{,}4)$, $S_2 = (0{,}5 ; 3{,}2)$, $S_3 = (1{,}9 ; 0{,}4)$ et mentionner en légende
  « proportions exagérées pour la lisibilité ».
  - $\vec{P}$ : de $S_2$ vers $S_1$ (flèche descendante), étiquette $\vec{P}$ à gauche ;
  - $\vec{F}$ : de $S_1$ vers $S_3$ (flèche horizontale vers la droite), étiquette $\vec{F}$ dessous ;
  - $\vec{R_A}$ : de $S_3$ vers $S_2$ (flèche montante oblique), étiquette $\vec{R_A}$ à droite ;
  - sous le triangle : $\vec{P} + \vec{F} + \vec{R_A} = \vec{0}$, et le titre « dynamique **fermé** ».
- **Droite (l'échelle)** : un segment `solideD` horizontal de $(4{,}6 ; 2{,}2)$ à $(5{,}6 ; 2{,}2)$ avec
  deux petits traits verticaux aux extrémités et la cote « 1 cm » dessous ; à droite, « ↔ 10 kN ».
  Sous ce cartouche, deux lignes en `\scriptsize` :
  « lire : $F = \ell_{\text{mesurée}} \times 10$ (kN) » et « tracer : $\ell = F / 10$ (cm) ».
  Exemple chiffré en bas : « 4,3 cm ↔ 43 kN ».

### 3. `2i2d-tour-guet` — schéma de l'exercice guidé « tour de guet »

Élévation cotée (largeur 8 cm, hauteur 5 cm ; échelle verticale **comprimée**, à signaler par une
double barre de rupture `solideD` sur le fût, vers $y = 2{,}2$).

- Sol hachuré `solideE` de $(0{,}5 ; 0)$ à $(7{,}5 ; 0)$.
- Deux massifs de fondation `solideE` (rectangles pleins clairs 0,5 × 0,25 cm) : **B** centré en
  $(2{,}4 ; -0{,}15)$, **A** centré en $(5{,}2 ; -0{,}15)$ ; étiquettes $B$ et $A$ dessous.
- Fût en treillis `solideB` : deux montants obliques de $(2{,}4 ; 0)$ à $(3{,}3 ; 4{,}0)$ et de
  $(5{,}2 ; 0)$ à $(4{,}3 ; 4{,}0)$ ; entre eux, 6 **diagonales** en zigzag et 4 traverses horizontales
  (trait 0,5 pt), formant des triangles ; le pylône se rétrécit vers le haut.
- Cabine : rectangle `solideB` de $(3{,}0 ; 4{,}0)$ à $(4{,}6 ; 4{,}55)$, surmonté d'une toiture à quatre
  pans stylisée (trapèze) ; sous le plancher, un bandeau `solideF` fin (les panneaux photovoltaïques) de
  $(3{,}0 ; 3{,}85)$ à $(4{,}6 ; 4{,}0)$, annoté « 14 panneaux — 10 m² » (trait de rappel vers la droite),
  et « cabine + toiture — 4 m² » vers la cabine.
- Point **V** : petit cercle noir en $(3{,}0 ; 4{,}0)$, étiquette $V$ ; flèche `solideA` **horizontale
  vers la droite** de $(1{,}8 ; 4{,}0)$ à $(3{,}0 ; 4{,}0)$, étiquetée $\vec{F}$ (« vent »).
- Point **G** : point noir en $(3{,}8 ; 2{,}0)$ sur l'axe du pylône, étiquette $G$ ; flèche `solideA`
  verticale descendante de $G$ à $(3{,}8 ; 1{,}1)$, étiquetée $\vec{P} = 55$ kN.
- Axe vertical du pylône en trait mixte `solideF` de $(3{,}8 ; -0{,}4)$ à $(3{,}8 ; 4{,}8)$.
- Cotes `solideD` : niveau « + 40,70 » avec ligne de rappel horizontale au niveau $y = 4{,}0$ ;
  niveau « ± 0,00 » au niveau du sol ; cote horizontale **4 m** entre l'axe ($x = 3{,}8$) et $A$
  ($x = 5{,}2$), placée à $y = -0{,}75$ ; cote horizontale **8 m** entre $B$ et $A$, à $y = -1{,}15$.
- Mention en bas à droite, `\scriptsize` : « à la limite du basculement, l'action en $B$ est nulle ».

---

## Compétence `2i2d-structures-porteuses`

### 4. `2i2d-descente-charges` — le cheminement des charges

Coupe schématique d'un bâtiment à un niveau (8 × 5 cm), lue de haut en bas.

- **Charges** : une rangée de 7 flèches `solideA` verticales descendantes, identiques (longueur 0,5 cm),
  réparties de $x = 1{,}0$ à $x = 7{,}0$ au-dessus de la dalle, étiquetée à droite
  « charges : poids propre, exploitation, neige ».
- **Dalle / poutre** (porteur horizontal) : rectangle `solideB` de $(0{,}8 ; 3{,}5)$ à $(7{,}2 ; 3{,}85)$ ;
  sous elle, en trait fin `solideB!60`, la même poutre **fléchie** (arc à flèche 0,2 cm) et l'étiquette
  « porteur horizontal → **flexion** ».
- **Poteaux** (porteurs verticaux) : deux rectangles `solideB` de $(1{,}2 ; 1{,}3)$ à $(1{,}7 ; 3{,}5)$ et
  de $(6{,}3 ; 1{,}3)$ à $(6{,}8 ; 3{,}5)$ ; sur chacun, deux petites flèches `solideA` **vers l'intérieur**
  (une en haut vers le bas, une en bas vers le haut) ; étiquette « porteur vertical → **compression** ».
- **Fondations** : deux semelles `solideE` trapézoïdales de $(0{,}8 ; 0{,}9)$ à $(2{,}1 ; 1{,}3)$ et
  symétrique à droite ; étiquette « fondations ».
- **Sol** : trait plein + hachures obliques `solideE` en $y = 0{,}9$, sur toute la largeur ; sous le sol,
  deux séries de petites flèches `solideF` **vers le haut** (réaction du sol), étiquetées « réaction du sol ».
- À gauche, une **grande flèche verticale descendante** `solideD` de $(0{,}25 ; 3{,}9)$ à $(0{,}25 ; 0{,}95)$,
  étiquetée verticalement « descente de charges ».

### 5. `2i2d-appuis-reactions` — inconnues de liaison en plan

Trois vignettes alignées (chacune ≈ 2,5 × 3,5 cm), séparées par des filets verticaux fins.

Dans chaque vignette : poutre horizontale `solideB` (trait épais, longueur 1,8 cm) et sol hachuré `solideE`.

1. **Appui simple glissant** — triangle isocèle `solideE` **pointe en haut** au contact de la poutre, base
   reposant sur **deux petits cercles** (rouleaux) posés sur le sol hachuré. Une seule flèche `solideF`
   verticale vers le haut, étiquetée $R_y$. Légende : « **1 inconnue** ».
2. **Appui simple fixe (articulation)** — même triangle, **sans rouleaux**, base directement sur le sol.
   Deux flèches `solideF` : une verticale $R_y$, une horizontale $R_x$. Légende : « **2 inconnues** ».
3. **Encastrement** — mur vertical hachuré à gauche duquel part la poutre horizontale. Deux flèches
   `solideF` ($R_x$, $R_y$) **plus** une flèche circulaire `solideF` étiquetée $M$.
   Légende : « **3 inconnues** ».

Bandeau sous les trois vignettes, `\scriptsize` :
« à chaque **mobilité bloquée** correspond une inconnue — translation → force, rotation → moment ;
en plan, le PFS donne **3 équations** ».

### 6. `2i2d-poutre-deux-appuis` — poutre sur deux appuis chargée

Schéma coté unique (8 × 3,5 cm), correspondant exactement à l'exemple de la leçon.

- Poutre `solideB` horizontale épaisse de $A = (0{,}9 ; 1{,}6)$ à $B = (6{,}9 ; 1{,}6)$ (6,00 m ↔ 6 cm).
- En $A$ : **articulation** (triangle `solideE` pointe en haut, base au sol hachuré, sol en $y = 1{,}15$).
  En $B$ : **appui glissant** (même triangle + deux rouleaux). Étiquettes $A$ et $B$ sous les appuis.
- Charges `solideA`, flèches verticales descendantes arrivant sur la poutre :
  - en $x = 2{,}9$ (2,00 m de $A$), étiquette « 12 kN » ;
  - en $x = 4{,}9$ (4,00 m de $A$), étiquette « 6 kN ».
- Réactions `solideF`, flèches verticales **vers le haut** partant des appuis, étiquetées $R_A$ et $R_B$.
- Cotes `solideD` sous la figure, en $y = 0{,}45$ : « 2,00 m » de $A$ à la première charge ; « 2,00 m »
  entre les deux charges ; « 2,00 m » de la seconde charge à $B$ ; en $y = 0{,}05$, cote totale « 6,00 m ».
- Repère $(\vec{x}, \vec{y})$ `solideF` en bas à gauche.

### 7. `2i2d-poinconnement` — pilier, semelle et résistance du sol

Deux vignettes côte à côte (total 8 × 4 cm).

- **Gauche (l'ouvrage)** : silhouette très simplifiée du pont — deux piliers `solideB` verticaux
  (rectangles $0{,}3 \times 2{,}2$ cm) en $x = 1{,}0$ et $x = 3{,}4$, reliés en haut par un tablier
  horizontal `solideB` ; sous le tablier, une petite **nacelle** `solideF` (rectangle 0,4 × 0,25 cm)
  suspendue par deux traits fins, avec une double flèche horizontale `solideD` indiquant son va-et-vient.
  Étiquettes : « pilier 1 », « pilier 2 », « nacelle 2,00 MN », « rue aérienne 270 m × 15 m ».
- **Droite (le poinçonnement)** : agrandissement du pied du pilier 1. Pilier `solideB` vertical descendant
  sur une **semelle** carrée `solideE` (rectangle de 1,8 cm de large, 0,35 cm de haut) posée sur un sol
  hachuré. Une grosse flèche `solideA` verticale descendante au-dessus du pilier, étiquetée
  $F = 35{,}07$ MN. Sous la semelle, un **champ de 7 petites flèches** `solideF` vers le haut,
  régulièrement réparties, étiquetées « pression $p$ répartie ». Cote `solideD` de la largeur de semelle :
  « 15 m ». Cartouche : $p = \dfrac{F}{S} \leq p_{\text{sol}}$, avec « $S = 15 \times 15 = 225$ m² » et
  « $p_{\text{sol}} = 0{,}20$ MPa ».

---

## Compétence `2i2d-treillis-stabilite`

### 8. `2i2d-treillis-ferme` — ferme en treillis, barres tendues et comprimées

Élévation d'une ferme triangulée à membrures parallèles (8 × 3,5 cm).

- **Membrure supérieure** `solideB` : segment de $(0{,}6 ; 2{,}4)$ à $(7{,}4 ; 2{,}4)$.
- **Membrure inférieure** `solideB` : segment de $(0{,}6 ; 1{,}0)$ à $(7{,}4 ; 1{,}0)$.
- **Montants** verticaux `solideB` aux abscisses $x = 0{,}6 ; 2{,}3 ; 4{,}0 ; 5{,}7 ; 7{,}4$.
- **Diagonales** `solideB` en zigzag : $(0{,}6 ; 1{,}0)$–$(2{,}3 ; 2{,}4)$, $(2{,}3 ; 1{,}0)$–$(4{,}0 ; 2{,}4)$,
  $(5{,}7 ; 2{,}4)$–$(4{,}0 ; 1{,}0)$, $(7{,}4 ; 2{,}4)$–$(5{,}7 ; 1{,}0)$ (symétrie centrale).
- **Nœuds** : petits disques noirs de 0,07 cm à toutes les intersections.
- **Charges** : trois flèches `solideA` verticales descendantes sur les nœuds supérieurs $x = 2{,}3 ; 4{,}0 ; 5{,}7$.
- **Appuis** : en $(0{,}6 ; 1{,}0)$ un triangle `solideE` pointe en haut (articulation) ; en $(7{,}4 ; 1{,}0)$
  le même triangle **sur deux rouleaux** ; sol hachuré sous les deux.
- **Code couleur des efforts** : membrure inférieure et diagonales montantes surlignées en `solideA` fin
  avec l'étiquette « **tendue** » ; membrure supérieure et montants surlignés en `solideB!70` épais avec
  l'étiquette « **comprimée** ». Petite légende à droite : deux traits témoins + les deux mots.
- Encart en bas à gauche (2 × 1 cm) : un **triangle** de barres articulées coché « indéformable » et un
  **quadrilatère** articulé penché en losange, coché « déformable ».

### 9. `2i2d-basculement` — moment renversant et moment stabilisateur

Schéma unique (8 × 5 cm).

- Sol hachuré `solideE` de $(0{,}6 ; 0)$ à $(7{,}4 ; 0)$.
- Structure schématisée par un rectangle élancé `solideB` (largeur 1,6 cm, hauteur 3,8 cm), de
  $(2{,}6 ; 0)$ à $(4{,}2 ; 3{,}8)$.
- **Arête de basculement** $A = (4{,}2 ; 0)$ : gros point noir, étiquette $A$ ; à gauche, l'appui
  $B = (2{,}6 ; 0)$, marqué d'un petit triangle `solideE` **barré d'une croix** et de la mention
  « action nulle ».
- **Poids** : point $G = (3{,}4 ; 1{,}9)$ (point noir, étiquette $G$), flèche `solideA` verticale
  descendante de $G$ à $(3{,}4 ; 0{,}5)$, étiquetée $\vec{P}$.
- **Vent** : flèche `solideA` horizontale vers la droite, de $(1{,}5 ; 3{,}6)$ à $(2{,}6 ; 3{,}6)$,
  étiquetée $\vec{F}$.
- **Bras de levier** en `solideD` :
  - cote horizontale $d_P$ de $x = 3{,}4$ à $x = 4{,}2$, placée en $y = -0{,}45$, avec l'angle droit marqué ;
  - cote verticale $h$ de $y = 0$ à $y = 3{,}6$, placée en $x = 4{,}9$, trait de rappel horizontal
    pointillé du point d'application du vent jusqu'à $x = 4{,}9$.
- **Flèche de rotation** : arc `solideD` en pointillés autour de $A$, sens horaire, ouvert de 60°,
  rayon 1,1 cm, avec une pointe de flèche — le mouvement de basculement.
- Cartouche en bas à droite, encadré :
  $M_{\text{stab}} = P \times d_P$ / $M_{\text{renv}} = F \times h$ / « stable si $M_{\text{stab}} > M_{\text{renv}}$ ».

### 10. `2i2d-palais-sports-treillis` — schéma de l'exercice guidé « palais des sports »

Élévation cotée (8 × 4 cm).

- Deux **poteaux en béton** `solideE` (rectangles hachurés 0,45 × 1,2 cm) en $x = 0{,}9$ et $x = 7{,}1$,
  posés sur un sol hachuré en $y = 0$ ; étiquettes « poteau 1 », « poteau 2 ».
- **Ferme en treillis** `solideB` entre les deux têtes de poteaux ($y = 1{,}2$) : membrure inférieure
  droite de $(0{,}9 ; 1{,}2)$ à $(7{,}1 ; 1{,}2)$ ; membrure supérieure **légèrement dissymétrique**, de
  $(0{,}9 ; 1{,}75)$ montant jusqu'à $(4{,}6 ; 2{,}55)$ puis redescendant à $(7{,}1 ; 2{,}05)$ — pente
  faible, cohérente avec l'exigence « ≤ 5° » ; montants verticaux tous les 0,9 cm et diagonales en zigzag.
- **Couverture** : trait `solideF` parallèle à la membrure supérieure, décalé de 0,15 cm au-dessus,
  étiqueté « couverture + panneaux photovoltaïques ».
- **Barre 1** : la barre de membrure supérieure située juste à droite du sommet, surlignée en `solideA`
  (1,3 pt) avec deux flèches axiales `solideA` **vers l'extérieur** (traction) et l'étiquette
  « barre 1 — $N = 1\,750$ kN ».
- **Appuis** : sur le poteau 1, triangle `solideE` **sur deux rouleaux** (« appui glissant, type A ») ;
  sur le poteau 2, triangle `solideE` **sans rouleaux** (« appui fixe, type B »).
- **Vent** : deux flèches `solideD` horizontales, l'une vers la droite à gauche de la figure
  (« vent d'ouest »), l'autre vers la gauche à droite (« vent d'est »).
- **Dilatation** : double flèche horizontale `solideD` en pointillés placée sous la membrure inférieure,
  au centre, étiquetée « dilatation ≈ 27 mm ».
- Cote `solideD` de portée sous la figure, en $y = -0{,}55$ : « 56 m ».

---

## Compétence `2i2d-materiaux-choix`

### 11. `2i2d-familles-contrainte-deformation` — ductile, fragile, élastomère

Un seul repère orthonormé (8 × 4,5 cm), quatre courbes superposées. **Aucune valeur chiffrée sur les
axes** : la figure est qualitative.

- Axe des ordonnées : « Contrainte $\sigma = F/S$ » ; axe des abscisses : « Déformation $\varepsilon = \Delta L / L$ ».
  Origine notée $0$. Axes en `solideF`, flèches aux extrémités.
- **Courbe A — céramique / verre (fragile)** : segment de droite très raide depuis $0$, jusqu'à un point
  haut et proche de l'axe des ordonnées, terminé par une **croix** `solideA` et l'étiquette
  « rupture **sans** déformation plastique ». Tracé `solideA`.
- **Courbe B — acier doux (ductile)** : segment de droite de pente moyenne jusqu'à un premier maximum
  noté $R_e$ (pointillé horizontal vers l'axe), petit **décrochement**, puis remontée concave jusqu'à un
  maximum noté $R_r$ (pointillé horizontal), puis décroissance jusqu'à une croix « Rupture ». Tracé
  `solideB`, le plus épais. Un petit triangle de pente sur la partie linéaire, étiqueté $E$.
- **Courbe C — alliage d'aluminium** : même allure que B, mais **pente plus faible** et maximum plus bas.
  Tracé `solideE`.
- **Courbe D — élastomère (caoutchouc)** : courbe très plate au départ puis relevée en fin de parcours,
  s'étendant beaucoup plus loin en abscisse que les trois autres. Tracé `solideD`.
- **Légende** à droite (4 lignes, traits témoins de 0,5 cm) : « céramique (fragile) », « acier doux
  (ductile) », « alliage d'aluminium », « élastomère ».
- Sous l'axe des abscisses, deux doubles flèches `solideD` sous la courbe B : « zone élastique » (courte)
  et « zone plastique » (longue).
- Cartouche `\scriptsize` en bas : « la **pente** donne la rigidité $E$ ; la **longueur** de la partie
  plastique donne la ductilité ».

### 12. `2i2d-radar-performance` — diagramme des indices de performance

Diagramme en toile d'araignée (8 × 5 cm).

- **6 axes** partant du centre, réparts tous les 60°, et **5 hexagones concentriques** (rayons 0,4 / 0,8 /
  1,2 / 1,6 / 2,0 cm), tracés fins en gris.
- Étiquettes des axes, en partant du haut et **dans le sens horaire** : « Résistance à la corrosion »
  (haut), « Coulabilité » (droite-haut), « Empreinte carbone » (droite-bas), « Recyclabilité » (bas),
  « Masse » (gauche-bas), « Limite élastique » (gauche-haut).
- Graduation **0 au centre → 5 à l'extérieur** : les chiffres 0 à 5 écrits en `\scriptsize` le long de
  l'axe « Recyclabilité » (celui du bas).
- **Deux polygones de comparaison** (contrairement au manuel, dont le diagramme est vierge — le préciser
  en légende) :
  - matériau 1 en `solideA`, trait plein, remplissage 10 % — notes, dans l'ordre des axes cité :
    3, 4, 2, 3, 1, 5 ;
  - matériau 2 en `solideB`, trait tireté, remplissage 8 % — notes : 4, 2, 4, 5, 4, 3.
  - petits points aux sommets ; légende à droite : « matériau 1 », « matériau 2 ».
- Bandeau sous le diagramme : « 0 Mauvais · 1 Faible · 2 Médiocre · 3 Acceptable · 4 Bon · 5 Excellent ».

### 13. `2i2d-cycle-vie-materiau` — cycle de vie et valorisation

Boucle fermée à 5 stations (8 × 5 cm).

- Cinq cartouches à coins arrondis `solideB` (1,5 × 0,6 cm) disposés en **cercle** (rayon 1,8 cm, centre
  $(4{,}0 ; 2{,}5)$), reliés par des **flèches courbes** `solideD` dans le sens horaire, dans cet ordre en
  partant du haut : « Extraction », « Transport », « Fabrication », « Utilisation », « Fin de vie ».
- Sous chaque cartouche, en `\scriptsize` et en gris, l'impact correspondant : « déforestation, carrières,
  plateformes pétrolières » / « gaz à effet de serre » / « gaz à effet de serre » / « gaz à effet de
  serre » / « pollution de l'eau et de l'air, déchets ».
- Depuis le cartouche « Fin de vie », **trois flèches** `solideE` divergentes vers la droite, chacune
  aboutissant à une petite étiquette encadrée `solideE` :
  « **Réutilisation** → l'objet resert », « **Recyclage** → la matière resert »,
  « **Valorisation énergétique** → la chaleur de combustion est récupérée ».
- Les deux premières étiquettes sont reliées par une **flèche de retour** en tirets `solideE` vers le
  cartouche « Fabrication » (pour la réutilisation) et vers « Extraction » (pour le recyclage), afin de
  matérialiser la boucle.

---

## Figures existantes réutilisées

Aucune n'est à redessiner ; elles sont référencées telles quelles par l'unité et les leçons.

| Figure | Où elle sert |
|---|---|
| `statique-deux-forces` | solide soumis à 2 forces, traction/compression (leçon et items niveau 1) |
| `statique-appuis` | les trois modélisations d'appui au sol (compétence structures porteuses) |
| `pc-familles-materiaux` | les quatre familles de matériaux (compétence familles de matériaux) |

Autres figures mobilisables si l'unité s'étoffe : `statique-trois-forces` (point de concours et dynamique,
version 1re), `rdm-sollicitations` (traction, compression, flexion, cisaillement, torsion),
`rdm-essai-traction` (courbe contrainte-déformation de l'acier), `rdm-contrainte` ($\sigma = F/S$),
`statique-moment-force` (bras de levier, utile pour le basculement).
