#!/usr/bin/env python3
"""Rekent een zelfgeschreven .docx na — Word doet dat niet mildjes.

WAAROM
De reviewdocumenten worden hier met de hand als XML geschreven (§ zie
`gen_word_revision.py`), want python-docx is er niet en LibreOffice kan in deze
sandbox geen enkel bestand openen. Er is dus geen programma dat het bestand
opent vóór de auteur het opent. Deze controle vervangt dat: ze kijkt naar de
twee dingen die Word wél weigert — een ontbrekend onderdeel in de zip, en
kinderen van een element in de verkeerde volgorde — en daarna of de inhoud van
de unit er compleet in staat.

De volgordes hieronder komen uit het officiële schema (ISO/IEC 29500-4:2016,
wml.xsd, CT_PPr · CT_RPr · CT_SectPr · CT_TblPr · CT_TcPr · CT_TrPr ·
CT_Style). Word leest een document met kinderen in de verkeerde volgorde niet
als «bijna goed» maar als stuk.

GEBRUIK
    python3 revisar_docx.py revisie/C5_U1_revisie.docx [C5 1]
    python3 revisar_docx.py --todos
"""

import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

ORDEN = {
    "pPr": ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr",
            "widowControl", "numPr", "suppressLineNumbers", "pBdr", "shd",
            "tabs", "suppressAutoHyphens", "kinsoku", "wordWrap",
            "overflowPunct", "topLinePunct", "autoSpaceDE", "autoSpaceDN",
            "bidi", "adjustRightInd", "snapToGrid", "spacing", "ind",
            "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc",
            "textDirection", "textAlignment", "textboxTightWrap", "outlineLvl",
            "divId", "cnfStyle", "rPr", "sectPr", "pPrChange"],
    "rPr": ["rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps",
            "strike", "dstrike", "outline", "shadow", "emboss", "imprint",
            "noProof", "snapToGrid", "vanish", "webHidden", "color", "spacing",
            "w", "kern", "position", "sz", "szCs", "highlight", "u", "effect",
            "bdr", "shd", "fitText", "vertAlign", "rtl", "cs", "em", "lang",
            "eastAsianLayout", "specVanish", "oMath", "rPrChange"],
    "sectPr": ["headerReference", "footerReference", "footnotePr", "endnotePr",
               "type", "pgSz", "pgMar", "paperSrc", "pgBorders", "lnNumType",
               "pgNumType", "cols", "formProt", "vAlign", "noEndnote",
               "titlePg", "textDirection", "bidi", "rtlGutter", "docGrid",
               "printerSettings", "sectPrChange"],
    "tblPr": ["tblStyle", "tblpPr", "tblOverlap", "bidiVisual",
              "tblStyleRowBandSize", "tblStyleColBandSize", "tblW", "jc",
              "tblCellSpacing", "tblInd", "tblBorders", "shd", "tblLayout",
              "tblCellMar", "tblLook", "tblCaption", "tblDescription",
              "tblPrChange"],
    "tcPr": ["cnfStyle", "tcW", "gridSpan", "hMerge", "vMerge", "tcBorders",
             "shd", "noWrap", "tcMar", "textDirection", "tcFitText", "vAlign",
             "hideMark", "headers", "cellIns", "cellDel", "cellMerge",
             "tcPrChange"],
    "trPr": ["cnfStyle", "divId", "gridBefore", "gridAfter", "wBefore",
             "wAfter", "cantSplit", "trHeight", "tblHeader", "tblCellSpacing",
             "jc", "hidden", "ins", "del", "trPrChange"],
    "style": ["name", "aliases", "basedOn", "next", "link", "autoRedefine",
              "hidden", "uiPriority", "semiHidden", "unhideWhenUsed",
              "qFormat", "locked", "personal", "personalCompose",
              "personalReply", "rsid", "pPr", "rPr", "tblPr", "trPr", "tcPr",
              "tblStylePr"],
}

PIEZAS = ["[Content_Types].xml", "_rels/.rels", "word/document.xml",
          "word/styles.xml", "word/_rels/document.xml.rels"]


def _texto(doc):
    """De tekst van het document. Binnen één alinea plakken de runs aan
    elkaar — «habl» + «o» is één woord, want de uitgang staat in een eigen
    run — tussen alinea's komt een regeleinde."""
    return "\n".join("".join(t.text or "" for t in p.iter(W + "t"))
                     for p in doc.iter(W + "p"))


