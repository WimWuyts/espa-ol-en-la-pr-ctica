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
sys.path.insert(0,GEN); import cast_gen as C; import vocab_icons as VI; import vocab_emoji as VE
moch=C.mochila("100%","compass")
ICONS=[f'<div class="fcico">{VE.emoji_for(v.get("es",""),v.get("grp",""))}</div>' for v in vocab]

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
.fc .s .fcico{font-size:40px;line-height:1;margin-bottom:2px}
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
/* ---- Lectura: perfiles + V/F met bewijs ---- */
.perfiles{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:640px){.perfiles{grid-template-columns:1fr}}
.perfil{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--g);border-radius:16px;padding:16px}
.perfil h4{font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px}
.perfil .txt{font-size:14px;line-height:1.6}
.perfil .txt .ev{background:#FEF3C7;border-radius:3px;padding:0 3px}
.vftask{margin-top:8px}
.vfrow{display:flex;gap:8px;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line);padding:7px 0;font-size:14px}
.vfrow .btns{display:flex;gap:6px}
.vfrow .vfb{border:1.5px solid var(--line);background:var(--card);color:var(--ink);border-radius:8px;padding:3px 10px;cursor:pointer;font-weight:700}
.vfrow .vfb.on{background:var(--g);color:#fff;border-color:var(--g)}
.vfrow .res{font-size:12px;color:var(--mut);min-width:150px}
/* ---- Hablar: inline recorder ---- */
.rec h3{font-family:var(--disp);margin:0 0 2px;color:var(--ink);font-size:18px}
.rec .desc{color:var(--mut);font-size:13px;margin:0 0 12px}
.rec .target{font-family:var(--disp);font-size:20px;color:var(--gd);background:var(--gt);border-radius:12px;padding:14px 16px;margin:8px 0;text-align:center}
.rec .cue{font-size:12px;color:var(--mut);text-transform:uppercase;letter-spacing:.05em}
.rec .rbtns{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:8px 0}
.rec .rbtn{border:none;border-radius:10px;padding:9px 15px;font-weight:700;cursor:pointer;font-family:var(--disp);font-size:14px;color:#fff;background:var(--g)}
.rec .rbtn.sec{background:var(--gt);color:var(--gd)}
.rec .rbtn.rec-on{background:var(--red);animation:pulse 1s infinite}
.rec .rbtn[disabled]{opacity:.4;cursor:not-allowed}
@keyframes pulse{50%{opacity:.55}}
.rec .moods{display:flex;gap:8px;margin-top:6px}
.rec .mood{font-size:22px;cursor:pointer;border:1.5px solid var(--line);border-radius:10px;padding:2px 10px;background:var(--card)}
.rec .mood.on{border-color:var(--g);background:var(--gt)}
.rec audio{width:100%;margin-top:6px}
/* ---- inline zelfcorrigerende oefeningen ---- */
.exhead{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-bottom:2px}
.exhead h3{font-family:var(--disp);margin:0;color:var(--ink);font-size:18px}
.ex .desc{color:var(--mut);font-size:13px;margin:0 0 10px}
.otra{border:none;background:var(--gt);color:var(--gd);border-radius:8px;padding:6px 12px;font-weight:700;cursor:pointer;font-size:13px;font-family:var(--disp);white-space:nowrap}
.exq{border:1px solid var(--line);border-radius:12px;padding:11px 14px;margin:9px 0;background:var(--card)}
.exq .qz{font-family:var(--disp);font-size:16px;margin-bottom:8px}
.exq .qz .gap{display:inline-block;min-width:60px;border-bottom:2.5px solid var(--g);margin:0 3px;vertical-align:baseline}
.exopts{display:flex;gap:8px;flex-wrap:wrap}
.exopt{border:1.5px solid var(--line);background:var(--card);color:var(--ink);border-radius:10px;padding:7px 13px;cursor:pointer;font-size:15px;font-weight:600;font-family:var(--body)}
.exopt.ok{border-color:var(--g);background:var(--g);color:#fff}
.exopt.no{border-color:var(--red);background:#fde8e8;color:var(--red)}
.exopt[disabled]{cursor:default}
.exwhy{margin-top:8px;font-size:13px;display:none;border-radius:8px;padding:7px 10px}
.exwhy.show{display:block}
.exwhy.g{background:var(--gt);color:var(--gd)}.exwhy.b{background:#fdeaea;color:var(--red)}
.exscore{font-size:13px;color:var(--mut);margin-top:8px}
.exscore b{color:var(--gd)}
.mcol{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:4px}
.mcell{border:1.5px solid var(--line);background:var(--card);color:var(--ink);border-radius:10px;padding:9px 12px;cursor:pointer;font-size:15px;text-align:center;font-weight:600;user-select:none}
.mcell.sel{border-color:var(--g);background:var(--gt)}
.mcell.done{border-color:var(--g);background:var(--g);color:#fff;cursor:default;opacity:.85}
.mcell.bad{border-color:var(--red);background:#fde8e8}
.oslots{display:flex;gap:6px;flex-wrap:wrap;margin:6px 0;min-height:40px}
.oslot{border:1.5px dashed var(--line);border-radius:9px;padding:7px 11px;font-size:14px;min-width:34px;color:var(--mut)}
.oslot.filled{border-style:solid;border-color:var(--g);background:var(--gt);color:var(--ink)}
.obank{display:flex;gap:7px;flex-wrap:wrap;margin-top:6px}
.ochip{border:1.5px solid var(--line);background:var(--card);color:var(--ink);border-radius:10px;padding:8px 13px;cursor:pointer;font-size:15px;font-weight:600}
.ochip.used{opacity:.35;cursor:default}
.ochip.shake{animation:shk .3s}
@keyframes shk{25%{transform:translateX(-4px)}75%{transform:translateX(4px)}}
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
    <p>La página digital de la Unidad 0: flashcards, gramática visual e interactiva, <b>lectura</b>, <b>hablar</b> (grábate) y <b>muchos juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR in het boek brengt je hier om te oefenen — zelfde thema, meer interactie.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U0. Klik om te draaien; wissel ES↔NL; klik 🔊 om te horen. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
    __FC__
    <h2 class="sec">Ejercicios de vocabulario · zelfcorrectie</h2>
    <p class="lead">Oefen de woorden actief: koppelen, invullen, país↔gentilicio en de <b>intruder</b>. Elke oefening geeft directe feedback en je kunt telkens een <b>andere reeks</b> trekken. <span class="gloss">herkennen → onderscheiden → ophalen.</span></p>
    <div class="card ex" id="vx_match"></div>
    <div class="card ex" id="vx_gap"></div>
    <div class="card ex" id="vx_pais"></div>
    <div class="card ex" id="vx_odd"></div>
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
    <h3 class="subh">🔤 El abecedario — letra ↔ nombre</h3>
    <div class="card ex" id="gx_abc"></div>
    <h3 class="subh">🔊 Los sonidos — b/v · h muda · la jota</h3>
    <div class="card ex" id="gx_sonido"></div>
    <h3 class="subh">🎩 El acento — aguda · llana · esdrújula</h3>
    <div class="card ex" id="gx_acento"></div>
    <div class="card ex" id="gx_tilde"></div>
    <h3 class="subh">🔢 Los números — cifra ↔ palabra</h3>
    <div class="card ex" id="gx_num"></div>
    <div class="card ex" id="gx_numorden"></div>
    <h3 class="subh">⚖️ El género — ¿el o la?</h3>
    <div class="card ex" id="gx_genero"></div>
    <h3 class="subh">🎯 Repaso mixto — rellena con feedback</h3>
    <div class="card ex" id="gx_mix"></div>
  </section>

  <section class="panel" data-p="lectura">
    <h2 class="sec">Lectura · el chat de la clase</h2>
    <p class="lead">Lees de <b>vier profielen</b> van de reisgenoten, <b>luister</b> ze (🔊 TTS) en <b>controleer je begrip</b>. Daarna zeg je hoe jij je voorstelt — dat neem je op in het tabblad <b>Hablar</b>. <span class="gloss">Keten: lezen → luisteren → spreken.</span></p>
    <div id="lecturawrap"></div>
    <h3 class="subh">🔢 Ordena</h3>
    <div class="card ex" id="lx_order"></div>
    <h3 class="subh">🔎 Comprensión · escanea y escoge</h3>
    <div class="card ex" id="lx_scan"></div>
  </section>

  <section class="panel" data-p="hablar">
    <h2 class="sec">Hablar · grábate 🎙️</h2>
    <p class="lead">Neem <b>jezelf</b> op: luister naar het model, spreek in, luister terug, en neem opnieuw op. <span class="gloss">Werkt in Chrome/Edge; sta de micro toe. Print blijft bruikbaar zonder opname.</span></p>
    <div class="card" id="rec_saluda"></div>
    <div class="card" id="rec_deletrear"></div>
    <div class="card" id="rec_presenta"></div>
    <p class="lead" style="margin-top:8px">Meer luister-/spreekoefening vind je ook onder <b>Juegos</b> (dictado, escucha) en <b>Gramática</b> (abecedario, tik de tónica).</p>
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
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Los dos besos 💋</h3>
      <p><b>ES:</b> En el mundo hispano, saludar es muy importante. En <b>España</b>, los amigos y la familia suelen darse <b>dos besos</b> (uno en cada mejilla). En muchos países de <b>Latinoamérica</b> se da <b>un solo beso</b>. <span class="gloss">Groeten is belangrijk: in Spanje vaak twee kusjes (één op elke wang), in veel Latijns-Amerikaanse landen één. Tussen mannen meestal een hand of «abrazo».</span></p></div>
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
const PANELS=[['vocab','Vocabulario'],['gram','Gramática'],['lectura','Lectura'],['juegos','Juegos'],['hablar','Hablar 🎙️'],['cultura','Cultura'],['extra','Extra']];
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
   const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "🌎 Símbolo: el águila sobre el nopal, en la bandera", "star": 0, "nl": ""}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "🌎 Símbolo: el sol y «¡hola!» como saludo", "star": 1, "nl": "★ ¡Estás aquí! Parada U0–U4 · Madrid · Sevilla · Barcelona · València"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "🌎 Símbolo: el cóndor y el grano de café", "star": 0, "nl": ""}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "🌎 Símbolo: el sol inca y la llama", "star": 0, "nl": ""}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "🌎 Símbolo: el sol de mayo en la bandera", "star": 0, "nl": ""}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "🌎 Símbolo: las siete estrellas de la bandera", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "🌎 Símbolo: la estrella solitaria de la bandera", "star": 0, "nl": ""}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "🌎 Símbolo: el cóndor de los Andes", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "🌎 Símbolo: el quetzal, ave nacional", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "🌎 Símbolo: la estrella solitaria y la palma real", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "🌎 Símbolo: el cóndor y la bandera wiphala", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "🌎 Símbolo: la única bandera del mundo con una Biblia", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "🌎 Símbolo: las cinco estrellas de Centroamérica", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "🌎 Símbolo: la única bandera distinta por cada lado", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "🌎 Símbolo: el arco iris en el escudo nacional", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "🌎 Símbolo: un volcán en el paisaje nacional", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "🌎 Símbolo: «Pura Vida», saludo y lema del país", "star": 0, "nl": ""}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "🌎 Símbolo: las dos estrellas y el Canal", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "🌎 Símbolo: el sol de mayo, como Argentina", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "🌎 Símbolo: la rana coquí, símbolo de la isla", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "🌎 Símbolo: la única nación hispana de África", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "🌎 Símbolo: la mezcla de banderas hispanas en las calles", "star": 0, "nl": ""}};
 const wrap=document.getElementById('mapwrap');const svg=wrap.querySelector('svg');const box=document.getElementById('mapinfo');
 if(!svg)return;
 svg.querySelectorAll('path.spa, path.usa').forEach(p=>{p.style.cursor='pointer';
   p.addEventListener('mouseenter',()=>{p.style.opacity='.75'});
   p.addEventListener('mouseleave',()=>{p.style.opacity=''});
   p.addEventListener('click',()=>{const c=p.getAttribute('data-c');const d=INFO[c];if(!d)return;
     box.innerHTML='<h3>'+d.fl+' '+d.n+' <span style="font-size:13px;color:var(--mut);font-weight:400">('+c+')</span>'+(d.star?' ★':'')+'</h3>'+'<div class="mrow"><b>🏛️ Capital:</b> '+d.cap+'</div>'+'<div class="mrow"><b>👥 Población:</b> '+d.pob+'</div>'+'<div class="mrow"><b>💰 Moneda:</b> '+d.mon+'</div>'+'<div class="mrow"><b>🗣️ Gentilicio:</b> '+d.gen+'</div>'+'<div class="mrow"><b>🌐 Idioma:</b> '+d.idi+'</div>'+(d.tema?'<div style="margin-top:8px;padding:8px 11px;background:rgba(255,255,255,.7);border-left:4px solid var(--gd);border-radius:7px;font-weight:600;color:var(--gd)">'+d.tema+'</div>':'')+(d.cool?'<div style="margin-top:8px;font-size:13px;line-height:1.5"><b>💡 ¿Sabías que…?</b> '+d.cool+'</div>':'')+(d.nl?'<div class="gloss" style="margin-top:6px">'+d.nl+'</div>':'');
     box.scrollIntoView({behavior:'smooth',block:'nearest'});});
 });
})();

