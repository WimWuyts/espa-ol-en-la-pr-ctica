#!/usr/bin/env python3
# C4 · Unidad 7 — §2 KIT + §4 GRAMÁTICA (functioneel) + §5 TAREA + §Suena bien.
# Thema: Las profesiones · ¿a qué te dedicas? · ser + profesión (sin un/una) · ser vs estar · trabajo/trabajas/trabaja als chunks.
import base64, os
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

CLUSTERS=[
 ("Las profesiones","de beroepen","💼",[
   ("el profesor · la profesora","de leraar · de lerares"),("el escritor · la escritora","de schrijver · schrijfster"),
   ("el actor · la actriz","de acteur · de actrice"),("el dependiente · la dependienta","de winkelbediende"),
   ("el/la estudiante","de student(e)"),("el médico · la médica","de dokter"),
 ]),
 ("Los lugares de trabajo","waar je werkt","🏢",[
   ("la academia · la escuela","de (taal)school"),("la tienda","de winkel"),("la oficina","het kantoor"),
   ("el hospital","het ziekenhuis"),("el teatro","het theater"),
 ]),
 ("Preguntar por el trabajo","naar werk vragen","❓",[
   ("¿A qué te dedicas?","Wat doe je (voor werk)?"),("¿En qué trabajas?","Waarin werk je?"),
   ("¿Dónde trabajas?","Waar werk je?"),("¿Trabaja en una tienda?","Werkt hij/zij in een winkel?"),
 ]),
 ("Decir el trabajo","je werk zeggen","🗣️",[
   ("Soy profesor/a","Ik ben leraar/lerares"),("Trabajo en una oficina","Ik werk op een kantoor"),
   ("Soy estudiante","Ik ben student(e)"),("Yo trabajo · tú trabajas · él trabaja","ik werk · jij werkt · hij werkt"),
 ]),
 ("¿Cómo estamos?","hoe we ons voelen","😌",[
   ("Estoy bien · tranquilo/a","Ik ben oké · rustig"),("Estamos todos bien","We zijn allemaal oké"),
   ("¿Estáis bien?","Zijn jullie oké?"),("Estás muy mal","Jij bent er erg aan toe"),
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
  <div class="note-h">🔎 <b>Fíjate</b> · Kijk terug naar de scène — je hoorde dit al:</div>
  <div class="obs">«Yo <span class="v">trabajo</span> aquí, tú <span class="v">trabajas</span> aquí y él <span class="v">trabaja</span> aquí.» · «<span class="v">Es</span> profesora.» · «Yo <span class="v">estoy</span> bien. <span class="v">Estamos</span> todos bien.»</div>
</div>

<div class="gcard">
  <h3><span class="v">ser</span> + profesión — <i>soy profesor (zonder un/una!)</i></h3>
  <p class="gp">Je beroep zeggen = <b>ser</b> + beroep, <b>zonder lidwoord</b>:</p>
  <table class="gt">
    <tr><td class="v">Soy profesora.</td><td>Ik ben lerares.</td><td class="ex">niet: <s>soy una profesora</s></td></tr>
    <tr><td class="v">Es escritor.</td><td>Hij is schrijver.</td><td class="ex">¿Es actriz? — No, es profesora.</td></tr>
    <tr><td class="v">Soy estudiante.</td><td>Ik ben student(e).</td><td class="ex">el/la estudiante (blijft gelijk)</td></tr>
  </table>
  <p class="ojo">⚠️ <b>¡Ojo! ♂/♀:</b> <span class="es">profesor/profesor<b>a</b> · escritor/escritor<b>a</b> · dependient<b>e</b>/dependient<b>a</b> · actor/<b>actriz</b>. Gelijk: el/la estudiante.</span></p>
</div>

<div class="gcard">
  <h3><span class="v">trabajo · trabajas · trabaja</span> — <i>chunks uit de scène</i></h3>
  <p class="gp">Drie vaste vormen om over werk te praten (leer ze als chunks — het volledige systeem komt in het 5de jaar):</p>
  <table class="gt">
    <tr><td class="v">(yo) trabajo</td><td>ik werk</td><td class="ex">Trabajo <b>en</b> una tienda.</td></tr>
    <tr><td class="v">(tú) trabajas</td><td>jij werkt</td><td class="ex">¿Dónde trabajas?</td></tr>
    <tr><td class="v">(él/ella) trabaja</td><td>hij/zij werkt</td><td class="ex">¿Trabaja en una oficina?</td></tr>
  </table>
  <p class="ojo">💡 <span class="es">Werkplek altijd met <b>en</b>: trabajo <b>en</b> una academia · <b>en</b> casa.</span></p>
</div>

<div class="gcard soft">
  <h3><span class="v">ser</span> ↔ <span class="v">estar</span> — <i>wie je bent ↔ hoe je je voelt</i></h3>
  <p class="gp">Twee keer «zijn», elk met een eigen job:</p>
  <div class="mv">
    <div class="mv-c mv-m"><span class="mv-t">SER · wie/wat je bent</span><span><b>Es</b> profesora. (beroep)</span><span><b>Soy</b> belga. (afkomst, U3)</span></div>
    <div class="mv-c mv-f"><span class="mv-t">ESTAR · hoe je je voelt / bent</span><span><b>Estoy</b> bien · tranquilo/a.</span><span><b>Estamos</b> todos bien. · ¿<b>Estáis</b> bien?</span></div>
  </div>
  <p class="ojo">💡 <span class="es">Uit de scène: «<b>Es</b> María» (wie) ↔ «Tú no <b>estás</b> bien» (toestand). estar ken je al van U2 (estoy cansado) en U6 (¿dónde está?).</span></p>
</div>
"""

TAREA=r"""
<div class="tcard">
  <div class="tmeta">
    <span><b>👤 Wie</b> jij → de klas</span>
    <span><b>🎯 Doel</b> een beroep raden & laten raden</span>
    <span><b>🗣️ Hoe</b> vragen stellen + gissen (zoals Josefina!)</span>
    <span><b>✅ Resultaat</b> «¿Quién soy?»-raadspel met fiche</span>
  </div>
  <h3>¿Quién soy? — <i>adivina la profesión</i></h3>
  <ol class="pasos">
    <li><b>Elige una profesión.</b> Kies (geheim!) een beroep + werkplek en vul je fiche in.</li>
    <li><b>Da tres pistas.</b> Geef drie tips in het Spaans, zónder het beroep te noemen:
        <div class="frame">«Trabajo en ____ .» · «Estoy con muchas personas.» · «Trabajo con libros / ropa / …»</div></li>
    <li><b>La clase adivina.</b> De klas gist zoals Josefina: <div class="frame">«¿Puede ser ____ ?» · «¿Trabajas en una tienda?» · «¡Ya lo sé! Eres ____ .»</div></li>
    <li><b>Confirma.</b> Antwoord: «Sí, soy…» of «No, no soy…» — wie het raadt, is aan de beurt.</li>
  </ol>
  <div class="carne">
    <div class="carne-h">¿QUIÉN SOY? · Academia «Bienvenidos al español»</div>
    <div class="carne-b diario">
      <div class="di-row"><span class="di-ic">💼</span><div class="di-lines">
        <div><span>Mi profesión:</span><i></i></div><div><span>Trabajo en…</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">🕵️</span><div class="di-lines">
        <div><span>Pista 1:</span><i></i></div><div><span>Pista 2:</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">🎯</span><div class="di-lines">
        <div><span>Pista 3:</span><i></i></div><div><span>¡Ya lo sé! Eres…</span><i></i></div></div><span class="di-ok">☐</span></div>
    </div>
  </div>
  <p class="crit">🏁 <b>Klaar als…</b> je drie pistas geeft met «trabajo en…» + «estoy…», en gist met «¿puede ser…?» / «¿trabajas en…?» — zónder af te lezen.</p>
</div>
"""

# §Suena bien · matrix A U7: c/qu = /k/ + esdrújula (recycle b/v U6)
KWORDS=[("casa","huis"),("cocina","keuken"),("médico","dokter"),("actriz","actrice"),("carta","kaart"),("tranquilo","rustig")]
QUWORDS=[("queso","kaas"),("¿quién?","wie?"),("aquí","hier"),("tranquilidad","rust"),("pequeño","klein"),("¿qué?","wat?")]
DISCRIM=[("médico",1),("profesora",0),("música",1),("escritora",0),("sábado",1),("oficina",0),("teléfono",1),("academia",0)]
ACENTO=[("médico","<b>MÉ</b>·di·co"),("música","<b>MÚ</b>·si·ca"),("sábado","<b>SÁ</b>·ba·do"),("teléfono","te·<b>LÉ</b>·fo·no")]
def jcard(w,nl):
    return (f'<div class="cc" data-es="{w}"><span class="cc-es">{w}</span>'
            f'<span class="cc-nl">{nl}</span><button class="cc-spk">🔊</button></div>')
def dchip(w,ok): return f'<button class="dchip" data-ok="{ok}" data-w="{w}">🔊 {w}</button>'
def acchip(w,html): return f'<button class="shchip" data-w="{w}">🔊 {html}</button>'
SUENA=('<div class="suena">'
 '<div class="sblok"><h3>① La c fuerte · c + a/o/u = /k/</h3>'
 '<p class="sh">Delante de <b>a, o, u</b> la <b>c</b> suena /k/: «casa», «cocina», «médico». Pulsa 🔊 y repite. <span class="gloss">c vóór a/o/u = /k/</span></p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in KWORDS)}</div></div>'
 '<div class="sblok"><h3>② qu + e/i = /k/ · de stille u</h3>'
 '<p class="sh">Vóór <b>e</b> en <b>i</b> schrijf je <b>qu</b> voor dezelfde /k/-klank — de <b>u</b> hoor je NIET: «queso» = «ke-so», «¿quién?» = «kjen».</p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in QUWORDS)}</div>'
 '<p class="ojo2">⚠️ <b>¡Ojo!</b> <span>que = «ke» (niet «kwe»!) · qui = «ki». Vergelijk: <b>c</b>asa /k/ maar <b>c</b>ine /θ/ (U3) — daarom bestaat qu.</span></p></div>'
 '<div class="sblok"><h3>③ ¿Esdrújula o no? · teken wat je hoort</h3>'
 '<p class="sh">Pulsa las palabras con el acento en la <b>antepenúltima</b> sílaba (<i>esdrújulas</i> — MÉ-di-co; verde = correcto). Pulsa 🔊 para escuchar. <span class="gloss">derde lettergreep van achter</span></p>'
 f'<div class="shrow">{"".join(dchip(*d) for d in DISCRIM)}</div>'
 '<p class="sfb" id="dfb"></p></div>'
 '<div class="sblok"><h3>④ La esdrújula · siempre con tilde</h3>'
 '<p class="sh">Las <i>esdrújulas</i> llevan <b>siempre</b> tilde: MÉ-di-co, MÚ-si-ca. Pulsa 🔊 y repite marcando bien el acento. <span class="gloss">esdrújulas hebben altijd een accent</span></p>'
 f'<div class="shrow">{"".join(acchip(*a) for a in ACENTO)}</div></div>'
 '</div>')

CSS=FONTS+r"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--card:#fff;
--p:#2563EB;--v:#EA7317;--o:#1E9E74;--pl:#0E9E97;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif}
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
.p{color:var(--p);font-weight:700}.v{color:var(--v);font-weight:700}.o{color:var(--o);font-weight:700}.pl{color:var(--pl);font-weight:700}
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
.mv-m{background:#E8F0FE;color:#1E40AF}.mv-f{background:#FEF1E7;color:#B4530E}
[data-theme=dark] .mv-m{background:#1b2740;color:#bcd0f5}[data-theme=dark] .mv-f{background:#3a2415;color:#f3c39a}
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
.di-lines div{display:flex;gap:8px;align-items:baseline}.di-lines span{font-size:12px;color:var(--mut);width:96px}
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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U7 · Kit · Gramática · Tarea</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 7 · Las profesiones</h1><p>De <b>kit de supervivencia</b> (beroepen &amp; werkplekken, naar werk vragen), een korte <b>uitlegnota</b> waar het helpt, en je <b>eindtaak</b>. Klik 🔊 om woorden te horen.</p></div>
<main>
 <h2 class="subh">🔊 Suena bien <small>uitspraak — c/qu = /k/ &amp; la esdrújula</small></h2>
 {SUENA}
 <h2 class="subh">§2 · Kit de supervivencia <small>de chunks per situatie — klik om te horen</small></h2>
 {KIT}
 <h2 class="subh">§4 · Gramática en la práctica <small>kort en functioneel — geen theorie om de theorie</small></h2>
 {GRAM}
 <h2 class="subh">§5 · Tarea final <small>jouw communicatieve opdracht</small></h2>
 {TAREA}
 <div class="foot">C4 · «Bienvenidos al español» · Unidad 7 · Las profesiones</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.cc').forEach(function(c){{var es=c.getAttribute('data-es').replace(/·.*/,'').replace(/[…?¿!¡]/g,'');c.onclick=function(){{speak(es);}};}});
document.querySelectorAll('.shchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));}};}});
var dtot=document.querySelectorAll('.dchip[data-ok="1"]').length;
document.querySelectorAll('.dchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));var ok=b.getAttribute('data-ok')==='1';b.classList.remove('ok','no');b.classList.add(ok?'ok':'no');var n=document.querySelectorAll('.dchip.ok').length;var fb=document.getElementById('dfb');fb.textContent=ok?('¡esdrújula! MÉ-di-co · '+n+'/'+dtot+' 👏'):'Die is llana (klemtoon op de voorlaatste). Prueba otra.';}};}});
</script></body></html>"""
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U7_kgt.html","w").write(HTML)
print("C4_U7_kgt.html geschreven:",len(HTML),"bytes")
