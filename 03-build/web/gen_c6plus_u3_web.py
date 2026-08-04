#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C6+ · U3 «Conectados».
# Eén standalone bestand: fonts base64, de U3-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U3-vocab), visuele/interactieve grammatica (ir a + inf · le/les · creo que),
# klikbare kaart (mundo hispano, parada 3 = México) + TTS + inline recorder + Lectura + editbar. Huisstijl morado.
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
vocab = json.load(open(f"{ROOT}/01-cursussen/06-vervolg/U3/u3_vocab.json", encoding="utf-8"))
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

# ---- de U3-motor-spellen: gegroepeerd (receptief -> productief -> hablar) + base64 ingebed ----
MOTOR = [
 ['① Reconocer · woordenschat', [
   ['digital-memoria', 'memoria digital', 'memory'],
   ['acciones-memoria', 'memoria de acciones', 'memory'],
   ['verbo-objeto', 'verbo ↔ objeto', 'match']]],
 ['② Distinguir · gramática', [
   ['presente-futuro', '¿ahora o después?', 'classify'],
   ['le-les', '¿le o les?', 'classify']]],
 ['③ Producir con apoyo', [
   ['ir-a', 'completa: ir a + infinitivo', 'cloze'],
   ['le-les-cloze', 'completa: le/les', 'cloze'],
   ['creo-que', 'completa: creo que + indicativo', 'cloze'],
   ['ir-a-tetris', 'ir a + inf.: burbujas', 'bubble'],
   ['plan-order', 'ordena la frase', 'order'],
   ['senala', 'señala', 'point']]],
 ['④ Hablar · grábate 🎙️', [
   ['repite-planes', 'escucha y repite: mis planes', 'speak'],
   ['mensaje-planes', 'mensaje de voz: mi finde', 'speak']]],
]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-c6plus-u3-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-c6plus-u3-{s}.html")}

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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="dispositivos">aparatos</option><option value="internet">internet/redes</option><option value="digital">acciones digitales</option><option value="comunicar">comunicar (le/les)</option><option value="planes">planes (ir a)</option><option value="opinar">opinión (creo que)</option><option value="adjmedia">adjetivos</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Más español en la práctica · C6+ U3 Conectados</title>
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
    <div><h1>U3 · Conectados</h1>
    <p>La página digital de la Unidad 3 (<b>conectados</b>): flashcards, gramática visual e interactiva y <b>__NGAMES__ juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie. Thema's: media/redes · ir a + infinitivo · le/les · creo que.</span></p></div>
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
__TYPESLOTS__
    <h2 class="sec">Naslagwerk · zoeken</h2>
    __NAS__
  </section>

  <section class="panel" data-p="gram">
    <h2 class="sec">Gramática visual e interactiva</h2>
    <p class="lead">De <b>essentiële</b> grammatica van U3: <b>ir a + infinitivo</b> (futuro próximo) + <b>acabar de</b>, de pronombres <b>le/les</b> en je mening met <b>creo que + indicativo</b>. Hier oefen je <b>maximaal</b> — elke oefening trekt uit een grote pool, dus «↻ otra serie» geeft telkens een nieuwe reeks. <span class="gloss">Eerst betekenis/patroon ontdekken, dan de regel.</span></p>
    <div class="card" id="colorsent"></div>
    <div class="card" id="irconj"></div>
    <h2 class="sec" style="margin-top:26px">🔮 Ir a + infinitivo — máxima práctica</h2>
    <p class="lead">ir (voy/vas/va/vamos/vais/van) + <b>a</b> + infinitivo. Vergeet de <b>a</b> niet! + <b>acabar de</b> (net gedaan). <span class="gloss">Blijf herspelen tot het automatisch komt.</span></p>
    <div class="game" id="g_cantidad"></div>
    <div class="card ex" id="gx_cantq"></div>
    <div class="card ex" id="gx_reg"></div>
    <div class="card ex" id="gx_adj"></div>
    <h2 class="sec" style="margin-top:26px">👉 Los pronombres le/les — ¿a quién?</h2>
    <p class="lead">le = aan één persoon · les = aan meerdere. Staat vóór het werkwoord (of achter de infinitivo). <span class="gloss">Le escribo a Diego.</span></p>
    <div class="game" id="g_pron"></div>
    <div class="card ex" id="gx_pronq"></div>
    <div class="card ex" id="gx_ser"></div>
    <div class="card ex" id="gx_build"></div>
    <h2 class="sec" style="margin-top:26px">💬 Creo que + indicativo · acabar de — máxima práctica</h2>
    <p class="lead">Je mening met de gewone tijd (nooit subjuntivo): creo que <b>es</b> útil. + acabar de + infinitivo (net gedaan). <span class="gloss">Creo que las redes son útiles porque…</span></p>
    <div class="card ex" id="gx_iraq"></div>
    <div class="card ex" id="gx_subj"></div>
    <div class="card ex" id="gx_plural"></div>
    <div class="card ex" id="gx_nac"></div>
    <div class="card ex" id="gx_conc"></div>
    <div class="card ex" id="gx_conc2"></div>
    <h3 class="subh">🎯 Repaso mixto — ir a + le/les + acabar de + creo que</h3>
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
    <h2 class="sec">Lectura completa · ¿Cuántas horas de pantalla?</h2>
    <p class="lead">Een echt artikel met enquête en meningen, met de volledige leesroute: <b>voorspellen → globaal → scannen → juist/fout met bewijs → betekenis uit de context → zelf schrijven</b>. <span class="gloss">Dezelfde tekst staat in je cursus, met schrijfruimte.</span></p>
    <div class="card ex" id="lec_c6p_u3"></div>
  </section>

  <section class="panel" data-p="escuchar">
    <h2 class="sec">Escuchar · Cómo hacer una videollamada 🎧</h2>
    <p class="lead">Diego leert zijn oma stap voor stap videobellen. Eén fragment, zes stappen: eerst <b>weten waar je bent</b>, dan <b>globaal</b> luisteren, dan de <b>details</b>, dan <b>juist/fout met bewijs</b>. Het <b>transcript</b> gaat pas open als je klaar bent — anders lees je mee in plaats van te luisteren. <span class="gloss">Zolang er nog geen opname is, leest de computerstem het fragment voor.</span></p>
    <div class="card ex" id="esc_c6p_u3"></div>
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
    <h2 class="sec">Cultura · el mundo digital hispano</h2>
    <p class="lead">Parada 3 = <b>Ciudad de México</b> 🇲🇽, bij <b>Diego</b>. De Spaanstalige wereld leeft volop <b>online</b>: reggaeton op streaming, WhatsApp overal en het Spaans als grote internettaal. <span class="gloss">Elk land heeft zijn digitale cultuur.</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🎵 El reguetón manda</h3>
      <p>Artiesten als <b>Bad Bunny</b> (Puerto Rico) en <b>Karol G</b> (Colombia) breken streamingrecords op Spotify en YouTube. Het Spaans klinkt wereldwijd — vaak zonder vertaling. <span class="gloss">Diego luistert het elke dag.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">💬 WhatsApp, la red nº 1</h3>
      <p>In veel Latijns-Amerikaanse landen is <b>WhatsApp</b> dé manier om te communiceren — met familie, vrienden én winkels. <span class="gloss">«Te mando un audio» hoor je overal.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🌐 El español en internet</h3>
      <p>Het Spaans is de <b>tweede taal</b> op sociale media na het Engels. Meer dan 500 miljoen sprekers zetten de digitale wereld deels in het Spaans. <span class="gloss">Jouw feed spreekt misschien al Spaans.</span></p></div>
    <h3 class="subh">📍 La Ruta · el mapa (parada 3 = CDMX, México ★)</h3>
    <p class="lead">Onze halte is <b>México</b> (CDMX). <b>Klik op een land</b> op de kaart voor info — klik op México (★) voor de parada (thema música).</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    __BRONNEN__
  </section>

  <div class="foot">Más español en la práctica · edición única · Unidad 3 «Conectados» — página digital. Uitbreiding op de PDF · huisstijl morado · print ↔ PowerPoint ↔ web.</div>
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

