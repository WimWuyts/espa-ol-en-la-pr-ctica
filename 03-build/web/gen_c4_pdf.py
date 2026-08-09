#!/usr/bin/env python3
"""De gedrukte unit voor U11–U14 — HTML als bron, Chromium maakt er de PDF van.

Eén generator voor vier units, gevoed uit dezelfde gegevens als de digitale
pagina (`kit_data.py`, `escena_data.py`, `comprension_data.py`,
`funciones_data.py`). Dat is de enige manier om te garanderen dat papier en
scherm hetzelfde zeggen: bij vier losse generatoren lopen ze binnen één
correctieronde uiteen.

DE BLADSPIEGEL VAN C4 (CLAUDE.md §3)
Elke sectie opent een nieuwe bladzijde én is verrijkt tot ze die bladzijde vult.
Dat is bewust anders dan C5/C6+, waar de secties doorvloeien — en de meting
geeft het gelijk: C4 haalt 88 tot 94 % vulling zonder halflege bladzijden.
Daarom wordt het gedeelde @bladspiegel-blok hier uit de kit geknipt, precies
zoals in `gen_c4uN_pdf.py`.

ANTWOORDRUIMTE (§14)
Elke oefening krijgt schrijfruimte van het juiste type: `.wl` voor een woord of
een zin, `.wbox` voor vrije productie, `.wcols` om te sorteren, `.wtab` voor een
tabel. Nooit oplossingen op de leerlingbladzijde — die staan online.

    C4_UNIT=11 python3 gen_c4_pdf.py
"""
import base64
import html
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)

import comprension_print                    # noqa: E402
import enlaces as EN                        # noqa: E402
import escena_data as ED                    # noqa: E402
import funciones_print                      # noqa: E402
import kit_data as KD                       # noqa: E402
from qr_codigo import qr_svg                # noqa: E402

UNIT = int(os.environ.get("C4_UNIT", "11"))
if UNIT not in KD.PORTADA:
    sys.exit("geen printgegevens voor unidad %d" % UNIT)


def b64(p):
    return base64.b64encode(open(p, "rb").read()).decode()


def face(f, p, w, fam=None):
    return ("@font-face{font-family:'%s';src:url(data:font/woff2;base64,%s) "
            "format('woff2');font-weight:%s;font-display:swap}"
            % (fam or f, b64("%s/02-huisstijl/fonts/%s" % (ROOT, p)), w))


FONTS = "".join([
    face("Bricolage Grotesque", "BricolageGrotesque-700.woff2", "700"),
    face("Bricolage Grotesque", "BricolageGrotesque-800.woff2", "800"),
    face("Bricolage Grotesque XBold", "BricolageGrotesque-800.woff2", "800",
         "Bricolage Grotesque XBold"),
    face("Inter", "Inter-400.woff2", "400"),
    face("Inter", "Inter-600.woff2", "600"),
    face("Caveat", "Caveat-700.woff2", "700")])

PRINTCSS = open("%s/02-huisstijl/templates/cursus-print.css" % ROOT, encoding="utf-8").read()
# Zie de kop: het gedeelde bladspiegel-blok is voor C5/C6+ geschreven, waar
# `.sec` het kopblok is. In C4 is `.sec` de hele bladzijde en levert het een
# blanco blad op.
PRINTCSS = re.sub(r"/\* @bladspiegel:ini.*?@bladspiegel:fin \*/", "", PRINTCSS, flags=re.S)

# de eigen kit van C4, uit de golden sample U1 — één bron voor alle C4-units
CSS_C4 = open(os.path.join(AQUI, "c4_print.css"), encoding="utf-8").read()

# BLADSPIEGEL — waarom deze vier units afwijken van U1–U10
# ------------------------------------------------------------------
# C4's regel is: elke sectie opent een blad én is verrijkt tot ze het vult
# (CLAUDE.md §3). Dat werkt in U1–U10 omdat die secties met de hand op maat
# gemaakt zijn. U11–U14 worden gegenereerd uit gegevens van wisselende lengte —
# de ene scène heeft dertien regels, de andere zeventien — en dan is «precies
# één blad» niet te halen: gemeten kwam het uit op 64 tot 79 % vulling met
# secties die net over de rand liepen.
#
# Daarom vloeit hier álles behalve de scène, die na de opener op een schoon
# blad hoort te beginnen. Elke extra gedwongen breuk kostte gemeten een halve
# bladzijde: met een eigen blad voor de eindtaak én het repaso bleef de unit op
# 81–83 % steken, met alleen de scène op ruim 90 %. De secties blijven
# herkenbaar aan hun bovenmarge en hun gekleurde sectielabel.
FLUJO = """
.sec{ break-before:auto; margin-top:9mm; }
.sec.major{ break-before:page; margin-top:0; }
.sec:first-of-type{ margin-top:0; }
p,li,td{ orphans:3; widows:3; }
.truc,.call,.qr,.audiorow,.obj,.guide,.maq,.wcols,.wbox{ break-inside:avoid; }
table{ break-inside:auto; }
thead{ display:table-header-group; }
.se{ break-after:avoid; }
"""

HUB = EN.url("C4", UNIT)


def qr(destino):
    """Een echte QR-code, met onze eigen encoder (PyPI is hier geblokkeerd)."""
    return qr_svg(destino, mm=26, nivel="Q", color="#A8323B")


def esc(s):
    return html.escape(s, quote=True)


def wl(cls=""):
    return '<span class="wl %s"></span>' % cls


