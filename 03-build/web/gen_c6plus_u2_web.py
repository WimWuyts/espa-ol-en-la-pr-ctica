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
vocab = json.load(open(f"{ROOT}/01-cursussen/06-vervolg/U2/u2_vocab.json", encoding="utf-8"))
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
   ['casa-memoria', 'memoria de la casa', 'memory'],
   ['barrio-memoria', 'memoria del barrio', 'memory'],
   ['lugar-funcion', 'lugar ↔ función', 'match'],
   ['preposicion-dibujo', '¿dónde está el gato?', 'match']]],
 ['② Distinguir · gramática', [
   ['hay-estar', '¿hay o está(n)?', 'classify'],
   ['gerundio-tipo', '¿-ando o -iendo?', 'classify'],
   ['dentro-fuera', 'dentro o fuera de casa', 'classify']]],
 ['③ Producir con apoyo', [
   ['gerundio', 'completa: estar + gerundio', 'cloze'],
   ['lo-la', 'completa: lo/la/los/las', 'cloze'],
   ['lo-la-tetris', 'lo/la: puertas', 'platform'],
   ['direcciones-order', 'ordena la ruta', 'order'],
   ['senala', 'señala', 'point'],
   ['pronombre-tap', '¿qué sustituye el pronombre?', 'tap']]],
 ['④ Hablar · grábate 🎙️', [
   ['repite-casa', 'escucha y repite: mi casa', 'speak'],
   ['mensaje-barrio', 'mensaje de voz: mi barrio', 'speak'],
   ['describe-casa', 'describe tu casa', 'sim'],
   ['carrusel-donde', 'carrusel · ¿dónde está?', 'speak']]],
 ['⑤ Escribir · escríbelo tú ✍️', [
   ['escribe-palabra', 'NL → escribe la palabra', 'type'],
   ['completa-frase', 'completa la frase', 'type'],
   ['que-palabra', '¿qué palabra es?', 'type'],
   ['dictado', 'dictado', 'type'],
   ['escribe-frase', 'escribe una frase', 'type']]]]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-c6plus-u2-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-c6plus-u2-{s}.html")}

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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="habitaciones">habitaciones</option><option value="muebles">muebles</option><option value="casa">la vivienda</option><option value="preposiciones">preposiciones</option><option value="barrio">el barrio</option><option value="ciudad">la ciudad</option><option value="direcciones">direcciones</option><option value="movimiento">movimiento</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Más español en la práctica · C6+ U2 Aquí vivo</title>
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
    <div><h1>U2 · Aquí vivo</h1>
    <p>La página digital de la Unidad 2 (<b>aquí vivo</b>): flashcards, gramática visual e interactiva y <b>__NGAMES__ juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie. Thema's: la casa · hay/estar · gerundio · lo/la.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U2. Klik om te draaien; wissel ES↔NL; filter per groep; klik 🔊 om te horen. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
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
    <p class="lead">De <b>essentiële</b> grammatica van U2: <b>hay/estar + preposiciones</b>, <b>estar + gerundio</b> en de pronombres <b>lo/la/los/las</b>. Hier oefen je <b>maximaal</b> — elke oefening trekt uit een grote pool, dus «↻ otra serie» geeft telkens een nieuwe reeks. <span class="gloss">Eerst betekenis/patroon ontdekken, dan de regel.</span></p>
    <div class="card" id="colorsent"></div>
    <div class="card" id="irconj"></div>
    <h2 class="sec" style="margin-top:26px">📍 Hay/estar + preposiciones — máxima práctica</h2>
    <p class="lead">hay = onbepaald (un/dos) · está(n) = bepaald (el/la) · encima de, al lado de… <span class="gloss">Blijf herspelen tot het automatisch komt.</span></p>
    <div class="game" id="g_cantidad"></div>
    <div class="card ex" id="gx_cantq"></div>
    <div class="card ex" id="gx_reg"></div>
    <div class="card ex" id="gx_adj"></div>
    <h2 class="sec" style="margin-top:26px">🔄 Estar + gerundio — ¿qué está pasando?</h2>
    <p class="lead">estar + -ando/-iendo. Onregelmatig: leyendo, durmiendo, pidiendo. <span class="gloss">Enkel estar verandert; de gerundio blijft gelijk.</span></p>
    <div class="game" id="g_pron"></div>
    <div class="card ex" id="gx_pronq"></div>
    <div class="card ex" id="gx_ser"></div>
    <div class="card ex" id="gx_build"></div>
    <h2 class="sec" style="margin-top:26px">🔁 Los pronombres lo/la/los/las — máxima práctica</h2>
    <p class="lead">Vervang het voorwerp; het pronomen komt overeen (m/v·ev/mv) en staat vóór het werkwoord. <span class="gloss">¿La casa? La veo.</span></p>
    <div class="card ex" id="gx_iraq"></div>
    <div class="card ex" id="gx_subj"></div>
    <div class="card ex" id="gx_plural"></div>
    <div class="card ex" id="gx_nac"></div>
    <div class="card ex" id="gx_conc"></div>
    <div class="card ex" id="gx_conc2"></div>
    <h3 class="subh">🎯 Repaso mixto — hay/estar + gerundio + lo/la</h3>
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
    <h2 class="sec">Lectura completa · «Casa Azul» — dos reseñas</h2>
    <p class="lead">Twee echte beoordelingen met de volledige leesroute: <b>voorspellen → globaal → scannen → juist/fout met bewijs → betekenis uit de context → zelf schrijven</b>. <span class="gloss">Dezelfde tekst staat in je cursus, met schrijfruimte.</span></p>
    <div class="card ex" id="lec_c6p_u2"></div>
  </section>

  <section class="panel" data-p="escuchar">
    <h2 class="sec">Escuchar · Estoy perdido en Cartagena 🎧</h2>
    <p class="lead">Sam belt Valen op: hij is de weg kwijt in de oude stad. Eén fragment, zes stappen: eerst <b>weten waar je bent</b>, dan <b>globaal</b> luisteren, dan de <b>details</b>, dan <b>juist/fout met bewijs</b>. Het <b>transcript</b> gaat pas open als je klaar bent — anders lees je mee in plaats van te luisteren. <span class="gloss">Zolang er nog geen opname is, leest de computerstem het fragment voor.</span></p>
    <div class="card ex" id="esc_c6p_u2"></div>
  </section>
  <section class="panel" data-p="juegos">
    <h2 class="sec">Ejercicios · __NGAMES__ juegos, jij kiest</h2>
    <p class="lead">Geordend van <b>herkennen → onderscheiden → produceren met steun → analyseren &amp; communiceren → hablar</b>. Elk spel geeft directe, verklarende feedback en de steun bouwt af. <span class="gloss">Klik een spel; het opent in een venster en werkt ook offline.</span></p>
    <div id="motorlink"></div>
  </section>

  <section class="panel" data-p="retos">
    <h2 class="sec">Retos · tres desafíos 🎯</h2>
    <p class="lead">Drie retos met <b>één harde regel</b>: je beschrijft een videogesprek waarin je de kamer ziet maar de persoon niet (vijf keer <i>estar + gerundio</i>, en pas op het einde één hypothese), je plaatst zes geluiden in een gebouw van vijf verdiepingen, en je legt aan Valen uit waarom Vlaamse huizen smal zijn — <b>uitleggen, niet vertalen</b>. <span class="gloss">De zeven andere retos van deze unit staan in het boek en in de PowerPoint.</span></p>
    <div id="retos_c6p_u2"></div>
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
    <h2 class="sec">Cultura · la vivienda hispana</h2>
    <p class="lead">Parada 2 = <b>Cartagena</b> 🇨🇴. De <b>casa</b> hispana heeft haar eigen stijl: <b>patios</b>, <b>balcones</b> vol bloemen en de <b>plaza</b> als hart van de buurt. <span class="gloss">Elk land heeft zijn eigen woning-stijl.</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🏛️ El patio andaluz</h3>
      <p>In het zuiden van <b>España</b> (Sevilla, Córdoba) heeft het huis een <b>patio</b>: een binnentuin met planten en een fontein, koel in de zomer. <span class="gloss">Lucía kent ze goed.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🌺 Los balcones de Cartagena</h3>
      <p>In <b>Cartagena</b> (Colombia) zijn de koloniale huizen <b>kleurrijk</b>, met houten <b>balcones</b> vol bloemen. De <b>ciudad amurallada</b> is UNESCO-werelderfgoed. <span class="gloss">Valen woont er.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🟨 La plaza, corazón del barrio</h3>
      <p>Overal in de Spaanstalige wereld is de <b>plaza</b> het middelpunt: markt, terrasjes, ontmoeting. <span class="gloss">«Quedamos en la plaza».</span></p></div>
    <h3 class="subh">📍 La Ruta · el mapa (parada 2 = Cartagena, Colombia ★)</h3>
    <p class="lead">Onze halte is <b>Colombia</b> (Cartagena). <b>Klik op een land</b> op de kaart voor info — klik op Colombia (★) voor de parada.</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    __BRONNEN__
  </section>

  <div class="foot">Más español en la práctica · edición única · Unidad 2 «Aquí vivo» — página digital. Uitbreiding op de PDF · huisstijl morado · print ↔ PowerPoint ↔ web.</div>
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
""" + hub_drills.SPEAK_JS + hub_drills.RETOS_JS + r"""
const TTS=('speechSynthesis'in window);
if(TTS){speechSynthesis.getVoices();speechSynthesis.onvoiceschanged=()=>{};}
const PANELS=[['vocab','Vocabulario'],['gram','Gramática'],['lectura','Lectura'],['escuchar','Escuchar 🎧'],['juegos','Juegos'],['retos','Retos 🎯'],['hablar','Hablar 🎙️'],['cultura','Cultura'],['extra','Extra']];
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

