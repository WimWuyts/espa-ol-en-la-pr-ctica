#!/usr/bin/env python3
# Genereert de zelfstandige HTML-hub voor U0 (flashcards, woordenschat-zoek,
# visuele/interactieve grammatica + spellen). Één standalone bestand:
#  - fonts base64 ingebed
#  - de 17 motor-arcade-spellen base64 ingebed → werken ook als je het bestand downloadt
#  - interactieve kaart (klik een land) + interactief abecedario + spraak (TTS)
# NB: géén werkwoordsvervoeging (conjugador/vervoegingscirkel) — dat hoort niet in U0.
import json, base64, os, sys

ROOT="/home/user/espa-ol-en-la-pr-ctica"
GEN=f"{ROOT}/02-huisstijl/beeld/generators"
vocab=json.load(open(f"{ROOT}/01-cursussen/05-a1/U0/u0_vocab.json"))
mapsvg=open(f"{GEN}/mundo_map_real.svg").read()
sys.path.insert(0,GEN); import cast_gen as C; import vocab_icons as VI
moch=C.mochila("100%","compass")
ICONS=[VI.icon_svg(v.get("es",""),v.get("grp",""),size=34,color="var(--gd)") for v in vocab]

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

# ---- de 17 motor-arcade-spellen: gegroepeerd + base64 ingebed ----
MOTOR=[
 ['Sonidos · uitspraak',[['be-uve','b = v · con be/uve','classify'],['hache-muda','h muda · hola↔ola','cloze'],['la-jota','la jota · ge/gi/j','classify']]],
 ['El acento · el sombrero',[['aguda-llana-esdrujula','aguda/llana/esdrújula','classify'],['silaba-tonica','tik de tónica','tap'],['lleva-tilde','¿con/sin tilde?','cloze'],['donde-va-la-tilde','waar staat de tilde?','tap']]],
 ['Números 0–100',[['numeros-match','cifra ↔ letra','match'],['numeros-orden','klein → groot','order'],['numeros-memoria','geheugenspel','memory']]],
 ['Saludos · lengua de clase',[['saludos','saludos ES↔NL','match'],['saludo-despedida','saludo/despedida/cortesía','classify'],['lenguaje-de-clase','klaszinnen aanvullen','cloze']]],
 ['Vocabulario · mundo hispano',[['vocabulario-match','woordenschat ES↔NL','match'],['vocabulario-memoria','geheugenspel','memory'],['gentilicios','país ↔ gentilicio','match'],['genero','el / la','classify']]],
]
GAMEDIR=f"{ROOT}/spaans-motor/games"
slugs=[g[0] for grp in MOTOR for g in grp[1]]
GAMES={s: b64(f"{GAMEDIR}/es-u0-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-u0-{s}.html")}

CSS = FONTS + """
:root{--g:#1E9E74;--gd:#157355;--gt:#E4F4EE;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E4E3DE;--red:#DC2626;--amber:#B7860B;--card:#fff;
--onder:#2563EB;--ww:#EA7317;--voorw:#1E9E74;--tijd:#7C3AED;--plaats:#14B8A6;
--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif;--hand:'Caveat',cursive}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#171713;--crema:#22221C;--gt:#12352A;--line:#33332B;--card:#20201A}
*{box-sizing:border-box}
body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
a{color:var(--gd)}
header.top{position:sticky;top:0;z-index:30;background:var(--g);color:#fff;box-shadow:0 2px 10px #0002}
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
.subnav{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 8px;padding:10px 0;position:sticky;top:52px;background:var(--paper);z-index:20;border-bottom:1px solid var(--line)}
.subnav button{border:1.5px solid var(--line);background:var(--card);color:var(--ink);font-weight:600;font-size:13px;padding:7px 13px;border-radius:20px;cursor:pointer}
.subnav button.on{background:var(--g);color:#fff;border-color:var(--g)}
section.panel{display:none;animation:fade .3s}
section.panel.show{display:block}
@keyframes fade{from{opacity:0;transform:translateY(6px)}to{opacity:1}}
h2.sec{font-family:var(--disp);font-weight:700;color:var(--gd);font-size:24px;margin:22px 0 4px}
.subh{font-family:var(--disp);color:var(--ink);font-size:17px;margin:26px 0 6px;padding-bottom:5px;border-bottom:2px solid var(--gt);display:flex;align-items:center;gap:10px}
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
.fc .spk{position:absolute;top:6px;right:8px;font-size:14px;opacity:.5}
/* tabel */
table.vt{width:100%;border-collapse:collapse;font-size:14px}
table.vt th,table.vt td{border-bottom:1px solid var(--line);padding:8px 10px;text-align:left}
table.vt th{background:var(--gt);color:var(--gd);position:sticky;top:0;z-index:1}
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
.txin{border:1.5px solid var(--line);border-radius:10px;padding:8px 12px;font-size:16px;background:var(--card);color:var(--ink);font-family:var(--disp);width:120px}
.spk-btn{border:none;background:var(--gt);color:var(--gd);border-radius:10px;padding:9px 16px;font-weight:700;cursor:pointer;font-size:15px}
/* kleur-zin */
.csent{font-size:22px;font-family:var(--disp);line-height:2}
.csent span{padding:2px 5px;border-radius:6px;cursor:help;position:relative}
.csent .tip{display:none;position:absolute;left:50%;top:120%;transform:translateX(-50%);background:var(--ink);color:#fff;font-size:12px;font-family:var(--body);padding:5px 9px;border-radius:6px;white-space:nowrap;z-index:5}
.csent span:hover .tip,.csent span:focus .tip{display:block}
.legend{display:flex;gap:10px;flex-wrap:wrap;font-size:12px;margin-top:10px}
.legend i{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:4px;vertical-align:-1px}
/* abecedario */
.abcgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(64px,1fr));gap:8px;margin-top:10px}
.abc-l{border:1.5px solid var(--line);border-radius:12px;padding:8px 4px;text-align:center;cursor:pointer;background:var(--card)}
.abc-l:hover{border-color:var(--g);background:var(--gt)}
.abc-l .big{font-family:var(--disp);font-weight:800;font-size:20px;color:var(--gd)}
.abc-l .nm{font-size:10px;color:var(--mut)}
.foot{color:var(--mut);font-size:12px;text-align:center;margin-top:30px}
/* kaart interactief */
#mapwrap svg{width:100%;height:auto}
#mapwrap path.spa,#mapwrap path.usa{transition:opacity .12s}
.mapinfo{margin-top:12px;padding:14px 16px;background:var(--gt);border-radius:12px;min-height:66px}
.mapinfo h3{margin:0 0 6px;font-family:var(--disp);color:var(--gd);font-size:19px}
.mapinfo .mrow{font-size:14px;margin:2px 0}
/* modal voor arcade-spellen */
.modal{display:none;position:fixed;inset:0;background:#0009;z-index:100;padding:16px}
.modal.show{display:flex;align-items:center;justify-content:center}
.modalbox{background:var(--card);border-radius:16px;width:min(940px,97vw);height:min(90vh,940px);display:flex;flex-direction:column;overflow:hidden;box-shadow:0 20px 60px #0006}
.modalbar{display:flex;justify-content:space-between;align-items:center;padding:10px 14px;background:var(--g);color:#fff;font-family:var(--disp);font-weight:700}
.modalbar button{background:#ffffff22;border:none;color:#fff;padding:6px 12px;border-radius:8px;cursor:pointer;font-weight:700;font-family:var(--disp)}
.modal iframe{border:0;flex:1;width:100%;background:#fff}
@media(max-width:600px){.hero h1{font-size:26px}.bar{flex-wrap:wrap}}
/* bewerk-in-browser */
.editbar{position:fixed;right:14px;bottom:14px;z-index:9999;display:flex;gap:8px;align-items:center;background:var(--gd);color:#fff;padding:8px 12px;border-radius:12px;box-shadow:0 6px 20px #0004;font-size:13px}
.editbar button{border:none;border-radius:8px;padding:7px 12px;font-weight:700;cursor:pointer;font-family:inherit;font-size:13px}
.editbar .b1{background:#fff;color:var(--gd)}.editbar .b2{background:#ffffff22;color:#fff}.editbar.on{background:var(--amber)}
body.editing [contenteditable=true]{outline:1.4px dashed var(--amber);outline-offset:2px;border-radius:3px}
body.editing [contenteditable=true]:focus{outline:2px solid var(--gd);background:#FEF9E7}
@media print{.editbar{display:none!important}}
"""

