# Figures à dessiner — unité « 2I2D Tle : analyse fonctionnelle et structurelle »

Douze figures TikZ nouvelles sont référencées par l'unité `2i2d-fonctionnel`
(`content/units/100-2i2d-fonctionnel.yaml` et `content/lessons/2i2d-*.md`). Tant qu'elles
n'existent pas dans `figures/tikz/`, `make content` échoue avec « figure inconnue » : ces douze
fichiers sont donc un **prérequis de build**.

Source des contenus : `docs/notes/cours-tle-a.md` (manuel Tle, p. 240-255),
`docs/notes/exercices-tle-a.md` (exercices 1 à 4, p. 306-319) et `docs/notes/exercices-tle-b.md`
(exercice 4, p. 320-322).

## Conventions communes

- un fichier par figure : `figures/tikz/<ID>.tex`, `\documentclass[tikz,border=4pt]{standalone}` +
  `\usepackage{liaisons}` (comme `figures/tikz/info-chaine-information.tex`, bon modèle de mise en
  page pour les chaînes fonctionnelles) ;
- couleurs de la bibliothèque : `solideA` (rouge), `solideB` (bleu), `solideC` (rose),
  `solideD` (orange), `solideE` (vert), `solideF` (violet) ;
- **code couleur de l'unité** :
  - chaîne d'**information** et diagrammes SysML « comportement » (uc, req) → `solideB` (bleu) ;
  - chaîne d'**énergie / puissance** et flux d'énergie → `solideD` (orange) ;
  - blocs de structure (bdd, ibd), fluides et pièces mobiles → `solideE` (vert) ;
  - éléments à mettre en évidence (repères ❶…❹, valeurs à retenir, bâti) → `solideA` (rouge) ;
- textes en `\small` / `\scriptsize`, **en français** ; les stéréotypes SysML restent en anglais
  entre guillemets français (`«requirement»`, `«block»`, `«include»`…) car ce sont des mots-clés
  normalisés ;
- largeur cible ≈ 8 cm (affichage mobile), hauteur ≤ 6,5 cm ; texte le plus court possible ;
- notations du manuel : $P$, $U$, $I$, $F$, $V$, $C$, $\omega$, $Q$, $p$, $\eta$, $R$, $Z$, $S$.

## Figures existantes réutilisées (ne rien redessiner)

`info-chaine-information` (chaîne ACQUÉRIR → TRAITER → COMMUNIQUER),
`transmission-engrenage`, `transmission-poulies`, `transmission-roue-vis`, `transmission-train`,
`transformation-pignon-cremaillere`, `transformation-vis-ecrou`,
`mecanisme-bielle-manivelle-schema`, `contact-pivot`, `cinematique-repere`,
`pc-presse-hydraulique`, `pc-chaine-energetique`.

---

## 1. `2i2d-uc-elements` — la légende du diagramme des cas d'utilisation

*Utilisée par* : leçon `2i2d-cas-exigences` ; 3 exercices de niveau 1.

Bandeau horizontal de **cinq vignettes** séparées par des filets verticaux fins gris, chacune
surmontée de son pictogramme et légendée en `\scriptsize` en dessous :

| Vignette | Pictogramme à tracer | Légende |
|---|---|---|
| 1 | Bonhomme filiforme (tête = cercle, corps + bras + jambes en traits) `solideB` | Acteur humain |
| 2 | Petit cube en perspective cavalière (bloc 3D) `solideE` | « Chose » en interaction (bateau, énergie…) |
| 3 | Ellipse `solideD` remplie très clair contenant `\scriptsize` « Franchir la Loire » | Cas d'utilisation |
| 4 | Flèche **pointillée** verticale montante à pointe ouverte, étiquette `«extend»` | Fonction **non** indispensable |
| 5 | Flèche **pointillée** verticale descendante à pointe ouverte, étiquette `«include»` | Fonction **indispensable** |

Sous le bandeau, une ligne `\scriptsize` : « acteurs **principaux** à gauche du système, acteurs
**secondaires** à droite ».

## 2. `2i2d-uc-transbordeur` — cas d'utilisation du pont transbordeur

*Utilisée par* : leçon `2i2d-cas-exigences` ; 3 exercices ; exercice guidé du transbordeur.

Cadre extérieur rectangulaire avec **onglet en haut à gauche** portant
`uc [Paquet] Utilisation principale`.

