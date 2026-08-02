#!/usr/bin/env python3
# C4 · Unidad 10 — §3 PRÁCTICA (native, zelfcorrigerend). Las tareas de casa ·
# hay que ↔ tengo que · saber + inf. ↔ poder + inf. · hulp aanbieden/afwijzen.
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
.fcgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px}
.fc{perspective:900px;height:112px;cursor:pointer}.fc .in{position:relative;width:100%;height:100%;transition:transform .5s;transform-style:preserve-3d}
.fc.flip .in{transform:rotateY(180deg)}.fc .s,.fc .b{position:absolute;inset:0;backface-visibility:hidden;border-radius:14px;border:1px solid var(--line);background:var(--card);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:8px;text-align:center}
.fc .s{border-top:4px solid var(--g)}.fc .b{transform:rotateY(180deg);background:var(--gt);border-top:4px solid var(--gd)}
.fc .w{font-family:var(--disp);font-weight:700;font-size:15px}.fc .tr{font-family:var(--disp);font-weight:700;font-size:14px;color:var(--gd)}
.dlgfill{font-size:15.5px;line-height:2.4}.dlgfill .txin{width:140px}
.wbox{border:1px solid var(--line);border-radius:10px;background:var(--crema);min-height:60px;padding:8px;margin-top:8px}
.big{font-family:var(--disp);font-size:21px;color:var(--gd);text-align:center;margin:8px 0}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:640px){.grid2{grid-template-columns:1fr}}
.tabla{width:100%;border-collapse:collapse;font-size:14.5px;margin-top:8px}
.tabla th{background:var(--gt);color:var(--gd);font-family:var(--disp);text-align:left;padding:7px 9px;font-size:13px}
.tabla td{border-bottom:1px solid var(--line);padding:6px 9px;vertical-align:middle}
.foot{color:var(--mut);font-size:12px;text-align:center;margin:24px 0}
"""

HTML="""<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U10 · Práctica</title><style>__CSS__</style></head><body>
<div class="top"><h1>Unidad 10 · Las tareas de casa — Práctica</h1><p>Oefen de bruikbare taal uit de scène: van <b>herkennen</b> → <b>kiezen</b> → <b>zelf zeggen/schrijven</b>. Alles corrigeert zichzelf; klik 🔊 om te horen.</p></div>
<main>
 <h2 class="subh">① Reconocer <span class="pill">receptief</span></h2>
 <div class="game" id="g_cards"></div>
 <div class="game" id="g_escucha"></div>
 <div class="game" id="g_clasifica"></div>
 <h2 class="subh">② Practicar <span class="pill">gestuurd</span></h2>
 <div class="game" id="g_hayque"></div>
 <div class="game" id="g_saber"></div>
 <div class="game" id="g_match"></div>
 <div class="game" id="g_completa"></div>
 <div class="game" id="g_ordena"></div>
 <h2 class="subh">③ Producir &amp; comunicar <span class="pill">vrije productie</span></h2>
 <div class="game" id="g_reparto"></div>
 <div class="foot">C4 · «Bienvenidos al español» · Unidad 10 · Las tareas de casa</div>
</main>
<script>__JS__</script></body></html>"""

JS=r"""
function speak(t){if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(x=>/^es/i.test(x.lang));if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}
var TTS=('speechSynthesis'in window);if(TTS)speechSynthesis.getVoices();
function sb(id){return '<div class="scorebar" id="'+id+'"><span>Punten: <b class="pt">0</b></span><span>Reeks: <b class="st">0</b></span></div>'}
function setSc(el,p,s){el.querySelector('.pt').textContent=p;el.querySelector('.st').textContent=s}
function fb(el,ok,m){el.className='fb '+(ok?'good':'bad');el.innerHTML=(ok?'✅ ':'❌ ')+m}

var CHUNKS=[["limpiar el polvo","afstoffen"],["pasar la aspiradora","stofzuigen"],["fregar los platos","de vaat doen"],["ordenar los armarios","de kasten opruimen"],["hacer la cama","het bed opmaken"],["planchar","strijken"],["Hay que limpiar","er moet gepoetst worden"],["Tengo que fregar","ík moet de vaat doen"],["¿Te ayudo?","help ik je?"],["Yo te ayudo","ik help je"],["¿Qué tengo que hacer?","wat moet ik doen?"],["No es molestia","het is geen moeite"],["¿Sabes…?","kan je…?"],["Sé pasar la aspiradora","ik kan stofzuigen"],["Claro que sé","natuurlijk kan ik dat"],["No funciona","het werkt niet"],["¡Qué desorden!","wat een rommel!"],["está enferma","zij is ziek"]];

