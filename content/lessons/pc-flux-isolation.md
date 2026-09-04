# Flux thermique, résistance thermique et isolation

## Le flux thermique

Le **flux thermique** $\Phi$ à travers une paroi est un **débit d'énergie** : c'est donc une **puissance**, exprimée en **watt (W)**.

$$\Phi = \frac{E}{\Delta t}$$

avec $E$ en joule (J) et $\Delta t$ en seconde (s). L'énergie traverse toujours la paroi **du côté le plus chaud vers le plus froid**. Le flux **augmente** avec la surface $S$ (en m²) et avec l'écart de température entre les deux faces ; il **diminue** quand la **résistance thermique** $R_{\text{th}}$ de la paroi augmente.

$$\Phi = \frac{S \times (T_{\text{chaud}} - T_{\text{froid}})}{R_{\text{th}}}$$

$\Phi$ en W, $S$ en m², les températures en K **ou** en °C, $R_{\text{th}}$ en **m²·K·W⁻¹**. *Inutile de convertir en kelvin* : la **différence** est la même dans les deux échelles, pourvu qu'on emploie la même unité pour les deux températures.

{{fig:pc-mur-flux-thermique}}

*Analogie électrique* : $\Phi$ joue le rôle de l'intensité, l'écart de température celui de la tension, $R_{\text{th}}$ celui de la résistance — d'où l'écriture $\Phi = \Delta T / R$ lorsque $R = \dfrac{e}{\lambda\,S}$ est la résistance de la paroi **entière** (en K·W⁻¹). Dans ce chapitre, on suit la convention du livre : $R_{\text{th}}$ est la résistance de **1 m²** de paroi, et la surface apparaît au numérateur.

## Résistance thermique d'une paroi homogène

$$R_{\text{th}} = \frac{e}{\lambda}$$

avec $R_{\text{th}}$ en m²·K·W⁻¹ (résistance de 1 m² de paroi), $e$ l'épaisseur en **mètre (m)** — l'erreur classique est de laisser des millimètres — et $\lambda$ la **conductivité thermique** du matériau, en W·m⁻¹·K⁻¹. Plus $\lambda$ est **petit**, plus le matériau est **isolant** ; plus $R_{\text{th}}$ est **grand**, plus la paroi s'oppose au passage du flux.

| Matériau | Placoplâtre | Carrelage grès | Moquette | Parquet stratifié | Parpaing | Verre |
|---|---|---|---|---|---|---|
| $\lambda$ (W·m⁻¹·K⁻¹) | 0,25 | 1,3 | 0,09 | 0,16 | 0,95 | 1,1 |
| Épaisseur usuelle (mm) | 13 | 10 | 4,0 | 12 | 200 | 5,0 |
| $R_{\text{th}}$ (m²·K·W⁻¹) | $5{,}2 \times 10^{-2}$ | $7{,}7 \times 10^{-3}$ | $4{,}4 \times 10^{-2}$ | $7{,}5 \times 10^{-2}$ | 0,21 | $4{,}5 \times 10^{-3}$ |

Pour un sol, aux épaisseurs usuelles, un parquet stratifié limite donc mieux les transferts par conduction qu'une moquette, et bien mieux qu'un carrelage en grès.

## Paroi composite : les résistances s'ajoutent

Les couches accolées sont traversées par le **même** flux : leurs résistances thermiques **s'additionnent**, comme des résistances électriques en série.

$$R_{\text{th, paroi}} = \sum_{\text{matériaux}} \frac{e_{\text{matériau}}}{\lambda_{\text{matériau}}}$$

**Exemple — toit de combles aménagés** (par m², de l'extérieur vers l'intérieur) : ardoise 0,003 + bois de charpente 0,333 + air peu ventilé 0,130 + laine de verre 5,400 + plaque de plâtre 0,040 = **5,906 m²·K·W⁻¹**. La laine de verre apporte à elle seule plus de 91 % du total.

{{fig:pc-resistances-serie}}

## Réglementation

| Résistance thermique exigée (m²·K·W⁻¹) | RT 2005 | « Basse énergie » | « Très basse énergie » |
|---|---|---|---|
| Toit | 5,0 | 6,7 | 10 |
| Plancher | 2,0 | 3,3 | 6,7 |
| Façade | 2,2 | 3,3 | 6,7 |

*(RT 2005 : 130 kWh·m⁻²·an⁻¹ ; « basse énergie » : 40 à 80 kWh·m⁻²·an⁻¹ ; « très basse énergie » : moins de 15 kWh·m⁻²·an⁻¹.)*

Le toit précédent (5,906 m²·K·W⁻¹) respecte la **RT 2005** mais **pas** les deux autres niveaux. *Attention* : le livre note ces exigences $R_{\max}$ alors qu'il s'agit de valeurs **minimales** à atteindre ; il faut lire $R_{\min}$.

{{fig:pc-isolation-niveaux}}
