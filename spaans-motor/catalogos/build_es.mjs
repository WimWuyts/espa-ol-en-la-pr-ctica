import { readFileSync, writeFileSync } from "node:fs";
const S = process.env.SCRATCH;
const built = JSON.parse(readFileSync(S+"/es_inventory.json","utf8"));

/* Arcade-rotatie C5/C6+ (PLAN_MOTOR §6bis) — te bouwen: enkel de skin wisselt. */
const SKIN = { belt:"Cinta · sorteerband", mole:"Topos · mollenmeppen", bubble:"Burbujas · bubbelschieter",
  snake:"Serpiente · snake", platform:"Puertas · platformer", tower:"Torres · torenverdediging",
  pinball:"Pinball · flipper", tetris:"Tetris" };
const ROT = [
  ["C5","U1","tetris","es-u1-presente-regular","Presente regular","blijft tetris — vervoeging in kolommen past hier"],
  ["C5","U2","belt","es-u2-familia-tetris","ser, estar y tener","was tetris"],
  ["C5","U3","mole","es-u3-irregular-tetris","Presente irregular","was tetris"],
  ["C5","U4","bubble","es-u4-presente-tetris","Presente (actividades)","was tetris"],
  ["C5","U5","snake","es-u5-cantidad-tetris","Cantidades · mucho","was tetris"],
  ["C5","U6","platform","es-u6-concordancia-tetris","Concordancia · prenda + color","was tetris"],
  ["C5","U7","tower","es-u7-preposicion-tetris","Preposiciones","was tetris"],
  ["C5","U8","pinball","es-u8-haber-tetris","Haber","was tetris"],
  ["C6+","U0","tetris","es-c6plus-u0-concordancia-tetris","Concordancia","blijft tetris"],
  ["C6+","U1","bubble","es-c6plus-u1-pronombre-tetris","Pronombre me/te/se","was tetris"],
  ["C6+","U2","mole","es-c6plus-u2-lo-la-tetris","lo / la","was tetris"],
  ["C6+","U3","platform","es-c6plus-u3-ir-a-tetris","ir a + infinitivo","was tetris"],
  ["C6+","U4","snake","es-c6plus-u4-participio-tetris","Participio","was tetris"],
  ["C6+","U5","belt","es-c6plus-u5-indef-tetris","Indefinido","was tetris"],
  ["C6+","U6","tower","es-c6plus-u6-imperf-tetris","Imperfecto","was tetris"],
  ["C6+","U7","pinball","es-c6plus-u7-imper-tetris","Imperativo","was tetris"],
];
const plan = ROT.map(([course,unit,tpl,id,topic,note])=>({
  course, unit, tpl, id, plan:1,
  title:"Arcade-slot → "+SKIN[tpl], sub:topic+" · "+note
}));
const ROWS = built; // arcade-rotatie is uitgevoerd (2026-07-29): geen planlaag meer
const json = JSON.stringify(ROWS);

