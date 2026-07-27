#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C5 · U5 «¡Ñam!».
# Eén standalone bestand: fonts base64, de 21 U5-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U5-vocab), visuele/interactieve grammatica (cantidades · ir a + inf · lo/la/los/las),
# klikbare kaart (mundo hispano, parada 5 = México) + TTS + inline recorder + Lectura + editbar. Huisstijl groen.
import json, base64, os, sys
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
GEN = f"{ROOT}/02-huisstijl/beeld/generators"
sys.path.insert(0, GEN); import cast_gen as C; import vocab_icons as VI; import vocab_emoji as VE
vocab = json.load(open(f"{ROOT}/01-cursussen/06-vervolg/U0/u0_vocab.json", encoding="utf-8"))
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
   ['saludos-memoria', 'memoria del reencuentro', 'memory'],
   ['paises-memoria', 'banderas y países', 'memory'],
   ['pais-nacionalidad', 'país ↔ nacionalidad', 'match']]],
 ['② Distinguir · gramática', [
   ['formal-informal', '¿formal o informal?', 'classify'],
   ['genero', '¿el o la?', 'classify'],
   ['ser-estar', '¿soy o estoy?', 'classify']]],
 ['③ Producir con apoyo', [
   ['presente', 'completa: el presente', 'cloze'],
   ['concordancia', 'completa: concordancia', 'cloze'],
   ['concordancia-tetris', 'concordancia Tetris', 'tetris'],
   ['presentacion-order', 'ordena la presentación', 'order'],
   ['senala', 'señala', 'point']]],
 ['④ Hablar · grábate 🎙️', [
   ['repite-saludos', 'escucha y repite: saludos', 'speak'],
   ['mensaje-presentate', 'mensaje de voz: preséntate', 'speak']]],
]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-c6plus-u0-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-c6plus-u0-{s}.html")}

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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="saludos">saludos</option><option value="presentarse">presentarse</option><option value="clase">en clase</option><option value="paises">países</option><option value="nacionalidades">nacionalidades</option><option value="descripcion">descripción</option><option value="familia">familia</option><option value="numeros">números</option><option value="verbos">verbos</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Español en la práctica · C6+ U0 ¡Volvemos!</title>
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
    <div><h1>U0 · ¡Volvemos!</h1>
    <p>La página digital de la Unidad 0 (el <b>reencuentro</b>): flashcards, gramática visual e interactiva y <b>13 juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie. Diagnostische repaso: presente · género · países.</span></p></div>
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
    <h2 class="sec">Naslagwerk · zoeken</h2>
    __NAS__
  </section>

  <section class="panel" data-p="gram">
    <h2 class="sec">Gramática visual e interactiva</h2>
    <p class="lead">Eerst betekenis en patroon ontdekken, dan de regel. Beweeg over de woorden, klik, en probeer. <span class="gloss">Alles binnen het thema van U0: el presente, género/concordancia y ser/estar.</span></p>
    <div class="card" id="colorsent"></div>
    <div class="card" id="irconj"></div>
    <h3 class="subh">🧩 El presente — ordena y practica</h3>
    <div class="card ex" id="gx_build"></div>
    <div class="card ex" id="gx_iraq"></div>
    <h3 class="subh">⚖️ Género y concordancia — el/la · -o/-a</h3>
    <div class="game" id="g_cantidad"></div>
    <div class="card ex" id="gx_conc"></div>
    <div class="card ex" id="gx_cantq"></div>
    <h3 class="subh">🔀 Ser o estar — soy / estoy</h3>
    <div class="game" id="g_pron"></div>
    <div class="card ex" id="gx_pronq"></div>
    <h3 class="subh">🎯 Repaso mixto — rellena con feedback</h3>
    <div class="card ex" id="gx_mix"></div>
  </section>

  <section class="panel" data-p="lectura">
    <h2 class="sec">Lectura · dos perfiles</h2>
    <p class="lead">Lees de <b>twee perfielen</b> van de cast, <b>luister</b> ze (🔊 TTS) en <b>controleer je begrip</b>. Daarna reageer je: met wie heb je meer gemeen? <span class="gloss">Keten: lezen → schrijven/spreken.</span></p>
    <div id="lecturawrap"></div>
    <h3 class="subh">🔢 Ordena la presentación</h3>
    <div class="card ex" id="lx_order"></div>
    <h3 class="subh">🔎 Comprensión · escanea y escoge</h3>
    <div class="card ex" id="lx_scan"></div>
  </section>

  <section class="panel" data-p="juegos">
    <h2 class="sec">Ejercicios · 13 juegos, jij kiest</h2>
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
    <h2 class="sec">Cultura · el mundo hispano</h2>
    <p class="lead">El español es la lengua de <b>21 países</b> y de más de <b>500 millones</b> de personas, en cuatro continentes. <span class="gloss">Spaans: 21 landen, 500+ miljoen sprekers, vier continenten.</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🇪🇸 Europa</h3>
      <p><b>España</b> is het enige Spaanstalige land in Europa. Naast het <b>castellano</b> spreekt men er ook <b>catalán</b>, <b>gallego</b> en <b>euskera</b>. <span class="gloss">Madrid = hoofdstad, ~47 miljoen inwoners.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🌎 América</h3>
      <p>De meeste <b>hispanohablantes</b> wonen in <b>Latijns-Amerika</b>: van 🇲🇽 México tot 🇦🇷 Argentina. <b>México</b> is het grootste Spaanstalige land (~130 miljoen). <span class="gloss">19 landen, veel accenten — in Argentina zegt men <b>vos</b> (voseo).</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🌍 ¿Sabías que…?</h3>
      <p>Ook in <b>Guinea Ecuatorial</b> (Afrika) is Spaans officieel. En in de <b>VS</b> wonen ~40 miljoen hispanohablantes — meer dan in Spanje! <span class="gloss">Español = 2ª lengua materna del mundo.</span></p></div>
    <h3 class="subh">📍 El mundo hispano · el mapa</h3>
    <p class="lead">Hier begint <b>La Ruta</b> (U0). <b>Klik op een land</b> op de kaart voor info. Straks reizen we van España naar América.</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    <h2 class="sec">Extra · bronnen</h2>
    <p class="lead">Externe uitleg &amp; oefeningen (de leerkracht vult de links aan).</p>
    <div class="card"><p>🎬 <b>profedeele</b> (YouTube — ir a + infinitivo / la comida) — <span class="gloss">link volgt.</span></p>
    <p>🧩 <b>arche-ele</b> (Genially — la comida / el restaurante) — <span class="gloss">link volgt.</span></p>
    <p>📄 In het boek (PDF) verwijzen de QR-codes naar déze pagina, op het juiste ankerpunt.</p></div>
  </section>

  <div class="foot">Español en la práctica · C6+ · Unidad 0 «¡Volvemos!» — página digital. Uitbreiding op de PDF · huisstijl morado · print ↔ PowerPoint ↔ web.</div>
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

