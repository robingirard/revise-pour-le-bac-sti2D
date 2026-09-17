# Préfixes, puissances de 10 et unités électriques

## À quoi sert un préfixe

Une même grandeur physique peut valoir $0{,}000\,012$ ampère ou $12$ microampères. C'est le **même** courant : seul l'affichage change. Le préfixe évite les chapelets de zéros et permet de lire un ordre de grandeur d'un coup d'œil.

Les préfixes du programme avancent **de trois en trois** :

{{fig:conv-escalier-prefixes}}

| Préfixe | Symbole | Facteur |
|---|---|---|
| giga | G | $10^{9}$ |
| méga | M | $10^{6}$ |
| kilo | k | $10^{3}$ |
| milli | m | $10^{-3}$ |
| micro | $\mu$ | $10^{-6}$ |
| nano | n | $10^{-9}$ |

Deux pièges de notation, tous les deux fréquents en devoir :

- **m** et **M** ne sont pas le même préfixe. $1$ mW est un millième de watt, $1$ MW en vaut un million. La casse n'est pas une coquetterie typographique.
- **micro** s'écrit $\mu$, la lettre grecque mu — jamais « u », jamais « mc ».

## Changer de préfixe

Monter d'une marche vers la droite, c'est **multiplier par mille** ; vers la gauche, **diviser par mille**. Deux marches, c'est $10^{3}\times10^{3}=10^{6}$.

$$1\ \mathrm{kW} = 10^{3}\ \mathrm{W} = 10^{6}\ \mathrm{mW}$$

Le réflexe qui évite l'erreur de sens : se demander si le nombre doit **augmenter** ou **diminuer**. On passe d'une unité grande à une unité petite ? Il en faut davantage, donc le nombre grandit.

$0{,}035$ A en milliampères : le milliampère est plus petit que l'ampère, le nombre doit grandir, donc on multiplie — $35$ mA.

## L'écriture scientifique

Un nombre est en **écriture scientifique** quand il s'écrit $a\times10^{n}$ avec $1\leqslant a<10$ : un seul chiffre non nul avant la virgule.

$$0{,}000\,12 = 1{,}2\times10^{-4} \qquad 92\,200 = 9{,}22\times10^{4}$$

$12\times10^{-5}$ et $0{,}12\times10^{-3}$ valent la même chose, mais ce ne sont pas des écritures scientifiques : la mantisse doit rester entre $1$ et $10$.

Multiplier par $10^{n}$ décale la virgule de $n$ rangs vers la **droite** ; par $10^{-n}$, de $n$ rangs vers la **gauche**.

## La loi d'Ohm : convertir d'abord, calculer ensuite

{{fig:conv-loi-ohm}}

Cette relation n'est vraie que si les trois grandeurs sont dans les unités du Système international : **volt**, **ohm**, **ampère**. Un milliampère laissé dans le calcul donne un résultat faux d'un facteur mille.

La méthode, toujours la même :

1. repérer la grandeur cherchée et les deux données ;
2. **convertir les deux données** en V, $\Omega$, A ;
3. isoler la grandeur cherchée : $U=R\,I$, ou $R=\dfrac{U}{I}$, ou $I=\dfrac{U}{R}$ ;
4. calculer ;
5. **reconvertir** le résultat dans l'unité demandée ;
6. vérifier l'ordre de grandeur.

Un exemple complet. $U=500$ mV aux bornes d'une résistance $R=10\ \mathrm{k\Omega}$ :

$$U=0{,}5\ \mathrm{V},\qquad R=10\,000\ \Omega$$
$$I=\frac{0{,}5}{10\,000}=5\times10^{-5}\ \mathrm{A}=50\ \mu\mathrm{A}$$

Cinquante microampères, c'est un courant très faible — cohérent avec une résistance de dix kilohms sous un demi-volt.

## La dernière étape n'est pas facultative

Un résultat faux d'un facteur exactement $1\,000$ (ou $10^{6}$) trahit presque toujours un préfixe oublié, jamais une erreur de raisonnement. C'est la première chose à regarder quand un calcul donne une tension de mille volts sur un montage alimenté par une pile.
