#!/usr/bin/env python3
# Conjugador (cursus-niveau, apart deliverable) — PRESENTE, regelmatig + onregelmatig.
# Twee lagen: (1) Opzoeken — de leerling ZIET de vervoeging; (2) Zelf vervoegen —
# persona + infinitivo + context → de leerling vervoegt zelf (nagerekend, nooit zelf raden).
# Conform leerplan III-Spa-d: ENKEL presente (geen futuro/condicional/subjuntivo).
import json, base64, os

ROOT="/home/user/espa-ol-en-la-pr-ctica"

def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(fam,path,w):
    return f"@font-face{{font-family:'{fam}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{path}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([
 face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),
 face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"), face("Inter","Inter-600.woff2","600"),
 face("Caveat","Caveat-700.woff2","700"),
])

# ---------------- WERKWOORDDATABASE (nagerekend via de motor-engine) ----------------
# 324 frequentste werkwoorden, vormen voorgerekend door de motor (03-build/web/extract_verbos.mjs).
motor=json.load(open(f"{ROOT}/03-build/web/verbos_es.json"))
# Context-situaties voor de oefenmodus (waar we ze hebben; anders neutraal frame).
SITS={
 'hablar':'en clase de idiomas','estudiar':'para el examen','trabajar':'en una tienda','escuchar':'música',
 'cantar':'en la fiesta','bailar':'salsa','viajar':'por Latinoamérica','comprar':'pan en el mercado',
 'cocinar':'una tortilla','tomar':'un café','mirar':'una película','llegar':'tarde a clase',
 'descansar':'el domingo','necesitar':'ayuda','llevar':'una mochila','preguntar':'a la profesora',
 'comer':'a las dos','beber':'agua','leer':'un libro','aprender':'español','correr':'en el parque',
 'vender':'fruta','deber':'estudiar más','comprender':'la pregunta','vivir':'en Madrid','escribir':'un mensaje',
 'abrir':'la ventana','recibir':'un regalo','subir':'al autobús','ser':'de España','estar':'en casa',
 'ir':'al cine','tener':'catorce años','hacer':'los deberes','ver':'la tele','dar':'un regalo',
 'saber':'la respuesta','poder':'venir hoy','querer':'un café','poner':'la mesa','venir':'a la fiesta',
 'decir':'la verdad','salir':'con amigos','jugar':'al fútbol','dormir':'ocho horas','pedir':'una pizza',
 'pensar':'en el futuro','empezar':'la clase','entender':'la gramática','volver':'a casa','encontrar':'las llaves',
 'conocer':'a mucha gente','trabajar ':'',
}
DB=[]; seen=set()
for v in motor:
    v=dict(v); v['sit']=SITS.get(v['inf'],''); DB.append(v); seen.add(v['inf'])
# extra (niet in de motor-lijst): wederkerend voorbeeld voor U0-koppeling
for v in [{'inf':'llamarse','nl':'heten','type':'wederkerend','forms':['me llamo','te llamas','se llama','nos llamamos','os llamáis','se llaman'],'sit':'Lucía'}]:
    if v['inf'] not in seen: DB.append(v)
DB.sort(key=lambda v:v['inf'])

