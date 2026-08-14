#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de print-HTML C6plus_U4.html (C6+ · Unidad 4 «De viaje») → PDF via Chromium.
# Zelfde componentenkit/CSS als de gelockte golden sample C6+·U0–U3 (geïmporteerd uit gen_u0_print).
# Cursuskleur = paars. Parada 4 = Chile (el gran viaje).
# Kerngrammatica: pretérito perfecto compuesto (haber + participio) · por/para (intro).
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/01-cursussen/06-vervolg/U0")
import gen_u0_print as U0
from gen_u0_print import (CSS, AV, TU, MOCH, audiorow, act, regla, guide, lpd, divider,
                          pcard, steun, sortcols, actx, tarea_com, obsbox, machine, blocks, tree,
                          mirror, fmu, scaffold, zoom, clusters, colloc, scale, vpairs, mispal, xray,
                          gustobars, menu)
import sys as _sys
_sys.path.insert(0, "/home/user/espa-ol-en-la-pr-ctica/03-build/web")
import qr_print as QRP; QRP.fijar("C6+", 4)
from qr_print import qr
import print_bloques as PB
import lectura_data as LD
import escucha_data as ED
import retos_data as RD
import retos_print as RP

BODY = []
def P(*x): BODY.extend(x)


def retos(ancla, titulo, intro_es, intro_nl):
    """Retoblok van één sectie — volledige oefening voor print, verwijskaartje
    voor wat op de hub of in de PowerPoint leeft."""
    P('<div class="page">')
    P(f'<div class="divider">{titulo}</div>')
    P(f'<div class="intro" style="margin-top:1mm"><b>ES:</b> {intro_es} '
      f'<span class="gloss">{intro_nl}</span></div>')
    for r in sorted(RD.por_ancla(ancla), key=lambda x: x["num"]):
        P(RP.reto_print(r) if r["soporte"] == "print" else RP.reto_puntero(r))
    P('</div>')

_AN = [0]
def AN():
    _AN[0] += 1
    return str(_AN[0])

def sec_open(num, pk, intro, lpd_html=None):
    P('<div class="page"><div class="parada sec">')
    P(f'<span class="num">{num}</span><span class="pk">{pk}</span>')
    P(f'<div class="intro"><b>ES:</b> {intro}</div>')
    if lpd_html:
        P(lpd_html)
    P('</div>')
def sec_close():
    P('</div>')

# ---------- OPENER ----------
P(f'''
<div class="hero">
  <div class="tab">U4 · DE VIAJE</div>
  <div class="eyebrow">UNIDAD 4 · LA RUTA · CHILE 🇨🇱 · DE VIAJE ✈️</div>
  <h1>De viaje</h1>
  <div class="sub">El viaje sigue hacia el sur: <b>Chile</b> y todo el mundo hispano. Aprendes a hablar de <b>experiencias recientes</b> con el <b>pretérito perfecto compuesto</b> (<b>he estado</b> en Perú, <b>he visto</b> la catedral), los <b>participios</b> y los marcadores del perfecto. <span class="gloss">Praten over wat je onlangs gedaan hebt.</span></div>
  <div class="q">¿Has viajado alguna vez a un país hispano? <span style="font-weight:400;opacity:.9">· Ben je ooit naar een Spaanstalig land gereisd?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U1 · El día a día</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U2 · Aquí vivo</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U3 · Conectados</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U4 · De viaje</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U5 · Érase una vez</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U6–U7 · el pasado</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 4 · Chile 🇨🇱 y el gran viaje.</b> Bajamos al sur: el <b>desierto de Atacama</b>, la <b>Patagonia</b> y la isla de <b>Rapa Nui</b>. Toda la cast cuenta <b>dónde ha estado</b> y <b>qué ha visto</b>. <span class="gloss">We zakken af naar het zuiden: de Atacama-woestijn, Patagonië en Paaseiland. De hele cast vertelt waar ze zijn geweest.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> Todos <b>han hecho</b> un viaje. Aprendes a contar <b>qué has hecho</b> hoy, esta semana o alguna vez: <i>he viajado, he probado la comida, he sacado fotos</i>. Distingues <b>por</b> (medio, duración: por avión, por dos días) de <b>para</b> (destino, objetivo: para Chile, para descansar). Al final: escribes sobre <b>tu mejor viaje</b>.
      <span class="gloss">Iedereen heeft een reis gemaakt. Je leert vertellen wat je (ooit/vandaag) gedaan hebt, en het verschil tussen por en para. Eindtaak: over je mooiste reis schrijven.</span></div>
      <div class="ojo"><b>¡Ojo! — dos trampas desde el primer día:</b> ① El <b>perfecto</b> es <b>haber</b> (he/has/ha…) + <b>participio</b>. ¡<b>haber</b> no es <i>tener</i>! (<i>he comido</i>, no <span class="trap">tengo comido</span>). ② Algunos participios son <b>irregulares</b>: hecho, visto, dicho, escrito, vuelto. <span class="gloss">Het hulpwerkwoord is haber, en een paar deelwoorden zijn onregelmatig.</span></div>
    </div>
    <div>
      <div class="se">La gente de la ruta</div>
      <div class="cast">
        <div class="pc"><div class="avw">{AV["lucia"]}</div><div class="nm">Lucía</div><div class="fr">Sevilla 🇪🇸</div></div>
        <div class="pc"><div class="avw">{AV["diego"]}</div><div class="nm">Diego</div><div class="fr">CDMX 🇲🇽</div></div>
        <div class="pc"><div class="avw">{AV["valen"]}</div><div class="nm">Valen</div><div class="fr">Cartagena 🇨🇴</div></div>
        <div class="pc"><div class="avw">{AV["nina"]}</div><div class="nm">Nina</div><div class="fr">Cusco 🇵🇪</div></div>
        <div class="pc tu"><div class="avw">{TU}</div><div class="nm">Tú</div><div class="fr">Flandes 🇧🇪</div></div>
      </div>
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila viajera</span><br><span class="gloss" style="font-size:8.5pt">Vul je rugzak met de reiswoorden: el billete, la maleta, el hotel, he estado, he visto, por/para — alles voor het grote reisverhaal.</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">hablar de transporte y alojamiento</span> (el avión, el hotel) <span class="nl">over vervoer & verblijf praten</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">contar experiencias recientes</span> con <b>el perfecto</b> (he viajado, he visto) <span class="nl">recente ervaringen vertellen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar los participios</span> regulares e irregulares (hecho, visto) <span class="nl">de deelwoorden gebruiken</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">distinguir <b>por</b> y <b>para</b></span> (por avión / para Chile) <span class="nl">por en para onderscheiden</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">dar tu opinión</span> sobre un viaje (lo mejor ha sido…) <span class="nl">een mini-mening geven</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">crear tu <b>«Mi mejor viaje»</b></span> <span class="nl">reisblog (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>Transporte</span><span><b>§2</b>Perfecto</span><span><b>§3</b>Por/para</span><span><b>§4</b>Experiencias</span><span><b>§5</b>Lectura</span><span><b>Taller</b>h · acentos</span><span><b>Cultura</b>El gran viaje</span><span><b>Tarea</b>Mi viaje</span><span><b>Repaso</b>Semáforo</span>
    </div>
  </div>
  <div class="se" style="margin-top:8mm">Cómo trabajar esta unidad · leeswijzer</div>
  <div class="fams" style="margin-top:2mm">
    <div class="pcard"><div class="t" style="font-size:10.5pt">Las etiquetas de cada actividad</div>
      <div class="ej" style="margin-top:2mm"><span class="badge skill">👂 Escuchar</span> <span class="badge skill">🎙️ Hablar</span> <span class="badge skill">🔍 Analizar</span> <span class="badge">👤 Solo</span> <span class="badge">👥 En parejas</span> <span class="badge">± 5 min</span> <span class="stars">★★☆</span></div>
      <div class="anchor gloss" style="margin-top:2mm">Elke oefening toont de <b>vaardigheid</b>, de <b>werkvorm</b>, de <b>tijd</b> en de <b>moeilijkheid</b>.</div></div>
    <div class="pcard"><div class="t" style="font-size:10.5pt">El apoyo baja poco a poco</div>
      <div class="ej" style="margin-top:2mm">Un ejemplo hecho → las palabras que necesitas → una frase para completar
      → solo la primera letra → nada.</div>
      <div class="anchor" style="margin-top:2mm">La ayuda baja escalón a escalón hasta que escribes tú solo/a.
      <span class="gloss">De steun bouwt af: voorbeeld → woordenbank → zin om aan te vullen → eerste letter → zonder hulp.</span></div></div>
  </div>
</div>
''')

