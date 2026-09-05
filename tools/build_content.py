#!/usr/bin/env python3
"""Construit dist/ : génère content.json (+ content.js) à partir de content/*.yaml, des leçons
Markdown et des SVG compilés, puis copie l'application (app/) dans dist/.

Ce module est le **moteur** : il ne connaît aucune matière. Ce qui est propre à un paquet — les
générateurs d'exercices, les tables des leçons, les animations — vient du module que `pack.yaml`
déclare sous la clé « generateurs ».

Chaque compétence de content/units.yaml combine :
  - des exercices écrits à la main (« items ») ;
  - des « générateurs » fournis par le paquet.
Les identifiants d'exercices sont stables (ils ne dépendent pas de l'ordre de génération) :
la progression enregistrée dans l'application survit à une reconstruction.

Usage : python3 tools/build_content.py
"""
import datetime
import json
import random
import re
import importlib
import shutil
import unicodedata
import sys
import zlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
SVG = ROOT / "figures" / "build" / "svg"
APP = ROOT / "app"
DIST = ROOT / "dist"



# ----------------------------------------------------------------------------- utilitaires
def fig(fid):
    return "{{fig:%s}}" % fid


def emoji(e):
    return "{{emoji:%s}}" % e if e else ""












def fr(x, nd=2):
    """Nombre en écriture française : 1 234,5 (zéros inutiles supprimés)."""
    s = f"{x:,.{nd}f}".replace(",", "\u202f").replace(".", ",")
    if "," in s:
        s = s.rstrip("0").rstrip(",")
    return s






def rng(key):
    return random.Random(zlib.crc32(key.encode("utf-8")))


def crc(text):
    return "%08x" % zlib.crc32(text.encode("utf-8"))


def cap(level):
    return max(1, min(3, int(level)))






























