#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de print-HTML U1.html (C5 · Unidad 1 «¿Quién eres?») → PDF via Chromium.
# Zelfde componentenkit/pijplijn als golden sample U0 (cursus-print.css). Fonts base64 ingebed,
# cast-avatars inline SVG (cast_gen). Cursuskleur = groen (C5). Output = standalone bewerkbare U1.html.
import os, sys, base64
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f"{ROOT}/02-huisstijl/beeld/generators")
import cast_gen as C
sys.path.insert(0, "/home/user/espa-ol-en-la-pr-ctica/03-build/web")
import qr_print as QRP; QRP.fijar("C5", 1)
import print_bloques as PB
import apoyo as APO
import lectura_data as LD
import escucha_data as ED
import retos_data as RD
import retos_print as RP

def b64(p): return base64.b64encode(open(p, "rb").read()).decode()
def face(fam, fn, w):
    return (f"@font-face{{font-family:'{fam}';src:url(data:font/woff2;base64,"
            f"{b64(f'{ROOT}/02-huisstijl/fonts/{fn}')}) format('woff2');font-weight:{w};font-display:swap}}")
FONTS = "".join([
    face("Bricolage Grotesque", "BricolageGrotesque-700.woff2", "700"),
    face("Bricolage Grotesque", "BricolageGrotesque-800.woff2", "800"),
    face("Bricolage Grotesque XBold", "BricolageGrotesque-800.woff2", "800"),
    face("Inter", "Inter-400.woff2", "400"),
    face("Inter", "Inter-600.woff2", "600"),
    face("Inter", "Inter-700.woff2", "700"),
    face("Caveat", "Caveat-700.woff2", "700"),
])

# cast-avatars (inline SVG, circulair) voor de openerstrip
AV = {n: C.make(n, "avatar", 64) for n in ["lucia", "diego", "valen", "nina"]}
TU = C.tu_avatar(64)
MOCH = C.mochila(84, "map")

