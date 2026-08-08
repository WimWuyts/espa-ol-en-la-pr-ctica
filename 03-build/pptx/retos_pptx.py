#!/usr/bin/env python3
"""Zet de reto-dia's rechtstreeks in een bestaand deck — zonder python-pptx.

WAAROM ZONDER BIBLIOTHEEK
In deze omgeving is python-pptx niet installeerbaar (PyPI geeft 403) en
LibreOffice converteert niets meer, ook geen tekstbestand. De generatoren
`gen_u*_docente.py` kunnen dus niet draaien. Een pptx is echter gewoon een
zip met XML, en dat kan wél: dit bestand schrijft de dia's zelf en doet de
volledige pakketboekhouding (content-types, relaties, `<p:sldIdLst>`).

WAT HET MAAKT
Per reto één dia in de huisstijl: groene kopbalk met chip en titel, het haakje
Spaans-eerst met Nederlandse steun, het okerkader met de beperking, en daaronder
een raster kaarten. Kaarten kunnen een **onthulregel** hebben die pas bij een
klik verschijnt — dezelfde didactiek als de rest van de decks.

De inhoud komt uit `retos_data.py`, dezelfde bron als print en hub.

    python3 retos_pptx.py C5_U0_docente.pptx --curso C5 --unidad 0 --after 6
    python3 retos_pptx.py --todo          # alle vier de decks van U0 en U1

LES UIT DE «REPAREREN»-BUG: precies één <a:effectLst> per <a:spPr>, en de
kinderen van spPr in schemavolgorde (xfrm · prstGeom · fill · ln · effectLst).
"""
import argparse
import os
import re
import shutil
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "03-build", "web"))
import retos_data as RD          # noqa: E402

EMU = 914400
W, H = 12191695, 6858000         # 13,33" × 7,5"

G, GD, GT = "1E9E74", "157355", "E4F4EE"
INK, MUT, PAPER, CREMA = "20242E", "6A6E78", "FCFBF8", "F3EEE4"
AMBER, AMBERBG, RED, WHITE, LINE = "B7860B", "FBF3D6", "DC2626", "FFFFFF", "E4E3DE"
DISP, BODY = "Bricolage Grotesque", "Inter"


def _in(v):
    return int(round(v * EMU))


def esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


# ---------------------------------------------------------------------------
# vormen
# ---------------------------------------------------------------------------

_ESTILO = ('<p:style><a:lnRef idx="1"><a:schemeClr val="accent1"/></a:lnRef>'
           '<a:fillRef idx="3"><a:schemeClr val="accent1"/></a:fillRef>'
           '<a:effectRef idx="2"><a:schemeClr val="accent1"/></a:effectRef>'
           '<a:fontRef idx="minor"><a:schemeClr val="lt1"/></a:fontRef></p:style>')


def forma(sid, nombre, x, y, cx, cy, relleno=None, linea=None, redondo=False, radio=0.06):
    """Rechthoek of afgeronde rechthoek. Eén effectLst, in schemavolgorde."""
    geo = ('<a:prstGeom prst="roundRect"><a:avLst><a:gd name="adj" fmla="val %d"/></a:avLst></a:prstGeom>'
           % int(radio * 100000)) if redondo else '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>'
    fill = ('<a:solidFill><a:srgbClr val="%s"/></a:solidFill>' % relleno) if relleno else "<a:noFill/>"
    ln = ('<a:ln w="12700"><a:solidFill><a:srgbClr val="%s"/></a:solidFill></a:ln>' % linea) \
        if linea else "<a:ln><a:noFill/></a:ln>"
    return ('<p:sp><p:nvSpPr><p:cNvPr id="%d" name="%s"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            '<p:spPr><a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm>'
            '%s%s%s<a:effectLst/></p:spPr>%s'
            '<p:txBody><a:bodyPr rtlCol="0" anchor="ctr"/><a:lstStyle/><a:p/></p:txBody></p:sp>'
            % (sid, esc(nombre), x, y, cx, cy, geo, fill, ln, _ESTILO))


