# Cotation tolérancée et ajustements

## Pourquoi tolérancer

Aucun procédé de fabrication ne donne exactement la cote demandée : une machine produit toujours une dispersion. Plutôt que d'exiger l'impossible, on définit un **intervalle** dans lequel la cote réalisée doit tomber pour que la pièce soit bonne.

Une cote tolérancée s'écrit donc avec une cote nominale et deux écarts :

$$\varnothing32^{+0{,}025}_{+0{,}009}$$

## Le vocabulaire, et sa convention de casse

{{fig:sc-tolerances}}

| Symbole | Signification |
|---|---|
| $CN$ | cote nominale — la **ligne zéro**, origine des écarts |
| $ES$, $EI$ | écarts supérieur et inférieur de l'**alésage** (majuscules) |
| $es$, $ei$ | écarts supérieur et inférieur de l'**arbre** (minuscules) |
| $IT$ | intervalle de tolérance |

La convention tient en une ligne : **majuscules pour l'alésage** (la pièce creuse), **minuscules pour l'arbre** (la pièce pleine). Elle vaut aussi pour les lettres de position — H7 est un alésage, m6 un arbre.

Les relations à connaître :

$$IT = ES - EI \quad\text{pour l'alésage}$$
$$IT = es - ei \quad\text{pour l'arbre}$$
$$\text{cote maxi} = CN + \text{écart supérieur}$$
$$\text{cote mini} = CN + \text{écart inférieur}$$

Deux points de vigilance :

- les **écarts ont un signe** (un écart négatif place la zone sous la ligne zéro), mais l'**$IT$ est toujours positif** : c'est une largeur de zone, pas une position ;
- les tables donnent les écarts en **micromètres**, les cotes s'écrivent en **millimètres**. $21\ \mu$m $=0{,}021$ mm.

## La notation normalisée

Dans $\varnothing20$ **H7/m6** :

- $20$ est le diamètre nominal, commun aux deux pièces ;
- la **lettre** donne la **position** de la zone par rapport à la ligne zéro ;
- le **chiffre** donne la **qualité**, c'est-à-dire la largeur de la zone.

La position H est particulière : elle place l'écart inférieur de l'alésage exactement sur la ligne zéro, $EI=0$. C'est le **système de l'alésage normal** : on garde toujours le même alésage H7 et l'on change la lettre de l'arbre pour obtenir le comportement voulu. Cela évite de refaire les outils de perçage à chaque montage.

## Jeu, serrage, incertain

{{fig:sc-jeu-serrage}}

Ce qui décide du type d'ajustement, ce n'est pas la largeur des zones mais leur **position relative** :

$$\text{jeu maxi} = \text{alésage maxi} - \text{arbre mini}$$
$$\text{jeu mini} = \text{alésage mini} - \text{arbre maxi}$$
$$\text{serrage maxi} = \text{arbre maxi} - \text{alésage mini}$$

Le jeu est maximal quand le trou est au plus grand **et** l'arbre au plus petit ; le serrage est maximal dans le cas inverse — le plus défavorable au montage.

- **Avec jeu** : la zone de l'arbre est entièrement sous celle de l'alésage. Le jeu minimal reste positif, l'arbre entre toujours librement.
- **Avec serrage** : la zone de l'arbre est entièrement au-dessus. Il faut forcer au montage, quelles que soient les pièces.
- **Incertain** : les deux zones se recoupent. Selon les pièces tirées du lot, on obtient un jeu ou un serrage.

## Trois ajustements à connaître

| Ajustement | Comportement | Emploi |
|---|---|---|
| H7/g6 | jeu garanti | guidage en rotation ou en translation |
| H7/m6 | incertain | centrage précis, immobile, démontable à la presse |
| H7/p6 | serrage garanti | montage définitif, transmission par adhérence |

**Exemple, $\varnothing18$ H7/g6.** Alésage : $ES=+18\ \mu$m, $EI=0$, soit $18{,}018$ / $18{,}000$. Arbre : $es=-6\ \mu$m, $ei=-17\ \mu$m, soit $17{,}994$ / $17{,}983$.

$$\text{jeu maxi}=18{,}018-17{,}983=35\ \mu\mathrm{m}$$
$$\text{jeu mini}=18{,}000-17{,}994=6\ \mu\mathrm{m}$$

Les deux sont positifs : il y aura toujours du jeu, l'ajustement convient à un guidage.

**Exemple, $\varnothing20$ H7/m6.** Alésage $20{,}021$ / $20{,}000$, arbre $20{,}021$ / $20{,}008$.

$$\text{jeu maxi}=20{,}021-20{,}008=13\ \mu\mathrm{m}$$
$$\text{serrage maxi}=20{,}021-20{,}000=21\ \mu\mathrm{m}$$

Un jeu **et** un serrage sont possibles : l'ajustement est incertain. C'est ce qu'on veut pour un moyeu, un roulement ou une pièce de centrage — pas de jeu appréciable, et un démontage encore possible à la presse.

## Une tolérance coûte cher

Diviser un $IT$ par quatre, c'est changer de procédé (rectifier au lieu de tourner), multiplier les contrôles et augmenter le rebut.

**On ne resserre une tolérance que si la fonction l'exige.** C'est l'une des règles de base de la conception économique — et une question classique en devoir.
