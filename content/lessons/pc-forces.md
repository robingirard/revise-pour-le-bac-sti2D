# Forces, poids et principe d'inertie

*Prérequis : la compétence **Mouvements et trajectoires** (référentiel, centre de masse, trajectoire rectiligne, circulaire ou curviligne).*

## Modéliser une action mécanique

Toute **action mécanique** exercée sur un système est modélisée par un **vecteur force**, défini — comme tout vecteur — par quatre caractéristiques :

- son **point d'application** (le centre de masse pour une force à distance) ;
- sa **direction** ;
- son **sens** ;
- sa **norme**, exprimée en **newton (N)**.

## Le poids

$$P = m \times g$$

| Grandeur | Signification | Unité |
|---|---|---|
| $P$ | norme du poids | newton (N) |
| $m$ | masse du système | kilogramme (kg) |
| $g$ | intensité de la pesanteur | $\mathrm{N\cdot kg^{-1}}$ (ou $\mathrm{m\cdot s^{-2}}$) |

Dans toute l'unité on prend **$g = 9{,}81\ \mathrm{N\cdot kg^{-1}}$**. *(Le manuel écrit tantôt $9{,}8$, tantôt $9{,}81$ ; l'écart est inférieur à 0,2 %.)*

**Ne jamais confondre** la **masse** (en kg, elle ne change pas) et le **poids** (en N, il dépend de $g$).

## Bilan des forces sur un livre posé sur une table

{{fig:pc-bilan-forces-livre}}

| Force | Point d'application | Direction | Sens | Norme |
|---|---|---|---|---|
| Poids $\vec{P}$ | centre de masse | verticale | vers le bas | $P = m\,g$ |
| Réaction $\vec{R}$ de la table | barycentre de la surface de contact | verticale | vers le haut | $R$ |

## Les frottements

Toute **force de frottement s'oppose au mouvement** : elle a la **même direction que le vecteur vitesse**, mais un **sens opposé**.

- **Entre deux solides** : deux choses la fixent — la **nature des deux surfaces** qui se touchent et l'**étendue de leur zone de contact**.
- **Entre un fluide et un solide** : sa valeur dépend de la **viscosité $\eta$** du fluide, ainsi que de la forme, de la vitesse et de l'état de surface du solide. À **faible** vitesse $f = k\,v$ ; à vitesse **élevée** $f = k\,v^2$.

## Projeter un vecteur force sur les axes

{{fig:pc-projection-force}}

$$\vec{T} = T_x\,\vec{\imath} + T_y\,\vec{\jmath} = T\cos\theta\,\vec{\imath} + T\sin\theta\,\vec{\jmath}$$

$T$ en N, $\theta$ = angle entre $\vec{T}$ et l'axe des abscisses. Piège classique : prendre le sinus pour $T_x$.

## Le principe d'inertie

Un système mécanique est **soit immobile, soit animé d'un mouvement rectiligne uniforme** si la somme vectorielle des forces extérieures qui lui sont appliquées est égale au vecteur nul :

$$\sum \overrightarrow{F_{\text{ext}}} = \vec{0}$$

{{fig:pc-bilan-forces-plan-incline}}

Une caisse qui glisse **à vitesse constante** sur un plan incliné est donc en équilibre : poids, **réaction normale** au plan et **force de frottement** se compensent.

## Méthode : faire un bilan des forces

1. définir le **système** étudié et le **référentiel** ;
2. inventorier **toutes** les forces extérieures appliquées ;
3. donner les **quatre caractéristiques** de chacune ;
4. tracer les vecteurs à leur point d'application ;
5. conclure avec le **principe d'inertie** : la somme est-elle nulle ou non ?
