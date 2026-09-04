# Figures à dessiner — unité « Mathématiques Tle STI2D »

Figures référencées par `content/units/35-maths-tle.yaml` et les six leçons
`content/lessons/maths-tle-*.md`. Tant qu'elles ne sont pas produites,
`tools/build_content.py` échoue avec « figure inconnue ».

**À produire :** un fichier `figures/tikz/<id>.tex` par figure (standalone, comme les figures
existantes), compilé par `make figures` en `figures/build/svg/<id>.svg` ; le `stem` du SVG **est**
l'identifiant utilisé dans `{{fig:ID}}`.

Conventions communes (celles des figures `maths-*` déjà produites) :

- `\documentclass[tikz,border=4pt]{standalone}`, `\usepackage{liaisons}` ;
- palette de `figures/tikz/liaisons.sty` : `solideA` **rouge** (courbe étudiée), `solideB` **bleu**
  (courbe secondaire, comparaison), `solideE` **vert** (élément construit : rectangle, asymptote,
  cercle trigonométrique) ; constructions et traits de rappel en **tirets gris** ;
- repère orthonormé quand la figure représente une aire ou un angle, axes fins noirs terminés par une
  flèche `-{Stealth[length=5pt]}`, origine étiquetée $O$ ; courbes en `line width=1.3pt` ;
- nombres en **écriture française** (virgule décimale, espace fine pour les milliers) ;
- largeur cible **≈ 8 cm**, lisible sur téléphone : pas plus de 8 étiquettes par figure ;
- pas de couleur porteuse d'information seule (un tiret / un trait plein doit suffire).

## Figures déjà existantes, réutilisées telles quelles

Aucune production n'est nécessaire pour ces deux-là, référencées par la compétence
« Complexes sous forme exponentielle » et sa leçon :

| Identifiant | Fichier existant | Réutilisée dans |
|---|---|---|
| `maths-plan-complexe` | `figures/tikz/maths-plan-complexe.tex` | leçon *complexes exp.* + 1 QCM (module et argument) |
| `maths-cercle-angles` | `figures/tikz/maths-cercle-angles.tex` | leçon *complexes exp.* + 1 QCM (angles remarquables) |

## Figures à produire

