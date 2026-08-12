#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de print-HTML C6plus_U3.html (C6+ · Unidad 3 «Conectados») → PDF via Chromium.
# Zelfde componentenkit/CSS als de gelockte golden sample C6+·U0/U1/U2 (geïmporteerd uit gen_u0_print).
# Cursuskleur = paars. Parada 3 = CDMX (México), gastheer Diego.
# Kerngrammatica: ir a + infinitivo (futuro próximo) + acabar de · OI-pronomina le/les · creo que + INDICATIVO.
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
import qr_print as QRP; QRP.fijar("C6+", 3)
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
  <div class="tab">U3 · CONECTADOS</div>
  <div class="eyebrow">UNIDAD 3 · LA RUTA · CDMX 🇲🇽 · CONECTADOS 📱</div>
  <h1>Conectados</h1>
  <div class="sub">La reis cruza «el charco» tot in <b>Ciudad de México</b>, bij <b>Diego</b>. Je leert <b>plannen maken</b> (<b>voy a</b> subir un vídeo), zeggen dat je iets <b>net gedaan</b> hebt (<b>acabo de</b> mandar un mensaje), <b>aan wie</b> je iets stuurt (<b>le</b> escribo a Diego) en je <b>eerste echte mening</b> geven (<b>creo que</b> las redes son útiles). <span class="gloss">Media & technologie: de nabije toekomst met ir a + infinitivo, de voornaamwoorden le/les en je mening met creo que.</span></div>
  <div class="q">¿Qué vas a hacer este fin de semana? <span style="font-weight:400;opacity:.9">· Wat ga je dit weekend doen?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U0 · Reencuentro</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U1 · El día a día</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U2 · Aquí vivo</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U3 · Conectados</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U4 · De viaje</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U5–U7 · el pasado</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 3 · Ciudad de México 🇲🇽.</b> Con <b>Diego</b> entras en el <b>mundo digital</b>: el móvil, las redes, los vídeos y los planes para el finde. CDMX es una de las ciudades más conectadas del mundo hispano. <span class="gloss">Bij Diego duik je in de digitale wereld: gsm, sociale media, video's en weekendplannen. CDMX is een van de meest connected steden van de Spaanstalige wereld.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> <b>Diego</b> te enseña cómo vive <b>en línea</b>: sube vídeos, chatea con amigos y hace planes por el móvil. Aprendes a decir <b>qué vas a hacer</b> (voy a salir), qué <b>acabas de hacer</b> (acabo de subir una foto), <b>a quién</b> escribes (le escribo a mi amiga) y <b>qué opinas</b> de las redes (creo que son útiles pero adictivas). Al final: tu <b>plan de fin de semana</b> en un chat, con tu opinión.
      <span class="gloss">Diego laat zien hoe hij online leeft. Je leert plannen maken, zeggen wat je net deed, aan wie je schrijft en wat je van sociale media vindt. Eindtaak: je weekendplan in een chat, met een mening.</span></div>
      <div class="ojo"><b>¡Ojo! — twee valstrikken meteen scherp:</b> ① <b>ir a + infinitivo</b> = de <b>nabije toekomst</b> (voy a comer = ik ga eten). Vergeet de <b>a</b> niet! ② <b>creo que</b> gaat mét de <b>indicativo</b> (creo que <b>es</b> útil), <b>nooit</b> met de subjuntivo — die zien we niet in deze cursus. <span class="gloss">ir + a + infinitivo · creo que + indicativo (gewone tijd).</span></div>
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
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila digital</span><br><span class="gloss" style="font-size:8.5pt">Vul je rugzak met de woorden van de digitale wereld: el móvil, las redes, subir, voy a…, le escribo, creo que — alles om online te leven en plannen te maken.</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">hablar de medios y redes</span> (el móvil, subir, chatear) <span class="nl">over media & sociale media praten</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">hacer planes</span> con <b>ir a + infinitivo</b> (voy a salir) <span class="nl">plannen maken (nabije toekomst)</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">decir qué acabas de hacer</span> con <b>acabar de + infinitivo</b> <span class="nl">zeggen wat je net deed</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">decir a quién</span> con los pronombres <b>le/les</b> (le escribo) <span class="nl">le/les gebruiken (aan wie?)</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">dar tu opinión</span> con <b>creo que + indicativo</b> (creo que es útil) <span class="nl">je mening geven</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">crear tu <b>«Mi plan de fin de semana»</b></span> <span class="nl">weekendplan-chat (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>El móvil</span><span><b>§2</b>Ir a + inf.</span><span><b>§3</b>Le/les</span><span><b>§4</b>Acabar de · creo que</span><span><b>§5</b>Comunicar y planes</span><span><b>§6</b>Lectura</span><span><b>Taller</b>c/z/qu · tiempo</span><span><b>Cultura</b>Mundo digital</span><span><b>Tarea</b>Mi finde</span><span><b>Repaso</b>Semáforo</span>
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
sec_open("0", "§0 · ¡Ponte al día!", 'Activamos dos cosas que hoy necesitas: el <b>presente</b> (voor je dagelijkse gewoontes online) y <b>gustar</b> (le gusta → dé opstap naar de pronombres <b>le/les</b>). <span class="gloss">We frissen de tegenwoordige tijd en gustar op — «le gusta» is de brug naar de voornaamwoorden le/les.</span>',
        lpd(("8","taalsysteem: presente (repaso)"), ("7","woordenschat: gustar/OI")))
P('<div class="truc"><b>Repaso gustar (U1) → le/les (U3):</b> je kent al <b>me gusta / te gusta / le gusta</b>. Dat kleine woordje <b>le</b> is precies het voornaamwoord van deze unit: het zegt <b>aan wie</b> iets gebeurt. In §3 gebruik je het bij véél meer werkwoorden: <i>le escribo, le mando, les cuento…</i></div>')
P(actx(AN(), "Presente · la vida digital (repaso)",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Vervoeg in het presente (infinitivo tussen haakjes).</p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl sm"></span> (chatear) con mis amigos cada día. &nbsp; 2. Diego <span class="wl sm"></span> (subir) muchos vídeos.<br>'
  '3. Nosotros <span class="wl sm"></span> (navegar) por internet. &nbsp; 4. ¿Tú <span class="wl sm"></span> (seguir, e→i) a muchos artistas?<br>'
  '5. Ellos <span class="wl sm"></span> (compartir) fotos. &nbsp; 6. Yo <span class="wl sm"></span> (encender, e→ie) el ordenador.</p>',
  apoyo="Pista: chateo · sube · navegamos · sigues · comparten · enciendo"))
P(actx(AN(), "Mi opinión · me gustan las redes porque…",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe dos frases: qué te gusta y qué no te gusta de internet, con <b>porque</b>. <span class="gloss">Twee zinnen met porque.</span></p>'
  '<p style="margin-left:12.5mm">Me gustan las redes sociales porque <span class="wl lg"></span><br>No me gusta <span class="wl md"></span> porque <span class="wl md"></span></p>',
  apoyo="Marco: Me gusta(n)… porque… · No me gusta(n)… porque…"))
sec_close()

# ================= §1 · EL MÓVIL Y LAS REDES =================
sec_open("1", "§1 · El móvil y las redes", 'El vocabulario del <b>mundo digital</b>: los <b>aparatos</b> (el móvil, el ordenador, los auriculares), las <b>redes</b> (el perfil, la publicación, el mensaje) y las <b>acciones</b> (subir, chatear, compartir). <span class="gloss">De woordenschat van de digitale wereld: apparaten, sociale media en acties.</span>',
        lpd(("7","woordenschat: medios y redes"), ("8","taalsysteem: género & artículos")))
P('<div class="se">El mundo digital <span class="gloss" style="font-size:8pt">— netwerk in clusters</span></div>')
P('<div class="clusters" style="grid-template-columns:1fr 1fr 1fr">'
  '<div class="clu"><div class="ch"><span class="ci">📱</span>Los aparatos</div><ul><li>el móvil · el ordenador</li><li>la tableta · la pantalla</li><li>los auriculares · el cargador</li></ul><div class="ex">Cargo el móvil por la noche.</div></div>'
  '<div class="clu"><div class="ch"><span class="ci">🌐</span>Las redes</div><ul><li>el perfil · el usuario</li><li>la publicación · el mensaje</li><li>el vídeo · la videollamada</li></ul><div class="ex">Subo un vídeo a mi perfil.</div></div>'
  '<div class="clu"><div class="ch"><span class="ci">📲</span>Las acciones</div><ul><li>chatear · navegar</li><li>subir · descargar</li><li>compartir · seguir</li></ul><div class="ex">Comparto la foto con la clase.</div></div></div>')
P('<div class="truc"><b>¡Ojo! el/la:</b> <b>el</b> móvil, <b>el</b> ordenador, <b>el</b> mensaje, <b>el</b> perfil, <b>el</b> vídeo (m) · <b>la</b> tableta, <b>la</b> pantalla, <b>la</b> app, <b>la</b> contraseña, <b>la</b> publicación (v). <b>los auriculares</b> = altijd meervoud (de oortjes).</div>')
P(actx(AN(), "Relaciona el verbo con el objeto",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Une las dos columnas: escribe la letra. <span class="gloss">Verbind en schrijf de letter.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Verbo</div><div class="cb short">1. subir &nbsp; 2. descargar &nbsp; 3. chatear &nbsp; 4. cargar</div></div>'
  '<div class="wcol"><div class="ch">Objeto</div><div class="cb short">a. una app &nbsp; b. un vídeo &nbsp; c. la batería &nbsp; d. con un amigo</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "Clasifica: ¿aparato, red o acción?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe cada palabra en su columna: <span class="gloss">zet elk woord in de juiste kolom</span> <span class="words"><b>el móvil · subir · el perfil · chatear · la pantalla · el mensaje · descargar · los auriculares</b></span></p>'
  + sortcols([("Aparato",""),("Red / cosa",""),("Acción (verbo)","")], eigen=True), apoyo="Banco de palabras"))
P(actx(AN(), "¿el o la? · el género digital",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★☆☆"}],
  '<p>___ móvil · ___ tableta · ___ pantalla · ___ mensaje · ___ contraseña · ___ perfil · ___ app · ___ vídeo</p>'
  '<p style="margin-left:12.5mm">1.<span class="wl sm"></span> 2.<span class="wl sm"></span> 3.<span class="wl sm"></span> 4.<span class="wl sm"></span> 5.<span class="wl sm"></span> 6.<span class="wl sm"></span> 7.<span class="wl sm"></span> 8.<span class="wl sm"></span></p>',
  apoyo="Pista: el móvil · la tableta · la pantalla · el mensaje · la contraseña · el perfil · la app · el vídeo"))
P(actx(AN(), "El intruso · ¿qué palabra sobra?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★★☆"}],
  '<p>Tacha la palabra que no encaja y di por qué. <span class="gloss">Streep het vreemde woord door en zeg waarom.</span></p>'
  '<p style="margin-left:12.5mm">1. el móvil · la tableta · <b>la cocina</b> · el ordenador → <span class="wl md"></span><br>'
  '2. subir · descargar · <b>dormir</b> · compartir → <span class="wl md"></span><br>'
  '3. el perfil · la publicación · el mensaje · <b>la nevera</b> → <span class="wl md"></span></p>',
  apoyo=""))
