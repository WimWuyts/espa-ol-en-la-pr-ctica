#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C6+ · U4 «De viaje».
# Eén standalone bestand: fonts base64, de U4-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U4-vocab), visuele/interactieve grammatica (perfecto compuesto · participios · por/para),
# klikbare kaart (mundo hispano, parada 4 = Chile) + TTS + inline recorder + Lectura + editbar. Huisstijl morado.
import json, base64, os, sys
import hub_drills
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
GEN = f"{ROOT}/02-huisstijl/beeld/generators"
sys.path.insert(0, GEN); import cast_gen as C; import vocab_icons as VI; import vocab_emoji as VE
vocab = json.load(open(f"{ROOT}/01-cursussen/06-vervolg/U4/u4_vocab.json", encoding="utf-8"))
mapsvg = open(f"{GEN}/mundo_map_real.svg").read()
moch = C.mochila("100%", "map")
ICONS=[f'<div class="fcico">{VE.emoji_for(v.get("es",""),v.get("grp",""))}</div>' for v in vocab]

def b64(p): return base64.b64encode(open(p, "rb").read()).decode()
def face(fam, path, w):
    return f"@font-face{{font-family:'{fam}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{path}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS = "".join([
 face("Bricolage Grotesque", "BricolageGrotesque-700.woff2", "700"),
 face("Bricolage Grotesque", "BricolageGrotesque-800.woff2", "800"),
 face("Inter", "Inter-400.woff2", "400"), face("Inter", "Inter-600.woff2", "600"),
 face("Caveat", "Caveat-700.woff2", "700"),
])

# ---- de U4-motor-spellen: gegroepeerd (receptief -> productief -> hablar) + base64 ingebed ----
MOTOR = [
 ['① Reconocer · woordenschat', [
   ['viaje-memoria', 'memoria del viaje', 'memory'],
   ['acciones-memoria', 'memoria de acciones', 'memory'],
   ['verbo-participio', 'verbo ↔ participio', 'match']]],
 ['② Distinguir · gramática', [
   ['participio-tipo', '¿regular o irregular?', 'classify'],
   ['por-para', '¿por o para?', 'classify']]],
 ['③ Producir con apoyo', [
   ['perfecto', 'completa: el perfecto', 'cloze'],
   ['por-para-cloze', 'completa: por/para', 'cloze'],
   ['participio-tetris', 'participio: torres', 'tower'],
   ['viaje-order', 'ordena la frase', 'order'],
   ['senala', 'señala', 'point']]],
 ['④ Hablar · grábate 🎙️', [
   ['repite-viaje', 'escucha y repite: mi viaje', 'speak'],
   ['mensaje-viaje', 'mensaje de voz: mi viaje', 'speak']]],
]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-c6plus-u4-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-c6plus-u4-{s}.html")}

CSS = FONTS + """
:root{--g:#7C56A9;--gd:#5B3E83;--gt:#EEE8F5;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E4E3DE;--red:#DC2626;--amber:#B7860B;--card:#fff;
--onder:#2563EB;--ww:#EA7317;--voorw:#1E9E74;--tijd:#7C3AED;--plaats:#14B8A6;
--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif;--hand:'Caveat',cursive}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#171713;--crema:#22221C;--gt:#241A33;--line:#33332B;--card:#20201A}
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
.controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:6px 0 14px}
.controls input,.controls select{border:1.5px solid var(--line);border-radius:10px;padding:8px 12px;font-size:14px;background:var(--card);color:var(--ink)}
.fcgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
.fc{perspective:900px;height:128px;cursor:pointer}
.fc .in{position:relative;width:100%;height:100%;transition:transform .5s;transform-style:preserve-3d}
.fc.flip .in{transform:rotateY(180deg)}
.fc .s,.fc .b{position:absolute;inset:0;backface-visibility:hidden;border-radius:14px;border:1px solid var(--line);background:var(--card);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:10px;text-align:center}
.fc .s{border-top:4px solid var(--g)}
.fc .s .fcico{font-size:40px;line-height:1;margin-bottom:2px}
.fc .b{transform:rotateY(180deg);background:var(--gt);border-top:4px solid var(--gd)}
.fc .w{font-family:var(--disp);font-weight:700;font-size:16px}
.fc .ej{font-size:11px;color:var(--mut);margin-top:6px}
.fc .tr{font-family:var(--disp);font-weight:700;font-size:18px;color:var(--gd)}
.fc .spk{position:absolute;top:6px;right:8px;font-size:14px;opacity:.5}
table.vt{width:100%;border-collapse:collapse;font-size:14px}
table.vt th,table.vt td{border-bottom:1px solid var(--line);padding:8px 10px;text-align:left}
table.vt th{background:var(--gt);color:var(--gd);position:sticky;top:0;z-index:1}
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
.col{border:1.5px dashed var(--line);border-radius:12px;padding:10px;min-height:60px}
.col h4{margin:0 0 8px;font-size:13px;color:var(--gd);text-transform:uppercase;letter-spacing:.04em}
.fb{margin-top:12px;padding:10px 14px;border-radius:10px;font-size:14px;display:none}
.fb.good{display:block;background:var(--gt);color:var(--gd)}
.fb.bad{display:block;background:#fdeaea;color:var(--red)}
.answerbtns{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}
.txin{border:1.5px solid var(--line);border-radius:10px;padding:8px 12px;font-size:16px;background:var(--card);color:var(--ink);font-family:var(--disp);width:120px}
.spk-btn{border:none;background:var(--gt);color:var(--gd);border-radius:10px;padding:9px 16px;font-weight:700;cursor:pointer;font-size:15px}
.csent{font-size:22px;font-family:var(--disp);line-height:2}
.csent span{padding:2px 5px;border-radius:6px;cursor:help;position:relative}
.csent .tip{display:none;position:absolute;left:50%;top:120%;transform:translateX(-50%);background:var(--ink);color:#fff;font-size:12px;font-family:var(--body);padding:5px 9px;border-radius:6px;white-space:nowrap;z-index:5}
.csent span:hover .tip,.csent span:focus .tip{display:block}
.legend{display:flex;gap:10px;flex-wrap:wrap;font-size:12px;margin-top:10px}
.legend i{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:4px;vertical-align:-1px}
.conjgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;margin-top:8px}
.conjcell{border:1.5px solid var(--line);border-radius:12px;padding:10px 12px;background:var(--card);cursor:pointer;text-align:center}
.conjcell .p{font-size:12px;color:var(--mut)}
.conjcell .v{font-family:var(--disp);font-weight:700;font-size:18px;color:var(--gd);margin-top:2px;min-height:22px}
.conjcell.rev{background:var(--gt)}
.foot{color:var(--mut);font-size:12px;text-align:center;margin-top:30px}
#mapwrap svg{width:100%;height:auto}
#mapwrap{max-width:360px;margin:12px auto 0}
#mapwrap path.spa,#mapwrap path.usa{transition:opacity .12s}
.platos{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 2px}
.platos .pl{flex:1 1 130px;background:var(--gt);border-radius:12px;padding:10px 8px;text-align:center}
.platos .pl .em{font-size:24px;line-height:1}
.platos .pl .nm{font-family:var(--disp);color:var(--gd);font-weight:700;font-size:14px;margin-top:2px}
.platos .pl small{color:var(--mut);display:block;font-size:11px}
.mapinfo{margin-top:12px;padding:14px 16px;background:var(--gt);border-radius:12px;min-height:66px}
.mapinfo h3{margin:0 0 6px;font-family:var(--disp);color:var(--gd);font-size:19px}
.mapinfo .mrow{font-size:14px;margin:2px 0}
.modal{display:none;position:fixed;inset:0;background:#0009;z-index:100;padding:16px}
.modal.show{display:flex;align-items:center;justify-content:center}
.modalbox{background:var(--card);border-radius:16px;width:min(940px,97vw);height:min(90vh,940px);display:flex;flex-direction:column;overflow:hidden;box-shadow:0 20px 60px #0006}
.modalbar{display:flex;justify-content:space-between;align-items:center;padding:10px 14px;background:var(--g);color:#fff;font-family:var(--disp);font-weight:700}
.modalbar button{background:#ffffff22;border:none;color:#fff;padding:6px 12px;border-radius:8px;cursor:pointer;font-weight:700;font-family:var(--disp)}
.modal iframe{border:0;flex:1;width:100%;background:#fff}
@media(max-width:600px){.hero h1{font-size:26px}.bar{flex-wrap:wrap}}
.editbar{position:fixed;right:14px;bottom:14px;z-index:9999;display:flex;gap:8px;align-items:center;background:var(--gd);color:#fff;padding:8px 12px;border-radius:12px;box-shadow:0 6px 20px #0004;font-size:13px}
.editbar button{border:none;border-radius:8px;padding:7px 12px;font-weight:700;cursor:pointer;font-family:inherit;font-size:13px}
.editbar .b1{background:#fff;color:var(--gd)}.editbar .b2{background:#ffffff22;color:#fff}.editbar.on{background:var(--amber)}
body.editing [contenteditable=true]{outline:1.4px dashed var(--amber);outline-offset:2px;border-radius:3px}
@media print{.editbar{display:none!important}}
.perfiles{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:640px){.perfiles{grid-template-columns:1fr}}
.perfil{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--g);border-radius:16px;padding:16px}
.perfil h4{font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px}
.perfil .txt{font-size:14px;line-height:1.6}
.perfil .txt .ev{background:#FEF3C7;border-radius:3px;padding:0 3px}
.vftask{margin-top:8px}
.vfrow{display:flex;gap:8px;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line);padding:7px 0;font-size:14px}
.vfrow .btns{display:flex;gap:6px}
.vfrow .vfb{border:1.5px solid var(--line);background:var(--card);border-radius:8px;padding:3px 10px;cursor:pointer;font-weight:700}
.vfrow .vfb.on{background:var(--g);color:#fff;border-color:var(--g)}
.vfrow .res{font-size:12px;color:var(--mut);min-width:150px}
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
.rec .warn{background:#fdeaea;color:var(--red);border-radius:10px;padding:8px 12px;font-size:13px;margin:6px 0}
.rec audio{width:100%;margin-top:6px}
.menucard{border:1px solid var(--line);border-top:4px solid var(--g);border-radius:16px;padding:16px;background:var(--card)}
.menucard h4{font-family:var(--disp);color:var(--gd);margin:0 0 8px}
.menucard .sec2{font-family:var(--disp);font-weight:700;color:var(--ww);font-size:12px;text-transform:uppercase;letter-spacing:.05em;margin:8px 0 2px}
.menucard .mi{display:flex;justify-content:space-between;font-size:14px;padding:3px 0;border-bottom:1px dotted var(--line)}
.menucard .mi .pr{color:var(--gd);font-weight:700}
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

def flashcards_html():
    return """<div class="controls">
      <input id="fcsearch" placeholder="🔎 zoek woord / palabra…" oninput="renderFC()">
      <select id="fcdir" onchange="renderFC()"><option value="es">ES → NL</option><option value="nl">NL → ES</option></select>
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="transporte">transporte</option><option value="alojamiento">alojamiento</option><option value="viaje">verbos del viaje</option><option value="experiencias">experiencias (perfecto)</option><option value="lugares">lugares</option><option value="porpara">por/para</option><option value="opinar">opinar</option><option value="tiempo">marcadores</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Español en la práctica · C6+ U4 De viaje</title>
<style>__CSS__</style></head><body>
<header class="top"><div class="bar">
  <div class="brand">Español en la práctica <small>· la página digital</small></div>
  <div class="tabs">
    <button class="tab" disabled>C4 · Welcome</button>
    <button class="tab" disabled>C5 · A1</button>
    <button class="tab" disabled>C6 · Clean</button>
    <button class="tab active">C6+ · Vervolg</button>
  </div>
  <button class="themebtn" onclick="toggleTheme()" title="licht/donker">◐</button>
