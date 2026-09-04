# Treillis, stabilité et basculement

## Le treillis

{{fig:2i2d-treillis-ferme}}

Un **treillis** est un assemblage de barres verticales, horizontales et diagonales formant des
**triangles**. En architecture, une **ferme** est l'élément de charpente qui supporte le poids de la
couverture ; pour les grandes portées, on la réalise en treillis.

Le triangle est la seule figure **indéformable** à côtés fixes : un quadrilatère articulé s'affaisse en
losange, un triangle non. C'est ce qui donne au treillis sa rigidité pour très peu de matière.

Dans un treillis idéal — barres articulées à leurs extrémités, charges appliquées **aux nœuds** — chaque
barre est un **solide soumis à 2 forces**. Son effort est donc porté par son axe : elle travaille en
**traction** ou en **compression** pure, jamais en flexion. La matière est utilisée au mieux.

Attention : une barre **comprimée** longue et fine peut céder par **flambement** bien avant d'atteindre sa
limite élastique, alors qu'une barre tendue ne connaît pas ce risque. Une même barre pouvant être tendue
sous vent d'ouest et comprimée sous vent d'est, on la dimensionne pour le cas le plus défavorable.

## Le basculement

{{fig:2i2d-basculement}}

Une structure haute soumise à une action horizontale (vent) risque de **basculer**. Elle décolle du côté
d'où vient le vent et pivote autour de l'appui **opposé**, qui joue le rôle d'arête de basculement.

À la **limite du basculement**, la structure ne s'appuie plus que sur cet appui : l'action de liaison de
l'autre côté devient **nulle** (un appui simple ne peut que pousser, jamais retenir). Le problème se
ramène alors à **3 forces** : poids, vent et réaction de l'appui restant — cas d'école de la statique
graphique.

On compare, par rapport à l'arête de basculement :

- le **moment stabilisateur** $M_{\text{stab}} = P \times d_P$ (dû au poids) ;
- le **moment renversant** $M_{\text{renv}} = F \times h$ (dû au vent).

La structure est stable si $M_{\text{stab}} > M_{\text{renv}}$. On exprime souvent ce résultat par un
**coefficient de stabilité** $M_{\text{stab}} / M_{\text{renv}}$, qui doit dépasser 1 (et de préférence
nettement, pour couvrir les incertitudes).

*Exemple* — tour de guet de 40,70 m, poids 55 kN à 4 m de l'appui $A$ :
$F_b = \dfrac{55 \times 4}{40{,}70} \approx 5{,}4$ kN suffit à la faire basculer. La force du vent se
calcule, elle, par $F = p \times S$ : avec 700 Pa sur 14 m² de prise au vent, $F = 9\,800$ N $= 9{,}8$ kN.
Comme $9{,}8 > 5{,}4$, la tour bascule. Remèdes : ancrer les fondations, élargir l'embase, ou réduire la
surface offerte au vent.

## Le poinçonnement

{{fig:2i2d-poinconnement}}

Le **poinçonnement** est l'enfoncement vertical de l'ouvrage dans le sol. La vérification consiste à
comparer la pression sous la semelle à la résistance du sol :

$p = \dfrac{F}{S} \leq p_{\text{admissible}}$

*Exemple* — semelle carrée de 15 m de côté ($S = 225$ m²) sous 35,07 MN :
$p = \dfrac{35{,}07 \times 10^{6}}{225} \approx 0{,}156$ MPa. Le sol admettant 0,20 MPa, la semelle
convient, avec 22 % de marge.

## Le choix des appareils d'appui

Une grande structure doit **résister au vent** tout en pouvant **se dilater**. Ces deux exigences sont
contradictoires si l'on choisit mal les appuis :

| Solution | Vent | Dilatation |
|---|---|---|
| Deux appuis glissants | instable : rien ne reprend l'effort horizontal | libre |
| Deux appuis fixes | stable | bloquée : contraintes parasites |
| Un fixe + un glissant | stable | libre |

C'est donc la combinaison **fixe + glissant** qui est retenue sur presque tous les ouvrages d'art :
l'appui fixe sert de point de référence et reprend les efforts horizontaux, l'appui glissant absorbe
l'allongement thermique. Sur une ferme de 56 m en acier ($\alpha = 12 \cdot 10^{-6}$ °C⁻¹) et une
amplitude de 40 °C, cet allongement vaut $\Delta L = 12 \cdot 10^{-6} \times 56\,000 \times 40 \approx 27$ mm.

## À retenir

| Question | Réponse |
|---|---|
| Treillis | barres assemblées en triangles, chaque barre à 2 forces |
| Barre comprimée élancée | risque de **flambement** |
| Limite du basculement | l'action de l'appui opposé est nulle |
| Condition de non-basculement | $P \times d_P > F \times h$ |
| Poinçonnement | $p = F/S \leq p_{\text{admissible}}$ du sol |
| Appuis d'un ouvrage | un fixe + un glissant |