# ================= §0 · ¡PONTE AL DÍA! =================
sec_open("0", "§0 · ¡Ponte al día!", 'Activamos dos cosas: el <b>presente</b> de los verbos más frecuentes (los vas a necesitar como participio) y <b>ir a + infinitivo</b> (U3), porque un viaje también tiene planes. <span class="gloss">We frissen het presente en ir a + infinitivo op; die heb je nodig voor de reis.</span>',
        lpd(("8","taalsysteem: presente/ir a (repaso)"), ("7","woordenschat")))
P('<div class="truc"><b>Repaso → perfecto (U4):</b> ya conoces el presente. En U4 llega el <b>pretérito perfecto</b>: <b>haber</b> (he/has/ha…) + <b>participio</b>. <i>Como paella → <b>He comido</b> paella.</i> Es tu <b>primer pasado</b>, el puente hacia U5 y U6. <span class="gloss">Je eerste verleden tijd — de brug naar U5 en U6.</span></div>')
P(actx(AN(), "Presente · verbos del viaje (repaso)",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Vervoeg in de tegenwoordige tijd.</p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl sm"></span> (viajar) mucho. &nbsp; 2. Nosotros <span class="wl sm"></span> (visitar) el museo.<br>'
  '3. ¿Tú <span class="wl sm"></span> (hacer) la maleta? &nbsp; 4. El tren <span class="wl sm"></span> (salir) a las ocho.<br>'
  '5. Yo <span class="wl sm"></span> (volver, o→ue) el domingo. &nbsp; 6. Ellos <span class="wl sm"></span> (ver) la costa.</p>',
  apoyo="Banco de palabras: viajar · visitar · hacer · salir · volver · ver"))
P(actx(AN(), "Mis planes de viaje · ir a + infinitivo (repaso)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>repaso U3.</i> Escribe dos planes de viaje con <b>ir a + infinitivo</b>. <span class="gloss">Twee reisplannen.</span></p>'
  '<p style="margin-left:12.5mm">Este verano voy a <span class="wl lg"></span><br>Primero vamos a <span class="wl md"></span> y luego a <span class="wl md"></span></p>',
  apoyo="Marco: Voy a viajar a… · Vamos a visitar… · Voy a probar…"))
sec_close()

# ================= §1 · TRANSPORTE Y ALOJAMIENTO =================
sec_open("1", "§1 · Transporte y alojamiento", 'El vocabulario del viaje: el <b>transporte</b> (el avión, el tren, el billete), el <b>alojamiento</b> (el hotel, la reserva, la llave) y los <b>lugares</b> (la playa, la montaña, el museo). <span class="gloss">De woorden van vervoer, verblijf en reisbestemmingen.</span>',
        lpd(("7","woordenschat: el viaje"), ("8","taalsysteem: género & artículos")))
P('<div class="se">El mundo del viaje <span class="gloss" style="font-size:8pt">— netwerk in clusters</span></div>')
P('<div class="clusters" style="grid-template-columns:1fr 1fr 1fr">'
  '<div class="clu"><div class="ch"><span class="ci">✈️</span>El transporte</div><ul><li>el avión · el tren</li><li>el autobús · el barco</li><li>el billete · el vuelo</li></ul><div class="ex">Compro un billete de tren.</div></div>'
  '<div class="clu"><div class="ch"><span class="ci">🏨</span>El alojamiento</div><ul><li>el hotel · el hostal</li><li>la habitación · la reserva</li><li>la llave · la recepción</li></ul><div class="ex">Reservo una habitación.</div></div>'
  '<div class="clu"><div class="ch"><span class="ci">🏖️</span>Los lugares</div><ul><li>la playa · la montaña</li><li>el museo · la ciudad</li><li>el desierto · la costa</li></ul><div class="ex">Vamos a la playa.</div></div></div>')
P('<div class="truc"><b>¡Ojo! el/la:</b> <b>el</b> avión, <b>el</b> tren, <b>el</b> billete, <b>el</b> hotel, <b>el</b> museo (m) · <b>la</b> maleta, <b>la</b> reserva, <b>la</b> llave, <b>la</b> playa, <b>la</b> montaña (v). <b>el equipaje</b> = onzijdig-klinkend maar m.</div>')
P(actx(AN(), "Relaciona la palabra con el lugar",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Une las dos columnas: escribe la letra. <span class="gloss">Verbind en schrijf de letter.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Palabra</div><div class="cb short">1. el billete &nbsp; 2. la llave &nbsp; 3. la maleta &nbsp; 4. el vuelo</div></div>'
  '<div class="wcol"><div class="ch">¿Dónde?</div><div class="cb short">a. el hotel &nbsp; b. el aeropuerto &nbsp; c. la estación &nbsp; d. hacer el equipaje</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "Clasifica: ¿transporte, alojamiento o lugar?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe cada palabra en su columna: <span class="gloss">zet elk woord in de juiste kolom</span> <span class="words"><b>el avión · el hotel · la playa · el tren · la reserva · la montaña · el billete · la habitación</b></span></p>'
  + sortcols([("Transporte",""),("Alojamiento",""),("Lugar","")], eigen=True), apoyo="Banco de palabras"))
P(actx(AN(), "¿el o la? · el género del viaje",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★☆☆"}],
  '<p>___ avión · ___ maleta · ___ billete · ___ reserva · ___ hotel · ___ playa · ___ museo · ___ llave</p>'
  '<p style="margin-left:12.5mm">1.<span class="wl sm"></span> 2.<span class="wl sm"></span> 3.<span class="wl sm"></span> 4.<span class="wl sm"></span> 5.<span class="wl sm"></span> 6.<span class="wl sm"></span> 7.<span class="wl sm"></span> 8.<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "El intruso · ¿qué palabra sobra?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★★☆"}],
  '<p>Tacha la palabra que no encaja y di por qué. <span class="gloss">Streep het vreemde woord door en zeg waarom.</span></p>'
  '<p style="margin-left:12.5mm">1. el avión · el tren · <b>la cama</b> · el barco → <span class="wl md"></span><br>'
  '2. el hotel · el hostal · la habitación · <b>la playa</b> → <span class="wl md"></span><br>'
  '3. la maleta · el billete · el equipaje · <b>el museo</b> → <span class="wl md"></span></p>',
  apoyo=""))
P(actx(AN(), "Mi viaje ideal · escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escribe tres frases: qué transporte, qué alojamiento y qué lugar eliges. <span class="gloss">Drie zinnen over jouw keuze.</span></p>'
  '<p style="margin-left:12.5mm">Viajo en <span class="wl md"></span> y me quedo en <span class="wl md"></span><br>Quiero visitar <span class="wl lg"></span></p>',
  apoyo="Marco: Quiero ir a… porque… · Allí voy a…"))
