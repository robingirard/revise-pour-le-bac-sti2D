# Les symboles des liaisons

Chaque liaison normalisée a un **symbole** (norme NF EN ISO 3952). Sur le schéma, les deux solides liés
sont dessinés de **deux couleurs** différentes : dans nos figures, le solide « intérieur » (arbre, sphère…)
est **rouge**, le solide « extérieur » (alésage, plan, coupelle…) est **bleu**.

Un même symbole change d'aspect selon la **vue** :

- **vue selon l'axe** (l'axe de la liaison pointe vers vous) : on voit un **cercle** ou un **carré** ;
- **vue de face** (l'axe est dans le plan de la feuille) : on voit un **rectangle** traversé par l'axe.

Le point **A** est le **centre** (ou point caractéristique) de la liaison ; le repère indique les axes du plan de la vue.

{{table:symboles}}

## Les symboles en perspective

Les manuels et les sujets de bac utilisent aussi la représentation **en perspective** (3D) de la norme :
elle montre d'un coup les surfaces en contact (cylindre dans un alésage, sphère dans une coupelle, prisme
dans un fourreau…). Même code couleur : solide 1 en rouge, solide 2 en bleu.

{{table:symboles3d}}

## Faire bouger les symboles

Touche un symbole (ou survole-le à la souris) pour l'animer : le solide 1, en **rouge**, fait alors
un mouvement que la liaison autorise.

Un dessin est plat, mais la liaison, elle, bouge dans l'espace. L'animation utilise donc **quatre
indices**, qui peuvent se combiner — compte-les, ils donnent les degrés de liberté :

| ce que fait le solide rouge | ce que ça veut dire |
|---|---|
| il **tourne** dans la feuille | rotation autour de l'axe qui pointe vers toi |
| il **glisse** dans la feuille | translation dans le plan du dessin |
| il **grossit et devient vif**, puis rapetisse et pâlit | translation **vers toi** : elle est dirigée le long de l'axe de visée, on ne peut pas la dessiner autrement |
| il **s'écrase** (il se raccourcit) | il **bascule hors de la feuille** : il peut sortir du plan |

Vues selon l'axe, plusieurs symboles se ressemblent beaucoup : c'est l'animation qui les sépare.

- **Pivot** : il tourne, et rien d'autre → 1 ddl.
- **Glissière** : il va et vient en profondeur, sans tourner → 1 ddl.
- **Hélicoïdale** : il tourne et avance **ensemble**, un aller-retour par tour → les deux mouvements
  sont liés, comme une vis dans son écrou : elle n'avance que parce qu'elle tourne → 1 ddl.
- **Pivot glissant** : il tourne **et** va et vient, chacun à son rythme → 2 mouvements indépendants.
- **Rotule** : il tourne **et s'écrase** → il tourne aussi hors de la feuille, dans toutes les
  directions → 3 rotations.
- **Ponctuelle** : il tourne, s'écrase **et se promène** sur le plan → il ne lui manque que la
  translation qui l'enfoncerait dans le plan → 5 ddl.

Deux réserves honnêtes : vue **de face**, un arbre qui tourne autour de son propre axe ne montre
rien du tout (le pivot y semble donc figé comme un encastrement, et la glissière, l'hélicoïdale et
le pivot glissant s'y ressemblent). C'est le **symbole** qui tranche alors — épaulements, filetage —
et c'est la vue selon l'axe qu'il faut regarder pour voir bouger.

## Astuces pour ne pas confondre

- **Pivot** vue de face : le rectangle est traversé par l'arbre **avec deux petits traits** (épaulements) qui bloquent la translation.
- **Pivot glissant** : même rectangle, arbre traversant **sans** épaulement ; vue selon l'axe : cercle **avec un point** au centre.
- **Glissière** : vue selon l'axe : **carré avec une croix** ; vue de face : rectangle avec l'arbre visible **seulement à l'extérieur**.
- **Hélicoïdale** : rectangle avec une **ligne ondulée** (le filetage).
- **Rotule** : cercle (sphère) dans une **coupelle**.
