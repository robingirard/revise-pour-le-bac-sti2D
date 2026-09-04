#!/usr/bin/env python3
"""Rend les scans (doubles pages A4 paysage, tournées) en une image PNG par page du livre.

Usage : python3 tools/render_scans.py            (lit ../*.pdf, écrit ../scans/pages/pNNN.png)
Le tableau JOBS donne, pour chaque PDF, le numéro de page du livre de la page de gauche de chaque scan.
"""
import glob
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]          # dossier STI2D/
OUT = ROOT / "scans" / "pages"                      # manuel I2D / 2I2D
OUT_PCM = ROOT / "scans" / "pages-pcm"              # manuel physique-chimie et mathématiques
JOBS_PCM = [
    ("scan_physique_maths/scan_rgirard_2026-09-04-13-56-27.pdf", [(i, 12 + 2 * (i - 1)) for i in range(1, 16)]),
    ("scan_physique_maths/scan_rgirard_2026-09-04-14-00-59.pdf", [(i, 42 + 2 * (i - 1)) for i in range(1, 8)]),
    ("scan_physique_maths/scan_rgirard_2026-09-04-14-02-22.pdf", [(i, 56 + 2 * (i - 1)) for i in range(1, 17)]),
    ("scan_physique_maths/scan_rgirard_2026-09-04-14-05-06.pdf", [(i, 94 + 2 * (i - 1)) for i in range(1, 17)]),
    ("scan_physique_maths/scan_rgirard_2026-09-04-14-07-28.pdf", [(i, 128 + 2 * (i - 1)) for i in range(1, 17)]),
    ("scan_physique_maths/scan_rgirard_2026-09-04-14-09-55.pdf", [(i, 158 + 2 * (i - 1)) for i in range(1, 12)]),
    ("scan_physique_maths/scan_rgirard_2026-09-04-14-11-48.pdf", [(i, 180 + 2 * (i - 1)) for i in range(1, 13)]),
]
JOBS = [
    ("scan_rgirard_2026-09-04-08-46-36.pdf", [(1, 24)]),
    ("scan_rgirard_2026-09-04-08-48-06.pdf", [(i, 26 + 2 * (i - 1)) for i in range(1, 7)]
     + [(i, 54 + 2 * (i - 7)) for i in range(7, 17)] + [(i, 96 + 2 * (i - 17)) for i in range(17, 21)]),
    ("scan_rgirard_2026-09-04-13-29-14.pdf", [(i, 108 + 2 * (i - 1)) for i in range(1, 7)]),
    ("scan_rgirard_2026-09-04-13-35-49.pdf", [(i, 152 + 2 * (i - 1)) for i in range(1, 18)]),
    ("scan_rgirard_2026-09-04-13-38-35.pdf", [(i, 184 + 2 * (i - 1)) for i in range(1, 13)]),
    ("scan_rgirard_2026-09-04-13-40-43.pdf", [(i, 240 + 2 * (i - 1)) for i in range(1, 16)]),
    ("scan_rgirard_2026-09-04-13-43-19.pdf", [(i, 270 + 2 * (i - 1)) for i in range(1, 15)]),
    ("scan_rgirard_2026-09-04-13-45-42.pdf", [(i, 306 + 2 * (i - 1)) for i in range(1, 16)]),
]


def render(jobs, out, dpi=120):
    out.mkdir(parents=True, exist_ok=True)
    tmp = tempfile.mkdtemp()
    n = 0
    for pdf, pages in jobs:
        src = ROOT / pdf
        if not src.exists():
            print("absent :", pdf, file=sys.stderr)
            continue
        subprocess.run(["pdftoppm", "-r", str(dpi), "-png", str(src), f"{tmp}/x"], check=True)
        files = sorted(glob.glob(f"{tmp}/x-*.png"))
        for idx, left in pages:
            im = Image.open(files[idx - 1]).rotate(-90, expand=True)   # scan tourné d'un quart de tour
            w, h = im.size
            for k, num in ((0, left), (1, left + 1)):
                im.crop((k * w // 2, 0, (k + 1) * w // 2, h)).save(out / f"p{num:03d}.png", optimize=True)
                n += 1
        for f in files:
            os.remove(f)
    print(n, "pages →", out)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "i2d"):
        render(JOBS, OUT)
    if which in ("all", "pcm"):
        render(JOBS_PCM, OUT_PCM)
