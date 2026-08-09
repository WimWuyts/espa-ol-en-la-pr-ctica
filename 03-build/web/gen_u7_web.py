#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C5 · U7 «Mi casa y mi barrio».
# Eén standalone bestand: fonts base64, de U7-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U7-vocab), visuele/interactieve grammatica (hay/estar · preposiciones · estar+gerundio · imperativo · ordinales),
# klikbare kaart (mundo hispano, parada 7 = Colombia/Cartagena) + TTS + inline recorder + Lectura + editbar. Huisstijl groen.
# Emoji-flashcards via lokale EXTRA-dict (vocab_emoji.py NIET aangeraakt).
import json, base64, os, sys
import hub_drills
import hub_iconos
import hub_type_sets
import hub_type_gram
import extra_bronnen
import hub_bloques
import escucha_data, lectura_data
import gen_rol
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
GEN = f"{ROOT}/02-huisstijl/beeld/generators"
sys.path.insert(0, GEN); import cast_gen as C; import vocab_emoji as VE
vocab = json.load(open(f"{ROOT}/01-cursussen/05-a1/U7/u7_vocab.json", encoding="utf-8"))
mapsvg = open(f"{GEN}/mundo_map_real.svg").read()
moch = C.mochila("100%", "map")
# --- U7-emoji via lokale dict (parallel-veilig; vocab_emoji.py wordt NIET aangepast) ---
EXTRA = {
 "casa":"🏠","piso":"🏢","apartamento":"🏢","planta baja":"🚪","primer piso":"🔢","escalera":"🪜",
 "ascensor":"🛗","puerta":"🚪","ventana":"🪟","pared":"🧱","jardín":"🌳","terraza":"⛱️",
 "habitación":"🛏️","salón":"🛋️","cocina":"🍳","baño":"🛁","dormitorio":"🛏️","comedor":"🍽️","pasillo":"🚪",
 "mesa":"🪑","silla":"🪑","sofá":"🛋️","cama":"🛏️","armario":"🗄️","estantería":"📚","lámpara":"💡",
 "nevera":"🧊","espejo":"🪞","alfombra":"🟫","ducha":"🚿",
 "barrio":"🏘️","calle":"🛣️","plaza":"⛲","tienda":"🏪","supermercado":"🛒","panadería":"🥖","farmacia":"💊",
 "banco":"🏦","parque":"🏞️","museo":"🏛️","estación":"🚉","iglesia":"⛪","cine":"🎬",
 "a la derecha":"➡️","a la izquierda":"⬅️","todo recto":"⬆️","esquina":"📐","semáforo":"🚦",
 "cerca":"📍","lejos":"🗺️","girar":"🔄","seguir":"⏩","cruzar":"🚸",
 "autobús":"🚌","metro":"🚇","taxi":"🚕","bicicleta":"🚲","a pie":"🚶",
 "encima de":"🔼","debajo de":"🔽","al lado de":"🤝","lado de":"🤝","entre":"🔗","delante de":"👉","detrás de":"👈",
 "dentro de":"📦","enfrente de":"🔛",
}
def emoji_u7(es, grp):
    return EXTRA.get(VE._norm(es)) or VE.emoji_for(es, grp)
ICONS=[f'<div class="fcico">{emoji_u7(v.get("es",""),v.get("grp",""))}</div>' for v in vocab]

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
   ['casa-memoria', 'memoria de la casa', 'memory'],
   ['habitacion-mueble', 'habitación ↔ mueble', 'match'],
   ['edificio-funcion', 'edificio ↔ función', 'match']]],
 ['② Distinguir · léxico/gramática', [
   ['hay-esta', '¿hay o está?', 'classify'],
   ['clasifica-lugar', 'habitación · mueble · edificio', 'classify'],
   ['clasifica-prepo', 'preposición: ¿dónde?', 'classify'],
   ['diptongo-hiato', '¿diptongo o hiato?', 'classify']]],
 ['③ Producir con apoyo', [
   ['gerundio-cloze', 'completa: estar + gerundio', 'cloze'],
   ['preposicion-cloze', 'completa la preposición', 'cloze'],
   ['imperativo-cloze', 'el camino: imperativo', 'cloze'],
   ['preposicion-tetris', 'preposiciones: torres', 'tower'],
   ['ordena-ruta', 'ordena las instrucciones', 'order'],
   ['ordena-casa', 'ordena de fuera a dentro', 'order'],
   ['senala-habitacion', 'señala en la habitación', 'point'],
   ['senala-plano', 'señala en el plano del barrio', 'point']]],
 ['④ Analizar & comunicar', [
   ['explica-camino', '¡explica el camino!', 'sim']]],
 ['⑤ Hablar · grábate 🎙️', [
   ['repite-barrio', 'escucha y repite: en el barrio', 'speak'],
   ['shadowing-valen', 'shadowing con Valen', 'speak'],
   ['describe-habitacion', 'describe tu habitación', 'speak'],
   ['explica-camino-voz', 'mensaje de voz: explica el camino', 'speak']]],
]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-u7-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-u7-{s}.html")}

