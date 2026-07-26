#!/usr/bin/env python3
# Genereert de zelfstandige HTML-hub voor U0 (flip cards, woordenschat-zoek, conjugador,
# visuele/interactieve grammatica + spellen). Fonts base64 ingebed → één standalone bestand.
import json, base64, os, sys

ROOT="/home/user/espa-ol-en-la-pr-ctica"
SCRATCH="/tmp/claude-0/-home-user-espa-ol-en-la-pr-ctica/c4f0edbd-dbbb-5710-a740-e04235ccd8ef/scratchpad"
vocab=json.load(open(f"{SCRATCH}/u0_vocab.json"))
mapsvg=open(f"{SCRATCH}/mundo_map_real.svg").read()
sys.path.insert(0,SCRATCH); import cast_gen as C
moch=C.mochila("100%","compass")
av={n:C.make(n,"avatar","100%") for n in ["lucia","diego","valen","nina"]}; av["tu"]=C.tu_avatar("100%")

def b64(p):
    return base64.b64encode(open(p,"rb").read()).decode()
def face(fam,path,w):
    return f"@font-face{{font-family:'{fam}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{path}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([
 face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),
 face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"), face("Inter","Inter-600.woff2","600"),
 face("Caveat","Caveat-700.woff2","700"),
])

CSS = FONTS + """
:root{--g:#1E9E74;--gd:#157355;--gt:#E4F4EE;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E4E3DE;--red:#DC2626;--amber:#B7860B;--card:#fff;
--onder:#2563EB;--ww:#EA7317;--voorw:#1E9E74;--tijd:#7C3AED;--plaats:#14B8A6;
--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif;--hand:'Caveat',cursive}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#171713;--crema:#22221C;--gt:#12352A;--line:#33332B;--card:#20201A}
*{box-sizing:border-box}
body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
a{color:var(--gd)}
header.top{position:sticky;top:0;z-index:20;background:var(--g);color:#fff;box-shadow:0 2px 10px #0002}
.bar{max-width:1080px;margin:0 auto;padding:10px 18px;display:flex;align-items:center;gap:14px}
.brand{font-family:var(--disp);font-weight:800;font-size:20px;letter-spacing:.2px}
.brand small{font-weight:400;opacity:.9;font-family:var(--body);font-size:12px}
.tabs{display:flex;gap:6px;margin-left:auto;flex-wrap:wrap}
.tab{border:none;background:#ffffff22;color:#fff;font-weight:700;font-size:13px;padding:7px 13px;border-radius:20px;cursor:pointer;font-family:var(--disp)}
.tab.active{background:#fff;color:var(--gd)}
.tab[disabled]{opacity:.5;cursor:not-allowed}
.themebtn{border:none;background:#ffffff22;color:#fff;width:34px;height:34px;border-radius:50%;cursor:pointer;font-size:15px}
main{max-width:1080px;margin:0 auto;padding:0 18px 80px}
.hero{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;border-radius:20px;padding:26px 28px;margin:22px 0;display:flex;gap:20px;align-items:center;flex-wrap:wrap}
.hero .mo{width:92px;flex:none}
.hero h1{font-family:var(--disp);font-weight:800;font-size:34px;margin:0 0 4px}
.hero p{margin:0;max-width:560px;opacity:.96}
.subnav{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0 8px;position:sticky;top:54px;background:var(--paper);padding:8px 0;z-index:10}
.subnav button{border:1.5px solid var(--line);background:var(--card);color:var(--ink);font-weight:600;font-size:13px;padding:7px 13px;border-radius:20px;cursor:pointer}
.subnav button.on{background:var(--g);color:#fff;border-color:var(--g)}
section.panel{display:none;animation:fade .3s}
section.panel.show{display:block}
@keyframes fade{from{opacity:0;transform:translateY(6px)}to{opacity:1}}
h2.sec{font-family:var(--disp);font-weight:700;color:var(--gd);font-size:24px;margin:22px 0 4px}
.lead{color:var(--mut);margin:0 0 14px;max-width:680px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin:14px 0;box-shadow:0 1px 3px #0000000a}
.gloss{color:var(--mut);font-style:italic}
.btn{border:none;background:var(--g);color:#fff;font-weight:700;border-radius:10px;padding:9px 16px;cursor:pointer;font-family:var(--disp);font-size:14px}
.btn.sec{background:var(--crema);color:var(--ink)}
.btn.small{padding:6px 11px;font-size:13px}
.pill{display:inline-block;background:var(--gt);color:var(--gd);border-radius:20px;padding:3px 10px;font-size:12px;font-weight:600}
/* flip cards */
.controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:6px 0 14px}
.controls input,.controls select{border:1.5px solid var(--line);border-radius:10px;padding:8px 12px;font-size:14px;background:var(--card);color:var(--ink)}
.fcgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
.fc{perspective:900px;height:120px;cursor:pointer}
.fc .in{position:relative;width:100%;height:100%;transition:transform .5s;transform-style:preserve-3d}
.fc.flip .in{transform:rotateY(180deg)}
.fc .s,.fc .b{position:absolute;inset:0;backface-visibility:hidden;border-radius:14px;border:1px solid var(--line);background:var(--card);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:10px;text-align:center}
.fc .s{border-top:4px solid var(--g)}
.fc .b{transform:rotateY(180deg);background:var(--gt);border-top:4px solid var(--gd)}
.fc .w{font-family:var(--disp);font-weight:700;font-size:17px}
.fc .ej{font-size:11px;color:var(--mut);margin-top:6px}
.fc .tr{font-family:var(--disp);font-weight:700;font-size:18px;color:var(--gd)}
/* tabel */
table.vt{width:100%;border-collapse:collapse;font-size:14px}
table.vt th,table.vt td{border-bottom:1px solid var(--line);padding:8px 10px;text-align:left}
table.vt th{background:var(--gt);color:var(--gd);position:sticky;top:96px}
/* game generiek */
.game{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin:14px 0}
.game h3{font-family:var(--disp);margin:0 0 2px;color:var(--ink);font-size:18px}
.game .desc{color:var(--mut);font-size:13px;margin:0 0 12px}
.scorebar{display:flex;gap:14px;align-items:center;font-size:13px;color:var(--mut);margin-bottom:10px}
.scorebar b{color:var(--gd)}
.chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{border:1.5px solid var(--line);background:var(--card);border-radius:12px;padding:9px 14px;font-weight:600;cursor:pointer;font-size:15px;user-select:none}
.chip.sel{border-color:var(--g);background:var(--gt)}
.chip.ok{border-color:var(--g);background:var(--g);color:#fff}
.chip.no{border-color:var(--red);background:#fde8e8}
.cols{display:grid;gap:12px;margin-top:6px}
.col{border:1.5px dashed var(--line);border-radius:12px;padding:10px;min-height:70px}
.col h4{margin:0 0 8px;font-size:13px;color:var(--gd);text-transform:uppercase;letter-spacing:.04em}
.fb{margin-top:12px;padding:10px 14px;border-radius:10px;font-size:14px;display:none}
.fb.good{display:block;background:var(--gt);color:var(--gd)}
.fb.bad{display:block;background:#fdeaea;color:var(--red)}
.answerbtns{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}
/* kleur-zin */
.csent{font-size:22px;font-family:var(--disp);line-height:2}
.csent span{padding:2px 5px;border-radius:6px;cursor:help;position:relative}
.csent .tip{display:none;position:absolute;left:50%;top:120%;transform:translateX(-50%);background:var(--ink);color:#fff;font-size:12px;font-family:var(--body);padding:5px 9px;border-radius:6px;white-space:nowrap;z-index:5}
.csent span:hover .tip,.csent span:focus .tip{display:block}
.legend{display:flex;gap:10px;flex-wrap:wrap;font-size:12px;margin-top:10px}
.legend i{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:4px;vertical-align:-1px}
/* conjugador */
.conjgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-top:12px}
.pv{background:var(--gt);border-radius:12px;padding:10px 12px}
.pv .p{font-size:12px;color:var(--mut)}
.pv .f{font-family:var(--disp);font-weight:700;font-size:18px;color:var(--gd)}
.foot{color:var(--mut);font-size:12px;text-align:center;margin-top:30px}
.tilinfo{font-size:13px;color:var(--mut)}
.wheel{display:flex;gap:20px;align-items:center;flex-wrap:wrap;justify-content:center;margin-top:8px}
.wcirc{position:relative;width:230px;height:230px}
.wcirc button{position:absolute;transform:translate(-50%,-50%);border:1.5px solid var(--line);background:var(--card);border-radius:20px;padding:6px 10px;font-weight:700;cursor:pointer;font-size:13px}
.wcirc button.on{background:var(--g);color:#fff;border-color:var(--g)}
.wcirc .mid{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:120px;height:120px;border-radius:50%;background:var(--gt);display:flex;flex-direction:column;align-items:center;justify-content:center}
.wcirc .mid .v{font-family:var(--disp);font-weight:800;font-size:24px;color:var(--gd)}
@media(max-width:600px){.hero h1{font-size:26px}.bar{flex-wrap:wrap}}
"""

