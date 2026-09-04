# Le cercle trigonométrique

## Enroulement de l'axe réel

On munit le plan du repère orthonormé $(O,I,J)$ et on note $\mathcal{C}$ le cercle de centre $O$ et de rayon $1$.
On place l'axe réel tangent au cercle en $I$, puis on l'**enroule** sur $\mathcal{C}$ : les réels positifs dans le sens inverse des aiguilles d'une montre (**sens direct** ou trigonométrique), les négatifs dans le **sens indirect**. Le plan est alors dit **orienté** et $\mathcal{C}$ s'appelle le **cercle trigonométrique**.

{{fig:maths-cercle-trigo}}

- À chaque réel $x$ correspond **un unique** point $M$ du cercle.
- À chaque point $M$ correspond une **infinité** de réels, différant tous d'un multiple de $2\pi$ (le périmètre du cercle).

## Angles orientés et radians

Si $M$ est le point associé au réel $x$, l'angle $\left(\overrightarrow{OI},\overrightarrow{OM}\right)$ mesure $x$ **radians** : la mesure en radians est la **mesure algébrique de l'arc** correspondant, donc un nombre **signé** (positif dans le sens direct, négatif dans le sens indirect).

La notation $\widehat{IOM}$ est réservée aux angles géométriques, dont la mesure n'est pas signée.

La **mesure principale** d'un angle orienté est celle qui appartient à $\left]-\pi\,;\pi\right]$ : on l'obtient en ajoutant ou en retranchant des multiples de $2\pi$.
*Exemple :* $\dfrac{7\pi}{3}-2\pi=\dfrac{\pi}{3}$ ; $\dfrac{5\pi}{4}-2\pi=-\dfrac{3\pi}{4}$.

## Conversion degrés – radians

| Degrés | 0 | 30 | 45 | 60 | 90 | 120 | 135 | 150 | 180 | 360 |
|---|---|---|---|---|---|---|---|---|---|---|
| Radians | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ | $\dfrac{2\pi}{3}$ | $\dfrac{3\pi}{4}$ | $\dfrac{5\pi}{6}$ | $\pi$ | $2\pi$ |

{{fig:maths-cercle-angles}}

Les degrés et les radians sont **proportionnels** : $180^{\circ}\leftrightarrow\pi$ rad, donc une mesure en degrés se convertit en la multipliant par $\dfrac{\pi}{180}$.

## Cosinus et sinus d'un réel

Soit $M$ le point du cercle trigonométrique associé au réel $x$. Par définition, $\cos(x)$ est l'**abscisse** de $M$ et $\sin(x)$ son **ordonnée** :
$$M\big(\cos(x)\,;\sin(x)\big).$$

{{fig:maths-cos-sin-cercle}}

Comme $OM=1$, le théorème de Pythagore donne la **relation fondamentale** : pour tout réel $x$,
$$\cos^{2}(x)+\sin^{2}(x)=1.$$

## Valeurs remarquables

| Radians | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ |
|---|---|---|---|---|---|
| $\cos$ | $1$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{1}{2}$ | $0$ |
| $\sin$ | $0$ | $\dfrac{1}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $1$ |

Le cosinus **décroît** de $1$ à $0$ et le sinus **croît** de $0$ à $1$ sur $\left[0\,;\dfrac{\pi}{2}\right]$ : les deux lignes se lisent en sens inverse.

## Angles associés

{{fig:maths-angles-associes}}

Pour tout réel $x$ :

| Angle | $\cos$ | $\sin$ |
|---|---|---|
| $-x$ | $\cos(x)$ | $-\sin(x)$ |
| $\pi-x$ | $-\cos(x)$ | $\sin(x)$ |
| $\pi+x$ | $-\cos(x)$ | $-\sin(x)$ |
| $\dfrac{\pi}{2}-x$ | $\sin(x)$ | $\cos(x)$ |
| $\dfrac{\pi}{2}+x$ | $-\sin(x)$ | $\cos(x)$ |
| $2\pi-x$ | $\cos(x)$ | $-\sin(x)$ |
| $2\pi+x$ | $\cos(x)$ | $\sin(x)$ |

Astuce : les lignes $-x$, $\pi-x$ et $\pi+x$ correspondent aux trois **symétries** du cercle (axe des abscisses, axe des ordonnées, centre $O$) ; celles en $\dfrac{\pi}{2}$ **échangent** cosinus et sinus.
