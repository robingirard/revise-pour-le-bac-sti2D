# Probabilités conditionnelles, variables aléatoires et loi binomiale

## Conditionner, et lire un arbre

Pour $P(A)\neq0$ : $P_{A}(B)=\dfrac{P(A\cap B)}{P(A)}$, donc $P(A\cap B)=P(A)\times P_{A}(B)$.

{{fig:mathstc-arbre-probas}}

Trois règles suffisent : la somme des poids des branches issues d'un même nœud vaut $1$ ; la probabilité d'un **chemin** est le **produit** des poids de ses branches ; la probabilité d'un événement est la **somme** des chemins qui y mènent (formule des probabilités totales).

*Exemple résolu.* La ligne A fournit $60\ \%$ des pièces, dont $3\ \%$ de défectueuses ; la ligne B fournit $40\ \%$ des pièces, dont $5\ \%$ de défectueuses.

$$P(A\cap D)=0{,}60\times0{,}03=0{,}018,\quad P(B\cap D)=0{,}40\times0{,}05=0{,}020,\quad P(D)=0{,}038.$$

**Conditionnement inverse** : si la pièce est défectueuse, la probabilité qu'elle vienne de A est $P_{D}(A)=\dfrac{0{,}018}{0{,}038}\approx0{,}474$. À retenir : $P_{D}(A)$ et $P_{A}(D)=0{,}03$ n'ont rien à voir, on ne peut pas échanger les rôles.

## Indépendance

$A$ et $B$, de probabilités non nulles, sont **indépendants** lorsque $P_{A}(B)=P(B)$, ce qui équivaut à $P(A\cap B)=P(A)\times P(B)$. Ici $P_{A}(D)=0{,}03$ alors que $P(D)=0{,}038$ : ils ne le sont pas.

## Espérance d'une variable aléatoire discrète

$$E(X)=\sum_{i}x_{i}\,p_{i}.$$

*Exemple.* $X$ prend les valeurs $-2$ ; $0$ ; $5$ ; $20$ avec les probabilités $0{,}45$ ; $0{,}30$ ; $0{,}20$ ; $0{,}05$ (somme $=1$), donc $E(X)=-0{,}9+0+1+1=1{,}1$. Sur un très grand nombre de parties, le gain **moyen** vaut environ $1{,}10$ € : ce n'est ni le gain le plus probable, ni un gain garanti.

## Coefficients binomiaux et triangle de Pascal

$\binom{n}{k}$ est le nombre de chemins d'un arbre de $n$ épreuves comportant exactement $k$ succès. On le lit dans le triangle de Pascal (exigible pour $n\leqslant10$) :

ligne $4$ : $1$ ; $4$ ; $6$ ; $4$ ; $1$ — ligne $5$ : $1$ ; $5$ ; $10$ ; $10$ ; $5$ ; $1$ — ligne $6$ : $1$ ; $6$ ; $15$ ; $20$ ; $15$ ; $6$ ; $1$.

Chaque coefficient est la somme des deux situés juste au-dessus, c'est la **formule de Pascal** $\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}$ ; par exemple $\binom{6}{3}=\binom{5}{2}+\binom{5}{3}=10+10=20$.

## Loi binomiale

$X$ suit $\mathcal{B}(n\,;p)$ lorsqu'elle compte les succès d'une **répétition de $n$ épreuves indépendantes et identiques** de probabilité de succès $p$. Alors

$$P(X=k)=\binom{n}{k}p^{k}(1-p)^{n-k},\qquad E(X)=np\ \text{(admise)}.$$

Cas immédiats : $P(X=0)=(1-p)^{n}$ et $P(X=n)=p^{n}$ (un seul chemin chacun), $P(X=1)=n\,p\,(1-p)^{n-1}$. *Exemple résolu.* Pour $X$ suivant $\mathcal{B}(20\,;0{,}1)$ : $P(X=0)\approx0{,}122$, $P(X=1)\approx0{,}270$, $P(X=2)\approx0{,}285$ et $P(X=3)\approx0{,}190$, d'où $P(X\geqslant2)=1-0{,}122-0{,}270\approx0{,}608$ et $E(X)=2$.

{{fig:mathstc-binomiale-batons}}

**Contre-exemple à retenir.** Un tirage **sans remise** dans un petit lot ne relève pas de la loi binomiale : les épreuves ne sont ni indépendantes ni identiques.

## Simuler en Python

```python
from random import random

def binomiale(n, p):
    succes = 0
    for _ in range(n):
        if random() < p:     # épreuve de Bernoulli de paramètre p
            succes = succes + 1
    return succes
```

En répétant cette fonction $10\,000$ fois et en comptant les résultats égaux à $k$, on retrouve $P(X=k)$ aux fluctuations près : c'est le lien entre la simulation de première et la loi calculée en terminale.
