import { readFileSync, writeFileSync } from "node:fs";
const S = process.env.SCRATCH;
const esBuilt = JSON.parse(readFileSync(S+"/es_inventory.json","utf8"));
const nl = JSON.parse(readFileSync(S+"/nl_catalog.json","utf8"));
const en = JSON.parse(readFileSync(S+"/en_catalog.json","utf8"));

/* Arcade-retrofit C5/C6+ (PLAN_MOTOR §6bis): de 7 nieuwe skins zijn gebouwd maar nog
   niet ingezet in het Spaans — één arcade-slot per unit krijgt een andere jas.
   Zelfde content-JSON, enkel het template wisselt. Status = te bouwen. */
const SKIN = { belt:"Cinta · sorteerband", mole:"Topos · mollenmeppen", bubble:"Burbujas · bubbelschieter",
  snake:"Serpiente · snake", platform:"Puertas · platformer", tower:"Torres · torenverdediging",
  pinball:"Pinball · flipper", tetris:"Tetris" };
const ROT = [
  ["C5","U1","tetris","Presente regular","blijft tetris — vervoeging in kolommen past hier"],
  ["C5","U2","belt","ser, estar y tener","was tetris"],
  ["C5","U3","mole","Presente irregular","was tetris"],
  ["C5","U4","bubble","Presente regular (actividades)","was tetris"],
  ["C5","U5","snake","Cantidades · mucho","was tetris"],
  ["C5","U6","platform","Concordancia · prenda + kleur","was tetris"],
  ["C5","U7","tower","Preposiciones","was tetris"],
  ["C5","U8","pinball","Haber","was tetris"],
  ["C6+","U0","tetris","Concordancia","blijft tetris"],
  ["C6+","U1","bubble","Pronombre me/te/se","was tetris"],
  ["C6+","U2","mole","lo/la","was tetris"],
  ["C6+","U3","platform","ir a + infinitivo","was tetris"],
  ["C6+","U4","snake","Participio","was tetris"],
  ["C6+","U5","belt","Indefinido","was tetris"],
  ["C6+","U6","tower","Imperfecto","was tetris"],
  ["C6+","U7","pinball","Imperativo","was tetris"],
];
const esPlan = ROT.map(([course,unit,tpl,topic,note])=>({
  course, unit, tpl, plan:1,
  title:"Arcade-slot → "+SKIN[tpl],
  sub:topic+" · "+note
}));
const es = esBuilt.concat(esPlan);

const DATA = { es, nl, en };
const json = JSON.stringify(DATA);