sec_close()

retos("viaje_c6p", "§1.4 · Retos — el viaje que empieza en el mostrador",
      'Un vuelo cancelado donde <b>los dos tenéis razón</b>, dos reseñas del mismo hostal con los <b>mismos ocho datos</b>, y una megafonía de estación.',
      'Een geannuleerde vlucht waarin jullie allebei gelijk hebben, twee recensies van dezelfde hostel met dezelfde acht gegevens, en een stationsomroep.')

# ================= §2 · PERFECTO COMPUESTO =================
sec_open("2", "§2 · El pretérito perfecto compuesto", 'Para <b>experiencias recientes</b> y para «lo que has hecho alguna vez»: <b>haber</b> (he/has/ha/hemos/habéis/han) + <b>participio</b> (-ado/-ido). <i>He viajado a Chile. ¿Has visto el mar?</i> <span class="gloss">De voltooide tijd: haber + deelwoord. Je eerste verleden tijd.</span>',
        lpd(("8","taalsysteem: perfecto compuesto"), ("7","woordenschat: experiencias"), ("3","spreken: ervaringen")))

# §2.1 el sistema
P('<h3>§2.1 · ¿Cómo funciona? — la máquina del perfecto</h3>')
P(obsbox([
  'Hoy <span class="hl">he desayunado</span> tarde y <span class="hl">he cogido</span> el tren.',
  'Este año <span class="hl">hemos viajado</span> mucho.',
  '¿<span class="hl">Has probado</span> alguna vez la comida chilena?',
], vragen='Welk klein woordje staat vóór élk werkwoord? En hoe eindigt het tweede deel? <span class="gloss">Kijk naar «he/has/ha…» + de -ado/-ido-vorm.</span>'))
P(machine([("haber → he/has/ha…","he"),("+ participio","he viajado")]))
P(regla("Regla · haber + participio", '<table class="conj" style="margin-top:1mm"><thead><tr><th>Persona</th><th>haber</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">he</td><td>He <b>viajado</b> a Chile.</td></tr>'
  '<tr><td class="p">tú</td><td class="v">has</td><td>¿Has <b>comido</b>?</td></tr>'
  '<tr><td class="p">él/ella</td><td class="v">ha</td><td>Ha <b>salido</b> el tren.</td></tr>'
  '<tr><td class="p">nosotros/as</td><td class="v">hemos</td><td>Hemos <b>visto</b> el mar.</td></tr>'
  '<tr><td class="p">vosotros/as</td><td class="v">habéis</td><td>¿Habéis <b>reservado</b>?</td></tr>'
  '<tr><td class="p">ellos/ellas</td><td class="v">han</td><td>Han <b>llegado</b> hoy.</td></tr></tbody></table>'
  '<p style="margin:2mm 0 0"><b>Participio:</b> -ar → <b>-ado</b> (viajar → viajado) · -er/-ir → <b>-ido</b> (comer → comido, salir → salido). <span class="gloss">🔴 haber ≠ tener: <i>he comido</i> (niet <span class="trap">tengo comido</span>). Het participio verandert nooit met de persoon.</span></p>'))
P(actx(AN(), "Forma el participio",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>vorm het (regelmatige) participio.</i></p>'
  '<p style="margin-left:12.5mm">viajar → <span class="wl sm"></span> &nbsp; comer → <span class="wl sm"></span> &nbsp; salir → <span class="wl sm"></span><br>'
  'visitar → <span class="wl sm"></span> &nbsp; beber → <span class="wl sm"></span> &nbsp; dormir → <span class="wl sm"></span></p>',
  apoyo="Modelo: -ado / -ido"))
P(actx(AN(), "La gran cloze · perfecto compuesto",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Escribe <b>haber + participio</b> (el infinitivo está entre paréntesis). <span class="gloss">Vul haber + deelwoord in.</span></p>'
  '<p style="margin-left:12.5mm">1. (Yo) <span class="wl md"></span> (viajar) a Chile. &nbsp; 2. ¿(Tú) <span class="wl md"></span> (comer) ya?<br>'
  '3. Nosotros <span class="wl md"></span> (visitar) el museo. &nbsp; 4. El avión <span class="wl md"></span> (llegar) tarde.<br>'
  '5. Mis amigos <span class="wl md"></span> (reservar) un hostal. &nbsp; 6. (Yo) <span class="wl md"></span> (dormir) mal.<br>'
  '7. ¿Vosotros <span class="wl md"></span> (sacar) fotos? &nbsp; 8. Valen <span class="wl md"></span> (subir) a la montaña.</p>',
  apoyo="Banco de palabras: he viajado · has comido · hemos visitado · ha llegado · han reservado · he dormido · habéis sacado · ha subido"))
P(actx(AN(), "Sustitución · cambia la persona",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Modelo: <b>Yo he viajado a Chile.</b> Vuelve a escribirla para cada persona. <span class="gloss">Herschrijf de modelzin per persoon.</span></p>'
  '<p style="margin-left:12.5mm">tú → <span class="wl md"></span> &nbsp; ella → <span class="wl md"></span> &nbsp; nosotros → <span class="wl md"></span> &nbsp; ellos → <span class="wl md"></span></p>',
  apoyo="Primera letra: has viajado…"))
P('</div>')

# §2.2 participios irregulares + cloze
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2.2 · Los participios irregulares</span>')
P('<div class="intro"><b>ES:</b> Algunos participios no siguen la regla y hay que aprenderlos: <b>hacer → hecho</b>, <b>ver → visto</b>, <b>decir → dicho</b>, <b>volver → vuelto</b>, <b>poner → puesto</b>, <b>escribir → escrito</b>, <b>abrir → abierto</b>, <b>romper → roto</b>. <span class="gloss">De onregelmatige deelwoorden — uit het hoofd leren.</span></div>')
P('</div>')
P('<table class="conj"><thead><tr><th>Infinitivo</th><th>Participio</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td>hacer</td><td class="v">hecho</td><td class="gloss">He hecho las maletas.</td></tr>'
  '<tr><td>ver</td><td class="v">visto</td><td class="gloss">¿Has visto el mar?</td></tr>'
  '<tr><td>decir</td><td class="v">dicho</td><td class="gloss">Me ha dicho la verdad.</td></tr>'
  '<tr><td>volver</td><td class="v">vuelto</td><td class="gloss">He vuelto hoy.</td></tr>'
  '<tr><td>poner</td><td class="v">puesto</td><td class="gloss">Ha puesto la maleta aquí.</td></tr>'
  '<tr><td>escribir</td><td class="v">escrito</td><td class="gloss">He escrito una postal.</td></tr>'
  '<tr><td>abrir</td><td class="v">abierto</td><td class="gloss">Han abierto el museo.</td></tr></tbody></table>')
