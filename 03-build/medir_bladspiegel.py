#!/usr/bin/env python3
"""Meet hoe vol elke bladzijde van de gebouwde PDF's staat.

WAAROM
De bladspiegel-regel («geen halflege pagina's», CLAUDE.md §13) was tot nu een
oordeel, geen meting. Dit script maakt er een getal van: per bladzijde de
laagste inkt, dus hoe ver de inhoud doorloopt. Zo is te zien of een wijziging
aan het breukgedrag echt helpt, en welke units nog halflege bladzijden hebben.

    python3 03-build/medir_bladspiegel.py            # samenvatting per unit
    python3 03-build/medir_bladspiegel.py C5_U0      # bladzijde per bladzijde

Er is in deze sandbox geen pdftoppm of Pillow, dus het meet niet op pixels maar
op de tekenopdrachten zelf: de PDF-contentstroom wordt uitgepakt en van elke
tekstregel en elk vlak wordt de y-coördinaat genomen. De laagste is de onderkant
van de inhoud. Dat is nauwkeurig genoeg om halflege bladzijden te vinden.

Het bladzijdenummer telt niet mee: dat staat in de ondermarge en zou elk blad
100 % vol maken. Het valt vanzelf buiten de meting omdat het met `Td` getekend
wordt en hier alleen `Tm` en vlakken worden gevolgd — als dat ooit verandert,
moet de stroom van `paginar.py` expliciet overgeslagen worden.
"""
import glob
import os
import re
import sys
import zlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "03-build", "pdf")

ALTO = 842.0            # A4 in punten
MARGEN = 34.0           # @page margin 12mm boven + onder, in punten
VACIA = 0.55            # onder deze vulling noemen we een bladzijde halfleeg


def _objetos(datos):
    """{objectnummer: (woordenboek, ruwe stroom of None)}"""
    out = {}
    for m in re.finditer(rb"(?m)^(\d+) 0 obj\b", datos):
        num = int(m.group(1))
        fin = datos.find(b"endobj", m.end())
        cuerpo = datos[m.end():fin if fin > 0 else len(datos)]
        s = cuerpo.find(b"stream")
        if s < 0:
            out[num] = (cuerpo, None)
            continue
        ini = cuerpo.find(b"\n", s) + 1
        e = cuerpo.find(b"endstream", ini)
        out[num] = (cuerpo[:s], cuerpo[ini:e])
    return out


_NUM = r"[-+]?[\d.]+"
_OP = re.compile(
    (r"(?P<cm>%s %s %s %s %s %s) cm|"
     r"(?P<re>%s %s %s %s) re|"
     r"(?P<tm>%s %s %s %s %s %s) Tm|"
     r"(?P<q>\bq\b)|(?P<Q>\bQ\b)") % ((_NUM,) * 16))


def _mult(m, n):
    """m × n, allebei [a b c d e f] — de affiene matrix van PDF."""
    a, b, c, d, e, f = m
    A, B, C, D, E, F = n
    return (a * A + b * C, a * B + b * D,
            c * A + d * C, c * B + d * D,
            e * A + f * C + E, e * B + f * D + F)


def _tinta(cru):
    """Alle y-coördinaten van inkt, in gebruikersruimte van de bladzijde.

    Chromium tekent niet in paginacoördinaten maar in een geschaalde,
    omgeklapte ruimte (`.24 0 0 -.24 0 841.92 cm`, met daarbinnen nog eens
    `3.125 0 0 3.125 0 -29028 cm`). Zonder die matrices mee te rekenen meet je
    onzin — de eerste versie van dit script mat 15 % vulling op volle pagina's.
    Daarom een kleine interpretatie van q/Q/cm.
    """
    ctm = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)
    pila = []
    ys = []
    texto = cru.decode("latin1")
    for m in _OP.finditer(texto):
        if m.group("q"):
            pila.append(ctm)
        elif m.group("Q"):
            if pila:
                ctm = pila.pop()
        elif m.group("cm"):
            ctm = _mult(tuple(float(v) for v in m.group("cm").split()), ctm)
        elif m.group("tm"):
            tm = tuple(float(v) for v in m.group("tm").split())
            ys.append(_mult(tm, ctm)[5])
        else:
            x, y, w, h = (float(v) for v in m.group("re").split())
            esq = [_mult((1, 0, 0, 1, x + dx, y + dy), ctm)[5]
                   for dx, dy in ((0, 0), (0, h), (w, 0), (w, h))]
            if max(esq) - min(esq) > 0.9 * ALTO:    # paginabrede ondergrond
                continue
            ys += esq
    return [y for y in ys if 0 <= y <= ALTO]


