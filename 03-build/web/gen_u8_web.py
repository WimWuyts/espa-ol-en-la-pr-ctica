#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C5 · U5 «¡Ñam!».
# Eén standalone bestand: fonts base64, de 21 U5-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U5-vocab), visuele/interactieve grammatica (cantidades · ir a + inf · lo/la/los/las),
# klikbare kaart (mundo hispano, parada 5 = México) + TTS + inline recorder + Lectura + editbar. Huisstijl groen.
import json, base64, os, sys
import hub_drills
import hub_iconos
import hub_type_sets
import hub_type_gram
import extra_bronnen
import hub_bloques
import escucha_data, lectura_data
import gen_coach
import gen_rol
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
GEN = f"{ROOT}/02-huisstijl/beeld/generators"
sys.path.insert(0, GEN); import cast_gen as C; import vocab_icons as VI; import vocab_emoji as VE
vocab = json.load(open(f"{ROOT}/01-cursussen/05-a1/U8/u8_vocab.json", encoding="utf-8"))
mapsvg = open(f"{GEN}/mundo_map_real.svg").read()
moch = C.mochila("100%", "map")
# ---- U8-emoji: lokale dict (vocab_emoji.py NIET aanraken) ----
def norm(w): return VE._norm(w)
EXTRA_RAW = {
 "el viaje":"✈️","las vacaciones":"🏖️","el billete":"🎫","la maleta":"🧳","el pasaporte":"🛂",
 "el hotel":"🏨","la playa":"🏖️","la montaña":"⛰️","el mar":"🌊","el/la turista":"🧳","la foto":"📷",
 "el recuerdo":"🎁","la excursión":"🥾","el mapa":"🗺️","viajar":"✈️","visitar":"🏛️",
 "hace sol":"☀️","hace calor":"🥵","hace frío":"🥶","hace viento":"💨","hace buen tiempo":"🌤️",
 "hace mal tiempo":"🌧️","llueve":"🌧️","la lluvia":"🌧️","nieva":"❄️","la nieve":"❄️",
 "está nublado":"☁️","la tormenta":"⛈️","la temperatura":"🌡️","el grado":"🌡️","el paraguas":"☂️","la nube":"☁️",
 "el avión":"✈️","el tren":"🚆","el autobús":"🚌","el barco":"🚢","el coche":"🚗","la bicicleta":"🚲",
 "el metro":"🚇","a pie":"🚶","el aeropuerto":"🛫","la estación":"🚉",
 "hoy":"📅","esta semana":"🗓️","este año":"🗓️","ya":"✅","todavía no":"⏳","nunca":"🚫",
 "alguna vez":"❓","muchas veces":"🔁","este mes":"🗓️","últimamente":"⏱️",
 "hecho":"🔨","visto":"👁️","dicho":"💬","escrito":"✍️","vuelto":"🔙","puesto":"📥","abierto":"🔓","roto":"💔",
 "Machu Picchu":"🏔️","los Andes":"🏔️","la llama":"🦙","las ruinas":"🏛️",
}
EXTRA = {norm(k): v for k, v in EXTRA_RAW.items()}
ICONS=[f'<div class="fcico">{EXTRA.get(norm(v.get("es",""))) or VE.emoji_for(v.get("es",""),v.get("grp",""))}</div>' for v in vocab]

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
   ['viajes-memoria', 'memoria de los viajes', 'memory'],
   ['clima-memoria', 'el tiempo y el clima', 'memory'],
   ['participio-infinitivo', 'participio ↔ infinitivo', 'match'],
   ['pais-clima', 'país ↔ clima', 'match']]],
 ['② Distinguir · gramática/léxico', [
   ['regular-irregular', '¿participio regular o irregular?', 'classify'],
   ['que-tiempo', '¿qué tiempo hace?', 'classify'],
   ['marcador', '¿periodo o experiencia?', 'classify']]],
 ['③ Producir con apoyo', [
   ['haber-participio', 'completa: haber + participio', 'cloze'],
   ['participio-irregular', 'el participio irregular', 'cloze'],
   ['ya-todavia', '¿ya, todavía no o…?', 'cloze'],
   ['haber-tetris', 'haber: pinball', 'pinball'],
   ['diario-order', 'ordena el diario de viaje', 'order'],
   ['senala-viaje', 'señala en el viaje', 'point']]],
 ['④ Analizar & comunicar', [
   ['cuenta-viaje', '¡cuenta tu viaje!', 'sim']]],
 ['⑤ Hablar · grábate 🎙️', [
   ['repite-tiempo', 'escucha y repite: el viaje', 'speak'],
   ['shadowing-nina', 'shadowing con Nina', 'speak'],
   ['mensaje-viaje', 'mensaje de voz: tu viaje', 'speak'],
   ['describe-vacaciones', 'describe tus vacaciones', 'speak']]],
]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-u8-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-u8-{s}.html")}

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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="viajes">viajes</option><option value="clima">el clima</option><option value="transporte">transporte</option><option value="experiencias">experiencias/marcadores</option><option value="participios">participios</option><option value="peru">Perú</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Español en la práctica · U8 ¿Qué has hecho?</title>
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
    <div><h1>U8 · ¿Qué has hecho?</h1>
    <p>La página digital de la Unidad 8 (parada <b>Perú · Cusco · Machu Picchu</b>): flashcards, gramática visual e interactiva y <b>__NGAMES__ juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U8. Klik om te draaien; wissel ES↔NL; filter per groep; klik 🔊 om te horen. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
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
    <p class="lead">Eerst betekenis en patroon ontdekken, dan de regel. Beweeg over de woorden, klik, en probeer. <span class="gloss">Alles binnen het thema van U8: perfecto compuesto, participios, marcadores y el tiempo.</span></p>
    <div class="card" id="colorsent"></div>
    <div class="card" id="irconj"></div>
    <h3 class="subh">🧱 Perfecto compuesto — construye y practica</h3>
    <div class="card ex" id="gx_build"></div>
    <div class="card ex" id="gx_iraq"></div>
    <h3 class="subh">⚙️ Participios — ¿regular o irregular?</h3>
    <div class="game" id="g_cantidad"></div>
    <div class="card ex" id="gx_conc"></div>
    <div class="card ex" id="gx_cantq"></div>
    <h3 class="subh">⏳ Marcadores — ya / todavía no</h3>
    <div class="game" id="g_pron"></div>
    <div class="card ex" id="gx_pronq"></div>
    <h3 class="subh">🎯 Repaso mixto — rellena con feedback</h3>
    <div class="card ex" id="gx_mix"></div>
  __GRAMSLOTS__
  </section>

  <section class="panel" data-p="lectura">
    <h2 class="sec">Lectura · El diario de viaje de Nina</h2>
    <p class="lead">Lees het <b>reisdagboek</b> van Nina, <b>luister</b> het (🔊 TTS) en <b>controleer je begrip</b>. Daarna vertel je je eigen dag — dat neem je op in het tabblad <b>Hablar</b>. <span class="gloss">Keten: lezen → luisteren → spreken.</span></p>
    <div id="lecturawrap"></div>
    <h3 class="subh">🔢 Ordena el viaje</h3>
    <div class="card ex" id="lx_order"></div>
    <h3 class="subh">🔎 Comprensión · escanea y escoge</h3>
    <div class="card ex" id="lx_scan"></div>
    <h2 class="sec">Lectura completa · ¿Qué tipo de viajero eres?</h2>
    <p class="lead">Een echte tijdschrifttest met de volledige leesroute: <b>voorspellen → globaal → scannen → juist/fout met bewijs → betekenis uit de context → zelf schrijven</b>. <span class="gloss">Dezelfde tekst staat in je cursus, met schrijfruimte.</span></p>
    <div class="card ex" id="lec_u8"></div>
  </section>

  <section class="panel" data-p="escuchar">
    <h2 class="sec">Escuchar · El tiempo en los Andes 🎧</h2>
    <p class="lead">Het weerbericht van acht uur op de radio van Cusco. Eén fragment, zes stappen: eerst <b>weten waar je bent</b>, dan <b>globaal</b> luisteren, dan de <b>details</b>, dan <b>juist/fout met bewijs</b>. Het <b>transcript</b> gaat pas open als je klaar bent — anders lees je mee in plaats van te luisteren. <span class="gloss">Zolang er nog geen opname is, leest de computerstem het fragment voor.</span></p>
    <div class="card ex" id="esc_u8"></div>
  </section>
  <section class="panel" data-p="juegos">
    <h2 class="sec">Ejercicios · __NGAMES__ juegos, jij kiest</h2>
    <p class="lead">Geordend van <b>herkennen → onderscheiden → produceren met steun → analyseren &amp; communiceren → hablar</b>. Elk spel geeft directe, verklarende feedback en de steun bouwt af. <span class="gloss">Klik een spel; het opent in een venster en werkt ook offline.</span></p>
    <div id="motorlink"></div>
  </section>

  <section class="panel" data-p="retos">
    <h2 class="sec">Retos · tres desafíos 🎯</h2>
    <p class="lead">Drie retos met <b>één harde regel</b>: je presenteert het weer van drie Peruaanse steden in <b>één minuut</b>, je schrijft een kaart aan wie je in september was met <b>ya, todavía no en nunca</b> elk precies één keer, en je vertelt een Nederlandse reisblog na in het Spaans — samenvattend, niet woord voor woord. <span class="gloss">De zeven andere retos van deze unit staan in het boek en in de PowerPoint.</span></p>
    <div id="retos_u8"></div>
      __COACH__
  </section>
  <section class="panel" data-p="hablar">
    __ROL__
    <h2 class="sec">Hablar · grábate 🎙️</h2>
    <p class="lead">Neem <b>jezelf</b> op: luister naar het model, spreek in, luister terug, en neem opnieuw op. <span class="gloss">Werkt in Chrome/Edge; sta de micro toe. Print blijft bruikbaar zonder opname.</span></p>
    <div class="card" id="rec_repite"></div>
    <div class="card" id="rec_pedido"></div>
    <div class="card" id="rec_plato"></div>
    <p class="lead" style="margin-top:8px">Meer spreek-/opnamespellen (shadowing con Nina, describe…) vind je ook onder <b>Juegos ⑤</b>.</p>
  </section>

  <section class="panel" data-p="cultura">
    <h2 class="sec">Cultura · Viajar por los Andes</h2>
    <p class="lead">Nuestra última parada: <b>Perú</b> 🇵🇪. Un país con <b>tres climas</b> — costa, sierra (los Andes) y selva. Descubre <b>Machu Picchu</b>, las <b>llamas</b> y por qué el tiempo cambia tanto. <span class="gloss">Peru heeft drie klimaten in één land; ontdek Machu Picchu, de lama's en het weer in de Andes.</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m8 3 4 8 5-5 5 15H2L8 3z"/></svg>Machu Picchu 🏔️ 🇵🇪</h3>
      <p>La ciudad <b>inca</b>, a 2430 metros de altura. Se llega en <b>tren</b> desde Cusco y luego a pie. Es una de las <b>siete maravillas</b> del mundo moderno. Nina la <b>ha visitado</b> hoy. <span class="gloss">Machu Picchu is het symbool van Peru: een Inca-stad in de bergen, bereikbaar met de trein vanuit Cusco.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20"/><path d="M2 12h20"/></svg>Los Andes y las llamas 🦙</h3>
      <p>La <b>sierra</b> (los Andes) es alta y fría. Allí viven las <b>llamas</b> y las <b>alpacas</b>. En <b>Cusco</b>, la antigua capital <b>inca</b> (3400 m), <b>hace frío</b> por la noche incluso en verano. <span class="gloss">De sierra is hoog en koud; er leven lama's en alpaca's. In Cusco is het 's nachts koud, zelfs in de zomer.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Los tres climas de Perú 🌦️</h3>
      <p><b>ES:</b> En Perú puedes tener <b>tres climas en un solo día</b>: sol en la costa, frío en la sierra y lluvia en la selva. Por eso Nina siempre lleva un <b>abrigo</b> y un <b>paraguas</b>. <span class="gloss">In Peru kun je drie klimaten op één dag hebben; daarom neemt Nina altijd een jas én een paraplu mee.</span></p>
      <div class="platos">
        <div class="pl"><div class="em">🌊</div><div class="nm">la costa</div><small>Lima · hace sol, seco</small></div>
        <div class="pl"><div class="em">🏔️</div><div class="nm">la sierra</div><small>Cusco · hace frío, nieva</small></div>
        <div class="pl"><div class="em">🌴</div><div class="nm">la selva</div><small>el Amazonas · hace calor, llueve</small></div>
        <div class="pl"><div class="em">🦙</div><div class="nm">la llama</div><small>animal de los Andes</small></div>
        <div class="pl"><div class="em">🚆</div><div class="nm">el tren</div><small>a Machu Picchu</small></div>
      </div>
      <p><span class="gloss">¡Ojo! «Het is warm (weer)» = «hace calor» (niet «es caliente»). Symbolen van de ruta: la Sagrada Família 🇪🇸 · los tacos 🇲🇽 · Cartagena 🇨🇴 · Machu Picchu 🇵🇪.</span></p></div>
    <h3 class="subh">📍 La Ruta · ¿dónde estamos?</h3>
    <p class="lead">Onze parada 8: <b>Perú · Cusco · Machu Picchu</b> 🇵🇪 — de laatste halte van jaar 5. <b>Klik op een groen land</b> op de kaart voor info.</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een groen land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    __BRONNEN__
  </section>

  <div class="foot">Español en la práctica · C5 · Unidad 8 «¿Qué has hecho?» — página digital. Uitbreiding op de PDF · huisstijl groen · print ↔ PowerPoint ↔ web.</div>
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

