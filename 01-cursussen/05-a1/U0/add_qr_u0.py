#!/usr/bin/env python3
"""Vervangt de nep-QR's in de handgebouwde U0.html door echte, gerichte codes.

U0 is de enige unit zonder generator — ze is met de hand gebouwd en daarna met
`add_bloques_u0.py` en `add_retos_u0.py` aangevuld. Dit script doet voor de
QR-codes wat `qr_print.py` voor de zestien andere units doet: het zoekt per
kaart het juiste anker op de hub en tekent er een echte code voor.

Herhaalbaar: een kaart die al een echte code bevat, wordt overgeslagen.
"""
import os
import re
import sys

ROOT = "/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, os.path.join(ROOT, "03-build", "web"))

import enlaces as EN          # noqa: E402
import qr_print as QRP        # noqa: E402

DOEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "U0.html")

# Twee kaarten wijzen niet naar een audiofragment; die krijgen hun doel hier.
MANUAL = {
    "Página U0 · repaso · juegos": EN.ancla_panel("juegos"),
    "Audio V · Decks A–E · 5:00": EN.ancla_panel("vocab"),
}

PATRON = re.compile(
    r'<div class="qr">\s*<svg.*?</svg>\s*'
    r'<div class="lab">(?P<lab>.*?)</div><div class="meta">(?P<meta>.*?)</div></div>',
    re.S)


def main():
    QRP.fijar("C5", 0)
    doc = open(DOEL, encoding="utf-8").read()
    if 'aria-label="QR-code"' in doc:
        print("U0.html heeft al echte codes — niets gedaan")
        return

    hechos = []

    def sustituir(m):
        lab, meta = m.group("lab"), m.group("meta")
        if meta in MANUAL:
            destino = EN.url("C5", 0, MANUAL[meta])
            hoe = "handmatig"
        else:
            destino, hoe = QRP.destino_de(lab, meta)
        hechos.append((lab, meta, destino.split("/")[-1], hoe))
        return EN.tarjeta_qr(destino, lab, meta)

    nuevo, n = PATRON.subn(sustituir, doc)
    if n == 0:
        sys.exit("geen QR-kaarten gevonden — is het patroon veranderd?")
    open(DOEL, "w", encoding="utf-8").write(nuevo)

    print("U0.html: %d codes vervangen\n" % n)
    for lab, meta, destino, hoe in hechos:
        marca = "  " if hoe != "GEEN MATCH" else "! "
        print("%s%-20s %-34s → %-28s %s" % (marca, lab, meta[:34], destino, hoe))


if __name__ == "__main__":
    main()
