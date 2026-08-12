#!/usr/bin/env python3
"""Reviewdocument (.docx) van een print-unit — om na te lezen, niet om te drukken.

WAAROM DIT GEEN OMZETTING IS
De cursus-PDF's zijn met de hand opgemaakt: kaders die precies op een blad
passen, kolommen, schrijflijnen op millimeters. Elke omzetter die daar Word van
maakt, maakt er iets van dat er *bijna* uitziet zoals het boek — en juist dat
«bijna» kost tijd: je leest dan de opmaak na in plaats van de inhoud, en de
opmerkingen die u maakt gaan over een layout die in de echte PDF niet bestaat.

Dit document doet het omgekeerde: het gooit de opmaak wég. Alles wordt
doorlopende tekst met koppen, genummerde oefeningen en een brede rechtermarge.
Het lijkt niet op de cursus — dat is de bedoeling. U kijkt de inhoud na
(taal, opdrachten, volgorde, moeilijkheid), zet uw opmerkingen erbij met de
Word-functie die u gewoon bent, en die opmerkingen verwerk ik daarna in de
échte bron. De opmaak van het boek verandert er niet door.

WAT ER GEBEURT MET WAT NIET IN TEKST KAN
  schrijflijn  →  ______  (zo lang als in het boek: kort · midden · lang · vol)
  schrijfvlak  →  [schrijfvlak]
  tabel        →  echte Word-tabel
  tekening/QR  →  weggelaten (die kijkt u in de PDF na)
  icoontje     →  weggelaten (het is interface, geen inhoud)

TECHNISCH
Een .docx is een zip met XML — python-docx is hier niet beschikbaar en
LibreOffice kan in deze sandbox geen enkel bestand openen, dus de XML wordt
hier met de hand geschreven. Dezelfde aanpak als bij de PowerPoints.

GEBRUIK
    python3 gen_word_revision.py C5 1            → 03-build/revisie/C5_U1_revisie.docx
    python3 gen_word_revision.py --todos          → alle 31 units
"""

import html
import os
import re
import sys
import zipfile
from html.parser import HTMLParser

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
SALIDA = os.path.join(AQUI, "revisie")

# ── waar de units staan ────────────────────────────────────────────────────
CURSOS = {
    "C4":  {"nombre": "¡Bienvenidos al español!",
            "sub": "C4 · 4 Moderne talen",
            "color": "D64550", "oscuro": "A8323B",
            "ruta": lambda u: os.path.join(AQUI, "web", "print", "C4_U%d.html" % u),
            "unidades": range(1, 15)},
    "C5":  {"nombre": "Español en la práctica",
            "sub": "C5 · 5de jaar",
            "color": "1E9E74", "oscuro": "157355",
            "ruta": lambda u: os.path.join(RAIZ, "01-cursussen", "05-a1",
                                           "U%d" % u, "U%d.html" % u),
            "unidades": range(0, 9)},
    "C6+": {"nombre": "Más español en la práctica · edición única",
            "sub": "C6+ · 6de jaar (huidige cohorte)",
            "color": "7C56A9", "oscuro": "5B3E83",
            "ruta": lambda u: os.path.join(RAIZ, "01-cursussen", "06-vervolg",
                                           "U%d" % u, "C6plus_U%d.html" % u),
            "unidades": range(0, 8)},
}

ARCHIVO = {"C4": "C4", "C5": "C5", "C6+": "C6plus"}

# ── de kleine DOM ──────────────────────────────────────────────────────────
VACIOS = {"br", "img", "meta", "link", "input", "hr", "col", "source"}
BLOQUE = {"div", "p", "h1", "h2", "h3", "h4", "h5", "ul", "ol", "li",
          "table", "thead", "tbody", "tr", "td", "th", "section", "header",
          "footer", "nav", "article", "figure", "blockquote", "dl"}
FUERA = {"script", "style", "svg", "button", "nav", "head", "noscript"}
# klassen die in het reviewdocument niets toevoegen
CLASES_FUERA = {"editbar", "scr-spacer", "indice-pdf", "qr", "qrbox", "qrcode",
                "pagenum", "foot", "avw", "dot", "ic"}


