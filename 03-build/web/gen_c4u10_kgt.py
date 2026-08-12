#!/usr/bin/env python3
# C4 · Unidad 10 — §2 KIT + §4 GRAMÁTICA (functioneel) + §5 TAREA + §Suena bien.
# Thema: Las tareas de casa · hay que + inf. (algemeen) ↔ tengo que (persoonlijk) · saber + inf. ·
# poder + inf. (recycle) · hulp aanbieden/afwijzen. Imperativo = ENKEL herkennen (systeem = C6).
import base64, os
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

CLUSTERS=[
 ("Las tareas de casa","de huistaken","🧹",[
   ("limpiar el polvo","afstoffen"),("pasar la aspiradora","stofzuigen"),
   ("fregar los platos","de vaat doen"),("ordenar los armarios","de kasten opruimen"),
   ("hacer la cama","het bed opmaken"),("planchar · cocinar","strijken · koken"),
 ]),
 ("Hulp aanbieden","ayudar","🤝",[
   ("Yo te ayudo","Ik help je"),("¿Te ayudo?","Help ik je?"),
   ("¿Qué tengo que hacer?","Wat moet ik doen?"),("No es molestia","Het is geen moeite"),
   ("Déjame, lo hago yo","Laat mij maar, ik doe het"),
 ]),
 ("¿Sabes hacerlo?","kunnen/weten","💡",[
   ("¿Sabes…?","Kan je…? / Weet je…?"),("Sé pasar la aspiradora","Ik kan stofzuigen"),
   ("Claro que sé","Natuurlijk kan ik dat"),("¿Sabes cómo funciona?","Weet je hoe het werkt?"),
   ("No sé cocinar","Ik kan niet koken"),
 ]),
 ("Hay que…","het moet gebeuren","✅",[
   ("Hay que limpiar","Er moet gepoetst worden"),("Hay que ordenar esto","Dit moet opgeruimd worden"),
   ("Tengo que fregar","Ík moet de vaat doen"),("No tienes que molestarte","Je hoeft geen moeite te doen"),
 ]),
 ("En la academia","kleine problemen","🔧",[
   ("está enferma","zij is ziek"),("no puede venir","zij kan niet komen"),
   ("no funciona","het werkt niet"),("¡Ahí está!","Daar is het! / Gelukt!"),("¡Qué desorden!","Wat een rommel!"),
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

# interactieve «taakverdeler»: kies persoon + taak → juiste formule (hay que / tengo que / sé)
REPARTO=r"""
<div class="builder">
  <div class="bh">🧹 <b>El reparto de tareas</b> · elige y pulsa: aparece la fórmula correcta. <span class="stn">kies en klik</span></div>
  <div class="brow">
    <div class="bcol"><span class="bl">1 · ¿quién?</span>
      <button class="bopt on" data-slot="0" data-v="hay">general <i>(hay que…)</i></button>
      <button class="bopt" data-slot="0" data-v="yo">yo <i>(tengo que…)</i></button>
      <button class="bopt" data-slot="0" data-v="tu">tú <i>(tienes que…)</i></button>
      <button class="bopt" data-slot="0" data-v="se">sé hacerlo <i>(sé…)</i></button>
    </div>
    <div class="bcol"><span class="bl">2 · ¿qué tarea?</span>
      <button class="bopt on" data-slot="1" data-v="limpiar el polvo">limpiar el polvo</button>
      <button class="bopt" data-slot="1" data-v="pasar la aspiradora">pasar la aspiradora</button>
      <button class="bopt" data-slot="1" data-v="fregar los platos">fregar los platos</button>
      <button class="bopt" data-slot="1" data-v="ordenar los armarios">ordenar los armarios</button>
      <button class="bopt" data-slot="1" data-v="cocinar">cocinar</button>
    </div>
  </div>
  <div class="bout" id="bout"></div>
  <p class="bhint">💡 <b>hay que</b> = tiene que hacerse (no dices quién) · <b>tengo que</b> = yo debo · <b>sé</b> = yo sé hacerlo. <span class="stn">algemeen · ík moet · ik kán het</span></p>
</div>
"""

GRAM=r"""
<div class="note">
  <div class="note-h">🔎 <b>Fíjate</b> · vuelve a la escena: ya lo has oído. <span class="stn">je hoorde dit al</span></div>
  <div class="obs">«<span class="v">Hay que</span> limpiar esto.» · «Yo <span class="v">te ayudo</span>. ¿Qué <span class="v">tengo que</span> hacer?» · «¿<span class="v">Sabes</span> pasar la aspiradora?» — «Claro que <span class="v">sé</span>.»</div>
</div>

<div class="gcard">
  <h3><span class="v">hay que</span> ↔ <span class="v">tengo que</span> — <i>algemeen of persoonlijk?</i></h3>
  <p class="gp">Dos maneras de decir «moeten». La diferencia: <b>¿dices quién?</b> <span class="stn">zeg je wíe het moet doen?</span></p>
  <div class="mv">
    <div class="mv-c mv-m"><span class="mv-t">🌐 hay que + infinitivo</span><span><b>Hay que</b> limpiar esto.</span><span><i>Tiene que hacerse</i> (sin decir quién) <span class="stn">er moet gepoetst worden</span></span></div>
    <div class="mv-c mv-f"><span class="mv-t">🙋 tener que + infinitivo</span><span><b>Tengo que</b> fregar. · <b>Tienes que</b> ordenar.</span><span><i>Yo debo · tú debes</i> (sí hay persona) <span class="stn">ík moet · jíj moet</span></span></div>
  </div>
  <p class="ojo">💡 <span class="es"><b>hay que</b> no cambia nunca, igual que <b>hay</b> (U5/U6). Útil cuando no quieres decir quién lo hace.</span> <span class="stn">hay que verandert nooit</span></p>
</div>

<div class="gcard">
  <h3><span class="v">saber</span> + infinitivo — <i>iets kúnnen (geleerd hebben)</i></h3>
  <p class="gp">Para decir que <b>sabes</b> hacer algo porque lo has aprendido: <span class="stn">kunnen omdat je het geleerd hebt</span></p>
  <table class="gt">
    <tr><td class="v">sé</td><td>ik kan / ik weet</td><td class="ex"><b>Sé</b> pasar la aspiradora.</td></tr>
    <tr><td class="v">¿sabes…?</td><td>kan jij…?</td><td class="ex">¿<b>Sabes</b> cómo funciona?</td></tr>
    <tr><td class="v">sabemos</td><td>wij kunnen</td><td class="ex">Los hombres también <b>sabemos</b> limpiar.</td></tr>
  </table>
  <p class="ojo">⚠️ <b>¡Ojo!</b> <span class="es"><b>saber</b> = poder porque lo has <i>aprendido</i> (sé cocinar). <b>poder</b> = porque te <i>dejan</i> o te sale (no puede venir, está enferma).</span> <span class="stn">saber = geleerd · poder = mag/lukt</span></p>
</div>

<div class="gcard soft">
  <h3>Drie formules, één patroon: <span class="v">+ infinitivo</span></h3>
  <p class="gp">Ya conoces una buena lista, y <b>todas</b> funcionan igual: forma fija + <b>el infinitivo</b>. <span class="stn">vaste vorm + het hele werkwoord</span></p>
  <div class="stack">
    <div class="st"><b>voy a</b> limpiar<i>plan (U9)</i></div>
    <div class="st"><b>tengo que</b> limpiar<i>ik moet (U9)</i></div>
    <div class="st"><b>hay que</b> limpiar<i>tiene que hacerse (nuevo)</i></div>
    <div class="st"><b>sé</b> limpiar<i>ik kan het (nieuw)</i></div>
    <div class="st"><b>puedo</b> limpiar<i>ik mag/kan (U6)</i></div>
  </div>
</div>

<div class="gcard">
  <h3>Ofrecer ayuda — <i>hulp aanbieden &amp; afwijzen</i></h3>
  <div class="dial">
    <div class="db">— ¿Qué haces? <b>Yo te ayudo.</b></div>
    <div class="da">— <b>No tienes que molestarte.</b></div>
    <div class="db">— <b>No es molestia.</b> ¿Qué <b>tengo que</b> hacer?</div>
    <div class="da">— Pues <b>puedes</b> ordenar los armarios.</div>
  </div>
  <p class="ojo">👂 <span class="es">En la escena Paul dice también «<b>Déjame</b>, lo hago yo» y «<b>friega</b>, <b>ordena</b>…». Esas formas de mandato solo hay que <b>reconocerlas</b>; todavía no tienes que formarlas tú.</span> <span class="stn">herkennen volstaat</span></p>
</div>
"""

TAREA=r"""
<div class="tcard">
  <div class="tmeta">
    <span><b>👤 Quién</b> tú + tu grupo</span>
    <span><b>🎯 Objetivo</b> repartir las tareas de forma justa</span>
    <span><b>🗣️ Cómo</b> decir qué hay que hacer, qué sabes hacer y quién hace qué</span>
    <span><b>✅ Resultado</b> «¿Quién hace qué?» — un cuadro de tareas</span>
  </div>
  <h3>¿Quién hace qué? — <i>haced juntos un cuadro de tareas</i> <span class="stn">maak samen een takenschema</span></h3>
  <ol class="pasos">
    <li><b>¿Qué hay que hacer?</b> Anotad en grupo <b>4 tareas</b> que hay que hacer: <span class="stn">vier taken die gedaan moeten worden</span>
        <div class="frame">«<b>Hay que</b> ____ (limpiar el polvo · fregar los platos…).»</div></li>
    <li><b>¿Qué sabes hacer?</b> Di lo que <b>tú</b> sabes hacer y pregúntaselo a tu grupo: <span class="stn">zeg wat jij kunt en vraag het door</span>
        <div class="frame">«<b>Yo sé</b> ____ .» · «¿<b>Sabes</b> ____ ?» — «Claro que sé.» / «No sé ____ .»</div></li>
    <li><b>Repartid las tareas.</b> Repartidlas: ¿quién hace qué? <span class="stn">wie doet wat?</span>
        <div class="frame">«Tú <b>tienes que</b> ____ y yo <b>tengo que</b> ____ .» · «<b>Yo te ayudo.</b>»</div></li>
    <li><b>Presentad el cuadro.</b> Presentad vuestro cuadro a la clase, sin leerlo. <span class="stn">zónder af te lezen</span></li>
  </ol>
  <div class="carne">
    <div class="carne-h">CUADRO DE TAREAS · Academia «Bienvenidos al español»</div>
    <div class="carne-b diario">
      <div class="di-row"><span class="di-ic">🧹</span><div class="di-lines">
        <div><span>Hay que…</span><i></i></div><div><span>¿Quién?</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">🍽️</span><div class="di-lines">
        <div><span>Hay que…</span><i></i></div><div><span>¿Quién?</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">💡</span><div class="di-lines">
        <div><span>Yo sé…</span><i></i></div><div><span>No sé…</span><i></i></div></div><span class="di-ok">☐</span></div>
    </div>
  </div>
  <p class="crit">🏁 <b>Está listo cuando…</b> nombras 4 tareas con «hay que + infinitivo», dices lo que sabes y lo que no con «(no) sé + infinitivo», y repartes las tareas con «tengo/tienes que» + «yo te ayudo», sin leer. <span class="stn">klaar als je dat alles zegt zónder af te lezen</span></p>
</div>
"""

# §Suena bien · matrix A U10: g/gu = /g/ ↔ ge/gi = /x/ (jota) + herhaling aguda/llana
GWORDS=[("guapo","knap"),("agua","water"),("luego","later"),("gato","kat"),("algo","iets"),("amigo","vriend")]
GUWORDS=[("guitarra","gitaar"),("seguir","volgen"),("juguete","speelgoed"),("guerra","oorlog"),("Miguel","Miguel"),("hoguera","vuur/kampvuur")]
DISCRIM=[("gente",1),("gato",0),("gimnasio",1),("guapo",0),("general",1),("guitarra",0),("girar",1),("agua",0)]
ACENTO=[("aspiradora","as·pi·ra·<b>DO</b>·ra"),("ordenar","or·de·<b>NAR</b>"),("armario","ar·<b>MA</b>·rio"),("limpiar","lim·<b>PIAR</b>")]
def jcard(w,nl):
    return (f'<div class="cc" data-es="{w}"><span class="cc-es">{w}</span>'
            f'<span class="cc-nl">{nl}</span><button class="cc-spk">🔊</button></div>')
def dchip(w,ok): return f'<button class="dchip" data-ok="{ok}" data-w="{w}">🔊 {w}</button>'
def acchip(w,html): return f'<button class="shchip" data-w="{w}">🔊 {html}</button>'
SUENA=('<div class="suena">'
 '<div class="sblok"><h3>① La g fuerte · g + a/o/u</h3>'
 '<p class="sh">Delante de <b>a, o, u</b> la <b>g</b> suena como en «goal»: «<b>g</b>uapo», «a<b>g</b>ua», «lue<b>g</b>o». Pulsa 🔊 y repite. <span class="gloss">g vóór a/o/u = harde g</span></p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in GWORDS)}</div></div>'
 '<div class="sblok"><h3>② gue / gui · de stille u</h3>'
 '<p class="sh">Delante de <b>e</b> e <b>i</b> se escribe <b>gue/gui</b> para el mismo sonido /g/: la <b>u</b> NO se oye: «<b>gui</b>tarra» = «gi-tarra». <span class="stn">de u hoor je niet</span></p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in GUWORDS)}</div>'
 '<p class="ojo2">⚠️ <b>¡Ojo!</b> <span>Igual que con <b>qu</b> (U7): la u es un <i>truco de escritura</i>. Sin u sale la jota: <b>ge</b>nte, <b>gi</b>mnasio = /x/ (U2).</span> <span class="stn">de u is een schrijftruc</span></p></div>'
 '<div class="sblok"><h3>③ ¿/g/ o jota? · marca lo que oyes <span class="stn">teken wat je hoort</span></h3>'
 '<p class="sh">Pulsa las palabras con el sonido de la <b>jota</b> /x/ (ge/gi; verde = correcto). Pulsa 🔊 para escuchar. <span class="gloss">klik de woorden met de jota-klank</span></p>'
 f'<div class="shrow">{"".join(dchip(*d) for d in DISCRIM)}</div>'
 '<p class="sfb" id="dfb"></p></div>'
 '<div class="sblok"><h3>④ Repaso · aguda o llana</h3>'
 '<p class="sh">Repaso: ¿dónde cae el acento en estas palabras de las tareas? Pulsa 🔊 y repite. <span class="gloss">waar ligt de klemtoon?</span></p>'
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
.mv-c i{font-family:var(--body);font-size:12px;font-style:italic;opacity:.85}
.mv-m{background:#E6F7F5;color:#0B7A73}.mv-f{background:#FEF1E7;color:#B4530E}
[data-theme=dark] .mv-m{background:#123a37;color:#7fd8cf}[data-theme=dark] .mv-f{background:#3a2415;color:#f3c39a}
.stack{display:flex;flex-direction:column;gap:6px;margin:8px 0}
.st{background:var(--paper);border:1.5px solid var(--line);border-left:4px solid var(--v);border-radius:10px;padding:8px 12px;font-family:var(--disp);font-size:15px}
.st i{float:right;font-family:var(--body);font-size:12px;color:var(--mut);font-style:normal}
.dial{display:flex;flex-direction:column;gap:6px;margin:6px 0}
.db,.da{border-radius:12px;padding:8px 12px;font-size:14.5px;max-width:88%}
.db{background:var(--crema);align-self:flex-start}
.da{background:var(--gt);align-self:flex-end;text-align:right}
.builder{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 16px;margin:14px 0}
.bh{font-family:var(--disp);font-size:15px;color:var(--gd);margin-bottom:8px}
.brow{display:grid;grid-template-columns:1fr 1fr;gap:12px}@media(max-width:760px){.brow{grid-template-columns:1fr}}
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
.di-lines div{display:flex;gap:8px;align-items:baseline}.di-lines span{font-size:12px;color:var(--mut);width:74px}
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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U10 · Kit · Gramática · Tarea</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 10 · Las tareas de casa</h1><p>El <b>kit de supervivencia</b> (las tareas de casa, ofrecer ayuda, decir lo que sabes hacer), una <b>nota breve</b> donde ayuda, y tu <b>tarea final</b>. Pulsa 🔊 para oír las palabras. <span class="stn">de taal die je nodig hebt, kort uitgelegd, plus je eindtaak</span></p></div>
<main>
 <h2 class="subh">🔊 Suena bien <small>pronunciación — la g, gue/gui y la jota</small></h2>
 {SUENA}
 <h2 class="subh">🧹 El reparto de tareas <small>pulsa y mira la fórmula correcta</small></h2>
 {REPARTO}
 <h2 class="subh">§2 · Kit de supervivencia <small>los chunks por situación — pulsa para oírlos</small></h2>
 {KIT}
 <h2 class="subh">§4 · Gramática en la práctica <small>kort en functioneel — geen theorie om de theorie</small></h2>
 {GRAM}
 <h2 class="subh">§5 · Tarea final <small>jouw communicatieve opdracht</small></h2>
 {TAREA}
 <div class="foot">C4 · «Bienvenidos al español» · Unidad 10 · Las tareas de casa</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.cc').forEach(function(c){{var es=c.getAttribute('data-es').replace(/·.*/,'').replace(/[…?¿!¡]/g,'');c.onclick=function(){{speak(es);}};}});
document.querySelectorAll('.shchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));}};}});
var dtot=document.querySelectorAll('.dchip[data-ok="1"]').length;
document.querySelectorAll('.dchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));var ok=b.getAttribute('data-ok')==='1';b.classList.remove('ok','no');b.classList.add(ok?'ok':'no');var n=document.querySelectorAll('.dchip.ok').length;var fb=document.getElementById('dfb');fb.textContent=ok?('¡jota! /x/ · '+n+'/'+dtot+' 👏'):'Die heeft de harde /g/. Prueba otra.';}};}});
// taakverdeler
var FORM={{hay:["Hay que"," (tiene que hacerse)"],yo:["Tengo que"," (yo)"],tu:["Tienes que"," (tú)"],se:["Sé"," (yo sé hacerlo)"]}};
var pick=["hay","limpiar el polvo"];
function render(){{var f=FORM[pick[0]];document.getElementById('bout').textContent=f[0]+" "+pick[1]+".";}}
document.querySelectorAll('.bopt').forEach(function(b){{b.onclick=function(){{var s=+b.getAttribute('data-slot');pick[s]=b.getAttribute('data-v');
 document.querySelectorAll('.bopt[data-slot="'+s+'"]').forEach(function(x){{x.classList.toggle('on',x===b);}});render();speak(FORM[pick[0]][0]+" "+pick[1]);}};}});
render();
</script></body></html>"""
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U10_kgt.html","w").write(HTML)
print("C4_U10_kgt.html geschreven:",len(HTML),"bytes")
