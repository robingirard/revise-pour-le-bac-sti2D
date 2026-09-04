# Figures à dessiner — unité « 2I2D Tle : bâtiment »

Dix figures TikZ nouvelles sont référencées par l'unité `2i2d-batiment`
(`content/units/120-2i2d-batiment.yaml` et `content/lessons/2i2d-batiment-*.md`). Tant qu'elles
n'existent pas dans `figures/tikz/`, `make content` échoue avec « figure inconnue » : ces dix
fichiers sont donc un **prérequis de build**.

## Figures existantes réutilisées (rien à dessiner)

| Id | Utilisation dans cette unité |
|---|---|
| `pc-resistances-serie` | paroi composite, association en série (compétence *parois*) |
| `pc-mur-flux-thermique` | flux à travers une paroi (leçon *parois*) |
| `pc-modes-transfert` | sens du flux, conduction/convection/rayonnement |
| `pc-echelle-temperature` | conversion °C / K (compétence *confort*) |
| `pc-isolation-niveaux` | exigences réglementaires $R$ minimales |
| `pc-echelle-decibels` | échelle des niveaux sonores et intensités |
| `pc-reflexion-transmission` | énergie incidente = réfléchie + absorbée + transmise |
| `pc-corps-chauffe` | spectre d'un filament, faible efficacité de l'incandescence |

## Conventions communes

- un fichier par figure : `figures/tikz/<ID>.tex`, `\documentclass[tikz,border=4pt]{standalone}` +
  `\usepackage{liaisons}` ;
- couleurs de la bibliothèque : `solideA` (rouge), `solideB` (bleu), `solideC` (rose),
  `solideD` (orange), `solideE` (vert), `solideF` (violet) ;
- **code couleur de l'unité** : chaud = `solideA`, froid = `solideB`, flux thermique = `solideD`,
  isolant = `solideE` ; pour l'éclairage, le faisceau lumineux est en `solideD!40` ;
- textes en `\small` / `\scriptsize`, en **français**, avec les notations de l'unité
  ($\lambda$, $R$, $U$, $\varphi$, $\Phi$, $\psi$, $\Delta T$, $L$, $T_R$, $E$, $I$) ;
- unités écrites exactement comme dans le contenu : W/(m·K), m²·K/W, W/(m²·K), W/m², W, dB, lm,
  lx, cd, lm/W ;
- largeur cible ≈ 8 cm (affichage mobile), hauteur ≤ 6 cm.

---

## 1. `2i2d-paroi-multicouche` — coupe d'un mur béton + laine de verre

*Utilisée par* : leçon `2i2d-batiment-parois` ; 3 exercices et l'exercice guidé
« Le local technique ».

Coupe **verticale** d'un mur vue de dessus, en bandes verticales accolées, de gauche
(**extérieur**) vers la droite (**intérieur**) :

| Bande | Largeur dessinée | Aspect | Étiquette sous la bande |
|---|---|---|---|
| Béton | 2,0 cm | gris moyen, semis de granulats | `Béton` · `e = 0,20 m` · `λ = 1 W/(m·K)` · `R = 0,20` |
| Laine de verre | 1,2 cm | `solideE!25`, hachures en zigzag serré (motif « isolation ») | `Laine de verre` · `e = 0,12 m` · `λ = 0,04 W/(m·K)` · `R = 3,00` |

Les épaisseurs dessinées sont **proportionnelles aux épaisseurs réelles** (0,20 et 0,12 m), pas
aux résistances : le message est justement que la couche la plus mince apporte 94 % de la
résistance.

- À gauche, zone `solideB!12` avec la mention **EXTÉRIEUR** et $-1\ ^\circ$C ; à droite, zone
  `solideA!12` avec **INTÉRIEUR** et $19\ ^\circ$C, chacune avec un petit thermomètre.
- Une **flèche `solideD` épaisse** traverse le mur **de la droite vers la gauche** (du chaud vers
  le froid), étiquetée $\varphi = 6{,}25$ W/m².
- Sous les deux bandes, une accolade horizontale portant l'encadré
  $R = 0{,}20 + 3{,}00 = \mathbf{3{,}20}$ m²·K/W.
- Au-dessus des bandes, un **profil de température** en trait fin `solideA` : segment descendant
  très peu dans le béton, puis chute brutale dans l'isolant (la pente est d'autant plus forte que
  la résistance de la couche est grande). Annoter cette courbe « profil de température ».
