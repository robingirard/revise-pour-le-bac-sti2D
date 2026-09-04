# Fonction inverse, dérivation et lecture de courbes

## La fonction inverse

Définie sur $\left]-\infty\,;0\right[\cup\left]0\,;+\infty\right[$, la fonction $x\mapsto\dfrac{1}{x}$ a pour courbe une **hyperbole** à deux branches séparées.

{{fig:mathstc-fonction-inverse}}

**Comportement aux bornes.** Quand $x$ se rapproche de $0$ par valeurs positives, $\dfrac{1}{x}$ devient aussi grand que l'on veut ($\dfrac{1}{0{,}0001}=10\,000$) ; quand $x$ devient très grand, $\dfrac{1}{x}$ se rapproche de $0$ sans l'atteindre ($\dfrac{1}{10^{6}}=10^{-6}$). On s'en tient à cette description **intuitive** : aucune définition d'asymptote n'est attendue.

## La dérivée, retrouvée par le taux de variation

Pour $x\neq0$ et $h\neq0$ :

$$\frac{\frac{1}{x+h}-\frac{1}{x}}{h}=\frac{\frac{x-(x+h)}{x(x+h)}}{h}=\frac{-h}{h\,x(x+h)}=\frac{-1}{x(x+h)}\ \xrightarrow[h\to0]{}\ -\frac{1}{x^{2}}.$$

Cette dérivée est **toujours strictement négative** : la fonction inverse décroît sur chacune de ses deux branches, mais pas sur leur réunion.

| Fonction | Dérivée |
|---|---|
| $x\mapsto k$ | $x\mapsto0$ |
| $x\mapsto x^{n}$ | $x\mapsto nx^{n-1}$ |
| $x\mapsto\dfrac{k}{x}$ | $x\mapsto-\dfrac{k}{x^{2}}$ |
| $x\mapsto u+v$ | $x\mapsto u'+v'$ |

## Combinaisons linéaires : la capacité exigible

On étudie les fonctions du type $f(x)=ax+\dfrac{b}{x}$, plus généralement une combinaison de la fonction inverse et d'un polynôme de degré au plus $3$.

*Exemple résolu.* $f(x)=2x+\dfrac{8}{x}$ sur $\left]0\,;+\infty\right[$ donne $f'(x)=2-\dfrac{8}{x^{2}}=\dfrac{2x^{2}-8}{x^{2}}$. Le dénominateur étant positif, $f'$ a le signe de $2x^{2}-8$, qui s'annule en $x=2$.

| $x$ | $0$ | | $2$ | | $+\infty$ |
|---|---|---|---|---|---|
| signe de $f'(x)$ | | $-$ | $0$ | $+$ | |
| variations de $f$ | | décroissante | $8$ | croissante | |

Le minimum vaut $f(2)=4+4=8$. *Autre exemple.* $g(x)=x^{2}-\dfrac{1}{x}$ : $g'(x)=2x+\dfrac{1}{x^{2}}$, somme de deux termes strictement positifs, donc $g$ est croissante. Attention au double changement de signe : la dérivée de $-\dfrac{1}{x}$ est $+\dfrac{1}{x^{2}}$.

## Tangente

La tangente au point d'abscisse $a$ a pour équation $y=f'(a)(x-a)+f(a)$. Pour $f(x)=\dfrac{1}{x}$ en $a=2$ : $f(2)=0{,}5$ et $f'(2)=-\dfrac{1}{4}$, donc $y=-\dfrac{1}{4}(x-2)+\dfrac{1}{2}=-\dfrac{1}{4}x+1$.

## Coût moyen et prix unitaire

Dès qu'il y a des **frais fixes**, la grandeur ramenée à l'unité fait apparaître un terme en $\dfrac{1}{q}$.

*Exemple résolu.* Coût total $C(q)=0{,}5q^{2}+40q+800$ euros pour $q$ pièces, donc

$$C_{M}(q)=\frac{C(q)}{q}=0{,}5q+40+\frac{800}{q},\qquad C_{M}'(q)=0{,}5-\frac{800}{q^{2}}.$$

$C_{M}'(q)=0$ donne $q^{2}=1\,600$, soit $q=40$ pièces, et $C_{M}(40)=20+40+20=80$ €.

{{fig:mathstc-cout-moyen}}

La courbe en U s'interprète directement : à gauche, les frais fixes sont répartis sur trop peu de pièces ; à droite, c'est le terme $0{,}5q$ qui pèse. *Prix unitaire.* Avec $p(n)=3+\dfrac{240}{n}$, l'inéquation $p(n)<5$ donne $n>120$, donc $121$ pièces au minimum.

## Lire un tableau de variations

Les **variations** de $f$ traduisent le **signe** de $f'$, jamais ses variations. Un minimum correspond à un changement de signe de $f'$ du négatif vers le positif, un maximum au changement inverse.
