# Les degrés de liberté des liaisons

Le tableau des liaisons donne, pour chacune, les mouvements **possibles** entre les deux pièces :
**T** pour une translation, **R** pour une rotation, suivant chacun des axes x, y, z.

Retenez la logique plutôt que la liste :

- **Encastrement** : rien ne bouge → 0 ddl.
- **Pivot** : une seule rotation, autour de son axe → 1 ddl (Rx pour un axe x).
- **Glissière** : une seule translation, le long de son axe → 1 ddl (Tx).
- **Hélicoïdale** (vis-écrou) : translation **et** rotation autour de l'axe, mais **liées** entre elles → 1 seul ddl indépendant.
- **Pivot glissant** : translation et rotation **indépendantes** autour de l'axe → 2 ddl.
- **Rotule** : les 3 rotations autour du centre → 3 ddl.
- **Appui plan** : glisse dans le plan (2 translations) et tourne autour de la normale (1 rotation) → 3 ddl.
- **Linéaire rectiligne** (cylindre sur plan) : appui plan + rotation autour de la ligne de contact → 4 ddl.
- **Linéaire annulaire** (sphère dans cylindre) : rotule + translation le long du cylindre → 4 ddl.
- **Ponctuelle** (sphère sur plan) : tout sauf la translation suivant la normale → 5 ddl.

{{table:ddl}}
