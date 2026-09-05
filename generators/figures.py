"""Figures propres au paquet STI2D : sources TikZ engendrées et animations déclarées.

Le moteur (`tools/build_figures.py`) sait compiler du TikZ en SVG et poser les conventions
d'animation que le CSS et `app/js/mech-anim.js` savent lire. Il ne sait pas **quelles** figures
existent ni **comment** elles bougent : c'est ce module qui le lui dit.

Ce que ce paquet apporte :
  - un `.tex` par vue de chaque liaison, engendré depuis `content/liaisons.yaml`, plus les figures
    de mobilités et la planche récapitulative imprimable ;
  - pour chaque figure de symbole, le mouvement visible dans le plan et la translation le long de
    l'axe de visée (lus dans `liaisons.yaml`) ;
  - pour chaque schéma cinématique, la couleur de chaque classe d'équivalence, qui permet au moteur
    de regrouper les tracés (lue dans `content/mecanismes/*.yaml` et `content/animations.yaml`).

La palette vit ici et non dans le moteur : ce sont les couleurs que `figures/tikz/liaisons.sty`
déclare, donc une convention de dessin de ce paquet. Un autre paquet dessinerait autrement, et le
moteur n'a pas à connaître « solideA ».

Le contrat attendu par le moteur est la fonction `figures()` en fin de fichier.
"""
from pathlib import Path

SYMBOL_TEMPLATE = r"""%% Engendré par generators/figures.py — ne pas modifier à la main.
\documentclass[tikz,border=2pt]{standalone}
\usepackage{liaisons}
\begin{document}
\begin{tikzpicture}[x=1cm,y=1cm]
  \useasboundingbox (-1.3,-1.05) rectangle (1.3,1.3);
  \repere{(0,0)}{%(h)s}{%(v)s}{%(sens)d}
  \pic[%(opts)s] at (0,0) {%(pic)s};
  \node[font=\small, anchor=south west, inner sep=1.5pt] at (0.1,0.12) {A};
\end{tikzpicture}
\end{document}
"""

MOBILITE_TEMPLATE = r"""%% Engendré par generators/figures.py — ne pas modifier à la main.
\documentclass[tikz,border=4pt]{standalone}
\usepackage{liaisons}
\begin{document}
\begin{tikzpicture}[x=1cm,y=1cm]
\definecolor{trans}{RGB}{40,110,200}\definecolor{rot}{RGB}{60,160,60}
\newcommand\axe[4]{%%
  \begin{scope}[rotate=#1]
    \draw[dashed, line width=0.5pt] (0,0) -- (2.5,0);
    \draw[-{Stealth[length=6pt]}, line width=0.6pt] (2.5,0) -- (3.2,0) node[pos=1, anchor=180+#1, inner sep=2pt, font=\small] {$\vec{#2}$};
    \ifnum#3=1 \draw[-{Stealth[length=8pt]}, line width=2.2pt, trans] (0.6,0.16) -- (2.0,0.16) node[pos=1, anchor=270+#1, inner sep=3pt, font=\bfseries, text=trans] {%(labelT)s}; \fi
    \ifnum#4=1 \draw[-{Stealth[length=8pt]}, line width=2pt, rot] (2.05,-0.5) arc (-90:190:0.16 and 0.5) node[pos=1, anchor=90+#1, inner sep=4pt, font=\bfseries, text=rot] {%(labelR)s}; \fi
  \end{scope}}
\axe{90}{z}{%(Tz)d}{%(Rz)d}
\axe{-150}{x}{%(Tx)d}{%(Rx)d}
\axe{-30}{y}{%(Ty)d}{%(Ry)d}
\fill (0,0) circle (1.2pt);
\end{tikzpicture}
\end{document}
"""

