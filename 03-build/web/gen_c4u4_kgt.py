#!/usr/bin/env python3
# C4 · Unidad 4 — §2 KIT + §4 GRAMÁTICA (functioneel) + §5 TAREA + §Suena bien.
# Thema: La familia · presentar & describir a personas (mi/tu · ser+adjetivo · concordancia -o/-a).
import base64, os
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

CLUSTERS=[
 ("La familia","de gezinsleden","👨‍👩‍👧‍👦",[
   ("la madre · el padre","de moeder · de vader"),("el hermano · la hermana","de broer · de zus"),
   ("el abuelo · la abuela","de opa · de oma"),("el tío · la tía","de oom · de tante"),
   ("el hijo · la hija","de zoon · de dochter"),("los padres","de ouders"),
 ]),
 ("Presentar a alguien","iemand voorstellen","🫱",[
   ("Esta es mi madre","Dit is mijn moeder"),("Este es mi padre","Dit is mijn vader"),
   ("Es mi hermano/a","Het is mijn broer/zus"),("Se llama…","Hij/zij heet…"),("Es la hermana de María","Het is de zus van María"),
 ]),
 ("Describir · el físico","het uiterlijk","🧍",[
   ("es alto/a · bajo/a","is lang · klein"),("es guapo/a","is knap"),("es delgado/a · gordo/a","is slank · mollig"),
   ("es fuerte","is sterk"),("tiene el pelo largo/corto","heeft lang/kort haar"),
 ]),
 ("Describir · el carácter","het karakter","😊",[
   ("es simpático/a","is aardig"),("es divertido/a","is grappig"),("es amable","is vriendelijk"),
   ("es inteligente","is intelligent"),("es elegante","is elegant"),("muy… · un poco…","heel… · een beetje…"),
 ]),
 ("¿Dónde vive?","waar iemand woont","🏠",[
   ("¿Dónde vives?","Waar woon je?"),("Vivo en…","Ik woon in…"),("Vive en Londres","Woont in Londen"),
   ("en la calle…","in de straat…"),
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
  <div class="obs">«Esta es <span class="p">mi</span> madre.» · «<span class="v">Es</span> muy elegante, pero un poco gorda.» · «<span class="v">Es</span> una chica muy delgad<u>a</u> y muy guap<u>a</u>.»</div>
</div>

<div class="gcard">
  <h3><span class="p">mi · tu · su</span> — <i>van wie is het?</i> (posesivos)</h3>
  <p class="gp">Om te zeggen <b>wiens</b> familielid het is. Drie vaste vormen volstaan nu:</p>
  <table class="gt">
    <tr><td class="p">mi</td><td>mijn</td><td class="ex"><b>mi</b> madre · <b>mi</b> hermano</td></tr>
    <tr><td class="p">tu</td><td>jouw</td><td class="ex">¿Y <b>tu</b> familia?</td></tr>
    <tr><td class="p">su</td><td>zijn/haar</td><td class="ex"><b>su</b> padre (el padre de él/ella)</td></tr>
  </table>
  <p class="ojo">💡 <span class="es">Ook mogelijk: <b>de</b> + naam — «la hermana <b>de</b> María» (= de zus van María).</span> mi/tu blijven <b>gelijk</b> (geen -o/-a): mi madre én mi padre.</p>
</div>

<div class="gcard">
  <h3><span class="v">es</span> + <i>adjetivo</i> — <i>iemand beschrijven</i></h3>
  <p class="gp">Met <b>ser</b> (es) beschrijf je hoe iemand <b>is</b>. Het adjectief past zich aan aan ♂/♀ (net als in U3):</p>
  <div class="mv">
    <div class="mv-c mv-m"><span class="mv-t">♂ un chico</span><span>es alt<b>o</b> · guap<b>o</b> · delgad<b>o</b></span><span>simpátic<b>o</b> · divertid<b>o</b></span></div>
    <div class="mv-c mv-f"><span class="mv-t">♀ una chica</span><span>es alt<b>a</b> · guap<b>a</b> · delgad<b>a</b></span><span>simpátic<b>a</b> · divertid<b>a</b></span></div>
  </div>
  <p class="gp" style="margin-top:10px">Sommige blijven <b>gelijk</b> voor ♂ én ♀: <b>amable</b>, <b>inteligente</b>, <b>elegante</b>, <b>fuerte</b> (eindigen op -e).</p>
  <p class="ojo">⚠️ <b>¡Ojo!</b> <span class="es">Beschrijven = <b>ser</b> (es), niet estar: «es guapa», «es simpático».</span> (estar = hoe je je nú voelt, uit U2.)</p>
</div>

<div class="gcard soft">
  <h3>muy <span class="v">·</span> un poco — <i>een beetje meer of minder</i></h3>
  <p class="gp"><b>muy</b> = heel (versterkt): «muy alta», «muy inteligente». <b>un poco</b> = een beetje (verzacht, vaak iets negatiefs): «un poco gorda», «un poco tímido». In de scène: «muy elegante, <b>pero un poco</b> gorda».</p>
</div>
"""

TAREA=r"""
<div class="tcard">
  <div class="tmeta">
    <span><b>👤 Wie</b> jij → de klas</span>
    <span><b>🎯 Doel</b> je familie voorstellen &amp; beschrijven</span>
    <span><b>🗣️ Hoe</b> een stamboom tekenen + mondeling presenteren</span>
    <span><b>✅ Resultaat</b> «Mi árbol de familia» met 4 personen</span>
  </div>
  <h3>Mi árbol de familia — <i>teken en beschrijf je (echte of fantasie-)familie</i></h3>
  <ol class="pasos">
    <li><b>Dibuja el árbol.</b> Teken een stamboom met <b>4 personen</b> (bv. madre, padre, hermano/a, abuela).</li>
    <li><b>Presenta a cada persona.</b> Zeg wie het is:
        <div class="frame">«Est__ es mi ____ (madre/padre/…). Se llama ____.»</div></li>
    <li><b>Descríbelo/la.</b> Geef per persoon 2 adjectieven (let op ♂/♀ + muy/un poco):
        <div class="frame">«Es ____ y ____. Es muy ____.»</div></li>
    <li><b>Preséntalo.</b> Stel je stamboom voor aan de klas — zónder af te lezen.</li>
  </ol>
  <div class="carne">
    <div class="carne-h">MI ÁRBOL DE FAMILIA · Academia «Bienvenidos al español»</div>
    <div class="carne-b diario">
      <div class="di-row"><span class="di-ic">👩</span><div class="di-lines">
        <div><span>Es mi…</span><i></i></div><div><span>Se llama</span><i></i></div><div><span>Es…</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">👨</span><div class="di-lines">
        <div><span>Es mi…</span><i></i></div><div><span>Se llama</span><i></i></div><div><span>Es…</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">🧑</span><div class="di-lines">
        <div><span>Es mi…</span><i></i></div><div><span>Se llama</span><i></i></div><div><span>Es…</span><i></i></div></div><span class="di-ok">☐</span></div>
    </div>
  </div>
  <p class="crit">🏁 <b>Klaar als…</b> je 4 familieleden voorstelt met «est_ es mi…», elk met 2 adjectieven (juiste ♂/♀ + muy/un poco), en je de stamboom aanwijst — zónder af te lezen.</p>
</div>
"""

# §Suena bien · matrix A U4: ll / y (yeísmo) + acentuación llana (recyclen ñ, c/z)
LLWORDS=[("ella","zij"),("calle","straat"),("llamar","bellen/heten"),("llave","sleutel"),("apellido","achternaam"),("silla","stoel")]
YWORDS=[("yo","ik"),("ya","al"),("playa","strand"),("mayo","mei"),("desayuno","ontbijt"),("leyenda","legende")]
DISCRIM=[("calle",1),("mesa",0),("playa",1),("gato",0),("llave",1),("pan",0),("ella",1),("libro",0)]
ACENTO=[("madre","MA·dre"),("hermano","her·MA·no"),("abuela","a·BUE·la"),("elegante","e·le·GAN·te")]
def jcard(w,nl):
    return (f'<div class="cc" data-es="{w}"><span class="cc-es">{w}</span>'
            f'<span class="cc-nl">{nl}</span><button class="cc-spk">🔊</button></div>')
def dchip(w,ok): return f'<button class="dchip" data-ok="{ok}" data-w="{w}">🔊 {w}</button>'
def acchip(w,html): return f'<button class="shchip" data-w="{w}">🔊 {html}</button>'
SUENA=('<div class="suena">'
 '<div class="sblok"><h3>① La elle · ll — de klank van «calle»</h3>'
 '<p class="sh">En la mayoría de los países la <b>ll</b> suena como la «j» de «ja»: «calle» ≈ «ca-je». Pulsa 🔊 y repite. <span class="gloss">ll klinkt als j</span></p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in LLWORDS)}</div>'
 '<p class="ojo2">⚠️ <b>¡Ojo!</b> <span>«ll» is één letter/klank, niet twee l\'s: ca<b>ll</b>e, <b>ll</b>ave, ape<b>ll</b>ido.</span></p></div>'
 '<div class="sblok"><h3>② La i griega · y — el yeísmo</h3>'
 '<p class="sh">De <b>y</b> klinkt <b>net als de ll</b> (dat heet <i>yeísmo</i>): «yo» ≈ «jo», «playa» ≈ «pla-ja».</p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in YWORDS)}</div></div>'
 '<div class="sblok"><h3>③ ¿ll/y o no? · teken wat je hoort</h3>'
 '<p class="sh">Pulsa las palabras con el sonido <b>ll/y</b> /ʝ/ (verde = correcto). Pulsa 🔊 para escuchar. <span class="gloss">klik de woorden met de ll/y-klank</span></p>'
 f'<div class="shrow">{"".join(dchip(*d) for d in DISCRIM)}</div>'
 '<p class="sfb" id="dfb"></p></div>'
 '<div class="sblok"><h3>④ El acento llano · de meeste woorden</h3>'
 '<p class="sh">La <b>mayoría</b> de las palabras españolas son <i>llanas</i>: el acento cae en la <b>penúltima</b> sílaba. Pulsa 🔊 y repite. <span class="gloss">meeste woorden: klemtoon voorlaatste</span></p>'
 f'<div class="shrow">{"".join(acchip(*a) for a in ACENTO)}</div></div>'
 '</div>')

CSS=FONTS+r"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--card:#fff;
--p:#2563EB;--v:#EA7317;--pl:#0E9E97;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif}
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
.p{color:var(--p);font-weight:700}.v{color:var(--v);font-weight:700}.pl{color:var(--pl);font-weight:700}
.gcard{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:14px 0}
.gcard.soft{background:var(--crema)}
.gcard h3{font-family:var(--disp);margin:0 0 6px;font-size:18px}
.gp{margin:0 0 10px;font-size:14px;color:var(--ink)}
.gt{border-collapse:collapse;width:100%;font-size:14.5px}
.gt td{border-bottom:1px solid var(--line);padding:7px 10px}
.gt td.p{color:var(--p);font-weight:600;font-family:var(--disp)}.gt td.ex{color:var(--mut);font-style:italic}
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
.di-lines div{display:flex;gap:8px;align-items:baseline}.di-lines span{font-size:12px;color:var(--mut);width:64px}
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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U4 · Kit · Gramática · Tarea</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 4 · La familia</h1><p>De <b>kit de supervivencia</b> (familie voorstellen &amp; beschrijven), een korte <b>uitlegnota</b> waar het helpt, en je <b>eindtaak</b>. Klik 🔊 om woorden te horen.</p></div>
<main>
 <h2 class="subh">🔊 Suena bien <small>uitspraak — de ll, de y (yeísmo) &amp; de klemtoon (llana)</small></h2>
 {SUENA}
 <h2 class="subh">§2 · Kit de supervivencia <small>de chunks per situatie — klik om te horen</small></h2>
 {KIT}
 <h2 class="subh">§4 · Gramática en la práctica <small>kort en functioneel — geen theorie om de theorie</small></h2>
 {GRAM}
 <h2 class="subh">§5 · Tarea final <small>jouw communicatieve opdracht</small></h2>
 {TAREA}
 <div class="foot">C4 · «Bienvenidos al español» · Unidad 4 · La familia</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.cc').forEach(function(c){{var es=c.getAttribute('data-es').replace(/·.*/,'').replace(/[…?¿!¡]/g,'');c.onclick=function(){{speak(es);}};}});
document.querySelectorAll('.shchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));}};}});
var dtot=document.querySelectorAll('.dchip[data-ok="1"]').length;
document.querySelectorAll('.dchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));var ok=b.getAttribute('data-ok')==='1';b.classList.remove('ok','no');b.classList.add(ok?'ok':'no');var n=document.querySelectorAll('.dchip.ok').length;var fb=document.getElementById('dfb');fb.textContent=ok?('¡Con ll/y! /ʝ/ · '+n+'/'+dtot+' 👏'):'Esa no tiene ll/y. Prueba otra.';}};}});
</script></body></html>"""
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U4_kgt.html","w").write(HTML)
print("C4_U4_kgt.html geschreven:",len(HTML),"bytes")