À l'intérieur, un rectangle central `solideB` (rempli très clair, bord `solideB` 1 pt) = frontière
du système, titré sur deux lignes centrées en haut : `«useCaseModel»` puis **Pont transbordeur**.
Ce rectangle contient trois ellipses `solideD` empilées verticalement, de haut en bas :

1. « Déambuler sur la rue aérienne »
2. « Franchir la Loire »
3. « Permettre le passage de bateaux »

Flèche **pointillée** de l'ellipse 1 vers l'ellipse 2, étiquetée `«extend»` ;
flèche **pointillée** de l'ellipse 2 vers l'ellipse 3, étiquetée `«include»`.

À gauche, **hors** du rectangle : bonhomme filiforme « Utilisateur » (en haut) et petit cube
« Busway » (en bas), chacun relié par un **trait plein** à l'ellipse « Franchir la Loire ».
À droite, hors du rectangle : deux petits cubes `solideE`, « La Loire » (haut) et « Bateaux »
(bas), reliés par des traits pleins aux ellipses.

## 3. `2i2d-req-transbordeur` — extrait du diagramme d'exigences

*Utilisée par* : leçon `2i2d-cas-exigences` ; 4 exercices (liens, priorités, lecture de valeurs).

Cadre extérieur avec onglet `req [Paquet] Exigences`. **Cinq** boîtes rectangulaires blanches à
bord `solideB`, à deux compartiments : en-tête (stéréotype en `\scriptsize` italique, puis nom en
gras) et corps (`Id = "…"` puis `Text = "…"`, texte **abrégé** pour tenir dans 8 cm).

| Position | Stéréotype | Nom | Id | Text (abrégé à tracer) |
|---|---|---|---|---|
| gauche, milieu | `«requirement»` | Franchissement de la Loire | "1" | Traverser la Loire à pied ou en busway |
| centre haut | `«requirement»` | Transport de véhicules et piétons | "1.1" | Charge utile de la nacelle : 100 tonnes |
| droite haut | `«functional Requirement»` | Traversée à pied | "1.1.1" | Deux cabines : 270 personnes |
| droite bas | `«functional Requirement»` | Traversée en busway | "1.1.2" | Un busway par traversée |
| extrême droite | `«physical Requirement»` | Dimensions d'un busway | "5" | Largeur 2,55 m — hauteur 3,12 m — 150 personnes |

*(La **longueur** du busway est illisible sur le scan du manuel — « mesure 18,1… mètres » — donc
volontairement absente de la figure et des exercices.)*

Liens à tracer :

- **décomposition** : trait plein terminé, du côté de l'exigence **générale**, par un petit
  **cercle barré d'une croix** (⊕) ; de « 1 » vers « 1.1 », puis de « 1.1 » vers « 1.1.1 » et
  vers « 1.1.2 » ;
- **`«refine»`** : flèche **pointillée** à pointe fermée allant de « 5 » vers « 1.1.2 »,
  étiquetée `«refine»`.

Légende `\scriptsize` sous le cadre : « ⊕ : l'exigence générale se décompose en exigences plus
détaillées — `«refine»` : précise l'exigence pointée ».

## 4. `2i2d-chaines-fonctionnelles` — les deux chaînes et l'ACTION

