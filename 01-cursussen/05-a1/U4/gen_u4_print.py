#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de print-HTML U4.html (C5 · Unidad 4 «Me gusta») → PDF via Chromium.
# Zelfde componentenkit/pijplijn als golden sample U0/U1 (cursus-print.css). Fonts base64 ingebed,
# cast-avatars inline SVG (cast_gen). Cursuskleur = groen (C5). Output = standalone bewerkbare U4.html.
import os, sys, base64
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f"{ROOT}/02-huisstijl/beeld/generators")
import cast_gen as C
import sys as _sys
_sys.path.insert(0, "/home/user/espa-ol-en-la-pr-ctica/03-build/web")
import qr_print as QRP; QRP.fijar("C5", 4)
import print_bloques as PB
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

# ---------- CSS: identiek aan golden sample U0/U1 (cursus-print.css + schrijf-componenten) ----------
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
/* ===== Banda sonora (parel) ===== */
.banda{ display:grid; grid-template-columns:1fr 1fr; gap:4mm; margin:4mm 0; }
.bard{ border:1px solid var(--line); border-left:4px solid var(--g); border-radius:12pt; padding:3.4mm 4.5mm; background:#fff; break-inside:avoid; }
.bard .bh{ display:flex; justify-content:space-between; align-items:baseline; gap:2mm; }
.bard .bn{ font-family:var(--disp); font-weight:800; font-size:12pt; color:var(--gd); }
.bard .bflag{ font-size:8pt; color:var(--mut); font-weight:600; }
.bard .bsong{ font-size:8.8pt; color:var(--ww); font-weight:700; margin:.4mm 0 1.6mm; }
.bard .bbio{ font-size:8.9pt; margin:0; line-height:1.42; } .bard .bbio .gloss{ display:block; margin-top:.6mm; }
.perla{ margin:4mm 0; border:1.5px solid var(--g); border-radius:12pt; padding:4mm 5mm; background:var(--gt); break-inside:avoid; }
.perla .pt{ font-family:var(--disp); font-weight:700; color:var(--gd); font-size:11pt; }
.perla .pt small{ font-family:var(--body); font-weight:400; color:var(--mut); font-size:8pt; }
.perla .steps2{ display:grid; grid-template-columns:repeat(4,1fr); gap:2.5mm; margin-top:3mm; align-items:stretch; }
.perla .st2{ border-radius:9pt; padding:2.6mm 2mm; text-align:center; color:#fff; }
.perla .st2 .ex{ font-family:var(--dispx); font-weight:800; font-size:11pt; display:block; }
.perla .st2 .nl2{ font-size:7.4pt; opacity:.95; display:block; margin-top:.6mm; }
.perla .arrow2{ text-align:center; font-size:8pt; color:var(--gd); font-weight:700; margin-top:2mm; letter-spacing:.05em; }
"""

# ---------------- component-helpers (identiek aan U1) ----------------
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
def pcard(t, body): return f'<div class="pcard"><div class="t">{t}</div>{body}</div>'

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


def steun(niveau):
    return (f'<div class="steun" style="margin-left:12.5mm">{niveau}</div>' if niveau else '')

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
    # rows = [(label, pct)]
    inner = "".join(f'<div class="gbar"><span>{lab}</span><div class="track2"><div class="fill" style="width:{p}%"></div><span class="pct">{p}%</span></div></div>' for lab, p in rows)
    return f'<div class="gustobars">{inner}</div>'

def banda(cards):
    # cards = [(nombre, flag, cancion, bio_html)]
    out = []
    for nm, flag, song, bio in cards:
        out.append(f'<div class="bard"><div class="bh"><span class="bn">{nm}</span><span class="bflag">{flag}</span></div>'
                   f'<div class="bsong">🎵 {song}</div><div class="bbio">{bio}</div></div>')
    return f'<div class="banda">{"".join(out)}</div>'

def perla_scale(stops):
    # stops = [(color, ejemplo_es, nl)] van odio (rood) → me encanta (groen)
    cols = "".join(f'<div class="st2" style="background:{c}"><span class="ex">{es}</span><span class="nl2">{nl}</span></div>' for c, es, nl in stops)
    return ('<div class="perla"><div class="pt">🎚️ La escala del gusto <small>· de Rosalía «La Perla»: de «odio» a «me encanta»</small></div>'
            f'<div class="steps2">{cols}</div>'
            '<div class="arrow2">◄ menos ——————————————— más ►</div></div>')

# ================= BODY =================
BODY = []
def P(*x): BODY.extend(x)

# ---------- OPENER ----------
P(f'''
<div class="hero">
  <div class="tab">U4 · ME GUSTA</div>
  <div class="eyebrow">UNIDAD 4 · LA RUTA · PARADA 4 — VALÈNCIA / LA COSTA 🇪🇸</div>
  <h1>Me gusta</h1>
  <div class="sub">Llegamos a <b>València</b>, junto al mar. Hoy hablas de tus <b>gustos</b>: música, deportes, cine, planes. <span class="gloss">We komen aan in València, aan zee. Vandaag praat je over je smaak: muziek, sport, film, plannen.</span></div>
  <div class="q">¿Qué te gusta hacer en tu tiempo libre? <span style="font-weight:400;opacity:.9">· Wat doe je graag in je vrije tijd?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U1 · Madrid</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U2 · Sevilla</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U3 · Barcelona</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U4 · València</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U5 · México</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U6–U8 · América</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 4 · València, la costa.</b> Bij de zee spreek je over wat je <b>leuk</b> vindt en wat je <b>wil doen</b>. Met <b>Lucía</b> en haar valenciaanse vriendin <b>Bea</b> maak je plannen. <span class="gloss">Aan de kust praat je over je smaak en over afspreken.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> En <b>València</b> hace sol. Lucía y <b>Bea</b> te preguntan: «¿Qué te <b>gusta</b>?». Aprendes a decir lo que te <b>gusta</b> y lo que te <b>encanta</b> (música, deportes, cine), a estar de <b>acuerdo</b> o no, y a <b>proponer un plan</b>: «¿<b>Quieres</b> ir a la playa?».
      <span class="gloss">In València schijnt de zon. Lucía en Bea vragen: «Wat vind jij leuk?». Je leert zeggen wat je leuk/geweldig vindt, akkoord gaan of niet, en een plan voorstellen.</span></div>
      <div class="ojo"><b>¡Ojo! — de grote valstrik:</b> <b>gustar</b> werkt <i>omgekeerd</i>. Je zegt niet «ik vind X leuk», maar <b>«X bevalt mij»</b>: <b>Me gusta</b> la música (= de muziek bevalt mij). Meervoud → <b>gusta<span class="trap">n</span></b>: <b>Me gustan</b> los deportes.</div>
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
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila de gustos</span><br><span class="gloss" style="font-size:8.5pt">In València vul je je rugzak met de woorden van jouw smaak: sport, muziek, film, planes.</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">decir qué te gusta</span> (con <b>gustar</b> / <b>encantar</b>) <span class="nl">zeggen wat je leuk/geweldig vindt</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar los pronombres</span> me/te/le/nos/os/les <span class="nl">de OI-voornaamwoorden gebruiken</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">estar de acuerdo o no</span> (también/tampoco · a mí sí/no) <span class="nl">akkoord gaan of niet</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">proponer un plan</span> (querer/poder + infinitivo · quedar) <span class="nl">een plan voorstellen & afspreken</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">justificar tu opinión</span> con <b>porque</b> <span class="nl">je mening motiveren</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">crear tu <b>playlist</b></span> y presentarla <span class="nl">je playlist maken (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>Me gusta(n)</span><span><b>§2</b>También/tampoco</span><span><b>§3</b>Quiero/puedo + quedar</span><span><b>§4</b>Lectura</span><span><b>Taller</b>Opinión/conect.</span><span><b>Cultura</b>Ocio & banda sonora</span><span><b>Tarea</b>Mi playlist</span><span><b>Repaso</b>Semáforo</span>
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
      <div class="ej" style="margin-top:2mm">📄 el libro · 🎮 la <b>página digital</b> (20 spellen, audio, flip cards) · 📊 el PowerPoint. De <b>QR</b>-codes brengen je naar de juiste online-oefening.</div>
      <div class="anchor gloss" style="margin-top:2mm">Print werkt <b>volledig zonder</b> scherm; het <b>repaso</b> staat online.</div></div>
  </div>
</div>
''')

# ---------- §0 Ponte al día ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">0</span><span class="pk">§0 · ¡Ponte al día!</span>')
P('<div class="intro"><b>ES:</b> Antes de hablar de gustos, recordamos lo que ya sabes y que necesitas hoy: los <b>verbos en presente</b>, las <b>actividades</b> del tiempo libre y los <b>adverbios de frecuencia</b>. <span class="gloss">Voor we over smaak praten: kort ophalen — presente, vrijetijdsactiviteiten en frequentie.</span></div>')
P(lpd(("7","woordenschat inzetten"), ("8","presente ophalen"), ("9","strategieën / lengua de clase")))
P('</div>')
P('<p style="font-size:9.6pt">① <b>¿Qué tienes ya en la mochila?</b> Drie clusters die je vandaag inzet. <span class="gloss">Wat zit er al in je rugzak?</span></p>')
P(clusters([
  ("🏃","Actividades",["nadar · bailar","jugar · leer","escuchar música"],"Wat je doet in je vrije tijd."),
  ("🔁","Frecuencia",["siempre · a menudo","a veces · nunca","todos los días"],"Hoe vaak."),
  ("🔤","Presente (U1)",["yo hablo · tú hablas","nosotros vivimos","ellos escuchan"],"De vormen die je al kent."),
]))
P(actx(1, "Calentamiento: ¿qué haces en tu tiempo libre?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Zeg drie activiteiten die je doet, met een frequentiewoord. Je buur noteert. Wissel.</p>'
  '<p style="margin-left:12.5mm">Modelo: <i>«A veces juego a videojuegos.»</i><br>Mi compañero/a hace: <span class="wl full"></span></p>', apoyo="Modelo"))
P(actx(2, "Conjuga en presente (repaso)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Vul de juiste presente-vorm in (regelmatig, uit U1).</p>'
  '<table class="mp"><thead><tr><th>Infinitivo</th><th>yo</th><th>tú</th><th>nosotros</th></tr></thead><tbody>'
  '<tr><td>escuchar</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>leer</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>vivir</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>', apoyo="Pista: uitgang -o/-as/-amos…"))
P(actx(3, "Ordena por frecuencia",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Zet de woorden op een lijn van <b>nunca</b> (0%) naar <b>siempre</b> (100%).</p>'
  + scale(["nunca","casi nunca","a veces","a menudo","siempre"]) +
  '<p style="margin-left:12.5mm">Schrijf de volgorde met een woord dat ontbreekt: <span class="wl full"></span></p>', apoyo="Modelo: lijn gegeven"))
P(actx(4, "Empareja la actividad con el lugar",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind de activiteit met de logische plaats (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Actividad</th><th></th><th>Lugar</th></tr></thead><tbody>'
  '<tr><td>1 · nadar</td><td><span class="wl sm"></span></td><td>A · el cine</td></tr>'
  '<tr><td>2 · ver una película</td><td><span class="wl sm"></span></td><td>B · la playa / el mar</td></tr>'
  '<tr><td>3 · jugar al fútbol</td><td><span class="wl sm"></span></td><td>C · el campo / el parque</td></tr></tbody></table>', apoyo="Banco de palabras"))
P(actx(5, "Mi semana en presente",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf twee ware zinnen: één met <b>a veces</b> en één met <b>todos los días</b>.</p>'
  '<div class="wbox sm"></div>', apoyo="Marco: frecuentia + presente"))
P(actx(6, "Verdadero para mí",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Zet ✔ als het klopt voor jou, ✘ als niet. Verbeter er één met een presente-zin.</p>'
  '<p style="margin-left:12.5mm">☐ Nado a menudo. &nbsp; ☐ Escucho música todos los días. &nbsp; ☐ Nunca leo.<br>Mi corrección: <span class="wl full"></span></p>', apoyo="Modelo"))
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> presente, actividades en frecuentie met zelfcorrectie op de digitale pagina.</div>')
P('</div>')  # close page

# ================= §1 · ME GUSTA(N) + ENCANTAR =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">1</span><span class="pk">§1 · Me gusta(n) · gustar & encantar</span>')
P('<div class="route-note">📍 Parada 4 · València — Lucía y Bea te preguntan qué te gusta.</div>')
P('<div class="intro"><b>ES:</b> Primero <b>descubres</b> cómo funciona <i>gustar</i> (¡al revés!), después usas los <b>pronombres</b> y la <b>concordancia</b> gusta/gustan para hablar de ti. <span class="gloss">Eerst ontdek je hoe «gustar» werkt (omgekeerd!), dan de voornaamwoorden en gusta/gustan.</span></div>')
P(lpd(("8","taalsysteem: gustar + OI + concordancia"), ("7","woordenschat: ocio/gustos"), ("3","doelgericht schrijven met steun"), ("4","mondelinge interactie")))
P('</div>')
# §1.1 — de omgekeerde constructie ontdekken
P('<h3 style="margin-top:6mm">§1.1 · La construcción al revés — observa</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto.</b> Bea chat met jou over muziek. Kijk <b>hoe</b> ze «leuk vinden» zegt. <span class="gloss">Let op de vorm van gustar.</span></p>')
P('<div class="chat">'
  '<div class="chatline you"><div class="bub">¡Hola! ¿Te gusta la música?</div><div class="who">Bea</div></div>'
  '<div class="chatline me"><div class="bub">Sí, <span class="fx vb">me gusta</span> mucho la música. Y <span class="fx vb">me gustan</span> los conciertos.</div><div class="who">Tú</div></div>'
  '<div class="chatline you"><div class="bub">A mí me encanta bailar. ¿Y a ti?</div><div class="who">Bea</div></div>'
  '<div class="chatline me"><div class="bub">A mí <span class="fx vb">me gusta</span> nadar, pero no <span class="fx vb">me gustan</span> los deportes de equipo.</div><div class="who">Tú</div></div></div>')
P('<p style="font-size:9.6pt">② <b>Radiografía — «het bevalt mij».</b> In het Spaans is <b>lo que te gusta</b> het <i>onderwerp</i>, en <b>jij</b> bent het meewerkend voorwerp (me/te/le…):</p>')
P(xray('<span class="fx ob">A mí</span> <span class="fx per">me</span> <span class="fx vb">gusta</span> <span class="fx pl">la música</span>.',
       [("A mí me","aan míj (OI)"),("gusta","3ª pers. — bevalt"),("la música","= het onderwerp!")]))
P('<div class="truc"><b>🔴 NL ↔ ES:</b> «<i>Ik</i> vind muziek leuk» → in het Spaans staat het om: «<i>De muziek</i> bevalt <i>mij</i>» = <b>Me gusta la música</b>. Het werkwoord past zich aan bij <b>het ding</b>, niet bij «ik».</div>')
P(obsbox([
  '<span class="fx per">Me</span> <span class="hl">gusta</span> el fútbol. <span class="gloss">(één ding → gusta)</span>',
  '<span class="fx per">Me</span> <span class="hl">gustan</span> los deportes. <span class="gloss">(meerdere dingen → gustan)</span>',
  '<span class="fx per">Me</span> <span class="hl">gusta</span> bailar. <span class="gloss">(een werkwoord → gusta)</span>',
], vragen='<b>1)</b> Wanneer gebruik je <i>gusta</i>? <b>2)</b> Wanneer <i>gustan</i>? <b>3)</b> Wat doet een infinitief (bailar)?'))
P('<p style="font-size:9.6pt">③ <b>Los pronombres — ¿a quién le gusta?</b> Voor élke persoon een ander OI-woord:</p>')
P('<table class="conj"><thead><tr><th>Persona</th><th>Pronombre OI</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="p">(a mí)</td><td class="v">me</td><td>Me gusta el mar.</td></tr>'
  '<tr><td class="p">(a ti)</td><td class="v">te</td><td>¿Te gusta bailar?</td></tr>'
  '<tr><td class="p">(a él/ella/usted)</td><td class="v">le</td><td>A Bea le gusta la playa.</td></tr>'
  '<tr><td class="p">(a nosotros/-as)</td><td class="v">nos</td><td>Nos gustan los conciertos.</td></tr>'
  '<tr><td class="p">(a vosotros/-as)</td><td class="v">os</td><td>¿Os gusta el cine?</td></tr>'
  '<tr><td class="p">(a ellos/-as/ustedes)</td><td class="v">les</td><td>Les gusta la música.</td></tr></tbody></table>')
P('</div>')  # page §1.1a

# §1.1b — herkennen → onderscheiden
P('<div class="page">')
P(actx(1, "¿gusta o gustan?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Kruis aan: één ding (<b>gusta</b>) of meerdere (<b>gustan</b>)?</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>gusta</th><th>gustan</th></tr></thead><tbody>'
  '<tr><td>Me ___ los videojuegos.</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Me ___ el fútbol.</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Me ___ nadar.</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Me ___ las series.</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Me ___ la playa.</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="Modelo: regel zichtbaar"))
P(actx(2, "Empareja el pronombre",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Verbind de persoon met het juiste OI-woord (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Persona</th><th></th><th>Pronombre</th></tr></thead><tbody>'
  '<tr><td>1 · a ti</td><td><span class="wl sm"></span></td><td>A · nos</td></tr>'
  '<tr><td>2 · a nosotros</td><td><span class="wl sm"></span></td><td>B · te</td></tr>'
  '<tr><td>3 · a ellos</td><td><span class="wl sm"></span></td><td>C · le</td></tr>'
  '<tr><td>4 · a ella</td><td><span class="wl sm"></span></td><td>D · les</td></tr></tbody></table>', apoyo="Banco de palabras"))
P(actx(3, "Clasifica: ¿por qué gusta o gustan?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Zet elk woord in de juiste kolom naargelang je <b>gusta</b> of <b>gustan</b> zou gebruiken. <span class="words"><b>el cine · los deportes · bailar · las canciones · la playa · los videojuegos · leer · las películas</b></span></p>'
  + sortcols([("gusta","+ ev. / infinitivo"),("gustan","+ mv.")]), apoyo="Banco de palabras"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha a tres jóvenes y anota qué les gusta.</b> <span class="gloss">Luister; noteer per persoon één gusto — selectief luisteren.</span></div>',
           qr("Escanea y escucha", "Audio 4.1 · Gustos · 0:55", seed=41)))
P(actx(4, "Marca el sujeto (¿qué le gusta?)",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Onderstreep <b>wat</b> bevalt (het echte onderwerp) en schrijf of het gusta of gustan vraagt.</p>'
  '<p style="margin-left:12.5mm">a) Me gustan los conciertos. → <span class="wl sm"></span><br>'
  'b) Me gusta la playa. → <span class="wl sm"></span><br>'
  'c) Me gusta escuchar música. → <span class="wl sm"></span></p>', apoyo="Pista: tel de dingen"))
P(mispal("Mis gustos — mis palabras", 3))
P('</div>')  # page §1.1b

# ---- §1.2 concordancia + encantar (bouwstroken → steiger → comunicar) ----
P('<div class="page">')
P('<div class="divider">Concordancia & encantar · §1.2</div>')
P('<h3>§1.2 · gusta / gustan / encanta(n) — construye</h3>')
P('<p style="font-size:9.6pt">① <b>El patrón como bloques.</b> Bouw je eigen zin: kies één blok uit elke rij (let op ev./mv.).</p>')
P(blocks([
  [("per","(A mí) me"),("vb","gusta"),("ob","la música")],
  [("per","(A mí) me"),("vb","gustan"),("ob","los deportes")],
  [("per","(A ti) te"),("vb","encanta"),("ob","bailar")],
  [("per","(A Bea) le"),("vb","encantan"),("ob","las playas")],
]))
P('<p style="font-size:9.6pt">② <b>La concordancia como una balanza.</b> Het werkwoord «weegt» mee met het onderwerp:</p>')
P('<div class="fams" style="margin-top:2mm"><div class="pcard"><div class="t" style="font-size:10pt">un ↔ muchos</div>'
  '<div class="agree"><div class="w">me gust<u>a</u> · el mar</div><div class="tie">1 ding / infinitivo → gusta</div>'
  '<div class="w" style="margin-top:2mm">me gust<u>an</u> · los mares</div><div class="tie">meerdere → gustan</div></div>'
  '</div><div class="pcard"><div class="t" style="font-size:10pt">gustar ↔ encantar</div>'
  + zoom("me gusta(n)","het bevalt / leuk","me encanta(n)","geweldig / dol op")
  + '</div></div>')
P(fmu('<b>me/te/le/nos/os/les</b> + <b>gusta</b> (ev./inf.) of <b>gustan</b> (mv.)<br><span class="gloss">encantar = idem, sterker</span>',
      'zeggen <b>wat</b> je (niet) leuk / geweldig vindt',
      '<i>Me gusta el cine. · Me gustan las series. · Me encanta bailar.</i>'))
P(regla("Regla · gustar & encantar",
  '<p><b>gusta</b> + één ding of een <b>infinitivo</b> · <b>gustan</b> + meerdere dingen. Zelfde met <b>encanta/encantan</b> (= sterker). '
  '<br>🔴 <b>Al revés:</b> me gusta <i>la música</i> = «de muziek bevalt mij». 🔴 Bij een <b>infinitief</b> altijd <b>gusta</b>: <i>me gusta bailar</i>. 🔴 Voor de naam mag <b>a + persoon</b>: <i>A Bea le gusta…</i>.</p>'))
P('</div>')  # page §1.2a

# §1.2b — steiger + oefeningen + cloze-verbo(gustar) + tarea
P('<div class="page">')
P('<p style="font-size:9.6pt">③ <b>De la copia a lo tuyo — la escalera.</b> De steun bouwt zichtbaar af:</p>')
P(scaffold([
  ("Modelo","«Me gustan los deportes y me encanta la música.»"),
  ("Marco","«Me gusta___ ___ y me encanta___ ___.»"),
  ("Clave","gusta/gustan · encanta/encantan"),
  ("Solo","Escribe tres gustos tuyos."),
]))
P(actx(4, "Completa: gusta o gustan",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Vul <b>gusta</b> of <b>gustan</b> in (let op ev./mv./infinitivo).</p>'
  '<p style="margin-left:12.5mm">a) Me ___ los videojuegos. &nbsp; b) Me ___ el cine. &nbsp; c) Me ___ nadar.<br>'
  'd) A Bea le ___ las canciones. &nbsp; e) Nos ___ la playa. &nbsp; f) ¿Te ___ los deportes?</p>', apoyo="Pista: tel de dingen)"))
P(actx(5, "Transforma con el pronombre correcto",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Herschrijf voor de nieuwe persoon (verander het OI-woord én let op gusta/gustan).</p>'
  '<table class="mp"><thead><tr><th>Modelo</th><th>Nieuwe persoon → jouw zin</th></tr></thead><tbody>'
  '<tr><td>Me gusta el mar.</td><td>(a ti) <span class="wl md"></span></td></tr>'
  '<tr><td>Me gustan las series.</td><td>(a nosotros) <span class="wl md"></span></td></tr>'
  '<tr><td>Me encanta bailar.</td><td>(a ella) <span class="wl md"></span></td></tr>'
  '<tr><td>Me gustan los conciertos.</td><td>(a ellos) <span class="wl md"></span></td></tr></tbody></table>', apoyo="Marco: OI-tabel)"))
P(actx(6, "Escribe tres gustos y un «no me gusta»",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>Schrijf drie dingen die je leuk/geweldig vindt en één dat je <b>niet</b> leuk vindt. Zeg ze daarna hardop.</p>'
  '<div class="wbox"></div>', apoyo="ronde 2 uit het hoofd"))
P(actx(7, "Encuesta rápida: gusta/gustan + tu opinión",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf per item een volledige zin met de juiste vorm (gusta/gustan) én jouw waarheid (+/–).</p>'
  '<table class="mp"><thead><tr><th>Tema</th><th>Tu frase (me gusta(n) / no me gusta(n))</th></tr></thead><tbody>'
  '<tr><td>los videojuegos</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>la música pop</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>bailar</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>las películas de terror</td><td><span class="wl lg"></span></td></tr></tbody></table>', apoyo="Marco"))
P(tarea_com("Tarea comunicativa · «Encuentra un gusto en común»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 Toda la clase"},{"t":"± 10 min"},{"t":"★★★"}],
  '<p><b>Situación:</b> jij loopt rond en zoekt per rij iemand met dezelfde smaak, en <b>rapporteert</b> daarna. <span class="gloss">«A mí me gustan los videojuegos. ¿Y a ti?»</span></p>'
  '<table class="wtab mp"><thead><tr><th>¿A quién de la clase…?</th><th>Nombre</th><th>Nota</th></tr></thead><tbody>'
  '<tr><td>…le gustan los videojuegos</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>…le encanta la música pop</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>…no le gusta el fútbol</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>'
  '<p style="margin-left:12.5mm">Resultado (rapport, 3ª pers.): <span class="wl full"></span></p>'
  ''))
P('<div class="route-note">🎮 <b>Juega online:</b> «¿gusta o gustan?», «pronombres OI» en «Me gusta Tetris» met zelfcorrectie.</div>')
P('</div>')  # page §1.2b

# ================= §2 · TAMBIÉN / TAMPOCO + A MÍ SÍ / A MÍ NO =================
retos("gustar", "§1.4 · Retos — lo que te gusta, medido",
      'Tres retos sobre el gusto: la clase como <b>termómetro</b>, una <b>playlist</b> ajena y los gustos que <b>cambian</b>.',
      'Drie retos over smaak: de klas als thermometer, andermans playlist, en smaken die veranderen.')
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2 · Estar de acuerdo · también/tampoco · a mí sí/no</span>')
P('<div class="intro"><b>ES:</b> Para reaccionar a un gusto (¿de acuerdo o no?) tienes cuatro respuestas cortas. La ruta: contexto → observar → regla → practicar → comunicar. <span class="gloss">Om te reageren op een smaak heb je vier korte antwoorden.</span></div>')
P(lpd(("8","taalsysteem: reacties también/tampoco"), ("4","interactie: akkoord/oneens"), ("3","mening uitdrukken")))
P('</div>')
# §2.1 observar via spiegel
P('<h3 style="margin-top:6mm">§2.1 · Las cuatro reacciones — el espejo</h3>')
P('<p style="font-size:9.6pt">① <b>Observa (espejo).</b> Bea zegt iets; jij reageert. De reactie hangt af van <b>+ of –</b> én van <b>akkoord of niet</b>:</p>')
P(mirror([
  ('Bea: «Me gusta el mar.» <span class="gloss">(+, akkoord)</span>', 'A mí <span class="mk">también</span>. <span class="gloss">(ik ook)</span>'),
  ('Bea: «Me gusta el mar.» <span class="gloss">(+, oneens)</span>', 'A mí <span class="mk">no</span>. <span class="gloss">(ik niet)</span>'),
  ('Bea: «No me gusta el fútbol.» <span class="gloss">(–, akkoord)</span>', 'A mí <span class="mk">tampoco</span>. <span class="gloss">(ik ook niet)</span>'),
  ('Bea: «No me gusta el fútbol.» <span class="gloss">(–, oneens)</span>', 'A mí <span class="mk">sí</span>. <span class="gloss">(ik wel)</span>'),
]))
P('<p style="font-size:9.6pt">② <b>El árbol de decisión — ¿qué digo?</b></p>')
P('<div class="fams" style="margin-top:2mm"><div class="pcard">' + tree([
  '¿La frase es <b>positiva</b> (me gusta)? <span class="yes">akkoord →</span> <span class="res">A mí también</span> · <span class="no">oneens →</span> <span class="res">A mí no</span>',
  '¿La frase es <b>negativa</b> (no me gusta)? <span class="yes">akkoord →</span> <span class="res">A mí tampoco</span> · <span class="no">oneens →</span> <span class="res">A mí sí</span>',
]) + '</div>'
  '<div class="pcard"><div class="t" style="font-size:10pt">Onthoud</div><div class="ej"><b>+ akkoord</b> también<br><b>+ oneens</b> a mí no<br><b>– akkoord</b> tampoco<br><b>– oneens</b> a mí sí</div>'
  '<div class="t2">🔴 <b>tampoco</b> = «ook niet», niet «ook».</div></div></div>')
P(regla("Regla · reacciones",
  '<p><b>A mí también</b> = ik ook (na +) · <b>A mí tampoco</b> = ik ook niet (na –) · <b>A mí sí</b> = ik wel (na –) · <b>A mí no</b> = ik niet (na +). 🟡 Zeg altijd <b>a mí</b>, niet <i>yo</i>: «A mí también» (niet <span class="trap">Yo también gusto</span>).</p>'))
P('</div>')  # page §2.1
# §2 práctica
P('<div class="page">')
P('<div class="divider">Practicar · §2.2</div>')
P(actx(1, "Elige la reacción",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Omkring de juiste reactie (akkoord met de spreker).</p>'
  '<p style="margin-left:12.5mm">a) «Me gusta bailar.» → A mí <b>también</b> / <b>tampoco</b><br>'
  'b) «No me gustan los lunes.» → A mí <b>sí</b> / <b>tampoco</b><br>'
  'c) «Me encanta el cine.» → A mí <b>también</b> / <b>no</b> <span class="gloss">(jij niet akkoord)</span><br>'
  'd) «No me gusta el frío.» → A mí <b>tampoco</b> / <b>sí</b> <span class="gloss">(jij wél)</span></p>', apoyo="Pista: boom hierboven"))
P(actx(2, "Reacciona con la verdad",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Reageer op elke zin volgens <b>jouw</b> smaak (kies zelf akkoord of niet).</p>'
  '<table class="mp"><thead><tr><th>Bea dice…</th><th>Tu reacción</th></tr></thead><tbody>'
  '<tr><td>Me gustan los videojuegos.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>No me gusta madrugar.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Me encanta la playa.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>No me gustan las series largas.</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="Marco: vier reacties)"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha seis mini-diálogos y marca la reacción.</b> <span class="gloss">Kruis per dialoog aan: también / tampoco / a mí sí / a mí no.</span></div>',
           qr("Escanea y escucha", "Audio 4.2 · Reacciones · 0:50", seed=42)))
P(actx(3, "Escucha y marca la reacción",
  [{"t":"👂 Escuchar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Kruis aan wélke reactie je hoort.</p>'
  '<table class="mp"><thead><tr><th>#</th><th>también</th><th>tampoco</th><th>a mí sí</th><th>a mí no</th></tr></thead><tbody>'
  '<tr><td>1</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>2</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>3</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>4</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>5</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>6</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="Modelo: vier opties open"))
P(actx(4, "Completa la reacción",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul de reactie aan (kijk naar +/– én naar akkoord/oneens).</p>'
  '<p style="margin-left:12.5mm">a) «Me gusta el mar.» —A mí ___ . <span class="gloss">(ik ook)</span><br>'
  'b) «No me gusta el frío.» —A mí ___ . <span class="gloss">(ik ook niet)</span><br>'
  'c) «Me gustan las mates.» —A mí ___ . <span class="gloss">(ik niet)</span><br>'
  'd) «No me gustan los lunes.» —A mí ___ . <span class="gloss">(ik wél)</span></p>', apoyo="Pista: boom §2.1"))
P(actx(5, "Cadena de gustos",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En grupo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>In een kring: A zegt een gusto, B reageert (también/tampoco/sí/no) én voegt een eigen gusto toe, enz. Noteer één opvallende reactie.</p>'
  '<p style="margin-left:12.5mm">Nota: <span class="wl full"></span></p>', apoyo=""))
P(tarea_com("Tarea comunicativa · «¿Estamos de acuerdo?»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b>Situación:</b> zeg om de beurt een gusto; je buur reageert echt (también/tampoco/sí/no) en jullie tellen hoeveel jullie <b>gemeen</b> hebben. <span class="gloss">«A mí me gusta… —A mí también / A mí no.»</span></p>'
  '<p style="margin-left:12.5mm">Gustos en común: <span class="wl sm"></span> / 5 &nbsp; Uno diferente: <span class="wl md"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Marco: vier reacties</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «Espejo de reacciones» (también/tampoco) en «a mí sí / a mí no».</div>')
P('</div>')  # page §2.2

# ================= §3 · QUERER / PODER + INFINITIVO + QUEDAR =================
retos("reacciones", "§2.4 · Retos — reaccionar de verdad",
      'Tres retos donde la reacción cuenta: la <b>radio</b>, una <b>cadena</b> que se rompe, y cuatro frases que no se traducen.',
      'Drie retos waarin de reactie telt: de radio, een ketting die breekt, en vier zinnen die niet te vertalen zijn.')
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3 · Proponer un plan · querer / poder + quedar</span>')
P('<div class="intro"><b>ES:</b> Para <b>proponer</b> un plan usas <b>querer</b> y <b>poder</b> + infinitivo, y <b>quedar</b> para citar. Ojo: querer y poder cambian la raíz (e→ie, o→ue). <span class="gloss">Om een plan voor te stellen: querer/poder + infinitief, en quedar om af te spreken.</span></div>')
P(lpd(("8","taalsysteem: querer/poder (stamwissel) + infinitivo"), ("4","interactie: voorstellen & afspreken"), ("3","doelgericht spreken")))
P('</div>')
# §3.1 machine (stamwissel)
P('<h3 style="margin-top:6mm">§3.1 · La máquina que cambia la raíz</h3>')
P('<p style="font-size:9.6pt">① <b>Observa la máquina.</b> In het midden verandert de klinker (behalve bij nosotros/vosotros):</p>')
P(machine([("infinitivo","querer"),("raíz cambia",'qu<span class="end">ie</span>r-'),("+ terminación",'<span class="end">-o</span>'),("forma","qu<span class=end>ie</span>ro")]))
P(machine([("infinitivo","poder"),("raíz cambia",'p<span class="end">ue</span>d-'),("+ terminación",'<span class="end">-es</span>'),("forma","p<span class=end>ue</span>des")]))
P('<p style="font-size:9.6pt">② <b>Las dos tablas — la raíz cambia menos en nosotros/vosotros (oranje).</b></p>')
P('<div class="fams" style="margin-top:2mm">')
for inf, ends, stems in [("querer (e→ie)", ["quiero","quieres","quiere","queremos","queréis","quieren"], None),
                          ("poder (o→ue)", ["puedo","puedes","puede","podemos","podéis","pueden"], None)]:
    rows = "".join(f'<tr><td class="p">{p}</td><td class="v">{e}</td></tr>'
                   for p, e in zip(["yo","tú","él/ella","nosotros","vosotros","ellos"], ends))
    P(pcard(inf, f'<table class="conj"><tbody>{rows}</tbody></table>'))
P('</div>')
P('<p style="font-size:9.6pt">③ <b>Como bloques.</b> querer/poder + <b>infinitivo</b> (het tweede werkwoord blijft in de infinitief!):</p>')
P(blocks([
  [("per","(Yo)"),("vb","quiero"),("opt","ir a la playa")],
  [("per","¿(Tú)"),("vb","puedes"),("opt","quedar el sábado?")],
  [("per","(Nosotros)"),("vb","queremos"),("opt","ver una película")],
]))
P(regla("Regla · querer / poder + infinitivo",
  '<p><b>querer</b> (e→ie): quiero, quieres, quiere, <b>queremos</b>, <b>queréis</b>, quieren. <b>poder</b> (o→ue): puedo, puedes, puede, <b>podemos</b>, <b>podéis</b>, pueden. '
  '<br>🔴 De klinker verandert <b>niet</b> bij <b>nosotros/vosotros</b>. 🔴 Het tweede werkwoord blijft <b>infinitief</b>: <i>Quiero <b>ir</b></i> (niet <span class="trap">quiero voy</span>).</p>'))
P('</div>')  # page §3.1
# §3.2 quedar + práctica
P('<div class="page">')
P('<div class="divider">Quedar & practicar · §3.2</div>')
P('<h3>§3.2 · Proponer, aceptar, quedar</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto (chat).</b> Lucía propone un plan. Observa las frases útiles:</p>')
P('<div class="chat">'
  '<div class="chatline you"><div class="bub">¿Quieres ir a la playa el sábado?</div><div class="who">Lucía</div></div>'
  '<div class="chatline me"><div class="bub">¡Vale! ¿A qué hora quedamos?</div><div class="who">Tú</div></div>'
  '<div class="chatline you"><div class="bub">¿Podemos quedar a las once?</div><div class="who">Lucía</div></div>'
  '<div class="chatline me"><div class="bub">De acuerdo. Quedamos a las once en la playa.</div><div class="who">Tú</div></div></div>')
P(colloc("proponer", ["¿Quieres…?","¿Por qué no…?","¿Podemos…?","¿Quedamos…?","¡Vale! / De acuerdo","¿A qué hora?"]))
P(actx(1, "Conjuga querer y poder",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Vervoeg (let op de stamwissel — nosotros/vosotros zonder wissel).</p>'
  '<table class="mp"><thead><tr><th>Infinitivo</th><th>yo</th><th>tú</th><th>nosotros</th><th>ellos</th></tr></thead><tbody>'
  '<tr><td>querer</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>poder</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>', apoyo="Modelo: tabel §3.1 open) → PISTA"))
P(actx(2, "Completa el diálogo",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul de handige zinnen aan (proponer/quedar).</p>'
  '<p style="margin-left:12.5mm">—¿___ ir al cine? &nbsp;—¡___! ¿A qué ___ quedamos? &nbsp;—¿___ quedar a las seis? &nbsp;—De ___.<br><span class="gloss">banco: Quieres · Vale · hora · Podemos · acuerdo</span></p>', apoyo="Banco de palabras"))
P(actx(3, "Completa con la forma correcta (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p>Vul de <b>juiste werkwoordsvorm</b> in (infinitief tussen haakjes). <span class="gloss">gustar-constructie + querer/poder — vormen nagerekend.</span></p>'
  '<p style="margin-left:12.5mm">1. A nosotros nos <span class="wl md"></span> <i>(gustar)</i> las playas.<br>'
  '2. ¿<span class="wl md"></span> <i>(querer, tú)</i> quedar el sábado?<br>'
  '3. (A mí) me <span class="wl md"></span> <i>(encantar)</i> la música.<br>'
  '4. Yo no <span class="wl md"></span> <i>(poder)</i> hoy, lo siento.<br>'
  '5. ¿A ti te <span class="wl md"></span> <i>(gustar)</i> los videojuegos?<br>'
  '6. Nosotros <span class="wl md"></span> <i>(querer)</i> ir al cine.<br>'
  '7. Ella <span class="wl md"></span> <i>(poder)</i> tocar la guitarra.<br>'
  '8. A ellos les <span class="wl md"></span> <i>(gustar)</i> bailar.<br>'
  '9. ¿<span class="wl md"></span> <i>(poder, vosotros)</i> venir a la playa?<br>'
  '10. (A mí) me <span class="wl md"></span> <i>(gustar)</i> la horchata.</p>'
  '<p style="margin-left:12.5mm" class="gloss">✅ De oplossingen staan online (zelfcorrectie op de digitale pagina).</p>', apoyo="Pista: infinitief gegeven)"))
P(actx(4, "Cadena de transformación",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Begin met <b>«Quiero ir a la playa.»</b> en voer elke opdracht uit (schrijf de hele zin).</p>'
  '<p style="margin-left:12.5mm">→ maak er een <b>vraag</b> van (tú): <span class="wl lg"></span><br>→ verander naar <b>nosotros</b>: <span class="wl lg"></span><br>→ maak <b>ontkennend</b> (yo, poder): <span class="wl lg"></span><br>→ voeg <b>«el domingo»</b> toe: <span class="wl lg"></span></p>', apoyo="Pista"))
P(audiorow('<div class="ic">🎧</div><div><b>Microdictado.</b> Escucha dos veces y escribe las propuestas. <span class="gloss">1ª: betekenis · 2ª: schrijf de zinnen.</span></div>',
           qr("Escanea y escucha", "Audio 4.3 · Planes · 0:45", seed=43)))
P(actx(5, "Propón un plan",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf twee voorstellen met <b>querer</b> en <b>poder</b> + infinitivo.</p>'
  '<div class="wbox sm"></div>', apoyo="Marco: ¿Quieres…? ¿Podemos…?"))
P(actx(6, "¿querer o poder?",
  [{"t":"🔍 Analizar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Kies <b>querer</b> (willen) of <b>poder</b> (kunnen/mogen) en vervoeg voor de gegeven persoon.</p>'
  '<p style="margin-left:12.5mm">a) (yo, wens) ___ ir a la playa. &nbsp; b) (tú, mogelijkheid) ¿___ quedar hoy?<br>'
  'c) (nosotros, wens) ___ ver una peli. &nbsp; d) (ellos, kunnen) no ___ venir.<br><span class="wl full"></span></p>', apoyo="Pista: tabel §3.1)"))
P(tarea_com("Tarea comunicativa · «Quedamos el finde»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b>Situación:</b> stel elkaar een plan voor, ga akkoord of stel iets anders voor, en spreek een <b>uur en plaats</b> af. <span class="gloss">«¿Quieres…? —Vale. ¿A qué hora quedamos?»</span></p>'
  '<p style="margin-left:12.5mm">Nuestro plan: <span class="wl full"></span></p>'
  '<p style="margin-left:12.5mm">☐ plan · ☐ hora · ☐ lugar</p>'
  '<div class="steun" style="margin-left:12.5mm">Marco: proponer/quedar</div>'))
P('<div class="route-note">🔁 <b>Ojo — conjugador online:</b> alle vervoegingen (~1000 werkwoorden, nagerekend, incl. querer/poder/jugar) in de aparte cursus-tool «Conjugador».</div>')
P('</div>')  # page §3.2

# ================= §4 · LECTURA =================
retos("planes", "§3.4 · Retos — quedar de verdad",
      'Dos retos para cerrar un plan: una <b>cita a ciegas</b> por notas y un <b>presupuesto</b> que no da para todo.',
      'Twee retos om een plan te sluiten: een blind date via briefjes, en een budget dat niet voor alles volstaat.')
P('<div class="page"><div class="parada sec">')
P('<span class="num">📖</span><span class="pk">§4 · Lectura — «Perfiles de gustos»</span>')
P('<div class="intro"><b>ES:</b> Vas a leer dos perfiles de una app de música (tipo playlist). Primero <b>predices</b>, después lees con un <b>objetivo</b>. <span class="gloss">Je leest twee muziekprofielen: eerst voorspellen, dan lezen met een doel.</span></div>')
P(lpd(("1","onderwerp/hoofdgedachte bij lezen"), ("2","relevante info selecteren"), ("3","doelgericht schrijven met steun")))
P('</div>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> perfil de música (app)</span><span class="tm"><b>De:</b> Lucía · Diego</span><span class="tm"><b>Para:</b> compartir gustos</span><span class="tm">🎯 saber qué música les gusta</span></div>')
P(actx(1, "Antes de leer: predice",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★☆☆"}],
  '<p>Bekijk alleen de vorm en de titels. ¿Qué gustos esperas encontrar?</p>'
  '<p style="margin-left:12.5mm">Espero leer sobre: <span class="wl full"></span></p>', apoyo="Modelo: música, película, deporte…"))
P('<div class="ptexts">'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["lucia"]}</div><div><div class="nm">Lucía</div><div class="fr">app · mi playlist</div></div></div>'
  '<p>¡Hola! Me <span class="evi">encanta la música</span>. Mi artista favorita es <span class="evi">Rosalía</span>, ¡me gustan todas sus canciones! También me <span class="evi">gusta bailar</span> flamenco. Los fines de semana <span class="evi">voy a la playa</span> con amigos. No me gustan los videojuegos, prefiero salir. ¿Y a ti, qué te gusta?</p></div>'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["diego"]}</div><div><div class="nm">Diego</div><div class="fr">app · mi playlist</div></div></div>'
  '<p>¡Qué onda! A mí me <span class="evi">gusta el reguetón</span> y me <span class="evi">encantan los videojuegos</span>. Toco un poco la <span class="evi">guitarra</span>. No me gusta bailar, pero me gusta escuchar música todos los días. Los sábados quiero <span class="evi">ver películas de acción</span>. ¡Escríbeme tu playlist!</p></div></div>')
P('<div class="lecdoel">🎯 <b>Objetivo de lectura:</b> lees om te ontdekken <b>welke muziek</b> ze leuk vinden en <b>wat ze niet</b> leuk vinden — je hoeft niet élk woord te begrijpen.</div>')
P('</div>')  # page §4a
P('<div class="page">')
P(actx(2, "Escanea: completa la tabla",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Zoek de gegevens in de perfiles.</p>'
  '<table class="mp"><thead><tr><th></th><th>Le encanta…</th><th>Le gusta…</th><th>No le gusta…</th></tr></thead><tbody>'
  '<tr><td><b>Lucía</b></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td><b>Diego</b></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '</tbody></table>', apoyo="Modelo: evidence gemarkeerd in de tekst"))
P(actx(3, "¿Verdadero o falso? + prueba",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Waar of niet waar? Noteer de <b>woorden uit de tekst</b> die het bewijzen (evidence).</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba (palabras del texto)</th></tr></thead><tbody>'
  '<tr><td>A Lucía le encanta Rosalía.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>A Diego le gustan los videojuegos.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>A los dos les gusta bailar.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Diego escucha música todos los días.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '</tbody></table>', apoyo="Pista: onderstreep in de tekst"))
P(actx(4, "Del contexto: ¿qué significa?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Wat betekent <b>«prefiero salir»</b> en <b>«toco la guitarra»</b>? Kies + leg uit welke aanwijzing hielp.</p>'
  '<p style="margin-left:12.5mm">prefiero = ☐ ik verkies ☐ ik haat &nbsp;·&nbsp; toco = ☐ ik bespeel ☐ ik luister<br>Pista que me ayudó: <span class="wl lg"></span></p>', apoyo="Pista"))
P(actx(5, "Ordena la mini-conversación",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Zet de chat over gustos in de juiste volgorde (1–4).</p>'
  '<p style="margin-left:12.5mm">___ A mí también. ¿Quieres ir al concierto? &nbsp; ___ ¡Hola! ¿Te gusta Rosalía? &nbsp; ___ ¡Vale! ¿A qué hora quedamos? &nbsp; ___ Sí, me encanta.</p>', apoyo="Banco de palabras"))
P(tarea_com("Tarea comunicativa · Responde con tu perfil",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b></b> Kies één perfil en schrijf een <b>antwoord</b> met je eigen gustos (afzender = jij · ontvanger = Lucía/Diego · doel = smaak delen). Lees het daarna hardop voor.</p>'
  '<div class="wbox"></div>'
  '<div class="steun" style="margin-left:0mm">Marco: Me encanta… · Me gusta… · No me gusta… porque…</div>'))
P('<div class="route-note">🎮 <b>Sigue online:</b> op de digitale pagina neem je je antwoord op (recorder) en luister je de perfiles (audio).</div>')
P('</div>')  # page §4b

# ================= TALLER DE LENGUA =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num" style="color:var(--crema)">✎</span><span class="pk" style="background:var(--gd)">Taller de lengua</span>')
P('<div class="intro"><b>ES:</b> Dos herramientas para dar tu opinión: la pregunta <b>¿por qué?</b> con <b>porque</b>, y los <b>conectores</b> para enlazar gustos. <span class="gloss">Twee gereedschappen om je mening te geven.</span></div>')
P(lpd(("8","taalsysteem: ¿por qué?/porque + conectoren"), ("3","mening motiveren")))
P('</div>')
P('<h3 style="margin-top:6mm">Opinar · ¿por qué? → porque</h3>')
P('<p style="font-size:9.6pt">① <b>Espejo:</b> een vraag met <b>¿por qué?</b> vraagt om een reden met <b>porque</b>:</p>')
P(mirror([
  ('¿<span class="mk">Por qué</span> te gusta Rosalía?', 'Me gusta <span class="mk">porque</span> canta muy bien.'),
  ('¿<span class="mk">Por qué</span> no te gusta el fútbol?', 'No me gusta <span class="mk">porque</span> es aburrido.'),
]))
P('<div class="truc"><b>🔴 Valstrik NL:</b> <i>waarom</i> = <b>¿por qué?</b> (twee woorden, tilde) · <i>want/omdat</i> = <b>porque</b> (één woord, geen tilde). Verwar ze niet!</div>')
P(actx(1, "¿por qué o porque?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul <b>¿por qué?</b> of <b>porque</b> in.</p>'
  '<p style="margin-left:12.5mm">a) ¿___ te gusta el mar? &nbsp; b) Me encanta ___ es relajante.<br>'
  'c) ¿___ no quieres ir? &nbsp; d) No puedo ___ trabajo el sábado.<br><span class="wl full"></span></p>', apoyo="Pista: vraag ↔ reden"))
P('<h3 style="margin-top:6mm">Conectores · y · también · pero · además · sobre todo</h3>')
P('<table class="mp"><thead><tr><th>Conector</th><th>Uso</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td><b>y / también</b></td><td>toevoegen (+)</td><td>Me gusta nadar <b>y también</b> bailar.</td></tr>'
  '<tr><td><b>pero</b></td><td>tegenstelling</td><td>Me gusta el cine, <b>pero</b> no las series.</td></tr>'
  '<tr><td><b>además</b></td><td>bovendien</td><td>Canta bien; <b>además</b>, sus letras son bonitas.</td></tr>'
  '<tr><td><b>sobre todo</b></td><td>vooral</td><td>Me gusta la música, <b>sobre todo</b> el pop.</td></tr></tbody></table>')
P(actx(2, "Une con el conector correcto",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het juiste verbindingswoord in.</p>'
  '<p style="margin-left:12.5mm">a) Me gusta el fútbol ___ no me gusta el tenis. &nbsp; b) Me encanta la música, ___ el reguetón.<br>'
  'c) Toco la guitarra ___ canto. &nbsp; d) Es divertido; ___, es barato.<br><span class="gloss">banco: pero · sobre todo · y también · además</span></p>', apoyo="Banco de palabras"))
P(actx(3, "Amplía con un porqué",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Voeg aan elke zin een reden met <b>porque</b> toe.</p>'
  '<p style="margin-left:12.5mm">Me encanta la playa <span class="wl lg"></span><br>No me gustan los lunes <span class="wl lg"></span></p>', apoyo=""))
P(actx(4, "Escribe tu mini-opinión con conectores",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Schrijf 3 zinnen over jouw smaak met <b>y también</b>, <b>pero</b> én <b>porque</b>.</p>'
  '<div class="wbox sm"></div>', apoyo=""))
P(actx(5, "Corrige la opinión",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Zoek de fout (gustar-vorm, porque/por qué of conector) en herschrijf correct.</p>'
  '<p style="margin-left:12.5mm">1) <span class="trap">Me gustan el fútbol porque es divertido.</span> → <span class="wl lg"></span><br>'
  '2) <span class="trap">Me encanta bailar por qué es relajante.</span> → <span class="wl lg"></span><br>'
  '3) <span class="trap">Yo también gusto la música.</span> → <span class="wl lg"></span></p>', apoyo="Modelo"))
P('<div class="route-note">🎮 <b>Practica online:</b> «¿por qué o porque?» en de conectoren-oefeningen met zelfcorrectie.</div>')
P('</div>')  # page Taller

# ================= §5 LECTURA · §6 ESCUCHA =================
# Zelfde bron als de digitale hub (lectura_data / escucha_data): papier en scherm
# kunnen zo niet uit elkaar lopen. Elk op een eigen bladzijde (§14).
P('<div class="page"><div class="parada sec">')
P('<span class="num">5</span><span class="pk">§5 · Lectura — «Fiesta de la Música · València»</span>')
P('<div class="intro"><b>ES:</b> El programa de un festival de verdad. <b>No hace falta entenderlo todo</b> para elegir tu concierto. <span class="gloss">Het echte programma van een festival. Je hoeft niet alles te begrijpen om te kiezen — scan de uren en de stijlen.</span></div>')
P(PB.lectura_print(LD.C5_U4, "1"))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">6</span><span class="pk">§6 · Escucha — «¿Qué haces en tu tiempo libre?»</span>')
P('<div class="intro"><b>ES:</b> La radio del instituto para a tres personas en la calle. <b>Escucha primero, escribe después.</b> <span class="gloss">De schoolradio houdt drie mensen staande. Eerst luisteren, dan schrijven; het transcript staat online en gaat pas open ná de taken.</span></div>')
P(PB.escucha_print(ED.C5_U4, "1"))
P('</div>')

# ================= CULTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">★</span><span class="pk">Cultura · El ocio joven y Rosalía</span>')
P('<div class="intro"><b>ES:</b> En el mundo hispano la música une a la gente. Descubre a <b>Rosalía</b> y qué hacen los jóvenes en su tiempo libre. <span class="gloss">In de Spaanstalige wereld verbindt muziek; ontdek Rosalía en de vrije tijd van jongeren.</span></div>')
P(lpd(("5","kenmerkende aspecten van de cultuur"), ("2","relevante info uit een tekst")))
P('</div>')
P('<div class="fams" style="margin-top:6mm">')
P(pcard("🎵 Rosalía 🇪🇸", '<div class="ej">Cantante de <b>Barcelona</b>. Mezcla <b>flamenco</b> con pop y reguetón. Álbumes famosos: <i>El mal querer</i>, <i>Motomami</i>. Canta en español — perfecto voor de klas.</div><div class="anchor gloss">Een brug tussen traditie en de charts van vandaag.</div>'))
P(pcard("🏖️ El ocio joven", '<div class="ej">Jongeren <b>salen con amigos</b>, escuchan música, ven series, hacen deporte y van a la <b>playa</b>. En València: <b>las Fallas</b>, la <b>paella</b> y la <b>horchata</b>.</div><div class="t2">Muziek & samen zijn staan centraal.</div>'))
P('</div>')
P('<p style="font-size:9.6pt">① <b>Contraste — géneros musicales:</b></p>')
P(vpairs([("el flamenco (tradición)","el reguetón (actual)"),("el pop","el rock"),("una canción lenta","una canción movida"),("la letra (tekst)","el ritmo (ritme)")]))
P('<div class="truc"><b>🟡 Dato:</b> el español es de los idiomas <b>más escuchados</b> en las plataformas de música. Artistas como <b>Rosalía, Bad Bunny of Shakira</b> están en el top mundial.</div>')
P(actx(1, "Comprensión — verdadero o falso",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Waar of niet waar? Verbeter de foute.</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Corrección</th></tr></thead><tbody>'
  '<tr><td>Rosalía canta en inglés.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Rosalía mezcla flamenco y pop.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Las Fallas son de València.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="Modelo: tekst boven"))
P('</div>')  # page Cultura 1
# Cultura pagina 2 — mini-reseña (leesje) + reacción + productie
P('<div class="page">')
P('<div class="divider">Una mini-reseña · lee y opina</div>')
P('<h3>Una reseña de una canción</h3>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> reseña (blog)</span><span class="tm"><b>De:</b> un fan</span><span class="tm">🎯 saber si vale la pena</span></div>')
P('<div class="ptexts">'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["nina"]}</div><div><div class="nm">@musiclover</div><div class="fr">blog · reseña ★★★★☆</div></div></div>'
  '<p>Mi canción favorita de <span class="evi">Rosalía</span> es genial. Me <span class="evi">encanta la letra</span> porque habla del amor. El <span class="evi">ritmo es movido</span> y me dan ganas de bailar. '
  '¡Es perfecta para el verano en la <span class="evi">playa</span>! No me gusta mucho el vídeo, pero la <span class="evi">música es increíble</span>. ¿La conoces?</p></div>'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["diego"]}</div><div><div class="nm">@diego_mx</div><div class="fr">comentario</div></div></div>'
  '<p>A mí <span class="evi">también me gusta</span>, ¡sobre todo el estribillo! Pero prefiero el <span class="evi">reguetón</span>. '
  'Me encanta escucharla cuando juego a videojuegos. Además, la letra es fácil para practicar español. ¡Buena reseña!</p></div></div>')
P(actx(2, "Escanea la reseña: ¿verdadero o falso?",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Waar of niet waar? Noteer het bewijs uit de tekst.</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba</th></tr></thead><tbody>'
  '<tr><td>A @musiclover le encanta la letra.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>A @diego_mx no le gusta la canción.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Diego prefiere el reguetón.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="Pista: evidence gemarkeerd"))
P(actx(3, "Escribe tu mini-reseña",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>Schrijf 3–4 zinnen over een artiest/lied dat jij leuk vindt, met <b>me gusta/encanta + porque + conectores</b>. Presenteer daarna aan je buur.</p>'
  '<p style="margin-left:12.5mm">Mi artista/canción: <span class="wl lg"></span></p>'
  '<div class="wbox sm"></div>', apoyo="Marco: Me encanta… porque… además…)"))
P('<div class="route-note">🎮 <b>Sigue online:</b> escucha una canción, lee la letra y reacciona met de gustos-spellen op de digitale pagina.</div>')
P('</div>')  # page Cultura 2

# ================= CULTURA · BANDA SONORA (PAREL-3/4) =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">♫</span><span class="pk">Cultura · Banda sonora</span>')
P('<div class="intro"><b>ES:</b> Cada unidad tiene su <b>banda sonora</b>: artistas que suenan hoy en todo el mundo hispano. Escucha, canta y pilla palabras nuevas — casi todos cantan de lo que te <b>gusta</b> y de lo que <b>quieres</b>. <span class="gloss">Elke unit heeft zijn soundtrack: artiesten die nu overal klinken. Luister, zing mee en pik nieuwe woorden op — bijna allemaal zingen ze over wat je leuk vindt.</span></div>')
P(lpd(("5","kenmerkende aspecten van de cultuur"), ("2","relevante info uit een tekst"), ("7","woordenschat via muziek")))
P('</div>')
P('<h3 style="margin-top:6mm">Seis artistas del mundo hispano <span class="gloss" style="font-size:8pt">· la playlist de la clase</span></h3>')
P(banda([
  ("Rosalía", "🇪🇸 flamenco-pop",  "La Perla · Motomami",
   'Cantante de <b>Barcelona</b>. Mezcla el <b>flamenco</b> tradicional con el pop, el trap y el reguetón. Sus álbumes <i>El mal querer</i> y <i>Motomami</i> son famosos en todo el mundo. Canta en español, ¡perfecto para la clase! '
   '<span class="gloss">Zangeres uit Barcelona. Ze mengt traditionele flamenco met pop, trap en reggaeton. Haar albums <i>El mal querer</i> en <i>Motomami</i> zijn wereldberoemd. Ze zingt in het Spaans — ideaal voor de klas!</span>'),
  ("Karol G", "🇨🇴 reguetón",  "TQG · Provenza",
   'Es de <b>Medellín</b> (Colombia) y es una de las reinas del <b>reguetón</b>. Su pelo naranja es su marca. Con canciones como <i>TQG</i> y <i>Provenza</i> llena estadios en América y Europa. A los jóvenes les <b>encanta</b> bailar sus temas. '
   '<span class="gloss">Komt uit Medellín (Colombia) en is een van de koninginnen van de reggaeton. Haar oranje haar is haar handelsmerk. Met liedjes als <i>TQG</i> en <i>Provenza</i> vult ze stadions in Amerika en Europa. Jongeren zijn dol op dansen op haar nummers.</span>'),
  ("Bad Bunny", "🇵🇷 urbano",  "Tití me preguntó",
   'El «conejo malo» es de <b>Puerto Rico</b> y es el artista más escuchado del planeta. Mezcla reguetón, trap y hasta música típica de su isla. Además de cantar, es actor y luchador. Sus conciertos son enormes. '
   '<span class="gloss">De «conejo malo» komt uit Puerto Rico en is de meest beluisterde artiest ter wereld. Hij mengt reggaeton, trap en zelfs typische muziek van zijn eiland. Naast zingen is hij ook acteur en worstelaar. Zijn concerten zijn enorm.</span>'),
  ("Shakira", "🇨🇴 pop",  "Waka Waka · BZRP 53",
   'De <b>Barranquilla</b> (Colombia), es una leyenda del pop mundial desde hace más de veinte años. Baila, escribe sus canciones y canta en español e inglés. <i>Waka Waka</i> fue el himno de un Mundial de fútbol. Es un símbolo de Latinoamérica. '
   '<span class="gloss">Uit Barranquilla (Colombia), al meer dan twintig jaar een legende van de wereldpop. Ze danst, schrijft haar eigen liedjes en zingt in het Spaans en Engels. <i>Waka Waka</i> was de hymne van een WK voetbal. Ze is een symbool van Latijns-Amerika.</span>'),
  ("Feid", "🇨🇴 reguetón",  "Feliz Cumpleaños Ferxxo",
   'Otro artista de <b>Medellín</b>, siempre con su ropa <b>verde</b>. Empezó escribiendo canciones para otros y ahora es una estrella del reguetón «neo perreo». Sus fans se llaman «los Ferxxos». Colabora mucho con Karol G. '
   '<span class="gloss">Nog een artiest uit Medellín, altijd in het groen gekleed. Hij begon met liedjes schrijven voor anderen en is nu een ster van de «neo perreo»-reggaeton. Zijn fans heten «los Ferxxos». Hij werkt vaak samen met Karol G.</span>'),
  ("Quevedo", "🇪🇸 urbano",  "Bzrp #52 · Columbia",
   'Joven cantante de las <b>Islas Canarias</b> (España). Se hizo famoso con su sesión con Bizarrap, un éxito mundial. Su estilo mezcla el trap y el reguetón con letras tranquilas. Representa a la nueva generación del urbano español. '
   '<span class="gloss">Jonge zanger van de Canarische Eilanden (Spanje). Hij werd beroemd met zijn sessie met Bizarrap, een wereldwijde hit. Zijn stijl mengt trap en reggaeton met rustige teksten. Hij vertegenwoordigt de nieuwe generatie van de Spaanse urban.</span>'),
]))
P('<div class="truc"><b>🟡 Dato:</b> el <b>español</b> es de los idiomas <b>más escuchados</b> en Spotify y YouTube. Cuatro de estos seis artistas son de <b>Colombia</b> o del <b>Caribe</b> — la ruta te lleva allí en U7 y U8.</div>')
P(audiorow('<div class="ic">🎧</div><div><b>Escucha «La Perla» de Rosalía</b> (o un fragmento) y anota <b>tres palabras</b> que reconoces. <span class="gloss">Luister; noteer drie woorden die je herkent — LyricsTraining staat online.</span></div>',
           qr("Escanea y escucha", "Banda sonora · playlist U4", seed=45)))
P('</div>')  # page Banda 1
P('<div class="page">')
P('<div class="divider">La escala del gusto · «La Perla»</div>')
P('<p style="font-size:9.6pt">① <b>De «odio» a «me encanta».</b> Rosalía canta en <i>La Perla</i> sobre alguien a quien no aguanta. Zo kan je je smaak <b>graderen</b>, van heel negatief tot heel positief:</p>')
P(perla_scale([
  ("#DC2626", "odio", "ik haat"),
  ("#B7860B", "no me gusta", "ik vind niet leuk"),
  ("#2FA8A0", "me gusta", "ik vind leuk"),
  ("#157355", "me encanta", "ik vind geweldig"),
]))
P('<div class="truc"><b>🔴 Ojo:</b> <b>odio</b> + naamwoord/infinitief: <i>odio los lunes · odio madrugar</i>. Bij <b>me encanta / me gusta</b> geldt weer de regel gusta/gustan (bevalt mij). <b>odio</b> vervoeg je gewoon (yo odio, tú odias…).</div>')
P(actx(1, "Coloca en la escala",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Plaats elk gevoel op de juiste trap (1 = odio … 4 = me encanta) en schrijf het cijfer.</p>'
  '<p style="margin-left:12.5mm">___ me encanta bailar &nbsp; ___ odio los lunes &nbsp; ___ me gusta el pop &nbsp; ___ no me gusta madrugar<br>Un gusto mío en cada nivel: <span class="wl full"></span></p>', apoyo="Modelo: escala boven"))
P(actx(2, "¿Qué artista y por qué? (mini-reseña con la escala)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Kies twee artiesten hierboven. Schrijf per artiest één zin met een <b>niveau van de escala</b> (odio / no me gusta / me gusta / me encanta) én een reden met <b>porque</b>.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span></p>', apoyo="Marco: Me encanta … porque …)"))
P(tarea_com("Tarea comunicativa · «La playlist de la clase»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b>Situación:</b> vergelijk met je buur welke van de zes artiesten jullie <b>me encanta / me gusta / no me gusta / odio</b> vinden. Reageer met <b>también/tampoco/a mí sí/no</b> en kies samen één nummer voor de klasplaylist.</p>'
  '<table class="mp"><thead><tr><th>Artista</th><th>Yo (escala)</th><th>Mi compañero/a</th><th>¿Igual?</th></tr></thead><tbody>'
  '<tr><td>Rosalía</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>Karol G</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>Bad Bunny</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>'
  '<p style="margin-left:12.5mm">Nuestra canción para la clase: <span class="wl lg"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Marco: escala + reacciones</div>'))
P('<div class="route-note">🎮 <b>Sigue online:</b> escucha la playlist, prueba <b>LyricsTraining</b> (vul de songtekst aan) y juega «La escala del gusto» met zelfcorrectie op de digitale pagina.</div>')
P('</div>')  # page Banda 2

# ================= TAREA FINAL =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num">✦</span><span class="pk" style="background:var(--gd)">Tarea final · Mi playlist</span>')
P('<div class="intro"><b>ES:</b> Crea tu <b>playlist personal</b>: canciones que te gustan + <b>por qué</b> + qué sientes. Preséntala a la clase. <span class="gloss">Maak je persoonlijke playlist en stel ze voor.</span></div>')
P('<div class="route-note">🎯 <b>Communicatieve taak:</b> afzender = jij · ontvanger = de klas/Lucía · doel = je smaak delen & motiveren · situatie = een muziekavond in València · resultaat = ingevulde playlist + presentatie.</div>')
P(lpd(("3","doelgericht schrijven met een voorbeeld"), ("4","mondeling presenteren & interageren"), ("7","woordenschat gustos/música"), ("8","gustar/encantar + porque")))
P('</div>')
P('<ol class="pasos">'
  '<li><b>Elige 4 canciones/artistas</b> que te gustan (o te encantan).</li>'
  '<li><b>Rellena la playlist</b> hieronder: canción · por qué (porque…) · qué sientes.</li>'
  '<li><b>Escribe tu presentación</b> (5–6 frases) met gustar/encantar + porque + conectores.</li>'
  '<li><b>Presenta</b> tu playlist a la clase (of neem audio op via de digitale pagina).</li>'
  '<li><b>Pregunta</b> a un compañero por sus gustos y reacciona (también/tampoco/a mí sí/no).</li></ol>')
P('<table class="alf"><thead><tr><th>🎵 Canción / artista</th><th>Me gusta / encanta porque…</th><th>Me hace sentir…</th></tr></thead><tbody>'
  '<tr><td><span class="wl md"></span></td><td><span class="wl md"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td><span class="wl md"></span></td><td><span class="wl md"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td><span class="wl md"></span></td><td><span class="wl md"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td><span class="wl md"></span></td><td><span class="wl md"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>')
P('<div class="se" style="margin-top:5mm">Mi presentación <span class="gloss" style="font-size:8pt">· 5–6 frases: gustar/encantar + porque + conectores</span></div><div class="wbox"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba tu presentación</b> en la página digital (recorder + rúbrica).</div>',
           qr("Escanea y graba", "Tarea · Mi playlist", seed=44)))
P('<div class="se" style="margin-top:5mm">Mini-encuesta: gustos de la clase <span class="gloss" style="font-size:8pt">— vraag 5 klasgenoten, teken de balken</span></div>')
P(gustobars([("la música pop", 60), ("los videojuegos", 40), ("el deporte", 50), ("bailar", 30)]))
P('<p style="font-size:8.6pt" class="gloss">↳ vervang de voorbeeld-balken door je eigen resultaten (aantal /5 → %).</p>')
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Mijn playlist heeft <b>4 items</b> met een <b>reden</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>gusta/gustan</b> en <b>encanta(n)</b> correct</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik motiveer met <b>porque</b> en verbind met <b>conectores</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>presenteer mondeling</b> en <b>reageer</b> op een klasgenoot</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — la playlist de mi compañero/a</div>'
  '<table><thead><tr><th>Lo que me gusta de su playlist</th><th>Un consejo (una cosa)</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('</div>')  # page Tarea

# ================= REPASO =================
retos("cultura_u4", "Retos — València sin mentiras",
      'Dos retos finales: un <b>anuncio</b> en el que todo es verdad y una <b>encuesta</b> de verdad.',
      'Twee slotretos: een reclame waarin alles waar is, en een echte enquête.')
P('<div class="page"><div class="parada sec">')
P('<span class="num">✓</span><span class="pk">Repaso · lo esencial</span>')
P('<div class="intro"><b>ES:</b> Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, 20 juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag.</span></div>')
P('</div>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>Gustar (al revés):</b> me/te/le/nos/os/les + <b>gusta</b> (ev./infinitivo) · <b>gustan</b> (mv.). Idem encanta(n).</li>'
  '<li><b>Reacciones:</b> + akkoord <b>a mí también</b> · + oneens <b>a mí no</b> · – akkoord <b>a mí tampoco</b> · – oneens <b>a mí sí</b>.</li>'
  '<li><b>Proponer:</b> <b>querer</b> (quiero…quieren, e→ie) / <b>poder</b> (puedo…pueden, o→ue) + <b>infinitivo</b> · <b>quedar</b> (afspreken).</li>'
  '<li><b>Opinar:</b> ¿por qué? → <b>porque</b> + reden · conectoren y/también · pero · además · sobre todo.</li>'
  '<li><b>Las trampas:</b> 🔴 gustar = «bevalt mij» · 🔴 gusta<b>n</b> bij mv. · 🔴 tampoco = ook niet · 🔴 querer/poder blijven wissel-loos bij nosotros · 🔴 ¿por qué? ≠ porque.</li></ul></div>')
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> 24 spelletjes met zelfcorrectie op de digitale pagina.</div>')
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td>zeggen wat ik <b>leuk/geweldig</b> vind (gusta/gustan/encanta)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>de <b>OI-voornaamwoorden</b> (me/te/le…) gebruiken</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>akkoord gaan of niet</b> (también/tampoco/a mí sí/no)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>een <b>plan voorstellen</b> (querer/poder + inf. · quedar)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>mijn mening <b>motiveren</b> met porque + conectoren</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil de U4: <span class="wl md"></span> · Lo más difícil: <span class="wl md"></span></i></div>')
P('<div class="bridge"><b>» Siguiente parada: cruzamos el charco → México (U5).</b> Ya sabes hablar de gustos; en <b>U5 «¡Ñam!»</b> (CDMX) pides comida en un restaurante y descubres la gastronomía mexicana. <span class="gloss">In U5 steek je de oceaan over naar Mexico en bestel je eten.</span></div>')
P('</div>')  # page Repaso

# ================= §V VOCABULARIO =================
import json
VOC = json.load(open(f"{HERE}/u4_vocab.json", encoding="utf-8"))
GRP = [("opinar","Expresar gustos y opiniones"),("ocio","Deportes y ocio"),("musica","Música y cine"),
       ("sentim","Sentimientos y opiniones (adjetivos)"),("frecuencia","Adverbios de frecuencia"),
       ("planes","Proponer y quedar"),("valencia","València · la costa")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (begrijpen en zelf gebruiken)")))
P('</div>')
P('<p style="font-size:9.6pt">Los <b>gustos</b> als netwerk — vier families die de hele unit dragen:</p>')
P(clusters([
  ("🎵","Música & cine",["la canción · el/la cantante","la película · la serie","escuchar · tocar"],"Wat je hoort en ziet."),
  ("🏃","Deportes & ocio",["el fútbol · nadar · bailar","los videojuegos · leer","la playa · salir"],"Wat je doet."),
  ("💬","Opinar & reaccionar",["me gusta(n) · me encanta(n)","también · tampoco · a mí sí/no","porque · pero · además"],"Wat je vindt & zegt."),
]))
for key, titel in GRP:
    items = [v for v in VOC if v.get("grp") == key]
    if not items: continue
    P(f'<h3 style="margin-top:6mm">{titel} <span class="gloss" style="font-size:8pt">· {len(items)} woorden</span></h3>')
    rows = "".join(f'<tr><td><b>{v["es"]}</b></td><td>{v["nl"]}</td><td class="gloss">{v["soort"]}</td><td class="gloss">{v["ej"]}</td></tr>' for v in items)
    P(f'<table class="alf"><thead><tr><th>Español</th><th>Nederlands</th><th>ERK/soort</th><th>Ejemplo</th></tr></thead><tbody>{rows}</tbody></table>')
# print-oefenladder V.1-V.4
P('</div><div class="page">')  # nieuwe bladzijde: oefenladder krijgt volle pagina
P('<div class="divider">Escalera de práctica · V.1–V.7</div>')
P(actx("V.1", "Reconocer — ES → NL",
  [{"t":"🔍 Leer","skill":True},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Schrijf de vertaling. la canción = <span class="wl md"></span> · el deporte = <span class="wl md"></span> · encantar = <span class="wl md"></span> · a menudo = <span class="wl md"></span></p>', apoyo="Modelo"))
P(actx("V.2", "Distinguir — sorteer per familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Sorteer: <span class="words"><b>bailar · la película · siempre · quedar · el mar · a veces</b></span></p>'
  + sortcols([("ocio/música",""),("frecuencia",""),("planes/valencia","")], eigen=False), apoyo="Banco de palabras"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het Spaanse woord aan (beginletter gegeven). het strand = <b>p</b>___ · de zanger(es) = <b>c</b>___ · willen = <b>q</b>___ · altijd = <b>s</b>___<br><span class="wl full"></span></p>', apoyo="Primera letra"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Maak één correcte zin met <b>me gusta(n) · porque · a veces</b>.</p><div class="wbox sm"></div>', apoyo=""))
P(actx("V.5", "Comunicar — mi top-3 de gustos",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Schrijf je <b>top-3</b> favoriete dingen met de juiste vorm (gusta/gustan/encanta) én telkens een reden met <b>porque</b>. Zeg ze daarna hardop tegen je buur, die reageert (también/tampoco/sí/no).</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>', apoyo="Marco: Me encanta … porque …)"))
P(actx("V.6", "Definiciones — ¿qué palabra es?",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Lees de definitie in het Spaans en schrijf het juiste woord uit de unit.</p>'
  '<table class="mp"><thead><tr><th>Definición (ES)</th><th>La palabra</th></tr></thead><tbody>'
  '<tr><td>Lugar con arena y mar donde vas en verano.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Una persona que canta.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Mover el cuerpo con la música.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Palabra para decir «want / omdat».</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Reacción cuando estás de acuerdo con algo positivo.</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="Banco de palabras: playa · cantante · bailar · porque · también"))
P(actx("V.7", "Mi carné de gustos — ficha final",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Vul je eigen «carné de gustos» in met volledige zinnen (gusta/gustan/encanta + porque). Bewaar het voor de eindtaak.</p>'
  '<div class="fichacard">'
  '<div><div class="row"><span class="k">Me encanta…</span><span class="v"><span class="wl sm"></span></span></div>'
  '<div class="row"><span class="k">Me gusta(n)…</span><span class="v"><span class="wl sm"></span></span></div>'
  '<div class="row"><span class="k">No me gusta…</span><span class="v"><span class="wl sm"></span></span></div></div>'
  '<div><div class="row"><span class="k">Odio…</span><span class="v"><span class="wl sm"></span></span></div>'
  '<div class="row"><span class="k">Mi artista favorito/a…</span><span class="v"><span class="wl sm"></span></span></div>'
  '<div class="row"><span class="k">…porque…</span><span class="v"><span class="wl sm"></span></span></div></div></div>', apoyo="Marco"))
P(mispal("Mis palabras de la unidad", 4))
P('<div class="route-note">🎴 <b>Sigue en la página digital:</b> flip cards (ES↔NL) van álle woorden, audio (TTS), buscador én de 20 spellen bouwen de steun verder af. Scan de QR op deze bladzijde en oefen tot je alles <b>sin ayuda</b> kan.</div>')
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
   a.href=URL.createObjectURL(blob); a.download='U4_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Español en la práctica · U4 Me gusta</title><style>'
        + CSS + PB.CSS + RP.CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/U4.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes")
