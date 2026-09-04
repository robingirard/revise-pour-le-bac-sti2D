# Figures à dessiner — unité `pc-mecanique` (physique : forces, énergie, dynamique)

Neuf figures TikZ sont référencées par les leçons de l'unité `pc-mecanique`
(`content/lessons/pc-forces.md`, `pc-travail-energie.md`, `pc-dynamique.md`, `pc-fluides.md`).
Tant qu'elles ne sont pas compilées, `tools/build_content.py` signalera
« leçon … : figure inconnue … » : ces neuf fichiers sont donc bloquants pour le build.

**Conventions communes** (voir `figures/tikz/cinematique-acceleration.tex` pour un modèle) :
fichiers `figures/tikz/<id>.tex`, classe `\documentclass[tikz,border=4pt]{standalone}`,
`\usepackage{liaisons}`, unités `x=1cm,y=1cm`.
Couleurs déjà définies dans `liaisons.sty` : `solideA` (rouge 225,55,25), `solideB` (bleu 45,75,205),
`solideC` (rose), `solideD` (orange 235,150,20), `solideE` (vert 20,150,90), `solideF` (violet).
Style de vecteur conseillé : `vect/.style={-{Stealth[length=5.5pt]}, line width=1.4pt}`.
Toutes les étiquettes en français, police `\small`, formules en mode mathématique.
Largeur cible : 6 à 10 cm (les figures sont affichées sur mobile).

Trois figures existantes sont réutilisées telles quelles et **ne sont pas à redessiner** :
`cinematique-acceleration`, `cinematique-champ-rotation`, `cinematique-chronogrammes`.

---

## 1. `pc-bilan-forces-livre` — bilan des forces sur un livre posé sur une table
*Leçon `pc-forces.md`, section « Bilan des forces sur un livre posé sur une table ».*

- Un rectangle horizontal gris clair (`black!15`, contour `black!55`), large (≈ 6 cm × 0,35 cm),
  étiqueté **Table** à son extrémité gauche, sous le rectangle.
- Posé dessus, centré, un rectangle plus petit (≈ 1,6 cm × 0,7 cm) rempli en `solideD!30`,
  contour `solideD`, étiqueté **Livre** à l'intérieur.
- Depuis le **centre du livre** (marquer le point par un disque plein noir de 1,6 pt, étiqueté $G$) :
  - une flèche `vect` **verte** (`solideE`) vers le **haut**, longueur 1,6 cm, étiquetée $\vec{R}$
    (étiquette à droite de la flèche) ;
  - une flèche `vect` **noire** vers le **bas**, **même longueur** 1,6 cm (elle traverse la table),
    étiquetée $\vec{P}$.
- Les deux flèches sont exactement alignées verticalement et de même longueur : c'est ce qui
  matérialise $R = P$.
- Sous la figure, en `\footnotesize` : « Système : le livre — Référentiel : terrestre ».

## 2. `pc-projection-force` — projection d'un vecteur force sur les axes
*Leçon `pc-forces.md`, section « Projeter un vecteur force sur les axes ».*

- Repère cartésien : axe horizontal $x$ (0 à 4,5 cm) et axe vertical $y$ (0 à 3 cm), flèches
  `-{Stealth}` en bout, origine notée $O$.
- Vecteurs unitaires $\vec{\imath}$ (horizontal) et $\vec{\jmath}$ (vertical) tracés en `solideA`,
  longueur 0,6 cm, à l'origine.
- Un vecteur `vect` **rouge** (`solideA`) $\vec{T}$ part de $O$ vers le haut à droite, angle **30°**,
  longueur 3,6 cm, étiqueté $\vec{T}$ au-dessus de son milieu.
