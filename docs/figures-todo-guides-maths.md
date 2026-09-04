# Figures à dessiner — exercices guidés de l'unité « Mathématiques : analyse et géométrie »

Figures référencées par les **exercices complets** (`type: guided`) ajoutés dans
`content/units/30-maths-1re.yaml`. Complément de `docs/figures-todo-maths.md` (figures 1 à 10),
dont les conventions restent valables. Tant qu'elles ne sont pas produites,
`tools/build_content.py` échoue avec « figure inconnue ».

**À produire :** un fichier `figures/tikz/<id>.tex` par figure (standalone, `\documentclass[tikz,border=4pt]{standalone}`
+ `\usepackage{liaisons}`, comme `figures/tikz/maths-sinusoide.tex`), compilé par `make figures`
en `figures/build/<id>.svg` ; le `stem` du SVG **est** l'identifiant utilisé dans `{{fig:ID}}`.

Conventions communes (identiques à `docs/figures-todo-maths.md`) :

- largeur finale visée ≈ **8 cm** (l'appli est mobile d'abord, lisible à 320 px) ;
- élément étudié (courbe, vecteur principal, point solution) en **rouge** : style `solideA` ;
- second élément ou grandeur mesurée en **bleu** : style `solideB` ;
- quadrillage, traits de rappel et constructions en **tirets gris/vert clair** : `solideE!25` à `solideE` ;
- axes noirs fins terminés par une flèche (`-{Stealth[length=5pt]}`), origine étiquetée $O$ ;
- angles droits marqués par un petit carré ; toutes les étiquettes en LaTeX, en français ;
- **ne jamais écrire sur la figure la valeur demandée par une étape** (angle, longueur, module) :
  les figures ci-dessous portent des noms de points ou des symboles, pas les résultats.

| # | Identifiant | Utilisée dans |
|---|---|---|
| 1 | `guide-maths-aire-debit` | guidé *Le remplissage d'un réservoir* (compétence Primitives) |
| 2 | `guide-maths-came-cercle` | guidé *La came circulaire* (compétence Cercle trigonométrique) |
| 3 | `guide-maths-travail-rampe` | guidé *Le treuil d'une rampe de chargement* (compétence Produit scalaire) |
| 4 | `guide-maths-triangle-repere` | guidé *Une ferme de charpente* (compétence Produit scalaire) |
| 5 | `guide-maths-impedance-complexe` | guidé *L'impédance d'un circuit RL* (compétence Nombres complexes) |

