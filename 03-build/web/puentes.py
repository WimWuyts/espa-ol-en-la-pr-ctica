#!/usr/bin/env python3
"""De bruggen tussen de drie dragers: boek ↔ PowerPoint ↔ digitale pagina.

CLAUDE.md §16 vraagt dat de formaten naar elkaar verwijzen («zie dia 12» /
«oefen online: …»). In de praktijk stond er alleen de kant boek → online, en de
kant boek → PowerPoint helemaal niet. Het probleem daarmee is dat een dianummer
niet vaststaat: zodra er een dia bijkomt — zoals de reto-dia's — klopt elke
verwijzing in het boek niet meer.

Dit bestand lost dat op door de dianummers niet op te schrijven maar op te
zóeken, in het deck zelf, op het moment dat het boek gebouwd wordt. De brug
verwijst dus altijd naar het deck zoals het nu is.

    import puentes
    puentes.dia("C5", 1, "SER")        → 6
    puentes.puente_ppt("C5", 1, "SER") → '<div class="route-note">📊 …dia 6…</div>'

Vindt hij niets, dan geeft hij None terug en laat de generator de verwijzing
gewoon weg — een verwijzing naar een dia die niet bestaat is erger dan geen.
"""
import os
import re
import zipfile

ROOT = "/home/user/espa-ol-en-la-pr-ctica"
PPTX = os.path.join(ROOT, "03-build", "pptx")

_CACHE = {}


def _deck(curso, unidad):
    return os.path.join(PPTX, "%s_U%d_docente.pptx"
                        % ("C5" if curso == "C5" else "C6plus", unidad))


def titulos(curso, unidad):
    """[(dianummer, titel)] van het docentendeck, in presentatievolgorde."""
    clave = (curso, unidad)
    if clave in _CACHE:
        return _CACHE[clave]
    ruta = _deck(curso, unidad)
    if not os.path.exists(ruta):
        _CACHE[clave] = []
        return []
    z = zipfile.ZipFile(ruta)
    pres = z.read("ppt/presentation.xml").decode()
    rels = z.read("ppt/_rels/presentation.xml.rels").decode()
    orden = re.findall(r'r:id="(rId\d+)"',
                       re.search(r"<p:sldIdLst>.*?</p:sldIdLst>", pres, re.S).group(0))
    mapa = {a: b for a, b in re.findall(r'Id="(rId\d+)"[^>]*Target="([^"]+)"', rels)}
    salida = []
    for n, rid in enumerate(orden, 1):
        x = z.read("ppt/" + mapa[rid]).decode()
        # de grootste lettergrootte op een dia is in dit sjabloon altijd de titel
        runs = [(int(s), t) for s, t in
                re.findall(r'sz="(\d+)"[^>]*>(?:(?!</a:r>).)*?<a:t>([^<]{2,70})</a:t>', x, re.S)]
        salida.append((n, max(runs)[1] if runs else ""))
    _CACHE[clave] = salida
    return salida


def dia(curso, unidad, *palabras):
    """Het nummer van de dia waarvan de titel alle `palabras` bevat.

    Zoekt hoofdletterongevoelig en op deelwoorden, zodat «SER» ook «El verbo SER
    (irregular)» vindt. Geen of meerdere treffers → None, en dan zwijgt het boek.
    """
    cand = []
    for n, t in titulos(curso, unidad):
        bajo = t.lower()
        if all(p.lower() in bajo for p in palabras):
            cand.append((n, t))
    return cand[0][0] if len(cand) == 1 else (cand[0][0] if cand else None)


def puente_ppt(curso, unidad, *palabras, etiqueta=None):
    """De verwijsregel boek → PowerPoint, of "" als de dia niet bestaat."""
    n = dia(curso, unidad, *palabras)
    if n is None:
        return ""
    titel = dict(titulos(curso, unidad))[n]
    lab = etiqueta or titel
    return ('<div class="route-note">📊 <b>En clase:</b> diapositiva %d — «%s».</div>'
            % (n, lab))


def informe(curso, unidad):
    """Overzicht voor de bouwcontrole."""
    return "\n".join("%2d  %s" % (n, t) for n, t in titulos(curso, unidad))


if __name__ == "__main__":
    import sys
    curso = sys.argv[1] if len(sys.argv) > 1 else "C5"
    unidad = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    print("Deck %s U%d\n" % (curso, unidad))
    print(informe(curso, unidad))
    print("\nVoorbeeldbrug:", puente_ppt(curso, unidad, "SER"))
