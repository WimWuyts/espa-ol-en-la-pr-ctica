#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de print-HTML C6plus_U5.html (C6+ · Unidad 5 «Érase una vez») → PDF via Chromium.
# Zelfde componentenkit/CSS als de gelockte golden sample C6+·U0–U4 (geïmporteerd uit gen_u0_print).
# Cursuskleur = paars. Parada 5 = Buenos Aires (Mateo · voseo).
# Kerngrammatica: pretérito indefinido (regular + fuertes) · OD+OI juntos (se lo).
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
import qr_print as QRP; QRP.fijar("C6+", 5)
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
  <div class="tab">U5 · ÉRASE UNA VEZ</div>
  <div class="eyebrow">UNIDAD 5 · LA RUTA · BUENOS AIRES 🇦🇷 · ÉRASE UNA VEZ 📖</div>
  <h1>Érase una vez</h1>
  <div class="sub">El viaje llega a <b>Buenos Aires</b>, con <b>Mateo</b>. Cuentas <b>biografías</b> e <b>historias del pasado</b> con el <b>pretérito indefinido</b> (<b>nació</b> en 1919, <b>escribió</b> novelas, <b>ganó</b> el Mundial, <b>murió</b> en 1990). <span class="gloss">Biografieën en verhalen uit het verleden vertellen.</span></div>
  <div class="q">¿A qué persona famosa admiras? <span style="font-weight:400;opacity:.9">· Welke beroemde persoon bewonder je?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U2 · Aquí vivo</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U3 · Conectados</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U4 · De viaje</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U5 · Érase una vez</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U6 · Cuando era pequeño</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U7 · Opina y cuídate</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 5 · Buenos Aires 🇦🇷.</b> Con <b>Mateo</b> descubres la ciudad del <b>tango</b>: La Boca, Gardel, Evita y, claro, Messi y Maradona. Mateo habla con <b>voseo</b> («vos tenés», «¿de dónde sos?») — un rasgo típico del español rioplatense. <span class="gloss">Bij Mateo ontdek je de tango-stad. Hij spreekt met voseo — typisch voor het Río de la Plata-Spaans.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> Cada persona famosa tiene una <b>historia</b>. Aprendes a contarla con el <b>indefinido</b>: <i>nació, creció, estudió, escribió, ganó, murió</i>. Memorizas las formas <b>fuertes</b> (fue, hizo, tuvo, estuvo, dijo) y combinas los pronombres: «¿La carta? <b>Se la</b> di a Mateo». Al final: escribes <b>una biografía</b>.
      <span class="gloss">Elk beroemd figuur heeft een verhaal. Je leert het vertellen met de indefinido, met de sterke vormen en de dubbele voornaamwoorden. Eindtaak: een biografie.</span></div>
      <div class="ojo"><b>¡Ojo! — dos trampas desde el primer día:</b> ① El <b>indefinido</b> es para hechos <b>cerrados</b> (<i>ayer, en 1982, el año pasado</i>), no para el perfecto (<i>hoy, esta semana</i>). ② <b>hizo</b> va con <b>z</b> (hacer → hizo). <span class="gloss">Afgeronde feiten krijgen het indefinido; let op de spelling van hizo.</span></div>
    </div>
    <div>
      <div class="se">La gente de la ruta</div>
      <div class="cast">
        <div class="pc"><div class="avw">{AV["diego"]}</div><div class="nm">Diego</div><div class="fr">CDMX 🇲🇽</div></div>
        <div class="pc"><div class="avw">{AV["valen"]}</div><div class="nm">Valen</div><div class="fr">Cartagena 🇨🇴</div></div>
        <div class="pc"><div class="avw">{AV["nina"]}</div><div class="nm">Nina</div><div class="fr">Cusco 🇵🇪</div></div>
        <div class="pc"><div class="avw">{AV["mateo"]}</div><div class="nm">Mateo</div><div class="fr">BsAs 🇦🇷 · voseo</div></div>
        <div class="pc tu"><div class="avw">{TU}</div><div class="nm">Tú</div><div class="fr">Flandes 🇧🇪</div></div>
      </div>
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila de historias</span><br><span class="gloss" style="font-size:8.5pt">Vul je rugzak met de verhaalwoorden: nació, ganó, escribió, murió, fue, hizo, se lo — alles om een biografie te vertellen.</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">hablar de biografías y logros</span> (nació, ganó, escribió) <span class="nl">over biografieën & prestaties praten</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar el pretérito indefinido</span> regular (hablé, comí, viví) <span class="nl">de indefinido gebruiken</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">memorizar las formas fuertes</span> (fue, hizo, tuvo, dijo) <span class="nl">de sterke vormen kennen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">combinar los pronombres</span> <b>se lo / se la</b> <span class="nl">se lo/se la gebruiken</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">contar una historia</span> con conectores (primero, después…) <span class="nl">een verhaal vertellen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">crear tu <b>«Una biografía»</b></span> <span class="nl">biografie (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>Biografía</span><span><b>§2</b>Indefinido</span><span><b>§3</b>Se lo/se la</span><span><b>§4</b>Contar</span><span><b>§5</b>Lectura</span><span><b>Taller</b>ortografía</span><span><b>Cultura</b>Figuras</span><span><b>Tarea</b>Biografía</span><span><b>Repaso</b>Semáforo</span>
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
sec_open("0", "§0 · ¡Ponte al día!", 'Venimos del <b>perfecto</b> (U4: he viajado). Ahora, el <b>indefinido</b>: el mismo «qué pasó», pero para hechos <b>cerrados</b> con fecha (ayer, en 1919). <span class="gloss">Van de voltooide tijd (perfecto) naar de afgeronde feiten (indefinido).</span>',
        lpd(("8","taalsysteem: perfecto → indefinido"), ("7","woordenschat")))
P('<div class="truc"><b>Perfecto ↔ indefinido:</b> <b>hoy/esta semana he viajado</b> (perfecto, dichtbij) tegenover <b>ayer/en 2019 viajé</b> (indefinido, afgerond verleden). In U5 vertellen we <b>biografieën</b> → altijd indefinido.</div>')
P(actx(AN(), "¿perfecto o indefinido? (repaso)",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Welke marker hoort bij welke tijd? Vul <b>perfecto</b> of <b>indefinido</b> in.</p>'
  '<p style="margin-left:12.5mm">1. hoy → <span class="wl md"></span> &nbsp; 2. en 1919 → <span class="wl md"></span> &nbsp; 3. esta semana → <span class="wl md"></span><br>'
  '4. ayer → <span class="wl md"></span> &nbsp; 5. el año pasado → <span class="wl md"></span> &nbsp; 6. últimamente → <span class="wl md"></span></p>',
  apoyo="Pista: hoy/esta semana/últimamente → perfecto · en …/ayer/el año pasado → indefinido"))
