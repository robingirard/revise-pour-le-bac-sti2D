# Chaîne de puissance et rendements

La **chaîne d'énergie** (ou chaîne de puissance) décrit comment l'énergie est distribuée, convertie et transmise pour réaliser une action.

## Les cinq fonctions

{{fig:2i2d-chaine-puissance}}

**ALIMENTER → DISTRIBUER → CONVERTIR → TRANSMETTRE → AGIR**

| Fonction | Composants types |
|---|---|
| Alimenter | Batterie, pile, réseau électrique, réservoir |
| Distribuer | Contacteur, relais, transistor, distributeur pneumatique |
| Convertir | Moteur électrique, pompe, vérin |
| Transmettre | Engrenages, poulies-courroie, pignon-crémaillère |
| Agir | Roue, chenille, pince, ventouse |

Les **ordres** venus de la chaîne d'information arrivent sur le bloc **DISTRIBUER** : c'est le préactionneur qui laisse ou non passer la puissance.

{{fig:info-chaine-information}}

## Effort et flux : la puissance sur un lien

Sur chaque lien de puissance circulent deux grandeurs : une grandeur d'**effort** et une grandeur de **flux**. Leur produit est une **puissance**, en watts.

| Domaine | Effort | Flux | Puissance |
|---|---|---|---|
| Électrique (continu) | Tension $U$ (V) | Intensité $I$ (A) | $P = U \times I$ |
| Mécanique (translation) | Force $F$ (N) | Vitesse $V$ (m·s⁻¹) | $P = F \times V$ |
| Mécanique (rotation) | Couple $C$ (N·m) | Vitesse angulaire $\omega$ (rad·s⁻¹) | $P = C \times \omega$ |
| Hydraulique | Pression $p$ (Pa) | Débit $Q$ (m³·s⁻¹) | $P = p \times Q$ |

*Attention* : $\omega$ est une **vitesse angulaire** en rad·s⁻¹ (on l'appelle parfois « fréquence de rotation »). On rencontre aussi une ligne « thermique » avec un flux en W·K⁻¹ : cette grandeur est un flux d'**entropie**, pas un flux thermique — un flux thermique est une puissance, en watts.

## Rendement d'un maillon

{{fig:pc-bilan-convertisseur}}

Un système reçoit une énergie $E_e$, en restitue une part utile $E_s$ et en dissipe le reste sous forme dégradée (chaleur, bruit) : $E_p = E_e - E_s$.

$$\eta = \frac{P_{\text{sortie}}}{P_{\text{entrée}}} = \frac{E_{\text{sortie}}}{E_{\text{entrée}}}$$

Le rendement est **sans unité**, compris entre 0 et 1 (souvent exprimé en pourcentage). La valeur 1 est la meilleure possible, inatteignable en pratique.

## Rendements en cascade

{{fig:2i2d-rendements-cascade}}

La sortie d'un maillon est l'entrée du suivant : les rendements se **multiplient**.

$$\eta_{\text{global}} = \eta_1 \times \eta_2 \times \dots \times \eta_n$$

**Exemple** — hacheur $\eta_1 = 0{,}95$ puis moteur $\eta_2 = 0{,}85$ : $\eta_{\text{global}} = 0{,}95 \times 0{,}85 = 0{,}8075$, soit environ 81 %. À partir de 336 W électriques, la roue reçoit $336 \times 0{,}8075 = 271{,}3$ W.

Deux erreurs à ne jamais commettre : **additionner** les rendements, ou en faire la **moyenne**. Quatre maillons « à 90 % » donnent $0{,}90^4 = 0{,}66$, et non 0,90.

## Descendre ou remonter une chaîne

- On **descend** la chaîne (de la source vers l'action) en **multipliant** : $P_{\text{sortie}} = P_{\text{entrée}} \times \eta$.
- On **remonte** la chaîne (de l'action vers la source) en **divisant** : $P_{\text{entrée}} = \dfrac{P_{\text{sortie}}}{\eta}$.

**Exemple** — le trolleybus consomme $2{,}7$ kWh·km⁻¹, soit $2{,}7 \times 3{,}6 = 9{,}72$ MJ·km⁻¹. En remontant la distribution ($\eta = 0{,}97$) puis l'acheminement ($\eta = 0{,}95$) : $9{,}7 / 0{,}97 = 10{,}0$ puis $10{,}0 / 0{,}95 = 10{,}5$ MJ·km⁻¹ à produire en sortie de centrale. En remontant encore les rendements de production (nucléaire 0,30, flamme 0,35), on obtient environ **30,9 MJ·km⁻¹ d'énergie primaire**. Si l'on avait multiplié au lieu de diviser, on aurait trouvé moins d'énergie en amont qu'en aval : impossible.
