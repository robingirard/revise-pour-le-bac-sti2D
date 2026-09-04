# Nombres complexes

## Forme algébrique

On introduit le nombre **imaginaire** $i$, dont le carré vaut $-1$ : $i^{2}=-1$.
Un **nombre complexe** est un nombre $z$ qui s'écrit $z=a+bi$ avec $a$ et $b$ réels : c'est sa **forme algébrique**.

- $a=\mathrm{Re}(z)$ est la **partie réelle** de $z$ (un nombre **réel**) ;
- $b=\mathrm{Im}(z)$ est la **partie imaginaire** de $z$ (un nombre **réel**, sans le $i$).

L'ensemble des nombres complexes se note $\mathbb{C}$. Il est muni d'une addition et d'une multiplication qui prolongent celles de $\mathbb{R}$ : **toutes les règles de calcul habituelles restent valables**, avec en plus $i^{2}=-1$.

- **Conjugué** : $\overline{z}=a-bi$.
- **Module** : $\displaystyle\left|z\right|=\sqrt{a^{2}+b^{2}}$ (un réel positif).

## Plan complexe

Dans un repère orthonormé direct $(O,I,J)$, le point $M$ de coordonnées $(a\,;b)$ est le **point d'affixe** $z=a+bi$, noté $M(z)$ ; le vecteur de coordonnées $(a\,;b)$ est le **vecteur d'affixe** $z$. L'axe des abscisses est l'**axe réel**, l'axe des ordonnées l'**axe des imaginaires purs**.

{{fig:maths-plan-complexe}}

Le module $\left|z\right|$ est la distance $OM$ ; le point d'affixe $\overline{z}$ est le symétrique de $M$ par rapport à l'axe réel.

## Opérations

$$(a+bi)+(a'+b'i)=(a+a')+(b+b')i\qquad\qquad(a+bi)(a'+b'i)=(aa'-bb')+(a'b+ab')i$$
$$(a+bi)^{2}=(a^{2}-b^{2})+2abi\qquad(a-bi)^{2}=(a^{2}-b^{2})-2abi\qquad(a+bi)(a-bi)=a^{2}+b^{2}$$

Le produit d'un complexe par son conjugué est donc un **réel positif**. C'est ce qui permet d'écrire un **quotient** sous forme algébrique : on multiplie le numérateur et le dénominateur par le conjugué du dénominateur. Pour $z'\neq0$ :
$$\frac{z}{z'}=\frac{z\,\overline{z'}}{z'\,\overline{z'}}=\frac{aa'+bb'}{a'^{2}+b'^{2}}+\frac{a'b-ab'}{a'^{2}+b'^{2}}\,i$$

Conjugués et modules se comportent bien vis-à-vis du produit et du quotient : $\overline{z+z'}=\overline{z}+\overline{z'}$, $\overline{z\times z'}=\overline{z}\times\overline{z'}$, $\left|z\times z'\right|=\left|z\right|\times\left|z'\right|$ et $\left|\dfrac{z}{z'}\right|=\dfrac{\left|z\right|}{\left|z'\right|}$. En revanche, pour la somme, on n'a qu'une **inégalité triangulaire** : $\left|z+z'\right|\leqslant\left|z\right|+\left|z'\right|$.

**Équation** $z^{2}=a$ (avec $a$ réel) : les solutions sont $\sqrt{a}$ et $-\sqrt{a}$ si $a>0$ ; $0$ si $a=0$ ; $i\sqrt{-a}$ et $-i\sqrt{-a}$ si $a<0$.

## Forme trigonométrique

Pour $z\neq0$ de point image $M$, l'**argument** de $z$, noté $\arg(z)$, est une mesure en radians de l'angle orienté $\left(\overrightarrow{OI},\overrightarrow{OM}\right)$, définie modulo $2\pi$. Tout complexe non nul s'écrit alors
$$z=r\big(\cos(\theta)+i\sin(\theta)\big)\qquad\text{avec } r=\left|z\right| \text{ et } \theta=\arg(z)\ [2\pi].$$

**De la forme algébrique à la forme trigonométrique** : $r=\sqrt{a^{2}+b^{2}}$, puis on cherche $\theta$ vérifiant **les deux** conditions $\cos(\theta)=\dfrac{a}{r}$ et $\sin(\theta)=\dfrac{b}{r}$ (le tableau des valeurs remarquables suffit dans les cas usuels).

**De la forme trigonométrique à la forme algébrique** : $a=r\cos(\theta)$ et $b=r\sin(\theta)$.

## Forme exponentielle

Pour tout réel $\theta$, on pose
$$\mathrm{e}^{i\theta}=\cos(\theta)+i\sin(\theta),$$
exponentielle qui possède **les mêmes propriétés algébriques** que l'exponentielle réelle. Tout complexe non nul s'écrit donc $z=r\,\mathrm{e}^{i\theta}$ avec $r=\left|z\right|$ et $\theta=\arg(z)\ [2\pi]$ : c'est la **forme exponentielle**.

*Exemples :* $2i=2\,\mathrm{e}^{i\frac{\pi}{2}}$, $-3=3\,\mathrm{e}^{i\pi}$, $1+i=\sqrt{2}\,\mathrm{e}^{i\frac{\pi}{4}}$, $1+i\sqrt{3}=2\,\mathrm{e}^{i\frac{\pi}{3}}$.

En développant $\mathrm{e}^{i(a+b)}=\mathrm{e}^{ia}\mathrm{e}^{ib}$, on retrouve les formules de trigonométrie :

$$\cos(a+b)=\cos(a)\cos(b)-\sin(a)\sin(b)\qquad\cos(a-b)=\cos(a)\cos(b)+\sin(a)\sin(b)$$
$$\sin(a+b)=\sin(a)\cos(b)+\sin(b)\cos(a)\qquad\sin(a-b)=\sin(a)\cos(b)-\sin(b)\cos(a)$$
$$\cos(2a)=\cos^{2}(a)-\sin^{2}(a)\qquad\sin(2a)=2\sin(a)\cos(a)$$
$$\cos^{2}(a)=\frac{1+\cos(2a)}{2}\qquad\sin^{2}(a)=\frac{1-\cos(2a)}{2}$$
