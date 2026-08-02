#!/usr/bin/env python3
# C4 · Unidad 9 — §3 PRÁCTICA (native, zelfcorrigerend). Planes y obligaciones · ir a / tener que / tener + nw.
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
.foot{color:var(--mut);font-size:12px;text-align:center;margin:24px 0}
"""

HTML="""<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U9 · Práctica</title><style>__CSS__</style></head><body>
<div class="top"><h1>Unidad 9 · Planes y obligaciones — Práctica</h1><p>Oefen de bruikbare taal uit de scène: van <b>herkennen</b> → <b>kiezen</b> → <b>zelf zeggen/schrijven</b>. Alles corrigeert zichzelf; klik 🔊 om te horen.</p></div>
<main>
 <h2 class="subh">① Reconocer <span class="pill">receptief</span></h2>
 <div class="game" id="g_cards"></div>
 <div class="game" id="g_escucha"></div>
 <div class="game" id="g_clasifica"></div>
 <h2 class="subh">② Practicar <span class="pill">gestuurd</span></h2>
 <div class="game" id="g_plan"></div>
 <div class="game" id="g_tener"></div>
 <div class="game" id="g_match"></div>
 <div class="game" id="g_completa"></div>
 <div class="game" id="g_ordena"></div>
 <h2 class="subh">③ Producir &amp; comunicar <span class="pill">vrije productie</span></h2>
 <div class="game" id="g_finde"></div>
 <div class="foot">C4 · «Bienvenidos al español» · Unidad 9 · Planes y obligaciones</div>
</main>
<script>__JS__</script></body></html>"""

JS=r"""
function speak(t){if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(x=>/^es/i.test(x.lang));if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}
var TTS=('speechSynthesis'in window);if(TTS)speechSynthesis.getVoices();
function sb(id){return '<div class="scorebar" id="'+id+'"><span>Punten: <b class="pt">0</b></span><span>Reeks: <b class="st">0</b></span></div>'}
function setSc(el,p,s){el.querySelector('.pt').textContent=p;el.querySelector('.st').textContent=s}
function fb(el,ok,m){el.className='fb '+(ok?'good':'bad');el.innerHTML=(ok?'✅ ':'❌ ')+m}

var CHUNKS=[["Voy a + inf.","ik ga + werkwoord"],["Vamos a dormir","we gaan slapen"],["¿Qué vas a hacer?","wat ga je doen?"],["Tengo que + inf.","ik moet + werkwoord"],["Tengo que trabajar","ik moet werken"],["¿Tienes que hacer algo?","moet je iets doen?"],["Tengo cosas que hacer","ik heb dingen te doen"],["Tengo hambre","ik heb honger"],["Tengo sueño","ik ben slaperig"],["ir al cine","naar de cinema gaan"],["pasear al perro","de hond uitlaten"],["quedar con amigos","afspreken met vrienden"],["ver una película","een film kijken"],["No puedo","ik kan niet"],["¡Qué pena!","wat jammer!"],["Estoy libre","ik ben vrij"],["el finde","het weekend"]];

(function(){var el=document.getElementById('g_cards');el.innerHTML='<h3>Tarjetas 🗂️</h3><p class="desc">Draai de kaart (ES↔NL); klik 🔊 om te horen.</p><div class="fcgrid" id="cg"></div>';
 var g=el.querySelector('#cg');CHUNKS.forEach(function(c){var d=document.createElement('div');d.className='fc';d.innerHTML='<div class="in"><div class="s"><div class="w">'+c[0]+'</div>'+(TTS?'<div style="font-size:12px;opacity:.5;margin-top:4px">🔊</div>':'')+'</div><div class="b"><div class="tr">'+c[1]+'</div></div></div>';
  d.onclick=function(){d.classList.toggle('flip');};if(TTS)d.querySelector('.s').addEventListener('click',function(e){e.stopPropagation();speak(c[0].replace('+ inf.','').replace(/[¿?¡!]/g,''));d.classList.toggle('flip');});g.appendChild(d);});})();