P('<div class="truc"><b>¡Ojo, acentos!</b> Después de una vocal, la <b>i</b> lleva tilde: leer → <b>leído</b>, oír → <b>oído</b>, creer → <b>creído</b>, caer → <b>caído</b>. (viajar → viajado, sin tilde.) <span class="gloss">Na een klinker krijgt de i een accent.</span></div>')
P(actx(AN(), "Empareja: infinitivo ↔ participio",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Une cada verbo con su participio irregular. <span class="gloss">Verbind met het onregelmatige deelwoord.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Infinitivo</div><div class="cb short">1. hacer &nbsp; 2. ver &nbsp; 3. decir &nbsp; 4. volver &nbsp; 5. escribir</div></div>'
  '<div class="wcol"><div class="ch">Participio</div><div class="cb short">a. vuelto &nbsp; b. hecho &nbsp; c. escrito &nbsp; d. visto &nbsp; e. dicho</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span> 5-<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "Cloze · participios irregulares",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escribe <b>haber + participio irregular</b>. <span class="gloss">Vul haber + onregelmatig deelwoord in.</span></p>'
  '<p style="margin-left:12.5mm">1. (Yo) <span class="wl md"></span> (hacer) las maletas. &nbsp; 2. ¿(Tú) <span class="wl md"></span> (ver) la Patagonia?<br>'
  '3. Nosotros <span class="wl md"></span> (volver) del viaje. &nbsp; 4. (Yo) <span class="wl md"></span> (escribir) una postal.<br>'
  '5. El guía nos <span class="wl md"></span> (decir) la hora. &nbsp; 6. Han <span class="wl md"></span> (abrir) el museo.</p>',
  apoyo="Banco de palabras: he hecho · has visto · hemos vuelto · he escrito · ha dicho · abierto"))
P(actx(AN(), "Del infinitivo al perfecto · escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe la forma de yo del pretérito perfecto (ojo: regular o irregular). <span class="gloss">Schrijf de yo-vorm; let op regelmatig of niet.</span></p>'
  '<p style="margin-left:12.5mm">viajar → <span class="wl md"></span> &nbsp; hacer → <span class="wl md"></span> &nbsp; ver → <span class="wl md"></span><br>'
  'comer → <span class="wl md"></span> &nbsp; volver → <span class="wl md"></span> &nbsp; escribir → <span class="wl md"></span></p>',
  apoyo="Marco: he + participio"))
P('</div>')

# §2.3 practicar + tarea com
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2.3 · Practicar el perfecto</span>')
P('<div class="intro"><b>ES:</b> Ahora entrenamos: corregir, transformar del presente al perfecto y contar experiencias de verdad. <span class="gloss">Verbeteren, van presente naar perfecto, en echt over ervaringen praten.</span></div>')
P('</div>')
P(actx(AN(), "Clínica de errores · el perfecto",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Elke zin heeft één fout (haber, participio of volgorde). Verbeter.</p>'
  '<p style="margin-left:12.5mm">1. Yo tengo comido paella. → <span class="wl md"></span><br>'
  '2. Nosotros ha viajado a Perú. → <span class="wl md"></span><br>'
  '3. ¿Tú has ver el mar? → <span class="wl md"></span><br>'
  '4. Ella ha hacido la maleta. → <span class="wl md"></span></p>',
  apoyo="Pista: he comido · hemos · has visto · ha hecho"))
P(actx(AN(), "Transforma · presente → perfecto",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Pasa del presente al pretérito perfecto (hoy). <span class="gloss">Herschrijf naar de voltooide tijd.</span></p>'
  '<p style="margin-left:12.5mm">1. Viajo a Chile. → Hoy <span class="wl md"></span><br>'
  '2. Vemos la costa. → Hoy <span class="wl md"></span><br>'
  '3. Hago la maleta. → Ya <span class="wl md"></span></p>',
  apoyo="Primera letra: He viajado…"))
P(actx("★", "Tarea comunicativa · ¿qué has hecho hoy?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>Pregunta a tu compañero/a qué ha hecho hoy (¿qué has hecho hoy?) y contesta con <b>el pretérito perfecto</b>. Anota dos cosas. <span class="gloss">Vraag wat je buur vandaag deed; noteer twee dingen.</span></p>'
  '<p style="margin-left:12.5mm">— ¿Qué has hecho hoy? — <span class="wl lg"></span></p>'
  '<p style="margin-left:12.5mm">Mi compañero/a: 1. <span class="wl full"></span>2. <span class="wl full"></span></p>',
  apoyo="Marco: Hoy he… · Todavía no he… · ¿Y tú, has…?"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha «¿Qué tal el viaje?»</b> en la web (TTS): Nina cuenta su viaje. <b>1ª vez:</b> ¿adónde ha ido? · <b>2ª vez:</b> ¿qué ha hecho? Escribe los datos.</div>',
           qr("Escanea y escucha", "§2 · ¿Qué tal el viaje?", seed=401)))
P('</div>')

retos("perfecto_c6p", "§2.4 · Retos — lo que has hecho y lo que no",
      'Un bingo de experiencias donde <b>una firma no basta</b>, y un viaje que nunca hiciste contado como si sí.',
      'Een ervaringenbingo waar één handtekening niet volstaat, en een reis die je nooit maakte alsof je er was.')

# ================= §3 · POR / PARA =================
sec_open("3", "§3 · Por y para", '<b>para</b> = doel/bestemming (para Chile, para descansar) · <b>por</b> = middel/duur/reden (por avión, por dos días, por el mal tiempo). <span class="gloss">para = waarheen/waarvoor · por = waardoor/hoelang/waarmee.</span>',
        lpd(("8","taalsysteem: por/para"), ("7","woordenschat: el viaje")))

# §3.1 contraste
P('<h3>§3.1 · El contraste por ↔ para</h3>')
P(obsbox([
  'Salgo <span class="hl">para</span> Chile y viajo <span class="hl">por</span> avión.',
  'Estudio español <span class="hl">para</span> viajar.',
  'Me quedo <span class="hl">por</span> dos semanas.',
], vragen='¿Cuándo se usa «para» y cuándo «por»? ¿Qué va detrás? <span class="gloss">Wanneer para en wanneer por? Wat volgt erna?</span> <span class="gloss">para + doel/bestemming · por + middel/duur/reden.</span>'))
P('<div class="fams" style="margin-top:2mm">'
  '<div class="pcard"><div class="t" style="color:var(--voorw)">PARA — doel & bestemming</div>'
  '<div class="ej" style="margin-top:2mm"><b>bestemming:</b> Salgo <b>para</b> Chile.<br><b>doel:</b> Viajo <b>para</b> descansar.<br><b>ontvanger:</b> Es <b>para</b> ti.<br><b>deadline:</b> <b>para</b> el lunes.</div></div>'
  '<div class="pcard"><div class="t" style="color:var(--ww)">POR — middel, duur & reden</div>'
  '<div class="ej" style="margin-top:2mm"><b>middel:</b> <b>por</b> avión / tren.<br><b>duur:</b> <b>por</b> dos días.<br><b>reden:</b> <b>por</b> el mal tiempo.<br><b>doorheen:</b> paseo <b>por</b> la costa · <b>por</b> la mañana.</div></div></div>')
P(tree([
  '<b>¿Qué quieres decir?</b>',
  '¿doel / bestemming / «om te» + inf.? → <span class="yes">para</span> <span class="res">para Chile · para descansar</span>',
  '¿middel / hoelang / reden / doorheen? → <span class="yes">por</span> <span class="res">por avión · por dos días · por la playa</span>',
]))
P(actx(AN(), "¿por o para? · completa",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escribe <b>por</b> o <b>para</b>. <span class="gloss">Vul por of para in.</span></p>'
  '<p style="margin-left:12.5mm">1. Salgo <span class="wl sm"></span> Madrid mañana. &nbsp; 2. Viajo <span class="wl sm"></span> avión.<br>'
  '3. Estudio <span class="wl sm"></span> aprobar. &nbsp; 4. Me quedo <span class="wl sm"></span> tres días.<br>'
  '5. Este regalo es <span class="wl sm"></span> ti. &nbsp; 6. Paseamos <span class="wl sm"></span> la playa.<br>'
  '7. No salimos <span class="wl sm"></span> el mal tiempo. &nbsp; 8. La reserva es <span class="wl sm"></span> el lunes.</p>',
  apoyo="Pista: para · por · para · por · para · por · por · para"))
