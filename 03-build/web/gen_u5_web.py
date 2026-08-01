#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C5 · U5 «¡Ñam!».
# Eén standalone bestand: fonts base64, de 21 U5-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U5-vocab), visuele/interactieve grammatica (cantidades · ir a + inf · lo/la/los/las),
# klikbare kaart (mundo hispano, parada 5 = México) + TTS + inline recorder + Lectura + editbar. Huisstijl groen.
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
vocab = json.load(open(f"{ROOT}/01-cursussen/05-a1/U5/u5_vocab.json", encoding="utf-8"))
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
   ['comida-memoria', 'memoria de la comida', 'memory'],
   ['fruta-verdura-memoria', 'fruta y verdura', 'memory'],
   ['plato-pais', 'plato ↔ país', 'match'],
   ['plato-ingrediente', 'plato ↔ ingrediente', 'match']]],
 ['② Distinguir · léxico/gramática', [
   ['comida-bebida', '¿comida o bebida?', 'classify'],
   ['en-el-mercado', 'en el mercado: fruta · verdura · carne/pescado', 'classify'],
   ['cantidad', '¿mucho, mucha, muchos o muchas?', 'classify'],
   ['camarero-cliente', '¿camarero o cliente?', 'classify']]],
 ['③ Producir con apoyo', [
   ['voy-a', 'completa: ir a + infinitivo', 'cloze'],
   ['cantidad-cloze', 'completa la cantidad', 'cloze'],
   ['pronombre-cloze', '¿lo, la, los o las?', 'cloze'],
   ['cantidad-tetris', 'cantidades: cinta', 'belt'],
   ['orden-restaurante', 'ordena el diálogo', 'order'],
   ['receta-order', 'ordena la receta', 'order'],
   ['pon-la-mesa', 'pon la mesa', 'point'],
   ['senala-mercado', 'señala en el mercado', 'point']]],
 ['④ Analizar & comunicar', [
   ['pide', '¡pide en el restaurante!', 'sim']]],
 ['⑤ Hablar · grábate 🎙️', [
   ['repite-comida', 'escucha y repite', 'speak'],
   ['shadowing-diego', 'shadowing con Diego', 'speak'],
   ['mensaje-pedido', 'mensaje de voz: pide comida', 'speak'],
   ['describe-plato', 'describe tu plato', 'speak']]],
]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-u5-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-u5-{s}.html")}

