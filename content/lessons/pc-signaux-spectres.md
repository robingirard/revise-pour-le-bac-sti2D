# Signaux périodiques, spectres, sons et transmission

## Signal périodique, fondamental et harmoniques

Un signal est **périodique** si un **motif élémentaire** se répète. La **période** $T$ est la **plus petite**
durée au bout de laquelle le signal se reproduit identique à lui-même (en s) ; la fréquence du **fondamental**
vaut $f_1 = \dfrac{1}{T}$, en **hertz (Hz)**.

**Décomposition de Fourier** : tout signal périodique de période $T$ est la somme d'une **composante continue**
et de sinusoïdes de fréquences **multiples** de $f_1$ :

$s(t) = A_0 + A_1 \sin(2\pi f_1 t + \phi_1) + A_2 \sin(2\pi f_2 t + \phi_2) + \dots + A_n \sin(2\pi f_n t + \phi_n)$

| Grandeur | Signification | Unité |
|---|---|---|
| $A_0$ | amplitude de la composante continue (raie à 0 Hz) | V |
| $A_n$ | amplitude de l'harmonique de rang $n$ | V |
| $\phi_n$ | phase à $t = 0$, entre $-\pi$ et $\pi$ | rad |
| $f_n = n \times f_1$ | fréquence de l'harmonique de rang $n$ | Hz |

**Rang d'un harmonique** : $n = \dfrac{f_n}{f_1}$, entier naturel non nul. Le rang est un **nombre**, pas une
fréquence : l'harmonique de rang 3 d'un fondamental à 250 Hz est à $3 \times 250 = 750$ Hz.

## Spectre d'amplitude

{{fig:pc-spectre-signal}}

Le **spectre d'amplitude** porte l'amplitude (V) en fonction de la fréquence (Hz) : une **raie** par
composante. Il donne la composante continue (à 0 Hz), le **fondamental** ($f_1$, fréquence non nulle la plus
faible) et les harmoniques. Exemple du cours : pour
$s(t) = 2 + 1 \sin(2\pi f_1 t) + 0{,}5 \sin\!\left(2\pi (2f_1) t + \tfrac{\pi}{2}\right)$, on lit une raie de
hauteur 1 à $f_1$ et une raie de hauteur 0,5 à $f_2 = 2 f_1$, la composante continue valant 2 V.

## Sons purs et sons complexes

Un son est **pur** si son signal est **sinusoïdal** : une seule raie sur son spectre. Sinon il est
**complexe** : plusieurs raies, aux fréquences $f_n = n \times f_1$. La **hauteur** (aigu ou grave) est donnée
par la fréquence $f_1$ du fondamental ; le **timbre** (ce qui distingue deux instruments jouant la même note)
dépend du **nombre d'harmoniques et de leurs amplitudes**.

## Niveau sonore et oreille humaine

Les **intensités acoustiques** $I$ (en W·m⁻²) s'additionnent, mais pas la sensation auditive. D'où le
**niveau sonore** :

$L = 10 \log\!\left(\dfrac{I}{I_0}\right)$ et réciproquement $I = I_0 \times 10^{L/10}$

$L$ en **décibel (dB)**, $I$ et $I_0$ en **W·m⁻²**, avec $I_0 = 10^{-12}$ W·m⁻² (seuil d'audibilité à
1 000 Hz). Conséquences : $I$ **× 10** → $L$ **+ 10 dB** ; $I$ **× 2** → $L$ **+ 3 dB**. Repères : 20 dB
(désert), 60 dB (conversation), 80 dB (restaurant scolaire), 85 dB (risque), 90 dB (danger), 100 dB (marteau
piqueur), 120 dB (F1), 140 dB (Ariane au décollage).

Champ auditif : **20 Hz à 20 000 Hz** ; en dessous, **infrasons** ; au-dessus, **ultrasons**. Les seuils
d'audibilité et de douleur **dépendent de la fréquence** : graves et aigus extrêmes sont mal perçus.
L'**indice d'affaiblissement acoustique** $R_w$, en **dB**, mesure l'aptitude d'un matériau à atténuer la
transmission du bruit : avec $R_w = 30$ dB, un bruit de 85 dB devient environ $85 - 30 = 55$ dB — les
décibels se **soustraient**, ils ne se divisent pas.

## Transmettre : filtrage, modulation, télécommunications

{{fig:pc-modulation}}

On **filtre** les harmoniques d'amplitude très faible (pour limiter la largeur de la bande émise), puis on
**module** une **porteuse**, onde électromagnétique de **haute fréquence**. Cette **transposition de
fréquence** translate le spectre autour de la porteuse **sans perte d'information**. Trois modulations :
d'**amplitude** (AM), de **fréquence** (FM), de **phase**. En AM, une porteuse $F$ modulée par deux
harmoniques $f_A$ et $f_B$ donne **cinq** raies : $F$, $F \pm f_A$, $F \pm f_B$. Pour transmettre plusieurs
informations à la fois, on utilise plusieurs canaux : **multiplexage fréquentiel**.

{{fig:pc-spectre-radiofrequence}}

Une onde électromagnétique se propage dans le vide ou l'air à $c = 3{,}00 \times 10^{8}$ m·s⁻¹ et
$\lambda = \dfrac{c}{f}$ ($\lambda$ en m, $f$ en Hz).

| Bande | Fréquence | Longueur d'onde | Usages |
|---|---|---|---|
| EHF | 300 GHz → 30 GHz | 1 mm → 1 cm | radar automatique |
| SHF | 30 GHz → 3 GHz | 1 cm → 10 cm | satellite |
| UHF | 3 GHz → 300 MHz | 10 cm → 1 m | téléphone mobile, DECT, four micro-ondes |
| VHF | 300 MHz → 30 MHz | 1 m → 10 m | télévision numérique terrestre |
| HF | 30 MHz → 3 MHz | 10 m → 100 m | |
| MF | 3 MHz → 300 kHz | 100 m → 1 km | radio AM, FM |
| LF | 300 kHz → 30 kHz | 1 km → 10 km | |

Pour une réception optimale, la **taille de l'antenne** doit être **du même ordre de grandeur que $\lambda$**.
La **fibre optique** transmet des **impulsions lumineuses** avec un débit très supérieur aux autres supports
filaires : la lumière est piégée dans le **cœur** (entouré d'une **gaine optique** et d'une enveloppe
protectrice) par **réflexion totale**.
