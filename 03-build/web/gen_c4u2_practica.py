#!/usr/bin/env python3
# C4 · Unidad 2 — §3 PRÁCTICA (native, zelfcorrigerend). Oefeningen op de chunks/woordenschat
# uit de scène (saludos por el día · estar + estado · cortesía · despedidas — functioneel).
# Receptief → gestuurd → productief. C4-rood, TTS, motor-vrij standalone. Zelfde pijplijn als U1.
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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U2 · Práctica</title><style>__CSS__</style></head><body>
<div class="top"><h1>Unidad 2 · Saludos — Práctica</h1><p>Oefen de bruikbare taal uit de scène: van <b>herkennen</b> → <b>kiezen</b> → <b>zelf zeggen/schrijven</b>. Alles corrigeert zichzelf; klik 🔊 om te horen.</p></div>
<main>
 <h2 class="subh">① Reconocer <span class="pill">receptief</span></h2>
 <div class="game" id="g_cards"></div>
 <div class="game" id="g_escucha"></div>
 <div class="game" id="g_clasifica"></div>
 <h2 class="subh">② Practicar <span class="pill">gestuurd</span></h2>
 <div class="game" id="g_match"></div>
 <div class="game" id="g_completa"></div>
 <div class="game" id="g_ordena"></div>
 <div class="game" id="g_oa"></div>
 <div class="game" id="g_tuusted"></div>
 <h2 class="subh">③ Producir &amp; comunicar <span class="pill">vrije productie</span></h2>
 <div class="game" id="g_presentate"></div>
 <div class="foot">C4 · «Welcome to Spanish» · Unidad 2 · Saludos</div>
</main>
<script>__JS__</script></body></html>"""

JS=r"""
function speak(t){if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(x=>/^es/i.test(x.lang));if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}
var TTS=('speechSynthesis'in window);if(TTS)speechSynthesis.getVoices();
function sb(id){return '<div class="scorebar" id="'+id+'"><span>Punten: <b class="pt">0</b></span><span>Reeks: <b class="st">0</b></span></div>'}
function setSc(el,p,s){el.querySelector('.pt').textContent=p;el.querySelector('.st').textContent=s}
function fb(el,ok,m){el.className='fb '+(ok?'good':'bad');el.innerHTML=(ok?'✅ ':'❌ ')+m}

// data — U2: saludos por el día · estar + estado · cortesía · despedidas
var CHUNKS=[["Buenos días","goedemorgen"],["Buenas tardes","goedemiddag"],["Buenas noches","goedenavond"],["¿Qué tal?","hoe gaat het?"],["¿Cómo estás?","hoe gaat het? (jij)"],["¿Cómo está usted?","hoe gaat het met u?"],["Estoy bien","ik voel me goed"],["Muy bien","heel goed"],["Regular","gaat wel"],["Estoy cansado/a","ik ben moe"],["Estoy ocupado/a","ik heb het druk"],["Estoy nervioso/a","ik ben nerveus"],["Estoy enfermo/a","ik ben ziek"],["Gracias","dank je"],["De nada","graag gedaan"],["Perdona","sorry"],["Adiós","dag / tot ziens"],["Hasta luego","tot straks"],["Hasta mañana","tot morgen"],["¡Nos vemos!","we zien elkaar"],["Chao","doei"]];

// ① Tarjetas
(function(){var el=document.getElementById('g_cards');el.innerHTML='<h3>Tarjetas 🗂️</h3><p class="desc">Draai de kaart (ES↔NL); klik 🔊 om te horen.</p><div class="fcgrid" id="cg"></div>';
 var g=el.querySelector('#cg');CHUNKS.forEach(function(c){var d=document.createElement('div');d.className='fc';d.innerHTML='<div class="in"><div class="s"><div class="w">'+c[0]+'</div>'+(TTS?'<div style="font-size:12px;opacity:.5;margin-top:4px">🔊</div>':'')+'</div><div class="b"><div class="tr">'+c[1]+'</div></div></div>';
  d.onclick=function(){d.classList.toggle('flip');};if(TTS)d.querySelector('.s').addEventListener('click',function(e){e.stopPropagation();speak(c[0].replace('/a','').replace('…',''));d.classList.toggle('flip');});g.appendChild(d);});})();