# ─── de opener ──────────────────────────────────────────────────────────────
def hero():
    nr, tit, sub_nl, sub_es, cita, cando, guia, cogn = KD.PORTADA[UNIT]
    lis = "".join(
        '<li><span class="ck">✓</span> <span><span class="es">%s</span> '
        '<span class="nl">— %s</span></span></li>' % (es, esc(nl))
        for es, nl in cando)
    chips = "".join("<span>%s</span>" % esc(c) for c in cogn)
    return """
<section class="hero">
  <div class="tab">C4 · LA RUTA</div>
  <div class="eyebrow">EL DESPEGUE · PARADA %(nr)d · SURVIVAL IN SPANISH</div>
  <h1>%(tit)s</h1>
  <div class="sub">%(subnl)s <span class="gloss">%(subes)s</span></div>
  <div class="q">%(cita)s</div>
</section>
<div class="page">
  <div class="obj"><div class="se">Al final de esta unidad · Op het einde van deze les</div>
    <ul>%(lis)s</ul>
  </div>
  <div class="guide"><span class="ic">🎒</span><div>
    <span class="hand">¡Seguimos la ruta! Parada %(nr)d.</span>
    <div class="g">%(guia)s</div></div></div>
  <div class="truc" style="margin-top:4mm"><b>¿Qué reconoces ya?</b>
    Deze woorden lijken op het Nederlands, Frans of Engels — je begrijpt ze al
    vóór je ze leert <i>(palabras transparentes)</i>:
    <div class="cogn">%(chips)s</div>
    <span style="font-size:8.6pt;color:var(--mut)">Onderstreep er drie die je
    meteen herkent, en schrijf er één zin mee: %(wl)s</span>
  </div>
</div>""" % {"nr": nr, "tit": esc(tit), "subnl": esc(sub_nl), "subes": esc(sub_es),
              "cita": esc(cita), "lis": lis, "guia": esc(guia), "chips": chips,
              "wl": wl("full")}


# ─── §1 · de scène ──────────────────────────────────────────────────────────
def escucha():
    e = ED.ESCENAS[UNIT]
    destino = EN.url("C4", UNIT, EN.ancla_c4("escucha"))
    # De hele scène op papier, niet alleen het begin: de leerling moet kunnen
    # meelezen bij álles wat hij hoort, en de bladzijde moet vol (CLAUDE.md §3).
    lineas = ""
    for t, i, ls in e["escenas"]:
        lineas += '<div class="se" style="margin-top:4mm">%s</div>' % esc(t)
        lineas += '<p style="font-size:9pt;color:var(--mut);margin:0 0 1mm">%s</p>' % esc(i)
        lineas += "".join(
            '<div class="tl"><span class="sp">%s</span><span class="tx">%s</span></div>'
            % (esc(sp), esc(es)) for sp, es, _nl in ls)
    chunks = "".join("<span>%s</span>" % esc(c.replace("_", " "))
                     for c in e["chunks"][:8])
    preguntas = "".join(
        '<div style="margin:2.4mm 0"><b>%d.</b> %s %s</div>' % (i + 1, q, wl("md"))
        for i, q in enumerate(PREGUNTAS_ESCENA[UNIT]))
    return """
<div class="page sec major">
  <div class="se">§1 · ¡Escucha!</div><h2>%(tit)s</h2>
  <div class="audiorow">
    <div class="call"><span class="ic">%(icono)s</span><div><b>%(tit)s</b> —
      %(consigna)s <b>Eerst zonder mee te lezen</b>: je hoeft niet alles te
      verstaan. Daarna lees je mee.</div></div>
    <div class="qr" data-url="%(url)s"><div class="lab">%(lab)s</div>%(qr)s
      <div class="meta">hub · Escucha</div></div>
  </div>
  <div class="se" style="margin-top:4mm">Antes de escuchar · voorspel</div>
  <p style="font-size:9.6pt">Kijk naar de titel en de chunks hieronder. Waarover
    gaat deze scène, denk je? Schrijf één zin in het Nederlands.</p>
  <div style="margin-left:6mm">%(wl)s</div>
  %(lineas)s
  <div class="truc" style="margin-top:3mm"><b>Chunks om mee te nemen</b> — hele
    stukken die je als één woord onthoudt:
    <div class="cogn">%(chunks)s</div></div>
  <div class="se" style="margin-top:4mm">Escucha con detalle · beantwoord in het Spaans</div>
  <div style="margin-left:6mm;font-size:9.6pt">%(preg)s</div>
  <div class="se" style="margin-top:4mm">Caza de chunks · zoek en onderstreep</div>
  <p style="font-size:9.6pt">Zoek elke chunk hierboven terug in de tekst en
    onderstreep hem. Schrijf er dan de Nederlandse betekenis bij.</p>
  <table class="mp"><thead><tr><th>Chunk</th><th>¿Qué significa?</th></tr></thead>
    <tbody>%(caza)s</tbody></table>
  <div class="truc" style="margin-top:3mm"><b>Nog eens luisteren?</b> Op de
    digitale pagina kan je elke regel apart aanklikken, het Nederlands aanzetten
    en de tekst verbergen om te toetsen of je het écht hoort.</div>
</div>""" % {"tit": esc(e["titulo"]), "url": destino, "qr": qr(destino),
              "lineas": lineas, "chunks": chunks, "preg": preguntas,
              "wl": wl("full"),
              "icono": "🎬" if UNIT in ED.VIDEO else "🎧",
              "lab": "Vídeo online" if UNIT in ED.VIDEO else "Escucha online",
              "consigna": ("scan de code en bekijk de aflevering op de digitale pagina."
                           if UNIT in ED.VIDEO else
                           "scan de code en luister de scène op de digitale pagina."),
              "caza": "".join("<tr><td>%s</td><td>%s</td></tr>"
                              % (esc(c.replace("_", " ")), wl("md"))
                              for c in e["chunks"][:6])}


