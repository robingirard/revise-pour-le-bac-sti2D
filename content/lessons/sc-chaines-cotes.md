# Cotation fonctionnelle et chaînes de cotes

## Un jeu ne se cote pas

Une **condition fonctionnelle** est une exigence de l'assemblage : « il doit rester entre $0{,}5$ et $1{,}5$ mm de jeu pour que la roue tourne librement sans battre ».

Elle n'est portée sur **aucun** dessin de définition. La raison est logique : un dessin de définition décrit **une** pièce, que l'atelier doit fabriquer seule. Le jeu, lui, n'existe qu'une fois les pièces assemblées.

On cote donc les pièces, et le jeu en résulte. Reste à savoir comment.

## La chaîne de cotes

{{fig:sc-chaine-cotes}}

On part d'une face du jeu, on traverse les pièces jusqu'à l'autre face, en notant **une cote par pièce traversée**. La chaîne se referme sur elle-même : c'est ce qui permet d'écrire une relation.

On oriente ensuite chaque cote par une flèche :

- cote dans le **même sens** que la condition $\rightarrow$ elle compte $+$ ;
- cote en **sens inverse** $\rightarrow$ elle compte $-$.

Sur cette chaîne, $A_1$ va dans le sens de $J_a$, $A_2$ et $A_3$ en sens inverse :

$$J_a = A_1 - A_2 - A_3$$

Avec $A_1=60$, $A_2=25$ et $A_3=34$ mm, le jeu nominal vaut $60-25-34=1$ mm.

## Le pire cas, jamais la moyenne

On assemble des pièces prises au hasard dans des lots. Si le calcul ne tient qu'« en moyenne », une partie des assemblages ne fonctionnera pas — et il faudra trier les pièces, ce qui coûte bien plus cher que d'avoir prévu large.

On calcule donc les deux extrêmes :

$$J_{a\max} = A_{1\max} - A_{2\min} - A_{3\min}$$
$$J_{a\min} = A_{1\min} - A_{2\max} - A_{3\max}$$

**Maxi pour les cotes positives, mini pour les négatives** — et l'inverse pour le jeu minimal. C'est là que se produit l'erreur la plus fréquente : prendre toutes les cotes au maximum pour obtenir le jeu maximal.

Avec $A_1=60\pm0{,}1$, $A_2=25\pm0{,}05$, $A_3=34\pm0{,}05$ :

$$J_{a\max}=60{,}1-24{,}95-33{,}95=1{,}2\ \mathrm{mm}$$
$$J_{a\min}=59{,}9-25{,}05-34{,}05=0{,}8\ \mathrm{mm}$$

## Les tolérances s'additionnent

$$IT(J_a) = IT(A_1) + IT(A_2) + IT(A_3)$$

**Toujours une somme**, quel que soit le signe des cotes : chaque pièce ajoute sa propre dispersion, et rien ne se compense.

Vérification sur l'exemple : $0{,}2+0{,}1+0{,}1=0{,}4$ mm, et l'on a bien $1{,}2-0{,}8=0{,}4$. Quand les deux chemins concordent, le calcul est juste.

## La conséquence, qui est une règle de conception

Ajouter une pièce dans la chaîne, c'est ajouter un $IT$ à la somme. Donc :

> **Une chaîne courte est une chaîne précise.**

Pour tenir un jeu serré, on réduit d'abord le **nombre de pièces** entre ses deux faces. Resserrer toutes les tolérances marche aussi, mais coûte bien plus cher — chaque centième gagné se paie en procédé, en contrôle et en rebut.

Et si la chaîne est imposée, on agit sur la cote dont l'$IT$ est le plus gros : c'est elle qui domine la somme.

## Dimensionner à l'envers

L'exercice se pose aussi dans l'autre sens : le cahier des charges donne le jeu, il faut en déduire les tolérances.

Si trois cotes de même tolérance $t$ doivent tenir un jeu entre $0{,}2$ et $0{,}6$ mm :

$$3t \leqslant 0{,}6-0{,}2 = 0{,}4$$
$$t \leqslant 0{,}13\ \mathrm{mm}$$

## La méthode

1. repérer la condition fonctionnelle et ses **deux faces** ;
2. tracer la chaîne, une cote par pièce traversée ;
3. orienter chaque cote et lui donner son signe ;
4. écrire la relation ;
5. calculer le jeu nominal, puis le maxi et le mini ;
6. **vérifier que l'intervalle obtenu respecte le cahier des charges**.

La dernière étape est celle qu'on oublie. Calculer un jeu ne sert à rien si l'on ne conclut pas — et conclure peut vouloir dire : « les tolérances conviennent, et il reste même de la marge : on pourrait les élargir pour réduire le coût. » Élargir une tolérance trop serrée est une vraie décision de conception.
