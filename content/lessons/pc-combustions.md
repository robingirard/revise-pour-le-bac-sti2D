# Combustions et bilan de matière

## Hydrocarbures et alcools

Les **hydrocarbures** ne contiennent que des atomes de carbone et d'hydrogène. Pour $n$ atomes de carbone :

| Famille | Formule brute | Liaisons | Exemples |
|---|---|---|---|
| **Alcanes** | $\mathrm{C_nH_{2n+2}}$ | uniquement des liaisons simples C–C et C–H | méthane $\mathrm{CH_4}$, propane $\mathrm{C_3H_8}$, butane $\mathrm{C_4H_{10}}$ |
| **Alcènes** | $\mathrm{C_nH_{2n}}$ | **une seule** liaison double $\mathrm{C}=\mathrm{C}$ | éthène $\mathrm{C_2H_4}$, propène $\mathrm{C_3H_6}$ |
| **Alcools** | $\mathrm{C_nH_{2n+1}OH}$, soit $\mathrm{C_nH_{2n+2}O}$ | un groupe hydroxyle $-\mathrm{OH}$ | méthanol $\mathrm{CH_3-OH}$, éthanol $\mathrm{C_2H_5-OH}$ |

{{fig:pc-formules-developpees}}

Tout **alcool** contient **un** atome d'oxygène, formant un groupe hydroxyle $-\mathrm{OH}$ avec un atome d'hydrogène. Le carburant **SP95-E10** contient **10 % d'éthanol**, ce qui limite les rejets de $\mathrm{CO_2}$.

## Combustion complète ou incomplète

Tout dépend de la quantité de **comburant** disponible :

- **complète** (dioxygène **en excès**) : il se forme du **dioxyde de carbone** $\mathrm{CO_2}$ et de l'**eau** $\mathrm{H_2O}$ — exemple : $\mathrm{CH_4} + 2\,\mathrm{O_2} \rightarrow \mathrm{CO_2} + 2\,\mathrm{H_2O}$ ;
- **incomplète** (dioxygène **en défaut**) : à $\mathrm{CO_2}$ et $\mathrm{H_2O}$ s'ajoutent le **monoxyde de carbone** $\mathrm{CO}$ et du **carbone** C (suie) — exemple : $4\,\mathrm{CH_4} + 6\,\mathrm{O_2} \rightarrow \mathrm{CO_2} + 8\,\mathrm{H_2O} + 2\,\mathrm{CO} + \mathrm{C}$.

**Le monoxyde de carbone est très dangereux** : **incolore et inodore**, il est indétectable par l'être humain, alors qu'il s'agit d'un **gaz mortel**.

## Ajuster une équation

Les atomes se conservent : on compte élément par élément, de chaque côté de la flèche. Pour $\mathrm{C_3H_8} + 5\,\mathrm{O_2} \rightarrow 3\,\mathrm{CO_2} + 4\,\mathrm{H_2O}$ : 3 C à gauche et 3 à droite ; 8 H et $4\times 2 = 8$ ; $5\times 2 = 10$ O et $3\times 2 + 4 = 10$ — l'équation est ajustée.

Piège classique : $\mathrm{O_2}$ apporte **deux** atomes d'oxygène, pas un ; et l'oxygène du groupe $-\mathrm{OH}$ d'un alcool compte lui aussi.

## Avancement et bilan de matière

L'**avancement**, noté $x$ et exprimé en **mole (mol)**, mesure l'évolution de la transformation : il varie de **0** à sa valeur maximale $x_{\max}$, atteinte **lorsqu'au moins un des réactifs a été totalement consommé**.

{{fig:pc-tableau-avancement}}

**Exemple : 2 mol de $\mathrm{CH_4}$ et 10 mol de $\mathrm{O_2}$**, avec $\mathrm{CH_4} + 2\,\mathrm{O_2} \rightarrow \mathrm{CO_2} + 2\,\mathrm{H_2O}$ :

| État du système | $\mathrm{CH_4}$ | $2\,\mathrm{O_2}$ | $\mathrm{CO_2}$ | $2\,\mathrm{H_2O}$ |
|---|---|---|---|---|
| initial ($x = 0$) | 2 | 10 | 0 | 0 |
| intermédiaire ($0 < x < x_{\max}$) | $2 - x$ | $10 - 2x$ | $x$ | $2x$ |
| final ($x_{\max} = 2$ mol) | 0 | 6 | 2 | 4 |

Deux hypothèses pour $x_{\max}$ : si $\mathrm{CH_4}$ est limitant, $2 - x_{\max} = 0$ donne $x_{\max} = 2$ mol ; si $\mathrm{O_2}$ est limitant, $10 - 2x_{\max} = 0$ donne $x_{\max} = 5$ mol. **On retient toujours la plus petite valeur**, sinon une quantité de matière serait **négative** à l'état final. Ici $x_{\max} = 2$ mol : le méthane est le **réactif limitant**, le dioxygène est en excès.

## La méthode, en cinq temps

Écrire et **ajuster** l'équation → relever les quantités de matière initiales (au besoin avec $n = \dfrac{m}{M}$) → construire le **tableau d'avancement** → chercher $x_{\max}$ en annulant tour à tour chaque réactif et retenir la plus petite valeur → remplacer $x$ par $x_{\max}$ pour obtenir l'**état final**, puis, si besoin, les masses avec $m = n \times M$.
