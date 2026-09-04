# Figures à dessiner — exercices guidés de physique-chimie (2ᵉ série)

Sept figures TikZ sont référencées par les **neuf nouveaux exercices guidés** ajoutés aux unités
`pc-ondes` (`content/units/70-pc-ondes.yaml`), `pc-mecanique` (`content/units/80-pc-mecanique.yaml`)
et `pc-tle-complements` (`content/units/90-pc-tle-complements.yaml`). Tant qu'elles n'existent pas
dans `figures/tikz/`, `make content` échoue avec « figure inconnue » : ces sept fichiers sont donc un
**prérequis de build**.

Les deux autres exercices guidés réutilisent des figures existantes et ne demandent aucun dessin :
« L'accumulateur Ni-Cd » réutilise `pc-pile-accumulateur`, « Alerte pollution » réutilise
`pc-echelle-ph`.

## Conventions communes

- un fichier par figure : `figures/tikz/<ID>.tex`, `\documentclass[tikz,border=4pt]{standalone}` +
  `\usepackage{liaisons}` ;
- couleurs de la bibliothèque utilisées ici : `solideA` (rouge), `solideB` (bleu), `solideD` (orange),
  `solideE` (vert) ;
- **code couleur** : signal émis / grandeur d'entrée = `solideA` ; signal reçu ou réfléchi = `solideB` ;
  cotes, lectures graphiques et grandeurs mesurées = `solideD` ; résultat, milieu récepteur ou état
  final = `solideE` ;
- textes en `\small` / `\scriptsize`, en **français**, avec les notations des exercices ;
- **écriture française des nombres** : virgule décimale, espace fine comme séparateur de milliers
  (0,40 ; 1 030 ; 10 994) ;
- largeur cible ≈ 8 cm (affichage mobile), hauteur ≤ 6 cm ;
- les figures illustrent l'énoncé : **ne rien y porter qui donne directement la réponse d'une étape**
  (pas de valeur calculée, pas de résultat final).

---

## 1. `guide-sismogramme` — lecture d'un enregistrement sismique

*Utilisée par* : exercice guidé « Le sismogramme : lire la double périodicité d'une onde »
(unité `pc-ondes`, compétence `pc-ondes-bases`).

Un **repère unique** avec quadrillage léger.

- Axe horizontal : $t$ (s), graduations **0 ; 0,10 ; 0,20 ; 0,30 ; 0,40**, régulièrement espacées.
- Axe vertical : $x$ (cm), graduations **−2 ; −1 ; 0 ; 1 ; 2**.
- **Sinusoïde `solideA`** d'amplitude 2,0 cm comptant **exactement 4 périodes** entre $t = 0$ et
  $t = 0{,}40$ s (donc une période de 0,10 s), partant de l'origine en montant.
- **Double flèche verticale `solideD`** à gauche, entre l'axe des abscisses et la première crête,
  annotée « amplitude ».
- **Double flèche horizontale `solideD`** au-dessus de la courbe, s'étendant de $t = 0$ à
  $t = 0{,}40$ s, annotée « **4 périodes** » (et non « T » : c'est à l'élève de diviser).

Titre au-dessus du repère, en `\small` : « Sismogramme — ondes S ». En légende `\scriptsize` :
« la célérité $v_\mathrm{S} = 4{,}0$ km·s⁻¹ est donnée par l'énoncé ».

## 2. `guide-cuve-ultrasons` — mesure de niveau par écho ultrasonore

*Utilisée par* : exercice guidé « Mesurer sans contact le niveau d'une cuve de produit toxique »
(unité `pc-ondes`, compétence `pc-son`).

Figure en deux parties côte à côte (ou empilées si la largeur le demande).

**Partie gauche — la cuve, en coupe.** Un **rectangle vertical** (paroi de la cuve, trait noir),
rempli sur son tiers inférieur d'un aplat `solideE!25` représentant le produit ; **surface libre**
tracée en trait plein `solideE`.

- Au-dessus de la cuve, un **petit boîtier gris** (le capteur) portant deux pastilles « É » et « R ».
- **Flèche `solideA`** descendante du capteur vers la surface, étiquetée « salve émise ».
- **Flèche `solideB`** montante, légèrement décalée, de la surface vers le capteur, étiquetée « écho ».
- **Cote `solideD`** verticale à gauche, du **fond** de la cuve jusqu'au capteur, annotée
  « **1,00 m** ».
- **Cote `solideD`** verticale à droite, du fond jusqu'à la surface libre, annotée $h$ (**sans
  valeur**).
