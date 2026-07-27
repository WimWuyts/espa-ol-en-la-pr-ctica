#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C5 · U2 «Mi gente».
# Eén standalone bestand: fonts base64, de 24 U2-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U2-vocab), visuele/interactieve grammatica (familia+tener · posesivos · adjetivos · ser/estar · demostrativos),
# klikbare kaart (mundo hispano) + TTS + editbar + inline recorders. Zelfde pijplijn/huisstijl als U0/U1-hub (groen).
import json, base64, os, sys
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
GEN = f"{ROOT}/02-huisstijl/beeld/generators"
sys.path.insert(0, GEN); import cast_gen as C; import vocab_icons as VI; import vocab_emoji as VE
vocab = json.load(open(f"{ROOT}/01-cursussen/05-a1/U2/u2_vocab.json", encoding="utf-8"))
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
   ['familia-memoria', 'memoria de la familia', 'memory'],
   ['parentesco', 'parentesco (¿quién es?)', 'match'],
   ['tonica-familia', 'la sílaba tónica', 'tap']]],
 ['② Distinguir · gramática', [
   ['tener-persona', 'tener → ¿qué persona?', 'classify'],
   ['fisico-caracter', '¿físico o carácter?', 'classify'],
   ['posesivo-numero', 'posesivo · ¿singular o plural?', 'classify'],
   ['ser-estar', '¿ser o estar?', 'classify'],
   ['este-ese', '¿este o ese? (cerca/lejos)', 'classify']]],
 ['③ Producir con apoyo', [
   ['tener-cloze', 'el verbo tener', 'cloze'],
   ['ser-estar-cloze', 'ser / estar (cloze)', 'cloze'],
   ['posesivo-cloze', 'los posesivos (mi/tu/su)', 'cloze'],
   ['adjetivo-concuerda', 'concuerda el adjetivo', 'cloze'],
   ['arbol-genealogico', 'ordena el árbol genealógico', 'order'],
   ['familia-tetris', 'tener/ser/estar Tetris', 'tetris']]],
 ['④ Analizar & comunicar', [
   ['cuerpo-point', 'señala el cuerpo', 'point'],
   ['describe-persona', 'describe a una persona', 'sim']]],
 ['⑤ Hablar · grábate 🎙️', [
   ['carrusel-familia', 'carrusel: mi familia', 'speak'],
   ['shadowing-lucia', 'shadowing: la familia de Lucía', 'speak'],
   ['mensaje-familia', 'mensaje de voz: mi familia', 'speak'],
   ['quien-es', 'juego: ¿quién es?', 'speak']]],
]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-u2-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-u2-{s}.html")}

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
/* ---- árbol de Rosalía (PAREL-2) ---- */
.arbol{display:flex;flex-direction:column;gap:14px;margin:8px 0 4px}
.agen{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;position:relative}
.anode{border:1.5px solid var(--line);border-top:4px solid var(--g);background:var(--card);border-radius:14px;padding:9px 12px;min-width:118px;text-align:center;cursor:pointer;transition:transform .12s}
.anode:hover{transform:translateY(-2px);border-color:var(--g)}
.anode.hi{border-top-color:var(--ww);background:var(--gt)}
.anode .an{font-family:var(--disp);font-weight:700;color:var(--gd);font-size:15px}
.anode .ar{font-size:11px;color:var(--mut);margin-top:1px}
.anode .aemo{font-size:20px;line-height:1}
.ainfo{margin-top:10px;padding:12px 15px;background:var(--gt);border-radius:12px;min-height:58px}
.ainfo h4{margin:0 0 4px;font-family:var(--disp);color:var(--gd);font-size:17px}
.ojo{border:1.5px solid var(--amber);background:#FEF7E7;border-radius:12px;padding:11px 14px;margin:10px 0;font-size:14px}
[data-theme=dark] .ojo{background:#2a2410}
.ojo b{color:var(--amber)}
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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="familia">la familia</option><option value="fisico">el físico</option><option value="colores">los colores</option><option value="caracter">el carácter</option><option value="cuerpo">el cuerpo</option><option value="util">palabras útiles</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Español en la práctica · U2 Mi gente</title>
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
    <div><h1>U2 · Mi gente</h1>
    <p>La página digital de la Unidad 2 (parada <b>Sevilla</b>, la ciudad de Lucía): flashcards, el árbol de Rosalía, gramática visual e interactiva, <b>+100 ejercicios</b> con zelfcorrectie y <b>20 juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U2. Klik om te draaien; wissel ES↔NL; filter per groep; klik 🔊 om te horen. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
    __FC__
    <h2 class="sec">La familia de Rosalía · el árbol genealógico 🎤</h2>
    <p class="lead">Leer het familievocab via de stamboom van de zangeres <b>Rosalía</b>. <b>Klik op een persoon</b> om te zien wie het is (en te horen 🔊). Let daarna op de grote valstrik: <b>primo/prima</b> ≠ <b>sobrino/sobrina</b>. <span class="gloss">We leren het familievocabulaire via de stamboom van Rosalía.</span></p>
    <div class="card" id="arbolwrap"></div>
    <div class="card ex" id="ax_rosalia"></div>
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
    <p class="lead">Eerst betekenis en patroon ontdekken, dan de regel. Beweeg over de woorden, klik, en probeer. <span class="gloss">Alles binnen het thema van U2: la familia + tener, los posesivos, los adjetivos, ser/estar en los demostrativos.</span></p>
    <div class="card" id="colorsent"></div>
    <h3 class="subh">👪 El verbo «tener» — construye y practica</h3>
    <div class="card" id="reflexconj"></div>
    <div class="card ex" id="gx_build"></div>
    <div class="card ex" id="gx_tener"></div>
    <h3 class="subh">🔑 Posesivos — mi · tu · su (+ mis/tus/sus)</h3>
    <div class="card ex" id="gx_pos"></div>
    <h3 class="subh">🎨 Adjetivos — concordancia (género + número)</h3>
    <div class="card ex" id="gx_conc"></div>
    <h3 class="subh">⚖️ ¿ser o estar? — dé valstrik van «zijn»</h3>
    <div class="game" id="g_hora"></div>
    <div class="card ex" id="gx_serestar"></div>
    <h3 class="subh">👉 Demostrativos — este/ese (cerca/lejos)</h3>
    <div class="game" id="g_depor"></div>
    <div class="card ex" id="gx_demo"></div>
    <h3 class="subh">🎯 Repaso mixto — rellena con feedback</h3>
    <div class="card ex" id="gx_mix"></div>
  </section>

  <section class="panel" data-p="lectura">
    <h2 class="sec">Lectura · la familia de Lucía</h2>
    <p class="lead">Lees het album van Lucía, <b>luister</b> het (🔊 TTS) en <b>controleer je begrip</b> (verdadero/falso met bewijs). Daarna reageer je met je eigen familie — dat neem je op in het tabblad <b>Hablar</b>. <span class="gloss">Keten: lezen → luisteren → spreken.</span></p>
    <div id="lecturawrap"></div>
    <h3 class="subh">🔢 Ordena · la familia</h3>
    <div class="card ex" id="lx_order"></div>
    <h3 class="subh">🔎 Comprensión · escanea y escoge</h3>
    <div class="card ex" id="lx_scan"></div>
  </section>

  <section class="panel" data-p="juegos">
    <h2 class="sec">Ejercicios · 20 juegos, jij kiest</h2>
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
    <h2 class="sec">Cultura · La familia hispana</h2>
    <p class="lead">La familia es muy importante en el mundo hispano: grande, unida y con muchos <b>apodos</b>. <span class="gloss">De familie is groot en hecht; bijnamen zijn heel gewoon. De familie is ook een groot thema in de kunst.</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>La familia grande y los apodos 👪</h3>
      <p><b>ES:</b> En muchos países hispanos la familia es <b>grande y unida</b>: abuelos, tíos y primos se ven a menudo, sobre todo los domingos para comer juntos. Muchos nombres tienen un <b>apodo</b>: <b>Pepe</b>=José · <b>Paco</b>=Francisco · <b>Lola</b>=Dolores. <span class="gloss">De familie is groot en hecht; bijnamen zoals Pepe (José) zijn heel gewoon.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 21v-8a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8"/><path d="M4 16s.5-1 2-1 2.5 2 4 2 2.5-2 4-2 2.5 2 4 2 2-1 2-1"/><path d="M2 21h20"/><path d="M7 8v3"/><path d="M12 8v3"/><path d="M17 8v3"/><path d="M7 4h.01"/><path d="M12 4h.01"/><path d="M17 4h.01"/></svg>La quinceañera 🎉</h3>
      <p><b>ES:</b> En América Latina, cuando una chica cumple <b>15 años</b>, se celebra la <b>quinceañera</b>: una gran fiesta familiar con <b>vestido</b>, baile y toda la familia reunida. Es uno de los momentos más importantes de la vida. <span class="gloss">Het grote 15-jaarsfeest voor een meisje: een galajurk, dans en de hele familie samen — een echte mijlpaal.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Frida Kahlo · la familia en el arte 🎨</h3>
      <p><b>ES:</b> La pintora mexicana <b>Frida Kahlo</b> (1907–1954) pintó su propio <b>árbol genealógico</b> en el cuadro «Mis abuelos, mis padres y yo»: abuelos, padres y ella, todos juntos. La familia es un gran tema del arte hispano. <span class="gloss">De Mexicaanse schilderes Frida Kahlo schilderde haar eigen stamboom; familie is een groot thema in de Spaanstalige kunst.</span></p></div>
    <h3 class="subh">📍 La Ruta · ¿dónde estamos?</h3>
    <p class="lead">Onze parada 2: <b>Sevilla</b> 🇪🇸 (Andalucía), la ciudad de Lucía. <b>Klik op een groen land</b> op de kaart voor info. Verderop: Barcelona → València → México → Colombia → Perú.</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een groen land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    <h2 class="sec">Extra · bronnen</h2>
    <p class="lead">Externe uitleg &amp; oefeningen (de leerkracht vult de links aan).</p>
    <div class="card"><p>🎬 <b>profedeele</b> (YouTube — la hora / verbos reflexivos / presente irregular) — <span class="gloss">link volgt.</span></p>
    <p>🧩 <b>arche-ele</b> (Genially — la rutina diaria / la hora) — <span class="gloss">link volgt.</span></p>
    <p>📄 In het boek (PDF) verwijzen de QR-codes naar déze pagina, op het juiste ankerpunt.</p></div>
  </section>

  <div class="foot">Español en la práctica · C5 · Unidad 2 «Mi gente» — página digital. Uitbreiding op de PDF · huisstijl groen · print ↔ PowerPoint ↔ web.</div>
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
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Mi familia — beweeg over de woorden</h3>'+
'<div class="csent">'+
'<span style="background:#dbeafe;color:#1e40af">Esta<span class="tip">demostrativo · dichtbij (cerca)</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">es<span class="tip">ser · identidad/descripción</span></span> '+
'<span style="background:#dbeafe;color:#1e40af">mi hermana<span class="tip">posesivo mi + persoon</span></span>. '+
'<span style="background:#fed7aa;color:#9a3412">Es<span class="tip">ser · descripción</span></span> '+
'<span style="background:#dcfce7;color:#166534">morena<span class="tip">adjetivo · concuerda (fem.)</span></span> y muy '+
'<span style="background:#dcfce7;color:#166534">simpática<span class="tip">adjetivo · carácter</span></span>, pero hoy '+
'<span style="background:#fed7aa;color:#9a3412">está<span class="tip">estar · estado ahora</span></span> '+
'<span style="background:#ede9fe;color:#5b21b6">cansada<span class="tip">estado pasajero</span></span>.</div>'+
'<div class="legend"><span><i style="background:#93c5fd"></i>persoon/aanwijzer</span><span><i style="background:#fdba74"></i>ser/estar</span><span><i style="background:#86efac"></i>adjetivo</span><span><i style="background:#c4b5fd"></i>estado</span></div>'+
'<p class="gloss" style="margin-top:8px">🔴 <b>es</b> morena (blijvend · ser) ↔ <b>está</b> cansada (nu · estar) — allebei «zijn»! · '+(TTS?'<button class="spk-btn" onclick="speak(\'Esta es mi hermana. Es morena y muy simpática, pero hoy está cansada.\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: reflexivo — klik om de vorm te onthullen ----
(function(){const el=document.getElementById('reflexconj');
 const R=[['yo','tengo'],['tú','tienes'],['él/ella/usted','tiene'],['nosotros/-as','tenemos'],['vosotros/-as','tenéis'],['ellos/-as/ustedes','tienen']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">El verbo tener — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">Denk eerst zelf de vorm; klik dan de kaart. 🔊 om te horen. Ojo: yo teng<b>o</b> · e→ie in tú/él/ellos.</p><div class="conjgrid" id="rcg"></div>';
 const g=el.querySelector('#rcg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v;if(TTS)speak(v);};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: la hora matcher (klik dígitos → frase) ----
function gameHora(){const el=document.getElementById('g_hora');
 const items=[['Mi padre ___ alto.','es',['es','está']],['Mi madre ___ en casa.','está',['es','está']],['Lucía ___ de Sevilla.','es',['es','está']],['Hoy mi hermano ___ cansado.','está',['es','está']],['Mis abuelos ___ simpáticos.','son',['son','están']],['Nosotros ___ en el parque.','estamos',['somos','estamos']]];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿ser o estar?</h3><p class="desc">Identidad/descripción → <b>ser</b>. Estado/lugar → <b>estar</b>. Kies de juiste vorm.</p>'+scoreBar('sbSE')+'<div id="seQ" style="font-size:20px;font-family:var(--disp);text-align:center;margin:10px 0;color:var(--gd)"></div><div class="chips" id="seC" style="justify-content:center"></div><div class="fb" id="seFb"></div>';
 const sb=el.querySelector('#sbSE');const cont=el.querySelector('#seC');
 function guess(k){const ok=k===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#seFb'),ok,(ok?'¡Sí! ':'Nee → ')+el.cur[0].replace('___','«'+el.cur[1]+'»')+' ('+(['es','son','somos'].includes(el.cur[1])?'ser · identidad/descripción':'estar · estado/lugar')+').');if(TTS&&ok)speak(el.cur[0].replace('___',el.cur[1]));setTimeout(next,1100);}
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#seQ').textContent=el.cur[0];cont.innerHTML='';el.cur[2].forEach(o=>{const b=document.createElement('div');b.className='chip';b.textContent=o;b.onclick=()=>guess(o);cont.appendChild(b);});el.querySelector('#seFb').className='fb';}
 next();}
// ---- GRAMMAR-VIZ 4: ¿de la o por la? ----
function gameDePor(){const el=document.getElementById('g_depor');
 const items=[['(cerca) ___ es mi hermano.','este',['este','ese']],['(lejos) ___ es mi tío.','ese',['este','ese']],['(cerca) ___ es mi madre.','esta',['esta','esa']],['(lejos) ___ son mis primos.','esos',['estos','esos']],['(cerca) ___ son mis hermanas.','estas',['estas','esas']],['(lejos) ___ es mi abuela.','esa',['esta','esa']]];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿este o ese?</h3><p class="desc">Dichtbij (cerca) → <b>este/esta…</b> · verder (lejos) → <b>ese/esa…</b>. Let op geslacht en getal.</p>'+scoreBar('sbEE')+'<div id="eeQ" style="font-size:20px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" id="eeC" style="justify-content:center"></div><div class="fb" id="eeFb"></div>';
 const sb=el.querySelector('#sbEE');const cont=el.querySelector('#eeC');
 function guess(k){const ok=k===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#eeFb'),ok,(ok?'¡Sí! ':'Nee → ')+'«'+el.cur[1]+'» '+(el.cur[0].includes('cerca')?'(cerca)':'(lejos)')+'.');if(TTS&&ok)speak(el.cur[0].replace('___',el.cur[1]).replace(/\(.*?\)/,''));setTimeout(next,1100);}
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#eeQ').textContent=el.cur[0];cont.innerHTML='';el.cur[2].forEach(o=>{const b=document.createElement('div');b.className='chip';b.textContent=o;b.onclick=()=>guess(o);cont.appendChild(b);});el.querySelector('#eeFb').className='fb';}
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
   const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "👪 En familia: a los 15 años se celebra la quinceañera", "star": 0, "nl": ""}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "👪 En familia: se llevan dos apellidos (padre y madre)", "star": 1, "nl": "★ ¡Estás aquí! Parada U0–U4 · Madrid · Sevilla · Barcelona · València"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "👪 En familia: la familia extensa es muy unida", "star": 0, "nl": ""}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "👪 En familia: muchos apellidos tienen raíces quechuas", "star": 0, "nl": ""}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "👪 En familia: el domingo es día de asado en familia", "star": 0, "nl": ""}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "👪 En familia: en Navidad se reúnen con hallacas", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "👪 En familia: existe el «Día de la Familia»", "star": 0, "nl": ""}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "👪 En familia: familias grandes, muchas kichwas", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "👪 En familia: las familias mayas transmiten su idioma en casa", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "👪 En familia: varias generaciones viven juntas", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "👪 En familia: la «cholita» y la pollera, herencia familiar", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "👪 En familia: la familia se reúne los domingos con música", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "👪 En familia: familias numerosas y muy unidas", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "👪 En familia: en casa la familia habla guaraní", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "👪 En familia: la familia celebra «la Purísima»", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "👪 En familia: muchas familias tienen parientes en EE. UU.", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "👪 En familia: entre familia y amigos se dice «mae»", "star": 0, "nl": ""}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "👪 En familia: familias diversas por el Canal (todo el mundo)", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "👪 En familia: el mate se comparte en familia", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "👪 En familia: la familia mezcla lo taíno, africano y español", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "👪 En familia: familias con lenguas fang y bubi en casa", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "👪 En familia: familias hispanas bilingües (español + inglés)", "star": 0, "nl": ""}};
 const wrap=document.getElementById('mapwrap');const svg=wrap.querySelector('svg');const box=document.getElementById('mapinfo');
 if(!svg)return;
 svg.querySelectorAll('path.spa, path.usa').forEach(p=>{p.style.cursor='pointer';
   p.addEventListener('mouseenter',()=>{p.style.opacity='.75'});p.addEventListener('mouseleave',()=>{p.style.opacity=''});
   p.addEventListener('click',()=>{const c=p.getAttribute('data-c');const d=INFO[c];if(!d)return;
     box.innerHTML='<h3>'+d.fl+' '+d.n+' <span style="font-size:13px;color:var(--mut);font-weight:400">('+c+')</span>'+(d.star?' ★':'')+'</h3>'+'<div class="mrow"><b>🏛️ Capital:</b> '+d.cap+'</div>'+'<div class="mrow"><b>👥 Población:</b> '+d.pob+'</div>'+'<div class="mrow"><b>💰 Moneda:</b> '+d.mon+'</div>'+'<div class="mrow"><b>🗣️ Gentilicio:</b> '+d.gen+'</div>'+'<div class="mrow"><b>🌐 Idioma:</b> '+d.idi+'</div>'+(d.tema?'<div style="margin-top:8px;padding:8px 11px;background:rgba(255,255,255,.7);border-left:4px solid var(--gd);border-radius:7px;font-weight:600;color:var(--gd)">'+d.tema+'</div>':'')+(d.cool?'<div style="margin-top:8px;font-size:13px;line-height:1.5"><b>💡 ¿Sabías que…?</b> '+d.cool+'</div>':'')+(d.nl?'<div class="gloss" style="margin-top:6px">'+d.nl+'</div>':'');
     box.scrollIntoView({behavior:'smooth',block:'nearest'});});
 });
})();

