# Débits, masses volumiques et grandeurs composées

## Lire une unité composée comme une phrase

$\mathrm{m^3/s}$ se lit « mètre cube **par** seconde », $\mathrm{kg/m^3}$ « kilogramme **par** mètre cube ». Ce « par » est une division, et c'est lui qui dicte la conversion : on traite le **numérateur** et le **dénominateur** séparément.

| Grandeur | Relation | Unité du Système international |
|---|---|---|
| Débit volumique | $Q=\dfrac{V}{\Delta t}$ | $\mathrm{m^3/s}$ |
| Masse volumique | $\mu=\dfrac{m}{V}$ | $\mathrm{kg/m^3}$ |
| Vitesse | $v=\dfrac{d}{\Delta t}$ | m/s |
| Pression | $p=\dfrac{F}{S}$ | Pa $=\mathrm{N/m^2}$ |
| Puissance | $P=\dfrac{E}{\Delta t}$ | W $=$ J/s |

## Convertir un débit

Un robinet remplit $1{,}5\ \ell$ en $7$ s.

{{fig:conv-debit-citerne}}

$$Q=\frac{1{,}5}{7}=0{,}214\ \ell/\mathrm{s}$$

- en $\mathrm{m^3/s}$ : seul le **volume** change d'unité, $0{,}214\ \ell/\mathrm{s}=2{,}14\times10^{-4}\ \mathrm{m^3/s}$ ;
- en $\ell/\mathrm{h}$ : seule la **durée** change, $0{,}214\times3\,600=771\ \ell/\mathrm{h}$.

Quand la durée du dénominateur passe à une unité plus grande, le nombre **augmente** : en une heure, il s'écoule bien plus qu'en une seconde.

Et pour trouver une durée de remplissage ou de vidage, on divise le volume par le débit — après avoir mis les deux dans des unités compatibles :

$$\Delta t=\frac{V}{Q}=\frac{100\,000\ \ell}{10\ \ell/\mathrm{s}}=10\,000\ \mathrm{s}$$

soit $2$ h $46$ min $40$ s.

## La masse volumique

$$m=\mu\times V$$

Le volume doit être dans l'unité qui figure au dénominateur de $\mu$. Si $\mu$ est en $\mathrm{kg/m^3}$, le volume est en $\mathrm{m^3}$ et la masse sort en kg.

| Matériau | $\mu$ |
|---|---|
| Neige fraîche | $50\ \mathrm{kg/m^3}$ |
| Eau | $1\,000\ \mathrm{kg/m^3}$ |
| Béton | $2\,400\ \mathrm{kg/m^3}$ |
| Acier | $7\,850\ \mathrm{kg/m^3}$ |

Attention au piège : $1\ \mathrm{g/cm^3}=1\,000\ \mathrm{kg/m^3}$, et non $1$. Le gramme vaut $10^{-3}$ kg, le centimètre cube $10^{-6}\ \mathrm{m^3}$ : le rapport vaut $10^{3}$.

Repère à retenir : **un mètre cube d'eau pèse une tonne**.

## Énergie et puissance

$$E=P\times\Delta t$$

Deux systèmes d'unités cohabitent, et il faut savoir passer de l'un à l'autre.

- En unités du Système international : $P$ en watts, $\Delta t$ en **secondes**, $E$ en joules.
- En unités de la facture d'électricité : $P$ en kilowatts, $\Delta t$ en **heures**, $E$ en kilowattheures.

$$1\ \mathrm{Wh}=3\,600\ \mathrm{J}, \qquad 1\ \mathrm{kWh}=3{,}6\times10^{6}\ \mathrm{J}$$

Un radiateur de $750$ W pendant $2$ h $30$ min :

$$E=0{,}750\times2{,}5=1{,}875\ \mathrm{kWh}$$
$$E=750\times9\,000=6{,}75\times10^{6}\ \mathrm{J}$$

Les deux chemins doivent donner le même résultat — $1{,}875\times3{,}6\times10^{6}=6{,}75\times10^{6}$. C'est la meilleure des vérifications.

Le **rendement** $\eta=\dfrac{E_u}{E_a}=\dfrac{P_u}{P_a}$ n'a pas d'unité : ce sont des joules divisés par des joules. Encore faut-il que les deux soient exprimés dans la **même** unité avant de faire le rapport.

## L'homogénéité : vérifier une formule sans calculer

Les unités se manipulent comme des nombres. Si l'on cherche une durée à partir d'un volume et d'un débit :

$$\frac{\mathrm{m^3}}{\mathrm{m^3/s}}=\mathrm{m^3}\times\frac{\mathrm{s}}{\mathrm{m^3}}=\mathrm{s}$$

C'est bien une durée. Tandis qu'en multipliant :

$$\mathrm{m^3}\times\mathrm{m^3/s}=\mathrm{m^6/s}$$

qui ne correspond à rien de physique.

Une formule dont les unités ne tombent pas juste est fausse, quelle que soit la beauté du raisonnement qui y a mené. Et quelques égalités valent la peine d'être connues, parce qu'elles suppriment des conversions entières :

- $1\ \mathrm{MPa}=1\ \mathrm{N/mm^2}$
- $1\ \mathrm{bar}=10^{5}\ \mathrm{Pa}$
- $1\ \mathrm{W}=1\ \mathrm{J/s}$

La première explique pourquoi, en résistance des matériaux, on travaille en newtons et en millimètres sans jamais rien convertir.

## Choisir « l'unité la plus appropriée »

Quand un énoncé le demande, la règle pratique est simple : celle qui donne un nombre **compris entre $1$ et $1\,000$**. $105\,000\ \mathrm{m^2}$ devient $10{,}5$ ha — un nombre qu'on se représente, et qu'on peut comparer à quelque chose de connu.