// ① ¿plan o obligación? (luisteren)
(function(){var el=document.getElementById('g_escucha');if(!TTS){el.innerHTML='<h3>¿Plan u obligación? 🎧</h3><p class="desc">Spraak werkt in Chrome/Edge.</p>';return;}
 var bank=[["Voy a ir al cine","plan"],["Tengo que trabajar","obligación"],["Vamos a dormir un poco más","plan"],["Tengo que estudiar","obligación"],["Voy a quedar con amigas","plan"],["Tengo que pasear al perro","obligación"],["¿Qué vas a hacer el finde?","plan"],["Tengo cosas que hacer","obligación"]];
 var p=0,s=0;
 el.innerHTML='<h3>¿Plan u obligación? 🎧</h3><p class="desc">Klik ▶, luister en beslis: is het een <b>plan</b> (voy a…) of een <b>verplichting</b> (tengo que…)?</p>'+sb('sbE')+'<div style="margin:6px 0"><button class="spk-btn" id="eP">▶ Speel opnieuw</button></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._po(\'plan\')">🗓️ un plan</div><div class="chip" onclick="window._po(\'obligación\')">✅ una obligación</div></div><div class="fb" id="eF"></div>';
 var bar=el.querySelector('#sbE');
 function nx(){el.cur=bank[Math.floor(Math.random()*bank.length)];el.querySelector('#eF').className='fb';speak(el.cur[0]);}
 window._po=function(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);fb(el.querySelector('#eF'),ok,'«'+el.cur[0]+'» → '+el.cur[1]);setTimeout(nx,1300);};
 el.querySelector('#eP').onclick=function(){if(el.cur)speak(el.cur[0]);};nx();})();

// ① Clasifica (plan / obligación / con tener)
(function(){var el=document.getElementById('g_clasifica');
 var items=[["voy a estudiar","plan"],["vamos a pasear","plan"],["¿qué vas a hacer?","plan"],["tengo que trabajar","obligación"],["tienes que dormir","obligación"],["tengo cosas que hacer","obligación"],["tengo hambre","tener"],["tengo sueño","tener"],["tengo prisa","tener"]];
 var cat={"plan":"un plan 🗓️","obligación":"obligación ✅","tener":"tener + nw. 🙋"};var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>Clasifica 🎯</h3><p class="desc">Plan (ir a), verplichting (tener que) of «tener + naamwoord»?</p>'+sb('sbC')+'<div class="big" id="cw"></div><div class="chips" id="cc" style="justify-content:center"></div><div class="fb" id="cf"></div>';
 var bar=el.querySelector('#sbC'),cc=el.querySelector('#cc');Object.keys(cat).forEach(function(k){var c=document.createElement('div');c.className='chip';c.textContent=cat[k];c.onclick=function(){g(k);};cc.appendChild(c);});
 function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#cw').textContent=el.cur[0];el.querySelector('#cf').className='fb';}
 function g(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);fb(el.querySelector('#cf'),ok,'«'+el.cur[0]+'» → '+cat[el.cur[1]]);setTimeout(nx,900);}nx();})();

// ② voy a / vas a / vamos a
(function(){var el=document.getElementById('g_plan');
 var items=[["Yo ___ preparar café.","voy a"],["¿Tú qué ___ hacer?","vas a"],["Nosotros ___ dormir más.","vamos a"],["Yo ___ quedar con amigas.","voy a"],["¿___ pasear? (nosotros)","vamos a"],["¿Qué ___ hacer el finde? (tú)","vas a"]];
 var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>¿voy a · vas a · vamos a? 🗓️</h3><p class="desc">Kies de juiste vorm van «ir a» (let op wie het doet).</p>'+sb('sbP')+'<div class="big" id="pw"></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._ir(\'voy a\')">voy a (ik)</div><div class="chip" onclick="window._ir(\'vas a\')">vas a (jij)</div><div class="chip" onclick="window._ir(\'vamos a\')">vamos a (wij)</div></div><div class="fb" id="pf"></div>';
 var bar=el.querySelector('#sbP');function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#pw').textContent=el.cur[0];el.querySelector('#pf').className='fb';}
 window._ir=function(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);var f=el.cur[0].replace('___',el.cur[1]);fb(el.querySelector('#pf'),ok,f);if(TTS&&ok)speak(f.replace(/[¿?]/g,''));setTimeout(nx,1050);};nx();})();

