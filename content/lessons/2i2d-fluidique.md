# Énergie fluidique : schémas, vérins et pompes

## Le schéma fluidique

Le **schéma fluidique** est une **représentation structurelle** du système : il montre les
constituants et représente, de façon simplifiée, le **transport du fluide**. On l'utilise en
**pneumatique** (fluide : air comprimé, quelques bars, compressible) et en **hydraulique**
(fluide : huile, souvent 100 à 300 bars, pratiquement incompressible). Les composants sont dessinés
avec des **symboles normalisés**, jamais avec leur forme réelle.

{{fig:2i2d-circuit-hydraulique}}

| Composant | Fonction |
|---|---|
| **Vérin double effet** | convertir une puissance hydraulique (débit, pression) en puissance mécanique (force, vitesse de translation) |
| **Distributeur piloté électriquement** | aiguiller le fluide vers une voie ou vers l'autre |
| **Moteur électrique et pompe** | faire circuler le fluide dans le circuit |
| **Filtre** | éliminer les particules solides du fluide |
| **Accumulateur** | stocker du fluide ; limiter les à-coups |
| **Manomètre** | lire la valeur de la pression |
| **Clapet anti-retour** | ne laisser passer le fluide que dans un seul sens |
| **Vanne** / **électrovanne** | stopper ou laisser passer le fluide (l'électrovanne est pilotée électriquement) |
| **Réducteur de débit** | réduire le débit, donc la vitesse de la tige d'un vérin |

Dans la **chaîne d'énergie**, la pompe et le vérin remplissent la fonction **Convertir**, le
distributeur la fonction **Distribuer**, et le vérin agit ensuite sur la matière d'œuvre.

## Le vérin double effet

Le corps du vérin est alimenté par **deux orifices** : le fluide poussant d'un côté fait **sortir**
la tige, de l'autre il la fait **rentrer**. Les deux mouvements sont donc motorisés (le vérin
simple effet, lui, ne l'est que dans un sens, le retour étant assuré par un ressort).

{{fig:2i2d-verin-double-effet}}

$$F = p \times S \qquad Q = S \times V \qquad P = Q \times p = F \times V$$

avec $F$ la force en newtons (N), $p$ la pression en pascals (Pa), $S$ la section du piston en m²,
$Q$ le débit en m³·s⁻¹, $V$ la vitesse de la tige en m·s⁻¹ et $P$ la puissance en watts (W).

Conversions à connaître : $1$ bar $= 10^{5}$ Pa ; $1$ cm² $= 10^{-4}$ m² ;
$1$ L·min⁻¹ $= \dfrac{10^{-3}}{60} \approx 1{,}67 \times 10^{-5}$ m³·s⁻¹.

*Exemple* : un vérin de section $S = 20$ cm² $= 2{,}0 \times 10^{-3}$ m², alimenté sous
$p = 60$ bar $= 6{,}0 \times 10^{6}$ Pa, développe
$F = 6{,}0 \times 10^{6} \times 2{,}0 \times 10^{-3} = 12\,000$ N. S'il sort à $V = 0{,}10$ m·s⁻¹,
il consomme $Q = 2{,}0 \times 10^{-3} \times 0{,}10 = 2{,}0 \times 10^{-4}$ m³·s⁻¹, soit
**12 L·min⁻¹**, et la puissance hydraulique vaut
$P = 2{,}0 \times 10^{-4} \times 6{,}0 \times 10^{6} = 1\,200$ W — exactement $F \times V$.

**Effet de la section annulaire** : côté tige, la surface utile est amputée de la section de la
tige. À pression égale, la force de **rentrée** est donc plus **faible** que la force de sortie, et
la tige rentre plus **vite** qu'elle ne sort à débit égal.

## Régler la vitesse d'un vérin

La vitesse de la tige ne dépend que du **débit** : $V = Q / S$. Pour ralentir un mouvement, on
place donc un **réducteur de débit** sur le circuit — et non un manomètre, qui ne fait que mesurer,
ni une vanne, qui ne fait qu'ouvrir ou fermer. Pour un vérin de course $c$, la durée d'une sortie
vaut $t = c / V$ : la même course de 400 mm à $0{,}10$ m·s⁻¹ demande $4{,}0$ s.

## Pression, force et sections

Un circuit hydraulique transmet la pression dans tout le fluide, ce qui permet de **démultiplier
une force** en changeant de section — c'est le principe de la presse hydraulique.

{{fig:pc-presse-hydraulique}}

C'est aussi la raison pour laquelle l'hydraulique équipe les engins de forte puissance : à
puissance égale, une pression dix fois plus élevée qu'en pneumatique permet des vérins dix fois
moins gros.
