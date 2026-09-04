# Intégrale, aire et valeur moyenne

## Définition : une aire

Soit $f$ **positive** et continue sur $\left[a\,;b\right]$ avec $a<b$. L'intégrale
$$\int_{a}^{b}f(x)\,\mathrm{d}x$$
est l'**aire**, en unités d'aire (u.a.), du domaine compris entre la courbe de $f$, l'axe des abscisses et les droites d'équations $x=a$ et $x=b$. L'existence de cette intégrale est **admise**.

{{fig:mathstle-aire-sous-courbe}}

On étend ensuite la définition aux fonctions négatives (l'aire est comptée négativement), puis aux fonctions qui changent de signe, et enfin au cas $a>b$ par la convention
$$\int_{b}^{a}f(x)\,\mathrm{d}x=-\int_{a}^{b}f(x)\,\mathrm{d}x.$$

## Approcher par des rectangles

En découpant $\left[a\,;b\right]$ en $n$ morceaux de largeur $\Delta x=\dfrac{b-a}{n}$, on approche l'aire par une somme de rectangles :
$$\sum_{i=0}^{n-1}f(x_{i})\,\Delta x\ \approx\ \int_{a}^{b}f(x)\,\mathrm{d}x.$$

{{fig:mathstle-rectangles}}

Plus $n$ est grand, meilleure est l'approximation. C'est cette écriture qui explique la notation : le signe $\int$ est un « S » allongé pour *somme*, et $\mathrm{d}x$ rappelle la largeur $\Delta x$.

## Primitives et calcul pratique

Si $F$ est une primitive de $f$ sur $\left[a\,;b\right]$, alors
$$\int_{a}^{b}f(x)\,\mathrm{d}x=\left[F(x)\right]_{a}^{b}=F(b)-F(a).$$
Le résultat ne dépend pas de la primitive choisie : la constante additive disparaît par différence.

| Fonction | Une primitive |
|---|---|
| $\mathrm{e}^{ax}$, $a\neq0$ | $\dfrac{1}{a}\mathrm{e}^{ax}$ |
| $\dfrac{1}{x}$ sur $\left]0\,;+\infty\right[$ | $\ln(x)$ |
| $u'\,\mathrm{e}^{u}$ | $\mathrm{e}^{u}$ |
| $\dfrac{u'}{u}$ avec $u>0$ | $\ln(u)$ |
| $u'u^{n}$, $n\neq-1$ | $\dfrac{u^{n+1}}{n+1}$ |
| $u'\cos(u)$ / $u'\sin(u)$ | $\sin(u)$ / $-\cos(u)$ |
| $f(ax+b)$, $F$ primitive de $f$ | $\dfrac{F(ax+b)}{a}$ |

Pour **montrer** que $F$ est une primitive de $f$, la seule technique est de **dériver $F$** et de retrouver $f$.

*Exemple résolu.* $f(x)=(8x+1)\mathrm{e}^{-x}$ et $F(x)=-(8x+9)\mathrm{e}^{-x}$ :
$F'(x)=-8\mathrm{e}^{-x}+(8x+9)\mathrm{e}^{-x}=\mathrm{e}^{-x}(8x+1)=f(x)$.
D'où l'aire sous la courbe entre $0$ et $2$ : $F(2)-F(0)=-25\mathrm{e}^{-2}+9\approx5{,}62$ u.a.

## Propriétés

- **Linéarité** : $\displaystyle\int_{a}^{b}(f+g)=\int_{a}^{b}f+\int_{a}^{b}g$ et $\displaystyle\int_{a}^{b}kf=k\int_{a}^{b}f$.
- **Positivité** : si $f\geqslant0$ sur $\left[a\,;b\right]$ et $a<b$, alors $\displaystyle\int_{a}^{b}f\geqslant0$.
- **Croissance** : si $f\leqslant g$, alors $\displaystyle\int_{a}^{b}f\leqslant\int_{a}^{b}g$.
- **Chasles** : $\displaystyle\int_{a}^{b}f=\int_{a}^{c}f+\int_{c}^{b}f$.

L'intégrale **n'est pas multiplicative** : $\displaystyle\int_{a}^{b}(f\times g)\neq\int_{a}^{b}f\times\int_{a}^{b}g$.

**Aire entre deux courbes.** Si $f\geqslant g$ sur $\left[a\,;b\right]$, l'aire du domaine compris entre les deux courbes vaut $\displaystyle\int_{a}^{b}\left(f(x)-g(x)\right)\mathrm{d}x$ : toujours « celle du haut moins celle du bas ».

## Valeur moyenne

La valeur moyenne de $f$ sur $\left[a\,;b\right]$ est
$$\mu=\frac{1}{b-a}\int_{a}^{b}f(x)\,\mathrm{d}x.$$
C'est la **hauteur** du rectangle de largeur $b-a$ qui a la même aire que le domaine sous la courbe.

{{fig:mathstle-valeur-moyenne}}

En physique : la valeur moyenne de la puissance sur une période est la **puissance active**. Pour $p(t)=U_{m}I_{m}\cos^{2}(\omega t)$, on linéarise avec $\cos^{2}(\theta)=\dfrac{1+\cos(2\theta)}{2}$, dont la valeur moyenne vaut $\dfrac{1}{2}$ : la puissance active vaut donc $\dfrac{U_{m}I_{m}}{2}$.

## Intégrale dépendant de sa borne supérieure

Pour $F_{a}(x)=\displaystyle\int_{a}^{x}f(t)\,\mathrm{d}t$, il faut distinguer trois rôles : $a$ est un **paramètre**, $x$ est la **variable**, et $t$ est une **variable muette** (on peut la renommer sans rien changer). On a alors $F_{a}'=f$ : dériver une intégrale à borne variable redonne la fonction intégrée.