const CSS = `
:root{
  --paper:#F5EFE0; --panel:#EDE4CE; --panel-2:#E4D9BE;
  --ink:#12264A; --ink-2:#3A3527; --dim:#7C7060; --line:rgba(18,38,74,.16);
  --p-red:#C4402C; --p-gold:#C98A16; --p-green:#2E8E68; --p-blue:#3D74D6; --p-purple:#8B5E9E;
  --serif:"Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  --shadow:0 4px 0 rgba(18,38,74,.13); --stripe:rgba(18,38,74,.05);
}
@media (prefers-color-scheme:dark){:root{
  --paper:#0F2140; --panel:#16305A; --panel-2:#1B3766;
  --ink:#F3ECDB; --ink-2:#D8CDB4; --dim:#9FB0CC; --line:rgba(243,236,219,.16);
  --p-gold:#E0A22F; --shadow:0 4px 0 rgba(0,0,0,.35); --stripe:rgba(243,236,219,.06);
}}
:root[data-theme="dark"]{
  --paper:#0F2140; --panel:#16305A; --panel-2:#1B3766;
  --ink:#F3ECDB; --ink-2:#D8CDB4; --dim:#9FB0CC; --line:rgba(243,236,219,.16);
  --p-gold:#E0A22F; --shadow:0 4px 0 rgba(0,0,0,.35); --stripe:rgba(243,236,219,.06);
}
:root[data-theme="light"]{
  --paper:#F5EFE0; --panel:#EDE4CE; --panel-2:#E4D9BE;
  --ink:#12264A; --ink-2:#3A3527; --dim:#7C7060; --line:rgba(18,38,74,.16);
  --p-gold:#C98A16; --shadow:0 4px 0 rgba(18,38,74,.13); --stripe:rgba(18,38,74,.05);
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);line-height:1.5;
  -webkit-font-smoothing:antialiased}
.wrap{max-width:1080px;margin:0 auto;padding:30px 20px 80px}
a{color:inherit}

/* header */
.masthead{position:relative;border:1px solid var(--line);border-radius:5px;background:var(--panel);
  box-shadow:var(--shadow);padding:26px 24px 24px;overflow:hidden}
.masthead::before{content:"";position:absolute;top:0;left:0;right:0;height:8px;
  background:repeating-linear-gradient(45deg,var(--ink) 0 5px,transparent 5px 10px),
             repeating-linear-gradient(-45deg,var(--ink) 0 5px,transparent 5px 10px);opacity:.42}
.eyebrow{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--dim);margin:8px 0 6px}
h1{font-family:var(--serif);font-weight:700;font-size:clamp(28px,5vw,44px);line-height:1.05;margin:0;
  text-wrap:balance;letter-spacing:.01em}
.lede{font-family:var(--serif);font-style:italic;font-size:clamp(15px,2.2vw,19px);color:var(--ink-2);
  margin:10px 0 0;max-width:60ch}

/* taalkaarten */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin:20px 0 0}
.lcard{position:relative;border:1px solid var(--line);border-radius:4px;background:var(--panel);
  box-shadow:var(--shadow);padding:16px 16px 14px;border-left:5px solid var(--lc)}
.lcard .lt{font-family:var(--serif);font-weight:700;font-size:19px}
.lcard .lstate{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--dim)}
.lcard .lnum{font-family:var(--serif);font-weight:700;font-size:38px;line-height:1;margin:6px 0 2px;
  font-variant-numeric:tabular-nums}
.lcard .lnum small{font-size:14px;font-weight:400;color:var(--dim)}
.distro{display:flex;height:9px;border-radius:99px;overflow:hidden;margin-top:10px;border:1px solid var(--line)}
.distro i{display:block;height:100%}
.dkey{display:flex;flex-wrap:wrap;gap:4px 12px;margin-top:8px;font-size:11px;color:var(--dim)}
.dkey span{display:inline-flex;align-items:center;gap:5px}
.dkey b{width:9px;height:9px;border-radius:2px;display:inline-block}

/* controls */
.controls{position:sticky;top:0;z-index:5;margin:22px 0 0;padding:12px 0;background:var(--paper);
  border-bottom:1px solid var(--line);display:flex;flex-wrap:wrap;gap:10px 14px;align-items:center}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:4px;overflow:hidden;background:var(--panel)}
.seg button{font-family:var(--sans);font-size:13px;font-weight:600;padding:8px 14px;border:0;background:transparent;
  color:var(--dim);cursor:pointer;border-right:1px solid var(--line)}
.seg button:last-child{border-right:0}
.seg button.on{background:var(--seg,#12264A);color:#F5EFE0}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chip{font-size:12px;font-weight:600;padding:6px 11px;border-radius:99px;border:1px solid var(--line);
  background:var(--panel);color:var(--ink-2);cursor:pointer;display:inline-flex;align-items:center;gap:6px}
.chip i{width:9px;height:9px;border-radius:2px;display:inline-block}
.chip.on{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.chip.on i{outline:1px solid var(--paper)}
.search{flex:1;min-width:180px;display:flex;align-items:center;gap:8px;border:1px solid var(--line);
  border-radius:4px;background:var(--panel);padding:8px 12px}
.search input{flex:1;border:0;background:transparent;color:var(--ink);font-size:14px;font-family:var(--sans);outline:none}
.search input::placeholder{color:var(--dim)}
.count{font-size:12px;color:var(--dim);font-variant-numeric:tabular-nums;white-space:nowrap}

/* groepen */
.group{margin:22px 0 0}
.ghead{display:flex;align-items:baseline;gap:10px;position:relative;padding:6px 0 8px;border-bottom:2px solid var(--line)}
.ghead .gu{font-family:var(--serif);font-weight:700;font-size:20px}
.ghead .gt{font-family:var(--serif);font-style:italic;color:var(--ink-2);font-size:16px}
.ghead .gn{margin-left:auto;font-size:12px;color:var(--dim);font-variant-numeric:tabular-nums}
.rows{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:8px;margin-top:12px}
.row{display:flex;gap:11px;align-items:flex-start;padding:11px 12px;border:1px solid var(--line);border-radius:3px;
  background:var(--panel);box-shadow:0 2px 0 rgba(18,38,74,.07)}
.badge{flex:0 0 auto;font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
  padding:4px 8px;border-radius:3px;color:#fff;white-space:nowrap;margin-top:1px;
  border:1px solid rgba(0,0,0,.22)}
.rtxt{min-width:0}
.rtitle{font-family:var(--serif);font-weight:600;font-size:15px;line-height:1.2}
.rsub{font-size:12.5px;color:var(--dim);margin-top:2px}
.row.plan{background:repeating-linear-gradient(135deg,transparent 0 9px,var(--stripe) 9px 18px),var(--panel);
  border-style:dashed}
.todo{display:inline-block;font-size:9.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
  color:var(--p-purple);border:1px solid var(--p-purple);border-radius:99px;padding:1px 6px;margin-left:7px;vertical-align:1px}
.split{font-size:11.5px;color:var(--dim);margin-top:7px}
.split b{color:var(--ink-2);font-variant-numeric:tabular-nums}
.empty{padding:40px 0;text-align:center;color:var(--dim);font-family:var(--serif);font-style:italic}

footer{margin-top:40px;padding-top:18px;border-top:1px solid var(--line);font-size:13px;color:var(--dim);max-width:70ch}
footer b{color:var(--ink-2)}
@media (max-width:560px){.rows{grid-template-columns:1fr}.ghead .gt{display:none}}
@media (prefers-reduced-motion:no-preference){.row,.chip,.seg button{transition:background .12s,color .12s}}
:focus-visible{outline:3px solid var(--p-blue);outline-offset:2px;border-radius:2px}
`;