</div></header>
<main>
  <div class="hero">
    <div class="mo">__MOCH__</div>
    <div><h1>U4 · De viaje</h1>
    <p>La página digital de la Unidad 4 (<b>de viaje</b>): flashcards, gramática visual e interactiva y <b>12 juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie. Thema's: transporte · perfecto compuesto · participios · por/para.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U4. Klik om te draaien; wissel ES↔NL; filter per groep; klik 🔊 om te horen. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
    __FC__
    <h2 class="sec">Ejercicios de vocabulario · zelfcorrectie</h2>
    <p class="lead">Oefen de woorden actief: koppelen, invullen, definities en de <b>intruder</b>. Elke oefening geeft directe feedback en je kunt telkens een <b>andere reeks</b> trekken. <span class="gloss">herkennen → onderscheiden → ophalen.</span></p>
    <div class="card ex" id="vx_match"></div>
    <div class="card ex" id="vx_gap"></div>
    <div class="card ex" id="vx_def"></div>
    <div class="card ex" id="vx_odd"></div>
    <h2 class="sec">Naslagwerk · zoeken</h2>
    __NAS__
  </section>

  <section class="panel" data-p="gram">
    <h2 class="sec">Gramática visual e interactiva</h2>
    <p class="lead">De <b>essentiële</b> grammatica van U4: het <b>pretérito perfecto compuesto</b> (haber + participio), de <b>participios</b> (regelmatig én onregelmatig) en het contrast <b>por / para</b>. Hier oefen je <b>maximaal</b> — elke oefening trekt uit een grote pool, dus «↻ otra serie» geeft telkens een nieuwe reeks. <span class="gloss">Eerst betekenis/patroon ontdekken, dan de regel.</span></p>
    <div class="card" id="colorsent"></div>
    <div class="card" id="irconj"></div>
    <h2 class="sec" style="margin-top:26px">✅ El perfecto compuesto — máxima práctica</h2>
    <p class="lead">haber (he/has/ha/hemos/habéis/han) + participio (-ado/-ido). 🔴 haber ≠ tener! <span class="gloss">Blijf herspelen tot het automatisch komt.</span></p>
    <div class="game" id="g_cantidad"></div>
    <div class="card ex" id="gx_cantq"></div>
    <div class="card ex" id="gx_reg"></div>
    <div class="card ex" id="gx_adj"></div>
    <h2 class="sec" style="margin-top:26px">⭐ Los participios irregulares</h2>
    <p class="lead">hecho · visto · dicho · vuelto · puesto · escrito · abierto · roto. Uit het hoofd leren. <span class="gloss">He hecho las maletas.</span></p>
    <div class="game" id="g_pron"></div>
    <div class="card ex" id="gx_pronq"></div>
    <div class="card ex" id="gx_ser"></div>
    <div class="card ex" id="gx_build"></div>
    <h2 class="sec" style="margin-top:26px">🎯 Por y para · marcadores — máxima práctica</h2>
    <p class="lead">para = doel/bestemming (para Chile, para descansar) · por = middel/duur/reden (por avión, por dos días). <span class="gloss">+ marcadores: ya, todavía no, nunca, alguna vez.</span></p>
    <div class="card ex" id="gx_iraq"></div>
    <div class="card ex" id="gx_subj"></div>
    <div class="card ex" id="gx_plural"></div>
    <div class="card ex" id="gx_nac"></div>
    <div class="card ex" id="gx_conc"></div>
    <div class="card ex" id="gx_conc2"></div>
    <h3 class="subh">🎯 Repaso mixto — perfecto + participios + por/para</h3>
    <div class="card ex" id="gx_mix"></div>
  </section>

  <section class="panel" data-p="lectura">
    <h2 class="sec">Lectura · dos perfiles</h2>
    <p class="lead">Lees de <b>twee perfielen</b> van de cast (su día y sus gustos), <b>luister</b> ze (🔊 TTS) en <b>controleer je begrip</b>. Daarna reageer je: met wie heb je meer gemeen? <span class="gloss">Keten: lezen → schrijven/spreken.</span></p>
    <div id="lecturawrap"></div>
    <h3 class="subh">🔢 Ordena el día</h3>
    <div class="card ex" id="lx_order"></div>
    <h3 class="subh">🔎 Comprensión · escanea y escoge</h3>
    <div class="card ex" id="lx_scan"></div>
  </section>

  <section class="panel" data-p="juegos">
    <h2 class="sec">Ejercicios · 12 juegos, jij kiest</h2>
    <p class="lead">Geordend van <b>herkennen → onderscheiden → produceren met steun → analyseren &amp; communiceren → hablar</b>. Elk spel geeft directe, verklarende feedback en de steun bouwt af. <span class="gloss">Klik een spel; het opent in een venster en werkt ook offline.</span></p>
    <div id="motorlink"></div>
  </section>

  <section class="panel" data-p="hablar">
    <h2 class="sec">Hablar · grábate 🎙️</h2>
    <p class="lead">Neem <b>jezelf</b> op: luister naar het model, spreek in, luister terug, en neem opnieuw op. <span class="gloss">Werkt in Chrome/Edge; sta de micro toe. Print blijft bruikbaar zonder opname.</span></p>
    <div class="card" id="rec_repite"></div>
    <div class="card" id="rec_pedido"></div>
    <div class="card" id="rec_plato"></div>
    <p class="lead" style="margin-top:8px">Meer spreek-/opnamespellen (preséntate, describe…) vind je ook onder <b>Juegos ④</b>.</p>
  </section>

  <section class="panel" data-p="cultura">
    <h2 class="sec">Cultura · el gran viaje hispano</h2>
    <p class="lead">Parada 4 = <b>Chile</b> 🇨🇱 y el gran viaje. De Spaanstalige wereld staat vol reisiconen: het <b>desierto de Atacama</b>, het <b>Camino de Santiago</b> en de moáis van <b>Rapa Nui</b>. <span class="gloss">Waar ben jij al geweest?</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🏜️ El desierto de Atacama</h3>
      <p>In <b>Chile</b> ligt de <b>droogste woestijn</b> ter wereld. 's Nachts zie je er de helderste sterrenhemel — er staan grote sterrenwachten. <span class="gloss">Nina «ha estado» er.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🥾 El Camino de Santiago</h3>
      <p>In <b>España</b> lopen pelgrims al eeuwen de <b>Camino</b> naar Santiago de Compostela. «He hecho el Camino» is een klassiek reisverhaal — honderden kilometers te voet. <span class="gloss">Lucía kent het.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🗿 Rapa Nui</h3>
      <p><b>Isla de Pascua</b> (Chile), midden in de Stille Oceaan, is beroemd om de <b>moáis</b>: reusachtige stenen beelden. Een van de meest afgelegen bewoonde plekken ter wereld. <span class="gloss">Todavía no he estado allí.</span></p></div>
    <h3 class="subh">📍 La Ruta · el mapa (parada 4 = Chile ★)</h3>
    <p class="lead">Onze halte is <b>Chile</b> (el gran viaje). <b>Klik op een land</b> op de kaart voor info — klik op Chile (★) voor de parada (thema viaje).</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    <h2 class="sec">Extra · bronnen</h2>
    <p class="lead">Externe uitleg &amp; oefeningen (de leerkracht vult de links aan).</p>
    <div class="card"><p>🎬 <b>profedeele</b> (YouTube — el pretérito perfecto / por y para) — <span class="gloss">link volgt.</span></p>
    <p>🧩 <b>arche-ele</b> (Genially — los participios / por vs para) — <span class="gloss">link volgt.</span></p>
    <p>📄 In het boek (PDF) verwijzen de QR-codes naar déze pagina, op het juiste ankerpunt.</p></div>
  </section>

  <div class="foot">Español en la práctica · C6+ · Unidad 4 «De viaje» — página digital. Uitbreiding op de PDF · huisstijl morado · print ↔ PowerPoint ↔ web.</div>
