# Parois, résistance thermique et coefficient $U$

*Le point de vue de l'ingénieur du bâtiment : on part du matériau, on arrive à la paroi.*

## La conductivité thermique $\lambda$ : une propriété du matériau

La conductivité thermique indique la quantité de chaleur qui traverse un matériau **d'un mètre d'épaisseur** pour un écart de **1 kelvin** entre ses deux faces. Symbole $\lambda$, unité **W/(m·K)**.

- $\lambda$ **faible** → matériau **isolant** ;
- $\lambda$ **élevée** → matériau **conducteur**.

| Matériau | Laine de verre | Nylon | Béton | Verre | Fer | Aluminium | Cuivre |
|---|---|---|---|---|---|---|---|
| $\lambda$ (W/(m·K)) | 0,04 | 0,25 | 1 | 1,2 | 80 | 237 | 390 |

*Attention* : on range parfois le béton et le verre du côté des « isolants », en n'opposant que deux familles extrêmes (non-métaux / métaux). Avec $\lambda = 1$ W/(m·K), le béton conduit **25 fois mieux** que la laine de verre : c'est un matériau **porteur**, jamais un isolant.

## La résistance thermique $R$ : une propriété de la couche

$$R = \frac{e}{\lambda}$$

$R$ en **m²·K/W**, $e$ l'épaisseur en **mètre**, $\lambda$ en W/(m·K). C'est la résistance d'**un mètre carré** de couche. Elle représente la capacité d'un matériau à s'opposer au flux de chaleur en prenant en compte son épaisseur.

Deux leviers pour l'augmenter : choisir un $\lambda$ plus faible, et/ou augmenter l'épaisseur $e$.

| Couche | Laine de verre 20 cm | Béton 20 cm | Verre 4 mm |
|---|---|---|---|
| $R$ (m²·K/W) | $0{,}20/0{,}04 = 5{,}0$ | $0{,}20/1 = 0{,}20$ | $0{,}004/1{,}2 = 3{,}3 \times 10^{-3}$ |

L'erreur qui coûte le plus cher : oublier de convertir les millimètres en mètres.

## Paroi multicouche : les résistances s'ajoutent

Les couches accolées sont traversées par le **même** flux : elles sont **en série**, comme des résistances électriques.

$$R^{\text{série}} = R^1 + R^2 + \cdots + R^n = \sum \frac{e}{\lambda}$$

{{fig:2i2d-paroi-multicouche}}

**Exemple** — mur de 0,20 m de béton doublé de 0,12 m de laine de verre :
$R = \dfrac{0{,}20}{1} + \dfrac{0{,}12}{0{,}04} = 0{,}20 + 3{,}00 = \mathbf{3{,}20}$ m²·K/W. L'isolant apporte à lui seul 94 % de la résistance.

{{fig:pc-resistances-serie}}

## Le coefficient $U$ : une propriété de la paroi

$$U = \frac{1}{R} \qquad \text{en W/(m²·K)}$$

$U$ est le nombre de watts qui traversent **un mètre carré** de paroi pour **un kelvin** d'écart. Une paroi performante a un **grand $R$** et un **petit $U$** : pour le mur ci-dessus, $U = 1/3{,}2 = 0{,}31$ W/(m²·K).

Les fabricants d'isolants annoncent un $R$, les fabricants de menuiseries et les réglementations un $U$ : les deux disent la même chose, à l'envers l'un de l'autre.

{{fig:2i2d-coefficient-u}}

## Du coefficient au flux

$$\varphi = \lambda \times \frac{\Delta T}{e} = \frac{\Delta T}{R} = U \times \Delta T \qquad \text{en W/m²}$$

$$\Phi = \varphi \times S = U \times S \times \Delta T \qquad \text{en W}$$

$\Delta T$ est un **écart** de température : il a la même valeur en °C et en K, aucune conversion n'est nécessaire. Le flux « va toujours du chaud vers le froid » — de l'intérieur vers l'extérieur en hiver, et dans l'autre sens lors d'une canicule.

{{fig:pc-mur-flux-thermique}}

**Exemple** — mur de $R = 3{,}2$ m²·K/W, intérieur 19 °C, extérieur −1 °C :
$\Delta T = 19 - (-1) = 20$ K, donc $\varphi = 20/3{,}2 = \mathbf{6{,}25}$ W/m².

## L'enchaînement à retenir

$$\lambda \ \xrightarrow{\ R = e/\lambda\ } \ R \ \xrightarrow{\ U = 1/R\ } \ U \ \xrightarrow{\ \varphi = U\Delta T\ } \ \varphi \ \xrightarrow{\ \Phi = \varphi S\ } \ \Phi$$

| Grandeur | $\lambda$ | $R$ | $U$ | $\varphi$ | $\Phi$ |
|---|---|---|---|---|---|
| Unité | W/(m·K) | m²·K/W | W/(m²·K) | W/m² | W |
| Décrit | le matériau | la couche | la paroi | 1 m² de paroi | la paroi entière |
