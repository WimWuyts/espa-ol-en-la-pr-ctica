#!/usr/bin/env python3
# C4 · Unidad 8 — §2 KIT + §4 GRAMÁTICA (functioneel) + §5 TAREA + §Suena bien.
# Thema: La hora y los días · ¿qué hora es? (es la una / son las…) · ¿a qué hora? · los días · quedar.
import base64, os
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

CLUSTERS=[
 ("¿Qué hora es?","de tijd zeggen","🕐",[
   ("¿Qué hora es?","Hoe laat is het?"),("Es la una","Het is één uur"),("Son las ocho","Het is acht uur"),
   ("y cuarto · y media","kwart over · half"),("menos cuarto","kwart voor"),("en punto","precies (op het uur)"),
 ]),
 ("Los días de la semana","de dagen","📅",[
   ("lunes · martes · miércoles","ma · di · wo"),("jueves · viernes","do · vr"),
   ("sábado · domingo","za · zo"),("el fin de semana","het weekend"),("hoy · mañana","vandaag · morgen"),
 ]),
 ("Los momentos del día","wanneer op de dag","🌗",[
   ("por la mañana","'s ochtends"),("por la tarde","'s middags/'s avonds"),("por la noche","'s nachts/'s avonds laat"),
   ("esta noche","vanavond"),("más tarde · ahora mismo","later · nu meteen"),("pronto · tarde","vroeg · laat"),
 ]),
 ("Quedar · afspreken","een afspraak maken","🤝",[
   ("¿Quieres quedar?","Wil je afspreken?"),("¿A qué hora?","Hoe laat?"),
   ("Quedamos a las…","We spreken af om…"),("¿Dónde quedamos?","Waar spreken we af?"),("Vale · perfecto","Oké · perfect"),
 ]),
 ("Por teléfono","aan de telefoon","📞",[
   ("¿Sí?","Ja? (opnemen)"),("No te oigo (nada)","Ik hoor je (helemaal) niet"),
   ("¿Puedes hablar más despacio?","Kan je langzamer spreken?"),("Hasta ahora","Tot straks"),("Un beso","Kusje (afscheid)"),
 ]),
]
def chunkcard(es,nl):
    return (f'<div class="cc" data-es="{es}"><span class="cc-es">{es}</span>'
            f'<span class="cc-nl">{nl}</span><button class="cc-spk" title="luister">🔊</button></div>')
def cluster(name,sub,ic,items):
    body="".join(chunkcard(*i) for i in items)
    return (f'<div class="clu"><div class="clu-h"><span class="clu-ic">{ic}</span>'
            f'<span><b>{name}</b><i>{sub}</i></span></div><div class="cc-grid">{body}</div></div>')
KIT="".join(cluster(*c) for c in CLUSTERS)

# visuele klok-rij (SVG-klokjes met de Spaanse benaming eronder)
def clock(h,m,label,nl):
    import math
    hx=50+26*math.sin(math.radians((h%12)*30+m*0.5)); hy=50-26*math.cos(math.radians((h%12)*30+m*0.5))
    mx=50+36*math.sin(math.radians(m*6)); my=50-36*math.cos(math.radians(m*6))
    return (f'<div class="clk" data-es="{label}"><svg viewBox="0 0 100 100" aria-label="{label}">'
            f'<circle cx="50" cy="50" r="46" fill="#fff" stroke="#E7E1DF" stroke-width="3"/>'
            f'<circle cx="50" cy="50" r="2.6" fill="#A8323B"/>'
            f'<line x1="50" y1="50" x2="{hx:.1f}" y2="{hy:.1f}" stroke="#20242E" stroke-width="4.6" stroke-linecap="round"/>'
            f'<line x1="50" y1="50" x2="{mx:.1f}" y2="{my:.1f}" stroke="#D64550" stroke-width="3.2" stroke-linecap="round"/>'
            f'</svg><b>{label}</b><i>{nl}</i></div>')
CLOCKS=[clock(1,0,"Es la una","1.00"),clock(3,15,"Son las tres y cuarto","3.15"),
        clock(8,30,"Son las ocho y media","8.30 · «half negen»!"),clock(6,45,"Son las siete menos cuarto","6.45 · kwart voor 7"),
        clock(12,0,"Son las doce en punto","12.00 precies"),clock(9,10,"Son las nueve y diez","9.10")]
RELOJES='<div class="clkrow">'+"".join(CLOCKS)+'</div>'

