# Figures à dessiner — unité « Mathématiques : analyse et géométrie »

Figures référencées par `content/units/30-maths-1re.yaml` et `content/lessons/maths-*.md`.
Tant qu'elles ne sont pas produites, `tools/build_content.py` échoue avec « figure inconnue ».

**À produire :** un fichier `figures/tikz/<id>.tex` par figure (standalone, comme les figures
existantes), compilé par `make figures` en `figures/build/<id>.svg` ; le `stem` du SVG **est**
l'identifiant utilisé dans `{{fig:ID}}`.

Conventions communes (celles des figures existantes et du manuel, p. 97-109) :

- repère orthonormé, axes noirs fins terminés par une flèche, origine étiquetée $O$ ;
- cercle trigonométrique en **vert**, rayon 1, tracé moyen ;
- élément mis en évidence (rayon, vecteur, courbe étudiée) en **rouge** ;
- constructions et traits de rappel en **tirets gris** ;
- angles droits marqués par un petit carré ;
- toutes les étiquettes en LaTeX, lisibles à 320 px de large (l'appli est mobile d'abord) ;
- pas de couleur porteuse d'information seule (un tiret / un trait plein doit suffire).

| # | Identifiant | Utilisée dans |
|---|---|---|
| 1 | `maths-cercle-trigo` | leçon *cercle trigonométrique* + 1 QCM |
| 2 | `maths-cercle-angles` | leçon *cercle trigonométrique* |
| 3 | `maths-cos-sin-cercle` | leçon *cercle trigonométrique* + 1 QCM |
| 4 | `maths-angles-associes` | leçon *cercle trigonométrique* + 1 QCM |
| 5 | `maths-courbe-cos-sin` | leçon *fonctions trigonométriques* + 1 QCM |
| 6 | `maths-sinusoide` | leçon *fonctions trigonométriques* + 1 QCM + intro de l'exercice guidé |
| 7 | `maths-produit-scalaire-angle` | leçon *produit scalaire* + 1 QCM |
| 8 | `maths-projection-orthogonale` | leçon *produit scalaire* + 1 QCM |
| 9 | `maths-al-kashi` | leçon *produit scalaire* + 1 QCM |
| 10 | `maths-plan-complexe` | leçon *nombres complexes* + 1 QCM |

---

## 1. `maths-cercle-trigo` — enroulement de l'axe réel

