#!/usr/bin/env python3
# C4 · Unidad 8 — §3 PRÁCTICA (native, zelfcorrigerend). La hora y los días · es la/son las · a las · quedar.
import base64, os
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

CSS=FONTS+"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--red:#DC2626;--card:#fff;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#181513;--crema:#241C1B;--gt:#3A1E20;--line:#3a302e;--card:#211a19}
*{box-sizing:border-box}body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
.top{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;padding:22px 22px}
.top h1{font-family:var(--disp);font-weight:800;margin:0;font-size:26px}.top p{margin:5px 0 0;opacity:.95;max-width:720px}
main{max-width:1000px;margin:0 auto;padding:18px}
.subh{font-family:var(--disp);color:var(--ink);font-size:18px;margin:24px 0 6px;padding-bottom:5px;border-bottom:2px solid var(--gt);display:flex;gap:10px;align-items:center}
.pill{display:inline-block;background:var(--gt);color:var(--gd);border-radius:20px;padding:3px 10px;font-size:12px;font-weight:700}
.game{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin:14px 0}
.game h3{font-family:var(--disp);margin:0 0 2px;color:var(--ink);font-size:18px}.game .desc{color:var(--mut);font-size:13px;margin:0 0 12px}
.scorebar{display:flex;gap:14px;font-size:13px;color:var(--mut);margin-bottom:10px}.scorebar b{color:var(--gd)}
.chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{border:1.5px solid var(--line);background:var(--card);border-radius:12px;padding:9px 14px;font-weight:600;cursor:pointer;font-size:15px;user-select:none}
.chip.sel{border-color:var(--g);background:var(--gt)}.chip.ok{border-color:var(--g);background:var(--g);color:#fff}.chip.no{border-color:var(--red);background:#fde8e8}
.fb{margin-top:12px;padding:10px 14px;border-radius:10px;font-size:14px;display:none}.fb.good{display:block;background:var(--gt);color:var(--gd)}.fb.bad{display:block;background:#fdeaea;color:var(--red)}
.spk-btn{border:none;background:var(--gt);color:var(--gd);border-radius:10px;padding:9px 15px;font-weight:700;cursor:pointer;font-size:15px}
.txin{border:1.5px solid var(--line);border-radius:10px;padding:7px 10px;font-size:15px;background:var(--card);color:var(--ink);font-family:var(--disp);width:120px}
select.txin{width:auto}
.answerbtns{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}
.btn{border:none;background:var(--g);color:#fff;font-weight:700;border-radius:10px;padding:8px 14px;cursor:pointer;font-family:var(--disp);font-size:14px}
.btn.sec{background:var(--crema);color:var(--ink)}
.col{border:1.5px dashed var(--line);border-radius:12px;padding:10px;min-height:60px;margin-top:8px}
.fcgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
.fc{perspective:900px;height:110px;cursor:pointer}.fc .in{position:relative;width:100%;height:100%;transition:transform .5s;transform-style:preserve-3d}
.fc.flip .in{transform:rotateY(180deg)}.fc .s,.fc .b{position:absolute;inset:0;backface-visibility:hidden;border-radius:14px;border:1px solid var(--line);background:var(--card);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:8px;text-align:center}
.fc .s{border-top:4px solid var(--g)}.fc .b{transform:rotateY(180deg);background:var(--gt);border-top:4px solid var(--gd)}
.fc .w{font-family:var(--disp);font-weight:700;font-size:16px}.fc .tr{font-family:var(--disp);font-weight:700;font-size:15px;color:var(--gd)}
.dlgfill{font-size:15.5px;line-height:2.4}.dlgfill .txin{width:130px}
.wbox{border:1px solid var(--line);border-radius:10px;background:var(--crema);min-height:60px;padding:8px;margin-top:8px}
.bigclock{font-family:var(--disp);font-size:40px;font-weight:800;color:var(--gd);text-align:center;margin:6px 0;letter-spacing:1px}
.foot{color:var(--mut);font-size:12px;text-align:center;margin:24px 0}
"""

HTML="""<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U8 · Práctica</title><style>__CSS__</style></head><body>
<div class="top"><h1>Unidad 8 · Las horas — Práctica</h1><p>Practica la lengua útil de la escena: de <b>reconocer</b> → <b>elegir</b> → <b>decirlo y escribirlo tú</b>. Todo se corrige solo; pulsa 🔊 para oírlo. <span class="stn">van herkennen naar zelf zeggen</span></p></div>
<main>
 <h2 class="subh">① Reconocer <span class="pill">receptief</span></h2>
 <div class="game" id="g_cards"></div>
 <div class="game" id="g_escucha"></div>
 <div class="game" id="g_clasifica"></div>
 <h2 class="subh">② Practicar <span class="pill">gestuurd</span></h2>
 <div class="game" id="g_reloj"></div>
 <div class="game" id="g_esson"></div>
 <div class="game" id="g_dias"></div>
 <div class="game" id="g_completa"></div>
 <div class="game" id="g_ordena"></div>
 <h2 class="subh">③ Producir &amp; comunicar <span class="pill">vrije productie</span></h2>
 <div class="game" id="g_quedar"></div>
 <div class="foot">C4 · «Bienvenidos al español» · Unidad 8 · La hora y los días</div>
</main>
<script>__JS__</script></body></html>"""

JS=r"""
function speak(t){if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(x=>/^es/i.test(x.lang));if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}
var TTS=('speechSynthesis'in window);if(TTS)speechSynthesis.getVoices();
function sb(id){return '<div class="scorebar" id="'+id+'"><span>Punten: <b class="pt">0</b></span><span>Reeks: <b class="st">0</b></span></div>'}
function setSc(el,p,s){el.querySelector('.pt').textContent=p;el.querySelector('.st').textContent=s}
function fb(el,ok,m){el.className='fb '+(ok?'good':'bad');el.innerHTML=(ok?'✅ ':'❌ ')+m}

var CHUNKS=[["¿Qué hora es?","hoe laat is het?"],["Es la una","het is één uur"],["Son las ocho","het is acht uur"],["y cuarto","kwart over"],["y media","half (…+30)"],["menos cuarto","kwart voor"],["en punto","precies"],["¿A qué hora?","hoe laat?"],["lunes","maandag"],["miércoles","woensdag"],["sábado","zaterdag"],["domingo","zondag"],["el fin de semana","het weekend"],["por la mañana","'s ochtends"],["esta noche","vanavond"],["¿Quieres quedar?","wil je afspreken?"],["Quedamos a las…","we spreken af om…"],["Hasta ahora","tot straks"]];

(function(){var el=document.getElementById('g_cards');el.innerHTML='<h3>Tarjetas 🗂️</h3><p class="desc">Draai de kaart (ES↔NL); klik 🔊 om te horen.</p><div class="fcgrid" id="cg"></div>';
 var g=el.querySelector('#cg');CHUNKS.forEach(function(c){var d=document.createElement('div');d.className='fc';d.innerHTML='<div class="in"><div class="s"><div class="w">'+c[0]+'</div>'+(TTS?'<div style="font-size:12px;opacity:.5;margin-top:4px">🔊</div>':'')+'</div><div class="b"><div class="tr">'+c[1]+'</div></div></div>';
  d.onclick=function(){d.classList.toggle('flip');};if(TTS)d.querySelector('.s').addEventListener('click',function(e){e.stopPropagation();speak(c[0].replace('…','').replace(/[¿?]/g,''));d.classList.toggle('flip');});g.appendChild(d);});})();

// ① ¿Qué hora oyes? (luister → kies de klok)
(function(){var el=document.getElementById('g_escucha');if(!TTS){el.innerHTML='<h3>¿Qué hora oyes? 🎧</h3><p class="desc">Spraak werkt in Chrome/Edge.</p>';return;}
 var bank=[["Es la una","1.00"],["Son las dos y media","2.30"],["Son las cinco y cuarto","5.15"],["Son las ocho menos cuarto","7.45"],["Son las once en punto","11.00"],["Son las nueve y diez","9.10"],["Son las tres y media","3.30"],["Son las doce y cuarto","12.15"]];
 var p=0,s=0;
 el.innerHTML='<h3>¿Qué hora oyes? 🎧</h3><p class="desc">Klik ▶, luister en kies het juiste uur (cijfers).</p>'+sb('sbE')+'<div style="margin:6px 0"><button class="spk-btn" id="eP">▶ Speel af</button></div><div class="chips" id="eO"></div><div class="fb" id="eF"></div>';
 var bar=el.querySelector('#sbE');function nx(){var a=bank[Math.floor(Math.random()*bank.length)];el.cur=a;var o=[a];while(o.length<4){var c=bank[Math.floor(Math.random()*bank.length)];if(o.indexOf(c)<0)o.push(c);}o.sort(()=>Math.random()-.5);var oc=el.querySelector('#eO');oc.innerHTML='';o.forEach(function(x){var c=document.createElement('div');c.className='chip';c.textContent=x[1];c.onclick=function(){var ok=x[1]===a[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);oc.querySelectorAll('.chip').forEach(function(z){if(z.textContent===a[1])z.classList.add('ok');else if(z===c&&!ok)z.classList.add('no');});fb(el.querySelector('#eF'),ok,'«'+a[0]+'» = '+a[1]);setTimeout(nx,1200);};oc.appendChild(c);});el.querySelector('#eF').className='fb';speak(a[0]);}
 el.querySelector('#eP').onclick=function(){if(el.cur)speak(el.cur[0]);};nx();})();

// ① Clasifica (hora / día / momento del día)
(function(){var el=document.getElementById('g_clasifica');
 var items=[["y media","hora"],["menos cuarto","hora"],["en punto","hora"],["martes","día"],["domingo","día"],["el fin de semana","día"],["por la mañana","momento"],["esta noche","momento"],["más tarde","momento"]];
 var cat={"hora":"la hora 🕐","día":"el día 📅","momento":"momento del día 🌗"};var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>Clasifica 🎯</h3><p class="desc">¿Es una hora, un día o un momento del día? <span class="stn">uur, dag of moment?</span></p>'+sb('sbC')+'<div id="cw" style="font-size:24px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" id="cc" style="justify-content:center"></div><div class="fb" id="cf"></div>';
 var bar=el.querySelector('#sbC'),cc=el.querySelector('#cc');Object.keys(cat).forEach(function(k){var c=document.createElement('div');c.className='chip';c.textContent=cat[k];c.onclick=function(){g(k);};cc.appendChild(c);});
 function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#cw').textContent=el.cur[0];el.querySelector('#cf').className='fb';}
 function g(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);fb(el.querySelector('#cf'),ok,'«'+el.cur[0]+'» → '+cat[el.cur[1]]);setTimeout(nx,900);}nx();})();

// ② Del reloj a las palabras (digitaal → Spaans)
(function(){var el=document.getElementById('g_reloj');
 var items=[["1:00","Es la una"],["3:30","Son las tres y media"],["6:15","Son las seis y cuarto"],["8:45","Son las nueve menos cuarto"],["10:00","Son las diez en punto"],["2:10","Son las dos y diez"],["8:30","Son las ocho y media"]];
 var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>Del reloj a las palabras 🕐</h3><p class="desc">Kijk naar de klok en kies de juiste Spaanse zin. ⚠️ Let op «half»!</p>'+sb('sbR')+'<div class="bigclock" id="rw"></div><div class="chips" id="ro" style="justify-content:center"></div><div class="fb" id="rf"></div>';
 var bar=el.querySelector('#sbR');
 function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#rw').textContent=el.cur[0];
  var o=[el.cur[1]];while(o.length<3){var c=items[Math.floor(Math.random()*items.length)][1];if(o.indexOf(c)<0)o.push(c);}o.sort(()=>Math.random()-.5);
  var ro=el.querySelector('#ro');ro.innerHTML='';o.forEach(function(x){var c=document.createElement('div');c.className='chip';c.textContent=x;c.onclick=function(){var ok=x===el.cur[1];if(ok){p++;s++;if(TTS)speak(x)}else s=0;setSc(bar,p,s);fb(el.querySelector('#rf'),ok,el.cur[0]+' → «'+el.cur[1]+'»');setTimeout(nx,1200);};ro.appendChild(c);});
  el.querySelector('#rf').className='fb';}
 nx();})();

// ② ¿es la o son las?
(function(){var el=document.getElementById('g_esson');
 var items=[["___ una y cuarto","es la"],["___ siete","son las"],["___ doce en punto","son las"],["___ una en punto","es la"],["___ cuatro y media","son las"],["___ dos menos cuarto","son las"]];
 var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>¿es la o son las? ⚖️</h3><p class="desc">Alleen 1 uur is enkelvoud (es la una). Kies.</p>'+sb('sbS')+'<div id="sw" style="font-size:22px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._es(\'es la\')">es la</div><div class="chip" onclick="window._es(\'son las\')">son las</div></div><div class="fb" id="sf"></div>';
 var bar=el.querySelector('#sbS');function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#sw').textContent=el.cur[0];el.querySelector('#sf').className='fb';}
 window._es=function(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);var frase=el.cur[0].replace('___',el.cur[1]);fb(el.querySelector('#sf'),ok,frase);if(TTS&&ok)speak(frase);setTimeout(nx,1000);};nx();})();

