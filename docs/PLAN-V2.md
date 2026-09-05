# Plan V2 — un moteur, des paquets de contenu, un index public

État : plan arrêté le 5 septembre 2026, rien n'est encore fait. Décisions prises avec Robin :
**deux dépôts dès maintenant** (moteur / contenu), **mémoire locale + carte d'identité exportable**
(pas de serveur), **la bibliothèque de figures élargit `bachelor_intro_to_energy_figures`**.

Ce fichier est la référence : l'ordre de travail est en §7, et chaque section dit ce qui bouge et
pourquoi. `docs/REPRISE.md` reste la fiche d'entrée d'une session ; ce plan la complète.

---

## 0. Ce qui existe déjà et qu'on ne réinvente pas

Trois patrons sont déjà en service chez Robin et servent de modèle :

| Existant | Ce qu'il nous donne |
|---|---|
| **The Net Zero Game** (`Code/Etude/The-net-zero-game`) | Publication en dossiers de version figés sous `assets/netzerogame/vX.Y/`, un `latest/` ; `app/publish.py` **copie dans le site sans commiter ni pousser** — Robin relit le diff avant que ça devienne une URL. Retours par `mailto:` **portant le contexte** (version, scénario, chiffres) pour que le rapport soit reproductible. |
| **`bachelor_intro_to_energy_figures`** (git.persee) | Une bibliothèque de figures qui existe déjà : manifeste `figures.yml` (famille, code, commande de rebuild, données et leur accès), `publish_page.py` qui **engendre** la page catalogue du site, double licence MIT / CC BY 4.0, règle « aucune donnée tierce redistribuée ». |
| **`Teaching.md` / `Enseignement.md`** du site | L'index demandé existe déjà en germe : une section « Interactive tools », la promesse « tout tourne chez vous, rien n'est envoyé », et la licence annoncée (CC BY 4.0 contenu, MIT code). Il n'y a pas d'index à inventer : il y a un troisième outil à y ajouter. |

Côté révise, l'état utile au découpage :

- 19 unités, 2 058 exercices, 84 compétences, 296 figures ; `dist/content.js` ≈ 2,5 Mo.
- Poids du contenu par matière : **ingénierie 1 258 ko (59 %)**, physique 505 ko (24 %), maths 361 ko (17 %).
- Les unités portent déjà un champ `matiere`, et les figures sont **déjà** chargées à la demande
  (`figureIndex` + `dist/figures/`). Le gros bloc restant est le texte des exercices.
- Le moteur fait 2 310 lignes de JS ; les outils Python 2 104 lignes, dont `build_content.py` 1 346.
- **Les 39 générateurs d'exercices sont tous spécifiques aux liaisons et aux mécanismes**, et une
  seule unité (`content/units.yaml`, 13 compétences) les utilise : toutes les autres unités écrivent
  leurs exercices explicitement. Ils n'appartiennent donc pas au moteur — c'est un point structurant.

---

## 1. Deux dépôts : `revise-core` et les paquets de contenu

### Ce que devient chaque dépôt

**`revise-core`** — le moteur, sans aucune connaissance d'une matière. Licence MIT.

```
revise-core/
  app/                      moteur : js/, css/, index.html, sw.js, manifest, vendor/katex
  revise/                   paquet Python : assemblage du contenu, compilation des figures,
                            validation du schéma générique, serveur de dev
  schema/                   le schéma d'un paquet de contenu (unités, compétences, exercices,
                            leçons, figures) — ce que le moteur sait lire
  tests/                    les 88 tests actuels + ceux du schéma
  CHANGELOG.md              versions du moteur (semver)
```

**`revise-sti2d`** (le dépôt actuel, vidé de son moteur) — un paquet de contenu. Licence CC BY 4.0.

```
revise-sti2d/
  pack.yaml                 manifeste : id, titre, matières, niveau, version, licence,
                            version de moteur requise, contact pour les retours
  content/                  units.yaml, units/, lessons/, liaisons.yaml, mecanismes/, annales.yaml
  generators/               les 39 générateurs liaisons/mécanismes — greffon du paquet, pas du moteur
  figures/tikz/             sources TikZ propres au paquet
  Makefile                  appelle le moteur ; ne contient aucune logique
```

### Comment un paquet consomme le moteur

Le moteur est **embarqué à la construction**, pas chargé depuis une URL : chaque site publié reste
un dossier autonome qui marche hors ligne, comme netzero. Concrètement :

- le paquet déclare `moteur: ">=1.2 <2"` dans `pack.yaml` ;
- `make` récupère la version épinglée du moteur (tag git, ou `pip install revise-core==1.2.3` pour
  la partie Python et une copie de `app/` pour la partie navigateur), construit, et **inscrit la
  version exacte du moteur dans le `dist/`** (visible dans la page « À propos ») ;
- si le paquet demande une version que le moteur ne fournit pas, le build échoue au lieu de
  produire un site subtilement cassé.

Le coût de ce choix est réel : toute évolution du moteur demande une version et une republication
des paquets. C'est le prix de pouvoir donner le moteur à quelqu'un d'autre — ce que le choix
« deux dépôts dès maintenant » vise explicitement.

