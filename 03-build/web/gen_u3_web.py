#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C5 · U3 «El tiempo vuela».
# Eén standalone bestand: fonts base64, de 24 U3-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U3-vocab), visuele/interactieve grammatica (la hora · reflexivos · presente irregular · de/por),
# klikbare kaart (mundo hispano) + TTS + editbar + inline recorders. Zelfde pijplijn/huisstijl als U0/U1-hub (groen).
import json, base64, os, sys
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
GEN = f"{ROOT}/02-huisstijl/beeld/generators"
sys.path.insert(0, GEN); import cast_gen as C; import vocab_icons as VI; import vocab_emoji as VE
vocab = json.load(open(f"{ROOT}/01-cursussen/05-a1/U3/u3_vocab.json", encoding="utf-8"))
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

# ---- de 24 U3-motor-spellen: gegroepeerd (receptief -> productief) + base64 ingebed ----
MOTOR = [
 ['① Reconocer · woordenschat', [
   ['hora-reloj', '¿qué hora es? (reloj)', 'match'],
   ['rutina-memoria', 'memoria de la rutina', 'memory'],
   ['verbo-memoria', 'verbos irregulares (memoria)', 'memory']]],
 ['② Distinguir · gramática', [
   ['reflexivo-no', '¿reflexivo o no?', 'classify'],
   ['cambio-raiz', 'cambio de raíz (ue/ie/i)', 'classify'],
   ['de-por', '¿de la o por la?', 'classify'],
   ['dia-mes', '¿día, mes o estación?', 'classify']]],
 ['③ Producir con apoyo', [
   ['la-hora', 'la hora (completa)', 'cloze'],
   ['reflexivo-cloze', 'verbos reflexivos', 'cloze'],
   ['irregular-cloze', 'presente irregular', 'cloze'],
   ['frecuencia', 'adverbios de frecuencia', 'cloze'],
   ['irregular-tetris', 'presente irregular Tetris', 'tetris'],
   ['tonica-rutina', 'la tónica de la rutina', 'tap'],
   ['orden-rutina', 'ordena mi rutina', 'order']]],
 ['④ Analizar & comunicar', [
   ['caza-reflexivo', 'caza del reflexivo', 'point'],
   ['senala-manana', 'señala la mañana', 'point'],
   ['hora-digital', 'el reloj de 24 horas', 'match'],
   ['orden-dia', 'ordena el día de Pau', 'order'],
   ['describe-dia', 'describe tu día', 'sim']]],
 ['⑤ Hablar · grábate 🎙️', [
   ['repite-hora', 'escucha y repite: la hora', 'speak'],
   ['shadowing-rutina', 'shadowing: la rutina de Pau', 'speak'],
   ['carrusel-dia', 'carrusel: mi día', 'speak'],
   ['mensaje-dia', 'mensaje de voz: mi día', 'speak'],
   ['describe-pau', 'describe la rutina de Pau', 'speak']]],
]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-u3-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-u3-{s}.html")}

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
.mealstrip{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0 2px}
.mealstrip .mc{flex:1 1 120px;background:var(--gt);border-radius:12px;padding:10px 8px;text-align:center}
.mealstrip .mc .em{font-size:26px;line-height:1}
.mealstrip .mc .nm{font-family:var(--disp);color:var(--gd);font-weight:700;font-size:14px;margin-top:2px}
.mealstrip .mc .hr{font-size:12px;color:var(--mut)}
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
/* lectura */
.perfiles{display:grid;grid-template-columns:1fr;gap:14px}
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
/* recorder */
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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="hora">la hora</option><option value="rutina">la rutina</option><option value="verbos">verbos irregulares</option><option value="frecuencia">frecuencia</option><option value="tiempo">días/meses/estaciones</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Español en la práctica · U3 El tiempo vuela</title>
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
    <div><h1>U3 · El tiempo vuela</h1>
    <p>La página digital de la Unidad 3 (parada <b>Barcelona</b>): flashcards, gramática visual e interactiva, <b>24 juegos</b> y <b>+100 ejercicios</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U3. Klik om te draaien; wissel ES↔NL; filter per groep; klik 🔊 om te horen. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
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
    <p class="lead">Eerst betekenis en patroon ontdekken, dan de regel. Beweeg over de woorden, klik, en probeer. <span class="gloss">Alles binnen het thema van U3: la hora, verbos reflexivos, presente irregular en de/por.</span></p>
    <div class="card" id="colorsent"></div>
    <div class="card" id="reflexconj"></div>
    <h3 class="subh">🕐 La hora — ¿qué hora es?</h3>
    <div class="game" id="g_hora"></div>
    <div class="card ex" id="gx_horaq"></div>
    <h3 class="subh">🔁 Verbos reflexivos — construye y practica</h3>
    <div class="card ex" id="gx_build"></div>
    <div class="card ex" id="gx_reflexq"></div>
    <div class="card ex" id="gx_reflexm"></div>
    <h3 class="subh">⚙️ Presente irregular — o&gt;ue · e&gt;ie · e&gt;i + hacer/ir/salir</h3>
    <div class="game" id="g_raiz"></div>
    <div class="card ex" id="gx_irreg"></div>
    <div class="card ex" id="gx_irregm"></div>
    <h3 class="subh">📅 Frecuencia y momentos del día</h3>
    <div class="card ex" id="gx_frec"></div>
    <div class="game" id="g_depor"></div>
    <div class="card ex" id="gx_deporq"></div>
    <h3 class="subh">🎯 Repaso mixto — rellena con feedback</h3>
    <div class="card ex" id="gx_mix"></div>
  </section>

  <section class="panel" data-p="lectura">
    <h2 class="sec">Lectura · el día de Pau</h2>
    <p class="lead">Lees het blog van Pau, <b>luister</b> het (🔊 TTS) en <b>controleer je begrip</b>. Daarna reageer je met een eigen bericht — dat neem je op in het tabblad <b>Hablar</b>. <span class="gloss">Keten: lezen → luisteren → spreken.</span></p>
    <div id="lecturawrap"></div>
    <h3 class="subh">🔢 Ordena el día de Pau</h3>
    <div class="card ex" id="lx_order"></div>
    <h3 class="subh">🔎 Comprensión · escanea y escoge</h3>
    <div class="card ex" id="lx_scan"></div>
  </section>

  <section class="panel" data-p="juegos">
    <h2 class="sec">Ejercicios · 24 juegos, jij kiest</h2>
    <p class="lead">Geordend van <b>herkennen → onderscheiden → produceren met steun → analyseren &amp; communiceren → hablar</b>. Elk spel geeft directe, verklarende feedback en de steun bouwt af. <span class="gloss">Klik een spel; het opent in een venster en werkt ook offline.</span></p>
    <div id="motorlink"></div>
  </section>

  <section class="panel" data-p="hablar">
    <h2 class="sec">Hablar · grábate 🎙️</h2>
    <p class="lead">Neem <b>jezelf</b> op: luister naar het model, spreek in, luister terug, en neem opnieuw op. <span class="gloss">Werkt in Chrome/Edge; sta de micro toe. Print blijft bruikbaar zonder opname.</span></p>
    <div class="card" id="rec_hora"></div>
    <div class="card" id="rec_dia"></div>
    <div class="card" id="rec_mensaje"></div>
    <p class="lead" style="margin-top:8px">Meer spreek-/opnamespellen (shadowing, describe…) vind je ook onder <b>Juegos ⑤</b>.</p>
  </section>

  <section class="panel" data-p="cultura">
    <h2 class="sec">Cultura · El horario español</h2>
    <p class="lead">En España se come y se cena <b>más tarde</b> que en Bélgica, y la famosa <b>siesta</b> es más mito que realidad. <span class="gloss">In Spanje eet men later dan in België; de siësta is meer mythe dan realiteit. De klok zegt veel over een cultuur.</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/></svg>Las comidas 🍽️</h3>
      <p><b>desayuno</b> (~8 u, licht) · <b>comida/almuerzo</b> (~14–15 u, de hoofdmaaltijd!) · <b>merienda</b> (~18 u) · <b>cena</b> (~21–22 u). <span class="gloss">In België eet men rond 12 u en 18 u — een paar uur vroeger. La comida = 14–15 h ↔ la cena = 21–22 h.</span></p>
      <div class="mealstrip">
        <div class="mc"><div class="em">🌅</div><div class="nm">el desayuno</div><div class="hr">~8:00</div></div>
        <div class="mc"><div class="em">🍽️</div><div class="nm">la comida</div><div class="hr">~14:00</div></div>
        <div class="mc"><div class="em">🍪</div><div class="nm">la merienda</div><div class="hr">~18:00</div></div>
        <div class="mc"><div class="em">🌙</div><div class="nm">la cena</div><div class="hr">~21:30</div></div>
      </div></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/></svg>El instituto y la siesta</h3>
      <p>Veel scholen lopen van ~<b>8:30</b> tot ~<b>14:30</b>; 's middags: deberes, deporte, amigos. De <b>siesta</b>? Mito: todos duermen ↔ realidad: pocos, sobre todo mayores. <span class="gloss">Een ander ritme dan een lange schooldag met middagpauze; de siësta is vooral een mythe.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">La sobremesa 🗣️</h3>
      <p><b>ES:</b> Después de comer, la gente no se levanta enseguida: se quedan en la mesa charlando. Es <b>la sobremesa</b>, un momento para hablar, reír y estar juntos. <span class="gloss">Na het eten blijft men aan tafel napraten: de «sobremesa». Een gezellig moment dat soms lang duurt — tijd is hier relatief.</span></p></div>
    <h3 class="subh">📍 La Ruta · ¿dónde estamos?</h3>
    <p class="lead">Onze parada 3: <b>Barcelona</b> 🇪🇸. <b>Klik op een groen land</b> op de kaart voor info. Verderop: València → México → Colombia → Perú.</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een groen land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    <h2 class="sec">Extra · bronnen</h2>
    <p class="lead">Externe uitleg &amp; oefeningen (de leerkracht vult de links aan).</p>
    <div class="card"><p>🎬 <b>profedeele</b> (YouTube — la hora / verbos reflexivos / presente irregular) — <span class="gloss">link volgt.</span></p>
    <p>🧩 <b>arche-ele</b> (Genially — la rutina diaria / la hora) — <span class="gloss">link volgt.</span></p>
    <p>📄 In het boek (PDF) verwijzen de QR-codes naar déze pagina, op het juiste ankerpunt.</p></div>
  </section>

  <div class="foot">Español en la práctica · C5 · Unidad 3 «El tiempo vuela» — página digital. Uitbreiding op de PDF · huisstijl groen · print ↔ PowerPoint ↔ web.</div>
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
function speak(t,rate){if(!('speechSynthesis'in window))return;const u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=rate||.92;
  const vs=speechSynthesis.getVoices();const es=vs.find(v=>/^es/i.test(v.lang));if(es)u.voice=es;try{speechSynthesis.cancel();speechSynthesis.speak(u);}catch(e){}}
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
    const sp=d.querySelector('.spk');if(sp)sp.onclick=e=>{e.stopPropagation();speak(v.es.replace(/\(.*?\)/g,'').replace(/→.*/,''));};
    g.appendChild(d);});
  document.getElementById('fccount').textContent=n+' woorden';}