- Légende `\scriptsize` : « les résistances des couches accolées s'additionnent ».

## 2. `2i2d-coefficient-u` — de la résistance $R$ au coefficient $U$

*Utilisée par* : leçon `2i2d-batiment-parois` ; 1 exercice de la compétence *déperditions*.

Deux vignettes carrées côte à côte, même échelle, représentant chacune 1 m² de paroi vu de face,
avec sous chaque vignette un tableau de deux lignes.

| | Vignette gauche | Vignette droite |
|---|---|---|
| Titre | **Mur non isolé** (`solideA!20`) | **Mur isolé** (`solideE!20`) |
| Composition dessinée | bande de béton seule | béton + bande verte hachurée |
| Valeurs | $R = 0{,}20$ m²·K/W ; $U = 5{,}0$ W/(m²·K) | $R = 3{,}20$ m²·K/W ; $U = 0{,}31$ W/(m²·K) |
| Flèches de flux | **10 flèches** `solideD` serrées traversant la vignette | **1 flèche** `solideD` isolée |

Le nombre de flèches est le message visuel : à $\Delta T$ égal, le mur non isolé laisse passer
environ 16 fois plus de flux (100 W/m² contre 6,25 W/m² pour $\Delta T = 20$ K).

En dessous, deux relations encadrées sur une ligne :
$U = \dfrac{1}{R}$ (W/(m²·K)) et $\Phi = U \times S \times \Delta T$ (W).

Légende `\scriptsize` : « grand $R$, petit $U$ : les deux disent la même chose, à l'envers ».

## 3. `2i2d-deperditions-piece` — bilan des déperditions d'une pièce

*Utilisée par* : leçon `2i2d-batiment-deperditions` ; 3 exercices (calcul du mur, total, `order`
de classement).

**Partie haute** : coupe verticale schématique d'un bureau (rectangle de 4 cm × 2,5 cm, sol
hachuré en bas, toiture inclinée à faible pente en haut, une fenêtre sur la façade droite).
Cinq **flèches `solideD` sortantes**, dont la **largeur de trait est proportionnelle au flux**,
chacune étiquetée avec sa valeur :

| Flèche | Départ | Valeur affichée |
|---|---|---|
| Fenêtre | traverse la fenêtre, vers la droite | `Fenêtre — 224 W` |
| Renouvellement d'air | sort par une bouche en haut à gauche (dessiner une petite bouche de VMC) | `Air neuf — 204 W` |
| Murs | traverse la façade gauche | `Murs — 186 W` |
| Pont thermique | part de la **jonction plancher/façade** (point rouge `solideA`) | `Pont thermique — 108 W` |
| Toiture | traverse la toiture, vers le haut | `Toiture — 68 W` |

À l'intérieur, la mention $19\ ^\circ$C (`solideA`), à l'extérieur $-1\ ^\circ$C (`solideB`) et
$\Delta T = 20$ K.

**Partie basse** : une **barre horizontale empilée** de 7 cm de long représentant les 790 W,
segmentée dans le même ordre et avec les mêmes teintes que les flèches, chaque segment portant son
pourcentage : 28 % / 26 % / 24 % / 14 % / 9 %. À droite de la barre, l'encadré
**Total = 790 W**.

Légende `\scriptsize` : « fenêtre et air neuf pèsent plus de la moitié du bilan ».

## 4. `2i2d-pont-thermique` — liaison plancher/façade, ITI contre ITE

*Utilisée par* : leçon `2i2d-batiment-deperditions` ; 2 exercices.

Deux coupes verticales côte à côte, même géométrie : un mur vertical (bande grise, béton) et un
plancher horizontal (bande grise) qui vient buter contre lui en formant un T couché.

- **Vignette gauche, titre « Isolation par l'intérieur (ITI) »** : la bande verte `solideE!30` de
  l'isolant est posée **du côté intérieur** et se trouve **interrompue** par le plancher. À la
  jonction, dessiner un **faisceau de lignes de flux `solideD` resserrées** qui contourne
  l'isolant en passant par le plancher, plus une **pastille `solideA`** marquée « point froid ».
  Étiquette : `ψ = 0,60 W/(m·K)`.
