#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de print-HTML C6plus_U1.html (C6+ · Unidad 1 «El día a día») → PDF via Chromium.
# Zelfde componentenkit/pijplijn/CSS als de gelockte golden sample C6+·U0 (geïmporteerd uit gen_u0_print).
# Cursuskleur = paars (C6+). Parada 1 = España (el horario español), gastvrouw Lucía + Diego.
# Kerngrammatica: reflexieve ww. · ser/estar-contrast · gustar + OI · P3-seed «me gusta… porque».
# Output = standalone bewerkbare C6plus_U1.html (+ PDF-render los).
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/01-cursussen/06-vervolg/U0")   # hergebruik de gelockte U0-componentenkit
import gen_u0_print as U0
from gen_u0_print import (CSS, AV, TU, MOCH, audiorow, act, regla, guide, lpd, divider,
                          pcard, steun, sortcols, actx, tarea_com, obsbox, machine, blocks, tree,
                          mirror, fmu, scaffold, zoom, clusters, colloc, scale, vpairs, mispal, xray,
                          gustobars, menu)

# ================= BODY =================
import sys as _sys
_sys.path.insert(0, "/home/user/espa-ol-en-la-pr-ctica/03-build/web")
import qr_print as QRP; QRP.fijar("C6+", 1)
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
    P('</div>')  # sluit .parada; .page blijft open
def sec_close():
    P('</div>')  # sluit .page

