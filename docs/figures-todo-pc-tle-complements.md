# Figures à dessiner — unité `pc-tle-complements`

Dix figures TikZ à produire dans `figures/tikz/<id>.tex` (standalone, `\usepackage{liaisons}`,
compilées en SVG par `tools/build_figures.py`). Elles sont déjà référencées par les leçons
`content/lessons/pc-*.md` et par les exercices de `content/units/90-pc-tle-complements.yaml` :
tant qu'elles n'existent pas, `tools/validate.py` signalera « figure inconnue » sur `dist/`.

Conventions communes (comme les figures existantes) :

- `\documentclass[tikz,border=4pt]{standalone}`, `\usepackage{liaisons}` ;
- palette de `figures/tikz/liaisons.sty` : `solideA` rouge (225,55,25), `solideB` bleu (45,75,205),
  `solideC` rose, `solideD` orange (235,150,20), `solideE` vert (20,150,90), `solideF` violet ;
- axes : `-{Stealth[length=5pt]}`, `line width=0.6pt` ; courbes : `line width=1.3pt`, `line cap=round` ;
- textes en `\small`, nombres en **écriture française** (virgule décimale, espace fine comme séparateur
  de milliers : 5 730, 20 000) ;
- largeur cible ≈ 8 à 12 cm, lisible sur téléphone : pas plus de 8 étiquettes par figure.

---

## 1. `pc-desintegrations` — les trois désintégrations et le rayonnement γ

Quatre lignes empilées, une par rayonnement, dans un cadre léger. Chaque ligne : noyau père à gauche,
flèche horizontale `-{Stealth}` étiquetée au-dessus, noyau fils à droite, puis flèche oblique montante
vers la particule émise.

| Ligne | Père | Flèche | Fils | Particule émise |
|---|---|---|---|---|
| 1 | amas sphérique de billes (2 couleurs) noté $^{A}_{Z}\mathrm{X}$ | α | amas légèrement plus petit, $^{A-4}_{Z-2}\mathrm{Y}$ | petit amas de 4 billes (2 `solideD` + 2 `solideB`), étiquette « particule α : $^{4}_{2}\mathrm{He}$ » |
| 2 | $^{14}_{6}\mathrm{C}$ « 6 protons / 8 neutrons » | β⁻ | $^{14}_{7}\mathrm{N}$ « 7 protons / 7 neutrons » | petit disque `solideE` marqué « − », étiquette « électron » |
| 3 | $^{10}_{6}\mathrm{C}$ « 6 protons / 4 neutrons » | β⁺ | $^{10}_{5}\mathrm{B}$ « 5 protons / 5 neutrons » | petit disque `solideA` marqué « + », étiquette « positron » |
| 4 | noyau fils **excité**, noté $^{A}_{Z}\mathrm{Y}^{*}$ | γ | même noyau $^{A}_{Z}\mathrm{Y}$ (désexcité) | onde sinusoïdale courte `solideF` terminée par une flèche, étiquette « photon γ » |

