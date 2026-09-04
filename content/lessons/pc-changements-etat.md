# Changements d'état et bilan énergétique

## Les six changements d'état

| Transformation | Nom | Énergie |
|---|---|---|
| Solide → Liquide | **Fusion** | endothermique ($Q_p > 0$) |
| Liquide → Solide | **Solidification** | exothermique ($Q_p < 0$) |
| Liquide → Gaz | **Vaporisation** | endothermique |
| Gaz → Liquide | **Condensation (liquéfaction)** | exothermique |
| Solide → Gaz | **Sublimation** | endothermique |
| Gaz → Solide | **Condensation** | exothermique |

*Piège de vocabulaire* : le livre emploie le mot « condensation » pour **deux** transformations différentes (gaz → liquide et gaz → solide) ; précisez toujours l'état d'arrivée.

{{fig:pc-etats-matiere}}

## Ce qui change, ce qui ne change pas

- **La masse se conserve** : le nombre d'entités chimiques ne varie pas.
- **Pour un corps pur, la température demeure constante** : on observe un **palier de température**.
- À l'échelle microscopique, seule l'**énergie potentielle** varie (rupture ou création de liaisons) ; l'**agitation thermique ne varie pas**, puisque la température reste constante.

Pour l'eau : fusion à **0 °C**, ébullition à **100 °C** sous pression atmosphérique normale. Pour le mercure : **−39 °C** et **357 °C**.

## Énergie échangée pendant un changement d'état

$$Q_p = m \times L$$

$Q_p$ en joule (J), $m$ en kilogramme (kg) et $L$, l'**énergie massique de changement d'état**, en J·kg⁻¹. $Q_p$ est **positive** quand le corps pur **reçoit** de l'énergie (transformation **endothermique**, état final plus désordonné) et **négative** quand il en **cède** (**exothermique**, état final plus ordonné). On en déduit les autres valeurs : $L_{\text{solidification}} = -\,L_{\text{fusion}}$.

| Eau pure | Fusion | Vaporisation | Sublimation |
|---|---|---|---|
| $\theta$ (°C) | 0 | 100 | 0 |
| $L$ (kJ·kg⁻¹) | 334 | $2{,}26 \times 10^{3}$ | $2{,}83 \times 10^{3}$ |

*Esprit critique* : $334 + 2\,260 = 2\,594 \neq 2\,830$. Ces trois valeurs ne sont pas données à la même température (l'énergie de vaporisation vaut environ 2 500 kJ·kg⁻¹ à 0 °C, contre 2 260 kJ·kg⁻¹ à 100 °C) : elles ne sont donc pas mutuellement cohérentes.

## La courbe de chauffage d'un corps pur

{{fig:pc-courbe-chauffage-eau}}

| Étape | Description | Formule |
|---|---|---|
| ❶ | échauffement du **solide** | $Q_1 = m\,c_{\text{solide}}\,(\theta_{\text{Fusion}} - \theta_1)$ |
| ❷ | **palier** de fusion | $Q_2 = m\,L_{\text{Fusion}}$ |
| ❸ | échauffement du **liquide** | $Q_3 = m\,c_{\text{liquide}}\,(\theta_{\text{Ébullition}} - \theta_{\text{Fusion}})$ |
| ❹ | **palier** d'ébullition | $Q_4 = m\,L_{\text{Vaporisation}}$ |
| ❺ | échauffement du **gaz** | $Q_5 = m\,c_{\text{gaz}}\,(\theta_2 - \theta_{\text{Ébullition}})$ |

**Méthode du bilan** : tant que l'état physique **n'est pas modifié**, utiliser $Q = m \times c \times \Delta\theta$ ; **pendant** un changement d'état, utiliser $Q_p = m \times L$ ; puis additionner $Q = Q_1 + Q_2 + Q_3 + Q_4 + Q_5$.

**Exemple** (1,0 kg de glace de −20 °C à 120 °C) : $Q_1 = 42$ ; $Q_2 = 334$ ; $Q_3 = 420$ ; $Q_4 = 2\,260$ ; $Q_5 = 40$ (en kJ), soit $Q = 3\,096$ kJ ≈ 3,10 MJ. Les deux changements d'état représentent à eux seuls **84 %** du total : les oublier est l'erreur la plus coûteuse d'un bilan énergétique.