CSS = FONTS + hub_iconos.CSS + extra_bronnen.CSS + hub_drills.ESCUCHA_CSS + hub_drills.LECTURA_CSS + hub_drills.TYPE_CSS + """
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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="casa">la casa</option><option value="habitaciones">habitaciones</option><option value="muebles">muebles</option><option value="barrio">el barrio</option><option value="direcciones">direcciones</option><option value="transporte">transporte</option><option value="preposiciones">preposiciones</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Español en la práctica · U7 Mi casa y mi barrio</title>
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
    <div><h1>U7 · Mi casa y mi barrio</h1>
    <p>La página digital de la Unidad 7 (parada <b>Colombia · Cartagena</b>): flashcards, gramática visual e interactiva y <b>__NGAMES__ juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie.</span></p></div>
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
    <p class="lead">Eerst betekenis en patroon ontdekken, dan de regel. Beweeg over de woorden, klik, en probeer. <span class="gloss">Alles binnen het thema van U7: hay/estar, preposiciones de lugar, estar + gerundio, imperativo y ordinales.</span></p>
    <div class="card" id="colorsent"></div>
    <h3 class="subh">🏠 Hay o está — descubre el contraste</h3>
    <div class="game" id="g_hayesta"></div>
    <div class="card ex" id="gx_hayq"></div>
    <h3 class="subh">📍 Preposiciones de lugar — ¿dónde está?</h3>
    <div class="game" id="g_prepo"></div>
    <div class="card ex" id="gx_prepoq"></div>
    <div class="card ex" id="gx_prepomatch"></div>
    <h3 class="subh">⏳ Estar + gerundio — construye y practica</h3>
    <div class="card" id="estarconj"></div>
    <div class="card ex" id="gx_gbuild"></div>
    <div class="card ex" id="gx_gerq"></div>
    <h3 class="subh">🧭 Imperativo — explica el camino</h3>
    <div class="card ex" id="gx_impq"></div>
    <h3 class="subh">🔢 Ordinales + apócope</h3>
    <div class="card ex" id="gx_ordq"></div>
    <h3 class="subh">🎯 Repaso mixto — rellena con feedback</h3>
    <div class="card ex" id="gx_mix"></div>
  __GRAMSLOTS__
  </section>

  <section class="panel" data-p="lectura">
    <h2 class="sec">Lectura · «Se alquila» + el barrio de Valen</h2>
    <p class="lead">Lees het <b>anuncio de piso</b> en de <b>tekst over het barrio</b>, <b>luister</b> ze (🔊 TTS) en <b>controleer je begrip</b>. Daarna beschrijf je een woning — dat neem je op in het tabblad <b>Hablar</b>. <span class="gloss">Keten: lezen → luisteren → spreken.</span></p>
    <div id="lecturawrap"></div>
    <h3 class="subh">🔢 Ordena</h3>
    <div class="card ex" id="lx_order"></div>
    <h3 class="subh">🔎 Comprensión · escanea y escoge</h3>
    <div class="card ex" id="lx_scan"></div>
    <h2 class="sec">Lectura completa · Se alquila apartamento en el centro</h2>
    <p class="lead">Een echte huuradvertentie met de volledige leesroute: <b>voorspellen → globaal → scannen → juist/fout met bewijs → betekenis uit de context → zelf schrijven</b>. <span class="gloss">Dezelfde tekst staat in je cursus, met schrijfruimte.</span></p>
    <div class="card ex" id="lec_u7"></div>
  </section>

  <section class="panel" data-p="escuchar">
    <h2 class="sec">Escuchar · La visita al piso 🎧</h2>
    <p class="lead">Sam en zijn moeder bezoeken een appartement — en niet alles klopt met de advertentie. Eén fragment, zes stappen: eerst <b>weten waar je bent</b>, dan <b>globaal</b> luisteren, dan de <b>details</b>, dan <b>juist/fout met bewijs</b>. Het <b>transcript</b> gaat pas open als je klaar bent — anders lees je mee in plaats van te luisteren. <span class="gloss">Zolang er nog geen opname is, leest de computerstem het fragment voor.</span></p>
    <div class="card ex" id="esc_u7"></div>
  </section>
  <section class="panel" data-p="juegos">
    <h2 class="sec">Ejercicios · __NGAMES__ juegos, jij kiest</h2>
    <p class="lead">Geordend van <b>herkennen → onderscheiden → produceren met steun → analyseren &amp; communiceren → hablar</b>. Elk spel geeft directe, verklarende feedback en de steun bouwt af. <span class="gloss">Klik een spel; het opent in een venster en werkt ook offline.</span></p>
    <div id="motorlink"></div>
  </section>

  <section class="panel" data-p="retos">
    <h2 class="sec">Retos · tres desafíos 🎯</h2>
    <p class="lead">Drie retos met <b>één harde regel</b>: je neemt een museumaudiogids op van je eigen straat met vijf verschillende voorzetsels, je hoort zes geluiden en zegt telkens <b>wie wat aan het doen is en waar</b>, en je gidst iemand die het gebouw <b>niet ziet</b> — dus geen kleuren en geen «daar». <span class="gloss">De zeven andere retos van deze unit staan in het boek en in de PowerPoint.</span></p>
    <div id="retos_u7"></div>
  </section>
  <section class="panel" data-p="hablar">
    __ROL__
    <h2 class="sec">Hablar · grábate 🎙️</h2>
    <p class="lead">Neem <b>jezelf</b> op: luister naar het model, spreek in, luister terug, en neem opnieuw op. <span class="gloss">Werkt in Chrome/Edge; sta de micro toe. Print blijft bruikbaar zonder opname.</span></p>
    <div class="card" id="rec_repite"></div>
    <div class="card" id="rec_pedido"></div>
    <div class="card" id="rec_plato"></div>
    <p class="lead" style="margin-top:8px">Meer spreek-/opnamespellen (shadowing con Valen, explica el camino…) vind je ook onder <b>Juegos ⑤</b>.</p>
  </section>

  <section class="panel" data-p="cultura">
    <h2 class="sec">Cultura · La plaza y el barrio</h2>
    <p class="lead">En el mundo hispano <b>la plaza es el corazón del barrio</b>. Descubre <b>Cartagena</b> 🇨🇴, sus <b>casas de colores</b> y cómo se vive (casa · piso · apartamento). <span class="gloss">Het plein is het hart van de wijk; ontdek Cartagena en het wonen in de Spaanstalige wereld.</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21h18"/><path d="M5 21V7l7-4 7 4v14"/><path d="M9 21v-6h6v6"/></svg>La plaza 🏛️ 🇨🇴</h3>
      <p><b>ES:</b> La <b>plaza</b> es el centro del barrio: hay bancos, árboles y una <b>iglesia</b>. Por la tarde la gente <b>está paseando</b> y charlando. En Cartagena, la <b>Plaza de los Coches</b> es famosa. <span class="gloss">Het plein is de ontmoetingsplek van de buurt; 's middags wandelt en kletst iedereen er.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/></svg>Las casas de colores 🏘️</h3>
      <p><b>ES:</b> Cartagena tiene un <b>casco histórico</b> con casas de <b>colores</b> vivos y <b>balcones con flores</b>. Las murallas protegen la ciudad frente al mar Caribe. El barrio <b>Getsemaní</b> es arte, música y color. <span class="gloss">Cartagena's oude stad heeft kleurrijke huizen met bloembalkons; de stadsmuren beschermen tegen de Caribische zee.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">¿Cómo se vive? · casa · piso · apartamento 🌎</h3>
      <p><b>ES:</b> No en todas partes se dice igual. En <b>España</b> se vive en un <b>piso</b>; en <b>América</b>, en un <b>apartamento</b>. La vivienda con jardín es un <b>chalet</b> (España) o una <b>casa</b> (América). <span class="gloss">In Spanje = piso, in Latijns-Amerika = apartamento. Bij het adres komt vaak het piso: «calle Real, 3º».</span></p>
      <div class="platos">
        <div class="pl"><div class="em">⛲</div><div class="nm">la Plaza Mayor</div><small>España 🇪🇸</small></div>
        <div class="pl"><div class="em">🏛️</div><div class="nm">el Zócalo</div><small>México 🇲🇽</small></div>
        <div class="pl"><div class="em">🎨</div><div class="nm">Getsemaní</div><small>Colombia 🇨🇴</small></div>
        <div class="pl"><div class="em">🏰</div><div class="nm">Plaza de Armas</div><small>Perú 🇵🇪</small></div>
        <div class="pl"><div class="em">🎭</div><div class="nm">La Boca</div><small>Argentina 🇦🇷</small></div>
      </div>
      <p><span class="gloss">Cada barrio tiene su plaza: het plein als hart van de buurt komt overal terug.</span></p></div>
    <h3 class="subh">📍 La Ruta · ¿dónde estamos?</h3>
    <p class="lead">Onze parada 7: <b>Cartagena · Colombia</b> 🇨🇴 (bajamos por el Caribe). <b>Klik op een groen land</b> op de kaart voor info. Verderop: Perú.</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een groen land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    __BRONNEN__
  </section>

  <div class="foot">Español en la práctica · C5 · Unidad 7 «Mi casa y mi barrio» — página digital. Uitbreiding op de PDF · huisstijl groen · print ↔ PowerPoint ↔ web.</div>
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
""" + hub_iconos.js() + hub_drills.SPEAK_JS + hub_drills.RETOS_JS + r"""
const TTS=('speechSynthesis'in window);
if(TTS){speechSynthesis.getVoices();speechSynthesis.onvoiceschanged=()=>{};}
const PANELS=[['vocab','Vocabulario'],['gram','Gramática'],['lectura','Lectura'],['escuchar','Escuchar'],['juegos','Juegos'],['retos','Retos'],['hablar','Hablar'],['cultura','Cultura'],['extra','Extra']];
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
PANELS.forEach((p,i)=>{const b=document.createElement('button');b.innerHTML=(IC[p[0]]||'')+'<span>'+p[1]+'</span>';if(i===0)b.classList.add('on');
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

// ---- GRAMMAR-VIZ 1: kleurgecodeerde estar+gerundio-zin ----
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Estar + gerundio — ¿qué pasa ahora?</h3>'+
'<div class="csent">'+
'<span style="background:#dbeafe;color:#1e40af">(Yo)<span class="tip">onderwerp</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">estoy<span class="tip">estar · presente (estoy, estás, está…)</span></span> '+
'<span style="background:#dcfce7;color:#166534">cocinando<span class="tip">gerundio (-ando / -iendo)</span></span> '+
'<span style="background:#ccfbf1;color:#0f766e">en la cocina<span class="tip">plaats</span></span>.</div>'+
'<div class="legend"><span><i style="background:#93c5fd"></i>onderwerp</span><span><i style="background:#fdba74"></i>estar (presente)</span><span><i style="background:#86efac"></i>gerundio</span><span><i style="background:#5eead4"></i>plaats</span></div>'+
'<p class="gloss" style="margin-top:8px">🔴 Twee delen: <b>estar</b> (vervoegd) + <b>gerundio</b> (-ando bij -ar · -iendo bij -er/-ir). · '+(TTS?'<button class="spk-btn" onclick="speak(\'Estoy cocinando en la cocina\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: estar (presente) — klik om te onthullen ----
(function(){const el=document.getElementById('estarconj');
 const R=[['yo','estoy'],['tú','estás'],['él/ella','está'],['nosotros','estamos'],['vosotros','estáis'],['ellos','están']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">El verbo «estar» — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">Denk eerst zelf de vorm; klik dan de kaart. Daarna: forma + gerundio.</p><div class="conjgrid" id="ecg"></div>';
 const g=el.querySelector('#ecg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v+' …ndo';if(TTS)speak(p+' '+v+' cocinando');};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: ¿hay o está/están? ----
function gameHayEsta(){const el=document.getElementById('g_hayesta');
 const items=[['En el salón ___ un sofá.','hay','nieuw (un sofá)'],['El sofá ___ al lado.','está','bekend + plaats'],['___ tres habitaciones.','hay','nieuw (número)'],['Los baños ___ arriba.','están','bekend mv. + plaats'],['La cocina ___ a la derecha.','está','bekend + plaats'],['___ un parque cerca.','hay','nieuw (un parque)'],['Las tiendas ___ en la plaza.','están','bekend mv.'],['___ muchas flores.','hay','nieuw (muchas)'],['El museo ___ enfrente.','está','bekend + plaats'],['En mi barrio ___ una farmacia.','hay','nieuw (una)']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿hay, está o están?</h3><p class="desc">Nieuw (un/una/número) → hay. Bekend (el/la) + plaats → está/están.</p>'+scoreBar('sbH')+'<div id="hW" style="font-size:20px;font-family:var(--disp);text-align:center;margin:8px 0"></div><div class="chips" id="hC" style="justify-content:center"></div><div class="fb" id="hFb"></div>';
 const sb=el.querySelector('#sbH');const cont=el.querySelector('#hC');
 ['hay','está','están'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#hW').textContent=el.cur[0];el.querySelector('#hFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#hFb'),ok,(ok?'¡Sí! ':'Nee → ')+el.cur[1]+' ('+el.cur[2]+').');setTimeout(next,1050);}
 next();}
// ---- GRAMMAR-VIZ 4: ¿qué preposición? ----
function gamePrepo(){const el=document.getElementById('g_prepo');
 const items=[['La lámpara está ___ la mesa (boven op).','encima de'],['El gato está ___ la cama (onder).','debajo de'],['El banco está ___ la farmacia (naast).','al lado de'],['El cine está ___ el banco y el parque (tussen).','entre'],['El jardín está ___ la casa (achter).','detrás de'],['Hay un árbol ___ la casa (vóór).','delante de'],['La ropa está ___ armario (binnen in).','dentro de'],['El museo está ___ la iglesia (tegenover).','enfrente de']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿Qué preposición de lugar?</h3><p class="desc">Kies de preposición die bij de betekenis (tussen haakjes) past.</p>'+scoreBar('sbPr')+'<div id="prW" style="font-size:19px;font-family:var(--disp);text-align:center;margin:10px 0"></div><div class="chips" id="prC" style="justify-content:center"></div><div class="fb" id="prFb"></div>';
 const sb=el.querySelector('#sbPr');const cont=el.querySelector('#prC');
 ['encima de','debajo de','al lado de','entre','delante de','detrás de','dentro de','enfrente de'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#prW').textContent=el.cur[0];el.querySelector('#prFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#prFb'),ok,(ok?'¡Sí! → ':'Nee → ')+el.cur[1]+'.');setTimeout(next,1050);}
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
   const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "🏙️ Un lugar: las casas coloridas de Guanajuato", "star": 1, "nl": "Parada anterior (U5–U6) · CDMX · los mercados (Diego)"}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "🏙️ Un lugar: los pisos y los patios andaluces", "star": 1, "nl": "Parada anterior (U0–U4) · Madrid · Sevilla · Barcelona · València"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "🏙️ Un lugar: los balcones floridos de Cartagena", "star": 1, "nl": "★ ¡Estás aquí! Parada U7 · Cartagena (Valen)"}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "🏙️ Un lugar: los barrios coloniales del Cusco", "star": 0, "nl": ""}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "🏙️ Un lugar: el barrio de La Boca, con casas de colores", "star": 0, "nl": ""}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "🏙️ Un lugar: los «ranchos» en las colinas de Caracas", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "🏙️ Un lugar: las casas de colores de Valparaíso", "star": 0, "nl": ""}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "🏙️ Un lugar: el centro histórico de Quito", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "🏙️ Un lugar: Antigua, ciudad colonial entre volcanes", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "🏙️ Un lugar: los edificios coloniales de La Habana Vieja", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "🏙️ Un lugar: las casas de adobe del Altiplano", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "🏙️ Un lugar: la Zona Colonial de Santo Domingo", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "🏙️ Un lugar: las casas de madera de las islas", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "🏙️ Un lugar: las casas con galería y patio", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "🏙️ Un lugar: Granada, ciudad colonial junto al lago", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "🏙️ Un lugar: los pueblos de la Ruta de las Flores", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "🏙️ Un lugar: las casas con jardín, «pura vida»", "star": 0, "nl": ""}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "🏙️ Un lugar: el Casco Viejo de la capital", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "🏙️ Un lugar: la Ciudad Vieja de Montevideo", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "🏙️ Un lugar: las casas de colores del Viejo San Juan", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "🏙️ Un lugar: Malabo y su arquitectura colonial", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "🏙️ Un lugar: barrios latinos como «Little Havana» (Miami)", "star": 0, "nl": ""}};
 const wrap=document.getElementById('mapwrap');const svg=wrap.querySelector('svg');const box=document.getElementById('mapinfo');
 if(!svg)return;
 svg.querySelectorAll('path.spa, path.usa').forEach(p=>{p.style.cursor='pointer';
   p.addEventListener('mouseenter',()=>{p.style.opacity='.75'});p.addEventListener('mouseleave',()=>{p.style.opacity=''});
   p.addEventListener('click',()=>{const c=p.getAttribute('data-c');const d=INFO[c];if(!d)return;
     box.innerHTML='<h3>'+d.fl+' '+d.n+' <span style="font-size:13px;color:var(--mut);font-weight:400">('+c+')</span>'+(d.star?' ★':'')+'</h3>'+'<div class="mrow"><b>🏛️ Capital:</b> '+d.cap+'</div>'+'<div class="mrow"><b>👥 Población:</b> '+d.pob+'</div>'+'<div class="mrow"><b>💰 Moneda:</b> '+d.mon+'</div>'+'<div class="mrow"><b>🗣️ Gentilicio:</b> '+d.gen+'</div>'+'<div class="mrow"><b>🌐 Idioma:</b> '+d.idi+'</div>'+(d.tema?'<div style="margin-top:8px;padding:8px 11px;background:rgba(255,255,255,.7);border-left:4px solid var(--gd);border-radius:7px;font-weight:600;color:var(--gd)">'+d.tema+'</div>':'')+(d.cool?'<div style="margin-top:8px;font-size:13px;line-height:1.5"><b>💡 ¿Sabías que…?</b> '+d.cool+'</div>':'')+(d.nl?'<div class="gloss" style="margin-top:6px">'+d.nl+'</div>':'');
     box.scrollIntoView({behavior:'smooth',block:'nearest'});});
 });
})();

// ---------- LECTURA: anuncio de piso + texto del barrio + TTS + begrip ----------
function renderLectura(){const el=document.getElementById('lecturawrap');if(!el)return;
 const M=[{n:'Se alquila piso 🏢',raw:'Bonito piso en el centro. Tercer piso con ascensor. Tiene dos habitaciones, un salón grande, cocina y baño. Hay una terraza con vistas a la plaza. Está cerca de la panadería y del parque. Seiscientos euros al mes.',
    html:'<div class="sec2">El piso</div><div class="mi"><span>Tercer piso (con ascensor)</span><span class="pr">3º</span></div><div class="mi"><span>Habitaciones</span><span class="pr">2</span></div><div class="mi"><span>Salón · cocina · baño</span><span class="pr">✓</span></div><div class="sec2">Extras</div><div class="mi"><span>Terraza con vistas a la plaza</span><span class="pr">✓</span></div><div class="mi"><span>Cerca de panadería y parque</span><span class="pr">✓</span></div><div class="mi"><span>Precio</span><span class="pr">600 €/mes</span></div>'},
   {n:'Mi barrio · Valen 🇨🇴',raw:'Vivo en un barrio de casas de colores. Enfrente de mi casa hay una plaza con palmeras. La panadería está al lado y el mar está cerca. Por la tarde, la gente está paseando y los niños están jugando. ¡Me encanta mi barrio!',
    html:'<p style="font-size:14px;line-height:1.6">Vivo en un barrio de <b>casas de colores</b>. Enfrente de mi casa <b>hay</b> una <b>plaza</b> con palmeras. La <b>panadería está al lado</b> y el mar <b>está cerca</b>. Por la tarde, la gente <b>está paseando</b> y los niños <b>están jugando</b>. ¡Me encanta mi barrio!</p>'}];
 el.innerHTML='<div class="perfiles">'+M.map((m,i)=>'<div class="menucard"><h4>'+m.n+' '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lm'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div id="lm'+i+'" data-raw="'+m.raw.replace(/"/g,'&quot;')+'">'+m.html+'</div></div>').join('')+'</div>';
 const items=[['El piso está en el tercer piso.',true,'«Tercer piso con ascensor»'],['El piso tiene dos habitaciones.',true,'«dos habitaciones»'],['El piso está en la planta baja.',false,'está en el tercer piso'],['Hay una terraza con vistas a la plaza.',true,'«terraza con vistas a la plaza»'],['El piso cuesta 600 € al mes.',true,'«seiscientos euros al mes»'],['Enfrente de la casa de Valen hay una plaza.',true,'«Enfrente de mi casa hay una plaza»'],['La panadería está lejos.',false,'«La panadería está al lado»'],['Los niños están jugando en el barrio.',true,'«los niños están jugando»']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — comprueba tu comprensión (con evidencia)</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Describe una vivienda</h3><p class="gloss" style="margin:0 0 8px">Wees de <b>propietario/a</b>: beschrijf een woning (¿cuántas habitaciones hay? ¿dónde está? ¿cuánto cuesta?). Neem het op onder <b>Hablar 🎙️</b> («describe tu habitación»).</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="Es un piso en el… Hay… Está cerca de…"></textarea>';
 el.appendChild(box);el.appendChild(resp);}

// ---------- INLINE RECORDER (MediaRecorder) ----------
""" + hub_drills.RECORDER_JS + r"""
function buildRecorders(){
 makeRecorder('rec_repite',{title:'Escucha y repite: en el barrio',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'En mi barrio hay una plaza muy bonita.',cue:'hay',tip:'Duidelijk uitgesproken? Probeer nog eens.'},{text:'La panadería está al lado del parque.',cue:'estar + preposición'},{text:'Estoy cocinando en la cocina.',cue:'estar + gerundio'},{text:'Sigue todo recto y gira a la derecha.',cue:'imperativo'},{text:'Vivo en el tercer piso.',cue:'ordinal'}]});
 makeRecorder('rec_pedido',{title:'Mensaje de voz: explica el camino',desc:'Neem één bericht op. Doel: leg iemand de weg uit van de school naar een plek. Gebruik: sigue · gira · cruza · todo recto · a la derecha/izquierda.',items:[
   {text:'Explica el camino de la escuela a la plaza (30 s): usa sigue, gira, cruza…',cue:'el camino',tip:'4-5 instructies met imperativo? Neem opnieuw op.'}]});
 makeRecorder('rec_plato',{title:'Describe tu habitación',desc:'Beschrijf je kamer: ¿qué hay? ¿dónde está cada mueble? ¿qué estás haciendo ahora?',items:[
   {text:'En mi habitación hay ___ . La cama está ___ . Ahora estoy ___ .',cue:'tu versión',tip:'Heb je hay, una preposición én estar+gerundio gebruikt? Herneem.'}]});
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
 // GRAMÁTICA · hay/estar
 buildChoice('gx_hayq',{title:'Mini-quiz: ¿hay, está o están?',desc:'Nieuw (un/una/número) → hay. Bekend (el/la) + plaats → está/están.',per:6,pool:[
   {q:'En el salón ___ un sofá.',opts:['hay','está','están'],ans:'hay',why:'un sofá = nieuw'},
   {q:'El sofá ___ al lado de la ventana.',opts:['está','hay','están'],ans:'está',why:'el sofá = bekend + plaats'},
   {q:'___ tres habitaciones.',opts:['Hay','Están','Está'],ans:'Hay',why:'número = hay'},
   {q:'Los baños ___ arriba.',opts:['están','hay','está'],ans:'están',why:'los baños = mv. bekend'},
   {q:'En mi barrio ___ una plaza.',opts:['hay','está','están'],ans:'hay',why:'una plaza = nieuw'},
   {q:'La plaza ___ en el centro.',opts:['está','hay','están'],ans:'está',why:'la plaza = bekend'},
   {q:'___ muchas tiendas cerca.',opts:['Hay','Están','Está'],ans:'Hay',why:'muchas = nieuw'},
   {q:'La farmacia ___ en la esquina.',opts:['está','hay','están'],ans:'está',why:'la farmacia = bekend'},
   {q:'¿Cuántas ventanas ___ ?',opts:['hay','están','está'],ans:'hay',why:'¿cuántas? = hay'},
   {q:'Las llaves ___ encima de la mesa.',opts:['están','hay','está'],ans:'están',why:'las llaves = mv. bekend'}]});
 // GRAMÁTICA · preposiciones
 buildChoice('gx_prepoq',{title:'Mini-quiz: preposiciones de lugar',desc:'Kies de preposición die bij de betekenis past.',per:6,pool:[
   {q:'La lámpara está ___ la mesa (boven op).',opts:['encima de','debajo de','entre'],ans:'encima de',why:'boven op = encima de'},
   {q:'El gato está ___ la cama (onder).',opts:['debajo de','encima de','al lado de'],ans:'debajo de',why:'onder = debajo de'},
   {q:'El banco está ___ la farmacia (naast).',opts:['al lado de','delante de','entre'],ans:'al lado de',why:'naast = al lado de'},
   {q:'El cine está ___ el banco y el parque.',opts:['entre','encima de','detrás de'],ans:'entre',why:'tussen = entre A y B'},
   {q:'El jardín está ___ la casa (achter).',opts:['detrás de','delante de','dentro de'],ans:'detrás de',why:'achter = detrás de'},
   {q:'Hay un árbol ___ la casa (vóór).',opts:['delante de','detrás de','encima de'],ans:'delante de',why:'vóór = delante de'},
   {q:'La ropa está ___ armario (binnen in).',opts:['dentro del','encima del','entre'],ans:'dentro del',why:'binnen in + del'},
   {q:'El museo está ___ la iglesia (tegenover).',opts:['enfrente de','al lado de','debajo de'],ans:'enfrente de',why:'tegenover = enfrente de'},
   {q:'El parque está ___ mi casa (dichtbij).',opts:['cerca de','lejos de','dentro de'],ans:'cerca de',why:'dichtbij = cerca de'},
   {q:'La estación está ___ (ver).',opts:['lejos','cerca','entre'],ans:'lejos',why:'ver = lejos'}]});
 buildMatch('gx_prepomatch',{title:'Empareja: preposición ↔ betekenis',desc:'Koppel de preposición aan de Nederlandse betekenis.',per:6,pool:[
   {a:'encima de',b:'boven op'},{a:'debajo de',b:'onder'},{a:'al lado de',b:'naast'},{a:'entre',b:'tussen'},
   {a:'delante de',b:'vóór'},{a:'detrás de',b:'achter'},{a:'dentro de',b:'binnen in'},{a:'enfrente de',b:'tegenover'},
   {a:'cerca de',b:'dichtbij'},{a:'lejos de',b:'ver'}]});
 // GRAMÁTICA · estar + gerundio
 buildOrder('gx_gbuild',{title:'Construye: estar + gerundio',desc:'Tik de blokjes in de juiste volgorde (onderwerp → estar → gerundio → plaats).',rounds:[
   {sub:'yo · cocinar',items:[{label:'Yo',key:1},{label:'estoy',key:2},{label:'cocinando',key:3},{label:'en la cocina',key:4}]},
   {sub:'tú · ver',items:[{label:'¿Tú',key:1},{label:'estás',key:2},{label:'viendo',key:3},{label:'la tele?',key:4}]},
   {sub:'nosotros · comer',items:[{label:'Nosotros',key:1},{label:'estamos',key:2},{label:'comiendo',key:3},{label:'en el comedor',key:4}]},
   {sub:'ellos · dormir',items:[{label:'Ellos',key:1},{label:'están',key:2},{label:'durmiendo',key:3},{label:'en el dormitorio',key:4}]},
   {sub:'ella · escribir',items:[{label:'Valen',key:1},{label:'está',key:2},{label:'escribiendo',key:3},{label:'una carta',key:4}]},
   {sub:'yo · leer',items:[{label:'Yo',key:1},{label:'estoy',key:2},{label:'leyendo',key:3},{label:'en el salón',key:4}]}]});
 buildChoice('gx_gerq',{title:'Mini-quiz: estar + gerundio',desc:'Kies de juiste vorm (estar + -ando/-iendo). Vormen nagerekend.',per:6,pool:[
   {q:'(Yo) ___ en la cocina. (cocinar)',opts:['estoy cocinando','estás cocinando','estoy cocinar'],ans:'estoy cocinando',why:'yo estoy + cocinando'},
   {q:'¿(Tú) ___ la tele? (ver)',opts:['estás viendo','estoy viendo','estás veiendo'],ans:'estás viendo',why:'ver → viendo'},
   {q:'(Nosotros) ___ . (comer)',opts:['estamos comiendo','están comiendo','estamos comer'],ans:'estamos comiendo',why:'comer → comiendo'},
   {q:'Valen ___ una carta. (escribir)',opts:['está escribiendo','están escribiendo','está escribir'],ans:'está escribiendo',why:'escribir → escribiendo'},
   {q:'(Ellos) ___ . (dormir)',opts:['están durmiendo','están dormiendo','está durmiendo'],ans:'están durmiendo',why:'dormir → durmiendo'},
   {q:'(Yo) ___ un libro. (leer)',opts:['estoy leyendo','estoy leiendo','estás leyendo'],ans:'estoy leyendo',why:'leer → leyendo'},
   {q:'La forma de «hablar»:',opts:['hablando','hablendo','hablado'],ans:'hablando',why:'-ar → -ando'},
   {q:'La forma de «vivir»:',opts:['viviendo','vivando','viviando'],ans:'viviendo',why:'-ir → -iendo'},
   {q:'Mi madre ___ la casa. (limpiar)',opts:['está limpiando','están limpiando','está limpiendo'],ans:'está limpiando',why:'-ar → -ando'},
   {q:'¿(Vosotros) ___ música? (escuchar)',opts:['estáis escuchando','estás escuchando','estáis escuchendo'],ans:'estáis escuchando',why:'vosotros estáis + escuchando'}]});
 // GRAMÁTICA · imperativo
 buildChoice('gx_impq',{title:'Mini-quiz: el imperativo (el camino)',desc:'Kies het juiste imperativo (tú) om de weg uit te leggen.',per:6,pool:[
   {q:'___ todo recto. (seguir)',opts:['Sigue','Sige','Sigues'],ans:'Sigue',why:'seguir → sigue (e→i)'},
   {q:'___ a la derecha. (girar)',opts:['Gira','Gire','Giras'],ans:'Gira',why:'-ar → -a'},
   {q:'___ la calle. (cruzar)',opts:['Cruza','Cruce','Cruzas'],ans:'Cruza',why:'-ar → -a'},
   {q:'___ la primera calle. (tomar)',opts:['Toma','Tome','Tomas'],ans:'Toma',why:'-ar → -a'},
   {q:'___ por la escalera. (subir)',opts:['Sube','Suba','Subes'],ans:'Sube',why:'-ir → -e'},
   {q:'___ a la plaza. (ir)',opts:['Ve','Va','Vas'],ans:'Ve',why:'ir → ve (onregelmatig)'},
   {q:'___ el autobús 5. (coger)',opts:['Coge','Coja','Coges'],ans:'Coge',why:'-er → -e'},
   {q:'___ en el semáforo. (parar)',opts:['Para','Pare','Paras'],ans:'Para',why:'-ar → -a'},
   {q:'___ a la izquierda. (doblar)',opts:['Dobla','Doble','Doblas'],ans:'Dobla',why:'-ar → -a'},
   {q:'___ hasta el final. (caminar)',opts:['Camina','Camine','Caminas'],ans:'Camina',why:'-ar → -a'}]});
 // GRAMÁTICA · ordinales
 buildChoice('gx_ordq',{title:'Mini-quiz: ordinales + apócope',desc:'primero → primer / tercero → tercer (vóór m. sing.).',per:6,pool:[
   {q:'Vivo en el ___ piso. (1º)',opts:['primer','primero','primera'],ans:'primer',why:'primero → primer + m. sing.'},
   {q:'La ___ calle a la derecha. (1ª)',opts:['primera','primer','primero'],ans:'primera',why:'vrouwelijk = geen apocope'},
   {q:'El ascensor va al ___ piso. (3º)',opts:['tercer','tercero','tercera'],ans:'tercer',why:'tercero → tercer + m. sing.'},
   {q:'Es mi ___ día aquí. (1º)',opts:['primer','primero','primera'],ans:'primer',why:'primer día'},
   {q:'El ___ piso (2º).',opts:['segundo','segund','segunda'],ans:'segundo',why:'segundo = geen apocope'},
   {q:'La ___ vez (3ª).',opts:['tercera','tercer','tercero'],ans:'tercera',why:'vrouwelijk = tercera'},
   {q:'Vivo en el ___ (kort, m.).',opts:['primero','primer','primera'],ans:'primero',why:'zonder zn. = primero'},
   {q:'El ___ piso (4º).',opts:['cuarto','cuart','cuarta'],ans:'cuarto',why:'cuarto = geen apocope'},
   {q:'El ___ piso (5º).',opts:['quinto','quint','quinta'],ans:'quinto',why:'quinto = geen apocope'},
   {q:'El ___ premio (3º).',opts:['tercer','tercero','tercera'],ans:'tercer',why:'tercer premio (m. sing.)'}]});
 // GRAMÁTICA · mixto
 buildChoice('gx_mix',{title:'Repaso mixto: rellena',desc:'Alles door elkaar: hay/estar · preposiciones · gerundio · imperativo · ordinales.',per:8,pool:[
   {q:'En el salón ___ un sofá.',opts:['hay','está','están'],ans:'hay',why:'un sofá = nieuw'},
   {q:'El banco está ___ la farmacia.',opts:['al lado de','encima de','dentro de'],ans:'al lado de',why:'naast'},
   {q:'(Yo) estoy ___ . (cocinar)',opts:['cocinando','cocinar','cocinado'],ans:'cocinando',why:'gerundio -ando'},
   {q:'___ todo recto. (seguir)',opts:['Sigue','Sige','Sigues'],ans:'Sigue',why:'imperativo'},
   {q:'Vivo en el ___ piso. (3º)',opts:['tercer','tercero','tercera'],ans:'tercer',why:'apocope'},
   {q:'Los baños ___ arriba.',opts:['están','hay','está'],ans:'están',why:'mv. bekend'},
   {q:'El gato está ___ la cama (onder).',opts:['debajo de','encima de','entre'],ans:'debajo de',why:'onder'},
   {q:'(Ellos) están ___ . (dormir)',opts:['durmiendo','dormiendo','dormido'],ans:'durmiendo',why:'dormir → durmiendo'},
   {q:'___ a la derecha. (girar)',opts:['Gira','Gire','Giras'],ans:'Gira',why:'imperativo'},
   {q:'La ___ calle (1ª).',opts:['primera','primer','primero'],ans:'primera',why:'vrouwelijk'},
   {q:'La ropa está ___ armario.',opts:['dentro del','encima','entre'],ans:'dentro del',why:'binnen in + del'},
   {q:'___ una plaza en mi barrio.',opts:['Hay','Está','Están'],ans:'Hay',why:'una plaza = nieuw'}]});
 // VOCABULARIO
 buildMatch('vx_match',{title:'Empareja: palabra ↔ emoji',desc:'Koppel het Spaanse woord aan het juiste beeld.',per:6,pool:[
   {a:'la cocina',b:'🍳'},{a:'la cama',b:'🛏️'},{a:'el sofá',b:'🛋️'},{a:'la ducha',b:'🚿'},
   {a:'la plaza',b:'⛲'},{a:'la panadería',b:'🥖'},{a:'el parque',b:'🏞️'},{a:'el autobús',b:'🚌'},
   {a:'la bicicleta',b:'🚲'},{a:'la escalera',b:'🪜'},{a:'el ascensor',b:'🛗'},{a:'la iglesia',b:'⛪'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat in de zin past.',per:6,pool:[
   {q:'Cocino en la ___.',opts:['cocina','cama','ducha'],ans:'cocina',why:'cocinar → la cocina'},
   {q:'Duermo en la ___.',opts:['cama','mesa','silla'],ans:'cama',why:'dormir → la cama'},
   {q:'Compro pan en la ___.',opts:['panadería','farmacia','estación'],ans:'panadería',why:'pan → panadería'},
   {q:'Saco dinero en el ___.',opts:['banco','museo','cine'],ans:'banco',why:'dinero → el banco'},
   {q:'Subo al quinto piso en el ___.',opts:['ascensor','armario','espejo'],ans:'ascensor',why:'piso → ascensor'},
   {q:'Los libros están en la ___.',opts:['estantería','nevera','alfombra'],ans:'estantería',why:'libros → estantería'},
   {q:'Voy al centro en ___.',opts:['autobús','pared','esquina'],ans:'autobús',why:'transporte'},
   {q:'La leche está en la ___.',opts:['nevera','lámpara','ventana'],ans:'nevera',why:'leche → nevera'},
   {q:'Me miro en el ___.',opts:['espejo','techo','pasillo'],ans:'espejo',why:'mirar → el espejo'},
   {q:'En la ___ hay una iglesia y bancos.',opts:['plaza','cocina','terraza'],ans:'plaza',why:'plaza pública'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het juiste woord.',per:6,pool:[
   {q:'Habitación donde cocinas:',opts:['la cocina','el salón','el baño'],ans:'la cocina',why:'cocina'},
   {q:'Habitación donde duermes:',opts:['el dormitorio','el comedor','la cocina'],ans:'el dormitorio',why:'dormir'},
   {q:'Tienda donde venden pan:',opts:['la panadería','la farmacia','el banco'],ans:'la panadería',why:'pan'},
   {q:'Lugar público con árboles y bancos:',opts:['el parque','el museo','la estación'],ans:'el parque',why:'parque'},
   {q:'Mueble para sentarte y ver la tele:',opts:['el sofá','la cama','el armario'],ans:'el sofá',why:'sofá'},
   {q:'Sube y baja entre pisos (máquina):',opts:['el ascensor','la escalera','la puerta'],ans:'el ascensor',why:'ascensor'},
   {q:'Lugar de la ciudad con casas y tiendas:',opts:['el barrio','el pasillo','la pared'],ans:'el barrio',why:'barrio'},
   {q:'Transporte bajo tierra, rápido:',opts:['el metro','el taxi','la bicicleta'],ans:'el metro',why:'metro'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['el sofá','la cama','el armario','la plaza'],odd:3,why:'la plaza = barrio; de rest muebles'},
   {words:['la cocina','el baño','el salón','el parque'],odd:3,why:'el parque = barrio; de rest habitaciones'},
   {words:['la panadería','la farmacia','el banco','la cama'],odd:3,why:'la cama = mueble; de rest edificios'},
   {words:['el autobús','el metro','el taxi','el espejo'],odd:3,why:'el espejo = mueble; de rest transporte'},
   {words:['encima de','debajo de','al lado de','cocina'],odd:3,why:'cocina = geen preposición'},
   {words:['gira','sigue','cruza','plaza'],odd:3,why:'plaza = geen imperativo'},
   {words:['primero','segundo','tercero','ventana'],odd:3,why:'ventana = geen ordinaal'},
   {words:['la escalera','el ascensor','la puerta','la naranja'],odd:3,why:'la naranja = fruta; de rest casa'}]});
 // LECTURA
 buildOrder('lx_order',{title:'Ordena',desc:'Tik de items in de juiste volgorde.',rounds:[
   {sub:'la ruta a la plaza',items:[{label:'Sal de casa',key:1},{label:'Sigue todo recto',key:2},{label:'Gira a la derecha',key:3},{label:'Cruza el semáforo',key:4},{label:'Llegas a la plaza',key:5}]},
   {sub:'de fuera a dentro',items:[{label:'la calle',key:1},{label:'la puerta',key:2},{label:'el pasillo',key:3},{label:'el salón',key:4}]},
   {sub:'los pisos (de abajo a arriba)',items:[{label:'la planta baja',key:1},{label:'el primer piso',key:2},{label:'el segundo piso',key:3},{label:'el tercer piso',key:4}]},
   {sub:'la ficha del anuncio',items:[{label:'Tercer piso',key:1},{label:'2 habitaciones',key:2},{label:'Terraza con vistas',key:3},{label:'600 €/mes',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in het anuncio en de tekst, en kies het juiste antwoord.',per:6,pool:[
   {q:'¿En qué piso está el apartamento?',opts:['Tercer piso','Planta baja','Primer piso'],ans:'Tercer piso',why:'«Tercer piso con ascensor»'},
   {q:'¿Cuántas habitaciones tiene?',opts:['2','3','1'],ans:'2',why:'«dos habitaciones»'},
   {q:'¿Cuánto cuesta al mes?',opts:['600 €','300 €','900 €'],ans:'600 €',why:'«seiscientos euros al mes»'},
   {q:'¿Qué hay enfrente de la casa de Valen?',opts:['una plaza','un banco','una estación'],ans:'una plaza',why:'«Enfrente de mi casa hay una plaza»'},
   {q:'¿Dónde está la panadería?',opts:['al lado','lejos','arriba'],ans:'al lado',why:'«La panadería está al lado»'},
   {q:'¿Qué están haciendo los niños?',opts:['jugando','cocinando','durmiendo'],ans:'jugando',why:'«los niños están jugando»'},
   {q:'¿El piso tiene terraza?',opts:['Sí','No','No se sabe'],ans:'Sí',why:'«terraza con vistas a la plaza»'},
   {q:'¿Cómo son las casas del barrio?',opts:['de colores','grises','muy altas'],ans:'de colores',why:'«casas de colores»'}]});
}

renderFC();renderTable();gameHayEsta();gamePrepo();renderLectura();buildRecorders();buildInlineExercises();
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='U7_web_mijn_versie.html';a.click();};
})();
"""

