# Ondes sonores et ultrasonores

*Prérequis : la compétence **Notion d'onde**.*

## Célérité du son et milieu de propagation

**À retenir** : l'énergie d'une onde sonore ou ultrasonore se propage **uniquement dans la matière**, sans déplacement de celle-ci, à une célérité qui dépend des propriétés du milieu :

- l'**état physique** : le son se propage de plus en plus vite dans un **gaz**, puis un **liquide**, puis un **solide** ;
- la **température** : plus elle est élevée, plus l'agitation moléculaire est grande et plus le son est rapide ;
- la **pression** : plus elle est élevée, plus les molécules sont rapprochées et plus le son est rapide.

| Milieu | Air (0 °C) | Air (20 °C) | Eau (20 °C) | Glace (0 °C) | Acier (20 °C) |
|---|---|---|---|---|---|
| $v_{\text{son}}$ (m·s⁻¹) | 330 | 340 | 1 500 | 3 200 | 6 000 |

$$v_{\text{son}} = \frac{\lambda}{T} = \lambda \times f$$

## Hauteur et fréquence

La **hauteur** d'un son distingue les sons **graves**, **médiums** et **aigus** : elle est liée à la **fréquence**. Plus $f$ est élevée, plus le son est **aigu** ; plus $f$ est basse, plus il est **grave**.

**À retenir** : les fréquences des sons **audibles** sont comprises **entre 20 Hz et 20 kHz**. En dessous : **infrasons**. Au-dessus : **ultrasons**, inaudibles.

## Mesurer une distance avec des ultrasons

{{fig:pc-telemetre-ultrasons}}

La mesure de la durée $\Delta t$ entre l'**émission** d'une salve et la **réception de l'écho** permet de calculer la distance entre l'émetteur et l'obstacle :

$$d = \frac{v_{\text{US}} \times \Delta t}{2}$$

| Grandeur | Signification | Unité |
|---|---|---|
| $d$ | distance émetteur-obstacle | mètre (m) |
| $v_{\text{US}}$ | célérité des ultrasons dans le milieu | m·s⁻¹ |
| $\Delta t$ | durée d'un **aller-retour** | seconde (s) |

Le facteur 2 vient de l'**aller-retour** : pendant $\Delta t$, l'onde parcourt $2d$. L'oublier double le résultat. Cette technique est celle des **télémètres** (aide au stationnement, à 40 kHz) et de l'**échographie** (dans les tissus, $v \approx 1\,500$ m·s⁻¹).

## Intensité acoustique et niveau sonore

L'**amplitude** d'un son est liée à son **intensité acoustique** $I$, exprimée en **watt par mètre carré (W·m⁻²)**, qui **diminue quand la distance source-récepteur augmente**.

{{fig:pc-intensite-distance}}

Pour une source qui émet **dans toutes les directions**, la puissance acoustique se répartit sur une **sphère** :

$$S = 4\pi r^2$$

Doubler la distance multiplie la surface par $2^2 = 4$ : l'intensité acoustique est **divisée par 4**.

Comme $I$ s'étale de $10^{-12}$ à $10^{5}$ W·m⁻², on utilise une **échelle logarithmique**, le **niveau sonore** $L$ en **décibels (dB)** :

$$L = 10 \log\!\left(\frac{I}{I_0}\right) \qquad\text{avec}\qquad I_0 = 1{,}0 \times 10^{-12}\ \mathrm{W\cdot m^{-2}}$$

{{fig:pc-echelle-decibels}}

| Situation | $I$ (W·m⁻²) | $L$ (dB) |
|---|---|---|
| Seuil d'audibilité (référence $I_0$) | $10^{-12}$ | 0 |
| Chuchotement | $10^{-8}$ | 40 |
| Conversation normale | $10^{-6}$ | 60 |
| Conversation à haute voix | $10^{-4}$ | 80 |
| Lecteur MP3 | $10^{-2}$ | 100 |
| Discothèque, concert | $10^{-1}$ | 110 |
| Réacteur d'avion (seuil de la douleur) | $10^{1}$ | 130 |

Le décibel n'est **pas linéaire** : deux sources identiques **n'additionnent pas leurs décibels**, mais leurs **intensités acoustiques**.

- $I$ multipliée par 2 → $L$ augmente de $10\log 2 \approx 3$ dB ;
- $I$ multipliée par 10 → $L$ augmente de 10 dB ;
- $I$ multipliée par 100 → $L$ augmente de 20 dB.

## Méthode : d'un niveau sonore à une intensité, et retour

1. de $I$ vers $L$ : calculer le rapport $I/I_0$, prendre son logarithme décimal, multiplier par 10 ;
2. de $L$ vers $I$ : $I = I_0 \times 10^{L/10}$ ;
3. pour additionner deux sources : **additionner les intensités** $I$ (en W·m⁻²), puis seulement ensuite repasser en décibels.