// ② Ordena los días de la semana
(function(){var el=document.getElementById('g_dias');
 var sol=["lunes","martes","miércoles","jueves","viernes","sábado","domingo"];
 var cur=[],pool=sol.slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>Ordena los días 📅</h3><p class="desc">Klik de dagen in de juiste volgorde (maandag eerst).</p><div class="chips" id="dP"></div><div class="col" id="dB"><b style="font-size:12px;color:var(--gd)">JOUW VOLGORDE</b><div class="chips" id="dBB" style="margin-top:6px"></div></div><div class="answerbtns"><button class="btn sec" id="dR">Reset</button><button class="btn" id="dC">Controleer</button></div><div class="fb" id="dF"></div>';
 function draw(){var p=el.querySelector('#dP');p.innerHTML='';pool.forEach(function(t,i){var c=document.createElement('div');c.className='chip';c.textContent=t;c.onclick=function(){cur.push(t);pool.splice(i,1);draw();built();if(TTS)speak(t);};p.appendChild(c);});}
 function built(){var b=el.querySelector('#dBB');b.innerHTML='';cur.forEach(function(t,i){var c=document.createElement('div');c.className='chip sel';c.textContent=(i+1)+'. '+t;c.onclick=function(){pool.push(t);cur.splice(i,1);draw();built();};b.appendChild(c);});}
 el.querySelector('#dC').onclick=function(){var ok=cur.join('|')===sol.join('|');fb(el.querySelector('#dF'),ok,ok?'¡Perfecto! lunes → domingo':'Todavía no — empieza por lunes.');};
 el.querySelector('#dR').onclick=function(){cur=[];pool=sol.slice().sort(()=>Math.random()-.5);draw();built();el.querySelector('#dF').className='fb';};draw();built();})();