# De begripsvragen bij de scène. Ze staan hier en niet in `escena_data.py`
# omdat ze bij de práct van het bóek horen: online worden dezelfde feiten
# anders bevraagd (met zelfcorrectie), en die twee hoeven niet identiek te zijn.
PREGUNTAS_ESCENA = {
 11: ["¿Adónde va ella de vacaciones?", "¿Qué tiempo hace siempre en Canarias?",
      "¿Adónde va Julio de vacaciones?", "¿Qué le gusta hacer al camarero en el Caribe?",
      "¿Cuántas veces por semana va la clienta al gimnasio?"],
 12: ["¿De qué color es la chaqueta de Paul?",
      "¿Qué lleva Julio: un jersey o una camisa? ¿De qué color?",
      "¿Quién lleva corbata, Paul o Julio?",
      "¿Qué zapatos lleva Julio?",
      "¿Qué verbo reflexivo dice la alumna?"],
 13: ["¿Por qué no va Julio a la academia?",
      "¿Qué tres cosas hay en la cesta de Julio?",
      "¿Cuánto cuestan los tomates?",
      "¿Qué tiene que comprar María en la carnicería?",
      "¿Dónde venden pescado fresco?"],
 14: ["¿Cuánto tiempo llevan juntos Julio y María?",
      "¿Quién elige la mesa?",
      "¿Qué bebe Julio? ¿Y sus padres?",
      "¿Qué recomienda el camarero de carne y de pescado?",
      "¿Qué postre piden al final?"],
}


# ─── Suena bien ─────────────────────────────────────────────────────────────
def suena():
    tit, expl, palabras, (atit, aexpl, acentos) = KD.SUENA[UNIT]
    chips = "".join("<span>%s</span>" % esc(p.replace("_", " ")) for p in palabras)
    filas = "".join(
        "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (esc(w), esc(d), wl("sm"))
        for w, d in acentos)
    return """
<div class="page sec">
  <div class="se">Suena bien · pronunciación</div><h2>%(tit)s</h2>
  <p style="font-size:9.6pt">%(expl)s</p>
  <div class="truc"><b>Escucha y repite.</b> Zeg elk woord drie keer hardop.
    Op de digitale pagina hoor je ze; hier vink je af wat al lukt.
    <div class="cogn">%(chips)s</div></div>
  <div class="se" style="margin-top:5mm">%(atit)s</div>
  <p style="font-size:9.6pt">%(aexpl)s</p>
  <table class="mp"><thead><tr><th>Palabra</th><th>¿Dónde está el acento?</th>
    <th>Klap mee ✓</th></tr></thead><tbody>%(filas)s</tbody></table>
  <div class="se" style="margin-top:5mm">Dictado corto · schrijf wat je hoort</div>
  <p style="font-size:9.6pt">Je leerkracht (of de digitale pagina) leest zes
    woorden voor. Schrijf ze op, mét accent waar het hoort.</p>
  <div style="margin-left:6mm;font-size:9.6pt">
    <div style="margin:2.4mm 0">1. %(l)s &nbsp; 2. %(l)s &nbsp; 3. %(l)s</div>
    <div style="margin:2.4mm 0">4. %(l)s &nbsp; 5. %(l)s &nbsp; 6. %(l)s</div>
  </div>
  <div class="se" style="margin-top:5mm">Tu turno · lees hardop voor</div>
  <p style="font-size:9.6pt">Kies drie zinnen uit de scène en lees ze voor aan je
    buur. Je buur luistert naar déze klank en zet een ✓ of een ✗.</p>
  <table class="mp"><thead><tr><th>Frase</th><th>La pronunciación ✓/✗</th></tr></thead>
    <tbody><tr><td>%(lf)s</td><td>%(ls)s</td></tr>
    <tr><td>%(lf)s</td><td>%(ls)s</td></tr>
    <tr><td>%(lf)s</td><td>%(ls)s</td></tr></tbody></table>
</div>""" % {"tit": tit, "expl": esc(expl), "chips": chips, "atit": esc(atit),
              "aexpl": esc(aexpl), "filas": filas,
              "l": wl("md"), "lf": wl("full"), "ls": wl("sm")}