CSS = FONTS + """
:root{--g:#1E9E74;--gd:#157355;--gt:#E4F4EE;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E4E3DE;--red:#DC2626;--amber:#B7860B;--card:#fff;
--p0:#2563EB;--p1:#EA7317;--p2:#1E9E74;--p3:#7C3AED;--p4:#0EA5A5;--p5:#DC2626;
--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif;--hand:'Caveat',cursive}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#171713;--crema:#22221C;--gt:#12352A;--line:#33332B;--card:#20201A}
*{box-sizing:border-box}
body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
header.top{position:sticky;top:0;z-index:30;background:var(--g);color:#fff;box-shadow:0 2px 10px #0002}
.bar{max-width:960px;margin:0 auto;padding:12px 18px;display:flex;align-items:center;gap:12px}
.brand{font-family:var(--disp);font-weight:800;font-size:20px}
.brand small{font-weight:400;opacity:.9;font-family:var(--body);font-size:12px}
.themebtn{margin-left:auto;border:none;background:#ffffff22;color:#fff;width:34px;height:34px;border-radius:50%;cursor:pointer;font-size:15px}
main{max-width:960px;margin:0 auto;padding:0 18px 80px}
.hero{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;border-radius:20px;padding:22px 26px;margin:20px 0}
.hero h1{font-family:var(--disp);font-weight:800;font-size:30px;margin:0 0 4px}
.hero p{margin:0;max-width:640px;opacity:.96}
.tabs{display:flex;gap:8px;margin:16px 0;flex-wrap:wrap}
.tab{border:1.5px solid var(--line);background:var(--card);color:var(--ink);font-weight:700;font-size:14px;padding:9px 16px;border-radius:22px;cursor:pointer;font-family:var(--disp)}
.tab.on{background:var(--g);color:#fff;border-color:var(--g)}
section.pane{display:none}section.pane.show{display:block}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin:14px 0;box-shadow:0 1px 3px #0000000a}
.gloss{color:var(--mut);font-style:italic}
.controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:6px 0 12px}
.controls input,.controls select{border:1.5px solid var(--line);border-radius:10px;padding:9px 12px;font-size:15px;background:var(--card);color:var(--ink)}
.btn{border:none;background:var(--g);color:#fff;font-weight:700;border-radius:10px;padding:9px 16px;cursor:pointer;font-family:var(--disp);font-size:14px}
.btn.sec{background:var(--crema);color:var(--ink)}.btn.small{padding:7px 12px;font-size:13px}
.pill{display:inline-block;background:var(--gt);color:var(--gd);border-radius:20px;padding:3px 11px;font-size:12px;font-weight:700}
.vchips{display:flex;gap:7px;flex-wrap:wrap;margin-top:6px}
.vchip{border:1.5px solid var(--line);background:var(--card);border-radius:11px;padding:6px 11px;font-weight:700;cursor:pointer;font-size:14px}
.vchip:hover{border-color:var(--g)}.vchip.on{background:var(--g);color:#fff;border-color:var(--g)}
.vchip small{font-weight:400;color:var(--mut);margin-left:4px}.vchip.on small{color:#dff}
.conj{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-top:14px}
.pv{border-radius:12px;padding:10px 14px;border-left:5px solid var(--g);background:var(--gt)}
.pv.p0{border-color:var(--p0)}.pv.p1{border-color:var(--p1)}.pv.p2{border-color:var(--p2)}.pv.p3{border-color:var(--p3)}.pv.p4{border-color:var(--p4)}.pv.p5{border-color:var(--p5)}
.pv .pr{font-size:12px;color:var(--mut)}
.pv .fm{font-family:var(--disp);font-weight:800;font-size:20px;color:var(--ink)}
.hdr{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.hdr h2{font-family:var(--disp);color:var(--gd);margin:0;font-size:26px}
.ex{margin-top:12px;background:var(--crema);border-radius:10px;padding:9px 13px;font-size:14px}
table.vt{width:100%;border-collapse:collapse;font-size:13.5px;margin-top:8px}
table.vt th,table.vt td{border-bottom:1px solid var(--line);padding:7px 9px;text-align:left}
table.vt th{background:var(--gt);color:var(--gd);position:sticky;top:0;font-size:12px}
table.vt td.m{font-family:var(--disp);font-weight:700}
/* practica */
.scorebar{display:flex;gap:16px;font-size:13px;color:var(--mut);margin:4px 0 12px}.scorebar b{color:var(--gd)}
.qbox{font-size:20px;font-family:var(--disp);margin:6px 0}
.qbox .gap{display:inline-block;min-width:90px;border-bottom:2.5px solid var(--g);color:var(--g);text-align:center}
.cue{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:8px 0}
.txin{border:1.5px solid var(--line);border-radius:10px;padding:9px 12px;font-size:17px;background:var(--card);color:var(--ink);font-family:var(--disp);width:180px}
.fb{margin-top:12px;padding:11px 14px;border-radius:10px;font-size:14px;display:none}
.fb.good{display:block;background:var(--gt);color:var(--gd)}.fb.bad{display:block;background:#fdeaea;color:var(--red)}
.foot{color:var(--mut);font-size:12px;text-align:center;margin-top:30px}
@media(max-width:600px){.hero h1{font-size:24px}}
"""

PRON=['yo','tú','él / ella / usted','nosotros/as','vosotros/as','ellos / ellas / ustedes']
PRONs=['yo','tú','él','nosotros','vosotros','ellos']

