#!/usr/bin/env python3
"""Vérifie la cohérence des sources pédagogiques (content/) et, s'il existe, de dist/content.json.

Invariants vérifiés :
  - liaisons : identifiants uniques, mobilités/efforts valides, ddl + efforts indépendants = 6,
    complémentarité mobilité ↔ effort sur chaque axe, symboles existants dans liaisons.sty ;
  - mécanismes : chaque pièce dans exactement une classe, liaisons entre classes existantes ;
  - arbre de compétences : prérequis existants et sans cycle, leçons présentes, générateurs connus.
Sortie non nulle en cas d'erreur.  Usage : python3 tools/validate.py
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from build_content import GENERATORS, fig_refs  # noqa: E402

CONTENT = ROOT / "content"
STY = ROOT / "figures" / "tikz" / "liaisons.sty"
DIST = ROOT / "dist" / "content.json"
DDL = {"Tx", "Ty", "Tz", "Rx", "Ry", "Rz"}
EFF = {"X", "Y", "Z", "L", "M", "N"}
PAIR = {"Tx": "X", "Ty": "Y", "Tz": "Z", "Rx": "L", "Ry": "M", "Rz": "N"}

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def check_liaisons(liaisons):
    pics = set(re.findall(r"pics/([^/]+)/\.style", STY.read_text(encoding="utf-8")))
    ids = [l["id"] for l in liaisons]
    if len(ids) != len(set(ids)):
        err("liaisons : identifiants en double")
    for l in liaisons:
        p = f"liaison {l['id']}"
        for k in ("nom", "designation", "parametre", "ddl", "efforts", "contact", "surfaces", "exemples", "symboles", "difficulte"):
            if k not in l:
                err(f"{p} : champ manquant « {k} »")
        bad = set(l["ddl"]) - DDL
        if bad:
            err(f"{p} : mobilités inconnues {bad}")
        bad = set(l["efforts"]) - EFF
        if bad:
            err(f"{p} : efforts inconnus {bad}")
        n = (len(l["ddl"]) - len(l.get("ddl_lies", []))) + (len(l["efforts"]) - len(l.get("efforts_lies", [])))
        if n != 6:
            err(f"{p} : ddl + efforts indépendants = {n} ≠ 6")
        linked = {x for pair in l.get("ddl_lies", []) for x in pair}
        for d, e in PAIR.items():
            if d in linked:
                continue
            if (d in l["ddl"]) == (e in l["efforts"]):
                err(f"{p} : {d} et {e} devraient être complémentaires")
        if not 1 <= l["difficulte"] <= 3:
            err(f"{p} : difficulte hors [1,3]")
        for c in l.get("confusables", []):
            if c not in ids or c == l["id"]:
                err(f"{p} : confusable invalide « {c} »")
        for s in l["symboles"]:
            if s["pic"] not in pics:
                err(f"{p} : symbole TikZ inconnu « {s['pic']} » (connus : {', '.join(sorted(pics))})")
            if s["vue"] not in ("bout", "face"):
                err(f"{p} : vue inconnue {s['vue']}")
            if len(s["plan"]) != 2 or set(s["plan"]) - {"x", "y", "z"}:
                err(f"{p} : plan invalide {s['plan']}")
            if s["sens"] not in (1, -1):
                err(f"{p} : sens invalide")
        if len(l["exemples"]) < 2:
            warn(f"{p} : moins de 2 exemples")
        for ex in l["exemples"]:
            if not isinstance(ex, dict) or "texte" not in ex:
                err(f"{p} : exemple mal formé (attendu {{texte, emoji}}) : {ex}")
        for k in ("contact_court", "reconnaitre", "mobilites"):
            if k not in l:
                err(f"{p} : champ manquant « {k} »")
        for s in l["symboles"]:
            if s["vue"] not in l.get("reconnaitre", {}):
                err(f"{p} : reconnaitre[{s['vue']}] manquant")
        missing = DDL - set(l.get("mobilites", {}))
        if missing:
            err(f"{p} : mobilites incomplet, manque {sorted(missing)}")
    return set(ids)


def check_mecanismes(mecanismes, liaison_ids):
    for m in mecanismes:
        p = f"mécanisme {m['id']}"
        nums = [pc["num"] for pc in m["pieces"]]
        if len(nums) != len(set(nums)):
            err(f"{p} : numéros de pièces en double")
        seen = {}
        for c in m["classes"]:
            for n in c["pieces"]:
                if n not in nums:
                    err(f"{p} : classe {c['id']} contient une pièce inconnue {n}")
                if n in seen:
                    err(f"{p} : pièce {n} dans deux classes ({seen[n]}, {c['id']})")
                seen[n] = c["id"]
        for n in nums:
            if n not in seen:
                warn(f"{p} : pièce {n} dans aucune classe (déformable ?)")
        cids = {c["id"] for c in m["classes"]}
        for li in m["liaisons"]:
            for c in li["entre"]:
                if c not in cids:
                    err(f"{p} : liaison entre classe inconnue {c}")
            if li["liaison"] not in liaison_ids:
                err(f"{p} : liaison inconnue {li['liaison']}")
            if not re.fullmatch(r"[A-Z]", li["point"]):
                err(f"{p} : point invalide {li['point']}")
        for q in m.get("questions", []):
            if q["type"] == "mcq" and not (0 <= q["answer"] < len(q["choices"])):
                err(f"{p} : question « {q['prompt'][:40]}… » réponse hors limites")
            if q["type"] == "mcq" and q.get("feedback") and len(q["feedback"]) != len(q["choices"]):
                err(f"{p} : question « {q['prompt'][:40]}… » feedback mal aligné")
            if q["type"] == "mcq" and not q.get("feedback"):
                warn(f"{p} : question « {q['prompt'][:40]}… » sans feedback par choix")
        for k in ("dessin", "classes", "graphe", "schema"):
            if k not in m["figures"]:
                err(f"{p} : figure « {k} » manquante")


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
            if g["gen"] not in GENERATORS:
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
    figs = set(c["figures"])
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
    liaisons = load(CONTENT / "liaisons.yaml")["liaisons"]
    ids = check_liaisons(liaisons)
    mecanismes = [load(p) for p in sorted((CONTENT / "mecanismes").glob("*.yaml"))]
    check_mecanismes(mecanismes, ids)
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
    print(f"OK — {len(liaisons)} liaisons, {len(mecanismes)} mécanismes, aucune erreur")


if __name__ == "__main__":
    main()