Légende sous la figure : pastille `solideD` = **proton**, pastille `solideB` = **neutron**.
Encadré à droite de la ligne 4 : « $A$ et $Z$ inchangés ».
Les noyaux sont des amas de disques de 1,6 mm de diamètre, empilés en quinconce (5 à 12 disques suffisent :
il ne s'agit pas de représenter les 14 nucléons exactement, mais l'idée d'un amas — le nombre de protons
et de neutrons est donné par le texte de l'étiquette).

## 2. `pc-decroissance-radioactive` — courbe de décroissance

Repère : axe vertical $N$ (ou $A$), axe horizontal $t$. Courbe exponentielle décroissante `solideA`,
$N(t) = N_0 e^{-\ln 2 \cdot t/t_{1/2}}$, tracée de $t = 0$ à $t = 3{,}4\,t_{1/2}$ (`plot[domain=…, samples=60, smooth]`).

- ordonnées graduées $N_0$, $\dfrac{N_0}{2}$, $\dfrac{N_0}{4}$, $\dfrac{N_0}{8}$, avec traits **pointillés
  horizontaux** gris jusqu'à la courbe ;
- abscisses graduées $0$, $t_{1/2}$, $2\,t_{1/2}$, $3\,t_{1/2}$, avec traits **pointillés verticaux** ;
- au-dessus de la courbe, quatre petites vignettes carrées (grille 4 × 4 de pastilles) montrant la
  population aux dates 0, $t_{1/2}$, $2\,t_{1/2}$, $3\,t_{1/2}$ : respectivement 16, 8, 4 et 2 pastilles
  `solideD` (noyau père), le reste en `solideB` (noyau fils) ;
- légende : pastille `solideD` = « noyau père $^{A}_{Z}\mathrm{X}$ », pastille `solideB` = « noyau fils » ;
- annoter la première marche par une accolade et le texte « à chaque $t_{1/2}$ : ÷ 2 ».

## 3. `pc-fission-fusion` — fission et fusion, côte à côte

Deux panneaux séparés par un filet vertical fin.

**Panneau gauche — fission.** De gauche à droite : petit cercle blanc à contour noir étiqueté « neutron »,
flèche `-{Stealth}` vers un gros amas de billes `solideA`/blanches étiqueté $^{235}_{92}\mathrm{U}$.
À droite, halo `solideD` (cercle rempli, opacité 0,25) entourant **deux** amas fils : celui du haut
$^{94}_{38}\mathrm{Sr}$, celui du bas $^{140}_{54}\mathrm{Xe}$. Mot « ÉNERGIE » en `solideD` gras au centre du
halo. Deux flèches sortantes vers la droite, chacune vers un petit cercle blanc « neutron ».
Sous le panneau, l'équation :
$^{1}_{0}\mathrm{n} + {}^{235}_{92}\mathrm{U} \rightarrow {}^{94}_{38}\mathrm{Sr} + {}^{140}_{54}\mathrm{Xe} + 2\,^{1}_{0}\mathrm{n}$.

**Panneau droit — fusion.** En haut à gauche un amas de 2 billes « deutérium », en bas à gauche un amas de
3 billes « tritium ». Deux flèches convergent vers un amas central de 4 billes entouré d'un halo `solideD`,
étiqueté « hélium », avec « ÉNERGIE » en dessous. Une flèche horizontale sort à droite vers un petit cercle
blanc « neutron libre ». Sous le panneau : « deutérium + tritium → hélium + neutron + énergie ».

Titres des panneaux, en gras : « Fission » et « Fusion ».

## 4. `pc-pile-accumulateur` — pile en décharge, puis accumulateur en recharge

Deux schémas côte à côte, même géométrie, pour montrer que **la polarité ne change pas** et que **le sens
des électrons s'inverse**.

**Schéma gauche — décharge.** En haut, rectangle « charge électrique » relié par deux fils aux électrodes ;
sur les fils, flèches `solideB` étiquetées $i$ (de la borne ⊕ vers la charge, puis vers la borne ⊖) et
flèches `solideE` étiquetées $e^-$ **en sens inverse**. Deux béchers rectangulaires reliés par un tube en U
inversé `solideE` étiqueté « pont salin ».

- électrode **gauche** : plaque grise étiquetée $\mathrm{PbO_2}$, pastille **⊕** rouge, mention « cathode » ;
  annotation en `solideB` : « réduction : $\mathrm{PbO_2} + 4\,\mathrm{H^+} + 2\,e^- = \mathrm{Pb^{2+}} + 2\,\mathrm{H_2O}$ » ;
- électrode **droite** : plaque grise étiquetée $\mathrm{Pb}$, pastille **⊖** noire, mention « anode » ;
  annotation en `solideA` : « oxydation : $\mathrm{Pb} = \mathrm{Pb^{2+}} + 2\,e^-$ ».

**Schéma droit — recharge.** Le rectangle du haut devient un **générateur** (symbole à bornes + et −).
Les pastilles ⊕ et ⊖ restent **aux mêmes électrodes** ; les flèches $i$ et $e^-$ sont **inversées** ;
gauche devient « anode / oxydation : $\mathrm{Pb^{2+}} + 2\,\mathrm{H_2O} = \mathrm{PbO_2} + 4\,\mathrm{H^+} + 2\,e^-$ »,
droite devient « cathode / réduction : $\mathrm{Pb^{2+}} + 2\,e^- = \mathrm{Pb}$ ».

Sous les deux schémas, l'équation réversible avec deux flèches superposées : celle du haut (`solideA`, vers
la droite) étiquetée « décharge », celle du bas (noire, vers la gauche) étiquetée « recharge » :
$\mathrm{PbO_2} + 4\,\mathrm{H^+} + \mathrm{Pb} \rightleftarrows 2\,\mathrm{Pb^{2+}} + 2\,\mathrm{H_2O}$.

Bandeau en bas, encadré : « Les polarités ⊕ et ⊖ ne changent pas ; le sens des électrons, si. »

## 5. `pc-pile-combustible` — cellule H₂ / O₂

Cellule rectangulaire verticale, membrane centrale en bande claire.

- à **gauche** : entrée « $\mathrm{O_2}$ » (flèche vers la droite) sur l'électrode marquée **⊕**, annotation
  `solideB` : « cathode — réduction : $\mathrm{O_2} + 4\,\mathrm{H^+} + 4\,e^- = 2\,\mathrm{H_2O}$ » ;
  sortie « $\mathrm{H_2O}$ » en bas à gauche (flèche sortante) ;
