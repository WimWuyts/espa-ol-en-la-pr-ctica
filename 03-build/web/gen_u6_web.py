#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de zelfstandige HTML-hub voor C5 · U6 «De tiendas».
# Eén standalone bestand: fonts base64, de U6-motor-spellen base64 ingebed (modal, offline),
# flashcards + naslag (U6-vocab), visuele/interactieve grammatica (lo/la/los/las · acabar de · este/ese/aquel · concordancia),
# klikbare kaart (mundo hispano, parada 6 = México/mercados) + TTS + inline recorder + Lectura + editbar. Huisstijl groen.
# NB: vocab_emoji.py NIET aangepast (parallel-conflict). U6-eigen emoji via lokale EXTRA-dict + norm.
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
sys.path.insert(0, GEN); import cast_gen as C; import vocab_icons as VI; import vocab_emoji as VE
vocab = json.load(open(f"{ROOT}/01-cursussen/05-a1/U6/u6_vocab.json", encoding="utf-8"))
mapsvg = open(f"{GEN}/mundo_map_real.svg").read()
moch = C.mochila("100%", "map")

# U6-eigen emoji (ropa/tienda/compra): lokale dict, gekoppeld op het genormaliseerde kernwoord.
def norm(es): return VE._norm(es)
EXTRA = {
  'camiseta':'👕','camisa':'👔','blusa':'👚','jersey':'🧥','sudadera':'🧥','chaqueta':'🧥','abrigo':'🧥',
  'pantalones':'👖','vaqueros':'👖','falda':'👗','vestido':'👗','traje':'🤵','bañador':'🩳',
  'zapatos':'👞','zapatillas':'👟','botas':'👢','sandalias':'👡','calcetines':'🧦','gorra':'🧢',
  'bufanda':'🧣','cinturón':'🎗️','gafas de sol':'🕶️','bolso':'👜','sombrero':'👒',
  'rojo':'🟥','negro':'⬛','blanco':'⬜','amarillo':'🟨','azul':'🟦','verde':'🟩',
  'gris':'🌫️','marrón':'🟫','morado':'🟪','rosa':'🌸','naranja':'🟧','celeste':'🩵',
  'liso':'⬜','de rayas':'📊','de cuadros':'🏁','de lunares':'🔴','estampado':'🌺','de algodón':'🧵','de lana':'🐑','de cuero':'🐄',
  'corto':'📏','largo':'📐','ancho':'↔️','estrecho':'📏',
  'tienda de ropa':'🏬','zapatería':'👟','panadería':'🥖','carnicería':'🥩','frutería':'🍎','farmacia':'💊',
  'supermercado':'🛒','mercado':'🏪','centro comercial':'🏬',
  'dependiente':'🧑‍💼','cliente':'🙋','probador':'🚪','escaparate':'🪟','caja':'🧾','etiqueta':'🏷️',
  'talla':'📏','rebajas':'🔖','descuento':'💯','bolsa':'🛍️','tarjeta':'💳',
  'cuánto cuesta':'💶','me lo llevo':'🛍️','puedo probármelo':'🚪','me queda bien':'👍','qué desea':'🛎️',
  'llevar':'👕','probarse':'🔄','comprar':'🛒','buscar':'🔎','regatear':'🤝','acabar de':'✅','en efectivo':'💵',
  'tianguis':'🧺','mercadillo':'🏮','moda sostenible':'♻️','ropa de segunda mano':'♻️','poncho':'🧣','guayabera':'👕',
}
def emoji_for(es, grp): return EXTRA.get(norm(es)) or VE.emoji_for(es, grp)
ICONS=[f'<div class="fcico">{emoji_for(v.get("es",""),v.get("grp",""))}</div>' for v in vocab]

def b64(p): return base64.b64encode(open(p, "rb").read()).decode()
def face(fam, path, w):
    return f"@font-face{{font-family:'{fam}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{path}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS = "".join([
 face("Bricolage Grotesque", "BricolageGrotesque-700.woff2", "700"),
 face("Bricolage Grotesque", "BricolageGrotesque-800.woff2", "800"),
 face("Inter", "Inter-400.woff2", "400"), face("Inter", "Inter-600.woff2", "600"),
 face("Caveat", "Caveat-700.woff2", "700"),
])