### Ce qui doit être tranché avant de découper

- **Licence et droits.** Le dépôt actuel n'a aucun fichier `LICENSE`, alors que le site annonce
  déjà MIT + CC BY 4.0 pour les autres outils. À ajouter des deux côtés.
- **Droits d'auteur du contenu.** `docs/notes/` (transcriptions des deux manuels) est ignoré par git
  pour cette raison — mais le dépôt est public (GitHub Pages le sert). Avant d'en faire un paquet
  affiché comme réutilisable, il faut **une passe de relecture** : aucun énoncé ne doit être repris
  d'un manuel, les annales sont référencées par lien et non recopiées. C'est déjà la règle suivie
  (les guidés tirés d'annales ont été réécrits avec d'autres valeurs) ; il s'agit de le vérifier et
  de l'écrire noir sur blanc dans le paquet.

---

## 2. Le contenu découpé par matière, chargé à la demande

Le grief de départ — « des circuits indépendants dans le même HTML statique » — se règle en deux
temps, et le second est aussi la dette technique déjà notée (2,5 Mo au premier chargement mobile).

1. **Un fichier par unité.** `content.js` devient :
   - `content-index.js` : matières, unités, compétences, titres, prérequis, compte d'exercices —
     tout ce qu'il faut pour dessiner l'accueil et la carte de progression (quelques dizaines de ko) ;
   - `content/<unite>.js` : les exercices et les leçons de cette unité, chargés quand on l'ouvre.

   Gain attendu : premier chargement divisé par dix environ, et une matière ne fait plus payer les
   autres. Les figures sont déjà à la demande, il n'y a rien à changer de ce côté.

2. **Un site par paquet, ou un site multi-paquets.** Le moteur lit une liste de paquets : publier
   `revise-sti2d` seul ou publier « STI2D + collège + … » sous un même toit devient un paramètre du
   build, pas une refonte. C'est ce qui rend le point 4 (l'index) extensible sans travail.

L'accueil par matière existe déjà ; il devient l'écran qui liste les paquets installés.

---

## 3. Profils et carte d'identité

Décision : **tout reste sur la machine de l'élève**, aucune donnée d'un mineur ne part ailleurs.
C'est aussi ce que le site promet déjà pour les autres outils.

- **Plusieurs profils par navigateur.** Aujourd'hui la progression vit sous une seule clé
  (`revise-sti2d.progress.v1`). Elle devient `revise.profil.<id>`, plus un index des profils
  (nom, emoji, date de dernière séance) et un profil courant. Deux élèves sur la même machine
  choisissent leur profil à l'ouverture.
