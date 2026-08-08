#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de print-HTML U6.html (C5 · Unidad 6 «De tiendas») → PDF via Chromium.
# Zelfde componentenkit/pijplijn als golden sample U0/U1/U4 (cursus-print.css). Fonts base64 ingebed,
# cast-avatars inline SVG (cast_gen). Cursuskleur = groen (C5). Parada 6 = México/mercados, gastheer Diego.
# Output = standalone bewerkbare U6.html.
import os, sys, base64
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f"{ROOT}/02-huisstijl/beeld/generators")
import cast_gen as C
import sys as _sys
_sys.path.insert(0, "/home/user/espa-ol-en-la-pr-ctica/03-build/web")
import qr_print as QRP; QRP.fijar("C5", 6)
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
    return f'<div class="steun" style="margin-left:12.5mm">Apoyo: {niveau}</div>'

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
  <div class="tab">U6 · DE TIENDAS</div>
  <div class="eyebrow">UNIDAD 6 · LA RUTA · PARADA 6 — MÉXICO / LOS MERCADOS 🇲🇽</div>
  <h1>De tiendas</h1>
  <div class="sub">Seguimos en <b>México</b>, pero hoy vamos <b>de compras</b>: ropa, colores, tallas y precios en el <b>mercado</b> y las <b>tiendas</b>. Con <b>Diego</b> aprendes a comprar, probarte ropa y hasta a <b>regatear</b>. <span class="gloss">We blijven in Mexico, maar gaan winkelen: kleding, kleuren, maten en prijzen — op de markt en in de winkel.</span></div>
  <div class="q">¿Qué te vas a comprar hoy? <span style="font-weight:400;opacity:.9">· Wat ga je vandaag kopen?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U3 · Barcelona</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U4 · València</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U5 · México</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U6 · Mercados</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U7 · Colombia</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U8 · Perú</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 6 · Los mercados de México.</b> Seguimos con <b>Diego</b>. Del <b>tianguis</b> al <b>centro comercial</b>: aprendes la <b>ropa</b>, los <b>colores</b>, a preguntar la <b>talla</b> y el <b>precio</b>, y a <b>regatear</b>. <span class="gloss">Van de tianguis tot het winkelcentrum: kleding, kleuren, maat, prijs en afdingen.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> En el <b>mercado</b> hay ropa de todos los colores. <b>Diego</b> te ayuda: «¿Te gusta <b>esta</b> camiseta o <b>esa</b>?». Te pruebas una chaqueta en el <b>probador</b>, preguntas «¿<b>cuánto cuesta</b>?» y, en el tianguis, <b>regateas</b> el precio. Al final: «Me <b>lo</b> llevo».
      <span class="gloss">Op de markt is kleding in alle kleuren. Diego helpt je kiezen, je past iets in het paskamer, vraagt de prijs en dingt af. Op het einde: «ik neem het».</span></div>
      <div class="ojo"><b>¡Ojo! — de valstrik van vandaag:</b> een kleur past zich aan bij het kledingstuk: <b>una camiseta roj<span class="trap">a</span></b> (v.) · <b>un vestido roj<span class="trap">o</span></b> (m.) · <b>unos zapatos roj<span class="trap">os</span></b>. Maar <b>azul · gris · verde · marrón · naranja · rosa</b> veranderen niet van geslacht: <i>una falda azul</i> (niet <span class="trap">azula</span>).</div>
    </div>
    <div>
      <div class="se">La gente de la ruta</div>
      <div class="cast">
        <div class="pc"><div class="avw">{AV["diego"]}</div><div class="nm">Diego</div><div class="fr">México 🇲🇽 · anfitrión</div></div>
        <div class="pc"><div class="avw">{AV["lucia"]}</div><div class="nm">Lucía</div><div class="fr">Sevilla 🇪🇸</div></div>
        <div class="pc"><div class="avw">{AV["valen"]}</div><div class="nm">Valen</div><div class="fr">Cartagena 🇨🇴</div></div>
        <div class="pc"><div class="avw">{AV["nina"]}</div><div class="nm">Nina</div><div class="fr">Cusco 🇵🇪</div></div>
        <div class="pc tu"><div class="avw">{TU}</div><div class="nm">Tú</div><div class="fr">Flandes 🇧🇪</div></div>
      </div>
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila de compras</span><br><span class="gloss" style="font-size:8.5pt">In de mercado vul je je rugzak met de woorden van het winkelen: la ropa, la talla, las rebajas, ¿cuánto cuesta?, me lo llevo.</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">nombrar la ropa y los colores</span> (camiseta, vaqueros, rojo…) <span class="nl">kleding & kleuren benoemen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar lo/la/los/las</span> (¿la falda? → la compro) <span class="nl">OD-voornaamwoord + plaats</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">decir qué acabas de hacer</span> con <b>acabar de + infinitivo</b> <span class="nl">zeggen wat je net gedaan hebt</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">señalar con este / ese / aquel</span> <span class="nl">aanwijzen (dichtbij ↔ ver)</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">hacer concordar el adjetivo</span> (camiseta roja · de rayas) <span class="nl">de bijvoeglijke naamwoorden laten overeenkomen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">abrir tu <b>tienda</b></span> y vender en pareja <span class="nl">je eigen winkel openen (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>lo/la/los/las</span><span><b>§2</b>acabar de + inf</span><span><b>§3</b>este/ese/aquel</span><span><b>§4</b>Concordancia</span><span><b>§5</b>Lectura</span><span><b>Taller</b>Sílaba/conect.</span><span><b>Cultura</b>Rebajas & regateo</span><span><b>Tarea</b>Abre tu tienda</span><span><b>Repaso</b>Semáforo</span>
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
      <div class="ej" style="margin-top:2mm">📄 el libro · 🎮 la <b>página digital</b> (16 spellen, audio, flip cards) · 📊 el PowerPoint. De <b>QR</b>-codes brengen je naar de juiste online-oefening.</div>
      <div class="anchor gloss" style="margin-top:2mm">Print werkt <b>volledig zonder</b> scherm; het <b>repaso</b> staat online.</div></div>
  </div>
