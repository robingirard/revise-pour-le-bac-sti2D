# Dynamique : translation et rotation

*Prérequis : les compétences **Travail, puissance et énergie mécanique** et **Accélération et équations du mouvement**.*

## Le principe fondamental de la dynamique (PFD)

Dans le **référentiel terrestre**, la résultante des forces $\vec{F_u}$ appliquée à un système assimilé à un point est égale au produit de sa masse par le vecteur accélération de son centre de masse :

$$\vec{F_u} = m \times \vec{a_G} \qquad \text{avec} \qquad \vec{F_u} = \sum \overrightarrow{F_{\text{ext}}}$$

$F_u$ en newton (N), $m$ en kilogramme (kg), $a_G$ en $\mathrm{m\cdot s^{-2}}$.

- $\vec{F_u}$ et $\vec{a_G}$ ont **la même direction et le même sens** ;
- du mouvement vers les forces : $F_u = m \times a_G$ ;
- des forces vers le mouvement : $a_G = \dfrac{F_u}{m}$.

{{fig:cinematique-acceleration}}

## La chute libre

Un système en **chute libre** n'est soumis qu'à son **poids** (toute force de frottement est négligée). Le PFD s'écrit alors $\vec{P} = m\,\vec{a_G}$ avec $\vec{P} = m\,\vec{g}$, donc :

$$\vec{a_G} = \vec{g} \qquad\text{soit}\qquad a = 9{,}81\ \mathrm{m\cdot s^{-2}}$$

La masse **se simplifie** : tous les corps tombent avec la même accélération. Avec une vitesse initiale nulle, les équations du mouvement uniformément varié donnent $v = g\,t$ et $h = \tfrac12\,g\,t^2$.

Avec **frottements**, la force de frottement s'oppose au mouvement : elle réduit $F_u$, donc l'accélération ; son travail est **résistant** ($\alpha = 180^\circ$, $W = -F \times \mathrm{AB}$).

## Vitesses angulaire et linéaire

$$\omega = \frac{\theta}{\Delta t} \qquad\qquad v = \omega \times r$$

$\omega$ en $\mathrm{rad\cdot s^{-1}}$, $\theta$ en rad, $\Delta t$ en s, $v$ en $\mathrm{m\cdot s^{-1}}$, $r$ = distance du point à l'axe $(\Delta)$, en m.

Conversion : $\theta(\mathrm{rad}) = \dfrac{\theta(^\circ) \times 2\pi}{360}$ ; une vitesse en $\mathrm{tr\cdot min^{-1}}$ se convertit par $\omega = \dfrac{n \times 2\pi}{60}$.

{{fig:cinematique-champ-rotation}}

**Tout point d'un solide en rotation tourne à la même vitesse angulaire $\omega$** ; plus il est éloigné de l'axe, plus sa **vitesse linéaire** $v$ est grande.

## Moment d'une force, moment d'un couple

{{fig:pc-moment-bras-levier}}

$$M_\Delta(\vec{F}) = F \times d$$

$M_\Delta(\vec{F})$ en **newton mètre (N·m)**, $F$ en N, $d$ = **bras de levier** en m, c'est-à-dire la **distance la plus courte entre l'axe de rotation $(\Delta)$ et la droite d'action de la force**.

Un **couple** est constitué de deux forces de même direction, de même valeur et de sens opposés. Son moment vaut $M = F \times d$, avec $F = F_1 = F_2$ et $d$ = distance la plus courte entre les **deux droites d'action**. Il est **indépendant de la position de l'axe de rotation**.

## Point de fonctionnement d'un ensemble moteur-charge

{{fig:pc-point-fonctionnement-moteur}}

On trace le **couple utile $T_u$ (N·m)** en fonction de la **vitesse de rotation $n$ ($\mathrm{tr\cdot min^{-1}}$)** pour le moteur **et** pour la charge :

- le **point de fonctionnement** se situe à l'**intersection** des deux caractéristiques ;
- **si aucune intersection n'existe, le moteur ne peut pas supporter la charge imposée**.

Sur la figure ci-dessus, le moteur doit fournir un couple utile de **100 N·m** à une vitesse **légèrement supérieure à 900 tr·min⁻¹** pour supporter la charge.