# ---- de U6-motor-spellen: gegroepeerd (receptief -> productief -> hablar) + base64 ingebed ----
MOTOR = [
 ['① Reconocer · woordenschat', [
   ['ropa-memoria', 'memoria de la ropa', 'memory'],
   ['tienda-producto-memoria', 'tienda ↔ producto', 'memory'],
   ['prenda-tienda', 'prenda ↔ tienda', 'match'],
   ['color-prenda', 'color + prenda (concordancia)', 'match']]],
 ['② Distinguir · léxico/gramática', [
   ['ropa-tipo', '¿arriba, abajo, calzado o complemento?', 'classify'],
   ['lo-la-los-las', '¿lo, la, los o las?', 'classify'],
   ['genero-adjetivo', 'masculino o femenino', 'classify'],
   ['este-ese-aquel', 'cerca · ahí · lejos', 'classify']]],
 ['③ Producir con apoyo', [
   ['pronombre-od-cloze', 'completa: lo/la/los/las', 'cloze'],
   ['acabar-de-cloze', 'completa: acabar de + infinitivo', 'cloze'],
   ['demostrativo-cloze', 'completa: este/ese/aquel', 'cloze'],
   ['concordancia-tetris', 'concordancia: puertas', 'platform'],
   ['orden-tienda', 'ordena el diálogo de la tienda', 'order'],
   ['pasos-compra', 'ordena los pasos de la compra', 'order'],
   ['senala-escaparate', 'señala en el escaparate', 'point']]],
 ['④ Analizar & comunicar', [
   ['de-compras', '¡vas de compras! (regateo)', 'sim']]],
 ['⑤ Hablar · grábate 🎙️', [
   ['repite-tienda', 'escucha y repite', 'speak'],
   ['shadowing-diego', 'shadowing con Diego', 'speak'],
   ['mensaje-regateo', 'mensaje de voz: regatea', 'speak'],
   ['describe-ropa', 'describe tu ropa', 'speak']]],
]
GAMEDIR = f"{ROOT}/spaans-motor/games"
slugs = [g[0] for grp in MOTOR for g in grp[1]]
GAMES = {s: b64(f"{GAMEDIR}/es-u6-{s}.html") for s in slugs if os.path.exists(f"{GAMEDIR}/es-u6-{s}.html")}

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
      <select id="fcgrp" onchange="renderFC()"><option value="">alle groepen</option><option value="ropa">la ropa</option><option value="calzado">calzado & complementos</option><option value="colores">colores</option><option value="material">formas & materiales</option><option value="tiendas">las tiendas</option><option value="tienda">en la tienda</option><option value="compra">verbos & expresiones</option><option value="mexico">moda & México</option></select>
      <span class="pill" id="fccount"></span>
      <button class="btn sec small" onclick="shuffleFC()">↻ shuffle</button>
    </div><div class="fcgrid" id="fcgrid"></div>"""

def naslag_html():
    return """<div class="controls"><input id="vsearch" placeholder="🔎 zoek in woordenschat…" oninput="renderTable()"><span class="pill" id="vcount"></span></div>
    <div style="max-height:60vh;overflow:auto"><table class="vt"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody id="vbody"></tbody></table></div>"""

HTML = """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Español en la práctica · U6 De tiendas</title>
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
    <div><h1>U6 · De tiendas</h1>
    <p>La página digital de la Unidad 6 (parada <b>México · los mercados</b>): flashcards, gramática visual e interactiva y <b>__NGAMES__ juegos</b> con muchas series. <span style="opacity:.85">Uitbreiding van het boek (PDF): elke QR brengt je hier om te oefenen met zelfcorrectie.</span></p></div>
  </div>
  <div class="subnav" id="subnav"></div>

  <section class="panel show" data-p="vocab">
    <h2 class="sec">Vocabulario · flashcards</h2>
    <p class="lead">Álle woorden van U6. Klik om te draaien; wissel ES↔NL; filter per groep; klik 🔊 om te horen. <span class="gloss">Voorkant = Spaans + voorbeeldzin, achterkant = vertaling.</span></p>
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
    <p class="lead">Eerst betekenis en patroon ontdekken, dan de regel. Beweeg over de woorden, klik, en probeer. <span class="gloss">Alles binnen het thema van U6: lo/la/los/las, acabar de + infinitivo, este/ese/aquel y la concordancia.</span></p>
    <h3 class="subh">🔁 Pronombres — lo / la / los / las</h3>
    <div class="card" id="colorsent"></div>
    <div class="game" id="g_pron"></div>
    <div class="card ex" id="gx_pronq"></div>
    <div class="card ex" id="gx_build"></div>
    <h3 class="subh">⏱️ Acabar de + infinitivo</h3>
    <div class="card" id="irconj"></div>
    <div class="card ex" id="gx_iraq"></div>
    <h3 class="subh">📍 Este / ese / aquel — cerca ↔ lejos</h3>
    <div class="game" id="g_cantidad"></div>
    <div class="card ex" id="gx_cantq"></div>
    <h3 class="subh">⚖️ Concordancia — color + prenda</h3>
    <div class="card ex" id="gx_conc"></div>
    <h3 class="subh">🎯 Repaso mixto — rellena con feedback</h3>
    <div class="card ex" id="gx_mix"></div>
  __GRAMSLOTS__
  </section>

  <section class="panel" data-p="lectura">
    <h2 class="sec">Lectura · ¡rebajas! + una reseña</h2>
    <p class="lead">Lees het <b>anuncio de rebajas</b> en de <b>reseña</b>, <b>luister</b> ze (🔊 TTS) en <b>controleer je begrip</b>. Daarna schrijf je je eigen review — die neem je op in het tabblad <b>Hablar</b>. <span class="gloss">Keten: lezen → schrijven → spreken.</span></p>
    <div id="lecturawrap"></div>
    <h3 class="subh">🔢 Ordena la compra</h3>
    <div class="card ex" id="lx_order"></div>
    <h3 class="subh">🔎 Comprensión · escanea y escoge</h3>
    <div class="card ex" id="lx_scan"></div>
    <h2 class="sec">Lectura completa · Cinco trucos para ir de rebajas</h2>
    <p class="lead">Een echt tipsartikel met de volledige leesroute: <b>voorspellen → globaal → scannen → juist/fout met bewijs → betekenis uit de context → zelf schrijven</b>. <span class="gloss">Dezelfde tekst staat in je cursus, met schrijfruimte.</span></p>
    <div class="card ex" id="lec_u6"></div>
  </section>

  <section class="panel" data-p="escuchar">
    <h2 class="sec">Escuchar · En el probador 🎧</h2>
    <p class="lead">Nina past kleren en Valen zegt eerlijk wat ze ervan vindt. Eén fragment, zes stappen: eerst <b>weten waar je bent</b>, dan <b>globaal</b> luisteren, dan de <b>details</b>, dan <b>juist/fout met bewijs</b>. Het <b>transcript</b> gaat pas open als je klaar bent — anders lees je mee in plaats van te luisteren. <span class="gloss">Zolang er nog geen opname is, leest de computerstem het fragment voor.</span></p>
    <div class="card ex" id="esc_u6"></div>
  </section>
  <section class="panel" data-p="juegos">
    <h2 class="sec">Ejercicios · __NGAMES__ juegos, jij kiest</h2>
    <p class="lead">Geordend van <b>herkennen → onderscheiden → produceren met steun → analyseren &amp; communiceren → hablar</b>. Elk spel geeft directe, verklarende feedback en de steun bouwt af. <span class="gloss">Klik een spel; het opent in een venster en werkt ook offline.</span></p>
    <div id="motorlink"></div>
  </section>

  <section class="panel" data-p="retos">
    <h2 class="sec">Retos · tres desafíos 🎯</h2>
    <p class="lead">Drie retos met <b>één harde regel</b>: je vraagt in Mexico naar een maat die daar <b>niet bestaat</b>, je maakt een radiospot van <b>exact twintig seconden</b>, en je beslist lo/la/los/las — waarbij het geslacht van het kledingstuk de knoop doorhakt. <span class="gloss">De zeven andere retos van deze unit staan in het boek en in de PowerPoint.</span></p>
    <div id="retos_u6"></div>
  </section>
  <section class="panel" data-p="hablar">
    __ROL__
    <h2 class="sec">Hablar · grábate 🎙️</h2>
    <p class="lead">Neem <b>jezelf</b> op: luister naar het model, spreek in, luister terug, en neem opnieuw op. <span class="gloss">Werkt in Chrome/Edge; sta de micro toe. Print blijft bruikbaar zonder opname.</span></p>
    <div class="card" id="rec_repite"></div>
    <div class="card" id="rec_pedido"></div>
    <div class="card" id="rec_plato"></div>
    <p class="lead" style="margin-top:8px">Meer spreek-/opnamespellen (shadowing con Diego, describe…) vind je ook onder <b>Juegos ⑤</b>.</p>
  </section>

  <section class="panel" data-p="cultura">
    <h2 class="sec">Cultura · La compra en México</h2>
    <p class="lead">Comprar es también cultura. Descubre las <b>rebajas</b>, el arte de <b>regatear</b>, los <b>tianguis</b> de México y la <b>moda sostenible</b>. <span class="gloss">Winkelen is ook cultuur: solden, afdingen, de tianguis en duurzame mode.</span></p>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7.5 4.27 9 5.15V3a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2.15l1.5-.88a1 1 0 0 1 1.4.4l3 5.19a1 1 0 0 1-.4 1.36L18 13.5V21a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1v-7.5l-2.5-1.28a1 1 0 0 1-.4-1.36l3-5.19a1 1 0 0 1 1.4-.4Z"/></svg>El tianguis 🧺 🇲🇽</h3>
      <p>El <b>tianguis</b> (del <b>náhuatl</b> <i>tiānquiztli</i>) es un mercado al aire libre e itinerante, desde tiempos <b>aztecas</b>. Se vende ropa, comida y artesanía; se paga <b>en efectivo</b> y se puede <b>regatear</b>. <span class="gloss">De tianguis is een openluchtmarkt met een náhuatl-naam, sinds de Azteken. Cash betalen en afdingen kan.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px;display:flex;align-items:center;gap:8px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.59 13.41 13.42 20.6a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82Z"/><circle cx="7" cy="7" r="1.2" fill="currentColor"/></svg>Rebajas y regateo 🏷️🤝</h3>
      <p>Dos veces al año hay <b>rebajas</b> (enero y julio en España): precios con <b>descuento</b> (−30 %, −50 %). En una tienda con <b>etiqueta</b> no se regatea; en el <b>mercado</b> o el tianguis, sí: «¿Me hace un descuento?». <span class="gloss">🔴 Regatear = afdingen — enkel op de markt, niet in de winkel met prijskaartje.</span></p></div>
    <div class="card"><h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Ropa típica y moda sostenible 👗♻️</h3>
      <p><b>ES:</b> Cada región tiene su ropa: el <b>poncho</b> andino, la <b>guayabera</b> caribeña, el <b>huipil</b> maya. Hoy crece la <b>moda sostenible</b> y la ropa de <b>segunda mano</b> frente a la <i>moda rápida</i>. <span class="gloss">Elke regio heeft eigen kledij; duurzame en tweedehandskledij groeit tegenover fast fashion.</span></p>
      <div class="platos">
        <div class="pl"><div class="em">🧣</div><div class="nm">el poncho</div><small>los Andes 🇵🇪🇧🇴</small></div>
        <div class="pl"><div class="em">👕</div><div class="nm">la guayabera</div><small>el Caribe 🇨🇺🇲🇽</small></div>
        <div class="pl"><div class="em">👚</div><div class="nm">el huipil</div><small>Mesoamérica 🇲🇽🇬🇹</small></div>
        <div class="pl"><div class="em">🧺</div><div class="nm">el tianguis</div><small>mercado azteca</small></div>
        <div class="pl"><div class="em">♻️</div><div class="nm">segunda mano</div><small>moda sostenible</small></div>
      </div>
      <p><span class="gloss">Refranes: «Lo barato sale caro» (goedkoop is duurkoop) · «El hábito no hace al monje» (kleren maken de man niet).</span></p></div>
    <h3 class="subh">📍 La Ruta · ¿dónde estamos?</h3>
    <p class="lead">Onze parada 6: <b>México · los mercados</b> 🇲🇽. <b>Klik op een groen land</b> op de kaart voor info. Verderop: Colombia → Perú.</p>
    <div class="card" id="mapwrap">__MAP__<div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een groen land (of een halte ★) om er meer over te lezen.</p></div></div>
  </section>

  <section class="panel" data-p="extra">
    __BRONNEN__
  </section>

  <div class="foot">Español en la práctica · C5 · Unidad 6 «De tiendas» — página digital. Uitbreiding op de PDF · huisstijl groen · print ↔ PowerPoint ↔ web.</div>
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