- **La carte d'identité.** Un seul fichier JSON par élève, couvrant **toutes** les matières et tous
  les paquets : identité (un prénom choisi, rien d'autre), résultats par compétence, historique,
  série en cours. `store.js` sait déjà exporter et importer ce format — il faut l'étendre aux
  profils et lui donner un numéro de version stable, car ce fichier va devenir le format d'échange.
- **Voyager d'une machine à l'autre.** Trois moyens, par ordre de fiabilité, et il faut être franc
  sur leurs limites :
  1. **le fichier** (téléchargé, envoyé par mail ou AirDrop, réimporté) — marche toujours ;
  2. **un lien** contenant la carte compressée dans le fragment d'URL — pratique, mais seulement
     tant que la carte est petite : un élève qui a vu 300 exercices tient dans quelques ko, un élève
     qui a tout parcouru non. Le bouton doit donc mesurer avant de proposer ;
  3. **un QR code** — même compression, plafond dur autour de 2,9 ko : à ne proposer que quand ça
     rentre, jamais comme moyen principal. Promettre un QR pour toute progression serait mentir.
- **Ce qu'on ne fait pas** : de comptes serveur. Ils apporteraient la synchro automatique, mais des
  données scolaires de mineurs, le RGPD et le consentement parental, un coût et une maintenance —
  pour un besoin (deux machines, deux élèves) que le fichier couvre.

---

## 4. Publication et index sur robingirard.eu

On suit le patron netzero à la lettre, il a déjà fait ses preuves :

- les sites construits vont dans `assets/revise/<paquet>/vX.Y/` avec un `latest/` ; **chaque version
  mineure garde son lien permanent**, pour qu'un lien donné à une classe continue d'ouvrir la
  version sur laquelle le travail a été fait ;
- un `publish.py` **copie dans l'arbre du site et s'arrête** : ni commit ni push, Robin relit ;
- une page dédiée `Revise.md` (en français, c'est un contenu de programme français), liée depuis
  `Teaching.md` **et** `Enseignement.md`, qui devient l'index demandé : une entrée par matière et
  par niveau, avec ce que ça couvre, le nombre d'exercices, la licence et le lien de la version
  courante. Quand un deuxième paquet arrive, c'est une ligne de plus, engendrée depuis les
  `pack.yaml` plutôt qu'écrite à la main — même principe que `figures.yml` → page catalogue.

---

## 5. Les retours des utilisateurs

Le mécanisme est celui de netzero, appliqué au grain de l'exercice :

- **un bouton « Signaler »** sur un exercice, une leçon ou une figure, qui ouvre un `mailto:` déjà
  rempli avec ce qui rend le rapport exploitable : identifiant de l'exercice, unité et compétence,
  version du paquet et du moteur, la réponse donnée et celle attendue, le nom de la figure affichée.
  Sans ce contexte, « il y a une erreur dans un exercice de maths » est inexploitable ;
- **une page « Comment c'est fait »**, dans l'application et sur le site, qui dit franchement que
  l'essentiel a été écrit avec Claude, que cela vaut pour la justesse scientifique comme pour
  l'ergonomie, et que **la critique des utilisateurs est le mécanisme de correction prévu**, pas un
  service après-vente. La formulation de netzero est le bon ton : « si un chiffre vous paraît faux,
  c'est une contribution ».
- Les retours arrivent par mail à `robin.girard@minesparis.psl.eu`, comme pour netzero.

---

## 6. La bibliothèque de figures

Décision : **élargir `bachelor_intro_to_energy_figures`** plutôt que créer un dépôt de plus. Il a
déjà tout ce qu'il faut, il change simplement de statut : de « figures d'un cours » à
« bibliothèque de figures, classée par domaine ».

- **Manifeste.** `figures.yml` gagne un niveau de classement (domaine → famille → figure) et, par
  figure, les mots-clés et le contexte d'usage. Le manifeste reste la seule source de vérité :
  la page du site en est une vue engendrée, jamais écrite à la main.
- **Ce qui entre.** Les 296 figures de révise (symboles de liaisons, schémas cinématiques animés,
  mécanismes, figures de physique et de maths), les figures du Bachelor déjà là, et les autres
  projets au fil de l'eau. Les figures de révise apportent quelque chose que le dépôt n'a pas
  encore : **l'animation** (`data-anim`, `data-axial`, `data-mech`), qui doit être documentée comme
  une convention de la bibliothèque, pas comme un détail de révise.
- **Formats.** Chaque figure disponible en SVG (celui qui sert dans l'application), PDF (pour LaTeX
  et l'impression) et PNG (pour PowerPoint) — la chaîne actuelle produit déjà PDF et SVG, le PNG
  est un `pdftocairo` de plus.
- **Page catalogue.** `publish_page.py` engendre une page classée, avec vignette, licence, commande
  de reconstruction et lien de téléchargement par format. Les figures animées s'y affichent animées.
- **Attention au poids.** `figures/` pèse 26 Mo dans révise. La page du Bachelor ne publie que
  3,3 Mo d'images dans le site « assez léger pour vivre dans le dépôt du site » — au-delà, il faudra
  décider ce qui est publié en vignette et ce qui se télécharge depuis le dépôt.

---

## 7. Ordre de travail proposé

Chaque étape est autonome et laisse l'application en état de marche. Les deux premières se
tiennent : découper le contenu avant de séparer les dépôts évite de déplacer deux fois les mêmes
fichiers.

| # | Étape | Pourquoi d'abord | Débloque |
|---|---|---|---|
| 1 | **Découper `content.js` par unité** (§2.1) | Purement interne, aucun risque, gain immédiat sur le téléphone | la notion de paquet |
| 2 | **Profils + carte d'identité** (§3) | Ne dépend de rien, et c'est le besoin le plus concret (deux élèves, deux machines) | l'usage par d'autres que son fils |
| 3 | **Sortir le moteur** (§1) : `revise-core` + `revise-sti2d` comme paquet, générateurs devenus greffon, licences | C'est la grosse pièce ; les étapes 1 et 2 la rendent mécanique | un deuxième paquet, l'open source |
| 4 | **Retours par mail** (§5) + page « Comment c'est fait » | Court, et il vaut mieux qu'il soit là **avant** que le public arrive | la boucle de correction |
| 5 | **Publication et index sur le site** (§4) | Dernier maillon : ce qui rend le reste visible | les niveaux et matières suivants |
| 6 | **Bibliothèque de figures** (§6) | Indépendante du reste, peut se faire en parallèle ou plus tard | la réutilisation hors révise |

Une passe de relecture des droits (§1) doit être faite **avant l'étape 5**, pas après.

---

## 8. Risques et points de vigilance

- **Le cache du service worker.** Chaque publication doit incrémenter `VERSION` dans `app/sw.js`,
  sinon les téléphones déjà à jour gardent l'ancienne version. Déjà rencontré le 5 septembre. Avec
  plusieurs paquets publiés au même endroit, la portée du service worker devra être vérifiée site
  par site.
- **La double copie moteur/paquet.** Un moteur embarqué à la construction veut dire que corriger un
  bug du moteur oblige à republier tous les paquets. À accepter en connaissance de cause, et à
  outiller (une commande qui reconstruit et republie tous les paquets).
- **Le contenu et les manuels.** Voir §1 : à vérifier avant toute mise en avant publique.
- **La dérive plan / réalité.** Ce fichier vaut par sa mise à jour : chaque étape faite se coche
  ici, sinon il redevient un souhait.