const JS = `
const DATA = __DATA__;
const DOMAIN = {
  match:"vocab",memory:"vocab",point:"vocab",
  classify:"gram",cloze:"gram",order:"gram",tap:"gram",
  type:"prod",speak:"prod",sim:"prod",
  tetris:"arcade",belt:"arcade",mole:"arcade",bubble:"arcade",snake:"arcade",platform:"arcade",tower:"arcade",pinball:"arcade"
};
const DCOL = {vocab:"var(--p-gold)",gram:"var(--p-blue)",prod:"var(--p-green)",arcade:"var(--p-red)"};
const DLABEL = {vocab:"Woordenschat",gram:"Grammatica",prod:"Productie",arcade:"Arcade"};
const LANGS = {
  es:{label:"Español",state:"gebouwd",accent:"var(--p-red)"},
  nl:{label:"NT2",state:"voorstel",accent:"var(--p-blue)"},
  en:{label:"English",state:"voorstel",accent:"var(--p-green)"}
};
let lang="es", domain="all", q="";

function esc(s){return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));}
function domCount(rows){const d={vocab:0,gram:0,prod:0,arcade:0};rows.forEach(r=>{const k=DOMAIN[r.tpl]||"gram";d[k]++;});return d;}

function renderCards(){
  const el=document.getElementById("cards");
  el.innerHTML=Object.keys(LANGS).map(k=>{
    const rows=DATA[k], d=domCount(rows), tot=rows.length;
    const seg=["vocab","gram","prod","arcade"].map(dm=>
      '<i style="width:'+(d[dm]/tot*100)+'%;background:'+DCOL[dm]+'"></i>').join("");
    const planN=rows.filter(r=>r.plan).length, builtN=tot-planN;
    return '<button class="lcard" data-lang="'+k+'" style="--lc:'+LANGS[k].accent+'" aria-label="Toon '+LANGS[k].label+'">'+
      '<div class="lstate">'+LANGS[k].state+'</div>'+
      '<div class="lt">'+LANGS[k].label+'</div>'+
      '<div class="lnum">'+tot+' <small>spellen</small></div>'+
      (planN?'<div class="split"><b>'+builtN+'</b> gebouwd · <b>'+planN+'</b> te bouwen (arcade-rotatie)</div>':'')+
      '<div class="distro">'+seg+'</div>'+
      '<div class="dkey">'+["vocab","gram","prod","arcade"].map(dm=>
        '<span><b style="background:'+DCOL[dm]+'"></b>'+DLABEL[dm]+' '+d[dm]+'</span>').join("")+'</div>'+
    '</button>';
  }).join("");
  el.querySelectorAll(".lcard").forEach(b=>b.addEventListener("click",()=>{lang=b.dataset.lang;sync();}));
}

function renderChips(){
  const el=document.getElementById("chips");
  const opts=[["all","Alles"],["vocab",DLABEL.vocab],["gram",DLABEL.gram],["prod",DLABEL.prod],["arcade",DLABEL.arcade]];
  el.innerHTML=opts.map(([k,lbl])=>{
    const dot=k==="all"?"":'<i style="background:'+DCOL[k]+'"></i>';
    return '<button class="chip'+(domain===k?" on":"")+'" data-dom="'+k+'">'+dot+esc(lbl)+'</button>';
  }).join("");
  el.querySelectorAll(".chip").forEach(b=>b.addEventListener("click",()=>{domain=b.dataset.dom;sync();}));
}

function renderList(){
  const rows=DATA[lang].filter(r=>{
    if(domain!=="all" && (DOMAIN[r.tpl]||"gram")!==domain) return false;
    if(q){ const hay=(r.title+" "+(r.theme||"")+" "+(r.sub||"")+" "+r.tpl).toLowerCase(); if(hay.indexOf(q)<0) return false; }
    return true;
  });
  document.getElementById("count").textContent=rows.length+" spellen";
  const host=document.getElementById("list");
  if(!rows.length){ host.innerHTML='<div class="empty">Geen spellen voor deze filter.</div>'; return; }
  // groepeer op unit/niveau
  const groups={};
  rows.forEach(r=>{ const g=r.unit||"—"; (groups[g]=groups[g]||[]).push(r); });
  const order=Object.keys(groups).sort();
  host.innerHTML=order.map(g=>{
    const items=groups[g];
    const theme = lang==="es" ? "" : "";
    const rowsHtml=items.map(r=>{
      const dm=DOMAIN[r.tpl]||"gram";
      return '<div class="row'+(r.plan?" plan":"")+'">'+
        '<span class="badge" style="background:'+DCOL[dm]+'">'+esc(r.tpl)+'</span>'+
        '<div class="rtxt"><div class="rtitle">'+esc(r.title)+
          (r.plan?'<span class="todo">te bouwen</span>':'')+'</div>'+
          (r.theme?'<div class="rsub">'+esc(r.theme)+(r.sub?' · '+esc(r.sub):'')+'</div>':
            (r.sub?'<div class="rsub">'+esc(r.sub)+'</div>':''))+
        '</div></div>';
    }).join("");
    const label = lang==="es" ? (DATA.es.find(x=>x.unit===g)?.course||"")+" "+g : g;
    return '<section class="group"><div class="ghead"><span class="gu">'+esc(label.trim())+'</span>'+
      '<span class="gn">'+items.length+'</span></div><div class="rows">'+rowsHtml+'</div></section>';
  }).join("");
}

function sync(){
  document.querySelectorAll(".seg button").forEach(b=>b.classList.toggle("on",b.dataset.lang===lang));
  document.querySelector(".seg").style.setProperty("--seg",LANGS[lang].accent);
  renderChips();
  renderList();
}

function init(){
  renderCards();
  const seg=document.getElementById("seg");
  seg.innerHTML=Object.keys(LANGS).map(k=>'<button data-lang="'+k+'"'+(k===lang?' class="on"':'')+'>'+LANGS[k].label+'</button>').join("");
  seg.querySelectorAll("button").forEach(b=>b.addEventListener("click",()=>{lang=b.dataset.lang;sync();}));
  document.getElementById("q").addEventListener("input",e=>{q=e.target.value.trim().toLowerCase();renderList();});
  sync();
}
init();
`.replace("__DATA__", json);