// ---- GRAMMAR-VIZ 1: kleurgecodeerde OD-zin ----
document.getElementById('colorsent').innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">lo / la / los / las — vervang de prenda</h3>'+
'<div class="csent">'+
'<span style="background:#fef3c7;color:#92400e">¿La camisa?<span class="tip">de prenda (v. ev.)</span></span> — Sí, '+
'<span style="background:#dcfce7;color:#166534">la<span class="tip">pronomen = la camisa (v. ev.)</span></span> '+
'<span style="background:#fed7aa;color:#9a3412">compro<span class="tip">vervoegd werkwoord — pronomen staat ervóór</span></span>.</div>'+
'<div class="legend"><span><i style="background:#fde68a"></i>de prenda</span><span><i style="background:#86efac"></i>lo/la/los/las</span><span><i style="background:#fdba74"></i>werkwoord</span></div>'+
'<p class="gloss" style="margin-top:8px">🔴 <b>lo</b> (m.ev.) · <b>la</b> (v.ev.) · <b>los</b> (m.mv.) · <b>las</b> (v.mv.). Vóór het vervoegde ww (<i>la compro</i>) of vast achter de infinitief (<i>comprarla</i>). · '+(TTS?'<button class="spk-btn" onclick="speak(\'¿La camisa? Sí, la compro.\')">🔊 hoor de zin</button>':'')+'</p>';

// ---- GRAMMAR-VIZ 2: acabar (presente) — klik om te onthullen ----
(function(){const el=document.getElementById('irconj');
 const R=[['yo','acabo'],['tú','acabas'],['él/ella','acaba'],['nosotros','acabamos'],['vosotros','acabáis'],['ellos','acaban']];
 el.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">El verbo «acabar» — klik om te onthullen</h3><p class="desc" style="color:var(--mut);font-size:13px">Denk eerst zelf de vorm; klik dan de kaart. Daarna: forma + <b>de</b> + infinitivo = «net gedaan».</p><div class="conjgrid" id="icg"></div>';
 const g=el.querySelector('#icg');
 R.forEach(([p,v])=>{const d=document.createElement('div');d.className='conjcell';d.innerHTML='<div class="p">'+p+'</div><div class="v">— ?</div>';
   d.onclick=()=>{d.classList.add('rev');d.querySelector('.v').textContent=v+' de…';if(TTS)speak(p+' '+v+' de comprar');};g.appendChild(d);});
})();

