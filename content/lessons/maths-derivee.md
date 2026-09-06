# Dérivation

## Le nombre dérivé

Soit $f$ une fonction définie sur un intervalle $I$ et $a$ un réel de $I$. Pour $h\neq0$ tel que $a+h$ appartienne à $I$, le **taux d'accroissement** de $f$ entre $a$ et $a+h$ est

$$\frac{f(a+h)-f(a)}{h}.$$

Lorsque ce quotient admet une limite finie $\ell$ quand $h$ tend vers $0$, on dit que $f$ est **dérivable en $a$** et on note $f'(a)=\ell$. Le réel $f'(a)$ s'appelle le **nombre dérivé** de $f$ en $a$.

{{fig:maths-nombre-derive}}

**Lecture graphique.** Le taux d'accroissement est le coefficient directeur de la sécante $(AM)$, où $A$ est le point de la courbe d'abscisse $a$ et $M$ celui d'abscisse $a+h$. Quand $M$ se rapproche de $A$, la sécante pivote autour de $A$ et vient se confondre avec la **tangente** en $A$ :

**$f'(a)$ est le coefficient directeur de la tangente à la courbe au point d'abscisse $a$.**

## L'équation de la tangente

La tangente passe par $A\big(a\,;f(a)\big)$ et a pour coefficient directeur $f'(a)$, d'où

$$y=f'(a)(x-a)+f(a).$$

*Exemple.* $f(x)=x^{2}$ en $a=2$ : $f(2)=4$ et $f'(2)=4$, donc $y=4(x-2)+4$, soit $y=4x-4$.

**Méthode.** Calculer $f'$, puis les deux nombres $f(a)$ et $f'(a)$, les reporter dans la formule, développer, et vérifier qu'en $x=a$ on retrouve bien $f(a)$.

## La fonction dérivée et les dérivées usuelles

Si $f$ est dérivable en tout point d'un intervalle $I$, la fonction $x\mapsto f'(x)$ est la **fonction dérivée** de $f$ sur $I$.