(function(){var el=document.getElementById('g_cards');el.innerHTML='<h3>Tarjetas 🗂️</h3><p class="desc">Draai de kaart (ES↔NL); klik 🔊 om te horen.</p><div class="fcgrid" id="cg"></div>';
 var g=el.querySelector('#cg');CHUNKS.forEach(function(c){var d=document.createElement('div');d.className='fc';d.innerHTML='<div class="in"><div class="s"><div class="w">'+c[0]+'</div>'+(TTS?'<div style="font-size:12px;opacity:.5;margin-top:4px">🔊</div>':'')+'</div><div class="b"><div class="tr">'+c[1]+'</div></div></div>';
  d.onclick=function(){d.classList.toggle('flip');};if(TTS)d.querySelector('.s').addEventListener('click',function(e){e.stopPropagation();speak(c[0].replace(/…/g,'').replace(/[¿?¡!]/g,''));d.classList.toggle('flip');});g.appendChild(d);});})();

// ① ¿Ofrece ayuda o pide ayuda? (luisteren)
(function(){var el=document.getElementById('g_escucha');if(!TTS){el.innerHTML='<h3>¿Ofrece o pide? 🎧</h3><p class="desc">Spraak werkt in Chrome/Edge.</p>';return;}
 var bank=[["Yo te ayudo","ofrece"],["¿Te ayudo?","ofrece"],["¿Me ayudas?","pide"],["¿Qué tengo que hacer?","pide"],["Déjame, lo hago yo","ofrece"],["¿Puedes ayudarme, por favor?","pide"],["No es molestia, yo lo hago","ofrece"],["¿Sabes cómo funciona? No sé","pide"]];
 var p=0,s=0;
 el.innerHTML='<h3>¿Ofrece ayuda o pide ayuda? 🎧</h3><p class="desc">Klik ▶, luister en beslis: <b>biedt</b> deze persoon hulp áán, of <b>vraagt</b> hij/zij hulp?</p>'+sb('sbE')+'<div style="margin:6px 0"><button class="spk-btn" id="eP">▶ Speel opnieuw</button></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._op(\'ofrece\')">🤝 ofrece ayuda</div><div class="chip" onclick="window._op(\'pide\')">🙋 pide ayuda</div></div><div class="fb" id="eF"></div>';
 var bar=el.querySelector('#sbE');
 function nx(){el.cur=bank[Math.floor(Math.random()*bank.length)];el.querySelector('#eF').className='fb';speak(el.cur[0]);}
 window._op=function(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);fb(el.querySelector('#eF'),ok,'«'+el.cur[0]+'» → '+(el.cur[1]==='ofrece'?'ofrece ayuda (hij/zij biedt aan)':'pide ayuda (hij/zij vraagt)'));setTimeout(nx,1400);};
 el.querySelector('#eP').onclick=function(){if(el.cur)speak(el.cur[0]);};nx();})();

// ① Clasifica (tarea de casa / ofrecer ayuda / saber hacerlo)
(function(){var el=document.getElementById('g_clasifica');
 var items=[["pasar la aspiradora","tarea"],["fregar los platos","tarea"],["limpiar el polvo","tarea"],["hacer la cama","tarea"],["Yo te ayudo","ayuda"],["¿Te ayudo?","ayuda"],["No es molestia","ayuda"],["Claro que sé","saber"],["Sé cocinar","saber"],["No sé planchar","saber"]];
 var cat={"tarea":"una tarea 🧹","ayuda":"ofrecer ayuda 🤝","saber":"sé / no sé 💡"};var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>Clasifica 🎯</h3><p class="desc">Is het een <b>huistaak</b>, <b>hulp aanbieden</b> of zeggen wat je <b>kan</b>?</p>'+sb('sbC')+'<div class="big" id="cw"></div><div class="chips" id="cc" style="justify-content:center"></div><div class="fb" id="cf"></div>';
 var bar=el.querySelector('#sbC'),cc=el.querySelector('#cc');Object.keys(cat).forEach(function(k){var c=document.createElement('div');c.className='chip';c.textContent=cat[k];c.onclick=function(){g(k);};cc.appendChild(c);});
 function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#cw').textContent=el.cur[0];el.querySelector('#cf').className='fb';}
 function g(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);fb(el.querySelector('#cf'),ok,'«'+el.cur[0]+'» → '+cat[el.cur[1]]);setTimeout(nx,900);}nx();})();