def data_js():
    return ("const VOCAB="+json.dumps(vocab,ensure_ascii=False)+";\n"
            +"const ICONS="+json.dumps(ICONS,ensure_ascii=False)+";\n"
            +"const MOTOR="+json.dumps(MOTOR,ensure_ascii=False)+";\n"
            +"const GAMES="+json.dumps(GAMES)+";\n")

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
    <p>La página digital de la Unidad 0: flashcards, woordenschat, gramática visual e interactiva y <b>juegos</b>. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR in het boek brengt je hier om te oefenen — zelfde thema, meer interactie.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U0. Klik om te draaien; wissel ES↔NL; klik 🔊 om te horen. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
    __FC__
    <h2 class="sec">Naslagwerk · zoeken</h2>
    __NAS__
  </section>

  <section class="panel" data-p="gram">
    <h2 class="sec">Gramática visual e interactiva</h2>
    <p class="lead">Eerst betekenis en patroon ontdekken, dan de regel. Beweeg over de woorden, klik, en probeer. <span class="gloss">Alles binnen het thema van U0: klanken, het abecedario en het accent.</span></p>
    <div class="card" id="abc"></div>
    <div class="card" id="colorsent"></div>
    <div class="game" id="g_tilde"></div>
    <div class="game" id="g_silaba"></div>
  </section>

  <section class="panel" data-p="juegos">
    <h2 class="sec">Ejercicios · veel oefeningen, jij kiest</h2>
    <p class="lead">Een ruime keuze aan oefeningen, geordend van <b>herkennen → luisteren → kiezen → zelf schrijven → communiceren</b>. Kies wat je wil oefenen; elke ronde geeft directe, verklarende feedback en de steun bouwt af (model → beginletter → geen steun).</p>
    <h3 class="subh">① Reconocer · luisteren &amp; herkennen <span class="pill">receptief</span></h3>
    <div class="game" id="g_escucha"></div>
    <div class="game" id="g_sonido"></div>
    <div class="game" id="g_marcatilde"></div>
    <div class="game" id="g_sombrero"></div>
    <div class="game" id="g_vf"></div>
    <h3 class="subh">② Practicar · gestuurd produceren <span class="pill">productief met steun</span></h3>
    <div class="game" id="g_completa"></div>
    <div class="game" id="g_dictado"></div>
    <div class="game" id="g_ordenaletras"></div>
    <div class="game" id="g_numeros"></div>
    <div class="game" id="g_escribenum"></div>
    <div class="game" id="g_saludos"></div>
    <div class="game" id="g_genero"></div>
    <h3 class="subh">③ Producir &amp; comunicar <span class="pill">vrije productie</span></h3>
    <div class="game" id="g_orden"></div>
    <div class="game" id="g_presentate"></div>
    <h3 class="subh">④ Repasar jugando <span class="pill">arcade</span></h3>
    <div class="game" id="g_memory"></div>
    <div class="card" id="motorlink"></div>
  </section>

  <section class="panel" data-p="cultura">
    <h2 class="sec">Cultura · El mundo hispano</h2>
    <p class="lead">El español no vive solo en España: es la lengua de más de 20 países. <span class="gloss">Spaans woont niet alleen in Spanje — het is de taal van meer dan 20 landen en ~500 miljoen sprekers.</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>La lengua de más de 20 países 🌍</h3>
      <p>El español es lengua oficial en <b>España</b>, en casi toda <b>Hispanoamérica</b> y hasta en <b>Guinea Ecuatorial</b> (África). Este año paras en cuatro sitios: España · México · Colombia · Perú. <span class="gloss">Spaans is officiële taal in Spanje, in bijna heel Spaanstalig Amerika en zelfs in Equatoriaal-Guinea. Dit jaar houd je halt op vier plekken.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 11V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2"/><path d="M14 10V4a2 2 0 0 0-2-2a2 2 0 0 0-2 2v2"/><path d="M10 10.5V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2v8"/><path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15"/></svg>Saludar en todas partes</h3>
      <p>En todo el mundo hispano se dice <b>«¡Hola!»</b>, pero cada país tiene su color: <i>¿Qué tal?</i> (España), <i>¿Qué onda?</i> (México), <i>¿Quiubo?</i> (Colombia). <span class="gloss">Overal klinkt «¡Hola!», maar elk land heeft zijn eigen kleur en groetvarianten — diversiteit binnen één taal.</span></p></div>
    <h3 class="subh">La Ruta · ¿dónde estamos?</h3>
    <p class="lead">Onze parada 0: <b>El mundo hispano → España</b>. <b>Klik op een groen land</b> op de kaart voor info. Verderop: México → Colombia → Perú.</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een groen land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    <h2 class="sec">Extra · bronnen</h2>
    <p class="lead">Externe uitleg & oefeningen (de leerkracht vult de links aan).</p>
    <div class="card"><p>🎬 <b>profedeele</b> (YouTube-grammatica) — <span class="gloss">link volgt.</span></p>
    <p>🧩 <b>arche-ele</b> (Genially woordenschat/grammatica) — <span class="gloss">link volgt.</span></p>
    <p>📄 In het boek (PDF) verwijzen de QR-codes naar déze pagina, op het juiste ankerpunt.</p></div>
  </section>

  <div class="foot">Español en la práctica · C5 · Unidad 0 — página digital (v2). Uitbreiding op de PDF · huisstijl groen · print ↔ PowerPoint ↔ web.</div>