- à **droite** : entrée « $\mathrm{H_2}$ » (flèche vers la gauche) sur l'électrode marquée **⊖**, annotation
  `solideA` : « anode — oxydation : $\mathrm{H_2} = 2\,\mathrm{H^+} + 2\,e^-$ » ;
- dans la membrane : quatre pastilles `solideD` « $\mathrm{H^+}$ » migrant **de droite à gauche** (petites
  flèches) ;
- en haut, un fil relie les deux électrodes à une ampoule allumée ; sur le fil, flèches `solideE` « $e^-$ »
  allant de l'électrode ⊖ vers l'électrode ⊕.

Sous la figure : $2\,\mathrm{H_2} + \mathrm{O_2} \rightarrow 2\,\mathrm{H_2O}$.

## 6. `pc-echelle-ph` — échelle de pH

Axe horizontal fléché vers la droite, étiqueté « pH », graduations **0**, **7**, **14** avec traits verticaux.

- segment **0 → 7** en dégradé `solideA` (rouge), surmonté du texte rouge « solutions acides » ;
- segment **7 → 14** en dégradé `solideE` (vert), surmonté du texte vert « solutions basiques » ;
- repère « pH = 7,0 : neutre » sous la graduation 7 ;
- sous l'axe, une seconde règle alignée donnant $[\mathrm{H_3O^+}]$ : $10^{0}$, $10^{-7}$, $10^{-14}$ mol·L⁻¹,
  avec la mention « $[\mathrm{H_3O^+}] = 10^{-\mathrm{pH}}$ » et une flèche indiquant que
  $[\mathrm{H_3O^+}]$ **diminue** quand le pH augmente ;
- trois repères illustratifs facultatifs, en petits caractères, sous l'axe : jus de citron (≈ 2),
  eau pure (7,0), déboucheur (≈ 13).

## 7. `pc-dilution-ph` — évolution du pH lors d'une dilution

Deux axes horizontaux fléchés « pH », superposés, étiquetés à gauche **Cas 1** et **Cas 2**.

- **Cas 1** (solution acide diluée), de gauche à droite : repère `solideA` « pH de la solution avant
  dilution », puis repère `solideE` « pH de la solution diluée » (au-dessus de l'axe), puis repère
  « pH de l'eau distillée » ; une flèche courbe part du premier repère vers le deuxième, étiquetée
  « + eau » ;
- **Cas 2** (solution basique diluée), de gauche à droite : « pH de l'eau distillée », puis « pH de la
  solution diluée », puis `solideA` « pH de la solution avant dilution » ; flèche courbe du repère de droite
  vers celui du milieu, étiquetée « + eau ».

Dans chaque cas, matérialiser par une **accolade** que la valeur diluée est **encadrée** par les deux autres.
Bandeau en bas : « La dilution rapproche le pH de celui de l'eau distillée, sans jamais le dépasser. »

## 8. `pc-spectre-signal` — du signal temporel au spectre d'amplitude

Deux repères côte à côte, sur l'exemple du cours
$s(t) = 2 + 1 \sin(2\pi f_1 t) + 0{,}5 \sin\!\left(2\pi (2f_1) t + \tfrac{\pi}{2}\right)$.

**Repère gauche (temporel)** : axes $u$ (V) / $t$ (s), quadrillage léger.

- droite horizontale `solideE` en pointillés à l'ordonnée 2 : composante continue $A_0 = 2$ ;
- sinusoïde `solideB` en pointillés, amplitude 1, période $T_1 = 1/f_1$ ;
- sinusoïde `solideA` en pointillés, amplitude 0,5, période **moitié**, déphasée de $\pi/2$ ;
- courbe noire épaisse = somme des trois, étiquetée $s(t)$, oscillant autour de 2 ;
- double flèche horizontale en haut, entre deux verticales pointillées, étiquetée $T$.

**Repère droit (fréquentiel)** : axes $u$ (V) gradué 0, 1, 2 / $f$ (Hz).

- raie `solideE` de hauteur **2** à $f = 0$ (composante continue) ;
- raie `solideB` de hauteur **1** à $f_1$, étiquetée « fondamental » ;
- raie `solideA` de hauteur **0,5** à $f_2 = 2 f_1$, étiquetée « harmonique de rang 2 » ;
- graduations $0$, $f_1$, $f_2$ sur l'axe des abscisses.

Flèche large entre les deux repères, étiquetée « décomposition de Fourier ».

> Remarque pour le dessinateur : sur le scan du livre (p. 172), la raie de la composante continue à 0 Hz
> n'est pas distinguable de l'axe des ordonnées ; le texte du cours précise pourtant que le spectre
> « permet de déterminer la valeur absolue de la composante continue (à 0 Hz) ». On la **trace donc
> explicitement** ici, ce qui est plus clair pour l'élève.

## 9. `pc-modulation` — filtrage, modulation, spectre AM

Trois spectres empilés (ou en ligne si la largeur le permet), reliés par deux flèches `solideA`.

1. **Spectre initial** : axes $u$ (V) / $f$ (Hz) ; raie du fondamental $A_1$ à $f_1$, harmoniques
   $A_2, A_3, A_4, \dots$ à $f_2, f_3, f_4, \dots$ d'amplitudes décroissantes (bande bleu clair étiquetée
   « harmoniques ») ; très à droite, raie `solideD` de hauteur $A_p$ à $f_p$, étiquetée « porteuse ».