P(actx(AN(), "Clasifica: ¿por o para?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Clasifica las expresiones: <span class="gloss">sorteer de uitdrukkingen</span> <span class="words"><b>… Chile (bestemming) · … avión · … dos días · … descansar · … la mañana · … ti</b></span></p>'
  + sortcols([("para (doel/bestemming)",""),("por (middel/duur/…)","")], eigen=False), apoyo="Banco de palabras"))
P(actx(AN(), "Traduce · por / para",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>traducir (NL → ES).</i> Elige por o para. <span class="gloss">Vertaal en kies por of para.</span></p>'
  '<p style="margin-left:12.5mm">1. Ik vertrek naar Chile. → Salgo <span class="wl sm"></span> Chile.<br>'
  '2. Ik reis per trein. → Viajo <span class="wl sm"></span> tren.<br>'
  '3. Ik studeer om te reizen. → Estudio <span class="wl sm"></span> viajar.<br>'
  '4. Het is voor jou. → Es <span class="wl sm"></span> ti.</p>',
  apoyo=""))
P('</div>')

# §3.2 practicar + tarea com
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3.2 · Practicar por/para</span>')
P('<div class="intro"><b>ES:</b> Entrenamos con corrección y producción propia. <span class="gloss">Verbeteren en zelf produceren.</span></div>')
P('</div>')
P(actx(AN(), "Clínica de errores · por/para",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 3 min"},{"t":"★★★"}],
  '<p>Elke zin heeft één fout (por/para). Verbeter.</p>'
  '<p style="margin-left:12.5mm">1. Salgo por Chile mañana. → <span class="wl md"></span><br>'
  '2. Viajo para tren. → <span class="wl md"></span><br>'
  '3. Estudio por viajar. → <span class="wl md"></span><br>'
  '4. Me quedo para dos semanas. → <span class="wl md"></span></p>',
  apoyo="Pista: para · por · para · por"))
P(actx(AN(), "Completa tu viaje · por/para",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Complétalo con tu propio viaje. <span class="gloss">Vul aan met je eigen reis.</span></p>'
  '<p style="margin-left:12.5mm">Salgo para <span class="wl md"></span>. Viajo por <span class="wl md"></span>. Me quedo por <span class="wl md"></span>. Voy para <span class="wl md"></span>.</p>',
  apoyo="Marco: salgo para… · viajo por… · un billete para…"))
