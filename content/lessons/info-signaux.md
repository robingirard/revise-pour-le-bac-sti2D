# Caractériser un signal, le numériser

## Un signal analogique périodique

{{fig:info-signal-periodique}}

La **période** $T$ est la durée au bout de laquelle le signal se répète ; elle s'exprime en **secondes** (s). La **fréquence** $f$, en **hertz** (Hz), est le nombre de répétitions par seconde : c'est l'inverse de la période.

$$f = \frac{1}{T}$$

Exemple : $T = 20$ ms $= 0{,}020$ s donne $f = 1 \div 0{,}020 = 50$ Hz. Il faut **toujours** convertir la période en secondes avant de calculer.

On repère aussi l'**amplitude**, l'**amplitude crête-à-crête** et la **valeur efficace** (*rms*), qui est la valeur de la tension continue produisant le même effet — c'est elle que mesure un voltmètre.

$$U_{\text{eff}} = \frac{U_{\max}}{\sqrt{2}}$$

Deux signaux de même période décalés de $\Delta t$ présentent un **déphasage** $\varphi = \Delta t \times 360 \div T$, en degrés.

## Les signaux numériques et la MLI

Un **chronogramme** représente les signaux en fonction du temps. On distingue le **niveau haut** (*High*, 1, 5 V) et le **niveau bas** (*Low*, 0, 0 V).

{{fig:info-mli}}

Dans la **modulation par largeur d'impulsion** (MLI, en anglais *PWM*), l'information utile est la durée $T_h$ passée au niveau haut par rapport à la période : c'est le **rapport cyclique**. La tension moyenne appliquée à la charge s'en déduit.

$$\alpha = \frac{T_h}{T} \times 100 \qquad U_{\text{moyenne}} = U_{\max} \times \frac{T_h}{T}$$

Exemple : sous $U_{\max} = 12$ V, avec $T = 2$ ms et $T_h = 1{,}4$ ms, $\alpha = 70$ % et $U_{\text{moyenne}} = 8{,}4$ V. La MLI sert à piloter les servomoteurs et la vitesse des moteurs à courant continu.

## La conversion analogique-numérique

Un **convertisseur analogique-numérique** (CAN, en anglais **ADC** pour *Analog to Digital Converter*) transforme la tension délivrée par un capteur en un nombre exploitable par la carte électronique. Attention : le **DAC** désigne la conversion inverse, du numérique vers l'analogique.

{{fig:info-can-symbole}}

La conversion comporte deux temps : l'**échantillonnage** (prélever la valeur du signal à intervalles réguliers) puis la **quantification** (comparer la valeur prélevée à des paliers).

{{fig:info-can-quantum}}

Le **quantum** $q$ est la variation minimale du signal d'entrée qui fait varier d'une unité la sortie numérique ; il s'exprime dans l'unité de la grandeur d'entrée, et $n$ est le nombre de bits du convertisseur.

$$q = \frac{\text{Amplitude du signal d'entrée}}{2^{n}}$$

**Plus le quantum est petit, plus le signal numérisé est fidèle** au signal analogique de départ.

| Convertisseur | Nombre de valeurs | Valeurs codées | Quantum sur 0 à 5 V |
|---|---|---|---|
| 2 bits | $2^2 = 4$ | 0 à 3 | 1,25 V |
| 3 bits | $2^3 = 8$ | 0 à 7 | 0,625 V |
| 8 bits | $2^8 = 256$ | 0 à 255 | 19,53 mV |
| 10 bits | $2^{10} = 1\,024$ | 0 à 1 023 | 4,88 mV |

Attention au piège : sur $n$ bits on code $2^n$ valeurs, mais la **plus grande** vaut $2^n - 1$, car le comptage commence à 0 (conversion **unipolaire**).