PLANCHE_HEAD = r"""%% Engendré par generators/figures.py — planche récapitulative des liaisons (à imprimer).
\documentclass[border=6mm]{standalone}
\usepackage{liaisons}
\usepackage{array,booktabs}
\renewcommand{\arraystretch}{1.1}
\begin{document}
\begin{tabular}{>{\raggedright\arraybackslash}p{4.2cm} >{\centering\arraybackslash}p{2.6cm} c c >{\centering\arraybackslash}p{2.6cm}}
\toprule
\textbf{Liaison} & \textbf{Degrés de liberté} & \textbf{Vue (z, y)} & \textbf{Vue (x, y)} & \textbf{Efforts transmissibles} \\
\midrule
"""
PLANCHE_ROW = r"""%(designation)s & %(ddl)s & %(fig1)s & %(fig2)s & %(efforts)s \\
"""
PLANCHE_FOOT = r"""\bottomrule
\end{tabular}
\end{document}
"""

# Couleurs déclarées par figures/tikz/liaisons.sty. Le moteur s'en sert pour reconnaître, dans le
# SVG, les tracés d'un solide donné — il ne les interprète pas, il les compare.
PALETTE = {"solideA": (225, 55, 25), "solideB": (45, 75, 205), "solideC": (225, 105, 180), "solideD": (235, 150, 20),
           "solideE": (20, 150, 90), "solideF": (110, 60, 180),
           "solideG": (0, 150, 160), "solideH": (140, 90, 40), "black": (0, 0, 0)}

# Ordonnée du centre A dans les figures de symboles : bord de 2 pt du gabarit ci-dessus, plus les
# 1,3 cm de sa boîte englobante. Le moteur en fait la variable CSS --cy, autour de laquelle tournent
# les animations ; elle dépend donc du gabarit, qui est ici.
CENTRE_Y_PT = 2 + 1.3 * 72 / 2.54


def tex_escape(s):
    return s.replace("&", r"\&").replace("%", r"\%").replace("_", r"\_")


def tikz_cell(sym):
    """Un symbole dans une cellule de la planche."""
    h, v = sym["plan"]
    opts = "rotate=%d" % sym.get("rotate", 0) if sym.get("rotate") else ""
    return (r"\begin{tikzpicture}[x=1cm,y=1cm,baseline=(current bounding box.center)]"
            r"\useasboundingbox (-1.3,-1.05) rectangle (1.3,1.3);"
            r"\repere{(0,0)}{%s}{%s}{%d}\pic[%s] at (0,0) {%s};"
            r"\node[font=\small, anchor=south west, inner sep=1.5pt] at (0.1,0.12) {A};"
            r"\end{tikzpicture}") % (h, v, sym["sens"], opts, sym["pic"])