P(actx(AN(), "Presente → una acción del pasado (repaso)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe dos cosas que hiciste <b>ayer</b> (prueba con una forma de pasado; ahora las practicamos). <span class="gloss">Twee dingen van gisteren.</span></p>'
  '<p style="margin-left:12.5mm">Ayer <span class="wl lg"></span><br>El fin de semana pasado <span class="wl lg"></span></p>',
  apoyo="Marco: hoy hablo → ayer hablé · hoy como → ayer comí"))
sec_close()

# ================= §1 · BIOGRAFÍA Y LOGROS =================
sec_open("1", "§1 · Biografía y logros", 'El vocabulario de una <b>vida</b>: las <b>etapas</b> (nacer, crecer, estudiar, casarse, morir), los <b>logros</b> (ganar, escribir, pintar, descubrir) y las <b>profesiones</b> (el escritor, la pintora, el futbolista). <span class="gloss">De woorden van een levensloop: etappes, prestaties en beroepen.</span>',
        lpd(("7","woordenschat: la biografía"), ("6","literatuur: biografía/personaje")))
P('<div class="se">La vida de una persona <span class="gloss" style="font-size:8pt">— netwerk in clusters</span></div>')
P('<div class="clusters" style="grid-template-columns:1fr 1fr 1fr">'
  '<div class="clu"><div class="ch"><span class="ci">👤</span>Las etapas</div><ul><li>nacer · crecer</li><li>estudiar · casarse</li><li>mudarse · morir</li></ul><div class="ex">Nació en Argentina.</div></div>'
  '<div class="clu"><div class="ch"><span class="ci">🏆</span>Los logros</div><ul><li>ganar · escribir</li><li>pintar · componer</li><li>descubrir · fundar</li></ul><div class="ex">Ganó un premio.</div></div>'
  '<div class="clu"><div class="ch"><span class="ci">🎭</span>Las personas</div><ul><li>el escritor · la pintora</li><li>el cantante · el futbolista</li><li>el científico · el líder</li></ul><div class="ex">Fue un gran escritor.</div></div></div>')
P('<div class="truc"><b>Woordfamilie:</b> escrib<b>ir</b> → el escrit<b>or</b> / la escrit<b>ora</b> · pint<b>ar</b> → el pint<b>or</b> · cant<b>ar</b> → el cant<b>ante</b> · cient<b>ífico</b> ← la cien<b>cia</b>. Het beroep hangt vast aan de actie.</div>')
P(actx(AN(), "Relaciona la persona con su logro",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Une las dos columnas: escribe la letra. <span class="gloss">Verbind en schrijf de letter.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Persona</div><div class="cb short">1. el escritor &nbsp; 2. la pintora &nbsp; 3. el futbolista &nbsp; 4. el cantante</div></div>'
  '<div class="wcol"><div class="ch">Logro</div><div class="cb short">a. ganó el Mundial &nbsp; b. escribió novelas &nbsp; c. compuso canciones &nbsp; d. pintó cuadros</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "Clasifica: ¿etapa, logro o persona?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe cada palabra en su columna: <span class="gloss">zet elk woord in de juiste kolom</span> <span class="words"><b>nacer · ganar · el pintor · casarse · escribir · el cantante · morir · descubrir</b></span></p>'
  + sortcols([("Etapa de la vida",""),("Logro (verbo)",""),("Persona (oficio)","")], eigen=True), apoyo="Banco de palabras"))
P(actx(AN(), "La familia de palabras",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe la profesión. <span class="gloss">Vul het beroep aan.</span></p>'
  '<p style="margin-left:12.5mm">escribir → el <span class="wl sm"></span> · pintar → el <span class="wl sm"></span> · cantar → el <span class="wl sm"></span> · la ciencia → el <span class="wl sm"></span></p>',
  apoyo="Primera letra: e… · p… · c… · c…"))
P(actx(AN(), "Mi persona admirada · escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escribe tres frases sobre una persona que admiras (su profesión y qué hizo). <span class="gloss">Drie zinnen over iemand die je bewondert.</span></p>'
  '<p style="margin-left:12.5mm">Admiro a <span class="wl md"></span>. Fue <span class="wl md"></span>.<br>Es famoso/a porque <span class="wl lg"></span></p>',
  apoyo="Marco: Admiro a… · Nació en… · Fue… · Porque…"))
sec_close()

retos("biografia", "§1.4 · Retos — una vida en objetos y en cifras",
      'El obituario de alguien que <b>nunca fue famoso</b>, un museo de una sola sala, y una biografía contada solo con <b>números</b>.',
      'Het overlijdensbericht van iemand die nooit beroemd werd, een museum van één zaal, en een biografie verteld in enkel cijfers.')

# ================= §2 · PRETÉRITO INDEFINIDO =================
sec_open("2", "§2 · El pretérito indefinido", 'Voor <b>afgeronde feiten</b> in het verleden: de <b>indefinido</b>. Regelmatig: -ar → <b>-é/-aste/-ó…</b>, -er/-ir → <b>-í/-iste/-ió…</b>. <i>Estudió medicina. Escribió novelas. Nació en 1919.</i> <span class="gloss">De onvoltooid verleden tijd voor afgesloten gebeurtenissen.</span>',
        lpd(("8","taalsysteem: indefinido regular"), ("7","woordenschat: la vida"), ("3","vertellen")))

# §2.1 el sistema
P('<h3>§2.1 · Las formas regulares — la máquina del pasado</h3>')
P(obsbox([
  'Gabriel García Márquez <span class="hl">nació</span> en 1927 y <span class="hl">escribió</span> muchas novelas.',
  'Frida Kahlo <span class="hl">pintó</span> autorretratos y <span class="hl">tuvo</span> una vida difícil.',
  'Ayer (yo) <span class="hl">estudié</span> y <span class="hl">comí</span> en casa.',
], vragen='¿Cómo terminan los verbos en -ar? ¿Y los de -er/-ir? Fíjate en el acento. <span class="gloss">Kijk naar de uitgangen en de klemtoon.</span> <span class="gloss">-ar → -é/-ó · -er/-ir → -í/-ió.</span>'))
P(machine([("-ar hablar","raíz habl-"),("+ -é/-aste/-ó…","habló")]))
P(machine([("-er/-ir comer","raíz com-"),("+ -í/-iste/-ió…","comió")]))
P(regla("Regla · indefinido regular", '<table class="conj" style="margin-top:1mm"><thead><tr><th>Persona</th><th>-ar (hablar)</th><th>-er/-ir (comer/vivir)</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">hablé</td><td class="v">comí / viví</td></tr>'
  '<tr><td class="p">tú</td><td class="v">hablaste</td><td class="v">comiste / viviste</td></tr>'
  '<tr><td class="p">él/ella</td><td class="v">habló</td><td class="v">comió / vivió</td></tr>'
  '<tr><td class="p">nosotros/as</td><td class="v">hablamos</td><td class="v">comimos / vivimos</td></tr>'
  '<tr><td class="p">vosotros/as</td><td class="v">hablasteis</td><td class="v">comisteis / vivisteis</td></tr>'
  '<tr><td class="p">ellos/ellas</td><td class="v">hablaron</td><td class="v">comieron / vivieron</td></tr></tbody></table>'
  '<p style="margin:2mm 0 0"><span class="gloss">🔴 De klemtoon staat op de uitgang: habl<b>é</b>, habl<b>ó</b>, com<b>í</b>, com<b>ió</b>. -er en -ir hebben dezelfde uitgangen.</span></p>'))
