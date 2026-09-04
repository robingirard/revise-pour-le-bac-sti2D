# Figures à dessiner — unité « Mathématiques Tle : enseignement commun »

Figures référencées par `content/units/36-maths-tle-tronc-commun.yaml` et les six leçons
`content/lessons/maths-tle-commun-*.md`. Tant qu'elles ne sont pas produites,
`tools/build_content.py` échoue avec « figure inconnue ».

**À produire :** un fichier `figures/tikz/<id>.tex` par figure (standalone, comme les figures
existantes), compilé par `make figures` en `figures/build/svg/<id>.svg` ; le `stem` du SVG **est**
l'identifiant utilisé dans `{{fig:ID}}`.

Préfixe **`mathstc-`** (tronc commun), distinct de `mathstle-` (spécialité) et de `maths-`
(première) pour éviter toute collision.

Conventions communes (celles des figures `maths-*` et `mathstle-*` déjà produites) :

- `\documentclass[tikz,border=4pt]{standalone}`, `\usepackage{liaisons}` ;
- palette de `figures/tikz/liaisons.sty` : `solideA` **rouge** (courbe ou série principale),
  `solideB` **bleu** (courbe ou série de comparaison), `solideE` **vert** (élément construit :
  tangente, droite d'ajustement, repère de lecture) ; constructions et traits de rappel en
  **tirets gris** ;
- axes fins noirs terminés par une flèche `-{Stealth[length=5pt]}`, origine étiquetée $O$ ;
  courbes en `line width=1.3pt` ;
- nombres en **écriture française** (virgule décimale, espace fine pour les milliers) ;
- largeur cible **≈ 8 cm**, lisible sur téléphone : pas plus de 8 étiquettes par figure ;
- pas de couleur porteuse d'information seule (un tiret / un trait plein doit suffire).

## Figures existantes, réutilisées telles quelles

La liste de `figures/tikz/` a été vérifiée : les figures `maths-*` couvrent la trigonométrie, le
produit scalaire et le plan complexe, les figures `mathstle-*` l'intégrale, les équations
différentielles et les complexes — rien qui corresponde au tronc commun, à une exception près.

| Identifiant | Fichier existant | Réutilisée dans |
|---|---|---|
| `mathstle-exp-ln-courbes` | `figures/tikz/mathstle-exp-ln-courbes.tex` | leçon *exponentielles de base $a$ et logarithme décimal*, section finale « Pont avec la spécialité » (symétrie exponentielle / logarithme par rapport à $y=x$, ici en base $\mathrm{e}$) |

## Figures à produire

| # | Identifiant | Utilisée dans |
|---|---|---|
| 1 | `mathstc-signe-parabole` | leçon *automatismes* + 2 QCM (signe, résolution graphique) |
| 2 | `mathstc-lecture-droite` | leçon *automatismes* + 1 QCM (lecture d'un seuil) |
| 3 | `mathstc-suite-batons` | leçon *suites* + 1 QCM (terme d'une suite géométrique) |
| 4 | `mathstc-suites-lin-vs-geo` | leçon *suites* + 1 exercice (linéaire contre exponentiel) |
| 5 | `mathstc-exp-base-a` | leçon *exp/log* + 1 QCM (définition de $x\mapsto a^{x}$) |
| 6 | `mathstc-log-decimal` | leçon *exp/log* + 1 QCM (définition de $\log$) |
| 7 | `mathstc-semilog` | leçon *exp/log* + 1 QCM (repère semi-logarithmique) |
| 8 | `mathstc-fonction-inverse` | leçon *fonction inverse* + 1 QCM (ensemble de définition, tangente) |
| 9 | `mathstc-cout-moyen` | leçon *fonction inverse* + 1 exercice (minimum du coût moyen) |
| 10 | `mathstc-nuage-ajustement` | leçon *statistiques* + 1 QCM (nuage de points, résidus) |
| 11 | `mathstc-changement-variable` | leçon *statistiques* + 1 exercice d'ordre (changement de variable) |
| 12 | `mathstc-arbre-probas` | leçon *probabilités* + 1 QCM (notation $P_{A}(B)$) |
| 13 | `mathstc-binomiale-batons` | leçon *probabilités* + 1 QCM (valeur la plus probable) |

---

## 1. `mathstc-signe-parabole` — signe de $-2(x-1)(x-3)$ par image mentale

Repère non orthonormé : abscisses de $-0{,}3$ à $4{,}3$ (**1,5 cm** par unité), ordonnées de $-6$ à
$3$ (**0,55 cm** par unité). Graduations $1$, $2$, $3$, $4$ en abscisse ; $-6$, $-4$, $-2$, $2$ en
ordonnée.

- parabole **`solideA`**, trait plein, de $f(x)=-2(x-1)(x-3)$ tracée pour
  $x\in\left[0{,}1\,;3{,}9\right]$ (`samples=60, smooth`). Repères de tracé : $f(0{,}1)=-5{,}22$ ;
  $f(1)=0$ ; $f(2)=2$ (sommet) ; $f(3)=0$ ; $f(3{,}9)=-5{,}22$ ;
- les deux racines $1$ et $3$ marquées par un point noir sur l'axe des abscisses, étiquetées
  $1$ et $3$ **sous** l'axe ;
- l'arc situé **au-dessus** de l'axe (entre $x=1$ et $x=3$) surligné en `solideA` épais, l'arc situé
  en dessous laissé en trait normal ;
- sous l'axe des abscisses, deux accolades grises : de $0{,}1$ à $1$ et de $3$ à $3{,}9$, légendées
  « $f(x)<0$ » ; entre $1$ et $3$, une accolade **au-dessus** de l'axe légendée « $f(x)>0$ » ;
- en haut à droite, en gris : « le coefficient $-2$ tourne la parabole vers le bas ».

Ne pas dessiner de tableau de signes : la figure doit rester une **image mentale**.

## 2. `mathstc-lecture-droite` — lire un seuil sur une droite

Repère, abscisses $n$ (nombre de pièces) de $0$ à $60$ (**1 cm pour 10 pièces**), ordonnées $C$
(coût en euros) de $0$ à $360$ (**1 cm pour 50 €**). Graduations $10$, $20$, $30$, $40$, $50$, $60$
en abscisse ; $50$, $100$, $150$, $200$, $250$, $300$, $350$ en ordonnée. Axes légendés
« nombre de pièces » et « coût (€) ».

- droite **`solideA`**, trait plein, d'équation $C=5n+60$, tracée de $(0\,;60)$ à $(60\,;360)$,
  étiquetée $\mathcal{D}$ au-dessus de son extrémité droite ;
- point $(0\,;60)$ marqué, étiqueté $60$ à gauche de l'axe des ordonnées ;
- **horizontale de lecture** en `solideE`, tirets, d'équation $C=260$, du bord gauche jusqu'au point
  d'intersection $(40\,;260)$, étiquetée $260$ à gauche de l'axe ;
- **verticale de rappel** en tirets gris de $(40\,;260)$ jusqu'à l'axe des abscisses, avec
  l'étiquette $40$ sous l'axe, en gras ;
- le point d'intersection $(40\,;260)$ marqué par un gros point noir ;
- petite flèche grise le long de la droite vers la droite du point, légendée « au-delà, le coût
  dépasse $260$ € ».

## 3. `mathstc-suite-batons` — diagramme en bâtons d'une suite géométrique

Repère, abscisses $n$ de $0$ à $10{,}5$ (**0,62 cm** par unité), ordonnées de $0$ à $32$
(**0,15 cm** par unité). Graduations entières $0$ à $10$ en abscisse ; $5$, $10$, $15$, $20$, $25$,
$30$ en ordonnée.

Onze bâtons verticaux **`solideA`** (`line width=2.4pt`), de l'axe jusqu'au point $\left(n\,;u_{n}\right)$
avec $u_{n}=5\times1{,}2^{n}$, sommet marqué d'un petit disque :

| $n$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $u_{n}$ | $5$ | $6$ | $7{,}2$ | $8{,}64$ | $10{,}37$ | $12{,}44$ | $14{,}93$ | $17{,}92$ | $21{,}50$ | $25{,}80$ | $30{,}96$ |

- valeurs de $u_{0}$, $u_{4}$ et $u_{10}$ écrites en petit au-dessus de leur bâton ($5$ ; $10{,}37$ ;
  $30{,}96$), les autres non étiquetées ;
- entre les sommets de $u_{3}$ et $u_{4}$, une petite flèche courbe grise légendée « $\times1{,}2$ » ;
- en haut à gauche, encadré : $u_{n}=5\times1{,}2^{n}$.

## 4. `mathstc-suites-lin-vs-geo` — croissance linéaire contre croissance exponentielle

Repère, abscisses $n$ de $0$ à $8{,}4$ (**0,78 cm** par unité), ordonnées de $0$ à $1\,000$
(**0,45 cm pour 100**). Graduations entières $0$ à $8$ en abscisse ; $200$, $400$, $600$, $800$,
$1\,000$ en ordonnée. Axes légendés « année $n$ » et « production ».

Deux séries de points, reliés par une ligne brisée fine pour la lisibilité :

| $n$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ |
|---|---|---|---|---|---|---|---|---|---|
| $400+60n$ (**`solideB`**, carrés) | $400$ | $460$ | $520$ | $580$ | $640$ | $700$ | $760$ | $820$ | $880$ |
| $400\times1{,}12^{n}$ (**`solideA`**, disques) | $400$ | $448$ | $501{,}8$ | $562{,}0$ | $629{,}4$ | $704{,}9$ | $789{,}5$ | $884{,}3$ | $990{,}4$ |

- étiquettes de série posées à droite des dernières valeurs : $400+60n$ en bleu,
  $400\times1{,}12^{n}$ en rouge ;
- entre $n=4$ et $n=5$, une **bande verticale grise à 15 % d'opacité** couvrant les deux abscisses,
  légendée sous l'axe « le modèle exponentiel passe devant » ;
- en $n=4$ les deux valeurs $640$ et $629{,}4$ sont écrites en petit ; en $n=5$, $700$ et $704{,}9$.

## 5. `mathstc-exp-base-a` — faisceau des fonctions $x\mapsto a^{x}$

Repère, abscisses de $-2{,}2$ à $2{,}2$ (**1,45 cm** par unité), ordonnées de $0$ à $4{,}3$
(**1,05 cm** par unité). Graduations $-2$, $-1$, $1$, $2$ en abscisse ; $1$, $2$, $3$, $4$ en
ordonnée.

Cinq courbes tracées sur $\left[-2\,;2\right]$ (`samples=80, smooth`), toutes passant par
$(0\,;1)$ :

| $a$ | couleur / style | $x=-2$ | $x=-1$ | $x=1$ | $x=2$ |
|---|---|---|---|---|---|
| $2$ | **`solideA`** trait plein | $0{,}25$ | $0{,}5$ | $2$ | $4$ |
| $1{,}5$ | **`solideA`** tirets | $0{,}444$ | $0{,}667$ | $1{,}5$ | $2{,}25$ |
| $1$ | gris, trait plein | $1$ | $1$ | $1$ | $1$ |
| $0{,}8$ | **`solideB`** tirets | $1{,}5625$ | $1{,}25$ | $0{,}8$ | $0{,}64$ |
| $0{,}5$ | **`solideB`** trait plein | $4$ | $2$ | $0{,}5$ | $0{,}25$ |

- chaque courbe étiquetée près de son extrémité droite par la valeur de $a$ ($a=2$, $a=1{,}5$,
  $a=1$, $a=0{,}8$, $a=0{,}5$) ;
- le point commun $(0\,;1)$ marqué par un gros point noir, étiqueté $(0\,;1)$ ;
- deux mentions en gris, l'une en haut à droite « $a>1$ : croissante », l'autre en haut à gauche
  « $0<a<1$ : décroissante » ;
- rappeler en bas, hors du repère, en petit : « toutes ces courbes restent **au-dessus** de l'axe
  des abscisses ».

## 6. `mathstc-log-decimal` — la courbe du logarithme décimal et la lecture de $\log(350)$

Repère non orthonormé : abscisses de $0$ à $520$ (**1,3 cm pour 100**), ordonnées de $-0{,}6$ à
$3$ (**1,4 cm** par unité). Graduations $100$, $200$, $300$, $400$, $500$ en abscisse ; $1$, $2$,
$3$ en ordonnée.

- courbe **`solideA`** de $y=\log(x)$ tracée pour $x\in\left[3\,;500\right]$ (`samples=120,
  smooth`). Repères de tracé : $\log(3)=0{,}477$ ; $\log(10)=1$ ; $\log(50)=1{,}699$ ;
  $\log(100)=2$ ; $\log(200)=2{,}301$ ; $\log(350)=2{,}544$ ; $\log(500)=2{,}699$ ;
- points marqués et étiquetés : $(10\,;1)$ et $(100\,;2)$ ;
- **lecture de $\log(350)$** : verticale en tirets gris de $(350\,;0)$ à $(350\,;2{,}544)$, puis
  horizontale en `solideE` tirets jusqu'à l'axe des ordonnées ; étiquette $350$ sous l'axe des
  abscisses et $\log(350)\approx2{,}54$ à gauche de l'axe des ordonnées ;
- en gris, près de l'origine, la mention « la courbe plonge vers le bas quand $x$ se rapproche de
  $0$ » avec une petite flèche vers le bas ;
- encadré en bas à droite : « $\log(b)$ est la solution de $10^{x}=b$ ».

## 7. `mathstc-semilog` — repère linéaire et repère semi-logarithmique

**Deux panneaux côte à côte**, séparés par un filet vertical fin, chacun ≈ 3,8 cm de large. Même
série dans les deux : $u_{n}=5\times1{,}2^{n}$ pour $n=0$, $2$, $4$, $6$, $8$, $10$.

Panneau de **gauche**, titre « repère ordinaire » : abscisses $n$ de $0$ à $10$ (0,33 cm par unité),
ordonnées de $0$ à $32$ (0,13 cm par unité). Points **`solideA`** aux ordonnées $5$ ; $7{,}2$ ;
$10{,}37$ ; $14{,}93$ ; $21{,}50$ ; $30{,}96$, reliés par une courbe fine **incurvée vers le haut**.

Panneau de **droite**, titre « repère semi-logarithmique » : abscisses $n$ identiques, ordonnées
$\log\left(u_{n}\right)$ de $0{,}6$ à $1{,}6$ (3,5 cm pour l'unité), graduations $0{,}8$, $1{,}0$,
$1{,}2$, $1{,}4$. Points **`solideA`** aux ordonnées $0{,}699$ ; $0{,}857$ ; $1{,}016$ ; $1{,}174$ ;
$1{,}333$ ; $1{,}491$, **alignés** ; droite **`solideE`** passant par eux, prolongée sur toute la
largeur du panneau.

Sous les deux panneaux, une seule ligne centrée :
« $\log\left(u_{n}\right)=\log(5)+n\log(1{,}2)$ : une expression **affine** en $n$ ».

## 8. `mathstc-fonction-inverse` — l'hyperbole et sa tangente en $x=2$

Repère orthonormé, unité **0,85 cm**, abscisses de $-4{,}2$ à $4{,}4$, ordonnées de $-4{,}2$ à
$4{,}2$. Graduations $-4$, $-2$, $2$, $4$ sur chaque axe.

- deux branches **`solideA`** de $y=\dfrac{1}{x}$, tracées pour $x\in\left[0{,}25\,;4\right]$ et
  $x\in\left[-4\,;-0{,}25\right]$ (`samples=80, smooth`) ;
- **tangente** en `solideE`, trait plein, d'équation $y=-\dfrac{1}{4}x+1$, tracée de $(0\,;1)$ à
  $(4{,}2\,;-0{,}05)$ ; point de tangence $(2\,;0{,}5)$ marqué par un gros point noir, étiqueté
  $\left(2\,;\dfrac{1}{2}\right)$ ; étiquette de la droite $y=-\dfrac{1}{4}x+1$ posée près de son
  extrémité droite ;
- deux flèches courbes en tirets gris avec leur légende : le long de la branche droite près de
  l'axe des ordonnées, « $x$ proche de $0$ : $\dfrac{1}{x}$ devient très grand » ; le long de la
  branche droite près de l'axe des abscisses, « $x$ très grand : $\dfrac{1}{x}$ se rapproche de
  $0$ » ;
- **ne pas écrire le mot « asymptote »** : le programme exclut explicitement cette notion.

## 9. `mathstc-cout-moyen` — la courbe en U du coût moyen

Repère non orthonormé : abscisses $q$ de $0$ à $105$ (**0,062 cm** par unité, soit ≈ 6,5 cm),
ordonnées de $0$ à $130$ (**0,04 cm** par euro, soit ≈ 5,2 cm). Graduations $20$, $40$, $60$, $80$,
$100$ en abscisse ; $40$, $80$, $120$ en ordonnée. Axes légendés « quantité $q$ » et
« coût moyen (€ par pièce) ».

Courbe **`solideA`** de $C_{M}(q)=0{,}5q+40+\dfrac{800}{q}$ sur $\left[10\,;100\right]$
(`samples=90, smooth`). Repères de tracé :

| $q$ | $10$ | $20$ | $30$ | $40$ | $50$ | $60$ | $80$ | $100$ |
|---|---|---|---|---|---|---|---|---|
| $C_{M}(q)$ | $125$ | $90$ | $81{,}7$ | $80$ | $81$ | $83{,}3$ | $90$ | $98$ |

- minimum $(40\,;80)$ marqué par un gros point noir, avec traits de rappel en **tirets gris** vers
  les deux axes ; étiquettes $40$ sous l'axe des abscisses et $80$ à gauche de l'axe des ordonnées ;
- deux légendes grises avec flèche : à gauche de la courbe, « frais fixes répartis sur peu de
  pièces » ; à droite, « le terme $0{,}5q$ l'emporte » ;
- encadré en haut à droite : $C_{M}(q)=0{,}5q+40+\dfrac{800}{q}$.

## 10. `mathstc-nuage-ajustement` — nuage, droite des moindres carrés et résidus

Repère non orthonormé : abscisses de $0$ à $5$ (**1,3 cm** par unité), ordonnées de $0$ à $10$
(**0,5 cm** par unité). Graduations $1$ à $4$ en abscisse ; $2$, $4$, $6$, $8$, $10$ en ordonnée.

- quatre points du nuage, gros disques noirs : $(1\,;3)$, $(2\,;5)$, $(3\,;8)$, $(4\,;9)$ ;
- droite **`solideE`**, trait plein, d'équation $y=2{,}1x+1$, tracée de $(0\,;1)$ à $(4{,}6\,;10{,}66)$,
  étiquetée $y=2{,}1x+1$ au-dessus de son extrémité droite ;
- **résidus** matérialisés par quatre segments **verticaux** en `solideA`, épais, joignant chaque
  point à la droite ; ordonnées prédites $3{,}1$ ; $5{,}2$ ; $7{,}3$ ; $9{,}4$, donc résidus
  $-0{,}1$ ; $-0{,}2$ ; $+0{,}7$ ; $-0{,}4$ ;
- le résidu du point $(3\,;8)$, le plus long, étiqueté $0{,}7$ à sa droite ;
- sous la figure, sur une ligne : « la droite des moindres carrés minimise
  $\displaystyle\sum_{i}\left(y_{i}-\left(ax_{i}+b\right)\right)^{2}=0{,}70$ ».

## 11. `mathstc-changement-variable` — linéariser par $z=\log(N)$

**Deux panneaux côte à côte**, séparés par un filet vertical fin, chacun ≈ 3,8 cm de large. Même
abscisse dans les deux : $t$ de $0$ à $4{,}3$ h (0,8 cm par unité), graduations entières $0$ à $4$.

Panneau de **gauche**, titre « $(t\,;N)$ » : ordonnées de $0$ à $15\,000$ (0,3 cm pour $1\,000$),
graduations $5\,000$, $10\,000$, $15\,000$. Points **`solideA`** aux ordonnées $500$ ; $1\,150$ ;
$2\,700$ ; $6\,200$ ; $14\,300$, reliés par une courbe fine **nettement incurvée vers le haut**.
Mention grise « pas d'alignement ».

Panneau de **droite**, titre « $(t\,;z)$ avec $z=\log(N)$ » : ordonnées de $2{,}5$ à $4{,}3$
(2,5 cm pour l'unité), graduations $3$, $3{,}5$, $4$. Points **`solideA`** aux ordonnées $2{,}699$ ;
$3{,}061$ ; $3{,}431$ ; $3{,}792$ ; $4{,}155$, **alignés** ; droite **`solideE`** d'équation
$z=0{,}364t+2{,}699$ tracée sur tout le panneau, étiquetée par son équation.

Sous les deux panneaux, une ligne centrée :
« retour aux variables initiales : $N\approx500\times2{,}31^{t}$ ».

## 12. `mathstc-arbre-probas` — arbre pondéré à deux niveaux

Pas de repère : un **arbre** orienté de gauche à droite, largeur ≈ 8 cm, hauteur ≈ 5,5 cm.

Un nœud racine (petit disque noir, sans étiquette) à gauche, deux branches vers $A$ et $B$, puis
deux branches depuis chacun vers $D$ et $\overline{D}$ (quatre feuilles). Nœuds dessinés en cadres
arrondis gris clair.

| Branche | Poids | Extrémité |
|---|---|---|
| racine $\to A$ | $0{,}60$ | $A$ (ligne A) |
| racine $\to B$ | $0{,}40$ | $B$ (ligne B) |
| $A\to D$ | $0{,}03$ | $D$ |
| $A\to\overline{D}$ | $0{,}97$ | $\overline{D}$ |
| $B\to D$ | $0{,}05$ | $D$ |
| $B\to\overline{D}$ | $0{,}95$ | $\overline{D}$ |

- poids écrits **au-dessus** de chaque branche, en petit ;
- le chemin racine $\to A\to D$ tracé en **`solideA`** épais, les cinq autres branches en noir fin ;
- à droite de chaque feuille, le produit du chemin : $0{,}018$ (en `solideA`), $0{,}582$, $0{,}020$,
  $0{,}380$ ;
- accolade grise à droite regroupant les deux feuilles $D$, légendée
  « $P(D)=0{,}018+0{,}020=0{,}038$ » ;
- en bas, en gris : « somme des quatre chemins $=1$ ».

## 13. `mathstc-binomiale-batons` — diagramme en bâtons de $\mathcal{B}(20\,;0{,}1)$

Repère, abscisses $k$ de $-0{,}5$ à $8{,}5$ (**0,7 cm** par unité), ordonnées de $0$ à $0{,}30$
(**15 cm** pour l'unité, soit 4,5 cm). Graduations entières $0$ à $8$ en abscisse ; $0{,}05$,
$0{,}10$, $0{,}15$, $0{,}20$, $0{,}25$ en ordonnée.

Neuf bâtons verticaux **`solideA`** (`line width=3pt`), sommet marqué d'un petit disque :

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ |
|---|---|---|---|---|---|---|---|---|---|
| $P(X=k)$ | $0{,}1216$ | $0{,}2702$ | $0{,}2852$ | $0{,}1901$ | $0{,}0898$ | $0{,}0319$ | $0{,}0089$ | $0{,}0020$ | $0{,}0004$ |

- valeurs de $P(X=0)$ à $P(X=3)$ écrites en petit au-dessus de leur bâton, arrondies à $0{,}001$
  ($0{,}122$ ; $0{,}270$ ; $0{,}285$ ; $0{,}190$) ; les bâtons suivants non étiquetés ;
- **espérance** marquée par une flèche verticale **`solideE`** partant de sous l'axe et pointant
  vers l'abscisse $k=2$, légendée $E(X)=np=2$ ;
- en haut à droite, encadré : $\mathcal{B}(20\,;0{,}1)$ ;
- en gris, sous l'axe à droite : « la loi n'est symétrique que si $p=0{,}5$ ».