def data_js():
    return "const VOCAB="+json.dumps(vocab,ensure_ascii=False)+";\n"

# ------- HTML secties -------
def flashcards_html():
    return """<div class="controls">
      <input id="fcsearch" placeholder="🔎 zoek woord / palabra…" oninput="renderFC()">
      <select id="fcdir" onchange="renderFC()"><option value="es">ES → NL</option><option value="nl">NL → ES</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

def conjugador_html():
    return """<p class="lead">Typ een werkwoord (infinitivo) en zie de <b>presente</b>. Onregelmatige kernwerkwoorden zijn nagerekend. <span class="gloss">Enkel presente — conform het leerplan (geen futuro/subjuntivo in de 3de graad).</span></p>
    <div class="controls"><input id="verbin" placeholder="bv. hablar, comer, vivir, ser, tener…" value="hablar" oninput="conjugate()"><button class="btn small" onclick="conjugate()">Vervoeg</button></div>
    <div id="conjout"></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Español en la práctica · U0 ¡Empezamos!</title>
<style>__CSS__</style></head><body>
<header class="top"><div class="bar">
  <div class="brand">Español en la práctica <small>· la página digital</small></div>
  <div class="tabs">
    <button class="tab" disabled>C4 · Welcome</button>
    <button class="tab active">C5 · A1</button>
    <button class="tab" disabled>C6 · Clean</button>
    <button class="tab" disabled>C6+ · Vervolg</button>
  </div>
  <button class="themebtn" onclick="toggleTheme()" title="licht/donker">◐</button>
