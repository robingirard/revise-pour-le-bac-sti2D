#!/usr/bin/env python3
"""Compile les figures TikZ en PDF (lualatex) puis en SVG (pdftocairo).

- Génère les figures des symboles de liaison à partir de content/liaisons.yaml
  (un fichier .tex par vue) et une planche récapitulative imprimable.
- Compile toutes les figures de figures/tikz/*.tex (sauf les fichiers _partagés).
- Post-traite les SVG pour qu'ils puissent être insérés en ligne dans une page HTML
  (identifiants préfixés, en-tête XML retiré).

Usage : python3 tools/build_figures.py [--force] [--jobs N]
"""
import argparse
import concurrent.futures
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TIKZ = ROOT / "figures" / "tikz"
BUILD = ROOT / "figures" / "build"
GEN = BUILD / "tex"      # .tex générés
PDF = BUILD / "pdf"
SVG = BUILD / "svg"
CONTENT = ROOT / "content"

SYMBOL_TEMPLATE = r"""%% Généré par tools/build_figures.py — ne pas modifier à la main.
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

MOBILITE_TEMPLATE = r"""%% Généré par tools/build_figures.py — ne pas modifier à la main.
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

PLANCHE_HEAD = r"""%% Généré par tools/build_figures.py — planche récapitulative des liaisons (à imprimer).
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


def tikz_cell(sym):
    """Un symbole dans une cellule de la planche."""
    h, v = sym["plan"]
    opts = "rotate=%d" % sym.get("rotate", 0) if sym.get("rotate") else ""
    return (r"\begin{tikzpicture}[x=1cm,y=1cm,baseline=(current bounding box.center)]"
            r"\useasboundingbox (-1.3,-1.05) rectangle (1.3,1.3);"
            r"\repere{(0,0)}{%s}{%s}{%d}\pic[%s] at (0,0) {%s};"
            r"\node[font=\small, anchor=south west, inner sep=1.5pt] at (0.1,0.12) {A};"
            r"\end{tikzpicture}") % (h, v, sym["sens"], opts, sym["pic"])


ANIMS = {}   # nom de figure → type d'animation (rot | rock | tx | ty), rempli par generate_symbol_sources
RED = re.compile(r"rgb\(88\.2\d*%,\s*21\.5\d*%,\s*9\.8\d*%\)")   # solideA = RGB(225,55,25) en % (pdftocairo)
CENTER_Y_PT = 2 + 1.3 * 72 / 2.54   # bord 2 pt + 1,3 cm : ordonnée du centre A dans les figures de symboles


PALETTE = {"solideA": (225, 55, 25), "solideB": (45, 75, 205), "solideC": (225, 105, 180), "solideD": (235, 150, 20),
           "solideE": (20, 150, 90), "solideF": (110, 60, 180), "black": (0, 0, 0)}
MECH = {}   # nom de figure de schéma → {id de classe: regex de sa couleur}


def color_regex(rgb):
    """Regex de la couleur telle qu'écrite par pdftocairo : rgb(88.235294%,21.568627%,9.803922%)."""
    parts = []
    for c in rgb:
        pct = c * 100 / 255
        parts.append(re.escape(f"{pct:.6f}"[:4]) + r"\d*%")
    return re.compile(r"rgb\(" + r",\s*".join(parts) + r"\)")


def load_mechanisms():
    for path in sorted((CONTENT / "mecanismes").glob("*.yaml")):
        m = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not m.get("animation"):
            continue
        MECH[m["figures"]["schema"]] = {c["id"]: color_regex(PALETTE.get(c.get("couleur", "black"), (0, 0, 0))) for c in m["classes"]}
    extra = CONTENT / "animations.yaml"
    if extra.exists():
        for fid, spec in (yaml.safe_load(extra.read_text(encoding="utf-8")) or {}).get("animations", {}).items():
            MECH[fid] = {cid: color_regex(PALETTE[c["couleur"]]) for cid, c in spec["classes"].items()}


def generate_symbol_sources(liaisons):
    """Écrit un .tex par vue de chaque liaison + la planche. Retourne la liste des fichiers."""
    GEN.mkdir(parents=True, exist_ok=True)
    files = []
    rows = []
    for l in liaisons:
        for sym in l["symboles"]:
            h, v = sym["plan"]
            opts = "rotate=%d" % sym.get("rotate", 0) if sym.get("rotate") else ""
            src = SYMBOL_TEMPLATE % dict(h=h, v=v, sens=sym["sens"], opts=opts, pic=sym["pic"])
            path = GEN / f"liaison-{l['id']}-{sym['vue']}.tex"
            write_if_changed(path, src)
            files.append(path)
            if sym.get("anim", "none") != "none":
                ANIMS[path.stem] = sym["anim"]
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
            path = GEN / f"mobilite-{m}{suffix}.tex"
            write_if_changed(path, MOBILITE_TEMPLATE % dict(flags, **labels))
            files.append(path)
    planche = GEN / "planche-liaisons.tex"
    write_if_changed(planche, PLANCHE_HEAD + "".join(rows) + PLANCHE_FOOT)
    files.append(planche)
    return files


def tex_escape(s):
    return s.replace("&", r"\&").replace("%", r"\%").replace("_", r"\_")


def write_if_changed(path, text):
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    path.write_text(text, encoding="utf-8")


def shared_sources():
    """Fichiers dont la modification invalide toutes les figures."""
    return [TIKZ / "liaisons.sty"] + sorted(TIKZ.glob("_*.tex"))


