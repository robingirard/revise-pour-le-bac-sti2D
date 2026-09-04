# Figures à dessiner — unité « Physique : énergie thermique »

Huit figures TikZ sont référencées par l'unité `pc-thermique`
(`content/units/50-pc-thermique.yaml` et `content/lessons/pc-*.md`). Tant qu'elles n'existent pas
dans `figures/tikz/`, `make content` échoue avec « figure inconnue » : ces huit fichiers sont donc
un **prérequis de build**.

## Conventions communes

- un fichier par figure : `figures/tikz/<ID>.tex`, `\documentclass[tikz,border=4pt]{standalone}` +
  `\usepackage{liaisons}` (comme `figures/tikz/cinematique-chronogrammes.tex`) ;
- couleurs de la bibliothèque : `solideA` (rouge), `solideB` (bleu), `solideC` (rose),
  `solideD` (orange), `solideE` (vert), `solideF` (violet) ;
- **code couleur de l'unité** : chaud = `solideA`, froid = `solideB`, flux thermique = `solideD`,
  isolant = `solideE` ;
- textes en `\small` / `\scriptsize`, en **français**, avec les notations du livre
  ($\theta$, $T$, $Q$, $Q_p$, $c$, $L$, $\Phi$, $R_{\text{th}}$, $\lambda$, $e$, $S$) ;
- largeur cible ≈ 8 cm (affichage mobile), hauteur ≤ 6 cm ;
- pas de texte en anglais (le livre écrit « RADIATION » sur son schéma : écrire
  **« RAYONNEMENT »**).

---

## 1. `pc-etats-matiere` — les six changements d'état

*Utilisée par* : leçons `pc-temperature-chaleur` et `pc-changements-etat` ; 4 exercices de
`pc-changements-etat`.

Trois boîtes arrondies aux sommets d'un **triangle pointe en haut** :

- **Gaz** en haut ; **Solide** en bas à gauche ; **Liquide** en bas à droite.

Sur chaque côté, **deux flèches parallèles de sens opposés** (décalées avec
`transform canvas={xshift=...}`), avec le nom écrit le long de la flèche :

| Côté | Flèche `solideA` (rouge, apport d'énergie) | Flèche `solideB` (bleu, cession d'énergie) |
|---|---|---|
| gauche : Solide ↔ Gaz | montante, **Sublimation** | descendante, **Condensation** |
| droit : Gaz ↔ Liquide | montante (Liquide → Gaz), **Vaporisation** | descendante, **Condensation (liquéfaction)** |
| bas : Solide ↔ Liquide | vers la droite (sous le côté), **Fusion** | vers la gauche (au-dessus), **Solidification** |

Trois **bulles circulaires** reliées par un trait fin à chaque état, montrant l'échelle
microscopique : solide = ~20 petits disques **rangés en réseau régulier** ; liquide = ~8 disques
**jointifs mais désordonnés** ; gaz = 3 disques **très espacés**.

Sous le triangle, une mention en `\scriptsize` : « flèches rouges : le corps **reçoit** de l'énergie
($Q_p > 0$) — flèches bleues : il en **cède** ($Q_p < 0$) ».

## 2. `pc-agitation-thermique` — température et agitation microscopique

*Utilisée par* : leçon `pc-temperature-chaleur` ; 1 exercice (niveau 1).

Deux vignettes côte à côte, même cadre carré, séparées par une flèche `solideD` horizontale portant
la mention « on chauffe ».

- Vignette de gauche, titre **« Corps froid »** (en `solideB`) : une douzaine de disques bleus
  disposés régulièrement, chacun portant une **flèche d'agitation courte** (≈ 2 mm) orientée au
  hasard. Sous la vignette : `θ faible`.
- Vignette de droite, titre **« Corps chaud »** (en `solideA`) : les **mêmes** disques, aux mêmes
  positions, portant des **flèches d'agitation longues** (≈ 5 mm) et des petits traits de vibration.
  Sous la vignette : `θ élevée`.

Message à faire passer : ni le nombre, ni la masse des constituants ne changent — **seule
l'agitation** change. Le mentionner en légende `\scriptsize`.

## 3. `pc-echelle-temperature` — échelles Celsius et kelvin

*Utilisée par* : leçon `pc-temperature-chaleur` ; 1 exercice de conversion.

