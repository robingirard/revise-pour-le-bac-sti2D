# Puissance moyenne, puissance instantanée et énergie

## Ce que mesure une puissance

L'énergie se compte en **joules**. Mais deux systèmes qui échangent la même énergie ne se valent pas si l'un met une seconde et l'autre une heure. Ce qui les distingue, c'est la **puissance** : la vitesse à laquelle l'énergie est échangée.

$$P=\frac{\Delta E}{\Delta t}$$

$P$ en watts (W), $\Delta E$ en joules (J), $\Delta t$ en secondes (s). D'où $1$ W $=1$ J/s.

## La puissance moyenne est une pente

Sur un relevé qui donne l'énergie absorbée au cours du temps, $\dfrac{\Delta E}{\Delta t}$ est le **taux de variation** de $E$ entre deux instants : c'est la **pente de la sécante** qui joint les deux points.

{{fig:2i2d-velo-energie}}

Sur ce relevé, la puissance moyenne n'est pas la même partout, parce que la courbe n'est pas une droite :

| Intervalle | $\Delta E$ | $\Delta t$ | $P$ |
|---|---|---|---|
| $[0\,;1\,000]$ | $30\,000$ J | $1\,000$ s | $30$ W |
| $[1\,000\,;2\,000]$ | $60\,000$ J | $1\,000$ s | $60$ W |
| $[2\,000\,;2\,300]$ | $30\,000$ J | $300$ s | $100$ W |
| $[2\,300\,;3\,600]$ | $60\,000$ J | $1\,300$ s | $46$ W |
| Promenade entière | $180\,000$ J | $3\,600$ s | $50$ W |

Le moteur ne fournit pas toujours la même puissance : il donne davantage en côte. La valeur sur l'ensemble, $50$ W, est une moyenne de toutes les autres — elle ne dit rien de ce qui s'est passé à un instant donné.

## La puissance instantanée est une dérivée

Pour décrire ce qui se passe **à un instant**, on rétrécit l'intervalle. La puissance moyenne sur $[t\,;t+\Delta t]$ s'écrit

$$\frac{E(t+\Delta t)-E(t)}{\Delta t}$$

et quand $\Delta t$ tend vers $0$, cette pente de sécante devient la pente de la **tangente** :

$$p(t)=\lim_{\Delta t\to0}\frac{E(t+\Delta t)-E(t)}{\Delta t}=\frac{\mathrm{d}E}{\mathrm{d}t}$$

**La puissance instantanée est la dérivée de la fonction énergie.** C'est le même objet mathématique que le nombre dérivé vu en cours de mathématiques, avec $t$ à la place de $x$.

### Le formulaire, écrit en $t$

| Fonction $f$ | Dérivée $f'$ | Ensemble |
|---|---|---|
| $f(t)=a$ | $f'(t)=0$ | $\mathbb{R}$ |
| $f(t)=a\,t$ | $f'(t)=a$ | $\mathbb{R}$ |
| $f(t)=a\,t^{2}$ | $f'(t)=2a\,t$ | $\mathbb{R}$ |
| $f(t)=a\sin(bt+c)$ | $f'(t)=ab\cos(bt+c)$ | $\mathbb{R}$ |
| $f(t)=a\cos(bt+c)$ | $f'(t)=-ab\sin(bt+c)$ | $\mathbb{R}$ |

Exemple : si $E(t)=45\,t^{2}$ joules, alors $p(t)=90\,t$ watts, et à $t=2$ s la puissance instantanée vaut $180$ W.

## L'énergie est une aire

L'opération inverse de la dérivation, c'est l'intégration. Connaissant $p(t)$, on retrouve l'énergie échangée entre $0$ et $t$ :

$$E=\int_{0}^{t}p(\tau)\,\mathrm{d}\tau$$

Ce nombre est l'**aire** balayée sous la courbe de $p$ entre les instants $0$ et $t$. L'unité le confirme : des watts multipliés par des secondes donnent des joules.

Si la puissance est **constante**, l'aire est un rectangle et l'on retrouve $E=P\times\Delta t$. Dès qu'elle varie, il faut l'aire véritable.

## Approcher l'aire par des rectangles

Quand la courbe n'est pas une figure simple, on découpe l'intervalle et on remplace l'aire par une **somme d'aires de rectangles**.

{{fig:2i2d-puissance-aire-rectangles}}

Ici, quatre rectangles de $1$ s de large, de hauteurs lues sur la courbe :

$$E\approx1\times(1+2{,}5+3+2)=8{,}5\ \mathrm{J}$$

Plus les rectangles sont fins, plus la somme s'approche de l'aire vraie. C'est exactement ainsi que l'intégrale est définie — et c'est aussi ainsi qu'un ordinateur la calcule.

## Chaîne d'énergie et rendement

Un **convertisseur** transforme une énergie d'une forme en une ou plusieurs autres. Rien ne se perd : la somme des énergies obtenues est égale à l'énergie initiale.

$$E_a=E_u+E_p$$

$E_a$ l'énergie absorbée, $E_u$ l'énergie utile, $E_p$ l'énergie perdue — toujours sous forme **thermique**.

{{fig:pc-bilan-convertisseur}}

Le **rendement** est le rapport de ce que le convertisseur restitue à ce qu'il absorbe :

$$\eta=\frac{E_u}{E_a}=\frac{P_u}{P_a}$$

Deux remarques qui reviennent à chaque devoir :

- le rendement est un nombre **sans unité** — des joules divisés par des joules ; l'écrire en pourcentage n'y change rien ;
- il est **toujours strictement inférieur à $1$**, puisque $E_p>0$. Un rendement supérieur à $1$ signale une erreur de calcul, presque toujours une confusion d'unités.

Exemple : un moteur absorbe $1\,897\,000$ J et fournit $1\,238\,000$ J d'énergie mécanique. Alors $E_p=659\,000$ J et $\eta=\dfrac{1\,238\,000}{1\,897\,000}=0{,}65$, soit $65\ \%$.
