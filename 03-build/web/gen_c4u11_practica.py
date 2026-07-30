#!/usr/bin/env python3
# C4 · Unidad 11 — §3 PRÁCTICA (native, zelfcorrigerend). El tiempo y los gustos ·
# hace + naamwoord ↔ tengo frío · me gusta ↔ me gustan · adverbios de frecuencia.
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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U11 · Práctica</title><style>__CSS__</style></head><body>
<div class="top"><h1>Unidad 11 · El tiempo y los gustos — Práctica</h1><p>Oefen de bruikbare taal uit de scène: van <b>herkennen</b> → <b>kiezen</b> → <b>zelf zeggen/schrijven</b>. Alles corrigeert zichzelf; klik 🔊 om te horen.</p></div>
<main>
 <h2 class="subh">① Reconocer <span class="pill">receptief</span></h2>
 <div class="game" id="g_cards"></div>
 <div class="game" id="g_escucha"></div>
 <div class="game" id="g_clasifica"></div>
 <h2 class="subh">② Practicar <span class="pill">gestuurd</span></h2>
 <div class="game" id="g_gusta"></div>
 <div class="game" id="g_hace"></div>
 <div class="game" id="g_frec"></div>
 <div class="game" id="g_match"></div>
 <div class="game" id="g_completa"></div>
 <div class="game" id="g_reaccion"></div>
 <h2 class="subh">③ Producir &amp; comunicar <span class="pill">vrije productie</span></h2>
 <div class="game" id="g_ficha"></div>
 <div class="foot">C4 · «Welcome to Spanish» · Unidad 11 · El tiempo y los gustos</div>
</main>
<script>__JS__</script></body></html>"""

JS=r"""
function speak(t){if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(x=>/^es/i.test(x.lang));if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}
var TTS=('speechSynthesis'in window);if(TTS)speechSynthesis.getVoices();
function sb(id){return '<div class="scorebar" id="'+id+'"><span>Punten: <b class="pt">0</b></span><span>Reeks: <b class="st">0</b></span></div>'}
function setSc(el,p,s){el.querySelector('.pt').textContent=p;el.querySelector('.st').textContent=s}
function fb(el,ok,m){el.className='fb '+(ok?'good':'bad');el.innerHTML=(ok?'✅ ':'❌ ')+m}

var CHUNKS=[["Hace frío","het is koud"],["Hace calor","het is warm"],["Hace sol","het is zonnig"],["Hace viento","het waait"],["Hace buen tiempo","het is mooi weer"],["¿Qué tiempo hace?","wat voor weer is het?"],["el verano","de zomer"],["el invierno","de winter"],["Me gusta el cine","ik hou van film"],["Me gustan los deportes","ik hou van sport"],["Me gusta hacer yoga","ik doe graag yoga"],["¿Te gusta…?","hou jij van…?"],["A mí también","ik ook"],["A mí tampoco","ik ook niet"],["siempre","altijd"],["a veces","soms"],["casi nunca","bijna nooit"],["tres veces por semana","drie keer per week"],["en cambio","daarentegen"],["demasiado calor","te warm"]];

(function(){var el=document.getElementById('g_cards');el.innerHTML='<h3>Tarjetas 🗂️</h3><p class="desc">Draai de kaart (ES↔NL); klik 🔊 om te horen.</p><div class="fcgrid" id="cg"></div>';
 var g=el.querySelector('#cg');CHUNKS.forEach(function(c){var d=document.createElement('div');d.className='fc';d.innerHTML='<div class="in"><div class="s"><div class="w">'+c[0]+'</div>'+(TTS?'<div style="font-size:12px;opacity:.5;margin-top:4px">🔊</div>':'')+'</div><div class="b"><div class="tr">'+c[1]+'</div></div></div>';
  d.onclick=function(){d.classList.toggle('flip');};if(TTS)d.querySelector('.s').addEventListener('click',function(e){e.stopPropagation();speak(c[0].replace(/…/g,'').replace(/[¿?¡!]/g,''));d.classList.toggle('flip');});g.appendChild(d);});})();

