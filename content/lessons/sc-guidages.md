# Guidage en rotation et en translation

## Ce qu'on demande à un guidage

Guider en rotation, c'est réaliser une **liaison pivot** : une seule mobilité autorisée, la rotation autour de l'axe. Les cinq autres — deux translations radiales, la translation axiale, deux basculements — doivent être supprimées.

Guider en translation, c'est réaliser une **glissière** : une seule translation autorisée.

Dans les deux cas, la question n'est pas *quelle liaison* — on le sait — mais **par quelle solution technologique**.

## Palier lisse ou roulement

{{fig:sc-roulement}}

Deux familles, deux compromis.

| | Palier lisse (coussinet) | Roulement |
|---|---|---|
| Contact | glissement | roulement |
| Frottement | élevé | très faible |
| Vitesse admissible | limitée | élevée |
| Encombrement | faible | plus important |
| Coût | faible | plus élevé |
| Bruit | silencieux | audible |

Le roulement remplace le frottement de glissement par du **roulement** : le couple à vaincre chute, l'échauffement aussi, le rendement monte. C'est tout son intérêt — et il le paie en encombrement et en prix.

On garde donc le coussinet partout où le frottement ne coûte rien : une charnière de portière s'ouvre quelques fois par jour, à vitesse nulle ou presque. **Un choix de conception, c'est accepter le bon défaut.**

## Choisir son roulement

La forme du corps roulant décide de ce que le roulement supporte.

| Type | Supporte le mieux |
|---|---|
| Billes | charges radiales modérées, grandes vitesses |
| Rouleaux | charges radiales élevées |
| Butée à billes | charges axiales seulement |
| Rotule | charges avec défaut d'alignement de l'arbre |

Un point de contact (bille) tourne vite mais porte peu ; une ligne de contact (rouleau) porte davantage. La butée n'accepte aucune charge radiale.

## La règle des ajustements

C'est la règle qu'un sujet d'examen demande toujours de justifier.

> La bague qui **tourne par rapport à la charge** est montée **serrée**.
> La bague **fixe par rapport à la charge** est montée **glissante**.

Pourquoi ? Une bague montée avec jeu alors qu'elle tourne sous la charge finit par **tourner dans son logement** : elle le mate, le jeu grandit, et le montage est ruiné.

Le cas courant : un arbre qui tourne dans un bâti fixe, avec une charge de direction constante (un poids). La bague intérieure tourne par rapport à cette charge $\rightarrow$ serrée sur l'arbre. La bague extérieure ne tourne pas par rapport à elle $\rightarrow$ glissante dans le logement.

## Les arrêts axiaux

{{fig:sc-montage-roulements}}

Un guidage en rotation doit bloquer la translation axiale **dans les deux sens**. Chaque bague est donc arrêtée de chaque côté : épaulement, anneau élastique, écrou, couvercle, entretoise.

C'est le défaut de montage le plus fréquent : sans arrêt, la bague se déplace, le contact se déporte sur le bord des chemins de roulement, et la durée de vie s'effondre.

## Côté fixe et côté libre

Un arbre chauffe, donc s'allonge. Pour un arbre en acier de $800$ mm et $40\ ^\circ$C d'échauffement :

$$\Delta L=\alpha\,L\,\Delta T$$
$$\Delta L=12\times10^{-6}\times800\times40=0{,}38\ \mathrm{mm}$$

Presque quatre dixièmes — bien plus que le jeu interne d'un roulement, qui se compte en centièmes. Si les deux roulements étaient bloqués axialement, cette dilatation créerait un effort énorme qui les détruirait.

D'où la règle des montages à deux roulements éloignés : **un côté fixe**, qui positionne l'arbre, et **un côté libre**, qui laisse passer la dilatation.

## La lubrification

Le lubrifiant sépare les surfaces par un film de quelques micromètres : il réduit le frottement et l'usure, et emporte la chaleur produite. Graisse pour les montages fermés et lents, huile pour les vitesses élevées.

Il ne rattrape aucun jeu et n'apporte aucune rigidité : ce n'est pas son rôle.

## La démarche, toujours la même

1. identifier la liaison à réaliser ;
2. relever la **charge**, sa direction, et la vitesse de rotation ;
3. décider entre palier lisse et roulement ;
4. choisir le type de roulement adapté à la direction de la charge ;
5. déterminer quelle bague tourne par rapport à la charge, donc les ajustements ;
6. prévoir les arrêts axiaux, et le côté libre s'il y a lieu ;
7. choisir la lubrification et l'étanchéité.

La charge et la vitesse viennent en premier : ce sont elles qui éliminent des familles entières de solutions.

## Guidage en translation

Mêmes principes, autre direction. Les solutions courantes :

- **queue d'aronde** : deux surfaces en V inversé, réglable par un lardon, très rigide ;
- **rail à billes** : le roulement appliqué à la translation, frottement très faible ;
- **arbre et douilles** : simple et économique, sur deux arbres parallèles ;
- **glissière en V** : auto-centrante, courante sur les machines-outils.

Et la même exigence : bloquer **toutes** les mobilités sauf une, et arrêter la pièce en fin de course.
