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


_MATERIAL = {"C5-U0-RETO-03": _gps, "C5-U0-RETO-08": _numeros, "C5-U0-RETO-10": _pasaporte}


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
