# Introduction à la notion d'onde

## Deux familles d'ondes

- les **ondes mécaniques** (son, ultrasons, ondes sismiques, vagues) **ont besoin d'un milieu matériel de propagation** : elles ne se propagent pas dans le vide ;
- les **ondes électromagnétiques** (lumière, ondes radio, rayons X) se propagent dans la matière **comme dans le vide**.

**À retenir** : la propagation d'une onde s'accompagne d'un **transfert d'énergie sans déplacement de matière**. La **vitesse de propagation**, appelée **célérité**, dépend de la **nature** de l'onde et du **milieu de propagation**.

{{fig:pc-onde-longitudinale-transversale}}

Selon la direction de la perturbation par rapport à la direction de propagation, l'onde est :

- **longitudinale** si la perturbation est **parallèle** à la direction de propagation (compression d'un ressort, son) ;
- **transversale** si elle lui est **perpendiculaire** (corde que l'on secoue, vague).

## La double périodicité

{{fig:pc-onde-periode-longueur}}

- **périodicité spatiale** : la **longueur d'onde** $\lambda$, distance entre deux motifs identiques à un instant donné ;
- **périodicité temporelle** : la **période** $T$, durée entre deux motifs identiques en un point donné.

$$\lambda = v \times T = \frac{v}{f} \qquad\text{avec}\qquad f = \frac{1}{T}$$

| Grandeur | Signification | Unité |
|---|---|---|
| $\lambda$ | longueur d'onde | mètre (m) |
| $v$ (ou $c$ pour la lumière) | célérité | mètre par seconde (m·s⁻¹) |
| $T$ | période | seconde (s) |
| $f$ (noté aussi $\nu$) | fréquence | hertz (Hz) |

Attention : on **divise** par la fréquence, on ne multiplie pas. Le contrôle des unités tranche : $\mathrm{m\cdot s^{-1}} \times \mathrm{s} = \mathrm{m}$ et $\mathrm{m\cdot s^{-1}} / \mathrm{s^{-1}} = \mathrm{m}$, alors que $\mathrm{m\cdot s^{-1}} \times \mathrm{Hz} = \mathrm{m\cdot s^{-2}}$ n'est pas une longueur.

*Notation* : on écrit $f$ pour les ondes et le son, et $\nu$ (lettre grecque « nu ») pour les ondes électromagnétiques. C'est **la même grandeur**, la fréquence en hertz. Ne pas confondre $\nu$ (fréquence) et $v$ (célérité).

## Transmission, réflexion et absorption

{{fig:pc-reflexion-transmission}}

Quand une onde passe d'un milieu **A** à un milieu **B**, son énergie est en partie :

- **réfléchie** dans le milieu A, à la surface de contact entre A et B ;
- **absorbée** dans le milieu B (elle y est dissipée, essentiellement en chaleur) ;
- **transmise** après le milieu B.

$$I = I_r + I_a + I_t$$

L'énergie de l'onde incidente est égale à la **somme** des énergies des ondes réfléchie, absorbée et transmise. En acoustique du bâtiment, l'**isolation** cherche à réduire la part transmise $I_t$, tandis que la **correction acoustique** joue sur les parts réfléchie et absorbée.

## Transmettre une information avec une onde

Pour transmettre une information sur une distance plus ou moins longue, on utilise une **onde électromagnétique** de fréquence adaptée, appelée **onde porteuse**.

**À retenir** : l'onde porteuse est **modulée** (en amplitude, en fréquence, etc.) selon un **code convenu entre l'émetteur et le récepteur**, par un **signal modulant** (voix, musique…). « FM » signifie *modulation de fréquence*.

## Méthode : calculer une longueur d'onde

1. relever la **période** $T$ sur l'enregistrement temporel, entre deux motifs identiques ;
2. en déduire la **fréquence** $f = 1/T$, en hertz ;
3. relever la **célérité** $v$ de l'onde dans le milieu, en m·s⁻¹ ;
4. calculer $\lambda = v \times T = v/f$ ;
5. **vérifier l'unité** : $\lambda$ doit s'exprimer en mètre.