Un **thermomètre vertical** (rectangle arrondi étroit, ampoule ronde en bas) avec **deux graduations
en vis-à-vis** : °C à gauche, K à droite, parfaitement alignées.

Repères à tracer (trait plein + valeur des deux côtés) :

| °C | K | Étiquette à droite |
|---|---|---|
| −273,15 | 0 | zéro absolu (inaccessible) |
| −39 | 234,15 | fusion du mercure |
| 0 | 273,15 | fusion de l'eau |
| 25 | 298,15 | température ambiante |
| 100 | 373,15 | ébullition de l'eau |

Échelle **linéaire** de −273,15 °C à 100 °C (les repères ne sont donc pas régulièrement espacés).
Remplissage du tube en dégradé `solideB` → `solideA` du bas vers le haut.

En dessous, la relation encadrée : $T\,(\text{K}) = \theta\,(^\circ\text{C}) + 273{,}15$, et une
**double flèche verticale** entre 0 °C et 100 °C annotée « Δθ = 100 °C = 100 K » pour illustrer que
l'**écart** est identique dans les deux échelles.

## 4. `pc-modes-transfert` — conduction, convection, rayonnement

*Utilisée par* : leçon `pc-temperature-chaleur` ; 3 exercices + le `grid` des modes de transfert.

Schéma de principe (dessin au trait, pas une photo) :

- au centre-bas, un **feu** (deux bûches croisées + flammes `solideD`/`solideA`) ;
- au-dessus, une **casserole** vue en coupe (paroi grise, manche horizontal partant à droite),
  contenant de l'eau (bleu clair) ;