- **Vignette droite, titre « Isolation par l'extérieur (ITE) »** : la bande verte est **continue**
  sur toute la façade, côté extérieur ; les lignes de flux `solideD` sont **parallèles et
  espacées**, sans resserrement à la jonction. Étiquette : `ψ fortement réduit`.

Dans les deux vignettes, mention **INT.** côté intérieur (`solideA!12`) et **EXT.** côté extérieur
(`solideB!12`).

Sous les deux vignettes, la relation encadrée $\Phi = \psi \times L \times \Delta T$ avec les
unités (W ; W/(m·K) ; m ; K).

## 5. `2i2d-inertie-thermique` — bâtiment léger et bâtiment lourd sur 24 h

*Utilisée par* : leçon `2i2d-batiment-confort` ; 2 exercices.

Graphique $\theta$ (°C) en ordonnée (graduations 20, 25, 30, 35), temps en abscisse (0 h à 24 h,
graduations toutes les 6 h), grille pointillée légère (style de `cinematique-chronogrammes.tex`).

Trois courbes :

| Courbe | Style | Allure |
|---|---|---|
| Température extérieure | `solideD`, trait pointillé | sinusoïde de 20 °C (6 h) à 35 °C (15 h) puis retour à 21 °C |
| Bâtiment **léger** (faible inertie) | `solideA`, trait plein | suit de près l'extérieur, maximum ≈ 32 °C vers 16 h |
| Bâtiment **lourd** (forte inertie) | `solideB`, trait plein épais | oscillation très amortie, maximum ≈ 26 °C vers 21 h |

Annoter par deux **double-flèches** :
- verticale entre les deux maxima : « amortissement » ;
- horizontale entre les abscisses des deux maxima : « déphasage (≈ 5 h) ».

Ajouter en `\scriptsize` sous le graphique : « allures qualitatives ; l'inertie ne supprime pas
l'énergie entrante, elle la retarde et l'amortit ».

À droite du graphique, une petite vignette : une dalle de béton en coupe avec
`4 × 5 × 0,20 m — 9 200 kg` et `+1 °C → 8,1 MJ (2,25 kWh)`.

## 6. `2i2d-confort-parois` — le confort dépend de l'air **et** des parois

*Utilisée par* : leçon `2i2d-batiment-confort` ; 2 exercices.

Diagramme à deux axes, gradués tous deux de 12 à 24 °C :
- **abscisse** : température des parois $T_{\text{parois}}$ (°C) ;
- **ordonnée** : température de l'air $T_{\text{air}}$ (°C).

Tracer la **droite de confort** $T_{\text{air}} + T_{\text{parois}} = 36$ (c'est-à-dire
$T_{\text{ressentie}} = 18\ ^\circ$C), en trait plein `solideE`, avec une **bande verte pâle** de
part et d'autre (largeur ±1 °C) étiquetée « zone de confort ressenti ≈ 18 °C ».

Deux points marqués et reliés par une flèche `solideD` :

| Point | Coordonnées | Étiquette |
|---|---|---|
| A | (15 ; 21) | `Avant isolation : parois 15 °C, air 21 °C` |
| B | (19 ; 17) | `Après isolation : parois 19 °C, air 17 °C` |

Les deux points sont **sur la même droite** : même sensation, mais 4 °C de consigne en moins.
Colorer légèrement le demi-plan situé sous la droite en `solideB!8` (« trop frais ») et celui
au-dessus en `solideA!8` (« trop chaud »).

Sous le diagramme, la relation encadrée
$T_{\text{ressentie}} \approx \dfrac{T_{\text{air}} + T_{\text{parois}}}{2}$ et la mention
`\scriptsize` « modèle simplifié ».

## 7. `2i2d-affaiblissement-paroi` — indice d'affaiblissement acoustique

*Utilisée par* : leçon `2i2d-batiment-acoustique` ; 2 exercices.

Deux locaux séparés par une paroi verticale épaisse (rectangle gris, motif de briques dessiné à la
main comme dans `pc-reflexion-transmission`, étiqueté `Paroi R = 42 dB`).

- **Local gauche** : une machine schématique (rectangle avec engrenage) et des arcs sonores
  `solideA` concentriques, nombreux et épais ; étiquette **$L_1 = 85$ dB**.
