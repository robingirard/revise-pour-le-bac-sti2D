# Figures à dessiner — unité « Physique : ondes et lumière »

Dix figures TikZ sont référencées par l'unité `pc-ondes` (`content/units/70-pc-ondes.yaml` et
`content/lessons/pc-ondes-bases.md`, `pc-son.md`, `pc-ondes-em.md`, `pc-lumiere-energie.md`). Tant
qu'elles n'existent pas dans `figures/tikz/`, `make content` échoue avec « figure inconnue » : ces dix
fichiers sont donc un **prérequis de build**.

## Conventions communes

- un fichier par figure : `figures/tikz/<ID>.tex`, `\documentclass[tikz,border=4pt]{standalone}` +
  `\usepackage{liaisons}` (comme `figures/tikz/cinematique-chronogrammes.tex`) ;
- couleurs de la bibliothèque : `solideA` (rouge), `solideB` (bleu), `solideC` (rose),
  `solideD` (orange), `solideE` (vert), `solideF` (violet) ;
- **code couleur de l'unité** : onde incidente / émission = `solideA` ; onde réfléchie = `solideB` ;
  onde transmise = `solideE` ; grandeurs mesurées et cotes = `solideD` ;
- textes en `\small` / `\scriptsize`, en **français**, avec les notations du livre
  ($\lambda$, $T$, $f$ ou $\nu$, $v$, $c$, $I$, $I_0$, $L$, $\Delta t$, $d$, $E$, $h$, $P_{\text{surf}}$) ;
- **écriture française des nombres** : virgule décimale, espace fine comme séparateur de milliers
  (340 ; 1 500 ; 3,0 × 10⁸) ;
- largeur cible ≈ 8 cm (affichage mobile), hauteur ≤ 6 cm ;
- les longueurs d'onde du visible sont **toujours** données en nanomètres entre 400 et 800 nm.

---

## 1. `pc-onde-periode-longueur` — la double périodicité

*Utilisée par* : leçon `pc-ondes-bases` ; 1 exercice (niveau 1, relation $\lambda = vT = v/f$).

**Deux repères superposés**, de même largeur, l'un au-dessus de l'autre, avec la **même sinusoïde**
tracée en `solideA` (2 périodes et demie, amplitude identique dans les deux).

- **Repère du haut** — « **photographie à un instant $t$ fixé** » : axe horizontal étiqueté
  $x$ (m), axe vertical « perturbation ». Une **double flèche `solideD` horizontale** entre deux
  crêtes consécutives, annotée $\lambda$ ; sous l'axe, en `\scriptsize` : « périodicité **spatiale** ».
- **Repère du bas** — « **enregistrement en un point $x$ fixé** » : axe horizontal étiqueté $t$ (s).
  Une **double flèche `solideD` horizontale** entre deux maximums consécutifs, annotée $T$ ; sous
  l'axe : « périodicité **temporelle** ».

Bien faire apparaître que les deux courbes **se ressemblent** mais que **les axes sont différents**
(m d'un côté, s de l'autre) : c'est la source de confusion la plus fréquente.

Sous les deux repères, la relation encadrée
$\lambda = v \times T = \dfrac{v}{f}$ avec les unités (m ; m·s⁻¹ ; s ; Hz).

## 2. `pc-onde-longitudinale-transversale` — direction de la perturbation

*Utilisée par* : leçon `pc-ondes-bases` ; 1 exercice (niveau 1).

Deux vignettes empilées, chacune montrant un **ressort horizontal** (zigzag / hélice `solideE`)
accroché à gauche à un **mur** (trait vertical gris hachuré). Dans les deux, une **flèche noire
horizontale** « **sens de propagation** » est placée sous le ressort, pointant vers la droite.

- **Vignette du haut, « Onde transversale »** : spires **régulièrement espacées** ; à l'extrémité
  droite, une **double flèche `solideA` verticale** (la main secoue de haut en bas). Annotation
  `\scriptsize` : « perturbation **perpendiculaire** à la propagation ».
