# Figures à dessiner — unité « 2I2D Tle : énergie électrique et chaîne de puissance »

Douze figures TikZ sont référencées par l'unité `2i2d-energie`
(`content/units/110-2i2d-energie.yaml` et `content/lessons/2i2d-energie-*.md`). Tant qu'elles
n'existent pas dans `figures/tikz/`, `make content` échoue avec « figure inconnue » : ces douze
fichiers sont donc un **prérequis de build**.

Deux figures existantes sont réutilisées telles quelles, **rien à dessiner** pour elles :

- `pc-bilan-convertisseur` (diagramme sagittal du rendement) — leçon `2i2d-energie-chaine` et
  1 exercice ;
- `info-chaine-information` (ACQUÉRIR / TRAITER / COMMUNIQUER) — leçon `2i2d-energie-chaine` et
  1 exercice.

## Conventions communes

- un fichier par figure : `figures/tikz/<ID>.tex`, `\documentclass[tikz,border=4pt]{standalone}` +
  `\usepackage{liaisons}` ;
- couleurs de la bibliothèque : `solideA` (rouge), `solideB` (bleu), `solideD` (orange),
  `solideE` (vert) ;
- **code couleur de l'unité** : puissance et flux d'énergie = `solideD` ; pertes = `solideA` ;
  grandeurs électriques et courbes de mesure = `solideB` ; solaire / gain = `solideE` ;
- textes en `\small` / `\scriptsize`, **en français**, notations du cours ($U$, $I$, $P$, $E$, $Q$,
  $\eta$, Wc, Ah, Wh, DoD) ;
- largeur cible ≈ 8 cm (affichage mobile), hauteur ≤ 6 cm ;
- symboles électriques **normalisés européens** (résistance = rectangle, jamais le zigzag
  américain, sauf sur la vignette qui compare explicitement les deux).

---

## 1. `2i2d-symboles-electriques` — planche des symboles normalisés

