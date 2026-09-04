# Travail, puissance et énergie mécanique

*Prérequis : la compétence **Forces, poids et principe d'inertie**.*

## Le travail d'une force constante

Quand une force **travaille**, elle transfère de l'énergie au système et lui permet de se déplacer.

$$W_{\mathrm{A}\to\mathrm{B}}(\vec{F}) = F \times \mathrm{AB} \times \cos\alpha$$

| Grandeur | Signification | Unité |
|---|---|---|
| $W_{\mathrm{A}\to\mathrm{B}}(\vec{F})$ | travail de la force de A à B | joule (J) |
| $F$ | norme de la force | newton (N) |
| $\mathrm{AB}$ | distance parcourue de A à B | mètre (m) |
| $\alpha$ | angle entre $\vec{F}$ et $\overrightarrow{\mathrm{AB}}$ | degré (°) |

{{fig:pc-travail-force-angle}}

| Position de la force | Travail |
|---|---|
| perpendiculaire au déplacement, $\alpha = 90^\circ$ | $W = 0\ \mathrm{J}$ : **la force ne travaille pas** |
| $\alpha < 90^\circ$ | $W > 0$ : travail **moteur** |
| $\alpha > 90^\circ$ | $W < 0$ : travail **résistant** (cas d'un frottement, $\alpha = 180^\circ$) |

## La puissance moyenne

$$P_{\text{moy}} = \frac{W_{\mathrm{A}\to\mathrm{B}}(\vec{F})}{\Delta t}$$

$P_{\text{moy}}$ en **watt (W)**, $W$ en joule (J), $\Delta t$ en seconde (s).
*De deux forces exerçant le même travail, celle qui le fait en moins de temps est la plus puissante.*

Cas particulier utile : si la force est **constante et dans le sens du déplacement**, $W = F\,d$ avec $d = v\,\Delta t$, d'où

$$P = F \times v \qquad (F \text{ en N},\ v \text{ en } \mathrm{m\cdot s^{-1}},\ P \text{ en W})$$

## Énergie cinétique et énergie potentielle

$$E_c = \frac{1}{2} \times m \times v^2 \qquad\qquad E_{pp} = m \times g \times h$$

- $E_c$, $E_{pp}$ en **joule (J)**, $m$ en kg, $v$ en $\mathrm{m\cdot s^{-1}}$, $h$ en m ;
- l'énergie potentielle de pesanteur est **nulle au niveau du sol** ; elle ne dépend **que de la position**, pas de la vitesse ;
- attention : $v$ est **au carré** et il ne faut pas oublier le facteur $\tfrac12$ — une vitesse **doublée** multiplie $E_c$ par **4** ;
- une vitesse en km/h doit **toujours** être convertie : $1\ \mathrm{m\cdot s^{-1}} = 3{,}6\ \mathrm{km\cdot h^{-1}}$.

Pour un ressort de raideur $k$ (en $\mathrm{N\cdot m^{-1}}$) écarté de $x$ (en m) de sa position au repos : $E_{pe} = \tfrac12\,k\,x^2$.

## Le théorème de l'énergie cinétique

La variation de l'énergie cinétique entre A et B est égale à la **somme des travaux de toutes les forces extérieures** :

$$\Delta E_c = E_c(\mathrm{B}) - E_c(\mathrm{A}) = \sum W_{\mathrm{A}\to\mathrm{B}}(\vec{F})$$

Tous les termes sont en **joules**. À vitesse constante, $\Delta E_c = 0$ : la somme des travaux est nulle.

## L'énergie mécanique

$$E_m = E_c + E_p$$

{{fig:pc-energie-mecanique-chute}}

- **sans frottement**, $E_m$ **se conserve** : ce que $E_{pp}$ perd, $E_c$ le gagne ;
- dès qu'**une force exerce un travail résistant**, $E_m$ **ne peut que diminuer**.

## Méthode : résoudre avec le théorème de l'énergie cinétique

1. définir le système, le point de départ A et le point d'arrivée B ;
2. faire le **bilan des forces extérieures** ;
3. calculer le **travail de chaque force** entre A et B ;
4. écrire $\Delta E_c = \sum W$ ;
5. en déduire la grandeur cherchée (vitesse, distance, force de freinage…).
