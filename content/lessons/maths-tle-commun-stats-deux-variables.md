# Séries statistiques à deux variables

## Nuage de points

Chaque individu observé fournit un couple $\left(x_{i}\,;y_{i}\right)$ placé dans un repère : l'ensemble de ces points est le **nuage**. On met en abscisse la variable explicative (celle que l'on fait varier), en ordonnée la variable expliquée. On ne relie **jamais** les points d'un nuage.

{{fig:mathstc-nuage-ajustement}}

## Ajustement affine et moindres carrés

Si le nuage est sensiblement aligné, on cherche une droite $y=ax+b$ qui le résume : **au jugé** à la règle, par la **droite de Mayer**, ou par les **moindres carrés** (calculatrice). Aucune connaissance théorique n'est exigible. Le **résidu** du point $i$ est l'écart vertical $y_{i}-\left(ax_{i}+b\right)$, et la méthode des moindres carrés cherche $(a\,;b)$ minimisant $\displaystyle\sum_{i}\left(y_{i}-\left(ax_{i}+b\right)\right)^{2}$.

*Exemple résolu.* Nuage $(1\,;3)$, $(2\,;5)$, $(3\,;8)$, $(4\,;9)$.

| Droite candidate | Résidus | Somme des carrés |
|---|---|---|
| $y=2x+1$ | $0$ ; $0$ ; $1$ ; $0$ | $1{,}00$ |
| $y=2{,}1x+0{,}5$ | $0{,}4$ ; $0{,}3$ ; $1{,}2$ ; $0{,}1$ | $1{,}70$ |
| $y=2{,}1x+1$ | $-0{,}1$ ; $-0{,}2$ ; $0{,}7$ ; $-0{,}4$ | $0{,}70$ |

La troisième l'emporte : c'est la droite des moindres carrés. Passer exactement par trois points sur quatre n'est donc pas un gage de qualité. On peut automatiser ce calcul et **balayer** une liste de couples candidats :

```python
def sce(xs, ys, a, b):
    return sum((y - (a * x + b))**2 for x, y in zip(xs, ys))

def balayage(xs, ys, candidats):
    return min(candidats, key=lambda ab: sce(xs, ys, ab[0], ab[1]))
```

## Interpoler, extrapoler

**Interpoler**, c'est estimer une valeur *à l'intérieur* de la plage des données : usage sûr. **Extrapoler**, c'est estimer *à l'extérieur* : usage risqué. Exemple : consommation de gaz ajustée par $y=-2{,}4x+58$ ($x$ en °C, $y$ en $\mathrm{m}^{3}$ par jour). En $x=9{,}5$ : $y=35{,}2$ (interpolation). En $x=-5$ : $y=70$ (extrapolation). Le coefficient $-2{,}4$ se lit « environ $2{,}4\ \mathrm{m}^{3}$ par jour de moins par degré supplémentaire ».

**Esprit critique.** Ce modèle prévoit une consommation nulle à $\dfrac{58}{2{,}4}\approx24{,}2$ °C, puis négative : il sort de son domaine de validité. Un ajustement excellent sur la plage mesurée ne dit rien de ce qui se passe en dehors.

## Changement de variable

Quand le nuage n'est pas aligné, on cherche un changement de variable qui le **linéarise**.

| Relation supposée | Changement de variable |
|---|---|
| $N=k\,a^{t}$ | $z=\log(N)$ |
| $d=k\,v^{2}$ | $u=v^{2}$ |
| $p=\dfrac{k}{t}$ | $u=\dfrac{1}{t}$ |

{{fig:mathstc-changement-variable}}

| $t$ (h) | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $N$ | $500$ | $1\,150$ | $2\,700$ | $6\,200$ | $14\,300$ |
| $z=\log(N)$ | $2{,}70$ | $3{,}06$ | $3{,}43$ | $3{,}79$ | $4{,}16$ |

*Exemple résolu — culture de bactéries.* Les $z$ progressent d'un pas presque constant : le nuage $(t\,;z)$ est aligné, et l'ajustement donne $z=0{,}364t+2{,}699$. Retour aux variables initiales :

$$N=10^{z}=10^{2{,}699}\times\left(10^{0{,}364}\right)^{t}\approx500\times2{,}31^{t}.$$

La population est multipliée par environ $2{,}31$ par heure, soit $+131\ \%$. Extrapolé à $t=24$ h, ce modèle donnerait de l'ordre de $10^{11}$ bactéries : le milieu sature bien avant.

**Droite d'étalonnage.** Usage le plus fréquent en STI2D et STL : on mesure la réponse d'un capteur pour des valeurs connues de la grandeur, on ajuste une droite, puis on s'en sert **à l'envers** pour convertir une mesure en grandeur physique. Le coefficient directeur est la **sensibilité** du capteur, en unité de sortie par unité d'entrée (par exemple mV/°C).
