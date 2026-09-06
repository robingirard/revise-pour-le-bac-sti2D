# La radioactivité

## Noyau, isotopes, désintégration

Un noyau se note $^{A}_{Z}\mathrm{X}$ : $Z$ est le **numéro atomique** (nombre de protons), $A$ le **nombre de
masse** (nombre de nucléons) ; le nombre de neutrons vaut $A - Z$. Deux **isotopes** ont le même $Z$ et des
$A$ différents ($^{12}_{6}\mathrm{C}$ et $^{14}_{6}\mathrm{C}$). Un **noyau père** instable se désintègre en
un **noyau fils** plus stable en émettant un rayonnement. La radioactivité est **naturelle** ou
**artificielle** (dans une centrale, un **neutron lent** est envoyé sur des noyaux d'uranium 235).

## Les trois désintégrations, et le rayonnement γ

{{fig:pc-desintegrations}}

| Type | Particule émise | Exemple |
|---|---|---|
| **α** | noyau d'hélium 4, $^{4}_{2}\mathrm{He}$ | le noyau fils perd 2 protons et 2 neutrons |
| **β⁻** | un **électron** | $^{14}_{6}\mathrm{C} \rightarrow {}^{14}_{7}\mathrm{N} + {}^{0}_{-1}\mathrm{e}$ |
| **β⁺** | un **positron** (positon, antiélectron) | $^{10}_{6}\mathrm{C} \rightarrow {}^{10}_{5}\mathrm{B} + {}^{0}_{+1}\mathrm{e}$ |

Toute équation de désintégration **conserve $A$ et $Z$**. En β⁻, $A$ ne change pas et $Z$ **augmente** de 1 ;
en β⁺, $A$ ne change pas et $Z$ **diminue** de 1. Le **rayonnement γ** n'est pas une désintégration : c'est un
**photon** émis en plus, quand le noyau fils laissé trop excité se désexcite ; $A$ et $Z$ sont inchangés.

## Activité et décroissance

La désintégration **d'un seul** noyau est **aléatoire**, mais une population très nombreuse suit toujours la
**loi de décroissance radioactive** :

$N(t) = N_0\, e^{-\lambda t}$ et $A(t) = A_0\, e^{-\lambda t}$, avec $\lambda = \dfrac{\ln 2}{t_{1/2}} = \dfrac{0{,}693}{t_{1/2}}$

| Grandeur | Signification | Unité |
|---|---|---|
| $N(t)$, $N_0$ | nombre de noyaux père restants, à la date $t$ et à $t = 0$ | sans unité |
| $A(t)$, $A_0$ | **activité** = nombre de désintégrations **par seconde** | becquerel (Bq) |
| $t_{1/2}$ | **demi-vie** : durée au bout de laquelle la population est **divisée par deux** | s, an… |
| $\lambda$ | constante radioactive | s⁻¹ (inverse de l'unité de $t_{1/2}$) |
| $\tau = \dfrac{1}{\lambda} = \dfrac{t_{1/2}}{\ln 2}$ | **constante de temps** | s, an… (une **durée**) |

{{fig:pc-decroissance-radioactive}}

Après $1\,t_{1/2}$ il reste $N_0/2$ ; après $2\,t_{1/2}$, $N_0/4$ ; après $3\,t_{1/2}$, $N_0/8$ : on **divise**
par 2 à chaque demi-vie, on ne soustrait pas. Demi-vies : $^{3}_{1}\mathrm{H}$ 12,32 ans ;
$^{14}_{6}\mathrm{C}$ 5 730 ans ; $^{235}_{92}\mathrm{U}$ 7,038 × 10⁸ ans.

*Attention aux unités* : $t_{1/2}$ et $\tau$ sont des **durées**, $\lambda$ est en s⁻¹. On lit parfois
« τ exprimée en s⁻¹ » : c'est une coquille, $\tau = t_{1/2}/\ln 2$ est bien une durée.

## Fission, fusion et énergie libérée

{{fig:pc-fission-fusion}}

**Fission** : un noyau lourd donne des noyaux fils plus légers, par exemple
$^{1}_{0}\mathrm{n} + {}^{235}_{92}\mathrm{U} \rightarrow {}^{94}_{38}\mathrm{Sr} + {}^{140}_{54}\mathrm{Xe} + 2\,^{1}_{0}\mathrm{n}$
($1 + 235 = 94 + 140 + 2$ et $0 + 92 = 38 + 54$). **Fusion** : des noyaux légers s'assemblent en un noyau
plus lourd — deutérium + tritium → hélium + neutron libre + énergie, la réaction des étoiles.

Toute réaction nucléaire s'accompagne d'une **perte de masse** $\Delta m = m_{\text{initiale}} - m_{\text{finale}}$
qui libère de l'énergie (relation d'Einstein) :

$E_{\text{libérée}} = \Delta m \times c^{2}$, avec $\Delta m$ en **kg**, $c = 3{,}00 \times 10^{8}$ m·s⁻¹, $E$ en **J**.

Ne pas oublier le **carré** : $c^2 = 9{,}00 \times 10^{16}$ m²·s⁻².
