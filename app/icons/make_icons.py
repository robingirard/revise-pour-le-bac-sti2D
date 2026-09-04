#!/usr/bin/env python3
"""Génère les icônes PNG de l'appli (même dessin que icon.svg : symbole de liaison pivot)."""
from pathlib import Path
from PIL import Image, ImageDraw

HERE = Path(__file__).parent
BLUE, WHITE, AMBER = (37, 99, 235, 255), (255, 255, 255, 255), (251, 191, 36, 255)


def make(size: int, path: Path) -> None:
    im = Image.new("RGBA", (size, size), BLUE)  # fond plein : iOS et Android arrondissent eux-mêmes
    d = ImageDraw.Draw(im)
    s = size / 100
    w = max(3, round(6 * s))
    d.line([(50 * s, 14 * s), (50 * s, 34 * s)], fill=AMBER, width=w)
    d.ellipse([32 * s, 34 * s, 68 * s, 70 * s], outline=WHITE, width=w)
    d.line([(50 * s, 70 * s), (50 * s, 88 * s)], fill=WHITE, width=w)
    im.save(path)


if __name__ == "__main__":
    for size, name in [(192, "icon-192.png"), (512, "icon-512.png"), (180, "apple-touch-icon.png")]:
        make(size, HERE / name)
        print("écrit", HERE / name)
