# Inertie, confort et réglementation

*Prérequis : la compétence **Déperditions et bilan thermique d'une pièce**.*

Isoler ne suffit pas : un bâtiment doit aussi **stocker**, **amortir** et **réguler**. C'est ce qui sépare un local conforme au calcul d'un local réellement confortable.

## Chaleur sensible et chaleur latente

- **Chaleur sensible** : la part de la chaleur échangée qui **fait varier la température**. Exemple du livre : chauffer l'eau de 0 °C à 100 °C demande **419 kJ/kg**.
- **Chaleur latente** : la part qui **fait changer d'état** le système, à température constante. Exemple : vaporiser cette eau demande **2 257 kJ/kg**, soit plus de cinq fois plus.

$$Q = m \times C \times (T_{\text{finale}} - T_{\text{initiale}})$$

$Q$ en joules, $m$ en kg, $C$ la **chaleur massique** en **J/(kg·K)**, les deux températures dans la même unité (°C ou K). La chaleur massique « caractérise la capacité de stockage d'énergie thermique » d'un matériau.

Rappel de conversion : $T\,(\text{K}) = \theta\,(^\circ\text{C}) + 273{,}15$. Mais une **variation** de température s'exprime indifféremment en °C ou en K : passer de 5 °C à 20 °C, c'est +15 °C **ou** +15 K.

{{fig:pc-echelle-temperature}}

## L'inertie thermique

L'inertie, c'est la capacité de la masse du bâtiment à **stocker** l'énergie. Elle se mesure par le produit $m \times C$.

**Exemple** — dalle de béton de 4 m × 5 m × 0,20 m, $\rho = 2\,300$ kg/m³, $C = 880$ J/(kg·K) :
$m = 4 \times 5 \times 0{,}20 \times 2\,300 = \mathbf{9\,200}$ kg, et pour **1 °C** d'élévation
$Q = 9\,200 \times 880 \times 1 = 8{,}1 \times 10^{6}$ J $= \mathbf{2{,}25}$ **kWh**.

Chaque degré gagné par la dalle représente plus de deux heures de fonctionnement d'un convecteur de 1 kW.

{{fig:2i2d-inertie-thermique}}

Conséquences pratiques :

- une **forte inertie** (béton, pierre, isolation par l'extérieur) **retarde** et **atténue** le pic de température : c'est le confort d'été sans climatisation, à condition de sur-ventiler la nuit ;
- une **faible inertie** (ossature bois, isolation par l'intérieur) chauffe vite mais surchauffe vite : il faut alors soigner les **protections solaires**.

## La température ressentie

Le corps échange par convection avec l'air **et** par rayonnement avec les parois. On modélise la sensation par la moyenne des deux :

$$T_{\text{ressentie}} \approx \frac{T_{\text{air}} + T_{\text{parois}}}{2}$$

{{fig:2i2d-confort-parois}}

- parois froides à 15 °C, air à 21 °C → $T_{\text{ressentie}} = 18$ °C : on a froid malgré un thermostat élevé ;
- après isolation, parois à 19 °C : un air à **17 °C** suffit pour ressentir les mêmes 18 °C.

Isoler, c'est donc **pouvoir baisser la consigne**. Et l'inverse coûte cher : passer la consigne de 19 °C à 20 °C avec −1 °C dehors fait passer $\Delta T$ de 20 K à 21 K, soit **+5 % de déperditions**.

## La dilatation thermique

$$\Delta L = L_0 \times \alpha \times \Delta\theta$$

$\Delta L$ et $L_0$ en m, $\alpha$ le coefficient de dilatation linéaire en °C⁻¹, $\Delta\theta$ en °C. Une poutre de 10 m ($\alpha = 12 \times 10^{-6}$ °C⁻¹) soumise à 40 °C de variation s'allonge de **4,8 mm**. D'où les **joints de dilatation** : on accompagne le mouvement au lieu de le contrarier, sous peine de fissures.

## Réglementation et leviers du confort

| Résistance thermique minimale (m²·K/W) | RT 2005 | « Basse énergie » | « Très basse énergie » |
|---|---|---|---|
| Toit | 5,0 | 6,7 | 10 |
| Plancher | 2,0 | 3,3 | 6,7 |
| Façade | 2,2 | 3,3 | 6,7 |

*(Consommations associées : 130 kWh·m⁻²·an⁻¹ ; 40 à 80 ; moins de 15.)* Ce sont des valeurs **minimales à atteindre**, même si le livre les note $R_{\max}$.

{{fig:pc-isolation-niveaux}}

| Levier | Effet principal |
|---|---|
| Isolation des parois | réduire le flux à travers l'enveloppe |
| Inertie (masse) | retarder et amortir les variations |
| Protection solaire (pergola bioclimatique, brise-soleil) | limiter les apports solaires d'été |
| VMC double flux | renouveler l'air en récupérant la chaleur de l'air extrait |

Une **pergola bioclimatique** à lames orientables module l'ensoleillement de la terrasse et de la maison, et se referme en toiture étanche par temps de pluie : c'est une protection solaire **mobile**, pilotée par capteurs.