def texto(sid, nombre, x, y, cx, cy, parrafos, align="l", anchor="t"):
    """parrafos = [[(tekst, {size, bold, color, font, italic}), …], …]"""
    ps = []
    for runs in parrafos:
        rs = []
        for t, o in runs:
            pr = ['sz="%d"' % int(o.get("size", 14) * 100)]
            if o.get("bold"):
                pr.append('b="1"')
            if o.get("italic"):
                pr.append('i="1"')
            cuerpo = ('<a:solidFill><a:srgbClr val="%s"/></a:solidFill>' % o.get("color", INK)
                      + '<a:latin typeface="%s"/>' % o.get("font", BODY))
            rs.append('<a:r><a:rPr %s>%s</a:rPr><a:t>%s</a:t></a:r>'
                      % (" ".join(pr), cuerpo, esc(t)))
        ps.append('<a:p><a:pPr algn="%s"/>%s</a:p>' % (align, "".join(rs) or ""))
    return ('<p:sp><p:nvSpPr><p:cNvPr id="%d" name="%s"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>'
            '<p:spPr><a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr>'
            '<p:txBody><a:bodyPr wrap="square" anchor="%s" lIns="45720" rIns="45720" '
            'tIns="27432" bIns="27432"><a:normAutofit/></a:bodyPr><a:lstStyle/>%s</p:txBody></p:sp>'
            % (sid, esc(nombre), x, y, cx, cy, anchor, "".join(ps)))


# ---------------------------------------------------------------------------
# klik-onthullingen
# ---------------------------------------------------------------------------

def timing(spids):
    """Elke vorm verschijnt bij een klik — zelfde <p:timing> als de rest van de decks."""
    if not spids:
        return ""
    nodos, cid = [], 5
    for spid in spids:
        nodos.append(
            '<p:par><p:cTn id="%d" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst>'
            '<p:childTnLst><p:par><p:cTn id="%d" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst>'
            '<p:childTnLst><p:par><p:cTn id="%d" presetID="10" presetClass="entr" presetSubtype="0" '
            'fill="hold" grpId="0" nodeType="clickEffect"><p:stCondLst><p:cond delay="0"/></p:stCondLst>'
            '<p:childTnLst>'
            '<p:set><p:cBhvr><p:cTn id="%d" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/>'
            '</p:stCondLst></p:cTn><p:tgtEl><p:spTgt spid="%d"/></p:tgtEl>'
            '<p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
            '<p:to><p:strVal val="visible"/></p:to></p:set>'
            '<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="%d" dur="500"/>'
            '<p:tgtEl><p:spTgt spid="%d"/></p:tgtEl></p:cBhvr></p:animEffect>'
            '</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>'
            % (cid, cid + 1, cid + 2, cid + 3, spid, cid + 4, spid))
        cid += 5
    return ('<p:timing><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" '
            'nodeType="tmRoot"><p:childTnLst><p:seq concurrent="1" nextAc="seek">'
            '<p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>%s</p:childTnLst></p:cTn>'
            '<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond>'
            '</p:prevCondLst><p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/>'
            '</p:tgtEl></p:cond></p:nextCondLst></p:seq></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>'
            % "".join(nodos))


# ---------------------------------------------------------------------------
# de dia van één reto
# ---------------------------------------------------------------------------

