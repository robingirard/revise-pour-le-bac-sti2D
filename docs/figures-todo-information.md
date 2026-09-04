# Figures à dessiner — unité « Chaîne d'information et numérique »

Figures référencées par les leçons de l'unité `information` (`content/units/20-information.yaml`).
**Tant qu'elles ne sont pas compilées, `make content` échoue** avec « leçon … : figure inconnue … » :
`tools/build_content.py` vérifie que tout `{{fig:ID}}` a bien un SVG dans `figures/build/svg/`.

Conventions du dépôt (voir `figures/tikz/cinematique-chronogrammes.tex` comme modèle) :

- un fichier `figures/tikz/<ID>.tex` par figure, `\documentclass[tikz,border=4pt]{standalone}` +
  `\usepackage{liaisons}` ; le nom du fichier **est** l'identifiant utilisé dans `{{fig:ID}}` ;
- couleurs de la feuille de style : `solideA` (rouge), `solideB` (bleu), `solideC` (rose),
  `solideD` (orange), `solideE` (vert), `solideF` (violet) ; traits d'axe en `-{Stealth}`,
  courbes en `line width=1.4pt`, graduations en `\scriptsize` ;
- figures lisibles sur un écran de téléphone : peu de texte, pas de légende superflue, largeur ≈ 6 à 8 cm ;
- **vocabulaire imposé** : le convertisseur analogique-numérique se note **CAN** (anglais **ADC**).
  Ne jamais écrire « DAC » : le manuel source commet cette erreur, elle est corrigée dans le contenu.

| # | Identifiant | Leçon | Source (notes) |
|---|---|---|---|
| 1 | `info-chaine-information` | info-chaine | 1re, fig. 1, p. 54 |
| 2 | `info-signal-analogique-numerique` | info-chaine | Tle, fig. 1, p. 286 |
| 3 | `info-capteur-tor-hysteresis` | info-chaine | 1re, fig. 12, p. 59 |
| 4 | `info-signal-periodique` | info-signaux | Tle, fig. 2, p. 287 |
| 5 | `info-mli` | info-signaux | Tle, fig. 5, p. 288 |
| 6 | `info-can-symbole` | info-signaux | Tle, fig. 8, p. 289 |
| 7 | `info-can-quantum` | info-signaux | 1re, fig. 10, p. 58 |
| 8 | `info-poids-binaires` | info-numeration | Tle, fig. 7, p. 289 |
| 9 | `info-bases-triangle` | info-numeration | Tle, fig. 11, p. 291 |
| 10 | `info-chronogramme-et` | info-logique | Tle, fig. 13, p. 293 |
| 11 | `info-algorigramme-symboles` | info-algo | Tle, fig. 18, p. 296 |
| 12 | `info-algorigramme-structures` | info-algo | Tle, fig. 19, p. 296 |
| 13 | `info-sysml-etats` | info-algo | 1re, fig. 34-35, p. 72-73 |
| 14 | `info-sysml-sequence` | info-algo | Tle, fig. 14, p. 293 |

---

## 1. `info-chaine-information`

Trois rectangles blancs à bord `solideB`, alignés horizontalement et de même taille, titrés en
majuscules **ACQUÉRIR**, **TRAITER**, **COMMUNIQUER**, reliés de gauche à droite par deux flèches
épaisses `solideB`. Flèche entrante à gauche, étiquetée « Grandeurs physiques, consignes » ;
flèche sortante à droite, étiquetée « Informations (ordres, messages) ». Sous le titre de chaque
rectangle, deux ou trois puces en `\scriptsize` : *ACQUÉRIR* : « capteurs », « boutons, clavier » ;
*TRAITER* : « carte Arduino », « automate » ; *COMMUNIQUER* : « voyants, écran », « relais,
transistors », « réseau ». Un cadre arrondi léger englobe les trois blocs, titré « Chaîne d'information ».

## 2. `info-signal-analogique-numerique`

Trois petits repères côte à côte, même largeur, axe horizontal « Temps », axe vertical sans unité.

