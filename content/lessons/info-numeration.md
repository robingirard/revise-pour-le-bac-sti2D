# Numération et codage

## Bit, octet et poids des bits

Le **bit** (*binary digit*) est la plus petite unité d'information manipulable par une machine numérique : il vaut 0 ou 1. L'**octet** (*byte*, noté B majuscule) est un groupe de **8 bits** : il code $2^8 = 256$ valeurs, de 0 (0000 0000) à 255 (1111 1111).

{{fig:info-poids-binaires}}

Dans un nombre binaire, la valeur d'un bit, appelée **poids**, dépend de sa position : le poids croît d'une puissance de 2 en allant de la droite vers la gauche. Le bit le plus à droite est le **bit de poids faible** (*lsb*), celui le plus à gauche le **bit de poids fort** (*msb*). Exemple : $(1101)_2 = 1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 = 8 + 4 + 0 + 1 = 13$.

## Les trois bases

On utilise la **base 10** dans la vie courante, la **base 2** dans les ordinateurs et la **base 16** (hexadécimal) pour compacter les mots binaires et les rendre lisibles par les humains. Un symbole hexadécimal code exactement **4 bits**.

| Décimal | Binaire | Hexadécimal | Décimal | Binaire | Hexadécimal |
|---|---|---|---|---|---|
| 0 | 0000 | 0 | 8 | 1000 | 8 |
| 1 | 0001 | 1 | 9 | 1001 | 9 |
| 2 | 0010 | 2 | 10 | 1010 | A |
| 3 | 0011 | 3 | 11 | 1011 | B |
| 4 | 0100 | 4 | 12 | 1100 | C |
| 5 | 0101 | 5 | 13 | 1101 | D |
| 6 | 0110 | 6 | 14 | 1110 | E |
| 7 | 0111 | 7 | 15 | 1111 | F |

On indique la base **en indice** pour éviter toute confusion : $(3A9)_{16}$, $(238)_{10}$, $(0100\,1101)_2$. En programmation, l'hexadécimal se repère par un préfixe qui dépend du langage : 0x en C, C++ et Java, ou # en HTML.

## Changer de base

{{fig:info-bases-triangle}}

- **Base 10 → base 2** : divisions successives par 2, restes lus **de bas en haut**.
- **Base 10 → base 16** : divisions successives par 16.
- **Base 2 ou base 16 → base 10** : somme des poids multipliés par les chiffres.
- **Base 2 ↔ base 16** : regroupement par **blocs de 4 bits**, à partir de la droite.

Exemple filé avec le nombre 59 : $59 \div 2 = 29$ reste 1 ; $29 \div 2 = 14$ reste 1 ; $14 \div 2 = 7$ reste 0 ; $7 \div 2 = 3$ reste 1 ; $3 \div 2 = 1$ reste 1 ; $1 \div 2 = 0$ reste 1. En lisant les restes de bas en haut, $59_{(10)} = (0011\,1011)_2$. Par blocs de 4 bits, 0011 donne $2 + 1 = 3$ et 1011 donne $8 + 2 + 1 = 11 = B$, donc $59_{(10)} = (3B)_{16}$. Vérification : $3 \times 16^1 + 11 \times 16^0 = 48 + 11 = 59$.

## Les masques

Pour ne conserver que certains bits d'un octet, on applique un **masque** : une opération logique **ET** entre la donnée et un mot comportant des 1 aux positions à conserver, des 0 ailleurs.

| | Mot de 8 bits |
|---|---|
| Donnée | 1011 0001 |
| Masque | 1100 0000 |
| Résultat | 1000 0000 |

## Le codage des caractères

Le code **ASCII** (*American Standard Code for Information Interchange*) sert à transmettre les caractères alphanumériques. Chaque caractère est codé sur **8 bits**, donc sur **2 symboles hexadécimaux** : « A » est codé $(41)_{16}$, soit $65_{(10)}$ et $(0100\,0001)_2$. La norme **Unicode** attribue un identifiant à tout caractère de toute langue ; l'encodage **UTF-8** est aujourd'hui le plus courant.
