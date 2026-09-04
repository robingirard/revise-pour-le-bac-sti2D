# Figures à dessiner — exercices guidés de mécanique (1re)

Cette liste recense les **7 figures** référencées par les 8 nouveaux exercices guidés (`type: guided`)
ajoutés dans `content/units.yaml` (unités *liaisons*, *schéma cinématique*, *transmission-mvt*,
*cinématique*) et dans `content/units/10-statique-rdm.yaml` (compétences `statique-actions`,
`statique-pfs`, `rdm-sollicitations`).
Tant qu'elles ne sont pas créées, `tools/validate.py` signalera « référence la figure inconnue … ».

Les systèmes sont ceux des exercices d'ingénierie de 1re (notes `docs/notes/exercices-1re-a.md` et
`docs/notes/exercices-1re-c.md`) : machine de nettoyage de lunettes, diffuseur de parfum,
distributeur de savon, suspension de moto électrique, trottinette électrique, fondations d'un
bâtiment. **Aucune de ces figures n'est la reproduction d'un dessin du livre** : ce sont des schémas
de principe reconstruits, cotés avec les seules données reprises dans les énoncés.

## Conventions communes

- un fichier `figures/tikz/<id>.tex` par figure, `\documentclass[tikz,border=4pt]{standalone}` +
  `\usepackage{liaisons}` (modèle : `figures/tikz/transmission-poulies.tex`) ;
- couleurs de `liaisons.sty` : `solideA` (rouge) = pièce motrice / effort ; `solideB` (bleu) = pièce
  menée ou pièce isolée ; `solideD` (orange) = cotes, courroies, bras de levier ; `solideE` (vert) =
  bâti, sol, appuis ; `solideF` (violet) = repères et axes ;