// ① Escucha
(function(){var el=document.getElementById('g_escucha');if(!TTS){el.innerHTML='<h3>¿Qué oyes? 🎧</h3><p class="desc">Spraak werkt in Chrome/Edge.</p>';return;}
 var bank=CHUNKS.map(c=>c[0].replace('/a','').replace('…','')).filter(x=>x.length<16);var p=0,s=0;
 el.innerHTML='<h3>¿Qué oyes? 🎧</h3><p class="desc">Klik ▶, luister en kies wat je hoort.</p>'+sb('sbE')+'<div style="margin:6px 0"><button class="spk-btn" id="eP">▶ Speel af</button></div><div class="chips" id="eO"></div><div class="fb" id="eF"></div>';
 var bar=el.querySelector('#sbE');function nx(){var a=bank[Math.floor(Math.random()*bank.length)];el.cur=a;var o=[a];while(o.length<4){var c=bank[Math.floor(Math.random()*bank.length)];if(o.indexOf(c)<0)o.push(c);}o.sort(()=>Math.random()-.5);var oc=el.querySelector('#eO');oc.innerHTML='';o.forEach(function(x){var c=document.createElement('div');c.className='chip';c.textContent=x;c.onclick=function(){var ok=x===a;if(ok){p++;s++}else s=0;setSc(bar,p,s);oc.querySelectorAll('.chip').forEach(function(z){if(z.textContent===a)z.classList.add('ok');else if(z===c&&!ok)z.classList.add('no');});fb(el.querySelector('#eF'),ok,'«'+a+'»');setTimeout(nx,1100);};oc.appendChild(c);});el.querySelector('#eF').className='fb';speak(a);}
 el.querySelector('#eP').onclick=function(){speak(el.cur);};nx();})();

// ① Clasifica (saludo/estado/despedida/cortesía)
(function(){var el=document.getElementById('g_clasifica');
 var items=[["Buenos días","saludo"],["Buenas tardes","saludo"],["¿Qué tal?","saludo"],["Estoy bien","estado"],["Estoy cansada","estado"],["Estoy ocupado","estado"],["Adiós","despedida"],["Hasta luego","despedida"],["Gracias","cortesía"],["De nada","cortesía"]];
 var cat={saludo:"saludo",estado:"estado (¿cómo?)",despedida:"despedida",cortesía:"cortesía"};var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>Clasifica 🎯</h3><p class="desc">Wat is het? Kies de categorie.</p>'+sb('sbC')+'<div id="cw" style="font-size:24px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" id="cc" style="justify-content:center"></div><div class="fb" id="cf"></div>';
 var bar=el.querySelector('#sbC'),cc=el.querySelector('#cc');Object.keys(cat).forEach(function(k){var c=document.createElement('div');c.className='chip';c.textContent=cat[k];c.onclick=function(){g(k);};cc.appendChild(c);});
 function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#cw').textContent=el.cur[0];el.querySelector('#cf').className='fb';}
 function g(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);fb(el.querySelector('#cf'),ok,'«'+el.cur[0]+'» → '+cat[el.cur[1]]);setTimeout(nx,900);}nx();})();

// ② Match chunk↔situación
(function(){var el=document.getElementById('g_match');
 var pairs=[["Buenos días","'s ochtends groeten"],["¿Cómo estás?","vragen hoe het gaat"],["Estoy cansada","zeggen dat je moe bent"],["Gracias","bedanken"],["De nada","graag gedaan"],["Hasta mañana","afscheid tot morgen"]];
 var p=0,s=0,sel=null,done=0;var L=pairs.map(x=>x[0]),R=pairs.map(x=>x[1]).slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>Relaciona 🧩</h3><p class="desc">Klik links een uitdrukking, dan rechts de situatie.</p>'+sb('sbM')+'<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px"><div class="chips" style="flex-direction:column" id="mL"></div><div class="chips" style="flex-direction:column" id="mR"></div></div><div class="fb" id="mf"></div>';
 var bar=el.querySelector('#sbM'),cL=el.querySelector('#mL'),cR=el.querySelector('#mR');
 L.forEach(function(t,i){var c=document.createElement('div');c.className='chip';c.textContent=t;c.dataset.i=i;c.onclick=function(){cL.querySelectorAll('.chip').forEach(z=>z.classList.remove('sel'));c.classList.add('sel');sel=i;};cL.appendChild(c);});
 R.forEach(function(t){var c=document.createElement('div');c.className='chip';c.textContent=t;c.onclick=function(){if(sel==null)return;var ok=t===pairs[sel][1];if(ok){c.classList.add('ok');cL.querySelector('.chip[data-i="'+sel+'"]').classList.add('ok');p++;s++;done++;fb(el.querySelector('#mf'),true,pairs[sel][0]+' → '+t);if(done===pairs.length)fb(el.querySelector('#mf'),true,'¡Completado!');}else{s=0;c.classList.add('no');setTimeout(()=>c.classList.remove('no'),500);fb(el.querySelector('#mf'),false,'Probeer opnieuw.');}setSc(bar,p,s);sel=null;cL.querySelectorAll('.chip').forEach(z=>z.classList.remove('sel'));};cR.appendChild(c);});})();

