#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de print-HTML C6plus_U2.html (C6+ · Unidad 2 «Aquí vivo») → PDF via Chromium.
# Zelfde componentenkit/CSS als de gelockte golden sample C6+·U0/U1 (geïmporteerd uit gen_u0_print).
# Cursuskleur = paars. Parada 2 = Cartagena (Colombia), gastvrouw Valen.
# Kerngrammatica: hay vs estar + preposiciones · estar + gerundio · OD-pronomina lo/la/los/las.
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
import qr_print as QRP; QRP.fijar("C6+", 2)
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
  <div class="tab">U2 · AQUÍ VIVO</div>
  <div class="eyebrow">UNIDAD 2 · LA RUTA · CARTAGENA 🇨🇴 · AQUÍ VIVO 🏠</div>
  <h1>Aquí vivo</h1>
  <div class="sub">De reis gaat verder naar <b>Cartagena</b>, bij <b>Valen</b>. Je leert je <b>huis</b> en <b>buurt</b> beschrijven: <b>waar</b> alles staat (hay/está + encima/al lado…), <b>wat er nú gebeurt</b> (estoy comiendo) en hoe je een woord kort maakt met <b>lo/la</b>. <span class="gloss">Wonen, de buurt en de weg — met hay/estar + voorzetsels, estar + gerundio en de voornaamwoorden lo/la.</span></div>
  <div class="q">¿Dónde vives tú? <span style="font-weight:400;opacity:.9">· Waar woon jij?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U0 · Reencuentro</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U1 · El día a día</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U2 · Aquí vivo</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U3 · Conectados</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U4 · De viaje</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U5–U7 · el pasado</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 2 · Cartagena 🇨🇴.</b> Cruzamos «el charco» a <b>Colombia</b>. Con <b>Valen</b> descubres su <b>barrio</b>: las casas de colores, los balcones floridos y las plazas de la ciudad amurallada. <span class="gloss">We steken de oceaan over naar Colombia. Bij Valen ontdek je haar buurt in de ommuurde stad Cartagena.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> <b>Valen</b> te invita a su casa en Cartagena. Aprendes a decir <b>qué hay</b> en cada habitación y <b>dónde está</b> cada cosa (la cama está <b>al lado de</b> la ventana). Miras <b>qué está haciendo</b> la familia ahora (mamá <b>está cocinando</b>) y, cuando algo ya se sabe, lo dices más corto: «¿El sofá? <b>Lo</b> pongo aquí». Al final: un <b>mapa de tu barrio</b>.
      <span class="gloss">Valen nodigt je uit in haar huis. Je leert wat er in elke kamer is en waar alles staat, wat de familie nu aan het doen is, en hoe je met lo/la korter praat. Eindtaak: een plattegrond van je buurt.</span></div>
      <div class="ojo"><b>¡Ojo! — twee valstrikken meteen scherp:</b> ① <b>hay</b> = «er is/zijn» (iets nieuws/onbepaald: <i>hay un parque</i>) tegenover <b>está</b> = «staat/ligt» (iets bepaald: <i>el parque está…</i>). ② <b>lo/la</b> vervangt het <b>lijdend voorwerp</b> en komt <b>vóór</b> het werkwoord: <i>Veo la casa → <b>La</b> veo.</i> <span class="gloss">hay = onbepaald · está = bepaald · lo/la vóór het werkwoord.</span></div>
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
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila del barrio</span><br><span class="gloss" style="font-size:8.5pt">Vul je rugzak met de woorden van je huis en buurt: la habitación, encima de, hay, está, ¿cómo llego a…?, lo/la — alles om je plek te beschrijven.</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">describir tu casa</span> (habitaciones y muebles) <span class="nl">je huis beschrijven</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">decir dónde está algo</span> con <b>hay/estar + preposiciones</b> <span class="nl">zeggen waar iets staat</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">decir qué pasa ahora</span> con <b>estar + gerundio</b> <span class="nl">zeggen wat er nu gebeurt</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar los pronombres <b>lo/la/los/las</b></span> (¿el sofá? lo pongo aquí) <span class="nl">lo/la gebruiken</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">preguntar y dar direcciones</span> (¿cómo llego a…?) <span class="nl">de weg vragen/wijzen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">crear tu <b>«Mapa de mi barrio»</b></span> <span class="nl">plattegrond van je buurt (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>La casa</span><span><b>§2</b>Hay/estar</span><span><b>§3</b>Gerundio</span><span><b>§4</b>Lo/la</span><span><b>§5</b>El barrio</span><span><b>§6</b>Lectura</span><span><b>Taller</b>b/v · lugar</span><span><b>Cultura</b>La vivienda</span><span><b>Tarea</b>Mapa de mi barrio</span><span><b>Repaso</b>Semáforo</span>
    </div>
  </div>
  <div class="se" style="margin-top:8mm">Cómo trabajar esta unidad · leeswijzer</div>
  <div class="fams" style="margin-top:2mm">
    <div class="pcard"><div class="t" style="font-size:10.5pt">Las etiquetas de cada actividad</div>
      <div class="ej" style="margin-top:2mm"><span class="badge skill">👂 Escuchar</span> <span class="badge skill">🎙️ Hablar</span> <span class="badge skill">🔍 Analizar</span> <span class="badge">👤 Solo</span> <span class="badge">👥 En parejas</span> <span class="badge">± 5 min</span> <span class="stars">★★☆</span></div>
      <div class="anchor gloss" style="margin-top:2mm">Elke oefening toont de <b>vaardigheid</b>, de <b>werkvorm</b>, de <b>tijd</b> en de <b>moeilijkheid</b>.</div></div>
    <div class="pcard"><div class="t" style="font-size:10.5pt">El apoyo baja poco a poco</div>
      <div class="ej" style="margin-top:2mm"><span class="steun">Modelo</span> → <span class="steun">Banco</span> → <span class="steun">Marco</span> → <span class="steun">Pista</span> → <span class="steun">Sin ayuda</span></div>
      <div class="anchor gloss" style="margin-top:2mm">De <b>steun bouwt af</b>: van model naar zónder hulp. Zo produceer je écht zelf.</div></div>
  </div>
