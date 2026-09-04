# Choisir un matériau

## Les cinq familles de critères

Le choix d'un matériau ne se réduit jamais à sa résistance. Il croise cinq familles de critères :

- **mécaniques** : limite élastique, masse, dureté, résilience… ;
- **physico-chimiques** : tenue à la corrosion, vieillissement… ;
- **de mise en œuvre** : usinabilité, soudabilité, trempabilité… ;
- **économiques** : prix, disponibilité, expérience industrielle… ;
- **écologiques** : toxicité, empreinte carbone, recyclabilité…

## Le diagramme des indices de performance

{{fig:2i2d-radar-performance}}

Pour comparer plusieurs matériaux, on trace un **diagramme radar** à six axes — résistance à la corrosion,
coulabilité, empreinte carbone, recyclabilité, masse, limite élastique — noté de **0 au centre à 5 vers
l'extérieur** :

| Note | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| | Mauvais | Faible | Médiocre | Acceptable | Bon | Excellent |

L'intérêt du diagramme est de ramener des grandeurs d'unités très différentes à une **note commune**. Il
ne désigne jamais un vainqueur à lui seul : il rend visibles les **compromis**, et c'est le cahier des
charges qui tranche.

## Deux hypothèses de la RDM

- **isotrope** : le matériau a les **mêmes propriétés mécaniques dans toutes les directions**. Ce n'est
  pas vrai du bois ni des composites, dont les propriétés dépendent du sens des fibres ;
- **homogène** : le matériau a la **même composition en tout point**.

Ne pas confondre les deux : l'isotropie concerne les **directions**, l'homogénéité les **points**.

## Ductile ou fragile

{{fig:2i2d-familles-contrainte-deformation}}

Sous charge croissante, un matériau se déforme d'abord de manière **réversible** (déformation
**élastique**). Au-delà de la limite élastique $R_e$ :

- un matériau **ductile** (acier doux, aluminium) se déforme de manière **définitive** — déformation
  **plastique** — avant de rompre. Il « prévient » ;
- un matériau **fragile** (verre, céramique, fonte) casse presque sans déformation préalable.

Attention à ne pas confondre **fragile** et **peu rigide** : la rigidité est la **pente** de la courbe,
c'est-à-dire le module d'élasticité longitudinale $E$. Une céramique est à la fois très rigide et très
fragile. Ordres de grandeur : $E_{\text{acier}} = 200\,000$ N/mm², $E_{\text{caoutchouc}} = 7{,}5$ N/mm².

Le bon fonctionnement des mécanismes impose de rester dans le **domaine élastique** : $\sigma_{\max} \leq R_e$.
Quand la géométrie est complexe, la contrainte n'est plus uniforme et l'on recourt à une **modélisation
par éléments finis** pour localiser les zones et les valeurs des contraintes maximales.

## Comportement thermique

**Dilatation** : $\Delta L = L_0 \times \alpha \times \Delta\theta$, avec $\alpha$ le coefficient de
dilatation linéaire (en °C⁻¹). Pour l'acier, $\alpha = 12 \cdot 10^{-6}$ °C⁻¹ : un rail de 10 m s'allonge
de 4,8 mm pour 40 °C. Une variation de température s'exprime **indifféremment en °C ou en K**.

**Conductivité thermique** $\lambda$ (en W/(m·K)) : la quantité de chaleur qui traverse un mètre
d'épaisseur pour 1 K d'écart entre les faces. Plus $\lambda$ est **faible**, plus le matériau est
**isolant**. Le pouvoir d'isolation vient du matériau, mais aussi de la **forme** : l'air emprisonné dans
un double vitrage isole, alors que l'air qui circule autour d'un radiateur dissipe la chaleur par
convection.

## Cycle de vie et valorisation

{{fig:2i2d-cycle-vie-materiau}}

Chaque étape du cycle de vie a son impact : **extraction** (déforestation pour le bois, carrières pour les
métaux et le verre, plateformes pétrolières pour les plastiques), **transport** et **fabrication**
(émissions de gaz à effet de serre), **utilisation**, puis **fin de vie** (pollution de l'eau, de l'air,
pollution visuelle).

Trois voies de **valorisation** :

- la **réutilisation** : l'objet resert, éventuellement après remplacement de composants ;
- le **recyclage** : le matériau usagé redevient de la matière première (le verre, par exemple) ;
- la **valorisation énergétique** : on brûle le matériau et on récupère la chaleur de combustion.

## À retenir

| Question | Réponse |
|---|---|
| Cinq familles de critères | mécaniques, physico-chimiques, mise en œuvre, économiques, écologiques |
| Diagramme radar | 0 au centre, 5 à l'extérieur |
| Isotrope / homogène | mêmes propriétés selon la direction / même composition en tout point |
| Ductile / fragile | se déforme avant de rompre / casse sans prévenir |
| Dilatation | $\Delta L = L_0 \, \alpha \, \Delta\theta$ |
| $\lambda$ faible | bon isolant thermique |