class Builder:
    """Fabrique d'exercices, sans aucune connaissance de matière.

    Un paquet qui a besoin de générateurs dérive cette classe et y ajoute des méthodes `gen_*`
    (voir `generators/liaisons.py` et la clé « generateurs » de `pack.yaml`).
    """

    def __init__(self):
        self.items = {}
        self.errors = []

    # --- primitives -----------------------------------------------------------
    def add(self, item):
        if item["id"] in self.items:
            self.errors.append(f"identifiant d'exercice en double : {item['id']}")
        item["level"] = cap(item.get("level", 1))
        item.setdefault("tags", [])
        self.items[item["id"]] = item
        return item["id"]

    def mcq_payload(self, iid, prompt, correct, distractors, explanation="", layout="list", feedback=None):
        """Payload d'un QCM : mélange déterministe des choix, feedback aligné."""
        feedback = dict(feedback or {})
        uniq, seen = [], {correct}
        for d in distractors:
            txt, fb = d if isinstance(d, tuple) else (d, None)
            if txt in seen:
                continue
            seen.add(txt)
            uniq.append(txt)
            if fb:
                feedback[txt] = fb
        choices = [correct] + uniq[:3]
        r = rng(iid)
        r.shuffle(choices)
        payload = {"prompt": prompt, "choices": choices, "answer": [choices.index(correct)],
                   "multiple": False, "layout": layout, "explanation": explanation}
        if feedback:
            payload["feedback"] = [None if c == correct else feedback.get(c) for c in choices]
        return payload

    def mcq(self, iid, skill, level, prompt, correct, distractors, explanation="", layout="list", tags=(), feedback=None):
        """distractors : liste de textes, ou de couples (texte, feedback). feedback : dict texte → feedback."""
        payload = self.mcq_payload(iid, prompt, correct, distractors, explanation, layout, feedback)
        return self.add({"id": iid, "skill": skill, "type": "mcq", "level": level, "tags": list(tags), "payload": payload})

    def guided(self, iid, skill, title, intro, steps, tags=()):
        """Exercice complet : enchaînement d'étapes (chacune = payload d'un exercice + « kind »)."""
        kinds = {"mcq", "input", "grid", "order", "match"}
        for k, s in enumerate(steps):
            if s.get("kind") not in kinds:
                self.errors.append(f"{iid} : étape {k + 1} de type inconnu {s.get('kind')}")
        return self.add({"id": iid, "skill": skill, "type": "guided", "level": 3, "tags": list(tags),
                         "payload": {"title": title, "intro": intro, "steps": steps}})

    def flashcard(self, iid, skill, level, front, back, tags=()):
        return self.add({"id": iid, "skill": skill, "type": "flashcard", "level": level, "tags": list(tags),
                         "payload": {"front": front, "back": back}})

    def grid(self, iid, skill, level, prompt, rows, cols, answer, explanation="", labels=None, tags=(), cell_feedback=None, hint=None):
        payload = {"prompt": prompt, "rows": rows, "cols": cols, "answer": list(answer), "explanation": explanation}
        if labels:
            payload["labels"] = labels
        if hint:
            payload["hint"] = hint
        if cell_feedback:
            payload["cellFeedback"] = cell_feedback
        return self.add({"id": iid, "skill": skill, "type": "grid", "level": level, "tags": list(tags), "payload": payload})

    def match(self, iid, skill, level, prompt, pairs, tags=(), explanation=""):
        payload = {"prompt": prompt, "pairs": pairs}
        if explanation:
            payload["explanation"] = explanation
        return self.add({"id": iid, "skill": skill, "type": "match", "level": level, "tags": list(tags), "payload": payload})

    def order(self, iid, skill, level, prompt, steps, tags=(), explanation=""):
        payload = {"prompt": prompt, "steps": steps}
        if explanation:
            payload["explanation"] = explanation
        return self.add({"id": iid, "skill": skill, "type": "order", "level": level, "tags": list(tags), "payload": payload})

    def input(self, iid, skill, level, prompt, answer, accept=(), numeric=False, tolerance=0, unit="", explanation="", tags=()):
        return self.add({"id": iid, "skill": skill, "type": "input", "level": level, "tags": list(tags),
                         "payload": {"prompt": prompt, "answer": str(answer), "accept": list(accept), "numeric": numeric,
                                     "tolerance": tolerance, "unit": unit, "explanation": explanation}})


    def numbers(self, n, key, lo=0, hi=6):
        cands = [k for k in range(lo, hi + 1) if k != n]
        cands.sort(key=lambda k: (abs(k - n), rng(key + str(k)).random()))
        return [str(k) for k in cands[:3]]




























    def add_handwritten(self, skill, q, prefix):
        t = q["type"]
        text = q.get("prompt") or q.get("front") or q.get("title") or ""   # guided : id stable dérivé du titre
        iid = f"{prefix}.h{crc(t + text)}"
        level = q.get("level", 1)
        if t == "flashcard":
            self.flashcard(iid, skill, level, q["front"], q["back"], tags=q.get("tags", []))
        elif t == "mcq":
            answer = q["answer"]
            answers = answer if isinstance(answer, list) else [answer]
            choices = list(q["choices"])
            for a in answers:
                if not 0 <= a < len(choices):
                    self.errors.append(f"{iid} : réponse hors limites")
            payload = {"prompt": q["prompt"], "choices": choices, "answer": answers,
                       "multiple": len(answers) > 1, "layout": q.get("layout", "list"),
                       "explanation": q.get("explanation", "")}
            if q.get("feedback"):
                if len(q["feedback"]) != len(choices):
                    self.errors.append(f"{iid} : feedback de longueur ≠ choix")
                payload["feedback"] = [None if i in answers else fb for i, fb in enumerate(q["feedback"])]
            self.add({"id": iid, "skill": skill, "type": "mcq", "level": level, "tags": q.get("tags", []), "payload": payload})
        elif t == "grid":
            rows = [{"id": r, "label": r} if isinstance(r, str) else r for r in q["rows"]]
            names = {"T": "Translation", "R": "Rotation", "F": "Force", "M": "Moment"}
            cols = [{"id": c, "label": names.get(c, c)} if isinstance(c, str) else c for c in q["cols"]]
            self.grid(iid, skill, level, q["prompt"], rows, cols, q["answer"], q.get("explanation", ""),
                      labels=q.get("labels"), tags=q.get("tags", []), cell_feedback=q.get("cellFeedback"), hint=q.get("hint"))
        elif t == "order":
            self.order(iid, skill, level, q["prompt"], list(q["steps"]), tags=q.get("tags", []), explanation=q.get("explanation", ""))
        elif t == "input":
            self.input(iid, skill, level, q["prompt"], q["answer"], q.get("accept", []), q.get("numeric", False),
                       q.get("tolerance", 0), q.get("unit", ""), q.get("explanation", ""), tags=q.get("tags", []))
        elif t == "match":
            self.match(iid, skill, level, q["prompt"], list(q["pairs"]), tags=q.get("tags", []), explanation=q.get("explanation", ""))
        elif t == "guided":
            self.guided(iid, skill, q["title"], q.get("intro", ""), list(q["steps"]), tags=q.get("tags", []))
        else:
            self.errors.append(f"{iid} : type inconnu {t}")








    # --- QCM numériques -----------------------------------------------------------
    def num_mcq(self, iid, skill, level, prompt, value, unit, distractors, explanation, nd=2, tags=()):
        """QCM à réponse numérique : `distractors` = liste de (valeur, feedback) ; les doublons sont écartés."""
        correct = f"{fr(value, nd)} {unit}".strip()
        distr = []
        for v, fb in distractors:
            txt = f"{fr(v, nd)} {unit}".strip()
            if txt != correct and txt not in [d[0] for d in distr]:
                distr.append((txt, fb))
        return self.mcq(iid, skill, level, prompt, correct, distr, explanation, tags=tags)



















