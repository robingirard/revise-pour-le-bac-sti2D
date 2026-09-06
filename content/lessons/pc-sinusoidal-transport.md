# Régime sinusoïdal, transport et protection

## Tension et intensité déphasées

En régime sinusoïdal, la tension et l'intensité aux bornes d'un dipôle sont le plus souvent **déphasées**
(décalées sur l'axe des temps) :

$u(t) = U\sqrt{2}\,\cos(\omega t)$ et $i(t) = I\sqrt{2}\,\cos(\omega t - \varphi)$

- $U$ : tension **efficace** (V) ; $I$ : intensité **efficace** (A) ;
- $\varphi$ : déphasage de $i(t)$ par rapport à $u(t)$ (° ou rad) ; $\omega$ : pulsation (rad/s).

Le dipôle est fléché en **convention récepteur**.

{{fig:pc-dephasage-u-i}}

## Puissances active et apparente

**Puissance active** (valeur moyenne de la puissance instantanée), en **watt (W)**, mesurée au **wattmètre**
(quatre bornes : deux pour la tension, deux pour l'intensité) :

$P = \langle p(t) \rangle = U \times I \times \cos\varphi$

**Puissance apparente**, en **volt-ampère (V·A)**, mesurée avec un **multimètre TRUE RMS** :

$S = U \times I$

| | dipôle purement résistif | dipôle purement capacitif | dipôle purement inductif |
|---|---|---|---|
| $\cos\varphi$ | 1 | 0 | 0 |
| $P$ (W) | $U \times I = R \times I^{2}$ | 0 | 0 |

*Remarque : on trouve parfois $\varphi = 90^{\circ}$ au dipôle capacitif et $\varphi = -90^{\circ}$ à l'inductif.
Avec la convention $i(t) = I\sqrt{2}\cos(\omega t - \varphi)$, les deux colonnes sont interverties
(le courant est en retard dans une bobine, en avance dans un condensateur). Cela ne change ni $\cos\varphi$,
nul dans les deux cas, ni $P = 0$ W.*

## Facteur de puissance

$k = \dfrac{P}{S} = \cos\varphi$ — **sans unité**, compris entre **0** (dipôle purement capacitif ou inductif,
aucune dissipation d'énergie) et **1** (dipôle purement résistif).

Un mauvais facteur de puissance fait circuler du courant dans la ligne sans produire de puissance active :
à $S$ fixée, l'intensité $I = S/U$ est la même, mais la puissance utile $P = S \times \cos\varphi$ est plus faible.

## Le réseau de transport et de distribution

{{fig:pc-reseau-transport}}

| Étape | Tension |
|---|---|
| poste de la centrale (production) | 20 kV |
| transport, lignes très haute tension | 400 kV |
| poste de transformation | 225 kV / 90 kV / 63 kV |
| poste source | 20 kV |
| distribution aux habitations | 400 V / 230 V |

Après la production, des transformateurs **élèvent** la tension ; avant la distribution, d'autres
l'**abaissent**. L'énergie électrique ne se stockant pas, elle doit être disponible à tout instant.

## Le transformateur

{{fig:pc-transformateur}}

Un transformateur diminue ou augmente une **tension alternative**. Il comporte un **noyau de fer doux** et
deux enroulements de spires jointives : les circuits **primaire** ($N_1$ spires) et **secondaire**
($N_2$ spires). Le **rapport de transformation** $m$, sans unité, vaut :

$m = \dfrac{N_2}{N_1} = \dfrac{U_2}{U_1} = \dfrac{I_1}{I_2}$

$m > 1$ : transformateur **élévateur** ; $m < 1$ : transformateur **abaisseur**. Attention à l'inversion pour
les intensités : abaisser la tension **élève** le courant au secondaire. Le transformateur assure en outre
une **isolation galvanique** (pas de chemin de courant entre les deux enroulements) et réduit le bruit de ligne.

## Protéger les personnes

{{fig:pc-securite-abaque}}

Les risques d'**électrisation**, voire d'**électrocution**, dépendent de l'**intensité** du courant et de la
**durée** de passage dans le corps.

| Intensité | Effet |
|---|---|
| 0,5 mA | seuil de perception, sensation très faible |
| 10 mA | seuil de non-lâcher, contraction musculaire |
| 30 mA | seuil de paralysie respiratoire au-delà de 500 ms |
| 50/75 mA | seuil de fibrillation cardiaque irréversible |
| 1 A | arrêt du cœur |

Deux dispositifs : la **prise de terre** (dévie le courant de fuite vers le sol) et le **disjoncteur
différentiel de 30 mA**, qui ouvre le circuit dès qu'une **fuite** dépasse 30 mA.

## Protéger le matériel

Contre les **courts-circuits** et les **surintensités** (multiprise surchargée) : **fusibles** et
**disjoncteurs magnéto-thermiques**, qui ouvrent le circuit défectueux.
Contre les **surtensions** : des **varistances branchées en dérivation** sur l'appareil à protéger.
