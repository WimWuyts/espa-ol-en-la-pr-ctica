#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de print-HTML C6plus_U7.html (C6+ · Unidad 7 «¡Opina y cuídate!») → PDF via Chromium.
# Zelfde componentenkit/CSS als de gelockte golden sample C6+·U0–U6 (geïmporteerd uit gen_u0_print).
# Cursuskleur = paars. Parada 7 = Costa Rica («pura vida»). Laatste unit → versie 1.
# Kerngrammatica: imperativo afirmativo (tú) + pronombres enclíticos · opinar y argumentar (indicativo + conectores).
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
import qr_print as QRP; QRP.fijar("C6+", 7)
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
  <div class="tab">U7 · ¡OPINA Y CUÍDATE!</div>
  <div class="eyebrow">UNIDAD 7 · LA RUTA · COSTA RICA 🇨🇷 · ¡PURA VIDA! 🌿</div>
  <h1>¡Opina y cuídate!</h1>
  <div class="sub">La última parada: <b>Costa Rica</b>, «<b>pura vida</b>». Aprendes a <b>dar consejos</b> con el <b>imperativo</b> (<b>cuida</b> tu salud, <b>come</b> sano, <b>haz</b> deporte, <b>recicla</b>) y a <b>dar tu opinión y argumentar</b> sobre la salud y el medio ambiente. <span class="gloss">Advies geven, je mening geven en argumenteren.</span></div>
  <div class="q">¿Qué haces tú para cuidarte y cuidar el planeta? <span style="font-weight:400;opacity:.9">· Wat doe jij om voor jezelf én de planeet te zorgen?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U3 · Conectados</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U4 · De viaje</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U5 · Érase una vez</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U6 · Cuando era pequeño</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U7 · ¡Opina y cuídate!</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">🏁 Fin de la ruta</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 7 · Costa Rica 🇨🇷 — la última.</b> Llegas al país de la «<b>pura vida</b>»: sin ejército, líder en <b>ecoturismo</b> y <b>biodiversidad</b>. Aquí aprendes a <b>dar consejos</b> y a <b>opinar</b> sobre la salud y el medio ambiente. <span class="gloss">De laatste halte: Costa Rica, land van «pura vida», ecotoerisme en biodiversiteit. Hier leer je advies geven en je mening geven.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> Cierras la ruta con dos herramientas para la vida: <b>dar consejos</b> (<i>cuídate, come sano, recicla</i>) y <b>opinar y argumentar</b> (<i>creo que… porque… además…</i>). Hablas de la <b>salud</b> (el cuerpo, el deporte, la dieta) y del <b>medio ambiente</b> (reciclar, ahorrar, proteger el planeta). Al final: creas tu <b>«cartel de opinión»</b> con consejos y argumentos.
      <span class="gloss">Je sluit de reis af met twee vaardigheden voor het leven: advies geven en je mening beargumenteren, over gezondheid en milieu.</span></div>
      <div class="ojo"><b>¡Ojo! — dos trampas desde el primer día:</b> ① El <b>imperativo (tú)</b> es muy corto: -ar → <b>-a</b> (cuida), -er/-ir → <b>-e</b> (come, vive). Ocho irregulares: <b>ten, ven, pon, haz, di, sal, sé, ve</b>. El pronombre se pega: cuida+te → <b>cuídate</b>. ② <b>creo que</b> va con indicativo. <span class="gloss">Korte vormen, acht onregelmatige, en het pronomen plakt vast.</span></div>
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
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila del final</span><br><span class="gloss" style="font-size:8.5pt">Vul je rugzak met de laatste woorden: cuídate, come sano, recicla, creo que, porque, además — alles om advies te geven en je mening te beargumenteren.</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">dar consejos</span> con el imperativo (cuídate, come sano) <span class="nl">advies geven</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar el imperativo (tú)</span> regular + irregular (haz, ven, di…) <span class="nl">de gebiedende wijs</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">añadir pronombres</span> (cuída<b>te</b>, haz<b>lo</b>, dí<b>melo</b>) <span class="nl">pronomen aanplakken</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">opinar</span> (creo que, en mi opinión, estoy de acuerdo) <span class="nl">je mening geven</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">argumentar</span> con <b>porque · además · por eso · sin embargo</b> <span class="nl">argumenteren met conectoren</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">crear tu <b>«cartel de opinión»</b></span> <span class="nl">opinie-affiche (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>Salud y planeta</span><span><b>§2</b>Imperativo</span><span><b>§3</b>Opinar</span><span><b>§4</b>Conectores</span><span><b>§5</b>Lectura</span><span><b>Taller</b>enclíticos</span><span><b>Cultura</b>Pura vida</span><span><b>Tarea</b>Cartel</span><span><b>Repaso</b>Semáforo</span>
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
sec_open("0", "§0 · ¡Ponte al día!", 'Venimos del <b>imperfecto</b> (U6: era, tenía). Ahora, dos cosas nuevas: <b>dar consejos</b> (imperativo) y <b>dar tu opinión</b> (creo que… + indicativo). <span class="gloss">Van beschrijven naar advies geven en argumenteren.</span>',
        lpd(("8","taalsysteem: imperativo + opinar"), ("7","woordenschat")))
P('<div class="truc"><b>Consejo ↔ opinión:</b> un <b>consejo</b> es una orden o un truco (<i>¡Come sano!</i>) → imperativo. Una <b>opinión</b> es lo que tú piensas (<i>Creo que la salud es importante</i>) → creo que + indicativo. En U7 aprendes los dos. <span class="gloss">Advies gaat met de imperativo, mening met creo que.</span></div>')
P(actx(AN(), "¿Consejo u opinión? (repaso)",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>¿Es un <b>consejo</b> (imperativo) o una <b>opinión</b> (creo que…)? Marca. <span class="gloss">Advies of mening?</span></p>'
  '<p style="margin-left:12.5mm">1. Come más fruta. → <span class="wl sm"></span> &nbsp; 2. Creo que el deporte es importante. → <span class="wl sm"></span><br>'
  '3. Recicla el papel. → <span class="wl sm"></span> &nbsp; 4. En mi opinión, hay mucha basura. → <span class="wl sm"></span></p>',
  apoyo="Pista: un imperativo (recicla, apaga) es un consejo; «creo que / en mi opinión» es una opinión"))
