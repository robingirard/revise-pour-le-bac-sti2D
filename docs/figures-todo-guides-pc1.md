# Figures à dessiner — exercices guidés de physique-chimie (électricité, thermique, chimie)

Figures référencées par les neuf **exercices complets** (`type: guided`) ajoutés dans
`content/units/40-pc-electricite.yaml`, `content/units/50-pc-thermique.yaml` et
`content/units/60-pc-chimie.yaml`. Compléments de `docs/figures-todo-pc-electricite.md`,
`docs/figures-todo-pc-thermique.md` et `docs/figures-todo-pc-chimie.md`, dont les conventions
restent valables. Tant qu'elles ne sont pas produites, `tools/build_content.py` échoue avec
« figure inconnue » : ces six fichiers sont donc un **prérequis de build**.

**À produire :** un fichier `figures/tikz/<id>.tex` par figure (standalone,
`\documentclass[tikz,border=4pt]{standalone}` + `\usepackage{liaisons}`, comme
`figures/tikz/pc-loi-mailles-noeuds.tex`), compilé par `make figures` en
`figures/build/<id>.svg` ; le `stem` du SVG **est** l'identifiant utilisé dans `{{fig:ID}}`.

## Conventions communes

- largeur finale visée ≈ **8 cm** (appli mobile d'abord), hauteur ≤ 6 cm ;
- couleurs de la bibliothèque : `solideA` (rouge), `solideB` (bleu), `solideD` (orange),
  `solideE` (vert) ;
- codes couleur repris des unités : **électricité** — tensions en `solideB`, courants en `solideA` ;
  **thermique** — chaud `solideA`, froid `solideB`, flux thermique `solideD`, isolant `solideE` ;
  **chimie** — oxydation `solideA`, réduction `solideB` (comme `pc-pile-daniell`) ;
- textes en `\small` / `\scriptsize`, **en français**, notations du livre
  ($U$, $I$, $R$, $\rho$, $S$, $\theta$, $\Phi$, $R_{\text{th}}$, $\lambda$, $e$) ;
- **règle absolue** : ne jamais écrire sur la figure une valeur demandée par une étape de
  l'exercice guidé. Les figures ne portent que les **données** de l'énoncé et des **symboles**.

| # | Identifiant | Utilisée dans |
|---|---|---|
| 1 | `guide-facture-electricite` | guidé *La facture d'électricité* (compétence Énergie, puissance, rendement) |
| 2 | `guide-circuit-trois-branches` | guidé *Le circuit à trois branches* (compétence Tension et intensité) |
| 3 | `guide-cable-compteur-maison` | guidé *Le câble entre le compteur et la maison* (compétence Puissance et énergie électriques) |
| 4 | `guide-bouilloire-courbe` | guidé *La bouilloire électrique* (compétence Température et chaleur massique) |
| 5 | `guide-cycle-frigorifique` | guidé *Le super-congélateur à vaccins* (compétence Flux thermique et isolation) |
| 6 | `guide-pile-plomb-cuivre` | guidé *La pile plomb-cuivre* (compétence Oxydoréduction, corrosion et piles) |

Les trois autres exercices guidés réutilisent des figures existantes ou s'en passent :
*L'eau des pâtes* utilise `pc-courbe-chauffage-eau` ; *La vitamine C du jus d'orange* et
*Gaz de ville ou bioéthanol* n'utilisent pas de figure.

---

## 1. `guide-facture-electricite` — extrait d'une facture d'électricité

Reproduction simplifiée d'une facture, dessinée au trait (pas de capture d'image) : un cadre
arrondi de largeur 8 cm, découpé en trois blocs séparés par des bandeaux gris (`black!8`) portant
un titre en `\scriptsize` gras.

**Bandeau 1 — « Consommations »** : tableau à quatre colonnes (Nouveau relevé, Ancien relevé,
Différence, Conso en kWh) et deux lignes :

| | Nouveau | Ancien | Différence | kWh |
|---|---|---|---|---|
| HC — heures creuses | 25 913 | 24 391 | 1 522 | 1 522 |
| HP — heures pleines | 66 776 | 65 507 | 1 269 | 1 269 |

**Bandeau 2 — « Détails de la facturation »**, sous-titre `\scriptsize`
« TARIF bleu — PUISSANCE 6 kV·A — monophasé 230 V » ; trois lignes, montants alignés à droite :

- `Abonnement du 13.01.2022 au 13.08.2022` … `85,05 €`
- `Consommation HC : 1 522 kWh × 0,1360 €` … `206,99 €`
- `Consommation HP : 1 269 kWh × 0,1820 €` … `230,96 €`