def tarjetas_de(r):
    """Het raster kaarten per reto: (kop, tekst, onthulregel of None)."""
    d, i = r["datos"], r["id"]
    if i == "C5-U0-RETO-02":
        return [("LOTE %d · %d pts" % (n, v), "%s   ·   %s" % (a, b),
                 ("IGUAL" if ig else "DIFERENTE") + " — " + reg.split("·")[0].strip())
                for n, a, b, ig, reg, v in d["lotes"]]
    if i == "C5-U0-RETO-05":
        return [(w, "", "%s — «%s»" % (t, sil)) for w, t, sil in d["palabras"]]
    if i == "C5-U0-RETO-06":
        return ([("Ronda %d" % k, es, None) for k, (es, _nl) in enumerate(r["pasos"], 1)]
                + [(le, nom, donde) for le, nom, donde in d["letras_dificiles"]])
    if i == "C5-U1-RETO-01":
        return ([(q, nl, "· usado ·") for q, nl in d["interrogativos"]]
                + [("★ " + quien, datos, None) for quien, datos in d["estrellas"]])
    if i == "C5-U1-RETO-04":
        return ([("PROHIBIDA", q, None) for q, _w in d["prohibidas"]]
                + [("rodeo", q, waarom) for q, waarom in d["rodeos"]])
    if i == "C5-U3-RETO-02":
        return ([(z, ("misma hora que Gante" if h == 0 else "%d horas menos" % -h), None)
                 for z, h in d["zonas"]]
                + [("marco", m, None) for m in d["marco"]])
    if i == "C5-U3-RETO-08":
        return ([(n, t, None) for n, t in d["roles"]]
                + [("marco", m, None) for m in d["marco"]])
    if i == "C5-U3-RETO-10":
        return ([("Pregunta %d" % k, q, wat) for k, (q, wat) in enumerate(d["preguntas"], 1)]
                + [("marco", m, None) for m in d["marco"]])
    if i == "C5-U4-RETO-01":
        return ([("Escala", " → ".join(d["escala"]), None)]
                + [("tema", t, None) for t in d["temas"]]
                + [("marco", m, None) for m in d["marco"]])
    if i == "C5-U4-RETO-03":
        return ([("Tú llamas", m, None) for m in d["marco_llamada"]]
                + [("El presentador", m, None) for m in d["marco_presentador"]]
                + [("canción", c, None) for c in d["canciones"]])
    if i == "C5-U4-RETO-08":
        return ([("Arranque", a, None) for a in d["arranque"]]
                + [("reacción", x, "usada ✗") for x in d["reacciones"]])
    if i == "C5-U2-RETO-02":
        return ([(n, sub, None) for n, sub in d["semilla"]]
                + [("marco", m, None) for m in d["marco"]]
                + [("¡Escándalo!", e, None) for e in d["escandalo"]])
    if i == "C5-U2-RETO-03":
        return ([(o, por, None) for o, por in d["objetos"]]
                + [("marco", m, None) for m in d["marco"]])
    if i == "C5-U2-RETO-08":
        salida = []
        for k, (escena, pies) in enumerate(d["casos"], 1):
            salida.append(("Foto %d" % k, escena, None))
            for pie, ok, porque in pies:
                salida.append(("" if ok else "", pie, ("✓ " if ok else "✗ ") + porque))
        return salida
    if i == "C5-U5-RETO-04":
        # kaart en formules gebundeld: los per gerecht werden het 21 kaarten en
        # dan houdt een kaart nog maar één tekstregel over
        def _trio(xs, n=3):
            return [" · ".join(xs[k:k + n]) for k in range(0, len(xs), n)]
        return ([("La carta", t, None) for t in _trio(d["carta"])]
                + [("Fórmulas", t, None) for t in _trio(d["formulas"])]
                + [("El camarero", n, "cambia de plato y de fórmula")
                   for n in d["no_hay"]])
    if i == "C5-U5-RETO-07":
        return ([(p, "", "descrito ✓") for p in d["productos"]]
                + [("marco", m, None) for m in d["marco"]])
    if i == "C5-U5-RETO-08":
        return ([("La cuenta", "%s — %d pesos" % (x, c), None) for x, c in d["cuenta"]]
                + [("TOTAL", "%d pesos" % sum(c for _x, c in d["cuenta"]), None)]
                + [(n, t, None) for n, t in d["roles"]]
                + [("marco", m, None) for m in d["marco"]])
    if i == "C5-U6-RETO-01":
        # de bodemprijs is het geheim van de verkoper: pas ná het afdingen
        # onthullen, anders valt er niets meer te onderhandelen
        return ([(p, "pide %d pesos" % pide, "solo al final: ≈ %d pesos" % suelo)
                 for p, pide, suelo in d["productos"]]
                + [("Vendedor/a", m, None) for m in d["marco_vendedor"]]
                + [("Cliente", m, None) for m in d["marco_cliente"]])
    if i == "C5-U6-RETO-02":
        return ([("La tienda dice", n, None) for n in d["negativas"]]
                + [("Tu argumento", a, None) for a in d["argumentos"]]
                + [("salida posible", s, None) for s in d["salidas"]])
    if i == "C5-U6-RETO-08":
        return ([(n, t, None) for n, t in d["tipos"]]
                + [("Vendedor/a", m, None) for m in d["marco_vendedor"]])
    if i == "C5-U1-RETO-09":
        return ([("Tu perfil", m, None) for m in d["marco_perfil"]]
                + [("El algoritmo", m, None) for m in d["marco_algoritmo"]]
                + [(etq, txt, None) for etq, txt in d["ejemplos"]])
    return []


