# Énergie, puissance et rendement

## Formes et sources d'énergie

Le cours distingue **quatre formes d'énergie** :

| Forme d'énergie | De quoi dépend-elle ? |
|---|---|
| **chimique** | des liaisons chimiques (pétrole, charbon, gaz…) |
| **mécanique** | du mouvement (énergie **cinétique**) et de l'altitude (énergie **potentielle**) |
| **thermique** | de la température du corps |
| **nucléaire** | de la **fission** de noyaux atomiques |

Une source d'énergie est **renouvelable** si elle est exploitable de façon **illimitée à l'échelle humaine** :
biomasse (bois), hydraulique (barrages), éolien, solaire, géothermie.
Elle est **non renouvelable** dans le cas contraire : le **nucléaire** et les **énergies fossiles**
(pétrole, gaz, charbon), fabriquées sur des temps géologiques.

## Transferts d'énergie et chaîne énergétique

Un système transfère de l'énergie à un autre de **quatre** manières :

- **thermique** : toujours du corps le plus chaud vers le corps le plus froid ;
- **par rayonnement** : le Soleil vers la Terre, par exemple ;
- **mécanique** : lors d'un déplacement ou du travail de forces ;
- **électrique** : l'électricité circule du producteur au consommateur par les lignes haute et basse tension.

{{fig:pc-chaine-energetique}}

Sur une **chaîne énergétique** : les **formes d'énergie sont encadrées**, le **convertisseur est entouré**,
et la **nature du transfert est écrite au-dessus des flèches**.

## Rendement d'un convertisseur

L'énergie **se conserve** : elle se convertit sous différentes formes, dont l'**énergie utile** et l'**énergie
thermique perdue** dans l'environnement.

{{fig:pc-bilan-convertisseur}}

$\eta = \dfrac{E_{\text{utile}}}{E_{\text{reçue}}}$ — sans unité (ou en %), toujours **compris entre 0 et 100 %**.

Les deux énergies doivent être exprimées dans la **même unité** (J ou kWh).
Énergie absorbée = énergie utile + pertes.

## Puissance moyenne et puissance instantanée

Toute **énergie** s'exprime en **joule (J)** ; toute **puissance** s'exprime en **watt (W)**.

**Puissance moyenne** sur une durée $\Delta t$ : $P = \dfrac{\Delta E}{\Delta t} = \dfrac{E_2 - E_1}{t_2 - t_1}$

**Puissance instantanée** : $p(t) = \dfrac{\mathrm{d}e(t)}{\mathrm{d}t}$ — c'est la **pente** de la courbe $e(t)$.

{{fig:pc-energie-temps}}

Sur ce relevé, la puissance vaut 2 kW pendant les deux rampes (de 0 à 6 h puis de 12 à 18 h) et **0 kW** sur
les paliers, où l'énergie n'augmente plus.

| Grandeur | Unités possibles |
|---|---|
| énergie $\Delta E$ | joule (J), wattheure (Wh), kilowattheure (kWh) |
| puissance $P$ | watt (W), kilowatt (kW) |
| durée $\Delta t$ | seconde (s), heure (h) |

## Le kilowattheure

$1\ \text{Wh} = 3\,600\ \text{J}$ et $1\ \text{kWh} = 3{,}6 \times 10^{6}\ \text{J}$.

Exemple : un téléviseur OLED de 40 W consomme en 1 h une énergie
$40 \times 3\,600 = 144\,000\ \text{J}$, soit 144 kJ — ou encore 40 Wh.

Astuce : si $P$ est en kW et $\Delta t$ en h, alors $\Delta E = P \times \Delta t$ est directement en kWh,
l'unité de la facture d'électricité.
