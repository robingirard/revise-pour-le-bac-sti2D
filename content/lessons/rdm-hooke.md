# Loi de Hooke et dimensionnement

## Déformation élastique, déformation plastique

Quand on charge une pièce, elle commence par se déformer de manière **réversible** : c'est la **déformation
élastique**, la pièce reprend sa forme initiale dès que la sollicitation cesse. Si l'on augmente la charge,
un matériau **ductile** se déforme de manière **définitive** : c'est la **déformation plastique**. Un
matériau **fragile**, lui, casse sans passer par là.

**À retenir** : la longévité et le bon fonctionnement des mécanismes imposent que les pièces restent dans le
**domaine élastique**.

## L'essai de traction

{{fig:rdm-essai-traction}}

On tire sur une éprouvette et on trace la **contrainte** $\sigma = F/S$ en fonction de la **déformation**
(l'allongement relatif) $\varepsilon = \Delta L / L$. La courbe obtenue donne trois informations :

- la partie **linéaire** de départ : c'est le domaine élastique. Sa **pente** est le **module d'élasticité
  longitudinale** $E$, ou **module de Young**. Plus $E$ est grand, plus le matériau est **rigide** ;
- la **limite élastique** $R_e$ : fin du domaine élastique. Au-delà, la pièce se déforme plastiquement ;
- la **limite à la rupture** $R_r$ : contrainte maximale atteinte au cours de l'essai, avant la rupture.

Ordres de grandeur : $E_{\text{acier}} = 200\,000$ N/mm², $E_{\text{caoutchouc}} = 7{,}5$ N/mm².

## La loi de Hooke

Dans le domaine élastique, contrainte et déformation sont proportionnelles :

$\sigma = E \times \varepsilon$, avec $\sigma = \dfrac{F}{S}$ et $\varepsilon = \dfrac{\Delta L}{L}$.

| Grandeur | Signification | Unité |
|---|---|---|
| $\sigma$ | contrainte | N/mm² (MPa) |
| $E$ | module de Young | N/mm² (MPa) |
| $\varepsilon$ | allongement relatif | **sans unité** |
| $\Delta L$ | allongement | mm |
| $L$ | longueur initiale | mm |

Méthode : $\varepsilon = \sigma / E$, puis $\Delta L = \varepsilon \times L$. Ne pas confondre $\varepsilon$
(un rapport, sans unité, souvent de l'ordre de $10^{-3}$) et $\Delta L$ (une longueur, en mm).

## La condition de résistance

La contrainte maximale ne doit pas dépasser la limite élastique : $\sigma_{\max} \leq R_e$.

Pour couvrir les incertitudes (matériau, modèle, valeur réelle des efforts, vieillissement), on applique un
**coefficient de sécurité** $s > 1$ :

$\sigma_{\max} \leq \dfrac{R_e}{s}$, et réciproquement $s = \dfrac{R_e}{\sigma_{\max}}$.

Le coefficient de sécurité est **sans unité**. S'il vaut moins de 1, la pièce est déjà plastifiée.

## Dimensionner une pièce en traction

1. calculer l'effort $N$ dans la pièce (PFS) ;
2. calculer la **contrainte admissible** $\sigma_{\text{adm}} = R_e / s$ ;
3. en déduire la **section minimale** $S_{\min} = N / \sigma_{\text{adm}}$ ;
4. pour une section circulaire, le diamètre minimal : $d_{\min} = \sqrt{\dfrac{4 S_{\min}}{\pi}}$ ;
5. choisir la valeur normalisée immédiatement **supérieure**.

Quand la géométrie est complexe, la contrainte n'est plus uniforme : on utilise alors une **modélisation par
éléments finis** pour trouver les zones et les valeurs des contraintes maximales.

## À retenir

| Grandeur | Formule | Unité |
|---|---|---|
| Loi de Hooke | $\sigma = E \times \varepsilon$ | MPa |
| Allongement relatif | $\varepsilon = \Delta L / L$ | sans unité |
| Allongement | $\Delta L = \varepsilon \times L$ | mm |
| Coefficient de sécurité | $s = R_e / \sigma_{\max}$ | sans unité |
| Section minimale | $S_{\min} = N \times s / R_e$ | mm² |
