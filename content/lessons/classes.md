# Les classes d'équivalence cinématique

Avant de tracer un schéma, on **simplifie** le mécanisme : les pièces qui **n'ont aucun mouvement relatif**
(assemblées par vis, rivet, soudure, emmanchement…) bougent comme **un seul solide**. On les regroupe
dans une même **classe d'équivalence cinématique**, et on leur donne **une couleur**.

Règles :

- deux pièces en **encastrement** sont dans la même classe ;
- les **pièces déformables** (ressorts, joints, courroies, câbles) sont **exclues** ;
- le bâti (solide de référence, souvent fixe) est une classe comme les autres, souvent notée 0 ou E1.

## Exemple : le serre-joint

{{fig:mecanisme-serre-joint-dessin}}

Le rail 2 est riveté (1) dans la mâchoire fixe 3 ; la poignée 6 est emmanchée sur la vis 5.
On obtient 4 classes :

{{fig:mecanisme-serre-joint-classes}}

- **E1** = {1, 2, 3} : rail + mâchoire fixe (bâti)
- **E2** = {4} : coulisseau
- **E3** = {5, 6} : vis + poignée
- **E4** = {7} : patin

## Exemple : l'étau d'établi

{{fig:mecanisme-etau-dessin}}

Plus de pièces, mais la même règle : l'écrou 2 est emmanché dans le corps 1 et la mordache 6
est vissée sur le mors fixe ; la mordache 7 est vissée sur le mors mobile 3. La barre 5, elle,
coulisse dans la tête de la vis 4 : elle n'est pas solidaire de la vis.

{{fig:mecanisme-etau-classes}}

- **E1** = {1, 2, 6} : bâti + écrou + mordache fixe
- **E2** = {3, 7} : mors mobile + sa mordache
- **E3** = {4} : vis de manœuvre
- **E4** = {5} : barre de manœuvre