// ① ¿el tiempo o los gustos? (luisteren)
(function(){var el=document.getElementById('g_escucha');if(!TTS){el.innerHTML='<h3>¿Tiempo o gustos? 🎧</h3><p class="desc">Spraak werkt in Chrome/Edge.</p>';return;}
 var bank=[["Hace mucho viento","tiempo"],["Me gusta el cine","gustos"],["En invierno hace frío","tiempo"],["No me gustan los hoteles","gustos"],["Siempre hace buen tiempo en Canarias","tiempo"],["A ella también le gusta hacer submarinismo","gustos"],["Aquí hace demasiado calor","tiempo"],["Me gusta más el frío","gustos"]];
 var p=0,s=0;
 el.innerHTML='<h3>¿Habla del tiempo o de sus gustos? 🎧</h3><p class="desc">Klik ▶, luister en beslis: gaat het over het <b>weer</b> of over wat iemand <b>graag heeft</b>?</p>'+sb('sbE')+'<div style="margin:6px 0"><button class="spk-btn" id="eP">▶ Speel opnieuw</button></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._tg(\'tiempo\')">🌤️ el tiempo</div><div class="chip" onclick="window._tg(\'gustos\')">❤️ los gustos</div></div><div class="fb" id="eF"></div>';
 var bar=el.querySelector('#sbE');
 function nx(){el.cur=bank[Math.floor(Math.random()*bank.length)];el.querySelector('#eF').className='fb';speak(el.cur[0]);}
 window._tg=function(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);fb(el.querySelector('#eF'),ok,'«'+el.cur[0]+'» → '+(el.cur[1]==='tiempo'?'el tiempo (hace…)':'los gustos (me gusta…)'));setTimeout(nx,1400);};
 el.querySelector('#eP').onclick=function(){if(el.cur)speak(el.cur[0]);};nx();})();

// ① Clasifica (tiempo / gustos / frecuencia)
(function(){var el=document.getElementById('g_clasifica');
 var items=[["hace calor","tiempo"],["hace viento","tiempo"],["hace buen tiempo","tiempo"],["me gusta la ópera","gustos"],["me gustan los deportes","gustos"],["no me gusta el frío","gustos"],["siempre","frec"],["casi nunca","frec"],["tres veces por semana","frec"],["a veces","frec"]];
 var cat={"tiempo":"el tiempo 🌤️","gustos":"los gustos ❤️","frec":"la frecuencia 🔁"};var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>Clasifica 🎯</h3><p class="desc">Weer, smaak of frequentie?</p>'+sb('sbC')+'<div class="big" id="cw"></div><div class="chips" id="cc" style="justify-content:center"></div><div class="fb" id="cf"></div>';
 var bar=el.querySelector('#sbC'),cc=el.querySelector('#cc');Object.keys(cat).forEach(function(k){var c=document.createElement('div');c.className='chip';c.textContent=cat[k];c.onclick=function(){g(k);};cc.appendChild(c);});
 function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#cw').textContent=el.cur[0];el.querySelector('#cf').className='fb';}
 function g(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);fb(el.querySelector('#cf'),ok,'«'+el.cur[0]+'» → '+cat[el.cur[1]]);setTimeout(nx,900);}nx();})();