HTML="""<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Conjugador · presente · Español en la práctica</title>
<style>__CSS__</style></head><body>
<header class="top"><div class="bar">
  <div class="brand">Conjugador <small>· presente · Español en la práctica</small></div>
  <button class="themebtn" onclick="toggleTheme()" title="licht/donker">◐</button>
</div></header>
<main>
  <div class="hero"><h1>El conjugador — presente</h1>
    <p>Werkwoorden in de <b>tegenwoordige tijd</b>, regelmatig én onregelmatig. Twee lagen: <b>opzoeken</b> (je ziet de vervoeging) en <b>zelf vervoegen</b> (persona + infinitivo + context → jij vervoegt). <span style="opacity:.85">Conform het leerplan: enkel presente — geen futuro, condicional of subjuntivo.</span></p></div>
  <div class="tabs">
    <button class="tab on" data-t="ver">📖 Opzoeken</button>
    <button class="tab" data-t="practica">✍️ Zelf vervoegen</button>
    <button class="tab" data-t="lista">🗂️ Alle werkwoorden</button>
  </div>

  <section class="pane show" data-p="ver">
    <div class="card">
      <div class="controls">
        <input id="vsearch" placeholder="🔎 zoek werkwoord (infinitivo)…" oninput="renderChips()">
        <select id="vfilter" onchange="renderChips()">
          <option value="">alle types</option><option value="regelmatig">regelmatig</option>
          <option value="onregelmatig">onregelmatig</option><option value="klankwissel">klankwissel (o→ue, e→ie, e→i, u→ue)</option>
          <option value="wederkerend">wederkerend</option>
        </select>
        <span class="pill" id="vcount"></span>
      </div>
      <div class="controls" style="margin-top:0">
        <input id="vfree" placeholder="…of typ eender welk werkwoord (bv. saltar)" onkeydown="if(event.key==='Enter')freeConj()">
        <button class="btn small" onclick="freeConj()">Vervoeg</button>
        <span class="gloss" style="font-size:12px">→ ook werkwoorden buiten de lijst (dan regelmatig aangenomen, met waarschuwing).</span>
      </div>
      <div class="vchips" id="vchips"></div>
    </div>
    <div class="card" id="conjcard"></div>
  </section>

  <section class="pane" data-p="practica">
    <div class="card">
      <div class="controls">
        <label style="font-size:13px;color:var(--mut)">Oefen op:</label>
        <select id="pfilter" onchange="pNext()">
          <option value="all">alle werkwoorden</option><option value="regelmatig">enkel regelmatig</option>
          <option value="irr">enkel onregelmatig + klankwissel</option>
        </select>
        <span class="pill" id="pType"></span>
      </div>
      <div class="scorebar"><span>Punten: <b id="pPt">0</b></span><span>Reeks: <b id="pSt">0</b></span></div>
      <div class="gloss" id="pCtx"></div>
      <div class="qbox" id="pQ"></div>
      <div class="cue">
        <span class="pill" id="pCue"></span>
        <input class="txin" id="pIn" placeholder="vervoeg…" autocomplete="off" spellcheck="false">
        <button class="btn small" id="pGo">OK</button>
        <button class="btn sec small" id="pHint">💡 hint</button>
        <button class="btn sec small" id="pSkip">overslaan →</button>
      </div>
      <div class="fb" id="pFb"></div>
    </div>
    <p class="gloss" style="font-size:13px">Steun bouwt af: probeer eerst zonder hint. De hint toont eerst de beginletter, dan meer. Tik het antwoord met of zonder het voornaamwoord — beide tellen.</p>
  </section>

  <section class="pane" data-p="lista">
    <div class="card">
      <div class="controls"><input id="lsearch" placeholder="🔎 zoek…" oninput="renderTable()"><span class="pill" id="lcount"></span></div>
      <div style="max-height:64vh;overflow:auto"><table class="vt"><thead><tr><th>Infinitivo</th><th>NL</th><th>Type</th><th>yo</th><th>tú</th><th>él/ella</th><th>nosotros</th><th>vosotros</th><th>ellos</th></tr></thead><tbody id="lbody"></tbody></table></div>
    </div>
  </section>

  <div class="foot">Conjugador · presente (regelmatig + onregelmatig) · """+str(len(DB))+""" werkwoorden · Español en la práctica · cursus-tool.</div>
</main>
<script>
const DB=__DB__;const PRON=__PRON__;const PRONS=__PRONS__;
function toggleTheme(){const r=document.documentElement;r.dataset.theme=r.dataset.theme==='dark'?'light':'dark'}
function strip(w){return w.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'')}
// tabs
document.querySelectorAll('.tab').forEach(b=>b.onclick=()=>{document.querySelectorAll('.tab').forEach(x=>x.classList.remove('on'));b.classList.add('on');
  document.querySelectorAll('.pane').forEach(x=>x.classList.remove('show'));document.querySelector('.pane[data-p="'+b.dataset.t+'"]').classList.add('show');});
// ---- filter helper ----
function matchType(v,f){if(!f)return true;if(f==='klankwissel')return v.type.includes('klankwissel');if(f==='onregelmatig')return v.type.includes('onregelmatig');if(f==='regelmatig')return v.type==='regelmatig';if(f==='wederkerend')return v.type==='wederkerend';return true;}
// ---- OPZOEKEN ----
let curV=DB.find(v=>v.inf==='hablar');
const COMMON=['ser','estar','tener','ir','hacer','poder','querer','saber','ver','dar','decir','poner','venir','salir','hablar','comer','vivir','trabajar','estudiar','jugar','dormir','pedir','pensar','volver'];
function renderChips(){const q=(document.getElementById('vsearch').value||'').trim().toLowerCase();const f=document.getElementById('vfilter').value;
  const box=document.getElementById('vchips');box.innerHTML='';
  const hits=DB.filter(v=>(!q||v.inf.includes(q)||v.nl.toLowerCase().includes(q))&&matchType(v,f));
  let list;
  if(!q&&!f){ // standaard: toon niet alle 1000, enkel de veelgebruikte
    list=COMMON.map(inf=>DB.find(v=>v.inf===inf)).filter(Boolean);
    box.innerHTML='<div class="gloss" style="width:100%;margin-bottom:8px">🔎 Typ hierboven om te zoeken in alle '+DB.length+' werkwoorden — of kies een veelgebruikt werkwoord. De volledige lijst staat onder «🗂️ Alle werkwoorden».</div>';
  }else list=hits.slice(0,120);
  list.forEach(v=>{const c=document.createElement('div');c.className='vchip'+(curV&&v.inf===curV.inf?' on':'');c.innerHTML=v.inf+' <small>'+v.nl+'</small>';c.onclick=()=>{curV=v;renderChips();renderConj();};box.appendChild(c);});
  if((q||f)&&hits.length>120){const m=document.createElement('div');m.className='gloss';m.style.width='100%';m.textContent='… en '+(hits.length-120)+' meer — verfijn je zoekterm.';box.appendChild(m);}
  document.getElementById('vcount').textContent=(q||f)?(hits.length+' gevonden'):(DB.length+' werkwoorden');}
function renderConj(){const v=curV;const box=document.getElementById('conjcard');if(!v){box.innerHTML='';return;}
  const badge=v.type==='regelmatig'?'<span class="pill">regelmatig</span>':'<span class="pill" style="background:#FDECD2;color:#9a5a00">'+v.type+'</span>';
  let g='';v.forms.forEach((f,i)=>{g+='<div class="pv p'+i+'"><div class="pr">'+PRON[i]+'</div><div class="fm">'+f+'</div></div>';});
  const ex=(v.type==='wederkerend'?'':cap(PRONS[0])+' ')+v.forms[0]+(v.sit?' '+v.sit:'')+'.';
  const warn=v.warn?'<div style="background:#FEF3C7;color:#92400E;border-radius:10px;padding:10px 13px;margin-bottom:12px">⚠️ <b>«'+v.inf+'»</b> staat niet in de database. Hieronder de <b>regelmatige</b> vervoeging — controleer of dit werkwoord onregelmatig is (klankwissel of aparte yo-vorm).</div>':'';
  box.innerHTML=warn+'<div class="hdr"><h2>'+v.inf+'</h2>'+badge+'<span class="gloss">'+v.nl+'</span></div><div class="conj">'+g+'</div><div class="ex">📝 Ejemplo: <b>'+ex+'</b></div>';}
function cap(s){return s.charAt(0).toUpperCase()+s.slice(1);}
function regConj(inf){var st=inf.slice(0,-2),e=inf.slice(-2);var E={ar:['o','as','a','amos','áis','an'],er:['o','es','e','emos','éis','en'],ir:['o','es','e','imos','ís','en']}[e];return E.map(x=>st+x);}
function freeConj(){var raw=(document.getElementById('vfree').value||'').trim().toLowerCase();if(!raw)return;
  var hit=DB.find(v=>v.inf===raw);
  if(hit){curV=hit;renderChips();renderConj();return;}
  if(!/(ar|er|ir)$/.test(raw)){document.getElementById('conjcard').innerHTML='<p class="gloss">Geef een infinitivo op -ar, -er of -ir (bv. saltar, beber, subir).</p>';return;}
  curV={inf:raw,nl:'(getypt werkwoord)',type:'regelmatig (aangenomen)',sit:'',forms:regConj(raw),warn:1};renderConj();}
// ---- ZELF VERVOEGEN ----
let pPt=0,pSt=0,pHintN=0;
function pPool(){const f=document.getElementById('pfilter').value;return DB.filter(v=>v.type!=='wederkerend'&&v.inf!=='haber').filter(v=>f==='all'?true:f==='regelmatig'?v.type==='regelmatig':v.type!=='regelmatig');}
function pNext(){const pool=pPool();const v=pool[Math.floor(Math.random()*pool.length)];const i=Math.floor(Math.random()*6);
  window._pv=v;window._pi=i;pHintN=0;
  document.getElementById('pType').textContent=v.type;
  document.getElementById('pCtx').textContent=v.sit?('Contexto: '+v.sit):'';
  document.getElementById('pQ').innerHTML=cap(PRONS[i])+' <span class="gap" id="pGap">?</span>'+(v.sit?' '+v.sit:'')+'.';
  document.getElementById('pCue').textContent=PRON[i]+' · '+v.inf+' ('+v.nl+')';
  const inp=document.getElementById('pIn');inp.value='';inp.focus();document.getElementById('pFb').className='fb';}
function pCheck(){const v=window._pv,i=window._pi;let g=(document.getElementById('pIn').value||'').trim().toLowerCase();
  if(!g)return;const want=v.forms[i].toLowerCase();
  // sta toe: met of zonder voornaamwoord ervoor
  g=g.replace(new RegExp('^('+PRONS[i]+'|él|ella|usted|ellos|ellas|ustedes)\\\\s+'),'');
  const ok=g===want;const near=strip(g)===strip(want);
  const fb=document.getElementById('pFb');
  if(ok){pPt++;pSt++;setSc();document.getElementById('pGap').textContent=want;
    fb.className='fb good';fb.innerHTML='✅ ¡Correcto! <b>'+cap(PRONS[i])+' '+want+'</b> — '+v.inf+' ('+v.type+').';setTimeout(pNext,1200);}
  else{pSt=0;setSc();fb.className='fb bad';
    fb.innerHTML=(near?'❌ Bijna — let op het accent: ':'❌ ')+'de juiste vorm is <b>'+want+'</b> ('+PRON[i]+' · '+v.inf+', '+v.type+').';}
}
function setSc(){document.getElementById('pPt').textContent=pPt;document.getElementById('pSt').textContent=pSt;}
function pHint(){const v=window._pv,i=window._pi;pHintN++;const want=v.forms[i];const show=Math.min(pHintN,want.length);
  document.getElementById('pIn').value=want.slice(0,show);document.getElementById('pIn').focus();
  const fb=document.getElementById('pFb');fb.className='fb good';fb.innerHTML='💡 hint: <b>'+want.slice(0,show)+'…</b> ('+(want.length)+' letters)';}
document.getElementById('pGo').onclick=pCheck;
document.getElementById('pIn').onkeydown=e=>{if(e.key==='Enter')pCheck();};
document.getElementById('pHint').onclick=pHint;
document.getElementById('pSkip').onclick=pNext;
// ---- LIJST ----
function renderTable(){const q=(document.getElementById('lsearch').value||'').toLowerCase();const b=document.getElementById('lbody');b.innerHTML='';let n=0;
  DB.forEach(v=>{if(q&&!(v.inf.includes(q)||v.nl.toLowerCase().includes(q)))return;n++;
    b.innerHTML+='<tr><td class="m">'+v.inf+'</td><td>'+v.nl+'</td><td>'+v.type+'</td>'+v.forms.map(f=>'<td>'+f+'</td>').join('')+'</tr>';});
  document.getElementById('lcount').textContent=n+' werkwoorden';}
// init
renderChips();renderConj();pNext();renderTable();
</script></body></html>"""

html=(HTML.replace("__CSS__",CSS).replace("__DB__",json.dumps(DB,ensure_ascii=False))
      .replace("__PRON__",json.dumps(PRON,ensure_ascii=False)).replace("__PRONS__",json.dumps(PRONs,ensure_ascii=False)))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/Conjugador.html","w").write(html)
print("Conjugador.html geschreven:",len(html),"bytes ·",len(DB),"werkwoorden")
