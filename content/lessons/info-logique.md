# La logique combinatoire

Dans la plupart des systèmes, une action est conditionnée par un événement ou une **combinaison d'événements**, qui peut être vraie ou fausse. On modélise ces événements par des **variables logiques**, qui ne prennent que deux valeurs : 0 ou 1. Trois outils décrivent une même fonction : la **table de vérité**, l'**équation logique** et le **chronogramme**.

## La table de vérité

La table de vérité donne l'état de la sortie pour **toutes** les combinaisons possibles des entrées. Avec $n$ variables d'entrée, elle comporte $2^n$ combinaisons, donc $2^n$ lignes : 4 lignes pour 2 entrées, 8 lignes pour 3 entrées, 16 lignes pour 4 entrées.

## L'équation logique

L'équation logique relie les variables binaires par des **opérateurs logiques**.

| Opérateur | Notation écrite | Notation en langage C |
|---|---|---|
| ET | un point : $S = e_1 \cdot e_2$ | et commercial doublé, && |
| OU | un plus : $S = e_1 + e_2$ | double barre verticale |
| NON | une barre : $S = \overline{e_1}$ | point d'exclamation, ! |

Exemple à trois variables : $S_1 = a \cdot (\overline{e} + c)$. Comme en algèbre, on calcule d'abord la parenthèse.

## Les fonctions logiques de base

| Fonction | Équation | La sortie vaut 1… |
|---|---|---|
| **OUI** | $S = e_1$ | quand l'entrée vaut 1 (la sortie recopie l'entrée) |
| **NON** | $S = \overline{e_1}$ | quand l'entrée vaut 0 (la sortie inverse l'entrée) |
| **ET** | $S = e_1 \cdot e_2$ | seulement si **toutes** les entrées valent 1 |
| **OU** | $S = e_1 + e_2$ | dès qu'**au moins une** entrée vaut 1 |

| $e_1$ | $e_2$ | ET | OU |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 |

Le **ET** n'a qu'une seule ligne à 1 ; le **OU** n'a qu'une seule ligne à 0. C'est le moyen le plus sûr de ne pas les confondre.

## Le chronogramme

Le chronogramme visualise, en fonction du temps, l'état logique des sorties en fonction de celui des entrées.

{{fig:info-chronogramme-et}}

La sortie du **ET** n'est haute que sur les intervalles où les deux entrées sont hautes **en même temps** ; la sortie du **OU** est haute dès que l'une des deux l'est.

## Méthode

- Repérer les variables d'entrée et la variable de sortie, et leur donner un nom.
- Compter le nombre $n$ d'entrées, puis tracer une table de $2^n$ lignes.
- Écrire toutes les combinaisons des entrées, puis remplir la colonne de sortie d'après le cahier des charges.
- En déduire l'équation logique.

Exemple : un convecteur chauffe ($S = 1$) **uniquement** si le local est occupé ($a = 1$) et si la température de consigne n'est pas atteinte ($b = 0$). L'équation est $S = a \cdot \overline{b}$, soit, en langage C, S = a && !b.