</main>

<div class="modal" id="gmodal"><div class="modalbox">
  <div class="modalbar"><span id="gmtitle">Juego</span><button onclick="closeGame()">✕ sluiten</button></div>
  <iframe id="gframe" title="Spel"></iframe>
</div></div>

<div class="editbar" id="editbar">
  <span id="ebtxt">✏️ «Bewerken» om titels/teksten aan te passen</span>
  <button class="b1" id="ebEdit">Bewerken</button>
  <button class="b2" id="ebSave">💾 Bewaar</button>
</div>

<script>__DATA__
__JS__
</script></body></html>"""

JS = r"""
function toggleTheme(){const r=document.documentElement;r.dataset.theme=r.dataset.theme==='dark'?'light':'dark'}
// ---------- spraak (TTS) ----------
function speak(t,rate){if(!('speechSynthesis'in window))return;const u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=rate||.92;
  const vs=speechSynthesis.getVoices();const es=vs.find(v=>/^es/i.test(v.lang));if(es)u.voice=es;try{speechSynthesis.cancel();speechSynthesis.speak(u);}catch(e){}}
const TTS=('speechSynthesis'in window);
if(TTS){speechSynthesis.getVoices();speechSynthesis.onvoiceschanged=()=>{};}
// subnav
const PANELS=[['vocab','Vocabulario'],['gram','Gramática'],['juegos','Juegos'],['cultura','Cultura'],['extra','Extra']];
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
    d.innerHTML='<div class="in"><div class="s">'+(TTS?'<span class="spk" title="luister">🔊</span>':'')+(ICONS[i]||'')+'<div class="w">'+front+'</div>'+(ej?'<div class="ej">'+ej+'</div>':'')+'</div><div class="b"><div class="tr">'+back+'</div></div></div>';
    d.onclick=()=>d.classList.toggle('flip');d.onkeydown=e=>{if(e.key===' '||e.key==='Enter'){e.preventDefault();d.classList.toggle('flip')}};
    const sp=d.querySelector('.spk');if(sp)sp.onclick=e=>{e.stopPropagation();speak(v.es);};
    g.appendChild(d);});
  document.getElementById('fccount').textContent=n+' woorden';}
// ---------- naslag ----------
function renderTable(){const q=(document.getElementById('vsearch').value||'').toLowerCase();const b=document.getElementById('vbody');b.innerHTML='';let n=0;
  VOCAB.forEach(v=>{if(q&&!(v.es.toLowerCase().includes(q)||v.nl.toLowerCase().includes(q)||v.ej.toLowerCase().includes(q)))return;n++;
    const tr=document.createElement('tr');tr.innerHTML='<td><b>'+v.es+'</b></td><td>'+v.nl+'</td><td>'+v.soort+'</td><td class="gloss">'+v.ej+'</td>';b.appendChild(tr);});
  document.getElementById('vcount').textContent=n+' items';}

// ---------- helpers spellen ----------
function scoreBar(id){return '<div class="scorebar" id="'+id+'"><span>Punten: <b class="pt">0</b></span><span>Reeks: <b class="st">0</b></span></div>'}
function setScore(el,pt,st){el.querySelector('.pt').textContent=pt;el.querySelector('.st').textContent=st}
function feedback(el,ok,msg){el.className='fb '+(ok?'good':'bad');el.innerHTML=(ok?'✅ ':'❌ ')+msg}
function strip(w){return w.normalize('NFD').replace(/[̀-ͯ]/g,'')}