</div>
''')

# ================= §0 · ¡PONTE AL DÍA! =================
sec_open("0", "§0 · ¡Ponte al día!", 'Activamos dos cosas de U1 que necesitas hoy: <b>ser/estar</b> (estar = plaats/toestand → dé basis van hay/estar) y <b>gustar</b> (voor je mening over je barrio). <span class="gloss">We frissen ser/estar en gustar op — die heb je nodig voor «waar staat wat» en je mening over je buurt.</span>',
        lpd(("8","taalsysteem: ser/estar (repaso)"), ("7","woordenschat: gustar")))
P('<div class="truc"><b>Repaso ser/estar (U1):</b> <b>ser</b> = wie/wat iets is (permanent) · <b>estar</b> = <b>waar</b> iets is en <b>hoe</b> het is (plaats/toestand). In U2 bouwt <b>estar</b> = plaats verder uit met <b>hay</b> en de <b>preposiciones</b>.</div>')
P(actx(AN(), "¿ser o estar? (repaso)",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>Kies de juiste vorm van ser of estar.</i></p>'
  '<p style="margin-left:12.5mm">1. Cartagena <span class="wl sm"></span> en Colombia. &nbsp; 2. La casa de Valen <span class="wl sm"></span> grande. &nbsp; 3. La ventana <span class="wl sm"></span> abierta.<br>'
  '4. El barrio <span class="wl sm"></span> tranquilo (eigenschap). &nbsp; 5. Yo <span class="wl sm"></span> en el salón. &nbsp; 6. Hoy Valen <span class="wl sm"></span> contenta.</p>',
  apoyo="Pista"))
P(actx(AN(), "Mi opinión · me gusta mi barrio porque…",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Schrijf 2 zinnen: wat vind je (niet) leuk aan waar je woont, met <b>porque</b>.</p>'
  '<p style="margin-left:12.5mm">Me gusta mi barrio porque <span class="wl lg"></span><br>No me gusta <span class="wl md"></span> porque <span class="wl md"></span></p>',
  apoyo="Marco"))
sec_close()

# ================= §1 · LA CASA =================
sec_open("1", "§1 · La casa — habitaciones y muebles", 'Las <b>habitaciones</b> (dormitorio, cocina, salón…) y los <b>muebles</b> (la cama, el sofá, el armario…). Con estas palabras describes <b>dónde vives</b>. <span class="gloss">De kamers en de meubels — de woorden om je huis te beschrijven.</span>',
        lpd(("7","woordenschat: la casa"), ("8","taalsysteem: género & artículos")))
P('<div class="se">Las habitaciones y los muebles <span class="gloss" style="font-size:8pt">— gelabelde scène</span></div>')
P('<div class="clusters" style="grid-template-columns:1fr 1fr 1fr">'
  '<div class="clu"><div class="ch"><span class="ci">🛏️</span>El dormitorio</div><ul><li>la cama · el armario</li><li>la lámpara · el espejo</li><li>la ventana</li></ul><div class="ex">Duermo en el dormitorio.</div></div>'
  '<div class="clu"><div class="ch"><span class="ci">🛋️</span>El salón</div><ul><li>el sofá · la mesa</li><li>la silla · la tele</li><li>la estantería</li></ul><div class="ex">Veo series en el salón.</div></div>'
  '<div class="clu"><div class="ch"><span class="ci">🍳</span>La cocina</div><ul><li>la nevera · la mesa</li><li>las sillas</li><li>la puerta</li></ul><div class="ex">Cocino en la cocina.</div></div></div>')
P('<table class="alf"><thead><tr><th>Habitación</th><th>Nederlands</th><th>Mueble típico</th></tr></thead><tbody>'
  '<tr><td><b>el dormitorio</b></td><td>de slaapkamer</td><td class="gloss">la cama, el armario</td></tr>'
  '<tr><td><b>el salón</b></td><td>de woonkamer</td><td class="gloss">el sofá, la estantería</td></tr>'
  '<tr><td><b>la cocina</b></td><td>de keuken</td><td class="gloss">la nevera, la mesa</td></tr>'
  '<tr><td><b>el baño</b></td><td>de badkamer</td><td class="gloss">el espejo, la ducha</td></tr>'
  '<tr><td><b>el pasillo / la terraza</b></td><td>de gang / het terras</td><td class="gloss">estrecho / con plantas</td></tr></tbody></table>')
P('<div class="truc"><b>¡Ojo! el/la:</b> <b>el</b> dormitorio, <b>el</b> salón, <b>el</b> baño, <b>el</b> armario, <b>el</b> sofá (m) · <b>la</b> cocina, <b>la</b> cama, <b>la</b> mesa, <b>la</b> silla, <b>la</b> nevera (v). En <b>el sofá</b> is m ondanks -á.</div>')
P(actx(AN(), "Relaciona el mueble con la habitación",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind (schrijf de letter).</p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Mueble</div><div class="cb short">1. la cama &nbsp; 2. el sofá &nbsp; 3. la nevera &nbsp; 4. el espejo</div></div>'
  '<div class="wcol"><div class="ch">Habitación</div><div class="cb short">a. el salón &nbsp; b. el baño &nbsp; c. el dormitorio &nbsp; d. la cocina</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "Clasifica: ¿qué habitación?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Sorteer de meubels in de juiste kamer en vul elke kolom aan met één eigen woord: <span class="words"><b>la cama · el sofá · la nevera · el armario · la estantería · las sillas</b></span></p>'
  + sortcols([("El dormitorio",""),("El salón",""),("La cocina","")], eigen=True), apoyo="Banco de palabras"))
P(actx(AN(), "¿el o la? · el género de los muebles",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★☆☆"}],
  '<p>___ cama · ___ sofá · ___ armario · ___ mesa · ___ nevera · ___ espejo · ___ silla · ___ salón</p>'
  '<p style="margin-left:12.5mm">1.<span class="wl sm"></span> 2.<span class="wl sm"></span> 3.<span class="wl sm"></span> 4.<span class="wl sm"></span> 5.<span class="wl sm"></span> 6.<span class="wl sm"></span> 7.<span class="wl sm"></span> 8.<span class="wl sm"></span></p>',
  apoyo="Pista: -o/-a; el sofá is m!"))
P(actx(AN(), "¿Cómo es tu casa? · escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf 3 zinnen over je huis: welke kamers, welk meubel je favoriet is.</p>'
  '<p style="margin-left:12.5mm">En mi casa hay <span class="wl lg"></span><br>Mi habitación favorita es <span class="wl md"></span> porque <span class="wl md"></span></p>',
  apoyo="Marco"))
sec_close()

retos("casa_c6p", "§1.4 · Retos — la casa dicha de otra manera",
      'Un anuncio que <b>no esconde nada</b> y una habitación descrita <b>sin nombrar un solo mueble</b>.',
      'Een advertentie die niets verbergt, en een kamer beschreven zonder één meubel te noemen.')

# ================= §2 · HAY VS ESTAR + PREPOSICIONES =================
sec_open("2", "§2 · Hay vs estar + preposiciones", 'Voor <b>waar iets staat</b>: <b>hay</b> zegt <b>dát</b> er iets is (onbepaald), <b>estar</b> zegt <b>waar</b> iets bepaalds staat. En de <b>preposiciones</b> (encima de, al lado de…) preciseren de plaats. <span class="gloss">hay = er is (onbepaald) · está = staat (bepaald) · voorzetsels van plaats erbij.</span>',
        lpd(("8","taalsysteem: hay/estar + preposiciones"), ("7","woordenschat: la casa"), ("4","interactie: dónde")))

# §2.1 hay vs estar
P('<h3>§2.1 · ¿hay o está? — el sistema</h3>')
P(obsbox([
  'En el salón <span class="hl">hay</span> un sofá. &nbsp;→&nbsp; El sofá <span class="hl">está</span> delante de la tele.',
  'En mi barrio <span class="hl">hay</span> dos parques. &nbsp;→&nbsp; El parque grande <span class="hl">está</span> cerca.',
], vragen='¿Cuándo usamos <b>hay</b> y cuándo <b>está(n)</b>? Fíjate en el artículo. <span class="gloss">Wanneer hay, wanneer está? Kijk naar het lidwoord.</span>'))
P(regla("Regla · hay ↔ estar", '<p><b>hay</b> (van <i>haber</i>, verandert nooit) → zegt <b>dát</b> er iets is; met <b>un/una/unos/dos/mucho</b> (onbepaald) of een getal: <i>Hay <b>un</b> parque. Hay <b>dos</b> baños.</i><br>'
  '<b>está / están</b> → zegt <b>waar</b> iets <b>bepaalds</b> staat; met <b>el/la/los/las/mi</b>: <i><b>El</b> parque <b>está</b> cerca. <b>Los</b> libros <b>están</b> en la estantería.</i><br>'
  '<span class="gloss">Vuistregel: onbepaald (un/dos/…) → hay · bepaald (el/la/mi) → está(n).</span></p>'))
P(tree([
  '<b>¿Qué quieres decir?</b>',
  '¿bestaat er iets (onbepaald: un, dos, mucho)? → <span class="yes">hay</span> <span class="res">hay un parque</span>',
  '¿waar staat iets bepaalds (el, la, mi)? → <span class="yes">está / están</span> <span class="res">el parque está cerca</span>',
]))
P(actx(AN(), "¿hay o está(n)? · completa",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul <b>hay</b>, <b>está</b> of <b>están</b> in.</p>'
  '<p style="margin-left:12.5mm">1. En mi barrio <span class="wl sm"></span> un supermercado. &nbsp; 2. El supermercado <span class="wl sm"></span> al lado del banco.<br>'
  '3. En el salón <span class="wl sm"></span> dos sofás. &nbsp; 4. Los sofás <span class="wl sm"></span> delante de la tele.<br>'
  '5. ¿<span class="wl sm"></span> una farmacia cerca? &nbsp; 6. La estación <span class="wl sm"></span> lejos.</p>',
  apoyo="Pista: un/dos → hay · el/la → está/están"))
P(actx(AN(), "Clasifica: ¿hay o estar?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Welke zin vraagt <b>hay</b>, welke <b>está(n)</b>? <span class="words"><b>un parque · el parque · dos tiendas · las tiendas · una plaza · mi casa</b></span></p>'
  + sortcols([("hay (onbepaald)",""),("está/están (bepaald)","")], eigen=False), apoyo="Banco de palabras"))
P(actx(AN(), "Transforma · hay → está",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Maak elke tweede zin af met está of están.</p>'
  '<p style="margin-left:12.5mm">1. En el salón hay una mesa. → La mesa <span class="wl md"></span><br>'
  '2. En mi barrio hay dos parques. → Los parques <span class="wl md"></span><br>'
  '3. Cerca hay una farmacia. → La farmacia <span class="wl md"></span></p>',
  apoyo="Primera letra: está / están …"))
P('</div>')

# §2.2 preposiciones
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2.2 · Las preposiciones de lugar</span>')
P('<div class="intro"><b>ES:</b> Para decir <b>exactamente dónde</b>: encima de, debajo de, al lado de, delante de, detrás de, entre… Casi todas llevan <b>de</b> (+ el = <b>del</b>). <span class="gloss">De voorzetsels van plaats — bijna allemaal met «de» (de + el = del).</span></div>')
P('</div>')
P('<div class="fams three" style="margin-top:2mm">'
  '<div class="pcard"><div class="t">Arriba ↕ abajo</div><div class="ej" style="margin-top:1mm"><b>encima de</b> (op/boven) · <b>debajo de</b> (onder)</div></div>'
  '<div class="pcard"><div class="t">Al lado ↔</div><div class="ej" style="margin-top:1mm"><b>al lado de</b> (naast) · <b>entre … y …</b> (tussen)</div></div>'
  '<div class="pcard"><div class="t">Delante ↔ detrás</div><div class="ej" style="margin-top:1mm"><b>delante de</b> (vóór) · <b>detrás de</b> (achter)</div></div>'
  '<div class="pcard"><div class="t">Dentro ↔ fuera</div><div class="ej" style="margin-top:1mm"><b>dentro de</b> (binnen) · <b>fuera de</b> (buiten)</div></div>'
  '<div class="pcard"><div class="t">Cerca ↔ lejos</div><div class="ej" style="margin-top:1mm"><b>cerca de</b> (dichtbij) · <b>lejos de</b> (ver)</div></div>'
  '<div class="pcard"><div class="t">Derecha ↔ izquierda</div><div class="ej" style="margin-top:1mm"><b>a la derecha de</b> · <b>a la izquierda de</b></div></div></div>')
P('<div class="truc"><b>¡Ojo! de + el = del:</b> al lado <b>del</b> banco (niet <span class="trap">de el</span>). Bij <b>la/los/las</b> blijft <b>de</b>: al lado <b>de la</b> plaza.</div>')
P('<div class="se" style="margin-top:4mm">La habitación de Valen · observa</div>')
P('<div class="obsbox"><div class="ln">🛏️ La cama está <span class="hl">al lado de</span> la ventana.</div>'
  '<div class="ln">📚 Los libros están <span class="hl">encima de</span> la estantería.</div>'
  '<div class="ln">🐱 El gato está <span class="hl">debajo de</span> la cama.</div>'
  '<div class="ln">🪑 La silla está <span class="hl">entre</span> la mesa y la pared.</div></div>')
P(actx(AN(), "Completa con la preposición correcta",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul in elke zin de juiste preposición uit het banco in. Bij zin 5 staat de betekenis tussen haakjes. <span class="words"><b>encima de · debajo de · al lado de · delante de · entre</b></span></p>'
  '<p style="margin-left:12.5mm">1. La lámpara está <span class="wl md"></span> la mesa. &nbsp; 2. El perro está <span class="wl md"></span> la cama.<br>'
  '3. El sofá está <span class="wl md"></span> la tele. &nbsp; 4. La farmacia está <span class="wl md"></span> el banco y la tienda.<br>'
  '5. El baño está <span class="wl md"></span> la cocina (naast).</p>',
  apoyo="Banco de palabras"))
P(actx(AN(), "Describe la escena · ¿dónde está?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Beschrijf je eigen kamer: waar staan 4 dingen? Gebruik <b>está/están + preposición</b>.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span>4. <span class="wl full"></span></p>',
  apoyo="Marco"))
P('</div>')

# §2.3 drills + tarea com
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2.3 · Practicar hay/estar + preposiciones</span>')
P('<div class="intro"><b>ES:</b> Ahora entrenamos: primero corregir, luego describir de verdad. <span class="gloss">Eerst verbeteren, dan echt beschrijven.</span></div>')
P('</div>')
P(actx(AN(), "Clínica de errores · hay/estar",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Elke zin heeft één fout (hay/está of preposición). Verbeter.</p>'
  '<p style="margin-left:12.5mm">1. El parque hay cerca de mi casa. → <span class="wl md"></span><br>'
  '2. En el salón está un sofá. → <span class="wl md"></span><br>'
  '3. La lámpara está encima la mesa. → <span class="wl md"></span><br>'
  '4. Al lado de el banco hay una farmacia. → <span class="wl md"></span></p>',
  apoyo="Pista"))
P(actx(AN(), "Sustitución · cambia el mueble",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Modelo: <b>La cama está al lado de la ventana.</b> Herschrijf met een ander meubel/plaats.</p>'
  '<table class="alf"><thead><tr><th>Mueble</th><th>Frase</th></tr></thead><tbody>'
  '<tr><td class="p">el sofá / delante de</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td class="p">los libros / encima de</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td class="p">el gato / debajo de</td><td><span class="wl lg"></span></td></tr></tbody></table>',
  apoyo="Marco"))
P(actx("★", "Tarea comunicativa · el cuarto de mi compañero/a",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>A beschrijft zijn kamer (hay + está + preposiciones), B tekent hem zonder te kijken. Vergelijk daarna. Noteer 2 dingen.</p>'
  '<p style="margin-left:12.5mm">En mi cuarto hay <span class="wl lg"></span> · … está <span class="wl lg"></span></p>',
  apoyo="Marco"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha «La casa de Valen»</b> en la web (TTS). <b>1ª vez:</b> ¿qué habitaciones hay? · <b>2ª vez:</b> ¿dónde está cada mueble? Escribe los datos.</div>',
           qr("Escanea y escucha", "§2 · La casa de Valen", seed=201)))
P('</div>')

retos("hay_estar_c6p", "§2.4 · Retos — metros cuadrados y quinientos euros",
      'Cuánto espacio tiene una persona en Bruselas, en Bogotá y en tu casa. Y una reforma con <b>presupuesto real</b>.',
      'Hoeveel ruimte iemand heeft in Brussel, in Bogotá en bij jou thuis. En een verbouwing met een echt budget.')

# ================= §3 · ESTAR + GERUNDIO =================
sec_open("3", "§3 · Estar + gerundio — ahora mismo", 'Para decir <b>qué pasa en este momento</b>: <b>estar</b> + la forma <b>-ando/-iendo</b>. <i>Valen <b>está cocinando</b>. Yo <b>estoy estudiando</b>.</i> <span class="gloss">Om te zeggen wat er nú aan het gebeuren is: estar + het -ando/-iendo-deelwoord.</span>',
        lpd(("8","taalsysteem: estar + gerundio"), ("7","woordenschat: acciones")))

# §3.1 ¿qué es?
P('<h3>§3.1 · ¿Qué es el gerundio?</h3>')
P('<p style="font-size:9.6pt">De gerundio = de «-ando/-iendo»-vorm (Nederlands «aan het …»). Je maakt hem uit de <b>raíz</b> + de uitgang:</p>')
P(machine([("-ar cocinar","raíz cocin-"),("+ -ando","cocinando")]))
P(machine([("-er/-ir comer","raíz com-"),("+ -iendo","comiendo")]))
P(regla("Regla · estar + gerundio", '<p><b>estar</b> (vervoegd) + <b>gerundio</b>: <i>estoy · estás · está · estamos · estáis · están</i> + <b>-ando</b> (-ar) / <b>-iendo</b> (-er, -ir).<br>'
  '<i>Yo <b>estoy comiendo</b>. Tú <b>estás estudiando</b>. Valen <b>está cocinando</b>.</i><br>'
  '<span class="gloss">Enkel <b>estar</b> verandert met de persoon; de gerundio blijft gelijk.</span></p>'))
P(actx(AN(), "Forma el gerundio",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Vorm het gerundio van de acht werkwoorden. <b>Let op de drie onregelmatige.</b></p>'
  '<p style="margin-left:12.5mm">hablar → <span class="wl sm"></span> &nbsp; estudiar → <span class="wl sm"></span> &nbsp; comer → <span class="wl sm"></span><br>'
  'escribir → <span class="wl sm"></span> &nbsp; cocinar → <span class="wl sm"></span> &nbsp; beber → <span class="wl sm"></span></p>',
  apoyo="Modelo: regla"))
P(actx(AN(), "¿Qué está haciendo?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Kijk naar de cue en schrijf met <b>estar + gerundio</b>.</p>'
  '<p style="margin-left:12.5mm">Valen (cocinar) → <span class="wl md"></span><br>'
  'Yo (estudiar) → <span class="wl md"></span><br>'
  'Los niños (jugar) → <span class="wl md"></span></p>',
  apoyo="Marco: está … / estoy … / están …"))
P(actx(AN(), "¿ahora o en general? · reconoce",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★★☆"}],
  '<p>Gebeurt het <b>nú</b> (estar+gerundio) of <b>in het algemeen</b> (presente)? Vink aan.</p>'
  '<p style="margin-left:12.5mm">☐ Normalmente como a las dos. → <span class="wl sm"></span> (nu/algemeen)<br>'
  '☐ Ahora estoy comiendo. → <span class="wl sm"></span><br>'
  '☐ Valen está cocinando. → <span class="wl sm"></span><br>'
  '☐ Los sábados juego al fútbol. → <span class="wl sm"></span></p>',
  apoyo="Pista: estar+gerundio = nu"))
P('</div>')

# §3.2 irregulares + cloze
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3.2 · Gerundios irregulares + la gran cloze</span>')
P('<div class="intro"><b>ES:</b> Algunos gerundios cambian: <b>leer → leyendo</b>, <b>dormir → durmiendo</b>, <b>pedir → pidiendo</b>. La <b>i</b> entre vocales se hace <b>y</b>; e→i / o→u en algunos. <span class="gloss">Enkele onregelmatige gerundios: leyendo, durmiendo, pidiendo.</span></div>')
P('</div>')
P('<table class="conj"><thead><tr><th>Infinitivo</th><th>Gerundio</th><th>Waarom</th></tr></thead><tbody>'
  '<tr><td>leer</td><td class="v">le<span class="end">yendo</span></td><td class="gloss">i → y (tussen klinkers)</td></tr>'
  '<tr><td>oír</td><td class="v">o<span class="end">yendo</span></td><td class="gloss">i → y</td></tr>'
  '<tr><td>dormir</td><td class="v">d<span class="end">u</span>rmiendo</td><td class="gloss">o → u</td></tr>'
  '<tr><td>pedir</td><td class="v">p<span class="end">i</span>diendo</td><td class="gloss">e → i</td></tr>'
  '<tr><td>decir</td><td class="v">d<span class="end">i</span>ciendo</td><td class="gloss">e → i</td></tr></tbody></table>')
P(actx(AN(), "La gran cloze · estar + gerundio",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Vul <b>estar + gerundio</b> in (infinitivo tussen haakjes).</p>'
  '<p style="margin-left:12.5mm">1. Valen <span class="wl md"></span> (cocinar) en la cocina. &nbsp; 2. Yo <span class="wl md"></span> (estudiar) para el examen.<br>'
  '3. Los niños <span class="wl md"></span> (dormir) ahora. &nbsp; 4. ¿Tú <span class="wl md"></span> (leer) un libro?<br>'
  '5. Nosotros <span class="wl md"></span> (comer) en la terraza. &nbsp; 6. Mamá <span class="wl md"></span> (escribir) un mensaje.<br>'
  '7. Diego <span class="wl md"></span> (pedir) una pizza. &nbsp; 8. Yo <span class="wl md"></span> (ver) la tele.</p>',
  apoyo="Banco de palabras: está cocinando · estoy estudiando · están durmiendo · estás leyendo · estamos comiendo · está escribiendo · está pidiendo · estoy viendo"))
P(actx(AN(), "Sustitución · cambia la persona",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Modelo: <b>Yo estoy comiendo.</b> Herschrijf per persoon.</p>'
  '<p style="margin-left:12.5mm">tú → <span class="wl md"></span> &nbsp; ella → <span class="wl md"></span> &nbsp; nosotros → <span class="wl md"></span> &nbsp; ellos → <span class="wl md"></span></p>',
  apoyo="Primera letra: estás…"))
P('</div>')

# §3.3 ¿qué están haciendo? + tarea
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3.3 · ¿Qué están haciendo en casa?</span>')
P('<div class="intro"><b>ES:</b> Aplicamos: describe qué hace cada persona ahora mismo. <span class="gloss">We passen toe: wat doet iedereen nu?</span></div>')
P('</div>')
P(actx(AN(), "La familia de Valen · ¿qué están haciendo?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf een zin per persoon met <b>estar + gerundio</b>.</p>'
  '<table class="alf"><thead><tr><th>Persona · lugar</th><th>Frase (estar + gerundio)</th></tr></thead><tbody>'
  '<tr><td>mamá · la cocina (cocinar)</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>Valen · el salón (ver la tele)</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>el hermano · el dormitorio (dormir)</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>tú · ¿? </td><td><span class="wl lg"></span></td></tr></tbody></table>',
  apoyo="Marco"))
P(actx(AN(), "Dictado · ¿qué está pasando?",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Luister en schrijf de 5 zinnen (met estar + gerundio).</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span>4. <span class="wl full"></span>5. <span class="wl full"></span></p>',
  apoyo="docent leest voor"))
P(actx("★", "Tarea comunicativa · llamada de vídeo",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Je belt (video) met je buur. Vraag: «¿Qué estás haciendo?» en antwoord met <b>estar + gerundio</b>. Noteer 2 antwoorden.</p>'
  '<p style="margin-left:12.5mm">— ¿Qué estás haciendo? — <span class="wl lg"></span></p>',
  apoyo="Marco"))
P('<div class="guide"><div class="ic">🎡</div><div><span class="hand">Online:</span> <span class="g">de <b>werkwoordmachine</b> en het <b>gerundio-spel</b> op de hub oefenen elke -ando/-iendo-vorm; + cloze en foutenkliniek.</span></div></div>')
P('</div>')

retos("gerundio_c6p", "§3.4 · Retos — ¿qué está pasando ahí?",
      'Un portátil desaparecido con cuatro coartadas, y una videollamada donde ves la habitación pero <b>no a la persona</b>.',
      "Een verdwenen laptop met vier alibi's, en een videogesprek waarin je de kamer ziet maar de persoon niet.")

# ================= §4 · OD-PRONOMINA lo/la/los/las =================
sec_open("4", "§4 · Los pronombres lo/la/los/las", 'Om niet steeds hetzelfde te herhalen, vervang je het <b>lijdend voorwerp</b> door <b>lo/la/los/las</b>. <i>¿Ves la casa? Sí, <b>la</b> veo.</i> <span class="gloss">Het lijdend voorwerp korter maken met lo/la/los/las — het staat vóór het werkwoord.</span>',
        lpd(("8","taalsysteem: OD-pronomina lo/la"), ("7","woordenschat: la casa")))

# §4.1 ¿qué es?
P('<h3>§4.1 · ¿Qué es un pronombre de OD?</h3>')
P('<p style="font-size:9.6pt">Het <b>lijdend voorwerp</b> (OD) = het ding dat de actie ondergaat. Je vervangt het door <b>lo/la/los/las</b> zodat je het niet herhaalt:</p>')
P('<div class="agree"><div class="w">Veo <u>la casa</u> → <u>La</u> veo.</div><div class="tie">la casa (v ev) → la</div></div>')
P('<div class="agree"><div class="w">Compro <u>los muebles</u> → <u>Los</u> compro.</div><div class="tie">los muebles (m mv) → los</div></div>')
P(regla("Regla · lo/la/los/las (OD)", '<table class="conj" style="margin-top:1mm"><thead><tr><th>Vervangt</th><th>Pronombre</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="p">m. ev. (el libro)</td><td class="v">lo</td><td>¿El libro? <b>Lo</b> leo.</td></tr>'
  '<tr><td class="p">v. ev. (la casa)</td><td class="v">la</td><td>¿La casa? <b>La</b> veo.</td></tr>'
  '<tr><td class="p">m. mv. (los muebles)</td><td class="v">los</td><td>¿Los muebles? <b>Los</b> compro.</td></tr>'
  '<tr><td class="p">v. mv. (las sillas)</td><td class="v">las</td><td>¿Las sillas? <b>Las</b> pongo aquí.</td></tr></tbody></table>'
  '<p style="margin:2mm 0 0">Het pronomen <b>komt overeen</b> met het woord dat het vervangt (m/v · ev/mv) en staat <b>vóór</b> het vervoegde werkwoord.</p>'))
P(blocks([[("per","¿La casa?"),("opt","→"),("ob","La"),("vb","veo")], [("per","¿Los libros?"),("opt","→"),("ob","Los"),("vb","leo")]]))
P(actx(AN(), "¿lo, la, los o las?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Kies per zin het juiste voornaamwoord. Kijk eerst naar het woord dat je vervangt: mannelijk of vrouwelijk, enkelvoud of meervoud.</p>'
  '<p style="margin-left:12.5mm">1. ¿El sofá? <span class="wl sm"></span> pongo en el salón. &nbsp; 2. ¿La cama? <span class="wl sm"></span> pongo aquí.<br>'
  '3. ¿Los platos? <span class="wl sm"></span> lavo. &nbsp; 4. ¿Las sillas? <span class="wl sm"></span> pongo en la cocina.<br>'
  '5. ¿La tele? <span class="wl sm"></span> veo por la noche. &nbsp; 6. ¿El coche? <span class="wl sm"></span> aparco en el garaje.</p>',
  apoyo="Modelo: tabla"))
P(actx(AN(), "Transforma la frase · usa lo/la/los/las",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Vervang het onderstreepte voorwerp door lo/la/los/las, vóór het werkwoord.</p>'
  '<p style="margin-left:12.5mm">1. Veo <u>la plaza</u>. → <span class="wl md"></span><br>'
  '2. Compro <u>los muebles</u>. → <span class="wl md"></span><br>'
  '3. Pongo <u>el espejo</u> aquí. → <span class="wl md"></span><br>'
  '4. Limpio <u>las ventanas</u>. → <span class="wl md"></span></p>',
  apoyo="Primera letra: La veo…"))
P('</div>')

# §4.2 concordancia + drills
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4.2 · La concordancia — practicar</span>')
P('<div class="intro"><b>ES:</b> El pronombre concuerda con el objeto (m/v · ev/mv). Entrenamos la elección correcta. <span class="gloss">Het pronomen komt overeen met het voorwerp — we oefenen de juiste keuze.</span></div>')
P('</div>')
P(actx(AN(), "Responde con el pronombre (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Antwoord met <b>lo/la/los/las</b> + het werkwoord.</p>'
  '<p style="margin-left:12.5mm">1. ¿Compras el sofá? — Sí, <span class="wl md"></span> compro. &nbsp; 2. ¿Ves la plaza? — Sí, <span class="wl md"></span> veo.<br>'
  '3. ¿Pones los libros aquí? — Sí, <span class="wl md"></span> pongo aquí. &nbsp; 4. ¿Limpias las ventanas? — Sí, <span class="wl md"></span> limpio.<br>'
  '5. ¿Coges el autobús? — Sí, <span class="wl md"></span> cojo.</p>',
  apoyo="Banco de palabras: lo · la · los · las · lo"))
P(actx(AN(), "Empareja: pregunta ↔ respuesta",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Verbind de vraag met het juiste antwoord (schrijf de letter).</p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Pregunta</div><div class="cb short">1. ¿Ves la tele? &nbsp; 2. ¿Compras los muebles? &nbsp; 3. ¿Pones el espejo? &nbsp; 4. ¿Lavas las sillas?</div></div>'
  '<div class="wcol"><div class="ch">Respuesta</div><div class="cb short">a. Sí, los compro. &nbsp; b. Sí, la veo. &nbsp; c. Sí, las lavo. &nbsp; d. Sí, lo pongo.</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
P('</div>')

# §4.3 posición + foutenkliniek + tarea
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4.3 · La posición del pronombre</span>')
P('<div class="intro"><b>ES:</b> Normaal <b>vóór</b> het vervoegde werkwoord: <i>Lo veo</i>. Bij een <b>infinitivo</b> of <b>gerundio</b> mag het ook <b>achteraan vast</b>: <i>Voy a comprar<b>lo</b> = <b>Lo</b> voy a comprar · Estoy leyéndo<b>lo</b> = <b>Lo</b> estoy leyendo</i>. <span class="gloss">Vóór het vervoegde werkwoord, óf vastgeplakt aan de infinitief/gerundio.</span></div>')
P('</div>')
P('<div class="agree"><div class="w"><u>Lo</u> veo.</div><div class="tie">vóór het vervoegde werkwoord</div></div>')
P('<div class="agree"><div class="w">Voy a comprar<u>lo</u> = <u>Lo</u> voy a comprar.</div><div class="tie">bij infinitief: achteraan óf vooraan</div></div>')
P(actx(AN(), "Reescribe con el pronombre (posición)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Herschrijf elke zin met lo/la/los/las. Kies zelf een correcte plaats voor het pronomen.</p>'
  '<p style="margin-left:12.5mm">1. Compro el sofá. → <span class="wl md"></span><br>'
  '2. Voy a limpiar la cocina. → <span class="wl lg"></span><br>'
  '3. Estoy leyendo el libro. → <span class="wl lg"></span><br>'
  '4. Pongo las sillas aquí. → <span class="wl md"></span></p>',
  apoyo="Pista: Lo compro · Voy a limpiarla / La voy a limpiar…"))
P(actx(AN(), "Clínica de errores · lo/la",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Elke zin heeft één fout (keuze of plaats). Verbeter.</p>'
  '<p style="margin-left:12.5mm">1. ¿La casa? Veo la. → <span class="wl md"></span><br>'
  '2. ¿Los muebles? Las compro. → <span class="wl md"></span><br>'
  '3. ¿El sofá? La pongo aquí. → <span class="wl md"></span><br>'
  '4. Voy a lo comprar. → <span class="wl md"></span></p>',
  apoyo="Pista: concordancia + plaats"))
P(actx("★", "Tarea comunicativa · ¿lo tienes?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Vraag je buur of hij dingen heeft/doet; antwoord kort met lo/la/los/las. «¿Tienes el libro? — Sí, lo tengo.» Noteer 3 antwoorden.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>',
  apoyo="Marco"))
P('</div>')

retos("pronombres_c6p2", "§4.4 · Reto — diez cosas, ni una más",
      'Os mudáis a treinta metros cuadrados. A partir de la segunda vez, la cosa ya <b>no tiene nombre</b>.',
      'Jullie verhuizen naar dertig vierkante meter. Vanaf de tweede keer heeft het ding geen naam meer.')

# ================= §5 · EL BARRIO Y CÓMO LLEGAR =================
sec_open("5", "§5 · El barrio y cómo llegar", 'Los <b>lugares</b> del barrio (la plaza, la farmacia, la parada…) y cómo <b>dar direcciones</b>: sigue recto, gira a la derecha, cruza la calle. <span class="gloss">De plekken in de buurt en hoe je de weg wijst.</span>',
        lpd(("7","woordenschat: el barrio"), ("4","mondelinge interactie: de weg"), ("9","strategieën")))
P('<div class="se">Los lugares del barrio</div>')
P('<div class="clusters" style="grid-template-columns:1fr 1fr 1fr">'
  '<div class="clu"><div class="ch"><span class="ci">🛒</span>Comprar</div><ul><li>la tienda</li><li>el supermercado</li><li>la farmacia</li></ul></div>'
  '<div class="clu"><div class="ch"><span class="ci">🌳</span>Espacio público</div><ul><li>la plaza</li><li>el parque</li><li>la calle</li></ul></div>'
  '<div class="clu"><div class="ch"><span class="ci">🚌</span>Servicios</div><ul><li>el banco</li><li>la parada</li><li>la estación</li></ul></div></div>')
P('<div class="se" style="margin-top:4mm">Cómo llegar · las direcciones</div>')
P('<div class="fams three" style="margin-top:1mm">'
  '<div class="pcard"><div class="t">Sigue recto</div><div class="ej">ga rechtdoor</div></div>'
  '<div class="pcard"><div class="t">Gira a la derecha / izquierda</div><div class="ej">sla rechts / links af</div></div>'
  '<div class="pcard"><div class="t">Cruza la calle</div><div class="ej">steek over · en la esquina / el semáforo</div></div></div>')
P('<div class="truc"><b>¡Ojo!</b> <b>¿Cómo llego a…?</b> = hoe geraak ik bij…? Antwoord met de <b>tú-imperativo</b> (sigue, gira, cruza) of met <b>tienes que</b> + infinitivo (tienes que seguir recto). Afstand: <b>está a cinco minutos</b> (a pie / en bus).</div>')
P(actx(AN(), "Relaciona el lugar con su función",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind (schrijf de letter).</p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Lugar</div><div class="cb short">1. la farmacia &nbsp; 2. la parada &nbsp; 3. el supermercado &nbsp; 4. el parque</div></div>'
  '<div class="wcol"><div class="ch">Función</div><div class="cb short">a. coger el autobús &nbsp; b. comprar comida &nbsp; c. pasear &nbsp; d. comprar medicinas</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "Completa las direcciones",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul aan met <b>sigue · gira · cruza · está</b>.</p>'
  '<p style="margin-left:12.5mm">Para ir a la plaza: <span class="wl sm"></span> recto hasta el semáforo, luego <span class="wl sm"></span> a la derecha y <span class="wl sm"></span> la calle. La plaza <span class="wl sm"></span> a la izquierda, a dos minutos.</p>',
  apoyo="Banco de palabras"))
P(actx(AN(), "Sustitución · da la ruta a otro lugar",
  [{"t":"🔁 Practicar","skill":True},{"t":"👥 En parejas"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Modelo: «Para ir a la plaza, sigue recto y gira a la derecha.» Herschrijf voor een ander doel/andere richting.</p>'
  '<p style="margin-left:12.5mm">→ a la farmacia: <span class="wl full"></span>→ al parque: <span class="wl full"></span></p>',
  apoyo="Marco"))
P(actx(AN(), "Dictado · el camino",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Luister en schrijf de route in vier stappen.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span>4. <span class="wl full"></span></p>',
  apoyo="docent/audio"))
P(actx("★", "Info-gap · ¿cómo llego a…?",
  [{"t":"🗣️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>A vraagt de weg naar 2 plekken; B geeft die met sigue/gira/cruza + afstand. Wissel daarna. Noteer één route.</p>'
  '<p style="margin-left:12.5mm">— ¿Cómo llego a <span class="wl sm"></span>? — <span class="wl full"></span></p>',
  apoyo="Marco"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha «¿Cómo llego a la plaza?»</b> en la web (TTS) y sigue la ruta en el plano. <b>1ª vez:</b> ¿adónde va? · <b>2ª vez:</b> anota las direcciones.</div>',
           qr("Escanea y escucha", "§5 · ¿Cómo llego?", seed=202)))
sec_close()

retos("barrio_c6p", "§5.4 · Retos — el edificio y el barrio",
      'Seis ruidos en cinco plantas, y un recorrido por tu casa de <b>cuarenta segundos exactos</b>.',
      'Zes geluiden op vijf verdiepingen, en een rondgang door je huis van precies veertig seconden.')

# ================= §6 · LECTURA =================
sec_open("6", "§6 · Lectura — «Mi barrio en Cartagena»", 'Valen describe su barrio. Lee, busca información y reacciona. <span class="gloss">Valen beschrijft haar buurt. Lezen, informatie zoeken, reageren.</span>',
        lpd(("1","lezen: hoofdgedachte"), ("2","lezen: info selecteren"), ("5","identiteit & cultuur")))
P('<div class="lecdoel"><b>Antes de leer:</b> mira el título. ¿Qué esperas (lugares, dónde están)? <span class="gloss">Kijk naar de titel: wat verwacht je?</span></div>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> blog / descripción</span><span class="tm"><b>Fuente:</b> muro de clase</span><span class="tm"><b>Objetivo:</b> conocer su barrio</span></div>')
P(f'<div class="ptexts">'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["valen"]}</div><div><div class="nm">Valen</div><div class="fr">Cartagena 🇨🇴</div></div></div>'
  f'<p>¡Hola! Vivo en un <span class="evi">barrio</span> del centro histórico de Cartagena, cerca del mar. Mi casa es antigua, con un <span class="evi">balcón</span> lleno de flores. Delante de mi casa <span class="evi">hay</span> una plaza pequeña con árboles. Al lado <span class="evi">está</span> la panadería; por la mañana huele a pan. La farmacia está a la derecha y la parada del bus, a dos minutos. Mi barrio es <span class="evi">tranquilo</span> por el día y alegre por la noche, con música.</p></div>'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["diego"]}</div><div><div class="nm">Diego</div><div class="fr">CDMX 🇲🇽</div></div></div>'
  f'<p>Yo vivo en un barrio grande de Ciudad de México. Es <span class="evi">ruidoso</span> pero me gusta: hay de todo. Detrás de mi edificio hay un mercado enorme. El metro está muy cerca y lo cojo cada día. No hay mucho silencio, pero <span class="evi">hay</span> vida en la calle a todas horas.</p></div></div>')
P(actx(AN(), "Verdadero o falso — con prueba",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf V of F en kopieer in de derde kolom de zin uit de tekst die het bewijst.</p>'
  '<table class="alf"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba (cita)</th></tr></thead><tbody>'
  '<tr><td>Delante de la casa de Valen hay una plaza.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>El barrio de Valen es ruidoso todo el día.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Diego coge el metro cada día.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>',
  apoyo="Modelo"))
P(actx(AN(), "Escanea — completa la ficha",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Zoek de gegevens per persoon terug in de tekst en vul de tabel aan. Eén woord of getal per vak.</p>'
  '<table class="alf"><thead><tr><th>—</th><th>Valen</th><th>Diego</th></tr></thead><tbody>'
  '<tr><td>¿Cómo es el barrio?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>¿Qué hay cerca?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>¿Qué transporte usa?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>',
  apoyo=""))
P(actx(AN(), "Reacciona — ¿y tu barrio?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>¿Tu barrio se parece más al de Valen o al de Diego? Schrijf 2–3 zinnen met <b>hay/está + porque</b>.</p>'
  '<div class="wbox sm"></div>',
  apoyo="Marco: Mi barrio se parece al de … porque …"))
sec_close()

# ================= TALLER =================
sec_open("T", "Taller de lengua", 'Dos herramientas: la <b>b/v</b> (klinkt gelijk!) in huis-/plaatswoorden en de <b>adverbios de lugar</b> (aquí, ahí, allí). <span class="gloss">De b/v en de plaatsbijwoorden.</span>')
P('<h3>1 · Ortografía — b of v</h3>')
P(regla("b y v suenan igual", '<p>In het Spaans klinken <b>b</b> en <b>v</b> <b>hetzelfde</b> (≈ NL «b»). Je moet de spelling <b>uit het hoofd</b> leren: <b>v</b>ivir, la <b>v</b>entana, el <b>b</b>arrio, el <b>b</b>alcón, el ar<b>m</b>ario.<br><span class="gloss">Tip: schrijf twijfelwoorden een paar keer op.</span></p>'))
P(actx(AN(), "¿b o v? · completa",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Vul <b>b</b> of <b>v</b> in.</p>'
  '<p style="margin-left:12.5mm">la _entana · _ivir · el _arrio · el _alcón · el _año · la _i_lioteca · el _ar</p>',
  apoyo="Pista: ventana, vivir, barrio, balcón, baño, biblioteca, bar"))
P('<h3 style="margin-top:6mm">2 · Adverbios de lugar — aquí · ahí · allí</h3>')
P(colloc("aquí · ahí · allí", ["aquí = hier (dichtbij)","ahí = daar (bij jou)","allí/allá = daar (ver)","cerca ↔ lejos"]))
P(actx(AN(), "Completa con aquí / ahí / allí",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Vul <b>aquí</b>, <b>ahí</b> of <b>allí</b> in. De afstand staat tussen haakjes achter de zin.</p>'
  '<p style="margin-left:12.5mm">1. La cama está <span class="wl sm"></span>, a mi lado (hier). &nbsp; 2. El parque está <span class="wl sm"></span>, muy lejos (daar-ver).<br>'
  '3. Pon la silla <span class="wl sm"></span>, cerca de ti (daar-bij jou).</p>',
  apoyo="Banco de palabras"))
sec_close()

# ================= §7 LECTURA · §8 ESCUCHA =================
# Zelfde bron als de digitale hub (lectura_data / escucha_data): papier en scherm
# kunnen zo niet uit elkaar lopen. Elk op een eigen bladzijde (§14).
P('<div class="page"><div class="parada sec">')
P('<span class="num">7</span><span class="pk">§7 · Lectura — «Casa Azul»: dos reseñas</span>')
P('<div class="intro"><b>ES:</b> Dos opiniones sobre la misma casa. <b>No hace falta entenderlo todo</b> para sacar la información. <span class="gloss">Twee meningen over hetzelfde huis. Je hoeft niet alles te begrijpen — zoek gericht, en let op waar ze het oneens zijn.</span></div>')
P(PB.lectura_print(LD.C6P_U2, AN()))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">8</span><span class="pk">§8 · Escucha — «Estoy perdido en Cartagena»</span>')
P('<div class="intro"><b>ES:</b> Sam llama a Valen: no encuentra su calle. <b>Escucha primero, escribe después.</b> <span class="gloss">Sam belt Valen op: hij vindt haar straat niet. Eerst luisteren, dan schrijven; het transcript staat online en gaat pas open ná de taken.</span></div>')
P(PB.escucha_print(ED.C6P_U2, AN()))
P('</div>')

# ================= CULTURA =================
sec_open("C", "Cultura · la vivienda hispana", 'La <b>casa</b> hispana tiene su propio estilo: <b>patios</b> con plantas, <b>balcones</b> floridos y <b>plazas</b> como corazón del barrio. Cada país tiene el suyo. <span class="gloss">Het Spaanstalige huis: patio\'s, balkons met bloemen en het plein als hart van de buurt.</span>',
        lpd(("5","identiteit in diversiteit: la vivienda hispana")))
P('<div class="fams three" style="margin-top:2mm">'
  '<div class="pcard"><div class="t">🏛️ El patio andaluz</div><div class="ej" style="margin-top:2mm">In het zuiden van <b>España</b> (Sevilla, Córdoba) heeft het huis een <b>patio</b>: een binnentuin met planten en een fontein, koel in de zomer. <b>Lucía</b> kent ze goed.</div></div>'
  '<div class="pcard"><div class="t">🌺 Los balcones de Cartagena</div><div class="ej" style="margin-top:2mm">In <b>Cartagena</b> (Colombia) zijn de koloniale huizen <b>kleurrijk</b>, met houten <b>balcones</b> vol bloemen. De <b>ciudad amurallada</b> is UNESCO-werelderfgoed.</div></div>'
  '<div class="pcard"><div class="t">🟨 La plaza, corazón del barrio</div><div class="ej" style="margin-top:2mm">Overal in de Spaanstalige wereld is de <b>plaza</b> het middelpunt: markt, terrasjes, ontmoeting. «Quedamos en la plaza».</div></div></div>')
P('<div class="route-note" style="margin-top:5mm">🗺️ <b>En la web:</b> haz clic en Colombia (★) en el mapa para descubrir Cartagena y su barrio. <span class="gloss">Online: klik op Colombia voor Cartagena.</span></div>')
P(actx(AN(), "Compara · tu casa y una casa hispana",
  [{"t":"🌍 Cultura","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Wat is anders tussen jouw woning en een huis met patio of balcón? Schrijf 2 zinnen met <b>hay</b> en <b>está</b>.</p>'
  '<div class="wbox sm"></div>',
  apoyo="Marco"))
P(actx(AN(), "Datos curiosos — une",
  [{"t":"🌍 Cultura","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Verbind (schrijf de letter).</p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Lugar</div><div class="cb short">1. el patio andaluz &nbsp; 2. Cartagena &nbsp; 3. la plaza &nbsp; 4. el balcón</div></div>'
  '<div class="wcol"><div class="ch">Dato</div><div class="cb short">a. corazón del barrio (mercado, terrazas) &nbsp; b. binnentuin koel in de zomer &nbsp; c. ciudad amurallada, UNESCO &nbsp; d. vol bloemen, kleurrijk</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo="Banco de palabras"))
sec_close()

retos("cultura_c6p2", "Reto — dos maneras de construir una casa",
      'Por qué las casas flamencas son estrechas y las cartageneras tienen patio. Explícaselo a Valen.',
      'Waarom Vlaamse huizen smal zijn en die in Cartagena een patio hebben. Leg het uit aan Valen.')

# ================= TAREA FINAL =================
sec_open("★", "Tarea final · «Mapa de mi barrio»", 'Dibuja el <b>mapa de tu barrio</b> y haz una <b>ruta guiada</b>: di qué hay, dónde está y cómo llegar. <span class="gloss">Teken de plattegrond van je buurt en geef een rondleiding.</span>')
P(fmu('tus compañeros de clase (el muro)', 'presentar tu barrio y una ruta', 'un mapa/plano + una presentación oral (± 1 min)'))
P('<ol class="pasos">'
  '<li><b>Dibuja el plano</b> de tu barrio (o tu calle): pon 5–6 lugares (tienda, parque, parada…).</li>'
  '<li><b>Escribe qué hay y dónde está</b> (4–6 frases): «En mi barrio <b>hay</b>… · La tienda <b>está al lado de</b>…».</li>'
  '<li><b>Añade una ruta</b>: «Para ir de mi casa a la plaza: <b>sigue recto</b>, <b>gira</b>… (está a … minutos)».</li>'
  '<li><b>Añade tu opinión</b>: «Me gusta mi barrio <b>porque</b>…».</li>'
  '<li><b>Preséntalo en pareja</b> y <b>graba</b> tu ruta en la web. Escúchate y mejora.</li></ol>')
P('<div class="se" style="margin-top:4mm">Mi plano <span class="gloss" style="font-size:8pt">· tekenvlak</span></div><div class="wbox lg"></div>')
P('<div class="se" style="margin-top:3mm">Mi descripción y mi ruta <span class="gloss" style="font-size:8pt">· 4–6 zinnen</span></div><div class="wbox"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba tu ruta guiada</b> en la web (recorder + rúbrica). Escucha, compara con el modelo y vuelve a grabar.</div>',
           qr("Escanea y graba", "Tarea · Mapa de mi barrio", seed=270)))
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Ik gebruik <b>hay</b> én <b>está(n)</b> correct</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik minstens <b>4 preposiciones de lugar</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik geef een <b>ruta</b> (sigue/gira/cruza + afstand)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik geef <b>één mening</b> met «me gusta… porque…»</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>presenteer vlot</b> (± 1 min)</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — el barrio de mi compañero/a</div>'
  '<table><thead><tr><th>Un lugar que también hay en mi barrio</th><th>Una pregunta que le hago</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('<div class="truc" style="margin-top:3mm"><b>✍️ Antes de colgar:</b> lees je tekst na — <i>hay/está correct? · preposiciones met del/de la? · una ruta? · una opinión?</i> Verbeter één ding: <span class="wl lg"></span></div>')
sec_close()

# ================= REPASO =================
sec_open("✓", "Repaso · lo esencial", 'Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag; de volledige herhaling staat online.</span>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>Hay vs estar:</b> hay + un/una/dos (onbepaald: <i>hay un parque</i>) · está(n) + el/la/mi (bepaald: <i>el parque está cerca</i>).</li>'
  '<li><b>Preposiciones:</b> encima de · debajo de · al lado de · delante de · detrás de · entre · cerca/lejos de. (de + el = <b>del</b>).</li>'
  '<li><b>Estar + gerundio:</b> estoy/estás/está… + -ando (-ar) / -iendo (-er, -ir). Irreg.: leyendo, durmiendo, pidiendo.</li>'
  '<li><b>Lo/la/los/las (OD):</b> vervangt het voorwerp, komt overeen (m/v·ev/mv), staat vóór het ww. of achter inf./gerundio.</li>'
  '<li><b>Direcciones:</b> ¿cómo llego a…? · sigue recto · gira a la derecha/izquierda · cruza · está a … minutos.</li>'
  '<li><b>Las trampas:</b> 🔴 hay ≠ está · 🔴 de + el = del · 🔴 lo/la vóór het ww. · 🔴 concordancia lo/la/los/las.</li></ul></div>')
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> spelletjes met zelfcorrectie (hay/está, preposiciones, gerundio, lo/la, direcciones…).</div>')
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td>mijn <b>huis</b> beschrijven (habitaciones/muebles)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>hay</b> en <b>estar + preposiciones</b> gebruiken</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>estar + gerundio</b> vormen (qué está pasando)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>de pronombres <b>lo/la/los/las</b> gebruiken</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>de <b>weg vragen en wijzen</b></td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil para mí: <span class="wl md"></span> · Lo que quiero practicar más: <span class="wl md"></span></i></div>')
P('<div class="se" style="margin-top:6mm">Auto-test rápido · ¿lo sé?</div>')
P('<p style="margin-left:0">1. hay of está: «En el salón ___ un sofá» = <span class="wl sm"></span><br>'
  '2. de + el = <span class="wl sm"></span><br>'
  '3. comer → gerundio = <span class="wl md"></span><br>'
  '4. ¿La casa? ___ veo = <span class="wl sm"></span><br>'
  '5. Geef de weg (1 zin): <span class="wl lg"></span></p>')
P('<div class="bridge"><b>» Siguiente parada: U3 «Conectados».</b> Ya describes tu barrio; en <b>U3</b> hablas de <b>media y planes</b> con <b>ir a + infinitivo</b> (futuro próximo) y los pronombres <b>le/les</b>. ¡Seguimos! <span class="gloss">In U3: media, technologie en plannen — met ir a + infinitivo.</span></div>')
sec_close()

# ================= §V VOCABULARIO =================
VOC = json.load(open(f"{HERE}/u2_vocab.json", encoding="utf-8"))
GRP = [("habitaciones","Las habitaciones"), ("muebles","Los muebles"), ("casa","La vivienda"),
       ("preposiciones","Hay/estar + preposiciones de lugar"), ("barrio","El barrio · lugares"),
       ("ciudad","La ciudad · adjetivos"), ("direcciones","Cómo llegar · direcciones"),
       ("movimiento","Verbos de movimiento")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (begrijpen en zelf gebruiken)")))
P('</div>')
P('<p style="font-size:9.6pt">Las palabras de <b>tu casa y tu barrio</b> como red — tres familias:</p>')
P(clusters([
  ("🏠","La casa",["la habitación · la cama","el salón · la cocina","el armario · la mesa"],"Waar je woont."),
  ("📍","¿Dónde está?",["encima de · debajo de","al lado de · entre","cerca / lejos de"],"Waar iets staat."),
  ("🧭","El barrio",["la plaza · la tienda","sigue recto · gira","¿cómo llego a…?"],"Je buurt & de weg."),
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
  '<p>Schrijf de vertaling. el dormitorio = <span class="wl md"></span> · al lado de = <span class="wl md"></span> · la plaza = <span class="wl md"></span> · hay = <span class="wl md"></span></p>', apoyo="Modelo"))
P(actx("V.2", "Distinguir — sorteer per familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Sorteer: <span class="words"><b>la cama · la plaza · encima de · el sofá · la farmacia · debajo de · el armario · cerca de</b></span></p>'
  + sortcols([("mueble",""),("lugar del barrio",""),("preposición","")], eigen=False), apoyo="Banco de palabras"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het Spaanse woord aan (beginletter gegeven). de keuken = <b>c</b>___ · naast = <b>a</b>___ l___ d___ · het park = <b>p</b>___ · er is = <b>h</b>___<br><span class="wl full"></span></p>', apoyo="Primera letra"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Maak één correcte zin met <b>hay · al lado de · el parque</b>.</p><div class="wbox sm"></div>', apoyo=""))
P(actx("V.5", "Comunicar — mi barrio en 3 frases",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Schrijf 3 zinnen over je buurt (qué hay · dónde está · una opinión) en zeg ze hardop.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>', apoyo="Marco"))
P('<div class="se" style="margin-top:6mm">Mi plano de palabras <span class="gloss" style="font-size:8pt">— teken je barrio en label 6 plekken/meubels in het Spaans</span></div>')
P('<div class="wbox lg"></div>')
P(mispal("Mis palabras de la unidad", 7))
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Sigue en la página digital:</span> <span class="g">flip cards (ES↔NL), audio en de spellen bouwen de steun verder af.</span></div></div>')
sec_close()

# ---------- OVERRIDE (bladspiegel-hygiëne, identiek aan U1) ----------
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
   a.href=URL.createObjectURL(blob); a.download='C6plus_U2_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Más español en la práctica · C6+ U2 Aquí vivo</title><style>'
        + CSS + CSS_OVR + RP.CSS + PB.CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/C6plus_U2.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes ·", _AN[0], "genummerde oefeningen (excl. V.1–V.5)")
