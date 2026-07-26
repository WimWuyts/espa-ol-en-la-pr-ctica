#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C5 · U1 «¿Quién eres?».
# Eén standalone bestand: fonts base64, de 24 U1-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U1-vocab), visuele/interactieve grammatica (ser · presente · interrogativos · el/la),
# klikbare kaart (mundo hispano) + TTS + editbar. Zelfde pijplijn/huisstijl als U0-hub (groen).
import json, base64, os, sys
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
GEN = f"{ROOT}/02-huisstijl/beeld/generators"
sys.path.insert(0, GEN); import cast_gen as C; import vocab_icons as VI; import vocab_emoji as VE
vocab = json.load(open(f"{ROOT}/01-cursussen/05-a1/U1/u1_vocab.json", encoding="utf-8"))
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

# ---- de 24 U1-motor-spellen: gegroepeerd (receptief -> productief) + base64 ingebed ----
MOTOR = [
 ['① Reconocer · woordenschat', [
   ['pais-nacionalidad', 'país ↔ nacionalidad', 'match'],
   ['datos-memoria', 'memoria de los datos', 'memory'],
   ['bandera-pais', 'banderas ↔ país', 'memory']]],
 ['② Distinguir · gramática', [
   ['ser-tener', '¿ser o tener?', 'classify'],
   ['ser-persona', 'el verbo SER', 'classify'],
   ['ar-er-ir', '-ar · -er · -ir', 'classify'],
   ['genero-articulo', '¿el o la?', 'classify'],
   ['mayuscula-minuscula', '¿mayúscula o minúscula?', 'classify']]],
 ['③ Producir con apoyo', [
   ['verbo-cloze', 'completa el verbo (ser+presente)', 'cloze'],
   ['interrogativos', 'palabras interrogativas', 'cloze'],
   ['un-una', '¿un o una?', 'cloze'],
   ['que-verbo', '¿qué verbo?', 'cloze'],
   ['presente-regular', 'presente Tetris', 'tetris'],
   ['tonica-datos', 'la tónica de los datos', 'tap'],
   ['presentacion-orden', 'ordena la presentación', 'order']]],
 ['④ Analizar & comunicar', [
   ['caza-mayusculas', 'caza de mayúsculas', 'point'],
   ['senala-hispano', 'señala el mundo hispano', 'point'],
   ['pregunta-respuesta', 'pregunta ↔ respuesta', 'match'],
   ['presentate', '¡Preséntate!', 'sim']]],
 ['⑤ Hablar · grábate 🎙️', [
   ['repite-presentacion', 'escucha y repite', 'speak'],
   ['shadowing-lucia', 'shadowing con Lucía', 'speak'],
   ['carrusel-presentate', 'carrusel: preséntate', 'speak'],
   ['mensaje-de-voz', 'mensaje de voz', 'speak'],
   ['describe-persona', 'describe a un personaje', 'speak']]],
]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-u1-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-u1-{s}.html")}

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
/* ---- inline zelfcorrigerende oefeningen (U5-model) ---- */
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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="datos">datos personales</option><option value="ficha">la ficha</option><option value="interrog">interrogativos</option><option value="saludos">saludos</option><option value="pais">mundo hispano</option><option value="mundo">países del mundo</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Español en la práctica · U1 ¿Quién eres?</title>
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
    <div><h1>U1 · ¿Quién eres?</h1>
    <p>La página digital de la Unidad 1 (parada <b>Madrid · Lucía</b>): flashcards, gramática visual e interactiva, <b>24 juegos</b> con muchas series y <b>más de 100 ejercicios</b> con autocorrección. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U1. Klik om te draaien; wissel ES↔NL; filter per groep; klik 🔊 om te horen. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
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
    <p class="lead">Eerst betekenis en patroon ontdekken, dan de regel. Beweeg over de woorden, klik, en probeer. <span class="gloss">Alles binnen het thema van U1: presentarse, ser, presente en el/la.</span></p>
    <div class="card" id="colorsent"></div>
    <div class="card" id="serconj"></div>
    <h3 class="subh">🧱 Preséntate — construye la frase</h3>
    <div class="card ex" id="gx_build"></div>
    <h3 class="subh">⚖️ ¿ser o tener? — la forma correcta</h3>
    <div class="card ex" id="gx_serq"></div>
    <h3 class="subh">✍️ Presente regular — completa el verbo (-ar · -er · -ir)</h3>
    <div class="card ex" id="gx_presente"></div>
    <h3 class="subh">❓ Palabras interrogativas — ¿qué preguntas?</h3>
    <div class="game" id="g_interrog"></div>
    <div class="card ex" id="gx_interrog"></div>
    <h3 class="subh">🔤 El género — ¿el o la?</h3>
    <div class="game" id="g_ella"></div>
    <div class="card ex" id="gx_gen"></div>
    <h3 class="subh">🌍 País ↔ nacionalidad</h3>
    <div class="card ex" id="gx_pais"></div>
    <h3 class="subh">🎯 Repaso mixto — rellena con feedback</h3>
    <div class="card ex" id="gx_mix"></div>
  </section>

  <section class="panel" data-p="lectura">
    <h2 class="sec">Lectura · dos perfiles</h2>
    <p class="lead">Lees de twee profielen, <b>luister</b> ze (🔊 TTS) en <b>controleer je begrip</b>. Daarna reageer je met een eigen bericht — dat neem je op in het tabblad <b>Hablar</b>. <span class="gloss">Keten: lezen → luisteren → spreken.</span></p>
    <div id="lecturawrap"></div>
    <h3 class="subh">🔢 Ordena la presentación</h3>
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
    <div class="card" id="rec_repite"></div>
    <div class="card" id="rec_carrusel"></div>
    <div class="card" id="rec_mensaje"></div>
    <p class="lead" style="margin-top:8px">Meer spreek-/opnamespellen (shadowing, describe…) vind je ook onder <b>Juegos ⑤</b>.</p>
  </section>

  <section class="panel" data-p="cultura">
    <h2 class="sec">Cultura · Los dos apellidos y el tú/usted</h2>
    <p class="lead">En el mundo hispano la gente tiene <b>dos apellidos</b> y trata de <b>tú</b> o de <b>usted</b> según la situación. <span class="gloss">In de Spaanstalige wereld heeft men twee achternamen en spreekt men iemand aan met tú of usted, naargelang de situatie.</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>Los dos apellidos</h3>
      <p><b>Lucía Ramírez García</b> = Ramírez (del padre) + García (de la madre). Al casarse, el apellido <b>no cambia</b>. <span class="gloss">Iedereen draagt de achternaam van vader én moeder; bij een huwelijk verandert de naam niet. Nederlands heeft één achternaam — hier twee.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>¿Tú o usted?</h3>
      <p><b>tú</b> (¿Cómo estás? · tú eres) met een leeftijdsgenoot ↔ <b>usted</b> (¿Cómo está usted? · usted es) beleefd/formeel. <span class="gloss">España: veel tú ↔ Colombia/Perú: vaak usted. Vooruitblik: in C6 ontmoet je Mateo uit Argentina met vos.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Madrid · el corazón de España 🐻🌳</h3>
      <p><b>ES:</b> Madrid es la <b>capital</b> y la ciudad más grande de España. En la <b>Puerta del Sol</b> está el <b>Kilómetro 0</b>, el punto de donde salen todas las carreteras del país. El símbolo de la ciudad es <b>el oso y el madroño</b> 🐻🌳. <span class="gloss">Madrid is de hoofdstad; op de Puerta del Sol ligt «Kilometer 0», het startpunt van alle wegen. Het symbool is de beer met de aardbeiboom.</span></p></div>
    <h3 class="subh">📍 La Ruta · ¿dónde estamos?</h3>
    <p class="lead">Onze parada 1: <b>Madrid</b> 🇪🇸, hoofdstad van España. <b>Klik op een groen land</b> op de kaart voor info. Verderop: México → Colombia → Perú.</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een groen land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    <h2 class="sec">Extra · bronnen</h2>
    <p class="lead">Externe uitleg &amp; oefeningen (de leerkracht vult de links aan).</p>
    <div class="card"><p>🎬 <b>profedeele</b> (YouTube — ser / presente / interrogativos) — <span class="gloss">link volgt.</span></p>
    <p>🧩 <b>arche-ele</b> (Genially — datos personales / países) — <span class="gloss">link volgt.</span></p>
    <p>📄 In het boek (PDF) verwijzen de QR-codes naar déze pagina, op het juiste ankerpunt.</p></div>
  </section>

  <div class="foot">Español en la práctica · C5 · Unidad 1 «¿Quién eres?» — página digital. Uitbreiding op de PDF · huisstijl groen · print ↔ PowerPoint ↔ web.</div>
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
    const sp=d.querySelector('.spk');if(sp)sp.onclick=e=>{e.stopPropagation();speak(v.es.replace(/→.*/,''));};
    g.appendChild(d);});
  document.getElementById('fccount').textContent=n+' woorden';}