P(actx(AN(), "Mi mundo digital · escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escribe tres frases: qué aparatos usas, qué redes y qué haces más. <span class="gloss">Drie zinnen over jouw toestellen en netwerken.</span></p>'
  '<p style="margin-left:12.5mm">Uso <span class="wl lg"></span><br>En las redes <span class="wl lg"></span></p>',
  apoyo="Marco: Uso… para… · Todos los días… · Nunca…"))
sec_close()

retos("movil_c6p", "§1.4 · Retos — la pantalla, medida y traducida",
      'Cinco mensajes que <b>sin emoji</b> ya no significan nada, tu tiempo de pantalla real, y las palabras que nadie traduce.',
      'Vijf berichten die zonder emoji niets meer betekenen, je echte schermtijd, en de woorden die niemand vertaalt.')

# ================= §2 · IR A + INFINITIVO =================
sec_open("2", "§2 · Ir a + infinitivo — el futuro próximo", 'Om te zeggen wat je <b>gaat doen</b> (straks, morgen, dit weekend): <b>ir</b> (vervoegd) + <b>a</b> + <b>infinitivo</b>. <i>Voy a subir un vídeo. Vamos a quedar en la plaza.</i> <span class="gloss">De nabije toekomst: ir vervoegd + a + hele werkwoord.</span>',
        lpd(("8","taalsysteem: ir a + infinitivo"), ("3","spreken/schrijven: planes"), ("7","woordenschat: planes")))

# §2.1 el sistema
P('<h3>§2.1 · ¿Cómo funciona? — la máquina del futuro</h3>')
P(obsbox([
  'Hoy estudio, pero mañana <span class="hl">voy a</span> descansar.',
  'Este finde <span class="hl">vamos a</span> salir y <span class="hl">vamos a</span> ver una peli.',
  '¿Qué <span class="hl">vas a</span> hacer luego? — <span class="hl">Voy a</span> chatear con Diego.',
], vragen='¿Qué dos palabras aparecen siempre antes del infinitivo? <span class="gloss">Welke twee woordjes staan altijd vóór het hele werkwoord?</span>'))
P(machine([("ir → voy/vas/va…","voy"),("+ a","voy a"),("+ infinitivo","voy a salir")]))
P(regla("Regla · ir a + infinitivo", '<table class="conj" style="margin-top:1mm"><thead><tr><th>Persona</th><th>ir</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">voy a</td><td>Voy a <b>subir</b> una foto.</td></tr>'
  '<tr><td class="p">tú</td><td class="v">vas a</td><td>¿Vas a <b>salir</b> hoy?</td></tr>'
  '<tr><td class="p">él/ella</td><td class="v">va a</td><td>Diego va a <b>chatear</b>.</td></tr>'
  '<tr><td class="p">nosotros/as</td><td class="v">vamos a</td><td>Vamos a <b>quedar</b>.</td></tr>'
  '<tr><td class="p">vosotros/as</td><td class="v">vais a</td><td>¿Vais a <b>estudiar</b>?</td></tr>'
  '<tr><td class="p">ellos/ellas</td><td class="v">van a</td><td>Van a <b>ver</b> una peli.</td></tr></tbody></table>'
  '<p style="margin:2mm 0 0">Enkel <b>ir</b> verandert met de persoon. Daarna altijd <b>a</b> + het <b>hele werkwoord</b> (infinitivo). <span class="gloss">Vergeet de <b>a</b> nooit: <span class="trap">voy subir</span> → voy <b>a</b> subir.</span></p>'))
P(actx(AN(), "La gran cloze · ir a + infinitivo",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Escribe <b>ir a + infinitivo</b> (el infinitivo está entre paréntesis). ¡Ojo con la <b>a</b>! <span class="gloss">Vergeet de a niet.</span></p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl md"></span> (subir) un vídeo esta tarde. &nbsp; 2. ¿Tú <span class="wl md"></span> (salir) el sábado?<br>'
  '3. Diego <span class="wl md"></span> (chatear) con nosotros luego. &nbsp; 4. Nosotros <span class="wl md"></span> (quedar) en la plaza.<br>'
  '5. Mis amigos <span class="wl md"></span> (ver) una serie. &nbsp; 6. ¿Vosotros <span class="wl md"></span> (estudiar) mañana?<br>'
  '7. Yo <span class="wl md"></span> (llamar) a mi abuela. &nbsp; 8. Valen <span class="wl md"></span> (compartir) las fotos.</p>',
  apoyo="Banco de palabras: voy a subir · vas a salir · va a chatear · vamos a quedar · van a ver · vais a estudiar · voy a llamar · va a compartir"))
