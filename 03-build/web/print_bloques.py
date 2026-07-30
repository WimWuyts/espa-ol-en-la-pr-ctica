#!/usr/bin/env python3
"""Zet dezelfde inhoudsbronnen om in printblokken.

De hub krijgt van `hub_bloques.py` een zelfcorrigerende versie; hier komt de
papieren versie van precies dezelfde inhoud, met antwoordruimte volgens
CLAUDE.md §14 (`wl` schrijflijn, `wcols`, `wbox`, `wtab`) en zonder oplossingen
— die horen in het docentmateriaal.

Het QR-balkje naast elke oefening komt uit `03-build/web/qr/balk_<ID>.html`,
al gegenereerd met echte QR-codes (segno). Het balkje draagt het oefening-ID als
anker, zodat print, PDF en hub naar hetzelfde punt wijzen.
"""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
QR_DIR = os.path.join(HIER, "qr")

# De opmaak van het balkje staat in _balkjes_overzicht.html; hier alleen wat de
# printcursus nodig heeft, in mm zodat het bij de rest van de bladspiegel past.
CSS = """
.qb{display:flex;align-items:center;gap:3mm;margin:3mm 0;padding:2mm 3mm;background:#FCFBF8;
    border:1px solid var(--line);border-left:1.2mm solid var(--g);border-radius:4pt;break-inside:avoid}
.qb-qr svg{width:16mm;height:16mm;display:block}
.qb-tx{display:flex;flex-direction:column;gap:.4mm;min-width:0}
.qb-t{font-size:9pt;line-height:1.2}
.qb-s{font-size:8pt;color:var(--mut)}
.qb-nl{font-style:italic}
.qb-id{margin-left:auto;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:6.5pt;
       color:#B6BAC2;letter-spacing:.04em;align-self:flex-start}
.lecp{border:1px solid var(--line);border-left:1.2mm solid var(--g);border-radius:8pt;
      padding:3mm 4mm;background:#fff;break-inside:avoid;margin:3mm 0}
.lecp h4{font-family:var(--disp);color:var(--gd);margin:0 0 1mm;font-size:12pt}
.lecp .lema{color:var(--mut);font-style:italic;margin:0 0 2mm}
.lecp ul{margin:2mm 0;padding-left:6mm}
.lecp .aviso{border:1px dashed var(--line);border-radius:6pt;padding:2mm 3mm;margin:2mm 0;background:#FAF9F5}
.fichatxt{display:flex;gap:4mm;flex-wrap:wrap;background:var(--gt);border-radius:5pt;
          padding:1.6mm 3mm;margin:2mm 0;font-size:8.4pt}
.fichatxt b{display:block;font-size:7pt;letter-spacing:.05em;text-transform:uppercase;color:var(--gd)}
.guionp{margin:2mm 0}
.guionp .gl{display:flex;gap:2.5mm;padding:1mm 0;border-bottom:.3pt solid var(--gt)}
.guionp .gw{font-size:7.6pt;color:var(--gd);text-transform:uppercase;letter-spacing:.04em;
            min-width:16mm;flex:none;padding-top:.6mm}
"""


def balk(ejercicio_id):
    """Het QR-balkje van één oefening, om pal naast die oefening te zetten.

    De balkjes met een ECHTE QR-code zijn al gegenereerd (segno) voor de
    blueprint-oefeningen; die worden hier ingelezen. Voor blokken zonder balkje
    komt er bewust GEEN nagemaakte QR: de hub-URL bestaat pas na de
    hosting-sweep (§18), en een QR die nergens heen gaat is slechter dan geen
    QR. In de plaats komt een gewone verwijzing — leerlingtekst, geen meta."""
    p = os.path.join(QR_DIR, "balk_%s.html" % ejercicio_id)
    if os.path.exists(p):
        return open(p, encoding="utf-8").read().strip()
    return ""


def puntero(tab, wat):
    """Verwijzing naar de digitale pagina, zonder QR."""
    return ('<div class="qb" style="border-left-color:var(--g)"><span class="qb-tx">'
            '<span class="qb-t"><b>En línea:</b> %s</span>'
            '<span class="qb-s qb-nl">Op de digitale pagina, tabblad «%s».</span>'
            '</span></div>' % (wat, tab))


