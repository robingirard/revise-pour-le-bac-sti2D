# Gestion et stockage de l'énergie

## Pourquoi stocker

La production solaire est **intermittente** : elle est concentrée sur quelques heures et varie du simple au quadruple entre janvier et juin. Le besoin, lui, suit les horaires de service. Le stockage **découple production et consommation dans le temps**. Il ne crée aucune énergie et ajoute même ses propres pertes (charge puis décharge).

## Architecture d'une alimentation autonome

{{fig:2i2d-alimentation-ferry}}

Sur le ferry-boat de Marseille, l'alimentation électrique associe :

| Élément | Fonction | Nature de la tension |
|---|---|---|
| 16 panneaux « propulsion », 8 panneaux « service » | Produire | Continue |
| Chargeur de propulsion | Régler tension et courant de charge | Sortie continue |
| Prise de quai | Recharger complètement la nuit | **Alternative** (réseau) |
| Deux parcs de batteries 384 V | Stocker et alimenter la propulsion | Continue |
| Battery Management System (BMS) | Mesurer $U$, $I$, température ; commander les ventilateurs ; dialoguer avec le chargeur | Signaux (bus CAN) |

Savoir repérer les frontières **continu / alternatif** sur un tel diagramme est un exercice classique : seule la prise de quai est en alternatif, tout le reste de la chaîne est en continu.

Le BMS est la **chaîne d'information du stockage** : il acquiert (mesures), traite (calcul du SoC, seuils) et communique (consignes, commande de ventilation). Sans lui, aucune limite de profondeur de décharge ne pourrait être tenue.

## Taux de couverture

$$\text{taux de couverture} = \frac{\text{production}}{\text{besoin}}$$

Sur le ferry, le besoin journalier en mode écoconduite vaut 22 752 Wh en hiver (8 h de service), 28 440 Wh au printemps et à l'automne (10 h) et 51 192 Wh en été (18 h). Face à une production solaire de 4,3 à 18,3 kWh/jour, le taux de couverture varie de **19 % en janvier à environ 36 % en juin**.

{{fig:2i2d-ferry-bilan}}

Conclusion : les panneaux sont un **appoint**, jamais une source d'autonomie. La recharge nocturne sur la prise de quai reste indispensable toute l'année.

## Arbitrer entre consommation, stockage et durée de vie

{{fig:2i2d-cycles-dod}}

La profondeur de décharge quotidienne se calcule en rapportant l'énergie prélevée à la capacité installée (104 448 Wh pour le ferry) :

| Situation (été, 18 h de service) | Énergie prélevée | DoD | Cycles |
|---|---|---|---|
| Sans écoconduite, sans solaire | 73 008 Wh | 70 % | ≈ 1 450 |
| Avec écoconduite | 51 192 Wh | 49 % | ≈ 2 400 |
| Avec écoconduite et solaire (17,9 kWh) | 33 292 Wh | 32 % | ≈ 4 400 |

L'écoconduite **double** la durée de vie du stockage, l'appoint solaire la **triple** — sans ajouter un seul élément de batterie. C'est le principe même de l'écoconception : *l'énergie la moins polluante est celle qu'on ne consomme pas*.

## Mesurer l'impact

Deux indicateurs reviennent systématiquement au bac.

**Émissions du kWh électrique.** Le suivi mensuel EDF 2024 donne 48, 54, 57, 41, 23, 19, 40, 34, 47, 50, 46 et 34 g Eq CO₂/kWh, soit une moyenne de $493/12 = 41$ g Eq CO₂/kWh. Les 4 400 kWh économisés chaque année par le solaire évitent donc $4\,400 \times 41{,}08 = 180\,767$ g, soit environ **181 kg de CO₂ par an**. Le gain est modeste parce que le mix français est déjà peu carboné : le même calcul dans un pays au mix charbonné donnerait dix fois plus.

**Émissions par passager.** Rapporter l'émission kilométrique au nombre de places change complètement le classement :

| Véhicule | g Eq CO₂/km | Places | Par passager |
|---|---|---|---|
| Trolleybus CRISTALIS | 92 | 96 | 0,96 |
| Autobus CITELIS | 1 409 | 105 | 13,4 |
| Voiture particulière | 127 | 5 | 25,4 |

Mais un véhicule n'est jamais plein : avec le remplissage moyen réel de **1,3 passager**, la voiture émet $127/1{,}3 = 97{,}7$ g Eq CO₂ par km et par passager, et l'autobus ne devient plus performant qu'**à partir de 15 passagers**. Un indicateur unique ne suffit jamais à conclure : il faut croiser gaz à effet de serre, ressources non renouvelables, pollution locale et énergie primaire.
