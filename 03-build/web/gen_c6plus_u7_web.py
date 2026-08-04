#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C6+ · U7 «¡Opina y cuídate!».
# Eén standalone bestand: fonts base64, de U4-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U7-vocab), visuele/interactieve grammatica (imperativo · opinar · conectores),
# klikbare kaart (mundo hispano, parada 7 = Costa Rica) + TTS + inline recorder + Lectura + editbar. Huisstijl morado.
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
vocab = json.load(open(f"{ROOT}/01-cursussen/06-vervolg/U7/u7_vocab.json", encoding="utf-8"))
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

# ---- de U7-motor-spellen: gegroepeerd (receptief -> productief -> hablar) + base64 ingebed ----
MOTOR = [
 ['① Reconocer · woordenschat', [
   ['salud-memoria', 'memoria de la salud', 'memory'],
   ['planeta-memoria', 'el planeta', 'memory'],
   ['verbo-imperativo', 'verbo ↔ imperativo', 'match'],
   ['cuerpo-dolor', 'el cuerpo y el dolor', 'match']]],
 ['② Distinguir · gramática', [
   ['salud-planeta', '¿salud o medio ambiente?', 'classify'],
   ['favor-contra', '¿a favor o en contra?', 'classify'],
   ['consejo-o-opinion', '¿consejo u opinión?', 'classify']]],
 ['③ Producir con apoyo', [
   ['imperativo', 'completa: el imperativo', 'cloze'],
   ['opinar', 'completa: opinar y conectar', 'cloze'],
   ['imper-tetris', 'imperativo: serpiente', 'snake'],
   ['argumento-order', 'ordena el argumento', 'order'],
   ['senala', 'señala', 'point'],
   ['imperativo-tilde', 'el imperativo + pronombre', 'tap']]],
 ['④ Hablar · grábate 🎙️', [
   ['repite-consejos', 'escucha y repite: consejos', 'speak'],
   ['mensaje-opinion', 'mensaje de voz: tu opinión', 'speak'],
   ['opina-cuidate', 'opina y aconseja', 'sim'],
   ['carrusel-consejo', 'carrusel · el consejo', 'speak']]],
 ['⑤ Escribir · escríbelo tú ✍️', [
   ['escribe-palabra', 'NL → escribe la palabra', 'type'],
   ['completa-frase', 'completa la frase', 'type'],
   ['que-palabra', '¿qué palabra es?', 'type'],
   ['dictado', 'dictado', 'type'],
   ['escribe-frase', 'escribe una frase', 'type']]]]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-c6plus-u7-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-c6plus-u7-{s}.html")}

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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="salud">salud</option><option value="consejos">consejos</option><option value="medioambiente">medio ambiente</option><option value="imperativo">imperativo</option><option value="opinar">opinar</option><option value="conectores">conectores</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Más español en la práctica · C6+ U7 ¡Opina y cuídate!</title>
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
    <div><h1>U7 · ¡Opina y cuídate!</h1>
    <p>La página digital de la Unidad 7 (<b>¡opina y cuídate!</b>): flashcards, gramática visual e interactiva y <b>__NGAMES__ juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie. Thema's: salud · medio ambiente · imperativo · opinar.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U7. Klik om te draaien; wissel ES↔NL; filter per groep; klik 🔊 om te horen. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
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
    <p class="lead">De <b>essentiële</b> grammatica van U7: de <b>imperativo</b> (cuida, come, haz + pronomen), het <b>opinar</b> (creo que… + indicativo) en de <b>conectoren</b> (porque, además, por eso). Hier oefen je <b>maximaal</b> — elke oefening trekt uit een grote pool, dus «↻ otra serie» geeft telkens een nieuwe reeks. <span class="gloss">Eerst betekenis/patroon ontdekken, dan de regel.</span></p>
    <div class="card" id="colorsent"></div>
    <div class="card" id="irconj"></div>
    <h2 class="sec" style="margin-top:26px">🗣️ El imperativo (tú) — máxima práctica</h2>
    <p class="lead">-ar → -a (cuida) · -er/-ir → -e (come, vive). 8 irregulares: ten · ven · pon · haz · di · sal · sé · ve. <span class="gloss">Voor advies en instructies.</span></p>
    <div class="game" id="g_cantidad"></div>
    <div class="card ex" id="gx_cantq"></div>
    <div class="card ex" id="gx_reg"></div>
    <div class="card ex" id="gx_adj"></div>
    <h2 class="sec" style="margin-top:26px">💬 Opinar y argumentar</h2>
    <p class="lead">creo que / pienso que / en mi opinión + indicativo (es, debemos). Reageren: (no) estoy de acuerdo. <span class="gloss">Géén subjuntivo: creo que ES.</span></p>
    <div class="game" id="g_pron"></div>
    <div class="card ex" id="gx_pronq"></div>
    <div class="card ex" id="gx_ser"></div>
    <div class="card ex" id="gx_build"></div>
    <h2 class="sec" style="margin-top:26px">🔗 Conectores — argumentar</h2>
    <p class="lead">porque (reden) · además (toevoeging) · por eso (gevolg) · sin embargo (tegenstelling). <span class="gloss">want/omdat = porque · dus = por eso.</span></p>
    <div class="card ex" id="gx_iraq"></div>
    <div class="card ex" id="gx_subj"></div>
    <div class="card ex" id="gx_plural"></div>
    <div class="card ex" id="gx_nac"></div>
    <div class="card ex" id="gx_conc"></div>
    <div class="card ex" id="gx_conc2"></div>
    <h3 class="subh">🎯 Repaso mixto — imperativo + opinar + conectores</h3>
    <div class="card ex" id="gx_mix"></div>
  __GRAMSLOTS__
  </section>

  <section class="panel" data-p="lectura">
    <h2 class="sec">Lectura · «Diez consejos para el planeta»</h2>
    <p class="lead">Lees de <b>advies-/opinietekst</b> uit de revista «Pura Vida», <b>luister</b> hem (🔊 TTS) en <b>controleer je begrip</b>. Daarna reageer je met je eigen mening. <span class="gloss">Keten: lezen → schrijven/spreken.</span></p>
    <div id="lecturawrap"></div>
    <h3 class="subh">🔢 Ordena el argumento</h3>
    <div class="card ex" id="lx_order"></div>
    <h3 class="subh">🔎 Comprensión · escanea y escoge</h3>
    <div class="card ex" id="lx_scan"></div>
    <h2 class="sec">Lectura completa · Carta al director</h2>
    <p class="lead">Een echte ingezonden brief met de volledige leesroute: <b>voorspellen → globaal → scannen → juist/fout met bewijs → betekenis uit de context → zelf schrijven</b>. <span class="gloss">Dezelfde tekst staat in je cursus, met schrijfruimte.</span></p>
    <div class="card ex" id="lec_c6p_u7"></div>
  </section>

  <section class="panel" data-p="escuchar">
    <h2 class="sec">Escuchar · En la consulta 🎧</h2>
    <p class="lead">Mateo slaapt slecht en krijgt vier adviezen — één weigert hij. Eén fragment, zes stappen: eerst <b>weten waar je bent</b>, dan <b>globaal</b> luisteren, dan de <b>details</b>, dan <b>juist/fout met bewijs</b>. Het <b>transcript</b> gaat pas open als je klaar bent — anders lees je mee in plaats van te luisteren. <span class="gloss">Zolang er nog geen opname is, leest de computerstem het fragment voor.</span></p>
    <div class="card ex" id="esc_c6p_u7"></div>
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
    <h2 class="sec">Cultura · Costa Rica y la «pura vida»</h2>
    <p class="lead">Parada 7 = <b>Costa Rica</b> 🇨🇷, la última. Un país <b>sin ejército</b>, líder en <b>ecoturismo</b> y <b>biodiversidad</b>, con un lema muy suyo: «<b>pura vida</b>». <span class="gloss">¡Fin de la ruta!</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🕊️ Sin ejército</h3>
      <p>In <b>1948</b> schafte Costa Rica zijn <b>leger</b> af. Het geld gaat naar <b>onderwijs</b> en <b>gezondheidszorg</b>. <span class="gloss">Un ejemplo de paz.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🌿 Ecoturismo y biodiversidad</h3>
      <p>Meer dan <b>25 %</b> van het land is beschermde natuur: regenwoud, vulkanen, stranden. Costa Rica huisvest ~<b>5 %</b> van alle soorten op aarde. <span class="gloss">Líder en energía renovable.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">🐒 ¡Pura vida!</h3>
      <p>«<b>Pura vida</b>» hoor je overal: als groet, bedankje of «alles oké». Het vat de optimistische levensstijl van de «ticos» samen. <span class="gloss">Una filosofía de vida.</span></p></div>
    <h3 class="subh">📍 La Ruta · el mapa (parada 7 = Costa Rica ★ · fin de la ruta)</h3>
    <p class="lead">Onze laatste halte is <b>Costa Rica</b>. <b>Klik op een land</b> op de kaart voor info — klik op Costa Rica (★) voor de parada.</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    __BRONNEN__
  </section>

  <div class="foot">Más español en la práctica · edición única · Unidad 7 «¡Opina y cuídate!» — página digital. Uitbreiding op de PDF · huisstijl morado · print ↔ PowerPoint ↔ web.</div>
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
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">El imperativo — dar un consejo</h3>'+
'<div class="csent">'+
'<span style="background:#fed7aa;color:#9a3412">Recicla<span class="tip">imperativo — bevel (tú)</span></span> '+
'<span style="background:#dcfce7;color:#166534">el papel<span class="tip">lijdend voorwerp</span></span> '+
'<span style="background:#e9d5ff;color:#6b21a8">porque<span class="tip">conector — reden</span></span> '+
'<span style="background:#dbeafe;color:#1e40af">es importante<span class="tip">argument (indicativo)</span></span>.</div>'+
'<div class="legend"><span><i style="background:#fdba74"></i>imperativo</span><span><i style="background:#86efac"></i>voorwerp</span><span><i style="background:#d8b4fe"></i>conector</span><span><i style="background:#93c5fd"></i>argument</span></div>'+
'<p class="gloss" style="margin-top:8px">🟠 De <b>imperativo</b> = advies/bevel. -ar → -a · -er/-ir → -e. · '+(TTS?'<button class="spk-btn" onclick="speak(\'Recicla el papel porque es importante\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: imperfecto — klik om te onthullen ----
(function(){const el=document.getElementById('irconj');
 const R=[['tener','ten'],['venir','ven'],['poner','pon'],['hacer','haz'],['decir','di'],['salir','sal'],['ser','sé'],['ir','ve']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">los 8 imperativos irregulares (tú) — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">Alleen deze 8 zijn onregelmatig; de rest is -a / -e.</p><div class="conjgrid" id="icg"></div>';
 const g=el.querySelector('#icg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v;if(TTS)speak(v);};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: imperfecto — ¿qué forma? ----
function gameCantidad(){const el=document.getElementById('g_cantidad');
 const items=[['___ (comer) más verdura.','Come','comer → come'],['___ (beber) agua.','Bebe','beber → bebe'],['___ (hacer) deporte.','Haz','hacer → haz ⭐'],['___ (ir) al médico.','Ve','ir → ve ⭐'],['___ (reciclar) el papel.','Recicla','reciclar → recicla'],['___ (ser) responsable.','Sé','ser → sé ⭐'],['___ (decir) la verdad.','Di','decir → di ⭐'],['___ (poner) la basura ahí.','Pon','poner → pon ⭐'],['___ (venir) conmigo.','Ven','venir → ven ⭐'],['___ (ahorrar) energía.','Ahorra','ahorrar → ahorra']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>el imperativo — ¿qué forma?</h3><p class="desc">-ar → -a · -er/-ir → -e · 8 irregulares (haz, ve, di…).</p>'+scoreBar('sbC')+'<div id="cW" style="font-size:17px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" id="cC" style="justify-content:center"></div><div class="fb" id="cFb"></div>';
 const sb=el.querySelector('#sbC');const cont=el.querySelector('#cC');
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#cW').textContent=el.cur[0];cont.innerHTML='';
   const opts=[el.cur[1]];const p2=['Come','Bebe','Haz','Ve','Recicla','Sé','Di','Pon','Ven','Ahorra'];while(opts.length<3){const x=p2[Math.floor(Math.random()*p2.length)];if(opts.indexOf(x)<0)opts.push(x);}
   for(let k=opts.length-1;k>0;k--){const j=Math.floor(Math.random()*(k+1));[opts[k],opts[j]]=[opts[j],opts[k]];}
   opts.forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});el.querySelector('#cFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#cFb'),ok,(ok?'¡Sí! ':'Nee: '+el.cur[1]+' ')+'('+el.cur[2]+').');setTimeout(next,1000);}
 next();}
// ---- GRAMMAR-VIZ 4: comparativos ----
function gamePron(){const el=document.getElementById('g_pron');
 const items=[['Reciclo ___ es importante. (reden)','porque','porque = reden'],['Es sano; ___, es barato. (toevoeging)','además','además = toevoeging'],['Contamina; ___ voy en bici. (gevolg)','por eso','por eso = gevolg'],['Como fruta ___ es sana. (reden)','porque','porque = reden'],['Hago deporte; ___, duermo mejor. (toevoeging)','además','además = toevoeging'],['El aire está sucio; ___ uso mascarilla. (gevolg)','por eso','por eso = gevolg'],['Ahorro agua ___ es un bien escaso. (reden)','porque','porque = reden'],['Es útil; ___, ahorra tiempo. (toevoeging)','además','además = toevoeging'],['Llueve; ___ llevo paraguas. (gevolg)','por eso','por eso = gevolg'],['Voy en bici ___ no contamina. (reden)','porque','porque = reden']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>Conectores — ¿porque, además o por eso?</h3><p class="desc">porque = reden · además = toevoeging · por eso = gevolg.</p>'+scoreBar('sbP')+'<div id="pQ" style="font-size:16px;font-family:var(--disp);text-align:center;margin:10px 0"></div><div class="chips" id="pC" style="justify-content:center"></div><div class="fb" id="pFb"></div>';
 const sb=el.querySelector('#sbP');const cont=el.querySelector('#pC');
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#pQ').textContent=el.cur[0];cont.innerHTML='';['porque','además','por eso'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});el.querySelector('#pFb').className='fb';}
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
        const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "🍽️ En la mesa: los tacos, el guacamole y el mole (base de maíz)", "star": 1, "nl": "Parada anterior (U3) · CDMX (Diego)"}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "🍽️ En la mesa: la paella, las tapas y la tortilla de patatas", "star": 1, "nl": "Parada anterior (U0–U1) · el mundo hispano · España (Lucía)"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "🍽️ En la mesa: la arepa, la bandeja paisa y el café", "star": 1, "nl": "Parada anterior (U2) · Cartagena (Valen)"}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "🍽️ En la mesa: el ceviche y el lomo saltado (cocina de fama mundial)", "star": 1, "nl": "Parada anterior (U6) · Cusco (Nina)"}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "🍽️ En la mesa: el asado, las empanadas y el dulce de leche", "star": 1, "nl": "Parada anterior (U5) · Buenos Aires (Mateo · voseo)"}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "🍽️ En la mesa: la arepa y el pabellón criollo", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "🍽️ En la mesa: las empanadas de pino y el pastel de choclo", "star": 1, "nl": "Parada anterior (U4) · Chile · el gran viaje (Patagonia, Atacama)"}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "🍽️ En la mesa: el ceviche de camarón y el encebollado", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "🍽️ En la mesa: el pepián y los tamales", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "🍽️ En la mesa: «moros y cristianos» (arroz y frijoles) y la ropa vieja", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "🍽️ En la mesa: la salteña y el silpancho", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "🍽️ En la mesa: «la bandera»: arroz, habichuelas y carne", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "🍽️ En la mesa: las baleadas (tortilla con frijoles)", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "🍽️ En la mesa: la sopa paraguaya y la chipa", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "🍽️ En la mesa: el gallo pinto y el nacatamal", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "🍽️ En la mesa: las pupusas, plato nacional", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "🍽️ En la mesa: el gallo pinto y el «casado»", "star": 1, "nl": "★ ¡Estás aquí! Parada U7 · Costa Rica · «pura vida» (salud y medio ambiente)"}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "🍽️ En la mesa: el sancocho y el arroz con pollo", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "🍽️ En la mesa: el asado y el chivito", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "🍽️ En la mesa: el mofongo y el arroz con gandules", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "🍽️ En la mesa: el pescado con yuca y plátano", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "🍽️ En la mesa: la comida tex-mex y los burritos (fusión latina)", "star": 0, "nl": ""}};
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
 const P=[{n:'Revista «Pura Vida» 🇨🇷',raw:'El planeta nos necesita. Creo que todos podemos ayudar con pequeños gestos. Recicla el papel, el vidrio y el plástico. Ahorra agua: cierra el grifo. Apaga las luces que no usas. Usa la bici o el transporte público, porque el coche contamina mucho. Come más verdura y menos carne. No tires basura al suelo. Planta un árbol si puedes. En mi opinión, los jóvenes son un ejemplo. Por eso, cuida el planeta hoy.',
    html:'El planeta nos necesita. <span class="ev">Creo que</span> todos podemos ayudar con pequeños gestos. <span class="ev">Recicla</span> el papel, el vidrio y el plástico. <span class="ev">Ahorra</span> agua: cierra el grifo. <span class="ev">Apaga</span> las luces que no usas. <span class="ev">Usa</span> la bici o el transporte público, <span class="ev">porque</span> el coche contamina mucho. <span class="ev">Come</span> más verdura y menos carne. <span class="ev">No tires</span> basura al suelo. <span class="ev">Planta</span> un árbol si puedes. <span class="ev">En mi opinión</span>, los jóvenes son un ejemplo. <span class="ev">Por eso</span>, cuida el planeta hoy.'},
   {n:'Un lector responde 💬',raw:'Estoy de acuerdo con la revista. Yo voy en bici porque es sano y no contamina. Además, ahorro dinero. Sin embargo, en mi pueblo no hay carril bici. Pienso que el ayuntamiento debe hacer más. Cuídate y cuida el planeta: ¡pura vida!',
    html:'<span class="ev">Estoy de acuerdo</span> con la revista. Yo voy en bici <span class="ev">porque</span> es sano y no contamina. <span class="ev">Además</span>, ahorro dinero. <span class="ev">Sin embargo</span>, en mi pueblo no hay carril bici. <span class="ev">Pienso que</span> el ayuntamiento debe hacer más. <span class="ev">Cuídate</span> y cuida el planeta: ¡pura vida!'}];
 el.innerHTML='<div class="perfiles">'+P.map((m,i)=>'<div class="perfil"><h4>👤 '+m.n+' '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lm'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div class="txt" id="lm'+i+'" data-raw="'+m.raw.replace(/"/g,'&quot;')+'">'+m.html+'</div></div>').join('')+'</div>';
 const items=[['El texto recomienda usar el coche.',false,'«Usa la bici o el transporte público»'],['La revista aconseja comer más verdura.',true,'«Come más verdura y menos carne»'],['Dice que hay que ahorrar agua cerrando el grifo.',true,'«Ahorra agua: cierra el grifo»'],['El lector no está de acuerdo con la revista.',false,'«Estoy de acuerdo con la revista»'],['El lector va en bici porque es sano y no contamina.',true,'«voy en bici porque es sano y no contamina»'],['En el pueblo del lector hay carril bici.',false,'«en mi pueblo no hay carril bici»'],['El lector piensa que el ayuntamiento debe hacer más.',true,'«Pienso que el ayuntamiento debe hacer más»'],['El texto termina con «pura vida».',true,'«¡pura vida!»']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — con evidencia</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">¿Y tú? Reacciona</h3><p class="gloss" style="margin:0 0 8px">¿Qué consejo te parece el más importante? Escribe 2–3 frases met een <b>mening</b> (creo que…) + un <b>conector</b> (porque/además). Grábalo en <b>Hablar 🎙️</b>.</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="Para mí, el consejo más importante es… porque…"></textarea>';
 el.appendChild(box);el.appendChild(resp);}

// ---------- INLINE RECORDER (MediaRecorder) ----------
""" + hub_drills.RECORDER_JS + r"""
function buildRecorders(){
 makeRecorder('rec_repite',{title:'Escucha y repite: consejos',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'Come sano y bebe mucha agua.',cue:'imperativo',tip:'Duidelijk? Probeer nog eens zonder te lezen.'},{text:'Haz deporte y duerme ocho horas.',cue:'imperativo'},{text:'Recicla el papel y ahorra energía.',cue:'imperativo'},{text:'Cuídate y relájate: ¡pura vida!',cue:'imperativo + pronombre'},{text:'Creo que debemos proteger el planeta.',cue:'opinar'},{text:'Reciclo porque es importante; además, ahorra dinero.',cue:'conectores'}]});
 makeRecorder('rec_pedido',{title:'Mensaje de voz: tus consejos',desc:'Neem één bericht op (30–40 s): geef 3 tips voor de gezondheid (gebruik de imperativo).',items:[
   {text:'Da 3 consejos de salud (usa el imperativo: come, bebe, haz…).',cue:'consejos de salud',tip:'3× de imperativo (tú)? Neem opnieuw op.'}]});
 makeRecorder('rec_plato',{title:'Mensaje de voz: tu opinión',desc:'Geef je mening over het milieu en argumenteer.',items:[
   {text:'Da tu opinión sobre el medio ambiente (creo que… porque… además…).',cue:'mi opinión',tip:'una opinión + un argumento (porque)? Herneem.'}]});
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
 // ===== IMPERATIVO =====
 buildChoice('gx_cantq',{title:'El imperativo — ¿qué forma?',desc:'-ar → -a · -er/-ir → -e · 8 irregulares.',per:8,pool:[
   {q:'___ (comer) más verdura.',opts:['Come','Comes','Comer'],ans:'Come',why:'comer → come'},
   {q:'___ (beber) dos litros de agua.',opts:['Bebe','Bebes','Beber'],ans:'Bebe',why:'beber → bebe'},
   {q:'___ (hacer) deporte.',opts:['Haz','Hace','Haces'],ans:'Haz',why:'hacer → haz ⭐'},
   {q:'___ (dormir) ocho horas.',opts:['Duerme','Dormes','Duermes'],ans:'Duerme',why:'dormir → duerme'},
   {q:'___ (reciclar) el plástico.',opts:['Recicla','Reciclas','Reciclar'],ans:'Recicla',why:'reciclar → recicla'},
   {q:'___ (ir) al médico.',opts:['Ve','Va','Ir'],ans:'Ve',why:'ir → ve ⭐'},
   {q:'___ (ser) responsable.',opts:['Sé','Ser','Eres'],ans:'Sé',why:'ser → sé ⭐'},
   {q:'___ (decir) la verdad.',opts:['Di','Dice','Dices'],ans:'Di',why:'decir → di ⭐'},
   {q:'___ (poner) la basura ahí.',opts:['Pon','Pone','Pones'],ans:'Pon',why:'poner → pon ⭐'},
   {q:'___ (venir) conmigo.',opts:['Ven','Viene','Vienes'],ans:'Ven',why:'venir → ven ⭐'},
   {q:'___ (ahorrar) energía.',opts:['Ahorra','Ahorras','Ahorrar'],ans:'Ahorra',why:'ahorrar → ahorra'},
   {q:'___ (proteger) los árboles.',opts:['Protege','Proteges','Proteger'],ans:'Protege',why:'proteger → protege'}]});
 buildChoice('gx_reg',{title:'Forma el imperativo (tú)',desc:'Kies de juiste vorm.',per:8,pool:[
   {q:'cuidar → tú',opts:['cuida','cuidas','cuidar'],ans:'cuida',why:'-a'},
   {q:'comer → tú',opts:['come','comes','comer'],ans:'come',why:'-e'},
   {q:'vivir → tú',opts:['vive','vives','vivir'],ans:'vive',why:'-e'},
   {q:'hacer → tú',opts:['haz','hace','haces'],ans:'haz',why:'irregular'},
   {q:'ir → tú',opts:['ve','va','vas'],ans:'ve',why:'irregular'},
   {q:'decir → tú',opts:['di','dice','dices'],ans:'di',why:'irregular'},
   {q:'tener → tú',opts:['ten','tiene','tienes'],ans:'ten',why:'irregular'},
   {q:'salir → tú',opts:['sal','sale','sales'],ans:'sal',why:'irregular'},
   {q:'ser → tú',opts:['sé','es','eres'],ans:'sé',why:'irregular'},
   {q:'poner → tú',opts:['pon','pone','pones'],ans:'pon',why:'irregular'}]});
 buildChoice('gx_adj',{title:'El imperativo + pronombre',desc:'Plak het pronomen vast (let op het accent).',per:8,pool:[
   {q:'cuida + te =',opts:['cuídate','cuidate','te cuida'],ans:'cuídate',why:'accent op í'},
   {q:'haz + lo =',opts:['hazlo','házlo','lo haz'],ans:'hazlo',why:'korte vorm, geen accent'},
   {q:'recicla + lo =',opts:['recíclalo','reciclalo','lo recicla'],ans:'recíclalo',why:'accent'},
   {q:'bebe + la =',opts:['bébela','bebela','la bebe'],ans:'bébela',why:'accent'},
   {q:'di + me =',opts:['dime','díme','me di'],ans:'dime',why:'korte vorm'},
   {q:'protege + lo =',opts:['protégelo','protegelo','lo protege'],ans:'protégelo',why:'accent'},
   {q:'di + me + lo =',opts:['dímelo','dimelo','me lo di'],ans:'dímelo',why:'accent'},
   {q:'pon + lo =',opts:['ponlo','pónlo','lo pon'],ans:'ponlo',why:'korte vorm'}]});
 // ===== OPINAR =====
 buildChoice('gx_pronq',{title:'Opinar — creo que + indicativo',desc:'Na «creo que» komt de indicativo (géén subjuntivo).',per:8,pool:[
   {q:'Creo que el deporte ___ importante.',opts:['es','sea','ser'],ans:'es',why:'indicativo: es'},
   {q:'Pienso que ___ reciclar más.',opts:['debemos','debamos','deber'],ans:'debemos',why:'indicativo: debemos'},
   {q:'En mi ___, hay mucha basura.',opts:['opinión','opino','opinar'],ans:'opinión',why:'en mi opinión'},
   {q:'Me ___ que tienes razón.',opts:['parece','pareces','parecer'],ans:'parece',why:'me parece que'},
   {q:'___ de acuerdo contigo.',opts:['Estoy','Soy','Tengo'],ans:'Estoy',why:'estar de acuerdo'},
   {q:'Tienes ___: hay que cuidarse.',opts:['razón','razones','derecho'],ans:'razón',why:'tener razón'},
   {q:'Creo que la comida rápida ___ mala.',opts:['es','sea','sería'],ans:'es',why:'indicativo: es'},
   {q:'Pienso ___ el aire está sucio.',opts:['que','de','por'],ans:'que',why:'pienso que'},
   {q:'No estoy de ___ con eso.',opts:['acuerdo','acuerdas','acordar'],ans:'acuerdo',why:'de acuerdo'},
   {q:'En mi opinión, el planeta ___ en peligro.',opts:['está','esté','estar'],ans:'está',why:'indicativo: está'}]});
 buildChoice('gx_ser',{title:'¿Consejo u opinión?',desc:'Advies (imperativo) of mening (creo que…)?',per:7,pool:[
   {q:'«Come más fruta» =',opts:['consejo (imperativo)','opinión (creo que)'],ans:'consejo (imperativo)',why:'bevel'},
   {q:'«Creo que es importante» =',opts:['opinión (creo que)','consejo (imperativo)'],ans:'opinión (creo que)',why:'mening'},
   {q:'«Recicla el papel» =',opts:['consejo (imperativo)','opinión (creo que)'],ans:'consejo (imperativo)',why:'bevel'},
   {q:'«En mi opinión, hay basura» =',opts:['opinión (creo que)','consejo (imperativo)'],ans:'opinión (creo que)',why:'mening'},
   {q:'«Haz deporte» =',opts:['consejo (imperativo)','opinión (creo que)'],ans:'consejo (imperativo)',why:'bevel'},
   {q:'«Pienso que el coche contamina» =',opts:['opinión (creo que)','consejo (imperativo)'],ans:'opinión (creo que)',why:'mening'},
   {q:'«Cuídate» =',opts:['consejo (imperativo)','opinión (creo que)'],ans:'consejo (imperativo)',why:'bevel'},
   {q:'«Me parece que tienes razón» =',opts:['opinión (creo que)','consejo (imperativo)'],ans:'opinión (creo que)',why:'mening'}]});
 buildOrder('gx_build',{title:'Ordena el argumento',desc:'Tik de woorden in de juiste volgorde.',rounds:[
   {sub:'consejo (imperativo)',items:[{label:'Recicla',key:1},{label:'el papel',key:2},{label:'y el vidrio',key:3},{label:'cada semana.',key:4}]},
   {sub:'opinión + reden',items:[{label:'Creo que',key:1},{label:'debemos reciclar',key:2},{label:'porque',key:3},{label:'protege el planeta.',key:4}]},
   {sub:'argumento completo',items:[{label:'La bici es genial.',key:1},{label:'No contamina.',key:2},{label:'Además, es sana.',key:3},{label:'Por eso la uso.',key:4}]},
   {sub:'reageren',items:[{label:'No estoy',key:1},{label:'de acuerdo',key:2},{label:'porque',key:3},{label:'el coche contamina.',key:4}]},
   {sub:'twee kanten',items:[{label:'Por un lado',key:1},{label:'es cómodo;',key:2},{label:'por otro lado,',key:3},{label:'contamina.',key:4}]}]});
 // ===== CONECTORES =====
 buildChoice('gx_iraq',{title:'¿porque, además o por eso?',desc:'reden · toevoeging · gevolg.',per:8,pool:[
   {q:'Reciclo ___ es importante.',opts:['porque','además','por eso'],ans:'porque',why:'reden'},
   {q:'Es sano; ___, es barato.',opts:['además','porque','por eso'],ans:'además',why:'toevoeging'},
   {q:'Contamina; ___ voy en bici.',opts:['por eso','porque','además'],ans:'por eso',why:'gevolg'},
   {q:'Como fruta ___ es sana.',opts:['porque','además','por eso'],ans:'porque',why:'reden'},
   {q:'Hago deporte; ___, duermo mejor.',opts:['además','porque','por eso'],ans:'además',why:'toevoeging'},
   {q:'El aire está sucio; ___ uso mascarilla.',opts:['por eso','porque','además'],ans:'por eso',why:'gevolg'},
   {q:'Ahorro agua ___ es un bien escaso.',opts:['porque','además','por eso'],ans:'porque',why:'reden'},
   {q:'Es útil; ___, ahorra tiempo.',opts:['además','porque','por eso'],ans:'además',why:'toevoeging'},
   {q:'Llueve; ___ llevo paraguas.',opts:['por eso','porque','además'],ans:'por eso',why:'gevolg'},
   {q:'Voy en bici ___ no contamina.',opts:['porque','además','por eso'],ans:'porque',why:'reden'}]});
 buildChoice('gx_subj',{title:'Sin embargo / por un lado',desc:'Tegenstelling en twee kanten.',per:6,pool:[
   {q:'Es caro; ___, funciona bien.',opts:['sin embargo','por eso','porque'],ans:'sin embargo',why:'tegenstelling'},
   {q:'___ un lado es cómodo; por otro, contamina.',opts:['Por','Para','Con'],ans:'Por',why:'por un lado'},
   {q:'Me gusta; ___, es un poco caro.',opts:['sin embargo','por eso','además'],ans:'sin embargo',why:'tegenstelling'},
   {q:'Por un lado ahorra tiempo; ___ otro lado, contamina.',opts:['por','para','con'],ans:'por',why:'por otro lado'},
   {q:'Es práctico; ___, hace ruido.',opts:['sin embargo','porque','por eso'],ans:'sin embargo',why:'tegenstelling'},
   {q:'«echter» =',opts:['sin embargo','por eso','además'],ans:'sin embargo',why:'sin embargo'}]});
 buildChoice('gx_plural',{title:'¿a favor o en contra?',desc:'Vóór of tégen (del coche en la ciudad)?',per:6,pool:[
   {q:'«Es rápido» =',opts:['a favor','en contra'],ans:'a favor',why:'vóór'},
   {q:'«Contamina el aire» =',opts:['en contra','a favor'],ans:'en contra',why:'tégen'},
   {q:'«Es cómodo cuando llueve» =',opts:['a favor','en contra'],ans:'a favor',why:'vóór'},
   {q:'«Hace mucho ruido» =',opts:['en contra','a favor'],ans:'en contra',why:'tégen'},
   {q:'«Da libertad para viajar» =',opts:['a favor','en contra'],ans:'a favor',why:'vóór'},
   {q:'«Gasta gasolina» =',opts:['en contra','a favor'],ans:'en contra',why:'tégen'},
   {q:'«Provoca atascos» =',opts:['en contra','a favor'],ans:'en contra',why:'tégen'},
   {q:'«Es útil con niños» =',opts:['a favor','en contra'],ans:'a favor',why:'vóór'}]});
 buildChoice('gx_nac',{title:'Traduce — imperativo/opinión',desc:'Kies de correcte Spaanse zin.',per:6,pool:[
   {q:'Eet gezond en drink water. →',opts:['Come sano y bebe agua.','Comes sano y bebes agua.','Comer sano y beber agua.'],ans:'Come sano y bebe agua.',why:'imperativo'},
   {q:'Ik denk dat we moeten recyclen. →',opts:['Creo que debemos reciclar.','Creo que debamos reciclar.','Creo reciclar.'],ans:'Creo que debemos reciclar.',why:'creo que + indicativo'},
   {q:'Recycle het, want het is belangrijk. →',opts:['Recíclalo porque es importante.','Recicla lo porque es importante.','Recíclalo por eso es importante.'],ans:'Recíclalo porque es importante.',why:'imperativo + pronombre + porque'},
   {q:'Zorg voor jezelf. →',opts:['Cuídate.','Te cuidas.','Cuidarte.'],ans:'Cuídate.',why:'imperativo + te'},
   {q:'Ik ben het eens met jou. →',opts:['Estoy de acuerdo contigo.','Soy de acuerdo contigo.','Tengo acuerdo contigo.'],ans:'Estoy de acuerdo contigo.',why:'estar de acuerdo'},
   {q:'Doe sport; bovendien slaap je beter. →',opts:['Haz deporte; además, duermes mejor.','Hace deporte; además, duermes mejor.','Haz deporte; porque duermes mejor.'],ans:'Haz deporte; además, duermes mejor.',why:'haz + además'}]});
 buildMatch('gx_conc',{title:'Empareja: infinitivo ↔ imperativo (tú)',desc:'Koppel het werkwoord aan de imperativo.',per:6,pool:[
   {a:'hacer',b:'haz'},{a:'ir',b:'ve'},{a:'decir',b:'di'},{a:'tener',b:'ten'},
   {a:'venir',b:'ven'},{a:'poner',b:'pon'},{a:'ser',b:'sé'},{a:'salir',b:'sal'},
   {a:'comer',b:'come'},{a:'reciclar',b:'recicla'}]});
 buildMatch('gx_conc2',{title:'Empareja: conector/opinión ↔ NL',desc:'Koppel de uitdrukking aan de vertaling.',per:6,pool:[
   {a:'porque',b:'want/omdat'},{a:'además',b:'bovendien'},{a:'por eso',b:'daarom'},{a:'sin embargo',b:'echter'},
   {a:'creo que',b:'ik denk dat'},{a:'estoy de acuerdo',b:'ik ben het eens'}]});
 buildChoice('gx_mix',{title:'Repaso mixto — imperativo + opinar + conectores',desc:'Alles door elkaar. Directe feedback.',per:8,pool:[
   {q:'___ (comer) más fruta.',opts:['Come','Comes','Comer'],ans:'Come',why:'imperativo'},
   {q:'hacer → imperativo (tú)',opts:['haz','hace','haces'],ans:'haz',why:'irregular'},
   {q:'cuida + te =',opts:['cuídate','cuidate','te cuida'],ans:'cuídate',why:'+ pronombre'},
   {q:'Creo que el deporte ___ bueno.',opts:['es','sea','ser'],ans:'es',why:'indicativo'},
   {q:'Reciclo ___ es importante.',opts:['porque','además','por eso'],ans:'porque',why:'reden'},
   {q:'Contamina; ___ voy en bici.',opts:['por eso','porque','además'],ans:'por eso',why:'gevolg'},
   {q:'ir → imperativo (tú)',opts:['ve','va','vas'],ans:'ve',why:'irregular'},
   {q:'«ik ben het eens» =',opts:['estoy de acuerdo','soy de acuerdo','tengo acuerdo'],ans:'estoy de acuerdo',why:'estar de acuerdo'},
   {q:'Es sano; ___, es barato.',opts:['además','porque','por eso'],ans:'además',why:'toevoeging'},
   {q:'haz + lo =',opts:['hazlo','házlo','lo haz'],ans:'hazlo',why:'+ pronombre'},
   {q:'«want / omdat» =',opts:['porque','por eso','además'],ans:'porque',why:'porque'},
   {q:'En mi opinión, el planeta ___ en peligro.',opts:['está','esté','estar'],ans:'está',why:'indicativo'}]});
 // ===== VOCABULARIO =====
 buildMatch('vx_match',{title:'Empareja: palabra ↔ emoji',desc:'Koppel het woord aan de emoji.',per:6,pool:[
   {a:'reciclar',b:'♻️'},{a:'el árbol',b:'🌳'},{a:'la basura',b:'🗑️'},{a:'el agua',b:'💧'},
   {a:'dormir',b:'😴'},{a:'la fruta',b:'🍎'},{a:'el deporte',b:'⚽'},{a:'la energía',b:'⚡'},
   {a:'la bici',b:'🚲'},{a:'el planeta',b:'🌍'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat past.',per:6,pool:[
   {q:'Para estar sano, ___ deporte.',opts:['haz','ten','ve'],ans:'haz',why:'hacer deporte'},
   {q:'___ el papel en el contenedor azul.',opts:['Recicla','Contamina','Gasta'],ans:'Recicla',why:'recyclen'},
   {q:'Bebe mucha ___.',opts:['agua','basura','energía'],ans:'agua',why:'water'},
   {q:'Creo ___ debemos proteger el planeta.',opts:['que','de','por'],ans:'que',why:'creo que'},
   {q:'Voy en bici ___ no contamina.',opts:['porque','por eso','además'],ans:'porque',why:'reden'},
   {q:'Duerme ocho horas para ___.',opts:['descansar','contaminar','gastar'],ans:'descansar',why:'rusten'},
   {q:'No tires ___ al suelo.',opts:['basura','fruta','energía'],ans:'basura',why:'afval'},
   {q:'En mi ___, el deporte es clave.',opts:['opinión','consejo','razón'],ans:'opinión',why:'en mi opinión'},
   {q:'Cuida el ___: recicla y ahorra.',opts:['planeta','estrés','cuerpo'],ans:'planeta',why:'planeet'},
   {q:'Estoy de ___ contigo.',opts:['acuerdo','razón','opinión'],ans:'acuerdo',why:'de acuerdo'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het woord.',per:6,pool:[
   {q:'Lo contrario de «enfermo»:',opts:['sano','sucio','caro'],ans:'sano',why:'gezond'},
   {q:'Volver a usar papel, vidrio, plástico:',opts:['reciclar','contaminar','gastar'],ans:'reciclar',why:'recyclen'},
   {q:'Lo que tiramos y no queremos:',opts:['la basura','la fruta','el árbol'],ans:'la basura',why:'afval'},
   {q:'«ik denk dat»:',opts:['creo que','por eso','además'],ans:'creo que',why:'mening'},
   {q:'Un sinónimo de «want / omdat»:',opts:['porque','por eso','sin embargo'],ans:'porque',why:'reden'},
   {q:'Usar menos agua o energía:',opts:['ahorrar','gastar','contaminar'],ans:'ahorrar',why:'besparen'},
   {q:'Una recomendación o tip:',opts:['el consejo','el estrés','el cuerpo'],ans:'el consejo',why:'tip'},
   {q:'«daarom» =',opts:['por eso','porque','además'],ans:'por eso',why:'gevolg'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['reciclar','ahorrar','proteger','contaminar'],odd:3,why:'contaminar is negatief, de rest beschermt'},
   {words:['come','bebe','haz','comes'],odd:3,why:'comes is presente, geen imperativo'},
   {words:['porque','además','por eso','planeta'],odd:3,why:'planeta is geen conector'},
   {words:['sano','enfermo','el deporte','la energía'],odd:3,why:'la energía hoort bij het milieu'},
   {words:['creo que','pienso que','en mi opinión','recicla'],odd:3,why:'recicla is een bevel, geen mening'},
   {words:['el árbol','el bosque','la naturaleza','el estrés'],odd:3,why:'el estrés hoort bij de gezondheid'},
   {words:['haz','ve','di','hace'],odd:3,why:'hace is presente, geen imperativo'},
   {words:['la fruta','dormir','el deporte','la basura'],odd:3,why:'la basura hoort bij het milieu'}]});
 // ===== LECTURA =====
 buildOrder('lx_order',{title:'Ordena',desc:'Tik in de juiste volgorde.',rounds:[
   {sub:'un consejo',items:[{label:'Usa la bici',key:1},{label:'o el transporte público',key:2},{label:'porque',key:3},{label:'el coche contamina.',key:4}]},
   {sub:'una opinión',items:[{label:'Creo que',key:1},{label:'todos podemos ayudar',key:2},{label:'con pequeños',key:3},{label:'gestos.',key:4}]},
   {sub:'reageren',items:[{label:'Estoy de acuerdo',key:1},{label:'porque es sano',key:2},{label:'y, además,',key:3},{label:'ahorro dinero.',key:4}]},
   {sub:'tegenstelling',items:[{label:'Me gusta la bici;',key:1},{label:'sin embargo,',key:2},{label:'en mi pueblo',key:3},{label:'no hay carril bici.',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in de twee teksten en kies.',per:6,pool:[
   {q:'¿Qué medio de transporte recomienda la revista?',opts:['la bici o el transporte público','el coche','el avión'],ans:'la bici o el transporte público',why:'«Usa la bici o el transporte público»'},
   {q:'¿Por qué hay que usar la bici?',opts:['porque el coche contamina','porque es caro','porque es lento'],ans:'porque el coche contamina',why:'«porque el coche contamina mucho»'},
   {q:'¿Qué hay que comer, según el texto?',opts:['más verdura y menos carne','más carne','solo fruta'],ans:'más verdura y menos carne',why:'«Come más verdura y menos carne»'},
   {q:'¿Está de acuerdo el lector con la revista?',opts:['sí','no','no lo dice'],ans:'sí',why:'«Estoy de acuerdo con la revista»'},
   {q:'¿Por qué va en bici el lector?',opts:['porque es sano y no contamina','porque es rápido','porque es caro'],ans:'porque es sano y no contamina',why:'«es sano y no contamina»'},
   {q:'¿Qué problema tiene el pueblo del lector?',opts:['no hay carril bici','hay mucho tráfico','no hay contenedores'],ans:'no hay carril bici',why:'«no hay carril bici»'},
   {q:'¿Qué debe hacer el ayuntamiento, según el lector?',opts:['hacer más','no hacer nada','subir los impuestos'],ans:'hacer más',why:'«el ayuntamiento debe hacer más»'},
   {q:'¿Con qué lema termina el texto?',opts:['¡pura vida!','¡hasta luego!','¡buen viaje!'],ans:'¡pura vida!',why:'«¡pura vida!»'}]});
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='C6plus_U7_web_mijn_versie.html';a.click();};
})();
"""

# Getypte woordenschat-drills (fase ophalen + produceren) in het paneel zelf.
JS += hub_type_sets.vocab_type_js(vocab)
JS += hub_type_gram.js('C6+', 7)
JS += (hub_bloques.escucha_js("esc_c6p_u7", escucha_data.C6P_U7)
       + hub_bloques.lectura_js("lec_c6p_u7", lectura_data.C6P_U7))
HTML = HTML.replace("__GRAMSLOTS__", hub_type_gram.slots('C6+', 7))
HTML = HTML.replace("__NGAMES__", str(len(GAMES)))
HTML = HTML.replace("__BRONNEN__", extra_bronnen.html('C6+', 7))
HTML = HTML.replace("__TYPESLOTS__", hub_type_sets.SLOTS_HTML)

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/C6plus_U7_web.html","w").write(html)
print("C6plus_U7_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