def _acthead(num, titel, badges):
    b = "".join('<span class="badge%s">%s</span>' % (" skill" if s else "", t) for t, s in badges)
    return ('<div class="acthead"><span class="anum">%s</span><div><div class="h">%s</div>'
            '<div class="badges">%s</div></div></div>' % (num, titel, b))


def _lineas(n, klasse="wl md", per_rij=4, start=1):
    """Genummerde schrijflijnen — één per item, zoals §14 voorschrijft."""
    out, rij = [], []
    for i in range(n):
        rij.append('<b>%d.</b> <span class="%s"></span>' % (start + i, klasse))
        if len(rij) == per_rij:
            out.append('<div style="margin:2.4mm 0">%s</div>' % " &nbsp; ".join(rij)); rij = []
    if rij:
        out.append('<div style="margin:2.4mm 0">%s</div>' % " &nbsp; ".join(rij))
    return '<div style="margin-left:12.5mm;font-size:9.6pt">%s</div>' % "".join(out)


def nat_print(bloque, num, opgave_tekst=None, klasse="wl md", per_rij=4):
    """Blueprint-oefening op papier: de prompts staan er, het antwoord schrijft
    de leerling zelf. Geen opties afdrukken — op papier zou een vierkeuze het
    ophalen weer terugbrengen tot herkennen."""
    prompts = ", ".join(str(it["q"]) for it in bloque["items"])
    return """<div class="act">
    %s
    <p>%s <span class="gloss">%s</span></p>
    <p style="margin-left:12.5mm;font-size:9.6pt"><b>%s</b></p>
    %s
    <span class="steun">Apoyo: sin ayuda · productief · zelfde reeks online (QR)</span>
    %s</div>""" % (
        _acthead(num, bloque["titulo"],
                 [("✍️ Escribir", True), ("👤 Solo", False), ("± %d min" % max(4, bloque["aantal"] // 3), False),
                  ("★★☆", False)]),
        opgave_tekst or bloque.get("instruccion_es", ""),
        bloque.get("instruccion_nl", ""),
        prompts,
        _lineas(bloque["aantal"], klasse, per_rij),
        balk(bloque.get("qr_id", bloque["id"])))


def lectura_print(t, num):
    """De leestekst met de volledige route en schrijfruimte per stap."""
    cuerpo = []
    for soort, c in t["texto"]:
        if soort == "titulo":
            cuerpo.append("<h4>%s</h4>" % c)
        elif soort == "lema":
            cuerpo.append('<p class="lema">%s</p>' % c)
        elif soort == "firma":
            cuerpo.append('<p style="font-size:8.6pt;color:var(--mut)">%s</p>' % c)
        elif soort == "lista":
            cuerpo.append("<ul>%s</ul>" % "".join("<li>%s</li>" % x for x in c))
        elif soort == "aviso":
            cuerpo.append('<div class="aviso"><b>%s</b><p style="margin:1mm 0 0">%s</p></div>' % (c[0], c[1]))
        else:
            cuerpo.append("<p>%s</p>" % c)

    esc = "".join(
        '<div style="margin:2.4mm 0"><b>%d.</b> %s <span class="wl md"></span></div>' % (i + 1, e["q"])
        for i, e in enumerate(t["escanear"]))
    vf = "".join(
        '<div style="margin:2.4mm 0"><b>%d.</b> %s &nbsp; ☐ V &nbsp; ☐ F<br>'
        '<span style="font-size:8.4pt;color:var(--mut)">prueba:</span> <span class="wl full"></span></div>'
        % (i + 1, v["q"]) for i, v in enumerate(t["vf"]))
    ctx = "".join(
        '<div style="margin:2.4mm 0"><b>%d.</b> %s <span class="wl md"></span></div>' % (i + 1, c["q"])
        for i, c in enumerate(t["contexto"]))

    return """<div class="act">
    %s
    <div class="fichatxt"><span><b>Tekstsoort</b>%s</span><span><b>Afzender</b>%s</span><span><b>Ontvanger</b>%s</span><span><b>Leesdoel</b>%s</span></div>
    <p><b>1 · Antes de leer.</b> %s <span class="gloss">Kijk alleen naar titel, vlaggen en getallen.</span></p>
    <div style="margin-left:12.5mm">☐ %s</div>
    <p><b>2 · El texto.</b></p>
    <div class="lecp">%s</div>
    <p><b>3 · Comprensión global.</b> %s</p>
    <div style="margin-left:12.5mm"><span class="wl full"></span></div>
    <p><b>4 · Escanea.</b> Zoek het gegeven in de tekst.</p>
    <div style="margin-left:12.5mm;font-size:9.6pt">%s</div>
    <p><b>5 · Verdadero o falso — con prueba.</b> Kruis aan én schrijf de zin die het bewijst.</p>
    <div style="margin-left:12.5mm;font-size:9.6pt">%s</div>
    <p><b>6 · El significado por el contexto.</b></p>
    <div style="margin-left:12.5mm;font-size:9.6pt">%s</div>
    <p><b>7 · Tu reacción.</b> %s</p>
    <div class="wbox lg"></div>
    <span class="steun">Apoyo: tekst blijft zichtbaar · van receptief naar productief</span>
    %s</div>""" % (
        _acthead(num, "Lectura · %s" % t["titulo"],
                 [("📖 Leer", True), ("✍️ Escribir", True), ("👤 Solo", False), ("± 20 min", False), ("★★☆", False)]),
        t["tipo"], t["emisor"], t["receptor"], t["objetivo"],
        t["prediccion"]["q"],
        " &nbsp;&nbsp; ☐ ".join(t["prediccion"]["opts"]),
        "".join(cuerpo),
        t["global"]["q"], esc, vf, ctx,
        t["produccion"]["prompt"],
        puntero("Lectura", "de tekst met zelfcorrectie en de vertaling"))


def escucha_print(f, num, qr_html=None):
    """Het luisterfragment op papier: alle taken met antwoordruimte, en het
    transcript expres NIET — dat staat op de hub, ná de taken. Meelezen tijdens
    het luisteren maakt van luisteren een leesoefening."""
    det = "".join(
        '<div style="margin:2.4mm 0"><b>%d.</b> %s <span class="wl md"></span></div>' % (i + 1, d["q"])
        for i, d in enumerate(f["detalle"]))
    vf = "".join(
        '<div style="margin:2.4mm 0"><b>%d.</b> %s &nbsp; ☐ V &nbsp; ☐ F<br>'
        '<span style="font-size:8.4pt;color:var(--mut)">prueba:</span> <span class="wl full"></span></div>'
        % (i + 1, v["q"]) for i, v in enumerate(f["vf"]))
    claves = " &nbsp;·&nbsp; ".join("<b>%s</b>" % c for c in f["situacion"]["claves"])
    return """<div class="act">
    %s
    <p><b>1 · Antes de escuchar.</b> <span class="gloss">Lees eerst de situatie — dan weet je waar je op moet letten.</span></p>
    <div class="fichatxt"><span><b>¿Dónde?</b>%s</span><span><b>¿Quién?</b>%s</span><span><b>¿Qué pasa?</b>%s</span></div>
    <p style="margin-left:12.5mm;font-size:9.6pt">Palabras clave: %s</p>
    <p><b>2 · Escucha global.</b> %s</p>
    <div style="margin-left:12.5mm">☐ %s</div>
    <p><b>3 · Escucha con detalle.</b> Luister opnieuw en noteer.</p>
    <div style="margin-left:12.5mm;font-size:9.6pt">%s</div>
    <p><b>4 · Verdadero o falso — con prueba.</b> Kruis aan én schrijf wat je hoort.</p>
    <div style="margin-left:12.5mm;font-size:9.6pt">%s</div>
    <p><b>5 · La transcripción</b> staat online, en pas <i>ná</i> de taken. <span class="gloss">Eerst luisteren, dan pas meelezen — anders lees je in plaats van te luisteren.</span></p>
    <p><b>6 · Tu reacción.</b> %s</p>
    <div class="wbox lg"></div>
    <span class="steun">Apoyo: situatie vooraf → geen steun bij de details · scan de QR om te luisteren</span>
    %s</div>""" % (
        _acthead(num, "Escucha · %s" % f["titulo"],
                 [("👂 Escuchar", True), ("✍️ Escribir", True), ("👤 Solo", False), ("± 20 min", False), ("★★☆", False)]),
        f["situacion"]["lugar"], f["situacion"]["quien"], f["situacion"]["que"], claves,
        f["global"]["q"],
        " &nbsp;&nbsp; ☐ ".join(f["global"]["opts"]),
        det, vf,
        f["produccion"]["prompt"],
        qr_html if qr_html is not None else puntero("Escuchar 🎧", "het fragment beluisteren en het transcript"))