// ② ¿gusta o gustan?
(function(){var el=document.getElementById('g_gusta');
 var items=[["el cine","gusta"],["los deportes","gustan"],["la ópera","gusta"],["las vacaciones","gustan"],["hacer yoga","gusta"],["los hoteles grandes","gustan"],["el frío","gusta"],["ir a la playa","gusta"],["los perros","gustan"]];
 var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>¿Me gusta o me gustan? ❤️</h3><p class="desc">Eén ding of een werkwoord → <b>gusta</b> · een meervoud → <b>gustan</b>.</p>'+sb('sbG')+'<div class="big" id="gw"></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._gu(\'gusta\')">Me gusta…</div><div class="chip" onclick="window._gu(\'gustan\')">Me gustan…</div></div><div class="fb" id="gf"></div>';
 var bar=el.querySelector('#sbG');function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#gw').textContent='Me gust___ '+el.cur[0];el.querySelector('#gf').className='fb';}
 window._gu=function(k){var ok=k===el.cur[1];if(ok){p++;s++}else s=0;setSc(bar,p,s);var f='Me '+el.cur[1]+' '+el.cur[0]+'.';fb(el.querySelector('#gf'),ok,f+(ok?'':' — '+(el.cur[1]==='gustan'?'meervoud!':'één ding / een werkwoord!')));if(TTS&&ok)speak(f);setTimeout(nx,1250);};nx();})();

// ② ¿hace o tengo?
(function(){var el=document.getElementById('g_hace');
 var items=[["In de winter is het koud. (buiten)","Hace frío"],["Ik heb het koud. (ík)","Tengo frío"],["Het is warm hier!","Hace calor"],["Ik heb het warm. (ík)","Tengo calor"],["Het waait hard.","Hace viento"],["Het is mooi weer in Canarias.","Hace buen tiempo"]];
 var pool=items.slice(),p=0,s=0;
 el.innerHTML='<h3>¿hace o tengo? 🌡️</h3><p class="desc">Over het <b>weer</b> → <b>hace</b> · over een <b>persoon</b> → <b>tengo</b>. Kies de juiste Spaanse zin.</p>'+sb('sbH')+'<div class="big" id="hw"></div><div class="chips" id="ho" style="justify-content:center"></div><div class="fb" id="hf"></div>';
 var bar=el.querySelector('#sbH');
 function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#hw').textContent=el.cur[0];
  var right=el.cur[1];
  var wrong = right.indexOf('Hace')===0 ? right.replace('Hace','Tengo') : right.replace('Tengo','Hace');
  var o=[right,wrong].sort(function(){return Math.random()-.5;});
  var ho=el.querySelector('#ho');ho.innerHTML='';
  o.forEach(function(x){var c=document.createElement('div');c.className='chip';c.textContent=x;c.onclick=function(){var ok=x===right;if(ok){p++;s++;if(TTS)speak(right)}else s=0;setSc(bar,p,s);
    fb(el.querySelector('#hf'),ok,ok?('¡Sí! '+right):('Juist is: '+right+' — <i>hace</i> = het weer, <i>tengo</i> = een persoon.'));setTimeout(nx,1600);};ho.appendChild(c);});
  el.querySelector('#hf').className='fb';}
 nx();})();

// ② De frecuencia-ladder ordenen
(function(){var el=document.getElementById('g_frec');
 var sol=["siempre","casi siempre","a veces","casi nunca","nunca"];
 var cur=[],pool=sol.slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>La escalera de frecuencia 🔁</h3><p class="desc">Klik de woorden van <b>100 %</b> naar <b>0 %</b>.</p><div class="chips" id="fP"></div><div class="col" id="fB"><b style="font-size:12px;color:var(--gd)">100 % → 0 %</b><div class="chips" id="fBB" style="margin-top:6px"></div></div><div class="answerbtns"><button class="btn sec" id="fR">Reset</button><button class="btn" id="fC">Controleer</button></div><div class="fb" id="fF"></div>';
 function draw(){var p=el.querySelector('#fP');p.innerHTML='';pool.forEach(function(t,i){var c=document.createElement('div');c.className='chip';c.textContent=t;c.onclick=function(){cur.push(t);pool.splice(i,1);draw();built();};p.appendChild(c);});}
 function built(){var b=el.querySelector('#fBB');b.innerHTML='';cur.forEach(function(t,i){var c=document.createElement('div');c.className='chip sel';c.textContent=(i+1)+'. '+t;c.onclick=function(){pool.push(t);cur.splice(i,1);draw();built();};b.appendChild(c);});}
 el.querySelector('#fC').onclick=function(){var ok=cur.join('|')===sol.join('|');fb(el.querySelector('#fF'),ok,ok?'¡Perfecto! siempre → casi siempre → a veces → casi nunca → nunca':'Nog niet — begin met 100 %.');};
 el.querySelector('#fR').onclick=function(){cur=[];pool=sol.slice().sort(()=>Math.random()-.5);draw();built();el.querySelector('#fF').className='fb';};draw();built();})();