// ② Completa el diálogo
(function(){var el=document.getElementById('g_completa');
 var gaps=[["días"],["estás"],["Estoy"],["cansada"],["luego"]];
 el.innerHTML='<h3>Completa el diálogo 💬</h3><p class="desc">Vul de ontbrekende woorden in en klik Controleer.</p>'
  +'<div class="dlgfill">— Buenos <input class="txin" data-i="0">, ¿cómo <input class="txin" data-i="1">? <br>— <input class="txin" data-i="2"> bien, gracias. ¿Y tú?<br>— Regular… estoy un poco <input class="txin" data-i="3"> <span style="color:var(--mut);font-size:12px">(una chica: moe)</span>.<br>— Vaya. ¡Hasta <input class="txin" data-i="4">!</div>'
  +'<div class="answerbtns"><button class="btn" id="coGo">Controleer</button></div><div class="fb" id="coF"></div>';
 el.querySelector('#coGo').onclick=function(){var n=0;el.querySelectorAll('.txin').forEach(function(inp){var i=+inp.dataset.i;var ok=(inp.value||'').trim().toLowerCase()===gaps[i][0].toLowerCase();inp.style.borderColor=ok?'#2F9A4A':'#DC2626';if(ok)n++;});fb(el.querySelector('#coF'),n===gaps.length,n+' / '+gaps.length+' juist.'+(n<gaps.length?' Kijk naar de rood omrande vakjes.':' ¡Perfecto!'));};})();

// ② Ordena la conversación
(function(){var el=document.getElementById('g_ordena');
 var sol=["Buenos días, ¿qué tal?","Muy bien, ¿y tú?","Regular, estoy un poco cansado.","Vaya, ¿por qué?","Mucho trabajo. ¡Hasta luego!","Adiós, hasta mañana."];
 var cur=[],pool=sol.slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>Ordena la conversación 🔢</h3><p class="desc">Klik de zinnen in de juiste volgorde.</p><div class="chips" id="oP"></div><div class="col" id="oB"><b style="font-size:12px;color:var(--gd)">JOUW VOLGORDE</b><div class="chips" id="oBB" style="margin-top:6px"></div></div><div class="answerbtns"><button class="btn sec" id="oR">Reset</button><button class="btn" id="oC">Controleer</button></div><div class="fb" id="oF"></div>';
 function draw(){var p=el.querySelector('#oP');p.innerHTML='';pool.forEach(function(t,i){var c=document.createElement('div');c.className='chip';c.textContent=t;c.onclick=function(){cur.push(t);pool.splice(i,1);draw();built();};p.appendChild(c);});}
 function built(){var b=el.querySelector('#oBB');b.innerHTML='';cur.forEach(function(t,i){var c=document.createElement('div');c.className='chip sel';c.textContent=(i+1)+'. '+t;c.onclick=function(){pool.push(t);cur.splice(i,1);draw();built();};b.appendChild(c);});}
 el.querySelector('#oC').onclick=function(){fb(el.querySelector('#oF'),cur.join('|')===sol.join('|'),cur.join('|')===sol.join('|')?'¡Perfecto!':'Nog niet — begin met een begroeting.');};
 el.querySelector('#oR').onclick=function(){cur=[];pool=sol.slice().sort(()=>Math.random()-.5);draw();built();el.querySelector('#oF').className='fb';};draw();built();})();

