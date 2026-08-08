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
import qr_print as QRP; QRP.fijar("C5", 5)
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
h2,h3,.pk,.divider,.se,.acthead,.intro,.route-note,.lpd,.asset{ break-after:avoid; }
.regla,.truc,.pcard,.call,.qr,.guide,.esen,.audiorow,.wcols,.wbox,.sem,.acthead,.chatline,.fichacard,.mispal,.ptext,.lecdoel,.gustobars{ break-inside:avoid; }
.newpage{ break-before:page; }
.act{ break-inside:auto; }
.alf tr,.mp tr,.sem tr,.conj tr{ break-inside:avoid; } .alf thead,.mp thead,.sem thead,.conj thead{ display:table-header-group; }
.sec{ break-before:page; } .hero + .page{ break-before:avoid; }
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
  <div class="tab">U5 · ¡ÑAM!</div>
  <div class="eyebrow">UNIDAD 5 · LA RUTA · PARADA 5 — MÉXICO / CDMX 🇲🇽</div>
  <h1>¡Ñam!</h1>
  <div class="sub">Cruzamos <b>el charco</b> y llegamos a <b>México</b>. Hoy praat je over <b>eten</b>: en el mercado, en el restaurante, y bestel je zoals een echte cliente. <span class="gloss">We steken de oceaan over naar Mexico. Vandaag: eten, de markt, het restaurant en bestellen.</span></div>
  <div class="q">¿Qué vas a comer hoy? <span style="font-weight:400;opacity:.9">· Wat ga je vandaag eten?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U2 · Sevilla</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U3 · Barcelona</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U4 · València</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U5 · México</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U6 · Mercados</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U7–U8 · Colombia · Perú</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 5 · Ciudad de México (CDMX).</b> Cruzamos el océano. Aquí <b>Diego</b> te lleva al <b>mercado</b> y a un <b>restaurante</b>: aprendes cantidades, a decir qué <b>vas a comer</b> y a <b>pedir</b> con cortesía. <span class="gloss">Diego neemt je mee naar de markt en het restaurant.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> En <b>CDMX</b> hay olores y colores por todas partes. <b>Diego</b> te enseña el <b>mercado</b>: «¿<b>Cuánto</b> quieres? ¿<b>mucho</b> o <b>poco</b>?». Luego vais a un restaurante: «¿Qué <b>vas a tomar</b>?». Aprendes a <b>pedir</b> comida y bebida, y a pedir la <b>cuenta</b>.
      <span class="gloss">In CDMX ruikt en kleurt het overal. Diego toont je de markt en jullie gaan naar een restaurant. Je leert eten & drinken bestellen en de rekening vragen.</span></div>
      <div class="ojo"><b>¡Ojo! — de valstrik van vandaag:</b> «lekker» = <b>rico/-a</b> (niet <span class="trap">sabroso</span> nodig), en «pikant» = <b>picante</b> — <i>let op:</i> <b>picante ≠ pica</b> nu niet «prikken». En je bestelt beleefd met <b>¿me pone…?</b> of <b>para mí…</b>, niet met «quiero» alleen.</div>
    </div>
    <div>
      <div class="se">La gente de la ruta</div>
      <div class="cast">
        <div class="pc"><div class="avw">{AV["diego"]}</div><div class="nm">Diego</div><div class="fr">CDMX 🇲🇽 · anfitrión</div></div>
        <div class="pc"><div class="avw">{AV["lucia"]}</div><div class="nm">Lucía</div><div class="fr">Sevilla 🇪🇸</div></div>
        <div class="pc"><div class="avw">{AV["valen"]}</div><div class="nm">Valen</div><div class="fr">Cartagena 🇨🇴</div></div>
        <div class="pc"><div class="avw">{AV["nina"]}</div><div class="nm">Nina</div><div class="fr">Cusco 🇵🇪</div></div>
        <div class="pc tu"><div class="avw">{TU}</div><div class="nm">Tú</div><div class="fr">Flandes 🇧🇪</div></div>
      </div>
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila de sabores</span><br><span class="gloss" style="font-size:8.5pt">In CDMX vul je je rugzak met de woorden van eten: comida, bebida, la carta, la cuenta, ¡que aproveche!</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">nombrar comida y bebida</span> (fruta, verdura, la mesa) <span class="nl">eten & drinken benoemen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">hablar de cantidades</span> (mucho/poco/un poco de · un kilo de) <span class="nl">over hoeveelheden praten</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">decir qué vas a comer</span> con <b>ir a + infinitivo</b> <span class="nl">zeggen wat je gaat eten (futuro próximo)</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">pedir en el restaurante</span> (¿me pone…? · para mí… · la cuenta) <span class="nl">bestellen met cortesía</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar lo/la/los/las</span> (la cuenta → la traigo) <span class="nl">OD-voornaamwoord (aanzet)</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">crear tu <b>carta</b></span> y pedir en pareja <span class="nl">je eigen menu maken (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>Cantidades</span><span><b>§2</b>Voy a comer</span><span><b>§3</b>Pedir · cortesía</span><span><b>§4</b>La cuenta (lo/la)</span><span><b>§5</b>Lectura</span><span><b>Taller</b>Receta/conect.</span><span><b>Cultura</b>Tacos & mercados</span><span><b>Tarea</b>La carta</span><span><b>Repaso</b>Semáforo</span>
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
P('<div class="intro"><b>ES:</b> Antes de comer, recordamos lo que necesitas hoy: los <b>números</b> (para los precios y las cantidades), el verbo <b>gustar</b> (U4) y el <b>presente</b>. <span class="gloss">Voor we gaan eten: kort ophalen — getallen, gustar en het presente.</span></div>')
P(lpd(("7","woordenschat inzetten"), ("8","presente & getallen ophalen"), ("9","strategieën / lengua de clase")))
P('</div>')
P('<p style="font-size:9.6pt">① <b>¿Qué tienes ya en la mochila?</b> Drie clusters die je vandaag inzet. <span class="gloss">Wat zit er al in je rugzak? geheugenraster.</span></p>')
P(clusters([
  ("🔢","Números (U0)",["diez · veinte","cincuenta","cien · ¿cuánto?"],"Voor prijzen en hoeveelheden."),
  ("👍","Gustar (U4)",["me gusta / me gustan","me encanta","no me gusta"],"Zeggen wat je lekker vindt."),
  ("🔤","Presente (U1/U3)",["yo como · tú comes","nosotros bebemos","ellos quieren"],"De vormen die je al kent."),
]))
P(actx(1, "Calentamiento: ¿qué comes normalmente?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Zeg drie dingen die je vaak eet of drinkt, met <b>me gusta(n)</b>. Je buur noteert. Wissel.</p>'
  '<p style="margin-left:12.5mm">Modelo: <i>«Me gusta la pasta y me gustan las manzanas.»</i><br>Mi compañero/a come/bebe: <span class="wl full"></span></p>', apoyo="MODELO → SIN AYUDA"))
