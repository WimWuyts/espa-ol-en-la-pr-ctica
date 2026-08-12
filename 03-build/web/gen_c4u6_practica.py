#!/usr/bin/env python3
# C4 · Unidad 6 — §3 PRÁCTICA (native, zelfcorrigerend). La casa · preposiciones · dónde está · poder.
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
.foot{color:var(--mut);font-size:12px;text-align:center;margin:24px 0}
"""

HTML="""<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U6 · Práctica</title><style>__CSS__</style></head><body>
<div class="top"><h1>Unidad 6 · La casa — Práctica</h1><p>Oefen de bruikbare taal uit de scène: van <b>herkennen</b> → <b>kiezen</b> → <b>zelf zeggen/schrijven</b>. Alles corrigeert zichzelf; klik 🔊 om te horen.</p></div>
<main>
 <h2 class="subh">① Reconocer <span class="pill">receptief</span></h2>
 <div class="game" id="g_cards"></div>
 <div class="game" id="g_escucha"></div>
 <div class="game" id="g_clasifica"></div>
 <h2 class="subh">② Practicar <span class="pill">gestuurd</span></h2>
 <div class="game" id="g_match"></div>
 <div class="game" id="g_completa"></div>
 <div class="game" id="g_ordena"></div>
 <div class="game" id="g_hayesta"></div>
 <div class="game" id="g_poder"></div>
 <h2 class="subh">③ Producir &amp; comunicar <span class="pill">vrije productie</span></h2>
 <div class="game" id="g_describe"></div>
 <div class="foot">C4 · «Bienvenidos al español» · Unidad 6 · La casa y los lugares</div>
</main>
<script>__JS__</script></body></html>"""

JS=r"""
function speak(t){if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(x=>/^es/i.test(x.lang));if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}
var TTS=('speechSynthesis'in window);if(TTS)speechSynthesis.getVoices();
function sb(id){return '<div class="scorebar" id="'+id+'"><span>Punten: <b class="pt">0</b></span><span>Reeks: <b class="st">0</b></span></div>'}
function setSc(el,p,s){el.querySelector('.pt').textContent=p;el.querySelector('.st').textContent=s}
function fb(el,ok,m){el.className='fb '+(ok?'good':'bad');el.innerHTML=(ok?'✅ ':'❌ ')+m}

var CHUNKS=[["la cocina","de keuken"],["el salón","de woonkamer"],["el dormitorio","de slaapkamer"],["el cuarto de baño","de badkamer"],["la cama","het bed"],["el armario","de kast"],["el frigorífico","de koelkast"],["encima de","op/boven"],["debajo de","onder"],["dentro de","in/binnen"],["al lado de","naast"],["delante de","voor"],["detrás de","achter"],["¿Dónde está?","waar is?"],["¿Puedo…?","mag ik…?"],["puedes ir fuera","je mag naar buiten"],["hay","er is/zijn"]];

(function(){var el=document.getElementById('g_cards');el.innerHTML='<h3>Tarjetas 🗂️</h3><p class="desc">Draai de kaart (ES↔NL); klik 🔊 om te horen.</p><div class="fcgrid" id="cg"></div>';
 var g=el.querySelector('#cg');CHUNKS.forEach(function(c){var d=document.createElement('div');d.className='fc';d.innerHTML='<div class="in"><div class="s"><div class="w">'+c[0]+'</div>'+(TTS?'<div style="font-size:12px;opacity:.5;margin-top:4px">🔊</div>':'')+'</div><div class="b"><div class="tr">'+c[1]+'</div></div></div>';
  d.onclick=function(){d.classList.toggle('flip');};if(TTS)d.querySelector('.s').addEventListener('click',function(e){e.stopPropagation();speak(c[0].replace('…','').replace(/[¿?]/g,''));d.classList.toggle('flip');});g.appendChild(d);});})();