// ② estar + estado (-o/-a) — m/v inductief
(function(){var el=document.getElementById('g_oa');
 var items=[["Julio (chico) dice:","cansad","o"],["Josefina (chica) dice:","cansad","a"],["María dice:","ocupad","a"],["Un profesor (hombre) dice:","enferm","o"],["Ana dice:","nervios","a"]];
 var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>Estoy… ¿-o o -a? 👀</h3><p class="desc">Mannen zeggen -o, vrouwen -a. Kies de juiste letter.</p>'+sb('sbO')+'<div id="ow" style="font-size:18px;text-align:center;margin:8px 0"></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._oa(\'o\')">-o</div><div class="chip" onclick="window._oa(\'a\')">-a</div></div><div class="fb" id="of"></div>';
 var bar=el.querySelector('#sbO');function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#ow').innerHTML=el.cur[0]+' <b>estoy '+el.cur[1]+'__</b>';el.querySelector('#of').className='fb';}
 window._oa=function(k){var ok=k===el.cur[2];if(ok){p++;s++}else s=0;setSc(bar,p,s);fb(el.querySelector('#of'),ok,'estoy '+el.cur[1]+el.cur[2]);setTimeout(nx,950);};nx();})();

// ② ¿Tú o usted?
(function(){var el=document.getElementById('g_tuusted');
 var items=[["¿Cómo estás?","tú"],["¿Cómo está usted?","usted"],["¿Y tú?","tú"],["¿Cómo está, señor Fernández?","usted"],["¿Qué tal?","tú"]];
 var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>¿Tú o usted? 🤝</h3><p class="desc">Informeel (tú) of beleefd (usted)? Kies.</p>'+sb('sbTU')+'<div id="tw" style="font-size:19px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._tu(\'tú\')">tú (informeel)</div><div class="chip" onclick="window._tu(\'usted\')">usted (beleefd)</div></div><div class="fb" id="tf"></div>';
 var bar=el.querySelector('#sbTU');function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#tw').textContent=el.cur[0];el.querySelector('#tf').className='fb';}
 window._tu=function(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);fb(el.querySelector('#tf'),ok,el.cur[1]==='tú'?'informeel (met vrienden/klasgenoten)':'beleefd (met een onbekende/volwassene)');setTimeout(nx,1100);};nx();})();

// ③ Saluda y di cómo estás (vrije productie)
(function(){var el=document.getElementById('g_presentate');
 el.innerHTML='<h3>Saluda y di cómo estás ✍️🗣️</h3><p class="desc">Kies een moment van de dag, zeg hoe je je voelt, en zeg het hardop. Er is geen «juist» — het is jouw begroeting.</p>'
  +'<div style="display:grid;gap:8px;max-width:520px"><div><span style="font-family:var(--disp)">Groet:</span> <select class="txin" id="p1"><option>Buenos días</option><option>Buenas tardes</option><option>Buenas noches</option></select></div>'
  +'<div><span style="font-family:var(--disp)">Yo estoy</span> <input class="txin" id="p2" placeholder="bien / cansado-a"> <span style="font-family:var(--disp)">, ¿y tú?</span></div></div>'
  +'<div class="answerbtns"><button class="btn" id="pGo">Maak mijn zin</button>'+(TTS?'<button class="spk-btn" id="pSpk">🔊 hoor</button>':'')+'</div><div class="fb" id="pF"></div>';
 el.querySelector('#pGo').onclick=function(){var a=el.querySelector('#p1').value,c=(el.querySelector('#p2').value||'bien').trim();el.cur='¡Hola! '+a+'. ¿Qué tal? Yo estoy '+c+', ¿y tú?';fb(el.querySelector('#pF'),true,'<b>'+el.cur+'</b><br><span style="color:var(--mut);font-style:italic">Zeg het nu hardop tegen je buur.</span>');};
 var sp=el.querySelector('#pSpk');if(sp)sp.onclick=function(){if(el.cur)speak(el.cur);};})();
"""

html=HTML.replace("__CSS__",CSS).replace("__JS__",JS)
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U2_practica.html","w").write(html)
print("C4_U2_practica.html geschreven:",len(html),"bytes")
