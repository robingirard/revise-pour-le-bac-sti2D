# Pression et statique des fluides

*Prérequis : la compétence **Forces, poids et principe d'inertie**.*

## Force pressante et pression

Les actions mécaniques de contact exercées par un fluide (ou un solide) sur une surface sont modélisées par des **forces pressantes**. La **résultante $F$ des forces pressantes** est proportionnelle à la **pression $P$** du fluide et à la **surface $S$** sous pression :

$$F = P \times S \qquad\Longleftrightarrow\qquad P = \frac{F}{S}$$

| Grandeur | Signification | Unité |
|---|---|---|
| $F$ | résultante des forces pressantes | newton (N) |
| $P$ | pression exercée par le fluide | **pascal (Pa)** |
| $S$ | surface sous pression | mètre carré (m²) |

L'**unité officielle** est le **pascal** ; d'autres unités usuelles restent en vigueur (bar, cm de mercure, atmosphère). La pression se mesure avec un **baromètre dans l'air** et un **manomètre dans un liquide**.

Conversions à connaître : $1\ \mathrm{bar} = 10^5\ \mathrm{Pa} = 1\,000\ \mathrm{hPa} = 100\ \mathrm{kPa}$ et $1\ \mathrm{hPa} = 100\ \mathrm{Pa}$.
Piège classique : une surface donnée en cm² doit être convertie, $1\ \mathrm{cm^2} = 10^{-4}\ \mathrm{m^2}$.

## Pressions absolue et relative

- la référence de la **pression absolue** est le **vide**, de pression nulle ;
- la référence de la **pression relative** est **l'air au niveau de la mer à 15 °C, soit 1 013 hPa**.

$$P_{\text{relative}} = P_{\text{absolue}} - 1\,013 \qquad (\text{pressions en hPa})$$

*Exemple du manuel* : un manomètre de pneu indique **2,4 bars, soit 240 kPa** ; c'est une pression **relative**. La pression **absolue** vaut donc $2\,400 + 1\,013 = 3\,413\ \mathrm{hPa}$, soit environ **3 400 hPa**.

## Le principe fondamental de l'hydrostatique

L'**hydrostatique** concerne les **fluides au repos**. Dans un liquide au repos, la pression est **la même en tout point d'un même plan horizontal** et **augmente avec la profondeur** ; à la **surface libre**, elle est égale à la pression atmosphérique.

{{fig:pc-pression-profondeur}}

$$\Delta P = P_\mathrm{A} - P_\mathrm{B} = \rho_{\text{liquide}} \times g \times h$$

$\Delta P$ en **pascal (Pa)**, $\rho$ en $\mathrm{kg\cdot m^{-3}}$, $g = 9{,}81\ \mathrm{m\cdot s^{-2}}$, $h = z_\mathrm{B} - z_\mathrm{A}$ = dénivellation en **mètres** (A est le point le plus profond).

Mesures du manuel pour une **même dénivellation de 50 cm** :

| Liquide | Eau | Huile d'arachide | Éthanol |
|---|---|---|---|
| $\rho$ ($\mathrm{kg\cdot m^{-3}}$) | 1 000 | 920 | 789 |
| $\Delta P$ (kPa) | 4,9 | 4,5 | 3,9 |

Plus le liquide est **dense**, plus la différence de pression est grande pour la même dénivellation.

## Deux applications

**Le château d'eau.** Ce qui fixe la pression au robinet, c'est la **hauteur d'eau située au-dessus** de lui — d'où l'intérêt de percher le réservoir. Dans l'eau, $10\ \mathrm{m}$ de profondeur valent environ $1\ \mathrm{bar}$ de plus.

**La presse hydraulique.** Le liquide au repos transmet la même pression aux deux pistons ; comme $F = P \times S$, un **petit** effort sur le **petit** piston donne un **grand** effort sur le **grand** piston.

{{fig:pc-presse-hydraulique}}
