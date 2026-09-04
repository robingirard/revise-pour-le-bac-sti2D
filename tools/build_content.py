#!/usr/bin/env python3
"""Construit dist/ : génère content.json (+ content.js) à partir de content/*.yaml, des leçons
Markdown et des SVG compilés, puis copie l'application (app/) dans dist/.

Chaque compétence de content/units.yaml combine :
  - des exercices écrits à la main (« items ») ;
  - des « générateurs » qui fabriquent des exercices à partir de la base de connaissances
    (content/liaisons.yaml, content/mecanismes/*.yaml).
Les identifiants d'exercices sont stables (ils ne dépendent pas de l'ordre de génération) :
la progression enregistrée dans l'application survit à une reconstruction.

Usage : python3 tools/build_content.py
"""
import datetime
import json
import random
import re
import shutil
import sys
import zlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
SVG = ROOT / "figures" / "build" / "svg"
APP = ROOT / "app"
DIST = ROOT / "dist"

AXES = ["x", "y", "z"]
FORCE = {"x": "X", "y": "Y", "z": "Z"}
MOMENT = {"x": "L", "y": "M", "z": "N"}
VUE_TXT = {"bout": "vue selon l'axe", "face": "vue de face"}
MOBS = ["Tx", "Ty", "Tz", "Rx", "Ry", "Rz"]
MOB_TXT = {"Tx": "la translation selon x", "Ty": "la translation selon y", "Tz": "la translation selon z",
           "Rx": "la rotation autour de x", "Ry": "la rotation autour de y", "Rz": "la rotation autour de z"}
MOB_LONG = {m: ("une translation (flèche droite) le long de l'axe " if m[0] == "T" else "une rotation (flèche courbe) autour de l'axe ") + m[1] for m in MOBS}
CELL_MOB = {"Fx": "Tx", "Fy": "Ty", "Fz": "Tz", "Mx": "Rx", "My": "Ry", "Mz": "Rz"}
EFFORT_LABEL = {"Fx": "X", "Fy": "Y", "Fz": "Z", "Mx": "L", "My": "M", "Mz": "N"}
GENERIC_WRONG_REASONS = [
    "Parce qu'elles sont en contact l'une avec l'autre",
    "Parce qu'elles ont la même couleur sur le dessin",
    "Parce qu'elles sont fabriquées dans le même matériau",
    "Parce qu'elles ont la même taille",
]


# ----------------------------------------------------------------------------- utilitaires
def fig(fid):
    return "{{fig:%s}}" % fid


def emoji(e):
    return "{{emoji:%s}}" % e if e else ""


def mob_list(ms):
    parts = [MOB_TXT[m] for m in MOBS if m in ms]
    if not parts:
        return ""
    return parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + " et " + parts[-1]


def diff_feedback(L, D, context=""):
    """Feedback quand on a choisi la liaison D à la place de L : compare leurs mobilités."""
    dl, dd = set(L["ddl"]), set(D["ddl"])
    extra, missing = dd - dl, dl - dd
    if L["id"] == "helicoidale" and D["id"] == "pivot-glissant":
        s = "Non : dans un pivot glissant, translation et rotation sont indépendantes ; ici elles sont liées par le filetage (un tour = un pas)."
    elif L["id"] == "pivot-glissant" and D["id"] == "helicoidale":
        s = "Non : une hélicoïdale lie la translation à la rotation (filetage) ; ici l'arbre est lisse, les deux mouvements sont indépendants."
    else:
        s = f"Non : la liaison {D['nom'].lower()}"
        if extra and missing:
            s += f" autoriserait {mob_list(extra)} mais bloquerait {mob_list(missing)}."
        elif extra:
            s += f" autoriserait aussi {mob_list(extra)}."
        elif missing:
            s += f" ne permettrait pas {mob_list(missing)}."
        else:
            s += " n'a pas le même contact."
    return (s + " " + context).strip()


def low_first(s):
    """Minuscule sur la première lettre seulement (« Pivot d'axe (B, x) » → « pivot d'axe (B, x) »)."""
    return s[:1].lower() + s[1:] if s else s


def le(m):
    """« le serre-joint », « l'étau » (élision devant voyelle)."""
    n = low_first(m["nom"])
    return ("l'" + n) if n[:1] in "aeiouyéèêh" else ("le " + n)


def du(m):
    n = low_first(m["nom"])
    return ("de l'" + n) if n[:1] in "aeiouyéèêh" else ("du " + n)


def fr(x, nd=2):
    """Nombre en écriture française : 1 234,5 (zéros inutiles supprimés)."""
    s = f"{x:,.{nd}f}".replace(",", "\u202f").replace(".", ",")
    if "," in s:
        s = s.rstrip("0").rstrip(",")
    return s


def ex_text(ex):
    return ex["texte"] if isinstance(ex, dict) else str(ex)


def ex_emoji(ex):
    return ex.get("emoji", "") if isinstance(ex, dict) else ""


def rng(key):
    return random.Random(zlib.crc32(key.encode("utf-8")))


def crc(text):
    return "%08x" % zlib.crc32(text.encode("utf-8"))


def cap(level):
    return max(1, min(3, int(level)))


def lvl(base, liaison):
    return cap(max(base, liaison.get("difficulte", 1)))


def sym_fig(liaison, vue):
    return f"liaison-{liaison['id']}-{vue}"


def distinct_views(liaison):
    """Vues dont le symbole est réellement différent (encastrement, rotule, appui plan : une seule)."""
    seen, out = set(), []
    for s in liaison["symboles"]:
        key = (s["pic"], s.get("rotate", 0))
        if key not in seen:
            seen.add(key)
            out.append(s)
    return out


def view_of(liaison, vue):
    for s in liaison["symboles"]:
        if s["vue"] == vue:
            return s
    return liaison["symboles"][0]


def nb_ddl(l):
    return len(l["ddl"]) - len(l.get("ddl_lies", []))


def nb_efforts(l):
    return len(l["efforts"]) - len(l.get("efforts_lies", []))


def fmt_ddl(l):
    if not l["ddl"]:
        return "aucune mobilité"
    txt = ", ".join(l["ddl"])
    if l.get("ddl_lies"):
        txt += " — liés (la rotation entraîne la translation)"
    elif l["id"] == "pivot-glissant":
        txt += " — indépendants"
    return txt


def fmt_efforts(l):
    txt = ", ".join(l["efforts"])
    if l.get("efforts_lies"):
        txt += " (X et L liés)"
    return txt


def fmt_pieces(pieces, m):
    """« la pièce 2 (rail) et la pièce 3 (mâchoire fixe) »"""
    names = {p["num"]: p["nom"] for p in m["pieces"]}
    parts = [f"{n} ({names[n]})" for n in pieces]
    if len(parts) == 1:
        return f"la pièce {parts[0]}"
    return "les pièces " + ", ".join(parts[:-1]) + " et " + parts[-1]


def plan_txt(sym):
    h, v = sym["plan"]
    return f"({h}, {v})"


def designation_complete(liaison, li):
    """Désignation avec le point/axe propres au mécanisme : « Pivot d'axe (O, z) »."""
    nom = liaison["nom"]
    p = li["point"]
    param = liaison["parametre"]
    if param.startswith("centre"):
        return f"{nom} de centre {p}"
    if param.startswith("normale") and "axe" not in param:
        return f"{nom} de normale ({p}, {li.get('axe', 'y')})"
    if param.startswith("normale"):
        return f"{nom} de normale ({p}, {li.get('normale', 'y')}) et d'axe ({p}, {li.get('axe', 'x')})"
    return f"{nom} d'axe ({p}, {li.get('axe', 'x')})"


def lesson_tables(liaisons):
    def row(cells):
        return "| " + " | ".join(cells) + " |"

    def by_plane(l, plane):
        for s in l["symboles"]:
            if tuple(s["plan"]) == plane:
                return fig(sym_fig(l, s["vue"]))
        return ""

    t = {}
    t["symboles"] = "\n".join([row(["Liaison", "Vue (z, y)", "Vue (x, y)"]), row(["---"] * 3)] +
                              [row([l["designation"], by_plane(l, ("z", "y")), by_plane(l, ("x", "y"))]) for l in liaisons])
    t["ddl"] = "\n".join([row(["Liaison", "Mobilités", "Nombre de ddl"]), row(["---"] * 3)] +
                         [row([l["designation"], fmt_ddl(l), str(nb_ddl(l))]) for l in liaisons])
    t["contacts"] = "\n".join([row(["Liaison", "Contact", "Surfaces de contact", "Exemples"]), row(["---"] * 4)] +
                              [row([l["nom"], fig(f"contact-{l['id']}"), l["surfaces"],
                                    " ; ".join(f"{ex_emoji(e)} {ex_text(e)}".strip() for e in l["exemples"])]) for l in liaisons])
    t["mobilites"] = "\n".join([row(["Notation", "Figure", "Signification"]), row(["---"] * 3)] +
                               [row([f"**{m}**", fig(f"mobilite-{m}"), MOB_LONG[m]]) for m in MOBS])
    t["efforts"] = "\n".join([row(["Liaison", "Mobilités", "Efforts transmissibles"]), row(["---"] * 3)] +
                             [row([l["designation"], fmt_ddl(l), fmt_efforts(l)]) for l in liaisons])
    return t


