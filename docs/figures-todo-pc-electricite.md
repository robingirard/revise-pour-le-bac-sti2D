# Figures à dessiner — unité « Physique : énergie électrique »

Figures référencées par `content/units/40-pc-electricite.yaml` et
`content/lessons/pc-*.md`. Tant qu'elles ne sont pas compilées,
`tools/build_content.py` signale « figure inconnue » et `make content` échoue.

**Cadre technique** (identique aux figures existantes, cf. `figures/tikz/cinematique-chronogrammes.tex`) :

- un fichier `figures/tikz/<ID>.tex` par figure, `\documentclass[tikz,border=4pt]{standalone}` +
  `\usepackage{liaisons}` (fournit `arrows.meta`, `calc`, `patterns`, `\hachures`, `\repere`) ;
- couleurs de la charte : `solideA` rouge (225,55,25), `solideB` bleu (45,75,205),
  `solideC` rose (225,105,180), `solideD` orange (235,150,20), `solideE` vert (20,150,90),
  `solideF` violet (110,60,180) ;
- styles usuels : axes `-{Stealth[length=5pt]}, line width=0.6pt` ; courbes `line width=1.4pt` ;
  graduations `font=\scriptsize` ; pointillés `black!25, line width=0.4pt, dotted` ;
- **pas de `circuitikz`** dans le dépôt aujourd'hui : dessiner les symboles électriques en TikZ pur
  (rectangle vide = récepteur, cercle = générateur, deux traits parallèles = condensateur,
  suite d'arcs = bobine, zigzag ou rectangle = résistance). Si `circuitikz` est disponible dans la
  distribution TeX, son usage est possible mais doit rester local à ces figures ;
- largeur cible ≈ 7 cm (les figures sont insérées en ligne sur mobile) ; texte en français,
  virgule décimale, espace fine comme séparateur de milliers.

---

## 1. `pc-chaine-energetique`

*Utilisée : leçon `pc-energie-puissance`, 2 QCM (« lecture d'une chaîne énergétique »), énoncé de
l'exercice guidé.* — Source : cours 1re, p. 13-14.

Trois blocs alignés horizontalement, avec un titre au-dessus de chacun :

- titre « Batterie » ; en dessous un **rectangle** (bord `solideB`) contenant « **Énergie chimique** » ;
- titre « Convertisseur » ; en dessous une **ellipse** (bord `solideE`) contenant « **Moteur électrique** » ;
- titre « Disque en rotation » ; en dessous un **rectangle** (bord `solideB`) contenant
  « **Énergie cinétique** ».

Flèches épaisses (`-{Stealth[length=7pt]}`, `line width=1.2pt`, `solideE`) : rectangle 1 → ellipse,
étiquetée « **Électrique** » en `solideD` au-dessus ; ellipse → rectangle 3, étiquetée « **Mécanique** »
en `solideD`. Une troisième flèche part du bas de l'ellipse vers le bas-droite jusqu'au mot
« Environnement » (sans encadré), étiquetée « **Thermique** » en `solideD`.

Règle à faire lire sur la figure : **formes d'énergie encadrées, convertisseur entouré, nature du
transfert au-dessus des flèches**.

## 2. `pc-bilan-convertisseur`

*Utilisée : leçon `pc-energie-puissance`, QCM sur l'expression du rendement.* — Source : cours Tle, p. 130.

Diagramme sagittal, quatre éléments :

- à gauche, rectangle à coins arrondis, contour et texte `solideD` : « Énergie / absorbée » (deux lignes) ;
- grosse flèche horizontale `solideD` vers la droite ;
- au centre, ellipse contour et texte `solideE` : « Convertisseur » ;
- grosse flèche horizontale `solideE` vers la droite ;
- à droite, rectangle arrondi contour et texte `solideB` : « Énergie / utile » ;
- depuis le bas de l'ellipse, grosse flèche `solideE` vers le bas jusqu'à un rectangle arrondi
  contour `solideB!70` : « Pertes ».

Ajouter, sous le schéma, la formule $\eta = E_{\text{utile}}/E_{\text{reçue}}$ en petit
(`font=\small`) et la mention « toujours entre 0 et 100 % ».

## 3. `pc-energie-temps`

*Utilisée : leçon `pc-energie-puissance`, 3 exercices (pente de la rampe, palier, puissance moyenne).*
— Source : cours 1re, p. 14 (exemple de la puissance instantanée).

Repère :

- axe vertical `e(t) (kWh)`, graduations **12** et **24**, ligne pointillée horizontale grise à chaque
  niveau ; origine notée 0 ;
- axe horizontal `t (h)`, graduations **0, 6, 12, 18, 24**, tirets verticaux à 6, 12, 18 et 24.

Courbe `solideD`, ligne brisée continue passant **exactement** par
$(0;0) \to (6;12) \to (12;12) \to (18;24) \to (24;24)$ : deux rampes de pente 2 kW séparées et suivies
de deux paliers horizontaux.

Annoter en petit, au-dessus de la première rampe, « pente = 2 kW » et au-dessus du premier palier
« pente nulle : 0 kW » (couleur `solideB`, `font=\scriptsize`) : ces valeurs sont utilisées telles
quelles dans les exercices.

## 4. `pc-sinusoide-umax-ueff`

*Utilisée : leçon `pc-tension-intensite`, exercices « amplitude du réseau » et « lecture d'un
oscillogramme ».* — Source : cours 1re, p. 17 (figure 4), complétée.

- Axe vertical `u(t) (V)`, axe horizontal `t (s)` ; le zéro est repéré sur l'axe vertical.
- Sinusoïde `solideD` d'environ 2,5 périodes, oscillant autour d'une horizontale
  $U_{\text{moy}} = U_{DC}$ **située au-dessus de 0** ; la courbe descend donc légèrement sous zéro.
- Trois horizontales en pointillé `solideE` : $U_{\max}$ (tangente aux crêtes),
  $U_{\text{moy}} = U_{DC}$, $U_{\min}$ (tangente aux creux), étiquetées à gauche.
- Double flèche verticale noire entre la ligne $U_{\text{moy}}$ et une crête, étiquetée
  « Amplitude $U_m$ ».
- Double flèche horizontale sous une période complète, étiquetée « $T = 1/f$ ».
- Valeurs numériques suggérées (elles rendent la lecture cohérente avec l'exercice de niveau 3) :
  $U_{\max} = 8$ V, $U_{\min} = -2$ V, donc $U_{\text{moy}} = 3$ V et $U_m = 5$ V. Graduer l'axe
  vertical en $-2$, 0, 3, 8.
- Encadré en petit, à droite : $U_{\text{moy}} = (U_{\max}+U_{\min})/2$ et
  $U_m = (U_{\max}-U_{\min})/2$.

## 5. `pc-convention-generateur-recepteur`

*Utilisée : leçons `pc-tension-intensite` et `pc-puissance-electrique`, 3 exercices (conventions, signe
de P).* — Source : cours 1re, p. 18 (tableau des conventions).

Deux schémas côte à côte, séparés par un filet vertical gris, avec un titre au-dessus de chacun.

**À gauche — « Convention générateur »** : fil horizontal ; au centre un **cercle** de rayon 0,3 cm
(générateur). Au-dessus du fil, à gauche du cercle, flèche `solideB` **vers la droite** étiquetée $i(t)$.
Sous le cercle, flèche `solideB` **vers la droite** étiquetée $u(t)$. Légende dessous :
« tension et intensité dans le **même sens** ».

**À droite — « Convention récepteur »** : fil horizontal ; au centre un **rectangle** vide
(1,0 × 0,5 cm). Au-dessus du fil, à gauche du rectangle, flèche `solideB` **vers la droite** étiquetée
$i(t)$. Sous le rectangle, flèche `solideB` **vers la gauche** étiquetée $u(t)$. Légende dessous :
« tension et intensité en **sens opposé** ».

## 6. `pc-loi-mailles-noeuds`

*Utilisée : leçon `pc-tension-intensite`, QCM loi des nœuds et loi des mailles.* — Source : cours 1re,
p. 18 (figure 7).

Circuit rectangulaire (≈ 6 × 3,5 cm), tracé noir, flèches et étiquettes `solideB` :

- **branche gauche (verticale)** : cercle = générateur ; flèche $u_G(t)$ verticale **vers le haut**,
  placée à gauche du cercle (convention générateur) ; flèche de courant sortant vers le haut ;
- **branche haute** : depuis le haut du générateur, un **rectangle** portant la lettre $R$ ; flèche
  $i_R(t)$ **vers la droite** au-dessus du fil, à gauche de $R$ ; flèche $u_R(t)$ **vers la gauche**
  sous le rectangle (convention récepteur) ;
- **deux branches verticales en parallèle** à droite de $R$, entre le fil du haut et le fil du bas :
  - condensateur (deux traits horizontaux parallèles courts) : flèche $i_C(t)$ **vers le bas**
    au-dessus, flèche $u_C(t)$ **vers le haut** à droite du symbole ;
  - bobine (3 ou 4 arcs) : flèche $i_L(t)$ **vers le bas** au-dessus, flèche $u_L(t)$ **vers le haut**
    à droite du symbole ;
- **branche basse** : fil de retour reliant générateur, condensateur et bobine.

Marquer d'un **point noir plein** (rayon 1,2 pt) le nœud du haut, à gauche du condensateur : c'est là que
$i_R = i_C + i_L$. Une accolade ou une étiquette « nœud » peut le désigner.

## 7. `pc-bilan-puissances`

*Utilisée : leçon `pc-puissance-electrique` (bilan de puissance).* — Source : cours 1re, p. 21.

Un rectangle `solideD` à gauche étiqueté « Générateur », duquel part une flèche horizontale portant
$P_G$ ; cette flèche se divise (en trois flèches obliques) vers trois rectangles `solideB` empilés
étiquetés « Récepteur 1 », « Récepteur 2 », « Récepteur 3 », les flèches portant respectivement
$P_1$, $P_2$, $P_3$. Sous le schéma, en `font=\small` :
$P_G = P_1 + P_2 + \dots + P_n$ et $\Delta E_G = \Delta E_1 + \Delta E_2 + \dots + \Delta E_n$.

Facultatif (cohérent avec les exercices) : porter les valeurs $P_1 = 60$ W, $P_2 = 250$ W,
$P_3 = 1{,}2$ kW et $P_G = 1\,510$ W.

## 8. `pc-pertes-ligne`

*Utilisée : leçons `pc-puissance-electrique`, 4 exercices (pertes dans un câble, intérêt de la haute
tension, ligne 20 kV).* — Source : cours 1re, p. 21 (encadré sur les lignes haute tension) et cours Tle,
p. 136.

Schéma de principe d'une ligne :

- à gauche, un cercle (générateur) étiqueté « Production, $U$ » ;
- au centre, deux longs fils horizontaux (aller et retour) portant chacun un **rectangle** étiqueté
  $R$ (résistance de la ligne) ; flèche `solideB` $I$ sur le fil du haut, vers la droite ;
- à droite, un rectangle étiqueté « Consommateur, $P$ » ;
- au-dessus des rectangles $R$, en `solideA` : $P_{\text{pertes}} = R \times I^{2}$ ;
- sous le schéma, deux colonnes de comparaison en `font=\small` :
  « sous 230 V : $I = 87$ A » / « sous 20 kV : $I = 1{,}0$ A », avec $P = 20$ kW transportée,
  $R = 2{,}0\ \Omega$ et les pertes correspondantes ($\approx 15$ kW contre 2,0 W).

Les valeurs doivent être exactement celles-là : elles sont réutilisées dans les explications des
exercices.

## 9. `pc-dephasage-u-i`

*Utilisée : leçon `pc-sinusoidal-transport`, QCM sur le facteur de puissance.* — Source : cours Tle,
p. 134 (figure 5).

Repère quadrillé fin (gris clair). Axe vertical gradué $-1$ ; $-0{,}5$ ; 0 ; 0,5 ; 1.
Axe horizontal gradué 0 ; 0,5 ; 1 ; 1,5 ; 2 ; 2,5, étiqueté `t (s)`.

- Courbe `solideB` $u(t)$ : cosinusoïde d'amplitude 1, de période 1 s, maximale en $t = 0$, 1 et 2 s.
- Courbe `solideA` $i(t)$ : cosinusoïde d'amplitude 0,5, même période, **retardée** d'environ 0,1 s
  (soit $\varphi \approx 36°$) par rapport à $u(t)$.
- Étiquettes `u(t)` (bleu) et `i(t)` (rouge) près des courbes.
- Double flèche horizontale entre les deux maxima, étiquetée $\varphi$.
- À gauche du graphe, les deux formules en couleur : $u(t) = U\sqrt{2}\cos(\omega t)$ en `solideB`,
  $i(t) = I\sqrt{2}\cos(\omega t - \varphi)$ en `solideA`.

## 10. `pc-transformateur`

*Utilisée : leçon `pc-sinusoidal-transport`, 4 exercices (rôle, $U_2$, $I_1$, rapport $m$).* — Source :
cours Tle, p. 136-137 (figures 7 et 8).

Deux parties côte à côte dans un même cadre.

**À gauche — « Constitution »** : noyau de fer doux dessiné comme un **cadre rectangulaire gris**
(empilement de tôles suggéré par des traits verticaux fins) ; sur la branche gauche, un bobinage
`solideB` (5 à 6 spires) annoté « Circuit primaire, $N_1$ spires » ; sur la branche droite, un bobinage
`solideB` annoté « Circuit secondaire, $N_2$ spires ». Annotation « Noyau de fer doux » sur le cadre.

**À droite — « Symbole »** : deux bobines (deux séries de demi-cercles) séparées par un **trait vertical
double** (le noyau) ; à gauche, deux bornes d'entrée avec flèche `solideA` $I_1$ entrante en haut et
flèche `solideA` verticale $U_1$ ; à droite, flèche `solideA` $I_2$ sortante et flèche `solideA`
verticale $U_2$. Points homologues (petits points noirs) en haut de chaque enroulement.

Sous les deux schémas, la relation en `font=\small` :
$m = \dfrac{N_2}{N_1} = \dfrac{U_2}{U_1} = \dfrac{I_1}{I_2}$, avec la mention
« $m > 1$ : élévateur — $m < 1$ : abaisseur ».

## 11. `pc-reseau-transport`

*Utilisée : leçon `pc-sinusoidal-transport`, exercice `order` sur le parcours de l'électricité.* —
Source : cours Tle, p. 136 (« Les chemins de l'électricité »).

Bande horizontale divisée en trois zones titrées : **PRODUCTION** (`solideD`), **TRANSPORT**
(`solideE`), **DISTRIBUTION** (`solideF`), séparées par des flèches horizontales.

- Zone production (fond bleu très clair) : quatre pictogrammes stylisés — barrage, éolienne, centrale
  thermique (deux cheminées), centrale nucléaire (tour de refroidissement) — convergeant vers un
  rectangle « Poste de la centrale » ; étiquette **20 kV**.
- Zone transport (fond vert très clair) : deux pylônes reliés par des lignes ; étiquette **400 kV** ;
  un rectangle « Poste de transformation » avec les étiquettes **225 kV**, **90 kV**, **63 kV** ; puis
  un rectangle « Poste source » avec étiquette **20 kV**.
- Zone distribution (fond violet très clair) : un transformateur de quartier sur poteau et deux
  maisons ; étiquettes **400 V** et **230 V**.

Les six niveaux de tension doivent être lisibles isolément : l'exercice `order` demande de les remettre
dans l'ordre.

## 12. `pc-securite-abaque`

*Utilisée : leçon `pc-sinusoidal-transport`, QCM sur les seuils (10 mA).* — Source : cours 1re, p. 19 et
cours Tle, p. 137.

Repère à échelles **non linéaires** (logarithmiques) :

- axe vertical « Durée de passage du courant (ms) », graduations
  0 ; 20 ; 50 ; 100 ; 200 ; 500 ; 1 000 ; 2 000 ; 5 000 ; 10 000 ;
- axe horizontal « Intensité du courant traversant le corps humain (mA) », graduations
  0 ; 0,2 ; 0,5 ; 1 ; 2 ; 5 ; 10 ; 30 ; 100 ; 500 ; 2 000 ; 10 000.

Cinq bandes verticales colorées couvrant toute la hauteur, nommées en blanc en haut du graphe :
**vert** « Picotement » (0 à ≈ 1 mA), **jaune** « Tétanisation » (≈ 1 à 10 mA), **orange**
« Paralysie respiratoire » (≈ 10 à 40 mA), **orange foncé** « Fibrillation ventriculaire »
(≈ 40 à 500 mA), **rouge** « Arrêt cardiaque » (au-delà). Les frontières des trois dernières bandes
sont **incurvées** : elles se décalent vers la droite quand la durée diminue. Grille blanche fine.

Repère blanc : segment horizontal au niveau **500 ms** allant de l'axe vertical jusqu'à **30 mA**, puis
segment vertical descendant jusqu'à l'axe des abscisses.

Légende sous le graphe, cinq lignes avec pastille colorée :
`1 A` (rouge) « Arrêt du cœur » ; `50/75 mA` (orange foncé) « Seuil de fibrillation cardiaque
irréversible » ; `30 mA` (orange) « Seuil de paralysie respiratoire au-delà de 500 ms » ;
`10 mA` (jaune) « Seuil de non-lâcher, contraction musculaire » ; `0,5 mA` (vert) « Seuil de
perception, sensation très faible ».
