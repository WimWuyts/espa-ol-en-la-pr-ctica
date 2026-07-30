#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C6+ · U5 «Érase una vez».
# Eén standalone bestand: fonts base64, de U4-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U5-vocab), visuele/interactieve grammatica (pretérito indefinido · fuertes · se lo),
# klikbare kaart (mundo hispano, parada 5 = Argentina) + TTS + inline recorder + Lectura + editbar. Huisstijl morado.
import json, base64, os, sys
import hub_drills
import hub_type_sets
import hub_type_gram
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
GEN = f"{ROOT}/02-huisstijl/beeld/generators"
sys.path.insert(0, GEN); import cast_gen as C; import vocab_icons as VI; import vocab_emoji as VE
vocab = json.load(open(f"{ROOT}/01-cursussen/06-vervolg/U5/u5_vocab.json", encoding="utf-8"))
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

# ---- de U5-motor-spellen: gegroepeerd (receptief -> productief -> hablar) + base64 ingebed ----
MOTOR = [
 ['① Reconocer · woordenschat', [
   ['biografia-memoria', 'memoria de la vida', 'memory'],
   ['persona-memoria', 'memoria de oficios', 'memory'],
   ['verbo-indefinido', 'verbo ↔ indefinido', 'match']]],
 ['② Distinguir · gramática', [
   ['indef-tipo', '¿regular o irregular?', 'classify'],
   ['presente-pasado', '¿presente o pasado?', 'classify']]],
 ['③ Producir con apoyo', [
   ['indefinido', 'completa: el indefinido', 'cloze'],
   ['se-lo', 'completa: se lo/se la', 'cloze'],
   ['indef-tetris', 'indefinido: pinball', 'pinball'],
   ['biografia-order', 'ordena la frase', 'order'],
   ['senala', 'señala', 'point']]],
 ['④ Hablar · grábate 🎙️', [
   ['repite-bio', 'escucha y repite: una biografía', 'speak'],
   ['mensaje-bio', 'mensaje de voz: una biografía', 'speak']]],
]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-c6plus-u5-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-c6plus-u5-{s}.html")}