def dia_reto(r):
    """Bouwt de volledige slideN.xml van één reto."""
    sid = 2
    sp, reveals = [], []

    # kopbalk
    sp.append(forma(sid, "Fondo", 0, 0, W, H, relleno=PAPER)); sid += 1
    sp.append(forma(sid, "Cabecera", 0, 0, W, _in(1.18), relleno=G)); sid += 1
    sp.append(forma(sid, "Chip", _in(0.5), _in(0.2), _in(3.3), _in(0.32),
                    relleno=WHITE, redondo=True, radio=0.5)); sid += 1
    sp.append(texto(sid, "ChipTxt", _in(0.5), _in(0.19), _in(3.3), _in(0.34),
                    [[("RETO %d · %s" % (r["num"], r["lente"].split(" ", 1)[1].upper()),
                       {"size": 9.5, "bold": True, "color": GD})]], align="ctr", anchor="ctr")); sid += 1
    sp.append(texto(sid, "Titulo", _in(0.5), _in(0.55), _in(9.2), _in(0.52),
                    [[(r["nombre"], {"size": 27, "bold": True, "color": WHITE, "font": DISP})]])); sid += 1
    sp.append(texto(sid, "Badges", _in(9.9), _in(0.28), _in(2.9), _in(0.7),
                    [[(r["forma"], {"size": 10, "color": GT})],
                     [("%s · %s" % (r["tiempo"], r["dificultad"]), {"size": 10, "color": GT})]],
                    align="r")); sid += 1

    # haakje: Spaans eerst, Nederlands eronder
    sp.append(texto(sid, "Gancho", _in(0.5), _in(1.34), _in(12.33), _in(0.62),
                    [[(r["gancho_es"], {"size": 16, "bold": True, "color": GD, "font": DISP})],
                     [(r["gancho_nl"], {"size": 11, "italic": True, "color": MUT})]])); sid += 1

    # de beperking
    sp.append(forma(sid, "ReglaCaja", _in(0.5), _in(2.02), _in(12.33), _in(0.72),
                    relleno=AMBERBG, redondo=True, radio=0.05)); sid += 1
    sp.append(texto(sid, "ReglaTxt", _in(0.66), _in(2.06), _in(12.0), _in(0.64),
                    [[("LA REGLA DEL RETO", {"size": 8.5, "bold": True, "color": AMBER})],
                     [(r["regla"], {"size": 11, "color": INK})]])); sid += 1

    # het raster kaarten
    tarjetas = tarjetas_de(r)
    cols = 4 if len(tarjetas) > 8 else (3 if len(tarjetas) > 4 else 2)
    ancho = (12.33 - 0.16 * (cols - 1)) / cols
    filas = (len(tarjetas) + cols - 1) // cols
    alto = min(1.28, (4.35 - 0.14 * (filas - 1)) / max(filas, 1))
    for k, (kop, txt, onthul) in enumerate(tarjetas):
        col, fila = k % cols, k // cols
        x = _in(0.5 + (ancho + 0.16) * col)
        y = _in(2.92 + (alto + 0.14) * fila)
        sp.append(forma(sid, "Tarjeta %d" % k, x, y, _in(ancho), _in(alto),
                        relleno=WHITE, linea=LINE, redondo=True)); sid += 1
        parr = [[(kop, {"size": 11, "bold": True, "color": GD, "font": DISP})]]
        if txt:
            parr.append([(txt, {"size": 10, "color": INK})])
        sp.append(texto(sid, "TarjetaTxt %d" % k, x + _in(0.1), y + _in(0.06),
                        _in(ancho - 0.2), _in(alto - (0.34 if onthul else 0.12)), parr)); sid += 1
        if onthul:
            # de pil is één regel hoog: langere tekst liep eruit (gezien in de
            # beeldcontrole van slide24, lot 3). De volledige regel staat in de
            # spreker-notities, dus hier mag hij afgekapt.
            limite = 46 if cols <= 3 else 34
            if len(onthul) > limite:
                onthul = onthul[:limite - 1].rstrip(" ·—-") + "…"
            yb = y + _in(alto - 0.32)
            sp.append(forma(sid, "Onthul %d" % k, x + _in(0.1), yb, _in(ancho - 0.2), _in(0.26),
                            relleno=GT, redondo=True, radio=0.2))
            reveals.append(sid); sid += 1
            sp.append(texto(sid, "OnthulTxt %d" % k, x + _in(0.12), yb, _in(ancho - 0.24), _in(0.26),
                            [[(onthul, {"size": 8.5, "bold": True, "color": GD})]], anchor="ctr"))
            reveals.append(sid); sid += 1

    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
            'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
            '<p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/>'
            '</p:nvGrpSpPr><p:grpSpPr/>%s</p:spTree></p:cSld>'
            '<p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>%s</p:sld>'
            % ("".join(sp), timing(reveals)))