*Utilisée par* : leçon `2i2d-chaines` ; 4 exercices (entrées/sorties, ordres, matière d'œuvre).

Schéma d'ensemble en deux bandeaux superposés, à la manière de p. 244 du manuel :

- bandeau **haut**, bord et titre `solideB` : **Chaîne d'information**, contenant trois petits
  blocs blancs alignés **ACQUÉRIR → TRAITER → COMMUNIQUER** (flèches fines `solideB`) ;
- bandeau **bas**, bord et titre `solideD` : **Chaîne d'énergie**, contenant cinq petits blocs
  **ALIMENTER → DISTRIBUER → CONVERTIR → TRANSMETTRE → AGIR**.

Flèches à ajouter :

- entrées à gauche du bandeau haut : « Informations » (arrivant du haut) et
  « Consignes / Commandes » ; sortie à droite : « Messages » ;
- **flèche épaisse `solideD`** descendant du bandeau haut vers le bloc **DISTRIBUER**, étiquetée
  **« Ordres »** (point clé : l'ordre arrive sur *Distribuer*, pas sur *Alimenter*) ;
- à droite, un rectangle vertical `solideA` étiqueté **ACTION** (texte vertical) recevant la sortie
  du bandeau bas ; une grosse flèche creuse entre par le haut (« Matière d'œuvre entrante ») et une
  autre sort par le bas (« Matière d'œuvre sortante ») ;
- une flèche fine `solideD` partant du bloc **AGIR** vers la droite et le bas, étiquetée
  **« Pertes »** ;
- un retour en trait fin `solideB` de la zone ACTION vers l'entrée « Informations ».

## 5. `2i2d-chaine-energie` — chaîne d'énergie générique et composants

*Utilisée par* : leçon `2i2d-chaines` ; 6 exercices d'association fonction ↔ composant.

Cinq rectangles `solideD` alignés horizontalement, reliés par des flèches épaisses `solideD` :
**Alimenter → Distribuer → Convertir → Transmettre → Agir**.

Sous chaque rectangle, un petit cadre blanc à bord fin gris avec deux exemples de composants en
`\scriptsize`, relié au bloc par un trait fin :

| Bloc | Cadre d'exemples |
|---|---|
| Alimenter | Réseau EDF, batterie, réservoir |
| Distribuer | Distributeur, contacteur, relais |
| Convertir | Moteur électrique, pompe, vérin |
| Transmettre | Engrenages, poulies-courroie |
| Agir | Roue, pince, ventouse |

Au-dessus du bloc **Distribuer**, une étiquette `solideB` « Ordres » avec une flèche descendante
épaisse vers ce bloc. Flèche d'entrée à gauche d'*Alimenter*, flèche de sortie à droite d'*Agir*.

## 6. `2i2d-flux-effort` — grandeurs de flux et grandeurs d'effort

*Utilisée par* : leçon `2i2d-chaines` ; 5 exercices (dont un `grid`).

Quatre lignes, une par domaine, dessinées comme un **lien de puissance** : un segment horizontal
épais avec, **au-dessus**, la grandeur de flux (`solideE`) et, **en dessous**, la grandeur d'effort
(`solideA`) ; à droite du segment, le produit encadré `solideD` donnant la puissance.

| Domaine (à gauche) | Au-dessus : flux | En dessous : effort | Encadré à droite |
|---|---|---|---|
| Électrique (continu) | $I$ (A) | $U$ (V) | $P = U \times I$ |
| Mécanique — translation | $V$ (m·s⁻¹) | $F$ (N) | $P = F \times V$ |
| Mécanique — rotation | $\omega$ (rad·s⁻¹) | $C$ (N·m) | $P = C \times \omega$ |
| Hydraulique | $Q$ (m³·s⁻¹) | $p$ (Pa) | $P = Q \times p$ |

En bas, une mention `\scriptsize` : « dans tous les domaines : **puissance = flux × effort**,
en watts (W) ».

## 7. `2i2d-rendements-cascade` — rendement global d'une chaîne

*Utilisée par* : leçon `2i2d-chaines` ; 3 exercices ; exercice guidé du trolleybus.

Trois blocs `solideD` alignés (**Convertir** $\eta_1$, **Transmettre** $\eta_2$, **Agir**
$\eta_3$), traversés par une **flèche horizontale épaisse** `solideD` dont la largeur **diminue**
visiblement de gauche à droite (bande de type diagramme de Sankey).

- à gauche, étiquette $P_{\text{entrée}}$ ; à droite, $P_{\text{sortie}}$ ;
- sous chaque bloc, une **flèche fine grise descendante** étiquetée « pertes » ;
- sous l'ensemble, la relation encadrée
  $\eta = \dfrac{P_{\text{sortie}}}{P_{\text{entrée}}} = \eta_1 \times \eta_2 \times \eta_3$ ;
- application numérique en `\scriptsize` sous la relation, avec les valeurs de l'exercice guidé :
  $P_{\text{entrée}} = 10\,000$ W, $P_{\text{sortie}} = 6\,000$ W, $\eta = 0{,}60$.

## 8. `2i2d-bdd-ferry` — diagramme de définition de blocs (navette électro-solaire)

*Utilisée par* : leçon `2i2d-blocs` ; 5 exercices (losanges, multiplicités, lecture de *values*).

Cadre extérieur avec onglet `bdd [Paquet] Blocks [BDD Ferry Boat]`. Boîtes `solideE` à bord fin,
remplies très clair, à deux compartiments (en-tête `«stéréotype»` + nom en gras ; compartiment
*values* en `\scriptsize`).

Arborescence sur trois niveaux, du haut vers le bas :

1. `«system»` **Ferry Boat** — *values* : Longueur = 13 m ; Largeur = 4,70 m ; Vitesse = 7 nœuds ;
2. `«subsystem»` **Alimentation électrique** (aucune *value*), relié au système par un trait
   terminé par un **losange noir** ◆ **du côté du système** ;
3. quatre `«block»` sous le sous-système :
   - **Panneaux photovoltaïques Propulsion** — Modèle = CENIT 220 ; Puissance crête = 220 Wc ;
     Rendement = 13,8 % — lien à **losange noir**, portant la multiplicité **16** ;
   - **Panneaux photovoltaïques Service** — Modèle = CENIT 150 ; Puissance crête = 150 Wc ;
     Rendement = 11,8 % — lien à **losange noir**, multiplicité **8** ;
   - **Parc 1 Batteries Propulsion** — Technologie = Ni-Cd ; Tension = 384 V — losange noir ;
   - **Ventilateurs batteries** — Modèle = JABSCO DC150CFM — lien à **losange blanc** ◇
     (élément optionnel), pour que la figure montre les deux symboles.

Légende `\scriptsize` : « losange **noir** ◆ = obligatoire, losange **blanc** ◇ = optionnel ;
le nombre porté sur le lien est le nombre d'éléments identiques ».

## 9. `2i2d-ibd-ferry` — diagramme de blocs internes (alimentation électrique)

*Utilisée par* : leçon `2i2d-blocs` ; 4 exercices (ports, nature des flux, repères ❶…❹).

Cadre extérieur avec onglet `ibd [Subsystem] Alimentation électrique`. **Quatre** *parts*
rectangulaires `solideE` (bandeau titre `: Nom`, intérieur vide), disposées en L :

- rangée du bas, de gauche à droite : `: Panneaux photovoltaïques Propulsion`,
  `: Chargeur Propulsion`, `: Parc 1 Batteries Propulsion` ;
- au-dessus du chargeur : `: Battery Management System`.

Ports : **petits carrés `solideE` pleins** posés sur les bords des blocs, traversés par une flèche
**entrante**, **sortante** ou **double** (↔) selon le sens du flux. Connecteurs en traits noirs à
angles droits, avec la nature du flux écrite **au-dessus** de la ligne :

| Connecteur | Étiquette | Repère |
|---|---|---|
| bord gauche du cadre → `: Chargeur Propulsion` | Prise de quai EDF | ❶ |
| `: Panneaux…Propulsion` → `: Chargeur Propulsion` | Énergie électrique | ❷ |
| `: Chargeur Propulsion` → `: Parc 1 Batteries Propulsion` | Courant de charge | ❸ |
| `: Parc 1 Batteries…` ↔ `: Battery Management System` | 384 V Parc 1 | ❹ |
| `: Battery Management System` ↔ `: Chargeur Propulsion` (trait **bleu** `solideB`) | Bus CAN | — |

Les quatre repères sont de **petites pastilles rondes `solideA`** numérotées ❶ ❷ ❸ ❹ posées sur le
connecteur correspondant. Un second port d'entrée sur le bord gauche, étiqueté « Énergie solaire »,
alimente les panneaux.

## 10. `2i2d-schema-camera` — schéma cinématique 3D de la caméra dôme

*Utilisée par* : leçon `2i2d-structure` ; 4 exercices ; exercice guidé de la caméra dôme.

Schéma cinématique **en perspective** (repère $(x, y, z)$ en traits mixtes, $z$ vertical vers le
haut, $y$ vers la droite en fuyante, $x$ vers l'avant-gauche), largement simplifié par rapport à la
vue du manuel : on ne garde que **trois classes d'équivalence** et **deux liaisons pivot**.

De haut en bas :

- **Bâti (0)** en `solideA` : trait horizontal hachuré en haut, portant le symbole du bâti ;
  étiquette « Bâti 0 : plateau 3 + tiges 2 + platine 1 » ;
- **liaison pivot d'axe $(O, \vec{z})$** : symbole normalisé de pivot d'axe vertical, étiqueté
  « pivot $(O, \vec{z})$ — roulements 5 » ; à côté, une flèche courbe grise et la mention
  « rotation **horizontale** (panoramique) » ;
- **Classe 1** en `solideB` : trait vertical descendant puis coudé, étiqueté
  « 1 : chape 8 + poulie 14 » ; y accrocher, sur la gauche, un petit cylindre `solideB` figurant le
  moteur porté par la chape ;
- **liaison pivot d'axe $(A, \vec{y})$** : symbole normalisé de pivot d'axe horizontal, étiqueté
  « pivot $(A, \vec{y})$ — roulements 9 », avec flèche courbe grise et mention
  « rotation **verticale** (site) » ;
- **Classe 2** en `solideE` : petit parallélépipède avec un cylindre d'objectif en façade,
  étiqueté « 2 : module caméra 27 + chape 10 + roue 13 ».

Encadré `\scriptsize` en bas : « la rotation dite *horizontale* se fait autour de l'axe
**vertical** $z$ ; la rotation dite *verticale* se fait autour de l'axe **horizontal** $y$ ».

## 11. `2i2d-verin-double-effet` — vérin double effet et distributeur

*Utilisée par* : leçon `2i2d-fluidique` ; 6 exercices (symboles, $F = p \times S$, $Q = S \times V$).

Deux parties superposées.

**Partie haute — le symbole normalisé** : un rectangle horizontal (corps du vérin) traversé par une
**tige** sortant à droite ; au milieu, le **piston** en trait épais `solideE` ; deux orifices
d'alimentation sur la face gauche du corps, reliés à un **distributeur** dessiné dessous : trois
cases carrées accolées contenant flèches et croisement (X), avec un rectangle de pilotage
électrique `solideA` de chaque côté. Le distributeur est relié en bas à une source (triangle plein
= pompe) et au réservoir (symbole en T inversé).

**Partie basse — les grandeurs** : le même corps de vérin redessiné en coupe simplifiée, coté :

- **$S$** : section du piston (double flèche verticale sur le diamètre, `solideB`) ;
- **$p$** : pression d'alimentation, flèche `solideD` entrant par l'orifice de gauche ;
- **$F$** : force développée, grosse flèche `solideA` vers la droite en bout de tige ;
- **$V$** : vitesse de sortie de la tige, flèche `solideE` au-dessus de la tige ;
- **course** : double flèche en pointillés sous la tige.

Sous la figure, les trois relations encadrées :
$F = p \times S$ ; $Q = S \times V$ ; $P = Q \times p = F \times V$, avec les unités
(N ; Pa ; m² ; m³·s⁻¹ ; m·s⁻¹ ; W).

## 12. `2i2d-circuit-hydraulique` — planche des symboles fluidiques

*Utilisée par* : leçon `2i2d-fluidique` ; 6 exercices d'identification de symboles.

Un **circuit hydraulique complet** dessiné en boucle (traits noirs fins, largeur ≈ 8 cm), sur
lequel chaque composant est **numéroté** par une petite pastille `solideA` renvoyant à une légende
en deux colonnes sous le dessin. Parcours du fluide, dans le sens des aiguilles d'une montre :

| N° | Symbole à tracer | Légende |
|---|---|---|
| 1 | Rectangle ouvert en haut (réservoir) | Réservoir |
| 2 | Losange traversé par la conduite, trait pointillé au milieu | Filtre |
| 3 | Cercle marqué « M » relié par un axe à un cercle contenant un triangle plein | Moteur électrique et pompe |
| 4 | Bille appuyée contre un siège en « V » | Clapet anti-retour |
| 5 | Ovale vertical ouvert en haut | Accumulateur |
| 6 | Cercle avec une aiguille inclinée | Manomètre |
| 7 | Trois cases carrées accolées, pilotage électrique `solideA` de chaque côté | Distributeur piloté électriquement |
| 8 | Conduite étranglée traversée par une flèche oblique | Réducteur de débit |
| 9 | Deux triangles opposés par la pointe (nœud papillon) | Vanne |
| 10 | Corps de vérin avec piston et tige, deux orifices | Vérin double effet |

Le fluide est figuré par une **teinte `solideE` très claire** dans les conduites d'aller et
`solideB` très clair au retour vers le réservoir. Aucune vignette isolée : c'est le circuit complet
qui doit être lisible, pour que l'élève apprenne les symboles **en situation**.