# ---------- CSS: identiek aan golden sample U0 (cursus-print.css + schrijf-componenten) ----------
CSS = FONTS + r"""
@page{ size:A4; margin:12mm 0; }
@page:first{ margin:0 0 12mm 0; }
*{ box-sizing:border-box; }
html{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }
:root{
 --g:#1E9E74; --gd:#157355; --gt:#E4F4EE; --ink:#20242E; --mut:#6A6E78; --paper:#FCFBF8; --crema:#F3EEE4; --line:#E4E3DE; --line2:#CFCEC8; --red:#DC2626; --amber:#B7860B; --amberbg:#FBF3D6;
 --luc:#E07A5F; --die:#C85B9A; --val:#2FA8A0; --nin:#D69A2E;
 --onder:#2563EB; --ww:#EA7317; --voorw:#1E9E74; --tijd:#7C3AED; --plaats:#14B8A6;
 --disp:'Bricolage Grotesque',sans-serif; --dispx:'Bricolage Grotesque XBold','Bricolage Grotesque',sans-serif; --body:'Inter',sans-serif; --hand:'Caveat',cursive;
}
body{ margin:0; font-family:var(--body); color:var(--ink); background:var(--paper); font-size:10.3pt; line-height:1.5; }
.page{ padding:0 15mm; }
.gloss{ color:var(--mut); font-style:italic; }

.regla,.truc,.pcard,.call,.qr,.guide,.esen,.audiorow,.wcols,.wbox,.sem,.acthead,.chatline,.fichacard,.mispal,.ptext,.lecdoel,.gustobars,.menu{ break-inside:avoid; }

.act{ break-inside:auto; }
.alf tr,.mp tr,.sem tr,.conj tr{ break-inside:avoid; } .alf thead,.mp thead,.sem thead,.conj thead{ display:table-header-group; }
 
/* schrijf-componenten */
.wl{ display:inline-block; border-bottom:1.6px solid var(--line2); min-width:34mm; height:6mm; vertical-align:-1.6mm; }
.wl.sm{ min-width:18mm } .wl.md{ min-width:50mm } .wl.lg{ min-width:72mm }
.wl.full{ display:block; width:100%; margin:3mm 0 }
.wbox{ border:1px solid var(--line2); border-radius:8pt; background-image:repeating-linear-gradient(var(--paper) 0 8.6mm, var(--line) 8.6mm 8.7mm); min-height:35mm; margin:3mm 0; }
.wbox.sm{ min-height:26mm } .wbox.lg{ min-height:52mm }
.wcols{ display:grid; gap:3.5mm; margin:3.5mm 0; }
.wcol{ border:1px solid var(--line); border-radius:10pt; overflow:hidden; background:#fff; }
.wcol>.ch{ font-family:var(--disp); font-weight:700; font-size:9.4pt; color:var(--gd); background:var(--gt); padding:2mm 3mm; text-align:center; }
.wcol>.ch small{ display:block; font-family:var(--body); font-weight:400; font-size:7.4pt; color:var(--mut); text-transform:none; letter-spacing:0 }
.wcol>.cb{ min-height:44mm; background-image:repeating-linear-gradient(#fff 0 8mm, var(--line) 8mm 8.1mm); }
.wcol>.cb.short{ min-height:30mm } .wcol>.cb.tall{ min-height:58mm }
.wtab td{ height:9mm; vertical-align:top } .wtab .wl{ margin-top:1mm }
/* hero */
.hero{ background:var(--g); color:#fff; padding:13mm 15mm 8mm; position:relative; }
.hero .eyebrow{ font-size:9pt; letter-spacing:.16em; font-weight:600; opacity:.9; }
.hero h1{ font-family:var(--dispx); font-size:47pt; line-height:1; margin:2mm 0 2mm; }
.hero .sub{ font-size:12pt; max-width:140mm; opacity:.97; } .hero .sub .gloss{ color:#DDF3EA; }
.hero .q{ margin-top:7mm; display:inline-block; font-family:var(--disp); font-weight:700; font-size:14pt; background:rgba(255,255,255,.15); border-radius:22pt; padding:3mm 7mm; }
.hero .tab{ position:absolute; top:0; right:0; background:var(--gd); color:#fff; font-weight:700; font-size:8.5pt; letter-spacing:.12em; padding:3mm 6mm; border-radius:0 0 0 10pt; }
.se{ font-size:8pt; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--mut); margin:0 0 1.5mm; }
h2{ font-family:var(--disp); font-weight:700; font-size:14pt; margin:0 0 3mm; color:var(--gd); }
h3{ font-family:var(--disp); font-weight:700; font-size:12pt; margin:0 0 2mm; color:var(--ink); }
.lead{ display:grid; grid-template-columns:1.15fr .85fr; gap:9mm; align-items:start; }
.hist{ font-size:10pt; margin-top:2mm; } .hist .gloss{ display:block; }
.ojo{ margin-top:4mm; border-left:3px solid var(--red); padding:1.5mm 0 1.5mm 4mm; font-size:9.4pt; } .ojo b{ color:var(--red); }
.cast{ display:grid; grid-template-columns:repeat(5,1fr); gap:4mm; margin-top:2mm; }
.pc{ text-align:center; } .av{ width:17mm; height:17mm; border-radius:50%; margin:0 auto 2mm; display:flex; align-items:center; justify-content:center; font-family:var(--dispx); font-size:15pt; color:#fff; }
.pc .nm{ font-family:var(--disp); font-weight:700; font-size:11pt; } .pc .fr{ font-size:8pt; color:var(--mut); }
.tu .av{ background:#fff; border:2px dashed var(--g); color:var(--g); }
.avw{ width:17mm; margin:0 auto 2mm; line-height:0; } .avw svg{ width:100%; height:auto; display:block; }
.moch{ background:var(--gt); border-radius:12pt; padding:5mm 6mm; margin-top:7mm; display:flex; gap:5mm; align-items:center; }
.moch .ic{ width:16mm;height:16mm;border-radius:10pt;background:#fff;display:flex;align-items:center;justify-content:center;flex:none; } .moch .ic svg{width:100%;height:auto}
.moch .hand{ font-family:var(--hand); font-size:16pt; color:var(--gd); }
.obj ul{ list-style:none; padding:0; margin:3mm 0 0; display:grid; grid-template-columns:1fr 1fr; gap:3mm 8mm; }
.obj li{ display:flex; gap:3mm; font-size:10pt; } .obj .ck{ color:var(--g); font-weight:800; } .obj .es{ font-weight:600; } .obj .nl{ color:var(--mut); font-size:8.5pt; }
.mini{ margin-top:4mm; background:var(--crema); border-radius:12pt; padding:3.5mm 6mm; break-inside:avoid; }
.mini .steps{ display:flex; justify-content:space-between; margin-top:3mm; font-size:8pt; color:var(--mut); text-align:center; gap:2mm; } .mini .steps b{ display:block; color:var(--ink); font-size:9pt; font-family:var(--disp); }
/* parada header */
.parada{ border-top:3px solid var(--g); padding-top:6mm; margin-top:2mm; position:relative; }
.parada .num{ position:absolute; right:0; top:4mm; font-family:var(--dispx); font-size:60pt; color:var(--gt); line-height:.8; z-index:0; }
.parada .pk{ position:relative; z-index:1; display:inline-block; background:var(--g); color:#fff; font-family:var(--disp); font-weight:700; font-size:12.5pt; border-radius:8pt; padding:2mm 6mm; }
.intro{ font-size:10pt; margin-top:4mm; position:relative; z-index:1; } .intro .gloss{ display:block; margin-top:.5mm; }
.route-note{ font-size:8.5pt; color:var(--gd); background:var(--gt); border-radius:8pt; padding:2.5mm 5mm; margin-top:4mm; }
.lpd{ display:flex; flex-wrap:wrap; gap:2mm; align-items:center; margin-top:4mm; }
.lpdlab{ font-size:7.4pt; font-weight:700; letter-spacing:.1em; text-transform:uppercase; color:var(--mut); }
.lpdchip{ font-size:7.8pt; background:#fff; border:1px solid var(--g); color:var(--gd); border-radius:20pt; padding:.8mm 3mm; }
.lpdchip b{ color:var(--g); }
/* audio callout + QR */
.audiorow{ display:grid; grid-template-columns:1fr auto; gap:5mm; margin:6mm 0; align-items:stretch; }
.call{ display:flex; gap:4mm; align-items:flex-start; background:var(--gt); border-radius:12pt; padding:4mm 5mm; font-size:9.7pt; } .call .ic{ font-size:16pt; } .call b{ color:var(--gd); }
.qr{ background:#fff; border:1px solid var(--line); border-radius:12pt; padding:3mm 4mm; text-align:center; width:38mm; }
.qr .lab{ font-size:7.4pt; font-weight:700; letter-spacing:.1em; color:var(--gd); text-transform:uppercase; }
.qr .meta{ font-size:7.6pt; color:var(--mut); margin-top:1mm; }
.asset{ font-size:7.6pt; color:#9AA0A6; font-style:italic; }
/* mochila guide */
.guide{ display:flex; gap:4mm; align-items:center; background:#fff; border:1.5px dashed var(--g); border-radius:14pt; padding:3.5mm 5mm; margin:6mm 0; }
.guide .ic{ font-size:20pt; } .guide .hand{ font-family:var(--hand); font-size:15pt; color:var(--gd); } .guide .g{ font-size:8.6pt; color:var(--mut); }
/* tabellen */
table{ border-collapse:collapse; width:100%; font-size:8.9pt; margin:3mm 0; }
.alf td,.alf th{ border:1px solid var(--line); padding:1.6mm 2.4mm; text-align:left; }
.alf th{ background:var(--gt); color:var(--gd); font-weight:700; font-size:7.9pt; text-transform:uppercase; letter-spacing:.04em; }
.alf .L{ font-family:var(--disp); font-weight:700; }
.trap{ color:var(--red); font-weight:700; }
/* regla = onthoudkaart */
.regla{ border:1.5px solid var(--g); border-radius:12pt; padding:4mm 5.5mm; margin:6mm 0; background:#fff; position:relative; }
.regla .tag{ font-family:var(--disp); font-weight:700; color:#fff; background:var(--g); font-size:9pt; border-radius:20pt; padding:1mm 4mm; position:absolute; top:-3mm; left:5mm; }
.regla p{ margin:3mm 0 0; font-size:9.7pt; }
/* tip amber */
.truc{ background:var(--amberbg); border-radius:12pt; padding:3.5mm 5mm; margin:5mm 0; font-size:9.5pt; } .truc b{ color:var(--amber); }
/* activity */
.act{ margin:6mm 0; }
.acthead{ display:flex; gap:3.5mm; align-items:center; }
.anum{ width:9mm; height:9mm; border-radius:50%; background:var(--g); color:#fff; font-family:var(--dispx); font-size:11pt; display:flex; align-items:center; justify-content:center; flex:none; }
.act .h{ font-family:var(--disp); font-weight:700; font-size:11pt; }
.badges{ display:flex; flex-wrap:wrap; gap:1.5mm; margin-top:.8mm; }
.badge{ font-size:7.3pt; font-weight:600; border-radius:20pt; padding:.5mm 2.6mm; background:var(--crema); color:var(--ink); }
.badge.skill{ background:var(--gt); color:var(--gd); }
.stars{ font-size:8pt; color:var(--amber); letter-spacing:1px; }
.act p{ margin:2.5mm 0 2.5mm 12.5mm; font-size:9.6pt; }
.act .steun{ margin-left:12.5mm; }
.words b{ background:var(--gt); border-radius:4pt; padding:.3mm 1.5mm; font-weight:600; }
.steun{ display:inline-block; font-size:7.4pt; font-weight:700; letter-spacing:.08em; text-transform:uppercase; color:var(--g); border:1px solid var(--g); border-radius:20pt; padding:.6mm 3mm; }
/* divider */
.divider{ display:flex; align-items:center; gap:4mm; margin:9mm 0 6mm; color:var(--mut); font-size:8pt; letter-spacing:.14em; text-transform:uppercase; font-weight:700; }
.divider::before,.divider::after{ content:""; flex:1; height:2px; background:repeating-linear-gradient(90deg,var(--line2) 0 4px,transparent 4px 10px); }
/* pron/info cards */
.fams{ display:grid; grid-template-columns:1fr 1fr; gap:5mm; margin-top:4mm; }
.fams.three{ grid-template-columns:1fr 1fr 1fr; }
.pcard{ border:1px solid var(--line); border-radius:12pt; padding:4mm 5mm; background:#fff; }
.pcard .t{ font-family:var(--disp); font-weight:700; font-size:11.5pt; color:var(--gd); }
.pcard .anchor{ font-size:9pt; margin:2mm 0; } .pcard .anchor b{ color:var(--amber); }
.pcard .ej{ font-size:9pt; } .pcard .ej b{ background:var(--gt); border-radius:4pt; padding:.3mm 1.5mm; }
.pcard .t2{ color:var(--red); font-size:8.8pt; margin-top:2mm; }
.mp{ width:100%; font-size:9.2pt; } .mp td,.mp th{ border:1px solid var(--line); padding:1.7mm 3mm; } .mp th{ background:var(--gt); color:var(--gd); font-size:8pt; text-transform:uppercase; }
/* conjugatie-kaart */
.conj{ width:100%; font-size:9.4pt; } .conj td,.conj th{ border:1px solid var(--line); padding:1.6mm 3mm; } .conj th{ background:var(--gt); color:var(--gd); font-size:8pt; text-transform:uppercase; } .conj .p{ color:var(--mut); } .conj .v{ font-weight:700; } .conj .end{ color:var(--ww); }
/* woordscene datos (gelabelde ficha) */
.fichacard{ display:grid; grid-template-columns:1fr 1fr; gap:5mm; border:1.5px solid var(--g); border-radius:14pt; padding:5mm 6mm; margin:5mm 0; background:#fff; }
.fichacard .row{ display:flex; justify-content:space-between; gap:3mm; border-bottom:1px dashed var(--line); padding:1.6mm 0; font-size:9.3pt; }
.fichacard .row .k{ color:var(--gd); font-weight:600; } .fichacard .row .v{ color:var(--ink); } .fichacard .row .nl{ color:var(--mut); font-size:7.8pt; }
/* chat/dialoog-bubbels */
.chat{ margin:4mm 0; } .chatline{ display:flex; gap:3mm; margin:2mm 0; align-items:flex-end; } .chatline.me{ flex-direction:row-reverse; }
.bub{ max-width:72%; border-radius:12pt; padding:2.4mm 4mm; font-size:9.4pt; } .chatline.you .bub{ background:var(--gt); color:var(--ink); border-bottom-left-radius:2pt; } .chatline.me .bub{ background:var(--g); color:#fff; border-bottom-right-radius:2pt; }
.chatline .who{ font-size:7.4pt; color:var(--mut); margin:0 2mm; }
/* kleur-semantiek chips (taalfuncties) */
.fx{ border-radius:4pt; padding:.2mm 1.4mm; font-weight:600; } .fx.per{ background:#DBEAFE; color:#1E40AF; } .fx.vb{ background:#FED7AA; color:#9A3412; } .fx.ob{ background:#DCFCE7; color:#166534; } .fx.ti{ background:#EDE9FE; color:#5B21B6; } .fx.pl{ background:#CCFBF1; color:#0F766E; }
.leg{ display:flex; gap:3mm; flex-wrap:wrap; font-size:7.6pt; margin-top:2mm; color:var(--mut); }
/* route-strip opener */
.rutastrip{ display:flex; align-items:center; gap:0; margin:3mm 0 0; }
.rutastrip .stop{ text-align:center; flex:1; position:relative; }
.rutastrip .dot{ width:5mm; height:5mm; border-radius:50%; background:var(--line2); margin:0 auto; }
.rutastrip .stop.on .dot{ background:var(--g); box-shadow:0 0 0 2px var(--gt); }
.rutastrip .stop.done .dot{ background:var(--gd); }
.rutastrip .lbl{ font-size:7pt; color:var(--mut); margin-top:1mm; } .rutastrip .stop.on .lbl{ color:var(--gd); font-weight:700; }
.rutastrip .bar{ height:2px; background:var(--line2); flex:0 0 auto; width:100%; position:absolute; top:2.5mm; left:50%; z-index:-1; }
/* esencial + bridge + semaforo */
.esen{ background:var(--crema); border-radius:14pt; padding:5mm 6mm; margin-top:6mm; font-size:9.6pt; } .esen b.tt{ font-family:var(--disp); color:var(--gd); font-size:11pt; } .esen ul{ margin:2mm 0 0; } .esen li{ margin:1.5mm 0; }
.bridge{ border-top:1px solid var(--line); margin-top:8mm; padding-top:3.5mm; font-size:9.5pt; } .bridge b{ color:var(--gd); }
.sem{width:100%;font-size:9pt;margin:3mm 0} .sem td,.sem th{border:1px solid var(--line);padding:1.7mm 3mm} .sem th,.semrow th{background:var(--gt);color:var(--gd);font-size:8pt;text-transform:uppercase;font-weight:700}
.pasos{ counter-reset:paso; list-style:none; padding:0; margin:3mm 0; }
.pasos li{ position:relative; padding:2mm 0 3mm 12mm; font-size:9.7pt; min-height:10mm; }
.pasos li::before{ counter-increment:paso; content:counter(paso); position:absolute; left:0; top:1mm; width:8mm; height:8mm; border-radius:50%; background:var(--g); color:#fff; font-family:var(--dispx); font-size:10pt; display:flex; align-items:center; justify-content:center; }
/* editbar */
.editbar{ position:fixed; right:14px; bottom:14px; z-index:9999; display:flex; gap:8px; align-items:center; background:#157355; color:#fff; padding:8px 12px; border-radius:12px; box-shadow:0 6px 20px #0004; font-family:'Inter',sans-serif; font-size:13px; }
.editbar button{ border:none; border-radius:8px; padding:7px 12px; font-weight:700; cursor:pointer; font-family:inherit; font-size:13px; }
.editbar .b1{ background:#fff; color:#157355; } .editbar .b2{ background:#ffffff22; color:#fff; } .editbar.on{ background:#B7860B; }
body.editing [contenteditable="true"]{ outline:1.4px dashed #B7860B; outline-offset:2px; border-radius:3px; }
body.editing [contenteditable="true"]:focus{ outline:2px solid #157355; background:#FEF9E7; }
@media print{ .editbar{ display:none !important; } body.editing [contenteditable="true"]{ outline:none !important; background:none !important; } }
/* ===== VISUELE GRAMMATICA-/WOORDENSCHATCOMPONENTEN (VISUELE_WOORDENSCHAT_EN_GRAMMATICA.md) ===== */
/* observatie-voorbeelden met gemarkeerd patroon */
.obsbox{ background:var(--gt); border-radius:12pt; padding:4mm 5mm; margin:3mm 0; }
.obsbox .ln{ font-size:11pt; margin:1.6mm 0; } .obsbox .hl{ background:#fff; border-bottom:2px solid var(--g); border-radius:3pt; padding:.2mm 1.4mm; font-weight:700; color:var(--gd); }
.obsq{ font-size:9pt; color:var(--gd); margin-top:2mm; } .obsq b{ color:var(--gd); }
/* GrammarMachine: infinitivo -> raíz -> terminación -> forma */
.machine{ display:flex; align-items:center; gap:0; flex-wrap:wrap; margin:4mm 0; }
.machine .mbox{ border:1.5px solid var(--g); border-radius:10pt; padding:2.5mm 4mm; text-align:center; background:#fff; min-width:22mm; }
.machine .mbox .lb{ font-size:7pt; letter-spacing:.08em; text-transform:uppercase; color:var(--mut); display:block; }
.machine .mbox .vv{ font-family:var(--disp); font-weight:700; font-size:12.5pt; color:var(--ink); } .machine .mbox .vv .end{ color:var(--ww); }
.machine .arr{ color:var(--g); font-weight:800; font-size:14pt; padding:0 3mm; }
.machine .mbox.res{ background:var(--gt); border-color:var(--gd); }
/* GrammarBuildingBlocks: verwisselbare blokken */
.blocks{ margin:3mm 0; } .brow{ display:flex; gap:2mm; margin:2mm 0; flex-wrap:wrap; align-items:center; }
.blk{ border-radius:8pt; padding:1.8mm 4mm; font-weight:600; font-size:10pt; border:1.5px solid; }
.blk.per{ background:#DBEAFE; border-color:#93c5fd; color:#1E40AF; } .blk.vb{ background:#FED7AA; border-color:#fdba74; color:#9A3412; }
.blk.ob{ background:#DCFCE7; border-color:#86efac; color:#166534; } .blk.pl{ background:#CCFBF1; border-color:#5eead4; color:#0F766E; } .blk.ti{ background:#EDE9FE; border-color:#c4b5fd; color:#5B21B6; }
.blk.opt{ background:#fff; border-color:var(--line2); color:var(--ink); border-style:dashed; }
/* GrammarAgreementMap: overeenkomst met verbindingsboog */
.agree{ text-align:center; margin:3mm 0; font-family:var(--disp); }
.agree .w{ font-size:15pt; font-weight:700; } .agree .w u{ color:var(--gd); text-decoration-thickness:2px; text-underline-offset:2px; }
.agree .tie{ font-size:8pt; color:var(--mut); margin-top:1mm; }
/* GrammarDecisionTree */
.tree{ border-left:3px solid var(--g); margin:3mm 0 3mm 3mm; padding-left:5mm; }
.tree .node{ font-size:9.6pt; margin:2mm 0; } .tree .node b{ color:var(--gd); } .tree .yes{ color:var(--g); font-weight:700; } .tree .no{ color:var(--mut); font-weight:700; }
.tree .res{ display:inline-block; background:var(--g); color:#fff; font-family:var(--disp); font-weight:700; border-radius:6pt; padding:.6mm 3mm; }
/* GrammarQuestionMirror */
.mirror{ margin:3mm 0; } .mirror .mq{ font-size:11pt; font-weight:700; color:var(--onder); } .mirror .ma{ font-size:11pt; color:var(--gd); margin-left:8mm; }
.mirror .mk{ background:#EDE9FE; border-radius:3pt; padding:.2mm 1.2mm; font-weight:700; }
/* GrammarFormMeaningUse */
.fmu{ display:grid; grid-template-columns:repeat(3,1fr); gap:3mm; margin:3mm 0; }
.fmu .fc{ border:1px solid var(--line); border-radius:10pt; overflow:hidden; background:#fff; }
.fmu .fc .hd{ font-family:var(--disp); font-weight:700; font-size:8pt; letter-spacing:.08em; text-transform:uppercase; color:#fff; background:var(--g); padding:1.6mm 3mm; text-align:center; }
.fmu .fc .bd{ padding:2.5mm 3mm; font-size:9.4pt; }
/* GrammarScaffold: aflopende steiger */
.scaffold{ display:grid; grid-template-columns:repeat(4,1fr); gap:2mm; margin:3mm 0; align-items:end; }
.scaffold .sq{ border:1.5px solid var(--g); border-radius:9pt; background:#fff; padding:2.5mm 3mm; font-size:8.6pt; }
.scaffold .sq .st{ font-size:7pt; text-transform:uppercase; letter-spacing:.08em; color:var(--g); font-weight:700; display:block; margin-bottom:1mm; }
.scaffold .s1{ height:34mm } .scaffold .s2{ height:29mm } .scaffold .s3{ height:24mm } .scaffold .s4{ height:19mm; background:var(--gt); }
/* GrammarZoom un/el */
.zoom{ display:grid; grid-template-columns:1fr auto 1fr; gap:3mm; align-items:center; margin:3mm 0; }
.zoom .zc{ border:1px solid var(--line); border-radius:10pt; padding:3mm 4mm; text-align:center; background:#fff; } .zoom .zc .zh{ font-size:7.6pt; text-transform:uppercase; color:var(--mut); } .zoom .zc b{ font-family:var(--disp); font-size:13pt; color:var(--gd); }
.zoom .zar{ font-size:16pt; color:var(--g); }
/* VocabularyCluster */
.clusters{ display:grid; grid-template-columns:repeat(3,1fr); gap:4mm; margin:3mm 0; }
.clu{ border:1px solid var(--line); border-top:4px solid var(--g); border-radius:12pt; padding:3mm 4mm; background:#fff; }
.clu .ch{ font-family:var(--disp); font-weight:700; font-size:10.5pt; color:var(--gd); display:flex; gap:2mm; align-items:center; } .clu .ci{ font-size:14pt; }
.clu ul{ margin:2mm 0 0; padding-left:4mm; font-size:9.4pt; } .clu li{ margin:.8mm 0; }
.clu .ex{ font-size:8.4pt; color:var(--mut); font-style:italic; margin-top:2mm; }
/* VocabularyCollocation: centraal werkwoord + takken */
.colloc{ display:flex; gap:5mm; align-items:center; margin:3mm 0; flex-wrap:wrap; }
.colloc .cen{ background:var(--ww); color:#fff; font-family:var(--disp); font-weight:800; font-size:15pt; border-radius:12pt; padding:4mm 7mm; }
.colloc .brs{ display:flex; flex-wrap:wrap; gap:2mm; } .colloc .br{ background:var(--gt); color:var(--gd); border-radius:20pt; padding:1.4mm 4mm; font-size:9.6pt; font-weight:600; }
/* VocabularyScale */
.scale{ margin:3mm 0; } .scale .track{ display:flex; align-items:center; gap:0; } .scale .sstop{ flex:1; text-align:center; position:relative; }
.scale .sd{ width:3.5mm; height:3.5mm; border-radius:50%; background:var(--g); margin:0 auto; } .scale .sl{ font-size:8.6pt; margin-top:1mm; color:var(--ink); }
.scale .bar{ position:absolute; top:1.6mm; left:0; right:-100%; height:2px; background:var(--line2); z-index:-1; }
/* VocabularyPair */
.vpairs{ display:grid; grid-template-columns:1fr 1fr; gap:2mm 6mm; margin:3mm 0; }
.vp{ display:flex; justify-content:space-between; border-bottom:1px dashed var(--line); padding:1.2mm 0; font-size:10pt; } .vp b{ color:var(--gd); } .vp .ar{ color:var(--mut); }
/* Mis palabras */
.mispal{ border:1.5px dashed var(--g); border-radius:12pt; padding:3mm 4mm; margin:4mm 0; background:#fff; }
.mispal .mh{ font-family:var(--hand); font-size:14pt; color:var(--gd); }
.mispal table{ width:100%; margin:2mm 0 0; } .mispal td,.mispal th{ border:1px solid var(--line); padding:1.4mm 2mm; height:8mm; font-size:8.6pt; } .mispal th{ background:var(--gt); color:var(--gd); font-size:7.6pt; text-transform:uppercase; }
/* GrammarXRay */
.xray{ margin:3mm 0; } .xray .xs{ font-family:var(--disp); font-size:12pt; text-align:center; } .xray .xrow{ display:flex; justify-content:center; gap:4mm; margin-top:2mm; flex-wrap:wrap; font-size:8.4pt; color:var(--mut); text-align:center; } .xray .xrow b{ display:block; color:var(--ink); font-family:var(--body); }
/* pictogram-cirkel voor cluster/sectie */
.pico{ width:9mm;height:9mm;border-radius:50%;background:var(--gt);display:inline-flex;align-items:center;justify-content:center;font-size:12pt; }
/* ===== leesvaardigheid (Lectura) ===== */
.lecdoel{ background:var(--amberbg); border-left:3px solid var(--amber); border-radius:8pt; padding:2.5mm 5mm; margin:3mm 0; font-size:9.6pt; } .lecdoel b{ color:var(--amber); }
.txtmeta{ display:flex; gap:2mm; flex-wrap:wrap; margin:2mm 0; } .txtmeta .tm{ font-size:7.6pt; font-weight:600; background:var(--gt); color:var(--gd); border-radius:20pt; padding:.7mm 3mm; } .txtmeta .tm b{ color:var(--gd); }
.ptexts{ display:grid; grid-template-columns:1fr 1fr; gap:5mm; margin:3mm 0; }
.ptext{ border:1px solid var(--line); border-top:4px solid var(--g); border-radius:12pt; padding:4mm 5mm; background:#fff; font-size:9.5pt; }
.ptext .ph{ display:flex; gap:3mm; align-items:center; margin-bottom:2mm; } .ptext .ph .av{ width:12mm;height:12mm;border-radius:50%;overflow:hidden;flex:none } .ptext .ph .av svg{width:100%;height:auto} .ptext .ph .nm{ font-family:var(--disp); font-weight:700; font-size:11pt; color:var(--ink); } .ptext .ph .fr{ font-size:8pt; color:var(--mut); }
.ptext p{ margin:1.5mm 0; } .evi{ background:#FEF3C7; border-radius:3pt; padding:.1mm 1mm; }
/* smaak-/encuesta-bars (infografía · lezen van data) — kit-pariteit met U5 */
.gustobars{ margin:3mm 0; } .gbar{ display:grid; grid-template-columns:40mm 1fr; gap:3mm; align-items:center; margin:1.8mm 0; font-size:9.2pt; }
.gbar .track2{ background:var(--crema); border-radius:6pt; height:6mm; position:relative; overflow:hidden; }
.gbar .fill{ background:var(--g); height:100%; border-radius:6pt; }
.gbar .pct{ position:absolute; right:2mm; top:0; line-height:6mm; font-size:8pt; color:#fff; font-weight:700; }
.infocard{ border:1px solid var(--line); border-top:4px solid var(--g); border-radius:12pt; padding:4mm 5mm; background:#fff; margin:3mm 0; }
.infocard .it{ font-family:var(--disp); font-weight:700; font-size:11pt; color:var(--gd); } .infocard .isub{ font-size:8pt; color:var(--mut); margin-bottom:1mm; }
/* menú-kaart (kit-pariteit met U5) */
.menu{ border:1.5px solid var(--gd); border-radius:14pt; padding:4mm 6mm; margin:4mm 0; background:#fff; }
.menu .mt{ font-family:var(--disp); font-weight:800; font-size:13pt; color:var(--gd); text-align:center; border-bottom:2px dashed var(--line2); padding-bottom:2mm; }
.menu .sec2{ font-family:var(--disp); font-weight:700; font-size:9.6pt; color:var(--ww); text-transform:uppercase; letter-spacing:.06em; margin:3mm 0 1mm; }
.menu .mi{ display:flex; justify-content:space-between; font-size:9.4pt; padding:.8mm 0; border-bottom:1px dotted var(--line); }
.menu .mi .pr{ color:var(--gd); font-weight:700; }
"""

