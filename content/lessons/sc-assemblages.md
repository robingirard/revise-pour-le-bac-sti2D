# Solutions constructives d'assemblage

## Deux grandes familles

La première question à poser devant un cahier des charges est celle de la **démontabilité** : peut-on défaire l'assemblage sans détériorer les pièces ?

| Démontables | Non démontables |
|---|---|
| Vis d'assemblage | Soudage |
| Boulon (vis + écrou) | Collage |
| Goujon | Rivetage |
| Vis de pression | Emmanchement conique |
| Anneau élastique (circlip) | Ajustement avec serrage |

C'est un critère **éliminatoire** : « démontable aisément » supprime d'un coup toute la colonne de droite.

## Les solutions filetées

| Solution | Principe | Quand l'utiliser |
|---|---|---|
| Vis d'assemblage | se visse dans un **taraudage** de la pièce | une des deux pièces peut être taraudée |
| Boulon | traverse les deux pièces, un **écrou** serre de l'autre côté | aucune pièce ne peut être taraudée |
| Goujon | tige filetée aux deux bouts, vissée **à demeure** | montages démontés souvent, matériau tendre |
| Vis de pression | petite vis qui **appuie** sur une pièce pour la bloquer | petits couples, solution économique |

Le goujon mérite une explication : il reste en place, et seul l'écrou est manipulé à chaque démontage. Le filetage de la pièce — souvent en aluminium ou en fonte — n'est donc pas usé par les montages successifs.

La vis de pression, elle, mate l'arbre et y laisse une empreinte qui gêne les démontages suivants ; le couple transmis ne tient que par adhérence sur une très petite surface. On usine un **méplat** pour qu'elle porte proprement.

## Les solutions non démontables

- **Soudage** : la matière fond localement, les deux pièces n'en font plus qu'une. Solide et économique, mais les pièces doivent être positionnées *avant*, par un montage — une soudure ne positionne rien.
- **Collage** : assemble sans percer, sans chauffer, sans ajouter de masse, y compris entre matériaux différents. Il travaille bien en cisaillement, mal en **pelage** et en arrachement, et il vieillit.
- **Rivetage** : une tige traversante dont on écrase la queue pour former une seconde tête. Léger, rapide, bon marché — il faut percer le rivet pour le déposer.
- **Emmanchement conique** : deux surfaces coniques identiques qui s'emboîtent. Le contact **centre et bloque en même temps**, et le serrage croît à l'enfoncement. C'est la solution des porte-outils de machines-outils.
- **Ajustement avec serrage** : l'arbre est légèrement plus gros que l'alésage ; au montage, les deux pièces se déforment élastiquement et la pression de contact suffit à transmettre l'effort. Cela se note $\varnothing20$ H7/p6.

## Transmettre un couple entre un arbre et un moyeu

Il faut bien distinguer les solutions qui **transmettent un couple** de celles qui **arrêtent en translation** — elles ne sont pas interchangeables.

| Solution | Transmet un couple | Arrête axialement |
|---|---|---|
| Clavette | oui | non |
| Cannelures | oui, couple élevé | non (coulissement possible) |
| Goupille | oui | oui |
| Vis de pression | oui, petit couple | oui, imprécis |
| Épaulement | non | oui, précis |
| Anneau élastique | non | oui |
| Écrou | non | oui, avec précontrainte |

- La **clavette** est la solution courante : simple, économique, un seul usinage sur chaque pièce.
- Les **cannelures** répartissent le couple sur toutes leurs dents : effort transmissible bien plus élevé, et coulissement axial possible sous charge. Plus chères, donc réservées aux cas qui l'exigent.
- La **goupille** bloque rotation et translation d'un coup. Mais le perçage traversant affaiblit l'arbre là où les contraintes sont les plus fortes ; la goupille devient le point de rupture — ce qui est parfois **voulu**, comme sécurité.

## Un organe, une fonction

La règle qui rend un montage lisible, calculable et réparable : on affecte **une solution à chaque fonction**.

Pour monter une roue dentée qui doit transmettre un couple élevé, rester démontable et être positionnée précisément :

- cannelures pour le couple ;
- épaulement usiné pour la position axiale d'un côté ;
- écrou ou anneau élastique de l'autre, puisqu'une butée n'agit que dans un sens.

Un épaulement de chaque côté serait plus simple — mais il deviendrait impossible d'enfiler la roue sur l'arbre.

## Deux règles qu'on oublie souvent

**La rondelle.** La tête d'une vis appuie sur une petite surface, où la pression est élevée et marque les matériaux tendres. La rondelle étale cette pression.

**Le freinage.** Sous vibrations, une liaison filetée se desserre toute seule. Il faut donc toujours lui associer un dispositif : rondelle frein, écrou autofreiné, frein filet ou goupille fendue. Ce n'est pas une précaution facultative, c'est une règle de conception.