// ---- GRAMMAR-VIZ 1: kleurgecodeerde plaats-zin ----
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">¿Dónde está? — hay/estar + preposición</h3>'+
'<div class="csent">'+
'<span style="background:#dbeafe;color:#1e40af">La lámpara<span class="tip">onderwerp — het ding</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">está<span class="tip">estar (bepaald: la lámpara)</span></span> '+
'<span style="background:#ccfbf1;color:#0f766e">encima de<span class="tip">preposición de lugar</span></span> '+
'<span style="background:#dcfce7;color:#166534">la mesa<span class="tip">referentiepunt</span></span>.</div>'+
'<div class="legend"><span><i style="background:#93c5fd"></i>ding</span><span><i style="background:#fdba74"></i>hay/estar</span><span><i style="background:#5eead4"></i>preposición</span><span><i style="background:#86efac"></i>punt</span></div>'+
'<p class="gloss" style="margin-top:8px">🟠 <b>hay</b> un/dos (onbepaald) · <b>está(n)</b> el/la (bepaald). · '+(TTS?'<button class="spk-btn" onclick="speak(\'La lámpara está encima de la mesa\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: estar + gerundio — klik om te onthullen ----
(function(){const el=document.getElementById('irconj');
 const R=[['yo','estoy comiendo'],['tú','estás comiendo'],['él/ella','está comiendo'],['nosotros','estamos comiendo'],['vosotros','estáis comiendo'],['ellos','están comiendo']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">estar + gerundio (comer) — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">Enkel estar verandert; de gerundio (comiendo) blijft gelijk.</p><div class="conjgrid" id="icg"></div>';
 const g=el.querySelector('#icg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v;if(TTS)speak(p+' '+v);};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: ¿hay o está(n)? ----
function gameCantidad(){const el=document.getElementById('g_cantidad');
 const items=[['En el salón ___ un sofá.','hay','un → hay'],['El sofá ___ delante de la tele.','está','el → está'],['En mi barrio ___ dos parques.','hay','dos → hay'],['Los parques ___ cerca.','están','los → están'],['¿___ una farmacia cerca?','hay','una → hay'],['La farmacia ___ en la esquina.','está','la → está'],['___ muchas tiendas aquí.','hay','muchas → hay'],['Las tiendas ___ abiertas.','están','las → están'],['En la cocina ___ una mesa.','hay','una → hay'],['La cama ___ al lado de la ventana.','está','la → está'],['¿Cuántos baños ___?','hay','cuántos → hay'],['El banco ___ lejos.','está','el → está']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿hay o está(n)?</h3><p class="desc">un/dos/mucho → hay · el/la/mi → está(n).</p>'+scoreBar('sbC')+'<div id="cW" style="font-size:18px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" id="cC" style="justify-content:center"></div><div class="fb" id="cFb"></div>';
 const sb=el.querySelector('#sbC');const cont=el.querySelector('#cC');
 ['hay','está','están'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#cW').textContent=el.cur[0];el.querySelector('#cFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#cFb'),ok,(ok?'¡Sí! ':'Nee: '+el.cur[1]+' ')+'('+el.cur[2]+').');setTimeout(next,1000);}
 next();}
// ---- GRAMMAR-VIZ 4: estar + gerundio (kies de vorm) ----
function gamePron(){const el=document.getElementById('g_pron');
 const items=[['comer','comiendo'],['estudiar','estudiando'],['leer','leyendo'],['dormir','durmiendo'],['escribir','escribiendo'],['cocinar','cocinando'],['pedir','pidiendo'],['ver','viendo'],['jugar','jugando'],['abrir','abriendo'],['beber','bebiendo'],['hacer','haciendo'],['decir','diciendo'],['pasear','paseando']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>El gerundio — ¿-ando o -iendo?</h3><p class="desc">Kies de juiste gerundio (let op de onregelmatige!).</p>'+scoreBar('sbP')+'<div id="pQ" style="font-size:20px;font-family:var(--disp);text-align:center;margin:10px 0"></div><div class="chips" id="pC" style="justify-content:center"></div><div class="fb" id="pFb"></div>';
 const sb=el.querySelector('#sbP');const cont=el.querySelector('#pC');
 function distract(v){var alt=v.replace(/iendo$/,'ando').replace(/ando$/,'iendo');var opts=[v,alt];var pool2=['leyendo','durmiendo','comiendo','haciendo','viviendo','pidiendo'];while(opts.length<3){var x=pool2[Math.floor(Math.random()*pool2.length)];if(opts.indexOf(x)<0)opts.push(x);}for(var i=opts.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=opts[i];opts[i]=opts[j];opts[j]=t;}return opts;}
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#pQ').textContent='estar + '+el.cur[0]+' → estoy …';cont.innerHTML='';distract(el.cur[1]).forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});el.querySelector('#pFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#pFb'),ok,(ok?'¡Sí! ':'Nee: ')+el.cur[0]+' → '+el.cur[1]+'.');setTimeout(next,1100);}
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
   const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "🏙️ Un lugar: las casas coloridas de Guanajuato", "star": 0, "nl": ""}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "🏙️ Un lugar: los pisos y los patios andaluces", "star": 1, "nl": "Parada anterior (U0–U1) · el mundo hispano · España (Lucía)"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "🏙️ Un lugar: los balcones floridos de Cartagena", "star": 1, "nl": "★ ¡Estás aquí! Parada U2 · Cartagena (Valen)"}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "🏙️ Un lugar: los barrios coloniales del Cusco", "star": 0, "nl": ""}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "🏙️ Un lugar: el barrio de La Boca, con casas de colores", "star": 0, "nl": ""}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "🏙️ Un lugar: los «ranchos» en las colinas de Caracas", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "🏙️ Un lugar: las casas de colores de Valparaíso", "star": 0, "nl": ""}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "🏙️ Un lugar: el centro histórico de Quito", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "🏙️ Un lugar: Antigua, ciudad colonial entre volcanes", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "🏙️ Un lugar: los edificios coloniales de La Habana Vieja", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "🏙️ Un lugar: las casas de adobe del Altiplano", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "🏙️ Un lugar: la Zona Colonial de Santo Domingo", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "🏙️ Un lugar: las casas de madera de las islas", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "🏙️ Un lugar: las casas con galería y patio", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "🏙️ Un lugar: Granada, ciudad colonial junto al lago", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "🏙️ Un lugar: los pueblos de la Ruta de las Flores", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "🏙️ Un lugar: las casas con jardín, «pura vida»", "star": 0, "nl": ""}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "🏙️ Un lugar: el Casco Viejo de la capital", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "🏙️ Un lugar: la Ciudad Vieja de Montevideo", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "🏙️ Un lugar: las casas de colores del Viejo San Juan", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "🏙️ Un lugar: Malabo y su arquitectura colonial", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "🏙️ Un lugar: barrios latinos como «Little Havana» (Miami)", "star": 0, "nl": ""}};
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
 const P=[{n:'Valen 🇨🇴',raw:'¡Hola! Vivo en un barrio del centro histórico de Cartagena, cerca del mar. Mi casa es antigua, con un balcón lleno de flores. Delante de mi casa hay una plaza pequeña con árboles. Al lado está la panadería. La farmacia está a la derecha y la parada del bus, a dos minutos. Mi barrio es tranquilo por el día y alegre por la noche.',
    html:'¡Hola! Vivo en un <span class="ev">barrio</span> del centro histórico de Cartagena, cerca del mar. Mi casa es antigua, con un <span class="ev">balcón</span> lleno de flores. Delante de mi casa <span class="ev">hay</span> una plaza pequeña. Al lado <span class="ev">está</span> la panadería. La farmacia está a la derecha y la parada, a dos minutos. Mi barrio es <span class="ev">tranquilo</span> por el día y alegre por la noche.'},
   {n:'Diego 🇲🇽',raw:'Yo vivo en un barrio grande de Ciudad de México. Es ruidoso pero me gusta: hay de todo. Detrás de mi edificio hay un mercado enorme. El metro está muy cerca y lo cojo cada día. No hay mucho silencio, pero hay vida en la calle a todas horas.',
    html:'Yo vivo en un barrio grande de Ciudad de México. Es <span class="ev">ruidoso</span> pero me gusta: hay de todo. Detrás de mi edificio <span class="ev">hay</span> un mercado enorme. El metro está muy cerca y <span class="ev">lo cojo</span> cada día. No hay mucho silencio, pero <span class="ev">hay</span> vida en la calle a todas horas.'}];
 el.innerHTML='<div class="perfiles">'+P.map((m,i)=>'<div class="perfil"><h4>👤 '+m.n+' '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lm'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div class="txt" id="lm'+i+'" data-raw="'+m.raw.replace(/"/g,'&quot;')+'">'+m.html+'</div></div>').join('')+'</div>';
 const items=[['Delante de la casa de Valen hay una plaza.',true,'«Delante de mi casa hay una plaza»'],['La farmacia de Valen está a la izquierda.',false,'«La farmacia está a la derecha»'],['El barrio de Valen es tranquilo por el día.',true,'«tranquilo por el día»'],['Diego vive en un barrio silencioso.',false,'«Es ruidoso», «No hay mucho silencio»'],['Detrás del edificio de Diego hay un mercado.',true,'«Detrás de mi edificio hay un mercado»'],['Diego coge el metro cada día.',true,'«lo cojo cada día»'],['La casa de Valen es moderna.',false,'«Mi casa es antigua»'],['La parada del bus está a dos minutos de Valen.',true,'«la parada, a dos minutos»']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — con evidencia</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">¿Y tu barrio? Reacciona</h3><p class="gloss" style="margin:0 0 8px">¿Tu barrio se parece más al de Valen o al de Diego? Escribe 2–3 frases con <b>hay/está + porque</b>. Grábalo en <b>Hablar 🎙️</b>.</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="Mi barrio se parece al de… porque hay…"></textarea>';
 el.appendChild(box);el.appendChild(resp);}

// ---------- INLINE RECORDER (MediaRecorder) ----------
""" + hub_drills.RECORDER_JS + r"""
function buildRecorders(){
 makeRecorder('rec_repite',{title:'Escucha y repite: mi casa y mi barrio',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'En mi casa hay tres habitaciones.',cue:'la casa',tip:'Duidelijk? Probeer nog eens zonder te lezen.'},{text:'La cama está al lado de la ventana.',cue:'preposición'},{text:'El sofá está delante de la tele.',cue:'preposición'},{text:'Ahora mismo estoy estudiando.',cue:'gerundio'},{text:'Para ir a la plaza, sigue recto y gira a la derecha.',cue:'direcciones'},{text:'¿El supermercado? Lo tengo cerca.',cue:'lo/la'}]});
 makeRecorder('rec_pedido',{title:'Mensaje de voz: mi habitación',desc:'Neem één bericht op (30–40 s): beschrijf je kamer — qué hay y dónde está (4 preposiciones).',items:[
   {text:'Describe tu habitación: qué hay y dónde está (usa hay/está + 4 preposiciones).',cue:'mi habitación',tip:'4 preposiciones + hay/está gezegd? Neem opnieuw op.'}]});
 makeRecorder('rec_plato',{title:'Da direcciones',desc:'Geef de weg van je huis naar een plek in de buurt.',items:[
   {text:'Da direcciones: sigue recto, gira a la derecha/izquierda, cruza, está a … minutos.',cue:'cómo llegar',tip:'3 stappen + afstand? Herneem.'}]});
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
 // ===== HAY/ESTAR + PREPOSICIONES =====
 buildChoice('gx_cantq',{title:'¿hay o está(n)?',desc:'un/dos/mucho → hay · el/la/mi → está(n).',per:8,pool:[
   {q:'En el salón ___ un sofá.',opts:['hay','está','están'],ans:'hay',why:'un → hay'},
   {q:'El sofá ___ delante de la tele.',opts:['está','hay','están'],ans:'está',why:'el sofá → está'},
   {q:'En mi barrio ___ dos parques.',opts:['hay','están','está'],ans:'hay',why:'dos → hay'},
   {q:'Los parques ___ cerca.',opts:['están','hay','está'],ans:'están',why:'los parques → están'},
   {q:'¿___ una farmacia cerca?',opts:['hay','está','están'],ans:'hay',why:'una → hay'},
   {q:'La farmacia ___ en la esquina.',opts:['está','hay','están'],ans:'está',why:'la farmacia → está'},
   {q:'___ muchas tiendas aquí.',opts:['hay','están','está'],ans:'hay',why:'muchas → hay'},
   {q:'Las tiendas ___ abiertas.',opts:['están','hay','está'],ans:'están',why:'las tiendas → están'},
   {q:'En la cocina ___ una mesa.',opts:['hay','está','están'],ans:'hay',why:'una → hay'},
   {q:'Mi casa ___ en el centro.',opts:['está','hay','están'],ans:'está',why:'mi casa → está'},
   {q:'Detrás de casa ___ un jardín.',opts:['hay','está','están'],ans:'hay',why:'un → hay'},
   {q:'La cama ___ al lado de la ventana.',opts:['está','hay','están'],ans:'está',why:'la cama → está'},
   {q:'¿Cuántos baños ___?',opts:['hay','está','están'],ans:'hay',why:'cuántos → hay'},
   {q:'El banco ___ lejos.',opts:['está','hay','están'],ans:'está',why:'el banco → está'}]});
 buildChoice('gx_reg',{title:'Completa la preposición de lugar',desc:'Kies de preposición die past (let op del/de la).',per:8,pool:[
   {q:'La lámpara está ___ la mesa (op).',opts:['encima de','debajo de','delante de'],ans:'encima de',why:'op = encima de'},
   {q:'El gato está ___ la cama (onder).',opts:['debajo de','encima de','al lado de'],ans:'debajo de',why:'onder = debajo de'},
   {q:'El baño está ___ la cocina (naast).',opts:['al lado de','delante de','detrás de'],ans:'al lado de',why:'naast = al lado de'},
   {q:'El sofá está ___ la tele (vóór).',opts:['delante de','detrás de','entre'],ans:'delante de',why:'vóór = delante de'},
   {q:'El jardín está ___ la casa (achter).',opts:['detrás de','delante de','encima de'],ans:'detrás de',why:'achter = detrás de'},
   {q:'La silla está ___ la mesa y la pared (tussen).',opts:['entre','al lado de','dentro de'],ans:'entre',why:'tussen = entre'},
   {q:'La ropa está ___ del armario (binnen).',opts:['dentro','fuera','encima'],ans:'dentro',why:'binnen = dentro de'},
   {q:'Vivo ___ del centro (dichtbij).',opts:['cerca','lejos','delante'],ans:'cerca',why:'dichtbij = cerca de'},
   {q:'La farmacia está ___ del banco (rechts).',opts:['a la derecha','a la izquierda','encima'],ans:'a la derecha',why:'rechts = a la derecha de'},
   {q:'al lado ___ banco',opts:['del','de el','de la'],ans:'del',why:'de + el = del'},
   {q:'al lado ___ plaza',opts:['de la','del','de el'],ans:'de la',why:'de + la = de la'},
   {q:'La estación está ___ mi casa (ver).',opts:['lejos de','cerca de','encima de'],ans:'lejos de',why:'ver = lejos de'}]});
 buildChoice('gx_adj',{title:'Hay/estar + preposición — mezclado',desc:'Alles door elkaar. Directe feedback.',per:8,pool:[
   {q:'En mi cuarto ___ una cama grande.',opts:['hay','está','están'],ans:'hay',why:'una → hay'},
   {q:'La cama ___ ___ la ventana.',opts:['está al lado de','hay al lado de','está en'],ans:'está al lado de',why:'la cama → está + prep'},
   {q:'En la plaza ___ árboles.',opts:['hay','están','está'],ans:'hay',why:'árboles (onbepaald) → hay'},
   {q:'Los libros ___ ___ la estantería.',opts:['están encima de','hay encima de','está encima de'],ans:'están encima de',why:'los libros → están'},
   {q:'de + el =',opts:['del','de el','dela'],ans:'del',why:'del'},
   {q:'El perro está ___ la cama.',opts:['debajo de','hay','dentro'],ans:'debajo de',why:'debajo de'},
   {q:'¿___ un supermercado cerca?',opts:['Hay','Está','Están'],ans:'Hay',why:'un → hay'},
   {q:'El baño está ___ la cocina.',opts:['al lado de','hay','encima'],ans:'al lado de',why:'al lado de'},
   {q:'En el barrio ___ dos farmacias.',opts:['hay','están','está'],ans:'hay',why:'dos → hay'},
   {q:'La farmacia grande ___ en la esquina.',opts:['está','hay','están'],ans:'está',why:'la farmacia → está'}]});
 // ===== ESTAR + GERUNDIO =====
 buildChoice('gx_pronq',{title:'Estar + gerundio — ¿qué está pasando?',desc:'Kies de juiste estar + gerundio-vorm.',per:8,pool:[
   {q:'Valen ___ en la cocina.',opts:['está cocinando','estoy cocinando','están cocinando'],ans:'está cocinando',why:'ella → está'},
   {q:'(Yo) ___ para el examen.',opts:['estoy estudiando','estás estudiando','está estudiando'],ans:'estoy estudiando',why:'yo → estoy'},
   {q:'Los niños ___ ahora.',opts:['están durmiendo','está durmiendo','estamos durmiendo'],ans:'están durmiendo',why:'ellos → están; dormir → durmiendo'},
   {q:'¿(Tú) ___ un libro?',opts:['estás leyendo','estoy leyendo','está leyendo'],ans:'estás leyendo',why:'tú → estás; leer → leyendo'},
   {q:'(Nosotros) ___ en la terraza.',opts:['estamos comiendo','estáis comiendo','están comiendo'],ans:'estamos comiendo',why:'nosotros → estamos'},
   {q:'Mamá ___ un mensaje.',opts:['está escribiendo','estás escribiendo','estoy escribiendo'],ans:'está escribiendo',why:'ella → está'},
   {q:'Diego ___ una pizza.',opts:['está pidiendo','está pediendo','está pidiando'],ans:'está pidiendo',why:'pedir → pidiendo'},
   {q:'(Yo) ___ la tele.',opts:['estoy viendo','estoy veiendo','estoy vidiendo'],ans:'estoy viendo',why:'ver → viendo'},
   {q:'¿(Vosotros) ___ música?',opts:['estáis escuchando','están escuchando','estamos escuchando'],ans:'estáis escuchando',why:'vosotros → estáis'},
   {q:'El bebé ___ .',opts:['está durmiendo','está dormiendo','está durmando'],ans:'está durmiendo',why:'dormir → durmiendo'},
   {q:'Los amigos ___ al fútbol.',opts:['están jugando','está jugando','estamos jugando'],ans:'están jugando',why:'ellos → están'},
   {q:'¿Qué ___ (tú) ahora?',opts:['estás haciendo','estás haziendo','estás hacando'],ans:'estás haciendo',why:'hacer → haciendo'}]});
 buildChoice('gx_ser',{title:'El gerundio — forma correcta',desc:'Kies de juiste gerundio (let op de onregelmatige).',per:7,pool:[
   {q:'comer →',opts:['comiendo','comando','comendo'],ans:'comiendo',why:'-er → -iendo'},
   {q:'estudiar →',opts:['estudiando','estudiendo','estudando'],ans:'estudiando',why:'-ar → -ando'},
   {q:'leer →',opts:['leyendo','leiendo','leendo'],ans:'leyendo',why:'i → y'},
   {q:'dormir →',opts:['durmiendo','dormiendo','durmando'],ans:'durmiendo',why:'o → u'},
   {q:'escribir →',opts:['escribiendo','escribando','escribendo'],ans:'escribiendo',why:'-ir → -iendo'},
   {q:'pedir →',opts:['pidiendo','pediendo','pidiando'],ans:'pidiendo',why:'e → i'},
   {q:'hacer →',opts:['haciendo','hacando','haciando'],ans:'haciendo',why:'-er → -iendo'},
   {q:'ver →',opts:['viendo','veiendo','vidiendo'],ans:'viendo',why:'ver → viendo'},
   {q:'decir →',opts:['diciendo','deciendo','dijiendo'],ans:'diciendo',why:'e → i'},
   {q:'jugar →',opts:['jugando','jugiendo','jugendo'],ans:'jugando',why:'-ar → -ando'}]});
 buildOrder('gx_build',{title:'Ordena la frase',desc:'Tik de woorden in de juiste volgorde.',rounds:[
   {sub:'preposición de lugar',items:[{label:'La lámpara',key:1},{label:'está',key:2},{label:'encima de',key:3},{label:'la mesa.',key:4}]},
   {sub:'hay + lugar',items:[{label:'En mi barrio',key:1},{label:'hay',key:2},{label:'un parque',key:3},{label:'muy grande.',key:4}]},
   {sub:'estar + gerundio',items:[{label:'Valen',key:1},{label:'está',key:2},{label:'cocinando',key:3},{label:'en la cocina.',key:4}]},
   {sub:'pronombre OD',items:[{label:'¿El sofá?',key:1},{label:'Lo',key:2},{label:'pongo',key:3},{label:'en el salón.',key:4}]},
   {sub:'cómo llegar',items:[{label:'Sigue recto',key:1},{label:'hasta el semáforo,',key:2},{label:'gira a la derecha',key:3},{label:'y cruza la calle.',key:4}]}]});
 // ===== LO/LA/LOS/LAS =====
 buildChoice('gx_iraq',{title:'¿lo, la, los o las?',desc:'Kies het OD-pronomen dat overeenkomt.',per:8,pool:[
   {q:'¿El sofá? ___ pongo aquí.',opts:['Lo','La','Los'],ans:'Lo',why:'el sofá (m ev) → lo'},
   {q:'¿La cama? ___ pongo aquí.',opts:['La','Lo','Las'],ans:'La',why:'la cama (v ev) → la'},
   {q:'¿Los platos? ___ lavo.',opts:['Los','Las','Lo'],ans:'Los',why:'los platos (m pl) → los'},
   {q:'¿Las sillas? ___ pongo en la cocina.',opts:['Las','Los','La'],ans:'Las',why:'las sillas (v pl) → las'},
   {q:'¿La tele? ___ veo por la noche.',opts:['La','Lo','Las'],ans:'La',why:'la tele → la'},
   {q:'¿El coche? ___ aparco en el garaje.',opts:['Lo','La','Los'],ans:'Lo',why:'el coche → lo'},
   {q:'¿Las ventanas? ___ limpio.',opts:['Las','Los','La'],ans:'Las',why:'las ventanas → las'},
   {q:'¿Los libros? ___ leo en el salón.',opts:['Los','Las','Lo'],ans:'Los',why:'los libros → los'},
   {q:'¿La plaza? ___ veo desde el balcón.',opts:['La','Lo','Las'],ans:'La',why:'la plaza → la'},
   {q:'¿El armario? ___ abro.',opts:['Lo','La','Los'],ans:'Lo',why:'el armario → lo'},
   {q:'¿El autobús? ___ cojo en la parada.',opts:['Lo','La','Los'],ans:'Lo',why:'el autobús → lo'},
   {q:'¿Las flores? ___ pongo en el balcón.',opts:['Las','Los','La'],ans:'Las',why:'las flores → las'}]});
 buildChoice('gx_subj',{title:'Responde con el pronombre',desc:'Kies het juiste korte antwoord met lo/la/los/las.',per:7,pool:[
   {q:'¿Compras el sofá? — Sí, ___ compro.',opts:['lo','la','los'],ans:'lo',why:'el sofá → lo'},
   {q:'¿Ves la plaza? — Sí, ___ veo.',opts:['la','lo','las'],ans:'la',why:'la plaza → la'},
   {q:'¿Pones los libros aquí? — Sí, ___ pongo.',opts:['los','las','lo'],ans:'los',why:'los libros → los'},
   {q:'¿Limpias las ventanas? — Sí, ___ limpio.',opts:['las','los','la'],ans:'las',why:'las ventanas → las'},
   {q:'¿Coges el autobús? — Sí, ___ cojo.',opts:['lo','la','los'],ans:'lo',why:'el autobús → lo'},
   {q:'¿Tienes la llave? — Sí, ___ tengo.',opts:['la','lo','las'],ans:'la',why:'la llave → la'},
   {q:'¿Compras las sillas? — Sí, ___ compro.',opts:['las','los','la'],ans:'las',why:'las sillas → las'},
   {q:'¿Ves el mercado? — Sí, ___ veo.',opts:['lo','la','los'],ans:'lo',why:'el mercado → lo'}]});
 buildChoice('gx_plural',{title:'La posición del pronombre',desc:'Kies de correcte plaats van lo/la.',per:6,pool:[
   {q:'Compro el sofá. →',opts:['Lo compro.','Compro lo.','Le compro.'],ans:'Lo compro.',why:'vóór het ww.'},
   {q:'Voy a limpiar la cocina. →',opts:['Voy a limpiarla.','Voy a la limpiar.','La voy limpiar.'],ans:'Voy a limpiarla.',why:'achter de infinitief (of: La voy a limpiar)'},
   {q:'Estoy leyendo el libro. →',opts:['Lo estoy leyendo.','Estoy lo leyendo.','Estoy leyendo lo.'],ans:'Lo estoy leyendo.',why:'vóór estar (of: estoy leyéndolo)'},
   {q:'Pongo las sillas aquí. →',opts:['Las pongo aquí.','Pongo las aquí.','Los pongo aquí.'],ans:'Las pongo aquí.',why:'las sillas → las, vóór het ww.'},
   {q:'¿La casa? →',opts:['La veo.','Veo la.','Lo veo.'],ans:'La veo.',why:'la casa → la, vóór het ww.'},
   {q:'Quiero comprar los muebles. →',opts:['Quiero comprarlos.','Quiero los comprar.','Los quiero comprarlos.'],ans:'Quiero comprarlos.',why:'achter de infinitief'}]});
 buildChoice('gx_nac',{title:'Aplica lo/la — traduce',desc:'Kies de correcte Spaanse zin met het OD-pronomen.',per:6,pool:[
   {q:'De bank? Ik zie hem. →',opts:['¿El banco? Lo veo.','¿El banco? La veo.','¿El banco? Le veo.'],ans:'¿El banco? Lo veo.',why:'el banco → lo'},
   {q:'De ramen? Ik maak ze schoon. →',opts:['¿Las ventanas? Las limpio.','¿Las ventanas? Los limpio.','¿Las ventanas? La limpio.'],ans:'¿Las ventanas? Las limpio.',why:'las ventanas → las'},
   {q:'De tafel? Ik zet ze hier. →',opts:['¿La mesa? La pongo aquí.','¿La mesa? Lo pongo aquí.','¿La mesa? Las pongo aquí.'],ans:'¿La mesa? La pongo aquí.',why:'la mesa → la'},
   {q:'De boeken? Ik lees ze. →',opts:['¿Los libros? Los leo.','¿Los libros? Las leo.','¿Los libros? Lo leo.'],ans:'¿Los libros? Los leo.',why:'los libros → los'},
   {q:'De bus? Ik neem hem. →',opts:['¿El autobús? Lo cojo.','¿El autobús? La cojo.','¿El autobús? Le cojo.'],ans:'¿El autobús? Lo cojo.',why:'el autobús → lo'},
   {q:'De bloemen? Ik zet ze op het balkon. →',opts:['¿Las flores? Las pongo en el balcón.','¿Las flores? Los pongo en el balcón.','¿Las flores? La pongo en el balcón.'],ans:'¿Las flores? Las pongo en el balcón.',why:'las flores → las'}]});
 buildMatch('gx_conc',{title:'Empareja: lugar ↔ función',desc:'Koppel de plek aan wat je er doet.',per:6,pool:[
   {a:'la farmacia',b:'comprar medicinas'},{a:'el supermercado',b:'comprar comida'},{a:'la parada',b:'coger el autobús'},
   {a:'el parque',b:'pasear'},{a:'el banco',b:'sacar dinero'},{a:'la estación',b:'coger el tren'},
   {a:'la cocina',b:'cocinar'},{a:'el dormitorio',b:'dormir'},{a:'el baño',b:'ducharse'},{a:'la plaza',b:'quedar con amigos'}]});
 buildMatch('gx_conc2',{title:'Empareja: mueble ↔ habitación',desc:'Koppel het meubel aan de kamer.',per:6,pool:[
   {a:'la cama',b:'el dormitorio'},{a:'el sofá',b:'el salón'},{a:'la nevera',b:'la cocina'},{a:'el espejo',b:'el baño'},
   {a:'la estantería',b:'el salón'},{a:'el armario',b:'el dormitorio'},{a:'la ducha',b:'el baño'},{a:'la mesa',b:'la cocina'}]});
 buildChoice('gx_mix',{title:'Repaso mixto — hay/estar + gerundio + lo/la',desc:'Alles door elkaar. Directe feedback.',per:8,pool:[
   {q:'En el salón ___ un sofá.',opts:['hay','está','están'],ans:'hay',why:'un → hay'},
   {q:'La cama ___ al lado de la ventana.',opts:['está','hay','están'],ans:'está',why:'la cama → está'},
   {q:'Valen ___ (cocinar) ahora.',opts:['está cocinando','cocina','cocinando'],ans:'está cocinando',why:'ahora → estar+gerundio'},
   {q:'¿La casa? ___ veo.',opts:['La','Lo','Las'],ans:'La',why:'la casa → la'},
   {q:'de + el =',opts:['del','de el','dela'],ans:'del',why:'del'},
   {q:'Los libros ___ encima de la mesa.',opts:['están','hay','está'],ans:'están',why:'los libros → están'},
   {q:'(Yo) ___ (leer) un libro.',opts:['estoy leyendo','leo','leyendo'],ans:'estoy leyendo',why:'ahora → estoy leyendo'},
   {q:'¿Los muebles? ___ compro.',opts:['Los','Las','Lo'],ans:'Los',why:'los muebles → los'},
   {q:'En mi barrio ___ dos parques.',opts:['hay','están','está'],ans:'hay',why:'dos → hay'},
   {q:'El baño está ___ la cocina (naast).',opts:['al lado de','encima de','hay'],ans:'al lado de',why:'naast = al lado de'},
   {q:'dormir → gerundio:',opts:['durmiendo','dormiendo','durmando'],ans:'durmiendo',why:'o → u'},
   {q:'¿Las sillas? ___ pongo aquí.',opts:['Las','Los','La'],ans:'Las',why:'las sillas → las'},
   {q:'La farmacia ___ en la esquina.',opts:['está','hay','están'],ans:'está',why:'la farmacia → está'},
   {q:'Para ir a la plaza, ___ recto.',opts:['sigue','gira','cruza'],ans:'sigue',why:'rechtdoor = sigue recto'}]});
 // ===== VOCABULARIO =====
 buildMatch('vx_match',{title:'Empareja: lugar ↔ emoji',desc:'Koppel de plek aan de emoji.',per:6,pool:[
   {a:'la plaza',b:'🟨'},{a:'el parque',b:'🌳'},{a:'la farmacia',b:'💊'},{a:'el supermercado',b:'🛒'},
   {a:'la parada',b:'🚌'},{a:'el banco',b:'💰'},{a:'la cama',b:'🛏️'},{a:'el sofá',b:'🛋️'},
   {a:'la cocina',b:'🍳'},{a:'el semáforo',b:'🚦'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat past.',per:6,pool:[
   {q:'La ropa está en el ___ .',opts:['armario','parque','semáforo'],ans:'armario',why:'la ropa → el armario'},
   {q:'Duermo en el ___ .',opts:['dormitorio','salón','banco'],ans:'dormitorio',why:'slaapkamer'},
   {q:'Compro pan en la ___ .',opts:['panadería','farmacia','estación'],ans:'panadería',why:'brood = panadería'},
   {q:'Cojo el autobús en la ___ .',opts:['parada','plaza','cocina'],ans:'parada',why:'halte'},
   {q:'Para cruzar, espera en el ___ .',opts:['semáforo','armario','espejo'],ans:'semáforo',why:'verkeerslicht'},
   {q:'Mi barrio es muy ___ , no hay ruido.',opts:['tranquilo','ruidoso','moderno'],ans:'tranquilo',why:'rustig'},
   {q:'La lámpara está ___ de la mesa.',opts:['encima','dentro','lejos'],ans:'encima',why:'encima de'},
   {q:'Para ir a la plaza, ___ a la derecha.',opts:['gira','hay','está'],ans:'gira',why:'sla af = gira'},
   {q:'En el centro ___ muchas tiendas.',opts:['hay','está','están'],ans:'hay',why:'muchas → hay'},
   {q:'El sofá está ___ de la tele.',opts:['delante','debajo','dentro'],ans:'delante',why:'vóór = delante de'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het woord.',per:6,pool:[
   {q:'De kamer waar je kookt:',opts:['la cocina','el salón','el baño'],ans:'la cocina',why:'keuken'},
   {q:'Waar je je auto zet:',opts:['el garaje','la terraza','el pasillo'],ans:'el garaje',why:'garage'},
   {q:'De open ruimte met terrasjes, hart van de buurt:',opts:['la plaza','la calle','la esquina'],ans:'la plaza',why:'plein'},
   {q:'«naast» in het Spaans:',opts:['al lado de','encima de','lejos de'],ans:'al lado de',why:'naast'},
   {q:'Er is / er zijn (onbepaald):',opts:['hay','está','es'],ans:'hay',why:'hay'},
   {q:'Waar je de bus neemt:',opts:['la parada','el banco','la nevera'],ans:'la parada',why:'halte'},
   {q:'«rustig» (geen lawaai):',opts:['tranquilo','ruidoso','antiguo'],ans:'tranquilo',why:'rustig'},
   {q:'Ga rechtdoor:',opts:['sigue recto','gira','cruza'],ans:'sigue recto',why:'rechtdoor'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['la cama','el sofá','el armario','la plaza'],odd:3,why:'la plaza is geen meubel'},
   {words:['la cocina','el dormitorio','el baño','el parque'],odd:3,why:'el parque is geen kamer'},
   {words:['encima de','debajo de','al lado de','tranquilo'],odd:3,why:'tranquilo is geen preposición'},
   {words:['la tienda','la farmacia','el supermercado','la nevera'],odd:3,why:'la nevera is geen plek in de buurt'},
   {words:['hay','está','están','sigue'],odd:3,why:'sigue is geen hay/estar'},
   {words:['sigue recto','gira','cruza','la ventana'],odd:3,why:'la ventana is geen richting'},
   {words:['comiendo','durmiendo','leyendo','armario'],odd:3,why:'armario is geen gerundio'},
   {words:['lo','la','los','de'],odd:3,why:'de is geen OD-pronomen'}]});
 // ===== LECTURA =====
 buildOrder('lx_order',{title:'Ordena',desc:'Tik in de juiste volgorde.',rounds:[
   {sub:'cómo llegar a la plaza',items:[{label:'Sal de casa.',key:1},{label:'Sigue recto.',key:2},{label:'Gira a la derecha.',key:3},{label:'La plaza está a la izquierda.',key:4}]},
   {sub:'describe la habitación',items:[{label:'En mi dormitorio',key:1},{label:'la cama está',key:2},{label:'al lado de',key:3},{label:'la ventana.',key:4}]},
   {sub:'el barrio de Valen',items:[{label:'Vivo en el centro histórico.',key:1},{label:'Delante hay una plaza.',key:2},{label:'Al lado está la panadería.',key:3},{label:'La parada, a dos minutos.',key:4}]},
   {sub:'estar + gerundio',items:[{label:'Ahora mismo',key:1},{label:'mamá',key:2},{label:'está',key:3},{label:'cocinando.',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in de twee perfielen (Valen y Diego) en kies.',per:6,pool:[
   {q:'¿Dónde vive Valen?',opts:['en Cartagena','en México','en Sevilla'],ans:'en Cartagena',why:'«centro histórico de Cartagena»'},
   {q:'¿Qué hay delante de la casa de Valen?',opts:['una plaza','un mercado','una estación'],ans:'una plaza',why:'«Delante de mi casa hay una plaza»'},
   {q:'¿Dónde está la panadería (Valen)?',opts:['al lado','lejos','detrás'],ans:'al lado',why:'«Al lado está la panadería»'},
   {q:'¿Cómo es el barrio de Diego?',opts:['ruidoso','tranquilo','pequeño'],ans:'ruidoso',why:'«Es ruidoso»'},
   {q:'¿Qué hay detrás del edificio de Diego?',opts:['un mercado','una plaza','una farmacia'],ans:'un mercado',why:'«hay un mercado enorme»'},
   {q:'¿Qué transporte coge Diego?',opts:['el metro','el autobús','el tren'],ans:'el metro',why:'«lo cojo cada día» (el metro)'},
   {q:'¿Cómo es la casa de Valen?',opts:['antigua','moderna','nueva'],ans:'antigua','why':'«Mi casa es antigua»'},
   {q:'¿A qué distancia está la parada (Valen)?',opts:['a dos minutos','a diez minutos','a una hora'],ans:'a dos minutos',why:'«la parada, a dos minutos»'}]});
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='C6plus_U2_web_mijn_versie.html';a.click();};
})();
"""

# Getypte woordenschat-drills (fase ophalen + produceren) in het paneel zelf.
JS += hub_type_sets.vocab_type_js(vocab)
JS += hub_type_gram.js('C6+', 2)
JS += hub_bloques.retos_js('retos_c6p_u2', 'C6+', 2)
JS += (hub_bloques.escucha_js("esc_c6p_u2", escucha_data.C6P_U2)
       + hub_bloques.lectura_js("lec_c6p_u2", lectura_data.C6P_U2))
HTML = HTML.replace("__GRAMSLOTS__", hub_type_gram.slots('C6+', 2))
HTML = HTML.replace("__NGAMES__", str(len(GAMES)))
HTML = HTML.replace("__BRONNEN__", extra_bronnen.html('C6+', 2))
HTML = HTML.replace("__TYPESLOTS__", hub_type_sets.SLOTS_HTML)

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/C6plus_U2_web.html","w").write(html)
print("C6plus_U2_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
