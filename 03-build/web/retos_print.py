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
       margin:4mm 0 5mm; break-inside:auto; background:#FFFDF9; }
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

/* ── bladspiegel · uit 02-huisstijl/templates/cursus-print.css ───────────── */
p,li,dd,td,.intro,.hist,.rgancho,.rconsigna{ orphans:3; widows:3; }
.sec{ break-before:auto; break-inside:auto; margin-top:12mm; }
.sec.major{ break-before:page; margin-top:0; }
.sec:first-of-type{ margin-top:0; }
.regla,.truc,.pcard,.call,.qr,.guide,.esen,.mp,.audiorow,.wcols,.wbox,.sem,
.acthead,.obsbox,.machine,.tree,.zoom,.fmu,.xray,.colloc,.clusters,.vpairs,
.blocks,.agree,.rpunt,.fichacard,.mispal,.scale{ break-inside:avoid; }
.act,.reto,.lectura,table{ break-inside:auto; }
.act > .acthead,.reto .rcab,.reto > h3{ break-after:avoid; }
.reto,.act,.esen,.obsbox{ -webkit-box-decoration-break:clone; box-decoration-break:clone; }
.alf tr,.mp tr,.sem tr,.conj tr,.wtab tr{ break-inside:avoid; }
.alf thead,.mp thead,.sem thead,.conj thead,.wtab thead{ display:table-header-group; }
.page .page{ padding-left:0; padding-right:0; }
h2,h3,.pk,.divider,.se{ break-after:avoid; }
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


def _plano(r):
    """Advertentie naast een plattegrond: de leugen aanwijzen én citeren."""
    d = r["datos"]
    anuncio = "".join(
        '<tr><td style="text-align:center;font-size:9pt;color:var(--mut)">%d</td>'
        '<td class="fr">%s</td><td style="text-align:center">☐</td></tr>'
        % (i, E(f)) for i, (f, _ok, _v) in enumerate(d["anuncio"], 1))
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    pruebas = "".join(
        '<tr><td><span class="wl sm"></span></td><td><span class="wl lg"></span></td></tr>'
        for _ in range(3))
    return (
        '<div class="rol">🏠 Se alquila · el anuncio</div>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>Lo que dice el anuncio</th><th style="width:20mm">¿Miente?</th>'
        '</tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>El plano.</b> Dibújalo mientras lees: '
        'cada habitación en su sitio. <span class="gloss">Teken het plan terwijl je leest — '
        'wie tekent, ziet de tegenspraak vanzelf.</span></p>'
        '<div class="wbox" style="height:42mm"></div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Las tres mentiras,</b> con la frase '
        'que las delata:</p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:16mm">Frase n.º</th>'
        '<th>El anuncio dice… pero en el plano…</th></tr></thead><tbody>%s</tbody></table>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>La trampa:</b> una frase parece falsa '
        'y es verdadera. ¿Cuál? <span class="wl md"></span></p>'
        % (anuncio, pruebas, marco))


