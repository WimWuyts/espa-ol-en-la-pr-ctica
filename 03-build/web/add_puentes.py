#!/usr/bin/env python3
"""Zet de verwijzing boek → PowerPoint in elke hoofdsectie van elke unit.

Waarom als nabewerking en niet in de zeventien generatoren: het dianummer komt
uit het deck, en dat deck verandert (de reto-dia's kwamen er later bij). Door de
brug ná de bouw te leggen, klopt hij altijd met het deck dat er op dat moment
ligt — en één script vervangt zeventien keer handwerk.

De brug komt onder de intro van de sectie te staan, in de bestaande
`route-note`-stijl, zodat hij naast de al bestaande «oefen online»-verwijzing
past. Secties waarvoor geen dia bestaat, krijgen niets: liever geen verwijzing
dan een verwijzing naar een dia die er niet is.

Herhaalbaar: bestaande bruggen worden vervangen, niet verdubbeld.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import puentes as PU          # noqa: E402

ROOT = "/home/user/espa-ol-en-la-pr-ctica"
MARCA_INI = "<!-- puente-ppt -->"

# Welk gebouwd bestand hoort bij welke unit.
def unidades():
    for u in range(9):
        p = "%s/01-cursussen/05-a1/U%d/U%d.html" % (ROOT, u, u)
        if os.path.exists(p):
            yield ("C5", u, p)
    for u in range(8):
        d = "%s/01-cursussen/06-vervolg/U%d" % (ROOT, u)
        for nombre in ("C6plus_U%d.html" % u, "U%d.html" % u):
            p = os.path.join(d, nombre)
            if os.path.exists(p):
                yield ("C6+", u, p)
                break


# De sectiekop ziet er zo uit: <span class="pk">§2 · El verbo SER …</span>
# gevolgd door <div class="intro">…</div>. Daarachter zetten we de brug.
SECCION = re.compile(
    r'(<span class="pk"[^>]*>(?P<tit>[^<]+)</span>'
    r'(?:<div class="lpd">.*?</div>)?'
    r'<div class="intro">.*?</div>)', re.S)

# Secties waar een dia-verwijzing niets toevoegt.
SALTAR = ("Vocabulario", "Repaso", "Taller de lengua", "¡Ponte al día!")


def clave_de(titulo):
    """Van «§2 · El verbo SER + los pronombres» naar de zoekwoorden voor het deck.

    Staat de titel van de tekst tussen guillemets — «El primer día en el
    instituto» — dan is dát het beste zoekwoord: de dia draagt dezelfde naam."""
    cita = re.search(r"«([^»]{4,44})»", titulo)
    if cita:
        return [cita.group(1)]
    t = re.sub(r"^[§\w.]+\s*·\s*", "", titulo).strip()
    t = re.sub(r"\s*[·—-]\s*.*$", "", t).strip()      # alleen het eerste deel
    # de kernwoorden: laat lidwoorden en voorzetsels vallen
    palabras = [w for w in re.split(r"[\s/]+", t)
                if len(w) > 2 and w.lower() not in
                ("los", "las", "del", "con", "por", "para", "que", "una", "uno")]
    return palabras[:2] or [t]


def procesar(curso, unidad, ruta):
    doc = open(ruta, encoding="utf-8").read()
    # oude bruggen eruit, zodat het script herhaalbaar is
    doc = re.sub(re.escape(MARCA_INI) + r'<div class="route-note">.*?</div>', "", doc)

    puestos, saltados = [], []

    def sustituir(m):
        titulo = m.group("tit")
        if any(s in titulo for s in SALTAR):
            return m.group(1)
        pal = clave_de(titulo)
        if "Tarea final" in titulo:
            n = PU.dia(curso, unidad, "Tarea final") or PU.dia(curso, unidad, *pal)
        else:
            n = PU.dia(curso, unidad, *pal)
        if n is None and len(pal) > 1:
            n = PU.dia(curso, unidad, pal[0])
        if n is None:
            saltados.append(titulo)
            return m.group(1)
        dtit = dict(PU.titulos(curso, unidad))[n].strip("«»")
        puestos.append((titulo, n, dtit))
        return (m.group(1) + MARCA_INI +
                '<div class="route-note">📊 <b>En clase:</b> diapositiva %d — «%s».</div>'
                % (n, dtit))

    nuevo = SECCION.sub(sustituir, doc)
    open(ruta, "w", encoding="utf-8").write(nuevo)
    return puestos, saltados


def main():
    tot_p = tot_s = 0
    for curso, unidad, ruta in unidades():
        p, s = procesar(curso, unidad, ruta)
        tot_p += len(p); tot_s += len(s)
        print("%-4s U%d  %2d bruggen, %d secties zonder dia" % (curso, unidad, len(p), len(s)))
        for tit, n, dtit in p:
            print("        %-42s → dia %2d  «%s»" % (tit[:42], n, dtit[:34]))
        for tit in s:
            print("      ! %-42s geen dia gevonden" % tit[:42])
    print("\n%d bruggen gelegd, %d secties overgeslagen" % (tot_p, tot_s))


if __name__ == "__main__":
    main()