# ─── gramática ──────────────────────────────────────────────────────────────
def gramatica():
    tit, sub, filas, trampa = KD.GRAMATICA[UNIT]
    cuerpo = "".join(
        '<div class="maq"><div class="m1">%s<small>%s</small></div>'
        '<div class="m2">%s</div><div class="m3">%s</div></div>'
        % (forma, esc(es), esc(nl), wl("md"))
        for forma, es, nl in filas)
    ejercicio = "".join(
        '<div style="margin:2.4mm 0"><b>%d.</b> %s %s</div>' % (i + 1, f, wl("lg"))
        for i, f in enumerate(CLOZE[UNIT]))
    return """
<div class="page sec">
  <div class="se">§2 · Gramática en la práctica</div><h2>%(tit)s · %(sub)s</h2>
  <p style="font-size:9.6pt">Kijk eerst naar de voorbeelden. Wat verandert er, en
    waarmee verandert het mee? Schrijf je eigen voorbeeld in de rechterkolom.</p>
  %(cuerpo)s
  <div class="truc" style="margin-top:4mm"><b>¡Ojo!</b> %(trampa)s</div>
  <div class="se" style="margin-top:5mm">Completa · vul de juiste vorm in</div>
  <p style="font-size:9.6pt">Vul aan. De oplossingen staan op de digitale pagina,
    niet hier — eerst zelf proberen.</p>
  <div style="margin-left:6mm;font-size:9.6pt">%(ej)s</div>
  <div class="se" style="margin-top:5mm">Sustituye · vervang alleen wat gemarkeerd is</div>
  <p style="font-size:9.6pt">Herschrijf de modelzin telkens met het nieuwe woord.
    Alles wat mee moet veranderen, verandert mee.</p>
  <table class="mp"><thead><tr><th>Modelo</th><th>Cambia a…</th><th>Mi frase</th>
    </tr></thead><tbody>%(sust)s</tbody></table>
  <div class="se" style="margin-top:5mm">Y ahora tú · schrijf drie eigen zinnen</div>
  <p style="font-size:9.6pt">Gebruik het patroon van deze bladzijde. Onderstreep
    telkens het woord dat het patroon draagt.</p>
  <div class="wbox"></div>
</div>""" % {"tit": esc(tit), "sub": esc(sub), "cuerpo": cuerpo,
              "trampa": trampa, "ej": ejercicio,
              "sust": "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>"
                              % (esc(m), esc(c), wl("full"))
                              for m, c in SUSTITUCION[UNIT])}


# De substitutieketen: één modelzin, telkens één ding anders. Klassiek, en het
# werkt — de leerling ziet wat er mee verandert zonder dat het uitgelegd wordt.
SUSTITUCION = {
 11: [("A mí me gusta la playa.", "→ a ti"),
      ("A mí me gusta la playa.", "→ a él"),
      ("Me gusta el cine.", "→ me encanta"),
      ("Voy a la playa en avión.", "→ a la montaña, en tren")],
 12: [("Yo me ducho por la mañana.", "→ tú"),
      ("Yo me ducho por la mañana.", "→ él"),
      ("Yo me ducho por la mañana.", "→ vosotros"),
      ("Paul lleva una chaqueta negra.", "→ una camiseta blanca"),
      ("Paul es alto.", "→ está cansado (ser of estar?)")],
 13: [("¿Cuánto cuesta la lechuga?", "→ los tomates"),
      ("Las manzanas son baratas.", "→ caras"),
      ("Yo puedo ir al mercado.", "→ tú"),
      ("No voy porque estoy enfermo.", "→ por eso (herschrijf de hele zin)")],
 14: [("Yo quiero agua.", "→ una cerveza"),
      ("Yo quiero vino.", "→ yo tampoco (maak er een ontkenning van)"),
      ("La paella está buena.", "→ buenísima"),
      ("Ésa es la mesa que nos gusta.", "→ el restaurante")],
}


# De klassieke cloze-oefening die elke unit moet hebben (§14bis). Met opzet
# gewone invulzinnen naast de visuele uitleg hierboven: de leerling heeft
# allebei nodig.
CLOZE = {
 11: ["A mí ____ gusta la playa. (me/te)",
      "¿A ti ____ gusta el yoga? (me/te)",
      "A Julio ____ gusta el submarinismo. (le/te)",
      "En Canarias ____ buen tiempo. (hace/tengo)",
      "Cierra la ventana: ____ frío. (hace/tengo — het weer)",
      "Ponme un abrigo: ____ frío. (hace/tengo — ík)"],
 12: ["Yo ____ ducho a las siete. (me/te)",
      "¿Tú ____ peinas antes de salir? (me/te)",
      "Paul ____ afeita todos los días. (se/te)",
      "Vosotros ____ ducháis después del deporte. (os/se)",
      "Paul ____ una chaqueta negra. (lleva/tiene — wat hij nú aanheeft)",
      "Yo no ____ corbatas. (llevo/tengo — bezit)",
      "Paul ____ alto y guapo. (es/está)",
      "Hoy Julio ____ cansado. (es/está)"],
 13: ["¿Cuánto ____ los tomates? (cuesta/cuestan)",
      "¿Cuánto ____ un kilo de manzanas? (cuesta/cuestan)",
      "¿____ pagar con tarjeta? (Puedo/Puedes — ik)",
      "Nosotros ____ ir al mercado el sábado. (podemos/puedo)",
      "¿____ no comes carne? (Por qué/Porque)",
      "No como carne ____ soy vegetariano. (por qué/porque)",
      "Estoy enfermo, ____ no voy a la academia. (por eso/porque)"],
 14: ["Ésa es la mesa ____ nos gusta. (que/qué)",
      "Somos cuatro personas ____ van a cenar. (que/qué)",
      "¿Quiere agua ____ vino? (o/y)",
      "Yo quiero cerveza. — Yo ____. (también/tampoco — ik ook)",
      "Yo no quiero vino. — Yo ____. (también/tampoco — ik ook niet)",
      "La sopa está buena → está buen____. (-ísima/-ísimo)",
      "Mis padres son simpáticos → son simpatiqu____. (-ísimos/-ísimas)"],
}