def _mudanza(r):
    """Info-gap met een leeg grondplan: A dicteert, B tekent blind."""
    d = r["datos"]
    dictado = "".join(
        '<div style="margin:1.8mm 0;font-size:9.6pt"><b>%d.</b> %s — <i>%s</i></div>'
        % (i, E(m), E(donde)) for i, (m, donde) in enumerate(d["plano_a"], 1))
    muebles = "".join('<span>%s</span>' % E(m) for m in d["muebles"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<div class="rol">🗣️ Alumno A · el que dicta</div>'
        '<p style="font-size:9.6pt;margin:0 0 1.5mm">Dicta mueble por mueble. No enseñes esta '
        'parte y no señales. <span class="gloss">Dicteer meubel per meubel. Laat dit deel niet '
        'zien en wijs niet.</span></p>'
        + dictado +
        '<div class="pliegue">✂ Doblar aquí · hier vouwen</div>'
        '<div class="rol">✏️ Alumno B · el que coloca</div>'
        '<p style="font-size:9.6pt;margin:0 0 1mm">Estos son tus muebles. Escríbelos en el plano '
        'donde te digan. <span class="gloss">Dit zijn jouw meubels. Schrijf ze op het plan waar '
        'je het hoort.</span></p>'
        '<div class="tira">%s</div>'
        '<div class="wbox" style="height:56mm"></div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Preguntas que puedes hacer</b> — en '
        'español, siempre:</p><div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Después de comparar:</b> ¿dónde se '
        'rompió la comunicación, y por qué?</p>%s'
        % (muebles, marco, _lineas(2, "wl full")))


def _capas(r):
    """Drie tijdlagen van dezelfde straat, in drie kolommen."""
    d = r["datos"]
    cols = "".join(
        '<div class="wcol"><div class="ch">%s</div>'
        '<div style="font-size:8.8pt;line-height:1.5;padding:2mm 2.5mm">%s</div>'
        '<div class="cb short"></div></div>'
        % (E(anno), "<br>".join("· " + E(x) for x in items))
        for anno, items in d["capas"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<p style="font-size:9.8pt;margin:0 0 1.5mm"><b>La misma calle, tres veces.</b> Debajo '
        'de cada capa escribes <u>una</u> frase con <b>hay</b> y <u>una</u> con <b>está</b>. '
        '<span class="gloss">Onder elke laag: één zin met hay en één met está.</span></p>'
        '<div class="wcols" style="grid-template-columns:repeat(3,1fr)">%s</div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>¿Qué ha cambiado de sitio?</b> Una cosa '
        'está en las tres capas, pero no hace lo mismo:</p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Tres frases que empiezan por «Ya no hay…»:</b></p>%s'
        % (cols, marco, _lineas(3, "wl full")))


def _robot(r):
    """Route in imperatieven, met een hindernisbaan die vaagheid afstraft."""
    d = r["datos"]
    ordenes = "".join('<span><b>%s</b></span>' % E(o) for o in d["ordenes"])
    obst = "".join(
        '<tr><td class="fr">%s</td><td style="text-align:center">☐ resuelto</td></tr>'
        % E(o) for o, _por in d["obstaculos"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<p style="font-size:9.8pt;margin:0 0 1mm"><b>Tus únicas órdenes.</b> Cada paso = un '
        'verbo + un número o un nombre. <span class="gloss">Elke stap is één werkwoord plus een '
        'getal of een naam.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:1.5mm 0 1mm"><b>La pista de obstáculos.</b> El robot '
        'choca en cada uno si tu orden es vaga. <span class="gloss">Bij elk obstakel botst de '
        'robot als je opdracht vaag is.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th>El obstáculo</th>'
        '<th style="width:30mm">¿Lo has resuelto?</th></tr></thead><tbody>%s</tbody></table>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Vuestra ruta</b> — una orden por línea:</p>%s'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Después de la ejecución:</b> ¿en qué '
        'orden chocó, y cómo la habéis corregido?</p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>'
        % (ordenes, obst, marco, _lineas(8, "wl full")))


def _maleta(r):
    """Vijftien voorwerpen om uit te knippen + het conclusieblad met bewijs."""
    d = r["datos"]
    fichas = "".join('<div class="ficha">%s</div>' % E(o) for o in d["objetos"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    filas = "".join(
        '<tr><td style="font-size:9.4pt">%d</td><td><span class="wl lg"></span></td>'
        '<td><span class="wl md"></span></td></tr>' % i for i in range(1, 6))
    return (
        '<div class="rol">🧳 Objetos perdidos · aeropuerto de Cusco</div>'
        '<p style="font-size:9.8pt;margin:0 0 1.5mm">Quince objetos y ni un nombre. '
        '<span class="gloss">Vijftien voorwerpen en geen enkele naam.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Cinco conclusiones, cinco pruebas.</b> '
        'Cada frase en perfecto. <span class="gloss">Elke zin in het perfecto, met het voorwerp '
        'dat haar bewijst.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>Ha … (en perfecto)</th><th style="width:46mm">Lo prueba…</th>'
        '</tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Un objeto no encaja.</b> ¿Cuál, y qué '
        'significa? <span class="gloss">Eén voorwerp past niet. Welk, en wat betekent dat?</span></p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>'
        '<div class="pliegue">✂ Objetos para recortar · voorwerpen om uit te knippen</div>'
        '<div class="fichas f3">%s</div>' % (marco, filas, fichas))


def _diario(r):
    """Vier foto-aanzetten, zes perfecto-zinnen, één te veel."""
    d = r["datos"]
    fotos = "".join(
        '<div class="ficha fid"><b>%s</b><span class="fl">%s</span><span>☐ la elijo</span></div>'
        % (E(t), E(sub)) for t, sub in d["fotos"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<p style="font-size:9.8pt;margin:0 0 1mm"><b>Elige una foto.</b> Nadie tiene que haber '
        'estado allí. <span class="gloss">Niemand hoeft er geweest te zijn — dat is net de opzet.</span></p>'
        '<div class="fichas f4">%s</div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Tu marco</b> — seis frases, todas en '
        'perfecto:</p><div class="tira">%s</div>'
        '%s'
        '<div class="prohib" style="display:inline-block;margin-top:2mm">La frase inventada va '
        'en el medio (3, 4 o 5). Nunca la última.</div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Al escuchar a los demás:</b> ¿qué frase '
        'es la falsa, y por qué?</p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:34mm">Compañero/a</th>'
        '<th style="width:16mm">Frase n.º</th><th>Porque…</th></tr></thead><tbody>%s</tbody></table>'
        % (fotos, marco, _lineas(6, "wl full"),
           "".join('<tr><td><span class="wl sm"></span></td>'
                   '<td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
                   for _ in range(4))))


def _machu(r):
    """Bezoekerstabel + conclusies met een cijfer, en het dilemma."""
    d = r["datos"]
    filas = "".join(
        '<tr><td style="text-align:center"><b>%s</b></td><td class="fr">%s</td>'
        '<td style="font-size:9.4pt;color:var(--mut)">%s</td></tr>'
        % (E(a), E(v), E(lim)) for a, v, lim in d["tabla"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<div class="rol">📈 Visitantes de Machu Picchu</div>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:20mm">Año</th>'
        '<th>Visitantes</th><th style="width:52mm">Límite diario</th>'
        '</tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.4pt;margin:1.5mm 0 0;color:var(--mut)">Cifras redondeadas — para '
        'ver el orden de magnitud, no para citar como estadística oficial.</p>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>La subida más grande</b> está entre '
        '<span class="wl sm"></span> y <span class="wl sm"></span> · '
        '<b>la única bajada</b> es en <span class="wl sm"></span>, porque '
        '<span class="wl md"></span></p>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Tres conclusiones,</b> cada una con '
        'una cifra y un verbo en perfecto:</p>'
        '<div class="tira">%s</div>%s'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>¿El límite es justo?</b> Una frase a '
        'favor y una en contra — las dos:</p>'
        '<div class="wcols" style="grid-template-columns:1fr 1fr">'
        '<div class="wcol"><div class="ch">A favor</div><div class="cb short"></div></div>'
        '<div class="wcol"><div class="ch">En contra</div><div class="cb short"></div></div></div>'
        % (filas, marco, _lineas(3, "wl full")))


def _balance(r):
    """Acht zinnen, acht participia, en ser/estar op slot."""
    d = r["datos"]
    banco = "".join('<span>%s</span>' % E(v) for v in d["banco"])
    irr = "".join('<span><b>%s</b> → %s</span>' % (E(inf), E(part))
                  for inf, part in d["irregulares"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    filas = "".join(
        '<tr><td style="font-size:9.4pt">%d</td><td><span class="wl lg"></span></td>'
        '<td><span class="wl sm"></span></td></tr>' % i for i in range(1, 9))
    return (
        '<div class="prohib" style="display:inline-block">Prohibido: he sido · he estado · '
        'ha sido · ha estado</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>El banco de verbos.</b> Elige ocho '
        'distintos. <span class="gloss">Kies er acht verschillende.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:1mm 0 1mm"><b>Los irregulares</b> — los que valen doble:</p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Tu balance.</b> Una frase por línea; '
        'en la última columna escribe el participio que has usado.</p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>Este año he…</th><th style="width:30mm">Participio</th>'
        '</tr></thead><tbody>%s</tbody></table>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm">Irregulares usados: '
        '<span class="wl sm"></span> de 9 &nbsp;·&nbsp; ¿algún participio repetido? ☐ sí ☐ no</p>'
        % (banco, irr, filas, marco))


# ── C6+ ──────────────────────────────────────────────────────────────────────

def _test_falso(r):
    """Tien testzinnen om te corrigeren, mét de naam van de regel."""
    d = r["datos"]
    filas = "".join(
        '<tr><td style="font-size:9.4pt">%d</td><td class="fr">%s</td>'
        '<td style="text-align:center">☐</td><td><span class="wl md"></span></td>'
        '<td><span class="wl sm"></span></td></tr>' % (i, E(f))
        for i, (f, _ok, _cor, _reg) in enumerate(d["frases"], 1))
    reglas = "".join('<span><b>%s</b></span>' % E(x) for x in d["reglas"])
    return (
        '<div class="rol">📝 Test de nivel · versión del corrector</div>'
        '<p style="font-size:9.8pt;margin:0 0 1mm">Cinco nombres de regla. Uno por error. '
        '<span class="gloss">Vijf regelnamen. Eén per fout — schrijf hem in de laatste kolom.</span></p>'
        '<div class="tira">%s</div>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>La frase</th><th style="width:16mm">¿Mal?</th><th style="width:48mm">Corrección</th>'
        '<th style="width:26mm">Regla</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>He encontrado</b> '
        '<span class="wl sm"></span> <b>errores de 6.</b> Ojo: una frase lleva dos. '
        '<span class="gloss">Let op: één zin bevat er twee.</span></p>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Mi punto débil</b> — la regla que más '
        'se me escapa: <span class="wl md"></span></p>' % (reglas, filas))


def _quien_es_quien(r):
    """Twintig knipfiches met land en kenmerk + het uitsluitblad."""
    d = r["datos"]
    fichas = "".join(
        '<div class="ficha fid"><b>%s</b><span>%s</span><span>%s</span>'
        '<span class="fl">%s</span></div>'
        % (E(n), E(pais), E(zona), E(extra if extra != "—" else rasgo))
        for n, pais, zona, extra, rasgo in d["fichas"])
    preg = "".join('<span><b>%s</b> %s</span>' % (E(q), E(nl)) for q, nl in d["preguntas"])
    filas = "".join(
        '<tr><td style="font-size:9.4pt">%d</td><td><span class="wl lg"></span></td>'
        '<td style="text-align:center;font-size:9.2pt">☐ sí ☐ no</td>'
        '<td><span class="wl md"></span></td></tr>' % i for i in range(1, 6))
    return (
        '<p style="font-size:9.8pt;margin:0 0 1mm"><b>Banco de preguntas.</b> Solo sí o no — y el '
        'nombre del país solo en la última. <span class="gloss">Alleen ja/nee. De landnaam mag '
        'pas in je laatste vraag.</span></p>'
        '<div class="tira">%s</div>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>Mi pregunta</th><th style="width:24mm">Respuesta</th>'
        '<th style="width:40mm">Descarto…</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Mi conclusión:</b> es de… '
        '<span class="wl md"></span> &nbsp;·&nbsp; ¿en cuántas preguntas? '
        '<span class="wl sm"></span></p>'
        '<div class="pliegue">✂ Veinte fichas · twintig fiches om uit te knippen</div>'
        '<div class="fichas f4">%s</div>' % (preg, filas, fichas))


def _lenguas(r):
    """Talentabel met sprekersaantallen + «se habla(n)»-zinnen."""
    d = r["datos"]
    filas = "".join(
        '<tr><td class="fr"><b>%s</b></td><td style="font-size:9.4pt">%s</td>'
        '<td style="text-align:right">%s</td><td style="font-size:9pt;color:var(--mut)">%s</td></tr>'
        % (E(l), E(donde), E(n), E(st)) for l, donde, n, st in d["lenguas"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<div class="rol">🗣️ Lenguas del mundo hispano</div>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:34mm">La lengua</th>'
        '<th style="width:44mm">¿Dónde?</th><th style="width:30mm">Hablantes</th>'
        '<th>Estatus</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.4pt;margin:1.5mm 0 0;color:var(--mut)">Cifras redondeadas: cada '
        'fuente cuenta de otra manera.</p>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>La lengua con más hablantes de toda la '
        'tabla</b> es <span class="wl md"></span> · <b>y la indígena con más hablantes</b> es '
        '<span class="wl md"></span></p>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Tres frases con «se habla» o «se '
        'hablan»</b> y una cifra. Ojo al plural:</p>'
        '<div class="tira">%s</div>%s'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Lo que más nos sorprende:</b></p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>'
        % (filas, marco, _lineas(3, "wl full")))


def _adjetivos_sitio(r):
    """Zes paren in context; de regel wordt zelf geformuleerd."""
    d = r["datos"]
    filas = "".join(
        '<tr><td class="fr"><b>%s</b></td><td class="fr"><b>%s</b></td>'
        '<td style="font-size:9.2pt;color:var(--mut)">%s</td></tr>'
        % (E(a), E(b), E(ctx)) for a, b, ctx in d["pares"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<div class="prohib" style="display:inline-block">Prohibido buscar la regla y prohibido '
        'preguntar. Se deduce.</div>'
        '<table class="wtab" style="width:100%%;margin-top:2.5mm"><thead><tr>'
        '<th style="width:34mm">Delante</th><th style="width:34mm">Detrás</th>'
        '<th>El contexto que lo delata</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>¿Qué significa cada posición?</b></p>'
        '<div class="wcols" style="grid-template-columns:1fr 1fr">'
        '<div class="wcol"><div class="ch">Delante del sustantivo</div><div class="cb short"></div></div>'
        '<div class="wcol"><div class="ch">Detrás del sustantivo</div><div class="cb short"></div></div>'
        '</div>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Nuestra regla, en una sola frase:</b></p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm">Y un descubrimiento extra: ¿qué le pasa a '
        '<b>grande</b> cuando va delante? <span class="wl md"></span></p>' % (filas, marco))


def _turno_noche(r):
    """Acht losse aanwijzingen → één omgekeerde dag."""
    d = r["datos"]
    pistas = "".join(
        '<div style="margin:1.6mm 0;font-size:9.6pt"><b>%d.</b> %s</div>'
        % (i, E(p)) for i, (p, _h) in enumerate(d["pistas"], 1))
    verbos = "".join('<span>%s</span>' % E(v) for v in d["verbos"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    filas = "".join(
        '<tr><td><span class="wl sm"></span></td><td><span class="wl lg"></span></td></tr>'
        for _ in range(8))
    return (
        '<div class="rol">🌙 Ocho pistas · ni un solo horario dado</div>'
        + pistas +
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Su día, de las seis de la tarde a las '
        'diez de la mañana.</b> Cada línea: la hora y una frase con reflexivo.</p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:22mm">Hora</th>'
        '<th>Lo que hace</th></tr></thead><tbody>%s</tbody></table>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Comparad con vuestro día:</b> ¿qué se '
        'invierte del todo?</p><div class="tira">%s</div>%s'
        % (filas, verbos, marco, _lineas(2, "wl full")))


def _agenda(r):
    """Vier agenda's om uit te knippen + het verschilblad."""
    d = r["datos"]
    original = "".join(
        '<tr><td style="font-size:9.4pt;color:var(--mut)">%s</td><td class="fr">%s</td></tr>'
        % (E(dia), E(x)) for dia, x in d["agenda"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    filas = "".join(
        '<tr><td style="font-size:9.4pt">%d</td><td><span class="wl md"></span></td>'
        '<td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
        % i for i in range(1, 6))
    return (
        '<div class="rol">📅 Tu agenda · no la enseñes a nadie</div>'
        '<p style="font-size:9.6pt;margin:0 0 1.5mm">Todas las horas se dicen <b>en palabras</b>. '
        '<span class="gloss">Alle uren zeg je voluit: «las nueve menos cuarto», nooit «8.45».</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:44mm">¿Cuándo?</th>'
        '<th>¿Qué?</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Las cinco diferencias</b> — con las dos '
        'horas, la tuya y la suya:</p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>¿Qué actividad?</th><th style="width:32mm">Yo tengo…</th>'
        '<th style="width:32mm">Él/ella tiene…</th></tr></thead><tbody>%s</tbody></table>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>¿Cuál es la agenda original?</b> '
        'Decidid en grupo y explicad por qué:</p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>'
        % (original, filas, marco))


def _diario_objeto(r):
    """Voorwerpkaarten + reflexievenbank + schrijfvlak."""
    d = r["datos"]
    obj = "".join('<div class="ficha fid"><b>%s</b><span class="fl">%s</span>'
                  '<span>☐ lo elijo</span></div>' % (E(o), E(v)) for o, v in d["objetos"])
    refl = "".join('<span>%s</span>' % E(v) for v in d["reflexivos"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<div class="fichas f3">%s</div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>El banco de reflexivos.</b> Necesitas '
        'seis, y dos en sentido figurado. <span class="gloss">Zes stuks, waarvan twee '
        'figuurlijk.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:1.5mm 0 1mm"><b>Tu marco</b> — todo en primera persona:</p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2mm 0 1mm"><b>El diario de mi objeto:</b></p>'
        '<div class="wbox" style="height:66mm"></div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm">Reflexivos usados: '
        '<span class="wl sm"></span> de 6 &nbsp;·&nbsp; ¿cuáles son los dos figurados? '
        '<span class="wl md"></span></p>' % (obj, refl, marco))


def _sustituto(r):
    """Handleiding per dagdeel, met de verplichte niet-doen-regel."""
    d = r["datos"]
    bloques = "".join(
        '<div class="wcol"><div class="ch">%s<small>%s</small></div><div class="cb"></div></div>'
        % (E(b), E(h)) for b, h in d["bloques"])
    verbos = "".join('<span>%s</span>' % E(v) for v in d["verbos"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<p style="font-size:9.8pt;margin:0 0 1mm"><b>Los verbos que necesitas</b> — en '
        'imperativo, con el pronombre en su sitio: <span class="gloss">in de gebiedende wijs, met '
        'het voornaamwoord op de juiste plaats.</span></p>'
        '<div class="tira">%s</div>'
        '<div class="tira">%s</div>'
        '<div class="wcols" style="grid-template-columns:repeat(4,1fr)">%s</div>'
        '<div class="prohib" style="display:inline-block;margin-top:3mm">Obligatorio: una línea '
        '«Lo que NO debes hacer». Una sola.</div>'
        '<div style="margin:2mm 0"><span class="wl full"></span></div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Después de intercambiar:</b> ¿qué le '
        'faltaba a tu manual para que funcionara?</p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>'
        % (verbos, marco, bloques))


def _casa_crimen(r):
    """Plattegrond, vier alibi's en de details die ze tegenspreken."""
    d = r["datos"]
    plano = "".join('<span>%s</span>' % E(x) for x in d["plano"])
    coart = "".join(
        '<div class="decl"><b>%s</b><span>«%s»</span>'
        '<span style="font-size:8.8pt;color:var(--mut)">dice que está en: %s</span></div>'
        % (E(n), E(txt), E(hab)) for n, txt, hab, _ok in d["coartadas"])
    det = "".join('<tr><td class="fr">%s</td></tr>' % E(x) for x in d["detalles"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<div class="rol">🏠 El plano del piso</div>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2mm 0 1mm"><b>Las cuatro coartadas.</b></p>%s'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Lo que sabemos del piso</b> — aquí está '
        'la contradicción: <span class="gloss">Hier zit de tegenspraak.</span></p>'
        '<table class="wtab" style="width:100%%"><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Las dos frases que no pueden ser verdad '
        'a la vez:</b></p>%s'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Acusamos a…</b> y esto es lo que '
        'estaba haciendo de verdad:</p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>'
        % (plano, coart, det, _lineas(2, "wl full"), marco))


def _metros(r):
    """Woonoppervlakte per persoon in vijf steden."""
    d = r["datos"]
    filas = "".join(
        '<tr><td class="fr"><b>%s</b></td><td style="text-align:center">%s</td>'
        '<td style="font-size:9.4pt">%s</td><td style="font-size:9pt;color:var(--mut)">%s</td></tr>'
        % (E(c), E(m2), E(viv), E(obs)) for c, m2, viv, obs in d["tabla"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:34mm">La ciudad</th>'
        '<th style="width:26mm">Por persona</th><th style="width:44mm">Vivienda típica</th>'
        '<th>Y además…</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.4pt;margin:1.5mm 0 0;color:var(--mut)">Cifras redondeadas de '
        'estadística pública de vivienda.</p>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Mi habitación mide, más o menos,</b> '
        '<span class="wl sm"></span> m² · <b>y en casa somos</b> <span class="wl sm"></span> '
        '<b>personas.</b></p>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Tres conclusiones</b> — cada una con '
        'una cifra y con <b>hay</b> o <b>está</b>. Una tiene que ser sobre vosotros:</p>'
        '<div class="tira">%s</div>%s' % (filas, marco, _lineas(3, "wl full")))


def _cuarto_sin(r):
    """Tien regels beschrijven zonder één voorwerp te noemen."""
    d = r["datos"]
    perm = "".join('<span>%s</span>' % E(x) for x in d["permitido"])
    prohib = "".join('<span class="prohib" style="font-size:8.6pt">%s</span>' % E(x)
                     for x in d["prohibido"])
    tipos = "".join('<div class="ficha">%s</div>' % E(t) for t in d["tipos"])
    return (
        '<p style="font-size:9.8pt;margin:0 0 1mm"><b>Lo que sí puedes usar:</b></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:1.5mm 0 1mm"><b>Lo que no, ni una vez:</b></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2mm 0 1mm"><b>Elige tu habitación</b> (o inventa otra):</p>'
        '<div class="fichas" style="grid-template-columns:repeat(5,1fr)">%s</div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Diez líneas, cero objetos:</b></p>%s'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm">Objetos nombrados: '
        '<span class="wl sm"></span> (tiene que ser 0) &nbsp;·&nbsp; ¿adivinan qué habitación es? '
        '☐ sí ☐ no</p>' % (perm, prohib, tipos, _lineas(10, "wl full")))


def _mudanza_etapas(r):
    """Zestien voorwerpen, tien plaatsen, en de pronomenregel."""
    d = r["datos"]
    obj = "".join('<span>☐ %s</span>' % E(o) for o in d["objetos"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    filas = "".join(
        '<tr><td style="font-size:9.4pt">%d</td><td><span class="wl md"></span></td>'
        '<td><span class="wl lg"></span></td></tr>' % i for i in range(1, 11))
    return (
        '<div class="decl"><b>El piso nuevo</b><span>%s</span></div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Dieciséis cosas, diez plazas.</b> '
        'Marcad las que os lleváis. <span class="gloss">Zestien dingen, tien plaatsen.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:1.5mm 0 1mm"><b>A partir de la segunda mención: '
        'pronombre.</b> <span class="gloss">Vanaf de tweede vermelding: voornaamwoord.</span></p>'
        '<div class="tira">%s</div>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th style="width:44mm">Nos la/lo llevamos…</th><th>… porque</th>'
        '</tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Y lo que dejamos</b> — una frase por cosa, '
        'con pronombre:</p>%s'
        % (E(d["espacio"]), obj, marco, filas, _lineas(3, "wl full")))


def _hilo(r):
    """De chatdraad met de ontvangerkolom leeg."""
    d = r["datos"]
    filas = "".join(
        '<tr><td style="font-size:9.4pt">%d</td>'
        '<td style="font-size:9.4pt;color:var(--gd);font-weight:600">%s</td>'
        '<td class="fr">%s</td><td><span class="wl sm"></span></td></tr>'
        % (i, E(q), E(t)) for i, (q, t, _a) in enumerate(d["hilo"], 1))
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<div class="rol">💬 Grupo «Cancha viernes» · 14 mensajes</div>'
        '<p style="font-size:9.6pt;margin:0 0 1.5mm">En la última columna escribe a quién va: '
        'un nombre, o <b>todos</b>. <span class="gloss">Schrijf in de laatste kolom aan wie het '
        'gericht is: een naam, of «todos».</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th style="width:22mm">¿Quién?</th><th>El mensaje</th>'
        '<th style="width:26mm">¿A quién?</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Siete frases con «le» o «les».</b> Ojo: '
        'en español el pronombre <u>y</u> la persona van juntos («le dije <b>a</b> Camila»).</p>'
        '<div class="tira">%s</div>%s'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>El malentendido empieza en el mensaje '
        'n.º</b> <span class="wl sm"></span> <b>, porque…</b></p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>'
        % (filas, marco, _lineas(7, "wl full")))


def _sin_emoji(r):
    """Vijf berichten herschrijven zonder emoji."""
    d = r["datos"]
    filas = "".join(
        '<tr><td style="font-size:9.4pt">%d</td><td class="fr" style="font-size:11pt">%s</td>'
        '<td><span class="wl sm"></span></td><td><span class="wl lg"></span></td></tr>'
        % (i, E(m)) for i, (m, _tono, _por) in enumerate(d["mensajes"], 1))
    banco = "".join('<span>%s</span>' % E(b) for b in d["banco"])
    return (
        '<div class="prohib" style="display:inline-block">Prohibido: emojis · MAYÚSCULAS para '
        'gritar · !!!!!</div>'
        '<table class="wtab" style="width:100%%;margin-top:2.5mm"><thead><tr>'
        '<th style="width:8mm">#</th><th style="width:34mm">El mensaje</th>'
        '<th style="width:26mm">El tono</th><th>En palabras</th></tr></thead>'
        '<tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>El banco</b> — así se marca el tono en '
        'español, con palabras:</p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2mm 0 1mm"><b>Lo que se pierde sin emoji es…</b></p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>' % (filas, banco))


def _acabo_voy(r):
    """Twaalf scènes, twee zinnen per scène."""
    d = r["datos"]
    filas = "".join(
        '<tr><td style="font-size:9.2pt">%d</td><td class="fr">%s</td>'
        '<td><span class="wl md"></span></td><td><span class="wl md"></span></td></tr>'
        % (i, E(e)) for i, (e, _a, _b) in enumerate(d["escenas"], 1))
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<div class="prohib" style="display:inline-block">Prohibido el presente: «hay un vaso» no '
        'vale. Solo <b>acaba de</b> y <b>va a</b>.</div>'
        '<table class="wtab" style="width:100%%;margin-top:2.5mm"><thead><tr>'
        '<th style="width:8mm">#</th><th>La escena</th>'
        '<th style="width:42mm">Acaba de…</th><th style="width:42mm">Y ahora va a…</th>'
        '</tr></thead><tbody>%s</tbody></table>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>La escena más difícil ha sido la n.º</b> '
        '<span class="wl sm"></span> <b>, porque…</b></p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>' % (filas, marco))


def _notificacion(r):
    """De vijf alarmsignalen, het valse bericht en het ontmaskerende."""
    d = r["datos"]
    sen = "".join(
        '<tr><td class="fr"><b>%s</b></td><td style="font-size:9.4pt">%s</td>'
        '<td style="text-align:center">☐</td></tr>' % (E(n), E(por))
        for n, por in d["senales"])
    mf = "".join('<span>%s</span>' % E(m) for m in d["marco_falso"])
    ma = "".join('<span>%s</span>' % E(m) for m in d["marco_aviso"])
    return (
        '<div class="prohib" style="display:inline-block">Sin marcas reales, sin enlaces reales, '
        'sin números reales. Es un modelo, no un cebo.</div>'
        '<table class="wtab" style="width:100%%;margin-top:2.5mm"><thead><tr>'
        '<th style="width:38mm">La señal</th><th>Por qué funciona</th>'
        '<th style="width:20mm">¿La usáis?</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>1 · El mensaje falso</b> (usted, '
        'imperativo, las cinco señales dentro):</p>'
        '<div class="tira">%s</div>'
        '<div class="wbox" style="height:44mm"></div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>2 · El mensaje que lo desmonta</b> (tú, '
        'señal por señal):</p>'
        '<div class="tira">%s</div>'
        '<div class="wbox" style="height:44mm"></div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm">Señales nombradas en el segundo mensaje: '
        '<span class="wl sm"></span> de 5</p>' % (sen, mf, ma))

def _sellos(r):
    """Acht paspoortstempels om te ordenen, met de por/para-kolommen."""
    d = r["datos"]
    sellos = "".join(
        '<div class="ficha fid"><b>%s</b><span>%s</span><span class="fl">%s</span></div>'
        % (E(f), E(lug), E(tipo)) for f, lug, tipo, _pista in d["sellos"])
    raz = "".join('<span>%s</span>' % E(x) for x in d["razones"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    filas = "".join(
        '<tr><td style="font-size:9.4pt">%d</td><td><span class="wl md"></span></td>'
        '<td><span class="wl md"></span></td><td><span class="wl md"></span></td></tr>'
        % i for i in range(1, 7))
    return (
        '<div class="rol">🛂 Ocho sellos, sin una sola explicación</div>'
        '<div class="fichas f4">%s</div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Las razones posibles</b> — no todas se usan:</p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2mm 0 1mm"><b>La ruta.</b> Por etapa: por dónde pasó, '
        'y para qué. <span class="gloss">Per etappe: waarlangs, en waarvoor.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>Etapa</th><th>Pasó por… (la vía)</th><th>Fue para… (el objetivo)</th>'
        '</tr></thead><tbody>%s</tbody></table>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Los sellos de puro tránsito son</b> '
        '<span class="wl md"></span> &nbsp;·&nbsp; <b>y el que no encaja es</b> '
        '<span class="wl sm"></span> <b>, porque</b> <span class="wl md"></span></p>'
        % (sellos, raz, filas, marco))


def _resena_hostal(r):
    """Acht neutrale feiten, twee recensies."""
    d = r["datos"]
    datos = "".join('<tr><td style="text-align:center;font-size:9pt;color:var(--mut)">%d</td>'
                    '<td class="fr">%s</td><td style="text-align:center">☐ ☐</td></tr>'
                    % (i, E(x)) for i, x in enumerate(d["datos"], 1))
    mb = "".join('<span>%s</span>' % E(m) for m in d["marco_bien"])
    mm = "".join('<span>%s</span>' % E(m) for m in d["marco_mal"])
    return (
        '<div class="decl"><b>%s</b><span>Ocho datos. Ni uno se puede omitir.</span></div>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>El dato</th><th style="width:26mm">★★★★★ / ★</th></tr></thead>'
        '<tbody>%s</tbody></table>'
        '<p style="font-size:9.4pt;margin:1.5mm 0 0;color:var(--mut)">Marca las dos casillas '
        'cuando el dato esté en las dos reseñas.</p>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>★★★★★ · el viajero contento</b></p>'
        '<div class="tira">%s</div><div class="wbox" style="height:40mm"></div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>★ · el viajero descontento</b></p>'
        '<div class="tira">%s</div><div class="wbox" style="height:40mm"></div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>La palabra que hace todo el trabajo es</b> '
        '<span class="wl md"></span> &nbsp;·&nbsp; ¿cuál de las dos es verdad? '
        '<span class="wl md"></span></p>'
        % (E(d["hostal"]), datos, mb, mm))


def _turismo(r):
    """Cijfers over overtoerisme plus vier stemmen."""
    d = r["datos"]
    filas = "".join(
        '<tr><td class="fr"><b>%s</b></td><td style="font-size:9.4pt">%s</td>'
        '<td style="font-size:9.4pt">%s</td><td style="font-size:9pt;color:var(--mut)">%s</td></tr>'
        % (E(c), E(h), E(v), E(x)) for c, h, v, x in d["tabla"])
    voces = "".join('<div class="decl"><b>%s</b><span>%s</span></div>' % (E(q), E(t))
                    for q, t in d["voces"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:44mm">Dónde</th>'
        '<th style="width:40mm">Habitantes</th><th style="width:44mm">Visitantes</th>'
        '<th>Y además</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.4pt;margin:1.5mm 0 0;color:var(--mut)">Cifras redondeadas de '
        'fuentes públicas.</p>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Visitantes por habitante y año:</b> '
        'Barcelona <span class="wl sm"></span> · Cusco <span class="wl sm"></span></p>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Cuatro voces</b> — ninguna miente:</p>%s'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Tu postura en tres frases,</b> cada una '
        'con una cifra. Una de las tres da la razón al otro lado:</p>'
        '<div class="tira">%s</div>%s' % (filas, voces, marco, _lineas(3, "wl full")))


def _bingo(r):
    """Bingokaart met twaalf ervaringen + de verplichte doorvraag."""
    d = r["datos"]
    cas = "".join(
        '<div class="wcol"><div class="ch" style="font-size:8.4pt">%s</div>'
        '<div style="padding:2mm;font-size:8.4pt;color:var(--mut)">firma:</div>'
        '<div class="cb short"></div></div>' % E(c) for c in d["casillas"])
    extra = "".join('<span>%s</span>' % E(x) for x in d["extra"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<p style="font-size:9.8pt;margin:0 0 1mm"><b>Una persona, una casilla.</b> Y en cada '
        'casilla, además de la firma, la respuesta a tu pregunta extra. '
        '<span class="gloss">Eén persoon, één vakje — plus het antwoord op je doorvraag.</span></p>'
        '<div class="tira">%s</div>'
        '<div class="wcols" style="grid-template-columns:repeat(4,1fr)">%s</div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Tus preguntas extra</b> — siempre en '
        'perfecto:</p><div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>La mejor historia que has oído hoy:</b></p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>' % (marco, cas, extra))


def _linea_saboteada(r):
    """Acht feiten door elkaar; twee zijn vals."""
    d = r["datos"]
    # vaste, bewust gekozen volgorde: door elkaar maar elke druk identiek
    orden = [4, 0, 6, 2, 7, 1, 5, 3]
    filas = "".join(
        '<tr><td style="text-align:center;font-size:9pt;color:var(--mut)">%s</td>'
        '<td style="font-size:9.6pt"><b>%s</b></td><td class="fr">%s</td>'
        '<td><span class="wl sm"></span></td><td style="text-align:center">☐</td></tr>'
        % (chr(65 + k), E(d["hechos"][i][0]), E(d["hechos"][i][1]))
        for k, i in enumerate(orden))
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<div class="rol">🗓️ Ocho hechos, desordenados</div>'
        '<p style="font-size:9.6pt;margin:0 0 1.5mm">En la cuarta columna, el orden (1–8). En la '
        'quinta, marca si crees que es falso. <span class="gloss">Vierde kolom: de volgorde. '
        'Vijfde: aankruisen wat vals is.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm"></th>'
        '<th style="width:16mm">Año</th><th>El hecho</th>'
        '<th style="width:18mm">Orden</th><th style="width:18mm">¿Falso?</th>'
        '</tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Los dos falsos, con el hecho que los '
        'delata:</b> <span class="gloss">De twee valse, met het feit waarmee ze botsen.</span></p>'
        '<div class="tira">%s</div>%s'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>La línea del tiempo definitiva,</b> en '
        'tres frases con conectores:</p>%s'
        % (filas, marco, _lineas(2, "wl full"), _lineas(3, "wl full")))


def _museo(r):
    """Vijf bijschriften van drie regels, met de zaalplattegrond."""
    d = r["datos"]
    fig = "".join('<div class="ficha fid"><b>%s</b><span class="fl">%s</span>'
                  '<span>☐ la elegimos</span></div>' % (E(n), E(s)) for n, s in d["figuras"])
    tipos = "".join('<span>%s</span>' % E(t) for t in d["tipos_objeto"])
    cart = "".join(
        '<div class="wcol"><div class="ch">Objeto %d</div>'
        '<div style="padding:2mm 2.5mm;font-size:8.4pt;color:var(--mut);line-height:2.4">'
        'Qué es:<br>Año:<br>En … ,</div><div class="cb"></div></div>' % i
        for i in range(1, 6))
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco_cartela"])
    return (
        '<p style="font-size:9.8pt;margin:0 0 1mm"><b>Elegid vuestra figura:</b></p>'
        '<div class="fichas f4">%s</div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Cinco tipos de objeto</b> — uno de cada:</p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:1.5mm 0 1mm"><b>La cartela</b>: tres líneas, y la '
        'tercera siempre en indefinido.</p>'
        '<div class="tira">%s</div>'
        '<div class="wcols" style="grid-template-columns:repeat(5,1fr)">%s</div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>El plano de la sala.</b> ¿Por dónde entra '
        'el visitante y en qué orden ve los objetos?</p>'
        '<div class="wbox" style="height:38mm"></div>' % (fig, tipos, marco, cart))


def _dos_versiones(r):
    """Twee versies naast elkaar + de scheiding feit/interpretatie."""
    d = r["datos"]
    a = "".join('<tr><td style="font-size:9pt;color:var(--mut)">%d</td><td class="fr">%s</td>'
                '<td style="text-align:center">☐</td></tr>' % (i, E(x))
                for i, x in enumerate(d["version_a"], 1))
    b = "".join('<tr><td style="font-size:9pt;color:var(--mut)">%d</td><td class="fr">%s</td>'
                '<td style="text-align:center">☐</td></tr>' % (i, E(x))
                for i, x in enumerate(d["version_b"], 1))
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<p style="font-size:9.8pt;margin:0 0 1.5mm">Marca ☐ lo que dicen <b>las dos</b> versiones. '
        'Lo demás es una afirmación, no un hecho. <span class="gloss">Kruis aan wat in béide '
        'staat. De rest is een bewering.</span></p>'
        '<div class="rol">📰 Versión A · el boletín municipal</div>'
        '<table class="wtab" style="width:100%%"><tbody>%s</tbody></table>'
        '<div class="rol" style="margin-top:3mm">🗞️ Versión B · el periódico de la comarca</div>'
        '<table class="wtab" style="width:100%%"><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Los tres hechos seguros:</b></p>%s'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Dos interpretaciones,</b> y por qué lo son:</p>'
        '<div class="tira">%s</div>%s'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Algo que solo dice una versión y aun '
        'así puede ser verdad:</b> <span class="wl md"></span></p>'
        % (a, b, _lineas(3, "wl full"), marco, _lineas(2, "wl full")))


def _bio_datos(r):
    """Acht cijfers, een tijdlijn en vijf indefinido-zinnen."""
    d = r["datos"]
    filas = "".join('<tr><td class="fr">%s</td><td style="text-align:right"><b>%s</b></td></tr>'
                    % (E(k), E(v)) for k, v in d["cifras"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<div class="prohib" style="display:inline-block">Prohibidos los adjetivos: nada de '
        '«grande», «famoso» ni «importante». Las cifras hablan solas.</div>'
        '<table class="wtab" style="width:100%%;margin-top:2.5mm"><thead><tr>'
        '<th>El dato</th><th style="width:26mm;text-align:right">Cuánto</th></tr></thead>'
        '<tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>La línea del tiempo.</b> Marca los años '
        'que puedes deducir:</p>'
        '<div class="wbox" style="height:34mm"></div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Cinco frases: una cifra, un indefinido, '
        'cero adjetivos.</b></p>'
        '<div class="tira">%s</div>%s'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>La cifra que dice más que las otras es</b> '
        '<span class="wl sm"></span> <b>, porque</b> <span class="wl md"></span></p>'
        % (filas, marco, _lineas(5, "wl full")))

def _foto_1998(r):
    """Twaalf zinnen classificeren: achtergrond of feit."""
    d = r["datos"]
    filas = "".join(
        '<tr><td style="font-size:9.2pt">%d</td><td class="fr">%s</td>'
        '<td style="text-align:center;font-size:9pt">☐ fondo ☐ hecho</td>'
        '<td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
        % (i, E(f)) for i, (f, _t, _v, _p) in enumerate(d["frases"], 1))
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<div class="rol">📷 Escuela primaria · curso 1997–1998</div>'
        '<p style="font-size:9.6pt;margin:0 0 1.5mm"><b>Fondo</b> = cómo era todo · <b>hecho</b> = '
        'lo que pasó ese día. <span class="gloss">Achtergrond = hoe alles was · feit = wat er die '
        'dag gebeurde.</span></p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>La frase</th><th style="width:30mm">¿Qué es?</th>'
        '<th style="width:24mm">La forma</th><th style="width:38mm">¿Por qué?</th>'
        '</tr></thead><tbody>%s</tbody></table>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Dos frases caben en las dos.</b> '
        '¿Cuáles, y qué cambia el significado?</p>%s'
        % (filas, marco, _lineas(2, "wl full")))


def _tres_infancias(r):
    """Drie kindertijden in kolommen + vier vergelijkingen."""
    d = r["datos"]
    filas = "".join(
        '<tr><td style="font-size:9.2pt;color:var(--mut)"><b>%s</b></td>'
        '<td class="fr">%s</td><td class="fr">%s</td><td class="fr">%s</td></tr>'
        % (E(a), E(c1), E(c2), E(c3)) for a, c1, c2, c3 in d["tabla"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:38mm"></th>'
        '<th>Cusco 🇵🇪</th><th>Cartagena 🇨🇴</th><th>Gante 🇧🇪</th></tr></thead>'
        '<tbody>%s</tbody></table>'
        '<p style="font-size:9.4pt;margin:1.5mm 0 0;color:var(--mut)">Los años noventa, no hoy.</p>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Cuatro comparaciones,</b> cada una con un '
        'dato de la tabla. Una tiene que ir en contra de lo que esperabais:</p>'
        '<div class="tira">%s</div>%s'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Y en esto se parecen los tres sitios:</b></p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>'
        % (filas, marco, _lineas(4, "wl full")))


def _cuento(r):
    """Verhaalbegin + schrijfvlak voor de voortzetting."""
    d = r["datos"]
    ini = "".join('<div style="margin:1.4mm 0;font-size:10pt">%s</div>' % E(x)
                  for x in d["principio"])
    bf = "".join('<span>%s</span>' % E(v) for v in d["banco_fondo"])
    bh = "".join('<span>%s</span>' % E(v) for v in d["banco_hecho"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<div class="rol">📖 El principio · subrayad fondo y hecho</div>'
        + ini +
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Fondo</b> (imperfecto):</p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:0 0 1mm"><b>Hecho</b> (indefinido):</p>'
        '<div class="tira">%s</div>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2mm 0 1mm"><b>Vuestras diez líneas.</b> Mínimo tres de '
        'fondo y tres de hecho, mezclados:</p>'
        '<div class="wbox" style="height:62mm"></div>'
        '<div class="pliegue">✂ Aquí se corta y se pasa al grupo de al lado</div>'
        '<p style="font-size:9.8pt;margin:1mm 0 1mm"><b>El final, escrito por el otro grupo:</b></p>'
        '<div class="wbox" style="height:38mm"></div>' % (bf, bh, marco))


def _nostalgia(r):
    """Nostalgische tekst over iets dat slechter was."""
    d = r["datos"]
    temas = "".join(
        '<div class="ficha fid"><b>%s</b><span class="fl">%s</span>'
        '<span>☐ lo elegimos</span></div>' % (E(t), E(x)) for t, x in d["temas"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    prohib = "".join('<span class="prohib" style="font-size:8.6pt">%s</span>' % E(x)
                     for x in d["prohibido"])
    return (
        '<div class="fichas f3">%s</div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Tu marco</b> — todo en imperfecto, todo '
        'positivo:</p><div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:1.5mm 0 1mm"><b>Y nada de esto:</b></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2mm 0 1mm"><b>Ocho frases nostálgicas:</b></p>%s'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm">Imperfectos usados: '
        '<span class="wl sm"></span> de 8 &nbsp;·&nbsp; ¿alguien ha notado que era broma? '
        '☐ sí ☐ no</p>' % (temas, marco, prohib, _lineas(8, "wl full")))


def _consejo(r):
    """Advies herschrijven van bevel naar aanbod."""
    d = r["datos"]
    sit = "".join(
        '<tr><td style="text-align:center;font-size:9pt;color:var(--mut)">%d</td>'
        '<td class="fr">%s</td><td style="font-size:9pt;color:var(--gd)">%s</td>'
        '<td style="text-align:center">☐</td></tr>' % (i, E(s), E(t))
        for i, (s, t) in enumerate(d["situaciones"], 1))
    suaves = "".join('<span>%s</span>' % E(x) for x in d["suaves"])
    prohib = "".join('<span class="prohib" style="font-size:8.6pt">%s</span>' % E(x)
                     for x in d["prohibido"])
    return (
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>La situación</th><th style="width:26mm">El tema</th>'
        '<th style="width:20mm">La elegimos</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Paso 1 — el consejo directo.</b> Escríbelo '
        'tal cual sale. <span class="gloss">Schrijf het zoals het eruit komt — het mág belerend '
        'klinken.</span></p>'
        '<div style="margin:1mm 0"><span class="wl full"></span></div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Prohibido en la versión final:</b></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:0 0 1mm"><b>Las fórmulas suaves</b> — dos imperativos, '
        'pero amables:</p><div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2mm 0 1mm"><b>Paso 2 — el consejo que sí se acepta,</b> '
        'en cinco frases:</p>%s'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm">Imperativos: <span class="wl sm"></span> '
        'de 2 &nbsp;·&nbsp; ¿lo aceptaría tu compañero/a? ☐ sí ☐ no'
        % (sit, prohib, suaves, _lineas(5, "wl full")))


def _factcheck(r):
    """Vier beweringen beoordelen met «creo que»."""
    d = r["datos"]
    filas = "".join(
        '<tr><td style="font-size:9.2pt">%d</td><td class="fr">%s</td>'
        '<td style="text-align:center;font-size:9pt">☐ V ☐ F</td>'
        '<td><span class="wl lg"></span></td></tr>' % (i, E(a))
        for i, (a, _ok, _por) in enumerate(d["afirmaciones"], 1))
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    prohib = "".join('<span class="prohib" style="font-size:8.6pt">%s</span>' % E(x)
                     for x in d["prohibido"])
    return (
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th>La afirmación</th><th style="width:24mm">Veredicto</th>'
        '<th style="width:52mm">Creo que… porque…</th></tr></thead><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Ojo con la forma:</b> después de '
        '<b>creo que</b> va el indicativo — «creo que <u>es</u> verdad», «creo que <u>no es</u> '
        'verdad». <span class="gloss">Na «creo que» komt de indicativo.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:1.5mm 0 1mm"><b>No vale decir:</b></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2mm 0 1mm"><b>Para estar seguros, vamos a comprobar…</b> '
        '(¿qué, y dónde?)</p>%s' % (filas, marco, prohib, _lineas(2, "wl full")))


def _cartel(r):
    """Affiche van precies drie woorden."""
    d = r["datos"]
    temas = "".join('<span>%s</span>' % E(t) for t in d["temas"])
    ej = "".join(
        '<tr><td class="fr" style="font-size:11pt"><b>%s</b></td>'
        '<td style="font-size:9pt;color:var(--mut)">%s</td></tr>' % (E(x), E(por))
        for x, por in d["ejemplos"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    return (
        '<p style="font-size:9.8pt;margin:0 0 1mm"><b>Vuestro tema:</b></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:1.5mm 0 1mm"><b>Cuatro ejemplos</b> — uno de ellos '
        'incumple la regla. ¿Cuál? <span class="gloss">Eén ervan breekt de regel.</span></p>'
        '<table class="wtab" style="width:100%%"><tbody>%s</tbody></table>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Diez versiones.</b> Sí, diez — tachar es '
        'la mitad del trabajo:</p>%s'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>El cartel definitivo</b> (tres palabras '
        'grandes) y la imagen:</p>'
        '<div class="wbox" style="height:56mm"></div>'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm">Palabras: <span class="wl sm"></span> '
        '(tiene que ser 3) &nbsp;·&nbsp; ¿cuál es el imperativo? <span class="wl sm"></span> '
        '&nbsp;·&nbsp; ¿se entiende sin explicación? ☐ sí ☐ no</p>'
        % (temas, ej, _lineas(10, "wl md"), marco))


def _manifiesto(r):
    """Tien engagementen, tien conectoren, één per stuk."""
    d = r["datos"]
    con = "".join('<span>☐ <b>%s</b></span>' % E(c) for c in d["conectores"])
    ej = "".join('<div class="decl"><span>%s</span></div>' % E(x)
                 for x in d["ejemplos_compromiso"])
    marco = "".join('<span>%s</span>' % E(m) for m in d["marco"])
    filas = "".join(
        '<tr><td style="font-size:9.4pt">%d</td><td><span class="wl sm"></span></td>'
        '<td><span class="wl full"></span></td></tr>' % i for i in range(1, 11))
    return (
        '<p style="font-size:9.8pt;margin:0 0 1mm"><b>Los diez conectores.</b> Cada uno exactamente '
        'una vez — marcadlos según los uséis. <span class="gloss">Elk precies één keer; vink af '
        'terwijl je schrijft.</span></p>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:2mm 0 1mm"><b>Así suena un compromiso concreto:</b></p>%s'
        '<p style="font-size:9.8pt;margin:2.5mm 0 1mm"><b>Vuestros diez compromisos.</b> En la '
        'segunda columna, el conector que usáis:</p>'
        '<table class="wtab" style="width:100%%"><thead><tr><th style="width:8mm">#</th>'
        '<th style="width:26mm">Conector</th><th>El compromiso</th></tr></thead>'
        '<tbody>%s</tbody></table>'
        '<div class="tira">%s</div>'
        '<p style="font-size:9.8pt;margin:3mm 0 1mm"><b>Firmado por la clase de</b> '
        '<span class="wl sm"></span> <b>, el</b> <span class="wl sm"></span> <b>de</b> '
        '<span class="wl sm"></span> <b>de 20</b><span class="wl sm"></span></p>'
        '<div class="wbox" style="height:26mm"></div>' % (con, ej, filas, marco))

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
             "C5-U6-RETO-05": _moda_circular, "C5-U6-RETO-07": _escaparate,
             "C5-U7-RETO-01": _plano, "C5-U7-RETO-02": _mudanza,
             "C5-U7-RETO-04": _capas, "C5-U7-RETO-06": _robot,
             "C5-U8-RETO-01": _maleta, "C5-U8-RETO-04": _diario,
             "C5-U8-RETO-05": _machu, "C5-U8-RETO-08": _balance,
             "C6P-U0-RETO-01": _test_falso, "C6P-U0-RETO-02": _quien_es_quien,
             "C6P-U0-RETO-04": _lenguas, "C6P-U0-RETO-05": _adjetivos_sitio,
             "C6P-U1-RETO-01": _turno_noche, "C6P-U1-RETO-03": _agenda,
             "C6P-U1-RETO-05": _diario_objeto, "C6P-U1-RETO-09": _sustituto,
             "C6P-U2-RETO-01": _casa_crimen, "C6P-U2-RETO-04": _metros,
             "C6P-U2-RETO-06": _cuarto_sin, "C6P-U2-RETO-10": _mudanza_etapas,
             "C6P-U3-RETO-01": _hilo, "C6P-U3-RETO-05": _sin_emoji,
             "C6P-U3-RETO-07": _acabo_voy, "C6P-U3-RETO-10": _notificacion,
             "C6P-U4-RETO-02": _sellos, "C6P-U4-RETO-04": _resena_hostal,
             "C6P-U4-RETO-09": _turismo, "C6P-U4-RETO-10": _bingo,
             "C6P-U5-RETO-02": _linea_saboteada, "C6P-U5-RETO-04": _museo,
             "C6P-U5-RETO-08": _dos_versiones, "C6P-U5-RETO-09": _bio_datos,
             "C6P-U6-RETO-01": _foto_1998, "C6P-U6-RETO-04": _tres_infancias,
             "C6P-U6-RETO-05": _cuento, "C6P-U6-RETO-07": _nostalgia,
             "C6P-U7-RETO-01": _consejo, "C6P-U7-RETO-04": _factcheck,
             "C6P-U7-RETO-05": _cartel, "C6P-U7-RETO-10": _manifiesto}


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