</main>

<div class="modal" id="gmodal"><div class="modalbox">
  <div class="modalbar"><span id="gmtitle">Juego</span><button onclick="closeGame()">✕ sluiten</button></div>
  <iframe id="gframe" title="Spel" allow="microphone; autoplay"></iframe>
</div></div>

<div class="editbar" id="editbar">
  <span id="ebtxt">✏️ «Bewerken» → pas titels & teksten aan · «Bewaar» = eigen versie downloaden</span>
  <button class="b1" id="ebEdit">Bewerken</button>
  <button class="b2" id="ebSave">💾 Bewaar</button>
</div>

<script>__DATA__
__JS__
</script></body></html>"""

JS = r"""
function toggleTheme(){const r=document.documentElement;r.dataset.theme=r.dataset.theme==='dark'?'light':'dark'}
""" + hub_drills.SPEAK_JS + r"""
const TTS=('speechSynthesis'in window);
if(TTS){speechSynthesis.getVoices();speechSynthesis.onvoiceschanged=()=>{};}
const PANELS=[['vocab','Vocabulario'],['gram','Gramática'],['lectura','Lectura'],['juegos','Juegos'],['hablar','Hablar 🎙️'],['cultura','Cultura'],['extra','Extra']];
const sn=document.getElementById('subnav');
PANELS.forEach((p,i)=>{const b=document.createElement('button');b.textContent=p[1];if(i===0)b.classList.add('on');b.onclick=()=>{
  document.querySelectorAll('.subnav button').forEach(x=>x.classList.remove('on'));b.classList.add('on');
  document.querySelectorAll('.panel').forEach(x=>x.classList.remove('show'));
  document.querySelector('.panel[data-p="'+p[0]+'"]').classList.add('show');window.scrollTo({top:0,behavior:'smooth'});};sn.appendChild(b);});

// flashcards
let FCorder=VOCAB.map((_,i)=>i);
function shuffleFC(){for(let i=FCorder.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[FCorder[i],FCorder[j]]=[FCorder[j],FCorder[i]]}renderFC()}
function renderFC(){const q=(document.getElementById('fcsearch').value||'').toLowerCase();const dir=document.getElementById('fcdir').value;const grp=document.getElementById('fcgrp').value;
  const g=document.getElementById('fcgrid');g.innerHTML='';let n=0;
  FCorder.forEach(i=>{const v=VOCAB[i];if(grp&&v.grp!==grp)return;if(q&&!(v.es.toLowerCase().includes(q)||v.nl.toLowerCase().includes(q)))return;n++;
    const front=dir==='es'?v.es:v.nl, back=dir==='es'?v.nl:v.es, ej=dir==='es'?('«'+v.ej+'»'):'';
    const d=document.createElement('div');d.className='fc';d.tabIndex=0;
    d.innerHTML='<div class="in"><div class="s">'+(TTS?'<span class="spk" title="luister">🔊</span>':'')+(ICONS[i]||'')+'<div class="w">'+front+'</div>'+(ej?'<div class="ej">'+ej+'</div>':'')+'</div><div class="b"><div class="tr">'+back+'</div></div></div>';
    d.onclick=()=>d.classList.toggle('flip');d.onkeydown=e=>{if(e.key===' '||e.key==='Enter'){e.preventDefault();d.classList.toggle('flip')}};
    const sp=d.querySelector('.spk');if(sp)sp.onclick=e=>{e.stopPropagation();speak(v.es.replace(/\(.*?\)/g,'').replace(/…/g,'').replace(/\/.*/,''));};
    g.appendChild(d);});
  document.getElementById('fccount').textContent=n+' woorden';}
function renderTable(){const q=(document.getElementById('vsearch').value||'').toLowerCase();const b=document.getElementById('vbody');b.innerHTML='';let n=0;
  VOCAB.forEach(v=>{if(q&&!(v.es.toLowerCase().includes(q)||v.nl.toLowerCase().includes(q)||v.ej.toLowerCase().includes(q)))return;n++;
    const tr=document.createElement('tr');tr.innerHTML='<td><b>'+v.es+'</b></td><td>'+v.nl+'</td><td>'+v.soort+'</td><td class="gloss">'+v.ej+'</td>';b.appendChild(tr);});
  document.getElementById('vcount').textContent=n+' items';}