// ---------- ABECEDARIO interactief (klik → hoor de naam + voorbeeld) ----------
(function(){const el=document.getElementById('abc');
 const L=[['a','a','árbol'],['b','be','bota'],['c','ce','casa'],['ch','che','chocolate'],['d','de','dedo'],['e','e','elefante'],['f','efe','foca'],['g','ge','gato'],['h','hache','hola'],['i','i','isla'],['j','jota','jamón'],['k','ka','kilo'],['l','ele','luna'],['ll','elle','lluvia'],['m','eme','mesa'],['n','ene','nube'],['ñ','eñe','niño'],['o','o','oso'],['p','pe','perro'],['q','cu','queso'],['r','erre','rojo'],['s','ese','sol'],['t','te','taza'],['u','u','uva'],['v','uve','vaca'],['w','uve doble','wifi'],['x','equis','examen'],['y','ye','yo'],['z','zeta','zapato']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 4px">El abecedario — 27 letras (+ ch, ll)</h3><p class="desc">Klik een letter: je hoort de <b>naam</b> van de letter en een voorbeeldwoord. Let op de valstrikken: <b>h</b> (muda), <b>j / ge / gi</b> (jota), <b>ll / y</b>, <b>ñ</b>, <b>z / ce / ci</b>.</p><div class="abcgrid" id="abcg"></div><div class="fb" id="abcfb"></div>';
 const g=el.querySelector('#abcg');
 L.forEach(([ltr,nm,ej])=>{const d=document.createElement('div');d.className='abc-l';d.innerHTML='<div class="big">'+ltr+'</div><div class="nm">'+nm+'</div>';
   d.onclick=()=>{speak(nm);setTimeout(()=>speak(ej),700);feedback(el.querySelector('#abcfb'),true,'<b>'+ltr+'</b> = «'+nm+'» · '+ej);};g.appendChild(d);});
 if(!TTS)el.querySelector('.desc').innerHTML+=' <span class="gloss">(Spraak werkt in Chrome/Edge.)</span>';
})();

// ---------- kleur-zin (grammar-viz) ----------
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Kleurgecodeerde zin — beweeg over de woorden</h3>'+
'<div class="csent">'+
'<span style="background:#dbeafe;color:#1e40af">Yo<span class="tip">onderwerp (persona)</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">me llamo<span class="tip">werkwoord (llamarse)</span></span> '+
'<span style="background:#dcfce7;color:#166534">Lucía<span class="tip">naam / voorwerp</span></span> '+
'<span style="background:#ede9fe;color:#5b21b6">hoy<span class="tip">tijd (ahora)</span></span>.</div>'+
'<div class="legend"><span><i style="background:#93c5fd"></i>onderwerp</span><span><i style="background:#fdba74"></i>werkwoord</span><span><i style="background:#86efac"></i>voorwerp</span><span><i style="background:#c4b5fd"></i>tijd</span></div>';

// ---------- GAME: escucha (luisteren, TTS) ----------
function gameEscucha(){const el=document.getElementById('g_escucha');
 if(!TTS){el.innerHTML='<h3>¿Qué oyes? — luisteren</h3><p class="desc">Je browser ondersteunt geen spraak. Probeer Chrome of Edge om deze luisteroefening te doen.</p>';return;}
 const bank=['uno','dos','siete','doce','veinte','treinta','cien','hola','gracias','adiós','buenos días','México','España','Perú'];
 let pt=0,st=0;
 el.innerHTML='<h3>¿Qué oyes? — luisteren</h3><p class="desc">Klik ▶, luister en kies wat je hoort. Herbeluisteren mag.</p>'+scoreBar('sbE')+
  '<div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:6px 0"><button class="spk-btn" id="ePlay">▶ Speel af</button></div><div class="chips" id="eOpts" style="margin-top:8px"></div><div class="fb" id="eFb"></div>';
 const sb=el.querySelector('#sbE');
 function next(){const ans=bank[Math.floor(Math.random()*bank.length)];el.cur=ans;
   const opts=[ans];while(opts.length<4){const c=bank[Math.floor(Math.random()*bank.length)];if(!opts.includes(c))opts.push(c);}opts.sort(()=>Math.random()-.5);
   const oc=el.querySelector('#eOpts');oc.innerHTML='';opts.forEach(o=>{const c=document.createElement('div');c.className='chip';c.textContent=o;c.onclick=()=>{const ok=o===ans;if(ok){pt++;st++}else st=0;setScore(sb,pt,st);
     oc.querySelectorAll('.chip').forEach(z=>{if(z.textContent===ans)z.classList.add('ok');else if(z===c&&!ok)z.classList.add('no');});
     feedback(el.querySelector('#eFb'),ok,(ok?'¡Sí! ':'Je hoorde: ')+'«'+ans+'».');setTimeout(next,1100);};oc.appendChild(c);});
   el.querySelector('#eFb').className='fb';speak(ans);}
 el.querySelector('#ePlay').onclick=()=>speak(el.cur);next();}
// ---------- GAME: klank sorteren (b=v / h muda / jota) ----------
function gameSonido(){const el=document.getElementById('g_sonido');
 const items=[['vaca','bv'],['bota','bv'],['hola','h'],['hora','h'],['jamón','j'],['gente','j'],['vino','bv'],['hijo','h'],['gigante','j']];
 const cats={bv:'b = v (zelfde klank)',h:'h · zwijgt',j:'jota (j · ge · gi)'};
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>Klank-detective</h3><p class="desc">In welke klankfamilie hoort het woord? Klik 🔊 om te horen, kies dan de familie.</p>'+scoreBar('sb1')+
  '<div style="display:flex;gap:10px;align-items:center;justify-content:center;margin:8px 0"><span id="s1word" style="font-size:26px;font-family:var(--disp)"></span>'+(TTS?'<button class="spk-btn" id="s1play">🔊</button>':'')+'</div>'+
  '<div class="chips" id="s1cats" style="justify-content:center"></div><div class="fb" id="s1fb"></div>';
 const sb=el.querySelector('#sb1');const cont=el.querySelector('#s1cats');
 Object.entries(cats).forEach(([k,v])=>{const c=document.createElement('div');c.className='chip';c.textContent=v;c.onclick=()=>guess(k);cont.appendChild(c);});
 const pb=el.querySelector('#s1play');if(pb)pb.onclick=()=>speak(el.cur[0]);
 function next(){if(!pool.length)pool=items.slice();const idx=Math.floor(Math.random()*pool.length);el.cur=pool.splice(idx,1)[0];el.querySelector('#s1word').textContent=el.cur[0];el.querySelector('#s1fb').className='fb';}
 function guess(k){const ok=k===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);
   const ex={bv:'b en v klinken identiek in het Spaans.',h:'de h wordt niet uitgesproken.',j:'j, en ge/gi, klinken als een harde keel-ch.'};
   feedback(el.querySelector('#s1fb'),ok,ok?('«'+el.cur[0]+'» — juist! '+ex[el.cur[1]]):('«'+el.cur[0]+'» hoort bij: '+cats[el.cur[1]]+'. '+ex[el.cur[1]]));setTimeout(next,950);}
 next();}
