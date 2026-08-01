#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de print-HTML C6plus_U6.html (C6+ · Unidad 6 «Cuando era pequeño») → PDF via Chromium.
# Zelfde componentenkit/CSS als de gelockte golden sample C6+·U0–U5 (geïmporteerd uit gen_u0_print).
# Cursuskleur = paars. Parada 6 = Cusco (Nina).
# Kerngrammatica: pretérito imperfecto · contraste indef./imperf. · comparativos + que.
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/01-cursussen/06-vervolg/U0")
import gen_u0_print as U0
from gen_u0_print import (CSS, AV, TU, MOCH, qr, audiorow, act, regla, guide, lpd, divider,
                          pcard, steun, sortcols, actx, tarea_com, obsbox, machine, blocks, tree,
                          mirror, fmu, scaffold, zoom, clusters, colloc, scale, vpairs, mispal, xray,
                          gustobars, menu)
import sys as _sys
_sys.path.insert(0, "/home/user/espa-ol-en-la-pr-ctica/03-build/web")
import print_bloques as PB
import lectura_data as LD
import escucha_data as ED

BODY = []
def P(*x): BODY.extend(x)
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
  <div class="tab">U6 · CUANDO ERA PEQUEÑO</div>
  <div class="eyebrow">UNIDAD 6 · LA RUTA · CUSCO 🇵🇪 · CUANDO ERA PEQUEÑO 🧸</div>
  <h1>Cuando era pequeño</h1>
  <div class="sub">De reis komt hoog in de Andes aan, in <b>Cusco</b>, bij <b>Nina</b>. Je vertelt over je <b>jeugd</b> en <b>hoe het vroeger was</b> met de <b>pretérito imperfecto</b> (<b>era</b> un niño feliz, <b>tenía</b> un perro, <b>jugaba</b> en la calle, <b>iba</b> a la escuela a pie). Je leert het <b>contrast</b> met de indefinido en je <b>vergelijkt</b> vroeger met nu. <span class="gloss">De onvoltooid verleden tijd (imperfecto) voor gewoontes en beschrijving + het contrast met de indefinido + vergelijkingen.</span></div>
  <div class="q">¿Cómo era tu vida cuando eras pequeño/a? <span style="font-weight:400;opacity:.9">· Hoe was je leven toen je klein was?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U2 · Aquí vivo</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U3 · Conectados</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U4 · De viaje</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U5 · Érase una vez</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U6 · Cuando era pequeño</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U7 · Opina y cuídate</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 6 · Cusco 🇵🇪.</b> Con <b>Nina</b> subes a los <b>Andes</b>: la antigua capital inca, cerca de <b>Machu Picchu</b>. Nina cuenta cómo <b>era</b> su infancia en un pueblo de montaña. <span class="gloss">Bij Nina klim je de Andes in, naar de oude Inca-hoofdstad. Ze vertelt hoe haar jeugd in een bergdorp was.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> Todos tenemos <b>recuerdos</b> de la infancia. Aprendes a describir cómo <b>era</b> todo: <i>vivía en un pueblo, tenía una mascota, jugaba en el patio, iba a la escuela a pie</i>. Cuentas qué <b>pasó un día</b> (indefinido) mientras algo <b>pasaba</b> (imperfecto) y <b>comparas</b> antes con ahora. Al final: escribes <b>«Cuando era pequeño/a»</b>.
      <span class="gloss">Iedereen heeft jeugdherinneringen. Je leert beschrijven hoe alles was, het contrast tussen achtergrond en gebeurtenis, en vroeger met nu vergelijken.</span></div>
      <div class="ojo"><b>¡Ojo! — twee valstrikken meteen scherp:</b> ① Het <b>imperfecto</b> = <b>achtergrond, gewoontes en beschrijving</b> (jugaba <b>siempre</b>) tegenover de <b>indefinido</b> = <b>afgerond feit</b> (un día <b>jugué</b>). ② De <b>comparativo</b>: <b>más/menos … que</b>, <b>tan … como</b>; onregelmatig <b>mejor/peor/mayor/menor</b> (niet «más bueno»). <span class="gloss">imperfecto = achtergrond · indefinido = feit · mejor/peor i.p.v. «más bueno/malo».</span></div>
    </div>
    <div>
      <div class="se">La gente de la ruta</div>
      <div class="cast">
        <div class="pc"><div class="avw">{AV["diego"]}</div><div class="nm">Diego</div><div class="fr">CDMX 🇲🇽</div></div>
        <div class="pc"><div class="avw">{AV["valen"]}</div><div class="nm">Valen</div><div class="fr">Cartagena 🇨🇴</div></div>
        <div class="pc"><div class="avw">{AV["mateo"]}</div><div class="nm">Mateo</div><div class="fr">BsAs 🇦🇷</div></div>
        <div class="pc"><div class="avw">{AV["nina"]}</div><div class="nm">Nina</div><div class="fr">Cusco 🇵🇪</div></div>
        <div class="pc tu"><div class="avw">{TU}</div><div class="nm">Tú</div><div class="fr">Flandes 🇧🇪</div></div>
      </div>
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila de recuerdos</span><br><span class="gloss" style="font-size:8.5pt">Vul je rugzak met de herinneringswoorden: era, tenía, jugaba, iba, antes, más… que — alles om je jeugd te vertellen.</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">hablar de tu infancia</span> (de pequeño, los recuerdos) <span class="nl">over je jeugd praten</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar el imperfecto</span> (era, tenía, jugaba, iba) <span class="nl">het imperfecto gebruiken</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">contrastar</span> indefinido ↔ imperfecto (jugaba cuando… empezó) <span class="nl">achtergrond ↔ feit</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">comparar</span> con <b>más/menos… que · tan… como</b> <span class="nl">vergelijken</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar <b>que</b></span> (el niño <b>que</b> jugaba…) <span class="nl">betrekkelijke bijzin</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">crear tu <b>«Cuando era pequeño/a»</b></span> <span class="nl">jeugdverhaal (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>La infancia</span><span><b>§2</b>Imperfecto</span><span><b>§3</b>Contraste</span><span><b>§4</b>Comparativos</span><span><b>§5</b>Lectura</span><span><b>Taller</b>acentos</span><span><b>Cultura</b>La infancia</span><span><b>Tarea</b>Mi infancia</span><span><b>Repaso</b>Semáforo</span>
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
sec_open("0", "§0 · ¡Ponte al día!", 'We komen van de <b>indefinido</b> (U5: nació, ganó). Nu de <b>imperfecto</b>: geen afgerond feit, maar <b>hoe iets wás</b> (achtergrond, gewoonte). <span class="gloss">Van de afgeronde feiten (indefinido) naar de beschrijving/gewoontes van vroeger (imperfecto).</span>',
        lpd(("8","taalsysteem: indefinido → imperfecto"), ("7","woordenschat")))
P('<div class="truc"><b>Indefinido ↔ imperfecto:</b> <b>Ayer jugué</b> (één afgerond feit) tegenover <b>De pequeño jugaba siempre</b> (gewoonte, achtergrond). In U6 draait alles om <b>hoe het vroeger was</b> → imperfecto.</div>')
P(actx(AN(), "¿acción única o costumbre? (repaso)",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>onderscheiden.</i> Is het een <b>afgerond feit</b> (indefinido) of een <b>gewoonte/achtergrond</b> (imperfecto)? Vink aan.</p>'
  '<p style="margin-left:12.5mm">1. Ayer fui al cine. → <span class="wl sm"></span> &nbsp; 2. De pequeño iba al parque cada día. → <span class="wl sm"></span><br>'
  '3. En 2019 ganó un premio. → <span class="wl sm"></span> &nbsp; 4. Cuando era niña vivía en Cusco. → <span class="wl sm"></span></p>',
  apoyo="PISTA (afgerond feit → indefinido · gewoonte/achtergrond → imperfecto)"))
P(actx(AN(), "Mi último recuerdo · escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>opstap.</i> Schrijf 2 dingen die je <b>vroeger vaak</b> deed (probeer «-aba / -ía»; we oefenen ze zo).</p>'
  '<p style="margin-left:12.5mm">De pequeño/a <span class="wl lg"></span><br>Todos los días <span class="wl lg"></span></p>',
  apoyo="MARCO"))
sec_close()

# ================= §1 · LA INFANCIA =================
sec_open("1", "§1 · La infancia", 'Het vocabulaire van de <b>jeugd</b>: de <b>herinneringen</b> (el recuerdo, de pequeño), de <b>school</b> (el patio, la maestra, el recreo) en de <b>familie van vroeger</b> (los abuelos, el pueblo, la mascota). <span class="gloss">De woorden van de kindertijd: herinneringen, school en familie.</span>',
        lpd(("7","woordenschat: la infancia"), ("5","identiteit: recuerdos")))
P('<div class="se">Los recuerdos de la infancia <span class="gloss" style="font-size:8pt">— netwerk in clusters</span></div>')
P('<div class="clusters" style="grid-template-columns:1fr 1fr 1fr">'
  '<div class="clu"><div class="ch"><span class="ci">🧸</span>La infancia</div><ul><li>de pequeño · el recuerdo</li><li>el juguete · jugar</li><li>soñar · pasarlo bien</li></ul><div class="ex">De pequeña jugaba mucho.</div></div>'
  '<div class="clu"><div class="ch"><span class="ci">🏫</span>La escuela</div><ul><li>la escuela · el patio</li><li>la maestra · el recreo</li><li>aprender · el compañero</li></ul><div class="ex">Iba a la escuela a pie.</div></div>'
  '<div class="clu"><div class="ch"><span class="ci">👵</span>La familia</div><ul><li>los abuelos · el pueblo</li><li>la casa de campo</li><li>la mascota · el vecino</li></ul><div class="ex">Visitaba a mis abuelos.</div></div></div>')
P('<div class="truc"><b>Tegenstellingen antes ↔ ahora:</b> <b>antes</b> (vroeger) ↔ <b>ahora</b> (nu) · <b>ya no</b> (niet meer) ↔ <b>todavía</b> (nog steeds) · <b>siempre / a menudo / todos los días</b> (gewoonte-markers → imperfecto).</div>')
P(actx(AN(), "Relaciona la palabra con el grupo",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>matching.</i> Verbind (schrijf de letter).</p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Palabra</div><div class="cb short">1. el patio &nbsp; 2. el juguete &nbsp; 3. los abuelos &nbsp; 4. la maestra</div></div>'
  '<div class="wcol"><div class="ch">Grupo</div><div class="cb short">a. la infancia &nbsp; b. la familia &nbsp; c. la escuela (persona) &nbsp; d. la escuela (lugar)</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo="SIN AYUDA"))
P(actx(AN(), "Clasifica: ¿infancia, escuela o familia?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>sorteren.</i> Zet elk woord in de juiste kolom: <span class="words"><b>el recuerdo · el recreo · los abuelos · el juguete · la maestra · la mascota · jugar · el pueblo</b></span></p>'
  + sortcols([("La infancia",""),("La escuela",""),("La familia","")], eigen=True), apoyo="BANCO"))
P(actx(AN(), "Antes ↔ ahora · empareja",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★★☆"}],
  '<p><i>tegenstellingsparen.</i> Verbind het paar.</p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">—</div><div class="cb short">1. antes &nbsp; 2. ya no &nbsp; 3. a menudo &nbsp; 4. feliz</div></div>'
  '<div class="wcol"><div class="ch">—</div><div class="cb short">a. todavía &nbsp; b. ahora &nbsp; c. triste &nbsp; d. casi nunca</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo="SIN AYUDA"))
P(actx(AN(), "Mi infancia · escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>gestuurd produceren.</i> Schrijf 3 zinnen over je jeugd (waar je woonde, wat je speelde, wie je bezocht).</p>'
  '<p style="margin-left:12.5mm">De pequeño/a vivía en <span class="wl md"></span> y jugaba a <span class="wl md"></span><br>Visitaba a <span class="wl lg"></span></p>',
  apoyo="MARCO"))
sec_close()

# ================= §2 · EL IMPERFECTO =================
sec_open("2", "§2 · El pretérito imperfecto", 'Voor <b>gewoontes, achtergrond en beschrijving</b> in het verleden: het <b>imperfecto</b>. Regelmatig: -ar → <b>-aba</b>, -er/-ir → <b>-ía</b>. <i>Jugaba, comía, vivía.</i> Slechts <b>3 onregelmatige</b>: <b>era, iba, veía</b>. <span class="gloss">De onvoltooid verleden tijd — heel regelmatig, maar 3 uitzonderingen.</span>',
        lpd(("8","taalsysteem: imperfecto"), ("7","woordenschat: la infancia"), ("3","beschrijven")))

# §2.1 el sistema
P('<h3>§2.1 · Las formas — la máquina del imperfecto</h3>')
P(obsbox([
  'De pequeña, Nina <span class="hl">vivía</span> en un pueblo y <span class="hl">jugaba</span> en la calle.',
  '<span class="hl">Era</span> tímida y <span class="hl">tenía</span> un perro.',
  'Todos los días <span class="hl">iba</span> a la escuela a pie.',
], vragen='Hoe eindigen de -ar-werkwoorden? En de -er/-ir? En welke drie zijn anders? <span class="gloss">-ar → -aba · -er/-ir → -ía · era/iba/veía.</span>'))
P(machine([("-ar jugar","raíz jug-"),("+ -aba","jugaba")]))
P(machine([("-er/-ir comer","raíz com-"),("+ -ía","comía")]))
P(regla("Regla · imperfecto", '<table class="conj" style="margin-top:1mm"><thead><tr><th>Persona</th><th>-ar (jugar)</th><th>-er/-ir (comer/vivir)</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">jugaba</td><td class="v">comía / vivía</td></tr>'
  '<tr><td class="p">tú</td><td class="v">jugabas</td><td class="v">comías / vivías</td></tr>'
  '<tr><td class="p">él/ella</td><td class="v">jugaba</td><td class="v">comía / vivía</td></tr>'
  '<tr><td class="p">nosotros/as</td><td class="v">jugábamos</td><td class="v">comíamos / vivíamos</td></tr>'
  '<tr><td class="p">vosotros/as</td><td class="v">jugabais</td><td class="v">comíais / vivíais</td></tr>'
  '<tr><td class="p">ellos/ellas</td><td class="v">jugaban</td><td class="v">comían / vivían</td></tr></tbody></table>'
  '<p style="margin:2mm 0 0"><b>Sólo 3 irregulares:</b> <b>ser</b> → era/eras/era/éramos/erais/eran · <b>ir</b> → iba/ibas/iba/íbamos/ibais/iban · <b>ver</b> → veía/veías/veía… <span class="gloss">🔴 yo = él/ella (jugaba, comía). Let op de <b>accent</b> op -ía.</span></p>'))
P(actx(AN(), "Forma el imperfecto",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>vorm de yo/él-vorm.</i></p>'
  '<p style="margin-left:12.5mm">jugar → <span class="wl sm"></span> &nbsp; comer → <span class="wl sm"></span> &nbsp; vivir → <span class="wl sm"></span><br>'
  'ser → <span class="wl sm"></span> &nbsp; ir → <span class="wl sm"></span> &nbsp; tener → <span class="wl sm"></span></p>',
  apoyo="MODELO (-aba / -ía; era/iba)"))
P(actx(AN(), "La gran cloze · imperfecto (la infancia)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>de verplichte werkwoord-cloze.</i> Vul het <b>imperfecto</b> in (infinitivo tussen haakjes).</p>'
  '<p style="margin-left:12.5mm">1. De pequeña, Nina <span class="wl md"></span> (vivir) en un pueblo. &nbsp; 2. <span class="wl md"></span> (ser) muy tímida.<br>'
  '3. Todos los días <span class="wl md"></span> (ir) a la escuela. &nbsp; 4. <span class="wl md"></span> (tener) un perro.<br>'
  '5. (Yo) <span class="wl md"></span> (jugar) en el patio. &nbsp; 6. Nosotros <span class="wl md"></span> (comer) en casa de la abuela.<br>'
  '7. Por la tarde <span class="wl md"></span> (ver, yo) dibujos. &nbsp; 8. Mis amigos <span class="wl md"></span> (soñar) con ser futbolistas.</p>',
  apoyo="BANCO: vivía · era · iba · tenía · jugaba · comíamos · veía · soñaban"))
P(actx(AN(), "Del presente al imperfecto · transforma",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>transformatie.</i> Herschrijf naar het imperfecto (antes / de pequeño).</p>'
  '<p style="margin-left:12.5mm">1. Vivo en la ciudad. → Antes <span class="wl md"></span><br>'
  '2. Voy al parque. → De pequeño <span class="wl md"></span><br>'
  '3. Soy tímido. → De niño <span class="wl md"></span></p>',
  apoyo="LETRA (vivía · iba · era)"))
P('</div>')

# §2.2 practicar cloze + sustitución
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2.2 · Más práctica del imperfecto</span>')
P('<div class="intro"><b>ES:</b> Seguimos: cambiar la persona y describir cómo era todo. <span class="gloss">Van persoon wisselen en beschrijven hoe alles was.</span></div>')
P('</div>')
P(actx(AN(), "Sustitución · cambia la persona",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>substitutietabel.</i> Model: <b>Yo jugaba y comía en casa.</b> Herschrijf per persoon.</p>'
  '<p style="margin-left:12.5mm">tú → <span class="wl md"></span> &nbsp; ella → <span class="wl md"></span> &nbsp; nosotros → <span class="wl md"></span> &nbsp; ellos → <span class="wl md"></span></p>',
  apoyo="LETRA (jugabas y comías…)"))
P(actx(AN(), "¿Cómo era? · describe con imperfecto",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>gestuurd → vrij.</i> Beschrijf hoe deze dingen vroeger waren (imperfecto).</p>'
  '<p style="margin-left:12.5mm">1. Mi pueblo (ser) → <span class="wl md"></span><br>'
  '2. Mi escuela (tener) → <span class="wl md"></span><br>'
  '3. Mis abuelos (vivir) → <span class="wl md"></span></p>',
  apoyo="MARCO (era… / tenía… / vivían…)"))
P(actx(AN(), "Clínica de errores · imperfecto",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 3 min"},{"t":"★★★"}],
  '<p><i>foutenkliniek.</i> Elke zin heeft één fout (vorm of accent). Verbeter.</p>'
  '<p style="margin-left:12.5mm">1. De pequeño yo jugava mucho. → <span class="wl md"></span><br>'
  '2. Nosotros comiamos en casa. → <span class="wl md"></span><br>'
  '3. Ella era tímida y tení un perro. → <span class="wl md"></span><br>'
  '4. Todos los días iva a la escuela. → <span class="wl md"></span></p>',
  apoyo="PISTA (jugaba · comíamos · tenía · iba)"))
P('</div>')

# §2.3 aplicar + tarea com
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2.3 · ¿Cómo era tu vida?</span>')
P('<div class="intro"><b>ES:</b> Aplicamos: describe tu propia infancia y compárala con la de un compañero. <span class="gloss">We passen toe: beschrijf je eigen jeugd.</span></div>')
P('</div>')
P(actx(AN(), "Mi vida de pequeño/a · la ficha",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>informatiekader.</i> Vul in met het imperfecto.</p>'
  '<table class="alf"><thead><tr><th>—</th><th>Cuando era pequeño/a</th></tr></thead><tbody>'
  '<tr><td>¿Dónde vivías?</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>¿Qué te gustaba hacer?</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>¿Cómo eras?</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>¿A quién veías a menudo?</td><td><span class="wl lg"></span></td></tr></tbody></table>',
  apoyo="MARCO"))
P(actx("★", "Tarea comunicativa · ¿cómo era tu infancia?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p><i>afzender·ontvanger·doel·situatie·resultaat.</i> Vraag je buur hoe zijn jeugd was (¿cómo era tu infancia?) en antwoord met het <b>imperfecto</b>. Noteer 2 dingen.</p>'
  '<p style="margin-left:12.5mm">— ¿Cómo era tu infancia? — <span class="wl lg"></span></p>'
  '<p style="margin-left:12.5mm">Mi compañero/a: 1. <span class="wl full"></span>2. <span class="wl full"></span></p>',
  apoyo="MARCO"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha «¿Cómo era tu infancia?»</b> en la web (TTS): Nina describe su niñez. <b>1ª vez:</b> ¿dónde vivía? · <b>2ª vez:</b> ¿qué hacía? Escribe los datos.</div>',
           qr("Escanea y escucha", "§2 · ¿Cómo era tu infancia?", seed=601)))
P('</div>')

# ================= §3 · CONTRASTE INDEF/IMPERF =================
sec_open("3", "§3 · Contraste — indefinido ↔ imperfecto", 'In een verhaal werken de twee verleden tijden <b>samen</b>: het <b>imperfecto</b> geeft de <b>achtergrond</b> (wat er al aan de gang was), de <b>indefinido</b> geeft de <b>gebeurtenis</b> (wat er toen gebeurde). <i>Jugaba en el patio cuando, de repente, empezó a llover.</i> <span class="gloss">imperfecto = decor/achtergrond · indefinido = de gebeurtenis die het verhaal vooruitduwt.</span>',
        lpd(("8","taalsysteem: contraste indef./imperf."), ("3","vertellen")))

# §3.1 el sistema
P('<h3>§3.1 · ¿Fondo o acción?</h3>')
P(obsbox([
  '<span class="hl">Era</span> de noche y <span class="hl">llovía</span>. (fondo) &nbsp;→&nbsp; De repente, <span class="hl">sonó</span> el teléfono. (acción)',
  'Nina <span class="hl">jugaba</span> en el patio cuando <span class="hl">llegó</span> su abuela.',
], vragen='Wat is de achtergrond (hoe het wás) en wat is de gebeurtenis (wat er toen gebeurde)? <span class="gloss">imperfecto = achtergrond · indefinido = feit.</span>'))
P(tree([
  '<b>¿Qué expresa el verbo?</b>',
  '¿achtergrond / decor / gewoonte / beschrijving? → <span class="yes">imperfecto</span> <span class="res">era, llovía, jugaba</span>',
  '¿afgeronde gebeurtenis / plotse actie? → <span class="yes">indefinido</span> <span class="res">sonó, llegó, empezó</span>',
]))
P(regla("Regla · imperfecto + indefinido", '<p><b>Imperfecto</b> = het decor: hoe alles <b>was</b>, wat al <b>bezig</b> was, <b>gewoontes</b> (era, tenía, llovía, jugaba). Markers: <i>siempre, a menudo, todos los días, mientras</i>.<br>'
  '<b>Indefinido</b> = de <b>gebeurtenis</b> die toen plaatsvond en het verhaal vooruitduwt (llegó, empezó, sonó). Markers: <i>un día, de repente, entonces</i>.<br>'
  '<span class="gloss">Vaak samen: <i>Jugaba (imperf.) cuando, de repente, empezó (indef.) a llover.</i></span></p>'))
P(actx(AN(), "Clasifica: ¿indefinido o imperfecto?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>onderscheiden.</i> Welke tijd hoort erbij? <span class="words"><b>Era de noche · sonó el teléfono · llovía · llegó mi abuela · siempre jugaba · un día empezó</b></span></p>'
  + sortcols([("imperfecto (achtergrond)",""),("indefinido (gebeurtenis)","")], eigen=False), apoyo="BANCO"))
P(actx(AN(), "Completa el relato · indef/imperf",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p><i>cloze contrast.</i> Vul in: imperfecto (achtergrond) of indefinido (gebeurtenis)?</p>'
  '<p style="margin-left:12.5mm">1. (Yo) <span class="wl md"></span> (jugar) en el patio cuando <span class="wl md"></span> (llegar) mi madre.<br>'
  '2. <span class="wl md"></span> (ser) de noche y <span class="wl md"></span> (empezar) a llover.<br>'
  '3. Nina <span class="wl md"></span> (vivir) en Cusco cuando <span class="wl md"></span> (nacer) su hermano.</p>',
  apoyo="PISTA (jugaba/llegó · era/empezó · vivía/nació)"))
P('</div>')

# §3.2 practicar + tarea com
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3.2 · Practicar el contraste</span>')
P('<div class="intro"><b>ES:</b> Entrenamos con corrección y una historia propia. <span class="gloss">Verbeteren en een eigen verhaaltje.</span></div>')
P('</div>')
P(actx(AN(), "Clínica de errores · contraste",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 3 min"},{"t":"★★★"}],
  '<p><i>foutenkliniek.</i> Kies de juiste tijd (achtergrond of feit). Verbeter.</p>'
  '<p style="margin-left:12.5mm">1. Ayer jugaba al fútbol y ganamos. → <span class="wl md"></span><br>'
  '2. Cuando era niño, un día fui al circo. (¿cuál es el fondo?) → <span class="wl md"></span><br>'
  '3. Llovió mientras yo estudiaba. → <span class="wl md"></span> (¿correcto?)</p>',
  apoyo="PISTA (jugaba → jugué? nee: het spel als achtergrond kan; kies logisch)"))
P(actx("★", "Tarea comunicativa · un recuerdo",
  [{"t":"🗣️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p><i>vertel een herinnering.</i> Vertel een klein voorval uit je jeugd: zet het <b>decor</b> (imperfecto) en de <b>gebeurtenis</b> (indefinido). Noteer je verhaal in 3 zinnen.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>',
  apoyo="MARCO (Era… / Tenía… cuando, de repente, … pasó)"))
P('<div class="guide"><div class="ic">🎡</div><div><span class="hand">Online:</span> <span class="g">de <b>contrast-beslisboom</b> en de spellen op de hub oefenen indef/imperf; + cloze en foutenkliniek.</span></div></div>')
P('</div>')

# ================= §4 · COMPARATIVOS =================
sec_open("4", "§4 · Comparativos + que", 'Om te <b>vergelijken</b>: <b>más … que</b> (meer dan), <b>menos … que</b> (minder dan), <b>tan … como</b> (even … als). Onregelmatig: <b>mejor/peor/mayor/menor</b>. En de <b>betrekkelijke que</b>: <i>el niño que jugaba…</i> <span class="gloss">Vergelijkingen + de betrekkelijke bijzin met que.</span>',
        lpd(("8","taalsysteem: comparativos + que"), ("7","woordenschat")))

# §4.1 el sistema
P('<h3>§4.1 · Comparar más / menos / tan</h3>')
P(obsbox([
  'Antes el pueblo <span class="hl">era más tranquilo que</span> la ciudad.',
  'Mi hermano <span class="hl">es tan alto como</span> yo.',
  'Este libro <span class="hl">es mejor que</span> ese.',
], vragen='Welk woordje komt na «más/menos» en welk na «tan»? <span class="gloss">más/menos … que · tan … como.</span>'))
P('<div class="fams three" style="margin-top:2mm">'
  '<div class="pcard"><div class="t">más … que</div><div class="ej">meer/-er dan: más alto que</div></div>'
  '<div class="pcard"><div class="t">menos … que</div><div class="ej">minder dan: menos caro que</div></div>'
  '<div class="pcard"><div class="t">tan … como</div><div class="ej">even … als: tan alto como</div></div></div>')
P('<div class="truc"><b>¡Ojo! irregulares:</b> niet «más bueno/malo» maar <b>mejor</b> (beter) / <b>peor</b> (slechter); niet «más viejo/joven» (voor personen) maar <b>mayor</b> (ouder) / <b>menor</b> (jonger). Superlativo: <b>el/la más …</b> (de meeste): «el más rápido de la clase».</div>')
P(actx(AN(), "Completa con más / menos / tan … que/como",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>gap-fill.</i> Vul de vergelijking aan.</p>'
  '<p style="margin-left:12.5mm">1. La ciudad es <span class="wl sm"></span> grande <span class="wl sm"></span> el pueblo (groter).<br>'
  '2. Antes yo era <span class="wl sm"></span> tímido <span class="wl sm"></span> ahora (minder).<br>'
  '3. Mi hermano es <span class="wl sm"></span> alto <span class="wl sm"></span> yo (even).<br>'
  '4. Hoy hace <span class="wl sm"></span> calor <span class="wl sm"></span> ayer (meer).</p>',
  apoyo="PISTA (más…que · menos…que · tan…como · más…que)"))
P(actx(AN(), "Los irregulares · elige",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>kies de juiste onregelmatige comparativo.</i></p>'
  '<p style="margin-left:12.5mm">1. Este libro es (bueno) <span class="wl sm"></span> que ese. &nbsp; 2. Hoy es (malo) <span class="wl sm"></span> que ayer.<br>'
  '3. Mi hermana es (viejo) <span class="wl sm"></span> que yo. &nbsp; 4. Soy (joven) <span class="wl sm"></span> que mi primo.</p>',
  apoyo="BANCO (mejor · peor · mayor · menor)"))
P(actx(AN(), "Traduce · la comparación",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>vertalen (NL → ES).</i></p>'
  '<p style="margin-left:12.5mm">1. De stad is groter dan het dorp. → <span class="wl lg"></span><br>'
  '2. Ik ben even oud als jij. → <span class="wl md"></span><br>'
  '3. Dit is beter dan dat. → <span class="wl md"></span></p>',
  apoyo="MARCO (más… que · tan… como · mejor que)"))
P('</div>')

# §4.2 relativo que + antes/ahora
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4.2 · La frase con «que» + antes/ahora</span>')
P('<div class="intro"><b>ES:</b> Met <b>que</b> koppel je twee zinnen: «el niño <b>que</b> jugaba en el patio era yo». En je vergelijkt <b>antes ↔ ahora</b>. <span class="gloss">De betrekkelijke que + vroeger/nu vergelijken.</span></div>')
P('</div>')
P('<div class="agree"><div class="w">La casa. La casa era grande. → La casa <u>que</u> era grande…</div><div class="tie">que = die/dat</div></div>')
P('<div class="agree"><div class="w">El lugar. Yo crecí allí. → El lugar <u>donde</u> crecí…</div><div class="tie">donde = waar</div></div>')
P(actx(AN(), "Une las frases con que / donde",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>koppelen.</i> Verbind de twee zinnen met <b>que</b> of <b>donde</b>.</p>'
  '<p style="margin-left:12.5mm">1. El niño. El niño jugaba en la calle. → <span class="wl lg"></span><br>'
  '2. La escuela. Yo estudiaba en la escuela. → <span class="wl lg"></span><br>'
  '3. El perro. El perro tenía manchas. → <span class="wl md"></span></p>',
  apoyo="LETRA (El niño que… · La escuela donde…)"))
P(actx(AN(), "Antes ↔ ahora · compara",
  [{"t":"✍️ Escribir","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p><i>vergelijking + imperfecto.</i> Schrijf 3 vergelijkingen tussen <b>vroeger</b> (imperfecto) en <b>nu</b> (presente).</p>'
  '<p style="margin-left:12.5mm">1. Antes <span class="wl md"></span>, ahora <span class="wl md"></span> (más…que).<br>'
  '2. Antes <span class="wl md"></span>, pero ahora ya no.<br>'
  '3. Antes <span class="wl md"></span>, y todavía <span class="wl md"></span></p>',
  apoyo="MARCO"))
P('</div>')

# ================= §5 · LECTURA =================
sec_open("5", "§5 · Lectura — «El pueblo de mi abuela»", 'Dos personas beschrijven hun jeugd. Lee, busca información y reacciona. <span class="gloss">Twee mensen beschrijven hun kindertijd. Lezen, info zoeken, reageren.</span>',
        lpd(("1","lezen: hoofdgedachte"), ("2","lezen: info selecteren"), ("5","identiteit & cultuur")))
P('<div class="lecdoel"><b>Antes de leer:</b> mira el título. ¿Cómo era la vida «antes», crees? <span class="gloss">Hoe was het leven vroeger, denk je?</span></div>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> recuerdo / relato</span><span class="tm"><b>Fuente:</b> muro de clase</span><span class="tm"><b>Objetivo:</b> compartir la infancia</span></div>')
P(f'<div class="ptexts">'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["nina"]}</div><div><div class="nm">Nina</div><div class="fr">Cusco 🇵🇪</div></div></div>'
  f'<p>De pequeña <span class="evi">vivía</span> en un pueblo cerca de Cusco. La casa de mi abuela <span class="evi">era</span> de adobe y <span class="evi">tenía</span> un patio grande. Todos los días <span class="evi">iba</span> a la escuela a pie y <span class="evi">jugaba</span> con mis primos. <span class="evi">Había</span> menos coches y todo <span class="evi">era más tranquilo que</span> ahora. Un día, <span class="evi">llegó</span> mi tío de la ciudad con una bici y ¡fue una fiesta! Echo de menos esa época.</p></div>'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["diego"]}</div><div><div class="nm">Diego</div><div class="fr">CDMX 🇲🇽</div></div></div>'
  f'<p>Yo <span class="evi">crecí</span> en la ciudad. De niño <span class="evi">veía</span> mucha tele y <span class="evi">jugaba</span> a videojuegos. Mi barrio <span class="evi">era más ruidoso que</span> el de Nina. <span class="evi">Tenía</span> muchos amigos y <span class="evi">íbamos</span> al parque. Un día <span class="evi">gané</span> un concurso de dibujo en la escuela. Ahora todo es diferente, pero también me gusta.</p></div></div>')
P(actx(AN(), "Verdadero o falso — con prueba",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>juist/fout + bewijs.</i> Waar (V) of niet waar (F)? Onderstreep het bewijs.</p>'
  '<table class="alf"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba (cita)</th></tr></thead><tbody>'
  '<tr><td>Nina vivía en un pueblo cerca de Cusco.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Para Nina, todo era más ruidoso que ahora.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Diego creció en la ciudad.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>',
  apoyo="MODELO"))
P(actx(AN(), "Escanea — completa la ficha",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>informatieraster.</i> Zoek en vul in.</p>'
  '<table class="alf"><thead><tr><th>—</th><th>Nina</th><th>Diego</th></tr></thead><tbody>'
  '<tr><td>¿Dónde vivía/crecía?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>¿Qué hacía (imperfecto)?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>¿Qué pasó un día (indefinido)?</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>',
  apoyo="SIN AYUDA"))
P(actx(AN(), "Reacciona — ¿y tú?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>productieve reactie.</i> ¿Tu infancia se parece más a la de Nina o a la de Diego? Schrijf 2–3 zinnen met het <b>imperfecto</b> + una comparación (más… que).</p>'
  '<div class="wbox sm"></div>',
  apoyo="MARCO (De pequeño/a yo… Mi vida era más… que…)"))
sec_close()

# ================= TALLER =================
sec_open("T", "Taller de lengua", 'Twee gereedschappen: de <b>acentos</b> in het imperfecto (-ía) en de <b>conectoren van vergelijking/contrast</b> (en cambio, mientras, sin embargo). <span class="gloss">De accenten en de contrast-connectoren.</span>')
P('<h3>1 · Ortografía — el acento en -ía</h3>')
P(regla("El acento del imperfecto", '<p>De -er/-ir-werkwoorden dragen in het imperfecto altijd een <b>accent</b> op de <b>í</b>: com<b>í</b>a, viv<b>í</b>a, ten<b>í</b>a, hac<b>í</b>a, ve<b>í</b>a. Ook nosotros -ábamos (jug<b>á</b>bamos).<br><span class="gloss">🔴 Zonder accent verandert de betekenis of klopt het niet: <i>tenia</i> → ten<b>í</b>a.</span></p>'))
P(actx(AN(), "¿Falta el acento? · corrige",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>plaats de accenten.</i> Schrijf correct: tenia · vivia · comiamos · veia · hacia · jugabamos</p>'
  '<p style="margin-left:12.5mm"><span class="wl full"></span></p>',
  apoyo="PISTA (tenía, vivía, comíamos, veía, hacía, jugábamos)"))
P('<h3 style="margin-top:6mm">2 · Conectores de contraste</h3>')
P(colloc("en cambio · mientras · sin embargo", ["antes… en cambio, ahora…","mientras = terwijl","sin embargo = echter","pero = maar"]))
P(actx(AN(), "Completa con el conector",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>gap-fill.</i> Vul aan met <b>en cambio · mientras · sin embargo</b>.</p>'
  '<p style="margin-left:12.5mm">1. Antes vivía en un pueblo; <span class="wl md"></span>, ahora vivo en la ciudad.<br>'
  '2. Jugaba en el patio <span class="wl md"></span> mis padres trabajaban.<br>'
  '3. Todo era más tranquilo; <span class="wl md"></span>, también más aburrido.</p>',
  apoyo="BANCO"))
sec_close()

# ================= §6 LECTURA · §7 ESCUCHA =================
# Zelfde bron als de digitale hub (lectura_data / escucha_data): papier en scherm
# kunnen zo niet uit elkaar lopen. Elk op een eigen bladzijde (§14).
P('<div class="page"><div class="parada sec">')
P('<span class="num">6</span><span class="pk">§6 · Lectura — «Carta de la abuela Rosario»</span>')
P('<div class="intro"><b>ES:</b> Una carta de verdad, escrita a mano por una abuela. <b>No hace falta entenderlo todo</b> para sacar la información. <span class="gloss">Een echte handgeschreven brief van een oma. Je hoeft niet alles te begrijpen — let op wat vroeger gewoonte was en wat één keer gebeurde.</span></div>')
P(PB.lectura_print(LD.C6P_U6, "1"))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">7</span><span class="pk">§7 · Escucha — «Pódcast «Antes y ahora»»</span>')
P('<div class="intro"><b>ES:</b> Dos invitados comparan su infancia en el pódcast del instituto. <b>Escucha primero, escribe después.</b> <span class="gloss">Twee gasten vergelijken hun kindertijd in de schoolpodcast. Eerst luisteren, dan schrijven; het transcript staat online en gaat pas open ná de taken.</span></div>')
P(PB.escucha_print(ED.C6P_U6, "1"))
P('</div>')

# ================= CULTURA =================
sec_open("C", "Cultura · la infancia en el mundo hispano", 'Elke cultuur heeft haar <b>kinderrituelen</b>: in Latijns-Amerika de <b>quinceañera</b> (15de verjaardag), traditionele <b>juegos</b> (la rayuela, el trompo) en de grote rol van de <b>abuelos</b>. In de Andes groeit Nina op met verhalen en muziek. <span class="gloss">De jeugd in de Spaanstalige wereld: quinceañera, traditionele spelletjes, de grootouders.</span>',
        lpd(("5","identiteit in diversiteit: la infancia hispana")))
P('<div class="fams three" style="margin-top:2mm">'
  '<div class="pcard"><div class="t">🎉 La quinceañera</div><div class="ej" style="margin-top:2mm">In veel Latijns-Amerikaanse landen viert een meisje haar <b>15de verjaardag</b> met een groot feest: de <b>quinceañera</b>. Het markeert de overgang van kind naar jongvolwassene.</div></div>'
  '<div class="pcard"><div class="t">🪀 Los juegos tradicionales</div><div class="ej" style="margin-top:2mm">Vroeger speelden kinderen <b>la rayuela</b> (hinkelen), <b>el trompo</b> (tol) en <b>las canicas</b> (knikkers) op straat. Nina «jugaba» ze allemaal in het dorp.</div></div>'
  '<div class="pcard"><div class="t">👵 Los abuelos</div><div class="ej" style="margin-top:2mm">In de hispanofoon spelen de <b>abuelos</b> een grote rol: ze passen op, vertellen verhalen en geven de <b>traditie</b> door. «Iba a casa de mi abuela» is een klassieke jeugdherinnering.</div></div></div>')
P('<div class="route-note" style="margin-top:5mm">🗺️ <b>En la web:</b> haz clic en Perú (★) en el mapa para descubrir Cusco y la infancia andina. <span class="gloss">Online: klik op Perú voor de familia-fiche.</span></div>')
P(actx(AN(), "Compara · tu infancia y la hispana",
  [{"t":"🌍 Cultura","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Vergelijk. Welke spelletjes speelde jij? Wat is anders/gelijk? Schrijf 2 zinnen met het <b>imperfecto</b> + una comparación.</p>'
  '<div class="wbox sm"></div>',
  apoyo="MARCO"))
P(actx(AN(), "Datos curiosos — une",
  [{"t":"🌍 Cultura","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>matching.</i> Verbind (schrijf de letter).</p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Elemento</div><div class="cb short">1. la quinceañera &nbsp; 2. la rayuela &nbsp; 3. los abuelos &nbsp; 4. el trompo</div></div>'
  '<div class="wcol"><div class="ch">Dato</div><div class="cb short">a. juego de calle (hinkelen) &nbsp; b. 15º cumpleaños &nbsp; c. juguete que gira (tol) &nbsp; d. transmiten la tradición</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span></p>',
  apoyo="BANCO"))
sec_close()

# ================= TAREA FINAL =================
sec_open("★", "Tarea final · «Cuando era pequeño/a»", 'Escribe un <b>recuerdo</b> de tu infancia met het <b>imperfecto</b>, een <b>vergelijking</b> antes/ahora en una <b>mini-mening</b>. <span class="gloss">Schrijf een jeugdherinnering met het imperfecto, een vergelijking en een mening.</span>')
P(fmu('tus compañeros de clase (el muro de recuerdos)', 'compartir tu infancia', 'un recuerdo (6–8 frases) + una presentación oral (± 1 min)'))
P('<ol class="pasos">'
  '<li><b>Describe cómo era todo</b> met het <b>imperfecto</b>: «De pequeño/a vivía en… tenía… jugaba…».</li>'
  '<li><b>Cuenta un día especial</b> (indefinido): «Un día, de repente,…».</li>'
  '<li><b>Compara</b> antes ↔ ahora: «Antes era más… que ahora».</li>'
  '<li><b>Añade tu opinión</b>: «Creo que antes era… porque…».</li>'
  '<li><b>Preséntalo en pareja</b> y <b>graba</b> tu recuerdo en la web. Escúchate y mejora.</li></ol>')
P('<div class="se" style="margin-top:4mm">Mi recuerdo <span class="gloss" style="font-size:8pt">· 6–8 zinnen</span></div><div class="wbox lg"></div>')
P('<div class="se" style="margin-top:3mm">Mi comparación y opinión <span class="gloss" style="font-size:8pt">· antes más… que ahora…</span></div><div class="wbox sm"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba tu recuerdo</b> en la web (recorder + rúbrica). Escucha, compara con el modelo y vuelve a grabar.</div>',
           qr("Escanea y graba", "Tarea · Cuando era pequeño", seed=670)))
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Ik gebruik het <b>imperfecto</b> correct (era, tenía, jugaba…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik het <b>contrast</b> met een indefinido (un día…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik maak minstens <b>één vergelijking</b> (más/menos/tan)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik geef <b>één mening</b> (creo que antes…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>presenteer vlot</b> (± 1 min)</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — la infancia de mi compañero/a</div>'
  '<table><thead><tr><th>Algo que teníamos en común</th><th>Una pregunta que le hago</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('<div class="truc" style="margin-top:3mm"><b>✍️ Antes de colgar:</b> lees je tekst na — <i>imperfecto correct? · een indefinido-feit? · una comparación? · una opinión?</i> Verbeter één ding: <span class="wl lg"></span></div>')
sec_close()

# ================= REPASO =================
sec_open("✓", "Repaso · lo esencial", 'Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag; de volledige herhaling staat online.</span>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>Imperfecto:</b> -ar → aba/abas/aba/ábamos/abais/aban · -er/-ir → ía/ías/ía/íamos/íais/ían.</li>'
  '<li><b>Sólo 3 irregulares:</b> ser → era · ir → iba · ver → veía.</li>'
  '<li><b>Contraste:</b> imperfecto = achtergrond/gewoonte (era, jugaba) · indefinido = gebeurtenis (llegó, empezó).</li>'
  '<li><b>Comparativos:</b> más/menos … que · tan … como · irr. mejor/peor/mayor/menor.</li>'
  '<li><b>Relativo:</b> que (die/dat) · donde (waar). El niño que jugaba…</li>'
  '<li><b>Las trampas:</b> 🔴 accent op -ía (tenía) · 🔴 imperf. ≠ indef. · 🔴 mejor (niet «más bueno»).</li></ul></div>')
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> spelletjes met zelfcorrectie (imperfecto, contraste, comparativos…).</div>')
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td>over mijn <b>jeugd</b> praten (recuerdos)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>het <b>imperfecto</b> vormen (era, tenía, jugaba)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>het <b>contrast</b> indefinido/imperfecto gebruiken</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>vergelijken met <b>más/menos/tan</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>zinnen koppelen met <b>que/donde</b></td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil para mí: <span class="wl md"></span> · Lo que quiero practicar más: <span class="wl md"></span></i></div>')
P('<div class="se" style="margin-top:6mm">Auto-test rápido · ¿lo sé?</div>')
P('<p style="margin-left:0">1. jugar → imperfecto (yo) = <span class="wl sm"></span><br>'
  '2. ser → imperfecto (él) = <span class="wl sm"></span><br>'
  '3. ir → imperfecto (yo) = <span class="wl sm"></span><br>'
  '4. «even groot als» = <span class="wl md"></span> grande <span class="wl sm"></span> yo<br>'
  '5. Beschrijf hoe je huis vroeger was (1 zin, imperfecto): <span class="wl lg"></span></p>')
P('<div class="bridge"><b>» Siguiente parada: U7 «¡Opina y cuídate!».</b> Ya describes el pasado; en la última unidad aprendes el <b>imperativo</b> (para dar consejos: cuídate, come sano) y a <b>opinar y argumentar</b> sobre la salud y el medio ambiente. ¡El último tramo! <span class="gloss">In U7: de imperativo (advies) + mening/argumentatie over gezondheid en milieu.</span></div>')
sec_close()

# ================= §V VOCABULARIO =================
VOC = json.load(open(f"{HERE}/u6_vocab.json", encoding="utf-8"))
GRP = [("infancia","La infancia"), ("escuela","La escuela"), ("familia","La familia · el pueblo"),
       ("imperfecto","El imperfecto"), ("antesahora","Antes ↔ ahora"),
       ("comparar","Comparativos"), ("relativo","Que / donde"), ("opinar","Opinar y recordar")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (receptief & productief)")))
P('</div>')
P('<p style="font-size:9.6pt">Las palabras de la <b>infancia</b> como red — tres familias:</p>')
P(clusters([
  ("🧸","La infancia",["de pequeño · el recuerdo","el juguete · jugar","la escuela · el patio"],"De kindertijd."),
  ("🔄","El imperfecto",["era · tenía · jugaba","iba · vivía · había","antes · siempre · a menudo"],"Hoe het vroeger was."),
  ("⚖️","Comparar",["más/menos … que","tan … como","mejor · peor · mayor"],"Vergelijken."),
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
  '<p>Schrijf de vertaling. de pequeño = <span class="wl md"></span> · era = <span class="wl md"></span> · el recreo = <span class="wl md"></span> · antes = <span class="wl md"></span></p>', apoyo="MODELO"))
P(actx("V.2", "Distinguir — sorteer per familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Sorteer: <span class="words"><b>el juguete · era · el patio · jugaba · los abuelos · tenía · la maestra · iba</b></span></p>'
  + sortcols([("sustantivo (infancia/escuela)",""),("forma imperfecto","")], eigen=False), apoyo="BANCO"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul aan (beginletter). als kind = <b>d</b>___ p___ · was = <b>e</b>___ · vroeger = <b>a</b>___ · beter dan = <b>m</b>___ que<br><span class="wl full"></span></p>', apoyo="LETRA INICIAL"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p><i>verplichte-woorden-zin.</i> Maak één correcte zin met <b>de pequeño · jugaba · el patio</b>.</p><div class="wbox sm"></div>', apoyo="SIN AYUDA"))
P(actx("V.5", "Comunicar — mi infancia en 3 frases",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>vrije productie → transfer.</i> Schrijf 3 zinnen over je jeugd (dónde vivías · qué hacías · una comparación) en zeg ze hardop.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>', apoyo="MARCO → SIN AYUDA"))
P('<div class="se" style="margin-top:6mm">Mi mapa de recuerdos <span class="gloss" style="font-size:8pt">— teken je jeugdplek en label 6 dingen in het Spaans</span></div>')
P('<div class="wbox lg"></div>')
P(mispal("Mis palabras de la unidad", 7))
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Sigue en la página digital:</span> <span class="g">flip cards (ES↔NL), audio en de spellen bouwen de steun verder af.</span></div></div>')
sec_close()

# ---------- OVERRIDE (bladspiegel-hygiëne) ----------
CSS_OVR = ('.act{break-inside:avoid;} .act .steun{break-before:avoid;} '
           '.fams,.machine,.obsbox,.scale,.tree,.zoom,.fmu,.xray,.colloc,.clusters,.vpairs,.blocks,.agree{break-inside:avoid;} '
           '.ptexts,.fichacard,.menu,.gustobars{break-inside:avoid;} '
           '.bridge,.guide,.route-note,.truc,.audiorow{break-before:avoid;} '
           '.esen{break-after:avoid;}')

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
   a.href=URL.createObjectURL(blob); a.download='C6plus_U6_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Español en la práctica · C6+ U6 Cuando era pequeño</title><style>'
        + CSS + CSS_OVR + PB.CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/C6plus_U6.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes ·", _AN[0], "genummerde oefeningen (excl. V.1–V.5)")