GRAM=r"""
<div class="note">
  <div class="note-h">🔎 <b>Fíjate</b> · Kijk terug naar de scène — je hoorde dit al:</div>
  <div class="obs">«<span class="t">¿Qué hora es?</span> ¿<span class="t">Las ocho y media</span>?» · «<span class="t">¿A qué hora?</span> No, <span class="t">a las once</span> no, mejor <span class="t">a las doce</span>.» · «¿<span class="v">Quieres quedar</span> esta noche? — <span class="v">Quedamos</span> en mi casa.»</div>
</div>

<div class="gcard">
  <h3><span class="t">¿Qué hora es?</span> — <i>es la una · son las dos</i></h3>
  <p class="gp">Eén uur is <b>enkelvoud</b>, alle andere uren <b>meervoud</b>:</p>
  <div class="mv">
    <div class="mv-c mv-m"><span class="mv-t">🕐 alleen 1 uur</span><span><b>Es la</b> una.</span><span><b>Es la</b> una y media.</span></div>
    <div class="mv-c mv-f"><span class="mv-t">🕑 alle andere uren</span><span><b>Son las</b> dos · tres · ocho…</span><span><b>Son las</b> doce en punto.</span></div>
  </div>
  <p class="ojo">⚠️ <b>¡Ojo, valstrik!</b> <span class="es">«<b>Half negen</b>» = <b>las ocho y media</b> (8 + 30). Het Spaans kijkt <b>terug</b> naar het vórige uur; het Nederlands kijkt <b>vooruit</b>. Dus: half tien = las nueve y media.</span></p>
</div>

<div class="gcard">
  <h3><span class="t">y cuarto · y media · menos cuarto</span></h3>
  <table class="gt">
    <tr><td class="t">Son las tres <b>y cuarto</b></td><td>3.15</td><td class="ex">kwart over drie</td></tr>
    <tr><td class="t">Son las tres <b>y media</b></td><td>3.30</td><td class="ex">half vier (!)</td></tr>
    <tr><td class="t">Son las cuatro <b>menos cuarto</b></td><td>3.45</td><td class="ex">kwart voor vier</td></tr>
    <tr><td class="t">Son las tres <b>en punto</b></td><td>3.00</td><td class="ex">precies drie uur</td></tr>
  </table>
  <p class="ojo">💡 <span class="es">Tot :30 gebruik je <b>y</b> (erbij), daarna <b>menos</b> (eraf) mét het <b>volgende</b> uur.</span></p>
</div>

<div class="gcard">
  <h3><span class="t">¿A qué hora?</span> — <i>a la una · a las doce</i></h3>
  <p class="gp">Voor een <b>afspraak</b> zet je <b>a</b> ervoor. Vergelijk goed:</p>
  <table class="gt">
    <tr><td class="t">Son las ocho.</td><td>Het <b>is</b> 8 u.</td><td class="ex">(hoe laat het nú is)</td></tr>
    <tr><td class="t">A las ocho.</td><td><b>Om</b> 8 u.</td><td class="ex">(wanneer iets gebeurt)</td></tr>
    <tr><td class="t">¿A qué hora quedamos?</td><td>Hoe laat spreken we af?</td><td class="ex">— A la una y media.</td></tr>
  </table>
</div>

<div class="gcard soft">
  <h3><span class="pl">el lunes · los lunes</span> — <i>de dagen</i></h3>
  <p class="gp">Dagen krijgen een <b>lidwoord</b>, géén «en»:</p>
  <table class="gt">
    <tr><td class="pl"><b>el</b> lunes</td><td>op maandag (deze ene)</td><td class="ex">El lunes quedamos a las seis.</td></tr>
    <tr><td class="pl"><b>los</b> lunes</td><td>elke maandag</td><td class="ex">Los lunes estudio español.</td></tr>
  </table>
  <p class="ojo">⚠️ <b>¡Ojo!</b> <span class="es">Zeg <b>el</b> lunes, niet <s>en lunes</s>. En dagen schrijf je met een <b>kleine letter</b>: lunes, martes, sábado…</span></p>
</div>
"""