(function(){var el=document.getElementById('g_escucha');if(!TTS){el.innerHTML='<h3>¿Qué oyes? 🎧</h3><p class="desc">Spraak werkt in Chrome/Edge.</p>';return;}
 var bank=["cocina","salón","dormitorio","baño","cama","armario","sofá","mesa","ventana","puerta","cocina","pasillo","entrada","frigorífico"];var p=0,s=0;
 el.innerHTML='<h3>¿Qué oyes? 🎧</h3><p class="desc">Klik ▶, luister en kies de kamer of het meubel dat je hoort.</p>'+sb('sbE')+'<div style="margin:6px 0"><button class="spk-btn" id="eP">▶ Speel af</button></div><div class="chips" id="eO"></div><div class="fb" id="eF"></div>';
 var bar=el.querySelector('#sbE');function nx(){var a=bank[Math.floor(Math.random()*bank.length)];el.cur=a;var o=[a];while(o.length<4){var c=bank[Math.floor(Math.random()*bank.length)];if(o.indexOf(c)<0)o.push(c);}o.sort(()=>Math.random()-.5);var oc=el.querySelector('#eO');oc.innerHTML='';o.forEach(function(x){var c=document.createElement('div');c.className='chip';c.textContent=x;c.onclick=function(){var ok=x===a;if(ok){p++;s++}else s=0;setSc(bar,p,s);oc.querySelectorAll('.chip').forEach(function(z){if(z.textContent===a)z.classList.add('ok');else if(z===c&&!ok)z.classList.add('no');});fb(el.querySelector('#eF'),ok,'«'+a+'»');setTimeout(nx,1100);};oc.appendChild(c);});el.querySelector('#eF').className='fb';speak(a);}
 el.querySelector('#eP').onclick=function(){speak(el.cur);};nx();})();

// ① Clasifica (habitación / mueble / posición)
(function(){var el=document.getElementById('g_clasifica');
 var items=[["la cocina","habitación"],["el salón","habitación"],["el dormitorio","habitación"],["la cama","mueble"],["el sofá","mueble"],["el armario","mueble"],["encima de","posición"],["debajo de","posición"],["al lado de","posición"]];
 var cat={"habitación":"habitación 🏠","mueble":"mueble 🛋️","posición":"posición 📍"};var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>Clasifica 🎯</h3><p class="desc">Is het een kamer, een meubel of een plaats-woord?</p>'+sb('sbC')+'<div id="cw" style="font-size:24px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" id="cc" style="justify-content:center"></div><div class="fb" id="cf"></div>';
 var bar=el.querySelector('#sbC'),cc=el.querySelector('#cc');Object.keys(cat).forEach(function(k){var c=document.createElement('div');c.className='chip';c.textContent=cat[k];c.onclick=function(){g(k);};cc.appendChild(c);});
 function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#cw').textContent=el.cur[0];el.querySelector('#cf').className='fb';}
 function g(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);fb(el.querySelector('#cf'),ok,'«'+el.cur[0]+'» → '+cat[el.cur[1]]);setTimeout(nx,900);}nx();})();

// ② Match habitación ↔ ¿qué hacemos ahí?
(function(){var el=document.getElementById('g_match');
 var pairs=[["la cocina","cocinar y comer"],["el dormitorio","dormir"],["el cuarto de baño","ducharse"],["el salón","ver la tele"],["la entrada","entrar en casa"]];
 var p=0,s=0,sel=null,done=0;var L=pairs.map(x=>x[0]),R=pairs.map(x=>x[1]).slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>Relaciona · ¿qué hacemos ahí? 🧩</h3><p class="desc">Klik links een kamer, dan rechts wat je er doet.</p>'+sb('sbM')+'<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px"><div class="chips" style="flex-direction:column" id="mL"></div><div class="chips" style="flex-direction:column" id="mR"></div></div><div class="fb" id="mf"></div>';
 var bar=el.querySelector('#sbM'),cL=el.querySelector('#mL'),cR=el.querySelector('#mR');
 L.forEach(function(t,i){var c=document.createElement('div');c.className='chip';c.textContent=t;c.dataset.i=i;c.onclick=function(){cL.querySelectorAll('.chip').forEach(z=>z.classList.remove('sel'));c.classList.add('sel');sel=i;};cL.appendChild(c);});
 R.forEach(function(t){var c=document.createElement('div');c.className='chip';c.textContent=t;c.onclick=function(){if(sel==null)return;var ok=t===pairs[sel][1];if(ok){c.classList.add('ok');cL.querySelector('.chip[data-i="'+sel+'"]').classList.add('ok');p++;s++;done++;fb(el.querySelector('#mf'),true,pairs[sel][0]+' → '+t);if(done===pairs.length)fb(el.querySelector('#mf'),true,'¡Completado!');}else{s=0;c.classList.add('no');setTimeout(()=>c.classList.remove('no'),500);fb(el.querySelector('#mf'),false,'Probeer opnieuw.');}setSc(bar,p,s);sel=null;cL.querySelectorAll('.chip').forEach(z=>z.classList.remove('sel'));};cR.appendChild(c);});})();