// ② Completa el diálogo
(function(){var el=document.getElementById('g_completa');
 var gaps=[["quedar"],["hora"],["las"],["media"],["ahora"]];
 el.innerHTML='<h3>Completa el diálogo 💬</h3><p class="desc">Completa (quedar · hora · las · media · ahora). <span class="gloss">vul aan</span></p>'
  +'<div class="dlgfill">— ¿Quieres <input class="txin" data-i="0"> esta noche? <br>— Sí, vale. ¿A qué <input class="txin" data-i="1">? <br>— ¿A <input class="txin" data-i="2"> nueve?<br>— Mejor a las nueve y <input class="txin" data-i="3"> <span style="color:var(--mut);font-size:12px">(9.30)</span>.<br>— Perfecto. ¡Hasta <input class="txin" data-i="4">!</div>'
  +'<div class="answerbtns"><button class="btn" id="coGo">Controleer</button></div><div class="fb" id="coF"></div>';
 el.querySelector('#coGo').onclick=function(){var n=0;el.querySelectorAll('.txin').forEach(function(inp){var i=+inp.dataset.i;var ok=(inp.value||'').trim().toLowerCase()===gaps[i][0].toLowerCase();inp.style.borderColor=ok?'#2F9A4A':'#DC2626';if(ok)n++;});fb(el.querySelector('#coF'),n===gaps.length,n+' / '+gaps.length+' juist.'+(n<gaps.length?' Kijk naar de rode vakjes.':' ¡Perfecto!'));};})();

