# Puissance et énergie en électricité

## Puissance électrique

En **régime continu** : $P = U \times I$

- $P$ : puissance, en watt (W) ; $U$ : tension, en volt (V) ; $I$ : intensité, en ampère (A).

En **régime variable**, on distingue :

| Puissance instantanée | Puissance moyenne |
|---|---|
| $p(t) = u(t) \times i(t)$ | $P = \langle p(t) \rangle = \langle u(t) \times i(t) \rangle$ |

Le symbole $\langle\ \rangle$ désigne la **valeur moyenne** sur une période.
Attention : en régime sinusoïdal, $\langle u \times i \rangle \neq \langle u \rangle \times \langle i \rangle$.

## Signe de la puissance et convention

{{fig:pc-convention-generateur-recepteur}}

| | $P > 0$ | $P < 0$ |
|---|---|---|
| **convention générateur** ($u$ et $i$ dans le même sens) | le dipôle **fournit** de l'énergie | le dipôle **reçoit** de l'énergie |
| **convention récepteur** ($u$ et $i$ en sens opposé) | le dipôle **reçoit** de l'énergie | le dipôle **fournit** de l'énergie |

## Énergie électrique

Pendant une durée $\Delta t$, un dipôle de puissance $P$ consomme ou produit :

$\Delta E = P \times \Delta t$

$\Delta E$ en joule (J) si $\Delta t$ est en seconde (s) ; en wattheure (Wh) si $\Delta t$ est en heure (h),
avec $1\ \text{Wh} = 3\,600\ \text{J}$.

## Effet Joule

Un dipôle ohmique de résistance $R$ échauffe : c'est l'**effet Joule**. En régime continu :

$P = U_R \times I_R = (R \times I_R) \times I_R = R \times I_R^{2}$
et $P = U_R \times I_R = U_R \times \dfrac{U_R}{R} = \dfrac{U_R^{2}}{R}$

Énergie dissipée pendant $\Delta t$ :
$\Delta E = R \times I_R^{2} \times \Delta t = \dfrac{U_R^{2}}{R} \times \Delta t$

En **régime variable**, on utilise les **valeurs efficaces** :
$\Delta E = R \times I_{\text{eff}}^{2} \times \Delta t = \dfrac{U_{\text{eff}}^{2}}{R} \times \Delta t$

{{fig:pc-pertes-ligne}}

Conséquence pratique : pour limiter les pertes par effet Joule lors du transport de l'électricité sur de
longues distances, on utilise des **lignes à haute tension**, dans lesquelles on **diminue l'intensité** du
courant. À puissance transportée fixée, diviser $I$ par 10 divise les pertes par **100**.

## Bilans de puissance et d'énergie

{{fig:pc-bilan-puissances}}

La puissance délivrée par un générateur se répartit sur tous les récepteurs qui lui sont reliés :

$p_G(t) = p_1(t) + p_2(t) + \dots + p_n(t)$ et $P_G = P_1 + P_2 + \dots + P_n$

$\Delta E_G = \Delta E_1 + \Delta E_2 + \dots + \Delta E_n$, **toutes les énergies étant exprimées dans la
même unité** (J, Wh ou kWh).

## Lire une facture

L'électricité est facturée au **kilowattheure** : coût = $\Delta E\ (\text{kWh}) \times$ prix du kWh.

Exemple : un radiateur de 2 000 W (soit 2,0 kW) fonctionnant 3,0 h consomme
$2{,}0 \times 3{,}0 = 6{,}0$ kWh ; à 0,25 € le kWh, cela coûte 1,50 €.

Pour réduire la consommation : **ne pas laisser les appareils en veille** et **les débrancher** quand ils ne
servent pas. Un **consomètre**, placé entre la prise et l'appareil, permet de mesurer sa puissance et son
énergie consommée.
