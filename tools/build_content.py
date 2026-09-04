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

    def mcq(self, iid, skill, level, prompt, correct, distractors, explanation="", layout="list", tags=(), feedback=None):
        """distractors : liste de textes, ou de couples (texte, feedback). feedback : dict texte → feedback."""
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
        return self.add({"id": iid, "skill": skill, "type": "mcq", "level": level, "tags": list(tags), "payload": payload})

    def flashcard(self, iid, skill, level, front, back, tags=()):
        return self.add({"id": iid, "skill": skill, "type": "flashcard", "level": level, "tags": list(tags),
                         "payload": {"front": front, "back": back}})

    def grid(self, iid, skill, level, prompt, rows, cols, answer, explanation="", labels=None, tags=(), cell_feedback=None):
        payload = {"prompt": prompt, "rows": rows, "cols": cols, "answer": list(answer), "explanation": explanation}
        if labels:
            payload["labels"] = labels
        if cell_feedback:
            payload["cellFeedback"] = cell_feedback
        return self.add({"id": iid, "skill": skill, "type": "grid", "level": level, "tags": list(tags), "payload": payload})

    def match(self, iid, skill, level, prompt, pairs, tags=()):
        return self.add({"id": iid, "skill": skill, "type": "match", "level": level, "tags": list(tags),
                         "payload": {"prompt": prompt, "pairs": pairs}})

    def order(self, iid, skill, level, prompt, steps, tags=()):
        return self.add({"id": iid, "skill": skill, "type": "order", "level": level, "tags": list(tags),
                         "payload": {"prompt": prompt, "steps": steps}})

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
                      labels=q.get("labels"), tags=q.get("tags", []), cell_feedback=q.get("cellFeedback"))
        elif t == "order":
            self.order(iid, skill, level, q["prompt"], list(q["steps"]), tags=q.get("tags", []))
        elif t == "input":
            self.input(iid, skill, level, q["prompt"], q["answer"], q.get("accept", []), q.get("numeric", False),
                       q.get("tolerance", 0), q.get("unit", ""), q.get("explanation", ""), tags=q.get("tags", []))
        elif t == "match":
            self.match(iid, skill, level, q["prompt"], list(q["pairs"]), tags=q.get("tags", []))
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
        units.append({"id": u["id"], "title": u["title"], "description": u.get("description", ""), "skills": skills})

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
    }
    return content


def write_dist(content):
    DIST.mkdir(exist_ok=True)
    if APP.exists():
        shutil.copytree(APP, DIST, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns("dev", "tests", "content.js", "*.py", "package.json", ".gitignore", ".DS_Store", "node_modules"))
    text = json.dumps(content, ensure_ascii=False, separators=(",", ":"))
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