- Depuis l'extrémité de $\vec{T}$ : un trait pointillé **vertical** descendant jusqu'à l'axe $x$
  (graduation notée $T_x$ sous l'axe) et un trait pointillé **horizontal** allant jusqu'à l'axe $y$
  (graduation notée $T_y$ à gauche de l'axe).
- Entre l'axe $x$ et $\vec{T}$, un secteur angulaire rempli en `solideE!25`, rayon 0,8 cm,
  étiqueté $\theta$.
- Annotation discrète en `\footnotesize` sous la figure :
  $T_x = T\cos\theta$ ; $T_y = T\sin\theta$.

## 3. `pc-bilan-forces-plan-incline` — caisse glissant à vitesse constante sur un plan incliné
*Leçon `pc-forces.md`, section « Le principe d'inertie ».*

- Un triangle rectangle gris (`black!12`, contour `black!55`) : sommet en bas à gauche, base
  horizontale de 6 cm, angle d'inclinaison **25°**, hachures fines sous l'hypoténuse pour figurer
  le sol. L'angle est coté $\alpha$ en bas à gauche par un petit secteur.
- Sur l'hypoténuse (le plan incliné), aux deux tiers de la montée, une caisse : carré de 0,9 cm de
  côté **incliné du même angle**, rempli `solideD!30`, contour `solideD`. Marquer son centre $G$.
- Trois flèches `vect` issues de $G$ :
  - $\vec{P}$ **noire**, **verticale vers le bas**, longueur 1,6 cm ;
  - $\vec{R_N}$ **verte** (`solideE`), **perpendiculaire au plan incliné**, longueur 1,45 cm
    (= $P\cos 25°$ à l'échelle), étiquetée « $\vec{R_N}$ (réaction normale) » ;
  - $\vec{f}$ **bleue** (`solideB`), **parallèle au plan**, dirigée **vers le haut de la pente**
    (opposée au mouvement), longueur 0,68 cm (= $P\sin 25°$), étiquetée $\vec{f}$.
- Une flèche fine en pointillés, parallèle au plan et dirigée **vers le bas de la pente**, étiquetée
  $\vec{v}$ = constante, placée en avant de la caisse.
- Les trois vecteurs doivent visiblement « se refermer » : $\vec{P} + \vec{R_N} + \vec{f} = \vec{0}$.
  Facultatif : reproduire le triangle des forces en petit, en haut à droite, en traits fins.

## 4. `pc-travail-force-angle` — travail d'une force selon l'angle α
*Leçon `pc-travail-energie.md`, tableau des travaux.*

Trois petits schémas alignés horizontalement (pas de 3,4 cm), numérotés **(1)**, **(2)**, **(3)**
au-dessus, et légendés en dessous.

Chaque schéma comporte :
- un segment fléché **bleu** (`solideB`, `vect`) horizontal du point **A** (à gauche) vers le point
  **B** (à droite), longueur 2,2 cm ; A et B marqués par une croix et étiquetés ; le segment porte
  l'étiquette $\overrightarrow{\mathrm{AB}}$ sous son milieu ;
- une flèche `vect` **rouge** (`solideA`) $\vec{F}$ issue de **A**, longueur 1,5 cm ;
- l'angle $\alpha$ entre $\vec{F}$ et $\overrightarrow{\mathrm{AB}}$ matérialisé par un secteur
  `solideE!25` de rayon 0,55 cm, étiqueté $\alpha$.

| Schéma | Orientation de $\vec{F}$ | Légende sous le schéma |
|---|---|---|
| (1) | oblique vers le haut **et vers B** (α = 40°) | $\alpha < 90^\circ$ — travail **moteur**, $W > 0$ |
| (2) | verticale vers le haut (α = 90°) | $\alpha = 90^\circ$ — la force **ne travaille pas**, $W = 0$ |
| (3) | oblique vers le haut **à l'opposé de B** (α = 140°) | $\alpha > 90^\circ$ — travail **résistant**, $W < 0$ |

## 5. `pc-energie-mecanique-chute` — énergie mécanique au cours d'une chute
*Leçon `pc-travail-energie.md`, section « L'énergie mécanique ».*

Deux repères côte à côte (pas horizontal ≈ 5,5 cm), même échelle, quadrillage fin `black!8`
(8 colonnes × 5 lignes). Axes : ordonnée $E$ (J), abscisse $t$ (s), flèches en bout.

- **Repère de gauche, titre « Sans frottement »** :
  - $E_m$ : droite **horizontale verte** (`solideE`), constante sur toute la largeur, étiquetée
    $E_m$ à droite ;
  - $E_c$ : courbe **bleue** (`solideB`) partant de 0 et croissant en s'incurvant vers le haut
    (parabole $t^2$), étiquetée $E_c$ ;
  - $E_{pp}$ : courbe **orange** (`solideD`) partant de la valeur de $E_m$ et décroissant jusqu'à 0,
    symétrique de $E_c$ par rapport à la droite $E_m/2$, étiquetée $E_{pp}$ ;
  - les deux courbes se croisent exactement au milieu ; à tout instant $E_c + E_{pp} = E_m$.
- **Repère de droite, titre « Avec frottements »** : mêmes couleurs, mais $E_m$ est une droite
  **légèrement décroissante** (pente négative faible), $E_{pp}$ décroît plus vite, $E_c$ croît en
  restant **sous** $E_m$ ; le croisement des deux courbes est plus tardif et plus bas.
  À tout instant $E_c + E_{pp} = E_m$, avec $E_m$ qui diminue.

## 6. `pc-moment-bras-levier` — moment d'une force et moment d'un couple
*Leçon `pc-dynamique.md`, section « Moment d'une force, moment d'un couple ».*

Deux panneaux côte à côte, séparés par un filet vertical `black!20`.

- **Panneau gauche — moment d'une force.** Une barre horizontale grise (`black!15`, contour
  `black!55`) de 4 cm articulée à gauche sur un axe : croix `×` étiquetée $(\Delta)$, entourée d'un
  petit cercle. Une flèche `vect` **rouge** (`solideA`) $\vec{F}$, **verticale vers le bas**,
  appliquée à l'extrémité droite de la barre. Une double flèche orange (`solideD`) sous la barre,
  entre l'axe et le point d'application, cotée $d$ (bras de levier), avec la mention en
  `\footnotesize` : « distance la plus courte entre $(\Delta)$ et la droite d'action ». La droite
  d'action de $\vec{F}$ est prolongée en pointillés fins.
  Formule sous le panneau : $M_\Delta(\vec{F}) = F \times d$.
- **Panneau droit — moment d'un couple (clé en croix).** Un cercle gris (jante) de rayon 1,1 cm
  avec quatre petits disques (écrous) ; une croix (la clé) superposée, traits épais `black!70`.
  Deux flèches `vect` **rouges** de **même longueur** (1,2 cm) et de **sens opposés**, appliquées aux
  deux extrémités horizontales de la clé : $\vec{F_1}$ vers le bas à droite, $\vec{F_2}$ vers le haut
  à gauche. Leurs droites d'action sont prolongées en pointillés verticaux ; la distance entre ces
  deux droites est cotée $d$ par une double flèche orange en bas.
  Formule sous le panneau : $M = F \times d$, avec $F = F_1 = F_2$ ;
  mention `\footnotesize` : « indépendant de la position de l'axe ».

## 7. `pc-point-fonctionnement-moteur` — caractéristiques couple-vitesse d'un ensemble moteur-charge
*Leçon `pc-dynamique.md`, section « Point de fonctionnement d'un ensemble moteur-charge ».*
**Figure clé, à soigner : c'est la seule lecture graphique de l'unité.**

- Repère orthogonal, quadrillage bleu clair (`solideB!12`) au pas de 100 tr·min⁻¹ (abscisse) et
  10 N·m (ordonnée).
- Ordonnée : « Couple utile $T_u$ (N.m) », graduations 0, 50, 100, 150.
- Abscisse : « Vitesse de rotation $n$ (tr.min$^{-1}$) », graduations 0, 200, 400, 600, 800, 1 000.
- **Courbe bleue** (`solideB`) « Caractéristique du moteur », marqueurs ronds, passant par
  (0 ; 60), (300 ; 70), (600 ; 103), (790 ; 145) — maximum —, puis **chute brutale** par
  (880 ; 65) jusqu'à (1 000 ; 0).
- **Droite rouge** (`solideA`) « Caractéristique de la charge », de l'origine (0 ; 0) à
  (1 000 ; 115).
- **Point A** marqué (disque plein) à l'intersection des deux courbes, aux environs de
  (900 ; 105), étiqueté **A** ; traits pointillés vers les deux axes.
- Encadré de légende en haut à gauche, avec les deux traits de couleur.

> Attention : les valeurs intermédiaires sont des **lectures graphiques approximatives** du manuel.
> Seules les valeurs citées dans le texte sont sûres : couple utile **100 N·m** et vitesse
> **légèrement supérieure à 900 tr·min⁻¹**. Le point A doit donc être placé juste **au-delà** de
> 900 tr·min⁻¹, à environ 100-105 N·m.

## 8. `pc-pression-profondeur` — colonne de liquide et principe fondamental de l'hydrostatique
*Leçon `pc-fluides.md`, section « Le principe fondamental de l'hydrostatique ».*

- Un cylindre vertical vu en perspective (ellipse en haut et en bas, hauteur 4,5 cm, demi-largeur
  1,4 cm), rempli d'un liquide bleu clair (`solideB!20`), contour `solideB`.
- Étiquettes : **AIR** au-dessus de la surface libre (avec la mention `\footnotesize`
  « $P = P_{\text{atm}}$ à la surface libre »), **LIQUIDE** et $\rho_{\text{liquide}}$ dans le
  volume.
- Deux points **B** et **B′** (croix) sur un même trait horizontal en pointillés, dans le tiers
  supérieur ; un point **A** (croix) sur un trait horizontal en pointillés, près du fond.
- Une double flèche verticale orange (`solideD`), à gauche, cote la dénivellation $h$ entre les deux
  plans.
- À droite, un axe vertical $Z$ (m) gradué, portant les repères $z_\mathrm{B} = z_{\mathrm{B}'}$
  (haut) et $z_\mathrm{A}$ (bas).
- Sous la figure, en `\footnotesize` : $P_\mathrm{B} = P_{\mathrm{B}'}$ ; $P_\mathrm{A} > P_\mathrm{B}$
  et $\Delta P = \rho\,g\,h$.

## 9. `pc-presse-hydraulique` — presse hydraulique
*Leçon `pc-fluides.md`, section « Deux applications ».*

- Deux cylindres verticaux reliés en bas par un conduit horizontal, l'ensemble rempli de liquide
  bleu clair (`solideB!20`), contour `black!55` ; forme générale en « U » aux branches de sections
  très différentes.
- **Branche gauche, étroite** (largeur 0,7 cm) : piston gris (`black!25`) surmonté d'une flèche
  `vect` rouge (`solideA`) **vers le bas** étiquetée $\vec{F_1}$ ; section cotée $S_1$ par une
  double flèche horizontale orange sous le piston.
- **Branche droite, large** (largeur 3,5 cm) : piston gris surmonté d'une flèche `vect` verte
  (`solideE`) **vers le haut** étiquetée $\vec{F_2}$, nettement plus longue que $\vec{F_1}$ ;
  section cotée $S_2$.
- Dans le liquide, trois ou quatre petites flèches fines rayonnantes (`solideB`) et la mention
  $P$ = même pression dans tout le liquide.
- Sous la figure, en `\footnotesize` : $P = \dfrac{F_1}{S_1} = \dfrac{F_2}{S_2}$, donc
  $F_2 = F_1 \times \dfrac{S_2}{S_1}$.

> Réserve pédagogique : la **presse hydraulique** (transmission intégrale de la pression par un
> liquide au repos) **ne figure pas** dans les pages transcrites du manuel
> (`docs/notes/pc-tle-cours-b.md`, ch. 8, p. 149-151), qui ne donne que $F = P \times S$,
> les pressions absolue/relative et $\Delta P = \rho g h$. La figure et l'exercice associé
> supposent la dénivellation entre les deux pistons négligeable. À confirmer avant publication.