const CSS = `
:root{
  --paper:#F5EFE0; --panel:#EDE4CE;
  --ink:#12264A; --ink-2:#3A3527; --dim:#7C7060; --line:rgba(18,38,74,.16);
  --p-red:#C4402C; --p-gold:#C98A16; --p-green:#2E8E68; --p-blue:#3D74D6; --p-purple:#8B5E9E;
  --serif:"Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  --shadow:0 4px 0 rgba(18,38,74,.13); --stripe:rgba(18,38,74,.05);
}
@media (prefers-color-scheme:dark){:root{
  --paper:#0F2140; --panel:#16305A;
  --ink:#F3ECDB; --ink-2:#D8CDB4; --dim:#9FB0CC; --line:rgba(243,236,219,.16);
  --p-gold:#E0A22F; --p-purple:#C79BD8; --shadow:0 4px 0 rgba(0,0,0,.35); --stripe:rgba(243,236,219,.06);
}}
:root[data-theme="dark"]{
  --paper:#0F2140; --panel:#16305A;
  --ink:#F3ECDB; --ink-2:#D8CDB4; --dim:#9FB0CC; --line:rgba(243,236,219,.16);
  --p-gold:#E0A22F; --p-purple:#C79BD8; --shadow:0 4px 0 rgba(0,0,0,.35); --stripe:rgba(243,236,219,.06);
}
:root[data-theme="light"]{
  --paper:#F5EFE0; --panel:#EDE4CE;
  --ink:#12264A; --ink-2:#3A3527; --dim:#7C7060; --line:rgba(18,38,74,.16);
  --p-gold:#C98A16; --p-purple:#8B5E9E; --shadow:0 4px 0 rgba(18,38,74,.13); --stripe:rgba(18,38,74,.05);
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);line-height:1.5;-webkit-font-smoothing:antialiased}
.wrap{max-width:1020px;margin:0 auto;padding:30px 20px 80px}

.masthead{position:relative;border:1px solid var(--line);border-radius:5px;background:var(--panel);
  box-shadow:var(--shadow);padding:26px 24px 22px;overflow:hidden}
.masthead::before{content:"";position:absolute;top:0;left:0;right:0;height:8px;
  background:repeating-linear-gradient(45deg,var(--ink) 0 5px,transparent 5px 10px),
             repeating-linear-gradient(-45deg,var(--ink) 0 5px,transparent 5px 10px);opacity:.42}
.eyebrow{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--dim);margin:8px 0 6px}
h1{font-family:var(--serif);font-weight:700;font-size:clamp(28px,5vw,42px);line-height:1.05;margin:0;text-wrap:balance}
.lede{font-family:var(--serif);font-style:italic;font-size:clamp(15px,2.2vw,18px);color:var(--ink-2);margin:10px 0 0;max-width:62ch}
.tally{display:flex;flex-wrap:wrap;gap:8px 26px;margin:18px 0 0;padding-top:16px;border-top:1px solid var(--line)}
.tal{display:flex;flex-direction:column}
.tal b{font-family:var(--serif);font-size:30px;line-height:1;font-variant-numeric:tabular-nums}
.tal span{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);margin-top:4px}
.tal.todo b{color:var(--p-purple)}

.controls{position:sticky;top:0;z-index:5;margin:20px 0 0;padding:12px 0;background:var(--paper);
  border-bottom:1px solid var(--line);display:flex;flex-wrap:wrap;gap:9px 14px;align-items:center}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chip{font-size:12px;font-weight:600;padding:6px 11px;border-radius:99px;border:1px solid var(--line);
  background:var(--panel);color:var(--ink-2);cursor:pointer;display:inline-flex;align-items:center;gap:6px}
.chip i{width:9px;height:9px;border-radius:2px;display:inline-block}
.chip.on{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.chip.on i{outline:1px solid var(--paper)}
.search{flex:1;min-width:170px;display:flex;align-items:center;gap:8px;border:1px solid var(--line);
  border-radius:4px;background:var(--panel);padding:8px 12px}
.search input{flex:1;border:0;background:transparent;color:var(--ink);font-size:14px;font-family:var(--sans);outline:none}
.search input::placeholder{color:var(--dim)}
.count{font-size:12px;color:var(--dim);font-variant-numeric:tabular-nums;white-space:nowrap}

.group{margin:22px 0 0}
.ghead{display:flex;align-items:baseline;gap:10px;padding:6px 0 8px;border-bottom:2px solid var(--line)}
.ghead .gu{font-family:var(--serif);font-weight:700;font-size:20px}
.ghead .gn{margin-left:auto;font-size:12px;color:var(--dim);font-variant-numeric:tabular-nums}
.rows{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:8px;margin-top:12px}
.row{display:flex;gap:11px;align-items:flex-start;padding:11px 12px;border:1px solid var(--line);border-radius:3px;
  background:var(--panel);box-shadow:0 2px 0 rgba(18,38,74,.07)}
.row.plan{background:repeating-linear-gradient(135deg,transparent 0 9px,var(--stripe) 9px 18px),var(--panel);border-style:dashed}
.badge{flex:0 0 auto;font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:4px 8px;
  border-radius:3px;color:#fff;white-space:nowrap;margin-top:1px;border:1px solid rgba(0,0,0,.22)}
.rtxt{min-width:0}
.rtitle{font-family:var(--serif);font-weight:600;font-size:15px;line-height:1.2}
.rsub{font-size:12.5px;color:var(--dim);margin-top:2px}
.rid{font-family:var(--mono);font-size:10.5px;color:var(--dim);margin-top:3px;word-break:break-all}
.todo{display:inline-block;font-size:9.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
  color:var(--p-purple);border:1px solid var(--p-purple);border-radius:99px;padding:1px 6px;margin-left:7px;vertical-align:1px}
.empty{padding:40px 0;text-align:center;color:var(--dim);font-family:var(--serif);font-style:italic}
footer{margin-top:38px;padding-top:18px;border-top:1px solid var(--line);font-size:13px;color:var(--dim);max-width:74ch}
footer b{color:var(--ink-2)}
@media (max-width:560px){.rows{grid-template-columns:1fr}}
:focus-visible{outline:3px solid var(--p-blue);outline-offset:2px;border-radius:2px}
`;

