# Transformer un mouvement

Un mécanisme de **transformation** change la nature du mouvement : rotation ↔ translation.

## Le pignon-crémaillère

{{fig:transformation-pignon-cremaillere}}

Le **pignon** (roue dentée) roule sans glisser sur la **crémaillère** (tige dentée). Le cercle primitif du pignon parcourt sur la crémaillère :

**d = r × θ** (d en m, r = rayon primitif en m, θ en **rad**) et **V = r × ω** (V en m/s, ω en rad/s).

**Réversible** : le pignon peut entraîner la crémaillère et inversement (direction assistée, portail coulissant).

## Le système vis-écrou

{{fig:transformation-vis-ecrou}}

Un tour de vis fait avancer l'écrou d'un **pas** p :

**d = p × n** (d en mm, p = pas en mm/tour, n = nombre de tours).

En général **irréversible** : l'écrou ne peut pas faire tourner la vis (serre-joint, étau, cric à vis).
Attention aux unités : ici l'angle est en **tours** et les longueurs en **mm**.

## Le système bielle-manivelle

{{fig:transformation-bielle-manivelle}}

La **manivelle** tourne en continu, la **bielle** (deux articulations) transforme cette rotation en **translation alternative**
du piston, et réciproquement : **réversible** (moteur thermique : le piston entraîne le vilebrequin ; pompe : le moteur entraîne le piston).
La course du piston vaut **deux fois le rayon** de la manivelle.

## À retenir

| Mécanisme | Transformation | Loi entrée/sortie | Réversible ? |
|---|---|---|---|
| Pignon-crémaillère | rotation ↔ translation | d = r × θ ; V = r × ω | oui |
| Vis-écrou | rotation → translation | d = p × n | non, en général |
| Bielle-manivelle | rotation continue ↔ translation alternative | course = 2 × rayon | oui |
