#!/usr/bin/env python3
"""Repareert PowerPoint-bestanden met een dubbele <a:effectLst> in één <p:spPr>.

HET PROBLEEM
PowerPoint vroeg bij het openen van onze decks om te «Repareren». De oorzaak zit
in de generatoren, in deze twee regels vlak na elkaar:

    shp.shadow.inherit = False      # python-pptx zet hiervoor een LEGE <a:effectLst/>
    _soft_shadow(shp)               # en wij hingen er een TWEEDE aan, met de schaduw

Het OOXML-schema (CT_ShapeProperties) laat hoogstens één `effectLst` per `spPr`
toe. Twee stuks maakt het bestand formeel ongeldig; PowerPoint repareert dat
stilzwijgend, maar meldt het eerst — en strikte lezers weigeren het bestand.

DE REPARATIE
Per `spPr` met meer dan één `effectLst`: hou de gevulde (de echte schaduw) en
gooi de lege weg. Staat er alleen een lege, dan blijft die staan — dat is geldig
en betekent «geen schaduw, ook niet geërfd».

Werkt rechtstreeks op het zip-archief en de XML, dus zónder python-pptx: zo is
een deck ook te herstellen op een machine waar de generator niet kan draaien.

    python3 repara_effectlst.py bestand.pptx [meer.pptx …]     # repareert ter plaatse
    python3 repara_effectlst.py --check bestand.pptx           # alleen tellen
    python3 repara_effectlst.py --out map/ bestand.pptx        # kopie in map/
"""
import argparse
import os
import re
import shutil
import sys
import zipfile

# Eén <p:spPr>…</p:spPr>-blok. Niet-gulzig, want er staan er veel na elkaar.
_SPPR = re.compile(r"<p:spPr\b[^>]*>.*?</p:spPr>|<p:spPr\b[^>]*/>", re.S)
# Een lege effectLst, in beide schrijfwijzen.
_VACIO = re.compile(r"<a:effectLst\s*/>|<a:effectLst\s*>\s*</a:effectLst\s*>")
# LET OP de volgorde van de alternatieven: de zelfsluitende variant moet éérst.
# Andersom slikt `<a:effectLst.*?</a:effectLst>` een lege tag én de gevulde tag
# erachter op als één match, en telt de dubbele dus als enkelvoudig.
_TODOS = re.compile(r"<a:effectLst\s*/>|<a:effectLst[^>/]*>.*?</a:effectLst\s*>", re.S)


def _arregla_sppr(bloque):
    """Geeft (nieuw blok, aantal verwijderde lege effectLst) terug."""
    todos = _TODOS.findall(bloque)
    if len(todos) < 2:
        return bloque, 0
    llenos = [e for e in todos if not _VACIO.fullmatch(e)]
    if not llenos:
        # allemaal leeg: hou er één over
        primero = True
        def _uno(m):
            nonlocal primero
            if primero:
                primero = False
                return m.group(0)
            return ""
        nuevo, n = _TODOS.subn(_uno, bloque)
        return nuevo, n - 1 if n else 0
    # er is een echte schaduw: alle lege eruit
    quitados = 0

    def _quita(m):
        nonlocal quitados
        if _VACIO.fullmatch(m.group(0)):
            quitados += 1
            return ""
        return m.group(0)

    return _TODOS.sub(_quita, bloque), quitados


def arregla_xml(texto):
    total = 0
    piezas, fin = [], 0
    for m in _SPPR.finditer(texto):
        nuevo, n = _arregla_sppr(m.group(0))
        if n:
            piezas.append(texto[fin:m.start()]); piezas.append(nuevo)
            fin = m.end(); total += n
    if not total:
        return texto, 0
    piezas.append(texto[fin:])
    return "".join(piezas), total


def revisa(ruta):
    """Telt de spPr-blokken met meer dan één effectLst, zonder iets te wijzigen."""
    malos = {}
    with zipfile.ZipFile(ruta) as z:
        for n in z.namelist():
            if not (n.startswith("ppt/") and n.endswith(".xml")):
                continue
            t = z.read(n).decode("utf8", "ignore")
            c = sum(1 for m in _SPPR.finditer(t) if len(_TODOS.findall(m.group(0))) > 1)
            if c:
                malos[n] = c
    return malos


def repara(ruta, destino=None):
    malos = revisa(ruta)
    if not malos:
        print("  %s — niets te repareren" % os.path.basename(ruta))
        return 0
    salida = destino or ruta
    tmp = salida + ".tmp"
    total = 0
    with zipfile.ZipFile(ruta) as z_in, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z_out:
        for item in z_in.infolist():
            datos = z_in.read(item.filename)
            if item.filename in malos:
                texto, n = arregla_xml(datos.decode("utf8"))
                datos = texto.encode("utf8"); total += n
            # bewaar de oorspronkelijke zip-metadata: PowerPoint is er niet kieskeurig
            # over, maar zo blijft het verschil met het origineel zo klein mogelijk
            z_out.writestr(item, datos)
    shutil.move(tmp, salida)
    print("  %s — %d lege effectLst verwijderd, over %d onderdelen"
          % (os.path.basename(salida), total, len(malos)))
    return total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("archivos", nargs="+")
    ap.add_argument("--check", action="store_true", help="alleen tellen, niets wijzigen")
    ap.add_argument("--out", help="map voor de gerepareerde kopie")
    a = ap.parse_args()
    if a.out:
        os.makedirs(a.out, exist_ok=True)
    fouten = 0
    for f in a.archivos:
        if a.check:
            malos = revisa(f)
            n = sum(malos.values())
            print("  %-42s %s" % (os.path.basename(f),
                                  ("%d dubbele effectLst in %d onderdelen" % (n, len(malos)))
                                  if malos else "schoon"))
            fouten += bool(malos)
        else:
            repara(f, os.path.join(a.out, os.path.basename(f)) if a.out else None)
    sys.exit(1 if (a.check and fouten) else 0)


if __name__ == "__main__":
    main()
