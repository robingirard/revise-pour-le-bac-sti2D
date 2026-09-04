# Poutres, sollicitations et contrainte

La **résistance des matériaux** (RDM) a trois objectifs : connaître les caractéristiques mécaniques des
matériaux, étudier la **résistance** des pièces et étudier leur **déformation**. Elle permet de choisir le
matériau et les dimensions d'une pièce, donc d'utiliser le moins de matière possible sans risquer la rupture.

## Les hypothèses de la RDM

Sur le **matériau**, on suppose qu'il est :

- **isotrope** : mêmes propriétés mécaniques dans toutes les directions (faux pour le bois et les composites) ;
- **homogène** : même composition en tout point ;
- **continu** : sans fissure.

{{fig:rdm-poutre}}

Sur la **forme**, on n'étudie que des **poutres**. Une poutre est un solide engendré par une surface plane
$(S)$ dont le centre de surface $G$ décrit une courbe $(C)$ appelée **ligne moyenne**. Ses caractéristiques :
ligne moyenne droite ou peu courbée, section droite constante ou variant progressivement, **grande longueur**
devant les dimensions transversales, et un plan de symétrie.

Sur les **déformations**, on les suppose **petites** devant les dimensions de la poutre : les efforts sont
alors calculés par le PFS sur la pièce non déformée. Enfin, l'**hypothèse de Barré de Saint-Venant** rappelle
que les résultats de la RDM ne sont valables qu'assez **loin des zones d'application des efforts concentrés**.

## Les sollicitations simples

{{fig:rdm-sollicitations}}

| Sollicitation | Chargement | Effet sur la poutre |
|---|---|---|
| Traction | deux efforts axiaux **vers l'extérieur** | **allongement**, puis rupture |
| Compression | deux efforts axiaux **vers l'intérieur** | **raccourcissement**, puis écrasement |
| Flexion | poutre sur appuis, charge transversale | **fléchissement**, puis rupture |
| Cisaillement | deux efforts transversaux très proches | glissement d'une section sur l'autre |
| Torsion | deux couples opposés autour de la ligne moyenne | la section tourne, la poutre se **tord** |

## Le torseur de cohésion

Pour connaître les efforts que la matière transmet à l'intérieur de la poutre, on réalise une **coupure
imaginaire** par un plan perpendiculaire à la ligne moyenne, puis on isole un tronçon. Les efforts exercés par
le tronçon supprimé sur le tronçon conservé forment le **torseur de cohésion**, exprimé au centre $G$ de la
section coupée. C'est la forme de ce torseur qui nomme la sollicitation :

- traction / compression : seul l'effort normal $N$ est non nul ($N > 0$ en traction, $N < 0$ en compression) ;
- flexion (simple) : effort tranchant $T_y$ et moment de flexion $M_{fz}$ non nuls.

## La contrainte normale

{{fig:rdm-contrainte}}

En traction ou en compression, l'effort $N$ se répartit uniformément sur la section : la **contrainte
normale** est l'effort **par unité de surface** :

$\sigma = \dfrac{F}{S}$, avec $F$ en **N**, $S$ en **mm²** et $\sigma$ en **N/mm²**.

Retenir : $1 \text{ N/mm}^2 = 1 \text{ MPa}$. La contrainte n'est donc **pas** une force : deux pièces
peuvent subir le même effort et des contraintes très différentes si leurs sections diffèrent.
Pour une section circulaire de diamètre $d$ : $S = \dfrac{\pi d^2}{4}$.

## À retenir

| Grandeur | Formule | Unité |
|---|---|---|
| Contrainte normale | $\sigma = F / S$ | N/mm² = MPa |
| Section circulaire | $S = \pi d^2 / 4$ | mm² |
| Effort normal | $N$ (traction $> 0$, compression $< 0$) | N |