P(actx(AN(), "Forma el indefinido (regular)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Forma el indefinido de los verbos regulares. <b>Ojo con la tilde</b> en yo y en él/ella. <span class="gloss">Let op het accent bij yo en él/ella.</span></p>'
  '<p style="margin-left:12.5mm">ganar → <span class="wl sm"></span> &nbsp; escribir → <span class="wl sm"></span> &nbsp; nacer → <span class="wl sm"></span><br>'
  'estudiar → <span class="wl sm"></span> &nbsp; vivir → <span class="wl sm"></span> &nbsp; pintar → <span class="wl sm"></span></p>',
  apoyo="Modelo: -ó / -ió"))
P(actx(AN(), "La gran cloze · indefinido (biografía)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Escribe el <b>indefinido</b> (el infinitivo está entre paréntesis). <span class="gloss">Vul de verleden tijd in.</span></p>'
  '<p style="margin-left:12.5mm">1. García Márquez <span class="wl md"></span> (nacer) en Colombia. &nbsp; 2. <span class="wl md"></span> (escribir) «Cien años de soledad».<br>'
  '3. Frida Kahlo <span class="wl md"></span> (pintar) autorretratos. &nbsp; 4. Messi <span class="wl md"></span> (ganar) el Mundial.<br>'
  '5. (Yo) <span class="wl md"></span> (estudiar) mucho ayer. &nbsp; 6. Nosotros <span class="wl md"></span> (comer) en el centro.<br>'
  '7. Gardel <span class="wl md"></span> (vivir) en Buenos Aires. &nbsp; 8. ¿(Tú) <span class="wl md"></span> (viajar) el año pasado?</p>',
  apoyo="Banco de palabras: nació · escribió · pintó · ganó · estudié · comimos · vivió · viajaste"))
P(actx(AN(), "Sustitución · cambia la persona",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Modelo: <b>Yo estudié y trabajé.</b> Vuelve a escribirla para cada persona. <span class="gloss">Herschrijf de modelzin per persoon.</span></p>'
  '<p style="margin-left:12.5mm">tú → <span class="wl md"></span> &nbsp; ella → <span class="wl md"></span> &nbsp; nosotros → <span class="wl md"></span> &nbsp; ellos → <span class="wl md"></span></p>',
  apoyo="Primera letra: estudiaste y trabajaste…"))
P('</div>')

# §2.2 fuertes + cloze
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2.2 · Los pretéritos fuertes (irregulares)</span>')
P('<div class="intro"><b>ES:</b> Algunos verbos muy frecuentes son <b>irregulares</b> y no llevan acento en yo/él: <b>ser/ir → fue</b>, <b>hacer → hizo</b> (con z), <b>tener → tuvo</b>, <b>estar → estuvo</b>, <b>decir → dijo</b>, <b>venir → vino</b>, <b>poder → pudo</b>, <b>dar → dio</b>, <b>ver → vio</b>. <span class="gloss">De sterke onregelmatige vormen — uit het hoofd.</span></div>')
P('</div>')
P('<table class="conj"><thead><tr><th>Infinitivo</th><th>yo</th><th>él/ella</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td>ser / ir</td><td class="v">fui</td><td class="v">fue</td><td class="gloss">Fue presidente.</td></tr>'
  '<tr><td>hacer</td><td class="v">hice</td><td class="v">hizo</td><td class="gloss">Hizo historia.</td></tr>'
  '<tr><td>tener</td><td class="v">tuve</td><td class="v">tuvo</td><td class="gloss">Tuvo éxito.</td></tr>'
  '<tr><td>estar</td><td class="v">estuve</td><td class="v">estuvo</td><td class="gloss">Estuvo en Europa.</td></tr>'
  '<tr><td>decir</td><td class="v">dije</td><td class="v">dijo</td><td class="gloss">Dijo la verdad.</td></tr>'
  '<tr><td>venir</td><td class="v">vine</td><td class="v">vino</td><td class="gloss">Vino a la ciudad.</td></tr>'
  '<tr><td>dar</td><td class="v">di</td><td class="v">dio</td><td class="gloss">Dio un concierto.</td></tr></tbody></table>')
P('<div class="truc"><b>¡Ojo!</b> <b>hizo</b> con <b>z</b>, no <span class="trap">hició</span> · <b>fue</b> vale para «was» (ser) y para «ging» (ir): <i>Fue médico / Fue a París</i>. Sin tilde: fue, hizo, tuvo, dio, vio. <span class="gloss">fue is zowel «was» als «ging»; deze vormen krijgen geen accent.</span></div>')
P(actx(AN(), "Empareja: infinitivo ↔ indefinido (él)",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Une cada verbo con su forma de él/ella. <span class="gloss">Verbind met de él/ella-vorm.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Infinitivo</div><div class="cb short">1. hacer &nbsp; 2. ser/ir &nbsp; 3. tener &nbsp; 4. decir &nbsp; 5. venir</div></div>'
  '<div class="wcol"><div class="ch">Indefinido</div><div class="cb short">a. tuvo &nbsp; b. vino &nbsp; c. hizo &nbsp; d. dijo &nbsp; e. fue</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span> 5-<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "Cloze · pretéritos fuertes",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>cloze (irregulares).</i> Escribe el <b>indefinido</b>. <span class="gloss">Vul de verleden tijd in.</span></p>'
  '<p style="margin-left:12.5mm">1. Evita <span class="wl md"></span> (ser) muy importante. &nbsp; 2. Maradona <span class="wl md"></span> (hacer) el «gol del siglo».<br>'
  '3. (Yo) <span class="wl md"></span> (tener) un buen día. &nbsp; 4. Gardel <span class="wl md"></span> (ir) a París.<br>'
  '5. El equipo <span class="wl md"></span> (estar) en la final. &nbsp; 6. Ella me <span class="wl md"></span> (dar) un regalo.</p>',
  apoyo="Banco de palabras: fue · hizo · tuve · fue · estuvo · dio"))