- Étiquette `\scriptsize` « air » entre le capteur et la surface, « produit » dans l'aplat vert.

**Partie droite — l'oscillogramme.** Un écran d'oscilloscope (rectangle noir, quadrillage clair en
divisions carrées, 10 divisions de large).

- Trace du haut en `solideA` : **salve dense** d'oscillations à l'extrême gauche, étiquetée
  « Émetteur ».
- Trace du bas en `solideB` : ligne quasi plate, puis **salve dense** commençant **8 divisions**
  après le début de la salve émise, étiquetée « Récepteur ».
- **Double flèche `solideD`** entre les deux débuts de salve, annotée $\Delta t$.
- Sous l'écran, en `\scriptsize` : « base de temps : **250 µs par division** ».

## 3. `guide-cable-coaxial` — célérité d'une onde dans un câble coaxial

*Utilisée par* : exercice guidé « Le câble coaxial : mesurer la célérité d'une onde
électromagnétique » (unité `pc-ondes`, compétence `pc-ondes-em`).

**Partie haute — le montage** (schéma-blocs simple, pas de dessin réaliste).

- À gauche, un rectangle « Générateur d'impulsions » ; à droite, un rectangle « Oscilloscope ».
- Entre les deux, un petit **T** noir (la dérivation BNC en T), relié au générateur et à l'entrée de
  l'oscilloscope par des traits épais.
- Du T part vers le bas un **câble enroulé** (deux ou trois boucles arrondies) étiqueté
  « câble coaxial — **100 m** », se terminant par une **extrémité ouverte** (deux petits traits
  écartés, non reliés) étiquetée « extrémité **libre** ».
- **Flèche `solideA`** le long du câble, du T vers l'extrémité libre ; **flèche `solideB`** en
  sens inverse, légèrement décalée, étiquetée « onde réfléchie ».

**Partie basse — les deux oscillogrammes**, l'un sous l'autre, même échelle, quadrillage léger.

- **Courbe (1)** en `solideA` : signal créneau régulier (niveau bas, front montant, plateau,
  front descendant), période valant **8 divisions**. Étiquette « courbe (1) — sans le câble ».
- **Courbe (2)** en `solideA` : le **même** créneau, avec en plus un **palier intermédiaire**
  (petite marche `solideB`) apparaissant pendant la partie basse, décalé de **4 divisions** après le
  front descendant. Étiquette « courbe (2) — câble branché ».
- **Double flèche `solideD`** entre le front et le début du palier, annotée $\Delta t$.
- Sous les courbes, en `\scriptsize` : « base de temps : **0,25 µs par division** ».

## 4. `guide-curling-phases` — les quatre phases du lancer

*Utilisée par* : exercice guidé « Le curling : quatre phases, quatre bilans de forces »
(unité `pc-mecanique`, compétence `pc-forces`).

**Quatre vignettes alignées horizontalement** (ou 2 × 2 si la largeur l'impose), de même taille,
séparées par des traits verticaux fins. Chaque vignette montre la **même pierre de curling** — un
disque aplati vu de côté, gris, surmonté d'une petite poignée — posée sur un **trait horizontal
bleu clair** (la glace).

Sous chaque vignette, l'étiquette de la phase, en `\small` gras : **A**, **B**, **C**, **D**.
Au-dessus, une légende `\scriptsize` :

| Vignette | Légende | Élément ajouté |
|---|---|---|
| **A** | « pierre posée » | aucun ; pastille « $\vec{v} = \vec{0}$ » |
| **B** | « poussée par le lanceur » | silhouette schématique d'un bras, **flèche `solideA` horizontale** vers la droite au niveau de la poignée, étiquetée $\vec{F}$ |
| **C** | « glissement libre » | **flèche `solideD` horizontale** vers la droite au-dessus de la pierre, étiquetée $\vec{v}$, avec la mention « la vitesse diminue » |
| **D** | « balayage » | deux petits **balais** hachurés devant la pierre, **flèche `solideD`** étiquetée $\vec{v}$ et mention « vitesse constante » |

**Ne dessiner aucun vecteur poids ni aucune réaction normale** : c'est précisément ce que l'exercice
demande d'inventorier. Aucune valeur numérique sur la figure.

## 5. `guide-skieur-pente` — remontée puis descente

*Utilisée par* : exercice guidé « Le skieur : du tire-fesses au bas de la piste »
(unité `pc-mecanique`, compétence `pc-travail-energie`).

Un **triangle rectangle** unique représentant la montagne : base horizontale, sommet en haut à
droite, **hypoténuse** = la piste, inclinée d'un angle marqué **15°** à sa base (arc `solideD` et
étiquette).