// ② ¿hay que · tengo que · tienes que?
(function(){var el=document.getElementById('g_hayque');
 var items=[["La academia está sucia: ___ limpiar. (algemeen — niemand in het bijzonder)","hay que"],
  ["Yo ___ fregar los platos. (ík)","tengo que"],
  ["Tú ___ pasar la aspiradora. (jíj)","tienes que"],
  ["¡Qué desorden! ___ ordenar los armarios. (algemeen)","hay que"],
  ["María, ___ hacer la cama. (jíj)","tienes que"],
  ["Hoy ___ planchar yo. (ík)","tengo que"]];
 var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>¿hay que · tengo que · tienes que? ✅</h3><p class="desc"><b>hay que</b> = het moet gebeuren (algemeen) · <b>tengo que</b> = ík moet · <b>tienes que</b> = jíj moet.</p>'+sb('sbH')+'<div class="big" id="hw"></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._hq(\'hay que\')">hay que (algemeen)</div><div class="chip" onclick="window._hq(\'tengo que\')">tengo que (ik)</div><div class="chip" onclick="window._hq(\'tienes que\')">tienes que (jij)</div></div><div class="fb" id="hf"></div>';
 var bar=el.querySelector('#sbH');function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#hw').textContent=el.cur[0];el.querySelector('#hf').className='fb';}
 window._hq=function(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);var f=el.cur[0].replace('___',el.cur[1]).replace(/\s*\([^)]*\)/g,'');fb(el.querySelector('#hf'),ok,f);if(TTS&&ok)speak(f.replace(/[¿?¡!]/g,''));setTimeout(nx,1300);};nx();})();

// ② ¿saber o poder?
(function(){var el=document.getElementById('g_saber');
 var items=[["Ik heb het geleerd: ik <b>kan</b> stofzuigen.","Sé pasar la aspiradora"],
  ["De stofzuiger is stuk: ik <b>kan</b> nu niet stofzuigen.","No puedo pasar la aspiradora"],
  ["Ik heb nooit leren koken.","No sé cocinar"],
  ["Ik heb geen tijd vandaag: ik <b>kan</b> niet helpen.","Hoy no puedo ayudar"],
  ["Ik heb leren strijken: ik <b>kan</b> strijken.","Sé planchar"],
  ["De machine werkt niet: we <b>kunnen</b> niet fregar.","No podemos fregar"]];
 var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>¿saber o poder? 💡</h3><p class="desc">Nederlands zegt <b>één</b> woord — «kunnen». Spaans kiest: <b>saber</b> = het geléérd hebben · <b>poder</b> = de kans/mogelijkheid hebben.</p>'+sb('sbS')+'<div class="big" id="sw"></div><div class="chips" id="so" style="justify-content:center"></div><div class="fb" id="sf"></div>';
 var bar=el.querySelector('#sbS');
 function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#sw').innerHTML=el.cur[0];
  var right=el.cur[1];
  var wrong = /(^|\s)(Sé|sé)(\s)/.test(right)
      ? right.replace(/^Sé /,'Puedo ').replace(/^No sé /,'No puedo ')
      : right.replace(/^No puedo /,'No sé ').replace(/^Hoy no puedo /,'Hoy no sé ').replace(/^No podemos /,'No sabemos ');
  if(wrong===right){wrong=right.replace('sé','puedo').replace('puedo','sé');}
  var o=[right,wrong].sort(function(){return Math.random()-.5;});
  var so=el.querySelector('#so');so.innerHTML='';
  o.forEach(function(x){var c=document.createElement('div');c.className='chip';c.textContent=x;c.onclick=function(){var ok=x===right;if(ok){p++;s++;if(TTS)speak(right)}else s=0;setSc(bar,p,s);
    fb(el.querySelector('#sf'),ok,ok?('¡Sí! '+right):('Juist is: '+right+' — <i>saber</i> = geleerd, <i>poder</i> = mogelijk.'));setTimeout(nx,1700);};so.appendChild(c);});
  el.querySelector('#sf').className='fb';}
 nx();})();