- **CONDUCTION** : étiquette à droite, flèche pointant le **manche** ; petites flèches courtes en
  chaîne le long de la paroi et du manche (l'énergie chemine de proche en proche) ;
- **CONVECTION** : étiquette en haut à gauche, flèche pointant l'**intérieur du liquide** ; dessiner
  **deux boucles fermées** (rouge en montée au centre, bleue en descente sur les bords) ;
- **RAYONNEMENT** : étiquette en bas à gauche ; **lignes ondulées** `solideA`/`solideD` partant des
  flammes dans toutes les directions (gauche, droite, haut), certaines s'échappant hors du cadre
  pour montrer qu'aucun support matériel n'est nécessaire.

Sous le schéma, trois pastilles rappelant en `\scriptsize` : « milieu matériel, sans déplacement de
matière » / « déplacement de matière (gaz ou liquide) » / « ondes électromagnétiques, sans milieu ».

## 5. `pc-courbe-chauffage-eau` — courbe de chauffage d'un corps pur

*Utilisée par* : leçon `pc-changements-etat` ; 4 exercices (palier, `order`, `grid`, bilan complet).

Graphique $\theta$ (°C) en ordonnée, $t$ (s) en abscisse, grille pointillée légère
(style de `cinematique-chronogrammes.tex`).

Valeurs à respecter (cas de l'eau, 1,0 kg, chauffage à puissance constante — les longueurs des
portions sont donc **proportionnelles aux énergies** du bilan p. 27) :

| Portion | Énergie (kJ) | Longueur relative en abscisse |
|---|---|---|
| ❶ solide, −20 → 0 °C | 42 | 1,4 % |
| ❷ palier de fusion, 0 °C | 334 | 10,8 % |
| ❸ liquide, 0 → 100 °C | 420 | 13,6 % |
| ❹ palier d'ébullition, 100 °C | 2 260 | 73,0 % |
| ❺ vapeur, 100 → 120 °C | 40 | 1,3 % |

Courbe `solideB` continue, épaisse, en cinq portions ; graduations d'ordonnée −20, 0, 100, 120 avec
traits pointillés horizontaux ; annotations **« Fusion »** et **« Ébullition »** au-dessus des deux
paliers ; cinq pastilles rondes rouges numérotées ❶…❺ au milieu de chaque portion.

Sous chaque portion, une mini-étiquette avec la formule : `Q₁ = m c_solide Δθ`, `Q₂ = m L_fusion`,
`Q₃ = m c_liquide Δθ`, `Q₄ = m L_vaporisation`, `Q₅ = m c_gaz Δθ`.

*Point pédagogique à rendre visible* : le palier ❹ occupe à lui seul près des trois quarts de l'axe
des temps.

## 6. `pc-mur-flux-thermique` — paroi traversée par un flux thermique

*Utilisée par* : leçon `pc-flux-isolation` ; 3 exercices (unité de Φ, formule, calcul du mur de
parpaing).

Paroi parallélépipédique vue **en perspective cavalière** (face avant en gris clair hachuré,
épaisseur visible sur le côté droit).

- À gauche, zone `solideA` très claire avec un **thermomètre** et la mention **CHAUD**
  $T_{\text{chaud}}$ ; à droite, zone `solideB` très claire, **FROID** $T_{\text{froid}}$.
- Une **grosse flèche `solideD`** traverse la paroi de gauche à droite, étiquetée $\Phi$ ; deux ou
  trois flèches plus fines parallèles au-dessus et en dessous.
- Cotes : **$S$** sur la face avant (double flèche horizontale + double flèche verticale, ou simple
  étiquette au centre de la face) ; **$e$** sur l'épaisseur, en haut ; **$R_{\text{th}}$** posé sur
  la face, dans une petite étiquette encadrée.
- Sous la figure, la relation :
  $\Phi = \dfrac{S \times (T_{\text{chaud}} - T_{\text{froid}})}{R_{\text{th}}}$ avec les unités
  (W ; m² ; K ou °C ; m²·K·W⁻¹).

## 7. `pc-resistances-serie` — toit de combles aménagés (paroi composite)

*Utilisée par* : leçon `pc-flux-isolation` ; 4 exercices dont l'**exercice complet guidé**.

**Partie haute** : coupe d'un rampant de toiture, **incliné d'environ 30°**, formé de cinq bandes
parallèles d'épaisseurs proportionnées, de l'extérieur (haut) vers l'intérieur (bas), avec traits
de rappel vers les étiquettes de gauche :

| Couche | Aspect | Étiquette |
|---|---|---|
| Ardoise | bande gris foncé, très fine | `Ardoise — 0,003` |
| Bois de charpente | bande brun clair | `Bois de charpente — 0,333` |
| Air peu ventilé | bande blanche | `Air peu ventilé — 0,130` |
| Laine de verre | bande `solideE` pâle, **la plus épaisse** | `Laine de verre — 5,400` |
| Plaque de plâtre | bande blanche fine | `Plaque de plâtre — 0,040` |

À droite, une grosse flèche `solideD` traversant les cinq couches (le flux $\Phi$), avec `CHAUD`
(intérieur, en bas) et `FROID` (extérieur, en haut).

**Partie basse** : l'**analogie électrique** — cinq rectangles en **série** sur un fil horizontal,
chacun portant sa valeur (0,003 ; 0,333 ; 0,130 ; **5,400** ; 0,040), suivis du signe `=` et de la
somme encadrée **5,906 m²·K·W⁻¹**. Le rectangle de la laine de verre est dessiné nettement plus
large que les autres.

Légende `\scriptsize` : « couches accolées = résistances en série : elles s'additionnent ».

## 8. `pc-isolation-niveaux` — exigences réglementaires

*Utilisée par* : leçon `pc-flux-isolation` ; 1 exercice (niveau 3, conformité de la toiture).

Diagramme en **barres horizontales groupées**, axe des abscisses = résistance thermique
(m²·K·W⁻¹), gradué de 0 à 11.

Trois groupes (**Toit**, **Plancher**, **Façade**), chacun avec trois barres :

| Paroi | RT 2005 | Basse énergie | Très basse énergie |
|---|---|---|---|
| Toit | 5,0 | 6,7 | 10 |
| Plancher | 2,0 | 3,3 | 6,7 |
| Façade | 2,2 | 3,3 | 6,7 |

Couleurs : RT 2005 en `solideD`, « basse énergie » en `solideE`, « très basse énergie » en
`solideB` ; légende à droite ou en dessous.

Superposer une **ligne verticale rouge en pointillés** à **5,906 m²·K·W⁻¹**, étiquetée
« toit de l'exemple : 5,906 » : on doit voir d'un coup d'œil qu'elle dépasse la barre RT 2005 du
toit mais reste en deçà des deux autres.

Ajouter en `\scriptsize` sous le graphique : « valeurs **minimales** à atteindre (le livre les note
$R_{\max}$, il faut lire $R_{\min}$) ».
