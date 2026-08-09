#!/usr/bin/env python3
"""Zet de hele site klaar als één map, klaar om te uploaden.

WAAROM
De gebouwde bestanden staan verspreid over de repo en heten daar zoals de
generator ze noemt (`U5_web.html`, `componentes/C4_U3_hub.html`). Op de site
moeten ze anders heten (`c5-u5.html`, `c4-u3.html`), want dáár zijn de adressen
op gebouwd waar de QR-codes in de gedrukte cursussen naar wijzen. Dit script
maakt daar één map van waarin alles al de juiste naam draagt, zodat uploaden
één handeling is: de map erop slepen.

WAT HET OOK DOET, EN DAAR GAAT HET EIGENLIJK OM
Het rekent na of élke link op de voordeur ook echt bij een bestand in de map
uitkomt. Een portaal met een dode link merk je anders pas als er een leerling
voor staat.

    python3 03-build/preparar_sitio.py
    python3 03-build/preparar_sitio.py --zip     # er ook een zip van maken
"""
import os
import re
import shutil
import sys
import zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(RAIZ, "03-build", "web")
sys.path.insert(0, WEB)

import enlaces as EN                          # noqa: E402

DESTINO = os.path.join(RAIZ, "03-build", "sitio")

LEEME = """SITE «Español en la práctica» — klaar om te uploaden
====================================================

Deze map is de hele website. Sleep de MAP (niet de losse bestanden) op het
uploadvak van je hoster; alles staat al onder de juiste naam.

  index.html        de voordeur: kies een cursus, dan een unidad
  c4-u1 … c4-u14    ¡Bienvenidos al español!   (4 Moderne talen)
  c5-u0 … c5-u8     Español en la práctica     (5de jaar)
  c6plus-u0 … u7    Más español · edición única (6de jaar)
  conjugador.html   werkwoorden opzoeken en zelf vervoegen

Elke pagina staat op zichzelf: de audio, de spellen, de woordkaarten en de
oefeningen zitten erin. Er is geen database, geen server en geen account nodig.
Een leerling die de pagina bewaart, houdt een werkende pagina over.

BELANGRIJK — het adres moet kloppen vóór je de cursussen afdrukt
De QR-codes in de gedrukte cursussen wijzen naar:

    %(base)s

Wordt dat een ander adres, geef het dan door: het staat op één plaats in de
code (BASE in 03-build/web/enlaces.py). Daarna moeten de units één keer
opnieuw gebouwd worden, en pas dán afdrukken.
"""


def main():
    hacer_zip = "--zip" in sys.argv
    if os.path.isdir(DESTINO):
        shutil.rmtree(DESTINO)
    os.makedirs(DESTINO)

    filas = EN.manifiesto()
    total = 0
    for src, dest, _wat in filas:
        origen = os.path.join(RAIZ, src)
        if not os.path.exists(origen):
            print("   ONTBREEKT: %s" % src)
            continue
        shutil.copy2(origen, os.path.join(DESTINO, dest))
        total += os.path.getsize(origen)

    open(os.path.join(DESTINO, "LEEME.txt"), "w", encoding="utf-8").write(
        LEEME % {"base": EN.BASE})

    # ── de controle die ertoe doet: komt elke link ergens uit? ──────────────
    hay = set(os.listdir(DESTINO))
    indice = os.path.join(DESTINO, "index.html")
    rotos, externos = [], []
    if os.path.exists(indice):
        doc = open(indice, encoding="utf-8").read()
        for href in re.findall(r'<a[^>]+href="([^"]+)"', doc):
            if href.startswith(("http://", "https://", "#", "mailto:")):
                externos.append(href)
            elif href not in hay:
                rotos.append(href)

    n = len([f for f in os.listdir(DESTINO) if f.endswith(".html")])
    print("map klaar: %s" % os.path.relpath(DESTINO, RAIZ))
    print("   %d pagina's · %.1f MB · grootste %s"
          % (n, total / 1e6,
             max(((os.path.getsize(os.path.join(DESTINO, f)), f)
                  for f in os.listdir(DESTINO) if f.endswith(".html")))[1]))
    print("   links op de voordeur: %d dood%s%s"
          % (len(rotos), "" if not rotos else " → " + ", ".join(rotos),
             "" if not externos else " · %d extern" % len(externos)))
    if rotos:
        sys.exit("er staan dode links op de voordeur — niet uploaden")

    if hacer_zip:
        ruta = os.path.join(RAIZ, "03-build", "sitio.zip")
        with zipfile.ZipFile(ruta, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(os.listdir(DESTINO)):
                z.write(os.path.join(DESTINO, f), f)
        print("   zip: %s (%.1f MB)"
              % (os.path.relpath(ruta, RAIZ), os.path.getsize(ruta) / 1e6))


if __name__ == "__main__":
    main()