2. Flèche `solideA` étiquetée **« filtrage »**.
3. **Spectre filtré** : mêmes axes ; seules subsistent les raies à $f_1$, $f_2$, $f_3$ (bande étiquetée
   « harmoniques conservées ») et la porteuse.
4. Flèche `solideA` étiquetée **« modulation »**.
5. **Spectre modulé (AM)** : plus aucune raie près de l'origine ; **cinq** raies groupées autour de $f_p$ —
   la porteuse `solideD` au centre (la plus haute), encadrée symétriquement par $f_p - f_A$, $f_p - f_B$ à
   gauche et $f_p + f_B$, $f_p + f_A$ à droite (amplitudes plus faibles) ; accolade au-dessus, étiquetée
   « bande de fréquences émise ».

Encadré en bas : « transposition de fréquence : le spectre est translaté, sans perte d'information ».

## 10. `pc-spectre-radiofrequence` — bandes de fréquences des télécommunications

Deux règles horizontales superposées encadrant une bande divisée en **7 cases**.

- règle du **haut**, `solideA`, étiquetée « Fréquence » à gauche ; graduations, de gauche à droite :
  300 GHz, 30 GHz, 3 GHz, 300 MHz, 30 MHz, 3 MHz, 300 kHz, 30 kHz ;
- bande centrale, 7 cases, chacune sur deux lignes (nom développé / sigle en gras) :
  extrême haute fréquence **EHF**, super haute fréquence **SHF**, ultra haute fréquence **UHF**,
  très haute fréquence **VHF**, haute fréquence **HF**, moyenne fréquence **MF**, basse fréquence **LF** ;
- règle du **bas**, `solideB`, étiquetée « Longueur d'onde » à droite ; graduations alignées sur celles du
  haut : 1 mm, 1 cm, 10 cm, 1 m, 10 m, 100 m, 1 km, 10 km ;
- au-dessus de la bande, petites étiquettes d'usage reliées à leur case par un trait fin : radar automatique
  (EHF), satellite (SHF), téléphone mobile / DECT / four micro-ondes (UHF), TNT (VHF), radio AM et FM (MF) ;
- rappel de la formule en haut à droite : $\lambda = \dfrac{c}{f}$ avec $c = 3{,}00 \times 10^{8}$ m·s⁻¹.

---

## Récapitulatif des usages

| Figure | Leçon | Exercices |
|---|---|---|
| `pc-desintegrations` | `pc-radioactivite.md` | QCM noyau fils du ¹⁴C ; grille rayonnement → particule |
| `pc-decroissance-radioactive` | `pc-radioactivite.md` | QCM fraction restante après $3\,t_{1/2}$ ; intro de l'exercice guidé « datation au carbone 14 » |
| `pc-fission-fusion` | `pc-radioactivite.md` | QCM équilibrage de la fission ; QCM fusion / fission |
| `pc-pile-accumulateur` | `pc-piles-accumulateurs.md` | QCM oxydation à l'anode ; QCM demi-équation en décharge ; grille décharge/recharge |
| `pc-pile-combustible` | `pc-piles-accumulateurs.md` | QCM réactifs de la pile à combustible |
| `pc-echelle-ph` | `pc-acido-basique.md` | QCM pH = 9,2 ; grille acide/neutre/basique |
| `pc-dilution-ph` | `pc-acido-basique.md` | QCM dilution ×10 ; QCM encadrement du pH après dilution |
| `pc-spectre-signal` | `pc-signaux-spectres.md` | QCM son pur ; saisie du rang d'un harmonique |
| `pc-modulation` | `pc-signaux-spectres.md` | QCM modulation FM ; ordre « chaîne de transmission » ; QCM cinq raies en AM |
| `pc-spectre-radiofrequence` | `pc-signaux-spectres.md` | grille bandes ↔ longueurs d'onde ; QCM taille d'antenne à 900 MHz |