// ================= INLINE ZELFCORRIGERENDE OEFENINGEN (U5-model) =================
function exSample(pool,n){const a=pool.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a.slice(0,Math.min(n,a.length));}
function exEsc(s){return String(s).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
function exFmt(s){return exEsc(s).replace(/___+/g,'<span class="gap">&nbsp;&nbsp;</span>');}
// MEERKEUZE / GAP-FILL: pool item = {q, opts, ans, why}
function exChoice(id,cfg){
 const host=document.getElementById(id);if(!host)return;const per=cfg.per||Math.min(6,cfg.pool.length);
 function render(){const series=exSample(cfg.pool,per);let ok=0;
   host.innerHTML='<div class="exhead"><h3>'+cfg.title+'</h3><button class="otra" type="button">↻ otra serie</button></div><p class="desc">'+cfg.desc+'</p><div class="qlist"></div><div class="exscore">Juist: <b class="ok">0</b>/'+series.length+'</div>';
   host.querySelector('.otra').onclick=render;const list=host.querySelector('.qlist'),scoreEl=host.querySelector('.ok');
   series.forEach(it=>{const q=document.createElement('div');q.className='exq';
     q.innerHTML='<div class="qz">'+exFmt(it.q)+'</div><div class="exopts"></div><div class="exwhy"></div>';
     const opts=q.querySelector('.exopts'),why=q.querySelector('.exwhy');let locked=false;
     exSample(it.opts,it.opts.length).forEach(o=>{const b=document.createElement('button');b.className='exopt';b.type='button';b.textContent=o;
       b.onclick=()=>{if(locked)return;locked=true;const good=o===it.ans;
         opts.querySelectorAll('.exopt').forEach(x=>{x.disabled=true;if(x.textContent===it.ans)x.classList.add('ok');});
         if(good){ok++;scoreEl.textContent=ok;}else{b.classList.add('no');}
         why.className='exwhy show '+(good?'g':'b');why.innerHTML=(good?'✅ ¡correcto! ':'❌ → '+exEsc(it.ans)+'. ')+(it.why?exEsc(it.why):'');};
       opts.appendChild(b);});
     list.appendChild(q);});}
 render();}
// MATCHING: pool item = {a,b}
function exMatch(id,cfg){
 const host=document.getElementById(id);if(!host)return;const per=cfg.per||Math.min(6,cfg.pool.length);
 function render(){const series=exSample(cfg.pool,per);let doneN=0;
   host.innerHTML='<div class="exhead"><h3>'+cfg.title+'</h3><button class="otra" type="button">↻ otra serie</button></div><p class="desc">'+cfg.desc+'</p><div class="mcol"><div class="mL"></div><div class="mR"></div></div><div class="exscore">Emparejados: <b class="ok">0</b>/'+series.length+'</div>';
   host.querySelector('.otra').onclick=render;const L=host.querySelector('.mL'),R=host.querySelector('.mR'),scoreEl=host.querySelector('.ok');
   const right=exSample(series.map((p,i)=>({p,i})),series.length);let selL=null,busy=false;
   series.forEach((p,i)=>{const c=document.createElement('div');c.className='mcell';c.textContent=p.a;c.dataset.i=i;
     c.onclick=()=>{if(busy||c.classList.contains('done'))return;if(selL)selL.classList.remove('sel');selL=c;c.classList.add('sel');};L.appendChild(c);});
   right.forEach(o=>{const c=document.createElement('div');c.className='mcell';c.textContent=o.p.b;c.dataset.i=o.i;
     c.onclick=()=>{if(busy||!selL||c.classList.contains('done'))return;busy=true;const good=selL.dataset.i===c.dataset.i;
       if(good){selL.classList.remove('sel');selL.classList.add('done');c.classList.add('done');doneN++;scoreEl.textContent=doneN;selL=null;busy=false;}
       else{c.classList.add('bad');const s=selL;setTimeout(()=>{c.classList.remove('bad');s.classList.remove('sel');selL=null;busy=false;},600);}};R.appendChild(c);});}
 render();}
// ORDENAR: cfg.rounds=[{sub, items:[{label,key}]}]
function exOrder(id,cfg){
 const host=document.getElementById(id);if(!host)return;let ri=Math.floor(Math.random()*cfg.rounds.length);
 function render(){const round=cfg.rounds[ri];const sorted=round.items.slice().sort((a,b)=>a.key-b.key);let pos=0,mist=0;
   host.innerHTML='<div class="exhead"><h3>'+cfg.title+'</h3><button class="otra" type="button">↻ otra ronda</button></div><p class="desc">'+cfg.desc+' · <b>'+exEsc(round.sub||'')+'</b></p><div class="oslots"></div><div class="obank"></div><div class="exwhy"></div>';
   host.querySelector('.otra').onclick=()=>{ri=(ri+1)%cfg.rounds.length;render();};
   const slots=host.querySelector('.oslots'),bank=host.querySelector('.obank'),why=host.querySelector('.exwhy');
   sorted.forEach((_,i)=>{const s=document.createElement('div');s.className='oslot';s.textContent=(i+1);s.dataset.pos=i;slots.appendChild(s);});
   exSample(round.items,round.items.length).forEach(it=>{const b=document.createElement('button');b.className='ochip';b.type='button';b.textContent=it.label;
     b.onclick=()=>{if(b.classList.contains('used'))return;const exp=sorted[pos];
       if(it.key===exp.key){b.classList.add('used');const sl=slots.querySelector('.oslot[data-pos="'+pos+'"]');sl.classList.add('filled');sl.textContent=(pos+1)+'. '+it.label;pos++;
         if(pos>=sorted.length){why.className='exwhy show '+(mist===0?'g':'b');why.innerHTML=mist===0?'✅ ¡Perfecto! sin errores.':'✔ Completado con '+mist+' error(es). Prueba «otra ronda».';}}
       else{mist++;b.classList.remove('shake');void b.offsetWidth;b.classList.add('shake');why.className='exwhy show b';why.innerHTML='❌ Primero: <b>'+exEsc(exp.label)+'</b>';}};
     bank.appendChild(b);});}
 render();}
// EL INTRUSO: pool item = {words:[...], odd, why}
function exOdd(id,cfg){
 const host=document.getElementById(id);if(!host)return;const per=cfg.per||Math.min(5,cfg.pool.length);
 function render(){const series=exSample(cfg.pool,per);let ok=0;
   host.innerHTML='<div class="exhead"><h3>'+cfg.title+'</h3><button class="otra" type="button">↻ otra serie</button></div><p class="desc">'+cfg.desc+'</p><div class="qlist"></div><div class="exscore">Juist: <b class="ok">0</b>/'+series.length+'</div>';
   host.querySelector('.otra').onclick=render;const list=host.querySelector('.qlist'),scoreEl=host.querySelector('.ok');
   series.forEach(it=>{const q=document.createElement('div');q.className='exq';q.innerHTML='<div class="exopts"></div><div class="exwhy"></div>';
     const opts=q.querySelector('.exopts'),why=q.querySelector('.exwhy');let locked=false;
     exSample(it.words.map((w,i)=>({w,i})),it.words.length).forEach(o=>{const b=document.createElement('button');b.className='exopt';b.type='button';b.textContent=o.w;
       b.onclick=()=>{if(locked)return;locked=true;const good=o.i===it.odd;opts.querySelectorAll('.exopt').forEach(x=>x.disabled=true);
         if(good){ok++;scoreEl.textContent=ok;b.classList.add('ok');}else{b.classList.add('no');opts.querySelectorAll('.exopt').forEach(x=>{if(x.textContent===it.words[it.odd])x.classList.add('ok');});}
         why.className='exwhy show '+(good?'g':'b');why.innerHTML=(good?'✅ ¡bien! ':'❌ → '+exEsc(it.words[it.odd])+'. ')+(it.why?exEsc(it.why):'');};
       opts.appendChild(b);});
     list.appendChild(q);});}
 render();}

function buildInlineExercises(){
 // ---------- VOCABULARIO ----------
 exMatch('vx_match',{title:'Empareja: palabra ↔ símbolo',desc:'Koppel het Spaanse woord aan het juiste beeld.',per:6,pool:[
   {a:'España',b:'🇪🇸'},{a:'México',b:'🇲🇽'},{a:'Colombia',b:'🇨🇴'},{a:'Perú',b:'🇵🇪'},
   {a:'la mochila',b:'🎒'},{a:'el libro',b:'📚'},{a:'el mapa',b:'🗺️'},{a:'¡Hola!',b:'👋'},
   {a:'el mundo',b:'🌍'},{a:'la profesora',b:'👩‍🏫'},{a:'el número',b:'🔢'},{a:'la letra',b:'🔤'},
   {a:'la clase',b:'🏫'},{a:'el lápiz',b:'✏️'}]});
 exChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat in de zin past (saludos & lengua de clase).',per:6,pool:[
   {q:'— ¡Hola! ¿Qué ___? — Bien, gracias.',opts:['tal','día','hola'],ans:'tal',why:'¿Qué tal? = hoe gaat het?'},
   {q:'Por la mañana: «Buenos ___».',opts:['días','noches','tardes'],ans:'días',why:'ochtend → buenos días'},
   {q:'Al llegar la noche: «Buenas ___».',opts:['noches','días','tardes'],ans:'noches',why:'avond/nacht → buenas noches'},
   {q:'Para despedirte: «Hasta ___».',opts:['luego','favor','nada'],ans:'luego',why:'hasta luego = tot straks'},
   {q:'«Muchas gracias.» — «De ___.»',opts:['nada','favor','acuerdo'],ans:'nada',why:'de nada = graag gedaan'},
   {q:'No entiendo. ¿Puedes ___?',opts:['repetir','comer','cantar'],ans:'repetir',why:'kun je herhalen?'},
   {q:'¿Cómo se ___ «mochila» en español?',opts:['dice','come','abre'],ans:'dice',why:'hoe zeg je …?'},
   {q:'¿Puedes ___ tu nombre, letra por letra?',opts:['deletrear','comer','abrir'],ans:'deletrear',why:'deletrear = spellen'},
   {q:'Más ___, por favor (no tan rápido).',opts:['despacio','alto','tarde'],ans:'despacio',why:'más despacio = trager'},
   {q:'Mi ___ es español, del Perú.',opts:['idioma','letra','número'],ans:'idioma',why:'el idioma = de taal'},
   {q:'España, México y Perú están en el ___ hispano.',opts:['mundo','libro','mapa'],ans:'mundo',why:'el mundo hispano'},
   {q:'La palabra «hola» tiene cuatro ___.',opts:['letras','números','mapas'],ans:'letras',why:'la letra = de letter'}]});
 exMatch('vx_pais',{title:'País ↔ gentilicio',desc:'Koppel het land aan de nationaliteit.',per:6,pool:[
   {a:'España',b:'español'},{a:'México',b:'mexicano'},{a:'Colombia',b:'colombiano'},{a:'Perú',b:'peruano'},
   {a:'Argentina',b:'argentino'},{a:'Chile',b:'chileno'},{a:'Cuba',b:'cubano'},{a:'Bélgica',b:'belga'},
   {a:'Venezuela',b:'venezolano'},{a:'Ecuador',b:'ecuatoriano'},{a:'Bolivia',b:'boliviano'},{a:'Guatemala',b:'guatemalteco'}]});
 exOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['¡Hola!','Buenos días','¿Qué tal?','Hasta luego'],odd:3,why:'«Hasta luego» is een afscheid, de rest zijn begroetingen'},
   {words:['España','México','Perú','Bélgica'],odd:3,why:'Bélgica is niet Spaanstalig'},
   {words:['uno','dos','tres','hola'],odd:3,why:'«hola» is geen getal'},
   {words:['a','e','i','m'],odd:3,why:'«m» is geen klinker (vocal)'},
   {words:['español','mexicano','peruano','Colombia'],odd:3,why:'Colombia is een land, niet een gentilicio'},
   {words:['la letra','el número','el idioma','gracias'],odd:3,why:'«gracias» is geen ding maar een uiting'},
   {words:['aguda','llana','esdrújula','tilde'],odd:3,why:'«tilde» is het accent zelf, niet een klemtoontype'},
   {words:['b','v','h','r'],odd:2,why:'«h» is stom (muda); b en v klinken gelijk, r is een aparte klank'}]});
 // ---------- GRAMÁTICA ----------
 exMatch('gx_abc',{title:'El abecedario — letra ↔ nombre',desc:'Koppel de letter aan haar Spaanse naam.',per:6,pool:[
   {a:'h',b:'hache'},{a:'j',b:'jota'},{a:'ñ',b:'eñe'},{a:'ll',b:'elle'},{a:'y',b:'ye'},{a:'v',b:'uve'},
   {a:'w',b:'uve doble'},{a:'z',b:'zeta'},{a:'r',b:'erre'},{a:'q',b:'cu'},{a:'g',b:'ge'},{a:'c',b:'ce'},
   {a:'b',b:'be'},{a:'x',b:'equis'}]});
 exChoice('gx_sonido',{title:'Los sonidos — ¿cómo suena?',desc:'Kies de juiste uitspraakregel.',per:6,pool:[
   {q:'La «h» de «hola» suena…',opts:['no suena (muda)','como la j','como la s'],ans:'no suena (muda)',why:'de h is muda (zwijgt)'},
   {q:'«hola» y «ola» suenan…',opts:['igual','diferente','con j'],ans:'igual',why:'de h zwijgt → identiek'},
   {q:'«b» y «v» en español suenan…',opts:['igual','diferente','como f'],ans:'igual',why:'b en v klinken gelijk'},
   {q:'La «j» de «jamón» suena…',opts:['fuerte, de garganta','como y','muda'],ans:'fuerte, de garganta',why:'jota = harde keelklank'},
   {q:'«gente» — la «g» suena…',opts:['como j','como en «gato»','muda'],ans:'como j',why:'ge/gi klinken als jota'},
   {q:'«gato» — la «g» suena…',opts:['dura (g)','como j','muda'],ans:'dura (g)',why:'ga/go/gu = harde g'},
   {q:'La «ñ» de «niño» suena como…',opts:['nj (Spanje)','n','m'],ans:'nj (Spanje)',why:'ñ ≈ «nj»'},
   {q:'La «z» de «zapato» (España) suena…',opts:['como th (inglés)','como k','como m'],ans:'como th (inglés)',why:'z ≈ zachte th in España'},
   {q:'«ll» de «lluvia» suena parecido a…',opts:['y','l sola','r'],ans:'y',why:'ll ≈ y'},
   {q:'«casa» — la «c» suena…',opts:['como k','como th','como j'],ans:'como k',why:'ca/co/cu = k'},
   {q:'«cine» — la «c» suena…',opts:['como th/s','como k','como j'],ans:'como th/s',why:'ce/ci = zachte c'},
   {q:'La «r» de «rojo» al empezar suena…',opts:['fuerte (rr)','suave','muda'],ans:'fuerte (rr)',why:'r aan het begin = rollende rr'}]});
 exChoice('gx_acento',{title:'El acento — ¿aguda, llana o esdrújula?',desc:'Waar ligt de klemtoon? Kies de familie.',per:6,pool:[
   {q:'«café» es…',opts:['aguda','llana','esdrújula'],ans:'aguda',why:'klemtoon op de laatste lettergreep'},
   {q:'«casa» es…',opts:['llana','aguda','esdrújula'],ans:'llana',why:'klemtoon op de voorlaatste'},
   {q:'«México» es…',opts:['esdrújula','llana','aguda'],ans:'esdrújula',why:'klemtoon op de derde van achteren'},
   {q:'«Perú» es…',opts:['aguda','llana','esdrújula'],ans:'aguda',why:'klemtoon op de laatste'},
   {q:'«árbol» es…',opts:['llana','aguda','esdrújula'],ans:'llana',why:'klemtoon op de voorlaatste'},
   {q:'«teléfono» es…',opts:['esdrújula','llana','aguda'],ans:'esdrújula',why:'derde van achteren'},
   {q:'«lunes» es…',opts:['llana','aguda','esdrújula'],ans:'llana',why:'voorlaatste'},
   {q:'«adiós» es…',opts:['aguda','llana','esdrújula'],ans:'aguda',why:'laatste lettergreep'},
   {q:'«música» es…',opts:['esdrújula','llana','aguda'],ans:'esdrújula',why:'derde van achteren'},
   {q:'«jamón» es…',opts:['aguda','llana','esdrújula'],ans:'aguda',why:'laatste'},
   {q:'«sílaba» es…',opts:['esdrújula','llana','aguda'],ans:'esdrújula',why:'derde van achteren'},
   {q:'«mesa» es…',opts:['llana','aguda','esdrújula'],ans:'llana',why:'voorlaatste'}]});
 exChoice('gx_tilde',{title:'¿Lleva tilde?',desc:'Draagt dit woord een accent (´)? Kies en lees waarom.',per:6,pool:[
   {q:'café',opts:['sí, lleva ´','no lleva'],ans:'sí, lleva ´',why:'aguda die eindigt op klinker → tilde'},
   {q:'casa',opts:['no lleva','sí, lleva ´'],ans:'no lleva',why:'llana op klinker → geen tilde'},
   {q:'México',opts:['sí, lleva ´','no lleva'],ans:'sí, lleva ´',why:'esdrújula → altijd tilde'},
   {q:'árbol',opts:['sí, lleva ´','no lleva'],ans:'sí, lleva ´',why:'llana die eindigt op -l → tilde'},
   {q:'lunes',opts:['no lleva','sí, lleva ´'],ans:'no lleva',why:'llana op -s → geen tilde'},
   {q:'adiós',opts:['sí, lleva ´','no lleva'],ans:'sí, lleva ´',why:'aguda op -s → tilde'},
   {q:'reloj',opts:['no lleva','sí, lleva ´'],ans:'no lleva',why:'aguda op -j → geen tilde'},
   {q:'música',opts:['sí, lleva ´','no lleva'],ans:'sí, lleva ´',why:'esdrújula → altijd tilde'},
   {q:'gente',opts:['no lleva','sí, lleva ´'],ans:'no lleva',why:'llana op klinker → geen tilde'},
   {q:'jamón',opts:['sí, lleva ´','no lleva'],ans:'sí, lleva ´',why:'aguda op -n → tilde'},
   {q:'sílaba',opts:['sí, lleva ´','no lleva'],ans:'sí, lleva ´',why:'esdrújula → altijd tilde'},
   {q:'Madrid',opts:['no lleva','sí, lleva ´'],ans:'no lleva',why:'aguda op -d → geen tilde'}]});
 exChoice('gx_num',{title:'Los números — ¿cómo se escribe?',desc:'Kies de juiste schrijfwijze van het getal.',per:6,pool:[
   {q:'11 =',opts:['once','onze','onse'],ans:'once',why:'11 = once'},
   {q:'15 =',opts:['quince','quinse','cinque'],ans:'quince',why:'15 = quince'},
   {q:'16 =',opts:['dieciséis','diez y seis','dieciseis'],ans:'dieciséis',why:'16–29 = één woord, met tilde'},
   {q:'20 =',opts:['veinte','veynte','viente'],ans:'veinte',why:'20 = veinte'},
   {q:'21 =',opts:['veintiuno','veinte y uno','venteuno'],ans:'veintiuno',why:'21 = veintiuno (één woord)'},
   {q:'30 =',opts:['treinta','treynta','trenta'],ans:'treinta',why:'30 = treinta'},
   {q:'40 =',opts:['cuarenta','cuarenta','carenta'],ans:'cuarenta',why:'40 = cuarenta'},
   {q:'50 =',opts:['cincuenta','cincuenta y','sincuenta'],ans:'cincuenta',why:'50 = cincuenta'},
   {q:'100 =',opts:['cien','ciento','sien'],ans:'cien',why:'100 alleen = cien'},
   {q:'7 =',opts:['siete','sieta','siet'],ans:'siete',why:'7 = siete'},
   {q:'12 =',opts:['doce','dose','doze'],ans:'doce',why:'12 = doce'},
   {q:'33 =',opts:['treinta y tres','treintitrés','treinta tres'],ans:'treinta y tres',why:'31+ = met «y»'}]});
 exOrder('gx_numorden',{title:'Ordena los números',desc:'Tik de getallen in de juiste volgorde (klein → groot).',rounds:[
   {sub:'de 1 a 5',items:[{label:'uno',key:1},{label:'dos',key:2},{label:'tres',key:3},{label:'cuatro',key:4},{label:'cinco',key:5}]},
   {sub:'de menor a mayor',items:[{label:'cero',key:0},{label:'siete',key:7},{label:'doce',key:12},{label:'veinte',key:20},{label:'cincuenta',key:50}]},
   {sub:'decenas',items:[{label:'diez',key:10},{label:'veinte',key:20},{label:'treinta',key:30},{label:'cuarenta',key:40},{label:'cien',key:100}]},
   {sub:'los teens',items:[{label:'once',key:11},{label:'trece',key:13},{label:'quince',key:15},{label:'dieciséis',key:16},{label:'diecinueve',key:19}]}]});
 exChoice('gx_genero',{title:'¿el o la? — el género',desc:'Kies het juiste lidwoord. Let op de valstrikken.',per:6,pool:[
   {q:'___ mapa',opts:['el','la'],ans:'el',why:'el mapa (uitzondering: -a maar masculino)'},
   {q:'___ casa',opts:['la','el'],ans:'la',why:'la casa (v)'},
   {q:'___ problema',opts:['el','la'],ans:'el',why:'el problema (-ma → masculino)'},
   {q:'___ ciudad',opts:['la','el'],ans:'la',why:'la ciudad (-dad → femenino)'},
   {q:'___ día',opts:['el','la'],ans:'el',why:'el día (uitzondering)'},
   {q:'___ mano',opts:['la','el'],ans:'la',why:'la mano (uitzondering: -o maar femenino)'},
   {q:'___ idioma',opts:['el','la'],ans:'el',why:'el idioma (-ma → masculino)'},
   {q:'___ letra',opts:['la','el'],ans:'la',why:'la letra (v)'},
   {q:'___ acento',opts:['el','la'],ans:'el',why:'el acento (m)'},
   {q:'___ sílaba',opts:['la','el'],ans:'la',why:'la sílaba (v)'},
   {q:'___ país',opts:['el','la'],ans:'el',why:'el país (m)'},
   {q:'___ lengua',opts:['la','el'],ans:'la',why:'la lengua (v)'}]});
 exChoice('gx_mix',{title:'Repaso mixto: rellena',desc:'Alles door elkaar: sonidos · acento · números · género · saludos.',per:8,pool:[
   {q:'«teléfono» es…',opts:['esdrújula','llana','aguda'],ans:'esdrújula',why:'derde van achteren'},
   {q:'___ mapa',opts:['el','la'],ans:'el',why:'el mapa'},
   {q:'16 =',opts:['dieciséis','diez y seis','dieciseis'],ans:'dieciséis',why:'één woord met tilde'},
   {q:'«hola» y «ola» suenan…',opts:['igual','diferente','con j'],ans:'igual',why:'de h is muda'},
   {q:'Por la mañana: «Buenos ___».',opts:['días','noches','tardes'],ans:'días',why:'buenos días'},
   {q:'«café» lleva…',opts:['tilde','no tilde'],ans:'tilde',why:'aguda op klinker'},
   {q:'España → gentilicio:',opts:['español','España','espano'],ans:'español',why:'español'},
   {q:'___ ciudad',opts:['la','el'],ans:'la',why:'la ciudad'},
   {q:'«b» y «v» suenan…',opts:['igual','diferente'],ans:'igual',why:'gelijk in het Spaans'},
   {q:'100 =',opts:['cien','ciento','sien'],ans:'cien',why:'cien'},
   {q:'«casa» lleva…',opts:['no tilde','tilde'],ans:'no tilde',why:'llana op klinker'},
   {q:'«Muchas gracias.» — «De ___.»',opts:['nada','favor','acuerdo'],ans:'nada',why:'de nada'}]});
 // ---------- LECTURA ----------
 exOrder('lx_order',{title:'Ordena',desc:'Tik de items in de juiste volgorde.',rounds:[
   {sub:'el abecedario (primeras letras)',items:[{label:'a',key:1},{label:'be',key:2},{label:'ce',key:3},{label:'de',key:4},{label:'e',key:5}]},
   {sub:'los saludos del día',items:[{label:'Buenos días',key:1},{label:'Buenas tardes',key:2},{label:'Buenas noches',key:3}]},
   {sub:'de menor a mayor edad',items:[{label:'trece',key:13},{label:'catorce',key:14},{label:'quince',key:15},{label:'dieciséis',key:16}]},
   {sub:'una conversación',items:[{label:'¡Hola!',key:1},{label:'¿Qué tal?',key:2},{label:'Bien, gracias.',key:3},{label:'Hasta luego.',key:4}]}]});
 exChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in de vier profielen en kies het juiste antwoord.',per:6,pool:[
   {q:'¿De dónde es Lucía?',opts:['de Sevilla (España)','de México','del Perú'],ans:'de Sevilla (España)',why:'«Soy de Sevilla»'},
   {q:'¿Cuántos años tiene Diego?',opts:['15','14','16'],ans:'15',why:'«tengo quince años»'},
   {q:'¿Quién es de Cartagena?',opts:['Valen','Nina','Lucía'],ans:'Valen',why:'«Soy de Cartagena»'},
   {q:'¿De qué país es Nina?',opts:['Perú','Colombia','España'],ans:'Perú',why:'«Soy de Cusco, en el Perú»'},
   {q:'¿Cómo saluda Diego?',opts:['¿Qué onda?','¿Quiubo?','¿Qué tal?'],ans:'¿Qué onda?',why:'saludo mexicano'},
   {q:'¿Quién tiene catorce años?',opts:['Lucía','Diego','Valen'],ans:'Lucía',why:'«tengo catorce años»'},
   {q:'¿Qué gentilicio es Nina?',opts:['peruana','colombiana','española'],ans:'peruana',why:'de Perú → peruana'},
   {q:'¿Con qué saluda Valen (Colombia)?',opts:['¿Quiubo?','¿Qué onda?','Hola, ¿qué tal?'],ans:'¿Quiubo?',why:'saludo colombiano'}]});
}

