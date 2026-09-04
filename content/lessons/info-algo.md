# Algorithmes, algorigrammes et diagrammes

Un **algorithme** est un ensemble de règles opératoires qui ordonnent d'exécuter, dans un ordre déterminé, un nombre **fini** d'opérations élémentaires appelées instructions. La démarche est toujours la même : **analyse** (définir le problème) → **algorithme** (définir la méthode qui mène à la solution) → **programme** (transcrire dans un langage de programmation).

L'algorithme ne dépend d'aucun langage : on l'écrit en **pseudo-code** (langage presque naturel) ou sous forme d'**algorigramme**. Il comporte un **en-tête** (son nom), une **partie déclarative** (constantes et variables) et une **partie exécutive**, délimitée par « début » et « fin ».

## Constantes et variables

Une **constante** est une donnée qui ne change pas au cours du programme ; on la déclare par nom = valeur, par exemple Pi = 3,1416. Une **variable** est le nom donné à un espace de stockage d'une donnée appelée à changer ; on la déclare par nom : type. C'est une boîte : le nom est l'étiquette, le type en fixe la taille, la valeur est ce qu'on range dedans.

| Type | Mot-clé | Exemples |
|---|---|---|
| Entier relatif | int | −323 ; 0 ; 42 |
| Booléen (variable logique sur 1 bit) | boolean | 0 ou 1, *False* ou *True* |
| Nombre décimal | float | −5,3 ; 0,007 (le séparateur est le **point**) |
| Chaîne de caractères | string | 'rouge' |
| Tableau | array | ['bleu', 'rouge', 'vert'], premier indice 0 |

La **portée** d'une variable désigne les espaces où elle est utilisable : déclarée dans une fonction, elle est **locale** et n'existe que là ; déclarée en dehors de toute fonction, elle est **globale**.

## L'algorigramme

{{fig:info-algorigramme-symboles}}

| Symbole | Rôle |
|---|---|
| Rectangle à bouts arrondis | début ou fin (un seul début, plusieurs fins possibles) |
| Rectangle | traitement (calcul, incrémentation, ordre) |
| Rectangle à double barre verticale | sous-programme |
| Parallélogramme | entrée ou sortie de données |
| Losange | test : la réponse est oui ou non |

{{fig:info-algorigramme-structures}}

- **Structure linéaire** : les traitements s'exécutent successivement, dans l'ordre de leur énoncé.
- **Structure alternative** : SI condition vraie ALORS traitement 1 SINON traitement 2 FIN SI — deux issues qui s'excluent mutuellement.
- **Structure répétitive** : TANT QUE condition vraie FAIRE traitement FIN TANT QUE — on teste **d'abord** la condition.
- **Boucle avec comptage** : POUR N = x jusqu'à N = 0, RÉPÉTER traitement, DÉCRÉMENTER N, FIN POUR.

Exemple de pseudo-code, pour faire clignoter une DEL branchée sur la broche 2 : **Début** ; allumer la DEL branchée sur la broche 2 ; attendre 1 seconde ; éteindre la DEL ; attendre 1 seconde ; recommencer ; **Fin**.

## Les diagrammes SysML

Le **diagramme d'activité** (act) décrit la transformation des flux d'entrée en flux de sortie par des séquences d'**actions** (rectangles à coins arrondis), avec un état initial (disque noir), des nœuds de décision (losanges) portant des **gardes** entre crochets, des barres de synchronisation et un état final. Dès qu'une tâche est terminée, la suivante commence : **aucun événement** n'est associé aux transitions.

{{fig:info-sysml-etats}}

Le **diagramme d'états-transitions** (stm) modélise l'évolution de l'état d'une machine **en fonction des événements**. Les états sont des rectangles à coins arrondis, les transitions des flèches étiquetées par l'événement qui les déclenche. Dans un état, on décrit les activités internes : entry (en entrant), do (tant qu'on y reste), exit (en sortant).

{{fig:info-sysml-sequence}}

Le **diagramme de séquence** (sd) représente les échanges de messages entre les acteurs et le système ; il se lit **de haut en bas**. Chaque bloc possède une **ligne de vie** (trait vertical pointillé) ; les flèches sont les messages (pointe pleine si le message est synchrone, trait pointillé pour une réponse). Trois opérateurs encadrent les séquences particulières : **alt** (conditionnelle), **loop** (répétitive) et **par** (simultanée).
