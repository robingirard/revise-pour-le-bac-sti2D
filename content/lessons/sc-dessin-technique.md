# Lire un dessin technique

## Deux documents, deux rôles

- Le **dessin de définition** décrit **une** pièce, complètement : formes, cotes, tolérances, états de surface. L'atelier doit pouvoir la fabriquer sans rien demander à personne.
- Le **dessin d'ensemble** montre les pièces **en place** les unes par rapport aux autres. Il sert à comprendre le fonctionnement, pas à fabriquer.

Le dessin d'ensemble s'accompagne d'une **nomenclature** : un tableau qui donne, pour chaque repère entouré sur le dessin, la désignation de la pièce, sa quantité et sa matière. C'est par là qu'on commence pour comprendre un mécanisme inconnu.

Et sur tout dessin, le **cartouche** donne le nom de la pièce, l'échelle, le matériau et le mode de projection. C'est le premier endroit où regarder : sans l'échelle et la projection, on peut lire tout le reste de travers.

## La projection européenne

{{fig:sc-projections}}

On rabat les vues **derrière** le plan de projection. D'où une disposition contre-intuitive, et c'est exactement ce que les sujets d'examen testent :

- la **vue de dessus** se place **en dessous** de la vue de face ;
- la **vue de gauche** se place **à droite** ;
- la vue de droite se place à gauche, la vue de dessous au-dessus.

(La projection américaine fait l'inverse, d'où le symbole du cartouche qui précise laquelle est utilisée.)

Les vues se correspondent : une hauteur lue sur la vue de face se retrouve à la même hauteur sur la vue de gauche, une largeur se retrouve à la même abscisse sur la vue de dessus. C'est ce qui permet de reconstruire une forme sans jamais la voir en perspective.

## Les traits disent tout

| Trait | Ce qu'il représente |
|---|---|
| Continu **fort** | arête ou contour **vu** |
| Interrompu fin | arête ou contour **caché** |
| Mixte fin | axe de symétrie ou de révolution |
| Continu fin | ligne de cote, hachures, ligne d'attache |

Un seul trait est fort : le contour vu. Tout le reste est fin. C'est ce contraste qui rend un dessin lisible d'un coup d'œil.

Deux lectures immédiates :

- un **trait interrompu**, c'est « c'est là, mais vous ne le verriez pas » — un perçage derrière la matière, une gorge intérieure ;
- un **cercle en trait fort avec deux traits mixtes croisés**, c'est une forme de révolution vue selon son axe. Reste à regarder une autre vue pour savoir si le cylindre rentre (perçage) ou sort (bossage).

## L'échelle ne change pas les cotes

**Une cote donne toujours la dimension de la pièce réelle**, quelle que soit l'échelle du dessin.

À l'échelle $2{:}1$, on dessine deux fois plus grand pour rendre lisible une petite pièce : le trait mesure $24$ mm sur le papier, mais la cote porte $12$, et la pièce mesure $12$ mm. On ne mesure jamais un dessin — les cotes sont là pour cela.

## Couper, pour voir l'intérieur

Un carter, un moyeu, un corps de vérin sont pleins de formes intérieures. En traits cachés, le dessin devient illisible.

On coupe alors la pièce par un plan, on retire la partie avant, et tout ce qui était caché devient **vu**.

{{fig:sc-coupe}}

Sur la vue où l'on définit la coupe :

- un **trait mixte fort** repère le plan de coupe ;
- deux **flèches** donnent la direction d'observation ;
- deux **lettres** nomment la coupe, et l'on écrit « A-A » sous la vue obtenue.

## La règle des hachures

> On hachure **ce que le plan de coupe traverse en matière**, et rien d'autre.

Deux conséquences, et ce sont les deux fautes les plus fréquentes sur une copie :

- **un trou n'est jamais hachuré** : ce n'est pas de la matière ;
- sur un dessin d'ensemble, **deux pièces voisines portent des hachures différentes** (inclinaison ou écartement), et chaque pièce garde les siennes dans toutes les vues. C'est ce qui permet de suivre une pièce d'un bout à l'autre du mécanisme.

Une convention à connaître : **vis, arbres, billes, clavettes et goupilles ne sont pas coupés** quand le plan les traverse dans leur longueur. Les couper ne montrerait rien d'utile et rendrait le dessin confus — on les dessine entiers, non hachurés, au milieu de la coupe.

## Coupe ou section

La **section** ne dessine que la surface coupée. Plus économe, elle suffit pour montrer la forme d'un arbre, d'une clavette, d'une nervure.

La **coupe** ajoute tout ce que l'on voit au-delà du plan.

Les deux sont hachurées de la même façon. La question tombe régulièrement à l'examen.

## Lire un dessin, dans l'ordre

1. le **cartouche** : nom, échelle, matériau, projection ;
2. les vues et leur disposition ;
3. les formes principales, vue par vue ;
4. la correspondance des traits cachés d'une vue avec les formes des autres ;
5. les cotes et leurs tolérances ;
6. les états de surface et les indications particulières.

L'étape 4 est le cœur du métier : c'est elle qui transforme trois dessins plats en un objet.