def notas(r):
    """De antwoordsleutel hoort in de spreker-notities, niet op de dia."""
    lineas = ["RETO %d · %s — %s" % (r["num"], r["nombre"], r["lente"])]
    lineas.append("OPDRACHT: " + r["consigna_nl"])
    lineas.append("DE REGEL: " + r["regla"])
    lineas.append("VERLOOP: " + " | ".join(es for es, _nl in r["pasos"]))
    lineas.append("SLEUTEL: " + "  ||  ".join(r["clave"]))
    if r.get("nota"):
        lineas.append("NOTA: " + r["nota"])
    ps = "".join('<a:p><a:r><a:t>%s</a:t></a:r></a:p>' % esc(l) for l in lineas)
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<p:notes xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
            'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
            '<p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/>'
            '</p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/>'
            '<a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'
            '<p:sp><p:nvSpPr><p:cNvPr id="2" name="Slide Image Placeholder 1"/>'
            '<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="sldImg" idx="2"/>'
            '</p:nvPr></p:nvSpPr><p:spPr/></p:sp>'
            '<p:sp><p:nvSpPr><p:cNvPr id="3" name="Notes Placeholder 2"/>'
            '<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
            '<p:nvPr><p:ph type="body" idx="3" sz="quarter"/></p:nvPr></p:nvSpPr><p:spPr/>'
            '<p:txBody><a:bodyPr/><a:lstStyle/>%s</p:txBody></p:sp>'
            '</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:notes>' % ps)


# ---------------------------------------------------------------------------
# pakketboekhouding
# ---------------------------------------------------------------------------

def ya_tiene_retos(partes):
    """Staan er al reto-dia's in? Zonder deze controle zet een tweede run ze
    er een tweede keer bij — en dat gebeurt vanzelf zodra iemand
    `gen_u<N>_docente.py` draait op een machine mét python-pptx: die generator
    bouwt dezelfde dia's ook."""
    for n, datos in partes.items():
        if re.match(r"ppt/slides/slide\d+\.xml$", n) and b"RETO " in datos \
                and b"LA REGLA DEL RETO" in datos:
            return True
    return False