P(actx(AN(), "Mis hábitos · escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe dos cosas que haces por tu salud o por el medio ambiente (en presente). <span class="gloss">Twee dingen die je doet.</span></p>'
  '<p style="margin-left:12.5mm">Para mi salud, yo <span class="wl lg"></span><br>Por el medio ambiente, yo <span class="wl lg"></span></p>',
  apoyo="Marco: Siempre… · A veces… · Nunca… porque…"))
sec_close()

# ================= §1 · SALUD Y MEDIO AMBIENTE =================
sec_open("1", "§1 · La salud y el medio ambiente", 'Twee woordvelden: de <b>gezondheid</b> (el cuerpo, sano, el deporte, la dieta, dormir) en het <b>milieu</b> (el planeta, reciclar, la basura, ahorrar, proteger). <span class="gloss">De woorden van gezondheid en milieu.</span>',
        lpd(("7","woordenschat: salud & medio ambiente"), ("5","identiteit: hábitos")))
P('<div class="se">Dos redes de palabras <span class="gloss" style="font-size:8pt">— netwerk in clusters</span></div>')
P('<div class="clusters" style="grid-template-columns:1fr 1fr 1fr">'
  '<div class="clu"><div class="ch"><span class="ci">💪</span>La salud</div><ul><li>sano · enfermo</li><li>el cuerpo · el ejercicio</li><li>dormir · descansar</li></ul><div class="ex">Como sano y hago deporte.</div></div>'
  '<div class="clu"><div class="ch"><span class="ci">🥗</span>Los consejos</div><ul><li>comer sano · beber agua</li><li>hacer deporte · evitar</li><li>relajarse · moverse</li></ul><div class="ex">Bebe mucha agua.</div></div>'
  '<div class="clu"><div class="ch"><span class="ci">🌍</span>El planeta</div><ul><li>reciclar · la basura</li><li>ahorrar · la energía</li><li>proteger · el árbol</li></ul><div class="ex">Recicla y ahorra agua.</div></div></div>')
P('<div class="truc"><b>Tegenstellingen:</b> <b>sano</b> (gezond) ↔ <b>enfermo</b> (ziek) · <b>limpio</b> (schoon) ↔ <b>sucio</b> (vuil) · <b>ahorrar</b> (besparen) ↔ <b>gastar</b> (verspillen) · <b>proteger</b> (beschermen) ↔ <b>contaminar</b> (vervuilen).</div>')
P(actx(AN(), "Relaciona la palabra con el grupo",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Une las dos columnas: escribe la letra. <span class="gloss">Verbind en schrijf de letter.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Palabra</div><div class="cb short">1. reciclar &nbsp; 2. el ejercicio &nbsp; 3. la basura &nbsp; 4. dormir</div></div>'
  '<div class="wcol"><div class="ch">Grupo</div><div class="cb short">a. salud (acción) &nbsp; b. medio ambiente (problema) &nbsp; c. medio ambiente (acción) &nbsp; d. salud (descanso)</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "Clasifica: ¿salud o medio ambiente?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe cada palabra en su columna: <span class="gloss">zet elk woord in de juiste kolom</span> <span class="words"><b>el cuerpo · reciclar · la dieta · la contaminación · el deporte · el árbol · descansar · la energía</b></span></p>'
  + sortcols([("La salud",""),("El medio ambiente","")], eigen=True), apoyo="Banco de palabras"))
P(actx(AN(), "Contrarios · empareja",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★★☆"}],
  '<p>Une cada palabra de la izquierda con su contrario de la derecha: escribe la letra. <span class="gloss">Verbind met het tegengestelde.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">—</div><div class="cb short">1. sano &nbsp; 2. ahorrar &nbsp; 3. proteger &nbsp; 4. limpio</div></div>'
  '<div class="wcol"><div class="ch">—</div><div class="cb short">a. contaminar &nbsp; b. sucio &nbsp; c. enfermo &nbsp; d. gastar</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "Mis consejos · escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escribe tres consejos con el infinitivo (comer sano, reciclar…). <span class="gloss">Drie tips met het infinitief.</span></p>'
  '<p style="margin-left:12.5mm">Para estar sano: <span class="wl md"></span> y <span class="wl md"></span><br>Por el planeta: <span class="wl lg"></span></p>',
  apoyo="Marco: Recicla… · Apaga… · Come… · No uses…"))
sec_close()

retos("salud_c6p", "§1.4 · Retos — la salud en cifras y en treinta segundos",
      'La huella de la clase, calculada de verdad, y una cuña de radio con <b>problema, consecuencia y consejo</b>.',
      'De voetafdruk van de klas, echt berekend, en een radiospot met probleem, gevolg en advies.')

# ================= §2 · EL IMPERATIVO =================
sec_open("2", "§2 · El imperativo (tú) — dar consejos", 'Om <b>advies of instructies te geven</b>: het <b>imperativo</b> (tú). Regelmatig heel kort: -ar → <b>-a</b> (cuida), -er/-ir → <b>-e</b> (come, vive). Slechts <b>8 onregelmatige</b>: <b>ten, ven, pon, haz, di, sal, sé, ve</b>. <span class="gloss">De gebiedende wijs (jij-vorm) — voor tips en instructies.</span>',
        lpd(("8","taalsysteem: imperativo afirmativo"), ("7","woordenschat: salud"), ("3","advies geven")))

