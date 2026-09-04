# Les actions mécaniques

On appelle **action mécanique** toute cause physique capable :

- de maintenir un solide en équilibre ;
- de déplacer un solide ou de modifier son mouvement ;
- de déformer un solide.

Une action mécanique a toujours une **origine** et une **cible** : on note $i \rightarrow j$ l'action de *i* sur *j*.
On distingue les actions **à distance** (pesanteur, champ magnétique, champ électrostatique) et les actions
**de contact**, exercées par un solide sur un autre par l'intermédiaire de leurs surfaces de contact.

Les actions mécaniques sont de deux natures :

- une **force** (effort) pousse ou tire suivant un axe : elle s'exprime en **newtons (N)** ;
- un **moment** (couple) fait tourner ou tordre autour d'un axe : il s'exprime en **newtons-mètres (N·m)**.

Forces et moments sont modélisés par des **vecteurs** : ils ont un point d'application, un support, un sens et une norme.

## Deux actions à connaître

{{fig:statique-poids}}

Le **poids** s'exerce en tout point du solide, mais il se ramène à une seule force appliquée au **centre de
gravité** $G$ et dirigée vers le bas : $P = m \times g$, avec $P$ en N, $m$ en kg et $g = 9{,}81$ m/s².

L'action d'un **fluide sous pression** sur une surface se ramène de même à une résultante appliquée au centre
géométrique de la surface : $F = p \times S$, avec $F$ en N, $p$ en Pa et $S$ en m².
Attention aux unités : $1 \text{ bar} = 10^5 \text{ Pa}$.

## Le moment d'une force

{{fig:statique-moment-force}}

Le **moment** d'une force par rapport à un point $A$ est le produit de l'intensité de la force par le
**bras de levier** $d$, c'est-à-dire la distance **perpendiculaire** entre $A$ et le support de la force :

$M_{/A}(\vec{F}) = F \times d$, avec $M$ en N·m, $F$ en N et $d$ en **mètres**.

{{fig:statique-moment-angle}}

Plus $d$ est grand, plus le moment est grand. Le moment est **maximal** quand la force est perpendiculaire au
bras ($90°$) et **nul** quand la force est colinéaire au bras. Le signe du moment suit le sens de rotation
qu'il tend à produire : le **sens trigonométrique** est pris comme sens positif.

## Le couple

{{fig:statique-couple}}

Un **couple** est produit par un ensemble de forces dont la somme vectorielle est nulle :
$\vec{F_1} + \vec{F_2} = \vec{0}$, et pourtant $T = F_1 \times r_1 + F_2 \times r_2$ n'est pas nul.
Un couple fait donc tourner sans pousser (couple moteur, couple de serrage).

## Projeter et modéliser

{{fig:statique-projection}}

Avec $\beta$ l'angle entre $\vec{F}$ et l'axe $y$ : $F_x = -F \sin\beta$ et $F_y = +F \cos\beta$
(signe $+$ si la composante va dans le sens de l'axe, $-$ sinon). Réciproquement, la norme se calcule par
Pythagore : $F = \sqrt{F_x^2 + F_y^2 + F_z^2}$.

{{fig:statique-torseur}}

Les six composantes d'une action mécanique se rangent dans un **torseur** : $X$, $Y$, $Z$ pour la
**résultante** (la force) et $L$, $M$, $N$ pour le **moment**. Le point écrit sous l'accolade est le
**point de réduction** : c'est le point où le moment est exprimé.

Enfin, le **principe des actions mutuelles** (3ᵉ loi de Newton) : au même point $A$,
$\{\tau_{2 \rightarrow 1}\} = -\{\tau_{1 \rightarrow 2}\}$ — toutes les composantes changent de signe.

## À retenir

| Grandeur | Formule | Unité |
|---|---|---|
| Poids | $P = m \times g$ ($g = 9{,}81$ m/s²) | N |
| Force d'un fluide | $F = p \times S$ ($1$ bar $= 10^5$ Pa) | N |
| Moment d'une force | $M = F \times d$ ($d$ = bras de levier) | N·m |
| Couple | $T = F_1 \times r_1 + F_2 \times r_2$ | N·m |
| Norme d'un vecteur | $F = \sqrt{F_x^2 + F_y^2 + F_z^2}$ | N |
