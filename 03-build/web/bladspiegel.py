#!/usr/bin/env python3
"""Zet de bladspiegel van de zeventien printunits recht — na de bouw, in één keer.

WAAROM DIT BESTAAT
De oude regel «elke hoofdsectie start op een nieuwe bladzijde» (CLAUDE.md §14)
botst met de regel «geen halflege pagina's» (§13). Gemeten in de gebouwde units:
58 tot 75 % van alle verspilde bladruimte kwam uit die ene regel, en in C6+ U1
was een op de drie bladzijden halfleeg. Een sectie van vier regels kreeg een
eigen blad; de sectie erna begon weer bovenaan.

De nieuwe regel: **een nieuwe bladzijde is voor de mijlpalen**, niet voor elke
sectie. §0 ¡Ponte al día!, Taller de lengua, Cultura, Tarea final, Repaso en
§V Vocabulario openen een blad; de genummerde inhoudssecties vloeien door en
worden herkenbaar gemaakt door hun bovenmarge en de gekleurde parada-lijn.

Dit script doet twee dingen aan élke gebouwde unit-HTML:

  1. het zet `major` op de secties die wél een blad mogen openen;
  2. het plakt het bladspiegel-blok uit `cursus-print.css` als láátste regels in
     de `<style>`, zodat het de oudere breukregels in de generatoren overstemt.

Als nabewerking en niet in de zeventien generatoren, om dezelfde reden als
`add_puentes.py`: één plek in plaats van zeventien, en C5 U0 heeft geen
generator maar wel dezelfde bladspiegel nodig.

Herhaalbaar: draai het zo vaak je wilt, het resultaat is hetzelfde.

    python3 03-build/web/bladspiegel.py            # alle units, met meting
    python3 03-build/web/bladspiegel.py --medir    # alleen meten, niets wijzigen
"""
import os
import re
import sys

ROOT = "/home/user/espa-ol-en-la-pr-ctica"
KIT = os.path.join(ROOT, "02-huisstijl", "templates", "cursus-print.css")

MARCA = "/* bladspiegel.py — gedeelde kit, laatste woord */"

# Secties die een nieuwe bladzijde openen. Alles wat hier niet in staat, vloeit
# door. Getest op de kopteksten zoals ze in de `pk`-span staan.
#
# §0 ¡Ponte al día! staat er bewust NIET bij: die volgt direct op de opener
# (ruta-strook + inleiding) en die twee vullen samen precies één bladzijde.
# Los van elkaar bleef de openingsbladzijde in vijftien van de zeventien units
# op ongeveer de helft steken.
MOJONES = (
    "Taller de lengua",
    "Cultura",
    "Tarea final",
    "Repaso",
    "Vocabulario",
)


def bloque():
    """Het bladspiegel-blok uit de gedeelde kit — de enige bron van waarheid."""
    css = open(KIT, encoding="utf-8").read()
    m = re.search(r"/\* @bladspiegel:ini.*?@bladspiegel:fin \*/", css, re.S)
    if not m:
        sys.exit("de markeringen @bladspiegel:ini/fin staan niet meer in %s" % KIT)
    return m.group(0)


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


# De zeventien units schrijven hun sectiekop op twee manieren: C5 zet het
# nummer in een <span class="num">, de handgebouwde U0 in een <div>, met
# regeleinden ertussen. Daarom: het openingsdiv, dan alles tot de eerste
# `pk`-span, zolang er geen tweede sectie tussen zit.
SECCION = re.compile(
    r'<div class="(?P<cls>[^"]*\bsec\b[^"]*)"(?P<resto>[^>]*)>'
    r'(?P<medio>(?:(?!<div class="[^"]*\bsec\b).){0,400}?)'
    r'<span class="pk"(?P<pkat>[^>]*)>(?P<tit>[^<]+)</span>', re.S)


def es_mojon(titulo):
    return any(m in titulo for m in MOJONES)


def procesar(ruta):
    doc = open(ruta, encoding="utf-8").read()
    puestos, corridos = [], []

    def sustituir(m):
        cls = m.group("cls").replace(" major", "")
        tit = m.group("tit").strip()
        if es_mojon(tit):
            cls += " major"
            puestos.append(tit)
        else:
            corridos.append(tit)
        return ('<div class="%s"%s>%s<span class="pk"%s>%s</span>'
                % (cls, m.group("resto"), m.group("medio"), m.group("pkat"), m.group("tit")))

    doc = SECCION.sub(sustituir, doc)

    # het blok als laatste in de <style>; een oude versie wordt vervangen
    doc = re.sub(re.escape(MARCA) + r".*?/\* @bladspiegel:fin \*/", "", doc, flags=re.S)
    i = doc.rfind("</style>")
    if i < 0:
        sys.exit("%s heeft geen </style>" % ruta)
    doc = doc[:i] + "\n" + MARCA + "\n" + bloque() + "\n" + doc[i:]

    open(ruta, "w", encoding="utf-8").write(doc)
    return puestos, corridos


def main():
    solo_medir = "--medir" in sys.argv
    tot_p = tot_c = 0
    for curso, u, ruta in unidades():
        if solo_medir:
            doc = open(ruta, encoding="utf-8").read()
            tit = [m.group("tit") for m in SECCION.finditer(doc)]
            p = [t for t in tit if es_mojon(t)]
            c = [t for t in tit if not es_mojon(t)]
        else:
            p, c = procesar(ruta)
        tot_p += len(p); tot_c += len(c)
        print("%-4s U%d  %2d nieuwe bladzijde, %2d doorlopend" % (curso, u, len(p), len(c)))
    print("\n%d secties openen een blad, %d vloeien door" % (tot_p, tot_c))


if __name__ == "__main__":
    main()
