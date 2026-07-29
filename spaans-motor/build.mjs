/* ============================================================
   BUILD — leest elk contentpakket in /content en lijmt de motor
   samen tot één zelfstandige, offline .html in /games.
   Geen dependencies: enkel Node. Draait dus ook in Claude Code web
   zonder netwerktoegang.
   Gebruik:  node build.mjs
   ============================================================ */
import { readFileSync, writeFileSync, readdirSync, mkdirSync, existsSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = dirname(fileURLToPath(import.meta.url));
const SRC = join(ROOT,"src");
const CONTENT = join(ROOT,"content");
const OUT = join(ROOT,"games");
if(!existsSync(OUT)) mkdirSync(OUT,{recursive:true});

const read = p => readFileSync(p,"utf8");

/* welke bronbestanden een pakket nodig heeft, in laadvolgorde */
function jsFor(pack){
  const files = [];
  const needsGen = !!pack.generator;
  if(needsGen){
    if(pack.generator.kind==="verbo") files.push(join(SRC,"data.verbos."+(pack.lang||"es")+".js"));
    else files.push(join(SRC,"data."+(pack.lang||"es")+".js"));
    files.push(join(SRC,"generators.js"));
  }
  files.push(join(SRC,"templates",pack.template+".js"));
  files.push(join(SRC,"engine.js"));
  return files;
}
function cssFor(pack){
  return [ join(SRC,"tokens.css"), join(SRC,"shell.css"), join(SRC,"templates",pack.template+".css") ];
}

/* bouwt de bootstrap: zet generator om in een _source, of gebruikt vaste items */
function bootstrap(pack){
  const cfg = JSON.parse(JSON.stringify(pack));
  let pre = "";
  if(pack.generator){
    const g = pack.generator;
    pre = "cfg._source = window.MotorGen['"+g.kind+"']("+JSON.stringify(g)+");\n"+
          "cfg._tagLabel = cfg._source.tagLabel;\n";
  } else if(pack.classify && pack.classify.items){
    pre = "cfg._source = { items: cfg.classify.items };\n";
  }
  return "(function(){\n"+
    "var cfg = "+JSON.stringify(cfg)+";\n"+
    pre+
    "Motor.mount(document.getElementById('app'), cfg);\n"+
    "})();";
}

function buildPack(pack, srcName){
  const css = cssFor(pack).map(read).join("\n");
  const js  = jsFor(pack).map(read).join("\n;\n");
  const html =
"<!DOCTYPE html>\n<html lang=\"nl\">\n<head>\n<meta charset=\"utf-8\">\n"+
"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"+
"<title>"+strip(pack.title)+"</title>\n<style>\n"+css+"\n</style>\n</head>\n<body>\n"+
"<div id=\"app\"></div>\n"+
"<!-- Gegenereerd door spaans-motor uit content/"+srcName+" -->\n"+
"<script>\n"+js+"\n;\n"+bootstrap(pack)+"\n</script>\n</body>\n</html>\n";
  const outfile = join(OUT, pack.id+".html");
  writeFileSync(outfile, html, "utf8");
  return { id:pack.id, title:strip(pack.title), template:pack.template, file:pack.id+".html", bytes:html.length };
}

function strip(s){ return String(s).replace(/<[^>]+>/g,"").replace(/\s+/g," ").trim(); }

/* --- alle pakketten bouwen --- */
const packs = readdirSync(CONTENT).filter(f=>f.endsWith(".json"));
const built = [];
for(const f of packs){
  const pack = JSON.parse(read(join(CONTENT,f)));
  try{ built.push(buildPack(pack,f)); console.log("  ✓ "+pack.id+"  ("+pack.template+")"); }
  catch(e){ console.log("  ✗ "+f+" — "+e.message); }
}

/* --- index.html: menu naar alle spellen --- */
const tplName = { classify:"classificeren", match:"koppelen", cloze:"invullen", order:"volgorde", point:"aanwijzen", tap:"aanwijzen", memory:"memoria", sim:"produceren", speak:"spreken", type:"escribir", tetris:"arcade", belt:"arcade", mole:"arcade", bubble:"arcade", snake:"arcade" };
const cards = built.map(b=>
  '<a class="ix-card" href="games/'+b.file+'">'+
    '<span class="ix-badge">'+(tplName[b.template]||b.template)+'</span>'+
    '<span class="ix-title">'+b.title+'</span>'+
  '</a>').join("\n");
const index =
"<!DOCTYPE html>\n<html lang=\"nl\">\n<head>\n<meta charset=\"utf-8\">\n"+
"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<title>Oefenspellen Spaans</title>\n<style>\n"+
read(join(SRC,"tokens.css"))+"\n"+
"*{box-sizing:border-box}body{margin:0;min-height:100vh;font-family:var(--sans);color:var(--cal);"+
"background:linear-gradient(180deg,var(--muro),var(--muro-2));padding:32px 18px 60px}"+
".ix-wrap{max-width:900px;margin:0 auto}"+
"h1{font-family:var(--serif);letter-spacing:.12em;font-size:clamp(26px,5vw,40px);margin:0 0 4px}h1 span{color:var(--p2)}"+
"p.lead{font-family:var(--serif);font-style:italic;color:var(--cal-dim);margin:0 0 28px}"+
".ix-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}"+
".ix-card{display:flex;flex-direction:column;gap:8px;padding:18px;border-radius:3px;text-decoration:none;"+
"background:linear-gradient(175deg,#FBF6E9,#E9E0C9);color:#12264A;border:1px solid rgba(0,0,0,.2);"+
"box-shadow:0 5px 0 rgba(0,0,0,.22);transition:transform .1s}"+
".ix-card:active{transform:translateY(3px)}"+
".ix-badge{align-self:flex-start;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:#8A7F66;"+
"border:1px solid #C3B99F;border-radius:2px;padding:2px 7px}"+
".ix-title{font-family:var(--serif);font-weight:700;font-size:19px}"+
"</style>\n</head>\n<body>\n<div class=\"ix-wrap\">\n"+
"<h1>Oefen<span>spellen</span></h1>\n<p class=\"lead\">Tik een spel om te starten.</p>\n"+
"<div class=\"ix-grid\">\n"+cards+"\n</div>\n</div>\n</body>\n</html>\n";
writeFileSync(join(ROOT,"index.html"), index, "utf8");

console.log("\n"+built.length+" spel(len) gebouwd → /games, menu → index.html");