class Nodo:
    __slots__ = ("tag", "clases", "hijos", "padre")

    def __init__(self, tag, clases=(), padre=None):
        self.tag = tag
        self.clases = set(clases)
        self.hijos = []
        self.padre = padre


class Lector(HTMLParser):
    """Zet de HTML om in een boom. Tolerant: sluitende tags die niet kloppen
    worden genegeerd i.p.v. de boom te breken."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.raiz = Nodo("root")
        self.actual = self.raiz
        self.saltar = 0

    def handle_starttag(self, tag, attrs):
        if self.saltar:
            if tag not in VACIOS:
                self.saltar += 1
            return
        if tag in FUERA:
            self.saltar = 1
            return
        cl = ""
        for k, v in attrs:
            if k == "class" and v:
                cl = v
        clases = cl.split()
        if CLASES_FUERA & set(clases):
            self.saltar = 1
            return
        n = Nodo(tag, clases, self.actual)
        self.actual.hijos.append(n)
        if tag not in VACIOS:
            self.actual = n

    def handle_startendtag(self, tag, attrs):
        if self.saltar:
            return
        if tag == "br":
            self.actual.hijos.append(Nodo("br", (), self.actual))

    def handle_endtag(self, tag):
        if self.saltar:
            if tag not in VACIOS:
                self.saltar -= 1
            return
        n = self.actual
        while n is not self.raiz:
            if n.tag == tag:
                self.actual = n.padre
                return
            n = n.padre
        # sluitende tag zonder opening: negeren

    def handle_data(self, d):
        if self.saltar:
            return
        if not d.strip():
            # witruimte tussen twee tags is in HTML één spatie waard; zonder
            # dit plakken «Lucía» en «Sevilla» aan elkaar
            if self.actual.hijos:
                self.actual.hijos.append(" ")
            return
        self.actual.hijos.append(re.sub(r"\s+", " ", d))


def lee(ruta):
    src = open(ruta, encoding="utf-8").read()
    p = Lector()
    p.feed(src)
    p.close()
    return p.raiz


# ── tekst uit een tak halen ────────────────────────────────────────────────
SALTO = "\x00"          # merkteken voor een <br> uit het boek
LARGO = {"sm": 8, "md": 14, "lg": 20, "full": 34, "short": 8}
# stukjes die in het boek naast de tekst staan (cijfer, icoon, vinkje) en er
# in doorlopende tekst tégen aan zouden plakken
PEGAJOSO = {"ci", "ck", "ic", "num", "anum", "tag", "k", "lbl", "dot", "pk",
            "se", "badge", "cif", "ck2"}


def _linea(n):
    for c in ("full", "lg", "md", "sm", "short"):
        if c in n.clases:
            return "_" * LARGO[c]
    return "_" * 14


def es_wbox(n):
    """Een leeg geruit schrijfvlak — in het boek ruimte, hier een merkteken."""
    return "wbox" in n.clases and not any(isinstance(h, str) and h.strip()
                                          for h in n.hijos)


def _pega(n, k, h, prev):
    """Moet er een spatie tussen dit stuk en het vorige?

    In het boek liggen kaderdelen naast elkaar zonder witruimte in de HTML:
    twee chips (<span>…</span><span>…</span>), of een label met zijn tekst
    (<b>§0</b>Ponte al día). In doorlopende tekst plakken die aan elkaar.
    Een <b> midden ín een woord (Encantad<b>o</b>) blijft wél plakken — dat
    is precies waarom de regel naar de plaats in het kader kijkt en niet
    zomaar na elk element een spatie zet."""
    if isinstance(h, Nodo) and isinstance(prev, Nodo):
        return True
    if (k == 1 and isinstance(prev, Nodo) and isinstance(h, str)
            and h[:1] and not h[:1].isspace()
            and h[0] not in ".,;:!?)]}»…/-"):
        return True
    # tekst gevolgd door een kadertje met een hele frase erin («por la mañana»
    # + «de las 6:30 a las 8:30», die in het boek onder elkaar staan). Eén
    # woord in het kadertje is een woorduitgang (habl + o) en blijft plakken.
    if (isinstance(h, Nodo) and isinstance(prev, str) and prev[-1:].strip()
            and " " in texto(h).strip()):
        return True
    return False


def texto(n):
    """Platte tekst van een tak, met de schrijflijnen als streepjes."""
    if isinstance(n, str):
        return n
    if n.tag == "br":
        return " "
    if "wl" in n.clases:
        return " " + _linea(n) + " "
    if es_wbox(n):
        return " [schrijfvlak] "
    out = []
    prev = None
    for k, h in enumerate(n.hijos):
        if _pega(n, k, h, prev):
            out.append(" ")
        out.append(texto(h))
        if isinstance(h, Nodo) and (h.tag in BLOQUE or PEGAJOSO & h.clases):
            out.append(" ")
        prev = h
    return "".join(out)


def limpia(s):
    s = re.sub(r"[ \t\r\n ]+", " ", s)
    return s.strip()


def tiene_bloque(n):
    for h in n.hijos:
        if isinstance(h, Nodo) and h.tag in BLOQUE:
            return True
    return False


def tiene(n, tags=(), clases=()):
    for h in n.hijos:
        if isinstance(h, Nodo):
            if h.tag in tags or (clases and clases & h.clases):
                return True
            if tiene(h, tags, clases):
                return True
    return False


# ── WordprocessingML ───────────────────────────────────────────────────────
def esc(s):
    return html.escape(s, quote=False).replace('"', "&quot;")


def run(t, negrita=False, cursiva=False, color=None, tam=None, sub=False):
    if not t:
        return ""
    pr = ""
    if negrita:
        pr += "<w:b/>"
    if cursiva:
        pr += "<w:i/>"
    # de volgorde binnen <w:rPr> ligt vast in het schema: b · i · color · sz · u
    if color:
        pr += '<w:color w:val="%s"/>' % color
    if tam:
        pr += '<w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (tam * 2, tam * 2)
    if sub:
        pr += '<w:u w:val="single"/>'
    pr = "<w:rPr>%s</w:rPr>" % pr if pr else ""
    return '<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (pr, esc(t))


def parrafo(runs, estilo=None, sangria=0, antes=0, despues=60, borde=None,
            sombra=None, alinea=None, conserva=False):
    pr = ""
    if estilo:
        pr += '<w:pStyle w:val="%s"/>' % estilo
    if conserva:
        pr += "<w:keepNext/>"
    if borde:
        pr += ('<w:pBdr><w:left w:val="single" w:sz="18" w:space="8" '
               'w:color="%s"/></w:pBdr>' % borde)
    if sombra:
        pr += '<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % sombra
    # en binnen <w:pPr>: … pBdr · shd · spacing · ind · jc
    pr += '<w:spacing w:before="%d" w:after="%d"/>' % (antes, despues)
    if sangria:
        pr += '<w:ind w:left="%d"/>' % sangria
    if alinea:
        pr += '<w:jc w:val="%s"/>' % alinea
    return "<w:p><w:pPr>%s</w:pPr>%s</w:p>" % (pr, "".join(runs))


# ── inline: b/i/u/gloss → echte opmaak ─────────────────────────────────────
# een run = (tekst, vet, cursief, kleur); pas op het einde XML, zodat de
# witruimte ertussen nog op te schonen valt
def inline(n, negrita=False, cursiva=False, color=None):
    """Runs van een tak, met vet/cursief en de Nederlandse gloss in grijs."""
    out = []
    if isinstance(n, str):
        return [(n, negrita, cursiva, color)]
    if n.tag == "br":
        return [(SALTO, negrita, cursiva, color)]
    if "wl" in n.clases:
        return [(" ", False, False, None), (_linea(n), False, False, "808080"),
                (" ", False, False, None)]
    if es_wbox(n):
        return [(" [schrijfvlak] ", False, True, "808080")]
    b = negrita or n.tag in ("b", "strong", "th")
    i = cursiva or n.tag in ("i", "em")
    c = color
    if "gloss" in n.clases or "nl" in n.clases:
        c, i = "6B6B6B", True
    if "trap" in n.clases:
        c = "B3261E"
    prev = None
    for k, h in enumerate(n.hijos):
        if _pega(n, k, h, prev):
            out.append((" ", False, False, None))
        out += inline(h, b, i, c)
        if isinstance(h, Nodo) and (h.tag in BLOQUE or PEGAJOSO & h.clases):
            out.append((" ", False, False, None))
        prev = h
    return out


def _pule(crudos):
    """Witruimte opschonen: geen dubbele spaties, geen spatie vooraan of
    achteraan, geen lege runs."""
    limpios = []
    for t, b, i, c in crudos:
        t = re.sub(r"[ \t\r\n ]+", " ", t)
        if not t:
            continue
        if limpios and limpios[-1][0].endswith(" ") and t.startswith(" "):
            t = t.lstrip()
            if not t:
                continue
        limpios.append((t, b, i, c))
    while limpios and not limpios[0][0].strip():
        limpios.pop(0)
    while limpios and not limpios[-1][0].strip():
        limpios.pop()
    if limpios:
        limpios[0] = (limpios[0][0].lstrip(),) + limpios[0][1:]
        limpios[-1] = (limpios[-1][0].rstrip(),) + limpios[-1][1:]
    if not any(t.strip() for t, _, _, _ in limpios):
        return []
    return limpios


def texto_runs(n, tam=None):
    """Alle runs van een tak als XML, in één alinea."""
    crudos = inline(n) if isinstance(n, Nodo) else [(n, False, False, None)]
    return [run(t.replace(SALTO, " "), b, i, c, tam=tam)
            for t, b, i, c in _pule(crudos)]


def texto_partido(n, tam=None):
    """Idem, maar gebroken op de <br>'s van het boek: een genummerde reeks
    (1. … 2. … 3. …) leest als een reeks en niet als één blok tekst."""
    crudos = inline(n) if isinstance(n, Nodo) else [(n, False, False, None)]
    partes, actual = [], []
    for t, b, i, c in crudos:
        if SALTO in t:
            trozos = t.split(SALTO)
            for j, tr in enumerate(trozos):
                if j:
                    partes.append(actual)
                    actual = []
                if tr:
                    actual.append((tr, b, i, c))
        else:
            actual.append((t, b, i, c))
    partes.append(actual)
    salida = []
    for p in partes:
        limpios = _pule(p)
        if limpios:
            salida.append([run(t, b, i, c, tam=tam) for t, b, i, c in limpios])
    return salida


# ── tabellen ───────────────────────────────────────────────────────────────
def celda_parrafos(n, ancho):
    ps = []
    for h in n.hijos:
        if isinstance(h, Nodo) and h.tag in ("p", "div", "ul", "ol") and tiene_bloque(h):
            ps += bloques(h, {})
    if not ps:
        for rs in texto_partido(n):
            ps.append(parrafo(rs, despues=0, antes=0))
    if not ps:
        ps = [parrafo([run("")], despues=0)]
    return ps


def tabla(n, color):
    filas = []
    for tr in _todos(n, "tr"):
        celdas = [c for c in tr.hijos if isinstance(c, Nodo) and c.tag in ("td", "th")]
        if celdas:
            filas.append(celdas)
    if not filas:
        return []
    cols = max(len(f) for f in filas)
    ancho = int(9000 / cols)
    grid = "".join('<w:gridCol w:w="%d"/>' % ancho for _ in range(cols))
    borde = ('<w:tblBorders>%s</w:tblBorders>'
             % "".join('<w:%s w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>' % b
                       for b in ("top", "left", "bottom", "right",
                                 "insideH", "insideV")))
    xml = ['<w:tbl><w:tblPr><w:tblW w:w="9000" w:type="dxa"/>%s'
           '<w:tblLayout w:type="fixed"/></w:tblPr><w:tblGrid>%s</w:tblGrid>'
           % (borde, grid)]
    for fi, f in enumerate(filas):
        cabecera = all(c.tag == "th" for c in f)
        xml.append("<w:tr>")
        if cabecera:
            xml.append("<w:trPr><w:tblHeader/></w:trPr>")
        for ci in range(cols):
            c = f[ci] if ci < len(f) else None
            sombra = ('<w:shd w:val="clear" w:color="auto" w:fill="EFEFEF"/>'
                      if cabecera else "")
            ps = celda_parrafos(c, ancho) if c is not None else [parrafo([run("")])]
            xml.append('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/>%s</w:tcPr>%s</w:tc>'
                       % (ancho, sombra, "".join(ps)))
        xml.append("</w:tr>")
    xml.append("</w:tbl>")
    xml.append(parrafo([run("")], despues=80))
    return xml


def _todos(n, tag):
    out = []
    for h in n.hijos:
        if isinstance(h, Nodo):
            if h.tag == tag:
                out.append(h)
            else:
                out += _todos(h, tag)
    return out


def _primero(n, clase=None, tag=None):
    for h in n.hijos:
        if isinstance(h, Nodo):
            if (clase and clase in h.clases) or (tag and h.tag == tag):
                return h
            r = _primero(h, clase, tag)
            if r is not None:
                return r
    return None


# ── de wandeling ───────────────────────────────────────────────────────────
def bloques(n, ctx):
    """Blokken van een tak. ctx draagt de cursuskleur en de oefenteller."""
    color = ctx.get("color", "444444")
    out = []
    # losse tekst en <b>/<i>/<span> tussen twee kaders horen bij elkaar in
    # één alinea — anders valt «…lijken op het Engels (palabras transparentes):»
    # uiteen in drie regels
    suelto = Nodo("div")

    def vacia():
        if not suelto.hijos:
            return
        rs = texto_runs(suelto)
        suelto.hijos = []
        if rs:
            out.append(parrafo(rs))

    for h in n.hijos:
        if isinstance(h, str):
            suelto.hijos.append(h)
            continue
        if h.tag in FUERA or CLASES_FUERA & h.clases:
            continue
        if h.tag not in BLOQUE and h.tag != "br" and not ({"act", "sec"} & h.clases):
            suelto.hijos.append(h)
            continue
        vacia()

        # ── oefening ───────────────────────────────────────────────────────
        if "act" in h.clases:
            out += oefening(h, ctx)
            continue

        # ── sectie ─────────────────────────────────────────────────────────
        if "sec" in h.clases:
            out += seccion(h, ctx)
            continue

        if h.tag == "table":
            out += tabla(h, color)
            continue

        # ── schrijfkolommen (sorteeroefening) ──────────────────────────────
        # alleen als de kolommen leeg zijn: dan is er niets dan een kop en
        # een geruit vlak. Staan er woorden in, dan is het inhoud en gaat ze
        # de gewone weg.
        if "wcols" in h.clases:
            cols, lleno = [], False
            for k in h.hijos:
                if not isinstance(k, Nodo):
                    continue
                # het geruite vlak heet .cb (C5/C6+) of .fill (C4); wat
                # daarbuiten staat, is de kop van de kolom
                vak = _primero(k, clase="cb") or _primero(k, clase="fill")
                cuerpo = limpia(texto(vak)) if vak is not None else ""
                if cuerpo:
                    lleno = True
                # de kop kan uit twee stukken bestaan (naam + onderschrift);
                # in het boek staan die onder elkaar, hier met een punt ertussen
                partes = []
                for x in k.hijos:
                    if isinstance(x, Nodo) and x is vak:
                        continue
                    t = limpia(texto(x))
                    if t and t != cuerpo:
                        partes.append(t)
                cols.append(" · ".join(partes))
            cols = [x for x in cols if x]
            if cols and not lleno:
                out.append(parrafo(
                    [run("Schrijfkolommen: ", cursiva=True, color="6B6B6B"),
                     run(" | ".join("%s → [schrijfruimte]" % x for x in cols))],
                    sangria=140, despues=60))
                continue

        if h.tag in ("ul", "ol"):
            for li in [x for x in h.hijos if isinstance(x, Nodo) and x.tag == "li"]:
                if tiene(li, tags=("table", "ul", "ol")):
                    out += bloques(li, ctx)
                else:
                    rs = texto_runs(li)
                    if rs:
                        out.append(parrafo([run("•  ")] + rs, sangria=280, despues=40))
            continue

        if h.tag in ("h1", "h2", "h3", "h4"):
            t = limpia(texto(h))
            if t:
                nivel = {"h1": "Kop1", "h2": "Kop2", "h3": "Kop2", "h4": "Kop3"}[h.tag]
                out.append(parrafo([run(t)], estilo=nivel, conserva=True))
            continue

        if h.tag == "br":
            continue

        # ── kaders die één regel mogen worden ──────────────────────────────
        if h.tag in BLOQUE and tiene_bloque(h):
            if compacto(h):
                t = " · ".join(x for x in (limpia(texto(k)) for k in h.hijos)
                               if x)
                if t:
                    out.append(parrafo([run(t)], sangria=140, despues=60))
                continue
            out += bloques(h, ctx)
            continue

        # ── gewone alinea ──────────────────────────────────────────────────
        partes = texto_partido(h)
        if not partes:
            continue
        destaca = {"intro", "ojo", "regla", "esen", "steun", "route-note",
                   "modelo", "pista"} & h.clases
        marca = {"ojo": "¡Ojo! ", "steun": "Steun · ", "pista": "Tip · "}
        plano = limpia(texto(h))
        pre = [run(marca[c], negrita=True, color=color)
               for c in h.clases if c in marca
               and not plano.lower().startswith(marca[c].split()[0].lower())]
        for j, rs in enumerate(partes):
            if destaca:
                out.append(parrafo((pre if not j else []) + rs, borde=color,
                                   sangria=140, antes=40 if not j else 0,
                                   despues=80 if j == len(partes) - 1 else 20))
            else:
                out.append(parrafo(rs, despues=60 if j == len(partes) - 1 else 20))
    vacia()
    return out


def compacto(n):
    """Een kader dat in het boek visueel is (strip, kaartjes, badges) en in
    het reviewdocument als één regel meer waard is dan als vijf losse."""
    hijos = [h for h in n.hijos if isinstance(h, Nodo)]
    if len(hijos) < 2:
        return False
    if any(h.tag in ("p", "table", "ul", "ol", "h1", "h2", "h3", "h4")
           for h in hijos):
        return False
    if any({"act", "sec", "wbox"} & h.clases for h in hijos):
        return False
    if tiene(n, tags=("table", "ul", "ol", "p")):
        return False
    return len(limpia(texto(n))) <= 200


def oefening(n, ctx):
    """Een .act: kop «Oefening N · titel», de labels als grijze regel,
    daarna de inhoud."""
    color = ctx["color"]
    cab = _primero(n, clase="acthead")
    num = _primero(n, clase="anum")
    tit = _primero(n, clase="h")
    badges = _primero(n, clase="badges")
    ctx["n"] = ctx.get("n", 0) + 1
    etiqueta = limpia(texto(num)) if num is not None else str(ctx["n"])
    titulo = limpia(texto(tit)) if tit is not None else ""
    out = [parrafo([run("Oefening %s" % etiqueta, negrita=True, color=color),
                    run("  ·  " + titulo, negrita=True)] if titulo else
                   [run("Oefening %s" % etiqueta, negrita=True, color=color)],
                   estilo="Kop3", conserva=True)]
    if badges is not None:
        eti = " · ".join(x for x in (limpia(texto(k)) for k in badges.hijos
                                     if isinstance(k, Nodo)) if x)
        if eti:
            out.append(parrafo([run(eti, cursiva=True, color="6B6B6B", tam=8)],
                               antes=0, despues=60, conserva=True))
    for h in n.hijos:
        if isinstance(h, Nodo) and h is cab:
            continue
        sub = Nodo("div")
        sub.hijos = [h]
        out += bloques(sub, ctx)
    return out


def seccion(n, ctx):
    """Een .sec: kop + de rest. C5/C6+ hebben .pk, C4 heeft .se + h2."""
    pk = _primero(n, clase="pk")
    se = _primero(n, clase="se")
    h2 = _primero(n, tag="h2")
    titulo = limpia(texto(pk)) if pk is not None else limpia(texto(se) if se is not None else "")
    extra = limpia(texto(h2)) if h2 is not None and pk is None else ""
    if extra and extra != titulo:
        titulo = "%s — %s" % (titulo, extra) if titulo else extra
    out = []
    if titulo:
        out.append(parrafo([run(titulo)], estilo="Kop1", antes=320, despues=120,
                           conserva=True))
    saltar = {x for x in (pk, se, h2, _primero(n, clase="num")) if x is not None}
    for h in n.hijos:
        if isinstance(h, Nodo) and h in saltar:
            continue
        sub = Nodo("div")
        sub.hijos = [h]
        out += bloques(sub, ctx)
    return out


# ── het document ───────────────────────────────────────────────────────────
CT = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>
</Relationships>"""