const HTML = `<style>${CSS}</style>
<div class="wrap">
  <header class="masthead">
    <div class="eyebrow">spaans-motor · oefenspellen</div>
    <h1>Catálogo de juegos</h1>
    <p class="lede">Eén motor, dertien speltypes, drie talen. De Spaanse lijst is wat er nu écht gebouwd is; NT2 en Engels zijn voorstel-catalogi — met exact dezelfde templates direct bouwbaar.</p>
    <div class="cards" id="cards"></div>
  </header>

  <div class="controls">
    <div class="seg" id="seg" role="tablist" aria-label="Taal"></div>
    <div class="chips" id="chips" aria-label="Filter op domein"></div>
    <label class="search"><span aria-hidden="true">🔎</span>
      <input id="q" type="search" placeholder="Zoek op woord, thema of speltype…" aria-label="Zoeken">
    </label>
    <span class="count" id="count"></span>
  </div>

  <div id="list"></div>

  <footer>
    <p><b>Español</b> = <b>299 gebouwde</b> spellen (bron: <code>content/*.json</code>), gegroepeerd per cursus/unit — C5 (U0–U8) en C6+ (U0–U7) — plus <b>16 geplande arcade-slots</b> (gestreept, «te bouwen»). Die laatste zijn de <b>arcade-rotatie</b>: C5 en C6+ zijn gebouwd vóór de 7 nieuwe skins bestonden, dus daar is <code>tetris</code> nu nog de enige arcade-vorm. Omdat de 8 skins onderling verwisselbare jassen zijn op dezelfde judge, krijgt elk arcade-slot enkel een andere skin — zelfde items, geen nieuwe didactische content. Zie <code>PLAN_MOTOR §6bis</code>.</p>
    <p><b>NT2 (241)</b> en <b>English (271)</b> zijn voorstel-catalogi per niveau (A1→B1/B2) en thema: elk thema krijgt een spelset verdeeld over de templates + de volledige arcade-rotatie. Kleuren = domein: <b>woordenschat</b> (goud), <b>grammatica</b> (blauw), <b>productie</b> — typen/spreken (groen), <b>arcade</b> (terracotta).</p>
  </footer>
</div>
<script>${JS}</script>`;

writeFileSync(S+"/catalogo.html", HTML);
console.log("catalogo.html geschreven —", (HTML.length/1024|0)+" KB");
