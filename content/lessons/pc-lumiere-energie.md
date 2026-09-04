# Énergie transportée par la lumière

*Prérequis : la compétence **Ondes électromagnétiques**.*

## Le photon

**À retenir** : dans le **modèle corpusculaire**, la lumière est un **flux de photons**, particules de **masse nulle** se déplaçant à la **célérité de la lumière**.

$$E = h \times \nu = \frac{h \times c}{\lambda}$$

| Grandeur | Signification | Unité |
|---|---|---|
| $E$ | énergie du photon | joule (J) |
| $h$ | constante de Planck, $h = 6{,}63 \times 10^{-34}$ | J·s |
| $\nu$ (ou $f$) | fréquence associée au photon | hertz (Hz) |
| $\lambda$ | longueur d'onde | mètre (m) |
| $c$ | célérité de la lumière, $c = 3{,}00 \times 10^{8}$ | m·s⁻¹ |

Les énergies mises en jeu étant très faibles, on utilise souvent l'**électronvolt** : $1{,}0\ \mathrm{eV} = 1{,}6 \times 10^{-19}\ \mathrm{J}$.

{{fig:pc-photon-panneau}}

- **émission** d'un photon : l'électron **perd** l'énergie correspondante et passe à un **niveau inférieur** — applications : **lasers**, **diodes électroluminescentes** ;
- **absorption** d'un photon : l'électron **absorbe** son énergie et passe à un **niveau supérieur** — applications : **photorésistances**, **photodiodes**, **cellules photovoltaïques**.

## Le panneau photovoltaïque

La puissance lumineuse reçue est proportionnelle à l'**irradiance** $P_{\text{surf}}$ (puissance surfacique du rayonnement), mesurée au **solarimètre** (ou pyranomètre), en **W·m⁻²** :

$$P_{\text{lumineuse}} = P_{\text{surf}} \times S$$

Le panneau fournit un courant **continu** d'intensité $I$ sous une tension **continue** $U$ :

$$P_{\text{élec}} = U \times I$$

Sur la **caractéristique courant-tension** du panneau se lisent l'intensité de **court-circuit** $I_{cc}$ (qui dépend de l'éclairement), la **tension à vide** $U_{co}$, et le **point de puissance maximale** de coordonnées $U_{ppm}$ et $I_{ppm}$, tel que $P_{\max} = U_{ppm} \times I_{ppm}$.

$$r = \frac{P_{\max}}{P_{\text{surf}} \times S}$$

| Grandeur | Signification | Unité |
|---|---|---|
| $r$ | rendement maximal | **sans unité** (souvent en %) |
| $P_{\max}$ | puissance électrique maximale | watt (W) |
| $P_{\text{surf}}$ | irradiance | W·m⁻² |
| $S$ | surface du panneau | m² |

Le rendement est **toujours inférieur à 100 %** : chaîne énergétique **énergie rayonnante → cellule photovoltaïque → énergie électrique (utile)**, avec une **énergie perdue** d'origine thermique et rayonnante. Le point de fonctionnement **réel** se lit à l'**intersection** de la caractéristique du panneau et de celle du récepteur branché.

## Les lasers

LASER : *light amplification by stimulated emission of radiation*. Le faisceau est :

- **quasi monochromatique** (une longueur d'onde $\lambda$ précise) ;
- **très peu divergent**, donc **directif** : son diamètre augmente très peu avec la distance ;
- **concentrant une grande quantité d'énergie** sur une **très faible surface**, donc potentiellement **très dangereux** — d'où le **pictogramme de sécurité** obligatoire sur tout laser.

| Type de laser | Relation | Unités |
|---|---|---|
| **continu** (longueur d'onde constante) | $P = P_{\text{surf}} \times S$ | $P$ en W, $P_{\text{surf}}$ en W·m⁻², $S$ (section du faisceau) en m² |
| **impulsionnel** (impulsions brèves) | $E = P_{\text{crête}} \times \tau$ | $E$ en J, $P_{\text{crête}}$ en W, $\tau$ en s |

## Méthode : calculer le rendement d'un panneau

1. relever l'**irradiance** $P_{\text{surf}}$ (en W·m⁻²) et la **surface** $S$ (en m²) ;
2. calculer la puissance lumineuse **reçue** : $P_{\text{surf}} \times S$, en watts ;
3. relever $U_{ppm}$ et $I_{ppm}$ sur la caractéristique ;
4. calculer $P_{\max} = U_{ppm} \times I_{ppm}$, en watts ;
5. calculer $r = P_{\max} / (P_{\text{surf}} \times S)$, puis l'exprimer en pourcentage ;
6. **vérifier** que $r < 1$ : sinon, la surface a été oubliée quelque part.