// ---- GRAMMAR-VIZ 3: ¿este, ese o aquel? (cerca/ahí/lejos) ----
function gameCantidad(){const el=document.getElementById('g_cantidad');
 const items=[['jersey (aquí)','este','m.ev. · cerca'],['falda (aquí)','esta','v.ev. · cerca'],['zapatos (aquí)','estos','m.mv. · cerca'],['botas (ahí)','esas','v.mv. · ahí'],['abrigo (ahí)','ese','m.ev. · ahí'],['camisa (allí)','aquella','v.ev. · lejos'],['pantalones (allí)','aquellos','m.mv. · lejos'],['gorra (aquí)','esta','v.ev. · cerca'],['vestido (ahí)','ese','m.ev. · ahí'],['sandalias (allí)','aquellas','v.mv. · lejos'],['cinturón (aquí)','este','m.ev. · cerca'],['gafas (ahí)','esas','v.mv. · ahí']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿este/esta, ese/esa o aquel/aquella?</h3><p class="desc">Kies de juiste vorm (cerca=este · ahí=ese · lejos=aquel), passend bij m/v · ev/mv.</p>'+scoreBar('sbC')+'<div id="cW" style="font-size:22px;font-family:var(--disp);text-align:center;margin:8px 0">___ <b></b></div><div class="chips" id="cC" style="justify-content:center"></div><div class="fb" id="cFb"></div>';
 const sb=el.querySelector('#sbC');const cont=el.querySelector('#cC');
 ['este','esta','estos','estas','ese','esa','esos','esas','aquel','aquella','aquellos','aquellas'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.style.fontSize='13px';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#cW b').textContent=el.cur[0];el.querySelector('#cFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#cFb'),ok,(ok?'¡Sí! ':'Nee → ')+el.cur[1]+' '+el.cur[0]+' ('+el.cur[2]+').');setTimeout(next,1000);}
 next();}
// ---- GRAMMAR-VIZ 4: ¿lo, la, los o las? ----
function gamePron(){const el=document.getElementById('g_pron');
 const items=[['la falda','la','v. ev.'],['el jersey','lo','m. ev.'],['los zapatos','los','m. mv.'],['las botas','las','v. mv.'],['la camisa','la','v. ev.'],['el abrigo','lo','m. ev.'],['los vaqueros','los','m. mv.'],['las sandalias','las','v. mv.'],['el cinturón','lo','m. ev.'],['la gorra','la','v. ev.'],['los calcetines','los','m. mv.'],['las gafas','las','v. mv.']];
 let pool=items.slice(),pt=0,st=0;
 el.innerHTML='<h3>¿lo, la, los o las?</h3><p class="desc">Welk pronomen vervangt de prenda? (la falda → la compro)</p>'+scoreBar('sbP')+'<div id="pQ" style="font-size:20px;font-family:var(--disp);text-align:center;margin:10px 0"></div><div class="chips" id="pC" style="justify-content:center"></div><div class="fb" id="pFb"></div>';
 const sb=el.querySelector('#sbP');const cont=el.querySelector('#pC');
 ['lo','la','los','las'].forEach(c=>{const b=document.createElement('div');b.className='chip';b.textContent=c;b.onclick=()=>guess(c);cont.appendChild(b);});
 function next(){if(!pool.length)pool=items.slice();const i=Math.floor(Math.random()*pool.length);el.cur=pool.splice(i,1)[0];el.querySelector('#pQ').textContent='¿'+el.cur[0]+'? → ___ compro';el.querySelector('#pFb').className='fb';}
 function guess(c){const ok=c===el.cur[1];if(ok){pt++;st++}else st=0;setScore(sb,pt,st);feedback(el.querySelector('#pFb'),ok,(ok?'¡Sí! ':'Nee → ')+el.cur[0]+' → '+el.cur[1]+' compro ('+el.cur[2]+').');setTimeout(next,1000);}
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
   const INFO={"MEX": {"fl": "🇲🇽", "n": "México", "cap": "Ciudad de México", "pob": "~130 mln", "mon": "peso mexicano", "gen": "mexicano/a", "idi": "español (+ náhuatl, maya y 66 lenguas más)", "cool": "los aztecas fundaron Tenochtitlan (hoy CDMX) en 1325 · Frida Kahlo y Diego Rivera, pintores · pirámides de Teotihuacán y Chichén Itzá (mayas)", "tema": "🛍️ De compras: los mercados y «tianguis»; se regatea", "star": 1, "nl": "★ ¡Estás aquí! Parada U5–U6 · CDMX · los mercados (Diego)"}, "ESP": {"fl": "🇪🇸", "n": "España", "cap": "Madrid", "pob": "~48 mln", "mon": "euro", "gen": "español/a", "idi": "español (+ catalán, gallego, euskera)", "cool": "la Sagrada Familia de Gaudí, aún en obras · la Alhambra de Granada, arquitectura árabe · Picasso, Velázquez y el Prado", "tema": "🛍️ De compras: los mercados y las rebajas de enero y julio", "star": 1, "nl": "Parada anterior (U0–U4) · Madrid · Sevilla · Barcelona · València"}, "COL": {"fl": "🇨🇴", "n": "Colombia", "cap": "Bogotá", "pob": "~52 mln", "mon": "peso colombiano", "gen": "colombiano/a", "idi": "español (+ 65 lenguas indígenas)", "cool": "Gabriel García Márquez, Nobel del «realismo mágico» · Shakira y Karol G · Cartagena, ciudad amurallada colonial", "tema": "🛍️ De compras: las plazas de mercado y las flores", "star": 0, "nl": ""}, "PER": {"fl": "🇵🇪", "n": "Perú", "cap": "Lima", "pob": "~34 mln", "mon": "sol", "gen": "peruano/a", "idi": "español, quechua y aymara", "cool": "Machu Picchu, ciudad inca en los Andes · el imperio inca tuvo su capital en Cusco · las misteriosas líneas de Nazca", "tema": "🛍️ De compras: los mercados andinos y los textiles", "star": 0, "nl": ""}, "ARG": {"fl": "🇦🇷", "n": "Argentina", "cap": "Buenos Aires", "pob": "~46 mln", "mon": "peso argentino", "gen": "argentino/a", "idi": "español (voseo: «vos tenés»)", "cool": "Lionel Messi y Diego Maradona (fútbol) · el tango nació en Buenos Aires · la Patagonia y el glaciar Perito Moreno", "tema": "🛍️ De compras: las ferias y los productos de cuero", "star": 0, "nl": ""}, "VEN": {"fl": "🇻🇪", "n": "Venezuela", "cap": "Caracas", "pob": "~28 mln", "mon": "bolívar", "gen": "venezolano/a", "idi": "español (+ lenguas indígenas)", "cool": "el Salto Ángel, la cascada más alta del mundo (979 m) · Simón Bolívar, «el Libertador» · tierra de muchas Miss Universo", "tema": "🛍️ De compras: los mercados populares y las «buhonerías»", "star": 0, "nl": ""}, "CHL": {"fl": "🇨🇱", "n": "Chile", "cap": "Santiago", "pob": "~20 mln", "mon": "peso chileno", "gen": "chileno/a", "idi": "español (+ mapudungun)", "cool": "el desierto de Atacama, el más seco del mundo · Pablo Neruda y Gabriela Mistral, poetas Nobel · la isla de Pascua y sus moáis", "tema": "🛍️ De compras: la «feria libre» de frutas y verduras", "star": 0, "nl": ""}, "ECU": {"fl": "🇪🇨", "n": "Ecuador", "cap": "Quito", "pob": "~18 mln", "mon": "dólar estadounidense", "gen": "ecuatoriano/a", "idi": "español y quechua (kichwa)", "cool": "las islas Galápagos, donde estudió Darwin · «la mitad del mundo»: la línea del ecuador · Quito, primer Patrimonio de la Humanidad (1978)", "tema": "🛍️ De compras: el mercado de Otavalo, textiles indígenas", "star": 0, "nl": ""}, "GTM": {"fl": "🇬🇹", "n": "Guatemala", "cap": "Ciudad de Guatemala", "pob": "~18 mln", "mon": "quetzal", "gen": "guatemalteco/a", "idi": "español (+ 20 lenguas mayas)", "cool": "Tikal, gran ciudad maya en la selva · Rigoberta Menchú, Nobel de la Paz · el lago de Atitlán entre volcanes", "tema": "🛍️ De compras: el mercado de Chichicastenango, muy colorido", "star": 0, "nl": ""}, "CUB": {"fl": "🇨🇺", "n": "Cuba", "cap": "La Habana", "pob": "~11 mln", "mon": "peso cubano", "gen": "cubano/a", "idi": "español", "cool": "La Habana Vieja y sus coches clásicos · cuna del son, la salsa y la rumba · José Martí, héroe nacional", "tema": "🛍️ De compras: el mercado agrícola y los puros", "star": 0, "nl": ""}, "BOL": {"fl": "🇧🇴", "n": "Bolivia", "cap": "Sucre / La Paz", "pob": "~12 mln", "mon": "boliviano", "gen": "boliviano/a", "idi": "español, quechua, aymara, guaraní (37 oficiales)", "cool": "el Salar de Uyuni, el mayor salar del mundo · el lago Titicaca, el lago navegable más alto · Tiwanaku, cultura anterior a los incas", "tema": "🛍️ De compras: el «Mercado de las Brujas» en La Paz", "star": 0, "nl": ""}, "DOM": {"fl": "🇩🇴", "n": "República Dominicana", "cap": "Santo Domingo", "pob": "~11 mln", "mon": "peso dominicano", "gen": "dominicano/a", "idi": "español", "cool": "la primera catedral y universidad de América · cuna del merengue y la bachata · Óscar de la Renta, diseñador", "tema": "🛍️ De compras: los «colmados» de barrio", "star": 0, "nl": ""}, "HND": {"fl": "🇭🇳", "n": "Honduras", "cap": "Tegucigalpa", "pob": "~10 mln", "mon": "lempira", "gen": "hondureño/a", "idi": "español (+ garífuna, miskito)", "cool": "Copán, ciudad maya de estelas famosas · las islas de la Bahía, paraíso del buceo · «Honduras» significa «profundidades»", "tema": "🛍️ De compras: los mercados de artesanía", "star": 0, "nl": ""}, "PRY": {"fl": "🇵🇾", "n": "Paraguay", "cap": "Asunción", "pob": "~7 mln", "mon": "guaraní", "gen": "paraguayo/a", "idi": "español y guaraní (bilingüe)", "cool": "país oficialmente bilingüe (español + guaraní) · la represa de Itaipú, una de las mayores del mundo · las misiones jesuíticas, Patrimonio de la Humanidad", "tema": "🛍️ De compras: el ñandutí, encaje típico", "star": 0, "nl": ""}, "NIC": {"fl": "🇳🇮", "n": "Nicaragua", "cap": "Managua", "pob": "~7 mln", "mon": "córdoba", "gen": "nicaragüense", "idi": "español (+ miskito en la costa)", "cool": "«tierra de lagos y volcanes» · Rubén Darío, padre del modernismo · la isla de Ometepe, con dos volcanes", "tema": "🛍️ De compras: las hamacas de Masaya", "star": 0, "nl": ""}, "SLV": {"fl": "🇸🇻", "n": "El Salvador", "cap": "San Salvador", "pob": "~6 mln", "mon": "dólar estadounidense", "gen": "salvadoreño/a", "idi": "español (+ náhuat)", "cool": "«el pulgarcito de América»: el más pequeño · las pupusas, plato nacional · playas famosas para el surf en el Pacífico", "tema": "🛍️ De compras: la artesanía de La Palma", "star": 0, "nl": ""}, "CRI": {"fl": "🇨🇷", "n": "Costa Rica", "cap": "San José", "pob": "~5 mln", "mon": "colón", "gen": "costarricense", "idi": "español", "cool": "sin ejército desde 1948 · «Pura Vida» y una enorme biodiversidad · líder mundial en energía renovable", "tema": "🛍️ De compras: las carretas pintadas a mano", "star": 0, "nl": ""}, "PAN": {"fl": "🇵🇦", "n": "Panamá", "cap": "Ciudad de Panamá", "pob": "~4 mln", "mon": "balboa / dólar", "gen": "panameño/a", "idi": "español", "cool": "el Canal de Panamá une dos océanos · el sombrero «panamá» es en realidad ecuatoriano · el Darién, de gran biodiversidad", "tema": "🛍️ De compras: las «molas», textiles del pueblo guna", "star": 0, "nl": ""}, "URY": {"fl": "🇺🇾", "n": "Uruguay", "cap": "Montevideo", "pob": "~3 mln", "mon": "peso uruguayo", "gen": "uruguayo/a", "idi": "español", "cool": "José «Pepe» Mujica, expresidente humilde · el mate y las playas de Punta del Este · ganó la primera Copa del Mundo (1930)", "tema": "🛍️ De compras: la feria de Tristán Narvaja", "star": 0, "nl": ""}, "PRI": {"fl": "🇵🇷", "n": "Puerto Rico", "cap": "San Juan", "pob": "~3 mln", "mon": "dólar estadounidense", "gen": "puertorriqueño/a", "idi": "español e inglés", "cool": "Bad Bunny y el reguetón · el Viejo San Juan, colonial y colorido · El Yunque, bosque tropical lluvioso", "tema": "🛍️ De compras: la artesanía y los «vejigantes»", "star": 0, "nl": ""}, "GNQ": {"fl": "🇬🇶", "n": "Guinea Ecuatorial", "cap": "Malabo", "pob": "~1,7 mln", "mon": "franco CFA", "gen": "ecuatoguineano/a", "idi": "español, francés y portugués", "cool": "el único país hispanohablante de África · antigua colonia española (hasta 1968) · la isla de Bioko y la selva ecuatorial", "tema": "🛍️ De compras: los mercados de pescado y yuca", "star": 0, "nl": ""}, "USA": {"fl": "🇺🇸", "n": "Estados Unidos", "cap": "Washington D.C.", "pob": "~60 mln hispanos", "mon": "dólar estadounidense", "gen": "estadounidense", "idi": "inglés; el español es la 2ª lengua", "cool": "~60 mln de hispanos: la 2ª lengua más hablada · Miami, Los Ángeles y Nueva York, muy hispanas · Sonia Sotomayor, jueza del Tribunal Supremo", "tema": "🛍️ De compras: los supermercados y las tiendas latinas", "star": 0, "nl": ""}};
 const wrap=document.getElementById('mapwrap');const svg=wrap.querySelector('svg');const box=document.getElementById('mapinfo');
 if(!svg)return;
 svg.querySelectorAll('path.spa, path.usa').forEach(p=>{p.style.cursor='pointer';
   p.addEventListener('mouseenter',()=>{p.style.opacity='.75'});p.addEventListener('mouseleave',()=>{p.style.opacity=''});
   p.addEventListener('click',()=>{const c=p.getAttribute('data-c');const d=INFO[c];if(!d)return;
     box.innerHTML='<h3>'+d.fl+' '+d.n+' <span style="font-size:13px;color:var(--mut);font-weight:400">('+c+')</span>'+(d.star?' ★':'')+'</h3>'+'<div class="mrow"><b>🏛️ Capital:</b> '+d.cap+'</div>'+'<div class="mrow"><b>👥 Población:</b> '+d.pob+'</div>'+'<div class="mrow"><b>💰 Moneda:</b> '+d.mon+'</div>'+'<div class="mrow"><b>🗣️ Gentilicio:</b> '+d.gen+'</div>'+'<div class="mrow"><b>🌐 Idioma:</b> '+d.idi+'</div>'+(d.tema?'<div style="margin-top:8px;padding:8px 11px;background:rgba(255,255,255,.7);border-left:4px solid var(--gd);border-radius:7px;font-weight:600;color:var(--gd)">'+d.tema+'</div>':'')+(d.cool?'<div style="margin-top:8px;font-size:13px;line-height:1.5"><b>💡 ¿Sabías que…?</b> '+d.cool+'</div>':'')+(d.nl?'<div class="gloss" style="margin-top:6px">'+d.nl+'</div>':'');
     box.scrollIntoView({behavior:'smooth',block:'nearest'});});
 });
})();

// ---------- LECTURA: anuncio de rebajas + reseña + TTS + begrip ----------
function renderLectura(){const el=document.getElementById('lecturawrap');if(!el)return;
 const M=[{n:'📣 Anuncio · «Moda Diego» 🇲🇽',raw:'¡Grandes rebajas! Hasta cincuenta por ciento de descuento. Camisetas de algodón: de diez a cinco euros. Vaqueros azules: de cuarenta a veinticinco euros. Zapatillas blancas: de sesenta a treinta y nueve euros. Vestidos de lunares: de treinta y cinco a veinte euros. Se paga con tarjeta o en efectivo, y se puede regatear.',
    html:'<div class="sec2">¡GRANDES REBAJAS! hasta −50 %</div><div class="mi"><span>Camisetas de algodón</span><span class="pr">10 € → 5 €</span></div><div class="mi"><span>Vaqueros azules</span><span class="pr">40 € → 25 €</span></div><div class="mi"><span>Zapatillas blancas</span><span class="pr">60 € → 39 €</span></div><div class="mi"><span>Vestidos de lunares</span><span class="pr">35 € → 20 €</span></div><div class="sec2">Pago: tarjeta o efectivo · ¡se regatea!</div>'},
   {n:'⭐ Reseña · @valen_style 🇨🇴 · ★★★★☆',raw:'Acabo de comprar unos vaqueros azules en las rebajas de Moda Diego. Estaban a veinticinco euros, antes cuarenta. Me los probé en el probador y me quedan muy bien. El dependiente es simpático y pagué con tarjeta. La camiseta lisa no la compré porque no la tenían en mi talla. ¡Vuelvo seguro!',
    html:'<div class="perfil" style="border:0;padding:0"><div class="txt">«Acabo de comprar unos <span class="ev">vaqueros azules</span> en las <span class="ev">rebajas</span>. Estaban a <span class="ev">25 €</span> (antes 40). Me <span class="ev">los</span> probé en el probador y me quedan muy bien. El <span class="ev">dependiente</span> es simpático y pagué <span class="ev">con tarjeta</span>. La camiseta lisa no <span class="ev">la</span> compré porque no la tenían en mi talla. ¡Vuelvo seguro!»</div></div>'}];
 el.innerHTML='<div class="perfiles">'+M.map((m,i)=>'<div class="menucard"><h4>'+m.n+' '+(TTS?'<button class="spk-btn" style="margin-left:auto;padding:4px 10px" onclick="speak(document.getElementById(\'lm'+i+'\').dataset.raw)">🔊 escuchar</button>':'')+'</h4><div id="lm'+i+'" data-raw="'+m.raw.replace(/"/g,'&quot;')+'">'+m.html+'</div></div>').join('')+'</div>';
 const items=[['Valen compró unos vaqueros.',true,'«Acabo de comprar unos vaqueros azules»'],['Los vaqueros costaban 40 € antes.',true,'«25 €, antes 40»'],['Valen compró la camiseta lisa.',false,'«no la compré… no la tenían en mi talla»'],['Pagó con tarjeta.',true,'«pagué con tarjeta»'],['Las camisetas de algodón cuestan 5 € en rebajas.',true,'«de 10 a 5 euros»'],['En Moda Diego no se puede regatear.',false,'«se puede regatear»'],['Los vestidos de lunares cuestan 20 € ahora.',true,'«de 35 a 20 euros»'],['Valen se probó los vaqueros en el probador.',true,'«me los probé en el probador»'],['Las zapatillas blancas cuestan 60 € en rebajas.',false,'ahora 39 € (antes 60)'],['A Valen le quedan bien los vaqueros.',true,'«me quedan muy bien»']];
 const box=document.createElement('div');box.className='card vftask';box.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 8px">¿Verdadero o falso? — comprueba tu comprensión (con evidencia)</h3>';
 items.forEach(([q,ans,pr])=>{const r=document.createElement('div');r.className='vfrow';
   r.innerHTML='<span>'+q+'</span><span class="btns"><button class="vfb">V</button><button class="vfb">F</button><span class="res"></span></span>';
   const [bv,bf]=r.querySelectorAll('.vfb');const res=r.querySelector('.res');
   function pick(val){bv.classList.toggle('on',val);bf.classList.toggle('on',!val);const ok=val===ans;res.innerHTML=(ok?'✅ ':'❌ ')+'<span class="gloss">'+pr+'</span>';res.style.color=ok?'var(--gd)':'var(--red)';}
   bv.onclick=()=>pick(true);bf.onclick=()=>pick(false);box.appendChild(r);});
 const resp=document.createElement('div');resp.className='card';resp.innerHTML='<h3 style="font-family:var(--disp);color:var(--gd);margin:0 0 6px">Escribe tu reseña</h3><p class="gloss" style="margin:0 0 8px">Schrijf een korte review (3-4 zinnen) over een prenda die je «net gekocht hebt»: gebruik <b>acabar de</b> + een <b>pronomen</b> (lo/la/los/las). Neem het op onder <b>Hablar 🎙️</b> («describe tu ropa»).</p><textarea class="txin" style="width:100%;height:80px;font-family:var(--body)" placeholder="Acabo de comprar… La/Lo/Los/Las… porque…"></textarea>';
 el.appendChild(box);el.appendChild(resp);}

// ---------- INLINE RECORDER (MediaRecorder) ----------
""" + hub_drills.RECORDER_JS + r"""
function buildRecorders(){
 makeRecorder('rec_repite',{title:'Escucha y repite: en la tienda',desc:'Luister → zeg na → neem op → luister terug → opnieuw.',items:[
   {text:'¿Cuánto cuesta esta camiseta?',cue:'preguntar el precio',tip:'Duidelijk uitgesproken? Probeer nog eens.'},{text:'¿Puedo probármelo?',cue:'probarse'},{text:'¿La tienen en talla M?',cue:'la talla'},{text:'Me queda bien. Me lo llevo.',cue:'comprar'},{text:'Acabo de comprar unos vaqueros.',cue:'acabar de'},{text:'¿Me hace un descuento?',cue:'regatear'}]});
 makeRecorder('rec_pedido',{title:'Mensaje de voz: regatea en el tianguis',desc:'Neem één bericht op. Doel: afdingen op een prijs. Gebruik: ¿cuánto cuesta? · es caro · ¿me hace un descuento? · me lo llevo.',items:[
   {text:'Regatea el precio de una prenda en el tianguis (30 s): pregunta el precio, di que es caro y pide un descuento.',cue:'el regateo',tip:'Prijs vragen + «es caro» + descuento vragen? Neem opnieuw op.'}]});
 makeRecorder('rec_plato',{title:'Describe tu ropa favorita',desc:'Beschrijf je lievelingsoutfit: ¿qué prenda es? ¿de qué color? ¿por qué te gusta?',items:[
   {text:'Mi prenda favorita es ___ . Es ___ (color) y de ___ . Me encanta porque ___ .',cue:'tu versión',tip:'Heb je prenda + kleur + patroon + reden gezegd? Herneem.'}]});
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
 buildChoice('gx_pronq',{title:'Mini-quiz: lo / la / los / las',desc:'Welk pronomen vervangt de prenda? (la falda → la compro)',per:6,pool:[
   {q:'¿La falda? — Sí, ___ compro.',opts:['la','lo','las'],ans:'la',why:'la falda (v ev)'},
   {q:'¿El jersey? — ___ quiero.',opts:['Lo','La','Los'],ans:'Lo',why:'el jersey (m ev)'},
   {q:'¿Los zapatos? — Sí, ___ llevo.',opts:['los','las','lo'],ans:'los',why:'los zapatos (m pl)'},
   {q:'¿Las botas? — ___ me pruebo.',opts:['Las','Los','La'],ans:'Las',why:'las botas (v pl)'},
   {q:'¿El abrigo? — Sí, ___ compro.',opts:['lo','la','los'],ans:'lo',why:'el abrigo (m ev)'},
   {q:'¿La camisa? — Ahora ___ busco.',opts:['la','lo','las'],ans:'la',why:'la camisa (v ev)'},
   {q:'¿Los vaqueros? — ___ llevo hoy.',opts:['Los','Las','Lo'],ans:'Los',why:'los vaqueros (m pl)'},
   {q:'¿Las gafas? — ___ veo en el escaparate.',opts:['Las','Los','La'],ans:'Las',why:'las gafas (v pl)'},
   {q:'¿El cinturón? — ___ compro también.',opts:['Lo','La','Los'],ans:'Lo',why:'el cinturón (m ev)'},
   {q:'¿La gorra? — ___ quiero roja.',opts:['La','Lo','Las'],ans:'La',why:'la gorra (v ev)'},
   {q:'¿Los calcetines? — ___ pago en la caja.',opts:['Los','Las','Lo'],ans:'Los',why:'los calcetines (m pl)'},
   {q:'¿Las sandalias? — ___ me llevo.',opts:['Las','Los','La'],ans:'Las',why:'las sandalias (v pl)'}]});
 buildOrder('gx_build',{title:'Construye: acabar de + infinitivo',desc:'Tik de blokjes in de juiste volgorde (onderwerp → acabar → de → infinitivo → voorwerp).',rounds:[
   {sub:'yo · comprar',items:[{label:'Yo',key:1},{label:'acabo',key:2},{label:'de',key:3},{label:'comprar',key:4},{label:'una gorra',key:5}]},
   {sub:'tú · probarse',items:[{label:'¿Tú',key:1},{label:'acabas',key:2},{label:'de',key:3},{label:'probarte',key:4},{label:'el vestido?',key:5}]},
   {sub:'nosotros · pagar',items:[{label:'Nosotros',key:1},{label:'acabamos',key:2},{label:'de',key:3},{label:'pagar',key:4},{label:'en la caja',key:5}]},
   {sub:'Diego · llegar',items:[{label:'Diego',key:1},{label:'acaba',key:2},{label:'de',key:3},{label:'llegar',key:4},{label:'al mercado',key:5}]},
   {sub:'ellos · ver',items:[{label:'Ellos',key:1},{label:'acaban',key:2},{label:'de',key:3},{label:'ver',key:4},{label:'el escaparate',key:5}]},
   {sub:'OD · plaats vóór het ww',items:[{label:'¿La falda?',key:1},{label:'Sí,',key:2},{label:'la',key:3},{label:'compro',key:4}]},
   {sub:'OD · achter infinitief',items:[{label:'Quiero',key:1},{label:'comprar',key:2},{label:'los',key:3},{label:'(comprarlos)',key:4}]}]});
 buildChoice('gx_iraq',{title:'Mini-quiz: acabar de + infinitivo',desc:'Kies de juiste vorm van «acabar de». Directe feedback.',per:6,pool:[
   {q:'(Yo) ___ comprar una gorra.',opts:['acabo de','acabas de','acaba de'],ans:'acabo de',why:'yo → acabo de'},
   {q:'¿(Tú) ___ probarte el vestido?',opts:['acabas de','acabo de','acaban de'],ans:'acabas de',why:'tú → acabas de'},
   {q:'(Nosotros) ___ pagar en la caja.',opts:['acabamos de','acaban de','acabáis de'],ans:'acabamos de',why:'nosotros → acabamos de'},
   {q:'Diego ___ llegar al mercado.',opts:['acaba de','acaban de','acabas de'],ans:'acaba de',why:'él → acaba de'},
   {q:'(Ellos) ___ ver el escaparate.',opts:['acaban de','acaba de','acabamos de'],ans:'acaban de',why:'ellos → acaban de'},
   {q:'¿(Vosotros) ___ entrar en la tienda?',opts:['acabáis de','acaban de','acabamos de'],ans:'acabáis de',why:'vosotros → acabáis de'},
   {q:'Lucía ___ encontrar unas botas.',opts:['acaba de','acaban de','acabas de'],ans:'acaba de',why:'ella → acaba de'},
   {q:'(Yo) ___ elegir la talla M.',opts:['acabo de','acaba de','acabas de'],ans:'acabo de',why:'yo → acabo de'},
   {q:'Valen y Nina ___ salir de la tienda.',opts:['acaban de','acabamos de','acabáis de'],ans:'acaban de',why:'ellas → acaban de'},
   {q:'¿Qué ___ comprar (tú)?',opts:['acabas de','acaba de','acabo de'],ans:'acabas de',why:'tú → acabas de'},
   {q:'Acabo ___ comprar una camisa.',opts:['de','a','que'],ans:'de',why:'acabar DE + infinitivo'},
   {q:'(Nosotros) ___ regatear el precio.',opts:['acabamos de','acaban de','acabo de'],ans:'acabamos de',why:'nosotros → acabamos de'}]});
 buildChoice('gx_cantq',{title:'Mini-quiz: este / ese / aquel',desc:'este (cerca) · ese (ahí) · aquel (lejos). Kies wat past.',per:6,pool:[
   {q:'Me gusta ___ camiseta (aquí, en mi mano).',opts:['esta','esa','aquella'],ans:'esta',why:'cerca (v) → esta'},
   {q:'¿Cuánto cuesta ___ gorra (ahí, a tu lado)?',opts:['esa','esta','aquella'],ans:'esa',why:'ahí (v) → esa'},
   {q:'___ abrigo (allí, en el escaparate) es caro.',opts:['Aquel','Este','Ese'],ans:'Aquel',why:'lejos (m) → aquel'},
   {q:'___ zapatos (aquí) son cómodos.',opts:['estos','esos','aquellos'],ans:'estos',why:'cerca (m pl) → estos'},
   {q:'Prefiero ___ vestido (ahí).',opts:['ese','este','aquel'],ans:'ese',why:'ahí (m) → ese'},
   {q:'___ botas (allí) son de cuero.',opts:['Aquellas','Estas','Esas'],ans:'Aquellas',why:'lejos (v pl) → aquellas'},
   {q:'¿Te gusta ___ jersey (aquí)?',opts:['este','ese','aquel'],ans:'este',why:'cerca (m) → este'},
   {q:'___ falda (ahí) es de cuadros.',opts:['Esa','Esta','Aquella'],ans:'Esa',why:'ahí (v) → esa'},
   {q:'Mira ___ pantalones (allí).',opts:['aquellos','estos','esos'],ans:'aquellos',why:'lejos (m pl) → aquellos'},
   {q:'Quiero ___ sandalias (aquí).',opts:['estas','esas','aquellas'],ans:'estas',why:'cerca (v pl) → estas'},
   {q:'¿Cuánto es ___ cinturón (ahí)?',opts:['ese','este','aquel'],ans:'ese',why:'ahí (m) → ese'},
   {q:'___ camisa (allí) es blanca.',opts:['Aquella','Esta','Esa'],ans:'Aquella',why:'lejos (v) → aquella'}]});
 buildMatch('gx_conc',{title:'Concordancia: prenda ↔ color',desc:'Koppel de prenda aan de juiste vorm van de kleur (m/v · ev/mv).',per:6,pool:[
   {a:'una camiseta',b:'roja'},{a:'un vestido',b:'rojo'},{a:'unos zapatos',b:'rojos'},{a:'unas botas',b:'rojas'},
   {a:'una falda azul',b:'azul'},{a:'unos vaqueros',b:'azules'},{a:'un jersey',b:'negro'},{a:'unas sandalias',b:'negras'},
   {a:'una gorra',b:'blanca'},{a:'unos calcetines',b:'verdes'},{a:'un abrigo',b:'gris'},{a:'unas gafas',b:'marrones'}]});
 buildChoice('gx_mix',{title:'Repaso mixto: rellena',desc:'Alles door elkaar: lo/la/los/las · acabar de · este/ese/aquel · concordancia.',per:8,pool:[
   {q:'¿La falda? — Sí, ___ compro.',opts:['la','lo','las'],ans:'la',why:'la falda (v ev)'},
   {q:'(Yo) ___ comprar una gorra.',opts:['acabo de','acaba de','acabas de'],ans:'acabo de',why:'yo → acabo de'},
   {q:'Me gusta ___ camiseta (aquí).',opts:['esta','esa','aquella'],ans:'esta',why:'cerca (v) → esta'},
   {q:'Una camiseta ___ (rood).',opts:['roja','rojo','rojos'],ans:'roja',why:'camiseta (v) → roja'},
   {q:'¿Los zapatos? — ___ llevo.',opts:['Los','Las','Lo'],ans:'Los',why:'los zapatos (m pl)'},
   {q:'Diego ___ llegar al mercado.',opts:['acaba de','acaban de','acabas de'],ans:'acaba de',why:'él → acaba de'},
   {q:'___ abrigo (allí) es caro.',opts:['Aquel','Este','Esa'],ans:'Aquel',why:'lejos (m) → aquel'},
   {q:'Unos pantalones ___ (blauw).',opts:['azules','azul','azulas'],ans:'azules',why:'m pl → azules (geen -a)'},
   {q:'¿La camisa? — ___ quiero.',opts:['La','Lo','Las'],ans:'La',why:'la camisa (v ev)'},
   {q:'(Nosotros) ___ pagar en la caja.',opts:['acabamos de','acaban de','acabo de'],ans:'acabamos de',why:'nosotros → acabamos de'},
   {q:'¿Cuánto cuesta ___ gorra (ahí)?',opts:['esa','esta','aquella'],ans:'esa',why:'ahí (v) → esa'},
   {q:'Unas botas ___ (bruin).',opts:['marrones','marrón','marronas'],ans:'marrones',why:'v pl → marrones'}]});
 // VOCABULARIO
 buildMatch('vx_match',{title:'Empareja: palabra ↔ emoji',desc:'Koppel het Spaanse woord aan het juiste beeld.',per:6,pool:[
   {a:'la camiseta',b:'👕'},{a:'los pantalones',b:'👖'},{a:'el vestido',b:'👗'},{a:'los zapatos',b:'👞'},
   {a:'las zapatillas',b:'👟'},{a:'la gorra',b:'🧢'},{a:'el bolso',b:'👜'},{a:'las gafas de sol',b:'🕶️'},
   {a:'las botas',b:'👢'},{a:'los calcetines',b:'🧦'},{a:'la bufanda',b:'🧣'},{a:'el sombrero',b:'👒'}]});
 buildChoice('vx_gap',{title:'Completa la frase',desc:'Kies het woord dat in de zin past.',per:6,pool:[
   {q:'Me pruebo la ropa en el ___.',opts:['probador','escaparate','caja'],ans:'probador',why:'probarse → el probador'},
   {q:'En enero hay ___ con descuento.',opts:['rebajas','tallas','bolsas'],ans:'rebajas',why:'rebajas = solden'},
   {q:'¿Qué ___ usas? ¿La M o la L?',opts:['talla','caja','etiqueta'],ans:'talla',why:'la talla (maat)'},
   {q:'Pago en la ___.',opts:['caja','bolsa','tarjeta'],ans:'caja',why:'la caja = kassa'},
   {q:'El vestido del ___ es muy bonito.',opts:['escaparate','probador','recibo'],ans:'escaparate',why:'etalage'},
   {q:'En el tianguis puedes ___ el precio.',opts:['regatear','comprar','llevar'],ans:'regatear',why:'regatear = afdingen'},
   {q:'Compro unos zapatos en la ___.',opts:['zapatería','panadería','farmacia'],ans:'zapatería',why:'schoenwinkel'},
   {q:'Pago con ___ o en efectivo.',opts:['tarjeta','talla','bolsa'],ans:'tarjeta',why:'la tarjeta = bankkaart'},
   {q:'Una camisa ___ (gestreept).',opts:['de rayas','de lana','de cuero'],ans:'de rayas',why:'patrón'},
   {q:'El jersey es ___ (van wol).',opts:['de lana','de rayas','de lunares'],ans:'de lana',why:'material'},
   {q:'Me queda bien. Me ___ llevo.',opts:['lo','la','las'],ans:'lo',why:'el jersey → lo'},
   {q:'Miro el precio en la ___.',opts:['etiqueta','caja','talla'],ans:'etiqueta',why:'prijskaartje'}]});
 buildChoice('vx_def',{title:'¿Qué palabra es?',desc:'Lees de definitie en kies het juiste woord.',per:6,pool:[
   {q:'Prenda para la parte de arriba, con mangas cortas:',opts:['la camiseta','la falda','los zapatos'],ans:'la camiseta',why:'T-shirt'},
   {q:'Prenda para las piernas, de tela vaquera:',opts:['los vaqueros','el jersey','la gorra'],ans:'los vaqueros',why:'jeans'},
   {q:'Sitio donde te pruebas la ropa:',opts:['el probador','la caja','el escaparate'],ans:'el probador',why:'paskamer'},
   {q:'Descuentos dos veces al año:',opts:['las rebajas','la talla','la bolsa'],ans:'las rebajas',why:'solden'},
   {q:'Tienda donde venden pan:',opts:['la panadería','la zapatería','la farmacia'],ans:'la panadería',why:'bakkerij'},
   {q:'Patrón con líneas:',opts:['de rayas','de lunares','de cuadros'],ans:'de rayas',why:'gestreept'},
   {q:'Se usa para pagar sin efectivo:',opts:['la tarjeta','la etiqueta','el recibo'],ans:'la tarjeta',why:'bankkaart'},
   {q:'Mercado al aire libre en México:',opts:['el tianguis','el probador','el descuento'],ans:'el tianguis',why:'tianguis 🇲🇽'},
   {q:'Prenda para los pies, para el deporte:',opts:['las zapatillas','las botas','la gorra'],ans:'las zapatillas',why:'sportschoenen'},
   {q:'Color del cielo, no cambia de género:',opts:['azul','rojo','blanco'],ans:'azul',why:'azul (invariable)'}]});
 buildOdd('vx_odd',{title:'El intruso',desc:'Klik het woord dat NIET bij de andere hoort.',per:5,pool:[
   {words:['la camiseta','la falda','el vestido','el probador'],odd:3,why:'el probador is geen prenda'},
   {words:['los zapatos','las botas','las sandalias','la gorra'],odd:3,why:'la gorra = complemento, geen calzado'},
   {words:['rojo','azul','verde','la talla'],odd:3,why:'la talla is geen color'},
   {words:['de rayas','de cuadros','de lunares','la caja'],odd:3,why:'la caja is geen patrón'},
   {words:['la zapatería','la panadería','la farmacia','el vestido'],odd:3,why:'el vestido is geen tienda'},
   {words:['las rebajas','el descuento','la caja','el poncho'],odd:3,why:'el poncho is een prenda, geen winkelwoord'},
   {words:['este','ese','aquel','rojo'],odd:3,why:'«rojo» is geen demostrativo'},
   {words:['comprar','llevar','probarse','la bolsa'],odd:3,why:'la bolsa is geen werkwoord'},
   {words:['azul','gris','verde','roja'],odd:3,why:'«roja» heeft een -a; de rest is onveranderlijk'}]});
 // LECTURA
 buildOrder('lx_order',{title:'Ordena la compra',desc:'Tik de items in de juiste volgorde.',rounds:[
   {sub:'los pasos de la compra',items:[{label:'Entrar en la tienda',key:1},{label:'Elegir una prenda',key:2},{label:'Probarse en el probador',key:3},{label:'Pagar en la caja',key:4}]},
   {sub:'de barato a caro (Moda Diego)',items:[{label:'Camiseta — 5 €',key:1},{label:'Vestido de lunares — 20 €',key:2},{label:'Vaqueros — 25 €',key:3},{label:'Zapatillas — 39 €',key:4}]},
   {sub:'el diálogo de la tienda',items:[{label:'¿Qué desea?',key:1},{label:'Busco una camisa azul.',key:2},{label:'¿Puedo probármela?',key:3},{label:'Me queda bien, me la llevo.',key:4}]},
   {sub:'la distancia (cerca → lejos)',items:[{label:'esta camiseta (aquí)',key:1},{label:'esa gorra (ahí)',key:2},{label:'aquel abrigo (allí)',key:3}]}]});
 buildChoice('lx_scan',{title:'Comprensión: escanea y escoge',desc:'Zoek de info in het anuncio en de reseña en kies het juiste antwoord.',per:6,pool:[
   {q:'¿Cuánto cuestan los vaqueros en rebajas?',opts:['25 €','40 €','39 €'],ans:'25 €',why:'«de 40 a 25 euros»'},
   {q:'¿Qué compró Valen?',opts:['unos vaqueros','una camiseta','unas zapatillas'],ans:'unos vaqueros',why:'«acabo de comprar unos vaqueros»'},
   {q:'¿Cuánto cuestan las camisetas de algodón ahora?',opts:['5 €','10 €','20 €'],ans:'5 €',why:'«de 10 a 5 euros»'},
   {q:'¿Cómo pagó Valen?',opts:['con tarjeta','en efectivo','no pagó'],ans:'con tarjeta',why:'«pagué con tarjeta»'},
   {q:'¿Por qué no compró la camiseta lisa?',opts:['no la tenían en su talla','era cara','no le gustó'],ans:'no la tenían en su talla',why:'«no la tenían en mi talla»'},
   {q:'¿Cuál es el mayor descuento del anuncio?',opts:['−50 %','−30 %','−20 %'],ans:'−50 %',why:'«hasta −50 %»'},
   {q:'¿Cuánto cuestan las zapatillas blancas ahora?',opts:['39 €','60 €','25 €'],ans:'39 €',why:'«de 60 a 39 euros»'},
   {q:'¿Se puede regatear en Moda Diego?',opts:['sí','no','solo con tarjeta'],ans:'sí',why:'«se puede regatear»'},
   {q:'¿Cuántas estrellas dio Valen?',opts:['4','5','3'],ans:'4',why:'★★★★☆'},
   {q:'¿Dónde se probó los vaqueros?',opts:['en el probador','en la caja','en el escaparate'],ans:'en el probador',why:'«me los probé en el probador»'}]});
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
   var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='U6_web_mijn_versie.html';a.click();};
})();
"""

# Getypte woordenschat-drills (fase ophalen + produceren) in het paneel zelf.
JS += hub_type_sets.vocab_type_js(vocab)
JS += hub_type_gram.js('C5', 6)
JS += hub_bloques.retos_js('retos_u6', 'C5', 6)
JS += (hub_bloques.escucha_js("esc_u6", escucha_data.C5_U6)
       + hub_bloques.lectura_js("lec_u6", lectura_data.C5_U6))
HTML = HTML.replace("__GRAMSLOTS__", hub_type_gram.slots('C5', 6))
HTML = HTML.replace("__NGAMES__", str(len(GAMES)))
HTML = HTML.replace("__BRONNEN__", extra_bronnen.html('C5', 6))
HTML = HTML.replace("__TYPESLOTS__", hub_type_sets.SLOTS_HTML)

# Het rollenspel: offline oefenpartner in het Hablar-paneel.
_rol = gen_rol.componente("C5", 6)
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
open(f"{ROOT}/03-build/web/U6_web.html","w").write(html)
print("U6_web.html geschreven:", len(html), "bytes ·", len(GAMES), "spellen ingebed")