# ─── práctica ───────────────────────────────────────────────────────────────
def practica():
    clusters = KD.CLUSTERS[UNIT]
    cols = "".join(
        '<div class="wcol"><div class="ch">%s</div><div class="cb"></div></div>'
        % esc(n) for n, _s, _i, _it in clusters)
    palabras = [es for _n, _s, _i, items in clusters for es, _nl in items]
    banco = " · ".join(esc(p) for p in palabras[:14])
    tabla = "".join(
        "<tr><td>%s</td><td>%s</td></tr>" % (esc(es), wl("md"))
        for _n, _s, _i, items in clusters for es, _nl in items[:3])
    return """
<div class="page sec">
  <div class="se">§3 · Práctica</div><h2>Oefen op papier — online verbeter je alles</h2>
  <div class="se" style="margin-top:3mm">Clasifica · zet elk woord in het juiste veld</div>
  <p style="font-size:9.4pt"><b>Banco de palabras:</b> %(banco)s</p>
  <div class="wcols">%(cols)s</div>
  <div class="se" style="margin-top:5mm">Traduce · schrijf de betekenis</div>
  <table class="mp"><thead><tr><th>Español</th><th>Nederlands</th></tr></thead>
    <tbody>%(tabla)s</tbody></table>
</div>
<div class="page sec">
  <div class="se">§3 · Práctica · sigue</div><h2>Van gestuurd naar zelf zeggen</h2>
  <div class="se">Ordena · zet de woorden in de juiste volgorde</div>
  <div style="margin-left:6mm;font-size:9.6pt">%(ordena)s</div>
  <div class="se" style="margin-top:5mm">Pregunta y responde · in tweetallen</div>
  <p style="font-size:9.6pt">Stel elkaar de vier vragen. Noteer het antwoord van
    je buur in het Spaans — niet in het Nederlands.</p>
  <table class="mp"><thead><tr><th>Pregunta</th><th>La respuesta de mi compañero/a</th>
    </tr></thead><tbody>%(pares)s</tbody></table>
  <div class="se" style="margin-top:5mm">Corrige · zoek de fout en herschrijf</div>
  <p style="font-size:9.6pt">In elke zin staat één fout. Onderstreep hem en
    schrijf de zin correct over.</p>
  <div style="margin-left:6mm;font-size:9.6pt">%(corrige)s</div>
  <div class="se" style="margin-top:5mm">Escribe · vijf zinnen over jezelf</div>
  <p style="font-size:9.6pt">Gebruik minstens vier chunks uit deze unidad.
    Onderstreep ze.</p>
  <div class="wbox lg"></div>
</div>""" % {
        "banco": banco, "cols": cols, "tabla": tabla,
        "ordena": "".join(
            '<div style="margin:3mm 0"><b>%d.</b> %s<br>%s</div>'
            % (i + 1, esc(f), wl("full")) for i, f in enumerate(ORDENA[UNIT])),
        "pares": "".join("<tr><td>%s</td><td>%s</td></tr>" % (esc(q), wl("full"))
                         for q in PAREJAS[UNIT]),
        "corrige": "".join('<div style="margin:3mm 0"><b>%d.</b> %s<br>%s</div>'
                           % (i + 1, esc(f), wl("full"))
                           for i, f in enumerate(CORRIGE[UNIT]))}


# De klassieke foutenzoeker. De fouten zijn gekozen op wat een Nederlandstalige
# leerling écht doet: het verkeerde aanwijzend voornaamwoord, «es» waar «hace»
# hoort, «tú» tegen een receptionist, «luego» voor «dus».
CORRIGE = {
 11: ["Yo gusto la playa.", "A mí me gusta el frío, ¿y a tú?",
      "Estoy frío, cierra la ventana.", "Voy a la playa con avión."],
 12: ["Yo ducho a las siete.", "Paul tiene una chaqueta negra hoy.",
      "Paul está alto y guapo.", "Vosotros se peináis.",
      "Llevo un jersey verdes."],
 13: ["¿Cuánto costan los tomates?", "¿Por qué no vas? Por qué estoy enfermo.",
      "Las manzanas son barato.", "Compro pescado en la carnicería.",
      "Estoy enfermo, luego no voy a la academia."],
 14: ["Ésa es la mesa qué nos gusta.", "Yo no quiero vino. — Yo también.",
      "La paella está buenísima y el cordero está buenísima.",
      "Somos cuatro personas van a cenar.",
      "Mis padres son simpaticísimos."],
}


ORDENA = {
 11: ["tiempo / buen / hace / Canarias / en / siempre",
      "submarinismo / gusta / hacer / me",
      "ópera / voy / a / casi / la / nunca",
      "gimnasio / semana / al / veces / por / tres / voy"],
 12: ["negra / lleva / chaqueta / Paul / una",
      "ojos / los / tiene / azules / Paul",
      "peino / me / mañanas / las / por / me / ducho / y",
      "cambio / yo / zapatillas / en / llevo / viejas"],
 13: ["cuestan / ¿ / cuánto / tomates / los / ?",
      "enfermo / estoy / eso / no / por / voy",
      "fresco / ¿ / venden / dónde / pescado / ?",
      "carnicería / la / falta / nos / por / pasar"],
 14: ["cuatro / mesa / para / una / por / favor",
      "gusta / la / ésa / mesa / es / nos / que",
      "vino / quiero / tampoco / yo / no",
      "cordero / de / les / el / recomiendo / carne"],
}

