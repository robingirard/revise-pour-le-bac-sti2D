# La statique graphique

La méthode **analytique** (projections, équations de moments) n'est pas la seule façon de résoudre un
problème de statique. Quand le problème est **plan** et qu'il ne met en jeu que **deux ou trois forces**,
la méthode **graphique** donne la réponse par un tracé, sans écrire une seule équation.

## Solide soumis à 2 forces

{{fig:statique-deux-forces}}

Un solide en équilibre sous l'action de **deux forces** seulement impose que ces forces aient :

- le **même support** ;
- la **même intensité** ;
- des **sens opposés**.

Le support commun ne peut être que la droite qui joint les deux points d'application. La pièce est alors
soit en **traction** (flèches vers l'extérieur), soit en **compression** (flèches vers l'intérieur).

C'est le cas des bielles, tirants, haubans et barres de treillis : dès qu'on les reconnaît, on connaît
gratuitement la **direction** de leur effort.

## Solide soumis à 3 forces

{{fig:2i2d-trois-forces-methode}}

Un solide en équilibre sous l'action de **trois forces** non parallèles vérifie deux conditions :

1. les **trois supports sont concourants** en un même point $I$ ;
2. la **somme vectorielle** des trois forces est nulle : $\vec{F_1} + \vec{F_2} + \vec{F_3} = \vec{0}$.

*Pourquoi le concours ?* Si l'on écrit les moments au point $I$ où deux supports se coupent, ces deux
moments sont nuls (bras de levier nul). Le théorème du moment $\sum \vec{M}_I = \vec{0}$ impose alors que
le moment de la troisième force soit nul lui aussi : son support passe donc par $I$.

## Le dynamique

{{fig:2i2d-dynamique-echelle}}

Le **dynamique** est le polygone obtenu en plaçant les vecteurs **bout à bout**, la pointe de l'un touchant
l'origine du suivant. Comme la somme est nulle, on revient au point de départ : le dynamique est **fermé**.
Avec trois forces, c'est un **triangle**.

Les longueurs des côtés sont proportionnelles aux intensités. Une **échelle des forces** (par exemple
*1 cm ↔ 10 kN*) permet de passer de l'une à l'autre :

- lire une force : $F = \ell_{\text{mesurée}} \times \text{échelle}$ ;
- tracer une force : $\ell = F / \text{échelle}$.

L'échelle doit toujours figurer sur la copie, sinon le tracé n'est pas exploitable.

## La démarche

1. **isoler** le solide et faire le bilan des trois actions extérieures ;
2. tracer les **supports connus** et repérer leur point de concours $I$ ;
3. joindre $I$ au point d'application de la troisième force : sa **direction** est trouvée ;
4. choisir une **échelle** et tracer le vecteur entièrement connu ;
5. tracer par ses extrémités les **parallèles** aux deux directions, jusqu'à fermer le triangle ;
6. **mesurer** les côtés inconnus et les convertir en newtons.

## Cas particuliers et limites

- **Trois forces parallèles** (poutre sur deux appuis) : le point de concours est rejeté à l'infini, la
  construction ne s'applique pas. On revient à l'analytique : $\sum F_y = 0$ et $\sum M_z = 0$.
- La précision dépend de l'épaisseur du trait et de l'échelle : un écart de 1 à 2 % avec le calcul
  analytique est normal.

## À retenir

| Question | Réponse |
|---|---|
| 2 forces en équilibre | même support, même intensité, sens opposés |
| 3 forces en équilibre | supports concourants **et** dynamique fermé |
| Le dynamique, c'est quoi ? | le polygone des forces mises bout à bout |
| Lire une force sur le tracé | longueur mesurée × échelle |
| Le point de concours est à l'infini | forces parallèles : passer à l'analytique |