# Getypte woordenschat-drills (fase ophalen + produceren) in het paneel zelf.
JS += hub_type_sets.vocab_type_js(vocab)
JS += hub_type_gram.js('C5', 7)
JS += hub_bloques.retos_js('retos_u7', 'C5', 7)
JS += (hub_bloques.escucha_js("esc_u7", escucha_data.C5_U7)
       + hub_bloques.lectura_js("lec_u7", lectura_data.C5_U7))
HTML = HTML.replace("__GRAMSLOTS__", hub_type_gram.slots('C5', 7))
HTML = HTML.replace("__NGAMES__", str(len(GAMES)))
HTML = HTML.replace("__BRONNEN__", extra_bronnen.html('C5', 7))
HTML = HTML.replace("__TYPESLOTS__", hub_type_sets.SLOTS_HTML)

# Het rollenspel: offline oefenpartner in het Hablar-paneel.
_rol = gen_rol.componente("C5", 7)
if _rol:
    _rol_html, _rol_css, _rol_js = _rol
    HTML = HTML.replace("__ROL__", _rol_html)
    CSS += _rol_css
    JS += _rol_js
else:
    HTML = HTML.replace("__ROL__", "")

html=(HTML.replace("__CSS__",CSS).replace("__MOCH__",moch).replace("__FC__",flashcards_html())
      .replace("__NAS__",naslag_html()).replace("__MAP__",mapsvg).replace("__DATA__",data_js()).replace("__JS__",JS))
os.makedirs(f"{ROOT}/03-build/web",exist_ok=True)
open(f"{ROOT}/03-build/web/U7_web.html","w").write(html)
print("U7_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