// ② tener que of tener + naamwoord?
(function(){var el=document.getElementById('g_tener');
 var items=[["Ik moet werken.","Tengo que trabajar"],["Ik heb honger.","Tengo hambre"],["Ik ben slaperig.","Tengo sueño"],["Ik moet studeren.","Tengo que estudiar"],["Ik heb haast.","Tengo prisa"],["Ik moet slapen.","Tengo que dormir"]];
 var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>Con «que» o sin «que»? 🙋</h3><p class="desc">Vóór een <b>werkwoord</b> → tengo <b>que</b>… · vóór een <b>naamwoord</b> → tengo… (zonder que). Kies de juiste Spaanse zin.</p>'+sb('sbT')+'<div class="big" id="tw"></div><div class="chips" id="to" style="justify-content:center"></div><div class="fb" id="tf"></div>';
 var bar=el.querySelector('#sbT');
 function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#tw').textContent=el.cur[0];
  var right=el.cur[1];
  // maak een plausibele fout: que weglaten of toevoegen
  var wrong = right.indexOf(' que ')>=0 ? right.replace(' que ',' ') : right.replace('Tengo ','Tengo que ');
  var o=[right,wrong].sort(function(){return Math.random()-.5;});
  var to=el.querySelector('#to');to.innerHTML='';
  o.forEach(function(x){var c=document.createElement('div');c.className='chip';c.textContent=x;c.onclick=function(){var ok=x===right;if(ok){p++;s++;if(TTS)speak(right)}else s=0;setSc(bar,p,s);
    fb(el.querySelector('#tf'),ok,ok?('¡Sí! '+right):('Fout — juist is: '+right));setTimeout(nx,1400);};to.appendChild(c);});
  el.querySelector('#tf').className='fb';}
 nx();})();

// ② Match invitación ↔ excusa
(function(){var el=document.getElementById('g_match');
 var pairs=[["¿Vamos al cine esta noche?","No puedo. Tengo que estudiar."],["¿Quedamos el sábado?","El sábado tengo que trabajar."],["¿Desayunamos juntos?","No tengo hambre, gracias."],["¿Vamos a dormir más?","No, tengo cosas que hacer."],["¿Tomamos algo el domingo?","Vale, el domingo estoy libre."]];
 var p=0,s=0,sel=null,done=0;var L=pairs.map(x=>x[0]),R=pairs.map(x=>x[1]).slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>Relaciona · invitación ↔ respuesta 🧩</h3><p class="desc">Klik links een uitnodiging, dan rechts het passende antwoord.</p>'+sb('sbM')+'<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px"><div class="chips" style="flex-direction:column" id="mL"></div><div class="chips" style="flex-direction:column" id="mR"></div></div><div class="fb" id="mf"></div>';
 var bar=el.querySelector('#sbM'),cL=el.querySelector('#mL'),cR=el.querySelector('#mR');
 L.forEach(function(t,i){var c=document.createElement('div');c.className='chip';c.textContent=t;c.dataset.i=i;c.onclick=function(){cL.querySelectorAll('.chip').forEach(z=>z.classList.remove('sel'));c.classList.add('sel');sel=i;};cL.appendChild(c);});
 R.forEach(function(t){var c=document.createElement('div');c.className='chip';c.textContent=t;c.onclick=function(){if(sel==null)return;var ok=t===pairs[sel][1];if(ok){c.classList.add('ok');cL.querySelector('.chip[data-i="'+sel+'"]').classList.add('ok');p++;s++;done++;fb(el.querySelector('#mf'),true,pairs[sel][0]+' → '+t);if(done===pairs.length)fb(el.querySelector('#mf'),true,'¡Completado!');}else{s=0;c.classList.add('no');setTimeout(()=>c.classList.remove('no'),500);fb(el.querySelector('#mf'),false,'Probeer opnieuw.');}setSc(bar,p,s);sel=null;cL.querySelectorAll('.chip').forEach(z=>z.classList.remove('sel'));};cR.appendChild(c);});})();

// ② Completa el diálogo
(function(){var el=document.getElementById('g_completa');
 var gaps=[["Voy"],["Tengo"],["que"],["vamos"],["puedo"]];
 el.innerHTML='<h3>Completa el diálogo 💬</h3><p class="desc">Vul aan (Voy · Tengo · que · vamos · puedo).</p>'
  +'<div class="dlgfill">— ¿Qué haces esta tarde? <br>— <input class="txin" data-i="0"> a estudiar. <br>— ¿Y esta noche?<br>— <input class="txin" data-i="1"> <input class="txin" data-i="2"> pasear al perro.<br>— ¿Y el domingo? ¿<input class="txin" data-i="3"> a tomar algo?<br>— El domingo no <input class="txin" data-i="4">. ¡Qué pena!</div>'
  +'<div class="answerbtns"><button class="btn" id="coGo">Controleer</button></div><div class="fb" id="coF"></div>';
 el.querySelector('#coGo').onclick=function(){var n=0;el.querySelectorAll('.txin').forEach(function(inp){var i=+inp.dataset.i;var ok=(inp.value||'').trim().toLowerCase()===gaps[i][0].toLowerCase();inp.style.borderColor=ok?'#2F9A4A':'#DC2626';if(ok)n++;});fb(el.querySelector('#coF'),n===gaps.length,n+' / '+gaps.length+' juist.'+(n<gaps.length?' Kijk naar de rode vakjes.':' ¡Perfecto!'));};})();

