# Dériver, varier, tendre vers

## Composer deux fonctions

Composer, c'est enchaîner : on applique d'abord $u$, puis $v$. La fonction obtenue se note $v\circ u$ et vaut $\left(v\circ u\right)(x)=v\left(u(x)\right)$.

{{fig:mathstle-composee-arbre}}

**Dérivée d'une composée** — la formule qui engendre toutes les autres :

$$\left(v\circ u\right)'=u'\times\left(v'\circ u\right)\qquad\text{c'est-à-dire}\qquad\left(v\left(u(x)\right)\right)'=u'(x)\times v'\left(u(x)\right).$$

On dérive « de l'extérieur vers l'intérieur », **sans oublier** le facteur $u'(x)$ : c'est l'oubli le plus fréquent.

## Le tableau à connaître par cœur

| Fonction | Dérivée | Exemple |
|---|---|---|
| $\mathrm{e}^{kx}$ | $k\,\mathrm{e}^{kx}$ | $\left(\mathrm{e}^{-0{,}5t}\right)'=-0{,}5\,\mathrm{e}^{-0{,}5t}$ |
| $\mathrm{e}^{u}$ | $u'\,\mathrm{e}^{u}$ | $\left(\mathrm{e}^{3x^{2}}\right)'=6x\,\mathrm{e}^{3x^{2}}$ |
| $\ln(u)$, $u>0$ | $\dfrac{u'}{u}$ | $\left(\ln(4x-7)\right)'=\dfrac{4}{4x-7}$ |
| $u^{n}$, $n$ entier relatif | $n\,u'\,u^{n-1}$ | $\left((2x+5)^{-3}\right)'=-6(2x+5)^{-4}$ |
| $\cos(u)$ | $-u'\sin(u)$ | $\left(\cos(2t)\right)'=-2\sin(2t)$ |
| $\sin(u)$ | $u'\cos(u)$ | $\left(\sin(3x^{2}+1)\right)'=6x\cos(3x^{2}+1)$ |

Rappels de première, toujours utiles : $(uv)'=u'v+uv'$ et $\left(\dfrac{u}{v}\right)'=\dfrac{u'v-uv'}{v^{2}}$.

*Exemple résolu.* $f(x)=\mathrm{e}^{2x}(-3x+1)$ est un **produit** :
$f'(x)=2\mathrm{e}^{2x}(-3x+1)+\mathrm{e}^{2x}\times(-3)=\mathrm{e}^{2x}\left(-6x+2-3\right)=\mathrm{e}^{2x}(-6x-1)$.

*Exemple résolu.* $h(x)=\dfrac{\mathrm{e}^{3x}}{x^{2}}$ sur $\left]0\,;+\infty\right[$ est un **quotient** :
$h'(x)=\dfrac{3\mathrm{e}^{3x}x^{2}-2x\,\mathrm{e}^{3x}}{x^{4}}=\dfrac{x\,\mathrm{e}^{3x}(3x-2)}{x^{4}}=\dfrac{\mathrm{e}^{3x}(3x-2)}{x^{3}}$.

## Étudier les variations

1. Déterminer l'ensemble de définition et vérifier que $f$ est dérivable.
2. Calculer $f'(x)$ en identifiant la forme (produit, quotient, composée).
3. **Factoriser** $f'(x)$ pour faire apparaître un facteur de signe connu.
4. Étudier le signe de $f'(x)$, puis dresser le tableau de variations.
5. Calculer les extremums et les limites aux bornes.

L'étape 3 est la clé : un facteur $\mathrm{e}^{u(x)}$ est **toujours strictement positif**, donc le signe de $f'$ est celui du facteur restant.

*Exemple résolu.* $f(x)=(8x+1)\mathrm{e}^{-x}$ sur $\left[0\,;+\infty\right[$ :
$f'(x)=8\mathrm{e}^{-x}-(8x+1)\mathrm{e}^{-x}=\mathrm{e}^{-x}(7-8x)$, du signe de $7-8x$.
$f$ croît sur $\left[0\,;\dfrac{7}{8}\right]$ puis décroît ; le maximum vaut $f\left(\dfrac{7}{8}\right)=8\,\mathrm{e}^{-0{,}875}\approx3{,}33$.

{{fig:mathstle-courbe-8x1expmx}}

**Ne pas confondre** : le *sens de variation de $f$* traduit le **signe de $f'$**, jamais les variations de $f'$.

## Croissances comparées

En $+\infty$, l'exponentielle l'emporte sur toute puissance de $x$. Pour tout entier $n\geqslant1$ :

$$\lim_{x\to+\infty}\frac{\mathrm{e}^{x}}{x^{n}}=+\infty\qquad\qquad\lim_{x\to+\infty}x^{n}\,\mathrm{e}^{-x}=0$$

{{fig:mathstle-croissances-comparees}}

Ces résultats s'étendent « naturellement et sans formalisme » aux fonctions $x\mapsto\dfrac{\mathrm{e}^{kx}}{x^{n}}$ et $x\mapsto x^{n}\mathrm{e}^{-kx}$ pour $k>0$. Ainsi $\lim\limits_{x\to+\infty}\dfrac{\mathrm{e}^{0{,}5x}}{x}=+\infty$ et $\lim\limits_{t\to+\infty}5t\,\mathrm{e}^{-0{,}5t}=0$.

L'erreur à éviter : une forme indéterminée $\dfrac{\infty}{\infty}$ ou $\infty\times0$ **ne vaut pas $1$**. Il faut comparer les vitesses de croissance.