- **Vignette du bas, « Onde longitudinale »** : spires **resserrées au milieu** (zone de compression
  bien visible) et plus écartées de part et d'autre ; à l'extrémité droite, une **double flèche
  `solideA` horizontale**. Annotation : « perturbation **parallèle** à la propagation ».

Aucune graduation, aucun axe.

## 3. `pc-reflexion-transmission` — réflexion, absorption, transmission

*Utilisée par* : leçon `pc-ondes-bases` ; 2 exercices (niveaux 1 et 3).

Au centre, un **rectangle vertical** représentant la paroi (milieu B), rempli d'un **motif de
briques** gris/orangé.

- Étiquette « **Milieu A** » à gauche du rectangle, « **Milieu B** » au-dessus.
- **Flèche `solideA`** arrivant du bas-gauche sur la face gauche, étiquetée $I$ (onde incidente).
- **Flèche `solideB`** repartant vers le haut-gauche depuis le même point d'impact, étiquetée
  « **Réflexion** $I_r$ » (angles de réflexion symétriques par rapport à la normale).
- **Trois flèches `solideE`** divergentes sortant de la face droite (haut-droite, horizontale,
  bas-droite), avec l'étiquette « **Transmission** $I_t$ » près de la flèche horizontale.
- **Bandeau `solideD`** en bas du rectangle portant « **Absorption** $I_a$ » en blanc, avec deux ou
  trois petites flèches ondulées descendantes à l'intérieur de la paroi (dissipation en chaleur).
- En légende, la relation encadrée $I = I_r + I_a + I_t$ et, en `\scriptsize` : « l'énergie
  incidente se répartit intégralement entre les trois parts ».

## 4. `pc-telemetre-ultrasons` — mesure de distance par écho

*Utilisée par* : leçon `pc-son` ; 1 exercice (niveau 1, justification du facteur 2).

**Partie haute — le montage.** À gauche, un **capteur** (petit boîtier rectangulaire gris portant
deux pastilles « É » émetteur et « R » récepteur). À droite, un **obstacle** (rectangle hachuré,
vertical, du sol au haut de la figure).

- **Flèche `solideA`** du capteur vers l'obstacle, étiquetée « salve émise » ;
- **Flèche `solideB`** de l'obstacle vers le capteur, tracée **légèrement en dessous** de la
  précédente, étiquetée « écho » ;
- **Double flèche `solideD`** au niveau du sol entre capteur et obstacle, cotée $d$.