// ② Ordena la conversación
(function(){var el=document.getElementById('g_ordena');
 var sol=["¿Quedamos para ir al cine esta noche?","No puedo. Tengo que pasear al perro.","¿Y mañana?","Mañana voy a quedar con unas amigas.","¡Qué pena! Otro día, ¿vale?"];
 var cur=[],pool=sol.slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>Ordena la conversación 🔢</h3><p class="desc">Klik de zinnen in de juiste volgorde (uitnodiging → excuus → nieuw voorstel).</p><div class="chips" id="oP"></div><div class="col" id="oB"><b style="font-size:12px;color:var(--gd)">JOUW VOLGORDE</b><div class="chips" id="oBB" style="margin-top:6px"></div></div><div class="answerbtns"><button class="btn sec" id="oR">Reset</button><button class="btn" id="oC">Controleer</button></div><div class="fb" id="oF"></div>';
 function draw(){var p=el.querySelector('#oP');p.innerHTML='';pool.forEach(function(t,i){var c=document.createElement('div');c.className='chip';c.textContent=t;c.onclick=function(){cur.push(t);pool.splice(i,1);draw();built();};p.appendChild(c);});}
 function built(){var b=el.querySelector('#oBB');b.innerHTML='';cur.forEach(function(t,i){var c=document.createElement('div');c.className='chip sel';c.textContent=(i+1)+'. '+t;c.onclick=function(){pool.push(t);cur.splice(i,1);draw();built();};b.appendChild(c);});}
 el.querySelector('#oC').onclick=function(){var ok=cur.join('|')===sol.join('|');fb(el.querySelector('#oF'),ok,ok?'¡Perfecto!':'Nog niet — begin met de uitnodiging.');};
 el.querySelector('#oR').onclick=function(){cur=[];pool=sol.slice().sort(()=>Math.random()-.5);draw();built();el.querySelector('#oF').className='fb';};draw();built();})();

// ③ Mi finde (vrije productie)
(function(){var el=document.getElementById('g_finde');
 el.innerHTML='<h3>Mi finde ✍️🗣️</h3><p class="desc">Zeg één plan én één verplichting. Er is geen «juist» — het is jouw weekend.</p>'
  +'<div style="display:grid;gap:8px;max-width:660px"><div><select class="txin" id="p0"><option>El sábado</option><option>El domingo</option><option>Esta noche</option><option>Este finde</option></select> <span style="font-family:var(--disp)">voy a</span> <input class="txin" id="p1" placeholder="ir al cine…" style="width:160px"> <span style="font-family:var(--disp)">, pero también tengo que</span> <input class="txin" id="p2" placeholder="estudiar…" style="width:150px"> <span style="font-family:var(--disp)">.</span></div></div>'
  +'<div class="answerbtns"><button class="btn" id="pGo">Maak mijn zin</button>'+(TTS?'<button class="spk-btn" id="pSpk">🔊 hoor</button>':'')+'</div><div class="fb" id="pF"></div>';
 el.querySelector('#pGo').onclick=function(){var d=el.querySelector('#p0').value,a=(el.querySelector('#p1').value||'ir al cine').trim(),b=(el.querySelector('#p2').value||'estudiar').trim();el.cur=d+' voy a '+a+', pero también tengo que '+b+'.';fb(el.querySelector('#pF'),true,'<b>'+el.cur+'</b><br><span style="color:var(--mut);font-style:italic">Zeg het hardop. Nodig dan je buur uit — en laat hem/haar beleefd «nee» zeggen met «tengo que…».</span>');};
 var sp=el.querySelector('#pSpk');if(sp)sp.onclick=function(){if(el.cur)speak(el.cur);};})();
"""

html=HTML.replace("__CSS__",CSS).replace("__JS__",JS)
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U9_practica.html","w").write(html)
print("C4_U9_practica.html geschreven:",len(html),"bytes")
