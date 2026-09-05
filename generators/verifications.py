"""Vérifications propres au paquet STI2D : liaisons, animations des symboles, mécanismes.

Le moteur (`tools/validate.py`) vérifie ce qui vaut pour tout paquet — unités, compétences,
prérequis, exercices construits. Ce qui suit ne vaut que pour ce paquet-ci : qu'une liaison ait six
mobilités et efforts indépendants, que son symbole compilé porte l'animation attendue, qu'une pièce
de mécanisme appartienne à exactement une classe d'équivalence.

Le moteur appelle `verifier()` s'il la trouve sur le module de générateurs déclaré dans `pack.yaml`.
"""
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
CONTENT = RACINE / "content"
err = warn = None      # injectés par verifier() : le moteur seul décide quoi faire d'une erreur


STY = RACINE / "figures" / "tikz" / "liaisons.sty"
SVGDIR = RACINE / "figures" / "build" / "svg"
DDL = {"Tx", "Ty", "Tz", "Rx", "Ry", "Rz"}
EFF = {"X", "Y", "Z", "L", "M", "N"}
PAIR = {"Tx": "X", "Ty": "Y", "Tz": "Z", "Rx": "L", "Ry": "M", "Rz": "N"}
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
MOUVEMENTS = {"rot", "rock", "tx", "ty", "wander", "tilt"}
AMBIGUITES_ADMISES = {("pivot", "face"), ("helicoidale", "face"), ("pivot-glissant", "face"),
                      ("lineaire-rectiligne", "face")}
def check_animations(liaisons):
    """Vérifie les animations des symboles : chaque mouvement déclaré doit correspondre à un ddl
    réel, deux liaisons ne doivent pas s'animer à l'identique dans une même vue, et le symbole
    compilé doit porter les attributs attendus (data-anim, data-axial)."""
    vues = {}
    for l in liaisons:
        for s in l["symboles"]:
            anim = s.get("anim", "none")
            anim = anim if isinstance(anim, list) else ([] if anim == "none" else [anim])
            p = f"liaison {l['id']} ({s['vue']})"
            bad = set(anim) - MOUVEMENTS
            if bad:
                err(f"{p} : mouvements inconnus {bad}")
            h, v = s["plan"]                          # axes du plan de la vue
            visee = ({"x", "y", "z"} - set(s["plan"])).pop()
            # un mouvement ne se déclare que s'il correspond à une mobilité de la liaison
            attendus = {
                "rot": f"R{visee}" in l["ddl"], "rock": f"R{visee}" in l["ddl"],
                "tx": f"T{h}" in l["ddl"], "ty": f"T{v}" in l["ddl"],
                "wander": f"T{h}" in l["ddl"] and f"T{v}" in l["ddl"],
                "tilt": bool({f"R{h}", f"R{v}"} & set(l["ddl"])),
            }
            for m in anim:
                if m in attendus and not attendus[m]:
                    err(f"{p} : mouvement « {m} » sans mobilité correspondante (ddl : {l['ddl']})")
            axial = ("lie" if l.get("ddl_lies") else "libre") if f"T{visee}" in l["ddl"] else None
            cle = (s["vue"], " ".join(sorted(anim)), axial)
            if cle in vues and (l["id"], s["vue"]) not in AMBIGUITES_ADMISES:
                warn(f"{p} : même animation que {vues[cle]} — les deux liaisons sont indistinguables")
            vues[cle] = f"{l['id']} ({s['vue']})"
    check_animations_svg(liaisons)
def check_animations_svg(liaisons):
    """Les attributs du SVG compilé doivent refléter le YAML (sinon : « make figures » à relancer)."""
    for l in liaisons:
        for s in l["symboles"]:
            svg = SVGDIR / f"liaison-{l['id']}-{s['vue']}.svg"
            if not svg.exists():
                continue   # figure pas encore compilée : « make figures » s'en charge
            tag = re.search(r"<svg\b[^>]*>", svg.read_text(encoding="utf-8"))
            attrs = tag.group(0) if tag else ""
            def attr(name, defaut=None):
                m = re.search(rf'{name}="([^"]+)"', attrs)
                return m.group(1) if m else defaut
            visee = ({"x", "y", "z"} - set(s["plan"])).pop()
            axial = ("lie" if l.get("ddl_lies") else "libre") if f"T{visee}" in l["ddl"] else None
            anim = s.get("anim", "none")
            anim = " ".join(anim) if isinstance(anim, list) else anim
            p = f"liaison {l['id']} ({s['vue']})"
            if attr("data-axial") != axial:
                err(f"{p} : data-axial = {attr('data-axial')!r}, attendu {axial!r} — relancez « make figures »")
            if attr("data-anim", "none") != anim:
                err(f"{p} : data-anim = {attr('data-anim')!r}, attendu {anim!r} — relancez « make figures »")
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


def verifier(racine, donnees, signaler_erreur, signaler_avertissement, load_yaml):
    """Contrôles du paquet. Renvoie le résumé que `validate.py` ajoute à sa ligne finale."""
    global RACINE, CONTENT, STY, SVGDIR, err, warn
    RACINE = Path(racine)
    CONTENT = RACINE / "content"
    STY = RACINE / "figures" / "tikz" / "liaisons.sty"
    SVGDIR = RACINE / "figures" / "build" / "svg"
    err, warn = signaler_erreur, signaler_avertissement

    liaisons = load_yaml(RACINE / donnees["liaisons"])["liaisons"]
    ids = check_liaisons(liaisons)
    check_animations(liaisons)
    dossier = RACINE / donnees["mecanismes"]
    mecanismes = [load_yaml(p) for p in sorted(dossier.glob("*.yaml"))] if dossier.exists() else []
    check_mecanismes(mecanismes, ids)
    return f"{len(liaisons)} liaisons, {len(mecanismes)} mécanismes"