// ---- GRAMMAR-VIZ 1: kleurgecodeerde perfecto-compuesto-zin ----
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Pretérito perfecto compuesto — haber + participio</h3>'+
'<div class="csent">'+
'<span style="background:#dbeafe;color:#1e40af">(Yo)<span class="tip">onderwerp</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">he<span class="tip">haber · presente (he, has, ha…)</span></span> '+
'<span style="background:#dcfce7;color:#166534">visto<span class="tip">participio (hier onregelmatig: ver → visto)</span></span> '+
'<span style="background:#ccfbf1;color:#0f766e">Machu Picchu<span class="tip">voorwerp/plaats</span></span> '+
'<span style="background:#ede9fe;color:#5b21b6">hoy<span class="tip">marcador (periode die nog loopt)</span></span>.</div>'+
'<div class="legend"><span><i style="background:#93c5fd"></i>onderwerp</span><span><i style="background:#fdba74"></i>haber</span><span><i style="background:#86efac"></i>participio</span><span><i style="background:#5eead4"></i>voorwerp</span><span><i style="background:#c4b5fd"></i>marcador</span></div>'+
'<p class="gloss" style="margin-top:8px">🔴 Auxiliar = <b>haber</b> (niet tener). De participio blijft <b>gelijk</b>: ella ha comid<b>o</b>. · '+(TTS?'<button class="spk-btn" onclick="speak(\'He visto Machu Picchu hoy\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: haber (presente) — klik om te onthullen ----
(function(){const el=document.getElementById('irconj');
 const R=[['yo','he'],['tú','has'],['él/ella','ha'],['nosotros','hemos'],['vosotros','habéis'],['ellos','han']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">El auxiliar «haber» — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">Denk eerst zelf de vorm; klik dan de kaart. Daarna: forma + participio.</p><div class="conjgrid" id="icg"></div>';
 const g=el.querySelector('#icg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v+' + …';if(TTS)speak(p+' '+v+' viajado');};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: ¿participio regular o irregular? ----
function gameCantidad(){const el=document.getElementById('g_cantidad');
 const items=[['viajar','viajado','-ar → -ado'],['comer','comido','-er → -ido'],['vivir','vivido','-ir → -ido'],['hacer','hecho','irregular'],['ver','visto','irregular'],['escribir','escrito','irregular'],['volver','vuelto','irregular'],['poner','puesto','irregular'],['abrir','abierto','irregular'],['romper','roto','irregular'],['decir','dicho','irregular'],['estudiar','estudiado','-ar → -ado']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿Cuál es el participio?</h3><p class="desc">Kies het juiste deelwoord (let op de onregelmatige).</p>'+scoreBar('sbC')+'<div id="cW" style="font-size:24px;font-family:var(--disp);text-align:center;margin:8px 0"><b></b> → ___</div><div class="chips" id="cC" style="justify-content:center"></div><div class="fb" id="cFb"></div>';
 const sb=el.querySelector('#sbC');const cont=el.querySelector('#cC');
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#cW b').textContent=el.cur[0];
   // bouw 3 opties: juiste + 2 afleiders
   const wrong=['viajado','comido','hecho','visto','escrito','puesto','abierto','vuelto','dicho','roto'].filter(x=>x!==el.cur[1]);
   for(let k=wrong.length-1;k>0;k--){const j=Math.floor(Math.random()*(k+1));[wrong[k],wrong[j]]=[wrong[j],wrong[k]];}
   const opts=[el.cur[1],wrong[0],wrong[1]];for(let k=opts.length-1;k>0;k--){const j=Math.floor(Math.random()*(k+1));[opts[k],opts[j]]=[opts[j],opts[k]];}
   cont.innerHTML='';opts.forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
   el.querySelector('#cFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#cFb'),ok,(ok?'¡Sí! ':'Nee → ')+el.cur[0]+' → '+el.cur[1]+' ('+el.cur[2]+').');setTimeout(next,1050);}
 next();}
// ---- GRAMMAR-VIZ 4: ¿ya o todavía no? ----
function gamePron(){const el=document.getElementById('g_pron');
 const items=[['He hecho la maleta. ✅','ya','klaar'],['He reservado el hotel. ⏳','todavía no','nog niet'],['Hemos comprado los billetes. ✅','ya','klaar'],['He visto Machu Picchu. ⏳','todavía no','nog niet'],['He desayunado. ✅','ya','klaar'],['He llamado al hotel. ⏳','todavía no','nog niet'],['Me he puesto el abrigo. ✅','ya','klaar'],['He comido. ⏳','todavía no','nog niet']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿ya o todavía no?</h3><p class="desc">Kies volgens ✅ (klaar) of ⏳ (nog niet).</p>'+scoreBar('sbP')+'<div id="pQ" style="font-size:19px;font-family:var(--disp);text-align:center;margin:10px 0"></div><div class="chips" id="pC" style="justify-content:center"></div><div class="fb" id="pFb"></div>';
 const sb=el.querySelector('#sbP');const cont=el.querySelector('#pC');
 ['ya','todavía no'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#pQ').textContent='___ '+el.cur[0];el.querySelector('#pFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#pFb'),ok,(ok?'¡Sí! ':'Nee → ')+el.cur[1]+' ('+el.cur[2]+').');setTimeout(next,1000);}
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
   const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "✈️ Para visitar: Chichén Itzá y las playas de Cancún", "star": 1, "nl": "Parada anterior (U5–U6) · CDMX · los mercados (Diego)"}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "✈️ Para visitar: la Sagrada Familia y la Alhambra", "star": 1, "nl": "Parada anterior (U0–U4) · Madrid · Sevilla · Barcelona · València"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "✈️ Para visitar: Cartagena y el Eje Cafetero", "star": 1, "nl": "Parada anterior (U7) · Cartagena (Valen)"}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "✈️ Para visitar: Machu Picchu, maravilla del mundo", "star": 1, "nl": "★ ¡Estás aquí! Parada U8 · Cusco · Machu Picchu (Nina)"}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "✈️ Para visitar: las cataratas del Iguazú y la Patagonia", "star": 0, "nl": ""}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "✈️ Para visitar: el Salto Ángel, la cascada más alta", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "✈️ Para visitar: el desierto de Atacama y la isla de Pascua", "star": 0, "nl": ""}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "✈️ Para visitar: las islas Galápagos", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "✈️ Para visitar: Tikal, ciudad maya en la selva", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "✈️ Para visitar: La Habana y las playas de Varadero", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "✈️ Para visitar: el Salar de Uyuni", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "✈️ Para visitar: Punta Cana y sus playas", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "✈️ Para visitar: las ruinas mayas de Copán", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "✈️ Para visitar: las misiones jesuíticas", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "✈️ Para visitar: la isla de Ometepe y sus volcanes", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "✈️ Para visitar: la Ruta de las Flores y el surf", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "✈️ Para visitar: los volcanes y los parques nacionales", "star": 0, "nl": ""}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "✈️ Para visitar: el Canal de Panamá", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "✈️ Para visitar: Punta del Este y Colonia del Sacramento", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "✈️ Para visitar: el Viejo San Juan y El Yunque", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "✈️ Para visitar: la isla de Bioko y sus playas", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "✈️ Para visitar: Miami, Los Ángeles y el suroeste hispano", "star": 0, "nl": ""}};
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
 const M=[{n:'Día 1 · Cusco 🇵🇪',raw:'Lunes. ¡Por fin he llegado a Cusco! He viajado en avión desde Lima. Aquí, a 3400 metros, hace frío y está nublado. Esta tarde he visto la Plaza de Armas y he comido un plato típico. Todavía no he subido a la montaña.',
    html:'<div class="sec2">Lunes</div><p style="margin:4px 0">¡Por fin <b>he llegado</b> a Cusco! <b>He viajado</b> en avión desde Lima. Aquí, a 3400 metros, <b>hace frío</b> y <b>está nublado</b>. Esta tarde <b>he visto</b> la Plaza de Armas y <b>he comido</b> un plato típico. Todavía no <b>he subido</b> a la montaña.</p>'},
   {n:'Día 2 · Machu Picchu 🇵🇪',raw:'Martes. ¡Qué día! He cogido el tren muy pronto y he subido a Machu Picchu. Ha hecho sol toda la mañana. He visto las llamas y he sacado mil fotos. He escrito una postal para mi familia. ¡Nunca he estado tan feliz!',
    html:'<div class="sec2">Martes</div><p style="margin:4px 0">¡Qué día! <b>He cogido</b> el tren muy pronto y <b>he subido</b> a Machu Picchu. <b>Ha hecho sol</b> toda la mañana. <b>He visto</b> las llamas y <b>he sacado</b> mil fotos. <b>He escrito</b> una postal para mi familia. ¡Nunca <b>he estado</b> tan feliz!</p>'}];
 el.innerHTML='<div class="perfiles">'+M.map((m,i)=>'<div class="menucard"><h4>📔 '+m.n+' '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lm'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div id="lm'+i+'" data-raw="'+m.raw.replace(/"/g,'&quot;')+'">'+m.html+'</div></div>').join('')+'</div>';
 const items=[['Nina ha viajado en avión a Cusco.',true,'«He viajado en avión desde Lima»'],['En Cusco hace calor.',false,'«hace frío y está nublado»'],['Nina ha subido a Machu Picchu.',true,'«he subido a Machu Picchu»'],['El día 1 ya ha subido a la montaña.',false,'«Todavía no he subido a la montaña»'],['En Machu Picchu ha hecho sol.',true,'«Ha hecho sol toda la mañana»'],['Nina ha escrito una postal.',true,'«He escrito una postal para mi familia»'],['Nina ha cogido el tren a Machu Picchu.',true,'«He cogido el tren muy pronto»'],['Nina ha visto las llamas.',true,'«He visto las llamas»']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — comprueba tu comprensión (con evidencia)</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Tu propio día de viaje</h3><p class="gloss" style="margin:0 0 8px">Schrijf, zoals Nina, één dagboekdag met minstens vier keer perfecto compuesto + het weer. Neem het daarna op onder <b>Hablar 🎙️</b> («describe tus vacaciones»).</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="Hoy he llegado a… He visto… Ha hecho…"></textarea>';
 el.appendChild(box);el.appendChild(resp);}

// ---------- INLINE RECORDER (MediaRecorder) ----------
""" + hub_drills.RECORDER_JS + r"""
function buildRecorders(){
 makeRecorder('rec_repite',{title:'Escucha y repite: el viaje y el tiempo',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'Hoy he subido a Machu Picchu.',cue:'perfecto compuesto',tip:'Duidelijk uitgesproken? Probeer nog eens.'},{text:'He viajado en avión desde Lima.',cue:'transporte'},{text:'Aquí hace frío y está nublado.',cue:'el tiempo'},{text:'¿Qué has hecho hoy?',cue:'pregunta'},{text:'Nunca he visto la nieve.',cue:'marcador'}]});
 makeRecorder('rec_pedido',{title:'Mensaje de voz: cuenta tu viaje',desc:'Neem één bericht op. Doel: vertellen wat je gedaan hebt. Gebruik: he ido a · he visto · he viajado en · ha hecho…',items:[
   {text:'Cuenta qué has hecho estas vacaciones (30 s): ¿adónde has ido? ¿qué has visto? ¿qué tiempo ha hecho?',cue:'las vacaciones',tip:'3 zinnen met perfecto compuesto + het weer? Neem opnieuw op.'}]});
 makeRecorder('rec_plato',{title:'Describe tus vacaciones',desc:'Beschrijf je vakantie: ¿adónde has ido? ¿qué has hecho? ¿qué tiempo ha hecho?',items:[
   {text:'Estas vacaciones he ido a ___ . He visto ___ . Ha hecho ___ .',cue:'tu versión',tip:'Heb je gezegd waar je bent geweest, wat je gedaan hebt en het weer? Herneem.'}]});
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
 buildOrder('gx_build',{title:'Construye: haber + participio',desc:'Tik de blokjes in de juiste volgorde (onderwerp → haber → participio → resto).',rounds:[
   {sub:'yo · subir',items:[{label:'Yo',key:1},{label:'he',key:2},{label:'subido',key:3},{label:'a Machu Picchu',key:4}]},
   {sub:'tú · ver',items:[{label:'¿Tú',key:1},{label:'has',key:2},{label:'visto',key:3},{label:'las llamas?',key:4}]},
   {sub:'nosotros · viajar',items:[{label:'Nosotros',key:1},{label:'hemos',key:2},{label:'viajado',key:3},{label:'en tren',key:4}]},
   {sub:'ella · escribir',items:[{label:'Nina',key:1},{label:'ha',key:2},{label:'escrito',key:3},{label:'una postal',key:4}]},
   {sub:'ellos · comer',items:[{label:'Ellos',key:1},{label:'han',key:2},{label:'comido',key:3},{label:'un ceviche',key:4}]},
   {sub:'yo · negativo',items:[{label:'Todavía no',key:1},{label:'(yo) he',key:2},{label:'comido',key:3},{label:'hoy',key:4}]},
   {sub:'vosotros · hacer',items:[{label:'¿Vosotros',key:1},{label:'habéis',key:2},{label:'hecho',key:3},{label:'la maleta?',key:4}]},
   {sub:'él · volver',items:[{label:'Diego',key:1},{label:'ha',key:2},{label:'vuelto',key:3},{label:'del viaje',key:4}]}]});
 buildChoice('gx_iraq',{title:'Mini-quiz: haber + participio',desc:'Kies de juiste vorm van het perfecto compuesto. Directe feedback.',per:6,pool:[
   {q:'(Yo) ___ a Machu Picchu.',opts:['he subido','has subido','he subir'],ans:'he subido',why:'yo → he + subido'},
   {q:'¿(Tú) ___ las llamas?',opts:['has visto','he visto','has veído'],ans:'has visto',why:'tú → has + visto (irreg.)'},
   {q:'(Nosotros) ___ muchas fotos.',opts:['hemos sacado','han sacado','hemos sacar'],ans:'hemos sacado',why:'nosotros → hemos + sacado'},
   {q:'Nina ___ un diario.',opts:['ha escrito','ha escribido','han escrito'],ans:'ha escrito',why:'ella → ha + escrito (irreg.)'},
   {q:'(Ellos) ___ en tren.',opts:['han viajado','ha viajado','han viajar'],ans:'han viajado',why:'ellos → han + viajado'},
   {q:'¿(Vosotros) ___ la maleta?',opts:['habéis hecho','han hecho','habéis hacido'],ans:'habéis hecho',why:'vosotros → habéis + hecho'},
   {q:'Diego ___ del viaje.',opts:['ha vuelto','ha volvido','han vuelto'],ans:'ha vuelto',why:'él → ha + vuelto (irreg.)'},
   {q:'¿Qué ___ (tú) hoy?',opts:['has hecho','he hecho','has hacido'],ans:'has hecho',why:'tú → has + hecho'},
   {q:'(Yo) ___ un ceviche.',opts:['he comido','has comido','he comer'],ans:'he comido',why:'yo → he + comido'},
   {q:'Lucía ___ el mar.',opts:['ha visto','ha veído','han visto'],ans:'ha visto',why:'ella → ha + visto'},
   {q:'(Nosotros) ___ a la montaña.',opts:['hemos subido','han subido','hemos subir'],ans:'hemos subido',why:'nosotros → hemos + subido'},
   {q:'Este año (yo) ___ mucho.',opts:['he estudiado','has estudiado','he estudiar'],ans:'he estudiado',why:'yo → he + estudiado'}]});
 buildMatch('gx_conc',{title:'Empareja: infinitivo ↔ participio',desc:'Koppel het werkwoord aan het juiste deelwoord (let op de onregelmatige).',per:6,pool:[
   {a:'hacer',b:'hecho'},{a:'ver',b:'visto'},{a:'decir',b:'dicho'},{a:'escribir',b:'escrito'},
   {a:'volver',b:'vuelto'},{a:'poner',b:'puesto'},{a:'abrir',b:'abierto'},{a:'romper',b:'roto'},
   {a:'viajar',b:'viajado'},{a:'comer',b:'comido'},{a:'vivir',b:'vivido'},{a:'subir',b:'subido'}]});
 buildChoice('gx_cantq',{title:'Mini-quiz: participio irregular',desc:'Kies het juiste onregelmatige deelwoord.',per:6,pool:[
   {q:'hacer → he ___',opts:['hecho','hacido','hacado'],ans:'hecho',why:'hacer → hecho'},
   {q:'ver → has ___',opts:['visto','veído','vido'],ans:'visto',why:'ver → visto'},
   {q:'decir → ha ___',opts:['dicho','decido','dijido'],ans:'dicho',why:'decir → dicho'},
   {q:'escribir → hemos ___',opts:['escrito','escribido','escribto'],ans:'escrito',why:'escribir → escrito'},
   {q:'volver → habéis ___',opts:['vuelto','volvido','volto'],ans:'vuelto',why:'volver → vuelto'},
   {q:'poner → han ___',opts:['puesto','ponido','posto'],ans:'puesto',why:'poner → puesto'},
   {q:'abrir → he ___',opts:['abierto','abrido','abrto'],ans:'abierto',why:'abrir → abierto'},
   {q:'romper → has ___',opts:['roto','rompido','rompto'],ans:'roto',why:'romper → roto'},
   {q:'ver → nunca he ___ el mar',opts:['visto','veído','vido'],ans:'visto',why:'ver → visto'},
   {q:'poner → me he ___ el abrigo',opts:['puesto','ponido','puestado'],ans:'puesto',why:'poner → puesto'}]});
 buildChoice('gx_pronq',{title:'Mini-quiz: marcadores',desc:'Kies de marcador die past (ya · todavía no · nunca · alguna vez · hoy).',per:6,pool:[
   {q:'___ he hecho la maleta. ✅',opts:['Ya','Todavía no','Nunca'],ans:'Ya',why:'klaar → ya'},
   {q:'___ he reservado el hotel. ⏳',opts:['Todavía no','Ya','Muchas veces'],ans:'Todavía no',why:'nog niet → todavía no'},
   {q:'¿Has viajado ___ en barco? (ooit)',opts:['alguna vez','ya','hoy'],ans:'alguna vez',why:'ooit → alguna vez'},
   {q:'___ he estado en Perú. (nooit)',opts:['Nunca','Ya','Esta semana'],ans:'Nunca',why:'nooit → nunca'},
   {q:'___ he estudiado dos horas. (vandaag)',opts:['Hoy','Nunca','Alguna vez'],ans:'Hoy',why:'vandaag → hoy'},
   {q:'He visto esa peli ___. (vaak)',opts:['muchas veces','todavía no','hoy'],ans:'muchas veces',why:'vaak → muchas veces'},
   {q:'—¿Has comido? —No, ___.',opts:['todavía no','ya','alguna vez'],ans:'todavía no',why:'nog niet'},
   {q:'—¿Has hecho los deberes? —Sí, ___.',opts:['ya','nunca','todavía no'],ans:'ya',why:'al klaar → ya'},
   {q:'___ he viajado a México. (dit jaar)',opts:['Este año','Nunca','Alguna vez'],ans:'Este año',why:'dit jaar → este año'},
   {q:'___ he visto la nieve. (nog nooit)',opts:['Nunca','Ya','Hoy'],ans:'Nunca',why:'nooit → nunca'}]});
 buildChoice('gx_mix',{title:'Repaso mixto: rellena',desc:'Alles door elkaar: perfecto compuesto · participios · marcadores · el tiempo.',per:8,pool:[
   {q:'(Nosotros) ___ a Perú.',opts:['hemos viajado','han viajado','he viajado'],ans:'hemos viajado',why:'nosotros → hemos + viajado'},
   {q:'¿Qué ___ (tú) hoy?',opts:['has hecho','he hecho','has hacido'],ans:'has hecho',why:'tú → has + hecho'},
   {q:'En Cusco ___ frío.',opts:['hace','está','llueve'],ans:'hace',why:'hace frío'},
   {q:'Nina ___ una postal.',opts:['ha escrito','ha escribido','han escrito'],ans:'ha escrito',why:'ella → ha + escrito'},
   {q:'Hoy ___ nublado.',opts:['está','hace','nieva'],ans:'está',why:'está nublado'},
   {q:'Todavía no ___ (yo) a la montaña.',opts:['he subido','has subido','he subir'],ans:'he subido',why:'yo → he + subido'},
   {q:'poner → me he ___ el abrigo',opts:['puesto','ponido','posto'],ans:'puesto',why:'poner → puesto'},
   {q:'En la selva ___ mucho.',opts:['llueve','hace','está'],ans:'llueve',why:'llueve = het regent'},
   {q:'¿(Tú) ___ el mar alguna vez?',opts:['has visto','he visto','has veído'],ans:'has visto',why:'tú → has + visto'},
   {q:'Nunca ___ (yo) en avión.',opts:['he viajado','has viajado','he viajar'],ans:'he viajado',why:'yo → he + viajado'},
   {q:'ver → has ___',opts:['visto','veído','vido'],ans:'visto',why:'ver → visto'},
   {q:'Ellos ___ a la cima.',opts:['han llegado','ha llegado','han llegar'],ans:'han llegado',why:'ellos → han + llegado'}]});
 // VOCABULARIO
 buildMatch('vx_match',{title:'Empareja: palabra ↔ emoji',desc:'Koppel het Spaanse woord aan het juiste beeld (viajes & clima).',per:6,pool:[
   {a:'el avión',b:'✈️'},{a:'el tren',b:'🚆'},{a:'el barco',b:'🚢'},{a:'la maleta',b:'🧳'},
   {a:'hace sol',b:'☀️'},{a:'hace frío',b:'🥶'},{a:'llueve',b:'🌧️'},{a:'nieva',b:'❄️'},
   {a:'la montaña',b:'⛰️'},{a:'la playa',b:'🏖️'},{a:'el paraguas',b:'☂️'},{a:'la llama',b:'🦙'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat in de zin past.',per:6,pool:[
   {q:'Para el viaje hago la ___.',opts:['maleta','nube','estación'],ans:'maleta',why:'la maleta = koffer'},
   {q:'He viajado en ___ desde Lima.',opts:['avión','paraguas','recuerdo'],ans:'avión',why:'transporte'},
   {q:'En Cusco ___ frío por la noche.',opts:['hace','llueve','está'],ans:'hace',why:'hace frío'},
   {q:'Cojo el ___ porque llueve.',opts:['paraguas','pasaporte','billete'],ans:'paraguas',why:'lluvia → paraguas'},
   {q:'El tren sale de la ___.',opts:['estación','playa','montaña'],ans:'estación',why:'la estación'},
   {q:'He sacado muchas ___ en el viaje.',opts:['fotos','nubes','maletas'],ans:'fotos',why:'sacar fotos'},
   {q:'En la selva ___ mucho.',opts:['llueve','nieva','hace sol'],ans:'llueve',why:'selva = lluvia'},
   {q:'Para volar necesito el ___.',opts:['pasaporte','recuerdo','mar'],ans:'pasaporte',why:'volar → pasaporte'},
   {q:'En invierno en los Andes ___.',opts:['nieva','hace calor','está seco'],ans:'nieva',why:'nieve = sneeuw'},
   {q:'Me he ___ el abrigo porque hace frío.',opts:['puesto','visto','dicho'],ans:'puesto',why:'ponerse → puesto'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het juiste woord.',per:6,pool:[
   {q:'Cuando el cielo está gris y no hay sol:',opts:['está nublado','hace calor','nieva'],ans:'está nublado',why:'nublado = bewolkt'},
   {q:'Transporte que vuela por el aire:',opts:['el avión','el barco','el tren'],ans:'el avión',why:'avión = vliegtuig'},
   {q:'Documento para viajar a otro país:',opts:['el pasaporte','el billete','el mapa'],ans:'el pasaporte',why:'paspoort'},
   {q:'Participio de «hacer»:',opts:['hecho','hacido','hago'],ans:'hecho',why:'hacer → hecho'},
   {q:'Agua congelada que cae del cielo:',opts:['la nieve','la lluvia','el sol'],ans:'la nieve',why:'nieve = sneeuw'},
   {q:'La ciudad inca de Perú, en la montaña:',opts:['Machu Picchu','Lima','Cartagena'],ans:'Machu Picchu',why:'Machu Picchu 🇵🇪'},
   {q:'Animal típico de los Andes:',opts:['la llama','el pollo','el gato'],ans:'la llama',why:'llama = lama'},
   {q:'Marcador que significa «nog niet»:',opts:['todavía no','ya','muchas veces'],ans:'todavía no',why:'todavía no'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['el avión','el tren','el barco','la maleta'],odd:3,why:'la maleta is geen transport'},
   {words:['hace sol','hace calor','hace frío','el hotel'],odd:3,why:'el hotel is geen weer'},
   {words:['hecho','visto','escrito','comer'],odd:3,why:'«comer» is een infinitief, geen participio'},
   {words:['ya','todavía no','nunca','avión'],odd:3,why:'«avión» is geen marcador'},
   {words:['la playa','la montaña','el mar','el billete'],odd:3,why:'el billete is geen plek/landschap'},
   {words:['llueve','nieva','hace viento','la foto'],odd:3,why:'la foto is geen weer'},
   {words:['viajado','comido','subido','hago'],odd:3,why:'«hago» is presente, geen participio'},
   {words:['hoy','esta semana','este año','la nube'],odd:3,why:'la nube is geen marcador van tijd'}]});
 // LECTURA
 buildOrder('lx_order',{title:'Ordena el viaje',desc:'Tik de items in de juiste volgorde.',rounds:[
   {sub:'el día de Nina',items:[{label:'He llegado a Cusco en avión.',key:1},{label:'He cogido el tren a Machu Picchu.',key:2},{label:'He subido y he sacado fotos.',key:3},{label:'Al final he vuelto al hotel.',key:4}]},
   {sub:'preparar el viaje',items:[{label:'He comprado el billete.',key:1},{label:'He hecho la maleta.',key:2},{label:'He llegado al aeropuerto.',key:3},{label:'He viajado a Perú.',key:4}]},
   {sub:'la postal',items:[{label:'He comprado una postal.',key:1},{label:'He escrito el mensaje.',key:2},{label:'He puesto el sello.',key:3},{label:'La he enviado.',key:4}]},
   {sub:'el mal tiempo',items:[{label:'Ha hecho sol por la mañana.',key:1},{label:'Luego se ha nublado.',key:2},{label:'Después ha empezado la tormenta.',key:3},{label:'Al final ha llovido mucho.',key:4}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in het diario de Nina en kies het juiste antwoord.',per:6,pool:[
   {q:'¿Cómo ha viajado Nina a Cusco?',opts:['en avión','en tren','en barco'],ans:'en avión',why:'«He viajado en avión desde Lima»'},
   {q:'¿Qué tiempo hace en Cusco (día 1)?',opts:['hace frío y está nublado','hace calor','llueve'],ans:'hace frío y está nublado',why:'«hace frío y está nublado»'},
   {q:'¿Qué ha cogido para ir a Machu Picchu?',opts:['el tren','el avión','el barco'],ans:'el tren',why:'«He cogido el tren muy pronto»'},
   {q:'¿Qué tiempo ha hecho en Machu Picchu?',opts:['ha hecho sol','ha nevado','ha llovido'],ans:'ha hecho sol',why:'«Ha hecho sol toda la mañana»'},
   {q:'¿Qué animales ha visto Nina?',opts:['las llamas','los perros','los gatos'],ans:'las llamas',why:'«He visto las llamas»'},
   {q:'¿Qué ha escrito Nina?',opts:['una postal','un libro','un email'],ans:'una postal',why:'«He escrito una postal»'},
   {q:'El día 1, ¿ya ha subido a la montaña?',opts:['no, todavía no','sí','no ha ido'],ans:'no, todavía no',why:'«Todavía no he subido»'},
   {q:'¿A cuántos metros está Cusco?',opts:['3400 metros','2430 metros','100 metros'],ans:'3400 metros',why:'«a 3400 metros»'}]});
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='U8_web_mijn_versie.html';a.click();};
})();
"""

# Getypte woordenschat-drills (fase ophalen + produceren) in het paneel zelf.
JS += hub_type_sets.vocab_type_js(vocab)
JS += hub_type_gram.js('C5', 8)
JS += hub_bloques.retos_js('retos_u8', 'C5', 8)
JS += (hub_bloques.escucha_js("esc_u8", escucha_data.C5_U8)
       + hub_bloques.lectura_js("lec_u8", lectura_data.C5_U8))
HTML = HTML.replace("__GRAMSLOTS__", hub_type_gram.slots('C5', 8))
HTML = HTML.replace("__NGAMES__", str(len(GAMES)))
HTML = HTML.replace("__BRONNEN__", extra_bronnen.html('C5', 8))
HTML = HTML.replace("__TYPESLOTS__", hub_type_sets.SLOTS_HTML)

# Het rollenspel: offline oefenpartner in het Hablar-paneel.
# De schrijfcoach bij de eindtaak, onderaan het Retos-paneel.
_co = gen_coach.componente("C5", 8)
if _co:
    _co_html, _co_css, _co_js = _co
    HTML = HTML.replace("__COACH__", _co_html)
    CSS += _co_css
    JS += _co_js
else:
    HTML = HTML.replace("__COACH__", "")

_rol = gen_rol.componente("C5", 8)
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
open(f"{ROOT}/03-build/web/U8_web.html","w").write(html)
print("U8_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
