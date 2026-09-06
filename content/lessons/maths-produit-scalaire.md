# Produit scalaire

## Définition géométrique

Soit $\vec{u}$ et $\vec{v}$ deux vecteurs **non nuls** du plan et $\theta$ une mesure de l'angle qu'ils forment. Le **produit scalaire** de $\vec{u}$ et $\vec{v}$ est le **nombre**
$$\vec{u}\cdot\vec{v}=\left\|\vec{u}\right\|\times\left\|\vec{v}\right\|\times\cos(\theta).$$
Si $\vec{u}$ ou $\vec{v}$ est nul, alors $\vec{u}\cdot\vec{v}=0$.

{{fig:maths-produit-scalaire-angle}}

Le signe du produit scalaire est celui de $\cos(\theta)$ : **positif** pour un angle aigu, **nul** pour un angle droit, **négatif** pour un angle obtus.

## Projection orthogonale et définition algébrique

Soit $\mathcal{D}$ une droite et $\vec{u}=\overrightarrow{AB}$. La **projection orthogonale** de $\vec{u}$ sur $\mathcal{D}$ est le vecteur $\overrightarrow{CD}$, où $C$ et $D$ sont les points de $\mathcal{D}$ tels que $(AC)$ et $(BD)$ soient perpendiculaires à $\mathcal{D}$.

{{fig:maths-projection-orthogonale}}

Si $\mathcal{D}$ est dirigée par $\vec{v}$, alors
$$\vec{u}\cdot\vec{v}=\begin{cases}\ \ \ CD\times\left\|\vec{v}\right\| & \text{si }\overrightarrow{CD}\text{ et }\vec{v}\text{ sont de même sens},\\[4pt] -CD\times\left\|\vec{v}\right\| & \text{s'ils sont de sens contraire}.\end{cases}$$

On retrouve la définition géométrique, puisque la longueur $CD$ vaut $\left\|\vec{u}\right\|\times\left|\cos(\theta)\right|$.

## Définition analytique et norme

Dans un repère **orthonormé**, si $\vec{u}$ a pour coordonnées $(x\,;y)$ et $\vec{v}$ pour coordonnées $(x'\,;y')$ :
$$\vec{u}\cdot\vec{v}=xx'+yy'\qquad\text{et}\qquad\left\|\vec{u}\right\|=\sqrt{\vec{u}\cdot\vec{u}}=\sqrt{x^{2}+y^{2}}.$$

## Propriétés

Soit $\vec{u}$, $\vec{v}$, $\vec{w}$ trois vecteurs et $k$ un réel.

- **Symétrie** : $\vec{u}\cdot\vec{v}=\vec{v}\cdot\vec{u}$.
- **Linéarité à gauche** : $(\vec{u}+k\vec{v})\cdot\vec{w}=\vec{u}\cdot\vec{w}+k(\vec{v}\cdot\vec{w})$.
- **Linéarité à droite** : $\vec{u}\cdot(\vec{v}+k\vec{w})=\vec{u}\cdot\vec{v}+k(\vec{u}\cdot\vec{w})$.

Relations avec la norme :
$$\left\|\vec{u}+\vec{v}\right\|^{2}=\left\|\vec{u}\right\|^{2}+2\,\vec{u}\cdot\vec{v}+\left\|\vec{v}\right\|^{2}$$
$$\left\|\vec{u}-\vec{v}\right\|^{2}=\left\|\vec{u}\right\|^{2}-2\,\vec{u}\cdot\vec{v}+\left\|\vec{v}\right\|^{2}$$
$$(\vec{u}+\vec{v})\cdot(\vec{u}-\vec{v})=\left\|\vec{u}\right\|^{2}-\left\|\vec{v}\right\|^{2}$$

*Attention :* on voit parfois un membre central en trop dans cette dernière égalité ; la relation correcte est bien $(\vec{u}+\vec{v})\cdot(\vec{u}-\vec{v})=\left\|\vec{u}\right\|^{2}-\left\|\vec{v}\right\|^{2}$.

On en déduit trois façons de calculer un produit scalaire à partir des seules longueurs :
$$\vec{u}\cdot\vec{v}=\frac{1}{2}\left(\left\|\vec{u}+\vec{v}\right\|^{2}-\left\|\vec{u}\right\|^{2}-\left\|\vec{v}\right\|^{2}\right)=\frac{1}{2}\left(\left\|\vec{u}\right\|^{2}+\left\|\vec{v}\right\|^{2}-\left\|\vec{u}-\vec{v}\right\|^{2}\right)=\frac{1}{4}\left(\left\|\vec{u}+\vec{v}\right\|^{2}-\left\|\vec{u}-\vec{v}\right\|^{2}\right)$$

## Orthogonalité

Deux vecteurs non nuls $\vec{u}$ et $\vec{v}$ sont **orthogonaux** (noté $\vec{u}\perp\vec{v}$) lorsque toute droite dirigée par $\vec{u}$ est perpendiculaire à toute droite dirigée par $\vec{v}$. On a l'équivalence :
$$\vec{u}\perp\vec{v}\iff\vec{u}\cdot\vec{v}=0.$$

C'est le test le plus rapide en coordonnées : $(2\,;3)$ et $(-3\,;2)$ sont orthogonaux car $2\times(-3)+3\times2=0$.

## Théorème d'Al-Kashi

Dans un triangle $ABC$, en posant $a=BC$, $b=AC$ et $c=AB$ :
$$a^{2}=b^{2}+c^{2}-2bc\cos(\hat{A})\qquad b^{2}=a^{2}+c^{2}-2ac\cos(\hat{B})\qquad c^{2}=a^{2}+b^{2}-2ab\cos(\hat{C})$$

{{fig:maths-al-kashi}}

C'est le **théorème de Pythagore généralisé** : si $\hat{A}=\dfrac{\pi}{2}$, alors $\cos(\hat{A})=0$ et il reste $a^{2}=b^{2}+c^{2}$. L'angle utilisé est toujours celui **opposé** au côté que l'on calcule.
