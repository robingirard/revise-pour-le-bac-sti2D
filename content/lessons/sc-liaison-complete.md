# La liaison complète : mise et maintien en position

## Ce qu'on demande à une liaison complète

Lier complètement deux pièces, c'est leur interdire **les six mobilités relatives**. Le résultat porte un nom : l'**encastrement**, la liaison à zéro degré de liberté.

Cette fonction principale se décompose toujours en deux fonctions techniques, qu'il faut savoir distinguer :

- **mettre en position (MAP)** — dire *où* la pièce doit se trouver ;
- **maintenir en position (MEP)** — l'empêcher de quitter cette place.

Sur un diagramme FAST, ce sont les fonctions FT11 et FT12. Elles sont remplies par des éléments **différents** : des surfaces usinées d'un côté, un organe de serrage de l'autre.

## Une surface positionne, un organe maintient

C'est la règle de conception qui gouverne tout le chapitre.

Une **surface fonctionnelle** est une surface de la pièce qui participe à la fonction : c'est elle qui touche l'autre pièce, et sa position est fixée à l'usinage. Une vis, elle, serre — mais l'endroit où elle s'arrête dépend du couple appliqué, donc du monteur.

Faire porter le positionnement par la vis, c'est faire dépendre une cote fonctionnelle du tour de clé. La précision s'effondre.

## Chaque surface ne fait qu'une chose

{{fig:sc-liaison-complete}}

Sur cette liaison entre la tige d'un vérin et son piston :

| Surface | Nature | Positionnement assuré |
|---|---|---|
| SF1 | cylindrique | **radial** : la coaxialité |
| SF2 | plane, perpendiculaire à l'axe | **axial** : la butée |

La portée cylindrique ne dit rien de la position *le long* de l'axe : le piston pourrait coulisser. La face plane ne dit rien de la position *autour* de l'axe. Il faut les deux.

## Associer deux liaisons simples

Chaque contact, pris isolément, réalise une liaison simple :

| Contact | Liaison simple | Degrés de liberté |
|---|---|---|
| Cylindrique | pivot glissant | $Tx$ et $Rx$ |
| Plan | appui plan | 3 |
| Sphérique | rotule | 3 rotations |

Le pivot glissant d'axe $x$ laisse $Tx$ et $Rx$. L'appui plan de normale $x$ supprime $Tx$. Leur association laisse donc $Rx$ : c'est une liaison **pivot**, pas encore un encastrement.

La mise en position est complète — mais la pièce peut encore tourner. C'est exactement ce qui justifie la présence de la vis.

## Le maintien en position

La vis serre la face plane du piston contre l'épaulement de la tige. L'adhérence ainsi créée supprime la dernière rotation, et la liaison devient complète.

Le cahier des charges guide le choix de l'organe :

- **« démontable aisément »** élimine d'un coup le soudage, le collage et le rivetage ; il ne reste que les solutions filetées et les anneaux élastiques ;
- **« action mécanique transmissible : effort de traction »** dimensionne la vis ;
- **« coût et encombrement minimaux »** départage les solutions restantes.

Un critère éliminatoire se traite en premier : inutile de comparer des solutions qui de toute façon ne conviennent pas.

## La démarche d'analyse

Face à un dessin d'ensemble, on part toujours du contact réel et on remonte vers le modèle :

1. repérer les surfaces en contact entre les deux pièces ;
2. donner la nature de chacune (plane, cylindrique, conique, sphérique) ;
3. dire quel positionnement chacune assure (radial ou axial) ;
4. nommer la liaison simple que chacune réalise ;
5. conclure sur la liaison obtenue par leur association ;
6. identifier la solution qui assure le maintien en position.

L'erreur classique est de commencer par nommer la liaison, puis de chercher à la justifier.

## Sur le schéma cinématique

Deux pièces liées complètement n'ont aucun mouvement relatif : elles appartiennent donc à la **même classe d'équivalence**. Sur le schéma, on ne les sépare pas, on ne met aucun symbole entre elles — elles sont dessinées comme une seule pièce, de la même couleur.

Pour le vérin de la pince, la tige et le piston forment une seule classe ; la glissière apparaît entre cet ensemble et le corps du vérin.