- gabarit : largeur utile ≈ 8 cm, hauteur ≤ 5 cm (l'appli plafonne les figures à 240 px de haut) ;
- étiquettes en `\small`, repères de pièces en `\small\bfseries` et de la couleur de la pièce ;
- bâti / sol : trait plein + hachures obliques (macro locale `\batihoriz`, cf. `transmission-poulies.tex`) ;
- symboles normalisés de liaison : `\pic … {pivot bout}`, `{pivot face}`, `{glissiere face}`,
  `{ponctuelle face}` de `liaisons.sty` (mêmes styles que `mecanisme-*-schema.tex`) ;
- les coordonnées ci-dessous sont en cm, `x=1cm, y=1cm`, et donnent une mise en page directement
  utilisable ; elles peuvent être ajustées tant que la boîte reste ≈ 8 cm de large.

---

## 1. `guide-diffuseur-schema` — schéma cinématique du diffuseur de parfum

*Exercice guidé « Diffuseur de parfum : lire les liaisons et les efforts transmissibles »
(unité `liaisons`, compétence `efforts`).*

Schéma cinématique plan, engrenages représentés par leurs **cercles primitifs**.
Boîte : `\useasboundingbox (-0.6,-3.2) rectangle (8.0,2.2);`

- **Pignon moteur 1** (`solideA`) : cercle de rayon 0,45 cm centré en **A** = (6,8 ; 1,2), repère
  « **1** Z1 = 10 » au-dessus.
- **Pignon double 2** (`solideB`) : deux cercles concentriques centrés en **B** = (4,9 ; 0,2), rayons
  2,05 cm (Z2 = 46) et 0,45 cm (Z2′ = 10) ; le grand cercle est **tangent** au cercle du pignon 1.
- **Pignon double 3** (`solideB!70!black`) : deux cercles concentriques centrés en **C** = (2,2 ; 0,2),
  rayons 2,25 cm (Z3 = 50) et 0,55 cm (Z3′ = 12) ; le grand cercle est tangent au petit cercle de 2.
- **Came 4** (`solideA`) : cercle de rayon 0,55 cm centré en **D** = (1,0 ; −1,6), tangent au petit
  cercle de 3 ; un **bossage** excentré (petit arc épais) sur sa périphérie, tourné vers le haut.
- **Tête d'aérosol 5** (`solideD`) : rectangle vertical 0,5 × 1,3 cm dont le bas touche la came en
  **E** = (1,0 ; −1,0) ; au-dessus, la buse. Point **E** marqué par un petit disque noir.
- Liaisons au **bâti 0** (`solideE`) : un `\pic{pivot bout}` en A, B, C et D, chacun relié par un
  arbre fin vertical à une ligne de bâti hachurée en y = −3,0 (macro `\batihoriz`) ; un
  `\pic{glissiere face}` vertical à droite de la tête 5, en **F** = (1,6 ; 0,0), relié au bâti.
- Étiquettes (`\small`) : « bâti **0** » sous les hachures ; « pignon moteur **1** — Z1 = 10 » ;
  « pignon double **2** — Z2 = 46 / Z2′ = 10 » ; « pignon double **3** — Z3 = 50 / Z3′ = 12 » ;
  « came **4** » ; « tête d'aérosol **5** » ; « **E** contact ponctuel ».
- Petit trièdre (`solideF`) en bas à droite : $\vec{x}$ vers la droite, $\vec{y}$ vers le haut,
  $\vec{z}$ figuré par un cercle pointé (sortant de la feuille).
- Une flèche `solideA` verticale descendante à côté de la tête 5, étiquetée « translation suivant
  $\vec{y}$ », pour rappeler que la rotation de la came pousse la tête.

---

## 2. `guide-moto-suspension` — suspension arrière d'une moto électrique

*Utilisée par deux exercices guidés : « Suspension arrière d'une moto électrique : classes et graphe
des liaisons » (unité `schéma cinématique`, compétence `classes`) et « Le combiné
ressort-amortisseur d'une moto électrique » (compétence `statique-actions`).*

Vue de profil, filaire, moto tournée vers la droite.
Boîte : `\useasboundingbox (-0.4,-1.0) rectangle (8.0,4.2);`

- **Châssis 1** (`solideE`) : contour simplifié en trait épais, un trapèze allant de (2,2 ; 1,6) à
  (5,4 ; 3,6), hachuré légèrement en haut à droite pour marquer la référence.
- **Bras oscillant 2** (`solideB`) : barre épaisse de **D** = (2,6 ; 1,5) à **A** = (6,6 ; 1,1),
  avec un **triangle** (D, B, A) tracé en trait plus fin pour figurer la structure triangulée ;
  **B** = (4,4 ; 1,9).
- **Roue arrière** : cercle fin (rayon 0,9 cm) centré en A, en gris (`black!40`).
- **Combiné ressort-amortisseur** : segment de **B** = (4,4 ; 1,9) à **C** = (5,6 ; 4,0),
  donc incliné de **60°** environ sur l'horizontale.
  - **corps 4** (`solideA`) : rectangle allongé (largeur 0,34 cm) occupant les deux tiers supérieurs
    du segment, côté C ;
  - **tige 3** (`solideD`) : trait épais occupant le tiers inférieur, côté B, entrant dans le corps ;
  - le ressort **n'est pas** représenté (mention « ressort non représenté » en `\small`, italique).
- Symboles de liaison : `\pic{pivot bout}` en **D** (bras 2 / châssis 1), en **B** (tige 3 / bras 2)
  et en **C** (corps 4 / châssis 1) ; petite **glissière** figurée par deux traits parallèles au
  segment BC là où la tige entre dans le corps (liaison 3-4).
- **Arc de cercle** fin en tirets, centré en D, passant par A, avec une double flèche : trajectoire
  du point A dans le mouvement 2/1.
- Cotes et annotations (`solideD`) : cote de l'entraxe **BC = 310 mm** le long du segment ; arc
  d'angle marqué **60°** entre BC et une horizontale pointillée passant par B.
- Deux flèches `solideA` **opposées**, portées par (BC) et dirigées **vers l'extérieur** du combiné
  (l'une appliquée en C vers le haut à droite, l'autre en B vers le bas à gauche), étiquetées
  $\vec{F}_{\text{ressort} \rightarrow 4}$ et $\vec{F}_{\text{ressort} \rightarrow 3}$ : ce sont les
  actions du ressort **comprimé**.
- Repères de pièces : « **1** châssis », « **2** bras oscillant », « **3** tige », « **4** corps »,
  et les points A, B, C, D en gras.
- Trièdre (`solideF`) en bas à gauche : $\vec{x}$ vers la droite, $\vec{y}$ vers le haut.

---

## 3. `guide-boboptic-schema` — schéma cinématique du système à rouleau

*Exercice guidé « Machine à nettoyer les lunettes (1) : la rotation du rouleau »
(unité `transmission-mvt`, compétence `transmission`).*

Schéma cinématique plan, engrenages en cercles primitifs, renvoi d'angle en tronc de cône.
Boîte : `\useasboundingbox (-0.6,-3.4) rectangle (8.0,2.4);`

- **Chariot 1** (`solideB`) : barre horizontale épaisse de (0,4 ; 1,6) à (7,4 ; 1,6), repère
  « **1** chariot » à droite. Deux arbres verticaux descendent du chariot, en (5,8 ; 1,6) et
  (3,6 ; 1,6), chacun terminé par un `\pic{pivot bout}` (liaisons pivot avec le chariot).
- **Arbre moteur** : à droite, en (5,8 ; 1,6) → (5,8 ; 0,4) ; **pignon moteur 3** (`solideA`),
  cercle de rayon 0,4 cm centré en (5,8 ; 0,4), étiqueté « **3** Z3 = 12 ».
- **Roue réceptrice 4** (`solideB`) : cercle de rayon 2,4 cm centré en **(3,6 ; 0,4)**, tangent au
  pignon 3 (entraxe 2,8 cm = 0,4 + 2,4), étiqueté « **4** Z4 = 72 ».
- **Pignon 5** (`solideB`) : cercle de rayon 0,8 cm **concentrique** à la roue 4 (même arbre), tracé
  en trait plus fin, étiqueté « **5** Z5 = 25 — R = 10 mm ».
- **Crémaillère 6** (`solideE`) : bande dentée horizontale de (1,0 ; −0,5) à (6,6 ; −0,5), tangente
  par le bas au pignon 5, fixée au **bâti 10** (hachures sous la bande), étiquetée
  « **6** crémaillère (fixe) — **10** bâti ».
- **Renvoi d'angle** : à gauche, sur l'arbre horizontal issu de la roue 4 (trait de (1,2 ; 0,4) à
  (3,6 ; 0,4)), un **pignon conique 7** (`solideA`) dessiné en tronc de cône pointe à droite, centré
  en (1,2 ; 0,4), en prise avec la **roue conique 8** (`solideB`) d'axe **vertical**, tronc de cône
  pointe en haut, centré en (1,2 ; −0,4). Étiquettes « **7** Z7 = 20 » et « **8** Z8 = 20 ».
- **Rouleau 9** (`solideA`) : rectangle vertical 0,7 × 1,2 cm sous la roue 8, de (0,85 ; −2,0) à
  (1,55 ; −0,8), étiqueté « **9** rouleau — Ø 30 mm ».
- **Verre de lunettes** : trait horizontal épais gris de (0,2 ; −2,2) à (2,4 ; −2,2), sous le
  rouleau, étiqueté « verre ».
- Flèche `solideD` horizontale sous le chariot, étiquetée « $\vec{V}$ chariot / bâti » (sens gauche
  → droite), et flèche circulaire `solideA` autour du rouleau, étiquetée $\omega_9$.
- Trièdre (`solideF`) en bas à droite ($\vec{x}$ droite, $\vec{y}$ haut).

---

## 4. `guide-boboptic-vitesse` — courbe de vitesse du chariot (profil trapézoïdal)

*Exercice guidé « Machine à nettoyer les lunettes (2) : la translation du chariot »
(unité `cinématique`, compétence `vitesses`).*

Repère orthogonal simple, allure trapézoïdale, dans le style de `cinematique-chronogrammes.tex`.
Boîte : `\useasboundingbox (-1.2,-1.0) rectangle (8.2,3.4);`

- Axes (`solideF`) : abscisse $t$ (s) de 0 à 1,75 s (1 s ↔ 4 cm), graduée tous les 0,25 s, avec les
  valeurs **0,25 ; 0,50 ; 1,25 ; 1,50** annotées ; ordonnée $V$ (m/s) de 0 à 0,15 (0,05 m/s ↔ 1 cm),
  avec la seule valeur **0,125** cotée et un pointillé horizontal à ce niveau.
- Courbe (`solideB`, trait 1,4 pt) : (0 ; 0) — (0,25 ; 0) — montée linéaire jusqu'à
  (0,50 ; 0,125) — palier jusqu'à (1,25 ; 0,125) — descente linéaire jusqu'à (1,50 ; 0) —
  (1,75 ; 0).
- Trois zones séparées par des traits verticaux fins en pointillés en t = 0,50 s et t = 1,25 s,
  numérotées sous l'axe : **1** (accélération), **2** (vitesse constante), **3** (freinage).
- L'aire sous la courbe est **remplie** en `solideD!15`, avec l'étiquette centrée
  « aire = course = 0,125 m » (`solideD`) et une flèche fine vers le trapèze.
- En zone 1, un petit triangle de pente (`solideA`) avec l'étiquette
  « $a = 0{,}125 / 0{,}25 = 0{,}5$ m/s² ».
- Sous la figure, en `\small` : « courbe mesurée modélisée par un trapèze ».

---

## 5. `guide-savon-cinematique` — chaîne cinématique du distributeur de savon

*Exercice guidé « Distributeur de savon sans contact : réduction, cadence et rendement »
(unité `transmission-mvt`, compétence `couple`).*

Schéma de principe, de gauche à droite, dans un cadre.
Boîte : `\useasboundingbox (-0.5,-2.6) rectangle (8.0,2.2);`

- **Moteur** (`solideA`) : rectangle 1,1 × 0,8 cm centré en (0,6 ; 0,9), étiqueté
  « moteur — N = 3 517 tr/min » (deux lignes, `\small`).
- **Vis sans fin 1** (`solideA`) : cylindre horizontal 1,4 × 0,5 cm de (1,3 ; 0,65) à (2,7 ; 1,15),
  hachuré en hélice (3 ou 4 traits obliques), étiqueté « **1** vis sans fin — Z1 = 1 filet ».
- **Roue 2** (`solideB`) : cercle de rayon 1,3 cm centré en **(3,4 ; −0,3)**, tangent par le haut à
  la vis, étiqueté « **2** roue — Z21 = 32 » ; dents figurées par une couronne de petits traits.
- **Pignon 2′** (`solideB`) : cercle **concentrique** de rayon 0,35 cm, tracé en trait fin (même
  arbre que la roue 2), étiqueté « Z22 = 8 ».
- **Roue excentrique 3** (`solideB!70!black`) : cercle de rayon 1,9 cm centré en **(5,65 ; −0,3)**,
  tangent au pignon 2′, étiqueté « **3** roue excentrique — Z3 = 48 » ; un **maneton** (petit disque
  noir) sur un rayon, à 1,0 cm du centre, marqué « excentricité ».
- **Piston 4** (`solideD`) : rectangle horizontal 1,4 × 0,45 cm à droite, de (6,3 ; 1,0) à
  (7,7 ; 1,45), guidé par un `\pic{glissiere face}` horizontal ; relié au maneton par une **bielle**
  fine (trait) ; étiqueté « **4** piston ».
- Double flèche `solideD` sous le piston : « aller-retour = 1 dose », et flèche `solideA` sortante à
  droite étiquetée « savon ».
- Liaisons au bâti : `\pic{pivot bout}` sur les axes de la vis 1, de la roue 2 et de la roue 3,
  chacun relié à une ligne de bâti hachurée en y = −2,4.
- Trièdre (`solideF`) en bas à droite.

---

## 6. `guide-trottinette-pente` — trottinette en montée sur une pente de 14 %

*Exercice guidé « La trottinette électrique peut-elle gravir une pente de 14 % ? »
(compétence `statique-pfs`).*

Schéma d'étude en montée, silhouette stylisée, dans l'esprit de `pc-bilan-forces-plan-incline.tex`.
Boîte : `\useasboundingbox (-0.6,-1.6) rectangle (8.0,4.4);`

- **Pente** (`solideE`) : droite passant par (0,4 ; 0) et (7,4 ; 0,98) — soit exactement 14 % —
  hachurée en dessous ; horizontale pointillée depuis (0,4 ; 0) vers la droite ; arc d'angle marqué
  **$\alpha$** entre les deux, avec « pente 14 % ».
- **Triangle de pente** (`solideD`, trait fin) sous la trottinette : base horizontale cotée
  « 100 m » et côté vertical coté « 14 m ».
- **Trottinette** (`solideB`) : plateau incliné parallèle à la pente de (2,6 ; 0,54) à
  (4,6 ; 0,82), deux roues (cercles de rayon 0,3 cm) aux points de contact **B** = (2,7 ; 0,32)
  (roue arrière, à gauche) et **A** = (4,5 ; 0,57) (roue avant motrice, à droite), colonne de
  direction montant de A vers un guidon en (5,1 ; 2,0).
- **Silhouette de l'usager** (gris, `black!45`), debout sur le plateau ; point **G** (petit disque
  noir) à hauteur (3,6 ; 2,3), étiqueté « $G$ ».