def paginas(ruta):
    """[(vulling 0–1, laagste y)] per bladzijde, in presentatievolgorde.

    De onderkant van de inhoud is de laagste y van een tekstregel of van een
    gekleurd vlak. Vlakken die (bijna) de hele bladzijde beslaan tellen niet
    mee: dat is de witte ondergrond die Chromium op élke bladzijde tekent, en
    die zou elke bladzijde 100 % vol maken.
    """
    datos = open(ruta, "rb").read()
    objs = _objetos(datos)
    util = ALTO - 2 * MARGEN
    salida = []
    for num in sorted(objs):
        dic, cru = objs[num]
        if b"/Type /Page" not in dic and b"/Type/Page" not in dic:
            continue
        # /Contents is één verwijzing óf een rij ervan (na paginar.py)
        m = re.search(rb"/Contents\s*(?:\[([^\]]*)\]|(\d+) 0 R)", dic)
        if not m:
            continue
        refs = ([int(x) for x in re.findall(rb"(\d+) 0 R", m.group(1))]
                if m.group(1) else [int(m.group(2))])
        refs = [x for x in refs if x in objs]
        if not refs:
            continue
        # álle stromen samen: sinds paginar.py staat de bladzijde-inhoud tussen
        # een `q`- en een `Q`-stroom, met het paginanummer erachter. Alleen de
        # eerste lezen levert een leeg blad op.
        piezas = []
        for ref in refs:
            cdic, cru = objs[ref]
            if cru is None:
                continue
            if b"/FlateDecode" in cdic:
                try:
                    cru = zlib.decompress(cru)
                except zlib.error:
                    continue
            piezas.append(cru)
        if not piezas:
            continue
        ys = _tinta(b"\n".join(piezas))
        bajo = min(ys) if ys else ALTO - MARGEN
        salida.append((max(0.0, min(1.0, (ALTO - MARGEN - bajo) / util)), bajo))
    return salida


def informe(ruta):
    """(aantal bladzijden, gemiddelde vulling, de halflege)

    De láátste bladzijde van een unit telt niet mee als halfleeg. Een unit moet
    ergens ophouden, en dat is bijna nooit precies onderaan een blad; die ene
    bladzijde meerekenen zou elke unit een fout geven die niet te herstellen is.
    Het gemiddelde blijft wél over álle bladzijden gaan — anders zou het een
    mooier getal tonen dan er op papier staat.
    """
    p = paginas(ruta)
    if not p:
        return None
    llenos = [x[0] for x in p]
    medio = sum(llenos) / len(llenos)
    flacas = [i + 1 for i, f in enumerate(llenos[:-1]) if f < VACIA]
    return len(p), medio, flacas


def main():
    if len(sys.argv) > 1:
        nombre = sys.argv[1]
        # C4 zet zijn PDF's naast de print-HTML, C5 en C6+ in 03-build/pdf
        ruta = os.path.join(PDF, nombre + ".pdf")
        if not os.path.exists(ruta):
            ruta = os.path.join(os.path.dirname(PDF), "web", "print", nombre + ".pdf")
        for i, (f, y) in enumerate(paginas(ruta), 1):
            barra = "█" * int(f * 40)
            print("  p%-3d %5.0f %%  %s" % (i, f * 100, barra))
        return

    tot_p = tot_f = 0
    tot_llen = 0.0
    print("unit            blz    vulling   halflege bladzijden")
    # C4 zet zijn PDF's naast de print-HTML, C5 en C6+ in 03-build/pdf.
    c4 = os.path.join(os.path.dirname(PDF), "web", "print")
    rutas = (sorted(glob.glob(os.path.join(c4, "C4_U*.pdf")),
                    key=lambda p: int(re.search(r"U(\d+)", p).group(1)))
             + sorted(glob.glob(os.path.join(PDF, "*.pdf"))))
    for ruta in rutas:
        nombre = os.path.basename(ruta)[:-4]
        r = informe(ruta)
        if not r:
            continue
        n, medio, flacas = r
        tot_p += n; tot_f += len(flacas); tot_llen += medio * n
        print("%-14s %3d    %5.0f %%   %s"
              % (nombre, n, medio * 100,
                 (("%d  " % len(flacas)) + ", ".join(str(x) for x in flacas[:12])
                  + (" …" if len(flacas) > 12 else "")) if flacas else "—"))
    print("\n%d bladzijden, gemiddeld %.0f %% gevuld, %d halfleeg (%.0f %%)"
          % (tot_p, 100 * tot_llen / tot_p, tot_f, 100.0 * tot_f / tot_p))


if __name__ == "__main__":
    main()
