#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C6+ · U6 «Cuando era pequeño».
# Eén standalone bestand: fonts base64, de U4-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U6-vocab), visuele/interactieve grammatica (imperfecto · contraste · comparativos),
# klikbare kaart (mundo hispano, parada 6 = Perú) + TTS + inline recorder + Lectura + editbar. Huisstijl morado.
import json, base64, os, sys
import hub_drills
import hub_type_sets
import hub_type_gram
import extra_bronnen
import hub_bloques
import escucha_data, lectura_data
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
GEN = f"{ROOT}/02-huisstijl/beeld/generators"
sys.path.insert(0, GEN); import cast_gen as C; import vocab_icons as VI; import vocab_emoji as VE
vocab = json.load(open(f"{ROOT}/01-cursussen/06-vervolg/U6/u6_vocab.json", encoding="utf-8"))
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

# ---- de U6-motor-spellen: gegroepeerd (receptief -> productief -> hablar) + base64 ingebed ----
MOTOR = [
 ['① Reconocer · woordenschat', [
   ['infancia-memoria', 'memoria de la infancia', 'memory'],
   ['antes-memoria', 'antes y ahora', 'memory'],
   ['verbo-imperfecto', 'verbo ↔ imperfecto', 'match'],
   ['infancia-objeto', 'la infancia', 'match']]],
 ['② Distinguir · gramática', [
   ['indef-imperf', '¿indefinido o imperfecto?', 'classify'],
   ['comparar', '¿más, menos o tan?', 'classify']]],
 ['③ Producir con apoyo', [
   ['imperfecto', 'completa: el imperfecto', 'cloze'],
   ['contraste', 'completa: indef ↔ imperf', 'cloze'],
   ['imperf-tetris', 'imperfecto: topos', 'mole'],
   ['recuerdo-order', 'ordena la frase', 'order'],
   ['senala', 'señala', 'point'],
   ['imperfecto-tap', 'tik la forma del imperfecto', 'tap']]],
 ['④ Hablar · grábate 🎙️', [
   ['repite-infancia', 'escucha y repite: mi infancia', 'speak'],
   ['mensaje-infancia', 'mensaje de voz: mi infancia', 'speak'],
   ['cuando-era', 'cuando era pequeño', 'sim'],
   ['carrusel-antes', 'carrusel · antes y ahora', 'speak']]],
 ['⑤ Escribir · escríbelo tú ✍️', [
   ['escribe-palabra', 'NL → escribe la palabra', 'type'],
   ['completa-frase', 'completa la frase', 'type'],
   ['que-palabra', '¿qué palabra es?', 'type'],
   ['dictado', 'dictado', 'type'],
   ['escribe-frase', 'escribe una frase', 'type']]]]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-c6plus-u6-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-c6plus-u6-{s}.html")}