def sources_symboles(liaisons, dossier, ecrire):
    """Écrit un .tex par vue de chaque liaison, les mobilités et la planche.

    Renvoie (fichiers, anims, axial) : les sources à compiler, le mouvement visible dans le plan de
    chaque vue, et la translation dirigée vers l'observateur quand la liaison l'autorise.
    """
    dossier.mkdir(parents=True, exist_ok=True)
    files, rows, anims, axial = [], [], {}, {}
    for l in liaisons:
        for sym in l["symboles"]:
            h, v = sym["plan"]
            opts = "rotate=%d" % sym.get("rotate", 0) if sym.get("rotate") else ""
            src = SYMBOL_TEMPLATE % dict(h=h, v=v, sens=sym["sens"], opts=opts, pic=sym["pic"])
            path = dossier / f"liaison-{l['id']}-{sym['vue']}.tex"
            ecrire(path, src)
            files.append(path)
            anim = sym.get("anim", "none")
            anim = " ".join(anim) if isinstance(anim, list) else anim
            if anim != "none":
                anims[path.stem] = anim
            # la translation le long de l'axe de visée (celui qui n'est pas dans le plan de la vue) est
            # dirigée vers l'observateur : aucun mouvement du plan ne peut la montrer (c'est ce qui rendait
            # le pivot et le pivot glissant identiques en vue de bout)
            visee = ({"x", "y", "z"} - set(sym["plan"])).pop()
            if f"T{visee}" in l["ddl"]:
                axial[path.stem] = "lie" if l.get("ddl_lies") else "libre"
        ddl = ", ".join(l["ddl"]) if l["ddl"] else "aucun"
        if l.get("ddl_lies"):
            ddl += " (liés)"
        efforts = ", ".join(l["efforts"])
        if l.get("efforts_lies"):
            efforts += " (X et L liés)"
        syms = {s["vue"]: s for s in l["symboles"]}
        first = syms.get("bout") or l["symboles"][0]
        second = syms.get("face") or l["symboles"][-1]
        # ordre des colonnes : vue (z,y) puis vue (x,y)
        by_plane = {tuple(s["plan"]): s for s in l["symboles"]}
        first = by_plane.get(("z", "y"), first)
        second = by_plane.get(("x", "y"), second)
        rows.append(PLANCHE_ROW % dict(designation=tex_escape(l["designation"]), ddl=ddl,
                                       fig1=tikz_cell(first), fig2=tikz_cell(second), efforts=efforts))
    for m in ("Tx", "Ty", "Tz", "Rx", "Ry", "Rz"):
        flags = {k: 1 if k == m else 0 for k in ("Tx", "Ty", "Tz", "Rx", "Ry", "Rz")}
        # version étiquetée (leçons, corrections) et version « question » sans étiquette
        for suffix, labels in (("", {"labelT": "T#2", "labelR": "R#2"}), ("-q", {"labelT": "", "labelR": ""})):
            path = dossier / f"mobilite-{m}{suffix}.tex"
            ecrire(path, MOBILITE_TEMPLATE % dict(flags, **labels))
            files.append(path)
    planche = dossier / "planche-liaisons.tex"
    ecrire(planche, PLANCHE_HEAD + "".join(rows) + PLANCHE_FOOT)
    files.append(planche)
    return files, anims, axial


def couleurs_des_classes(racine, donnees, load_yaml):
    """{figure de schéma: {classe d'équivalence: couleur RGB}} — de quoi grouper les tracés."""
    mech = {}
    dossier = racine / donnees["mecanismes"]
    for path in sorted(dossier.glob("*.yaml")) if dossier.exists() else []:
        m = load_yaml(path)
        if not m.get("animation"):
            continue
        mech[m["figures"]["schema"]] = {c["id"]: PALETTE.get(c.get("couleur", "black"), (0, 0, 0))
                                        for c in m["classes"]}
    extra = racine / donnees.get("animations", "")
    if donnees.get("animations") and extra.exists():
        for fid, spec in (load_yaml(extra) or {}).get("animations", {}).items():
            mech[fid] = {cid: PALETTE[c["couleur"]] for cid, c in spec["classes"].items()}
    return mech


def figures(racine, donnees, load_yaml, dossier_gen, ecrire):
    """Ce que ce paquet apporte au compilateur de figures du moteur.

    `dossier_gen` est l'endroit où le moteur veut les sources engendrées ; `ecrire` est son
    écriture conditionnelle (ne touche au fichier que s'il change, sinon la date de modification
    invaliderait inutilement les figures déjà compilées).

    Renvoie :
      sources   — les .tex engendrés, à compiler ;
      anims     — {figure: mouvements visibles dans le plan}, séparés par des espaces ;
      axial     — {figure: « libre » | « lie »} pour la translation vers l'observateur ;
      mech      — {figure: {classe: couleur RGB}} pour les schémas cinématiques ;
      solide1   — la couleur du solide animé des symboles ;
      centre_y  — l'ordonnée du centre de rotation, en points.
    """
    racine = Path(racine)
    liaisons = load_yaml(racine / donnees["liaisons"])["liaisons"]
    sources, anims, axial = sources_symboles(liaisons, Path(dossier_gen), ecrire)
    return {"sources": sources, "anims": anims, "axial": axial,
            "mech": couleurs_des_classes(racine, donnees, load_yaml),
            "solide1": PALETTE["solideA"], "centre_y": CENTRE_Y_PT}