</div></header>
<main>
  <div class="hero">
    <div class="mo">__MOCH__</div>
    <div><h1>U0 · ¡Empezamos!</h1>
    <p>La página digital de la Unidad 0: flashcards, woordenschat, <b>conjugador</b>, gramática visual e interactiva y <b>juegos</b>. <span style="opacity:.85">Todo lo que en el libro (PDF) tiene un QR, aquí lo puedes practicar.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U0. Klik om te draaien; wissel ES↔NL. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
    __FC__
    <h2 class="sec">Naslagwerk · zoeken</h2>
    __NAS__
  </section>

  <section class="panel" data-p="gram">
    <h2 class="sec">Gramática visual e interactiva</h2>
    <p class="lead">Eerst betekenis en patroon ontdekken, dan de regel. Beweeg over de woorden, klik, en probeer.</p>
    <div class="card" id="colorsent"></div>
    <div class="game" id="g_tilde"></div>
    <div class="game" id="g_silaba"></div>
    <div class="card" id="wheel"></div>
  </section>

  <section class="panel" data-p="juegos">
    <h2 class="sec">Juegos · oefenen met feedback</h2>
    <p class="lead">Receptief → productief. Elke ronde met directe, verklarende feedback.</p>
    <div class="game" id="g_sonido"></div>
    <div class="game" id="g_sombrero"></div>
    <div class="game" id="g_numeros"></div>
    <div class="game" id="g_saludos"></div>
    <div class="game" id="g_genero"></div>
    <div class="game" id="g_orden"></div>
    <div class="game" id="g_memory"></div>
    <div class="card" id="motorlink"></div>
  </section>

  <section class="panel" data-p="conjug">
    <h2 class="sec">Conjugador</h2>
    __CONJ__
  </section>

  <section class="panel" data-p="cultura">
    <h2 class="sec">Cultura · el mundo hispano</h2>
    <p class="lead">+20 países, ~500 miljoen sprekers. Onze route dit jaar: España → México → Colombia → Perú.</p>
    <div class="card">__MAP__</div>
  </section>

  <section class="panel" data-p="extra">
    <h2 class="sec">Extra · bronnen</h2>
    <p class="lead">Externe uitleg & oefeningen (de leerkracht vult de links aan).</p>
    <div class="card"><p>🎬 <b>profedeele</b> (YouTube-grammatica) — <span class="gloss">link volgt.</span></p>
    <p>🧩 <b>arche-ele</b> (Genially woordenschat/grammatica) — <span class="gloss">link volgt.</span></p>
    <p>📄 In het boek (PDF) verwijzen de QR-codes naar déze pagina, op het juiste ankerpunt.</p></div>
  </section>

  <div class="foot">Español en la práctica · C5 · Unidad 0 — página digital (v1). Huisstijl groen · print ↔ PowerPoint ↔ web.</div>
