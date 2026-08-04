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
vocab = json.load(open(f"{ROOT}/01-cursussen/06-vervolg/U1/u1_vocab.json", encoding="utf-8"))
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
   ['rutina-memoria', 'memoria de la rutina', 'memory'],
   ['sentimientos-memoria', '¿cómo estás?', 'memory'],
   ['accion-hora', 'acción ↔ hora', 'match']]],
 ['② Distinguir · gramática', [
   ['reflexivo-o-no', '¿reflexivo o no?', 'classify'],
   ['ser-estar', '¿ser o estar?', 'classify'],
   ['gusta-gustan', '¿gusta o gustan?', 'classify']]],
 ['③ Producir con apoyo', [
   ['reflexivos', 'completa: los reflexivos', 'cloze'],
   ['gustar', 'completa: gustar', 'cloze'],
   ['pronombre-tetris', 'pronombre: cinta', 'belt'],
   ['rutina-order', 'ordena tu día', 'order'],
   ['senala', 'señala', 'point']]],
 ['④ Hablar · grábate 🎙️', [
   ['repite-dia', 'escucha y repite: mi día', 'speak'],
   ['mensaje-dia', 'mensaje de voz: mi día a día', 'speak']]],
]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-c6plus-u1-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-c6plus-u1-{s}.html")}

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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="rutina">rutina</option><option value="hora">la hora</option><option value="calendario">días/meses</option><option value="frecuencia">frecuencia</option><option value="conectores">conectores</option><option value="sentimientos">sentimientos</option><option value="ocio">ocio</option><option value="gustar">gustar</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Más español en la práctica · C6+ U1 El día a día</title>
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
    <div><h1>U1 · El día a día</h1>
    <p>La página digital de la Unidad 1 (<b>el día a día</b>): flashcards, gramática visual e interactiva y <b>__NGAMES__ juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie. Thema's: rutina · reflexivos · ser/estar · gustar.</span></p></div>
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
__TYPESLOTS__
    <h2 class="sec">Naslagwerk · zoeken</h2>
    __NAS__
  </section>

  <section class="panel" data-p="gram">
    <h2 class="sec">Gramática visual e interactiva</h2>
    <p class="lead">De <b>essentiële</b> grammatica van U1: de <b>reflexieve werkwoorden</b>, <b>ser/estar</b> en <b>gustar</b>. Hier oefen je <b>maximaal</b> — elke oefening trekt uit een grote pool, dus «↻ otra serie» geeft telkens een nieuwe reeks. <span class="gloss">Eerst betekenis/patroon ontdekken, dan de regel.</span></p>
    <div class="card" id="colorsent"></div>
    <div class="card" id="irconj"></div>
    <h2 class="sec" style="margin-top:26px">🔁 Los verbos reflexivos — máxima práctica</h2>
    <p class="lead">De ster van de unit: pronombre (me·te·se·nos·os·se) + verbo. <span class="gloss">Blijf herspelen tot de vormen automatisch komen.</span></p>
    <div class="card ex" id="gx_reg"></div>
    <div class="card ex" id="gx_irreg"></div>
    <div class="card ex" id="gx_ser"></div>
    <div class="card ex" id="gx_iraq"></div>
    <div class="card ex" id="gx_subj"></div>
    <div class="card ex" id="gx_build"></div>
    <h2 class="sec" style="margin-top:26px">⚖️ Ser vs estar — el contraste</h2>
    <p class="lead">ser = identiteit/karakter · estar = plaats/gevoel. <span class="gloss">Let op: es aburrido ≠ está aburrido.</span></p>
    <div class="game" id="g_pron"></div>
    <div class="card ex" id="gx_pronq"></div>
    <h2 class="sec" style="margin-top:26px">👍 Gustar + OI — máxima práctica</h2>
    <p class="lead">gustar werkt <b>al revés</b>: me/te/le… + gusta (1/inf.) / gustan (varios). <span class="gloss">Het werkwoord volgt het ding, niet de persoon.</span></p>
    <div class="game" id="g_cantidad"></div>
    <div class="card ex" id="gx_cantq"></div>
    <div class="card ex" id="gx_adj"></div>
    <div class="card ex" id="gx_plural"></div>
    <div class="card ex" id="gx_nac"></div>
    <div class="card ex" id="gx_conc"></div>
    <div class="card ex" id="gx_conc2"></div>
    <h3 class="subh">🎯 Repaso mixto — reflexivos + ser/estar + gustar</h3>
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
    <h2 class="sec">Lectura completa · un martes cualquiera</h2>
    <p class="lead">Een echte tekst met de volledige leesroute: <b>voorspellen → globaal → scannen → juist/fout met bewijs → betekenis uit de context → zelf schrijven</b>. <span class="gloss">Dezelfde tekst staat in je cursus, met schrijfruimte.</span></p>
    <div class="card ex" id="lec_c6p_u1"></div>
  </section>


  <section class="panel" data-p="escuchar">
    <h2 class="sec">Escuchar · entrevista a un deportista 🎧</h2>
    <p class="lead">Eén fragment, zes stappen: eerst <b>weten waar je bent</b>, dan <b>globaal</b> luisteren, dan de <b>details</b>, dan <b>juist/fout met bewijs</b>. Het <b>transcript</b> gaat pas open als je klaar bent — anders lees je mee in plaats van te luisteren. <span class="gloss">Zolang er nog geen opname is, leest de computerstem het fragment voor.</span></p>
    <div class="card ex" id="esc_c6p_u1"></div>
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
    <h2 class="sec">Cultura · el horario español</h2>
    <p class="lead">Parada 1 = <b>España</b>. Un día hispano tiene su propio ritmo: se <b>come</b> a las 2–3 y se <b>cena</b> a las 9–10. <span class="gloss">In Spanje eet men laat; de dagindeling verschilt per land.</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🍽️ Se come tarde</h3>
      <p>In <b>España</b> is <b>la comida</b> (de lunch) de hoofdmaaltijd, om <b>14–15u</b>. <b>La cena</b> is licht en laat: <b>21–22u</b>. Het ontbijt (desayuno) is klein: koffie + tostada. <span class="gloss">Vergelijk met jouw dag: wanneer eet jij?</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">😴 La siesta — mito y realidad</h3>
      <p>Na de comida rusten sommige mensen even (<b>la siesta</b>), vooral in kleine steden en in de zomer. In grote steden werkt bijna niemand nog met siesta. <span class="gloss">Geen siesta voor iedereen!</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🌎 No es igual en todo el mundo</h3>
      <p>In <b>México</b> is de hoofdmaaltijd ook rond 14–15u, maar men ontbijt steviger. In veel <b>LatAm</b>-landen eet men vroeger dan in España. <span class="gloss">Un día hispano ≠ un solo horario.</span></p></div>
    <h3 class="subh">📍 La Ruta · el mapa (parada 1 = España)</h3>
    <p class="lead">De reis begint bij <b>España</b>. <b>Klik op een land</b> op de kaart voor info. Straks reizen we verder over de Spaanstalige wereld.</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    __BRONNEN__
  </section>

  <div class="foot">Más español en la práctica · edición única · Unidad 1 «El día a día» — página digital. Uitbreiding op de PDF · huisstijl morado · print ↔ PowerPoint ↔ web.</div>
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

