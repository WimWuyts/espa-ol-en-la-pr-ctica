#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C6+ · U0 «¡Volvemos!» (het reencuentro).
# Eén standalone bestand: fonts base64, de U0-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U0-vocab), visuele/interactieve grammatica (presente · género/concordancia · ser/estar),
# klikbare kaart (mundo hispano, meelopende fiche) + TTS + inline recorder + Lectura + editbar. Huisstijl morado.
import json, base64, os, sys
import hub_drills, hub_bloques
import hub_type_sets
import hub_type_gram
import extra_bronnen
import nat_data, escucha_data, lectura_data
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
   ['pais-nacionalidad', 'país ↔ nacionalidad', 'match'],
   ['verbo-yo', 'el verbo y su yo', 'match']]],
 ['② Distinguir · gramática', [
   ['formal-informal', '¿formal o informal?', 'classify'],
   ['genero', '¿el o la?', 'classify'],
   ['ser-estar', '¿soy o estoy?', 'classify']]],
 ['③ Producir con apoyo', [
   ['presente', 'completa: el presente', 'cloze'],
   ['concordancia', 'completa: concordancia', 'cloze'],
   ['concordancia-tetris', 'concordancia Tetris', 'tetris'],
   ['presentacion-order', 'ordena la presentación', 'order'],
   ['senala', 'señala', 'point'],
   ['acento-tap', '¿dónde va el acento?', 'tap']]],
 ['④ Hablar · grábate 🎙️', [
   ['repite-saludos', 'escucha y repite: saludos', 'speak'],
   ['mensaje-presentate', 'mensaje de voz: preséntate', 'speak'],
   ['vuelve-presentate', 'preséntate otra vez', 'sim'],
   ['carrusel-presentate', 'carrusel · preséntate', 'speak']]]]
# De getypte woordenschatladder (make_vocab_type_games.py): ophalen en
# produceren, de treden die boven het koppelen en aanwijzen liggen.
_grupo = hub_bloques.grupo_escribir(
    lambda sl: os.path.exists(f"{ROOT}/spaans-motor/games/es-c6plus-u0-{sl}.html"))
if _grupo: MOTOR.append(_grupo)
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-c6plus-u0-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-c6plus-u0-{s}.html")}

