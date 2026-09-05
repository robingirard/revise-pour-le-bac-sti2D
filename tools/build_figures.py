#!/usr/bin/env python3
"""Compile les figures TikZ en PDF (lualatex) puis en SVG (pdftocairo).

Ce moteur ne connaît aucune matière. Il sait :
  - compiler les sources `.tex` d'un paquet, en parallèle, et ne refaire que ce qui a changé ;
  - préparer les SVG à l'insertion en ligne dans une page (identifiants préfixés, coordonnées
    arrondies, en-tête XML retiré) ;
  - poser les conventions d'animation que le CSS et `app/js/mech-anim.js` savent lire :
    `data-anim` et `data-axial` sur un symbole, le solide 1 enveloppé dans `g.s1`, `data-mech` sur
    un schéma cinématique et un groupe `g.mech[data-class]` par classe d'équivalence.

**Quelles** figures existent et **comment** elles bougent vient du paquet, par le greffon que
`pack.yaml` déclare (voir `generators/figures.py` et sa fonction `figures()`).

Usage : python3 tools/build_figures.py [--force] [--jobs N] [--only TEXTE]
"""
import argparse
import concurrent.futures
import importlib
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
GEN = BUILD / "tex"      # .tex engendrés par le paquet
PDF = BUILD / "pdf"
SVG = BUILD / "svg"

ANIMS = {}        # figure → mouvements visibles dans le plan de la vue, séparés par des espaces
AXIAL = {}        # figure → translation le long de l'axe de visée (libre | lie), invisible dans le plan
MECH = {}         # figure de schéma → {classe d'équivalence: regex de sa couleur}
SOLIDE1 = None    # regex de la couleur du solide animé des symboles
CENTER_Y_PT = 0   # ordonnée du centre de rotation, en points (dépend du gabarit du paquet)
CODE = []         # fichiers de code dont un changement invalide toutes les figures (voir shared_sources)


def load_yaml(path):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def write_if_changed(path, text):
    """N'écrit que si le contenu change : sinon la date de modification invaliderait les figures
    déjà compilées, et tout serait recompilé pour rien."""
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    path.write_text(text, encoding="utf-8")


def color_regex(rgb):
    """Regex de la couleur telle qu'écrite par pdftocairo : rgb(88.235294%,21.568627%,9.803922%)."""
    parts = []
    for c in rgb:
        pct = c * 100 / 255
        parts.append(r"0(?:\.0*)?%" if c == 0 else re.escape(f"{pct:.6f}"[:4]) + r"\d*%")   # pdftocairo écrit « 0% » pour une composante nulle
    return re.compile(r"rgb\(" + r",\s*".join(parts) + r"\)")


VIDE = {"sources": [], "anims": {}, "axial": {}, "mech": {}, "solide1": None, "centre_y": 0}


def charger_pack():
    """Lit pack.yaml et demande au greffon ce qu'il faut compiler et animer.

    L'import se fait ici, et non au sommet du fichier, pour la même raison que dans
    `build_content.py` : le greffon importe le moteur en retour, et ce décalage évite le cycle.
    Un paquet sans greffon, ou dont le greffon n'engendre aucune figure, reste valable : le moteur
    compile alors seulement les sources écrites à la main dans `figures/tikz/`.
    """
    pack = load_yaml(ROOT / "pack.yaml") or {}
    sys.path.insert(0, str(ROOT))                                # le greffon est un paquet de la racine
    sys.path.insert(0, str(Path(__file__).resolve().parent))     # et il y retrouve le moteur
    nom = pack.get("generateurs")
    if not nom:
        return VIDE
    greffon = importlib.import_module(nom)
    CODE.extend(sorted(Path(greffon.__file__).parent.glob("*.py")))   # le greffon décide aussi du résultat
    if not hasattr(greffon, "figures"):
        return VIDE
    fourni = greffon.figures(ROOT, pack.get("donnees", {}), load_yaml, GEN, write_if_changed)
    manquant = set(VIDE) - set(fourni)
    if manquant:
        sys.exit(f"pack.yaml : le greffon « {nom} » ne fournit pas {sorted(manquant)}")
    return fourni


def shared_sources():
    """Fichiers dont la modification invalide toutes les figures.

    Le code en fait partie, et pas seulement les sources TikZ : le post-traitement décide des
    attributs d'animation et du regroupement des tracés, donc le changer change les SVG. Sans
    cela, une correction du moteur laissait en place des figures compilées par la version d'avant
    — c'est arrivé, et quatre schémas de mécanismes sont restés en ligne sans leur classe E0.
    """
    return sorted(TIKZ.glob("*.sty")) + sorted(TIKZ.glob("_*.tex")) + CODE


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
    if prefix in ANIMS or prefix in AXIAL:
        # symbole animable : le solide 1 reçoit la classe s1, le centre A est donné en unités utilisateur
        # chaque élément du solide 1 est enveloppé dans un groupe (un transform CSS sur l'élément lui-même
        # écraserait son attribut transform et le déplacerait) ; c'est le groupe qui est animé
        text = re.sub(r"<(path|circle|use)\b([^>]*)/>",
                      lambda m: f'<g class="s1"><{m.group(1)}{m.group(2)}/></g>' if SOLIDE1.search(m.group(2)) else m.group(0), text)
        w = re.search(r'\bwidth="([\d.]+)pt"', text)
        cx = float(w.group(1)) / 2 if w else 0
        axial = f' data-axial="{AXIAL[prefix]}"' if prefix in AXIAL else ""
        text = text.replace("<svg ", f'<svg data-anim="{ANIMS.get(prefix, "none")}"{axial}'
                            f' style="--cx:{cx:.2f}px;--cy:{CENTER_Y_PT:.2f}px" ', 1)
    # arrondi des coordonnées des chemins (0,01 pt suffit) : divise la taille par ~1,5
    text = re.sub(r'\bd="([^"]*)"', lambda m: 'd="' + re.sub(r"-?\d+\.\d{3,}", lambda n: f"{float(n.group()):.2f}", m.group(1)) + '"', text)
    return text.strip()


def main():
    global ANIMS, AXIAL, MECH, SOLIDE1, CENTER_Y_PT
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

    CODE.append(Path(__file__).resolve())
    fourni = charger_pack()
    ANIMS = fourni["anims"]
    AXIAL = fourni["axial"]
    MECH = {fig: {cid: color_regex(rgb) for cid, rgb in classes.items()}
            for fig, classes in fourni["mech"].items()}
    # sans couleur de solide 1, aucun tracé n'est enveloppé : une regex qui ne peut pas correspondre
    SOLIDE1 = color_regex(fourni["solide1"]) if fourni["solide1"] else re.compile(r"(?!x)x")
    CENTER_Y_PT = fourni["centre_y"]

    sources = list(fourni["sources"])
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