// ② Completa el diálogo
(function(){var el=document.getElementById('g_completa');
 var gaps=[["está"],["Está"],["debajo"],["puedes"]];
 el.innerHTML='<h3>Completa el diálogo 💬</h3><p class="desc">Completa (está · debajo · puedes). <span class="gloss">vul aan</span></p>'
  +'<div class="dlgfill">— ¿Dónde <input class="txin" data-i="0"> mi bolso? <br>— <input class="txin" data-i="1"> encima del sofá. <br>— ¿Y las llaves?<br>— Están <input class="txin" data-i="2"> de la mesa <span style="color:var(--mut);font-size:12px">(onder)</span>.<br>— ¿Puedo mirar en la cocina?<br>— Sí, <input class="txin" data-i="3">.</div>'
  +'<div class="answerbtns"><button class="btn" id="coGo">Controleer</button></div><div class="fb" id="coF"></div>';
 el.querySelector('#coGo').onclick=function(){var n=0;el.querySelectorAll('.txin').forEach(function(inp){var i=+inp.dataset.i;var ok=(inp.value||'').trim().toLowerCase()===gaps[i][0].toLowerCase();inp.style.borderColor=ok?'#2F9A4A':'#DC2626';if(ok)n++;});fb(el.querySelector('#coF'),n===gaps.length,n+' / '+gaps.length+' juist.'+(n<gaps.length?' Kijk naar de rode vakjes.':' ¡Perfecto!'));};})();

// ② Ordena la conversación
(function(){var el=document.getElementById('g_ordena');
 var sol=["¿Dónde está mi bolso?","Está en el salón.","¿Encima del sofá?","No, debajo de la mesa.","¡Ah, gracias!"];
 var cur=[],pool=sol.slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>Ordena la conversación 🔢</h3><p class="desc">Klik de zinnen in de juiste volgorde.</p><div class="chips" id="oP"></div><div class="col" id="oB"><b style="font-size:12px;color:var(--gd)">JOUW VOLGORDE</b><div class="chips" id="oBB" style="margin-top:6px"></div></div><div class="answerbtns"><button class="btn sec" id="oR">Reset</button><button class="btn" id="oC">Controleer</button></div><div class="fb" id="oF"></div>';
 function draw(){var p=el.querySelector('#oP');p.innerHTML='';pool.forEach(function(t,i){var c=document.createElement('div');c.className='chip';c.textContent=t;c.onclick=function(){cur.push(t);pool.splice(i,1);draw();built();};p.appendChild(c);});}
 function built(){var b=el.querySelector('#oBB');b.innerHTML='';cur.forEach(function(t,i){var c=document.createElement('div');c.className='chip sel';c.textContent=(i+1)+'. '+t;c.onclick=function(){pool.push(t);cur.splice(i,1);draw();built();};b.appendChild(c);});}
 el.querySelector('#oC').onclick=function(){fb(el.querySelector('#oF'),cur.join('|')===sol.join('|'),cur.join('|')===sol.join('|')?'¡Perfecto!':'Nog niet — begin met de vraag «¿Dónde está…?».');};
 el.querySelector('#oR').onclick=function(){cur=[];pool=sol.slice().sort(()=>Math.random()-.5);draw();built();el.querySelector('#oF').className='fb';};draw();built();})();

