# Fonctions trigonométriques

## Les fonctions circulaires

Les fonctions $\cos : x\mapsto\cos(x)$ et $\sin : x\mapsto\sin(x)$ sont définies sur $\mathbb{R}$ tout entier et sont **périodiques**, de période $2\pi$ (un tour de cercle ramène au même point).

| | cosinus | sinus |
|---|---|---|
| Ensemble de définition | $\mathbb{R}$ | $\mathbb{R}$ |
| Période | $2\pi$ | $2\pi$ |
| Parité | **paire** : $\cos(-x)=\cos(x)$ | **impaire** : $\sin(-x)=-\sin(x)$ |
| Dérivée | $\cos'(x)=-\sin(x)$ | $\sin'(x)=\cos(x)$ |
| Symétrie de la courbe | axe des ordonnées | origine du repère |

{{fig:maths-courbe-cos-sin}}

**Composées.** Si $f$ est dérivable sur $I$ :
$$(\cos\circ f)'=-f'\times(\sin\circ f)\qquad\text{et}\qquad(\sin\circ f)'=f'\times(\cos\circ f).$$
On en déduit deux règles de primitives : $f'\times(\sin\circ f)$ a pour primitives $x\mapsto-\cos\big(f(x)\big)+k$, et $f'\times(\cos\circ f)$ a pour primitives $x\mapsto\sin\big(f(x)\big)+k$.

## Variations sur $[-\pi\,;\pi]$

**Cosinus.** Sur $[-\pi\,;0]$, $\sin(x)\leqslant0$ donc $\cos'(x)=-\sin(x)\geqslant0$ : le cosinus **croît** de $-1$ à $1$. Sur $[0\,;\pi]$, $\cos'(x)\leqslant0$ : il **décroît** de $1$ à $-1$.

*Attention :* le tableau imprimé p. 101 du manuel donne la ligne des signes « $-$ puis $+$ », ce qui contredit sa propre ligne de variations. Le signe correct est $+$ puis $-$.

**Sinus.** $\sin'=\cos$, donc le sinus décroît sur $\left[-\pi\,;-\dfrac{\pi}{2}\right]$ (de $0$ à $-1$), croît sur $\left[-\dfrac{\pi}{2}\,;\dfrac{\pi}{2}\right]$ (de $-1$ à $1$), puis décroît sur $\left[\dfrac{\pi}{2}\,;\pi\right]$ (de $1$ à $0$).

## Fonctions sinusoïdales

Les fonctions
$$f_c : t\longmapsto A\cos(\omega t+\varphi)\qquad\text{et}\qquad f_s : t\longmapsto A\sin(\omega t+\varphi)$$
s'appellent des **fonctions sinusoïdales**. On ne les étudie en général que pour $t\geqslant0$, la variable représentant le temps.

{{fig:maths-sinusoide}}

- $A$ est l'**amplitude** : le minimum vaut $-A$ et le maximum $A$.
- La **période** est $T=\dfrac{2\pi}{\omega}$ (en secondes si $t$ est en secondes).
- La **fréquence** est $f=\dfrac{1}{T}=\dfrac{\omega}{2\pi}$ (en hertz).
- $\omega$ est la **pulsation** (en rad$\cdot$s$^{-1}$) ; elle est proportionnelle à la fréquence : $\omega=2\pi f$.
- $\varphi$ est la **phase à l'origine** et $\omega t+\varphi$ la **phase instantanée** (en radians).

## Dériver et primitiver un signal sinusoïdal

$$f_c'(t)=-A\,\omega\,\sin(\omega t+\varphi)\qquad\qquad f_s'(t)=A\,\omega\,\cos(\omega t+\varphi)$$
$$F_c(t)=\frac{A}{\omega}\sin(\omega t+\varphi)+k\qquad\qquad F_s(t)=-\frac{A}{\omega}\cos(\omega t+\varphi)+k$$

Retenir : on **multiplie** par $\omega$ pour dériver, on **divise** par $\omega$ pour primitiver ; le signe $-$ apparaît quand on dérive un cosinus ou quand on primitive un sinus.

En particulier, une primitive de $\cos$ est $\sin$, et une primitive de $\sin$ est $-\cos$.

*Exemple.* Pour $u(t)=12\cos\left(100\pi t+\dfrac{\pi}{3}\right)$ : $A=12$ V, $\omega=100\pi$ rad$\cdot$s$^{-1}$, $\varphi=\dfrac{\pi}{3}$ rad, $T=0{,}02$ s $=20$ ms et $f=50$ Hz — c'est la tension du réseau.
