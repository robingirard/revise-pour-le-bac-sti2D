# Panneaux photovoltaïques

## Irradiance, surface, rendement

{{fig:2i2d-pv-orientation}}

L'**irradiance** $E_{\text{irr}}$ est la puissance lumineuse reçue par unité de surface, en **W·m⁻²** (mesurée au solarimètre). Par ciel dégagé, elle atteint environ 1 000 W·m⁻² au sol.

La puissance lumineuse reçue par un module de surface $S$ vaut $P_{\text{reçue}} = E_{\text{irr}} \times S$, et son rendement :

$$\eta = \frac{P_{\text{électrique}}}{E_{\text{irr}} \times S}$$

La **puissance crête**, en watts-crête (Wc), est la puissance électrique délivrée dans les **conditions de référence** : irradiance 1 000 W·m⁻², cellule à 25 °C. C'est une caractéristique normalisée du matériel, pas un record de production.

**Exemple** — panneau CENIT 220 du ferry-boat de Marseille : $1{,}635 \times 0{,}984 = 1{,}609$ m², 220 Wc. Rendement : $\eta = \dfrac{220}{1\,000 \times 1{,}609} = 0{,}137$, soit **13,7 %**, conforme aux 13,8 % annoncés. Plus de 86 % de l'énergie solaire reçue n'est donc pas convertie en électricité.

Un module photovoltaïque est un générateur de **courant continu** : pour alimenter le réseau, il faut un **onduleur**.

## Associer des cellules

{{fig:2i2d-pv-associations}}

Comme pour les batteries :

- **en série**, les tensions s'additionnent, le courant ne change pas ;
- **en parallèle**, la tension ne change pas, les courants s'additionnent.

Quatre cellules identiques de 18 V et 5,56 A (soit 100 W chacune) :

| Branchement | Tension | Courant | Puissance |
|---|---|---|---|
| 4 en parallèle | 18 V | 22,24 A | 400 W |
| 2 × 2 en série-parallèle | 36 V | 11,12 A | 400 W |
| 4 en série | 72 V | 5,56 A | 400 W |

**La puissance délivrée est la même dans les trois cas** : le branchement fixe le couple ($U$, $I$), pas leur produit. On le choisit pour adapter la tension au convertisseur placé en aval.

*Précision de calcul* : $4 \times 5{,}56 = 22{,}24$ A et $18 \times 22{,}24 = 400{,}3$ W. On lit souvent 22,2 A, puis 400 W ; ne jamais réutiliser une valeur arrondie dans un calcul suivant.

## Production journalière

Pour une installation de puissance crête $P_{\text{crête}}$, on estime la production quotidienne par le nombre d'**heures équivalent plein soleil** $h$ :

$$E_{\text{jour}} = P_{\text{crête}} \times h$$

**Exemple** — les 16 panneaux de propulsion du ferry donnent $16 \times 220 = 3\,520$ Wc, soit 3,52 kWc. La simulation annonce 17,9 kWh en juillet à Marseille, ce qui correspond à $17{,}9 / 3{,}52 = 5{,}1$ heures équivalent plein soleil.

La production varie fortement dans l'année : environ 4,3 kWh/jour en janvier contre 18,3 kWh/jour en juin, à cause de la hauteur du Soleil et de la durée du jour.

{{fig:2i2d-ferry-bilan}}

## Orientation et inclinaison

La puissance captée dépend de l'**angle d'incidence** du rayonnement : elle est maximale quand les rayons arrivent perpendiculairement au plan du panneau. En France métropolitaine, l'optimum annuel est voisin d'une orientation **plein sud** et d'une inclinaison de **30 à 35°**.

Sur le ferry-boat, les panneaux sont posés **à plat** (inclinaison 0°). Ce choix n'est pas optimal en rendement, mais c'est le seul cohérent pour un bateau : le ferry change constamment de cap, une inclinaison orientée serait tantôt favorable, tantôt défavorable. À inclinaison nulle, l'orientation saisie dans le modèle n'a d'ailleurs **aucun effet** : un plan horizontal est identique à lui-même par rotation autour de la verticale. S'ajoutent deux avantages pratiques : pas de prise au vent et pas de surcharge de structure.

Enfin, à rendement et irradiance donnés, $P_{\text{crête}} = \eta \times E_{\text{irr}} \times S$ : la production est **proportionnelle à la surface** installée.