P(actx(2, "Números para los precios",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Schrijf de prijs voluit (¿cuánto cuesta?).</p>'
  '<table class="mp"><thead><tr><th>Precio</th><th>En letras</th></tr></thead><tbody>'
  '<tr><td>12 €</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>25 €</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>100 €</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="PISTA (doce · veinticinco · cien)"))
P(actx(3, "Ordena por hambre",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Zet op een lijn van <b>nada</b> (0) naar <b>mucha hambre</b> (100%).</p>'
  + scale(["nada","un poco","bastante","mucha hambre"]) +
  '<p style="margin-left:12.5mm">Ik heb nu: <span class="wl md"></span> hambre.</p>', apoyo="MODELO (lijn gegeven)"))
P(actx(4, "Empareja la comida con la comida del día",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind (schrijf de letter). Repaso rutina (U3) + comida.</p>'
  '<table class="mp"><thead><tr><th>Momento</th><th></th><th>Comida típica</th></tr></thead><tbody>'
  '<tr><td>1 · el desayuno</td><td><span class="wl sm"></span></td><td>A · una sopa y pollo</td></tr>'
  '<tr><td>2 · el almuerzo / la comida</td><td><span class="wl sm"></span></td><td>B · café con leche y tostada</td></tr>'
  '<tr><td>3 · la cena</td><td><span class="wl sm"></span></td><td>C · una ensalada ligera</td></tr></tbody></table>', apoyo="BANCO"))
P(actx(5, "Mi comida favorita en presente",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf twee ware zinnen: één met <b>como</b> en één met <b>bebo</b>.</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (yo como… / yo bebo…)"))
P(actx(6, "Verdadero para mí",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Zet ✔ als het klopt, ✘ als niet. Verbeter er één met een presente-zin.</p>'
  '<p style="margin-left:12.5mm">☐ Me gusta el pescado. &nbsp; ☐ Bebo mucha agua. &nbsp; ☐ No como carne.<br>Mi corrección: <span class="wl full"></span></p>', apoyo="MODELO"))
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> números, gustar en comida-básica met zelfcorrectie op de digitale pagina.</div>')
P('</div>')  # close §0

# ================= §1 · CANTIDADES =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">1</span><span class="pk">§1 · Cantidades · mucho / poco / un poco de</span>')
P('<div class="route-note">📍 Parada 5 · CDMX — Diego te lleva al mercado: «¿Cuánto quieres?».</div>')
P('<div class="intro"><b>ES:</b> Primero <b>descubres</b> la escala de cantidad (nada ▸ poco ▸ mucho), después usas <b>un kilo de</b>, <b>una botella de</b>… en el mercado. La ruta: contexto → observar → regla → practicar → comunicar. <span class="gloss">Eerst de hoeveelheidsschaal, dan de maten in de markt.</span></div>')
P(lpd(("8","taalsysteem: cantidad + concordantie mucho/-a"), ("7","woordenschat: comida/mercado"), ("3","doelgericht schrijven met steun"), ("4","mondelinge interactie")))
P('</div>')
# §1.1 observar via schuifregelaar
P('<h3 style="margin-top:6mm">§1.1 · La escala de cantidad — el deslizador</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto.</b> Diego chat met jou over de boodschappen. Kijk <b>hoeveel</b> hij van elk wil. <span class="gloss">Let op mucho/poco/un poco de.</span></p>')
P('<div class="chat">'
  '<div class="chatline you"><div class="bub">¿Compramos fruta? Necesitamos <span class="fx ob">muchas</span> manzanas.</div><div class="who">Diego</div></div>'
  '<div class="chatline me"><div class="bub">Vale. Y <span class="fx ob">un poco de</span> queso, ¿no?</div><div class="who">Tú</div></div>'
  '<div class="chatline you"><div class="bub">Sí, <span class="fx ob">poco</span> queso. Y <span class="fx ob">un kilo de</span> tomates.</div><div class="who">Diego</div></div>'
  '<div class="chatline me"><div class="bub">¡Perfecto! Y <span class="fx ob">una botella de</span> agua.</div><div class="who">Tú</div></div></div>')
P('<p style="font-size:9.6pt">② <b>El deslizador — de betekenisschuifregelaar.</b> Van niets naar veel:</p>')
P(scale(["nada","un poco de","bastante","mucho/-a"]))
P('<p style="font-size:9.6pt">③ <b>Escala semántica — el tamaño de las porciones:</b></p>')
P(scale(["una pizca","un poco de","medio kilo","un kilo de","mucho/-a"]))
P('<div class="truc"><b>🔴 NL ↔ ES:</b> <b>mucho/poco</b> passen zich aan bij het woord: <b>much<span class="trap">o</span> pan</b> (m.) · <b>much<span class="trap">a</span> fruta</b> (v.) · <b>much<span class="trap">os</span> tomates</b> · <b>much<span class="trap">as</span> manzanas</b>. Maar <b>un poco de</b> verandert nooit: <i>un poco de pan / un poco de leche</i>.</div>')
P(obsbox([
  '<span class="hl">mucho</span> pan · <span class="hl">mucha</span> fruta <span class="gloss">(past bij m./v.)</span>',
  '<span class="hl">muchos</span> tomates · <span class="hl">muchas</span> manzanas <span class="gloss">(meervoud)</span>',
  '<span class="hl">un poco de</span> queso · <span class="hl">un poco de</span> leche <span class="gloss">(altijd gelijk)</span>',
], vragen='<b>1)</b> Wanneer -o/-a? <b>2)</b> Wanneer -os/-as? <b>3)</b> Verandert «un poco de» ooit?'))
P('<p style="font-size:9.6pt">④ <b>Los envases (infographic) — cantidades para comprar:</b></p>')
P('<table class="conj"><thead><tr><th>Envase / cantidad</th><th>+ producto</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="v">un kilo de</td><td class="p">fruta / verdura</td><td>un kilo de tomates</td></tr>'
  '<tr><td class="v">una botella de</td><td class="p">líquido</td><td>una botella de agua</td></tr>'
  '<tr><td class="v">un paquete de</td><td class="p">seco</td><td>un paquete de arroz</td></tr>'
  '<tr><td class="v">un poco de</td><td class="p">no contable</td><td>un poco de queso</td></tr></tbody></table>')
P('</div>')  # page §1.1

# §1.2 práctica
P('<div class="page">')
P('<div class="divider">Practicar · §1.2</div>')
P(actx(1, "¿mucho, mucha, muchos o muchas?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Kruis de juiste vorm aan (kijk naar m./v. en ev./mv.).</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>mucho</th><th>mucha</th><th>muchos</th><th>muchas</th></tr></thead><tbody>'
  '<tr><td>___ pan</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ fruta</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ tomates</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ manzanas</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ agua</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="MODELO (regel §1.1 zichtbaar)"))
P(actx(2, "Clasifica: contable o no contable",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Sorteer: krijgt het <b>un poco de</b> (niet-telbaar) of <b>muchos/-as</b> (telbaar)? '
  '<span class="words"><b>queso · manzanas · agua · tomates · leche · huevos · arroz · uvas</b></span></p>'
  + sortcols([("un poco de","niet telbaar"),("muchos / muchas","telbaar mv.")]), apoyo="BANCO → +1 eigen woord"))
P(actx(3, "Gap-fill: la lista de la compra",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul de cantidad in (un kilo de · una botella de · un paquete de · un poco de).</p>'
  '<p style="margin-left:12.5mm">a) ___ agua &nbsp; b) ___ tomates &nbsp; c) ___ arroz &nbsp; d) ___ queso<br>'
  'e) ___ leche &nbsp; f) ___ manzanas<br><span class="gloss">banco: un kilo de · una botella de · un paquete de · un poco de</span></p>', apoyo="BANCO"))
P(audiorow('<div class="ic">🎧</div><div><b>El dictado de la compra.</b> Diego dicteert een boodschappenlijst. Escucha dos veces y escribe (cantidad + producto). <span class="gloss">Dictee — 1ª betekenis, 2ª schrijven.</span></div>',
           qr("Escanea y escucha", "Audio 5.1 · La lista · 0:50", seed=51)))
P(actx(4, "Dictado: la lista de la compra",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Schrijf de zes producten met hun hoeveelheid (één per regel).</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl lg"></span> 2. <span class="wl lg"></span> 3. <span class="wl lg"></span><br>'
  '4. <span class="wl lg"></span> 5. <span class="wl lg"></span> 6. <span class="wl lg"></span></p>', apoyo="MODELO (twee keer beluisteren)"))
P(actx(5, "Escribe tu lista de la compra",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf vijf producten met een <b>juiste cantidad</b> voor een feestje.</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (un kilo de… / una botella de…)"))
P(actx(6, "¿Es correcto? — ejemplo o no-ejemplo",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Kruis ✔ (goed) of ✘ (fout) aan en verbeter de foute.</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>✔ / ✘</th><th>Corrección</th></tr></thead><tbody>'
  '<tr><td>mucho fruta</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>muchas manzanas</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>un poco de leche</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>muchos agua</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="PISTA (m/v · telbaar) → SIN AYUDA"))
P(actx(7, "Empareja: cantidad ↔ producto",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Welke cantidad past logisch? Verbind (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Cantidad</th><th></th><th>Producto</th></tr></thead><tbody>'
  '<tr><td>1 · una botella de</td><td><span class="wl sm"></span></td><td>A · arroz</td></tr>'
  '<tr><td>2 · un kilo de</td><td><span class="wl sm"></span></td><td>B · agua</td></tr>'
  '<tr><td>3 · un paquete de</td><td><span class="wl sm"></span></td><td>C · queso</td></tr>'
  '<tr><td>4 · un poco de</td><td><span class="wl sm"></span></td><td>D · tomates</td></tr></tbody></table>', apoyo="BANCO"))
P(regla("Regla · cantidades",
  '<p><b>mucho/-a/-os/-as</b> past zich aan bij het woord (much<b>o</b> pan · much<b>a</b> fruta · much<b>os</b> tomates · much<b>as</b> uvas). '
  '<b>un poco de</b> (= een beetje) blijft altijd gelijk en gebruik je bij <b>niet-telbare</b> dingen (queso, leche, agua). '
  '<br>🔴 Envases: <b>un kilo de</b>, <b>una botella de</b>, <b>un paquete de</b> + product.</p>'))
P(tarea_com("Tarea comunicativa · «En el mercado»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b>Afzender·ontvanger·doel·situatie·resultaat:</b> A = cliente met een lijst, B = vendedor/a in de mercado. Vraag om producten met een <b>cantidad</b>; B antwoordt met de prijs. Wissel. <span class="gloss">«¿Me pone un kilo de tomates? —Claro, son dos euros.»</span></p>'
  '<p style="margin-left:12.5mm">Mi compra (3 productos + cantidad): <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: MARCO (¿me pone…? + cantidad) → SIN AYUDA</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «cantidades» (tetris), «un poco de o muchos» en «señala en el mercado» met zelfcorrectie.</div>')
P('</div>')  # page §1.2

retos("cantidades", "§1.4 · Retos — la cantidad, con consecuencias",
      'Tres retos sobre cantidades: una receta que solo se <b>oye</b>, un mercado con <b>precios de verdad</b> y un producto en <b>cinco palabras</b>.',
      'Drie retos over hoeveelheden: een recept dat je alleen hoort, een markt met echte prijzen, en een product in vijf woorden.')

# ================= §2 · IR A + INFINITIVO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2 · Voy a comer · ir a + infinitivo</span>')
P('<div class="intro"><b>ES:</b> Para decir qué <b>vas a hacer</b> (pronto/luego) usas <b>ir a + infinitivo</b> (el futuro próximo). La ruta: máquina → bloques → regla → practicar → comunicar. <span class="gloss">Om te zeggen wat je (straks) gaat doen: ir a + infinitief.</span></div>')
P(lpd(("8","taalsysteem: ir a + infinitivo (futuro próximo)"), ("4","interactie: plannen"), ("3","doelgericht spreken")))
P('</div>')
# §2.1 machine + bloques
P('<h3 style="margin-top:6mm">§2.1 · La máquina «ir a + infinitivo»</h3>')
P('<p style="font-size:9.6pt">① <b>Observa la máquina.</b> Neem het werkwoord <b>ir</b> in het presente + <b>a</b> + een infinitief:</p>')
P(machine([("persona","yo"),("ir (presente)",'v<span class="end">oy</span>'),("+ a +","a"),("infinitivo","comer"),("frase","voy a comer")]))
P('<p style="font-size:9.6pt">② <b>La tabla de <i>ir</i> (nagerekend):</b></p>')
P('<div class="fams" style="margin-top:2mm">')
P(pcard("ir (presente)", '<table class="conj"><tbody>'
  '<tr><td class="p">yo</td><td class="v">voy</td></tr>'
  '<tr><td class="p">tú</td><td class="v">vas</td></tr>'
  '<tr><td class="p">él/ella</td><td class="v">va</td></tr>'
  '<tr><td class="p">nosotros</td><td class="v">vamos</td></tr>'
  '<tr><td class="p">vosotros</td><td class="v">vais</td></tr>'
  '<tr><td class="p">ellos</td><td class="v">van</td></tr></tbody></table>'))
P(pcard("La fórmula", '<div class="ej"><b>ir</b> (voy, vas, va…) + <b>a</b> + <b>infinitivo</b>.<br>'
  '<i>Voy a <b>comer</b> un taco.</i><br><i>Vamos a <b>pedir</b> la cuenta.</i><br><i>¿Vas a <b>tomar</b> un café?</i></div>'
  '<div class="t2">🔴 Het tweede werkwoord blijft <b>infinitief</b> (comer, pedir…).</div>'))
P('</div>')
P('<p style="font-size:9.6pt">③ <b>Como bloques (/ bouwstroken).</b> Kies één blok uit elke rij:</p>')
P(blocks([
  [("per","(Yo) voy"),("vb","a"),("opt","comer un taco")],
  [("per","(Tú) vas"),("vb","a"),("opt","tomar un refresco")],
  [("per","(Nosotros) vamos"),("vb","a"),("opt","pedir la cuenta")],
  [("per","(Ellos) van"),("vb","a"),("opt","probar el guacamole")],
]))
P(regla("Regla · ir a + infinitivo",
  '<p><b>ir</b> in het presente (voy, vas, va, <b>vamos</b>, vais, van) + <b>a</b> + <b>infinitivo</b>. '
  'Je gebruikt het voor plannen dichtbij: <i>Hoy voy a cenar en casa.</i> '
  '<br>🔴 Vergeet de <b>a</b> niet: <i>voy <b>a</b> comer</i> (niet <span class="trap">voy comer</span>). 🔴 Tweede werkwoord = <b>infinitief</b>.</p>'))
P('</div>')  # page §2.1

# §2.2 práctica + CLOZE (verplicht)
P('<div class="page">')
P('<div class="divider">Practicar · §2.2</div>')
P(actx(1, "Conjuga ir",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Vul de vorm van <b>ir</b> in.</p>'
  '<p style="margin-left:12.5mm">yo <span class="wl sm"></span> · tú <span class="wl sm"></span> · él <span class="wl sm"></span> · nosotros <span class="wl sm"></span> · ellos <span class="wl sm"></span></p>', apoyo="PISTA (v-o-y…) "))
P(actx(2, "Substitutie: cambia la persona",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Herschrijf de zin <b>«voy a comer»</b> voor elke persoon.</p>'
  '<table class="mp"><thead><tr><th>Persona</th><th>… a comer</th></tr></thead><tbody>'
  '<tr><td>tú</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>nosotros</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>ella</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>ellos</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="MARCO (tabla ir) → SIN AYUDA"))
P(actx(3, "Completa con la forma correcta (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p>Vul <b>ir a + infinitivo</b> aan (persoon tussen haakjes). <span class="gloss">Let op: vorm van ir + a + infinitief.</span></p>'
  '<p style="margin-left:12.5mm">1. (Yo) <span class="wl md"></span> comer un taco. <i>(comer)</i><br>'
  '2. ¿(Tú) <span class="wl md"></span> tomar un café? <i>(tomar)</i><br>'
  '3. (Nosotros) <span class="wl md"></span> pedir la cuenta. <i>(pedir)</i><br>'
  '4. Diego <span class="wl md"></span> probar el ceviche. <i>(probar)</i><br>'
  '5. (Ellos) <span class="wl md"></span> reservar una mesa. <i>(reservar)</i><br>'
  '6. (Yo) no <span class="wl md"></span> beber refresco. <i>(beber)</i><br>'
  '7. ¿(Vosotros) <span class="wl md"></span> cenar en casa? <i>(cenar)</i><br>'
  '8. Lucía <span class="wl md"></span> preparar una tortilla. <i>(preparar)</i></p>'
  '<p style="margin-left:12.5mm" class="gloss">✅ De oplossingen staan online (zelfcorrectie op de digitale pagina).</p>', apoyo="PISTA (vorm van ir gegeven idee) → SIN AYUDA"))
P(actx(4, "Cadena de transformación",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Begin met <b>«Voy a comer un taco.»</b> en voer elke opdracht uit (schrijf de hele zin).</p>'
  '<p style="margin-left:12.5mm">→ maak er een <b>vraag</b> van (tú): <span class="wl lg"></span><br>→ verander naar <b>nosotros</b>: <span class="wl lg"></span><br>→ maak <b>ontkennend</b> (yo): <span class="wl lg"></span><br>→ voeg <b>«mañana»</b> toe: <span class="wl lg"></span></p>', apoyo="PISTA → SIN AYUDA"))
P(actx(5, "¿Qué vas a pedir? — escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf drie zinnen: wat je <b>vas a comer</b>, <b>a beber</b> en <b>a probar</b> in México.</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (Voy a … / Voy a probar …)"))
P(tarea_com("Tarea comunicativa · «Nuestros planes para la cena»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 7 min"},{"t":"★★★"}],
  '<p><b>Afzender·ontvanger·doel·situatie·resultaat:</b> vertel elkaar wat jullie vanavond <b>gaan eten en drinken</b> (ir a + infinitivo) en noteer één plan van je buur. <span class="gloss">«Esta noche voy a cenar pasta. ¿Y tú?»</span></p>'
  '<p style="margin-left:12.5mm">El plan de mi compañero/a: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: MARCO (Voy a … · Vamos a …) → SIN AYUDA</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «voy a… (cloze)», «ordena la cena» en de presente-Tetris met zelfcorrectie.</div>')
P('</div>')  # page §2.2

retos("comida", "§2.4 · Retos — la comida bajo sospecha",
      'Una carta con <b>intrusos</b> y una receta explicada <b>en directo</b>, sin poder parar.',
      'Een menukaart met indringers, en een recept dat je live uitlegt zonder te kunnen stoppen.')

# ================= §3 · PEDIR & CORTESÍA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3 · Pedir en el restaurante · la cortesía</span>')
P('<div class="intro"><b>ES:</b> En el restaurante hay dos papeles: el <b>camarero</b> pregunta (¿qué va a tomar?) y el <b>cliente</b> pide (para mí… / ¿me pone…?). Escuchas un diálogo real y aprendes a pedir con cortesía. <span class="gloss">Camarero vraagt, cliente bestelt — beleefd.</span></div>')
P(lpd(("8","taalsysteem: functies pedir/cortesía"), ("4","interactie: bestellen"), ("1","luisteren naar een dialoog"), ("3","mondeling reageren")))
P('</div>')
# §3.1 diálogo + personajes
P('<h3 style="margin-top:6mm">§3.1 · El diálogo del restaurante — observa</h3>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> diálogo (restaurante)</span><span class="tm"><b>Voces:</b> camarero · cliente</span><span class="tm">🎯 pedir comida y bebida</span></div>')
P('<div class="chat">'
  '<div class="chatline you"><div class="bub">Buenas tardes. ¿Qué va a <span class="fx vb">tomar</span>?</div><div class="who">Camarero</div></div>'
  '<div class="chatline me"><div class="bub">Para <span class="fx per">mí</span>, de primero una sopa y de segundo pollo, por favor.</div><div class="who">Tú (cliente)</div></div>'
  '<div class="chatline you"><div class="bub">Muy bien. ¿Y para <span class="fx vb">beber</span>?</div><div class="who">Camarero</div></div>'
  '<div class="chatline me"><div class="bub">¿Me <span class="fx vb">pone</span> una botella de agua?</div><div class="who">Tú (cliente)</div></div>'
  '<div class="chatline you"><div class="bub">Claro. ¡Que aproveche!</div><div class="who">Camarero</div></div>'
  '<div class="chatline me"><div class="bub">Gracias. La <span class="fx ob">cuenta</span>, por favor.</div><div class="who">Tú (cliente)</div></div></div>')
P(audiorow('<div class="ic">🎧</div><div><b>Escucha el diálogo del restaurante</b> y sigue con el dedo. <span class="gloss">Luisterdialoog (script + TTS op de hub). 1ª globaal · 2ª detail.</span></div>',
           qr("Escanea y escucha", "Audio 5.2 · En el restaurante · 1:05", seed=52)))
P('<p style="font-size:9.6pt">① <b>Los dos papeles — ¿quién dice qué?</b></p>')
P('<div class="fams" style="margin-top:2mm">')
P(pcard("🧑‍🍳 El camarero pregunta", '<div class="ej">¿Qué va a tomar?<br>¿Y para beber?<br>¿Algo de postre?<br>¡Que aproveche!</div>'))
P(pcard("🙋 El cliente pide", '<div class="ej">Para mí, …<br>¿Me pone…?<br>¿Me trae…?<br>La cuenta, por favor.</div>'))
P('</div>')
P(colloc("pedir", ["Para mí…","¿Me pone…?","¿Me trae…?","De primero…","De segundo…","La cuenta, por favor"]))
P(regla("Regla · pedir con cortesía",
  '<p>De cliente bestelt beleefd met <b>Para mí, …</b> · <b>¿Me pone…?</b> · <b>¿Me trae…?</b> (+ <b>por favor</b>). '
  'De camarero vraagt <b>¿Qué va a tomar?</b> / <b>¿Y para beber?</b>. '
  '<br>🔴 Zeg niet enkel «quiero» — dat klinkt bot. Gebruik <b>¿me pone…?</b> of <b>para mí…</b>. Structuur: <b>de primero</b> (voor) · <b>de segundo</b> (hoofd) · <b>de postre</b> (na).</p>'))
P('</div>')  # page §3.1

# §3.2 práctica
P('<div class="page">')
P('<div class="divider">Practicar · §3.2</div>')
P(actx(1, "Escucha: ¿camarero o cliente?",
  [{"t":"👂 Escuchar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Kruis aan wie spreekt.</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>camarero</th><th>cliente</th></tr></thead><tbody>'
  '<tr><td>¿Qué va a tomar?</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Para mí, una ensalada.</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>¿Me pone un refresco?</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>¿Y para beber?</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>La cuenta, por favor.</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="MODELO (dialoog §3.1)"))
P(actx(2, "Ordena el diálogo del restaurante",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>zinnen ordenen (1–6).</i> Zet de bestel-dialoog in de juiste volgorde.</p>'
  '<p style="margin-left:12.5mm">___ ¿Y para beber? &nbsp; ___ Buenas tardes, ¿qué va a tomar? &nbsp; ___ La cuenta, por favor.<br>'
  '___ Para mí, de segundo, pollo. &nbsp; ___ ¿Me pone agua? &nbsp; ___ ¡Que aproveche!</p>', apoyo="BANCO (nummers 1–6)"))
P(actx(3, "Completa el diálogo (gap-fill)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul de handige zinnen aan.</p>'
  '<p style="margin-left:12.5mm">—Buenas, ¿qué ___ a tomar? &nbsp;—___ mí, una sopa. &nbsp;—¿Me ___ agua? &nbsp;—Sí. La ___, por favor.<br><span class="gloss">banco: va · Para · pone · cuenta</span></p>', apoyo="BANCO"))
P(actx(4, "Empareja: plato ↔ categoría",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind het gerecht met de gang (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Plato</th><th></th><th>Categoría</th></tr></thead><tbody>'
  '<tr><td>1 · una sopa</td><td><span class="wl sm"></span></td><td>A · de postre</td></tr>'
  '<tr><td>2 · pollo con arroz</td><td><span class="wl sm"></span></td><td>B · de primero</td></tr>'
  '<tr><td>3 · fruta / churros</td><td><span class="wl sm"></span></td><td>C · de segundo</td></tr>'
  '<tr><td>4 · agua / refresco</td><td><span class="wl sm"></span></td><td>D · para beber</td></tr></tbody></table>', apoyo="BANCO"))
P(actx(5, "Pide para ti (escribe tu pedido)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Schrijf jouw bestelling: primero, segundo, postre y bebida — met cortesía.</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (Para mí… / ¿Me pone…?) → SIN AYUDA"))
P(tarea_com("Tarea comunicativa · «En el restaurante»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 9 min"},{"t":"★★★"}],
  '<p><b>Afzender·ontvanger·doel·situatie·resultaat:</b> A = camarero/a, B = cliente. Speel de hele scène: begroeten → bestellen (primero/segundo/beber) → ¡que aproveche! → la cuenta. Wissel van rol. <span class="gloss">Gebruik: ¿Qué va a tomar? · Para mí… · ¿Me pone…? · La cuenta, por favor.</span></p>'
  '<p style="margin-left:12.5mm">☐ begroet · ☐ primero · ☐ segundo · ☐ bebida · ☐ la cuenta<br>Mijn bestelling: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: MARCO (rollenkaart) → SIN AYUDA</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «ordena el diálogo», «¿camarero o cliente?» en de simulatie «¡Pide en el restaurante!».</div>')
P('</div>')  # page §3.2

retos("pedir", "§3.4 · Retos — pedir cuando todo sale mal",
      'Tres retos en la mesa: un camarero que dice <b>«no hay»</b>, una reseña de <b>una estrella</b> sin insultos, y una cuenta que <b>nadie</b> quiere pagar.',
      'Drie retos aan tafel: een ober die «no hay» zegt, een recensie van één ster zonder scheldwoorden, en een rekening die niemand wil betalen.')

# ================= §4 · OD-PRONOMBRES (la cuenta → la traigo) =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4 · La cuenta → la traigo · lo / la / los / las</span>')
P('<div class="intro"><b>ES:</b> Voor niet steeds hetzelfde te herhalen, vervang je het <b>voorwerp</b> door <b>lo/la/los/las</b>. La ruta: contexto → radiografía → contraste → practicar. <span class="gloss">Om herhaling te vermijden vervang je het lijdend voorwerp door lo/la/los/las (A2-aanzet).</span></div>')
P(lpd(("8","taalsysteem: OD-pronomen (aanzet)"), ("4","interactie in de dialoog"), ("3","zinnen herschrijven")))
P('</div>')
P('<h3 style="margin-top:6mm">§4.1 · La radiografía — ¿qué reemplaza «la»?</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto.</b> Diego en de camarero herhalen niet:</p>')
P('<div class="chat">'
  '<div class="chatline me"><div class="bub">¿Me trae la <span class="fx ob">cuenta</span>?</div><div class="who">Tú</div></div>'
  '<div class="chatline you"><div class="bub">Sí, ahora <span class="fx ob">la</span> traigo. <span class="gloss">(la = la cuenta)</span></div><div class="who">Camarero</div></div>'
  '<div class="chatline me"><div class="bub">¿Y los <span class="fx ob">tacos</span>?</div><div class="who">Tú</div></div>'
  '<div class="chatline you"><div class="bub"><span class="fx ob">Los</span> traigo enseguida. <span class="gloss">(los = los tacos)</span></div><div class="who">Camarero</div></div></div>')
P('<p style="font-size:9.6pt">② <b>Radiografía:</b></p>')
P(xray('¿Me trae la cuenta? — Sí, <span class="fx ob">la</span> <span class="fx vb">traigo</span>.',
       [("la","= la cuenta (v. ev.)"),("traigo","werkwoord traer"),("→","geen herhaling!")]))
P('<p style="font-size:9.6pt">③ <b>Contrastes mínimos — de vier vormen:</b></p>')
P(vpairs([("el pan → lo","la carta → la"),("los tacos → los","las gambas → las"),("el postre → lo traigo","la cuenta → la traigo"),("¿el café? → lo pido","¿la sopa? → la pido")]))
P('<div class="truc"><b>🔴 Concordancia:</b> <b>lo</b> (m. ev.) · <b>la</b> (v. ev.) · <b>los</b> (m. mv.) · <b>las</b> (v. mv.). Het pronomen staat <b>vóór</b> het werkwoord: <i>La traigo</i> (niet <span class="trap">traigo la</span>).</div>')
P(regla("Regla · lo / la / los / las (OD-aanzet)",
  '<p>Om het <b>voorwerp</b> niet te herhalen: <b>lo</b> (m. ev.), <b>la</b> (v. ev.), <b>los</b> (m. mv.), <b>las</b> (v. mv.). '
  'Het staat <b>vóór</b> het vervoegde werkwoord: <i>¿La cuenta? — La traigo.</i> · <i>¿Los tacos? — Los quiero.</i></p>'))
P('</div>')  # page §4.1
# §4.2 práctica (kort, A2-aanzet)
P('<div class="page">')
P('<div class="divider">Practicar · §4.2</div>')
P(actx(1, "¿lo, la, los o las?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Welk pronomen vervangt het woord? Kruis aan.</p>'
  '<table class="mp"><thead><tr><th>Palabra</th><th>lo</th><th>la</th><th>los</th><th>las</th></tr></thead><tbody>'
  '<tr><td>la cuenta</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>el pan</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>los tacos</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>las gambas</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>la carta</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="MODELO (regel §4.1)"))
P(actx(2, "Responde con el pronombre (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Antwoord met <b>lo/la/los/las</b> + het werkwoord.</p>'
  '<p style="margin-left:12.5mm">a) ¿Me trae la cuenta? —Sí, ___ traigo.<br>'
  'b) ¿Quieres el postre? —Sí, ___ quiero.<br>'
  'c) ¿Traes los refrescos? —___ traigo ahora.<br>'
  'd) ¿Pides las gambas? —Sí, ___ pido.<br><span class="gloss">✅ Zelfcorrectie op de digitale pagina.</span></p>', apoyo="PISTA (m/v · ev/mv) → SIN AYUDA"))
P(actx(3, "Transforma sin repetir",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Herschrijf zonder het voorwerp te herhalen.</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>Con pronombre</th></tr></thead><tbody>'
  '<tr><td>Traigo la carta.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Quiero el café.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Pido los tacos.</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="MARCO (lo/la/los/las) → SIN AYUDA"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha y marca el pronombre.</b> Cuatro respuestas cortas del camarero. <span class="gloss">Kruis aan welk pronomen je hoort.</span></div>',
           qr("Escanea y escucha", "Audio 5.3 · ¿lo/la/los/las? · 0:40", seed=53)))
P(actx(4, "Escucha: ¿qué pronombre oyes?",
  [{"t":"👂 Escuchar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Kruis aan wélk pronomen je hoort in het antwoord.</p>'
  '<table class="mp"><thead><tr><th>#</th><th>lo</th><th>la</th><th>los</th><th>las</th></tr></thead><tbody>'
  '<tr><td>1</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>2</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>3</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>4</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="MODELO (vier opties open)"))
P(tarea_com("Tarea comunicativa · «¿Me lo trae?»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p><b>Afzender·ontvanger·doel·situatie·resultaat:</b> A vraagt om iets (la carta, el pan, los tacos…), B antwoordt kort met het pronomen. Wissel. <span class="gloss">«¿Me trae la carta? —Sí, la traigo.»</span></p>'
  '<p style="margin-left:12.5mm">Un ejemplo nuestro: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: MARCO (lo/la/los/las) → SIN AYUDA</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «¿lo, la, los o las?» met zelfcorrectie.</div>')
P('</div>')  # page §4.2

retos("pronombres_u5", "§4.4 · Reto — el pronombre decide",
      'Sin pronombre no hay respuesta. Aquí lo compruebas plato por plato.',
      'Zonder voornaamwoord krijg je geen antwoord. Hier bewijs je dat, gerecht per gerecht.')

# ================= §5 · LECTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">📖</span><span class="pk">§5 · Lectura — «Dos cartas / una receta»</span>')
P('<div class="intro"><b>ES:</b> Vas a leer <b>dos menús</b> (la carta de dos restaurantes) y una <b>mini-receta</b>. Primero <b>predices</b>, después lees con un <b>objetivo</b>. <span class="gloss">Je leest twee menu\'s en een recept: eerst voorspellen, dan doelgericht lezen. parallelle teksten.</span></div>')
P(lpd(("1","onderwerp/hoofdgedachte bij lezen"), ("2","relevante info selecteren"), ("3","doelgericht schrijven met steun")))
P('</div>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> la carta (menú) · receta</span><span class="tm"><b>De:</b> dos restaurantes</span><span class="tm">🎯 comparar y elegir</span></div>')
P(actx(1, "Antes de leer: predice",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★☆☆"}],
  '<p>Bekijk de vorm en titels. ¿Qué platos esperas encontrar?</p>'
  '<p style="margin-left:12.5mm">Espero leer sobre: <span class="wl full"></span></p>', apoyo="MODELO (sopa, pollo, postre…)"))
P('<div class="fams" style="margin-top:2mm">')
P(menu("La Cocina de Lucía 🇪🇸", [
  ("De primero", [("Sopa de tomate","4 €"),("Ensalada mixta","5 €")]),
  ("De segundo", [("Pollo con patatas","9 €"),("Pescado a la plancha","11 €")]),
  ("De postre", [("Fruta del día","3 €"),("Churros con chocolate","4 €")]),
]))
P(menu("El Sabor de Diego 🇲🇽", [
  ("Para empezar", [("Guacamole con nachos","5 €"),("Elote con queso","4 €")]),
  ("Platos fuertes", [("Tacos de pollo (3)","8 €"),("Ceviche de pescado","10 €")]),
  ("Para terminar", [("Flan casero","3 €"),("Piña con lima","3 €")]),
]))
P('</div>')
P('<div class="lecdoel">🎯 <b>Objetivo de lectura:</b> lees om te <b>vergelijken</b> welk restaurant welke gerechten heeft en <b>hoeveel</b> ze kosten — je hoeft niet élk woord te begrijpen.</div>')
P('</div>')  # page §5a
P('<div class="page">')
P(actx(2, "Escanea: completa la tabla",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Zoek de gegevens in de twee cartas.</p>'
  '<table class="mp"><thead><tr><th></th><th>Un primero / entrante</th><th>Un segundo / fuerte</th><th>Un postre</th></tr></thead><tbody>'
  '<tr><td><b>Lucía 🇪🇸</b></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td><b>Diego 🇲🇽</b></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '</tbody></table>', apoyo="MODELO (menús boven)"))
P(actx(3, "¿Verdadero o falso? + prueba",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>juist/fout + bewijs (evidence).</i> Waar of niet waar? Noteer de <b>woorden uit de carta</b> die het bewijzen.</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba (precio/plato)</th></tr></thead><tbody>'
  '<tr><td>En casa de Diego hay tacos.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>El pollo con patatas cuesta 9 €.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Los dos tienen postre de fruta.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>El ceviche es un postre.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '</tbody></table>', apoyo="PISTA (onderstreep in de carta)"))
P(actx(4, "Del contexto: ¿qué significa?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Wat betekent <b>«plato fuerte»</b> en <b>«casero»</b>? Kies + leg uit welke aanwijzing hielp.</p>'
  '<p style="margin-left:12.5mm">plato fuerte = ☐ hoofdgerecht ☐ dessert &nbsp;·&nbsp; casero = ☐ zelfgemaakt ☐ duur<br>Pista que me ayudó: <span class="wl lg"></span></p>', apoyo="PISTA"))
P('<div class="ptexts">'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["diego"]}</div><div><div class="nm">Diego · una receta</div><div class="fr">guacamole en 3 pasos</div></div></div>'
  '<p><b>Ingredientes:</b> un <span class="evi">aguacate</span>, un <span class="evi">tomate</span>, un poco de <span class="evi">cebolla</span> y <span class="evi">lima</span>.<br>'
  '<b>Pasos:</b> <span class="evi">Primero</span>, abre el aguacate. <span class="evi">Luego</span>, añade el tomate y la cebolla. <span class="evi">Después</span>, exprime la lima. <span class="evi">¡Que aproveche!</span></p></div>'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["nina"]}</div><div><div class="nm">@comidasana</div><div class="fr">comentario ★★★★☆</div></div></div>'
  '<p>¡Qué rica <span class="evi">la receta</span>! Yo <span class="evi">voy a preparar</span> guacamole el sábado. En Perú lo comemos con <span class="evi">maíz</span>. Es fácil, barato y <span class="evi">muy sano</span>. ¿Tú lo vas a probar?</p></div></div>')
P(actx(5, "Ordena la receta",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Zet de stappen van de receta in volgorde (1–4) met de conectores.</p>'
  '<p style="margin-left:12.5mm">___ Después, exprime la lima. &nbsp; ___ Primero, abre el aguacate. &nbsp; ___ ¡Que aproveche! &nbsp; ___ Luego, añade el tomate y la cebolla.</p>', apoyo="BANCO (primero/luego/después)"))
P(tarea_com("Tarea comunicativa · «¿Qué vas a pedir?» (keten lezen→spreken)",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b>Keten lezen → spreken.</b> Kies één van de twee cartas. Zeg wat je <b>vas a pedir</b> (primero, segundo, postre, bebida) én waarom. Je buur bestelt uit de andere carta. <span class="gloss">«Voy a pedir tacos de pollo porque me gusta el pollo.»</span></p>'
  '<div class="wbox sm"></div>'
  '<div class="steun" style="margin-left:0mm">Apoyo: MARCO (Voy a pedir… porque…) → SIN AYUDA</div>'))
P('<div class="route-note">🎮 <b>Sigue online:</b> luister de cartas (TTS), lees de receta en neem je bestelling op (recorder) op de digitale pagina.</div>')
P('</div>')  # page §5b

# ================= TALLER DE LENGUA =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num" style="color:var(--crema)">✎</span><span class="pk" style="background:var(--gd)">Taller de lengua</span>')
P('<div class="intro"><b>ES:</b> Dos herramientas: los <b>conectores de secuencia</b> (primero/luego/después — ¡para las recetas!) y la <b>ortografía</b> de la ñ y las palabras de comida. <span class="gloss">Conectoren van volgorde + spelling.</span></div>')
P(lpd(("8","taalsysteem: conectoren + ortografía"), ("3","tekst ordenen")))
P('</div>')
P('<h3 style="margin-top:6mm">Conectores de secuencia · primero · luego · después · por último</h3>')
P('<p style="font-size:9.6pt">① <b>La receta como una escalera de pasos:</b></p>')
P(scale(["primero","luego","después","por último"]))
P('<table class="mp"><thead><tr><th>Conector</th><th>Uso</th><th>Ejemplo (receta)</th></tr></thead><tbody>'
  '<tr><td><b>primero</b></td><td>eerste stap</td><td><b>Primero</b>, corta el tomate.</td></tr>'
  '<tr><td><b>luego / después</b></td><td>daarna</td><td><b>Luego</b>, añade la cebolla.</td></tr>'
  '<tr><td><b>por último</b></td><td>laatste stap</td><td><b>Por último</b>, exprime la lima.</td></tr></tbody></table>')
P(actx(1, "Une la receta con conectores",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het juiste verbindingswoord in (primero/luego/después/por último).</p>'
  '<p style="margin-left:12.5mm">___ , pon el arroz en el agua. ___ , añade la sal. ___ , espera 15 minutos. ___ , ¡a comer!<br><span class="wl full"></span></p>', apoyo="BANCO"))
P('<h3 style="margin-top:6mm">Ortografía · la ñ y los sonidos de la comida</h3>')
P('<div class="truc"><b>🔴 La ñ:</b> <b>ñ</b> klinkt als «nj»: <b>ñam-ñam</b>, la <b>pi<span class="trap">ñ</span>a</b>, el <b>ni<span class="trap">ñ</span>o</b>. Verwar niet met <b>n</b>: <i>pena</i> ≠ <i>peña</i>.</div>')
P(actx(2, "¿n o ñ?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Vul <b>n</b> of <b>ñ</b> in.</p>'
  '<p style="margin-left:12.5mm">la pi__a (ananas) · ma__a__a (morgen) · el ni__o · la ca__a · a__o (jaar)<br><span class="gloss">Let op: piña, mañana, niño, caña, año.</span></p>', apoyo="PISTA (klank «nj»)"))
P(actx(3, "Dictado corto de la cocina",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>dictee (reconstrueren).</i> Escucha y escribe cuatro palabras de comida (con tilde/ñ).</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl md"></span> 2. <span class="wl md"></span> 3. <span class="wl md"></span> 4. <span class="wl md"></span></p>', apoyo="MODELO (2×)"))
P(actx(4, "Escribe tu mini-receta con conectores",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Schrijf een receta van 3–4 stappen (un bocadillo, una ensalada…) met <b>primero · luego · después · por último</b>.</p>'
  '<div class="wbox sm"></div>', apoyo="SIN AYUDA"))
P(actx(5, "Corrige la receta",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Zoek de fout (conector, cantidad of ñ/spelling) en herschrijf correct.</p>'
  '<p style="margin-left:12.5mm">1) <span class="trap">Primero corta el tomate. Primero añade la sal.</span> → <span class="wl lg"></span><br>'
  '2) <span class="trap">Necesito mucho fruta.</span> → <span class="wl lg"></span><br>'
  '3) <span class="trap">Me gusta la pina y la cana.</span> → <span class="wl lg"></span></p>', apoyo="MODELO → SIN AYUDA"))
P('<div class="route-note">🎮 <b>Practica online:</b> «ordena la receta» en de conectoren-oefeningen met zelfcorrectie.</div>')
P('</div>')  # page Taller

# ================= §6 LECTURA · §7 ESCUCHA =================
# Zelfde bron als de digitale hub (lectura_data / escucha_data): papier en scherm
# kunnen zo niet uit elkaar lopen. Elk op een eigen bladzijde (§14).
P('<div class="page"><div class="parada sec">')
P('<span class="num">6</span><span class="pk">§6 · Lectura — «El mercado de La Merced en cinco datos»</span>')
P('<div class="intro"><b>ES:</b> Una infografía de verdad, con cifras. <b>No hace falta entenderlo todo</b> para sacar la información. <span class="gloss">Een echte infografie met cijfers. Je hoeft niet alles te begrijpen — lees de cijfers af en leg ze naast de tekst.</span></div>')
P(PB.lectura_print(LD.C5_U5, "1"))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">7</span><span class="pk">§7 · Escucha — «Una mesa para tres»</span>')
P('<div class="intro"><b>ES:</b> Diego pide en un restaurante del centro, pero un plato ya no queda. <b>Escucha primero, escribe después.</b> <span class="gloss">Diego bestelt in een restaurant, maar één gerecht is op. Eerst luisteren, dan schrijven; het transcript staat online en gaat pas open ná de taken.</span></div>')
P(PB.escucha_print(ED.C5_U5, "1"))
P('</div>')

# ================= CULTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">★</span><span class="pk">Cultura · Tacos, mercados y horarios</span>')
P('<div class="intro"><b>ES:</b> La comida une al mundo hispano. Descubre los <b>mercados</b> de México, el <b>taco</b>, y compara los <b>horarios de comida</b> ES ↔ MX ↔ Bélgica. <span class="gloss">Ontdek de markten, de taco en de eettijden.</span></div>')
P(lpd(("5","kenmerkende aspecten van de cultuur"), ("2","relevante info uit een tekst")))
P('</div>')
P('<div class="fams" style="margin-top:6mm">')
P(pcard("🌮 El taco 🇲🇽", '<div class="ej">De <b>maíz</b>, con carne, verdura y <b>salsa</b>. En CDMX hay <b>taquerías</b> por todas partes. Comparte varios: al pastor, de pollo, de pescado…</div><div class="anchor gloss">El taco = het hart van de Mexicaanse keuken.</div>'))
P(pcard("🏪 Los mercados", '<div class="ej">En los <b>mercados</b> compras fruta, verdura y comida fresca. Regatear el <b>precio</b> es normal. Colores, olores y mucha vida.</div><div class="t2">El mercado = de plek om cantidades te oefenen.</div>'))
P('</div>')
P('<p style="font-size:9.6pt">① <b>Horario de comidas — ¿a qué hora se come? (contraste):</b></p>')
P('<table class="mp"><thead><tr><th>Comida</th><th>🇧🇪 Bélgica</th><th>🇪🇸 España</th><th>🇲🇽 México</th></tr></thead><tbody>'
  '<tr><td>el desayuno</td><td>7:00</td><td>8:00</td><td>8:00</td></tr>'
  '<tr><td>la comida / el almuerzo</td><td>12:00</td><td>14:30</td><td>14:00</td></tr>'
  '<tr><td>la cena</td><td>18:00</td><td>21:30</td><td>20:00</td></tr></tbody></table>')
P('<div class="truc"><b>🟡 Dato:</b> en <b>España</b> se cena <b>muy tarde</b> (21:00–22:00). En <b>México</b> y <b>Bélgica</b> un poco antes. ¡No comas a las 18:00 en Madrid — no hay nadie!</div>')
P('<p style="font-size:9.6pt">② <b>Un plato por país (clusters pan-hispano):</b></p>')
P(vpairs([("la paella 🇪🇸","los tacos 🇲🇽"),("las arepas 🇨🇴","el ceviche 🇵🇪"),("las empanadas 🇦🇷","los churros 🇪🇸")]))
P(actx(1, "Comprensión — verdadero o falso",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Waar of niet waar? Verbeter de foute.</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Corrección</th></tr></thead><tbody>'
  '<tr><td>El taco es de maíz.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>En España se cena a las 18:00.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>La arepa es de Colombia.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="MODELO (tekst boven)"))
P(actx(2, "Un plato de mi país / mi familia",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Schrijf 2–3 zinnen over een typisch gerecht bij jou thuis (¿qué es? ¿qué lleva? ¿cuándo lo comes?). Presenteer aan je buur.</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (Es… · Lleva… · Lo comemos…) → SIN AYUDA"))
P(actx(3, "Empareja: plato ↔ país",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind het typische gerecht met het land (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Plato</th><th></th><th>País</th></tr></thead><tbody>'
  '<tr><td>1 · los tacos</td><td><span class="wl sm"></span></td><td>A · España 🇪🇸</td></tr>'
  '<tr><td>2 · la paella</td><td><span class="wl sm"></span></td><td>B · Perú 🇵🇪</td></tr>'
  '<tr><td>3 · la arepa</td><td><span class="wl sm"></span></td><td>C · México 🇲🇽</td></tr>'
  '<tr><td>4 · el ceviche</td><td><span class="wl sm"></span></td><td>D · Colombia 🇨🇴</td></tr></tbody></table>', apoyo="BANCO"))
P('<div class="route-note">🎮 <b>Sigue online:</b> «plato ↔ país» (match) en de mercado-spellen op de digitale pagina.</div>')
P('</div>')  # page Cultura

retos("cultura_u5", "Retos — la cocina que no se mide",
      'La abuela nunca dice cuánto. Tú tienes que <b>traducirlo a gramos</b>.',
      'De grootmoeder zegt nooit hoeveel. Jij moet het omzetten naar grammen.')

# ================= TAREA FINAL =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num">✦</span><span class="pk" style="background:var(--gd)">Tarea final · La carta</span>')
P('<div class="intro"><b>ES:</b> Crea la <b>carta</b> de tu propio restaurante: primeros, segundos, postres y bebidas con <b>precios</b>. Luego, un compañero <b>pide</b> y tú eres el <b>camarero</b>. <span class="gloss">Maak je eigen menukaart en speel de restaurantscène.</span></div>')
P('<div class="route-note">🎯 <b>Communicatieve taak:</b> afzender = jij (het restaurant) · ontvanger = de cliente · doel = een menu aanbieden & een bestelling opnemen · situatie = un restaurante en CDMX · resultaat = ingevulde carta + gespeelde dialoog.</div>')
P(lpd(("3","doelgericht schrijven met een voorbeeld"), ("4","mondeling interageren (bestellen)"), ("7","woordenschat comida/restaurante"), ("8","cantidades · ir a + inf. · cortesía")))
P('</div>')
P('<ol class="pasos">'
  '<li><b>Elige un nombre</b> para tu restaurante y un país/estilo (mexicano, español…).</li>'
  '<li><b>Rellena la carta</b> hieronder: primeros · segundos · postres · bebidas — met <b>precios</b>.</li>'
  '<li><b>Escribe el diálogo</b> (camarero ↔ cliente): begroeten → bestellen → ¡que aproveche! → la cuenta.</li>'
  '<li><b>Representa</b> la escena en pareja (of neem audio op via de digitale pagina).</li>'
  '<li><b>Pregunta</b> al cliente qué le gusta y recomienda un plato («Le recomiendo…»).</li></ol>')
P('<div class="se" style="margin-top:4mm">Mi carta <span class="gloss" style="font-size:8pt">· vul de gerechten + prijzen in</span></div>')
P('<table class="alf"><thead><tr><th>Sección</th><th>Plato / bebida</th><th>Precio</th></tr></thead><tbody>'
  '<tr><td>De primero</td><td><span class="wl md"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>De segundo</td><td><span class="wl md"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>De postre</td><td><span class="wl md"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>Para beber</td><td><span class="wl md"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>')
P('<div class="se" style="margin-top:5mm">Nuestro diálogo <span class="gloss" style="font-size:8pt">· camarero ↔ cliente</span></div><div class="wbox"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba la escena</b> en la página digital (recorder + rúbrica).</div>',
           qr("Escanea y graba", "Tarea · La carta", seed=54)))
P('<div class="se" style="margin-top:5mm">Mini-encuesta: los platos favoritos de la clase <span class="gloss" style="font-size:8pt">— vraag 5 klasgenoten, teken de balken</span></div>')
P(gustobars([("los tacos", 60), ("la pizza", 50), ("la fruta", 40), ("los churros", 30)]))
P('<p style="font-size:8.6pt" class="gloss">↳ vervang de voorbeeld-balken door je eigen resultaten (aantal /5 → %).</p>')
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Mijn carta heeft <b>4 secties</b> met <b>prijzen</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>cortesía</b> (para mí… / ¿me pone…?)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik zeg wat ik <b>voy a pedir</b> en vraag de <b>cuenta</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>speel de scène</b> vlot in pareja</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — la carta de mi compañero/a</div>'
  '<table><thead><tr><th>Lo que me gusta de su carta</th><th>Un consejo (una cosa)</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('</div>')  # page Tarea

# ================= REPASO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">✓</span><span class="pk">Repaso · lo esencial</span>')
P('<div class="intro"><b>ES:</b> Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, 20 juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag.</span></div>')
P('</div>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>Cantidades:</b> much<b>o</b>/much<b>a</b>/much<b>os</b>/much<b>as</b> (past aan) · <b>un poco de</b> (blijft gelijk) · un kilo de · una botella de.</li>'
  '<li><b>Futuro próximo:</b> <b>ir</b> (voy, vas, va, vamos, vais, van) + <b>a</b> + <b>infinitivo</b>: <i>Voy a comer.</i></li>'
  '<li><b>Pedir con cortesía:</b> ¿Qué va a tomar? · Para mí… · ¿Me pone…? · ¿Me trae…? · La cuenta, por favor. De primero/segundo/postre.</li>'
  '<li><b>lo/la/los/las:</b> ¿La cuenta? → <b>La</b> traigo. ¿Los tacos? → <b>Los</b> quiero (vóór het werkwoord).</li>'
  '<li><b>Las trampas:</b> 🔴 much<b>a</b> fruta ≠ mucho · 🔴 voy <b>a</b> comer (a niet vergeten) · 🔴 pide con cortesía, niet enkel «quiero» · 🔴 la ñ (piña).</li></ul></div>')
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> 14 spelletjes met zelfcorrectie en spreiding op de digitale pagina.</div>')
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td><b>comida y bebida</b> benoemen (fruta, verdura, la mesa)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>over <b>cantidades</b> praten (mucho/poco · un kilo de)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>zeggen wat ik <b>voy a comer</b> (ir a + inf.)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>bestellen</b> met cortesía en de <b>cuenta</b> vragen</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>lo/la/los/las</b> gebruiken (la traigo)</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil de U5: <span class="wl md"></span> · Lo más difícil: <span class="wl md"></span></i></div>')
P('<div class="bridge"><b>» Siguiente parada: los mercados de México (U6).</b> Ya sabes pedir comida; en <b>U6 «De tiendas»</b> vas de compras en el mercado y descubres los precios, las ofertas y el regateo. <span class="gloss">In U6 ga je winkelen op de markt.</span></div>')
P('</div>')  # page Repaso

# ================= §V VOCABULARIO =================
import json
VOC = json.load(open(f"{HERE}/u5_vocab.json", encoding="utf-8"))
GRP = [("comida","Comida · platos y básicos"),("fruta","La fruta"),("verdura","La verdura"),
       ("bebida","Las bebidas"),("mesa","La mesa · los cubiertos"),("restaurante","En el restaurante"),
       ("cantidades","Cantidades y envases"),("cortesia","Pedir con cortesía"),("mexico","Sabores de México y América")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (receptief & productief)")))
P('</div>')
P('<p style="font-size:9.6pt">La <b>comida</b> als netwerk — drie families die de hele unit dragen:</p>')
P(clusters([
  ("🍽️","En el plato",["carne · pescado · pollo","arroz · pasta · sopa","fruta · verdura · pan"],"Wat je eet."),
  ("🥤","Para beber",["agua · zumo · leche","café · té · refresco","una botella de…"],"Wat je drinkt."),
  ("🍴","En el restaurante",["la carta · el menú","el/la camarero/a · la cuenta","para mí… · ¿me pone…?"],"Wat je zegt & doet."),
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
  '<p>Schrijf de vertaling. el pollo = <span class="wl md"></span> · la cuenta = <span class="wl md"></span> · un kilo de = <span class="wl md"></span> · el aguacate = <span class="wl md"></span></p>', apoyo="MODELO"))
P(actx("V.2", "Distinguir — sorteer per familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Sorteer: <span class="words"><b>la manzana · el tenedor · el zumo · la carta · la lechuga · el vaso</b></span></p>'
  + sortcols([("fruta/verdura",""),("bebida",""),("mesa/restaurante","")], eigen=False), apoyo="BANCO"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het Spaanse woord aan (beginletter gegeven). de rekening = <b>c</b>___ · het brood = <b>p</b>___ · de vork = <b>t</b>___ · lekker = <b>r</b>___<br><span class="wl full"></span></p>', apoyo="LETRA INICIAL"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p>Maak één correcte zin met <b>voy a · un poco de · rico</b>.</p><div class="wbox sm"></div>', apoyo="SIN AYUDA"))
P(actx("V.5", "Comunicar — mi menú ideal",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p>Schrijf jouw ideale menu (primero, segundo, postre, bebida) met <b>voy a pedir…</b> én telkens waarom. Zeg het daarna hardop tegen je buur, die als camarero reageert.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>', apoyo="MARCO (Voy a pedir … porque …) → SIN AYUDA"))
P(mispal("Mis palabras de la unidad", 4))
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
   a.href=URL.createObjectURL(blob); a.download='U5_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Español en la práctica · U5 ¡Ñam!</title><style>'
        + CSS + PB.CSS + RP.CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/U5.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes")