# ---------------- component-helpers ----------------
import sys as _qs; _qs.path.insert(0, "/home/user/espa-ol-en-la-pr-ctica/03-build/web")
from qr_print import qr          # echte QR-code, zie qr_print.py

def audiorow(call_html, qr_html):
    return f'<div class="audiorow"><div class="call">{call_html}</div>{qr_html}</div>'

def act(num, title, badges, body, steun=None):
    b = "".join(f'<span class="badge{" skill" if s.get("skill") else ""}">{s["t"]}</span>' for s in badges)
    stars = ""
    s = "".join(x for x in [f'<div class="steun" style="margin-left:12.5mm">{steun}</div>' if steun else ""])
    return (f'<div class="act"><div class="acthead"><span class="anum">{num}</span>'
            f'<div><div class="h">{title}</div><div class="badges">{b}</div></div></div>{body}{s}</div>')

def regla(tag, html):
    return f'<div class="regla"><span class="tag">{tag}</span>{html}</div>'

def guide(hand, g, ic="🎒"):
    return f'<div class="guide"><div class="ic">{ic}</div><div><span class="hand">{hand}</span> <span class="g">{g}</span></div></div>'

def lpd(*chips):
    c = "".join(f'<span class="lpdchip"><b>LPD {n}</b> · {t}</span>' for n, t in chips)
    return f'<div class="lpd"><span class="lpdlab">Leerplandoelen III-Spa-d</span>{c}</div>'

def divider(t): return f'<div class="divider">{t}</div>'

def retos(ancla, titulo, intro_es, intro_nl):
    """Het retoblok van één sectie: volledige oefening voor de print-retos,
    een verwijskaartje voor wie op de hub of in de PowerPoint leeft."""
    P('<div class="page">')
    P(divider(titulo))
    P(f'<div class="intro" style="margin-top:1mm"><b>ES:</b> {intro_es} '
      f'<span class="gloss">{intro_nl}</span></div>')
    for r in sorted(RD.por_ancla(ancla), key=lambda x: x["num"]):
        P(RP.reto_print(r) if r["soporte"] == "print" else RP.reto_puntero(r))
    P('</div>')


def pcard(t, body): return f'<div class="pcard"><div class="t">{t}</div>{body}</div>'

def steun(niveau):
    # één plaats voor de hele cursus: apoyo.py maakt er «Apoyo (steun) · Marco
    # (zinsframe): …» van, in het Spaans met het Nederlandse woord erbij
    return APO.html(niveau)

def sortcols(cols, height="short", eigen=True):
    # cols = [(kop, sub)] → geruite sorteer/classificeer-schrijfkolommen (§14 antwoordruimte)
    n = len(cols)
    inner = "".join(
        f'<div class="wcol"><div class="ch">{k}{f"<small>{s}</small>" if s else ""}</div><div class="cb {height}"></div></div>'
        for k, s in cols)
    style = f'grid-template-columns:repeat({n},1fr)'
    eig = ('<div class="gloss" style="font-size:8pt;margin:1mm 0 0 12.5mm">↳ voeg per kolom één <b>eigen</b> woord toe.</div>' if eigen else "")
    return f'<div class="wcols" style="{style};margin-left:12.5mm">{inner}</div>{eig}'

def actx(num, title, badges, body, apoyo=None):
    # activiteit met optioneel apoyo-label (steunniveau)
    return act(num, title, badges, body + (steun(apoyo) if apoyo else ""))

def tarea_com(title, badges, body):
    return act("★", title, badges, body)

# ----- visuele grammatica-/woordenschatcomponenten -----
def obsbox(lines, vragen=None):
    ln = "".join(f'<div class="ln">{l}</div>' for l in lines)
    q = f'<div class="obsq">{vragen}</div>' if vragen else ""
    return f'<div class="obsbox"><div class="se" style="margin:0 0 1.5mm">Observa · ¿qué se repite?</div>{ln}{q}</div>'

def machine(boxes):
    # boxes = [(label, value_html)]; laatste = resultaat
    parts = []
    for i, (lab, val) in enumerate(boxes):
        cls = "mbox res" if i == len(boxes)-1 else "mbox"
        parts.append(f'<div class="{cls}"><span class="lb">{lab}</span><span class="vv">{val}</span></div>')
        if i < len(boxes)-1: parts.append('<span class="arr">→</span>')
    return f'<div class="machine">{"".join(parts)}</div>'

def blocks(rows):
    # rows = [[(cls,text)]]
    out = []
    for r in rows:
        out.append('<div class="brow">' + "".join(f'<span class="blk {c}">{t}</span>' for c, t in r) + '</div>')
    return f'<div class="blocks">{"".join(out)}</div>'

def tree(nodes, resultaten):
    n = "".join(f'<div class="node">{x}</div>' for x in nodes)
    return f'<div class="tree">{n}</div>'

def mirror(pairs):
    out = []
    for q, a in pairs:
        out.append(f'<div class="mq">{q}</div><div class="ma">↳ {a}</div>')
    return f'<div class="mirror">{"".join(out)}</div>'

def fmu(forma, signif, uso):
    return (f'<div class="fmu">'
            f'<div class="fc"><div class="hd">Forma</div><div class="bd">{forma}</div></div>'
            f'<div class="fc"><div class="hd">Significado</div><div class="bd">{signif}</div></div>'
            f'<div class="fc"><div class="hd">Uso</div><div class="bd">{uso}</div></div></div>')

def scaffold(steps):
    # steps = [(label, html)] x4 : MODELO -> FRAME -> CLAVE -> SOLO
    cls = ["s1", "s2", "s3", "s4"]
    return '<div class="scaffold">' + "".join(
        f'<div class="sq {cls[i]}"><span class="st">{lab}</span>{html}</div>' for i, (lab, html) in enumerate(steps)) + '</div>'

def zoom(left_h, left_v, right_h, right_v):
    return (f'<div class="zoom"><div class="zc"><span class="zh">{left_h}</span><br><b>{left_v}</b></div>'
            f'<div class="zar">🔎→</div><div class="zc"><span class="zh">{right_h}</span><br><b>{right_v}</b></div></div>')

def clusters(cols):
    # cols = [(icon, kop, [items], ejemplo)]
    out = []
    for ic, kop, items, ej in cols:
        li = "".join(f'<li>{x}</li>' for x in items)
        out.append(f'<div class="clu"><div class="ch"><span class="ci">{ic}</span>{kop}</div><ul>{li}</ul><div class="ex">{ej}</div></div>')
    return f'<div class="clusters">{"".join(out)}</div>'

def colloc(center, branches):
    br = "".join(f'<span class="br">{b}</span>' for b in branches)
    return f'<div class="colloc"><div class="cen">{center}</div><div class="brs">{br}</div></div>'

def scale(stops):
    s = "".join(f'<div class="sstop"><div class="sd"></div><div class="sl">{x}</div>{"" if i==len(stops)-1 else "<div class=bar></div>"}</div>' for i, x in enumerate(stops))
    return f'<div class="scale"><div class="track">{s}</div></div>'

def vpairs(pairs):
    return '<div class="vpairs">' + "".join(f'<div class="vp"><b>{a}</b><span class="ar">↔</span><span>{b}</span></div>' for a, b in pairs) + '</div>'

def mispal(hand="Mis palabras — je eigen woorden", rows=3):
    body = "".join('<tr><td></td><td></td><td></td></tr>' for _ in range(rows))
    return (f'<div class="mispal"><div class="mh">✍️ {hand}</div>'
            f'<table><thead><tr><th>Palabra (ES)</th><th>Símbolo/dibujo</th><th>Mi ejemplo</th></tr></thead><tbody>{body}</tbody></table></div>')

def xray(sentence, parts):
    p = "".join(f'<div><b>{w}</b>{fn}</div>' for w, fn in parts)
    return f'<div class="xray"><div class="xs">{sentence}</div><div class="xrow">{p}</div></div>'

def gustobars(rows):
    inner = "".join(f'<div class="gbar"><span>{lab}</span><div class="track2"><div class="fill" style="width:{p}%"></div><span class="pct">{p}%</span></div></div>' for lab, p in rows)
    return f'<div class="gustobars">{inner}</div>'

def agree_wrap():
    return ('<div class="agree"><div class="w"><u>el</u> paí<u>s</u></div><div class="tie">m. · enkelvoud</div>'
            '<div class="w" style="margin-top:2mm"><u>los</u> paíse<u>s</u></div><div class="tie">m. · meervoud</div></div>'
            '<div class="agree" style="margin-top:2mm"><div class="w"><u>la</u> ciuda<u>d</u></div><div class="tie">v. · enkelvoud</div>'
            '<div class="w" style="margin-top:2mm"><u>las</u> ciudade<u>s</u></div><div class="tie">v. · meervoud</div></div>')

# ================= BODY =================
BODY = []
def P(*x): BODY.extend(x)

# ---------- OPENER ----------
P(f'''
<div class="hero">
  <div class="tab">U1 · ¿QUIÉN ERES?</div>
  <div class="eyebrow">UNIDAD 1 · LA RUTA · PARADA 1 — MADRID 🇪🇸</div>
  <h1>¿Quién eres?</h1>
  <div class="sub">Llegamos a <b>Madrid</b>. Hoy te presentas: nombre, edad, país, idiomas. <span class="gloss">We komen aan in Madrid. Vandaag stel je jezelf voor: naam, leeftijd, land, talen.</span></div>
  <div class="q">¿Cómo te llamas… y de dónde eres? <span style="font-weight:400;opacity:.9">· Hoe heet je… en waar kom je vandaan?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U0 · Mundo</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U1 · Madrid</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U2 · Sevilla</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U3 · Barcelona</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U4 · València</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U5–U8 · América</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 1 · Madrid.</b> Empieza el viaje en España. Conoces a <b>Lucía</b> y aprendes a presentarte: la base de todas las paradas siguientes. <span class="gloss">We beginnen echt: je stelt jezelf voor, en dat gebruik je de hele reis.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> En Madrid conoces a <b>Lucía</b>. Ella te pregunta: «¿Quién eres?». Aprendes a decir tu <b>nombre</b>, tu <b>edad</b>, tu <b>país</b> y los <b>idiomas</b> que hablas — y a preguntar lo mismo a los demás.
      <span class="gloss">In Madrid ontmoet je Lucía. Zij vraagt: «Wie ben jij?». Je leert je naam, leeftijd, land en talen zeggen — en hetzelfde aan anderen vragen.</span></div>
      <div class="ojo"><b>¡Ojo! — la trampa:</b> la edad va con <b>tener</b>, no con <i>ser</i>: <b>Tengo</b> 15 años (✔), no <span class="trap">Soy 15 años</span> (✘). <span class="gloss">Het Nederlands zegt «ik bén 15 jaar», het Spaans «ik héb 15 jaar».</span></div>
    </div>
    <div>
      <div class="se">La gente de la ruta</div>
      <div class="cast">
        <div class="pc"><div class="avw">{AV["lucia"]}</div><div class="nm">Lucía</div><div class="fr">Sevilla 🇪🇸</div></div>
        <div class="pc"><div class="avw">{AV["diego"]}</div><div class="nm">Diego</div><div class="fr">CDMX 🇲🇽</div></div>
        <div class="pc"><div class="avw">{AV["valen"]}</div><div class="nm">Valen</div><div class="fr">Cartagena 🇨🇴</div></div>
        <div class="pc"><div class="avw">{AV["nina"]}</div><div class="nm">Nina</div><div class="fr">Cusco 🇵🇪</div></div>
        <div class="pc tu"><div class="avw">{TU}</div><div class="nm">Tú</div><div class="fr">Flandes 🇧🇪</div></div>
      </div>
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila de palabras</span><br><span class="gloss" style="font-size:8.5pt">In Madrid vul je je rugzak met de eerste échte woorden om jezelf voor te stellen.</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">presentarte</span> (nombre, edad, país, idiomas) <span class="nl">jezelf voorstellen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">preguntar a alguien</span> quién es <span class="nl">iemand naar zijn gegevens vragen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar el verbo <b>ser</b></span> y el presente regular <span class="nl">ser + tegenwoordige tijd</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">rellenar una ficha</span> con tus datos <span class="nl">een formulier invullen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">reconocer países y nacionalidades</span> <span class="nl">landen & nationaliteiten (de kaart groeit)</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">crear tu <b>pasaporte</b></span> y presentarte <span class="nl">je paspoort maken (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>Tus datos</span><span><b>§2</b>Ser + yo/tú</span><span><b>§3</b>-ar/-er/-ir</span><span><b>§4</b>Preguntar</span><span><b>Taller</b>Mayús./conect.</span><span><b>Cultura</b>Madrid</span><span><b>Tarea</b>Mi pasaporte</span><span><b>Repaso</b>Semáforo</span>
    </div>
  </div>
  <div class="se" style="margin-top:8mm">Cómo trabajar esta unidad <span class="gloss">leeswijzer</span></div>
  <div class="fams" style="margin-top:2mm">
    <div class="pcard"><div class="t" style="font-size:10.5pt">Las etiquetas de cada actividad</div>
      <div class="ej" style="margin-top:2mm"><span class="badge skill">👂 Escuchar</span> <span class="badge skill">🎙️ Hablar</span> <span class="badge skill">🔍 Analizar</span> <span class="badge">👤 Solo</span> <span class="badge">👥 En parejas</span> <span class="badge">± 5 min</span> <span class="stars">★★☆</span></div>
      <div class="anchor" style="margin-top:2mm">Cada actividad indica la <b>destreza</b>, la <b>forma de trabajo</b>,
      el <b>tiempo</b> y la <b>dificultad</b>. <span class="gloss">vaardigheid · werkvorm · tijd · moeilijkheid</span></div></div>
    <div class="pcard"><div class="t" style="font-size:10.5pt">El apoyo baja poco a poco</div>
      <div class="ej" style="margin-top:2mm">Un ejemplo hecho → las palabras que necesitas → una frase para completar
      → solo la primera letra → nada.</div>
      <div class="anchor" style="margin-top:2mm">La ayuda baja escalón a escalón hasta que escribes tú solo/a.
      <span class="gloss">De steun bouwt af: voorbeeld → woordenbank → zin om aan te vullen → eerste letter → zonder hulp.</span></div></div>
  </div>
  <div class="fams" style="margin-top:4mm">
    <div class="pcard"><div class="t" style="font-size:10.5pt">Dos capas de color</div>
      <div class="ej" style="margin-top:2mm"><b>1 · verde</b> = el curso. <b>2 · la función</b>:
      <span class="fx per">persona</span> <span class="fx vb">verbo</span> <span class="fx ob">objeto</span>
      <span class="fx ti">tiempo</span> <span class="fx pl">lugar</span>
      <span style="color:var(--red);font-weight:700">🔴 trampa</span>.
      <span class="gloss">persoon · werkwoord · voorwerp · tijd · plaats · valstrik</span></div>
      <div class="anchor" style="margin-top:2mm">El color nunca va solo: siempre hay también una etiqueta o una forma.
      <span class="gloss">Kleur is nooit de enige drager.</span></div></div>
    <div class="pcard"><div class="t" style="font-size:10.5pt">Papel + pantalla</div>
      <div class="ej" style="margin-top:2mm">📄 el libro · 🎮 la <b>página digital</b> (20 juegos, audio, flip cards)
      · 📊 el PowerPoint. Los códigos <b>QR</b> te llevan al ejercicio online que toca.
      <span class="gloss">De QR-codes brengen je naar de juiste online-oefening.</span></div>
      <div class="anchor" style="margin-top:2mm">El libro funciona <b>sin pantalla</b>; el <b>repaso</b> completo está
      en la página digital. <span class="gloss">Print werkt volledig zonder scherm; het repaso staat online.</span></div></div>
  </div>
</div>
''')

