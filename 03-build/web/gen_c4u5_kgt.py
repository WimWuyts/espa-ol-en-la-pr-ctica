#!/usr/bin/env python3
# C4 · Unidad 5 — §2 KIT + §4 GRAMÁTICA (functioneel) + §5 TAREA + §Suena bien.
# Thema: Objetos cotidianos · identificar (¿qué es esto?) · hay · para qué sirve. Español-eerst + NL-steun.
import base64, os
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

CLUSTERS=[
 ("Objetos de la clase","in de klas","📚",[
   ("el libro · el cuaderno","het boek · het schrift"),("el boli · el lápiz","de pen · het potlood"),
   ("la mochila","de rugzak"),("la mesa · la silla","de tafel · de stoel"),("el móvil","de gsm"),
 ]),
 ("Objetos de casa","in huis","🏠",[
   ("el sofá","de bank"),("la televisión","de tv"),("la ventana · la puerta","het raam · de deur"),
   ("el ordenador","de computer"),("las llaves","de sleutels"),("el vaso","het glas"),
 ]),
 ("Identificar · ¿qué es esto?","voorwerpen benoemen","❓",[
   ("¿Qué es esto?","Wat is dit?"),("Esto es un/una…","Dit is een…"),("Esto son…","Dit zijn…"),
   ("un libro · una mesa","een boek · een tafel"),
 ]),
 ("¿Para qué sirve?","waarvoor het dient","🔧",[
   ("¿Para qué sirve?","Waarvoor dient het?"),("Sirve para + inf.","Het dient om te…"),
   ("para abrir · beber","om te openen · drinken"),("para descansar · estudiar","om te rusten · studeren"),
 ]),
 ("¿Qué hay?","wat er is","📦",[
   ("¿Hay…?","Is/zijn er…?"),("(No) hay…","Er is (geen)…"),("Sí que hay…","Jawel, er is…"),
   ("aquí · ahí","hier · daar"),
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

GRAM=r"""
<div class="note">
  <div class="note-h">🔎 <b>Fíjate</b> · vuelve a la escena: ya lo has oído. <span class="stn">je hoorde dit al</span></div>
  <div class="obs">«<span class="v">¿Qué es esto?</span> — Esto es <span class="o">un sofá</span>, que <span class="v">sirve para</span> descansar.» · «¿<span class="v">Hay</span> <span class="o">un ordenador</span>? — No <span class="v">hay</span>… sí que <span class="v">hay</span>.»</div>
</div>

<div class="gcard">
  <h3><span class="o">un · una</span> — <i>een (♂ of ♀)</i> · el / la</h3>
  <p class="gp">Elk voorwerp is <b>♂ of ♀</b>. Meestal: <b>-o = ♂</b> (un libr<b>o</b>), <b>-a = ♀</b> (una mes<b>a</b>).</p>
  <div class="mv">
    <div class="mv-c mv-m"><span class="mv-t">♂ masculino</span><span><b>un</b> libro · <b>un</b> vaso</span><span><b>el</b> boli · <b>el</b> ordenador</span></div>
    <div class="mv-c mv-f"><span class="mv-t">♀ femenino</span><span><b>una</b> mesa · <b>una</b> silla</span><span><b>la</b> ventana · <b>la</b> mochila</span></div>
  </div>
  <p class="ojo">⚠️ <b>¡Ojo!</b> <span class="es">Algunas excepciones: <b>el</b> sofá, <b>la</b> televisión, <b>el</b> día, <b>la</b> mano. Apréndelas junto con su un/una.</span> <span class="stn">leer de uitzonderingen er meteen bij</span></p>
</div>

<div class="gcard">
  <h3><span class="v">¿Qué es esto?</span> — Esto es… · Esto son…</h3>
  <p class="gp">Pregunta por un objeto y responde: <span class="stn">vraag en antwoord</span></p>
  <table class="gt">
    <tr><td class="v">¿Qué es esto?</td><td>Wat is dit?</td><td class="ex">Esto <b>es</b> <b>un</b> libro. (één)</td></tr>
    <tr><td class="v">¿Qué es eso?</td><td>Wat is dat?</td><td class="ex">Eso <b>es</b> <b>una</b> ventana.</td></tr>
    <tr><td class="v">Esto son…</td><td>Dit zijn…</td><td class="ex">Esto <b>son</b> <b>las</b> llaves. (meer)</td></tr>
  </table>
  <p class="ojo">💡 <span class="es"><b>esto</b> = dit · <b>eso</b> = dat.</span> Eén ding → «es»; meer dingen → «son».</p>
</div>

<div class="gcard">
  <h3><span class="v">hay</span> — <i>er is / er zijn</i></h3>
  <p class="gp"><b>hay</b> no cambia nunca: para uno y para varios. <span class="stn">hay blijft altijd hetzelfde</span></p>
  <table class="gt">
    <tr><td class="v">Hay</td><td>er is / er zijn</td><td class="ex"><b>Hay</b> un sofá y dos sillas.</td></tr>
    <tr><td class="v">¿Hay…?</td><td>is/zijn er…?</td><td class="ex">¿<b>Hay</b> un ordenador?</td></tr>
    <tr><td class="v">No hay…</td><td>er is geen…</td><td class="ex"><b>No hay</b> televisión.</td></tr>
  </table>
  <p class="ojo">💡 <span class="es">Julio zegt «no hay… sí que <b>hay</b>» — «jawel, er is er wél één».</span></p>
</div>

<div class="gcard soft">
  <h3>… que <span class="v">sirve para</span> + <i>infinitivo</i></h3>
  <p class="gp">Om te zeggen <b>waarvoor</b> iets dient: <b>sirve para</b> + werkwoord (hele vorm). In de scène: «un vaso que <b>sirve para</b> beber», «un sofá que <b>sirve para</b> descansar». Meer dingen: «que <b>sirven</b> para…».</p>
</div>
"""

TAREA=r"""
<div class="tcard">
  <div class="tmeta">
    <span><b>👤 Quién</b> tú → la clase</span>
    <span><b>🎯 Objetivo</b> hacer un minidiccionario de objetos</span>
    <span><b>🗣️ Cómo</b> dibujar, nombrar y presentar</span>
    <span><b>✅ Resultado</b> «Diccionario de la clase» con 5 objetos</span>
  </div>
  <h3>Diccionario de la clase — <i>teken en benoem 5 voorwerpen</i></h3>
  <ol class="pasos">
    <li><b>Elige 5 objetos.</b> Elige 5 objetos de la clase o de tu casa. <span class="stn">vijf voorwerpen</span></li>
    <li><b>Dibuja e identifica.</b> Teken elk en schrijf de naam met <b>un/una</b>:
        <div class="frame">«Esto es ____ (un/una) ____.»</div></li>
    <li><b>¿Para qué sirve?</b> Schrijf per voorwerp waarvoor het dient:
        <div class="frame">«Sirve para ____ (abrir · beber · estudiar…).»</div></li>
    <li><b>Preséntalo.</b> Presenta tu diccionario a la clase, sin leer. <span class="stn">zónder af te lezen</span></li>
  </ol>
  <div class="carne">
    <div class="carne-h">DICCIONARIO DE LA CLASE · Academia «Bienvenidos al español»</div>
    <div class="carne-b diario">
      <div class="di-row"><span class="di-ic">✏️</span><div class="di-lines">
        <div><span>Esto es…</span><i></i></div><div><span>Sirve para…</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">📕</span><div class="di-lines">
        <div><span>Esto es…</span><i></i></div><div><span>Sirve para…</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">🎒</span><div class="di-lines">
        <div><span>Esto es…</span><i></i></div><div><span>Sirve para…</span><i></i></div></div><span class="di-ok">☐</span></div>
    </div>
  </div>
  <p class="crit">🏁 <b>Está listo cuando…</b> nombras 5 objetos con «esto es un/una…» (♂/♀ correcto) y de cada uno dices «sirve para + infinitivo», sin leer. <span class="stn">vijf voorwerpen, elk met «sirve para»</span></p>
</div>
"""

# §Suena bien · matrix A U5: r / rr (vibrante enkel↔dubbel) + de tilde (waarom een accent?)
RWORDS=[("pero","maar"),("cara","gezicht"),("para","voor/om"),("ahora","nu"),("mira","kijk"),("hora","uur")]
RRWORDS=[("perro","hond"),("rojo","rood"),("guitarra","gitaar"),("rosa","roze/roos"),("arriba","boven"),("ratón","muis")]
DISCRIM=[("perro",1),("pero",0),("carro",1),("caro",0),("rosa",1),("para",0),("radio",1),("cara",0)]
ACENTO=[("sofá","so·<b>FÁ</b>"),("televisión","te·le·vi·<b>SIÓN</b>"),("música","<b>MÚ</b>·si·ca"),("bolígrafo","bo·<b>LÍ</b>·gra·fo")]
def jcard(w,nl):
    return (f'<div class="cc" data-es="{w}"><span class="cc-es">{w}</span>'
            f'<span class="cc-nl">{nl}</span><button class="cc-spk">🔊</button></div>')
def dchip(w,ok): return f'<button class="dchip" data-ok="{ok}" data-w="{w}">🔊 {w}</button>'
def acchip(w,html): return f'<button class="shchip" data-w="{w}">🔊 {html}</button>'
SUENA=('<div class="suena">'
 '<div class="sblok"><h3>① La r suave · tussen klinkers</h3>'
 '<p class="sh">Entre vocales la <b>r</b> es <b>suave</b>: un solo toque de la lengua: «pe-ro», «ca-ra». Pulsa 🔊 y repite. <span class="gloss">r tussen klinkers = zacht</span></p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in RWORDS)}</div></div>'
 '<div class="sblok"><h3>② La rr fuerte · rollende r</h3>'
 '<p class="sh">La <b>rr</b> (y la <b>r</b> inicial) es <b>fuerte</b>, vibrante: «pe-<b>rr</b>o», «<b>r</b>ojo». <span class="stn">sterk en rollend</span></p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in RRWORDS)}</div>'
 '<p class="ojo2">⚠️ <b>¡Ojo!</b> <span>pe<b>r</b>o ≠ pe<b>rr</b>o. La doble r cambia el significado.</span> <span class="stn">maar ≠ hond</span></p></div>'
 '<div class="sblok"><h3>③ ¿r o rr? · marca lo que oyes <span class="stn">teken wat je hoort</span></h3>'
 '<p class="sh">Pulsa las palabras con la r <b>fuerte</b> (rr o r inicial; verde = correcto). Pulsa 🔊 para escuchar. <span class="gloss">klik de woorden met de sterke r</span></p>'
 f'<div class="shrow">{"".join(dchip(*d) for d in DISCRIM)}</div>'
 '<p class="sfb" id="dfb"></p></div>'
 '<div class="sblok"><h3>④ La tilde · waarom een accent?</h3>'
 '<p class="sh">El acento (<i>la tilde</i>) va en la sílaba más <b>fuerte</b>. Pulsa 🔊 y repite. <span class="gloss">de tilde staat op de sterkste lettergreep</span></p>'
 f'<div class="shrow">{"".join(acchip(*a) for a in ACENTO)}</div></div>'
 '</div>')

CSS=FONTS+r"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--card:#fff;
--p:#2563EB;--v:#EA7317;--o:#1E9E74;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif}
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
.p{color:var(--p);font-weight:700}.v{color:var(--v);font-weight:700}.o{color:var(--o);font-weight:700}
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
.mv-c{border-radius:12px;padding:12px;display:flex;flex-direction:column;gap:4px;font-family:var(--disp);font-size:15px}
.mv-c b{color:var(--gd)}.mv-t{font-size:13px;font-weight:800;margin-bottom:4px}
.mv-m{background:#E8F0FE;color:#1E40AF}.mv-f{background:#FCE7F0;color:#9D174D}
[data-theme=dark] .mv-m{background:#1b2740;color:#bcd0f5}[data-theme=dark] .mv-f{background:#3a1c2b;color:#f3b8d0}
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
.di-lines div{display:flex;gap:8px;align-items:baseline}.di-lines span{font-size:12px;color:var(--mut);width:70px}
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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U5 · Kit · Gramática · Tarea</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 5 · Objetos cotidianos</h1><p>El <b>kit de supervivencia</b> (nombrar objetos y decir para qué sirven), una <b>nota breve</b> donde ayuda, y tu <b>tarea final</b>. Pulsa 🔊 para oír las palabras. <span class="stn">de taal die je nodig hebt, kort uitgelegd, plus je eindtaak</span></p></div>
<main>
 <h2 class="subh">🔊 Suena bien <small>pronunciación — la r, la rr y la tilde</small></h2>
 {SUENA}
 <h2 class="subh">§2 · Kit de supervivencia <small>los chunks por situación — pulsa para oírlos</small></h2>
 {KIT}
 <h2 class="subh">§4 · Gramática en la práctica <small>kort en functioneel — geen theorie om de theorie</small></h2>
 {GRAM}
 <h2 class="subh">§5 · Tarea final <small>jouw communicatieve opdracht</small></h2>
 {TAREA}
 <div class="foot">C4 · «Bienvenidos al español» · Unidad 5 · Objetos cotidianos</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.cc').forEach(function(c){{var es=c.getAttribute('data-es').replace(/·.*/,'').replace(/[…?¿!¡]/g,'');c.onclick=function(){{speak(es);}};}});
document.querySelectorAll('.shchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));}};}});
var dtot=document.querySelectorAll('.dchip[data-ok="1"]').length;
document.querySelectorAll('.dchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));var ok=b.getAttribute('data-ok')==='1';b.classList.remove('ok','no');b.classList.add(ok?'ok':'no');var n=document.querySelectorAll('.dchip.ok').length;var fb=document.getElementById('dfb');fb.textContent=ok?('¡r fuerte! /r/ · '+n+'/'+dtot+' 👏'):'Esa es una r suave. Prueba otra.';}};}});
</script></body></html>"""
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U5_kgt.html","w").write(HTML)
print("C4_U5_kgt.html geschreven:",len(HTML),"bytes")