SETTINGS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:zoom w:percent="100"/><w:defaultTabStop w:val="708"/>
<w:compat><w:compatSetting w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="15"/></w:compat>
</w:settings>"""


def styles(color, oscuro):
    def est(sid, nombre, tam, negrita, col, antes, despues, base=False,
            fuente="Calibri"):
        return ('<w:style w:type="paragraph" %sw:styleId="%s">'
                '<w:name w:val="%s"/>%s<w:qFormat/>'
                '<w:pPr><w:keepNext/><w:spacing w:before="%d" w:after="%d"/></w:pPr>'
                '<w:rPr><w:rFonts w:ascii="%s" w:hAnsi="%s"/>%s'
                '<w:color w:val="%s"/><w:sz w:val="%d"/><w:szCs w:val="%d"/></w:rPr>'
                '</w:style>'
                % ("w:default=\"1\" " if base else "", sid, nombre,
                   '<w:basedOn w:val="Normal"/>' if not base else "",
                   antes, despues, fuente, fuente,
                   "<w:b/>" if negrita else "", col, tam * 2, tam * 2))

    return ("""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults><w:rPrDefault><w:rPr>
<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>
<w:sz w:val="21"/><w:szCs w:val="21"/><w:lang w:val="nl-BE"/>
</w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="80" w:line="264" w:lineRule="auto"/></w:pPr></w:pPrDefault>
</w:docDefaults>"""
            + '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
              '<w:name w:val="Normal"/><w:qFormat/></w:style>'
            + est("Titel", "Title", 22, True, oscuro, 0, 120)
            + est("Kop1", "heading 1", 15, True, color, 320, 120)
            + est("Kop2", "heading 2", 12, True, oscuro, 240, 100)
            + est("Kop3", "heading 3", 11, True, "333333", 180, 60)
            + "</w:styles>")


def core(titulo):
    return ("""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
 xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:title>%s</dc:title><dc:creator>Español en la práctica</dc:creator>