# ---------- §0 Ponte al día ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">0</span><span class="pk">§0 · ¡Ponte al día!</span>')
P('<div class="intro"><b>ES:</b> Antes de empezar, recordamos lo que ya sabes de la Unidad 0 y que necesitas hoy: <b>saludar</b>, <b>deletrear</b> y los <b>números</b>. <span class="gloss">Voor we starten: kort ophalen — groeten, spellen en getallen.</span></div>')
P(lpd(("7","woordenschat inzetten"), ("9","strategieën / lengua de clase")))
P('</div>')
P('<p style="font-size:9.6pt">① <b>¿Qué tienes ya en la mochila?</b> '
  '<span class="gloss">wat zit er al in je rugzak?</span></p>')
P(clusters([
  ("👋","Saludar",["¡Hola! · Adiós","Buenos días","¿Qué tal? · Encantado/-a"],"Saludar y conocerse. <span class='gloss'>groeten &amp; kennismaken</span>"),
  ("🔤","Deletrear",["¿Cómo se escribe?","con/sin hache · @ (arroba)","mayúscula · minúscula"],"Deletrear tu nombre y tu correo. <span class='gloss'>naam &amp; e-mail spellen</span>"),
  ("🔢","Números 0–100",["catorce · quince · dieciséis","veintiuno · treinta","cuarenta y cinco"],"Para la edad y el teléfono. <span class='gloss'>voor leeftijd &amp; telefoon</span>"),
]))
P(actx(1, "Calentamiento: salúdate y deletrea",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Saluda con <b>¡Hola!</b>, di tu nombre y deletréalo. Tu compañero/a lo escribe. Después cambiad. '
  '<span class="gloss">Groet, zeg je naam en spel je voornaam; je buur schrijft ze op. Wissel daarna.</span></p>'
  '<p style="margin-left:12.5mm">Mi nombre: <span class="wl lg"></span> &nbsp; Mi compañero/a: <span class="wl lg"></span></p>', apoyo="Modelo"))
P(actx(2, "Los números que necesito hoy",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Lee el número en español y escribe la cifra. '
  '<span class="gloss">Lees het Spaanse getal en schrijf het cijfer.</span></p>'
  '<table class="mp"><thead><tr><th>En letras</th><th>Cifra</th><th>En letras</th><th>Cifra</th></tr></thead>'
  '<tbody><tr><td>catorce</td><td><span class="wl sm"></span></td><td>treinta</td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>dieciséis</td><td><span class="wl sm"></span></td><td>veintiuno</td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>cuarenta y cinco</td><td><span class="wl sm"></span></td><td>noventa y nueve</td><td><span class="wl sm"></span></td></tr></tbody></table>',
  apoyo="Pista: 16–29 = één woord"))
P(actx(3, "Empareja la frase de clase con su función",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Une cada frase de clase con su función: escribe la letra. '
  '<span class="gloss">Verbind de klaszin met zijn functie; schrijf de letter.</span></p>'
  '<table class="mp"><thead><tr><th>Frase</th><th></th><th>Función</th></tr></thead><tbody>'
  '<tr><td>1 · ¿Cómo se dice…?</td><td><span class="wl sm"></span></td><td>A · no lo entiendo</td></tr>'
  '<tr><td>2 · ¿Puedes repetir?</td><td><span class="wl sm"></span></td><td>B · cómo se dice</td></tr>'
  '<tr><td>3 · No entiendo.</td><td><span class="wl sm"></span></td><td>C · repite, por favor</td></tr></tbody></table>', apoyo="Banco de palabras"))
P(actx(4, "Deletrea tu correo",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Deletrea tu correo (puede ser inventado) letra por letra; tu compañero/a lo escribe. '
  'Usa <b>arroba (@)</b>, <b>punto</b> y <b>guion</b>. '
  '<span class="gloss">Spel je (verzonnen) e-mailadres letter per letter; je buur schrijft mee.</span></p>'
  '<p style="margin-left:12.5mm">El correo de mi compañero/a: <span class="wl lg"></span></p>', apoyo="Marco: arroba/punto"))
P(actx(5, "Números en contexto",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escribe el número con letras. '
  '<span class="gloss">Escribe el número con letras. <span class="gloss">Schrijf het getal voluit.</span></span></p>'
  '<p style="margin-left:12.5mm">Tengo <b>15</b> años → <span class="wl md"></span><br>Mi número es <b>0470 22 13</b> → <span class="wl full"></span></p>', apoyo="Pista: del 16 al 29 se escribe en una palabra; el teléfono se lee de dos en dos"))
P(actx(6, "Ordena el saludo",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Ordena el mini-diálogo (1–4). '
  '<span class="gloss">Zet de mini-dialoog in de juiste volgorde.</span></p>'
  '<p style="margin-left:12.5mm">___ Encantada. &nbsp; ___ ¡Hola! ¿Qué tal? &nbsp; ___ Muy bien, ¿y tú? &nbsp; ___ Bien. Me llamo Ana.</p>', apoyo="Banco de palabras"))
P('<div class="route-note">🎮 <b>Repasa jugando</b> en la página digital: números, saludos y deletreo, '
  'con corrección automática. <span class="gloss">Online herhalen met zelfcorrectie.</span></div>')
P('</div>')  # close page

# ================= §1 · TUS DATOS PERSONALES =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">1</span><span class="pk">§1 · Tus datos personales</span>')
P('<div class="route-note">📍 Parada 1 · Madrid — Lucía te pregunta quién eres.</div>')
P('<div class="intro"><b>ES:</b> Primero <b>reconoces</b> los datos en una situación, después los <b>organizas</b> y los <b>usas</b> para presentarte. <span class="gloss">Eerst herken je de gegevens in een situatie, dan orden je ze en gebruik je ze.</span></div>')
P(lpd(("7","woordenschat: datos personales"), ("2","relevante info in een ficha"), ("3","doelgericht schrijven met steun"), ("4","mondelinge interactie")))
P('</div>')
# §1.1 — situatie (gelabelde ficha) + organiseren (cluster + collocatie)
P('<h3 style="margin-top:6mm">§1.1 · La situación — la ficha de Lucía</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto.</b> Lucía llega a un intercambio y rellena su ficha. Léela y adivina las palabras <b>sin</b> mirar la traducción. <span class="gloss">Lees de fiche en raad de woorden, zónder naar de kleine vertaling te kijken.</span></p>')
P('<div class="fichacard">'
  '<div><div class="row"><span class="k">el nombre</span><span class="v">Lucía <span class="nl">voornaam</span></span></div>'
  '<div class="row"><span class="k">el apellido</span><span class="v">Ramírez García <span class="nl">achternaam (×2!)</span></span></div>'
  '<div class="row"><span class="k">la edad</span><span class="v">16 años <span class="nl">leeftijd</span></span></div>'
  '<div class="row"><span class="k">el país</span><span class="v">España <span class="nl">land</span></span></div></div>'
  '<div><div class="row"><span class="k">la nacionalidad</span><span class="v">española <span class="nl">nationaliteit</span></span></div>'
  '<div class="row"><span class="k">la ciudad</span><span class="v">Sevilla <span class="nl">stad</span></span></div>'
  '<div class="row"><span class="k">los idiomas</span><span class="v">español, inglés <span class="nl">talen</span></span></div>'
  '<div class="row"><span class="k">el correo</span><span class="v">lucia@mail.com <span class="nl">e-mail</span></span></div></div></div>')
P('<p style="font-size:9.6pt">② <b>Organiza.</b> Las mismas palabras en <b>tres grupos</b>, no en una lista. '
  '<span class="gloss">Dezelfde woorden geordend in drie clusters — zo onthoud je ze beter.</span></p>')
P(clusters([
  ("🪪","Identidad",["el nombre","el apellido","la edad"],"Quién eres. <span class='gloss'>wie je bent</span>"),
  ("🌍","Origen",["el país · la nacionalidad","la ciudad","los idiomas"],"De dónde eres. <span class='gloss'>waar je vandaan komt</span>"),
  ("✉️","Contacto",["la dirección","el correo","el teléfono"],"Cómo te encuentran. <span class='gloss'>hoe men je bereikt</span>"),
]))
P('<p style="font-size:9.6pt">③ <b>Colocaciones.</b> Cada dato viaja con su verbo. Lee las seis parejas en voz '
  'alta y subraya las dos que ya sabes usar. '
  '<span class="gloss">Elk gegeven hoort bij een vast werkwoord. Lees de zes combinaties hardop en onderstreep '
  'de twee die je al kunt gebruiken — leer ze als één geheel, niet los.</span></p>')
P(colloc("presentarse", ["me llamo + nombre","soy de + país","soy + nacionalidad",
                         "tengo + años","vivo en + ciudad","hablo + idioma"]))
P(actx(1, "Empareja el dato con el ejemplo",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Une cada dato con su ejemplo: escribe la letra. '
  '<span class="gloss">Verbind het gegeven met het juiste voorbeeld; schrijf de letter.</span></p>'
  '<table class="mp"><thead><tr><th>Dato</th><th>Letra</th><th></th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td>1 · el apellido</td><td><span class="wl sm"></span></td><td>A</td><td>16 años</td></tr>'
  '<tr><td>2 · la edad</td><td><span class="wl sm"></span></td><td>B</td><td>española</td></tr>'
  '<tr><td>3 · la nacionalidad</td><td><span class="wl sm"></span></td><td>C</td><td>García</td></tr>'
  '<tr><td>4 · el correo</td><td><span class="wl sm"></span></td><td>D</td><td>lucia@mail.com</td></tr>'
  '<tr><td>5 · la ciudad</td><td><span class="wl sm"></span></td><td>E</td><td>Sevilla</td></tr></tbody></table>', apoyo="Modelo: ficha zichtbaar"))
P(actx(2, "Clasifica en la red",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Escribe cada palabra en la columna que le toca. '
  '<span class="gloss">Escribe cada palabra en su columna. <span class="gloss">zet elk woord in de juiste kolom</span></span>'
  '<span class="words"><b>apellido · país · correo · edad · ciudad · teléfono · nacionalidad · dirección</b></span></p>'
  + sortcols([("Identidad",""),("Origen",""),("Contacto","")]), apoyo="Banco de palabras"))
P(actx(3, "El intruso",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Tacha la palabra que no encaja y escribe por qué. '
  '<span class="gloss">Streep het woord door dat er niet bij hoort en schrijf waarom.</span></p>'
  '<p style="margin-left:12.5mm">a) nombre · apellido · español · edad → <span class="wl md"></span><br>'
  'b) España · México · Sevilla · Perú → <span class="wl md"></span><br>'
  'c) correo · teléfono · dirección · idioma → <span class="wl md"></span></p>', apoyo="Pista: pregúntate: ¿es un dato de identidad, de origen o de contacto?"))
P('</div>')  # page §1.1a

# §1.1b — afbouwen tot productie + Mis palabras
P('<div class="page">')
P(actx(4, "Completa las palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Completa las letras que faltan. Son cinco palabras. '
  '<span class="gloss">Vul de ontbrekende letters aan — vijf woorden.</span></p>'
  '<p style="margin-left:12.5mm">na__ona__dad · ap__l__do · di__ec__ión · i__ioma · c__rr__o<br><span class="wl full"></span></p>', apoyo="Pista: aantal letters"))
P(actx(5, "Rellena tu ficha",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p>Rellena tu propia ficha: datos reales o inventados. La vas a usar en la tarea final. '
  '<span class="gloss">Vul je eigen fiche in, echt of verzonnen; je gebruikt ze bij de eindtaak.</span></p>'
  '<div class="fichacard"><div>'
  '<div class="row"><span class="k">Nombre</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Apellido</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Edad</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">País</span><span class="v"><span class="wl md"></span></span></div></div><div>'
  '<div class="row"><span class="k">Nacionalidad</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Ciudad</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Idiomas</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Correo</span><span class="v"><span class="wl md"></span></span></div></div></div>', apoyo="Marco: labels gegeven"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha a cuatro personas y anota el dato que falta.</b> <span class="gloss">Luister naar vier personen en noteer telkens het gegeven dat ontbreekt.</span></div>',
           qr("Escanea y escucha", "Audio 1.1 · Datos · 0:55", seed=11)))
P(mispal("Mis palabras de la ficha", 3))
P('</div>')  # page §1.1b

