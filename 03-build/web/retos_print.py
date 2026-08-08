#!/usr/bin/env python3
"""De retos op papier — HTML-blokken uit `retos_data.py`.

Twee soorten blokken:

  `reto_print(r)`      de volledige oefening, voor de retos met soporte="print".
                       Alles wat de leerling nodig heeft staat op papier:
                       materiaal, verloop, de beperking en type-correcte
                       schrijfruimte (CLAUDE.md §14).

  `reto_puntero(r)`    een kaartje van vier regels voor de retos die op de hub
                       of in de PowerPoint leven. Géén halve kopie: een veiling
                       naspelen op papier werkt niet, en een opnameoefening al
                       helemaal niet. Het kaartje zegt wát het is, wat de
                       beperking is en waar het staat — meer hoort er niet.

De extra CSS (`CSS`) hangt in dezelfde componentenkit als de rest: reto-kop met
lens-chip, beperkingskader, knipfiches, vouwlijn voor de info-gap.
"""

import html

E = lambda s: html.escape(s or "")

CSS = """
/* ── retos — de out-of-the-box oefeningen ────────────────────────────────── */
.reto{ border:.5pt solid var(--line2); border-radius:4mm; padding:4mm 5mm 4.5mm;
       margin:4mm 0 5mm; break-inside:avoid; background:#FFFDF9; }
.reto .rcab{ display:flex; gap:2.5mm; align-items:center; flex-wrap:wrap; margin-bottom:1.5mm; }
.reto .rnum{ background:var(--g); color:#fff; font-family:var(--dispx); font-size:11pt;
             width:8.5mm; height:8.5mm; border-radius:50%; display:flex; align-items:center;
             justify-content:center; flex:none; }
.reto .rlente{ font-size:7.6pt; font-weight:700; color:var(--gd); background:var(--gt);
               border-radius:999px; padding:.7mm 2.6mm; letter-spacing:.03em; }
.reto h3{ font-family:var(--disp); font-size:13pt; color:var(--ink); margin:0; }
.reto .rgancho{ font-size:10.4pt; margin:1.5mm 0 0; }
.reto .rgancho b{ color:var(--gd); }
.reto .rnl{ font-size:9pt; color:var(--mut); font-style:italic; margin:.6mm 0 2.5mm; }
.reto .rconsigna{ font-size:10pt; margin:0 0 2mm; }
.regla-reto{ border-left:2.6mm solid var(--amber); background:var(--amberbg);
             border-radius:0 3mm 3mm 0; padding:2.6mm 4mm; margin:2.5mm 0 3mm; font-size:9.6pt; }
.regla-reto b{ color:#8A6508; text-transform:uppercase; letter-spacing:.06em; font-size:8.4pt; }
.rpasos{ counter-reset:rp; margin:0 0 3mm; padding:0; list-style:none; }
.rpasos li{ counter-increment:rp; position:relative; padding-left:7.5mm; margin:1.6mm 0; font-size:9.8pt; }
.rpasos li::before{ content:counter(rp); position:absolute; left:0; top:.2mm; width:5mm; height:5mm;
                    border-radius:50%; background:var(--gt); color:var(--gd); font-weight:700;
                    font-size:8pt; display:flex; align-items:center; justify-content:center; }
.rpasos .pnl{ color:var(--mut); font-style:italic; font-size:8.6pt; display:block; }
/* het verwijskaartje voor retos die elders leven */
.rpunt{ display:flex; gap:3.5mm; align-items:flex-start; border:.5pt dashed var(--line2);
        border-radius:3.5mm; padding:3mm 4mm; margin:3mm 0; background:var(--crema);
        break-inside:avoid; }
.rpunt .ric{ font-size:15pt; flex:none; line-height:1; }
.rpunt h4{ font-family:var(--disp); font-size:11pt; margin:0 0 .8mm; color:var(--gd); }
.rpunt p{ margin:0; font-size:9.4pt; }
.rpunt .rdonde{ font-size:8.6pt; color:var(--mut); margin-top:1.2mm; }
/* materiaal: knipfiches en de vouwlijn van een info-gap */
.fichas{ display:grid; grid-template-columns:repeat(4,1fr); gap:2.5mm; margin:2.5mm 0 1mm; }
.ficha{ border:.5pt dashed var(--line2); border-radius:2.5mm; padding:3.5mm 2mm; text-align:center;
        font-family:var(--disp); font-size:10pt; color:var(--ink); background:#fff; }
.pliegue{ border-top:.7pt dashed var(--line2); margin:5mm 0 3mm; padding-top:1.5mm;
          font-size:8pt; color:var(--mut); letter-spacing:.08em; text-transform:uppercase; }
.rol{ background:var(--gt); border-radius:2.5mm; padding:1mm 3mm; font-family:var(--disp);
      font-size:9.6pt; color:var(--gd); display:inline-block; margin-bottom:2mm; }
.tira{ display:flex; flex-wrap:wrap; gap:1.4mm; margin:2mm 0 3mm; }
.tira span{ border:.4pt solid var(--line); border-radius:2mm; padding:1.2mm 2.4mm; font-size:8.8pt;
            background:#fff; }
.tira b{ color:var(--gd); }
/* fiches met meerdere regels, knipbaar */
.fichas.f3{ grid-template-columns:repeat(3,1fr); }
.fichas.f4{ grid-template-columns:repeat(4,1fr); }
.ficha.fid{ text-align:left; font-family:var(--body); font-size:8.6pt; line-height:1.3; padding:2.5mm 3mm; }
.ficha.fid b{ font-family:var(--disp); font-size:10.5pt; color:var(--gd); display:block; }
.ficha.fid span{ display:block; color:var(--mut); }
.ficha.fid .fl{ color:var(--ink); }
.ficha.tarjeta{ background:var(--gt); text-align:left; padding:2.5mm 3mm; }
.ficha.tarjeta .tk{ display:block; font-size:6.6pt; letter-spacing:.14em; color:var(--gd); }
.ficha.tarjeta b{ font-family:var(--dispx); font-size:13pt; display:block; }
.ficha.tarjeta span{ display:block; font-size:8.4pt; color:var(--mut); }
/* het rooster voor de staafgrafiek van het censo */
.grafico{ display:flex; gap:2mm; margin:1.5mm 0 0; }
.grafico .ejey{ display:flex; flex-direction:column; justify-content:space-between;
                font-size:7.4pt; color:var(--mut); height:38mm; padding-top:.5mm; }
.grafico .rejilla{ flex:1; height:38mm; border-left:.6pt solid var(--line2);
                   border-bottom:.6pt solid var(--line2);
                   background-image:linear-gradient(to right, var(--line) .3pt, transparent .3pt),
                                    linear-gradient(to bottom, var(--line) .3pt, transparent .3pt);
                   background-size:5mm 7.6mm; }
/* levens bij el error caro */
.vidas{ display:flex; align-items:center; gap:1.5mm; margin:3mm 0 0; font-size:9.4pt;
        color:var(--mut); flex-wrap:wrap; }
.vida{ color:var(--red); font-size:12pt; }
.wtab td.op{ font-size:8.8pt; color:var(--mut); }
.wtab td.fr{ font-size:9.8pt; }
.decl{ border-left:2mm solid var(--gt); padding:1.4mm 3mm; margin:1.6mm 0; }
.decl b{ color:var(--gd); font-family:var(--disp); font-size:10pt; }
.decl span{ display:block; font-size:9.6pt; }
.prohib{ background:#FEF2F2; border:.4pt solid var(--red); color:var(--red);
         border-radius:2mm; padding:1.2mm 2.6mm; font-size:9pt; font-weight:600; }
.barra{ display:inline-block; height:3.4mm; background:var(--g); border-radius:1mm; }
"""