<cp:lastModifiedBy>Español en la práctica</cp:lastModifiedBy>
</cp:coreProperties>""" % esc(titulo))


APP = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">
<Application>Español en la práctica</Application></Properties>"""

# A4 = 11906 × 16838 twips. Links 1134 (2 cm), rechts 3402 (6 cm) voor
# opmerkingen in de marge.
SECTPR = ('<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
          '<w:pgMar w:top="1134" w:right="3402" w:bottom="1134" w:left="1134"'
          ' w:header="708" w:footer="708" w:gutter="0"/>'
          '<w:lnNumType w:countBy="5" w:restart="continuous" w:distance="284"/>'
          '</w:sectPr>')


def portada(curso, unidad, titulo_unidad, sub, eyebrow="", pregunta=""):
    c = CURSOS[curso]
    hoy = "12 augustus 2026"
    out = [
        parrafo([run("%s · Unidad %d" % (c["sub"], unidad), color=c["oscuro"],
                     negrita=True, tam=10)], despues=40),
        parrafo([run(c["nombre"])], estilo="Titel", despues=40),
        parrafo([run(titulo_unidad, negrita=True, tam=14, color=c["oscuro"])],
                despues=60),
    ]
    if eyebrow:
        out.append(parrafo([run(eyebrow, color="6B6B6B", tam=9)], despues=60))
    if sub:
        out.append(parrafo([run(sub, cursiva=True, color="555555")], despues=60))
    if pregunta:
        out.append(parrafo([run(pregunta, negrita=True, color=c["color"])],
                           despues=200))
    out += [
        parrafo([run("Reviewdocument — %s" % hoy, color="6B6B6B", tam=9)],
                despues=200),
        parrafo([run("Zo leest u dit", negrita=True, color=c["color"])],
                borde=c["color"], sangria=140, antes=120, despues=40),
        parrafo([run("Dit is niet de cursus. De opmaak is er bewust uit gehaald, "
                     "zodat u de ")] +
                [run("inhoud", negrita=True)] +
                [run(" nakijkt: de taal, de opdrachten, de volgorde, de "
                     "moeilijkheid. Zet uw opmerkingen erbij zoals u gewoon "
                     "bent (Controleren ▸ Nieuwe opmerking, of gewoon in het "
                     "rood typen). Ik verwerk ze daarna in de bron en lever "
                     "opnieuw in PDF.")],
                borde=c["color"], sangria=140, despues=40),
        parrafo([run("Opmerkingen over de ")] + [run("opmaak", negrita=True)] +
                [run(" kan ik hier niet plaatsen — die staat in dit document "
                     "niet. Daarvoor gebruikt u de PDF.")],
                borde=c["color"], sangria=140, despues=40),
        parrafo([run("Schrijflijnen staan als ______ (even lang als in het "
                     "boek), schrijfvlakken als [schrijfvlak]. Tekeningen, "
                     "QR-codes en icoontjes zijn weggelaten. In de linkermarge "
                     "staan regelnummers, handig om naar te verwijzen.",
                     color="555555", tam=9)],
                borde=c["color"], sangria=140, despues=120),
        # de unit zelf begint op een nieuwe bladzijde
        "<w:p><w:r><w:br w:type=\"page\"/></w:r></w:p>",
    ]
    return out


