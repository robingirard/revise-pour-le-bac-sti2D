# Déperditions et bilan thermique d'une pièce

*Prérequis : la compétence **Parois, résistance thermique et coefficient $U$**.*

Un bilan thermique répond à une question d'ingénieur : **quelle puissance de chauffage** faut-il installer pour maintenir une température intérieure donnée, quand il fait froid dehors ?

## Les trois familles de déperditions

| Poste | Relation | Coefficient |
|---|---|---|
| Paroi opaque ou vitrée | $\Phi = U \times S \times \Delta T$ | $U$ en W/(m²·K), $S$ en m² |
| Pont thermique linéique | $\Phi = \psi \times L \times \Delta T$ | $\psi$ en W/(m·K), $L$ en m |
| Renouvellement d'air | $\Phi = 0{,}34 \times n \times V \times \Delta T$ | $n$ en h⁻¹, $V$ en m³ |

$\Delta T$ est l'**écart** entre l'intérieur et l'extérieur : même valeur en °C et en K.

Le coefficient $0{,}34$ Wh/(m³·K) du renouvellement d'air n'est pas magique : pour l'air, $\rho \times c \approx 1{,}2 \times 1\,000 = 1\,200$ J/(m³·K), soit $1\,200 / 3\,600 = 0{,}33$ Wh/(m³·K).

## Les ponts thermiques

Un **pont thermique** est une zone où la continuité de l'isolant est rompue : liaison plancher/façade, refend, appui de fenêtre, balcon. Les lignes de flux s'y resserrent, la paroi y est plus froide et la condensation s'y forme.

{{fig:2i2d-pont-thermique}}

- **Isolation par l'intérieur (ITI)** : chaque plancher et chaque refend interrompt l'isolant → beaucoup de ponts thermiques.
- **Isolation par l'extérieur (ITE)** : l'enveloppe isolante est continue → ponts thermiques fortement réduits, et la masse des murs reste du côté chaud.

## Un bilan complet : le bureau de 20 m²

Intérieur **19 °C**, extérieur **−1 °C**, donc $\Delta T = 20$ K. Volume $V = 50$ m³.

| Poste | Données | Calcul | $\Phi$ |
|---|---|---|---|
| Murs extérieurs | $S = 30$ m², $U = 0{,}31$ | $0{,}31 \times 30 \times 20$ | **186 W** |
| Fenêtre | $S = 4$ m², $U = 2{,}8$ | $2{,}8 \times 4 \times 20$ | **224 W** |
| Toiture | $S = 20$ m², $R = 5{,}906$ → $U = 0{,}17$ | $0{,}17 \times 20 \times 20$ | **68 W** |
| Pont thermique plancher/façade | $\psi = 0{,}60$, $L = 9$ m | $0{,}60 \times 9 \times 20$ | **108 W** |
| Renouvellement d'air | $n = 0{,}6$ h⁻¹, $V = 50$ m³ | $0{,}34 \times 0{,}6 \times 50 \times 20$ | **204 W** |
| | | **Total** | **790 W** |

{{fig:2i2d-deperditions-piece}}

Trois lectures s'imposent :

- la **fenêtre**, 7,5 fois plus petite que les murs, perd davantage qu'eux : c'est le produit $U \times S$ qui compte, et $2{,}8 \times 4 = 11{,}2$ contre $0{,}31 \times 30 = 9{,}3$ ;
- **9 mètres** de pont thermique (108 W) coûtent plus cher que **20 m²** de toiture isolée (68 W) ;
- le **renouvellement d'air** pèse le quart du bilan : dans un bâtiment bien isolé, il devient le poste dominant, d'où l'intérêt de la VMC double flux.

## De la puissance à l'énergie

$$E = \Phi \times \Delta t$$

Sur 24 heures : $E = 790 \times 24 = 18\,960$ W·h $= 19{,}0$ **kWh**. Si le chauffage est un convecteur électrique purement résistif alimenté sous 230 V, il appelle $I = \dfrac{P}{U_{\text{réseau}}} = \dfrac{790}{230} = 3{,}43$ **A** — ce qui fixe le calibre du disjoncteur et la section des conducteurs. *(Attention à la notation : ici $U_{\text{réseau}}$ est une tension en volts, sans rapport avec le coefficient $U$ des parois.)*

## Ce que change une amélioration

Remplacer la fenêtre ($U = 2{,}8$ → $U = 1{,}4$ W/(m²·K)) fait passer son flux de 224 W à $1{,}4 \times 4 \times 20 = 112$ W. Le bilan tombe à $790 - 224 + 112 = 678$ W, soit **14 % d'économie pour 4 m² traités**. C'est ainsi qu'un bureau d'études hiérarchise les travaux : on compare toujours le gain en watts au coût des travaux, poste par poste.

## Méthode

1. décomposer l'enveloppe : parois opaques, vitrages, liaisons, ventilation ;
2. pour chaque paroi, $R = \sum e/\lambda$ puis $U = 1/R$ ;
3. relever les surfaces $S$, les longueurs $L$, le volume $V$ et l'écart $\Delta T$ ;
4. calculer chaque $\Phi$, puis sommer ;
5. convertir en énergie ($E = \Phi \Delta t$) et en courant ($I = P/U$) si nécessaire.