</main>
<script>__DATA__
__JS__
</script></body></html>"""

JS = r"""
function toggleTheme(){const r=document.documentElement;r.dataset.theme=r.dataset.theme==='dark'?'light':'dark'}
// subnav
const PANELS=[['vocab','Vocabulario'],['gram','Gramática'],['juegos','Juegos'],['conjug','Conjugador'],['cultura','Cultura'],['extra','Extra']];
const sn=document.getElementById('subnav');
PANELS.forEach((p,i)=>{const b=document.createElement('button');b.textContent=p[1];if(i===0)b.classList.add('on');b.onclick=()=>{
  document.querySelectorAll('.subnav button').forEach(x=>x.classList.remove('on'));b.classList.add('on');
  document.querySelectorAll('.panel').forEach(x=>x.classList.remove('show'));
  document.querySelector('.panel[data-p="'+p[0]+'"]').classList.add('show');window.scrollTo({top:0,behavior:'smooth'});};sn.appendChild(b);});

// ---------- flashcards ----------
let FCorder=VOCAB.map((_,i)=>i);
function shuffleFC(){for(let i=FCorder.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[FCorder[i],FCorder[j]]=[FCorder[j],FCorder[i]]}renderFC()}
function renderFC(){const q=(document.getElementById('fcsearch').value||'').toLowerCase();const dir=document.getElementById('fcdir').value;
  const g=document.getElementById('fcgrid');g.innerHTML='';let n=0;
  FCorder.forEach(i=>{const v=VOCAB[i];if(q&&!(v.es.toLowerCase().includes(q)||v.nl.toLowerCase().includes(q)))return;n++;
    const front=dir==='es'?v.es:v.nl, back=dir==='es'?v.nl:v.es, ej=dir==='es'?('«'+v.ej+'»'):'';
    const d=document.createElement('div');d.className='fc';d.tabIndex=0;
    d.innerHTML='<div class="in"><div class="s"><div class="w">'+front+'</div>'+(ej?'<div class="ej">'+ej+'</div>':'')+'</div><div class="b"><div class="tr">'+back+'</div></div></div>';
    d.onclick=()=>d.classList.toggle('flip');d.onkeydown=e=>{if(e.key===' '||e.key==='Enter'){e.preventDefault();d.classList.toggle('flip')}};
    g.appendChild(d);});
  document.getElementById('fccount').textContent=n+' woorden';}
// ---------- naslag ----------
function renderTable(){const q=(document.getElementById('vsearch').value||'').toLowerCase();const b=document.getElementById('vbody');b.innerHTML='';let n=0;
  VOCAB.forEach(v=>{if(q&&!(v.es.toLowerCase().includes(q)||v.nl.toLowerCase().includes(q)||v.ej.toLowerCase().includes(q)))return;n++;
    const tr=document.createElement('tr');tr.innerHTML='<td><b>'+v.es+'</b></td><td>'+v.nl+'</td><td>'+v.soort+'</td><td class="gloss">'+v.ej+'</td>';b.appendChild(tr);});
  document.getElementById('vcount').textContent=n+' items';}

// ---------- conjugador ----------
const IRR={ser:['soy','eres','es','somos','sois','son'],estar:['estoy','estás','está','estamos','estáis','están'],
 tener:['tengo','tienes','tiene','tenemos','tenéis','tienen'],ir:['voy','vas','va','vamos','vais','van'],
 hacer:['hago','haces','hace','hacemos','hacéis','hacen'],ll:0};
const PRON=['yo','tú','él/ella','nosotros','vosotros','ellos/ellas'];
function conjugate(){const raw=(document.getElementById('verbin').value||'').trim().toLowerCase();const out=document.getElementById('conjout');
  if(!raw){out.innerHTML='';return}
  let forms,note='';
  if(IRR[raw]){forms=IRR[raw];note='onregelmatig (nagerekend)';}
  else if(/ar$|er$|ir$/.test(raw)){const st=raw.slice(0,-2);const t=raw.slice(-2);
    const E={ar:['o','as','a','amos','áis','an'],er:['o','es','e','emos','éis','en'],ir:['o','es','e','imos','ís','en']}[t];
    forms=E.map(e=>st+e);note='regelmatig · -'+t;}
  else{out.innerHTML='<p class="gloss">Geef een infinitivo op -ar / -er / -ir (bv. hablar, comer, vivir) of een kernwerkwoord (ser, estar, tener, ir, hacer).</p>';return}
  out.innerHTML='<div class="pill">presente · '+note+'</div><div class="conjgrid">'+
    forms.map((f,i)=>'<div class="pv"><div class="p">'+PRON[i]+'</div><div class="f">'+f+'</div></div>').join('')+'</div>';}