# §2.1 el sistema
P('<h3>§2.1 · Las formas — la máquina del imperativo</h3>')
P(obsbox([
  '<span class="hl">Come</span> más fruta y <span class="hl">bebe</span> mucha agua.',
  '<span class="hl">Haz</span> deporte y <span class="hl">duerme</span> ocho horas.',
  '<span class="hl">Recicla</span> el papel y <span class="hl">protege</span> el planeta.',
], vragen='¿Cómo terminan los verbos en -ar? ¿Y los de -er/-ir? ¿Cuáles son irregulares? <span class="gloss">Kijk naar de uitgangen en de uitzonderingen.</span> <span class="gloss">-ar → -a · -er/-ir → -e · 8 irregulares.</span>'))
P(machine([("-ar cuidar","raíz cuid-"),("+ -a","cuida")]))
P(machine([("-er/-ir comer","raíz com-"),("+ -e","come")]))
P(regla("Regla · imperativo afirmativo (tú)", '<table class="conj" style="margin-top:1mm"><thead><tr><th>Infinitivo</th><th>Imperativo (tú)</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="p">cuidar (-ar)</td><td class="v">cuida</td><td>¡Cuida tu salud!</td></tr>'
  '<tr><td class="p">comer (-er)</td><td class="v">come</td><td>¡Come sano!</td></tr>'
  '<tr><td class="p">escribir (-ir)</td><td class="v">escribe</td><td>¡Escribe aquí!</td></tr></tbody></table>'
  '<p style="margin:2mm 0 0"><b>Los 8 irregulares:</b> tener → <b>ten</b> · venir → <b>ven</b> · poner → <b>pon</b> · hacer → <b>haz</b> · decir → <b>di</b> · salir → <b>sal</b> · ser → <b>sé</b> · ir → <b>ve</b>. <span class="gloss">🔴 Let op: <b>haz</b> deporte (niet «hace»), <b>ve</b> al médico. Verandering o→ue/e→ie blijft: dormir → <b>duerme</b>, mover → <b>mueve</b>.</span></p>'))
P(actx(AN(), "Forma el imperativo (tú)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Vorm de imperativo voor <b>tú</b>. Acht werkwoorden, waarvan er drie onregelmatig zijn.</p>'
  '<p style="margin-left:12.5mm">cuidar → <span class="wl sm"></span> &nbsp; beber → <span class="wl sm"></span> &nbsp; reciclar → <span class="wl sm"></span><br>'
  'hacer → <span class="wl sm"></span> &nbsp; venir → <span class="wl sm"></span> &nbsp; decir → <span class="wl sm"></span></p>',
  apoyo="Modelo: -a / -e; haz/ven/di"))
P(actx(AN(), "La gran cloze · imperativo (consejos de salud)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Escribe el <b>imperativo (tú)</b> (el infinitivo está entre paréntesis). <span class="gloss">Vul de gebiedende wijs in.</span></p>'
  '<p style="margin-left:12.5mm">1. <span class="wl md"></span> (comer) más verdura. &nbsp; 2. <span class="wl md"></span> (beber) dos litros de agua.<br>'
  '3. <span class="wl md"></span> (hacer) deporte tres veces por semana. &nbsp; 4. <span class="wl md"></span> (dormir) ocho horas.<br>'
  '5. <span class="wl md"></span> (reciclar) el plástico. &nbsp; 6. <span class="wl md"></span> (ahorrar) energía.<br>'
  '7. <span class="wl md"></span> (ir) al médico una vez al año. &nbsp; 8. <span class="wl md"></span> (ser) responsable con la basura.</p>',
  apoyo="Banco de palabras: come · bebe · haz · duerme · recicla · ahorra · ve · sé"))
P(actx(AN(), "Del infinitivo al consejo · transforma",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Convierte cada consejo en una <b>orden</b> (imperativo). <span class="gloss">Maak van elke tip een gebiedende wijs.</span></p>'
  '<p style="margin-left:12.5mm">1. Es bueno comer fruta. → <span class="wl md"></span> fruta.<br>'
  '2. Hay que hacer deporte. → <span class="wl md"></span> deporte.<br>'
  '3. Es importante reciclar. → <span class="wl md"></span></p>',
  apoyo="Primera letra: come · haz · recicla"))
P('</div>')

# §2.2 pronombres enclíticos
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2.2 · El imperativo + pronombres (enclíticos)</span>')
P('<div class="intro"><b>ES:</b> En el imperativo afirmativo el pronombre se <b>pega detrás</b>: cuida + te → <b>cuídate</b>, haz + lo → <b>hazlo</b>, di + me + lo → <b>dímelo</b>. <span class="gloss">Het pronomen plakt vast, en soms komt er een accent bij.</span></div>')
P('</div>')
P(blocks([[("per","cuida"),("opt","+ te"),("vb","cuídate")], [("per","haz"),("opt","+ lo"),("vb","hazlo")], [("per","di"),("opt","+ me"),("vb","dime")], [("per","di"),("opt","+ me + lo"),("vb","dímelo")]]))
P('<div class="truc"><b>¡Ojo, el acento!</b> Cuando la palabra crece, mantienes el acento en su sitio con una <b>tilde</b>: cuida → <b>cuídate</b>, protege → <b>protégelo</b>, di+me+lo → <b>dímelo</b>. Formas cortas sin tilde: <b>hazlo, dime, ponlo</b>. <span class="gloss">De klemtoon blijft waar ze zat, dus komt er een accent bij.</span></div>')
P(actx(AN(), "Añade el pronombre",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Plak het pronomen vast (let op het accent).</p>'
  '<p style="margin-left:12.5mm">cuida + te → <span class="wl sm"></span> &nbsp; haz + lo → <span class="wl sm"></span> &nbsp; recicla + lo → <span class="wl sm"></span><br>'
  'bebe + la → <span class="wl sm"></span> &nbsp; di + me → <span class="wl sm"></span> &nbsp; protege + lo → <span class="wl sm"></span></p>',
  apoyo="Modelo: werkwoord + pronomen = één woord; het accent blijft op de klemtoon van het werkwoord"))
P(actx(AN(), "Clínica de errores · imperativo",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 3 min"},{"t":"★★★"}],
  '<p>Elke zin heeft één fout (vorm, pronomen of accent). Verbeter.</p>'
  '<p style="margin-left:12.5mm">1. ¡Hace deporte cada día! → <span class="wl md"></span><br>'
  '2. Cuida te mucho. → <span class="wl md"></span><br>'
  '3. El papel: recicla lo. → <span class="wl md"></span><br>'
  '4. Ir al médico. (bevel) → <span class="wl md"></span></p>',
  apoyo="Pista: haz · cuídate · recíclalo · ve"))
P(actx(AN(), "Cinco consejos para un amigo",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Je vriend is moe en gestrest. Geef 5 tips met de imperativo (+ pronomen waar mogelijk).</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span>4. <span class="wl full"></span>5. <span class="wl full"></span></p>',
  apoyo="Banco de palabras: duerme · relájate · come sano · haz deporte · cuídate"))
P('</div>')