// ② Match tarea ↔ objeto / lugar
(function(){var el=document.getElementById('g_match');
 var pairs=[["pasar la aspiradora","la aspiradora 🧹"],["fregar los platos","los platos 🍽️"],["planchar","la plancha 👕"],["hacer la cama","el dormitorio 🛏️"],["ordenar los armarios","el armario 🚪"],["limpiar el polvo","el trapo 🧽"]];
 var p=0,s=0,sel=null,done=0;var L=pairs.map(x=>x[0]),R=pairs.map(x=>x[1]).slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>Relaciona · tarea ↔ objeto 🧩</h3><p class="desc">Klik links een taak, dan rechts wat je ervoor nodig hebt (of waar je het doet).</p>'+sb('sbM')+'<div class="grid2"><div class="chips" style="flex-direction:column" id="mL"></div><div class="chips" style="flex-direction:column" id="mR"></div></div><div class="fb" id="mf"></div>';
 var bar=el.querySelector('#sbM'),cL=el.querySelector('#mL'),cR=el.querySelector('#mR');
 L.forEach(function(t,i){var c=document.createElement('div');c.className='chip';c.textContent=t;c.dataset.i=i;c.onclick=function(){cL.querySelectorAll('.chip').forEach(z=>z.classList.remove('sel'));c.classList.add('sel');sel=i;};cL.appendChild(c);});
 R.forEach(function(t){var c=document.createElement('div');c.className='chip';c.textContent=t;c.onclick=function(){if(sel==null)return;var ok=t===pairs[sel][1];if(ok){c.classList.add('ok');cL.querySelector('.chip[data-i="'+sel+'"]').classList.add('ok');p++;s++;done++;fb(el.querySelector('#mf'),true,pairs[sel][0]+' → '+t);if(done===pairs.length)fb(el.querySelector('#mf'),true,'¡Completado!');}else{s=0;c.classList.add('no');setTimeout(()=>c.classList.remove('no'),500);fb(el.querySelector('#mf'),false,'Probeer opnieuw.');}setSc(bar,p,s);sel=null;cL.querySelectorAll('.chip').forEach(z=>z.classList.remove('sel'));};cR.appendChild(c);});})();

// ② Completa el diálogo
(function(){var el=document.getElementById('g_completa');
 var gaps=[["Hay"],["ayudo"],["tengo"],["Sabes"],["sé"]];
 el.innerHTML='<h3>Completa el diálogo 💬</h3><p class="desc">Vul aan (Hay · ayudo · tengo · Sabes · sé).</p>'
  +'<div class="dlgfill">— ¡Qué desorden! <input class="txin" data-i="0"> que limpiar esto.<br>— Yo te <input class="txin" data-i="1">. ¿Qué <input class="txin" data-i="2"> que hacer?<br>— ¿<input class="txin" data-i="3"> pasar la aspiradora?<br>— Claro que <input class="txin" data-i="4">. No es molestia.</div>'
  +'<div class="answerbtns"><button class="btn" id="coGo">Controleer</button></div><div class="fb" id="coF"></div>';
 el.querySelector('#coGo').onclick=function(){var n=0;el.querySelectorAll('.txin').forEach(function(inp){var i=+inp.dataset.i;var ok=(inp.value||'').trim().toLowerCase()===gaps[i][0].toLowerCase();inp.style.borderColor=ok?'#2F9A4A':'#DC2626';if(ok)n++;});fb(el.querySelector('#coF'),n===gaps.length,n+' / '+gaps.length+' juist.'+(n<gaps.length?' Kijk naar de rode vakjes.':' ¡Perfecto!'));};})();