P(actx(AN(), "Del presente al indefinido · transforma",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Vuelve a escribir la frase en indefinido (ayer / el año pasado). <span class="gloss">Herschrijf in de verleden tijd.</span></p>'
  '<p style="margin-left:12.5mm">1. Hace historia. → El año pasado <span class="wl md"></span><br>'
  '2. Va a París. → En 1933 <span class="wl md"></span> a París.<br>'
  '3. Tiene mucho éxito. → <span class="wl md"></span> mucho éxito.</p>',
  apoyo="Primera letra: hizo · fue · tuvo"))
P('</div>')

# §2.3 practicar + tarea com
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2.3 · Practicar el indefinido</span>')
P('<div class="intro"><b>ES:</b> Ahora entrenamos: corregir, cambiar la persona y contar una vida de verdad. <span class="gloss">Verbeteren, van persoon wisselen en een echt leven vertellen.</span></div>')
P('</div>')
P(actx(AN(), "Clínica de errores · el indefinido",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Elke zin heeft één fout (vorm of accent). Verbeter.</p>'
  '<p style="margin-left:12.5mm">1. Nació en 1919 y hació muchas cosas. → <span class="wl md"></span><br>'
  '2. Frida pintó y tenió una vida difícil. → <span class="wl md"></span><br>'
  '3. Yo estudie mucho ayer. → <span class="wl md"></span><br>'
  '4. Messi ganó y fui campeón. → <span class="wl md"></span></p>',
  apoyo="Pista: hizo · tuvo · estudié · fue"))
P(actx(AN(), "Sustitución · cambia la persona",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Modelo: <b>Yo escribí una carta.</b> Vuelve a escribirla para cada persona. <span class="gloss">Herschrijf de modelzin per persoon.</span></p>'
  '<p style="margin-left:12.5mm">tú → <span class="wl md"></span> &nbsp; ella → <span class="wl md"></span> &nbsp; nosotros → <span class="wl md"></span> &nbsp; ellos → <span class="wl md"></span></p>',
  apoyo="Primera letra: escribiste…"))
P(actx("★", "Tarea comunicativa · ¿qué hiciste ayer?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>Pregunta a tu compañero/a qué hizo ayer (¿qué hiciste ayer?) y contesta con el <b>indefinido</b>. Anota dos cosas. <span class="gloss">Vraag wat je buur gisteren deed; noteer twee dingen.</span></p>'
  '<p style="margin-left:12.5mm">— ¿Qué hiciste ayer? — <span class="wl lg"></span></p>'
  '<p style="margin-left:12.5mm">Mi compañero/a: 1. <span class="wl full"></span>2. <span class="wl full"></span></p>',
  apoyo="Marco: Ayer… · Después… · ¿Y tú, qué hiciste?"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha «¿Quién fue…?»</b> en la web (TTS): una minibiografía misteriosa. <b>1ª vez:</b> ¿de qué oficio habla? · <b>2ª vez:</b> ¿qué hizo? Escribe los datos.</div>',
           qr("Escanea y escucha", "§2 · ¿Quién fue…?", seed=501)))
P('</div>')

retos("indefinido", "§2.4 · Retos — lo que pasó de verdad",
      'Ocho hechos de una vida, de los que <b>dos no ocurrieron nunca</b>, y una silla donde se sienta un personaje histórico.',
      'Acht feiten uit één leven, waarvan er twee nooit gebeurden, en een stoel waarop een historisch personage plaatsneemt.')

# ================= §3 · OD+OI JUNTOS (se lo) =================
sec_open("3", "§3 · Los pronombres juntos — se lo / se la", 'Cuando juntas el <b>OI (le/les)</b> con el <b>OD (lo/la)</b>, <b>le/les</b> se convierte en <b>se</b>. <i>Le di el libro → <b>Se lo</b> di.</i> <span class="gloss">le + lo wordt se lo: eerst wie ontvangt, dan wat.</span>',
        lpd(("8","taalsysteem: OD+OI se lo"), ("7","woordenschat")))

# §3.1 qué es
P('<h3>§3.1 · ¿Por qué «se»?</h3>')
P('<p style="font-size:9.6pt">Cuando <b>le/les</b> (a quién) se junta con <b>lo/la/los/las</b> (qué), <b>le/les</b> pasa a <b>se</b> (para evitar «le lo»). El orden es: <b>se + lo/la</b> + verbo. <span class="gloss">le + lo wordt se lo.</span></p>')
P('<div class="agree"><div class="w">Di el libro <u>a Mateo</u> → <u>Le</u> di el libro → <u>Se lo</u> di.</div><div class="tie">le + lo → se lo</div></div>')
P('<div class="agree"><div class="w">Mandé las fotos <u>a Nina</u> → <u>Se las</u> mandé.</div><div class="tie">le + las → se las</div></div>')
P(regla("Regla · se lo / se la / se los / se las", '<table class="conj" style="margin-top:1mm"><thead><tr><th>OI + OD</th><th>Resultado</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="p">le/les + lo</td><td class="v">se lo</td><td>¿El libro? Se lo di.</td></tr>'
  '<tr><td class="p">le/les + la</td><td class="v">se la</td><td>¿La carta? Se la mandé.</td></tr>'
  '<tr><td class="p">le/les + los</td><td class="v">se los</td><td>¿Los discos? Se los presté.</td></tr>'
  '<tr><td class="p">le/les + las</td><td class="v">se las</td><td>¿Las fotos? Se las enseñé.</td></tr></tbody></table>'
  '<p style="margin:2mm 0 0"><span class="gloss">Volgorde: <b>se</b> (aan wie) + <b>lo/la</b> (wat) + werkwoord. Bij infinitivo mag het achteraan vast: <i>dár<b>selo</b> = <b>se lo</b> voy a dar</i>.</span></p>'))
P(mirror([("¿El regalo? (a él)", "Se lo di."), ("¿Las llaves? (a ella)", "Se las di.")]))
P(actx(AN(), "¿lo, la, los o las? (con se)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>kies het OD-deel na «se».</i></p>'
  '<p style="margin-left:12.5mm">1. ¿El libro? Se <span class="wl sm"></span> di a Mateo. &nbsp; 2. ¿La carta? Se <span class="wl sm"></span> mandé.<br>'
  '3. ¿Los discos? Se <span class="wl sm"></span> presté. &nbsp; 4. ¿Las fotos? Se <span class="wl sm"></span> enseñé.<br>'
  '5. ¿El secreto? Se <span class="wl sm"></span> conté. &nbsp; 6. ¿La noticia? Se <span class="wl sm"></span> dije.</p>',
  apoyo="Modelo: el→lo · la→la · los→los · las→las"))