- *Signal logique* : une courbe grise en cloche (la grandeur physique), une droite horizontale
  pointillée notée « valeur seuil », et par-dessus un créneau `solideD` qui passe à 1 tant que la
  courbe est au-dessus du seuil ; deux petits disques `solideE` marquent les deux intersections.
- *Signal analogique* : la même courbe, tracée en trait plein `solideA`, sans seuil ni créneau.
- *Signal numérique* : axe vertical gradué de bas en haut `000`, `001`, `010`, `011`, `100`, `101`,
  `110`, `111` ; la courbe en pointillé et, par-dessus, l'escalier `solideA` qui l'approxime.

Titre au-dessus de chaque panneau : « Logique », « Analogique », « Numérique ».

## 3. `info-capteur-tor-hysteresis`

Repère « Grandeur d'entrée » (axe vertical) / « Temps » (axe horizontal). Sinusoïde `solideB` sur une
période. Deux droites horizontales proches : trait plein `solideD` étiqueté « Seuil haut (VT+) » et
trait pointillé `solideA` étiqueté « Seuil bas (VT−) », légèrement plus bas. En dessous, sur un second
axe partagé, le créneau de sortie en `solideE` : front montant à l'instant où la sinusoïde croise le
seuil haut **en montant**, front descendant à l'instant où elle croise le seuil bas **en descendant**.
Deux traits verticaux pointillés relient ces deux instants au créneau. Étiquette « Sortie » à droite du créneau.

## 4. `info-signal-periodique`

Sinusoïde `solideA` de trois périodes, axe horizontal $t$ passant au milieu, axe vertical $U$.
Double flèche horizontale `solideB` entre deux maxima consécutifs, étiquetée « Période $T$ ».
Double flèche verticale `solideE` de l'axe au sommet, étiquetée « Amplitude » ; seconde double flèche
verticale `solideE` du minimum au maximum, étiquetée « Amplitude crête-à-crête ». Ligne horizontale
pointillée `solideD` au niveau $U_{\text{eff}}$, étiquetée à gauche « Valeur efficace (rms) ».
Repères pointillés au sommet et au creux, avec l'étiquette $U_{\max}$ sur l'axe vertical.

## 5. `info-mli`