// ---------- helpers spellen ----------
function scoreBar(id){return '<div class="scorebar" id="'+id+'"><span>Punten: <b class="pt">0</b></span><span>Reeks: <b class="st">0</b></span></div>'}
function setScore(el,pt,st){el.querySelector('.pt').textContent=pt;el.querySelector('.st').textContent=st}
function feedback(el,ok,msg){el.className='fb '+(ok?'good':'bad');el.innerHTML=(ok?'✅ ':'❌ ')+msg}

// ---------- kleur-zin (grammar-viz 1) ----------
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Kleurgecodeerde zin — beweeg over de woorden</h3>'+
'<div class="csent">'+
'<span style="background:#dbeafe;color:#1e40af">Yo<span class="tip">onderwerp (persona)</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">me llamo<span class="tip">werkwoord (llamarse)</span></span> '+
'<span style="background:#dcfce7;color:#166534">Lucía<span class="tip">naam / voorwerp</span></span> '+
'<span style="background:#ede9fe;color:#5b21b6">hoy<span class="tip">tijd (ahora)</span></span>.</div>'+
'<div class="legend"><span><i style="background:#93c5fd"></i>onderwerp</span><span><i style="background:#fdba74"></i>werkwoord</span><span><i style="background:#86efac"></i>voorwerp</span><span><i style="background:#c4b5fd"></i>tijd</span></div>';

// ---------- vervoegingscirkel (grammar-viz 8) ----------
(function(){const box=document.getElementById('wheel');const verb='hablar';const st='habl';const E=['o','as','a','amos','áis','an'];
 box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Vervoegingscirkel — klik een persoon</h3><p class="desc" style="color:var(--mut)">'+verb+' (presente). Klik yo/tú/…</p><div class="wheel"><div class="wcirc" id="wc"></div></div>';
 const wc=document.getElementById('wc');const R=95,cx=115,cy=115;
 wc.innerHTML='<div class="mid"><div class="p" style="font-size:12px;color:var(--mut)">'+verb+'</div><div class="v" id="wv">—</div></div>';
 PRON.forEach((p,i)=>{const a=(-90+i*60)*Math.PI/180;const x=cx+R*Math.cos(a),y=cy+R*Math.sin(a);
   const b=document.createElement('button');b.textContent=p;b.style.left=x+'px';b.style.top=y+'px';
   b.onclick=()=>{wc.querySelectorAll('button').forEach(z=>z.classList.remove('on'));b.classList.add('on');document.getElementById('wv').textContent=st+E[i]};wc.appendChild(b);});
})();

// ---------- GAME: klank sorteren (b=v / h muda / jota) ----------
function gameSonido(){const el=document.getElementById('g_sonido');
 const items=[['vaca','bv'],['bota','bv'],['hola','h'],['hora','h'],['jamón','j'],['gente','j'],['vino','bv'],['hijo','h'],['gigante','j']];
 const cats={bv:'b = v (zelfde klank)',h:'h · zwijgt',j:'jota (j · ge · gi)'};
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>Klank-detective</h3><p class="desc">In welke klankfamilie hoort het woord? Klik het woord, klik dan de familie.</p>'+scoreBar('sb1')+
  '<div id="s1word" style="font-size:26px;font-family:var(--disp);text-align:center;margin:8px 0"></div>'+
  '<div class="chips" id="s1cats"></div><div class="fb" id="s1fb"></div>';
 const sb=el.querySelector('#sb1');const cont=el.querySelector('#s1cats');
 Object.entries(cats).forEach(([k,v])=>{const c=document.createElement('div');c.className='chip';c.textContent=v;c.onclick=()=>guess(k);cont.appendChild(c);});
 function next(){if(!pool.length)pool=items.slice();const idx=Math.floor(Math.random()*pool.length);el.cur=pool.splice(idx,1)[0];el.querySelector('#s1word').textContent=el.cur[0];el.querySelector('#s1fb').className='fb';}
 function guess(k){const ok=k===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);
   const ex={bv:'b en v klinken identiek in het Spaans.',h:'de h wordt niet uitgesproken.',j:'j, en ge/gi, klinken als een harde keel-ch.'};
   feedback(el.querySelector('#s1fb'),ok,ok?('«'+el.cur[0]+'» — juist! '+ex[el.cur[1]]):('«'+el.cur[0]+'» hoort bij: '+cats[el.cur[1]]+'. '+ex[el.cur[1]]));setTimeout(next,900);}
 next();}