P(actx(AN(), "Empareja: pregunta ↔ respuesta (se lo)",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Une cada pregunta con su respuesta. <span class="gloss">Verbind vraag en antwoord.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Pregunta</div><div class="cb short">1. ¿El libro a Mateo? &nbsp; 2. ¿La carta a Nina? &nbsp; 3. ¿Los discos a Diego? &nbsp; 4. ¿Las fotos a Valen?</div></div>'
  '<div class="wcol"><div class="ch">Respuesta</div><div class="cb short">a. Se las enseñé. &nbsp; b. Se lo di. &nbsp; c. Se los presté. &nbsp; d. Se la mandé.</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "Transforma · usa se lo / se la",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Vervang OI + OD door <b>se + lo/la/los/las</b>.</p>'
  '<p style="margin-left:12.5mm">1. Di el libro a Mateo. → <span class="wl md"></span><br>'
  '2. Mandé las fotos a Nina. → <span class="wl md"></span><br>'
  '3. Conté la historia a mis amigos. → <span class="wl md"></span><br>'
  '4. Presté los discos a Diego. → <span class="wl md"></span></p>',
  apoyo="Primera letra: Se lo di…"))
P('</div>')

# §3.2 practicar + tarea com
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3.2 · Practicar se lo / se la</span>')
P('<div class="intro"><b>ES:</b> Entrenamos con corrección y producción propia. <span class="gloss">Verbeteren en zelf produceren.</span></div>')
P('</div>')
P(actx(AN(), "Responde con se lo/se la (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Antwoord met <b>se + lo/la/los/las</b> + het werkwoord.</p>'
  '<p style="margin-left:12.5mm">1. ¿Diste el libro a Mateo? — Sí, <span class="wl md"></span> di. &nbsp; 2. ¿Mandaste la carta a Nina? — Sí, <span class="wl md"></span> mandé.<br>'
  '3. ¿Contaste el secreto a Diego? — Sí, <span class="wl md"></span> conté. &nbsp; 4. ¿Enseñaste las fotos a Valen? — Sí, <span class="wl md"></span> enseñé.</p>',
  apoyo="Banco de palabras: se lo · se la · se lo · se las"))
P(actx(AN(), "Clínica de errores · se lo",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 3 min"},{"t":"★★★"}],
  '<p>Elke zin heeft één fout (le lo → se lo, of volgorde). Verbeter.</p>'
  '<p style="margin-left:12.5mm">1. ¿El libro? Le lo di. → <span class="wl md"></span><br>'
  '2. ¿La carta? Se le mandé. → <span class="wl md"></span><br>'
  '3. ¿Las fotos? Se lo enseñé. → <span class="wl md"></span></p>',
  apoyo="Pista: Se lo di · Se la mandé · Se las enseñé"))