P(actx(AN(), "Clasifica: ¿ahora (presente) o después (ir a)?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Gebeurt het <b>nu/gewoonlijk</b> (presente) of <b>straks</b> (ir a + inf)? <span class="words"><b>Ahora chateo · Mañana voy a salir · Cada día subo fotos · Este finde vamos a quedar · Luego voy a llamar · Normalmente navego</b></span></p>'
  + sortcols([("Ahora / siempre (presente)",""),("Después (ir a + inf.)","")], eigen=False), apoyo="Banco de palabras"))
P('</div>')

# §2.2 expresiones de tiempo + ordenar
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2.2 · ¿Cuándo? — las expresiones de tiempo</span>')
P('<div class="intro"><b>ES:</b> Voor de toekomst gebruik je woorden als <b>luego, mañana, este fin de semana, el próximo mes, pronto</b>. Ze zeggen <b>wanneer</b> je plan gebeurt. <span class="gloss">De tijdsuitdrukkingen die bij ir a + infinitivo passen: straks, morgen, dit weekend…</span></div>')
P('</div>')
P('<div class="fams three" style="margin-top:2mm">'
  '<div class="pcard"><div class="t">Muy pronto</div><div class="ej" style="margin-top:1mm"><b>luego</b> (straks) · <b>más tarde</b> · <b>esta tarde/noche</b></div></div>'
  '<div class="pcard"><div class="t">Mañana</div><div class="ej" style="margin-top:1mm"><b>mañana</b> (morgen) · <b>pasado mañana</b></div></div>'
  '<div class="pcard"><div class="t">El fin de semana</div><div class="ej" style="margin-top:1mm"><b>este fin de semana / el finde</b> · <b>el sábado</b></div></div>'
  '<div class="pcard"><div class="t">Más lejos</div><div class="ej" style="margin-top:1mm"><b>el próximo mes/año</b> · <b>pronto</b> (binnenkort)</div></div></div>')
P(colloc("Chunks del futuro", ["voy a + infinitivo","este finde voy a…","mañana vamos a…","luego te llamo","el próximo año voy a…"]))
P(actx(AN(), "Completa con ir a + una expresión de tiempo",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Completa con <b>ir a + infinitivo</b> y elige una expresión de tiempo. <span class="gloss">Vul aan en kies een tijdsuitdrukking.</span> <span class="words"><b>luego · mañana · este finde · el próximo mes</b></span></p>'
  '<p style="margin-left:12.5mm">1. <span class="wl sm"></span> (tijd) yo <span class="wl md"></span> (llamar) a Diego. &nbsp; 2. <span class="wl sm"></span> (tijd) nosotros <span class="wl md"></span> (salir).<br>'
  '3. <span class="wl sm"></span> (tijd) mis padres <span class="wl md"></span> (comprar) un móvil nuevo.</p>',
  apoyo="Marco: Mañana voy a… · Este finde vamos a… · La semana que viene…"))
