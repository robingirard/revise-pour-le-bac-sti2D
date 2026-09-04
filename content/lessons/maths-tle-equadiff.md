# Équations différentielles

## De quoi parle-t-on ?

Une **équation différentielle** est une équation dont l'inconnue est une **fonction**, et qui relie cette fonction à sa dérivée. Une **solution** est une fonction qui vérifie l'égalité pour **toutes** les valeurs de la variable.

Deux notations coexistent, et il faut savoir lire les deux :

- $y'=ay+b$ : notation fonctionnelle, celle des mathématiques ;
- $\dfrac{\mathrm{d}v}{\mathrm{d}t}=-6{,}8\,v+7{,}5$ : notation des sciences physiques, qui **nomme la variable** et rappelle qu'une dérivée est un rapport de variations infinitésimales.

C'est la même équation. Au programme de terminale, deux types seulement : $y'=ay$ et $y'=ay+b$, avec $a$ et $b$ réels.

## Résoudre $y'=ay$

Les solutions sur $\mathbb{R}$ sont les fonctions
$$x\longmapsto k\,\mathrm{e}^{ax},\qquad k\in\mathbb{R}.$$

Vérification : $\left(k\,\mathrm{e}^{ax}\right)'=ka\,\mathrm{e}^{ax}=a\times\left(k\,\mathrm{e}^{ax}\right)$. Il y a donc une **infinité** de solutions, une par valeur de $k$.

## Résoudre $y'=ay+b$ (avec $a\neq0$)

La méthode tient en deux idées.

1. **La solution constante.** Si $y$ est constante, $y'=0$, donc $0=ay+b$, soit $y=-\dfrac{b}{a}$. C'est le **régime permanent** du système physique.
2. **On ajoute les solutions de $y'=ay$.** L'ensemble des solutions est
$$x\longmapsto k\,\mathrm{e}^{ax}-\frac{b}{a},\qquad k\in\mathbb{R}.$$

**Condition initiale.** Une seule solution vérifie une condition donnée, par exemple $y(0)=y_{0}$ : cette **unicité est admise** par le programme. On l'obtient en remplaçant $x$ par $0$ et en résolvant l'équation d'inconnue $k$.

*Exemple résolu.* $(E)\ y'=-4y+80$ avec $f(0)=100$.
Solution constante : $0=-4y+80$ donne $y=20$. Solutions : $f(t)=k\,\mathrm{e}^{-4t}+20$.
Condition initiale : $f(0)=k+20=100$, donc $k=80$ et $f(t)=80\,\mathrm{e}^{-4t}+20$.

**Variante piégeuse** : la condition peut porter sur la **dérivée**. Pour $y'=2y-0{,}5$, les solutions sont $f(x)=k\,\mathrm{e}^{2x}+0{,}25$, donc $f'(x)=2k\,\mathrm{e}^{2x}$ ; la condition $f'(0)=-3$ donne $2k=-3$, soit $k=-1{,}5$.

## Réécrire avant d'identifier

Les énoncés donnent rarement l'équation sous la forme du cours. **Premier réflexe : isoler $y'$.**

| Énoncé | Forme du cours | Solution constante |
|---|---|---|
| $y'+0{,}006y=0{,}069$ | $y'=-0{,}006y+0{,}069$ | $11{,}5$ |
| $RC\,u'+u=E$ | $u'=-\dfrac{1}{RC}u+\dfrac{E}{RC}$ | $E$ |
| $\dfrac{\mathrm{d}v}{\mathrm{d}t}=-6{,}8v+7{,}5$ | déjà correcte | $\dfrac{75}{68}\approx1{,}10$ |

## Comportement en $+\infty$

Si $a<0$, alors $\mathrm{e}^{ax}\to0$ et toute solution tend vers $-\dfrac{b}{a}$ : la courbe admet une **asymptote horizontale**, qui est le régime permanent. Le sens de variation, lui, dépend du signe de $k$ : décroissante si $k>0$, croissante si $k<0$.

{{fig:mathstle-eqdiff-asymptote}}

Si $a>0$, la solution diverge (croissance exponentielle) : c'est le cas d'un emballement, rarement souhaitable.

## Quatre modèles physiques à reconnaître

- **Charge d'un condensateur** : $RC\,u'+u=E$, donc $u(t)=E\left(1-\mathrm{e}^{-t/\tau}\right)$ avec $\tau=RC$. Au bout de $\tau$, la tension atteint $63\ \%$ de $E$ ; au bout de $5\tau$, plus de $99\ \%$.
- **Refroidissement (loi de Newton)** : la vitesse de refroidissement est proportionnelle à l'écart avec la température extérieure, d'où une équation $T'=aT+b$ et une limite $-\dfrac{b}{a}$ égale à la température du milieu.
- **Chute avec frottement fluide** : $\dfrac{\mathrm{d}v}{\mathrm{d}t}=-kv+c$ (avec $k>0$), par exemple $\dfrac{\mathrm{d}v}{\mathrm{d}t}=-6{,}8v+7{,}5$. La limite $\dfrac{c}{k}=\dfrac{7{,}5}{6{,}8}\approx1{,}10\ \mathrm{m}\cdot\mathrm{s}^{-1}$ est la **vitesse limite** ; elle ne dépend **pas** de la vitesse initiale.
- **Décroissance radioactive** : $\dfrac{\mathrm{d}N}{\mathrm{d}t}=-\lambda N$, cas $b=0$, d'où $N(t)=N_{0}\,\mathrm{e}^{-\lambda t}$ et $t_{1/2}=\dfrac{\ln(2)}{\lambda}$.

**Esprit critique.** Un modèle n'est valable que sur le domaine où il a été établi. Si le modèle prévoit une limite de $11{,}5$ °C alors que la pièce est à $23$ °C, c'est qu'il cesse d'être applicable au bout de quelques minutes — l'épreuve attend ce genre de commentaire.