// ② Match estación ↔ tiempo
(function(){var el=document.getElementById('g_match');
 var pairs=[["el invierno","hace frío y nieva ❄️"],["el verano","hace mucho calor ☀️"],["el otoño","hace viento y llueve 🍂"],["la primavera","hace buen tiempo 🌷"],["Canarias","hace buen tiempo todo el año 🏝️"],["Ávila","hace un frío terrible 🥶"]];
 var p=0,s=0,sel=null,done=0;var L=pairs.map(x=>x[0]),R=pairs.map(x=>x[1]).slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>Relaciona · ¿qué tiempo hace? 🧩</h3><p class="desc">Klik links een seizoen of plek, dan rechts het passende weer.</p>'+sb('sbM')+'<div class="grid2"><div class="chips" style="flex-direction:column" id="mL"></div><div class="chips" style="flex-direction:column" id="mR"></div></div><div class="fb" id="mf"></div>';
 var bar=el.querySelector('#sbM'),cL=el.querySelector('#mL'),cR=el.querySelector('#mR');
 L.forEach(function(t,i){var c=document.createElement('div');c.className='chip';c.textContent=t;c.dataset.i=i;c.onclick=function(){cL.querySelectorAll('.chip').forEach(z=>z.classList.remove('sel'));c.classList.add('sel');sel=i;};cL.appendChild(c);});
 R.forEach(function(t){var c=document.createElement('div');c.className='chip';c.textContent=t;c.onclick=function(){if(sel==null)return;var ok=t===pairs[sel][1];if(ok){c.classList.add('ok');cL.querySelector('.chip[data-i="'+sel+'"]').classList.add('ok');p++;s++;done++;fb(el.querySelector('#mf'),true,pairs[sel][0]+' → '+t);if(done===pairs.length)fb(el.querySelector('#mf'),true,'¡Completado!');}else{s=0;c.classList.add('no');setTimeout(()=>c.classList.remove('no'),500);fb(el.querySelector('#mf'),false,'Probeer opnieuw.');}setSc(bar,p,s);sel=null;cL.querySelectorAll('.chip').forEach(z=>z.classList.remove('sel'));};cR.appendChild(c);});})();

// ② Completa el diálogo
(function(){var el=document.getElementById('g_completa');
 var gaps=[["hace"],["gusta"],["gustan"],["veces"],["también"]];
 el.innerHTML='<h3>Completa el diálogo 💬</h3><p class="desc">Vul aan (hace · gusta · gustan · veces · también).</p>'
  +'<div class="dlgfill">— ¡Uf! Aquí <input class="txin" data-i="0"> demasiado calor.<br>— A mí me <input class="txin" data-i="1"> más el frío.<br>— ¿Y los deportes? — Sí, me <input class="txin" data-i="2"> mucho. Voy al gimnasio tres <input class="txin" data-i="3"> por semana.<br>— ¡A mí <input class="txin" data-i="4">!</div>'
  +'<div class="answerbtns"><button class="btn" id="coGo">Controleer</button></div><div class="fb" id="coF"></div>';
 el.querySelector('#coGo').onclick=function(){var n=0;el.querySelectorAll('.txin').forEach(function(inp){var i=+inp.dataset.i;var ok=(inp.value||'').trim().toLowerCase()===gaps[i][0].toLowerCase();inp.style.borderColor=ok?'#2F9A4A':'#DC2626';if(ok)n++;});fb(el.querySelector('#coF'),n===gaps.length,n+' / '+gaps.length+' juist.'+(n<gaps.length?' Kijk naar de rode vakjes.':' ¡Perfecto!'));};})();

// ② ¿Cómo reaccionas?
(function(){var el=document.getElementById('g_reaccion');
 var items=[["Me gusta el cine. (jij ook)","A mí también"],["No me gusta la ópera. (jij ook niet)","A mí tampoco"],["Me gustan los deportes. (jij niet)","A mí no"],["No me gusta el frío. (jij wel)","A mí sí"],["Me gusta hacer yoga. (jij ook)","A mí también"],["No me gustan los hoteles. (jij wel)","A mí sí"]];
 var pool=items.slice(),p=0,s=0;
 var opts=["A mí también","A mí tampoco","A mí no","A mí sí"];
 el.innerHTML='<h3>¿Cómo reaccionas? 🙋</h3><p class="desc">Reageer met de juiste chunk. Let op of de zin <b>positief</b> of <b>negatief</b> is.</p>'+sb('sbR')+'<div class="big" id="rw"></div><div class="chips" id="ro" style="justify-content:center"></div><div class="fb" id="rf"></div>';
 var bar=el.querySelector('#sbR'),ro=el.querySelector('#ro');
 opts.forEach(function(o){var c=document.createElement('div');c.className='chip';c.textContent=o;c.onclick=function(){g(o);};ro.appendChild(c);});
 function nx(){if(!pool.length)pool=items.slice();el.cur=pool.splice(Math.floor(Math.random()*pool.length),1)[0];el.querySelector('#rw').textContent='— '+el.cur[0];el.querySelector('#rf').className='fb';}
 function g(o){var ok=o===el.cur[1];if(ok){p++;s++;if(TTS)speak(el.cur[1])}else s=0;setSc(bar,p,s);
  fb(el.querySelector('#rf'),ok,ok?('¡Sí! «'+el.cur[1]+'»'):('Juist is: «'+el.cur[1]+'» — bij een <b>negatieve</b> zin gebruik je <i>tampoco</i> of <i>sí</i>.'));setTimeout(nx,1600);}
 nx();})();