- Vecteurs (`solideA`, épais) :
  - $\vec{P}$ en G, **vertical descendant**, longueur 1,6 cm ;
  - ses deux projections en pointillés : $-mg\sin\alpha \,\vec{u}$ (parallèle à la pente, vers le
    bas de la pente) et $-mg\cos\alpha \,\vec{v}$ (perpendiculaire à la pente) ;
  - $\vec{F}_{\text{tract}}$ en A, parallèle à la pente **vers le haut** ;
  - $\vec{R}_{\text{av}}$ en A et $\vec{R}_{\text{ar}}$ en B, perpendiculaires à la pente, vers le haut.
- **Repère local** (`solideF`) près du guidon : $\vec{u}$ parallèle à la pente vers l'avant,
  $\vec{v}$ perpendiculaire, avec le vecteur vitesse $\vec{V}_{G,t/\text{sol}}$ (`solideD`) parallèle
  à $\vec{u}$ et l'annotation « vitesse constante ».
- Cotes : « Ø 216 mm » avec ligne de rappel vers la roue avant.

---

## 7. `guide-fondations-zone` — zone d'influence de la dalle sur un ensemble poteaux-poutre

*Exercice guidé « Descente de charges : de la toiture-parking aux fondations »
(compétence `rdm-sollicitations`).*