- Sur l'hypoténuse, **deux silhouettes de skieur** très schématiques (un segment + un rond) :
  - la **basse**, montante, reliée par un trait fin à un **câble de tire-fesses** tendu au-dessus de
    la pente (poulies aux deux extrémités) ; **flèche `solideA`** vers le haut de la pente,
    étiquetée $\vec{T}$ ; mention `\scriptsize` « montée à **vitesse constante** » ;
  - la **haute**, au sommet, avec une **flèche `solideE`** vers le bas de la pente, étiquetée
    « $v_0 = 2{,}0$ m/s » ;
- **Cote `solideD`** le long de l'hypoténuse, du sommet au bas de la piste, annotée « **50,0 m** » ;
- **Cote `solideD` verticale** en pointillé, du sommet jusqu'à la base du triangle, annotée $h$
  (**sans valeur** : c'est l'étape 3 qui la fait calculer) ;
- petit rectangle d'angle droit entre la verticale et la base.

Aucun vecteur poids, aucune réaction normale : l'étape 2 demande justement de les inventorier.

## 6. `guide-fosse-mariannes` — pression et profondeur

*Utilisée par* : exercice guidé « La fosse des Mariannes : jusqu'où monte la pression ? »
(unité `pc-mecanique`, compétence `pc-fluides`).

Une **colonne d'eau verticale** occupant toute la hauteur de la figure, en dégradé `solideB!15`
(en haut) → `solideB!55` (en bas), fermée en bas par un **fond hachuré** (le plancher océanique,
profil irrégulier en V pour évoquer la fosse).

- Au-dessus de la surface libre, en `\small` : « AIR — $P_{\text{atm}} = 1\,013$ hPa », avec une
  petite flèche `solideD` descendante vers la surface.
- Étiquette `\small` dans l'eau, en haut à gauche : « eau de mer, $\rho = 1\,030$ kg·m⁻³ ».
- **Cote `solideD`** verticale à gauche, de la surface au fond, annotée
  « $h = 10\,994$ m ».
- Au fond, un petit **bathyscaphe** schématique (sphère + coque allongée) posé sur le relief, avec
  une bulle d'annotation `\scriptsize` : « mesure de 1960 : **1 087 bars** ».
- **Trois flèches `solideA`** perpendiculaires à la coque du bathyscaphe (une de chaque côté, une du
  dessus), de longueurs croissant avec la profondeur, pour rappeler que la pression s'exerce dans
  toutes les directions.
- En légende encadrée, sous la figure : $\Delta P = \rho\,g\,h$ et
  $P_{\text{abs}} = P_{\text{atm}} + \Delta P$, avec les unités (Pa ; kg·m⁻³ ; N·kg⁻¹ ; m).

**Aucune valeur de pression calculée** ne doit figurer sur le dessin.

## 7. `guide-spectre-fm` — spectre d'amplitude d'une modulation de fréquence

*Utilisée par* : exercice guidé « Modulons puis recevons : spectre d'une modulation de fréquence et
antenne » (unité `pc-tle-complements`, compétence `pc-signaux-spectres`).

Un **repère unique** avec quadrillage léger.

- Axe vertical : « amplitude $u$ (V) », non gradué (ou gradué 0 / 0,5 / 1 en `\scriptsize`).
- Axe horizontal : $f$ (kHz), portant **uniquement** les deux repères du livre : **500** et **515**,
  avec leurs traits de graduation. Ne porter ni 485, ni 505, ni 510 : c'est le comptage des
  intervalles qui est demandé à l'élève.
- **Sept raies verticales `solideA`**, régulièrement espacées (pas de 5 kHz dans l'échelle, soit
  trois intervalles entre les repères 500 et 515), s'étendant de 485 kHz à 515 kHz :
  la raie **la plus haute** est à l'aplomb de **500 kHz** ; les amplitudes décroissent de part et
  d'autre, la dernière à droite tombant exactement sur la graduation **515**.
  Trois raies plus courtes se trouvent à gauche de la raie principale.
- **Double flèche `solideD`** au-dessus des raies, entre la première et la dernière, sans annotation
  chiffrée, portant simplement l'étiquette « largeur de bande ».

Titre en `\small` au-dessus : « Spectre d'amplitude après modulation de fréquence ». Aucune mention
de la valeur de la porteuse ni de l'écart entre raies : ce sont les réponses des étapes 2 et 3.
