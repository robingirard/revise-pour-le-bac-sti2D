# Obtenir une pièce : procédés et prototypage

## Trois façons d'obtenir une forme

Tous les procédés se rangent en trois familles, selon ce qu'ils font à la matière.

| Famille | Principe | Exemples |
|---|---|---|
| **Enlèvement** | on retire de la matière d'un brut | tournage, fraisage, perçage, rectification |
| **Déformation** | on déforme sans rien retirer | forgeage, emboutissage, pliage, extrusion |
| **Ajout** | on dépose la matière là où il en faut | fonderie, injection, fabrication additive |

La question à se poser devant un procédé inconnu est simple : est-ce qu'on enlève des copeaux, est-ce qu'on plie sans rien enlever, ou est-ce qu'on part de rien et qu'on remplit ?

## Les usinages courants

- **Tournage** : la **pièce** tourne, l'outil avance. On obtient des formes **de révolution** — arbres, alésages, gorges, filetages.
- **Fraisage** : l'**outil** tourne, la pièce avance sous lui. On obtient des formes prismatiques, des rainures, des poches.
- **Perçage** : le foret tourne et avance, et laisse un trou cylindrique. Pour une meilleure précision, on **alèse** ensuite.

Le **brut**, c'est ce dont part l'usinage : barre, tôle, pièce moulée ou forgée. (À ne pas confondre avec le **rebut**, qui est une pièce ratée.)

## Trois critères, et rien d'autre

> **La forme, le matériau, la quantité.**

Ces trois-là se contraignent mutuellement, et ils suffisent à choisir.

| Pièce | Procédé |
|---|---|
| Boîtier de télécommande, 200 000 pièces | injection plastique |
| Arbre de transmission en acier | tournage |
| Carrosserie en tôle, grande série | emboutissage |
| Prototype de poignée ergonomique | impression 3D |
| Carter de moteur en aluminium | moulage, puis reprise en usinage |

Le prix et le délai ne sont pas des critères d'entrée : ce sont les **conséquences** du choix.

## L'outillage décide de tout

C'est la ligne de partage entre les procédés.

- Ceux qui demandent un **outillage dédié** — moule d'injection, matrice d'emboutissage, moule de fonderie sous pression — coûtent cher au départ, puis presque rien par pièce.
- Ceux qui n'en demandent **aucun** — impression 3D, usinage — démarrent bon marché, mais leur coût unitaire ne descend jamais.

D'où le calcul du **point d'équilibre**. Si un moule coûte $24\,000$ € pour $1{,}50$ € la pièce, contre $19{,}50$ € en impression 3D sans outillage :

$$24\,000 + 1{,}5\,n < 19{,}5\,n$$
$$n > \frac{24\,000}{18} = 1\,333$$

À partir de **1 334 pièces**, l'injection l'emporte. En dessous, l'outillage n'est pas amorti.

Ce raisonnement se refait à chaque fois : il n'y a pas de seuil universel, et « 500 pièces, c'est de la série » ne veut rien dire tant qu'on n'a pas les chiffres.

## Obtenir, puis reprendre

Un carter moulé sort avec une précision de l'ordre du millimètre. Or ses **portées de roulement** demandent quelques centièmes.

On procède donc en deux temps : la forme générale par un procédé rapide et bon marché, puis une reprise en usinage — **seulement** sur les surfaces fonctionnelles.

Usiner le carter entier dans un bloc coûterait dix fois plus cher, pour une précision inutile sur 90 % de la pièce.

C'est aussi la raison pour laquelle on cherche un brut **proche de la forme finale** : chaque copeau, c'est de la matière achetée puis jetée, du temps machine et de l'énergie. Un brut de forme complexe coûte plus cher à obtenir — l'arbitrage est là, et c'est ce qui rend l'éco-conception concrète.

## La fabrication additive

On découpe le modèle numérique en tranches et la machine les empile : dépôt de fil fondu, photopolymérisation, frittage de poudre. Aucun outil, aucun moule.

Ses atouts : les **formes impossibles** à usiner ou à démouler (canaux internes, treillis), la pièce unique, et la modification gratuite — changer la forme ne coûte qu'un nouveau fichier, là où l'injection demanderait un moule neuf.

Sa limite, et elle est structurelle : **aucun effet d'échelle**. Une pièce imprimée en trois heures en demandera toujours trois, qu'on en fasse une ou mille.

## Le prototype

Un prototype répond à des questions qu'aucun dessin ne tranche : est-ce que ça tient en main, est-ce que ça se monte, est-ce que la cinématique fonctionne ?

Il est fabriqué vite et à l'unité, souvent par impression 3D, et rarement dans le matériau de série — ses essais de résistance ne valent donc que pour lui. Il ne remplace pas le dessin de définition : on cote toujours.

## Deux notes qui reviennent en devoir

**Le forgeage rend plus résistant.** En usinant un bloc, on coupe les fibres du métal ; en forgeant, on les couche le long de la forme. Une bielle ou un vilebrequin forgé résiste bien mieux à la fatigue qu'une pièce identique taillée dans la masse.

**L'état de surface se cote.** Le symbole porté sur une cote indique la rugosité exigée. Comme pour les tolérances : une exigence de finesse coûte cher, on ne la porte que là où la fonction la réclame. Une portée de roulement, oui ; une face brute de fonderie, non.