def needs_build(tex, svg, force):
    if force or not svg.exists():
        return True
    newest = max(p.stat().st_mtime for p in [tex] + shared_sources())
    return newest > svg.stat().st_mtime


def compile_one(tex, force=False):
    name = tex.stem
    pdf = PDF / f"{name}.pdf"
    svg = SVG / f"{name}.svg"
    if not needs_build(tex, svg, force):
        return name, "à jour"
    env = dict(os.environ, TEXINPUTS=f"{TIKZ}:{GEN}:")
    cmd = ["lualatex", "-interaction=batchmode", "-halt-on-error",
           f"-output-directory={PDF}", str(tex)]
    r = subprocess.run(cmd, env=env, capture_output=True, text=True, cwd=PDF)
    if r.returncode != 0 or not pdf.exists():
        log = (PDF / f"{name}.log")
        tail = ""
        if log.exists():
            lines = log.read_text(encoding="utf-8", errors="replace").splitlines()
            errs = [i for i, ln in enumerate(lines) if ln.startswith("!")]
            start = errs[0] if errs else max(0, len(lines) - 25)
            tail = "\n".join(lines[start:start + 25])
        return name, f"ERREUR lualatex\n{tail}"
    r = subprocess.run(["pdftocairo", "-svg", str(pdf), str(svg)], capture_output=True, text=True)
    if r.returncode != 0:
        return name, f"ERREUR pdftocairo : {r.stderr.strip()}"
    svg.write_text(postprocess_svg(svg.read_text(encoding="utf-8"), name), encoding="utf-8")
    return name, "compilé"


def postprocess_svg(text, prefix):
    """Prépare le SVG à l'insertion en ligne : supprime l'en-tête XML, préfixe les identifiants
    (sinon deux figures dans la même page se partagent leurs glyphes), ajoute une classe."""
    text = re.sub(r"<\?xml[^>]*\?>\s*", "", text)
    text = re.sub(r"<!DOCTYPE[^>]*>\s*", "", text)
    ids = set(re.findall(r'\bid="([^"]+)"', text))
    for i in sorted(ids, key=len, reverse=True):
        text = text.replace(f'id="{i}"', f'id="{prefix}--{i}"')
        text = text.replace(f'href="#{i}"', f'href="#{prefix}--{i}"')
        text = text.replace(f'url(#{i})', f'url(#{prefix}--{i})')
    text = text.replace("<svg ", f'<svg class="fig" role="img" data-fig="{prefix}" ', 1)
    if prefix in MECH:
        # schéma cinématique animable : chaque tracé prend le groupe de sa classe d'équivalence (par couleur)
        classes = MECH[prefix]

        def wrap(m):
            attrs = m.group(2)
            for cid, rx in classes.items():
                if rx.search(attrs):
                    return f'<g class="mech" data-class="{cid}"><{m.group(1)}{attrs}/></g>'
            return m.group(0)
        text = re.sub(r"<(path|circle)\b([^>]*)/>", wrap, text)   # pas les glyphes (<use>) : les étiquettes restent fixes
        text = text.replace("<svg ", f'<svg data-mech="{prefix}" ', 1)
    if prefix in ANIMS:
        # symbole animable : le solide 1 (rouge) reçoit la classe s1, le centre A est donné en unités utilisateur
        # chaque élément rouge est enveloppé dans un groupe (un transform CSS sur l'élément lui-même
        # écraserait son attribut transform et le déplacerait) ; c'est le groupe qui est animé
        text = re.sub(r"<(path|circle|use)\b([^>]*)/>",
                      lambda m: f'<g class="s1"><{m.group(1)}{m.group(2)}/></g>' if RED.search(m.group(2)) else m.group(0), text)
        w = re.search(r'\bwidth="([\d.]+)pt"', text)
        cx = float(w.group(1)) / 2 if w else 0
        text = text.replace("<svg ", f'<svg data-anim="{ANIMS[prefix]}" style="--cx:{cx:.2f}px;--cy:{CENTER_Y_PT:.2f}px" ', 1)
    # arrondi des coordonnées des chemins (0,01 pt suffit) : divise la taille par ~1,5
    text = re.sub(r'\bd="([^"]*)"', lambda m: 'd="' + re.sub(r"-?\d+\.\d{3,}", lambda n: f"{float(n.group()):.2f}", m.group(1)) + '"', text)
    return text.strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--force", action="store_true", help="recompiler même si à jour")
    ap.add_argument("--jobs", type=int, default=os.cpu_count() or 2)
    ap.add_argument("--only", help="ne compiler que les figures dont le nom contient ce texte")
    args = ap.parse_args()

    for tool in ("lualatex", "pdftocairo"):
        if shutil.which(tool) is None:
            sys.exit(f"Outil manquant : {tool}")
    for d in (GEN, PDF, SVG):
        d.mkdir(parents=True, exist_ok=True)

    liaisons = yaml.safe_load((CONTENT / "liaisons.yaml").read_text(encoding="utf-8"))["liaisons"]
    load_mechanisms()
    sources = generate_symbol_sources(liaisons)
    sources += [p for p in sorted(TIKZ.glob("*.tex")) if not p.name.startswith("_")]
    if args.only:
        sources = [p for p in sources if args.only in p.stem]

    failures = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as ex:
        for name, status in ex.map(lambda p: compile_one(p, args.force), sources):
            print(f"  {name:45s} {status}")
            if status.startswith("ERREUR"):
                failures += 1
    # nettoyage des fichiers auxiliaires
    for p in PDF.glob("*"):
        if p.suffix in (".aux", ".log"):
            p.unlink()
    print(f"{len(sources)} figures, {failures} erreur(s) → {SVG}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