// ---------- GAME: la regla del sombrero ----------
function gameSombrero(){const el=document.getElementById('g_sombrero');
 const items=[['café','aguda'],['casa','llana'],['México','esdrujula'],['Perú','aguda'],['árbol','llana'],['teléfono','esdrujula'],['lunes','llana'],['adiós','aguda'],['música','esdrujula']];
 const cats={aguda:'aguda (laatste)',llana:'llana (voorlaatste)',esdrujula:'esdrújula (3e van achteren)'};
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>La regla del sombrero</h3><p class="desc">Waar ligt de klemtoon? Kies de familie.</p>'+scoreBar('sb2')+
  '<div id="s2word" style="font-size:26px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" id="s2cats" style="justify-content:center"></div><div class="fb" id="s2fb"></div>';
 const sb=el.querySelector('#sb2');const cont=el.querySelector('#s2cats');
 Object.entries(cats).forEach(([k,v])=>{const c=document.createElement('div');c.className='chip';c.textContent=v;c.onclick=()=>guess(k);cont.appendChild(c);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#s2word').textContent=el.cur[0];el.querySelector('#s2fb').className='fb';}
 function guess(k){const ok=k===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);
   feedback(el.querySelector('#s2fb'),ok,ok?'¡Correcto! «'+el.cur[0]+'» is '+cats[el.cur[1]]+'.':'«'+el.cur[0]+'» is '+cats[el.cur[1]]+'.');setTimeout(next,950);}
 next();}
// ---------- GAME: completa (gap-fill, productief) ----------
function gameCompleta(){const el=document.getElementById('g_completa');
 // woord met ontbrekende letter (accent/valstrik); typ de ontbrekende letter(s)
 const items=[['café','caf_','é','aguda op klinker → tilde'],['adiós','adi_s','ó','aguda op -s → tilde'],['México','M_xico','é','esdrújula → altijd tilde'],['música','m_sica','ú','esdrújula → altijd tilde'],['jamón','jam_n','ó','aguda op -n → tilde'],['teléfono','tel_fono','é','esdrújula → altijd tilde'],['hola','_ola','h','de h is muda (zwijgt)'],['gente','_ente','g','ge klinkt als jota']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>Completa la palabra — vul aan</h3><p class="desc">Typ de ontbrekende letter (met of zonder hoedje) en druk Enter.</p>'+scoreBar('sbC')+
  '<div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:8px 0"><span id="cWord" style="font-size:26px;font-family:var(--disp)"></span><input class="txin" id="cIn" placeholder="?" autocomplete="off"><button class="btn small" id="cGo">OK</button></div><div class="fb" id="cFb"></div>';
 const sb=el.querySelector('#sbC');const inp=el.querySelector('#cIn');
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#cWord').textContent=el.cur[1].replace('_','__');inp.value='';inp.focus();el.querySelector('#cFb').className='fb';}
 function check(){const g=(inp.value||'').trim().toLowerCase();if(!g)return;const ok=g===el.cur[2];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);
   feedback(el.querySelector('#cFb'),ok,(ok?'¡Perfecto! ':'De letter is «'+el.cur[2]+'». ')+'«'+el.cur[0]+'» — '+el.cur[3]+'.');setTimeout(next,1200);}
 el.querySelector('#cGo').onclick=check;inp.onkeydown=e=>{if(e.key==='Enter')check();};next();}
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
// ---------- GAME: verdadero o falso (regels) ----------
function gameVF(){const el=document.getElementById('g_vf');
 const items=[['«b» y «v» suenan igual.',true],['La «h» se pronuncia siempre.',false],['Las esdrújulas siempre llevan tilde.',true],['«casa» lleva tilde.',false],['«ñ» suena como «nj» (español ↔ Spanje).',true],['Los números 16–29 se escriben en una palabra.',true],['«el mapa» es incorrecto; es «la mapa».',false],['«j», «ge» y «gi» tienen el sonido de la jota.',true]];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿Verdadero o falso? — de regels</h3><p class="desc">Klopt de bewering over uitspraak/accent/getallen? Kies.</p>'+scoreBar('sbV')+
  '<div id="vfStmt" style="font-size:18px;font-family:var(--disp);text-align:center;margin:10px 0;min-height:48px"></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._vf(true)">✓ verdadero</div><div class="chip" onclick="window._vf(false)">✗ falso</div></div><div class="fb" id="vfFb"></div>';
 const sb=el.querySelector('#sbV');
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#vfStmt').textContent=el.cur[0];el.querySelector('#vfFb').className='fb';}
 window._vf=g=>{const ok=g===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);
   feedback(el.querySelector('#vfFb'),ok,(ok?'¡Correcto! ':'Nee → ')+'de bewering is '+(el.cur[1]?'verdadera (waar)':'falsa (onwaar)')+'.');setTimeout(next,1100);};
 next();}
// ---------- GAME: woordvolgorde ----------
function gameOrden(){const el=document.getElementById('g_orden');
 const sol=['Yo','me llamo','Diego','y','soy de México'];let cur=[],pool=sol.slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>Bouw de zin — woordvolgorde</h3><p class="desc">Klik de tegels in de juiste volgorde. Doel: een correcte voorstelzin.</p>'+
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
 function next(){if(!pool.length)pool=W.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#tiWord').textContent=strip(el.cur[0]);el.querySelector('#tiFb').className='fb';}
 window._tiGuess=g=>{const ok=g===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);
   feedback(el.querySelector('#tiFb'),ok,(ok?'¡Correcto! ':'')+'«'+el.cur[0]+'» — '+el.cur[2]+(el.cur[1]?' → wél een hoedje.':' → géén hoedje.'));setTimeout(next,1100);};
 next();}