# ----------------------------------------------------------------------------- construction
def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_figures():
    figures = {}
    if not SVG.exists():
        return figures
    for p in sorted(SVG.glob("*.svg")):
        if p.stem.startswith("planche-"):
            continue
        figures[p.stem] = p.read_text(encoding="utf-8")
    return figures


FIG_RE = re.compile(r"\{\{fig:([^}]+)\}\}")


def fig_refs(obj):
    if isinstance(obj, str):
        return FIG_RE.findall(obj)
    if isinstance(obj, dict):
        return [f for v in obj.values() for f in fig_refs(v)]
    if isinstance(obj, list):
        return [f for v in obj for f in fig_refs(v)]
    return []


def charger_pack():
    """Lit pack.yaml et le greffon de générateurs qu'il déclare.

    L'import du greffon se fait ici, et non au sommet du fichier : le greffon importe en retour le
    Builder du moteur, et ne peut le faire qu'une fois ce module entièrement chargé.
    """
    pack = load_yaml(ROOT / "pack.yaml") or {}
    sys.path.insert(0, str(Path(__file__).resolve().parent))   # le greffon retrouve le moteur
    sys.path.insert(0, str(ROOT))                              # et le moteur retrouve generators/
    nom = pack.get("generateurs")
    if not nom:
        return pack, {"builder": Builder(), "tables": {}, "animations": {}}
    greffon = importlib.import_module(nom)
    fourni = greffon.charger(ROOT, pack.get("donnees", {}), load_yaml)
    manquant = {"builder", "tables", "animations"} - set(fourni)
    if manquant:
        sys.exit(f"pack.yaml : le greffon « {nom} » ne fournit pas {sorted(manquant)}")
    return pack, fourni