# §2.3 aplicar + tarea com
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2.3 · Un cartel de consejos</span>')
P('<div class="intro"><b>ES:</b> Aplicamos: haz un mini-cartel con consejos para el planeta. <span class="gloss">We passen toe: een mini-affiche met tips.</span></div>')
P('</div>')
P(actx(AN(), "Mi mini-cartel · el medio ambiente",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het affiche in met 4 bevelen (imperativo).</p>'
  '<table class="alf"><thead><tr><th>🌍 ¡Cuida el planeta!</th><th>Consejo (imperativo)</th></tr></thead><tbody>'
  '<tr><td>el agua</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>el papel/plástico</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>la energía</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>los árboles</td><td><span class="wl lg"></span></td></tr></tbody></table>',
  apoyo="Marco: Ahorra… · Recicla… · Apaga… · Protege…"))
P(actx("★", "Tarea comunicativa · un consejo para tu compañero/a",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>Tu compañero/a quiere vivir más sano. Dale tres consejos en voz alta (imperativo) y escucha los suyos. Anota dos. <span class="gloss">Geef drie tips en noteer er twee.</span></p>'
  '<p style="margin-left:12.5mm">Mis consejos: <span class="wl full"></span></p>'
  '<p style="margin-left:12.5mm">Consejos para mí: 1. <span class="wl full"></span>2. <span class="wl full"></span></p>',
  apoyo="Marco: Para estar mejor, … · Es importante… porque…"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha «¿Qué opinas del medio ambiente?»</b> en la web (TTS): Valen y Diego opinan. <b>1ª vez:</b> ¿de qué hablan? · <b>2ª vez:</b> ¿qué consejo dan? Escribe.</div>',
           qr("Escanea y escucha", "§2 · ¿Qué opinas del medio ambiente?", seed=701)))
P('</div>')

retos("imperativo_c6p", "§2.4 · Retos — mandar sin sonar a sermón",
      'Un consejo que nadie pidió, un cartel de <b>tres palabras</b>, y una consulta médica imposible.',
      'Advies waar niemand om vroeg, een affiche van drie woorden, en een onmogelijk doktersconsult.')

# ================= §3 · OPINAR Y ARGUMENTAR =================
sec_open("3", "§3 · Opinar y argumentar", 'Om je <b>mening te geven</b>: <b>creo que</b>, <b>pienso que</b>, <b>en mi opinión</b>, <b>me parece que</b> + de <b>indicativo</b> (géén subjuntivo). Om te reageren: <b>estoy de acuerdo</b> / <b>no estoy de acuerdo</b>, <b>tienes razón</b>. <span class="gloss">Je mening geven en op de mening van een ander reageren.</span>',
        lpd(("8","taalsysteem: opinar con indicativo"), ("4","interactie: mening & akkoord")))

# §3.1 el sistema
P('<h3>§3.1 · Dar tu opinión</h3>')
P(obsbox([
  '<span class="hl">Creo que</span> la salud <span class="hl">es</span> lo más importante.',
  '<span class="hl">En mi opinión</span>, <span class="hl">debemos</span> reciclar más.',
  '— <span class="hl">Estoy de acuerdo</span>. — Pues yo <span class="hl">no estoy de acuerdo</span>.',
], vragen='Welk werkwoord komt na «creo que»: subjuntivo of gewoon indicativo? <span class="gloss">Gewoon de indicativo: creo que ES / debemos.</span>'))
P(mirror([("— ¿Qué opinas del deporte?", "— Creo que es muy importante para la salud."), ("— ¿Y del reciclaje?", "— Pienso que debemos reciclar más.")]))
P(regla("Regla · opinar (indicativo)", '<p><b>Mening geven:</b> <b>Creo que</b> / <b>Pienso que</b> / <b>Me parece que</b> / <b>En mi opinión,</b> + <b>indicativo</b> (es, tiene, debemos…). <span class="gloss">🔴 Géén subjuntivo hier: creo que <b>es</b> (niet «sea»).</span><br>'
  '<b>Reageren:</b> (No) estoy de acuerdo · Tienes razón · Yo pienso lo mismo · Yo, en cambio, creo que… <span class="gloss">akkoord / oneens / gelijk hebben.</span></p>'))
P(actx(AN(), "Da tu opinión · completa",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Complétalo con tu propia opinión (en indicativo). <span class="gloss">Vul je eigen mening aan.</span></p>'
  '<p style="margin-left:12.5mm">1. Creo que el deporte <span class="wl lg"></span><br>'
  '2. En mi opinión, el medio ambiente <span class="wl lg"></span><br>'
  '3. Me parece que la comida rápida <span class="wl lg"></span></p>',
  apoyo="Marco: … es importante / … está en peligro"))
