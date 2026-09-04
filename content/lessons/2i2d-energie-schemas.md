# Schémas électriques et composants

Un schéma électrique représente les composants d'une installation et leurs liaisons. Il ne dessine pas les objets : il utilise des **symboles normalisés**, les mêmes pour tous les bureaux d'études.

## Les symboles à reconnaître

{{fig:2i2d-symboles-electriques}}

| Symbole | Composant | Fonction |
|---|---|---|
| Traits longs et courts alternés, $+$ en haut | Pack batterie | Alimenter en courant continu |
| Deux cercles sécants | Transformateur | Modifier la tension d'alimentation |
| Cercle avec `M` et `~` | Moteur électrique | Convertir l'électricité en rotation |
| Cercle barré d'une croix | Lampe | Convertir l'électricité en lumière |
| Triangle et barre, deux flèches | DEL (LED) | Émettre de la lumière |
| Cercle avec `B`, `C`, `E` | Transistor | Interrupteur commandé électroniquement |
| Rectangle sur un fil | Résistance | S'opposer au passage du courant |

Le rectangle est la **norme européenne** de la résistance ; le zigzag est la norme américaine. Les deux désignent le même composant.

## Les organes de protection

- **Interrupteur sectionneur à fusible** : en cas de court-circuit ou de surcharge, le fusible **fond** et ouvre le circuit. Il est à usage unique.
- **Disjoncteur sectionneur magnéto-thermique** : un bilame détecte les **surcharges** (effet thermique), une bobine détecte les **courts-circuits** (effet magnétique).
- **Disjoncteur différentiel** : il compare le courant entrant et le courant sortant. Dès que leur **différence** atteint sa sensibilité (30 mA en logement), il s'ouvre.
- **Bouton d'arrêt d'urgence** : contact **fermé au repos** qui s'ouvre à l'appui sur la tête « coup de poing ».

*Règle à retenir* : **différentiel → protège les personnes** ; **fusible et magnéto-thermique → protègent le matériel**. Les deux familles sont exigées dans une installation.

## Les convertisseurs d'énergie

Chaque convertisseur se dessine par un **carré barré d'une diagonale** : la grandeur d'entrée en haut à gauche, la grandeur de sortie en bas à droite (`=` continu, `~` alternatif).

{{fig:2i2d-convertisseurs}}

| Convertisseur | Conversion | Exemple d'emploi |
|---|---|---|
| Onduleur | `=` → `~` | Réinjecter la production photovoltaïque sur le réseau |
| Redresseur | `~` → `=` | Charger une batterie depuis une prise du réseau |
| Hacheur | `=` → `=` | Faire varier la vitesse d'un moteur à courant continu alimenté par batterie |
| Variateur (gradateur) | `~` → `~` | Faire varier fréquence et tension d'un moteur alternatif |

Un **transformateur** n'est pas un convertisseur de ce tableau : il modifie une tension **alternative** et ne fonctionne pas en continu.

## Lire un schéma de puissance et de commande

{{fig:2i2d-demarrage-direct}}

Le démarrage direct d'un moteur triphasé se lit sur **deux circuits séparés**.

- **Circuit de puissance** (fortes intensités) : réseau $3 \times 400$ V → sectionneur porte-fusibles `Q0` (fusibles `F1`) → contacts du contacteur `KM1` → relais thermique `F4` → moteur `M3`.
- **Circuit de commande** (très basse tension) : fusible `F2` → transformateur `T1` (400 V / 24 V, 50 V·A) → fusible `F3` → contact `F4` → bouton d'arrêt `S2` → bouton de marche `S1`, en parallèle avec le contact d'**auto-maintien** `KM1` → bobine `KM1`.

Fonctionnement :

- pour démarrer, il faut `Q0` fermé **et** un appui sur `S1` ;
- si l'on relâche `S1`, le contact d'auto-maintien `KM1`, fermé au démarrage, maintient la bobine alimentée : le moteur **continue de tourner** ;
- pour arrêter, on appuie sur `S2`, qui ouvre la boucle.

La commande est alimentée en **24 V** pour deux raisons : la sécurité de l'opérateur qui manœuvre les boutons, et l'isolation galvanique apportée par `T1`. La mention **50 V·A** de ce transformateur est sa puissance apparente admissible : au secondaire, $I_2 \le \dfrac{50}{24} \approx 2{,}08$ A.