*(d'après la figure de la p. 97)*

Repère orthonormé $(O,I,J)$, unité ≈ 1,6 cm. Cercle **vert** de centre $O$ et de rayon 1,
étiqueté $\mathcal{C}$ à gauche du cercle (vers l'angle $\pi$).
Points $I(1\,;0)$ et $J(0\,;1)$ marqués par un point plein et étiquetés ; $O$ étiqueté sous l'origine.

Droite verticale **rouge** (l'axe réel), tangente au cercle en $I$, allant de $y=-1{,}8$ à $y=+2{,}2$,
flèche vers le haut. Graduations rouges : petit trait et étiquette $0$ au niveau de $I$ ($y=0$),
$1$ à $y=1$, $2$ à $y=2$, $-1$ à $y=-1$.

Flèche courbe noire dans le premier quadrant, à l'extérieur du cercle (rayon ≈ 1,25),
orientée dans le **sens antihoraire**, accompagnée d'un signe $+$ et de la mention
« sens direct ». Une seconde flèche courbe, plus discrète, en tirets, dans le sens horaire,
étiquetée « sens indirect », dans le quatrième quadrant.

Point $M$ sur le cercle vers l'angle $1$ rad, avec le rayon $[OM]$ en trait fin et un arc rouge
de $I$ à $M$ épaissi, pour montrer que la longueur d'arc vaut la graduation $1$ de l'axe réel.

## 2. `maths-cercle-angles` — les angles remarquables en radians

*(d'après la figure de la p. 98)*

Cercle noir de centre $O$, rayon 1 ; axes fins horizontaux/verticaux.
Point $I$ à droite, étiqueté « $0$ rad » ; point $J$ en haut.

Rayons tracés depuis $O$ vers les points d'angle
$\dfrac{\pi}{6}$, $\dfrac{\pi}{4}$, $\dfrac{\pi}{3}$ (étiquettes à **droite**, à l'extérieur du cercle),
$\dfrac{\pi}{2}$ (étiquette au-dessus de $J$),
$\dfrac{2\pi}{3}$, $\dfrac{3\pi}{4}$, $\dfrac{5\pi}{6}$ (étiquettes à **gauche**),
et $\pi$ (rayon horizontal vers la gauche, étiquette « $\pi$ rad »).
Chaque étiquette porte la mention « rad ». Ajouter la mesure en degrés en gris sous chaque
étiquette ($30^{\circ}$, $45^{\circ}$, $60^{\circ}$, $90^{\circ}$, $120^{\circ}$, $135^{\circ}$,
$150^{\circ}$, $180^{\circ}$) : c'est le tableau de conversion de la leçon, sous forme visuelle.

Les rayons du premier quadrant en rose/rouge, ceux du deuxième en gris, comme dans le manuel.

## 3. `maths-cos-sin-cercle` — cosinus et sinus d'un réel

*(d'après la figure de la p. 98)*

Repère $(O,I,J)$, cercle **vert** $\mathcal{C}$ de rayon 1 (étiquette $\mathcal{C}$ à gauche).
Point $M$ sur le cercle dans le **premier quadrant**, vers $x\approx0{,}9$ rad
(coordonnées ≈ $(0{,}62\,;0{,}78)$), marqué et étiqueté $M$.

- rayon $[OM]$ en **rouge** ;
- petit arc rouge entre l'axe des abscisses et $[OM]$, étiqueté $x$ ;
- trait de rappel horizontal en tirets de $M$ vers l'axe des ordonnées, point marqué et
  étiqueté $\sin(x)$ ;
- trait de rappel vertical en tirets de $M$ vers l'axe des abscisses, point marqué et
  étiqueté $\cos(x)$ ;
- petit carré d'angle droit au pied de chaque trait de rappel.

Points $I$ et $J$ marqués et étiquetés, $O$ à l'origine.

## 4. `maths-angles-associes` — les symétries du cercle

*(figure complémentaire, non présente dans le livre ; illustre le tableau des angles associés p. 99)*

Repère $(O,I,J)$ et cercle vert de rayon 1. Quatre points sur le cercle, tous marqués et étiquetés,
pour un angle $x\approx\dfrac{\pi}{5}$ (≈ $36^{\circ}$) :

- $M$ associé à $x$, dans le premier quadrant, en **rouge** ;
- $M_1$ associé à $-x$, symétrique de $M$ par rapport à **l'axe des abscisses** ;
- $M_2$ associé à $\pi-x$, symétrique de $M$ par rapport à **l'axe des ordonnées** ;
- $M_3$ associé à $\pi+x$, symétrique de $M$ par rapport à **$O$**.

Étiqueter chaque point par la valeur de l'angle ($x$, $-x$, $\pi-x$, $\pi+x$) et tracer en
tirets gris les trois segments de symétrie ($MM_1$ vertical, $MM_2$ horizontal, $MM_3$ passant par $O$).
Indiquer sur l'axe des abscisses les deux abscisses $\cos(x)$ et $-\cos(x)$, sur l'axe des ordonnées
les deux ordonnées $\sin(x)$ et $-\sin(x)$, en tirets.

## 5. `maths-courbe-cos-sin` — courbes du cosinus et du sinus

*(synthèse des figures des p. 101 et 102)*

Un seul repère quadrillé (grille bleu très clair) : abscisses de $-4$ à $4$ (graduations entières,
plus les repères $-\pi$, $-\dfrac{\pi}{2}$, $\dfrac{\pi}{2}$, $\pi$ en petit sous l'axe),
ordonnées de $-2$ à $2$ (graduations $-1$, $1$).

- $y=\cos(x)$ en **rouge, trait plein**, étiquette $\mathcal{C}_{\cos}$ : maximum $1$ en $0$,
  zéros en $\pm\dfrac{\pi}{2}\approx\pm1{,}57$, minimums $-1$ en $\pm\pi\approx\pm3{,}14$ ;
- $y=\sin(x)$ en **bleu, tirets**, étiquette $\mathcal{C}_{\sin}$ : passe par l'origine,
  maximum $1$ en $\dfrac{\pi}{2}$, minimum $-1$ en $-\dfrac{\pi}{2}$, zéros en $0$ et $\pm\pi$.

Petite légende en haut à droite. Faire apparaître visuellement les deux symétries : axe des
ordonnées pour le cosinus (fonction paire), origine pour le sinus (fonction impaire) — par exemple
par deux repères discrets (un axe de symétrie en pointillé vertical, un point marqué en $O$).

## 6. `maths-sinusoide` — courbe de $t\mapsto A\cos(\omega t+\varphi)$

*(d'après la figure de la p. 103)*

Repère quadrillé vert clair. Abscisse : le temps $t$ ; ordonnée : la valeur du signal.
Courbe **rouge** sinusoïdale d'amplitude $A\approx1{,}6$ (ordonnées de $-2$ à $2$), décalée
horizontalement (phase à l'origine non nulle), sur environ 2,5 périodes ; étiquette $\mathcal{C}$
à gauche de la courbe.

- deux droites horizontales **vertes en tirets** aux ordonnées $A$ et $-A$, étiquetées $A$ et $-A$
  à gauche ;
- deux droites verticales **bleues en tirets** passant par deux **maximums consécutifs** ;
- entre elles, une double flèche bleue horizontale étiquetée $T=\dfrac{2\pi}{\omega}$ ;
- marquer l'ordonnée à l'origine par un point, étiqueté $u(0)=A\cos(\varphi)$.

## 7. `maths-produit-scalaire-angle` — définition géométrique

*(figure complémentaire, non présente dans le livre)*

Deux vecteurs de même origine $O$ : $\vec{u}$ (violet, vers la droite et légèrement vers le haut,
longueur ≈ 3) et $\vec{v}$ (bleu, plus court, longueur ≈ 2, incliné d'environ $50^{\circ}$
au-dessus de $\vec{u}$). Arc entre les deux vecteurs étiqueté $\theta$.
Étiquettes $\vec{u}$ et $\vec{v}$ au bout de chaque flèche, et les longueurs
$\left\|\vec{u}\right\|$ et $\left\|\vec{v}\right\|$ le long des vecteurs, en gris.

Sous la figure, l'égalité
$\vec{u}\cdot\vec{v}=\left\|\vec{u}\right\|\times\left\|\vec{v}\right\|\times\cos(\theta)$.

## 8. `maths-projection-orthogonale` — projection d'un vecteur sur une droite

*(d'après la figure de la p. 104)*

Droite noire $\mathcal{D}$ légèrement inclinée (montant vers la droite, pente ≈ 0,25),
étiquetée $\mathcal{D}$ à droite ; sur $\mathcal{D}$, un vecteur directeur $\vec{v}$ (bleu, court)
placé vers la gauche de la figure.

Au-dessus de $\mathcal{D}$ : deux points $A$ (à gauche, plus bas) et $B$ (à droite, plus haut),
reliés par un vecteur **violet** $\vec{u}=\overrightarrow{AB}$, étiquette $\vec{u}$ au-dessus.

Deux droites **en tirets gris**, parallèles entre elles et perpendiculaires à $\mathcal{D}$ :
l'une passe par $A$ et coupe $\mathcal{D}$ en $C$, l'autre passe par $B$ et coupe $\mathcal{D}$ en $D$.
Vecteur **rouge** $\overrightarrow{CD}$ porté par $\mathcal{D}$. Petits carrés d'angle droit (verts) en $C$ et en $D$.
Étiqueter la longueur $CD$ sous le segment.

## 9. `maths-al-kashi` — triangle quelconque

*(figure complémentaire, non présente dans le livre)*

Triangle $ABC$ nettement non rectangle (par exemple $A(0\,;0)$, $B(4\,;0)$, $C(1{,}2\,;2{,}4)$),
sommets marqués et étiquetés $A$, $B$, $C$.
Côtés étiquetés par leur longueur, selon la convention du manuel :
$a=BC$ (côté opposé à $A$), $b=AC$, $c=AB$.
Arc marquant l'angle $\hat{A}$ au sommet $A$, en rouge.

Sous la figure : $a^{2}=b^{2}+c^{2}-2bc\cos(\hat{A})$.

## 10. `maths-plan-complexe` — module et argument

*(figure complémentaire, non présente dans le livre ; cohérente avec le texte des p. 107-108)*

Repère orthonormé direct $(O,I,J)$ ; axe des abscisses étiqueté « axe réel », axe des ordonnées
« axe des imaginaires purs ».

- point $M$ de coordonnées $(a\,;b)$ avec $a\approx2$ et $b\approx1{,}5$, étiqueté $M(z)$,
  avec la mention $z=a+bi$ ;
- vecteur $\overrightarrow{OM}$ en **rouge** ; longueur $OM$ étiquetée $r=\left|z\right|$ ;
- traits de rappel en tirets gris vers $a$ sur l'axe réel et vers $b$ sur l'axe des imaginaires ;
- arc orienté entre $\overrightarrow{OI}$ et $\overrightarrow{OM}$, étiqueté $\theta=\arg(z)$ ;
- point $M'$ d'affixe $\overline{z}$, de coordonnées $(a\,;-b)$, étiqueté $M'(\overline{z})$,
  symétrique de $M$ par rapport à l'axe réel, avec le segment $MM'$ en tirets et l'arc $-\theta$
  en gris.