</div>
''')

# ---------- §0 Ponte al día ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">0</span><span class="pk">§0 · ¡Ponte al día!</span>')
P('<div class="intro"><b>ES:</b> Antes de ir de compras, recordamos lo que necesitas hoy: los <b>números</b> (para los precios), la <b>concordancia</b> (mucho/-a) de U5, y el verbo <b>gustar</b>. <span class="gloss">Voor we gaan winkelen: kort ophalen — getallen/prijzen, concordantie en gustar.</span></div>')
P(lpd(("7","woordenschat inzetten"), ("8","concordantie & getallen ophalen"), ("9","strategieën / lengua de clase")))
P('</div>')
P('<p style="font-size:9.6pt">① <b>¿Qué tienes ya en la mochila?</b> Drie clusters die je vandaag inzet. <span class="gloss">Wat zit er al in je rugzak? omgekeerde flashcards.</span></p>')
P(clusters([
  ("🔢","Precios (U0)",["diez · veinte","cincuenta euros","¿cuánto cuesta?"],"Voor de prijskaartjes."),
  ("⚖️","Concordancia (U5)",["mucho pan · mucha fruta","el/la · los/las","un/una · unos/unas"],"Vorm past bij het woord."),
  ("👍","Gustar (U4)",["me gusta esta camiseta","me gustan estos zapatos","no me gusta el color"],"Zeggen wat je mooi vindt."),
]))
P(actx(1, "Calentamiento: ¿qué llevas hoy?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Zeg drie kledingstukken die je vandaag draagt, met <b>llevo</b>. Je buur noteert. Wissel.</p>'
  '<p style="margin-left:12.5mm">Modelo: <i>«Hoy llevo unos vaqueros, una camiseta y zapatillas.»</i><br>Mi compañero/a lleva: <span class="wl full"></span></p>', apoyo="MODELO → SIN AYUDA"))
P(actx(2, "Números para los precios",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Schrijf de prijs voluit (¿cuánto cuesta?).</p>'
  '<table class="mp"><thead><tr><th>Precio</th><th>En letras</th></tr></thead><tbody>'
  '<tr><td>15 €</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>40 €</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>100 €</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="PISTA (quince · cuarenta · cien)"))
P(actx(3, "Empareja: prenda con imagen",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind het woord met de emoji (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Palabra</th><th></th><th>Imagen</th></tr></thead><tbody>'
  '<tr><td>1 · la camiseta</td><td><span class="wl sm"></span></td><td>A · 👖</td></tr>'
  '<tr><td>2 · los zapatos</td><td><span class="wl sm"></span></td><td>B · 👕</td></tr>'
  '<tr><td>3 · los vaqueros</td><td><span class="wl sm"></span></td><td>C · 👗</td></tr>'
  '<tr><td>4 · el vestido</td><td><span class="wl sm"></span></td><td>D · 👞</td></tr></tbody></table>', apoyo="BANCO"))
P(actx(4, "¿el, la, los o las?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Vul het juiste lidwoord in (kijk naar m./v. · ev./mv.).</p>'
  '<p style="margin-left:12.5mm">___ camiseta &nbsp; ___ zapatos &nbsp; ___ falda &nbsp; ___ pantalones &nbsp; ___ abrigo &nbsp; ___ botas<br><span class="gloss">Let op: la · los · la · los · el · las.</span></p>', apoyo="PISTA (el/la · los/las)"))
P(actx(5, "Mi ropa favorita en presente",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf twee ware zinnen: één met <b>llevo</b> en één met <b>me gusta(n)</b>.</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (Llevo… / Me gusta(n)…)"))
P(actx(6, "Verdadero para mí",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Zet ✔ als het klopt, ✘ als niet. Verbeter er één met een zin.</p>'
  '<p style="margin-left:12.5mm">☐ Me gustan las zapatillas. &nbsp; ☐ Llevo gafas. &nbsp; ☐ No me gusta el color rosa.<br>Mi corrección: <span class="wl full"></span></p>', apoyo="MODELO"))
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> ropa básica, getallen/precios en concordantie met zelfcorrectie op de digitale pagina.</div>')
P('</div>')  # close §0

# ================= §1 · OD-PRONOMBRES =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">1</span><span class="pk">§1 · lo / la / los / las · ¿la falda? → la compro</span>')
P('<div class="route-note">📍 Parada 6 · Diego en la tienda: «¿La camiseta roja? — Sí, la quiero.».</div>')
P('<div class="intro"><b>ES:</b> Para no repetir la prenda, la cambias por <b>lo / la / los / las</b>. La ruta: contexto → rieles (¿dónde va?) → radiografía → practicar → comunicar. <span class="gloss">Om het kledingstuk niet te herhalen vervang je het door lo/la/los/las. Waar staat het in de zin?</span></div>')
P(lpd(("8","taalsysteem: OD-pronomen + plaatsing"), ("7","woordenschat: ropa/tienda"), ("3","doelgericht schrijven met steun"), ("4","mondelinge interactie")))
P('</div>')
# §1.1 observar
P('<h3 style="margin-top:6mm">§1.1 · Descubre — ¿qué reemplaza «lo/la»?</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto.</b> In de tienda herhaalt niemand de hele prenda:</p>')
P('<div class="chat">'
  '<div class="chatline you"><div class="bub">¿Te gusta esta <span class="fx ob">camiseta</span>?</div><div class="who">Diego</div></div>'
  '<div class="chatline me"><div class="bub">Sí, <span class="fx ob">la</span> quiero. <span class="gloss">(la = la camiseta)</span></div><div class="who">Tú</div></div>'
  '<div class="chatline you"><div class="bub">¿Y los <span class="fx ob">zapatos</span> negros?</div><div class="who">Diego</div></div>'
  '<div class="chatline me"><div class="bub"><span class="fx ob">Los</span> compro también. <span class="gloss">(los = los zapatos)</span></div><div class="who">Tú</div></div></div>')
P('<p style="font-size:9.6pt">② <b>Los cuatro pronombres (vervangingskaart):</b></p>')
P('<div class="fams" style="margin-top:2mm">')
P(pcard("Concordancia", '<table class="conj"><thead><tr><th>Género/número</th><th>Pronombre</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="p">m. ev.</td><td class="v">lo</td><td>el jersey → <b>lo</b> compro</td></tr>'
  '<tr><td class="p">v. ev.</td><td class="v">la</td><td>la falda → <b>la</b> compro</td></tr>'
  '<tr><td class="p">m. mv.</td><td class="v">los</td><td>los zapatos → <b>los</b> compro</td></tr>'
  '<tr><td class="p">v. mv.</td><td class="v">las</td><td>las botas → <b>las</b> compro</td></tr></tbody></table>'))
P(pcard("¿Dónde va? — los rieles", '<div class="ej"><b>1 · vóór</b> het vervoegde werkwoord:<br><i>La <b>compro</b>.</i> · <i>Los <b>quiero</b>.</i><br><b>2 · achter</b> de infinitief (vast):<br><i>Voy a comprar<b>la</b>.</i> · <i>Quiero probármelo<b>s</b>.</i></div>'
  '<div class="t2">🔴 Vóór het vervoegde ww, niet erna: <span class="trap">compro la</span> ✗ → <b>la compro</b> ✓.</div>'))
P('</div>')
P('<p style="font-size:9.6pt">③ <b>Radiografía (foutenvergrootglas):</b></p>')
P(xray('¿La camisa azul? — Sí, <span class="fx ob">la</span> <span class="fx vb">compro</span>.',
       [("la","= la camisa (v. ev.)"),("compro","werkwoord comprar"),("→","geen herhaling!")]))
P('<div class="truc"><b>🔴 me / te / se — al bekend:</b> <i>Me llamo… · ¿Te gusta?</i> En bij het passen: <i>¿Puedo <b>probármelo</b>?</i> (me + lo). De OD-pronombres <b>lo/la/los/las</b> werken net zo: ze staan vóór het vervoegde werkwoord of vast achter de infinitief.</div>')
P(regla("Regla · lo / la / los / las",
  '<p>Om de <b>prenda</b> niet te herhalen: <b>lo</b> (m. ev.), <b>la</b> (v. ev.), <b>los</b> (m. mv.), <b>las</b> (v. mv.). '
  'Plaats: <b>vóór</b> het vervoegde werkwoord (<i>La compro</i>) of <b>vast achter</b> de infinitief (<i>Voy a comprarla</i>).</p>'))
P('</div>')  # page §1.1
# §1.2 práctica + CLOZE
P('<div class="page">')
P('<div class="divider">Practicar · §1.2</div>')
P(actx(1, "¿lo, la, los o las?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Welk pronomen vervangt de prenda? Kruis aan.</p>'
  '<table class="mp"><thead><tr><th>Prenda</th><th>lo</th><th>la</th><th>los</th><th>las</th></tr></thead><tbody>'
  '<tr><td>la falda</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>el jersey</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>los vaqueros</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>las botas</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>el abrigo</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="MODELO (regel §1.1)"))
P(actx(2, "Responde con el pronombre (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Antwoord met <b>lo/la/los/las</b> + het werkwoord.</p>'
  '<p style="margin-left:12.5mm">a) ¿Compras la falda? —Sí, ___ compro.<br>'
  'b) ¿Quieres el jersey? —Sí, ___ quiero.<br>'
  'c) ¿Llevas los zapatos? —___ llevo hoy.<br>'
  'd) ¿Te pruebas las botas? —Sí, ___ pruebo.<br>'
  'e) ¿Ves el vestido del escaparate? —Sí, ___ veo.<br>'
  'f) ¿Buscas las gafas? —Sí, ___ busco.<br><span class="gloss">✅ Zelfcorrectie op de digitale pagina.</span></p>', apoyo="PISTA (m/v · ev/mv) → SIN AYUDA"))
P(actx(3, "Transforma sin repetir",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Herschrijf zonder de prenda te herhalen (zet het pronomen vóór het ww).</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>Con pronombre</th></tr></thead><tbody>'
  '<tr><td>Compro la camisa.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Quiero el cinturón.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Llevo los calcetines.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Busco las sandalias.</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="MARCO (lo/la/los/las) → SIN AYUDA"))
P(actx(4, "¿Dónde va el pronombre?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>plaatsing (rieles).</i> Kies de juiste zin. ☐ voor de goede.</p>'
  '<p style="margin-left:12.5mm">1) ☐ La compro. &nbsp; ☐ Compro la.<br>'
  '2) ☐ Voy a comprarla. &nbsp; ☐ Voy la a comprar.<br>'
  '3) ☐ Los quiero. &nbsp; ☐ Quiero los.<br>'
  '4) ☐ Quiero probármela. &nbsp; ☐ Quiero me la probar.<br><span class="gloss">✅ Zelfcorrectie op de digitale pagina.</span></p>', apoyo="MODELO → PISTA"))
P(audiorow('<div class="ic">🎧</div><div><b>En la tienda.</b> Escucha el diálogo entre el/la dependiente/-a y el cliente. ¿Qué pronombre usan? <span class="gloss">Luisterdialoog (script + TTS op de hub). 1ª globaal · 2ª detail.</span></div>',
           qr("Escanea y escucha", "Audio 6.1 · En la tienda · 1:05", seed=61)))
P(actx(5, "Escucha: ¿qué pronombre oyes?",
  [{"t":"👂 Escuchar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Kruis aan wélk pronomen je hoort in het antwoord.</p>'
  '<table class="mp"><thead><tr><th>#</th><th>lo</th><th>la</th><th>los</th><th>las</th></tr></thead><tbody>'
  '<tr><td>1</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>2</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>3</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>4</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="MODELO (vier opties open)"))
P(actx(6, "¿Es correcto? — ejemplo o no-ejemplo",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Kruis ✔ (goed) of ✘ (fout) aan en verbeter de foute.</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>✔ / ✘</th><th>Corrección</th></tr></thead><tbody>'
  '<tr><td>Compro la.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>¿La falda? La quiero.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Los zapatos, la compro.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Voy a comprarlo.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="PISTA (m/v · plaats) → SIN AYUDA"))
P(tarea_com("Tarea comunicativa · «¿Te lo llevas?»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 7 min"},{"t":"★★★"}],
  '<p><b>Afzender·ontvanger·doel·situatie·resultaat:</b> A = dependiente/a, B = cliente. A vraagt over prendas («¿Te gusta esta camisa?»), B antwoordt kort met het pronomen («Sí, la quiero» / «No, no la quiero»). Wissel. <span class="gloss">«¿Los vaqueros? —Sí, me los llevo.»</span></p>'
  '<p style="margin-left:12.5mm">Un ejemplo nuestro: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: MARCO (lo/la/los/las) → SIN AYUDA</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «¿lo, la, los o las?» (cloze), de vervangingsanimatie en «ordena el diálogo de la tienda» met zelfcorrectie.</div>')
P('</div>')  # page §1.2

retos("pronombres_u6", "§1.4 · Retos — el pronombre en el escaparate",
      'Tres retos con <b>lo, la, los, las</b>: un cartel de <b>treinta palabras exactas</b>, un anuncio de radio de <b>veinte segundos</b> y un dilema de compra.',
      'Drie retos met lo, la, los, las: een affiche van precies dertig woorden, een radiospot van twintig seconden en een koopdilemma.')

# ================= §2 · ACABAR DE + INFINITIVO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2 · Acabar de + infinitivo · net iets gedaan</span>')
P('<div class="intro"><b>ES:</b> Para decir que <b>acabas de hacer</b> algo (hace un momento) usas <b>acabar de + infinitivo</b>. La ruta: línea del tiempo → máquina → regla → practicar → comunicar. <span class="gloss">Om te zeggen dat je net iets gedaan hebt: acabar de + infinitief.</span></div>')
P(lpd(("8","taalsysteem: acabar de + infinitivo"), ("4","interactie: vertellen"), ("3","doelgericht spreken")))
P('</div>')
# §2.1
P('<h3 style="margin-top:6mm">§2.1 · La línea del tiempo — «acabo de comprar»</h3>')
P('<p style="font-size:9.6pt">① <b>Observa (tijdlijn).</b> «Acabar de» = een punt <b>net vóór nu</b>:</p>')
P(scale(["hace un rato","hace 5 min","acabo de… (recién)","AHORA"]))
P('<p style="font-size:9.6pt">② <b>La máquina (tijdlijn).</b> Neem <b>acabar</b> in het presente + <b>de</b> + infinitief:</p>')
P(machine([("persona","yo"),("acabar (presente)",'acab<span class="end">o</span>'),("+ de +","de"),("infinitivo","comprar"),("frase","acabo de comprar")]))
P('<p style="font-size:9.6pt">③ <b>La tabla de <i>acabar</i> (regelmatig, presente):</b></p>')
P('<div class="fams" style="margin-top:2mm">')
P(pcard("acabar (presente)", '<table class="conj"><tbody>'
  '<tr><td class="p">yo</td><td class="v">acabo</td></tr>'
  '<tr><td class="p">tú</td><td class="v">acabas</td></tr>'
  '<tr><td class="p">él/ella</td><td class="v">acaba</td></tr>'
  '<tr><td class="p">nosotros</td><td class="v">acabamos</td></tr>'
  '<tr><td class="p">vosotros</td><td class="v">acabáis</td></tr>'
  '<tr><td class="p">ellos</td><td class="v">acaban</td></tr></tbody></table>'))
P(pcard("La fórmula", '<div class="ej"><b>acabar</b> (acabo, acabas…) + <b>de</b> + <b>infinitivo</b>.<br>'
  '<i>Acabo de <b>comprar</b> una gorra.</i><br><i>Acabamos de <b>pagar</b> en la caja.</i><br><i>¿Acabas de <b>probarte</b> el vestido?</i></div>'
  '<div class="t2">🔴 Vergeet <b>de</b> niet: acabo <b>de</b> comprar. Tweede werkwoord = <b>infinitief</b>.</div>'))
P('</div>')
P(regla("Regla · acabar de + infinitivo",
  '<p><b>acabar</b> in het presente (acabo, acabas, acaba, acabamos, acabáis, acaban) + <b>de</b> + <b>infinitivo</b> = <i>net (zopas) iets gedaan hebben</i>. '
  '<br>🔴 <i>Acabo de llegar</i> = ik ben net aangekomen. Niet verwarren met <b>acabar</b> = eindigen.</p>'))
P('</div>')  # page §2.1
# §2.2 práctica + CLOZE
P('<div class="page">')
P('<div class="divider">Practicar · §2.2</div>')
P(actx(1, "Conjuga acabar",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Vul de vorm van <b>acabar</b> in.</p>'
  '<p style="margin-left:12.5mm">yo <span class="wl sm"></span> · tú <span class="wl sm"></span> · él <span class="wl sm"></span> · nosotros <span class="wl sm"></span> · ellos <span class="wl sm"></span></p>', apoyo="PISTA (acab-o…)"))
P(actx(2, "Substitutie: cambia la persona",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Herschrijf de zin <b>«acabo de comprar»</b> voor elke persoon.</p>'
  '<table class="mp"><thead><tr><th>Persona</th><th>… de comprar</th></tr></thead><tbody>'
  '<tr><td>tú</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>nosotros</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>ella</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>ellos</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="MARCO (tabla acabar) → SIN AYUDA"))
P(actx(3, "Completa con acabar de + infinitivo (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p>Vul <b>acabar de + infinitivo</b> aan (persoon tussen haakjes). <span class="gloss">Let op: vorm van acabar + de + infinitief.</span></p>'
  '<p style="margin-left:12.5mm">1. (Yo) <span class="wl md"></span> comprar una gorra. <i>(comprar)</i><br>'
  '2. ¿(Tú) <span class="wl md"></span> probarte el vestido? <i>(probarse)</i><br>'
  '3. (Nosotros) <span class="wl md"></span> pagar en la caja. <i>(pagar)</i><br>'
  '4. Diego <span class="wl md"></span> llegar al mercado. <i>(llegar)</i><br>'
  '5. (Ellos) <span class="wl md"></span> ver el escaparate. <i>(ver)</i><br>'
  '6. Lucía <span class="wl md"></span> encontrar unas botas. <i>(encontrar)</i><br>'
  '7. ¿(Vosotros) <span class="wl md"></span> entrar en la tienda? <i>(entrar)</i><br>'
  '8. (Yo) <span class="wl md"></span> elegir la talla M. <i>(elegir)</i></p>'
  '<p style="margin-left:12.5mm" class="gloss">✅ De oplossingen staan online (zelfcorrectie op de digitale pagina).</p>', apoyo="PISTA (vorm van acabar) → SIN AYUDA"))
P(actx(4, "Cadena de transformación",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Begin met <b>«Acabo de comprar una camisa.»</b> en voer elke opdracht uit (schrijf de hele zin).</p>'
  '<p style="margin-left:12.5mm">→ maak er een <b>vraag</b> van (tú): <span class="wl lg"></span><br>→ verander naar <b>nosotros</b>: <span class="wl lg"></span><br>→ vervang «una camisa» door een <b>pronomen</b>: <span class="wl lg"></span><br>→ zet in het <b>meervoud</b> (dos camisas → las): <span class="wl lg"></span></p>', apoyo="PISTA → SIN AYUDA"))
P(actx(5, "¿Qué acabas de hacer? — escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf drie ware zinnen: wat je vandaag <b>acabas de hacer</b> (comprar / comer / ver…).</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (Acabo de + infinitivo)"))
P(tarea_com("Tarea comunicativa · «¡Acabo de comprarlo!»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p><b>Afzender·ontvanger·doel·situatie·resultaat:</b> je komt terug van het winkelen. Vertel elkaar wat je <b>net gekocht/gedaan hebt</b> (acabar de + infinitivo) en gebruik een pronomen. <span class="gloss">«Acabo de comprar unas zapatillas. ¡Las acabo de estrenar!»</span></p>'
  '<p style="margin-left:12.5mm">Lo que acaba de hacer mi compañero/a: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: MARCO (Acabo de + inf.) → SIN AYUDA</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «acabar de + infinitivo» (cloze) en de tijdlijn-oefening met zelfcorrectie.</div>')
P('</div>')  # page §2.2

retos("acabar", "§2.4 · Retos — lo que acabas de hacer",
      'Una devolución <b>imposible</b> y unos datos de moda que cambian lo que <b>acabas de comprar</b>.',
      'Een onmogelijke terugbetaling, en modecijfers die veranderen hoe je kijkt naar wat je net kocht.')

# ================= §3 · DEMOSTRATIVOS =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3 · este / ese / aquel · cerca ↔ lejos</span>')
P('<div class="intro"><b>ES:</b> Para señalar una prenda usas <b>este</b> (cerca), <b>ese</b> (un poco lejos) o <b>aquel</b> (lejos). La ruta: distancia → tabla → practicar → comunicar. <span class="gloss">Om een kledingstuk aan te wijzen: este (dichtbij), ese (iets verder), aquel (ver).</span></div>')
P(lpd(("8","taalsysteem: demostrativos"), ("7","woordenschat: ropa/tienda"), ("4","interactie: aanwijzen")))
P('</div>')
# §3.1
P('<h3 style="margin-top:6mm">§3.1 · La distancia — los rieles del espacio</h3>')
P('<p style="font-size:9.6pt">① <b>Descubre (afstand als rails).</b> Hoe verder weg, hoe «verder» het aanwijswoord:</p>')
P(scale(["este (aquí) 👉","ese (ahí) 👉👉","aquel (allí) 👉👉👉"]))
P('<p style="font-size:9.6pt">② <b>La tabla — concuerda con la prenda (m/v · ev/mv):</b></p>')
P('<table class="conj"><thead><tr><th>Distancia</th><th>m. ev.</th><th>v. ev.</th><th>m. mv.</th><th>v. mv.</th></tr></thead><tbody>'
  '<tr><td class="p">cerca · aquí</td><td class="v">este</td><td class="v">esta</td><td class="v">estos</td><td class="v">estas</td></tr>'
  '<tr><td class="p">un poco lejos · ahí</td><td class="v">ese</td><td class="v">esa</td><td class="v">esos</td><td class="v">esas</td></tr>'
  '<tr><td class="p">lejos · allí</td><td class="v">aquel</td><td class="v">aquella</td><td class="v">aquellos</td><td class="v">aquellas</td></tr></tbody></table>')
P('<p style="font-size:9.6pt">③ <b>Contextos (contextkaarten):</b></p>')
P('<div class="fams three" style="margin-top:2mm">')
P(pcard("👉 este/esta", '<div class="ej"><i>Me gusta <b>esta</b> camiseta (aquí, en mi mano).</i></div>'))
P(pcard("👉👉 ese/esa", '<div class="ej"><i>¿Cuánto cuesta <b>ese</b> jersey (ahí, cerca de ti)?</i></div>'))
P(pcard("👉👉👉 aquel/aquella", '<div class="ej"><i><b>Aquellos</b> zapatos (allí, en el escaparate) son bonitos.</i></div>'))
P('</div>')
P('<div class="truc"><b>🔴 Concuerda con la prenda, no con la distancia:</b> <b>est<span class="trap">a</span></b> falda (v.) · <b>est<span class="trap">os</span></b> pantalones (m. mv.). Kijk naar het kledingstuk!</div>')
P(regla("Regla · este / ese / aquel",
  '<p><b>este</b> = cerca (aquí) · <b>ese</b> = un poco lejos (ahí) · <b>aquel</b> = lejos (allí). '
  'Elk woord past zich aan: este/esta/estos/estas — ese/esa/esos/esas — aquel/aquella/aquellos/aquellas.</p>'))
P('</div>')  # page §3.1
# §3.2 práctica
P('<div class="page">')
P('<div class="divider">Practicar · §3.2</div>')
P(actx(1, "¿este, esta, estos o estas?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Kies de juiste vorm van <b>este</b> (cerca). Kruis aan.</p>'
  '<table class="mp"><thead><tr><th>Prenda (aquí)</th><th>este</th><th>esta</th><th>estos</th><th>estas</th></tr></thead><tbody>'
  '<tr><td>___ jersey</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ falda</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ zapatos</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ botas</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ vestido</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="MODELO (tabla §3.1)"))
P(actx(2, "Gap-fill: cerca o lejos",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul <b>este/esta</b> (aquí), <b>ese/esa</b> (ahí) of <b>aquel/aquella</b> (allí) in.</p>'
  '<p style="margin-left:12.5mm">a) Me gusta ___ camiseta (aquí, en mi mano).<br>'
  'b) ¿Cuánto cuesta ___ gorra (ahí, a tu lado)?<br>'
  'c) ___ abrigo (allí, en el escaparate) es caro.<br>'
  'd) ___ zapatos (aquí) son cómodos.<br><span class="gloss">✅ Zelfcorrectie op de digitale pagina.</span></p>', apoyo="BANCO (este/ese/aquel + vormen)"))
P(actx(3, "Empareja: distancia ↔ demostrativo",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Situación</th><th></th><th>Palabra</th></tr></thead><tbody>'
  '<tr><td>1 · en mi mano (aquí)</td><td><span class="wl sm"></span></td><td>A · aquella</td></tr>'
  '<tr><td>2 · a tu lado (ahí)</td><td><span class="wl sm"></span></td><td>B · esta</td></tr>'
  '<tr><td>3 · en el escaparate (allí)</td><td><span class="wl sm"></span></td><td>C · esa</td></tr></tbody></table>', apoyo="BANCO"))
P(actx(4, "Transforma: este → ese → aquel",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Begin met <b>«esta camiseta»</b> en verplaats ze steeds verder weg.</p>'
  '<p style="margin-left:12.5mm">esta camiseta (aquí) → <b>ese</b>… (ahí): <span class="wl md"></span> → <b>aquel</b>… (allí): <span class="wl md"></span><br>estos zapatos (aquí) → esos (ahí): <span class="wl md"></span> → aquellos (allí): <span class="wl md"></span></p>', apoyo="MARCO → SIN AYUDA"))
P(actx(5, "Escribe: señala en la tienda",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf drie zinnen: wijs één prenda cerca, één ahí en één lejos aan (met de juiste vorm).</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (Me gusta este/ese/aquel…)"))
P(tarea_com("Tarea comunicativa · «Señala y pregunta»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p><b>Afzender·ontvanger·doel·situatie·resultaat:</b> in de tienda wijs je prendas aan en vraag je de prijs. A: «¿Cuánto cuesta <b>esa</b> chaqueta?» B antwoordt. Gebruik este/ese/aquel volgens de afstand. <span class="gloss">Beweeg door de klas als «tienda».</span></p>'
  '<p style="margin-left:12.5mm">Una pregunta nuestra: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: MARCO (¿Cuánto cuesta este/ese/aquel…?) → SIN AYUDA</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «este/ese/aquel» (cloze) en «señala en el escaparate» (point) met zelfcorrectie.</div>')
P('</div>')  # page §3.2

retos("demostrativos", "§3.4 · Retos — este, ese, aquel… ¿y cuánto?",
      'Se regatea señalando: <b>este</b> sombrero, <b>esa</b> manta. Y una talla que <b>no existe</b> donde estás.',
      'Afdingen doe je wijzend: deze hoed, die deken. En een maat die niet bestaat waar jij bent.')

# ================= §4 · CONCORDANCIA DEL ADJETIVO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4 · Concordancia · una camiseta roja de rayas</span>')
P('<div class="intro"><b>ES:</b> El adjetivo (color, forma, material) <b>concuerda</b> con la prenda: género (m/v) y número (ev/mv). La ruta: observar → tarjeta de concordancia → «Colorea la equipación» → practicar → comunicar. <span class="gloss">Kleur/vorm/materiaal komt overeen met het kledingstuk in geslacht en getal.</span></div>')
P(lpd(("8","taalsysteem: concordantie adjectief"), ("7","woordenschat: colores/materiales"), ("5","cultuur: selecciones"), ("3","doelgericht schrijven")))
P('</div>')
# §4.1
P('<h3 style="margin-top:6mm">§4.1 · La tarjeta de concordancia</h3>')
P('<p style="font-size:9.6pt">① <b>Observa (grammaticale paren).</b> De uitgang van de kleur volgt het kledingstuk:</p>')
P(obsbox([
  'un vestido <span class="hl">rojo</span> · una camiseta <span class="hl">roja</span> <span class="gloss">(m. → -o · v. → -a)</span>',
  'unos zapatos <span class="hl">rojos</span> · unas botas <span class="hl">rojas</span> <span class="gloss">(meervoud → +s)</span>',
  'una falda <span class="hl">azul</span> · unos vaqueros <span class="hl">azules</span> <span class="gloss">(azul/gris/verde: geen -o/-a)</span>',
], vragen='<b>1)</b> Wanneer -o/-a? <b>2)</b> Wat gebeurt in het meervoud? <b>3)</b> Welke kleuren veranderen NIET van geslacht?'))
P('<p style="font-size:9.6pt">② <b>La overeenkomst-kaart (AgreementMap):</b></p>')
P('<div class="agree"><div class="w">una <u>camisa</u> blanc<u>a</u> de <u>ray</u>as</div><div class="tie">v. ev. → blanc<b>a</b> · patrón: de rayas</div></div>')
P('<table class="mp"><thead><tr><th>Prenda</th><th>+ color</th><th>+ patrón/material</th></tr></thead><tbody>'
  '<tr><td>el vestido (m.)</td><td class="v">rojo / azul</td><td>de lunares / de seda</td></tr>'
  '<tr><td>la camisa (v.)</td><td class="v">roja / azul</td><td>de rayas / de algodón</td></tr>'
  '<tr><td>los zapatos (m. mv.)</td><td class="v">rojos / azules</td><td>de cuero</td></tr>'
  '<tr><td>las botas (v. mv.)</td><td class="v">rojas / azules</td><td>de cuadros</td></tr></tbody></table>')
P('<div class="truc"><b>🔴 Twee soorten kleuren:</b> (1) kleuren op -o veranderen: <b>rojo/roja/rojos/rojas</b>, blanco, negro, amarillo, morado. (2) De rest verandert <b>niet</b> van geslacht: <b>azul, gris, verde, marrón, naranja, rosa, celeste</b> — enkel meervoud +s/+es: <i>faldas azules, zapatos grises</i>.</div>')
P(regla("Regla · concordancia del adjetivo",
  '<p>Het adjectief (kleur, vorm, materiaal) komt overeen met de prenda in <b>geslacht</b> (m/v) en <b>getal</b> (ev/mv). '
  'Kleuren op <b>-o</b>: rojo → roja → rojos → rojas. Andere kleuren (azul, gris, verde…): enkel meervoud (+s/+es). Patronen met <b>de</b> (de rayas, de cuadros) veranderen niet.</p>'))
P('</div>')  # page §4.1
# §4.2 PAREL-1 equipación
P('<div class="page">')
P('<div class="divider">PAREL · §4.2 · Colorea la equipación 🎽</div>')
P('<p style="font-size:9.6pt">② <b>«Colorea la equipación» (collocaties · cultura del fútbol).</b> Elke selección heeft een <b>camiseta</b> met een <b>color</b> en soms een <b>patrón</b> (de rayas · de cuadros · de lunares · liso). Schrijf de <b>concordantie</b> correct (la camiseta is v.). <span class="gloss">Kleur de shirts en schrijf de kleur + patroon correct — let op de v.-uitgang.</span></p>')
P(actx(1, "Grupo A · el mundo hispano",
  [{"t":"🎨 Colorear","skill":True},{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p>Kleur het shirt (□) en vul de kleur/patroon in (v.: <b>-a</b> waar nodig).</p>'
  '<table class="alf"><thead><tr><th>Selección</th><th>Color</th><th>Patrón</th><th>«La camiseta es…»</th></tr></thead><tbody>'
  '<tr><td>🇦🇷 Argentina</td><td>celeste</td><td>de rayas</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>🇪🇸 España</td><td>rojo</td><td>lisa</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>🇨🇴 Colombia</td><td>amarillo</td><td>lisa</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>🇲🇽 México</td><td>verde</td><td>lisa</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>🇺🇾 Uruguay</td><td>celeste</td><td>lisa</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>🇨🇱 Chile</td><td>rojo</td><td>lisa</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>🇵🇪 Perú</td><td>blanco</td><td>con una banda roja</td><td><span class="wl md"></span></td></tr></tbody></table>'
  '<p style="margin-left:12.5mm" class="gloss">Modelo: 🇦🇷 → «La camiseta es <b>celeste, de rayas</b>.» · 🇪🇸 → «La camiseta es <b>roja, lisa</b>.»</p>', apoyo="MODELO → SIN AYUDA"))
P(actx(2, "Grupo B · Top de la FIFA",
  [{"t":"🎨 Colorear","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Idem: schrijf «La camiseta es + color (+ patrón)».</p>'
  '<table class="alf"><thead><tr><th>Selección</th><th>Color</th><th>Patrón</th><th>«La camiseta es…»</th></tr></thead><tbody>'
  '<tr><td>🇫🇷 Francia</td><td>azul</td><td>lisa</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>🇳🇱 Países Bajos</td><td>naranja</td><td>lisa</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>🇧🇪 Bélgica</td><td>rojo</td><td>lisa</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>🇭🇷 Croacia</td><td>rojo</td><td>de cuadros</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>🇮🇹 Italia</td><td>azul</td><td>lisa</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>🇧🇷 Brasil</td><td>amarillo</td><td>lisa</td><td><span class="wl md"></span></td></tr></tbody></table>'
  '<p style="margin-left:12.5mm" class="gloss">🔴 Let op: 🇫🇷 azul → «azul» (geen -a) · 🇭🇷 «roja, de cuadros» · 🇧🇷 «amarilla, lisa».</p>', apoyo="PISTA (azul verandert niet) → SIN AYUDA"))
P(actx(3, "Concordancia: color ↔ prenda (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Vul de kleur in de juiste vorm in (tussen haakjes de basis).</p>'
  '<p style="margin-left:12.5mm">1. una camiseta <span class="wl sm"></span> <i>(rojo)</i> &nbsp; 2. unos pantalones <span class="wl sm"></span> <i>(negro)</i><br>'
  '3. una falda <span class="wl sm"></span> <i>(azul)</i> &nbsp; 4. unas botas <span class="wl sm"></span> <i>(marrón)</i><br>'
  '5. un vestido <span class="wl sm"></span> <i>(blanco)</i> &nbsp; 6. unos calcetines <span class="wl sm"></span> <i>(verde)</i><br><span class="gloss">✅ Zelfcorrectie op de digitale pagina.</span></p>', apoyo="PISTA (m/v · ev/mv) → SIN AYUDA"))
P(actx(4, "Clasifica: ¿cambia de género o no?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Sorteer de kleuren: verandert de kleur van geslacht (rojo/roja) of niet (azul)? '
  '<span class="words"><b>rojo · azul · negro · gris · amarillo · verde · blanco · marrón · morado</b></span></p>'
  + sortcols([("cambia (-o / -a)","rojo → roja"),("no cambia","azul, azul")]), apoyo="BANCO → +1 eigen kleur"))
P(actx(5, "Describe una prenda del escaparate",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Beschrijf drie prendas met kleur + patroon/materiaal (let op concordantie).</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (una … + color + de …) → SIN AYUDA"))
P(tarea_com("Tarea comunicativa · «¿De qué color es tu equipación?»",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p><b>Afzender·ontvanger·doel·situatie·resultaat:</b> beschrijf de <b>camiseta</b> van je lievelingsploeg (of van je school) met kleur + patroon; je buur raadt de selección/ploeg. <span class="gloss">«Mi camiseta es azul y blanca, de rayas. ¿Qué selección es?»</span></p>'
  '<p style="margin-left:12.5mm">Mi equipación: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: MARCO (Mi camiseta es + color + de + patrón) → SIN AYUDA</div>'))
P(actx(6, "Traduce y concuerda",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>NL → ES met concordantie.</i> Vertaal en let op de uitgang van de kleur.</p>'
  '<table class="mp"><thead><tr><th>Nederlands</th><th>Español</th></tr></thead><tbody>'
  '<tr><td>een rode rok</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>zwarte schoenen</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>een blauwe jurk</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>witte sokken</td><td><span class="wl md"></span></td></tr></tbody></table>'
  '<p style="margin-left:12.5mm" class="gloss">✅ De oplossingen staan online (zelfcorrectie op de digitale pagina).</p>', apoyo="PISTA (m/v · ev/mv) → SIN AYUDA"))
P('<div class="route-note">🎮 <b>Juega online:</b> «color + prenda» (match), de concordancia-Tetris en «masculino/femenino» met zelfcorrectie.</div>')
P('</div>')  # page §4.2

retos("concordancia_u6", "§4.4 · Retos — la ropa que te delata",
      'Dos retos de concordancia: una <b>equipación</b> descrita solo por colores, y un <b>armario</b> que dice quién eres.',
      'Twee retos over overeenkomst: een voetbaltruitje enkel in kleuren beschreven, en een kast die verraadt wie je bent.')

# ================= §5 · LECTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">📖</span><span class="pk">§5 · Lectura — «¡Rebajas! + una reseña»</span>')
P('<div class="intro"><b>ES:</b> Vas a leer un <b>anuncio de rebajas</b> (una tienda) y una <b>reseña</b> (un cliente). Primero <b>predices</b>, después lees con un <b>objetivo</b>. <span class="gloss">Je leest een soldenadvertentie en een klantenreview: eerst voorspellen, dan doelgericht lezen. gelaagde teksten · tekstsoorten.</span></div>')
P(lpd(("1","onderwerp/hoofdgedachte bij lezen"), ("2","relevante info selecteren"), ("3","doelgericht schrijven met steun")))
P('</div>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> anuncio (rebajas) · reseña</span><span class="tm"><b>De:</b> una tienda · un cliente</span><span class="tm">🎯 buscar ofertas y opiniones</span></div>')
P(actx(1, "Antes de leer: predice",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★☆☆"}],
  '<p>Bekijk de vorm en titels. ¿Qué información esperas encontrar en un anuncio de rebajas?</p>'
  '<p style="margin-left:12.5mm">Espero leer sobre: <span class="wl full"></span></p>', apoyo="MODELO (precios, descuentos, ropa…)"))
P('<div class="fichacard">'
  '<div><div class="se" style="margin:0 0 2mm">📣 Anuncio · Tienda «Moda Diego» 🇲🇽</div>'
  '<div class="row"><span class="k">¡GRANDES REBAJAS!</span><span class="v">hasta −50 %</span></div>'
  '<div class="row"><span class="v">Camisetas de algodón</span><span class="k">10 € → <b>5 €</b></span></div>'
  '<div class="row"><span class="v">Vaqueros azules</span><span class="k">40 € → <b>25 €</b></span></div>'
  '<div class="row"><span class="v">Zapatillas blancas</span><span class="k">60 € → <b>39 €</b></span></div>'
  '<div class="row"><span class="v">Vestidos de lunares</span><span class="k">35 € → <b>20 €</b></span></div>'
  '<div class="row"><span class="k">Pago</span><span class="v">tarjeta o en efectivo · ¡se puede regatear!</span></div></div>'
  '<div><div class="se" style="margin:0 0 2mm">⭐ Reseña · @valen_style 🇨🇴 · ★★★★☆</div>'
  '<div class="ej" style="font-size:9.3pt">«Acabo de comprar unos <span class="evi">vaqueros azules</span> en las <span class="evi">rebajas</span> de Moda Diego. Estaban a <span class="evi">25 €</span> (¡antes 40!). Me los <span class="evi">probé</span> en el probador y me quedan muy bien. El <span class="evi">dependiente</span> es simpático y pagué <span class="evi">con tarjeta</span>. La camiseta lisa no la compré porque no <span class="evi">la</span> tenían en mi talla. ¡Vuelvo seguro!»</div></div></div>')
P('<div class="lecdoel">🎯 <b>Objetivo de lectura:</b> lees om te <b>vinden</b> welke prijzen en kortingen er zijn en wat de klant <b>wel/niet</b> kocht — je hoeft niet élk woord te begrijpen.</div>')
P('</div>')  # page §5a
P('<div class="page">')
P(actx(2, "Escanea: completa la tabla de precios",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Zoek de prijzen (antes → ahora) in het anuncio.</p>'
  '<table class="mp"><thead><tr><th>Prenda</th><th>Antes</th><th>Ahora (rebaja)</th></tr></thead><tbody>'
  '<tr><td>camisetas de algodón</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>vaqueros azules</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>zapatillas blancas</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>vestidos de lunares</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>', apoyo="MODELO (anuncio boven)"))
P(actx(3, "¿Verdadero o falso? + prueba",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>juist/fout + bewijs (evidence).</i> Waar of niet waar? Noteer de <b>woorden uit de tekst</b> die het bewijzen.</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba</th></tr></thead><tbody>'
  '<tr><td>Valen compró unos vaqueros.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Los vaqueros costaban 40 € antes.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Valen compró la camiseta lisa.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Pagó con tarjeta.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="PISTA (onderstreep in de tekst)"))
P(actx(4, "Del contexto: ¿qué significa?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Wat betekent <b>«me quedan bien»</b> en <b>«regatear»</b>? Kies + leg uit welke aanwijzing hielp.</p>'
  '<p style="margin-left:12.5mm">me quedan bien = ☐ ze staan me goed ☐ ze zijn duur &nbsp;·&nbsp; regatear = ☐ afdingen ☐ betalen<br>Pista que me ayudó: <span class="wl lg"></span></p>', apoyo="PISTA"))
P(actx(5, "Del anuncio: ¿la, lo, los o las?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>terugkoppeling §1.</i> In de reseña staat «no <b>la</b> tenían». Waar verwijst <b>la</b> naar? En vul aan: «Me <b>los</b> probé» → los = ___?</p>'
  '<p style="margin-left:12.5mm">«la» = <span class="wl md"></span> &nbsp;·&nbsp; «los» = <span class="wl md"></span><br><span class="gloss">✅ Zelfcorrectie op de digitale pagina.</span></p>', apoyo="PISTA (zoek de prenda ervoor)"))
P(tarea_com("Tarea comunicativa · «Escribe tu reseña» (keten lezen→schrijven)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b>Keten lezen → schrijven.</b> Schrijf een korte <b>reseña</b> (3–4 zinnen) over een prenda die je «net gekocht hebt»: wat, welke kleur, hoeveel, hoe ze zit, en of je terugkomt. Gebruik <b>acabar de</b> + een <b>pronomen</b>. <span class="gloss">«Acabo de comprar una chaqueta negra. Me queda bien. La pagué con tarjeta.»</span></p>'
  '<div class="wbox sm"></div>'
  '<div class="steun" style="margin-left:0mm">Apoyo: MODELO (reseña de Valen) → SIN AYUDA</div>'))
P(actx(6, "Después de leer: ¿qué prenda es?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Verbind de omschrijving uit het anuncio met de prenda (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Descripción</th><th></th><th>Prenda</th></tr></thead><tbody>'
  '<tr><td>1 · de algodón, 5 € en rebajas</td><td><span class="wl sm"></span></td><td>A · los vaqueros azules</td></tr>'
  '<tr><td>2 · azules, 40 € → 25 €</td><td><span class="wl sm"></span></td><td>B · las zapatillas blancas</td></tr>'
  '<tr><td>3 · blancas, 39 €</td><td><span class="wl sm"></span></td><td>C · la camiseta</td></tr>'
  '<tr><td>4 · de lunares, 20 €</td><td><span class="wl sm"></span></td><td>D · el vestido</td></tr></tbody></table>', apoyo="MODELO (anuncio §5a)"))
P('<div class="route-note">🎮 <b>Sigue online:</b> luister het anuncio (TTS), lees de reseña en neem je eigen review op (recorder) op de digitale pagina.</div>')
P('</div>')  # page §5b

# ================= TALLER DE LENGUA =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num" style="color:var(--crema)">✎</span><span class="pk" style="background:var(--gd)">Taller de lengua</span>')
P('<div class="intro"><b>ES:</b> Dos herramientas: la <b>sílaba tónica</b> (agudas · llanas · esdrújulas) con la trampa del <b>plural</b>, y los <b>conectores</b> (y→e · o→u · pero/sino · así que/por eso). <span class="gloss">Klemtoon + spelling van het meervoud, en verbindingswoorden.</span></div>')
P(lpd(("8","taalsysteem: ortografía + conectoren"), ("3","tekst verbinden")))
P('</div>')
P('<h3 style="margin-top:6mm">Ortografía · la sílaba tónica — agudas, llanas, esdrújulas</h3>')
P('<p style="font-size:9.6pt">① <b>¿Dónde está el golpe de voz?</b> (lettergreeppuzzel)</p>')
P('<table class="mp"><thead><tr><th>Tipo</th><th>Golpe de voz</th><th>Ejemplo (ropa)</th></tr></thead><tbody>'
  '<tr><td><b>aguda</b></td><td>laatste lettergreep</td><td>pan-ta-<b>lón</b> · a-<b>zul</b> · mar-<b>rón</b></td></tr>'
  '<tr><td><b>llana</b></td><td>voorlaatste</td><td><b>fal</b>-da · <b>ne</b>-gro · <b>bo</b>-tas</td></tr>'
  '<tr><td><b>esdrújula</b></td><td>voor-voorlaatste (altijd tilde)</td><td><b>sá</b>-ba-do · <b>ú</b>l-ti-mo</td></tr></tbody></table>')
P('<div class="truc"><b>🔴 La trampa del plural:</b> soms verhuist de klemtoon-regel: <b>el marrón → los marrones</b> (aguda → llana, tilde weg!) · <b>el pantalón → los pantalones</b>. Maar <b>el jersey → los jerséis</b>. Kijk goed naar de tilde in het meervoud.</div>')
P(actx(1, "Clasifica: aguda, llana o esdrújula",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Sorteer: <span class="words"><b>camisa · pantalón · sábado · azul · botas · marrón</b></span></p>'
  + sortcols([("aguda","laatste"),("llana","voorlaatste"),("esdrújula","voor-voorl.")], eigen=False), apoyo="BANCO"))
P(actx(2, "El plural con tilde",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Zet in het meervoud (let op de tilde!).</p>'
  '<p style="margin-left:12.5mm">el pantalón → <span class="wl md"></span> · el marrón → <span class="wl md"></span> · el cinturón → <span class="wl md"></span><br><span class="gloss">Let op: los pantalones · los marrones · los cinturones (tilde weg).</span></p>', apoyo="PISTA (tilde valt weg) → SIN AYUDA"))
P('<h3 style="margin-top:6mm">Conectores · y→e · o→u · pero / sino · así que / por eso</h3>')
P('<table class="mp"><thead><tr><th>Conector</th><th>Uso</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td><b>y → e</b></td><td>«en» vóór i-/hi-</td><td>zapatos <b>e</b> hijos · madre <b>e</b> hija</td></tr>'
  '<tr><td><b>o → u</b></td><td>«of» vóór o-/ho-</td><td>siete <b>u</b> ocho · mujer <b>u</b> hombre</td></tr>'
  '<tr><td><b>pero / sino</b></td><td>maar / maar wel (na ontkenning)</td><td>No es roja <b>sino</b> rosa.</td></tr>'
  '<tr><td><b>así que / por eso</b></td><td>dus</td><td>Hay rebajas, <b>así que</b> compro.</td></tr></tbody></table>')
P('<div class="truc"><b>🔴 NL-valstrik:</b> «dus» = <b>así que / por eso</b> (niet <span class="trap">luego</span>). «want» én «omdat» = <b>porque</b>. Na een ontkenning: «maar wel» = <b>sino</b> (No es azul, <b>sino</b> verde).</div>')
P(actx(3, "Une con el conector correcto (gap-fill)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul in: <b>e · u · pero · sino · así que · por eso</b>.</p>'
  '<p style="margin-left:12.5mm">a) Compro una camisa ___ hijos… (¡nee: «e» vóór i-) → madre ___ hija.<br>'
  'b) ¿Quieres siete ___ ocho camisetas?<br>'
  'c) No es azul, ___ verde.<br>'
  'd) Hay rebajas, ___ me lo llevo.<br><span class="gloss">✅ Zelfcorrectie op de digitale pagina.</span></p>', apoyo="BANCO"))
P(actx(4, "Dictado corto de la tienda",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>dictee (reconstrueren).</i> Escucha y escribe cuatro palabras de ropa (met de juiste tilde).</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl md"></span> 2. <span class="wl md"></span> 3. <span class="wl md"></span> 4. <span class="wl md"></span></p>', apoyo="MODELO (2×)"))
P(actx(5, "Escribe: dos prendas con conector",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Schrijf twee zinnen over kleding, elk met een <b>conector</b> (pero · así que · sino · por eso).</p>'
  '<div class="wbox sm"></div>', apoyo="SIN AYUDA"))
P('<div class="route-note">🎮 <b>Practica online:</b> «sílaba tónica» en de conectoren-oefeningen met zelfcorrectie.</div>')
P('</div>')  # page Taller

# ================= §6 LECTURA · §7 ESCUCHA =================
# Zelfde bron als de digitale hub (lectura_data / escucha_data): papier en scherm
# kunnen zo niet uit elkaar lopen. Elk op een eigen bladzijde (§14).
P('<div class="page"><div class="parada sec">')
P('<span class="num">6</span><span class="pk">§6 · Lectura — «Cinco trucos para ir de rebajas»</span>')
P('<div class="intro"><b>ES:</b> Un artículo de consejos de una revista juvenil. <b>No hace falta entenderlo todo</b> para sacar la información. <span class="gloss">Een tipsartikel uit een jeugdblad. Je hoeft niet alles te begrijpen — weeg elke tip: past hij bij jou?</span></div>')
P(PB.lectura_print(LD.C5_U6, "1"))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">7</span><span class="pk">§7 · Escucha — «En el probador»</span>')
P('<div class="intro"><b>ES:</b> Nina se prueba ropa y Valen le dice la verdad. <b>Escucha primero, escribe después.</b> <span class="gloss">Nina past kleren en Valen zegt eerlijk wat ze ervan vindt. Eerst luisteren, dan schrijven; het transcript staat online en gaat pas open ná de taken.</span></div>')
P(PB.escucha_print(ED.C5_U6, "1"))
P('</div>')

# ================= CULTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">★</span><span class="pk">Cultura · Rebajas, regateo y tianguis</span>')
P('<div class="intro"><b>ES:</b> Comprar es también cultura. Descubre las <b>rebajas</b>, el arte de <b>regatear</b>, los <b>tianguis</b> de México (palabra <b>náhuatl</b>) y la <b>moda sostenible</b>. <span class="gloss">Winkelen is ook cultuur: solden, afdingen, de tianguis en duurzame mode.</span></div>')
P(lpd(("5","kenmerkende aspecten van de cultuur"), ("2","relevante info uit een tekst")))
P('</div>')
P('<div class="fams" style="margin-top:6mm">')
P(pcard("🏷️ Las rebajas", '<div class="ej">Dos veces al año hay <b>rebajas</b> (enero y julio en España). Precios con <b>descuento</b>: −30 %, −50 %… La gente hace cola en las tiendas.</div><div class="anchor gloss">Rebajas = solden — jacht op koopjes.</div>'))
P(pcard("🤝 El regateo", '<div class="ej">En el <b>mercado</b> o el <b>tianguis</b> se puede <b>regatear</b>: «¿Me hace un descuento?». En una tienda con etiqueta, <b>no</b> se regatea.</div><div class="t2">🔴 Regatear = afdingen — enkel op de markt, niet in de winkel.</div>'))
P('</div>')
P('<p style="font-size:9.6pt">① <b>El tianguis — una palabra náhuatl (sleutelwoord):</b></p>')
P('<div class="fichacard"><div><div class="row"><span class="k">tianguis</span><span class="v">del náhuatl <i>tiānquiztli</i></span></div>'
  '<div class="row"><span class="k">¿qué es?</span><span class="v">mercado al aire libre, itinerante</span></div>'
  '<div class="row"><span class="k">¿dónde?</span><span class="v">México, desde tiempos aztecas</span></div></div>'
  '<div><div class="row"><span class="k">se vende</span><span class="v">ropa, comida, artesanía</span></div>'
  '<div class="row"><span class="k">se paga</span><span class="v">en efectivo · se regatea</span></div>'
  '<div class="row"><span class="k">un refrán</span><span class="v">«Lo barato sale caro.»</span></div></div></div>')
P('<p style="font-size:9.6pt">② <b>Moda rápida ↔ moda sostenible + refranes:</b></p>')
P(vpairs([("la moda rápida (fast fashion)","la moda sostenible ♻️"),("ropa nueva","ropa de segunda mano"),("«El hábito no hace al monje»","(= kleren maken de man niet)"),("«Lo barato sale caro»","(= goedkoop is duurkoop)")]))
P(actx(1, "Comprensión — verdadero o falso",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Waar of niet waar? Verbeter de foute.</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Corrección</th></tr></thead><tbody>'
  '<tr><td>«Tianguis» viene del náhuatl.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>En una tienda con etiqueta se regatea.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>La moda sostenible respeta el planeta.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="MODELO (tekst boven)"))
P(actx(2, "La moda en mi vida",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Schrijf 2–3 zinnen: ¿compras ropa nueva o de segunda mano? ¿regateas? ¿te gusta la moda sostenible? Presenteer aan je buur.</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (Compro… · (No) regateo… · Me gusta…) → SIN AYUDA"))
P(actx(3, "Empareja: refrán ↔ significado",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind het refrán met de betekenis (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Refrán</th><th></th><th>Significado</th></tr></thead><tbody>'
  '<tr><td>1 · «Lo barato sale caro»</td><td><span class="wl sm"></span></td><td>A · kleren maken de man niet</td></tr>'
  '<tr><td>2 · «El hábito no hace al monje»</td><td><span class="wl sm"></span></td><td>B · goedkoop is duurkoop</td></tr>'
  '<tr><td>3 · «De tal palo, tal astilla»</td><td><span class="wl sm"></span></td><td>C · de appel valt niet ver van de boom</td></tr></tbody></table>', apoyo="BANCO"))
P('<div class="route-note">🎮 <b>Sigue online:</b> «prenda ↔ tienda» (match) en de mercado-spellen op de digitale pagina.</div>')
P('</div>')  # page Cultura

retos("cultura_u6", "Retos — el cliente que no se rinde",
      'Cinco clientes imposibles. Uno detrás de otro, sin repetir la misma frase.',
      'Vijf onmogelijke klanten. De een na de ander, zonder één zin te herhalen.')

# ================= TAREA FINAL =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num">✦</span><span class="pk" style="background:var(--gd)">Tarea final · Abre tu tienda</span>')
P('<div class="intro"><b>ES:</b> Abre tu propia <b>tienda</b>: un nombre, un <b>escaparate</b> (con precios), un <b>anuncio de rebajas</b>, y un <b>diálogo</b> vendedor ↔ cliente. Al final, escribe una <b>reseña</b>. <span class="gloss">Open je eigen winkel: naam, etalage, advertentie, klantendialoog en een review.</span></div>')
P('<div class="route-note">🎯 <b>Communicatieve taak:</b> afzender = jij (de winkel) · ontvanger = de cliente · doel = kleding aanbieden & verkopen · situatie = una tienda / un tianguis en México · resultaat = escaparate + anuncio + gespeelde dialoog + reseña.</div>')
P(lpd(("3","doelgericht schrijven met een voorbeeld"), ("4","mondeling interageren (verkopen)"), ("7","woordenschat ropa/tienda"), ("8","lo/la/los/las · concordantie · acabar de")))
P('</div>')
P('<ol class="pasos">'
  '<li><b>Elige un nombre</b> voor je winkel en een estilo (deportivo, elegante, sostenible…).</li>'
  '<li><b>Diseña el escaparate</b>: 4 prendas met <b>color/patrón</b> en <b>precio</b> (let op concordantie).</li>'
  '<li><b>Escribe un anuncio de rebajas</b> (antes → ahora, descuento).</li>'
  '<li><b>Escribe el diálogo</b> (vendedor ↔ cliente): saludar → mostrar (este/ese) → probador → precio/regateo → «me lo llevo».</li>'
  '<li><b>Representa</b> la escena en pareja (of neem audio op) y escribe una <b>reseña</b> de la tienda de tu compañero/a.</li></ol>')
P('<div class="se" style="margin-top:4mm">Mi escaparate <span class="gloss" style="font-size:8pt">· vul de prendas + kleur + prijs in</span></div>')
P('<table class="alf"><thead><tr><th>Prenda</th><th>Color / patrón</th><th>Precio</th></tr></thead><tbody>'
  '<tr><td><span class="wl md"></span></td><td><span class="wl md"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td><span class="wl md"></span></td><td><span class="wl md"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td><span class="wl md"></span></td><td><span class="wl md"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td><span class="wl md"></span></td><td><span class="wl md"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>')
P('<div class="se" style="margin-top:5mm">Mi anuncio de rebajas <span class="gloss" style="font-size:8pt">· antes → ahora</span></div><div class="wbox sm"></div>')
P('<div class="se" style="margin-top:5mm">Nuestro diálogo <span class="gloss" style="font-size:8pt">· vendedor ↔ cliente</span></div><div class="wbox"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba la escena</b> en la página digital (recorder + rúbrica).</div>',
           qr("Escanea y graba", "Tarea · Abre tu tienda", seed=64)))
P('<div class="se" style="margin-top:5mm">Mini-encuesta: la ropa favorita de la clase <span class="gloss" style="font-size:8pt">— vraag 5 klasgenoten, teken de balken</span></div>')
P(gustobars([("las zapatillas", 60), ("los vaqueros", 50), ("las camisetas", 45), ("los vestidos", 30)]))
P('<p style="font-size:8.6pt" class="gloss">↳ vervang de voorbeeld-balken door je eigen resultaten (aantal /5 → %).</p>')
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Mijn escaparate heeft <b>4 prendas</b> met <b>kleur + prijs</b> (concordantie)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>lo/la/los/las</b> in de dialoog</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>este/ese/aquel</b> en <b>acabar de</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>speel de scène</b> vlot in pareja</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — la tienda de mi compañero/a</div>'
  '<table><thead><tr><th>Lo que me gusta de su tienda</th><th>Un consejo (una cosa)</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('</div>')  # page Tarea

# ================= REPASO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">✓</span><span class="pk">Repaso · lo esencial</span>')
P('<div class="intro"><b>ES:</b> Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, 16 juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag.</span></div>')
P('</div>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>lo/la/los/las:</b> ¿la falda? → <b>La</b> compro. ¿Los zapatos? → <b>Los</b> quiero. Vóór het vervoegde ww of vast achter de infinitief (comprar<b>la</b>).</li>'
  '<li><b>acabar de + infinitivo:</b> acabo/acabas/acaba… + <b>de</b> + infinitief = net (zopas) iets gedaan: <i>Acabo de comprar.</i></li>'
  '<li><b>este/ese/aquel:</b> este (aquí) · ese (ahí) · aquel (allí) — past bij de prenda (este/esta/estos/estas…).</li>'
  '<li><b>Concordancia:</b> camiseta roj<b>a</b> · zapatos roj<b>os</b>. Kleuren op -o veranderen; azul/gris/verde/marrón/naranja/rosa niet (enkel mv. +s/+es).</li>'
  '<li><b>Las trampas:</b> 🔴 la compro (niet «compro la») · 🔴 acabo <b>de</b> comprar · 🔴 una falda azul (niet «azula») · 🔴 los pantalones (tilde weg) · 🔴 «dus» = así que/por eso.</li></ul></div>')
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> 16 spelletjes met zelfcorrectie en spreiding op de digitale pagina.</div>')
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td><b>ropa y colores</b> benoemen (camiseta, vaqueros, rojo)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>lo/la/los/las</b> gebruiken (la compro)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>zeggen wat ik <b>acabo de hacer</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>este/ese/aquel</b> gebruiken (afstand)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>de <b>concordancia</b> van kleur/patroon toepassen</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil de U6: <span class="wl md"></span> · Lo más difícil: <span class="wl md"></span></i></div>')
P('<div class="bridge"><b>» Siguiente parada: Cartagena, Colombia (U7).</b> Ya sabes comprar ropa; en <b>U7 «Mi casa y mi barrio»</b> descubres la casa, el barrio y cómo describir dónde vives. <span class="gloss">In U7 verhuis je naar Cartagena en beschrijf je je huis en buurt.</span></div>')
P('</div>')  # page Repaso

# ================= §V VOCABULARIO =================
import json
VOC = json.load(open(f"{HERE}/u6_vocab.json", encoding="utf-8"))
GRP = [("ropa","La ropa · prendas"),("calzado","El calzado y los complementos"),("colores","Los colores"),
       ("material","Formas, materiales y estampados"),("tiendas","Las tiendas"),("tienda","En la tienda · la compra"),
       ("compra","Verbos y expresiones de la compra"),("mexico","De compras en México y la moda")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (receptief & productief)")))
P('</div>')
P('<p style="font-size:9.6pt">La <b>compra</b> als netwerk — drie families die de hele unit dragen:</p>')
P(clusters([
  ("👕","La ropa",["camiseta · camisa · jersey","pantalones · falda · vestido","zapatos · botas · gorra"],"Wat je draagt."),
  ("🎨","Colores & patrones",["rojo · azul · verde","de rayas · de cuadros","de algodón · de lana"],"Hoe het eruitziet."),
  ("🏬","En la tienda",["la talla · el probador","las rebajas · el descuento","¿cuánto cuesta? · me lo llevo"],"Wat je zegt & doet."),
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
  '<p>Schrijf de vertaling. la falda = <span class="wl md"></span> · las rebajas = <span class="wl md"></span> · el probador = <span class="wl md"></span> · de rayas = <span class="wl md"></span></p>', apoyo="MODELO"))
P(actx("V.2", "Distinguir — sorteer per familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Sorteer: <span class="words"><b>la camiseta · el probador · rojo · las botas · de cuadros · la caja</b></span></p>'
  + sortcols([("ropa/calzado",""),("color/patrón",""),("en la tienda","")], eigen=False), apoyo="BANCO"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het Spaanse woord aan (beginletter gegeven). de maat = <b>t</b>___ · de solden = <b>r</b>___ · de handtas = <b>b</b>___ · afdingen = <b>r</b>___<br><span class="wl full"></span></p>', apoyo="LETRA INICIAL"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Maak één correcte zin met <b>acabar de · la talla · me lo llevo</b>.</p><div class="wbox sm"></div>', apoyo="SIN AYUDA"))
P(actx("V.5", "Comunicar — mi tienda ideal",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Schrijf jouw ideale outfit (3 prendas + color) met <b>me gusta / me lo llevo</b> én telkens waarom. Zeg het daarna hardop tegen je buur, die als dependiente reageert.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>', apoyo="MARCO (Me gusta … porque …) → SIN AYUDA"))
P(actx("V.6", "Bingo del vocabulario",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Kies uit elke rij één woord dat bij de categorie hoort en omcirkel het.</p>'
  '<table class="mp"><thead><tr><th>Categoría</th><th colspan="3">Opciones</th></tr></thead><tbody>'
  '<tr><td><b>calzado</b></td><td>la falda</td><td>las botas</td><td>el probador</td></tr>'
  '<tr><td><b>un color</b></td><td>morado</td><td>la caja</td><td>la talla</td></tr>'
  '<tr><td><b>en la tienda</b></td><td>el jersey</td><td>las rebajas</td><td>de lana</td></tr>'
  '<tr><td><b>un patrón</b></td><td>de cuadros</td><td>el bolso</td><td>la gorra</td></tr></tbody></table>'
  '<p style="margin-left:12.5mm" class="gloss">✅ De oplossingen staan online (zelfcorrectie op de digitale pagina).</p>', apoyo="BANCO"))
P(mispal("Mis palabras de la unidad", 4))
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Sigue en la página digital:</span> <span class="g">flip cards (ES↔NL), audio en de 16 spellen bouwen de steun verder af.</span></div></div>')
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
   var html='<!doctype html>\n'+clone.outerHTML;
   var blob=new Blob([html],{type:'text/html'}); var a=document.createElement('a');
   a.href=URL.createObjectURL(blob); a.download='U6_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Español en la práctica · U6 De tiendas</title><style>'
        + CSS + PB.CSS + RP.CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/U6.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes")