// ② Ordena la conversación
(function(){var el=document.getElementById('g_ordena');
 var sol=["La asistenta está enferma y no puede venir.","Entonces hay que limpiar nosotros.","Yo te ayudo. ¿Qué tengo que hacer?","¿Sabes pasar la aspiradora?","Claro que sé. ¡Ahí está!"];
 var cur=[],pool=sol.slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>Ordena la conversación 🔢</h3><p class="desc">Klik de zinnen in de juiste volgorde (probleem → wat moet gebeuren → hulp → taak → ¡gelukt!).</p><div class="chips" id="oP"></div><div class="col" id="oB"><b style="font-size:12px;color:var(--gd)">JOUW VOLGORDE</b><div class="chips" id="oBB" style="margin-top:6px"></div></div><div class="answerbtns"><button class="btn sec" id="oR">Reset</button><button class="btn" id="oC">Controleer</button></div><div class="fb" id="oF"></div>';
 function draw(){var p=el.querySelector('#oP');p.innerHTML='';pool.forEach(function(t,i){var c=document.createElement('div');c.className='chip';c.textContent=t;c.onclick=function(){cur.push(t);pool.splice(i,1);draw();built();};p.appendChild(c);});}
 function built(){var b=el.querySelector('#oBB');b.innerHTML='';cur.forEach(function(t,i){var c=document.createElement('div');c.className='chip sel';c.textContent=(i+1)+'. '+t;c.onclick=function(){pool.push(t);cur.splice(i,1);draw();built();};b.appendChild(c);});}
 el.querySelector('#oC').onclick=function(){var ok=cur.join('|')===sol.join('|');fb(el.querySelector('#oF'),ok,ok?'¡Perfecto!':'Nog niet — begin met het probleem (de asistenta).');};
 el.querySelector('#oR').onclick=function(){cur=[];pool=sol.slice().sort(()=>Math.random()-.5);draw();built();el.querySelector('#oF').className='fb';};draw();built();})();

// ③ ¿Quién hace qué en mi casa? (vrije productie)
(function(){var el=document.getElementById('g_reparto');
 var TAREAS=["pasar la aspiradora","fregar los platos","limpiar el polvo","hacer la cama","ordenar los armarios","planchar","cocinar"];
 var rows='';
 for(var i=0;i<3;i++){
  rows+='<tr><td><select class="txin r-t"><option>—</option>'+TAREAS.map(t=>'<option>'+t+'</option>').join('')+'</select></td>'
   +'<td><select class="txin r-q"><option>yo</option><option>tú</option><option>mi madre</option><option>mi padre</option><option>mi hermano/a</option><option>nadie</option></select></td>'
   +'<td><select class="txin r-s"><option>sé hacerlo</option><option>no sé hacerlo</option></select></td></tr>';
 }
 el.innerHTML='<h3>¿Quién hace qué en mi casa? ✍️🗣️</h3><p class="desc">Kies drie taken en zeg wie ze doet. Er is geen «juist» — het is jouw huis.</p>'
  +'<table class="tabla"><thead><tr><th>tarea</th><th>¿quién?</th><th>¿y yo?</th></tr></thead><tbody id="rB">'+rows+'</tbody></table>'
  +'<div class="answerbtns"><button class="btn" id="rGo">Maak mijn tekst</button>'+(TTS?'<button class="spk-btn" id="rSpk">🔊 hoor</button>':'')+'</div><div class="fb" id="rF"></div>';
 el.querySelector('#rGo').onclick=function(){
  var out=[],rows=el.querySelectorAll('#rB tr');
  rows.forEach(function(tr){var t=tr.querySelector('.r-t').value,q=tr.querySelector('.r-q').value,s=tr.querySelector('.r-s').value;
   if(t==='—')return;
   var frase;
   if(q==='yo') frase='Tengo que '+t+'.';
   else if(q==='tú') frase='Tienes que '+t+'.';
   else if(q==='nadie') frase='Hay que '+t+', pero nadie lo hace.';
   else frase=q.charAt(0).toUpperCase()+q.slice(1)+' hace una tarea: '+t+'.';
   frase+=' Yo '+(s==='sé hacerlo'?'sé':'no sé')+' '+t.replace(/^(pasar|fregar|limpiar|hacer|ordenar|planchar|cocinar)/,'$1')+'.';
   out.push(frase);});
  if(!out.length){fb(el.querySelector('#rF'),false,'Kies eerst minstens één tarea.');return;}
  el.cur='En mi casa: '+out.join(' ');
  fb(el.querySelector('#rF'),true,'<b>'+el.cur+'</b><br><span style="color:var(--mut);font-style:italic">Zeg het hardop. Vraag daarna aan je buur: «¿Y en tu casa? ¿Quién friega los platos?» — en bied hulp aan met «Yo te ayudo».</span>');};
 var sp=el.querySelector('#rSpk');if(sp)sp.onclick=function(){if(el.cur)speak(el.cur);};})();
"""

html=HTML.replace("__CSS__",CSS).replace("__JS__",JS)
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U10_practica.html","w").write(html)
print("C4_U10_practica.html geschreven:",len(html),"bytes")
