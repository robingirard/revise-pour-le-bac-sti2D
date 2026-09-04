# Batteries et accumulateurs

## Capacité, énergie, autonomie

La **capacité** $Q$ d'une batterie est la quantité de **charge** qu'elle peut restituer après une charge complète :

$$Q = I \times t$$

avec $Q$ en ampères-heures (Ah), $I$ en ampères (A) et $t$ en **heures**. Une batterie de 7 Ah délivre 7 A pendant 1 h, ou 3,5 A pendant 2 h.

*Précision importante* : l'ampère-heure mesure une charge, **pas une énergie** (le manuel écrit « quantité d'énergie », c'est une formulation à corriger). L'énergie s'obtient en multipliant par la tension :

$$E = U \times Q$$

avec $E$ en wattheures (Wh), $U$ en volts (V) et $Q$ en Ah. Un module 12 V / 7 Ah stocke $12 \times 7 = 84$ Wh.

L'**autonomie** d'un système alimenté par ce pack se calcule ensuite avec $t = \dfrac{E}{P}$, où $P$ est la puissance appelée.

## Associer des éléments

{{fig:2i2d-batterie-associations}}

- **En série** (pôle $+$ d'un élément sur le pôle $-$ du suivant) : les **tensions s'additionnent**, la capacité en Ah ne change pas.
- **En parallèle** (tous les $+$ ensemble, tous les $-$ ensemble) : la **tension ne change pas**, les **capacités s'additionnent**.

Quatre modules 12 V / 7 Ah donnent :

| Branchement | Tension | Capacité | Énergie |
|---|---|---|---|
| 4 en parallèle | 12 V | 28 Ah | 336 Wh |
| 2 × 2 en série-parallèle | 24 V | 14 Ah | 336 Wh |
| 4 en série | 48 V | 7 Ah | 336 Wh |

**L'énergie stockée ne dépend pas du branchement** : elle est fixée par le nombre d'éléments. Le branchement sert à **adapter la tension** au récepteur (48 V pour un scooter, 384 V pour une propulsion marine).

## Décharge, DoD, SoC

{{fig:2i2d-courbe-decharge}}

Quand une batterie se décharge, la tension à ses bornes **diminue**. La forme de la courbe dépend de la technologie : la **lithium-ion** présente un long plateau presque plat puis une chute brutale, tandis que la **plomb-acide** décroît régulièrement du début à la fin.

Trois grandeurs à ne pas confondre :

- **SoC** (*State of Charge*) : état de charge restant, en % de la capacité ;
- **DoD** (*Depth of Discharge*) : profondeur de décharge, énergie déjà prélevée, en % de la capacité — c'est le complément du SoC ;
- **tension de coupure** : valeur en deçà de laquelle le système coupe l'alimentation pour éviter la décharge profonde ; à distinguer de la **tension nominale**, valeur de référence inscrite sur la batterie.

On mesure le SoC en lisant la **tension** en fonctionnement, ou avec un **compteur de coulombs** qui intègre les charges injectées et soutirées.

## Pourquoi limiter la profondeur de décharge

{{fig:2i2d-cycles-dod}}

Une décharge trop profonde déclenche des phénomènes chimiques qui altèrent l'élément de façon **irréversible**. Le constructeur donne le nombre de cycles admissibles en fonction du DoD : pour les éléments SAFT STM 5-140 MR du ferry-boat de Marseille, environ **1 450 cycles à 70 %**, **2 400 à 50 %**, **4 400 à 30 %**.

Conséquence de dimensionnement : un pack plus grand travaille à faible DoD et dure beaucoup plus longtemps. À l'inverse, réduire la consommation produit le même effet **sans ajouter de matériel**.

## Dimensionner un pack : la démarche

1. Relever la **tension** imposée par la chaîne de propulsion (ici 384 V).
2. Relever la **tension nominale** et la **capacité** d'un élément (6 V ; 136 Ah).
3. Nombre d'éléments **en série** : $384 / 6 = 64$.
4. Énergie par élément $6 \times 136 = 816$ Wh, par parc $64 \times 816 = 52\,224$ Wh, pour deux parcs $104\,448$ Wh.
5. Appliquer la limite de DoD : $104\,448 \times 0{,}70 = 73\,114$ Wh **réellement disponibles**.
6. Comparer au besoin journalier le plus défavorable (73 008 Wh) : le stockage est dimensionné **au plus juste**.