P(actx(AN(), "Ordena el plan de Diego (1–5)",
  [{"t":"🔢 Ordenar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Ordena el plan del fin de semana (1–5) y escribe el número. <span class="gloss">Zet het weekendplan in volgorde.</span></p>'
  '<p style="margin-left:12.5mm">'
  '<span class="wl sm"></span> Por la noche voy a ver una peli.<br>'
  '<span class="wl sm"></span> Primero, el sábado por la mañana voy a estudiar.<br>'
  '<span class="wl sm"></span> Después voy a quedar con mis amigos en la plaza.<br>'
  '<span class="wl sm"></span> Luego vamos a comer unos tacos.<br>'
  '<span class="wl sm"></span> Y el domingo voy a descansar.</p>',
  apoyo="Pista: primero → mañana → tarde → noche → domingo"))
P('</div>')

# §2.3 practicar + tarea com
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2.3 · Practicar el futuro próximo</span>')
P('<div class="intro"><b>ES:</b> Ahora entrenamos: corregir errores, cambiar la persona y hablar de tus planes de verdad. <span class="gloss">Verbeteren, van persoon wisselen en echt over je plannen praten.</span></div>')
P('</div>')
P(actx(AN(), "Clínica de errores · ir a + infinitivo",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Elke zin heeft één fout (de <b>a</b> ontbreekt, verkeerde persoon of geen infinitivo). Verbeter.</p>'
  '<p style="margin-left:12.5mm">1. Mañana voy subir un vídeo. → <span class="wl md"></span><br>'
  '2. Diego van a chatear con nosotros. → <span class="wl md"></span><br>'
  '3. Nosotros vamos a salimos el sábado. → <span class="wl md"></span><br>'
  '4. ¿Tú va a estudiar hoy? → <span class="wl md"></span></p>',
  apoyo="Pista: a · va · salir · vas"))
P(actx(AN(), "Sustitución · cambia la persona",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Modelo: <b>Yo voy a salir el sábado.</b> Vuelve a escribirla para cada persona. <span class="gloss">Herschrijf de modelzin per persoon.</span></p>'
  '<p style="margin-left:12.5mm">tú → <span class="wl md"></span> &nbsp; Diego → <span class="wl md"></span> &nbsp; nosotros → <span class="wl md"></span> &nbsp; ellos → <span class="wl md"></span></p>',
  apoyo="Primera letra: vas a…"))
P(actx(AN(), "Traduce · ik ga bellen",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Traduce al español con <b>ir a + infinitivo</b>. <span class="gloss">Vertaal met ir a + infinitief.</span></p>'
  '<p style="margin-left:12.5mm">1. Ik ga bellen. → <span class="wl md"></span> &nbsp; 2. We gaan afspreken. → <span class="wl md"></span><br>'
  '3. Ga jij morgen studeren? → <span class="wl lg"></span></p>',
  apoyo="Marco: voy a + infinitivo"))
P(actx("★", "Tarea comunicativa · ¿qué vas a hacer el finde?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>Pregunta a tu compañero/a por sus planes del fin de semana (¿qué vas a hacer?) y contesta con <b>ir a + infinitivo</b> y una expresión de tiempo. <span class="gloss">Vraag naar de weekendplannen en antwoord met ir a.</span> Noteer 2 plannen van je buur.</p>'
  '<p style="margin-left:12.5mm">— ¿Qué vas a hacer el finde? — <span class="wl lg"></span></p>'
  '<p style="margin-left:12.5mm">Mi compañero/a: 1. <span class="wl full"></span>2. <span class="wl full"></span></p>',
  apoyo="Marco: ¿Qué vas a hacer…? — Voy a… · ¿Quedamos…?"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha «¿Qué vas a hacer el finde?»</b> en la web (TTS). Diego y una amiga hacen planes. <b>1ª vez:</b> ¿qué van a hacer? · <b>2ª vez:</b> ¿cuándo? Escribe los datos.</div>',
           qr("Escanea y escucha", "§2 · Planes de finde", seed=301)))
P('</div>')

retos("ir_a_c6p", "§2.4 · Reto — veinticuatro horas sin pantalla",
      'Planificad el día entero con <b>vamos a</b> — y sobrevivid a tres pegas.',
      'Plan de hele dag met «vamos a» — en overleef drie tegenwerpingen.')

# ================= §3 · OI-PRONOMINA le/les =================
sec_open("3", "§3 · Los pronombres le/les — ¿a quién?", 'Als je zegt <b>aan wie</b> je iets doet (schrijven, sturen, vertellen), gebruik je een <b>meewerkend voorwerp</b>: <b>me/te/le/nos/os/les</b>. <i>Le escribo a Diego. Les mando fotos a mis amigos.</i> <span class="gloss">Het meewerkend voorwerp (aan wie?): le = aan hem/haar/u · les = aan hen.</span>',
        lpd(("8","taalsysteem: OI-pronomina le/les"), ("7","woordenschat: comunicar"), ("4","interactie")))

# §3.1 ¿qué es?
P('<h3>§3.1 · ¿Qué es un pronombre de OI?</h3>')
P('<p style="font-size:9.6pt">Het <b>meewerkend voorwerp</b> (OI) = de <b>persoon</b> die iets ontvangt (aan/voor wie?). Je zet er een klein woordje voor: <b>me/te/le/nos/os/les</b>. Bij <b>le/les</b> mag je de persoon ook nog eens noemen met <b>a</b>:</p>')
P('<div class="agree"><div class="w">Escribo <u>a Diego</u> → <u>Le</u> escribo (a Diego).</div><div class="tie">a Diego (één persoon) → le</div></div>')
P('<div class="agree"><div class="w">Mando fotos <u>a mis amigos</u> → <u>Les</u> mando fotos.</div><div class="tie">a mis amigos (meer personen) → les</div></div>')
P(regla("Regla · me/te/le/nos/os/les (OI)", '<table class="conj" style="margin-top:1mm"><thead><tr><th>A quién</th><th>Pronombre</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="p">a mí</td><td class="v">me</td><td>Diego <b>me</b> escribe.</td></tr>'
  '<tr><td class="p">a ti</td><td class="v">te</td><td><b>Te</b> mando un mensaje.</td></tr>'
  '<tr><td class="p">a él/ella/usted</td><td class="v">le</td><td><b>Le</b> escribo a Diego.</td></tr>'
  '<tr><td class="p">a nosotros/as</td><td class="v">nos</td><td>Mamá <b>nos</b> cuenta algo.</td></tr>'
  '<tr><td class="p">a vosotros/as</td><td class="v">os</td><td><b>Os</b> mando la foto.</td></tr>'
  '<tr><td class="p">a ellos/ellas/ustedes</td><td class="v">les</td><td><b>Les</b> regalo auriculares.</td></tr></tbody></table>'
  '<p style="margin:2mm 0 0">Het pronomen staat <b>vóór</b> het vervoegde werkwoord. <b>le</b> = aan één persoon (hem/haar/u) · <b>les</b> = aan meerdere. <span class="gloss">In het Spaans zeg je vaak <b>le</b> én <b>a Diego</b> samen — dat is normaal.</span></p>'))
P(mirror([("¿A quién le escribes?", "Le escribo a Diego."), ("¿Y a tus amigos?", "Les escribo (a ellos).")]))
P(actx(AN(), "¿le o les?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>Kies le of les.</i></p>'
  '<p style="margin-left:12.5mm">1. <span class="wl sm"></span> escribo a mi amiga. &nbsp; 2. <span class="wl sm"></span> mando fotos a mis padres.<br>'
  '3. <span class="wl sm"></span> cuento un secreto a Diego. &nbsp; 4. <span class="wl sm"></span> regalo auriculares a mis hermanos.<br>'
  '5. <span class="wl sm"></span> pregunto la contraseña a Valen. &nbsp; 6. <span class="wl sm"></span> muestro mi perfil a mis amigos.</p>',
  apoyo="Pista: a + één persoon → le · a + meer → les"))
P(actx(AN(), "Transforma · añade el pronombre",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Voeg <b>le/les</b> toe vóór het werkwoord (de persoon blijft staan met a).</p>'
  '<p style="margin-left:12.5mm">1. Escribo a Diego. → <span class="wl md"></span><br>'
  '2. Mando un mensaje a mis amigos. → <span class="wl md"></span><br>'
  '3. Cuento la noticia a mi madre. → <span class="wl md"></span><br>'
  '4. Regalo un móvil a mi hermano. → <span class="wl md"></span></p>',
  apoyo="Primera letra: Le escribo a Diego…"))
P('</div>')

# §3.2 concordancia + drills
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3.2 · Los verbos de comunicación — practicar</span>')
P('<div class="intro"><b>ES:</b> Het OI hoort vooral bij <b>werkwoorden van communicatie & geven</b>: escribir, mandar, decir, contar, preguntar, regalar, mostrar. Die oefenen we nu. <span class="gloss">le/les komt vaak bij werkwoorden van communiceren & geven.</span></div>')
P('</div>')
P(colloc("Verbos + le/les", ["escribir a alguien","mandar/enviar a alguien","decir/contar a alguien","preguntar a alguien","regalar/mostrar a alguien"]))
P(actx(AN(), "Responde con le/les (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Antwoord met <b>le</b> of <b>les</b> + het werkwoord.</p>'
  '<p style="margin-left:12.5mm">1. ¿Escribes a Diego? — Sí, <span class="wl md"></span> escribo. &nbsp; 2. ¿Mandas fotos a tus amigos? — Sí, <span class="wl md"></span> mando fotos.<br>'
  '3. ¿Cuentas el secreto a Valen? — Sí, <span class="wl md"></span> cuento el secreto. &nbsp; 4. ¿Preguntas la hora a tus padres? — Sí, <span class="wl md"></span> pregunto.<br>'
  '5. ¿Regalas auriculares a tu hermana? — Sí, <span class="wl md"></span> regalo unos.</p>',
  apoyo="Banco de palabras: le · les · le · les · le"))
P(actx(AN(), "Empareja: pregunta ↔ respuesta",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Une cada pregunta con su respuesta: escribe la letra. <span class="gloss">Verbind de vraag met het antwoord.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Pregunta</div><div class="cb short">1. ¿Escribes a Diego? &nbsp; 2. ¿Mandas fotos a tus padres? &nbsp; 3. ¿Cuentas algo a Valen? &nbsp; 4. ¿Preguntas a los profes?</div></div>'
  '<div class="wcol"><div class="ch">Respuesta</div><div class="cb short">a. Sí, les mando fotos. &nbsp; b. Sí, le escribo. &nbsp; c. Sí, les pregunto. &nbsp; d. Sí, le cuento algo.</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
P('</div>')

# §3.3 posición + foutenkliniek + tarea
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3.3 · La posición de le/les</span>')
P('<div class="intro"><b>ES:</b> Normaal <b>vóór</b> het vervoegde werkwoord: <i>Le escribo</i>. Bij <b>ir a + infinitivo</b> mag het ook <b>achteraan vast</b>: <i>Voy a escribir<b>le</b> = <b>Le</b> voy a escribir</i>. <span class="gloss">Vóór het vervoegde werkwoord, óf vastgeplakt aan de infinitief.</span></div>')
P('</div>')
P('<div class="agree"><div class="w"><u>Le</u> escribo un mensaje.</div><div class="tie">vóór het vervoegde werkwoord</div></div>')
P('<div class="agree"><div class="w">Voy a mandar<u>le</u> una foto = <u>Le</u> voy a mandar una foto.</div><div class="tie">bij ir a + inf.: achteraan óf vooraan</div></div>')
P(blocks([[("per","¿a Diego?"),("opt","→"),("ob","Le"),("vb","escribo")], [("per","¿a mis amigos?"),("opt","→"),("ob","Les"),("vb","mando fotos")]]))
P(actx(AN(), "Reescribe con le/les (posición)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vuelve a escribir cada frase con <b>le/les</b> y coloca el pronombre en un sitio correcto. <span class="gloss">Herschrijf met le of les.</span></p>'
  '<p style="margin-left:12.5mm">1. Escribo un mensaje a Diego. → <span class="wl md"></span><br>'
  '2. Voy a mandar fotos a mis amigos. → <span class="wl lg"></span><br>'
  '3. Voy a contar la noticia a Valen. → <span class="wl lg"></span><br>'
  '4. Pregunto la contraseña a mi hermano. → <span class="wl md"></span></p>',
  apoyo="Pista: Le escribo… · Voy a mandarles… / Les voy a mandar…"))
P(actx(AN(), "Clínica de errores · le/les",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Elke zin heeft één fout (le/les of plaats). Verbeter.</p>'
  '<p style="margin-left:12.5mm">1. Escribo le a Diego. → <span class="wl md"></span><br>'
  '2. Mando fotos a mis amigos → Le mando fotos. → <span class="wl md"></span><br>'
  '3. Voy a le escribir. → <span class="wl md"></span><br>'
  '4. Cuento un secreto a Valen → Les cuento un secreto. → <span class="wl md"></span></p>',
  apoyo="Pista: le vóór ww · les = meer personen · achter infinitivo vast"))
P(actx("★", "Tarea comunicativa · ¿a quién le escribes?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Pregunta a tu compañero/a a quién le escribe, le llama o le manda fotos a menudo <span class="gloss">vraag aan wie je buur vaak schrijft, belt of foto\'s stuurt; antwoord met <b>le/les</b>. «¿A quién le escribes cada día? — Le escribo a…» Noteer 3 antwoorden.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>',
  apoyo="Marco: Le escribo a… · Les mando… · Me manda…"))
P('<div class="guide"><div class="ic">🎡</div><div><span class="hand">Online:</span> <span class="g">de <b>vervangingsanimatie le/les</b> en de spellen op de hub oefenen elke keuze én plaats; + cloze en foutenkliniek.</span></div></div>')
P('</div>')

retos("oi_c6p", "§3.4 · Retos — ¿a quién se lo dices?",
      'Catorce mensajes en un grupo donde ya nadie sabe quién le contestó a quién, y un favor que <b>recorre la clase</b>.',
      'Veertien berichten in een groep waar niemand nog weet wie aan wie antwoordde, en een gunst die de hele klas rondgaat.')

# ================= §4 · ACABAR DE + CREO QUE =================
sec_open("4", "§4 · Acabar de + creo que — net gedaan & je mening", 'Twee handige structuren: <b>acabar de + infinitivo</b> = «net … gedaan hebben» (<i>acabo de subir una foto</i>) en <b>creo que / pienso que + indicativo</b> = je <b>mening</b> geven (<i>creo que las redes son útiles</i>). <span class="gloss">acabar de + inf. = net gedaan · creo que + indicativo = je mening.</span>',
        lpd(("8","taalsysteem: acabar de · creo que + indicativo"), ("3","mening geven"), ("7","woordenschat: opinar")))

# §4.1 acabar de
P('<h3>§4.1 · Acabar de + infinitivo — «net gedaan»</h3>')
P(obsbox([
  '— ¿Vienes a comer? — No puedo, <span class="hl">acabo de</span> comer.',
  'Diego <span class="hl">acaba de</span> subir un vídeo nuevo.',
  'Acabamos <span class="hl">de</span> mandar el mensaje.',
], vragen='¿Pasó hace mucho o hace muy poco? <span class="gloss">Is het lang of net gebeurd?</span>'))
P(regla("Regla · acabar de + infinitivo", '<p><b>acabar</b> (vervoegd) + <b>de</b> + <b>infinitivo</b> = «net … gedaan hebben» (heel recent verleden, zonder een echte verleden tijd).<br>'
  '<i>acabo · acabas · acaba · acabamos · acabáis · acaban</i> + <b>de</b> + infinitivo.<br>'
  '<i>Acabo de <b>mandar</b> un mensaje. Diego acaba de <b>conectarse</b>.</i><br>'
  '<span class="gloss">Zelfde bouw als ir a: enkel het eerste werkwoord verandert; daarna <b>de</b> + hele werkwoord.</span></p>'))
P(machine([("acabar → acabo…","acabo"),("+ de","acabo de"),("+ infinitivo","acabo de comer")]))
P(actx(AN(), "Forma frases con acabar de",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe con <b>acabar de + infinitivo</b> (algo que acaba de pasar). <span class="gloss">Schrijf met acabar de: net gebeurd.</span></p>'
  '<p style="margin-left:12.5mm">1. yo / subir una foto → <span class="wl md"></span><br>'
  '2. Diego / mandar un mensaje → <span class="wl md"></span><br>'
  '3. nosotros / comer → <span class="wl md"></span><br>'
  '4. mis amigos / conectarse → <span class="wl md"></span></p>',
  apoyo="Marco: acabo de… · acaba de… · acabamos de… · acaban de…"))
P(actx(AN(), "¿futuro (ir a) o recién (acabar de)?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>¿Se habla de algo que <b>va a pasar</b> (ir a) o que <b>acaba de pasar</b> (acabar de)? Escribe la estructura correcta. <span class="gloss">Toekomst of net gebeurd?</span></p>'
  '<p style="margin-left:12.5mm">1. Mañana <span class="wl md"></span> (yo, salir). &nbsp; 2. ¡Mira! Diego <span class="wl md"></span> (subir) una foto ahora mismo.<br>'
  '3. Este finde <span class="wl md"></span> (nosotros, quedar). &nbsp; 4. No tengo hambre, <span class="wl md"></span> (yo, comer).</p>',
  apoyo="Pista: mañana/finde → ir a · ahora mismo/ya → acabar de"))
P('</div>')

# §4.2 creo que + indicativo
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4.2 · Creo que + indicativo — tu opinión</span>')
P('<div class="intro"><b>ES:</b> Om je <b>mening</b> te geven: <b>creo que · pienso que · me parece que</b> + de <b>gewone tijd</b> (indicativo). <i>Creo que las redes <b>son</b> útiles.</i> Voeg <b>porque</b> toe voor je reden. <span class="gloss">creo que + indicativo (nooit subjuntivo in deze cursus) + porque voor je argument.</span></div>')
P('</div>')
P(obsbox([
  '<span class="hl">Creo que</span> el móvil <span class="hl">es</span> muy útil.',
  '<span class="hl">Pienso que</span> pasamos demasiado tiempo en las redes.',
  '<span class="hl">Me parece que</span> los videojuegos <span class="hl">son</span> adictivos.',
], vragen='¿Qué forma del verbo sigue a «creo que»? ¿Normal o rara? <span class="gloss">Welke werkwoordsvorm volgt op «creo que»? De gewone!</span>'))
P(regla("Regla · dar tu opinión", '<p><b>creo que / pienso que / me parece que / en mi opinión</b> + <b>indicativo</b> (de gewone tegenwoordige tijd die je al kent). <b>Geen subjuntivo</b> in deze cursus.<br>'
  '<i>Creo que <b>es</b> útil. · Pienso que <b>tienes</b> razón. · Me parece que <b>hay</b> un problema.</i><br>'
  'Reageren: <b>(no) estoy de acuerdo · tienes razón · es verdad / es mentira · por un lado… por otro…</b><br>'
  '<span class="gloss">Bouw je mening af: <b>creo que</b> + gewone zin + <b>porque</b> + reden.</span></p>'))
P(actx(AN(), "Cloze · creo que + indicativo",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>cloze (indicativo!).</i> Vervoeg in de <b>gewone tijd</b> na «creo que…».</p>'
  '<p style="margin-left:12.5mm">1. Creo que las redes <span class="wl sm"></span> (ser) útiles. &nbsp; 2. Pienso que Diego <span class="wl sm"></span> (tener) razón.<br>'
  '3. Me parece que nosotros <span class="wl sm"></span> (pasar) mucho tiempo online. &nbsp; 4. Creo que el móvil <span class="wl sm"></span> (ayudar) a estudiar.<br>'
  '5. Pienso que los videojuegos <span class="wl sm"></span> (poder) ser adictivos.</p>',
  apoyo="Banco de palabras: son · tiene · pasamos · ayuda · pueden"))
P(actx(AN(), "¿de acuerdo o no? · clasifica",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Coloca cada reacción en su columna: <span class="gloss">zet elke reactie in de juiste kolom</span> <span class="words"><b>tienes razón · no estoy de acuerdo · es verdad · es mentira · estoy de acuerdo · creo que no</b></span></p>'
  + sortcols([("Estoy de acuerdo 👍",""),("No estoy de acuerdo 👎","")], eigen=False), apoyo="Banco de palabras"))
P(actx(AN(), "Mi opinión sobre las redes · escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Escribe tres frases con <b>creo que / pienso que + indicativo + porque</b>. <span class="gloss">Drie zinnen met je mening en een reden.</span> Banco: útil · práctico · peligroso · adictivo · rápido.</p>'
  '<div class="wbox sm"></div>',
  apoyo="Marco: Creo que … es … porque …"))
P(actx("★", "Tarea comunicativa · debate exprés",
  [{"t":"🗣️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>Tema: «Las redes sociales son buenas para los jóvenes.» A da su opinión (creo que… porque…) y B reacciona <span class="gloss">A geeft een mening, B reageert</span> (estoy de acuerdo / no estoy de acuerdo porque…). Noteer één argument van elk.</p>'
  '<p style="margin-left:12.5mm">A: <span class="wl full"></span>B: <span class="wl full"></span></p>',
  apoyo="Marco: Creo que… porque… · No estoy de acuerdo porque… · Además…"))
P('</div>')

retos("acabar_c6p", "§4.4 · Retos — medio segundo antes, medio segundo después",
      'Doce escenas congeladas, y un podcast donde estáis <b>de acuerdo en no estar de acuerdo</b>.',
      'Twaalf bevroren scènes, en een podcast waarin jullie het eens zijn dat jullie het oneens zijn.')

# ================= §5 · COMUNICAR Y HACER PLANES =================
sec_open("5", "§5 · Comunicar y hacer planes", 'Alles komt samen: de <b>werkwoorden van communicatie</b> (escribir, llamar, mandar, contestar) en de woorden om een <b>afspraak</b> te maken (quedar, salir, ¿cuándo?, ¿dónde?). <span class="gloss">Communiceren en afspreken — met le/les en ir a.</span>',
        lpd(("7","woordenschat: comunicar y planes"), ("4","mondelinge interactie: quedar"), ("3","schrijven: un plan")))
P('<div class="se">Comunicar · las acciones</div>')
P('<div class="clusters" style="grid-template-columns:1fr 1fr 1fr">'
  '<div class="clu"><div class="ch"><span class="ci">✉️</span>Mandar mensajes</div><ul><li>escribir · mandar/enviar</li><li>contestar/responder</li><li>el mensaje · la foto</li></ul></div>'
  '<div class="clu"><div class="ch"><span class="ci">📞</span>Hablar</div><ul><li>llamar · la videollamada</li><li>contar · decir</li><li>preguntar</li></ul></div>'
  '<div class="clu"><div class="ch"><span class="ci">📅</span>Hacer planes</div><ul><li>quedar · salir</li><li>hacer planes</li><li>¿cuándo? ¿dónde?</li></ul></div></div>')
P('<div class="truc"><b>Chunks para quedar:</b> <b>¿Quedamos?</b> (spreken we af?) · <b>¿A qué hora?</b> · <b>¿Dónde?</b> · <b>Vale, nos vemos</b> (oké, tot dan). Un plan: <i>«¿Quedamos el sábado? Vamos a ir al centro y luego le escribo a Diego.»</i></div>')
P(actx(AN(), "Relaciona la acción con el objeto",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Une las dos columnas: escribe la letra. <span class="gloss">Verbind en schrijf de letter.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Verbo</div><div class="cb short">1. mandar &nbsp; 2. contestar &nbsp; 3. quedar &nbsp; 4. hacer</div></div>'
  '<div class="wcol"><div class="ch">Objeto</div><div class="cb short">a. el mensaje &nbsp; b. un mensaje / una foto &nbsp; c. planes &nbsp; d. en la plaza</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "Completa el chat de planes",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Completa con <b>quedamos · voy a · le · vamos a · vas a</b>. <span class="gloss">Vul aan met die vijf woorden.</span></p>'
  '<p style="margin-left:12.5mm">— ¡Hola! ¿<span class="wl sm"></span> el sábado? &nbsp; — ¡Vale! ¿Qué <span class="wl sm"></span> hacer?<br>'
  '— <span class="wl sm"></span> ir al centro y luego <span class="wl sm"></span> escribo a Diego para invitarlo. &nbsp; — Genial, <span class="wl sm"></span> comer tacos juntos.</p>',
  apoyo="Banco de palabras"))
P(actx(AN(), "Dictado · un plan para el finde",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escucha y escribe las cinco frases (con ir a / le / acabar de). <span class="gloss">Luister en schrijf de vijf zinnen.</span></p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span>4. <span class="wl full"></span>5. <span class="wl full"></span></p>',
  apoyo="docent/audio leest voor"))
P(actx("★", "Info-gap · organizamos el finde",
  [{"t":"🗣️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>A y B hacen juntos un plan para el fin de semana: proponed (voy a… / ¿quedamos…?) y decidid día, hora y lugar. <span class="gloss">Maak samen een weekendplan.</span> Noteer het afgesproken plan.</p>'
  '<p style="margin-left:12.5mm">Nuestro plan: <span class="wl full"></span><span class="wl full"></span></p>',
  apoyo="Marco: ¿Puedes el sábado? — Sí, pero voy a… · Entonces quedamos a las…"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha «Quedamos el sábado»</b> en la web (TTS): Diego y una amiga organizan el finde. <b>1ª vez:</b> ¿qué van a hacer? · <b>2ª vez:</b> ¿cuándo y dónde quedan?</div>',
           qr("Escanea y escucha", "§5 · Quedamos el sábado", seed=302)))
sec_close()

# ================= §6 · LECTURA =================
sec_open("6", "§6 · Lectura 1 — «¿Adicto al móvil?»", 'Una encuesta y dos opiniones sobre el tiempo de pantalla. Lee, busca información y da tu opinión. <span class="gloss">Een enquête en twee meningen over schermtijd. Lezen, info zoeken, je mening geven.</span>',
        lpd(("1","lezen: hoofdgedachte"), ("2","lezen: info selecteren"), ("5","identiteit & cultuur")))
P('<div class="lecdoel"><b>Antes de leer:</b> mira el título «¿Adicto al móvil?». ¿De qué va a hablar el texto? <span class="gloss">Waar zal de tekst over gaan?</span></div>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> encuesta / opiniones</span><span class="tm"><b>Fuente:</b> revista juvenil</span><span class="tm"><b>Objetivo:</b> reflexionar sobre el móvil</span></div>')
P(f'<div class="ptexts">'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["diego"]}</div><div><div class="nm">Diego</div><div class="fr">CDMX 🇲🇽</div></div></div>'
  f'<p>Yo <span class="evi">paso muchas horas</span> con el móvil: subo vídeos, chateo y sigo a muchos artistas. Creo que el móvil <span class="evi">es muy útil</span> para estudiar y para hablar con mis amigos lejos. Pero también pienso que a veces es <span class="evi">adictivo</span>: acabo de mirar la pantalla y, cinco minutos después, la miro otra vez. Este finde voy a hacer una cosa: <span class="evi">apagar</span> el móvil dos horas al día.</p></div>'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["lucia"]}</div><div><div class="nm">Lucía</div><div class="fr">Sevilla 🇪🇸</div></div></div>'
  f'<p>A mí me gustan las redes, pero no paso tanto tiempo. Creo que las redes <span class="evi">conectan</span> a la gente, pero también <span class="evi">pueden ser peligrosas</span> si compartes demasiado. En mi opinión, lo importante es el <span class="evi">equilibrio</span>: uso el móvil para lo práctico y luego lo apago. Por un lado es genial, por otro hay que tener cuidado.</p></div></div>')
P(actx(AN(), "Verdadero o falso — con prueba",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escribe V o F y copia en la tercera columna la frase del texto que lo demuestra. <span class="gloss">Schrijf V of F en kopieer de bewijszin.</span></p>'
  '<table class="alf"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba (cita)</th></tr></thead><tbody>'
  '<tr><td>Diego cree que el móvil es útil para estudiar.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Diego va a usar el móvil aún más este finde.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Lucía piensa que las redes pueden ser peligrosas.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>',
  apoyo="Modelo"))
P(actx(AN(), "Escanea — completa la ficha",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Busca los datos de cada persona en el texto y completa la tabla. Una palabra o un número por casilla. <span class="gloss">Zoek de gegevens en vul de tabel aan.</span></p>'
  '<table class="alf"><thead><tr><th>—</th><th>Diego</th><th>Lucía</th></tr></thead><tbody>'
  '<tr><td>¿Qué opina del móvil/redes?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>¿Qué problema ve?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>¿Qué va a hacer / qué hace?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>',
  apoyo=""))
P(actx(AN(), "Reacciona — ¿y tú?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>¿Estás más de acuerdo con Diego o con Lucía? Escribe 2–3 frases con <b>creo que + porque</b>. <span class="gloss">Twee tot drie zinnen met je mening.</span> Voeg één plan toe met <b>voy a</b>.</p>'
  '<div class="wbox sm"></div>',
  apoyo="Marco: Estoy más de acuerdo con … porque … Este finde voy a …"))
sec_close()

# ================= TALLER =================
sec_open("T", "Taller de lengua", 'Dos herramientas: la <b>c/z/qu</b> (de klank /k/ en /θ/ in tech-woorden) y los <b>conectores de tiempo</b> (primero, después, luego, más tarde) om je plan te ordenen. <span class="gloss">De spelling c/z/qu en de tijdsconnectoren.</span>')
P('<h3>1 · Ortografía — c / z / qu</h3>')
P(regla("El sonido /k/ y /θ/", '<p>Voor de <b>/k/</b>-klank: <b>c</b> vóór a/o/u (<b>c</b>ontraseña, <b>c</b>argador) en <b>qu</b> vóór e/i (bus<b>qu</b>e, <b>qu</b>edar). Voor de <b>/θ/</b>-klank (zachte c): <b>z</b> vóór a/o/u en <b>c</b> vóór e/i (la <b>c</b>ena, el <b>z</b>umo).<br><span class="gloss">Nooit <span class="trap">qua/quo</span>: gebruik <b>cua/cuo</b> (cuando). Nooit <span class="trap">ze/zi</span> in gewone woorden: gebruik <b>ce/ci</b>.</span></p>'))
P(actx(AN(), "¿c, z o qu? · completa",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Vul <b>c</b>, <b>z</b> of <b>qu</b> in.</p>'
  '<p style="margin-left:12.5mm">la _ontraseña · el _argador · _edar (afspreken) · bus_ar · la _ena · el _umo · _uando · la músi_a</p>',
  apoyo="Pista: contraseña, cargador, quedar, buscar, cena, zumo, cuando, música"))
P('<h3 style="margin-top:6mm">2 · Conectores de tiempo — ordena tu plan</h3>')
P(colloc("primero · después · luego · más tarde · por último", ["primero = eerst","después / luego = daarna","más tarde = later","al final / por último = ten slotte"]))
P(actx(AN(), "Ordena el plan con conectores",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Vuelve a escribir el plan en orden con <b>primero, después, luego, más tarde, al final</b>. <span class="gloss">Herschrijf het plan in volgorde.</span></p>'
  '<p style="margin-left:12.5mm">ver una peli · quedar con amigos · estudiar · comer tacos · descansar<br>'
  '1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span>4. <span class="wl full"></span>5. <span class="wl full"></span></p>',
  apoyo="Marco: Primero… · Luego… · Después… · Por último…"))
sec_close()

# ================= LECTURA 2 · ESCUCHA =================
# Zelfde bron als de digitale hub (lectura_data / escucha_data): papier en scherm
# kunnen zo niet uit elkaar lopen. Elk op een eigen bladzijde (§14).
P('<div class="page"><div class="parada sec">')
P('<span class="num">7</span><span class="pk">§7 · Lectura 2 — «¿Cuántas horas de pantalla?»</span>')
P('<div class="intro"><b>ES:</b> Un artículo con una encuesta de verdad. <b>No hace falta entenderlo todo</b> para sacar la información. <span class="gloss">Een echt artikel met een enquête. Je hoeft niet alles te begrijpen — zoek de cijfers én kijk wie wat vindt.</span></div>')
P(PB.lectura_print(LD.C6P_U3, AN()))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">8</span><span class="pk">§8 · Escucha — «Cómo hacer una videollamada con la abuela»</span>')
P('<div class="intro"><b>ES:</b> Diego le explica a su abuela, paso a paso. <b>Escucha primero, escribe después.</b> <span class="gloss">Diego legt het zijn oma stap voor stap uit. Eerst luisteren, dan schrijven; het transcript staat online en gaat pas open ná de taken.</span></div>')
P(PB.escucha_print(ED.C6P_U3, AN()))
P('</div>')

# ================= CULTURA =================
sec_open("C", "Cultura · el mundo digital hispano", 'La cultura hispana <b>en línea</b>: el <b>reguetón</b> que conquista el streaming, <b>WhatsApp</b> como red número uno en Latinoamérica y el <b>español</b> como una de las lenguas más usadas de internet. <span class="gloss">De Spaanstalige wereld online: reggaeton op streaming, WhatsApp in Latijns-Amerika en het Spaans als grote internettaal.</span>',
        lpd(("5","identiteit in diversiteit: el mundo digital hispano")))
P('<div class="fams three" style="margin-top:2mm">'
  '<div class="pcard"><div class="t">🎵 El reguetón manda</div><div class="ej" style="margin-top:2mm">Artiesten als <b>Bad Bunny</b> (Puerto Rico) en <b>Karol G</b> (Colombia) breken streamingrecords op Spotify en YouTube. Het Spaans is wereldwijd te horen — vaak zonder vertaling.</div></div>'
  '<div class="pcard"><div class="t">💬 WhatsApp, la red nº 1</div><div class="ej" style="margin-top:2mm">In veel Latijns-Amerikaanse landen is <b>WhatsApp</b> dé manier om te communiceren — met familie, vrienden én winkels. «Te mando un audio» hoor je overal.</div></div>'
  '<div class="pcard"><div class="t">🌐 El español en internet</div><div class="ej" style="margin-top:2mm">Het Spaans is de <b>tweede taal</b> op sociale media na het Engels. Meer dan 500 miljoen sprekers zetten de digitale wereld deels in het Spaans.</div></div></div>')
P('<div class="route-note" style="margin-top:5mm">🗺️ <b>En la web:</b> haz clic en México (★) en el mapa para descubrir CDMX, Diego y su música. <span class="gloss">Online: klik op México voor CDMX en de música-fiche.</span></div>')
P(actx(AN(), "Compara · tú y el mundo digital hispano",
  [{"t":"🌍 Cultura","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>¿Qué redes usas tú y cuáles se usan en Latinoamérica? Escribe dos frases con <b>creo que</b> o <b>me gusta</b>. <span class="gloss">Twee zinnen met je mening.</span></p>'
  '<div class="wbox sm"></div>',
  apoyo="Marco: Aquí… pero allí… · Nosotros… y ellos…"))
P(actx(AN(), "Datos curiosos — une",
  [{"t":"🌍 Cultura","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Une las dos columnas: escribe la letra. <span class="gloss">Verbind en schrijf de letter.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Elemento</div><div class="cb short">1. Bad Bunny &nbsp; 2. WhatsApp &nbsp; 3. el español &nbsp; 4. Karol G</div></div>'
  '<div class="wcol"><div class="ch">Dato</div><div class="cb short">a. red nº 1 en Latinoamérica &nbsp; b. 2ª lengua en redes sociales &nbsp; c. reguetón de Puerto Rico, récords en Spotify &nbsp; d. cantante de Colombia</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo="Banco de palabras"))
sec_close()

retos("cultura_c6p3", "Retos — explicar y desmontar",
      'El algoritmo explicado a tu abuela <b>sin una palabra en inglés</b>, y el mensaje falso que aprendes a reconocer escribiéndolo tú.',
      'Het algoritme uitgelegd aan je grootmoeder zonder één Engels woord, en het valse bericht dat je leert herkennen door het zelf te schrijven.')

# ================= TAREA FINAL =================
sec_open("★", "Tarea final · «Mi plan de fin de semana»", 'Escribe un <b>chat/post</b> con tus <b>planes de fin de semana</b> (ir a + infinitivo), di <b>a quién</b> vas a escribir (le/les) y da tu <b>opinión</b> (creo que…). <span class="gloss">Schrijf een chat/post met je weekendplannen, aan wie je schrijft en een mening.</span>')
P(fmu('tus compañeros de clase (el grupo de chat)', 'contar tu plan de finde y tu opinión', 'un chat/post (6–8 mensajes) + una presentación oral (± 1 min)'))
P('<ol class="pasos">'
  '<li><b>Escribe 3–4 planes</b> con <b>ir a + infinitivo</b> y una <b>expresión de tiempo</b>: «El sábado <b>voy a</b> quedar con… Luego <b>vamos a</b>…».</li>'
  '<li><b>Di a quién escribes/llamas</b> con <b>le/les</b>: «<b>Le</b> escribo a Diego para invitarlo. <b>Les</b> mando la hora a mis amigos».</li>'
  '<li><b>Añade algo que acabas de hacer</b>: «<b>Acabo de</b> crear el grupo».</li>'
  '<li><b>Da tu opinión</b> con <b>creo que + indicativo + porque</b>: «Creo que va a ser un finde genial porque…».</li>'
  '<li><b>Preséntalo en pareja</b> y <b>graba</b> tu plan en la web. Escúchate y mejora.</li></ol>')
P('<div class="se" style="margin-top:4mm">Mi chat de planes <span class="gloss" style="font-size:8pt">· 6–8 berichten</span></div><div class="wbox lg"></div>')
P('<div class="se" style="margin-top:3mm">Mi opinión <span class="gloss" style="font-size:8pt">· creo que … porque …</span></div><div class="wbox sm"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba tu plan de finde</b> en la web (recorder + rúbrica). Escucha, compara con el modelo y vuelve a grabar.</div>',
           qr("Escanea y graba", "Tarea · Mi plan de fin de semana", seed=370)))
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Ik geef ≥3 plannen met <b>ir a + infinitivo</b> (+ de <b>a</b>)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>le</b> én <b>les</b> correct</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik één keer <b>acabar de + infinitivo</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik geef een <b>mening</b> met «creo que… porque…» (indicativo)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>presenteer vlot</b> (± 1 min)</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — el plan de mi compañero/a</div>'
  '<table><thead><tr><th>Un plan que también quiero hacer</th><th>Una pregunta que le hago</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('<div class="truc" style="margin-top:3mm"><b>✍️ Antes de enviar:</b> lees je tekst na — <i>ir <b>a</b> + infinitivo? · le/les correct? · una opinión con creo que + indicativo?</i> Verbeter één ding: <span class="wl lg"></span></div>')
sec_close()

# ================= REPASO =================
sec_open("✓", "Repaso · lo esencial", 'Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag; de volledige herhaling staat online.</span>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>Ir a + infinitivo</b> (futuro próximo): voy/vas/va/vamos/vais/van + <b>a</b> + infinitivo. <i>Voy a salir.</i> Vergeet de <b>a</b> niet!</li>'
  '<li><b>Acabar de + infinitivo</b> (net gedaan): acabo/acabas/acaba… + <b>de</b> + infinitivo. <i>Acabo de comer.</i></li>'
  '<li><b>Le/les (OI):</b> aan wie? le = één persoon · les = meerdere. Staat vóór het ww. of achter de infinitivo. <i>Le escribo a Diego.</i></li>'
  '<li><b>Creo que + indicativo:</b> mening met de gewone tijd (nooit subjuntivo). <i>Creo que es útil porque…</i></li>'
  '<li><b>Reageren:</b> (no) estoy de acuerdo · tienes razón · es verdad/mentira · por un lado… por otro…</li>'
  '<li><b>Las trampas:</b> 🔴 voy <b>a</b> subir (niet «voy subir») · 🔴 le/les vóór het ww. · 🔴 creo que + <b>indicativo</b> · 🔴 los auriculares = meervoud.</li></ul></div>')
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> spelletjes met zelfcorrectie (ir a / le-les / acabar de / creo que, planes, media…).</div>')
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td>over <b>media en redes</b> praten</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>plannen maken</b> met ir a + infinitivo</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>de pronombres <b>le/les</b> gebruiken (aan wie?)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>zeggen wat ik <b>net gedaan</b> heb (acabar de)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>mijn <b>mening</b> geven met creo que + porque</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil para mí: <span class="wl md"></span> · Lo que quiero practicar más: <span class="wl md"></span></i></div>')
P('<div class="se" style="margin-top:6mm">Auto-test rápido · ¿lo sé?</div>')
P('<p style="margin-left:0">1. «Ik ga bellen» = <span class="wl md"></span><br>'
  '2. ¿le of les? «___ mando fotos a mis amigos» = <span class="wl sm"></span><br>'
  '3. acabar de: «Ik heb net gegeten» = <span class="wl md"></span><br>'
  '4. «Creo que las redes ___ (ser) útiles» = <span class="wl sm"></span><br>'
  '5. Geef één plan voor het weekend (1 zin): <span class="wl lg"></span></p>')
P('<div class="bridge"><b>» Siguiente parada: U4 «De viaje».</b> Ya haces planes y das tu opinión; en <b>U4</b> preparas un <b>viaje</b> por el mundo hispano: el transporte, el alojamiento y qué vas a hacer allí. ¡Seguimos! <span class="gloss">In U4: reizen door de Spaanstalige wereld — vervoer, verblijf en wat je er gaat doen.</span></div>')
sec_close()

# ================= §V VOCABULARIO =================
VOC = json.load(open(f"{HERE}/u3_vocab.json", encoding="utf-8"))
GRP = [("dispositivos","Los aparatos"), ("internet","Internet y las redes"), ("digital","Acciones digitales"),
       ("comunicar","Comunicar (verbos + le/les)"), ("planes","Hacer planes · ir a"),
       ("opinar","Dar tu opinión · creo que"), ("adjmedia","Adjetivos del mundo digital")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (begrijpen en zelf gebruiken)")))
P('</div>')
P('<p style="font-size:9.6pt">Las palabras del <b>mundo digital</b> como red — tres familias:</p>')
P(clusters([
  ("📱","Los aparatos y redes",["el móvil · el ordenador","el perfil · el mensaje","la app · la contraseña"],"Waarmee je online gaat."),
  ("📲","Las acciones",["subir · descargar","chatear · compartir","escribir · mandar"],"Wat je online doet."),
  ("🗓️","Planes y opinión",["voy a + inf.","acabar de + inf.","creo que · pienso que"],"Plannen & je mening."),
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
  '<p>Escribe la traducción. <span class="gloss">Schrijf de vertaling.</span> el móvil = <span class="wl md"></span> · subir = <span class="wl md"></span> · las redes = <span class="wl md"></span> · creo que = <span class="wl md"></span></p>', apoyo="Modelo"))
P(actx("V.2", "Distinguir — sorteer per familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Clasifica: <span class="gloss">sorteer deze woorden</span> <span class="words"><b>el móvil · subir · el mensaje · chatear · la tableta · compartir · el perfil · descargar</b></span></p>'
  + sortcols([("aparato/red",""),("acción (verbo)","")], eigen=False), apoyo="Banco de palabras"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Completa la palabra en español; tienes la primera letra. <span class="gloss">de beginletter staat erbij</span><br>de gsm = <b>m</b>___ · uploaden = <b>s</b>___ · het bericht = <b>m</b>___ · ik denk dat = <b>c</b>___ q___<br><span class="wl full"></span></p>', apoyo="Primera letra"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Escribe una frase correcta con <b>voy a · el vídeo · subir</b>.</p><div class="wbox sm"></div>', apoyo=""))
P(actx("V.5", "Comunicar — mi vida digital en 3 frases",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Escribe tres frases sobre tu vida digital (qué usas · un plan con ir a · una opinión con creo que) y dilas en voz alta. <span class="gloss">Drie zinnen over je digitale leven.</span></p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>', apoyo="Marco: Uso… · Voy a… · Creo que… porque…"))
P('<div class="se" style="margin-top:6mm">Mi red de palabras <span class="gloss" style="font-size:8pt">— teken je scherm en label 6 apps/acties in het Spaans</span></div>')
P('<div class="wbox lg"></div>')
P(mispal("Mis palabras de la unidad", 7))
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Sigue en la página digital:</span> <span class="g">flip cards (ES↔NL), audio en de spellen bouwen de steun verder af.</span></div></div>')
sec_close()

# ---------- OVERRIDE (bladspiegel-hygiëne, identiek aan U2) ----------
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
   a.href=URL.createObjectURL(blob); a.download='C6plus_U3_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Más español en la práctica · C6+ U3 Conectados</title><style>'
        + CSS + CSS_OVR + RP.CSS + PB.CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/C6plus_U3.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes ·", _AN[0], "genummerde oefeningen (excl. V.1–V.5)")