PAREJAS = {
 11: ["¿Qué tiempo hace hoy aquí?", "¿Adónde vas de vacaciones? ¿Cómo vas?",
      "¿Qué te gusta hacer en vacaciones?",
      "¿Con qué frecuencia lo haces: siempre, a veces o casi nunca?"],
 12: ["¿Qué ropa llevas hoy? ¿De qué color?",
      "¿A qué hora te levantas y te duchas?",
      "¿Cómo es tu mejor amigo/a? (alto, guapo, simpático…)",
      "¿Qué ropa te queda bien y qué ropa no te gusta?"],
 13: ["¿Qué comes normalmente: carne, pescado o verdura?",
      "¿Dónde compra tu familia: en el mercado o en el supermercado?",
      "¿Cuánto cuesta un kilo de manzanas aquí?",
      "¿Qué no compras nunca? ¿Por qué?"],
 14: ["¿Cuál es tu plato favorito? ¿Y tu bebida?",
      "¿Vas mucho al restaurante? ¿Con quién?",
      "Yo prefiero algo dulce de postre. ¿Y tú? (yo también / yo no)",
      "¿Qué plato español o latinoamericano quieres probar? ¿Por qué?"],
}


# ─── tarea final ────────────────────────────────────────────────────────────
def tarea():
    tit, ses, snl, pasos = KD.TAREA[UNIT]
    lis = "".join('<li>%s</li>' % p for p in pasos)
    destino = EN.url("C4", UNIT, EN.ancla_c4("practica"))
    return """
<div class="page sec">
  <div class="se">§4 · Tarea final</div><h2>%(tit)s</h2>
  <p style="font-size:10pt"><b>%(ses)s</b> <span class="gloss">%(snl)s</span></p>
  <ol style="font-size:9.8pt">%(lis)s</ol>
  <div class="se" style="margin-top:4mm">Mi preparación · schrijf hier je tekst</div>
  <div class="wbox lg"></div>
  <div class="audiorow" style="margin-top:4mm">
    <div class="call"><span class="ic">🎙️</span><div><b>Grábate.</b> Neem je taak
      op via de digitale pagina en luister terug: versta jíj jezelf? Neem daarna
      nog een keer op — de tweede keer is altijd beter.</div></div>
    <div class="qr" data-url="%(url)s"><div class="lab">Graba tu tarea</div>%(qr)s
      <div class="meta">hub · Práctica</div></div>
  </div>
  <div class="se" style="margin-top:4mm">Evaluación · kruis eerlijk aan</div>
  <table class="mp"><thead><tr><th>Criterio</th><th>Todavía no</th><th>Casi</th>
    <th>¡Sí!</th></tr></thead><tbody>
    <tr><td>Ik gebruik de chunks van deze unidad</td><td>☐</td><td>☐</td><td>☐</td></tr>
    <tr><td>Men verstaat mij zonder dat ik het herhaal</td><td>☐</td><td>☐</td><td>☐</td></tr>
    <tr><td>Ik spreek de klank van deze unidad goed uit</td><td>☐</td><td>☐</td><td>☐</td></tr>
    <tr><td>Ik durf te antwoorden zonder mijn blad</td><td>☐</td><td>☐</td><td>☐</td></tr>
  </tbody></table>
</div>""" % {"tit": esc(tit), "ses": esc(ses), "snl": esc(snl), "lis": lis,
              "url": destino, "qr": qr(destino)}


# ─── cultura ────────────────────────────────────────────────────────────────
CULTURA = {
 11: ("España en verano", "Waarom half Madrid in augustus verdwijnt",
      "In augustus loopt Madrid leeg: wie kan, vertrekt naar de <b>costa</b> of naar "
      "<b>el pueblo</b> — het dorp waar de familie vandaan komt. Julio doet precies "
      "dat. Het binnenland kent extremen: 40 graden in de zomer, en in de bergen bij "
      "Ávila vriest het 's winters hard. Op de <b>Canarias</b>, voor de kust van "
      "Afrika, is het het hele jaar door 20 tot 26 graden — daarom heten ze "
      "<i>las islas de la eterna primavera</i>.",
      ["Wat betekent <i>ir al pueblo</i>, en heb jij zoiets?",
       "Zoek de temperatuur van vandaag in Madrid en in Las Palmas.",
       "Waarom is het op de Canarias het hele jaar zacht? Zoek het op."]),
 12: ("La ropa que cuenta algo", "Van de guayabera tot de sneakers van Madrid",
      "Kleding is nooit alleen kleding. In het Caribisch gebied draagt men de "
      "<b>guayabera</b>, een licht overhemd met plooien dat je zelfs op een "
      "trouwfeest mag aanhebben; in de Andes de <b>poncho</b>, geweven in de "
      "kleuren van de streek; in Guatemala de <b>huipil</b>, waarvan het "
      "borduurwerk verraadt uit welk dorp je komt. En in Madrid? Daar dragen "
      "tieners ongeveer hetzelfde als jij. Eén detail is wel anders: "
      "<i>llevar</i> is «aanhebben», terwijl wij «dragen» zeggen — en dat woord "
      "betekent in het Spaans iets heel anders.",
      ["Zoek een foto van een <i>guayabera</i> en van een <i>huipil</i>. Beschrijf "
       "er één in het Spaans: <i>Lleva…</i>",
       "Welke kleuren zie je het meest in de traditionele kleding van de Andes?",
       "Wat draag jij vandaag? Schrijf drie zinnen met <i>llevo</i> + kleur."]),
 13: ("El mercado de barrio", "Waarom de Spanjaard nog altijd bij vier winkels langsgaat",
      "In Spanje en Latijns-Amerika is <b>el mercado</b> geen folklore maar een "
      "gewone maandagochtend. Onder één dak staan losse kraampjes: de "
      "<b>pescadería</b> voor vis, de <b>carnicería</b> voor vlees, de "
      "<b>frutería</b> voor groenten en fruit. Je koopt er per stuk of per kilo, "
      "je vraagt de prijs hardop, en de verkoper kent je naam. In Mexico heet "
      "zo'n rondtrekkende markt een <i>tianguis</i>, een woord uit het Nahuatl — "
      "ouder dus dan het Spaans zelf.",
      ["Zoek een Spaanse marktfolder en noteer drie prijzen per kilo.",
       "Wat is een <i>tianguis</i>? Uit welke taal komt het woord?",
       "Waar koopt jouw gezin: markt, winkel of online? Schrijf één zin met "
       "<i>compramos… porque…</i>"]),
 14: ("La mesa española", "Twee uur aan tafel, en niemand die haast heeft",
      "Wie in Spanje uit eten gaat, eet later en langer. De <b>comida</b> is "
      "tussen twee en vier, de <b>cena</b> begint pas om negen of tien. "
      "'s Middags bestaat het <b>menú del día</b>: voorgerecht, hoofdgerecht, "
      "nagerecht, brood en drank voor één prijs — het goedkoopste warme eten van "
      "het land. Na het nagerecht komt de koffie, en die blijft staan: de "
      "<i>sobremesa</i>, het napraten aan tafel, hoort bij de maaltijd. De "
      "rekening vraag je zelf; ze wordt niet gebracht.",
      ["Zoek een echt <i>menú del día</i> online. Wat kost het en wat krijg je?",
       "Wat is <i>la sobremesa</i>? Bestaat daar een Nederlands woord voor?",
       "Stel jouw menú del día samen in het Spaans: primer plato, segundo, postre."]),
}