CSS = FONTS + extra_bronnen.CSS + hub_drills.ESCUCHA_CSS + hub_drills.LECTURA_CSS + hub_drills.TYPE_CSS + """
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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="comida">comida</option><option value="fruta">fruta</option><option value="verdura">verdura</option><option value="bebida">bebida</option><option value="mesa">la mesa</option><option value="restaurante">restaurante</option><option value="cantidades">cantidades</option><option value="cortesia">cortesía</option><option value="mexico">sabores de América</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Español en la práctica · U5 ¡Ñam!</title>
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
    <div><h1>U5 · ¡Ñam!</h1>
    <p>La página digital de la Unidad 5 (parada <b>México · CDMX</b>): flashcards, gramática visual e interactiva y <b>__NGAMES__ juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie.</span></p></div>
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
    <p class="lead">Eerst betekenis en patroon ontdekken, dan de regel. Beweeg over de woorden, klik, en probeer. <span class="gloss">Alles binnen het thema van U5: cantidades, ir a + infinitivo y lo/la/los/las.</span></p>
    <div class="card" id="colorsent"></div>
    <div class="card" id="irconj"></div>
    <h3 class="subh">🧱 Ir a + infinitivo — construye y practica</h3>
    <div class="card ex" id="gx_build"></div>
    <div class="card ex" id="gx_iraq"></div>
    <h3 class="subh">⚖️ Cantidades — mucho/mucha/muchos/muchas</h3>
    <div class="game" id="g_cantidad"></div>
    <div class="card ex" id="gx_conc"></div>
    <div class="card ex" id="gx_cantq"></div>
    <h3 class="subh">🔁 Pronombres — lo/la/los/las</h3>
    <div class="game" id="g_pron"></div>
    <div class="card ex" id="gx_pronq"></div>
    <h3 class="subh">🎯 Repaso mixto — rellena con feedback</h3>
    <div class="card ex" id="gx_mix"></div>
  __GRAMSLOTS__
  </section>

  <section class="panel" data-p="lectura">
    <h2 class="sec">Lectura · dos cartas (menús)</h2>
    <p class="lead">Lees de <b>twee menu's</b>, <b>luister</b> ze (🔊 TTS) en <b>controleer je begrip</b>. Daarna zeg je wat je <b>vas a pedir</b> — dat neem je op in het tabblad <b>Hablar</b>. <span class="gloss">Keten: lezen → luisteren → spreken.</span></p>
    <div id="lecturawrap"></div>
    <h3 class="subh">🔢 Ordena la comida</h3>
    <div class="card ex" id="lx_order"></div>
    <h3 class="subh">🔎 Comprensión · escanea y escoge</h3>
    <div class="card ex" id="lx_scan"></div>
    <h2 class="sec">Lectura completa · el mercado de La Merced</h2>
    <p class="lead">Een echte infografie met de volledige leesroute: <b>voorspellen → globaal → scannen → juist/fout met bewijs → betekenis uit de context → zelf schrijven</b>. <span class="gloss">Dezelfde tekst staat in je cursus, met schrijfruimte.</span></p>
    <div class="card ex" id="lec_u5"></div>
  </section>

  <section class="panel" data-p="escuchar">
    <h2 class="sec">Escuchar · Una mesa para tres 🎧</h2>
    <p class="lead">Diego bestelt in een restaurant in CDMX — maar één gerecht is op. Eén fragment, zes stappen: eerst <b>weten waar je bent</b>, dan <b>globaal</b> luisteren, dan de <b>details</b>, dan <b>juist/fout met bewijs</b>. Het <b>transcript</b> gaat pas open als je klaar bent — anders lees je mee in plaats van te luisteren. <span class="gloss">Zolang er nog geen opname is, leest de computerstem het fragment voor.</span></p>
    <div class="card ex" id="esc_u5"></div>
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
    <p class="lead" style="margin-top:8px">Meer spreek-/opnamespellen (shadowing con Diego, describe…) vind je ook onder <b>Juegos ⑤</b>.</p>
  </section>

  <section class="panel" data-p="cultura">
    <h2 class="sec">Cultura · La comida mexicana</h2>
    <p class="lead">En el mundo hispano <b>la comida une a la gente</b>. Descubre los <b>tacos</b>, los <b>mercados</b> de México y compara los <b>horarios de comida</b>. <span class="gloss">In de Spaanstalige wereld verbindt eten; ontdek de taco, de markten en de eettijden.</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 11v3a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1v-3"/><path d="M12 19H4a1 1 0 0 1-1-1v-2a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-3.83"/><path d="m3 11 7.77-6.04a2 2 0 0 1 2.46 0L21 11H3Z"/></svg>El taco 🌮 🇲🇽</h3>
      <p>De <b>maíz</b>, con carne, verdura y <b>salsa</b>. En la CDMX hay <b>taquerías</b> por todas partes: al pastor, de pollo, de pescado… <span class="gloss">De taco is het hart van de Mexicaanse keuken — je deelt er meerdere.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/></svg>Los mercados y los horarios 🏪</h3>
      <p>En los <b>mercados</b> compras fruta, verdura y comida fresca; regatear el <b>precio</b> es normal. <b>Horario:</b> en España se cena muy tarde (21:30), en México y Bélgica un poco antes. <span class="gloss">De markt is dé plek om cantidades te oefenen. Contraste: la paella 🇪🇸 ↔ los tacos 🇲🇽 ↔ la arepa 🇨🇴 ↔ el ceviche 🇵🇪.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Platos típicos de México 🇲🇽</h3>
      <p><b>ES:</b> En México, comer es una fiesta y casi todo empieza con el <b>maíz</b>. Muchos platos se comen en la calle, en un <b>puesto</b> o en el mercado. <span class="gloss">In Mexico is eten een feest; bijna alles begint met maïs. Veel gerechten eet je op straat.</span></p>
      <div class="platos">
        <div class="pl"><div class="em">🌮</div><div class="nm">los tacos</div><small>tortilla + carne + salsa</small></div>
        <div class="pl"><div class="em">🥑</div><div class="nm">el guacamole</div><small>aguacate, lima, chile</small></div>
        <div class="pl"><div class="em">🫓</div><div class="nm">las quesadillas</div><small>tortilla con queso</small></div>
        <div class="pl"><div class="em">🌽</div><div class="nm">el elote</div><small>maíz de la calle</small></div>
        <div class="pl"><div class="em">🌶️</div><div class="nm">el pozole</div><small>sopa con maíz y carne</small></div>
      </div>
      <p><span class="gloss">¡Ojo! In Spanje = «la comida española» (tapas, paella); in Mexico andere smaken. Pittig = «picante» (met chile).</span></p></div>
    <h3 class="subh">📍 La Ruta · ¿dónde estamos?</h3>
    <p class="lead">Onze parada 5: <b>México · CDMX</b> 🇲🇽 (cruzamos el charco). <b>Klik op een groen land</b> op de kaart voor info. Verderop: Colombia → Perú.</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een groen land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    __BRONNEN__
  </section>

  <div class="foot">Español en la práctica · C5 · Unidad 5 «¡Ñam!» — página digital. Uitbreiding op de PDF · huisstijl groen · print ↔ PowerPoint ↔ web.</div>
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

// ---- GRAMMAR-VIZ 1: kleurgecodeerde ir-a-zin ----
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Ir a + infinitivo — el futuro próximo</h3>'+
'<div class="csent">'+
'<span style="background:#dbeafe;color:#1e40af">(Yo)<span class="tip">onderwerp</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">voy<span class="tip">ir · presente (voy, vas, va…)</span></span> '+
'<span style="background:#ede9fe;color:#5b21b6">a<span class="tip">verbindingswoord — vergeet «a» niet!</span></span> '+
'<span style="background:#dcfce7;color:#166534">comer<span class="tip">infinitivo (2e werkwoord)</span></span> '+
'<span style="background:#ccfbf1;color:#0f766e">un taco<span class="tip">voorwerp</span></span>.</div>'+
'<div class="legend"><span><i style="background:#93c5fd"></i>onderwerp</span><span><i style="background:#fdba74"></i>ir (presente)</span><span><i style="background:#c4b5fd"></i>a</span><span><i style="background:#86efac"></i>infinitivo</span><span><i style="background:#5eead4"></i>voorwerp</span></div>'+
'<p class="gloss" style="margin-top:8px">🔴 Vergeet de <b>a</b> niet: voy <b>a</b> comer. Het tweede werkwoord blijft <b>infinitief</b>. · '+(TTS?'<button class="spk-btn" onclick="speak(\'Voy a comer un taco\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: ir (presente) — klik om te onthullen ----
(function(){const el=document.getElementById('irconj');
 const R=[['yo','voy'],['tú','vas'],['él/ella','va'],['nosotros','vamos'],['vosotros','vais'],['ellos','van']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">El verbo «ir» — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">Denk eerst zelf de vorm; klik dan de kaart. Daarna: forma + a + infinitivo.</p><div class="conjgrid" id="icg"></div>';
 const g=el.querySelector('#icg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v+' a…';if(TTS)speak(p+' '+v+' a comer');};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: ¿mucho, mucha, muchos o muchas? ----
function gameCantidad(){const el=document.getElementById('g_cantidad');
 const items=[['pan','mucho','el pan (m)'],['fruta','mucha','la fruta (f)'],['tomates','muchos','los tomates (m pl)'],['manzanas','muchas','las manzanas (f pl)'],['arroz','mucho','el arroz (m)'],['leche','mucha','la leche (f)'],['huevos','muchos','los huevos (m pl)'],['uvas','muchas','las uvas (f pl)']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿mucho, mucha, muchos o muchas?</h3><p class="desc">Kies de vorm die past bij het woord (m/v · ev/mv).</p>'+scoreBar('sbC')+'<div id="cW" style="font-size:24px;font-family:var(--disp);text-align:center;margin:8px 0">___ <b></b></div><div class="chips" id="cC" style="justify-content:center"></div><div class="fb" id="cFb"></div>';
 const sb=el.querySelector('#sbC');const cont=el.querySelector('#cC');
 ['mucho','mucha','muchos','muchas'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#cW b').textContent=el.cur[0];el.querySelector('#cFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#cFb'),ok,(ok?'¡Sí! ':'Nee → ')+el.cur[1]+' '+el.cur[0]+' ('+el.cur[2]+').');setTimeout(next,950);}
 next();}
// ---- GRAMMAR-VIZ 4: ¿lo, la, los o las? ----
function gamePron(){const el=document.getElementById('g_pron');
 const items=[['la cuenta','la','v. ev.'],['el pan','lo','m. ev.'],['los tacos','los','m. mv.'],['las gambas','las','v. mv.'],['la carta','la','v. ev.'],['el postre','lo','m. ev.'],['los refrescos','los','m. mv.'],['las manzanas','las','v. mv.']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿lo, la, los o las?</h3><p class="desc">Welk pronomen vervangt het voorwerp? (la cuenta → la traigo)</p>'+scoreBar('sbP')+'<div id="pQ" style="font-size:20px;font-family:var(--disp);text-align:center;margin:10px 0"></div><div class="chips" id="pC" style="justify-content:center"></div><div class="fb" id="pFb"></div>';
 const sb=el.querySelector('#sbP');const cont=el.querySelector('#pC');
 ['lo','la','los','las'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#pQ').textContent='¿'+el.cur[0]+'? → ___ traigo';el.querySelector('#pFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#pFb'),ok,(ok?'¡Sí! ':'Nee → ')+el.cur[0]+' → '+el.cur[1]+' traigo ('+el.cur[2]+').');setTimeout(next,1000);}
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
   const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "🍽️ En la mesa: los tacos, el guacamole y el mole (base de maíz)", "star": 1, "nl": "★ ¡Estás aquí! Parada U5–U6 · CDMX · los mercados (Diego)"}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "🍽️ En la mesa: la paella, las tapas y la tortilla de patatas", "star": 1, "nl": "Parada anterior (U0–U4) · Madrid · Sevilla · Barcelona · València"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "🍽️ En la mesa: la arepa, la bandeja paisa y el café", "star": 0, "nl": ""}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "🍽️ En la mesa: el ceviche y el lomo saltado (cocina de fama mundial)", "star": 0, "nl": ""}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "🍽️ En la mesa: el asado, las empanadas y el dulce de leche", "star": 0, "nl": ""}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "🍽️ En la mesa: la arepa y el pabellón criollo", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "🍽️ En la mesa: las empanadas de pino y el pastel de choclo", "star": 0, "nl": ""}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "🍽️ En la mesa: el ceviche de camarón y el encebollado", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "🍽️ En la mesa: el pepián y los tamales", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "🍽️ En la mesa: «moros y cristianos» (arroz y frijoles) y la ropa vieja", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "🍽️ En la mesa: la salteña y el silpancho", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "🍽️ En la mesa: «la bandera»: arroz, habichuelas y carne", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "🍽️ En la mesa: las baleadas (tortilla con frijoles)", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "🍽️ En la mesa: la sopa paraguaya y la chipa", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "🍽️ En la mesa: el gallo pinto y el nacatamal", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "🍽️ En la mesa: las pupusas, plato nacional", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "🍽️ En la mesa: el gallo pinto y el «casado»", "star": 0, "nl": ""}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "🍽️ En la mesa: el sancocho y el arroz con pollo", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "🍽️ En la mesa: el asado y el chivito", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "🍽️ En la mesa: el mofongo y el arroz con gandules", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "🍽️ En la mesa: el pescado con yuca y plátano", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "🍽️ En la mesa: la comida tex-mex y los burritos (fusión latina)", "star": 0, "nl": ""}};
 const wrap=document.getElementById('mapwrap');const svg=wrap.querySelector('svg');const box=document.getElementById('mapinfo');
 if(!svg)return;
 svg.querySelectorAll('path.spa, path.usa').forEach(p=>{p.style.cursor='pointer';
   p.addEventListener('mouseenter',()=>{p.style.opacity='.75'});p.addEventListener('mouseleave',()=>{p.style.opacity=''});
   p.addEventListener('click',()=>{const c=p.getAttribute('data-c');const d=INFO[c];if(!d)return;
     box.innerHTML='<h3>'+d.fl+' '+d.n+' <span style="font-size:13px;color:var(--mut);font-weight:400">('+c+')</span>'+(d.star?' ★':'')+'</h3>'+'<div class="mrow"><b>🏛️ Capital:</b> '+d.cap+'</div>'+'<div class="mrow"><b>👥 Población:</b> '+d.pob+'</div>'+'<div class="mrow"><b>💰 Moneda:</b> '+d.mon+'</div>'+'<div class="mrow"><b>🗣️ Gentilicio:</b> '+d.gen+'</div>'+'<div class="mrow"><b>🌐 Idioma:</b> '+d.idi+'</div>'+(d.tema?'<div style="margin-top:8px;padding:8px 11px;background:rgba(255,255,255,.7);border-left:4px solid var(--gd);border-radius:7px;font-weight:600;color:var(--gd)">'+d.tema+'</div>':'')+(d.cool?'<div style="margin-top:8px;font-size:13px;line-height:1.5"><b>💡 ¿Sabías que…?</b> '+d.cool+'</div>':'')+(d.nl?'<div class="gloss" style="margin-top:6px">'+d.nl+'</div>':'');
     box.scrollIntoView({behavior:'smooth',block:'nearest'});});
 });
})();

// ---------- LECTURA: dos cartas (menús) + TTS + begrip ----------
function renderLectura(){const el=document.getElementById('lecturawrap');if(!el)return;
 const M=[{n:'La Cocina de Lucía 🇪🇸',raw:'De primero: sopa de tomate, cuatro euros; ensalada mixta, cinco euros. De segundo: pollo con patatas, nueve euros; pescado a la plancha, once euros. De postre: fruta del día, tres euros; churros con chocolate, cuatro euros.',
    html:'<div class="sec2">De primero</div><div class="mi"><span>Sopa de tomate</span><span class="pr">4 €</span></div><div class="mi"><span>Ensalada mixta</span><span class="pr">5 €</span></div><div class="sec2">De segundo</div><div class="mi"><span>Pollo con patatas</span><span class="pr">9 €</span></div><div class="mi"><span>Pescado a la plancha</span><span class="pr">11 €</span></div><div class="sec2">De postre</div><div class="mi"><span>Fruta del día</span><span class="pr">3 €</span></div><div class="mi"><span>Churros con chocolate</span><span class="pr">4 €</span></div>'},
   {n:'El Sabor de Diego 🇲🇽',raw:'Para empezar: guacamole con nachos, cinco euros; elote con queso, cuatro euros. Platos fuertes: tacos de pollo, ocho euros; ceviche de pescado, diez euros. Para terminar: flan casero, tres euros; piña con lima, tres euros.',
    html:'<div class="sec2">Para empezar</div><div class="mi"><span>Guacamole con nachos</span><span class="pr">5 €</span></div><div class="mi"><span>Elote con queso</span><span class="pr">4 €</span></div><div class="sec2">Platos fuertes</div><div class="mi"><span>Tacos de pollo (3)</span><span class="pr">8 €</span></div><div class="mi"><span>Ceviche de pescado</span><span class="pr">10 €</span></div><div class="sec2">Para terminar</div><div class="mi"><span>Flan casero</span><span class="pr">3 €</span></div><div class="mi"><span>Piña con lima</span><span class="pr">3 €</span></div>'}];
 el.innerHTML='<div class="perfiles">'+M.map((m,i)=>'<div class="menucard"><h4>🍽️ '+m.n+' '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lm'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div id="lm'+i+'" data-raw="'+m.raw.replace(/"/g,'&quot;')+'">'+m.html+'</div></div>').join('')+'</div>';
 const items=[['En casa de Diego hay tacos.',true,'«Tacos de pollo»'],['El pollo con patatas cuesta 9 €.',true,'«Pollo con patatas 9 €»'],['Los dos tienen postre de fruta.',true,'«Fruta del día» / «Piña con lima»'],['El ceviche es un postre.',false,'el ceviche es un plato fuerte (8-10 €)'],['La sopa de tomate cuesta cuatro euros.',true,'«Sopa de tomate 4 €»'],['El guacamole está en la carta de Diego.',true,'«Guacamole con nachos»'],['La ensalada mixta cuesta seis euros.',false,'cuesta cinco euros'],['Los tacos de Diego son de pescado.',false,'son «tacos de pollo»']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — comprueba tu comprensión (con evidencia)</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">¿Qué vas a pedir?</h3><p class="gloss" style="margin:0 0 8px">Kies één carta en zeg wat je vas a pedir (primero, segundo, postre, bebida) én waarom. Neem het op onder <b>Hablar 🎙️</b> («describe tu plato»).</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="Voy a pedir… porque…"></textarea>';
 el.appendChild(box);el.appendChild(resp);}

// ---------- INLINE RECORDER (MediaRecorder) ----------
""" + hub_drills.RECORDER_JS + r"""
function buildRecorders(){
 makeRecorder('rec_repite',{title:'Escucha y repite: pedir en el restaurante',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'Para mí, una sopa, por favor.',cue:'pedir',tip:'Duidelijk uitgesproken? Probeer nog eens.'},{text:'¿Me pone una botella de agua?',cue:'cortesía'},{text:'Voy a comer un taco.',cue:'ir a + infinitivo'},{text:'La cuenta, por favor.',cue:'pedir'},{text:'¡Que aproveche!',cue:'cortesía'}]});
 makeRecorder('rec_pedido',{title:'Mensaje de voz: pide comida',desc:'Neem één bericht op. Doel: eten bestellen voor een feestje. Gebruik: voy a comprar · un kilo de · una botella de · un poco de.',items:[
   {text:'Pide comida para una fiesta (30 s): ¿qué vas a comprar y cuánta cantidad?',cue:'para · la fiesta',tip:'3 productos + cantidad? Neem opnieuw op.'}]});
 makeRecorder('rec_plato',{title:'Describe tu plato favorito',desc:'Beschrijf je lievelingsgerecht: ¿qué es? ¿qué lleva? ¿por qué te gusta?',items:[
   {text:'Mi plato favorito es ___ . Lleva ___ . Me encanta porque ___ .',cue:'tu versión',tip:'Heb je gezegd wat het is, wat erin zit en waarom? Herneem.'}]});
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
 // GRAMÁTICA
 buildOrder('gx_build',{title:'Construye: ir a + infinitivo',desc:'Tik de blokjes in de juiste volgorde (onderwerp → ir → a → infinitivo → voorwerp).',rounds:[
   {sub:'yo · comer',items:[{label:'Yo',key:1},{label:'voy',key:2},{label:'a',key:3},{label:'comer',key:4},{label:'un taco',key:5}]},
   {sub:'tú · tomar',items:[{label:'¿Tú',key:1},{label:'vas',key:2},{label:'a',key:3},{label:'tomar',key:4},{label:'un café?',key:5}]},
   {sub:'nosotros · pedir',items:[{label:'Nosotros',key:1},{label:'vamos',key:2},{label:'a',key:3},{label:'pedir',key:4},{label:'la cuenta',key:5}]},
   {sub:'ellos · probar',items:[{label:'Ellos',key:1},{label:'van',key:2},{label:'a',key:3},{label:'probar',key:4},{label:'el ceviche',key:5}]},
   {sub:'ella · preparar',items:[{label:'Lucía',key:1},{label:'va',key:2},{label:'a',key:3},{label:'preparar',key:4},{label:'una tortilla',key:5}]},
   {sub:'yo · negativo',items:[{label:'Yo',key:1},{label:'no',key:2},{label:'voy',key:3},{label:'a',key:4},{label:'beber refresco',key:5}]}]});
 buildChoice('gx_iraq',{title:'Mini-quiz: ir a + infinitivo',desc:'Kies de juiste vorm van «ir a». Directe feedback.',per:6,pool:[
   {q:'(Yo) ___ comer un taco.',opts:['voy a','vas a','va a'],ans:'voy a',why:'yo → voy a'},
   {q:'¿(Tú) ___ tomar algo?',opts:['vas a','voy a','va a'],ans:'vas a',why:'tú → vas a'},
   {q:'(Nosotros) ___ pedir la cuenta.',opts:['vamos a','van a','voy a'],ans:'vamos a',why:'nosotros → vamos a'},
   {q:'Diego ___ probar el ceviche.',opts:['va a','van a','vas a'],ans:'va a',why:'él → va a'},
   {q:'(Ellos) ___ cocinar hoy.',opts:['van a','va a','vamos a'],ans:'van a',why:'ellos → van a'},
   {q:'¿(Vosotros) ___ cenar aquí?',opts:['vais a','van a','vamos a'],ans:'vais a',why:'vosotros → vais a'},
   {q:'Mañana (yo) ___ preparar arepas.',opts:['voy a','va a','vas a'],ans:'voy a',why:'yo → voy a'},
   {q:'Lucía ___ comprar fruta.',opts:['va a','van a','vas a'],ans:'va a',why:'ella → va a'},
   {q:'¿Qué ___ tomar tú?',opts:['vas a','va a','voy a'],ans:'vas a',why:'tú → vas a'},
   {q:'Nina y Valen ___ viajar a México.',opts:['van a','vamos a','va a'],ans:'van a',why:'ellas → van a'}]});
 buildMatch('gx_conc',{title:'Concordancia: nombre ↔ mucho…',desc:'Koppel het woord aan de juiste vorm van «mucho» (m/v · ev/mv).',per:6,pool:[
   {a:'pan',b:'mucho pan'},{a:'fruta',b:'mucha fruta'},{a:'tomates',b:'muchos tomates'},{a:'manzanas',b:'muchas manzanas'},
   {a:'arroz',b:'mucho arroz'},{a:'leche',b:'mucha leche'},{a:'huevos',b:'muchos huevos'},{a:'uvas',b:'muchas uvas'},
   {a:'queso',b:'mucho queso'},{a:'gambas',b:'muchas gambas'}]});
 buildChoice('gx_cantq',{title:'Mini-quiz: cantidades',desc:'un kilo de · un poco de · una botella de. Kies wat past.',per:6,pool:[
   {q:'___ agua, por favor.',opts:['una botella de','un kilo de','un poco de'],ans:'una botella de',why:'vloeistof → botella'},
   {q:'___ tomates para la salsa.',opts:['un kilo de','una botella de','un poco de'],ans:'un kilo de',why:'fruta/verdura → kilo'},
   {q:'Solo ___ queso, gracias.',opts:['un poco de','un kilo de','una botella de'],ans:'un poco de',why:'niet-telbaar → un poco de'},
   {q:'___ manzanas, por favor.',opts:['un kilo de','una botella de','un poco de'],ans:'un kilo de',why:'fruta → kilo'},
   {q:'___ refresco bien frío.',opts:['una botella de','un kilo de','un poco de'],ans:'una botella de',why:'vloeistof → botella'},
   {q:'Pon ___ sal en la sopa.',opts:['un poco de','un kilo de','una botella de'],ans:'un poco de',why:'niet-telbaar'},
   {q:'___ zumo de naranja.',opts:['una botella de','un kilo de','un paquete de'],ans:'una botella de',why:'vloeistof → botella'},
   {q:'Quiero ___ uvas.',opts:['un kilo de','una botella de','un poco de'],ans:'un kilo de',why:'fruta → kilo'},
   {q:'Necesito ___ harina.',opts:['un poco de','un kilo de','una botella de'],ans:'un poco de',why:'niet-telbaar'},
   {q:'___ leche para el café.',opts:['un poco de','un kilo de','un paquete de'],ans:'un poco de',why:'niet-telbaar'}]});
 buildChoice('gx_pronq',{title:'Mini-quiz: lo / la / los / las',desc:'Welk pronomen vervangt het voorwerp? (la cuenta → la traigo)',per:6,pool:[
   {q:'¿La cuenta? — Sí, ___ traigo.',opts:['la','lo','las'],ans:'la',why:'la cuenta (f ev)'},
   {q:'¿El pan? — ___ traigo ahora.',opts:['Lo','La','Los'],ans:'Lo',why:'el pan (m ev)'},
   {q:'¿Los tacos? — Sí, ___ quiero.',opts:['los','las','lo'],ans:'los',why:'los tacos (m pl)'},
   {q:'¿Las gambas? — ___ pido.',opts:['Las','Los','La'],ans:'Las',why:'las gambas (f pl)'},
   {q:'¿El postre? — Sí, ___ quiero.',opts:['lo','la','los'],ans:'lo',why:'el postre (m ev)'},
   {q:'¿La carta? — Ahora ___ traigo.',opts:['la','lo','las'],ans:'la',why:'la carta (f ev)'},
   {q:'¿Los refrescos? — ___ traigo.',opts:['Los','Las','Lo'],ans:'Los',why:'los refrescos (m pl)'},
   {q:'¿Las manzanas? — ___ como.',opts:['Las','Los','La'],ans:'Las',why:'las manzanas (f pl)'},
   {q:'¿El guacamole? — ___ preparo yo.',opts:['Lo','La','Los'],ans:'Lo',why:'el guacamole (m ev)'},
   {q:'¿La ensalada? — ___ traigo.',opts:['La','Lo','Las'],ans:'La',why:'la ensalada (f ev)'}]});
 buildChoice('gx_mix',{title:'Repaso mixto: rellena',desc:'Alles door elkaar: ir a · cantidades · pronombres · vocabulario.',per:8,pool:[
   {q:'(Nosotros) ___ comer paella.',opts:['vamos a','van a','voy a'],ans:'vamos a',why:'nosotros → vamos a'},
   {q:'Hay ___ fruta en el mercado.',opts:['mucha','mucho','muchos'],ans:'mucha',why:'la fruta (f)'},
   {q:'¿La cuenta? — ___ traigo.',opts:['La','Lo','Las'],ans:'La',why:'la cuenta (f ev)'},
   {q:'Para mí ___ botella de agua.',opts:['una','un','unos'],ans:'una',why:'la botella (f)'},
   {q:'Diego ___ probar el ceviche.',opts:['va a','van a','vas a'],ans:'va a',why:'él → va a'},
   {q:'¿El pan? — ___ traigo ahora.',opts:['Lo','La','Los'],ans:'Lo',why:'el pan (m ev)'},
   {q:'Compro un ___ de tomates.',opts:['kilo','poco','botella'],ans:'kilo',why:'fruta/verdura → un kilo de'},
   {q:'Hay ___ churros en la mesa.',opts:['muchos','muchas','mucho'],ans:'muchos',why:'los churros (m pl)'},
   {q:'¿(Tú) ___ tomar postre?',opts:['vas a','va a','voy a'],ans:'vas a',why:'tú → vas a'},
   {q:'¿Las bebidas? — ___ pongo en la mesa.',opts:['Las','Los','La'],ans:'Las',why:'las bebidas (f pl)'},
   {q:'Solo ___ poco de queso.',opts:['un','una','unos'],ans:'un',why:'un poco de'},
   {q:'En el mercado hay ___ verduras.',opts:['muchas','muchos','mucha'],ans:'muchas',why:'las verduras (f pl)'}]});
 // VOCABULARIO
 buildMatch('vx_match',{title:'Empareja: palabra ↔ emoji',desc:'Koppel het Spaanse woord aan het juiste beeld.',per:6,pool:[
   {a:'la manzana',b:'🍎'},{a:'el plátano',b:'🍌'},{a:'la naranja',b:'🍊'},{a:'las uvas',b:'🍇'},
   {a:'la piña',b:'🍍'},{a:'el pan',b:'🥖'},{a:'el queso',b:'🧀'},{a:'el pollo',b:'🍗'},
   {a:'el pescado',b:'🐟'},{a:'los tacos',b:'🌮'},{a:'el café',b:'☕'},{a:'la sopa',b:'🍲'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat in de zin past.',per:6,pool:[
   {q:'En el mercado compro ___ para el zumo.',opts:['naranjas','tenedor','cuenta'],ans:'naranjas',why:'zumo de naranja'},
   {q:'Para la ensalada necesito ___.',opts:['lechuga','refresco','postre'],ans:'lechuga',why:'ensalada = lechuga'},
   {q:'De postre quiero un ___.',opts:['flan','vaso','mantel'],ans:'flan',why:'el flan = postre'},
   {q:'El ___ es una bebida caliente.',opts:['café','pan','queso'],ans:'café',why:'café = bebida caliente'},
   {q:'Como un ___ de pollo con salsa.',opts:['taco','vaso','plato'],ans:'taco',why:'el taco'},
   {q:'Bebo una ___ de agua.',opts:['botella','cuchara','servilleta'],ans:'botella',why:'una botella de agua'},
   {q:'El guacamole lleva ___.',opts:['aguacate','arroz','pollo'],ans:'aguacate',why:'guacamole = aguacate'},
   {q:'Tomo la sopa con la ___.',opts:['cuchara','taza','servilleta'],ans:'cuchara',why:'la sopa → la cuchara'},
   {q:'Corto el pan con el ___.',opts:['cuchillo','vaso','plato'],ans:'cuchillo',why:'cortar → el cuchillo'},
   {q:'La paella lleva ___.',opts:['arroz','chocolate','lechuga'],ans:'arroz',why:'paella = arroz'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het juiste woord.',per:6,pool:[
   {q:'Fruta amarilla y curva:',opts:['el plátano','la manzana','el tomate'],ans:'el plátano',why:'plátano = banaan'},
   {q:'Bebida de la mañana, caliente:',opts:['el café','el agua','el zumo'],ans:'el café',why:'café'},
   {q:'Postre típico, dulce y blando:',opts:['el flan','la sopa','la ensalada'],ans:'el flan',why:'flan = postre'},
   {q:'Verdura verde para la ensalada:',opts:['la lechuga','la cebolla','el maíz'],ans:'la lechuga',why:'lechuga = sla'},
   {q:'Plato mexicano con tortilla:',opts:['el taco','la paella','el ceviche'],ans:'el taco',why:'taco 🇲🇽'},
   {q:'Se usa para beber agua:',opts:['el vaso','el plato','el tenedor'],ans:'el vaso',why:'vaso = glas'},
   {q:'Producto del cerdo, salado:',opts:['el jamón','el queso','el huevo'],ans:'el jamón',why:'jamón = ham'},
   {q:'Fruta tropical de México:',opts:['la piña','las uvas','la fresa'],ans:'la piña',why:'piña = ananas'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['la manzana','el plátano','la naranja','el pollo'],odd:3,why:'el pollo = carne, geen fruta'},
   {words:['el agua','el café','el zumo','el pan'],odd:3,why:'el pan = comida, geen bebida'},
   {words:['el tenedor','el cuchillo','la cuchara','la manzana'],odd:3,why:'la manzana = fruta, geen cubierto'},
   {words:['los tacos','el guacamole','la paella','las quesadillas'],odd:2,why:'la paella = España; de rest México'},
   {words:['la lechuga','el tomate','la cebolla','la fresa'],odd:3,why:'la fresa = fruta; de rest verdura'},
   {words:['el flan','los churros','el pescado','la piña'],odd:2,why:'el pescado is geen postre'},
   {words:['mucho','mucha','muchos','poco'],odd:3,why:'«poco» is geen vorm van «mucho»'},
   {words:['la sopa','el pollo','el arroz','el refresco'],odd:3,why:'el refresco = bebida; de rest comida'}]});
 // LECTURA
 buildOrder('lx_order',{title:'Ordena la comida',desc:'Tik de items in de juiste volgorde.',rounds:[
   {sub:'las partes del menú',items:[{label:'De primero (entrante)',key:1},{label:'De segundo (plato fuerte)',key:2},{label:'De postre',key:3},{label:'La cuenta',key:4}]},
   {sub:'de barato a caro · carta de Lucía',items:[{label:'Fruta del día — 3 €',key:1},{label:'Sopa de tomate — 4 €',key:2},{label:'Pollo con patatas — 9 €',key:3},{label:'Pescado a la plancha — 11 €',key:4}]},
   {sub:'los momentos del día',items:[{label:'el desayuno',key:1},{label:'la comida',key:2},{label:'la merienda',key:3},{label:'la cena',key:4}]},
   {sub:'de barato a caro · carta de Diego',items:[{label:'Flan casero — 3 €',key:1},{label:'Elote con queso — 4 €',key:2},{label:'Tacos de pollo — 8 €',key:3},{label:'Ceviche de pescado — 10 €',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in de twee cartas en kies het juiste antwoord.',per:6,pool:[
   {q:'¿Cuánto cuesta el pollo con patatas?',opts:['9 €','11 €','4 €'],ans:'9 €',why:'«Pollo con patatas 9 €»'},
   {q:'¿Qué postre hay en casa de Lucía?',opts:['Churros con chocolate','Flan casero','Elote con queso'],ans:'Churros con chocolate',why:'carta de Lucía'},
   {q:'¿De qué son los tacos de Diego?',opts:['de pollo','de pescado','de carne'],ans:'de pollo',why:'«Tacos de pollo»'},
   {q:'¿Cuál es el plato más caro de Lucía?',opts:['Pescado a la plancha','Sopa de tomate','Ensalada mixta'],ans:'Pescado a la plancha',why:'11 € = el más caro'},
   {q:'¿Qué cuesta 5 € en casa de Lucía?',opts:['Ensalada mixta','Fruta del día','Sopa de tomate'],ans:'Ensalada mixta',why:'«Ensalada mixta 5 €»'},
   {q:'¿Cuánto cuesta el ceviche de Diego?',opts:['10 €','8 €','3 €'],ans:'10 €',why:'«Ceviche de pescado 10 €»'},
   {q:'¿Qué fruta hay de postre en casa de Diego?',opts:['Piña con lima','Manzana','Uvas'],ans:'Piña con lima',why:'carta de Diego'},
   {q:'¿Cuánto cuesta el guacamole con nachos?',opts:['5 €','4 €','8 €'],ans:'5 €',why:'«Guacamole con nachos 5 €»'}]});
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='U5_web_mijn_versie.html';a.click();};
})();
"""

# Getypte woordenschat-drills (fase ophalen + produceren) in het paneel zelf.
JS += hub_type_sets.vocab_type_js(vocab)
JS += hub_type_gram.js('C5', 5)
JS += (hub_bloques.escucha_js("esc_u5", escucha_data.C5_U5)
       + hub_bloques.lectura_js("lec_u5", lectura_data.C5_U5))
HTML = HTML.replace("__GRAMSLOTS__", hub_type_gram.slots('C5', 5))
HTML = HTML.replace("__NGAMES__", str(len(GAMES)))
HTML = HTML.replace("__BRONNEN__", extra_bronnen.html('C5', 5))
HTML = HTML.replace("__TYPESLOTS__", hub_type_sets.SLOTS_HTML)

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/U5_web.html","w").write(html)
print("U5_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