TAREA=r"""
<div class="tcard">
  <div class="tmeta">
    <span><b>👤 Wie</b> jij → een klasgenoot</span>
    <span><b>🎯 Doel</b> je week tonen én een afspraak maken</span>
    <span><b>🗣️ Hoe</b> schema invullen + samen quedar</span>
    <span><b>✅ Resultaat</b> «Mi horario» + één afspraak</span>
  </div>
  <h3>Mi horario — <i>jouw week in het Spaans</i></h3>
  <ol class="pasos">
    <li><b>Rellena tu horario.</b> Vul voor <b>4 dagen</b> één activiteit in met dag + uur:
        <div class="frame">«<b>El</b> lunes <b>a las</b> ____ (hora) ____ (actividad).»</div></li>
    <li><b>Di la hora en voz alta.</b> Zeg elk uur hardop — let op «es la una» ↔ «son las…».</li>
    <li><b>Queda con un compañero.</b> Zoek samen een moment waarop jullie <b>beiden</b> vrij zijn:
        <div class="frame">«¿Quieres quedar el ____? — ¿A qué hora? — Quedamos a las ____.» · «Vale, ¡hasta ahora!»</div></li>
    <li><b>Presenta.</b> Vertel je week en jullie afspraak aan de klas — zónder af te lezen.</li>
  </ol>
  <div class="carne">
    <div class="carne-h">MI HORARIO · Academia «Welcome to Spanish»</div>
    <div class="carne-b diario">
      <div class="di-row"><span class="di-ic">📅</span><div class="di-lines">
        <div><span>El día:</span><i></i></div><div><span>A las…</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">🕐</span><div class="di-lines">
        <div><span>El día:</span><i></i></div><div><span>A las…</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">🤝</span><div class="di-lines">
        <div><span>Quedamos el:</span><i></i></div><div><span>A las…</span><i></i></div></div><span class="di-ok">☐</span></div>
    </div>
  </div>
  <p class="crit">🏁 <b>Klaar als…</b> je 4 momenten zegt met «el + dag» én «a las + uur» (juiste es la/son las), en samen een afspraak maakt met «¿quieres quedar?» — zónder af te lezen.</p>
</div>
"""

# §Suena bien · matrix A U8: la d (zacht/intervocalisch ↔ initiaal) + klemtoon in getallen (recycle c/qu U7)
DSUAVE=[("nada","niets"),("cada","elk(e)"),("media","half"),("sábado","zaterdag"),("quedar","afspreken"),("adiós","dag/tot ziens")]
DINIC=[("día","dag"),("dos","twee"),("doce","twaalf"),("domingo","zondag"),("después","daarna"),("despacio","langzaam")]
DISCRIM=[("dieciséis",1),("catorce",0),("veintidós",1),("cuarenta",0),("dieciocho",0),("veintitrés",1),("treinta",0),("veintiún",1)]
ACENTO=[("dieciséis","die·ci·<b>SÉIS</b>"),("veintidós","vein·ti·<b>DÓS</b>"),("catorce","ca·<b>TOR</b>·ce"),("cuarenta","cua·<b>REN</b>·ta")]
def jcard(w,nl):
    return (f'<div class="cc" data-es="{w}"><span class="cc-es">{w}</span>'
            f'<span class="cc-nl">{nl}</span><button class="cc-spk">🔊</button></div>')
def dchip(w,ok): return f'<button class="dchip" data-ok="{ok}" data-w="{w}">🔊 {w}</button>'
def acchip(w,html): return f'<button class="shchip" data-w="{w}">🔊 {html}</button>'
SUENA=('<div class="suena">'
 '<div class="sblok"><h3>① La d suave · tussen klinkers</h3>'
 '<p class="sh">Tussen klinkers (en op het einde) is de <b>d</b> <b>heel zacht</b>, bijna als de Engelse «th» in <i>this</i>: «na-da», «me-dia». Klik 🔊 en spreek na.</p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in DSUAVE)}</div></div>'
 '<div class="sblok"><h3>② La d inicial · steviger</h3>'
 '<p class="sh">Aan het begin van een woord is de <b>d</b> <b>steviger</b> (zoals in het Nederlands): «<b>d</b>ía», «<b>d</b>oce», «<b>d</b>omingo».</p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in DINIC)}</div>'
 '<p class="ojo2">⚠️ <b>¡Ojo!</b> <span>Zeg «me-<b>d</b>ia» héél zacht — niet als de harde NL «d» in «medisch». Vergelijk: <b>d</b>oce (stevig) ↔ na<b>d</b>a (zacht).</span></p></div>'
 '<div class="sblok"><h3>③ ¿Con tilde o sin tilde? · los números</h3>'
 '<p class="sh">Klik de getallen die <b>een accent</b> hebben (klemtoon op de láátste lettergreep; groen = juist). Klik 🔊 om te horen.</p>'
 f'<div class="shrow">{"".join(dchip(*d) for d in DISCRIM)}</div>'
 '<p class="sfb" id="dfb"></p></div>'
 '<div class="sblok"><h3>④ El acento en los números</h3>'
 '<p class="sh">Let op wáár de klemtoon valt bij getallen — dat helpt je de uren correct zeggen. Klik 🔊 en herhaal.</p>'
 f'<div class="shrow">{"".join(acchip(*a) for a in ACENTO)}</div></div>'
 '</div>')