_ICONO = {"hub": "🎮", "ppt": "📊", "print": "📄"}
_DONDE = {"hub": ("la página digital", "op de digitale pagina, tabblad «Retos»"),
          "ppt": ("la presentación de clase", "klassikaal, in de PowerPoint van deze unit"),
          "print": ("el libro", "in het boek")}


def _cabecera(r):
    return ('<div class="rcab"><span class="rnum">%d</span>'
            '<h3>%s</h3><span class="rlente">%s</span></div>'
            '<p class="rgancho"><b>%s</b></p><p class="rnl">%s</p>'
            % (r["num"], E(r["nombre"]), E(r["lente"]),
               E(r["gancho_es"]), E(r["gancho_nl"])))


def _badges(r):
    return ('<div class="badges"><span class="badge skill">%s</span>'
            '<span class="badge">%s</span><span class="badge">%s</span>'
            '<span class="badge">%s</span></div>'
            % (E(r["skill"]), E(r["forma"]), E(r["tiempo"]), E(r["dificultad"])))


def _pasos(r):
    return ('<ol class="rpasos">%s</ol>'
            % "".join('<li>%s<span class="pnl">%s</span></li>' % (E(es), E(nl))
                      for es, nl in r["pasos"]))


def _regla(r):
    return ('<div class="regla-reto"><b>La regla del reto</b><br>%s</div>' % E(r["regla"]))


def _lineas(n, klasse="wl full", start=1):
    return "".join('<div style="margin:2.6mm 0"><b>%d.</b> <span class="%s"></span></div>'
                   % (start + i, klasse) for i in range(n))


# ---------------------------------------------------------------------------
# De drie print-retos, elk met zijn eigen materiaal
# ---------------------------------------------------------------------------

def _gps(r):
    d = r["datos"]
    tira = "".join('<span><b>km %d</b> %s</span>' % (km, E(c)) for km, c in d["ciudades"])
    rutas = "".join(
        '<div style="margin:2.2mm 0;font-size:9.8pt"><b>Ruta %d.</b> '
        'Sal del kilómetro <b>%d</b>, ve <b>%d</b> kilómetros <b>%s</b>. '
        '¿A qué ciudad llegas?</div>' % (i, ini, mov, dirn)
        for i, (ini, mov, dirn, _fin, _c) in enumerate(d["rutas"], 1))
    return (
        '<div class="rol">🔊 Alumno A · el GPS que habla</div>'
        '<p style="font-size:9.6pt;margin:0 0 2mm">Lee cada ruta en voz alta. No enseñes '
        'esta parte. <span class="gloss">Lees elke route hardop voor. Laat dit deel niet zien.</span></p>'
        + rutas +
        '<div class="pliegue">✂ Doblar aquí · hier vouwen</div>'
        '<div class="rol">🗺️ Alumno B · el mapa mudo</div>'
        '<p style="font-size:9.6pt;margin:0 0 1mm">Esta es tu carretera. Escucha, calcula y '
        'escribe la ciudad. <span class="gloss">Dit is jouw weg. Luister, reken en schrijf de stad op.</span></p>'
        '<div class="tira">%s</div>%s' % (tira, _lineas(len(d["rutas"]), "wl lg")))


