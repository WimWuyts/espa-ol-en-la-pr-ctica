#!/usr/bin/env python3
# C4 · Unidad 9 — §2 KIT + §4 GRAMÁTICA (functioneel) + §5 TAREA + §Suena bien.
# Thema: Planes y obligaciones · ir a + infinitivo · tener que + infinitivo · tener + naamwoord · declinar.
import base64, os
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

CLUSTERS=[
 ("Los planes · voy a…","plannen maken","🗓️",[
   ("Voy a + infinitivo","Ik ga + werkwoord"),("Voy a preparar café","Ik ga koffie zetten"),
   ("Vamos a dormir","Laten we/We gaan slapen"),("¿Vamos a pasear?","Gaan we wandelen?"),
   ("¿Qué vas a hacer?","Wat ga je doen?"),
 ]),
 ("Las obligaciones · tengo que…","moeten","✅",[
   ("Tengo que + infinitivo","Ik moet + werkwoord"),("Tengo que trabajar","Ik moet werken"),
   ("Tengo que estudiar","Ik moet studeren"),("¿Tienes que hacer algo?","Moet je iets doen?"),
   ("Tengo cosas que hacer","Ik heb dingen te doen"),
 ]),
 ("Actividades del finde","weekendactiviteiten","🎉",[
   ("ir al cine","naar de cinema gaan"),("pasear al perro","de hond uitlaten"),
   ("quedar con amigos/as","afspreken met vrienden"),("ver una película","een film kijken"),
   ("jugar al fútbol","voetballen"),("tomar algo","iets gaan drinken"),
 ]),
 ("Con tener · geen «ser»!","tener + naamwoord","🙋",[
   ("Tengo hambre","Ik heb honger"),("Tengo sueño","Ik ben slaperig (lett. ik héb slaap)"),
   ("Tengo sed","Ik heb dorst"),("Tengo prisa","Ik heb haast"),
 ]),
 ("Aceptar o rechazar","ja of nee zeggen","🤷",[
   ("¡Vale! · ¡Perfecto!","Oké! · Perfect!"),("No puedo","Ik kan niet"),
   ("¡Qué pena!","Wat jammer!"),("Estoy libre","Ik ben vrij"),("Otro día, ¿vale?","Een andere dag, oké?"),
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

# visuele «bouwmachine»: [persona] + a/que + [infinitivo]  → interactieve zinbouwer
BUILD=r"""
<div class="builder">
  <div class="bh">🔧 <b>La máquina de frases</b> · construye tu propia frase: elige y pulsa. <span class="stn">bouw je eigen zin</span></div>
  <div class="brow">
    <div class="bcol"><span class="bl">1 · ¿plan of moeten?</span>
      <button class="bopt on" data-slot="0" data-v="Voy a">Voy a… <i>(plan)</i></button>
      <button class="bopt" data-slot="0" data-v="Tengo que">Tengo que… <i>(moeten)</i></button>
      <button class="bopt" data-slot="0" data-v="Vamos a">Vamos a… <i>(wij)</i></button>
    </div>
    <div class="bcol"><span class="bl">2 · el infinitivo</span>
      <button class="bopt on" data-slot="1" data-v="estudiar">estudiar</button>
      <button class="bopt" data-slot="1" data-v="trabajar">trabajar</button>
      <button class="bopt" data-slot="1" data-v="pasear al perro">pasear al perro</button>
      <button class="bopt" data-slot="1" data-v="ir al cine">ir al cine</button>
      <button class="bopt" data-slot="1" data-v="ver una película">ver una película</button>
    </div>
    <div class="bcol"><span class="bl">3 · ¿cuándo?</span>
      <button class="bopt on" data-slot="2" data-v="esta tarde">esta tarde</button>
      <button class="bopt" data-slot="2" data-v="esta noche">esta noche</button>
      <button class="bopt" data-slot="2" data-v="el sábado">el sábado</button>
      <button class="bopt" data-slot="2" data-v="el finde">el finde</button>
    </div>
  </div>
  <div class="bout" id="bout"></div>
  <p class="bhint">💡 Merk op: ná <b>voy a</b> / <b>tengo que</b> komt áltijd het <b>hele werkwoord</b> (infinitivo).</p>
</div>
"""

GRAM=r"""
<div class="note">
  <div class="note-h">🔎 <b>Fíjate</b> · vuelve a la escena: ya lo has oído. <span class="stn">je hoorde dit al</span></div>
  <div class="obs">«<span class="v">Voy a</span> preparar café.» · «<span class="v">Vamos a</span> dormir un poquito más.» · «<span class="v">Tengo que</span> pasear al perro.» · «<span class="v">Tengo</span> sueño.»</div>
</div>

<div class="gcard">
  <h3><span class="v">ir a</span> + infinitivo — <i>plannen: «ik ga…»</i></h3>
  <p class="gp">Para decir lo que <b>vas a hacer</b>: una forma de <b>ir</b> + <b>a</b> + <b>infinitivo</b>. <span class="stn">ir + a + het hele werkwoord</span></p>
  <table class="gt">
    <tr><td class="v">voy a</td><td>ik ga</td><td class="ex"><b>Voy a</b> preparar café.</td></tr>
    <tr><td class="v">vas a</td><td>jij gaat</td><td class="ex">¿Qué <b>vas a</b> hacer?</td></tr>
    <tr><td class="v">vamos a</td><td>we gaan / laten we</td><td class="ex"><b>Vamos a</b> dormir un poquito más.</td></tr>
  </table>
  <p class="ojo">💡 <span class="es">No olvides la <b>a</b>: voy <b>a</b> estudiar.</span> <span class="stn">net als «ik ga koffie zetten»</span></p>
</div>

<div class="gcard">
  <h3><span class="v">tener que</span> + infinitivo — <i>moeten</i></h3>
  <p class="gp">Para decir lo que <b>tienes que</b> hacer: <b>tengo que</b> / <b>tienes que</b> + infinitivo. <span class="stn">wat je moet doen</span></p>
  <table class="gt">
    <tr><td class="v">tengo que</td><td>ik moet</td><td class="ex"><b>Tengo que</b> trabajar.</td></tr>
    <tr><td class="v">tienes que</td><td>tú debes <span class="stn">jij moet</span></td><td class="ex">¿<b>Tienes que</b> hacer algo?</td></tr>
    <tr><td class="v">tiene que</td><td>hij/zij moet</td><td class="ex"><b>Tiene que</b> estudiar.</td></tr>
  </table>
  <p class="ojo">⚠️ <b>¡Ojo!</b> <span class="es">De <b>que</b> is verplicht: tengo <b>que</b> trabajar (niet <s>tengo trabajar</s>). Letterlijk: «ik héb te werken».</span></p>
</div>

<div class="gcard soft">
  <h3><span class="v">tener</span> + naamwoord — <i>hambre · sueño · sed · prisa</i></h3>
  <p class="gp">Aquí el español usa <b>tener</b> donde el neerlandés dice «zijn» o «hebben»: <span class="stn">Spaans «hebben» waar wij «zijn» zeggen</span></p>
  <div class="mv">
    <div class="mv-c mv-m"><span class="mv-t">✅ así lo dice el español</span><span><b>Tengo</b> hambre · <b>Tengo</b> sed</span><span><b>Tengo</b> sueño · <b>Tengo</b> prisa</span></div>
    <div class="mv-c mv-f"><span class="mv-t">🇳🇱 wat wij zeggen</span><span>Ik <b>heb</b> honger · dorst</span><span>Ik <b>ben</b> slaperig · <b>heb</b> haast</span></div>
  </div>
  <p class="ojo">⚠️ <b>¡Ojo!</b> <span class="es">Se dice <b>tengo sueño</b>, nunca <s>soy/estoy sueño</s>. Es la trampa de esta lección.</span> <span class="stn">«ik ben slaperig» = tengo sueño</span></p>
</div>

<div class="gcard">
  <h3>Rechazar con educación — <i>hoe María «nee» zegt</i></h3>
  <p class="gp">Een uitnodiging afwijzen doe je in twee stappen: <b>nee</b> + <b>reden</b>:</p>
  <div class="dial">
    <div class="db">— ¿Quedamos para ir al cine?</div>
    <div class="da">— <b>No puedo.</b> <b>Tengo que</b> pasear al perro.</div>
    <div class="db">— ¿Y mañana?</div>
    <div class="da">— <b>Tengo cosas que hacer.</b> Otro día, ¿vale?</div>
  </div>
  <p class="ojo">💡 <span class="es">Suavizantes útiles: <b>¡Qué pena!</b> · <b>Otro día, ¿vale?</b></span> <span class="stn">wat jammer · een andere dag, oké?</span></p>
</div>
"""

TAREA=r"""
<div class="tcard">
  <div class="tmeta">
    <span><b>👤 Quién</b> tú ↔ un compañero/a</span>
    <span><b>🎯 Objetivo</b> planear tu finde y rechazar una invitación</span>
    <span><b>🗣️ Cómo</b> rellenar la agenda y representar el diálogo</span>
    <span><b>✅ Resultado</b> «Mi finde» + 1 cita y 1 excusa</span>
  </div>
  <h3>Mi finde — <i>plannen, moeten… en beleefd «nee» zeggen</i></h3>
  <ol class="pasos">
    <li><b>Rellena tu finde.</b> Escribe <b>3 planes</b> (voy a…) y <b>2 obligaciones</b> (tengo que…): <span class="stn">drie plannen en twee verplichtingen</span>
        <div class="frame">«El sábado por la tarde <b>voy a</b> ____ .» · «El domingo <b>tengo que</b> ____ .»</div></li>
    <li><b>Invita a un compañero.</b> Invita a tu compañero/a a uno de tus planes: <span class="stn">nodig je buur uit</span>
        <div class="frame">«¿<b>Quedamos para</b> ____ el ____ ?» — «¿<b>Vamos a</b> ____ ?»</div></li>
    <li><b>Rechaza una vez.</b> Rechaza su invitación una vez con educación, con una <b>excusa de verdad</b>: <span class="stn">wijs één keer beleefd af</span>
        <div class="frame">«<b>No puedo.</b> <b>Tengo que</b> ____ . ¡Qué pena! Otro día, ¿vale?»</div></li>
    <li><b>Cerrad un plan.</b> Buscad juntos un momento que sí os vaya bien y quedad (día + hora). <span class="stn">vind tóch één moment en spreek af</span></li>
  </ol>
  <div class="carne">
    <div class="carne-h">MI FINDE · Academia «Bienvenidos al español»</div>
    <div class="carne-b diario">
      <div class="di-row"><span class="di-ic">🗓️</span><div class="di-lines">
        <div><span>Voy a…</span><i></i></div><div><span>¿Cuándo?</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">✅</span><div class="di-lines">
        <div><span>Tengo que…</span><i></i></div><div><span>¿Cuándo?</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">🤝</span><div class="di-lines">
        <div><span>Quedamos:</span><i></i></div><div><span>A las…</span><i></i></div></div><span class="di-ok">☐</span></div>
    </div>
  </div>
  <p class="crit">🏁 <b>Está listo cuando…</b> dices 3 planes con «voy a + infinitivo», 2 obligaciones con «tengo que + infinitivo», rechazas una invitación con educación («no puedo, tengo que…») y cerráis una cita, sin leer. <span class="stn">drie plannen, twee verplichtingen, één beleefde weigering</span></p>
</div>
"""

# §Suena bien · matrix A U9: diptongos ie/ue (+ tilde op de diptong). Recycle: d (U8), esdrújula (U7).
IEW=[("quiero","ik wil"),("tienes","jij hebt"),("bien","goed"),("siete","zeven"),("fiesta","feest"),("viernes","vrijdag")]
UEW=[("puedo","ik kan"),("bueno","goed"),("luego","later"),("fuera","buiten"),("juego","ik speel/spel"),("cuenta","rekening")]
DISCRIM=[("puedo",1),("quiero",0),("bueno",1),("tienes",0),("luego",1),("siete",0),("juego",1),("fiesta",0)]
ACENTO=[("adiós","a·<b>DIÓS</b>"),("después","des·<b>PUÉS</b>"),("también","tam·<b>BIÉN</b>"),("canción","can·<b>CIÓN</b>")]
def jcard(w,nl):
    return (f'<div class="cc" data-es="{w}"><span class="cc-es">{w}</span>'
            f'<span class="cc-nl">{nl}</span><button class="cc-spk">🔊</button></div>')
def dchip(w,ok): return f'<button class="dchip" data-ok="{ok}" data-w="{w}">🔊 {w}</button>'
def acchip(w,html): return f'<button class="shchip" data-w="{w}">🔊 {html}</button>'
SUENA=('<div class="suena">'
 '<div class="sblok"><h3>① El diptongo <i>ie</i> · één lettergreep</h3>'
 '<p class="sh">Dos vocales juntas = <b>una sola</b> sílaba (un <i>diptongo</i>). Di «qu<b>ie</b>-ro» en 2 partes, no en 3. Pulsa 🔊 y repite. <span class="gloss">twee klinkers = één lettergreep</span></p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in IEW)}</div></div>'
 '<div class="sblok"><h3>② El diptongo <i>ue</i></h3>'
 '<p class="sh">Mismo principio con <b>ue</b>: «p<b>ue</b>-do», «b<b>ue</b>-no». Desliza suavemente de la u a la e. <span class="stn">glijd vloeiend van u naar e</span></p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in UEW)}</div>'
 '<p class="ojo2">⚠️ <b>¡Ojo!</b> <span>No las separes: «pu-e-do» suena mal. Un solo movimiento: «pue-do». Y la <b>u</b> de <b>que/qui</b> es muda (U7): ahí no hay diptongo.</span> <span class="stn">niet splitsen; que/qui is géén diptongo</span></p></div>'
 '<div class="sblok"><h3>③ ¿ie o ue? · marca lo que oyes <span class="stn">teken wat je hoort</span></h3>'
 '<p class="sh">Pulsa las palabras con el diptongo <b>ue</b> (verde = correcto). Pulsa 🔊 para escuchar. <span class="gloss">klik de woorden met ue</span></p>'
 f'<div class="shrow">{"".join(dchip(*d) for d in DISCRIM)}</div>'
 '<p class="sfb" id="dfb"></p></div>'
 '<div class="sblok"><h3>④ La tilde en el diptongo</h3>'
 '<p class="sh">Si el acento cae en un diptongo final, la <b>tilde va en la segunda vocal</b>: a·di<b>ó</b>s. Pulsa 🔊 y repite. <span class="gloss">tilde op de tweede klinker</span></p>'
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
.gt td.v{color:var(--v);font-weight:700;font-family:var(--disp)}.gt td.ex{color:var(--mut);font-style:italic}
.ojo{background:var(--gt);border-radius:10px;padding:9px 12px;font-size:13.5px;margin:12px 0 0}
.ojo .es{font-weight:600;color:var(--ink)}
.mv{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:8px 0}
.mv-c{border-radius:12px;padding:12px;display:flex;flex-direction:column;gap:4px;font-family:var(--disp);font-size:14.5px}
.mv-c b{color:var(--gd)}.mv-t{font-size:13px;font-weight:800;margin-bottom:4px}
.mv-m{background:#FEF1E7;color:#B4530E}.mv-f{background:#E8F0FE;color:#1E40AF}
[data-theme=dark] .mv-m{background:#3a2415;color:#f3c39a}[data-theme=dark] .mv-f{background:#1b2740;color:#bcd0f5}
.dial{display:flex;flex-direction:column;gap:6px;margin:6px 0}
.db,.da{border-radius:12px;padding:8px 12px;font-size:14.5px;max-width:88%}
.db{background:var(--crema);align-self:flex-start}
.da{background:var(--gt);align-self:flex-end;text-align:right}
.builder{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 16px;margin:14px 0}
.bh{font-family:var(--disp);font-size:15px;color:var(--gd);margin-bottom:8px}
.brow{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}@media(max-width:760px){.brow{grid-template-columns:1fr}}
.bcol{display:flex;flex-direction:column;gap:6px}
.bl{font-size:11.5px;font-weight:700;color:var(--mut);text-transform:uppercase}
.bopt{border:1.5px solid var(--line);background:var(--paper);border-radius:10px;padding:7px 10px;font-size:14px;font-weight:600;cursor:pointer;text-align:left;color:var(--ink);font-family:var(--body)}
.bopt i{color:var(--mut);font-size:11.5px;font-style:normal}
.bopt.on{border-color:var(--g);background:var(--gt);color:var(--gd)}
.bout{margin-top:12px;background:var(--gt);border-radius:12px;padding:12px 14px;font-family:var(--disp);font-size:19px;color:var(--gd);text-align:center;min-height:26px}
.bhint{font-size:12.5px;color:var(--mut);margin:8px 0 0}
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
.di-lines div{display:flex;gap:8px;align-items:baseline}.di-lines span{font-size:12px;color:var(--mut);width:84px}
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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U9 · Kit · Gramática · Tarea</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 9 · Planes y obligaciones</h1><p>El <b>kit de supervivencia</b> (hacer planes, decir lo que tienes que hacer, decir «no» con educación), una <b>nota breve</b> donde ayuda, y tu <b>tarea final</b>. Pulsa 🔊 para oír las palabras. <span class="stn">de taal die je nodig hebt, kort uitgelegd, plus je eindtaak</span></p></div>
<main>
 <h2 class="subh">🔊 Suena bien <small>uitspraak — de diptongos ie &amp; ue</small></h2>
 {SUENA}
 <h2 class="subh">🔧 La máquina de frases <small>constrúyela tú: voy a / tengo que + infinitivo</small></h2>
 {BUILD}
 <h2 class="subh">§2 · Kit de supervivencia <small>los chunks por situación — pulsa para oírlos</small></h2>
 {KIT}
 <h2 class="subh">§4 · Gramática en la práctica <small>kort en functioneel — geen theorie om de theorie</small></h2>
 {GRAM}
 <h2 class="subh">§5 · Tarea final <small>jouw communicatieve opdracht</small></h2>
 {TAREA}
 <div class="foot">C4 · «Bienvenidos al español» · Unidad 9 · Planes y obligaciones</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.cc').forEach(function(c){{var es=c.getAttribute('data-es').replace(/·.*/,'').replace(/[…?¿!¡]/g,'').replace('+ infinitivo','');c.onclick=function(){{speak(es);}};}});
document.querySelectorAll('.shchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));}};}});
var dtot=document.querySelectorAll('.dchip[data-ok="1"]').length;
document.querySelectorAll('.dchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));var ok=b.getAttribute('data-ok')==='1';b.classList.remove('ok','no');b.classList.add(ok?'ok':'no');var n=document.querySelectorAll('.dchip.ok').length;var fb=document.getElementById('dfb');fb.textContent=ok?('¡diptongo ue! '+n+'/'+dtot+' 👏'):'Dat is het diptongo ie. Prueba otra.';}};}});
// zinbouwer
var pick=["Voy a","estudiar","esta tarde"];
function render(){{var s=pick[0]+" "+pick[1]+" "+pick[2]+".";document.getElementById('bout').textContent=s;}}
document.querySelectorAll('.bopt').forEach(function(b){{b.onclick=function(){{var s=+b.getAttribute('data-slot');pick[s]=b.getAttribute('data-v');
 document.querySelectorAll('.bopt[data-slot="'+s+'"]').forEach(function(x){{x.classList.toggle('on',x===b);}});render();speak(pick[0]+" "+pick[1]+" "+pick[2]);}};}});
render();
</script></body></html>"""
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U9_kgt.html","w").write(HTML)
print("C4_U9_kgt.html geschreven:",len(HTML),"bytes")
