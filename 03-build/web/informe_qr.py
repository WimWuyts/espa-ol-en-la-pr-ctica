#!/usr/bin/env python3
"""Waar wijst elke QR-code in het boek naartoe? — controle vóór het drukken.

De vraag van de auteur was: «er staan een heleboel QR-codes die nog nergens
naartoe leiden». Dat klopte: ze waren cosmetisch. Nu dragen ze een echt adres,
en dit script laat zien welk — zónder te moeten scannen. Het leest het
`data-url`-attribuut dat `enlaces.tarjeta_qr` meegeeft, en controleert per code:

  · staat het anker écht op de bijbehorende hub-pagina? (zo niet: FOUT)
  · wijst de code naar een specifieke oefening of alleen naar een paneel?

Een paneelverwijzing is niet fout — «neem hier iets op» hoort bij het
spreekpaneel als geheel — maar de auteur vroeg om zo specifiek mogelijk te
verwijzen, dus het verschil is de moeite waard om te zien.

    python3 03-build/web/informe_qr.py
    python3 03-build/web/informe_qr.py --breed   # met elke regel apart
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

import enlaces as EN          # noqa: E402

PANELES = ("vocab", "gram", "lectura", "escuchar", "juegos", "retos",
           "hablar", "cultura", "extra")

TARJETA = re.compile(
    r'<div class="qr" data-url="(?P<url>[^"]*)".*?'
    r'<div class="lab">(?P<lab>.*?)</div>'
    r'(?:<div class="meta">(?P<meta>.*?)</div>)?', re.S)


def unidades():
    for u in range(9):
        p = "%s/01-cursussen/05-a1/U%d/U%d.html" % (ROOT, u, u)
        if os.path.exists(p):
            yield ("C5", u, p, os.path.join(HERE, "U%d_web.html" % u))
    for u in range(8):
        d = "%s/01-cursussen/06-vervolg/U%d" % (ROOT, u)
        for nombre in ("C6plus_U%d.html" % u, "U%d.html" % u):
            p = os.path.join(d, nombre)
            if os.path.exists(p):
                yield ("C6+", u, p, os.path.join(HERE, "C6plus_U%d_web.html" % u))
                break


def anclas_de(ruta_hub):
    """Alle id's die op de hub bestaan — het antwoord op «leidt dit ergens heen?»."""
    if not os.path.exists(ruta_hub):
        return None
    d = open(ruta_hub, encoding="utf-8").read()
    ids = set(re.findall(r'\bid="([^"]+)"', d))
    # de panelen worden bij naam gerouteerd, niet via een id
    ids |= set(PANELES)
    # De ankers van de luisterfragmenten en de retos staan niet als id in de
    # HTML: de hub bouwt die kaarten in JavaScript en zet het id pas dan
    # (`if(f.ancla)it.id=f.ancla`). Het anker staat wél in de meegeleverde
    # data, dus dáár tellen we ze — anders meldt de controle vals alarm.
    ids |= set(re.findall(r'["\']ancla["\']\s*:\s*["\']([a-z0-9-]+)["\']', d))
    return ids


def main():
    breed = "--breed" in sys.argv
    n_tot = n_esp = n_pan = 0
    malos = []
    for curso, u, ruta, hub in unidades():
        doc = open(ruta, encoding="utf-8").read()
        ids = anclas_de(hub)
        filas = []
        for m in TARJETA.finditer(doc):
            url, lab = m.group("url"), re.sub(r"<[^>]+>", "", m.group("lab") or "")
            ancla = url.split("#")[1] if "#" in url else ""
            especifico = bool(ancla) and ancla not in PANELES
            existe = ids is None or not ancla or ancla in ids
            n_tot += 1
            n_esp += especifico
            n_pan += (bool(ancla) and not especifico)
            if not existe:
                malos.append((curso, u, lab, ancla))
            filas.append((lab, ancla, especifico, existe))
        print("%-4s U%d  %2d codes · %2d naar een oefening · %2d naar een paneel"
              % (curso, u, len(filas), sum(1 for f in filas if f[2]),
                 sum(1 for f in filas if f[1] and not f[2])))
        if breed:
            for lab, ancla, esp, existe in filas:
                print("        %-26s → #%-26s %s"
                      % (lab[:26], ancla or "(pagina)",
                         "" if existe else "◀ ANKER BESTAAT NIET"))

    print("\n%d QR-codes: %d naar een specifieke oefening, %d naar een paneel, "
          "%d naar de paginatop" % (n_tot, n_esp, n_pan, n_tot - n_esp - n_pan))
    if malos:
        print("\n%d codes wijzen naar een anker dat niet bestaat:" % len(malos))
        for curso, u, lab, ancla in malos:
            print("   %-4s U%d  %-28s #%s" % (curso, u, lab[:28], ancla))
        sys.exit(1)
    print("elk anker bestaat op de hub · basis: %s" % EN.BASE)


if __name__ == "__main__":
    main()