const JS = `
const ROWS = __DATA__;
const DOMAIN = {match:"vocab",memory:"vocab",point:"vocab",classify:"gram",cloze:"gram",order:"gram",tap:"gram",
  type:"prod",speak:"prod",sim:"prod",tetris:"arcade",belt:"arcade",mole:"arcade",bubble:"arcade",snake:"arcade",
  platform:"arcade",tower:"arcade",pinball:"arcade"};
const DCOL={vocab:"var(--p-gold)",gram:"var(--p-blue)",prod:"var(--p-green)",arcade:"var(--p-red)"};
const DLABEL={vocab:"Woordenschat",gram:"Grammatica",prod:"Productie",arcade:"Arcade"};
let course="all", domain="all", status="all", q="";
function esc(s){return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));}

function chipRow(host,opts,cur,cb){
  host.innerHTML=opts.map(([k,lbl,col])=>
    '<button class="chip'+(cur===k?" on":"")+'" data-k="'+k+'">'+(col?'<i style="background:'+col+'"></i>':'')+esc(lbl)+'</button>').join("");
  host.querySelectorAll(".chip").forEach(b=>b.addEventListener("click",()=>cb(b.dataset.k)));
}
function renderControls(){
  chipRow(document.getElementById("cCourse"),
    [["all","Alle cursussen"],["C5","C5"],["C6+","C6+"],["tool","Tools"]],course,k=>{course=k;draw();});
  chipRow(document.getElementById("cDom"),
    [["all","Alle domeinen"],["vocab",DLABEL.vocab,DCOL.vocab],["gram",DLABEL.gram,DCOL.gram],
     ["prod",DLABEL.prod,DCOL.prod],["arcade",DLABEL.arcade,DCOL.arcade]],domain,k=>{domain=k;draw();});

}
function filtered(){
  return ROWS.filter(r=>{
    if(course!=="all" && (r.course||"tool")!==course) return false;
    if(domain!=="all" && (DOMAIN[r.tpl]||"gram")!==domain) return false;
    if(q){ const h=(r.title+" "+(r.sub||"")+" "+(r.id||"")+" "+r.tpl).toLowerCase(); if(h.indexOf(q)<0) return false; }
    return true;
  });
}
function draw(){
  renderControls();
  const rows=filtered();
  const nPlan=rows.filter(r=>r.plan).length;
  document.getElementById("count").textContent=rows.length+" spellen"+(nPlan?" · "+nPlan+" te bouwen":"");
  const host=document.getElementById("list");
  if(!rows.length){ host.innerHTML='<div class="empty">Geen spellen voor deze filter.</div>'; return; }
  const g={}; rows.forEach(r=>{const k=(r.course||"tool")+" "+(r.unit||"");(g[k]=g[k]||[]).push(r);});
  host.innerHTML=Object.keys(g).sort().map(k=>{
    const items=g[k].slice().sort((a,b)=>(a.plan?1:0)-(b.plan?1:0));
    const inner=items.map(r=>{
      const dm=DOMAIN[r.tpl]||"gram";
      return '<div class="row'+(r.plan?" plan":"")+'">'+
        '<span class="badge" style="background:'+DCOL[dm]+'">'+esc(r.tpl)+'</span>'+
        '<div class="rtxt"><div class="rtitle">'+esc(r.title)+(r.plan?'<span class="todo">te bouwen</span>':'')+'</div>'+
        (r.sub?'<div class="rsub">'+esc(r.sub)+'</div>':'')+
        (r.id?'<div class="rid">'+esc(r.id)+'</div>':'')+
        '</div></div>';
    }).join("");
    return '<section class="group"><div class="ghead"><span class="gu">'+esc(k.trim())+'</span>'+
      '<span class="gn">'+items.length+'</span></div><div class="rows">'+inner+'</div></section>';
  }).join("");
}
document.getElementById("q").addEventListener("input",e=>{q=e.target.value.trim().toLowerCase();draw();});
draw();
`.replace("__DATA__", json);