def cultura():
    tit, sub, texto, preguntas = CULTURA[UNIT]
    lis = "".join('<div style="margin:3mm 0"><b>%d.</b> %s<br>%s</div>'
                  % (i + 1, p, wl("full")) for i, p in enumerate(preguntas))
    destino = EN.url("C4", UNIT, EN.ancla_c4("musica"))
    return """
<div class="page sec">
  <div class="se">Cultura · Banda sonora</div><h2>%(tit)s</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 2mm">%(sub)s</p>
  <p style="font-size:9.8pt">%(texto)s</p>
  <div class="se" style="margin-top:5mm">Investiga · zoek het op en schrijf</div>
  <div style="margin-left:6mm;font-size:9.6pt">%(lis)s</div>
  <div class="audiorow" style="margin-top:4mm">
    <div class="call"><span class="ic">🎵</span><div><b>La banda sonora.</b>
      Op de digitale pagina staat de playlist bij deze unidad. Kies één nummer,
      luister het twee keer en noteer drie woorden die je herkent.</div></div>
    <div class="qr" data-url="%(url)s"><div class="lab">Escucha la playlist</div>%(qr)s
      <div class="meta">hub · Música</div></div>
  </div>
  <div style="margin-left:6mm;font-size:9.6pt;margin-top:2mm">
    Mis tres palabras: %(l)s &nbsp; %(l)s &nbsp; %(l)s</div>
</div>""" % {"tit": esc(tit), "sub": esc(sub), "texto": texto, "lis": lis,
              "url": destino, "qr": qr(destino), "l": wl("md")}


# ─── repaso ─────────────────────────────────────────────────────────────────
def repaso():
    clusters = KD.CLUSTERS[UNIT]
    esencial = "".join(
        '<div class="cuadro"><b>%s</b><div>%s</div></div>'
        % (esc(n), " · ".join(esc(es) for es, _ in items[:4]))
        for n, _s, _i, items in clusters)
    nr, tit, _snl, _ses, _c, cando, _g, _cg = KD.PORTADA[UNIT]
    sem = "".join(
        "<tr><td>%s</td><td>🔴</td><td>🟡</td><td>🟢</td></tr>"
        % re.sub(r"<[^>]+>", "", es) for es, _nl in cando)
    destino = EN.url("C4", UNIT, EN.ancla_c4("practica"))
    return """
<div class="page sec">
  <div class="se">Repaso · Lo esencial de un vistazo</div><h2>Wat je nu kunt</h2>
  <div class="kitwrap">%(esencial)s</div>
  <div class="se" style="margin-top:5mm">El semáforo · hoe zeker ben je?</div>
  <p style="font-size:9.6pt">Kleur eerlijk in. Alles wat rood of oranje is, oefen
    je online — daar verbetert het zichzelf.</p>
  <table class="mp"><thead><tr><th>Puedo…</th><th>nog niet</th><th>bijna</th>
    <th>ja</th></tr></thead><tbody>%(sem)s</tbody></table>
  <div class="audiorow" style="margin-top:4mm">
    <div class="call"><span class="ic">🎮</span><div><b>Repasa jugando.</b>
      De digitale pagina heeft zeven zelfcorrigerende oefeningen bij deze unidad,
      van herkennen tot zelf opnemen. Begin bij wat oranje of rood is.</div></div>
    <div class="qr" data-url="%(url)s"><div class="lab">Repasa online</div>%(qr)s
      <div class="meta">hub · Práctica</div></div>
  </div>
  <div class="se" style="margin-top:5mm">Mis palabras · jouw eigen vijf</div>
  <p style="font-size:9.6pt">Welke vijf woorden of chunks uit deze unidad wil jíj
    zeker onthouden? Schrijf ze op met een voorbeeldzin.</p>
  <table class="mp"><thead><tr><th>Mi palabra</th><th>Mi frase</th></tr></thead>
    <tbody>%(mis)s</tbody></table>
</div>""" % {"esencial": esencial, "sem": sem, "url": destino, "qr": qr(destino),
              "mis": "".join("<tr><td>%s</td><td>%s</td></tr>" % (wl("md"), wl("full"))
                             for _ in range(5))}