// ② Ordena la conversación (quedar)
(function(){var el=document.getElementById('g_ordena');
 var sol=["¿Quieres quedar esta tarde?","Sí, ¿a qué hora?","¿A las seis?","A las seis no puedo, mejor a las siete y media.","Vale, quedamos en el cine."];
 var cur=[],pool=sol.slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>Ordena la conversación 🔢</h3><p class="desc">Klik de zinnen in de juiste volgorde.</p><div class="chips" id="oP"></div><div class="col" id="oB"><b style="font-size:12px;color:var(--gd)">JOUW VOLGORDE</b><div class="chips" id="oBB" style="margin-top:6px"></div></div><div class="answerbtns"><button class="btn sec" id="oR">Reset</button><button class="btn" id="oC">Controleer</button></div><div class="fb" id="oF"></div>';
 function draw(){var p=el.querySelector('#oP');p.innerHTML='';pool.forEach(function(t,i){var c=document.createElement('div');c.className='chip';c.textContent=t;c.onclick=function(){cur.push(t);pool.splice(i,1);draw();built();};p.appendChild(c);});}
 function built(){var b=el.querySelector('#oBB');b.innerHTML='';cur.forEach(function(t,i){var c=document.createElement('div');c.className='chip sel';c.textContent=(i+1)+'. '+t;c.onclick=function(){pool.push(t);cur.splice(i,1);draw();built();};b.appendChild(c);});}
 el.querySelector('#oC').onclick=function(){var ok=cur.join('|')===sol.join('|');fb(el.querySelector('#oF'),ok,ok?'¡Perfecto!':'Todavía no — empieza por «¿Quieres quedar…?».');};
 el.querySelector('#oR').onclick=function(){cur=[];pool=sol.slice().sort(()=>Math.random()-.5);draw();built();el.querySelector('#oF').className='fb';};draw();built();})();

