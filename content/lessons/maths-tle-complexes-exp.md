# Complexes sous forme exponentielle

*(Prérequis de première : forme algébrique, conjugué, module, plan complexe — voir la leçon « Nombres complexes ».)*

## L'exponentielle complexe

Pour tout réel $\theta$, on **pose**
$$\mathrm{e}^{i\theta}=\cos(\theta)+i\sin(\theta),$$
et on admet que cette exponentielle possède les mêmes propriétés algébriques que l'exponentielle réelle.

Comme $\cos^{2}(\theta)+\sin^{2}(\theta)=1$, on a $\left|\mathrm{e}^{i\theta}\right|=1$ : les points d'affixe $\mathrm{e}^{i\theta}$ décrivent exactement le **cercle trigonométrique**.

Tout complexe **non nul** s'écrit alors
$$z=r\,\mathrm{e}^{i\theta}\qquad\text{avec}\qquad r=\left|z\right|>0\quad\text{et}\quad\theta=\arg(z)\ [2\pi].$$

{{fig:maths-plan-complexe}}

## De la forme algébrique à la forme exponentielle

Pour $z=a+ib$ non nul :

1. calculer le module $r=\sqrt{a^{2}+b^{2}}$ ;
2. repérer le **quadrant** du point image (signes de $a$ et de $b$) ;
3. résoudre **les deux** équations $\cos(\theta)=\dfrac{a}{r}$ et $\sin(\theta)=\dfrac{b}{r}$ ;
4. écrire $z=r\,\mathrm{e}^{i\theta}$.

L'erreur classique est de n'utiliser que le cosinus : deux angles opposés ont le même cosinus. Le cercle des angles remarquables permet de conclure en une ligne.

{{fig:maths-cercle-angles}}

| $z$ | $r$ | $\theta$ | Forme exponentielle |
|---|---|---|---|
| $\sqrt{3}+i$ | $2$ | $\dfrac{\pi}{6}$ | $2\,\mathrm{e}^{i\pi/6}$ |
| $\sqrt{3}-i$ | $2$ | $-\dfrac{\pi}{6}$ | $2\,\mathrm{e}^{-i\pi/6}$ |
| $1+i$ | $\sqrt{2}$ | $\dfrac{\pi}{4}$ | $\sqrt{2}\,\mathrm{e}^{i\pi/4}$ |
| $-2\sqrt{3}+2i$ | $4$ | $\dfrac{5\pi}{6}$ | $4\,\mathrm{e}^{i5\pi/6}$ |
| $2i$ | $2$ | $\dfrac{\pi}{2}$ | $2\,\mathrm{e}^{i\pi/2}$ |
| $-3$ | $3$ | $\pi$ | $3\,\mathrm{e}^{i\pi}$ |

**Retour à la forme algébrique** : $r\,\mathrm{e}^{i\theta}=r\cos(\theta)+ir\sin(\theta)$.
Par exemple $4\,\mathrm{e}^{i2\pi/3}=4\left(-\dfrac{1}{2}+i\dfrac{\sqrt{3}}{2}\right)=-2+2i\sqrt{3}$.

## Lire une affixe sur une figure

Les sujets fournissent souvent un plan complexe muni de cercles concentriques : on **lit** le module sur les cercles et l'argument sur l'angle formé avec l'axe réel, sans aucun calcul.

{{fig:mathstle-plan-complexe-cercles}}

## Produit, quotient, puissance

$$r\,\mathrm{e}^{i\alpha}\times r'\,\mathrm{e}^{i\beta}=rr'\,\mathrm{e}^{i(\alpha+\beta)}\qquad\frac{r\,\mathrm{e}^{i\alpha}}{r'\,\mathrm{e}^{i\beta}}=\frac{r}{r'}\,\mathrm{e}^{i(\alpha-\beta)}\qquad\left(r\,\mathrm{e}^{i\theta}\right)^{n}=r^{n}\,\mathrm{e}^{in\theta}$$

**Les modules se multiplient, les arguments s'ajoutent.** La dernière égalité, avec $r=1$, est la **formule de Moivre** : $\left(\cos\theta+i\sin\theta\right)^{n}=\cos(n\theta)+i\sin(n\theta)$. Enfin $\overline{r\,\mathrm{e}^{i\theta}}=r\,\mathrm{e}^{-i\theta}$.

Règle de choix : **somme et différence en forme algébrique, produit et quotient en forme exponentielle.**

*Exemple résolu.* $z_{1}=1-i\sqrt{3}$ et $z_{2}=\sqrt{2}\,\mathrm{e}^{i\pi/4}$ ; nature de $Z=z_{1}^{3}\times z_{2}^{2}$ ?
$z_{1}=2\,\mathrm{e}^{-i\pi/3}$, donc $z_{1}^{3}=8\,\mathrm{e}^{-i\pi}=-8$ et $z_{2}^{2}=2\,\mathrm{e}^{i\pi/2}=2i$.
Ainsi $Z=-16i$ : un **imaginaire pur**. Développer $z_{1}^{3}$ sous forme algébrique aurait pris dix fois plus de temps.

En développant $\mathrm{e}^{i(a+b)}=\mathrm{e}^{ia}\,\mathrm{e}^{ib}$, on retrouve les formules d'addition et de duplication, et par suite la linéarisation $\cos^{2}(a)=\dfrac{1+\cos(2a)}{2}$, utile pour calculer des primitives.

## Application : l'impédance complexe

En électricité, on note $\mathrm{j}$ le nombre imaginaire, pour ne pas le confondre avec l'intensité $i$. En régime sinusoïdal de pulsation $\omega$, à chaque dipôle on associe une **impédance complexe** :

| Dipôle | Impédance $\underline{Z}$ | Module | Argument |
|---|---|---|---|
| Résistor | $R$ | $R$ | $0$ |
| Bobine | $\mathrm{j}L\omega$ | $L\omega$ | $\dfrac{\pi}{2}$ |
| Condensateur | $\dfrac{1}{\mathrm{j}C\omega}$ | $\dfrac{1}{C\omega}$ | $-\dfrac{\pi}{2}$ |

En série, les impédances complexes **s'ajoutent**. Le module donne l'impédance en ohms ($U=\left|\underline{Z}\right|\times I$ en valeurs efficaces), et l'argument donne le **déphasage** de la tension par rapport au courant.

*Exemple.* $R=30\ \Omega$ et $L\omega=40\ \Omega$ en série : $\underline{Z}=30+40\mathrm{j}$, donc $\left|\underline{Z}\right|=\sqrt{30^{2}+40^{2}}=50\ \Omega$ et $\varphi\approx53{,}1^{\circ}\approx0{,}927$ rad. Le facteur de puissance vaut $\cos(\varphi)=0{,}6$. Noter que $50\neq30+40$ : ce sont les impédances **complexes** qui s'ajoutent, pas leurs modules.
