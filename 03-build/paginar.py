#!/usr/bin/env python3
"""Zet bladzijdenummers en bladwijzers in de gebouwde PDF's.

WAAROM
Een werkboek van veertig bladzijden zonder nummers is in de klas onbruikbaar:
«ga naar bladzijde 23» kan niet, een oefening terugvinden kan niet, en een
verwijzing binnen de cursus evenmin. Het ontbrak, en het is niet met CSS op te
lossen: Chromium kent de `@page`-margeblokken (`@bottom-center{content:
counter(page)}`) niet, en de enige polyfill die dat wél doet (Paged.js) is een
JavaScript-opmaakmotor die hier niet te installeren valt én op documenten van
veertig bladzijden met ingebedde fonts traag en onbetrouwbaar wordt.

Dus doen we het achteraf, in de PDF zelf. Die is dankbaar eenvoudig: Chromium
schrijft PDF 1.4 met een klassieke xref-tabel en ongecomprimeerde objecten. Per
bladzijde komt er één tekenopdracht bij — een tekstregel in Helvetica — en het
bestand wordt met een verse xref-tabel weggeschreven. De bestaande inhoud wordt
byte voor byte overgenomen; er wordt niets hertekend.

De openingsbladzijde krijgt geen nummer (dat is de hero-pagina), de telling
begint dus zichtbaar bij 2.

BLADWIJZERS
Een boek van veertig bladzijden dat op een scherm opengaat zonder inhoudsopgave
in de zijbalk, is even lastig als een boek zonder nummers. De bladwijzers komen
uit de PDF zelf: `bladspiegel.py` geeft elke sectie een anker en zet achteraan
een verborgen lijst die ernaar linkt. Chromium schrijft daarvan een
`/Dests`-tabel — naam → bladzijde — en dat is de enige betrouwbare manier om ná
de opmaak te weten waar een sectie begint. De tekst zelf uitlezen kan niet: die
staat in de PDF als glyfnummers van een ingebed font, niet als letters.

    python3 03-build/paginar.py                 # alle PDF's in 03-build/pdf
    python3 03-build/paginar.py C5_U3           # één bestand
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "03-build", "pdf")

ANCHO, ALTO = 595.276, 841.89          # A4 in punten
BASE = 20.0                            # hoogte van het nummer boven de onderrand
CUERPO = 8.5
GRIS = "0.45 0.46 0.50"

MARCA = b"% paginado por paginar.py"


def objetos(datos):
    """{nummer: (begin, eind)} — de byte-grenzen van elk object, verbatim."""
    out = {}
    for m in re.finditer(rb"(?m)^(\d+) 0 obj\b", datos):
        num = int(m.group(1))
        fin = datos.find(b"endobj", m.end())
        out[num] = (m.start(), fin + 6)
    return out


def orden_paginas(datos, objs):
    """De objectnummers van de bladzijden, in leesvolgorde.

    De paginaboom is genest: een wortel-/Pages met /Pages-knopen eronder, en pas
    daaronder de bladzijden. Plat achter elkaar plakken telt de tussenknopen mee
    (43 bladzijden werden er zo 49). Dus: van de wortel af, recursief.
    """
    cuerpo = {n: datos[a:b] for n, (a, b) in objs.items()}

    def es_nodo(n):
        return b"/Type /Pages" in cuerpo.get(n, b"") or b"/Type/Pages" in cuerpo.get(n, b"")

    hijos = {}
    for n in cuerpo:
        if not es_nodo(n):
            continue
        m = re.search(rb"/Kids\s*\[(.*?)\]", cuerpo[n], re.S)
        hijos[n] = [int(x) for x in re.findall(rb"(\d+) 0 R", m.group(1))] if m else []

    if hijos:
        de_alguien = {k for v in hijos.values() for k in v}
        raices = [n for n in hijos if n not in de_alguien] or [max(hijos)]
        salida, pila = [], list(raices)
        visto = set()
        while pila:
            n = pila.pop(0)
            if n in visto:
                continue
            visto.add(n)
            if es_nodo(n):
                pila = hijos.get(n, []) + pila
            elif n in cuerpo:
                salida.append(n)
        if salida:
            return salida

    return [n for n in sorted(cuerpo)
            if b"/Type /Page" in cuerpo[n] and not es_nodo(n)]


def _con_fuente(cuerpo, ref):
    """Zet /PGF in de /Font van de bladzijde — of maakt die aan."""
    m = re.search(rb"/Font\s*<<", cuerpo)
    if m:
        return cuerpo[:m.end()] + b"/PGF %d 0 R " % ref + cuerpo[m.end():]
    m = re.search(rb"/Resources\s*<<", cuerpo)
    if not m:
        return None
    return cuerpo[:m.end()] + b"/Font <</PGF %d 0 R>> " % ref + cuerpo[m.end():]


def _con_contenido(cuerpo, abre, cierra, nuevo):
    """Zet de bladzijde-inhoud tussen haakjes en hangt het nummer erachter.

    Dit is het addertje: Chromium begint zijn contentstroom met een óngepaarde
    `.24 0 0 -.24 0 841.92 cm` — een geschaalde, omgeklapte ruimte. Streams in
    een /Contents-rij worden aan elkaar geplakt alsof het er één is, dus die
    matrix zou ook voor het paginanummer gelden: op 24 % van zijn grootte, aan
    de verkeerde kant van het blad. Daarom komt de oorspronkelijke stroom tussen
    een `q` en een `Q` te staan; het nummer tekent daarna in de normale
    paginaruimte. De twee haakjes zijn gedeelde objecten, één keer in het
    bestand voor alle bladzijden samen.
    """
    m = re.search(rb"/Contents\s*(\d+) 0 R", cuerpo)
    if m:
        return (cuerpo[:m.start()]
                + b"/Contents [%d 0 R %s 0 R %d 0 R %d 0 R]"
                % (abre, m.group(1), cierra, nuevo)
                + cuerpo[m.end():])
    m = re.search(rb"/Contents\s*\[(.*?)\]", cuerpo, re.S)
    if m:
        return (cuerpo[:m.start()]
                + b"/Contents [%d 0 R %s %d 0 R %d 0 R]"
                % (abre, m.group(1).strip(), cierra, nuevo)
                + cuerpo[m.end():])
    return None


def _flujo_crudo(cru):
    return b"<</Length %d>>\nstream\n%s\nendstream" % (len(cru), cru)


def flujo(texto, x):
    """De tekenopdracht voor één nummer, netjes in een eigen q/Q."""
    cru = ("q BT /PGF %.1f Tf %s rg %.1f %.1f Td (%s) Tj ET Q"
           % (CUERPO, GRIS, x, BASE, texto)).encode("latin1")
    return b"<</Length %d>>\nstream\n%s\nendstream" % (len(cru), cru)


def _destinos(datos, objs):
    """{ankernaam: objectnummer van de bladzijde} uit de /Dests-tabel."""
    m = re.search(rb"/Dests\s+(\d+) 0 R", datos)
    if not m:
        return {}
    num = int(m.group(1))
    if num not in objs:
        return {}
    a, b = objs[num]
    cuerpo = datos[a:b]
    return {n.decode("latin1"): int(p)
            for n, p in re.findall(rb"/([A-Za-z0-9_.-]+)\s*\[\s*(\d+) 0 R", cuerpo)}


def _titulos(ruta_pdf):
    """De sectietitels, uit de HTML waaruit deze PDF gebouwd is.

    De volgorde in `bladspiegel.py` is dezelfde als hier: sec-1, sec-2, … Dus de
    titel bij een anker is gewoon op te zoeken in de bron.
    """
    nombre = os.path.basename(ruta_pdf)[:-4]
    curso, u = nombre.split("_U")
    if curso == "C5":
        html = os.path.join(ROOT, "01-cursussen", "05-a1", "U%s" % u, "U%s.html" % u)
    else:
        d = os.path.join(ROOT, "01-cursussen", "06-vervolg", "U%s" % u)
        html = os.path.join(d, "C6plus_U%s.html" % u)
        if not os.path.exists(html):
            html = os.path.join(d, "U%s.html" % u)
    if not os.path.exists(html):
        return {}
    doc = open(html, encoding="utf-8").read()
    m = re.search(r'<nav class="indice-pdf".*?</nav>', doc, re.S)
    if not m:
        return {}
    return {a: re.sub(r"\s+", " ", t).strip()
            for a, t in re.findall(r'href="#([^"]+)">([^<]*)</a>', m.group(0))}


def _texto_pdf(s):
    """Een titel als PDF-tekenreeks, in UTF-16.

    Als gewone `(tekst)` moet PDFDocEncoding volstaan, en dat kan het gedachte-
    streepje niet: «§1 · La hora — ¿Qué hora es?» werd «La hora ? ¿Qué hora es?».
    Een hexadecimale tekenreeks met de UTF-16-markering ervoor kan élk teken, en
    hoeft bovendien niets te ontsnappen.
    """
    return b"<FEFF" + s.encode("utf-16-be").hex().upper().encode("ascii") + b">"


def paginar(ruta):
    datos = open(ruta, "rb").read()
    if MARCA in datos:
        return None                    # al genummerd; herhaalbaar zonder schade
    objs = objetos(datos)
    if not objs:
        return None
    paginas = orden_paginas(datos, objs)
    siguiente = max(objs) + 1

    fuente_num = siguiente
    abre_num = siguiente + 1
    cierra_num = siguiente + 2
    siguiente += 3
    nuevos = {fuente_num: b"<</Type /Font /Subtype /Type1 /BaseFont /Helvetica "
                          b"/Encoding /WinAnsiEncoding>>",
              abre_num: _flujo_crudo(b"q"),
              cierra_num: _flujo_crudo(b"Q")}

    cuerpos = {n: datos[a:b] for n, (a, b) in objs.items()}
    hechas = 0
    for i, num in enumerate(paginas, 1):
        if i == 1 or num not in cuerpos:
            continue                   # de openingsbladzijde blijft schoon
        cuerpo = cuerpos[num]
        # het object zonder zijn omhulsel, zodat we het straks opnieuw kunnen zetten
        interior = re.sub(rb"^\d+ 0 obj\s*", b"", cuerpo)
        interior = re.sub(rb"\s*endobj$", b"", interior)
        con_f = _con_fuente(interior, fuente_num)
        if con_f is None:
            continue
        flujo_num = siguiente
        siguiente += 1
        con_c = _con_contenido(con_f, abre_num, cierra_num, flujo_num)
        if con_c is None:
            continue
        etiqueta = str(i)
        x = ANCHO / 2 - len(etiqueta) * CUERPO * 0.28
        nuevos[flujo_num] = flujo(etiqueta, x)
        cuerpos[num] = b"%d 0 obj\n%s\nendobj" % (num, con_c)
        hechas += 1

    # ── bladwijzers ──────────────────────────────────────────────────────────
    # /Dests zegt bij welk paginaobject een anker hoort; `paginas` zegt de
    # hoeveelste bladzijde dat is. Samen leveren ze de zijbalk.
    dests = _destinos(datos, objs)
    titulos = _titulos(ruta)
    pagina_de = {num: i for i, num in enumerate(paginas, 1)}
    marcas = []
    for ancla, obj_pag in sorted(dests.items(),
                                 key=lambda kv: pagina_de.get(kv[1], 10 ** 6)):
        if not ancla.startswith("sec-") or obj_pag not in pagina_de:
            continue
        marcas.append((titulos.get(ancla, ancla), obj_pag))

    if marcas:
        raiz_num = siguiente
        siguiente += 1
        nums = list(range(siguiente, siguiente + len(marcas)))
        siguiente += len(marcas)
        for i, ((titulo, obj_pag), n) in enumerate(zip(marcas, nums)):
            partes = [b"<</Title %s" % _texto_pdf(titulo),
                      b"/Parent %d 0 R" % raiz_num,
                      b"/Dest [%d 0 R /XYZ null null null]" % obj_pag]
            if i:
                partes.append(b"/Prev %d 0 R" % nums[i - 1])
            if i + 1 < len(nums):
                partes.append(b"/Next %d 0 R" % nums[i + 1])
            nuevos[n] = b"\n".join(partes) + b">>"
        nuevos[raiz_num] = (b"<</Type /Outlines /First %d 0 R /Last %d 0 R /Count %d>>"
                            % (nums[0], nums[-1], len(nums)))

    # opnieuw wegschrijven met een verse xref-tabel: de byte-posities zijn
    # verschoven, dus de oude tabel is per definitie ongeldig geworden
    salida = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n" + MARCA + b"\n")
    posicion = {}
    for num in sorted(set(list(cuerpos) + list(nuevos))):
        posicion[num] = len(salida)
        if num in nuevos and num not in cuerpos:
            salida += b"%d 0 obj\n%s\nendobj\n" % (num, nuevos[num])
        else:
            salida += cuerpos[num].rstrip() + b"\n"

    maximo = max(posicion) + 1
    inicio = len(salida)
    salida += b"xref\n0 %d\n" % maximo
    salida += b"0000000000 65535 f \n"
    for n in range(1, maximo):
        salida += (b"%010d 00000 n \n" % posicion[n]) if n in posicion \
            else b"0000000000 65535 f \n"

    if marcas:
        # de catalogus krijgt /Outlines en /PageMode, zodat de zijbalk meteen
        # openstaat in plaats van dat de lezer hem moet gaan zoeken
        cat = int(re.search(rb"/Root\s+(\d+) 0 R", datos).group(1))
        if cat in cuerpos:
            cuerpos[cat] = re.sub(
                rb"/Type\s*/Catalog",
                b"/Type /Catalog /Outlines %d 0 R /PageMode /UseOutlines" % raiz_num,
                cuerpos[cat], count=1)

    raiz = re.search(rb"/Root\s+(\d+) 0 R", datos)
    info = re.search(rb"/Info\s+(\d+) 0 R", datos)
    salida += b"trailer\n<</Size %d /Root %s 0 R" % (maximo, raiz.group(1))
    if info:
        salida += b" /Info %s 0 R" % info.group(1)
    salida += b">>\nstartxref\n%d\n%%%%EOF\n" % inicio

    open(ruta, "wb").write(bytes(salida))
    return hechas, len(paginas), len(marcas)


def main():
    objetivo = sys.argv[1] if len(sys.argv) > 1 else None
    rutas = sorted(glob.glob(os.path.join(PDF, "*.pdf")))
    if objetivo:
        rutas = [p for p in rutas if objetivo in os.path.basename(p)]
    for ruta in rutas:
        r = paginar(ruta)
        nombre = os.path.basename(ruta)
        if r is None:
            print("%-16s al genummerd" % nombre)
        else:
            print("%-16s %2d van %2d bladzijden genummerd · %2d bladwijzers"
                  % (nombre, r[0], r[1], r[2]))


if __name__ == "__main__":
    main()
