# Le graphe des liaisons

Une fois les classes identifiées, on regarde **chaque contact entre deux classes** et on en déduit
la **liaison** (nom, centre, axe). Le **graphe des liaisons** résume tout :

- un **cercle** par classe d'équivalence (avec sa couleur) ;
- un **trait** par liaison, avec son nom, son centre et son axe.

## Exemple : le serre-joint

| Entre | Contact | Liaison |
|---|---|---|
| E1 et E2 | surfacique plan (×2) | **Glissière** d'axe (A, x) |
| E2 et E3 | filetage / taraudage | **Hélicoïdale** d'axe (B, x) |
| E3 et E4 | surfacique sphérique | **Rotule** de centre C |

{{fig:mecanisme-serre-joint-graphe}}

## Exemple : le bielle-manivelle

{{fig:mecanisme-bielle-manivelle-graphe}}

## La démarche complète

1. **Étudier** le dessin d'ensemble pour comprendre le fonctionnement.
2. **Identifier les classes d'équivalence** (une couleur par classe, pièces déformables exclues).
3. **Identifier la nature des contacts** entre classes → nature de chaque liaison et son repère.
4. **Tracer le graphe des liaisons** (nom, centre, axe de chaque liaison).
5. **Tracer le schéma cinématique** 2D ou 3D.

## Exemple : l'étau (une boucle dans le graphe)

| Entre | Contact | Liaison |
|---|---|---|
| E1 et E2 | surfacique plan (×2) | **Glissière** d'axe (A, x) |
| E1 et E3 | filetage / taraudage | **Hélicoïdale** d'axe (B, x) |
| E2 et E3 | cylindre court + épaulements | **Pivot** d'axe (C, x) |
| E3 et E4 | cylindre long | **Pivot glissant** d'axe (D, y) |

{{fig:mecanisme-etau-graphe}}

Le graphe contient une **boucle** E1 – E2 – E3 : les mouvements de ces trois classes sont liés
(un tour de vis fait avancer le mors mobile d'un pas). C'est une **chaîne fermée**.