CSS = FONTS + hub_drills.TYPE_CSS + """
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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="biografia">biografía</option><option value="logros">logros</option><option value="persona">oficios</option><option value="indefinido">indefinido (fuertes)</option><option value="tiempo">marcadores</option><option value="odoi">se lo/se la</option><option value="relato">contar</option><option value="opinar">opinar</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Español en la práctica · C6+ U5 Érase una vez</title>
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
    <div><h1>U5 · Érase una vez</h1>
    <p>La página digital de la Unidad 5 (<b>érase una vez</b>): flashcards, gramática visual e interactiva y <b>12 juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie. Thema's: biografía · pretérito indefinido · fuertes · se lo/se la.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U5. Klik om te draaien; wissel ES↔NL; filter per groep; klik 🔊 om te horen. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
    __FC__
    <h2 class="sec">Ejercicios de vocabulario · zelfcorrectie</h2>
    <p class="lead">Oefen de woorden actief: koppelen, invullen, definities en de <b>intruder</b>. Elke oefening geeft directe feedback en je kunt telkens een <b>andere reeks</b> trekken. <span class="gloss">herkennen → onderscheiden → ophalen.</span></p>
    <div class="card ex" id="vx_match"></div>
    <div class="card ex" id="vx_gap"></div>
    <div class="card ex" id="vx_def"></div>
    <div class="card ex" id="vx_odd"></div>
__TYPESLOTS__
    <h2 class="sec">Naslagwerk · zoeken</h2>
    __NAS__
  </section>

  <section class="panel" data-p="gram">
    <h2 class="sec">Gramática visual e interactiva</h2>
    <p class="lead">De <b>essentiële</b> grammatica van U5: het <b>pretérito indefinido</b> (regelmatig + de sterke vormen fue/hizo/tuvo…) en de dubbele voornaamwoorden <b>se lo / se la</b>. Hier oefen je <b>maximaal</b> — elke oefening trekt uit een grote pool, dus «↻ otra serie» geeft telkens een nieuwe reeks. <span class="gloss">Eerst betekenis/patroon ontdekken, dan de regel.</span></p>
    <div class="card" id="colorsent"></div>
    <div class="card" id="irconj"></div>
    <h2 class="sec" style="margin-top:26px">⏳ El indefinido regular — máxima práctica</h2>
    <p class="lead">-ar → é/aste/ó/amos/asteis/aron · -er/-ir → í/iste/ió/imos/isteis/ieron. <span class="gloss">Voor afgeronde feiten in het verleden.</span></p>
    <div class="game" id="g_cantidad"></div>
    <div class="card ex" id="gx_cantq"></div>
    <div class="card ex" id="gx_reg"></div>
    <div class="card ex" id="gx_adj"></div>
    <h2 class="sec" style="margin-top:26px">⭐ Los pretéritos fuertes (irregulares)</h2>
    <p class="lead">ser/ir → fue · hacer → hizo · tener → tuvo · estar → estuvo · decir → dijo · venir → vino · dar → dio. <span class="gloss">Uit het hoofd leren.</span></p>
    <div class="game" id="g_pron"></div>
    <div class="card ex" id="gx_pronq"></div>
    <div class="card ex" id="gx_ser"></div>
    <div class="card ex" id="gx_build"></div>
    <h2 class="sec" style="margin-top:26px">🔁 Se lo / se la · conectores — máxima práctica</h2>
    <p class="lead">le/les + lo/la → <b>se lo / se la</b>. «¿El libro? Se lo di». <span class="gloss">+ conectoren van het verhaal: primero, después, entonces, al final.</span></p>
    <div class="card ex" id="gx_iraq"></div>
    <div class="card ex" id="gx_subj"></div>
    <div class="card ex" id="gx_plural"></div>
    <div class="card ex" id="gx_nac"></div>
    <div class="card ex" id="gx_conc"></div>
    <div class="card ex" id="gx_conc2"></div>
    <h3 class="subh">🎯 Repaso mixto — indefinido + fuertes + se lo</h3>
    <div class="card ex" id="gx_mix"></div>
  __GRAMSLOTS__
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
    <h2 class="sec">Cultura · figuras del mundo hispano</h2>
    <p class="lead">Parada 5 = <b>Buenos Aires</b> 🇦🇷, bij <b>Mateo</b>. De Spaanstalige wereld gaf grote figuren: <b>Gardel</b> (tango), <b>Messi</b> &amp; <b>Maradona</b>, <b>Frida Kahlo</b> en <b>García Márquez</b>. <span class="gloss">Wie bewonder jij?</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🎵 Carlos Gardel</h3>
      <p>De legende van de <b>tango</b>. Hij groeide op in <b>Buenos Aires</b> en werd de stem van het genre. <span class="gloss">Mateo's stad ademt hem nog.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">⚽ Messi y Maradona</h3>
      <p>Twee <b>argentijnse</b> voetbalgoden. Maradona maakte in 1986 het «gol del siglo»; Messi werd in 2022 wereldkampioen. Beiden <b>hicieron historia</b>. <span class="gloss">Trots van Argentinië.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🎨 Frida & García Márquez</h3>
      <p><b>Frida Kahlo</b> (México) schilderde onvergetelijke autorretratos; <b>García Márquez</b> (Colombia) won de <b>Nobelprijs</b> met het «realismo mágico». <span class="gloss">Iconen van de hispanofoon.</span></p></div>
    <h3 class="subh">📍 La Ruta · el mapa (parada 5 = Buenos Aires, Argentina ★)</h3>
    <p class="lead">Onze halte is <b>Argentina</b> (Buenos Aires, Mateo). <b>Klik op een land</b> op de kaart voor info — klik op Argentina (★) voor de parada (thema persona).</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    <h2 class="sec">Extra · bronnen</h2>
    <p class="lead">Externe uitleg &amp; oefeningen (de leerkracht vult de links aan).</p>
    <div class="card"><p>🎬 <b>profedeele</b> (YouTube — el pretérito indefinido / verbos irregulares) — <span class="gloss">link volgt.</span></p>
    <p>🧩 <b>arche-ele</b> (Genially — indefinido / se lo se la) — <span class="gloss">link volgt.</span></p>
    <p>📄 In het boek (PDF) verwijzen de QR-codes naar déze pagina, op het juiste ankerpunt.</p></div>
  </section>

  <div class="foot">Español en la práctica · C6+ · Unidad 5 «Érase una vez» — página digital. Uitbreiding op de PDF · huisstijl morado · print ↔ PowerPoint ↔ web.</div>
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

// ---- GRAMMAR-VIZ 1: kleurgecodeerde indefinido-zin ----
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">El indefinido — hechos del pasado</h3>'+
'<div class="csent">'+
'<span style="background:#dbeafe;color:#1e40af">García Márquez<span class="tip">onderwerp</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">escribió<span class="tip">indefinido — afgerond feit</span></span> '+
'<span style="background:#dcfce7;color:#166534">novelas<span class="tip">voorwerp</span></span> '+
'<span style="background:#e9d5ff;color:#6b21a8">en 1967<span class="tip">marcador: wanneer</span></span>.</div>'+
'<div class="legend"><span><i style="background:#93c5fd"></i>persoon</span><span><i style="background:#fdba74"></i>indefinido</span><span><i style="background:#86efac"></i>voorwerp</span><span><i style="background:#d8b4fe"></i>marcador</span></div>'+
'<p class="gloss" style="margin-top:8px">🟠 De <b>indefinido</b> = afgeronde feiten (en 1967, ayer, el año pasado). Klemtoon op de uitgang: escrib<b>ió</b>. · '+(TTS?'<button class="spk-btn" onclick="speak(\'García Márquez escribió novelas en 1967\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: indefinido — klik om te onthullen ----
(function(){const el=document.getElementById('irconj');
 const R=[['yo','hablé'],['tú','hablaste'],['él/ella','habló'],['nosotros','hablamos'],['vosotros','hablasteis'],['ellos','hablaron']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">el indefinido (hablar) — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">-ar → é/aste/ó/amos/asteis/aron. De klemtoon staat op de uitgang.</p><div class="conjgrid" id="icg"></div>';
 const g=el.querySelector('#icg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v;if(TTS)speak(p+' '+v);};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: indefinido — ¿qué forma? ----
function gameCantidad(){const el=document.getElementById('g_cantidad');
 const items=[['García Márquez ___ (nacer) en 1927.','nació','nacer → nació'],['Frida ___ (pintar) autorretratos.','pintó','pintar → pintó'],['Messi ___ (ganar) el Mundial.','ganó','ganar → ganó'],['Gardel ___ (vivir) en BsAs.','vivió','vivir → vivió'],['(Yo) ___ (estudiar) ayer.','estudié','yo → estudié'],['¿(Tú) ___ (viajar)?','viajaste','tú → viajaste'],['Nosotros ___ (comer) allí.','comimos','nosotros → comimos'],['Ella ___ (escribir) una carta.','escribió','escribir → escribió'],['Ellos ___ (trabajar) mucho.','trabajaron','ellos → trabajaron'],['Él ___ (crecer) en un pueblo.','creció','crecer → creció']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>el indefinido regular — ¿qué forma?</h3><p class="desc">-ar → é/ó · -er/-ir → í/ió.</p>'+scoreBar('sbC')+'<div id="cW" style="font-size:17px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" id="cC" style="justify-content:center"></div><div class="fb" id="cFb"></div>';
 const sb=el.querySelector('#sbC');const cont=el.querySelector('#cC');
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#cW').textContent=el.cur[0];cont.innerHTML='';
   const opts=[el.cur[1]];const alt=el.cur[1].replace(/ó$/,'ío').replace(/é$/,'ó');if(alt!==el.cur[1])opts.push(alt);const p2=['nació','ganó','escribió','vivió','pintó','comió'];while(opts.length<3){const x=p2[Math.floor(Math.random()*p2.length)];if(opts.indexOf(x)<0)opts.push(x);}
   for(let k=opts.length-1;k>0;k--){const j=Math.floor(Math.random()*(k+1));[opts[k],opts[j]]=[opts[j],opts[k]];}
   opts.forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});el.querySelector('#cFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#cFb'),ok,(ok?'¡Sí! ':'Nee: '+el.cur[1]+' ')+'('+el.cur[2]+').');setTimeout(next,1000);}
 next();}
// ---- GRAMMAR-VIZ 4: se lo / se la ----
function gamePron(){const el=document.getElementById('g_pron');
 const items=[['¿El libro a Mateo?','Se lo','el libro → se lo'],['¿La carta a Nina?','Se la','la carta → se la'],['¿Los discos a Diego?','Se los','los discos → se los'],['¿Las fotos a Valen?','Se las','las fotos → se las'],['¿El secreto a ella?','Se lo','el secreto → se lo'],['¿La noticia a él?','Se la','la noticia → se la'],['¿El regalo a tu madre?','Se lo','el regalo → se lo'],['¿Las llaves a él?','Se las','las llaves → se las'],['¿La verdad a ellos?','Se la','les+la → se la'],['¿Los libros a Nina?','Se los','los libros → se los']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>Los pronombres juntos — se lo/se la</h3><p class="desc">le/les + lo/la → se + lo/la (welk OD-deel?).</p>'+scoreBar('sbP')+'<div id="pQ" style="font-size:18px;font-family:var(--disp);text-align:center;margin:10px 0"></div><div class="chips" id="pC" style="justify-content:center"></div><div class="fb" id="pFb"></div>';
 const sb=el.querySelector('#sbP');const cont=el.querySelector('#pC');
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#pQ').textContent=el.cur[0]+' → ___ di.';cont.innerHTML='';['Se lo','Se la','Se los','Se las'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});el.querySelector('#pFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#pFb'),ok,(ok?'¡Sí! ':'Nee: ')+el.cur[1]+' ('+el.cur[2]+').');setTimeout(next,1100);}
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
      const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "⭐ Alguien de aquí: Frida Kahlo, pintora", "star": 1, "nl": "Parada anterior (U3) · CDMX (Diego)"}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "⭐ Alguien de aquí: Rafael Nadal, tenista", "star": 1, "nl": "Parada anterior (U0–U1) · el mundo hispano · España (Lucía)"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "⭐ Alguien de aquí: Shakira, cantante", "star": 1, "nl": "Parada anterior (U2) · Cartagena (Valen)"}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "⭐ Alguien de aquí: Mario Vargas Llosa, Nobel de Literatura", "star": 0, "nl": ""}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "⭐ Alguien de aquí: Lionel Messi, futbolista", "star": 1, "nl": "★ ¡Estás aquí! Parada U5 · Buenos Aires (Mateo · voseo)"}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "⭐ Alguien de aquí: Simón Bolívar, «el Libertador»", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "⭐ Alguien de aquí: Pablo Neruda, poeta Nobel", "star": 1, "nl": "Parada anterior (U4) · Chile · el gran viaje (Patagonia, Atacama)"}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "⭐ Alguien de aquí: Oswaldo Guayasamín, pintor", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "⭐ Alguien de aquí: Rigoberta Menchú, Nobel de la Paz", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "⭐ Alguien de aquí: José Martí, poeta y héroe", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "⭐ Alguien de aquí: Adela Zamudio, poeta y feminista", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "⭐ Alguien de aquí: Juan Luis Guerra, músico", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "⭐ Alguien de aquí: David Suazo, futbolista", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "⭐ Alguien de aquí: José Luis Chilavert, portero legendario", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "⭐ Alguien de aquí: Rubén Darío, poeta", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "⭐ Alguien de aquí: Óscar Romero, arzobispo y santo", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "⭐ Alguien de aquí: Óscar Arias, Nobel de la Paz", "star": 0, "nl": ""}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "⭐ Alguien de aquí: Rubén Blades, músico y actor", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "⭐ Alguien de aquí: Luis Suárez, futbolista", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "⭐ Alguien de aquí: Roberto Clemente, béisbol", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "⭐ Alguien de aquí: Donato Ndongo, escritor", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "⭐ Alguien de aquí: Sonia Sotomayor, jueza", "star": 0, "nl": ""}};
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
 const P=[{n:'Frida Kahlo 🇲🇽',raw:'Frida Kahlo nació en México en 1907. De joven tuvo un accidente grave y, durante su recuperación, empezó a pintar. Pintó muchos autorretratos con colores fuertes. Se casó con el pintor Diego Rivera. Fue una artista única y hoy es un icono. Murió en 1954.',
    html:'Frida Kahlo <span class="ev">nació</span> en México en 1907. De joven <span class="ev">tuvo</span> un accidente grave y <span class="ev">empezó</span> a pintar. <span class="ev">Pintó</span> muchos autorretratos. <span class="ev">Se casó</span> con Diego Rivera. <span class="ev">Fue</span> una artista única. <span class="ev">Murió</span> en 1954.'},
   {n:'Lionel Messi 🇦🇷',raw:'Lionel Messi nació en Rosario, Argentina, en 1987. De niño jugó en un equipo local y luego se mudó a Barcelona. Ganó muchos títulos y en 2022 fue campeón del Mundo. Mucha gente dijo que hizo historia. Para muchos, es el mejor de todos los tiempos.',
    html:'Lionel Messi <span class="ev">nació</span> en Rosario en 1987. De niño <span class="ev">jugó</span> en un equipo local y <span class="ev">se mudó</span> a Barcelona. <span class="ev">Ganó</span> muchos títulos y en 2022 <span class="ev">fue</span> campeón del Mundo. Mucha gente <span class="ev">dijo</span> que <span class="ev">hizo</span> historia.'}];
 el.innerHTML='<div class="perfiles">'+P.map((m,i)=>'<div class="perfil"><h4>👤 '+m.n+' '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lm'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div class="txt" id="lm'+i+'" data-raw="'+m.raw.replace(/"/g,'&quot;')+'">'+m.html+'</div></div>').join('')+'</div>';
 const items=[['Frida empezó a pintar después de un accidente.',true,'«tuvo un accidente… empezó a pintar»'],['Frida se casó con Diego Rivera.',true,'«Se casó con Diego Rivera»'],['Frida murió en 1907.',false,'«Murió en 1954»'],['Messi nació en Buenos Aires.',false,'«nació en Rosario»'],['Messi se mudó a Barcelona.',true,'«se mudó a Barcelona»'],['Messi fue campeón del Mundo en 2022.',true,'«en 2022 fue campeón del Mundo»'],['Frida pintó paisajes, no autorretratos.',false,'«Pintó muchos autorretratos»'],['Mucha gente dijo que Messi hizo historia.',true,'«dijo que hizo historia»']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — con evidencia</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">¿Y tú? Reacciona</h3><p class="gloss" style="margin:0 0 8px">¿A quién admiras más? Escribe 2–3 frases con <b>el indefinido</b> y una mini-opinión (creo que fue… porque…). Grábalo en <b>Hablar 🎙️</b>.</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="Admiro a… Nació en… Creo que fue… porque…"></textarea>';
 el.appendChild(box);el.appendChild(resp);}

// ---------- INLINE RECORDER (MediaRecorder) ----------
""" + hub_drills.RECORDER_JS + r"""
function buildRecorders(){
 makeRecorder('rec_repite',{title:'Escucha y repite: una biografía',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'Nació en Argentina en 1987.',cue:'indefinido',tip:'Duidelijk? Probeer nog eens zonder te lezen.'},{text:'De joven jugó en un equipo local.',cue:'indefinido'},{text:'Ganó muchos títulos.',cue:'indefinido'},{text:'En 2022 fue campeón del Mundo.',cue:'fuerte'},{text:'El libro se lo di a Mateo.',cue:'se lo'},{text:'Creo que fue un genio.',cue:'opinión'}]});
 makeRecorder('rec_pedido',{title:'Mensaje de voz: una biografía',desc:'Neem één bericht op (30–40 s): vertel een biografie (gebruik 3× el indefinido).',items:[
   {text:'Cuenta la vida de una persona famosa (usa 3 veces el indefinido: nació, hizo/ganó, escribió).',cue:'una biografía',tip:'3× el indefinido (afgeronde feiten)? Neem opnieuw op.'}]});
 makeRecorder('rec_plato',{title:'Mensaje de voz: mi opinión',desc:'Geef je mening over de figuur (creo que fue…).',items:[
   {text:'Usa conectores (primero, después, al final) y da tu opinión: creo que fue… porque…',cue:'mi opinión',tip:'conectoren + una opinión met «fue»? Herneem.'}]});
}

// ================= INLINE ZELFCORRIGERENDE OEFENINGEN =================
""" + hub_drills.HELPERS_JS + hub_drills.TYPE_JS + r"""

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
 // ===== INDEFINIDO REGULAR =====
 buildChoice('gx_cantq',{title:'El indefinido regular — ¿qué forma?',desc:'-ar → é/ó · -er/-ir → í/ió.',per:8,pool:[
   {q:'García Márquez ___ (nacer) en 1927.',opts:['nació','nacío','naceó'],ans:'nació',why:'nacer → nació'},
   {q:'___ (escribir, él) novelas.',opts:['escribió','escribó','escrivió'],ans:'escribió',why:'escribir → escribió'},
   {q:'Frida ___ (pintar) autorretratos.',opts:['pintó','pintió','pintaba'],ans:'pintó',why:'pintar → pintó'},
   {q:'Messi ___ (ganar) el Mundial.',opts:['ganó','ganió','gané'],ans:'ganó',why:'ganar → ganó'},
   {q:'(Yo) ___ (estudiar) ayer.',opts:['estudié','estudó','estudí'],ans:'estudié',why:'yo → estudié'},
   {q:'Nosotros ___ (comer) en el centro.',opts:['comimos','comemos','comió'],ans:'comimos',why:'nosotros → comimos'},
   {q:'Gardel ___ (vivir) en BsAs.',opts:['vivió','vivó','vivía'],ans:'vivió',why:'vivir → vivió'},
   {q:'¿(Tú) ___ (viajar) el año pasado?',opts:['viajaste','viajastes','viajó'],ans:'viajaste',why:'tú → viajaste'},
   {q:'Ella ___ (crecer) en un pueblo.',opts:['creció','crecío','creceó'],ans:'creció',why:'crecer → creció'},
   {q:'Ellos ___ (trabajar) mucho.',opts:['trabajaron','trabajoron','trabajieron'],ans:'trabajaron',why:'ellos → trabajaron'},
   {q:'(Yo) ___ (escribir) una carta.',opts:['escribí','escribié','escribó'],ans:'escribí',why:'yo → escribí'},
   {q:'El artista ___ (crear) un personaje.',opts:['creó','crió','creyó'],ans:'creó',why:'crear → creó'}]});
 buildChoice('gx_reg',{title:'¿presente o indefinido?',desc:'Kies de vorm die past bij de marker.',per:8,pool:[
   {q:'Ayer (yo) ___ mucho.',opts:['estudié','estudio','estudiaré'],ans:'estudié',why:'ayer → indefinido'},
   {q:'Hoy (yo) ___ en casa.',opts:['estudio','estudié','estudiar'],ans:'estudio',why:'hoy → presente'},
   {q:'En 1927 ___ (él) en Colombia.',opts:['nació','nace','nacerá'],ans:'nació',why:'en 1927 → indefinido'},
   {q:'Normalmente (él) ___ novelas.',opts:['escribe','escribió','escribir'],ans:'escribe',why:'normalmente → presente'},
   {q:'En 2022 Messi ___ campeón.',opts:['fue','es','será'],ans:'fue',why:'en 2022 → indefinido'},
   {q:'Ahora (él) ___ en Miami.',opts:['juega','jugó','jugará'],ans:'juega',why:'ahora → presente'},
   {q:'El año pasado (yo) ___ a Perú.',opts:['viajé','viajo','viajaré'],ans:'viajé',why:'año pasado → indefinido'},
   {q:'Cada día ella ___ deporte.',opts:['hace','hizo','hará'],ans:'hace',why:'cada día → presente'},
   {q:'De repente, todo ___.',opts:['cambió','cambia','cambiará'],ans:'cambió',why:'de repente → indefinido'},
   {q:'Hace dos años (yo) me ___.',opts:['mudé','mudo','mudaré'],ans:'mudé',why:'hace dos años → indefinido'}]});
 buildChoice('gx_adj',{title:'El indefinido — mezclado',desc:'Alles door elkaar. Directe feedback.',per:8,pool:[
   {q:'(Yo) ___ (estudiar) medicina.',opts:['estudié','estudó','estudiaba'],ans:'estudié',why:'yo → estudié'},
   {q:'Ella ___ (casarse) joven.',opts:['se casó','se casé','se casaba'],ans:'se casó',why:'casarse → se casó'},
   {q:'Nosotros ___ (vivir) allí.',opts:['vivimos','vivíamos','vivieron'],ans:'vivimos',why:'nosotros → vivimos'},
   {q:'¿(Tú) ___ (ganar) el premio?',opts:['ganaste','ganastes','ganó'],ans:'ganaste',why:'tú → ganaste'},
   {q:'El escritor ___ (morir) en 2014.',opts:['murió','morió','moría'],ans:'murió',why:'morir → murió (o→u)'},
   {q:'Ellos ___ (escribir) un libro.',opts:['escribieron','escribiron','escribían'],ans:'escribieron',why:'ellos → escribieron'},
   {q:'(Yo) ___ (nacer) en Bélgica.',opts:['nací','nacé','nacío'],ans:'nací',why:'yo → nací'},
   {q:'El pintor ___ (crear) su obra.',opts:['creó','crió','creaba'],ans:'creó',why:'crear → creó'},
   {q:'Nosotros ___ (estudiar) juntos.',opts:['estudiamos','estudiábamos','estudiaron'],ans:'estudiamos',why:'nosotros → estudiamos'},
   {q:'Ella ___ (componer) canciones.',opts:['compuso','componió','componía'],ans:'compuso',why:'componer → compuso (fuerte)'}]});
 // ===== FUERTES =====
 buildChoice('gx_pronq',{title:'Los pretéritos fuertes',desc:'Kies de sterke vorm (él/ella).',per:8,pool:[
   {q:'ser/ir → él',opts:['fue','fui','fué'],ans:'fue',why:'fue'},
   {q:'hacer → él',opts:['hizo','hació','hizió'],ans:'hizo',why:'hizo (z)'},
   {q:'tener → él',opts:['tuvo','tenió','tuvió'],ans:'tuvo',why:'tuvo'},
   {q:'estar → él',opts:['estuvo','estó','estuvió'],ans:'estuvo',why:'estuvo'},
   {q:'decir → él',opts:['dijo','dició','dijió'],ans:'dijo',why:'dijo'},
   {q:'venir → él',opts:['vino','venió','vinió'],ans:'vino',why:'vino'},
   {q:'dar → él',opts:['dio','dió','daba'],ans:'dio',why:'dio'},
   {q:'poder → él',opts:['pudo','podió','pudió'],ans:'pudo',why:'pudo'},
   {q:'ver → él',opts:['vio','vió','veyó'],ans:'vio',why:'vio'},
   {q:'poner → él',opts:['puso','ponió','pusió'],ans:'puso',why:'puso'}]});
 buildChoice('gx_ser',{title:'Fuertes en contexto',desc:'Vul de sterke indefinido in.',per:7,pool:[
   {q:'Evita ___ muy importante.',opts:['fue','fui','era'],ans:'fue',why:'ser → fue'},
   {q:'Maradona ___ el «gol del siglo».',opts:['hizo','hació','hacía'],ans:'hizo',why:'hacer → hizo'},
   {q:'(Yo) ___ un buen día.',opts:['tuve','tení','tenía'],ans:'tuve',why:'tener → tuve'},
   {q:'Gardel ___ a París.',opts:['fue','fui','iba'],ans:'fue',why:'ir → fue'},
   {q:'El equipo ___ en la final.',opts:['estuvo','estó','estaba'],ans:'estuvo',why:'estar → estuvo'},
   {q:'Ella me ___ un regalo.',opts:['dio','dió','daba'],ans:'dio',why:'dar → dio'},
   {q:'El líder ___ la verdad.',opts:['dijo','dició','decía'],ans:'dijo',why:'decir → dijo'},
   {q:'(Yo) ___ a la ciudad.',opts:['vine','viné','venía'],ans:'vine',why:'venir → vine'}]});
 buildOrder('gx_build',{title:'Ordena la frase',desc:'Tik de woorden in de juiste volgorde.',rounds:[
   {sub:'biografía',items:[{label:'García Márquez',key:1},{label:'nació',key:2},{label:'en Colombia',key:3},{label:'en 1927.',key:4}]},
   {sub:'forma fuerte',items:[{label:'Messi',key:1},{label:'fue',key:2},{label:'campeón',key:3},{label:'del Mundo.',key:4}]},
   {sub:'se lo',items:[{label:'El libro,',key:1},{label:'se lo',key:2},{label:'di',key:3},{label:'a Mateo.',key:4}]},
   {sub:'conectores',items:[{label:'Primero estudió,',key:1},{label:'después escribió,',key:2},{label:'entonces triunfó',key:3},{label:'y al final murió famoso.',key:4}]},
   {sub:'se las',items:[{label:'Las fotos,',key:1},{label:'se las',key:2},{label:'mandé',key:3},{label:'a Nina.',key:4}]}]});
 // ===== SE LO + CONECTORES + TRADUCE =====
 buildChoice('gx_iraq',{title:'Se lo / se la',desc:'le/les + lo/la → se + lo/la. Kies het OD-deel.',per:8,pool:[
   {q:'¿El libro a Mateo? — ___ di.',opts:['Se lo','Le lo','Se la'],ans:'Se lo',why:'el libro → se lo'},
   {q:'¿La carta a Nina? — ___ mandé.',opts:['Se la','Le la','Se lo'],ans:'Se la',why:'la carta → se la'},
   {q:'¿Los discos a Diego? — ___ presté.',opts:['Se los','Le los','Se las'],ans:'Se los',why:'los discos → se los'},
   {q:'¿Las fotos a Valen? — ___ enseñé.',opts:['Se las','Le las','Se los'],ans:'Se las',why:'las fotos → se las'},
   {q:'¿El secreto a ella? — ___ conté.',opts:['Se lo','Le lo','Se la'],ans:'Se lo',why:'el secreto → se lo'},
   {q:'¿La noticia a él? — ___ dije.',opts:['Se la','Le la','Se lo'],ans:'Se la',why:'la noticia → se la'},
   {q:'¿El regalo a tu madre? — ___ di.',opts:['Se lo','Le lo','Se la'],ans:'Se lo',why:'el regalo → se lo'},
   {q:'¿Las llaves a él? — ___ dejé.',opts:['Se las','Le las','Se los'],ans:'Se las',why:'las llaves → se las'},
   {q:'¿La verdad a ellos? — ___ conté.',opts:['Se la','Les la','Se lo'],ans:'Se la',why:'les+la → se la'},
   {q:'¿El vídeo a tus amigos? — ___ mandé.',opts:['Se lo','Les lo','Se la'],ans:'Se lo',why:'les+lo → se lo'}]});
 buildChoice('gx_subj',{title:'Conectores del relato',desc:'Kies de connector die past.',per:7,pool:[
   {q:'___ un niño pobre (begin).',opts:['Érase una vez','Al final','Por eso'],ans:'Érase una vez',why:'begin'},
   {q:'Nació y ___ estudió (vervolg).',opts:['después','al final','érase'],ans:'después',why:'vervolg'},
   {q:'Estudió y ___ triunfó (toen/dus).',opts:['entonces','primero','érase'],ans:'entonces',why:'toen/dus'},
   {q:'___, murió muy famoso (einde).',opts:['Al final','Primero','Érase'],ans:'Al final',why:'einde'},
   {q:'Trabajó mucho; ___ es famoso (daarom).',opts:['por eso','después','primero'],ans:'por eso',why:'daarom'},
   {q:'___ nació, luego creció (eerst).',opts:['Primero','Al final','Entonces'],ans:'Primero',why:'eerst'},
   {q:'Ganó y ___ se hizo rico (daarna).',opts:['después','érase','al final'],ans:'después',why:'daarna'},
   {q:'«er was eens» =',opts:['érase una vez','al final','por eso'],ans:'érase una vez',why:'begin'}]});
 buildChoice('gx_plural',{title:'Traduce — indefinido / se lo',desc:'Kies de correcte Spaanse zin.',per:6,pool:[
   {q:'Hij werd geboren in 1927. →',opts:['Nació en 1927.','Nace en 1927.','Ha nacido en 1927.'],ans:'Nació en 1927.',why:'indefinido'},
   {q:'Hij deed/maakte veel. →',opts:['Hizo mucho.','Hació mucho.','Hace mucho.'],ans:'Hizo mucho.',why:'hacer → hizo'},
   {q:'Zij was president. →',opts:['Fue presidenta.','Es presidenta.','Fui presidenta.'],ans:'Fue presidenta.',why:'ser → fue'},
   {q:'Het boek gaf ik aan hem. →',opts:['Se lo di.','Le lo di.','Lo le di.'],ans:'Se lo di.',why:'se lo'},
   {q:'De foto (aan haar) stuurde ik. →',opts:['Se la mandé.','Le la mandé.','La le mandé.'],ans:'Se la mandé.',why:'se la'},
   {q:'Ik denk dat hij een genie was. →',opts:['Creo que fue un genio.','Creo que es un genio.','Creo que fui un genio.'],ans:'Creo que fue un genio.',why:'creo que fue'}]});
 buildChoice('gx_nac',{title:'Formas fuertes — traduce',desc:'Kies de correcte él/ella-vorm.',per:6,pool:[
   {q:'hij had (tener) →',opts:['tuvo','tenió','tuvió'],ans:'tuvo',why:'tuvo'},
   {q:'hij zei (decir) →',opts:['dijo','dició','deció'],ans:'dijo',why:'dijo'},
   {q:'hij kwam (venir) →',opts:['vino','venió','vinió'],ans:'vino',why:'vino'},
   {q:'hij gaf (dar) →',opts:['dio','dió','daba'],ans:'dio',why:'dio'},
   {q:'hij was (estar) →',opts:['estuvo','estó','estaba'],ans:'estuvo',why:'estuvo'},
   {q:'hij kon (poder) →',opts:['pudo','podió','pudió'],ans:'pudo',why:'pudo'}]});
 buildMatch('gx_conc',{title:'Empareja: infinitivo ↔ indefinido (él)',desc:'Koppel het werkwoord aan de él/ella-vorm.',per:6,pool:[
   {a:'ser/ir',b:'fue'},{a:'hacer',b:'hizo'},{a:'tener',b:'tuvo'},{a:'estar',b:'estuvo'},
   {a:'decir',b:'dijo'},{a:'venir',b:'vino'},{a:'dar',b:'dio'},{a:'ver',b:'vio'}]});
 buildMatch('gx_conc2',{title:'Empareja: pregunta ↔ respuesta (se lo)',desc:'Koppel de vraag aan het antwoord.',per:6,pool:[
   {a:'¿El libro a Mateo?',b:'Se lo di.'},{a:'¿La carta a Nina?',b:'Se la mandé.'},
   {a:'¿Los discos a Diego?',b:'Se los presté.'},{a:'¿Las fotos a Valen?',b:'Se las enseñé.'},
   {a:'¿El secreto a ella?',b:'Se lo conté.'},{a:'¿Las llaves a él?',b:'Se las dejé.'}]});
 buildChoice('gx_mix',{title:'Repaso mixto — indefinido + fuertes + se lo',desc:'Alles door elkaar. Directe feedback.',per:8,pool:[
   {q:'(Él) ___ (nacer) en 1927.',opts:['nació','nace','ha nacido'],ans:'nació',why:'indefinido'},
   {q:'hacer → indefinido (él)',opts:['hizo','hació','hace'],ans:'hizo',why:'hizo'},
   {q:'ser/ir → indefinido (él)',opts:['fue','fui','era'],ans:'fue',why:'fue'},
   {q:'¿El libro a él? ___ di.',opts:['Se lo','Le lo','Se la'],ans:'Se lo',why:'se lo'},
   {q:'«hij schreef» =',opts:['escribió','escribe','ha escrito'],ans:'escribió',why:'indefinido'},
   {q:'tener → indefinido (yo)',opts:['tuve','tení','tengo'],ans:'tuve',why:'tuve'},
   {q:'¿Las fotos a ella? ___ mandé.',opts:['Se las','Le las','Se los'],ans:'Se las',why:'se las'},
   {q:'«uiteindelijk» =',opts:['al final','primero','entonces'],ans:'al final',why:'conector'},
   {q:'Nosotros ___ (vivir) allí.',opts:['vivimos','vivíamos','vivieron'],ans:'vivimos',why:'nosotros'},
   {q:'decir → indefinido (él)',opts:['dijo','dició','dice'],ans:'dijo',why:'dijo'},
   {q:'¿La carta a Nina? ___ di.',opts:['Se la','Le la','Se lo'],ans:'Se la',why:'se la'},
   {q:'«ik werd geboren» =',opts:['nací','nazco','he nacido'],ans:'nací',why:'yo indefinido'}]});
 // ===== VOCABULARIO =====
 buildMatch('vx_match',{title:'Empareja: palabra ↔ emoji',desc:'Koppel het woord aan de emoji.',per:6,pool:[
   {a:'el escritor',b:'✍️'},{a:'la pintora',b:'🎨'},{a:'el cantante',b:'🎤'},{a:'el futbolista',b:'⚽'},
   {a:'el premio',b:'🏆'},{a:'nacer',b:'👶'},{a:'morir',b:'⚰️'},{a:'la leyenda',b:'📖'},
   {a:'el científico',b:'🔬'},{a:'casarse',b:'💍'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat past.',per:6,pool:[
   {q:'Frida ___ en México en 1907.',opts:['nació','ganó','murió'],ans:'nació',why:'geboren = nació'},
   {q:'García Márquez ___ el Nobel.',opts:['ganó','pintó','nació'],ans:'ganó',why:'won = ganó'},
   {q:'Gardel fue un ___ de tango.',opts:['cantante','pintor','científico'],ans:'cantante',why:'zanger'},
   {q:'Un ___ escribe novelas.',opts:['escritor','pintor','futbolista'],ans:'escritor',why:'schrijver'},
   {q:'Messi ___ el Mundial en 2022.',opts:['ganó','pintó','escribió'],ans:'ganó',why:'won'},
   {q:'Recibió un ___ importante.',opts:['premio','personaje','leyenda'],ans:'premio',why:'prijs'},
   {q:'Ella ___ (morir) en 1954.',opts:['murió','morió','moría'],ans:'murió',why:'morir → murió'},
   {q:'«Érase una ___» (er was eens)',opts:['vez','historia','vida'],ans:'vez',why:'érase una vez'},
   {q:'Creo que ___ un genio.',opts:['fue','es','era'],ans:'fue',why:'indefinido'},
   {q:'Primero nació, ___ estudió.',opts:['después','al final','por eso'],ans:'después',why:'daarna'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het woord.',per:6,pool:[
   {q:'Iemand die verhalen/boeken schrijft:',opts:['el escritor','el pintor','el cantante'],ans:'el escritor',why:'schrijver'},
   {q:'Geboren worden:',opts:['nacer','morir','crecer'],ans:'nacer',why:'geboren worden'},
   {q:'Een prijs winnen:',opts:['ganar','pintar','vivir'],ans:'ganar',why:'winnen'},
   {q:'De él/ella-vorm van «hacer» in indefinido:',opts:['hizo','hació','hace'],ans:'hizo',why:'hizo'},
   {q:'«was» én «ging» (indefinido):',opts:['fue','era','iba'],ans:'fue',why:'fue = ser/ir'},
   {q:'«het boek aan hem» (2 pron.):',opts:['se lo','le lo','lo le'],ans:'se lo',why:'se lo'},
   {q:'Verhaalbegin «er was eens»:',opts:['érase una vez','al final','por eso'],ans:'érase una vez',why:'begin'},
   {q:'«beroemd»:',opts:['famoso','increíble','importante'],ans:'famoso',why:'beroemd'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['nacer','crecer','morir','ganar'],odd:3,why:'ganar is een logro, geen levensfase'},
   {words:['el escritor','el pintor','el cantante','el premio'],odd:3,why:'el premio is geen persoon'},
   {words:['fue','hizo','tuvo','hace'],odd:3,why:'hace is presente, geen indefinido'},
   {words:['ayer','en 1919','el año pasado','mañana'],odd:3,why:'mañana is toekomst'},
   {words:['se lo','se la','se los','le lo'],odd:3,why:'«le lo» bestaat niet → se lo'},
   {words:['primero','después','al final','famoso'],odd:3,why:'famoso is geen connector'},
   {words:['escribió','pintó','ganó','escribe'],odd:3,why:'escribe is presente'},
   {words:['nació','vivió','murió','vive'],odd:3,why:'vive is presente'}]});
 // ===== LECTURA =====
 buildOrder('lx_order',{title:'Ordena',desc:'Tik in de juiste volgorde.',rounds:[
   {sub:'la vida de Frida',items:[{label:'Nació en 1907.',key:1},{label:'Tuvo un accidente.',key:2},{label:'Empezó a pintar.',key:3},{label:'Murió en 1954.',key:4}]},
   {sub:'la vida de Messi',items:[{label:'Nació en Rosario.',key:1},{label:'Jugó en un equipo local.',key:2},{label:'Se mudó a Barcelona.',key:3},{label:'Fue campeón del Mundo.',key:4}]},
   {sub:'indefinido',items:[{label:'García Márquez',key:1},{label:'escribió',key:2},{label:'muchas',key:3},{label:'novelas.',key:4}]},
   {sub:'opinión',items:[{label:'Creo que',key:1},{label:'fue',key:2},{label:'un genio',key:3},{label:'porque cambió el arte.',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in de twee biografieën (Frida y Messi) en kies.',per:6,pool:[
   {q:'¿Dónde nació Frida?',opts:['en México','en Argentina','en España'],ans:'en México',why:'«nació en México»'},
   {q:'¿Qué le pasó de joven a Frida?',opts:['un accidente','ganó un premio','se mudó'],ans:'un accidente',why:'«tuvo un accidente grave»'},
   {q:'¿Con quién se casó Frida?',opts:['con Diego Rivera','con Gardel','con un futbolista'],ans:'con Diego Rivera',why:'«Se casó con Diego Rivera»'},
   {q:'¿Dónde nació Messi?',opts:['en Rosario','en Buenos Aires','en Barcelona'],ans:'en Rosario',why:'«nació en Rosario»'},
   {q:'¿Adónde se mudó Messi?',opts:['a Barcelona','a Madrid','a México'],ans:'a Barcelona',why:'«se mudó a Barcelona»'},
   {q:'¿Cuándo fue campeón del Mundo Messi?',opts:['en 2022','en 1986','en 2007'],ans:'en 2022',why:'«en 2022 fue campeón»'},
   {q:'¿Qué pintó Frida?',opts:['autorretratos','paisajes','retratos de reyes'],ans:'autorretratos',why:'«Pintó muchos autorretratos»'},
   {q:'¿Qué dijo mucha gente de Messi?',opts:['que hizo historia','que perdió','que se retiró'],ans:'que hizo historia',why:'«dijo que hizo historia»'}]});
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='C6plus_U5_web_mijn_versie.html';a.click();};
})();
"""

# Getypte woordenschat-drills (fase ophalen + produceren) in het paneel zelf.
JS += hub_type_sets.vocab_type_js(vocab)
JS += hub_type_gram.js('C6+', 5)
HTML = HTML.replace("__GRAMSLOTS__", hub_type_gram.slots('C6+', 5))
HTML = HTML.replace("__TYPESLOTS__", hub_type_sets.SLOTS_HTML)

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/C6plus_U5_web.html","w").write(html)
print("C6plus_U5_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
