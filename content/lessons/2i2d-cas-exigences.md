# Cahier des charges, cas d'utilisation et exigences

## Du besoin au cahier des charges

Un **système** (ou **produit**) est conçu pour satisfaire un **besoin**, exprimé ou latent, de
futurs utilisateurs. Le **cahier des charges** est le document — ou le dossier de documents — qui
définit ce que l'utilisateur attend du produit, en termes de fonctions et de fonctionnalités.
L'**analyse fonctionnelle** consiste ensuite à examiner les fonctions que le système doit remplir,
compte tenu du but à atteindre.

Deux diagrammes SysML servent à mettre le cahier des charges en images : le diagramme des **cas
d'utilisation** (`uc`) et le diagramme d'**exigences** (`req`).

## Le diagramme des cas d'utilisation (`uc`)

Il présente les **interactions entre le système et son environnement**. Il décrit **ce que** le
futur système devra faire, **sans dire comment** il le fera.

{{fig:2i2d-uc-elements}}

| Élément | Représentation |
|---|---|
| Le **système** | un rectangle : sa frontière ; le nom est précédé du stéréotype `«useCaseModel»` |
| Les **acteurs humains** | un bonhomme filiforme, à l'extérieur du rectangle |
| Les « **choses** » en interaction | un petit bloc 3D (bateau, énergie, véhicule…) |
| Les **cas d'utilisation** | une ellipse par service rendu, à l'intérieur du rectangle |

Les acteurs **principaux** se placent à **gauche** du système, les acteurs **secondaires** à
**droite**. Deux liens relient les cas d'utilisation entre eux :

- `«include»` — lien d'**inclusion** : la fonction pointée est **indispensable** à la fonction
  principale ;
- `«extend»` — lien d'**extension** : la fonction à l'origine de la flèche **n'est pas
  indispensable**.

{{fig:2i2d-uc-transbordeur}}

Sur le projet de **pont transbordeur** de Nantes, « Franchir la Loire » **inclut** « Permettre le
passage de bateaux » (on ne peut pas construire l'ouvrage sans laisser passer les navires), tandis
que « Déambuler sur la rue aérienne » **étend** le franchissement : c'est un service en plus.

## Le diagramme d'exigences (`req`)

Il **décrit les exigences du cahier des charges** : les fonctions que le système doit réaliser et
les contraintes qu'il doit respecter. Chaque exigence est une boîte à deux compartiments : un
en-tête (stéréotype + nom) et un corps contenant `Id = "…"` et `Text = "…"`. Une **priorité**
haute, moyenne ou basse (**1, 2, 3**) peut lui être associée.

{{fig:2i2d-req-transbordeur}}

Les stéréotypes précisent la nature de l'exigence : `«functional Requirement»` (une fonction à
assurer), `«physical Requirement»` (une dimension, une masse), `«usability Requirement»` (le
confort ou l'accessibilité), `«performance Requirement»` (une durée, une vitesse).

Les exigences sont reliées par des **liens de dépendance** :

| Lien | Tracé | Signification |
|---|---|---|
| décomposition | trait plein terminé par un cercle barré d'une croix ⊕ du côté de l'exigence générale | l'exigence générale se compose d'exigences plus détaillées |
| `«refine»` | flèche pointillée vers l'élément pointé | **ajoute des précisions** sur cet élément |
| `«deriveRqt»` | flèche pointillée vers l'exigence pointée | l'exigence **découle** de celle qui est pointée |
| `«satisfy»` | flèche pointillée vers l'exigence pointée | l'élément **répond à la demande** formulée |

## Lire des valeurs dans un `req`

Le diagramme n'est pas décoratif : il contient les **données chiffrées** du projet. Sur le pont
transbordeur, l'exigence « 1.1.1 » indique que deux cabines fermées accueillent **270 personnes**,
l'exigence « 5 » qu'un busway transporte jusqu'à **150 personnes**, et l'exigence « 12 » que la
hauteur libre sous le tablier vaut au moins **55 m** au-dessus de la Loire à marée haute.

Une traversée transporte donc $270 + 150 = 420$ personnes. Avec un passage effectué en
$1{,}75$ minute (exigence « 6 »), un aller-retour dure $2 \times 1{,}75 = 3{,}5$ min, soit
$60 / 3{,}5 \approx 17{,}1$ traversées par heure dans un sens, et un flux de
$17{,}1 \times 420 \approx 7\,200$ personnes par heure et par sens.