def documento(curso, unidad):
    c = CURSOS[curso]
    ruta = c["ruta"](unidad)
    if not os.path.exists(ruta):
        raise SystemExit("bestaat niet: %s" % ruta)
    raiz = lee(ruta)
    body = _primero(raiz, tag="body") or raiz

    hero = _primero(body, clase="hero")
    h1 = _primero(hero, tag="h1") if hero is not None else _primero(body, tag="h1")
    titulo_unidad = limpia(texto(h1)) if h1 is not None else "Unidad %d" % unidad
    subt = _primero(hero, clase="sub") if hero is not None else None
    sub = limpia(texto(subt)) if subt is not None else ""
    eye = _primero(hero, clase="eyebrow") if hero is not None else None
    preg = _primero(hero, clase="q") if hero is not None else None

    ctx = {"color": c["color"], "oscuro": c["oscuro"], "n": 0}
    cuerpo = portada(curso, unidad, titulo_unidad, sub,
                     limpia(texto(eye)) if eye is not None else "",
                     limpia(texto(preg)) if preg is not None else "")
    for h in body.hijos:
        if isinstance(h, Nodo) and h is hero:
            continue
        sub_n = Nodo("div")
        sub_n.hijos = [h]
        cuerpo += bloques(sub_n, ctx)

    doc = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
           '<w:body>%s%s</w:body></w:document>' % ("".join(cuerpo), SECTPR))
    return doc, titulo_unidad, ctx["n"]


