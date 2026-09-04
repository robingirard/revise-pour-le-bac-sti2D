# Le principe fondamental de la statique

L'objectif de la **statique** est de calculer les actions mécaniques appliquées à un solide **en équilibre**.

Un solide est en équilibre s'il est **au repos** ou s'il a un **mouvement rectiligne uniforme** (vitesse
constante). Le principe fondamental de la statique (PFS, 1ʳᵉ loi de Newton) s'écrit alors :

- **théorème de la résultante** : $\sum \vec{F}_{\text{ext} \rightarrow S} = \vec{0}$ ;
- **théorème du moment résultant** : $\sum \vec{M}_{A(\vec{F}_{\text{ext}} \rightarrow S)} = \vec{0}$.

Autrement dit, la somme des torseurs des actions extérieures est le torseur nul :
$\sum {}_A\{\tau_{\text{ext} \rightarrow S}\} = {}_A\{0\}$.

**Attention** : tous les moments (donc tous les torseurs) doivent être exprimés **au même point**. Le moment
d'une force dépend du point où on le calcule ; additionner des moments écrits en des points différents n'a
aucun sens.

## La démarche

1. on **isole** le solide (on trace sa frontière : tout ce qui est dehors est « extérieur ») ;
2. on fait le **bilan** de toutes les actions mécaniques extérieures (contact **et** distance) ;
3. on **modélise** ces actions (vecteurs ou torseurs) ;
4. on choisit une **méthode de résolution** : analytique ou graphique ;
5. on **présente les résultats** (valeur, direction, sens).

Astuce : pour la méthode analytique, on écrit le théorème du moment **au point où passent le plus
d'inconnues** — leur bras de levier est nul, elles disparaissent de l'équation.

## Deux cas graphiques à connaître

{{fig:statique-deux-forces}}

**Solide soumis à 2 forces** : les deux forces ont le **même support**, la **même intensité** et des **sens
opposés**. La pièce est alors soit en traction, soit en compression (bielle, tirant, hauban).

{{fig:statique-trois-forces}}

**Solide soumis à 3 forces** : les trois supports sont **concourants** (ils se coupent en un même point $I$)
et la somme vectorielle est nulle, donc le **dynamique** (le polygone des forces mis bout à bout) est un
**triangle fermé**. On en déduit graphiquement les intensités inconnues en mesurant le triangle.

## Les appuis

{{fig:statique-appuis}}

| Appui | Symbole | Ce qu'il autorise |
|---|---|---|
| Appui simple (glissant) | triangle sur deux rouleaux | rotation **et** translation le long du sol |
| Articulation (appui simple fixe) | triangle seul | rotation seulement |
| Encastrement | poutre partant d'un mur hachuré | rien : aucun degré de liberté |

## L'hypothèse d'un problème plan

On peut se ramener à une étude **plane** si le système est symétrique par rapport au plan d'étude, si les
forces extérieures sont contenues dans ce plan (ou symétriques par rapport à lui) et si les moments
extérieurs lui sont orthogonaux. Dans le plan $(x, y)$, il reste alors **3 équations** : deux de résultante
($\sum F_x = 0$, $\sum F_y = 0$) et une de moment ($\sum M_z = 0$).

## À retenir

| Question | Réponse |
|---|---|
| Que dit le PFS ? | $\sum \vec{F}_{\text{ext}} = \vec{0}$ **et** $\sum \vec{M}_{A} = \vec{0}$ |
| Le PFS s'applique-t-il en mouvement ? | oui, si le mouvement est rectiligne **uniforme** |
| Combien d'équations en plan ? | 3 |
| Solide à 2 forces | même support, même intensité, sens opposés |
| Solide à 3 forces | supports concourants + dynamique fermé |