*Utilisée par* : leçon `2i2d-energie-schemas` ; 4 exercices (transformateur, moteur, arrêt
d'urgence, fusible).

Planche de **10 vignettes** en grille 5 colonnes × 2 lignes, chaque vignette = un cadre fin
gris clair (≈ 1,4 × 1,4 cm) contenant le symbole en trait noir, avec son nom en `\scriptsize`
**sous** le cadre.

| Rang | Vignette | Tracé |
|---|---|---|
| 1 | Pack batterie | Alternance de 2 traits longs et 2 traits courts verticaux, `+` en haut, `−` en bas |
| 2 | Transformateur | Deux cercles sécants superposés verticalement |
| 3 | Moteur | Cercle contenant `M` et, en dessous, le signe `~` |
| 4 | Lampe | Cercle barré d'une croix (×) |
| 5 | DEL | Triangle pointe à droite + barre verticale, deux petites flèches sortantes obliques |
| 6 | Transistor | Cercle, base `B` à gauche, collecteur `C` en haut, émetteur `E` en bas fléché |
| 7 | Résistance | Rectangle sur un fil horizontal, mention `norme européenne` en `\tiny` |
| 8 | Arrêt d'urgence | Contact **fermé** au repos surmonté d'une tête « coup de poing » (demi-disque) |
| 9 | Sectionneur à fusible | Contact ouvert associé au rectangle allongé du fusible |
| 10 | Disjoncteur différentiel | Contact avec astérisque + tore (ellipse) en trait pointillé |

Les trois dernières vignettes (8, 9, 10) sont regroupées par un liseré `solideA` et une étiquette
`PROTECTIONS` en `\scriptsize`, avec sous elles la mention
« différentiel → **personnes** ; fusible et magnéto-thermique → **matériel** ».

## 2. `2i2d-convertisseurs` — les quatre convertisseurs d'énergie

*Utilisée par* : leçon `2i2d-energie-schemas` ; 3 exercices (onduleur, hacheur, association).

Quatre vignettes alignées horizontalement. Chaque vignette : un **carré** (≈ 1,2 cm) traversé par
une **diagonale montante** (du coin bas gauche au coin haut droit), la grandeur d'entrée écrite en
haut à gauche, la grandeur de sortie en bas à droite ; un fil entrant à gauche, un fil sortant à
droite (flèche `solideD` sur le fil de sortie).

| Vignette | Entrée → sortie | Étiquette sous le carré |
|---|---|---|
| 1 | `=` → `~` | **Onduleur** |
| 2 | `~` → `=` | **Redresseur** |
| 3 | `=` → `=` | **Hacheur** |
| 4 | `~` → `~` | **Variateur** (gradateur) |

Sous la ligne de vignettes, en `\scriptsize` : « `=` continu · `~` alternatif ».

## 3. `2i2d-demarrage-direct` — schéma de puissance et de commande

*Utilisée par* : leçon `2i2d-energie-schemas` ; 4 exercices (puissance/commande, S1, conditions de
démarrage, `order` du circuit de puissance) et 1 exercice numérique (T1).

Deux colonnes séparées par un trait vertical pointillé gris.

**Colonne gauche — circuit de puissance** (fils épais, `solideD` pour le repère « PUISSANCE ») :
trois lignes horizontales étiquetées `3 × 400 V` en haut, puis de haut en bas
`Q0` (sectionneur 3 pôles + fusibles `F1`) → `KM1` (3 contacts reliés par un trait pointillé) →
`F4` (relais thermique, 3 bilames) → `M3` (cercle avec `M` et `3~`) relié au symbole de terre.

**Colonne droite — circuit de commande** (fils fins, repère « COMMANDE » en `solideB`), boucle
verticale unique de haut en bas : fusible `F2` → transformateur `T1` (deux cercles sécants, avec
les annotations `400 V`, `50 V·A`, `24 V`) → fusible `F3` → contact `F4` (NF) → bouton poussoir
`S2` (NF, étiqueté *Arrêt*) → bouton poussoir `S1` (NO, étiqueté *Marche*) **doublé en parallèle**
par le contact d'auto-maintien `KM1` → bobine `KM1` (rectangle).

Le contact d'auto-maintien et son étiquette `auto-maintien` sont mis en évidence en `solideE`
(c'est le point de la question). Aucun texte en anglais.

## 4. `2i2d-chaine-puissance` — les cinq blocs et les grandeurs de lien

*Utilisée par* : leçon `2i2d-energie-chaine` ; 4 exercices (`order`, `match`, ordres, effort/flux).

Cinq rectangles de même gabarit alignés horizontalement, reliés par de **grosses flèches**
`solideD` (les liens de puissance) :

`ALIMENTER` → `DISTRIBUER` → `CONVERTIR` → `TRANSMETTRE` → `AGIR`

- sous chaque bloc, en `\scriptsize` et en gris : un composant type
  (`Batterie` / `Contacteur` / `Moteur` / `Réducteur` / `Roue`) ;
- **au-dessus de chaque flèche**, le couple effort/flux du domaine concerné :
  `U (V) · I (A)` sur les deux premières, `C (N·m) · ω (rad·s⁻¹)` sur les deux dernières ;
- une flèche `solideB` fine arrive **par le haut** sur le bloc `DISTRIBUER`, étiquetée
  **Ordres** (venant de la chaîne d'information) ;
- une flèche `solideA` fine part **vers le bas** de chaque bloc `CONVERTIR` et `TRANSMETTRE`,
  regroupée en une étiquette `Pertes`.

Un cadre englobant en trait pointillé porte le titre `Chaîne d'énergie (chaîne de puissance)`.

## 5. `2i2d-rendements-cascade` — rendements en cascade (diagramme de flux)

*Utilisée par* : leçon `2i2d-energie-chaine` ; 3 exercices (rendement global, cascade, remontée du
trolleybus) et l'exercice guidé du trolleybus.

Diagramme de type Sankey **simplifié** (bandes rectangulaires horizontales, largeur
proportionnelle à la puissance), de gauche à droite, sur deux valeurs chiffrées cohérentes avec
les exercices :

- bande d'entrée `solideD` de hauteur 1 unité, étiquetée `336 W (batterie)` ;
- premier bloc encadré `Hacheur — η₁ = 0,95` ; une bande `solideA` fine se détache vers le bas,
  étiquetée `pertes 16,8 W` ;
- bande intermédiaire de hauteur 0,95 unité, étiquetée `319,2 W` ;
- second bloc encadré `Moteur — η₂ = 0,85` ; bande `solideA` vers le bas, `pertes 47,9 W` ;
- bande de sortie de hauteur 0,81 unité, étiquetée `271,3 W (roue)`.

Sous le diagramme, encadré : $\eta_{\text{global}} = \eta_1 \times \eta_2 = 0{,}95 \times 0{,}85 =
0{,}8075$, et en `\scriptsize` : « on **descend** la chaîne en multipliant, on la **remonte** en
divisant ».

## 6. `2i2d-batterie-associations` — trois branchements de 4 modules 12 V / 7 Ah

*Utilisée par* : leçon `2i2d-energie-batteries` ; 5 exercices et l'exercice guidé du ferry-boat.

Trois colonnes titrées **Parallèle**, **Série-parallèle**, **Série**. Chaque module est un petit
rectangle `solideB` clair portant `12 V` en haut et `7 Ah` en bas, bornes `−` à gauche et `+` à
droite. Rails de raccordement en `solideA` (fil `+`) et noir (fil `−`).

- *Parallèle* : 4 modules empilés verticalement, tous les `+` sur un rail commun, tous les `−`
  sur l'autre.
- *Série-parallèle* : 2 lignes de 2 modules chaînés, les deux lignes mises en parallèle.
- *Série* : 4 modules alignés horizontalement, `+` de l'un relié au `−` du suivant.

Sous chaque colonne, un tableau de trois lignes en `\scriptsize` :

| | Parallèle | Série-parallèle | Série |
|---|---|---|---|
| $U$ | 12 V | 24 V | 48 V |
| $Q$ | 28 Ah | 14 Ah | 7 Ah |
| $E = U \times Q$ | **336 Wh** | **336 Wh** | **336 Wh** |

Les trois valeurs `336 Wh` sont encadrées en `solideE` et reliées par une accolade portant la
mention « même énergie dans les trois cas ».

## 7. `2i2d-courbe-decharge` — courbes de décharge lithium-ion / plomb-acide

*Utilisée par* : leçon `2i2d-energie-batteries` ; 2 exercices (allure de la décharge, avantage du
lithium).

Repère quadrillé léger. Ordonnée **Tension de batterie (V)** graduée de 42 à 60 par pas de 2 ;
abscisse **Profondeur de décharge (%)** graduée de 0 à 100 par pas de 10.

- Courbe **Lithium-ion** en `solideA` : départ ≈ 58 V, plateau très plat de 56 à 54 V jusqu'à
  environ 80 %, puis coude marqué et chute rapide vers 46 V à 100 %. Étiquette `Lithium-ion` posée
  sur le plateau.
- Courbe **Plomb-acide** en `solideB` : départ ≈ 56 V, décroissance continue et de plus en plus
  rapide jusqu'à ≈ 42 V à 100 %. Étiquette `Plomb-acide` le long de la courbe.

Une ligne horizontale pointillée `solideD` à 48 V étiquetée `tension de coupure (exemple)`, et une
double flèche verticale en `\scriptsize` montrant que la lithium-ion l'atteint bien plus tard.

*Note à porter en `\scriptsize`* : les valeurs de départ (58 V et 56 V) sont lues sur le graphique
du manuel, qui ne les imprime pas.

## 8. `2i2d-cycles-dod` — nombre de cycles en fonction de la profondeur de décharge

*Utilisée par* : leçons `2i2d-energie-batteries` et `2i2d-energie-gestion` ; 2 exercices.

Diagramme à **trois barres verticales**, ordonnée `Nombre de cycles charge/décharge` graduée de 0
à 5 000 par pas de 500, abscisse `Profondeur de décharge`.

| Barre | Valeur | Couleur |
|---|---|---|
| 70 % | ≈ 1 450 | `solideA` |
| 50 % | ≈ 2 400 | `solideD` |
| 30 % | ≈ 4 400 | `solideE` |

Valeur inscrite au sommet de chaque barre. Sous le graphique, en `\scriptsize` :
« batteries SAFT STM 5-140 MR — moins on décharge, plus le pack dure » et la mention
« valeurs lues sur le graphique du constructeur, non imprimées ».

## 9. `2i2d-pv-associations` — trois branchements de 4 cellules photovoltaïques

*Utilisée par* : leçon `2i2d-energie-photovoltaique` ; 4 exercices.

Même structure que `2i2d-batterie-associations`, en trois colonnes **Parallèle**,
**Série-parallèle**, **Série**. Chaque cellule est un rectangle `solideB` foncé, texturé de fines
lignes verticales (aspect module PV), portant l'étiquette `18 V · 5,56 A`.

Sous chaque colonne :

| | Parallèle | Série-parallèle | Série |
|---|---|---|---|
| $U$ | 18 V | 36 V | 72 V |
| $I$ | 22,24 A | 11,12 A | 5,56 A |
| $P = U \times I$ | **≈ 400 W** | **≈ 400 W** | **≈ 400 W** |

Mention en `\scriptsize` : « valeurs exactes 400,3 W ; le manuel arrondit le courant à 22,2 A puis
écrit 400 W ».

## 10. `2i2d-pv-orientation` — irradiance, surface, orientation et inclinaison

*Utilisée par* : leçon `2i2d-energie-photovoltaique` ; 3 exercices (irradiance, rendement,
orientation).

Vue de profil, dessin au trait.

- Un **panneau** (rectangle allongé `solideB`, épaisseur visible) posé sur un support, incliné d'un
  angle $\beta$ par rapport à l'horizontale ; l'angle $\beta$ est coté par un arc `solideD`.
- Un **faisceau** de 4 à 5 flèches parallèles `solideD` venant du haut à gauche (le Soleil, petit
  disque `solideD` en haut à gauche), avec l'étiquette
  $E_{\text{irr}} = 1\,000\ \mathrm{W \cdot m^{-2}}$.
- La **normale** au panneau en trait pointillé, et l'angle d'incidence $i$ entre le faisceau et la
  normale, coté par un arc fin ; annotation en `\scriptsize` « production maximale quand $i = 0$ ».
- Cote de la **surface** $S$ le long du panneau.
- Une flèche `solideE` sortant du panneau vers la droite, étiquetée
  $P_{\text{crête}} = \eta \times E_{\text{irr}} \times S$, avec la mention `courant continu (=)`.

En bas, une petite rose des vents (`Nord = 0°`, `Est = 90°`, `Sud = 180°`) rappelant la convention
d'orientation utilisée dans le modèle de simulation, et la mention en `\scriptsize` :
« si $\beta = 0$ (panneau à plat), l'orientation n'a aucun effet ».

## 11. `2i2d-ferry-bilan` — production solaire et besoin journalier du ferry-boat

*Utilisée par* : leçons `2i2d-energie-photovoltaique` et `2i2d-energie-gestion` ; 3 exercices
(variation saisonnière, couverture) et l'exercice guidé des panneaux.

Diagramme mixte, abscisse = les 12 mois (`Jan` … `Déc`), ordonnée `Énergie par jour (kWh)` graduée
de 0 à 55 par pas de 5.

- **Barres** `solideE` = production photovoltaïque quotidienne simulée (valeurs lues sur le
  graphique du manuel, à porter telles quelles) : 4,3 ; 7 ; 11 ; 14,3 ; 16,3 ; 18,3 ; 17,9 ; 15 ;
  12,5 ; 8,8 ; 6 ; 4,6.
- **Ligne brisée en escalier** `solideA`, épaisse, = besoin journalier en mode écoconduite :
  22,75 kWh de janvier à février et de novembre à décembre ; 28,44 kWh de mars à avril et de
  septembre à octobre ; 51,19 kWh de mai à août. Étiquette `Besoin (écoconduite)`.
- **Ligne brisée en escalier** `solideA` en pointillés = besoin sans écoconduite : 32,45 ; 40,56 ;
  73,01 kWh sur les mêmes périodes — si l'échelle le permet, sinon la mentionner en légende.

Deux annotations `\scriptsize` avec flèche : `janvier : 19 % du besoin` et
`juin : ≈ 36 % du besoin`. Légende sous le graphique.

## 12. `2i2d-alimentation-ferry` — synoptique de l'alimentation électrique

*Utilisée par* : leçon `2i2d-energie-gestion` ; sert d'appui aux exercices sur la nature des
tensions et sur le rôle du BMS.

Synoptique de blocs (rectangles à coins arrondis), flux de puissance en grosses flèches `solideD`,
flux d'information en flèches fines `solideB` pointillées.

Disposition en deux étages :

- en haut à gauche, `16 panneaux photovoltaïques propulsion` → flèche `= Énergie électrique` →
  `Chargeur propulsion` → flèche `Courant de charge (=)` → `Parc 1 (384 V)` et `Parc 2 (384 V)` ;
- en bas à gauche, `Prise de quai` avec l'étiquette **`~` réseau alternatif** en `solideA`
  (c'est le seul point en alternatif de tout le schéma), reliée au même `Chargeur propulsion` ;
- à droite des parcs, `Propulsion (moteurs)` ;
- au centre, `Battery Management System` relié aux deux parcs par des flèches fines `solideB`
  étiquetées `Mesures U, I, température`, et au chargeur par `Consignes U et I (bus CAN)` ;
- sous le BMS, `Ventilateurs batteries`, relié par `Commande ventilateurs`.

Une pastille `solideE` marquée `=` est posée sur chaque lien continu, une pastille `solideA`
marquée `~` sur le seul lien alternatif (prise de quai). Légende en `\scriptsize` :
« un seul point en alternatif : le raccordement au réseau du quai ».