// ---- GRAMMAR-VIZ 1: kleurgecodeerde reflexieve zin ----
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Un verbo reflexivo — la acción vuelve a ti</h3>'+
'<div class="csent">'+
'<span style="background:#dbeafe;color:#1e40af">(Yo)<span class="tip">onderwerp — de persoon</span></span> '+
'<span style="background:#ede9fe;color:#5b21b6">me<span class="tip">reflexief pronomen (past bij yo)</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">levanto<span class="tip">werkwoord · presente (levantar levant-o)</span></span> '+
'<span style="background:#ccfbf1;color:#0f766e">a las siete<span class="tip">de hora</span></span>.</div>'+
'<div class="legend"><span><i style="background:#93c5fd"></i>onderwerp</span><span><i style="background:#c4b5fd"></i>pronombre</span><span><i style="background:#fdba74"></i>werkwoord</span><span><i style="background:#5eead4"></i>hora</span></div>'+
'<p class="gloss" style="margin-top:8px">🟣 Het pronomen past bij de persoon: yo <b>me</b> levanto, tú <b>te</b> levantas, él <b>se</b> levanta. · '+(TTS?'<button class="spk-btn" onclick="speak(\'Yo me levanto a las siete\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: levantarse (reflexief) — klik om te onthullen ----
(function(){const el=document.getElementById('irconj');
 const R=[['yo','me levanto'],['tú','te levantas'],['él/ella','se levanta'],['nosotros','nos levantamos'],['vosotros','os levantáis'],['ellos','se levantan']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">El verbo «levantarse» — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">Denk eerst zelf pronombre + vorm; klik dan de kaart.</p><div class="conjgrid" id="icg"></div>';
 const g=el.querySelector('#icg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v;if(TTS)speak(p+' '+v);};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: ¿gusta o gustan? ----
function gameCantidad(){const el=document.getElementById('g_cantidad');
 const items=[['el fútbol','gusta','el fútbol (1 ding)'],['los perros','gustan','los perros (varios)'],['bailar','gusta','infinitivo → gusta'],['las películas','gustan','varias'],['la música','gusta','1 ding'],['los videojuegos','gustan','varios'],['leer','gusta','infinitivo → gusta'],['las vacaciones','gustan','varias'],['el chocolate','gusta','1 ding'],['los deportes','gustan','varios'],['la comida española','gusta','1 ding'],['las flores','gustan','varias']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿gusta o gustan?</h3><p class="desc">Me ___ … · 1 ding/infinitivo → gusta · meerdere → gustan.</p>'+scoreBar('sbC')+'<div id="cW" style="font-size:22px;font-family:var(--disp);text-align:center;margin:8px 0">Me ___ <b></b></div><div class="chips" id="cC" style="justify-content:center"></div><div class="fb" id="cFb"></div>';
 const sb=el.querySelector('#sbC');const cont=el.querySelector('#cC');
 ['gusta','gustan'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#cW b').textContent=el.cur[0];el.querySelector('#cFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#cFb'),ok,(ok?'¡Sí! ':'Nee: me '+el.cur[1]+' ')+el.cur[2]+'.');setTimeout(next,950);}
 next();}
// ---- GRAMMAR-VIZ 4: ¿ser o estar? ----
function gamePron(){const el=document.getElementById('g_pron');
 const items=[['Lucía ___ de Sevilla.','es','herkomst → ser'],['Hoy ___ cansado.','estoy','gevoel → estar'],['___ estudiante.','soy','identiteit → ser'],['La mochila ___ en clase.','está','plaats → estar'],['___ simpático.','soy','karakter → ser'],['___ muy bien, gracias.','estoy','toestand → estar'],['Diego ___ mexicano.','es','nationaliteit → ser'],['___ en casa.','estoy','plaats → estar'],['El profesor ___ alto.','es','eigenschap → ser'],['___ nervioso hoy.','estoy','gevoel → estar'],['Son las dos: ___ mediodía.','es','tijd → ser'],['La ventana ___ abierta.','está','toestand → estar']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿ser o estar?</h3><p class="desc">ser (identiteit/karakter) of estar (plaats/gevoel)? Kies de juiste vorm.</p>'+scoreBar('sbP')+'<div id="pQ" style="font-size:19px;font-family:var(--disp);text-align:center;margin:10px 0"></div><div class="chips" id="pC" style="justify-content:center"></div><div class="fb" id="pFb"></div>';
 const sb=el.querySelector('#sbP');const cont=el.querySelector('#pC');
 function chips(){cont.innerHTML='';const opts=el.cur[1]==='soy'||el.cur[1]==='es'?['soy','es','estoy','está']:['estoy','está','soy','es'];
   ['soy','eres','es','estoy','estás','está'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});}
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#pQ').textContent=el.cur[0];el.querySelector('#pFb').className='fb';chips();}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#pFb'),ok,(ok?'¡Sí! ':'Nee: ')+el.cur[1]+' ('+el.cur[2]+').');setTimeout(next,1000);}
 next();}

// ---- MOTOR-ARCADE: ingebed (aantal wordt geteld, zie hieronder) ----
document.getElementById('motorlink').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 4px">Arcade · la máquina de juegos 🕹️</h3><p class="gloss" style="margin:0 0 10px">'+MOTOR.reduce((n,g)=>n+g[1].length,0)+' extra spellen met score & directe feedback — ingebed, dus ze werken ook als je dit bestand downloadt. Klik om te spelen.</p>'+MOTOR.map(([grp,gs])=>'<div class="subh">'+grp+'</div><div class="fcgrid">'+
   gs.map(([f,t,tpl])=>'<div class="chip" style="display:block;border-radius:14px" onclick="openGame(\''+f+'\',\''+t.replace(/'/g,"")+'\')"><div style="font-weight:700;color:var(--ink);font-size:14px">'+t+'</div><div class="pill" style="margin-top:4px;font-size:10px">'+tpl+'</div></div>').join('')+'</div>').join('');
function openGame(slug,title){const g=GAMES[slug];if(!g){alert('Spel niet gevonden.');return;}
  document.getElementById('gmtitle').textContent=title;document.getElementById('gframe').src='data:text/html;base64,'+g;document.getElementById('gmodal').classList.add('show');}
function closeGame(){document.getElementById('gmodal').classList.remove('show');document.getElementById('gframe').src='about:blank';}
document.getElementById('gmodal').addEventListener('click',e=>{if(e.target.id==='gmodal')closeGame();});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeGame();});

// ---- KAART interactief ----
(function(){
   const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "🕐 El ritmo del día: se almuerza fuerte a las 14–15 h", "star": 0, "nl": ""}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "🕐 El ritmo del día: se come a las 14 h y se cena a las 21–22 h", "star": 1, "nl": "★ ¡Estás aquí! Parada U0–U1 · el mundo hispano · España (Lucía)"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "🕐 El ritmo del día: el «tinto» (café) acompaña todo el día", "star": 0, "nl": ""}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "🕐 El ritmo del día: «la hora peruana»: llegar un poco tarde", "star": 0, "nl": ""}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "🕐 El ritmo del día: la cena puede ser a las 22 h", "star": 0, "nl": ""}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "🕐 El ritmo del día: un cafecito («guayoyo») a media mañana", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "🕐 El ritmo del día: «las onces», la merienda de la tarde", "star": 0, "nl": ""}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "🕐 El ritmo del día: el almuerzo es la comida principal", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "🕐 El ritmo del día: el día empieza temprano, con el sol", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "🕐 El ritmo del día: vida en la calle y música por la tarde", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "🕐 El ritmo del día: en la altura, el ritmo es más pausado", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "🕐 El ritmo del día: la música suena desde temprano", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "🕐 El ritmo del día: jornada temprana por el calor", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "🕐 El ritmo del día: siesta al mediodía por el calor", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "🕐 El ritmo del día: vida tranquila: todo está «tuani»", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "🕐 El ritmo del día: pupusas por la noche, en las pupuserías", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "🕐 El ritmo del día: ritmo «pura vida», sin prisa", "star": 0, "nl": ""}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "🕐 El ritmo del día: la capital no duerme: ritmo financiero", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "🕐 El ritmo del día: el mate acompaña toda la jornada", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "🕐 El ritmo del día: el día acaba con música «plena»", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "🕐 El ritmo del día: el ritmo tropical marca el día", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "🕐 El ritmo del día: horarios tempranos: se cena a las 18–19 h", "star": 0, "nl": ""}};
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
 const P=[{n:'Lucía 🇪🇸',raw:'¡Hola! Soy Lucía. Entre semana me despierto a las siete y me levanto enseguida. Primero me ducho, luego desayuno tostadas con aceite. A las ocho salgo de casa. Como a las tres, ¡en España comemos tarde! Por la tarde me gusta bailar flamenco. Los fines de semana me acuesto tarde. Hoy estoy contenta porque es viernes.',
    html:'¡Hola! Soy Lucía. Entre semana <span class="ev">me despierto</span> a las siete y <span class="ev">me levanto</span> enseguida. Primero me ducho, luego desayuno tostadas. A las ocho salgo de casa. Como a las tres, ¡en España comemos tarde! Por la tarde <span class="ev">me gusta</span> bailar flamenco. Los fines de semana <span class="ev">me acuesto</span> tarde. Hoy <span class="ev">estoy contenta</span> porque es viernes.'},
   {n:'Diego 🇲🇽',raw:'¡Qué onda! Soy Diego. Me levanto a las seis y media porque el insti empieza temprano. No desayuno mucho: solo fruta. Me encantan los videojuegos y el fútbol, pero no me gusta nada madrugar. Por la tarde me gusta quedar con amigos. Normalmente me acuesto a las once. Ahora mismo estoy un poco cansado, pero feliz.',
    html:'¡Qué onda! Soy Diego. <span class="ev">Me levanto</span> a las seis y media porque el insti empieza temprano. No desayuno mucho: solo fruta. <span class="ev">Me encantan</span> los videojuegos y el fútbol, pero <span class="ev">no me gusta nada</span> madrugar. Por la tarde me gusta quedar con amigos. Normalmente <span class="ev">me acuesto</span> a las once. Ahora mismo <span class="ev">estoy cansado</span>, pero feliz.'}];
 el.innerHTML='<div class="perfiles">'+P.map((m,i)=>'<div class="perfil"><h4>👤 '+m.n+' '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lm'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div class="txt" id="lm'+i+'" data-raw="'+m.raw.replace(/"/g,'&quot;')+'">'+m.html+'</div></div>').join('')+'</div>';
 const items=[['A Lucía le gusta bailar.',true,'«me gusta bailar flamenco»'],['Diego se levanta a las siete.',false,'se levanta a las seis y media'],['A Diego le gusta madrugar.',false,'«no me gusta nada madrugar»'],['Lucía come a las tres.',true,'«Como a las tres»'],['A Diego le encantan los videojuegos.',true,'«Me encantan los videojuegos»'],['Lucía se acuesta temprano el fin de semana.',false,'«los fines de semana me acuesto tarde»'],['Diego desayuna fruta.',true,'«solo fruta»'],['Hoy Lucía está contenta.',true,'«estoy contenta porque es viernes»']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — con evidencia</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">¿Y tú? Reacciona</h3><p class="gloss" style="margin:0 0 8px">¿Con quién tienes más en común, con Diego o con Nina? Escribe 2–3 frases con <b>porque</b>. Grábalo en <b>Hablar 🎙️</b>.</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="Tengo más en común con… porque…"></textarea>';
 el.appendChild(box);el.appendChild(resp);}

// ---------- INLINE RECORDER (MediaRecorder) ----------
""" + hub_drills.RECORDER_JS + r"""
function buildRecorders(){
 makeRecorder('rec_repite',{title:'Escucha y repite: mi día',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'Me levanto a las siete y cuarto.',cue:'la rutina',tip:'Duidelijk? Probeer nog eens zonder te lezen.'},{text:'Primero me ducho y luego desayuno.',cue:'conectores'},{text:'Como a las dos y ceno a las nueve.',cue:'la hora'},{text:'Me gusta bailar porque es divertido.',cue:'opinión'},{text:'Hoy estoy contento porque es viernes.',cue:'ser/estar'},{text:'¿A qué hora te levantas tú?',cue:'interacción'}]});
 makeRecorder('rec_pedido',{title:'Mensaje de voz: mi día a día',desc:'Neem één bericht op (30–40 s): je rutina met 5 reflexieve werkwoorden, de hora en conectores.',items:[
   {text:'Describe tu rutina: 5 verbos reflexivos + la hora + conectores (primero, luego, después).',cue:'mi día',tip:'5 reflexieve werkwoorden + de hora gezegd? Neem opnieuw op.'}]});
 makeRecorder('rec_plato',{title:'Mis gustos y cómo estoy',desc:'Zeg wat je (niet) leuk vindt met «porque», en hoe je je vandaag voelt.',items:[
   {text:'Me gusta ___ porque ___ . No me gusta ___ . Hoy estoy ___ .',cue:'gustos + ánimo',tip:'2 gustos + 1 porque + 1 sentimiento? Herneem.'}]});
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
 // ===== REFLEXIVOS (essentieel · grote pools) =====
 buildChoice('gx_reg',{title:'Los reflexivos: pronombre + verbo',desc:'Kies de juiste reflexieve vorm (pronombre + verbo).',per:8,pool:[
   {q:'(Yo) ___ a las siete. (levantarse)',opts:['me levanto','te levantas','se levanta'],ans:'me levanto',why:'yo → me levanto'},
   {q:'(Tú) ___ por la mañana. (ducharse)',opts:['te duchas','me ducho','se ducha'],ans:'te duchas',why:'tú → te duchas'},
   {q:'Lucía ___ rápido. (vestirse)',opts:['se viste','me visto','te vistes'],ans:'se viste',why:'ella → se viste'},
   {q:'(Nosotros) ___ a las once. (acostarse)',opts:['nos acostamos','os acostáis','se acuestan'],ans:'nos acostamos',why:'nosotros → nos acostamos'},
   {q:'(Vosotros) ___ tarde. (levantarse)',opts:['os levantáis','nos levantamos','se levantan'],ans:'os levantáis',why:'vosotros → os levantáis'},
   {q:'Mis padres ___ a las seis. (despertarse)',opts:['se despiertan','nos despertamos','os despertáis'],ans:'se despiertan',why:'ellos → se despiertan'},
   {q:'(Yo) ___ los dientes. (lavarse)',opts:['me lavo','te lavas','se lava'],ans:'me lavo',why:'yo → me lavo'},
   {q:'(Tú) ___ en el sofá. (sentarse)',opts:['te sientas','me siento','se sienta'],ans:'te sientas',why:'tú → te sientas'},
   {q:'Diego ___ enseguida. (dormirse)',opts:['se duerme','me duermo','te duermes'],ans:'se duerme',why:'él → se duerme'},
   {q:'(Nosotros) ___ delante del espejo. (peinarse)',opts:['nos peinamos','os peináis','se peinan'],ans:'nos peinamos',why:'nosotros → nos peinamos'},
   {q:'(Yo) ___ enseguida. (despertarse)',opts:['me despierto','te despiertas','se despierta'],ans:'me despierto',why:'yo → me despierto'},
   {q:'Los niños ___ a las nueve. (acostarse)',opts:['se acuestan','nos acostamos','os acostáis'],ans:'se acuestan',why:'ellos → se acuestan'}]});
 buildChoice('gx_irreg',{title:'Reflexivos con cambio vocálico (la bota)',desc:'despertarse (e→ie) · acostarse (o→ue) · vestirse (e→i). Kies de vorm.',per:7,pool:[
   {q:'(Yo) me ___ a las siete. (despertarse e→ie)',opts:['despierto','despierta','despiertas'],ans:'despierto',why:'yo → me despierto'},
   {q:'(Tú) te ___ tarde. (acostarse o→ue)',opts:['acuestas','acostas','acuestes'],ans:'acuestas',why:'tú → te acuestas'},
   {q:'Ella se ___ rápido. (vestirse e→i)',opts:['viste','vieste','vesta'],ans:'viste',why:'ella → se viste'},
   {q:'(Nosotros) nos ___ temprano. (despertarse)',opts:['despertamos','despiertamos','despertimos'],ans:'despertamos',why:'nosotros: GEEN wissel → despertamos'},
   {q:'(Yo) me ___ a las once. (acostarse)',opts:['acuesto','acosto','acuesta'],ans:'acuesto',why:'yo → me acuesto'},
   {q:'(Vosotros) os ___ elegantes. (vestirse)',opts:['vestís','vistéis','vestéis'],ans:'vestís',why:'vosotros: GEEN wissel → vestís'},
   {q:'Ellos se ___ a las seis. (despertarse)',opts:['despiertan','despertan','despierten'],ans:'despiertan',why:'ellos → se despiertan'},
   {q:'(Tú) te ___ rápido. (vestirse)',opts:['vistes','vestes','vistas'],ans:'vistes',why:'tú → te vistes'},
   {q:'(Nosotros) nos ___ a medianoche. (acostarse)',opts:['acostamos','acuestamos','acostemos'],ans:'acostamos',why:'nosotros: GEEN wissel → acostamos'},
   {q:'Él se ___ enseguida. (dormirse o→ue)',opts:['duerme','dorme','duermo'],ans:'duerme',why:'él → se duerme'}]});
 buildChoice('gx_ser',{title:'Conjuga «levantarse»',desc:'De volledige reflexieve vervoeging. Kies pronombre + vorm.',per:6,pool:[
   {q:'yo →',opts:['me levanto','te levantas','se levanta'],ans:'me levanto',why:'yo → me levanto'},
   {q:'tú →',opts:['te levantas','me levanto','se levanta'],ans:'te levantas',why:'tú → te levantas'},
   {q:'él/ella →',opts:['se levanta','te levantas','nos levantamos'],ans:'se levanta',why:'él/ella → se levanta'},
   {q:'nosotros →',opts:['nos levantamos','os levantáis','se levantan'],ans:'nos levantamos',why:'nosotros → nos levantamos'},
   {q:'vosotros →',opts:['os levantáis','se levantan','nos levantamos'],ans:'os levantáis',why:'vosotros → os levantáis'},
   {q:'ellos →',opts:['se levantan','os levantáis','se levanta'],ans:'se levantan',why:'ellos → se levantan'},
   {q:'María y yo ___ temprano.',opts:['nos levantamos','se levantan','os levantáis'],ans:'nos levantamos',why:'nosotros → nos levantamos'},
   {q:'Tú y él ___ tarde.',opts:['os levantáis','nos levantamos','se levantan'],ans:'os levantáis',why:'vosotros → os levantáis'}]});
 buildChoice('gx_iraq',{title:'Los reflexivos — todo mezclado',desc:'Alle personen door elkaar. Directe feedback.',per:8,pool:[
   {q:'(Yo) ___ a las siete.',opts:['me levanto','te levantas','se levanta'],ans:'me levanto',why:'yo → me levanto'},
   {q:'¿(Tú) ___ por la mañana?',opts:['te duchas','me ducho','se ducha'],ans:'te duchas',why:'tú → te duchas'},
   {q:'Lucía ___ temprano.',opts:['se despierta','me despierto','te despiertas'],ans:'se despierta',why:'ella → se despierta'},
   {q:'(Nosotros) ___ a las once.',opts:['nos acostamos','os acostáis','se acuestan'],ans:'nos acostamos',why:'nosotros → nos acostamos'},
   {q:'Diego ___ rápido.',opts:['se viste','me visto','te vistes'],ans:'se viste',why:'él → se viste'},
   {q:'(Yo) ___ enseguida.',opts:['me duermo','te duermes','se duerme'],ans:'me duermo',why:'yo → me duermo'},
   {q:'¿(Vosotros) ___ aquí?',opts:['os sentáis','se sientan','nos sentamos'],ans:'os sentáis',why:'vosotros → os sentáis'},
   {q:'Mis hermanos ___ delante del espejo.',opts:['se peinan','nos peinamos','os peináis'],ans:'se peinan',why:'ellos → se peinan'},
   {q:'(Tú) ___ los dientes.',opts:['te lavas','me lavo','se lava'],ans:'te lavas',why:'tú → te lavas'},
   {q:'(Yo) ___ a las once.',opts:['me acuesto','te acuestas','se acuesta'],ans:'me acuesto',why:'yo → me acuesto'},
   {q:'Ella ___ por la noche.',opts:['se ducha','te duchas','me ducho'],ans:'se ducha',why:'ella → se ducha'},
   {q:'(Nosotros) ___ temprano.',opts:['nos despertamos','os despertáis','se despiertan'],ans:'nos despertamos',why:'nosotros → nos despertamos'},
   {q:'(Vosotros) ___ tarde.',opts:['os levantáis','nos levantamos','se levantan'],ans:'os levantáis',why:'vosotros → os levantáis'},
   {q:'(Yo) ___ en el sofá.',opts:['me siento','te sientas','se sienta'],ans:'me siento',why:'yo → me siento'}]});
 buildChoice('gx_subj',{title:'¿Qué pronombre reflexivo?',desc:'Kies het pronomen dat bij het onderwerp past (me/te/se/nos/os/se).',per:7,pool:[
   {q:'Yo ___ levanto',opts:['me','te','se'],ans:'me',why:'yo → me'},
   {q:'Tú ___ duchas',opts:['te','me','se'],ans:'te',why:'tú → te'},
   {q:'Él ___ acuesta',opts:['se','te','nos'],ans:'se',why:'él → se'},
   {q:'Nosotros ___ vestimos',opts:['nos','os','se'],ans:'nos',why:'nosotros → nos'},
   {q:'Vosotros ___ peináis',opts:['os','nos','se'],ans:'os',why:'vosotros → os'},
   {q:'Ellos ___ despiertan',opts:['se','os','me'],ans:'se',why:'ellos → se'},
   {q:'Usted ___ sienta',opts:['se','te','me'],ans:'se',why:'usted → se (3ª)'},
   {q:'Ella y yo ___ dormimos pronto',opts:['nos','se','os'],ans:'nos',why:'nosotros → nos'},
   {q:'¿Y tú, a qué hora ___ acuestas?',opts:['te','se','me'],ans:'te',why:'tú → te'},
   {q:'Mis padres ___ lavan las manos',opts:['se','nos','os'],ans:'se',why:'ellos → se'}]});
 buildOrder('gx_build',{title:'Ordena tu rutina',desc:'Tik de acties in de logische volgorde.',rounds:[
   {sub:'la mañana',items:[{label:'Me despierto a las 7:00.',key:1},{label:'Me ducho.',key:2},{label:'Desayuno.',key:3},{label:'Salgo de casa.',key:4}]},
   {sub:'con conectores',items:[{label:'Primero me levanto.',key:1},{label:'Luego me visto.',key:2},{label:'Después desayuno.',key:3},{label:'Por último, voy al insti.',key:4}]},
   {sub:'la tarde y la noche',items:[{label:'Vuelvo a casa.',key:1},{label:'Hago los deberes.',key:2},{label:'Ceno a las nueve.',key:3},{label:'Me acuesto.',key:4}]},
   {sub:'la hora, de menor a mayor',items:[{label:'Es la una.',key:1},{label:'Son las tres y cuarto.',key:2},{label:'Son las seis y media.',key:3},{label:'Son las nueve.',key:4}]},
   {sub:'una opinión (me gusta… porque)',items:[{label:'Me gusta el finde',key:1},{label:'porque',key:2},{label:'no hay clase',key:3},{label:'y quedo con amigos.',key:4}]}]});
 buildChoice('gx_pronq',{title:'¿ser o estar?',desc:'ser (identiteit/karakter) of estar (plaats/gevoel)? Kies de vorm.',per:7,pool:[
   {q:'Lucía ___ de Sevilla.',opts:['es','está','soy'],ans:'es',why:'herkomst → ser'},
   {q:'Hoy ___ cansado.',opts:['estoy','soy','está'],ans:'estoy',why:'gevoel → estar'},
   {q:'(Yo) ___ estudiante.',opts:['soy','estoy','es'],ans:'soy',why:'identiteit → ser'},
   {q:'La mochila ___ en clase.',opts:['está','es','estoy'],ans:'está',why:'plaats → estar'},
   {q:'Diego ___ simpático.',opts:['es','está','soy'],ans:'es',why:'karakter → ser'},
   {q:'(Yo) ___ muy bien, gracias.',opts:['estoy','soy','está'],ans:'estoy',why:'toestand → estar'},
   {q:'Nosotros ___ de Bélgica.',opts:['somos','estamos','sois'],ans:'somos',why:'herkomst → ser'},
   {q:'La ventana ___ abierta.',opts:['está','es','están'],ans:'está',why:'toestand → estar'},
   {q:'Son las dos: ___ mediodía.',opts:['es','está','son'],ans:'es',why:'tijd → ser'},
   {q:'Los alumnos ___ en el patio.',opts:['están','son','estáis'],ans:'están',why:'plaats → estar'},
   {q:'La clase ___ aburrida (saai).',opts:['es','está','son'],ans:'es',why:'eigenschap → ser'},
   {q:'(Yo) ___ aburrido (verveel me).',opts:['estoy','soy','está'],ans:'estoy',why:'toestand nu → estar'}]});
 // ===== GUSTAR (essentieel · grote pools) =====
 buildChoice('gx_cantq',{title:'¿gusta o gustan?',desc:'1 ding/infinitivo → gusta · meerdere → gustan.',per:8,pool:[
   {q:'Me ___ el fútbol.',opts:['gusta','gustan','gusto'],ans:'gusta',why:'el fútbol (1)'},
   {q:'Me ___ los perros.',opts:['gustan','gusta','gustas'],ans:'gustan',why:'los perros (varios)'},
   {q:'Me ___ bailar.',opts:['gusta','gustan','gusto'],ans:'gusta',why:'infinitivo → gusta'},
   {q:'Me ___ las películas.',opts:['gustan','gusta','gustas'],ans:'gustan',why:'las películas (varias)'},
   {q:'Me ___ la música.',opts:['gusta','gustan','gusto'],ans:'gusta',why:'la música (1)'},
   {q:'Me ___ los videojuegos.',opts:['gustan','gusta','gustas'],ans:'gustan',why:'los videojuegos (varios)'},
   {q:'Me ___ cantar y bailar.',opts:['gusta','gustan','gusto'],ans:'gusta',why:'infinitivos → gusta'},
   {q:'Me ___ las vacaciones.',opts:['gustan','gusta','gustas'],ans:'gustan',why:'las vacaciones (varias)'},
   {q:'Me ___ el chocolate.',opts:['gusta','gustan','gusto'],ans:'gusta',why:'el chocolate (1)'},
   {q:'Me ___ los deportes.',opts:['gustan','gusta','gustas'],ans:'gustan',why:'los deportes (varios)'},
   {q:'Me ___ leer.',opts:['gusta','gustan','gusto'],ans:'gusta',why:'infinitivo → gusta'},
   {q:'Me ___ las flores.',opts:['gustan','gusta','gustas'],ans:'gustan',why:'las flores (varias)'}]});
 buildChoice('gx_adj',{title:'Gustar: los pronombres (me/te/le…)',desc:'Kies het juiste voornaamwoord (a wie bevalt het?).',per:7,pool:[
   {q:'A mí ___ gusta el cine.',opts:['me','te','le'],ans:'me',why:'a mí → me'},
   {q:'A ti ___ gustan los deportes.',opts:['te','me','le'],ans:'te',why:'a ti → te'},
   {q:'A Lucía ___ gusta bailar.',opts:['le','les','me'],ans:'le',why:'a Lucía → le'},
   {q:'A nosotros ___ gusta viajar.',opts:['nos','os','les'],ans:'nos',why:'a nosotros → nos'},
   {q:'¿A vosotros ___ gusta la música?',opts:['os','nos','les'],ans:'os',why:'a vosotros → os'},
   {q:'A mis amigos ___ gustan los videojuegos.',opts:['les','le','nos'],ans:'les',why:'a ellos → les'},
   {q:'A Diego ___ gusta el fútbol.',opts:['le','les','te'],ans:'le',why:'a Diego → le'},
   {q:'A mí ___ encanta la comida española.',opts:['me','te','le'],ans:'me',why:'a mí → me'},
   {q:'A mis padres ___ gusta la siesta.',opts:['les','le','nos'],ans:'les',why:'a ellos → les'},
   {q:'¿A ti ___ gusta madrugar?',opts:['te','me','le'],ans:'te',why:'a ti → te'}]});
 buildChoice('gx_plural',{title:'La hora — ¿qué hora es?',desc:'Kies de juiste tijd in woorden.',per:7,pool:[
   {q:'1:00 →',opts:['es la una','son la una','son las una'],ans:'es la una',why:'1 uur → es la una'},
   {q:'3:00 →',opts:['son las tres','es las tres','son la tres'],ans:'son las tres',why:'2+ → son las'},
   {q:'3:15 →',opts:['son las tres y cuarto','son las tres y media','son las tres menos cuarto'],ans:'son las tres y cuarto',why:':15 → y cuarto'},
   {q:'6:30 →',opts:['son las seis y media','son las seis y cuarto','es la seis y media'],ans:'son las seis y media',why:':30 → y media'},
   {q:'4:45 →',opts:['son las cinco menos cuarto','son las cuatro y cuarto','son las cuatro menos cuarto'],ans:'son las cinco menos cuarto',why:':45 → menos cuarto (volgende uur)'},
   {q:'9:00 en punto →',opts:['son las nueve en punto','son las nueve y punto','es las nueve'],ans:'son las nueve en punto',why:'op het uur → en punto'},
   {q:'2:15 →',opts:['son las dos y cuarto','son las dos y media','es la dos y cuarto'],ans:'son las dos y cuarto',why:':15 → y cuarto'},
   {q:'1:30 →',opts:['es la una y media','son la una y media','son las una y media'],ans:'es la una y media',why:'1 uur → es la una y media'},
   {q:'¿A qué hora te levantas? →',opts:['A las siete','Son las siete','Es las siete'],ans:'A las siete',why:'¿a qué hora? → a las…'},
   {q:'8:45 →',opts:['son las nueve menos cuarto','son las ocho menos cuarto','son las ocho y cuarto'],ans:'son las nueve menos cuarto',why:':45 → menos cuarto'}]});
 buildChoice('gx_nac',{title:'Traduce al revés (gustar)',desc:'Kies de correcte Spaanse zin. ¡Ojo con la estructura!',per:6,pool:[
   {q:'Ik hou van honden. →',opts:['Me gustan los perros','Yo gusto los perros','Me gusta los perros'],ans:'Me gustan los perros',why:'varios → gustan'},
   {q:'Ik vind voetbal leuk. →',opts:['Me gusta el fútbol','Yo gusto el fútbol','Me gustan el fútbol'],ans:'Me gusta el fútbol',why:'1 ding → gusta + el'},
   {q:'Hij houdt van reizen. →',opts:['Le gusta viajar','Le gustan viajar','Él gusta viajar'],ans:'Le gusta viajar',why:'le + infinitivo → gusta'},
   {q:'Wij vinden horrorfilms niet leuk. →',opts:['No nos gustan las películas de terror','No nos gusta las películas','Nosotros no gustamos'],ans:'No nos gustan las películas de terror',why:'varias → gustan'},
   {q:'Vind jij reggaetón leuk? →',opts:['¿Te gusta el reguetón?','¿Tú gustas el reguetón?','¿Te gustan el reguetón?'],ans:'¿Te gusta el reguetón?',why:'te + 1 ding → gusta'},
   {q:'Mijn ouders houden van de siësta. →',opts:['A mis padres les gusta la siesta','A mis padres le gusta la siesta','Mis padres gustan la siesta'],ans:'A mis padres les gusta la siesta',why:'a ellos → les'},
   {q:'Ik vind maandagen niet leuk. →',opts:['No me gustan los lunes','No me gusta los lunes','Yo no gusto los lunes'],ans:'No me gustan los lunes',why:'los lunes (varios) → gustan'},
   {q:'Ik dans graag. →',opts:['Me gusta bailar','Me gustan bailar','Yo gusto bailar'],ans:'Me gusta bailar',why:'infinitivo → gusta'}]});
 buildMatch('gx_conc',{title:'Empareja: acción ↔ hora',desc:'Koppel de actie aan een logisch uur.',per:6,pool:[
   {a:'me levanto',b:'a las 7:00'},{a:'desayuno',b:'a las 7:30'},{a:'como',b:'a las 14:00'},
   {a:'meriendo',b:'a las 17:00'},{a:'ceno',b:'a las 21:00'},{a:'me acuesto',b:'a las 23:00'},
   {a:'empiezan las clases',b:'a las 8:30'},{a:'vuelvo a casa',b:'a las 16:00'},{a:'hago deporte',b:'los martes'},{a:'quedo con amigos',b:'el sábado'}]});
 buildMatch('gx_conc2',{title:'Empareja: infinitivo ↔ forma «yo»',desc:'Koppel het reflexieve werkwoord aan de yo-vorm.',per:6,pool:[
   {a:'levantarse',b:'me levanto'},{a:'ducharse',b:'me ducho'},{a:'vestirse',b:'me visto'},
   {a:'acostarse',b:'me acuesto'},{a:'despertarse',b:'me despierto'},{a:'peinarse',b:'me peino'},
   {a:'sentarse',b:'me siento'},{a:'dormirse',b:'me duermo'},{a:'lavarse',b:'me lavo'},{a:'llamarse',b:'me llamo'}]});
 buildChoice('gx_mix',{title:'Repaso mixto — reflexivos + ser/estar + gustar',desc:'Alles door elkaar. Directe feedback.',per:8,pool:[
   {q:'(Yo) ___ a las siete.',opts:['me levanto','te levantas','se levanta'],ans:'me levanto',why:'reflexivo: yo → me levanto'},
   {q:'Lucía ___ de Sevilla.',opts:['es','está','soy'],ans:'es',why:'herkomst → ser'},
   {q:'Me ___ los perros.',opts:['gustan','gusta','gusto'],ans:'gustan',why:'varios → gustan'},
   {q:'Hoy (yo) ___ cansado.',opts:['estoy','soy','está'],ans:'estoy',why:'gevoel → estar'},
   {q:'A Diego ___ gusta el fútbol.',opts:['le','les','me'],ans:'le',why:'a Diego → le'},
   {q:'(Nosotros) ___ a las once.',opts:['nos acostamos','os acostáis','se acuestan'],ans:'nos acostamos',why:'reflexivo: nosotros'},
   {q:'La mochila ___ en clase.',opts:['está','es','estoy'],ans:'está',why:'plaats → estar'},
   {q:'Me ___ bailar.',opts:['gusta','gustan','gusto'],ans:'gusta',why:'infinitivo → gusta'},
   {q:'¿(Tú) ___ por la mañana? (ducharse)',opts:['te duchas','me ducho','se ducha'],ans:'te duchas',why:'reflexivo: tú'},
   {q:'Diego ___ mexicano.',opts:['es','está','soy'],ans:'es',why:'nationaliteit → ser'},
   {q:'A mí no ___ gusta madrugar.',opts:['me','te','le'],ans:'me',why:'a mí → me'},
   {q:'3:30 →',opts:['son las tres y media','son las tres y cuarto','es la tres y media'],ans:'son las tres y media',why:':30 → y media'},
   {q:'(Yo) ___ contento porque es viernes.',opts:['estoy','soy','está'],ans:'estoy',why:'gevoel → estar'},
   {q:'Ellos ___ tarde. (acostarse)',opts:['se acuestan','nos acostamos','os acostáis'],ans:'se acuestan',why:'reflexivo: ellos'}]});
 // VOCABULARIO
 buildMatch('vx_match',{title:'Empareja: sentimiento ↔ emoji',desc:'Koppel het gevoel aan de emoji.',per:6,pool:[
   {a:'contento',b:'😀'},{a:'triste',b:'😢'},{a:'cansado',b:'😴'},{a:'nervioso',b:'😰'},
   {a:'enfadado',b:'😠'},{a:'relajado',b:'😌'},{a:'aburrido',b:'🥱'},{a:'feliz',b:'😄'},
   {a:'estresado',b:'😖'},{a:'ocupado',b:'📚'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat in de zin past.',per:6,pool:[
   {q:'Por la mañana ___ a las siete.',opts:['me levanto','me acuesto','ceno'],ans:'me levanto',why:'la rutina'},
   {q:'En España se ___ a las tres.',opts:['come','duerme','levanta'],ans:'come',why:'la comida a las 3'},
   {q:'Primero me ducho, ___ desayuno.',opts:['luego','porque','siempre'],ans:'luego',why:'conector de secuencia'},
   {q:'___ me levanto a las siete (100%).',opts:['Siempre','Nunca','A veces'],ans:'Siempre',why:'100% → siempre'},
   {q:'Hoy estoy ___ porque es viernes.',opts:['contento','cansado','triste'],ans:'contento',why:'sentimiento +'},
   {q:'Me ___ bailar porque es divertido.',opts:['gusta','gustan','gusto'],ans:'gusta',why:'infinitivo → gusta'},
   {q:'¿Qué ___ es? — Son las dos.',opts:['hora','día','año'],ans:'hora',why:'¿qué hora es?'},
   {q:'Después de cenar, me ___ a las once.',opts:['acuesto','levanto','ducho'],ans:'acuesto',why:'acostarse = naar bed'},
   {q:'— Me gusta el pop. — A mí ___ .',opts:['también','tampoco','no'],ans:'también',why:'reageren op (+)'},
   {q:'En ___ hace frío y en verano hace calor.',opts:['invierno','primavera','otoño'],ans:'invierno',why:'estaciones'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het juiste woord.',per:6,pool:[
   {q:'Wakker worden:',opts:['despertarse','acostarse','ducharse'],ans:'despertarse',why:'despertarse'},
   {q:'De maaltijd rond 21u in Spanje:',opts:['la cena','el desayuno','la merienda'],ans:'la cena',why:'la cena = avondeten'},
   {q:'100% van de tijd:',opts:['siempre','nunca','a veces'],ans:'siempre',why:'siempre = altijd'},
   {q:'Wat je zegt bij een positieve mening (max):',opts:['me encanta','no me gusta','me gusta'],ans:'me encanta',why:'me encanta = het maximum'},
   {q:'Het gevoel na een examen soms:',opts:['nervioso','contento','relajado'],ans:'nervioso',why:'nervioso'},
   {q:'Korte rust na de lunch in España:',opts:['la siesta','la merienda','el recreo'],ans:'la siesta',why:'la siesta'},
   {q:'Kwart over drie:',opts:['las tres y cuarto','las tres y media','las tres menos cuarto'],ans:'las tres y cuarto',why:':15 → y cuarto'},
   {q:'Eerst… daarna… (verbindingswoord):',opts:['primero … luego','porque … pero','siempre … nunca'],ans:'primero … luego',why:'conectores de secuencia'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['me levanto','me ducho','me visto','desayuno'],odd:3,why:'desayuno is niet reflexief'},
   {words:['siempre','a veces','nunca','contento'],odd:3,why:'contento is een gevoel, geen frecuencia'},
   {words:['contento','cansado','nervioso','lunes'],odd:3,why:'lunes is een dag, geen gevoel'},
   {words:['primero','luego','después','porque'],odd:3,why:'porque = reden, de rest = secuencia'},
   {words:['gusta','gustan','encanta','levanto'],odd:3,why:'levanto is geen gustar-vorm'},
   {words:['enero','julio','martes','diciembre'],odd:2,why:'martes is een dag, de rest = maanden'},
   {words:['me','te','se','el'],odd:3,why:'el is een lidwoord, de rest = reflexief pronomen'},
   {words:['la mañana','la tarde','la noche','la siesta'],odd:3,why:'la siesta is geen deel van de dag/momento'}]});
 // LECTURA
 buildOrder('lx_order',{title:'Ordena el día',desc:'Tik de zinnen in de juiste volgorde.',rounds:[
   {sub:'el día de Lucía',items:[{label:'Me despierto a las siete.',key:1},{label:'Me ducho y desayuno.',key:2},{label:'Como a las tres.',key:3},{label:'Por la tarde bailo flamenco.',key:4}]},
   {sub:'el día de Diego',items:[{label:'Me levanto a las seis y media.',key:1},{label:'Desayuno fruta.',key:2},{label:'Quedo con amigos.',key:3},{label:'Me acuesto a las once.',key:4}]},
   {sub:'de + a − (la escala de gustos)',items:[{label:'me encanta',key:1},{label:'me gusta',key:2},{label:'no me gusta',key:3},{label:'no me gusta nada',key:4}]},
   {sub:'la hora, de menor a mayor',items:[{label:'es la una',key:1},{label:'son las cinco',key:2},{label:'son las ocho y media',key:3},{label:'son las diez',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in de twee perfielen (Lucía y Diego) en kies.',per:6,pool:[
   {q:'¿A qué hora se levanta Lucía?',opts:['a las siete','a las seis y media','a las ocho'],ans:'a las siete',why:'«me despierto a las siete»'},
   {q:'¿Qué le gusta hacer a Lucía por la tarde?',opts:['bailar flamenco','jugar al fútbol','leer'],ans:'bailar flamenco',why:'«me gusta bailar flamenco»'},
   {q:'¿A qué hora come Lucía?',opts:['a las tres','a las dos','a la una'],ans:'a las tres',why:'«Como a las tres»'},
   {q:'¿Qué NO le gusta a Diego?',opts:['madrugar','el fútbol','los videojuegos'],ans:'madrugar',why:'«no me gusta nada madrugar»'},
   {q:'¿Qué desayuna Diego?',opts:['fruta','tostadas','nada'],ans:'fruta',why:'«solo fruta»'},
   {q:'¿A qué hora se acuesta Diego?',opts:['a las once','a las diez','a medianoche'],ans:'a las once',why:'«me acuesto a las once»'},
   {q:'¿Cómo está Lucía hoy?',opts:['contenta','cansada','nerviosa'],ans:'contenta',why:'«estoy contenta»'},
   {q:'¿Qué le encanta a Diego?',opts:['los videojuegos','el flamenco','la siesta'],ans:'los videojuegos',why:'«Me encantan los videojuegos»'}]});
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='C6plus_U1_web_mijn_versie.html';a.click();};
})();
"""

# Getypte woordenschat-drills (fase ophalen + produceren) in het paneel zelf.
JS += hub_type_sets.vocab_type_js(vocab)
JS += hub_type_gram.js('C6+', 1)
JS += (hub_bloques.escucha_js("esc_c6p_u1", escucha_data.C6P_U1)
       + hub_bloques.lectura_js("lec_c6p_u1", lectura_data.C6P_U1))
HTML = HTML.replace("__GRAMSLOTS__", hub_type_gram.slots('C6+', 1))
HTML = HTML.replace("__BRONNEN__", extra_bronnen.html('C6+', 1))
# Aantal spellen wordt geteld, niet met de hand bijgehouden.
HTML = HTML.replace("__NGAMES__", str(len(GAMES)))
HTML = HTML.replace("__TYPESLOTS__", hub_type_sets.SLOTS_HTML)

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/C6plus_U1_web.html","w").write(html)
print("C6plus_U1_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