# ---- §1.2 presentarse (bouwstroken → röntgen → steiger → comunicar) ----
P('<div class="page">')
P('<div class="divider">Presentarse · §1.2</div>')
P('<h3>§1.2 · Presentarse — observa el patrón</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto.</b> Lucía te escribe por chat. Observa cómo se presenta ella y cómo respondes tú. <span class="gloss">Kijk hoe zij zich voorstelt en hoe jij antwoordt; elke kleur is een taalfunctie.</span></p>')
P('<div class="chat">'
  '<div class="chatline you"><div class="bub">¡Hola! ¿Quién eres?</div><div class="who">Lucía</div></div>'
  '<div class="chatline me"><div class="bub"><span class="fx per">Yo</span> <span class="fx vb">me llamo</span> Leo. <span class="fx vb">Soy</span> <span class="fx pl">de Bélgica</span> y <span class="fx vb">tengo</span> <span class="fx ti">15 años</span>.</div><div class="who">Tú</div></div>'
  '<div class="chatline you"><div class="bub">¿Y dónde vives?</div><div class="who">Lucía</div></div>'
  '<div class="chatline me"><div class="bub"><span class="fx vb">Vivo</span> <span class="fx pl">en Gante</span> y <span class="fx vb">hablo</span> neerlandés y español.</div><div class="who">Tú</div></div></div>')
P('<p style="font-size:9.6pt">② <b>El patrón como bloques.</b> Cada frase se monta con tres bloques: '
  '<b>persona + verbo + dato</b>. Completa el tercer bloque de las cuatro filas con <b>tus</b> datos y '
  'lee las cuatro frases en voz alta. '
  '<span class="gloss">Elke zin bestaat uit drie blokken: persoon + werkwoord + gegeven. Vul in de vier rijen '
  'het derde blok in met jouw gegevens en lees de vier zinnen hardop.</span></p>')
P(blocks([
  [("per","Yo"),("vb","me llamo"),("ob","… (nombre)")],
  [("per","Yo"),("vb","soy de"),("pl","… (país)")],
  [("per","Yo"),("vb","tengo"),("ti","… años")],
  [("per","Yo"),("vb","vivo en"),("pl","… (ciudad)")],
]))
P('<p style="font-size:9.6pt">③ <b>Por dentro de la frase.</b> Mira la frase de abajo: debajo de cada parte '
  'está escrito qué hace. Después señala esas mismas partes en <b>tu</b> frase del bloque ②. '
  '<span class="gloss">Onder elk stuk van de zin staat wat het doet. Duid daarna dezelfde stukken aan in '
  'jouw eigen zin uit blok ②.</span></p>')
P(xray('<span class="fx per">Yo</span> <span class="fx vb">soy</span> <span class="fx pl">de Bélgica</span> y <span class="fx vb">tengo</span> <span class="fx ti">15 años</span>.',
       [("Yo","la persona"),("soy","el verbo ser"),("de Bélgica","el origen"),
        ("tengo","el verbo tener"),("15 años","la edad")]))
P(regla("Regla · presentarse",
  '<p><b>Me llamo</b> + nombre · <b>Soy de</b> + país · <b>Soy</b> + nacionalidad · <b>Tengo</b> + número + '
  '<b>años</b> · <b>Vivo en</b> + ciudad · <b>Hablo</b> + idioma. '
  '<span class="gloss">naam · land · nationaliteit · leeftijd · stad · taal</span>'
  '<br>🔴 <b>La edad va con tener</b>: <i>Tengo 15 años</i>, no <span class="trap">soy 15</span>. '
  '🔴 <b>La nacionalidad va en minúscula</b>: <i>belga, español</i>. '
  '<span class="gloss">Leeftijd met tener, nationaliteit met kleine letter.</span></p>'))
P('</div>')  # page §1.2a

# §1.2b — scaffold + oefeningen + tarea
P('<div class="page">')
P('<p style="font-size:9.6pt">④ <b>De la copia a lo tuyo.</b> Cuatro escalones: el primero te lo damos hecho, '
  'en el último escribes tú solo/a. Haz los cuatro. '
  '<span class="gloss">Vier trapjes: bovenaan krijg je alles, onderaan schrijf je het zelf. Doe ze alle vier.</span></p>')
P(scaffold([
  ("Modelo","«Me llamo Leo, soy de Bélgica y tengo 15 años.»"),
  ("Marco","«Me llamo ___, soy de ___ y tengo ___ años.»"),
  ("Clave","yo · llamarse · país · años"),
  ("Solo","Escribe quién eres, sin ayuda."),
]))
P(actx(6, "Construye con la tabla de sustitución",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Combina una palabra de cada columna y escribe tres frases correctas. '
  '<span class="gloss">Combineer per zin één stuk uit elke kolom; schrijf drie correcte zinnen.</span></p>'
  '<table class="mp"><thead><tr><th>Persona</th><th>Verbo</th><th>Dato</th></tr></thead><tbody>'
  '<tr><td>(Yo)</td><td>me llamo / soy de / vivo en / tengo / hablo</td><td>Leo · Bélgica · Gante · 15 años · español</td></tr></tbody></table>'
  '<p style="margin-left:12.5mm">1) <span class="wl full"></span>2) <span class="wl full"></span>3) <span class="wl full"></span></p>', apoyo="Marco: (Yo) + verbo + dato: «Yo vivo en Gante.»"))
P(actx(7, "Cue → frase completa",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Escribe una frase completa con cada grupo de palabras. Son cuatro frases. '
  '<span class="gloss">Maak van elk groepje één volledige zin — vier zinnen.</span></p>'
  '<table class="mp"><thead><tr><th>Cue</th><th>Frase</th></tr></thead><tbody>'
  '<tr><td>yo / llamarse / Sara</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>yo / ser de / México</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>yo / tener / 14 años</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>yo / vivir en / Madrid</td><td><span class="wl lg"></span></td></tr></tbody></table>', apoyo="Pista: werkwoord gegeven"))
P(actx(8, "Preséntate en cinco frases",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 7 min"},{"t":"★★★"}],
  '<p>Escribe cinco frases verdaderas sobre ti y dilas en voz alta. '
  '<span class="gloss">Schrijf vijf ware zinnen over jezelf en zeg ze hardop.</span></p>'
  '<div class="wbox"></div>', apoyo="ronde 2 uit het hoofd"))
P(tarea_com("Tarea comunicativa · «¿Quién de la clase…?»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 Toda la clase"},{"t":"± 10 min"},{"t":"★★★"}],
  '<p><b>Situación:</b> pregunta por la clase hasta encontrar a alguien para cada línea de la tabla. Apunta su nombre y escribe la nota en <b>tercera persona</b>: «Ana tiene 15 años». <span class="gloss">Vraag rond in de klas tot je voor elke regel iemand vindt; noteer de naam en schrijf de notitie in de derde persoon.</span></p>'
  '<table class="wtab mp"><thead><tr><th>¿Quién de la clase…?</th><th>Nombre</th><th>Nota (3ª pers.)</th></tr></thead><tbody>'
  '<tr><td>…tiene 15 años</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>…vive en una ciudad grande</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>…habla más de dos idiomas</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>'
  '<p style="margin-left:12.5mm">Resultado (rapport): <span class="wl full"></span></p>'
  ''))
P('<div class="route-note">🎮 <b>Juega online:</b> «Memoria de los datos», «país ↔ nacionalidad» y «¡Preséntate!», '
  'con corrección automática. <span class="gloss">Online spelletjes met zelfcorrectie.</span></div>')
P('</div>')  # page §1.2b

# ================= §2 · EL VERBO SER =================
retos("datos", "§1.3 · Retos — tus datos, de verdad",
      'Tres juegos con tus datos. En cada uno tienes <b>una tarea concreta</b>: presentarte como otra '
      'persona, contar a toda la clase en números, o escribir un perfil sin nombre. Cada reto explica '
      'debajo qué haces paso a paso y qué regla no puedes romper.',
      'Drie spellen met je gegevens. Elk reto zegt hieronder stap voor stap wat je doet en welke regel je '
      'niet mag breken.')
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2 · El verbo SER + los pronombres</span>')
P('<div class="intro"><b>ES:</b> Para decir <b>quién eres</b> y <b>de dónde eres</b> usas el verbo <b>ser</b>. <span class="gloss">Om te zeggen wie je bent en waar je vandaan komt, gebruik je «ser».</span></div>')
P(lpd(("8","taalsysteem: ser + pronombres"), ("3","zich voorstellen"), ("4","interactie")))
P('</div>')
# §2.1 observar
P('<h3 style="margin-top:6mm">§2.1 · Observa el verbo SER</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto.</b> Lee el chat y fíjate en la forma de <i>ser</i>. '
  '<span class="gloss">Lees de chat en let op de vorm van «ser».</span></p>')
P(obsbox([
  '<span class="fx per">Yo</span> <span class="hl">soy</span> Lucía. ¿<span class="fx per">Tú</span> <span class="hl">eres</span> de Bélgica?',
  '<span class="fx per">Diego</span> <span class="hl">es</span> de México. <span class="fx per">Nosotros</span> <span class="hl">somos</span> de Flandes.',
  '¿<span class="fx per">Vosotros</span> <span class="hl">sois</span> estudiantes? Ellas <span class="hl">son</span> profesoras.',
], vragen='<b>1)</b> ¿Qué verbo se repite? <b>2)</b> ¿Cambia la forma según la persona? '
             '<b>3)</b> ¿Qué forma va con <i>yo</i>? '
             '<span class="gloss">Welk werkwoord keert terug? Verandert de vorm per persoon? '
             'Welke vorm hoort bij yo?</span>'))
P('<p style="font-size:9.6pt">② <b>El patrón — persona ↔ forma.</b></p>')
P('<table class="conj"><thead><tr><th>Persona</th><th>ser</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">soy</td><td>Soy Leo, soy belga.</td></tr>'
  '<tr><td class="p">tú</td><td class="v">eres</td><td>¿De dónde eres?</td></tr>'
  '<tr><td class="p">él / ella / usted</td><td class="v">es</td><td>Lucía es española.</td></tr>'
  '<tr><td class="p">nosotros/-as</td><td class="v">somos</td><td>Somos de Bélgica.</td></tr>'
  '<tr><td class="p">vosotros/-as</td><td class="v">sois</td><td>¿Sois estudiantes?</td></tr>'
  '<tr><td class="p">ellos/-as / ustedes</td><td class="v">son</td><td>Son de México.</td></tr></tbody></table>')
P('<p style="font-size:9.6pt">③ <b>Forma · significado · uso.</b></p>')
P(fmu('<b>soy · eres · es<br>somos · sois · son</b><br>'
      '<span class="gloss">onregelmatig: elke persoon heeft een eigen vorm</span>',
      'decir <b>quién</b> es alguien, <b>de dónde</b> es, su <b>nacionalidad</b> o cómo <b>es</b> '
      '<span class="gloss">zeggen wie iemand is, waar hij vandaan komt, welke nationaliteit hij heeft '
      'of hoe hij is</span>',
      '<i>Soy Leo. · Soy de Bélgica. · Soy belga. · Lucía es simpática.</i>'))
P('<div class="truc"><b>🟡 Ojo · tú o usted.</b> Con alguien de tu edad: <b>tú eres</b>. '
  'Con una persona adulta que no conoces: <b>usted es</b> (¡tercera persona!). En España se usa mucho '
  '<i>tú</i>; en partes de Latinoamérica, <i>usted</i>. El pronombre puede desaparecer: <i>(Yo) soy Leo</i>. '
  '<span class="gloss">Leeftijdsgenoot: tú eres. Onbekende volwassene: usted es (derde persoon!). '
  'Het onderwerpwoord mag weg.</span></div>')
P('</div>')  # page §2.1
# §2.1 práctica
P('<div class="page">')
P('<div class="divider">Practicar SER · §2.1</div>')
P(actx(1, "Elige la forma de ser",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Escribe la forma correcta de <b>ser</b>. '
  '<span class="gloss">Vul de juiste vorm van «ser» in.</span></p>'
  '<p style="margin-left:12.5mm">a) Yo <span class="wl sm"></span> de Gante. &nbsp; b) ¿Tú <span class="wl sm"></span> español? &nbsp; c) Lucía <span class="wl sm"></span> de Sevilla.<br>'
  'd) Nosotros <span class="wl sm"></span> belgas. &nbsp; e) Diego y Nina <span class="wl sm"></span> de América. &nbsp; f) ¿Vosotros <span class="wl sm"></span> amigos?</p>', apoyo="Banco de palabras: tabel open"))