def _numeros(r):
    d = r["datos"]
    filas = "".join(
        '<tr><td style="font-size:9.6pt">%d</td><td>%s</td>'
        '<td><span class="wl md"></span></td><td><span class="wl md"></span></td></tr>'
        % (i, E(p)) for i, (p, _n) in enumerate(d["prefijos"], 1))
    marco = "".join('<span>%s</span>' % E(f) for f in d["marco"])
    return (
        '<p style="font-size:9.8pt;margin:0 0 2mm"><b>Paso 1 — escucha y anota.</b> Escribe el '
        'prefijo <b>en cifras</b> y <b>en letras</b>. <span class="gloss">Noteer de landcode in '
        'cijfers én voluit — dat laatste is de eigenlijke oefening.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr>'
        '<th style="width:8mm">#</th><th style="width:38mm">País</th>'
        '<th style="width:24mm">En cifras</th><th>En letras</th></tr></thead>'
        '<tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3.5mm 0 1.5mm"><b>Paso 2 — la llamada.</b> A llama, '
        'B contesta. Usa el marco y deletrea tu nombre. '
        '<span class="gloss">A belt, B neemt op. Gebruik het frame en spel je naam.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.4pt;margin:1mm 0 1.5mm">Anota el prefijo de tu compañero/a y '
        'su nombre deletreado:</p>%s' % (filas, marco, _lineas(2, "wl full")))


def _pasaporte(r):
    d = r["datos"]
    fichas = "".join('<div class="ficha">%s</div>' % E(c) for c in d["fichas"])
    banco = "".join('<span><b>%s</b> %s</span>' % (E(es), E(nl)) for es, nl in d["banco_preguntas"])
    filas = "".join(
        '<tr><td style="font-size:9.4pt">%d</td><td><span class="wl lg"></span></td>'
        '<td style="text-align:center;font-size:9.4pt">☐ sí ☐ no</td></tr>' % i
        for i in range(1, 9))
    return (
        '<p style="font-size:9.8pt;margin:0 0 1.5mm"><b>Banco de preguntas.</b> Elige, no '
        'improvises. <span class="gloss">Kies uit de vragenbank; improviseren kost je een beurt.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1.5mm"><b>Tu registro.</b> Anota cada pregunta '
        'y la respuesta. <span class="gloss">Noteer elke vraag en het antwoord — zo sluit je uit '
        'in plaats van te gokken.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>Mi pregunta</th><th style="width:26mm">Respuesta</th></tr></thead>'
        '<tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Mi conclusión:</b> la ciudad de mi '
        'compañero/a es…</p><div style="margin:1mm 0"><span class="wl full"></span></div>'
        '<div class="pliegue">✂ Recortar las fichas · fiches uitknippen</div>'
        '<div class="fichas">%s</div>' % (banco, filas, fichas))


