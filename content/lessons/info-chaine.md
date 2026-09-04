# La chaîne d'information

Pour réagir et s'adapter à son environnement, un système automatisé doit **acquérir des informations**. La grandeur physique captée est convertie en un **signal**, qui est ensuite traité, puis communiqué.

{{fig:info-chaine-information}}

La chaîne d'information reçoit des **grandeurs physiques** et des **consignes** ; elle délivre des **informations** (ordres, messages). Elle se décompose en trois blocs.

| Bloc | Rôle | Exemples |
|---|---|---|
| **ACQUÉRIR** | prélever l'information | capteurs ; interface utilisateur : boutons poussoirs, clavier |
| **TRAITER** | décider | ordinateur ; carte Arduino ou Raspberry Pi ; automate programmable |
| **COMMUNIQUER** | transmettre l'information | voyants, écran ; relais et transistors vers la chaîne de puissance ; interface réseau |

## La nature des informations

L'information circule dans le système sous **trois formes** différentes.

{{fig:info-signal-analogique-numerique}}

| Nature | Définition | Exemple |
|---|---|---|
| **Logique** | la grandeur ne prend que **deux** valeurs : 0 ou 1, *Low* ou *High*, 0 V ou 5 V | un capteur de présence détecte, ou non, un objet |
| **Analogique** | la grandeur varie de façon **continue** dans le temps | la tension aux bornes d'une photorésistance suit la luminosité |
| **Numérique** | suite d'informations logiques (0 et 1) représentant des nombres : le signal ne prend qu'un **nombre fini** de valeurs | un codeur de position délivre le mot 101, image de l'angle du disque |

## Les capteurs

Quatre critères servent à choisir un capteur : l'**étendue de mesure** (les valeurs extrêmes mesurables), la **résolution** (la plus petite variation mesurable), la **sensibilité** (la variation de la sortie rapportée à celle de l'entrée, par exemple 10 mV/°C) et la **précision** (l'aptitude à donner une mesure proche de la valeur vraie).

Un capteur **tout ou rien** (TOR) délivre une information **binaire** : sous le seuil, la sortie vaut 0 ; au-dessus, elle vaut 1.

{{fig:info-capteur-tor-hysteresis}}

En pratique, il possède **deux seuils distincts**, pour éviter que la sortie ne devienne instable quand l'entrée est très proche du seuil : la sortie ne passe à l'état haut qu'au-dessus du **seuil haut** VT+, et ne retombe à l'état bas qu'en dessous du **seuil bas** VT−.

Un capteur **proportionnel analogique** fournit un signal proportionnel à la grandeur mesurée : une température de −20 à +20 °C devient, par exemple, une tension de 0 à 5 V. La photorésistance est un capteur **passif** : elle doit être insérée dans un montage, en général un **pont diviseur de tension** alimenté sous $V_e$, où l'on mesure

$$V_s = R_1 \times \frac{V_e}{R_1 + R_2}$$

Un capteur **proportionnel numérique** fournit directement un mot binaire, du *msb* au *lsb* : $N = (10100001)_2 = (161)_{10}$. Le **codeur absolu** donne ainsi la position d'un axe ; le **codeur incrémental** compte des impulsions, et une seconde piste décalée de 25 % permet de connaître le **sens de rotation** (on regarde l'état de la voie B au moment d'un front descendant de la voie A).

## Les systèmes asservis

Un système **asservi ou régulé** compare en permanence ce qu'il fait à ce qu'il doit faire : consigne → comparateur → correcteur → système → sortie, avec une **boucle de retour** qui ramène la mesure du capteur vers le comparateur. Si un écart est détecté, le système le corrige.