P(actx(2, "Una cosa cambia",
  [{"t":"🔍 Analizar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Parte de <b>«Yo soy de Bélgica.»</b> y cambia <b>una sola cosa</b> cada vez. Escribe la frase entera. '
  '<span class="gloss">Vertrek van die zin en verander telkens één ding; schrijf de hele zin.</span></p>'
  '<p style="margin-left:12.5mm">→ maak <b>tú</b>: <span class="wl lg"></span><br>→ maak <b>nosotros</b>: <span class="wl lg"></span><br>→ maak <b>ella</b> + España: <span class="wl lg"></span></p>', apoyo="Pista: cambia el pronombre y el verbo; el resto de la frase se queda igual"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha seis frases con «ser» y marca la persona.</b> <span class="gloss">Luister naar zes zinnen met «ser» en kruis per zin aan over wie het gaat.</span></div>',
           qr("Escanea y escucha", "Audio 2.1 · Ser · 0:45", seed=21)))
P(actx(3, "Escucha y marca la persona",
  [{"t":"👂 Escuchar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Marca con una cruz la persona que oyes. '
  '<span class="gloss">Kruis aan welke persoon je hoort.</span></p>'
  '<table class="mp"><thead><tr><th>#</th><th>yo</th><th>tú</th><th>él/ella</th><th>nosotros</th><th>ellos</th></tr></thead><tbody>'
  '<tr><td>1</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>2</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>3</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>4</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>5</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>6</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="Modelo: tabel ser open"))
P(actx(4, "Clínica de errores",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Busca el error, escribe la frase correcta y explica <b>por qué</b>. '
  '<span class="gloss">Zoek de fout, verbeter de zin en leg uit waarom.</span></p>'
  '<p style="margin-left:12.5mm">1) <span class="trap">Soy 15 años.</span> → <span class="wl lg"></span><br>'
  '2) <span class="trap">Yo es de Bélgica.</span> → <span class="wl lg"></span><br>'
  '3) <span class="trap">Nosotros somos Español.</span> → <span class="wl lg"></span></p>', apoyo="MODELO-correctie"))
P(tarea_com("Tarea comunicativa · Entrevista con marco",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p>Entrevista a tu compañero/a con <b>ser</b>: nombre, origen y nacionalidad. Después preséntalo/la '
  'a la clase en <b>tercera persona</b>: «Ella es Sara, es de Amberes, es belga.» '
  '<span class="gloss">Interview je buur met «ser» en stel die persoon daarna voor in de derde persoon.</span></p>'
  '<p style="margin-left:12.5mm">Mi compañero/a: <span class="wl full"></span></p>'
  + APO.html("Marco: ¿Cómo…? ¿De dónde…?")))
P(actx(5, "Preséntate con SER",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
'<p>Escribe tres frases verdaderas sobre ti con <b>ser</b>: quién eres, de dónde eres y tu nacionalidad. <span class="gloss">Drie ware zinnen over jezelf met «ser»: identiteit, afkomst, nationaliteit.</span></p>'
  '<p style="margin-left:12.5mm"><span class="wl full"></span><span class="wl full"></span><span class="wl full"></span></p>', apoyo="Marco: Soy… · Soy de… · Soy…"))
P('<div class="route-note">🎮 <b>Juega online:</b> «El verbo SER» (welke persoon?) en «Presente Tetris».</div>')
P('</div>')  # page §2.1 práctica

# ================= §3 · EL PRESENTE REGULAR =================
retos("ser", "§2.3 · Retos — ser bajo presión",
      'Dos juegos con el verbo <b>ser</b>. En el primero buscas, preguntando, al pasajero que tiene tus '
      'mismos datos. En el segundo cazas los errores de otro equipo, pero una acusación falsa te cuesta '
      'una vida. Los pasos están debajo de cada reto.',
      'Twee spellen met «ser»: in het eerste zoek je al vragend de passagier met jouw gegevens, in het '
      'tweede jaag je op de fouten van een ander team — maar een valse beschuldiging kost je een leven. '
      'De stappen staan onder elk reto.')
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3 · El presente regular (-ar · -er · -ir)</span>')
P('<div class="intro"><b>ES:</b> Casi todos los verbos siguen un <b>patrón</b>. Descúbrelo como una <b>máquina</b>: quita la terminación del infinitivo y añade la nueva. <span class="gloss">Ontdek het patroon als een machine.</span></div>')
P(lpd(("8","taalsysteem: presente regular"), ("3","vertellen over jezelf")))
P('</div>')
# §3.1 machine + bloques
P('<h3 style="margin-top:6mm">§3.1 · La máquina del verbo</h3>')
P('<p style="font-size:9.6pt">① <b>Observa la máquina.</b> Zo bouw je een werkwoordsvorm:</p>')
P(machine([("infinitivo","hablar"),("raíz","habl-"),("+ terminación",'<span class="end">-o</span>'),("forma","habl<span class=end>o</span>")]))
P('<p style="font-size:9.6pt">② <b>Las tres familias — la terminación cambia por persona (oranje).</b></p>')
P('<div class="fams three" style="margin-top:2mm">')
for inf, ends in [("hablar (-ar)", ["o","as","a","amos","áis","an"]),
                  ("aprender (-er)", ["o","es","e","emos","éis","en"]),
                  ("vivir (-ir)", ["o","es","e","imos","ís","en"])]:
    stem = inf.split()[0][:-2]
    rows = "".join(f'<tr><td class="p">{p}</td><td>{stem}<span class="end">{e}</span></td></tr>'
                   for p, e in zip(["yo","tú","él/ella","nosotros","vosotros","ellos"], ends))
    P(pcard(inf, f'<table class="conj"><tbody>{rows}</tbody></table>'))
P('</div>')
P('<p style="font-size:9.6pt">③ <b>Como bloques.</b> Vervang blokken en bouw nieuwe zinnen:</p>')
P(blocks([
  [("per","Yo"),("vb","hablo"),("ob","español"),("pl","en casa")],
  [("per","Mi amiga"),("vb","estudia"),("ob","inglés"),("pl","en el instituto")],
  [("per","Nosotros"),("vb","vivimos"),("pl","en Gante"),("ti","ahora")],
]))
P(regla("Regla · presente regular",
  '<p><b>-er</b> en <b>-ir</b> zijn bijna gelijk — alleen bij <b>nosotros/vosotros</b> verschillen ze (-emos/-éis vs. -imos/-ís). De <b>yo</b>-vorm eindigt altijd op <b>-o</b>. 🟡 Ken je de yo-vorm, dan ken je het patroon.</p>'))
P('</div>')  # page §3.1
# §3.2 práctica
P('<div class="page">')
P('<div class="divider">Usar el presente · §3.2</div>')
P(actx(1, "Ordena por familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Clasifica los infinitivos según su terminación: -ar, -er o -ir. '
  '<span class="gloss">Sorteer de infinitieven volgens hun uitgang.</span>'
  '<span class="words"><b>hablar · comer · vivir · estudiar · aprender · escribir · trabajar · beber · abrir</b></span></p>'
  + sortcols([("-ar",""),("-er",""),("-ir","")]), apoyo="Banco de palabras"))
P(actx(2, "Conjuga en presente",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
'<p>Conjuga los cuatro verbos en presente para <i>yo</i>, <i>tú</i> y <i>nosotros</i>. <span class="gloss">Vervoeg de vier werkwoorden in de tegenwoordige tijd voor yo, tú en nosotros.</span></p>'
  '<table class="mp"><thead><tr><th>Infinitivo</th><th>yo</th><th>tú</th><th>nosotros</th></tr></thead><tbody>'
  '<tr><td>hablar</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>aprender</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>vivir</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>estudiar</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>', apoyo="Modelo"))
P(actx(3, "Completa con la forma correcta",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★☆"}],
'<p>Escribe la <b>forma correcta</b> del verbo. El infinitivo está entre paréntesis. <span class="gloss">Vul de juiste werkwoordsvorm in; het infinitief staat tussen haakjes.</span></p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl md"></span> <i>(ser)</i> de Bélgica y <span class="wl md"></span> <i>(hablar)</i> neerlandés.<br>'
  '2. Lucía <span class="wl md"></span> <i>(ser)</i> española y <span class="wl md"></span> <i>(vivir)</i> en Sevilla.<br>'
  '3. ¿Tú <span class="wl md"></span> <i>(estudiar)</i> español? — Sí, <span class="wl md"></span> <i>(aprender)</i> mucho.<br>'
  '4. Nosotros <span class="wl md"></span> <i>(ser)</i> estudiantes y <span class="wl md"></span> <i>(trabajar)</i> los sábados.<br>'
  '5. Diego y Nina <span class="wl md"></span> <i>(vivir)</i> en América y <span class="wl md"></span> <i>(hablar)</i> español.<br>'
  '6. ¿Vosotros <span class="wl md"></span> <i>(ser)</i> de Madrid? — No, <span class="wl md"></span> <i>(ser)</i> de Barcelona.</p>'
  '<p style="margin-left:12.5mm" class="gloss">✅ De oplossingen staan online (zelfcorrectie op de digitale pagina).</p>', apoyo="Pista: infinitief gegeven"))
P(actx(4, "Cadena de transformación",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Parte de <b>«Yo hablo español.»</b> y haz cada cambio, escribiendo la frase entera. <span class="gloss">Vertrek van die zin, voer elke opdracht uit en schrijf telkens de hele zin.</span></p>'
  '<p style="margin-left:12.5mm">→ maak <b>ontkennend</b>: <span class="wl lg"></span><br>→ maak er een <b>vraag</b> van: <span class="wl lg"></span><br>→ verander onderwerp naar <b>nosotros</b>: <span class="wl lg"></span><br>→ voeg <b>«en el instituto»</b> toe: <span class="wl lg"></span></p>', apoyo="Pista: cada paso cambia o añade una sola parte de la frase"))
P(actx(5, "Amplía la frase",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Start met <b>«Estudio.»</b> en voeg stap voor stap toe: <span class="gloss">wat · waar · wanneer · waarom.</span></p>'
  '<div class="wbox sm"></div>', apoyo="Marco: wat/waar/wanneer/waarom"))
P(audiorow('<div class="ic">🎧</div><div><b>Microdictado.</b> Escucha dos veces y escribe. <span class="gloss">1ª: betekenis · 2ª: schrijf de zinnen.</span></div>',
           qr("Escanea y escucha", "Audio 3.2 · Microdictado · 0:40", seed=31)))
P(actx(6, "Microdictado con reconstrucción",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★★"}],
'<p>Reconstruye las tres frases que oyes y escribe después una variante <b>tuya</b>. <span class="gloss">Reconstrueer de drie zinnen die je hoort en maak daarna één eigen variant.</span></p>'
  '<p style="margin-left:12.5mm">1) <span class="wl full"></span>2) <span class="wl full"></span>3) <span class="wl full"></span></p>'
  '<p style="margin-left:12.5mm">Mi variante: <span class="wl full"></span></p>', apoyo="eerste letter"))
P(tarea_com("Tarea comunicativa · 4/3/2 «Un día en mi vida»",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p>Vertel in <b>4/3/2</b>-ronden (telkens sneller, andere partner) drie dingen die je doet, met <b>hablar · estudiar · vivir</b>.</p>'
  '<p style="margin-left:12.5mm">Mis notas: <span class="wl full"></span> ☐ 4 min ☐ 3 min ☐ 2 min</p>'
  '<div class="steun" style="margin-left:12.5mm">notas</div>'))
P(actx(7, "Habla de tres personas",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
'<p>Escribe una frase en presente por cada persona (hablar · estudiar · vivir · trabajar). <span class="gloss">Schrijf per persoon één zin in de tegenwoordige tijd.</span></p>'
  '<table class="mp"><thead><tr><th>Persona</th><th>Frase</th></tr></thead><tbody>'
  '<tr><td>yo</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>mi amigo/a</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>mis padres</td><td><span class="wl lg"></span></td></tr></tbody></table>', apoyo="Pista: la persona te dice la terminación: -o · -as · -a · -amos"))
P('<div class="route-note">🔁 <b>Ojo — el conjugador.</b> Todas las conjugaciones (unos 1000 verbos) están '
  'en la herramienta «Conjugador» de la página digital. '
  '<span class="gloss">Alle vervoegingen staan in de aparte cursus-tool «Conjugador».</span></div>')
P('</div>')  # page §3.2

# ================= §4 · PREGUNTAR + GÉNERO =================
retos("presente", "§3.3 · Reto — el presente en la calle",
      'Comparas dos fotos de la misma plaza de Madrid, con cuarenta años de diferencia, y escribes cinco '
      'frases en <b>presente</b> sobre lo que ves. Los pasos y la regla están debajo.',
      'Je vergelijkt twee foto\'s van hetzelfde plein in Madrid, veertig jaar uit elkaar, en schrijft er vijf '
      'zinnen over in het presente. De stappen en de regel staan eronder.')
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4 · Preguntar: interrogativos + el/la</span>')
P('<div class="intro"><b>ES:</b> Ya sabes presentarte; ahora aprende a <b>preguntar</b> — y a poner el <b>artículo</b> correcto. <span class="gloss">Nu leer je vragen stellen en het juiste lidwoord kiezen.</span></div>')
P(lpd(("8","taalsysteem: interrogativos, género/número, artículos"), ("4","mondelinge interactie")))
P('</div>')
# §4.1 interrogativos via vraag-spiegel
P('<h3 style="margin-top:6mm">§4.1 · Preguntar — la pregunta es un espejo</h3>')
P('<p style="font-size:9.6pt">① <b>Observa (espejo).</b> Het vraagwoord «zoekt» een soort antwoord; dat antwoord spiegelt de vraag:</p>')
P(mirror([
  ('¿<span class="mk">Cómo</span> te llamas?', 'Me llamo Leo. <span class="gloss">(nombre)</span>'),
  ('¿De <span class="mk">dónde</span> eres?', 'Soy de Bélgica. <span class="gloss">(origen)</span>'),
  ('¿<span class="mk">Cuántos años</span> tienes?', 'Tengo 15 años. <span class="gloss">(edad)</span>'),
]))
P('<table class="mp"><thead><tr><th>Pregunta</th><th>Busca…</th><th>Respuesta modelo</th></tr></thead><tbody>'
  '<tr><td><b>¿Cómo</b> te llamas?</td><td>de naam</td><td>Me llamo Leo.</td></tr>'
  '<tr><td><b>¿De dónde</b> eres?</td><td>de afkomst</td><td>Soy de Bélgica.</td></tr>'
  '<tr><td><b>¿Dónde</b> vives?</td><td>de woonplaats</td><td>Vivo en Gante.</td></tr>'
  '<tr><td><b>¿Cuántos años</b> tienes?</td><td>de leeftijd</td><td>Tengo 15 años.</td></tr>'
  '<tr><td><b>¿Cuál</b> es tu correo?</td><td>een gegeven</td><td>Es leo@mail.com.</td></tr>'
  '<tr><td><b>¿Qué</b> idiomas hablas?</td><td>info (open)</td><td>Hablo dos idiomas.</td></tr>'
  '<tr><td><b>¿Quién</b> es ella?</td><td>een persoon</td><td>Es Lucía.</td></tr></tbody></table>')
P('<div class="truc"><b>🔴 ¿Cuál? frente a ¿Qué?</b> Delante de <i>ser</i> + un dato eliges <b>¿Cuál?</b>: <i>¿<b>Cuál</b> es tu nombre?</i>, no <span class="trap">¿Qué es tu nombre?</span>. Las palabras interrogativas llevan <b>tilde</b>. <span class="gloss">Vóór ser + gegeven kies je ¿Cuál?; vraagwoorden dragen een accent.</span></div>')
P(actx(1, "Haz la pregunta",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>¿Qué pregunta va con esta respuesta? <span class="gloss">welke vraag past bij dit antwoord?</span></p>'
  '<table class="mp"><thead><tr><th>Respuesta</th><th>Tu pregunta</th></tr></thead><tbody>'
  '<tr><td>Soy de Colombia.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Tengo 14 años.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Me llamo Nina.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Es nina@mail.com.</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="Pista: mira la respuesta: lo que no sabes es lo que preguntas"))
P(actx(2, "Entrevista relámpago",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★☆"}],
'<p>Hazle a tu compañero/a las cuatro preguntas y anota su respuesta en pocas palabras. Después cambiad. <span class="gloss">Stel je buur de vier vragen, noteer kort en wissel daarna van rol.</span></p>'
  '<table class="wtab mp"><thead><tr><th>¿Cómo?</th><th>¿De dónde?</th><th>¿Cuántos años?</th><th>¿Qué idiomas?</th></tr></thead><tbody>'
  '<tr><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>', apoyo="Marco: ¿Cómo te llamas? · ¿De dónde eres? · ¿Cuántos años tienes? · ¿Qué idiomas hablas?"))
P('</div>')  # page §4.1
# §4.2 género via agreement + tree + zoom
P('<div class="page">')
P('<div class="divider">Género y artículos · §4.2</div>')
P('<h3>§4.2 · el / la / un / una</h3>')
P('<p style="font-size:9.6pt">① <b>Observa (concordancia).</b> Het lidwoord «trouwt» met het woord — zelfde geslacht en getal:</p>')
P('<div class="fams" style="margin-top:2mm"><div class="pcard"><div class="t" style="font-size:10pt">enkelvoud → meervoud</div>'
  + agree_wrap()
  + '</div><div class="pcard"><div class="t" style="font-size:10pt">bepaald ↔ onbepaald (zoom)</div>'
  + zoom("eerste keer / onbekend","un país · una ciudad","specifiek / bekend","el país · la ciudad")
  + '</div></div>')
P('<p style="font-size:9.6pt">② <b>Beslisboom — ¿el o la?</b></p>')
P('<div class="fams" style="margin-top:2mm"><div class="pcard">' + tree([
  'Eindigt het op <b>-a, -ción, -dad, -tad</b>? <span class="yes">JA →</span> meestal <span class="res">la</span>',
  'Eindigt het op <b>-o</b> of iets anders? <span class="yes">JA →</span> meestal <span class="res">el</span>',
  '🔴 <span class="no">Uitzondering:</span> <b>el</b> idioma, <b>el</b> día, <b>el</b> mapa, <b>el</b> problema · <b>la</b> mano',
], None) + '</div>'
  '<div class="pcard"><div class="t" style="font-size:10pt">Onthoud</div><div class="ej">bepaald: <b>el/la · los/las</b><br>onbepaald: <b>un/una</b><br>🟡 leer elk woord <b>mét</b> lidwoord</div></div></div>')
P(actx(3, "Clasifica el/la",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Escribe cada palabra en su columna: <b>el</b> o <b>la</b>. '
  '<span class="gloss">Escribe cada palabra en su columna. <span class="gloss">zet elk woord in de juiste kolom</span></span>'
  '<span class="words"><b>ciudad · país · idioma · edad · correo · dirección · día · mano · nombre</b></span></p>'
  + sortcols([("el (m.)","-o, valstrik -a"),("la (f.)","-a, -ción, -dad")]), apoyo="Pista: valstrikken gemarkeerd"))
P(actx(4, "Concordancia — singular ↔ plural",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
'<p>Pon en plural: artículo + palabra. <span class="gloss">Zet in het meervoud: lidwoord + woord.</span></p>'
  '<p style="margin-left:12.5mm">el país → <span class="wl md"></span> &nbsp; la ciudad → <span class="wl md"></span> &nbsp; el idioma → <span class="wl md"></span> &nbsp; la nacionalidad → <span class="wl md"></span></p>', apoyo="Modelo: los/las"))
P(tarea_com("Tarea comunicativa · Tarjetas de rol",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 10 min"},{"t":"★★★"}],
  '<p>Krijg een <b>nieuwe identiteit</b> (naam, land, leeftijd) en stel elkaar vragen om die te achterhalen. Presenteer je partner daarna.</p>'
  '<div class="fams" style="margin-top:2mm"><div class="pcard"><div class="t" style="font-size:10pt">Mi tarjeta</div><div class="ej">Nombre: <span class="wl sm"></span><br>País: <span class="wl sm"></span> · Edad: <span class="wl sm"></span></div></div>'
  '<div class="pcard"><div class="t" style="font-size:10pt">Mi compañero/a (notas)</div><div class="ej"><span class="wl full"></span></div></div></div>'
  ''))
P(actx(5, "Un/una — artículo indefinido",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escribe <b>un</b> o <b>una</b>: es la primera vez que se nombra la cosa. <span class="gloss">Vul un of una in — het gaat om iets dat voor het eerst genoemd wordt.</span></p>'
  '<p style="margin-left:12.5mm">___ ciudad · ___ país · ___ idioma · ___ dirección · ___ nombre · ___ nacionalidad<br><span class="wl full"></span></p>', apoyo="Pista: un + palabra masculina · una + palabra femenina"))
P('<div class="route-note">🎮 <b>Juega online:</b> «Palabras interrogativas», «Pregunta ↔ respuesta» y «El o la». '
  '<span class="gloss">Online spelletjes bij deze sectie.</span></div>')
P('</div>')  # page §4.2

# ================= §5 · LECTURA (leesvaardigheid) =================
retos("preguntar", "§4.3 · Retos — preguntar de otra manera",
      'Tres juegos para preguntar mejor: en una <b>rueda de prensa</b> cada periodista hace una pregunta '
      'distinta; en el segundo consigues la misma información con tres preguntas <b>prohibidas</b>; en el '
      'tercero decides el artículo (<b>el</b> o <b>la</b>) de doce objetos inventados y dices qué regla usas.',
      'Drie spellen om beter te leren vragen: een persconferentie, dezelfde informatie halen zonder drie '
      'verboden vragen, en het juiste lidwoord kiezen bij twaalf verzonnen voorwerpen — met de regel erbij.')
P('<div class="page"><div class="parada sec">')
P('<span class="num">📖</span><span class="pk">§5 · Lectura 1 — «Dos perfiles»</span>')
P('<div class="intro"><b>ES:</b> Vas a leer dos perfiles de una app de intercambio. Primero <b>predices</b>, después lees con un <b>objetivo</b>. <span class="gloss">Je leest twee profielen van een uitwisselings-app: eerst voorspellen, dan lezen met een doel.</span></div>')
P(lpd(("1","onderwerp/hoofdgedachte bij lezen"), ("2","relevante info selecteren"), ("3","doelgericht schrijven met steun")))
P('</div>')
# ① visuele tekstintroductie + voorspellen
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> perfil (app)</span><span class="tm"><b>De:</b> Lucía · Diego</span><span class="tm"><b>Para:</b> un intercambio</span><span class="tm">🎯 conocer a alguien nuevo</span></div>')
P(actx(1, "Antes de leer: predice",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★☆☆"}],
  '<p>Mira solo las fotos y la forma del texto. Escribe tres datos que esperas encontrar. '
  '<span class="gloss">Bekijk alleen de foto\'s en de vorm; noteer drie gegevens die je verwacht.</span></p>'
  '<p style="margin-left:12.5mm">Espero encontrar: <span class="wl full"></span></p>', apoyo="Modelo: nombre, país, edad…"))
# de teksten (parallelle perfiles) — de bewijszinnen staan gemarkeerd
P('<div class="ptexts">'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["lucia"]}</div><div><div class="nm">Lucía</div><div class="fr">app · perfil</div></div></div>'
  '<p>¡Hola! Me llamo <span class="evi">Lucía Ramírez</span>. Soy de <span class="evi">Sevilla</span>, en el sur de España, y tengo <span class="evi">16 años</span>. '
  'Estudio en un instituto y hablo <span class="evi">español e inglés</span>. Me gusta la música y viajar. Busco un amigo o una amiga para hablar español. ¿Y tú, quién eres?</p></div>'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["diego"]}</div><div><div class="nm">Diego</div><div class="fr">app · perfil</div></div></div>'
  '<p>¡Qué onda! Soy <span class="evi">Diego</span>, de <span class="evi">Ciudad de México</span>. Tengo <span class="evi">15 años</span> y vivo con mi familia. '
  'Hablo <span class="evi">español</span> y un poco de <span class="evi">inglés</span>. Me encanta la comida y el fútbol. Quiero conocer gente de Europa. ¡Escríbeme!</p></div></div>')
P('<div class="lecdoel">🎯 <b>Objetivo de lectura:</b> lees om te ontdekken <b>wie waarvandaan komt</b> en <b>welke talen</b> ze spreken — je hoeft niet élk woord te begrijpen.</div>')
P('</div>')  # page §5a
# ② scannen (informatieraster) + juist/fout + bewijs
P('<div class="page">')
P(actx(2, "Escanea: completa la tabla",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
'<p>Busca los datos en los perfiles. <span class="gloss">Zoek de gegevens in de profielen.</span></p>'
  '<table class="mp"><thead><tr><th></th><th>País / ciudad</th><th>Edad</th><th>Idiomas</th><th>Le gusta…</th></tr></thead><tbody>'
  '<tr><td><b>Lucía</b></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td><b>Diego</b></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '</tbody></table>', apoyo="Modelo: de bewijszinnen staan gemarkeerd in de tekst"))
P(actx(3, "¿Verdadero o falso? + prueba",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
'<p>¿Verdadero o falso? Copia las palabras del texto que lo demuestran. <span class="gloss">Waar of niet waar? Schrijf de woorden uit de tekst die het bewijzen.</span></p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba (palabras del texto)</th></tr></thead><tbody>'
  '<tr><td>Lucía tiene 16 años.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Diego es de España.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Los dos hablan inglés.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>A Diego le gusta la música.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '</tbody></table>', apoyo="Pista: onderstreep in de tekst"))
P(actx(4, "Del contexto: ¿qué significa?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>¿Qué significan <b>«Busco un amigo»</b> y <b>«¡Escríbeme!»</b>? Elige y explica qué pista te ha ayudado. '
  '<span class="gloss">Wat betekenen die twee uitdrukkingen? Kies en leg uit welke aanwijzing je hielp.</span></p>'
  '<p style="margin-left:12.5mm">Busco = ☐ ik zoek ☐ ik vind &nbsp;·&nbsp; ¡Escríbeme! = ☐ bel me ☐ schrijf me<br>Pista que me ayudó: <span class="wl lg"></span></p>', apoyo="Pista: no mires la palabra suelta: lee la frase entera"))
# ③bis — leer una gráfica (infografía · mediación: lezen van data)
P('<div class="infocard"><div class="it">📊 Infografía · ¿Qué idiomas estudian los jóvenes en Europa?</div>'
  '<div class="isub">Fuente: encuesta escolar (datos aproximados) · lees de balken</div>'
  + gustobars([("inglés",92),("español",26),("francés",23),("alemán",18),("neerlandés",6)]) + '</div>')
P(actx(5, "Lee la gráfica y responde",
  [{"t":"🔍 Leer","skill":True},{"t":"🔢 Mediar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Antwoord met een <b>hele zin</b> op basis van de grafiek.</p>'
  '<p style="margin-left:12.5mm">a) ¿Qué idioma estudian más? <span class="wl md"></span><br>'
  'b) ¿Cuántos por ciento estudian español? <span class="wl md"></span><br>'
  'c) ¿Qué idioma estudian menos? <span class="wl md"></span><br>'
  'd) ¿Y tú? Yo estudio <span class="wl md"></span> <i>(porque…)</i> <span class="wl md"></span></p>', apoyo="Marco: estudian… · el … por ciento"))
# ③ productieve reactie (keten lezen→schrijven/spreken)
P(tarea_com("Tarea comunicativa · Responde a un perfil",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p>Elige un perfil y escribe un <b>mensaje de respuesta</b> en el que te presentas: escribes tú, '
  'a Lucía o a Diego, para conoceros. Después léelo en voz alta. '
  '<span class="gloss">Kies één profiel en schrijf een antwoordbericht waarin je jezelf voorstelt; '
  'lees het daarna hardop voor.</span></p>'
  '<div class="wbox"></div>'
  + APO.html("Marco: Hola, me llamo… soy de… tengo… hablo…")))
P(mispal("Mis palabras del perfil — woorden die ik uit de teksten haal", 3))
P('<div class="route-note">🎮 <b>Sigue online:</b> en la página digital escuchas los dos perfiles, grabas tu mensaje de respuesta y juegas con las flip cards y los drills, que se corrigen solos. <span class="gloss">Online: luisteren, opnemen en zelfcorrigerend oefenen.</span></div>')
P('</div>')  # page §5b

# ================= TALLER DE LENGUA =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num" style="color:var(--crema)">✎</span><span class="pk" style="background:var(--gd)">Taller de lengua</span>')
P('<div class="intro"><b>ES:</b> Dos herramientas para escribir bien: la <b>mayúscula</b> y los <b>conectores</b>. <span class="gloss">Twee schrijfgereedschappen.</span></div>')
P(lpd(("8","taalsysteem: ortografía + conectoren")))
P('</div>')
P('<h3 style="margin-top:6mm">Ortografía · mayúscula o minúscula</h3>')
P('<p style="font-size:9.6pt">① <b>Contraste visual:</b></p>')
P(vpairs([("España 🔵 (land)","español (taal)"),("Bélgica (land)","belga (nat.)"),("Madrid (stad)","madrileño (inwoner)"),("Francia","francés")]))
P(regla("Regla · mayúsculas", '<p><b>Land/stad/naam = hoofdletter</b> · <b>nationaliteit/taal = kleine letter</b>. 🟡 <i>«el país grita, la nacionalidad susurra»</i> (het land roept, de nationaliteit fluistert).</p>'))
P(actx(1, "Clínica de mayúsculas",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
'<p>Subraya el error y vuelve a escribir la frase bien. <span class="gloss">Onderstreep de fout en herschrijf de zin correct.</span></p>'
  '<p style="margin-left:12.5mm">1) <span class="trap">soy Español y vivo en bélgica</span> → <span class="wl lg"></span><br>'
  '2) <span class="trap">Ella habla Francés e Inglés</span> → <span class="wl lg"></span><br>'
  '3) <span class="trap">diego es de méxico, es Mexicano</span> → <span class="wl lg"></span></p>', apoyo="Modelo"))
P('<h3 style="margin-top:6mm">Conectores · y · e · o · u · porque</h3>')
P('<table class="mp"><thead><tr><th>Conector</th><th>Uso</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td><b>y</b></td><td>en</td><td>Soy belga <b>y</b> hablo español.</td></tr>'
  '<tr><td><b>e</b></td><td>«en» vóór i-/hi-</td><td>español <b>e</b> inglés</td></tr>'
  '<tr><td><b>o</b> / <b>u</b></td><td>of (u vóór o-/ho-)</td><td>siete <b>u</b> ocho</td></tr>'
  '<tr><td><b>porque</b></td><td>want / omdat</td><td>Aprendo español <b>porque</b> me gusta.</td></tr></tbody></table>')
P('<div class="truc"><b>🔴 Trampa para neerlandeses:</b> «want» y «omdat» son las dos <b>porque</b>, una sola palabra. Y «dus» es <b>así que / por eso</b>, no <i>luego</i>. <span class="gloss">Eén woord porque voor allebei; «dus» is niet luego.</span></div>')
P(actx(2, "Une con y / e / o / u / porque",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
'<p>Escribe el conector que falta. <span class="gloss">Escribe el conector correcto. <span class="gloss">vul het juiste verbindingswoord in</span></span></p>'
  '<p style="margin-left:12.5mm">a) Hablo neerlandés ___ inglés. &nbsp; b) ¿Tienes siete ___ ocho años? &nbsp; c) Estudio español ___ me gusta viajar. &nbsp; d) español ___ italiano.<br><span class="wl full"></span></p>', apoyo="Banco de palabras"))
P(actx(3, "Amplía con un porqué",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
'<p>Añade a cada frase una razón con <b>porque</b>. <span class="gloss">Voeg aan elke zin een reden met «porque» toe.</span></p>'
  '<p style="margin-left:12.5mm">Aprendo español <span class="wl lg"></span><br>Vivo en mi ciudad <span class="wl lg"></span></p>', apoyo=""))
P(actx(4, "Puntúa la frase",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vuelve a escribir con <b>mayúsculas</b> correctas y un <b>conector</b>. <span class="gloss">herschrijf met hoofdletters en een verbindingswoord</span></p>'
  '<p style="margin-left:12.5mm">1) leo es de bélgica habla neerlandés inglés → <span class="wl full"></span>'
  '2) sara vive en madrid estudia español le gusta → <span class="wl full"></span></p>', apoyo="Modelo"))
P(actx(5, "Escribe tu mini-perfil con conectores",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
'<p>Escribe tres frases sobre ti con <b>y</b>, <b>e</b> y <b>porque</b>, con las mayúsculas correctas. <span class="gloss">Schrijf drie zinnen over jezelf met y, e én porque, met correcte hoofdletters.</span></p>'
  '<div class="wbox sm"></div>', apoyo=""))
P('<div class="route-note">🎮 <b>Practica online:</b> «Caza de mayúsculas» en de conectoren-oefeningen met zelfcorrectie.</div>')
P('</div>')  # page Taller

# ================= LECTURA 2 · ESCUCHA =================
# Zelfde bron als de digitale hub (lectura_data / escucha_data): papier en scherm
# kunnen zo niet uit elkaar lopen. Elk op een eigen bladzijde (§14).
P('<div class="page"><div class="parada sec">')
P('<span class="num">5.2</span><span class="pk">§5.2 · Lectura 2 — «Busco un compi de intercambio»</span>')
P('<div class="intro"><b>ES:</b> Un perfil de verdad, de una app de intercambio. <b>No hace falta entenderlo todo</b> para sacar la información. <span class="gloss">Een echt profiel uit een uitwisselingsapp. Je hoeft niet alles te begrijpen om de informatie te vinden — zoek gericht.</span></div>')
P(PB.lectura_print(LD.C5_U1, "1"))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">6</span><span class="pk">§6 · Escucha — «El primer día en el instituto»</span>')
P('<div class="intro"><b>ES:</b> Álex y Sam se conocen en el pasillo. <b>Escucha primero, escribe después.</b> <span class="gloss">Álex en Sam leren elkaar kennen in de gang. Eerst luisteren, dan schrijven; het transcript staat online en gaat pas open ná de taken.</span></div>')
P(PB.escucha_print(ED.C5_U1, "1"))
P('</div>')

# ================= CULTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">★</span><span class="pk">Cultura · Madrid y los nombres hispanos</span>')
P('<div class="intro"><b>ES:</b> En el mundo hispano la gente tiene <b>dos apellidos</b> y trata de <b>tú</b> o de <b>usted</b> según la situación. <span class="gloss">Twee achternamen; tú of usted naargelang de situatie.</span></div>')
P(lpd(("5","kenmerkende aspecten van de cultuur"), ("2","relevante info uit een tekst")))
P('</div>')
P('<div class="fams" style="margin-top:6mm">')
P(pcard("Madrid 🇪🇸", '<div class="ej">Hoofdstad van España (~3,3 mln). <b>Puerta del Sol</b>, el <b>Prado</b>, el <b>Retiro</b>, el <b>Real Madrid</b>.</div><div class="anchor gloss">Onze eerste parada: vertrekpunt van La Ruta.</div>'))
P(pcard("Los dos apellidos", '<div class="ej"><b>Lucía Ramírez García</b>: <i>Ramírez</i> (padre) + <i>García</i> (madre). Bij trouwen verandert de naam <b>niet</b>.</div><div class="t2">NL heeft één achternaam — hier twee.</div>'))
P('</div>')
P('<p style="font-size:9.6pt">① <b>¿Tú o usted? — contraste:</b></p>')
P(vpairs([("tú (leeftijdsgenoot)","usted (beleefd)"),("¿Cómo estás?","¿Cómo está usted?"),("tú eres","usted es"),("España: veel tú","Colombia/Perú: vaak usted")]))
P('<div class="truc"><b>🟡 Adelanto:</b> en <b>C6</b> conoces a Mateo, de Argentina, que usa <b>vos</b>: otra forma de tratamiento. <span class="gloss">In C6 kom je nog een aanspreekvorm tegen.</span></div>')
P(actx(1, "Comprensión — verdadero o falso",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
'<p>¿Verdadero o falso? Corrige las frases falsas. <span class="gloss">Waar of niet waar? Verbeter de foute zinnen.</span></p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Corrección</th></tr></thead><tbody>'
  '<tr><td>En España se usa un solo apellido.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>«Usted» es más formal que «tú».</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Madrid es la capital de México.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="Modelo: tekst boven"))
P(actx(2, "Escribe y elige tú/usted",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p>Inventa tres nombres «a la hispana» (nombre + dos apellidos) y elige para cada situación '
  '<b>tú</b> o <b>usted</b> con su saludo. '
  '<span class="gloss">Bedenk drie namen op zijn Spaans en kies per situatie tú of usted met de juiste groet.</span></p>'
  '<p style="margin-left:12.5mm">Nombres: <span class="wl full"></span></p>'
  '<p style="margin-left:12.5mm">a) een klasgenoot: <span class="wl md"></span> &nbsp; b) de directeur: <span class="wl md"></span> &nbsp; c) een oude mevrouw: <span class="wl md"></span></p>', apoyo="Pista: ¿es alguien de tu edad o una persona adulta que no conoces?"))
P('</div>')  # page Cultura

# ================= TAREA FINAL =================
retos("cultura_u1", "Reto — hablar por otro",
      'El último reto no va de ti: presentas a <b>tu compañero/a</b> durante un minuto, en tercera persona, '
      'con lo que has anotado en esta unidad.',
      'De laatste reto gaat niet over jou: je stelt één minuut lang je partner voor, in de derde persoon, '
      'met wat je in deze unit genoteerd hebt.')
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num">✦</span><span class="pk" style="background:var(--gd)">Tarea final · Mi pasaporte</span>')
P('<div class="intro"><b>ES:</b> Crea tu <b>pasaporte de La Ruta</b> y preséntate (identidad real o nueva). <span class="gloss">Maak je paspoort en stel je voor.</span></div>')
P('<div class="route-note">🎯 <b>Communicatieve taak:</b> afzender = jij · ontvanger = de klas/Lucía · doel = jezelf voorstellen · situatie = aankomst in Madrid · resultaat = ingevuld paspoort + voorstelling.</div>')
P(lpd(("3","doelgericht schrijven met een voorbeeld"), ("4","zich mondeling voorstellen"), ("7","woordenschat"), ("8","ser/presente/artículos")))
P('</div>')
P('<ol class="pasos">'
  '<li><b>Elige tu identidad.</b> Nombre + dos apellidos, país, ciudad, edad, idiomas.</li>'
  '<li><b>Rellena el pasaporte</b> hieronder (in hele woorden).</li>'
  '<li><b>Escribe tu presentación</b> (5–6 frases) met ser + presente + conectoren.</li>'
  '<li><b>Preséntate</b> a la clase (of neem een filmpje/audio op via de digitale pagina).</li>'
  '<li><b>Pregunta</b> a un compañero y presenta a esa persona en 3ª persona.</li></ol>')
P('<div class="fichacard" style="border-color:var(--gd)"><div>'
  '<div class="row"><span class="k">🛂 Nombre</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Apellidos</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">País</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Nacionalidad</span><span class="v"><span class="wl md"></span></span></div></div><div>'
  '<div class="row"><span class="k">Edad</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Ciudad</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Idiomas</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Firma</span><span class="v"><span class="wl md"></span></span></div></div></div>')
P('<div class="se" style="margin-top:5mm">Mi presentación <span class="gloss" style="font-size:8pt">· 5–6 frases: ser + presente + conectores</span></div><div class="wbox"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba tu presentación</b> en la página digital (recorder + rúbrica).</div>',
           qr("Escanea y graba", "Tarea · Mi pasaporte", seed=41)))
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Mijn paspoort heeft <b>alle gegevens</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>ser</b> en het <b>presente</b> correct</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik verbind met <b>y / porque</b> en schrijf <b>mayúsculas</b> juist</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>stel mezelf mondeling voor</b> en versta een klasgenoot</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="se" style="margin-top:5mm">Paso 5 · Presenta a un compañero/a <span class="gloss" style="font-size:8pt">— interview + presenteer in de 3e persoon</span></div>')
P('<table class="wtab mp"><thead><tr><th>Nombre</th><th>País / ciudad</th><th>Edad</th><th>Idiomas</th></tr></thead><tbody>'
  '<tr><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>'
  '<p style="margin-left:0mm">Mi presentación (3ª persona): <span class="wl full"></span></p>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — el pasaporte de mi compañero/a</div>'
  '<table><thead><tr><th>Lo que está muy bien</th><th>Un consejo (una cosa)</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('</div>')  # page Tarea

# ================= REPASO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">✓</span><span class="pk">Repaso · lo esencial</span>')
P('<div class="intro"><b>ES:</b> Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, 20 juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag.</span></div>')
P('</div>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>Presentarse:</b> Me llamo… · Soy de… · Soy + nat. · Tengo … años · Vivo en… · Hablo…</li>'
  '<li><b>Ser:</b> soy · eres · es · somos · sois · son. <b>Presente reg.:</b> -o/-as/-a/-amos/-áis/-an.</li>'
  '<li><b>Preguntar:</b> ¿Cómo? ¿De dónde? ¿Dónde? ¿Cuántos años? ¿Cuál? ¿Qué? ¿Quién?</li>'
  '<li><b>Artículos:</b> el/la · los/las · un/una (leer met lidwoord!).</li>'
  '<li><b>Las trampas:</b> 🔴 edad = <b>tener</b> · 🔴 nationaliteit = <b>klein</b> · 🔴 ¿Cuál? vóór ser · 🔴 want/omdat = <b>porque</b>.</li></ul></div>')
P(guide("Repasa jugando (online):", "— 18 spelletjes met zelfcorrectie op de digitale pagina.", "🎮"))
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td>mezelf <b>voorstellen</b> (naam, land, leeftijd, stad)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>het verbo <b>ser</b> en het presente regular gebruiken</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>iemand <b>vragen</b> stellen</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>het juiste <b>lidwoord</b> kiezen</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>landen & nationaliteiten <b>herkennen</b></td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil de U1: <span class="wl md"></span> · Lo más difícil: <span class="wl md"></span></i></div>')
P('<div class="bridge"><b>» Siguiente parada: Sevilla (U2).</b> Ya sabes decir quién eres; en <b>U2 «Mi gente»</b> presentas a tu <b>familia</b> met <i>tener</i>, los posesivos y describir. <span class="gloss">In U2 stel je je familie voor in Sevilla.</span></div>')
P('</div>')  # page Repaso

# ================= §V VOCABULARIO =================
import json
VOC = json.load(open(f"{HERE}/u1_vocab.json", encoding="utf-8"))
GRP = [("datos","Datos personales"),("ficha","La ficha / el formulario"),("interrog","Palabras interrogativas"),
       ("saludos","Saludos (uit U0)"),("pais","Países y nacionalidades — mundo hispano"),("mundo","Países del mundo")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (begrijpen en zelf gebruiken)")))
P('</div>')
# visueel netwerk vóór de tabellen
P('<p style="font-size:9.6pt">Het <b>mundo hispano</b> als netwerk — landen per regio (de kaart groeit mee):</p>')
P(clusters([
  ("🇪🇸","España + Europa",["España → español","Francia → francés","Portugal → portugués"],"Ons vertrekpunt + buurlanden."),
  ("🌎","América hispana",["México → mexicano","Colombia → colombiano","Perú · Argentina · Chile"],"De volgende paradas."),
  ("🌍","Más allá",["Bélgica → belga","Guinea Ecuatorial (África)","EE. UU. → estadounidense"],"Spaans klinkt overal."),
]))
for key, titel in GRP:
    items = [v for v in VOC if v.get("grp") == key]
    if not items: continue
    P(f'<h3 style="margin-top:6mm">{titel} <span class="gloss" style="font-size:8pt">· {len(items)} woorden</span></h3>')
    rows = "".join(f'<tr><td><b>{v["es"]}</b></td><td>{v["nl"]}</td><td class="gloss">{v["soort"]}</td><td class="gloss">{v["ej"]}</td></tr>' for v in items)
    P(f'<table class="alf"><thead><tr><th>Español</th><th>Nederlands</th><th>ERK/soort</th><th>Ejemplo</th></tr></thead><tbody>{rows}</tbody></table>')
# print-oefenladder V.1-V.4
P('<div class="divider">Escalera de práctica · V.1–V.4</div>')
P(actx("V.1", "Reconocer — ES → NL",
  [{"t":"🔍 Leer","skill":True},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Escribe la traducción. <span class="gloss">Escribe la traducción. <span class="gloss">Schrijf de vertaling.</span></span> el apellido = <span class="wl md"></span> · la edad = <span class="wl md"></span> · el idioma = <span class="wl md"></span> · la dirección = <span class="wl md"></span></p>', apoyo="Modelo"))
P(actx("V.2", "Distinguir — sorteer per thema",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Clasifica estas seis palabras. <span class="gloss">Sorteer deze zes woorden.</span>'
  '<span class="words"><b>correo · Perú · ¿Cuál? · nacionalidad · Chile · edad</b></span></p>'
  + sortcols([("dato",""),("país",""),("interrogativo","")], eigen=False), apoyo="Banco de palabras"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Completa la palabra en español; tienes la primera letra. '
  '<span class="gloss">Vul het Spaanse woord aan; de beginletter staat er.</span><br>het land = <b>p</b>___ · de stad = <b>c</b>___ · de taal = <b>i</b>___ · de nationaliteit = <b>n</b>___<br><span class="wl full"></span></p>', apoyo="Primera letra"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Escribe una frase correcta con <b>nombre · país · edad</b>. '
  '<span class="gloss">Escribe una frase correcta con die drie gegevens.</span></p><div class="wbox sm"></div>', apoyo=""))
P(mispal("Mis palabras de la unidad", 3))
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Sigue en la página digital:</span> <span class="g">flip cards (ES↔NL), audio en de 20 spellen bouwen de steun verder af.</span></div></div>')
P('</div>')  # page §V

# ---------- EDITBAR ----------
EDITBAR = '''
<div class="editbar" id="editbar">
  <span id="ebtxt">✏️ «Bewerken» om zelf tekst aan te passen</span>
  <button class="b1" id="ebEdit">Bewerken</button>
  <button class="b2" id="ebPdf">🖨️ Opslaan als PDF</button>
  <button class="b2" id="ebSave">💾 Bewaar</button>
</div>
<script id="ebscript">
(function(){
 var SEL='h1,h2,h3,h4,p,td,th,li,.intro,.hist,.gloss,.ojo,.anchor,.ej,.q,.sub,.route-note,.pk,.se,.divider,.t,.t2,.nl,.es,.lpdchip,.lpdlab,.wcol .ch,.bub,.k,.v,.ln,.mq,.ma,.br,.blk,.clu li,.node';
 var editing=false;
 function setEditable(on){document.querySelectorAll(SEL).forEach(function(e){if(on){e.setAttribute('contenteditable','true');e.setAttribute('spellcheck','false');}else{e.removeAttribute('contenteditable');}});}
 var eb=document.getElementById('editbar'),txt=document.getElementById('ebtxt'),bE=document.getElementById('ebEdit');
 bE.onclick=function(){editing=!editing;document.body.classList.toggle('editing',editing);eb.classList.toggle('on',editing);setEditable(editing);
   txt.textContent=editing?'✏️ AAN — klik op tekst en typ':'✏️ «Bewerken» om zelf tekst aan te passen';bE.textContent=editing?'Klaar':'Bewerken';};
 document.getElementById('ebPdf').onclick=function(){window.print();};
 document.getElementById('ebSave').onclick=function(){
   if(editing){bE.click();}
   var clone=document.documentElement.cloneNode(true);
   var b=clone.querySelector('.editbar'); if(b) b.remove();
   var s=clone.querySelector('script#ebscript'); if(s) s.remove();
   var html='<!doctype html>\\n'+clone.outerHTML;
   var blob=new Blob([html],{type:'text/html'}); var a=document.createElement('a');
   a.href=URL.createObjectURL(blob); a.download='U1_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Español en la práctica · U1 ¿Quién eres?</title><style>'
        + CSS + PB.CSS + RP.CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/U1.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes")