// ---- GRAMMAR-VIZ 1: kleurgecodeerde ir a + infinitivo-zin ----
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">El futuro próximo — ir + a + infinitivo</h3>'+
'<div class="csent">'+
'<span style="background:#dbeafe;color:#1e40af">Este finde<span class="tip">wanneer? — expresión de tiempo</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">voy a<span class="tip">ir (voy) + a</span></span> '+
'<span style="background:#e9d5ff;color:#6b21a8">subir<span class="tip">infinitivo — het hele werkwoord</span></span> '+
'<span style="background:#dcfce7;color:#166534">un vídeo<span class="tip">voorwerp</span></span>.</div>'+
'<div class="legend"><span><i style="background:#93c5fd"></i>tijd</span><span><i style="background:#fdba74"></i>ir + a</span><span><i style="background:#d8b4fe"></i>infinitivo</span><span><i style="background:#86efac"></i>voorwerp</span></div>'+
'<p class="gloss" style="margin-top:8px">🟠 <b>ir</b> verandert met de persoon (voy/vas/va…) · daarna altijd <b>a</b> + infinitivo. Vergeet de <b>a</b> niet! · '+(TTS?'<button class="spk-btn" onclick="speak(\'Este fin de semana voy a subir un vídeo\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: ir a + infinitivo — klik om te onthullen ----
(function(){const el=document.getElementById('irconj');
 const R=[['yo','voy a salir'],['tú','vas a salir'],['él/ella','va a salir'],['nosotros','vamos a salir'],['vosotros','vais a salir'],['ellos','van a salir']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">ir a + infinitivo (salir) — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">Enkel ir verandert (voy/vas/va…); daarna altijd «a + salir».</p><div class="conjgrid" id="icg"></div>';
 const g=el.querySelector('#icg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v;if(TTS)speak(p+' '+v);};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: ir a — ¿qué forma de ir? ----
function gameCantidad(){const el=document.getElementById('g_cantidad');
 const items=[['Yo ___ subir un vídeo.','voy a','yo → voy a'],['¿Tú ___ salir el sábado?','vas a','tú → vas a'],['Diego ___ chatear.','va a','él → va a'],['Nosotros ___ quedar.','vamos a','nosotros → vamos a'],['Mis amigos ___ ver una peli.','van a','ellos → van a'],['¿Vosotros ___ estudiar?','vais a','vosotros → vais a'],['Yo ___ llamar a mi abuela.','voy a','yo → voy a'],['Valen ___ compartir las fotos.','va a','ella → va a'],['Ellos ___ publicar un vídeo.','van a','ellos → van a'],['Diego y yo ___ comer tacos.','vamos a','nosotros → vamos a'],['¿Tú me ___ llamar luego?','vas a','tú → vas a'],['Mi madre ___ comprar un móvil.','va a','ella → va a']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>ir a + infinitivo — ¿qué forma de ir?</h3><p class="desc">voy/vas/va/vamos/vais/van + a + infinitivo.</p>'+scoreBar('sbC')+'<div id="cW" style="font-size:18px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" id="cC" style="justify-content:center"></div><div class="fb" id="cFb"></div>';
 const sb=el.querySelector('#sbC');const cont=el.querySelector('#cC');
 ['voy a','vas a','va a','vamos a','vais a','van a'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#cW').textContent=el.cur[0];el.querySelector('#cFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#cFb'),ok,(ok?'¡Sí! ':'Nee: '+el.cur[1]+' ')+'('+el.cur[2]+').');setTimeout(next,1000);}
 next();}
// ---- GRAMMAR-VIZ 4: le/les (¿a quién?) ----
function gamePron(){const el=document.getElementById('g_pron');
 const items=[['___ escribo a mi amiga.','le','a mi amiga (1) → le'],['___ mando fotos a mis padres.','les','a mis padres → les'],['___ cuento un secreto a Diego.','le','a Diego (1) → le'],['___ regalo algo a mis hermanos.','les','a mis hermanos → les'],['___ pregunto la hora a Valen.','le','a Valen (1) → le'],['___ muestro el perfil a mis amigos.','les','a mis amigos → les'],['___ digo la verdad a mi madre.','le','a mi madre (1) → le'],['___ envío un audio a los profes.','les','a los profes → les'],['___ llamo a mi abuela.','le','a mi abuela (1) → le'],['___ cuento las noticias a mis primos.','les','a mis primos → les'],['___ escribo a mi profesor.','le','a mi profesor (1) → le'],['___ enseño las fotos a mis abuelos.','les','a mis abuelos → les']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>Los pronombres le/les — ¿a quién?</h3><p class="desc">a + één persoon → le · a + meer personen → les.</p>'+scoreBar('sbP')+'<div id="pQ" style="font-size:19px;font-family:var(--disp);text-align:center;margin:10px 0"></div><div class="chips" id="pC" style="justify-content:center"></div><div class="fb" id="pFb"></div>';
 const sb=el.querySelector('#sbP');const cont=el.querySelector('#pC');
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#pQ').textContent=el.cur[0];cont.innerHTML='';['le','les'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});el.querySelector('#pFb').className='fb';}
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
    const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "🎵 Música: el mariachi y el corrido", "star": 1, "nl": "★ ¡Estás aquí! Parada U3 · CDMX (Diego)"}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "🎵 Música: el flamenco y el pop de Rosalía", "star": 1, "nl": "Parada anterior (U0–U1) · el mundo hispano · España (Lucía)"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "🎵 Música: la cumbia, el vallenato y el reguetón", "star": 1, "nl": "Parada anterior (U2) · Cartagena (Valen)"}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "🎵 Música: el huayno andino y la música criolla", "star": 0, "nl": ""}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "🎵 Música: el tango y el rock nacional", "star": 0, "nl": ""}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "🎵 Música: el joropo y la gaita", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "🎵 Música: la cueca, baile nacional", "star": 0, "nl": ""}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "🎵 Música: el pasillo, canción típica", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "🎵 Música: la marimba, instrumento nacional", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "🎵 Música: el son, la salsa y la rumba", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "🎵 Música: música andina con charango y zampoña", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "🎵 Música: el merengue y la bachata", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "🎵 Música: la punta garífuna", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "🎵 Música: el arpa paraguaya y la guarania", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "🎵 Música: el son nica y la marimba", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "🎵 Música: la cumbia y las «xuc»", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "🎵 Música: el calypso y la música guanacasteca", "star": 0, "nl": ""}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "🎵 Música: la salsa de Rubén Blades y el tamborito", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "🎵 Música: el candombe con tambores", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "🎵 Música: el reguetón y la salsa", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "🎵 Música: ritmos africanos y el «malamba»", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "🎵 Música: el latin pop y el hip-hop en español", "star": 0, "nl": ""}};
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
 const P=[{n:'Diego 🇲🇽',raw:'Yo paso muchas horas con el móvil: subo vídeos, chateo y sigo a muchos artistas. Creo que el móvil es muy útil para estudiar y para hablar con mis amigos lejos. Pero también pienso que a veces es adictivo: acabo de mirar la pantalla y, cinco minutos después, la miro otra vez. Este finde voy a hacer una cosa: apagar el móvil dos horas al día.',
    html:'Yo <span class="ev">paso muchas horas</span> con el móvil: subo vídeos, chateo y sigo a muchos artistas. Creo que el móvil <span class="ev">es muy útil</span> para estudiar. Pero también pienso que a veces es <span class="ev">adictivo</span>: <span class="ev">acabo de</span> mirar la pantalla y, cinco minutos después, la miro otra vez. Este finde <span class="ev">voy a apagar</span> el móvil dos horas al día.'},
   {n:'Lucía 🇪🇸',raw:'A mí me gustan las redes, pero no paso tanto tiempo. Creo que las redes conectan a la gente, pero también pueden ser peligrosas si compartes demasiado. En mi opinión, lo importante es el equilibrio: uso el móvil para lo práctico y luego lo apago. Por un lado es genial, por otro hay que tener cuidado.',
    html:'A mí me gustan las redes, pero no paso tanto tiempo. Creo que las redes <span class="ev">conectan</span> a la gente, pero también <span class="ev">pueden ser peligrosas</span> si compartes demasiado. En mi opinión, lo importante es el <span class="ev">equilibrio</span>: uso el móvil para lo práctico y luego lo apago. Por un lado es genial, <span class="ev">por otro</span> hay que tener cuidado.'}];
 el.innerHTML='<div class="perfiles">'+P.map((m,i)=>'<div class="perfil"><h4>👤 '+m.n+' '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lm'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div class="txt" id="lm'+i+'" data-raw="'+m.raw.replace(/"/g,'&quot;')+'">'+m.html+'</div></div>').join('')+'</div>';
 const items=[['Diego cree que el móvil es útil para estudiar.',true,'«el móvil es muy útil para estudiar»'],['Diego va a usar el móvil aún más este finde.',false,'«voy a apagar el móvil dos horas al día»'],['Diego dice que a veces el móvil es adictivo.',true,'«a veces es adictivo»'],['Lucía pasa muchísimo tiempo en las redes.',false,'«no paso tanto tiempo»'],['Lucía piensa que las redes pueden ser peligrosas.',true,'«pueden ser peligrosas»'],['Para Lucía, lo importante es el equilibrio.',true,'«lo importante es el equilibrio»'],['Diego acaba de mirar la pantalla otra vez.',true,'«acabo de mirar la pantalla»'],['Lucía nunca apaga el móvil.',false,'«luego lo apago»']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — con evidencia</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">¿Y tú? Reacciona</h3><p class="gloss" style="margin:0 0 8px">¿Estás más de acuerdo con Diego o con Lucía? Escribe 2–3 frases con <b>creo que + porque</b> y un plan con <b>voy a</b>. Grábalo en <b>Hablar 🎙️</b>.</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="Estoy más de acuerdo con… porque… Este finde voy a…"></textarea>';
 el.appendChild(box);el.appendChild(resp);}

// ---------- INLINE RECORDER (MediaRecorder) ----------
""" + hub_drills.RECORDER_JS + r"""
function buildRecorders(){
 makeRecorder('rec_repite',{title:'Escucha y repite: mis planes',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'Este fin de semana voy a salir con mis amigos.',cue:'ir a + inf',tip:'Duidelijk? Probeer nog eens zonder te lezen.'},{text:'Mañana voy a subir un vídeo nuevo.',cue:'ir a + inf'},{text:'Le escribo a Diego cada día.',cue:'le/les'},{text:'Les mando fotos a mis amigos.',cue:'le/les'},{text:'Acabo de mandar un mensaje.',cue:'acabar de'},{text:'Creo que las redes son útiles pero adictivas.',cue:'opinión'}]});
 makeRecorder('rec_pedido',{title:'Mensaje de voz: mi finde',desc:'Neem één bericht op (30–40 s): vertel je weekendplan (gebruik 3× ir a + infinitivo).',items:[
   {text:'Cuenta tu plan de fin de semana (usa 3 veces ir a + infinitivo + una expresión de tiempo).',cue:'mi plan',tip:'3× ir a + infinitivo (met de a)? Neem opnieuw op.'}]});
 makeRecorder('rec_plato',{title:'Mensaje de voz: mi opinión',desc:'Geef je mening over sociale media.',items:[
   {text:'Da tu opinión sobre las redes sociales: creo que … porque … · por un lado … por otro …',cue:'mi opinión',tip:'creo que + indicativo + porque? Herneem.'}]});
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
 // ===== IR A + INFINITIVO (+ acabar de, expresiones de tiempo) =====
 buildChoice('gx_cantq',{title:'ir a + infinitivo — ¿qué forma de ir?',desc:'voy/vas/va/vamos/vais/van + a + infinitivo.',per:8,pool:[
   {q:'Yo ___ un vídeo esta tarde.',opts:['voy a subir','vas a subir','va a subir'],ans:'voy a subir',why:'yo → voy a'},
   {q:'¿Tú ___ el sábado?',opts:['vas a salir','voy a salir','van a salir'],ans:'vas a salir',why:'tú → vas a'},
   {q:'Diego ___ con nosotros luego.',opts:['va a chatear','vas a chatear','voy a chatear'],ans:'va a chatear',why:'él → va a'},
   {q:'Nosotros ___ en la plaza.',opts:['vamos a quedar','van a quedar','vais a quedar'],ans:'vamos a quedar',why:'nosotros → vamos a'},
   {q:'Mis amigos ___ una serie.',opts:['van a ver','va a ver','vamos a ver'],ans:'van a ver',why:'ellos → van a'},
   {q:'¿Vosotros ___ mañana?',opts:['vais a estudiar','van a estudiar','vamos a estudiar'],ans:'vais a estudiar',why:'vosotros → vais a'},
   {q:'Yo ___ a mi abuela.',opts:['voy a llamar','va a llamar','vas a llamar'],ans:'voy a llamar',why:'yo → voy a'},
   {q:'Valen ___ las fotos.',opts:['va a compartir','van a compartir','vas a compartir'],ans:'va a compartir',why:'ella → va a'},
   {q:'¿Qué ___ (tú) este finde?',opts:['vas a hacer','va a hacer','voy a hacer'],ans:'vas a hacer',why:'tú → vas a'},
   {q:'Mi madre ___ un móvil nuevo.',opts:['va a comprar','van a comprar','vas a comprar'],ans:'va a comprar',why:'ella → va a'},
   {q:'Los niños ___ al parque.',opts:['van a ir','va a ir','vamos a ir'],ans:'van a ir',why:'ellos → van a'},
   {q:'Diego y yo ___ tacos.',opts:['vamos a comer','van a comer','voy a comer'],ans:'vamos a comer',why:'nosotros → vamos a'}]});
 buildChoice('gx_reg',{title:'¿ahora, después o recién?',desc:'presente (nu) · ir a (straks) · acabar de (net gedaan).',per:8,pool:[
   {q:'Mañana ___ (yo, salir).',opts:['voy a salir','salgo','acabo de salir'],ans:'voy a salir',why:'mañana → ir a'},
   {q:'¡Mira! Diego ___ (subir) una foto ahora mismo.',opts:['acaba de subir','va a subir','sube'],ans:'acaba de subir',why:'ahora mismo/ya → acabar de'},
   {q:'Cada día (yo) ___ (chatear) con mis amigos.',opts:['chateo','voy a chatear','acabo de chatear'],ans:'chateo',why:'cada día → presente'},
   {q:'No tengo hambre, ___ (yo, comer).',opts:['acabo de comer','voy a comer','como'],ans:'acabo de comer',why:'net gegeten → acabar de'},
   {q:'Este finde ___ (nosotros, quedar).',opts:['vamos a quedar','quedamos','acabamos de quedar'],ans:'vamos a quedar',why:'este finde → ir a'},
   {q:'Normalmente (yo) ___ (navegar) por la noche.',opts:['navego','voy a navegar','acabo de navegar'],ans:'navego',why:'normalmente → presente'},
   {q:'Espera, ___ (yo, mandar) el mensaje (net).',opts:['acabo de mandar','voy a mandar','mando'],ans:'acabo de mandar',why:'net → acabar de'},
   {q:'Luego (yo) ___ (llamar) a Diego.',opts:['voy a llamar','llamo','acabo de llamar'],ans:'voy a llamar',why:'luego → ir a'},
   {q:'Los domingos (yo) ___ (ver) series.',opts:['veo','voy a ver','acabo de ver'],ans:'veo',why:'los domingos → presente'},
   {q:'El próximo año ___ (nosotros, viajar).',opts:['vamos a viajar','viajamos','acabamos de viajar'],ans:'vamos a viajar',why:'el próximo año → ir a'},
   {q:'Diego ___ (conectarse) hace un segundo.',opts:['acaba de conectarse','va a conectarse','se conecta'],ans:'acaba de conectarse',why:'hace un segundo → acabar de'},
   {q:'Pronto (yo) ___ (comprar) una tableta.',opts:['voy a comprar','compro','acabo de comprar'],ans:'voy a comprar',why:'pronto → ir a'}]});
 buildChoice('gx_adj',{title:'¿Cuándo? — expresiones de tiempo',desc:'Kies de tijdsuitdrukking die past bij het plan.',per:7,pool:[
   {q:'___ voy a salir (dit weekend).',opts:['Este fin de semana','Ayer','Cada día'],ans:'Este fin de semana',why:'dit weekend'},
   {q:'___ te llamo (straks).',opts:['Luego','Ahora','Siempre'],ans:'Luego',why:'straks = luego'},
   {q:'___ voy a jugar al fútbol (morgen).',opts:['Mañana','Nunca','Hoy'],ans:'Mañana',why:'morgen = mañana'},
   {q:'___ voy a comprar un móvil (binnenkort).',opts:['Pronto','Ayer','Normalmente'],ans:'Pronto',why:'binnenkort = pronto'},
   {q:'___ voy a viajar (volgende jaar).',opts:['El próximo año','Anoche','Cada semana'],ans:'El próximo año',why:'volgend jaar'},
   {q:'Te escribo ___ (later).',opts:['más tarde','ayer','siempre'],ans:'más tarde',why:'later = más tarde'},
   {q:'«dit weekend» =',opts:['este fin de semana','el fin de semana pasado','todos los días'],ans:'este fin de semana',why:'este finde'},
   {q:'Primero estudio y ___ salgo (daarna).',opts:['después','antes','nunca'],ans:'después',why:'daarna = después'}]});
 // ===== LE/LES (OI) =====
 buildChoice('gx_pronq',{title:'¿le o les?',desc:'a + één persoon → le · a + meer personen → les.',per:8,pool:[
   {q:'___ escribo a mi amiga.',opts:['Le','Les','La'],ans:'Le',why:'a mi amiga (1) → le'},
   {q:'___ mando fotos a mis padres.',opts:['Les','Le','Los'],ans:'Les',why:'a mis padres → les'},
   {q:'___ cuento un secreto a Diego.',opts:['Le','Les','Lo'],ans:'Le',why:'a Diego (1) → le'},
   {q:'___ regalo auriculares a mis hermanos.',opts:['Les','Le','Las'],ans:'Les',why:'a mis hermanos → les'},
   {q:'___ pregunto la hora a Valen.',opts:['Le','Les','La'],ans:'Le',why:'a Valen (1) → le'},
   {q:'___ muestro el perfil a mis amigos.',opts:['Les','Le','Lo'],ans:'Les',why:'a mis amigos → les'},
   {q:'___ digo la verdad a mi madre.',opts:['Le','Les','La'],ans:'Le',why:'a mi madre (1) → le'},
   {q:'___ envío un audio a los profes.',opts:['Les','Le','Los'],ans:'Les',why:'a los profes → les'},
   {q:'___ llamo a mi abuela los domingos.',opts:['Le','Les','La'],ans:'Le',why:'a mi abuela (1) → le'},
   {q:'___ cuento las noticias a mis primos.',opts:['Les','Le','Las'],ans:'Les',why:'a mis primos → les'},
   {q:'___ escribo a mi profesor.',opts:['Le','Les','Lo'],ans:'Le',why:'a mi profesor (1) → le'},
   {q:'___ enseño las fotos a mis abuelos.',opts:['Les','Le','Las'],ans:'Les',why:'a mis abuelos → les'}]});
 buildChoice('gx_ser',{title:'Responde con le/les',desc:'Antwoord kort met le of les + het werkwoord.',per:7,pool:[
   {q:'¿Escribes a Diego? — Sí, ___ escribo.',opts:['le','les','la'],ans:'le',why:'a Diego (1) → le'},
   {q:'¿Mandas fotos a tus amigos? — Sí, ___ mando fotos.',opts:['les','le','los'],ans:'les',why:'a tus amigos → les'},
   {q:'¿Cuentas el secreto a Valen? — Sí, ___ cuento.',opts:['le','les','lo'],ans:'le',why:'a Valen (1) → le'},
   {q:'¿Preguntas la hora a tus padres? — Sí, ___ pregunto.',opts:['les','le','las'],ans:'les',why:'a tus padres → les'},
   {q:'¿Regalas algo a tu hermana? — Sí, ___ regalo algo.',opts:['le','les','la'],ans:'le',why:'a tu hermana (1) → le'},
   {q:'¿Muestras el perfil a los profes? — Sí, ___ muestro.',opts:['les','le','lo'],ans:'les',why:'a los profes → les'},
   {q:'¿Llamas a tu abuela? — Sí, ___ llamo.',opts:['le','les','la'],ans:'le',why:'a tu abuela (1) → le'},
   {q:'¿Respondes a tus compañeros? — Sí, ___ respondo.',opts:['les','le','los'],ans:'les',why:'a compañeros → les'}]});
 buildOrder('gx_build',{title:'Ordena la frase',desc:'Tik de woorden in de juiste volgorde.',rounds:[
   {sub:'ir a + infinitivo',items:[{label:'Este finde',key:1},{label:'voy a',key:2},{label:'quedar',key:3},{label:'con mis amigos.',key:4}]},
   {sub:'le + verbo',items:[{label:'Le',key:1},{label:'escribo',key:2},{label:'un mensaje',key:3},{label:'a Diego.',key:4}]},
   {sub:'les + verbo',items:[{label:'Les',key:1},{label:'mando',key:2},{label:'fotos',key:3},{label:'a mis amigos.',key:4}]},
   {sub:'acabar de + infinitivo',items:[{label:'Acabo',key:1},{label:'de',key:2},{label:'subir',key:3},{label:'una foto.',key:4}]},
   {sub:'creo que + porque',items:[{label:'Creo que',key:1},{label:'las redes',key:2},{label:'son útiles',key:3},{label:'porque conectan.',key:4}]}]});
 // ===== CREO QUE + INDICATIVO · ACABAR DE · POSICIÓN =====
 buildChoice('gx_iraq',{title:'Creo que + indicativo',desc:'Kies de gewone tijd (geen subjuntivo!) na «creo que…».',per:8,pool:[
   {q:'Creo que las redes ___ útiles.',opts:['son','sean','es'],ans:'son',why:'las redes → son (indicativo)'},
   {q:'Pienso que Diego ___ razón.',opts:['tiene','tenga','tienen'],ans:'tiene',why:'Diego → tiene'},
   {q:'Me parece que (nosotros) ___ mucho tiempo online.',opts:['pasamos','pasemos','pasan'],ans:'pasamos',why:'nosotros → pasamos'},
   {q:'Creo que el móvil ___ a estudiar.',opts:['ayuda','ayude','ayudan'],ans:'ayuda',why:'el móvil → ayuda'},
   {q:'Pienso que los videojuegos ___ ser adictivos.',opts:['pueden','puedan','puede'],ans:'pueden',why:'los videojuegos → pueden'},
   {q:'Creo que la wifi ___ rápida.',opts:['es','sea','son'],ans:'es',why:'la wifi → es'},
   {q:'Me parece que (tú) ___ demasiado en el móvil.',opts:['estás','estés','está'],ans:'estás',why:'tú → estás'},
   {q:'Pienso que las apps ___ prácticas.',opts:['son','sean','es'],ans:'son',why:'las apps → son'},
   {q:'Creo que internet ___ peligroso a veces.',opts:['es','sea','son'],ans:'es',why:'internet → es'},
   {q:'Creo que Valen ___ muchos seguidores.',opts:['tiene','tenga','tienen'],ans:'tiene',why:'Valen → tiene'},
   {q:'Me parece que la gente ___ mucho en las redes.',opts:['comparte','comparta','comparten'],ans:'comparte',why:'la gente → comparte'},
   {q:'Creo que las videollamadas ___ geniales.',opts:['son','sean','es'],ans:'son',why:'las videollamadas → son'}]});
 buildChoice('gx_subj',{title:'Acabar de + infinitivo',desc:'«net gedaan»: acabo/acabas/acaba… + de + infinitivo.',per:7,pool:[
   {q:'(Yo) ___ un mensaje (net).',opts:['acabo de mandar','acabo mandar','acabo de mando'],ans:'acabo de mandar',why:'yo → acabo de + inf'},
   {q:'Diego ___ una foto.',opts:['acaba de subir','acaba subir','acaba de sube'],ans:'acaba de subir',why:'él → acaba de + inf'},
   {q:'(Nosotros) ___ .',opts:['acabamos de comer','acabamos comer','acabamos de comemos'],ans:'acabamos de comer',why:'nosotros → acabamos de + inf'},
   {q:'Mis amigos ___ .',opts:['acaban de conectarse','acaban conectarse','acaban de se conectan'],ans:'acaban de conectarse',why:'ellos → acaban de + inf'},
   {q:'¿(Tú) ___ el vídeo?',opts:['acabas de ver','acabas ver','acabas de ves'],ans:'acabas de ver',why:'tú → acabas de + inf'},
   {q:'Mamá ___ .',opts:['acaba de llamar','acaba llamar','acaba de llama'],ans:'acaba de llamar',why:'ella → acaba de + inf'},
   {q:'(Yo) ___ la contraseña.',opts:['acabo de cambiar','acabo cambiar','voy de cambiar'],ans:'acabo de cambiar',why:'yo → acabo de + inf'},
   {q:'Valen y yo ___ un audio.',opts:['acabamos de escuchar','acabamos escuchar','acaban de escuchar'],ans:'acabamos de escuchar',why:'nosotros → acabamos de'}]});
 buildChoice('gx_plural',{title:'La posición de le/les',desc:'vóór het werkwoord, óf vast achter de infinitivo.',per:6,pool:[
   {q:'Escribo un mensaje a Diego. →',opts:['Le escribo un mensaje.','Escribo le un mensaje.','Lo escribo un mensaje.'],ans:'Le escribo un mensaje.',why:'le vóór het ww.'},
   {q:'Voy a mandar fotos a mis amigos. →',opts:['Voy a mandarles fotos.','Voy a les mandar fotos.','Les voy mandar fotos.'],ans:'Voy a mandarles fotos.',why:'achter de infinitief (of: Les voy a mandar)'},
   {q:'Voy a contar la noticia a Valen. →',opts:['Voy a contarle la noticia.','Voy a le contar la noticia.','Le voy contar la noticia.'],ans:'Voy a contarle la noticia.',why:'achter de infinitief (of: Le voy a contar)'},
   {q:'Pregunto la hora a mis padres. →',opts:['Les pregunto la hora.','Pregunto les la hora.','Le pregunto la hora.'],ans:'Les pregunto la hora.',why:'a mis padres → les, vóór het ww.'},
   {q:'Mando un audio a Diego. →',opts:['Le mando un audio.','Mando le un audio.','Les mando un audio.'],ans:'Le mando un audio.',why:'a Diego (1) → le'},
   {q:'Voy a escribir a mi profe. →',opts:['Voy a escribirle.','Voy a le escribir.','Le voy escribir.'],ans:'Voy a escribirle.',why:'achter de infinitief (of: Le voy a escribir)'}]});
 buildChoice('gx_nac',{title:'Traduce — ir a / le / creo que',desc:'Kies de correcte Spaanse zin.',per:6,pool:[
   {q:'Ik ga bellen. →',opts:['Voy a llamar.','Voy llamar.','Voy a llamo.'],ans:'Voy a llamar.',why:'ir a + infinitivo (+ a)'},
   {q:'We gaan afspreken. →',opts:['Vamos a quedar.','Van a quedar.','Vamos quedar.'],ans:'Vamos a quedar.',why:'nosotros → vamos a'},
   {q:'Ik schrijf Diego (aan hem). →',opts:['Le escribo a Diego.','Les escribo a Diego.','Lo escribo a Diego.'],ans:'Le escribo a Diego.',why:'a Diego (1) → le'},
   {q:'Ik stuur mijn vrienden foto\'s. →',opts:['Les mando fotos a mis amigos.','Le mando fotos a mis amigos.','Los mando fotos.'],ans:'Les mando fotos a mis amigos.',why:'a mis amigos → les'},
   {q:'Ik vind dat sociale media nuttig zijn. →',opts:['Creo que las redes son útiles.','Creo que las redes sean útiles.','Creo que las redes es útil.'],ans:'Creo que las redes son útiles.',why:'creo que + indicativo'},
   {q:'Ik heb net gegeten. →',opts:['Acabo de comer.','Voy a comer.','Acabo comer.'],ans:'Acabo de comer.',why:'acabar de + infinitivo'}]});
 buildMatch('gx_conc',{title:'Empareja: verbo ↔ objeto',desc:'Koppel de actie aan het logische ding.',per:6,pool:[
   {a:'subir',b:'un vídeo'},{a:'descargar',b:'una app'},{a:'cargar',b:'la batería'},{a:'seguir',b:'a un artista'},
   {a:'mandar',b:'un mensaje'},{a:'hacer',b:'una videollamada'},{a:'apagar',b:'el móvil'},{a:'compartir',b:'una foto'}]});
 buildMatch('gx_conc2',{title:'Empareja: pregunta ↔ respuesta (le/les)',desc:'Koppel de vraag aan het juiste antwoord.',per:6,pool:[
   {a:'¿Escribes a Diego?',b:'Sí, le escribo.'},{a:'¿Mandas fotos a tus padres?',b:'Sí, les mando fotos.'},
   {a:'¿Cuentas algo a Valen?',b:'Sí, le cuento algo.'},{a:'¿Preguntas a los profes?',b:'Sí, les pregunto.'},
   {a:'¿Llamas a tu abuela?',b:'Sí, le llamo.'},{a:'¿Enseñas fotos a tus amigos?',b:'Sí, les enseño fotos.'}]});
 buildChoice('gx_mix',{title:'Repaso mixto — ir a + le/les + acabar de + creo que',desc:'Alles door elkaar. Directe feedback.',per:8,pool:[
   {q:'Yo ___ (subir) un vídeo mañana.',opts:['voy a subir','subo','acabo de subir'],ans:'voy a subir',why:'mañana → ir a'},
   {q:'___ escribo a Diego.',opts:['Le','Les','Lo'],ans:'Le',why:'a Diego (1) → le'},
   {q:'___ mando fotos a mis amigos.',opts:['Les','Le','Los'],ans:'Les',why:'a mis amigos → les'},
   {q:'Creo que las redes ___ útiles.',opts:['son','sean','es'],ans:'son',why:'indicativo'},
   {q:'Ik heb net gegeten = ',opts:['Acabo de comer.','Voy a comer.','Como.'],ans:'Acabo de comer.',why:'acabar de'},
   {q:'¿Tú ___ (salir) el sábado?',opts:['vas a salir','sales','acabas de salir'],ans:'vas a salir',why:'el sábado → ir a'},
   {q:'«ik ga eten» =',opts:['voy a comer','voy comer','voy a como'],ans:'voy a comer',why:'ir + a + infinitivo'},
   {q:'Pienso que Diego ___ razón.',opts:['tiene','tenga','tienen'],ans:'tiene',why:'indicativo'},
   {q:'Nosotros ___ (quedar) este finde.',opts:['vamos a quedar','quedamos','acabamos de quedar'],ans:'vamos a quedar',why:'este finde → ir a'},
   {q:'Voy a mandar fotos a Diego. →',opts:['Voy a mandarle fotos.','Voy a le mandar fotos.','Le voy mandar fotos.'],ans:'Voy a mandarle fotos.',why:'achter infinitivo'},
   {q:'«dit weekend» =',opts:['este fin de semana','ayer','siempre'],ans:'este fin de semana',why:'este finde'},
   {q:'Diego ___ (conectarse) ahora mismo.',opts:['acaba de conectarse','va a conectarse','se conecta'],ans:'acaba de conectarse',why:'ahora mismo → acabar de'}]});
 // ===== VOCABULARIO =====
 buildMatch('vx_match',{title:'Empareja: palabra ↔ emoji',desc:'Koppel het woord aan de emoji.',per:6,pool:[
   {a:'el móvil',b:'📱'},{a:'el ordenador',b:'💻'},{a:'la pantalla',b:'🖥️'},{a:'los auriculares',b:'🎧'},
   {a:'el cargador',b:'🔌'},{a:'la contraseña',b:'🔑'},{a:'el vídeo',b:'🎬'},{a:'la videollamada',b:'📹'},
   {a:'las redes sociales',b:'🌐'},{a:'el mensaje',b:'✉️'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat past.',per:6,pool:[
   {q:'No tengo ___ , mi móvil se apaga.',opts:['batería','pantalla','perfil'],ans:'batería',why:'batterij op = batería'},
   {q:'Escucho música con los ___ .',opts:['auriculares','mensajes','vídeos'],ans:'auriculares',why:'oortjes'},
   {q:'Para entrar necesito mi usuario y mi ___ .',opts:['contraseña','pantalla','app'],ans:'contraseña',why:'wachtwoord'},
   {q:'___ una foto a Instagram.',opts:['Subo','Apago','Cargo'],ans:'Subo',why:'uploaden = subir'},
   {q:'___ el vídeo con la clase.',opts:['Comparto','Descargo','Enciendo'],ans:'Comparto',why:'delen = compartir'},
   {q:'Por la noche ___ el móvil.',opts:['apago','enciendo','subo'],ans:'apago',why:'uitzetten = apagar'},
   {q:'Hacemos una ___ por FaceTime.',opts:['videollamada','contraseña','batería'],ans:'videollamada',why:'videogesprek'},
   {q:'Sigo a muchos artistas en las ___ .',opts:['redes sociales','pantallas','baterías'],ans:'redes sociales',why:'sociale media'},
   {q:'Creo que el móvil es muy ___ .',opts:['útil','ruidoso','antiguo'],ans:'útil',why:'nuttig'},
   {q:'Los videojuegos pueden ser ___ .',opts:['adictivos','prácticos','gratis'],ans:'adictivos',why:'verslavend'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het woord.',per:6,pool:[
   {q:'Het apparaat dat je overal meeneemt om te bellen:',opts:['el móvil','el ordenador','la tableta'],ans:'el móvil',why:'gsm'},
   {q:'Het geheime woord om in te loggen:',opts:['la contraseña','el usuario','el perfil'],ans:'la contraseña',why:'wachtwoord'},
   {q:'Een foto/video op sociale media plaatsen:',opts:['subir','descargar','apagar'],ans:'subir',why:'uploaden'},
   {q:'«ik ga…» (nabije toekomst):',opts:['voy a','acabo de','creo que'],ans:'voy a',why:'ir a + inf'},
   {q:'«ik heb net…»:',opts:['acabo de','voy a','pienso que'],ans:'acabo de',why:'acabar de'},
   {q:'Zo geef je je mening:',opts:['creo que','sigo a','apago'],ans:'creo que',why:'mening'},
   {q:'De oortjes om muziek te horen:',opts:['los auriculares','el cargador','la pantalla'],ans:'los auriculares',why:'oortjes'},
   {q:'«nuttig» in het Spaans:',opts:['útil','peligroso','gratis'],ans:'útil',why:'nuttig'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['el móvil','la tableta','el ordenador','la cocina'],odd:3,why:'la cocina is geen apparaat'},
   {words:['subir','descargar','compartir','dormir'],odd:3,why:'dormir is geen digitale actie'},
   {words:['el perfil','la publicación','el mensaje','la nevera'],odd:3,why:'la nevera hoort niet bij redes'},
   {words:['voy a','vas a','va a','tengo'],odd:3,why:'tengo is geen vorm van ir a'},
   {words:['le','les','me','del'],odd:3,why:'del is geen OI-pronomen'},
   {words:['útil','práctico','adictivo','encima'],odd:3,why:'encima is geen adjectief van media'},
   {words:['creo que','pienso que','me parece que','al lado de'],odd:3,why:'al lado de is geen meningsuitdrukking'},
   {words:['mañana','luego','este finde','ayer'],odd:3,why:'ayer is verleden, niet toekomst'}]});
 // ===== LECTURA =====
 buildOrder('lx_order',{title:'Ordena',desc:'Tik in de juiste volgorde.',rounds:[
   {sub:'el plan del sábado',items:[{label:'Primero voy a estudiar,',key:1},{label:'después voy a quedar,',key:2},{label:'luego vamos a comer',key:3},{label:'y por la noche voy a descansar.',key:4}]},
   {sub:'ir a + infinitivo',items:[{label:'Este finde',key:1},{label:'voy a',key:2},{label:'subir',key:3},{label:'un vídeo nuevo.',key:4}]},
   {sub:'le + verbo',items:[{label:'Le',key:1},{label:'escribo',key:2},{label:'un mensaje',key:3},{label:'a Diego.',key:4}]},
   {sub:'opinión con porque',items:[{label:'Creo que',key:1},{label:'el móvil',key:2},{label:'es útil',key:3},{label:'porque ayuda a estudiar.',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in de twee perfielen (Diego y Lucía) en kies.',per:6,pool:[
   {q:'¿Qué hace Diego con el móvil?',opts:['subir vídeos y chatear','solo llamar','nada'],ans:'subir vídeos y chatear',why:'«subo vídeos, chateo»'},
   {q:'¿Por qué cree Diego que el móvil es útil?',opts:['para estudiar y hablar con amigos','para dormir','para cocinar'],ans:'para estudiar y hablar con amigos',why:'«útil para estudiar y para hablar con mis amigos»'},
   {q:'¿Qué va a hacer Diego este finde?',opts:['apagar el móvil dos horas','comprar un móvil','borrar las redes'],ans:'apagar el móvil dos horas',why:'«voy a apagar el móvil dos horas al día»'},
   {q:'¿Qué piensa Lucía de las redes?',opts:['conectan pero pueden ser peligrosas','son inútiles','son aburridas'],ans:'conectan pero pueden ser peligrosas',why:'«conectan… pueden ser peligrosas»'},
   {q:'Para Lucía, lo importante es…',opts:['el equilibrio','subir más fotos','tener muchos seguidores'],ans:'el equilibrio',why:'«lo importante es el equilibrio»'},
   {q:'¿Quién dice «acabo de mirar la pantalla»?',opts:['Diego','Lucía','nadie'],ans:'Diego',why:'Diego habla de la adicción'},
   {q:'¿Qué usa Lucía para lo práctico?',opts:['el móvil','solo el ordenador','nada'],ans:'el móvil',why:'«uso el móvil para lo práctico»'},
   {q:'«por un lado… por otro…» sirve para…',opts:['dar dos puntos de vista','pedir la hora','dar direcciones'],ans:'dar dos puntos de vista',why:'contrast in een mening'}]});
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='C6plus_U3_web_mijn_versie.html';a.click();};
})();
"""

# Getypte woordenschat-drills (fase ophalen + produceren) in het paneel zelf.
JS += hub_type_sets.vocab_type_js(vocab)
JS += hub_type_gram.js('C6+', 3)
JS += (hub_bloques.escucha_js("esc_c6p_u3", escucha_data.C6P_U3)
       + hub_bloques.lectura_js("lec_c6p_u3", lectura_data.C6P_U3))
HTML = HTML.replace("__GRAMSLOTS__", hub_type_gram.slots('C6+', 3))
HTML = HTML.replace("__NGAMES__", str(len(GAMES)))
HTML = HTML.replace("__BRONNEN__", extra_bronnen.html('C6+', 3))
HTML = HTML.replace("__TYPESLOTS__", hub_type_sets.SLOTS_HTML)

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/C6plus_U3_web.html","w").write(html)
print("C6plus_U3_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