def construye(curso, unidad):
    c = CURSOS[curso]
    doc, titulo, n = documento(curso, unidad)
    os.makedirs(SALIDA, exist_ok=True)
    destino = os.path.join(SALIDA, "%s_U%d_revisie.docx"
                           % (ARCHIVO[curso], unidad))
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CT)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("word/document.xml", doc)
        z.writestr("word/styles.xml", styles(c["color"], c["oscuro"]))
        z.writestr("word/settings.xml", SETTINGS)
        z.writestr("docProps/core.xml",
                   core("%s · U%d %s" % (c["nombre"], unidad, titulo)))
        z.writestr("docProps/app.xml", APP)
    return destino, titulo, n, len(doc)


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__.split("GEBRUIK")[-1])
        raise SystemExit(0)
    if args[0] == "--todos":
        tareas = [(c, u) for c in ("C4", "C5", "C6+") for u in CURSOS[c]["unidades"]]
    else:
        tareas = [(args[0], int(args[1]))]
    for curso, unidad in tareas:
        destino, titulo, n, largo = construye(curso, unidad)
        print("%-6s U%-2d  %-32s %2d oefeningen  %6d B XML  → %s"
              % (curso, unidad, titulo[:32], n, largo,
                 os.path.relpath(destino, RAIZ)))