// ③ Mi ficha «El tiempo y yo» (vrije productie)
(function(){var el=document.getElementById('g_ficha');
 var GUSTA=["el cine","la ópera","el frío","el calor","hacer yoga","ir a la playa","hacer submarinismo"];
 var GUSTAN=["los deportes","las vacaciones","los hoteles grandes","los días de sol","las fiestas"];
 el.innerHTML='<h3>Mi ficha · El tiempo y yo ✍️🗣️</h3><p class="desc">Bouw je eigen ficha. Er is geen «juist» — het is jouw seizoen en jouw smaak.</p>'
  +'<div style="display:grid;gap:10px;max-width:720px">'
  +'<div>Mi estación favorita es <select class="txin" id="q0"><option>el verano</option><option>el invierno</option><option>la primavera</option><option>el otoño</option></select>. En <span id="q0b" style="font-family:var(--disp)"></span> <span style="font-family:var(--disp)">hace</span> <select class="txin" id="q1"><option>calor</option><option>frío</option><option>sol</option><option>viento</option><option>buen tiempo</option></select>.</div>'
  +'<div><span style="font-family:var(--disp)">Me gusta</span> <select class="txin" id="q2">'+GUSTA.map(g=>'<option>'+g+'</option>').join('')+'</select> <span style="font-family:var(--disp)">y me gustan</span> <select class="txin" id="q3">'+GUSTAN.map(g=>'<option>'+g+'</option>').join('')+'</select>.</div>'
  +'<div><select class="txin" id="q4"><option>Siempre</option><option>Casi siempre</option><option>A veces</option><option>Casi nunca</option></select> <input class="txin" id="q5" placeholder="voy al cine…" style="width:190px"> — <input class="txin" id="q6" placeholder="dos" style="width:70px"> <span style="font-family:var(--disp)">veces por semana</span>.</div>'
  +'</div>'
  +'<div class="answerbtns"><button class="btn" id="fiGo">Maak mijn ficha</button>'+(TTS?'<button class="spk-btn" id="fiSpk">🔊 hoor</button>':'')+'</div><div class="fb" id="fiF"></div>';
 function est(){return el.querySelector('#q0').value;}
 function sync(){el.querySelector('#q0b').textContent=est();}
 el.querySelector('#q0').onchange=sync;sync();
 el.querySelector('#fiGo').onclick=function(){
  var v=id=>el.querySelector(id).value.trim();
  var act=v('#q5')||'voy al cine', n=v('#q6')||'dos';
  el.cur='Mi estación favorita es '+est()+'. En '+est()+' hace '+v('#q1')+'. '
        +'Me gusta '+v('#q2')+' y me gustan '+v('#q3')+'. '
        +v('#q4')+' '+act+' — '+n+' veces por semana.';
  fb(el.querySelector('#fiF'),true,'<b>'+el.cur+'</b><br><span style="color:var(--mut);font-style:italic">Zeg het hardop. Vraag daarna aan drie klasgenoten «¿Te gusta…?» en reageer met «A mí también / A mí tampoco».</span>');};
 var sp=el.querySelector('#fiSpk');if(sp)sp.onclick=function(){if(el.cur)speak(el.cur);};})();
"""

html=HTML.replace("__CSS__",CSS).replace("__JS__",JS)
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U11_practica.html","w").write(html)
print("C4_U11_practica.html geschreven:",len(html),"bytes")