# ─── het slot van het jaar (alleen de laatste unidad) ───────────────────────
# De veertien parada's met per parada één can-do. Ze staan hier uitgeschreven en
# worden niet uit de units getrokken: U1–U10 hebben elk hun eigen generator, en
# een terugblik die van tien andere bestanden afhangt breekt bij de eerste
# hernoeming. Dit is één bladzijde die één keer bestaat.
EL_AÑO = [
 (1, "Presentaciones", "Me llamo… · ¿Cómo te llamas?"),
 (2, "Saludos", "Buenos días · ¿Qué tal? · Hasta luego"),
 (3, "Nacionalidades y países", "Soy de… · ¿De dónde eres?"),
 (4, "La familia", "Esta es mi madre · es alto y simpático"),
 (5, "Objetos cotidianos", "¿Qué es esto? · sirve para…"),
 (6, "La casa y los lugares", "¿Dónde está? · encima de · al lado de"),
 (7, "Las profesiones", "¿A qué te dedicas? · soy profesor"),
 (8, "La hora y los días", "¿Qué hora es? · ¿Quieres quedar?"),
 (9, "Planes y obligaciones", "Voy a… · tengo que…"),
 (10, "Las tareas de casa", "Yo te ayudo · sé cocinar"),
 (11, "El tiempo y las vacaciones", "Hace sol · me gusta · casi nunca"),
 (12, "La ropa y los colores", "Lleva una chaqueta negra · me ducho"),
 (13, "En el mercado", "¿Cuánto cuestan? · porque · por eso"),
 (14, "En el restaurante", "Yo quiero… · yo también · buenísimo"),
]


def cierre():
    """De slotbladzijde van het jaar. Alleen de laatste unidad heeft ze."""
    if UNIT != max(KD.PORTADA):
        return ""
    filas = "".join(
        "<tr><td><b>%d</b></td><td>%s</td><td>%s</td>"
        "<td>🔴</td><td>🟡</td><td>🟢</td></tr>" % (n, esc(t), esc(c))
        for n, t, c in EL_AÑO)
    return """
<div class="sec">
  <div class="se">¡Ya hablas español! · veertien parada's later</div>
  <p style="font-size:9.8pt"><b>Hace un año no sabías decir nada en español. Ahora
    puedes presentarte, describir tu casa, quedar con alguien, comprar en el
    mercado y pedir una cena entera.</b>
    <span class="gloss">Een jaar geleden kon je hier nog niets zeggen. Nu stel je
    jezelf voor, beschrijf je je huis, maak je een afspraak, doe je boodschappen
    op de markt en bestel je een volledig menu.</span>
    Loop de veertien parada's na en kleur eerlijk in: wat rood of oranje blijft,
    staat online klaar om te herhalen.</p>
  <div class="truc"><b>¿Y ahora?</b> Dit was «¡Bienvenidos al español!». De
    klanken, het accent en de chunks die je hier opbouwde, zijn precies waarmee
    de volgende cursus vertrekt.
    <span class="gloss">Aquí termina el primer viaje; el siguiente empieza donde
    este acaba.</span></div>
  <table class="mp" style="margin-top:3mm"><thead><tr><th>#</th><th>Parada</th>
    <th>Ya sé decir…</th><th>nog niet</th><th>bijna</th><th>ja</th></tr></thead>
    <tbody>%(filas)s</tbody></table>
  <div style="margin-left:6mm;font-size:9.6pt;margin-top:3mm">
    <b>Mi frase del año</b> — de Spaanse zin die je nooit meer wil vergeten:
    %(l)s</div>
</div>"""  % {"filas": filas, "l": wl("full")}


# ─── het geheel ─────────────────────────────────────────────────────────────
def main():
    nr, tit = KD.PORTADA[UNIT][0], KD.PORTADA[UNIT][1]
    cuerpo = (hero() + escucha()
              + comprension_print.print_section(UNIT, HUB)
              + suena() + gramatica() + practica() + tarea() + cultura()
              + funciones_print.print_section(UNIT)
              + repaso() + cierre())
    # De gedeelde blokken (comprensión, funciones) zetten zelf een harde
    # paginabreuk: dat klopt in U1–U10, waar élke sectie een blad opent. Hier
    # vloeit alles behalve de vier mijlpalen, dus die inline breuk moet eruit —
    # anders krijgt een blok van een halve bladzijde er alsnog een hele.
    cuerpo = cuerpo.replace(' style="break-before:page"', '')
    doc = ("""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>C4 · Unidad %d · %s</title><style>%s</style></head><body class="c4">
%s
</body></html>""" % (nr, esc(tit), FONTS + PRINTCSS + CSS_C4 + FLUJO, cuerpo))
    ruta = os.path.join(AQUI, "print", "C4_U%d.html" % UNIT)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    open(ruta, "w", encoding="utf-8").write(doc)
    print("C4_U%d.html geschreven: %d bytes · %d secties"
          % (UNIT, len(doc), doc.count('class="page sec"')))


if __name__ == "__main__":
    main()
