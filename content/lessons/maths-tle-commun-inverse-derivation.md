# Fonction inverse, limites, dérivation et lecture de courbes

## La fonction inverse

Définie sur $\left]-\infty\,;0\right[\cup\left]0\,;+\infty\right[$, la fonction $x\mapsto\dfrac{1}{x}$ a pour courbe une **hyperbole** à deux branches séparées.

{{fig:mathstc-fonction-inverse}}

**Comportement aux bornes.** Quand $x$ se rapproche de $0$ par valeurs positives, $\dfrac{1}{x}$ devient aussi grand que l'on veut ($\dfrac{1}{0{,}0001}=10\,000$) ; quand $x$ devient très grand, $\dfrac{1}{x}$ se rapproche de $0$ sans l'atteindre ($\dfrac{1}{10^{6}}=10^{-6}$). On s'en tient à cette description **intuitive** : aucune définition d'asymptote n'est attendue.

## Les quatre limites de la fonction inverse

Le comportement aux bornes se lit dans un **tableau de valeurs**, puis s'écrit avec la notation `lim`.

**Loin de l'origine.** Pour $x=-10$, $-1\,000$, $-100\,000$, $-2\,000\,000$, l'inverse vaut $-0{,}1$, $-0{,}001$, $-10^{-5}$, $-5\times10^{-7}$ : il s'écrase sur $0$. Même chose du côté positif. On écrit

$$\lim_{x\to+\infty}\frac{1}{x}=0 \qquad\text{et}\qquad \lim_{x\to-\infty}\frac{1}{x}=0.$$

Cela se lit : $\dfrac{1}{x}$ peut être rendu **aussi proche de $0$ que l'on veut**, pourvu que l'on choisisse $x$ assez grand. La fonction ne vaut jamais $0$ — elle s'en approche indéfiniment.

**Près de l'origine.** Pour $x=0{,}1$, $0{,}025$, $0{,}000\,08$, $0{,}000\,000\,1$, l'inverse vaut $10$, $40$, $12\,500$, $10^{7}$ : il s'envole. Avec les mêmes valeurs négatives, il plonge. Les deux côtés ne donnent pas le même résultat, il faut donc **préciser par où l'on arrive** :

$$\lim_{\substack{x\to0\\x>0}}\frac{1}{x}=+\infty \qquad\text{et}\qquad \lim_{\substack{x\to0\\x<0}}\frac{1}{x}=-\infty.$$

Sans cette précision, la limite en $0$ n'existe pas. Et $+\infty$ n'est **pas un nombre** : on n'écrit jamais $\dfrac{1}{+\infty}$.

## Vérifier une limite par un algorithme de seuil

« Aussi grand que l'on veut » se teste : on fixe un seuil $A$ et on cherche à partir de quel $x$ on a $\dfrac{1}{x}>A$. En essayant $x=10^{-N}$ pour $N=1$, $2$, $3$… :

```python
A = float(input("Entrer un nombre positif"))
x = 0.1
N = 1
while 1/x < A:
    N = N + 1
    x = 1/10**N
print("x =", x)
```

Comme $\dfrac{1}{x}=10^{N}$, la boucle s'arrête au premier $N$ tel que $10^{N}>A$. Pour $A=350\,000$ : $10^{5}=100\,000$ ne suffit pas, $10^{6}=1\,000\,000$ dépasse — donc $N=6$ et $x=10^{-6}$.

Quel que soit le seuil demandé, on finit par le franchir : c'est précisément ce que dit $\displaystyle\lim_{\substack{x\to0\\x>0}}\frac{1}{x}=+\infty$.

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