def build():
    pack, fourni = charger_pack()
    b = fourni["builder"]
    tables = fourni["tables"]
    units_src = load_yaml(CONTENT / "units.yaml")
    for extra in sorted((CONTENT / "units").glob("*.yaml")) if (CONTENT / "units").exists() else []:
        more = load_yaml(extra) or {}
        units_src["units"].extend(more.get("units", []))
    annales_src = load_yaml(CONTENT / "annales.yaml") if (CONTENT / "annales.yaml").exists() else {"annales": []}
    figures = load_figures()
    # les générateurs offerts sont ceux du paquet : le moteur n'en connaît aucun
    generateurs = {n[4:]: n for n in dir(type(b)) if n.startswith("gen_")}

    units = []
    skill_ids = set()
    for u in units_src["units"]:
        skills = []
        for s in u["skills"]:
            sid = s["id"]
            if sid in skill_ids:
                b.errors.append(f"compétence en double : {sid}")
            skill_ids.add(sid)
            before = set(b.items)
            for q in s.get("items", []):
                b.add_handwritten(sid, q, sid)
            for g in s.get("generators", []):
                name = g["gen"]
                if name not in generateurs:
                    b.errors.append(f"{sid} : générateur inconnu « {name} » (connus : {', '.join(sorted(generateurs))})")
                    continue
                getattr(b, generateurs[name])(sid)
            new_ids = [i for i in b.items if i not in before]
            lesson = ""
            if s.get("lesson"):
                lp = CONTENT / s["lesson"]
                if lp.exists():
                    lesson = lp.read_text(encoding="utf-8")
                    lesson = re.sub(r"\{\{table:(\w+)\}\}", lambda mm: tables.get(mm.group(1), f"(table {mm.group(1)} inconnue)"), lesson)
                else:
                    b.errors.append(f"{sid} : leçon introuvable {s['lesson']}")
            skills.append({"id": sid, "title": s["title"], "icon": s.get("icon", "📘"),
                           "description": s.get("description", ""), "prerequisites": s.get("prerequisites", []),
                           "lesson": lesson, "levels": s.get("levels", 3), "items": new_ids})
        units.append({"id": u["id"], "matiere": u.get("matiere", "ingenierie"), "title": u["title"],
                      "description": u.get("description", ""), "skills": skills})

    # vérifications
    for u in units:
        for s in u["skills"]:
            for p in s["prerequisites"]:
                if p not in skill_ids:
                    b.errors.append(f"{s['id']} : prérequis inconnu {p}")
            if len(s["items"]) < 5:
                b.errors.append(f"{s['id']} : seulement {len(s['items'])} exercice(s)")
            for f in fig_refs(s["lesson"]):
                if f not in figures:
                    b.errors.append(f"leçon {s['id']} : figure inconnue {f}")
    for it in b.items.values():
        for f in fig_refs(it["payload"]):
            if f not in figures:
                b.errors.append(f"{it['id']} : figure inconnue {f}")
        if it["type"] == "mcq" and len(it["payload"]["choices"]) < 2:
            b.errors.append(f"{it['id']} : pas assez de choix")
        if it["type"] == "match" and len(it["payload"]["pairs"]) < 3:
            b.errors.append(f"{it['id']} : pas assez de paires")
        if it["type"] == "mcq" and "feedback" in it["payload"] and len(it["payload"]["feedback"]) != len(it["payload"]["choices"]):
            b.errors.append(f"{it['id']} : feedback mal aligné")
    annales = []
    for a in annales_src.get("annales", []) or []:
        for pr in a.get("prerequis", []):
            if pr["skill"] not in skill_ids:
                b.errors.append(f"annales {a['id']} : prérequis inconnu {pr['skill']}")
        if a.get("guided") and a["guided"] not in b.items:
            b.errors.append(f"annales {a['id']} : exercice guidé inconnu {a['guided']}")
        annales.append({"id": a["id"], "titre": a["titre"], "session": str(a.get("session", "")), "epreuve": a.get("epreuve", ""),
                        "partie": a.get("partie", ""), "url": a.get("url", ""), "corrige": a.get("corrige"),
                        "themes": a.get("themes", []), "prerequis": a.get("prerequis", []), "guided": a.get("guided")})
    if b.errors:
        print("Erreurs de construction :", file=sys.stderr)
        for e in b.errors:
            print("  -", e, file=sys.stderr)
        sys.exit(1)

    used = set()
    for it in b.items.values():
        used.update(fig_refs(it["payload"]))
    for u in units:
        for s in u["skills"]:
            used.update(fig_refs(s["lesson"]))
    animations = fourni["animations"]
    for fid in animations:
        if fid not in figures:
            b.errors.append(f"animations : figure inconnue {fid}")
    content = {
        "version": 1,
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "title": units_src.get("title") or pack.get("titre", "Révise"),
        "figures": {k: v for k, v in figures.items() if k in used},
        "units": units,
        "items": b.items,
        "annales": annales,
        "animations": animations,
    }
    return content