- **Local droit** : un poste de travail (table + écran) et des arcs sonores `solideB` peu nombreux
  et fins ; étiquette **$L_2 = 43$ dB**.
- Entre les deux, sur la paroi, l'encadré $L_2 = L_1 - R$ avec l'application numérique
  $85 - 42 = 43$ dB.

Sous la figure, un **encart d'avertissement** en `\scriptsize` :
« le $R$ acoustique s'exprime en **dB** et se **soustrait** ; il n'a rien à voir avec la résistance
thermique en m²·K/W ».

## 8. `2i2d-reverberation-salle` — trajets réfléchis et décroissance du niveau

*Utilisée par* : leçon `2i2d-batiment-acoustique` ; 2 exercices.

**Partie gauche** : coupe d'une salle (rectangle de 3,5 cm × 2,2 cm), une source (petit
haut-parleur) à gauche, un auditeur (silhouette simplifiée) à droite.
- un **trajet direct** en trait plein `solideA` de la source à l'auditeur ;
- **trois trajets réfléchis** en trait fin `solideB` rebondissant sur le plafond, le sol et le mur
  du fond, chacun avec une petite flèche.
- Étiquettes `V = 1 000 m³` et `A = 200 m²`.

**Partie droite** : petit graphique niveau sonore $L$ (dB) en fonction du temps (s).
- palier horizontal (source en marche), puis **arrêt de la source** marqué par un trait vertical
  pointillé étiqueté « arrêt » ;
- décroissance rectiligne `solideD` ; une double flèche verticale de **60 dB** et une double flèche
  horizontale de $T_R = 0{,}80$ s délimitant la même portion de courbe.

Sous l'ensemble, la relation encadrée $T_R = 0{,}16 \times \dfrac{V}{A}$ avec les unités (s ; m³ ;
m²) et la mention `\scriptsize` « formule de Sabine ».

## 9. `2i2d-grandeurs-photometriques` — flux, intensité, éclairement

*Utilisée par* : leçon `2i2d-batiment-eclairage` ; 2 exercices.

Trois vignettes encadrées de même taille, côte à côte, chacune avec une ampoule identique dessinée
au trait (bulbe clair, filament, culot gris) :

| Vignette | Dessin | Titre et unité |
|---|---|---|
| 1 | **huit flèches** `solideD` rayonnant dans toutes les directions autour de l'ampoule | **Flux lumineux $\varphi$** — lumen (lm) |
| 2 | **une seule** grosse flèche `solideD` dirigée vers le bas, les autres directions en gris très pâle | **Intensité lumineuse $I$** — candela (cd) |
| 3 | l'ampoule au-dessus d'un **cône de lumière** `solideD!25` évasé, tombant sur un rectangle horizontal (le plan de travail) coté $S$ | **Éclairement $E$** — lux (lx) |

Sous la troisième vignette, l'égalité encadrée **1 lx = 1 lm/m²**.

Bandeau `\scriptsize` sous les trois vignettes : « $\varphi$ et $I$ décrivent la **source**, $E$
décrit la **surface éclairée** ».

## 10. `2i2d-eclairement-surface` — de la puissance électrique aux lux

*Utilisée par* : leçon `2i2d-batiment-eclairage` ; 3 exercices et l'exercice guidé
« L'éclairage de l'atelier ».

**Partie haute — chaîne de conversion** : trois blocs rectangulaires reliés par des flèches
`solideD` :

`P = 20 W (puissance électrique)` → **[ Luminaire LED — $\eta$ = 100 lm/W ]** →
`φ = 2 000 lm (flux lumineux)` → **[ Local — S = 200 m² ]** → `E = 120 lx (éclairement)`

Sous les deux blocs, les relations $\varphi = \eta \times P$ et $E = \dfrac{\varphi}{S}$.

**Partie basse — vue en coupe du local** : un plafond horizontal portant **quatre luminaires**
schématiques, chacun émettant un **cône `solideD!25`** vers le bas ; les cônes se recouvrent
partiellement sur un **plan de travail** horizontal coté $S$. Sur le plan de travail, l'étiquette
`E = φ_total / S`.

À droite du plan de travail, une petite **échelle verticale des éclairements** graduée avec les
deux valeurs de l'exercice guidé : `120 lx (installation actuelle)` en `solideA` et
`300 lx (cahier des charges)` en `solideE`, la seconde nettement au-dessus de la première.
