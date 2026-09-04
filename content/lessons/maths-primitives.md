# Primitives

## Définition

Soit $f$ et $F$ deux fonctions définies sur un intervalle $I$ de $\mathbb{R}$.
On dit que $F$ est une **primitive** de $f$ sur $I$ lorsque $F$ est dérivable sur $I$ et que $F'=f$ sur $I$.

Primitiver, c'est donc **remonter** la dérivation : on cherche la fonction dont $f$ est la dérivée.

**Les primitives d'une fonction diffèrent d'une constante.** Si $F$ est une primitive de $f$ sur $I$, alors une fonction $G$ dérivable sur $I$ est une primitive de $f$ sur $I$ **si et seulement s'il** existe un réel $k$ tel que $F=G+k$. Une fonction qui admet une primitive en admet donc une infinité.

## Tableau des primitives usuelles

Dans tout le tableau, $k$ désigne une constante réelle.

| Fonction $f$ | Primitives $F$ |
|---|---|
| $f(x)=C$ (constante) | $F(x)=Cx+k$ |
| $f(x)=x$ | $F(x)=\dfrac{x^{2}}{2}+k$ |
| $f(x)=x^{2}$ | $F(x)=\dfrac{x^{3}}{3}+k$ |
| $f(x)=x^{3}$ | $F(x)=\dfrac{x^{4}}{4}+k$ |
| $f(x)=x^{n}$, $n\in\mathbb{N}^{*}$ | $F(x)=\dfrac{x^{n+1}}{n+1}+k$ |
| $f(x)=ax+b$ | $F(x)=\dfrac{ax^{2}}{2}+bx+k$ |
| $f(x)=ax^{2}+bx+c$ | $F(x)=\dfrac{ax^{3}}{3}+\dfrac{bx^{2}}{2}+cx+k$ |
| $f(x)=ax^{3}+bx^{2}+cx+d$ | $F(x)=\dfrac{ax^{4}}{4}+\dfrac{bx^{3}}{3}+\dfrac{cx^{2}}{2}+dx+k$ |

Retenir la règle : on **augmente l'exposant de 1** et on **divise par le nouvel exposant**.

Le tableau du manuel (p. 95) ne contient que des fonctions polynomiales ; pour les autres, on utilise les règles de composition ci-dessous. Par exemple $\dfrac{1}{x^{2}}=x^{-2}$ a pour primitives $x\mapsto-\dfrac{1}{x}+k$ (piège classique du signe).

## Primitives de fonctions composées

**Fonction affine à l'intérieur.** Si $F$ est une primitive de $f$ et $a\neq0$, alors $x\mapsto f(ax+b)$ a pour primitives
$$x\longmapsto \frac{F(ax+b)}{a}+k.$$

**Puissance d'une fonction.** Si $n$ est un entier relatif **différent de** $-1$ et $f$ une fonction dérivable, alors $f'\times f^{\,n}$ a pour primitives
$$x\longmapsto \frac{\big(f(x)\big)^{\,n+1}}{n+1}+k.$$

*(La condition est bien $n\neq-1$, car $n+1$ doit être non nul ; le manuel imprime « différent de 1 » p. 96 : c'est une coquille.)*

**Quotient** $\dfrac{f'}{f}$. Si $f$ est dérivable et **strictement positive**, ses primitives sont $x\mapsto\ln\big(f(x)\big)+k$ ; si $f$ est **strictement négative**, ce sont $x\mapsto\ln\big(-f(x)\big)+k$.

**Exponentielle.** Si $f$ est dérivable, $f'\mathrm{e}^{f}$ a pour primitives $x\mapsto\mathrm{e}^{f(x)}+k$.

## Trouver LA primitive : la condition initiale

Toutes les primitives diffèrent d'une constante ; pour en choisir une seule, on impose une **condition initiale** $F(x_0)=y_0$.

1. Écrire la forme générale $F(x)=\dots+k$.
2. Remplacer $x$ par $x_0$ et résoudre l'équation $F(x_0)=y_0$, d'inconnue $k$.
3. Écrire $F$ avec la valeur de $k$ trouvée, puis **vérifier en dérivant**.

*Exemple.* $f(x)=3x^{2}+4x-5$ et $F(0)=2$ : $F(x)=x^{3}+2x^{2}-5x+k$, or $F(0)=k=2$, donc $F(x)=x^{3}+2x^{2}-5x+2$ et $F(1)=0$.
