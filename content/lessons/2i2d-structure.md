# Schéma cinématique en 3D et structure d'un mécanisme

## Ce que montre un schéma cinématique

Le **schéma cinématique** d'un système est une figure **plane ou spatiale** qui permet d'analyser
les **mouvements des éléments les uns par rapport aux autres**. Les pièces reliées entre elles par
une **liaison encastrement** n'ont aucun mouvement relatif : on les regroupe en **classes
d'équivalence cinématique**, identifiées par un nom ou un numéro.

Quatre éléments doivent figurer sur le schéma :

| Élément | Rôle |
|---|---|
| un **repère** $(x, y, z)$ | orienter le mécanisme et les axes des liaisons |
| un **élément de référence** (bâti) | la partie immobile ; symbole en traits hachurés |
| des **liaisons normalisées** | donner les mobilités d'une classe par rapport à une autre |
| les **classes d'équivalence** | traits (ou volumes) colorés, un par groupe de pièces |

{{fig:cinematique-repere}}

Chaque liaison est repérée par un **point** et un **axe** : on écrit par exemple
« liaison pivot $(B, \vec{x})$ ». En perspective, on utilise la **schématisation spatiale** de la
liaison ; en vue plane, l'une des deux schématisations planes selon la direction de l'axe.

**Attention à ne pas confondre trois notions** qui utilisent parfois les mêmes mots :

- les **mouvements** : rotation, translation circulaire, mouvement plan… ;
- les **liaisons** : pivot, glissière, rotule, sphère-plan… ;
- les **trajectoires** : segment de droite, arc de cercle, cercle, courbe quelconque…

## Le torseur des actions transmissibles

À côté de ses **degrés de liberté**, une liaison se caractérise par les **composantes** de la force
et du moment qu'elle **transmet**, écrites au point $A$ dans le repère $R$ :

$$\{X_A\ \ L_A\ ;\ Y_A\ \ M_A\ ;\ Z_A\ \ N_A\}_R$$

$X_A$, $Y_A$, $Z_A$ sont les composantes de la **force** suivant $\vec{x}$, $\vec{y}$, $\vec{z}$
(en N) ; $L_A$, $M_A$, $N_A$ celles du **moment** autour de ces mêmes axes (en N·m).

**Règle de lecture** : à chaque **degré de liberté** correspond une **composante nulle** ; à chaque
mobilité **bloquée** correspond une composante transmissible. Une liaison parfaite ne peut pas
retenir un mouvement qu'elle autorise.

{{fig:contact-pivot}}

| Liaison | ddl | Torseur transmissible |
|---|---|---|
| Encastrement de centre $A$ | 0 | $X_A\ L_A$ ; $Y_A\ M_A$ ; $Z_A\ N_A$ |
| Pivot d'axe $(A, \vec{x})$ | 1 ($R_x$) | $X_A\ 0$ ; $Y_A\ M_A$ ; $Z_A\ N_A$ |
| Glissière d'axe $(A, \vec{x})$ | 1 ($T_x$) | $0\ L_A$ ; $Y_A\ M_A$ ; $Z_A\ N_A$ |
| Pivot glissant d'axe $(A, \vec{x})$ | 2 ($T_x$, $R_x$) | $0\ 0$ ; $Y_A\ M_A$ ; $Z_A\ N_A$ |
| Rotule de centre $A$ | 3 | $X_A\ 0$ ; $Y_A\ 0$ ; $Z_A\ 0$ |

Cas particulier : la liaison **hélicoïdale** n'a qu'**un** degré de liberté, car $T_x$ et $R_x$ y
sont **liés** par le pas ; de même, $X_A$ et $L_A$ y sont liés.

## Une application : la caméra dôme motorisée

La caméra dôme du hall d'un palais des sports est orientable dans deux directions grâce à deux
moteurs à courant continu indépendants (repère 25 de la nomenclature, quantité 2).

{{fig:2i2d-schema-camera}}

| Classe | Contenu | Liaison avec la classe précédente |
|---|---|---|
| 0 — bâti | plateau support 3, tiges 2, platine 1 et leur visserie | — |
| 1 — panoramique | chape 8, poulie 14, axe d'articulation 6, collecteur tournant 24 | pivot $(O, \vec{z})$, roulements 5 |
| 2 — site | module caméra 27, chape 10, roue dentée 13 | pivot $(A, \vec{y})$, roulements 9 |

*Piège de vocabulaire du manuel* : la **rotation horizontale** (panoramique) se fait autour de
l'axe **vertical** $z$, et la **rotation verticale** (site) autour de l'axe **horizontal** $y$. Le
mouvement est nommé d'après la direction dans laquelle la visée balaie, non d'après son axe.

## Deux transmissions, deux comportements

{{fig:transmission-poulies}}

La classe 1 est entraînée par une **transmission poulies-courroie** : poulie 19 ($Z = 10$) →
courroie 26 → poulie 14 ($Z = 56$). Le rapport vaut $10/56 \approx 0{,}18$ (réduction de 5,6) et le
**sens de rotation est conservé**.

{{fig:transmission-engrenage}}

La classe 2 est entraînée par un **engrenage extérieur** : pignon 12 ($Z = 10$, $m = 1$) → roue
dentée 13 ($Z = 83$, $m = 1$). Le rapport vaut $10/83 \approx 0{,}12$ (réduction de 8,3) et le
**sens de rotation est inversé**.

Avec un moteur à 500 tr·min⁻¹ et $R = 0{,}18$, la chape tourne à
$500 \times 0{,}18 = 90$ tr·min⁻¹, soit $90 \times 360 / 60 = 540$ °·s⁻¹.
