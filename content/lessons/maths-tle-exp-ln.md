# Exponentielle et logarithme népérien

## Le nombre e et la fonction exponentielle

En tronc commun, on a étudié les fonctions $x\mapsto a^{x}$ pour $a>0$. Parmi elles, **une seule** a une tangente de coefficient directeur $1$ au point d'abscisse $0$ : la valeur correspondante de $a$ est notée $\mathrm{e}$. Son existence et son unicité sont **admises**.

$$\mathrm{e}=2{,}718\,281\,828\ldots\approx2{,}718$$

La fonction $x\mapsto\mathrm{e}^{x}$ est définie, dérivable et **strictement positive** sur $\mathbb{R}$, et elle est sa propre dérivée.

| Propriété | Formule |
|---|---|
| Produit | $\mathrm{e}^{a}\times\mathrm{e}^{b}=\mathrm{e}^{a+b}$ |
| Inverse | $\mathrm{e}^{-a}=\dfrac{1}{\mathrm{e}^{a}}$ |
| Quotient | $\dfrac{\mathrm{e}^{a}}{\mathrm{e}^{b}}=\mathrm{e}^{a-b}$ |
| Puissance | $\left(\mathrm{e}^{a}\right)^{n}=\mathrm{e}^{an}$ |
| Valeurs | $\mathrm{e}^{0}=1$ et $\mathrm{e}^{1}=\mathrm{e}$ |

*Exemple.* $\dfrac{\left(\mathrm{e}^{-3x}\right)^{2}\times\left(\mathrm{e}^{2x}\right)^{-3}}{\mathrm{e}^{5x}\times\mathrm{e}^{6x}}=\dfrac{\mathrm{e}^{-6x}\times\mathrm{e}^{-6x}}{\mathrm{e}^{11x}}=\dfrac{\mathrm{e}^{-12x}}{\mathrm{e}^{11x}}=\mathrm{e}^{-23x}$.

## Le logarithme népérien

Pour tout réel $a>0$, l'équation $\mathrm{e}^{x}=a$ admet **une unique solution**, notée $\ln(a)$ : c'est la définition du logarithme népérien. On en déduit les deux identités de base

$$\mathrm{e}^{\ln(a)}=a\quad(a>0)\qquad\text{et}\qquad\ln\left(\mathrm{e}^{x}\right)=x\quad(x\in\mathbb{R}).$$

La fonction $\ln$ est définie et **strictement croissante** sur $\left]0\,;+\infty\right[$, de dérivée $\dfrac{1}{x}$, avec $\ln(1)=0$ et $\ln(\mathrm{e})=1$.

| Propriété | Formule (pour $a>0$, $b>0$) |
|---|---|
| Produit | $\ln(ab)=\ln(a)+\ln(b)$ |
| Quotient | $\ln\left(\dfrac{a}{b}\right)=\ln(a)-\ln(b)$ |
| Inverse | $\ln\left(\dfrac{1}{a}\right)=-\ln(a)$ |
| Puissance | $\ln\left(a^{n}\right)=n\ln(a)$, et $\ln\left(a^{x}\right)=x\ln(a)$ (admis) |
| Racine | $\ln\left(\sqrt{a}\right)=\dfrac{1}{2}\ln(a)$ |

**Piège classique** : $\ln(a+b)$ **ne se simplifie pas**. Contre-exemple : $\ln(1+1)=\ln(2)\approx0{,}69$ alors que $\ln(1)+\ln(1)=0$.

**Lien avec le logarithme décimal** du tronc commun : $\log(x)=\dfrac{\ln(x)}{\ln(10)}$ avec $\ln(10)\approx2{,}303$. C'est ce logarithme-là qui sert au pH et aux décibels.

## Courbes et limites

{{fig:mathstle-exp-ln-courbes}}

$$\lim_{x\to-\infty}\mathrm{e}^{x}=0\qquad\lim_{x\to+\infty}\mathrm{e}^{x}=+\infty\qquad\lim_{x\to0^{+}}\ln(x)=-\infty\qquad\lim_{x\to+\infty}\ln(x)=+\infty$$

Les deux courbes sont symétriques par rapport à la droite d'équation $y=x$ : l'asymptote **horizontale** de l'exponentielle en $-\infty$ devient l'asymptote **verticale** du logarithme en $0$.

## Résoudre équations et inéquations

- $\mathrm{e}^{ax}=b$ : on vérifie d'abord que $b>0$ (sinon pas de solution), puis $ax=\ln(b)$ et $x=\dfrac{\ln(b)}{a}$.
- $\ln(x)=b$ : la solution est $x=\mathrm{e}^{b}$, à condition que $x>0$ soit respecté.
- Pour les **inéquations**, les deux fonctions sont strictement croissantes : elles **conservent** le sens de l'inégalité. Ainsi $\ln(x)\leqslant2{,}5$ équivaut à $0<x\leqslant\mathrm{e}^{2{,}5}\approx12{,}18$.

*Exemple résolu.* $\mathrm{e}^{-0{,}016x}-2=0$ donne $\mathrm{e}^{-0{,}016x}=2$, puis $-0{,}016x=\ln(2)$ et $x=-\dfrac{\ln(2)}{0{,}016}\approx-43{,}32$. La solution est **négative** : si $x$ désigne une durée, le problème n'a pas de solution acceptable. Toujours interpréter le résultat.

## Trois applications à la physique-chimie

- **Demi-vie.** Pour $N(t)=N_{0}\,\mathrm{e}^{-\lambda t}$, la demi-vie vérifie $\mathrm{e}^{-\lambda t_{1/2}}=0{,}5$, d'où $t_{1/2}=\dfrac{\ln(2)}{\lambda}$. Le nombre initial $N_{0}$ disparaît du calcul.
- **pH.** $\mathrm{pH}=-\log\left(\left[\mathrm{H}_{3}\mathrm{O}^{+}\right]\right)$, donc $\left[\mathrm{H}_{3}\mathrm{O}^{+}\right]=10^{-\mathrm{pH}}$.
- **Niveau sonore.** $L=10\log\dfrac{I}{I_{0}}$ avec $I_{0}=10^{-12}\ \mathrm{W}\cdot\mathrm{m}^{-2}$. Doubler l'intensité ajoute $10\log(2)\approx3$ dB, **quelle que soit** l'intensité de départ.
