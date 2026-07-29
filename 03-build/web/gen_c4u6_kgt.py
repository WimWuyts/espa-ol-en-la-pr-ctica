#!/usr/bin/env python3
# C4 · Unidad 6 — §2 KIT + §4 GRAMÁTICA (functioneel) + §5 TAREA + §Suena bien.
# Thema: La casa y los lugares · preposiciones de lugar · ¿dónde está? · hay · poder (permiso). Español-eerst + NL-steun.
import base64, os
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

CLUSTERS=[
 ("Las habitaciones","de kamers","🏠",[
   ("la cocina","de keuken"),("el salón","de woonkamer"),("el dormitorio","de slaapkamer"),
   ("el cuarto de baño","de badkamer"),("la entrada · el pasillo","de hal · de gang"),
 ]),
 ("En casa · muebles y cosas","meubels & spullen","🛋️",[
   ("la cama","het bed"),("el sofá · la mesa","de bank · de tafel"),("el armario","de kast"),
   ("el frigorífico","de koelkast"),("la ventana · la puerta","het raam · de deur"),
 ]),
 ("¿Dónde está? · las preposiciones","waar iets is","📍",[
   ("encima de","op / boven"),("debajo de","onder"),("dentro de","in / binnen in"),
   ("al lado de","naast"),("delante de · detrás de","voor · achter"),("entre","tussen"),
 ]),
 ("Situar · hay & está","situeren","🔎",[
   ("¿Dónde está…?","Waar is…?"),("está en…","het is in/op…"),("hay … en la cocina","er is … in de keuken"),
   ("aquí · ahí · fuera","hier · daar · buiten"),
 ]),
 ("Pedir permiso · poder","toestemming vragen","🙋",[
   ("¿Puedo…?","Mag/kan ik…?"),("¿Puedes…?","Kan/mag jij…?"),("Sí, puedes… · Aquí no","Ja, je mag… · Hier niet"),
   ("puedes ir fuera","je mag naar buiten"),
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
  <div class="obs">«Hay cosas <span class="pl">encima de</span> todas las sillas, <span class="pl">debajo de</span> la cama. <span class="pl">Dentro del</span> frigorífico tengo tres botellas.» · «¿<span class="v">Puedo</span> fumar? — Aquí no, pero <span class="v">puedes</span> ir fuera.»</div>
</div>

<div class="gcard">
  <h3><span class="pl">¿Dónde está?</span> — las preposiciones de lugar</h3>
  <p class="gp">Om te zeggen <b>waar</b> iets is, gebruik je een <b>plaats-woord</b> (turquoise):</p>
  <div class="prep">
    <div class="pr"><b>encima de</b><i>op / boven</i></div>
    <div class="pr"><b>debajo de</b><i>onder</i></div>
    <div class="pr"><b>dentro de</b><i>in / binnen</i></div>
    <div class="pr"><b>al lado de</b><i>naast</i></div>
    <div class="pr"><b>delante de</b><i>voor</i></div>
    <div class="pr"><b>detrás de</b><i>achter</i></div>
    <div class="pr"><b>entre</b><i>tussen</i></div>
  </div>
  <p class="ojo">⚠️ <b>¡Ojo!</b> <span class="es"><b>de + el = del</b>: encima <b>del</b> sofá (niet «de el»). En <b>a + el = al</b>: al lado <b>del</b> armario.</span></p>
</div>

<div class="gcard">
  <h3><span class="v">hay</span> vs. <span class="v">está</span> — er is / het staat</h3>
  <p class="gp">Twee manieren om te situeren:</p>
  <table class="gt">
    <tr><td class="v">hay</td><td>er is / er zijn (iets nieuw)</td><td class="ex">En el salón <b>hay</b> un sofá.</td></tr>
    <tr><td class="v">¿Dónde está…?</td><td>waar is…? (iets bekend)</td><td class="ex">¿Dónde <b>está</b> el bolso?</td></tr>
    <tr><td class="v">está / están</td><td>het staat / ze staan</td><td class="ex"><b>Está</b> encima de la mesa.</td></tr>
  </table>
  <p class="ojo">💡 <span class="es"><b>hay</b> = er bestaat iets (onbekend) · <b>está</b> = waar dat bekende ding zich bevindt.</span></p>
</div>

<div class="gcard soft">
  <h3><span class="v">poder</span> — ¿puedo…? · ¿puedes…? · pedir permiso</h3>
  <p class="gp">Om te vragen of iets <b>mag</b> of <b>kan</b>: <b>poder</b> + hele werkwoord.</p>
  <div class="mv">
    <div class="mv-c mv-m"><span class="mv-t">🙋 vragen</span><span><b>¿Puedo</b> fumar? (ik)</span><span><b>¿Puedes</b> venir? (jij)</span></div>
    <div class="mv-c mv-f"><span class="mv-t">✅ antwoorden</span><span>Sí, <b>puedes</b>…</span><span>Aquí no, pero <b>puedes</b> ir fuera.</span></div>
  </div>
  <p class="ojo">💡 <span class="es"><b>puedo</b> (ik) · <b>puedes</b> (jij) · <b>puede</b> (hij/zij). Altijd + een werkwoord in de hele vorm.</span></p>
</div>
"""

TAREA=r"""
<div class="tcard">
  <div class="tmeta">
    <span><b>👤 Wie</b> jij → de klas</span>
    <span><b>🎯 Doel</b> je huis tonen en zeggen waar alles is</span>
    <span><b>🗣️ Hoe</b> tekenen + benoemen + situeren</span>
    <span><b>✅ Resultaat</b> «Plano de mi casa» met 4 kamers</span>
  </div>
  <h3>Plano de mi casa — <i>teken je huis en zeg waar alles staat</i></h3>
  <ol class="pasos">
    <li><b>Dibuja el plano.</b> Teken de plattegrond van je huis (echt of droomhuis).</li>
    <li><b>Etiqueta las habitaciones.</b> Benoem elke kamer:
        <div class="frame">«Aquí está ____ (la cocina · el salón · el dormitorio…).»</div></li>
    <li><b>Sitúa las cosas.</b> Zeg waar de meubels/dingen zijn met een plaats-woord:
        <div class="frame">«En el salón hay un sofá. ____ (encima de · al lado de…) la mesa está ____.»</div></li>
    <li><b>Preséntalo.</b> Stel je plattegrond voor aan de klas — zónder af te lezen.</li>
  </ol>
  <div class="carne">
    <div class="carne-h">PLANO DE MI CASA · Academia «Welcome to Spanish»</div>
    <div class="carne-b diario">
      <div class="di-row"><span class="di-ic">🍳</span><div class="di-lines">
        <div><span>La habitación:</span><i></i></div><div><span>¿Qué hay?</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">🛋️</span><div class="di-lines">
        <div><span>La habitación:</span><i></i></div><div><span>¿Qué hay?</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">🛏️</span><div class="di-lines">
        <div><span>La habitación:</span><i></i></div><div><span>¿Qué hay?</span><i></i></div></div><span class="di-ok">☐</span></div>
    </div>
  </div>
  <p class="crit">🏁 <b>Klaar als…</b> je 4 kamers benoemt en per kamer zegt wat er is én waar het staat (met «hay» + een plaats-woord) — zónder af te lezen.</p>
</div>
"""

# §Suena bien · matrix A U6: b = v (betacismo, één klank) + llana ↔ aguda (klemtoon herkennen)
BVWORDS=[("bien","goed"),("vino","wijn"),("bueno","goed/lekker"),("vivir","leven/wonen"),("beber","drinken"),("ventana","raam")]
BVPAREN=[("baca","imperiaal (op auto)"),("vaca","koe"),("bello","mooi"),("vello","donshaar")]
DISCRIM=[("sofá",1),("casa",0),("salón",1),("silla",0),("balcón",1),("cocina",0),("sillón",1),("mesa",0)]
ACENTO=[("cocina","co·<b>CI</b>·na"),("salón","sa·<b>LÓN</b>"),("armario","ar·<b>MA</b>·rio"),("sofá","so·<b>FÁ</b>")]
def jcard(w,nl):
    return (f'<div class="cc" data-es="{w}"><span class="cc-es">{w}</span>'
            f'<span class="cc-nl">{nl}</span><button class="cc-spk">🔊</button></div>')
def dchip(w,ok): return f'<button class="dchip" data-ok="{ok}" data-w="{w}">🔊 {w}</button>'
def acchip(w,html): return f'<button class="shchip" data-w="{w}">🔊 {html}</button>'
SUENA=('<div class="suena">'
 '<div class="sblok"><h3>① La b y la v · un solo sonido</h3>'
 '<p class="sh">In het Spaans klinken <b>b</b> en <b>v</b> <b>net hetzelfde</b> (betacismo): «<b>b</b>ien» en «<b>v</b>ino» beginnen met dezelfde klank. Klik 🔊 en spreek na.</p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in BVWORDS)}</div></div>'
 '<div class="sblok"><h3>② ¿b o v? · se escribe distinto</h3>'
 '<p class="sh">Je hóórt geen verschil, dus let op de <b>schrijfwijze</b>! Deze paren klinken identiek maar betekenen iets anders:</p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in BVPAREN)}</div>'
 '<p class="ojo2">⚠️ <b>¡Ojo!</b> <span>ba<b>c</b>a (imperiaal) klinkt als <b>v</b>aca (koe)! De klank is gelijk; enkel de spelling verschilt.</span></p></div>'
 '<div class="sblok"><h3>③ ¿Llana o aguda? · teken wat je hoort</h3>'
 '<p class="sh">Klik de woorden met de klemtoon op de <b>laatste</b> lettergreep (<i>aguda</i>; groen = juist). Klik 🔊 om te horen.</p>'
 f'<div class="shrow">{"".join(dchip(*d) for d in DISCRIM)}</div>'
 '<p class="sfb" id="dfb"></p></div>'
 '<div class="sblok"><h3>④ Acentúa · dónde va la fuerza</h3>'
 '<p class="sh">De meeste woorden zijn <i>llana</i> (klemtoon op de <b>voorlaatste</b>): ca·SA. Klik 🔊 en herhaal.</p>'
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
.prep{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:8px;margin:6px 0}
.pr{background:#E6F7F5;border-radius:10px;padding:8px 10px;font-family:var(--disp);text-align:center}
.pr b{display:block;color:#0B7A73;font-size:14.5px}.pr i{font-size:11.5px;color:var(--mut);font-style:normal}
[data-theme=dark] .pr{background:#123a37}[data-theme=dark] .pr b{color:#7fd8cf}
.mv{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:8px 0}
.mv-c{border-radius:12px;padding:12px;display:flex;flex-direction:column;gap:4px;font-family:var(--disp);font-size:14.5px}
.mv-c b{color:var(--gd)}.mv-t{font-size:13px;font-weight:800;margin-bottom:4px}
.mv-m{background:#FEF1E7;color:#B4530E}.mv-f{background:#E9F7EF;color:#1E7A4E}
[data-theme=dark] .mv-m{background:#3a2415;color:#f3c39a}[data-theme=dark] .mv-f{background:#153a26;color:#a9e6c2}
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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U6 · Kit · Gramática · Tarea</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 6 · La casa y los lugares</h1><p>De <b>kit de supervivencia</b> (kamers benoemen &amp; zeggen waar de dingen zijn), een korte <b>uitlegnota</b> waar het helpt, en je <b>eindtaak</b>. Klik 🔊 om woorden te horen.</p></div>
<main>
 <h2 class="subh">🔊 Suena bien <small>uitspraak — b = v &amp; llana/aguda</small></h2>
 {SUENA}
 <h2 class="subh">§2 · Kit de supervivencia <small>de chunks per situatie — klik om te horen</small></h2>
 {KIT}
 <h2 class="subh">§4 · Gramática en la práctica <small>kort en functioneel — geen theorie om de theorie</small></h2>
 {GRAM}
 <h2 class="subh">§5 · Tarea final <small>jouw communicatieve opdracht</small></h2>
 {TAREA}
 <div class="foot">C4 · «Welcome to Spanish» · Unidad 6 · La casa y los lugares</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.cc').forEach(function(c){{var es=c.getAttribute('data-es').replace(/·.*/,'').replace(/[…?¿!¡]/g,'');c.onclick=function(){{speak(es);}};}});
document.querySelectorAll('.shchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));}};}});
var dtot=document.querySelectorAll('.dchip[data-ok="1"]').length;
document.querySelectorAll('.dchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));var ok=b.getAttribute('data-ok')==='1';b.classList.remove('ok','no');b.classList.add(ok?'ok':'no');var n=document.querySelectorAll('.dchip.ok').length;var fb=document.getElementById('dfb');fb.textContent=ok?('¡aguda! klemtoon op de laatste · '+n+'/'+dtot+' 👏'):'Esa es llana (klemtoon op de voorlaatste). Prueba otra.';}};}});
</script></body></html>"""
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U6_kgt.html","w").write(HTML)
print("C4_U6_kgt.html geschreven:",len(HTML),"bytes")
