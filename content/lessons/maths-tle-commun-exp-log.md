# Fonctions exponentielles de base $a$ et logarithme décimal

## Du discret au continu

Une suite géométrique $a^{0}$, $a^{1}$, $a^{2}$, ... n'est définie qu'aux rangs entiers. On la **prolonge** à toutes les valeurs positives de $x$ : c'est la fonction $x\mapsto a^{x}$, définie pour $a>0$, puis étendue aux réels négatifs en posant $a^{-x}=\dfrac{1}{a^{x}}$. Le procédé de construction est la **moyenne géométrique** : entre $a^{0}=1$ et $a^{1}=a$ on intercale $a^{1/2}=\sqrt{a}$, puis on recommence. Pour $a=0{,}88$, le coefficient d'une demi-journée est $0{,}88^{1/2}\approx0{,}938$, puisque $0{,}938^{2}\approx0{,}88$.

C'est le **modèle continu d'évolution relative constante** : $t\mapsto k\,a^{t}$ décrit une grandeur dont le taux d'évolution est le même sur toute durée de même longueur.

{{fig:mathstc-exp-base-a}}

| Fonction | $a>1$ | $0<a<1$ |
|---|---|---|
| $x\mapsto a^{x}$ | croissante | décroissante |
| $x\mapsto k\,a^{x}$ avec $k>0$ | croissante | décroissante |
| $x\mapsto k\,a^{x}$ avec $k<0$ | décroissante | croissante |

Toutes ces courbes passent par $(0\,;k)$ et gardent le signe de $k$ : $a^{x}$ n'est jamais nul.

## Propriétés algébriques (admises)

$$a^{x+y}=a^{x}a^{y},\qquad a^{x-y}=\frac{a^{x}}{a^{y}},\qquad a^{nx}=\left(a^{x}\right)^{n}\ (n\text{ entier relatif}).$$
*Exemple résolu.* $\dfrac{3^{2x}\times3^{-x}}{3^{x-4}}=3^{2x-x-(x-4)}=3^{4}=81$, quel que soit $x$.

**Taux d'évolution moyen : l'exposant $\dfrac{1}{n}$.** Si une grandeur est multipliée par $C$ en $n$ périodes, le coefficient **moyen** par période est $C^{1/n}$. Un chiffre d'affaires qui passe de $3{,}2$ à $4{,}7$ M€ en $6$ ans donne $C=1{,}468\,75$ et $C^{1/6}\approx1{,}066\,2$, soit $+6{,}6\ \%$ par an : on ne divise pas le taux global par $6$. De même, le taux mensuel équivalent à $+9\ \%$ par an vaut $1{,}09^{1/12}-1\approx+0{,}72\ \%$, un peu moins que $\dfrac{9}{12}=0{,}75\ \%$.

## Le logarithme décimal

Pour $b>0$, $\log(b)$ est **l'unique solution de l'équation $10^{x}=b$**. Donc $10^{\log(b)}=b$ et $\log\left(10^{x}\right)=x$. La fonction $\log$ est strictement croissante sur $\left]0\,;+\infty\right[$.

{{fig:mathstc-log-decimal}}

| Propriété | Formule |
|---|---|
| produit | $\log(ab)=\log(a)+\log(b)$ |
| quotient | $\log\left(\dfrac{b}{a}\right)=\log(b)-\log(a)$ |
| puissance | $\log\left(a^{n}\right)=n\log(a)$ |
| inverse | $\log\left(\dfrac{1}{b}\right)=-\log(b)$ |

**Piège majeur** : $\log(a+b)\neq\log(a)+\log(b)$. Contre-exemple : $\log(1+1)\approx0{,}30$ alors que $\log(1)+\log(1)=0$.

## Résoudre des équations et des inéquations

- $a^{x}=b$ : on applique $\log$, puis $x=\dfrac{\log(b)}{\log(a)}$. Ainsi $1{,}05^{x}=2$ donne $x\approx14{,}21$.
- $x^{a}=b$ : $\log(x)=\dfrac{\log(b)}{a}$, puis $x=10^{\log(x)}$. Ainsi $x^{3}=200$ donne $x\approx5{,}848$.
- $a^{n}<b$ avec $n$ entier : si $a<1$, alors $\log(a)<0$ et la division **retourne** l'inégalité. Ainsi $0{,}97^{n}<0{,}5$ donne $n>22{,}76$, soit $n\geqslant23$.

**Ordre de grandeur.** La partie entière de $\log(N)$ donne l'ordre de grandeur de $N$ ; pour un entier, le nombre de chiffres vaut $\lfloor\log(N)\rfloor+1$. Ainsi $\log\left(2^{100}\right)=100\log(2)\approx30{,}103$ : $2^{100}$ s'écrit avec $31$ chiffres.

## Repère semi-logarithmique (utile en STI2D)

Si $u_{n}=k\,q^{n}$, alors $\log(u_{n})=\log(k)+n\log(q)$ : en portant $\log(u_{n})$ en ordonnée, les points s'**alignent**. C'est l'outil des diagrammes de gain, du niveau sonore $L=10\log\dfrac{I}{I_{0}}$ et du pH.

{{fig:mathstc-semilog}}

## Pont avec la spécialité

En spécialité, la même construction est reprise avec la base $\mathrm{e}\approx2{,}718$ et son logarithme, le logarithme **népérien** $\ln$. L'allure des courbes et leur symétrie par rapport à la droite $y=x$ sont identiques à ce que l'on observe ici avec $10^{x}$ et $\log$ ; on a d'ailleurs $\log(x)=\dfrac{\ln(x)}{\ln(10)}$.

{{fig:mathstle-exp-ln-courbes}}