def revisa(ruta, fuente=None):
    fallos, avisos = [], []
    z = zipfile.ZipFile(ruta)
    nombres = z.namelist()
    for p in PIEZAS:
        if p not in nombres:
            fallos.append("ontbreekt in de zip: %s" % p)

    arboles = {}
    for n in nombres:
        try:
            arboles[n] = ET.fromstring(z.read(n))
        except ET.ParseError as e:
            fallos.append("%s is geen geldige XML: %s" % (n, e))

    # ── volgorde van de kinderen ──────────────────────────────────────────
    for n, raiz in arboles.items():
        for el in raiz.iter():
            tag = el.tag.split("}")[-1]
            if tag not in ORDEN:
                continue
            ref = ORDEN[tag]
            pos, ultimo, previo = -1, None, None
            for ch in el:
                t = ch.tag.split("}")[-1]
                if t not in ref:
                    avisos.append("%s: <w:%s> kent <w:%s> niet" % (n, tag, t))
                    continue
                i = ref.index(t)
                if i < pos:
                    fallos.append("%s: in <w:%s> staat <w:%s> ná <w:%s> — "
                                  "het schema wil de omgekeerde volgorde"
                                  % (n, tag, t, previo))
                pos, previo = max(pos, i), t

    # ── xml:space bij tekst met spaties ───────────────────────────────────
    doc = arboles.get("word/document.xml")
    if doc is not None:
        sin = 0
        for t in doc.iter(W + "t"):
            v = t.text or ""
            if v != v.strip() and t.get("{http://www.w3.org/XML/1998/namespace}space") != "preserve":
                sin += 1
        if sin:
            fallos.append("%d stukjes tekst met een spatie ervoor of erna "
                          "missen xml:space=\"preserve\" — Word gooit die weg" % sin)

        # ── tabellen: evenveel cellen als kolommen ────────────────────────
        for k, tbl in enumerate(doc.iter(W + "tbl"), 1):
            cols = len(tbl.findall(W + "tblGrid/" + W + "gridCol"))
            for fila, tr in enumerate(tbl.findall(W + "tr"), 1):
                celdas = len(tr.findall(W + "tc"))
                if celdas != cols:
                    fallos.append("tabel %d, rij %d: %d cellen bij %d kolommen"
                                  % (k, fila, celdas, cols))
            for tc in tbl.iter(W + "tc"):
                if not tc.findall(W + "p"):
                    fallos.append("tabel %d: een cel zonder alinea (Word "
                                  "weigert een lege cel)" % k)

        cuerpo = doc.find(W + "body")
        if cuerpo is None or len(cuerpo) == 0 or cuerpo[-1].tag != W + "sectPr":
            fallos.append("de body eindigt niet op <w:sectPr>")

    # ── staat de inhoud van de unit er volledig in? ───────────────────────
    texto_doc = ""
    if doc is not None:
        texto_doc = _texto(doc)
    if fuente:
        import gen_word_revision as G
        curso, unidad = fuente
        raiz = G.lee(G.CURSOS[curso]["ruta"](unidad))
        body = G._primero(raiz, tag="body")
        html = G.limpia(G.texto(body))
        pat = r"[^\W\d_]+"
        c1, c2 = Counter(re.findall(pat, html)), Counter(re.findall(pat, texto_doc))
        falta = sorted(((w, n - c2.get(w, 0)) for w, n in c1.items()
                        if n > c2.get(w, 0)), key=lambda x: -x[1])
        # de hero-tab («U1 · ¿QUIÉN ERES?») en de sectiebadges (V, T, ★) staan
        # bewust niet in het reviewdocument
        falta = [(w, n) for w, n in falta if len(w) > 1 and not w.isupper()]
        if falta:
            fallos.append("staat niet in het reviewdocument: %s"
                          % ", ".join("%s (%d×)" % x for x in falta[:12]))

    cifras = {}
    if doc is not None:
        cuerpo = doc.find(W + "body")
        cifras = {"alinea's": len(doc.findall(".//" + W + "p")),
                  "tabellen": len(list(doc.iter(W + "tbl"))),
                  "woorden": len(re.findall(r"[^\W\d_]+", texto_doc)),
                  "koppen": len(doc.findall(".//" + W + "pStyle"))}
    return fallos, avisos, cifras


if __name__ == "__main__":
    args = sys.argv[1:]
    trabajos = []
    if args and args[0] == "--todos":
        import gen_word_revision as G
        for c in ("C4", "C5", "C6+"):
            for u in G.CURSOS[c]["unidades"]:
                r = os.path.join(G.SALIDA, "%s_U%d_revisie.docx"
                                 % (G.ARCHIVO[c], u))
                if os.path.exists(r):
                    trabajos.append((r, (c, u)))
    elif args:
        trabajos = [(args[0], (args[1], int(args[2])) if len(args) > 2 else None)]
    else:
        raise SystemExit(__doc__.split("GEBRUIK")[-1])

    malos = 0
    for ruta, fuente in trabajos:
        fallos, avisos, cifras = revisa(ruta, fuente)
        print("── %s" % os.path.basename(ruta))
        print("   %s" % "  ·  ".join("%s %s" % (v, k) for k, v in cifras.items()))
        for a in sorted(set(avisos))[:5]:
            print("   ? %s" % a)
        for f in fallos:
            print("   ✗ %s" % f)
        if not fallos:
            print("   ✓ structuur, volgorde en inhoud kloppen")
        malos += bool(fallos)
    if malos:
        raise SystemExit("\n%d bestand(en) met fouten" % malos)