// ---- GRAMMAR-VIZ 1: kleurgecodeerde presente-zin ----
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">El presente — ¿quién hace qué?</h3>'+
'<div class="csent">'+
'<span style="background:#dbeafe;color:#1e40af">(Yo)<span class="tip">onderwerp — de persoon</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">hablo<span class="tip">werkwoord · presente (hablar habl-o)</span></span> '+
'<span style="background:#dcfce7;color:#166534">español<span class="tip">voorwerp/inhoud</span></span> '+
'<span style="background:#ccfbf1;color:#0f766e">en clase<span class="tip">plaats</span></span>.</div>'+
'<div class="legend"><span><i style="background:#93c5fd"></i>onderwerp</span><span><i style="background:#fdba74"></i>werkwoord</span><span><i style="background:#86efac"></i>voorwerp</span><span><i style="background:#5eead4"></i>plaats</span></div>'+
'<p class="gloss" style="margin-top:8px">🟠 Het werkwoord verandert met de persoon: yo habl<b>o</b>, tú habl<b>as</b>, él habl<b>a</b>. · '+(TTS?'<button class="spk-btn" onclick="speak(\'Yo hablo español en clase\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: ser (presente) — klik om te onthullen ----
(function(){const el=document.getElementById('irconj');
 const R=[['yo','soy'],['tú','eres'],['él/ella','es'],['nosotros','somos'],['vosotros','sois'],['ellos','son']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">El verbo «ser» — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">Denk eerst zelf de vorm; klik dan de kaart. ser = wie/wat je bent.</p><div class="conjgrid" id="icg"></div>';
 const g=el.querySelector('#icg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v;if(TTS)speak(p+' '+v);};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: ¿el o la? (género) ----
function gameCantidad(){const el=document.getElementById('g_cantidad');
 const items=[['libro','el','el libro (m)'],['casa','la','la casa (f)'],['problema','el','el problema (m! -ma)'],['mano','la','la mano (f! -o)'],['día','el','el día (m! -a)'],['ciudad','la','la ciudad (f)'],['mapa','el','el mapa (m! -a)'],['lengua','la','la lengua (f)'],['foto','la','la foto (f! -o)'],['idioma','el','el idioma (m! -ma)'],['familia','la','la familia (f)'],['país','el','el país (m)']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿el o la?</h3><p class="desc">Kies het juiste lidwoord (let op de valstrikken -ma/-a/-o!).</p>'+scoreBar('sbC')+'<div id="cW" style="font-size:24px;font-family:var(--disp);text-align:center;margin:8px 0">___ <b></b></div><div class="chips" id="cC" style="justify-content:center"></div><div class="fb" id="cFb"></div>';
 const sb=el.querySelector('#sbC');const cont=el.querySelector('#cC');
 ['el','la'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#cW b').textContent=el.cur[0];el.querySelector('#cFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#cFb'),ok,(ok?'¡Sí! ':'Nee: ')+el.cur[2]+'.');setTimeout(next,950);}
 next();}
// ---- GRAMMAR-VIZ 4: ¿soy o estoy? (ser/estar) ----
function gamePron(){const el=document.getElementById('g_pron');
 const items=[['___ de Bélgica.','soy','herkomst → ser'],['___ en clase.','estoy','plaats → estar'],['___ estudiante.','soy','identiteit → ser'],['Hoy ___ contento.','estoy','gevoel → estar'],['___ belga.','soy','nationaliteit → ser'],['___ muy bien.','estoy','toestand → estar'],['___ simpático.','soy','karakter → ser'],['___ en casa.','estoy','plaats → estar'],['___ profesor.','soy','beroep → ser'],['___ cansado hoy.','estoy','gevoel → estar']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿soy o estoy?</h3><p class="desc">soy (wie/wat je bent) of estoy (waar/hoe je bent)?</p>'+scoreBar('sbP')+'<div id="pQ" style="font-size:20px;font-family:var(--disp);text-align:center;margin:10px 0"></div><div class="chips" id="pC" style="justify-content:center"></div><div class="fb" id="pFb"></div>';
 const sb=el.querySelector('#sbP');const cont=el.querySelector('#pC');
 ['soy','estoy'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#pQ').textContent=el.cur[0];el.querySelector('#pFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#pFb'),ok,(ok?'¡Sí! ':'Nee: ')+el.cur[1]+' ('+el.cur[2]+').');setTimeout(next,1000);}
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
 const INFO={
  MEX:{fl:'🇲🇽',n:'México',cap:'Ciudad de México',f:'Onze parada 5: CDMX. Mercados, tacos, guacamole y mucha comida. Meeste Spaanstaligen ter wereld (~130 mln).',nl:'Parada 5 · CDMX (Diego).',star:1},
  ESP:{fl:'🇪🇸',n:'España',cap:'Madrid',f:'Paradas anteriores: Madrid, Sevilla, Barcelona, València. La paella, las tapas.',nl:'Paradas U1–U4.',star:1},
  COL:{fl:'🇨🇴',n:'Colombia',cap:'Bogotá',f:'Parada: Cartagena. La arepa es típica.',nl:'Parada van Valen (U7).',star:1},
  PER:{fl:'🇵🇪',n:'Perú',cap:'Lima',f:'Parada: Cusco. El ceviche es típico.',nl:'Parada van Nina (U8).',star:1},
  GTM:{fl:'🇬🇹',n:'Guatemala',cap:'Ciudad de Guatemala',f:'Rijke Maya-erfenis.',nl:''},HND:{fl:'🇭🇳',n:'Honduras',cap:'Tegucigalpa',f:'Hart van Centraal-Amerika.',nl:''},
  SLV:{fl:'🇸🇻',n:'El Salvador',cap:'San Salvador',f:'Kleinste land van Centraal-Amerika.',nl:''},NIC:{fl:'🇳🇮',n:'Nicaragua',cap:'Managua',f:'Land van meren en vulkanen.',nl:''},
  CRI:{fl:'🇨🇷',n:'Costa Rica',cap:'San José',f:'«¡Pura vida!» — geen leger.',nl:''},PAN:{fl:'🇵🇦',n:'Panamá',cap:'Panamá',f:'Het kanaal verbindt twee oceanen.',nl:''},
  CUB:{fl:'🇨🇺',n:'Cuba',cap:'La Habana',f:'Bakermat van son en salsa.',nl:''},DOM:{fl:'🇩🇴',n:'República Dominicana',cap:'Santo Domingo',f:'Oudste stad van Amerika.',nl:''},
  PRI:{fl:'🇵🇷',n:'Puerto Rico',cap:'San Juan',f:'Bad Bunny y el reguetón.',nl:''},VEN:{fl:'🇻🇪',n:'Venezuela',cap:'Caracas',f:'Salto Ángel: hoogste waterval ter wereld.',nl:''},
  ECU:{fl:'🇪🇨',n:'Ecuador',cap:'Quito',f:'«La mitad del mundo»: op de evenaar.',nl:''},BOL:{fl:'🇧🇴',n:'Bolivia',cap:'Sucre / La Paz',f:'Salar de Uyuni: grootste zoutvlakte.',nl:''},
  PRY:{fl:'🇵🇾',n:'Paraguay',cap:'Asunción',f:'Tweetalig: español én guaraní.',nl:''},URY:{fl:'🇺🇾',n:'Uruguay',cap:'Montevideo',f:'Klein land tussen twee reuzen.',nl:''},
  ARG:{fl:'🇦🇷',n:'Argentina',cap:'Buenos Aires',f:'Las empanadas; vanaf C6 gastheer Mateo (voseo).',nl:''},CHL:{fl:'🇨🇱',n:'Chile',cap:'Santiago',f:'Het langste, smalste land ter wereld.',nl:''},
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

// ---------- LECTURA: dos perfiles + TTS + begrip ----------
function renderLectura(){const el=document.getElementById('lecturawrap');if(!el)return;
 const P=[{n:'Diego 🇲🇽',raw:'¡Hola! Me llamo Diego y soy de la Ciudad de México. Tengo dieciséis años. Vivo con mi madre y mi hermana. Me gusta el fútbol. En clase soy alegre y un poco hablador. Hablo español y estudio neerlandés.',
    html:'¡Hola! Me <span class="ev">llamo</span> Diego y <span class="ev">soy</span> de la Ciudad de México. <span class="ev">Tengo</span> dieciséis años. Vivo con mi madre y mi hermana. Me gusta el fútbol. En clase soy <span class="ev">alegre</span> y un poco hablador. Hablo español y estudio neerlandés.'},
   {n:'Nina 🇵🇪',raw:'Buenos días. Soy Nina, peruana, de Cusco. Tengo dieciséis años y tengo un hermano pequeño. Soy tranquila y trabajadora. Hablo español y un poco de quechua, la lengua de los Andes. Estoy muy contenta.',
    html:'Buenos días. <span class="ev">Soy</span> Nina, <span class="ev">peruana</span>, de Cusco. Tengo dieciséis años y tengo un hermano pequeño. Soy <span class="ev">tranquila</span> y trabajadora. Hablo español y un poco de <span class="ev">quechua</span>, la lengua de los Andes. Estoy muy contenta.'}];
 el.innerHTML='<div class="perfiles">'+P.map((m,i)=>'<div class="perfil"><h4>👤 '+m.n+' '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lm'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div class="txt" id="lm'+i+'" data-raw="'+m.raw.replace(/"/g,'&quot;')+'">'+m.html+'</div></div>').join('')+'</div>';
 const items=[['Diego tiene una hermana.',true,'«mi madre y mi hermana»'],['Nina habla tres lenguas.',false,'habla español y un poco de quechua (dos)'],['Los dos tienen dieciséis años.',true,'«Tengo dieciséis años» (los dos)'],['Diego es de Perú.',false,'Diego es de México'],['Nina es tranquila y trabajadora.',true,'«Soy tranquila y trabajadora»'],['Diego estudia neerlandés.',true,'«estudio neerlandés»'],['Nina vive en Cusco.',true,'«de Cusco» (Perú)'],['Diego es tímido en clase.',false,'es alegre y un poco hablador']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — con evidencia</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">¿Y tú? Reacciona</h3><p class="gloss" style="margin:0 0 8px">¿Con quién tienes más en común, con Diego o con Nina? Escribe 2–3 frases con <b>porque</b>. Grábalo en <b>Hablar 🎙️</b>.</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="Tengo más en común con… porque…"></textarea>';
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
 makeRecorder('rec_repite',{title:'Escucha y repite: saludos y presentación',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'¡Hola! Me llamo Diego.',cue:'presentarse',tip:'Duidelijk? Probeer nog eens zonder te lezen.'},{text:'Soy de Bélgica y tengo dieciséis años.',cue:'origen + edad'},{text:'Vivo en Gante y hablo neerlandés.',cue:'dónde + lengua'},{text:'Encantado, ¿cómo te llamas?',cue:'cortesía'},{text:'Buenos días, ¿qué tal?',cue:'saludo'},{text:'¡Hasta luego!',cue:'despedida'}]});
 makeRecorder('rec_pedido',{title:'Mensaje de voz: preséntate',desc:'Neem één bericht op (20–30 s): nombre, edad, de dónde eres, dónde vives y una lengua.',items:[
   {text:'Preséntate: nombre, edad, origen, dónde vives y una lengua.',cue:'tu presentación',tip:'5 gegevens gezegd? Neem opnieuw op.'}]});
 makeRecorder('rec_plato',{title:'Describe a un compañero/a',desc:'Beschrijf een klasgenoot: ¿cómo es? (carácter y físico).',items:[
   {text:'Mi compañero/a se llama ___ . Es ___ y ___ . Tiene ___ .',cue:'tu versión',tip:'2 karakter + 1 fysiek? Herneem.'}]});
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
 // GRAMÁTICA
 buildOrder('gx_build',{title:'Ordena la presentación',desc:'Tik de zinnen in de logische volgorde.',rounds:[
   {sub:'saludar → nombre → origen → edad',items:[{label:'¡Hola! ¿Qué tal?',key:1},{label:'Me llamo Nina.',key:2},{label:'Soy de Perú.',key:3},{label:'Tengo dieciséis años.',key:4}]},
   {sub:'nombre → dónde vives → lengua → y tú',items:[{label:'Me llamo Diego.',key:1},{label:'Vivo en México.',key:2},{label:'Hablo español.',key:3},{label:'¿Y tú?',key:4}]},
   {sub:'pregunta → respuesta → repregunta → mucho gusto',items:[{label:'¿Cómo te llamas?',key:1},{label:'Me llamo Lucía, ¿y tú?',key:2},{label:'Yo soy Mateo.',key:3},{label:'¡Mucho gusto!',key:4}]},
   {sub:'origen → nacionalidad → lengua → carácter',items:[{label:'Soy de Cartagena.',key:1},{label:'Soy colombiana.',key:2},{label:'Hablo español.',key:3},{label:'Soy muy alegre.',key:4}]},
   {sub:'formal: saludar → nombre → usted → encantada',items:[{label:'Buenos días, señora.',key:1},{label:'Me llamo Ana.',key:2},{label:'¿Cómo se llama usted?',key:3},{label:'Encantada.',key:4}]}]});
 buildChoice('gx_iraq',{title:'Mini-quiz: el presente',desc:'Kies de juiste vorm in het presente.',per:6,pool:[
   {q:'(Yo) ___ de Bélgica.',opts:['soy','eres','es'],ans:'soy',why:'yo → soy'},
   {q:'¿(Tú) ___ en Gante?',opts:['vives','vivo','vive'],ans:'vives',why:'tú → vives'},
   {q:'Nina ___ dieciséis años.',opts:['tiene','tienes','tengo'],ans:'tiene',why:'ella → tiene'},
   {q:'(Nosotros) ___ español.',opts:['hablamos','habláis','hablan'],ans:'hablamos',why:'nosotros → hablamos'},
   {q:'Diego ___ al mercado.',opts:['va','vas','voy'],ans:'va',why:'él → va'},
   {q:'(Yo) ___ muy bien.',opts:['estoy','está','estás'],ans:'estoy',why:'yo → estoy'},
   {q:'¿(Vosotros) ___ los deberes?',opts:['hacéis','hacen','hago'],ans:'hacéis',why:'vosotros → hacéis'},
   {q:'(Ellos) ___ de México.',opts:['vienen','venís','viene'],ans:'vienen',why:'ellos → vienen'},
   {q:'Lucía ___ española.',opts:['es','eres','soy'],ans:'es',why:'ella → es'},
   {q:'(Yo) ___ dos hermanas.',opts:['tengo','tienes','tiene'],ans:'tengo',why:'yo → tengo'}]});
 buildMatch('gx_conc',{title:'Empareja: país ↔ nacionalidad',desc:'Koppel het land aan de nationaliteit.',per:6,pool:[
   {a:'España',b:'español/a'},{a:'México',b:'mexicano/a'},{a:'Colombia',b:'colombiano/a'},{a:'Perú',b:'peruano/a'},
   {a:'Argentina',b:'argentino/a'},{a:'Bélgica',b:'belga'},{a:'Chile',b:'chileno/a'},{a:'Cuba',b:'cubano/a'},
   {a:'Ecuador',b:'ecuatoriano/a'},{a:'Venezuela',b:'venezolano/a'}]});
 buildChoice('gx_cantq',{title:'Mini-quiz: ¿el o la?',desc:'Género: kies el (m) of la (v). Let op de valstrikken.',per:6,pool:[
   {q:'___ problema',opts:['el','la'],ans:'el',why:'-ma → masculino'},
   {q:'___ casa',opts:['la','el'],ans:'la',why:'la casa (f)'},
   {q:'___ día',opts:['el','la'],ans:'el',why:'el día (m! -a)'},
   {q:'___ mano',opts:['la','el'],ans:'la',why:'la mano (f! -o)'},
   {q:'___ mapa',opts:['el','la'],ans:'el',why:'el mapa (m! -a)'},
   {q:'___ ciudad',opts:['la','el'],ans:'la',why:'-dad → femenino'},
   {q:'___ idioma',opts:['el','la'],ans:'el',why:'-ma → masculino'},
   {q:'___ foto',opts:['la','el'],ans:'la',why:'la foto (f! -o)'},
   {q:'___ libro',opts:['el','la'],ans:'el',why:'el libro (m)'},
   {q:'___ nacionalidad',opts:['la','el'],ans:'la',why:'-dad → femenino'}]});
 buildChoice('gx_pronq',{title:'Mini-quiz: ¿soy o estoy?',desc:'ser (identiteit) of estar (plaats/gevoel)?',per:6,pool:[
   {q:'___ de Bélgica.',opts:['soy','estoy'],ans:'soy',why:'herkomst → ser'},
   {q:'___ en clase.',opts:['estoy','soy'],ans:'estoy',why:'plaats → estar'},
   {q:'___ estudiante.',opts:['soy','estoy'],ans:'soy',why:'identiteit → ser'},
   {q:'Hoy ___ contento.',opts:['estoy','soy'],ans:'estoy',why:'gevoel → estar'},
   {q:'___ belga.',opts:['soy','estoy'],ans:'soy',why:'nationaliteit → ser'},
   {q:'___ muy bien, gracias.',opts:['estoy','soy'],ans:'estoy',why:'toestand → estar'},
   {q:'___ simpático.',opts:['soy','estoy'],ans:'soy',why:'karakter → ser'},
   {q:'___ en casa.',opts:['estoy','soy'],ans:'estoy',why:'plaats → estar'},
   {q:'___ el hermano de Nina.',opts:['soy','estoy'],ans:'soy',why:'identiteit → ser'},
   {q:'___ cansado hoy.',opts:['estoy','soy'],ans:'estoy',why:'gevoel → estar'}]});
 buildChoice('gx_mix',{title:'Repaso mixto: rellena',desc:'Alles door elkaar: presente · género · ser/estar · concordancia.',per:8,pool:[
   {q:'(Nosotros) ___ amigos.',opts:['somos','sois','son'],ans:'somos',why:'nosotros → somos'},
   {q:'La chica es ___ .',opts:['simpática','simpático','simpáticas'],ans:'simpática',why:'la chica (f ev)'},
   {q:'___ problema es difícil.',opts:['El','La','Los'],ans:'El',why:'el problema (m)'},
   {q:'(Yo) ___ en clase.',opts:['estoy','soy','está'],ans:'estoy',why:'plaats → estar'},
   {q:'Diego ___ mexicano.',opts:['es','está','soy'],ans:'es',why:'nationaliteit → ser'},
   {q:'Los libros son ___ .',opts:['rojos','rojas','rojo'],ans:'rojos',why:'los libros (m pl)'},
   {q:'¿(Tú) ___ dieciséis años?',opts:['tienes','tiene','tengo'],ans:'tienes',why:'tú → tienes'},
   {q:'___ ciudad es bonita.',opts:['La','El','Los'],ans:'La',why:'la ciudad (f)'},
   {q:'(Ellos) ___ de Perú.',opts:['son','somos','sois'],ans:'son',why:'ellos → son'},
   {q:'Nina ___ peruana.',opts:['es','está','soy'],ans:'es',why:'nationaliteit → ser'},
   {q:'Las casas son ___ .',opts:['blancas','blancos','blanca'],ans:'blancas',why:'las casas (f pl)'},
   {q:'(Yo) ___ al instituto en bici.',opts:['voy','vas','va'],ans:'voy',why:'yo → voy'}]});
 // VOCABULARIO
 buildMatch('vx_match',{title:'Empareja: país ↔ bandera',desc:'Koppel het land aan de vlag.',per:6,pool:[
   {a:'España',b:'🇪🇸'},{a:'México',b:'🇲🇽'},{a:'Colombia',b:'🇨🇴'},{a:'Perú',b:'🇵🇪'},
   {a:'Argentina',b:'🇦🇷'},{a:'Bélgica',b:'🇧🇪'},{a:'Chile',b:'🇨🇱'},{a:'Cuba',b:'🇨🇺'},
   {a:'Venezuela',b:'🇻🇪'},{a:'Ecuador',b:'🇪🇨'},{a:'Uruguay',b:'🇺🇾'},{a:'Guatemala',b:'🇬🇹'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat in de zin past.',per:6,pool:[
   {q:'Buenos días, ¿cómo te ___?',opts:['llamas','vives','tienes'],ans:'llamas',why:'¿cómo te llamas?'},
   {q:'—¿De dónde eres? —___ de Bélgica.',opts:['Soy','Estoy','Tengo'],ans:'Soy',why:'herkomst → soy de'},
   {q:'Tengo dieciséis ___ .',opts:['años','año','añas'],ans:'años',why:'tengo … años'},
   {q:'Nina habla español y un poco de ___ .',opts:['quechua','Bélgica','Cusco'],ans:'quechua',why:'quechua = lengua'},
   {q:'Mi ___ es profesora.',opts:['madre','libro','ciudad'],ans:'madre',why:'la familia'},
   {q:'Perdón, no ___ .',opts:['entiendo','vivo','soy'],ans:'entiendo',why:'clastaal'},
   {q:'¿Puedes ___, por favor?',opts:['repetir','vivir','ser'],ans:'repetir',why:'¿puedes repetir?'},
   {q:'Lucía es de Sevilla; es ___ .',opts:['española','peruana','belga'],ans:'española',why:'España → española'},
   {q:'Yo ___ en Gante.',opts:['vivo','soy','tengo'],ans:'vivo',why:'vivir → vivo'},
   {q:'¡___! Hasta luego.',opts:['Adiós','Hola','Gracias'],ans:'Adiós',why:'despedida'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het juiste woord.',per:6,pool:[
   {q:'Groet in de ochtend:',opts:['buenos días','adiós','gracias'],ans:'buenos días',why:'ochtendgroet'},
   {q:'De taal van de Andes naast het Spaans:',opts:['el quechua','el neerlandés','el francés'],ans:'el quechua',why:'quechua'},
   {q:'Iemand die vrolijk is:',opts:['alegre','trabajador','moreno'],ans:'alegre',why:'alegre = vrolijk'},
   {q:'Je broer of zus:',opts:['hermano','padre','amigo'],ans:'hermano',why:'hermano = broer'},
   {q:'Land met hoofdstad Bogotá:',opts:['Colombia','España','Chile'],ans:'Colombia',why:'Bogotá → Colombia'},
   {q:'Wat je zegt als je iets niet snapt:',opts:['no entiendo','mucho gusto','de nada'],ans:'no entiendo',why:'clastaal'},
   {q:'Nationaliteit van iemand uit México:',opts:['mexicano','peruano','belga'],ans:'mexicano',why:'México → mexicano'},
   {q:'Het getal 100:',opts:['cien','veinte','cincuenta'],ans:'cien',why:'cien = 100'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['hola','buenos días','adiós','mesa'],odd:3,why:'mesa is geen groet/afscheid'},
   {words:['España','México','español','Perú'],odd:2,why:'español = nacionalidad, de rest = país'},
   {words:['soy','eres','es','tengo'],odd:3,why:'tengo = tener, de rest = ser'},
   {words:['alto','simpático','alegre','ciudad'],odd:3,why:'ciudad is geen adjectief'},
   {words:['padre','madre','hermano','amigo'],odd:3,why:'amigo is geen familielid'},
   {words:['español','francés','neerlandés','Bélgica'],odd:3,why:'Bélgica = país, de rest = lengua'},
   {words:['veinte','cincuenta','cien','casa'],odd:3,why:'casa is geen getal'},
   {words:['buenos días','buenas tardes','buenas noches','gracias'],odd:3,why:'gracias is geen begroeting'}]});
 // LECTURA
 buildOrder('lx_order',{title:'Ordena la presentación',desc:'Tik de zinnen in de juiste volgorde.',rounds:[
   {sub:'Diego se presenta',items:[{label:'¡Hola! Me llamo Diego.',key:1},{label:'Soy de la Ciudad de México.',key:2},{label:'Tengo dieciséis años.',key:3},{label:'Hablo español y estudio neerlandés.',key:4}]},
   {sub:'Nina se presenta',items:[{label:'Buenos días, soy Nina.',key:1},{label:'Soy peruana, de Cusco.',key:2},{label:'Soy tranquila y trabajadora.',key:3},{label:'Hablo español y quechua.',key:4}]},
   {sub:'los saludos del día',items:[{label:'Buenos días',key:1},{label:'Buenas tardes',key:2},{label:'Buenas noches',key:3},{label:'Adiós',key:4}]},
   {sub:'de menor a mayor (getallen)',items:[{label:'catorce',key:1},{label:'veinte',key:2},{label:'cincuenta',key:3},{label:'cien',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in de twee perfielen en kies.',per:6,pool:[
   {q:'¿De dónde es Diego?',opts:['México','Perú','Bélgica'],ans:'México',why:'«de la Ciudad de México»'},
   {q:'¿Cuántos años tiene Nina?',opts:['dieciséis','quince','catorce'],ans:'dieciséis',why:'«Tengo dieciséis años»'},
   {q:'¿Qué lengua habla Nina además del español?',opts:['quechua','neerlandés','francés'],ans:'quechua',why:'«un poco de quechua»'},
   {q:'¿Cómo es Diego en clase?',opts:['alegre','tímido','serio'],ans:'alegre',why:'«soy alegre»'},
   {q:'¿Quién tiene un hermano pequeño?',opts:['Nina','Diego','Lucía'],ans:'Nina',why:'«tengo un hermano pequeño»'},
   {q:'¿Qué estudia Diego?',opts:['neerlandés','quechua','francés'],ans:'neerlandés',why:'«estudio neerlandés»'},
   {q:'¿Cómo es Nina?',opts:['tranquila','habladora','nerviosa'],ans:'tranquila',why:'«Soy tranquila»'},
   {q:'¿De qué ciudad es Nina?',opts:['Cusco','Lima','Bogotá'],ans:'Cusco',why:'«de Cusco»'}]});
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='C6plus_U0_web_mijn_versie.html';a.click();};
})();
"""

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/C6plus_U0_web.html","w").write(html)
print("C6plus_U0_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