function scoreBar(id){return '<div class="scorebar" id="'+id+'"><span>Punten: <b class="pt">0</b></span><span>Reeks: <b class="st">0</b></span></div>'}
function setScore(el,pt,st){el.querySelector('.pt').textContent=pt;el.querySelector('.st').textContent=st}
function feedback(el,ok,msg){el.className='fb '+(ok?'good':'bad');el.innerHTML=(ok?'✅ ':'❌ ')+msg}

// ---- GRAMMAR-VIZ 1: kleurgecodeerde perfecto-zin ----
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">El perfecto — haber + participio</h3>'+
'<div class="csent">'+
'<span style="background:#dbeafe;color:#1e40af">(Yo)<span class="tip">onderwerp</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">he<span class="tip">haber (vervoegd)</span></span> '+
'<span style="background:#e9d5ff;color:#6b21a8">viajado<span class="tip">participio — -ado/-ido</span></span> '+
'<span style="background:#dcfce7;color:#166534">a Chile<span class="tip">bestemming</span></span>.</div>'+
'<div class="legend"><span><i style="background:#93c5fd"></i>persoon</span><span><i style="background:#fdba74"></i>haber</span><span><i style="background:#d8b4fe"></i>participio</span><span><i style="background:#86efac"></i>rest</span></span></div>'+
'<p class="gloss" style="margin-top:8px">🟠 <b>haber</b> verandert (he/has/ha…) · het <b>participio</b> blijft gelijk. 🔴 haber ≠ tener! · '+(TTS?'<button class="spk-btn" onclick="speak(\'He viajado a Chile\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: perfecto — klik om te onthullen ----
(function(){const el=document.getElementById('irconj');
 const R=[['yo','he comido'],['tú','has comido'],['él/ella','ha comido'],['nosotros','hemos comido'],['vosotros','habéis comido'],['ellos','han comido']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">el perfecto (comer) — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">Enkel haber verandert (he/has/ha…); het participio (comido) blijft gelijk.</p><div class="conjgrid" id="icg"></div>';
 const g=el.querySelector('#icg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v;if(TTS)speak(p+' '+v);};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: perfecto — ¿qué forma de haber? ----
function gameCantidad(){const el=document.getElementById('g_cantidad');
 const items=[['Yo ___ viajado a Chile.','he','yo → he'],['¿Tú ___ comido?','has','tú → has'],['El avión ___ llegado.','ha','él → ha'],['Nosotros ___ visto el mar.','hemos','nosotros → hemos'],['¿Vosotros ___ reservado?','habéis','vosotros → habéis'],['Ellos ___ llegado hoy.','han','ellos → han'],['Yo ___ hecho las maletas.','he','yo → he'],['Nina ___ subido a la montaña.','ha','ella → ha'],['Mis amigos ___ vuelto.','han','ellos → han'],['(Nosotros) ___ estado en Perú.','hemos','nosotros → hemos'],['¿Tú ___ escrito la postal?','has','tú → has'],['Diego ___ probado la paella.','ha','él → ha']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>el perfecto — ¿qué forma de haber?</h3><p class="desc">he/has/ha/hemos/habéis/han + participio.</p>'+scoreBar('sbC')+'<div id="cW" style="font-size:18px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" id="cC" style="justify-content:center"></div><div class="fb" id="cFb"></div>';
 const sb=el.querySelector('#sbC');const cont=el.querySelector('#cC');
 ['he','has','ha','hemos','habéis','han'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#cW').textContent=el.cur[0];el.querySelector('#cFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#cFb'),ok,(ok?'¡Sí! ':'Nee: '+el.cur[1]+' ')+'('+el.cur[2]+').');setTimeout(next,1000);}
 next();}
// ---- GRAMMAR-VIZ 4: participio — ¿cuál es correcto? ----
function gamePron(){const el=document.getElementById('g_pron');
 const items=[['hacer','hecho'],['ver','visto'],['decir','dicho'],['volver','vuelto'],['poner','puesto'],['escribir','escrito'],['abrir','abierto'],['romper','roto'],['viajar','viajado'],['comer','comido'],['salir','salido'],['dormir','dormido'],['probar','probado'],['subir','subido']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>El participio — ¿cuál es correcto?</h3><p class="desc">Kies het juiste participio (let op de onregelmatige!).</p>'+scoreBar('sbP')+'<div id="pQ" style="font-size:20px;font-family:var(--disp);text-align:center;margin:10px 0"></div><div class="chips" id="pC" style="justify-content:center"></div><div class="fb" id="pFb"></div>';
 const sb=el.querySelector('#sbP');const cont=el.querySelector('#pC');
 function distract(inf,v){var alt1=inf.replace(/ar$/,'ado').replace(/er$/,'ido').replace(/ir$/,'ido');var opts=[v];if(alt1!==v)opts.push(alt1);var pool2=['hecho','visto','dicho','vuelto','puesto','escrito','comido','salido','viajado'];while(opts.length<3){var x=pool2[Math.floor(Math.random()*pool2.length)];if(opts.indexOf(x)<0)opts.push(x);}for(var i=opts.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=opts[i];opts[i]=opts[j];opts[j]=t;}return opts;}
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#pQ').textContent=el.cur[0]+' → he …';cont.innerHTML='';distract(el.cur[0],el.cur[1]).forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});el.querySelector('#pFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#pFb'),ok,(ok?'¡Sí! ':'Nee: ')+el.cur[0]+' → '+el.cur[1]+'.');setTimeout(next,1100);}
 next();}

// ---- MOTOR-ARCADE: 20 spellen, ingebed ----
document.getElementById('motorlink').innerHTML=MOTOR.map(([grp,gs])=>'<div class="subh">'+grp+'</div><div class="fcgrid">'+
   gs.map(([f,t,tpl])=>'<div class="chip" style="display:block;border-radius:14px" onclick="openGame(\''+f+'\',\''+t.replace(/'/g,"")+'\')"><div style="font-weight:700;color:var(--ink);font-size:14px">'+t+'</div><div class="pill" style="margin-top:4px;font-size:10px">'+tpl+'</div></div>').join('')+'</div>').join('');
function openGame(slug,title){const g=GAMES[slug];if(!g){alert('Spel niet gevonden.');return;}
  document.getElementById('gmtitle').textContent=title;document.getElementById('gframe').src='data:text/html;base64,'+g;document.getElementById('gmodal').classList.add('show');}
function closeGame(){document.getElementById('gmodal').classList.remove('show');document.getElementById('gframe').src='about:blank';}
document.getElementById('gmodal').addEventListener('click',e=>{if(e.target.id==='gmodal')closeGame();});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeGame();});

// ---- KAART interactief ----
(function(){
     const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "✈️ Para visitar: Chichén Itzá y las playas de Cancún", "star": 1, "nl": "Parada anterior (U3) · CDMX (Diego)"}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "✈️ Para visitar: la Sagrada Familia y la Alhambra", "star": 1, "nl": "Parada anterior (U0–U1) · el mundo hispano · España (Lucía)"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "✈️ Para visitar: Cartagena y el Eje Cafetero", "star": 1, "nl": "Parada anterior (U2) · Cartagena (Valen)"}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "✈️ Para visitar: Machu Picchu, maravilla del mundo", "star": 0, "nl": ""}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "✈️ Para visitar: las cataratas del Iguazú y la Patagonia", "star": 0, "nl": ""}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "✈️ Para visitar: el Salto Ángel, la cascada más alta", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "✈️ Para visitar: el desierto de Atacama y la isla de Pascua", "star": 1, "nl": "★ ¡Estás aquí! Parada U4 · Chile · el gran viaje (Patagonia, Atacama)"}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "✈️ Para visitar: las islas Galápagos", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "✈️ Para visitar: Tikal, ciudad maya en la selva", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "✈️ Para visitar: La Habana y las playas de Varadero", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "✈️ Para visitar: el Salar de Uyuni", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "✈️ Para visitar: Punta Cana y sus playas", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "✈️ Para visitar: las ruinas mayas de Copán", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "✈️ Para visitar: las misiones jesuíticas", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "✈️ Para visitar: la isla de Ometepe y sus volcanes", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "✈️ Para visitar: la Ruta de las Flores y el surf", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "✈️ Para visitar: los volcanes y los parques nacionales", "star": 0, "nl": ""}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "✈️ Para visitar: el Canal de Panamá", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "✈️ Para visitar: Punta del Este y Colonia del Sacramento", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "✈️ Para visitar: el Viejo San Juan y El Yunque", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "✈️ Para visitar: la isla de Bioko y sus playas", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "✈️ Para visitar: Miami, Los Ángeles y el suroeste hispano", "star": 0, "nl": ""}};
 const wrap=document.getElementById('mapwrap');const svg=wrap.querySelector('svg');const box=document.getElementById('mapinfo');
 if(!svg)return;
 svg.querySelectorAll('path.spa, path.usa').forEach(p=>{p.style.cursor='pointer';
   p.addEventListener('mouseenter',()=>{p.style.opacity='.75'});p.addEventListener('mouseleave',()=>{p.style.opacity=''});
   p.addEventListener('click',()=>{const c=p.getAttribute('data-c');const d=INFO[c];if(!d)return;
     box.innerHTML='<h3>'+d.fl+' '+d.n+' <span style="font-size:13px;color:var(--mut);font-weight:400">('+c+')</span>'+(d.star?' ★':'')+'</h3>'+'<div class="mrow"><b>🏛️ Capital:</b> '+d.cap+'</div>'+'<div class="mrow"><b>👥 Población:</b> '+d.pob+'</div>'+'<div class="mrow"><b>💰 Moneda:</b> '+d.mon+'</div>'+'<div class="mrow"><b>🗣️ Gentilicio:</b> '+d.gen+'</div>'+'<div class="mrow"><b>🌐 Idioma:</b> '+d.idi+'</div>'+(d.tema?'<div style="margin-top:8px;padding:8px 11px;background:rgba(255,255,255,.7);border-left:4px solid var(--gd);border-radius:7px;font-weight:600;color:var(--gd)">'+d.tema+'</div>':'')+(d.cool?'<div style="margin-top:8px;font-size:13px;line-height:1.5"><b>💡 ¿Sabías que…?</b> '+d.cool+'</div>':'')+(d.nl?'<div class="gloss" style="margin-top:6px">'+d.nl+'</div>':'');
     box.scrollIntoView({behavior:'smooth',block:'nearest'});});
 });
})();