P(actx("★", "Tarea comunicativa · ¿se lo diste?",
  [{"t":"🗣️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Pregunta a tu compañero/a si le dio o le mandó algo a alguien y contesta con <b>se lo/se la</b>: «¿El regalo a tu madre? — Sí, se lo di.» <span class="gloss">Vraag en antwoord met se lo / se la.</span> Noteer 3 antwoorden.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>',
  apoyo="Marco: ¿Se lo diste? — Sí, se lo di / No, no se lo di"))
P('<div class="guide"><div class="ic">🎡</div><div><span class="hand">Online:</span> <span class="g">de <b>dubbele-vervangingsanimatie</b> en de spellen op de hub oefenen se lo/se la; + cloze en foutenkliniek.</span></div></div>')
P('</div>')

retos("se_lo", "§3.4 · Reto — se lo di a…",
      'Cinco objetos recorren la clase y al final <b>nadie sabe dónde acabaron</b>.',
      'Vijf voorwerpen gaan de klas rond en op het eind weet niemand waar ze belandden.')

# ================= §4 · CONTAR UNA HISTORIA =================
sec_open("4", "§4 · Contar una historia", 'Para contar una <b>historia</b>: los <b>conectores</b> de orden (primero, después, entonces, al final) y la estructura «érase una vez… al final». <span class="gloss">De verhaalconnectoren om een biografie of leyenda te structureren.</span>',
        lpd(("6","literatuur: leyenda/relato"), ("3","schrijven: een verhaal"), ("4","interactie")))
P('<div class="se">Los conectores del relato</div>')
P('<div class="fams three" style="margin-top:1mm">'
  '<div class="pcard"><div class="t">Empezar</div><div class="ej">érase una vez · primero · al principio</div></div>'
  '<div class="pcard"><div class="t">Seguir</div><div class="ej">después · luego · entonces · más tarde</div></div>'
  '<div class="pcard"><div class="t">Terminar</div><div class="ej">al final · por eso · y así</div></div></div>')
P('<div class="truc"><b>Chunks:</b> <b>Érase una vez…</b> · <b>Primero nació en…</b> · <b>Después estudió…</b> · <b>Entonces empezó su carrera…</b> · <b>Al final, murió en…</b> · <b>Por eso es famoso/a.</b></div>')
P(actx(AN(), "Ordena la biografía (1–5)",
  [{"t":"🔢 Ordenar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Ordena la biografía (1–5). <span class="gloss">Zet de biografie in volgorde.</span></p>'
  '<p style="margin-left:12.5mm">'
  '<span class="wl sm"></span> Al final, murió en 2014, muy famoso.<br>'
  '<span class="wl sm"></span> Nació en Colombia en 1927.<br>'
  '<span class="wl sm"></span> Entonces escribió «Cien años de soledad».<br>'
  '<span class="wl sm"></span> Primero estudió y trabajó de periodista.<br>'
  '<span class="wl sm"></span> Después ganó el premio Nobel.</p>',
  apoyo="Pista: nació → estudió → escribió → Nobel → murió"))
P(actx(AN(), "Completa el relato con conectores",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Completa con <b>érase una vez · primero · después · entonces · al final</b>. <span class="gloss">Vul de vertelwoorden aan.</span></p>'
  '<p style="margin-left:12.5mm"><span class="wl md"></span> un niño pobre. <span class="wl sm"></span> creció en un pueblo. <span class="wl sm"></span> se mudó a la ciudad. <span class="wl sm"></span> empezó a cantar. <span class="wl sm"></span>, se hizo famoso.</p>',
  apoyo="Banco de palabras"))
P(actx(AN(), "Dictado · una minibiografía",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escucha y escribe las cinco frases (con el indefinido). <span class="gloss">Luister en schrijf de vijf zinnen.</span></p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span>4. <span class="wl full"></span>5. <span class="wl full"></span></p>',
  apoyo="docent/audio leest voor"))
P(actx("★", "Info-gap · adivina el personaje",
  [{"t":"🗣️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>A describe a un personaje con el indefinido (nació…, ganó…, escribió…) sin decir el nombre; B adivina. Después cambiad. <span class="gloss">A beschrijft zonder naam, B raadt.</span> Noteer wie het is.</p>'
  '<p style="margin-left:12.5mm">Personaje 1: <span class="wl full"></span>Personaje 2: <span class="wl full"></span></p>',
  apoyo="Marco: Nació en… · Trabajó como… · Escribió/pintó/ganó…"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha «Una leyenda del tango»</b> en la web (TTS). <b>1ª vez:</b> ¿de quién habla? · <b>2ª vez:</b> ordena los hechos de su vida.</div>',
           qr("Escanea y escucha", "§4 · Una leyenda", seed=502)))
sec_close()

retos("historia_c6p", "§4.4 · Retos — contar y comprobar",
      'Una leyenda con el orden <b>cambiado</b>, dos versiones del mismo día que no coinciden, y una efeméride en treinta segundos.',
      'Een legende met omgegooide volgorde, twee versies van dezelfde dag die niet overeenkomen, en een gedenkdag in dertig seconden.')

# ================= §5 · LECTURA =================
sec_open("5", "§5 · Lectura 1 — «Una vida de película»", 'Dos minibiografías de figuras hispanas. Lee, busca información y reacciona. <span class="gloss">Twee korte biografieën van Spaanstalige figuren. Lezen, info zoeken, reageren.</span>',
        lpd(("1","lezen: hoofdgedachte"), ("2","lezen: info selecteren"), ("6","literatuur"), ("5","identiteit & cultuur")))
P('<div class="lecdoel"><b>Antes de leer:</b> mira los nombres. ¿Qué sabes ya de estas personas? <span class="gloss">Wat weet je al?</span></div>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> biografía</span><span class="tm"><b>Fuente:</b> enciclopedia juvenil</span><span class="tm"><b>Objetivo:</b> conocer una vida</span></div>')
P(f'<div class="ptexts">'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["mateo"]}</div><div><div class="nm">Frida Kahlo</div><div class="fr">México 🇲🇽</div></div></div>'
  f'<p>Frida Kahlo <span class="evi">nació</span> en México en 1907. De joven <span class="evi">tuvo</span> un accidente grave y, durante su recuperación, <span class="evi">empezó</span> a pintar. <span class="evi">Pintó</span> muchos autorretratos con colores fuertes. <span class="evi">Se casó</span> con el pintor Diego Rivera. <span class="evi">Fue</span> una artista única y hoy es un icono. <span class="evi">Murió</span> en 1954.</p></div>'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["mateo"]}</div><div><div class="nm">Lionel Messi</div><div class="fr">Argentina 🇦🇷</div></div></div>'
  f'<p>Lionel Messi <span class="evi">nació</span> en Rosario, Argentina, en 1987. De niño <span class="evi">jugó</span> en un equipo local y luego <span class="evi">se mudó</span> a Barcelona. <span class="evi">Ganó</span> muchos títulos y en 2022 <span class="evi">fue</span> campeón del Mundo. Mucha gente <span class="evi">dijo</span> que <span class="evi">hizo</span> historia. Para muchos, es el mejor de todos los tiempos.</p></div></div>')
P(actx(AN(), "Verdadero o falso — con prueba",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>¿Verdadero (V) o falso (F)? Subraya la prueba. <span class="gloss">Waar of niet waar? Onderstreep het bewijs.</span></p>'
  '<table class="alf"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba (cita)</th></tr></thead><tbody>'
  '<tr><td>Frida empezó a pintar después de un accidente.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Messi nació en Buenos Aires.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Messi fue campeón del Mundo en 2022.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>',
  apoyo="Modelo"))
P(actx(AN(), "Escanea — completa la ficha",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Busca los datos de cada persona en el texto y completa la tabla. Una palabra o un número por casilla. <span class="gloss">Zoek de gegevens en vul de tabel aan.</span></p>'
  '<table class="alf"><thead><tr><th>—</th><th>Frida</th><th>Messi</th></tr></thead><tbody>'
  '<tr><td>¿Dónde y cuándo nació?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>¿Qué hizo (logro)?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>¿Por qué es famoso/a?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>',
  apoyo=""))
P(actx(AN(), "Reacciona — tu opinión",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>¿A quién admiras más? Escribe 2–3 frases con <b>creo que fue… porque…</b>. <span class="gloss">Twee tot drie zinnen met je mening.</span></p>'
  '<div class="wbox sm"></div>',
  apoyo="Marco: Admiro a … Creo que fue … porque …"))
sec_close()

# ================= TALLER =================
sec_open("T", "Taller de lengua", 'Twee gereedschappen: de <b>spellingwissels</b> in de indefinido (c→qu, g→gu, z→c) en de <b>verhaalconnectoren</b>. <span class="gloss">De spellingveranderingen bij de yo-vorm + de connectoren.</span>')
P('<h3>1 · Ortografía — c→qu / g→gu / z→c (yo)</h3>')
P(regla("Para conservar el sonido", '<p>Bij <b>yo</b> in de indefinido verandert de spelling om de klank te bewaren: <b>c → qu</b> (buscar → bus<b>qu</b>é), <b>g → gu</b> (llegar → lle<b>gu</b>é), <b>z → c</b> (empezar → empe<b>c</b>é).<br><span class="gloss">Enkel bij <b>yo</b>! (buscó blijft met c). Zo: sacar → saqué, jugar → jugué, tocar → toqué.</span></p>'))
P(actx(AN(), "Escribe la forma «yo»",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Vorm de <b>yo</b>-vorm van de indefinido.</p>'
  '<p style="margin-left:12.5mm">buscar → <span class="wl sm"></span> · llegar → <span class="wl sm"></span> · empezar → <span class="wl sm"></span> · sacar → <span class="wl sm"></span> · jugar → <span class="wl sm"></span></p>',
  apoyo="Modelo: c → qu · g → gu · z → c vóór -é"))
P('<h3 style="margin-top:6mm">2 · Conectores del relato</h3>')
P(colloc("primero · después · entonces · al final", ["primero = eerst","después/luego = daarna","entonces = toen/dus","al final = uiteindelijk"]))
P(actx(AN(), "Une el conector con su función",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Une las dos columnas: escribe la letra. <span class="gloss">Verbind en schrijf de letter.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Conector</div><div class="cb short">1. érase una vez &nbsp; 2. después &nbsp; 3. al final &nbsp; 4. por eso</div></div>'
  '<div class="wcol"><div class="ch">Función</div><div class="cb short">a. gevolg (daarom) &nbsp; b. begin (er was eens) &nbsp; c. einde (uiteindelijk) &nbsp; d. vervolg (daarna)</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
sec_close()

# ================= LECTURA 2 · ESCUCHA =================
# Zelfde bron als de digitale hub (lectura_data / escucha_data): papier en scherm
# kunnen zo niet uit elkaar lopen. Elk op een eigen bladzijde (§14).
P('<div class="page"><div class="parada sec">')
P('<span class="num">6</span><span class="pk">§6 · Lectura 2 — «La leyenda de la yerba mate»</span>')
P('<div class="intro"><b>ES:</b> Una leyenda guaraní contada entera en indefinido. <b>No hace falta entenderlo todo</b> para seguir la historia. <span class="gloss">Een Guaraní-legende, volledig in het indefinido. Je hoeft niet alles te begrijpen om het verhaal te volgen — let op de volgorde van de gebeurtenissen.</span></div>')
P(PB.lectura_print(LD.C6P_U5, AN()))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">7</span><span class="pk">§7 · Escucha — «Los que llegaron en barco»</span>')
P('<div class="intro"><b>ES:</b> Una visita guiada en el Museo de la Inmigración. <b>Escucha primero, escribe después.</b> <span class="gloss">Een rondleiding in het immigratiemuseum van Buenos Aires. Eerst luisteren, dan schrijven; het transcript staat online en gaat pas open ná de taken.</span></div>')
P(PB.escucha_print(ED.C6P_U5, AN()))
P('</div>')

# ================= CULTURA =================
sec_open("C", "Cultura · figuras del mundo hispano", 'De Spaanstalige wereld gaf grote <b>figuren</b>: uit Argentinië <b>Messi</b>, <b>Maradona</b>, <b>Gardel</b> (tango) en <b>Evita</b>; pan-hispano <b>Frida Kahlo</b> (México) en <b>García Márquez</b> (Colombia, Nobel). <span class="gloss">Beroemde figuren van de hispanofoon.</span>',
        lpd(("5","identiteit in diversiteit"), ("6","literatuur: figuras y obras")))
P('<div class="fams three" style="margin-top:2mm">'
  '<div class="pcard"><div class="t">🎵 Carlos Gardel</div><div class="ej" style="margin-top:2mm">La leyenda del <b>tango</b>. Creció en <b>Buenos Aires</b> y se convirtió en la voz del género. «Gardel cada día canta mejor», se dice. La ciudad de Mateo todavía lo respira. <span class="gloss">Gardel, de stem van de tango.</span></div></div>'
  '<div class="pcard"><div class="t">⚽ Messi y Maradona</div><div class="ej" style="margin-top:2mm">Twee <b>argentijnse</b> voetbalgoden. Maradona maakte in 1986 het «gol del siglo»; Messi werd in 2022 wereldkampioen. Beiden <b>hicieron historia</b>.</div></div>'
  '<div class="pcard"><div class="t">🎨 Frida & García Márquez</div><div class="ej" style="margin-top:2mm"><b>Frida Kahlo</b> (México) pintó autorretratos inolvidables; <b>Gabriel García Márquez</b> (Colombia) ganó el <b>Premio Nobel</b> de literatura con el «realismo mágico». <span class="gloss">Twee namen die je overal tegenkomt.</span></div></div></div>')
P('<div class="route-note" style="margin-top:5mm">🗺️ <b>En la web:</b> haz clic en Argentina (★) en el mapa para descubrir Buenos Aires y sus figuras. <span class="gloss">Online: klik op Argentinië voor de figuras-fiche.</span></div>')
P(actx(AN(), "Une la figura con su logro",
  [{"t":"🌍 Cultura","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Une las dos columnas: escribe la letra. <span class="gloss">Verbind en schrijf de letter.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Figura</div><div class="cb short">1. Gardel &nbsp; 2. Messi &nbsp; 3. Frida Kahlo &nbsp; 4. García Márquez</div></div>'
  '<div class="wcol"><div class="ch">Logro</div><div class="cb short">a. Nobel de Literatura &nbsp; b. leyenda del tango &nbsp; c. autorretratos &nbsp; d. campeón del Mundo 2022</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo="Banco de palabras"))
P(actx(AN(), "El voseo de Mateo · observa",
  [{"t":"🌍 Cultura","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Mateo dice «¿de dónde <b>sos</b>?» y «vos <b>tenés</b> razón». Eso es el <b>voseo</b> (vos en vez de tú). Compara: tú eres → vos sos <span class="gloss">Dat is voseo: vos in plaats van tú.</span> · tú tienes → vos tenés. Schrijf de tú-vorm ernaast.</p>'
  '<p style="margin-left:12.5mm">vos sos → tú <span class="wl sm"></span> · vos tenés → tú <span class="wl sm"></span> · vos hablás → tú <span class="wl sm"></span></p>',
  apoyo="Pista: eres · tienes · hablas"))
sec_close()

retos("cultura_c6p5", "Reto — la misma vida, para alguien de ocho años",
      'Simplificar <b>sin mentir</b> es más difícil que traducir.',
      'Vereenvoudigen zonder te liegen is moeilijker dan vertalen.')

# ================= TAREA FINAL =================
sec_open("★", "Tarea final · «Una biografía»", 'Escribe la <b>biografía</b> de una persona (real o inventada) met de <b>indefinido</b>, conectoren en una <b>mini-mening</b>. <span class="gloss">Schrijf een biografie met de indefinido, connectoren en een mening.</span>')
P(fmu('tus compañeros de clase (el muro de biografías)', 'presentar una vida', 'una biografía (6–8 frases) + una presentación oral (± 1 min)'))
P('<ol class="pasos">'
  '<li><b>Empieza con los datos</b>: «Nació en… en (año). Creció en…».</li>'
  '<li><b>Cuenta 3–4 hechos</b> con el <b>indefinido</b>: «Estudió…, escribió…, ganó…, hizo…».</li>'
  '<li><b>Usa conectores</b>: primero · después · entonces · al final.</li>'
  '<li><b>Añade tu opinión</b>: «Creo que fue… porque…».</li>'
  '<li><b>Preséntalo en pareja</b> y <b>graba</b> tu biografía en la web. Escúchate y mejora.</li></ol>')
P('<div class="se" style="margin-top:4mm">Mi biografía <span class="gloss" style="font-size:8pt">· 6–8 zinnen</span></div><div class="wbox lg"></div>')
P('<div class="se" style="margin-top:3mm">Mi opinión <span class="gloss" style="font-size:8pt">· creo que fue… porque…</span></div><div class="wbox sm"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba tu biografía</b> en la web (recorder + rúbrica). Escucha, compara con el modelo y vuelve a grabar.</div>',
           qr("Escanea y graba", "Tarea · Una biografía", seed=570)))
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Ik gebruik de <b>indefinido</b> correct</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik minstens <b>2 sterke vormen</b> (fue, hizo, tuvo…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>conectoren</b> (primero, después, al final)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik geef <b>één mening</b> (creo que fue… porque…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>presenteer vlot</b> (± 1 min)</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — la biografía de mi compañero/a</div>'
  '<table><thead><tr><th>Un hecho que me sorprendió</th><th>Una pregunta que le hago</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('<div class="truc" style="margin-top:3mm"><b>✍️ Antes de colgar:</b> lees je tekst na — <i>indefinido correct? · 2 fuertes? · conectoren? · una opinión?</i> Verbeter één ding: <span class="wl lg"></span></div>')
sec_close()

# ================= REPASO =================
sec_open("✓", "Repaso · lo esencial", 'Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag; de volledige herhaling staat online.</span>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>Indefinido regular:</b> -ar → é/aste/ó/amos/asteis/aron · -er/-ir → í/iste/ió/imos/isteis/ieron.</li>'
  '<li><b>Fuertes:</b> ser/ir → fue · hacer → hizo · tener → tuvo · estar → estuvo · decir → dijo · venir → vino · dar → dio.</li>'
  '<li><b>Se lo/se la:</b> le/les + lo/la → se lo/se la. «¿El libro? Se lo di».</li>'
  '<li><b>Marcadores:</b> ayer · el año pasado · en 1919 · hace dos años · de repente · entonces.</li>'
  '<li><b>Conectoren:</b> érase una vez · primero · después · entonces · al final · por eso.</li>'
  '<li><b>Las trampas:</b> 🔴 hizo (z) · fue = ser én ir · 🔴 le lo → se lo · 🔴 yo: busqué/llegué/empecé.</li></ul></div>')
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> spelletjes met zelfcorrectie (indefinido, fuertes, se lo, conectoren…).</div>')
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td>over <b>biografieën</b> praten (oficios/logros)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>de <b>indefinido</b> vormen (regelmatig)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>de <b>sterke vormen</b> gebruiken (fue, hizo…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>se lo / se la</b> gebruiken</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>een <b>verhaal vertellen</b> met conectoren</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil para mí: <span class="wl md"></span> · Lo que quiero practicar más: <span class="wl md"></span></i></div>')
P('<div class="se" style="margin-top:6mm">Auto-test rápido · ¿lo sé?</div>')
P('<p style="margin-left:0">1. escribir → él/ella indefinido = <span class="wl sm"></span><br>'
  '2. hacer → él/ella = <span class="wl sm"></span><br>'
  '3. ser/ir → él/ella = <span class="wl sm"></span><br>'
  '4. ¿El libro (a él)? = <span class="wl md"></span> di<br>'
  '5. Geef één biografie-feit (1 zin met el indefinido): <span class="wl lg"></span></p>')
P('<div class="bridge"><b>» Siguiente parada: U6 «Cuando era pequeño».</b> Ya cuentas <b>hechos</b> con el indefinido; en <b>U6</b> aprendes el <b>imperfecto</b> (era, tenía, jugaba) para describir el <b>fondo</b> y las <b>costumbres</b> del pasado — y el <b>contraste</b> entre ambos. ¡Seguimos! <span class="gloss">In U6: de imperfecto voor achtergrond en gewoontes + het contrast met de indefinido.</span></div>')
sec_close()

# ================= §V VOCABULARIO =================
VOC = json.load(open(f"{HERE}/u5_vocab.json", encoding="utf-8"))
GRP = [("biografia","Las etapas de la vida"), ("logros","Los logros"), ("persona","Las personas · oficios"),
       ("indefinido","El indefinido · formas fuertes"), ("tiempo","Marcadores del pasado"),
       ("odoi","Se lo / se la"), ("relato","Contar una historia"), ("opinar","Opinar sobre una figura")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (begrijpen en zelf gebruiken)")))
P('</div>')
P('<p style="font-size:9.6pt">Las palabras de la <b>biografía</b> como red — tres familias:</p>')
P(clusters([
  ("👤","La vida",["nacer · crecer","estudiar · casarse","morir · la vida"],"De levensfasen."),
  ("⏳","El indefinido",["fue · hizo · tuvo","nació · escribió · ganó","ayer · en 1919"],"De verleden vormen."),
  ("📖","Contar",["érase una vez","primero · después","se lo · se la"],"Vertellen & pronomina."),
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
  '<p>Escribe la traducción. <span class="gloss">Schrijf de vertaling.</span> nacer = <span class="wl md"></span> · fue = <span class="wl md"></span> · el escritor = <span class="wl md"></span> · ayer = <span class="wl md"></span></p>', apoyo="Modelo"))
P(actx("V.2", "Distinguir — sorteer per familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Clasifica: <span class="gloss">sorteer deze woorden</span> <span class="words"><b>nacer · fue · el pintor · ganar · hizo · el cantante · morir · tuvo</b></span></p>'
  + sortcols([("etapa/logro (infinitivo)",""),("forma indefinido",""),("persona","")], eigen=False), apoyo="Banco de palabras"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Completa la palabra; tienes la primera letra. <span class="gloss">de beginletter staat erbij</span> geboren worden = <b>n</b>___ · winnen = <b>g</b>___ · was/ging = <b>f</b>___ · gisteren = <b>a</b>___<br><span class="wl full"></span></p>', apoyo="Primera letra"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Escribe una frase correcta con <b>nació · en 1919 · escribió</b>.</p><div class="wbox sm"></div>', apoyo=""))
P(actx("V.5", "Comunicar — una minibiografía en 3 frases",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Escribe tres frases sobre un personaje (nació · hizo · una opinión) y dilas en voz alta. <span class="gloss">Drie zinnen over een figuur.</span></p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>', apoyo="Marco: Nació en… · Estudió/trabajó… · Murió en… / Hoy vive en…"))
P('<div class="se" style="margin-top:6mm">Mi línea de tiempo <span class="gloss" style="font-size:8pt">— teken een tijdlijn en label 5 momenten in het Spaans</span></div>')
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
   a.href=URL.createObjectURL(blob); a.download='C6plus_U5_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Más español en la práctica · C6+ U5 Érase una vez</title><style>'
        + CSS + CSS_OVR + RP.CSS + PB.CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/C6plus_U5.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes ·", _AN[0], "genummerde oefeningen (excl. V.1–V.5)")