// ---------- GAME: la regla del sombrero ----------
function gameSombrero(){const el=document.getElementById('g_sombrero');
 const items=[['café','aguda'],['casa','llana'],['México','esdrujula'],['Perú','aguda'],['árbol','llana'],['teléfono','esdrujula'],['lunes','llana'],['adiós','aguda'],['música','esdrujula']];
 const cats={aguda:'aguda (laatste)',llana:'llana (voorlaatste)',esdrujula:'esdrújula (3e van achteren)'};
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>La regla del sombrero</h3><p class="desc">Waar ligt de klemtoon? Kies de familie.</p>'+scoreBar('sb2')+
  '<div id="s2word" style="font-size:26px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" id="s2cats"></div><div class="fb" id="s2fb"></div>';
 const sb=el.querySelector('#sb2');const cont=el.querySelector('#s2cats');
 Object.entries(cats).forEach(([k,v])=>{const c=document.createElement('div');c.className='chip';c.textContent=v;c.onclick=()=>guess(k);cont.appendChild(c);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#s2word').textContent=el.cur[0];el.querySelector('#s2fb').className='fb';}
 function guess(k){const ok=k===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);
   feedback(el.querySelector('#s2fb'),ok,ok?'¡Correcto! «'+el.cur[0]+'» is '+cats[el.cur[1]]+'.':'«'+el.cur[0]+'» is '+cats[el.cur[1]]+'.');setTimeout(next,900);}
 next();}
// ---------- GAME: números match ----------
function gameNumeros(){const el=document.getElementById('g_numeros');
 const P=[[3,'tres'],[7,'siete'],[12,'doce'],[16,'dieciséis'],[21,'veintiuno'],[40,'cuarenta'],[55,'cincuenta y cinco'],[100,'cien']];
 buildMatch(el,'Números — verbind cijfer en woord',P.map(p=>[String(p[0]),p[1]]));}
// ---------- GAME: saludos match ----------
function gameSaludos(){const el=document.getElementById('g_saludos');
 const P=[['¡Hola!','hallo'],['Buenos días','goedemorgen'],['Buenas noches','goedenacht'],['¿Qué tal?','hoe gaat het?'],['Hasta luego','tot straks'],['Encantada','aangenaam (v.)']];
 buildMatch(el,'Saludos — verbind ES en NL',P);}
// generieke match (klik links, klik rechts)
function buildMatch(el,title,pairs){let pt=0,st=0,sel=null,done=0;
 const L=pairs.map(p=>p[0]),Rr=pairs.map(p=>p[1]).slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>'+title+'</h3><p class="desc">Klik een kaart links, dan de juiste rechts.</p>'+scoreBar('m'+title.length)+
  '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px"><div class="chips" style="flex-direction:column" id="mL"></div><div class="chips" style="flex-direction:column" id="mR"></div></div><div class="fb" id="mfb"></div>';
 const sb=el.querySelector('.scorebar');const cL=el.querySelector('#mL'),cR=el.querySelector('#mR');
 L.forEach((t,i)=>{const c=document.createElement('div');c.className='chip';c.textContent=t;c.dataset.i=i;c.onclick=()=>{cL.querySelectorAll('.chip').forEach(z=>z.classList.remove('sel'));c.classList.add('sel');sel=i};cL.appendChild(c);});
 Rr.forEach(t=>{const c=document.createElement('div');c.className='chip';c.textContent=t;c.onclick=()=>{if(sel==null){return}const want=pairs[sel][1];const ok=t===want;
   if(ok){c.classList.add('ok');cL.querySelector('.chip[data-i="'+sel+'"]').classList.add('ok');pt++;st++;done++;feedback(el.querySelector('#mfb'),true,pairs[sel][0]+' → '+t);
     if(done===pairs.length)feedback(el.querySelector('#mfb'),true,'¡Completado! '+pt+' correct.');}
   else{st=0;c.classList.add('no');setTimeout(()=>c.classList.remove('no'),500);feedback(el.querySelector('#mfb'),false,'Probeer opnieuw.');}
   setScore(sb,pt,st);sel=null;cL.querySelectorAll('.chip').forEach(z=>z.classList.remove('sel'));};cR.appendChild(c);});}
// ---------- GAME: ¿el o la? ----------
function gameGenero(){const el=document.getElementById('g_genero');
 const items=[['mapa','el'],['casa','la'],['problema','el'],['ciudad','la'],['día','el'],['mano','la'],['idioma','el'],['letra','la'],['acento','el'],['sílaba','la']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿el o la?</h3><p class="desc">Kies het juiste lidwoord. Let op de valstrikken (el mapa, el día…).</p>'+scoreBar('sb4')+
  '<div id="s4word" style="font-size:26px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._genGuess(\'el\')">el</div><div class="chip" onclick="window._genGuess(\'la\')">la</div></div><div class="fb" id="s4fb"></div>';
 const sb=el.querySelector('#sb4');
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#s4word').textContent=el.cur[0];el.querySelector('#s4fb').className='fb';}
 window._genGuess=k=>{const ok=k===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);
   feedback(el.querySelector('#s4fb'),ok,(ok?'¡Sí! ':'Nee → ')+el.cur[1]+' '+el.cur[0]);setTimeout(next,850);};
 next();}
// ---------- GAME: woordvolgorde ----------
function gameOrden(){const el=document.getElementById('g_orden');
 const sol=['Yo','me llamo','Diego','y','soy de México'];let cur=[],pool=sol.slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>Bouw de zin — sleepbare woordvolgorde</h3><p class="desc">Klik de tegels in de juiste volgorde. Doel: een correcte voorstelzin.</p>'+
  '<div class="chips" id="oPool"></div><div class="col" id="oZone" style="margin-top:10px"><h4>jouw zin</h4><div class="chips" id="oBuilt"></div></div><div class="answerbtns"><button class="btn small" onclick="window._ordCheck()">Controleer</button><button class="btn sec small" onclick="window._ordReset()">Reset</button></div><div class="fb" id="oFb"></div>';
 function draw(){const p=el.querySelector('#oPool');p.innerHTML='';pool.forEach((w,i)=>{const c=document.createElement('div');c.className='chip';c.textContent=w;c.onclick=()=>{cur.push(w);pool.splice(i,1);draw();built();};p.appendChild(c);});}
 function built(){const b=el.querySelector('#oBuilt');b.innerHTML='';cur.forEach((w,i)=>{const c=document.createElement('div');c.className='chip sel';c.textContent=w;c.onclick=()=>{pool.push(w);cur.splice(i,1);draw();built();};b.appendChild(c);});}
 window._ordCheck=()=>{const ok=cur.join(' ')===sol.join(' ');feedback(el.querySelector('#oFb'),ok,ok?'¡Perfecto! «'+sol.join(' ')+'».':'Nog niet — let op: onderwerp → werkwoord → rest.');};
 window._ordReset=()=>{cur=[];pool=sol.slice().sort(()=>Math.random()-.5);draw();built();el.querySelector('#oFb').className='fb';};
 draw();built();}
// ---------- GAME: memory (vocab) ----------
function gameMemory(){const el=document.getElementById('g_memory');
 const pick=VOCAB.filter(v=>v.es.length<12&&!v.es.includes('/')&&!v.es.includes('→')).slice(0,6);
 let cards=[];pick.forEach(v=>{cards.push({k:v.es,t:v.es,g:v.es});cards.push({k:v.es,t:v.nl,g:v.es});});
 cards.sort(()=>Math.random()-.5);let open=[],found=0,moves=0;
 el.innerHTML='<h3>Memoria — vind de paren ES/NL</h3><p class="desc">Draai twee kaarten; match Spaans met Nederlands.</p><div class="scorebar" id="mmSb"><span>Zetten: <b class="pt">0</b></span><span>Paren: <b class="st">0</b>/6</span></div><div class="fcgrid" id="mmGrid"></div><div class="fb" id="mmFb"></div>';
 const sb=el.querySelector('#mmSb');const g=el.querySelector('#mmGrid');
 cards.forEach((c,i)=>{const d=document.createElement('div');d.className='fc';d.style.height='84px';d.tabIndex=0;
   d.innerHTML='<div class="in"><div class="s" style="border-top-color:var(--mut)"><div class="w" style="font-size:20px">?</div></div><div class="b" style="transform:rotateY(180deg)"><div style="font-weight:700">'+c.t+'</div></div></div>';
   d.onclick=()=>{if(d.classList.contains('flip')||open.length===2||d.dataset.done)return;d.classList.add('flip');open.push({d,c});
     if(open.length===2){moves++;sb.querySelector('.pt').textContent=moves;
       if(open[0].c.g===open[1].c.g&&open[0].d!==open[1].d){open.forEach(o=>{o.d.dataset.done=1});found++;sb.querySelector('.st').textContent=found;open=[];if(found===6)feedback(el.querySelector('#mmFb'),true,'¡Completado en '+moves+' zetten!');}
       else setTimeout(()=>{open.forEach(o=>o.d.classList.remove('flip'));open=[];},700);}};
   g.appendChild(d);});}

// ---------- GRAMMAR-VIZ: sílaba tónica tapper ----------
function gameSilaba(){const el=document.getElementById('g_silaba');
 const W=[[['ca','fé'],1],[['ca','sa'],0],[['mé','xi','co'],0],[['te','lé','fo','no'],1],[['pe','rú'],1],[['lu','nes'],0],[['plá','ta','no'],0],[['a','diós'],1]];
 let pool=W.slice(),pt=0,st=0;
 el.innerHTML='<h3>Tik de tónica — welke lettergreep zeg je het sterkst?</h3><p class="desc">Klik de sterke lettergreep. Daarna zie je de familie.</p>'+scoreBar('sbT')+'<div class="chips" id="tapW" style="justify-content:center;font-size:20px"></div><div class="fb" id="tapFb"></div>';
 const sb=el.querySelector('#sbT');
 function fam(syl,ton){const n=syl.length;const fromEnd=n-1-ton;return fromEnd===0?'aguda':fromEnd===1?'llana':'esdrújula';}
 function next(){if(!pool.length)pool=W.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];const [syl,ton]=el.cur;const c=el.querySelector('#tapW');c.innerHTML='';
   syl.forEach((s,idx)=>{const b=document.createElement('div');b.className='chip';b.textContent=s;b.onclick=()=>{const ok=idx===ton;if(ok){pt++;st++}else st=0;setScore(sb,pt,st);
     c.querySelectorAll('.chip').forEach((z,zi)=>{if(zi===ton)z.classList.add('ok');else if(zi===idx&&!ok)z.classList.add('no');});
     feedback(el.querySelector('#tapFb'),ok,(ok?'¡Sí! ':'De tónica is «'+syl[ton]+'». ')+'«'+syl.join('·')+'» is '+fam(syl,ton)+'.');setTimeout(next,1000);};c.appendChild(b);});
   el.querySelector('#tapFb').className='fb';}
 next();}
