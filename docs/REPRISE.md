# Reprise du travail (état au 4 sept. 2026, fin de la 3e session)

## Publié (gh-pages, commit 2b63708)
13 unités, 1 076 exercices, 170 figures, 3 mécanismes animés, figures de transmission/transformation animées.

## Écrit sur le disque, validé, PAS ENCORE PUBLIÉ (commits 424e130 → HEAD)
- 4 unités 2I2D Tle : `content/units/100-2i2d-fonctionnel.yaml` (107 ex.), `110-2i2d-energie.yaml` (105),
  `120-2i2d-batiment.yaml` (111), `130-2i2d-structures.yaml` (113) + leçons `content/lessons/2i2d-*.md`
  + fiches `docs/figures-todo-2i2d-*.md`.
- Unité information complétée (143 ex., compétence `info-transmission`, 6 guidés) ; figures info-* dessinées.
- 39 exercices guidés ajoutés dans units.yaml, 10-statique-rdm, 30-maths-1re, 40/50/60/70/80/90-pc
  (fiches `docs/figures-todo-guides-{meca,maths,pc1,pc2}.md`).
- 3 mécanismes animés nouveaux : `content/mecanismes/{pompe-a-main,essuie-glace,benne-verin}.yaml`
  + figures `mecanisme-*` (compilent, 0 erreur) ; mouvements `rocker`/`aim`/`offset` dans `app/js/mech-anim.js`.
- `docs/notes/maths-tle-programme.md` (gitignoré, local) : programme officiel de maths Tle (spécialité PCM),
  épreuve, 5 sujets APMEP 2023-2026 avec URL (§ 6), découpage en 6 compétences.
- `tools/build_content.py` : id des guidés dérivé du titre (plusieurs guidés par compétence possibles).

## En cours au moment de l'arrêt (agents tués par la fin de session : vérifier ce qui existe sur le disque)
- Figures TikZ des fiches : `docs/figures-todo-2i2d-fonctionnel.md` (12), `-2i2d-energie.md` (11 + rendements
  partagée), `-2i2d-batiment.md` (10), `-2i2d-structures.md` (13), `-guides-meca.md` (7) + `-guides-maths.md` (5),
  `-guides-pc1.md` (6) + `-guides-pc2.md` (7). Pour chacune : `python3 tools/check_unit.py <unité> <fiche>`
  → « manquantes » = figures à (re)dessiner (agent `complex-figure-builder`, sans droit de lancer d'agents).
- Unité maths Tle : `content/units/35-maths-tle.yaml` + `content/lessons/maths-tle-*.md` +
  `docs/figures-todo-maths-tle.md` (agent `section-writer` d'après la note ci-dessus) : si le fichier est absent
  ou incomplet, relancer l'agent avec le même brief (6 compétences M1-M6 de la note, pas de probabilités).

## Pour reprendre (dans l'ordre)
1. `git status` ; `make figures` ; pour chaque unité nouvelle/modifiée : `python3 tools/check_unit.py …` ;
   relancer des agents figures uniquement pour les « manquantes ».
2. `make content` (échoue tant qu'une figure référencée manque) → `make check` → `make test`
   (`cd app && node --test tests/*.test.mjs`).
3. Animations des 3 mécanismes : `node app/dev/mech-bench.mjs mecanisme-pompe-a-main-schema,mecanisme-essuie-glace-schema,mecanisme-benne-verin-schema <dossier>`
   → regarder les 4 captures (centres, sens, courses dans les guides).
4. Annales : ajouter dans `content/annales.yaml` les 5 sujets PCM du § 6 de la note maths (URL APMEP sujet +
   corrigé, thèmes, `prerequis` sur les compétences maths-tle), puis `make content`.
5. `node app/dev/tour.mjs dist <dossier>` (captures de l'appli), incrémenter `VERSION` dans `app/sw.js`,
   `git commit`, `make deploy`, vérifier le site.
6. Mémoire : `~/.claude/projects/-Users-rgirard-Documents-Enseignement-STI2D/memory/project-revise-sti2d.md`.

## Idées suivantes
Tronc commun de maths Tle (§ 4 de la note), symboles 3D, autres mécanismes, relecture des « à vérifier ».
