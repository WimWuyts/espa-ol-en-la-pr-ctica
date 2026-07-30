#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C5 · U4 «Me gusta».
# Eén standalone bestand: fonts base64, de 24 U4-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U4-vocab), visuele/interactieve grammatica (gustar · pronombres · reacciones · querer/poder),
# klikbare kaart (mundo hispano, parada 4 = València) + TTS + inline recorder + Lectura + editbar. Huisstijl groen.
import json, base64, os, sys
import hub_drills
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
GEN = f"{ROOT}/02-huisstijl/beeld/generators"
sys.path.insert(0, GEN); import cast_gen as C; import vocab_icons as VI; import vocab_emoji as VE
vocab = json.load(open(f"{ROOT}/01-cursussen/05-a1/U4/u4_vocab.json", encoding="utf-8"))
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

# ---- de 24 U4-motor-spellen: gegroepeerd (receptief -> productief -> hablar) + base64 ingebed ----
MOTOR = [
 ['① Reconocer · woordenschat', [
   ['gustos-memoria', 'memoria de los gustos', 'memory'],
   ['musica-memoria', 'música y cine', 'memory'],
   ['frecuencia-escala', 'adverbios de frecuencia', 'match']]],
 ['② Distinguir · gramática', [
   ['gusta-gustan', '¿gusta o gustan?', 'classify'],
   ['pronombre-oi', 'el pronombre OI', 'classify'],
   ['reaccion', 'la reacción correcta', 'classify'],
   ['querer-poder', '¿querer o poder?', 'classify'],
   ['porque', '¿por qué o porque?', 'classify']]],
 ['③ Producir con apoyo', [
   ['gusta-cloze', 'completa: gusta o gustan', 'cloze'],
   ['verbo-cloze', 'completa el verbo (gustar/querer/poder)', 'cloze'],
   ['pronombre-cloze', '¿me, te, le…?', 'cloze'],
   ['conectores', 'conectores de opinión', 'cloze'],
   ['presente-tetris', 'presente: serpiente', 'snake'],
   ['tonica', 'la tónica de los gustos', 'tap'],
   ['plan-orden', 'ordena el plan', 'order']]],
 ['④ Analizar & comunicar', [
   ['caza-gustar', 'caza del error (gustar)', 'point'],
   ['pregunta-respuesta', 'pregunta ↔ respuesta', 'match'],
   ['reaccion-match', 'el espejo de reacciones', 'match'],
   ['opina', 'da tu opinión', 'sim']]],
 ['⑤ Hablar · grábate 🎙️', [
   ['repite-gustos', 'escucha y repite', 'speak'],
   ['shadowing-bea', 'shadowing con Bea', 'speak'],
   ['mensaje-plan', 'mensaje de voz: propón un plan', 'speak'],
   ['describe-gustos', 'describe los gustos', 'speak'],
   ['carrusel-gustos', 'carrusel: mis gustos', 'speak']]],
]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-u4-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-u4-{s}.html")}

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
.artists{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 2px}
.artists .ar{flex:1 1 150px;background:var(--gt);border-radius:12px;padding:8px 10px}
.artists .ar b{color:var(--gd)}
.artists .ar small{color:var(--mut);display:block}
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
/* ---- Banda sonora (Cultura · muziek) ---- */
.bandas{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px;margin:8px 0 4px}
.banda{border:1px solid var(--line);border-top:4px solid var(--g);border-radius:14px;padding:12px 14px;background:var(--card);display:flex;flex-direction:column;gap:4px}
.banda .top{display:flex;align-items:center;justify-content:space-between;gap:8px}
.banda .ar{font-family:var(--disp);font-weight:700;font-size:16px;color:var(--gd)}
.banda .fl{font-size:20px;line-height:1}
.banda .sg{font-size:13px;color:var(--ink)}.banda .sg b{color:var(--ww)}
.banda .ge{display:inline-block;background:var(--gt);color:var(--gd);border-radius:20px;padding:2px 9px;font-size:11px;font-weight:600;width:fit-content}
.banda .bio{font-size:12.5px;color:var(--mut);line-height:1.5;margin-top:2px}
.banda .spk-mini{align-self:flex-start;border:none;background:var(--gt);color:var(--gd);border-radius:8px;padding:4px 9px;font-weight:700;cursor:pointer;font-size:12px;margin-top:2px}
.perla{background:linear-gradient(135deg,var(--gt),#fff);border:1px solid var(--g);border-left:6px solid var(--g)}
[data-theme=dark] .perla{background:linear-gradient(135deg,var(--gt),var(--card))}
.escala{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0 2px}
.escala .st{flex:1 1 100px;text-align:center;border-radius:10px;padding:7px 6px;font-size:12px;font-weight:600;border:1.5px solid var(--line)}
.escala .st .em{font-size:20px;display:block}
.musiclinks{display:flex;gap:10px;flex-wrap:wrap;margin-top:6px}
.musiclink{flex:1 1 210px;display:flex;align-items:center;gap:10px;border:1px solid var(--line);border-radius:12px;padding:10px 12px;background:var(--card);text-decoration:none;color:var(--ink)}
.musiclink .ic{font-size:22px}.musiclink b{color:var(--gd);display:block;font-size:14px}.musiclink small{color:var(--mut);font-size:12px}
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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="opinar">expresar gustos</option><option value="ocio">deportes y ocio</option><option value="musica">música y cine</option><option value="sentim">sentimientos</option><option value="frecuencia">frecuencia</option><option value="planes">proponer y quedar</option><option value="valencia">València</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Español en la práctica · U4 Me gusta</title>
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
    <div><h1>U4 · Me gusta</h1>
    <p>La página digital de la Unidad 4 (parada <b>València</b>): flashcards, gramática visual e interactiva, <b>+100 ejercicios</b> con autocorrección y <b>20 juegos</b>. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U4. Klik om te draaien; wissel ES↔NL; filter per groep; klik 🔊 om te horen. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
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
    <p class="lead">Eerst betekenis en patroon ontdekken, dan de regel. Beweeg over de woorden, klik, en probeer. <span class="gloss">Alles binnen het thema van U4: gustar (al revés), pronombres, reacciones y querer/poder.</span></p>
    <div class="card" id="colorsent"></div>
    <div class="card" id="oiconj"></div>
    <h3 class="subh">🧱 Gustar/querer al revés — construye la frase</h3>
    <div class="card ex" id="gx_build"></div>
    <h3 class="subh">⚖️ ¿gusta o gustan? — concordancia</h3>
    <div class="game" id="g_gusta"></div>
    <div class="card ex" id="gx_gustaq"></div>
    <h3 class="subh">🔁 Pronombres OI — me/te/le/nos/os/les</h3>
    <div class="card ex" id="gx_oi"></div>
    <div class="card ex" id="gx_pregresp"></div>
    <h3 class="subh">🪞 Reacciones — también · tampoco · a mí sí/no</h3>
    <div class="game" id="g_reaccion"></div>
    <div class="card ex" id="gx_reac"></div>
    <h3 class="subh">🗓️ Querer · poder + infinitivo (quedar)</h3>
    <div class="card ex" id="gx_querer"></div>
    <h3 class="subh">🎯 Repaso mixto — rellena con feedback</h3>
    <div class="card ex" id="gx_mix"></div>
  </section>

  <section class="panel" data-p="lectura">
    <h2 class="sec">Lectura · perfiles de gustos</h2>
    <p class="lead">Lees de twee muziekprofielen, <b>luister</b> ze (🔊 TTS) en <b>controleer je begrip</b>. Daarna reageer je met je eigen playlist — die neem je op in het tabblad <b>Hablar</b>. <span class="gloss">Keten: lezen → luisteren → spreken.</span></p>
    <div id="lecturawrap"></div>
    <h3 class="subh">🔢 Ordena · plan, frecuencia y mensaje</h3>
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
    <div class="card" id="rec_repite"></div>
    <div class="card" id="rec_carrusel"></div>
    <div class="card" id="rec_mensaje"></div>
    <p class="lead" style="margin-top:8px">Meer spreek-/opnamespellen (shadowing, describe…) vind je ook onder <b>Juegos ⑤</b>.</p>
  </section>

  <section class="panel" data-p="cultura">
    <h2 class="sec">Cultura · El ocio y la música</h2>
    <p class="lead">En el mundo hispano <b>la música une a la gente</b>. Descubre a <b>Rosalía</b> y qué hacen los jóvenes en su tiempo libre. <span class="gloss">In de Spaanstalige wereld verbindt muziek; ontdek Rosalía en de vrije tijd van jongeren.</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>Rosalía 🎵 🇪🇸</h3>
      <p>Cantante de <b>Barcelona</b>. Mezcla <b>flamenco</b> con pop y reguetón. Álbumes famosos: <i>El mal querer</i>, <i>Motomami</i>. Canta en español. <span class="gloss">Een brug tussen traditie en de charts van vandaag — perfect voor de klas. El español es de los idiomas más escuchados en las plataformas de música.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="6" x2="10" y1="11" y2="11"/><line x1="8" x2="8" y1="9" y2="13"/><line x1="15" x2="15.01" y1="12" y2="12"/><line x1="18" x2="18.01" y1="10" y2="10"/><path d="M17.32 5H6.68a4 4 0 0 0-3.978 3.59c-.006.052-.01.101-.017.152C2.604 9.416 2 14.456 2 16a3 3 0 0 0 3 3c1 0 1.5-.5 2-1l1.414-1.414A2 2 0 0 1 9.828 16h4.344a2 2 0 0 1 1.414.586L17 18c.5.5 1 1 2 1a3 3 0 0 0 3-3c0-1.545-.604-6.584-.685-7.258-.007-.05-.011-.1-.017-.151A4 4 0 0 0 17.32 5z"/></svg>El ocio joven 🏖️</h3>
      <p>Jongeren <b>salen con amigos</b>, escuchan música, ven series, hacen deporte y van a la playa. En <b>València</b>: las Fallas, la paella y la horchata. <span class="gloss">Muziek en samen zijn staan centraal. Contraste: el flamenco (tradición) ↔ el reguetón (actual).</span></p></div>
    <h3 class="subh">🎧 Banda sonora — leer Spaans via muziek die jullie kennen</h3>
    <div class="card">
      <p><b>ES:</b> Cada unidad tiene una <b>banda sonora</b>: canciones de artistas que suenan ahora. <b>Escucha, canta y aprende</b> palabras nuevas. Para esta unidad («Me gusta») usamos estrellas de España y de Latinoamérica. <span class="gloss">Elke unit heeft een banda sonora: nummers van artiesten van nu. Luister, zing mee en pik nieuwe woorden op — perfect voor «me gusta / me encanta».</span></p>
      <div class="bandas" id="bandas"></div>
      <p class="gloss" style="margin:8px 0 0">🔊 Klik op een kaartje om de artiest + het nummer te horen (TTS). Alle nummers staan in de klas-playlist hieronder.</p>
    </div>
    <div class="card perla"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px">⭐ «La Perla» — Rosalía 🇪🇸 <span class="ge" style="display:inline-block;background:var(--gt);color:var(--gd);border-radius:20px;padding:2px 9px;font-size:11px;font-weight:600">canción de la unidad</span></h3>
      <p><b>ES:</b> «La Perla» está en el álbum <b>LUX (2025)</b> de Rosalía. La canción habla, con humor, de una persona que no es de fiar («una perla»). <b>Escúchala</b> y di en la escala: ¿la <b>odias</b>, <b>no te gusta</b>, <b>te gusta</b> o <b>te encanta</b>? <span class="gloss">Uit het album LUX (2025). Gebruik de gustar-schaal om je mening te geven — dé U4-structuur.</span></p>
      <div class="escala">
        <div class="st" style="background:#fde8e8;border-color:#f5b5b5"><span class="em">😡</span>La odio</div>
        <div class="st" style="background:#fef3c7;border-color:#f3d98b"><span class="em">🙁</span>No me gusta</div>
        <div class="st" style="background:#e0f2e9;border-color:#9fd9bf"><span class="em">🙂</span>Me gusta</div>
        <div class="st" style="background:#d1fadf;border-color:#6fd39b"><span class="em">😍</span>Me encanta</div>
      </div>
      <p class="gloss" style="margin:6px 0 0">Parel uit het vorige project (PAREL-4). Beluister ze via de playlist of LyricsTraining hieronder, en gebruik daarna «gustar» om te reageren.</p></div>
    <h3 class="subh">🎼 La playlist de la clase · canta con LyricsTraining</h3>
    <div class="card">
      <p><b>ES:</b> Escucha la playlist, y <b>completa la letra mientras escuchas</b> en LyricsTraining. También puedes ver los vídeos de las canciones. <span class="gloss">Luister naar de playlist en vul de songtekst aan terwijl je luistert (LyricsTraining). Extern = link.</span></p>
      <div class="musiclinks">
        <a class="musiclink" href="https://open.spotify.com/search/Rosal%C3%ADa%20Karol%20G%20Bad%20Bunny%20Quevedo%20Feid%20Shakira" target="_blank" rel="noopener"><span class="ic">🟢</span><span><b>Spotify · la playlist de la clase</b><small>Rosalía · Karol G · Bad Bunny · Quevedo · Feid · Shakira — scan de QR in het boek of open Spotify.</small></span></a>
        <a class="musiclink" href="https://lyricstraining.com/es" target="_blank" rel="noopener"><span class="ic">🎤</span><span><b>LyricsTraining</b><small>Kies een nummer en vul de tekst aan terwijl je luistert (niveau «beginner»/«fácil»).</small></span></a>
        <a class="musiclink" href="https://www.youtube.com/results?search_query=Rosal%C3%ADa+La+Perla" target="_blank" rel="noopener"><span class="ic">▶️</span><span><b>Los vídeos</b><small>Videoclips van de nummers — via YouTube (leerkracht kiest de klasversie).</small></span></a>
      </div></div>
    <h3 class="subh">📍 La Ruta · ¿dónde estamos?</h3>
    <p class="lead">Onze parada 4: <b>València</b> 🇪🇸 (la costa). <b>Klik op een groen land</b> op de kaart voor info. Verderop: México → Colombia → Perú.</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een groen land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    <h2 class="sec">Extra · bronnen</h2>
    <p class="lead">Externe uitleg &amp; oefeningen (de leerkracht vult de links aan).</p>
    <div class="card"><p>🎬 <b>profedeele</b> (YouTube — el verbo gustar / los pronombres) — <span class="gloss">link volgt.</span></p>
    <p>🧩 <b>arche-ele</b> (Genially — gustos / ocio / música) — <span class="gloss">link volgt.</span></p>
    <p>📄 In het boek (PDF) verwijzen de QR-codes naar déze pagina, op het juiste ankerpunt.</p></div>
  </section>

  <div class="foot">Español en la práctica · C5 · Unidad 4 «Me gusta» — página digital. Uitbreiding op de PDF · huisstijl groen · print ↔ PowerPoint ↔ web.</div>
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

// ---- GRAMMAR-VIZ 1: kleurgecodeerde gustar-zin (al revés) ----
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Gustar — al revés: «het bevalt mij»</h3>'+
'<div class="csent">'+
'<span style="background:#dcfce7;color:#166534">A mí<span class="tip">aan mij (OI)</span></span> '+
'<span style="background:#dbeafe;color:#1e40af">me<span class="tip">meewerkend voorwerp · a mí</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">gusta<span class="tip">3ª pers. · 1 ding/infinitivo</span></span> '+
'<span style="background:#ccfbf1;color:#0f766e">la música<span class="tip">= het ONDERWERP</span></span> y '+
'<span style="background:#dbeafe;color:#1e40af">me<span class="tip">a mí</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">gustan<span class="tip">meervoud → -n</span></span> '+
'<span style="background:#ccfbf1;color:#0f766e">los deportes<span class="tip">= meervoudig onderwerp</span></span>.</div>'+
'<div class="legend"><span><i style="background:#86efac"></i>a + persoon</span><span><i style="background:#93c5fd"></i>pronombre OI</span><span><i style="background:#fdba74"></i>gusta/gustan</span><span><i style="background:#5eead4"></i>onderwerp (het ding)</span></div>'+
'<p class="gloss" style="margin-top:8px">🔴 In het NL: «<b>ik</b> vind muziek leuk». In het ES staat het om: «de muziek <b>bevalt mij</b>». gusta<b>n</b> bij meervoud! · '+(TTS?'<button class="spk-btn" onclick="speak(\'A mí me gusta la música y me gustan los deportes\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: los pronombres OI — klik om te onthullen ----
(function(){const el=document.getElementById('oiconj');
 const R=[['a mí','me'],['a ti','te'],['a él/ella/usted','le'],['a nosotros/-as','nos'],['a vosotros/-as','os'],['a ellos/-as/ustedes','les']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Los pronombres OI — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">Denk eerst zelf: welk woord hoort bij de persoon? Klik dan de kaart.</p><div class="conjgrid" id="ocg"></div>';
 const g=el.querySelector('#ocg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v+' gusta…';if(TTS)speak(p+' '+v+' gusta');};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: ¿gusta o gustan? ----
function gameGusta(){const el=document.getElementById('g_gusta');
 const items=[['el fútbol','gusta'],['los deportes','gustan'],['bailar','gusta'],['las series','gustan'],['la playa','gusta'],['los videojuegos','gustan'],['escuchar música','gusta'],['las canciones','gustan']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿gusta o gustan?</h3><p class="desc">Kies de juiste vorm. Eén ding of een infinitief → <b>gusta</b>; meerdere → <b>gustan</b>.</p>'+scoreBar('sbG')+'<div id="gW" style="font-size:24px;font-family:var(--disp);text-align:center;margin:8px 0">Me ___ <b></b></div><div class="chips" style="justify-content:center"><div class="chip" onclick="window._gustaG(\'gusta\')">gusta</div><div class="chip" onclick="window._gustaG(\'gustan\')">gustan</div></div><div class="fb" id="gFb"></div>';
 const sb=el.querySelector('#sbG');
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#gW b').textContent=el.cur[0];el.querySelector('#gFb').className='fb';}
 window._gustaG=k=>{const ok=k===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#gFb'),ok,(ok?'¡Sí! ':'Nee → ')+'Me '+el.cur[1]+' '+el.cur[0]+'.');setTimeout(next,850);};
 next();}
// ---- GRAMMAR-VIZ 4: la reacción (también/tampoco/a mí sí/a mí no) ----
function gameReaccion(){const el=document.getElementById('g_reaccion');
 // [frase, positief?, akkoord? -> juiste reactie]
 const items=[['Me gusta el mar.',true,'también'],['No me gusta el frío.',false,'tampoco'],['Me encanta bailar.',true,'también'],['No me gustan los lunes.',false,'tampoco'],['Me gustan los videojuegos.',true,'también'],['No me gusta madrugar.',false,'tampoco']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>El espejo de reacciones</h3><p class="desc">Reageer om <b>akkoord</b> te gaan met de spreker (+ → también · – → tampoco).</p>'+scoreBar('sbR')+'<div id="rQ" style="font-size:19px;font-family:var(--disp);text-align:center;margin:10px 0"></div><div class="chips" id="rC" style="justify-content:center"></div><div class="fb" id="rFb"></div>';
 const sb=el.querySelector('#sbR');const cont=el.querySelector('#rC');
 ['A mí también','A mí tampoco'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c.includes('también')?'también':'tampoco');cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#rQ').textContent='«'+el.cur[0]+'»';el.querySelector('#rFb').className='fb';}
 function guess(c){const ok=c===el.cur[2];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#rFb'),ok,(ok?'¡Sí! ':'Nee → ')+'«'+el.cur[0]+'» ('+(el.cur[1]?'+':'–')+') → A mí '+el.cur[2]+'.');setTimeout(next,1000);}
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
   const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "🎵 Música: el mariachi y el corrido", "star": 0, "nl": ""}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "🎵 Música: el flamenco y el pop de Rosalía", "star": 1, "nl": "★ ¡Estás aquí! Parada U0–U4 · Madrid · Sevilla · Barcelona · València"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "🎵 Música: la cumbia, el vallenato y el reguetón", "star": 0, "nl": ""}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "🎵 Música: el huayno andino y la música criolla", "star": 0, "nl": ""}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "🎵 Música: el tango y el rock nacional", "star": 0, "nl": ""}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "🎵 Música: el joropo y la gaita", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "🎵 Música: la cueca, baile nacional", "star": 0, "nl": ""}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "🎵 Música: el pasillo, canción típica", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "🎵 Música: la marimba, instrumento nacional", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "🎵 Música: el son, la salsa y la rumba", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "🎵 Música: música andina con charango y zampoña", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "🎵 Música: el merengue y la bachata", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "🎵 Música: la punta garífuna", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "🎵 Música: el arpa paraguaya y la guarania", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "🎵 Música: el son nica y la marimba", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "🎵 Música: la cumbia y las «xuc»", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "🎵 Música: el calypso y la música guanacasteca", "star": 0, "nl": ""}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "🎵 Música: la salsa de Rubén Blades y el tamborito", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "🎵 Música: el candombe con tambores", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "🎵 Música: el reguetón y la salsa", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "🎵 Música: ritmos africanos y el «malamba»", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "🎵 Música: el latin pop y el hip-hop en español", "star": 0, "nl": ""}};
 const wrap=document.getElementById('mapwrap');const svg=wrap.querySelector('svg');const box=document.getElementById('mapinfo');
 if(!svg)return;
 svg.querySelectorAll('path.spa, path.usa').forEach(p=>{p.style.cursor='pointer';
   p.addEventListener('mouseenter',()=>{p.style.opacity='.75'});p.addEventListener('mouseleave',()=>{p.style.opacity=''});
   p.addEventListener('click',()=>{const c=p.getAttribute('data-c');const d=INFO[c];if(!d)return;
     box.innerHTML='<h3>'+d.fl+' '+d.n+' <span style="font-size:13px;color:var(--mut);font-weight:400">('+c+')</span>'+(d.star?' ★':'')+'</h3>'+'<div class="mrow"><b>🏛️ Capital:</b> '+d.cap+'</div>'+'<div class="mrow"><b>👥 Población:</b> '+d.pob+'</div>'+'<div class="mrow"><b>💰 Moneda:</b> '+d.mon+'</div>'+'<div class="mrow"><b>🗣️ Gentilicio:</b> '+d.gen+'</div>'+'<div class="mrow"><b>🌐 Idioma:</b> '+d.idi+'</div>'+(d.tema?'<div style="margin-top:8px;padding:8px 11px;background:rgba(255,255,255,.7);border-left:4px solid var(--gd);border-radius:7px;font-weight:600;color:var(--gd)">'+d.tema+'</div>':'')+(d.cool?'<div style="margin-top:8px;font-size:13px;line-height:1.5"><b>💡 ¿Sabías que…?</b> '+d.cool+'</div>':'')+(d.nl?'<div class="gloss" style="margin-top:6px">'+d.nl+'</div>':'');
     box.scrollIntoView({behavior:'smooth',block:'nearest'});});
 });
})();

// ---------- LECTURA: perfiles de música + TTS + begrip ----------
function renderLectura(){const el=document.getElementById('lecturawrap');if(!el)return;
 const P=[{n:'Lucía',fr:'Sevilla 🇪🇸',t:'¡Hola! Me <span class="ev">encanta la música</span>. Mi artista favorita es <span class="ev">Rosalía</span>, ¡me gustan todas sus canciones! También me <span class="ev">gusta bailar</span> flamenco. Los fines de semana <span class="ev">voy a la playa</span> con amigos. No me gustan los videojuegos, prefiero salir. ¿Y a ti, qué te gusta?'},
  {n:'Diego',fr:'CDMX 🇲🇽',t:'¡Qué onda! A mí me <span class="ev">gusta el reguetón</span> y me <span class="ev">encantan los videojuegos</span>. Toco un poco la <span class="ev">guitarra</span>. No me gusta bailar, pero me gusta escuchar música todos los días. Los sábados quiero <span class="ev">ver películas de acción</span>. ¡Escríbeme tu playlist!'}];
 const strip=h=>h.replace(/<[^>]+>/g,'');
 el.innerHTML='<div class="perfiles">'+P.map((p,i)=>'<div class="perfil"><h4>🎵 '+p.n+' <span class="gloss" style="font-size:12px;font-weight:400">· '+p.fr+'</span> '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lx'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div class="txt" id="lx'+i+'" data-raw="'+strip(p.t).replace(/"/g,'&quot;')+'">'+p.t+'</div></div>').join('')+'</div>';
 const items=[['A Lucía le encanta Rosalía.',true,'«me encanta … Rosalía»'],['A Diego le gustan los videojuegos.',true,'«me encantan los videojuegos»'],['A los dos les gusta bailar.',false,'a Diego no le gusta bailar'],['Diego escucha música todos los días.',true,'«escuchar música todos los días»']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — comprueba tu comprensión</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Responde</h3><p class="gloss" style="margin:0 0 8px">Kies één profiel en antwoord met je eigen gustos. Neem het op onder <b>Hablar 🎙️</b> («mensaje de voz»).</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="¡Hola! A mí me gusta…"></textarea>';
 el.appendChild(box);el.appendChild(resp);}

// ---------- INLINE RECORDER (MediaRecorder) ----------
""" + hub_drills.RECORDER_JS + r"""
function buildRecorders(){
 makeRecorder('rec_repite',{title:'Escucha y repite: mis gustos',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'Me gusta la música.',cue:'gusto',tip:'Duidelijk uitgesproken? Probeer nog eens.'},{text:'Me gustan los deportes.',cue:'gustan (mv.)'},{text:'Me encanta bailar.',cue:'encanta + infinitivo'},{text:'No me gusta el fútbol.',cue:'negatief'},{text:'¿Y a ti, qué te gusta?',cue:'interacción'}]});
 makeRecorder('rec_carrusel',{title:'Carrusel: mis gustos',desc:'Eén element wisselt per ronde. Bouw de zin, spreek ze in.',items:[
   {text:'Me gusta la playa porque es relajante.',cue:'ronda 1'},{text:'Me gustan los conciertos porque son divertidos.',cue:'ronda 2'},{text:'Me gusta ___ porque es ___.',cue:'jouw versie'}]});
 makeRecorder('rec_mensaje',{title:'Mensaje de voz: propón un plan',desc:'Neem één bericht op. Ontvanger: Lucía/Diego · Doel: een plan voorstellen. Gebruik: ¿Quieres…? · ¿Podemos…? · quedamos a las…',items:[
   {text:'Propón un plan para el fin de semana (30 s).',cue:'para · Lucía / Diego',tip:'Heb je een plan + een uur gezegd? Neem opnieuw op.'}]});
}

// ---------- BANDA SONORA (Cultura · muziek) ----------
function renderBandas(){const el=document.getElementById('bandas');if(!el)return;
 const A=[
  {ar:'Rosalía',fl:'🇪🇸',song:'La Perla',ge:'flamenco + pop',bio:'Es de <b>Barcelona</b> y mezcla el <b>flamenco</b> con pop y música urbana. Sus álbumes «Motomami» y «LUX» son famosos en todo el mundo. Canta casi siempre en español. <span style="color:var(--mut)">Brug tussen traditie en de charts van nu.</span>'},
  {ar:'Karol G',fl:'🇨🇴',song:'Si antes te hubiera conocido',ge:'reguetón',bio:'«La Bichota» es de <b>Medellín (Colombia)</b>. Es una de las reinas del <b>reguetón</b>. Llena estadios por toda América y Europa. <span style="color:var(--mut)">Herkenbare hits, ideaal om «me encanta» te oefenen.</span>'},
  {ar:'Bad Bunny',fl:'🇵🇷',song:'Baile inolvidable',ge:'reguetón / trap',bio:'Es de <b>Puerto Rico</b> y es la estrella más escuchada del <b>reguetón</b> y el trap. Defiende el español y su cultura caribeña. Su álbum «Debí tirar más fotos» (2025) es un éxito. <span style="color:var(--mut)">Bewijs dat Spaanstalige muziek de wereld verovert.</span>'},
  {ar:'Shakira',fl:'🇨🇴',song:'Hips Don’t Lie',ge:'pop latino',bio:'Es de <b>Barranquilla (Colombia)</b> y canta en español e inglés. Mezcla pop, rock y ritmos latinos desde hace más de 20 años. <span style="color:var(--mut)">Klassieker die elke generatie kent.</span>'},
  {ar:'Feid',fl:'🇨🇴',song:'Luna',ge:'reguetón',bio:'«Ferxxo» es de <b>Medellín</b> y hace <b>reguetón</b> moderno y relajado. Es muy popular entre los jóvenes. <span style="color:var(--mut)">Handig voor gustos + adjetivos (relajante, guay).</span>'},
  {ar:'Quevedo',fl:'🇪🇸',song:'Quédate',ge:'trap / urbano',bio:'Es de las <b>Islas Canarias (España)</b>. Hace música <b>urbana</b> y trap. Su «Bzrp Session #52» batió récords. <span style="color:var(--mut)">Actueel Spaans van een jonge artiest.</span>'}];
 el.innerHTML=A.map(a=>'<div class="banda" tabindex="0" data-say="'+(a.ar+', '+a.song).replace(/"/g,'&quot;')+'"><div class="top"><span class="ar">'+a.ar+'</span><span class="fl">'+a.fl+'</span></div><div class="sg">🎵 <b>'+a.song+'</b></div><span class="ge">'+a.ge+'</span><div class="bio">'+a.bio+'</div>'+(TTS?'<button class="spk-mini" type="button">🔊 escuchar</button>':'')+'</div>').join('');
 el.querySelectorAll('.banda').forEach(c=>{const say=c.dataset.say;const go=()=>{if(TTS)speak(say);};
   const b=c.querySelector('.spk-mini');if(b)b.onclick=e=>{e.stopPropagation();go();};
   c.onclick=go;c.onkeydown=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();go();}};});}

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

function buildInlineExercises(){
 // ---------- GRAMÁTICA ----------
 buildOrder('gx_build',{title:'Construye: gustar / querer al revés',desc:'Tik de blokjes in de juiste volgorde (a + persona → pronombre → verbo → resto).',rounds:[
   {sub:'a mí · gustar (ev.)',items:[{label:'A mí',key:1},{label:'me',key:2},{label:'gusta',key:3},{label:'la música',key:4}]},
   {sub:'a mí · gustar (mv.)',items:[{label:'A mí',key:1},{label:'me',key:2},{label:'gustan',key:3},{label:'los deportes',key:4}]},
   {sub:'a Lucía · encantar',items:[{label:'A Lucía',key:1},{label:'le',key:2},{label:'encanta',key:3},{label:'bailar',key:4}]},
   {sub:'querer + infinitivo',items:[{label:'(Yo)',key:1},{label:'quiero',key:2},{label:'ir',key:3},{label:'al cine',key:4}]},
   {sub:'poder + infinitivo',items:[{label:'¿(Tú)',key:1},{label:'puedes',key:2},{label:'quedar',key:3},{label:'el sábado?',key:4}]},
   {sub:'quedar · la hora',items:[{label:'Quedamos',key:1},{label:'a las',key:2},{label:'cinco',key:3},{label:'en la playa',key:4}]}]});
 buildChoice('gx_gustaq',{title:'Mini-quiz: ¿gusta o gustan?',desc:'Eén ding of infinitief → gusta · meerdere dingen → gustan.',per:6,pool:[
   {q:'A mí me ___ la música.',opts:['gusta','gustan'],ans:'gusta',why:'la música = 1 ding'},
   {q:'A mí me ___ los deportes.',opts:['gustan','gusta'],ans:'gustan',why:'los deportes = mv.'},
   {q:'A ti te ___ bailar.',opts:['gusta','gustan'],ans:'gusta',why:'infinitivo → gusta'},
   {q:'A ella le ___ las canciones.',opts:['gustan','gusta'],ans:'gustan',why:'las canciones = mv.'},
   {q:'Nos ___ la playa.',opts:['gusta','gustan'],ans:'gusta',why:'la playa = ev.'},
   {q:'Me ___ los videojuegos.',opts:['gustan','gusta'],ans:'gustan',why:'los videojuegos = mv.'},
   {q:'Le ___ escuchar música.',opts:['gusta','gustan'],ans:'gusta',why:'infinitivo → gusta'},
   {q:'¿Te ___ las series?',opts:['gustan','gusta'],ans:'gustan',why:'las series = mv.'},
   {q:'Me ___ el fútbol.',opts:['gusta','gustan'],ans:'gusta',why:'el fútbol = ev.'},
   {q:'Os ___ los conciertos.',opts:['gustan','gusta'],ans:'gustan',why:'los conciertos = mv.'}]});
 buildChoice('gx_oi',{title:'Mini-quiz: el pronombre OI',desc:'Welk voornaamwoord hoort bij de persoon? (a mí → me · a ti → te · a él/ella → le · a nosotros → nos · a vosotros → os · a ellos → les)',per:6,pool:[
   {q:'A mí ___ gusta el mar.',opts:['me','te','le'],ans:'me',why:'a mí → me'},
   {q:'A ti ___ gustan los deportes.',opts:['te','me','le'],ans:'te',why:'a ti → te'},
   {q:'A Lucía ___ encanta bailar.',opts:['le','me','les'],ans:'le',why:'a ella → le'},
   {q:'A nosotros ___ gusta la playa.',opts:['nos','os','les'],ans:'nos',why:'a nosotros → nos'},
   {q:'A vosotros ___ gusta el cine.',opts:['os','nos','les'],ans:'os',why:'a vosotros → os'},
   {q:'A ellos ___ gustan las series.',opts:['les','le','nos'],ans:'les',why:'a ellos → les'},
   {q:'A Diego ___ gusta el reguetón.',opts:['le','les','te'],ans:'le',why:'a él → le'},
   {q:'A mí ___ encanta la música.',opts:['me','le','nos'],ans:'me',why:'a mí → me'},
   {q:'¿A ti ___ gusta nadar?',opts:['te','le','os'],ans:'te',why:'a ti → te'},
   {q:'A mis amigos ___ gusta la playa.',opts:['les','le','nos'],ans:'les',why:'a ellos → les'}]});
 buildMatch('gx_pregresp',{title:'Empareja: pregunta ↔ respuesta',desc:'Koppel elke vraag/uitspraak aan de logische reactie.',per:6,pool:[
   {a:'¿Te gusta bailar?',b:'Sí, me encanta.'},
   {a:'¿Qué música te gusta?',b:'El pop y el reguetón.'},
   {a:'¿Quieres ir al cine?',b:'Vale, ¿a qué hora?'},
   {a:'¿A qué hora quedamos?',b:'A las cinco.'},
   {a:'No me gusta el fútbol.',b:'A mí tampoco.'},
   {a:'Me encanta la playa.',b:'A mí también.'},
   {a:'¿Puedes el sábado?',b:'Sí, puedo.'},
   {a:'¿Por qué no vamos a nadar?',b:'¡Buena idea!'}]});
 buildChoice('gx_reac',{title:'Reacciona: también · tampoco · a mí sí/no',desc:'Kies de juiste reactie. Akkoord bij + → también · akkoord bij – → tampoco · NIET akkoord → a mí sí / a mí no.',per:6,pool:[
   {q:'—Me gusta el mar. —A mí ___. (je bent het EENS, +)',opts:['también','tampoco','no'],ans:'también',why:'akkoord + → A mí también'},
   {q:'—No me gusta el frío. —A mí ___. (EENS, –)',opts:['tampoco','también','sí'],ans:'tampoco',why:'akkoord – → A mí tampoco'},
   {q:'—Me encanta bailar. —A mí ___. (NIET eens)',opts:['no','también','tampoco'],ans:'no',why:'oneens met + → A mí no'},
   {q:'—No me gustan los lunes. —A mí ___. (NIET eens)',opts:['sí','tampoco','también'],ans:'sí',why:'oneens met – → A mí sí'},
   {q:'—Me gustan los videojuegos. —A mí ___. (EENS, +)',opts:['también','tampoco','sí'],ans:'también',why:'akkoord + → también'},
   {q:'—No me gusta madrugar. —A mí ___. (EENS, –)',opts:['tampoco','también','no'],ans:'tampoco',why:'akkoord – → tampoco'},
   {q:'—Me encanta la música. —A mí ___. (NIET eens)',opts:['no','sí','tampoco'],ans:'no',why:'oneens met + → A mí no'},
   {q:'—No me gusta el fútbol. —A mí ___. (NIET eens)',opts:['sí','no','también'],ans:'sí',why:'oneens met – → A mí sí'},
   {q:'—Me gusta la playa. —A mí ___. (EENS, +)',opts:['también','tampoco','sí'],ans:'también',why:'akkoord + → también'},
   {q:'—No me gustan las series. —A mí ___. (EENS, –)',opts:['tampoco','también','no'],ans:'tampoco',why:'akkoord – → tampoco'}]});
 buildChoice('gx_querer',{title:'Completa: querer / poder + infinitivo',desc:'Kies de juiste vorm van het werkwoord tussen haakjes (e>ie querer · o>ue poder).',per:6,pool:[
   {q:'(querer · yo) ___ ir a la playa.',opts:['quiero','quieres','quiere'],ans:'quiero',why:'yo → quiero'},
   {q:'(querer · tú) ¿___ quedar el sábado?',opts:['quieres','quiero','quiere'],ans:'quieres',why:'tú → quieres'},
   {q:'(querer · ella) Lucía ___ ver una película.',opts:['quiere','quieres','quieren'],ans:'quiere',why:'ella → quiere'},
   {q:'(poder · tú) ¿___ venir a las cinco?',opts:['puedes','puedo','puede'],ans:'puedes',why:'tú → puedes'},
   {q:'(poder · yo) Hoy no ___, lo siento.',opts:['puedo','puedes','puede'],ans:'puedo',why:'yo → puedo'},
   {q:'(poder · nosotros) ¿___ quedar mañana?',opts:['podemos','podéis','pueden'],ans:'podemos',why:'nosotros → podemos'},
   {q:'(querer · nosotros) ___ ir al cine.',opts:['queremos','queréis','quieren'],ans:'queremos',why:'nosotros → queremos'},
   {q:'(poder · ellos) Ellos ___ jugar hoy.',opts:['pueden','podemos','puede'],ans:'pueden',why:'ellos → pueden'},
   {q:'(querer · tú) ¿Qué ___ hacer?',opts:['quieres','quiere','quieren'],ans:'quieres',why:'tú → quieres'},
   {q:'(poder · ella) Nina ___ tocar la guitarra.',opts:['puede','puedes','pueden'],ans:'puede',why:'ella → puede'}]});
 buildChoice('gx_mix',{title:'Repaso mixto: rellena',desc:'Alles door elkaar: gusta/gustan · pronombres OI · reacciones · querer/poder.',per:8,pool:[
   {q:'A mí me ___ los deportes.',opts:['gustan','gusta'],ans:'gustan',why:'mv. → gustan'},
   {q:'A Lucía ___ encanta bailar.',opts:['le','me','les'],ans:'le',why:'a ella → le'},
   {q:'—Me gusta el mar. —A mí ___.',opts:['también','tampoco','sí'],ans:'también',why:'akkoord + → también'},
   {q:'(querer · yo) ___ ir a la playa.',opts:['quiero','quieres','quiere'],ans:'quiero',why:'yo → quiero'},
   {q:'A mí me ___ la música pop.',opts:['gusta','gustan'],ans:'gusta',why:'ev. → gusta'},
   {q:'—No me gusta el frío. —A mí ___.',opts:['tampoco','también','no'],ans:'tampoco',why:'akkoord – → tampoco'},
   {q:'(poder · tú) ¿___ quedar hoy?',opts:['puedes','puedo','puede'],ans:'puedes',why:'tú → puedes'},
   {q:'A nosotros ___ gusta la playa.',opts:['nos','os','les'],ans:'nos',why:'a nosotros → nos'},
   {q:'¿Te ___ las series?',opts:['gustan','gusta'],ans:'gustan',why:'las series = mv.'},
   {q:'—Me encanta la música. —A mí ___. (NIET eens)',opts:['no','también','tampoco'],ans:'no',why:'oneens met + → A mí no'},
   {q:'(querer · ella) Lucía ___ ver una peli.',opts:['quiere','quieres','quieren'],ans:'quiere',why:'ella → quiere'},
   {q:'A ti ___ gusta nadar, ¿verdad?',opts:['te','me','le'],ans:'te',why:'a ti → te'}]});
 // ---------- VOCABULARIO ----------
 buildMatch('vx_match',{title:'Empareja: palabra ↔ emoji',desc:'Koppel het Spaanse woord aan het juiste beeld.',per:6,pool:[
   {a:'el fútbol',b:'⚽'},{a:'el baloncesto',b:'🏀'},{a:'nadar',b:'🏊'},{a:'bailar',b:'💃'},
   {a:'el videojuego',b:'🎮'},{a:'leer',b:'📖'},{a:'la playa',b:'🏖️'},{a:'la música',b:'🎵'},
   {a:'la guitarra',b:'🎸'},{a:'la película',b:'🎬'},{a:'el/la cantante',b:'🎤'},{a:'el cine',b:'🎥'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat in de zin past.',per:6,pool:[
   {q:'En mi ___ libre escucho música.',opts:['tiempo','plan','mar'],ans:'tiempo',why:'el tiempo libre'},
   {q:'Rosalía es una ___ española.',opts:['cantante','playa','serie'],ans:'cantante',why:'la cantante'},
   {q:'Me gusta ___ en el mar.',opts:['nadar','leer','tocar'],ans:'nadar',why:'nadar en el mar'},
   {q:'Toco la ___ en un grupo.',opts:['guitarra','película','costa'],ans:'guitarra',why:'tocar la guitarra'},
   {q:'Veo una ___ de acción en el cine.',opts:['película','canción','banda'],ans:'película',why:'la película'},
   {q:'La ___ de la canción es muy bonita.',opts:['letra','playa','paella'],ans:'letra',why:'la letra = songtekst'},
   {q:'Los fines de semana ___ con amigos.',opts:['salgo','odio','prefiero'],ans:'salgo',why:'salir con amigos'},
   {q:'València está en la ___.',opts:['costa','serie','banda'],ans:'costa',why:'la costa'},
   {q:'Una película ___ me pone nervioso.',opts:['emocionante','aburrida','relajante'],ans:'emocionante',why:'emocionante = spannend'},
   {q:'El mar es muy ___.',opts:['relajante','divertido','genial'],ans:'relajante',why:'el mar = relajante'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het juiste woord.',per:6,pool:[
   {q:'Persona que canta canciones:',opts:['el/la cantante','el/la artista','el grupo'],ans:'el/la cantante',why:'cantante = zanger(es)'},
   {q:'Deporte con un balón y una portería:',opts:['el fútbol','el baloncesto','la playa'],ans:'el fútbol',why:'fútbol'},
   {q:'Lugar con arena y mar:',opts:['la playa','el cine','la banda'],ans:'la playa',why:'la playa'},
   {q:'Adjetivo: lo contrario de «divertido»:',opts:['aburrido','genial','emocionante'],ans:'aburrido',why:'aburrido = saai'},
   {q:'La usas para hacer música con las manos:',opts:['la guitarra','la letra','la serie'],ans:'la guitarra',why:'la guitarra'},
   {q:'Historia en capítulos que ves en la tele:',opts:['la serie','la película','la canción'],ans:'la serie',why:'la serie'},
   {q:'Fiesta típica de València en marzo:',opts:['las Fallas','la horchata','la paella'],ans:'las Fallas',why:'las Fallas'},
   {q:'Verbo: moverse con la música:',opts:['bailar','leer','nadar'],ans:'bailar',why:'bailar = dansen'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['el fútbol','el baloncesto','nadar','la canción'],odd:3,why:'la canción = música, geen deporte'},
   {words:['la música','la canción','la letra','la playa'],odd:3,why:'la playa hoort niet bij música'},
   {words:['divertido','aburrido','genial','bailar'],odd:3,why:'bailar = werkwoord, geen adjectief'},
   {words:['siempre','a veces','nunca','guitarra'],odd:3,why:'guitarra = geen frecuencia'},
   {words:['querer','poder','quedar','playa'],odd:3,why:'playa = zelfst. nw., geen ww. van planes'},
   {words:['la paella','la horchata','las Fallas','el reguetón'],odd:3,why:'el reguetón is niet van València'},
   {words:['me gusta','me encanta','odio','nadar'],odd:3,why:'nadar = activiteit, geen mening'},
   {words:['también','tampoco','a mí sí','cantante'],odd:3,why:'cantante = geen reactiewoord'}]});
 // ---------- LECTURA ----------
 buildOrder('lx_order',{title:'Ordena',desc:'Tik de items in de juiste volgorde.',rounds:[
   {sub:'proponer un plan (una conversación)',items:[{label:'¿Quieres ir a la playa?',key:1},{label:'Sí, ¡buena idea!',key:2},{label:'¿A qué hora quedamos?',key:3},{label:'A las cinco. ¡Vale!',key:4}]},
   {sub:'la frecuencia: de – a +',items:[{label:'nunca',key:1},{label:'casi nunca',key:2},{label:'a veces',key:3},{label:'a menudo',key:4},{label:'siempre',key:5}]},
   {sub:'un mensaje de gustos',items:[{label:'¡Hola!',key:1},{label:'Me encanta la música.',key:2},{label:'¿Y a ti, qué te gusta?',key:3},{label:'¡Un abrazo!',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in de twee perfiles (Lucía y Diego) en kies het juiste antwoord.',per:6,pool:[
   {q:'¿Quién es la artista favorita de Lucía?',opts:['Rosalía','Karol G','Shakira'],ans:'Rosalía',why:'«Mi artista favorita es Rosalía»'},
   {q:'¿Qué le encanta a Diego?',opts:['los videojuegos','bailar flamenco','la playa'],ans:'los videojuegos',why:'«me encantan los videojuegos»'},
   {q:'¿Qué instrumento toca Diego?',opts:['la guitarra','el piano','la batería'],ans:'la guitarra',why:'«Toco un poco la guitarra»'},
   {q:'¿A Lucía le gustan los videojuegos?',opts:['No, prefiere salir','Sí, mucho','Solo a veces'],ans:'No, prefiere salir',why:'«No me gustan los videojuegos, prefiero salir»'},
   {q:'¿Qué baile le gusta a Lucía?',opts:['el flamenco','el reguetón','la salsa'],ans:'el flamenco',why:'«me gusta bailar flamenco»'},
   {q:'¿Qué quiere ver Diego el sábado?',opts:['películas de acción','una serie','un concierto'],ans:'películas de acción',why:'«quiero ver películas de acción»'},
   {q:'¿Cuándo va Lucía a la playa?',opts:['los fines de semana','todos los días','nunca'],ans:'los fines de semana',why:'«Los fines de semana voy a la playa»'},
   {q:'¿A Diego le gusta bailar?',opts:['No','Sí, mucho','Solo flamenco'],ans:'No',why:'«No me gusta bailar»'}]});
}

renderFC();renderTable();gameGusta();gameReaccion();renderLectura();buildRecorders();renderBandas();buildInlineExercises();
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='U4_web_mijn_versie.html';a.click();};
})();
"""

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/U4_web.html","w").write(html)
print("U4_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