def _identidad(r):
    """Twaalf knipfiches: je stelt je voor als iemand anders."""
    d = r["datos"]
    fichas = "".join(
        '<div class="ficha fid"><b>%s</b><span>%d años</span><span>%s</span>'
        '<span>%s</span><span class="fl">%s</span></div>'
        % (E(n), ed, E(pa), E(ci), E(le)) for n, ed, pa, ci, le in d["fichas"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<p style="font-size:9.8pt;margin:0 0 1.5mm"><b>Tu marco.</b> Cinco frases, todas en '
        'primera persona. <span class="gloss">Vijf zinnen, allemaal in de ik-vorm.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Mis notas</b> — lo que voy a decir:</p>'
        '%s'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Al escuchar a los demás:</b> ¿quién '
        'crees que es? <span class="gloss">Noteer per voorstelling welke fiche je denkt.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:34mm">Compañero/a</th>'
        '<th>Creo que es…</th><th style="width:30mm">¿Por qué?</th></tr></thead><tbody>%s</tbody></table>'
        '<div class="pliegue">✂ Recortar las fichas · fiches uitknippen</div>'
        '<div class="fichas f3">%s</div>'
        % (marco, _lineas(5, "wl full"),
           "".join('<tr><td><span class="wl sm"></span></td><td><span class="wl md"></span></td>'
                   '<td><span class="wl sm"></span></td></tr>' for _ in range(4)),
           fichas))


def _censo(r):
    """Datablad: turven, grafiek tekenen, conclusies schrijven."""
    d = r["datos"]
    preg = "".join(
        '<tr><td style="font-size:9.6pt"><b>%d</b></td><td>%s</td><td class="op">%s</td></tr>'
        % (i, E(q), E(o)) for i, (q, o) in enumerate(d["preguntas"], 1))
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    # geruit vlak voor de staafgrafiek, met een assenlijn
    grafico = ('<div class="grafico"><div class="ejey">'
               + "".join('<span>%d</span>' % v for v in (20, 15, 10, 5, 0))
               + '</div><div class="rejilla"></div></div>')
    return (
        '<p style="font-size:9.8pt;margin:0 0 1.5mm"><b>Paso 1 — elegid vuestra pregunta</b> '
        'y marcad con palitos. <span class="gloss">Kies je vraag en turf de antwoorden.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th style="width:52mm">La pregunta</th><th>Las respuestas · marca con palitos</th>'
        '</tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Paso 2 — el gráfico.</b> Una barra por '
        'respuesta. <span class="gloss">Eén staaf per antwoord; schrijf eronder wat ze voorstelt.</span></p>'
        '%s'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Paso 3 — tres conclusiones</b> con '
        '<b>somos</b> o <b>son</b> y un número de verdad:</p>'
        '<div class="tira">%s</div>%s'
        % (preg, grafico, marco, _lineas(3, "wl full")))


def _aeropuerto(r):
    """Rolkaarten + instapkaarten om uit te knippen, plus een uitsluitingslijst."""
    d = r["datos"]
    # BEWUST zonder stoelnummer: staat het er wél op, dan lost de klas de puzzel
    # op door nummers te vergelijken in plaats van te vragen.
    pas = "".join(
        '<div class="ficha fid"><b>%s</b><span>%s</span><span class="fl">%s</span></div>'
        % (E(n), E(na), E(ci)) for n, na, ci, _a in d["pasajeros"])
    tar = "".join(
        '<div class="ficha tarjeta"><span class="tk">BOARDING</span><b>%s</b>'
        '<span>%s · %s</span></div>' % (E(a), E(na), E(ci))
        for _n, na, ci, a in d["pasajeros"])
    preg = "".join('<span><b>%s</b> %s</span>' % (E(q), E(nl)) for q, nl in d["preguntas"])
    return (
        '<p style="font-size:9.8pt;margin:0 0 1.5mm"><b>Dos tarjetas.</b> La <b>ficha de pasajero</b> dice quién eres; la <b>tarjeta de embarque</b> dice a quién buscas. '
        '<span class="gloss">De passagiersfiche zegt wie jij bent; de instapkaart zegt wie je zoekt. Je eigen stoelnummer weet je dus niet.</span></p>'
        '<p style="font-size:9.8pt;margin:0 0 1.5mm"><b>Solo estas preguntas.</b> '
        '<span class="gloss">Alleen deze vragen — in het Spaans, ook als het traag gaat.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Ya descartados</b> — a quién has '
        'preguntado ya: <span class="gloss">Wie je al hebt uitgesloten, en waarom.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:40mm">Nombre</th>'
        '<th>No es, porque…</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Mi pareja de vuelo es…</b> '
        '(preséntala en tercera persona)</p><div style="margin:1mm 0"><span class="wl full"></span></div>'
        '<div class="pliegue">✂ Fichas de pasajero · passagiersfiches</div>'
        '<div class="fichas f4">%s</div>'
        '<div class="pliegue">✂ Tarjetas de embarque · instapkaarten</div>'
        '<div class="fichas f4">%s</div>'
        % (preg,
           "".join('<tr><td><span class="wl sm"></span></td><td><span class="wl lg"></span></td></tr>'
                   for _ in range(5)),
           pas, tar))


def _error_caro(r):
    """Opwarmbank met geplante fouten + het uitwisselblad met levens."""
    d = r["datos"]
    filas = "".join(
        '<tr><td style="font-size:9.6pt"><b>%d</b></td><td class="fr">%s</td>'
        '<td style="text-align:center">☐</td><td><span class="wl md"></span></td></tr>'
        % (i, E(f)) for i, (f, _ok, _c) in enumerate(d["banco"], 1))
    vidas = "".join('<span class="vida">♥</span>' for _ in range(5))
    return (
        '<p style="font-size:9.8pt;margin:0 0 1.5mm"><b>Ronda 0 — calentamiento.</b> Marca ☐ si '
        'la frase tiene un error y escribe la corrección. <span class="gloss">Kruis aan bij een '
        'fout én schrijf de verbetering — aanwijzen alleen telt niet.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>La frase</th><th style="width:14mm">¿error?</th><th style="width:48mm">Corrección</th>'
        '</tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Ronda 1 — nuestras seis frases</b> '
        '(cuatro correctas, dos con trampa):</p>%s'
        '<div class="vidas"><span>Nuestras vidas:</span>%s'
        '<span style="margin-left:auto">Vidas del equipo rival:</span>%s</div>'
        % (filas, _lineas(6, "wl full"), vidas, vidas))


def _arbol(r):
    d = r["datos"]
    decl = "".join(
        '<div class="decl"><b>%s</b><span>«%s»</span></div>' % (E(q), E(t))
        for q, t in d["declaraciones"])
    return (
        '<p style="font-size:9.8pt;margin:0 0 1.5mm"><b>Las cuatro declaraciones.</b> '
        '<span class="gloss">Lees ze eerst helemaal, zonder te schrijven.</span></p>%s'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Vuestro árbol</b> — dibujadlo con lo '
        'que todos confirman: <span class="gloss">Teken de stamboom met wat álle vier bevestigen.</span></p>'
        '<div class="wbox" style="height:34mm"></div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Miente:</b> '
        '<span class="wl md"></span> &nbsp; <b>La prueba (cita exacta):</b></p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>' % decl)


def _familias(r):
    d = r["datos"]
    filas = "".join(
        '<tr><td>%s</td><td style="text-align:center"><b>%s</b></td>'
        '<td><span class="barra" style="width:%dmm"></span></td></tr>'
        % (E(p), ("%.1f" % n).replace(".", ","), int(n * 14)) for p, n in d["tabla"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:34mm">País</th>'
        '<th style="width:22mm">Personas</th><th>&nbsp;</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Tres frases con «tener»</b> y un número '
        'de verdad: <span class="gloss">Drie zinnen met tener en een echt getal.</span></p>'
        '<div class="tira">%s</div>%s' % (filas, marco, _lineas(4, "wl full")))


def _sin_familia(r):
    d = r["datos"]
    proh = "".join('<span class="prohib">%s</span>' % E(w) for w in d["prohibidas"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<p style="font-size:9.8pt;margin:0 0 1.5mm"><b>Palabras prohibidas:</b></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1.5mm"><b>Tu marco</b> — cógelo o déjalo:</p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Mi gente</b> — cinco frases:</p>'
        '<div class="wbox" style="height:42mm"></div>' % (proh, marco))


def _adjetivo(r):
    d = r["datos"]
    proh = "".join('<span class="prohib">%s</span>' % E(w) for w in d["prohibidas"])
    banco = "".join('<span>%s</span>' % E(w) for w in d["banco"])
    filas = "".join(
        '<tr><td><span class="wl sm"></span></td><td><span class="wl md"></span></td>'
        '<td><span class="wl md"></span></td><td style="text-align:center">☐</td></tr>'
        for _ in range(3))
    return (
        '<p style="font-size:9.8pt;margin:0 0 1.5mm"><b>Prohibidos:</b></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1.5mm"><b>Banco</b> — para empezar; '
        'los fuertes trabajan sin él:</p><div class="tira">%s</div>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:34mm">¿Quién?</th>'
        '<th>Adjetivo 1</th><th>Adjetivo 2</th><th style="width:22mm">¿Adivinado?</th></tr>'
        '</thead><tbody>%s</tbody></table>' % (proh, banco, filas))


def _horario(r):
    d = r["datos"]
    filas = "".join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td>'
                    '<td style="text-align:center">☐</td><td><span class="wl sm"></span></td></tr>'
                    % (E(h), E(q), E(dur)) for h, q, dur in d["agenda"])
    return ('<table class="wtab" style="width:100%%"><thead><tr><th style="width:18mm">Hora</th>'
            '<th>Cita</th><th style="width:28mm">Dura</th><th style="width:16mm">¿choca?</th>'
            '<th style="width:26mm">Nueva hora</th></tr></thead><tbody>%s</tbody></table>'
            '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Los tres choques</b>, con la razón:</p>%s'
            % (filas, _lineas(3, "wl full")))


def _al_reves(r):
    d = r["datos"]
    fr = "".join('<tr><td style="width:14mm"><span class="wl sm"></span></td><td>%s</td>'
                 '<td style="width:34mm"><span class="wl md"></span></td></tr>' % E(f)
                 for f in d["frases"])
    con = "".join('<span>%s</span>' % E(c) for c in d["conectores"])
    return ('<p style="font-size:9.8pt;margin:0 0 1.5mm"><b>Conectores</b> para la tercera columna:</p>'
            '<div class="tira">%s</div>'
            '<table class="wtab" style="width:100%%"><thead><tr><th>Nº</th><th>La frase</th>'
            '<th>Conector</th></tr></thead><tbody>%s</tbody></table>' % (con, fr))


def _oficios(r):
    d = r["datos"]
    bloques = "".join(
        '<div class="decl"><b>%s</b>%s</div>'
        % (E(o), "".join('<span>· %s</span>' % E(p) for p in pistas))
        for o, pistas in d["oficios"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return ('%s<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Su día, en orden</b> '
            '(elegid uno):</p>%s'
            '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Y comparado con el vuestro:</b></p>'
            '<div class="tira">%s</div>%s'
            % (bloques, _lineas(4, "wl full"), marco, _lineas(2, "wl full")))


def _app(r):
    d = r["datos"]
    mod = "".join('<div class="decl"><b>Tú</b><span>%s</span><b>La app</b><span>%s</span></div>'
                  % (E(a), E(b)) for a, b in d["modelos"])
    vb = "".join('<span>%s</span>' % E(v) for v in d["verbos"])
    filas = "".join('<tr><td><span class="wl lg"></span></td><td><span class="wl lg"></span></td></tr>'
                    for _ in range(3))
    return ('%s<p style="font-size:9.8pt;margin:2.5mm 0 1.5mm"><b>Verbos que la app usa siempre:</b></p>'
            '<div class="tira">%s</div>'
            '<table class="wtab" style="width:100%%"><thead><tr><th style="width:50%%">Tu día</th>'
            '<th>La respuesta de la app</th></tr></thead><tbody>%s</tbody></table>'
            % (mod, vb, filas))


def _cita_ciegas(r):
    d = r["datos"]
    def tira(k):
        return "".join('<span>%s</span>' % E(m) for m in d[k])
    planes = "".join('<div class="ficha">%s</div>' % E(p) for p in d["planes"])
    return ('<p style="font-size:9.8pt;margin:0 0 1mm"><b>Ronda 1 — propón:</b></p>'
            '<div class="tira">%s</div><div style="margin:1mm 0"><span class="wl full"></span></div>'
            '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Ronda 2 — reacciona:</b></p>'
            '<div class="tira">%s</div><div style="margin:1mm 0"><span class="wl full"></span></div>'
            '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Ronda 3 — cierra:</b></p>'
            '<div class="tira">%s</div><div style="margin:1mm 0"><span class="wl full"></span></div>'
            '<div class="pliegue">✂ Planes para repartir · plannen om uit te knippen</div>'
            '<div class="fichas f3">%s</div>'
            % (tira("marco_1"), tira("marco_2"), tira("marco_3"), planes))


def _presupuesto(r):
    d = r["datos"]
    filas = "".join('<tr><td>%s</td><td style="text-align:center"><b>%d €</b></td>'
                    '<td style="text-align:center">☐</td></tr>' % (E(p), c)
                    for p, c in d["planes"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return ('<table class="wtab" style="width:100%%"><thead><tr><th>El plan</th>'
            '<th style="width:22mm">Cuesta</th><th style="width:22mm">¿lo hacemos?</th></tr>'
            '</thead><tbody>%s</tbody></table>'
            '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Total:</b> '
            '<span class="wl sm"></span> € &nbsp; <b>de 25 €</b> — ¿cuánto sobra o falta? '
            '<span class="wl sm"></span></p>'
            '<div class="tira">%s</div>'
            '<p style="font-size:9.8pt;margin:2mm 0 1mm"><b>Nuestro plan final</b>, con horas:</p>%s'
            % (filas, marco, _lineas(3, "wl full")))


def _anuncio(r):
    d = r["datos"]
    hechos = "".join('<span class="%s">%s</span>'
                     % ("prohib" if v == "menos bueno" else "", E(h))
                     for h, v in d["hechos"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return ('<p style="font-size:9.8pt;margin:0 0 1.5mm"><b>Los datos.</b> Lo rojo es lo menos '
            'bueno — y también tiene que salir. <span class="gloss">Het rode moet er óók in.</span></p>'
            '<div class="tira">%s</div>'
            '<div class="tira">%s</div>'
            '<p style="font-size:9.8pt;margin:2mm 0 1mm"><b>Tu anuncio</b> — seis frases:</p>'
            '<div class="wbox" style="height:44mm"></div>' % (hechos, marco))


def _encuesta(r):
    d = r["datos"]
    filas = "".join('<tr><td style="font-size:9.6pt">%d</td><td>%s</td><td class="op">%s</td>'
                    '<td><span class="wl sm"></span></td><td><span class="wl sm"></span></td>'
                    '<td><span class="wl sm"></span></td></tr>'
                    % (i, E(q), E(o)) for i, (q, o) in enumerate(d["preguntas"], 1))
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return ('<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
            '<th>La pregunta</th><th style="width:34mm">Opciones</th>'
            '<th>Persona 1</th><th>Persona 2</th><th>Persona 3</th></tr></thead>'
            '<tbody>%s</tbody></table>'
            '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Tu diagrama:</b></p>'
            '<div class="wbox" style="height:30mm"></div>'
            '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Mi conclusión</b> — con un número '
            'y una reacción:</p><div class="tira">%s</div>%s'
            % (filas, marco, _lineas(2, "wl full")))


def _carta_intrusa(r):
    """Menukaart met indringers: aankruisen én het echte land noteren."""
    d = r["datos"]
    filas = "".join(
        '<tr><td style="text-align:center">☐</td><td class="fr">%s</td>'
        '<td><span class="wl md"></span></td></tr>' % E(p)
        for p, _pais, _mex in d["carta"])
    return (
        '<div class="rol">🍽️ La carta de «Sabor de México»</div>'
        '<p style="font-size:9.8pt;margin:0 0 2mm">Diez platos, diez banderas. Pero cuatro no '
        'son de aquí. <span class="gloss">Tien gerechten — vier horen er niet thuis. Kruis ze aan '
        'en schrijf het echte land ernaast.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr>'
        '<th style="width:14mm">¿Intruso?</th><th>El plato</th>'
        '<th style="width:44mm">Es de… (país)</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>La trampa.</b> Dos platos suenan '
        'extranjeros y son mexicanos de toda la vida. ¿Cuáles? '
        '<span class="gloss">Twee gerechten klinken buitenlands en zijn door en door Mexicaans.</span></p>'
        '%s'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Vuestra puntuación:</b> '
        'intrusos acertados <span class="wl sm"></span> × 1 &nbsp;−&nbsp; mexicanos marcados '
        '<span class="wl sm"></span> × 2 &nbsp;=&nbsp; <b><span class="wl sm"></span> puntos</b></p>'
        % (filas, _lineas(2, "wl lg")))


def _resena(r):
    """Eén ster geven zonder één lelijk woord — beleefd vernietigend."""
    d = r["datos"]
    quejas = "".join('<span>%s</span>' % E(q) for q in d["quejas"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    estrellas = ('<div class="vidas"><span class="vida">★</span>'
                 '<span style="color:var(--line2);font-size:12pt">★★★★</span>'
                 '<span>una estrella de cinco · één ster op vijf</span></div>')
    return (
        '<div class="prohib" style="display:inline-block">Prohibido: malo · horrible · fatal · '
        'asqueroso · no me gusta nada</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Paso 1 — elige cinco quejas.</b> '
        '<span class="gloss">Kies vijf klachten en kruis ze aan.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:1mm 0 1mm"><b>Paso 2 — tu único material.</b> '
        'Todo lo demás está prohibido. <span class="gloss">Alleen met deze vijf frames.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Paso 3 — la reseña.</b> Cinco frases '
        'y una despedida amable:</p>'
        '<div class="wbox" style="height:46mm"></div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Tu estrella y tu título</b> — cinco '
        'palabras como máximo:</p>%s%s'
        % (quejas, marco, estrellas,
           '<div style="margin:1.5mm 0"><span class="wl full"></span></div>'))


def _precio_justo(r):
    """Peso ↔ euro: omrekenen, vergelijken, conclusies met een hoeveelheid."""
    d = r["datos"]
    filas = "".join(
        '<tr><td class="fr">%s</td><td style="text-align:center">%d</td>'
        '<td><span class="wl sm"></span> €</td><td style="text-align:center">%s €</td>'
        '<td><span class="wl sm"></span></td></tr>'
        % (E(p), pesos, ("%.2f" % be).replace(".", ","))
        for p, pesos, be in d["productos"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<div class="decl"><b>El cambio de hoy</b><span>%s</span></div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1.5mm"><b>Paso 1 — convertid.</b> Dividid los '
        'pesos entre 20. <span class="gloss">Deel de peso\'s door 20 — dat is de omrekening.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th>El producto</th>'
        '<th style="width:18mm">Pesos</th><th style="width:22mm">= euros</th>'
        '<th style="width:22mm">En Bélgica</th><th style="width:26mm">¿Más caro dónde?</th>'
        '</tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.4pt;margin:1.5mm 0 0;color:var(--mut)">En la última columna escribe '
        '<b>MX</b> o <b>BE</b>. <span class="gloss">Schrijf waar het duurder is.</span></p>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Paso 2 — tres conclusiones,</b> cada una '
        'con una cantidad <u>y</u> un precio:</p>'
        '<div class="tira">%s</div>%s'
        % (E(d["cambio"]), filas, marco, _lineas(3, "wl full")))


def _lo_pido(r):
    """Info-gap met pronomen: A ziet het ingrediënt, B moet ernaar vragen."""
    d = r["datos"]
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    # Alumno A krijgt de ingrediëntkolom, B alleen de gerechten — anders valt er
    # niets te vragen.
    lista_a = "".join(
        '<tr><td style="font-size:9.4pt">%d</td><td class="fr">%s</td>'
        '<td style="font-size:9.4pt;color:var(--gd)">%s</td></tr>'
        % (i, E(p), E(ing)) for i, (p, ing) in enumerate(d["platos"], 1))
    lista_b = "".join(
        '<tr><td style="font-size:9.4pt">%d</td><td class="fr">%s</td>'
        '<td style="text-align:center;font-size:9.2pt">☐ lo pido &nbsp; ☐ no lo pido</td>'
        '<td><span class="wl md"></span></td></tr>'
        % (i, E(p)) for i, (p, _ing) in enumerate(d["platos"], 1))
    return (
        '<p style="font-size:9.8pt;margin:0 0 1.5mm"><b>Tu marco.</b> Sin pronombre no hay '
        'respuesta. <span class="gloss">Zonder voornaamwoord krijg je geen antwoord.</span></p>'
        '<div class="tira">%s</div>'
        '<div class="rol">🍳 Alumno A · la cocina lo sabe todo</div>'
        '<p style="font-size:9.6pt;margin:0 0 1mm">Contesta solo <b>sí, lo lleva</b> o '
        '<b>no, no lo lleva</b>. No leas la lista en voz alta. '
        '<span class="gloss">Antwoord alleen ja of nee. Lees de lijst niet voor.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>El plato</th><th style="width:52mm">Lleva…</th></tr></thead><tbody>%s</tbody></table>'
        '<div class="pliegue">✂ Doblar aquí · hier vouwen</div>'
        '<div class="rol">🙋 Alumno B · tú decides</div>'
        '<p style="font-size:9.6pt;margin:0 0 1mm">Pregunta, decide y escribe <b>por qué</b>. '
        '<span class="gloss">Vraag, beslis en schrijf waarom.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>El plato</th><th style="width:38mm">Mi decisión</th><th>Porque…</th>'
        '</tr></thead><tbody>%s</tbody></table>'
        % (marco, lista_a, lista_b))


def _equipacion(r):
    """Knipkaarten met truitjes: beschrijven op kleur, de groep raadt."""
    d = r["datos"]
    tarjetas = "".join(
        '<div class="ficha fid"><b>%s</b><span>%s</span><span class="fl">%s</span></div>'
        % (E(eq), E(pais), E(desc)) for eq, pais, desc in d["equipos"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    filas = "".join(
        '<tr><td style="font-size:9.4pt">%d</td><td><span class="wl md"></span></td>'
        '<td><span class="wl sm"></span></td><td style="text-align:center;font-size:9.2pt">'
        '☐ sí ☐ no</td></tr>' % i for i in range(1, 9))
    return (
        '<div class="prohib" style="display:inline-block">Prohibido decir: el nombre del club · '
        'la ciudad · el país</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Tu marco</b> — mínimo dos prendas por '
        'descripción: <span class="gloss">minstens twee kledingwoorden per beschrijving.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2mm 0 1mm"><b>El marcador del grupo.</b> '
        '<span class="gloss">Noteer per beurt welke club en welk land jullie gokken.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>Creemos que es…</th><th style="width:30mm">País</th>'
        '<th style="width:24mm">¿Acertado?</th></tr></thead><tbody>%s</tbody></table>'
        '<div class="pliegue">✂ Tarjetas de equipación · truitjeskaarten</div>'
        '<div class="fichas f4">%s</div>' % (marco, filas, tarjetas))


def _armario(r):
    """Inventaris van een kast; elke conclusie heeft een bewijsstuk."""
    d = r["datos"]
    inv = "".join('<tr><td style="text-align:center;font-size:9pt;color:var(--mut)">%d</td>'
                  '<td class="fr">%s</td></tr>' % (i, E(x))
                  for i, x in enumerate(d["armario"], 1))
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    pruebas = "".join(
        '<tr><td><span class="wl md"></span></td><td><span class="wl lg"></span></td></tr>'
        for _ in range(3))
    return (
        '<div class="rol">🚪 El armario de… ¿de quién?</div>'
        '<p style="font-size:9.8pt;margin:0 0 2mm">Nadie te dice quién vive aquí. Solo tienes '
        'lo que hay dentro — y lo que <b>no</b> hay. '
        '<span class="gloss">Niemand zegt wie hier woont. Je hebt alleen wat erin ligt — en wat er '
        '<b>niet</b> ligt.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>En el armario hay…</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Tres conclusiones, tres pruebas.</b> '
        'Una conclusión sin prenda no vale. <span class="gloss">Een conclusie zonder kledingstuk '
        'telt niet.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:52mm">Creo que…</th>'
        '<th>… porque en el armario hay/no hay…</th></tr></thead><tbody>%s</tbody></table>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Mi personaje en una frase</b> — oficio, '
        'edad más o menos y dónde vive:</p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>'
        % (inv, pruebas, marco))


def _moda_circular(r):
    """Waterdata + eigen aankopen, in «acabar de»-zinnen."""
    d = r["datos"]
    filas = "".join('<tr><td class="fr">%s</td><td style="text-align:right"><b>%s</b></td></tr>'
                    % (E(q), E(v)) for q, v in d["tabla"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<div class="rol">💧 La ropa en cifras</div>'
        '<table class="wtab" style="width:100%%"><thead><tr><th>El dato</th>'
        '<th style="width:44mm;text-align:right">Cuánto</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>El dato que más nos sorprende</b> y por qué:</p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Vuestras tres últimas compras</b> — con '
        '«acabar de» y un número de la tabla:</p>'
        '<div class="tira">%s</div>%s'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Una promesa realista</b> para el próximo mes '
        '(sin prometer imposibles):</p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>'
        % (filas, marco, _lineas(3, "wl full")))


def _escaparate(r):
    """Precies dertig woorden — met een telrooster om echt te tellen."""
    d = r["datos"]
    prendas = "".join('<span><b>%s</b> %s</span>' % (E(p), E(pr)) for p, pr in d["prendas"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    # zes rijen van vijf hokjes = precies dertig woorden, één woord per hokje
    rejilla = "".join(
        '<tr>%s</tr>' % "".join('<td><span class="wl sm"></span></td>' for _ in range(5))
        for _ in range(6))
    return (
        '<p style="font-size:9.8pt;margin:0 0 1mm"><b>Elegid una prenda.</b></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:1mm 0 1mm"><b>Fórmulas con pronombre</b> — necesitáis '
        'cuatro como mínimo: <span class="gloss">minstens vier keer lo, la, los of las.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>El cartel.</b> Una palabra por casilla. '
        'Seis filas de cinco = treinta exactas. <span class="gloss">Eén woord per hokje. Zes rijen '
        'van vijf = precies dertig — het rooster telt voor je.</span></p>'
        '<table class="wtab" style="width:100%%"><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm">Pronombres usados: '
        '<span class="wl sm"></span> &nbsp;·&nbsp; ¿llegáis a treinta? ☐ sí ☐ no — '
        '¿qué habéis quitado? <span class="wl md"></span></p>'
        % (prendas, marco, rejilla))


_MATERIAL = {"C5-U0-RETO-03": _gps, "C5-U0-RETO-08": _numeros, "C5-U0-RETO-10": _pasaporte,
             "C5-U1-RETO-02": _identidad, "C5-U1-RETO-03": _censo,
             "C5-U1-RETO-06": _aeropuerto, "C5-U1-RETO-08": _error_caro,
             "C5-U2-RETO-01": _arbol, "C5-U2-RETO-05": _familias,
             "C5-U2-RETO-06": _sin_familia, "C5-U2-RETO-10": _adjetivo,
             "C5-U3-RETO-01": _horario, "C5-U3-RETO-03": _al_reves,
             "C5-U3-RETO-06": _oficios, "C5-U3-RETO-07": _app,
             "C5-U4-RETO-04": _cita_ciegas, "C5-U4-RETO-05": _presupuesto,
             "C5-U4-RETO-07": _anuncio, "C5-U4-RETO-10": _encuesta,
             "C5-U5-RETO-02": _carta_intrusa, "C5-U5-RETO-03": _resena,
             "C5-U5-RETO-05": _precio_justo, "C5-U5-RETO-10": _lo_pido,
             "C5-U6-RETO-03": _equipacion, "C5-U6-RETO-04": _armario,
             "C5-U6-RETO-05": _moda_circular, "C5-U6-RETO-07": _escaparate}


def reto_print(r):
    """De volledige oefening op papier."""
    cuerpo = _MATERIAL[r["id"]](r)
    return ('<div class="reto">%s%s'
            '<p class="rconsigna">%s <span class="gloss">%s</span></p>'
            '%s%s%s</div>'
            % (_cabecera(r), _badges(r), E(r["consigna_es"]), E(r["consigna_nl"]),
               _regla(r), _pasos(r), cuerpo))


def reto_puntero(r):
    """Vier regels voor een reto die elders leeft — geen halve kopie."""
    es, nl = _DONDE[r["soporte"]]
    return ('<div class="rpunt"><div class="ric">%s</div><div>'
            '<h4>Reto %d · %s</h4>'
            '<p><b>%s</b> <span class="gloss">%s</span></p>'
            '<p style="margin-top:1.2mm"><b>La regla:</b> %s</p>'
            '<p class="rdonde">%s · %s — %s</p></div></div>'
            % (_ICONO[r["soporte"]], r["num"], E(r["nombre"]),
               E(r["gancho_es"]), E(r["gancho_nl"]), E(r["regla"]),
               E(r["lente"]), E(es), E(nl)))
