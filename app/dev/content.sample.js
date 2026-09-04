// content.sample.js — jeu de données de développement (même format que dist/content.js produit par le build).
// Copier vers app/content.js pour tester l'appli sans lancer le build : cp dev/content.sample.js content.js
(function () {
  const svg = (inner) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="120" height="120"><g fill="none" stroke-width="3" stroke-linecap="round">${inner}</g></svg>`;
  const RED = '#d63b2f', BLUE = '#2f5fd6';
  const figures = {
    'liaison-pivot-axe': svg(`<line x1="50" y1="10" x2="50" y2="35" stroke="${RED}"/><circle cx="50" cy="50" r="15" stroke="${BLUE}"/><line x1="50" y1="65" x2="50" y2="90" stroke="${BLUE}"/><text x="58" y="34" font-size="11" fill="#333" stroke="none">A</text>`),
    'liaison-glissiere-axe': svg(`<line x1="50" y1="10" x2="50" y2="35" stroke="${RED}"/><rect x="35" y="35" width="30" height="30" stroke="${BLUE}"/><line x1="35" y1="35" x2="65" y2="65" stroke="${RED}"/><line x1="65" y1="35" x2="35" y2="65" stroke="${RED}"/><line x1="50" y1="65" x2="50" y2="90" stroke="${BLUE}"/><text x="58" y="34" font-size="11" fill="#333" stroke="none">A</text>`),
    'liaison-rotule': svg(`<line x1="50" y1="10" x2="50" y2="36" stroke="${RED}"/><circle cx="50" cy="50" r="14" stroke="${RED}"/><path d="M 31 50 A 19 19 0 0 0 69 50" stroke="${BLUE}"/><line x1="50" y1="69" x2="50" y2="90" stroke="${BLUE}"/><text x="58" y="34" font-size="11" fill="#333" stroke="none">A</text>`),
    'liaison-appui-plan': svg(`<line x1="50" y1="10" x2="50" y2="46" stroke="${RED}"/><line x1="30" y1="46" x2="70" y2="46" stroke="${RED}"/><line x1="15" y1="52" x2="85" y2="52" stroke="${BLUE}"/><line x1="50" y1="52" x2="50" y2="90" stroke="${BLUE}"/><text x="58" y="42" font-size="11" fill="#333" stroke="none">A</text>`),
  };

  const DDL_ROWS = [{ id: 'x', label: 'x' }, { id: 'y', label: 'y' }, { id: 'z', label: 'z' }];
  const DDL_COLS = [{ id: 'T', label: 'Translation' }, { id: 'R', label: 'Rotation' }];
  const ddl = (id, skill, level, nom, answer, explanation, cellFeedback) => ({
    id, skill, type: 'grid', level, tags: [nom.toLowerCase()],
    payload: { prompt: `Coche les degrés de liberté d'une **${nom}**.`, rows: DDL_ROWS, cols: DDL_COLS, answer, explanation, ...(cellFeedback ? { cellFeedback } : {}) },
  });

  const items = [
    // ---- liaisons-mobilites
    { id: 'mob-fc-1', skill: 'liaisons-mobilites', type: 'flashcard', level: 1, tags: ['ddl'], payload: {
      front: 'Combien de mouvements indépendants sont possibles entre deux solides **sans aucun contact** ?',
      back: '**6** : 3 translations (Tx, Ty, Tz) et 3 rotations (Rx, Ry, Rz).' } },
    { id: 'mob-fc-2', skill: 'liaisons-mobilites', type: 'flashcard', level: 1, tags: ['ddl'], payload: {
      front: 'Que désigne la lettre **T** dans la colonne « degrés de liberté » ?',
      back: 'Une **translation** suivant un axe : Tx, Ty ou Tz.' } },
    { id: 'mob-fc-3', skill: 'liaisons-mobilites', type: 'flashcard', level: 2, tags: ['ddl'], payload: {
      front: 'Qu\'est-ce qu\'un **degré de liberté** (ddl) ?',
      back: 'Un mouvement relatif indépendant possible entre deux pièces : une translation le long d\'un axe ou une rotation autour d\'un axe.' } },
    { id: 'mob-math-1', skill: 'liaisons-mobilites', type: 'mcq', level: 1, tags: ['maths'], payload: {
      prompt: 'Un engrenage : roue menante $Z_1 = 20$, roue menée $Z_2 = 60$. Le rapport $R = \\dfrac{\\omega_2}{\\omega_1}$ vaut :',
      choices: ['$R = \\frac{Z_1}{Z_2} = \\frac{1}{3}$', '$R = \\frac{Z_2}{Z_1} = 3$', '$R = Z_1 + Z_2$', '$R = 1$'], answer: [0], multiple: false, layout: 'list',
      feedback: [null, "Non : c'est l'inverse, $R = \\frac{Z_{\\text{menante}}}{Z_{\\text{menée}}}$.", 'Non : on divise, on n\'additionne pas.', 'Non : les roues n\'ont pas le même nombre de dents.'],
      explanation: 'Position en mouvement uniformément varié : $$x(t) = \\tfrac12 a t^2 + v_0 t + x_0$$ (formule affichée pour tester).' } },
    { id: 'mob-mcq-1', skill: 'liaisons-mobilites', type: 'mcq', level: 1, tags: ['notation'], payload: {
      prompt: 'Une rotation autour de l\'axe $\\vec{z}$ se note :', choices: ['Rz', 'Tz', 'Rx', 'Ty'], answer: [0],
      feedback: [null, 'Non : **T** désigne une translation (déplacement en ligne droite), pas une rotation.', 'Non : l\'axe est **z**, pas x.', 'Non : **T** désigne une translation, et l\'axe est z.'],
      explanation: '**R** pour rotation, **z** pour l\'axe autour duquel on tourne.' } },
    { id: 'mob-mcq-3', skill: 'liaisons-mobilites', type: 'mcq', level: 1, tags: ['porte'], payload: {
      prompt: '{{emoji:🚪}} Une **porte** sur ses gonds (axe vertical z). Quel est son seul degré de liberté par rapport au mur ?', choices: ['Rz', 'Tz', 'Rx', 'Ty'], answer: [0],
      feedback: [null, 'Non : la porte ne monte pas et ne descend pas (pas de translation selon z) : elle **tourne**.', 'Non : l\'axe des gonds est **vertical**, c\'est l\'axe z.', 'Non : la porte ne se déplace pas en ligne droite : elle **tourne** autour de ses gonds.'],
      explanation: 'La porte ne peut que tourner autour de l\'axe vertical des gonds : rotation **Rz**.' } },
    { id: 'mob-mcq-2', skill: 'liaisons-mobilites', type: 'mcq', level: 1, tags: ['contact'], payload: {
      prompt: 'Chaque contact entre deux pièces…', choices: ['limite les mobilités', 'ajoute des mobilités', 'ne change rien aux mobilités', 'supprime toujours les 6 mobilités'], answer: [0],
      feedback: [null, 'Non : un contact ne crée jamais de mouvement, il en **empêche**.', 'Non : dès qu\'il y a contact, certains mouvements deviennent impossibles.', 'Non : seul un **encastrement** supprime les 6 mobilités ; les autres liaisons en laissent.'],
      explanation: 'Les surfaces de contact suppriment certains mouvements : ce qui reste définit la liaison.' } },
    { id: 'mob-input-1', skill: 'liaisons-mobilites', type: 'input', level: 1, tags: ['ddl'], payload: {
      prompt: 'Nombre **maximal** de degrés de liberté entre deux solides ?', answer: '6', numeric: true, explanation: '3 translations + 3 rotations.' } },
    { id: 'mob-input-2', skill: 'liaisons-mobilites', type: 'input', level: 2, tags: ['ddl'], payload: {
      prompt: 'Combien de **translations** indépendantes existe-t-il dans l\'espace ?', answer: '3', numeric: true, explanation: 'Une par axe : x, y et z.' } },
    { id: 'mob-order-1', skill: 'liaisons-mobilites', type: 'order', level: 2, tags: ['ddl'], payload: {
      prompt: 'Classe ces situations de la **plus libre** à la **plus contrainte**.',
      steps: ['Deux solides sans contact (6 ddl)', 'Rotule (3 ddl)', 'Pivot (1 ddl)', 'Encastrement (0 ddl)'],
      explanation: 'Plus il y a de contact, moins il reste de degrés de liberté.' } },

    { id: 'mob-guided-1', skill: 'liaisons-mobilites', type: 'guided', level: 3, tags: ['porte', 'ddl'], payload: {
      title: 'La porte : des mobilités à la liaison',
      intro: '{{emoji:🚪}} Une **porte** est fixée au mur par deux gonds d\'axe vertical z. On étudie ses mouvements possibles par rapport au mur, puis on nomme la liaison.',
      steps: [
        { kind: 'mcq', prompt: 'Étape 1 — Combien de mobilités possède un solide **libre** dans l\'espace ?', choices: ['6', '3', '2', '12'], answer: [0],
          feedback: [null, 'Non : il y a 3 translations **et** 3 rotations.', 'Non : 2 ce serait dans un plan ; dans l\'espace il y a 3 axes.', 'Non : 3 axes × 2 types de mouvement = 6.'],
          explanation: '3 translations + 3 rotations = 6 mobilités.' },
        { kind: 'input', prompt: 'Étape 2 — Combien de mobilités la porte **garde-t-elle** par rapport au mur ?', answer: '1', numeric: true,
          explanation: 'Les gonds ne laissent qu\'un mouvement : tourner autour de leur axe.' },
        { kind: 'grid', prompt: 'Étape 3 — Coche la mobilité restante de la porte.', rows: DDL_ROWS, cols: DDL_COLS, answer: ['Rz'],
          cellFeedback: { Tz: 'la porte ne monte pas : les gonds la portent', Rx: 'l\'axe des gonds est vertical (z), pas horizontal', Ty: 'la porte ne se déplace pas en ligne droite' },
          explanation: 'Rotation autour de l\'axe vertical z : **Rz**.' },
        { kind: 'order', prompt: 'Étape 4 — Remets dans l\'ordre le raisonnement qui mène à la liaison.',
          steps: ['Repérer les surfaces de contact (les gonds)', 'En déduire les mouvements bloqués', 'Compter les mobilités restantes', 'Nommer la liaison : pivot d\'axe (A, z)'],
          explanation: 'Contact → mouvements bloqués → degrés de liberté → nom de la liaison.' },
      ] } },
    // ---- liaisons-symboles
    { id: 'sym-mcq-grid-1', skill: 'liaisons-symboles', type: 'mcq', level: 1, tags: ['pivot'], payload: {
      prompt: 'Quel symbole représente une **liaison pivot** (vue selon l\'axe) ?', layout: 'grid',
      choices: ['{{fig:liaison-pivot-axe}}', '{{fig:liaison-glissiere-axe}}', '{{fig:liaison-rotule}}', '{{fig:liaison-appui-plan}}'], answer: [0],
      explanation: 'Vue selon son axe, la pivot est un **cercle** : la pièce rouge tourne dans la pièce bleue.' } },
    { id: 'sym-mcq-grid-2', skill: 'liaisons-symboles', type: 'mcq', level: 1, tags: ['glissiere'], payload: {
      prompt: 'Quel symbole représente une **liaison glissière** (vue selon l\'axe) ?', layout: 'grid',
      choices: ['{{fig:liaison-pivot-axe}}', '{{fig:liaison-glissiere-axe}}', '{{fig:liaison-rotule}}', '{{fig:liaison-appui-plan}}'], answer: [1],
      explanation: 'Un **carré barré d\'une croix** : le coulisseau glisse le long de l\'axe qui pointe vers toi.' } },
    { id: 'sym-mcq-grid-3', skill: 'liaisons-symboles', type: 'mcq', level: 2, tags: ['rotule'], payload: {
      prompt: 'Quel symbole représente une **liaison rotule** ?', layout: 'grid',
      choices: ['{{fig:liaison-pivot-axe}}', '{{fig:liaison-glissiere-axe}}', '{{fig:liaison-rotule}}', '{{fig:liaison-appui-plan}}'], answer: [2],
      explanation: 'Une **sphère** (cercle) dans une **coupelle** (arc) : 3 rotations possibles.' } },
    { id: 'sym-mcq-1', skill: 'liaisons-symboles', type: 'mcq', level: 1, tags: ['pivot'], payload: {
      prompt: '{{fig:liaison-pivot-axe}}\nQuelle est cette liaison ?', choices: ['Pivot', 'Glissière', 'Rotule', 'Appui plan'], answer: [0],
      explanation: 'Le cercle vu selon l\'axe est le symbole de la **pivot**.' } },
    { id: 'sym-mcq-2', skill: 'liaisons-symboles', type: 'mcq', level: 1, tags: ['glissiere'], payload: {
      prompt: '{{fig:liaison-glissiere-axe}}\nQuelle est cette liaison ?', choices: ['Pivot', 'Glissière', 'Rotule', 'Appui plan'], answer: [1],
      explanation: 'Le carré avec une croix est la **glissière** vue selon son axe.' } },
    { id: 'sym-match-1', skill: 'liaisons-symboles', type: 'match', level: 1, tags: ['symboles'], payload: {
      prompt: 'Associe chaque symbole à son nom.',
      pairs: [
        { left: '{{fig:liaison-pivot-axe}}', right: 'Pivot' },
        { left: '{{fig:liaison-glissiere-axe}}', right: 'Glissière' },
        { left: '{{fig:liaison-rotule}}', right: 'Rotule' },
        { left: '{{fig:liaison-appui-plan}}', right: 'Appui plan' },
      ] } },
    { id: 'sym-match-2', skill: 'liaisons-symboles', type: 'match', level: 2, tags: ['parametrage'], payload: {
      prompt: 'Associe chaque liaison à la façon dont on la **paramètre**.',
      pairs: [
        { left: 'Pivot', right: 'd\'axe (A, x)' },
        { left: 'Rotule', right: 'de centre A' },
        { left: 'Appui plan', right: 'de normale (A, y)' },
      ] } },
    { id: 'sym-fc-1', skill: 'liaisons-symboles', type: 'flashcard', level: 2, tags: ['rotule'], payload: {
      front: '{{fig:liaison-rotule}}', back: '**Rotule** de centre A : la sphère rouge tourne librement dans la coupelle bleue (3 rotations).' } },
    { id: 'sym-input-1', skill: 'liaisons-symboles', type: 'input', level: 2, tags: ['helicoidale'], payload: {
      prompt: 'Comment s\'appelle la liaison entre une **vis** et un **écrou** ?', answer: 'hélicoïdale', accept: ['liaison hélicoïdale', 'helicoidale'],
      explanation: 'La liaison **hélicoïdale** : la translation et la rotation sont liées par le pas de la vis.' } },

    // ---- liaisons-ddl
    ddl('ddl-grid-1', 'liaisons-ddl', 1, 'liaison pivot d\'axe (A, x)', ['Rx'], 'Une pivot ne laisse qu\'**une rotation** autour de son axe.',
      { Tx: 'la translation le long de l\'axe est bloquée par les épaulements', Ty: 'l\'arbre ne peut pas sortir de son alésage', Rx: 'c\'est la rotation autour de l\'axe, la seule mobilité du pivot', Ry: 'l\'alésage long empêche l\'arbre de basculer' }),
    ddl('ddl-grid-2', 'liaisons-ddl', 1, 'liaison glissière d\'axe (A, x)', ['Tx'], 'Une glissière ne laisse qu\'**une translation** le long de son axe.'),
    ddl('ddl-grid-3', 'liaisons-ddl', 1, 'liaison rotule de centre A', ['Rx', 'Ry', 'Rz'], 'Une rotule laisse les **trois rotations** et bloque les trois translations.'),
    ddl('ddl-grid-4', 'liaisons-ddl', 2, 'liaison appui plan de normale (A, y)', ['Tx', 'Tz', 'Ry'], 'On glisse dans le plan (Tx, Tz) et on tourne autour de la normale (Ry).'),
    ddl('ddl-grid-5', 'liaisons-ddl', 2, 'liaison pivot glissant d\'axe (A, x)', ['Tx', 'Rx'], 'Comme un piston : translation **et** rotation indépendantes le long de l\'axe.'),
    { id: 'ddl-mcq-1', skill: 'liaisons-ddl', type: 'mcq', level: 1, tags: ['rotule'], payload: {
      prompt: 'Combien de degrés de liberté possède une liaison **rotule** ?', choices: ['3', '1', '2', '0'], answer: [0],
      explanation: 'Trois rotations, aucune translation.' } },
    { id: 'ddl-match-1', skill: 'liaisons-ddl', type: 'match', level: 2, tags: ['ddl'], payload: {
      prompt: 'Associe chaque liaison à son nombre de degrés de liberté.',
      pairs: [
        { left: 'Encastrement', right: '0' }, { left: 'Pivot', right: '1' }, { left: 'Pivot glissant', right: '2' },
        { left: 'Rotule', right: '3' }, { left: 'Ponctuelle', right: '5' },
      ] } },
    { id: 'ddl-input-1', skill: 'liaisons-ddl', type: 'input', level: 3, tags: ['ponctuelle'], payload: {
      prompt: 'Nombre de degrés de liberté d\'une liaison **ponctuelle** ?', answer: '5', numeric: true,
      explanation: 'Seule la translation suivant la normale au contact est bloquée : 6 − 1 = 5.' } },
    { id: 'ddl-fc-1', skill: 'liaisons-ddl', type: 'flashcard', level: 3, tags: ['efforts'], payload: {
      front: 'Degrés de liberté + composantes d\'effort transmissibles = ?',
      back: '**6**, toujours : ce que la liaison ne laisse pas bouger, elle le transmet (force ou moment).' } },

    // ---- schema-demarche
    { id: 'dem-order-1', skill: 'schema-demarche', type: 'order', level: 1, tags: ['demarche'], payload: {
      prompt: 'Remets dans l\'ordre les **5 étapes** de la démarche pour tracer un schéma cinématique.',
      steps: [
        'Étudier le dessin d\'ensemble pour comprendre le fonctionnement',
        'Identifier les classes d\'équivalence cinématique (colorier)',
        'Identifier la nature des contacts et en déduire les liaisons',
        'Tracer le graphe des liaisons',
        'Tracer le schéma cinématique 2D ou 3D',
      ],
      explanation: 'Comprendre → colorier → contacts → graphe → schéma.' } },
    { id: 'dem-order-2', skill: 'schema-demarche', type: 'order', level: 1, tags: ['demarche'], payload: {
      prompt: 'Dans quel ordre fait-on ces trois choses ?',
      steps: ['Identifier les classes d\'équivalence', 'Identifier la nature des contacts entre classes', 'Tracer le graphe des liaisons'],
      explanation: 'Le graphe relie les classes par les liaisons déduites des contacts.' } },
    { id: 'dem-mcq-1', skill: 'schema-demarche', type: 'mcq', level: 1, tags: ['serre-joint'], payload: {
      prompt: 'Dans le **serre-joint**, la vis et l\'écrou (filetage/taraudage) forment une liaison…', choices: ['Hélicoïdale', 'Pivot', 'Glissière', 'Rotule'], answer: [0],
      explanation: 'Un contact filetage/taraudage donne toujours une liaison **hélicoïdale**.' } },
    { id: 'dem-fc-1', skill: 'schema-demarche', type: 'flashcard', level: 1, tags: ['classes'], payload: {
      front: 'Que fait-on des pièces **déformables** (ressorts, joints) dans les classes d\'équivalence ?',
      back: 'On les **exclut** de toute classe d\'équivalence.' } },
    { id: 'dem-input-1', skill: 'schema-demarche', type: 'input', level: 2, tags: ['serre-joint'], payload: {
      prompt: 'Combien de **classes d\'équivalence** compte le serre-joint étudié (E1 = {1, 2, 3}, E2 = {4}, E3 = {5, 6}, E4 = {7}) ?', answer: '4', numeric: true,
      explanation: 'E1 à E4 : quatre classes.' } },
  ];

  const byId = {};
  for (const it of items) byId[it.id] = it;
  const idsOf = (skill) => items.filter((it) => it.skill === skill).map((it) => it.id);

  window.CONTENT = {
    version: 1,
    generatedAt: '2026-09-04T09:00:00Z',
    title: 'Révise STI2D',
    figures,
    units: [
      {
        id: 'liaisons',
        title: 'Les liaisons mécaniques',
        description: 'Reconnaître les 10 liaisons normalisées, leurs symboles et leurs degrés de liberté.',
        skills: [
          {
            id: 'liaisons-mobilites', title: 'Les 6 mobilités', icon: '🧭',
            description: 'Translations, rotations et degrés de liberté.', prerequisites: [], levels: 2,
            lesson: `# Les six mobilités
Deux solides **sans aucun contact** peuvent bouger l'un par rapport à l'autre de **6** façons indépendantes :

- en **translation** suivant chacun des 3 axes : Tx, Ty, Tz ;
- en **rotation** autour de chacun des 3 axes : Rx, Ry, Rz.

Ces mouvements sont les **degrés de liberté** (ddl). Chaque contact entre deux pièces *supprime* des ddl : ce qui reste définit la **liaison**.

## Formules utiles (test KaTeX)

| Grandeur | Formule | Unité |
|---|---|---|
| Vitesse d'un point en rotation | $v = R \\omega$ | m/s |
| Puissance | $P = C \\times \\omega$ | W |
| Rapport de transmission | $R = \\dfrac{Z_{\\text{menante}}}{Z_{\\text{menée}}}$ | sans unité |

Position en mouvement uniformément varié :

$$x(t) = \\tfrac{1}{2} a t^2 + v_0 t + x_0$$

- conversion : $\\omega = N \\times \\dfrac{2\\pi}{60}$ (N en tr/min)

| Mouvement | Notation |
|---|---|
| Translation suivant $\\vec{x}$ | Tx |
| Rotation autour de $\\vec{x}$ | Rx |

## Un algorithme (test des blocs de code)

Le pseudo-code d'un capteur de fin de course, avec du \`code en ligne\` :

\`\`\`
DEBUT
  SI capteur = 1 ALORS
    moteur <- ARRET   # le $ et {{fig:pivot}} restent tels quels ici : $x$
  SINON
    moteur <- MARCHE
  FIN SI
FIN
\`\`\`
`,
            items: idsOf('liaisons-mobilites'),
          },
          {
            id: 'liaisons-symboles', title: 'Reconnaître les symboles', icon: '🔩',
            description: 'Les symboles normalisés des liaisons en vue plane.', prerequisites: ['liaisons-mobilites'], levels: 3,
            lesson: `# Les symboles des liaisons
Chaque liaison a un symbole normalisé. En **2D**, il dépend de la vue (selon l'axe ou perpendiculairement à l'axe).

{{fig:liaison-pivot-axe}}

- **Pivot** : un cercle (vue selon l'axe).
- **Glissière** : un carré barré d'une croix.
- **Rotule** : une sphère dans une coupelle.
- **Appui plan** : deux traits parallèles.`,
            items: idsOf('liaisons-symboles'),
          },
          {
            id: 'liaisons-ddl', title: 'Degrés de liberté', icon: '🎚️',
            description: 'Retrouver les mobilités de chaque liaison.', prerequisites: ['liaisons-symboles'], levels: 3,
            lesson: `# Degrés de liberté des liaisons
On note **T** une translation et **R** une rotation, indicées par l'axe. Une liaison est décrite par les mobilités qu'elle **laisse**.

| Liaison | ddl |
|---|---|
| Encastrement | 0 |
| Pivot | Rx |
| Glissière | Tx |
| Pivot glissant | Tx, Rx |
| Rotule | Rx, Ry, Rz |
| Appui plan (normale y) | Tx, Tz, Ry |

Règle : **ddl + efforts transmissibles = 6**.`,
            items: idsOf('liaisons-ddl'),
          },
        ],
      },
      {
        id: 'schema',
        title: 'Le schéma cinématique',
        description: 'Passer du mécanisme réel au schéma : classes d\'équivalence, graphe des liaisons, schéma.',
        skills: [
          {
            id: 'schema-demarche', title: 'La démarche en 5 étapes', icon: '📐',
            description: 'Du dessin d\'ensemble au schéma cinématique.', prerequisites: ['liaisons-ddl'], levels: 2,
            lesson: `# La démarche
1. Étudier le dessin d'ensemble.
2. Identifier les **classes d'équivalence** (une couleur chacune ; pièces déformables exclues).
3. Identifier la nature des **contacts** → liaisons.
4. Tracer le **graphe des liaisons**.
5. Tracer le **schéma cinématique** (2D ou 3D).`,
            items: idsOf('schema-demarche'),
          },
        ],
      },
    ],
    items: byId,
    annales: [
      { id: 'demo-2024', titre: 'Bac 2024 — 2I2D, métropole (démo)', session: '2024', epreuve: '2I2D', partie: 'Partie commune, exercice 1 : porte automatique',
        url: 'https://eduscol.education.fr/', corrige: null, themes: ['mobilités', 'liaisons'], prerequis: [{ skill: 'liaisons-mobilites', level: 1 }], guided: 'mob-guided-1' },
      { id: 'demo-2023', titre: 'Bac 2023 — 2I2D, Polynésie (démo)', session: '2023', epreuve: '2I2D', partie: 'Partie commune, exercice 2 : schéma cinématique',
        url: 'https://eduscol.education.fr/', corrige: 'https://eduscol.education.fr/', themes: ['schéma cinématique', 'statique'], prerequis: [{ skill: 'schema-demarche', level: 2 }], guided: null },
    ],
  };
})();