| Fonction $f(x)$ | Dérivée $f'(x)$ | Sur |
|---|---|---|
| $k$ (constante) | $0$ | $\mathbb{R}$ |
| $x$ | $1$ | $\mathbb{R}$ |
| $x^{n}$, $n$ entier $\geqslant1$ | $nx^{n-1}$ | $\mathbb{R}$ |
| $\dfrac{1}{x}$ | $-\dfrac{1}{x^{2}}$ | $\mathbb{R}^{*}$ |
| $\sqrt{x}$ | $\dfrac{1}{2\sqrt{x}}$ | $\left]0\,;+\infty\right[$ |
| $\mathrm{e}^{x}$ | $\mathrm{e}^{x}$ | $\mathbb{R}$ |
| $\cos(x)$ | $-\sin(x)$ | $\mathbb{R}$ |
| $\sin(x)$ | $\cos(x)$ | $\mathbb{R}$ |

Deux pièges classiques : la fonction racine carrée est définie en $0$ mais **n'y est pas dérivable** (tangente verticale) ; et c'est la dérivée du **cosinus** qui porte le signe moins.

## Opérations sur les dérivées

Pour $u$ et $v$ dérivables sur $I$ et $k$ un réel :

$$(u+v)'=u'+v' \qquad\qquad (ku)'=ku'$$

$$(uv)'=u'v+uv' \qquad\qquad \left(\frac{u}{v}\right)'=\frac{u'v-uv'}{v^{2}}\quad(v\neq0)$$

Dans la formule du produit, on dérive **un facteur à la fois** ; dans celle du quotient, l'ordre $u'v-uv'$ du numérateur est essentiel.

*Exemple résolu.* $f(x)=(3x+1)\left(x^{2}-2\right)$ est un **produit** :
$f'(x)=3\left(x^{2}-2\right)+(3x+1)\times2x=3x^{2}-6+6x^{2}+2x=9x^{2}+2x-6$.

*Exemple résolu.* $f(x)=\dfrac{2x-1}{x+3}$ sur $\left]-3\,;+\infty\right[$ est un **quotient** :
$f'(x)=\dfrac{2(x+3)-(2x-1)\times1}{(x+3)^{2}}=\dfrac{2x+6-2x+1}{(x+3)^{2}}=\dfrac{7}{(x+3)^{2}}$, strictement positive : $f$ est croissante.

## Deux composées à connaître

Ces deux formules servent en permanence en physique et en 2I2D. Pour tous réels $a$, $b$, $\omega$ et $\varphi$ :

$$\left(\mathrm{e}^{ax+b}\right)'=a\,\mathrm{e}^{ax+b}$$

$$\left(\cos(\omega t+\varphi)\right)'=-\omega\sin(\omega t+\varphi) \qquad \left(\sin(\omega t+\varphi)\right)'=\omega\cos(\omega t+\varphi)$$

Le facteur qui « sort » est toujours la dérivée de l'expression intérieure : $a$ ou $\omega$, jamais l'expression entière. C'est l'oubli le plus fréquent.

*Exemple.* $u(t)=12\cos(100t+0{,}5)$ donne $u'(t)=12\times(-100)\sin(100t+0{,}5)=-1\,200\sin(100t+0{,}5)$.

## Signe de la dérivée et sens de variation

Soit $f$ dérivable sur un intervalle $I$ :

- si $f'(x)>0$ sur $I$, alors $f$ est **strictement croissante** sur $I$ ;
- si $f'(x)<0$ sur $I$, alors $f$ est **strictement décroissante** sur $I$ ;
- si $f'(x)=0$ sur tout $I$, alors $f$ est **constante** sur $I$.

**Ne pas confondre** : le sens de variation de $f$ traduit le *signe* de $f'$, jamais les *variations* de $f'$.

{{fig:maths-tangente-variations}}

**Méthode pour dresser un tableau de variations.**

1. Déterminer l'intervalle d'étude et vérifier que $f$ y est dérivable.
2. Calculer $f'(x)$.
3. Factoriser $f'(x)$, ou résoudre l'équation $f'(x)=0$.
4. Déterminer le signe de $f'(x)$ sur l'intervalle.
5. Reporter ce signe dans la première ligne du tableau, puis tracer les flèches.
6. Calculer les valeurs de $f$ aux bornes et aux extremums.

## Extremums

Si $f'$ s'annule **en changeant de signe** en $a$, alors $f$ admet un extremum local en $a$ : un **maximum** si $f'$ passe du $+$ au $-$, un **minimum** si elle passe du $-$ au $+$. La tangente y est horizontale.

La réciproque est fausse : $f'(a)=0$ ne suffit pas. Contre-exemple : $f(x)=x^{3}$ vérifie $f'(0)=0$, mais $f'(x)=3x^{2}$ reste positive : la fonction est croissante et n'a aucun extremum.

*Exemple.* $f(x)=-2x^{2}+12x-7$ : $f'(x)=-4x+12$ s'annule en $x=3$, positive avant, négative après. Maximum en $x=3$, de valeur $f(3)=11$.

## Applications techniques

- **Cinématique.** La vitesse est la dérivée de la position par rapport au temps, $v(t)=x'(t)$ ; l'accélération est la dérivée de la vitesse, $a(t)=v'(t)$.
- **Électricité.** L'intensité est le débit de charge : $i(t)=\dfrac{\mathrm{d}q}{\mathrm{d}t}=q'(t)$, ce que confirme l'unité, $1$ A $=1$ $\mathrm{C}\cdot\mathrm{s}^{-1}$.
- **Optimisation.** Pour trouver la dimension qui rend une grandeur maximale (volume d'un caisson, section d'une poutre, rendement), on met la grandeur en équation en fonction d'une variable, on précise l'intervalle où le problème a un sens, puis on cherche où la dérivée change de signe.

Enfin, la dérivation est l'opération que les **primitives** viennent inverser : $F$ est une primitive de $f$ lorsque $F'=f$. Tout ce tableau se lit donc aussi de droite à gauche.