Les autres exercices guidés réutilisent les figures existantes : `maths-sinusoide`
(guidé *Le signal d'un capteur de vibration*, comme le guidé *Une tension sinusoïdale du réseau*).
Le guidé *Le freinage d'un chariot automatisé* n'utilise pas de figure.

---

## 1. `guide-maths-aire-debit` — aire sous la courbe d'un débit

Courbe de $q(t)=0{,}5\,t^{2}-4t+10$ sur $[0\,;6]$, l'aire sous la courbe représentant le volume écoulé.

Échelle suggérée : `x=1.05cm`, `y=0.55cm` (largeur ≈ 7,5 cm, hauteur ≈ 6,5 cm).

- quadrillage léger `solideE!25`, pas $1$ en $t$ et $2$ en $q$, de $(0\,;0)$ à $(6{,}5\,;11)$ ;
- axes : abscisses de $-0{,}2$ à $7$, étiquette $t$ (s) à droite ; ordonnées de $-0{,}5$ à $11{,}5$,
  étiquette $q$ ($\mathrm{L}\cdot\mathrm{s}^{-1}$) en haut ; graduations $1$ à $6$ sur l'axe des abscisses,
  $2$, $4$, $6$, $8$, $10$ sur l'axe des ordonnées ; origine étiquetée $O$ ;
- **domaine hachuré** entre la courbe, l'axe des abscisses et les droites $t=0$ et $t=6$ :
  remplissage `solideA!12` + hachures `pattern=north east lines`, trait `solideA!50` ;
- **courbe** `solideA`, épaisseur 1,4 pt, tracée pour $t\in[0\,;6]$
  (`plot[domain=0:6, samples=100, smooth] (\x,{0.5*\x*\x-4*\x+10})`) ;
  points remarquables : $q(0)=10$, $q(1)=6{,}5$, $q(2)=4$, $q(3)=2{,}5$, $q(4)=2$, $q(5)=2{,}5$, $q(6)=4$ ;
  étiquette $\mathcal{C}_q$ près de l'extrémité droite de la courbe ;
- deux droites verticales en tirets `solideB` en $t=0$ et $t=6$, montant jusqu'à la courbe ;
- point du minimum marqué (petit disque plein `solideA` en $(4\,;2)$) **sans étiquette de valeur** ;
- au centre du domaine hachuré, en gris, le texte « aire = volume écoulé ».

## 2. `guide-maths-came-cercle` — cercle trigonométrique et équations

Cercle trigonométrique portant les intersections utilisées par les équations
$\cos(\theta)=-\dfrac{1}{2}$ et $\sin(\theta)=\dfrac{\sqrt{2}}{2}$.

Unité : $1$ = 2,6 cm (cercle de diamètre ≈ 5,2 cm, largeur totale ≈ 8 cm avec les étiquettes).

- repère $(O,I,J)$, axes fins fléchés de $-1{,}35$ à $1{,}35$ ; points $I(1\,;0)$ et $J(0\,;1)$
  marqués et étiquetés à l'intérieur du cercle ;
- cercle de centre $O$ et de rayon $1$ en **vert** (`solideE`), comme dans `maths-cercle-trigo` ;
  flèche courbe extérieure dans le premier quadrant indiquant le **sens direct** ;
- droite verticale en tirets gris d'équation $x=-\dfrac{1}{2}$, de $y=-1{,}25$ à $y=1{,}25$,
  étiquetée $x=-\dfrac{1}{2}$ en bas ;
- ses deux intersections avec le cercle, en **rouge** (`solideA`) : $M_1\left(-\dfrac{1}{2}\,;\dfrac{\sqrt{3}}{2}\right)$
  soit $(-0{,}5\,;0{,}866)$, et $M_2\left(-\dfrac{1}{2}\,;-\dfrac{\sqrt{3}}{2}\right)$ soit $(-0{,}5\,;-0{,}866)$ ;
  rayons $[OM_1]$ et $[OM_2]$ tracés en `solideA` ; étiquettes $M_1$ et $M_2$ à l'extérieur du cercle
  (**pas** les valeurs d'angles, qui sont les réponses attendues) ;
- droite horizontale en tirets gris d'équation $y=\dfrac{\sqrt{2}}{2}$, de $x=-1{,}25$ à $x=1{,}25$,
  étiquetée $y=\dfrac{\sqrt{2}}{2}$ à droite ;
- ses deux intersections, en **bleu** (`solideB`) : $N_1(0{,}707\,;0{,}707)$ et $N_2(-0{,}707\,;0{,}707)$,
  rayons $[ON_1]$ et $[ON_2]$ en `solideB`, étiquettes $N_1$ et $N_2$ ;
- petits arcs orientés depuis $[OI]$ vers $[OM_1]$ et vers $[ON_1]$, étiquetés $\theta$ (sans valeur).

## 3. `guide-maths-travail-rampe` — travail des forces sur un plan incliné

Chariot tiré vers le haut d'une rampe inclinée de $30^{\circ}$.

Échelle suggérée : `x=y=1.1cm` (largeur ≈ 7,5 cm).

- triangle du plan incliné, sommets $A(0\,;0)$, $H(5{,}196\,;0)$ et $B(5{,}196\,;3)$
  ($B=A+6\times(\cos 30^{\circ}\,;\sin 30^{\circ})$), rempli `solideE!12`, contours fins ;
  la **rampe** est l'hypoténuse $[AB]$, tracée en trait noir épais ; le sol $[AH]$ en trait fin ;
- arc d'angle en $A$ (rayon 0,9) entre l'horizontale et la rampe, étiqueté $30^{\circ}$ ;
- petit rectangle (le chariot, ≈ $0{,}9\times0{,}5$) incliné de $30^{\circ}$, centré en $C(2{,}6\,;1{,}5)$,
  rempli en gris clair ;
- **vecteur déplacement** $\overrightarrow{AB}$ en **bleu** (`solideB`), flèche de $A$ à $B$ tracée
  légèrement en dessous de la rampe (décalage perpendiculaire de $-0{,}35$), étiqueté
  $\overrightarrow{AB}$ et, en petit, $AB=12$ m ;
- **vecteur poids** $\vec{P}$ en **rouge** (`solideA`), origine $C$, vertical vers le bas, longueur 2,
  étiqueté $\vec{P}$ sous la pointe ;
- **vecteur réaction normale** $\vec{R}$ en gris foncé, origine $C$, direction $(-\sin 30^{\circ}\,;\cos 30^{\circ})=(-0{,}5\,;0{,}866)$,
  longueur 1,5, étiqueté $\vec{R}$, avec un petit carré d'angle droit entre $\vec{R}$ et la rampe ;
- **vecteur traction** $\vec{F}$ en vert (`solideE`), origine $C$, dirigé vers le haut de la pente
  (direction $(0{,}866\,;0{,}5)$), longueur 1,5, étiqueté $\vec{F}$ ;
- arc gris centré en $C$ entre $\vec{P}$ et la direction de $\overrightarrow{AB}$, étiqueté $\theta$
  (**sans** donner la valeur $\frac{2\pi}{3}$) ;
- mentions « $m=200$ kg » près du chariot et « $30^{\circ}$ » à l'angle en $A$.

## 4. `guide-maths-triangle-repere` — triangle dans un repère orthonormé

Triangle $ABC$ de sommets $A(0\,;0)$, $B(4\,;0)$, $C(1\,;3)$, unité : le mètre.

Échelle suggérée : `x=y=1.3cm` (largeur ≈ 7 cm).

- quadrillage `solideE!25` de pas $1$, de $(-0{,}5\,;-0{,}5)$ à $(5\,;3{,}5)$ ;
- axes fins fléchés, graduations entières $1$ à $4$ (abscisses) et $1$ à $3$ (ordonnées),
  origine étiquetée $O$, mention « unité : 1 m » en petit sous l'axe des abscisses ;
- triangle $ABC$ rempli `solideA!8`, contour noir fin ; sommets marqués par des disques pleins
  et étiquetés $A(0\,;0)$ (en dessous à gauche), $B(4\,;0)$ (en dessous à droite), $C(1\,;3)$ (au-dessus) ;
- **vecteur** $\overrightarrow{AB}$ en **rouge** (`solideA`), de $A$ à $B$, étiqueté $\overrightarrow{AB}$
  sous le segment ;
- **vecteur** $\overrightarrow{AC}$ en **bleu** (`solideB`), de $A$ à $C$, étiqueté $\overrightarrow{AC}$
  à gauche du segment ;
- arc rouge en $A$ (rayon 0,6) entre les deux vecteurs, étiqueté $\widehat{BAC}$ (**sans** valeur) ;
- côté $[BC]$ en trait noir, étiqueté « $BC=?$ » au milieu du segment, côté extérieur.

## 5. `guide-maths-impedance-complexe` — impédance dans le plan complexe

Point d'affixe $Z=100+100\sqrt{3}\,i$ (en ohms) dans le plan complexe.

Échelle : $1$ unité $=50$ $\Omega$, `x=y=0.85cm` ; $Z$ est donc au point $(2\,;3{,}46)$ du dessin
(largeur ≈ 7 cm, hauteur ≈ 4 cm).

- repère orthonormé direct, axes fins fléchés : axe horizontal de $-0{,}4$ à $3{,}2$, étiqueté
  « axe réel — résistance $R$ ($\Omega$) » ; axe vertical de $-0{,}4$ à $4{,}2$, étiqueté
  « axe imaginaire — réactance $X$ ($\Omega$) » ; origine étiquetée $O$ ;
- graduations tous les $50$ $\Omega$ (soit toutes les unités de dessin) : $50$, $100$, $150$ sur
  l'axe réel ; $50$, $100$, $150$ sur l'axe imaginaire ;
- point $M$ d'affixe $Z$ en $(2\,;3{,}46)$, marqué par un disque plein et étiqueté $M(Z)$,
  avec la mention $Z=100+100\sqrt{3}\,i$ à droite du point ;
- **vecteur** $\overrightarrow{OM}$ en **rouge** (`solideA`), épaisseur 1,2 pt ; le long du vecteur,
  en gris, l'étiquette $\left|Z\right|$ (**sans** la valeur $200$) ;
- traits de rappel en tirets gris : horizontal de $M$ vers l'axe imaginaire (point marqué,
  étiquette $X=100\sqrt{3}$) et vertical de $M$ vers l'axe réel (point marqué, étiquette $R=100$) ;
  petit carré d'angle droit au pied du trait vertical ;
- arc orienté en **bleu** (`solideB`), de rayon 0,8, entre le demi-axe réel positif et
  $\overrightarrow{OM}$, étiqueté $\varphi=\arg(Z)$ (**sans** la valeur $\frac{\pi}{3}$) ;
- en bas à droite, en petit et en gris : « $Z=R+X\,i$ ».