def inserta(origen, destino, retos, despues_de):
    """Voegt de dia's toe ná dianummer `despues_de` (1-gebaseerd)."""
    z = zipfile.ZipFile(origen)
    partes = {n: z.read(n) for n in z.namelist()}
    orden = z.namelist()
    z.close()
    if ya_tiene_retos(partes):
        return 0, len(re.findall(rb"<p:sldId ", partes["ppt/presentation.xml"]))

    nums = [int(re.findall(r"\d+", n)[0]) for n in partes if re.match(r"ppt/slides/slide\d+\.xml$", n)]
    siguiente = max(nums) + 1
    pres = partes["ppt/presentation.xml"].decode()
    rels = partes["ppt/_rels/presentation.xml.rels"].decode()
    ct = partes["[Content_Types].xml"].decode()
    max_rid = max(int(x) for x in re.findall(r'Id="rId(\d+)"', rels))
    max_sid = max(int(x) for x in re.findall(r'<p:sldId id="(\d+)"', pres))
    # de layout die de bestaande dia's gebruiken, zodat de nieuwe erbij passen
    layout = re.search(r'Target="(\.\./slideLayouts/[^"]+)"',
                       partes["ppt/slides/_rels/slide2.xml.rels"].decode()).group(1)
    notas_nums = [int(re.findall(r"\d+", n)[0]) for n in partes
                  if re.match(r"ppt/notesSlides/notesSlide\d+\.xml$", n)]
    max_notes = max(notas_nums) if notas_nums else 0

    nuevas = []
    for r in retos:
        nombre = "ppt/slides/slide%d.xml" % siguiente
        partes[nombre] = dia_reto(r).encode("utf8")
        # spreker-notities met de sleutel — alleen zinvol als het deck een
        # notesMaster heeft; het leerlingdeck krijgt ze net zo goed, want ze zijn
        # in de diavoorstelling niet zichtbaar
        nnum = max_notes + len(nuevas) + 1
        nnombre = "ppt/notesSlides/notesSlide%d.xml" % nnum
        partes[nnombre] = notas(r).encode("utf8")
        partes["ppt/notesSlides/_rels/notesSlide%d.xml.rels" % nnum] = (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
            'relationships/notesMaster" Target="../notesMasters/notesMaster1.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
            'relationships/slide" Target="../slides/slide%d.xml"/></Relationships>'
            % siguiente).encode("utf8")
        ct = ct.replace("</Types>",
                        '<Override PartName="/%s" ContentType="application/vnd.openxmlformats-'
                        'officedocument.presentationml.notesSlide+xml"/></Types>' % nnombre)
        partes["ppt/slides/_rels/slide%d.xml.rels" % siguiente] = (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
            'relationships/slideLayout" Target="%s"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
            'relationships/notesSlide" Target="../notesSlides/notesSlide%d.xml"/>'
            '</Relationships>' % (layout, nnum)).encode("utf8")
        orden += [nombre, "ppt/slides/_rels/slide%d.xml.rels" % siguiente,
                  nnombre, "ppt/notesSlides/_rels/notesSlide%d.xml.rels" % nnum]
        max_rid += 1
        max_sid += 1
        rels = rels.replace("</Relationships>",
                            '<Relationship Id="rId%d" Type="http://schemas.openxmlformats.org/'
                            'officeDocument/2006/relationships/slide" Target="slides/slide%d.xml"/>'
                            "</Relationships>" % (max_rid, siguiente))
        ct = ct.replace("</Types>",
                        '<Override PartName="/ppt/slides/slide%d.xml" ContentType="application/'
                        'vnd.openxmlformats-officedocument.presentationml.slide+xml"/></Types>'
                        % siguiente)
        nuevas.append('<p:sldId id="%d" r:id="rId%d"/>' % (max_sid, max_rid))
        siguiente += 1

    # op de juiste plaats in de volgorde zetten
    ids = re.findall(r'<p:sldId [^/]*/>', re.search(r"<p:sldIdLst>(.*?)</p:sldIdLst>", pres, re.S).group(1))
    ids[despues_de:despues_de] = nuevas
    pres = re.sub(r"<p:sldIdLst>.*?</p:sldIdLst>",
                  "<p:sldIdLst>%s</p:sldIdLst>" % "".join(ids), pres, flags=re.S)

    partes["ppt/presentation.xml"] = pres.encode("utf8")
    partes["ppt/_rels/presentation.xml.rels"] = rels.encode("utf8")
    partes["[Content_Types].xml"] = ct.encode("utf8")

    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as out:
        for n in orden:
            out.writestr(n, partes[n])
    return len(nuevas), len(ids)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck", nargs="?")
    ap.add_argument("--curso", default="C5")
    ap.add_argument("--unidad", type=int, default=0)
    ap.add_argument("--after", type=int, default=6, help="na welk dianummer")
    ap.add_argument("--todo", action="store_true", help="alle decks van U0 en U1")
    a = ap.parse_args()

    trabajos = ([(("C5_U0_%s.pptx" % m), "C5", 0, 6) for m in ("docente", "alumno")]
                + [(("C5_U1_%s.pptx" % m), "C5", 1, 6) for m in ("docente", "alumno")]) \
        if a.todo else [(a.deck, a.curso, a.unidad, a.after)]

    for deck, curso, unidad, after in trabajos:
        ruta = deck if os.path.isabs(deck) else os.path.join(HERE, deck)
        retos = [r for r in RD.de(curso, unidad) if r["soporte"] == "ppt"]
        tmp = ruta + ".tmp"
        n, total = inserta(ruta, tmp, retos, after)
        if n == 0:
            if os.path.exists(tmp):
                os.remove(tmp)
            print("  %-24s bevat de reto-dia's al — niets gedaan" % os.path.basename(ruta))
            continue
        shutil.move(tmp, ruta)
        print("  %-24s +%d reto-dia's → %d dia's" % (os.path.basename(ruta), n, total))


if __name__ == "__main__":
    main()
