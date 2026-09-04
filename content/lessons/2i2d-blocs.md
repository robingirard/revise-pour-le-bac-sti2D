# Diagrammes de blocs : `bdd` et `ibd`

L'**étude structurelle** répond à la question « de quoi le système est-il fait, et comment ses
constituants échangent-ils ? ». Deux diagrammes SysML s'en chargent : le diagramme de définition de
blocs (`bdd`) et le diagramme de blocs internes (`ibd`). Dans les deux cas, le **nom du diagramme
est toujours écrit en haut à gauche**, dans un onglet.

## Le diagramme de définition de blocs (`bdd`)

Il décrit le système d'un point de vue « **composants** » et montre les liens entre les blocs :
c'est le diagramme de l'**architecture matérielle**.

{{fig:2i2d-bdd-ferry}}

| Élément | Rôle |
|---|---|
| `«system»` | le système entier, avec ses caractéristiques principales |
| `«subsystem»` | un sous-ensemble ; ses liens pointent vers les blocs qui le composent |
| `«block»` | un composant ; ses caractéristiques figurent dans le compartiment *values* |

Deux détails de tracé livrent une information à eux seuls :

- un **losange noir** ◆ à la base du lien : l'élément pointé est **obligatoire** ;
- un **losange blanc** ◇ : l'élément pointé est **optionnel** ;
- le **nombre** porté sur le lien donne la **quantité d'éléments identiques**.

*Exemple — la navette maritime électro-solaire (« ferry boat »)* : le sous-système *Alimentation
électrique* est relié à *Panneaux photovoltaïques Propulsion* par un lien portant **16**, et à
*Panneaux photovoltaïques Service* par un lien portant **8**. Comme un panneau « propulsion » a une
puissance crête de 220 Wc, l'installation de propulsion développe
$P = 16 \times 220 = 3\,520$ Wc, soit **3,52 kWc**.

## Le diagramme de blocs internes (`ibd`)

C'est un diagramme **structurel** : il décrit les **échanges de matière, d'énergie et
d'information** entre les blocs **de même niveau**, grâce aux **ports de flux**.

{{fig:2i2d-ibd-ferry}}

| Élément | Représentation |
|---|---|
| un composant (*part*) | un cadre titré `: Nom du composant` |
| un port de flux **entrant** | petit carré posé sur le bord, flèche dirigée **vers l'intérieur** |
| un port de flux **sortant** | petit carré, flèche dirigée **vers l'extérieur** |
| un port **bidirectionnel** | petit carré avec une double flèche ↔ |
| un flux | une ligne reliant deux ports ; **sa nature est écrite au-dessus** |

Les couleurs distinguent souvent les natures de flux : énergie, matière, information (un bus de
terrain comme le *bus CAN* transporte de l'information, un *courant de charge* transporte de
l'énergie).

## Lire un `ibd` : la nature des tensions

Sur l'`ibd` de l'alimentation électrique de la navette, la **prise de quai EDF** est le seul point
en **courant alternatif** : c'est le réseau. Partout ailleurs — sortie des panneaux
photovoltaïques, courant de charge en sortie du chargeur, tension de 384 V d'un parc de batteries —
le courant est **continu**.

## Du `bdd` au dimensionnement

Le `bdd` fournit les données d'un calcul de dimensionnement. Les parcs de batteries de la navette
sont en **384 V** et sont bâtis avec des éléments SAFT de **6 V** et **136 Ah** :

- nombre d'éléments par parc : $384 / 6 = 64$, **câblés en série** (seule l'association série
  additionne les tensions ; la mise en parallèle n'augmenterait que la capacité) ;
- énergie d'un élément : $E = U \times Q = 6 \times 136 = 816$ Wh ;
- énergie des deux parcs : $2 \times 64 \times 816 = 104\,448$ Wh ;
- énergie réellement utilisable avec une profondeur de décharge limitée à 70 % :
  $104\,448 \times 0{,}70 \approx 73\,100$ Wh, soit environ **73 kWh**.

## Quel diagramme pour quelle question ?

| Question | Diagramme |
|---|---|
| Que doit faire le système, et pour qui ? | cas d'utilisation `uc` |
| Quelles fonctions et contraintes doit-il respecter ? | exigences `req` |
| De quels composants est-il fait ? | définition de blocs `bdd` |
| Qu'échangent ces composants entre eux ? | blocs internes `ibd` |