# ---------- OPENER ----------
P(f'''
<div class="hero">
  <div class="tab">U1 · EL DÍA A DÍA</div>
  <div class="eyebrow">UNIDAD 1 · LA RUTA · ESPAÑA · EL DÍA A DÍA ⏰</div>
  <h1>El día a día</h1>
  <div class="sub">¡Empieza el viaje! Hoy cuentas tu <b>día a día</b>: a qué hora te <b>levantas</b>, qué haces <b>cada día</b>, cómo te <b>sientes</b> (estoy cansado) y qué te <b>gusta</b> (me gusta…). <span class="gloss">De reis begint echt: je dagelijks leven, je gevoel en je smaak.</span></div>
  <div class="q">¿Cómo es un día en tu vida? <span style="font-weight:400;opacity:.9">· Hoe ziet jouw dag eruit?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U0 · Reencuentro</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U1 · El día a día</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U2 · Aquí vivo</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U3 · Conectados</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U4 · De viaje</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U5–U7 · el pasado</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 1 · España.</b> Nuestra primera parada es <b>España</b>. Con <b>Lucía</b> (Sevilla) descubres el <b>horario español</b>: se come tarde (la comida a las 14–15, la cena a las 21–22) y a veces hay <b>siesta</b>. <span class="gloss">Eerste halte Spanje: het Spaanse dagritme, met laat eten en soms een siësta.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> Un día normal de <b>Lucía</b> en Sevilla: se <b>despierta</b>, se <b>ducha</b>, va al instituto y por la tarde queda con <b>Diego</b>. Aprendes a contar <b>tu</b> día: la <b>hora</b>, la <b>rutina</b> (con verbos reflexivos), cómo te <b>sientes</b> (ser vs estar) y qué te <b>gusta</b> hacer. Al final: <b>«me gusta… porque…»</b> — tu primera opinión.
      <span class="gloss">Een gewone dag van Lucía in Sevilla. Je leert je eigen dag vertellen: het uur, de routine, hoe je je voelt en wat je graag doet — en je geeft je eerste mening met «porque».</span></div>
      <div class="ojo"><b>¡Ojo! — dos trampas desde el primer día:</b> ① reflexivo = <b>pronombre + verbo</b>: <i>me</i> levanto, <i>te</i> levantas (nunca «yo levanto» para «ik sta op»). ② <b>gustar funciona al revés</b>: <i>Me gusta la música</i> = la música me gusta a mí. <span class="gloss">Het pronomen hoort erbij, en gustar draait de zin om.</span></div>
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
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila del día</span><br><span class="gloss" style="font-size:8.5pt">Vul je rugzak met de woorden van je dag: me levanto, me ducho, ¿qué hora es?, me gusta, estoy cansado… — alles wat je vandaag nodig hebt.</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">decir la hora</span> (¿qué hora es? · son las…) <span class="nl">de klok lezen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">contar tu rutina</span> con <b>verbos reflexivos</b> (me levanto, me ducho…) <span class="nl">je routine vertellen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">contrastar ser y estar</span> (soy simpático / estoy cansado) <span class="nl">ser vs estar gebruiken</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">hablar de tus gustos</span> con <b>gustar + OI</b> (me/te/le gusta…) <span class="nl">over je smaken praten</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">leer dos perfiles</span> y reaccionar <span class="nl">profielen lezen (Lectura)</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">crear tu <b>«Mi día a día»</b></span> y presentarlo en pareja <span class="nl">je dagblog maken (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>La hora</span><span><b>§2</b>Mi rutina</span><span><b>§3</b>Reflexivos</span><span><b>§4</b>Ser/estar</span><span><b>§5</b>Gustar</span><span><b>§6</b>Lectura</span><span><b>Taller</b>Sílaba/conect.</span><span><b>Cultura</b>Horario</span><span><b>Tarea</b>Mi día</span><span><b>Repaso</b>Semáforo</span>
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

# ================= §0 · ¡PONTE AL DÍA! (repaso) =================
sec_open("0", "§0 · ¡Ponte al día!", 'Antes de empezar, activamos tres cosas de U0: el <b>presente</b> (yo/tú/él…), <b>ser/estar</b> y los <b>números</b> (los necesitas para la hora). <span class="gloss">Eerst frissen we het presente, ser/estar en de getallen op — die heb je zo nodig voor de klok.</span>',
        lpd(("8","taalsysteem: presente & ser/estar (repaso)"), ("3","spreken/schrijven over jezelf")))
P('<div class="se">El presente (repaso) <span class="gloss" style="font-size:8pt">— de motor uit U0</span></div>')
P('<table class="conj"><thead><tr><th>—</th><th>hablar</th><th>comer</th><th>vivir</th><th>ser</th><th>ir</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">habl<span class="end">o</span></td><td class="v">com<span class="end">o</span></td><td class="v">viv<span class="end">o</span></td><td class="v">soy</td><td class="v">voy</td></tr>'
  '<tr><td class="p">tú</td><td class="v">habl<span class="end">as</span></td><td class="v">com<span class="end">es</span></td><td class="v">viv<span class="end">es</span></td><td class="v">eres</td><td class="v">vas</td></tr>'
  '<tr><td class="p">él/ella</td><td class="v">habl<span class="end">a</span></td><td class="v">com<span class="end">e</span></td><td class="v">viv<span class="end">e</span></td><td class="v">es</td><td class="v">va</td></tr>'
  '<tr><td class="p">nosotros</td><td class="v">habl<span class="end">amos</span></td><td class="v">com<span class="end">emos</span></td><td class="v">viv<span class="end">imos</span></td><td class="v">somos</td><td class="v">vamos</td></tr>'
  '<tr><td class="p">ellos</td><td class="v">habl<span class="end">an</span></td><td class="v">com<span class="end">en</span></td><td class="v">viv<span class="end">en</span></td><td class="v">son</td><td class="v">van</td></tr></tbody></table>')
P(actx(AN(), "Calienta · el presente (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>Escribe el presente (el infinitivo está entre paréntesis).</i> <span class="gloss">Vul de tegenwoordige tijd in.</span></p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl sm"></span> (estudiar) español. &nbsp; 2. ¿Tú <span class="wl sm"></span> (vivir) en Gante? &nbsp; 3. Lucía <span class="wl sm"></span> (ser) de Sevilla.<br>'
  '4. Nosotros <span class="wl sm"></span> (comer) a las dos. &nbsp; 5. Ellos <span class="wl sm"></span> (ir) al instituto. &nbsp; 6. Yo <span class="wl sm"></span> (hacer) deporte.</p>',
  apoyo="Banco de palabras: estudio · vives · es · comemos · van · hago"))
P('<div class="truc"><b>Repaso ser/estar (U0):</b> <b>ser</b> = quién o qué eres (soy belga, soy simpático) · <b>estar</b> = dónde o cómo estás (estoy en clase, estoy bien). <span class="gloss">In §4 zetten we dit contrast helemaal op scherp.</span></div>')
P(actx(AN(), "¿ser o estar? (repaso rápido)",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★☆☆"}],
  '<p><i>Elige soy o estoy.</i> <span class="gloss">Kies soy of estoy.</span></p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl sm"></span> de Bélgica. &nbsp; 2. Hoy <span class="wl sm"></span> cansado. &nbsp; 3. <span class="wl sm"></span> estudiante. &nbsp; 4. <span class="wl sm"></span> en el instituto.</p>',
  apoyo="Pista: ser = identidad o carácter · estar = lugar o estado de ahora"))
sec_close()

# ================= §1 · LA HORA =================
sec_open("1", "§1 · ¿Qué hora es? — la hora", 'Para contar tu día necesitas la <b>hora</b>. <b>Es la una</b> (1 sola) · <b>Son las</b> dos, tres… (2+). Y los momentos: <b>y cuarto</b>, <b>y media</b>, <b>menos cuarto</b>. <span class="gloss">Voor je dagverhaal heb je de klok nodig: es la una / son las…, en y cuarto, y media, menos cuarto.</span>',
        lpd(("8","taalsysteem: la hora & getallen"), ("7","woordenschat: tijdsuitdrukkingen"), ("4","luisteren: cijfers & tijd")))
P(obsbox([
  '🕐 <span class="hl">Es la una</span>. &nbsp; 🕑 <span class="hl">Son las dos</span>. &nbsp; 🕔 Son las cinco.',
  '🕝 Son las dos <span class="hl">y media</span>. &nbsp; 🕜 Son la una <span class="hl">y cuarto</span>. &nbsp; 🕟 Son las cuatro <span class="hl">menos cuarto</span>.',
], vragen='¿Cuándo dices <b>es la</b> y cuándo <b>son las</b>? ¿Qué significan <b>y cuarto</b>, <b>y media</b>, <b>menos cuarto</b>? <span class="gloss">Wanneer «es la» / «son las»? Wat betekenen y cuarto / y media / menos cuarto?</span>'))
P(regla("Regla · la hora", '<p><b>Es la una</b> (enkel bij 1 uur). <b>Son las</b> + 2, 3, 4…: <i>Son las tres</i>.<br>'
  '<b>+ minuten:</b> <i>y cuarto</i> (:15) · <i>y media</i> (:30) · <i>menos cuarto</i> (:45, «kwart vóór het volgende uur»). Precies op het uur: <b>en punto</b>.<br>'
  '<b>Momento del día:</b> <i>de la mañana</i> (ochtend) · <i>de la tarde</i> (namiddag) · <i>de la noche</i> (avond/nacht).<br>'
  '<b>¿A qué hora?</b> → <b>A la una</b> / <b>A las</b> ocho: <i>A las siete me levanto.</i></p>'))
P(zoom("1 uur → enkelvoud", "Es la una", "2+ uur → meervoud", "Son las dos"))
P(actx(AN(), "Escribe la hora en palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escribe la hora con letras (son las… / es la…). <span class="gloss">Schrijf de tijd voluit.</span></p>'
  '<p style="margin-left:12.5mm">3:00 → <span class="wl md"></span> &nbsp; 1:15 → <span class="wl md"></span> &nbsp; 6:30 → <span class="wl md"></span><br>'
  '4:45 → <span class="wl md"></span> &nbsp; 9:00 → <span class="wl md"></span> &nbsp; 2:15 → <span class="wl md"></span></p>',
  apoyo="Modelo: regla"))
P(actx(AN(), "Relaciona el reloj y la hora",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Une cada hora digital con su frase: escribe la letra. <span class="gloss">Verbind de digitale tijd met de zin.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Reloj</div><div class="cb short">1. 08:30 &nbsp; 2. 01:00 &nbsp; 3. 05:15 &nbsp; 4. 10:45</div></div>'
  '<div class="wcol"><div class="ch">La hora</div><div class="cb short">a. es la una en punto &nbsp; b. son las once menos cuarto &nbsp; c. son las ocho y media &nbsp; d. son las cinco y cuarto</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "¿A qué hora? · tu horario",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>¿A qué hora haces estas cosas? Contesta con <b>A la(s)…</b> y dilo en voz alta. <span class="gloss">Antwoord met A la(s)… en zeg het hardop.</span></p>'
  '<table class="alf"><thead><tr><th>Pregunta</th><th>Tu respuesta</th></tr></thead><tbody>'
  '<tr><td>¿A qué hora te levantas?</td><td>Me levanto <span class="wl md"></span></td></tr>'
  '<tr><td>¿A qué hora empiezan las clases?</td><td>Empiezan <span class="wl md"></span></td></tr>'
  '<tr><td>¿A qué hora comes?</td><td>Como <span class="wl md"></span></td></tr>'
  '<tr><td>¿A qué hora te acuestas?</td><td>Me acuesto <span class="wl md"></span></td></tr></tbody></table>',
  apoyo="Marco: A las… · Es la una · Son las… y cuarto / y media / menos cuarto"))
P(audiorow('<div class="ic">🎧</div><div><b>Dictado de horas.</b> Escucha en la página digital (o el/la profe lee) y escribe la hora. <b>1ª vez:</b> la hora en punto · <b>2ª vez:</b> con minutos.</div>',
           qr("Escanea y escucha", "§1 · Dictado de horas", seed=101)))
P(actx(AN(), "Dictado · escribe la hora que oyes",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escucha y escribe las seis horas con letras (son las…). <span class="gloss">Luister en schrijf de zes tijden voluit.</span></p>'
  '<p style="margin-left:12.5mm">a) <span class="wl sm"></span> &nbsp; b) <span class="wl sm"></span> &nbsp; c) <span class="wl sm"></span> &nbsp; d) <span class="wl sm"></span> &nbsp; e) <span class="wl sm"></span> &nbsp; f) <span class="wl sm"></span></p>',
  apoyo="docent leest voor"))
P('<div class="se" style="margin-top:5mm">Los días, meses y estaciones <span class="gloss" style="font-size:8pt">— el calendario del año</span></div>')
P('<div class="clusters" style="grid-template-columns:1fr 1fr 1fr">'
  '<div class="clu"><div class="ch"><span class="ci">📅</span>Los días</div><ul><li>lunes · martes · miércoles</li><li>jueves · viernes</li><li>sábado · domingo</li></ul><div class="ex">el fin de semana · minuscule letter!</div></div>'
  '<div class="clu"><div class="ch"><span class="ci">🗓️</span>Los meses</div><ul><li>enero · febrero · marzo</li><li>abril · mayo · junio…</li><li>…diciembre</li></ul><div class="ex">en enero, en julio (met «en»)</div></div>'
  '<div class="clu"><div class="ch"><span class="ci">🍂</span>Las estaciones</div><ul><li>la primavera · el verano</li><li>el otoño · el invierno</li></ul><div class="ex">en verano vamos a la playa</div></div></div>')
P('<div class="truc"><b>¡Ojo!</b> Los días y los meses se escriben con <b>minúscula</b> (lunes, enero), no <span class="trap">Lunes, Enero</span>. «Op maandag» es <b>el lunes</b>; «elke maandag», <b>los lunes</b>. <span class="gloss">Kleine letter, en el lunes tegenover los lunes.</span></div>')
P(actx(AN(), "El calendario · completa",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Completa los días que faltan. Después completa las dos frases sobre tu mes favorito y la estación. <span class="gloss">Vul de dagen aan en daarna de twee zinnen.</span></p>'
  '<p style="margin-left:12.5mm">lunes — <span class="wl sm"></span> — miércoles — <span class="wl sm"></span> — viernes — <span class="wl sm"></span> — <span class="wl sm"></span><br>'
  'Mi mes favorito es <span class="wl sm"></span> porque <span class="wl md"></span>. &nbsp; En <span class="wl sm"></span> (estación) hace buen tiempo.</p>',
  apoyo="Pista: los días y los meses van en minúscula"))
sec_close()

retos("hora_c6p", "§1.4 · Retos — la hora que decide",
      'Una agenda <b>saboteada</b> y cuatro agendas que casi no encajan.',
      "Een gesaboteerde agenda en vier agenda's die bijna niet passen.")

# ================= §2 · MI RUTINA (vocab + conectores + frecuencia) =================
sec_open("2", "§2 · Mi día a día — la rutina", 'Las <b>acciones</b> de un día normal, en orden con <b>conectores</b> (primero, luego, después) y con qué <b>frecuencia</b> (siempre, a veces, nunca). <span class="gloss">De acties van je dag, in volgorde met verbindingswoorden en frequentie-woorden.</span>',
        lpd(("7","woordenschat: acciones de la rutina"), ("8","taalsysteem: conectores"), ("3","spreken/schrijven over jezelf")))
P('<div class="se">Las acciones de la rutina <span class="gloss" style="font-size:8pt"> (Unidad 3)</span></div>')
P('<table class="alf"><thead><tr><th>Español</th><th>Nederlands</th><th>Ejemplo (forma «yo»)</th></tr></thead><tbody>'
  '<tr><td><b>despertarse</b></td><td>wakker worden</td><td class="gloss">Me despierto a las siete.</td></tr>'
  '<tr><td><b>levantarse</b></td><td>opstaan</td><td class="gloss">Me levanto a las siete y cuarto.</td></tr>'
  '<tr><td><b>ducharse</b></td><td>(zich) douchen</td><td class="gloss">Me ducho por la mañana.</td></tr>'
  '<tr><td><b>vestirse</b></td><td>zich aankleden</td><td class="gloss">Me visto rápido.</td></tr>'
  '<tr><td><b>desayunar</b></td><td>ontbijten</td><td class="gloss">Desayuno pan con leche.</td></tr>'
  '<tr><td><b>salir de casa</b></td><td>het huis uit gaan</td><td class="gloss">Salgo de casa a las ocho.</td></tr>'
  '<tr><td><b>comer</b> / <b>merendar</b></td><td>eten / tussendoortje eten</td><td class="gloss">Como a las dos; meriendo a las cinco.</td></tr>'
  '<tr><td><b>hacer los deberes</b></td><td>huiswerk maken</td><td class="gloss">Hago los deberes por la tarde.</td></tr>'
  '<tr><td><b>volver a casa</b></td><td>naar huis terugkeren</td><td class="gloss">Vuelvo a casa a las seis.</td></tr>'
  '<tr><td><b>cenar</b></td><td>avondeten</td><td class="gloss">Ceno a las nueve.</td></tr>'
  '<tr><td><b>acostarse</b></td><td>naar bed gaan</td><td class="gloss">Me acuesto a las once.</td></tr></tbody></table>')
P('<div class="se" style="margin-top:4mm">Los conectores de secuencia <span class="gloss" style="font-size:8pt">— vertel je dag in orde</span></div>')
P(colloc("primero · luego · después · por último", ["primero = eerst","luego/después = daarna","más tarde = later","antes de + inf.","por último = ten slotte"]))
P('<div class="se" style="margin-top:4mm">Los adverbios de frecuencia <span class="gloss" style="font-size:8pt">— ¿con qué frecuencia?</span></div>')
P(scale(["siempre 100%","casi siempre","normalmente","a veces","casi nunca","nunca 0%"]))
P(actx(AN(), "Ordena tu día · numera las acciones",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Ordena tu rutina: numera las acciones del 1 al 8. <span class="gloss">Zet je routine in volgorde.</span></p>'
  '<p style="margin-left:12.5mm">___ ceno &nbsp; ___ me levanto &nbsp; ___ voy al instituto &nbsp; ___ me acuesto<br>'
  '___ desayuno &nbsp; ___ como &nbsp; ___ hago los deberes &nbsp; ___ me ducho</p>',
  apoyo="Modelo"))
P(actx(AN(), "Relaciona la acción con una hora típica",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Une las dos columnas: escribe la letra. <span class="gloss">Verbind en schrijf de letter.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Acción</div><div class="cb short">1. me levanto &nbsp; 2. como &nbsp; 3. meriendo &nbsp; 4. me acuesto</div></div>'
  '<div class="wcol"><div class="ch">Hora</div><div class="cb short">a. a las cinco de la tarde &nbsp; b. a las siete de la mañana &nbsp; c. a las once de la noche &nbsp; d. a las dos</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "Completa con los conectores",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Elige entre <span class="gloss">kies uit</span> <span class="words"><b>primero · luego · después · por último</b></span></p>'
  '<p style="margin-left:12.5mm">Por la mañana, <span class="wl sm"></span> me levanto a las siete. <span class="wl sm"></span> me ducho y me visto. <span class="wl sm"></span> desayuno con mi familia. <span class="wl sm"></span>, voy al instituto en bici.</p>',
  apoyo="Banco de palabras"))
P(actx(AN(), "¿Con qué frecuencia? · escribe 4 frases",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escribe cuatro frases sobre tu rutina con un adverbio de frecuencia y una hora. <span class="gloss">Vier zinnen over je routine.</span> <span class="words"><b>siempre · normalmente · a veces · nunca</b></span></p>'
  '<p style="margin-left:12.5mm" class="gloss">Modelo: <i>Normalmente me levanto a las siete.</i></p>'
  '<div class="wbox sm"></div>',
  apoyo="Marco: Siempre… · Normalmente… · A veces… · Nunca…"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha «Un día con Lucía»</b> en la página digital (TTS). <b>1ª vez:</b> ¿a qué hora se levanta? · <b>2ª vez:</b> ¿qué hace por la tarde? Escribe los datos y luego cuenta tu día.</div>',
           qr("Escanea y escucha", "§2 · Un día con Lucía", seed=102)))
sec_close()

retos("rutina_c6p", "§2.4 · Retos — el día más normal del mundo",
      'El día de tu <b>móvil</b>, cinco minutos de podcast sin que pase nada, y tres rutinas extremas.',
      'De dag van je gsm, vijf minuten podcast zonder dat er iets gebeurt, en drie extreme routines.')

# ================= §3 · LOS VERBOS REFLEXIVOS =================
sec_open("3", "§3 · Los verbos reflexivos", 'La <b>estrella</b> de la unidad. En «me levanto» la acción <b>vuelve a mí</b>: pronombre (<b>me·te·se·nos·os·se</b>) + verbo. Aprendes a formarlos y a colocarlos. <span class="gloss">De ster van deze unit: bij reflexieve werkwoorden keert de handeling terug naar het onderwerp — pronomen + werkwoord.</span>',
        lpd(("8","taalsysteem: reflexieve werkwoorden"), ("3","spreken/schrijven over jezelf")))

# ---- §3.1 ¿Qué es un reflexivo? ----
P('<h3>§3.1 · ¿Qué es un verbo reflexivo?</h3>')
P('<p style="font-size:9.6pt">La acción <b>vuelve al sujeto</b>. Compara: <span class="gloss">de handeling keert terug naar het onderwerp</span></p>')
P('<div class="fams" style="grid-template-columns:1fr 1fr;margin-top:2mm">'
  '<div class="pcard"><div class="t" style="font-size:10.5pt">lavar (iets/iemand anders)</div><div class="ej" style="margin-top:1mm">Lucía <b>lava</b> el coche. <span class="gloss">→ de handeling gaat naar iets anders.</span></div></div>'
  '<div class="pcard"><div class="t" style="font-size:10.5pt">lavar<b>se</b> (jezelf)</div><div class="ej" style="margin-top:1mm">Lucía <b>se lava</b> las manos. <span class="gloss">→ de handeling keert terug naar háár.</span></div></div></div>')
P(machine([("infinitivo","levantar-se"), ("pronombre (yo)","me"), ("+ verbo","me levanto")]))
P(regla("Regla · el pronombre reflexivo", '<table class="conj" style="margin-top:1mm"><thead><tr><th>persona</th><th>pron.</th><th>persona</th><th>pron.</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">me</td><td class="p">nosotros/as</td><td class="v">nos</td></tr>'
  '<tr><td class="p">tú</td><td class="v">te</td><td class="p">vosotros/as</td><td class="v">os</td></tr>'
  '<tr><td class="p">él/ella/usted</td><td class="v">se</td><td class="p">ellos/ustedes</td><td class="v">se</td></tr></tbody></table>'
  '<p style="margin:2mm 0 0">Het pronomen komt <b>vóór</b> het vervoegde werkwoord en <b>past bij het onderwerp</b>: <i>yo <b>me</b> levanto, tú <b>te</b> levantas, él <b>se</b> levanta.</i></p>'))
P(blocks([[("per","yo"),("opt","me"),("vb","levanto")], [("per","tú"),("opt","te"),("vb","levantas")], [("per","ella"),("opt","se"),("vb","levanta")]]))
P(actx(AN(), "Completa con el pronombre reflexivo",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe el pronombre correcto (<b>me · te · se · nos · os · se</b>). <span class="gloss">Vul het juiste pronomen in.</span></p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl sm"></span> levanto a las siete. &nbsp; 2. ¿Tú <span class="wl sm"></span> duchas por la mañana? &nbsp; 3. Mi hermano <span class="wl sm"></span> acuesta tarde.<br>'
  '4. Nosotros <span class="wl sm"></span> lavamos las manos antes de comer. &nbsp; 5. Vosotros <span class="wl sm"></span> vestís elegantes. &nbsp; 6. Mis padres <span class="wl sm"></span> despiertan a las seis.</p>',
  apoyo="Modelo: tabla"))
P(actx(AN(), "¿Reflexivo o no? · clasifica",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Clasifica: <span class="gloss">sorteer deze woorden</span> welke acties zijn <b>reflexief</b> (jezelf) en welke niet? <span class="words"><b>ducharse · desayunar · lavarse · comer · vestirse · hacer los deberes · peinarse · cenar</b></span></p>'
  + sortcols([("reflexivo (me…)",""),("no reflexivo","")], eigen=False), apoyo="Banco de palabras"))
P('</div>')  # sluit .page §3.1

# ---- §3.2 La conjugación (+ cambio vocálico) ----
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3.2 · La conjugación completa</span>')
P('<div class="intro"><b>ES:</b> Ahora conjugamos <b>del todo</b>. Muchos reflexivos de rutina tienen también <b>cambio vocálico</b> (la «bota»): despertar<b>se</b> (e→ie), acostar<b>se</b> (o→ue), vestir<b>se</b> (e→i). <span class="gloss">Nu de volledige vervoeging — met de klinkerwissel («laarsje») bij veel routine-werkwoorden.</span></div>')
P('</div>')
P('<div class="fams" style="grid-template-columns:1fr 1fr;margin-top:2mm">'
  '<div><table class="conj"><thead><tr><th>—</th><th>levantarse</th><th>ducharse</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">me levanto</td><td class="v">me ducho</td></tr>'
  '<tr><td class="p">tú</td><td class="v">te levantas</td><td class="v">te duchas</td></tr>'
  '<tr><td class="p">él/ella</td><td class="v">se levanta</td><td class="v">se ducha</td></tr>'
  '<tr><td class="p">nosotros</td><td class="v">nos levantamos</td><td class="v">nos duchamos</td></tr>'
  '<tr><td class="p">vosotros</td><td class="v">os levantáis</td><td class="v">os ducháis</td></tr>'
  '<tr><td class="p">ellos</td><td class="v">se levantan</td><td class="v">se duchan</td></tr></tbody></table></div>'
  '<div><table class="conj"><thead><tr><th>bota · e→ie</th><th>despertarse</th><th>acostarse (o→ue)</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">me desp<span class="end">ie</span>rto</td><td class="v">me ac<span class="end">ue</span>sto</td></tr>'
  '<tr><td class="p">tú</td><td class="v">te despiertas</td><td class="v">te acuestas</td></tr>'
  '<tr><td class="p">él/ella</td><td class="v">se despierta</td><td class="v">se acuesta</td></tr>'
  '<tr><td class="p">nosotros</td><td class="v">nos despertamos</td><td class="v">nos acostamos</td></tr>'
  '<tr><td class="p">vosotros</td><td class="v">os despertáis</td><td class="v">os acostáis</td></tr>'
  '<tr><td class="p">ellos</td><td class="v">se despiertan</td><td class="v">se acuestan</td></tr></tbody></table></div></div>')
P('<div class="truc"><b>La bota (§4, repaso de U0):</b> la vocal cambia en <b>yo · tú · él · ellos</b>, pero <b>no</b> en <i>nosotros / vosotros</i>: esas cuatro formas dibujan juntas una bota. Con <b>vestirse</b> (e→i): me v<b>i</b>sto, te vistes… nos vestimos. <span class="gloss">De vier vormen die veranderen tekenen samen een laarsje.</span></div>')
P(actx(AN(), "Conjuga · completa la tabla",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Completa la tabla en presente: pronombre reflexivo + forma del verbo. <span class="gloss">Vul de tabel in: pronomen + werkwoordsvorm.</span></p>'
  '<table class="alf"><thead><tr><th>—</th><th>vestirse (e→i)</th><th>acostarse (o→ue)</th><th>peinarse</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td class="p">tú</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td class="p">nosotros</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>',
  apoyo="Modelo: tabla arriba"))
P(actx(AN(), "La gran cloze reflexiva · el presente",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Escribe el verbo reflexivo en presente (pronombre + forma; el infinitivo está entre paréntesis). <span class="gloss">Vul pronomen én vorm in.</span></p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl md"></span> (levantarse) a las siete. &nbsp; 2. ¿Tú <span class="wl md"></span> (ducharse) por la mañana?<br>'
  '3. Lucía <span class="wl md"></span> (despertarse) muy temprano. &nbsp; 4. Nosotros <span class="wl md"></span> (acostarse) a las once.<br>'
  '5. Diego <span class="wl md"></span> (vestirse) rápido. &nbsp; 6. Mis hermanos <span class="wl md"></span> (peinarse) delante del espejo.<br>'
  '7. Yo <span class="wl md"></span> (dormirse) enseguida. &nbsp; 8. ¿Vosotros <span class="wl md"></span> (sentarse) aquí?</p>',
  apoyo="Banco de palabras: me levanto · te duchas · se despierta · nos acostamos · se viste · se peinan · me duermo · os sentáis"))
P(actx(AN(), "Sustitución · cambia la persona",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Modelo: <b>Yo me levanto a las siete y me ducho.</b> Vuelve a escribirla para cada persona. <span class="gloss">Herschrijf de modelzin per persoon.</span></p>'
  '<table class="alf"><thead><tr><th>Persona</th><th>Frase</th></tr></thead><tbody>'
  '<tr><td class="p">tú</td><td>Tú <span class="wl lg"></span></td></tr>'
  '<tr><td class="p">ella</td><td>Ella <span class="wl lg"></span></td></tr>'
  '<tr><td class="p">nosotros</td><td>Nosotros <span class="wl lg"></span></td></tr>'
  '<tr><td class="p">ellos</td><td>Ellos <span class="wl lg"></span></td></tr></tbody></table>',
  apoyo="Marco: me · te · se · nos · os · se + verbo"))
P('</div>')  # sluit .page §3.2

# ---- §3.3 La posición del pronombre + drills ----
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3.3 · La posición del pronombre</span>')
P('<div class="intro"><b>ES:</b> Normalmente el pronombre va <b>antes</b> del verbo: <i>Me ducho</i>. Pero con un <b>infinitivo</b> puede ir en dos sitios: <i>Quiero ducharme</i> = <i>Me quiero duchar</i> (allebei juist). <span class="gloss">Normaal vóór het werkwoord; bij een infinitief mag het op twee plaatsen.</span></div>')
P('</div>')
P('<div class="agree"><div class="w"><u>Me</u> ducho por la mañana.</div><div class="tie">pronombre vóór het vervoegde werkwoord</div></div>')
P('<div class="agree"><div class="w">Quiero ducha<u>rme</u> = <u>Me</u> quiero duchar.</div><div class="tie">bij infinitief: achteraan óf vooraan</div></div>')
P(actx(AN(), "Clínica de errores · busca y corrige",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Elke zin heeft één fout (pronomen of vorm). Verbeter.</p>'
  '<p style="margin-left:12.5mm">1. Yo lavo las manos antes de comer. → <span class="wl md"></span><br>'
  '2. Tú se despiertas muy tarde. → <span class="wl md"></span><br>'
  '3. María me acuesta a las diez. → <span class="wl md"></span><br>'
  '4. Nosotros os vestimos rápido. → <span class="wl md"></span><br>'
  '5. Ellos se levanta temprano. → <span class="wl md"></span></p>',
  apoyo="Pista: kijk naar de persoon → juist pronomen"))
P(actx(AN(), "¿Quién de la clase…? (encuesta)",
  [{"t":"🗣️ Interacción","skill":True},{"t":"👥 Clase"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p><i>Sta op en vraag rond. Schrijf bij elke zin een naam.</i> Sta op en vraag rond: «¿Te acuestas antes de las 22:00?». Schrijf de naam.</p>'
  '<table class="alf"><thead><tr><th>¿Quién de la clase…?</th><th>Nombre</th></tr></thead><tbody>'
  '<tr><td>…se levanta antes de las 6:30</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>…se ducha por la noche</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>…nunca se peina</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>…se acuesta después de medianoche</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>…se viste en menos de cinco minutos</td><td><span class="wl md"></span></td></tr></tbody></table>',
  apoyo=""))
P(actx(AN(), "Escribe tu rutina · 5 verbos reflexivos",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Escribe tu rutina de la mañana con al menos <b>cinco verbos reflexivos</b>, en orden (con conectores) y con la hora. <span class="gloss">Je ochtendroutine met vijf reflexieve werkwoorden.</span></p>'
  '<p style="margin-left:12.5mm" class="gloss">Modelo: <i>Me despierto a las 7:00. Primero me ducho, luego me visto…</i></p>'
  '<div class="wbox"></div>',
  apoyo="Marco: Me despierto a las… · Me ducho… · Después me visto… · Luego…"))
P(actx("★", "Tarea comunicativa · la rutina de tu compañero/a",
  [{"t":"🎙️ Hablar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>Entrevista a tu compañero/a (¿A qué hora te levantas? ¿Te duchas por la mañana o por la noche?) y después escribe sobre él/ella <span class="gloss">interview je buur en schrijf daarna over hem of haar</span> in de <b>3ª persona</b> (se levanta, se ducha…).</p>'
  '<p style="margin-left:12.5mm">Mi compañero/a se llama <span class="wl md"></span>. <span class="wl full"></span><span class="wl full"></span></p>',
  apoyo="Marco: ¿A qué hora te…? — Me… a las… · Él/Ella se… a las…"))
P('<div class="guide"><div class="ic">🎡</div><div><span class="hand">Online:</span> <span class="g">de <b>vervangingsanimatie</b> en het <b>vervoegingswiel</b> op de digitale pagina oefenen elke reflexieve vorm; + cloze-, sorteer- en tetris-spellen (me/te/se…).</span></div></div>')
P('</div>')  # sluit .page §3.3

retos("reflexivos", "§3.4 · Retos — la acción vuelve a mí",
      'Un día <b>del revés</b>, un manual para tu sustituto, y dos compañeros de piso que no se aguantan.',
      'Een omgekeerde dag, een handleiding voor je vervanger, en twee huisgenoten die elkaar niet verdragen.')

# ================= §4 · SER VS ESTAR (contrast) =================
sec_open("4", "§4 · Ser vs estar — el contraste", 'Los dos son «zijn», pero no significan lo mismo. <b>ser</b> = quién o qué <b>eres</b> (permanente, identidad, carácter). <b>estar</b> = <b>dónde</b> estás y <b>cómo</b> te <b>sientes</b> (lugar, estado, ánimo). <span class="gloss">ser = permanent/identiteit · estar = plaats en gevoel. In U0 zag je enkel soy/estoy; nu het volledige contrast.</span>',
        lpd(("8","taalsysteem: ser vs estar"), ("7","woordenschat: sentimientos")))

# ---- §4.1 ¿ser o estar? ----
P('<h3>§4.1 · ¿ser o estar? — el sistema</h3>')
P(fmu('<b>ser</b>: soy · eres · es · somos · sois · son<br><b>estar</b>: estoy · estás · está · estamos · estáis · están',
      'ser = <b>identiteit</b>, herkomst, beroep, <b>karakter</b>.<br>estar = <b>plaats</b>, <b>gevoel</b>, tijdelijke toestand.',
      '¿<b>quién/cómo eres</b>? → ser · ¿<b>dónde/cómo estás</b>? → estar.'))
P('<div class="obsbox"><div class="se" style="margin:0 0 1.5mm">Observa · ser ↔ estar</div>'
  '<div class="ln">Lucía <span class="hl">es</span> simpática. (karakter) &nbsp;↔&nbsp; Lucía <span class="hl">está</span> cansada. (gevoel nu)</div>'
  '<div class="ln">Diego <span class="hl">es</span> de México. (herkomst) &nbsp;↔&nbsp; Diego <span class="hl">está</span> en clase. (plaats)</div>'
  '<div class="obsq">¿Cuál no cambia (permanent) y cuál cambia hoy? <span class="gloss">Welke is permanent en welke geldt enkel nu?</span></div></div>')
P(regla("Regla · ser vs estar", '<p><b>ser</b> → identiteit · herkomst · beroep · <b>karakter</b> · uur/datum: <i>Soy alto. Son las dos.</i><br>'
  '<b>estar</b> → <b>plaats</b> · <b>gevoel/toestand</b> (nu): <i>Estoy en casa. Estoy contento.</i><br>'
  '<span class="gloss">Truc: permanent/eigenschap → <b>ser</b> · tijdelijk/plaats/gevoel → <b>estar</b>.</span></p>'))
P(tree([
  '<b>¿Qué quieres decir?</b>',
  '¿identiteit, herkomst, beroep of <b>karakter</b>? → <span class="yes">ser</span> <span class="res">soy alto, es profesora</span>',
  '¿<b>plaats</b> (dónde)? → <span class="yes">estar</span> <span class="res">estoy en clase</span>',
  '¿<b>gevoel/toestand</b> nu (cómo)? → <span class="yes">estar</span> <span class="res">estoy cansado</span>',
]))
P(actx(AN(), "¿ser o estar? · completa",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escribe la forma correcta de <b>ser</b> o <b>estar</b>. <span class="gloss">Vul de juiste vorm in.</span></p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl sm"></span> estudiante. &nbsp; 2. Mi mochila <span class="wl sm"></span> en clase. &nbsp; 3. Nosotros <span class="wl sm"></span> de Bélgica.<br>'
  '4. ¿Cómo <span class="wl sm"></span> (tú)? — <span class="wl sm"></span> muy bien. &nbsp; 5. El profesor <span class="wl sm"></span> simpático. &nbsp; 6. La ventana <span class="wl sm"></span> abierta.</p>',
  apoyo="Pista: identiteit → ser · plaats/gevoel → estar"))
P(actx(AN(), "Clasifica: ¿ser o estar?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Clasifica los trozos de frase: ¿cuáles piden <b>ser</b> y cuáles <b>estar</b>? <span class="gloss">Welke vragen om ser, welke om estar?</span> <span class="words"><b>de Sevilla · en el instituto · profesor · cansado · simpático · contento · las dos · en casa</b></span></p>'
  + sortcols([("ser (permanent)",""),("estar (plaats/gevoel)","")], eigen=False), apoyo="Banco de palabras"))
P('</div>')  # sluit .page §4.1

# ---- §4.2 Los sentimientos con estar ----
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4.2 · ¿Cómo estás? — los sentimientos</span>')
P('<div class="intro"><b>ES:</b> Para decir <b>cómo te sientes</b> usas <b>estar</b> + adjetivo: <i>estoy contento, estoy cansado</i>. El estado es pasajero → siempre <b>estar</b>. <span class="gloss">Gevoelens = estar + bijvoeglijk naamwoord, dat overeenkomt in geslacht en getal.</span></div>')
P('</div>')
P('<div class="clusters" style="grid-template-columns:1fr 1fr 1fr;margin-top:2mm">'
  '<div class="clu"><div class="ch"><span class="ci">😀</span>+ positivo</div><ul><li>contento/a (blij)</li><li>feliz (gelukkig)</li><li>relajado/a (ontspannen)</li></ul></div>'
  '<div class="clu"><div class="ch"><span class="ci">😔</span>− negativo</div><ul><li>triste (verdrietig)</li><li>cansado/a (moe)</li><li>enfadado/a (boos)</li></ul></div>'
  '<div class="clu"><div class="ch"><span class="ci">😰</span>tensión</div><ul><li>nervioso/a (nerveus)</li><li>estresado/a (gestrest)</li><li>ocupado/a (druk)</li></ul></div></div>')
P('<div class="truc"><b>¡Ojo! concordancia:</b> el adjetivo concuerda: <i>Diego está cansad<b>o</b> · Lucía está cansad<b>a</b></i>. Y fíjate: <b>estar aburrido</b> = aburrirse ahora ≠ <b>ser aburrido</b> = ser una persona aburrida. → §4.3. <span class="gloss">estar aburrido = zich vervelen; ser aburrido = saai zijn.</span></div>')
P(actx(AN(), "¿Cómo están? · completa con estar + adjetivo",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escribe <b>estar</b> + el sentimiento correcto (¡ojo con masculino y femenino!). <span class="gloss">Vul estar en het juiste gevoel in.</span></p>'
  '<p style="margin-left:12.5mm">1. Después de correr, Diego <span class="wl md"></span> (moe). &nbsp; 2. Hoy Lucía <span class="wl md"></span> (blij).<br>'
  '3. Antes del examen, yo <span class="wl md"></span> (nerveus). &nbsp; 4. Los alumnos <span class="wl md"></span> (druk) con los deberes.</p>',
  apoyo="Banco de palabras: está cansado · está contenta · estoy nervioso/a · están ocupados"))
P(actx(AN(), "¿Y tú? · ¿cómo estás en estos momentos?",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escribe cómo te sientes en estas situaciones, con <b>porque</b>. <span class="gloss">Schrijf hoe je je voelt, met een reden.</span></p>'
  '<p style="margin-left:12.5mm">El lunes por la mañana: <span class="wl lg"></span><br>'
  'El viernes por la tarde: <span class="wl lg"></span><br>'
  'Antes de un examen: <span class="wl lg"></span></p>'
  '<p style="margin-left:12.5mm" class="gloss">Modelo: <i>El viernes estoy contento porque no hay clase.</i></p>',
  apoyo="Marco: Por la mañana estoy… · Después del examen estoy… · Los viernes estoy…"))
P('</div>')  # sluit .page §4.2

# ---- §4.3 El contraste es/está ----
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4.3 · El contraste: es aburrido / está aburrido</span>')
P('<div class="intro"><b>ES:</b> Algunos adjetivos <b>cambian de significado</b> con ser o estar. <b>ser aburrido</b> = saai zijn (karakter) · <b>estar aburrido</b> = zich vervelen (nu). ¡El contraste importa! <span class="gloss">Sommige adjectieven veranderen van betekenis: ser = eigenschap, estar = toestand nu.</span></div>')
P('</div>')
P('<div class="fams" style="grid-template-columns:1fr 1fr;margin-top:2mm">'
  '<div class="pcard"><div class="t">La película <b>es</b> aburrida.</div><div class="anchor">= de film is saai <b>(eigenschap)</b>.</div></div>'
  '<div class="pcard"><div class="t">Yo <b>estoy</b> aburrido.</div><div class="anchor">= ik verveel me <b>(nu)</b>.</div></div></div>')
P(vpairs([("es listo <i>(slim)</i>","está listo <i>(klaar)</i>"),("es rico <i>(rijk)</i>","está rico <i>(lekker)</i>"),("es aburrido <i>(saai)</i>","está aburrido <i>(verveelt zich)</i>"),("es bueno <i>(goed mens)</i>","está bueno <i>(lekker/gezond)</i>")]))
P(actx(AN(), "¿es o está? · elige según el significado",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Elige <b>es</b> o <b>está</b> según el significado entre paréntesis. <span class="gloss">Kies volgens de betekenis tussen haakjes.</span></p>'
  '<p style="margin-left:12.5mm">1. La clase <span class="wl sm"></span> aburrida (saai). &nbsp; 2. Estoy en casa y <span class="wl sm"></span> aburrido (verveel me).<br>'
  '3. La paella <span class="wl sm"></span> rica (lekker, nu). &nbsp; 4. Mi tío <span class="wl sm"></span> rico (rijk). &nbsp; 5. ¿Ya <span class="wl sm"></span> lista, Lucía? (klaar).</p>',
  apoyo="Pista: eigenschap → ser · toestand nu → estar"))
P(actx(AN(), "Clínica de errores · ser/estar",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Elke zin heeft één fout (ser/estar). Verbeter.</p>'
  '<p style="margin-left:12.5mm">1. Yo estoy estudiante. → <span class="wl md"></span><br>'
  '2. Mi mochila es en clase. → <span class="wl md"></span><br>'
  '3. Hoy soy muy cansado. → <span class="wl md"></span><br>'
  '4. Sevilla está en el sur de España — dat klopt! ¿verdad o falso? → <span class="wl sm"></span></p>',
  apoyo="Pista: pregúntate si es identidad (ser) o lugar/estado (estar)"))
P(actx("★", "Tarea comunicativa · ¿cómo es y cómo está?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Describe a un compañero/a con <b>ser</b> (2 rasgos) y con <b>estar</b> (cómo se siente ahora). Dilo en voz alta. <span class="gloss">Twee eigenschappen met ser, plus hoe hij of zij zich nu voelt.</span></p>'
  '<p style="margin-left:12.5mm">Mi compañero/a <b>es</b> <span class="wl md"></span> y <span class="wl md"></span>, y hoy <b>está</b> <span class="wl md"></span>.</p>',
  apoyo="Marco: … es … pero hoy está …"))
P('</div>')  # sluit .page §4.3

retos("ser_estar_c6p", "§4.4 · Retos — es aburrido o está aburrido",
      'Doce escenas donde solo el <b>detalle</b> decide, y un termómetro de la clase en cifras.',
      'Twaalf scènes waar enkel het detail beslist, en een klasthermometer in cijfers.')

# ================= §5 · GUSTAR + OI =================
sec_open("5", "§5 · Gustar + OI — me gusta", 'El <b>corazón</b> de la unidad para hablar de <b>gustos</b>. Pero ¡ojo! gustar funciona <b>al revés</b>: <i>Me gusta la música</i> = de muziek bevalt míj. Y al final: <b>«me gusta… porque…»</b>, tu primera opinión. <span class="gloss">Gustar werkt omgekeerd. Op het einde geef je je eerste mening met «porque».</span>',
        lpd(("8","taalsysteem: gustar + OI-pronomina"), ("7","woordenschat: ocio & gustos"), ("3","mening geven")))

# ---- §5.1 gusta/gustan ----
P('<h3>§5.1 · gustar «al revés» — ¿gusta o gustan?</h3>')
P('<div class="fams" style="grid-template-columns:1fr 1fr;margin-top:2mm">'
  '<div class="pcard"><div class="t" style="font-size:10pt">NL / EN</div><div class="ej"><b>Ik</b> vind muziek leuk. <span class="gloss">ik = onderwerp (doet de actie).</span></div></div>'
  '<div class="pcard"><div class="t" style="font-size:10pt">ES — ¡al revés!</div><div class="ej"><b>Me gusta la música.</b> <span class="gloss">la música = onderwerp → het bevalt mij.</span></div></div></div>')
P('<div class="truc"><b>¡Ojo! NUNCA «yo gusto».</b> La persona no hace la acción; la cosa te gusta a ti. Siempre: <b>me gusta, te gusta, le gusta…</b> <span class="gloss">Het ding bevalt jou, jij «gust» niet.</span></div>')
P(regla("Regla · gusta of gustan?", '<p><b>gusta</b> + <b>1 ding</b> (met lidwoord) of een <b>infinitief</b>: <i>Me gusta <b>el</b> fútbol. Me gusta bailar.</i><br>'
  '<b>gustan</b> + <b>meerdere dingen</b> (meervoud): <i>Me gustan <b>los</b> perros.</i><br>'
  '<span class="gloss">Het werkwoord volgt het <b>ding</b> (ev/mv), niet de persoon. Met een sustantivo is het lidwoord verplicht.</span></p>'))
P(machine([("¿1 cosa o infinitivo?","gusta"), ("¿varias cosas?","gustan")]))
P(actx(AN(), "¿gusta o gustan? · rodea la forma",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Elige la forma correcta. <span class="gloss">Kies de juiste vorm.</span></p>'
  '<p style="margin-left:12.5mm">1. Me <span class="wl sm"></span> el fútbol. &nbsp; 2. Me <span class="wl sm"></span> los videojuegos. &nbsp; 3. Me <span class="wl sm"></span> bailar.<br>'
  '4. Me <span class="wl sm"></span> las películas de terror. &nbsp; 5. Me <span class="wl sm"></span> la música. &nbsp; 6. Me <span class="wl sm"></span> cantar y bailar.</p>',
  apoyo="Pista: 1 ding/infinitivo → gusta · meerdere → gustan"))
P(actx(AN(), "Clasifica · me gusta / me gustan",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe cada palabra en su columna. <span class="gloss">zet elk woord in de juiste kolom</span> <span class="words"><b>correr · las flores · el chocolate · los deportes · bailar · las vacaciones · la música · los perros</b></span></p>'
  + sortcols([("Me gusta…","1 ding / infinitivo"),("Me gustan…","meervoud")], eigen=True), apoyo="Banco de palabras"))
P('</div>')  # sluit .page §5.1

# ---- §5.2 los pronombres OI ----
P('<div class="page"><div class="parada sec">')
P('<span class="num">5</span><span class="pk">§5.2 · ¿A quién? — me · te · le · nos · os · les</span>')
P('<div class="intro"><b>ES:</b> Con el pronombre dices <b>a quién</b> le gusta algo: <b>me</b>, <b>te</b>, <b>le</b>, <b>nos</b>, <b>os</b>, <b>les</b>. Para insistir: <i>A mí me gusta…, A Lucía le gusta…</i> <span class="gloss">Het pronomen zegt aan wie iets bevalt; met «a mí» leg je nadruk.</span></div>')
P('</div>')
P('<table class="mp"><thead><tr><th>tónico (opcional)</th><th>átono (verplicht)</th><th>+ gusta / gustan</th></tr></thead><tbody>'
  '<tr><td>(a mí)</td><td class="v"><b>me</b></td><td>gusta el fútbol · gustan los perros</td></tr>'
  '<tr><td>(a ti)</td><td class="v"><b>te</b></td><td>gusta el fútbol · gustan los perros</td></tr>'
  '<tr><td>(a él/ella/usted)</td><td class="v"><b>le</b></td><td>gusta el fútbol · gustan los perros</td></tr>'
  '<tr><td>(a nosotros/as)</td><td class="v"><b>nos</b></td><td>gusta el fútbol · gustan los perros</td></tr>'
  '<tr><td>(a vosotros/as)</td><td class="v"><b>os</b></td><td>gusta el fútbol · gustan los perros</td></tr>'
  '<tr><td>(a ellos/as/ustedes)</td><td class="v"><b>les</b></td><td>gusta el fútbol · gustan los perros</td></tr></tbody></table>')
P('<div class="truc"><b>¡Ojo con «le»!</b> Con un nombre usas <b>le/les</b> + a + nombre: <i>A Diego <b>le</b> gusta el fútbol. A mis padres <b>les</b> gusta viajar.</i> <span class="gloss">Bij een naam komt le of les erbij.</span></div>')
P(actx(AN(), "Completa con el pronombre correcto",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe <b>me · te · le · nos · os · les</b>. <span class="gloss">Vul het juiste pronomen in.</span></p>'
  '<p style="margin-left:12.5mm">1. A mí <span class="wl sm"></span> gusta el cine. &nbsp; 2. A ti <span class="wl sm"></span> gustan los deportes. &nbsp; 3. A Lucía <span class="wl sm"></span> gusta bailar.<br>'
  '4. A nosotros <span class="wl sm"></span> gusta viajar. &nbsp; 5. ¿A vosotros <span class="wl sm"></span> gusta la música? &nbsp; 6. A mis amigos <span class="wl sm"></span> gustan los videojuegos.</p>',
  apoyo="Modelo: tabla"))
P(actx(AN(), "Traduce al español · ¡ojo con la estructura!",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Traduce las cuatro frases al español con gustar: lo que en neerlandés es el objeto, en español es el sujeto. <span class="gloss">Vertaal met gustar; het Nederlandse voorwerp wordt het Spaanse onderwerp.</span></p>'
  '<p style="margin-left:12.5mm">1. Ik hou van honden. → <span class="wl lg"></span><br>'
  '2. Ik vind voetbal leuk. → <span class="wl lg"></span><br>'
  '3. Hij houdt van reizen. → <span class="wl lg"></span><br>'
  '4. Wij vinden horrorfilms niet leuk. → <span class="wl lg"></span></p>',
  apoyo="Pista: Me gustan los perros…"))
P(actx(AN(), "Clínica de errores · gustar",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 3 min"},{"t":"★★★"}],
  '<p>Elke zin heeft één fout (gustar). Verbeter.</p>'
  '<p style="margin-left:12.5mm">1. Yo gusto el fútbol. → <span class="wl md"></span><br>'
  '2. Me gusta los perros. → <span class="wl md"></span><br>'
  '3. Me gusta tenis. → <span class="wl md"></span><br>'
  '4. A María gusta bailar. → <span class="wl md"></span></p>',
  apoyo="Pista: el verbo va con la cosa, no con la persona: me gusta / me gustan"))
P('</div>')  # sluit .page §5.2

# ---- §5.3 la escala + porque + también/tampoco ----
P('<div class="page"><div class="parada sec">')
P('<span class="num">5</span><span class="pk">§5.3 · La escala + «me gusta… porque»</span>')
P('<div class="intro"><b>ES:</b> De <b>me encanta</b> hasta <b>no me gusta nada</b>: la escala de gustos. Y das <b>tu opinión</b>: <b>Me gusta… porque…</b> — je eerste mening (P3). Reageer op anderen: <b>a mí también / a mí tampoco</b>. <span class="gloss">De schaal me encanta → no me gusta nada; je eerste mening met porque; reageren met a mí también/tampoco.</span></div>')
P('</div>')
P('<div class="scale"><div class="track">'
  '<div class="sstop"><div class="sd"></div><div class="sl">me encanta 😍</div><div class="bar"></div></div>'
  '<div class="sstop"><div class="sd"></div><div class="sl">me gusta mucho</div><div class="bar"></div></div>'
  '<div class="sstop"><div class="sd"></div><div class="sl">me gusta 🙂</div><div class="bar"></div></div>'
  '<div class="sstop"><div class="sd"></div><div class="sl">no me gusta</div><div class="bar"></div></div>'
  '<div class="sstop"><div class="sd"></div><div class="sl">no me gusta nada 🙁</div></div></div></div>')
P('<div class="truc"><b>me encanta = el máximo</b> (encantar funciona como gustar: me encanta / me encantan). No lo uses con «mucho» ni en negativo (<span class="trap">me encanta mucho / no me encanta</span>). <span class="gloss">encantar is al het maximum: geen mucho, geen ontkenning.</span></div>')
P(xray('A mí me gusta el fútbol porque es divertido.', [
  ('A mí me', 'aan wie (OI)'), ('gusta', 'ww. (al revés)'), ('el fútbol', 'wat (onderwerp)'), ('porque', 'want/omdat'), ('es divertido', 'reden = mening')]))
P(regla("Mi primera opinión", '<p>Combina una frase con gustar y una razón: <b>Me gusta / No me gusta … porque …</b> <span class="gloss">Combineer een gustar-zin met een reden.</span><br>'
  '<i>Me gusta la música latina <b>porque</b> es alegre. No me gustan los lunes <b>porque</b> estoy cansado/a.</i><br>'
  '<span class="gloss">Zo geef je je eerste mening. In U3 komt «creo que…»; nu volstaat «porque».</span></p>'))
P(actx(AN(), "Reacciona · me gusta… porque…",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Da tu opinión sobre cada tema con la escala <b>y</b> una razón con <b>porque</b>. <span class="gloss">Gebruik de schaal én een reden.</span></p>'
  '<p style="margin-left:12.5mm">El fútbol: <span class="wl lg"></span><br>'
  'La música clásica: <span class="wl lg"></span><br>'
  'Los videojuegos: <span class="wl lg"></span><br>'
  'Levantarse temprano: <span class="wl lg"></span></p>'
  '<p style="margin-left:12.5mm" class="gloss">Modelo: <i>Me encanta el fútbol porque es emocionante.</i></p>',
  apoyo="Marco: Me gusta(n)… porque… · No me gusta(n)… porque…"))
P('<div class="se" style="margin-top:4mm">Reaccionar a los gustos de otro · a mí también / a mí tampoco</div>')
P('<table class="alf"><thead><tr><th>Alguien dice…</th><th>De acuerdo (=)</th><th>En desacuerdo (≠)</th></tr></thead><tbody>'
  '<tr><td>Me gusta el pop. <span class="gloss">(+)</span></td><td><b>A mí también.</b></td><td>A mí no.</td></tr>'
  '<tr><td>No me gusta el jazz. <span class="gloss">(−)</span></td><td><b>A mí tampoco.</b></td><td>A mí sí.</td></tr></tbody></table>')
P('<div class="truc"><b>¡Ojo!</b> Con gustar se dice <b>a mí también</b>, no <span class="trap">yo también</span>, porque gustar lleva <i>a mí</i>. «también» responde a (+) y «tampoco» a (−). <span class="gloss">a mí también, want gustar gaat met a mí.</span></div>')
P(actx(AN(), "Reacciona · ¿a mí también o a mí tampoco?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Je bent het eens. Reageer met <b>A mí también</b> of <b>A mí tampoco</b>.</p>'
  '<p style="margin-left:12.5mm">– Me gusta el pop. → <span class="wl md"></span><br>'
  '– No me gusta el terror. → <span class="wl md"></span><br>'
  '– Me gustan los deportes. → <span class="wl md"></span><br>'
  '– No me gusta la música clásica. → <span class="wl md"></span></p>',
  apoyo="Modelo"))
P(audiorow('<div class="ic">🎵</div><div><b>Escucha «La Perla» (Rosalía)</b> en la página digital. Escribe tu opinión con <b>me gusta / me encanta … porque …</b>, pregunta la suya a tu compañero/a y cuéntalo en <b>3ª persona</b>. <span class="gloss">Luister, geef je mening, vraag die van je buur en vertel ze daarna in de derde persoon.</span></div>',
           qr("Escanea y escucha", "§5 · Canción «La Perla»", seed=103, ancla="c6p-u1-cancion")))
P('</div>')  # sluit .page §5.3

# ================= §6 · LECTURA =================
sec_open("6", "§6 · Lectura 1 — «¿Qué les gusta?»", 'Dos perfiles de la cast: su <b>día</b> y sus <b>gustos</b>. Lee, busca información y reacciona. <span class="gloss">Twee profielen: hun dag en hun smaken. Lezen, informatie zoeken, reageren.</span>',
        lpd(("1","lezen: onderwerp & hoofdgedachte"), ("2","lezen: relevante info selecteren"), ("5","identiteit & cultuur")))
P('<div class="lecdoel"><b>Antes de leer:</b> mira los títulos y las fotos. ¿Qué tipo de texto es? ¿Qué información esperas (rutina, gustos)? <span class="gloss">Kijk vóór het lezen: welk soort tekst? Wat verwacht je?</span></div>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> perfil / blog</span><span class="tm"><b>Fuente:</b> muro de clase</span><span class="tm"><b>Objetivo:</b> conocer su día y sus gustos</span></div>')
P(f'<div class="ptexts">'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["lucia"]}</div><div><div class="nm">Lucía</div><div class="fr">Sevilla 🇪🇸</div></div></div>'
  f'<p>¡Hola! Soy Lucía. Entre semana <span class="evi">me despierto</span> a las siete y <span class="evi">me levanto</span> enseguida. Primero me ducho, luego desayuno tostadas con aceite. A las ocho salgo de casa. Como a las tres — ¡en España comemos tarde! Por la tarde hago los deberes y <span class="evi">me gusta</span> bailar flamenco. Los fines de semana <span class="evi">me acuesto</span> tarde. Hoy estoy contenta porque es viernes.</p></div>'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["diego"]}</div><div><div class="nm">Diego</div><div class="fr">CDMX 🇲🇽</div></div></div>'
  f'<p>¡Qué onda! Soy Diego. Me levanto a las seis y media porque el insti empieza temprano. No desayuno mucho: solo fruta. <span class="evi">Me encantan</span> los videojuegos y el fútbol, pero <span class="evi">no me gusta nada</span> madrugar. Por la tarde <span class="evi">me gusta</span> quedar con amigos. Normalmente me acuesto a las once. Ahora mismo estoy un poco cansado, pero feliz.</p></div></div>')
P(actx(AN(), "Verdadero o falso — con prueba",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>¿Verdadero (V) o falso (F)? Subraya la <b>prueba</b> en el texto y cópiala. <span class="gloss">Waar of niet waar? Onderstreep het bewijs en schrijf het op.</span></p>'
  '<table class="alf"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba (cita del texto)</th></tr></thead><tbody>'
  '<tr><td>A Lucía le gusta bailar.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Diego se levanta a las siete.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>A Diego le gusta madrugar.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Lucía come a las tres.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>',
  apoyo="Modelo"))
P(actx(AN(), "Escanea — completa la ficha",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Busca los datos de cada persona en el texto y completa la tabla. Una palabra o un número por casilla. <span class="gloss">Zoek de gegevens en vul de tabel aan.</span></p>'
  '<table class="alf"><thead><tr><th>—</th><th>Lucía</th><th>Diego</th></tr></thead><tbody>'
  '<tr><td>¿A qué hora se levanta?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>Le gusta(n)…</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>No le gusta…</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>¿Cómo está hoy?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>',
  apoyo=""))
P(actx(AN(), "Reacciona — ¿y tú?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>¿Con quién tienes más en común, con Lucía o con Diego? Escribe 2–3 frases con <b>porque</b> (rutina y gustos). <span class="gloss">Twee tot drie zinnen met porque.</span></p>'
  '<div class="wbox sm"></div>',
  apoyo="Marco: Tengo más en común con … porque …"))
sec_close()

# ================= TALLER DE LENGUA =================
sec_open("T", "Taller de lengua", 'Dos herramientas: la <b>sílaba tónica</b> en los verbos reflexivos (me DUcho, se desPIERta) y los <b>conectores de secuencia</b> para contar tu día en orden. <span class="gloss">Twee taalgereedschappen: klemtoon in reflexieven en verbindingswoorden.</span>')
P('<h3>1 · Ortografía — la sílaba tónica</h3>')
P(regla("¿Dónde va el acento?", '<p>La mayoría de las palabras son <b>llanas</b> (acento en la penúltima sílaba): <b>du</b>-cho, le-<b>van</b>-to. Si la palabra lleva <b>tilde</b>, sigue la tilde: <b>miér</b>-co-les (esdrújula), des-per-<b>tar</b> (aguda).<br>' '<span class="gloss">Reflexieve vormen: me <b>du</b>-cho, se des-<b>pier</b>-ta, nos le-van-<b>ta</b>-mos.</span></p>'))
P(actx(AN(), "Clasifica por el acento",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Clasifica: <span class="gloss">sorteer deze woorden</span> <span class="words"><b>ducho · levanto · miércoles · después · rutina · sábado · reloj · música</b></span></p>'
  + sortcols([("aguda",""),("llana",""),("esdrújula","")], eigen=False), apoyo="Banco de palabras"))
P('<h3 style="margin-top:6mm">2 · Conectores — contar tu día en orden</h3>')
P(colloc("primero · luego · después · más tarde · por último", ["primero = eerst","luego/después = daarna","más tarde = later","antes de + inf.","por último = ten slotte"]))
P('<div class="truc"><b>¡Ojo!</b> «want» y «omdat» son <b>porque</b> (nunca <span class="trap">por que / porqué</span> aquí). «dus» es <b>así que / por eso</b>. <span class="gloss">Eén woord porque; «dus» is así que of por eso.</span></div>')
P(actx(AN(), "Completa con el conector correcto",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Elige entre <span class="gloss">kies uit</span> <b>primero · luego · después · por último · porque</b>.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl sm"></span> me levanto, <span class="wl sm"></span> me ducho y <span class="wl sm"></span> desayuno.<br>'
  '2. <span class="wl sm"></span>, me acuesto. &nbsp; 3. Me gusta el fin de semana <span class="wl sm"></span> no hay clase.</p>',
  apoyo="Banco de palabras"))
sec_close()

# ================= LECTURA 2 · ESCUCHA =================
# Zelfde bron als de hub (lectura_data / escucha_data), zodat papier en scherm
# niet uit elkaar kunnen lopen. Elk op een eigen bladzijde (§14).
P('<div class="page"><div class="parada sec">')
P('<span class="num">6.2</span><span class="pk">§6.2 · Lectura 2 — «Un martes cualquiera»</span>')
P('<div class="intro"><b>ES:</b> Una entrada de blog de verdad. <b>No hace falta entenderlo todo</b> para sacar la información. <span class="gloss">Een echte blogpost. Je hoeft niet alles te begrijpen om de informatie te vinden — let vooral op de uren.</span></div>')
P(PB.lectura_print(LD.C6P_U1, AN()))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">7</span><span class="pk">§7 · Escucha — «Entrevista a un deportista»</span>')
P('<div class="intro"><b>ES:</b> Una periodista entrevista a Hugo, nadador. <b>Escucha primero, escribe después.</b> <span class="gloss">Een schooljournaliste interviewt zwemmer Hugo. Eerst luisteren, dan schrijven; het transcript staat online en gaat pas open ná de taken.</span></div>')
P(PB.escucha_print(ED.C6P_U1, AN()))
P('</div>')

# ================= CULTURA =================
sec_open("C", "Cultura · el horario español", 'En España el <b>horario</b> es diferente: se <b>come</b> a las 2–3 y se <b>cena</b> a las 9–10. Y existe la <b>siesta</b>. Un día hispano no es igual en todos los países. <span class="gloss">In Spanje eet men laat en soms is er een siësta. De dagindeling verschilt per land.</span>',
        lpd(("5","identiteit in diversiteit: la vida cotidiana hispana")))
P('<div class="fams three" style="margin-top:2mm">'
  '<div class="pcard"><div class="t">🍽️ Se come tarde</div><div class="ej" style="margin-top:2mm">In España is <b>la comida</b> (de lunch) de hoofdmaaltijd, om <b>14–15u</b>. <b>La cena</b> is licht en laat: <b>21–22u</b>. Ontbijt (desayuno) is klein.</div><div class="anchor gloss">Compara con tu día: ¿tú a qué hora comes? <span class="gloss">Wanneer eet jij?</span></div></div>'
  '<div class="pcard"><div class="t">😴 La siesta</div><div class="ej" style="margin-top:2mm">Na de comida rusten sommige mensen even (<b>la siesta</b>), vooral in kleine steden en in de zomer. In grote steden werkt bijna niemand nog met siesta.</div><div class="anchor gloss">Mito y realidad: geen siesta voor iedereen!</div></div>'
  '<div class="pcard"><div class="t">🌎 No es igual en todo el mundo</div><div class="ej" style="margin-top:2mm">In <b>México</b> is de hoofdmaaltijd ook rond 14–15u, maar men ontbijt steviger. In veel LatAm-landen eet men vroeger dan in España.</div><div class="anchor gloss">Un día hispano ≠ un solo horario.</div></div></div>')
P('<div class="route-note" style="margin-top:5mm">🗺️ <b>En la web:</b> compara tu horario con el de Lucía (Sevilla) y Diego (CDMX) en la página digital. <span class="gloss">Online: vergelijk jouw dagindeling met die van de cast.</span></div>')
P(actx(AN(), "Compara los horarios",
  [{"t":"🌍 Cultura","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Escribe a qué hora suele ser cada momento en España y en tu casa. <span class="gloss">Schrijf per moment het gebruikelijke uur.</span></p>'
  '<table class="alf"><thead><tr><th>Momento</th><th>En España</th><th>En tu casa</th></tr></thead><tbody>'
  '<tr><td>el desayuno</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>la comida</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>la cena</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>'
  '<p style="margin-left:12.5mm">¿Qué diferencia te sorprende más? <span class="wl lg"></span></p>',
  apoyo="Marco: En España comen a las… pero en Bélgica comemos a las…"))
P(actx(AN(), "Datos curiosos — une país y horario",
  [{"t":"🌍 Cultura","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Une las dos columnas: escribe la letra. <span class="gloss">Verbind en schrijf de letter.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Dato</div><div class="cb short">1. la siesta &nbsp; 2. la comida a las 14–15h &nbsp; 3. la cena a las 21–22h &nbsp; 4. desayuno pequeño</div></div>'
  '<div class="wcol"><div class="ch">Explicación</div><div class="cb short">a. de hoofdmaaltijd &nbsp; b. korte rust na de lunch &nbsp; c. laat en licht &nbsp; d. vaak alleen koffie + tostada</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo="Banco de palabras"))
sec_close()

retos("cultura_c6p1", "Reto — encontrar el hueco imposible",
      'Cuatro agendas y un solo momento. O ninguno — y también hay que <b>demostrarlo</b>.',
      "Vier agenda's en één moment. Of geen enkel — en dat moet je ook bewijzen.")

# ================= TAREA FINAL =================
sec_open("★", "Tarea final · «Mi día a día»", 'Crea tu <b>blog «Mi día a día»</b> para el muro de la clase y preséntalo en pareja: tu rutina (reflexivos), tu hora, cómo te sientes y qué te gusta. <span class="gloss">Maak je dagblog voor de klasmuur en stel het voor in duo.</span>')
P(fmu('tus compañeros de clase (el muro)', 'compartir cómo es un día en tu vida', 'un texto/blog + una presentación oral (± 1 min)'))
P('<ol class="pasos">'
  '<li><b>Planifica.</b> Anota 6–8 acciones de tu día con la hora (me levanto a las…, como a las…).</li>'
  '<li><b>Escribe tu blog</b> (6–8 frases) con <b>verbos reflexivos</b>, <b>conectores</b> (primero, luego, después), <b>la hora</b> y <b>la frecuencia</b> (siempre, a veces).</li>'
  '<li><b>Añade tus gustos y tu ánimo</b>: «Me gusta… porque…» y «Por la mañana estoy…».</li>'
  '<li><b>Preséntalo en pareja</b>: lee tu día en voz alta; tu compañero/a anota una hora y hace una pregunta.</li>'
  '<li><b>Grábate</b> en la página digital, escúchate y vuelve a grabar una vez.</li></ol>')
P('<div class="se" style="margin-top:4mm">Mi día · el borrador <span class="gloss" style="font-size:8pt">· schrijf je 6–8 zinnen (geruit)</span></div><div class="wbox"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba tu «día a día»</b> en la página digital (recorder + rúbrica). Escucha, compara con el modelo y vuelve a grabar.</div>',
           qr("Escanea y graba", "Tarea · Mi día a día", seed=170)))
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Ik gebruik minstens <b>5 reflexieve werkwoorden</b> correct (me/te/se…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik zeg de <b>hora</b> en gebruik <b>conectores</b> (primero, luego…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>ser/estar</b> en <b>gustar</b> correct</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik geef <b>één mening</b> met «me gusta… porque…»</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>presenteer vlot</b> in pareja (± 1 min)</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — el día de mi compañero/a</div>'
  '<table><thead><tr><th>Una cosa que hace igual que yo</th><th>Una pregunta que le hago</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('<div class="truc" style="margin-top:3mm"><b>✍️ Antes de colgar:</b> vuelve a leer tu blog — <i>¿reflexivos correctos? · ¿ser/estar? · ¿gustar con me/te/le? · ¿una opinión con porque?</i> Corrige una cosa: <span class="wl lg"></span> <span class="gloss">Lees na en verbeter één ding.</span></div>')
sec_close()

# ================= REPASO =================
sec_open("✓", "Repaso · lo esencial", 'Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag; de volledige herhaling staat online.</span>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>La hora:</b> es la una · son las dos… · y cuarto/y media/menos cuarto · A las siete me levanto.</li>'
  '<li><b>Reflexivos:</b> pronombre (me·te·se·nos·os·se) + verbo → me levanto, te duchas, se acuesta. Cambio vocálico: me despierto, me acuesto, me visto.</li>'
  '<li><b>Ser vs estar:</b> ser = identiteit/karakter (soy simpático) · estar = plaats/gevoel (estoy en clase, estoy cansado). es aburrido ≠ está aburrido.</li>'
  '<li><b>Gustar + OI:</b> me/te/le/nos/os/les + gusta (1/inf.) / gustan (varios). ¡Al revés! Me gustan los perros.</li>'
  '<li><b>Mi opinión (P3):</b> Me gusta… <b>porque</b>… · A mí también / a mí tampoco.</li>'
  '<li><b>Las trampas:</b> 🔴 nunca «yo gusto» · 🔴 me gusta <b>el</b> fútbol (lidwoord) · 🔴 me/te/se… bij reflexief · 🔴 a mí también (niet yo también).</li></ul></div>')
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> 11 spelletjes met zelfcorrectie (reflexivos, ser/estar, gusta/gustan, la hora, la rutina…).</div>')
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td>de <b>hora</b> zeggen (¿qué hora es? · son las…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>mijn <b>rutina</b> vertellen met <b>reflexieve werkwoorden</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>ser</b> en <b>estar</b> contrasteren (identiteit ↔ plaats/gevoel)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>over mijn <b>gustos</b> praten met <b>gustar + OI</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>een <b>mening</b> geven met «me gusta… porque…»</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil para mí: <span class="wl md"></span> · Lo que quiero practicar más: <span class="wl md"></span></i></div>')
P('<div class="se" style="margin-top:6mm">Auto-test rápido · ¿lo sé? <span class="gloss" style="font-size:8pt">— dek de unit af en probeer uit het hoofd</span></div>')
P('<p style="margin-left:0">1. 7:30 = <span class="wl md"></span><br>'
  '2. yo (levantarse · ducharse · acostarse) = <span class="wl md"></span><br>'
  '3. ser of estar: «Hoy ___ cansado» = <span class="wl sm"></span><br>'
  '4. Me ___ los perros (gusta/gustan) = <span class="wl sm"></span><br>'
  '5. Geef een mening: Me gusta ___ porque ___ = <span class="wl lg"></span></p>')
P('<div class="bridge"><b>» Siguiente parada: U2 «Aquí vivo».</b> Ya cuentas tu día; en <b>U2</b> describes <b>dónde vives</b>: la casa, el barrio y la ciudad, con <b>hay/estar</b> y los pronombres <b>lo/la</b>. ¡Seguimos el viaje! <span class="gloss">In U2: wonen, de buurt en de weg — met hay/estar en lo/la.</span></div>')
sec_close()

# ================= §V VOCABULARIO =================
VOC = json.load(open(f"{HERE}/u1_vocab.json", encoding="utf-8"))
GRP = [("rutina","La rutina · acciones del día"), ("hora","La hora"),
       ("calendario","Días, meses y estaciones"), ("frecuencia","Adverbios de frecuencia"),
       ("conectores","Conectores de secuencia"), ("sentimientos","Sentimientos (estar + adj.)"),
       ("ocio","Ocio y tiempo libre"), ("gustar","Gustar · expresar preferencias")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (begrijpen en zelf gebruiken)")))
P('</div>')
P('<p style="font-size:9.6pt">Las palabras del <b>día a día</b> como red — tres familias que abren la unidad:</p>')
P(clusters([
  ("🔁","La rutina",["me levanto · me ducho","desayuno · como · ceno","me acuesto"],"Wat je elke dag doet."),
  ("😊","¿Cómo estás?",["contento · cansado","nervioso · relajado","estar + adjetivo"],"Hoe je je voelt."),
  ("👍","Gustos",["me gusta · me encanta","no me gusta nada","a mí también"],"Wat je leuk vindt."),
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
  '<p>Escribe la traducción. <span class="gloss">Schrijf de vertaling.</span> me acuesto = <span class="wl md"></span> · a veces = <span class="wl md"></span> · cansado = <span class="wl md"></span> · me encanta = <span class="wl md"></span></p>', apoyo="Modelo"))
P(actx("V.2", "Distinguir — sorteer per familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Clasifica: <span class="gloss">sorteer deze woorden</span> <span class="words"><b>me ducho · siempre · contento · me gusta · me levanto · nunca · nervioso · me encanta</b></span></p>'
  + sortcols([("rutina",""),("frecuencia",""),("sentimiento/gusto","")], eigen=False), apoyo="Banco de palabras"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Completa la palabra en español; tienes la primera letra. <span class="gloss">de beginletter staat erbij</span><br>opstaan = <b>l</b>___ · altijd = <b>s</b>___ · moe = <b>c</b>___ · ik vind leuk = <b>m</b>___ g___<br><span class="wl full"></span></p>', apoyo="Primera letra"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Escribe una frase correcta con <b>me levanto · a las siete · porque</b>.</p><div class="wbox sm"></div>', apoyo=""))
P(actx("V.5", "Comunicar — mi día en 3 frases",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Escribe tres frases sobre tu día (rutina + hora + un gusto) y dilas en voz alta a tu compañero/a. <span class="gloss">Drie zinnen over je dag; zeg ze daarna hardop.</span></p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>', apoyo="Marco: Me levanto a las… · Por la tarde… · Me gusta… porque…"))
P('<div class="se" style="margin-top:6mm">Mi red de palabras <span class="gloss" style="font-size:8pt">— teken je woordennetwerk rond «MI DÍA»: la mañana, la tarde, la noche, mis gustos</span></div>')
P('<div class="wbox lg"></div>')
P(mispal("Mis palabras de la unidad", 7))
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Sigue en la página digital:</span> <span class="g">flip cards (ES↔NL), audio en de 11 spellen bouwen de steun verder af.</span></div></div>')
sec_close()

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
   a.href=URL.createObjectURL(blob); a.download='C6plus_U1_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- OVERRIDE (bladspiegel-hygiëne, U1) ----------
# Voorkom weesregels/orphan-staarten: een activiteit + zijn APOYO-badge blijven samen op één pagina
# (anders spilt de trailing steun-badge alleen op een lege pagina). Tabellen/wboxen niet doorsnijden.
CSS_OVR = (' .act .steun{break-before:avoid;} '
           '.fams,.machine,.obsbox,.scale,.tree,.zoom,.fmu,.xray,.colloc,.clusters,.vpairs,.blocks,.agree{break-inside:avoid;} '
           '.ptexts,.fichacard,.menu,.gustobars{break-inside:avoid;} '
           # trailing slotblokken (guide/verwijzing/bridge) mogen nooit alleen op een pagina spillen:
           ' '
           '')

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Más español en la práctica · C6+ U1 El día a día</title><style>'
        + CSS + CSS_OVR + RP.CSS + PB.CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/C6plus_U1.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes ·", _AN[0], "genummerde oefeningen (excl. V.1–V.5)")
