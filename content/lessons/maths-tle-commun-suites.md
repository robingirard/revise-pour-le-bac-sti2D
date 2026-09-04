# Suites arithmétiques, suites géométriques et leurs sommes

## Deux modèles d'évolution

| | Arithmétique | Géométrique (termes positifs) |
|---|---|---|
| Récurrence | $u_{n+1}=u_{n}+r$ | $u_{n+1}=q\times u_{n}$ |
| Terme général | $u_{n}=u_{0}+nr$ | $u_{n}=u_{0}\times q^{n}$ |
| Opération | on **ajoute** $r$ | on **multiplie** par $q$ |
| Langage courant | croissance **linéaire** | croissance **exponentielle** |

Attention au vocabulaire : la raison $q$ d'une suite géométrique modélisant une évolution de $t\ \%$ est le **coefficient multiplicateur** $1+\dfrac{t}{100}$, pas le taux. Perdre $1{,}5\ \%$ par an, c'est $q=0{,}985$, et non $-0{,}015$.

## Reconnaître trois termes consécutifs

- Arithmétique : le terme du milieu est la **moyenne arithmétique** des deux autres, $b=\dfrac{a+c}{2}$.
- Géométrique : le terme du milieu est la **moyenne géométrique**, c'est-à-dire $b^{2}=ac$ (termes positifs).

*Exemples.* $7$ ; $12$ ; $17$ : $\dfrac{7+17}{2}=12$, c'est arithmétique. $3$ ; $6$ ; $12$ : $6^{2}=36=3\times12$, c'est géométrique — et pas arithmétique, car les écarts valent $3$ puis $6$.

{{fig:mathstc-suite-batons}}

## Sommes de termes consécutifs

**Arithmétique** : $\text{nombre de termes}\times\dfrac{\text{premier}+\text{dernier}}{2}$, par exemple $1+2+\cdots+60=60\times\dfrac{1+60}{2}=1\,830$.

**Géométrique** de raison $q\neq1$ : $\text{premier terme}\times\dfrac{1-q^{N}}{1-q}$ où $N$ est le nombre de termes, par exemple $\displaystyle\sum_{k=0}^{9}2^{k}=\dfrac{1-2^{10}}{1-2}=1\,023$. L'erreur la plus fréquente porte sur $N$ : de $u_{0}$ à $u_{9}$, il y a **dix** termes.

*Exemple résolu — placement à versements réguliers.* On verse $1\,200$ € au début de chaque année à $3\ \%$. Le premier versement travaille $10$ ans, le dernier $1$ an :

$$S=1\,200\times1{,}03\times\frac{1{,}03^{10}-1}{0{,}03}\approx1\,200\times11{,}8078\approx14\,169\ \text{€},$$

pour $12\,000$ € effectivement versés.

## La notation $\Sigma$

$\displaystyle\sum_{k=1}^{n}a_{k}$ se lit « somme des $a_{k}$ pour $k$ allant de $1$ à $n$ ». Elle sert aussi pour des sommes qui ne sont ni arithmétiques ni géométriques :

$$\sum_{k=1}^{10}k^{2}=385,\qquad \sum_{k=1}^{5}k^{3}=225,\qquad \sum_{k=1}^{6}\frac{1}{k}=\frac{147}{60}=2{,}45.$$

En Python, cette notation se traduit par un **accumulateur** dans une boucle :

```python
def somme_carres(n):
    S = 0                      # initialisation de l'accumulateur
    for k in range(1, n + 1):  # compteur de 1 à n
        S = S + k**2           # accumulation
    return S                   # sortie, hors de la boucle
```

## Linéaire ou exponentiel ?

Une production part de $400$ unités. Modèle arithmétique : $400+60n$, qui vaut $640$ en $n=4$ et $700$ en $n=5$. Modèle géométrique : $400\times1{,}12^{n}$, qui vaut $629{,}4$ en $n=4$ et $704{,}9$ en $n=5$.

{{fig:mathstc-suites-lin-vs-geo}}

Le modèle exponentiel démarre plus lentement puis dépasse définitivement le modèle linéaire : ici à partir de la cinquième année. C'est une règle générale dès que $q>1$.

**Esprit critique.** Une croissance de $6\ \%$ par mois multiplie la production par $7{,}7$ en trois ans. Aucun atelier ne peut suivre indéfiniment : un modèle exponentiel n'est valable que sur un horizon limité.
