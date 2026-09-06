# Acoustique du bâtiment

*Prérequis : la compétence **Parois, résistance thermique et coefficient $U$**.*

## Le son et ses grandeurs

Le **son** est une sensation auditive produite par une **variation rapide de la pression de l'air** : la vibration d'un corps crée une succession de zones de pression et de dépression qui fait vibrer le tympan. Dans l'air, l'onde se propage à **340 m/s**.

| Grandeur | Plage utile | Unité |
|---|---|---|
| Fréquence | 20 à 20 000 (audible) | hertz (Hz) |
| Pression acoustique | 0,000 02 à 20 | pascal (Pa) |
| Niveau sonore | 0 à 130 (seuil de la douleur) | décibel (dB) |

Plus la fréquence est élevée, plus le son est **aigu**. Entre la plus faible et la plus forte pression audible, le rapport atteint **1 à 1 000 000** : pour ramener cette étendue à une échelle maniable, on a adopté la notation logarithmique et créé le **décibel**.

$$L = 10\log\!\left(\frac{I}{I_0}\right) \qquad \text{avec}\qquad I_0 = 1{,}0 \times 10^{-12}\ \text{W/m}^2$$

{{fig:pc-echelle-decibels}}

**Les décibels ne s'additionnent pas** : ce sont les **intensités** qui s'ajoutent.

- deux sources identiques : $\times 2$ sur $I$ → **+3 dB** (60 dB + 60 dB = 63 dB) ;
- dix sources identiques : $\times 10$ sur $I$ → **+10 dB** (60 dB → 70 dB).

Conséquence de chantier : supprimer la moitié des machines ne fait gagner que 3 dB. Mieux vaut traiter la source la plus bruyante.

## Ce que devient l'énergie sonore sur une paroi

L'énergie incidente se divise en **trois** parts :

- l'énergie **transmise**, qui traverse la paroi ;
- l'énergie **absorbée**, dissipée en chaleur dans la paroi ;
- l'énergie **réfléchie**, renvoyée vers le local d'origine.

{{fig:pc-reflexion-transmission}}

Deux métiers en découlent :

| | Part de l'énergie visée | Objectif |
|---|---|---|
| **Isolation acoustique** | transmise | la réduire le plus possible (protéger le local voisin) |
| **Correction acoustique** | absorbée et réfléchie | rendre le local lui-même confortable |

## Isoler : l'indice d'affaiblissement $R$

Une paroi est caractérisée par son **indice d'affaiblissement acoustique** $R$, exprimé en **décibels**. Il se **soustrait** au niveau émis :

$$L_2 = L_1 - R$$

{{fig:2i2d-affaiblissement-paroi}}

**Exemple** — atelier à $L_1 = 85$ dB, paroi de $R = 42$ dB → bureau voisin à $L_2 = 43$ dB. Si le cahier des charges impose 35 dB, il faut $R = 85 - 35 = 50$ dB.

*Attention* : ce $R$ acoustique en dB n'a rien à voir avec la résistance thermique en m²·K/W, malgré la lettre commune.

Deux principes gouvernent l'isolation aux **bruits aériens** :

- la **masse** : plus une paroi est lourde, plus elle est difficile à mettre en vibration, donc plus elle transmet peu ;
- le **découplage** (système masse-ressort-masse) : deux parois séparées par une lame d'air garnie de laine isolent bien mieux qu'une paroi unique de même masse — c'est le principe du double vitrage et des doublages.

Les **bruits d'impact** (pas, chocs) sont injectés directement dans la structure : alourdir ne suffit pas, il faut **désolidariser** (chape flottante sur couche résiliente).

Ne pas confondre : un matériau **absorbant** (léger, poreux) absorbe bien mais **isole mal** ; un matériau **isolant** acoustique est lourd ou découplé.

## Corriger : le temps de réverbération

Après l'arrêt de la source, le son continue de rebondir sur les parois. Le **temps de réverbération** $T_R$ est la durée au bout de laquelle le niveau a chuté de **60 dB**. La formule de Sabine le relie au volume et à l'absorption :

$$T_R = 0{,}16 \times \frac{V}{A}$$

$T_R$ en secondes, $V$ le volume du local en m³, $A$ l'**aire d'absorption équivalente** en m². *(Relation classique de l'acoustique des salles, donnée ici en complément du programme.)*

{{fig:2i2d-reverberation-salle}}

**Exemple** — gymnase de $V = 1\,000$ m³ avec $A = 200$ m² : $T_R = 0{,}16 \times 1\,000/200 = \mathbf{0{,}80}$ s. Pour descendre à 0,50 s, il faut $A = 0{,}16 \times 1\,000/0{,}50 = 320$ m², soit **120 m² d'absorption à ajouter** (panneaux au plafond ou en partie haute des murs).

Un hall entièrement carrelé et vitré réfléchit presque toute l'énergie : $A$ est faible, $T_R$ est long, et chaque syllabe est encore audible quand la suivante est prononcée — l'**intelligibilité** s'effondre.
