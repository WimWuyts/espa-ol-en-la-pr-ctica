#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de print-HTML U2.html (C5 · Unidad 2 «Mi gente») → PDF via Chromium.
# Zelfde componentenkit/pijplijn als golden sample U0/U1 (cursus-print.css). Fonts base64 ingebed,
# cast-avatars inline SVG (cast_gen). Cursuskleur = groen (C5). Output = standalone bewerkbare U2.html.
import os, sys, base64, math
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f"{ROOT}/02-huisstijl/beeld/generators")
import cast_gen as C
import sys as _sys
_sys.path.insert(0, "/home/user/espa-ol-en-la-pr-ctica/03-build/web")
import qr_print as QRP; QRP.fijar("C5", 2)
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

.regla,.truc,.pcard,.call,.qr,.guide,.esen,.audiorow,.wcols,.wbox,.sem,.acthead,.chatline,.fichacard{ break-inside:avoid; }

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
/* clocks (la hora) */
.clockrow{ display:flex; gap:5mm; flex-wrap:wrap; margin:3mm 0; align-items:flex-start; }
.clockcard{ text-align:center; } .clockcard .cw{ width:24mm; margin:0 auto; } .clockcard svg{ width:100%; height:auto; display:block; }
.clockcard .es{ font-family:var(--disp); font-weight:700; font-size:9.6pt; color:var(--gd); margin-top:1mm; }
.clockcard .nl{ font-size:7.6pt; color:var(--mut); }
/* ===== leesvaardigheid (Lectura) ===== */
.lecdoel{ background:var(--amberbg); border-left:3px solid var(--amber); border-radius:8pt; padding:2.5mm 5mm; margin:3mm 0; font-size:9.6pt; } .lecdoel b{ color:var(--amber); }
.txtmeta{ display:flex; gap:2mm; flex-wrap:wrap; margin:2mm 0; } .txtmeta .tm{ font-size:7.6pt; font-weight:600; background:var(--gt); color:var(--gd); border-radius:20pt; padding:.7mm 3mm; } .txtmeta .tm b{ color:var(--gd); }
.ptexts{ display:grid; grid-template-columns:1fr 1fr; gap:5mm; margin:3mm 0; }
.ptext{ border:1px solid var(--line); border-top:4px solid var(--g); border-radius:12pt; padding:4mm 5mm; background:#fff; font-size:9.5pt; }
.ptext .ph{ display:flex; gap:3mm; align-items:center; margin-bottom:2mm; } .ptext .ph .av{ width:12mm;height:12mm;border-radius:50%;overflow:hidden;flex:none } .ptext .ph .av svg{width:100%;height:auto} .ptext .ph .nm{ font-family:var(--disp); font-weight:700; font-size:11pt; color:var(--ink); } .ptext .ph .fr{ font-size:8pt; color:var(--mut); }
.ptext p{ margin:1.5mm 0; } .evi{ background:#FEF3C7; border-radius:3pt; padding:.1mm 1mm; }
/* PAREL-2 · árbol genealógico (Rosalía) */
.arbol{ border:1.5px solid var(--g); border-radius:16pt; padding:4mm 5mm; margin:4mm 0; background:#fff; break-inside:avoid; }
.arbol .cap{ font-family:var(--hand); font-size:14pt; color:var(--gd); margin-bottom:1mm; }
.arbolwrap{ display:grid; grid-template-columns:1.35fr 1fr; gap:6mm; align-items:center; margin:4mm 0; }
.arbolwrap .arbol{ margin:0; }
.ojofam{ border:1.5px solid var(--red); border-radius:12pt; padding:3.5mm 5mm; background:#fff; }
.ojofam .oh{ font-family:var(--disp); font-weight:700; color:var(--red); font-size:10.5pt; }
.ojofam p{ margin:2mm 0 0; font-size:9.3pt; } .ojofam .pair{ display:block; margin:1.5mm 0; }
.ojofam .k{ font-weight:700; color:var(--gd); }
/* horario tabel (routine profiel) */
.horario{ width:100%; font-size:9pt; } .horario td,.horario th{ border:1px solid var(--line); padding:1.6mm 3mm; } .horario th{ background:var(--gt); color:var(--gd); font-size:8pt; text-transform:uppercase; } .horario .hh{ font-family:var(--disp); font-weight:700; color:var(--gd); white-space:nowrap; }
"""

# ---------------- component-helpers ----------------
import sys as _qs; _qs.path.insert(0, "/home/user/espa-ol-en-la-pr-ctica/03-build/web")
from qr_print import qr          # echte QR-code, zie qr_print.py

def audiorow(call_html, qr_html):
    return f'<div class="audiorow"><div class="call">{call_html}</div>{qr_html}</div>'

def act(num, title, badges, body, steun=None):
    b = "".join(f'<span class="badge{" skill" if s.get("skill") else ""}">{s["t"]}</span>' for s in badges)
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

def clock(h, m):
    # analoge klok SVG (24mm), h=uur (0-23), m=minuten
    cx, cy, r = 50, 50, 44
    ma = math.radians(m*6 - 90)
    ha = math.radians((h % 12)*30 + m*0.5 - 90)
    mx, my = cx + 30*math.cos(ma), cy + 30*math.sin(ma)
    hx, hy = cx + 20*math.cos(ha), cy + 20*math.sin(ha)
    ticks = ""
    for i in range(12):
        a = math.radians(i*30 - 90)
        x1, y1 = cx + (r-4)*math.cos(a), cy + (r-4)*math.sin(a)
        x2, y2 = cx + r*math.cos(a), cy + r*math.sin(a)
        ticks += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#CFCEC8" stroke-width="1.6"/>'
    return (f'<div class="cw"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="46" fill="#fff" stroke="#1E9E74" stroke-width="2.2"/>'
            f'{ticks}<line x1="50" y1="50" x2="{hx:.1f}" y2="{hy:.1f}" stroke="#20242E" stroke-width="3.4" stroke-linecap="round"/>'
            f'<line x1="50" y1="50" x2="{mx:.1f}" y2="{my:.1f}" stroke="#EA7317" stroke-width="2.4" stroke-linecap="round"/>'
            f'<circle cx="50" cy="50" r="3" fill="#157355"/></svg></div>')

def clockcard(h, m, es, nl):
    return f'<div class="clockcard">{clock(h,m)}<div class="es">{es}</div><div class="nl">{nl}</div></div>'

def arbol_rosalia():
    # PAREL-2 · el árbol genealógico de Rosalía (flat-vector SVG, print-veilig).
    # Personas: abuelos → padres → Pili + Rosalía → Genís (sobrino de Rosalía).
    G, GD, GT = "#1E9E74", "#157355", "#E4F4EE"
    def box(x, y, name, role, hi=False):
        fill = GD if hi else "#fff"
        stroke = GD if hi else "#CFCEC8"
        tcol = "#fff" if hi else "#20242E"
        rcol = "#DDF3EA" if hi else "#6A6E78"
        return (f'<g><rect x="{x}" y="{y}" width="130" height="44" rx="10" fill="{fill}" '
                f'stroke="{stroke}" stroke-width="{2.4 if hi else 1.6}"/>'
                f'<text x="{x+65}" y="{y+19}" text-anchor="middle" fill="{tcol}" '
                f'font-family="Bricolage Grotesque,sans-serif" font-weight="700" font-size="14">{name}</text>'
                f'<text x="{x+65}" y="{y+34}" text-anchor="middle" fill="{rcol}" '
                f'font-family="Inter,sans-serif" font-size="9.5">{role}</text></g>')
    lines = (f'<g stroke="{G}" stroke-width="2" fill="none">'
             # abuelos pareja
             '<path d="M200 30 H320"/>'
             # bajada a los padres (Pilar es hija de los abuelos)
             '<path d="M260 30 V61 H385 V92"/>'
             # padres pareja
             '<path d="M200 114 H320"/>'
             # bajada + reparto a las dos hijas
             '<path d="M260 114 V149 H135 V176"/>'
             '<path d="M260 149 H385 V176"/>'
             # Pili -> Genís (sobrino)
             '<path d="M135 220 V260"/>'
             '</g>')
    boxes = "".join([
        box(70, 8, "Antonio", "el abuelo"),
        box(320, 8, "Carmen", "la abuela"),
        box(70, 92, "José Manuel", "el padre"),
        box(320, 92, "Pilar", "la madre"),
        box(70, 176, "Pili", "la hermana"),
        box(320, 176, "Rosalía", "la cantante", hi=True),
        box(70, 260, "Genís", "el sobrino de Rosalía"),
    ])
    svg = (f'<svg viewBox="0 0 470 316" style="width:100%;height:auto;display:block">'
           f'<rect width="470" height="316" fill="{GT}" rx="14"/>{lines}{boxes}</svg>')
    return f'<div class="arbol">{svg}</div>'

# ================= BODY =================
BODY = []
def P(*x): BODY.extend(x)

# ---------- OPENER ----------
P(f'''
<div class="hero">
  <div class="tab">U2 · MI GENTE</div>
  <div class="eyebrow">UNIDAD 2 · LA RUTA · PARADA 2 — SEVILLA 🇪🇸</div>
  <h1>Mi gente</h1>
  <div class="sub">Llegamos a <b>Sevilla</b>, la ciudad de <b>Lucía</b>. Hoy ella te presenta a <b>su familia</b>: sus padres, sus hermanos, sus abuelos… <span class="gloss">We komen aan in Sevilla, de stad van Lucía. Vandaag stelt zij haar familie voor.</span></div>
  <div class="q">¿Quién es quién en tu familia? <span style="font-weight:400;opacity:.9">· Wie is wie in jouw familie?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U1 · Madrid</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U2 · Sevilla</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U3 · Barcelona</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U4 · València</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U5–U8 · América</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 2 · Sevilla (Andalucía).</b> Esta es la ciudad de <b>Lucía</b>. Ella abre su <b>álbum de familia</b> y te presenta a su gente. Con su familia aprendes a <b>describir personas</b>, usar <b>tener</b>, los <b>posesivos</b> y la gran trampa: <b>ser</b> o <b>estar</b>. <span class="gloss">Sevilla is de thuisstad van Lucía; met haar familie leer je mensen beschrijven.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> En <b>Sevilla</b>, Lucía te enseña una foto: «Esta es <b>mi familia</b>. Somos cinco.» Aprendes los <b>miembros de la familia</b>, a decir cuántos <b>tienes</b>, a <b>describir</b> a las personas (alto, moreno, simpático) y a distinguir <b>ser</b> (identidad) de <b>estar</b> (estado/lugar).
      <span class="gloss">In Sevilla toont Lucía haar familiefoto. Je leert de familieleden, tellen met tener, beschrijven en ser/estar onderscheiden.</span></div>
      <div class="ojo"><b>¡Ojo! — valstrik:</b> in het NL is <b>zijn</b> één woord, in het Spaans <b>twee</b>: <b>ser</b> (wie/hoe iemand ís: es alta, es simpática) en <b>estar</b> (hoe/waar iemand nú is: está cansada, está en casa). En <b>mi</b> hermana → <b>mis</b> hermanas (het bezit past bij het <span class="trap">aantal</span>).</div>
    </div>
    <div>
      <div class="se">La gente de la ruta</div>
      <div class="cast">
        <div class="pc"><div class="avw">{AV["lucia"]}</div><div class="nm">Lucía</div><div class="fr">Sevilla 🇪🇸 · anfitriona</div></div>
        <div class="pc"><div class="avw">{AV["diego"]}</div><div class="nm">Diego</div><div class="fr">CDMX 🇲🇽</div></div>
        <div class="pc"><div class="avw">{AV["valen"]}</div><div class="nm">Valen</div><div class="fr">Cartagena 🇨🇴</div></div>
        <div class="pc"><div class="avw">{AV["nina"]}</div><div class="nm">Nina</div><div class="fr">Cusco 🇵🇪</div></div>
        <div class="pc tu"><div class="avw">{TU}</div><div class="nm">Tú</div><div class="fr">Flandes 🇧🇪</div></div>
      </div>
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila de la familia</span><br><span class="gloss" style="font-size:8.5pt">In Sevilla vul je je rugzak met familiewoorden, beschrijvingen en ser/estar.</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">presentar a tu familia</span> (miembros + tener) <span class="nl">je familie voorstellen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar los posesivos</span> (mi/tu/su/nuestro · mis/tus/sus) <span class="nl">bezittelijke voornaamwoorden</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">describir a las personas</span> físico + carácter <span class="nl">iemand beschrijven (uiterlijk + karakter)</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">distinguir ser y estar</span> <span class="nl">de valstrik «zijn»: ser vs. estar</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">señalar con este/ese</span> en el álbum <span class="nl">dit/dat aanwijzen bij foto’s</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">crear tu <b>«Álbum de familia»</b></span> <span class="nl">familiealbum + stamboom + raadspel (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>La familia</span><span><b>§2</b>Posesivos</span><span><b>§3</b>Adjetivos</span><span><b>§4</b>Ser/estar</span><span><b>§5</b>Este/ese</span><span><b>§6</b>Lectura</span><span><b>Taller</b>Conectores</span><span><b>Cultura</b>Familia</span><span><b>Tarea</b>Álbum</span>
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
P('<div class="intro"><b>ES:</b> Antes de empezar recordamos lo que necesitas hoy: el <b>presente regular</b>, los verbos <b>ser</b> y <b>tener</b>, los <b>números</b> y cómo <b>presentarte</b> (U0–U1). <span class="gloss">Voor we starten: presente regular, ser/tener, getallen en jezelf voorstellen ophalen.</span></div>')
P(lpd(("7","woordenschat inzetten"), ("9","strategieën / lengua de clase"), ("8","taalsysteem ophalen")))
P('</div>')
P('<p style="font-size:9.6pt">① <b>¿Qué tienes ya en la mochila?</b> Drie clusters die je vandaag opnieuw inzet. <span class="gloss">Wat zit er al in je rugzak?</span></p>')
P(clusters([
  ("🔤","Presente regular",["-ar: hablo, hablas…","-er: como, comes…","-ir: vivo, vives…"],"Werkwoorden vervoegen (U1)."),
  ("👤","Ser · tener",["yo soy · tú eres","yo tengo · tú tienes","edad = tener años"],"Wie je bent + leeftijd (U1)."),
  ("🔢","Números 0–100",["cero · cinco · diez","quince · veinte · treinta","cuarenta · cien"],"Voor leeftijd & aantal (U0)."),
]))
P(actx(1, "Repasa el presente regular",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Vervoeg in het presente regular (uit U1).</p>'
  '<table class="mp"><thead><tr><th>Infinitivo</th><th>yo</th><th>tú</th><th>nosotros</th></tr></thead><tbody>'
  '<tr><td>hablar</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>vivir</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>llamarse</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>', apoyo="Banco de palabras: tabel open"))
P(actx(2, "¿ser o tener?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Vul <b>ser</b> of <b>tener</b> in.</p>'
  '<p style="margin-left:12.5mm">a) Yo <span class="wl sm"></span> de Bélgica. &nbsp; b) Lucía <span class="wl sm"></span> 16 años. &nbsp; c) Nosotros <span class="wl sm"></span> estudiantes. &nbsp; d) ¿Tú <span class="wl sm"></span> hermanos?</p>', apoyo="Pista: edad = tener"))
P(actx(3, "Los números para contar",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Schrijf het getal voluit in letters.</p>'
  '<table class="mp"><thead><tr><th>Cifra</th><th>En letras</th><th>Cifra</th><th>En letras</th></tr></thead>'
  '<tbody><tr><td>2</td><td><span class="wl md"></span></td><td>5</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>13</td><td><span class="wl md"></span></td><td>40</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="Modelo"))
P(actx(4, "La lengua de clase",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind de klaszin met zijn functie (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th></th><th>Función</th></tr></thead><tbody>'
  '<tr><td>1 · ¿Cómo se dice…?</td><td><span class="wl sm"></span></td><td>A · ik begrijp het niet</td></tr>'
  '<tr><td>2 · No entiendo.</td><td><span class="wl sm"></span></td><td>B · hoe zeg je…?</td></tr>'
  '<tr><td>3 · ¿Puede repetir?</td><td><span class="wl sm"></span></td><td>C · kunt u herhalen?</td></tr></tbody></table>', apoyo="Banco de palabras"))
P(actx(5, "Calentamiento: preséntate",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Zeg aan je buur drie dingen over jezelf met het presente + ser/tener (Me llamo… · Soy de… · Tengo … años). Je buur onthoudt ze.</p>'
  '<p style="margin-left:12.5mm">Mis tres cosas: <span class="wl full"></span></p>', apoyo="Modelo"))
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> presente regular, ser/tener en números met zelfcorrectie op de digitale pagina.</div>')
P('</div>')  # close §0

# ================= §1 · LA FAMILIA + TENER =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">1</span><span class="pk">§1 · La familia — los miembros + tener</span>')
P('<div class="route-note">📍 Parada 2 · Sevilla — Lucía abre su álbum: «Mira, esta es mi gente.»</div>')
P('<div class="intro"><b>ES:</b> Primero conoces a los <b>miembros de la familia</b>, después dices cuántos <b>tienes</b>. La ruta: contexto → observar → patrón → regla → practicar → comunicar. <span class="gloss">Eerst de familieleden, dan tellen met tener.</span></div>')
P(lpd(("7","woordenschat: la familia"), ("8","taalsysteem: tener"), ("3","je familie voorstellen"), ("4","interactie")))
P('</div>')
# §1.1 vocab familia
P('<h3 style="margin-top:6mm">§1.1 · Los miembros de la familia — el vocabulario</h3>')
# --- PAREL-2 · el árbol genealógico de Rosalía ---
P('<p style="font-size:9.6pt">① <b>El árbol de Rosalía.</b> Antes de tu familia, conocemos a la familia de una cantante famosa: <b>Rosalía</b>. Explora su árbol y aprende el vocabulario de la familia. <span class="gloss">We leren het familievocabulaire via de stamboom van Rosalía.</span></p>')
P('<div class="arbolwrap">')
# Geen productienotitie maar een eerlijke bronvermelding: de stamboom gaat over een
# echt persoon, dus moet erbij staan wat wél en niet vaststaat. Daarom in de
# leerlingstijl (Spaans + NL-steun) en niet in het grijze asset-kader.
P('<div>' + arbol_rosalia() + '<div class="hist" style="margin-top:1mm;font-size:8.6pt">'
  '<b>Nota:</b> los nombres de los <b>abuelos</b> son inventados: de la familia de Rosalía '
  'se sabe poco públicamente. El resto del árbol sí es real. '
  '<span class="gloss">De namen van de grootouders zijn verzonnen — over Rosalía\'s familie is '
  'weinig publiek bekend. De rest van de stamboom klopt wel. Zo weet je meteen wat je hier '
  'als feit mag onthouden.</span></div></div>')
P('<div class="ojofam"><div class="oh">💡 ¡Ojo! — «neef/nicht» = dos palabras</div>'
  '<p>En neerlandés <b>«neef/nicht»</b> son <b>dos cosas</b> en español:'
  '<span class="pair"><span class="k">el primo / la prima</span> = kind van je <b>oom of tante</b> <span class="gloss">(tío/tía)</span></span>'
  '<span class="pair"><span class="k">el sobrino / la sobrina</span> = kind van je <b>broer of zus</b> <span class="gloss">(hermano/hermana)</span></span>'
  '<b>Genís</b> es el <b>sobrino</b> de Rosalía (el hijo de su hermana Pili) — <b>no</b> su <span class="trap">primo</span>.</p></div>')
P('</div>')
P(actx(1, "¿Quién es quién en el árbol de Rosalía?",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Kijk naar de stamboom en vul het juiste familiewoord in.</p>'
  '<p style="margin-left:12.5mm">a) Pilar es la <span class="wl md"></span> de Rosalía.<br>'
  'b) Antonio y Carmen son los <span class="wl md"></span> de Rosalía.<br>'
  'c) Pili es la <span class="wl md"></span> de Rosalía.<br>'
  'd) Genís es el <span class="wl md"></span> de Rosalía (no el primo).</p>', apoyo="Banco de palabras: madre · abuelos · hermana · sobrino"))
P('<p style="font-size:9.6pt">② <b>Los miembros — la ficha.</b> Observa y adivina el significado. <span class="gloss">De familieleden — raad de betekenis.</span></p>')
P('<div class="fichacard">'
  '<div><div class="row"><span class="k">los padres</span><span class="v">Antonio + Rosa <span class="nl">de ouders</span></span></div>'
  '<div class="row"><span class="k">el padre / la madre</span><span class="v">papá / mamá <span class="nl">vader / moeder</span></span></div>'
  '<div class="row"><span class="k">el hermano / la hermana</span><span class="v">Marco / Ana <span class="nl">broer / zus</span></span></div>'
  '<div class="row"><span class="k">los abuelos</span><span class="v">Pepe + Carmen <span class="nl">grootouders</span></span></div></div>'
  '<div><div class="row"><span class="k">el tío / la tía</span><span class="v">hermano/a de papá o mamá <span class="nl">oom / tante</span></span></div>'
  '<div class="row"><span class="k">el primo / la prima</span><span class="v">Julia <span class="nl">neef / nicht</span></span></div>'
  '<div class="row"><span class="k">el hijo / la hija</span><span class="v">de zoon / dochter</span></div>'
  '<div class="row"><span class="k">la mascota</span><span class="v">el perro, el gato <span class="nl">huisdier</span></span></div></div></div>')
P('<p style="font-size:9.6pt">③ <b>Organiza en clusters</b> — de familie als netwerk, niet als lijst:</p>')
P(clusters([
  ("👴","Los mayores",["los abuelos: abuelo · abuela","los padres: padre · madre","los tíos: tío · tía"],"De oudere generaties."),
  ("🧒","Mi generación",["hermano · hermana","primo · prima","yo"],"Broers, zussen, neven, nichten."),
  ("💞","Otros",["marido · mujer","hijo · hija · nieto/a","mayor ↔ menor"],"Relaties & leeftijd."),
]))
P('<p style="font-size:9.6pt">④ <b>Parejas: masculino ↔ femenino.</b> Veel familiewoorden komen in paren (-o/-a):</p>')
P(vpairs([("el hermano","la hermana"),("el abuelo","la abuela"),("el tío","la tía"),("el primo","la prima"),("el hijo","la hija"),("el nieto","la nieta")]))
P(actx(2, "Empareja miembro ↔ definición",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Verbind het familielid met de omschrijving (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Miembro</th><th>Letra</th><th></th><th>Definición</th></tr></thead><tbody>'
  '<tr><td>1 · el abuelo</td><td><span class="wl sm"></span></td><td>A</td><td>de broer van mijn moeder</td></tr>'
  '<tr><td>2 · la prima</td><td><span class="wl sm"></span></td><td>B</td><td>de vader van mijn vader</td></tr>'
  '<tr><td>3 · el tío</td><td><span class="wl sm"></span></td><td>C</td><td>de dochter van mijn tante</td></tr>'
  '<tr><td>4 · la hermana</td><td><span class="wl sm"></span></td><td>D</td><td>de andere dochter van mijn ouders</td></tr></tbody></table>', apoyo="Banco de palabras"))
P(actx(3, "Masculino o femenino — clasifica",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Zet elk woord in de juiste kolom. <span class="words"><b>el primo · la abuela · el hijo · la tía · el hermano · la madre</b></span></p>'
  + sortcols([("Masculino (el)",""),("Femenino (la)","")]), apoyo="Banco de palabras"))
P(actx(4, "El árbol genealógico — completa",
  [{"t":"🔍 Analizar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Kijk naar Lucía: haar ouders zijn Antonio en Rosa; haar opa en oma zijn Pepe en Carmen. Vul in wat Pepe en Carmen zijn voor Lucía, en wat Lucía is voor hen.</p>'
  '<p style="margin-left:12.5mm">Pepe y Carmen son los <span class="wl md"></span> de Lucía.<br>Lucía es la <span class="wl md"></span> de Pepe y Carmen.<br>Antonio es el <span class="wl md"></span> de Lucía.</p>', apoyo="Banco de palabras: abuelos · nieta · padre"))
P(mispal("Mi familia — je eigen woorden", 3))
P('</div>')  # page §1.1
# §1.2 tener
P('<div class="page">')
P('<div class="divider">El verbo tener · §1.2</div>')
P('<h3>§1.2 · «Tengo dos hermanos» — el verbo tener</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto (chat).</b> Observa el verbo <b>tener</b>:</p>')
P('<div class="chat">'
  '<div class="chatline you"><div class="bub">¿<b>Tienes</b> hermanos?</div><div class="who">Lucía</div></div>'
  '<div class="chatline me"><div class="bub">Sí, <span class="fx per">yo</span> <span class="fx vb">tengo</span> <span class="fx ob">dos hermanos</span>. ¿Y tú?</div><div class="who">Tú</div></div>'
  '<div class="chatline you"><div class="bub"><span class="fx per">Yo</span> <span class="fx vb">tengo</span> un hermano y una hermana. Y mi familia <span class="fx vb">tiene</span> un perro.</div><div class="who">Lucía</div></div></div>')
P('<p style="font-size:9.6pt">② <b>El patrón — tener es irregular (e→ie + yo especial).</b></p>')
P(machine([("infinitivo","tener"),("yo","tengo"),("tú/él","t<span class=end>ie</span>nes / t<span class=end>ie</span>ne")]))
P('<table class="conj"><thead><tr><th>Persona</th><th>tener</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">tengo</td><td>Tengo dos hermanos.</td></tr>'
  '<tr><td class="p">tú</td><td class="v">tienes</td><td>¿Tienes primos?</td></tr>'
  '<tr><td class="p">él / ella / usted</td><td class="v">tiene</td><td>Lucía tiene un perro.</td></tr>'
  '<tr><td class="p">nosotros/-as</td><td class="v">tenemos</td><td>Tenemos una familia grande.</td></tr>'
  '<tr><td class="p">vosotros/-as</td><td class="v">tenéis</td><td>¿Tenéis mascota?</td></tr>'
  '<tr><td class="p">ellos/-as / ustedes</td><td class="v">tienen</td><td>Mis tíos tienen tres hijos.</td></tr></tbody></table>')
P('<p style="font-size:9.6pt">③ <b>Como bloques.</b> Kies één blok per rij en bouw je zin:</p>')
P(blocks([
  [("per","Yo"),("vb","tengo"),("ob","dos hermanos")],
  [("per","Lucía"),("vb","tiene"),("ob","un perro")],
  [("per","Nosotros"),("vb","tenemos"),("ob","una familia grande")],
]))
P(regla("Regla · tener",
  '<p><b>tener</b> = hebben. Onregelmatig: <b>yo tengo</b> (met -g-) en <b>e→ie</b> in tú/él/ellos (t<b>ie</b>nes, t<b>ie</b>ne, t<b>ie</b>nen). Nosotros/vosotros gewoon: ten<b>e</b>mos, ten<b>é</b>is. '
  '<br>🟡 <b>Ojo:</b> leeftijd = <b>tener … años</b> (niet <span class="trap">ser</span>): <i>Tengo 16 años.</i></p>'))
P(actx(5, "Elige la forma de tener",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Kruis de juiste vorm aan.</p>'
  '<p style="margin-left:12.5mm">a) Yo ☐ tengo ☐ tienes dos primas. &nbsp; b) ¿Tú ☐ tiene ☐ tienes hermanos?<br>c) Mis abuelos ☐ tienen ☐ tenemos un gato. &nbsp; d) Nosotros ☐ tienen ☐ tenemos una casa grande.</p>', apoyo="Modelo"))
P(actx(6, "Conjuga tener (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Vul de juiste vorm van <b>tener</b> in.</p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl md"></span> dos hermanos.<br>'
  '2. ¿Cuántos primos <span class="wl md"></span> tú?<br>'
  '3. Lucía <span class="wl md"></span> el pelo largo.<br>'
  '4. Nosotros <span class="wl md"></span> una familia grande.<br>'
  '5. Mis tíos <span class="wl md"></span> tres hijos.</p>'
  '<p style="margin-left:12.5mm" class="gloss">✅ De oplossingen staan online (zelfcorrectie op de digitale pagina).</p>', apoyo="Pista: kijk naar de persoon"))
P(actx(7, "¿Cuántos tienes? — pregunta y responde",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vraag je buur naar zijn/haar familie en noteer de aantallen.</p>'
  '<table class="wtab mp"><thead><tr><th>¿Cuántos/as… tienes?</th><th>Mi compañero/a</th></tr></thead><tbody>'
  '<tr><td>…hermanos</td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>…primos</td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>…mascotas</td><td><span class="wl sm"></span></td></tr></tbody></table>', apoyo="Marco: ¿Cuántos… tienes? — Tengo…"))
P('</div>')  # page §1.2
# §1.3 tarea comunicativa
P('<div class="page">')
P('<h3>§1.3 · Comunicar — presenta a tu familia</h3>')
P('<p style="font-size:9.6pt">Nu je de leden kent en met <b>tener</b> kan tellen, stel je je gezin voor.</p>')
P(actx(8, "Mi familia en números",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf drie zinnen over jouw familie met <b>tener</b> + een aantal.</p>'
  '<p style="margin-left:12.5mm">1) En mi familia somos <span class="wl md"></span>.<br>2) Tengo <span class="wl lg"></span>.<br>3) Mi familia tiene <span class="wl lg"></span>.</p>', apoyo="Marco"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha a Lucía presentar a su familia.</b> <span class="gloss">Luister; noteer hoeveel broers/zussen en huisdieren ze heeft.</span></div>',
           qr("Escanea y escucha", "Audio 1 · Mi familia · 0:45", seed=221)))
P(actx(9, "Escucha y anota",
  [{"t":"👂 Escuchar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Luister en noteer bij elk woord het aantal dat je hoort.</p>'
  '<p style="margin-left:12.5mm">hermanos: <span class="wl sm"></span> · primos: <span class="wl sm"></span> · mascota: <span class="wl md"></span> · abuelos: <span class="wl sm"></span></p>', apoyo="Pista: números"))
P(tarea_com("Tarea comunicativa · Preséntame a tu gente",
  [{"t":"🎙️ Hablar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b>Situación:</b> jij en je buur wisselen jullie families uit, net zoals Lucía haar album toont. Vertel wie er in je gezin zit en hoeveel je er van elk hebt. Je buur tekent jouw <b>árbol genealógico</b>. <span class="gloss">«En mi familia somos cuatro. Tengo una hermana y un perro…»</span></p>'
  '<div class="wbox sm"></div>'
  '<div class="steun" style="margin-left:0mm">Modelo: Lucía</div>'))
P(actx(10, "Dictado preparado — la familia de Lucía",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Luister en schrijf de vier zinnen op.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>'
  '2. <span class="wl full"></span>'
  '3. <span class="wl full"></span>'
  '4. <span class="wl full"></span></p>'
  '<p style="margin-left:12.5mm" class="gloss">✅ Vergelijk daarna met de tekst online (zelfcorrectie).</p>', apoyo="Banco de palabras: familiewoorden"))
P(audiorow('<div class="ic">🎧</div><div><b>Repite en voz alta.</b> <span class="gloss">Luister opnieuw en herhaal elke zin — let op de klemtoon van de namen.</span></div>',
           qr("Escanea y repite", "Audio 1b · Dictado · 0:40", seed=222)))
P('<div class="route-note">🎮 <b>Juega online:</b> «memoria de la familia», «parentesco» en «tener (cloze)» — met zelfcorrectie en meerdere reeksen op de digitale pagina.</div>')
P('</div>')  # page §1.3

# ================= §2 · LOS POSESIVOS =================
retos("familia", "§1.4 · Retos — tu gente de verdad",
      'Tres retos sobre las personas que cuentan: un <b>árbol imposible</b>, los <b>números</b> del mundo hispano y un texto con <b>palabras prohibidas</b>.',
      'Drie retos over de mensen die tellen: een onmogelijke stamboom, de cijfers van de Spaanstalige wereld, en een tekst met verboden woorden.')
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2 · Los posesivos — mi, tu, su, nuestro</span>')
P('<div class="intro"><b>ES:</b> Para decir <b>de quién</b> es la familia usas los posesivos: <b>mi</b> madre, <b>tu</b> primo, <b>su</b> perro. Y en plural: <b>mis</b> hermanos, <b>tus</b> tíos. La ruta: observar → patrón → regla → practicar → comunicar. <span class="gloss">Bezittelijke voornaamwoorden: mijn/jouw/zijn·haar + de meervoudsvorm.</span></div>')
P(lpd(("8","taalsysteem: posesivos"), ("7","woordenschat: familia"), ("3","over je familie schrijven")))
P('</div>')
# §2.1 observar
P('<h3 style="margin-top:6mm">§2.1 · Observa: mi · tu · su · nuestro</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto.</b> Lees hoe Lucía over haar mensen praat:</p>')
P(obsbox([
  '<span class="hl">Mi</span> madre se llama Rosa. — <span class="hl">Mis</span> hermanos son Marco y Ana.',
  '¿Cómo se llama <span class="hl">tu</span> padre? — ¿Y <span class="hl">tus</span> primos?',
  '<span class="hl">Su</span> perro es pequeño. — <span class="hl">Nuestra</span> abuela vive en Sevilla.',
], vragen='<b>1)</b> Wanneer verandert <i>mi</i> in <i>mis</i>? <b>2)</b> Waar hangt dat van af: van de bezitter of van het aantal bezittingen?'))
P('<p style="font-size:9.6pt">② <b>El patrón — el posesivo concuerda con la cosa poseída (en número).</b></p>')
P('<table class="conj"><thead><tr><th>de quién</th><th>1 cosa</th><th>varias cosas</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">mi hermano</td><td class="v">mis hermanos</td></tr>'
  '<tr><td class="p">tú</td><td class="v">tu prima</td><td class="v">tus primas</td></tr>'
  '<tr><td class="p">él/ella/usted</td><td class="v">su tío</td><td class="v">sus tíos</td></tr>'
  '<tr><td class="p">nosotros</td><td class="v">nuestro/a abuelo/a</td><td class="v">nuestros/as abuelos/as</td></tr></tbody></table>')
P(actx(1, "¿singular o plural? — clasifica",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Zet elk voorbeeld bij de juiste vorm. <span class="words"><b>mi tía · mis primos · tu abuelo · tus hermanas · su hijo · sus nietos</b></span></p>'
  + sortcols([("Singular (mi/tu/su)","1 persona"),("Plural (mis/tus/sus)","varias personas")], eigen=False), apoyo="Modelo"))
P(actx(2, "Empareja posesivo ↔ persona",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind het posesivo met de bezitter (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Posesivo</th><th>Letra</th><th></th><th>De quién</th></tr></thead><tbody>'
  '<tr><td>1 · mi / mis</td><td><span class="wl sm"></span></td><td>A</td><td>van jou (tú)</td></tr>'
  '<tr><td>2 · tu / tus</td><td><span class="wl sm"></span></td><td>B</td><td>van hem/haar (él/ella)</td></tr>'
  '<tr><td>3 · su / sus</td><td><span class="wl sm"></span></td><td>C</td><td>van mij (yo)</td></tr></tbody></table>', apoyo="Modelo"))
P('</div>')  # page §2.1
# §2.2 mecanismo
P('<div class="page">')
P('<div class="divider">Concordancia en número · §2.2</div>')
P('<h3>§2.2 · mi → mis: el posesivo sigue a la cosa</h3>')
P('<p style="font-size:9.6pt">① <b>Overeenkomst zichtbaar.</b> Het posesivo verandert mee met het <b>aantal</b> (niet met de bezitter):</p>')
P('<div class="agree"><div class="w"><u>mi</u> herman<u>a</u> &nbsp;→&nbsp; <u>mis</u> herman<u>as</u></div><div class="tie">1 zus → meerdere zussen · <b>mi → mis</b></div></div>')
P('<p style="font-size:9.6pt">② <b>Como bloques.</b> Kies het juiste posesivo bij enkelvoud of meervoud:</p>')
P(blocks([
  [("per","yo →"),("opt","mi hermano"),("opt","mis hermanos")],
  [("per","tú →"),("opt","tu primo"),("opt","tus primos")],
  [("per","él/ella →"),("opt","su tío"),("opt","sus tíos")],
]))
P(regla("Regla · los posesivos",
  '<p><b>mi · tu · su</b> (1 ding) → <b>mis · tus · sus</b> (meerdere dingen). Het posesivo past bij de <b>bezitting</b>, niet bij de bezitter. <b>nuestro/nuestra/nuestros/nuestras</b> past ook in geslacht. '
  '<br>🔴 <b>Valstrik NL:</b> in het Spaans staat er <b>geen</b> apart woordje «van»: <i>mi madre</i> = «mijn moeder», <i>el perro de mi tía</i> = «de hond van mijn tante».</p>'))
P(actx(3, "Completa con el posesivo (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Vul <b>mi/mis · tu/tus · su/sus</b> in.</p>'
  '<p style="margin-left:12.5mm">1. (yo) <span class="wl sm"></span> madre es de Sevilla.<br>'
  '2. (yo) <span class="wl sm"></span> hermanos son mayores.<br>'
  '3. (tú) ¿Cómo se llama <span class="wl sm"></span> padre?<br>'
  '4. (tú) ¿Y <span class="wl sm"></span> primas?<br>'
  '5. (él) <span class="wl sm"></span> abuelos viven en Madrid.</p>'
  '<p style="margin-left:12.5mm" class="gloss">✅ Zelfcorrectie online.</p>', apoyo="Pista: kijk of het meervoud is"))
P(actx(4, "Transforma a plural",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Zet posesivo én zelfstandig naamwoord in het meervoud.</p>'
  '<p style="margin-left:12.5mm">mi hermana → <span class="wl lg"></span><br>tu primo → <span class="wl lg"></span><br>su tío → <span class="wl lg"></span></p>', apoyo="Modelo: mi hermana → mis hermanas"))
P(tarea_com("Tarea comunicativa · El árbol de mi compañero/a",
  [{"t":"🎙️ Hablar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👥 En parejas"},{"t":"± 7 min"},{"t":"★★★"}],
  '<p><b>Situatie:</b> jij beschrijft je familie met posesivos; je buur tekent de stamboom en labelt elk vak. Wissel dan om. <span class="gloss">«Mi padre se llama… Mis abuelos viven en…»</span></p>'
  '<div class="wbox sm"></div>'
  '<div class="steun" style="margin-left:0mm">Marco: mi/mis…</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «posesivo (cloze)» en «singular o plural».</div>')
P('</div>')  # page §2.2

# ================= §3 · LOS ADJETIVOS =================
retos("posesivos", "§2.4 · Retos — ¿de quién es?",
      'Dos retos donde el posesivo decide: una <b>telenovela</b> que la clase escribe junta y una <b>herencia</b> que hay que repartir.',
      'Twee retos waarin het bezittelijk voornaamwoord beslist: een telenovela die de klas samen schrijft, en een erfenis die verdeeld moet worden.')
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3 · Los adjetivos — describir a las personas</span>')
P('<div class="intro"><b>ES:</b> Para <b>describir</b> a tu gente usas adjetivos: físicos (alto, moreno) y de carácter (simpático, tímido). Aprendes la <b>concordancia</b> (género/número) y la <b>posición</b> (después del sustantivo). <span class="gloss">Beschrijven met bijvoeglijke naamwoorden — met overeenkomst en plaats.</span></div>')
P(lpd(("7","woordenschat: descripción física + carácter"), ("8","taalsysteem: concordancia + posición"), ("3","personen beschrijven")))
P('</div>')
# §3.1 física
P('<h3 style="margin-top:6mm">§3.1 · El físico — ¿cómo es?</h3>')
P('<p style="font-size:9.6pt">① <b>Observa a la familia de Lucía.</b> Elk gezicht heeft zijn beschrijving. <span class="gloss">Raad de betekenis uit de context.</span></p>')
P(clusters([
  ("📏","El cuerpo",["alto ↔ bajo","delgado ↔ gordito","joven ↔ mayor"],"Grootte & bouw."),
  ("💇","El pelo",["moreno · rubio · pelirrojo","largo ↔ corto","liso ↔ rizado"],"Kleur & vorm van het haar."),
  ("👀","La cara",["los ojos: azules · verdes · marrones","la barba · las gafas","guapo · joven"],"Ogen & details."),
]))
P('<p style="font-size:9.6pt">② <b>Parejas de contrarios.</b> Leer ze samen als tegenstellingen:</p>')
P(vpairs([("alto","bajo"),("delgado","gordito"),("largo","corto"),("liso","rizado"),("joven","mayor"),("moreno","rubio")]))
P(actx(1, "Empareja adjetivo ↔ definición",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind het adjectief met de vertaling (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Adjetivo</th><th>Letra</th><th></th><th>NL</th></tr></thead><tbody>'
  '<tr><td>1 · moreno</td><td><span class="wl sm"></span></td><td>A</td><td>krullend</td></tr>'
  '<tr><td>2 · rizado</td><td><span class="wl sm"></span></td><td>B</td><td>klein (persoon)</td></tr>'
  '<tr><td>3 · bajo</td><td><span class="wl sm"></span></td><td>C</td><td>donker(harig)</td></tr>'
  '<tr><td>4 · pelirrojo</td><td><span class="wl sm"></span></td><td>D</td><td>roodharig</td></tr></tbody></table>', apoyo="Banco de palabras"))
P(actx(2, "Describe el pelo y los ojos",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul de vier gaten aan met een woord uit het banco. <span class="words"><b>largo · corto · rizado · azules · verdes · marrones</b></span></p>'
  '<p style="margin-left:12.5mm">Lucía tiene el pelo <span class="wl md"></span> y los ojos <span class="wl md"></span>.<br>Mi mejor amigo/a tiene el pelo <span class="wl md"></span> y los ojos <span class="wl md"></span>.</p>', apoyo="Banco de palabras"))
P('</div>')  # page §3.1
# §3.2 congruencia
P('<div class="page">')
P('<div class="divider">La concordancia · género y número · §3.2</div>')
P('<h3>§3.2 · El adjetivo concuerda (-o / -a / -os / -as)</h3>')
P('<p style="font-size:9.6pt">① <b>Overeenkomst zichtbaar (röntgen).</b> Het adjectief past bij het zelfstandig naamwoord in <b>geslacht</b> en <b>aantal</b>:</p>')
P(xray("Mis herman<b>as</b> son alt<b>as</b>.", [("Mis hermanas","vrouwelijk · meervoud"),("altas","-a → -as (concuerda)")]))
P('<div class="agree"><div class="w">alt<u>o</u> · alt<u>a</u> · alt<u>os</u> · alt<u>as</u></div><div class="tie">un chico alt<b>o</b> · una chica alt<b>a</b> · dos chicos alt<b>os</b> · dos chicas alt<b>as</b></div></div>')
P('<p style="font-size:9.6pt">② <b>La máquina de la concordancia.</b> Van basisvorm naar de juiste uitgang:</p>')
P(machine([("adjetivo","simpático"),("¿femenino?",'simpátic<span class="end">a</span>'),("¿plural?",'simpátic<span class="end">as</span>')]))
P('<p style="font-size:9.6pt">③ <b>Cuidado:</b> adjectieven op <b>-e</b> of medeklinker veranderen niet van geslacht:</p>')
P(fmu('alto → alt<b>a</b>/os/as · <br>inteligent<b>e</b> (m/v gelijk) · <br>joven / mayor (m/v gelijk)',
      'Bijvoeglijk naamwoord past bij het zn.',
      'Op -o: 4 vormen. Op -e of medeklinker: enkel meervoud (-s/-es).'))
P(regla("Regla · concordancia + posición",
  '<p><b>Concordancia:</b> adjectief op <b>-o</b> → -o/-a/-os/-as (guapo/guapa/guapos/guapas). Op <b>-e</b> of medeklinker → enkel getal (inteligente/inteligentes; joven/jóvenes). '
  '<br><b>Posición:</b> het adjectief staat <b>na</b> het zn.: <i>una chica <b>simpática</b></i> (niet <span class="trap">una simpática chica</span>).</p>'))
P(actx(3, "¿Concuerda? — corrige",
  [{"t":"🔍 Analizar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Verbeter de uitgang zodat het adjectief overeenkomt.</p>'
  '<p style="margin-left:12.5mm">a) Mi madre es alt<b>o</b>. → <span class="wl md"></span><br>b) Mis primos son simpátic<b>a</b>. → <span class="wl md"></span><br>c) Una chica guap<b>os</b>. → <span class="wl md"></span></p>', apoyo="Pista: kijk naar geslacht + getal"))
P(actx(4, "Concuerda el adjetivo (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Zet het adjectief tussen haakjes in de juiste vorm.</p>'
  '<p style="margin-left:12.5mm">1. Mi hermana es <span class="wl md"></span> <i>(moreno)</i>.<br>'
  '2. Mis abuelos son muy <span class="wl md"></span> <i>(simpático)</i>.<br>'
  '3. Las primas de Lucía son <span class="wl md"></span> <i>(alto)</i>.<br>'
  '4. Mi profesor es <span class="wl md"></span> <i>(inteligente)</i>.</p>'
  '<p style="margin-left:12.5mm" class="gloss">✅ Zelfcorrectie online.</p>', apoyo="Marco"))
P(actx(5, "Clasifica: -o / -e·consonante",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Welke adjectieven hebben 4 vormen (-o) en welke maar 2? <span class="words"><b>guapo · inteligente · alto · joven · rubio · mayor</b></span></p>'
  + sortcols([("4 vormen (-o/-a/-os/-as)",""),("2 vormen (-e / consonante)","")], eigen=False), apoyo="Modelo"))
P('</div>')  # page §3.2
# §3.3 carácter + posición
P('<div class="page">')
P('<div class="divider">El carácter · §3.3</div>')
P('<h3>§3.3 · El carácter — ¿cómo es de personalidad?</h3>')
P('<p style="font-size:9.6pt">① <b>El carácter, como una escala.</b> Van heel verlegen tot heel praatgraag:</p>')
P(scale(["muy tímido","tímido","normal","hablador","muy hablador"]))
P(clusters([
  ("😊","Positivo",["simpático · majo","gracioso · alegre","inteligente · trabajador"],"Fijne eigenschappen."),
  ("😐","Neutro",["tímido · tranquilo","hablador","joven · mayor"],"Neutrale trekjes."),
  ("😠","Negativo",["antipático","serio","perezoso (lui)"],"Minder fijn."),
]))
P(actx(6, "Empareja carácter ↔ situación",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Welk adjectief past? Schrijf het.</p>'
  '<p style="margin-left:12.5mm">a) Habla mucho con todos. → es muy <span class="wl md"></span><br>b) No dice casi nada, es reservado. → es <span class="wl md"></span><br>c) Siempre está contento y ríe. → es <span class="wl md"></span></p>', apoyo="Banco de palabras: hablador · tímido · alegre"))
P(actx(7, "Describe a un familiar",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Beschrijf iemand uit je familie: minstens twee fysieke en twee karaktereigenschappen.</p>'
  '<div class="wbox"></div>', apoyo=""))
P(tarea_com("Tarea comunicativa · ¿A quién describo?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 7 min"},{"t":"★★★"}],
  '<p><b>Situatie (juego «¿Quién es?»):</b> beschrijf een familielid van je buur zonder de naam te zeggen; je buur raadt wie. Wissel om. <span class="gloss">«Es alta, morena y muy simpática. ¿Quién es?»</span></p>'
  '<p style="margin-left:12.5mm">Mi descripción: <span class="wl full"></span> ¿Quién es? <span class="wl md"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Marco: Es… tiene…</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «físico vs. carácter», «concuerda el adjetivo» en «colores».</div>')
P('</div>')  # page §3.3

# ================= §4 · SER / ESTAR =================
retos("adjetivos", "§3.4 · Retos — describir sin lo fácil",
      'Dos retos que te sacan de los tres adjetivos de siempre.',
      'Twee retos die je weghalen bij de drie bijvoeglijke naamwoorden van altijd.')
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4 · Ser o estar — la gran trampa del «zijn»</span>')
P('<div class="intro"><b>ES:</b> En neerlandés «zijn» es <b>una</b> palabra, pero en español hay <b>dos</b>: <b>ser</b> (identidad, descripción) y <b>estar</b> (estado, lugar). Aquí lo descubres con una <b>máquina de decisión</b>. <span class="gloss">De grote valstrik: ser vs. estar — allebei «zijn».</span></div>')
P(lpd(("8","taalsysteem: ser/estar"), ("3","beschrijven & lokaliseren"), ("9","strategie: beslisboom")))
P('</div>')
# §4.1 observar contrast
P('<h3 style="margin-top:6mm">§4.1 · Observa el contraste</h3>')
P('<p style="font-size:9.6pt">① <b>Dos columnas, dos usos.</b> Lees en vergelijk:</p>')
P(mirror([
  ('<b>SER</b> — ¿quién/cómo es? (identidad)', 'Lucía <b>es</b> de Sevilla. · <b>Es</b> alta y simpática.'),
  ('<b>ESTAR</b> — ¿cómo/dónde está? (estado/lugar)', 'Lucía <b>está</b> en casa. · Hoy <b>está</b> cansada.'),
]))
P(obsbox([
  'Mi abuela <span class="hl">es</span> simpática. &nbsp; (siempre — carácter)',
  'Mi abuela <span class="hl">está</span> en Sevilla. &nbsp; (ahora — lugar)',
  'Mi abuela <span class="hl">está</span> cansada. &nbsp; (ahora — estado)',
], vragen='<b>1)</b> Welke zin gaat over een <i>blijvende</i> eigenschap? <b>2)</b> Welke over <i>waar</i> of <i>hoe iemand nu is</i>?'))
P(actx(1, "¿ser o estar? — clasifica los usos",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Zet elk gebruik in de juiste kolom. <span class="words"><b>origen · lugar · descripción física · estado de ánimo · carácter · posición ahora</b></span></p>'
  + sortcols([("SER (identidad)",""),("ESTAR (estado/lugar)","")], eigen=False), apoyo="Modelo"))
P(actx(2, "Empareja frase ↔ uso",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Verbind de zin met de reden voor ser of estar (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>Letra</th><th></th><th>Uso</th></tr></thead><tbody>'
  '<tr><td>1 · Es española.</td><td><span class="wl sm"></span></td><td>A</td><td>estado (nu moe)</td></tr>'
  '<tr><td>2 · Está en el parque.</td><td><span class="wl sm"></span></td><td>B</td><td>identiteit/origine</td></tr>'
  '<tr><td>3 · Está cansada.</td><td><span class="wl sm"></span></td><td>C</td><td>plaats</td></tr></tbody></table>', apoyo="Modelo"))
P('</div>')  # page §4.1
# §4.2 regla + tree + cloze
P('<div class="page">')
P('<div class="divider">La máquina de decisión · §4.2</div>')
P('<h3>§4.2 · ¿Cómo elijo? — el árbol de decisión</h3>')
P('<p style="font-size:9.6pt">① <b>Sigue el árbol.</b> Stel jezelf de vraag:</p>')
P(tree([
  '¿Es una <b>identidad</b> o <b>descripción</b> permanente (quién/cómo es, origen, profesión)? <span class="yes">SÍ →</span> <span class="res">SER</span>',
  '¿Es un <b>estado</b> pasajero (hoe iemand nú is) o un <b>lugar</b> (waar)? <span class="yes">SÍ →</span> <span class="res">ESTAR</span>',
  'Truco: <b>ESTAR</b> tiene una <b>-t-</b> como en… ¡es<b>t</b>ado y es<b>t</b>ás!',
]))
P('<table class="conj"><thead><tr><th>Persona</th><th>ser</th><th>estar</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">soy</td><td class="v">estoy</td></tr>'
  '<tr><td class="p">tú</td><td class="v">eres</td><td class="v">estás</td></tr>'
  '<tr><td class="p">él/ella/usted</td><td class="v">es</td><td class="v">está</td></tr>'
  '<tr><td class="p">nosotros/-as</td><td class="v">somos</td><td class="v">estamos</td></tr>'
  '<tr><td class="p">vosotros/-as</td><td class="v">sois</td><td class="v">estáis</td></tr>'
  '<tr><td class="p">ellos/-as/ustedes</td><td class="v">son</td><td class="v">están</td></tr></tbody></table>')
P(regla("Regla · ser vs. estar",
  '<p><b>SER</b> = identidad, origen, carácter, descripción física (es alta, es de Sevilla, es simpática). '
  '<b>ESTAR</b> = estado de ánimo, lugar (está cansada, está en casa). '
  '<br>🔴 <b>Valstrik NL:</b> beide vertaal je met «zijn». Vraag je altijd af: <i>blijvend (ser)</i> of <i>nu/plaats (estar)</i>?</p>'))
P(actx(3, "Elige ser o estar",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Kruis de juiste vorm aan.</p>'
  '<p style="margin-left:12.5mm">a) Mi padre ☐ es ☐ está alto. &nbsp; b) Mi hermana ☐ es ☐ está en Madrid.<br>c) Hoy yo ☐ soy ☐ estoy cansado. &nbsp; d) Nosotros ☐ somos ☐ estamos de Bélgica.</p>', apoyo="Pista: blijvend? → ser"))
P(actx(4, "Completa con ser o estar (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>Vul de juiste vorm in. Het infinitief staat tussen haakjes.</p>'
  '<p style="margin-left:12.5mm">1. Mi abuela <span class="wl md"></span> <i>(ser)</i> simpática y hoy <span class="wl md"></span> <i>(estar)</i> en Sevilla.<br>'
  '2. Yo <span class="wl md"></span> <i>(tener)</i> dos primos.<br>'
  '3. Mis padres <span class="wl md"></span> <i>(ser)</i> de Andalucía.<br>'
  '4. Nosotros <span class="wl md"></span> <i>(estar)</i> en casa.<br>'
  '5. ¿Cuántos hermanos <span class="wl md"></span> <i>(tener)</i> tú?<br>'
  '6. Lucía <span class="wl md"></span> <i>(tener)</i> el pelo largo y <span class="wl md"></span> <i>(ser)</i> morena.<br>'
  '7. Mi hermano <span class="wl md"></span> <i>(estar)</i> cansado.<br>'
  '8. Vosotros <span class="wl md"></span> <i>(ser)</i> muy majos.</p>'
  '<p style="margin-left:12.5mm" class="gloss">✅ De sleutel staat online (zelfcorrectie op de digitale pagina).</p>', apoyo="Pista: ser/estar/tener"))
P(tarea_com("Tarea comunicativa · ¿Cómo es y cómo está hoy?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p><b>Situatie:</b> beschrijf een familielid met <b>ser</b> (blijvend) én zeg hoe hij/zij zich <b>vandaag</b> voelt of waar hij/zij is met <b>estar</b>. Je buur reageert. <span class="gloss">«Mi tía es muy alegre, pero hoy está un poco cansada.»</span></p>'
  '<div class="wbox sm"></div>'
  '<div class="steun" style="margin-left:0mm">Marco: es… / está…</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «ser o estar» (clasifica) en «ser/estar (cloze)».</div>')
P('</div>')  # page §4.2

# ================= §5 · LOS DEMOSTRATIVOS =================
retos("ser_estar", "§4.4 · Reto — la foto que delata",
      'Una foto, tres pies, y una palabra que lo decide todo.',
      'Eén foto, drie onderschriften, en één woord dat alles beslist.')
P('<div class="page"><div class="parada sec">')
P('<span class="num">5</span><span class="pk">§5 · Los demostrativos — este y ese</span>')
P('<div class="intro"><b>ES:</b> Con el álbum en la mano señalas: <b>este</b> es mi hermano (cerca), <b>ese</b> es mi tío (más lejos). Aprendes <b>este/esta/estos/estas</b> y <b>ese/esa/esos/esas</b>. <span class="gloss">Aanwijzen bij de foto’s: dit (dichtbij) / dat (verder).</span></div>')
P(lpd(("8","taalsysteem: demostrativos"), ("7","woordenschat: familia"), ("4","aanwijzen & voorstellen")))
P('</div>')
# §5.1 este/ese
P('<h3 style="margin-top:6mm">§5.1 · este (cerca) · ese (lejos)</h3>')
P('<p style="font-size:9.6pt">① <b>Señala en el álbum.</b> Lucía wijst naar de foto\'s:</p>')
P(zoom("cerca (aquí)", "este / esta", "más lejos (ahí)", "ese / esa"))
P(obsbox([
  '<span class="hl">Este</span> es mi hermano Marco. — <span class="hl">Esta</span> es mi madre.',
  '<span class="hl">Ese</span> es mi tío. — <span class="hl">Esos</span> son mis primos.',
], vragen='<b>1)</b> Wanneer gebruik je <i>este</i> en wanneer <i>ese</i>? <b>2)</b> Wat verandert bij vrouwelijk/meervoud?'))
P(actx(1, "¿este o ese? — según la distancia",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Vul este of ese in. Tussen haakjes staat hoe ver de persoon staat.</p>'
  '<p style="margin-left:12.5mm">a) (dichtbij) <span class="wl sm"></span> es mi hermana. &nbsp; b) (verder) <span class="wl sm"></span> es mi abuelo.<br>c) (dichtbij) <span class="wl sm"></span> son mis padres. &nbsp; d) (verder) <span class="wl sm"></span> es mi prima.</p>', apoyo="Pista: cerca = este"))
P('</div>')  # page §5.1
# §5.2 congruencia
P('<div class="page">')
P('<div class="divider">Concordancia de los demostrativos · §5.2</div>')
P('<h3>§5.2 · este / esta / estos / estas</h3>')
P('<p style="font-size:9.6pt">① <b>Los cuatro, como bloques.</b> Kies de vorm bij geslacht + getal:</p>')
P(blocks([
  [("opt","este hermano"),("opt","esta hermana")],
  [("opt","estos hermanos"),("opt","estas hermanas")],
  [("opt","ese tío"),("opt","esa tía"),("opt","esos tíos"),("opt","esas tías")],
]))
P(regla("Regla · demostrativos",
  '<p><b>este</b> (m) · <b>esta</b> (f) · <b>estos</b> (m.pl) · <b>estas</b> (f.pl) = dit/deze (dichtbij). '
  '<b>ese/esa/esos/esas</b> = dat/die (verder). Ze passen in <b>geslacht en getal</b> bij het zn. '
  '<br>🟡 <b>Truc:</b> <b>e-s-t</b>e = dichtbij (met -t- van «hier bij mij»); <b>ese</b> = verder.</p>'))
P(actx(2, "Completa con el demostrativo",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul este/esta/estos/estas in (alles dichtbij, in het album).</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl sm"></span> es mi padre.<br>'
  '2. <span class="wl sm"></span> es mi tía Carmen.<br>'
  '3. <span class="wl sm"></span> son mis hermanos.<br>'
  '4. <span class="wl sm"></span> son mis primas.</p>'
  '<p style="margin-left:12.5mm" class="gloss">✅ Zelfcorrectie online.</p>', apoyo="Marco: este/esta/estos/estas"))
P(tarea_com("Tarea comunicativa · Presenta tu álbum",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p><b>Situatie:</b> toon (echte of getekende) foto\'s en stel je familie voor met <b>este/esta</b> + <b>ser</b> + una descripción. Je buur stelt vragen. <span class="gloss">«Esta es mi madre. Es alta y muy simpática.»</span></p>'
  '<div class="wbox sm"></div>'
  '<div class="steun" style="margin-left:0mm">Modelo: Lucía</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «este o ese» en «señala en el álbum».</div>')
P('</div>')  # page §5.2

# ================= §6 · LECTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">6</span><span class="pk">§6 · Lectura 1 — «La familia de Lucía»</span>')
P('<div class="intro"><b>ES:</b> Lees el álbum de Lucía. Antes de leer <b>predices</b>, luego <b>escaneas</b> y <b>compruebas</b> (verdadero/falso con prueba), y al final <b>reaccionas</b>. <span class="gloss">Volledige leesketen: voorspellen → scannen → juist/fout met bewijs → reageren.</span></div>')
P(lpd(("1","hoofdgedachte begrijpen"), ("2","relevante info vinden"), ("7","woordenschat in context"), ("3","productieve reactie")))
P('</div>')
P('<div class="lecdoel"><b>Tekstsoort:</b> un álbum/una descripción · <b>Afzender:</b> Lucía · <b>Leesdoel:</b> ontdekken wie tot haar familie hoort en hoe ze zijn.</div>')
P('<div class="txtmeta"><span class="tm"><b>Tekstsoort:</b> descripción</span><span class="tm"><b>Registro:</b> informeel</span><span class="tm"><b>Onderwerp:</b> la familia</span></div>')
P(actx(1, "Antes de leer — predecir",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★☆☆"}],
  '<p>Lucía\'s familie is uit Sevilla. Welke woorden verwacht je in de tekst? Kruis aan.</p>'
  '<p style="margin-left:12.5mm">☐ hermano &nbsp; ☐ paella &nbsp; ☐ abuelos &nbsp; ☐ ordenador &nbsp; ☐ simpática &nbsp; ☐ pelirroja</p>', apoyo=""))
P('<div class="ptexts"><div class="ptext">'
  '<div class="ph"><div class="av">'+AV["lucia"]+'</div><div><div class="nm">Lucía</div><div class="fr">Sevilla 🇪🇸</div></div></div>'
  '<p>¡Hola! Soy Lucía y esta es <b>mi familia</b> de Sevilla. Somos cinco: mis padres, mi hermano mayor Marco, mi hermana menor Ana y yo.</p>'
  '<p>Mi padre se llama <b>Antonio</b>; es alto, moreno y muy tranquilo. Mi madre, <b>Rosa</b>, es baja, rubia y muy habladora.</p>'
  '<p>Mi hermano Marco tiene diecinueve años; es delgado y lleva gafas. Ana solo tiene ocho años: es pequeña, graciosa y un poco tímida.</p>'
  '<p>También tengo dos abuelos, <b>Pepe y Carmen</b>, y una prima, <b>Julia</b>, que es pelirroja y muy simpática. Hoy todos estamos en casa de los abuelos. ¡Es una familia grande y muy alegre!</p>'
  '</div>'
  '<div class="ptext"><div class="ph"><div class="av">'+MOCH+'</div><div><div class="nm">Guía de lectura</div><div class="fr">cómo leer</div></div></div>'
  '<p><b>1. Globaal:</b> ¿de quién habla el texto? <span class="gloss">Waarover gaat het?</span></p>'
  '<p><b>2. Scannen:</b> zoek namen en aantallen.</p>'
  '<p><b>3. Bewijs:</b> markeer de zin die je antwoord bewijst.</p>'
  '<p><b>4. Context:</b> raad <i>habladora</i>, <i>mayor</i>, <i>lleva gafas</i> uit de zin.</p>'
  '<p><b>5. Reageer:</b> vergelijk met je eigen familie.</p></div></div>')
P(actx(2, "Escanea — busca los datos",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Zoek snel de informatie in de tekst.</p>'
  '<p style="margin-left:12.5mm">¿Cuántos son en la familia? <span class="wl sm"></span> · ¿Cómo se llama el padre? <span class="wl md"></span><br>¿Cuántos años tiene Ana? <span class="wl sm"></span> · ¿Quién es pelirroja? <span class="wl md"></span></p>', apoyo="Pista: namen zijn vetgedrukt"))
P(actx(3, "Verdadero o falso — con prueba",
  [{"t":"🔍 Analizar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Kruis V of F aan en schrijf de zin uit de tekst die het bewijst (<span class="evi">evidencia</span>).</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba (cita del texto)</th></tr></thead><tbody>'
  '<tr><td>a) Marco es el hermano menor.</td><td><span class="wl sm"></span></td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>b) La madre es muy habladora.</td><td><span class="wl sm"></span></td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>c) Julia es la abuela.</td><td><span class="wl sm"></span></td><td><span class="wl lg"></span></td></tr></tbody></table>', apoyo="Marco: cita = kopieer een zin"))
P(actx(4, "El significado por el contexto",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Wat betekenen deze woorden volgens de tekst?</p>'
  '<p style="margin-left:12.5mm">mayor = <span class="wl md"></span> · habladora = <span class="wl md"></span> · lleva gafas = <span class="wl md"></span></p>', apoyo="Pista: kijk naar de hele zin"))
P(tarea_com("Tarea comunicativa · Y tu familia, ¿cómo es?",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b>Productieve reactie:</b> schrijf een korte tekst zoals Lucía over jouw familie (aantal, namen, één beschrijving per persoon). Lees hem daarna voor. <span class="gloss">Recycle: tener · posesivos · adjetivos · ser/estar.</span></p>'
  '<div class="wbox"></div>'
  '<div class="steun" style="margin-left:0mm">Modelo: de tekst van Lucía</div>'))
P('</div>')  # page §6

# ================= TALLER DE LENGUA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">T</span><span class="pk">Taller de lengua — conectores + ortografía</span>')
P('<div class="intro"><b>ES:</b> Para unir tus frases usas <b>conectores</b>: <b>y</b>, <b>pero</b>, <b>también</b>, <b>porque</b>. Y repasamos la ortografía de los nombres y la concordancia. <span class="gloss">Verbindingswoorden + spelling.</span></div>')
P(lpd(("8","taalsysteem: conectores"), ("9","strategie: schrijven verzorgen")))
P('</div>')
P('<h3 style="margin-top:6mm">Los conectores</h3>')
P(colloc("conectores", ["y = en","pero = maar","también = ook","porque = want/omdat"]))
P('<div class="truc"><b>🔴 Valstrik NL:</b> <b>want</b> én <b>omdat</b> zijn allebei <b>porque</b> (één woord!). En <b>también</b> = «ook» (Mi hermana también es morena).</div>')
P('<h3 style="margin-top:4mm">La ortografía</h3>')
P('<div class="truc"><b>🟡 Recuerda:</b> nombres y apellidos con <b>mayúscula</b> (Antonio, García); los adjetivos concuerdan (-o/-a/-os/-as); la edad = <b>tener … años</b>.</div>')
P(actx(1, "Une con el conector correcto",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul y / pero / también / porque in.</p>'
  '<p style="margin-left:12.5mm">1. Mi hermano es alto <span class="wl sm"></span> delgado.<br>'
  '2. Mi prima es simpática <span class="wl sm"></span> un poco tímida.<br>'
  '3. Me gusta mi familia <span class="wl sm"></span> es muy alegre.<br>'
  '4. Mi madre es habladora; mi tía <span class="wl sm"></span> lo es.</p>'
  '<p style="margin-left:12.5mm" class="gloss">✅ Zelfcorrectie online.</p>', apoyo="Banco de palabras: y·pero·también·porque"))
P(actx(2, "Escribe una descripción unida",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Schrijf drie zinnen over een familielid en verbind ze met minstens twee conectoren.</p>'
  '<div class="wbox sm"></div>', apoyo=""))
P(actx(3, "¿por qué? — responde con porque",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Antwoord op elke vraag met een reden. <span class="gloss">«¿Por qué…? — Porque…»</span></p>'
  '<p style="margin-left:12.5mm">1. ¿Por qué te gusta tu familia? → Porque <span class="wl lg"></span><br>'
  '2. ¿Por qué es especial tu abuelo/a? → Porque <span class="wl lg"></span><br>'
  '3. ¿Por qué es simpático tu mejor amigo/a? → Porque <span class="wl lg"></span></p>', apoyo="Marco: Porque es… / tiene…"))
P(actx(4, "Ordena las palabras — construye la frase",
  [{"t":"🔍 Analizar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Zet de woorden in de juiste volgorde. Schrijf met hoofdletter en punt.</p>'
  '<p style="margin-left:12.5mm">1. simpática · mi · muy · es · hermana → <span class="wl lg"></span><br>'
  '2. alto · pero · mi · es · tímido · primo → <span class="wl lg"></span><br>'
  '3. porque · me · familia · alegre · gusta · es · mi → <span class="wl full"></span>'
  '4. también · mi · morena · abuela · es → <span class="wl lg"></span></p>'
  '<p style="margin-left:12.5mm" class="gloss">✅ Zelfcorrectie online.</p>', apoyo="Pista: begin met het onderwerp"))
P(actx(5, "Corrige la ortografía",
  [{"t":"🔍 Analizar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Zoek en verbeter de fout in elke zin (hoofdletter, concordancia of edad).</p>'
  '<table class="mp"><thead><tr><th>Frase con error</th><th>Correcta</th></tr></thead><tbody>'
  '<tr><td>mi hermano se llama marco.</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>Mi madre es alto y morena.</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>Mi abuela es 70 años.</td><td><span class="wl lg"></span></td></tr></tbody></table>', apoyo="Pista: mayúscula · -o/-a · tener años"))
P('<div class="route-note">🎮 <b>Juega online:</b> «conectores», «caza del adjetivo» en «ortografía» — meerdere reeksen met zelfcorrectie op de digitale pagina.</div>')
P('</div>')  # page Taller

# ================= LECTURA 2 · ESCUCHA =================
# Zelfde bron als de digitale hub (lectura_data / escucha_data): papier en scherm
# kunnen zo niet uit elkaar lopen. Elk op een eigen bladzijde (§14).
P('<div class="page"><div class="parada sec">')
P('<span class="num">7</span><span class="pk">§7 · Lectura 2 — «Mi familia en una foto»</span>')
P('<div class="intro"><b>ES:</b> Un correo de verdad, con foto adjunta. <b>No hace falta entenderlo todo</b> para sacar la información. <span class="gloss">Een echte mail met een foto erbij. Je hoeft niet alles te begrijpen om de informatie te vinden — zoek gericht.</span></div>')
P(PB.lectura_print(LD.C5_U2, "1"))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">8</span><span class="pk">§8 · Escucha — «¿Quién es quién? — el concurso de la clase»</span>')
P('<div class="intro"><b>ES:</b> En clase juegan a adivinar quién es cada foto. <b>Escucha primero, escribe después.</b> <span class="gloss">In de klas raden ze wie er op elke foto staat. Eerst luisteren, dan schrijven; het transcript staat online en gaat pas open ná de taken.</span></div>')
P(PB.escucha_print(ED.C5_U2, "1"))
P('</div>')

# ================= CULTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">C</span><span class="pk">Cultura — La familia hispana</span>')
P('<div class="intro"><b>ES:</b> La familia es muy importante en el mundo hispano. Descubre cómo son las familias, los <b>apodos</b>, la <b>quinceañera</b> y a <b>Frida Kahlo</b>. <span class="gloss">De hechte familie, bijnamen, het 15e verjaardagsfeest en Frida Kahlo.</span></div>')
P(lpd(("5","doeltaalcultuur: la familia hispana"), ("1","cultuurtekst begrijpen")))
P('</div>')
P('<div class="fams" style="margin-top:4mm">'
  '<div class="pcard"><div class="t">La familia grande y unida</div>'
  '<div class="ej" style="margin-top:2mm"><b>ES:</b> En muchos países hispanos la familia es <b>grande</b> y muy <b>unida</b>: abuelos, tíos y primos se ven a menudo, sobre todo los domingos para comer juntos. <span class="gloss">De familie is groot en hecht; men ziet elkaar vaak, vooral op zondag.</span></div></div>'
  '<div class="pcard"><div class="t">Los apodos</div>'
  '<div class="ej" style="margin-top:2mm"><b>ES:</b> Muchos nombres tienen un <b>apodo</b> cariñoso: <b>Pepe</b> = José · <b>Paco</b> = Francisco · <b>Lola</b> = Dolores · <b>Curro</b> = Francisco (Andalucía). <span class="gloss">Bijnamen zijn heel gewoon.</span></div></div></div>')
P('<div class="fams" style="margin-top:4mm">'
  '<div class="pcard"><div class="t">La quinceañera</div>'
  '<div class="ej" style="margin-top:2mm"><b>ES:</b> En América Latina, cuando una chica cumple <b>15 años</b>, se celebra la <b>quinceañera</b>: una gran fiesta familiar con vestido, baile y toda la familia. <span class="gloss">Het grote 15-jaarsfeest voor meisjes in Latijns-Amerika.</span></div></div>'
  '<div class="pcard"><div class="t">Frida Kahlo · «Mi familia»</div>'
  '<div class="ej" style="margin-top:2mm"><b>ES:</b> La pintora mexicana <b>Frida Kahlo</b> pintó su <b>árbol genealógico</b> en el cuadro «Mis abuelos, mis padres y yo». La familia es un gran tema en el arte hispano. <span class="gloss">Frida schilderde haar eigen stamboom.</span></div></div></div>')
P(actx(1, "Reacciona a la cultura",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Vergelijk met België: is de familie bij jou ook groot en hecht? Zie je opa/oma vaak? Ken je apodos? Schrijf twee zinnen.</p>'
  '<div class="wbox sm"></div>', apoyo="Marco: En mi familia… · Veo a mis abuelos…"))
P('<div class="route-note">🎮 <b>Explora online:</b> foto\'s van una quinceañera en el cuadro de Frida Kahlo (Extra-tab).</div>')
P('</div>')  # page Cultura

# ================= TAREA FINAL =================
retos("cultura_u2", "Retos — escuchar a Sevilla",
      'Dos retos con voces de verdad: un abuelo que te escribe y tres vecinos que no se ponen de acuerdo.',
      'Twee retos met echte stemmen: een opa die je schrijft en drie buren die het niet eens zijn.')
P('<div class="page"><div class="parada sec">')
P('<span class="num">★</span><span class="pk">Tarea final — «Álbum de familia»</span>')
P('<div class="intro"><b>ES:</b> Como Lucía, creas tu <b>álbum de familia</b>: un árbol genealógico, fotos con descripciones y un juego «¿Quién es?». <span class="gloss">Jouw familiealbum + stamboom + raadspel.</span></div>')
P(lpd(("3","doelgericht schrijven/spreken"), ("4","interactie"), ("7","woordenschat"), ("8","taalsysteem toepassen")))
P('</div>')
P('<div class="call" style="margin-top:4mm"><div class="ic">🎯</div><div>Lucía deelt haar familiealbum. Jij maakt het jouwe voor de klas: een stamboom, een korte voorstelling en een raadspel «¿Quién es?».</div></div>')
P('<ol class="pasos">'
  '<li><b>El árbol genealógico.</b> Teken je stamboom met minstens zes leden (namen + relatie: mi madre, mi abuelo…). <span class="gloss">Stamboom met posesivos.</span></li>'
  '<li><b>Las fotos.</b> Kies drie personen. Schrijf onder elke foto een onderschrift met <b>ser</b> + twee adjectieven (físico + carácter): «Esta es mi hermana. Es alta y muy simpática.»</li>'
  '<li><b>¿Cómo están hoy?</b> Voeg bij één persoon een zin met <b>estar</b> toe (estado/lugar): «Hoy está en Sevilla / está contenta.»</li>'
  '<li><b>El juego «¿Quién es?».</b> Schrijf een raadsel: beschrijf één familielid zonder de naam; de klas raadt. «Es mayor, tiene el pelo gris y es muy tranquilo. ¿Quién es?»</li>'
  '<li><b>Preséntalo.</b> Toon je album en stel je familie voor met <b>este/esta</b>. Neem het op op de digitale pagina (grábate).</li>'
  '</ol>')
P('<div class="se" style="margin-top:4mm">Rúbrica · ¿lo tengo todo?</div>')
P('<table class="sem"><thead><tr><th>Criterio</th><th>🔴 aún no</th><th>🟠 casi</th><th>🟢 sí</th></tr></thead><tbody>'
  '<tr><td>Árbol con 6+ miembros y posesivos (mi/mis…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>3 descripciones con ser + 2 adjetivos que concuerdan</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>1 frase con estar (estado/lugar)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Juego «¿Quién es?» claro</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Presentación con este/esta (grabada)</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>')
P('<div class="guide"><div class="ic">🎒</div><div><span class="hand">Consejo de la mochila:</span> <span class="g">gebruik de flip cards en de spellen op de digitale pagina om je woorden op te frissen vóór je presenteert.</span></div></div>')
P('</div>')  # page Tarea

# ================= REPASO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">R</span><span class="pk">Repaso — lo esencial de un vistazo</span>')
P('<div class="intro"><b>ES:</b> Tu chuleta de la unidad. El repaso completo (drills + quiz) está <b>online</b>. <span class="gloss">Spiekkaart; het volledige herhalen staat online.</span></div>')
P('</div>')
P('<div class="esen"><b class="tt">Lo esencial de U2</b>'
  '<ul>'
  '<li><b>La familia:</b> padre/madre · hermano/a · abuelos · tíos · primos · hijo/a.</li>'
  '<li><b>tener:</b> tengo · tienes · tiene · tenemos · tenéis · tienen. Edad = tener … años.</li>'
  '<li><b>Posesivos:</b> mi/tu/su → <b>mis/tus/sus</b> (concuerda en número); nuestro/-a.</li>'
  '<li><b>Adjetivos:</b> -o/-a/-os/-as, <b>después</b> del sustantivo; -e/consonante → 2 vormen.</li>'
  '<li><b>ser</b> = identidad/descripción · <b>estar</b> = estado/lugar. 🔴 beide = «zijn».</li>'
  '<li><b>Demostrativos:</b> este/esta/estos/estas (cerca) · ese/esa/esos/esas (lejos).</li>'
  '</ul></div>')
P('<div class="divider">El semáforo · ¿cómo voy?</div>')
P('<table class="sem"><thead><tr><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr></thead><tbody>'
  '<tr><td>nombrar a los miembros de la familia</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>usar tener y decir cuántos tengo</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>usar los posesivos (mi/mis…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>describir a alguien (concordancia)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>elegir entre ser y estar</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>señalar con este/ese</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil de U2: <span class="wl md"></span> · Lo más difícil: <span class="wl md"></span></i></div>')
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> alle spellen van U2 met zelfcorrectie + de flip cards van álle woorden.</div>')
P('<div class="bridge"><b>» Siguiente parada: Barcelona (U3).</b> Ya sabes presentar a tu gente; en <b>U3 «El tiempo vuela»</b> aprendes <b>la hora</b> y tu <b>rutina diaria</b>. <span class="gloss">Op naar Barcelona: de klok en je dagritme.</span></div>')
P('</div>')  # page Repaso

# ================= §V VOCABULARIO =================
import json
VOC = json.load(open(f"{HERE}/u2_vocab.json", encoding="utf-8"))
GRP = [("familia","La familia"),("fisico","La descripción física"),
       ("colores","Los colores"),("caracter","El carácter"),
       ("cuerpo","El cuerpo (básico)"),("util","Palabras útiles (tener · ser/estar · este/ese)")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL) con icono, audio (TTS) y buscador. <span class="gloss">Online: flip cards met icoon, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (begrijpen en zelf gebruiken)")))
P('</div>')
P('<p style="font-size:9.6pt">Het thema <b>«mi gente»</b> als netwerk — van de familie tot de beschrijving:</p>')
P(clusters([
  ("👪","La familia",["padre · madre · hermano/a","abuelos · tíos · primos","hijo/a · nieto/a"],"Wie is wie."),
  ("🧍","El físico",["alto · bajo · delgado","moreno · rubio · pelirrojo","pelo · ojos · gafas"],"Hoe iemand eruitziet."),
  ("😊","El carácter",["simpático · majo · gracioso","tímido · tranquilo · alegre","trabajador · inteligente"],"Hoe iemand is."),
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
  '<p>Schrijf de vertaling. la abuela = <span class="wl md"></span> · moreno = <span class="wl md"></span> · simpático = <span class="wl md"></span> · los primos = <span class="wl md"></span></p>', apoyo="Modelo"))
P(actx("V.2", "Distinguir — sorteer per thema",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Sorteer: <span class="words"><b>el tío · alto · simpático · rubio · la prima · tímido</b></span></p>'
  + sortcols([("familia",""),("físico",""),("carácter","")], eigen=False), apoyo="Banco de palabras"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het Spaanse woord aan (beginletter gegeven). de zus = <b>h</b>___ · de opa = <b>a</b>___ · blond = <b>r</b>___ · verlegen = <b>t</b>___<br><span class="wl full"></span></p>', apoyo="Primera letra"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Maak één correcte zin met <b>hermano · tener · simpático</b>.</p><div class="wbox sm"></div>', apoyo=""))
P(actx("V.5", "Comunicar — mi familia en tres frases",
  [{"t":"🎙️ Hablar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Combineer een familielid, een posesivo én een adjectief in drie zinnen over jouw gente. Zeg ze daarna hardop.</p>'
  '<p style="margin-left:12.5mm">1) <span class="wl full"></span>2) <span class="wl full"></span>3) <span class="wl full"></span></p>', apoyo=""))
P(mispal("Mis palabras de la unidad", 5))
P('<p style="font-size:9.6pt;margin-top:4mm"><b>Tu red de palabras.</b> Kies uit elk cluster twee woorden en verbind ze in één zin over jouw familie:</p>')
P(vpairs([("un miembro ↔ un físico","Mi hermano es alto."),("un miembro ↔ un carácter","Mi tía es simpática."),("un posesivo ↔ un plural","Mis primos son jóvenes."),("ser ↔ estar","Es alegre, pero hoy está triste.")]))
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Sigue en la página digital:</span> <span class="g">flip cards (ES↔NL) met icoon, audio en de spellen bouwen de steun verder af.</span></div></div>')
P('<div class="bridge"><b>» ¡Hasta la próxima parada!</b> Con tu familia, los posesivos y ser/estar ya puedes describir a tu gente. En <b>U3 «El tiempo vuela»</b> viajas a <b>Barcelona</b> y aprendes la hora. <span class="gloss">Je kan nu je familie beschrijven — op naar Barcelona!</span></div>')
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
   a.href=URL.createObjectURL(blob); a.download='U2_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Español en la práctica · U2 Mi gente</title><style>'
        + CSS + PB.CSS + RP.CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/U2.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes")