// ---------- GRAMMAR-VIZ: ¿lleva tilde? (regel ontdekken) ----------
function gameTilde(){const el=document.getElementById('g_tilde');
 const W=[['café',true,'aguda, eindigt op klinker'],['casa',false,'llana, eindigt op klinker'],['México',true,'esdrújula'],['árbol',true,'llana, eindigt op -l'],['lunes',false,'llana, eindigt op -s'],['adiós',true,'aguda, eindigt op -s'],['reloj',false,'aguda, eindigt op -j'],['música',true,'esdrújula']];
 let pool=W.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿Lleva tilde? — de regel van het hoedje</h3><p class="desc">Draagt dit woord een accent (´)? Beslis en ontdek waarom.</p>'+scoreBar('sbTi')+'<div id="tiWord" style="font-size:26px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._tiGuess(true)">sí, lleva ´</div><div class="chip" onclick="window._tiGuess(false)">no lleva</div></div><div class="fb" id="tiFb"></div>';
 const sb=el.querySelector('#sbTi');
 function strip(w){return w.normalize('NFD').replace(/[̀-ͯ]/g,'');}
 function next(){if(!pool.length)pool=W.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#tiWord').textContent=strip(el.cur[0]);el.querySelector('#tiFb').className='fb';}
 window._tiGuess=g=>{const ok=g===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);
   feedback(el.querySelector('#tiFb'),ok,(ok?'¡Correcto! ':'')+'«'+el.cur[0]+'» — '+el.cur[2]+(el.cur[1]?' → wél een hoedje.':' → géén hoedje.'));setTimeout(next,1100);};
 next();}
// motorlink kaart
document.getElementById('motorlink').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 4px">Meer spellen (motor)</h3><p class="gloss" style="margin:0">De offline arcade-spellen van de spaans-motor (classify · match · tetris · …) worden hier per thema ingebed. Ze staan in <code>spaans-motor/games/</code>.</p>';

// init
renderFC();renderTable();conjugate();gameSilaba();gameTilde();gameSonido();gameSombrero();gameNumeros();gameSaludos();gameGenero();gameOrden();gameMemory();
// hash-navigatie (deep-link naar een paneel)
(function(){const h=location.hash.replace('#','');const i=PANELS.findIndex(p=>p[0]===h);if(i>=0)sn.children[i].click();})();
window.addEventListener('hashchange',()=>{const h=location.hash.replace('#','');const i=PANELS.findIndex(p=>p[0]===h);if(i>=0)sn.children[i].click();});
"""

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__CONJ__",conjugador_html())
      .replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/U0_web.html","w").write(html)
print("U0_web.html geschreven:", len(html), "bytes")
