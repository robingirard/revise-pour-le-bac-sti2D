# Coder et transmettre l'information

Le bloc **COMMUNIQUER** de la chaîne d'information transporte les données d'un composant à un autre : du microcontrôleur vers un écran, d'un pupitre vers des projecteurs, d'un véhicule vers un centre de régulation. Encore faut-il que l'émetteur et le récepteur soient d'accord sur la façon de coder les bits : c'est le rôle d'un **protocole**.

## Débit binaire, liaison série et liaison parallèle

Le **débit binaire** est le nombre de bits transmis par seconde ; il s'exprime en **bit/s** (on parle aussi de bauds pour les liaisons série simples). La durée de transmission s'en déduit immédiatement.

$$t = \frac{\text{nombre de bits}}{\text{débit}}$$

Exemple : 11 bits à 19 200 bit/s durent $11 \div 19\,200 = 5{,}73 \times 10^{-4}$ s, soit environ 573 µs.

Dans une liaison **parallèle**, tous les bits d'un mot partent en même temps, sur autant de fils que de bits. Dans une liaison **série**, ils partent l'un après l'autre sur un seul conducteur : moins de fils, mais il faut repérer le début et la fin de chaque caractère.

## La trame série asynchrone

{{fig:info-trame-serie}}

Au repos, la ligne est à l'état **1**. Chaque caractère est encadré :

| Champ | Rôle |
|---|---|
| **Bit de start** (0) | réveille le récepteur et donne le rythme |
| **Bits de donnée** | en général 8 bits, **poids faible (D0) en tête** |
| **Bit de parité** | facultatif, il permet de détecter une erreur |
| **Bit(s) de stop** (1) | referme la trame et ramène la ligne au repos |

Le **bit de parité** complète la donnée pour que le nombre total de « 1 » soit pair (parité **paire**) ou impair (parité **impaire**). Exemple : la donnée 0011 0101 contient quatre « 1 » ; en parité impaire, le bit de parité vaut 1, ce qui porte le total à cinq.

Attention au piège de lecture : sur un chronogramme, les bits arrivent **poids faible en premier**. Il faut retourner la suite lue avant de calculer la valeur. Sur une liaison **RS-232**, il faut en plus inverser les niveaux : le 1 logique y est transmis sous −12 V et le 0 sous +12 V.

Exemple : un robot tondeuse annonce un taux de charge de 25 % en envoyant les codes ASCII des caractères « 2 » ($(32)_{16}$) puis « 5 » ($(35)_{16}$), et non le nombre 25.

## La liaison symétrique

{{fig:info-liaison-symetrique}}

Une liaison **symétrique** (ou différentielle) transmet le signal sur deux fils opposés, DATA+ et DATA−, plus une masse de blindage. Le récepteur reconstitue l'information par la **différence** $U_{\text{DATA+}} - U_{\text{DATA−}}$.

Une perturbation extérieure atteint les deux fils de la même façon : $(U_+ + p) - (U_- + p) = U_+ - U_-$, elle **disparaît** dans la différence. Le signal utile est en outre doublé (± 5 V au lieu de 0 à 5 V). C'est ce qui permet de longues liaisons dans un environnement bruité.

Le protocole **DMX 512**, utilisé pour piloter les projecteurs de scène, en est un bon exemple : liaison symétrique unidirectionnelle à **250 000 bit/s**, **512 canaux** valant chacun de 0 à 255, jusqu'à **32 récepteurs** pilotés par un seul pupitre. Chaque canal occupe 1 bit de start + 8 bits de donnée + 2 bits de stop, soit 11 bits.

## Les réseaux et l'adressage IP

{{fig:info-adressage-ip}}

Sur un réseau, chaque machine possède une **adresse IP** de quatre octets (par exemple 10.0.3.19). Le **masque de réseau** sépare l'adresse en deux parties : les bits à 1 du masque désignent la **partie réseau**, les bits à 0 la **partie hôte**, c'est-à-dire le numéro de la machine.

Le masque 255.255.252.0 s'écrit 1111 1111 . 1111 1111 . 1111 1100 . 0000 0000 : il comporte 22 bits à 1, d'où la notation **/22**. Il reste $32 - 22 = 10$ bits pour numéroter les machines.

| Adresse | Construction | Exemple (10.0.3.19 / 22) |
|---|---|---|
| Adresse du **réseau** | partie hôte tout à 0 | 10.0.0.0 |
| Première machine | partie hôte = 1 | 10.0.0.1 |
| Dernière machine | partie hôte = maximum − 1 | 10.0.3.254 |
| Adresse de **diffusion** | partie hôte tout à 1 | 10.0.3.255 |

Le nombre de machines adressables vaut donc $2^{10} - 2 = 1\,022$ : on retire l'adresse du réseau et l'adresse de diffusion, qui désigne toutes les machines à la fois et ne peut identifier personne.

Un même système utilise souvent plusieurs supports : une flotte de bus reçoit sa position par **liaison satellite** (GPS), la transmet au centre de régulation par **GSM/GPRS**, qui alimente les bornes d'arrêt par GSM/GPRS et le serveur de l'application par le **réseau Internet**, le smartphone du voyageur étant relié en **3G ou Wi-Fi**.
