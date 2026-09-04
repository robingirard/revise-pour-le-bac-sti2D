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
OUT = ROOT / "scans" / "pages"
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


def main(dpi=120):
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = tempfile.mkdtemp()
    n = 0
    for pdf, pages in JOBS:
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
                im.crop((k * w // 2, 0, (k + 1) * w // 2, h)).save(OUT / f"p{num:03d}.png", optimize=True)
                n += 1
        for f in files:
            os.remove(f)
    print(n, "pages →", OUT)


if __name__ == "__main__":
    main()
