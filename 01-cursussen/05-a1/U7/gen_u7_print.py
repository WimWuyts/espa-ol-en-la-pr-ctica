#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de print-HTML U5.html (C5 · Unidad 5 «¡Ñam!») → PDF via Chromium.
# Zelfde componentenkit/pijplijn als golden sample U0/U1/U4 (cursus-print.css). Fonts base64 ingebed,
# cast-avatars inline SVG (cast_gen). Cursuskleur = groen (C5). Parada 5 = México/CDMX, gastheer Diego.
# Output = standalone bewerkbare U5.html.
import os, sys, base64
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f"{ROOT}/02-huisstijl/beeld/generators")
import cast_gen as C
import sys as _sys
_sys.path.insert(0, "/home/user/espa-ol-en-la-pr-ctica/03-build/web")
import qr_print as QRP; QRP.fijar("C5", 7)
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

AV = {n: C.make(n, "avatar", 64) for n in ["lucia", "diego", "valen", "nina"]}
TU = C.tu_avatar(64)
MOCH = C.mochila(84, "map")

# ---------- CSS: identiek aan golden sample U0/U1/U4 (cursus-print.css + schrijf-componenten) ----------
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

.regla,.truc,.pcard,.call,.qr,.guide,.esen,.audiorow,.wcols,.wbox,.sem,.acthead,.chatline,.fichacard,.mispal,.ptext,.lecdoel,.gustobars{ break-inside:avoid; }

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
/* ===== VISUELE GRAMMATICA-/WOORDENSCHATCOMPONENTEN ===== */
.obsbox{ background:var(--gt); border-radius:12pt; padding:4mm 5mm; margin:3mm 0; }
.obsbox .ln{ font-size:11pt; margin:1.6mm 0; } .obsbox .hl{ background:#fff; border-bottom:2px solid var(--g); border-radius:3pt; padding:.2mm 1.4mm; font-weight:700; color:var(--gd); }
.obsq{ font-size:9pt; color:var(--gd); margin-top:2mm; } .obsq b{ color:var(--gd); }
.machine{ display:flex; align-items:center; gap:0; flex-wrap:wrap; margin:4mm 0; }
.machine .mbox{ border:1.5px solid var(--g); border-radius:10pt; padding:2.5mm 4mm; text-align:center; background:#fff; min-width:22mm; }
.machine .mbox .lb{ font-size:7pt; letter-spacing:.08em; text-transform:uppercase; color:var(--mut); display:block; }
.machine .mbox .vv{ font-family:var(--disp); font-weight:700; font-size:12.5pt; color:var(--ink); } .machine .mbox .vv .end{ color:var(--ww); }
.machine .arr{ color:var(--g); font-weight:800; font-size:14pt; padding:0 3mm; }
.machine .mbox.res{ background:var(--gt); border-color:var(--gd); }
.blocks{ margin:3mm 0; } .brow{ display:flex; gap:2mm; margin:2mm 0; flex-wrap:wrap; align-items:center; }
.blk{ border-radius:8pt; padding:1.8mm 4mm; font-weight:600; font-size:10pt; border:1.5px solid; }
.blk.per{ background:#DBEAFE; border-color:#93c5fd; color:#1E40AF; } .blk.vb{ background:#FED7AA; border-color:#fdba74; color:#9A3412; }
.blk.ob{ background:#DCFCE7; border-color:#86efac; color:#166534; } .blk.pl{ background:#CCFBF1; border-color:#5eead4; color:#0F766E; } .blk.ti{ background:#EDE9FE; border-color:#c4b5fd; color:#5B21B6; }
.blk.opt{ background:#fff; border-color:var(--line2); color:var(--ink); border-style:dashed; }
.agree{ text-align:center; margin:3mm 0; font-family:var(--disp); }
.agree .w{ font-size:15pt; font-weight:700; } .agree .w u{ color:var(--gd); text-decoration-thickness:2px; text-underline-offset:2px; }
.agree .tie{ font-size:8pt; color:var(--mut); margin-top:1mm; }
.tree{ border-left:3px solid var(--g); margin:3mm 0 3mm 3mm; padding-left:5mm; }
.tree .node{ font-size:9.6pt; margin:2mm 0; } .tree .node b{ color:var(--gd); } .tree .yes{ color:var(--g); font-weight:700; } .tree .no{ color:var(--mut); font-weight:700; }
.tree .res{ display:inline-block; background:var(--g); color:#fff; font-family:var(--disp); font-weight:700; border-radius:6pt; padding:.6mm 3mm; }
.mirror{ margin:3mm 0; } .mirror .mq{ font-size:11pt; font-weight:700; color:var(--onder); } .mirror .ma{ font-size:11pt; color:var(--gd); margin-left:8mm; }
.mirror .mk{ background:#EDE9FE; border-radius:3pt; padding:.2mm 1.2mm; font-weight:700; }
.fmu{ display:grid; grid-template-columns:repeat(3,1fr); gap:3mm; margin:3mm 0; }
.fmu .fc{ border:1px solid var(--line); border-radius:10pt; overflow:hidden; background:#fff; }
.fmu .fc .hd{ font-family:var(--disp); font-weight:700; font-size:8pt; letter-spacing:.08em; text-transform:uppercase; color:#fff; background:var(--g); padding:1.6mm 3mm; text-align:center; }
.fmu .fc .bd{ padding:2.5mm 3mm; font-size:9.4pt; }
.scaffold{ display:grid; grid-template-columns:repeat(4,1fr); gap:2mm; margin:3mm 0; align-items:end; }
.scaffold .sq{ border:1.5px solid var(--g); border-radius:9pt; background:#fff; padding:2.5mm 3mm; font-size:8.6pt; }
.scaffold .sq .st{ font-size:7pt; text-transform:uppercase; letter-spacing:.08em; color:var(--g); font-weight:700; display:block; margin-bottom:1mm; }
.scaffold .s1{ height:34mm } .scaffold .s2{ height:29mm } .scaffold .s3{ height:24mm } .scaffold .s4{ height:19mm; background:var(--gt); }
.zoom{ display:grid; grid-template-columns:1fr auto 1fr; gap:3mm; align-items:center; margin:3mm 0; }
.zoom .zc{ border:1px solid var(--line); border-radius:10pt; padding:3mm 4mm; text-align:center; background:#fff; } .zoom .zc .zh{ font-size:7.6pt; text-transform:uppercase; color:var(--mut); } .zoom .zc b{ font-family:var(--disp); font-size:13pt; color:var(--gd); }
.zoom .zar{ font-size:16pt; color:var(--g); }
.clusters{ display:grid; grid-template-columns:repeat(3,1fr); gap:4mm; margin:3mm 0; }
.clu{ border:1px solid var(--line); border-top:4px solid var(--g); border-radius:12pt; padding:3mm 4mm; background:#fff; }
.clu .ch{ font-family:var(--disp); font-weight:700; font-size:10.5pt; color:var(--gd); display:flex; gap:2mm; align-items:center; } .clu .ci{ font-size:14pt; }
.clu ul{ margin:2mm 0 0; padding-left:4mm; font-size:9.4pt; } .clu li{ margin:.8mm 0; }
.clu .ex{ font-size:8.4pt; color:var(--mut); font-style:italic; margin-top:2mm; }
.colloc{ display:flex; gap:5mm; align-items:center; margin:3mm 0; flex-wrap:wrap; }
.colloc .cen{ background:var(--ww); color:#fff; font-family:var(--disp); font-weight:800; font-size:15pt; border-radius:12pt; padding:4mm 7mm; }
.colloc .brs{ display:flex; flex-wrap:wrap; gap:2mm; } .colloc .br{ background:var(--gt); color:var(--gd); border-radius:20pt; padding:1.4mm 4mm; font-size:9.6pt; font-weight:600; }
.scale{ margin:3mm 0; } .scale .track{ display:flex; align-items:center; gap:0; } .scale .sstop{ flex:1; text-align:center; position:relative; }
.scale .sd{ width:3.5mm; height:3.5mm; border-radius:50%; background:var(--g); margin:0 auto; } .scale .sl{ font-size:8.6pt; margin-top:1mm; color:var(--ink); }
.scale .bar{ position:absolute; top:1.6mm; left:0; right:-100%; height:2px; background:var(--line2); z-index:-1; }
.vpairs{ display:grid; grid-template-columns:1fr 1fr; gap:2mm 6mm; margin:3mm 0; }
.vp{ display:flex; justify-content:space-between; border-bottom:1px dashed var(--line); padding:1.2mm 0; font-size:10pt; } .vp b{ color:var(--gd); } .vp .ar{ color:var(--mut); }
.mispal{ border:1.5px dashed var(--g); border-radius:12pt; padding:3mm 4mm; margin:4mm 0; background:#fff; }
.mispal .mh{ font-family:var(--hand); font-size:14pt; color:var(--gd); }
.mispal table{ width:100%; margin:2mm 0 0; } .mispal td,.mispal th{ border:1px solid var(--line); padding:1.4mm 2mm; height:8mm; font-size:8.6pt; } .mispal th{ background:var(--gt); color:var(--gd); font-size:7.6pt; text-transform:uppercase; }
.xray{ margin:3mm 0; } .xray .xs{ font-family:var(--disp); font-size:12pt; text-align:center; } .xray .xrow{ display:flex; justify-content:center; gap:4mm; margin-top:2mm; flex-wrap:wrap; font-size:8.4pt; color:var(--mut); text-align:center; } .xray .xrow b{ display:block; color:var(--ink); font-family:var(--body); }
.pico{ width:9mm;height:9mm;border-radius:50%;background:var(--gt);display:inline-flex;align-items:center;justify-content:center;font-size:12pt; }
/* ===== leesvaardigheid (Lectura) ===== */
.lecdoel{ background:var(--amberbg); border-left:3px solid var(--amber); border-radius:8pt; padding:2.5mm 5mm; margin:3mm 0; font-size:9.6pt; } .lecdoel b{ color:var(--amber); }
.txtmeta{ display:flex; gap:2mm; flex-wrap:wrap; margin:2mm 0; } .txtmeta .tm{ font-size:7.6pt; font-weight:600; background:var(--gt); color:var(--gd); border-radius:20pt; padding:.7mm 3mm; } .txtmeta .tm b{ color:var(--gd); }
.ptexts{ display:grid; grid-template-columns:1fr 1fr; gap:5mm; margin:3mm 0; }
.ptext{ border:1px solid var(--line); border-top:4px solid var(--g); border-radius:12pt; padding:4mm 5mm; background:#fff; font-size:9.5pt; }
.ptext .ph{ display:flex; gap:3mm; align-items:center; margin-bottom:2mm; } .ptext .ph .av{ width:12mm;height:12mm;border-radius:50%;overflow:hidden;flex:none } .ptext .ph .av svg{width:100%;height:auto} .ptext .ph .nm{ font-family:var(--disp); font-weight:700; font-size:11pt; color:var(--ink); } .ptext .ph .fr{ font-size:8pt; color:var(--mut); }
.ptext p{ margin:1.5mm 0; } .evi{ background:#FEF3C7; border-radius:3pt; padding:.1mm 1mm; }
/* smaak-bars (encuesta/grafiek) */
.gustobars{ margin:3mm 0; } .gbar{ display:grid; grid-template-columns:34mm 1fr; gap:3mm; align-items:center; margin:1.8mm 0; font-size:9.2pt; }
.gbar .track2{ background:var(--crema); border-radius:6pt; height:6mm; position:relative; overflow:hidden; }
.gbar .fill{ background:var(--g); height:100%; border-radius:6pt; }
.gbar .pct{ position:absolute; right:2mm; top:0; line-height:6mm; font-size:8pt; color:#fff; font-weight:700; }
/* menú-kaart (la carta) */
.menu{ border:1.5px solid var(--gd); border-radius:14pt; padding:4mm 6mm; margin:4mm 0; background:#fff; }
.menu .mt{ font-family:var(--disp); font-weight:800; font-size:13pt; color:var(--gd); text-align:center; border-bottom:2px dashed var(--line2); padding-bottom:2mm; }
.menu .sec2{ font-family:var(--disp); font-weight:700; font-size:9.6pt; color:var(--ww); text-transform:uppercase; letter-spacing:.06em; margin:3mm 0 1mm; }
.menu .mi{ display:flex; justify-content:space-between; font-size:9.4pt; padding:.8mm 0; border-bottom:1px dotted var(--line); }
.menu .mi .pr{ color:var(--gd); font-weight:700; }
"""

# ---------------- component-helpers (identiek aan U1/U4) ----------------
import sys as _qs; _qs.path.insert(0, "/home/user/espa-ol-en-la-pr-ctica/03-build/web")
from qr_print import qr          # echte QR-code, zie qr_print.py

def audiorow(call_html, qr_html):
    return f'<div class="audiorow"><div class="call">{call_html}</div>{qr_html}</div>'

def act(num, title, badges, body, steun=None):
    b = "".join(f'<span class="badge{" skill" if s.get("skill") else ""}">{s["t"]}</span>' for s in badges)
    return (f'<div class="act"><div class="acthead"><span class="anum">{num}</span>'
            f'<div><div class="h">{title}</div><div class="badges">{b}</div></div></div>{body}</div>')

def regla(tag, html):
    return f'<div class="regla"><span class="tag">{tag}</span>{html}</div>'

def guide(hand, g, ic="🎒"):
    return f'<div class="guide"><div class="ic">{ic}</div><div><span class="hand">{hand}</span> <span class="g">{g}</span></div></div>'

def lpd(*chips):
    c = "".join(f'<span class="lpdchip"><b>LPD {n}</b> · {t}</span>' for n, t in chips)
    return f'<div class="lpd"><span class="lpdlab">Leerplandoelen III-Spa-d</span>{c}</div>'

def divider(t): return f'<div class="divider">{t}</div>'


def retos(ancla, titulo, intro_es, intro_nl):
    """Retoblok van één sectie — volledige oefening voor print, verwijskaartje
    voor wat op de hub of in de PowerPoint leeft."""
    P('<div class="page">')
    P(f'<div class="divider">{titulo}</div>')
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
    n = len(cols)
    inner = "".join(
        f'<div class="wcol"><div class="ch">{k}{f"<small>{s}</small>" if s else ""}</div><div class="cb {height}"></div></div>'
        for k, s in cols)
    style = f'grid-template-columns:repeat({n},1fr)'
    eig = ('<div class="gloss" style="font-size:8pt;margin:1mm 0 0 12.5mm">↳ voeg per kolom één <b>eigen</b> woord toe.</div>' if eigen else "")
    return f'<div class="wcols" style="{style};margin-left:12.5mm">{inner}</div>{eig}'

def actx(num, title, badges, body, apoyo=None):
    return act(num, title, badges, body + (steun(apoyo) if apoyo else ""))

def tarea_com(title, badges, body):
    return act("★", title, badges, body)

def obsbox(lines, vragen=None):
    ln = "".join(f'<div class="ln">{l}</div>' for l in lines)
    q = f'<div class="obsq">{vragen}</div>' if vragen else ""
    return f'<div class="obsbox"><div class="se" style="margin:0 0 1.5mm">Observa · ¿qué se repite?</div>{ln}{q}</div>'

def machine(boxes):
    parts = []
    for i, (lab, val) in enumerate(boxes):
        cls = "mbox res" if i == len(boxes)-1 else "mbox"
        parts.append(f'<div class="{cls}"><span class="lb">{lab}</span><span class="vv">{val}</span></div>')
        if i < len(boxes)-1: parts.append('<span class="arr">→</span>')
    return f'<div class="machine">{"".join(parts)}</div>'

def blocks(rows):
    out = []
    for r in rows:
        out.append('<div class="brow">' + "".join(f'<span class="blk {c}">{t}</span>' for c, t in r) + '</div>')
    return f'<div class="blocks">{"".join(out)}</div>'

def tree(nodes):
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
    cls = ["s1", "s2", "s3", "s4"]
    return '<div class="scaffold">' + "".join(
        f'<div class="sq {cls[i]}"><span class="st">{lab}</span>{html}</div>' for i, (lab, html) in enumerate(steps)) + '</div>'

def zoom(left_h, left_v, right_h, right_v):
    return (f'<div class="zoom"><div class="zc"><span class="zh">{left_h}</span><br><b>{left_v}</b></div>'
            f'<div class="zar">🔎→</div><div class="zc"><span class="zh">{right_h}</span><br><b>{right_v}</b></div></div>')

def clusters(cols):
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

def menu(titel, secs):
    out = [f'<div class="menu"><div class="mt">{titel}</div>']
    for sec, items in secs:
        out.append(f'<div class="sec2">{sec}</div>')
        for nm, pr in items:
            out.append(f'<div class="mi"><span>{nm}</span><span class="pr">{pr}</span></div>')
    out.append('</div>')
    return "".join(out)


# ================= BODY =================
BODY = []
def P(*x): BODY.extend(x)

# ---------- OPENER ----------
P(f'''
<div class="hero">
  <div class="tab">U7 · MI CASA</div>
  <div class="eyebrow">UNIDAD 7 · LA RUTA · PARADA 7 — COLOMBIA / CARTAGENA 🇨🇴</div>
  <h1>Mi casa y mi barrio</h1>
  <div class="sub">Bajamos por la costa hasta <b>Cartagena</b>, en <b>Colombia</b>. Hoy praat je over <b>waar je woont</b>: la casa, las habitaciones, los muebles — en je leert <b>de weg vragen en uitleggen</b> in el barrio. <span class="gloss">We reizen naar Cartagena. Vandaag: je huis, je kamers en de weg vinden in de buurt.</span></div>
  <div class="q">¿Dónde vives? ¿Cómo es tu barrio? <span style="font-weight:400;opacity:.9">· Waar woon je? Hoe is jouw buurt?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U4 · València</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U5 · México</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U6 · Mercados</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U7 · Cartagena</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U8 · Perú</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 7 · Cartagena de Indias (Colombia).</b> Bajamos por la costa del Caribe. Aquí <b>Valen</b> te enseña su <b>barrio</b> de casas de colores: dónde <b>hay</b> qué, dónde <b>está</b> cada cosa, qué está pasando <b>ahora</b> y cómo <b>llegar</b> a la plaza. <span class="gloss">Valen toont je haar kleurrijke buurt en leert je de weg.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> En <b>Cartagena</b> las casas son de colores y tienen <b>balcones con flores</b>. <b>Valen</b> te abre la puerta: «Mira, en el <b>salón</b> <b>hay</b> un sofá y la cocina <b>está</b> a la derecha». Salís al <b>barrio</b>: «¿Cómo se va a la <b>plaza</b>? <b>Sigue</b> todo recto y <b>gira</b> a la izquierda». Aprendes a decir <b>dónde está</b> todo y a <b>explicar el camino</b>.
      <span class="gloss">In Cartagena zijn de huizen kleurrijk. Valen toont je haar huis en buurt: waar alles staat en hoe je de weg uitlegt.</span></div>
      <div class="ojo"><b>¡Ojo! — de valstrik van vandaag:</b> <b>hay</b> (= er is/zijn, iets nieuws, geen lidwoord-de) ≠ <b>está</b> (= staat/ligt, iets bekend, met de plaats). Zeg <i>Hay <b>un</b> parque</i> maar <i><b>El</b> parque está cerca</i>. En «rechts» = <b>a la derecha</b> (niet <span class="trap">correcto</span>!).</div>
    </div>
    <div>
      <div class="se">La gente de la ruta</div>
      <div class="cast">
        <div class="pc"><div class="avw">{AV["valen"]}</div><div class="nm">Valen</div><div class="fr">Cartagena 🇨🇴 · anfitriona</div></div>
        <div class="pc"><div class="avw">{AV["lucia"]}</div><div class="nm">Lucía</div><div class="fr">Sevilla 🇪🇸</div></div>
        <div class="pc"><div class="avw">{AV["diego"]}</div><div class="nm">Diego</div><div class="fr">CDMX 🇲🇽</div></div>
        <div class="pc"><div class="avw">{AV["nina"]}</div><div class="nm">Nina</div><div class="fr">Cusco 🇵🇪</div></div>
        <div class="pc tu"><div class="avw">{TU}</div><div class="nm">Tú</div><div class="fr">Flandes 🇧🇪</div></div>
      </div>
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila de la casa</span><br><span class="gloss" style="font-size:8.5pt">In Cartagena vul je je rugzak met de woorden van wonen: la casa, la habitación, el barrio, a la derecha, todo recto, ¡sigue!</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">describir tu casa</span> (habitaciones y muebles) <span class="nl">je huis & kamers beschrijven</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar <b>hay</b> y <b>estar</b></span> (hay un sofá · el sofá está…) <span class="nl">zeggen wat er is / waar iets staat</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">decir <b>dónde está</b></span> con preposiciones (encima de, al lado de…) <span class="nl">voorzetsels van plaats</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">decir qué pasa <b>ahora</b></span> con <b>estar + gerundio</b> <span class="nl">estoy cocinando (nu bezig)</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">explicar el camino</span> con el <b>imperativo</b> (gira, sigue, cruza) <span class="nl">de weg uitleggen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">presentar <b>tu barrio</b></span> (plano + rondleiding) <span class="nl">je buurt voorstellen (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>Hay / estar</span><span><b>§2</b>Preposiciones</span><span><b>§3</b>Estar + gerundio</span><span><b>§4</b>El camino (imperativo)</span><span><b>§5</b>Ordinales</span><span><b>§6</b>Lectura</span><span><b>Taller</b>Diptongo/hiato</span><span><b>Cultura</b>La plaza y el barrio</span><span><b>Tarea</b>Mapa de mi barrio</span><span><b>Repaso</b>Semáforo</span>
    </div>
  </div>
  <div class="se" style="margin-top:8mm">Cómo trabajar esta unidad · leeswijzer</div>
  <div class="fams" style="margin-top:2mm">
    <div class="pcard"><div class="t" style="font-size:10.5pt">Las etiquetas de cada actividad</div>
      <div class="ej" style="margin-top:2mm"><span class="badge skill">👂 Escuchar</span> <span class="badge skill">🎙️ Hablar</span> <span class="badge skill">🔍 Analizar</span> <span class="badge">👤 Solo</span> <span class="badge">👥 En parejas</span> <span class="badge">± 5 min</span> <span class="stars">★★☆</span></div>
      <div class="anchor gloss" style="margin-top:2mm">Elke oefening toont de <b>vaardigheid</b>, de <b>werkvorm</b>, de <b>tijd</b> en de <b>moeilijkheid</b>.</div></div>
    <div class="pcard"><div class="t" style="font-size:10.5pt">El apoyo baja poco a poco</div>
      <div class="ej" style="margin-top:2mm"><span class="steun">Modelo</span> → <span class="steun">Banco</span> → <span class="steun">Marco</span> → <span class="steun">Pista</span> → <span class="steun">Sin ayuda</span></div>
      <div class="anchor gloss" style="margin-top:2mm">De <b>steun bouwt af</b>: van model naar zónder hulp. Zo produceer je écht zelf.</div></div>
  </div>
  <div class="fams" style="margin-top:4mm">
    <div class="pcard"><div class="t" style="font-size:10.5pt">Dos capas de color</div>
      <div class="ej" style="margin-top:2mm"><b>1 · groen</b> = de cursus/unit. <b>2 · función</b>: <span class="fx per">persoon</span> <span class="fx vb">werkwoord</span> <span class="fx ob">voorwerp</span> <span class="fx ti">tijd</span> <span class="fx pl">plaats</span> <span style="color:var(--red);font-weight:700">🔴 valstrik</span>.</div>
      <div class="anchor gloss" style="margin-top:2mm">Kleur is <b>nooit</b> de enige drager — altijd óók label of vorm.</div></div>
    <div class="pcard"><div class="t" style="font-size:10.5pt">Papel + pantalla</div>
      <div class="ej" style="margin-top:2mm">📄 el libro · 🎮 la <b>página digital</b> (spellen, audio, flip cards) · 📊 el PowerPoint. De <b>QR</b>-codes brengen je naar de juiste online-oefening.</div>
      <div class="anchor gloss" style="margin-top:2mm">Print werkt <b>volledig zonder</b> scherm; het <b>repaso</b> staat online.</div></div>
  </div>
</div>
''')

# ---------- §0 Ponte al día ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">0</span><span class="pk">§0 · ¡Ponte al día!</span>')
P('<div class="intro"><b>ES:</b> Antes de entrar en casa, recordamos lo que necesitas hoy: los <b>números</b> (los pisos), el <b>presente</b>, <b>ser/estar</b> básico y las <b>comidas</b> de la unidad anterior (U5). <span class="gloss">Voor we het huis binnengaan: getallen, presente, ser/estar en de vorige woordenschat ophalen.</span></div>')
P(lpd(("7","woordenschat inzetten"), ("8","presente & ser/estar ophalen"), ("9","strategieën / lengua de clase")))
P('</div>')
P('<p style="font-size:9.6pt">① <b>¿Qué tienes ya en la mochila?</b> Drie clusters die je vandaag inzet. <span class="gloss">Wat zit er al in je rugzak? woordmuur ophalen.</span></p>')
P(clusters([
  ("🔢","Números (U0)",["primero → primer","segundo · tercero","cuatro · cinco pisos"],"Voor de verdiepingen."),
  ("🔤","Presente (U1/U3)",["yo vivo · tú vives","nosotros comemos","¿dónde vives?"],"De vormen die je al kent."),
  ("📍","Ser / estar (U1)",["soy de Bélgica","¿dónde está?","está aquí / allí"],"Wie & waar."),
]))
P(actx(1, "Calentamiento: ¿dónde vives?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Zeg drie dingen over waar je woont (casa/piso · ciudad · con quién). Je buur noteert. Wissel.</p>'
  '<p style="margin-left:12.5mm">Modelo: <i>«Vivo en una casa en Brujas, con mi familia.»</i><br>Mi compañero/a vive: <span class="wl full"></span></p>', apoyo="Modelo"))
P(actx(2, "Números: los pisos del edificio",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Schrijf het rangtelwoord voluit (¿en qué piso?).</p>'
  '<table class="mp"><thead><tr><th>Piso</th><th>En letras</th></tr></thead><tbody>'
  '<tr><td>1º</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>2º</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>3º</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="Pista: het rangtelwoord eindigt op -o"))
P(actx(3, "Presente: conjuga «vivir»",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Vul de vorm van <b>vivir</b> in.</p>'
  '<p style="margin-left:12.5mm">yo <span class="wl sm"></span> · tú <span class="wl sm"></span> · él <span class="wl sm"></span> · nosotros <span class="wl sm"></span> · ellos <span class="wl sm"></span></p>', apoyo="Pista: viv-o…"))
P(actx(4, "Empareja: la comida con el lugar (U5→U7)",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>¿Dónde?</th><th></th><th>¿Qué compras / haces?</th></tr></thead><tbody>'
  '<tr><td>1 · la panadería</td><td><span class="wl sm"></span></td><td>A · sacar dinero</td></tr>'
  '<tr><td>2 · el supermercado</td><td><span class="wl sm"></span></td><td>B · comprar pan</td></tr>'
  '<tr><td>3 · el banco</td><td><span class="wl sm"></span></td><td>C · comprar comida</td></tr></tbody></table>', apoyo="Banco de palabras"))
P(actx(5, "Mi ciudad en presente",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf twee ware zinnen: één met <b>vivo</b> en één met <b>hay</b> (en mi ciudad hay…).</p>'
  '<div class="wbox sm"></div>', apoyo="Marco: Vivo en… / En mi ciudad hay…"))
P(actx(6, "Verdadero para mí",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Zet ✔ als het klopt, ✘ als niet. Verbeter er één met een presente-zin.</p>'
  '<p style="margin-left:12.5mm">☐ Vivo en un piso. &nbsp; ☐ Mi barrio es tranquilo. &nbsp; ☐ Hay un parque cerca.<br>Mi corrección: <span class="wl full"></span></p>', apoyo="Modelo"))
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> números, presente en ser/estar básico met zelfcorrectie op de digitale pagina.</div>')
P('</div>')  # close §0

# ================= §1 · HAY / ESTAR =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">1</span><span class="pk">§1 · Hay / estar · er is · waar het staat</span>')
P('<div class="route-note">📍 Parada 7 · Cartagena — Valen te abre la puerta: «Mira, en el salón hay un sofá».</div>')
P('<div class="intro"><b>ES:</b> Con <b>hay</b> dices <b>qué existe</b> (algo nuevo, sin artículo definido); con <b>estar</b> dices <b>dónde está</b> (algo conocido, la posición). La ruta: contexto → observar → regla → practicar → comunicar. <span class="gloss">hay = er is/zijn (iets nieuws); estar = waar iets staat (iets bekends).</span></div>')
P(lpd(("8","taalsysteem: hay/estar contrast"), ("7","woordenschat: casa/habitaciones"), ("3","doelgericht schrijven met steun"), ("4","mondelinge interactie")))
P('</div>')
# §1.1 observar via contextkaarten
P('<h3 style="margin-top:6mm">§1.1 · Hay o está — descubre el contraste</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto.</b> Valen te muestra su salón. Kijk naar <b>hay</b> en <b>está</b>. <span class="gloss">Let op het lidwoord en de plaats.</span></p>')
P('<div class="chat">'
  '<div class="chatline you"><div class="bub">En mi salón <span class="fx ob">hay</span> un sofá y una mesa.</div><div class="who">Valen</div></div>'
  '<div class="chatline me"><div class="bub">¿Y dónde <span class="fx vb">está</span> la tele?</div><div class="who">Tú</div></div>'
  '<div class="chatline you"><div class="bub">La tele <span class="fx vb">está</span> <span class="fx pl">al lado</span> del sofá. Y <span class="fx ob">hay</span> muchas plantas.</div><div class="who">Valen</div></div></div>')
P('<p style="font-size:9.6pt">② <b>Las contextkaarten — dos usos:</b></p>')
P('<div class="fams" style="margin-top:2mm">')
P(pcard("① HAY — ¿qué existe?", '<div class="ej"><b>hay</b> + un/una/dos/muchos… (of niets).<br><i>Hay <b>un</b> parque.</i><br><i>Hay <b>dos</b> baños.</i><br><i>Hay plantas.</i></div><div class="t2">🔴 Nooit met el/la: niet «hay el parque».</div>'))
P(pcard("② ESTAR — ¿dónde está?", '<div class="ej"><b>está / están</b> + plaats.<br><i><b>El</b> parque <b>está</b> cerca.</i><br><i>Los baños <b>están</b> arriba.</i></div><div class="t2">🔴 Met el/la (iets bekends) + una preposición.</div>'))
P('</div>')
P(obsbox([
  'En el barrio <span class="hl">hay</span> una plaza. <span class="gloss">(er is een plein — nieuw)</span>',
  '<span class="hl">La</span> plaza <span class="hl">está</span> en el centro. <span class="gloss">(het plein staat/ligt… — bekend)</span>',
  '<span class="hl">Hay</span> tres tiendas. · Las tiendas <span class="hl">están</span> aquí. <span class="gloss">(hay + aantal · están + plaats)</span>',
], vragen='<b>1)</b> Wanneer «hay»? <b>2)</b> Wanneer «está/están»? <b>3)</b> Welk gebruikt een lidwoord de (el/la)?'))
P('<p style="font-size:9.6pt">③ <b>La máquina de decisión:</b></p>')
P(tree([
  '¿Introduces algo <b>nuevo</b> (con un/una/número/nada)? → <span class="yes">SÍ</span> → <span class="res">hay</span>',
  '¿Dices <b>dónde</b> está algo <b>conocido</b> (con el/la)? → <span class="yes">SÍ</span> → <span class="res">está / están</span>',
]))
P('</div>')  # page §1.1

# §1.2 práctica
P('<div class="page">')
P('<div class="divider">Practicar · §1.2</div>')
P(actx(1, "¿hay o está/están?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Kruis aan: <b>hay</b>, <b>está</b> of <b>están</b>.</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>hay</th><th>está</th><th>están</th></tr></thead><tbody>'
  '<tr><td>En el salón ___ un sofá.</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>El sofá ___ al lado de la ventana.</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ tres habitaciones.</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Los baños ___ arriba.</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>La cocina ___ a la derecha.</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="Modelo: regel §1.1 zichtbaar"))
P(actx(2, "Clasifica: ¿hay o estar?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Sorteer de zinsstukken: openen ze met <b>hay</b> (nieuw) of met <b>el/la … está</b> (bekend/plaats)? '
  '<span class="words"><b>un parque · el parque cerca · dos tiendas · la tienda en la esquina · muchas flores · el baño arriba</b></span></p>'
  + sortcols([("HAY + …","iets nieuws"),("EL/LA … ESTÁ","bekend + plaats")]), apoyo="Banco de palabras"))
P(actx(3, "Gap-fill: la casa de Valen",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul <b>hay</b>, <b>está</b> of <b>están</b> in.</p>'
  '<p style="margin-left:12.5mm">a) En mi casa ___ tres dormitorios. &nbsp; b) La cocina ___ al lado del comedor.<br>'
  'c) ___ un jardín detrás. &nbsp; d) Las sillas ___ en el comedor.<br>'
  'e) ___ una terraza grande. &nbsp; f) El baño ___ en el pasillo.<br><span class="gloss">✅ Zelfcorrectie op de digitale pagina.</span></p>', apoyo="Pista: nieuw→hay · plaats→está"))
P(audiorow('<div class="ic">🎧</div><div><b>Valen describe su barrio.</b> Escucha dos veces: 1ª ¿qué hay?, 2ª ¿dónde está? <span class="gloss">Luister twee keer en noteer.</span></div>',
           qr("Escanea y escucha", "Audio 7.1 · El barrio de Valen · 1:00", seed=71)))
P(actx(4, "Escucha: marca lo que hay",
  [{"t":"👂 Escuchar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Valen vertelt over haar barrio. Kruis aan wat er <b>is</b> en noteer <b>waar</b>.</p>'
  '<table class="mp"><thead><tr><th>¿Hay…?</th><th>☐ sí</th><th>¿Dónde está? (escribe)</th></tr></thead><tbody>'
  '<tr><td>una plaza</td><td>☐</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>un supermercado</td><td>☐</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>una farmacia</td><td>☐</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>un parque</td><td>☐</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="Modelo: twee keer beluisteren"))
P(actx(5, "Describe tu salón (5 cosas)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf vijf zinnen over jouw woonkamer: drie met <b>hay</b>, twee met <b>está/están</b>.</p>'
  '<div class="wbox sm"></div>', apoyo="Marco: En mi salón hay… / … está…"))
P(actx(6, "¿Es correcto? — ejemplo o no-ejemplo",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Kruis ✔ (goed) of ✘ (fout) aan en verbeter de foute.</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>✔ / ✘</th><th>Corrección</th></tr></thead><tbody>'
  '<tr><td>Hay el parque cerca.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>El baño está arriba.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Hay dos ventanas.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>La cocina hay a la derecha.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="Pista: nieuw/bekend"))
P(regla("Regla · hay / estar",
  '<p><b>hay</b> = er is/zijn. Voor iets <b>nieuws</b>: <b>hay</b> + un/una/dos/muchos… (of niets). Altijd dezelfde vorm. '
  '<b>estar</b> (está/están) = zeggen <b>waar</b> iets <b>bekends</b> (met el/la) staat: <i>El parque está cerca.</i> '
  '<br>🔴 Nooit «hay el/la…». 🔴 Meervoud: <i>hay dos baños</i> maar <i>los baños <b>están</b></i>.</p>'))
P(tarea_com("Tarea comunicativa · «Mi habitación»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b>Situación:</b> A beschrijft zijn/haar kamer (¿qué hay? ¿dónde está?), B tekent mee zonder te kijken. Vergelijk daarna. Wissel. <span class="gloss">«En mi habitación hay una cama. La cama está al lado de la ventana.»</span></p>'
  '<p style="margin-left:12.5mm">Mi habitación (3 cosas + dónde): <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Marco: hay… / … está…</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «¿hay o está?» (classify), «señala en la habitación» (point) en de casa-Memoria met zelfcorrectie.</div>')
P('</div>')  # page §1.2

retos("hay_estar", "§1.4 · Retos — lo que hay y donde está",
      'Un anuncio que <b>miente</b> tres veces, y la misma calle en <b>tres épocas</b>.',
      'Een advertentie die drie keer liegt, en dezelfde straat in drie tijdperken.')

# ================= §2 · PREPOSICIONES DE LUGAR =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2 · ¿Dónde está? · preposiciones de lugar</span>')
P('<div class="intro"><b>ES:</b> Para decir <b>dónde</b> está algo usas las <b>preposiciones de lugar</b>: encima de, debajo de, al lado de, entre… La ruta: escena → plano → regla → practicar → comunicar. <span class="gloss">Voorzetsels van plaats: waar staat iets precies?</span></div>')
P(lpd(("8","taalsysteem: preposiciones de lugar"), ("7","woordenschat: muebles/casa"), ("4","interactie: waar staat iets"), ("3","doelgericht schrijven")))
P('</div>')
# §2.1 escena + plano (stijl + GT-021)
P('<h3 style="margin-top:6mm">§2.1 · La habitación — ¿dónde está el gato?</h3>')
P('<p style="font-size:9.6pt">① <b>Observa la escena.</b> El gato está en sitios distintos. Kijk naar de <b>preposición</b>:</p>')
P('<div class="fichacard">'
  '<div><div class="row"><span class="k">encima de</span><span class="v">la mesa</span><span class="nl">boven op</span></div>'
  '<div class="row"><span class="k">debajo de</span><span class="v">la cama</span><span class="nl">onder</span></div>'
  '<div class="row"><span class="k">al lado de</span><span class="v">el sofá</span><span class="nl">naast</span></div>'
  '<div class="row"><span class="k">dentro de</span><span class="v">el armario</span><span class="nl">binnen in</span></div></div>'
  '<div><div class="row"><span class="k">delante de</span><span class="v">la puerta</span><span class="nl">vóór</span></div>'
  '<div class="row"><span class="k">detrás de</span><span class="v">la silla</span><span class="nl">achter</span></div>'
  '<div class="row"><span class="k">entre</span><span class="v">la mesa y la silla</span><span class="nl">tussen</span></div>'
  '<div class="row"><span class="k">enfrente de</span><span class="v">la ventana</span><span class="nl">tegenover</span></div></div></div>')
P('<div class="truc"><b>🔴 De + el = del:</b> encima <b>del</b> armario (niet <span class="trap">de el</span>). Bij <b>entre</b> gebruik je géén «de»: <i>entre la mesa <b>y</b> la silla</i>.</div>')
P('<p style="font-size:9.6pt">② <b>El plano del barrio (conceptmap) — ¿dónde está cada edificio?</b></p>')
P('<table class="conj"><thead><tr><th>Edificio</th><th>Preposición</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="v">la farmacia</td><td class="p">en la esquina</td><td>La farmacia está en la esquina.</td></tr>'
  '<tr><td class="v">el banco</td><td class="p">al lado de</td><td>El banco está al lado de la farmacia.</td></tr>'
  '<tr><td class="v">el cine</td><td class="p">entre … y …</td><td>El cine está entre el banco y el parque.</td></tr>'
  '<tr><td class="v">el museo</td><td class="p">enfrente de</td><td>El museo está enfrente de la iglesia.</td></tr></tbody></table>')
P(regla("Regla · preposiciones de lugar",
  '<p><b>encima de · debajo de · al lado de · delante de · detrás de · dentro de · enfrente de · cerca de · lejos de</b> + lugar. '
  '<b>entre</b> A <b>y</b> B (zonder «de»). <br>🔴 <b>de + el = del</b>: al lado <b>del</b> parque. Vorm van estar: <i>está</i> (ev.) / <i>están</i> (mv.).</p>'))
P('</div>')  # page §2.1

# §2.2 práctica
P('<div class="page">')
P('<div class="divider">Practicar · §2.2</div>')
P(actx(1, "¿Qué preposición? — mira la escena",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Kies de juiste preposición (kruis aan).</p>'
  '<table class="mp"><thead><tr><th>La lámpara está ___ la mesa</th><th>encima de</th><th>debajo de</th><th>entre</th></tr></thead><tbody>'
  '<tr><td>… (boven)</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>'
  '<table class="mp"><thead><tr><th>Frase</th><th>al lado de</th><th>detrás de</th><th>enfrente de</th></tr></thead><tbody>'
  '<tr><td>El jardín está ___ la casa (achter)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>El banco está ___ la farmacia (naast)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>El museo está ___ la iglesia (tegenover)</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="Modelo: ficha §2.1"))
P(actx(2, "Gap-fill: ¿dónde está el gato?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul de preposición in (let op <b>del</b>!).</p>'
  '<p style="margin-left:12.5mm">a) El gato está ___ la cama (onder). &nbsp; b) La ropa está ___ armario (binnen in).<br>'
  'c) El sofá está ___ la tele (tegenover). &nbsp; d) La mesa está ___ dos sillas (tussen).<br><span class="gloss">banco: debajo de · dentro del · enfrente de · entre</span></p>', apoyo="Banco de palabras"))
P(actx(3, "Empareja: preposición ↔ betekenis",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Español</th><th></th><th>Nederlands</th></tr></thead><tbody>'
  '<tr><td>1 · encima de</td><td><span class="wl sm"></span></td><td>A · onder</td></tr>'
  '<tr><td>2 · debajo de</td><td><span class="wl sm"></span></td><td>B · tussen</td></tr>'
  '<tr><td>3 · entre</td><td><span class="wl sm"></span></td><td>C · boven op</td></tr>'
  '<tr><td>4 · detrás de</td><td><span class="wl sm"></span></td><td>D · achter</td></tr></tbody></table>', apoyo="Banco de palabras"))
P(actx(4, "Transforma: cambia la posición",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Herschrijf de zin met de <b>tegengestelde</b> preposición.</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>Al contrario</th></tr></thead><tbody>'
  '<tr><td>El libro está encima de la mesa.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>El parque está cerca de mi casa.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>El coche está delante de la casa.</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="Pista: encima↔debajo · cerca↔lejos · delante↔detrás"))
P(actx(5, "Dictado: mi habitación",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Schrijf de vier zinnen (mueble + preposición + plaats), één per regel.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl lg"></span> 2. <span class="wl lg"></span><br>'
  '3. <span class="wl lg"></span> 4. <span class="wl lg"></span></p>', apoyo="Modelo: twee keer beluisteren"))
P(actx(6, "Escribe: mi barrio en un plano",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Teken een mini-plattegrond (4 gebouwen) en schrijf drie zinnen: waar staat wat.</p>'
  '<div class="wbox"></div>', apoyo="Marco: … está al lado de… / entre… y…"))
P(tarea_com("Tarea comunicativa · «¿Dónde está?»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 7 min"},{"t":"★★★"}],
  '<p><b>Situación:</b> A verstopt een voorwerp in zijn plattegrond, B raadt met vragen (¿Está debajo de…? ¿al lado de…?). Wissel. <span class="gloss">«—¿Está detrás del sofá? —No. —¿Al lado de la ventana? —¡Sí!»</span></p>'
  '<p style="margin-left:12.5mm">Mi pregunta ganadora: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Marco: ¿Está … de …?</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «preposición de lugar» (cloze), «señala en el plano del barrio» (point) en de preposiciones-Tetris.</div>')
P('</div>')  # page §2.2

retos("preposiciones", "§2.4 · Retos — el espacio dicho en voz alta",
      'Una mudanza <b>a ciegas</b> y una audioguía de tu propia calle. Aquí «ahí» no existe.',
      'Een verhuis op de tast en een audiogids van je eigen straat. «Daar» bestaat hier niet.')

# ================= §3 · ESTAR + GERUNDIO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3 · Estoy cocinando · estar + gerundio</span>')
P('<div class="intro"><b>ES:</b> Para decir qué pasa <b>ahora, en este momento</b>, usas <b>estar + gerundio</b> (estoy cocinando). La ruta: línea del tiempo → máquina → regla → practicar → comunicar. <span class="gloss">Om te zeggen wat er nú aan de hand is: estar + gerundio (het -ing).</span></div>')
P(lpd(("8","taalsysteem: estar + gerundio (presente continuo)"), ("4","interactie: ¿qué estás haciendo?"), ("3","doelgericht spreken")))
P('</div>')
# §3.1 tijdlijn + machine
P('<h3 style="margin-top:6mm">§3.1 · La máquina «estar + gerundio»</h3>')
P('<p style="font-size:9.6pt">① <b>La línea del tiempo — ¿cuándo?</b> El gerundio es para <b>ahora mismo</b>:</p>')
P(scale(["antes","hoy","ahora, en este momento ✓","luego"]))
P('<p style="font-size:9.6pt">② <b>La máquina.</b> Neem <b>estar</b> (presente) + het werkwoord met de gerundio-uitgang:</p>')
P(machine([("persona","yo"),("estar (presente)","estoy"),("raíz","cocin"),("+ terminación",'<span class="end">-ando</span>'),("frase","estoy cocinando")]))
P('<p style="font-size:9.6pt">③ <b>La terminación del gerundio (uitgangswissel):</b></p>')
P('<div class="fams" style="margin-top:2mm">')
P(pcard("estar (presente)", '<table class="conj"><tbody>'
  '<tr><td class="p">yo</td><td class="v">estoy</td></tr>'
  '<tr><td class="p">tú</td><td class="v">estás</td></tr>'
  '<tr><td class="p">él/ella</td><td class="v">está</td></tr>'
  '<tr><td class="p">nosotros</td><td class="v">estamos</td></tr>'
  '<tr><td class="p">vosotros</td><td class="v">estáis</td></tr>'
  '<tr><td class="p">ellos</td><td class="v">están</td></tr></tbody></table>'))
P(pcard("El gerundio", '<div class="ej"><b>-ar</b> → <b class="fx vb">-ando</b>: cocin<b>ar</b> → cocin<b>ando</b><br>'
  '<b>-er</b> → <b class="fx vb">-iendo</b>: com<b>er</b> → com<b>iendo</b><br>'
  '<b>-ir</b> → <b class="fx vb">-iendo</b>: escrib<b>ir</b> → escrib<b>iendo</b></div>'
  '<div class="t2">🔴 leer → le<b>y</b>endo · dormir → d<b>u</b>rmiendo (pas op).</div>'))
P('</div>')
P('<p style="font-size:9.6pt">④ <b>Como bloques (bouwstroken).</b> Kies één blok uit elke rij:</p>')
P(blocks([
  [("per","(Yo) estoy"),("vb","cocinando"),("opt","en la cocina")],
  [("per","(Tú) estás"),("vb","comiendo"),("opt","en el comedor")],
  [("per","(Nosotros) estamos"),("vb","viendo la tele"),("opt","en el salón")],
  [("per","(Ellos) están"),("vb","durmiendo"),("opt","en el dormitorio")],
]))
P(regla("Regla · estar + gerundio",
  '<p><b>estar</b> in het presente (estoy, estás, está, <b>estamos</b>, estáis, están) + <b>gerundio</b> (-ando / -iendo). '
  'Je gebruikt het voor wat <b>nu</b> gebeurt: <i>¿Qué estás haciendo? — Estoy estudiando.</i> '
  '<br>🔴 Twee delen: <b>estar</b> (vervoegd) + gerundio (onveranderd). 🔴 -ar→-ando, -er/-ir→-iendo.</p>'))
P('</div>')  # page §3.1

# §3.2 práctica + CLOZE (verplicht)
P('<div class="page">')
P('<div class="divider">Practicar · §3.2</div>')
P(actx(1, "Forma el gerundio",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Schrijf de gerundio (-ando / -iendo).</p>'
  '<p style="margin-left:12.5mm">hablar → <span class="wl sm"></span> · comer → <span class="wl sm"></span> · vivir → <span class="wl sm"></span> · estudiar → <span class="wl sm"></span> · beber → <span class="wl sm"></span></p>', apoyo="Pista: -ar→-ando · -er/-ir→-iendo"))
P(actx(2, "Substitutie: cambia la persona",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Herschrijf <b>«estoy cocinando»</b> voor elke persoon (verander alleen <b>estar</b>).</p>'
  '<table class="mp"><thead><tr><th>Persona</th><th>… cocinando</th></tr></thead><tbody>'
  '<tr><td>tú</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>nosotros</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>ella</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>ellos</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="Marco: tabla estar"))
P(actx(3, "Completa con estar + gerundio (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p>Vul <b>estar + gerundio</b> aan (werkwoord tussen haakjes). <span class="gloss">Let op: vorm van estar + gerundio.</span></p>'
  '<p style="margin-left:12.5mm">1. (Yo) <span class="wl md"></span> en la cocina. <i>(cocinar)</i><br>'
  '2. ¿(Tú) <span class="wl md"></span> la tele? <i>(ver)</i><br>'
  '3. (Nosotros) <span class="wl md"></span> en el comedor. <i>(comer)</i><br>'
  '4. Valen <span class="wl md"></span> una carta. <i>(escribir)</i><br>'
  '5. (Ellos) <span class="wl md"></span> en el dormitorio. <i>(dormir)</i><br>'
  '6. (Yo) <span class="wl md"></span> un libro en el salón. <i>(leer)</i><br>'
  '7. ¿(Vosotros) <span class="wl md"></span> música? <i>(escuchar)</i><br>'
  '8. Mi madre <span class="wl md"></span> la casa. <i>(limpiar)</i></p>'
  '<p style="margin-left:12.5mm" class="gloss">✅ De oplossingen staan online (zelfcorrectie op de digitale pagina).</p>', apoyo="Pista: estar-vorm + gerundio"))
P(actx(4, "Empareja: habitación ↔ acción",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Welke actie past bij de kamer? Verbind (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Habitación</th><th></th><th>Acción</th></tr></thead><tbody>'
  '<tr><td>1 · la cocina</td><td><span class="wl sm"></span></td><td>A · está durmiendo</td></tr>'
  '<tr><td>2 · el dormitorio</td><td><span class="wl sm"></span></td><td>B · está cocinando</td></tr>'
  '<tr><td>3 · el baño</td><td><span class="wl sm"></span></td><td>C · está viendo la tele</td></tr>'
  '<tr><td>4 · el salón</td><td><span class="wl sm"></span></td><td>D · está duchándose</td></tr></tbody></table>', apoyo="Banco de palabras"))
P(actx(5, "¿Qué estás haciendo? — escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf drie zinnen: wat jij, je vriend en je familie <b>nu</b> aan het doen zijn (estar + gerundio).</p>'
  '<div class="wbox sm"></div>', apoyo="Marco: Estoy… / Está… / Estamos…"))
P(tarea_com("Tarea comunicativa · «¿Qué están haciendo?»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 7 min"},{"t":"★★★"}],
  '<p><b>Situación:</b> A mimet een actie (cocinar, dormir, leer…), B raadt met <b>«¿Estás …ndo?»</b>. Wissel. Noteer één actie van je buur. <span class="gloss">«—¿Estás cocinando? —¡Sí, estoy cocinando!»</span></p>'
  '<p style="margin-left:12.5mm">Mi compañero/a está: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Marco: ¿Estás …ndo?</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «estar + gerundio» (cloze), «¿qué estás haciendo?» en de gerundio-drills met zelfcorrectie.</div>')
P('</div>')  # page §3.2

retos("gerundio", "§3.4 · Reto — ¿quién está haciendo qué?",
      'Seis ruidos en un piso de Cartagena. Cada uno delata una <b>acción</b>, no un objeto.',
      'Zes geluiden in een appartement in Cartagena. Elk verraadt een handeling, geen voorwerp.')

# ================= §4 · IMPERATIVO (EL CAMINO) =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4 · ¿Cómo se va? · el imperativo (el camino)</span>')
P('<div class="intro"><b>ES:</b> Para <b>explicar el camino</b> usas el <b>imperativo</b> (tú): <b>gira</b>, <b>sigue</b>, <b>cruza</b>, <b>toma</b>… La ruta: escena → árbol de decisión → regla → practicar → comunicar. <span class="gloss">De weg uitleggen met de gebiedende wijs: draai, ga door, steek over.</span></div>')
P(lpd(("8","taalsysteem: imperativo afirmativo (tú)"), ("4","interactie: de weg vragen/uitleggen"), ("1","luisteren naar instructies"), ("3","mondeling reageren")))
P('</div>')
# §4.1 handelingenreeks + beslisboom
P('<h3 style="margin-top:6mm">§4.1 · Las instrucciones del camino — observa</h3>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> instrucciones (la ruta)</span><span class="tm"><b>Voz:</b> tú (imperativo)</span><span class="tm">🎯 explicar el camino</span></div>')
P('<p style="font-size:9.6pt">① <b>Como una secuencia de acciones:</b></p>')
P(scale(["Sal de casa","Sigue todo recto","Gira a la derecha","Cruza el semáforo","¡Llegas a la plaza!"]))
P('<p style="font-size:9.6pt">② <b>El imperativo (tú) — la forma:</b></p>')
P('<table class="conj"><thead><tr><th>Infinitivo</th><th>Imperativo (tú)</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="p">girar</td><td class="v">gir<span class="end">a</span></td><td>Gira a la izquierda.</td></tr>'
  '<tr><td class="p">tomar</td><td class="v">tom<span class="end">a</span></td><td>Toma la primera calle.</td></tr>'
  '<tr><td class="p">cruzar</td><td class="v">cruz<span class="end">a</span></td><td>Cruza la plaza.</td></tr>'
  '<tr><td class="p">seguir</td><td class="v">sig<span class="end">ue</span></td><td>Sigue todo recto. <span class="trap">(e→i)</span></td></tr>'
  '<tr><td class="p">subir</td><td class="v">sub<span class="end">e</span></td><td>Sube por la escalera.</td></tr></tbody></table>')
P('<p style="font-size:9.6pt">③ <b>El árbol de decisión:</b></p>')
P(tree([
  '¿La plaza está lejos? → <span class="yes">SÍ</span> → <b>Toma</b> el autobús. → <span class="no">NO</span> → <b>Ve</b> a pie.',
  '¿A la derecha o a la izquierda? → <b>Gira</b> a la derecha en el semáforo.',
  '¿Ya llegaste? → <span class="yes">SÍ</span> → <span class="res">¡Estás en la plaza!</span>',
]))
P('<div class="truc"><b>🔴 Formas útiles:</b> <b>gira</b> (draai) · <b>sigue</b> (ga door) · <b>cruza</b> (steek over) · <b>toma/coge</b> (neem) · <b>ve</b> (ga, van «ir»). Bij een regelmatig <b>-ar</b>-werkwoord: eind op <b>-a</b>; bij <b>-er/-ir</b>: eind op <b>-e</b>.</div>')
P(regla("Regla · imperativo afirmativo (tú)",
  '<p>Voor een <b>bevel/instructie</b> aan <b>tú</b>: neem de <b>él/ella-vorm</b> van het presente. '
  '<b>-ar</b> → <b>-a</b> (gira, cruza, toma) · <b>-er/-ir</b> → <b>-e</b> (sube, sigue). '
  '<br>🔴 Onregelmatig: <b>ir → ve</b> · <b>seguir → sigue</b> (e→i). Zo leg je de weg uit.</p>'))
P('</div>')  # page §4.1

# §4.2 práctica
P('<div class="page">')
P('<div class="divider">Practicar · §4.2</div>')
P(actx(1, "Del infinitivo al imperativo",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Schrijf het imperativo (tú).</p>'
  '<p style="margin-left:12.5mm">girar → <span class="wl sm"></span> · cruzar → <span class="wl sm"></span> · seguir → <span class="wl sm"></span> · tomar → <span class="wl sm"></span> · subir → <span class="wl sm"></span></p>', apoyo="Pista: -ar→-a · -er/-ir→-e · seguir→sigue"))
P(actx(2, "Ordena las instrucciones (la ruta)",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Zet de route in de juiste volgorde.</p>'
  '<p style="margin-left:12.5mm">___ Cruza el semáforo. &nbsp; ___ Sal de casa. &nbsp; ___ Gira a la derecha.<br>'
  '___ Sigue todo recto por la calle Real. &nbsp; ___ La plaza está a la izquierda.</p>', apoyo="Banco de palabras: nummers 1–5"))
P(actx(3, "Completa el camino ",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het juiste imperativo in.</p>'
  '<p style="margin-left:12.5mm">Para ir a la panadería: ___ (seguir) todo recto, ___ (girar) a la izquierda y ___ (cruzar) la calle. La panadería está a la derecha.<br><span class="gloss">banco: sigue · gira · cruza</span></p>', apoyo="Banco de palabras"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha las indicaciones</b> y sigue el camino en tu plano. <span class="gloss">Markeer de weg op je plano.</span></div>',
           qr("Escanea y escucha", "Audio 7.2 · ¿Cómo se va? · 0:50", seed=72)))
P(actx(4, "Escucha: ¿adónde llegas?",
  [{"t":"👂 Escuchar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Volg de instructies. Waar kom je uit? Kruis aan.</p>'
  '<p style="margin-left:12.5mm">☐ la plaza &nbsp; ☐ el museo &nbsp; ☐ la estación &nbsp; ☐ el parque<br>Mi respuesta: <span class="wl md"></span></p>', apoyo="Modelo: plano gegeven"))
P(actx(5, "Escribe el camino a tu casa",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Leg uit hoe je van school naar jouw huis gaat (4–5 instructies, imperativo).</p>'
  '<div class="wbox sm"></div>', apoyo="Marco: Sal de… · Sigue… · Gira… · Cruza…"))
P(tarea_com("Tarea comunicativa · «¿Cómo se va a…?»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 9 min"},{"t":"★★★"}],
  '<p><b>Situación:</b> A vraagt de weg naar een plek in het barrio, B legt uit met imperativo. A volgt op het plano en controleert. Wissel van rol. <span class="gloss">«—Perdona, ¿cómo se va a la farmacia? —Sigue todo recto y gira a la derecha.»</span></p>'
  '<p style="margin-left:12.5mm">☐ vraag gesteld · ☐ sigue/gira/cruza gebruikt · ☐ bestemming klopt<br>Mijn instructie: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Marco: rollenkaart + plano</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «ordena las instrucciones», «imperativo (la ruta)» (cloze) en de simulatie «¡explica el camino!».</div>')
P('</div>')  # page §4.2

retos("imperativo", "§4.4 · Retos — dar órdenes que funcionen",
      'Un robot que lo toma todo <b>literalmente</b>, y dos vecinos que tienen los dos razón.',
      'Een robot die alles letterlijk neemt, en twee buren die allebei gelijk hebben.')

# ================= §5 · ORDINALES + APOCOPE =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">5</span><span class="pk">§5 · Los ordinales · primero → el primer piso</span>')
P('<div class="intro"><b>ES:</b> Los <b>números ordinales</b> (primero, segundo, tercero…) dicen el <b>orden</b>. ¡Ojo con la <b>apócope</b>: primero → <b>el primer piso</b>. La ruta: observar → lupa → regla → practicar. <span class="gloss">Rangtelwoorden + de apocope (primero valt weg tot primer vóór een m. zn.).</span></div>')
P(lpd(("8","taalsysteem: ordinales + apócope"), ("7","woordenschat: la casa/los pisos"), ("3","doelgericht schrijven")))
P('</div>')
P('<h3 style="margin-top:6mm">§5.1 · Los ordinales y la apócope</h3>')
P('<p style="font-size:9.6pt">① <b>Observa el edificio:</b></p>')
P('<table class="conj"><thead><tr><th>Nº</th><th>Ordinal</th><th>Apócope (+ m. sing.)</th></tr></thead><tbody>'
  '<tr><td>1º</td><td class="v">primero</td><td>el <b class="end">primer</b> piso</td></tr>'
  '<tr><td>2º</td><td class="v">segundo</td><td>el segundo piso</td></tr>'
  '<tr><td>3º</td><td class="v">tercero</td><td>el <b class="end">tercer</b> piso</td></tr>'
  '<tr><td>4º</td><td class="v">cuarto</td><td>el cuarto piso</td></tr>'
  '<tr><td>5º</td><td class="v">quinto</td><td>el quinto piso</td></tr></tbody></table>')
P('<p style="font-size:9.6pt">② <b>La lupa (foutenvergrootglas) — solo primero y tercero pierden la -o:</b></p>')
P(zoom("primero + piso", "el primer piso", "primera + planta", "la primera planta"))
P('<div class="truc"><b>🔴 Apócope:</b> <b>primero → primer</b> · <b>tercero → tercer</b> — enkel vóór een <b>mannelijk enkelvoud</b> zelfstandig naamwoord. Bij vrouwelijk blijft het: <i>la primer<b>a</b> planta</i>. De rest verandert niet: <i>el segundo piso</i>.</div>')
P(regla("Regla · ordinales + apócope",
  '<p><b>primero, segundo, tercero, cuarto, quinto…</b> = de volgorde. '
  '<b>primero</b> en <b>tercero</b> verliezen de <b>-o</b> vóór een mannelijk enkelvoud: <b>el primer piso</b>, <b>el tercer piso</b>. '
  '<br>🔴 Vrouwelijk = geen apocope: <i>la primera vez</i>. Andere blijven gelijk: <i>el segundo, el cuarto</i>.</p>'))
P('</div>')  # page §5.1
P('<div class="page">')
P('<div class="divider">Practicar · §5.2</div>')
P(actx(1, "¿primero o primer?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Kies de juiste vorm.</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>primero</th><th>primer</th><th>primera</th></tr></thead><tbody>'
  '<tr><td>el ___ piso</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>la ___ calle</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Vivo en el ___ (kort)</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="Modelo: regel §5.1"))
P(actx(2, "Gap-fill: los ordinales",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het juiste ordinaal in (let op de apocope).</p>'
  '<p style="margin-left:12.5mm">a) Vivo en el ___ (3º) piso. &nbsp; b) La farmacia está en la ___ (1ª) calle.<br>'
  'c) El ascensor va al ___ (5º) piso. &nbsp; d) Es mi ___ (1º) día en Cartagena.<br><span class="gloss">✅ Zelfcorrectie op de digitale pagina.</span></p>', apoyo="Pista: m. sing → apocope"))
P(actx(3, "Empareja: número ↔ ordinal",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Nº</th><th></th><th>Ordinal</th></tr></thead><tbody>'
  '<tr><td>1 · 2º</td><td><span class="wl sm"></span></td><td>A · cuarto</td></tr>'
  '<tr><td>2 · 4º</td><td><span class="wl sm"></span></td><td>B · segundo</td></tr>'
  '<tr><td>3 · 3º</td><td><span class="wl sm"></span></td><td>C · quinto</td></tr>'
  '<tr><td>4 · 5º</td><td><span class="wl sm"></span></td><td>D · tercero</td></tr></tbody></table>', apoyo="Banco de palabras"))
P(actx(4, "Escribe: ¿en qué piso vives?",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf twee zinnen met een ordinaal (¿en qué piso? · ¿cuál es tu primer plato favorito?). Zeg ze hardop.</p>'
  '<div class="wbox sm"></div>', apoyo="Marco: Vivo en el… piso"))
P('<div class="route-note">🎮 <b>Juega online:</b> «primero o primer» en de ordinales-drills met zelfcorrectie.</div>')
P('</div>')  # page §5.2

retos("ordinales", "§5.4 · Reto — el primer, el segundo, el tercer",
      'Guías a alguien que <b>no ve</b> el edificio. Solo cuenta lo que se puede contar o tocar.',
      'Je gidst iemand die het gebouw niet ziet. Alleen wat je kunt tellen of voelen telt.')

# ================= §6 · LECTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">📖</span><span class="pk">§6 · Lectura 1 — «Un paseo por Cartagena»</span>')
P('<div class="intro"><b>ES:</b> Vas a leer un <b>anuncio de piso</b> y un pequeño <b>texto</b> sobre el barrio de Valen. Primero <b>predices</b> desde la imagen, después lees con un <b>objetivo</b>. <span class="gloss">Je leest een woningadvertentie en een tekst over Valens buurt: eerst voorspellen, dan doelgericht lezen.</span></div>')
P(lpd(("1","onderwerp/hoofdgedachte bij lezen"), ("2","relevante info selecteren"), ("3","doelgericht schrijven met steun")))
P('</div>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> anuncio (piso) · texto (barrio)</span><span class="tm"><b>De:</b> Valen · Cartagena</span><span class="tm">🎯 seleccionar información</span></div>')
P(actx(1, "Antes de leer: predice",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★☆☆"}],
  '<p>Bekijk de vorm van een <b>anuncio de piso</b>. ¿Qué información esperas encontrar?</p>'
  '<p style="margin-left:12.5mm">Espero leer sobre: <span class="wl full"></span></p>', apoyo="Modelo: habitaciones, precio, dónde…"))
P('<div class="ptexts">'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["valen"]}</div><div><div class="nm">Se alquila piso</div><div class="fr">anuncio · Cartagena</div></div></div>'
  '<p><b>Bonito piso en el <span class="evi">centro</span>.</b> <span class="evi">Tercer piso</span> con ascensor. Tiene <span class="evi">dos habitaciones</span>, un <span class="evi">salón</span> grande, <span class="evi">cocina</span> y <span class="evi">baño</span>. Hay una <span class="evi">terraza</span> con vistas a la plaza. Está <span class="evi">cerca de</span> la panadería y del parque. <span class="evi">600 € al mes</span>.</p></div>'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["valen"]}</div><div><div class="nm">Valen · mi barrio</div><div class="fr">texto · costeña</div></div></div>'
  '<p>Vivo en un barrio de <span class="evi">casas de colores</span>. Enfrente de mi casa <span class="evi">hay</span> una <span class="evi">plaza</span> con palmeras. La <span class="evi">panadería está al lado</span> y el mar <span class="evi">está cerca</span>. Por la tarde, la gente <span class="evi">está paseando</span> y los niños <span class="evi">están jugando</span>. ¡Me encanta mi barrio!</p></div></div>')
P('<div class="lecdoel">🎯 <b>Objetivo de lectura:</b> lees om te <b>selecteren</b> welke kamers het piso heeft en <b>waar</b> alles staat in Valens barrio — je hoeft niet élk woord te begrijpen.</div>')
P('</div>')  # page §6a
P('<div class="page">')
P(actx(2, "Escanea: completa la ficha del piso",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Zoek de gegevens in het anuncio.</p>'
  '<table class="mp"><thead><tr><th>Dato</th><th>Respuesta</th></tr></thead><tbody>'
  '<tr><td>Piso (¿qué número?)</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Nº de habitaciones</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>¿Tiene terraza?</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Precio al mes</td><td><span class="wl md"></span></td></tr>'
  '</tbody></table>', apoyo="Modelo: anuncio boven"))
P(actx(3, "¿Verdadero o falso? + prueba",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Waar of niet waar? Noteer de <b>woorden uit de tekst</b> die het bewijzen.</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba</th></tr></thead><tbody>'
  '<tr><td>El piso está en la planta baja.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Enfrente de la casa de Valen hay una plaza.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>La panadería está lejos.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Los niños están jugando en el barrio.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '</tbody></table>', apoyo="Pista: onderstreep in de tekst"))
P(actx(4, "Del contexto: ¿qué significa?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Wat betekent <b>«se alquila»</b> en <b>«vistas a la plaza»</b>? Kies + leg uit welke aanwijzing hielp.</p>'
  '<p style="margin-left:12.5mm">se alquila = ☐ te huur ☐ te koop &nbsp;·&nbsp; vistas a la plaza = ☐ uitzicht op het plein ☐ dichtbij het plein<br>Pista que me ayudó: <span class="wl lg"></span></p>', apoyo="Pista"))
P(tarea_com("Tarea comunicativa · «Se alquila» (keten lezen→spreken)",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b></b> A is de <b>propietario/a</b> en beschrijft een woning (habitaciones, dónde está, precio); B is de <b>cliente</b> en stelt vragen (¿Cuántas habitaciones hay? ¿Dónde está?). Wissel. <span class="gloss">«Es un piso en el segundo. Hay dos habitaciones y está cerca del parque.»</span></p>'
  '<div class="wbox sm"></div>'
  '<div class="steun" style="margin-left:0mm">Marco: Hay… · … está… · cuesta…</div>'))
P('<div class="route-note">🎮 <b>Sigue online:</b> luister het anuncio (TTS), lees de tekst en neem je beschrijving op (recorder) op de digitale pagina.</div>')
P('</div>')  # page §6b

# ================= TALLER DE LENGUA =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num" style="color:var(--crema)">✎</span><span class="pk" style="background:var(--gd)">Taller de lengua</span>')
P('<div class="intro"><b>ES:</b> Dos herramientas: los <b>conectores de lugar</b> (a la derecha, al final de la calle, enfrente…) y la <b>ortografía</b> de los <b>diptongos e hiatos</b> (panadería, día, país). <span class="gloss">Plaats-conectoren + spelling van tweeklanken/hiaten.</span></div>')
P(lpd(("8","taalsysteem: conectoren + ortografía"), ("3","tekst structureren")))
P('</div>')
P('<h3 style="margin-top:6mm">Conectores de lugar · para explicar dónde y cómo llegar</h3>')
P('<p style="font-size:9.6pt">① <b>Para una ruta / una descripción:</b></p>')
P(colloc("¿dónde?", ["a la derecha","a la izquierda","todo recto","al final de la calle","en la esquina","enfrente de","al lado de"]))
P('<table class="mp"><thead><tr><th>Conector</th><th>Uso</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td><b>todo recto</b></td><td>richting</td><td>Sigue <b>todo recto</b>.</td></tr>'
  '<tr><td><b>a la derecha / izquierda</b></td><td>afslaan</td><td>Gira <b>a la derecha</b>.</td></tr>'
  '<tr><td><b>al final de la calle</b></td><td>plaats</td><td>La plaza está <b>al final de la calle</b>.</td></tr></tbody></table>')
P(actx(1, "Une la ruta con conectores",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het juiste verbindingswoord in (todo recto / a la derecha / al final de / enfrente de).</p>'
  '<p style="margin-left:12.5mm">Sigue ___ por la calle Real. Gira ___ en el semáforo. La panadería está ___ la calle, ___ la plaza.<br><span class="wl full"></span></p>', apoyo="Banco de palabras"))
P('<h3 style="margin-top:6mm">Ortografía · diptongos e hiatos (la regla del sombrero)</h3>')
P('<div class="truc"><b>🔴 Diptongo vs. hiato:</b> een <b>diptongo</b> = twee klinkers in één lettergreep (b<b>ai</b>le, p<b>ue</b>rta). Een <b>hiato</b> = twee klinkers apart, vaak met tilde: pana-de-r<b>í</b>-a, d<b>í</b>-a, pa-<b>í</b>s. De tilde op de <b>i/u</b> breekt de tweeklank.</div>')
P(obsbox([
  '<span class="hl">diptongo</span>: puerta · bueno · tiene · seis <span class="gloss">(twee klinkers = één klank)</span>',
  '<span class="hl">hiato</span>: pana<b>de</b>ría · día · país · frío <span class="gloss">(tilde op í = apart)</span>',
], vragen='<b>1)</b> Waar staat de tilde in «panadería»? <b>2)</b> Diptongo of hiato: «puerta»?'))
P(actx(2, "¿Diptongo o hiato?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Sorteer de woorden. '
  '<span class="words"><b>día · puerta · país · bueno · panadería · seis</b></span></p>'
  + sortcols([("diptongo","één lettergreep"),("hiato (con tilde)","apart")], eigen=False), apoyo="Banco de palabras"))
P(actx(3, "Dictado corto del barrio",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Escucha y escribe cuatro palabras (con tilde donde toca).</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl md"></span> 2. <span class="wl md"></span> 3. <span class="wl md"></span> 4. <span class="wl md"></span></p>', apoyo="Modelo: 2×"))
P(actx(4, "Corrige la descripción",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Zoek de fout (conector, hay/está, preposición of tilde) en herschrijf correct.</p>'
  '<p style="margin-left:12.5mm">1) <span class="trap">Hay el parque al lado de mi casa.</span> → <span class="wl lg"></span><br>'
  '2) <span class="trap">La farmacia esta a la derecha.</span> → <span class="wl lg"></span><br>'
  '3) <span class="trap">Voy a la panaderia todos los dias.</span> → <span class="wl lg"></span></p>', apoyo="Modelo"))
P(actx(5, "Escribe: describe tu calle (5 líneas)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Schrijf 5 zinnen over jouw straat: gebruik <b>hay</b>, <b>está</b>, twee <b>preposiciones</b> en één <b>conector de lugar</b>.</p>'
  '<div class="wbox sm"></div>', apoyo=""))
P(actx(6, "Pon la tilde donde toca",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Zet de tilde op de juiste plaats (of laat weg als het een diptongo is). Herschrijf.</p>'
  '<table class="mp"><thead><tr><th>Palabra</th><th>Con/sin tilde</th><th>¿diptongo o hiato?</th></tr></thead><tbody>'
  '<tr><td>panaderia</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>puerta</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>pais</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>bueno</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>', apoyo="Pista: tilde op í = hiato"))
P(tarea_com("Tarea comunicativa · «Dame indicaciones»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p><b>Situación:</b> beschrijf mondeling de weg van de klas naar een plek in de school/stad met <b>conectores de lugar</b> (todo recto · a la derecha · al final de…). Je buur tekent en controleert. <span class="gloss">«Sal de clase, gira a la derecha y sigue todo recto.»</span></p>'
  '<p style="margin-left:12.5mm">Mi ruta (3 pasos): <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Banco de palabras: conectores</div>'))
P('<div class="route-note">🎮 <b>Practica online:</b> «diptongo o hiato» en de conectoren-oefeningen met zelfcorrectie.</div>')
P('</div>')  # page Taller

# ================= LECTURA 2 · ESCUCHA =================
# Zelfde bron als de digitale hub (lectura_data / escucha_data): papier en scherm
# kunnen zo niet uit elkaar lopen. Elk op een eigen bladzijde (§14).
P('<div class="page"><div class="parada sec">')
P('<span class="num">7</span><span class="pk">§7 · Lectura 2 — «Se alquila apartamento en el centro»</span>')
P('<div class="intro"><b>ES:</b> Un anuncio de alquiler de verdad, con el plano descrito. <b>No hace falta entenderlo todo</b> para sacar la información. <span class="gloss">Een echte huuradvertentie waarin de plattegrond beschreven wordt. Je hoeft niet alles te begrijpen — teken in je hoofd mee.</span></div>')
P(PB.lectura_print(LD.C5_U7, "1"))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">8</span><span class="pk">§8 · Escucha — «La visita al piso»</span>')
P('<div class="intro"><b>ES:</b> Sam y su madre visitan el piso y no todo es como en el anuncio. <b>Escucha primero, escribe después.</b> <span class="gloss">Sam en zijn moeder bezoeken het appartement en niet alles klopt met de advertentie. Eerst luisteren, dan schrijven; het transcript staat online en gaat pas open ná de taken.</span></div>')
P(PB.escucha_print(ED.C5_U7, "1"))
P('</div>')

# ================= CULTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">★</span><span class="pk">Cultura · La plaza y el barrio</span>')
P('<div class="intro"><b>ES:</b> En el mundo hispano, la <b>plaza</b> es el corazón del <b>barrio</b>: la gente pasea, charla y se encuentra. Descubre Cartagena, las <b>casas de colores</b> y cómo se vive (casa · piso · apartamento). <span class="gloss">Het plein is het hart van de wijk. Ontdek Cartagena en het wonen in de Spaanstalige wereld.</span></div>')
P(lpd(("5","kenmerkende aspecten van de cultuur"), ("2","relevante info uit een tekst")))
P('</div>')
P('<div class="fams" style="margin-top:6mm">')
P(pcard("🏛️ La plaza 🇨🇴", '<div class="ej">La <b>plaza</b> es el centro del barrio: hay bancos, árboles y una <b>iglesia</b>. Por la tarde la gente <b>está paseando</b> y charlando. En Cartagena, la <b>Plaza de los Coches</b> es famosa.</div><div class="anchor gloss">La plaza = de ontmoetingsplek van de buurt.</div>'))
P(pcard("🏘️ Las casas de colores", '<div class="ej">Cartagena tiene un <b>casco histórico</b> con casas de <b>colores</b> vivos y <b>balcones con flores</b>. Las murallas protegen la ciudad frente al mar Caribe.</div><div class="t2">Barrio Getsemaní = arte, música y color.</div>'))
P('</div>')
P('<p style="font-size:9.6pt">① <b>¿Cómo se vive? — casa · piso · apartamento (contraste):</b></p>')
P('<table class="mp"><thead><tr><th>Palabra</th><th>🇪🇸 España</th><th>🇨🇴 / 🌎 América</th><th>🇧🇪 Bélgica</th></tr></thead><tbody>'
  '<tr><td>vivienda urbana</td><td>el piso</td><td>el apartamento</td><td>het appartement</td></tr>'
  '<tr><td>vivienda con jardín</td><td>el chalet</td><td>la casa</td><td>het huis</td></tr>'
  '<tr><td>planta a nivel de calle</td><td>la planta baja</td><td>la planta baja</td><td>gelijkvloers</td></tr></tbody></table>')
P('<div class="truc"><b>🟡 Dato:</b> in Spanje zegt men meestal <b>piso</b>, in Latijns-Amerika <b>apartamento</b>. Bij het adres komt vaak het <b>piso</b> erbij: <i>calle Real, 3º</i> (tercer piso).</div>')
P('<p style="font-size:9.6pt">② <b>Un lugar por país (pan-hispano):</b></p>')
P(vpairs([("la Plaza Mayor 🇪🇸","la plaza de Cartagena 🇨🇴"),("el Zócalo 🇲🇽","la Plaza de Armas 🇵🇪"),("el barrio Getsemaní 🇨🇴","el barrio de La Boca 🇦🇷")]))
P(actx(1, "Comprensión — verdadero o falso",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Waar of niet waar? Verbeter de foute.</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Corrección</th></tr></thead><tbody>'
  '<tr><td>La plaza es el centro del barrio.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>En España se dice «apartamento».</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Cartagena tiene casas de colores.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="Modelo: tekst boven"))
P(actx(2, "Mi plaza / mi barrio",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Schrijf 2–3 zinnen over een plein of buurt bij jou (¿qué hay? ¿dónde está? ¿qué haces ahí?). Presenteer aan je buur.</p>'
  '<div class="wbox sm"></div>', apoyo="Marco: En mi barrio hay… · … está…"))
P(actx(3, "Empareja: lugar ↔ país",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind de bekende plek met het land (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Lugar</th><th></th><th>País</th></tr></thead><tbody>'
  '<tr><td>1 · el Zócalo</td><td><span class="wl sm"></span></td><td>A · Colombia 🇨🇴</td></tr>'
  '<tr><td>2 · Getsemaní</td><td><span class="wl sm"></span></td><td>B · España 🇪🇸</td></tr>'
  '<tr><td>3 · la Plaza Mayor</td><td><span class="wl sm"></span></td><td>C · México 🇲🇽</td></tr>'
  '<tr><td>4 · la Plaza de Armas</td><td><span class="wl sm"></span></td><td>D · Perú 🇵🇪</td></tr></tbody></table>', apoyo="Banco de palabras"))
P('<div class="route-note">🎮 <b>Sigue online:</b> «lugar ↔ país» (match) en de barrio-spellen op de digitale pagina.</div>')
P('</div>')  # page Cultura

retos("cultura_u7", "Retos — el barrio que construyes tú",
      'Doce puntos para un barrio entero, y una casa del futuro <b>sin futuro</b>.',
      'Twaalf punten voor een hele wijk, en een huis van de toekomst zonder toekomende tijd.')

# ================= TAREA FINAL =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num">✦</span><span class="pk" style="background:var(--gd)">Tarea final · Mapa de mi barrio</span>')
P('<div class="intro"><b>ES:</b> Crea el <b>plano de tu barrio</b> (o de un barrio ideal) y da una <b>visita guiada</b>: di qué <b>hay</b>, dónde <b>está</b> cada cosa y <b>explica el camino</b> de tu casa a la plaza. <span class="gloss">Maak de plattegrond van je buurt en geef een rondleiding + de weg.</span></div>')
P('<div class="route-note">🎯 <b>Communicatieve taak:</b> afzender = jij (de gids) · ontvanger = een bezoeker/nieuwe leerling · doel = je buurt voorstellen & de weg uitleggen · situatie = un paseo por el barrio · resultaat = ingevuld plano + gespeelde rondleiding.</div>')
P(lpd(("3","doelgericht schrijven met een voorbeeld"), ("4","mondeling interageren (de weg)"), ("7","woordenschat casa/barrio"), ("8","hay/estar · preposiciones · imperativo")))
P('</div>')
P('<ol class="pasos">'
  '<li><b>Dibuja el plano</b> de tu barrio (calles, plaza, tiendas, tu casa) op het raster hieronder.</li>'
  '<li><b>Escribe 5 frases</b>: qué <b>hay</b> en tu barrio y dónde <b>está</b> cada cosa (met preposiciones).</li>'
  '<li><b>Escribe el camino</b> de tu casa a la plaza (imperativo: sigue, gira, cruza).</li>'
  '<li><b>Da la visita guiada</b> en pareja (of neem audio op via de digitale pagina).</li>'
  '<li><b>Responde</b> a las preguntas del visitante («¿Dónde está la farmacia?»).</li></ol>')
P('<div class="se" style="margin-top:4mm">El plano de mi barrio <span class="gloss" style="font-size:8pt">· teken je buurt</span></div>')
P('<div class="wbox lg"></div>')
P('<div class="se" style="margin-top:5mm">Mi barrio en 5 frases <span class="gloss" style="font-size:8pt">· hay / está + preposiciones</span></div>')
P('<table class="alf"><thead><tr><th>#</th><th>Frase</th></tr></thead><tbody>'
  '<tr><td>1</td><td><span class="wl full" style="margin:0"></span></td></tr>'
  '<tr><td>2</td><td><span class="wl full" style="margin:0"></span></td></tr>'
  '<tr><td>3</td><td><span class="wl full" style="margin:0"></span></td></tr>'
  '<tr><td>4</td><td><span class="wl full" style="margin:0"></span></td></tr>'
  '<tr><td>5</td><td><span class="wl full" style="margin:0"></span></td></tr></tbody></table>')
P('<div class="se" style="margin-top:5mm">El camino de mi casa a la plaza <span class="gloss" style="font-size:8pt">· imperativo</span></div><div class="wbox sm"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba la visita guiada</b> en la página digital (recorder + rúbrica).</div>',
           qr("Escanea y graba", "Tarea · Mapa de mi barrio", seed=74)))
P('<div class="se" style="margin-top:5mm">Mini-encuesta: ¿qué hay en el barrio de la clase? <span class="gloss" style="font-size:8pt">— vraag 5 klasgenoten, teken de balken</span></div>')
P(gustobars([("un parque", 60), ("una panadería", 50), ("una plaza", 40), ("un cine", 20)]))
P('<p style="font-size:8.6pt" class="gloss">↳ vervang de voorbeeld-balken door je eigen resultaten (aantal /5 → %).</p>')
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Mijn plano heeft <b>5+ lugares</b> met namen</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>hay</b> én <b>está/están</b> correct</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>preposiciones</b> (al lado de, entre…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik leg <b>de weg</b> uit met imperativo (gira, sigue…)</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — el barrio de mi compañero/a</div>'
  '<table><thead><tr><th>Lo que me gusta de su barrio</th><th>Un consejo (una cosa)</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('</div>')  # page Tarea

# ================= REPASO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">✓</span><span class="pk">Repaso · lo esencial</span>')
P('<div class="intro"><b>ES:</b> Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag.</span></div>')
P('</div>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>Hay / estar:</b> <b>hay</b> + un/una/número (nieuw, geen «el/la») · <b>el/la … está/están</b> + plaats (bekend).</li>'
  '<li><b>Preposiciones de lugar:</b> encima de · debajo de · al lado de · entre A y B · delante/detrás de · dentro de · enfrente de (de + el = <b>del</b>).</li>'
  '<li><b>Estar + gerundio:</b> estoy/estás/está… + <b>-ando</b> (-ar) / <b>-iendo</b> (-er/-ir): <i>Estoy cocinando.</i></li>'
  '<li><b>Imperativo (el camino):</b> gir<b>a</b> · sigu<b>e</b> · cruz<b>a</b> · tom<b>a</b> · <b>ve</b> (ir). -ar→-a · -er/-ir→-e.</li>'
  '<li><b>Ordinales:</b> primero → <b>el primer</b> piso · tercero → <b>el tercer</b> piso (apocope, m. sing.).</li>'
  '<li><b>Las trampas:</b> 🔴 niet «hay el parque» · 🔴 de + el = del · 🔴 estoy comi<b>e</b>ndo · 🔴 el primer piso · 🔴 hiato panader<b>í</b>a.</li></ul></div>')
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> spelletjes met zelfcorrectie op de digitale pagina.</div>')
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td>mijn <b>casa</b> beschrijven (habitaciones, muebles)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>hay</b> en <b>estar</b> juist gebruiken</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>zeggen <b>waar</b> iets staat (preposiciones)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>zeggen wat er <b>nu</b> gebeurt (estar + gerundio)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>de <b>weg uitleggen</b> (imperativo)</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil de U7: <span class="wl md"></span> · Lo más difícil: <span class="wl md"></span></i></div>')
P('<div class="bridge"><b>» Siguiente parada: Perú — Cusco y Machu Picchu (U8).</b> Ya sabes describir tu barrio; en <b>U8 «¿Qué has hecho?»</b> viajas y cuentas lo que <b>has hecho</b> con el pretérito perfecto. <span class="gloss">In U8 reis je en vertel je wat je (net) gedaan hebt.</span></div>')
P('</div>')  # page Repaso

# ================= §V VOCABULARIO =================
import json as _json
VOC = _json.load(open(f"{HERE}/u7_vocab.json", encoding="utf-8"))
GRP = [("casa","La casa · exterior e interior"),("habitaciones","Las habitaciones"),("muebles","Los muebles"),
       ("barrio","El barrio · la ciudad"),("direcciones","Direcciones · el camino"),("transporte","El transporte"),
       ("preposiciones","Preposiciones de lugar")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (begrijpen en zelf gebruiken)")))
P('</div>')
P('<p style="font-size:9.6pt">La <b>casa y el barrio</b> als netwerk — drie families die de hele unit dragen:</p>')
P(clusters([
  ("🏠","Dentro de casa",["el salón · la cocina · el baño","la mesa · la cama · el sofá","la puerta · la ventana"],"Waar je woont."),
  ("🏘️","En el barrio",["la plaza · la calle","la panadería · el banco","el parque · el supermercado"],"Wat er in de buurt is."),
  ("🧭","El camino",["a la derecha · a la izquierda","todo recto · la esquina","gira · sigue · cruza"],"Hoe je de weg vindt."),
]))
for key, titel in GRP:
    items = [v for v in VOC if v.get("grp") == key]
    if not items: continue
    P(f'<h3 style="margin-top:6mm">{titel} <span class="gloss" style="font-size:8pt">· {len(items)} woorden</span></h3>')
    rows = "".join(f'<tr><td><b>{v["es"]}</b></td><td>{v["nl"]}</td><td class="gloss">{v["soort"]}</td><td class="gloss">{v["ej"]}</td></tr>' for v in items)
    P(f'<table class="alf"><thead><tr><th>Español</th><th>Nederlands</th><th>ERK/soort</th><th>Ejemplo</th></tr></thead><tbody>{rows}</tbody></table>')
# print-oefenladder V.1-V.5
P('<div class="divider">Escalera de práctica · V.1–V.5</div>')
P(actx("V.1", "Reconocer — ES → NL",
  [{"t":"🔍 Leer","skill":True},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Schrijf de vertaling. el dormitorio = <span class="wl md"></span> · la plaza = <span class="wl md"></span> · al lado de = <span class="wl md"></span> · el ascensor = <span class="wl md"></span></p>', apoyo="Modelo"))
P(actx("V.2", "Distinguir — sorteer per familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Sorteer: <span class="words"><b>la cocina · el parque · el sofá · la panadería · la cama · la plaza</b></span></p>'
  + sortcols([("habitación/mueble",""),("edificio del barrio",""),("lugar público","")], eigen=False), apoyo="Banco de palabras"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het Spaanse woord aan (beginletter gegeven). de keuken = <b>c</b>___ · het plein = <b>p</b>___ · rechts = <b>a</b> la <b>d</b>___ · onder = <b>d</b>___ de<br><span class="wl full"></span></p>', apoyo="Primera letra"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Maak één correcte zin met <b>hay · al lado de · plaza</b>.</p><div class="wbox sm"></div>', apoyo=""))
P(actx("V.5", "Comunicar — mi casa ideal",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Schrijf jouw ideale huis (habitaciones + muebles) met <b>hay</b> en <b>está</b>, en zeg waar alles staat. Zeg het daarna hardop tegen je buur.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>', apoyo="Marco: En mi casa hay… · … está…"))
P(mispal("Mis palabras de la unidad", 4))
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Sigue en la página digital:</span> <span class="g">flip cards (ES↔NL), audio en de spellen bouwen de steun verder af.</span></div></div>')
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
 var SEL='h1,h2,h3,h4,p,td,th,li,.intro,.hist,.gloss,.ojo,.anchor,.ej,.q,.sub,.route-note,.pk,.se,.divider,.t,.t2,.nl,.es,.lpdchip,.lpdlab,.wcol .ch,.bub,.k,.v,.ln,.mq,.ma,.br,.blk,.clu li,.node,.mi,.mt,.sec2';
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
   a.href=URL.createObjectURL(blob); a.download='U7_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Español en la práctica · U7 Mi casa y mi barrio</title><style>'
        + CSS + PB.CSS + RP.CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/U7.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes")