P(actx("★", "Tarea comunicativa · planificamos un viaje",
  [{"t":"🗣️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Planead juntos un viaje: adónde (para), en qué (por), cuánto tiempo (por) y para qué (para + infinitivo). Anotad el plan. <span class="gloss">Plan samen een reis en noteer het.</span></p>'
  '<p style="margin-left:12.5mm">Nuestro viaje: <span class="wl full"></span><span class="wl full"></span></p>',
  apoyo="Marco: Vamos a ir a… · Podemos… · Prefiero… porque…"))
P('<div class="guide"><div class="ic">🎡</div><div><span class="hand">Online:</span> <span class="g">de <b>por/para-schuifregelaar</b> en de spellen op de hub oefenen elk geval; + cloze en foutenkliniek.</span></div></div>')
P('</div>')

retos("por_para", "§3.4 · Retos — por dónde y para qué",
      'Ocho sellos sin explicación, seiscientos euros para diez días, y siete kilos para treinta días.',
      'Acht stempels zonder uitleg, zeshonderd euro voor tien dagen, en zeven kilo voor dertig dagen.')

# ================= §4 · EXPERIENCIAS Y LUGARES =================
sec_open("4", "§4 · Experiencias y lugares", 'Cuenta lo que has hecho <b>alguna vez</b> (o lo que <b>todavía no</b>): con <b>ya</b>, <b>todavía no</b>, <b>nunca</b>, <b>alguna vez</b>. <i>¿Has estado alguna vez en Perú? — Todavía no.</i> <span class="gloss">Ervaringen met ya, todavía no, nunca en alguna vez.</span>',
        lpd(("7","woordenschat: lugares/experiencias"), ("4","interactie: preguntar por experiencias"), ("3","spreken")))
P('<div class="se">Los marcadores del perfecto</div>')
P('<div class="fams three" style="margin-top:1mm">'
  '<div class="pcard"><div class="t">ya ↔ todavía no</div><div class="ej">Ya he ido · Todavía no he ido</div></div>'
  '<div class="pcard"><div class="t">alguna vez</div><div class="ej">¿Has estado alguna vez…?</div></div>'
  '<div class="pcard"><div class="t">nunca</div><div class="ej">Nunca he montado en avión</div></div></div>')
P('<div class="truc"><b>Chunks:</b> <b>¿Has estado alguna vez en…?</b> · <b>Sí, he estado (una vez).</b> · <b>No, nunca.</b> · <b>Todavía no, pero quiero ir.</b> · <b>Este año he viajado a…</b></div>')
P(actx(AN(), "Relaciona pregunta y respuesta",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Une cada pregunta con su respuesta. <span class="gloss">Verbind vraag en antwoord.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Pregunta</div><div class="cb short">1. ¿Has estado en Perú? &nbsp; 2. ¿Has visto el mar? &nbsp; 3. ¿Has montado en avión? &nbsp; 4. ¿Ya has comido?</div></div>'
  '<div class="wcol"><div class="ch">Respuesta</div><div class="cb short">a. Sí, muchas veces. &nbsp; b. Todavía no. &nbsp; c. No, nunca. &nbsp; d. Sí, he estado una vez.</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "Completa con ya / todavía no / nunca",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe el marcador correcto. <span class="gloss">Vul het juiste tijdswoord in.</span></p>'
  '<p style="margin-left:12.5mm">1. <span class="wl sm"></span> he hecho las maletas (al). &nbsp; 2. <span class="wl sm"></span> he estado en Chile (nog niet).<br>'
  '3. <span class="wl sm"></span> he montado en barco (nooit). &nbsp; 4. ¿Has viajado <span class="wl sm"></span> a Asia? (ooit)</p>',
  apoyo="Banco de palabras: ya · todavía no · nunca · alguna vez"))
P(actx(AN(), "Transforma · pregunta → respuesta",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Contesta a la pregunta con el pretérito perfecto (sí/no). <span class="gloss">Antwoord in de voltooide tijd.</span></p>'
  '<p style="margin-left:12.5mm">1. ¿Has estado en Perú? → Sí, <span class="wl md"></span><br>'
  '2. ¿Has visto el mar? → No, todavía <span class="wl md"></span><br>'
  '3. ¿Has hecho las maletas? → Sí, ya <span class="wl md"></span></p>',
  apoyo="Primera letra: he estado…"))
P(audiorow('<div class="ic">🎧</div><div><b>Escanea y escribe.</b> El dictado está en la página digital: <b>1ª vez</b> la frase entera, <b>2ª vez</b> por trozos. <span class="gloss">Het dictee staat online: eerst de hele zin, dan in stukken.</span></div>',
           qr("Escanea y escucha", '§2.3 · Dictado · un día de viaje', seed=403)))
P(actx(AN(), "Dictado · un día de viaje",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escucha y escribe las cinco frases (con el pretérito perfecto). <span class="gloss">Luister en schrijf de vijf zinnen.</span></p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span>4. <span class="wl full"></span>5. <span class="wl full"></span></p>',
  apoyo="1ª de zin heel · 2ª in stukken"))
P(actx("★", "Info-gap · ¿lo has hecho alguna vez?",
  [{"t":"🗣️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>Haceos cuatro preguntas «¿Has … alguna vez?» y contestad (sí/no/todavía no). Anota tres respuestas de tu compañero/a. <span class="gloss">Vier vragen; noteer drie antwoorden.</span></p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>',
  apoyo="Marco: ¿Alguna vez has…? — Sí, he… / No, nunca he…"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha «Experiencias de viaje»</b> en la web (TTS). Marca lo que <b>han hecho</b> los personajes. <b>2ª vez:</b> ¿quién ha estado dónde?</div>',
           qr("Escanea y escucha", "§4 · Experiencias", seed=402)))
sec_close()

# ================= §5 · LECTURA =================
sec_open("5", "§5 · Lectura 1 — «Un viaje inolvidable»", 'Dos personas cuentan un viaje reciente. Lee, busca información y reacciona. <span class="gloss">Twee mensen vertellen over een recente reis. Lezen, info zoeken, reageren.</span>',
        lpd(("1","lezen: hoofdgedachte"), ("2","lezen: info selecteren"), ("5","identiteit & cultuur")))
P('<div class="lecdoel"><b>Antes de leer:</b> mira el título «Un viaje inolvidable». ¿Qué esperas encontrar? <span class="gloss">Wat verwacht je in de tekst?</span></div>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> blog de viajes</span><span class="tm"><b>Fuente:</b> muro de clase</span><span class="tm"><b>Objetivo:</b> compartir un viaje</span></div>')
P(f'<div class="ptexts">'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["nina"]}</div><div><div class="nm">Nina</div><div class="fr">Cusco 🇵🇪</div></div></div>'
  f'<p>Este año <span class="evi">he viajado</span> a Chile con mi familia. <span class="evi">Hemos estado</span> en el desierto de Atacama, el más seco del mundo. <span class="evi">He visto</span> un cielo lleno de estrellas, ¡impresionante! También <span class="evi">hemos ido</span> al sur, a la Patagonia. Lo mejor <span class="evi">ha sido</span> el paisaje. Todavía no <span class="evi">he estado</span> en Rapa Nui, pero quiero ir. Ha sido un viaje <span class="evi">inolvidable</span>.</p></div>'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["diego"]}</div><div><div class="nm">Diego</div><div class="fr">CDMX 🇲🇽</div></div></div>'
  f'<p>Yo <span class="evi">he vuelto</span> hace poco de un viaje por Europa. <span class="evi">He estado</span> en España y <span class="evi">he probado</span> la paella en València. <span class="evi">He hecho</span> muchas fotos y <span class="evi">he escrito</span> un diario. Lo peor <span class="evi">ha sido</span> el vuelo, muy largo, pero ha valido la pena. Nunca <span class="evi">he estado</span> tan lejos de casa.</p></div></div>')
P(actx(AN(), "Verdadero o falso — con prueba",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>¿Verdadero (V) o falso (F)? Subraya la prueba. <span class="gloss">Waar of niet waar? Onderstreep het bewijs.</span></p>'
  '<table class="alf"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba (cita)</th></tr></thead><tbody>'
  '<tr><td>Nina ha estado en el desierto de Atacama.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Nina ya ha estado en Rapa Nui.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Diego ha probado la paella en València.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>',
  apoyo="Modelo"))
P(actx(AN(), "Escanea — completa la ficha",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Busca los datos de cada persona en el texto y completa la tabla. Una palabra o un número por casilla. <span class="gloss">Zoek de gegevens en vul de tabel aan.</span></p>'
  '<table class="alf"><thead><tr><th>—</th><th>Nina</th><th>Diego</th></tr></thead><tbody>'
  '<tr><td>¿Adónde ha viajado?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>¿Qué ha hecho/visto?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>¿Qué ha sido lo mejor/peor?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>',
  apoyo=""))
P(actx(AN(), "Reacciona — ¿y tú?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>¿Cuál de los dos viajes prefieres? Escribe 2–3 frases con <b>el pretérito perfecto</b> sobre un viaje tuyo (o uno que te gustaría hacer). <span class="gloss">Twee tot drie zinnen over een reis.</span></p>'
  '<div class="wbox sm"></div>',
  apoyo="Marco: Yo he estado en … He visto … Lo mejor ha sido …"))
sec_close()

# ================= TALLER =================
sec_open("T", "Taller de lengua", 'Dos herramientas: de <b>h muda</b> (stomme h, o.a. in <b>he/has/ha</b>!) en de <b>acentos</b> in participios (leído, oído) + conectoren van volgorde. <span class="gloss">De stomme h en de accenten.</span>')
P('<h3>1 · Ortografía — la h muda</h3>')
P(regla("La h no suena", '<p>La <b>h</b> no se pronuncia, pero sí se escribe. Es clave en el perfecto: <b>h</b>e, <b>h</b>as, <b>h</b>a, <b>h</b>emos, <b>h</b>an. También: el <b>h</b>otel, el <b>h</b>ostal, la <b>h</b>abitación, <b>h</b>acer → <b>h</b>echo, <b>h</b>oy.<br><span class="gloss">🔴 Vergeet de h niet: <i>he comido</i>, niet <span class="trap">e comido</span>.</span></p>'))
P(actx(AN(), "¿Falta la h? · completa",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe la h donde haga falta (o déjalo en blanco). <span class="gloss">Schrijf de h waar ze hoort.</span></p>'
  '<p style="margin-left:12.5mm">___e comido · ___as visto · el ___otel · la ___abitación · ___acer · ___oy · el ___ostal</p>',
  apoyo="Pista: he, has, hotel, habitación, hacer, hoy, hostal"))
P('<h3 style="margin-top:6mm">2 · Conectores de secuencia — cuenta tu viaje</h3>')
P(colloc("primero · luego · después · al final", ["primero = eerst","luego / después = daarna","más tarde = later","al final = ten slotte"]))
P(actx(AN(), "Ordena el relato del viaje",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Vuelve a escribir el viaje en orden con <b>primero, luego, después, al final</b>. <span class="gloss">Herschrijf de reis in volgorde.</span></p>'
  '<p style="margin-left:12.5mm">hemos vuelto · hemos cogido el avión · hemos visitado el desierto · hemos hecho las maletas<br>'
  '1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span>4. <span class="wl full"></span></p>',
  apoyo="Marco: Primero… · Después… · Al final…"))
sec_close()

# ================= LECTURA 2 · ESCUCHA =================
# Zelfde bron als de digitale hub (lectura_data / escucha_data): papier en scherm
# kunnen zo niet uit elkaar lopen. Elk op een eigen bladzijde (§14).
P('<div class="page"><div class="parada sec">')
P('<span class="num">6</span><span class="pk">§6 · Lectura 2 — «Una postal desde Valparaíso»</span>')
P('<div class="intro"><b>ES:</b> Una postal de verdad, con un diario de viaje. <b>No hace falta entenderlo todo</b> para sacar la información. <span class="gloss">Een echte postkaart met een reisdagboek erbij. Je hoeft niet alles te begrijpen — let op wat ze al gedaan heeft en wat nog niet.</span></div>')
P(PB.lectura_print(LD.C6P_U4, AN()))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">7</span><span class="pk">§7 · Escucha — «En la recepción del hostal»</span>')
P('<div class="intro"><b>ES:</b> Nina llega a las once de la noche y la reserva no coincide. <b>Escucha primero, escribe después.</b> <span class="gloss">Nina komt om elf uur \'s avonds aan en de reservering klopt niet. Eerst luisteren, dan schrijven; het transcript staat online en gaat pas open ná de taken.</span></div>')
P(PB.escucha_print(ED.C6P_U4, AN()))
P('</div>')

# ================= CULTURA =================
sec_open("C", "Cultura · el gran viaje hispano", 'El mundo hispano está lleno de <b>iconos de viaje</b>: el <b>desierto de Atacama</b> (Chile), <b>Machu Picchu</b> (Perú), el <b>Camino de Santiago</b> (España) y <b>Rapa Nui</b> con sus moáis. <span class="gloss">De grote reisbestemmingen van de Spaanstalige wereld.</span>',
        lpd(("5","identiteit in diversiteit: el gran viaje hispano")))
P('<div class="fams three" style="margin-top:2mm">'
  '<div class="pcard"><div class="t">🏜️ El desierto de Atacama</div><div class="ej" style="margin-top:2mm">In <b>Chile</b> ligt de <b>droogste woestijn</b> ter wereld. \'s Nachts zie je er de helderste sterrenhemel — er staan grote sterrenwachten. Nina «ha estado» er.</div></div>'
  '<div class="pcard"><div class="t">🥾 El Camino de Santiago</div><div class="ej" style="margin-top:2mm">In <b>España</b> lopen pelgrims al eeuwen de <b>Camino</b> naar Santiago de Compostela. «He hecho el Camino» is een klassiek reisverhaal — te voet, honderden kilometers.</div></div>'
  '<div class="pcard"><div class="t">🗿 Rapa Nui</div><div class="ej" style="margin-top:2mm"><b>Isla de Pascua</b> (Chile), midden in de Stille Oceaan, is beroemd om de <b>moáis</b>: reusachtige stenen beelden. Een van de meest afgelegen bewoonde plekken ter wereld.</div></div></div>')
P('<div class="route-note" style="margin-top:5mm">🗺️ <b>En la web:</b> haz clic en Chile (★) en el mapa para descubrir el gran viaje. <span class="gloss">Online: klik op Chile voor de reis-fiche.</span></div>')
P(actx(AN(), "¿Adónde quieres viajar? · escribe",
  [{"t":"🌍 Cultura","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Elige un destino y di por qué. Escribe dos frases con <b>quiero / tengo ganas de</b> y el perfecto (todavía no he estado…). <span class="gloss">Kies een bestemming en zeg waarom.</span></p>'
  '<div class="wbox sm"></div>',
  apoyo="Marco: Quiero ir a… porque… · Me gustaría ver…"))
P(actx(AN(), "Datos curiosos — une",
  [{"t":"🌍 Cultura","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Une las dos columnas: escribe la letra. <span class="gloss">Verbind en schrijf de letter.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Lugar</div><div class="cb short">1. Atacama &nbsp; 2. Camino de Santiago &nbsp; 3. Rapa Nui &nbsp; 4. Machu Picchu</div></div>'
  '<div class="wcol"><div class="ch">Dato</div><div class="cb short">a. moáis en el Pacífico &nbsp; b. ciudad inca (Perú) &nbsp; c. desierto más seco &nbsp; d. camino de peregrinos</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo="Banco de palabras"))
sec_close()

retos("cultura_c6p4", "Retos — el viaje visto desde el otro lado",
      'Cuántos visitantes caben en Barcelona y en Cusco, y cuatro situaciones donde un belga <b>mete la pata sin saberlo</b>.',
      'Hoeveel bezoekers er passen in Barcelona en Cusco, en vier situaties waarin een Belg de bal misslaat zonder het te weten.')

# ================= TAREA FINAL =================
sec_open("★", "Tarea final · «Mi mejor viaje»", 'Escribe un <b>blog/postal</b> sobre un viaje (real o inventado) met <b>el perfecto</b>, <b>por/para</b> y una <b>mini-opinión</b>. <span class="gloss">Schrijf een reisblog met de voltooide tijd, por/para en een mening.</span>')
P(fmu('tus compañeros de clase (el muro de viajes)', 'contar tu mejor viaje', 'un blog/postal (6–8 frases) + una presentación oral (± 1 min)'))
P('<ol class="pasos">'
  '<li><b>Di adónde has viajado</b> y con qué: «He viajado a… <b>por</b> avión/tren».</li>'
  '<li><b>Cuenta 3–4 experiencias</b> con <b>el perfecto</b>: «He visto…, he probado…, he hecho…».</li>'
  '<li><b>Usa por/para</b>: «He ido <b>para</b> descansar», «Me he quedado <b>por</b> una semana».</li>'
  '<li><b>Añade tu opinión</b>: «Lo mejor <b>ha sido</b>… porque…».</li>'
  '<li><b>Preséntalo en pareja</b> y <b>graba</b> tu relato en la web. Escúchate y mejora.</li></ol>')
P('<div class="se" style="margin-top:4mm">Mi blog de viaje <span class="gloss" style="font-size:8pt">· 6–8 zinnen</span></div><div class="wbox lg"></div>')
P('<div class="se" style="margin-top:3mm">Mi opinión <span class="gloss" style="font-size:8pt">· lo mejor ha sido… porque…</span></div><div class="wbox sm"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba tu relato de viaje</b> en la web (recorder + rúbrica). Escucha, compara con el modelo y vuelve a grabar.</div>',
           qr("Escanea y graba", "Tarea · Mi mejor viaje", seed=470)))
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Ik gebruik de <b>perfecto</b> correct (haber + participio)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik minstens <b>2 onregelmatige participios</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>por</b> én <b>para</b> correct</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik geef <b>één mening</b> (lo mejor ha sido… porque…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>presenteer vlot</b> (± 1 min)</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — el viaje de mi compañero/a</div>'
  '<table><thead><tr><th>Un lugar que también quiero visitar</th><th>Una pregunta que le hago</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('<div class="truc" style="margin-top:3mm"><b>✍️ Antes de colgar:</b> lees je tekst na — <i>haber + participio correct? · 2 irregulares? · por/para? · una opinión?</i> Verbeter één ding: <span class="wl lg"></span></div>')
sec_close()

# ================= REPASO =================
sec_open("✓", "Repaso · lo esencial", 'Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag; de volledige herhaling staat online.</span>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>Perfecto compuesto:</b> haber (he/has/ha/hemos/habéis/han) + participio (-ado/-ido). <i>He viajado.</i></li>'
  '<li><b>Participios irregulares:</b> hecho · visto · dicho · vuelto · puesto · escrito · abierto · roto.</li>'
  '<li><b>Marcadores:</b> hoy · esta semana · este año · ya · todavía no · nunca · alguna vez.</li>'
  '<li><b>Para</b> = doel/bestemming/«om te» (para Chile · para descansar · para ti).</li>'
  '<li><b>Por</b> = middel/duur/reden/doorheen (por avión · por dos días · por el mal tiempo).</li>'
  '<li><b>Las trampas:</b> 🔴 haber ≠ tener · 🔴 vergeet de <b>h</b> niet (he, has) · 🔴 hecho/visto (irreg.) · 🔴 por ≠ para.</li></ul></div>')
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> spelletjes met zelfcorrectie (perfecto, participios, por/para, marcadores…).</div>')
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td>over <b>transport en verblijf</b> praten</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>de <b>perfecto compuesto</b> vormen (haber + participio)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>de <b>onregelmatige participios</b> gebruiken</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>por</b> en <b>para</b> onderscheiden</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>contar un <b>viaje</b> con una miniopinión <span class="gloss">een reis vertellen met een korte mening</span></td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil para mí: <span class="wl md"></span> · Lo que quiero practicar más: <span class="wl md"></span></i></div>')
P('<div class="se" style="margin-top:6mm">Auto-test rápido · ¿lo sé?</div>')
P('<p style="margin-left:0">1. «Ik heb gereisd» = <span class="wl md"></span><br>'
  '2. hacer → participio = <span class="wl sm"></span><br>'
  '3. ver → participio = <span class="wl sm"></span><br>'
  '4. por of para: «Salgo ___ Chile» = <span class="wl sm"></span><br>'
  '5. Geef één ervaring (1 zin met el perfecto): <span class="wl lg"></span></p>')
P('<div class="bridge"><b>» Siguiente parada: U5 «Érase una vez».</b> Ya cuentas lo que <b>has hecho</b>; en <b>U5</b> das el gran salto al <b>pretérito indefinido</b> (fui, hice, vi) para contar <b>biografías</b> e historias del pasado, en Buenos Aires con <b>Mateo</b>. ¡Seguimos! <span class="gloss">In U5: de indefinido — verhalen en biografieën uit het verleden.</span></div>')
sec_close()

# ================= §V VOCABULARIO =================
VOC = json.load(open(f"{HERE}/u4_vocab.json", encoding="utf-8"))
GRP = [("transporte","El transporte"), ("alojamiento","El alojamiento"), ("viaje","Verbos del viaje"),
       ("experiencias","El perfecto · experiencias"), ("lugares","Los lugares"),
       ("porpara","Por y para"), ("opinar","Opinar sobre el viaje"), ("tiempo","Marcadores de tiempo")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (begrijpen en zelf gebruiken)")))
P('</div>')
P('<p style="font-size:9.6pt">Las palabras del <b>viaje</b> como red — tres familias:</p>')
P(clusters([
  ("🧳","El viaje",["el billete · la maleta","el hotel · la reserva","viajar · reservar"],"Vervoer & verblijf."),
  ("📸","Experiencias",["he estado · he visto","he hecho · he probado","ya · todavía no · nunca"],"Wat je gedaan hebt."),
  ("🎯","Por y para",["para Chile · para ti","por avión · por dos días","lo mejor · impresionante"],"por/para & mening."),
]))
for key, titel in GRP:
    items = [v for v in VOC if v.get("grp") == key]
    if not items: continue
    P(f'<h3 style="margin-top:6mm">{titel} <span class="gloss" style="font-size:8pt">· {len(items)} woorden</span></h3>')
    rows = "".join(f'<tr><td><b>{v["es"]}</b></td><td>{v["nl"]}</td><td class="gloss">{v["soort"]}</td><td class="gloss">{v["ej"]}</td></tr>' for v in items)
    P(f'<table class="alf"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody>{rows}</tbody></table>')
P('<div class="divider">Escalera de práctica · V.1–V.5</div>')
P(actx("V.1", "Reconocer — ES → NL",
  [{"t":"🔍 Leer","skill":True},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Escribe la traducción. <span class="gloss">Schrijf de vertaling.</span> el billete = <span class="wl md"></span> · he visto = <span class="wl md"></span> · la playa = <span class="wl md"></span> · para = <span class="wl md"></span></p>', apoyo="Modelo"))
P(actx("V.2", "Distinguir — sorteer per familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Clasifica: <span class="gloss">sorteer deze woorden</span> <span class="words"><b>el avión · he visto · el hotel · la playa · he probado · el billete · la reserva · he hecho</b></span></p>'
  + sortcols([("viaje (sustantivo)",""),("experiencia (perfecto)","")], eigen=False), apoyo="Banco de palabras"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Completa la palabra; tienes la primera letra. <span class="gloss">de beginletter staat erbij</span> het ticket = <b>b</b>___ · de koffer = <b>m</b>___ · ik heb gezien = <b>h</b>___ v___ · om te = <b>p</b>___<br><span class="wl full"></span></p>', apoyo="Primera letra"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Escribe una frase correcta con <b>he estado · por · avión</b>.</p><div class="wbox sm"></div>', apoyo=""))
P(actx("V.5", "Comunicar — mi viaje en 3 frases",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Escribe tres frases sobre un viaje (adónde has ido · qué has hecho · una opinión) y dilas en voz alta. <span class="gloss">Drie zinnen over een reis.</span></p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>', apoyo="Marco: He estado en… · He visto… · Lo mejor ha sido…"))
P('<div class="se" style="margin-top:6mm">Mi mapa de palabras <span class="gloss" style="font-size:8pt">— teken je reis en label 6 dingen in het Spaans</span></div>')
P('<div class="wbox lg"></div>')
P(mispal("Mis palabras de la unidad", 7))
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Sigue en la página digital:</span> <span class="g">flip cards (ES↔NL), audio en de spellen bouwen de steun verder af.</span></div></div>')
sec_close()

# ---------- OVERRIDE (bladspiegel-hygiëne) ----------
CSS_OVR = (' .act .steun{break-before:avoid;} '
           '.fams,.machine,.obsbox,.scale,.tree,.zoom,.fmu,.xray,.colloc,.clusters,.vpairs,.blocks,.agree{break-inside:avoid;} '
           '.ptexts,.fichacard,.menu,.gustobars{break-inside:avoid;} '
           ' '
           '')

# ---------- EDITBAR ----------
EDITBAR = '''
<div class="editbar" id="editbar">
  <span id="ebtxt">✏️ «Bewerken» om zelf tekst aan te passen</span>
  <button class="b1" id="ebEdit">Bewerken</button>
  <button class="b2" id="ebPdf">🖨️ Opslaan als PDF</button>
  <button class="b2" id="ebSave">💾 Bewaar</button>
</div>
<script id="ebscript">
(function(){
 var SEL='h1,h2,h3,h4,p,td,th,li,.intro,.hist,.gloss,.ojo,.anchor,.ej,.q,.sub,.route-note,.pk,.se,.divider,.t,.t2,.nl,.es,.lpdchip,.lpdlab,.wcol .ch,.bub,.k,.v,.ln,.mq,.ma,.br,.blk,.clu li,.node,.mi,.mt,.sec2';
 var editing=false;
 function setEditable(on){document.querySelectorAll(SEL).forEach(function(e){if(on){e.setAttribute('contenteditable','true');e.setAttribute('spellcheck','false');}else{e.removeAttribute('contenteditable');}});}
 var eb=document.getElementById('editbar'),txt=document.getElementById('ebtxt'),bE=document.getElementById('ebEdit');
 bE.onclick=function(){editing=!editing;document.body.classList.toggle('editing',editing);eb.classList.toggle('on',editing);setEditable(editing);
   txt.textContent=editing?'✏️ AAN — klik op tekst en typ':'✏️ «Bewerken» om zelf tekst aan te passen';bE.textContent=editing?'Klaar':'Bewerken';};
 document.getElementById('ebPdf').onclick=function(){window.print();};
 document.getElementById('ebSave').onclick=function(){
   if(editing){bE.click();}
   var clone=document.documentElement.cloneNode(true);
   var b=clone.querySelector('.editbar'); if(b) b.remove();
   var s=clone.querySelector('script#ebscript'); if(s) s.remove();
   var html='<!doctype html>\\n'+clone.outerHTML;
   var blob=new Blob([html],{type:'text/html'}); var a=document.createElement('a');
   a.href=URL.createObjectURL(blob); a.download='C6plus_U4_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Más español en la práctica · C6+ U4 De viaje</title><style>'
        + CSS + CSS_OVR + RP.CSS + PB.CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/C6plus_U4.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes ·", _AN[0], "genummerde oefeningen (excl. V.1–V.5)")
