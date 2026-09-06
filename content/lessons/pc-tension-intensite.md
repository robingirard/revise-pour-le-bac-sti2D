# Tension et intensité, en continu et en variable

## Régime continu, régime variable

En **régime continu**, la tension $U$ et l'intensité $I$ gardent la même valeur (une pile, une batterie).
En **régime variable**, elles changent au cours du temps : on les note alors $u(t)$ et $i(t)$.

Une tension sinusoïdale s'écrit :

$u(t) = U_m \times \sin(2 \times \pi \times f \times t) + U_{\text{moy}}$

- $u(t)$ : tension à l'instant $t$, en volt (V) ;
- $U_m$ : **amplitude**, en volt (V) ;
- $f$ : **fréquence**, en hertz (Hz) ; la **période** vaut $T = \dfrac{1}{f}$, en seconde (s) ;
- $U_{\text{moy}}$ : **composante continue** (notée aussi $U_{DC}$), en volt (V).

Si $U_{\text{moy}} = 0$ V, la tension est dite **sinusoïdale alternative**.

## Valeur moyenne et valeur efficace

{{fig:pc-sinusoide-umax-ueff}}

| Cas | Valeur efficace |
|---|---|
| tension sinusoïdale avec $U_{\text{moy}} \neq 0$ V | $U_{\text{eff}} = \sqrt{U_{\text{moy}}^{2} + \dfrac{U_m^{2}}{2}}$ |
| tension sinusoïdale alternative ($U_{\text{moy}} = 0$ V) | $U_{\text{eff}} = \sqrt{\dfrac{U_m^{2}}{2}} = \dfrac{U_m}{\sqrt{2}}$ |

**À retenir** : en France, la tension du réseau est **sinusoïdale alternative**, de valeur efficace
**230 V** ($\pm\ 10$ %) et de fréquence **50 Hz** (donc $T = 20$ ms). Son amplitude vaut
$U_m = 230 \times \sqrt{2} \approx 325$ V : l'amplitude est toujours **plus grande** que la valeur efficace.

Deux relations très utiles pour exploiter un oscillogramme (elles ne sont pas au programme, mais elles
se lisent directement sur la courbe) :

$U_{\text{moy}} = \dfrac{U_{\max} + U_{\min}}{2}$ et $U_m = \dfrac{U_{\max} - U_{\min}}{2}$

## Conventions générateur et récepteur

{{fig:pc-convention-generateur-recepteur}}

| Convention | Dipôle | Fléchage |
|---|---|---|
| **générateur** | pile, batterie… (symbole rond) | tension et intensité fléchées dans le **même sens** |
| **récepteur** | dipôle ohmique, condensateur, bobine… (symbole rectangulaire) | tension et intensité fléchées dans le **sens opposé** |

Il faut choisir les conventions **avant** d'écrire les lois du circuit : ce sont elles qui fixent les signes.

## Lois des mailles, des nœuds et loi d'Ohm

{{fig:pc-loi-mailles-noeuds}}

Pour ce circuit (générateur, dipôle ohmique $R$ en série, puis condensateur et bobine en parallèle) :

| Loi des mailles | Loi des nœuds | Loi d'Ohm |
|---|---|---|
| $u_G(t) - u_R(t) - u_L(t) = 0$ | | |
| $u_G(t) - u_R(t) - u_C(t) = 0$ | $i_R(t) = i_C(t) + i_L(t)$ | $u_R(t) = R \times i_R(t)$ |
| $u_C(t) - u_L(t) = 0$ | | |

$R$ est la résistance du dipôle ohmique, en **ohm** ($\Omega$).

**Attention** : les lois des mailles et des nœuds peuvent s'appliquer aux **valeurs efficaces**
$U_{\text{eff}}$ et $I_{\text{eff}}$ **uniquement si les récepteurs se limitent à des dipôles ohmiques**.
Dès qu'il y a un condensateur ou une bobine, les tensions sont déphasées et leurs valeurs efficaces ne
s'additionnent plus.
