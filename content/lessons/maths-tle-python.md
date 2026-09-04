# Python et méthodes numériques

Le programme ne demande que quatre situations : **rectangles**, **Monte-Carlo**, **balayage ou dichotomie**, **méthode d'Euler**. On attend surtout de savoir **lire** un script court et le **compléter**, pas de l'écrire de zéro.

## Les trois réflexes de lecture

- `range(n)` produit les entiers de $0$ à $n-1$, soit **$n$ valeurs** — jamais $n+1$.
- L'**indentation** délimite les blocs. Un `return` indenté dans la boucle arrête la fonction dès le premier tour.
- Un **accumulateur** (`s = 0`) doit être initialisé **avant** la boucle, et une seule fois.

Rappel : `=` **affecte** une valeur, `==` **compare**.

## Méthode des rectangles

{{fig:mathstle-rectangles}}

```python
def aire(f, a, b, n):
    pas = (b - a) / n
    s = 0
    for i in range(n):
        s = s + f(a + i * pas)
    return s * pas
```

La fonction renvoie $\sum_{i=0}^{n-1}f(x_{i})\,\Delta x$ avec $\Delta x=\dfrac{b-a}{n}$ : ce sont les rectangles **à gauche**, car les points utilisés sont $a$, $a+\Delta x$, …, $a+(n-1)\Delta x$.

*Test à la main.* $f(x)=x$ sur $\left[0\,;1\right]$ avec $n=4$ : les points sont $0$ ; $0{,}25$ ; $0{,}5$ ; $0{,}75$, la somme des images vaut $1{,}5$, et la fonction renvoie $1{,}5\times0{,}25=0{,}375$, à comparer à la valeur exacte $0{,}5$.

**Sens de l'erreur** : pour une fonction **croissante**, les rectangles à gauche sous-estiment ; pour une fonction **décroissante**, ils surestiment. Ainsi, pour $f(x)=\mathrm{e}^{-x}$ sur $\left[0\,;1\right]$ avec $n=100$, on obtient $0{,}6353$ alors que la valeur exacte est $1-\mathrm{e}^{-1}\approx0{,}6321$.

**Erreurs à repérer** : oublier `* pas` (résultat sans unité d'aire), ou écrire `range(n + 1)` (un rectangle de trop, qui sort de l'intervalle).

*Variante Monte-Carlo* : on tire $N$ points au hasard dans un rectangle contenant le domaine, et l'aire est estimée par $\text{aire du rectangle}\times\dfrac{\text{points sous la courbe}}{N}$.

## Méthode d'Euler

On approche la courbe d'une solution d'équation différentielle par une **ligne brisée** : à chaque pas, on avance le long de la tangente.

$$y_{k+1}=y_{k}+h\times y'_{k}$$

{{fig:mathstle-euler}}

Pour $y'=y$ avec $y(0)=1$, dont la solution exacte est $\mathrm{e}^{x}$ :

```python
def euler(h, n):
    x, y = 0, 1
    for k in range(n):
        y = y + h * y
        x = x + h
    return y
```

Comme $y_{k+1}=(1+h)\,y_{k}$, la suite est **géométrique** de raison $1+h$ : on peut vérifier le programme à la main par $y_{n}=(1+h)^{n}$.

| Pas $h$ | Nombre d'étapes | Valeur renvoyée | Écart à $\mathrm{e}\approx2{,}718$ |
|---|---|---|---|
| $0{,}1$ | $10$ | $1{,}1^{10}\approx2{,}594$ | $0{,}125$ |
| $0{,}01$ | $100$ | $1{,}01^{100}\approx2{,}705$ | $0{,}013$ |

Diviser le pas par $10$ divise l'erreur par environ $10$. Le résultat est **toujours inférieur** à $\mathrm{e}^{x}$ : l'exponentielle est convexe, donc sa courbe reste au-dessus de chacune de ses tangentes.

## Dichotomie

On cherche une solution de $f(x)=0$ sur $\left[a\,;b\right]$, sachant que $f(a)$ et $f(b)$ sont de **signes contraires**.

```python
def dichotomie(f, a, b, p):
    while b - a > p:
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return (a + b) / 2
```

À chaque tour, l'amplitude est **divisée par deux** : partant de $\left[1\,;2\right]$, elle vaut $\dfrac{1}{2^{n}}$ après $n$ étapes, donc $7$ étapes suffisent pour descendre sous $0{,}01$ et $10$ étapes pour diviser l'amplitude par $1\,024$.

Le **balayage** est la variante naïve : on avance d'un pas fixe jusqu'au changement de signe. Plus simple à écrire, mais beaucoup plus lent.

On choisit une boucle `for` quand le nombre de tours est connu à l'avance (rectangles, Euler) et une boucle `while` quand on s'arrête sur une **condition de précision** (dichotomie, balayage).