Perspective cavalière simple (fuyante à 30°, coefficient 0,5), très épurée.
Boîte : `\useasboundingbox (-0.8,-1.2) rectangle (8.2,4.6);`

- **Dalle** (`solideB!25`, contour `solideB`) : dalle plate en perspective, face avant de
  (0,6 ; 3,0) à (6,6 ; 3,0), épaisseur **0,40 m** cotée à gauche (cote `solideD` verticale entre
  y = 3,0 et y = 3,4) ; annotation fléchée « zone d'influence : **348 m²** » posée sur le dessus.
- **Poutre** (`solideB`) : barre horizontale épaisse sous la dalle, de (0,8 ; 2,75) à (6,4 ; 2,75).
- **Trois poteaux** (`solideB`) : rectangles verticaux de 0,35 cm de large, aux abscisses 1,2 / 3,6 /
  6,0, descendant de y = 2,75 à y = 0,3 ; hauteur cotée **4,75 m** (cote `solideD` à droite).
- **Semelles de fondation** (`solideE`) : trois blocs plats 1,0 × 0,3 cm sous chaque poteau, posés
  sur une ligne de sol hachurée en y = 0 ; la semelle centrale est cotée **0,80 m** en largeur.
- **Charges** (`solideA`) : une rangée de 6 à 8 petites flèches verticales descendantes réparties sur
  le dessus de la dalle, avec l'étiquette « $q_{ne} = 2{,}95$ kN/m² (exploitation + neige) » ; sous
  chaque semelle, une flèche montante étiquetée « réaction du sol ».
- Annotations de sollicitation (`\small`) : « poutre : **flexion** » avec une flèche vers la poutre,
  dessinée légèrement **fléchie** en trait fin pointillé ; « poteaux : **compression** » avec deux
  petites flèches opposées le long d'un poteau.
- Une silhouette de voiture stylisée (gris clair) posée sur la dalle rappelle l'usage en parking.

---

## Figures existantes réutilisées par ces exercices

| Figure | Exercice guidé |
|---|---|
| `transmission-roue-vis` | déjà utilisée par « Motorisation d'un portail coulissant (1) » |
| `cinematique-chronogrammes` | déjà utilisée par « Motorisation d'un portail coulissant (2) » |
| `rdm-passerelle` | déjà utilisée par « Passerelle piétonne sur tirant acier » |

Aucune autre figure existante n'a été réutilisée : les sept schémas ci-dessus concernent des
systèmes nouveaux. En attendant leur création, les exercices restent jouables — l'appli affiche
simplement un espace vide à la place de la figure — mais l'énoncé de chaque exercice a été rédigé
pour être **compréhensible sans la figure** (toutes les données géométriques utiles sont dans
l'`intro`).