// ---------- LECTURA: el blog de Pau + TTS + begrip ----------
function renderLectura(){const el=document.getElementById('lecturawrap');if(!el)return;
 const P=[{n:'La familia de Lucía',fr:'Sevilla · el álbum',t:'¡Hola! Soy Lucía y esta es mi familia de Sevilla. <span class="ev">Somos cinco</span>: mis padres, mi hermano mayor Marco, mi hermana menor Ana y yo. Mi padre se llama <span class="ev">Antonio</span>; es alto, moreno y muy tranquilo. Mi madre, Rosa, es baja, rubia y <span class="ev">muy habladora</span>. Mi hermano Marco tiene diecinueve años; es delgado y lleva gafas. Ana solo tiene ocho años: es pequeña, graciosa y un poco tímida. También tengo dos abuelos, Pepe y Carmen, y una prima, <span class="ev">Julia, que es pelirroja</span> y muy simpática. Hoy todos estamos en casa de los abuelos. ¡Es una familia grande y muy alegre!'}];
 const strip=h=>h.replace(/<[^>]+>/g,'');
 el.innerHTML='<div class="perfiles">'+P.map((p,i)=>'<div class="perfil"><h4>📓 '+p.n+' <span class="gloss" style="font-size:12px;font-weight:400">· '+p.fr+'</span> '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lx'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div class="txt" id="lx'+i+'" data-raw="'+strip(p.t).replace(/"/g,'&quot;')+'">'+p.t+'</div></div>').join('')+'</div>';
 const items=[['La familia de Lucía tiene cinco miembros.',true,'«Somos cinco»'],['Marco es el hermano menor.',false,'Marco es el hermano mayor'],['La madre de Lucía es muy habladora.',true,'«Rosa… muy habladora»'],['Julia es la abuela de Lucía.',false,'Julia es la prima (pelirroja)']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — comprueba tu comprensión</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Responde</h3><p class="gloss" style="margin:0 0 8px">Schrijf zoals Lucía over jouw familie (aantal + namen + één beschrijving). Neem het op onder <b>Hablar 🎙️</b> («mensaje de voz: mi familia»).</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="¡Hola! Esta es mi familia. Somos…"></textarea>';
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
 makeRecorder('rec_hora',{title:'Describe a un familiar',desc:'Luister het model → beschrijf iemand uit je familie → neem op → luister terug → opnieuw.',items:[
   {text:'Mi hermana es alta, morena y muy simpática.',cue:'modelo'},{text:'Mi abuelo es mayor, tiene el pelo gris y es muy tranquilo.',cue:'modelo 2'},{text:'Describe a un familiar tuyo (físico + carácter).',cue:'jouw versie',tip:'Heb je 2 físicos + 1 carácter gezegd? Neem opnieuw op.'}]});
 makeRecorder('rec_dia',{title:'Juego: ¿Quién es?',desc:'Beschrijf een familielid zonder de naam; laat iemand raden. Spreek in en luister terug.',items:[
   {text:'Es mayor, tiene el pelo gris y es muy tranquilo. ¿Quién es?',cue:'ronde 1'},{text:'Es joven, es pelirroja y muy simpática. ¿Quién es?',cue:'ronde 2'},{text:'Beschrijf zelf iemand: Es… tiene… ¿Quién es?',cue:'jouw raadsel'}]});
 makeRecorder('rec_mensaje',{title:'Mensaje de voz: mi familia',desc:'Neem één bericht op. Ontvanger: Lucía · Doel: je familie voorstellen. Gebruik: En mi familia somos… · Tengo… · Mi madre es…',items:[
   {text:'Preséntale tu familia a Lucía en un mensaje de voz (30 s).',cue:'para · Lucía',tip:'Heb je aantal + tener + één beschrijving gezegd? Neem opnieuw op.'}]});
}

// ---------- ÁRBOL DE ROSALÍA (PAREL-2) ----------
function renderArbol(){const el=document.getElementById('arbolwrap');if(!el)return;
 const GEN=[
  [{n:'Antonio',r:'el abuelo materno',nl:'de opa',e:'👴',say:'el abuelo'},{n:'Carmen',r:'la abuela',nl:'de oma',e:'👵',say:'la abuela'}],
  [{n:'José Manuel',r:'el padre de Rosalía',nl:'de vader',e:'👨',say:'el padre'},{n:'Pilar',r:'la madre de Rosalía',nl:'de moeder',e:'👩',say:'la madre'}],
  [{n:'Pili',r:'la hermana mayor de Rosalía',nl:'de (oudere) zus',e:'👱‍♀️',say:'la hermana'},{n:'Rosalía',r:'la cantante · la hija menor · la tía de Genís',nl:'de zangeres',e:'🎤',say:'Rosalía',hi:true}],
  [{n:'Genís',r:'el sobrino de Rosalía (el hijo de Pili)',nl:'het neefje',e:'👦',say:'el sobrino'}]
 ];
 const GN=['Los abuelos','Los padres','Las hijas','La nueva generación'];
 el.innerHTML='<div class="arbol" id="arb"></div>'+
  '<div class="ainfo" id="ainfo"><p class="gloss" style="margin:0">👆 Klik op een persoon in de stamboom.</p></div>'+
  '<div class="ojo">💡 <b>¡Ojo! neef/nicht = twee woorden in het Spaans:</b> <b>el primo / la prima</b> = kind van je <b>oom/tante</b> · <b>el sobrino / la sobrina</b> = kind van je <b>broer/zus</b>. '+
  '<span class="gloss">Genís is de <b>sobrino</b> van Rosalía (zoon van haar zus Pili), niet haar primo.</span></div>'+
  '<p class="gloss" style="font-size:12px">De namen van de grootouders zijn voorbeelden. · '+(TTS?'<button class="spk-btn" style="padding:5px 11px" onclick="speak(\'Esta es la familia de Rosalía: los abuelos, los padres, la hermana y el sobrino.\')">🔊 escuchar la familia</button>':'')+'</p>';
 const arb=el.querySelector('#arb'),info=el.querySelector('#ainfo');
 GEN.forEach((row,gi)=>{const g=document.createElement('div');g.className='agen';
   row.forEach(p=>{const d=document.createElement('div');d.className='anode'+(p.hi?' hi':'');
     d.innerHTML='<div class="aemo">'+p.e+'</div><div class="an">'+p.n+'</div><div class="ar">'+p.r+'</div>';
     d.onclick=()=>{info.innerHTML='<h4>'+p.e+' '+p.n+'</h4><div>'+p.r+' · <span class="gloss">'+p.nl+'</span></div>';if(TTS)speak(p.say);};
     g.appendChild(d);});
   arb.appendChild(g);});}

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
// MATCHING: pool item = {a,b}
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
 // ---- PAREL-2 · quiz sobre el árbol de Rosalía (primo vs sobrino) ----
 buildChoice('ax_rosalia',{title:'¿Quién es quién? · la familia de Rosalía',desc:'Kijk naar de stamboom hierboven en kies het juiste familielid. Let op primo/prima ↔ sobrino/sobrina.',per:6,pool:[
   {q:'Genís es el ___ de Rosalía (el hijo de su hermana Pili).',opts:['sobrino','primo','hermano'],ans:'sobrino',why:'kind van je zus = sobrino, geen primo'},
   {q:'Pili es la ___ de Rosalía.',opts:['hermana','madre','tía'],ans:'hermana',why:'Pili y Rosalía son hijas de los mismos padres'},
   {q:'José Manuel es el ___ de Rosalía.',opts:['padre','abuelo','tío'],ans:'padre',why:'José Manuel = el padre'},
   {q:'Rosalía es la ___ de Genís.',opts:['tía','madre','prima'],ans:'tía',why:'la hermana de tu madre/padre = tía'},
   {q:'Carmen es la ___ de Rosalía.',opts:['abuela','madre','tía'],ans:'abuela',why:'Carmen = la abuela'},
   {q:'Pilar es la ___ de Rosalía.',opts:['madre','abuela','hermana'],ans:'madre',why:'Pilar = la madre'},
   {q:'El hijo de tu tío es tu ___.',opts:['primo','sobrino','hermano'],ans:'primo',why:'kind van oom/tante = primo'},
   {q:'La hija de tu hermana es tu ___.',opts:['sobrina','prima','hija'],ans:'sobrina',why:'kind van broer/zus = sobrina'},
   {q:'El padre de tu padre es tu ___.',opts:['abuelo','tío','primo'],ans:'abuelo',why:'el padre de tu padre = el abuelo'},
   {q:'Pili es la ___ de Genís.',opts:['madre','tía','abuela'],ans:'madre',why:'Genís es el hijo de Pili'}]});
 // ================= VOCABULARIO =================
 buildMatch('vx_match',{title:'Empareja: palabra ↔ imagen',desc:'Koppel het Spaanse woord aan het juiste beeld (familia · físico · colores).',per:6,pool:[
   {a:'el padre',b:'👨'},{a:'la madre',b:'👩'},{a:'el abuelo',b:'👴'},{a:'la abuela',b:'👵'},
   {a:'el bebé',b:'👶'},{a:'el ojo',b:'👀'},{a:'la mano',b:'✋'},{a:'la nariz',b:'👃'},
   {a:'el pelo',b:'💇'},{a:'el perro',b:'🐶'},{a:'la boca',b:'👄'},{a:'la oreja',b:'👂'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat in de zin past.',per:6,pool:[
   {q:'El hermano de mi madre es mi ___.',opts:['tío','primo','abuelo'],ans:'tío',why:'hermano de mi madre → tío'},
   {q:'Mi hermana pequeña es la hermana ___.',opts:['menor','mayor','media'],ans:'menor',why:'pequeña → menor'},
   {q:'Lucía tiene el ___ largo y moreno.',opts:['pelo','ojo','mano'],ans:'pelo',why:'el pelo largo'},
   {q:'Mi abuelo ya es ___.',opts:['mayor','menor','joven'],ans:'mayor',why:'abuelo → mayor (oud)'},
   {q:'Mi prima es muy ___: siempre habla.',opts:['habladora','tímida','tranquila'],ans:'habladora',why:'siempre habla → habladora'},
   {q:'Tiene los ___ azules.',opts:['ojos','pelos','pies'],ans:'ojos','why':'ojos azules'},
   {q:'Ana no es alta, es ___.',opts:['baja','delgada','rubia'],ans:'baja',why:'no alta → baja'},
   {q:'Mi padre lleva ___ para leer.',opts:['gafas','barba','pelo'],ans:'gafas',why:'para leer → gafas'},
   {q:'Mi hermano es ___: nunca dice nada.',opts:['tímido','gracioso','hablador'],ans:'tímido',why:'nunca habla → tímido'},
   {q:'La familia de Lucía es ___ y alegre.',opts:['grande','pequeña','triste'],ans:'grande',why:'muchos miembros → grande'},
   {q:'Mi tía tiene el pelo ___ (roodharig).',opts:['pelirrojo','rubio','castaño'],ans:'pelirrojo',why:'roodharig → pelirrojo'},
   {q:'El hijo de mi hermano es mi ___.',opts:['sobrino','primo','nieto'],ans:'sobrino',why:'hijo de mi hermano → sobrino'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de omschrijving en kies het juiste woord.',per:6,pool:[
   {q:'El padre de mi padre:',opts:['el abuelo','el tío','el primo'],ans:'el abuelo',why:'padre del padre = abuelo'},
   {q:'La hija de mi tía:',opts:['la prima','la sobrina','la hermana'],ans:'la prima',why:'hija de tía = prima'},
   {q:'El hijo de mi hermana:',opts:['el sobrino','el primo','el nieto'],ans:'el sobrino',why:'hijo de hermana = sobrino'},
   {q:'El hermano de mi madre:',opts:['el tío','el abuelo','el primo'],ans:'el tío',why:'hermano de madre = tío'},
   {q:'La madre de mi madre:',opts:['la abuela','la tía','la prima'],ans:'la abuela',why:'madre de madre = abuela'},
   {q:'Persona con poco pelo:',opts:['calvo','rubio','moreno'],ans:'calvo',why:'poco pelo → calvo'},
   {q:'Persona que habla mucho:',opts:['hablador','tímido','tranquilo'],ans:'hablador',why:'habla mucho → hablador'},
   {q:'Color del pelo como el fuego:',opts:['pelirrojo','castaño','gris'],ans:'pelirrojo',why:'fuego → pelirrojo'},
   {q:'Lo contrario de alto:',opts:['bajo','delgado','joven'],ans:'bajo',why:'≠ alto → bajo'},
   {q:'Lo contrario de gordo:',opts:['delgado','bajo','mayor'],ans:'delgado',why:'≠ gordo → delgado'},
   {q:'Parte de la cara para ver:',opts:['los ojos','la boca','la mano'],ans:'los ojos',why:'ver → los ojos'},
   {q:'Persona de pocos años:',opts:['joven','mayor','alto'],ans:'joven',why:'pocos años → joven'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['el padre','la madre','el hermano','el ojo'],odd:3,why:'el ojo = cuerpo, geen familielid'},
   {words:['alto','bajo','delgado','tío'],odd:3,why:'tío = familia, geen físico'},
   {words:['rubio','moreno','pelirrojo','simpático'],odd:3,why:'simpático = carácter, geen kleur/pelo'},
   {words:['la mano','el pie','la boca','la abuela'],odd:3,why:'la abuela = familia, geen cuerpo'},
   {words:['simpático','gracioso','tímido','castaño'],odd:3,why:'castaño = color, geen carácter'},
   {words:['el tío','la tía','el primo','el pelo'],odd:3,why:'el pelo = cuerpo'},
   {words:['los ojos','la nariz','la oreja','el hijo'],odd:3,why:'el hijo = familia'},
   {words:['mayor','menor','joven','hablador'],odd:3,why:'hablador = carácter; de rest = leeftijd'}]});
 // ================= GRAMÁTICA =================
 buildOrder('gx_build',{title:'Construye la frase',desc:'Tik de blokjes in de juiste volgorde (persoon → werkwoord → rest).',rounds:[
   {sub:'mi hermana · descripción',items:[{label:'Mi hermana',key:1},{label:'es',key:2},{label:'morena',key:3},{label:'y simpática',key:4}]},
   {sub:'yo · tener',items:[{label:'Yo',key:1},{label:'tengo',key:2},{label:'dos',key:3},{label:'hermanos',key:4}]},
   {sub:'este/esta · demostrativo',items:[{label:'Esta',key:1},{label:'es',key:2},{label:'mi',key:3},{label:'prima Julia',key:4}]},
   {sub:'estar · estado',items:[{label:'Hoy',key:1},{label:'mi abuelo',key:2},{label:'está',key:3},{label:'cansado',key:4}]},
   {sub:'posesivo plural',items:[{label:'Mis',key:1},{label:'abuelos',key:2},{label:'son',key:3},{label:'mayores',key:4}]},
   {sub:'ser · origen',items:[{label:'Nosotros',key:1},{label:'somos',key:2},{label:'de',key:3},{label:'Sevilla',key:4}]}]});
 buildChoice('gx_tener',{title:'Mini-quiz: el verbo tener',desc:'Kies de juiste vorm van «tener». Directe feedback.',per:6,pool:[
   {q:'(Yo) ___ dos hermanos.',opts:['tengo','tienes','tiene'],ans:'tengo',why:'yo → tengo'},
   {q:'¿(Tú) ___ primos?',opts:['tienes','tengo','tiene'],ans:'tienes',why:'tú → tienes'},
   {q:'Mi hermano ___ quince años.',opts:['tiene','tienes','tengo'],ans:'tiene',why:'él → tiene'},
   {q:'(Nosotros) ___ una mascota.',opts:['tenemos','tienen','tengo'],ans:'tenemos',why:'nosotros → tenemos'},
   {q:'Mis abuelos ___ un perro.',opts:['tienen','tiene','tenéis'],ans:'tienen',why:'ellos → tienen'},
   {q:'¿(Vosotros) ___ familia en Madrid?',opts:['tenéis','tienen','tenemos'],ans:'tenéis',why:'vosotros → tenéis'},
   {q:'Lucía ___ el pelo largo.',opts:['tiene','tienes','tengo'],ans:'tiene',why:'ella → tiene'},
   {q:'(Yo) ___ una hermana menor.',opts:['tengo','tiene','tienes'],ans:'tengo',why:'yo → tengo'},
   {q:'Mi tía ___ dos hijos.',opts:['tiene','tienen','tengo'],ans:'tiene',why:'ella → tiene'},
   {q:'Mis primos ___ un gato.',opts:['tienen','tiene','tenéis'],ans:'tienen',why:'ellos → tienen'}]});
 buildChoice('gx_pos',{title:'Mini-quiz: mi · tu · su (mis/tus/sus)',desc:'Kies het juiste bezittelijk voornaamwoord (persoon + enkel/meervoud).',per:6,pool:[
   {q:'___ hermanos son altos. (yo · 2)',opts:['Mis','Mi','Su'],ans:'Mis',why:'meervoud → mis'},
   {q:'___ prima se llama Julia. (yo · 1)',opts:['Mi','Mis','Tu'],ans:'Mi',why:'enkelv. → mi'},
   {q:'¿Cómo se llama ___ padre? (tú)',opts:['tu','tus','su'],ans:'tu',why:'enkelv. → tu'},
   {q:'___ abuelos viven en Sevilla. (yo · 2)',opts:['Mis','Mi','Sus'],ans:'Mis',why:'meervoud → mis'},
   {q:'Lucía y ___ familia son de Sevilla. (ella)',opts:['su','sus','tu'],ans:'su',why:'enkelv. → su'},
   {q:'¿Tienes fotos de ___ primos? (tú · 2)',opts:['tus','tu','sus'],ans:'tus',why:'meervoud → tus'},
   {q:'___ madre es habladora. (yo · 1)',opts:['Mi','Mis','Su'],ans:'Mi',why:'enkelv. → mi'},
   {q:'¿Dónde están ___ gafas? (tú)',opts:['tus','tu','sus'],ans:'tus',why:'gafas = mv → tus'},
   {q:'___ tía tiene dos hijos. (ella)',opts:['Su','Sus','Mi'],ans:'Su',why:'enkelv. → su'},
   {q:'___ casa está en Sevilla. (nosotros · 1)',opts:['Nuestra','Nuestro','Nuestros'],ans:'Nuestra',why:'la casa (f) → nuestra'}]});
 buildMatch('gx_conc',{title:'Concordancia: adjetivo ↔ persona',desc:'Koppel de persoon aan de juiste vorm van het adjectief (género + número).',per:6,pool:[
   {a:'Mi hermana es…',b:'alta'},{a:'Mis primos son…',b:'simpáticos'},{a:'Lucía es…',b:'morena'},
   {a:'Mi padre es…',b:'tranquilo'},{a:'Mis abuelas son…',b:'bajas'},{a:'Mis hermanos son…',b:'rubios'},
   {a:'Mi tía es…',b:'habladora'},{a:'Las primas son…',b:'guapas'},{a:'El bebé es…',b:'gracioso'},
   {a:'Mis sobrinas son…',b:'pequeñas'}]});
 buildChoice('gx_serestar',{title:'Mini-quiz: ¿ser o estar?',desc:'Identidad/descripción → ser. Estado/lugar → estar.',per:6,pool:[
   {q:'Mi padre ___ alto.',opts:['es','está'],ans:'es',why:'descripción → ser'},
   {q:'Mi madre ___ en casa.',opts:['está','es'],ans:'está',why:'lugar → estar'},
   {q:'Lucía ___ de Sevilla.',opts:['es','está'],ans:'es',why:'origen → ser'},
   {q:'Hoy mi hermano ___ cansado.',opts:['está','es'],ans:'está',why:'estado → estar'},
   {q:'Mis abuelos ___ simpáticos.',opts:['son','están'],ans:'son',why:'carácter → ser'},
   {q:'Nosotros ___ en el parque.',opts:['estamos','somos'],ans:'estamos',why:'lugar → estar'},
   {q:'Ana ___ tímida.',opts:['es','está'],ans:'es',why:'carácter → ser'},
   {q:'La ventana ___ abierta.',opts:['está','es'],ans:'está',why:'toestand → estar'},
   {q:'Rosalía ___ cantante.',opts:['es','está'],ans:'es',why:'profesión → ser'},
   {q:'¿Cómo ___ (tú) hoy?',opts:['estás','eres'],ans:'estás',why:'estado → estar'}]});
 buildChoice('gx_demo',{title:'Mini-quiz: este/ese (cerca/lejos)',desc:'Dichtbij → este/esta… · verder weg → ese/esa… Let op geslacht en getal.',per:6,pool:[
   {q:'(cerca) ___ es mi hermano.',opts:['este','ese','esta'],ans:'este',why:'cerca + m → este'},
   {q:'(lejos) ___ es mi tío.',opts:['ese','este','esa'],ans:'ese',why:'lejos + m → ese'},
   {q:'(cerca) ___ es mi madre.',opts:['esta','esa','este'],ans:'esta',why:'cerca + f → esta'},
   {q:'(lejos) ___ son mis primos.',opts:['esos','estos','esas'],ans:'esos',why:'lejos + m pl → esos'},
   {q:'(cerca) ___ son mis hermanas.',opts:['estas','esas','estos'],ans:'estas',why:'cerca + f pl → estas'},
   {q:'(lejos) ___ es mi abuela.',opts:['esa','esta','ese'],ans:'esa',why:'lejos + f → esa'},
   {q:'(cerca) ___ es mi primo.',opts:['este','ese','esta'],ans:'este',why:'cerca + m → este'},
   {q:'(lejos) ___ son mis tías.',opts:['esas','estas','esos'],ans:'esas',why:'lejos + f pl → esas'},
   {q:'(cerca) ___ son mis abuelos.',opts:['estos','esos','estas'],ans:'estos',why:'cerca + m pl → estos'},
   {q:'(lejos) ___ es mi sobrina.',opts:['esa','esta','ese'],ans:'esa',why:'lejos + f → esa'}]});
 buildChoice('gx_mix',{title:'Repaso mixto: rellena',desc:'Alles door elkaar: tener · posesivos · adjetivos · ser/estar · demostrativos.',per:8,pool:[
   {q:'(Yo) ___ dos hermanos.',opts:['tengo','tienes','tiene'],ans:'tengo',why:'yo → tengo'},
   {q:'___ prima es pelirroja. (yo · 1)',opts:['Mi','Mis','Su'],ans:'Mi',why:'enkelv. → mi'},
   {q:'Mi hermana es ___. (moreno)',opts:['morena','moreno','morenas'],ans:'morena',why:'fem. sing.'},
   {q:'Hoy mi abuelo ___ cansado.',opts:['está','es','son'],ans:'está',why:'estado → estar'},
   {q:'(cerca) ___ es mi tío.',opts:['este','ese','esta'],ans:'este',why:'cerca + m → este'},
   {q:'Mis abuelos ___ simpáticos.',opts:['son','están','es'],ans:'son',why:'carácter → ser'},
   {q:'¿Cuántos primos ___ tú?',opts:['tienes','tienen','tengo'],ans:'tienes',why:'tú → tienes'},
   {q:'Mis primos son ___. (simpático)',opts:['simpáticos','simpática','simpático'],ans:'simpáticos',why:'masc. pl.'},
   {q:'Lucía ___ de Sevilla.',opts:['es','está','son'],ans:'es',why:'origen → ser'},
   {q:'___ abuelos viven en Sevilla. (yo · 2)',opts:['Mis','Mi','Sus'],ans:'Mis',why:'meervoud → mis'},
   {q:'(lejos) ___ son mis primas.',opts:['esas','estas','esos'],ans:'esas',why:'lejos + f pl → esas'},
   {q:'Nosotros ___ belgas.',opts:['somos','estamos','son'],ans:'somos',why:'nacionalidad → ser'}]});
 // ================= LECTURA =================
 buildOrder('lx_order',{title:'Ordena · la familia',desc:'Tik de tegels in de juiste volgorde.',rounds:[
   {sub:'las generaciones (mayor → menor)',items:[{label:'los abuelos',key:1},{label:'los padres',key:2},{label:'los hijos',key:3},{label:'los nietos',key:4}]},
   {sub:'los hermanos de Lucía (mayor → menor)',items:[{label:'Marco (19)',key:1},{label:'Lucía (16)',key:2},{label:'Ana (8)',key:3}]},
   {sub:'presenta a tu familia (orden lógico)',items:[{label:'Esta es mi familia.',key:1},{label:'Somos cinco.',key:2},{label:'Mi padre se llama…',key:3},{label:'Mi hermana es…',key:4}]},
   {sub:'la familia de Rosalía (mayor → menor)',items:[{label:'los abuelos',key:1},{label:'los padres',key:2},{label:'Pili y Rosalía',key:3},{label:'Genís (el sobrino)',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in het album van Lucía en kies het juiste antwoord.',per:6,pool:[
   {q:'¿Cuántos son en la familia de Lucía?',opts:['cinco','cuatro','seis'],ans:'cinco',why:'«Somos cinco»'},
   {q:'¿Cómo se llama el padre de Lucía?',opts:['Antonio','Marco','Pepe'],ans:'Antonio',why:'«Mi padre se llama Antonio»'},
   {q:'¿Cómo es la madre, Rosa?',opts:['habladora','tímida','alta'],ans:'habladora',why:'«muy habladora»'},
   {q:'¿Cuántos años tiene Marco?',opts:['diecinueve','ocho','dieciséis'],ans:'diecinueve',why:'«tiene diecinueve años»'},
   {q:'¿Quién es la más pequeña?',opts:['Ana','Julia','Rosa'],ans:'Ana',why:'«Ana solo tiene ocho años»'},
   {q:'¿Qué lleva Marco?',opts:['gafas','barba','sombrero'],ans:'gafas',why:'«lleva gafas»'},
   {q:'¿Cómo es Julia, la prima?',opts:['pelirroja','morena','rubia'],ans:'pelirroja',why:'«Julia, que es pelirroja»'},
   {q:'¿Dónde están todos hoy?',opts:['en casa de los abuelos','en el colegio','en el parque'],ans:'en casa de los abuelos',why:'«hoy todos estamos en casa de los abuelos»'}]});
}

renderFC();renderTable();gameHora();gameDePor();renderLectura();buildRecorders();renderArbol();buildInlineExercises();
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='U2_web_mijn_versie.html';a.click();};
})();
"""

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/U2_web.html","w").write(html)
print("U2_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