// ---------- GAME: marca las tildes (receptief, multi-select) ----------
function gameMarcaTilde(){const el=document.getElementById('g_marcatilde');
 const bank=[['café',1],['casa',0],['México',1],['lunes',0],['adiós',1],['reloj',0],['música',1],['gente',0],['jamón',1],['mano',0],['sílaba',1],['acento',0]];
 let pt=0,st=0;
 function round(){const set=bank.slice().sort(()=>Math.random()-.5).slice(0,6);
  el.innerHTML='<h3>Marca las tildes — klik alle woorden mét accent</h3><p class="desc">Selecteer élk woord dat een hoedje (´) draagt en klik Controleer.</p>'+scoreBar('sbMt')+'<div class="chips" id="mtW" style="justify-content:center"></div><div class="answerbtns"><button class="btn small" id="mtGo">Controleer</button><button class="btn sec small" id="mtNew">Nieuwe ronde</button></div><div class="fb" id="mtFb"></div>';
  const c=el.querySelector('#mtW');set.forEach(([w,t])=>{const d=document.createElement('div');d.className='chip';d.textContent=w;d.dataset.t=t;d.onclick=()=>d.classList.toggle('sel');c.appendChild(d);});
  el.querySelector('#mtGo').onclick=()=>{let ok=true;c.querySelectorAll('.chip').forEach(d=>{const sel=d.classList.contains('sel');const t=d.dataset.t==='1';if(t&&sel){d.classList.add('ok')}else if((!t&&sel)||(t&&!sel)){d.classList.add('no');ok=false}});
   const sb=el.querySelector('#sbMt');if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#mtFb'),ok,ok?'¡Perfecto! Alle accenten juist aangeduid.':'Rood = fout aangeduid of gemist. Esdrújula draagt áltijd een accent.');};
  el.querySelector('#mtNew').onclick=round;}
 round();}
// ---------- GAME: dictado (productief, TTS → typen) ----------
function gameDictado(){const el=document.getElementById('g_dictado');
 if(!TTS){el.innerHTML='<h3>Dictado — schrijf wat je hoort</h3><p class="desc">Spraak werkt in Chrome/Edge; open de pagina daar voor deze oefening.</p>';return;}
 const bank=['hola','gracias','México','España','café','adiós','uno','doce','veinte','buenos días','jamón','música','Perú','Colombia'];
 let pt=0,st=0;
 el.innerHTML='<h3>Dictado — schrijf wat je hoort</h3><p class="desc">Klik ▶, luister en typ het woord (juiste letters én accenten). Enter = controleer.</p>'+scoreBar('sbD')+'<div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:8px 0"><button class="spk-btn" id="dPlay">▶ Speel af</button><input class="txin" id="dIn" style="width:220px" placeholder="typ hier…" autocomplete="off"><button class="btn small" id="dGo">OK</button></div><div class="fb" id="dFb"></div>';
 const sb=el.querySelector('#sbD');const inp=el.querySelector('#dIn');
 function next(){el.cur=bank[Math.floor(Math.random()*bank.length)];inp.value='';inp.focus();el.querySelector('#dFb').className='fb';speak(el.cur);}
 function check(){const g=(inp.value||'').trim().toLowerCase();if(!g)return;const ok=g===el.cur.toLowerCase();const near=strip(g)===strip(el.cur.toLowerCase());
   if(ok){pt++;st++}else st=0;setScore(sb,pt,st);
   feedback(el.querySelector('#dFb'),ok,ok?'¡Perfecto! «'+el.cur+'».':(near?'Bijna! Let op het accent → «'+el.cur+'».':'Het woord was: «'+el.cur+'».'));setTimeout(next,1500);}
 el.querySelector('#dPlay').onclick=()=>speak(el.cur);el.querySelector('#dGo').onclick=check;inp.onkeydown=e=>{if(e.key==='Enter')check();};next();}
// ---------- GAME: escribe el número ----------
function gameEscribeNumero(){const el=document.getElementById('g_escribenum');
 const M={0:'cero',1:'uno',2:'dos',3:'tres',4:'cuatro',5:'cinco',6:'seis',7:'siete',8:'ocho',9:'nueve',10:'diez',11:'once',12:'doce',13:'trece',14:'catorce',15:'quince',16:'dieciséis',17:'diecisiete',18:'dieciocho',19:'diecinueve',20:'veinte',21:'veintiuno',30:'treinta',40:'cuarenta',50:'cincuenta',100:'cien'};
 const keys=Object.keys(M);let pt=0,st=0;
 el.innerHTML='<h3>Escribe el número — schrijf voluit</h3><p class="desc">Schrijf het getal in letters. Tip: 16–29 = één woord. Enter = controleer.</p>'+scoreBar('sbN2')+'<div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:8px 0"><span id="nNum" style="font-size:30px;font-family:var(--disp);color:var(--gd)"></span><input class="txin" id="nIn" style="width:240px" placeholder="in letters…" autocomplete="off"><button class="btn small" id="nGo">OK</button></div><div class="fb" id="nFb"></div>';
 const sb=el.querySelector('#sbN2');const inp=el.querySelector('#nIn');
 function next(){el.cur=keys[Math.floor(Math.random()*keys.length)];el.querySelector('#nNum').textContent=el.cur;inp.value='';inp.focus();el.querySelector('#nFb').className='fb';}
 function check(){const g=(inp.value||'').trim().toLowerCase();if(!g)return;const want=M[el.cur];const ok=strip(g)===strip(want);
   if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#nFb'),ok,ok?'¡Correcto! '+el.cur+' = «'+want+'».':el.cur+' = «'+want+'».');setTimeout(next,1300);}
 el.querySelector('#nGo').onclick=check;inp.onkeydown=e=>{if(e.key==='Enter')check();};next();}
// ---------- GAME: ordena las letras (anagram) ----------
function gameOrdenaLetras(){const el=document.getElementById('g_ordenaletras');
 const bank=['hola','gato','casa','sol','luna','mesa','jamón','café','México','gracias','España','vaca'];
 function next(el2){const w=bank[Math.floor(Math.random()*bank.length)];el.cur=w;let cur=[],pool=w.split('').sort(()=>Math.random()-.5);
  el.innerHTML='<h3>Ordena las letras — vorm het woord</h3><p class="desc">Klik de letters in de juiste volgorde.'+(TTS?' 🔊 hint beschikbaar.':'')+'</p>'+scoreBar('sbOl')+(TTS?'<button class="spk-btn" id="olPlay" style="margin:0 0 8px">🔊 hoor het woord</button>':'')+'<div class="chips" id="olPool" style="font-size:20px;justify-content:center"></div><div class="col" style="margin-top:10px"><h4>jouw woord</h4><div class="chips" id="olBuilt" style="font-size:20px"></div></div><div class="answerbtns"><button class="btn sec small" id="olReset">Reset</button><button class="btn sec small" id="olNew">Ander woord</button></div><div class="fb" id="olFb"></div>';
  const sb=el.querySelector('#sbOl');const pp=el.querySelector('#olPool'),bb=el.querySelector('#olBuilt');
  const pb=el.querySelector('#olPlay');if(pb)pb.onclick=()=>speak(w);
  function draw(){pp.innerHTML='';pool.forEach((ch,i)=>{const c=document.createElement('div');c.className='chip';c.textContent=ch;c.onclick=()=>{cur.push(ch);pool.splice(i,1);draw();built();check();};pp.appendChild(c);});}
  function built(){bb.innerHTML='';cur.forEach((ch,i)=>{const c=document.createElement('div');c.className='chip sel';c.textContent=ch;c.onclick=()=>{pool.push(ch);cur.splice(i,1);draw();built();};bb.appendChild(c);});}
  function check(){if(pool.length)return;const ok=cur.join('')===w;if(ok){el._pt=(el._pt||0)+1;el._st=(el._st||0)+1;setScore(sb,el._pt,el._st);feedback(el.querySelector('#olFb'),true,'¡'+w+'! Correcto.');setTimeout(()=>next(),1200);}else{el._st=0;setScore(sb,el._pt||0,0);feedback(el.querySelector('#olFb'),false,'Nog niet — reset en probeer opnieuw.');}}
  el.querySelector('#olReset').onclick=()=>{pool=pool.concat(cur);cur=[];pool.sort(()=>Math.random()-.5);draw();built();el.querySelector('#olFb').className='fb';};
  el.querySelector('#olNew').onclick=()=>next();draw();built();}
 next();}
// ---------- GAME: preséntate (vrije productie, steun bouwt af) ----------
function gamePresentate(){const el=document.getElementById('g_presentate');
 el.innerHTML='<h3>Preséntate — stel jezelf voor</h3><p class="desc">Vul je eigen gegevens in. Dit is <b>vrije productie</b>: er is geen «juist» antwoord — je maakt je eigen zin met het zinsframe. Zeg hem daarna hardop, en probeer ronde 2 uit het hoofd.</p>'+
  '<div style="display:grid;gap:8px;max-width:480px">'+
  '<div style="display:flex;gap:8px;align-items:center"><span style="font-family:var(--disp);min-width:78px">Me llamo</span><input class="txin" id="pr1" style="width:auto;flex:1" placeholder="je naam"></div>'+
  '<div style="display:flex;gap:8px;align-items:center"><span style="font-family:var(--disp);min-width:78px">Soy de</span><input class="txin" id="pr2" style="width:auto;flex:1" placeholder="stad / land"></div>'+
  '<div style="display:flex;gap:8px;align-items:center"><span style="font-family:var(--disp);min-width:78px">Tengo</span><input class="txin" id="pr3" style="width:80px" placeholder="14"><span style="font-family:var(--disp)">años.</span></div>'+
  '</div><div class="answerbtns"><button class="btn small" id="prGo">Maak mijn zin</button>'+(TTS?'<button class="spk-btn" id="prSpk">🔊 hoor mijn zin</button>':'')+'</div><div class="fb" id="prFb"></div>';
 el.querySelector('#prGo').onclick=()=>{const a=(el.querySelector('#pr1').value||'').trim()||'…',b=(el.querySelector('#pr2').value||'').trim()||'…',c=(el.querySelector('#pr3').value||'').trim()||'…';
   el.cur='Hola, me llamo '+a+'. Soy de '+b+' y tengo '+c+' años. ¿Y tú?';
   feedback(el.querySelector('#prFb'),true,'<b style="font-size:16px">'+el.cur+'</b><br><span class="gloss">Zeg het nu hardop. Ronde 2: dek de vakken af en zeg het uit het hoofd.</span>');};
 const sp=el.querySelector('#prSpk');if(sp)sp.onclick=()=>{if(el.cur)speak(el.cur);};}

// ---------- MOTOR-ARCADE: 17 spellen, ingebed (openen in modal, werkt offline) ----------
document.getElementById('motorlink').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 4px">Arcade · la máquina de juegos 🕹️</h3><p class="gloss" style="margin:0 0 10px">17 extra spellen met score & directe feedback — ingebed, dus ze werken ook als je dit bestand downloadt. Klik om te spelen.</p>'+
 MOTOR.map(([grp,gs])=>'<div style="margin:10px 0 4px;font-weight:700;color:var(--gd);font-size:13px">'+grp+'</div><div class="fcgrid">'+
   gs.map(([f,t,tpl])=>'<div class="chip" style="display:block;border-radius:12px" onclick="openGame(\''+f+'\',\''+t.replace(/'/g,"")+'\')"><div style="font-weight:700;color:var(--ink);font-size:14px">'+t+'</div><div class="pill" style="margin-top:4px;font-size:10px">'+tpl+'</div></div>').join('')+'</div>').join('');
function openGame(slug,title){const g=GAMES[slug];if(!g){alert('Spel niet gevonden.');return;}
  document.getElementById('gmtitle').textContent=title;document.getElementById('gframe').src='data:text/html;base64,'+g;document.getElementById('gmodal').classList.add('show');}
function closeGame(){document.getElementById('gmodal').classList.remove('show');document.getElementById('gframe').src='about:blank';}
document.getElementById('gmodal').addEventListener('click',e=>{if(e.target.id==='gmodal')closeGame();});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeGame();});

// ---------- KAART interactief (klik op een land) ----------
(function(){
 const INFO={
  ESP:{fl:'🇪🇸',n:'España',cap:'Madrid',f:'De bakermat van het Spaans; onze parada 0.',nl:'Vertrekpunt van de reis.',star:1},
  MEX:{fl:'🇲🇽',n:'México',cap:'Ciudad de México',f:'Het land met de meeste Spaanstaligen (~130 mln).',nl:'Meeste sprekers ter wereld · parada (Diego).',star:1},
  COL:{fl:'🇨🇴',n:'Colombia',cap:'Bogotá',f:'Parada: Cartagena, aan de Caribische kust.',nl:'Parada van Valen.',star:1},
  PER:{fl:'🇵🇪',n:'Perú',cap:'Lima',f:'Parada: Cusco en Machu Picchu, in de Andes.',nl:'Parada van Nina.',star:1},
  GTM:{fl:'🇬🇹',n:'Guatemala',cap:'Ciudad de Guatemala',f:'Rijke Maya-erfenis.',nl:''},
  HND:{fl:'🇭🇳',n:'Honduras',cap:'Tegucigalpa',f:'In het hart van Centraal-Amerika.',nl:''},
  SLV:{fl:'🇸🇻',n:'El Salvador',cap:'San Salvador',f:'Het kleinste land van Centraal-Amerika.',nl:''},
  NIC:{fl:'🇳🇮',n:'Nicaragua',cap:'Managua',f:'Land van meren en vulkanen.',nl:''},
  CRI:{fl:'🇨🇷',n:'Costa Rica',cap:'San José',f:'«¡Pura vida!» — geen leger.',nl:''},
  PAN:{fl:'🇵🇦',n:'Panamá',cap:'Panamá',f:'Het kanaal verbindt twee oceanen.',nl:''},
  CUB:{fl:'🇨🇺',n:'Cuba',cap:'La Habana',f:'Bakermat van son en salsa.',nl:''},
  DOM:{fl:'🇩🇴',n:'República Dominicana',cap:'Santo Domingo',f:'De oudste stad van Amerika.',nl:''},
  PRI:{fl:'🇵🇷',n:'Puerto Rico',cap:'San Juan',f:'Vrijstaat verbonden met de VS.',nl:''},
  VEN:{fl:'🇻🇪',n:'Venezuela',cap:'Caracas',f:'De Salto Ángel: hoogste waterval ter wereld.',nl:''},
  ECU:{fl:'🇪🇨',n:'Ecuador',cap:'Quito',f:'«La mitad del mundo»: op de evenaar.',nl:''},
  BOL:{fl:'🇧🇴',n:'Bolivia',cap:'Sucre / La Paz',f:'De Salar de Uyuni: grootste zoutvlakte.',nl:''},
  PRY:{fl:'🇵🇾',n:'Paraguay',cap:'Asunción',f:'Tweetalig: español én guaraní.',nl:''},
  URY:{fl:'🇺🇾',n:'Uruguay',cap:'Montevideo',f:'Klein land tussen twee reuzen.',nl:''},
  ARG:{fl:'🇦🇷',n:'Argentina',cap:'Buenos Aires',f:'De tango; vanaf C6 gastheer Mateo (voseo).',nl:''},
  CHL:{fl:'🇨🇱',n:'Chile',cap:'Santiago',f:'Het langste, smalste land ter wereld.',nl:''},
  GNQ:{fl:'🇬🇶',n:'Guinea Ecuatorial',cap:'Malabo',f:'Het enige Spaanstalige land in Afrika.',nl:''},
  USA:{fl:'🇺🇸',n:'Estados Unidos',cap:'Washington D.C.',f:'~60 mln hispanohablantes — geen officiële taal, wél overal aanwezig.',nl:''}
 };
 const wrap=document.getElementById('mapwrap');const svg=wrap.querySelector('svg');const box=document.getElementById('mapinfo');
 if(!svg)return;
 svg.querySelectorAll('path.spa, path.usa').forEach(p=>{p.style.cursor='pointer';
   p.addEventListener('mouseenter',()=>{p.style.opacity='.75'});
   p.addEventListener('mouseleave',()=>{p.style.opacity=''});
   p.addEventListener('click',()=>{const c=p.getAttribute('data-c');const d=INFO[c];if(!d)return;
     box.innerHTML='<h3>'+d.fl+' '+d.n+' <span style="font-size:13px;color:var(--mut);font-weight:400">('+c+')</span>'+(d.star?' ★':'')+'</h3><div class="mrow"><b>Capital:</b> '+d.cap+'</div><div class="mrow">'+d.f+'</div>'+(d.nl?'<div class="gloss">'+d.nl+'</div>':'');
     box.scrollIntoView({behavior:'smooth',block:'nearest'});});
 });
})();

// init
renderFC();renderTable();
// ① receptief
gameEscucha();gameSonido();gameMarcaTilde();gameSombrero();gameVF();
// ② gestuurd productief
gameCompleta();gameDictado();gameOrdenaLetras();gameNumeros();gameEscribeNumero();gameSaludos();gameGenero();
// ③ vrije productie
gameOrden();gamePresentate();
// ④ repaso
gameMemory();
// gramática-viz
gameSilaba();gameTilde();
// hash-navigatie (deep-link naar een paneel)
(function(){const h=location.hash.replace('#','');const i=PANELS.findIndex(p=>p[0]===h);if(i>=0)sn.children[i].click();})();
window.addEventListener('hashchange',()=>{const h=location.hash.replace('#','');const i=PANELS.findIndex(p=>p[0]===h);if(i>=0)sn.children[i].click();});

// ---------- bewerk-in-browser (statische teksten) ----------
(function(){
 var SEL='.hero h1,.hero p,h2.sec,p.lead,.subh,.foot,section .card p,section .card h3,section .card h4,section .card li,#mapinfo';
 var editing=false;
 var eb=document.getElementById('editbar'),txt=document.getElementById('ebtxt'),bE=document.getElementById('ebEdit');
 function setEd(on){document.querySelectorAll(SEL).forEach(function(e){if(on){e.setAttribute('contenteditable','true');e.setAttribute('spellcheck','false');}else{e.removeAttribute('contenteditable');}});}
 bE.onclick=function(){editing=!editing;document.body.classList.toggle('editing',editing);eb.classList.toggle('on',editing);setEd(editing);
   txt.textContent=editing?'✏️ AAN — klik op een titel/tekst en typ':'✏️ «Bewerken» om titels/teksten aan te passen';bE.textContent=editing?'Klaar':'Bewerken';};
 document.getElementById('ebSave').onclick=function(){if(editing)bE.click();
   var clone=document.documentElement.cloneNode(true);var b=clone.querySelector('.editbar');if(b)b.remove();
   var html='<!doctype html>\n'+clone.outerHTML;var blob=new Blob([html],{type:'text/html'});
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='U0_web_mijn_versie.html';a.click();};
})();
"""

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html())
      .replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/U0_web.html","w").write(html)
print("U0_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