function renderTable(){const q=(document.getElementById('vsearch').value||'').toLowerCase();const b=document.getElementById('vbody');b.innerHTML='';let n=0;
  VOCAB.forEach(v=>{if(q&&!(v.es.toLowerCase().includes(q)||v.nl.toLowerCase().includes(q)||v.ej.toLowerCase().includes(q)))return;n++;
    const tr=document.createElement('tr');tr.innerHTML='<td><b>'+v.es+'</b></td><td>'+v.nl+'</td><td>'+v.soort+'</td><td class="gloss">'+v.ej+'</td>';b.appendChild(tr);});
  document.getElementById('vcount').textContent=n+' items';}

function scoreBar(id){return '<div class="scorebar" id="'+id+'"><span>Punten: <b class="pt">0</b></span><span>Reeks: <b class="st">0</b></span></div>'}
function setScore(el,pt,st){el.querySelector('.pt').textContent=pt;el.querySelector('.st').textContent=st}
function feedback(el,ok,msg){el.className='fb '+(ok?'good':'bad');el.innerHTML=(ok?'✅ ':'❌ ')+msg}

// ---- GRAMMAR-VIZ 1: kleurgecodeerde rutina-zin ----
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Mi rutina — beweeg over de woorden</h3>'+
'<div class="csent">'+
'<span style="background:#dbeafe;color:#1e40af">Yo<span class="tip">persoon (onderwerp)</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">me levanto<span class="tip">reflexief werkwoord · me + levanto</span></span> '+
'<span style="background:#ede9fe;color:#5b21b6">a las siete<span class="tip">tijd · la hora</span></span>, '+
'<span style="background:#fed7aa;color:#9a3412">me ducho<span class="tip">reflexief werkwoord</span></span> y '+
'<span style="background:#fed7aa;color:#9a3412">empiezo<span class="tip">presente irregular · e→ie</span></span> '+
'<span style="background:#ccfbf1;color:#0f766e">en el instituto<span class="tip">plaats</span></span> '+
'<span style="background:#ede9fe;color:#5b21b6">a las nueve<span class="tip">tijd</span></span>.</div>'+
'<div class="legend"><span><i style="background:#93c5fd"></i>persoon</span><span><i style="background:#fdba74"></i>werkwoord</span><span><i style="background:#5eead4"></i>plaats</span><span><i style="background:#c4b5fd"></i>tijd</span></div>'+
'<p class="gloss" style="margin-top:8px">🔴 <b>me</b> levanto — het reflexief pronomen staat <b>vóór</b> het werkwoord! · '+(TTS?'<button class="spk-btn" onclick="speak(\'Yo me levanto a las siete, me ducho y empiezo en el instituto a las nueve\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: reflexivo — klik om de vorm te onthullen ----
(function(){const el=document.getElementById('reflexconj');
 const R=[['yo','me levanto'],['tú','te levantas'],['él/ella/usted','se levanta'],['nosotros/-as','nos levantamos'],['vosotros/-as','os levantáis'],['ellos/-as/ustedes','se levantan']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Verbos reflexivos — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">Denk eerst zelf het pronombre + de vorm; klik dan de kaart. 🔊 om te horen.</p><div class="conjgrid" id="rcg"></div>';
 const g=el.querySelector('#rcg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v;if(TTS)speak(v);};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: la hora matcher (klik dígitos → frase) ----
function gameHora(){const el=document.getElementById('g_hora');
 const items=[['1:00','Es la una'],['2:30','Son las dos y media'],['3:15','Son las tres y cuarto'],['4:45','Son las cinco menos cuarto'],['6:00','Son las seis en punto'],['9:20','Son las nueve y veinte']];
 const cats=['Es la una','Son las dos y media','Son las tres y cuarto','Son las cinco menos cuarto','Son las seis en punto','Son las nueve y veinte'];let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿Qué hora es?</h3><p class="desc">Lees de digitale klok en kies de juiste zin.</p>'+scoreBar('sbH')+'<div id="hQ" style="font-size:32px;font-family:var(--disp);text-align:center;margin:10px 0;color:var(--gd)"></div><div class="chips" id="hC"></div><div class="fb" id="hFb"></div>';
 const sb=el.querySelector('#sbH');const cont=el.querySelector('#hC');
 cats.forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#hQ').textContent=el.cur[0];el.querySelector('#hFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#hFb'),ok,(ok?'¡Sí! ':'Nee → ')+el.cur[0]+' = «'+el.cur[1]+'».');if(TTS&&ok)speak(el.cur[1]);setTimeout(next,1000);}
 next();}
// ---- GRAMMAR-VIZ 4: ¿de la o por la? ----
function gameDePor(){const el=document.getElementById('g_depor');
 const items=[['Son las 7 ___ mañana.','de la'],['___ tarde hago deporte.','por la'],['Ceno a las 9 ___ noche.','de la'],['___ mañana voy al insti.','por la'],['Me levanto a las 8 ___ mañana.','de la'],['Estudio ___ noche.','por la']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿de la o por la?</h3><p class="desc">Concreet uur → <b>de la</b>. Deel van de dag → <b>por la</b>.</p>'+scoreBar('sbD')+'<div id="dW" style="font-size:20px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._deporG(\'de la\')">de la</div><div class="chip" onclick="window._deporG(\'por la\')">por la</div></div><div class="fb" id="dFb"></div>';
 const sb=el.querySelector('#sbD');
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#dW').textContent=el.cur[0];el.querySelector('#dFb').className='fb';}
 window._deporG=k=>{const ok=k===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#dFb'),ok,(ok?'¡Sí! ':'Nee → ')+'«'+el.cur[1]+'» ('+(el.cur[1]==='de la'?'concreet uur':'dagdeel, geen uur')+').');setTimeout(next,950);};
 next();}

// ---- GRAMMAR-VIZ 5: cambio de raíz — ¿o>ue, e>ie, e>i o regular? ----
function gameRaiz(){const el=document.getElementById('g_raiz');
 const items=[['dormir','o>ue','duermo'],['poder','o>ue','puedo'],['volver','o>ue','vuelvo'],['almorzar','o>ue','almuerzo'],['jugar','u>ue','juego'],
  ['empezar','e>ie','empiezo'],['querer','e>ie','quiero'],['preferir','e>ie','prefiero'],['despertarse','e>ie','me despierto'],
  ['pedir','e>i','pido'],['vestirse','e>i','me visto'],['servir','e>i','sirvo'],
  ['trabajar','regular','trabajo'],['estudiar','regular','estudio'],['desayunar','regular','desayuno']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿Cómo cambia la raíz?</h3><p class="desc">Kies de stamwissel in de <b>yo</b>-vorm. (Let op: nosotros/vosotros wisselen NIET!)</p>'+scoreBar('sbR')+'<div id="rW" style="font-size:26px;font-family:var(--disp);text-align:center;margin:8px 0;color:var(--gd)"></div><div class="chips" id="rC" style="justify-content:center"></div><div class="fb" id="rFb"></div>';
 const sb=el.querySelector('#sbR');const cont=el.querySelector('#rC');
 ['o>ue','u>ue','e>ie','e>i','regular'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#rW').textContent=el.cur[0];el.querySelector('#rFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#rFb'),ok,(ok?'¡Sí! ':'Nee → ')+el.cur[0]+' → yo '+el.cur[2]+' ('+el.cur[1]+').');if(TTS&&ok)speak(el.cur[2]);setTimeout(next,1050);}
 next();}

// ---- MOTOR-ARCADE: 24 spellen, ingebed ----
document.getElementById('motorlink').innerHTML=MOTOR.map(([grp,gs])=>'<div class="subh">'+grp+'</div><div class="fcgrid">'+
   gs.map(([f,t,tpl])=>'<div class="chip" style="display:block;border-radius:14px" onclick="openGame(\''+f+'\',\''+t.replace(/'/g,"")+'\')"><div style="font-weight:700;color:var(--ink);font-size:14px">'+t+'</div><div class="pill" style="margin-top:4px;font-size:10px">'+tpl+'</div></div>').join('')+'</div>').join('');
function openGame(slug,title){const g=GAMES[slug];if(!g){alert('Spel niet gevonden.');return;}
  document.getElementById('gmtitle').textContent=title;document.getElementById('gframe').src='data:text/html;base64,'+g;document.getElementById('gmodal').classList.add('show');}
function closeGame(){document.getElementById('gmodal').classList.remove('show');document.getElementById('gframe').src='about:blank';}
document.getElementById('gmodal').addEventListener('click',e=>{if(e.target.id==='gmodal')closeGame();});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeGame();});

// ---- KAART interactief ----
(function(){
 const INFO={
  ESP:{fl:'🇪🇸',n:'España',cap:'Madrid',f:'Onze parada 3: Barcelona, in Catalunya. Pau habla catalán y español.',nl:'Parada 3 · Barcelona (Lucía + Pau).',star:1},
  MEX:{fl:'🇲🇽',n:'México',cap:'Ciudad de México',f:'Meeste Spaanstaligen ter wereld (~130 mln).',nl:'Parada van Diego.',star:1},
  COL:{fl:'🇨🇴',n:'Colombia',cap:'Bogotá',f:'Parada: Cartagena.',nl:'Parada van Valen.',star:1},
  PER:{fl:'🇵🇪',n:'Perú',cap:'Lima',f:'Parada: Cusco en Machu Picchu.',nl:'Parada van Nina.',star:1},
  GTM:{fl:'🇬🇹',n:'Guatemala',cap:'Ciudad de Guatemala',f:'Rijke Maya-erfenis.',nl:''},HND:{fl:'🇭🇳',n:'Honduras',cap:'Tegucigalpa',f:'Hart van Centraal-Amerika.',nl:''},
  SLV:{fl:'🇸🇻',n:'El Salvador',cap:'San Salvador',f:'Kleinste land van Centraal-Amerika.',nl:''},NIC:{fl:'🇳🇮',n:'Nicaragua',cap:'Managua',f:'Land van meren en vulkanen.',nl:''},
  CRI:{fl:'🇨🇷',n:'Costa Rica',cap:'San José',f:'«¡Pura vida!» — geen leger.',nl:''},PAN:{fl:'🇵🇦',n:'Panamá',cap:'Panamá',f:'Het kanaal verbindt twee oceanen.',nl:''},
  CUB:{fl:'🇨🇺',n:'Cuba',cap:'La Habana',f:'Bakermat van son en salsa.',nl:''},DOM:{fl:'🇩🇴',n:'República Dominicana',cap:'Santo Domingo',f:'Oudste stad van Amerika.',nl:''},
  PRI:{fl:'🇵🇷',n:'Puerto Rico',cap:'San Juan',f:'Vrijstaat verbonden met de VS.',nl:''},VEN:{fl:'🇻🇪',n:'Venezuela',cap:'Caracas',f:'Salto Ángel: hoogste waterval ter wereld.',nl:''},
  ECU:{fl:'🇪🇨',n:'Ecuador',cap:'Quito',f:'«La mitad del mundo»: op de evenaar.',nl:''},BOL:{fl:'🇧🇴',n:'Bolivia',cap:'Sucre / La Paz',f:'Salar de Uyuni: grootste zoutvlakte.',nl:''},
  PRY:{fl:'🇵🇾',n:'Paraguay',cap:'Asunción',f:'Tweetalig: español én guaraní.',nl:''},URY:{fl:'🇺🇾',n:'Uruguay',cap:'Montevideo',f:'Klein land tussen twee reuzen.',nl:''},
  ARG:{fl:'🇦🇷',n:'Argentina',cap:'Buenos Aires',f:'De tango; vanaf C6 gastheer Mateo (voseo).',nl:''},CHL:{fl:'🇨🇱',n:'Chile',cap:'Santiago',f:'Het langste, smalste land ter wereld.',nl:''},
  GNQ:{fl:'🇬🇶',n:'Guinea Ecuatorial',cap:'Malabo',f:'Het enige Spaanstalige land in Afrika.',nl:''},USA:{fl:'🇺🇸',n:'Estados Unidos',cap:'Washington D.C.',f:'~60 mln hispanohablantes.',nl:''}
 };
 const wrap=document.getElementById('mapwrap');const svg=wrap.querySelector('svg');const box=document.getElementById('mapinfo');
 if(!svg)return;
 svg.querySelectorAll('path.spa, path.usa').forEach(p=>{p.style.cursor='pointer';
   p.addEventListener('mouseenter',()=>{p.style.opacity='.75'});p.addEventListener('mouseleave',()=>{p.style.opacity=''});
   p.addEventListener('click',()=>{const c=p.getAttribute('data-c');const d=INFO[c];if(!d)return;
     box.innerHTML='<h3>'+d.fl+' '+d.n+' <span style="font-size:13px;color:var(--mut);font-weight:400">('+c+')</span>'+(d.star?' ★':'')+'</h3><div class="mrow"><b>Capital:</b> '+d.cap+'</div><div class="mrow">'+d.f+'</div>'+(d.nl?'<div class="gloss">'+d.nl+'</div>':'');
     box.scrollIntoView({behavior:'smooth',block:'nearest'});});
 });
})();

// ---------- LECTURA: el blog de Pau + TTS + begrip ----------
function renderLectura(){const el=document.getElementById('lecturawrap');if(!el)return;
 const P=[{n:'El blog de Pau',fr:'Barcelona · un día normal',t:'¡Hola! Soy Pau, de Barcelona. Os cuento mi día. <span class="ev">Me despierto a las siete</span> y me levanto enseguida. Me ducho, me visto y desayuno un bocadillo. <span class="ev">Salgo de casa a las ocho</span> y voy al instituto en metro. Las clases <span class="ev">empiezan a las nueve</span>. Al mediodía <span class="ev">almuerzo en el instituto</span> con mis amigos. Por la tarde <span class="ev">hago los deberes</span> y, a menudo, <span class="ev">juego al fútbol</span>. Ceno con mi familia a las nueve y <span class="ev">me acuesto a las once</span>. Los sábados duermo más: ¡me levanto a las diez! ¿Y tú, a qué hora te levantas?'}];
 const strip=h=>h.replace(/<[^>]+>/g,'');
 el.innerHTML='<div class="perfiles">'+P.map((p,i)=>'<div class="perfil"><h4>📓 '+p.n+' <span class="gloss" style="font-size:12px;font-weight:400">· '+p.fr+'</span> '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lx'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div class="txt" id="lx'+i+'" data-raw="'+strip(p.t).replace(/"/g,'&quot;')+'">'+p.t+'</div></div>').join('')+'</div>';
 const items=[['Pau se despierta a las siete.',true,'«Me despierto a las siete»'],['Pau va al instituto en coche.',false,'va al instituto en metro'],['Las clases empiezan a las nueve.',true,'«empiezan a las nueve»'],['Los sábados se levanta temprano.',false,'los sábados se levanta a las diez (más tarde)']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — comprueba tu comprensión</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Responde</h3><p class="gloss" style="margin:0 0 8px">Schrijf Pau een antwoord over jouw dag (horas + rutina). Neem het op onder <b>Hablar 🎙️</b> («mensaje de voz: mi día»).</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="¡Hola, Pau! Me levanto a las…"></textarea>';
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
 makeRecorder('rec_hora',{title:'Escucha y repite: la hora',desc:'Luister → zeg de tijd na → neem op → luister terug → opnieuw.',items:[
   {text:'Es la una en punto.',cue:'1:00'},{text:'Son las dos y media.',cue:'2:30'},{text:'Son las cinco menos cuarto.',cue:'4:45'},{text:'Son las nueve de la noche.',cue:'21:00',tip:'Duidelijk? Zeg nu de tijd van nu, zonder te lezen.'}]});
 makeRecorder('rec_dia',{title:'Carrusel: mi día',desc:'Eén element wisselt per ronde. Bouw de zin en spreek ze in.',items:[
   {text:'Me levanto a las siete y desayuno.',cue:'ronde 1'},{text:'Me levanto a las seis y media y me ducho.',cue:'ronde 2'},{text:'Me levanto a las… y…',cue:'jouw versie'}]});
 makeRecorder('rec_mensaje',{title:'Mensaje de voz: mi día',desc:'Neem één bericht op. Ontvanger: Pau · Doel: je dag vertellen. Gebruik: me levanto a las… · por la tarde… · me acuesto a las…',items:[
   {text:'Cuéntale tu día a Pau en un mensaje de voz (30 s).',cue:'para · Pau',tip:'Heb je horas + rutina (mañana/tarde/noche) gezegd? Neem opnieuw op.'}]});
}

// ================= INLINE ZELFCORRIGERENDE OEFENINGEN =================
function exSample(pool,n){const a=pool.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a.slice(0,Math.min(n,a.length));}
function exEsc(s){return String(s).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
function exFmt(s){return exEsc(s).replace(/___+/g,'<span class="gap">&nbsp;&nbsp;</span>');}

// MEERKEUZE / GAP-FILL: pool item = {q, opts, ans, why}
function buildChoice(id,cfg){
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

// MATCHING: pool item = {a,b}  (b moet uniek zijn)
function buildMatch(id,cfg){
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
function buildOrder(id,cfg){
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
function buildOdd(id,cfg){
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

// ---- data + calls ----
function buildInlineExercises(){
 // ---------- GRAMÁTICA ----------
 // LA HORA — mini-quiz (schrijf/kies de zin)
 buildChoice('gx_horaq',{title:'Mini-quiz: ¿qué hora es?',desc:'Lees de digitale klok en kies de juiste zin. Es la una (1) · Son las… (2+) · y cuarto/media · menos cuarto.',per:6,pool:[
   {q:'1:00 →',opts:['Es la una','Son las una','Son la una'],ans:'Es la una',why:'1 uur → «es la una»'},
   {q:'3:00 →',opts:['Son las tres','Es las tres','Son la tres'],ans:'Son las tres',why:'vanaf 2 → «son las»'},
   {q:'2:30 →',opts:['Son las dos y media','Son las dos y treinta','Es la dos y media'],ans:'Son las dos y media',why:'30 min → «y media»'},
   {q:'4:15 →',opts:['Son las cuatro y cuarto','Son las cuatro y quince','Son las cuatro menos cuarto'],ans:'Son las cuatro y cuarto',why:'15 min → «y cuarto»'},
   {q:'6:45 →',opts:['Son las siete menos cuarto','Son las seis y cuarenta y cinco','Son las seis menos cuarto'],ans:'Son las siete menos cuarto',why:'45 → volgend uur «menos cuarto»'},
   {q:'9:00 →',opts:['Son las nueve en punto','Es la nueve','Son las nueve y punto'],ans:'Son las nueve en punto',why:'exact uur → «en punto»'},
   {q:'5:20 →',opts:['Son las cinco y veinte','Son las cinco menos veinte','Es la cinco y veinte'],ans:'Son las cinco y veinte',why:'+20 min → «y veinte»'},
   {q:'8:50 →',opts:['Son las nueve menos diez','Son las ocho y cincuenta','Son las ocho menos diez'],ans:'Son las nueve menos diez',why:'50 → volgend uur «menos diez»'},
   {q:'1:30 →',opts:['Es la una y media','Son la una y media','Son las una y media'],ans:'Es la una y media',why:'1 uur blijft «es la una…»'},
   {q:'12:00 →',opts:['Son las doce','Es las doce','Son la doce'],ans:'Son las doce',why:'12 → «son las doce»'},
   {q:'7:10 →',opts:['Son las siete y diez','Son las siete menos diez','Es la siete y diez'],ans:'Son las siete y diez',why:'+10 → «y diez»'},
   {q:'10:40 →',opts:['Son las once menos veinte','Son las diez y cuarenta','Son las diez menos veinte'],ans:'Son las once menos veinte',why:'40 → volgend uur «menos veinte»'}]});
 // REFLEXIVOS — construye
 buildOrder('gx_build',{title:'Construye: verbo reflexivo',desc:'Tik de blokjes in de juiste volgorde (onderwerp → pronombre me/te/se → werkwoord → tijd).',rounds:[
   {sub:'yo · levantarse',items:[{label:'Yo',key:1},{label:'me',key:2},{label:'levanto',key:3},{label:'a las siete',key:4}]},
   {sub:'tú · ducharse',items:[{label:'Tú',key:1},{label:'te',key:2},{label:'duchas',key:3},{label:'por la mañana',key:4}]},
   {sub:'Pau · acostarse',items:[{label:'Pau',key:1},{label:'se',key:2},{label:'acuesta',key:3},{label:'a las once',key:4}]},
   {sub:'nosotros · vestirse',items:[{label:'Nosotros',key:1},{label:'nos',key:2},{label:'vestimos',key:3},{label:'rápido',key:4}]},
   {sub:'yo · despertarse',items:[{label:'Yo',key:1},{label:'me',key:2},{label:'despierto',key:3},{label:'temprano',key:4}]},
   {sub:'ellos · acostarse',items:[{label:'Ellos',key:1},{label:'se',key:2},{label:'acuestan',key:3},{label:'tarde',key:4}]}]});
 // REFLEXIVOS — cloze (traditionele werkwoordscloze, VERPLICHT)
 buildChoice('gx_reflexq',{title:'Completa el verbo reflexivo',desc:'Kies de juiste vorm (pronombre + werkwoord). Klassieke werkwoordsoefening.',per:8,pool:[
   {q:'(Yo) ___ a las siete.',opts:['me levanto','te levantas','se levanta'],ans:'me levanto',why:'yo → me levanto'},
   {q:'(Tú) ___ en el baño.',opts:['te duchas','me ducho','se ducha'],ans:'te duchas',why:'tú → te duchas'},
   {q:'Pau ___ a las once de la noche.',opts:['se acuesta','me acuesto','te acuestas'],ans:'se acuesta',why:'él → se acuesta (o>ue)'},
   {q:'(Nosotros) ___ rápido.',opts:['nos vestimos','os vestís','se visten'],ans:'nos vestimos',why:'nosotros → nos vestimos'},
   {q:'(Yo) ___ temprano los lunes.',opts:['me despierto','te despiertas','se despierta'],ans:'me despierto',why:'yo → me despierto (e>ie)'},
   {q:'Mis amigos ___ tarde el finde.',opts:['se levantan','nos levantamos','os levantáis'],ans:'se levantan',why:'ellos → se levantan'},
   {q:'¿(Tú) ___ temprano?',opts:['te despiertas','me despierto','se despierta'],ans:'te despiertas',why:'tú → te despiertas'},
   {q:'(Nosotros) ___ a las siete.',opts:['nos levantamos','me levanto','se levantan'],ans:'nos levantamos',why:'nosotros → nos levantamos'},
   {q:'Lucía ___ y desayuna.',opts:['se viste','me visto','te vistes'],ans:'se viste',why:'ella → se viste (e>i)'},
   {q:'(Vosotros) ___ pronto.',opts:['os acostáis','se acuestan','nos acostamos'],ans:'os acostáis',why:'vosotros → os acostáis'},
   {q:'(Yo) ___ los dientes.',opts:['me lavo','te lavas','se lava'],ans:'me lavo',why:'yo → me lavo'},
   {q:'El niño ___ y va a la cama.',opts:['se acuesta','me acuesto','os acostáis'],ans:'se acuesta',why:'él → se acuesta'}]});
 // REFLEXIVOS — match pronombre ↔ persoon
 buildMatch('gx_reflexm',{title:'Empareja: persona ↔ forma',desc:'Koppel het onderwerp aan de juiste reflexieve vorm van «levantarse».',per:6,pool:[
   {a:'yo',b:'me levanto'},{a:'tú',b:'te levantas'},{a:'él / ella',b:'se levanta'},
   {a:'nosotros',b:'nos levantamos'},{a:'vosotros',b:'os levantáis'},{a:'ellos / ellas',b:'se levantan'}]});
 // PRESENTE IRREGULAR — cloze (traditionele werkwoordscloze, VERPLICHT)
 buildChoice('gx_irreg',{title:'Presente irregular · completa',desc:'Vul de juiste vorm in (o>ue · e>ie · e>i + hacer/ir/salir). Vormen nagerekend.',per:8,pool:[
   {q:'(Yo) ___ ocho horas. (dormir)',opts:['duermo','dormo','duermes'],ans:'duermo',why:'o>ue: yo duermo'},
   {q:'Las clases ___ a las nueve. (empezar)',opts:['empiezan','empezan','empiezo'],ans:'empiezan',why:'e>ie: ellos empiezan'},
   {q:'(Yo) ___ de casa a las ocho. (salir)',opts:['salgo','salo','sales'],ans:'salgo',why:'yo salgo (g irregular)'},
   {q:'(Yo) ___ los deberes por la tarde. (hacer)',opts:['hago','haco','haces'],ans:'hago',why:'yo hago'},
   {q:'¿(Tú) ___ jugar al fútbol? (poder)',opts:['puedes','podes','puede'],ans:'puedes',why:'o>ue: tú puedes'},
   {q:'Pau ___ al insti en metro. (ir)',opts:['va','ve','vas'],ans:'va',why:'ir: él va'},
   {q:'(Nosotros) ___ a las nueve. (volver)',opts:['volvemos','vuelvemos','volvéis'],ans:'volvemos',why:'nosotros NIET wisselen: volvemos'},
   {q:'(Yo) ___ un café. (pedir)',opts:['pido','pedo','pides'],ans:'pido',why:'e>i: yo pido'},
   {q:'Ella ___ estudiar más. (querer)',opts:['quiere','quere','quieres'],ans:'quiere',why:'e>ie: ella quiere'},
   {q:'(Ellos) ___ al fútbol el sábado. (jugar)',opts:['juegan','jugan','juegas'],ans:'juegan',why:'u>ue: ellos juegan'},
   {q:'(Yo) ___ a las siete. (almorzar → no, empezar)',opts:['empiezo','empezo','empiezas'],ans:'empiezo',why:'e>ie: yo empiezo'},
   {q:'(Nosotros) ___ a las tres. (almorzar)',opts:['almorzamos','almuerzamos','almorzáis'],ans:'almorzamos',why:'nosotros NIET wisselen: almorzamos'},
   {q:'(Yo) ___ estudiar francés. (preferir)',opts:['prefiero','prefero','prefieres'],ans:'prefiero',why:'e>ie: yo prefiero'},
   {q:'¿A qué hora ___ (tú) a casa? (volver)',opts:['vuelves','volves','vuelve'],ans:'vuelves',why:'o>ue: tú vuelves'}]});
 // PRESENTE IRREGULAR — match verbo ↔ yo-vorm
 buildMatch('gx_irregm',{title:'Empareja: infinitivo ↔ yo',desc:'Koppel de infinitief aan de juiste «yo»-vorm.',per:6,pool:[
   {a:'dormir',b:'duermo'},{a:'empezar',b:'empiezo'},{a:'poder',b:'puedo'},{a:'pedir',b:'pido'},
   {a:'hacer',b:'hago'},{a:'salir',b:'salgo'},{a:'jugar',b:'juego'},{a:'volver',b:'vuelvo'},
   {a:'querer',b:'quiero'},{a:'preferir',b:'prefiero'},{a:'ir',b:'voy'},{a:'servir',b:'sirvo'}]});
 // FRECUENCIA — ordena (schaal)
 buildOrder('gx_frec',{title:'Ordena la frecuencia',desc:'Tik van MEER naar MINDER frecuentie (100% → 0%).',rounds:[
   {sub:'de siempre a nunca',items:[{label:'siempre',key:1},{label:'a menudo',key:2},{label:'a veces',key:3},{label:'casi nunca',key:4},{label:'nunca',key:5}]},
   {sub:'los días de la semana',items:[{label:'lunes',key:1},{label:'martes',key:2},{label:'miércoles',key:3},{label:'jueves',key:4},{label:'viernes',key:5}]},
   {sub:'las estaciones (del año)',items:[{label:'primavera',key:1},{label:'verano',key:2},{label:'otoño',key:3},{label:'invierno',key:4}]},
   {sub:'los meses (primeros)',items:[{label:'enero',key:1},{label:'febrero',key:2},{label:'marzo',key:3},{label:'abril',key:4},{label:'mayo',key:5}]}]});
 // DE LA / POR LA — mini-quiz
 buildChoice('gx_deporq',{title:'Mini-quiz: de la / por la',desc:'Concreet uur → «de la». Deel van de dag (zonder uur) → «por la».',per:6,pool:[
   {q:'Son las siete ___ mañana.',opts:['de la','por la'],ans:'de la',why:'concreet uur → de la'},
   {q:'___ tarde hago deporte.',opts:['por la','de la'],ans:'por la',why:'dagdeel zonder uur → por la'},
   {q:'Ceno a las nueve ___ noche.',opts:['de la','por la'],ans:'de la',why:'concreet uur → de la'},
   {q:'___ mañana voy al insti.',opts:['por la','de la'],ans:'por la',why:'dagdeel → por la'},
   {q:'Me levanto a las ocho ___ mañana.',opts:['de la','por la'],ans:'de la',why:'concreet uur → de la'},
   {q:'Estudio ___ noche.',opts:['por la','de la'],ans:'por la',why:'dagdeel → por la'},
   {q:'Como a las dos ___ tarde.',opts:['de la','por la'],ans:'de la',why:'concreet uur → de la'},
   {q:'___ tarde juego al fútbol.',opts:['por la','de la'],ans:'por la',why:'dagdeel → por la'},
   {q:'Salgo a las tres ___ tarde.',opts:['de la','por la'],ans:'de la',why:'concreet uur → de la'},
   {q:'Desayuno ___ mañana, temprano.',opts:['por la','de la'],ans:'por la',why:'dagdeel → por la'}]});
 // REPASO MIXTO
 buildChoice('gx_mix',{title:'Repaso mixto: rellena',desc:'Alles door elkaar: la hora · reflexivos · irregulares · frecuencia · de/por.',per:8,pool:[
   {q:'(Yo) ___ a las siete y media. (levantarse)',opts:['me levanto','te levantas','se levanta'],ans:'me levanto',why:'yo → me levanto'},
   {q:'Las clases ___ a las nueve. (empezar)',opts:['empiezan','empezan','empieza'],ans:'empiezan',why:'e>ie: ellas empiezan'},
   {q:'2:30 → Son las dos ___ .',opts:['y media','y treinta','menos media'],ans:'y media',why:'30 → y media'},
   {q:'Estudio ___ noche.',opts:['por la','de la','en la'],ans:'por la',why:'dagdeel → por la'},
   {q:'(Yo) ___ ocho horas. (dormir)',opts:['duermo','dormo','duermes'],ans:'duermo',why:'o>ue: yo duermo'},
   {q:'___ nunca voy al cine. (100% → 0%)',opts:['Casi','Muy','Mucho'],ans:'Casi',why:'«casi nunca» = bijna nooit'},
   {q:'Pau ___ al insti en metro. (ir)',opts:['va','ve','vas'],ans:'va',why:'ir: él va'},
   {q:'Son las nueve ___ noche.',opts:['de la','por la','en la'],ans:'de la',why:'concreet uur → de la'},
   {q:'(Yo) ___ los deberes por la tarde. (hacer)',opts:['hago','haco','haces'],ans:'hago',why:'yo hago'},
   {q:'6:45 → Son las siete ___ cuarto.',opts:['menos','y','más'],ans:'menos',why:'45 → menos cuarto'},
   {q:'(Nosotros) ___ a las tres. (almorzar)',opts:['almorzamos','almuerzamos','almorzáis'],ans:'almorzamos',why:'nosotros NIET wisselen'},
   {q:'El lunes es el primer ___ de la semana.',opts:['día','mes','estación'],ans:'día',why:'lunes = día'}]});
 // ---------- VOCABULARIO ----------
 buildMatch('vx_match',{title:'Empareja: palabra ↔ emoji',desc:'Koppel het Spaanse woord aan het juiste beeld.',per:6,pool:[
   {a:'despertarse',b:'⏰'},{a:'ducharse',b:'🚿'},{a:'desayunar',b:'🥐'},{a:'el reloj',b:'🕐'},
   {a:'dormir',b:'😴'},{a:'el instituto',b:'🏫'},{a:'jugar al fútbol',b:'⚽'},{a:'la noche',b:'🌙'},
   {a:'la mañana',b:'🌅'},{a:'vestirse',b:'👕'},{a:'el calendario',b:'📅'},{a:'los deberes',b:'📓'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat in de zin past.',per:6,pool:[
   {q:'Miro la hora en el ___.',opts:['reloj','plato','libro'],ans:'reloj',why:'de klok = el reloj'},
   {q:'Por la mañana ___ un café con leche.',opts:['desayuno','ceno','duermo'],ans:'desayuno',why:'ontbijten = desayunar'},
   {q:'Por la noche ___ ocho horas.',opts:['duermo','juego','estudio'],ans:'duermo',why:'slapen = dormir'},
   {q:'Voy al ___ para estudiar.',opts:['instituto','parque','cine'],ans:'instituto',why:'school = el instituto'},
   {q:'Hago los ___ después de las clases.',opts:['deberes','platos','coches'],ans:'deberes',why:'huiswerk = los deberes'},
   {q:'Me ___ los dientes por la mañana.',opts:['lavo','como','abro'],ans:'lavo',why:'lavarse los dientes'},
   {q:'El sábado y el ___ no hay clase.',opts:['domingo','lunes','martes'],ans:'domingo',why:'weekend = sábado + domingo'},
   {q:'En ___ hace calor y no hay clase.',opts:['verano','invierno','otoño'],ans:'verano',why:'zomer = el verano'},
   {q:'Me levanto y me ___ enseguida.',opts:['ducho','ceno','vuelvo'],ans:'ducho',why:'douchen = ducharse'},
   {q:'Ceno con mi familia a las nueve de la ___.',opts:['noche','mañana','tarde'],ans:'noche',why:'21 u → de la noche'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het juiste woord.',per:6,pool:[
   {q:'La primera comida del día:',opts:['el desayuno','la cena','la merienda'],ans:'el desayuno',why:'ontbijt'},
   {q:'La última comida del día:',opts:['la cena','el desayuno','el almuerzo'],ans:'la cena',why:'avondmaal'},
   {q:'El objeto que da la hora:',opts:['el reloj','el móvil','la agenda'],ans:'el reloj',why:'klok'},
   {q:'La parte del día cuando sale el sol:',opts:['la mañana','la noche','la tarde'],ans:'la mañana',why:'ochtend'},
   {q:'El primer día de la semana (España):',opts:['lunes','domingo','sábado'],ans:'lunes',why:'maandag'},
   {q:'La estación del frío y la nieve:',opts:['el invierno','el verano','la primavera'],ans:'el invierno',why:'winter'},
   {q:'Lo haces en la cama por la noche:',opts:['dormir','correr','comer'],ans:'dormir',why:'slapen'},
   {q:'El deporte con un balón y dos porterías:',opts:['el fútbol','el tenis','la natación'],ans:'el fútbol',why:'voetbal'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['lunes','martes','enero','viernes'],odd:2,why:'enero = maand; de rest = dagen'},
   {words:['primavera','verano','otoño','domingo'],odd:3,why:'domingo = dag; de rest = seizoenen'},
   {words:['desayunar','ducharse','levantarse','acostarse'],odd:0,why:'desayunar is NIET reflexief'},
   {words:['siempre','a veces','nunca','reloj'],odd:3,why:'reloj = voorwerp, geen frecuentie'},
   {words:['el desayuno','la comida','la cena','el instituto'],odd:3,why:'instituto is geen maaltijd'},
   {words:['empezar','querer','preferir','desayunar'],odd:3,why:'desayunar is regelmatig; de rest e>ie'},
   {words:['dormir','poder','volver','pedir'],odd:3,why:'pedir = e>i; de rest o>ue'},
   {words:['la mañana','la tarde','la noche','el verano'],odd:3,why:'verano = seizoen; de rest = dagdeel'}]});
 // ---------- LECTURA ----------
 buildOrder('lx_order',{title:'Ordena el día de Pau',desc:'Tik de acties in de juiste volgorde van de dag.',rounds:[
   {sub:'la rutina de la mañana',items:[{label:'Me despierto',key:1},{label:'Me levanto',key:2},{label:'Me ducho',key:3},{label:'Desayuno',key:4},{label:'Salgo de casa',key:5}]},
   {sub:'el día de Pau (completo)',items:[{label:'Voy al instituto',key:1},{label:'Las clases empiezan',key:2},{label:'Almuerzo con amigos',key:3},{label:'Hago los deberes',key:4},{label:'Me acuesto',key:5}]},
   {sub:'las comidas del día',items:[{label:'el desayuno',key:1},{label:'la comida',key:2},{label:'la merienda',key:3},{label:'la cena',key:4}]},
   {sub:'las horas (temprano → tarde)',items:[{label:'las siete',key:1},{label:'las nueve',key:2},{label:'las dos',key:3},{label:'las once',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in het blog van Pau en kies het juiste antwoord.',per:6,pool:[
   {q:'¿A qué hora se despierta Pau?',opts:['a las siete','a las ocho','a las diez'],ans:'a las siete',why:'«Me despierto a las siete»'},
   {q:'¿Cómo va Pau al instituto?',opts:['en metro','en coche','a pie'],ans:'en metro',why:'«voy al instituto en metro»'},
   {q:'¿A qué hora empiezan las clases?',opts:['a las nueve','a las ocho','a las diez'],ans:'a las nueve',why:'«empiezan a las nueve»'},
   {q:'¿Dónde almuerza Pau?',opts:['en el instituto','en casa','en un bar'],ans:'en el instituto',why:'«almuerzo en el instituto»'},
   {q:'¿Qué hace Pau por la tarde?',opts:['los deberes','duerme','va al insti'],ans:'los deberes',why:'«hago los deberes»'},
   {q:'¿A qué hora cena Pau?',opts:['a las nueve','a las siete','a las once'],ans:'a las nueve',why:'«Ceno con mi familia a las nueve»'},
   {q:'¿A qué hora se acuesta Pau?',opts:['a las once','a las nueve','a las diez'],ans:'a las once',why:'«me acuesto a las once»'},
   {q:'¿A qué hora se levanta los sábados?',opts:['a las diez','a las siete','a las ocho'],ans:'a las diez',why:'«los sábados… ¡me levanto a las diez!»'}]});
}

renderFC();renderTable();gameHora();gameDePor();gameRaiz();renderLectura();buildRecorders();buildInlineExercises();
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='U3_web_mijn_versie.html';a.click();};
})();
"""

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/U3_web.html","w").write(html)
print("U3_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
