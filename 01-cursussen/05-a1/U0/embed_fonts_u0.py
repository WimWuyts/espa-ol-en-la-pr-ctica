#!/usr/bin/env python3
"""Embedt de huisstijlfonts in de printlaag van C5 U0.

De CSS van deze unit verwijst naar 'Bricolage Grotesque', 'Inter' en 'Caveat',
maar er stond geen enkele @font-face in het bestand. Chromium viel dus terug op
een systeemfont, en de PDF was niet reproduceerbaar: dezelfde HTML gaf 62
bladzijden op de ene machine en 57 op de andere, omdat de regelafbreking
meeschuift met het vervangende font. CLAUDE.md §6 vraagt de fonts ingebed in
álle formaten — de hub en de C6+-printlaag doen dat al, deze unit niet.

Idempotent: draait de tweede keer zonder effect.

    python3 01-cursussen/05-a1/U0/embed_fonts_u0.py
"""
import base64
import io
import os
import re
import sys

ROOT = "/home/user/espa-ol-en-la-pr-ctica"
DOEL = os.path.join(ROOT, "01-cursussen/05-a1/U0/U0.html")
FONTDIR = os.path.join(ROOT, "02-huisstijl/fonts")

# Dezelfde zeven gezichten als gen_u0_print.py van C6+ — één huisstijl, één set.
FACES = [
    ("Bricolage Grotesque", "BricolageGrotesque-700.woff2", "700"),
    ("Bricolage Grotesque", "BricolageGrotesque-800.woff2", "800"),
    ("Bricolage Grotesque XBold", "BricolageGrotesque-800.woff2", "800"),
    ("Inter", "Inter-400.woff2", "400"),
    ("Inter", "Inter-600.woff2", "600"),
    ("Inter", "Inter-700.woff2", "700"),
    ("Caveat", "Caveat-700.woff2", "700"),
]


def face(fam, fn, w):
    p = os.path.join(FONTDIR, fn)
    if not os.path.exists(p):
        sys.exit("Font ontbreekt: %s" % p)
    b = base64.b64encode(open(p, "rb").read()).decode()
    return ("@font-face{font-family:'%s';src:url(data:font/woff2;base64,%s) "
            "format('woff2');font-weight:%s;font-display:swap}" % (fam, b, w))


def main():
    s = io.open(DOEL, encoding="utf-8").read()
    if "@font-face" in s:
        print("Fonts stonden er al in — niets gedaan.")
        return
    m = re.search(r"<style[^>]*>", s)
    if not m:
        sys.exit("Geen <style> gevonden in %s" % DOEL)
    fonts = "".join(face(*f) for f in FACES)
    s = s[:m.end()] + fonts + s[m.end():]
    io.open(DOEL, "w", encoding="utf-8").write(s)
    print("%d fonts ingebed in %s (+%.0f kB)"
          % (len(FACES), os.path.relpath(DOEL, ROOT), len(fonts) / 1024))


if __name__ == "__main__":
    main()
