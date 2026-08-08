#!/usr/bin/env python3
"""Beeldcontrole voor dia's, zonder LibreOffice.

LibreOffice converteert in deze omgeving niets meer — ook geen tekstbestand —
dus de gewone weg naar een render bestaat hier niet. Deze previewer leest de
dia-XML terug uit het pptx en tekent hem als HTML op ware verhouding. Het is
géén PowerPoint-render: lettertypes en woordafbreking verschillen. Wat je er
wél mee ziet, en dat is waar het om gaat: staan de vormen waar ze horen,
overlappen ze, en loopt tekst uit zijn kader.

    python3 vista_previa.py deck.pptx 24 25 26 -o /tmp/preview.html
"""
import argparse
import html
import zipfile
from xml.etree import ElementTree as ET

P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
EMU_W, EMU_H = 12191695, 6858000
PX_W = 1280


def _color(el):
    c = el.find(".//" + A + "srgbClr") if el is not None else None
    return "#" + c.get("val") if c is not None else None


def dia_html(xml, titulo):
    raiz = ET.fromstring(xml)
    esc = PX_W / EMU_W
    piezas = []
    for sp in raiz.iter(P + "sp"):
        xfrm = sp.find(".//" + A + "xfrm")
        if xfrm is None:
            continue
        off, ext = xfrm.find(A + "off"), xfrm.find(A + "ext")
        x, y = int(off.get("x")) * esc, int(off.get("y")) * esc
        w, h = int(ext.get("cx")) * esc, int(ext.get("cy")) * esc
        spPr = sp.find(P + "spPr")
        relleno = _color(spPr.find(A + "solidFill")) if spPr is not None else None
        ln = spPr.find(A + "ln") if spPr is not None else None
        borde = _color(ln) if ln is not None and ln.find(".//" + A + "srgbClr") is not None else None
        geo = spPr.find(A + "prstGeom") if spPr is not None else None
        radio = "10px" if geo is not None and geo.get("prst") == "roundRect" else "0"
        # de tekst, per alinea en per run
        parrafos = []
        for p in sp.iter(A + "p"):
            runs = []
            for r in p.findall(A + "r"):
                t = r.find(A + "t")
                rPr = r.find(A + "rPr")
                sz = int(rPr.get("sz", "1400")) / 100 if rPr is not None else 14
                col = _color(rPr) if rPr is not None else "#20242E"
                b = "700" if rPr is not None and rPr.get("b") == "1" else "400"
                it = "italic" if rPr is not None and rPr.get("i") == "1" else "normal"
                fam = "sans-serif"
                lat = rPr.find(A + "latin") if rPr is not None else None
                if lat is not None and "Bricolage" in (lat.get("typeface") or ""):
                    fam = "'Trebuchet MS',sans-serif"
                runs.append('<span style="font-size:%.1fpx;color:%s;font-weight:%s;'
                            'font-style:%s;font-family:%s">%s</span>'
                            % (sz * (PX_W / 960), col or "#20242E", b, it, fam,
                               html.escape(t.text or "" if t is not None else "")))
            if runs:
                alin = p.find(A + "pPr")
                algn = {"ctr": "center", "r": "right"}.get(
                    alin.get("algn") if alin is not None else "l", "left")
                parrafos.append('<p style="margin:0;text-align:%s">%s</p>' % (algn, "".join(runs)))
        estilo = ("position:absolute;left:%.1fpx;top:%.1fpx;width:%.1fpx;height:%.1fpx;"
                  "border-radius:%s;box-sizing:border-box;padding:3px 5px;overflow:visible;"
                  % (x, y, w, h, radio))
        if relleno:
            estilo += "background:%s;" % relleno
        if borde:
            estilo += "border:1px solid %s;" % borde
        piezas.append('<div style="%s">%s</div>' % (estilo, "".join(parrafos)))
    return ('<figure class="dia"><figcaption>%s</figcaption>'
            '<div class="lienzo">%s</div></figure>'
            % (html.escape(titulo), "".join(piezas)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("slides", nargs="+", type=int)
    ap.add_argument("-o", default="preview.html")
    a = ap.parse_args()
    z = zipfile.ZipFile(a.deck)
    cuerpo = "".join(dia_html(z.read("ppt/slides/slide%d.xml" % n), "slide%d" % n)
                     for n in a.slides)
    alto = PX_W * EMU_H / EMU_W
    open(a.o, "w", encoding="utf-8").write(
        '<!doctype html><meta charset="utf-8"><style>'
        'body{background:#333;margin:0;padding:16px;font-family:sans-serif}'
        '.dia{margin:0 0 20px}figcaption{color:#bbb;font-size:12px;margin-bottom:4px}'
        '.lienzo{position:relative;width:%dpx;height:%.0fpx;background:#fff;overflow:hidden}'
        '</style>%s' % (PX_W, alto, cuerpo))
    print("geschreven:", a.o)


if __name__ == "__main__":
    main()
