# Chaînes fonctionnelles : information et puissance

Pour analyser les flux d'**énergie** et d'**information** qui traversent un système, on le
représente par ses deux **chaînes fonctionnelles**. La chaîne d'information envoie des **ordres** à
la chaîne d'énergie, qui réalise l'**ACTION** sur la matière d'œuvre.

{{fig:2i2d-chaines-fonctionnelles}}

La chaîne d'information reçoit des *informations* et des *consignes*, et délivre des *messages*
vers l'utilisateur ; l'ACTION transforme la **matière d'œuvre entrante** en **matière d'œuvre
sortante**, avec une flèche « Pertes » qui rappelle qu'aucune conversion n'est parfaite.

## La chaîne d'énergie (ou chaîne de puissance)

Elle décrit la façon dont l'énergie est **distribuée, convertie et transmise** aux différents
composants pour réaliser une action.

**Alimenter → Distribuer → Convertir → Transmettre → Agir**

{{fig:2i2d-chaine-energie}}

| Fonction | Composants |
|---|---|
| Alimenter | batterie, pile, réseau électrique, réservoir |
| Distribuer | transistor, distributeur pneumatique, contacteur, relais |
| Convertir | moteur électrique, pompe, vérin pneumatique, compresseur |
| Transmettre | engrenages, poulies-courroie, roue et vis sans fin, pignon-crémaillère |
| Agir | ventouse, roue, chenille, pince |

Point de vigilance : les **ordres** venus de la chaîne d'information arrivent sur le bloc
**Distribuer** — c'est lui qui laisse passer, ou non, l'énergie fournie par *Alimenter*.

## La chaîne d'information

Elle décrit la façon dont les informations issues du système ou de l'extérieur sont **acquises,
traitées et communiquées**, sous forme d'ordres vers la chaîne d'énergie ou d'informations vers
l'utilisateur.

**Acquérir → Traiter → Communiquer**

{{fig:info-chaine-information}}

Entre deux blocs, on précise le **type d'information** : logique, analogique ou numérique.
Sur le pont transbordeur : un *capteur de fin de course* acquiert, une *carte électronique*
traite, des *voyants du pupitre* communiquent ; l'ordre produit agit sur la *carte de puissance*,
qui remplit la fonction **Distribuer**.

## Grandeurs de flux et grandeurs d'effort

Sur un lien de puissance, on précise deux grandeurs : une **grandeur de flux** (ce qui « coule »)
et une **grandeur d'effort** (ce qui « pousse »). Leur **produit** est la puissance échangée, en
watts (W).

{{fig:2i2d-flux-effort}}

| Domaine | Grandeur de flux | Grandeur d'effort | Puissance |
|---|---|---|---|
| Électrique (courant continu) | intensité $I$ (A) | tension $U$ (V) | $P = U \times I$ |
| Mécanique — translation | vitesse $V$ (m·s⁻¹) | force $F$ (N) | $P = F \times V$ |
| Mécanique — rotation | vitesse angulaire $\omega$ (rad·s⁻¹) | couple $C$ (N·m) | $P = C \times \omega$ |
| Hydraulique | débit $Q$ (m³·s⁻¹) | pression $p$ (Pa) | $P = Q \times p$ |

On peut aussi porter sur le diagramme les caractéristiques de chaque élément : rapport de
réduction, rendement, vitesse nominale, pas d'un système vis-écrou…

## Rendements

Le **rendement** d'un maillon est le rapport de la puissance qu'il restitue à celle qu'il reçoit :

$$\eta = \frac{P_{\text{sortie}}}{P_{\text{entrée}}} \le 1$$

Les rendements de maillons placés à la suite se **multiplient** :
$\eta = \eta_1 \times \eta_2 \times \eta_3$.

{{fig:2i2d-rendements-cascade}}

*Exemple (chariot du pont transbordeur)* : le moteur absorbe
$P_{\text{élec}} = U \times I = 400 \times 25 = 10\,000$ W ; la roue motrice développe
$C = F \times r = 8\,000 \times 0{,}15 = 1\,200$ N·m à $\omega = 5$ rad·s⁻¹, soit
$P_{\text{méca}} = C \times \omega = 6\,000$ W. Le rendement global vaut
$\eta = 6\,000 / 10\,000 = 0{,}60$, soit **60 %** ; les 4 000 W manquants sont les *pertes*.

## Remonter une chaîne : énergie finale et énergie primaire

Pour connaître l'énergie **primaire** consommée, on **remonte** la chaîne en **divisant** par
chaque rendement. Le trolleybus CRISTALIS consomme $2{,}7$ kWh·km⁻¹, soit
$2{,}7 \times 3{,}6 = 9{,}72$ MJ·km⁻¹. En amont du réseau de distribution
($\eta = 0{,}97$) puis du réseau de transport ($\eta = 0{,}95$), il faut injecter
$9{,}7 / 0{,}97 = 10{,}0$ puis $10{,}0 / 0{,}95 \approx 10{,}5$ MJ·km⁻¹.
