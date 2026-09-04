# Figures à dessiner — unité « Statique et résistance des matériaux »

Cette liste recense les **14 figures** référencées par `content/units/10-statique-rdm.yaml` et par les
quatre leçons `content/lessons/statique-*.md` et `content/lessons/rdm-*.md`.
Tant qu'elles ne sont pas créées, `tools/validate.py` signalera « référence la figure inconnue … »
au niveau de `dist/content.json`.

## Conventions communes

- un fichier `figures/tikz/<id>.tex` par figure, `\documentclass[tikz,border=4pt]{standalone}` +
  `\usepackage{liaisons}` (comme `figures/tikz/transmission-poulies.tex`, pris comme modèle) ;
- couleurs de `liaisons.sty` : `solideA` (rouge) pour les **efforts/forces**, `solideB` (bleu) pour les
  **pièces isolées**, `solideD` (orange) pour les **cotes et bras de levier**, `solideE` (vert) pour les
  **appuis**, `solideF` (violet) pour les **repères et axes** ;
- gabarit : largeur utile ≈ 8 cm, hauteur ≤ 5 cm (l'appli plafonne les figures à 240 px de haut) ;
- étiquettes en `\small`, notations mathématiques identiques à celles des leçons
  ($\vec{F}$, $d$, $M$, $\sigma$, $\varepsilon$, $R_e$, $R_r$, $N$, $S$, $G$) ;
- sol/bâti : trait plein + hachures obliques (macro locale `\batihoriz`, cf. `transmission-poulies.tex`).

Les numéros « note n° X » renvoient à la section « Figures à redessiner » de
`docs/notes/materiaux-rdm-1re.md` (pages du chapitre 6/7 de 1re), ou à `docs/notes/cours-tle-b.md` /
`docs/notes/cours-tle-c.md` quand c'est précisé.

---

## Compétence `statique-actions`

### 1. `statique-poids` — l'action de la pesanteur (note 1re n° 12, p. 110)

Deux vignettes séparées par un signe « ⇔ ».
- **Gauche** : un solide 3D simple (parallélépipède ou coin) en gris clair, parcouru par un **champ** de
  petites flèches verticales descendantes (≈ 12 flèches réparties dans le volume, `solideF`, fines).
- **Droite** : le **même** solide, avec un point noir marqué **$G$** au centre, et **une seule** flèche
  épaisse `solideA` descendante étiquetée $\vec{P}$, partant de $G$.
- Sous les deux vignettes, un cartouche : $P = m \times g$ avec les unités (N) = (kg) × (m/s²), et la
  mention $g = 9{,}81$ m/s².
- Petit repère $(\vec{x}, \vec{y})$ en bas à gauche, $y$ vers le haut.

### 2. `statique-moment-force` — moment et bras de levier (note 1re n° 16, p. 111 ; tle-b n° 20a/20b)

Deux schémas côte à côte, séparés par un filet vertical fin.
- **Schéma (a)** : un pivot **$P$** (petit cercle noir) à gauche ; un segment horizontal en pointillés
  jusqu'au point **$A$** à droite, coté **$d$** (double flèche `solideD` sous le segment) ; en $A$, une
  flèche `solideA` **verticale vers le haut** étiquetée $\vec{F}$, perpendiculaire à $PA$. Légende :
  « $M = F \times d$ ».
- **Schéma (b)** : même pivot $P$ et même point $A$, mais la flèche $\vec{F}$ en $A$ est **oblique**
  (≈ 40° au-dessus de l'horizontale) ; sa **droite d'action** est prolongée en pointillés fins des deux
  côtés ; depuis $P$, on abaisse la **perpendiculaire** à cette droite, tracée en `solideD` et cotée **$d$**
  (angle droit marqué au pied). Légende : « $d$ est mesurée perpendiculairement au **support** de $\vec{F}$ ».

### 3. `statique-moment-angle` — influence de l'angle (note 1re n° 18, p. 112)

Trois vignettes alignées, identiques sauf l'orientation de la force. Chacune : une clé plate stylisée
(rectangle allongé `solideB` à bouts arrondis) articulée en **$O$** (petit cercle) à gauche, tête à droite ;
une flèche `solideA` étiquetée $\vec{F}$ appliquée à l'extrémité droite, **même longueur** dans les trois
vignettes ; la cote $d$ (`solideD`) est identique dans les trois.
- (a) $\vec{F}$ **perpendiculaire** au manche → légende « moment **maximal** » ;
- (b) $\vec{F}$ oblique (≈ 45°) → légende « moment intermédiaire » ; l'angle est marqué ;
- (c) $\vec{F}$ **colinéaire** au manche (horizontale, vers la droite) → légende « moment **nul** ».

### 4. `statique-couple` — le couple (note 1re n° 20, p. 112 ; tle-b n° 22)

Un cylindre vu en perspective (ellipse supérieure + deux génératrices), axe vertical.
Sur la face supérieure : deux flèches **tangentielles opposées** `solideA` étiquetées $\vec{F_1}$ et
$\vec{F_2}$, appliquées à l'extrémité de deux rayons tracés depuis l'axe et cotés $r_1$ et $r_2$
(traits `solideD`). Au-dessus du cylindre, une flèche **circulaire** noire autour de l'axe étiquetée
$\vec{T}$. Sous la figure, les deux relations : $\vec{F_1} + \vec{F_2} = \vec{0}$ et
$T = F_1 \times r_1 + F_2 \times r_2$.

### 5. `statique-projection` — projection d'un vecteur (note 1re n° 22, p. 113 ; tle-b n° 18)

Repère orthonormé d'origine $O$ : axe $x$ vers la droite (vecteur unitaire $\vec{i}$), axe $y$ vers le haut
($\vec{j}$), axes en `solideF`. Un vecteur $\vec{F}$ (`solideA`, épais) part de $O$ vers le **quadrant
supérieur gauche** (donc $F_x < 0$ et $F_y > 0$). L'angle **$\beta$** est marqué **entre $\vec{F}$ et
l'axe $y$** (arc + étiquette). Projections en pointillés : $\vec{F_y}$ portée par $y$ (flèche vers le haut)
et $\vec{F_x}$ portée par $x$ (flèche vers la **gauche**). Cartouche :
$F_x = -F \sin\beta$, $F_y = +F \cos\beta$, $F_z = 0$.

### 6. `statique-torseur` — écriture d'un torseur (note tle-b n° 23, p. 269)

À droite, la grande accolade du torseur $\{\tau_{1 \rightarrow 2}\}$ à **deux colonnes** :
colonne gauche $X_{1 \rightarrow 2}$, $Y_{1 \rightarrow 2}$, $Z_{1 \rightarrow 2}$ ;
colonne droite $L_{A\,1 \rightarrow 2}$, $M_{A\,1 \rightarrow 2}$, $N_{A\,1 \rightarrow 2}$ ;
indice **$A$** en bas à droite de l'accolade fermante.
À gauche, deux cartouches à coins arrondis reliés par des flèches fines : « **résultante** (la force),
en N » pointant vers la colonne gauche, et « **moment**, en N·m » vers la colonne droite. Sous la figure,
un troisième cartouche : « **point de réduction** : le point où est exprimé le moment » avec une flèche
vers l'indice $A$.

---

## Compétence `statique-pfs`

### 7. `statique-deux-forces` — équilibre sous 2 forces (note tle-c n° 1, p. 270)

Deux vignettes séparées par le mot « ou ».
- (a) une barre inclinée à ≈ 45° (rectangle `solideB` à bouts arrondis, un petit trou circulaire à chaque
  extrémité) ; une flèche `solideA` à chaque extrémité, dirigée **vers l'extérieur**, le long de l'axe de la
  barre → légende « **traction** » ;
- (b) la même barre avec les deux flèches dirigées **vers l'intérieur** → légende « **compression** ».
Sous les deux vignettes : « même support, même intensité, sens opposés ».

### 8. `statique-trois-forces` — méthode des 3 forces (note tle-c n° 2 et n° 3, p. 270)

Figure en deux parties côte à côte.
- **Gauche (le schéma)** : une barre/plateau incliné `solideB` posé en **$A$** sur un appui (petit
  demi-disque `solideE`) et retenu en **$B$** ; le poids $\vec{P}$ (`solideA`, vertical descendant)
  appliqué en **$G$** au milieu. Les **trois droites d'action** sont prolongées en pointillés fins et se
  coupent en un point **$I$**, marqué par un petit cercle et étiqueté « point de concours ».
- **Droite (le dynamique)** : les trois vecteurs mis **bout à bout** formant un **triangle fermé**
  (tracé `solideA`, sommets marqués par de petits carrés) : $\vec{A_{2 \rightarrow S}}$ montant,
  $\vec{P}$ vertical descendant, $\vec{B_{0 \rightarrow S}}$ horizontal. Sous le triangle :
  $\vec{A_{2 \rightarrow S}} + \vec{B_{0 \rightarrow S}} + \vec{P} = \vec{0}$, et le titre « dynamique fermé ».
*Remarque : le schéma d'origine (p. 270) est rogné dans le scan ; le tracé ci-dessus est une reconstruction
pédagogique équivalente, à ne pas présenter comme la reproduction exacte du livre.*

### 9. `statique-appuis` — les symboles d'appui (note 1re n° 4, p. 98 ; tle-c n° 7, 8, 9)

Trois vignettes alignées, chacune avec la poutre figurée par un trait horizontal épais `solideB` et le sol
par un trait + hachures obliques.
- **Appui simple** : triangle isocèle `solideE`, pointe **en haut** au contact de la poutre, base reposant
  sur **deux petits cercles** (rouleaux) posés sur le sol hachuré ; légende « rotation + translation ».
- **Articulation** (appui simple fixe) : le même triangle, pointe en haut, **sans rouleaux**, base
  directement sur le sol hachuré ; légende « rotation seule ».
- **Encastrement** : un mur vertical hachuré (hachures à gauche du trait) duquel part la poutre
  horizontale ; légende « aucun degré de liberté ».
*Attention : le livre de 1re dessine l'articulation avec un cercle au sommet du triangle, la note tle-c
signale l'ambiguïté pointe haut / pointe bas. Retenir ici la version « triangle pointe en haut », cohérente
avec le tableau de la leçon `statique-pfs.md`.*

---

## Compétence `rdm-sollicitations`

### 10. `rdm-poutre` — définition d'une poutre (note 1re n° 26, p. 116)

Une poutre 3D en perspective (prisme droit à section rectangulaire, gris clair), légèrement courbée pour
montrer que la ligne moyenne peut être à grand rayon de courbure.
- à l'extrémité gauche, la **section droite $(S)$** dessinée hachurée, avec son **centre de surface $G$**
  (point noir étiqueté) ;
- la **ligne moyenne $(C)$** tracée en `solideE`, trait mixte, passant par $G$ et parcourant toute la
  poutre, avec l'étiquette « ligne moyenne (C) » ;
- une cote de longueur $L$ le long de la poutre et une cote transversale, pour illustrer
  « grande longueur devant les dimensions transversales » ;
- en encart, une seconde section (circulaire) pour montrer que la forme de $(S)$ est libre.

### 11. `rdm-sollicitations` — les cinq sollicitations simples (note 1re n° 3 p. 98 et n° 27 p. 117 ; tle-c n° 19 p. 281)

Tableau de **5 vignettes** (2 lignes : 3 + 2), en-têtes « Traction », « Compression », « Flexion »,
« Cisaillement », « Torsion ». Chaque vignette montre la **même poutre** rectangulaire horizontale
(`solideB`), avec sa ligne moyenne en pointillés, et le chargement en `solideA` :
- **Traction** : deux flèches axiales horizontales dirigées **vers l'extérieur**, notées $N$ ; sous la
  poutre, la même poutre dessinée **allongée** en trait fin ;
- **Compression** : deux flèches axiales dirigées **vers l'intérieur**, notées $N$ ; poutre **raccourcie**
  en trait fin ;
- **Flexion** : poutre sur deux appuis triangulaires `solideE` aux extrémités, une flèche verticale
  descendante notée $T$ au milieu, deux flèches montantes aux appuis (réactions) ; poutre **fléchie** en
  trait fin ;
- **Cisaillement** : deux flèches **transversales** opposées, très rapprochées (encadrant un plan de
  cisaillement marqué par un trait `solideD` en travers de la poutre) ;
- **Torsion** : deux flèches **circulaires** opposées autour de la ligne moyenne, aux deux extrémités ;
  une génératrice initialement droite est redessinée **en hélice** pour montrer la torsion.
*Attention : les extraits transcrits du livre ne traitent explicitement que traction, compression et flexion
(p. 117) ; le cisaillement apparaît p. 98 et la torsion n'y figure pas. Les deux dernières vignettes sont
donc un ajout, conforme au programme mais à vérifier avec le manuel avant diffusion.*

### 12. `rdm-contrainte` — la contrainte normale $\sigma = F/S$

Figure en trois temps, de gauche à droite, reliée par deux flèches fines.
1. une barre cylindrique horizontale `solideB` tirée par deux flèches `solideA` notées $F$, dirigées vers
   l'extérieur ;
2. la même barre avec une **coupure imaginaire** verticale (trait `solideD` en tirets) séparant deux
   tronçons, l'un des deux tronçons étant grisé (« tronçon supprimé ») ;
3. la **section coupée** vue de face (disque hachuré d'aire $S$), recouverte d'un **champ de petites
   flèches** identiques et régulièrement réparties, perpendiculaires à la section, avec l'étiquette
   « répartition uniforme » ; à côté, le centre $G$ et l'effort normal $N$.
Cartouche en bas : $\sigma = \dfrac{F}{S}$, avec $F$ en N, $S$ en mm², $\sigma$ en N/mm² = MPa, et le
rappel $S = \dfrac{\pi d^2}{4}$ pour une section circulaire.

---

## Compétence `rdm-hooke`

### 13. `rdm-essai-traction` — courbe contrainte-déformation (note 1re n° 28, p. 118 ; tle-c n° 20, p. 282)

**Figure clé de la compétence.** Repère orthonormé, origine notée $0$.
- **ordonnée** : « Contrainte » avec l'annotation $\sigma = \dfrac{F}{S}$ ;
- **abscisse** : « Déformation » avec l'annotation $\varepsilon = \dfrac{\Delta L}{L}$ ;
- courbe en trait épais `solideB` : (1) **segment rectiligne** croissant depuis $0$, annoté le long de la
  droite « $\sigma = E \cdot \varepsilon$ », jusqu'à un premier maximum local ; (2) petit **décrochement**
  (crochet vers le bas puis remontée) ; (3) remontée concave jusqu'à un **maximum** ; (4) décroissance
  jusqu'au point étiqueté « **Rupture** » (extrémité droite, croix ou éclair) ;
- pointillés horizontaux depuis l'axe des ordonnées vers la fin de la partie linéaire (**$R_e$**) et vers
  le maximum (**$R_r$**) ; pointillé vertical descendant du maximum vers l'abscisse ;
- sous l'axe des abscisses, deux **doubles flèches** `solideD` délimitant « Zone élastique » (courte, à
  gauche) et « Zone de déformation plastique » (longue, à droite) ;
- un petit triangle de pente sur la partie linéaire, avec l'étiquette $E$ (pente = module de Young).

### 14. `rdm-passerelle` — schéma de l'exercice guidé « passerelle sur tirant acier »

Schéma 2D d'ensemble, coté, servant d'énoncé à l'exercice guidé.
- un **pilier** maçonné à gauche (rectangle hachuré) portant une **articulation** en **$A$** (triangle
  `solideE`, pointe en haut) ;
- le **tablier** $AB$ horizontal `solideB` (trait épais), de $A$ à $B$, coté **$L = 4{,}00$ m** ; le milieu
  du tablier marqué par un point, coté **2,00 m** depuis $A$ ;
- au milieu, une flèche `solideA` verticale descendante étiquetée $\vec{P}$ (poids du tablier + piétons) ;
  une petite silhouette de piéton peut être ajoutée au-dessus ;
- en **$B$**, un **tirant vertical** (trait fin `solideA`) montant vers une **potence** ancrée en haut à
  droite (équerre hachurée) ; le tirant coté **$\ell = 2\,500$ mm** et **$d = 8$ mm** ;
- deux flèches de réaction verticales vers le haut : $\vec{F_A}$ en $A$ et $\vec{F_B}$ en $B$ (en trait
  plus fin, `solideF`, pour distinguer les inconnues) ;
- repère $(\vec{x}, \vec{y})$ en bas à gauche ($x$ vers la droite, $y$ vers le haut).

---

## Figures existantes réutilisables

Aucune n'est indispensable à cette unité, mais elles peuvent enrichir des questions ultérieures :

| Figure | Usage possible |
|---|---|
| `contact-encastrement` | illustrer l'encastrement comme liaison complète (0 ddl) |
| `contact-pivot`, `contact-appui-plan`, `contact-ponctuelle` | rapprocher appuis de structure et liaisons normalisées |
| `liaison-<id>-bout` / `liaison-<id>-face` | symboles normalisés, pour relier efforts transmissibles et appuis |
| `mecanisme-serre-joint-schema` | isolement d'une classe d'équivalence pour un calcul d'effort de serrage |
| `mecanisme-etau-dessin` | même chose sur l'étau (vis-écrou, effort presseur) |
| `mobilites` | rappel des 6 mobilités avant de parler d'appuis et de degrés de liberté |