const nBuilt = built.length, nPlan = plan.length;
const HTML = `<style>${CSS}</style>
<div class="wrap">
  <header class="masthead">
    <div class="eyebrow">spaans-motor · español</div>
    <h1>Lista de juegos — C5 &amp; C6+</h1>
    <p class="lede">Alles wat er nu in de motor zit voor het Spaans — elk spel staat ook in de digitale hub van zijn unidad. Filter op cursus, domein of speltype.</p>
    <div class="tally">
      <div class="tal"><b>${nBuilt}</b><span>spellen · alle gebouwd</span></div>
      <div class="tal"><b>192</b><span>C5 · U0–U8</span></div>
      <div class="tal"><b>99</b><span>C6+ · U0–U7</span></div>
      <div class="tal"><b>13</b><span>speltypes</span></div>
      <div class="tal"><b>8/8</b><span>arcade-skins in gebruik</span></div>
    </div>
  </header>

  <div class="controls">
    <div class="chips" id="cCourse" aria-label="Filter op cursus"></div>
    <div class="chips" id="cDom" aria-label="Filter op domein"></div>
    <label class="search"><span aria-hidden="true">🔎</span>
      <input id="q" type="search" placeholder="Zoek op titel, thema of ID…" aria-label="Zoeken"></label>
    <span class="count" id="count"></span>
  </div>

  <div id="list"></div>

  <footer>
    <p>Kleuren = domein: <b>woordenschat</b> (goud) · <b>grammatica</b> (blauw) · <b>productie</b> — typen/spreken (groen) · <b>arcade</b> (terracotta). <b>Alle 291 unit-spellen zijn ingebed in de hub van hun unidad</b> (geverifieerd 291/291). De <b>arcade-rotatie is uitgevoerd</b>: elk van de 8 skins staat 1× per cursus (C5: tetris·mole·bubble·snake·belt·platform·tower·pinball · C6+: tetris·belt·platform·bubble·tower·pinball·mole·snake). Skins zijn per slot toegewezen op het aantal categorieën — bubbels/mollen/snake bij 6 categorieën, torens/deuren/pinball bij 3–5. De game-ID's bleven ongewijzigd (hub-links lopen op ID).</p>
  </footer>
</div>
<script>${JS}</script>`;

writeFileSync(S+"/catalogo_es.html", HTML);
console.log("catalogo_es.html —", (HTML.length/1024|0)+" KB ·", nBuilt, "spellen (alle gebouwd)");
