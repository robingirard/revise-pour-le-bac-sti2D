# Piles, accumulateurs et piles à combustible

## Un générateur électrochimique, c'est une réaction d'oxydoréduction

Un **générateur électrochimique** convertit de l'énergie **chimique** en énergie **électrique** : deux couples
oxydant/réducteur échangent des électrons **par le circuit extérieur**, entre deux **électrodes**.

| Électrode | Demi-équation | Électrons | Polarité (transformation spontanée) |
|---|---|---|---|
| **anode** | oxydation : $\mathrm{red_1} = \mathrm{ox_1} + n_1\,e^-$ | **quittent** l'anode | borne **négative** ⊖ |
| **cathode** | réduction : $\mathrm{ox_2} + n_2\,e^- = \mathrm{red_2}$ | **arrivent** à la cathode | borne **positive** ⊕ |

{{fig:pc-pile-accumulateur}}

Le **pont salin** assure la **neutralité électrique** de chaque compartiment (il ne transporte pas les
électrons). Le **sens conventionnel du courant** va de la borne **+** vers la borne **−** dans le circuit
extérieur : il est **opposé** au sens de déplacement des électrons. Moyen mnémotechnique :
**anode → oxydation**, **cathode → réduction** — toujours vrai, en décharge comme en recharge.

## Pile (irréversible) ou accumulateur (réversible)

Une transformation est **spontanée** si elle démarre dès que les réactifs sont en présence, et
**irréversible** si elle ne peut avoir lieu que dans un sens : c'est le cas d'une **pile**, qu'on jette. Un
**accumulateur** met en jeu une transformation **réversible** : il se **décharge** spontanément, puis on le
**recharge** en le branchant sur un générateur, ce qui régénère les réactifs disparus.

**Exemple : l'accumulateur au plomb**, $\mathrm{PbO_2} + 4\,\mathrm{H^+} + \mathrm{Pb} \;\rightleftarrows\; 2\,\mathrm{Pb^{2+}} + 2\,\mathrm{H_2O}$ (→ décharge, ← recharge).

| | Décharge | Recharge |
|---|---|---|
| Électrode PbO₂ (borne ⊕) | réduction : $\mathrm{PbO_2} + 4\,\mathrm{H^+} + 2\,e^- = \mathrm{Pb^{2+}} + 2\,\mathrm{H_2O}$ | oxydation : $\mathrm{Pb^{2+}} + 2\,\mathrm{H_2O} = \mathrm{PbO_2} + 4\,\mathrm{H^+} + 2\,e^-$ |
| Électrode Pb (borne ⊖) | oxydation : $\mathrm{Pb} = \mathrm{Pb^{2+}} + 2\,e^-$ | réduction : $\mathrm{Pb^{2+}} + 2\,e^- = \mathrm{Pb}$ |

**Les polarités ⊕ et ⊖ ne changent pas** entre décharge et recharge ; ce qui s'inverse, c'est le **sens de
circulation des électrons**, donc le rôle anode/cathode de chaque électrode.

## La pile à combustible

{{fig:pc-pile-combustible}}

Réactifs : **dihydrogène H₂** et **dioxygène O₂**, couples $\mathrm{O_2}/\mathrm{H_2O}$ et $\mathrm{H^+}/\mathrm{H_2}$ :
cathode ⊕, réduction $\mathrm{O_2} + 4\,\mathrm{H^+} + 4\,e^- = 2\,\mathrm{H_2O}$ ; anode ⊖, oxydation
$\mathrm{H_2} = 2\,\mathrm{H^+} + 2\,e^-$ ; bilan $2\,\mathrm{H_2} + \mathrm{O_2} \rightarrow 2\,\mathrm{H_2O}$.
Le seul produit est de l'**eau**.

## Bilan de matière

Les rapports se lisent **directement dans l'équation** :

- accumulateur au plomb : $n(\mathrm{Pb^{2+}})$ formé $= 2 \times n(\mathrm{PbO_2})$ disparu, et d'après la
  demi-équation $n(e^-)$ échangés $= 2 \times n(\mathrm{PbO_2})$ disparu ;
- pile à combustible : $n(\mathrm{H_2O})$ formée $= n(\mathrm{H_2})$ consommé $= 2 \times n(\mathrm{O_2})$ consommé ;
- pile Daniell ($\mathrm{Cu^{2+}} + \mathrm{Zn} \rightarrow \mathrm{Cu} + \mathrm{Zn^{2+}}$) : $n(\mathrm{Zn^{2+}})$ formé $= n(\mathrm{Cu^{2+}})$ consommé, et $n(e^-) = 2 \times n(\mathrm{Cu^{2+}})$.

## Capacité et énergie stockée

| Grandeur | Relation | Unité |
|---|---|---|
| capacité $Q$ (réserve de charge) | $Q = I \times t$ ($I$ en A, $t$ en h) | ampère-heure (A·h) |
| énergie stockée $E$ | $E = Q \times U$ ($Q$ en A·h, $U$ en V) | wattheure (W·h) |

Ne pas confondre $I$ (en A), un **débit** de charge, et $Q$ (en A·h), une **réserve** : une batterie de
60 A·h qui débite 3,0 A tient $t = Q/I = 20$ h. Conversions : 1 A·h = 3 600 C ; 1 000 mA·h = 1 A·h ;
1 000 W·h = 1 kW·h.