CSS=FONTS+r"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--card:#fff;
--p:#2563EB;--v:#EA7317;--o:#1E9E74;--pl:#0E9E97;--t:#7C3AED;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#181513;--crema:#241C1B;--gt:#3A1E20;--line:#3a302e;--card:#211a19}
*{box-sizing:border-box}body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
.top{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;padding:22px}
.top h1{font-family:var(--disp);font-weight:800;margin:0;font-size:26px}.top p{margin:5px 0 0;opacity:.95;max-width:760px}
main{max-width:1000px;margin:0 auto;padding:18px}
.subh{font-family:var(--disp);color:var(--ink);font-size:20px;margin:30px 0 4px;padding-bottom:6px;border-bottom:2px solid var(--gt);display:flex;gap:10px;align-items:center}
.subh small{font-weight:400;color:var(--mut);font-size:13px;font-family:var(--body)}
.clu{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 16px;margin:14px 0}
.clu-h{display:flex;gap:10px;align-items:center;margin-bottom:10px}
.clu-ic{font-size:22px}.clu-h b{font-family:var(--disp);font-size:17px}.clu-h i{display:block;color:var(--mut);font-size:12.5px;font-style:normal}
.cc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:10px}
.cc-grid.tight{grid-template-columns:repeat(auto-fill,minmax(150px,1fr))}
.cc{position:relative;border:1.5px solid var(--line);border-left:4px solid var(--g);border-radius:12px;padding:9px 34px 9px 12px;cursor:pointer;background:var(--paper)}
.cc:hover{background:var(--gt)}
.cc-es{display:block;font-family:var(--disp);font-weight:700;font-size:15.5px}
.cc-nl{display:block;color:var(--mut);font-size:12.5px}
.cc-spk{position:absolute;right:8px;top:50%;transform:translateY(-50%);border:none;background:transparent;cursor:pointer;font-size:15px;opacity:.55}
.note{background:var(--gt);border-radius:14px;padding:12px 16px;margin:14px 0}
.note-h{font-weight:700;margin-bottom:4px}.obs{font-size:16px;font-family:var(--disp)}
.p{color:var(--p);font-weight:700}.v{color:var(--v);font-weight:700}.o{color:var(--o);font-weight:700}.pl{color:var(--pl);font-weight:700}.t{color:var(--t);font-weight:700}
.gcard{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:14px 0}
.gcard.soft{background:var(--crema)}
.gcard h3{font-family:var(--disp);margin:0 0 6px;font-size:18px}
.gp{margin:0 0 10px;font-size:14px;color:var(--ink)}
.gt{border-collapse:collapse;width:100%;font-size:14.5px}
.gt td{border-bottom:1px solid var(--line);padding:7px 10px}
.gt td.t{color:var(--t);font-weight:700;font-family:var(--disp)}.gt td.pl{color:var(--pl);font-weight:700;font-family:var(--disp)}.gt td.ex{color:var(--mut);font-style:italic}
.ojo{background:var(--gt);border-radius:10px;padding:9px 12px;font-size:13.5px;margin:12px 0 0}
.ojo .es{font-weight:600;color:var(--ink)}
.mv{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:8px 0}
.mv-c{border-radius:12px;padding:12px;display:flex;flex-direction:column;gap:4px;font-family:var(--disp);font-size:14.5px}
.mv-c b{color:var(--gd)}.mv-t{font-size:13px;font-weight:800;margin-bottom:4px}
.mv-m{background:#EDE9FE;color:#5B21B6}.mv-f{background:#E6F7F5;color:#0B7A73}
[data-theme=dark] .mv-m{background:#2a2145;color:#cdbcf7}[data-theme=dark] .mv-f{background:#123a37;color:#7fd8cf}
.clkrow{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:12px;margin:14px 0}
.clk{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:10px;text-align:center;cursor:pointer}
.clk:hover{background:var(--gt)}.clk svg{width:100%;max-width:78px;height:auto}
.clk b{display:block;font-family:var(--disp);font-size:12.5px;color:var(--gd);margin-top:4px;line-height:1.25}
.clk i{display:block;font-size:11px;color:var(--mut);font-style:normal}
[data-theme=dark] .clk svg circle[fill="#fff"]{fill:#2a2220}
.tcard{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:14px 0}
.tcard h3{font-family:var(--disp);font-size:19px;margin:8px 0 10px}
.tmeta{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px;background:var(--gt);border-radius:12px;padding:12px;font-size:13px}
.pasos{margin:6px 0 12px;padding-left:22px}.pasos li{margin:8px 0}
.frame{border:1.5px dashed var(--g);border-radius:10px;padding:8px 12px;margin:6px 0;font-family:var(--disp);color:var(--gd);background:var(--gt)}
.carne{max-width:460px;border:2px solid var(--g);border-radius:14px;overflow:hidden;margin:14px 0}
.carne-h{background:var(--g);color:#fff;font-family:var(--disp);font-weight:700;font-size:12.5px;padding:6px 12px}
.diario{display:flex;flex-direction:column;padding:6px 12px 12px}
.di-row{display:flex;gap:12px;align-items:center;padding:10px 0;border-bottom:1px solid var(--line)}
.di-row:last-child{border-bottom:none}
.di-ic{font-size:26px;flex:none}
.di-lines{flex:1;display:flex;flex-direction:column;gap:10px}
.di-lines div{display:flex;gap:8px;align-items:baseline}.di-lines span{font-size:12px;color:var(--mut);width:88px}
.di-lines i{flex:1;border-bottom:1.5px solid var(--line);height:15px}
.di-ok{font-size:20px;color:var(--mut);flex:none}
.crit{background:var(--crema);border-radius:10px;padding:10px 14px;font-size:13.5px;margin-top:10px}
.foot{color:var(--mut);font-size:12px;text-align:center;margin:26px 0}
.suena{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:760px){.suena{grid-template-columns:1fr}}
.sblok{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 16px}
.sblok h3{font-family:var(--disp);color:var(--gd);margin:0 0 4px;font-size:16px}
.sh{color:var(--mut);font-size:12.5px;margin:0 0 10px}
.ojo2{background:var(--gt);border-radius:10px;padding:8px 12px;font-size:12.5px;margin:10px 0 0}.ojo2 b{color:#DC2626}
.shrow{display:flex;flex-wrap:wrap;gap:8px}
.shchip,.dchip{border:1.5px solid var(--line);background:var(--paper);border-radius:20px;padding:8px 14px;font-weight:700;font-size:14px;cursor:pointer;font-family:var(--disp);color:var(--ink)}
.shchip:hover,.dchip:hover{background:var(--gt);border-color:var(--g)}
.dchip.ok{background:var(--g);color:#fff;border-color:var(--g)}
.dchip.no{background:#fde8e8;border-color:#DC2626;color:#DC2626;text-decoration:line-through}
.sfb{font-size:13px;color:var(--gd);font-weight:600;min-height:18px;margin:8px 0 0}
"""

HTML=f"""<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U8 · Kit · Gramática · Tarea</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 8 · La hora y los días</h1><p>De <b>kit de supervivencia</b> (de tijd zeggen, dagen &amp; afspreken), een korte <b>uitlegnota</b> waar het helpt, en je <b>eindtaak</b>. Klik 🔊 om woorden te horen.</p></div>
<main>
 <h2 class="subh">🔊 Suena bien <small>uitspraak — de zachte d &amp; de klemtoon in getallen</small></h2>
 {SUENA}
 <h2 class="subh">🕐 Los relojes <small>klik een klok om de tijd te horen</small></h2>
 {RELOJES}
 <h2 class="subh">§2 · Kit de supervivencia <small>de chunks per situatie — klik om te horen</small></h2>
 {KIT}
 <h2 class="subh">§4 · Gramática en la práctica <small>kort en functioneel — geen theorie om de theorie</small></h2>
 {GRAM}
 <h2 class="subh">§5 · Tarea final <small>jouw communicatieve opdracht</small></h2>
 {TAREA}
 <div class="foot">C4 · «Welcome to Spanish» · Unidad 8 · La hora y los días</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.cc').forEach(function(c){{var es=c.getAttribute('data-es').replace(/·.*/,'').replace(/[…?¿!¡]/g,'');c.onclick=function(){{speak(es);}};}});
document.querySelectorAll('.clk').forEach(function(c){{c.onclick=function(){{speak(c.getAttribute('data-es'));}};}});
document.querySelectorAll('.shchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));}};}});
var dtot=document.querySelectorAll('.dchip[data-ok="1"]').length;
document.querySelectorAll('.dchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));var ok=b.getAttribute('data-ok')==='1';b.classList.remove('ok','no');b.classList.add(ok?'ok':'no');var n=document.querySelectorAll('.dchip.ok').length;var fb=document.getElementById('dfb');fb.textContent=ok?('¡con tilde! klemtoon op de laatste · '+n+'/'+dtot+' 👏'):'Die heeft géén accent (klemtoon op de voorlaatste). Prueba otra.';}};}});
</script></body></html>"""
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U8_kgt.html","w").write(HTML)
print("C4_U8_kgt.html geschreven:",len(HTML),"bytes")