function renderTable(){const q=(document.getElementById('vsearch').value||'').toLowerCase();const b=document.getElementById('vbody');b.innerHTML='';let n=0;
  VOCAB.forEach(v=>{if(q&&!(v.es.toLowerCase().includes(q)||v.nl.toLowerCase().includes(q)||v.ej.toLowerCase().includes(q)))return;n++;
    const tr=document.createElement('tr');tr.innerHTML='<td><b>'+v.es+'</b></td><td>'+v.nl+'</td><td>'+v.soort+'</td><td class="gloss">'+v.ej+'</td>';b.appendChild(tr);});
  document.getElementById('vcount').textContent=n+' items';}

function scoreBar(id){return '<div class="scorebar" id="'+id+'"><span>Punten: <b class="pt">0</b></span><span>Reeks: <b class="st">0</b></span></div>'}
function setScore(el,pt,st){el.querySelector('.pt').textContent=pt;el.querySelector('.st').textContent=st}
function feedback(el,ok,msg){el.className='fb '+(ok?'good':'bad');el.innerHTML=(ok?'✅ ':'❌ ')+msg}

// ---- GRAMMAR-VIZ 1: kleurgecodeerde presentarse-zin ----
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Presentarse — beweeg over de woorden</h3>'+
'<div class="csent">'+
'<span style="background:#dbeafe;color:#1e40af">Yo<span class="tip">persoon (onderwerp)</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">me llamo<span class="tip">werkwoord · llamarse</span></span> '+
'<span style="background:#dcfce7;color:#166534">Leo<span class="tip">naam</span></span>, '+
'<span style="background:#fed7aa;color:#9a3412">soy<span class="tip">werkwoord · ser</span></span> '+
'<span style="background:#ccfbf1;color:#0f766e">de Bélgica<span class="tip">plaats · afkomst</span></span> y '+
'<span style="background:#fed7aa;color:#9a3412">tengo<span class="tip">werkwoord · tener (leeftijd!)</span></span> '+
'<span style="background:#ede9fe;color:#5b21b6">15 años<span class="tip">tijd/leeftijd</span></span>.</div>'+
'<div class="legend"><span><i style="background:#93c5fd"></i>persoon</span><span><i style="background:#fdba74"></i>werkwoord</span><span><i style="background:#86efac"></i>naam/voorwerp</span><span><i style="background:#5eead4"></i>plaats</span><span><i style="background:#c4b5fd"></i>tijd/leeftijd</span></div>'+
'<p class="gloss" style="margin-top:8px">🔴 <b>tengo</b> 15 años — leeftijd met <b>tener</b>, niet met <i>ser</i>! · '+(TTS?'<button class="spk-btn" onclick="speak(\'Yo me llamo Leo, soy de Bélgica y tengo quince años\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: SER — klik om de vorm te onthullen ----
(function(){const el=document.getElementById('serconj');
 const R=[['yo','soy'],['tú','eres'],['él/ella/usted','es'],['nosotros/-as','somos'],['vosotros/-as','sois'],['ellos/-as/ustedes','son']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">El verbo SER — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">Denk eerst zelf de vorm; klik dan de kaart. 🔊 om te horen.</p><div class="conjgrid" id="scg"></div>';
 const g=el.querySelector('#scg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v;if(TTS)speak(p.split('/')[0]+' '+v);};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: interrogativos matcher (klik vraag → antwoordtype) ----
function gameInterrog(){const el=document.getElementById('g_interrog');
 const items=[['¿Cómo te llamas?','nombre'],['¿De dónde eres?','origen'],['¿Cuántos años tienes?','edad'],['¿Dónde vives?','ciudad'],['¿Cuál es tu correo?','dato'],['¿Quién es ella?','persona']];
 const cats=['nombre','origen','edad','ciudad','dato','persona'];let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿Qué pregunta pide qué?</h3><p class="desc">Lees de vraag en kies wát ze vraagt.</p>'+scoreBar('sbI')+'<div id="iQ" style="font-size:20px;font-family:var(--disp);text-align:center;margin:10px 0"></div><div class="chips" id="iC" style="justify-content:center"></div><div class="fb" id="iFb"></div>';
 const sb=el.querySelector('#sbI');const cont=el.querySelector('#iC');
 cats.forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#iQ').textContent=el.cur[0];el.querySelector('#iFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#iFb'),ok,(ok?'¡Sí! ':'Nee → ')+'«'+el.cur[0]+'» pide: '+el.cur[1]+'.');setTimeout(next,950);}
 next();}
// ---- GRAMMAR-VIZ 4: ¿el o la? ----
function gameElla(){const el=document.getElementById('g_ella');
 const items=[['nombre','el'],['ciudad','la'],['país','el'],['dirección','la'],['idioma','el'],['edad','la'],['correo','el'],['nacionalidad','la'],['apellido','el'],['firma','la']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿el o la?</h3><p class="desc">Kies het juiste lidwoord. Let op de valstrik: <b>el</b> idioma, <b>el</b> país.</p>'+scoreBar('sbE')+'<div id="eW" style="font-size:26px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._ellaG(\'el\')">el</div><div class="chip" onclick="window._ellaG(\'la\')">la</div></div><div class="fb" id="eFb"></div>';
 const sb=el.querySelector('#sbE');
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#eW').textContent=el.cur[0];el.querySelector('#eFb').className='fb';}
 window._ellaG=k=>{const ok=k===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#eFb'),ok,(ok?'¡Sí! ':'Nee → ')+el.cur[1]+' '+el.cur[0]);setTimeout(next,850);};
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
  ESP:{fl:'🇪🇸',n:'España',cap:'Madrid',f:'Onze parada 1: Madrid, de hoofdstad. Vertrekpunt van La Ruta.',nl:'Parada 1 · Madrid (Lucía).',star:1},
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

// init
// ---------- LECTURA: perfiles + TTS + begrip ----------
function renderLectura(){const el=document.getElementById('lecturawrap');if(!el)return;
 const P=[{n:'Lucía',fr:'Sevilla 🇪🇸',t:'¡Hola! Me llamo <span class="ev">Lucía Ramírez García</span>. Soy de <span class="ev">Sevilla</span>, en el sur de España, y tengo <span class="ev">16 años</span>. Vivo en el <span class="ev">centro</span> de la ciudad. Estudio en un instituto y hablo <span class="ev">español e inglés</span>. Me gusta la música y viajar. Busco un amigo o una amiga para hablar español. ¿Y tú, quién eres?'},
  {n:'Diego',fr:'CDMX 🇲🇽',t:'¡Qué onda! Soy <span class="ev">Diego Hernández</span>, de <span class="ev">Ciudad de México</span>. Tengo <span class="ev">15 años</span> y vivo con mi familia. Mi nacionalidad es <span class="ev">mexicana</span>. Hablo <span class="ev">español</span> y un poco de <span class="ev">inglés</span>. Me encanta la comida y el fútbol. Quiero conocer gente de Europa. ¡Escríbeme!'}];
 const strip=h=>h.replace(/<[^>]+>/g,'');
 el.innerHTML='<div class="perfiles">'+P.map((p,i)=>'<div class="perfil"><h4>👤 '+p.n+' <span class="gloss" style="font-size:12px;font-weight:400">· '+p.fr+'</span> '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lx'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div class="txt" id="lx'+i+'" data-raw="'+strip(p.t).replace(/"/g,'&quot;')+'">'+p.t+'</div></div>').join('')+'</div>';
 // V/F begripstaak
 const items=[['Lucía tiene 16 años.',true,'«tengo 16 años»'],['Diego es de España.',false,'Diego es de México (CDMX)'],['Los dos hablan inglés.',true,'Lucía: inglés · Diego: un poco de inglés'],['A Diego le gusta la música.',false,'a Diego le gusta la comida y el fútbol'],['Lucía vive en el sur de España.',true,'«Sevilla, en el sur de España»'],['Diego es mayor que Lucía.',false,'Diego 15 · Lucía 16 → Lucía es mayor'],['La nacionalidad de Diego es mexicana.',true,'«Mi nacionalidad es mexicana»'],['Lucía busca a alguien para hablar español.',true,'«Busco un amigo… para hablar español»']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — comprueba tu comprensión (con evidencia)</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Responde</h3><p class="gloss" style="margin:0 0 8px">Kies één profiel en stel jezelf voor in een antwoordbericht. Neem het op onder <b>Hablar 🎙️</b> («mensaje de voz»).</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="¡Hola! Me llamo…"></textarea>';
 el.appendChild(box);el.appendChild(resp);}

// ---------- INLINE RECORDER (MediaRecorder, draait in de hub-origin) ----------
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
 makeRecorder('rec_repite',{title:'Escucha y repite',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'Me llamo Leo.',cue:'nombre',tip:'Duidelijk uitspreken? Probeer nog eens.'},{text:'Soy de Bélgica.',cue:'origen'},{text:'Tengo 15 años.',cue:'edad'},{text:'Vivo en Gante y hablo español.',cue:'ciudad · idiomas'}]});
 makeRecorder('rec_carrusel',{title:'Carrusel: preséntate',desc:'Eén element wisselt per ronde. Bouw de zin, spreek ze in.',items:[
   {text:'Me llamo Sara, soy de Bélgica y tengo 14 años.',cue:'ronde 1'},{text:'Me llamo Tom, soy de Amberes y tengo 16 años.',cue:'ronde 2'},{text:'Me llamo… , soy de… y tengo… años.',cue:'jouw versie'}]});
 makeRecorder('rec_mensaje',{title:'Mensaje de voz',desc:'Neem één bericht op. Ontvanger: Lucía/Diego · Doel: jezelf voorstellen. Gebruik: me llamo · soy de · tengo … años.',items:[
   {text:'Preséntate a Lucía o a Diego en un mensaje de voz (30 s).',cue:'para · Lucía / Diego',tip:'Heb je nombre + origen + edad + idiomas gezegd? Neem opnieuw op.'}]});
}

// ================= INLINE ZELFCORRIGERENDE OEFENINGEN (U5-model) =================
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

function buildInlineExercises(){
 // ---------------- GRAMÁTICA ----------------
 buildOrder('gx_build',{title:'Construye: preséntate',desc:'Tik de blokjes in de juiste volgorde (onderwerp → werkwoord → rest).',rounds:[
   {sub:'nombre',items:[{label:'Yo',key:1},{label:'me llamo',key:2},{label:'Lucía',key:3}]},
   {sub:'origen',items:[{label:'Yo',key:1},{label:'soy',key:2},{label:'de',key:3},{label:'Bélgica',key:4}]},
   {sub:'edad · tener',items:[{label:'Yo',key:1},{label:'tengo',key:2},{label:'quince',key:3},{label:'años',key:4}]},
   {sub:'vivir',items:[{label:'Yo',key:1},{label:'vivo',key:2},{label:'en',key:3},{label:'Gante',key:4}]},
   {sub:'pregunta',items:[{label:'¿De',key:1},{label:'dónde',key:2},{label:'eres',key:3},{label:'tú?',key:4}]},
   {sub:'idiomas',items:[{label:'Yo',key:1},{label:'hablo',key:2},{label:'español',key:3},{label:'e inglés',key:4}]}]});
 buildChoice('gx_serq',{title:'¿ser o tener? — mini-quiz',desc:'Kies de juiste vorm. ¡Ojo! leeftijd = tener, niet ser.',per:6,pool:[
   {q:'(Yo) ___ de Bélgica.',opts:['soy','tengo','es'],ans:'soy',why:'origen → ser: yo soy'},
   {q:'(Yo) ___ quince años.',opts:['tengo','soy','tienes'],ans:'tengo',why:'edad → tener: yo tengo'},
   {q:'¿(Tú) ___ de España?',opts:['eres','tienes','soy'],ans:'eres',why:'origen → ser: tú eres'},
   {q:'¿Cuántos años ___ (tú)?',opts:['tienes','eres','tiene'],ans:'tienes',why:'edad → tener: tú tienes'},
   {q:'Lucía ___ de Sevilla.',opts:['es','tiene','eres'],ans:'es',why:'origen → ser: él/ella es'},
   {q:'Diego ___ dieciséis años.',opts:['tiene','es','tienes'],ans:'tiene',why:'edad → tener: él/ella tiene'},
   {q:'(Nosotros) ___ estudiantes.',opts:['somos','tenemos','sois'],ans:'somos',why:'ser: nosotros somos'},
   {q:'(Nosotros) ___ un examen hoy.',opts:['tenemos','somos','tienen'],ans:'tenemos',why:'tener: nosotros tenemos'},
   {q:'Ellos ___ mexicanos.',opts:['son','tienen','somos'],ans:'son',why:'ser: ellos son'},
   {q:'Mis amigos ___ catorce años.',opts:['tienen','son','tenéis'],ans:'tienen',why:'tener: ellos tienen'},
   {q:'¿(Vosotros) ___ de aquí?',opts:['sois','tenéis','son'],ans:'sois',why:'ser: vosotros sois'},
   {q:'Yo ___ un hermano.',opts:['tengo','soy','tienes'],ans:'tengo',why:'bezit → tener: yo tengo'}]});
 buildChoice('gx_presente',{title:'Presente regular — completa el verbo',desc:'Kies de juiste vorm van het werkwoord tussen haakjes (-ar · -er · -ir).',per:6,pool:[
   {q:'(Yo) ___ español. (hablar)',opts:['hablo','hablas','habla'],ans:'hablo',why:'-ar · yo → -o: hablo'},
   {q:'(Tú) ___ en un instituto. (estudiar)',opts:['estudias','estudio','estudia'],ans:'estudias',why:'-ar · tú → -as: estudias'},
   {q:'Lucía ___ en Sevilla. (vivir)',opts:['vive','vives','vivo'],ans:'vive',why:'-ir · él/ella → -e: vive'},
   {q:'(Nosotros) ___ español este año. (aprender)',opts:['aprendemos','aprendéis','aprenden'],ans:'aprendemos',why:'-er · nosotros → -emos'},
   {q:'(Yo) ___ en Gante. (vivir)',opts:['vivo','vives','vive'],ans:'vivo',why:'-ir · yo → -o: vivo'},
   {q:'Mi madre ___ en Bruselas. (trabajar)',opts:['trabaja','trabajo','trabajas'],ans:'trabaja',why:'-ar · él/ella → -a'},
   {q:'(Ellos) ___ tres idiomas. (hablar)',opts:['hablan','habláis','hablamos'],ans:'hablan',why:'-ar · ellos → -an'},
   {q:'¿(Tú) ___ neerlandés? (aprender)',opts:['aprendes','aprende','aprendo'],ans:'aprendes',why:'-er · tú → -es'},
   {q:'(Vosotros) ___ en Amberes. (vivir)',opts:['vivís','vivimos','viven'],ans:'vivís',why:'-ir · vosotros → -ís'},
   {q:'(Nosotros) ___ mucho. (estudiar)',opts:['estudiamos','estudiáis','estudian'],ans:'estudiamos',why:'-ar · nosotros → -amos'},
   {q:'(Yo) ___ inglés. (aprender)',opts:['aprendo','aprende','aprendes'],ans:'aprendo',why:'-er · yo → -o'},
   {q:'Diego ___ fútbol. (practicar)',opts:['practica','practico','practican'],ans:'practica',why:'-ar · él/ella → -a'}]});
 buildChoice('gx_interrog',{title:'Palabras interrogativas — completa',desc:'Kies het juiste vraagwoord. Let op accenten en de betekenis.',per:6,pool:[
   {q:'¿___ te llamas? — Me llamo Leo.',opts:['Cómo','Dónde','Cuántos'],ans:'Cómo',why:'naam vragen → ¿Cómo te llamas?'},
   {q:'¿De ___ eres? — Soy de Bélgica.',opts:['dónde','cómo','qué'],ans:'dónde',why:'herkomst → ¿De dónde eres?'},
   {q:'¿___ años tienes? — Tengo 15.',opts:['Cuántos','Cuál','Quién'],ans:'Cuántos',why:'aantal → ¿Cuántos años tienes?'},
   {q:'¿___ vives? — Vivo en Gante.',opts:['Dónde','Cómo','Qué'],ans:'Dónde',why:'plaats → ¿Dónde vives?'},
   {q:'¿___ es tu correo? — leo@mail.com',opts:['Cuál','Cómo','Dónde'],ans:'Cuál',why:'gegeven kiezen → ¿Cuál es…?'},
   {q:'¿___ es ella? — Es Lucía.',opts:['Quién','Qué','Cómo'],ans:'Quién',why:'persoon → ¿Quién es?'},
   {q:'¿___ idiomas hablas? — Dos.',opts:['Cuántos','Cuál','Cómo'],ans:'Cuántos',why:'aantal → ¿Cuántos…?'},
   {q:'¿___ estudias? — Español.',opts:['Qué','Quién','Dónde'],ans:'Qué',why:'ding/zaak → ¿Qué estudias?'},
   {q:'¿___ está usted? — Muy bien.',opts:['Cómo','Cuál','Quién'],ans:'Cómo',why:'toestand → ¿Cómo está?'},
   {q:'¿___ es tu número de teléfono?',opts:['Cuál','Qué','Dónde'],ans:'Cuál',why:'gegeven → ¿Cuál es…?'},
   {q:'¿De ___ país eres?',opts:['qué','dónde','cuál'],ans:'qué',why:'¿De qué país…? = welk land'},
   {q:'¿___ trabaja tu padre? — En Bruselas.',opts:['Dónde','Cómo','Cuántos'],ans:'Dónde',why:'plaats → ¿Dónde trabaja?'}]});
 buildChoice('gx_gen',{title:'El género — ¿el o la?',desc:'Kies het juiste lidwoord. Let op de valstrikken: el idioma, el país, la nacionalidad.',per:6,pool:[
   {q:'___ nombre',opts:['el','la'],ans:'el',why:'el nombre (m)'},
   {q:'___ ciudad',opts:['la','el'],ans:'la',why:'la ciudad (f)'},
   {q:'___ país',opts:['el','la'],ans:'el',why:'el país (m) — valstrik!'},
   {q:'___ dirección',opts:['la','el'],ans:'la',why:'la dirección (f, -ción)'},
   {q:'___ idioma',opts:['el','la'],ans:'el',why:'el idioma (m) — valstrik, eindigt op -a!'},
   {q:'___ edad',opts:['la','el'],ans:'la',why:'la edad (f)'},
   {q:'___ correo',opts:['el','la'],ans:'el',why:'el correo (m)'},
   {q:'___ nacionalidad',opts:['la','el'],ans:'la',why:'la nacionalidad (f, -dad)'},
   {q:'___ apellido',opts:['el','la'],ans:'el',why:'el apellido (m)'},
   {q:'___ firma',opts:['la','el'],ans:'la',why:'la firma (f)'},
   {q:'___ teléfono',opts:['el','la'],ans:'el',why:'el teléfono (m)'},
   {q:'___ fecha',opts:['la','el'],ans:'la',why:'la fecha (f)'}]});
 buildMatch('gx_pais',{title:'País ↔ nacionalidad',desc:'Koppel het land aan de juiste nationaliteit (m/v-vorm hier: standaard).',per:6,pool:[
   {a:'España',b:'español / española'},{a:'México',b:'mexicano / mexicana'},{a:'Colombia',b:'colombiano / colombiana'},
   {a:'Perú',b:'peruano / peruana'},{a:'Argentina',b:'argentino / argentina'},{a:'Bélgica',b:'belga'},
   {a:'Chile',b:'chileno / chilena'},{a:'Cuba',b:'cubano / cubana'},{a:'Alemania',b:'alemán / alemana'},
   {a:'Francia',b:'francés / francesa'},{a:'Portugal',b:'portugués / portuguesa'},{a:'Ecuador',b:'ecuatoriano / ecuatoriana'}]});
 buildChoice('gx_mix',{title:'Repaso mixto — rellena',desc:'Alles door elkaar: ser · tener · presente · interrogativos · el/la.',per:8,pool:[
   {q:'(Yo) ___ de Bélgica.',opts:['soy','tengo','es'],ans:'soy',why:'origen → ser'},
   {q:'¿___ te llamas?',opts:['Cómo','Dónde','Cuál'],ans:'Cómo',why:'naam → ¿Cómo te llamas?'},
   {q:'Lucía ___ dieciséis años.',opts:['tiene','es','tienes'],ans:'tiene',why:'edad → tener'},
   {q:'(Yo) ___ en Gante. (vivir)',opts:['vivo','vives','vive'],ans:'vivo',why:'-ir · yo → -o'},
   {q:'___ idioma',opts:['el','la'],ans:'el',why:'el idioma (m) — valstrik'},
   {q:'¿De ___ eres?',opts:['dónde','cómo','qué'],ans:'dónde',why:'herkomst → ¿De dónde eres?'},
   {q:'(Nosotros) ___ español. (hablar)',opts:['hablamos','habláis','hablan'],ans:'hablamos',why:'-ar · nosotros'},
   {q:'Diego es ___ (México).',opts:['mexicano','español','belga'],ans:'mexicano',why:'México → mexicano'},
   {q:'¿___ años tienes?',opts:['Cuántos','Cuál','Quién'],ans:'Cuántos',why:'aantal → ¿Cuántos…?'},
   {q:'___ ciudad',opts:['la','el'],ans:'la',why:'la ciudad (f)'},
   {q:'(Ellos) ___ estudiantes.',opts:['son','están','tienen'],ans:'son',why:'ser: ellos son'},
   {q:'(Tú) ___ en un instituto. (estudiar)',opts:['estudias','estudio','estudia'],ans:'estudias',why:'-ar · tú → -as'}]});
 // ---------------- VOCABULARIO ----------------
 buildMatch('vx_match',{title:'Empareja: país ↔ bandera',desc:'Koppel het land aan de juiste vlag.',per:6,pool:[
   {a:'España',b:'🇪🇸'},{a:'México',b:'🇲🇽'},{a:'Colombia',b:'🇨🇴'},{a:'Perú',b:'🇵🇪'},
   {a:'Argentina',b:'🇦🇷'},{a:'Bélgica',b:'🇧🇪'},{a:'Chile',b:'🇨🇱'},{a:'Cuba',b:'🇨🇺'},
   {a:'Alemania',b:'🇩🇪'},{a:'Francia',b:'🇫🇷'},{a:'Portugal',b:'🇵🇹'},{a:'Ecuador',b:'🇪🇨'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat in de zin past (datos personales).',per:6,pool:[
   {q:'¿Cuál es tu ___? — Mi nombre es Leo.',opts:['nombre','edad','ciudad'],ans:'nombre',why:'nombre = voornaam'},
   {q:'Mi ___ es García.',opts:['apellido','idioma','firma'],ans:'apellido',why:'apellido = achternaam'},
   {q:'Tengo catorce ___.',opts:['años','ciudad','país'],ans:'años',why:'tener … años'},
   {q:'Vivo en una ___ pequeña.',opts:['ciudad','edad','firma'],ans:'ciudad',why:'ciudad = stad'},
   {q:'Mi ___ es leo@mail.com.',opts:['correo','teléfono','número'],ans:'correo',why:'correo electrónico'},
   {q:'Hablo tres ___.',opts:['idiomas','años','países'],ans:'idiomas',why:'idioma = taal'},
   {q:'Rellena la ___ con tus datos.',opts:['ficha','edad','firma'],ans:'ficha',why:'la ficha = fiche'},
   {q:'Mi ___ es belga.',opts:['nacionalidad','dirección','curso'],ans:'nacionalidad',why:'nacionalidad'},
   {q:'¿De qué ___ eres? — De España.',opts:['país','idioma','curso'],ans:'país',why:'país = land'},
   {q:'___ aquí, por favor. (tu nombre)',opts:['Firma','Vivo','Hablo'],ans:'Firma',why:'firmar = tekenen'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het juiste woord.',per:6,pool:[
   {q:'El número de años que tienes:',opts:['la edad','el nombre','el país'],ans:'la edad',why:'edad = leeftijd'},
   {q:'La lengua que hablas:',opts:['el idioma','la ciudad','la firma'],ans:'el idioma',why:'idioma = taal'},
   {q:'Tu nombre de familia:',opts:['el apellido','el correo','el curso'],ans:'el apellido',why:'apellido'},
   {q:'El territorio donde naces (España, México…):',opts:['el país','la calle','la edad'],ans:'el país',why:'país = land'},
   {q:'Dónde vives (Madrid, Gante…):',opts:['la ciudad','el idioma','la firma'],ans:'la ciudad',why:'ciudad = stad'},
   {q:'Tu correo con @:',opts:['el correo electrónico','el teléfono','la fecha'],ans:'el correo electrónico',why:'e-mail'},
   {q:'Tu nombre escrito a mano al final:',opts:['la firma','el número','la edad'],ans:'la firma',why:'firma = handtekening'},
   {q:'Español, belga, mexicano… es tu:',opts:['nacionalidad','apellido','ciudad'],ans:'nacionalidad',why:'nacionalidad'},
   {q:'El país donde vive Lucía:',opts:['España','México','Bélgica'],ans:'España',why:'Lucía es de Sevilla, España'},
   {q:'La calle y el número donde vives:',opts:['la dirección','el correo','la firma'],ans:'la dirección',why:'dirección = adres'},
   {q:'El año, mes y día en que naces:',opts:['la fecha de nacimiento','el código postal','el curso'],ans:'la fecha de nacimiento',why:'geboortedatum'},
   {q:'El verbo para decir tu nombre:',opts:['llamarse','vivir','hablar'],ans:'llamarse',why:'me llamo…'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['España','México','Perú','español'],odd:3,why:'«español» = idioma/nacionalidad, geen país'},
   {words:['¿Cómo?','¿Dónde?','¿Cuántos?','vivo'],odd:3,why:'«vivo» is geen interrogativo'},
   {words:['soy','eres','es','tengo'],odd:3,why:'«tengo» is van tener; de rest is ser'},
   {words:['hablar','estudiar','trabajar','vivir'],odd:3,why:'«vivir» is -ir; de rest -ar'},
   {words:['el nombre','el apellido','la edad','la firma'],odd:2,why:'la edad ≠ deel van je naam'},
   {words:['belga','español','mexicano','país'],odd:3,why:'«país» is geen nacionalidad'},
   {words:['la ciudad','el país','la dirección','el idioma'],odd:3,why:'el idioma ≠ plaats/adres'},
   {words:['tengo','tienes','tiene','soy'],odd:3,why:'«soy» is van ser; de rest tener'},
   {words:['¿Cómo?','¿Dónde?','¿De dónde?','porque'],odd:3,why:'«porque» is geen vraagwoord'},
   {words:['hablo','estudio','vivo','tengo'],odd:3,why:'«tengo» = tener; de rest is regelmatig presente (yo)'},
   {words:['Madrid','Sevilla','Barcelona','España'],odd:3,why:'España = país; de rest zijn steden'},
   {words:['español','francés','inglés','belga'],odd:3,why:'«belga» = nacionalidad, geen idioma'}]});
 // ---------------- LECTURA ----------------
 buildOrder('lx_order',{title:'Ordena la presentación',desc:'Tik de blokjes in een logische volgorde.',rounds:[
   {sub:'una presentación completa',items:[{label:'¡Hola! Me llamo Sara',key:1},{label:'Soy de Bélgica',key:2},{label:'Tengo 15 años',key:3},{label:'Hablo español e inglés',key:4}]},
   {sub:'la conversación',items:[{label:'¿Cómo te llamas?',key:1},{label:'Me llamo Diego',key:2},{label:'¿De dónde eres?',key:3},{label:'Soy de México',key:4}]},
   {sub:'la ficha personal',items:[{label:'Nombre',key:1},{label:'Apellido',key:2},{label:'Fecha de nacimiento',key:3},{label:'Firma',key:4}]},
   {sub:'los saludos del día',items:[{label:'Buenos días',key:1},{label:'Buenas tardes',key:2},{label:'Buenas noches',key:3},{label:'¡Hasta mañana!',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in de twee perfiles en kies het juiste antwoord.',per:6,pool:[
   {q:'¿Cuántos años tiene Lucía?',opts:['16','15','14'],ans:'16',why:'«tengo 16 años»'},
   {q:'¿De dónde es Diego?',opts:['Ciudad de México','Sevilla','Madrid'],ans:'Ciudad de México',why:'perfil de Diego'},
   {q:'¿Qué apellido tiene Lucía?',opts:['Ramírez García','Hernández','García López'],ans:'Ramírez García',why:'«Lucía Ramírez García»'},
   {q:'¿Qué idiomas habla Lucía?',opts:['español e inglés','solo español','francés'],ans:'español e inglés',why:'perfil de Lucía'},
   {q:'¿Qué le gusta a Diego?',opts:['la comida y el fútbol','la música','viajar'],ans:'la comida y el fútbol',why:'perfil de Diego'},
   {q:'¿Cuál es la nacionalidad de Diego?',opts:['mexicana','española','belga'],ans:'mexicana',why:'«Mi nacionalidad es mexicana»'},
   {q:'¿En qué parte de España vive Lucía?',opts:['el sur','el norte','el este'],ans:'el sur',why:'«Sevilla, en el sur»'},
   {q:'¿Qué busca Lucía?',opts:['un amigo para hablar español','un profesor','un trabajo'],ans:'un amigo para hablar español',why:'«Busco un amigo…»'},
   {q:'¿Con quién vive Diego?',opts:['con su familia','solo','con amigos'],ans:'con su familia',why:'«vivo con mi familia»'},
   {q:'¿A quién quiere conocer Diego?',opts:['gente de Europa','gente de Asia','a un profesor'],ans:'gente de Europa',why:'«Quiero conocer gente de Europa»'},
   {q:'¿Quién es mayor?',opts:['Lucía','Diego','tienen la misma edad'],ans:'Lucía',why:'Lucía 16 · Diego 15'},
   {q:'¿Qué le gusta a Lucía?',opts:['la música y viajar','la comida','el fútbol'],ans:'la música y viajar',why:'perfil de Lucía'}]});
}

renderFC();renderTable();gameInterrog();gameElla();renderLectura();buildRecorders();buildInlineExercises();
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='U1_web_mijn_versie.html';a.click();};
})();
"""

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/U1_web.html","w").write(html)
print("U1_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