CSS = FONTS + extra_bronnen.CSS + hub_drills.ESCUCHA_CSS + hub_drills.LECTURA_CSS + hub_drills.TYPE_CSS + """
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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="infancia">infancia</option><option value="escuela">escuela</option><option value="familia">familia</option><option value="imperfecto">imperfecto</option><option value="antesahora">antes/ahora</option><option value="comparar">comparativos</option><option value="relativo">que/donde</option><option value="opinar">opinar</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Más español en la práctica · C6+ U6 Cuando era pequeño</title>
<style>__CSS__</style></head><body>
<header class="top"><div class="bar">
  <div class="brand">Más español en la práctica <small>· edición única</small></div>
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
    <div><h1>U6 · Cuando era pequeño</h1>
    <p>La página digital de la Unidad 6 (<b>cuando era pequeño</b>): flashcards, gramática visual e interactiva y <b>__NGAMES__ juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie. Thema's: infancia · imperfecto · contraste · comparativos.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U6. Klik om te draaien; wissel ES↔NL; filter per groep; klik 🔊 om te horen. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
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
    <p class="lead">De <b>essentiële</b> grammatica van U6: het <b>pretérito imperfecto</b> (era, tenía, jugaba, iba), het <b>contrast</b> met de indefinido en de <b>comparativos</b> (más/menos… que). Hier oefen je <b>maximaal</b> — elke oefening trekt uit een grote pool, dus «↻ otra serie» geeft telkens een nieuwe reeks. <span class="gloss">Eerst betekenis/patroon ontdekken, dan de regel.</span></p>
    <div class="card" id="colorsent"></div>
    <div class="card" id="irconj"></div>
    <h2 class="sec" style="margin-top:26px">🔄 El imperfecto — máxima práctica</h2>
    <p class="lead">-ar → aba/abas/aba… · -er/-ir → ía/ías/ía… Slechts 3 irregulares: era · iba · veía. <span class="gloss">Voor gewoontes en beschrijving.</span></p>
    <div class="game" id="g_cantidad"></div>
    <div class="card ex" id="gx_cantq"></div>
    <div class="card ex" id="gx_reg"></div>
    <div class="card ex" id="gx_adj"></div>
    <h2 class="sec" style="margin-top:26px">↔️ Contraste indefinido ↔ imperfecto</h2>
    <p class="lead">imperfecto = achtergrond/gewoonte (era, jugaba) · indefinido = gebeurtenis (llegó, empezó). <span class="gloss">Jugaba cuando, de repente, empezó a llover.</span></p>
    <div class="game" id="g_pron"></div>
    <div class="card ex" id="gx_pronq"></div>
    <div class="card ex" id="gx_ser"></div>
    <div class="card ex" id="gx_build"></div>
    <h2 class="sec" style="margin-top:26px">⚖️ Comparativos + que — máxima práctica</h2>
    <p class="lead">más/menos … que · tan … como · irr. mejor/peor/mayor/menor. <span class="gloss">+ betrekkelijke que: el niño que jugaba…</span></p>
    <div class="card ex" id="gx_iraq"></div>
    <div class="card ex" id="gx_subj"></div>
    <div class="card ex" id="gx_plural"></div>
    <div class="card ex" id="gx_nac"></div>
    <div class="card ex" id="gx_conc"></div>
    <div class="card ex" id="gx_conc2"></div>
    <h3 class="subh">🎯 Repaso mixto — imperfecto + contraste + comparativos</h3>
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
    <h2 class="sec">Lectura completa · Carta de la abuela Rosario</h2>
    <p class="lead">Een echte brief met de volledige leesroute: <b>voorspellen → globaal → scannen → juist/fout met bewijs → betekenis uit de context → zelf schrijven</b>. <span class="gloss">Dezelfde tekst staat in je cursus, met schrijfruimte.</span></p>
    <div class="card ex" id="lec_c6p_u6"></div>
  </section>

  <section class="panel" data-p="escuchar">
    <h2 class="sec">Escuchar · Pódcast «Antes y ahora» 🎧</h2>
    <p class="lead">Twee gasten vergelijken hun kindertijd in de schoolpodcast. Eén fragment, zes stappen: eerst <b>weten waar je bent</b>, dan <b>globaal</b> luisteren, dan de <b>details</b>, dan <b>juist/fout met bewijs</b>. Het <b>transcript</b> gaat pas open als je klaar bent — anders lees je mee in plaats van te luisteren. <span class="gloss">Zolang er nog geen opname is, leest de computerstem het fragment voor.</span></p>
    <div class="card ex" id="esc_c6p_u6"></div>
  </section>
  <section class="panel" data-p="juegos">
    <h2 class="sec">Ejercicios · __NGAMES__ juegos, jij kiest</h2>
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
    <h2 class="sec">Cultura · la infancia en el mundo hispano</h2>
    <p class="lead">Parada 6 = <b>Cusco</b> 🇵🇪, bij <b>Nina</b>. Elke cultuur heeft haar kinderrituelen: de <b>quinceañera</b>, traditionele <b>juegos</b> en de grote rol van de <b>abuelos</b>. <span class="gloss">Hoe was jouw jeugd?</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🎉 La quinceañera</h3>
      <p>In veel Latijns-Amerikaanse landen viert een meisje haar <b>15de verjaardag</b> met een groot feest. Het markeert de overgang van kind naar jongvolwassene. <span class="gloss">Un rito de paso.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🪀 Los juegos tradicionales</h3>
      <p>Vroeger speelden kinderen <b>la rayuela</b> (hinkelen), <b>el trompo</b> (tol) en <b>las canicas</b> (knikkers) op straat. <span class="gloss">Nina «jugaba» ze in het dorp.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">👵 Los abuelos</h3>
      <p>In de hispanofoon spelen de <b>abuelos</b> een grote rol: ze passen op, vertellen verhalen en geven de traditie door. <span class="gloss">«Iba a casa de mi abuela».</span></p></div>
    <h3 class="subh">📍 La Ruta · el mapa (parada 6 = Cusco, Perú ★)</h3>
    <p class="lead">Onze halte is <b>Perú</b> (Cusco, Nina). <b>Klik op een land</b> op de kaart voor info — klik op Perú (★) voor de parada (thema familia).</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    __BRONNEN__
  </section>

  <div class="foot">Más español en la práctica · edición única · Unidad 6 «Cuando era pequeño» — página digital. Uitbreiding op de PDF · huisstijl morado · print ↔ PowerPoint ↔ web.</div>
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
const PANELS=[['vocab','Vocabulario'],['gram','Gramática'],['lectura','Lectura'],['escuchar','Escuchar 🎧'],['juegos','Juegos'],['hablar','Hablar 🎙️'],['cultura','Cultura'],['extra','Extra']];
const sn=document.getElementById('subnav');
// ── tabbladen · het adres volgt mee ──────────────────────────────────────────
// #escuchar opent dat tabblad; #lec_1 opent het paneel waar dat element in
// staat en springt ernaartoe. Zo kan een QR-code of een gedeelde link meteen
// op de juiste plek openen en werkt de terugknop van de browser.
function toonPaneel(sleutel){
  const i=PANELS.findIndex(p=>p[0]===sleutel), p=PANELS[i<0?0:i];
  document.querySelectorAll('.subnav button').forEach((b,j)=>{
    if(PANELS[j])b.classList.toggle('on',PANELS[j][0]===p[0]);});
  document.querySelectorAll('.panel').forEach(x=>x.classList.remove('show'));
  const el=document.querySelector('.panel[data-p="'+p[0]+'"]');
  if(el)el.classList.add('show');
}
function vanAdres(){
  let h='';
  try{h=decodeURIComponent((location.hash||'').slice(1));}catch(e){h=(location.hash||'').slice(1);}
  if(!h){toonPaneel(PANELS[0][0]);return true;}
  if(PANELS.some(p=>p[0]===h)){toonPaneel(h);window.scrollTo({top:0,behavior:'smooth'});return true;}
  const doel=document.getElementById(h);
  if(doel){
    const paneel=doel.closest?doel.closest('.panel'):null;
    if(paneel)toonPaneel(paneel.getAttribute('data-p'));
    doel.scrollIntoView({behavior:'smooth',block:'start'});
    return true;
  }
  return false;   // onbekend anker → laat de hub staan zoals ze opent
}
PANELS.forEach((p,i)=>{const b=document.createElement('button');b.textContent=p[1];if(i===0)b.classList.add('on');
  b.onclick=()=>{
    if((location.hash||'').slice(1)===p[0])vanAdres();   // al op dit tabblad → enkel naar boven
    else location.hash=p[0];                             // anders: adres wijzigen, hashchange doet de rest
  };sn.appendChild(b);});
addEventListener('hashchange',vanAdres);
// Bij het laden. Lukt het anker nog niet (element wordt later opgebouwd),
// dan proberen we het na 'load' nog één keer.
if(!vanAdres())addEventListener('load',vanAdres);

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

// ---- GRAMMAR-VIZ 1: kleurgecodeerde imperfecto-zin ----
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">El imperfecto — cómo era todo</h3>'+
'<div class="csent">'+
'<span style="background:#e9d5ff;color:#6b21a8">De pequeña<span class="tip">marcador: wanneer/gewoonte</span></span> '+
'<span style="background:#dbeafe;color:#1e40af">Nina<span class="tip">onderwerp</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">vivía<span class="tip">imperfecto — achtergrond/gewoonte</span></span> '+
'<span style="background:#dcfce7;color:#166534">en un pueblo<span class="tip">plaats</span></span>.</div>'+
'<div class="legend"><span><i style="background:#d8b4fe"></i>marcador</span><span><i style="background:#93c5fd"></i>persoon</span><span><i style="background:#fdba74"></i>imperfecto</span><span><i style="background:#86efac"></i>plaats</span></div>'+
'<p class="gloss" style="margin-top:8px">🟠 Het <b>imperfecto</b> = gewoonte/beschrijving. -ar → -aba · -er/-ir → -ía. · '+(TTS?'<button class="spk-btn" onclick="speak(\'De pequeña Nina vivía en un pueblo\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: imperfecto — klik om te onthullen ----
(function(){const el=document.getElementById('irconj');
 const R=[['yo','jugaba'],['tú','jugabas'],['él/ella','jugaba'],['nosotros','jugábamos'],['vosotros','jugabais'],['ellos','jugaban']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">el imperfecto (jugar) — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">-ar → aba/abas/aba/ábamos/abais/aban. yo = él/ella.</p><div class="conjgrid" id="icg"></div>';
 const g=el.querySelector('#icg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v;if(TTS)speak(p+' '+v);};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: imperfecto — ¿qué forma? ----
function gameCantidad(){const el=document.getElementById('g_cantidad');
 const items=[['Nina ___ (vivir) en un pueblo.','vivía','vivir → vivía'],['(Ella) ___ (ser) tímida.','era','ser → era'],['(Yo) ___ (ir) a la escuela.','iba','ir → iba'],['(Ella) ___ (tener) un perro.','tenía','tener → tenía'],['(Yo) ___ (jugar) en el patio.','jugaba','jugar → jugaba'],['(Yo) ___ (ver) dibujos.','veía','ver → veía'],['___ (haber) menos coches.','había','haber → había'],['Nosotros ___ (comer) en casa.','comíamos','nosotros → comíamos'],['Los niños ___ (jugar) fuera.','jugaban','ellos → jugaban'],['Mi abuela ___ (hacer) pan.','hacía','hacer → hacía']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>el imperfecto — ¿qué forma?</h3><p class="desc">-ar → -aba · -er/-ir → -ía · era/iba/veía.</p>'+scoreBar('sbC')+'<div id="cW" style="font-size:17px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" id="cC" style="justify-content:center"></div><div class="fb" id="cFb"></div>';
 const sb=el.querySelector('#sbC');const cont=el.querySelector('#cC');
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#cW').textContent=el.cur[0];cont.innerHTML='';
   const opts=[el.cur[1]];const p2=['vivía','era','iba','tenía','jugaba','veía','había','comía','hacía'];while(opts.length<3){const x=p2[Math.floor(Math.random()*p2.length)];if(opts.indexOf(x)<0)opts.push(x);}
   for(let k=opts.length-1;k>0;k--){const j=Math.floor(Math.random()*(k+1));[opts[k],opts[j]]=[opts[j],opts[k]];}
   opts.forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});el.querySelector('#cFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#cFb'),ok,(ok?'¡Sí! ':'Nee: '+el.cur[1]+' ')+'('+el.cur[2]+').');setTimeout(next,1000);}
 next();}
// ---- GRAMMAR-VIZ 4: comparativos ----
function gamePron(){const el=document.getElementById('g_pron');
 const items=[['La ciudad es ___ grande que el pueblo. (groter)','más','más … que'],['Es ___ alto como yo. (even)','tan','tan … como'],['Antes era ___ tímido que ahora. (minder)','menos','menos … que'],['Es ___ rápido como un tren. (even)','tan','tan … como'],['Hoy hace ___ calor que ayer. (meer)','más','más … que'],['Corre ___ rápido como yo. (even)','tan','tan … como'],['El pueblo es ___ tranquilo que la ciudad. (rustiger)','más','más … que'],['Había ___ coches que ahora. (minder)','menos','menos … que'],['Es ___ simpática como Diego. (even)','tan','tan … como'],['Este libro es ___ interesante que ese. (meer)','más','más … que']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>Comparativos — ¿más, menos o tan?</h3><p class="desc">más/menos … QUE · tan … COMO.</p>'+scoreBar('sbP')+'<div id="pQ" style="font-size:16px;font-family:var(--disp);text-align:center;margin:10px 0"></div><div class="chips" id="pC" style="justify-content:center"></div><div class="fb" id="pFb"></div>';
 const sb=el.querySelector('#sbP');const cont=el.querySelector('#pC');
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#pQ').textContent=el.cur[0];cont.innerHTML='';['más','menos','tan'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});el.querySelector('#pFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#pFb'),ok,(ok?'¡Sí! ':'Nee: ')+el.cur[1]+' ('+el.cur[2]+').');setTimeout(next,1100);}
 next();}

// ---- MOTOR-ARCADE: 20 spellen, ingebed ----
document.getElementById('motorlink').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 4px">Arcade · la máquina de juegos 🕹️</h3><p class="gloss" style="margin:0 0 10px">'+MOTOR.reduce((n,g)=>n+g[1].length,0)+' extra spellen met score & directe feedback — ingebed, dus ze werken ook als je dit bestand downloadt. Klik om te spelen.</p>'+MOTOR.map(([grp,gs])=>'<div class="subh">'+grp+'</div><div class="fcgrid">'+
   gs.map(([f,t,tpl])=>'<div class="chip" style="display:block;border-radius:14px" onclick="openGame(\''+f+'\',\''+t.replace(/'/g,"")+'\')"><div style="font-weight:700;color:var(--ink);font-size:14px">'+t+'</div><div class="pill" style="margin-top:4px;font-size:10px">'+tpl+'</div></div>').join('')+'</div>').join('');
function openGame(slug,title){const g=GAMES[slug];if(!g){alert('Spel niet gevonden.');return;}
  document.getElementById('gmtitle').textContent=title;document.getElementById('gframe').src='data:text/html;base64,'+g;document.getElementById('gmodal').classList.add('show');}
function closeGame(){document.getElementById('gmodal').classList.remove('show');document.getElementById('gframe').src='about:blank';}
document.getElementById('gmodal').addEventListener('click',e=>{if(e.target.id==='gmodal')closeGame();});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeGame();});

// ---- KAART interactief ----
(function(){
       const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "👪 En familia: a los 15 años se celebra la quinceañera", "star": 1, "nl": "Parada anterior (U3) · CDMX (Diego)"}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "👪 En familia: se llevan dos apellidos (padre y madre)", "star": 1, "nl": "Parada anterior (U0–U1) · el mundo hispano · España (Lucía)"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "👪 En familia: la familia extensa es muy unida", "star": 1, "nl": "Parada anterior (U2) · Cartagena (Valen)"}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "👪 En familia: muchos apellidos tienen raíces quechuas", "star": 1, "nl": "★ ¡Estás aquí! Parada U6 · Cusco (Nina)"}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "👪 En familia: el domingo es día de asado en familia", "star": 1, "nl": "Parada anterior (U5) · Buenos Aires (Mateo · voseo)"}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "👪 En familia: en Navidad se reúnen con hallacas", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "👪 En familia: existe el «Día de la Familia»", "star": 1, "nl": "Parada anterior (U4) · Chile · el gran viaje (Patagonia, Atacama)"}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "👪 En familia: familias grandes, muchas kichwas", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "👪 En familia: las familias mayas transmiten su idioma en casa", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "👪 En familia: varias generaciones viven juntas", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "👪 En familia: la «cholita» y la pollera, herencia familiar", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "👪 En familia: la familia se reúne los domingos con música", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "👪 En familia: familias numerosas y muy unidas", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "👪 En familia: en casa la familia habla guaraní", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "👪 En familia: la familia celebra «la Purísima»", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "👪 En familia: muchas familias tienen parientes en EE. UU.", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "👪 En familia: entre familia y amigos se dice «mae»", "star": 0, "nl": ""}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "👪 En familia: familias diversas por el Canal (todo el mundo)", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "👪 En familia: el mate se comparte en familia", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "👪 En familia: la familia mezcla lo taíno, africano y español", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "👪 En familia: familias con lenguas fang y bubi en casa", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "👪 En familia: familias hispanas bilingües (español + inglés)", "star": 0, "nl": ""}};
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
 const P=[{n:'Nina 🇵🇪',raw:'De pequeña vivía en un pueblo cerca de Cusco. La casa de mi abuela era de adobe y tenía un patio grande. Todos los días iba a la escuela a pie y jugaba con mis primos. Había menos coches y todo era más tranquilo que ahora. Un día llegó mi tío con una bici. Echo de menos esa época.',
    html:'De pequeña <span class="ev">vivía</span> en un pueblo cerca de Cusco. La casa de mi abuela <span class="ev">era</span> de adobe y <span class="ev">tenía</span> un patio grande. Todos los días <span class="ev">iba</span> a la escuela a pie y <span class="ev">jugaba</span> con mis primos. <span class="ev">Había</span> menos coches y todo <span class="ev">era más tranquilo que</span> ahora. Un día <span class="ev">llegó</span> mi tío con una bici.'},
   {n:'Diego 🇲🇽',raw:'Yo crecí en la ciudad. De niño veía mucha tele y jugaba a videojuegos. Mi barrio era más ruidoso que el de Nina. Tenía muchos amigos e íbamos al parque. Un día gané un concurso de dibujo en la escuela. Ahora todo es diferente, pero también me gusta.',
    html:'Yo <span class="ev">crecí</span> en la ciudad. De niño <span class="ev">veía</span> mucha tele y <span class="ev">jugaba</span> a videojuegos. Mi barrio <span class="ev">era más ruidoso que</span> el de Nina. <span class="ev">Tenía</span> muchos amigos e <span class="ev">íbamos</span> al parque. Un día <span class="ev">gané</span> un concurso de dibujo.'}];
 el.innerHTML='<div class="perfiles">'+P.map((m,i)=>'<div class="perfil"><h4>👤 '+m.n+' '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lm'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div class="txt" id="lm'+i+'" data-raw="'+m.raw.replace(/"/g,'&quot;')+'">'+m.html+'</div></div>').join('')+'</div>';
 const items=[['Nina vivía en un pueblo cerca de Cusco.',true,'«vivía en un pueblo cerca de Cusco»'],['Para Nina, todo era más ruidoso que ahora.',false,'«todo era más tranquilo que ahora»'],['La casa de la abuela tenía un patio grande.',true,'«tenía un patio grande»'],['Diego creció en la ciudad.',true,'«crecí en la ciudad»'],['Diego de niño leía muchos libros.',false,'«veía mucha tele y jugaba a videojuegos»'],['El barrio de Diego era más ruidoso que el de Nina.',true,'«era más ruidoso que el de Nina»'],['Un día llegó el tío de Nina con una bici.',true,'«Un día llegó mi tío con una bici»'],['Diego ganó un concurso de matemáticas.',false,'«un concurso de dibujo»']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — con evidencia</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">¿Y tú? Reacciona</h3><p class="gloss" style="margin:0 0 8px">¿Tu infancia se parece más a la de Nina o a la de Diego? Escribe 2–3 frases con het <b>imperfecto</b> + una comparación (más… que). Grábalo en <b>Hablar 🎙️</b>.</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="De pequeño/a yo… Mi vida era más… que…"></textarea>';
 el.appendChild(box);el.appendChild(resp);}

// ---------- INLINE RECORDER (MediaRecorder) ----------
""" + hub_drills.RECORDER_JS + r"""
function buildRecorders(){
 makeRecorder('rec_repite',{title:'Escucha y repite: mi infancia',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'De pequeña vivía en un pueblo.',cue:'imperfecto',tip:'Duidelijk? Probeer nog eens zonder te lezen.'},{text:'Tenía un perro y jugaba en la calle.',cue:'imperfecto'},{text:'Todos los días iba a la escuela a pie.',cue:'imperfecto (ir)'},{text:'Mi abuela era muy amable.',cue:'imperfecto (ser)'},{text:'Jugaba cuando, de repente, empezó a llover.',cue:'contraste'},{text:'Antes el pueblo era más tranquilo que la ciudad.',cue:'comparativo'}]});
 makeRecorder('rec_pedido',{title:'Mensaje de voz: mi infancia',desc:'Neem één bericht op (30–40 s): vertel hoe je jeugd was (gebruik 3× het imperfecto).',items:[
   {text:'Cuenta cómo era tu infancia (usa 3 veces el imperfecto: vivía, tenía, jugaba).',cue:'mi infancia',tip:'3× het imperfecto (achtergrond/gewoonte)? Neem opnieuw op.'}]});
 makeRecorder('rec_plato',{title:'Mensaje de voz: antes y ahora',desc:'Vergelijk vroeger met nu.',items:[
   {text:'Compara antes y ahora y da tu opinión (más/menos… que · creo que antes…).',cue:'antes ↔ ahora',tip:'una comparación + una opinión? Herneem.'}]});
}

// ================= INLINE ZELFCORRIGERENDE OEFENINGEN =================
""" + hub_drills.HELPERS_JS + hub_drills.TYPE_JS + hub_drills.ESCUCHA_JS + hub_drills.LECTURA_JS + r"""

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
 // ===== IMPERFECTO =====
 buildChoice('gx_cantq',{title:'El imperfecto — ¿qué forma?',desc:'-ar → -aba · -er/-ir → -ía · era/iba/veía.',per:8,pool:[
   {q:'De pequeña, Nina ___ (vivir) en un pueblo.',opts:['vivía','vivió','vive'],ans:'vivía',why:'vivir → vivía'},
   {q:'(Ella) ___ (ser) muy tímida.',opts:['era','fue','es'],ans:'era',why:'ser → era'},
   {q:'Todos los días ___ (ir, ella) a la escuela.',opts:['iba','fue','va'],ans:'iba',why:'ir → iba'},
   {q:'(Ella) ___ (tener) un perro.',opts:['tenía','tuvo','tiene'],ans:'tenía',why:'tener → tenía'},
   {q:'(Yo) ___ (jugar) en el patio.',opts:['jugaba','jugué','juego'],ans:'jugaba',why:'jugar → jugaba'},
   {q:'Nosotros ___ (comer) en casa.',opts:['comíamos','comimos','comemos'],ans:'comíamos',why:'nosotros → comíamos'},
   {q:'Por la tarde (yo) ___ (ver) dibujos.',opts:['veía','vi','veo'],ans:'veía',why:'ver → veía'},
   {q:'___ (haber) menos coches antes.',opts:['Había','Hubo','Hay'],ans:'Había',why:'haber → había'},
   {q:'Mi abuela ___ (hacer) pan cada día.',opts:['hacía','hizo','hace'],ans:'hacía',why:'hacer → hacía'},
   {q:'Los niños ___ (jugar) en la calle.',opts:['jugaban','jugaron','juegan'],ans:'jugaban',why:'ellos → jugaban'},
   {q:'(Yo) ___ (aprender) a leer.',opts:['aprendía','aprendí','aprendo'],ans:'aprendía',why:'aprender → aprendía'},
   {q:'(Nosotros) ___ (ir) al parque.',opts:['íbamos','fuimos','vamos'],ans:'íbamos',why:'ir → íbamos'}]});
 buildChoice('gx_reg',{title:'Forma el imperfecto',desc:'Kies de juiste vorm.',per:8,pool:[
   {q:'jugar → yo',opts:['jugaba','jugaría','jugué'],ans:'jugaba',why:'-aba'},
   {q:'comer → yo',opts:['comía','comiba','comí'],ans:'comía',why:'-ía'},
   {q:'vivir → yo',opts:['vivía','viviba','viví'],ans:'vivía',why:'-ía'},
   {q:'ser → él',opts:['era','sería','fue'],ans:'era',why:'irregular'},
   {q:'ir → yo',opts:['iba','iría','fui'],ans:'iba',why:'irregular'},
   {q:'ver → él',opts:['veía','vería','vio'],ans:'veía',why:'irregular'},
   {q:'tener → yo',opts:['tenía','teniba','tuve'],ans:'tenía',why:'-ía'},
   {q:'jugar → nosotros',opts:['jugábamos','jugabamos','jugamos'],ans:'jugábamos',why:'accent -ábamos'},
   {q:'hacer → él',opts:['hacía','haciba','hizo'],ans:'hacía',why:'-ía'},
   {q:'estudiar → ellos',opts:['estudiaban','estudiában','estudiaron'],ans:'estudiaban',why:'-aban'}]});
 buildChoice('gx_adj',{title:'El imperfecto — mezclado',desc:'Alles door elkaar. Directe feedback.',per:8,pool:[
   {q:'(Yo) ___ (ser) tímido.',opts:['era','fui','soy'],ans:'era',why:'ser → era'},
   {q:'Antes ___ (haber) menos coches.',opts:['había','hubo','hay'],ans:'había',why:'haber → había'},
   {q:'(Nosotros) ___ (cuidar) a los abuelos.',opts:['cuidábamos','cuidamos','cuidaron'],ans:'cuidábamos',why:'nosotros'},
   {q:'¿(Tú) ___ (vivir) en la ciudad?',opts:['vivías','viviste','vives'],ans:'vivías',why:'tú → vivías'},
   {q:'Mi maestra ___ (ser) amable.',opts:['era','fue','es'],ans:'era',why:'ser → era'},
   {q:'(Yo) ___ (tener) cinco años.',opts:['tenía','tuve','tengo'],ans:'tenía',why:'leeftijd → imperfecto'},
   {q:'Los abuelos ___ (vivir) en el pueblo.',opts:['vivían','vivieron','viven'],ans:'vivían',why:'ellos → vivían'},
   {q:'(Yo) ___ (soñar) con ser piloto.',opts:['soñaba','soñé','sueño'],ans:'soñaba',why:'soñar → soñaba'},
   {q:'Por la mañana ___ (ir, yo) al mercado.',opts:['iba','fui','voy'],ans:'iba',why:'gewoonte → iba'},
   {q:'La escuela ___ (tener) un patio grande.',opts:['tenía','tuvo','tiene'],ans:'tenía',why:'beschrijving → tenía'}]});
 // ===== CONTRASTE =====
 buildChoice('gx_pronq',{title:'¿indefinido o imperfecto?',desc:'achtergrond → imperfecto · gebeurtenis → indefinido.',per:8,pool:[
   {q:'(Yo) ___ en el patio cuando llegó mi madre.',opts:['jugaba','jugué','juego'],ans:'jugaba',why:'achtergrond → imperfecto'},
   {q:'Jugaba cuando, de repente, ___ a llover.',opts:['empezó','empezaba','empieza'],ans:'empezó',why:'gebeurtenis → indefinido'},
   {q:'___ de noche y llovía.',opts:['Era','Fue','Es'],ans:'Era',why:'decor → imperfecto'},
   {q:'Nina vivía en Cusco cuando ___ su hermano.',opts:['nació','nacía','nace'],ans:'nació',why:'gebeurtenis → indefinido'},
   {q:'Todos los días ___ al parque.',opts:['iba','fui','voy'],ans:'iba',why:'gewoonte → imperfecto'},
   {q:'Ayer ___ a mi abuela.',opts:['visité','visitaba','visito'],ans:'visité',why:'ayer → indefinido'},
   {q:'Mientras (yo) ___, sonó el teléfono.',opts:['estudiaba','estudié','estudio'],ans:'estudiaba',why:'mientras → imperfecto'},
   {q:'Un día ___ un concurso.',opts:['gané','ganaba','gano'],ans:'gané',why:'un día → indefinido'},
   {q:'La casa ___ grande.',opts:['era','fue','es'],ans:'era',why:'beschrijving → imperfecto'},
   {q:'De repente, ___ mi tío.',opts:['llegó','llegaba','llega'],ans:'llegó',why:'de repente → indefinido'}]});
 buildChoice('gx_ser',{title:'¿fondo o acción?',desc:'Achtergrond (imperfecto) of gebeurtenis (indefinido)?',per:7,pool:[
   {q:'«Era de noche» =',opts:['imperfecto (achtergrond)','indefinido (feit)'],ans:'imperfecto (achtergrond)',why:'decor'},
   {q:'«Sonó el teléfono» =',opts:['indefinido (feit)','imperfecto (achtergrond)'],ans:'indefinido (feit)',why:'gebeurtenis'},
   {q:'«Siempre jugaba» =',opts:['imperfecto (gewoonte)','indefinido (feit)'],ans:'imperfecto (gewoonte)',why:'siempre'},
   {q:'«Un día llegó» =',opts:['indefinido (feit)','imperfecto (achtergrond)'],ans:'indefinido (feit)',why:'un día'},
   {q:'«Tenía cinco años» =',opts:['imperfecto (beschrijving)','indefinido (feit)'],ans:'imperfecto (beschrijving)',why:'leeftijd'},
   {q:'«De repente empezó» =',opts:['indefinido (feit)','imperfecto (achtergrond)'],ans:'indefinido (feit)',why:'de repente'},
   {q:'«La casa era bonita» =',opts:['imperfecto (beschrijving)','indefinido (feit)'],ans:'imperfecto (beschrijving)',why:'beschrijving'},
   {q:'«Ayer conocí a Nina» =',opts:['indefinido (feit)','imperfecto (achtergrond)'],ans:'indefinido (feit)',why:'ayer'}]});
 buildOrder('gx_build',{title:'Ordena la frase',desc:'Tik de woorden in de juiste volgorde.',rounds:[
   {sub:'imperfecto',items:[{label:'De pequeña',key:1},{label:'Nina',key:2},{label:'vivía',key:3},{label:'en un pueblo.',key:4}]},
   {sub:'contraste',items:[{label:'Jugaba en el patio',key:1},{label:'cuando,',key:2},{label:'de repente,',key:3},{label:'empezó a llover.',key:4}]},
   {sub:'comparativo',items:[{label:'El pueblo',key:1},{label:'era más',key:2},{label:'tranquilo',key:3},{label:'que la ciudad.',key:4}]},
   {sub:'relativo que',items:[{label:'El niño',key:1},{label:'que',key:2},{label:'jugaba en la calle',key:3},{label:'era yo.',key:4}]},
   {sub:'gewoonte',items:[{label:'Todos los días',key:1},{label:'íbamos',key:2},{label:'al parque',key:3},{label:'a jugar.',key:4}]}]});
 // ===== COMPARATIVOS + RELATIVO =====
 buildChoice('gx_iraq',{title:'¿más, menos, tan?',desc:'más/menos … que · tan … como.',per:8,pool:[
   {q:'La ciudad es ___ grande que el pueblo. (groter)',opts:['más','menos','tan'],ans:'más',why:'más…que'},
   {q:'Es ___ alto como yo. (even)',opts:['tan','más','menos'],ans:'tan',why:'tan…como'},
   {q:'Hoy hace ___ calor que ayer. (meer)',opts:['más','menos','tan'],ans:'más',why:'más…que'},
   {q:'Antes era ___ tímido que ahora. (minder)',opts:['menos','más','tan'],ans:'menos',why:'menos…que'},
   {q:'Corre ___ rápido como yo. (even)',opts:['tan','más','menos'],ans:'tan',why:'tan…como'},
   {q:'El pueblo es ___ tranquilo que la ciudad. (rustiger)',opts:['más','menos','tan'],ans:'más',why:'más…que'},
   {q:'Había ___ coches que ahora. (minder)',opts:['menos','más','tan'],ans:'menos',why:'menos…que'},
   {q:'Es ___ divertido como un juego. (even)',opts:['tan','más','menos'],ans:'tan',why:'tan…como'},
   {q:'Este libro es ___ interesante que ese. (meer)',opts:['más','menos','tan'],ans:'más',why:'más…que'},
   {q:'Mi perro es ___ grande como el tuyo. (even)',opts:['tan','más','menos'],ans:'tan',why:'tan…como'}]});
 buildChoice('gx_subj',{title:'Los comparativos irregulares',desc:'Kies de onregelmatige comparativo.',per:6,pool:[
   {q:'Este libro es (bueno) ___ que ese.',opts:['mejor','más bueno','tan bueno'],ans:'mejor',why:'bueno → mejor'},
   {q:'Hoy es (malo) ___ que ayer.',opts:['peor','más malo','tan malo'],ans:'peor',why:'malo → peor'},
   {q:'Mi hermana es (viejo) ___ que yo.',opts:['mayor','más vieja','tan vieja'],ans:'mayor',why:'personen → mayor'},
   {q:'Soy (joven) ___ que mi primo.',opts:['menor','más joven','tan joven'],ans:'menor',why:'personen → menor'},
   {q:'Esta peli es (bueno) ___ que la otra.',opts:['mejor','más buena','tan buena'],ans:'mejor',why:'bueno → mejor'},
   {q:'El tiempo hoy es (malo) ___ que ayer.',opts:['peor','más malo','tan malo'],ans:'peor',why:'malo → peor'}]});
 buildChoice('gx_plural',{title:'Que / donde',desc:'Betrekkelijke bijzin: que (die/dat) of donde (waar).',per:6,pool:[
   {q:'El niño ___ jugaba era yo.',opts:['que','donde','como'],ans:'que',why:'que = die'},
   {q:'La casa ___ vivía era grande.',opts:['donde','que','cuando'],ans:'donde',why:'donde = waar'},
   {q:'El perro ___ tenía manchas.',opts:['que','donde','como'],ans:'que',why:'que = dat'},
   {q:'El pueblo ___ crecí es pequeño.',opts:['donde','que','como'],ans:'donde',why:'donde = waar'},
   {q:'La escuela ___ estudiaba era vieja.',opts:['donde','que','cuando'],ans:'donde',why:'donde = waar'},
   {q:'La amiga ___ me visitaba era Nina.',opts:['que','donde','como'],ans:'que',why:'que = die'}]});
 buildChoice('gx_nac',{title:'Traduce — imperfecto/comparación',desc:'Kies de correcte Spaanse zin.',per:6,pool:[
   {q:'Als kind woonde ik in een dorp. →',opts:['De pequeño vivía en un pueblo.','De pequeño viví en un pueblo.','De pequeño vivo en un pueblo.'],ans:'De pequeño vivía en un pueblo.',why:'imperfecto'},
   {q:'De stad is groter dan het dorp. →',opts:['La ciudad es más grande que el pueblo.','La ciudad es tan grande que el pueblo.','La ciudad es más grande como el pueblo.'],ans:'La ciudad es más grande que el pueblo.',why:'más…que'},
   {q:'Ik ben even oud als jij. →',opts:['Soy tan mayor como tú.','Soy más mayor que tú.','Soy menos mayor que tú.'],ans:'Soy tan mayor como tú.',why:'tan…como'},
   {q:'Dit is beter dan dat. →',opts:['Esto es mejor que eso.','Esto es más bueno que eso.','Esto es tan bueno como eso.'],ans:'Esto es mejor que eso.',why:'mejor'},
   {q:'Vroeger ging ik naar school te voet. →',opts:['Antes iba a la escuela a pie.','Antes fui a la escuela a pie.','Antes voy a la escuela a pie.'],ans:'Antes iba a la escuela a pie.',why:'gewoonte → iba'},
   {q:'Het kind dat speelde was ik. →',opts:['El niño que jugaba era yo.','El niño donde jugaba era yo.','El niño que jugó era yo.'],ans:'El niño que jugaba era yo.',why:'que + imperfecto'}]});
 buildMatch('gx_conc',{title:'Empareja: infinitivo ↔ imperfecto',desc:'Koppel het werkwoord aan het imperfecto (yo/él).',per:6,pool:[
   {a:'ser',b:'era'},{a:'ir',b:'iba'},{a:'ver',b:'veía'},{a:'tener',b:'tenía'},
   {a:'jugar',b:'jugaba'},{a:'comer',b:'comía'},{a:'vivir',b:'vivía'},{a:'haber',b:'había'}]});
 buildMatch('gx_conc2',{title:'Empareja: antes ↔ opuesto',desc:'Koppel het tegengestelde/paar.',per:6,pool:[
   {a:'antes',b:'ahora'},{a:'ya no',b:'todavía'},{a:'más',b:'menos'},{a:'mejor',b:'peor'},
   {a:'mayor',b:'menor'},{a:'feliz',b:'triste'}]});
 buildChoice('gx_mix',{title:'Repaso mixto — imperfecto + contraste + comparativos',desc:'Alles door elkaar. Directe feedback.',per:8,pool:[
   {q:'(Yo) ___ (jugar) en el patio.',opts:['jugaba','jugué','juego'],ans:'jugaba',why:'gewoonte → imperfecto'},
   {q:'ser → imperfecto (él)',opts:['era','fue','es'],ans:'era',why:'era'},
   {q:'Un día ___ (llegar) mi tío.',opts:['llegó','llegaba','llega'],ans:'llegó',why:'un día → indefinido'},
   {q:'La ciudad es ___ grande que el pueblo.',opts:['más','tan','menos'],ans:'más',why:'más…que'},
   {q:'ir → imperfecto (yo)',opts:['iba','fui','voy'],ans:'iba',why:'iba'},
   {q:'«beter dan» =',opts:['mejor que','más bueno que','tan bueno como'],ans:'mejor que',why:'irregular'},
   {q:'Era de noche cuando ___ el teléfono.',opts:['sonó','sonaba','suena'],ans:'sonó',why:'gebeurtenis → indefinido'},
   {q:'El niño ___ jugaba era yo.',opts:['que','donde','como'],ans:'que',why:'que'},
   {q:'ver → imperfecto (él)',opts:['veía','vio','ve'],ans:'veía',why:'veía'},
   {q:'Es ___ alto como yo.',opts:['tan','más','menos'],ans:'tan',why:'tan…como'},
   {q:'Todos los días ___ (comer) pan.',opts:['comía','comí','como'],ans:'comía',why:'gewoonte → imperfecto'},
   {q:'«niet meer» =',opts:['ya no','todavía','siempre'],ans:'ya no',why:'antes/ahora'}]});
 // ===== VOCABULARIO =====
 buildMatch('vx_match',{title:'Empareja: palabra ↔ emoji',desc:'Koppel het woord aan de emoji.',per:6,pool:[
   {a:'el juguete',b:'🧸'},{a:'la escuela',b:'🏫'},{a:'los abuelos',b:'👵'},{a:'la mascota',b:'🐶'},
   {a:'el patio',b:'⛲'},{a:'el pueblo',b:'🏘️'},{a:'jugar',b:'🪀'},{a:'soñar',b:'💭'},
   {a:'el recuerdo',b:'📷'},{a:'aprender',b:'📚'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat past.',per:6,pool:[
   {q:'De pequeño jugaba en el ___ de la escuela.',opts:['patio','recuerdo','pueblo'],ans:'patio',why:'speelplaats'},
   {q:'Visitaba a mis ___ los domingos.',opts:['abuelos','juguetes','vecinos'],ans:'abuelos',why:'grootouders'},
   {q:'Tenía un perro de ___.',opts:['mascota','escuela','época'],ans:'mascota',why:'huisdier'},
   {q:'Mi maestra ___ muy amable.',opts:['era','fue','es'],ans:'era',why:'imperfecto'},
   {q:'Antes vivía en un ___ pequeño.',opts:['pueblo','recreo','juguete'],ans:'pueblo',why:'dorp'},
   {q:'La ciudad es más grande ___ el pueblo.',opts:['que','como','de'],ans:'que',why:'más…que'},
   {q:'___ jugaba, ahora estudio.',opts:['Antes','Ahora','Todavía'],ans:'Antes',why:'vroeger'},
   {q:'Echo de ___ mi infancia.',opts:['menos','más','nada'],ans:'menos',why:'echar de menos'},
   {q:'Todos los días ___ a la escuela a pie.',opts:['iba','fui','voy'],ans:'iba',why:'gewoonte → iba'},
   {q:'El niño ___ jugaba era yo.',opts:['que','donde','como'],ans:'que',why:'betrekkelijk que'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het woord.',per:6,pool:[
   {q:'De ruimte waar kinderen op school spelen:',opts:['el patio','el pueblo','la época'],ans:'el patio',why:'speelplaats'},
   {q:'Iets uit het verleden dat je bijblijft:',opts:['el recuerdo','el juguete','la mascota'],ans:'el recuerdo',why:'herinnering'},
   {q:'De ouders van je ouders:',opts:['los abuelos','los vecinos','los compañeros'],ans:'los abuelos',why:'grootouders'},
   {q:'«als kind»:',opts:['de pequeño','ahora','todavía'],ans:'de pequeño',why:'als kind'},
   {q:'De él/ella-vorm van «ser» in imperfecto:',opts:['era','fue','es'],ans:'era',why:'era'},
   {q:'«even groot als» =',opts:['tan grande como','más grande que','menos grande que'],ans:'tan grande como',why:'tan…como'},
   {q:'«niet meer» =',opts:['ya no','todavía','siempre'],ans:'ya no',why:'antes/ahora'},
   {q:'«missen» (iemand/iets):',opts:['echar de menos','aprender','cuidar'],ans:'echar de menos',why:'missen'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['el juguete','el patio','la escuela','el avión'],odd:3,why:'el avión hoort niet bij de jeugd/school'},
   {words:['era','tenía','jugaba','jugó'],odd:3,why:'jugó is indefinido, geen imperfecto'},
   {words:['antes','ya no','todavía','muy'],odd:3,why:'muy is geen tijdsmarker'},
   {words:['más','menos','tan','que'],odd:3,why:'que is geen vergelijkingswoord'},
   {words:['mejor','peor','mayor','grande'],odd:3,why:'grande is geen irregular comparativo'},
   {words:['los abuelos','el vecino','la mascota','el trompo'],odd:3,why:'el trompo is speelgoed, geen persoon/dier'},
   {words:['era','iba','veía','fue'],odd:3,why:'fue is indefinido'},
   {words:['de pequeño','de niño','cuando era niño','mañana'],odd:3,why:'mañana is toekomst'}]});
 // ===== LECTURA =====
 buildOrder('lx_order',{title:'Ordena',desc:'Tik in de juiste volgorde.',rounds:[
   {sub:'la infancia de Nina',items:[{label:'De pequeña vivía en un pueblo.',key:1},{label:'Iba a la escuela a pie.',key:2},{label:'Jugaba con sus primos.',key:3},{label:'Un día llegó su tío con una bici.',key:4}]},
   {sub:'contraste',items:[{label:'Era de noche',key:1},{label:'y llovía',key:2},{label:'cuando, de repente,',key:3},{label:'sonó el teléfono.',key:4}]},
   {sub:'comparativo',items:[{label:'Antes',key:1},{label:'el pueblo',key:2},{label:'era más tranquilo',key:3},{label:'que la ciudad.',key:4}]},
   {sub:'relativo',items:[{label:'La casa',key:1},{label:'donde',key:2},{label:'vivía',key:3},{label:'era de adobe.',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in de twee teksten (Nina y Diego) en kies.',per:6,pool:[
   {q:'¿Dónde vivía Nina de pequeña?',opts:['en un pueblo cerca de Cusco','en la ciudad','en Lima'],ans:'en un pueblo cerca de Cusco',why:'«vivía en un pueblo cerca de Cusco»'},
   {q:'¿Cómo era la casa de la abuela?',opts:['de adobe con patio','de cristal','moderna'],ans:'de adobe con patio',why:'«era de adobe y tenía un patio»'},
   {q:'¿Cómo iba Nina a la escuela?',opts:['a pie','en coche','en bici'],ans:'a pie',why:'«iba a la escuela a pie»'},
   {q:'¿Qué hacía Diego de niño?',opts:['veía tele y jugaba a videojuegos','leía libros','pintaba'],ans:'veía tele y jugaba a videojuegos',why:'«veía mucha tele y jugaba a videojuegos»'},
   {q:'El barrio de Diego era…',opts:['más ruidoso que el de Nina','muy tranquilo','pequeño'],ans:'más ruidoso que el de Nina',why:'«era más ruidoso que el de Nina»'},
   {q:'¿Qué ganó Diego un día?',opts:['un concurso de dibujo','un partido','un premio de mates'],ans:'un concurso de dibujo',why:'«gané un concurso de dibujo»'},
   {q:'¿Qué echa de menos Nina?',opts:['esa época','la ciudad','el ruido'],ans:'esa época',why:'«Echo de menos esa época»'},
   {q:'Antes había… coches que ahora.',opts:['menos','más','tantos'],ans:'menos',why:'«Había menos coches»'}]});
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='C6plus_U6_web_mijn_versie.html';a.click();};
})();
"""

# Getypte woordenschat-drills (fase ophalen + produceren) in het paneel zelf.
JS += hub_type_sets.vocab_type_js(vocab)
JS += hub_type_gram.js('C6+', 6)
JS += (hub_bloques.escucha_js("esc_c6p_u6", escucha_data.C6P_U6)
       + hub_bloques.lectura_js("lec_c6p_u6", lectura_data.C6P_U6))
HTML = HTML.replace("__GRAMSLOTS__", hub_type_gram.slots('C6+', 6))
HTML = HTML.replace("__NGAMES__", str(len(GAMES)))
HTML = HTML.replace("__BRONNEN__", extra_bronnen.html('C6+', 6))
HTML = HTML.replace("__TYPESLOTS__", hub_type_sets.SLOTS_HTML)

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/C6plus_U6_web.html","w").write(html)
print("C6plus_U6_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
