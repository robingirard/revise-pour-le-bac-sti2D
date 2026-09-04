# Les structures porteuses

Une **structure porteuse** a pour fonction d'**encaisser** les charges subies par l'ouvrage et de les
**acheminer** jusqu'aux points d'ancrage au sol. On en rencontre deux grandes catégories : les
**bâtiments** (individuels ou collectifs) et les **ouvrages d'aménagement du territoire** (ponts,
barrages…).

On distingue la partie visible, la **superstructure**, de la partie invisible, l'**infrastructure**
(fondations).

## Les actions subies

| Direction | Fréquence | Origine |
|---|---|---|
| Verticale | Permanente | poids propre |
| Verticale | Variable | charges d'exploitation (utilisateurs, stockages), neige |
| Horizontale | Variable | vent, séisme, pression de l'eau |

Le poids propre est la seule action **permanente** : c'est aussi souvent la plus lourde. Sur une dalle de
348 m² et 0,40 m d'épaisseur en béton armé (poids volumique 25 kN·m⁻³), le poids propre atteint 3 480 kN,
contre 1 027 kN pour l'exploitation et la neige réunies.

## La descente de charges

{{fig:2i2d-descente-charges}}

La **descente de charges** étudie le transfert des charges dans la structure : leur **répartition** et
leur **cheminement**, du haut jusqu'aux fondations.

Les charges transitent d'abord par des porteurs « **horizontaux** » (dalles, poutres) principalement
**fléchis**, qui les reportent sur des porteurs « **verticaux** » (poteaux, murs) principalement
**comprimés**, puis sur les fondations et enfin sur le sol. Des éléments inclinés (charpentes, câbles,
haubans) peuvent s'intercaler.

Les valeurs obtenues servent ensuite à **dimensionner** chaque élément porteur.

## ELS et ELU

Une structure est calculée pour deux types d'utilisation :

- **ELS**, état limite de service : l'utilisation « quotidienne ». Les charges ne sont **pas pondérées**.
- **ELU**, état limite ultime : le cas le plus défavorable. On veut garantir que l'ouvrage résistera à la
  **rupture**, donc on **pondère** les charges, c'est-à-dire qu'on augmente leur valeur en les multipliant
  par un coefficient défini par une norme.

## La modélisation des appuis au sol

{{fig:statique-appuis}}

| Appui | Ce qu'il autorise | Ce qu'il bloque |
|---|---|---|
| Appui simple **glissant** (sur rouleaux) | rotation **et** translation le long du sol | 1 translation |
| Appui simple **fixe** (articulation) | rotation seule | 2 translations |
| **Encastrement** | rien, liaison complète | 2 translations + 1 rotation |

{{fig:2i2d-appuis-reactions}}

Règle à retenir : **à chaque mobilité bloquée correspond une inconnue de liaison**. Une translation bloquée
donne une composante d'effort, une rotation bloquée donne un moment. Dans un problème plan, l'appui
glissant apporte 1 inconnue, l'articulation 2, l'encastrement 3.

Comme le PFS plan ne fournit que **3 équations**, une poutre reposant sur une articulation et un appui
glissant (2 + 1 = 3 inconnues) est exactement soluble : on dit qu'elle est **isostatique**.

## Poutre sur deux appuis

{{fig:2i2d-poutre-deux-appuis}}

Méthode : on écrit le théorème du moment **à l'un des appuis** pour éliminer sa réaction, ce qui donne
directement l'autre ; puis le théorème de la résultante donne la première.

Exemple : poutre $AB$ de 6,00 m, charges de 12 kN à 2,00 m de $A$ et de 6 kN à 4,00 m de $A$.
Moment en $A$ : $R_B \times 6{,}00 = 12 \times 2{,}00 + 6 \times 4{,}00 = 48$, donc $R_B = 8$ kN ;
résultante : $R_A = 18 - 8 = 10$ kN. L'appui le plus proche de la charge lourde reprend le plus d'effort.

## Des fondations au sol

La dernière étape de la descente de charges est la vérification du **sol**. On compare la pression sous la
semelle, $q_F = Q_p / S$, à la pression admissible du sol. Si elle est dépassée, on **élargit** la semelle :
c'est le seul moyen de réduire la pression à charge constante.

## À retenir

| Question | Réponse |
|---|---|
| Rôle d'une structure porteuse | encaisser et acheminer les charges jusqu'au sol |
| Porteur horizontal / vertical | fléchi / comprimé |
| ELS / ELU | charges non pondérées / charges pondérées |
| Inconnues en plan | glissant 1, articulation 2, encastrement 3 |
| Pression sous une semelle | $q_F = Q_p / S$, à comparer à la résistance du sol |
