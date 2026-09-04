# Les efforts transmissibles

Une liaison **transmet des efforts** exactement dans les directions où elle **bloque** le mouvement
(en supposant les contacts parfaits, sans frottement).

- Une **force** transmise a trois composantes possibles : **X, Y, Z** (suivant chaque axe).
- Un **moment** (couple) transmis a trois composantes possibles : **L, M, N** (autour de x, y, z).

## La règle de complémentarité

Pour chaque axe et chaque type de mouvement :

- si la **translation** Tx est **libre**, la force **X** n'est **pas** transmise (et réciproquement) ;
- si la **rotation** Rx est **libre**, le moment **L** n'est **pas** transmis.

Donc : **nombre de ddl + nombre de composantes transmissibles = 6**.

Exemples :

- **Pivot** d'axe x : Rx libre → pas de moment L ; tout le reste est transmis : X, Y, Z, M, N (5 composantes).
- **Rotule** : les 3 rotations libres → aucun moment ; seules les forces X, Y, Z (3 composantes).
- **Appui plan** de normale y : Tx, Tz, Ry libres → transmet Y, L, N.

Cas particulier de l'**hélicoïdale** : Tx et Rx sont liés, X et L le sont aussi (le couple de serrage produit une force axiale).

{{table:efforts}}