**Bandeau 3 — « Total de la facture »** : montant **523,00 €** dans un cadre `solideA`,
épaisseur 1 pt.

Deux mentions manuscrites en `solideB`, `\scriptsize`, reliées par des flèches fines aux lignes
correspondantes : « puissance souscrite » (vers 6 kV·A) et « période facturée » (vers les dates).
Aucune intensité, aucune durée en jours, aucun coût estimé ne figure sur le document (ce sont
les réponses des étapes 1, 4 et 5).

## 2. `guide-circuit-trois-branches` — circuit à deux branches en dérivation

Circuit fermé rectangulaire (largeur ≈ 7 cm, hauteur ≈ 4,5 cm) : deux montants verticaux
(gauche et droite) reliés par **trois branches horizontales**. Les deux nœuds, en haut et en bas
du montant de droite, sont marqués par un disque plein de 1,8 pt.

- **Branche du haut** : un conducteur ohmique (rectangle blanc contour noir) étiqueté `R` ;
  sous lui, la tension donnée `2 V` ; puis une **lampe** (cercle barré d'une croix) dont la
  tension est notée $U_2$ (double flèche `solideB` sous la lampe, sans valeur) ; flèche de
  courant `solideA` orientée vers la droite étiquetée $I_2$.
- **Branche du milieu** : flèche de courant `solideA` étiquetée $I_1$, puis un conducteur ohmique
  étiqueté `100 Ω` ; tension $U_1$ en double flèche `solideB` au-dessus (sans valeur).
- **Branche du bas** : flèche de courant `solideA` étiquetée `0,20 A`, puis le symbole du
  **générateur** (deux traits parallèles de longueurs inégales) étiqueté `12 V`, puis une lampe
  étiquetée `1 V`.

Les branches du haut et du milieu sont explicitement repérées « en dérivation » par une accolade
grise à gauche. **Ne pas écrire** les valeurs de $U_1$, $U_2$, $I_1$, $I_2$ ni celle de $R$ :
ce sont les réponses des étapes 2 à 6.

## 3. `guide-cable-compteur-maison` — liaison compteur → habitation

Vue de principe, largeur ≈ 8 cm, hauteur ≈ 4 cm.

- À gauche, un **coffret de comptage** : rectangle vertical gris clair avec un afficheur, légende
  `Compteur` et, en dessous, `230 V — 9 kV·A`.
- À droite, une **maison** au trait (carré + toit à deux pentes), légende `Habitation`.
- Entre les deux, le **câble** : deux conducteurs parallèles horizontaux (aller et retour),
  épaisseur 1,2 pt, avec une flèche de courant `solideA` étiquetée $I$ sur le conducteur du haut.
- Sous le câble, une **cote** (double flèche fine + traits d'attache) étiquetée $L = 50$ m.
- Au milieu du câble, un **arrachement** montrant la section du conducteur : petit disque gris
  vu en bout, relié par un trait de rappel à l'étiquette $S$ ; à côté, la mention
  `cuivre : ρ = 1,7 × 10⁻⁸ Ω·m`.
- Au-dessus du câble, trois petites flèches ondulées `solideD` s'échappant vers le haut,
  étiquetées `pertes par effet Joule`.
- Sous la figure, encadrée en `\scriptsize` : $R = \rho \times \dfrac{L}{S}$ et
  $P_J = R \times I^{2}$, avec les unités (Ω ; Ω·m ; m ; m² ; W ; A).

Aucune valeur de $R$, de $I$ ni de $P_J$ (réponses des étapes 2 à 4), et **aucune section**
de câble (réponse de l'étape 1) ne doit apparaître.

## 4. `guide-bouilloire-courbe` — chauffage de 1,00 kg d'eau dans une bouilloire

Graphique $\theta$ (°C) en ordonnée, $t$ (s) en abscisse, grille pointillée légère (style de
`pc-courbe-chauffage-eau`). Largeur ≈ 8 cm, hauteur ≈ 5 cm.

- Abscisses de 0 à 350 s, graduations tous les 50 s ; ordonnées de 0 à 120 °C, graduations tous
  les 20 °C ; origine étiquetée $O$.
- **Tracé** en `solideB`, épaisseur 1,4 pt, en deux portions :
  - un **segment de droite** de $(0\,;20)$ à $(250\,;100)$ ;
  - un **palier horizontal** à 100 °C, de $t = 250$ s à $t = 320$ s.
- Traits de rappel en tirets gris : horizontal à $\theta = 100$ °C, vertical à $t = 250$ s ;
  valeurs 20 et 100 marquées sur l'axe des ordonnées, 250 sur l'axe des abscisses.
- **Triangle du coefficient directeur** sur la partie linéaire, en `solideA` : cathète
  horizontale de $(0\,;20)$ à $(250\,;20)$ étiquetée $\Delta t$, cathète verticale de
  $(250\,;20)$ à $(250\,;100)$ étiquetée $\Delta\theta$ — **sans écrire la valeur de la pente**,
  qui est la réponse de l'étape 3.
- Annotation `\scriptsize` au-dessus du palier : « palier d'ébullition ».
- En cartouche, en haut à gauche du graphique, les données :
  `m = 1,00 kg` · `R = 40 Ω` · `U_eff = 230 V` · `bouilloire très bien isolée`.

## 5. `guide-cycle-frigorifique` — cycle frigorifique d'un super-congélateur

Deux zones séparées par une **paroi isolante** verticale, hachurée, de couleur `solideE!30`,
cotée $e$ en haut et repérée $S$, $\lambda$ sur sa face.

- **À gauche, l'enceinte** (fond `solideB!8`) : mention `intérieur : −80 °C` et un pictogramme
  de flacons de vaccin (deux petits rectangles arrondis).
- **À droite, le local** (fond `solideA!8`) : mention `air ambiant : 20 °C`.
- Une **grosse flèche `solideD`** traverse la paroi de la droite vers la gauche (du chaud vers le
  froid), étiquetée $\Phi$ ; deux flèches plus fines parallèles au-dessus et en dessous.

Superposée à ces deux zones, la **boucle du fluide frigorigène** : quatre boîtes arrondies aux
sommets d'un rectangle, reliées par des flèches épaisses formant un circuit fermé orienté dans
le sens `Évaporateur → Compresseur → Condenseur → Détendeur → Évaporateur` :

| Position | Boîte | Couleur du cadre | Mention `\scriptsize` en dessous |
|---|---|---|---|
| bas gauche, **dans** l'enceinte | `Évaporateur` | `solideB` | liquide → gaz |
| haut gauche, à cheval sur la paroi | `Compresseur` | noir | la pression augmente |
| haut droite, dans le local | `Condenseur` | `solideA` | gaz → liquide |
| bas droite, dans le local | `Détendeur` | noir | la pression diminue |

Deux flèches d'échange d'énergie : une flèche `solideB` allant de l'air intérieur vers
l'évaporateur, étiquetée « énergie prélevée à l'air intérieur » ; une flèche `solideA` allant du
condenseur vers l'air du local, étiquetée « énergie cédée à l'extérieur ».

Données à porter, en `\scriptsize` : `propane, L_vaporisation = 426 kJ·kg⁻¹`, `100 g par cycle`,
`air intérieur : 750 g` ; et sur la paroi `e = 10 cm`, `S = 10 m²`, `λ = 0,0050 W·m⁻¹·K⁻¹`.
Ne pas faire figurer $R_{\text{th}}$, la valeur de $\Phi$, ni la baisse de température
(réponses des étapes 3, 4, 6 et 7).

## 6. `guide-pile-plomb-cuivre` — pile plomb-cuivre à légender

Schéma de principe (largeur ≈ 8 cm, hauteur ≈ 5 cm) construit comme `pc-pile-daniell`, mais
**sans les réponses** : c'est une figure à compléter mentalement.

- Deux **béchers** identiques, vus de face, contours noirs.
  - Bécher de gauche, légende `Compartiment A` : solution teintée `solideB!15`, mention
    `Cu²⁺ , 1,0 mol·L⁻¹ — 100 mL` ; une **lame verticale** gris rosé plongeant dans la solution,
    légende `lame de cuivre (200 g)`.
  - Bécher de droite, légende `Compartiment B` : solution incolore (contour seul), mention
    `Pb²⁺ , 1,0 mol·L⁻¹ — 100 mL` ; une **lame verticale** gris foncé, légende
    `lame de plomb (200 g)`.
  - Le compartiment où a lieu la réduction (cuivre) est repéré en `solideB`, celui où a lieu
    l'oxydation (plomb) en `solideA` : c'est le code couleur de l'unité, appliqué **au rôle**
    et non à la position.
- Un **pont salin** en arc de cercle reliant les deux solutions, dessiné en double trait,
  légende `pont salin`.
- Un **circuit extérieur** reliant le haut des deux lames, avec un **voltmètre** (cercle
  contenant `V`) au milieu.
- **Cinq points d'interrogation** `?` en `solideD`, encadrés, marquant ce que l'élève doit
  déterminer : deux au niveau des bornes, de part et d'autre du voltmètre (polarité), un sur le
  fil (sens conventionnel du courant), un dans chaque bécher (demi-équation de l'électrode).

Ne pas écrire les demi-équations, la polarité, le sens du courant ni l'évolution des masses :
ce sont les réponses des étapes 1 à 5.