| # | Identifiant | Utilisée dans |
|---|---|---|
| 1 | `mathstle-exp-ln-courbes` | leçon *exp/ln* + 1 QCM (limites) |
| 2 | `mathstle-croissances-comparees` | leçon *dérivation* + 1 QCM (limite d'un quotient) |
| 3 | `mathstle-composee-arbre` | leçon *dérivation* + 1 QCM (dérivée d'une composée) |
| 4 | `mathstle-courbe-8x1expmx` | leçon *dérivation* + 1 exercice (maximum) |
| 5 | `mathstle-aire-sous-courbe` | leçon *intégrale* + 1 QCM (définition) |
| 6 | `mathstle-valeur-moyenne` | leçon *intégrale* + 1 QCM (valeur moyenne) |
| 7 | `mathstle-rectangles` | leçons *intégrale* et *Python* + 1 QCM |
| 8 | `mathstle-eqdiff-asymptote` | leçon *équations différentielles* + 1 QCM (limite) |
| 9 | `mathstle-plan-complexe-cercles` | leçon *complexes exp.* + 1 QCM (lecture d'affixe) |
| 10 | `mathstle-euler` | leçon *Python* + 1 QCM + explication de l'exercice guidé |

---

## 1. `mathstle-exp-ln-courbes` — exponentielle et logarithme, symétriques

Repère orthonormé, unité **1 cm**, abscisses de $-3$ à $3{,}2$, ordonnées de $-3$ à $3{,}2$.
Graduations entières marquées $-2$, $-1$, $1$, $2$, $3$ sur chaque axe.

- $y=\mathrm{e}^{x}$ en **`solideA`**, trait plein, tracée pour $x\in\left[-3\,;1{,}15\right]$
  (`samples=60, smooth`), étiquette $y=\mathrm{e}^{x}$ posée en haut à droite de la courbe ;
- $y=\ln(x)$ en **`solideB`**, trait plein, tracée pour $x\in\left[0{,}05\,;3{,}2\right]$,
  étiquette $y=\ln(x)$ à droite de la courbe ;
- droite $y=x$ en **tirets gris fins**, de $(-3\,;-3)$ à $(3\,;3)$, étiquetée $y=x$ près de
  l'extrémité haute ; c'est l'axe de symétrie entre les deux courbes ;
- points marqués et étiquetés : $(0\,;1)$ sur la courbe rouge, $(1\,;0)$ sur la bleue.

Deux mentions d'asymptote : le long de l'axe des abscisses à gauche, en gris,
« asymptote horizontale de $\exp$ » ; le long de l'axe des ordonnées vers le bas, en gris,
« asymptote verticale de $\ln$ ». Deux petites flèches en tirets gris relient un point de la courbe
rouge à son symétrique sur la bleue, par exemple $(1\,;\mathrm{e})\leftrightarrow(\mathrm{e}\,;1)$.

## 2. `mathstle-croissances-comparees` — l'exponentielle l'emporte

Repère **non orthonormé** : abscisses de $0$ à $5$ (1,4 cm par unité), ordonnées de $0$ à $160$
(1 cm pour $25$). Graduations $1$ à $5$ en abscisse, $50$, $100$, $150$ en ordonnée.

- $y=x^{3}$ en **`solideB`**, trait plein (`domain=0:5, samples=60`), étiquette $y=x^{3}$ ;
- $y=\mathrm{e}^{x}$ en **`solideA`**, trait plein (`domain=0:5, samples=80`), étiquette
  $y=\mathrm{e}^{x}$ ;
- les deux courbes se coupent en $x\approx1{,}86$ et $x\approx4{,}54$ : marquer **le second** point
  d'intersection par un point noir et une droite verticale en tirets gris jusqu'à l'axe des
  abscisses, avec l'étiquette $x\approx4{,}5$ ;
- à droite de cette verticale, une accolade horizontale grise sous l'axe, légendée
  « au-delà, $\mathrm{e}^{x}$ dépasse $x^{3}$ **définitivement** » ;
- encadré en bas à droite, sur deux lignes :
  $\lim\limits_{x\to+\infty}\dfrac{\mathrm{e}^{x}}{x^{n}}=+\infty$ et
  $\lim\limits_{x\to+\infty}x^{n}\mathrm{e}^{-x}=0$.

## 3. `mathstle-composee-arbre` — dériver une composée

Pas de repère : un **schéma en trois étages**, orienté de gauche à droite, largeur ≈ 8 cm.

Trois cadres arrondis alignés horizontalement, espacés de 2 cm :
$x$ (cadre gris clair) → $u(x)$ (cadre **`solideB`**) → $v\left(u(x)\right)$ (cadre **`solideA`**).
Les deux flèches `-{Stealth}` qui les relient sont étiquetées **au-dessus** par $u$ puis $v$.

Sous les mêmes flèches, en **`solideE`** et dans le sens **inverse** (flèches courbes revenant de
droite à gauche, en tirets), les deux facteurs de la dérivée : sous la flèche de droite
$v'\left(u(x)\right)$, sous celle de gauche $u'(x)$.

Sous le schéma, encadrée, la formule
$\left(v\circ u\right)'(x)=u'(x)\times v'\left(u(x)\right)$, avec la mention en gris
« on dérive de l'extérieur vers l'intérieur, sans oublier $u'$ ».

À droite, une colonne de trois exemples en petit, alignés :
$\mathrm{e}^{u}\rightarrow u'\mathrm{e}^{u}$ ; $\ln(u)\rightarrow\dfrac{u'}{u}$ ;
$u^{n}\rightarrow n\,u'u^{n-1}$.

## 4. `mathstle-courbe-8x1expmx` — maximum de $f(x)=(8x+1)\mathrm{e}^{-x}$

Repère, abscisses de $0$ à $5$ (1,5 cm par unité), ordonnées de $0$ à $4$ (1 cm par unité).
Graduations entières sur les deux axes.

Courbe **`solideA`** de $f(x)=(8x+1)\mathrm{e}^{-x}$ sur $\left[0\,;5\right]$
(`samples=80, smooth`). Repères de tracé : $f(0)=1$ ; $f(0{,}875)\approx3{,}33$ ;
$f(2)\approx2{,}30$ ; $f(3)\approx1{,}24$ ; $f(4)\approx0{,}60$ ; $f(5)\approx0{,}28$.

- maximum marqué par un point noir, avec traits de rappel en **tirets gris** vers les deux axes ;
  étiquette $x=\dfrac{7}{8}=0{,}875$ sous l'axe des abscisses, étiquette $3{,}33$ à gauche de l'axe
  des ordonnées ;
- à côté du maximum, en `solideE`, la mention « $f'$ s'annule en changeant de signe » ;
- l'axe des abscisses est prolongé en tirets gris jusqu'à $x=5{,}5$, avec l'étiquette
  « asymptote horizontale $y=0$ » ;
- étiquette de la courbe $\mathcal{C}_{f}$ posée vers $x=1{,}6$, au-dessus de la courbe.

## 5. `mathstle-aire-sous-courbe` — l'intégrale est une aire

Repère orthonormé, unité **1 cm**, abscisses de $0$ à $5{,}5$, ordonnées de $0$ à $6$.

Courbe **`solideA`** de $f(x)=0{,}25x^{2}+1$ sur $\left[0\,;5\right]$ ($f(1)=1{,}25$, $f(4)=5$),
étiquetée $\mathcal{C}_{f}$ au-dessus de son extrémité droite.

- domaine **hachuré** (hachures fines à $45^{\circ}$, gris, `pattern=north east lines`) entre la
  courbe, l'axe des abscisses et les deux verticales $x=1$ et $x=4$ ;
- les deux verticales en trait plein fin, avec les étiquettes $a=1$ et $b=4$ sous l'axe ;
- au centre du domaine, l'étiquette $\displaystyle\int_{a}^{b}f(x)\,\mathrm{d}x$ ;
- en haut à droite, hors du domaine, un **petit carré `solideE`** de côté 1 cm, légendé
  « 1 u.a. » : c'est l'unité d'aire, à faire apparaître explicitement.

## 6. `mathstle-valeur-moyenne` — le rectangle de même aire

**Même repère et même courbe** que la figure 5 ($f(x)=0{,}25x^{2}+1$, domaine entre $a=1$ et $b=4$),
pour que les deux figures se lisent en série.

- domaine sous la courbe hachuré en gris, comme précédemment ;
- **rectangle `solideE`** en trait plein, de $x=1$ à $x=4$ et de hauteur $\mu=2{,}75$, rempli à
  opacité 0,15 ; sa hauteur est marquée par une droite horizontale `solideE` d'équation $y=\mu$
  prolongée en tirets jusqu'à l'axe des ordonnées, étiquetée $\mu$ ;
- double flèche horizontale grise sous le rectangle, étiquetée $b-a=3$ ;
- la courbe coupe le segment horizontal $y=\mu$ à l'intérieur du rectangle (vers $x\approx2{,}6$) :
  marquer ce point d'un petit rond, sans étiquette ;
- sous la figure, l'égalité $\mu\times(b-a)=\displaystyle\int_{a}^{b}f(x)\,\mathrm{d}x$, avec la
  mention en gris « même aire, mais un rectangle ».

## 7. `mathstle-rectangles` — la méthode des rectangles

**Deux panneaux côte à côte**, séparés par un filet vertical fin, chacun ≈ 3,8 cm de large.
Même fonction et mêmes échelles dans les deux : $f(x)=\mathrm{e}^{-x}$ sur $\left[0\,;1\right]$,
abscisses 3 cm pour l'unité, ordonnées 2,5 cm pour l'unité, graduations $0$, $0{,}5$, $1$.

- courbe **`solideA`** dans les deux panneaux, étiquetée $\mathcal{C}_{f}$ dans le panneau de gauche ;
- rectangles **à gauche** (hauteur prise à la borne **gauche** de chaque sous-intervalle), contour
  `solideB`, remplissage bleu à opacité 0,12 ;
- panneau de gauche : $n=4$, largeur $\Delta x=0{,}25$, hauteurs $1$ ; $0{,}779$ ; $0{,}607$ ;
  $0{,}472$ ; titre au-dessus « $n=4$ : $0{,}714$ » ;
- panneau de droite : $n=10$, largeur $\Delta x=0{,}1$ ; titre au-dessus « $n=10$ : $0{,}664$ » ;
- sous les deux panneaux, une seule ligne centrée :
  « valeur exacte $\displaystyle\int_{0}^{1}\mathrm{e}^{-x}\,\mathrm{d}x=1-\mathrm{e}^{-1}\approx0{,}632$ » ;
- dans le panneau de gauche, une petite double flèche horizontale sous le premier rectangle,
  étiquetée $\Delta x$.

Les rectangles dépassent la courbe : la surestimation doit être **visible**, c'est l'objet du QCM.

## 8. `mathstle-eqdiff-asymptote` — solutions de $y'=ay+b$ avec $a<0$

Repère, abscisses $t$ de $0$ à $1{,}4$ (5 cm pour l'unité), ordonnées de $0$ à $110$
(1 cm pour $20$). Graduations $20$, $50$, $100$ en ordonnée ; $0{,}5$ et $1$ en abscisse.

Trois solutions de $(E)\ y'=-4y+80$, c'est-à-dire $f(t)=k\,\mathrm{e}^{-4t}+20$ :

- $k=80$ (donc $f(0)=100$) en **`solideA`**, décroissante — repères : $f(0{,}25)\approx49{,}4$,
  $f(0{,}5)\approx30{,}8$, $f(1)\approx21{,}5$ ;
- $k=-20$ (donc $f(0)=0$) en **`solideB`**, croissante — repères : $f(0{,}25)\approx12{,}6$,
  $f(0{,}5)\approx17{,}3$, $f(1)\approx19{,}6$ ;
- $k=0$ : la droite horizontale $y=20$, en **`solideE`**, trait plein, prolongée en **tirets** au-delà
  de $t=1{,}2$, étiquetée à droite $y=-\dfrac{b}{a}=20$ et, en dessous en gris,
  « solution constante = régime permanent ».

Les deux conditions initiales $(0\,;100)$ et $(0\,;0)$ sont marquées par un point noir étiqueté
$f(0)$. Encadré en haut à droite, sur deux lignes : $f(t)=k\,\mathrm{e}^{at}-\dfrac{b}{a}$ et
« si $a<0$ : $\lim\limits_{t\to+\infty}f(t)=-\dfrac{b}{a}$ ».

## 9. `mathstle-plan-complexe-cercles` — lire une affixe

Repère orthonormé direct, unité **0,7 cm**, abscisses de $-5{,}5$ à $5{,}5$, ordonnées idem ; axe
horizontal étiqueté « axe réel », axe vertical « axe des imaginaires purs ».

- **cinq cercles concentriques** de centre $O$ et de rayons $1$, $2$, $3$, $4$, $5$, en gris fin ;
  le rayon de chacun est indiqué en petit sur l'axe des abscisses positif ($1$ à $5$) ;
- point $M$ de coordonnées $\left(\dfrac{5\sqrt{2}}{2}\,;-\dfrac{5\sqrt{2}}{2}\right)\approx(3{,}54\,;-3{,}54)$,
  c'est-à-dire sur le **cinquième** cercle, dans le **quatrième quadrant** ; point plein noir,
  étiqueté $M$ au-dessus à droite ;
- segment $\left[OM\right]$ en **`solideA`**, épais ;
- arc orienté **`solideE`** de l'axe des abscisses positif vers $\left[OM\right]$, de rayon 1,2 cm,
  sans étiquette de valeur (c'est à l'élève de la trouver) ;
- traits de rappel en tirets gris de $M$ vers les deux axes, sans valeurs chiffrées.

**Important :** ne pas écrire l'affixe sur la figure — le QCM demande de la lire.

## 10. `mathstle-euler` — la ligne brisée d'Euler

Repère, abscisses de $0$ à $1{,}15$ (5,5 cm pour l'unité), ordonnées de $0$ à $3$ (1,7 cm pour
l'unité). Graduations $0{,}25$, $0{,}5$, $0{,}75$, $1$ en abscisse ; $1$, $2$, $3$ en ordonnée.

- courbe exacte $y=\mathrm{e}^{x}$ en **`solideA`**, trait plein, sur $\left[0\,;1{,}1\right]$ ;
  étiquette $y=\mathrm{e}^{x}$ à droite ;
- **ligne brisée `solideB`** d'Euler pour $h=0{,}25$, passant par les points
  $(0\,;1)$, $(0{,}25\,;1{,}25)$, $(0{,}5\,;1{,}5625)$, $(0{,}75\,;1{,}9531)$,
  $(1\,;2{,}4414)$ ; chaque sommet marqué par un petit carré bleu ;
- le **premier segment** est prolongé en tirets gris au-delà de $x=0{,}25$ pour montrer qu'il s'agit
  de la **tangente** en $(0\,;1)$ ; étiquette grise « tangente » ;
- verticales en tirets gris aux abscisses $0{,}25$, $0{,}5$, $0{,}75$, $1$ ; sous l'axe, une double
  flèche entre $0$ et $0{,}25$ étiquetée $h$ ;
- en $x=1$, double flèche verticale **`solideE`** entre $2{,}441$ et $\mathrm{e}\approx2{,}718$,
  étiquetée « écart $\approx0{,}28$ » ; les deux ordonnées $2{,}44$ et $2{,}72$ sont écrites à droite
  de l'axe des ordonnées, en petit.

La ligne brisée doit rester **sous** la courbe sur tout l'intervalle : c'est ce que la leçon et le
QCM font observer (convexité de l'exponentielle).