// ③ Queda conmigo (vrije productie)
(function(){var el=document.getElementById('g_quedar');
 el.innerHTML='<h3>Queda conmigo ✍️🗣️</h3><p class="desc">Haz tu propia cita. No hay respuesta «correcta»: es tu semana. <span class="stn">het is jouw week</span></p>'
  +'<div style="display:grid;gap:8px;max-width:640px"><div><span style="font-family:var(--disp)">¿Quieres quedar</span> <select class="txin" id="p1"><option>el lunes</option><option>el miércoles</option><option>el viernes</option><option>el sábado</option><option>esta noche</option></select> <span style="font-family:var(--disp)">? Quedamos a</span> <select class="txin" id="p2"><option>la una</option><option>las cuatro</option><option>las seis y media</option><option>las ocho menos cuarto</option></select> <span style="font-family:var(--disp)">en</span> <input class="txin" id="p3" placeholder="el cine / mi casa…" style="width:150px"> <span style="font-family:var(--disp)">.</span></div></div>'
  +'<div class="answerbtns"><button class="btn" id="pGo">Maak mijn afspraak</button>'+(TTS?'<button class="spk-btn" id="pSpk">🔊 hoor</button>':'')+'</div><div class="fb" id="pF"></div>';
 el.querySelector('#pGo').onclick=function(){var d=el.querySelector('#p1').value,h=el.querySelector('#p2').value,l=(el.querySelector('#p3').value||'el cine').trim();el.cur='¿Quieres quedar '+d+'? Quedamos a '+h+' en '+l+'.';fb(el.querySelector('#pF'),true,'<b>'+el.cur+'</b><br><span style="color:var(--mut);font-style:italic">Zeg het nu hardop tegen je buur — hij/zij antwoordt «Vale» of «A esa hora no puedo».</span>');};
 var sp=el.querySelector('#pSpk');if(sp)sp.onclick=function(){if(el.cur)speak(el.cur);};})();
"""

html=HTML.replace("__CSS__",CSS).replace("__JS__",JS)
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U8_practica.html","w").write(html)
print("C4_U8_practica.html geschreven:",len(html),"bytes")