# ----------------------------------------------------------------------------- générateurs
class Builder:
    def __init__(self, liaisons, mecanismes):
        self.liaisons = liaisons
        self.by_id = {l["id"]: l for l in liaisons}
        self.mecanismes = mecanismes
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

    def others(self, l, k, key):
        """k liaisons distractrices : d'abord les « confusables », puis au hasard (déterministe)."""
        pool = [self.by_id[c] for c in l.get("confusables", []) if c in self.by_id]
        rest = [o for o in self.liaisons if o["id"] != l["id"] and o not in pool]
        rng(key).shuffle(rest)
        return (pool + rest)[:k]

    def numbers(self, n, key, lo=0, hi=6):
        cands = [k for k in range(lo, hi + 1) if k != n]
        cands.sort(key=lambda k: (abs(k - n), rng(key + str(k)).random()))
        return [str(k) for k in cands[:3]]

    # --- feedbacks types ---------------------------------------------------------
    def fb_symbole(self, L, D, vue):
        """On a répondu D au lieu de L devant le symbole de L (vue donnée)."""
        return diff_feedback(L, D, f"Le symbole de la liaison {low_first(D['nom'])} serait {D['reconnaitre'][vue]} ; ici, {L['reconnaitre'][vue]} : c'est la liaison {low_first(L['nom'])}.")

    def fb_figure_de(self, D, vue):
        """On a choisi la figure de D (symbole) à la place de celle attendue."""
        return f"Non : ce symbole ({D['reconnaitre'][vue]}) est celui de la liaison {low_first(D['nom'])}."

    def fb_contact(self, L, D):
        return diff_feedback(L, D, f"Le contact « {D['contact_court']} » donnerait une liaison {low_first(D['nom'])} ; ici le contact est « {L['contact_court']} » : liaison {low_first(L['nom'])}.")

    def liaison_choices(self, L, key, fb):
        """3 liaisons distractrices avec leur feedback (fb(D) → texte)."""
        return [(o["nom"], fb(o)) for o in self.others(L, 3, key)]

    def mob_cell_feedback(self, L):
        return {m: L["mobilites"][m] for m in MOBS if m in L.get("mobilites", {})}

    # --- liaisons --------------------------------------------------------------
    def gen_symbole_vers_nom(self, skill):
        for l in self.liaisons:
            for s in distinct_views(l):
                iid = f"{skill}.symbole_vers_nom.{l['id']}.{s['vue']}"
                many = len(distinct_views(l)) > 1
                vue = f" ({VUE_TXT[s['vue']]}, plan {plan_txt(s)})" if many else ""
                self.mcq(iid, skill, lvl(1 if s["vue"] == "bout" else 2, l),
                         "Quelle liaison est représentée par ce symbole ?\n" + fig(sym_fig(l, s["vue"])),
                         l["nom"], self.liaison_choices(l, iid, lambda o, l=l, v=s["vue"]: self.fb_symbole(l, o, v)),
                         f"C'est la liaison **{l['designation']}**{vue} : {l['reconnaitre'][s['vue']]}. {l['contact']}", tags=[l["id"]])

    def gen_nom_vers_symbole(self, skill):
        for l in self.liaisons:
            for s in distinct_views(l):
                iid = f"{skill}.nom_vers_symbole.{l['id']}.{s['vue']}"
                distractors = []
                for o in self.others(l, 3, iid):
                    ov = view_of(o, s["vue"])["vue"]
                    distractors.append((fig(sym_fig(o, ov)), self.fb_figure_de(o, ov)))
                self.mcq(iid, skill, lvl(2 if s["vue"] == "bout" else 3, l),
                         f"Quel symbole représente la liaison **{l['designation']}** dans une vue du plan **{plan_txt(s)}** ?",
                         fig(sym_fig(l, s["vue"])), distractors,
                         f"{l['nom']} : {l['reconnaitre'][s['vue']]}. {l['contact']}", layout="grid", tags=[l["id"]])

    def gen_match_symboles(self, skill):
        groupes = [
            ("mix-1", ["encastrement", "pivot", "rotule", "glissiere"], "bout", 1),
            ("axes-bout", ["pivot", "glissiere", "helicoidale", "pivot-glissant"], "bout", 2),
            ("axes-face", ["pivot", "glissiere", "helicoidale", "pivot-glissant"], "face", 2),
            ("contacts-bout", ["rotule", "appui-plan", "ponctuelle", "lineaire-annulaire"], "bout", 3),
            ("contacts-face", ["lineaire-rectiligne", "appui-plan", "ponctuelle", "lineaire-annulaire"], "face", 3),
        ]
        for gid, ids, vue, level in groupes:
            pairs = [{"left": self.by_id[i]["nom"], "right": fig(sym_fig(self.by_id[i], view_of(self.by_id[i], vue)["vue"]))}
                     for i in ids if i in self.by_id]
            self.match(f"{skill}.match_symboles.{gid}", skill, level,
                       "Associez chaque liaison à son symbole.", pairs, tags=ids)

    def gen_nb_ddl_mcq(self, skill):
        for l in self.liaisons:
            iid = f"{skill}.nb_ddl_mcq.{l['id']}"
            n = nb_ddl(l)
            expl = f"Mobilités : {fmt_ddl(l)} → **{n}** degré(s) de liberté."
            if l.get("ddl_lies"):
                expl = "Tx et Rx sont liés (un tour = une avance d'un pas) : un seul degré de liberté indépendant."
            distr = []
            for k in self.numbers(n, iid):
                k = int(k)
                if l.get("ddl_lies") and k == 2:
                    fb = "Non : Tx et Rx sont liés par le filetage, ils ne comptent que pour **un** degré de liberté indépendant."
                elif k > n:
                    fb = f"Non, {k} c'est trop : seules ces mobilités sont possibles : {fmt_ddl(l)} → {n}."
                else:
                    fb = f"Non, {k} ce n'est pas assez : {fmt_ddl(l)} → {n}."
                distr.append((str(k), fb))
            self.mcq(iid, skill, lvl(1, l),
                     f"Combien de **degrés de liberté** possède la liaison **{l['designation']}** ?\n" + fig(sym_fig(l, distinct_views(l)[0]["vue"])),
                     str(n), distr, expl, tags=[l["id"]])

    def gen_ddl_grid(self, skill):
        rows = [{"id": a, "label": a} for a in AXES]
        cols = [{"id": "T", "label": "Translation"}, {"id": "R", "label": "Rotation"}]
        for l in self.liaisons:
            iid = f"{skill}.ddl_grid.{l['id']}"
            figs = " ".join(fig(sym_fig(l, s["vue"])) for s in distinct_views(l))
            self.grid(iid, skill, lvl(2, l),
                      f"Cochez les mobilités autorisées par la liaison **{l['designation']}**.\n{figs} {fig('contact-' + l['id'])}",
                      rows, cols, l["ddl"], f"Mobilités : {fmt_ddl(l)}. {l['contact']}", tags=[l["id"]],
                      cell_feedback=self.mob_cell_feedback(l))

    def gen_ddl_vers_nom(self, skill):
        for l in self.liaisons:
            iid = f"{skill}.ddl_vers_nom.{l['id']}"
            self.mcq(iid, skill, lvl(2, l),
                     f"Quelle liaison autorise **exactement** les mobilités suivantes : **{fmt_ddl(l)}** ?",
                     l["nom"], self.liaison_choices(l, iid, lambda o, l=l: diff_feedback(l, o, f"{l['nom']} : {l['contact']}")),
                     f"{l['designation']} : {l['contact']}", tags=[l["id"]])

    def gen_contact_figure_vers_nom(self, skill):
        for l in self.liaisons:
            iid = f"{skill}.contact_figure_vers_nom.{l['id']}"
            self.mcq(iid, skill, lvl(1, l),
                     f"Voici les surfaces en contact entre deux pièces (le contact est surligné en rouge). Quelle est la liaison ?\n{fig('contact-' + l['id'])}",
                     l["nom"], self.liaison_choices(l, iid, lambda o, l=l: self.fb_contact(l, o)),
                     f"{l['contact_court']} → **{l['nom']}** : {l['contact']}", tags=[l["id"]])

    def gen_nom_vers_contact_figure(self, skill):
        for l in self.liaisons:
            iid = f"{skill}.nom_vers_contact_figure.{l['id']}"
            distr = [(fig("contact-" + o["id"]), f"Non : ce dessin montre « {o['contact_court']} », c'est le contact d'une liaison {o['nom']}.")
                     for o in self.others(l, 3, iid)]
            self.mcq(iid, skill, lvl(2, l),
                     f"Quelles surfaces de contact réalisent une liaison **{l['nom']}** ?",
                     fig("contact-" + l["id"]), distr, f"{l['nom']} : {l['surfaces']}", layout="grid", tags=[l["id"]])

    def gen_contact_vers_nom(self, skill):
        for l in self.liaisons:
            iid = f"{skill}.contact_vers_nom.{l['id']}"
            self.mcq(iid, skill, lvl(2, l),
                     f"Les surfaces en contact entre les deux pièces sont : **{l['surfaces']}**\nQuelle est la liaison ?",
                     l["nom"], self.liaison_choices(l, iid, lambda o, l=l: self.fb_contact(l, o)),
                     f"{l['designation']} : {l['contact']}", tags=[l["id"]])

    def gen_exemple_vers_nom(self, skill):
        for l in self.liaisons:
            for k, ex in enumerate(l["exemples"]):
                iid = f"{skill}.exemple_vers_nom.{l['id']}.{k}"
                txt = ex_text(ex)
                self.mcq(iid, skill, lvl(2, l),
                         f"{emoji(ex_emoji(ex))}\n**{txt[0].upper() + txt[1:]}** : par quelle liaison modélise-t-on ce contact ?".strip(),
                         l["nom"], self.liaison_choices(l, iid, lambda o, l=l, txt=txt: diff_feedback(l, o, f"{txt[0].upper() + txt[1:]} : {l['surfaces']} → {l['nom']}.")),
                         f"{l['nom']} : {l['surfaces']} {l['contact']}", tags=[l["id"]])

    def gen_nom_vers_contact(self, skill):
        for l in self.liaisons:
            iid = f"{skill}.nom_vers_contact.{l['id']}"
            distr = [(o["surfaces"], f"Non : « {o['surfaces']} » réalise une liaison {o['nom']} ({fmt_ddl(o)}).") for o in self.others(l, 3, iid)]
            self.mcq(iid, skill, lvl(3, l),
                     f"Quelles surfaces de contact réalisent une liaison **{l['nom']}** ?",
                     l["surfaces"], distr, f"{l['designation']} : {l['contact']}", tags=[l["id"]])

    def gen_efforts_grid(self, skill):
        rows = [{"id": a, "label": a} for a in AXES]
        cols = [{"id": "F", "label": "Force"}, {"id": "M", "label": "Moment"}]
        cell_of = {"X": "Fx", "Y": "Fy", "Z": "Fz", "L": "Mx", "M": "My", "N": "Mz"}
        for l in self.liaisons:
            iid = f"{skill}.efforts_grid.{l['id']}"
            answer = [cell_of[e] for e in l["efforts"]]
            cfb = {}
            for cell, mob in CELL_MOB.items():
                reason = l.get("mobilites", {}).get(mob, "")
                if cell in answer:
                    cfb[cell] = f"{EFFORT_LABEL[cell]} est transmise car {mob} est {reason}"
                else:
                    cfb[cell] = f"{EFFORT_LABEL[cell]} n'est pas transmise car {mob} est {reason}"
            self.grid(iid, skill, lvl(2, l),
                      f"Cochez les composantes d'effort **transmissibles** par la liaison **{l['designation']}** "
                      f"(forces X, Y, Z ; moments L, M, N).\n" + fig(sym_fig(l, distinct_views(l)[0]["vue"])),
                      rows, cols, answer,
                      f"Transmis : {fmt_efforts(l)}. Les mobilités ({fmt_ddl(l)}) annulent les composantes correspondantes.",
                      labels=EFFORT_LABEL, tags=[l["id"]], cell_feedback=cfb)

    def gen_nb_efforts_mcq(self, skill):
        for l in self.liaisons:
            iid = f"{skill}.nb_efforts_mcq.{l['id']}"
            n = nb_efforts(l)
            distr = [(k, f"Non : 6 mobilités − {nb_ddl(l)} degré(s) de liberté = {n} composantes ({fmt_efforts(l)}).") for k in self.numbers(n, iid)]
            self.mcq(iid, skill, lvl(1, l),
                     f"Combien de composantes d'effort **indépendantes** transmet la liaison **{l['designation']}** ?\n{fig('contact-' + l['id'])}",
                     str(n), distr, f"6 − {nb_ddl(l)} ddl = **{n}** composantes : {fmt_efforts(l)}.", tags=[l["id"]])

    def gen_choix_symbole_vue(self, skill):
        for l in self.liaisons:
            views = distinct_views(l)
            if len(views) < 2:
                continue
            for s in views:
                iid = f"{skill}.choix_symbole_vue.{l['id']}.{s['vue']}"
                other = [v for v in views if v is not s][0]
                axe = l["parametre"].split("(")[-1].rstrip(")").split(",")[-1].strip() if "(" in l["parametre"] else "x"
                if s["vue"] == "bout":
                    why = f"Dans le plan {plan_txt(s)}, l'axe {axe} de la liaison est **perpendiculaire** à la feuille : on dessine la vue selon l'axe ({l['reconnaitre']['bout']})."
                else:
                    why = f"Dans le plan {plan_txt(s)}, l'axe {axe} de la liaison est **dans** la feuille : on dessine la vue de face ({l['reconnaitre']['face']})."
                choices = [(fig(sym_fig(l, other["vue"])), f"Non : c'est bien le symbole de la liaison {low_first(l['nom'])}, mais dans l'autre vue. {why}")]
                for o in self.others(l, 5, iid):
                    ov = distinct_views(o)
                    if len(ov) >= 2:
                        choices += [(fig(sym_fig(o, v["vue"])), self.fb_figure_de(o, v["vue"])) for v in ov[:2]]
                        break
                if len(choices) < 3:
                    choices += [(fig(sym_fig(o, distinct_views(o)[0]["vue"])), self.fb_figure_de(o, distinct_views(o)[0]["vue"]))
                                for o in self.others(l, 3, iid + "b")]
                note = " (l'axe x pointe vers vous)" if tuple(s["plan"]) == ("z", "y") else ""
                self.mcq(iid, skill, lvl(2 if s["vue"] == "bout" else 3, l),
                         f"On trace le schéma dans le plan **{plan_txt(s)}**{note}. "
                         f"Quel symbole représente la liaison **{l['designation']}** dans cette vue ?",
                         fig(sym_fig(l, s["vue"])), choices[:3], why, layout="grid", tags=[l["id"]])

    # --- mobilités (figures mobilite-Tx …) --------------------------------------
    def mob_distractors(self, m, key):
        same_axis = [x for x in MOBS if x != m and x[1] == m[1]]
        same_type = [x for x in MOBS if x != m and x[0] == m[0]]
        rng(key).shuffle(same_type)
        return same_axis + same_type

    def gen_mobilite_figure_vers_nom(self, skill):
        for m in MOBS:
            iid = f"{skill}.mobilite_figure_vers_nom.{m}"
            distr = [(d, f"Non : {d} serait {MOB_LONG[d]} ; la figure montre {MOB_LONG[m]}.") for d in self.mob_distractors(m, iid)]
            self.mcq(iid, skill, 1, f"Quelle mobilité est représentée sur cette figure ?\n{fig('mobilite-' + m + '-q')}",
                     m, distr, f"**{m}** : {MOB_LONG[m]}. {fig('mobilite-' + m)}", tags=["mobilites"])

    def gen_mobilite_nom_vers_figure(self, skill):
        for m in MOBS:
            iid = f"{skill}.mobilite_nom_vers_figure.{m}"
            distr = [(fig("mobilite-" + d + "-q"), f"Non : cette figure montre {d}, {MOB_LONG[d]}.") for d in self.mob_distractors(m, iid)]
            self.mcq(iid, skill, 2, f"Quelle figure représente la mobilité **{m}** ?",
                     fig("mobilite-" + m + "-q"), distr, f"**{m}** : {MOB_LONG[m]}. {fig('mobilite-' + m)}", layout="grid", tags=["mobilites"])

    # --- mécanismes ------------------------------------------------------------
    def handwritten(self, skill, questions, prefix):
        for q in questions:
            if q.get("skill", "schema-2d") != skill:
                continue
            self.add_handwritten(skill, q, prefix)

    def add_handwritten(self, skill, q, prefix):
        t = q["type"]
        text = q.get("prompt") or q.get("front") or ""
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

    def liaison_between(self, m, ca, cb):
        for li in m["liaisons"]:
            if set(li["entre"]) == {ca, cb}:
                return li
        return None

    def gen_classes_mecanisme(self, skill):
        for m in self.mecanismes:
            titre, dessin, classes_fig = m["titre"], fig(m["figures"]["dessin"]), fig(m["figures"]["classes"])
            names = {p["num"]: p["nom"] for p in m["pieces"]}
            all_pieces = [p["num"] for p in m["pieces"]]
            classes = m["classes"]
            class_of = {n: c for c in classes for n in c["pieces"]}

            def why_not_together(x, p):
                cx, cp = class_of.get(x), class_of.get(p)
                if cx is None or cp is None or cx is cp:
                    return f"la pièce {x} ({names[x]}) est bien solidaire de la pièce {p}"
                li = self.liaison_between(m, cx["id"], cp["id"])
                if li:
                    L = self.by_id[li["liaison"]]
                    return f"Non : la pièce {x} ({names[x]}) est en liaison **{L['nom'].lower()}** avec la classe de la pièce {p} : elles ont un mouvement relatif."
                return f"Non : la pièce {x} ({names[x]}) n'est pas solidaire de la pièce {p} : elle appartient à la classe « {cx['nom']} », qui bouge par rapport à « {cp['nom']} »."

            self.input(f"{skill}.nb_classes.{m['id']}", skill, 1,
                       f"Combien de **classes d'équivalence cinématique** compte {le(m)} ?\n{dessin}",
                       len(classes), numeric=True,
                       explanation="  ;  ".join(f"{c['id']} = {{{', '.join(map(str, c['pieces']))}}}" for c in classes),
                       tags=[m["id"]])
            for c in classes:
                pcs = c["pieces"]
                if len(pcs) >= 2:
                    p = pcs[0]
                    iid = f"{skill}.classe_de.{m['id']}.{p}"
                    others = [x for x in all_pieces if x not in pcs]
                    r = rng(iid)
                    wrong = [("aucune : elle forme une classe à elle seule", f"Non : {c.get('pourquoi', 'ces pièces sont solidaires.')}")]
                    tries = 0
                    while len(wrong) < 3 and tries < 20 and others:
                        tries += 1
                        k = min(len(others), r.choice([1, 2]))
                        s = sorted(r.sample(others, k))
                        txt = fmt_pieces(s, m)
                        if txt not in [w[0] for w in wrong]:
                            wrong.append((txt, why_not_together(s[0], p)))
                    self.mcq(iid, skill, 1,
                             f"Dans {le(m)}, quelles pièces forment la **même classe d'équivalence** que la pièce "
                             f"**{p} ({names[p]})** ?\n{dessin}",
                             fmt_pieces([x for x in pcs if x != p], m), wrong, c.get("pourquoi", ""), tags=[m["id"]])
                    if c.get("pourquoi"):
                        iid = f"{skill}.pourquoi.{m['id']}.{c['id']}"
                        distr = [(o["pourquoi"], f"Non : cette raison concerne la classe {o['id']} ({o['nom']}).")
                                 for o in classes if o is not c and o.get("pourquoi") and len(o["pieces"]) >= 2]
                        generic_fb = "Non : être en contact, avoir la même couleur, le même matériau ou la même taille n'empêche pas un mouvement relatif. Seule l'absence de mouvement relatif compte."
                        distr += [(g, generic_fb) for g in GENERIC_WRONG_REASONS]
                        self.mcq(iid, skill, 2,
                                 f"Pourquoi {fmt_pieces(pcs[:2], m)} {du(m)} sont-elles dans la **même** classe d'équivalence ?\n{classes_fig}",
                                 c["pourquoi"], distr[:3], "", tags=[m["id"]])
                else:
                    p = pcs[0]
                    iid = f"{skill}.singleton.{m['id']}.{p}"
                    others = [x for x in all_pieces if x != p]
                    r = rng(iid)
                    r.shuffle(others)
                    wrong = [(f"Oui, avec la pièce {x} ({names[x]})", why_not_together(x, p)) for x in others[:3]]
                    self.mcq(iid, skill, 2,
                             f"Dans {le(m)}, la pièce **{p} ({names[p]})** forme-t-elle une classe d'équivalence "
                             f"avec d'autres pièces ?\n{dessin}",
                             "Non : elle forme une classe à elle seule", wrong, c.get("pourquoi", ""), tags=[m["id"]])
            self.handwritten(skill, m.get("questions", []), f"{skill}.{m['id']}")

    def gen_liaison_entre_classes(self, skill):
        for m in self.mecanismes:
            cls = {c["id"]: c for c in m["classes"]}
            points = sorted({li["point"] for li in m["liaisons"]})
            by_point = {}
            for li in m["liaisons"]:
                by_point.setdefault(li["point"], li)
            for li in m["liaisons"]:
                l = self.by_id[li["liaison"]]
                a, b = li["entre"]
                iid = f"{skill}.liaison_entre.{m['id']}.{a}-{b}"
                self.mcq(iid, skill, 1,
                         f"Dans {le(m)}, entre **{a} ({cls[a]['nom']})** et **{b} ({cls[b]['nom']})**, "
                         f"le contact est : **{li['contact']}** ({li['surfaces']}).\nQuelle est la liaison ?\n{fig(m['figures']['classes'])}",
                         l["nom"], self.liaison_choices(l, iid, lambda o, l=l, li=li: diff_feedback(l, o, li.get("explication", ""))),
                         li.get("explication", ""), tags=[m["id"], l["id"]])
                # désignation complète (point + axe)
                iid2 = f"{skill}.designation.{m['id']}.{a}-{b}"
                correct = designation_complete(l, li)
                wrong = []
                for p in points:
                    if p != li["point"]:
                        other = by_point[p]
                        oL = self.by_id[other["liaison"]]
                        wrong.append((designation_complete(l, dict(li, point=p)),
                                      f"Non : le point {p} est le centre de la liaison {low_first(designation_complete(oL, other))} ; celle-ci est en {li['point']}."))
                for ax in AXES:
                    if ax != li.get("axe", "x") and not l["parametre"].startswith("centre"):
                        wrong.append((designation_complete(l, dict(li, axe=ax)),
                                      f"Non : sur le schéma, l'axe de cette liaison est ({li['point']}, {li.get('axe', 'x')}), pas ({li['point']}, {ax})."))
                if l["parametre"].startswith("centre"):
                    wrong.append((f"{l['nom']} d'axe ({li['point']}, x)", f"Non : une liaison {low_first(l['nom'])} se définit par son **centre**, pas par un axe."))
                o = self.others(l, 1, iid2)[0]
                wrong.append((designation_complete(o, dict(li, axe=li.get("axe", "x"))), diff_feedback(l, o, li.get("explication", ""))))
                rng(iid2).shuffle(wrong)
                self.mcq(iid2, skill, 2,
                         f"Dans {le(m)}, comment désigne-t-on **complètement** la liaison entre **{a}** et **{b}** "
                         f"(nom, centre, axe) ?\n{fig(m['figures']['schema'])}",
                         correct, wrong, li.get("explication", ""), tags=[m["id"], l["id"]])

    def gen_lecture_graphe(self, skill):
        for m in self.mecanismes:
            graphe = fig(m["figures"]["graphe"])
            self.input(f"{skill}.nb_liaisons.{m['id']}", skill, 1,
                       f"Combien de **liaisons** compte le graphe des liaisons {du(m)} ?\n{graphe}",
                       len(m["liaisons"]), numeric=True,
                       explanation="Chaque trait du graphe est une liaison entre deux classes.", tags=[m["id"]])
            desig = {designation_complete(self.by_id[li["liaison"]], li): li for li in m["liaisons"]}
            for li in m["liaisons"]:
                l = self.by_id[li["liaison"]]
                a, b = li["entre"]
                correct = designation_complete(l, li)
                wrong = [(d, f"Non : {d} relie {o['entre'][0]} et {o['entre'][1]}.") for d, o in desig.items() if d != correct]
                for o in self.others(l, 3, f"{skill}.{m['id']}.{a}{b}"):
                    d = designation_complete(o, li)
                    wrong.append((d, f"Non : {d} n'apparaît pas dans ce mécanisme."))
                for suffix, level, figtxt in (("lecture", 1, "\n" + graphe), ("memoire", 2, "")):
                    iid = f"{skill}.{suffix}.{m['id']}.{a}-{b}"
                    self.mcq(iid, skill, level,
                             f"{'D’après le graphe des liaisons, ' if suffix == 'lecture' else 'De mémoire : dans ' + le(m) + ', '}"
                             f"quelle liaison relie **{a}** et **{b}** ?{figtxt}",
                             correct, wrong, li.get("explication", ""), tags=[m["id"], l["id"]])
            self.handwritten(skill, m.get("questions", []), f"{skill}.{m['id']}")

    def gen_lecture_schema(self, skill):
        for m in self.mecanismes:
            self.handwritten(skill, m.get("questions", []), f"{skill}.{m['id']}")

    def gen_exercice_complet(self, skill):
        """Exercice de fin de chapitre : la démarche complète du schéma cinématique sur chaque mécanisme."""
        DEMARCHE = ["Étudier le dessin d'ensemble pour comprendre le fonctionnement",
                    "Identifier les classes d'équivalence (une couleur par classe)",
                    "Identifier la nature des contacts et en déduire les liaisons",
                    "Tracer le graphe des liaisons",
                    "Tracer le schéma cinématique (2D ou 3D)"]
        for m in self.mecanismes:
            iid = f"{skill}.complet.{m['id']}"
            names = {p["num"]: p["nom"] for p in m["pieces"]}
            all_pieces = [p["num"] for p in m["pieces"]]
            classes = m["classes"]
            class_of = {n: c for c in classes for n in c["pieces"]}
            cls = {c["id"]: c for c in classes}
            steps = []
            # 1. nombre de classes
            steps.append({"kind": "input", "prompt": f"**Étape 1.** Après avoir repéré les pièces solidaires (vissées, emmanchées, rivetées…), "
                                                     f"combien de **classes d'équivalence** compte {le(m)} ?",
                          "answer": str(len(classes)), "numeric": True, "tolerance": 0,
                          "explanation": "  ;  ".join(f"{c['id']} = {{{', '.join(map(str, c['pieces']))}}} ({c['nom']})" for c in classes)})
            # 2. composition de la plus grande classe
            big = max(classes, key=lambda c: len(c["pieces"]))
            if len(big["pieces"]) >= 2:
                pp = big["pieces"][0]
                others = [x for x in all_pieces if x not in big["pieces"]]
                r = rng(iid + "classe")
                wrong = [("aucune : elle forme une classe à elle seule", f"Non : {big.get('pourquoi', 'ces pièces sont solidaires.')}")]
                tries = 0
                while len(wrong) < 3 and tries < 20 and others:
                    tries += 1
                    s = sorted(r.sample(others, min(len(others), r.choice([1, 2]))))
                    txt = fmt_pieces(s, m)
                    if txt not in [w[0] for w in wrong]:
                        cx = class_of[s[0]]
                        li = self.liaison_between(m, cx["id"], big["id"])
                        why = (f"Non : la pièce {s[0]} ({names[s[0]]}) est en liaison **{self.by_id[li['liaison']]['nom'].lower()}** avec cette classe : mouvement relatif."
                               if li else f"Non : la pièce {s[0]} ({names[s[0]]}) appartient à une autre classe (« {cx['nom']} »).")
                        wrong.append((txt, why))
                steps.append(dict(kind="mcq", **self.mcq_payload(iid + ".classe",
                    f"**Étape 2.** Quelles pièces forment la même classe d'équivalence que la pièce **{pp} ({names[pp]})** ?\n{fig(m['figures']['dessin'])}",
                    fmt_pieces([x for x in big["pieces"] if x != pp], m), wrong, big.get("pourquoi", ""))))
            # 3. une étape par liaison : contact → liaison
            for k, li in enumerate(m["liaisons"], 3):
                l = self.by_id[li["liaison"]]
                a, b = li["entre"]
                steps.append(dict(kind="mcq", **self.mcq_payload(iid + f".liaison{k}",
                    f"**Étape {k}.** Entre **{a} ({cls[a]['nom']})** et **{b} ({cls[b]['nom']})**, le contact est : **{li['contact']}** "
                    f"({li['surfaces']}). Quelle est la liaison ?\n{fig(m['figures']['classes'])}",
                    l["nom"], self.liaison_choices(l, iid + str(k), lambda o, l=l, li=li: diff_feedback(l, o, li.get("explication", ""))),
                    li.get("explication", ""))))
            k = 3 + len(m["liaisons"])
            # 4. graphe : nombre de liaisons
            steps.append({"kind": "input", "prompt": f"**Étape {k}.** On trace le graphe des liaisons : un cercle par classe, un trait par liaison. "
                                                     f"Combien de **traits** compte-t-il ?",
                          "answer": str(len(m["liaisons"])), "numeric": True, "tolerance": 0,
                          "explanation": f"Une liaison par contact entre deux classes : {len(m['liaisons'])} traits.\n{fig(m['figures']['graphe'])}"})
            k += 1
            # 5. symbole de la première liaison à axe dans le plan du schéma
            for li in m["liaisons"]:
                l = self.by_id[li["liaison"]]
                views = distinct_views(l)
                if len(views) < 2:
                    continue
                axe = li.get("axe", "x")
                # dans le plan (x, y) du schéma : l'axe z est perpendiculaire → vue « bout » ; x ou y → vue « face »
                vue = "bout" if axe == "z" else "face"
                other = "face" if vue == "bout" else "bout"
                why = (f"L'axe ({li['point']}, {axe}) est perpendiculaire au plan (x, y) : on dessine la vue selon l'axe ({l['reconnaitre']['bout']})."
                       if vue == "bout" else
                       f"L'axe ({li['point']}, {axe}) est dans le plan (x, y) : on dessine la vue de face ({l['reconnaitre']['face']}).")
                choices = [(fig(sym_fig(l, other)), f"Non : c'est bien le symbole de la liaison {low_first(l['nom'])}, mais dans l'autre vue. {why}")]
                for o in self.others(l, 5, iid + "sym"):
                    ov = distinct_views(o)
                    if len(ov) >= 2:
                        choices += [(fig(sym_fig(o, v["vue"])), self.fb_figure_de(o, v["vue"])) for v in ov[:2]]
                        break
                steps.append(dict(kind="mcq", **self.mcq_payload(iid + ".symbole",
                    f"**Étape {k}.** Le schéma est tracé dans le plan **(x, y)**. Quel symbole représente la liaison "
                    f"**{designation_complete(l, li)}** ?", fig(sym_fig(l, vue)), choices[:3], why, layout="grid")))
                k += 1
                break
            # 6. la démarche dans l'ordre
            steps.append({"kind": "order", "prompt": f"**Étape {k}.** Pour finir, remets dans l'ordre les cinq étapes de la démarche que tu viens de suivre.",
                          "steps": DEMARCHE, "explanation": "Étudier → classes → contacts et liaisons → graphe → schéma (manuel p. 33)."})
            k += 1
            # 7. lecture du schéma final : première question écrite à la main sur le schéma
            for q in m.get("questions", []):
                if q["type"] == "mcq" and q.get("skill", "schema-2d") == "schema-2d":
                    answers = [q["answer"]] if not isinstance(q["answer"], list) else q["answer"]
                    step = {"kind": "mcq", "prompt": f"**Étape {k}.** Voici le schéma cinématique obtenu. " + q["prompt"],
                            "choices": list(q["choices"]), "answer": answers, "multiple": False, "layout": q.get("layout", "list"),
                            "explanation": q.get("explanation", "")}
                    if q.get("feedback"):
                        step["feedback"] = [None if i in answers else fb for i, fb in enumerate(q["feedback"])]
                    steps.append(step)
                    break
            self.guided(iid, skill, f"{m['titre']} : du dessin d'ensemble au schéma cinématique",
                        f"{m['description'].strip()}\n{fig(m['figures']['dessin'])}\nRepère : {m['repere']}.",
                        steps, tags=[m["id"]])


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

    # --- transmission de mouvement -------------------------------------------------
    def gen_engrenage_rapport(self, skill):
        for z1, z2 in [(20, 60), (15, 45), (30, 20), (12, 48), (25, 50), (40, 10)]:
            R = z1 / z2
            iid = f"{skill}.engrenage_rapport.{z1}-{z2}"
            nature = "réducteur : la roue menée tourne moins vite" if R < 1 else "multiplicateur : la roue menée tourne plus vite"
            self.num_mcq(iid, skill, 1,
                         f"Un engrenage : roue menante Z₁ = {z1} dents, roue menée Z₂ = {z2} dents. "
                         f"Quel est le rapport de transmission R = ω₂ ÷ ω₁ ?\n{fig('transmission-engrenage')}",
                         R, "", [(z2 / z1, "Non : tu as inversé le rapport. R = Z menante ÷ Z menée (= ω sortie ÷ ω entrée)."),
                                 (z1 / (z1 + z2), "Non : on divise par le nombre de dents de la roue menée, pas par le total des dents."),
                                 (1, "Non : les roues n'ont pas le même nombre de dents, elles ne tournent pas à la même vitesse.")],
                         f"R = Z₁ ÷ Z₂ = {z1} ÷ {z2} = {fr(R, 3)} ({nature}).", nd=3, tags=["engrenage"])
            n1 = 1500
            n2 = R * n1
            self.num_mcq(iid + ".vitesse", skill, 2,
                         f"Le même engrenage (Z₁ = {z1}, Z₂ = {z2}) : la roue menante tourne à {fr(n1, 0)} tr/min. "
                         f"À quelle vitesse tourne la roue menée ?", n2, "tr/min",
                         [(n1 / R, "Non : tu as multiplié par l'inverse du rapport ; ω₂ = R × ω₁ avec R = Z₁ ÷ Z₂."),
                          (n1, "Non : les nombres de dents sont différents, la vitesse change."),
                          (n2 * 2 * 3.14159, "Non : la question est en tr/min, il n'y a pas de conversion en rad/s à faire.")],
                         f"ω₂ = R × ω₁ = ({z1} ÷ {z2}) × {fr(n1, 0)} = {fr(n2, 0)} tr/min.", nd=0, tags=["engrenage"])

    def gen_train_rapport(self, skill):
        for z in [(20, 60, 15, 45), (12, 36, 10, 40), (25, 50, 20, 60)]:
            z1, z2, z3, z4 = z
            R = z1 * z3 / (z2 * z4)
            iid = f"{skill}.train_rapport.{'-'.join(map(str, z))}"
            self.num_mcq(iid, skill, 2,
                         f"Train d'engrenages : Z₁ = {z1} (menante), Z₂ = {z2} et Z₃ = {z3} (roues solidaires sur l'arbre intermédiaire), "
                         f"Z₄ = {z4} (roue de sortie). Rapport R = ω₄ ÷ ω₁ ?\n{fig('transmission-train')}",
                         R, "", [(z2 * z4 / (z1 * z3), "Non : c'est l'inverse. R = (produit des Z menantes) ÷ (produit des Z menées) = (Z₁ × Z₃) ÷ (Z₂ × Z₄)."),
                                 (z1 / z4, "Non : les roues intermédiaires comptent ! Z₂ est menée par Z₁, et Z₃ (solidaire de Z₂) mène Z₄."),
                                 (z1 / z2 + z3 / z4, "Non : les rapports des deux engrenages se **multiplient**, ils ne s'additionnent pas.")],
                         f"R = (Z₁ × Z₃) ÷ (Z₂ × Z₄) = ({z1} × {z3}) ÷ ({z2} × {z4}) = {fr(R, 4)}.", nd=4, tags=["engrenage"])

    def gen_roue_vis_rapport(self, skill):
        for z1, z2 in [(1, 40), (2, 50), (1, 60)]:
            R = z1 / z2
            iid = f"{skill}.roue_vis.{z1}-{z2}"
            self.num_mcq(iid, skill, 1,
                         f"Roue et vis sans fin : vis à Z₁ = {z1} filet(s), roue à Z₂ = {z2} dents. Rapport R = ω roue ÷ ω vis ?\n{fig('transmission-roue-vis')}",
                         R, "", [(z2 / z1, "Non : c'est l'inverse ; la roue tourne beaucoup **moins** vite que la vis."),
                                 (z1 / (2 * z2), "Non : il n'y a pas de facteur 2 ; R = nombre de filets ÷ nombre de dents."),
                                 (1, "Non : un tour de vis ne fait avancer la roue que d'une dent (par filet).")],
                         f"R = Z₁ ÷ Z₂ = {z1} ÷ {z2} = {fr(R, 4)} : grand rapport de réduction, et en général irréversible.", nd=4, tags=["roue-vis"])
            n1 = 3000
            self.num_mcq(iid + ".vitesse", skill, 2,
                         f"La vis sans fin ({z1} filet(s)) tourne à {fr(n1, 0)} tr/min ; la roue a {z2} dents. Vitesse de la roue ?",
                         n1 * R, "tr/min", [(n1 * z2 / z1, "Non : la roue tourne moins vite que la vis, pas plus vite."),
                                             (n1 / z2 / 2, "Non : il n'y a pas de facteur 2 supplémentaire."),
                                             (n1, "Non : un réducteur change la vitesse.")],
                         f"ω roue = R × ω vis = ({z1} ÷ {z2}) × {fr(n1, 0)} = {fr(n1 * R, 0)} tr/min.", nd=0, tags=["roue-vis"])

    def gen_poulies_rapport(self, skill):
        for d1, d2 in [(80, 240), (100, 250), (150, 100), (60, 180)]:
            R = d1 / d2
            iid = f"{skill}.poulies.{d1}-{d2}"
            self.num_mcq(iid, skill, 1,
                         f"Poulies-courroie : poulie motrice d₁ = {d1} mm, poulie réceptrice d₂ = {d2} mm. Rapport R = ω₂ ÷ ω₁ ?\n{fig('transmission-poulies')}",
                         R, "", [(d2 / d1, "Non : c'est l'inverse. R = d₁ ÷ d₂ : une grande poulie réceptrice tourne moins vite."),
                                 (d1 / (d1 + d2), "Non : on divise par le diamètre de la poulie réceptrice, pas par la somme."),
                                 (1, "Non : les diamètres sont différents, les vitesses aussi (seule la courroie a une vitesse unique).")],
                         f"R = d₁ ÷ d₂ = {d1} ÷ {d2} = {fr(R, 3)}.", nd=3, tags=["poulies"])
            w1 = 50
            V = w1 * (d1 / 1000) / 2
            self.num_mcq(iid + ".courroie", skill, 2,
                         f"La poulie motrice (d₁ = {d1} mm) tourne à ω₁ = {w1} rad/s. Vitesse de la courroie ?",
                         V, "m/s", [(w1 * d1 / 1000, "Non : V = ω × rayon, et le rayon vaut d₁ ÷ 2."),
                                    (w1 * d1 / 2, "Non : attention aux unités, le diamètre est en mm ; il faut le convertir en m."),
                                    (w1 * (d2 / 1000) / 2, "Non : la courroie va à la vitesse de la poulie **motrice** (mais aussi de la réceptrice : les deux donnent la même valeur si tu utilises ω₂).")],
                         f"V = ω₁ × d₁ ÷ 2 = {w1} × {fr(d1 / 1000, 3)} ÷ 2 = {fr(V, 2)} m/s.", nd=2, tags=["poulies"])

    # --- couple, puissance, rendement ----------------------------------------------
    def gen_couple_sortie(self, skill):
        for ce, R, eta in [(2, 0.1, 0.9), (0.5, 0.05, 0.8), (3, 0.25, 0.95), (1.2, 0.02, 0.7)]:
            cs = eta * ce / R
            iid = f"{skill}.couple_sortie.{ce}-{R}-{eta}"
            self.num_mcq(iid, skill, 2,
                         f"Un réducteur de rapport R = {fr(R, 2)} et de rendement η = {fr(eta, 2)} reçoit un couple C e = {fr(ce, 1)} N·m. Couple de sortie C s ?",
                         cs, "N·m", [(eta * ce * R, "Non : tu as **multiplié** par R. Un réducteur (R < 1) augmente le couple : C s = η × C e ÷ R."),
                                     (ce / R, "Non : tu as oublié le rendement η, qui diminue le couple disponible."),
                                     (eta * ce, "Non : tu as oublié le rapport de réduction, qui multiplie le couple par 1 ÷ R.")],
                         f"C s = η × C e ÷ R = {fr(eta, 2)} × {fr(ce, 1)} ÷ {fr(R, 2)} = {fr(cs, 1)} N·m.", nd=1, tags=["couple"])

    def gen_conversion_trmin(self, skill):
        for n in [1500, 3000, 750, 120, 60, 12000]:
            w = n * 2 * 3.14159265 / 60
            iid = f"{skill}.conversion_trmin.{n}"
            self.num_mcq(iid, skill, 1,
                         f"Convertir N = {fr(n, 0)} tr/min en rad/s.",
                         w, "rad/s", [(n / 60, "Non : tu as converti les minutes en secondes mais oublié qu'un tour vaut 2π rad."),
                                      (n * 2 * 3.14159265, "Non : tu as oublié de passer des minutes aux secondes (÷ 60)."),
                                      (n * 60 / (2 * 3.14159265), "Non : la conversion est ω = N × 2π ÷ 60, pas l'inverse.")],
                         f"ω = N × 2π ÷ 60 = {fr(n, 0)} × 2π ÷ 60 ≈ {fr(w, 1)} rad/s.", nd=1, tags=["conversion"])

    def gen_puissance_rotation(self, skill):
        for c, n in [(2, 3000), (10, 1500), (0.5, 12000), (40, 750)]:
            w = n * 2 * 3.14159265 / 60
            P = c * w
            iid = f"{skill}.puissance.{c}-{n}"
            self.num_mcq(iid, skill, 2,
                         f"Un moteur fournit un couple C = {fr(c, 1)} N·m à N = {fr(n, 0)} tr/min. Quelle puissance mécanique délivre-t-il ?",
                         P, "W", [(c * n, "Non : P = C × ω avec ω en **rad/s** ; il faut convertir les tr/min (× 2π ÷ 60)."),
                                  (c * n / 60, "Non : tu as divisé par 60 mais oublié le facteur 2π."),
                                  (c / w, "Non : la puissance est le **produit** du couple par la vitesse angulaire.")],
                         f"ω = {fr(n, 0)} × 2π ÷ 60 = {fr(w, 1)} rad/s ; P = C × ω = {fr(c, 1)} × {fr(w, 1)} ≈ {fr(P, 0)} W.", nd=0, tags=["puissance"])

    def gen_rendement_global(self, skill):
        for etas in [(0.9, 0.99), (0.9, 0.8), (0.75, 0.96), (0.8, 0.8, 0.8)]:
            prod = 1
            for e in etas:
                prod *= e
            txt = " puis ".join(f"η = {fr(e, 2)}" for e in etas)
            iid = f"{skill}.rendement_global.{'-'.join(str(e) for e in etas)}"
            self.num_mcq(iid, skill, 2,
                         f"Une chaîne de {len(etas)} éléments a pour rendements : {txt}. Rendement global ?",
                         prod, "", [(sum(etas) / len(etas), "Non : le rendement global n'est pas la moyenne ; chaque élément perd une part de ce qu'il reçoit, les rendements se **multiplient**."),
                                    (min(etas), "Non : le maillon le plus faible ne suffit pas, chaque élément ajoute ses pertes."),
                                    (max(etas), "Non : les pertes s'accumulent, le rendement global est plus faible que chacun des rendements.")],
                         f"η global = {' × '.join(fr(e, 2) for e in etas)} = {fr(prod, 3)}, soit {fr(prod * 100, 1)} %.", nd=3, tags=["rendement"])

    # --- transformation de mouvement ---------------------------------------------
    def gen_pignon_cremaillere(self, skill):
        for r, th in [(50, 2), (40, 3), (25, 4)]:
            d = r * th
            iid = f"{skill}.pignon_cremaillere.{r}-{th}"
            self.num_mcq(iid, skill, 1,
                         f"Pignon-crémaillère : rayon primitif r = {r} mm, le pignon tourne de θ = {th} rad. Déplacement d de la crémaillère ?\n{fig('transformation-pignon-cremaillere')}",
                         d, "mm", [(r * th * 2 * 3.14159265, "Non : l'angle est déjà en radians, il n'y a pas de facteur 2π à ajouter."),
                                   (r / th, "Non : d = r × θ (produit), pas un quotient."),
                                   (2 * r * th, "Non : la formule utilise le **rayon** r, pas le diamètre.")],
                         f"d = r × θ = {r} × {th} = {fr(d, 0)} mm (θ en rad).", nd=0, tags=["pignon-cremaillere"])
        for r, tours in [(20, 2), (30, 1.5)]:
            d = r * tours * 2 * 3.14159265
            iid = f"{skill}.pignon_cremaillere_tours.{r}-{tours}"
            self.num_mcq(iid, skill, 2,
                         f"Un pignon de rayon primitif r = {r} mm fait {fr(tours, 1)} tour(s). De combien avance la crémaillère ?",
                         d, "mm", [(r * tours, "Non : dans d = r × θ, l'angle doit être en **radians** : 1 tour = 2π rad."),
                                   (r * tours * 360, "Non : pas en degrés ; 1 tour = 2π rad ≈ 6,28 rad."),
                                   (d / 2, "Non : tu as utilisé r ÷ 2 ; c'est bien le rayon qui intervient.")],
                         f"θ = {fr(tours, 1)} × 2π = {fr(tours * 2 * 3.14159265, 2)} rad ; d = r × θ = {r} × {fr(tours * 2 * 3.14159265, 2)} ≈ {fr(d, 0)} mm.", nd=0, tags=["pignon-cremaillere"])
        for r, w in [(0.05, 10), (0.02, 25)]:
            V = r * w
            iid = f"{skill}.pignon_vitesse.{r}-{w}"
            self.num_mcq(iid, skill, 2,
                         f"Pignon de rayon primitif r = {fr(r * 1000, 0)} mm tournant à ω = {w} rad/s. Vitesse V de la crémaillère ?",
                         V, "m/s", [(r * 1000 * w, "Non : avec r en mm tu obtiens des mm/s ; convertis r en m pour avoir des m/s."),
                                    (w / r, "Non : V = r × ω (produit)."),
                                    (2 * r * w, "Non : c'est le rayon qui intervient, pas le diamètre.")],
                         f"V = r × ω = {fr(r, 3)} × {w} = {fr(V, 2)} m/s.", nd=2, tags=["pignon-cremaillere"])

    def gen_vis_ecrou(self, skill):
        for p, n in [(2, 10), (1.5, 6), (5, 2.5), (1.25, 8)]:
            d = p * n
            iid = f"{skill}.vis_ecrou.{p}-{n}"
            self.num_mcq(iid, skill, 1,
                         f"Vis-écrou : pas p = {fr(p, 2)} mm, la vis fait {fr(n, 1)} tour(s). De combien avance l'écrou ?\n{fig('transformation-vis-ecrou')}",
                         d, "mm", [(p / n, "Non : d = p × n (produit) : chaque tour fait avancer d'un pas."),
                                   (n / p, "Non : d = p × n, pas n ÷ p."),
                                   (p * n * 2 * 3.14159265, "Non : ici l'angle est compté en **tours**, pas en radians : pas de 2π.")],
                         f"d = p × n = {fr(p, 2)} × {fr(n, 1)} = {fr(d, 2)} mm.", nd=2, tags=["vis-ecrou"])
        for p, d in [(2, 30), (1.5, 12)]:
            n = d / p
            iid = f"{skill}.vis_ecrou_tours.{p}-{d}"
            self.num_mcq(iid, skill, 2,
                         f"Vis de pas p = {fr(p, 2)} mm. Combien de tours pour faire avancer l'écrou de {fr(d, 0)} mm ?",
                         n, "tours", [(d * p, "Non : n = d ÷ p ; plus le pas est grand, moins il faut de tours."),
                                      (n / 2, "Non : pas de facteur 2."),
                                      (d - p, "Non : c'est un quotient, pas une différence.")],
                         f"n = d ÷ p = {fr(d, 0)} ÷ {fr(p, 2)} = {fr(n, 1)} tours.", nd=1, tags=["vis-ecrou"])

    # --- cinématique ----------------------------------------------------------------
    def gen_vitesse_moyenne(self, skill):
        for d, tsec, txt in [(150, 30, "150 m en 30 s"), (100, 8, "100 m en 8 s"), (12000, 1200, "12 km en 20 min")]:
            v = d / tsec
            iid = f"{skill}.vitesse_moyenne.{d}-{tsec}"
            self.num_mcq(iid, skill, 1,
                         f"Un mobile parcourt {txt}. Vitesse moyenne ?",
                         v, "m/s", [(tsec / d, "Non : V = d ÷ t (distance divisée par le temps)."),
                                    (v * 3.6, "Non : ce serait la valeur en km/h ; en m/s, divise la distance en m par le temps en s."),
                                    (d * tsec, "Non : c'est un quotient, pas un produit.")],
                         f"V = d ÷ t = {fr(d, 0)} ÷ {fr(tsec, 0)} = {fr(v, 2)} m/s.", nd=2, tags=["vitesse"])
        for kmh in [36, 90, 54, 108]:
            ms = kmh / 3.6
            iid = f"{skill}.kmh.{kmh}"
            self.num_mcq(iid, skill, 1,
                         f"Convertir {kmh} km/h en m/s.",
                         ms, "m/s", [(kmh * 3.6, "Non : de km/h vers m/s on **divise** par 3,6 (1 km = 1 000 m, 1 h = 3 600 s)."),
                                     (kmh / 60, "Non : il faut diviser par 3,6, pas par 60."),
                                     (kmh, "Non : ce ne sont pas les mêmes unités.")],
                         f"{kmh} km/h = {kmh} × 1 000 ÷ 3 600 = {fr(ms, 1)} m/s.", nd=1, tags=["vitesse"])

    def gen_vitesse_point(self, skill):
        for R, w in [(0.3, 20), (0.5, 4), (0.15, 100)]:
            v = R * w
            iid = f"{skill}.vitesse_point.{R}-{w}"
            self.num_mcq(iid, skill, 1,
                         f"Un solide tourne à ω = {w} rad/s. Vitesse d'un point situé à R = {fr(R, 2)} m de l'axe ?\n{fig('cinematique-champ-rotation')}",
                         v, "m/s", [(w / R, "Non : V = R × ω (produit) : plus on est loin de l'axe, plus on va vite."),
                                    (R / w, "Non : V = R × ω, pas R ÷ ω."),
                                    (R + w, "Non : on ne peut pas additionner un rayon et une vitesse angulaire.")],
                         f"V = R × ω = {fr(R, 2)} × {w} = {fr(v, 2)} m/s.", nd=2, tags=["vitesse"])
        for R, n in [(0.2, 300), (0.35, 120)]:
            w = n * 2 * 3.14159265 / 60
            v = R * w
            iid = f"{skill}.vitesse_point_trmin.{R}-{n}"
            self.num_mcq(iid, skill, 2,
                         f"Une roue de rayon R = {fr(R, 2)} m tourne à N = {n} tr/min. Vitesse d'un point de sa périphérie ?",
                         v, "m/s", [(R * n, "Non : convertis d'abord N en rad/s (× 2π ÷ 60) avant d'appliquer V = R × ω."),
                                    (R * n / 60, "Non : tu as divisé par 60 mais oublié le facteur 2π."),
                                    (R * n * 2 * 3.14159265, "Non : tu as oublié de diviser par 60 (minutes → secondes).")],
                         f"ω = {n} × 2π ÷ 60 = {fr(w, 2)} rad/s ; V = R × ω = {fr(R, 2)} × {fr(w, 2)} = {fr(v, 2)} m/s.", nd=2, tags=["vitesse"])

    def gen_composition_vitesses(self, skill):
        for v1, v2, meme in [(20, 4, True), (15, 4, False), (25, 3, True)]:
            v = v1 + v2 if meme else v1 - v2
            sens = "dans le même sens que le camion" if meme else "dans le sens opposé au camion"
            iid = f"{skill}.composition.{v1}-{v2}-{int(meme)}"
            self.num_mcq(iid, skill, 2,
                         f"Un camion (1) roule à {v1} m/s par rapport au sol (0). Sur son plateau, un cascadeur (2) court à {v2} m/s {sens}. "
                         f"Vitesse du cascadeur par rapport au sol ?\n{fig('cinematique-composition')}",
                         v, "m/s", [(v1 - v2 if meme else v1 + v2, "Non : regarde les sens ! Même sens → les vitesses s'ajoutent ; sens opposés → elles se retranchent."),
                                    (v1, "Non : le cascadeur bouge par rapport au camion, sa vitesse par rapport au sol n'est pas celle du camion."),
                                    (v2, "Non : c'est sa vitesse par rapport au **camion** ; par rapport au sol il faut ajouter celle du camion.")],
                         f"V(2/0) = V(2/1) + V(1/0) = {'+' if meme else '−'}{v2} + {v1} = {v} m/s (vecteurs de même direction).", nd=0, tags=["vitesse"])

    def gen_mruv(self, skill):
        for a, v0, tt in [(2, 0, 5), (-1.5, 12, 4), (0.8, 2, 10)]:
            v = a * tt + v0
            iid = f"{skill}.mruv_vitesse.{a}-{v0}-{tt}"
            self.num_mcq(iid, skill, 2,
                         f"Mouvement uniformément varié : v₀ = {fr(v0, 0)} m/s, a = {fr(a, 1)} m/s². Vitesse après t = {tt} s ?",
                         v, "m/s", [(a * tt * tt + v0, "Non : v(t) = a × t + v₀ ; le t² n'apparaît que dans la **position**."),
                                    (v0, "Non : l'accélération n'est pas nulle, la vitesse change."),
                                    (a * tt / 2 + v0, "Non : pas de ½ dans la vitesse ; le ½ est dans la position x(t) = ½ a t² + v₀ t.")],
                         f"v = a × t + v₀ = {fr(a, 1)} × {tt} + {fr(v0, 0)} = {fr(v, 1)} m/s.", nd=1, tags=["acceleration"])
        for a, v0, tt in [(2, 0, 5), (0.5, 0, 8), (1, 5, 4)]:
            x = 0.5 * a * tt * tt + v0 * tt
            iid = f"{skill}.mruv_position.{a}-{v0}-{tt}"
            self.num_mcq(iid, skill, 3,
                         f"Départ en x₀ = 0 avec v₀ = {fr(v0, 0)} m/s et a = {fr(a, 1)} m/s² constante. Distance parcourue après t = {tt} s ?",
                         x, "m", [(a * tt * tt + v0 * tt, "Non : tu as oublié le ½ devant a t²."),
                                  (v0 * tt, "Non : tu as oublié le terme d'accélération ½ a t²." if v0 else "Non : la distance n'est pas nulle, le mobile accélère : x = ½ a t²."),
                                  (0.5 * a * tt + v0 * tt, "Non : c'est t² (le temps au carré) dans le terme ½ a t².")],
                         f"x = ½ a t² + v₀ t = 0,5 × {fr(a, 1)} × {tt}² + {fr(v0, 0)} × {tt} = {fr(x, 1)} m.", nd=1, tags=["acceleration"])

    def gen_acceleration_normale(self, skill):
        for v, r in [(10, 50), (2, 0.5), (30, 100)]:
            an = v * v / r
            iid = f"{skill}.an.{v}-{r}"
            self.num_mcq(iid, skill, 2,
                         f"Un point décrit un cercle de rayon r = {fr(r, 1)} m à la vitesse constante v = {v} m/s. Accélération normale ?\n{fig('cinematique-acceleration')}",
                         an, "m/s²", [(v / r, "Non : a n = v² ÷ r : la vitesse est au **carré**."),
                                      (v * v * r, "Non : on divise par le rayon, on ne multiplie pas."),
                                      (0, "Non : même à vitesse constante, la **direction** de la vitesse change : l'accélération normale n'est pas nulle.")],
                         f"a n = v² ÷ r = {v}² ÷ {fr(r, 1)} = {fr(an, 2)} m/s², dirigée vers le centre.", nd=2, tags=["acceleration"])


