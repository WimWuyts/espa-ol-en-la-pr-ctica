#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render_avatars.py — rendert de ECHTE cast-avatars (flat-vector SVG uit
02-huisstijl/beeld/generators/cast_gen.py) naar transparante hoge-resolutie PNG's
in 03-build/pptx/assets/.  Vervangt de grijze Pillow-placeholders (make_avatars.py).

Bestandsnamen (identiek aan wat gen_u0_*.py verwacht):
  lucia.png · diego.png · valen.png · nina.png · tu.png · mochila.png

Renderpad: cairosvg (SVG -> transparante PNG). Fallback: headless Chromium screenshot.
"""
import os, sys, re

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
GEN = os.path.abspath(os.path.join(HERE, "..", "..", "02-huisstijl", "beeld", "generators"))
os.makedirs(ASSETS, exist_ok=True)
sys.path.insert(0, GEN)

import cast_gen as C

PX = 600  # uitvoerresolutie (ruim voor 300 dpi bij ~1.5 inch plaatsing)


def square_mochila(svg):
    """De mochila-SVG heeft viewBox '0 0 220 250' (niet vierkant). Maak er een
    vierkante viewBox van zodat de rugzak niet uitgerekt wordt wanneer gen_u0
    hem als vierkant plaatst."""
    return svg.replace('viewBox="0 0 220 250"', 'viewBox="-15 0 250 250"', 1)


def build_svgs():
    out = {}
    for name in ["lucia", "diego", "valen", "nina"]:
        out[name] = C.make(name, "avatar", w=PX)
    out["tu"] = C.tu_avatar(w=PX)
    out["mochila"] = square_mochila(C.mochila(w=PX))
    return out


def render_cairosvg(svgs):
    import cairosvg
    for name, svg in svgs.items():
        png = os.path.join(ASSETS, f"{name}.png")
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=png,
                         output_width=PX, output_height=PX, background_color="transparent")
        print("  avatar:", name, "->", png)


def render_chromium(svgs):
    """Fallback: elke SVG in een minimale HTML, Chromium --screenshot."""
    import subprocess, tempfile
    CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
    for name, svg in svgs.items():
        html = (f'<!doctype html><meta charset=utf-8>'
                f'<style>html,body{{margin:0;background:transparent}}'
                f'svg{{width:{PX}px;height:{PX}px;display:block}}</style>{svg}')
        with tempfile.NamedTemporaryFile("w", suffix=".html", dir=ASSETS, delete=False) as f:
            f.write(html); hp = f.name
        png = os.path.join(ASSETS, f"{name}.png")
        subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
                        "--default-background-color=00000000",
                        f"--screenshot={png}", f"--window-size={PX},{PX}",
                        "--hide-scrollbars", f"file://{hp}"],
                       check=True, capture_output=True)
        os.unlink(hp)
        print("  avatar (chromium):", name, "->", png)


def main():
    svgs = build_svgs()
    try:
        render_cairosvg(svgs)
        print("render: cairosvg OK")
    except Exception as e:
        print("cairosvg faalde (%s) -> Chromium-fallback" % e)
        render_chromium(svgs)
    print("klaar ->", ASSETS)


if __name__ == "__main__":
    main()
