#!/usr/bin/env python3
"""Contrôle rapide d'un fichier d'unité livré : YAML valide, compétences, exercices, figures référencées
(existantes / manquantes / hors de la fiche de figures à dessiner).
Usage : python3 tools/check_unit.py content/units/40-pc-electricite.yaml [docs/figures-todo-pc-electricite.md]"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FIG = re.compile(r"\{\{fig:([^}]+)\}\}")


def main(unit_path, todo_path=None):
    u = yaml.safe_load(Path(unit_path).read_text(encoding="utf-8"))
    existing = {p.stem for p in (ROOT / "figures" / "build" / "svg").glob("*.svg")}
    todo = set(re.findall(r"`([a-z0-9-]+)`", Path(todo_path).read_text(encoding="utf-8"))) if todo_path else set()
    figs, total, errors = set(), 0, []
    for unit in u["units"]:
        print(f"[{unit['id']}] {unit['title']}")
        for s in unit["skills"]:
            items = s.get("items", [])
            total += len(items)
            kinds = {}
            for it in items:
                kinds[it["type"]] = kinds.get(it["type"], 0) + 1
                if it["type"] == "mcq":
                    if not isinstance(it.get("answer"), int) or not 0 <= it["answer"] < len(it["choices"]):
                        errors.append(f"{s['id']} : QCM « {str(it.get('prompt'))[:40]} » réponse invalide")
                    if it.get("feedback") and len(it["feedback"]) != len(it["choices"]):
                        errors.append(f"{s['id']} : QCM « {str(it.get('prompt'))[:40]} » feedback mal aligné")
                if it["type"] == "guided":
                    for k, st in enumerate(it.get("steps", []), 1):
                        if st.get("kind") == "mcq" and not isinstance(st.get("answer"), list):
                            errors.append(f"{s['id']} : étape guidée {k} : answer doit être une liste")
            figs |= set(FIG.findall(yaml.safe_dump(s, allow_unicode=True)))
            lp = ROOT / "content" / s["lesson"]
            if lp.exists():
                figs |= set(FIG.findall(lp.read_text(encoding="utf-8")))
            else:
                errors.append(f"{s['id']} : leçon absente {s['lesson']}")
            print(f"   {s['id']:26s} {len(items):3d} exercices  prérequis={s.get('prerequisites', [])}  {kinds}")
    missing = sorted(f for f in figs if f not in existing)
    print(f"{total} exercices ; figures référencées {len(figs)}, manquantes {len(missing)}, hors fiche {[f for f in missing if f not in todo]}")
    print("manquantes :", missing)
    for e in errors:
        print("ERREUR :", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