// ---------- LECTURA: dos perfiles + TTS + begrip ----------
function renderLectura(){const el=document.getElementById('lecturawrap');if(!el)return;
 const P=[{n:'Nina 🇵🇪',raw:'Este año he viajado a Chile con mi familia. Hemos estado en el desierto de Atacama, el más seco del mundo. He visto un cielo lleno de estrellas, ¡impresionante! También hemos ido al sur, a la Patagonia. Lo mejor ha sido el paisaje. Todavía no he estado en Rapa Nui, pero quiero ir. Ha sido un viaje inolvidable.',
    html:'Este año <span class="ev">he viajado</span> a Chile. <span class="ev">Hemos estado</span> en el desierto de Atacama, el más seco del mundo. <span class="ev">He visto</span> un cielo lleno de estrellas. También <span class="ev">hemos ido</span> a la Patagonia. Lo mejor <span class="ev">ha sido</span> el paisaje. Todavía no <span class="ev">he estado</span> en Rapa Nui, pero quiero ir. Ha sido un viaje <span class="ev">inolvidable</span>.'},
   {n:'Diego 🇲🇽',raw:'Yo he vuelto hace poco de un viaje por Europa. He estado en España y he probado la paella en València. He hecho muchas fotos y he escrito un diario. Lo peor ha sido el vuelo, muy largo, pero ha valido la pena. Nunca he estado tan lejos de casa.',
    html:'Yo <span class="ev">he vuelto</span> hace poco de un viaje por Europa. <span class="ev">He estado</span> en España y <span class="ev">he probado</span> la paella en València. <span class="ev">He hecho</span> muchas fotos y <span class="ev">he escrito</span> un diario. Lo peor <span class="ev">ha sido</span> el vuelo, muy largo. Nunca <span class="ev">he estado</span> tan lejos de casa.'}];
 el.innerHTML='<div class="perfiles">'+P.map((m,i)=>'<div class="perfil"><h4>👤 '+m.n+' '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lm'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div class="txt" id="lm'+i+'" data-raw="'+m.raw.replace(/"/g,'&quot;')+'">'+m.html+'</div></div>').join('')+'</div>';
 const items=[['Nina ha estado en el desierto de Atacama.',true,'«Hemos estado en el desierto de Atacama»'],['Nina ya ha estado en Rapa Nui.',false,'«Todavía no he estado en Rapa Nui»'],['Para Nina, lo mejor ha sido el paisaje.',true,'«Lo mejor ha sido el paisaje»'],['Diego ha probado la paella en València.',true,'«he probado la paella en València»'],['Diego dice que lo peor ha sido el vuelo.',true,'«Lo peor ha sido el vuelo»'],['Diego ha escrito un diario del viaje.',true,'«he escrito un diario»'],['Nina ha viajado sola.',false,'«he viajado a Chile con mi familia»'],['Diego ha viajado por Asia.',false,'«un viaje por Europa»']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — con evidencia</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">¿Y tú? Reacciona</h3><p class="gloss" style="margin:0 0 8px">¿Cuál viaje prefieres? Escribe 2–3 frases con <b>el perfecto</b> sobre un viaje tuyo (o deseado). Grábalo en <b>Hablar 🎙️</b>.</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="Yo he estado en… He visto… Lo mejor ha sido…"></textarea>';
 el.appendChild(box);el.appendChild(resp);}

// ---------- INLINE RECORDER (MediaRecorder) ----------
""" + hub_drills.RECORDER_JS + r"""
function buildRecorders(){
 makeRecorder('rec_repite',{title:'Escucha y repite: mi viaje',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'Este año he viajado a Chile.',cue:'perfecto',tip:'Duidelijk? Probeer nog eens zonder te lezen.'},{text:'He visto el desierto de Atacama.',cue:'perfecto'},{text:'He hecho muchas fotos.',cue:'participio irr.'},{text:'¿Has estado alguna vez en Perú?',cue:'perfecto'},{text:'Viajo por avión para descansar.',cue:'por/para'},{text:'Lo mejor ha sido el paisaje.',cue:'opinión'}]});
 makeRecorder('rec_pedido',{title:'Mensaje de voz: mi viaje',desc:'Neem één bericht op (30–40 s): vertel een reis (gebruik 3× el perfecto).',items:[
   {text:'Cuenta un viaje (usa 3 veces el perfecto: he ido, he visto, he hecho).',cue:'mi viaje',tip:'3× el perfecto (haber + participio)? Neem opnieuw op.'}]});
 makeRecorder('rec_plato',{title:'Mensaje de voz: mi opinión',desc:'Geef je mening over de reis (por/para + lo mejor).',items:[
   {text:'Di cómo has viajado (por/para) y da tu opinión: lo mejor ha sido… porque…',cue:'mi opinión',tip:'por/para + una opinión met «ha sido»? Herneem.'}]});
}

// ================= INLINE ZELFCORRIGERENDE OEFENINGEN =================
""" + hub_drills.HELPERS_JS + r"""

// MEERKEUZE / GAP-FILL: pool item = {q, opts, ans, why}
""" + hub_drills.CHOICE_JS + r"""

// MATCHING: pool item = {a,b}  (b moet uniek zijn)
""" + hub_drills.MATCH_JS + r"""

// ORDENAR: cfg.rounds=[{sub, items:[{label,key}]}]
""" + hub_drills.ORDER_JS + r"""

// EL INTRUSO: pool item = {words:[...], odd, why}
""" + hub_drills.ODD_JS + r"""

// ---- data + calls ----
function buildInlineExercises(){
 // ===== PERFECTO COMPUESTO =====
 buildChoice('gx_cantq',{title:'El perfecto — ¿qué forma?',desc:'haber (he/has/ha…) + participio.',per:8,pool:[
   {q:'(Yo) ___ a Chile.',opts:['he viajado','has viajado','ha viajado'],ans:'he viajado',why:'yo → he'},
   {q:'¿(Tú) ___ ya?',opts:['has comido','he comido','han comido'],ans:'has comido',why:'tú → has'},
   {q:'Nosotros ___ el museo.',opts:['hemos visitado','habéis visitado','han visitado'],ans:'hemos visitado',why:'nosotros → hemos'},
   {q:'El avión ___ tarde.',opts:['ha llegado','han llegado','has llegado'],ans:'ha llegado',why:'él → ha'},
   {q:'Mis amigos ___ un hostal.',opts:['han reservado','ha reservado','habéis reservado'],ans:'han reservado',why:'ellos → han'},
   {q:'¿Vosotros ___ fotos?',opts:['habéis sacado','han sacado','hemos sacado'],ans:'habéis sacado',why:'vosotros → habéis'},
   {q:'(Yo) ___ mal.',opts:['he dormido','has dormido','ha dormido'],ans:'he dormido',why:'yo → he'},
   {q:'Nina ___ a la montaña.',opts:['ha subido','han subido','has subido'],ans:'ha subido',why:'ella → ha'},
   {q:'(Nosotros) ___ en Perú.',opts:['hemos estado','habéis estado','han estado'],ans:'hemos estado',why:'nosotros → hemos'},
   {q:'¿(Tú) ___ el tren?',opts:['has perdido','he perdido','ha perdido'],ans:'has perdido',why:'tú → has'},
   {q:'Ellos ___ hoy.',opts:['han llegado','ha llegado','habéis llegado'],ans:'han llegado',why:'ellos → han'},
   {q:'(Yo) ___ la paella.',opts:['he probado','has probado','ha probado'],ans:'he probado',why:'yo → he'}]});
 buildChoice('gx_reg',{title:'Forma el participio',desc:'Kies het juiste deelwoord (regelmatig én onregelmatig).',per:8,pool:[
   {q:'viajar →',opts:['viajado','viajido','viajido'],ans:'viajado',why:'-ar → -ado'},
   {q:'comer →',opts:['comido','comado','comiendo'],ans:'comido',why:'-er → -ido'},
   {q:'salir →',opts:['salido','salado','salvido'],ans:'salido',why:'-ir → -ido'},
   {q:'hacer →',opts:['hecho','hacido','hacho'],ans:'hecho',why:'irregular'},
   {q:'ver →',opts:['visto','veído','vido'],ans:'visto',why:'irregular'},
   {q:'decir →',opts:['dicho','decido','dijido'],ans:'dicho',why:'irregular'},
   {q:'volver →',opts:['vuelto','volvido','vueltado'],ans:'vuelto',why:'irregular'},
   {q:'poner →',opts:['puesto','ponido','ponesto'],ans:'puesto',why:'irregular'},
   {q:'escribir →',opts:['escrito','escribido','escrivido'],ans:'escrito',why:'irregular'},
   {q:'abrir →',opts:['abierto','abrido','aberto'],ans:'abierto',why:'irregular'},
   {q:'dormir →',opts:['dormido','durmido','dormiendo'],ans:'dormido',why:'-ir → -ido'},
   {q:'romper →',opts:['roto','rompido','rompto'],ans:'roto',why:'irregular'}]});
 buildChoice('gx_adj',{title:'El perfecto — mezclado',desc:'Alles door elkaar (haber + participio). Directe feedback.',per:8,pool:[
   {q:'(Yo) ___ las maletas.',opts:['he hecho','he hacido','tengo hecho'],ans:'he hecho',why:'hacer → hecho'},
   {q:'¿(Tú) ___ el mar?',opts:['has visto','has veído','has vido'],ans:'has visto',why:'ver → visto'},
   {q:'Nosotros ___ del viaje.',opts:['hemos vuelto','hemos volvido','hemos vueltado'],ans:'hemos vuelto',why:'volver → vuelto'},
   {q:'(Yo) ___ una postal.',opts:['he escrito','he escribido','he escrivido'],ans:'he escrito',why:'escribir → escrito'},
   {q:'El guía nos ___ la hora.',opts:['ha dicho','ha decido','ha dijido'],ans:'ha dicho',why:'decir → dicho'},
   {q:'Han ___ el museo.',opts:['abierto','abrido','aberto'],ans:'abierto',why:'abrir → abierto'},
   {q:'El viaje ___ genial.',opts:['ha sido','ha seído','ha estado sido'],ans:'ha sido',why:'ser → sido'},
   {q:'«ik heb gereisd» =',opts:['he viajado','tengo viajado','he viajar'],ans:'he viajado',why:'haber ≠ tener'},
   {q:'(Nosotros) ___ en Chile.',opts:['hemos estado','han estado','habéis estado'],ans:'hemos estado',why:'nosotros → hemos'},
   {q:'(Yo) ___ la paella.',opts:['he probado','he probido','he prueba'],ans:'he probado',why:'probar → probado'}]});
 // ===== PARTICIPIOS =====
 buildChoice('gx_pronq',{title:'Participios irregulares',desc:'Kies het juiste onregelmatige participio.',per:8,pool:[
   {q:'hacer →',opts:['hecho','hacido','hacho'],ans:'hecho',why:'hecho'},
   {q:'ver →',opts:['visto','veído','vido'],ans:'visto',why:'visto'},
   {q:'decir →',opts:['dicho','decido','dijido'],ans:'dicho',why:'dicho'},
   {q:'volver →',opts:['vuelto','volvido','vueltado'],ans:'vuelto',why:'vuelto'},
   {q:'poner →',opts:['puesto','ponido','ponesto'],ans:'puesto',why:'puesto'},
   {q:'escribir →',opts:['escrito','escribido','escrivido'],ans:'escrito',why:'escrito'},
   {q:'abrir →',opts:['abierto','abrido','aberto'],ans:'abierto',why:'abierto'},
   {q:'romper →',opts:['roto','rompido','rompto'],ans:'roto',why:'roto'},
   {q:'descubrir →',opts:['descubierto','descubrido','descuberto'],ans:'descubierto',why:'descubierto'},
   {q:'morir →',opts:['muerto','morido','muerido'],ans:'muerto',why:'muerto'}]});
 buildChoice('gx_ser',{title:'¿participio regular o irregular?',desc:'Kies de correcte vorm.',per:7,pool:[
   {q:'comer →',opts:['comido','comado','comiendo'],ans:'comido',why:'regular -ido'},
   {q:'viajar →',opts:['viajado','viajido','viajando'],ans:'viajado',why:'regular -ado'},
   {q:'leer →',opts:['leído','leido','leyido'],ans:'leído',why:'accent: leído'},
   {q:'oír →',opts:['oído','oido','oyido'],ans:'oído',why:'accent: oído'},
   {q:'hacer →',opts:['hecho','hacido','hacho'],ans:'hecho',why:'irregular'},
   {q:'subir →',opts:['subido','subado','subiendo'],ans:'subido',why:'regular -ido'},
   {q:'poner →',opts:['puesto','ponido','ponesto'],ans:'puesto',why:'irregular'},
   {q:'beber →',opts:['bebido','bebado','bebiendo'],ans:'bebido',why:'regular -ido'}]});
 buildOrder('gx_build',{title:'Ordena la frase',desc:'Tik de woorden in de juiste volgorde.',rounds:[
   {sub:'haber + participio',items:[{label:'Este año',key:1},{label:'he',key:2},{label:'viajado',key:3},{label:'a Chile.',key:4}]},
   {sub:'participio irregular',items:[{label:'(Yo)',key:1},{label:'he',key:2},{label:'visto',key:3},{label:'el mar.',key:4}]},
   {sub:'pregunta con perfecto',items:[{label:'¿Has',key:1},{label:'estado',key:2},{label:'alguna vez',key:3},{label:'en Perú?',key:4}]},
   {sub:'por/para',items:[{label:'Viajo',key:1},{label:'por avión',key:2},{label:'para',key:3},{label:'visitar Chile.',key:4}]},
   {sub:'lo mejor',items:[{label:'Lo mejor',key:1},{label:'ha sido',key:2},{label:'el paisaje',key:3},{label:'de la Patagonia.',key:4}]}]});
 // ===== POR/PARA + MARCADORES =====
 buildChoice('gx_iraq',{title:'¿por o para?',desc:'para = doel/bestemming · por = middel/duur/reden.',per:8,pool:[
   {q:'Salgo ___ Chile mañana.',opts:['para','por','de'],ans:'para',why:'bestemming → para'},
   {q:'Viajo ___ avión.',opts:['por','para','en'],ans:'por',why:'middel → por'},
   {q:'Estudio ___ aprobar.',opts:['para','por','a'],ans:'para',why:'doel → para'},
   {q:'Me quedo ___ una semana.',opts:['por','para','en'],ans:'por',why:'duur → por'},
   {q:'Este billete es ___ ti.',opts:['para','por','de'],ans:'para',why:'ontvanger → para'},
   {q:'Paseamos ___ la costa.',opts:['por','para','en'],ans:'por',why:'doorheen → por'},
   {q:'No viajo ___ el mal tiempo.',opts:['por','para','con'],ans:'por',why:'reden → por'},
   {q:'La reserva es ___ el lunes.',opts:['para','por','en'],ans:'para',why:'deadline → para'},
   {q:'Voy al hotel ___ descansar.',opts:['para','por','a'],ans:'para',why:'om te → para'},
   {q:'Salimos ___ la mañana.',opts:['por','para','en'],ans:'por',why:'deel v.d. dag → por'},
   {q:'Gracias ___ el viaje.',opts:['por','para','de'],ans:'por',why:'reden → por'},
   {q:'El tren sale ___ Barcelona.',opts:['para','por','a'],ans:'para',why:'bestemming → para'}]});
 buildChoice('gx_subj',{title:'Marcadores del perfecto',desc:'ya · todavía no · nunca · alguna vez.',per:7,pool:[
   {q:'___ he hecho las maletas (al).',opts:['Ya','Todavía no','Nunca'],ans:'Ya',why:'al → ya'},
   {q:'___ he estado en Chile (nog niet).',opts:['Todavía no','Ya','Alguna vez'],ans:'Todavía no',why:'nog niet'},
   {q:'___ he montado en barco (nooit).',opts:['Nunca','Ya','Todavía'],ans:'Nunca',why:'nooit'},
   {q:'¿Has viajado ___ a Asia? (ooit)',opts:['alguna vez','ya','nunca'],ans:'alguna vez',why:'ooit'},
   {q:'___ hemos comido, no tengo hambre.',opts:['Ya','Nunca','Todavía no'],ans:'Ya',why:'al gegeten'},
   {q:'___ he visto el mar, quiero ir.',opts:['Todavía no','Ya','Alguna vez'],ans:'Todavía no',why:'nog niet'},
   {q:'¿Has estado ___ en un desierto?',opts:['alguna vez','ya','nunca'],ans:'alguna vez',why:'ooit (vraag)'},
   {q:'___ he probado la comida chilena (nooit).',opts:['Nunca','Ya','Todavía'],ans:'Nunca',why:'nooit'}]});
 buildChoice('gx_plural',{title:'Traduce — por/para y perfecto',desc:'Kies de correcte Spaanse zin.',per:6,pool:[
   {q:'Ik vertrek naar Chile. →',opts:['Salgo para Chile.','Salgo por Chile.','Salgo a Chile.'],ans:'Salgo para Chile.',why:'bestemming → para'},
   {q:'Ik reis per trein. →',opts:['Viajo por tren.','Viajo para tren.','Viajo en para tren.'],ans:'Viajo por tren.',why:'middel → por'},
   {q:'Ik heb gegeten. →',opts:['He comido.','Tengo comido.','He comer.'],ans:'He comido.',why:'haber + participio'},
   {q:'Ik studeer om te reizen. →',opts:['Estudio para viajar.','Estudio por viajar.','Estudio a viajar.'],ans:'Estudio para viajar.',why:'doel → para'},
   {q:'Ik ben nog niet geweest. →',opts:['Todavía no he estado.','Ya he estado.','Nunca estado.'],ans:'Todavía no he estado.',why:'todavía no'},
   {q:'Ik heb het gezien. →',opts:['Lo he visto.','Lo he vido.','Lo tengo visto.'],ans:'Lo he visto.',why:'ver → visto'}]});
 buildChoice('gx_nac',{title:'¿por o para? — usos',desc:'Herken het gebruik.',per:6,pool:[
   {q:'«hoelang» (duur) →',opts:['por','para','en'],ans:'por',why:'duur → por'},
   {q:'«bestemming/waarheen» →',opts:['para','por','a'],ans:'para',why:'bestemming → para'},
   {q:'«om te + inf.» (doel) →',opts:['para','por','a'],ans:'para',why:'doel → para'},
   {q:'«per (avión/tren)» (middel) →',opts:['por','para','en'],ans:'por',why:'middel → por'},
   {q:'«voor jou» (ontvanger) →',opts:['para','por','de'],ans:'para',why:'ontvanger → para'},
   {q:'«door/langs» (doorheen) →',opts:['por','para','en'],ans:'por',why:'doorheen → por'}]});
 buildMatch('gx_conc',{title:'Empareja: infinitivo ↔ participio',desc:'Koppel het werkwoord aan het (onregelmatige) participio.',per:6,pool:[
   {a:'hacer',b:'hecho'},{a:'ver',b:'visto'},{a:'decir',b:'dicho'},{a:'volver',b:'vuelto'},
   {a:'poner',b:'puesto'},{a:'escribir',b:'escrito'},{a:'abrir',b:'abierto'},{a:'romper',b:'roto'}]});
 buildMatch('gx_conc2',{title:'Empareja: pregunta ↔ respuesta',desc:'Koppel de vraag aan het antwoord.',per:6,pool:[
   {a:'¿Has estado en Perú?',b:'Sí, he estado una vez.'},{a:'¿Has visto el mar?',b:'No, todavía no.'},
   {a:'¿Has montado en avión?',b:'No, nunca.'},{a:'¿Ya has comido?',b:'Sí, ya he comido.'},
   {a:'¿Qué tal el viaje?',b:'¡Genial! Ha sido inolvidable.'},{a:'¿Cómo has viajado?',b:'Por avión.'}]});
 buildChoice('gx_mix',{title:'Repaso mixto — perfecto + participios + por/para',desc:'Alles door elkaar. Directe feedback.',per:8,pool:[
   {q:'(Yo) ___ (viajar) a Chile.',opts:['he viajado','he viajar','tengo viajado'],ans:'he viajado',why:'haber + participio'},
   {q:'hacer → participio',opts:['hecho','hacido','hacho'],ans:'hecho',why:'irregular'},
   {q:'Salgo ___ Chile.',opts:['para','por','a'],ans:'para',why:'bestemming'},
   {q:'Viajo ___ avión.',opts:['por','para','en'],ans:'por',why:'middel'},
   {q:'¿(Tú) ___ el mar?',opts:['has visto','has vido','tienes visto'],ans:'has visto',why:'ver → visto'},
   {q:'«nog niet» =',opts:['todavía no','ya','siempre'],ans:'todavía no',why:'marcador'},
   {q:'Nosotros ___ (volver) hoy.',opts:['hemos vuelto','hemos volvido','han vuelto'],ans:'hemos vuelto',why:'volver → vuelto'},
   {q:'Estudio ___ viajar.',opts:['para','por','a'],ans:'para',why:'doel'},
   {q:'ver → participio',opts:['visto','veído','vido'],ans:'visto',why:'irregular'},
   {q:'Me quedo ___ dos días.',opts:['por','para','en'],ans:'por',why:'duur'},
   {q:'«ik heb gedaan» =',opts:['he hecho','tengo hecho','he hacido'],ans:'he hecho',why:'haber + hecho'},
   {q:'El viaje ___ genial.',opts:['ha sido','ha seído','es sido'],ans:'ha sido',why:'ser → sido'}]});
 // ===== VOCABULARIO =====
 buildMatch('vx_match',{title:'Empareja: palabra ↔ emoji',desc:'Koppel het woord aan de emoji.',per:6,pool:[
   {a:'el avión',b:'✈️'},{a:'el tren',b:'🚆'},{a:'la maleta',b:'🧳'},{a:'el hotel',b:'🏨'},
   {a:'la playa',b:'🏖️'},{a:'la montaña',b:'⛰️'},{a:'el museo',b:'🏛️'},{a:'el billete',b:'🎫'},
   {a:'la llave',b:'🔑'},{a:'la foto',b:'📸'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat past.',per:6,pool:[
   {q:'Compro un ___ de ida y vuelta.',opts:['billete','museo','llave'],ans:'billete',why:'ticket = billete'},
   {q:'Reservo una ___ en el hotel.',opts:['habitación','maleta','playa'],ans:'habitación',why:'kamer'},
   {q:'Hago la ___ antes de viajar.',opts:['maleta','reserva','montaña'],ans:'maleta',why:'koffer pakken'},
   {q:'El ___ sale del aeropuerto.',opts:['avión','tren','barco'],ans:'avión',why:'vliegtuig'},
   {q:'En Atacama hay un ___ muy seco.',opts:['desierto','museo','hotel'],ans:'desierto',why:'woestijn'},
   {q:'He ___ muchas fotos del viaje.',opts:['sacado','perdido','reservado'],ans:'sacado',why:'sacar fotos'},
   {q:'Lo mejor ___ sido el paisaje.',opts:['ha','he','han'],ans:'ha',why:'lo mejor → ha'},
   {q:'Viajo ___ avión.',opts:['por','para','en'],ans:'por',why:'middel → por'},
   {q:'El viaje ha sido ___ .',opts:['inolvidable','barato','lejos'],ans:'inolvidable',why:'onvergetelijk'},
   {q:'Todavía no ___ estado en Rapa Nui.',opts:['he','ha','han'],ans:'he',why:'yo → he'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het woord.',per:6,pool:[
   {q:'Het document om te reizen (per trein/vliegtuig):',opts:['el billete','la llave','la reserva'],ans:'el billete',why:'ticket'},
   {q:'De plek waar vliegtuigen vertrekken:',opts:['el aeropuerto','la estación','el hotel'],ans:'el aeropuerto',why:'luchthaven'},
   {q:'Waar je slaapt op reis:',opts:['el hotel','el museo','la playa'],ans:'el hotel',why:'hotel'},
   {q:'«ik ben geweest» (perfecto):',opts:['he estado','estoy','voy a estar'],ans:'he estado',why:'perfecto'},
   {q:'De droogste woestijn ter wereld (Chile):',opts:['Atacama','Patagonia','Rapa Nui'],ans:'Atacama',why:'Atacama'},
   {q:'«om te» / bestemming:',opts:['para','por','de'],ans:'para',why:'para'},
   {q:'«per (avión)» / duur:',opts:['por','para','a'],ans:'por',why:'por'},
   {q:'«onvergetelijk»:',opts:['inolvidable','cansado','barato'],ans:'inolvidable',why:'inolvidable'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['el avión','el tren','el barco','la playa'],odd:3,why:'la playa is geen transport'},
   {words:['el hotel','el hostal','la habitación','el museo'],odd:3,why:'el museo is geen alojamiento'},
   {words:['he estado','he visto','he hecho','tengo'],odd:3,why:'tengo is geen perfecto'},
   {words:['hecho','visto','vuelto','comer'],odd:3,why:'comer is geen participio'},
   {words:['por','para','de','participio'],odd:3,why:'participio hoort niet bij por/para'},
   {words:['ya','todavía no','nunca','avión'],odd:3,why:'avión is geen marcador'},
   {words:['la maleta','el billete','la reserva','la montaña'],odd:3,why:'la montaña is een lugar, geen reisdocument'},
   {words:['impresionante','precioso','inolvidable','tren'],odd:3,why:'tren is geen adjectief'}]});
 // ===== LECTURA =====
 buildOrder('lx_order',{title:'Ordena',desc:'Tik in de juiste volgorde.',rounds:[
   {sub:'el viaje de Nina',items:[{label:'Hemos hecho las maletas,',key:1},{label:'hemos cogido el avión,',key:2},{label:'hemos visitado el desierto',key:3},{label:'y hemos vuelto a casa.',key:4}]},
   {sub:'haber + participio',items:[{label:'Este año',key:1},{label:'he',key:2},{label:'estado',key:3},{label:'en Chile.',key:4}]},
   {sub:'lo mejor',items:[{label:'Lo mejor',key:1},{label:'ha sido',key:2},{label:'el paisaje,',key:3},{label:'impresionante.',key:4}]},
   {sub:'por/para',items:[{label:'He ido',key:1},{label:'por avión',key:2},{label:'para',key:3},{label:'descansar.',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in de twee perfielen (Nina y Diego) en kies.',per:6,pool:[
   {q:'¿Adónde ha viajado Nina?',opts:['a Chile','a España','a Asia'],ans:'a Chile',why:'«he viajado a Chile»'},
   {q:'¿Qué ha visto Nina en Atacama?',opts:['estrellas','el mar','pirámides'],ans:'estrellas',why:'«un cielo lleno de estrellas»'},
   {q:'¿Ya ha estado Nina en Rapa Nui?',opts:['todavía no','sí','no lo dice'],ans:'todavía no',why:'«Todavía no he estado en Rapa Nui»'},
   {q:'¿Dónde ha probado la paella Diego?',opts:['en València','en Cusco','en Chile'],ans:'en València',why:'«he probado la paella en València»'},
   {q:'¿Qué ha sido lo peor para Diego?',opts:['el vuelo','la comida','el hotel'],ans:'el vuelo',why:'«Lo peor ha sido el vuelo»'},
   {q:'¿Qué ha escrito Diego?',opts:['un diario','una carta','un examen'],ans:'un diario',why:'«he escrito un diario»'},
   {q:'Para Nina, el viaje ha sido…',opts:['inolvidable','aburrido','corto'],ans:'inolvidable',why:'«un viaje inolvidable»'},
   {q:'¿Con quién ha viajado Nina?',opts:['con su familia','sola','con amigos'],ans:'con su familia',why:'«con mi familia»'}]});
}
renderFC();renderTable();gameCantidad();gamePron();renderLectura();buildRecorders();buildInlineExercises();
(function(){const h=location.hash.replace('#','');const i=PANELS.findIndex(p=>p[0]===h);if(i>=0)sn.children[i].click();})();
window.addEventListener('hashchange',()=>{const h=location.hash.replace('#','');const i=PANELS.findIndex(p=>p[0]===h);if(i>=0)sn.children[i].click();});

// editbar
(function(){
 var SEL='.hero h1,.hero p,h2.sec,p.lead,.subh,.foot,#mapinfo,section .card p,section .card h3,section .card h4,section .card li,.perfil p,.perfil h3';
 var editing=false;var eb=document.getElementById('editbar'),txt=document.getElementById('ebtxt'),bE=document.getElementById('ebEdit');
 function setEd(on){document.querySelectorAll(SEL).forEach(function(e){if(on){e.setAttribute('contenteditable','true');e.setAttribute('spellcheck','false');}else{e.removeAttribute('contenteditable');}});}
 bE.onclick=function(){editing=!editing;document.body.classList.toggle('editing',editing);eb.classList.toggle('on',editing);setEd(editing);
   txt.textContent=editing?'✏️ AAN — klik op een titel/tekst en typ':'✏️ «Bewerken» → pas titels & teksten aan · «Bewaar» = eigen versie downloaden';bE.textContent=editing?'Klaar':'Bewerken';};
 document.getElementById('ebSave').onclick=function(){if(editing)bE.click();
   var clone=document.documentElement.cloneNode(true);var b=clone.querySelector('.editbar');if(b)b.remove();
   var html='<!doctype html>\n'+clone.outerHTML;var blob=new Blob([html],{type:'text/html'});
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='C6plus_U4_web_mijn_versie.html';a.click();};
})();
"""

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/C6plus_U4_web.html","w").write(html)
print("C6plus_U4_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
