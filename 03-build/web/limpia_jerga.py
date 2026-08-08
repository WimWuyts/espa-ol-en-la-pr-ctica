#!/usr/bin/env python3
"""Haalt de bouwtaal van de leerlingpagina en houdt de bewerkbare kopie gelijk.

WAAROM
CLAUDE.md §13/§18 zijn duidelijk: geen componentnamen, geen didactisch model en
geen meta op de bladzijde die de leerling voor zich krijgt. In de praktijk lekte
het er langs drie kanten in:

  · de steunladder uit §14 — «Apoyo: PISTA (media/cuarto)». PISTA is een niveau
    uit het model; voor de leerling betekenisloos. De hulp tussen haakjes is wél
    bruikbaar, dus die blijft, met een gewone naam ervoor.
  · «Afzender · ontvanger · doel · situatie · resultaat» — de checklist waarmee
    een communicatieve taak wordt ontworpen, niet de opdracht zelf.
  · woorden als «receptief», «productief», «spreiding», «keten».

De generatoren zijn hierop rechtgezet, maar C5 U0 is met de hand gebouwd en
heeft geen generator. En de bewerkbare `_BEWERKBAAR.html`-kopieën van C6+ waren
losse bestanden die niet meegroeiden. Dit script sluit beide gaten na de bouw,
zodat één blik volstaat om te zien dat het weg is.

Herhaalbaar; draait ná de printgeneratoren.
"""
import os
import re
import shutil
import sys

ROOT = "/home/user/espa-ol-en-la-pr-ctica"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import enlaces as EN          # noqa: E402


ETIQUETA = {"MODELO": "Modelo", "BANCO": "Banco de palabras", "MARCO": "Marco",
            "PISTA": "Pista", "LETRA": "Primera letra",
            "LETRA INICIAL": "Primera letra", "CUE": "Pista"}
_N = "MODELO|BANCO|MARCO|PISTA|LETRA INICIAL|LETRA|CUE|SIN AYUDA"

NIVEL = re.compile(
    r"Apoyo:\s*(%s)(?:\s*→\s*(?:%s))*\s*(?:\(([^)]*)\))?" % (_N, _N))


def _nivel(m):
    nivel, dentro = m.group(1), (m.group(2) or "").strip()
    if nivel == "SIN AYUDA":
        return dentro
    return ("%s: %s" % (ETIQUETA[nivel], dentro)) if dentro else ETIQUETA[nivel]


SUSTITUCIONES = [
    (re.compile(r"<b>Afzender\s*[·/]\s*ontvanger\s*[·/]\s*doel\s*[·/]\s*"
                r"situatie\s*[·/]\s*resultaat:</b>\s*"), "<b>Situación:</b> "),
    (re.compile(r"Afzender\s*[·/]\s*ontvanger\s*[·/]\s*doel\s*[·/]\s*"
                r"situatie\s*[·/]\s*resultaat:\s*"), "Situación: "),
    (re.compile(r"Keten\s+(?:lezen|luisteren|schrijven|spreken)"
                r"(?:\s*→\s*\w+)+\.\s*"), ""),
    (re.compile(r"\(receptief\s*(?:&amp;|&)\s*productief\)"),
     "(begrijpen en zelf gebruiken)"),
    (re.compile(r"van receptief naar productief"),
     "eerst herkennen, daarna zelf zeggen"),
    (re.compile(r"\s+en spreiding\b"), ""),
    (re.compile(r"\s*→\s*SIN AYUDA"), ""),
    # C5 U0 schreef de steun in proza («Apoyo: banco de palabras → sin ayuda»).
    # De beschrijving zelf is bruikbaar — ze zegt de leerling dat ronde twee
    # zonder bank gaat — maar het woord «Apoyo» is de naam van het ontwerp, niet
    # van de hulp. Hoofdletter erop, prefix eraf.
    (re.compile(r"Apoyo:\s*(\w)"), lambda m: m.group(1).upper()),
    (re.compile(r"\s*·\s*(?:receptief|productief)\b"), ""),
    # een steunregel die na het opschonen leeg is, hoort er niet meer te staan
    (re.compile(r'<div class="steun"[^>]*>\s*</div>'), ""),
    (re.compile(r'<span class="steun">\s*</span>'), ""),
]


def unidades():
    """(curso, unidad, print-HTML, bewerkbare kopie|None).

    De lijst zelf staat in enlaces.py. De bewerkbare kopie hoort daar niet bij:
    die bestaat alleen in C6+, waar hij naast de PDF geleverd wordt (§10, de
    leveringsregel). Waar hij niet bestaat, is er niets te kopiëren.
    """
    for curso, u, impreso, _hub in EN.unidades():
        copia = None
        if curso == "C6+":
            copia = os.path.join(os.path.dirname(impreso),
                                 "C6plus_U%d_BEWERKBAAR.html" % u)
        yield (curso, u, impreso, copia)


def main():
    tot = 0
    for curso, u, ruta, copia in unidades():
        doc = open(ruta, encoding="utf-8").read()
        nuevo, n = NIVEL.subn(_nivel, doc)
        for pat, rep in SUSTITUCIONES:
            nuevo, k = pat.subn(rep, nuevo)
            n += k
        if nuevo != doc:
            open(ruta, "w", encoding="utf-8").write(nuevo)
        tot += n
        # de bewerkbare kopie is precies de printbladzijde, nooit een oudere versie
        aviso = ""
        if copia:
            shutil.copyfile(ruta, copia)
            aviso = " · bewerkbare kopie bijgewerkt"
        if n or aviso:
            print("%-4s U%d  %3d stukken bouwtaal weg%s" % (curso, u, n, aviso))
    print("\n%d stukken bouwtaal van de leerlingpagina's gehaald" % tot)


if __name__ == "__main__":
    main()