Axe vertical $V$, axe horizontal $t$. Trois créneaux rectangulaires identiques, de rapport cyclique
visiblement supérieur à 50 % (viser 70 %, la valeur de l'exemple de la leçon), régulièrement espacés.
Double flèche horizontale « Période $T$ » entre deux fronts montants successifs ; double flèche plus
courte, à l'intérieur du premier créneau, étiquetée $T_h$. Ligne horizontale `solideA` à 70 % de la
hauteur du créneau, étiquetée à droite « Tension moyenne ». Graduations $0$ et $U_{\max}$ sur l'axe vertical.

## 6. `info-can-symbole`

Carré à bord noir traversé par sa diagonale montante (de l'angle bas-gauche à l'angle haut-droit).
Dans le triangle supérieur gauche, le symbole d'une sinusoïde (∩) ; dans le triangle inférieur droit,
le symbole `#`. Flèche entrante à gauche, étiquetée $V_e$ (tension analogique). Trois flèches sortantes
à droite, étiquetées $b_0$, $b_1$, $b_2$ de bas en haut, regroupées par une accolade notée $N$.
Mention « CAN (ADC) » sous le carré — **pas** « DAC ».

## 7. `info-can-quantum`

Caractéristique de transfert d'un CAN 3 bits. Axe vertical « Sortie numérique » gradué `000`, `001`,
`010`, `011`, `100`, `101`, `110`, `111` ; axe horizontal « $V_e$ (V) » gradué de 0 à 7. Droite idéale
à 45° en trait fin pointillé, et par-dessus l'escalier `solideB` de 8 marches. Sur une marche du
milieu, double flèche horizontale entre deux pointillés verticaux, cotée $q$. Encadré discret :
$q = \text{amplitude} \div 2^n$.

## 8. `info-poids-binaires`

Décomposition de $(1101)_2 = 13$. Trois lignes alignées à droite d'un libellé : « Position » →
`3 2 1 0` ; « Valeur » → $2^3$, $2^2$, $2^1$, $2^0$ ; « Chiffres » → quatre cases carrées contenant
`1 1 0 1`. Sous les cases, quatre traits en équerre partant de chaque chiffre vers un encadré à droite
listant $1 \times 2^0 = 1$, $0 \times 2^1 = 0$, $1 \times 2^2 = 4$, $1 \times 2^3 = 8$, puis une case
« Total = 13 » mise en évidence. Flèches d'annotation : « bit de poids fort (msb) » vers la case de
gauche, « bit de poids faible (lsb) » vers la case de droite.

## 9. `info-bases-triangle`

Triangle des changements de base, sur l'exemple filé du nombre 59. Trois boîtes : en haut au centre
« Base 10 — $59_{(10)}$ » (`solideB`) ; en bas à gauche « Base 2 — $(0011\,1011)_2$ » (`solideE`) ;
en bas à droite « Base 16 — $(3B)_{16}$ » (`solideC`). Flèche Base 10 → Base 2 étiquetée « restes des
divisions successives par 2 » ; flèche Base 10 → Base 16 étiquetée « restes des divisions successives
par 16 » ; deux flèches remontant vers Base 10 partageant l'étiquette « somme des poids × chiffre » ;
double flèche horizontale Base 2 ↔ Base 16 étiquetée « blocs de 4 bits ». En bas, deux petits tableaux
de poids `8 4 2 1` : `0 0 1 1` → $2 + 1 = 3$ et `1 0 1 1` → $8 + 2 + 1 = 11 = B$.

## 10. `info-chronogramme-et`

Quatre axes de temps superposés, étiquetés à gauche $e_1$, $e_2$, « ET », « OU ». Les deux entrées sont
des créneaux `solideB` décalés, de sorte à faire apparaître les quatre combinaisons (0,0), (0,1),
(1,0), (1,1) dans cet ordre, séparées par des traits verticaux pointillés gris. Les deux sorties sont
des créneaux `solideA` : le ET n'est haut que sur le quatrième intervalle, le OU est haut sur les
trois derniers. États `0` et `1` écrits en `\scriptsize` au-dessus de chaque palier.

## 11. `info-algorigramme-symboles`

Une ligne de cinq cellules, chaque forme dessinée avec une flèche verticale entrante par le haut et,
en gras dessous, sa signification : rectangle à bouts arrondis → « Début / fin » ; rectangle →
« Traitement » ; rectangle à double barre verticale intérieure → « Sous-programme » ;
parallélogramme → « Entrée / sortie » ; losange (avec sorties « oui » en bas et « non » à droite) →
« Test / condition ». Formes remplies en blanc, bord `solideB`.

## 12. `info-algorigramme-structures`

Trois algorigrammes côte à côte, titrés « Linéaire », « Alternative », « Répétitive ».

- *Linéaire* : trois rectangles `Traitement 1`, `Traitement 2`, `Traitement 3` reliés verticalement.
- *Alternative* : losange `Condition` ; sortie « oui » vers le bas → `Traitement 1` ; sortie « non »
  vers la droite → `Traitement 2` ; les deux branches se rejoignent en bas sur une flèche commune.
- *Répétitive* : flèche entrante arrivant sur un point de jonction, puis losange `Condition` ; sortie
  « oui » à droite → `Traitement` dont la sortie remonte rejoindre le point de jonction **au-dessus**
  du losange ; sortie « non » vers le bas.

Rectangles en jaune pâle bord `solideD`, losanges bord `solideB`, liaisons de rebouclage en `solideF`.

## 13. `info-sysml-etats`

Diagramme d'états-transitions minimal, dans un cadre à onglet portant `stm [Machine à État] Volet`.
Pseudo-état de démarrage (disque noir plein) → état « Volet ouvert ». Deux états à coins arrondis
superposés, « Volet ouvert » et « Volet fermé », reliés par deux flèches opposées : celle qui descend
est étiquetée « N > 614 », celle qui remonte « N ≤ 614 ». Dans l'état « Volet fermé », un second
compartiment liste `entry / Éclairer voyant rouge` et `exit / Éteindre voyant rouge`. Trois étiquettes
de légende reliées en tirets : « Pseudo état de démarrage », « État », « Transition (événement) ».

## 14. `info-sysml-sequence`

Diagramme de séquence à deux lignes de vie, dans un cadre à onglet `sd`. Deux rectangles en haut,
`utilisateur:Bloc` et `carte:Bloc`, chacun surmontant un trait vertical pointillé et une barre
d'activation étroite. Quatre messages horizontaux numérotés : (1) flèche à pointe pleine vers la
droite « demande de mesure » ; (2) flèche pointillée vers la gauche « valeur N » ; (3) flèche à pointe
ouverte vers la droite « ordre de fermeture » ; (4) message réflexif sur la ligne de droite
(flèche qui part et revient en formant un rectangle) « comparer N au seuil ». Flèche verticale
`solideA` à gauche, étiquetée « sens d'écoulement du temps ». Un cadre étiqueté `loop [tant que
le système est en marche]` englobe les messages, pour illustrer un opérateur de séquence.

---

# Figures ajoutées (Tle et exercices guidés)

Six figures nouvelles, ajoutées avec les notions de Terminale (échantillonnage, codeur à deux voies)
et la compétence **Codage et transmission** (`info-transmission`). Mêmes conventions que ci-dessus :
un fichier `figures/tikz/<ID>.tex`, largeur ≈ 8 cm, peu de texte, couleurs `solideA` (rouge),
`solideB` (bleu), `solideD` (orange), `solideE` (vert).

| # | Identifiant | Leçon | Source (notes) |
|---|---|---|---|
| 15 | `info-echantillonnage` | info-signaux | Tle, § 4, p. 288 (échantillonnage) et fig. 9, p. 290 |
| 16 | `info-codeur-deux-voies` | info-chaine | exercices Tle B, ex. 7, fig. 2, p. 331 |
| 17 | `info-trame-serie` | info-transmission | exercices 1re B, ex. 14, chronogramme UART, p. 182 |
| 18 | `info-liaison-symetrique` | info-transmission | exercices 1re B, ex. 17, chronogramme DMX, p. 188 |
| 19 | `info-adressage-ip` | info-transmission | exercices Tle B, ex. 8, tableau d'adressage, p. 335 |
| 20 | `info-algorigramme-mini-voiture` | info-logique | exercices 1re B, ex. 12, algorigramme, p. 178 |

## 15. `info-echantillonnage`

Un seul repère : axe horizontal « Temps », axe vertical « Tension ». Une courbe lisse `solideB`
en cloche asymétrique (le signal analogique). Sur l'axe des temps, des graduations régulières
espacées de $T_e$ ; à chaque graduation, un trait vertical pointillé gris monte jusqu'à la courbe
et se termine par un disque plein `solideA` (l'échantillon prélevé). Par-dessus, l'escalier
`solideA` en trait plein qui joint les paliers successifs. Double flèche horizontale entre deux
graduations, cotée $T_e$, avec l'étiquette « période d'échantillonnage ». Encadré discret en haut
à droite : $f_e = 1 \div T_e$. Huit à dix échantillons suffisent pour que la figure reste lisible.

## 16. `info-codeur-deux-voies`

Deux panneaux côte à côte, titrés « Marche avant » et « Marche arrière », de même largeur.
Chaque panneau contient deux axes de temps superposés, étiquetés à gauche « Tête 1 » et
« Tête 2 » : deux créneaux `solideB` de rapport cyclique 1/2, sur trois périodes, la voie 2 étant
décalée d'un quart de période — **en retard** dans le panneau de gauche, **en avance** dans celui
de droite. Sur chaque panneau, un trait vertical pointillé `solideA` passe par un **front
descendant** de la tête 1 et descend jusqu'à la voie 2 ; l'état lu y est annoté en `\scriptsize`
(« Tête 2 = 1 » à gauche, « Tête 2 = 0 » à droite). Double flèche horizontale cotée $T/4$ entre les
deux fronts correspondants, dans le panneau de gauche seulement.

## 17. `info-trame-serie`

Chronogramme d'une trame série asynchrone, sur un seul axe de temps. Niveaux 0 et 1 gradués à
gauche. Le tracé `solideB` part du niveau haut (« Repos »), descend pour le **bit de start**,
puis enchaîne huit intervalles de même largeur étiquetés `D0` à `D7` sous l'axe, dont le motif
tracé correspond à 1 0 1 0 1 1 0 0 (le caractère « 5 », code ASCII 0011 0101, transmis poids
faible en tête), puis un intervalle « parité » à l'état 1, un intervalle « stop » à l'état 1, et
le retour au repos. Sous l'axe, quatre accolades `solideD` regroupent et nomment les champs :
« start », « 8 bits de donnée (D0 en tête) », « parité », « stop ». Deux étiquettes « Repos » aux
extrémités. Traits verticaux pointillés gris entre les intervalles.

## 18. `info-liaison-symetrique`

Trois repères superposés partageant le même axe des temps et le même quadrillage vertical
pointillé, étiquetés à gauche $U_{\text{DATA}+}$, $U_{\text{DATA}-}$ et
$U_{\text{DATA}+} - U_{\text{DATA}-}$.

- Panneau 1 : créneau `solideB` entre 0 et 5 V, portant une petite marche de 1 V (perturbation)
  pendant un état bas, annotée « perturbation de 1 V » par une flèche `solideD`.
- Panneau 2 : le créneau **complémentaire**, également entre 0 et 5 V, portant la **même** marche
  de 1 V au même instant.
- Panneau 3 : le signal différentiel `solideA`, gradué + 5 V, 0 V, − 5 V, parfaitement rectangulaire
  et **sans aucune perturbation**, avec l'étiquette « la perturbation commune disparaît ».

## 19. `info-adressage-ip`

Tableau de quatre colonnes (les quatre octets), sans bordure extérieure, aligné en `\ttfamily`.
Trois lignes étiquetées à gauche : « @ IP 10.0.3.19 » → `0000 1010 | 0000 0000 | 0000 0011 |
0001 0011` ; « Masque /22 » → `1111 1111 | 1111 1111 | 1111 1100 | 0000 0000` ; « Adresses
d'hôtes » → `0000 1010 | 0000 0000 | 0000 00xx | xxxx xxxx`. Un bandeau `solideB` translucide
couvre les 22 premiers bits des trois lignes, étiqueté « partie réseau (22 bits) » ; un bandeau
`solideD` couvre les 10 derniers, étiqueté « partie hôte (10 bits) ». Sous le tableau, deux
encadrés : « réseau : 10.0.0.0 » (`solideE`) et « diffusion : 10.0.3.255 » (`solideA`).

## 20. `info-algorigramme-mini-voiture`

Algorigramme en cascade, formes blanches, rectangles bord `solideD` et losanges bord `solideB`.
Stade « Début » → parallélogramme « Lire Capt_G » → parallélogramme « Lire Capt_D » → trois
losanges en escalier vers la droite : « Capt_G = 1 et Capt_D = 1 ? » (sortie **oui** vers le bas →
rectangle « Arrêt = 0 / Alarme = 0 ») ; « Capt_G = 1 et Capt_D = 0 ? » (oui → « Arrêt = 0 /
Alarme = 1 ») ; « Capt_G = 0 et Capt_D = 1 ? » (oui → « Arrêt = 0 / Alarme = 1 » ; **non**, sortie
la plus à droite → « Arrêt = 1 / Alarme = 1 »). Toutes les branches se rejoignent sur une ligne
horizontale basse `solideF` qui mène au stade « Fin ». Les sorties « non » des losanges sont
étiquetées à droite, les sorties « oui » en dessous.
