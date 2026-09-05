#!/usr/bin/env python3
"""Vérifie la cohérence des sources pédagogiques (content/) et, s'il existe, de dist/content.json.

Ce module est générique : il vérifie ce qui vaut pour **tout** paquet — arbre de compétences
(prérequis existants et sans cycle, leçons présentes, générateurs connus), exercices construits,
annales. Les invariants propres à un paquet — pour STI2D : liaisons, animations des symboles,
mécanismes — sont vérifiés par la fonction `verifier()` que son module de générateurs expose.

Sortie non nulle en cas d'erreur.  Usage : python3 tools/validate.py
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT))
from build_content import charger_pack, fig_refs, load_yaml  # noqa: E402

CONTENT = ROOT / "content"
DIST = ROOT / "dist" / "content.json"

errors, warnings = [], []
GENERATEURS = set()


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))




# Vues où deux liaisons s'animent forcément pareil : leur seule différence est une rotation autour
# de l'axe de révolution du solide, qui ne se voit pas de profil (arbre qui tourne sur lui-même).
# Le symbole, lui, les distingue (épaulements, filetage, contact) — c'est ce que dit la leçon.








def check_units(units):
    skills = {}
    for u in units["units"]:
        for s in u["skills"]:
            if s["id"] in skills:
                err(f"compétence en double : {s['id']}")
            skills[s["id"]] = s
    for sid, s in skills.items():
        for pr in s.get("prerequisites", []):
            if pr not in skills:
                err(f"{sid} : prérequis inconnu {pr}")
        if s.get("lesson") and not (CONTENT / s["lesson"]).exists():
            err(f"{sid} : leçon introuvable {s['lesson']}")
        for g in s.get("generators", []):
            if g["gen"] not in GENERATEURS:
                err(f"{sid} : générateur inconnu {g['gen']}")
        if not s.get("generators") and not s.get("items"):
            err(f"{sid} : aucun exercice")
    # cycles
    state = {}

    def visit(sid, stack):
        if state.get(sid) == 1:
            err("cycle de prérequis : " + " → ".join(stack + [sid]))
            return
        if state.get(sid) == 2:
            return
        state[sid] = 1
        for pr in skills[sid].get("prerequisites", []):
            if pr in skills:
                visit(pr, stack + [sid])
        state[sid] = 2

    for sid in skills:
        visit(sid, [])


def check_dist():
    if not DIST.exists():
        warn("dist/content.json absent : lancez « make » pour vérifier le contenu construit")
        return
    c = json.loads(DIST.read_text(encoding="utf-8"))
    figs = set(c["figures"]) | set(c.get("figureIndex", {}))   # figures inline ou chargées à la demande
    for it in c["items"].values():
        for f in fig_refs(it["payload"]):
            if f not in figs:
                err(f"dist : {it['id']} référence la figure inconnue {f}")
    for u in c["units"]:
        for s in u["skills"]:
            for f in fig_refs(s["lesson"]):
                if f not in figs:
                    err(f"dist : leçon {s['id']} référence la figure inconnue {f}")
            for i in s["items"]:
                if i not in c["items"]:
                    err(f"dist : {s['id']} liste un exercice inconnu {i}")
    kinds = {"mcq", "input", "grid", "order", "match"}
    for it in c["items"].values():
        if it["type"] != "guided":
            continue
        steps = it["payload"].get("steps", [])
        if len(steps) < 3:
            err(f"dist : {it['id']} : exercice guidé trop court ({len(steps)} étapes)")
        for k, s in enumerate(steps, 1):
            if s.get("kind") not in kinds:
                err(f"dist : {it['id']} étape {k} : kind invalide")
            if s.get("kind") == "mcq" and not (s.get("choices") and s.get("answer")):
                err(f"dist : {it['id']} étape {k} : QCM incomplet")
            if s.get("kind") == "mcq" and s.get("feedback") and len(s["feedback"]) != len(s["choices"]):
                err(f"dist : {it['id']} étape {k} : feedback mal aligné")
    skills = {s["id"] for u in c["units"] for s in u["skills"]}
    for a in c.get("annales", []):
        for k in ("id", "titre", "url"):
            if not a.get(k):
                err(f"dist : annale sans {k}")
        for pr in a.get("prerequis", []):
            if pr.get("skill") not in skills:
                err(f"dist : annale {a['id']} : prérequis inconnu {pr}")
    print(f"dist/content.json : {len(c['items'])} exercices, {len(c['figures'])} figures, "
          f"{sum(len(u['skills']) for u in c['units'])} compétences, "
          f"{sum(1 for i in c['items'].values() if i['type'] == 'guided')} exercices guidés, {len(c.get('annales', []))} annales")


def main():
    global GENERATEURS
    # Le paquet fournit ses générateurs et, s'il en a, ses propres vérifications : le moteur ne sait
    # pas ce qu'est une liaison mécanique, mais il sait demander au paquet de se contrôler lui-même.
    pack, fourni = charger_pack()
    GENERATEURS = {n[4:] for n in dir(type(fourni["builder"])) if n.startswith("gen_")}
    resume = ""
    greffon = sys.modules.get(pack.get("generateurs", ""))
    if greffon is not None and hasattr(greffon, "verifier"):
        resume = greffon.verifier(ROOT, pack.get("donnees", {}), err, warn, load_yaml)

    units = load(CONTENT / "units.yaml")
    for extra in sorted((CONTENT / "units").glob("*.yaml")) if (CONTENT / "units").exists() else []:
        units["units"].extend((load(extra) or {}).get("units", []))
    check_units(units)
    check_dist()
    for w in warnings:
        print("avertissement :", w)
    if errors:
        for e in errors:
            print("ERREUR :", e)
        sys.exit(1)
    print("OK — " + (resume + ", " if resume else "") + "aucune erreur")


if __name__ == "__main__":
    main()