CSS = FONTS + extra_bronnen.CSS + hub_drills.TYPE_CSS + hub_drills.ESCUCHA_CSS + hub_drills.LECTURA_CSS + hub_bloques.CSS_EXTRA + """
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
<title>Más español en la práctica · C6+ U0 ¡Volvemos!</title>
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
    <div><h1>U0 · ¡Volvemos!</h1>
    <p>La página digital de la Unidad 0 (el <b>reencuentro</b>): flashcards, gramática visual e interactiva y <b>__NGAMES__ juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie. Diagnostische repaso: presente · género · países.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U0. Klik om te draaien; wissel ES↔NL; filter per groep; klik 🔊 om te horen. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
    __FC__
    <h2 class="sec">Ejercicios de vocabulario · zelfcorrectie</h2>
    <p class="lead">Oefen de woorden actief: koppelen, invullen, definities en de <b>intruder</b>. Elke oefening geeft directe feedback en je kunt telkens een <b>andere reeks</b> trekken. <span class="gloss">herkennen → onderscheiden → ophalen.</span></p>
    <div class="card ex" id="vx_match"></div>
    <div class="card ex" id="vx_gap"></div>
    <div class="card ex" id="vx_def"></div>
    <div class="card ex" id="vx_odd"></div>
    <h3 class="subh">🌎 Países y nacionalidades — la serie completa</h3>
    <p class="lead">Eerst <b>koppelen</b> (herkennen), daarna <b>zelf schrijven</b> (produceren). Dezelfde twintig landen, twee treden van de ladder.</p>
    <div class="card ex" id="nat_c6p_match"></div>
    <div class="card ex" id="nat_c6p_type"></div>
__TYPESLOTS__
    <h2 class="sec">Naslagwerk · zoeken</h2>
    __NAS__
  </section>

  <section class="panel" data-p="gram">
    <h2 class="sec">Gramática visual e interactiva</h2>
    <p class="lead">De <b>essentiële</b> grammatica van U0: de <b>werkwoorden</b> en de <b>concordancia</b>. Hier oefen je <b>maximaal</b> — elke oefening trekt uit een grote pool, dus «↻ otra serie» geeft telkens een nieuwe reeks. <span class="gloss">Eerst betekenis/patroon ontdekken, dan de regel.</span></p>
    <div class="card" id="colorsent"></div>
    <div class="card" id="irconj"></div>
    <h2 class="sec" style="margin-top:26px">🔑 Los verbos — máxima práctica</h2>
    <p class="lead">De motor van alles. Regelmatig (-ar/-er/-ir) én de 7 irregulares (ser · estar · tener · ir · hacer · venir · dar). <span class="gloss">Blijf herspelen tot de vormen automatisch komen.</span></p>
    <div class="card ex" id="gx_reg"></div>
    <div class="card ex" id="gx_irreg"></div>
    <div class="card ex" id="gx_ser"></div>
    <div class="card ex" id="gx_iraq"></div>
    <div class="card ex" id="gx_subj"></div>
    <div class="card ex" id="gx_build"></div>
    <h3 class="subh">🔀 Ser o estar — soy / estoy</h3>
    <div class="game" id="g_pron"></div>
    <div class="card ex" id="gx_pronq"></div>
    <h2 class="sec" style="margin-top:26px">⚖️ La concordancia — máxima práctica</h2>
    <p class="lead">Alles komt overeen: <b>género</b> (el/la · -o/-a), <b>número</b> (plural) en de <b>nacionalidades</b>. <span class="gloss">Kijk telkens naar m/v én enkelvoud/meervoud.</span></p>
    <div class="game" id="g_cantidad"></div>
    <div class="card ex" id="gx_cantq"></div>
    <div class="card ex" id="gx_adj"></div>
    <div class="card ex" id="gx_plural"></div>
    <div class="card ex" id="gx_nac"></div>
    <div class="card ex" id="gx_conc"></div>
    <div class="card ex" id="gx_conc2"></div>
    <h3 class="subh">🎯 Repaso mixto — verbos + concordancia</h3>
    <div class="card ex" id="gx_mix"></div>
  __GRAMSLOTS__
  </section>

  <section</section>

  <section class="panel" data-p="lectura">
    <h2 class="sec">Lectura · dos perfiles</h2>
    <p class="lead">Lees de <b>twee perfielen</b> van de cast, <b>luister</b> ze (🔊 TTS) en <b>controleer je begrip</b>. Daarna reageer je: met wie heb je meer gemeen? <span class="gloss">Keten: lezen → schrijven/spreken.</span></p>
    <div id="lecturawrap"></div>
    <h3 class="subh">🔢 Ordena la presentación</h3>
    <div class="card ex" id="lx_order"></div>
    <h3 class="subh">🔎 Comprensión · escanea y escoge</h3>
    <div class="card ex" id="lx_scan"></div>
    <h2 class="sec">Lectura completa · el tablón de anuncios</h2>
    <p class="lead">Drie echte berichtjes van het prikbord, met de volledige leesroute: <b>voorspellen → globaal → scannen → juist/fout met bewijs → betekenis uit de context → zelf schrijven</b>. <span class="gloss">Dezelfde tekst staat in je cursus, met schrijfruimte.</span></p>
    <div class="card ex" id="lec_c6p"></div>
  </section>

  <section class="panel" data-p="juegos">
    <h2 class="sec">Ejercicios · __NGAMES__ juegos, jij kiest</h2>
    <p class="lead">Geordend van <b>herkennen → onderscheiden → produceren met steun → analyseren &amp; communiceren → hablar</b>. Elk spel geeft directe, verklarende feedback en de steun bouwt af. <span class="gloss">Klik een spel; het opent in een venster en werkt ook offline.</span></p>
    <div id="motorlink"></div>
  </section>

  <section class="panel" data-p="retos">
    <h2 class="sec">Retos · tres desafíos 🎯</h2>
    <p class="lead">Drie retos met <b>één harde regel</b>: je beschrijft jezelf <b>alleen met wat je niet bent</b>, je neemt een welkomstboodschap op voor iemand die vandaag van nul begint, en je krijgt een mail uit Buenos Aires met woorden die je <b>niet kent</b> — en je vraagt het na in het Spaans, niet in het Engels. <span class="gloss">De zeven andere retos van deze unit staan in het boek en in de PowerPoint.</span></p>
    <div id="retos_c6p_u0"></div>
  </section>
  <section class="panel" data-p="hablar">
    <h2 class="sec">Hablar · grábate 🎙️</h2>
    <p class="lead">Neem <b>jezelf</b> op: luister naar het model, spreek in, luister terug, en neem opnieuw op. <span class="gloss">Werkt in Chrome/Edge; sta de micro toe. Print blijft bruikbaar zonder opname.</span></p>
    <div class="card" id="rec_repite"></div>
    <div class="card" id="rec_pedido"></div>
    <div class="card" id="rec_plato"></div>
    <p class="lead" style="margin-top:8px">Meer spreek-/opnamespellen (preséntate, describe…) vind je ook onder <b>Juegos ④</b>.</p>
  </section>

  <section class="panel" data-p="escuchar">
    <h2 class="sec">Escuchar · el primer día de curso 🎧</h2>
    <p class="lead">Eén gesprek op de speelplaats, zes stappen: <b>situatie</b> → <b>globaal</b> → <b>details</b> → <b>juist/fout met bewijs</b>. Het <b>transcript</b> gaat pas open als de taken klaar zijn. <span class="gloss">Zolang er nog geen opname is, leest de computerstem het gesprek voor.</span></p>
    <div class="card ex" id="esc_c6p"></div>
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
    __BRONNEN__
  </section>

  <div class="foot">Más español en la práctica · edición única · Unidad 0 «¡Volvemos!» — página digital. Uitbreiding op de PDF · huisstijl morado · print ↔ PowerPoint ↔ web.</div>
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
document.getElementById('motorlink').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 4px">Arcade · la máquina de juegos 🕹️</h3><p class="gloss" style="margin:0 0 10px">'+MOTOR.reduce((n,g)=>n+g[1].length,0)+' extra spellen met score & directe feedback — ingebed, dus ze werken ook als je dit bestand downloadt. Klik om te spelen.</p>'+MOTOR.map(([grp,gs])=>'<div class="subh">'+grp+'</div><div class="fcgrid">'+
   gs.map(([f,t,tpl])=>'<div class="chip" style="display:block;border-radius:14px" onclick="openGame(\''+f+'\',\''+t.replace(/'/g,"")+'\')"><div style="font-weight:700;color:var(--ink);font-size:14px">'+t+'</div><div class="pill" style="margin-top:4px;font-size:10px">'+tpl+'</div></div>').join('')+'</div>').join('');
function openGame(slug,title){const g=GAMES[slug];if(!g){alert('Spel niet gevonden.');return;}
  document.getElementById('gmtitle').textContent=title;document.getElementById('gframe').src='data:text/html;base64,'+g;document.getElementById('gmodal').classList.add('show');}
function closeGame(){document.getElementById('gmodal').classList.remove('show');document.getElementById('gframe').src='about:blank';}
document.getElementById('gmodal').addEventListener('click',e=>{if(e.target.id==='gmodal')closeGame();});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeGame();});

// ---- KAART interactief ----
(function(){
   const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "🌎 Símbolo: el águila sobre el nopal, en la bandera", "star": 0, "nl": ""}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "🌎 Símbolo: el sol y «¡hola!» como saludo", "star": 1, "nl": "★ ¡Estás aquí! Parada U0–U1 · el mundo hispano · España (Lucía)"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "🌎 Símbolo: el cóndor y el grano de café", "star": 0, "nl": ""}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "🌎 Símbolo: el sol inca y la llama", "star": 0, "nl": ""}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "🌎 Símbolo: el sol de mayo en la bandera", "star": 0, "nl": ""}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "🌎 Símbolo: las siete estrellas de la bandera", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "🌎 Símbolo: la estrella solitaria de la bandera", "star": 0, "nl": ""}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "🌎 Símbolo: el cóndor de los Andes", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "🌎 Símbolo: el quetzal, ave nacional", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "🌎 Símbolo: la estrella solitaria y la palma real", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "🌎 Símbolo: el cóndor y la bandera wiphala", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "🌎 Símbolo: la única bandera del mundo con una Biblia", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "🌎 Símbolo: las cinco estrellas de Centroamérica", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "🌎 Símbolo: la única bandera distinta por cada lado", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "🌎 Símbolo: el arco iris en el escudo nacional", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "🌎 Símbolo: un volcán en el paisaje nacional", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "🌎 Símbolo: «Pura Vida», saludo y lema del país", "star": 0, "nl": ""}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "🌎 Símbolo: las dos estrellas y el Canal", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "🌎 Símbolo: el sol de mayo, como Argentina", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "🌎 Símbolo: la rana coquí, símbolo de la isla", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "🌎 Símbolo: la única nación hispana de África", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "🌎 Símbolo: la mezcla de banderas hispanas en las calles", "star": 0, "nl": ""}};
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
""" + hub_drills.RECORDER_JS + r"""
function buildRecorders(){
 makeRecorder('rec_repite',{title:'Escucha y repite: saludos y presentación',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'¡Hola! Me llamo Diego.',cue:'presentarse',tip:'Duidelijk? Probeer nog eens zonder te lezen.'},{text:'Soy de Bélgica y tengo dieciséis años.',cue:'origen + edad'},{text:'Vivo en Gante y hablo neerlandés.',cue:'dónde + lengua'},{text:'Encantado, ¿cómo te llamas?',cue:'cortesía'},{text:'Buenos días, ¿qué tal?',cue:'saludo'},{text:'¡Hasta luego!',cue:'despedida'}]});
 makeRecorder('rec_pedido',{title:'Mensaje de voz: preséntate',desc:'Neem één bericht op (20–30 s): nombre, edad, de dónde eres, dónde vives y una lengua.',items:[
   {text:'Preséntate: nombre, edad, origen, dónde vives y una lengua.',cue:'tu presentación',tip:'5 gegevens gezegd? Neem opnieuw op.'}]});
 makeRecorder('rec_plato',{title:'Describe a un compañero/a',desc:'Beschrijf een klasgenoot: ¿cómo es? (carácter y físico).',items:[
   {text:'Mi compañero/a se llama ___ . Es ___ y ___ . Tiene ___ .',cue:'tu versión',tip:'2 karakter + 1 fysiek? Herneem.'}]});
}

// ================= INLINE ZELFCORRIGERENDE OEFENINGEN =================
""" + hub_drills.HELPERS_JS + r"""

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
 // ===== WERKWOORDEN (essentieel · grote pools) =====
 buildChoice('gx_reg',{title:'Regulares: -ar / -er / -ir',desc:'Kies de juiste vorm van het regelmatige werkwoord.',per:8,pool:[
   {q:'(Yo) ___ (hablar) español.',opts:['hablo','hablas','habla'],ans:'hablo',why:'yo → -o'},
   {q:'(Tú) ___ (hablar) muy bien.',opts:['hablas','hablo','habla'],ans:'hablas',why:'tú → -as'},
   {q:'Ella ___ (estudiar) mucho.',opts:['estudia','estudias','estudio'],ans:'estudia',why:'él/ella → -a'},
   {q:'(Nosotros) ___ (trabajar) aquí.',opts:['trabajamos','trabajáis','trabajan'],ans:'trabajamos',why:'nosotros → -amos'},
   {q:'(Vosotros) ___ (escuchar) música.',opts:['escucháis','escuchan','escuchamos'],ans:'escucháis',why:'vosotros → -áis'},
   {q:'(Ellos) ___ (comprar) pan.',opts:['compran','compra','compráis'],ans:'compran',why:'ellos → -an'},
   {q:'(Yo) ___ (comer) a las dos.',opts:['como','comes','come'],ans:'como',why:'yo → -o'},
   {q:'(Tú) ___ (beber) agua.',opts:['bebes','bebe','bebo'],ans:'bebes',why:'tú → -es'},
   {q:'Él ___ (leer) un libro.',opts:['lee','lees','leo'],ans:'lee',why:'él → -e'},
   {q:'(Nosotros) ___ (comer) juntos.',opts:['comemos','coméis','comen'],ans:'comemos',why:'nosotros → -emos'},
   {q:'(Ellos) ___ (aprender) español.',opts:['aprenden','aprende','aprendéis'],ans:'aprenden',why:'ellos → -en'},
   {q:'(Yo) ___ (vivir) en Gante.',opts:['vivo','vives','vive'],ans:'vivo',why:'yo → -o'},
   {q:'(Tú) ___ (escribir) un correo.',opts:['escribes','escribe','escribo'],ans:'escribes',why:'tú → -es'},
   {q:'Ella ___ (abrir) la puerta.',opts:['abre','abres','abro'],ans:'abre',why:'él/ella → -e'},
   {q:'(Nosotros) ___ (vivir) en Flandes.',opts:['vivimos','vivís','viven'],ans:'vivimos',why:'nosotros → -imos'},
   {q:'(Vosotros) ___ (escribir) bien.',opts:['escribís','escriben','escribimos'],ans:'escribís',why:'vosotros → -ís'}]});
 buildChoice('gx_irreg',{title:'Los 7 irregulares clave',desc:'ser · estar · tener · ir · hacer · venir · dar. Kies de juiste vorm.',per:8,pool:[
   {q:'(Yo) ___ (ser) estudiante.',opts:['soy','eres','es'],ans:'soy',why:'ser: yo → soy'},
   {q:'(Yo) ___ (estar) en clase.',opts:['estoy','estás','está'],ans:'estoy',why:'estar: yo → estoy'},
   {q:'(Yo) ___ (tener) 16 años.',opts:['tengo','tienes','tiene'],ans:'tengo',why:'tener: yo → tengo'},
   {q:'(Yo) ___ (ir) al instituto.',opts:['voy','vas','va'],ans:'voy',why:'ir: yo → voy'},
   {q:'(Yo) ___ (hacer) deporte.',opts:['hago','haces','hace'],ans:'hago',why:'hacer: yo → hago'},
   {q:'(Yo) ___ (venir) de casa.',opts:['vengo','vienes','viene'],ans:'vengo',why:'venir: yo → vengo'},
   {q:'(Yo) ___ (dar) las gracias.',opts:['doy','das','da'],ans:'doy',why:'dar: yo → doy'},
   {q:'(Tú) ___ (tener) hambre.',opts:['tienes','tengo','tiene'],ans:'tienes',why:'tener: tú → tienes'},
   {q:'Ella ___ (estar) contenta.',opts:['está','estás','estoy'],ans:'está',why:'estar: ella → está'},
   {q:'Diego ___ (ir) al mercado.',opts:['va','vas','voy'],ans:'va',why:'ir: él → va'},
   {q:'(Nosotros) ___ (ser) amigos.',opts:['somos','sois','son'],ans:'somos',why:'ser: nosotros → somos'},
   {q:'(Nosotros) ___ (tener) clase.',opts:['tenemos','tenéis','tienen'],ans:'tenemos',why:'tener: nosotros → tenemos'},
   {q:'(Vosotros) ___ (hacer) los deberes.',opts:['hacéis','hacen','hacemos'],ans:'hacéis',why:'hacer: vosotros → hacéis'},
   {q:'(Ellos) ___ (venir) de México.',opts:['vienen','venís','viene'],ans:'vienen',why:'venir: ellos → vienen'},
   {q:'(Ellos) ___ (ir) a España.',opts:['van','va','vamos'],ans:'van',why:'ir: ellos → van'},
   {q:'(Tú) ___ (hacer) la cena.',opts:['haces','hago','hace'],ans:'haces',why:'hacer: tú → haces'},
   {q:'(Nosotros) ___ (estar) bien.',opts:['estamos','estáis','están'],ans:'estamos',why:'estar: nosotros → estamos'},
   {q:'Mateo ___ (venir) de Argentina.',opts:['viene','vienes','vengo'],ans:'viene',why:'venir: él → viene'}]});
 buildChoice('gx_ser',{title:'Conjuga «ser»',desc:'De volledige vervoeging van ser. Kies de vorm.',per:6,pool:[
   {q:'yo →',opts:['soy','eres','es'],ans:'soy',why:'yo → soy'},
   {q:'tú →',opts:['eres','es','soy'],ans:'eres',why:'tú → eres'},
   {q:'él/ella →',opts:['es','eres','somos'],ans:'es',why:'él/ella → es'},
   {q:'nosotros →',opts:['somos','sois','son'],ans:'somos',why:'nosotros → somos'},
   {q:'vosotros →',opts:['sois','son','somos'],ans:'sois',why:'vosotros → sois'},
   {q:'ellos →',opts:['son','sois','es'],ans:'son',why:'ellos → son'},
   {q:'María y yo ___ amigos.',opts:['somos','son','sois'],ans:'somos',why:'nosotros → somos'},
   {q:'Vosotras ___ de Madrid.',opts:['sois','son','somos'],ans:'sois',why:'vosotros → sois'}]});
 buildChoice('gx_iraq',{title:'El presente — todo mezclado',desc:'Regular + irregular, alle personen door elkaar.',per:8,pool:[
   {q:'(Yo) ___ de Bélgica.',opts:['soy','eres','es'],ans:'soy',why:'ser: yo → soy'},
   {q:'¿(Tú) ___ en Gante?',opts:['vives','vivo','vive'],ans:'vives',why:'vivir: tú → vives'},
   {q:'Nina ___ dieciséis años.',opts:['tiene','tienes','tengo'],ans:'tiene',why:'tener: ella → tiene'},
   {q:'(Nosotros) ___ español.',opts:['hablamos','habláis','hablan'],ans:'hablamos',why:'hablar: nosotros'},
   {q:'Diego ___ al mercado.',opts:['va','vas','voy'],ans:'va',why:'ir: él → va'},
   {q:'(Yo) ___ muy bien.',opts:['estoy','está','estás'],ans:'estoy',why:'estar: yo → estoy'},
   {q:'¿(Vosotros) ___ los deberes?',opts:['hacéis','hacen','hago'],ans:'hacéis',why:'hacer: vosotros'},
   {q:'(Ellos) ___ de México.',opts:['vienen','venís','viene'],ans:'vienen',why:'venir: ellos'},
   {q:'Lucía ___ española.',opts:['es','eres','soy'],ans:'es',why:'ser: ella → es'},
   {q:'(Yo) ___ dos hermanas.',opts:['tengo','tienes','tiene'],ans:'tengo',why:'tener: yo → tengo'},
   {q:'(Nosotros) ___ amigos.',opts:['somos','sois','son'],ans:'somos',why:'ser: nosotros'},
   {q:'¿Cómo te ___ ?',opts:['llamas','llama','llamo'],ans:'llamas',why:'llamarse: tú'},
   {q:'(Ellos) ___ mucho español.',opts:['hablan','habláis','hablamos'],ans:'hablan',why:'hablar: ellos'},
   {q:'(Yo) ___ deporte.',opts:['hago','haces','hace'],ans:'hago',why:'hacer: yo → hago'},
   {q:'(Tú) ___ contento hoy.',opts:['estás','está','estoy'],ans:'estás',why:'estar: tú → estás'},
   {q:'(Yo) ___ al insti en bici.',opts:['voy','vas','va'],ans:'voy',why:'ir: yo → voy'},
   {q:'(Nosotros) ___ en Flandes.',opts:['vivimos','vivís','viven'],ans:'vivimos',why:'vivir: nosotros'},
   {q:'(Vosotros) ___ de Madrid.',opts:['sois','son','somos'],ans:'sois',why:'ser: vosotros'},
   {q:'Mateo ___ de Argentina.',opts:['viene','vienes','vengo'],ans:'viene',why:'venir: él → viene'},
   {q:'(Ellos) ___ hambre.',opts:['tienen','tenéis','tenemos'],ans:'tienen',why:'tener: ellos'}]});
 buildChoice('gx_subj',{title:'¿Qué forma va con el sujeto?',desc:'Kies de vorm die bij het onderwerp past.',per:7,pool:[
   {q:'Yo ___',opts:['soy','eres','es'],ans:'soy',why:'yo → soy'},
   {q:'Mis abuelos ___',opts:['viven','vive','vivís'],ans:'viven',why:'ellos → viven'},
   {q:'Tú ___',opts:['comes','come','como'],ans:'comes',why:'tú → comes'},
   {q:'Mi hermana ___',opts:['habla','hablas','hablo'],ans:'habla',why:'ella → habla'},
   {q:'Nosotros ___',opts:['tenemos','tienen','tenéis'],ans:'tenemos',why:'nosotros → tenemos'},
   {q:'Vosotros ___',opts:['hacéis','hacen','hacemos'],ans:'hacéis',why:'vosotros → hacéis'},
   {q:'Los chicos ___',opts:['van','va','vamos'],ans:'van',why:'ellos → van'},
   {q:'Usted ___',opts:['es','eres','soy'],ans:'es',why:'usted → es (3ª)'},
   {q:'Ella y yo ___',opts:['estamos','están','estáis'],ans:'estamos',why:'nosotros → estamos'},
   {q:'¿Y tú, de dónde ___?',opts:['eres','es','soy'],ans:'eres',why:'tú → eres'}]});
 buildOrder('gx_build',{title:'Ordena la presentación',desc:'Tik de zinnen in de logische volgorde.',rounds:[
   {sub:'saludar → nombre → origen → edad',items:[{label:'¡Hola! ¿Qué tal?',key:1},{label:'Me llamo Nina.',key:2},{label:'Soy de Perú.',key:3},{label:'Tengo dieciséis años.',key:4}]},
   {sub:'nombre → dónde vives → lengua → y tú',items:[{label:'Me llamo Diego.',key:1},{label:'Vivo en México.',key:2},{label:'Hablo español.',key:3},{label:'¿Y tú?',key:4}]},
   {sub:'pregunta → respuesta → repregunta → mucho gusto',items:[{label:'¿Cómo te llamas?',key:1},{label:'Me llamo Lucía, ¿y tú?',key:2},{label:'Yo soy Mateo.',key:3},{label:'¡Mucho gusto!',key:4}]},
   {sub:'origen → nacionalidad → lengua → carácter',items:[{label:'Soy de Cartagena.',key:1},{label:'Soy colombiana.',key:2},{label:'Hablo español.',key:3},{label:'Soy muy alegre.',key:4}]},
   {sub:'formal: saludar → nombre → usted → encantada',items:[{label:'Buenos días, señora.',key:1},{label:'Me llamo Ana.',key:2},{label:'¿Cómo se llama usted?',key:3},{label:'Encantada.',key:4}]}]});
 buildChoice('gx_pronq',{title:'¿soy o estoy?',desc:'ser (identiteit) of estar (plaats/gevoel)?',per:7,pool:[
   {q:'___ de Bélgica.',opts:['soy','estoy'],ans:'soy',why:'herkomst → ser'},
   {q:'___ en clase.',opts:['estoy','soy'],ans:'estoy',why:'plaats → estar'},
   {q:'___ estudiante.',opts:['soy','estoy'],ans:'soy',why:'identiteit → ser'},
   {q:'Hoy ___ contento.',opts:['estoy','soy'],ans:'estoy',why:'gevoel → estar'},
   {q:'___ belga.',opts:['soy','estoy'],ans:'soy',why:'nationaliteit → ser'},
   {q:'___ muy bien, gracias.',opts:['estoy','soy'],ans:'estoy',why:'toestand → estar'},
   {q:'___ simpático.',opts:['soy','estoy'],ans:'soy',why:'karakter → ser'},
   {q:'___ en casa.',opts:['estoy','soy'],ans:'estoy',why:'plaats → estar'},
   {q:'___ el hermano de Nina.',opts:['soy','estoy'],ans:'soy',why:'identiteit → ser'},
   {q:'___ cansado hoy.',opts:['estoy','soy'],ans:'estoy',why:'gevoel → estar'},
   {q:'___ profesor de español.',opts:['soy','estoy'],ans:'soy',why:'beroep → ser'},
   {q:'___ nervioso antes del examen.',opts:['estoy','soy'],ans:'estoy',why:'gevoel → estar'}]});
 // ===== CONCORDANCIA (essentieel · grote pools) =====
 buildChoice('gx_cantq',{title:'¿el o la? — género',desc:'Kies el (m) of la (v). Let op de valstrikken -ma/-a/-o/-dad.',per:8,pool:[
   {q:'___ problema',opts:['el','la'],ans:'el',why:'-ma → masculino'},
   {q:'___ casa',opts:['la','el'],ans:'la',why:'la casa (f)'},
   {q:'___ día',opts:['el','la'],ans:'el',why:'el día (m! -a)'},
   {q:'___ mano',opts:['la','el'],ans:'la',why:'la mano (f! -o)'},
   {q:'___ mapa',opts:['el','la'],ans:'el',why:'el mapa (m! -a)'},
   {q:'___ ciudad',opts:['la','el'],ans:'la',why:'-dad → femenino'},
   {q:'___ idioma',opts:['el','la'],ans:'el',why:'-ma → masculino'},
   {q:'___ foto',opts:['la','el'],ans:'la',why:'la foto (f! -o)'},
   {q:'___ libro',opts:['el','la'],ans:'el',why:'el libro (m)'},
   {q:'___ nacionalidad',opts:['la','el'],ans:'la',why:'-dad → femenino'},
   {q:'___ padre',opts:['el','la'],ans:'el',why:'el padre (m)'},
   {q:'___ madre',opts:['la','el'],ans:'la',why:'la madre (f)'},
   {q:'___ hombre',opts:['el','la'],ans:'el',why:'el hombre (m)'},
   {q:'___ mujer',opts:['la','el'],ans:'la',why:'la mujer (f)'},
   {q:'___ lengua',opts:['la','el'],ans:'la',why:'la lengua (f)'},
   {q:'___ país',opts:['el','la'],ans:'el',why:'el país (m)'},
   {q:'___ instituto',opts:['el','la'],ans:'el',why:'el instituto (m)'},
   {q:'___ clase',opts:['la','el'],ans:'la',why:'la clase (f)'}]});
 buildChoice('gx_adj',{title:'Concordancia del adjetivo',desc:'Kies de vorm die overeenkomt (m/v · ev/mv).',per:8,pool:[
   {q:'La chica es ___ .',opts:['simpática','simpático','simpáticas'],ans:'simpática',why:'la chica (f ev)'},
   {q:'El chico es ___ .',opts:['alto','alta','altos'],ans:'alto',why:'el chico (m ev)'},
   {q:'Los libros son ___ .',opts:['rojos','rojas','rojo'],ans:'rojos',why:'los libros (m pl)'},
   {q:'Las casas son ___ .',opts:['blancas','blancos','blanca'],ans:'blancas',why:'las casas (f pl)'},
   {q:'Nina es ___ .',opts:['peruana','peruano','peruanas'],ans:'peruana',why:'ella → peruana'},
   {q:'Diego es ___ .',opts:['mexicano','mexicana','mexicanos'],ans:'mexicano',why:'él → mexicano'},
   {q:'Mis amigas son ___ .',opts:['alegres','alegre','alegras'],ans:'alegres',why:'alegre → alegres (pl)'},
   {q:'La profesora es ___ .',opts:['trabajadora','trabajador','trabajadoras'],ans:'trabajadora',why:'la profesora (f ev)'},
   {q:'El coche es ___ .',opts:['nuevo','nueva','nuevos'],ans:'nuevo',why:'el coche (m ev)'},
   {q:'Las chicas son ___ .',opts:['morenas','morenos','morena'],ans:'morenas',why:'las chicas (f pl)'},
   {q:'Los perros son ___ .',opts:['pequeños','pequeñas','pequeño'],ans:'pequeños',why:'los perros (m pl)'},
   {q:'Mi madre es ___ .',opts:['española','español','españolas'],ans:'española',why:'ella → española'},
   {q:'Un ___ amigo (apócope).',opts:['buen','bueno','buena'],ans:'buen',why:'bueno → buen vóór m.ev.'},
   {q:'Una ___ ciudad (apócope).',opts:['gran','grande','grandes'],ans:'gran',why:'grande → gran vóór het nw.'},
   {q:'El libro es ___ .',opts:['azul','azula','azules'],ans:'azul',why:'azul = onveranderlijk (m/v)'},
   {q:'Los ejercicios son ___ .',opts:['difíciles','difícil','difíciles'],ans:'difíciles',why:'difícil → difíciles (pl)'},
   {q:'Valen es ___ .',opts:['colombiana','colombiano','colombianas'],ans:'colombiana',why:'ella → colombiana'},
   {q:'Mis hermanos son ___ .',opts:['altos','altas','alto'],ans:'altos',why:'los hermanos (m pl)'}]});
 buildChoice('gx_plural',{title:'El plural',desc:'Kies het juiste meervoud (klinker +s · medeklinker +es · -z → -ces).',per:7,pool:[
   {q:'el chico →',opts:['los chicos','las chicos','los chico'],ans:'los chicos',why:'klinker → +s'},
   {q:'la amiga →',opts:['las amigas','los amigas','las amiga'],ans:'las amigas',why:'klinker → +s'},
   {q:'el profesor →',opts:['los profesores','los profesors','las profesores'],ans:'los profesores',why:'medeklinker → +es'},
   {q:'la ciudad →',opts:['las ciudades','las ciudads','los ciudades'],ans:'las ciudades',why:'medeklinker → +es'},
   {q:'el lápiz →',opts:['los lápices','los lápizes','los lápiz'],ans:'los lápices',why:'-z → -ces'},
   {q:'la vez →',opts:['las veces','las vezes','las vez'],ans:'las veces',why:'-z → -ces'},
   {q:'la foto →',opts:['las fotos','los fotos','las fotoes'],ans:'las fotos',why:'klinker → +s (la foto, f)'},
   {q:'el país →',opts:['los países','los paises','las países'],ans:'los países',why:'medeklinker → +es'},
   {q:'la nacionalidad →',opts:['las nacionalidades','las nacionalidads','los nacionalidades'],ans:'las nacionalidades',why:'-dad → +es'},
   {q:'el problema →',opts:['los problemas','las problemas','los problema'],ans:'los problemas',why:'klinker → +s (m!)'},
   {q:'la mano →',opts:['las manos','los manos','las manoes'],ans:'las manos',why:'klinker → +s (f!)'},
   {q:'el reloj →',opts:['los relojes','los relojs','las relojes'],ans:'los relojes',why:'medeklinker → +es'}]});
 buildChoice('gx_nac',{title:'Concordancia de la nacionalidad',desc:'Kies de nationaliteit die overeenkomt met het onderwerp.',per:7,pool:[
   {q:'María es de España → es ___ .',opts:['española','español','españolas'],ans:'española',why:'v ev → española'},
   {q:'Tom es de Bélgica → es ___ .',opts:['belga','belgo','belgas'],ans:'belga',why:'belga = onveranderlijk'},
   {q:'Hans es de Alemania → es ___ .',opts:['alemán','alemana','alemanes'],ans:'alemán',why:'m ev → alemán'},
   {q:'Sophie es de Francia → es ___ .',opts:['francesa','francés','francesas'],ans:'francesa',why:'v ev → -esa'},
   {q:'Los chicos son de México → son ___ .',opts:['mexicanos','mexicano','mexicanas'],ans:'mexicanos',why:'m pl → -os'},
   {q:'Las chicas son de Perú → son ___ .',opts:['peruanas','peruanos','peruana'],ans:'peruanas',why:'v pl → -as'},
   {q:'Diego es ___ .',opts:['mexicano','mexicana','mexicanos'],ans:'mexicano',why:'m ev → -o'},
   {q:'Ella es de Italia → es ___ .',opts:['italiana','italiano','italianas'],ans:'italiana',why:'v ev → -a'},
   {q:'Ellos son de EE. UU. → son ___ .',opts:['estadounidenses','estadounidense','estadounidensos'],ans:'estadounidenses',why:'-ense → +s (pl)'},
   {q:'Ella es de Marruecos → es ___ .',opts:['marroquí','marroquía','marroquíes'],ans:'marroquí',why:'marroquí = onveranderlijk (ev)'},
   {q:'Nosotras somos de Colombia → somos ___ .',opts:['colombianas','colombianos','colombiana'],ans:'colombianas',why:'v pl → -as'},
   {q:'Él es de Reino Unido → es ___ .',opts:['inglés','inglesa','ingleses'],ans:'inglés',why:'m ev → -és'}]});
 buildMatch('gx_conc',{title:'Empareja: país ↔ nacionalidad',desc:'Koppel het land aan de nationaliteit.',per:6,pool:[
   {a:'España',b:'español/a'},{a:'México',b:'mexicano/a'},{a:'Colombia',b:'colombiano/a'},{a:'Perú',b:'peruano/a'},
   {a:'Argentina',b:'argentino/a'},{a:'Bélgica',b:'belga'},{a:'Alemania',b:'alemán/-ana'},{a:'Francia',b:'francés/-esa'},
   {a:'Italia',b:'italiano/a'},{a:'Marruecos',b:'marroquí'}]});
 buildMatch('gx_conc2',{title:'Empareja: sustantivo ↔ adjetivo',desc:'Koppel elk zelfstandig nw. aan het adjectief dat overeenkomt (m/v · ev/mv).',per:6,pool:[
   {a:'la chica',b:'simpática'},{a:'el chico',b:'alto'},{a:'las casas',b:'blancas'},{a:'los libros',b:'rojos'},
   {a:'la profesora',b:'trabajadora'},{a:'los perros',b:'pequeños'},{a:'la mochila',b:'roja'},{a:'el coche',b:'nuevo'},
   {a:'las amigas',b:'alegres'},{a:'los hermanos',b:'altos'}]});
 buildChoice('gx_mix',{title:'Repaso mixto — verbos + concordancia',desc:'Alles door elkaar. Directe feedback.',per:8,pool:[
   {q:'(Nosotros) ___ amigos.',opts:['somos','sois','son'],ans:'somos',why:'ser: nosotros'},
   {q:'La chica es ___ .',opts:['simpática','simpático','simpáticas'],ans:'simpática',why:'la chica (f ev)'},
   {q:'___ problema es difícil.',opts:['El','La','Los'],ans:'El',why:'el problema (m)'},
   {q:'(Yo) ___ en clase.',opts:['estoy','soy','está'],ans:'estoy',why:'estar: yo → estoy'},
   {q:'Diego ___ mexicano.',opts:['es','está','soy'],ans:'es',why:'ser: él → es'},
   {q:'Los libros son ___ .',opts:['rojos','rojas','rojo'],ans:'rojos',why:'los libros (m pl)'},
   {q:'¿(Tú) ___ dieciséis años?',opts:['tienes','tiene','tengo'],ans:'tienes',why:'tener: tú → tienes'},
   {q:'la ciudad → plural:',opts:['las ciudades','las ciudads','los ciudades'],ans:'las ciudades',why:'-dad → +es'},
   {q:'(Ellos) ___ de Perú.',opts:['son','somos','sois'],ans:'son',why:'ser: ellos → son'},
   {q:'Nina es ___ .',opts:['peruana','peruano','peruanas'],ans:'peruana',why:'ella → peruana'},
   {q:'Las casas son ___ .',opts:['blancas','blancos','blanca'],ans:'blancas',why:'las casas (f pl)'},
   {q:'(Yo) ___ al instituto en bici.',opts:['voy','vas','va'],ans:'voy',why:'ir: yo → voy'},
   {q:'(Vosotros) ___ los deberes.',opts:['hacéis','hacen','hacemos'],ans:'hacéis',why:'hacer: vosotros'},
   {q:'el lápiz → plural:',opts:['los lápices','los lápizes','los lápiz'],ans:'los lápices',why:'-z → -ces'}]});
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
""" + hub_drills.TYPE_JS + hub_drills.ESCUCHA_JS + hub_drills.LECTURA_JS + r"""
// ---------- Blueprint-oefeningen, luisteren en lezen (uit de inhoudsbronnen) ----------
__BLOQUES__
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

BLOQUES=(hub_bloques.match_js("nat_c6p_match", nat_data.C6P_U0_NAC, per=20)
        +hub_bloques.type_js("nat_c6p_type", nat_data.C6P_U0_NAC_TYPE)
        +hub_bloques.escucha_js("esc_c6p", escucha_data.C6P_U0)
        +hub_bloques.lectura_js("lec_c6p", lectura_data.C6P_U0))
JS=JS.replace("__BLOQUES__", BLOQUES)

# Getypte woordenschat-drills (fase ophalen + produceren) in het paneel zelf.
JS += hub_type_sets.vocab_type_js(vocab)
JS += hub_type_gram.js('C6+', 0)
JS += hub_bloques.retos_js('retos_c6p_u0', 'C6+', 0)
HTML = HTML.replace("__GRAMSLOTS__", hub_type_gram.slots('C6+', 0))
HTML = HTML.replace("__BRONNEN__", extra_bronnen.html("C6+", 0))
# Aantal spellen niet met de hand bijhouden: het verouderde al twee keer.
HTML = HTML.replace("__NGAMES__", str(len(GAMES)))
HTML = HTML.replace("__TYPESLOTS__", hub_type_sets.SLOTS_HTML)

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/C6plus_U0_web.html","w").write(html)
print("C6plus_U0_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