// ---------- LECTURA: cuatro perfiles + TTS + V/F met bewijs ----------
function renderLectura(){const el=document.getElementById('lecturawrap');if(!el)return;
 const P=[
  {n:'Lucía 🇪🇸',raw:'Hola, me llamo Lucía. Soy de Sevilla, en España. Tengo catorce años. Para saludar digo: «Hola, ¿qué tal?».',
   html:'Hola, me llamo <b>Lucía</b>. Soy de <span class="ev">Sevilla</span>, en España. Tengo <span class="ev">catorce</span> años. Para saludar digo: «<span class="ev">Hola, ¿qué tal?</span>».'},
  {n:'Diego 🇲🇽',raw:'¡Qué onda! Me llamo Diego y soy de la Ciudad de México. Tengo quince años. En México saludamos así: «¿Qué onda?».',
   html:'¡Qué onda! Me llamo <b>Diego</b> y soy de la <span class="ev">Ciudad de México</span>. Tengo <span class="ev">quince</span> años. En México saludamos así: «<span class="ev">¿Qué onda?</span>».'},
  {n:'Valen 🇨🇴',raw:'¡Quiubo! Me llamo Valen. Soy de Cartagena, en Colombia. Tengo quince años. Soy colombiana.',
   html:'¡Quiubo! Me llamo <b>Valen</b>. Soy de <span class="ev">Cartagena</span>, en Colombia. Tengo quince años. Soy <span class="ev">colombiana</span>.'},
  {n:'Nina 🇵🇪',raw:'Hola, soy Nina. Soy de Cusco, en el Perú. Tengo dieciséis años. Soy peruana.',
   html:'Hola, soy <b>Nina</b>. Soy de <span class="ev">Cusco</span>, en el <span class="ev">Perú</span>. Tengo <span class="ev">dieciséis</span> años. Soy <span class="ev">peruana</span>.'}];
 el.innerHTML='<div class="perfiles">'+P.map((m,i)=>'<div class="perfil"><h4>🧳 '+m.n+' '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lp'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div class="txt" id="lp'+i+'" data-raw="'+m.raw.replace(/"/g,'&quot;')+'">'+m.html+'</div></div>').join('')+'</div>';
 const items=[['Lucía es de Sevilla.',true,'«Soy de Sevilla»'],['Diego tiene catorce años.',false,'tiene quince años'],['Nina es del Perú.',true,'«Soy de Cusco, en el Perú»'],['Valen es española.',false,'es colombiana (Cartagena)'],['Diego saluda con «¿Qué onda?».',true,'saludo mexicano'],['Lucía tiene quince años.',false,'tiene catorce años'],['Nina es peruana.',true,'de Perú → peruana'],['Valen es de Cartagena.',true,'«Soy de Cartagena»']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — comprueba tu comprensión (con evidencia)</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">¿Y tú? Preséntate</h3><p class="gloss" style="margin:0 0 8px">Schrijf jouw voorstelzin (naam · woonplaats/land · leeftijd · groet). Neem hem daarna op onder <b>Hablar 🎙️</b> («preséntate»).</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="Hola, me llamo… Soy de… Tengo… años."></textarea>';
 el.appendChild(box);el.appendChild(resp);}

// ---------- INLINE RECORDER (MediaRecorder) ----------
function makeRecorder(elId, cfg){const el=document.getElementById(elId);if(!el)return;
 el.classList.add('rec');
 let idx=0, media=null, chunks=[], stream=null, curURL=null;
 const items=cfg.items;
 el.innerHTML='<h3>'+cfg.title+'</h3><p class="desc">'+cfg.desc+'</p>'+
   '<div class="scorebar"><span>Ítem <b class="pos">1</b>/'+items.length+'</span></div>'+
   '<div class="cue" id="'+elId+'_cue"></div><div class="target" id="'+elId+'_tg"></div>'+
   '<div class="rbtns">'+(TTS?'<button class="rbtn sec" id="'+elId+'_play">🔊 Escuchar</button>':'')+
   '<button class="rbtn" id="'+elId+'_rec">⏺ Grabar</button>'+
   '<button class="rbtn sec" id="'+elId+'_mine" disabled>▶ Mi grabación</button>'+
   '<button class="rbtn sec" id="'+elId+'_next">Siguiente ▸</button></div>'+
   '<div id="'+elId+'_au"></div><div class="moods" id="'+elId+'_mood"></div><div id="'+elId+'_fb" class="fb"></div>';
 const tg=el.querySelector('#'+elId+'_tg'),cue=el.querySelector('#'+elId+'_cue'),pos=el.querySelector('.pos');
 const bRec=el.querySelector('#'+elId+'_rec'),bMine=el.querySelector('#'+elId+'_mine'),bNext=el.querySelector('#'+elId+'_next'),bPlay=el.querySelector('#'+elId+'_play');
 const au=el.querySelector('#'+elId+'_au'),moodbox=el.querySelector('#'+elId+'_mood');
 function load(){const it=items[idx];pos.textContent=idx+1;cue.textContent=it.cue||'';tg.innerHTML=it.text;au.innerHTML='';bMine.disabled=true;moodbox.innerHTML='';el.querySelector('#'+elId+'_fb').className='fb';
   ['☹','😐','☺'].forEach((m,mi)=>{const b=document.createElement('div');b.className='mood';b.textContent=m;b.onclick=()=>{moodbox.querySelectorAll('.mood').forEach(x=>x.classList.remove('on'));b.classList.add('on');feedback(el.querySelector('#'+elId+'_fb'),true,(it.tip||'¡Bien! Prueba otra vez para mejorar.'));};moodbox.appendChild(b);});}
 if(bPlay)bPlay.onclick=()=>speak((items[idx].text||'').replace(/<[^>]+>/g,''));
 bNext.onclick=()=>{idx=(idx+1)%items.length;load();};
 async function start(){
   if(!navigator.mediaDevices||!window.MediaRecorder){warn();return;}
   try{stream=await navigator.mediaDevices.getUserMedia({audio:true});}catch(e){warn();return;}
   chunks=[];media=new MediaRecorder(stream);media.ondataavailable=e=>chunks.push(e.data);
   media.onstop=()=>{const blob=new Blob(chunks,{type:'audio/webm'});if(curURL)URL.revokeObjectURL(curURL);curURL=URL.createObjectURL(blob);
     au.innerHTML='<audio controls src="'+curURL+'"></audio>';bMine.disabled=false;stream.getTracks().forEach(t=>t.stop());};
   media.start();bRec.textContent='⏹ Parar';bRec.classList.add('rec-on');}
 function stop(){if(media&&media.state!=='inactive')media.stop();bRec.textContent='⏺ Grabar';bRec.classList.remove('rec-on');}
 bRec.onclick=()=>{if(media&&media.state==='recording')stop();else start();};
 bMine.onclick=()=>{const a=au.querySelector('audio');if(a)a.play();};
 function warn(){el.querySelector('#'+elId+'_fb').className='fb bad';el.querySelector('#'+elId+'_fb').innerHTML='🎙️ Micrófono no disponible — usa Chrome/Edge y permite el micrófono. Puedes escuchar el modelo (🔊) y practicar en voz alta.';}
 load();}
function buildRecorders(){
 makeRecorder('rec_saluda',{title:'Escucha y repite: saludos',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'Hola, ¿qué tal?',cue:'saludo'},{text:'Buenos días.',cue:'saludo'},{text:'Buenas noches.',cue:'saludo'},{text:'Encantado. / Encantada.',cue:'cortesía'},{text:'Hasta luego.',cue:'despedida'}]});
 makeRecorder('rec_deletrear',{title:'Deletrea — spel je naam',desc:'Zeg de letters van je naam met de Spaanse letternamen (a, be, ce, che…). Neem het op.',items:[
   {text:'Me llamo ___ . Se escribe: ___ , ___ , ___ …',cue:'deletrear tu nombre',tip:'Heb je elke letter met de Spaanse naam gezegd? Herneem.'}]});
 makeRecorder('rec_presenta',{title:'Preséntate — mensaje de voz',desc:'Neem één bericht op: naam · woonplaats/land · leeftijd · een groet.',items:[
   {text:'Hola, me llamo ___ . Soy de ___ . Tengo ___ años. ¡Hasta luego!',cue:'tu presentación',tip:'Naam + herkomst + leeftijd + groet? Neem opnieuw op.'}]});
}

// init
renderFC();renderTable();
buildInlineExercises();renderLectura();buildRecorders();
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
 var SEL='.hero h1,.hero p,h2.sec,p.lead,.subh,.foot,section .card p,section .card h3,section .card h4,section .card li,.perfil h4,#mapinfo';
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