GENERATORS = {name[4:]: name for name in dir(Builder) if name.startswith("gen_")}


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


def build():
    liaisons = load_yaml(CONTENT / "liaisons.yaml")["liaisons"]
    mecanismes = [load_yaml(p) for p in sorted((CONTENT / "mecanismes").glob("*.yaml"))]
    units_src = load_yaml(CONTENT / "units.yaml")
    for extra in sorted((CONTENT / "units").glob("*.yaml")) if (CONTENT / "units").exists() else []:
        more = load_yaml(extra) or {}
        units_src["units"].extend(more.get("units", []))
    annales_src = load_yaml(CONTENT / "annales.yaml") if (CONTENT / "annales.yaml").exists() else {"annales": []}
    figures = load_figures()
    tables = lesson_tables(liaisons)
    b = Builder(liaisons, mecanismes)

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
                if name not in GENERATORS:
                    b.errors.append(f"{sid} : générateur inconnu « {name} » (connus : {', '.join(sorted(GENERATORS))})")
                    continue
                getattr(b, GENERATORS[name])(sid)
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
    content = {
        "version": 1,
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "title": units_src.get("title", "Révise STI2D"),
        "figures": {k: v for k, v in figures.items() if k in used},
        "units": units,
        "items": b.items,
        "annales": annales,
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
    text = json.dumps(light, ensure_ascii=False, separators=(",", ":"))
    (DIST / "content.json").write_text(text, encoding="utf-8")
    (DIST / "content.js").write_text("window.CONTENT = " + text + ";\n", encoding="utf-8")


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
