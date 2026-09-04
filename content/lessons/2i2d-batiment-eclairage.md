# Éclairage et grandeurs photométriques

## Les quatre grandeurs à ne pas confondre

| Grandeur | Symbole | Définition | Unité |
|---|---|---|---|
| Flux lumineux | $\varphi$ | énergie émise par la source sous forme de rayonnements visibles, **dans toutes les directions**, par unité de temps | lumen (lm) |
| Intensité lumineuse | $I$ | importance du flux émis **dans une direction donnée** par une source ponctuelle | candela (cd) |
| Éclairement lumineux | $E$ | quantité de lumière **reçue par unité de surface** | lux (lx) |
| Efficacité lumineuse | $\eta$ | flux lumineux obtenu par watt électrique consommé | lm/W |

**1 lux = 1 lumen par mètre carré.** Trois de ces grandeurs décrivent la **source** ($\varphi$, $I$, $\eta$) ; une seule décrit ce que **reçoit** la surface ($E$).

{{fig:2i2d-grandeurs-photometriques}}

## La source, un convertisseur d'énergie

Une source lumineuse est un convertisseur : la grandeur d'**entrée** est la **puissance électrique** en watts, la grandeur de **sortie** est le **flux lumineux** en lumens. Son rendement est l'**efficacité lumineuse** :

$$\eta = \frac{\varphi}{P}$$

Exemple : une LED de $P = 15$ W émettant $\varphi = 1\,200$ lm a une efficacité $\eta = 1\,200/15 = \mathbf{80}$ lm/W. Erreur fréquente : calculer $P/\varphi$.

| Source | Principe | Ordre de grandeur de $\eta$ |
|---|---|---|
| Incandescence | un filament chauffé par le courant émet de la lumière | ≈ 15 lm/W |
| Décharge | un gaz ou une vapeur métallique émet de la lumière quand il est traversé par un courant | — |
| Fluorescence | une décharge dans la vapeur de mercure produit un ultraviolet, converti en lumière visible par une poudre fluorescente | — |
| LED, OLED | un composant électronique émet de la lumière quand il est parcouru par un courant | ≈ 100 lm/W |

Un filament porté à haute température rayonne surtout dans l'**infrarouge** : l'essentiel de l'énergie part en chaleur, d'où la très faible efficacité de l'incandescence.

{{fig:pc-corps-chauffe}}

Le livre retient **trois critères** pour caractériser une lampe : la **performance** (indice de rendu des couleurs, efficacité lumineuse, température de couleur), l'**économie** (puissance absorbée, durée de vie, coût) et l'**utilisation** (température de la lampe, temps d'allumage).

## Éclairement d'une surface

$$E = \frac{\varphi}{S} \qquad \text{(éclairement moyen, en lux)}$$

{{fig:2i2d-eclairement-surface}}

Pour une source ponctuelle éclairant perpendiculairement une surface située à la distance $d$ :

$$E = \frac{I}{d^2}$$

avec $I$ en candela et $d$ en mètres. **Doubler la distance divise l'éclairement par 4** : le même flux se répartit sur une surface quatre fois plus grande. Un spot de 200 cd à 2 m donne $E = 200/2^2 = 50$ lx.

## Dimensionner une installation

On remonte la chaîne **à l'envers** : du besoin sur la surface vers la puissance électrique.

1. relever l'éclairement $E$ (lux) exigé par le cahier des charges et la surface $S$ du local ;
2. calculer le flux total nécessaire $\varphi = E \times S$ ;
3. choisir un luminaire et relever son flux unitaire ;
4. calculer le nombre de luminaires $N = \varphi / \varphi_{\text{luminaire}}$, **arrondi à l'entier supérieur** ;
5. en déduire la puissance installée $P = \varphi / \eta$ et l'énergie annuelle $E_{\text{élec}} = P \times t$.

**Exemple** — atelier de 200 m² équipé de 12 luminaires LED de 20 W ($\eta = 100$ lm/W) :

- flux d'un luminaire : $\varphi = \eta P = 100 \times 20 = 2\,000$ lm ;
- flux total : $12 \times 2\,000 = 24\,000$ lm ;
- éclairement obtenu : $E = 24\,000/200 = \mathbf{120}$ lx — insuffisant si le cahier des charges impose 300 lx ;
- flux nécessaire : $300 \times 200 = 60\,000$ lm, soit $60\,000/2\,000 = \mathbf{30}$ luminaires ;
- puissance installée : $30 \times 20 = 600$ W, soit sur 2 000 h/an une consommation de **1 200 kWh**.

Avec des lampes à incandescence ($\eta = 15$ lm/W), les mêmes 60 000 lm auraient demandé $60\,000/15 = 4\,000$ W, soit **8 000 kWh par an** : la LED divise la facture d'éclairage par plus de six.
