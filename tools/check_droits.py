#!/usr/bin/env python3
"""Vérifie qu'aucun texte du manuel ne se retrouve dans l'outil publié.

Le dépôt est public. Les transcriptions du manuel vivent dans `docs/notes/`, hors de git — mais
c'est le contenu **publié** qu'il faut contrôler, pas les notes. Ce script compare donc
`dist/content.json` (exactement ce qui part en ligne : énoncés, choix, corrections, leçons) aux
transcriptions locales, et signale toute reprise littérale longue.

Deux niveaux, parce qu'ils n'ont pas la même gravité :

  GRAVE       la reprise tombe dans un passage que la transcription donne entre guillemets « … »,
              c'est-à-dire du texte du livre cité mot pour mot. Sortie en erreur.
  À VÉRIFIER  la reprise tombe ailleurs dans la transcription du livre. Souvent anodin (une
              définition standard, une formule, un terme de métier), parfois non : à lire.

Les sections où les agents ont écrit **nos** propositions (« Propositions pour l'application »,
« Idée d'exercice complet », « Figures à redessiner », « Remarques ») sont exclues de la
comparaison : une correspondance avec elles est normale, c'est notre texte.

Deux limites à garder en tête, le script ne les corrige pas :
  - les notes sont des transcriptions, pas le livre : un passage reformulé par le transcripteur
    puis repris tel quel dans l'outil ne sera pas détecté ;
  - une suite de 8 mots identiques n'est pas en soi une contrefaçon (une définition scolaire se
    dit d'une seule façon). Le script signale, il ne juge pas.

    python3 tools/check_droits.py [--mots 8] [--notes docs/notes]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist" / "content.json"
NOTES = ROOT / "docs" / "notes"

# Sections des notes qui transcrivent le livre (le reste, ce sont nos propositions).
SECTIONS_LIVRE = ("contenu", "exercices du livre", "liste des exercices", "exercices", "plan")
SECTIONS_A_NOUS = ("propositions pour l'application", "idée d'exercice", "figures à redessiner",
                   "remarques", "notions du programme")


def mots(texte):
    """Suite de mots normalisés : sans accents, sans balisage, sans ponctuation."""
    t = unicodedata.normalize("NFD", str(texte).lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"\$[^$]*\$|\$\$[^$]*\$\$", " ", t)      # formules : hors comparaison
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return t.split()


def sections(md):
    """Découpe une note en (titre, texte) sur les titres de niveau 2."""
    out, titre, buf = [], "(en-tête)", []
    for ligne in md.splitlines():
        m = re.match(r"^##\s+(.*)", ligne)
        if m:
            out.append((titre, "\n".join(buf)))
            titre, buf = m.group(1).strip(), []
        else:
            buf.append(ligne)
    out.append((titre, "\n".join(buf)))
    return out


def est_du_livre(titre):
    t = unicodedata.normalize("NFC", titre.lower())
    if any(t.startswith(x) or x in t for x in SECTIONS_A_NOUS):
        return False
    return any(x in t for x in SECTIONS_LIVRE)


def empreintes_des_notes(dossier, n):
    """{n-gramme: (fichier, cité)} sur les seules sections qui transcrivent le livre.

    « cité » = le n-gramme tombe dans un passage entre guillemets, donc du texte du livre repris
    mot pour mot par le transcripteur : c'est là que la reprise serait grave.
    """
    table = {}
    for chemin in sorted(dossier.glob("*.md")):
        for titre, corps in sections(chemin.read_text(encoding="utf-8")):
            if not est_du_livre(titre):
                continue
            cites = set()
            for extrait in re.findall(r"«([^»]{20,})»", corps):
                for g in fenetres(mots(extrait), n):
                    cites.add(g)
            for g in fenetres(mots(corps), n):
                if g not in table or (g in cites and not table[g][1]):
                    table[g] = (chemin.name, g in cites)
    return table


def fenetres(ms, n):
    return [" ".join(ms[i:i + n]) for i in range(len(ms) - n + 1)]


def textes_publies(content):
    """(origine, texte) de tout ce que l'application affiche."""
    out = []
    for unit in content["units"]:
        for skill in unit["skills"]:
            if skill.get("lesson"):
                out.append((f"leçon {skill['id']}", skill["lesson"]))
            if skill.get("description"):
                out.append((f"compétence {skill['id']}", skill["description"]))
    for iid, it in content["items"].items():
        for texte in chaines(it.get("payload")):
            out.append((iid, texte))
    return out


def chaines(obj):
    """Toutes les chaînes d'un énoncé, quelle que soit sa forme (QCM, guidé, grille…)."""
    if isinstance(obj, str):
        if len(obj) > 30:
            yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from chaines(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from chaines(v)


def reprises(ms, table, n):
    """Suites maximales de mots présentes dans les notes ; renvoie (extrait, fichier, cité)."""
    out, i = [], 0
    while i + n <= len(ms):
        g = " ".join(ms[i:i + n])
        if g not in table:
            i += 1
            continue
        fin = i + n
        fichier, cite = table[g]
        while fin < len(ms):
            suivant = " ".join(ms[fin - n + 1:fin + 1])
            if suivant not in table:
                break
            cite = cite or table[suivant][1]
            fin += 1
        out.append((" ".join(ms[i:fin]), fichier, cite))
        i = fin
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mots", type=int, default=8, help="longueur minimale d'une reprise (défaut : 8 mots)")
    ap.add_argument("--notes", type=Path, default=NOTES)
    ap.add_argument("--montrer", type=int, default=20, help="nombre de reprises affichées par niveau")
    args = ap.parse_args()

    if not DIST.exists():
        sys.exit("dist/content.json absent : lancez « make » d'abord.")
    if not args.notes.exists():
        # les transcriptions sont locales (droits d'auteur) : ailleurs, il n'y a rien à comparer
        print(f"{args.notes} absent : vérification des droits ignorée (transcriptions locales).")
        return 0

    table = empreintes_des_notes(args.notes, args.mots)
    content = json.loads(DIST.read_text(encoding="utf-8"))
    textes = textes_publies(content)

    graves, verifier = [], []
    for origine, texte in textes:
        for extrait, fichier, cite in reprises(mots(texte), table, args.mots):
            (graves if cite else verifier).append((len(extrait.split()), origine, extrait, fichier))

    fichiers = len(list(args.notes.glob("*.md")))
    print(f"{len(textes)} textes publiés comparés à {fichiers} transcriptions "
          f"({len(table)} suites de {args.mots} mots issues du livre)")

    for titre, lot in (("GRAVE — texte du livre cité mot pour mot", graves),
                       ("À VÉRIFIER — reprise de la transcription du livre", verifier)):
        if not lot:
            continue
        print(f"\n{titre} : {len(lot)}")
        for n, origine, extrait, fichier in sorted(lot, reverse=True)[:args.montrer]:
            print(f"  [{n} mots] {origine}  ← {fichier}")
            print(f"      « {extrait[:160]}{'…' if len(extrait) > 160 else ''} »")
        if len(lot) > args.montrer:
            print(f"  … et {len(lot) - args.montrer} autres")

    if graves:
        print("\nÀ corriger avant toute publication : réécrire ces passages.")
        return 1
    print("\nAucune citation littérale du manuel dans le contenu publié."
          + (f" {len(verifier)} reprise(s) à relire." if verifier else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