P(actx(AN(), "¿De acuerdo o no? · reacciona",
  [{"t":"🗣️ Interacción","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Reageer op elke stelling met <b>estoy de acuerdo</b> of <b>no estoy de acuerdo</b> + waarom.</p>'
  '<p style="margin-left:12.5mm">1. «El coche es mejor que la bici.» → <span class="wl lg"></span><br>'
  '2. «Reciclar no sirve para nada.» → <span class="wl lg"></span></p>',
  apoyo="Marco: No estoy de acuerdo porque…"))
P('</div>')

# §3.2 practicar + tarea com
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3.2 · Practicar la opinión</span>')
P('<div class="intro"><b>ES:</b> Entrenamos con una encuesta y un mini-debate. <span class="gloss">Oefenen met een enquête en een mini-debat.</span></div>')
P('</div>')
P(actx(AN(), "Encuesta · ¿qué opinas?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Geef je mening (creo que… + indicativo).</p>'
  '<table class="alf"><thead><tr><th>Tema</th><th>Mi opinión</th></tr></thead><tbody>'
  '<tr><td>el deporte</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>la comida sana</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>reciclar</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>los coches en la ciudad</td><td><span class="wl lg"></span></td></tr></tbody></table>',
  apoyo="Marco: Creo que… · Me parece que… · En mi opinión…"))
P(actx("★", "Tarea comunicativa · mini-debate",
  [{"t":"🗣️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>Elige una afirmación: una está <b>a favor</b> y otra <b>en contra</b>. Da tu opinión y un argumento (porque…). <span class="gloss">Kies een stelling en geef één argument.</span> Noteer.</p>'
  '<p style="margin-left:12.5mm">Tema: <span class="wl md"></span></p>'
  '<p style="margin-left:12.5mm">A favor: <span class="wl full"></span>En contra: <span class="wl full"></span></p>',
  apoyo="Marco: Creo que… porque…"))
P('<div class="guide"><div class="ic">🎡</div><div><span class="hand">Online:</span> <span class="g">de <b>meningszinnen</b> en de spellen op de hub oefenen opinar/argumentar; + cloze en foutenkliniek.</span></div></div>')
P('</div>')

retos("opinar", "§3.4 · Retos — creer, comprobar y defender lo contrario",
      'Cuatro afirmaciones sobre salud de las que <b>dos son falsas</b>, y un debate donde defiendes lo que no piensas.',
      'Vier beweringen over gezondheid waarvan er twee vals zijn, en een debat waarin je verdedigt wat je niet vindt.')

# ================= §4 · CONECTORES =================
sec_open("4", "§4 · Conectores — argumentar", 'Para <b>argumentar</b> enlazas tus opiniones con <b>conectores</b>: <b>porque</b>, <b>además</b>, <b>por eso</b>, <b>sin embargo</b>, <b>por un lado / por otro lado</b>. <span class="gloss">omdat · bovendien · daarom · echter · enerzijds/anderzijds.</span>',
        lpd(("8","taalsysteem: conectores argumentativos"), ("4","interactie: argumenteren")))

# §4.1 el sistema
P('<h3>§4.1 · Los conectores del argumento</h3>')
P(obsbox([
  'Reciclo <span class="hl">porque</span> es importante. <span class="hl">Además</span>, ahorra dinero.',
  'El coche contamina; <span class="hl">por eso</span> voy en bici.',
  '<span class="hl">Por un lado</span> es cómodo; <span class="hl">por otro lado</span>, contamina.',
], vragen='¿Qué conector da una razón? ¿Cuál añade algo? ¿Cuál da una consecuencia? <span class="gloss">Reden, toevoeging of gevolg?</span> <span class="gloss">porque = reden · además = toevoeging · por eso = gevolg.</span>'))
P('<div class="fams three" style="margin-top:2mm">'
  '<div class="pcard"><div class="t">porque</div><div class="ej">reden (omdat/want): … porque es sano.</div></div>'
  '<div class="pcard"><div class="t">además · por eso</div><div class="ej">toevoeging / gevolg: además… · por eso…</div></div>'
  '<div class="pcard"><div class="t">sin embargo</div><div class="ej">tegenstelling (echter): …, sin embargo…</div></div></div>')
P('<div class="truc"><b>¡Ojo, trampa NL→ES!</b> «want» y «omdat» son <b>porque</b>. «dus» es <b>por eso / así que</b>, no «luego». «bovendien» es <b>además</b>. Pon <b>coma</b> después de «además», «por eso» o «sin embargo» al principio de la frase. <span class="gloss">Let ook op de komma na een conector vooraan de zin.</span></div>')
P(actx(AN(), "Completa con el conector",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Completa con <b>porque · además · por eso · sin embargo</b>. <span class="gloss">Vul het verbindingswoord aan.</span></p>'
  '<p style="margin-left:12.5mm">1. Como fruta <span class="wl md"></span> es sana.<br>'
  '2. Hago deporte; <span class="wl md"></span>, duermo mejor.<br>'
  '3. El plástico contamina; <span class="wl md"></span> lo reciclo.<br>'
  '4. Es caro; <span class="wl md"></span>, funciona muy bien.</p>',
  apoyo="Banco de palabras"))
P(actx(AN(), "Ordena el argumento",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Ordena (1–4): opinión → argumento → añadido → conclusión. <span class="gloss">Zet in een logische volgorde.</span></p>'
  '<p style="margin-left:12.5mm">☐ Por eso, en mi ciudad hay muchas bicis. &nbsp; ☐ Creo que la bici es genial.<br>'
  '☐ Además, es bueno para la salud. &nbsp; ☐ Porque no contamina.</p>'
  '<p style="margin-left:12.5mm">Orden: <span class="wl sm"></span> - <span class="wl sm"></span> - <span class="wl sm"></span> - <span class="wl sm"></span></p>',
  apoyo="Pista: opinión eerst, conclusie laatst"))
P('</div>')

# §4.2 a favor / en contra + relativo
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4.2 · A favor y en contra</span>')
P('<div class="intro"><b>ES:</b> Un buen argumento tiene dos lados. Ordena ideas <b>a favor</b> y <b>en contra</b> y escribe un mini-texto. <span class="gloss">Voor- en tegenargumenten ordenen en een mini-tekst schrijven.</span></div>')
P('</div>')
P(actx(AN(), "Clasifica: ¿a favor o en contra? (del coche en la ciudad)",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Zet elk argument in de juiste kolom: <span class="words"><b>es rápido · contamina · es cómodo · hace ruido · gasta gasolina · protege de la lluvia</b></span></p>'
  + sortcols([("A favor",""),("En contra","")], eigen=True), apoyo="Banco de palabras"))
P(actx(AN(), "Mi mini-texto de opinión",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Schrijf 4 zinnen: mening + reden (porque) + toevoeging (además) + conclusie (por eso).</p>'
  '<div class="wbox sm"></div>',
  apoyo="Marco: Creo que… porque… Además… Por eso…"))
P(actx(AN(), "Une con que / porque",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Une las frases con <b>que</b> o <b>porque</b>. <span class="gloss">Verbind met que of porque.</span></p>'
  '<p style="margin-left:12.5mm">1. Uso una botella. La botella es reutilizable. → <span class="wl lg"></span><br>'
  '2. Reciclo. Es importante para el planeta. → <span class="wl lg"></span></p>',
  apoyo="Primera letra: …que es reutilizable · …porque es importante"))
P('</div>')

retos("conectores", "§4.4 · Retos — enlazar lo que se dice",
      'Primero le das la razón y solo después matizas. Y al final: el <b>manifiesto</b> de la clase.',
      'Eerst geef je gelijk en pas dan nuanceer je. En op het eind: het manifest van de klas.')

# ================= §5 · LECTURA =================
sec_open("5", "§5 · Lectura 1 — «Diez consejos para el planeta»", 'Een informatieve advies-/opinietekst. Lee, busca los consejos y reacciona. <span class="gloss">Een advies-/opinietekst. Lezen, de tips zoeken, reageren.</span>',
        lpd(("1","lezen: hoofdgedachte"), ("2","lezen: info selecteren"), ("5","identiteit & cultuur")))
P('<div class="lecdoel"><b>Antes de leer:</b> mira el título. ¿Qué consejos esperas encontrar? <span class="gloss">Welke tips verwacht je?</span></div>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> artículo / decálogo</span><span class="tm"><b>Fuente:</b> revista escolar «Pura Vida»</span><span class="tm"><b>Objetivo:</b> convencer y aconsejar</span></div>')
P(f'<div class="ptexts">'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["valen"]}</div><div><div class="nm">Revista «Pura Vida»</div><div class="fr">Costa Rica 🇨🇷</div></div></div>'
  f'<p>El planeta nos necesita. <span class="evi">Creo que</span> todos podemos ayudar con pequeños gestos. Aquí van diez consejos: <span class="evi">recicla</span> el papel, el vidrio y el plástico. <span class="evi">Ahorra</span> agua: cierra el grifo. <span class="evi">Apaga</span> las luces que no usas. <span class="evi">Usa</span> la bici o el transporte público, <span class="evi">porque</span> el coche contamina mucho. <span class="evi">Come</span> más verdura y menos carne. <span class="evi">No tires</span> basura al suelo. <span class="evi">Planta</span> un árbol si puedes. <span class="evi">Además</span>, comparte estos consejos con tu familia. En Costa Rica muchos jóvenes ya lo hacen: <span class="evi">en mi opinión</span>, son un ejemplo. ¡El planeta es de todos! <span class="evi">Por eso</span>, cuídalo hoy.</p></div></div>')
P(actx(AN(), "Verdadero o falso — con prueba",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>¿Verdadero (V) o falso (F)? Subraya la prueba. <span class="gloss">Waar of niet waar? Onderstreep het bewijs.</span></p>'
  '<table class="alf"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba (cita)</th></tr></thead><tbody>'
  '<tr><td>El texto recomienda usar el coche.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Aconseja comer más verdura.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Dice que el planeta es de todos.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>',
  apoyo="Modelo"))
P(actx(AN(), "Escanea — busca los imperativos",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Busca en el texto y escribe cinco <b>órdenes</b> (imperativo). <span class="gloss">Zoek vijf gebiedende wijzen in de tekst.</span></p>'
  '<p style="margin-left:12.5mm">1. <span class="wl sm"></span> 2. <span class="wl sm"></span> 3. <span class="wl sm"></span> 4. <span class="wl sm"></span> 5. <span class="wl sm"></span></p>',
  apoyo=""))
P(actx(AN(), "Reacciona — ¿y tú?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>¿Qué consejo te parece el más importante? Escribe 2–3 frases con una <b>opinión</b> (creo que…) y un <b>conector</b> (porque/además). <span class="gloss">Twee tot drie zinnen met mening en verbindingswoord.</span></p>'
  '<div class="wbox sm"></div>',
  apoyo="Marco: Para mí, el consejo más importante es… porque…"))
sec_close()

# ================= TALLER =================
sec_open("T", "Taller de lengua", 'Dos herramientas: el <b>acento</b> con pronombres enclíticos (cuídate, dímelo) y los <b>conectores de argumentación</b>. <span class="gloss">Accenten bij aangehechte pronomen plus de argumentatie-connectoren.</span>')
P('<h3>1 · Ortografía — el acento en los enclíticos</h3>')
P(regla("El acento del imperativo + pronombre", '<p>Cuando pegas un pronombre detrás, la palabra crece. Para mantener el acento en su sitio suele aparecer una <b>tilde</b>: cuida → <b>cuídate</b>, come → <b>cómelo</b>, protege → <b>protégelo</b>, di+me+lo → <b>dímelo</b>.<br><span class="gloss">🔴 Korte vormen krijgen géén accent: <b>hazlo, dime, ponlo, dilo</b>.</span></p>'))
P(actx(AN(), "¿Falta el acento? · corrige",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>cuidate · comelo · protegelo · dimelo · hazlo · dime</p>'
  '<p style="margin-left:12.5mm"><span class="wl full"></span></p>',
  apoyo=""))
P('<h3 style="margin-top:6mm">2 · Conectores de argumentación</h3>')
P(colloc("porque · además · por eso · sin embargo", ["porque = want/omdat","además = bovendien","por eso = daarom","sin embargo = echter"]))
P(actx(AN(), "Completa con el conector",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Completa con <b>porque · además · por eso</b>. <span class="gloss">Vul het verbindingswoord aan.</span></p>'
  '<p style="margin-left:12.5mm">1. Voy en bici <span class="wl md"></span> no contamina.<br>'
  '2. La bici es sana; <span class="wl md"></span>, es barata.<br>'
  '3. El aire está sucio; <span class="wl md"></span> uso mascarilla.</p>',
  apoyo="Banco de palabras"))
sec_close()

# ================= LECTURA 2 · ESCUCHA =================
# Zelfde bron als de digitale hub (lectura_data / escucha_data): papier en scherm
# kunnen zo niet uit elkaar lopen. Elk op een eigen bladzijde (§14).
P('<div class="page"><div class="parada sec">')
P('<span class="num">6</span><span class="pk">§6 · Lectura 2 — «Carta al director»</span>')
P('<div class="intro"><b>ES:</b> Una carta al director de verdad, con todos los conectores en su sitio. <b>No hace falta entenderlo todo</b> para seguir el argumento. <span class="gloss">Een echte ingezonden brief, met alle verbindingswoorden op hun plaats. Je hoeft niet alles te begrijpen — volg de opbouw van het betoog.</span></div>')
P(PB.lectura_print(LD.C6P_U7, AN()))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">7</span><span class="pk">§7 · Escucha — «En la consulta»</span>')
P('<div class="intro"><b>ES:</b> Mateo duerme mal y recibe cuatro consejos; uno no lo acepta. <b>Escucha primero, escribe después.</b> <span class="gloss">Mateo slaapt slecht en krijgt vier adviezen; eentje weigert hij. Eerst luisteren, dan schrijven; het transcript staat online en gaat pas open ná de taken.</span></div>')
P(PB.escucha_print(ED.C6P_U7, AN()))
P('</div>')

# ================= CULTURA =================
sec_open("C", "Cultura · Costa Rica y la «pura vida»", 'Costa Rica es un país especial: <b>no tiene ejército</b> desde 1948, es líder mundial en <b>ecoturismo</b> y protege una <b>biodiversidad</b> enorme (¡el 5 % de las especies del planeta!). Su lema: «<b>pura vida</b>» — una forma de saludar, dar las gracias y decir que todo va bien. <span class="gloss">Costa Rica: geen leger, ecotoerisme, enorme biodiversiteit, en het motto «pura vida».</span>',
        lpd(("5","identiteit in diversiteit: Costa Rica")))
P('<div class="fams three" style="margin-top:2mm">'
  '<div class="pcard"><div class="t">🕊️ Sin ejército</div><div class="ej" style="margin-top:2mm">En <b>1948</b> Costa Rica abolió su <b>ejército</b>. Ese dinero va a la <b>educación</b> y a la <b>sanidad</b>. Un ejemplo de paz único en el mundo. <span class="gloss">Een land zonder leger sinds 1948.</span></div></div>'
  '<div class="pcard"><div class="t">🌿 Ecoturismo</div><div class="ej" style="margin-top:2mm">Más del <b>25 %</b> del país es <b>naturaleza</b> protegida: selva, volcanes, playas. Costa Rica es líder mundial en <b>turismo sostenible</b>. <span class="gloss">Een kwart van het land is beschermde natuur.</span></div></div>'
  '<div class="pcard"><div class="t">🐒 ¡Pura vida!</div><div class="ej" style="margin-top:2mm">«<b>Pura vida</b>» se oye por todas partes: como saludo, como gracias o como «todo bien». Resume el <b>optimismo</b> de los «ticos». <span class="gloss">Groet, bedankje en «alles oké» in twee woorden.</span></div></div></div>')
P('<div class="route-note" style="margin-top:5mm">🗺️ <b>En la web:</b> haz clic en Costa Rica (★) en el mapa para descubrir la «pura vida» y cerrar la ruta. <span class="gloss">Online: klik op Costa Rica om de reis af te sluiten.</span></div>')
P(actx(AN(), "Opina · ¿pura vida?",
  [{"t":"🌍 Cultura","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>¿Te parece bien un país sin ejército? Da tu opinión (creo que…) y un argumento (porque…). Escribe dos frases. <span class="gloss">Geef je mening met een argument.</span></p>'
  '<div class="wbox sm"></div>',
  apoyo="Marco: Creo que… porque… · Además… · Por eso…"))
P(actx(AN(), "Datos curiosos — une",
  [{"t":"🌍 Cultura","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Une las dos columnas: escribe la letra. <span class="gloss">Verbind en schrijf de letter.</span></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Elemento</div><div class="cb short">1. 1948 &nbsp; 2. pura vida &nbsp; 3. ecoturismo &nbsp; 4. biodiversidad</div></div>'
  '<div class="wcol"><div class="ch">Dato</div><div class="cb short">a. saludo y filosofía tica &nbsp; b. fin del ejército &nbsp; c. 5 % de las especies &nbsp; d. turismo en la naturaleza</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo="Banco de palabras"))
sec_close()

retos("cultura_c6p7", "Reto — una campaña que cruza el océano",
      'Lo que funciona en Gante no siempre dice nada en Cartagena. Cambiar la forma, mantener la idea.',
      'Lo que funciona en Gante a veces no dice nada en Cartagena: cambia la forma y conserva la idea. <span class="gloss">Verander de vorm, houd het idee.</span>')

# ================= TAREA FINAL =================
sec_open("★", "Tarea final · «Mi cartel de opinión»", 'Crea un <b>cartel</b> sobre la salud o el medio ambiente: da <b>consejos</b> (imperativo) y tu <b>opinión argumentada</b> (creo que… porque… además…). <span class="gloss">Maak een affiche met advies en je beargumenteerde mening — de capstone van de reis.</span>')
P(fmu('tus compañeros de clase (la exposición «Pura Vida»)', 'convencer y aconsejar', 'un cartel (título + 4 consejos + un texto de opinión de 4–5 frases) + una presentación oral (± 1–2 min)'))
P('<ol class="pasos">'
  '<li><b>Elige un tema</b>: la salud o el medio ambiente.</li>'
  '<li><b>Da 4 consejos</b> con el <b>imperativo</b> (+ pronomen): «Recicla el papel», «Cuídate».</li>'
  '<li><b>Escribe tu opinión</b> (4–5 frases): «Creo que… <b>porque</b>… <b>Además</b>… <b>Por eso</b>…».</li>'
  '<li><b>Reacciona</b> a una posible objeción: «Sin embargo, algunos dicen que… pero…».</li>'
  '<li><b>Preséntalo</b> y <b>graba</b> tu cartel en la web. Escúchate y mejora.</li></ol>')
P('<div class="se" style="margin-top:4mm">Mis 4 consejos (imperativo) <span class="gloss" style="font-size:8pt">· ¡Recicla! ¡Cuídate!</span></div><div class="wbox sm"></div>')
P('<div class="se" style="margin-top:3mm">Mi texto de opinión <span class="gloss" style="font-size:8pt">· creo que… porque… además… por eso…</span></div><div class="wbox lg"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba tu cartel</b> en la web (recorder + rúbrica). Escucha, compara con el modelo y vuelve a grabar.</div>',
           qr("Escanea y graba", "Tarea · Mi cartel de opinión", seed=770)))
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Ik geef advies met de <b>imperativo</b> (cuídate, recicla…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik minstens één <b>pronomen</b> (cuídate, hazlo)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik geef een <b>mening</b> (creo que… + indicativo)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik minstens <b>twee conectoren</b> (porque, además…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>presenteer vlot</b> (± 1–2 min)</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — el cartel de mi compañero/a</div>'
  '<table><thead><tr><th>Un consejo que me gusta</th><th>Una pregunta / objeción</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('<div class="truc" style="margin-top:3mm"><b>✍️ Antes de exponer:</b> lees je tekst na — <i>imperativo correct? · un pronombre? · una opinión con indicativo? · dos conectores?</i> Verbeter één ding: <span class="wl lg"></span></div>')
sec_close()

# ================= REPASO =================
sec_open("✓", "Repaso · lo esencial", 'Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag; de volledige herhaling staat online.</span>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>Imperativo (tú):</b> -ar → -a (cuida) · -er/-ir → -e (come, vive).</li>'
  '<li><b>8 irregulares:</b> ten · ven · pon · haz · di · sal · sé · ve.</li>'
  '<li><b>+ pronombre:</b> cuídate · hazlo · dímelo (let op het accent).</li>'
  '<li><b>Opinar (indicativo):</b> creo que / pienso que / en mi opinión + es/debemos… (géén subjuntivo).</li>'
  '<li><b>Reageren:</b> (no) estoy de acuerdo · tienes razón.</li>'
  '<li><b>Conectores:</b> porque (reden) · además (toevoeging) · por eso (gevolg) · sin embargo (tegenstelling).</li>'
  '<li><b>Las trampas:</b> 🔴 haz, no «hace» · 🔴 la tilde: cuídate · 🔴 «want» y «omdat» = porque · «dus» = por eso. <span class="gloss">De vier valstrikken van deze unit.</span></li></ul></div>')
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> spelletjes met zelfcorrectie (imperativo, opinar, conectores…).</div>')
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td><b>advies geven</b> met de imperativo (come, haz, cuídate)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>een <b>pronomen aanplakken</b> (cuídate, hazlo)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>mijn <b>mening geven</b> (creo que… + indicativo)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>argumenteren</b> met porque/además/por eso</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>praten over <b>salud & medio ambiente</b></td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil para mí: <span class="wl md"></span> · Lo que quiero practicar más: <span class="wl md"></span></i></div>')
P('<div class="se" style="margin-top:6mm">Auto-test rápido · ¿lo sé?</div>')
P('<p style="margin-left:0">1. hacer → imperativo (tú) = <span class="wl sm"></span><br>'
  '2. cuidar + te = <span class="wl sm"></span><br>'
  '3. «ik denk dat het belangrijk is» = <span class="wl lg"></span><br>'
  '4. «want» / «omdat» = <span class="wl sm"></span><br>'
  '5. Geef één tip voor het milieu (imperativo): <span class="wl lg"></span></p>')
P('<div class="bridge"><b>🏁 ¡Fin de la ruta!</b> Has recorrido España, México, Colombia, Argentina, Perú y Costa Rica. Ya sabes hablar del presente, del pasado (perfecto, indefinido, imperfecto), dar consejos y <b>opinar</b>. ¡Enhorabuena, viajero/a! <span class="gloss">Einde van de reis: van het heden, over de verleden tijden, tot advies geven en je mening beargumenteren. Proficiat!</span></div>')
sec_close()

# ================= §V VOCABULARIO =================
VOC = json.load(open(f"{HERE}/u7_vocab.json", encoding="utf-8"))
GRP = [("salud","La salud"), ("consejos","Los consejos"), ("medioambiente","El medio ambiente"),
       ("imperativo","El imperativo (tú)"), ("opinar","Opinar"), ("conectores","Conectores")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (begrijpen en zelf gebruiken)")))
P('</div>')
P('<p style="font-size:9.6pt">Las palabras de la <b>salud</b> y el <b>medio ambiente</b> como red — tres familias:</p>')
P(clusters([
  ("💪","La salud",["sano · enfermo · el cuerpo","el deporte · la dieta","dormir · descansar"],"Gezond leven."),
  ("🌍","El planeta",["reciclar · la basura","ahorrar · la energía","proteger · el árbol"],"Het milieu."),
  ("💬","Opinar",["creo que · pienso que","en mi opinión","porque · además · por eso"],"Je mening geven."),
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
  '<p>Escribe la traducción. <span class="gloss">Schrijf de vertaling.</span> sano = <span class="wl md"></span> · reciclar = <span class="wl md"></span> · el consejo = <span class="wl md"></span> · además = <span class="wl md"></span></p>', apoyo="Modelo"))
P(actx("V.2", "Distinguir — sorteer per familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Clasifica: <span class="gloss">sorteer deze woorden</span> <span class="words"><b>el cuerpo · reciclar · dormir · la basura · el deporte · ahorrar · la dieta · proteger</b></span></p>'
  + sortcols([("salud",""),("medio ambiente","")], eigen=False), apoyo="Banco de palabras"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Completa la palabra; tienes la primera letra. <span class="gloss">de beginletter staat erbij</span> gezond = <b>s</b>___ · recyclen = <b>r</b>___ · ik denk dat = <b>c</b>___ que · daarom = <b>p</b>___ e___<br><span class="wl full"></span></p>', apoyo="Primera letra"))
P(actx("V.4", "Producir — un consejo con imperativo",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Escribe un consejo (imperativo) con <b>reciclar · el papel</b>. <span class="gloss">Eén advies in de gebiedende wijs.</span></p><div class="wbox sm"></div>', apoyo=""))
P(actx("V.5", "Comunicar — mi opinión en 3 frases",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Escribe tres frases sobre salud o medio ambiente (una opinión + un consejo + un conector) y dilas en voz alta. <span class="gloss">Drie zinnen; zeg ze daarna hardop.</span></p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>', apoyo="Marco: Creo que… porque… · Además… · Por eso…"))
P('<div class="se" style="margin-top:6mm">Mi cartel de la «pura vida» <span class="gloss" style="font-size:8pt">— teken een affiche en label 6 dingen in het Spaans</span></div>')
P('<div class="wbox lg"></div>')
P(mispal("Mis palabras de la unidad", 7))
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Sigue en la página digital:</span> <span class="g">flip cards (ES↔NL), audio en de spellen bouwen de steun verder af.</span></div></div>')
sec_close()

# ---------- OVERRIDE (bladspiegel-hygiëne) ----------
CSS_OVR = (' .act .steun{break-before:avoid;} '
           '.fams,.machine,.obsbox,.scale,.tree,.zoom,.fmu,.xray,.colloc,.clusters,.vpairs,.blocks,.agree,.mirror{break-inside:avoid;} '
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
   a.href=URL.createObjectURL(blob); a.download='C6plus_U7_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Más español en la práctica · C6+ U7 ¡Opina y cuídate!</title><style>'
        + CSS + CSS_OVR + RP.CSS + PB.CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/C6plus_U7.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes ·", _AN[0], "genummerde oefeningen (excl. V.1–V.5)")