def write_dist(content):
    DIST.mkdir(exist_ok=True)
    if APP.exists():
        shutil.copytree(APP, DIST, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns("dev", "tests", "content.js", "*.py", "package.json", ".gitignore", ".DS_Store", "node_modules"))
    # Figures : un fichier SVG par figure, chargé à la demande par l'appli (content.json reste léger),
    # plus un index {id: {w, h, bytes}} (dimensions en pt, pour réserver la place avant chargement).
    figdir = DIST / "figures"
    figdir.mkdir(exist_ok=True)
    for old in figdir.glob("*.svg"):
        if old.stem not in content["figures"]:
            old.unlink()
    index = {}
    for fid, svg in content["figures"].items():
        (figdir / f"{fid}.svg").write_text(svg, encoding="utf-8")
        w = re.search(r'\bwidth="([\d.]+)pt"', svg)
        h = re.search(r'\bheight="([\d.]+)pt"', svg)
        index[fid] = {"w": float(w.group(1)) if w else 0, "h": float(h.group(1)) if h else 0, "bytes": len(svg.encode("utf-8"))}
    (figdir / "index.json").write_text(json.dumps(index, separators=(",", ":")), encoding="utf-8")
    light = dict(content, figures={}, figureIndex=index)
    # content.json reste entier : c'est ce que lisent validate.py et les scripts de vérification.
    (DIST / "content.json").write_text(json.dumps(light, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    write_content_js(light)


def normalize_answer(s):
    """Même normalisation que normalizeAnswer() de app/js/answers.js (accents, espaces, virgule)."""
    s = unicodedata.normalize("NFD", str(s).strip().lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", "", s).replace(",", ".")


def tag_labels(light):
    """Libellé lisible d'un tag : le choix de QCM qui porte ce nom (« pivot-glissant » → « Pivot
    glissant »). Calculé ici parce que l'application ne charge plus tous les exercices : bilan.js le
    déduisait en les parcourant tous, ce qui n'est plus possible."""
    out = {}
    for it in light["items"].values():
        if it["type"] != "mcq":
            continue
        for tag in it.get("tags") or []:
            if tag in out:
                continue
            wanted = normalize_answer(tag.replace("-", " "))
            for c in (it["payload"].get("choices") or []):
                if isinstance(c, str) and normalize_answer(c) == wanted:
                    out[tag] = c
                    break
    return out


def write_content_js(light):
    """Écrit l'index (`content.js`) et un paquet par unité (`content/<unite>.js`).

    Tout tenait dans un seul fichier de 2,5 Mo qu'il fallait charger avant d'afficher quoi que ce
    soit : ouvrir une leçon de maths faisait payer l'ingénierie et la physique. L'index ne garde
    désormais que ce dont l'application a besoin **avant** d'ouvrir une unité — de quoi dessiner
    l'accueil et la carte de progression, et composer une séance : la compétence, le type, le niveau
    et les tags de chaque exercice. Les énoncés et les leçons arrivent unité par unité, à la demande.
    """
    packdir = DIST / "content"
    packdir.mkdir(exist_ok=True)
    connus = {u["id"] for u in light["units"]}
    for old in packdir.glob("*.js"):
        if old.stem not in connus:
            old.unlink()

    unites, places = [], set()
    for unit in light["units"]:
        items, lessons, skills = {}, {}, []
        for skill in unit["skills"]:
            skills.append({k: v for k, v in skill.items() if k != "lesson"})
            if skill.get("lesson"):
                lessons[skill["id"]] = skill["lesson"]
            for iid in skill["items"]:
                items[iid] = light["items"][iid]
                places.add(iid)
        unites.append(dict(unit, skills=skills))
        pack = json.dumps({"items": items, "lessons": lessons}, ensure_ascii=False, separators=(",", ":"))
        (packdir / f"{unit['id']}.js").write_text(
            f"window.REVISE_UNIT({json.dumps(unit['id'])}, {pack});\n", encoding="utf-8")

    # liste lue par le service worker pour remplir le cache en arrière-plan (voir app/sw.js)
    (packdir / "liste.json").write_text(
        json.dumps([u["id"] for u in light["units"]], separators=(",", ":")), encoding="utf-8")

    perdus = set(light["items"]) - places
    if perdus:   # un exercice qu'aucune compétence ne liste ne serait plus jamais chargé
        sys.exit(f"{len(perdus)} exercice(s) hors de toute compétence : {sorted(perdus)[:3]}")

    # Fiche d'index d'un exercice : le strict nécessaire à la composition d'une séance et au bilan.
    # Ni « id » ni « skill » : l'un est la clé, l'autre est déjà dans skill.items — l'application les
    # recolle au démarrage (packs.js), ce qui épargne 115 ko de chaînes répétées.
    fiches = {}
    for iid, it in light["items"].items():
        fiche = {"type": it["type"], "level": it.get("level", 1)}
        if it.get("tags"):
            fiche["tags"] = it["tags"]
        fiches[iid] = fiche
    index = dict(light, units=unites, items=fiches, tagLabels=tag_labels(light))
    (DIST / "content.js").write_text(
        "window.CONTENT = " + json.dumps(index, ensure_ascii=False, separators=(",", ":")) + ";\n",
        encoding="utf-8")


def stats(content):
    print(f"{len(content['items'])} exercices, {len(content['figures'])} figures")
    for u in content["units"]:
        print(f"[{u['id']}] {u['title']}")
        for s in u["skills"]:
            items = [content["items"][i] for i in s["items"]]
            per_level = {lv: sum(1 for i in items if i["level"] == lv) for lv in (1, 2, 3)}
            per_type = {}
            for i in items:
                per_type[i["type"]] = per_type.get(i["type"], 0) + 1
            types = ", ".join(f"{k} {v}" for k, v in sorted(per_type.items()))
            print(f"   {s['id']:12s} {len(items):3d} exercices  niveaux {per_level[1]}/{per_level[2]}/{per_level[3]}  ({types})")


if __name__ == "__main__":
    c = build()
    write_dist(c)
    stats(c)
    print(f"→ {DIST}/content.json ({(DIST / 'content.json').stat().st_size // 1024} ko)")