**Partie basse — le chronogramme.** Repère « tension (V) » / « $t$ (s) », avec **deux pics
triangulaires étroits** : un pic `solideA` haut à l'origine (« émission »), un pic `solideB` plus
bas plus loin (« réception de l'écho »). Entre les deux pics, une **double flèche `solideD`** annotée
$\Delta t$.

Sous la figure, la relation encadrée $d = \dfrac{v_{\text{US}} \times \Delta t}{2}$ et, en
`\scriptsize` : « pendant $\Delta t$, l'onde parcourt $2d$ : **aller-retour** ».

## 5. `pc-echelle-decibels` — échelle des niveaux sonores

*Utilisée par* : leçon `pc-son`.

Une **règle verticale** graduée de 0 à 130 dB (pas de 10), remplie d'un **dégradé
`solideE` → `solideD` → `solideA`** du bas vers le haut.

Deux colonnes de repères en vis-à-vis, parfaitement alignées :

| $L$ (dB) | $I$ (W·m⁻²) | Étiquette à droite |
|---|---|---|
| 0 | $10^{-12}$ | seuil d'audibilité ($I_0$) |
| 40 | $10^{-8}$ | chuchotement |
| 60 | $10^{-6}$ | conversation normale |
| 80 | $10^{-4}$ | conversation à haute voix |
| 100 | $10^{-2}$ | lecteur MP3 |
| 110 | $10^{-1}$ | discothèque, concert |
| 130 | $10^{1}$ | réacteur d'avion — **seuil de la douleur** |

L'axe des dB est **régulier** ; la colonne des intensités montre en regard des puissances de 10 :
c'est tout l'intérêt de la figure (échelle logarithmique).

À droite, hors de la règle, un petit encadré : $L = 10\log(I/I_0)$ avec
$I_0 = 1{,}0 \times 10^{-12}$ W·m⁻², et deux flèches courbes `solideD` annotées
« $\times 2$ sur $I$ → $+3$ dB » et « $\times 10$ sur $I$ → $+10$ dB ».

## 6. `pc-intensite-distance` — décroissance de l'intensité acoustique

*Utilisée par* : leçon `pc-son` ; 1 exercice (niveau 3, division par 4).

À gauche, une **enceinte** (parallélépipède en perspective cavalière) faisant office de source
ponctuelle. De la source partent **quatre droites divergentes** formant un cône.

- Deux **calottes sphériques** bleu clair perpendiculaires à l'axe : une **petite** à la distance
  $r_1$, une **grande** (deux fois plus loin) à la distance $r_2 = 2r_1$ ; contour de la grande
  complété en **pointillé** pour la partie cachée.
- Cotes `solideD` : $r_1$ et $r_2$ mesurées depuis la source, sur l'axe.
- Une pastille **« 1 »** près de la petite calotte, une pastille **« 2 »** près de la grande.
- Sur chaque calotte, une étiquette : « $S_1 = 4\pi r_1^2$ » et « $S_2 = 4\pi r_2^2 = 4\,S_1$ ».

Légende `\scriptsize` : « la même puissance acoustique se répartit sur une surface **4 fois plus
grande** : $I$ est **divisée par 4** ».

## 7. `pc-spectre-em` — spectre des ondes électromagnétiques

*Utilisée par* : leçon `pc-ondes-em` ; 1 exercice (niveau 1, domaine du visible).

Une **barre horizontale** découpée en bandes colorées, encadrée par deux axes.

- **Axe du haut** (flèche `solideA` vers la **gauche**), étiqueté « **Fréquence $\nu$ croissante** » :
  la fréquence **augmente vers la gauche**. Repères portés au-dessus : $3{,}0\times10^{19}$ Hz (à
  l'aplomb de 10 pm), 300 GHz (à 1 mm), 30 kHz (à 10 km).
- **Bandes**, de gauche à droite, avec étiquettes : « **Rayons gamma** », « **Rayons X** »,
  « **UV** », « **Visible** » (bande étroite en dégradé arc-en-ciel), « **IR** »,
  « **Ondes radiofréquences** » (la plus large).
- **Axe du bas** (flèche vers la droite), étiqueté « **Longueur d'onde $\lambda$ croissante** », avec
  les graduations : 1 fm, 10 pm, 10 nm, 0,4 µm, 0,8 µm, 1 mm, 10 km.
- **Zoom du visible** : deux traits pointillés `solideF` partant des bords de la bande « Visible » et
  s'évasant vers le bas jusqu'à un **rectangle en dégradé** violet → bleu → vert → jaune → orange →
  rouge, étiqueté « **VISIBLE** », avec « **400 nm** » à gauche et « **800 nm** » à droite.

**Ne pas reprendre le repère « 300 THz »** du livre : il y est placé à la frontière visible/IR alors
que $\lambda = c/\nu = 1{,}0$ µm est déjà dans l'infrarouge. Si on le porte, l'aligner sur **1 µm**,
dans la bande IR (un exercice de niveau 3 fait justement calculer cette valeur).

## 8. `pc-spectres-sources` — spectres de quatre sources lumineuses

*Utilisée par* : leçon `pc-ondes-em` ; 2 exercices (le `grid` polychromatique / monochromatique et
un QCM de niveau 3).

**Quatre vignettes en 2 × 2**, toutes de même largeur, toutes graduées **400 / 500 / 600 / 700 nm**
sous l'image.

1. **Lampe spectrale au mercure** : rectangle **noir** traversé d'une dizaine de **raies verticales
   fines** de couleurs variées (violettes à gauche, bleues, vert-bleu, vertes, jaunes, une raie
   orangée isolée à droite). *Ne chiffrer aucune longueur d'onde de raie* : le livre ne les donne
   pas. Titre : « Lampe spectrale — spectre de raies, polychromatique ».
2. **Laser rouge** : même rectangle noir, **une seule raie fine rouge** près de 700 nm. Titre :
   « Laser — monochromatique ».
3. **LED rouge** : même rectangle noir, **une bande rouge large** entre 600 et 700 nm environ.
   Titre : « LED rouge — polychromatique ».
4. **LED blanche** : un **repère** (intensité en unité arbitraire / longueur d'onde en nm) et non un
   rectangle noir : un **pic étroit bleu** centré vers 450 nm, étiqueté « **LED bleue** », puis une
   **large bosse** en dégradé arc-en-ciel culminant entre 550 et 600 nm et redescendant vers 700 nm,
   étiquetée « **Luminophore** ». Le creux entre les deux **ne redescend pas à zéro**. Titre :
   « LED blanche — polychromatique ».

## 9. `pc-corps-chauffe` — émission d'un corps chauffé

*Utilisée par* : leçon `pc-ondes-em` ; 1 exercice (niveau 3, $\lambda_{\max}$ et température).

Repère : ordonnée « **Intensité (unité arbitraire)** », abscisse « $\lambda$ (nm) », graduée
**régulièrement** de 0 à 2 000 nm (pas de 500). *Corriger ici le livre, dont les graduations
0, 400, 800, 1 000, 1 500, 2 000 sont inégalement espacées et rendent toute lecture impossible.*

- **Rectangle vertical en dégradé arc-en-ciel** entre 400 et 800 nm, étiqueté « **Visible** » ;
  « **Ultraviolet** » à sa gauche, « **Infrarouge** » à sa droite.
- **Courbe `solideA`** légendée « **6 000 K** » : haute, maximum au voisinage de **500 nm** (dans le
  visible), puis décroissance lente jusqu'à 2 000 nm.
- **Courbe `solideB`** légendée « **3 000 K** » : nettement plus basse, maximum vers **1 000 nm**
  (dans l'infrarouge), décroissance lente.
- Deux traits verticaux pointillés depuis chaque maximum jusqu'à l'axe, annotés
  $\lambda_{\max}(6\,000\ \mathrm{K})$ et $\lambda_{\max}(3\,000\ \mathrm{K})$, avec une **flèche
  `solideD`** de l'un vers l'autre annotée « $T$ augmente → $\lambda_{\max}$ **diminue** ».

Les positions des maximums sont **qualitatives** (le livre ne donne pas la loi de Wien) : ne porter
aucune valeur chiffrée de $\lambda_{\max}$ sur l'axe, seulement l'ordre relatif.

## 10. `pc-photon-panneau` — du photon au panneau photovoltaïque

*Utilisée par* : leçon `pc-lumiere-energie` ; 1 exercice (niveau 1, $E = h\nu$) et l'**exercice
complet guidé** « Le refuge solaire ».

Figure en **deux parties séparées par un trait vertical fin**.

**Partie gauche — absorption d'un photon.** Deux **niveaux d'énergie** horizontaux (traits noirs
étiquetés $E_1$ en bas, $E_2$ en haut). Une **flèche ondulée `solideD`** arrivant de la gauche,
étiquetée « photon $E = h\nu$ », et une **flèche verticale montante `solideA`** entre les deux
niveaux, portant un petit disque noir (l'électron) qui passe de $E_1$ à $E_2$. Étiquette
« **absorption** » et, en `\scriptsize` : « applications : photorésistance, photodiode, cellule
photovoltaïque ».

**Partie droite — chaîne énergétique du panneau.** Trois blocs alignés horizontalement, reliés par
des flèches épaisses :

`Énergie rayonnante` (flèche `solideD`) → **`Cellule photovoltaïque`** (rectangle, plus grand) →
`Énergie électrique (utile)` (flèche `solideE`),

avec une **flèche `solideA` descendante** partant du bloc central vers le bas, étiquetée
« **Énergie perdue** (thermique, rayonnante) ».

Sous les blocs, les deux relations : $P_{\text{lumineuse}} = P_{\text{surf}} \times S$ et
$r = \dfrac{P_{\max}}{P_{\text{surf}} \times S}$, avec les unités (W ; W·m⁻² ; m² ; sans unité).