// ② ¿hay o está?
(function(){var el=document.getElementById('g_hayesta');
 var items=[["En el salón ___ un sofá.","hay"],["El bolso ___ encima de la mesa.","está"],["¿___ un frigorífico en la cocina?","hay"],["Mi libro ___ debajo de la cama.","está"],["¿Qué ___ en tu dormitorio?","hay"],["La cocina ___ al lado del salón.","está"]];
 var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>¿hay o está? 🔎</h3><p class="desc">hay = er is iets (nieuw) · está = waar dat bekende ding staat. Kies.</p>'+sb('sbH')+'<div id="hw" style="font-size:19px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._he(\'hay\')">hay</div><div class="chip" onclick="window._he(\'está\')">está</div></div><div class="fb" id="hf"></div>';
 var bar=el.querySelector('#sbH');function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#hw').textContent=el.cur[0];el.querySelector('#hf').className='fb';}
 window._he=function(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);fb(el.querySelector('#hf'),ok,el.cur[0].replace('___',el.cur[1]));setTimeout(nx,1000);};nx();})();

// ② ¿puedo o puedes?
(function(){var el=document.getElementById('g_poder');
 var items=[["¿___ fumar aquí? (ik vraag)","puedo"],["Sí, ___ ir fuera. (jij mag)","puedes"],["¿___ venir conmigo? (jij)","puedes"],["¿___ abrir la ventana? (ik)","puedo"],["Aquí no ___ comer. (jij)","puedes"]];
 var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>¿puedo o puedes? 🙋</h3><p class="desc">puedo = ik · puedes = jij. Elige la forma correcta. <span class="gloss">Kies de juiste vorm.</span></p>'+sb('sbP')+'<div id="pw" style="font-size:18px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._pd(\'puedo\')">puedo (ik)</div><div class="chip" onclick="window._pd(\'puedes\')">puedes (jij)</div></div><div class="fb" id="pf"></div>';
 var bar=el.querySelector('#sbP');function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#pw').textContent=el.cur[0];el.querySelector('#pf').className='fb';}
 window._pd=function(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);fb(el.querySelector('#pf'),ok,el.cur[0].replace('___',el.cur[1]));setTimeout(nx,1000);};nx();})();

// ③ Describe tu casa (vrije productie)
(function(){var el=document.getElementById('g_describe');
 el.innerHTML='<h3>Describe tu casa ✍️🗣️</h3><p class="desc">Zeg in welke kamer wat staat en waar. Er is geen «juist» — het is jouw huis.</p>'
  +'<div style="display:grid;gap:8px;max-width:620px"><div><span style="font-family:var(--disp)">En mi</span> <select class="txin" id="p1"><option>salón</option><option>cocina</option><option>dormitorio</option><option>cuarto de baño</option></select> <span style="font-family:var(--disp)">hay</span> <input class="txin" id="p2" placeholder="un sofá / una cama…"> <span style="font-family:var(--disp)">. Está</span> <select class="txin" id="p3"><option>al lado de</option><option>encima de</option><option>debajo de</option><option>delante de</option><option>detrás de</option></select> <input class="txin" id="p4" placeholder="la ventana…" style="width:120px"> <span style="font-family:var(--disp)">.</span></div></div>'
  +'<div class="answerbtns"><button class="btn" id="pGo">Maak mijn zin</button>'+(TTS?'<button class="spk-btn" id="pSpk">🔊 hoor</button>':'')+'</div><div class="fb" id="pF"></div>';
 el.querySelector('#pGo').onclick=function(){var r=el.querySelector('#p1').value,o=(el.querySelector('#p2').value||'un sofá').trim(),pr=el.querySelector('#p3').value,w=(el.querySelector('#p4').value||'la ventana').trim();el.cur='En mi '+r+' hay '+o+'. Está '+pr+' '+w+'.';fb(el.querySelector('#pF'),true,'<b>'+el.cur+'</b><br><span style="color:var(--mut);font-style:italic">Zeg het nu hardop tegen je buur — wijs op je plattegrond.</span>');};
 var sp=el.querySelector('#pSpk');if(sp)sp.onclick=function(){if(el.cur)speak(el.cur);};})();
"""

html=HTML.replace("__CSS__",CSS).replace("__JS__",JS)
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U6_practica.html","w").write(html)
print("C4_U6_practica.html geschreven:",len(html),"bytes")
