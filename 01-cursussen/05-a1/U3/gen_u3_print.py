#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genereert de print-HTML U3.html (C5 · Unidad 3 «El tiempo vuela») → PDF via Chromium.
# Zelfde componentenkit/pijplijn als golden sample U0/U1 (cursus-print.css). Fonts base64 ingebed,
# cast-avatars inline SVG (cast_gen). Cursuskleur = groen (C5). Output = standalone bewerkbare U3.html.
import os, sys, base64, math
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f"{ROOT}/02-huisstijl/beeld/generators")
import cast_gen as C

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
h2,h3,.pk,.divider,.se,.acthead,.intro,.route-note,.lpd,.asset{ break-after:avoid; }
.regla,.truc,.pcard,.call,.qr,.guide,.esen,.audiorow,.wcols,.wbox,.sem,.acthead,.chatline,.fichacard{ break-inside:avoid; }
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
/* horario tabel (routine profiel) */
.horario{ width:100%; font-size:9pt; } .horario td,.horario th{ border:1px solid var(--line); padding:1.6mm 3mm; } .horario th{ background:var(--gt); color:var(--gd); font-size:8pt; text-transform:uppercase; } .horario .hh{ font-family:var(--disp); font-weight:700; color:var(--gd); white-space:nowrap; }
"""

# ---------------- component-helpers ----------------
def qr(lab, meta, seed=0):
    import random; rnd = random.Random(seed)
    cells = "".join(f'<rect x="{18+ (i%4)*4}" y="{6+ (i//4)*5}" width="4" height="4"/>' for i in range(10) if rnd.random() > .4)
    extra = "".join(f'<rect x="{6+(i%3)*4}" y="{18+(i//3)*4}" width="4" height="4"/>' for i in range(6) if rnd.random() > .45)
    return (f'<div class="qr"><svg width="18mm" height="18mm" viewBox="0 0 40 40"><rect width="40" height="40" fill="#fff"/>'
            f'<g fill="#20242E"><rect x="3" y="3" width="10" height="10"/><rect x="27" y="3" width="10" height="10"/>'
            f'<rect x="3" y="27" width="10" height="10"/>{cells}{extra}</g></svg>'
            f'<div class="lab">{lab}</div><div class="meta">{meta}</div></div>')

def audiorow(call_html, qr_html):
    return f'<div class="audiorow"><div class="call">{call_html}</div>{qr_html}</div>'

def act(num, title, badges, body, steun=None):
    b = "".join(f'<span class="badge{" skill" if s.get("skill") else ""}">{s["t"]}</span>' for s in badges)
    s = "".join(x for x in [f'<div class="steun" style="margin-left:12.5mm">Apoyo: {steun}</div>' if steun else ""])
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

# ================= BODY =================
BODY = []
def P(*x): BODY.extend(x)

# ---------- OPENER ----------
P(f'''
<div class="hero">
  <div class="tab">U3 · EL TIEMPO VUELA</div>
  <div class="eyebrow">UNIDAD 3 · LA RUTA · PARADA 3 — BARCELONA 🇪🇸</div>
  <h1>El tiempo vuela</h1>
  <div class="sub">Llegamos a <b>Barcelona</b>. Hoy hablas de <b>la hora</b> y de <b>tu día</b>: te levantas, desayunas, empiezas las clases… <span class="gloss">We komen aan in Barcelona. Vandaag praat je over de klok en over je dag.</span></div>
  <div class="q">¿Qué hora es… y qué haces cada día? <span style="font-weight:400;opacity:.9">· Hoe laat is het… en wat doe je elke dag?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U1 · Madrid</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U2 · Sevilla</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U3 · Barcelona</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U4 · València</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U5–U8 · América</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 3 · Barcelona.</b> Lucía te presenta a su amigo <b>Pau</b>, un chico de Barcelona (habla catalán y español). Con él sigues su <b>rutina diaria</b> — la excusa perfecta para aprender <b>la hora</b> y el <b>presente</b>. <span class="gloss">Je volgt de dagindeling van Pau; zo leer je de klok en de tegenwoordige tijd.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> En <b>Barcelona</b> pasas un día con <b>Pau</b>. Él <b>se levanta</b> temprano, <b>desayuna</b>, va al instituto y por la tarde <b>juega</b> y <b>hace</b> los deberes. Aprendes a decir <b>qué hora es</b>, a contar tu <b>rutina</b> y a usar verbos que cambian de raíz (<i>empezar, poder, dormir…</i>).
      <span class="gloss">In Barcelona breng je een dag door met Pau. Je leert de tijd zeggen, je routine vertellen en werkwoorden met een stamwissel gebruiken.</span></div>
      <div class="ojo"><b>¡Ojo! — valstrik:</b> één uur = <b>Es la una</b> (enkelvoud); vanaf twee uur = <b>Son las</b> dos, tres… (meervoud). En het reflexief pronomen staat <b>vóór</b> het werkwoord: <b>me</b> levanto, niet <span class="trap">levanto me</span>.</div>
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
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila del tiempo</span><br><span class="gloss" style="font-size:8.5pt">In Barcelona vul je je rugzak met de klok, je dagritme en nieuwe werkwoorden.</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">decir la hora</span> (¿Qué hora es? · Son las dos y media) <span class="nl">de tijd/klok zeggen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">contar tu rutina</span> con verbos reflexivos <span class="nl">je dagroutine vertellen (me levanto…)</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar el presente irregular</span> (o→ue · e→ie · e→i) <span class="nl">werkwoorden met stamwissel</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">decir con qué frecuencia</span> haces cosas <span class="nl">siempre · a veces · nunca…</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">los días, meses y estaciones</span> <span class="nl">dagen, maanden & seizoenen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">crear tu <b>«Un día en mi vida»</b></span> <span class="nl">vlog/tekst over je dag (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>La hora</span><span><b>§2</b>Mi rutina</span><span><b>§3</b>Presente irreg.</span><span><b>§4</b>Frecuencia</span><span><b>§5</b>Lectura</span><span><b>Taller</b>Conectores</span><span><b>Cultura</b>El horario</span><span><b>Tarea</b>Mi día</span>
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
      <div class="ej" style="margin-top:2mm">📄 el libro · 🎮 la <b>página digital</b> (24 spellen, audio, flip cards) · 📊 el PowerPoint. De <b>QR</b>-codes brengen je naar de juiste online-oefening.</div>
      <div class="anchor gloss" style="margin-top:2mm">Print werkt <b>volledig zonder</b> scherm; het <b>repaso</b> staat online.</div></div>
  </div>
</div>
''')

# ---------- §0 Ponte al día ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">0</span><span class="pk">§0 · ¡Ponte al día!</span>')
P('<div class="intro"><b>ES:</b> Antes de empezar recordamos lo que necesitas hoy: los <b>números</b> (para la hora), el <b>presente regular</b> y los verbos <b>ser</b>/<b>tener</b>. <span class="gloss">Voor we starten: getallen (voor de klok), presente regular en ser/tener ophalen.</span></div>')
P(lpd(("7","woordenschat inzetten"), ("9","strategieën / lengua de clase"), ("8","taalsysteem ophalen")))
P('</div>')
P('<p style="font-size:9.6pt">① <b>¿Qué tienes ya en la mochila?</b> Drie clusters die je vandaag inzet. <span class="gloss">Wat zit er al in je rugzak?</span></p>')
P(clusters([
  ("🔢","Números 0–60",["cero · cinco · diez","quince · veinte · treinta","cuarenta · cincuenta"],"Voor de klok & de dagen."),
  ("🔤","Presente regular",["-ar: hablo, hablas…","-er: como, comes…","-ir: vivo, vives…"],"Werkwoorden vervoegen."),
  ("👤","Ser · tener",["yo soy · tú eres","yo tengo · tú tienes","edad = tener años"],"Wie je bent + leeftijd."),
]))
P(actx(1, "Los números que necesito para la hora",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Schrijf het getal voluit (recyclen U0).</p>'
  '<table class="mp"><thead><tr><th>Cifra</th><th>En letras</th><th>Cifra</th><th>En letras</th></tr></thead>'
  '<tbody><tr><td>12</td><td><span class="wl md"></span></td><td>15</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>30</td><td><span class="wl md"></span></td><td>45</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="MODELO → SIN AYUDA"))
P(actx(2, "Repasa el presente regular",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Vervoeg in het presente regular (uit U1).</p>'
  '<table class="mp"><thead><tr><th>Infinitivo</th><th>yo</th><th>tú</th><th>nosotros</th></tr></thead><tbody>'
  '<tr><td>hablar</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>comer</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>vivir</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>', apoyo="BANCO (tabel open)"))
P(actx(3, "¿ser o tener?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Vul <b>ser</b> of <b>tener</b> in (let op de leeftijd-valstrik uit U1).</p>'
  '<p style="margin-left:12.5mm">a) Yo <span class="wl sm"></span> de Bélgica. &nbsp; b) Pau <span class="wl sm"></span> 16 años. &nbsp; c) Nosotros <span class="wl sm"></span> estudiantes.</p>', apoyo="PISTA (edad = tener)"))
P(actx(4, "El día de la semana",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind de klaszin met zijn functie (schrijf de letter) — recyclen lengua de clase.</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th></th><th>Función</th></tr></thead><tbody>'
  '<tr><td>1 · ¿Qué hora es?</td><td><span class="wl sm"></span></td><td>A · om hoe laat?</td></tr>'
  '<tr><td>2 · ¿A qué hora empiezas?</td><td><span class="wl sm"></span></td><td>B · hoe laat is het?</td></tr>'
  '<tr><td>3 · Otra vez, por favor.</td><td><span class="wl sm"></span></td><td>C · nog eens a.u.b.</td></tr></tbody></table>', apoyo="BANCO"))
P(actx(5, "Calentamiento: cuenta tu horario",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Zeg aan je buur drie dingen die je <b>vandaag</b> doet met het presente regular (hablar, estudiar, comer…). Je buur telt ze.</p>'
  '<p style="margin-left:12.5mm">Mis tres cosas: <span class="wl full"></span></p>', apoyo="MODELO → SIN AYUDA"))
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> números, presente regular en ser/tener met zelfcorrectie op de digitale pagina.</div>')
P('</div>')  # close §0

# ================= §1 · LA HORA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">1</span><span class="pk">§1 · La hora — ¿Qué hora es?</span>')
P('<div class="route-note">📍 Parada 3 · Barcelona — Pau mira su reloj: es hora de empezar el día.</div>')
P('<div class="intro"><b>ES:</b> Primero <b>observas</b> cómo se dice la hora, después la <b>construyes</b> y la <b>usas</b> para hacer planes. <span class="gloss">Eerst kijk je hoe de klok werkt, dan bouw je ze en gebruik je ze.</span></div>')
P(lpd(("8","taalsysteem: la hora"), ("7","woordenschat: el reloj"), ("3","doelgericht schrijven"), ("4","mondelinge interactie")))
P('</div>')
# §1.1 observar de klok
P('<h3 style="margin-top:6mm">§1.1 · Es la una · Son las dos — observa</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto.</b> Mira los relojes de Pau. ¿Qué se repite? <span class="gloss">Bekijk de klokken; wat verandert, wat blijft?</span></p>')
P('<div class="clockrow">'
  + clockcard(1,0,"Es la una","1:00 · enkelvoud!")
  + clockcard(2,0,"Son las dos","2:00")
  + clockcard(3,0,"Son las tres","3:00")
  + clockcard(7,0,"Son las siete","7:00")
  + '</div>')
P(obsbox([
  '<span class="hl">Es la</span> una. — <span class="hl">Son las</span> dos. — <span class="hl">Son las</span> tres. — <span class="hl">Son las</span> siete.',
], vragen='<b>1)</b> Wanneer gebruik je <i>es la</i> en wanneer <i>son las</i>? <b>2)</b> Wat is het verschil met 1 uur?'))
P(regla("Regla · ¿Qué hora es?",
  '<p><b>Es la una</b> (enkelvoud, alléén bij 1 uur) · <b>Son las</b> + getal vanaf 2 uur. '
  '<br>🔴 <b>Valstrik:</b> nooit <span class="trap">son la una</span> of <span class="trap">es las dos</span>.</p>'))
P(actx(1, "Empareja el reloj con la hora",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Schrijf onder elke klok de juiste tijd.</p>'
  '<div class="clockrow">'
  + '<div class="clockcard">'+clock(4,0)+'<div class="nl"><span class="wl sm"></span></div></div>'
  + '<div class="clockcard">'+clock(1,0)+'<div class="nl"><span class="wl sm"></span></div></div>'
  + '<div class="clockcard">'+clock(9,0)+'<div class="nl"><span class="wl sm"></span></div></div>'
  + '<div class="clockcard">'+clock(6,0)+'<div class="nl"><span class="wl sm"></span></div></div>'
  + '</div>', apoyo="MODELO (Es la… / Son las…)"))
P(actx(2, "¿es la o son las?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>cloze klassiek.</i> Vul <b>Es la</b> of <b>Son las</b> aan.</p>'
  '<p style="margin-left:12.5mm">a) <span class="wl sm"></span> una. &nbsp; b) <span class="wl sm"></span> cinco. &nbsp; c) <span class="wl sm"></span> diez. &nbsp; d) <span class="wl sm"></span> doce. &nbsp; e) <span class="wl sm"></span> una y media.</p>', apoyo="PISTA (1 = es la)"))
P(actx(3, "Clasifica: singular o plural",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>sorteren.</i> Zet elke tijd bij «es la» (1 u) of «son las» (≥2 u). <span class="words"><b>la una · las tres · las ocho · la una y cuarto · las doce · las dos</b></span></p>'
  + sortcols([("Es la…","1 uur"),("Son las…","vanaf 2 uur")]), apoyo="BANCO"))
P('</div>')  # page §1.1
# §1.2 y media / cuarto / menos + ¿a qué hora?
P('<div class="page">')
P('<div class="divider">Los minutos + ¿A qué hora? · §1.2</div>')
P('<h3>§1.2 · … y media, y cuarto, menos cuarto</h3>')
P('<p style="font-size:9.6pt">① <b>Observa los minutos.</b> Mira cómo se añaden los minutos:</p>')
P('<div class="clockrow">'
  + clockcard(2,15,"Son las dos y cuarto","2:15 · +15")
  + clockcard(2,30,"Son las dos y media","2:30 · +30")
  + clockcard(2,45,"Son las tres menos cuarto","2:45 · −15")
  + clockcard(6,0,"Son las seis en punto","6:00 · precies")
  + '</div>')
P(machine([("hora","las dos"),("+ minutos",'<span class="end">y media</span>'),("resultado","las dos <span class=end>y media</span>")]))
P(regla("Regla · los minutos",
  '<p><b>hasta la media</b> → hora + <b>y</b> + minutos: <i>las dos <b>y</b> diez, <b>y</b> cuarto, <b>y</b> media</i>. '
  '<b>después de la media</b> → volgend uur + <b>menos</b>: <i>las tres <b>menos</b> cuarto</i>. · <b>en punto</b> = precies. '
  '<br>🟡 <b>Truc:</b> <i>y</i> = tot half; <i>menos</i> = na half (je «leent» van het volgende uur).</p>'))
P('<p style="font-size:9.6pt">② <b>¿A qué hora? — de la mañana/tarde/noche.</b> Om een concreet uur te noemen:</p>')
P(mirror([
  ('¿<span class="mk">A qué hora</span> te levantas?', 'A las siete <b>de la mañana</b>. <span class="gloss">(concreet uur → de la)</span>'),
  ('¿<span class="mk">A qué hora</span> comes?', 'A las dos <b>de la tarde</b>.'),
  ('¿<span class="mk">A qué hora</span> te acuestas?', 'A las once <b>de la noche</b>.'),
]))
P('<div class="truc"><b>🔴 de la vs. por la:</b> <b>de la</b> mañana/tarde/noche = bij een <b>concreet uur</b> (a las 7 <b>de la</b> mañana). <b>por la</b> mañana/tarde/noche = een <b>deel van de dag</b>, zonder uur (estudio <b>por la</b> tarde).</div>')
P(actx(4, "Escribe la hora completa",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>cue → volledige zin.</i> Schrijf de tijd voluit.</p>'
  '<table class="mp"><thead><tr><th>Reloj</th><th>La hora (frase completa)</th></tr></thead><tbody>'
  '<tr><td>3:30</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>9:15</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>7:45</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>1:00</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>10:00 (avond)</td><td><span class="wl lg"></span></td></tr></tbody></table>', apoyo="MARCO (y/media/menos) → SIN AYUDA"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha cinco horas y dibuja las manecillas.</b> <span class="gloss">Luister; teken de wijzers of noteer de tijd — selectief luisteren.</span></div>',
           qr("Escanea y escucha", "Audio 1.2 · La hora · 0:50", seed=131)))
P(actx(5, "Escucha y anota la hora",
  [{"t":"👂 Escuchar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>luisteren en noteren.</i> Schrijf de vijf tijden die je hoort.</p>'
  '<p style="margin-left:12.5mm">1) <span class="wl md"></span> 2) <span class="wl md"></span> 3) <span class="wl md"></span> 4) <span class="wl md"></span> 5) <span class="wl md"></span></p>', apoyo="PISTA (media/cuarto)"))
P(actx(6, "de la o por la",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>onderscheiden.</i> Kies <b>de la</b> (concreet uur) of <b>por la</b> (deel van de dag).</p>'
  '<p style="margin-left:12.5mm">a) Me levanto a las 7 ___ mañana. &nbsp; b) ___ tarde hago los deberes.<br>c) Ceno a las 9 ___ noche. &nbsp; d) ___ mañana voy al instituto.<br><span class="wl full"></span></p>', apoyo="PISTA (uur → de la)"))
P(tarea_com("Tarea comunicativa · ¿A qué hora…? — la agenda",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b>Afzender·ontvanger·doel·situatie·resultaat:</b> jij en je buur zijn in Barcelona en willen <b>afspreken</b>. Vraag naar elkaars uren en vind een gemeenschappelijk vrij moment. <span class="gloss">«¿A qué hora comes? ¿A qué hora sales del insti?»</span></p>'
  '<table class="wtab mp"><thead><tr><th>¿A qué hora…?</th><th>Yo</th><th>Mi compañero/a</th></tr></thead><tbody>'
  '<tr><td>…te levantas</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>…comes</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>…sales del instituto</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>'
  '<p style="margin-left:12.5mm">Nuestro momento libre común: <span class="wl md"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: MARCO (¿A qué hora…?) → SIN AYUDA · [CROSS: dia 8 · HTML «La hora»]</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «La hora» (reloj ↔ frase), «¿es la o son las?» en «escucha la hora».</div>')
P('</div>')  # page §1.2

# ================= §2 · MI RUTINA + REFLEXIVOS =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2 · Mi rutina — verbos reflexivos</span>')
P('<div class="intro"><b>ES:</b> Para contar tu día usas verbos <b>reflexivos</b> (una acción sobre ti mismo): <i>me levanto, me ducho, me visto…</i> La ruta: contexto → observar → patrón → regla → practicar → comunicar. <span class="gloss">Om je dag te vertellen gebruik je wederkerende werkwoorden.</span></div>')
P(lpd(("7","woordenschat: rutina diaria"), ("8","taalsysteem: verbos reflexivos"), ("3","je dag vertellen"), ("4","interactie")))
P('</div>')
# §2.1 vocab rutina
P('<h3 style="margin-top:6mm">§2.1 · Las acciones del día — el vocabulario</h3>')
P('<p style="font-size:9.6pt">① <b>La rutina de Pau, en orden.</b> Observa y adivina el significado. <span class="gloss">De dag van Pau op volgorde — raad de betekenis.</span></p>')
P('<div class="fichacard">'
  '<div><div class="row"><span class="k">7:00 · despertarse</span><span class="v">Pau se despierta <span class="nl">wakker worden</span></span></div>'
  '<div class="row"><span class="k">7:10 · levantarse</span><span class="v">se levanta <span class="nl">opstaan</span></span></div>'
  '<div class="row"><span class="k">7:20 · ducharse</span><span class="v">se ducha <span class="nl">douchen</span></span></div>'
  '<div class="row"><span class="k">7:40 · vestirse</span><span class="v">se viste <span class="nl">zich aankleden</span></span></div></div>'
  '<div><div class="row"><span class="k">8:00 · desayunar</span><span class="v">desayuna <span class="nl">ontbijten</span></span></div>'
  '<div class="row"><span class="k">14:30 · almorzar</span><span class="v">almuerza <span class="nl">lunchen</span></span></div>'
  '<div class="row"><span class="k">21:00 · cenar</span><span class="v">cena <span class="nl">avondmalen</span></span></div>'
  '<div class="row"><span class="k">23:00 · acostarse</span><span class="v">se acuesta <span class="nl">gaan slapen</span></span></div></div></div>')
P('<p style="font-size:9.6pt">② <b>Organiza en clusters</b> — het dagritme als netwerk, niet als lijst:</p>')
P(clusters([
  ("🌅","Por la mañana",["despertarse · levantarse","ducharse · lavarse","vestirse · peinarse"],"Het ochtendritueel."),
  ("🏫","Durante el día",["desayunar · almorzar","ir al instituto","hacer los deberes"],"School & eten."),
  ("🌙","Por la noche",["cenar · descansar","jugar · ver la tele","acostarse"],"Ontspannen & slapen."),
]))
P('<p style="font-size:9.6pt">③ <b>Colocaciones.</b> Welke tijd hoort bij welke actie? Leer ze <b>samen</b>:</p>')
P(colloc("¿Cuándo?", ["por la mañana → me levanto","al mediodía → almuerzo","por la tarde → los deberes","por la noche → me acuesto"]))
P(actx(1, "Ordena la rutina de Pau",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p><i>op volgorde zetten.</i> Nummer de acties in de logische volgorde (1–6).</p>'
  '<p style="margin-left:12.5mm">___ se acuesta &nbsp; ___ se levanta &nbsp; ___ desayuna &nbsp; ___ se despierta &nbsp; ___ cena &nbsp; ___ va al instituto</p>', apoyo="MODELO (de klok helpt)"))
P(actx(2, "Empareja acción ↔ dibujo",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p><i>woord-betekenis-koppeling.</i> Verbind de Spaanse actie met de vertaling (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Acción</th><th>Letra</th><th></th><th>NL</th></tr></thead><tbody>'
  '<tr><td>1 · ducharse</td><td><span class="wl sm"></span></td><td>A</td><td>gaan slapen</td></tr>'
  '<tr><td>2 · vestirse</td><td><span class="wl sm"></span></td><td>B</td><td>douchen</td></tr>'
  '<tr><td>3 · acostarse</td><td><span class="wl sm"></span></td><td>C</td><td>ontbijten</td></tr>'
  '<tr><td>4 · desayunar</td><td><span class="wl sm"></span></td><td>D</td><td>zich aankleden</td></tr></tbody></table>', apoyo="BANCO"))
P(actx(3, "Clasifica el momento del día",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>semantisch sorteren.</i> Zet elke actie onder het juiste dagdeel. <span class="words"><b>me levanto · almuerzo · me acuesto · desayuno · ceno · hago los deberes</b></span></p>'
  + sortcols([("Por la mañana",""),("Al mediodía / tarde",""),("Por la noche","")]), apoyo="BANCO → +1 eigen woord"))
P(mispal("Mis acciones del día", 3))
P('</div>')  # page §2.1
# §2.2 reflexivos mechanisme
P('<div class="page">')
P('<div class="divider">Los verbos reflexivos · §2.2</div>')
P('<h3>§2.2 · me · te · se — el pronombre reflexivo</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto (chat).</b> Observa el pronombre delante del verbo:</p>')
P('<div class="chat">'
  '<div class="chatline you"><div class="bub">¿A qué hora <b>te levantas</b>?</div><div class="who">Lucía</div></div>'
  '<div class="chatline me"><div class="bub"><span class="fx per">Yo</span> <span class="fx vb">me levanto</span> <span class="fx ti">a las siete</span> y <span class="fx vb">me ducho</span> enseguida.</div><div class="who">Tú</div></div>'
  '<div class="chatline you"><div class="bub">¿Y Pau? ¿A qué hora <b>se acuesta</b>?</div><div class="who">Lucía</div></div>'
  '<div class="chatline me"><div class="bub">Pau <span class="fx vb">se acuesta</span> <span class="fx ti">a las once</span>.</div><div class="who">Tú</div></div></div>')
P('<p style="font-size:9.6pt">② <b>El patrón — el pronombre cambia con la persona.</b></p>')
P('<table class="conj"><thead><tr><th>Persona</th><th>pronombre</th><th>levantarse</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">me</td><td>me levanto</td></tr>'
  '<tr><td class="p">tú</td><td class="v">te</td><td>te levantas</td></tr>'
  '<tr><td class="p">él / ella / usted</td><td class="v">se</td><td>se levanta</td></tr>'
  '<tr><td class="p">nosotros/-as</td><td class="v">nos</td><td>nos levantamos</td></tr>'
  '<tr><td class="p">vosotros/-as</td><td class="v">os</td><td>os levantáis</td></tr>'
  '<tr><td class="p">ellos/-as / ustedes</td><td class="v">se</td><td>se levantan</td></tr></tbody></table>')
P('<p style="font-size:9.6pt">③ <b>Como bloques.</b> Kies één blok per rij en bouw je zin:</p>')
P(blocks([
  [("per","Yo"),("vb","me"),("vb","levanto"),("ti","a las 7")],
  [("per","Tú"),("vb","te"),("vb","duchas"),("ti","por la mañana")],
  [("per","Pau"),("vb","se"),("vb","acuesta"),("ti","a las 11")],
]))
P(regla("Regla · verbos reflexivos",
  '<p>Reflexief werkwoord = <b>pronombre</b> (me/te/se/nos/os/se) + vervoegd werkwoord. Het pronomen staat <b>vóór</b> het werkwoord en <b>past bij de persoon</b>. '
  '<br>🔴 <b>Valstrik NL:</b> zeg <i><b>me</b> levanto</i>, niet <span class="trap">levanto me</span>. Het werkwoord zelf vervoeg je gewoon (levantar → levanto).</p>'))
P(actx(4, "Elige el pronombre",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p><i>cloze pronombre.</i> Vul me/te/se/nos in.</p>'
  '<p style="margin-left:12.5mm">a) Yo <span class="wl sm"></span> ducho. &nbsp; b) ¿Tú <span class="wl sm"></span> levantas pronto? &nbsp; c) Pau <span class="wl sm"></span> viste rápido.<br>d) Nosotros <span class="wl sm"></span> acostamos tarde. &nbsp; e) Lucía y Pau <span class="wl sm"></span> despiertan a las siete.</p>', apoyo="BANCO (me/te/se/nos)"))
P(actx(5, "Conjuga el verbo reflexivo (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p><i>cloze klassiek · werkwoordsvormen.</i> Vul het reflexief werkwoord <b>volledig</b> in (pronombre + vorm). Het infinitief staat tussen haakjes.</p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl md"></span> <i>(despertarse)</i> a las siete.<br>'
  '2. Pau <span class="wl md"></span> <i>(ducharse)</i> por la mañana.<br>'
  '3. ¿Tú <span class="wl md"></span> <i>(vestirse)</i> rápido?<br>'
  '4. Nosotros <span class="wl md"></span> <i>(levantarse)</i> temprano.<br>'
  '5. Mis amigos <span class="wl md"></span> <i>(acostarse)</i> a medianoche.</p>'
  '<p style="margin-left:12.5mm" class="gloss">[antwoord-laag online] 1 me despierto · 2 se ducha · 3 te vistes · 4 nos levantamos · 5 se acuestan</p>', apoyo="PISTA (pronombre gegeven) → SIN AYUDA"))
P(actx(6, "De Pau a mí — transforma",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p><i>transformatieketting.</i> Zet de zin van <b>Pau (se)</b> naar <b>jou (yo)</b>.</p>'
  '<p style="margin-left:12.5mm">Pau se levanta a las 7. → <span class="wl lg"></span><br>Pau se ducha y se viste. → <span class="wl lg"></span><br>Pau se acuesta a las 11. → <span class="wl lg"></span></p>', apoyo="MODELO → SIN AYUDA"))
P(tarea_com("Tarea comunicativa · Mi mañana",
  [{"t":"🎙️ Hablar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p>Vertel je buur je <b>ochtend</b> in de juiste volgorde met tijden en reflexieve werkwoorden. Je buur tekent jouw horario. <span class="gloss">«Me despierto a las 7, me levanto, me ducho…»</span></p>'
  '<div class="wbox sm"></div>'
  '<div class="steun" style="margin-left:0mm">Apoyo: MODELO (Pau) → SIN AYUDA · [CROSS: HTML «Carrusel: mi día» — grábate]</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «¿reflexivo o no?», «memoria de la rutina» en «ordena mi día».</div>')
P('</div>')  # page §2.2

# ================= §3 · PRESENTE IRREGULAR (cambio de raíz) =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3 · Presente irregular — cambio de raíz</span>')
P('<div class="intro"><b>ES:</b> Algunos verbos cambian la <b>raíz</b> en presente (¡pero no siempre!). Descúbrelo como una <b>máquina</b>: la vocal de la raíz cambia… menos en <i>nosotros/vosotros</i>. <span class="gloss">Sommige werkwoorden wijzigen hun stam — behalve bij nosotros/vosotros.</span></div>')
P(lpd(("8","taalsysteem: presente irregular"), ("3","vertellen over je dag"), ("9","strategie: patroon herkennen")))
P('</div>')
# §3.1 o→ue
P('<h3 style="margin-top:6mm">§3.1 · o → ue (poder, dormir, volver, acostarse)</h3>')
P('<p style="font-size:9.6pt">① <b>Observa la máquina.</b> Zo verandert de stam:</p>')
P(machine([("infinitivo","poder"),("raíz","pod-"),("o → ue",'<span class="end">pued-</span>'),("+ o","p<span class=end>ue</span>do")]))
P('<p style="font-size:9.6pt">② <b>El patrón — la vocal cambia… salvo nosotros/vosotros (zoom).</b></p>')
P('<div class="fams" style="margin-top:2mm"><div class="pcard"><div class="t" style="font-size:10pt">poder (o→ue)</div>'
  '<table class="conj"><tbody>'
  '<tr><td class="p">yo</td><td>p<span class="end">ue</span>do</td></tr>'
  '<tr><td class="p">tú</td><td>p<span class="end">ue</span>des</td></tr>'
  '<tr><td class="p">él/ella</td><td>p<span class="end">ue</span>de</td></tr>'
  '<tr><td class="p">nosotros</td><td>p<b>o</b>demos</td></tr>'
  '<tr><td class="p">vosotros</td><td>p<b>o</b>déis</td></tr>'
  '<tr><td class="p">ellos</td><td>p<span class="end">ue</span>den</td></tr></tbody></table></div>'
  '<div class="pcard"><div class="t" style="font-size:10pt">la zona que cambia</div>'
  + zoom("nosotros / vosotros","raíz normal: podemos","el resto","raíz fuerte: puedo")
  + '<div class="ej" style="margin-top:2mm">Zo ook: <b>dormir</b> → duermo · <b>volver</b> → vuelvo · <b>acostarse</b> → me ac<span class="end">ue</span>sto · <b>almorzar</b> → almuerzo · <b>jugar</b> → j<span class="end">ue</span>go (u→ue!).</div></div></div>')
P(regla("Regla · o → ue (la «bota»)",
  '<p>De klinker in de stam wordt <b>ue</b> in álle vormen <b>behalve</b> nosotros/vosotros (die houden de gewone stam). '
  '<br>🟡 Teken een <b>laars/bota</b> rond de vormen die veranderen: yo, tú, él, ellos. Nosotros/vosotros vallen erbuiten.</p>'))
P(actx(1, "¿cambia o no cambia?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>onderscheiden.</i> Sorteer de vormen: stamwissel (ue) of gewone stam?<span class="words"><b>podemos · puedo · dormís · duerme · volvemos · vuelven · juego · jugamos</b></span></p>'
  + sortcols([("Cambia → ue",""),("No cambia (nos./vos.)","")]), apoyo="BANCO"))
P(actx(2, "Conjuga o→ue",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>substitutietabel.</i> Vervoeg (let op nosotros!).</p>'
  '<table class="mp"><thead><tr><th>Infinitivo</th><th>yo</th><th>tú</th><th>nosotros</th><th>ellos</th></tr></thead><tbody>'
  '<tr><td>poder</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>dormir</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>volver</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>', apoyo="MODELO → PISTA"))
P('</div>')  # page §3.1
# §3.2 e→ie / e→i
P('<div class="page">')
P('<div class="divider">e → ie · e → i · §3.2</div>')
P('<h3>§3.2 · e → ie (querer, empezar, preferir, despertarse) · e → i (pedir, vestirse)</h3>')
P('<div class="fams" style="margin-top:2mm"><div class="pcard"><div class="t" style="font-size:10pt">empezar (e→ie)</div>'
  '<table class="conj"><tbody>'
  '<tr><td class="p">yo</td><td>emp<span class="end">ie</span>zo</td></tr>'
  '<tr><td class="p">tú</td><td>emp<span class="end">ie</span>zas</td></tr>'
  '<tr><td class="p">él/ella</td><td>emp<span class="end">ie</span>za</td></tr>'
  '<tr><td class="p">nosotros</td><td>emp<b>e</b>zamos</td></tr>'
  '<tr><td class="p">ellos</td><td>emp<span class="end">ie</span>zan</td></tr></tbody></table>'
  '<div class="ej" style="margin-top:1mm">Zo ook: querer → qu<span class="end">ie</span>ro · preferir → prefiero · despertarse → me despierto.</div></div>'
  '<div class="pcard"><div class="t" style="font-size:10pt">pedir (e→i)</div>'
  '<table class="conj"><tbody>'
  '<tr><td class="p">yo</td><td>p<span class="end">i</span>do</td></tr>'
  '<tr><td class="p">tú</td><td>p<span class="end">i</span>des</td></tr>'
  '<tr><td class="p">él/ella</td><td>p<span class="end">i</span>de</td></tr>'
  '<tr><td class="p">nosotros</td><td>p<b>e</b>dimos</td></tr>'
  '<tr><td class="p">ellos</td><td>p<span class="end">i</span>den</td></tr></tbody></table>'
  '<div class="ej" style="margin-top:1mm">Zo ook: vestirse → me visto · servir → sirvo · repetir → repito.</div></div></div>')
P(regla("Regla · e→ie / e→i",
  '<p>Zelfde «bota»: de <b>e</b> wordt <b>ie</b> (empezar → empiezo) of <b>i</b> (pedir → pido) — behalve bij <b>nosotros/vosotros</b>. '
  '<br>🟡 Ken je de <b>yo</b>-vorm, dan ken je bijna heel het rijtje (behalve nosotros/vosotros).</p>'))
P(actx(3, "Completa con el presente irregular (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p><i>cloze klassiek · werkwoordsvormen nagerekend.</i> Vul de <b>juiste vorm</b> in. Het infinitief staat tussen haakjes.</p>'
  '<p style="margin-left:12.5mm">1. Las clases <span class="wl md"></span> <i>(empezar)</i> a las nueve.<br>'
  '2. Yo <span class="wl md"></span> <i>(querer)</i> dormir más.<br>'
  '3. ¿Tú <span class="wl md"></span> <i>(preferir)</i> la mañana o la tarde?<br>'
  '4. Pau <span class="wl md"></span> <i>(pedir)</i> un café.<br>'
  '5. Nosotros <span class="wl md"></span> <i>(empezar)</i> a las ocho.<br>'
  '6. Yo <span class="wl md"></span> <i>(despertarse)</i> a las siete y <span class="wl md"></span> <i>(vestirse)</i> rápido.</p>'
  '<p style="margin-left:12.5mm" class="gloss">[antwoord-laag online] 1 empiezan · 2 quiero · 3 prefieres · 4 pide · 5 empezamos · 6 me despierto · me visto</p>', apoyo="PISTA (infinitief gegeven) → SIN AYUDA"))
P(actx(4, "Una cosa cambia",
  [{"t":"🔍 Analizar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>één verandering tegelijk.</i> Begin met <b>«Yo empiezo a las ocho.»</b> en pas telkens één ding aan.</p>'
  '<p style="margin-left:12.5mm">→ maak <b>nosotros</b>: <span class="wl lg"></span><br>→ maak <b>Pau</b>: <span class="wl lg"></span><br>→ verander werkwoord naar <b>querer</b> (yo): <span class="wl lg"></span></p>', apoyo="PISTA"))
P('</div>')  # page §3.2
# §3.3 hacer/ir/salir
P('<div class="page">')
P('<div class="divider">hacer · ir · salir · §3.3</div>')
P('<h3>§3.3 · hacer, ir, salir — solo el «yo» es especial</h3>')
P('<p style="font-size:9.6pt">① <b>Observa: la sorpresa está en el «yo».</b></p>')
P('<div class="fams three" style="margin-top:2mm">')
P(pcard("hacer (doen/maken)", '<table class="conj"><tbody>'
  '<tr><td class="p">yo</td><td class="v">ha<span class="end">go</span></td></tr>'
  '<tr><td class="p">tú</td><td>haces</td></tr><tr><td class="p">él/ella</td><td>hace</td></tr>'
  '<tr><td class="p">nosotros</td><td>hacemos</td></tr><tr><td class="p">ellos</td><td>hacen</td></tr></tbody></table>'))
P(pcard("ir (gaan)", '<table class="conj"><tbody>'
  '<tr><td class="p">yo</td><td class="v">v<span class="end">oy</span></td></tr>'
  '<tr><td class="p">tú</td><td>vas</td></tr><tr><td class="p">él/ella</td><td>va</td></tr>'
  '<tr><td class="p">nosotros</td><td>vamos</td></tr><tr><td class="p">ellos</td><td>van</td></tr></tbody></table>'))
P(pcard("salir (uitgaan)", '<table class="conj"><tbody>'
  '<tr><td class="p">yo</td><td class="v">sal<span class="end">go</span></td></tr>'
  '<tr><td class="p">tú</td><td>sales</td></tr><tr><td class="p">él/ella</td><td>sale</td></tr>'
  '<tr><td class="p">nosotros</td><td>salimos</td></tr><tr><td class="p">ellos</td><td>salen</td></tr></tbody></table>'))
P('</div>')
P('<div class="truc"><b>🟡 Truc:</b> <b>hago · salgo</b> krijgen een <b>-g-</b> in de yo-vorm; <b>ir</b> is helemaal apart: <b>voy, vas, va…</b> De rest is gewoon regelmatig.</div>')
P(actx(5, "Conjuga hacer / ir / salir",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>cloze.</i> Vul de juiste vorm in.</p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl md"></span> <i>(hacer)</i> los deberes por la tarde.<br>'
  '2. Pau <span class="wl md"></span> <i>(ir)</i> al instituto en metro.<br>'
  '3. Yo <span class="wl md"></span> <i>(salir)</i> de casa a las ocho.<br>'
  '4. Nosotros <span class="wl md"></span> <i>(ir)</i> al parque el domingo.<br>'
  '5. ¿Tú <span class="wl md"></span> <i>(hacer)</i> deporte?</p>'
  '<p style="margin-left:12.5mm" class="gloss">[antwoord-laag online] 1 hago · 2 va · 3 salgo · 4 vamos · 5 haces</p>', apoyo="PISTA → SIN AYUDA"))
P(audiorow('<div class="ic">🎧</div><div><b>Microdictado.</b> Escucha dos veces y escribe las frases sobre el día de Pau. <span class="gloss">1ª: betekenis · 2ª: schrijf.</span></div>',
           qr("Escanea y escucha", "Audio 3.3 · Microdictado · 0:45", seed=133)))
P(actx(6, "Microdictado con reconstrucción",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p><i>microdictogloss.</i> Reconstrueer de drie zinnen die je hoort en maak daarna één <b>eigen</b> variant over jouw dag.</p>'
  '<p style="margin-left:12.5mm">1) <span class="wl full"></span>2) <span class="wl full"></span>3) <span class="wl full"></span></p>'
  '<p style="margin-left:12.5mm">Mi variante: <span class="wl full"></span></p>', apoyo="eerste letter → SIN AYUDA"))
P(tarea_com("Tarea comunicativa · El día de Pau, en 4/3/2",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p>Vertel in <b>4/3/2</b>-ronden (telkens sneller, andere partner) een dag met <b>empezar · poder · hacer · ir · salir</b>. <span class="gloss">Afzender = jij · doel = de dag beschrijven · resultaat = vloeiender elke ronde.</span></p>'
  '<p style="margin-left:12.5mm">Mis notas: <span class="wl full"></span> ☐ 4 min ☐ 3 min ☐ 2 min</p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: notas → SIN AYUDA</div>'))
# resumen visueel van de drie patronen (vult de sectiepagina + spreiding)
P('<p style="font-size:9.6pt;margin-top:5mm"><b>Resumen visual · las tres botas.</b> Elk patroon in één machine — de raíz verandert, behalve nosotros/vosotros:</p>')
P(machine([("o → ue","dormir"),("raíz fuerte",'d<span class="end">ue</span>rm-'),("yo","d<span class=end>ue</span>rmo")]))
P(machine([("e → ie","querer"),("raíz fuerte",'qu<span class="end">ie</span>r-'),("yo","qu<span class=end>ie</span>ro")]))
P(machine([("e → i","pedir"),("raíz fuerte",'p<span class="end">i</span>d-'),("yo","p<span class=end>i</span>do")]))
P(actx(7, "¿ue, ie o i? — clasifica",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>patroon herkennen.</i> Zet elk werkwoord onder zijn cambio de raíz. <span class="words"><b>poder · empezar · pedir · dormir · querer · vestirse · volver · preferir</b></span></p>'
  + sortcols([("o → ue",""),("e → ie",""),("e → i","")]), apoyo="BANCO → +1 eigen werkwoord"))
P(mispal("Mis verbos con cambio de raíz", 2))
P('<div class="route-note">🔁 <b>Ojo — conjugador online:</b> alle vervoegingen (~1000 werkwoorden, nagerekend) staan in de aparte cursus-tool «Conjugador» — óók de stamwisselaars.</div>')
P('</div>')  # page §3.3

# ================= §4 · FRECUENCIA + DÍAS/MESES/ESTACIONES =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4 · Frecuencia + días, meses y estaciones</span>')
P('<div class="intro"><b>ES:</b> ¿Con qué frecuencia haces las cosas? Con <b>siempre, a veces, nunca…</b> y con los <b>días</b> y <b>meses</b> sitúas tu rutina en el tiempo. <span class="gloss">Hoe vaak? En op welke dag/maand — zo plaats je je routine in de tijd.</span></div>')
P(lpd(("7","woordenschat: frecuencia, tiempo"), ("8","taalsysteem: adverbios"), ("3","je gewoontes vertellen")))
P('</div>')
# §4.1 frecuencia
P('<h3 style="margin-top:6mm">§4.1 · Los adverbios de frecuencia</h3>')
P('<p style="font-size:9.6pt">① <b>Una escala — de siempre a nunca.</b></p>')
P(scale(["siempre 100%","normalmente","a menudo","a veces","casi nunca","nunca 0%"]))
P('<p style="font-size:9.6pt">② <b>¿Dónde van?</b> Meestal <b>vóór</b> het werkwoord (of vooraan de zin):</p>')
P(blocks([
  [("ti","Siempre"),("vb","desayuno"),("ti","a las ocho")],
  [("per","Yo"),("ti","a veces"),("vb","ceno"),("ti","tarde")],
  [("ti","Nunca"),("vb","llego"),("ob","tarde a clase")],
]))
P(regla("Regla · frecuencia",
  '<p><b>siempre · normalmente · a menudo · a veces · casi nunca · nunca</b>. Ze staan meestal <b>vóór</b> het werkwoord of <b>vooraan</b>. '
  '<br>🟡 <b>todos los días</b>, <b>una vez por semana</b>, <b>el fin de semana</b> zijn ook frequentie-uitdrukkingen.</p>'))
P(actx(1, "Ordena por frecuencia",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>op volgorde.</i> Nummer van <b>meest</b> (1) naar <b>minst</b> (5) vaak.</p>'
  '<p style="margin-left:12.5mm">___ a veces &nbsp; ___ siempre &nbsp; ___ nunca &nbsp; ___ a menudo &nbsp; ___ casi nunca</p>', apoyo="MODELO (de escala boven)"))
P(actx(2, "Escribe la verdad sobre ti",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>gestuurde productie.</i> Maak ware zinnen met een frequentiebijwoord.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl sm"></span> desayuno por la mañana.<br>'
  '2. <span class="wl sm"></span> hago los deberes.<br>'
  '3. <span class="wl sm"></span> me acuesto tarde.<br>'
  '4. <span class="wl sm"></span> juego con el móvil en clase.</p>', apoyo="BANCO → SIN AYUDA"))
P('</div>')  # page §4.1
# §4.2 días/meses/estaciones
P('<div class="page">')
P('<div class="divider">Días · meses · estaciones · §4.2</div>')
P('<h3>§4.2 · Los días, los meses y las estaciones</h3>')
P(clusters([
  ("📅","Los días",["lunes · martes","miércoles · jueves","viernes · sábado · domingo"],"Let op: kleine letter!"),
  ("🗓️","Los meses",["enero · febrero · marzo","abril · mayo · junio","… diciembre"],"Ook klein, geen hoofdletter."),
  ("🍂","Las estaciones",["primavera · verano","otoño · invierno","en verano / en invierno"],"De seizoenen."),
]))
P('<div class="truc"><b>🔴 Valstrik NL:</b> <b>días</b> en <b>meses</b> schrijf je met een <b>kleine letter</b> (lunes, enero) — anders dan landen/steden (Barcelona, España). «op maandag» = <b>el lunes</b>; «elke maandag» = <b>los lunes</b>.</div>')
P(actx(3, "¿día, mes o estación?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p><i>sorteren.</i> Zet elk woord in de juiste kolom. <span class="words"><b>martes · agosto · verano · domingo · marzo · invierno · viernes · julio</b></span></p>'
  + sortcols([("Día",""),("Mes",""),("Estación","")]), apoyo="BANCO"))
P(actx(4, "Completa con el tiempo",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>cloze met betekenis.</i> Vul een dag, maand of seizoen in (correcte kleine letter!).</p>'
  '<p style="margin-left:12.5mm">a) Hoy es <span class="wl sm"></span>, mañana es <span class="wl sm"></span>.<br>'
  'b) Mi cumpleaños es en <span class="wl sm"></span>.<br>'
  'c) En <span class="wl sm"></span> hace calor y vamos a la playa.<br>'
  'd) El <span class="wl sm"></span> no tengo clase.</p>', apoyo="PISTA (kleine letter)"))
P(tarea_com("Tarea comunicativa · Mi semana típica",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 7 min"},{"t":"★★★"}],
  '<p>Vertel je buur wat je op <b>drie verschillende dagen</b> doet, met frequentie en tijden. Je buur vult een mini-agenda in. <span class="gloss">«Los lunes siempre empiezo a las 8; el sábado juego al fútbol.»</span></p>'
  '<table class="wtab mp"><thead><tr><th>Día</th><th>¿Qué hace mi compañero/a?</th></tr></thead><tbody>'
  '<tr><td>lunes</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>miércoles</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>sábado</td><td><span class="wl lg"></span></td></tr></tbody></table>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: MARCO (frecuencia + hora) → SIN AYUDA</div>'))
P(actx(5, "Mi estación favorita",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>vrije productie klein.</i> Schrijf 2–3 zinnen: welk seizoen vind je leuk en wat doe je dan? Gebruik <b>en</b> + seizoen + een frequentiebijwoord.</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (En verano… siempre…) → SIN AYUDA"))
P(mispal("Mis días, meses y estaciones", 2))
P('<div class="route-note">🎮 <b>Juega online:</b> «frecuencia», «día vs. mes» en «señala la mañana».</div>')
P('</div>')  # page §4.2

# ================= §5 · LECTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">📖</span><span class="pk">§5 · Lectura — «El día de Pau»</span>')
P('<div class="intro"><b>ES:</b> Vas a leer el <b>horario</b> de un día de Pau en Barcelona. Primero <b>predices</b>, después lees con un <b>objetivo</b>. <span class="gloss">Je leest Pau\'s dagindeling: eerst voorspellen, dan lezen met een doel.</span></div>')
P(lpd(("1","onderwerp/hoofdgedachte bij lezen"), ("2","relevante info selecteren"), ("3","doelgericht schrijven met steun")))
P('</div>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> blog / horario</span><span class="tm"><b>De:</b> Pau</span><span class="tm"><b>Para:</b> su intercambio</span><span class="tm">🎯 conocer su rutina</span></div>')
P(actx(1, "Antes de leer: predice",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★☆☆"}],
  '<p><i>voorspellen vanuit vorm.</i> Bekijk alleen de titel en de klokjes. ¿Qué acciones esperas leer? Noteer er drie.</p>'
  '<p style="margin-left:12.5mm">Espero leer: <span class="wl full"></span></p>', apoyo="MODELO (levantarse, comer…)"))
P('<div class="ptext"><div class="ph"><div class="av">'+AV["diego"]+'</div><div><div class="nm">El blog de Pau</div><div class="fr">Barcelona · un día normal</div></div></div>'
  '<p>¡Hola! Soy Pau, de Barcelona. Os cuento mi día. <span class="evi">Me despierto a las siete</span> y me levanto enseguida. '
  '<span class="evi">Me ducho, me visto</span> y desayuno un bocadillo. <span class="evi">Salgo de casa a las ocho</span> y voy al instituto en metro. '
  'Las clases <span class="evi">empiezan a las nueve</span>. Al mediodía <span class="evi">almuerzo en el instituto</span> con mis amigos. '
  'Por la tarde <span class="evi">hago los deberes</span> y, a menudo, <span class="evi">juego al fútbol</span>. '
  'Ceno con mi familia a las nueve y <span class="evi">me acuesto a las once</span>. Los sábados duermo más: ¡me levanto a las diez! ¿Y tú, a qué hora te levantas?</p></div>')
P('<div class="lecdoel">🎯 <b>Objetivo de lectura:</b> lees om te ontdekken <b>op welk uur</b> Pau de dingen doet en <b>wat hij ‘s middags/‘s avonds</b> doet — je hoeft niet élk woord te begrijpen.</div>')
P('</div>')  # page §5a
P('<div class="page">')
P(actx(2, "Escanea: completa el horario",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>scannen → informatieraster.</i> Zoek de uren in de tekst en vul Pau\'s horario aan.</p>'
  '<table class="horario"><thead><tr><th>Hora</th><th>¿Qué hace Pau?</th></tr></thead><tbody>'
  '<tr><td class="hh"><span class="wl sm"></span></td><td>se despierta</td></tr>'
  '<tr><td class="hh"><span class="wl sm"></span></td><td>sale de casa</td></tr>'
  '<tr><td class="hh"><span class="wl sm"></span></td><td>empiezan las clases</td></tr>'
  '<tr><td class="hh">al mediodía</td><td><span class="wl md"></span></td></tr>'
  '<tr><td class="hh"><span class="wl sm"></span></td><td>se acuesta</td></tr></tbody></table>', apoyo="MODELO (evidence gemarkeerd)"))
P(actx(3, "¿Verdadero o falso? + prueba",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>juist/fout + bewijs.</i> Waar of niet waar? Noteer de <b>woorden uit de tekst</b> die het bewijzen.</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba (palabras del texto)</th></tr></thead><tbody>'
  '<tr><td>Pau va al instituto en coche.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Las clases empiezan a las nueve.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Por la tarde juega al fútbol.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Los sábados se levanta temprano.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="PISTA (onderstreep in de tekst)"))
P(actx(4, "Del contexto: ¿qué significa?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>betekenis uit context.</i> Wat betekent <b>«enseguida»</b> en <b>«al mediodía»</b>? Kies + leg uit welke aanwijzing hielp.</p>'
  '<p style="margin-left:12.5mm">enseguida = ☐ meteen ☐ later &nbsp;·&nbsp; al mediodía = ☐ \'s middags (12u) ☐ \'s nachts<br>Pista que me ayudó: <span class="wl lg"></span></p>', apoyo="PISTA"))
P(tarea_com("Tarea comunicativa · Responde a Pau",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b>Keten lezen → schrijven → spreken.</b> Schrijf Pau een <b>antwoordbericht</b> over jouw dag (afzender = jij · ontvanger = Pau · doel = je routine delen). Gebruik uren + reflexieve/onregelmatige werkwoorden. Lees het daarna hardop voor.</p>'
  '<div class="wbox"></div>'
  '<div class="steun" style="margin-left:0mm">Apoyo: MARCO (Me levanto a las… / empiezo… / por la tarde…) → SIN AYUDA · [CROSS: HTML «Mensaje de voz»]</div>'))
P('<div class="route-note">🎮 <b>Sigue online:</b> op de digitale pagina beluister je «El día de Pau» (audio) en neem je je antwoord op (recorder).</div>')
P('</div>')  # page §5b

# ================= TALLER DE LENGUA =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num" style="color:var(--crema)">✎</span><span class="pk" style="background:var(--gd)">Taller de lengua</span>')
P('<div class="intro"><b>ES:</b> Dos herramientas para contar tu día en orden: los <b>conectores temporales</b> (primero, después…) y la <b>ortografía del tiempo</b>. <span class="gloss">Twee schrijfgereedschappen: tijdsvolgorde-woorden + spelling.</span></div>')
P(lpd(("8","taalsysteem: conectoren + ortografía"), ("3","samenhangend schrijven")))
P('</div>')
P('<h3 style="margin-top:6mm">Conectores temporales · primero · después · luego · por fin</h3>')
P('<table class="mp"><thead><tr><th>Conector</th><th>Uso</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td><b>primero</b></td><td>eerst</td><td><b>Primero</b> me levanto.</td></tr>'
  '<tr><td><b>después / luego</b></td><td>daarna / vervolgens</td><td><b>Después</b> desayuno.</td></tr>'
  '<tr><td><b>más tarde</b></td><td>later</td><td><b>Más tarde</b> hago los deberes.</td></tr>'
  '<tr><td><b>por fin / finalmente</b></td><td>ten slotte</td><td><b>Por fin</b> me acuesto.</td></tr></tbody></table>')
P('<div class="truc"><b>🔴 Valstrik NL:</b> «dan/vervolgens» = <b>después / luego</b>, niet <i>entonces</i> (dat is «in dat geval»). Recyclen U1: «want/omdat» = <b>porque</b>.</div>')
P(actx(1, "Ordena el día con conectores",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>gap-fill met betekenis.</i> Vul een conector temporal in (primero/después/luego/por fin).</p>'
  '<p style="margin-left:12.5mm"><span class="wl sm"></span> me despierto. <span class="wl sm"></span> me ducho. <span class="wl sm"></span> desayuno. <span class="wl sm"></span> voy al instituto.<br><span class="wl full"></span></p>', apoyo="BANCO"))
P('<h3 style="margin-top:6mm">Ortografía · la tilde y la hora</h3>')
P('<p style="font-size:9.6pt">① <b>Contraste visual</b> — deze tijdwoorden dragen een tilde:</p>')
P(vpairs([("miércoles","sábado"),("¿qué hora?","el número"),("después","por qué"),("mediodía","estación")]))
P(regla("Regla · la tilde", '<p>Veel tijd-/klokwoorden dragen een <b>tilde</b>: <i>miércoles, sábado, después, mediodía, estación</i>. En de <b>vraagwoorden</b> altijd: <i>¿qué?, ¿a qué hora?</i>. 🟡 De tilde staat op de <b>sterke lettergreep</b>.</p>'))
P(actx(2, "Pon las tildes que faltan",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>foutenkliniek.</i> Herschrijf met de correcte tilde(s).</p>'
  '<p style="margin-left:12.5mm">1) <span class="trap">el miercoles hago deporte</span> → <span class="wl lg"></span><br>'
  '2) <span class="trap">¿que hora es? son las tres y media</span> → <span class="wl lg"></span><br>'
  '3) <span class="trap">despues del mediodia almuerzo</span> → <span class="wl lg"></span></p>', apoyo="MODELO → SIN AYUDA"))
P(actx(3, "Puntúa y conecta",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>ortografía toepassen.</i> Herschrijf met hoofdletters, tildes én een conector.</p>'
  '<p style="margin-left:12.5mm">1) pau se levanta a las siete se ducha desayuna → <span class="wl full"></span>'
  '2) primero voy al insti luego hago los deberes → <span class="wl full"></span></p>', apoyo="MODELO → SIN AYUDA"))
P(actx(4, "Escribe tu mini-rutina con conectores",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>vrije productie.</i> Schrijf 4 zinnen over je ochtend met <b>primero · después · luego · por fin</b> en correcte tildes.</p>'
  '<div class="wbox sm"></div>', apoyo="SIN AYUDA"))
P('<div class="route-note">🎮 <b>Practica online:</b> «caza del reflexivo» en de conectoren-/tilde-oefeningen met zelfcorrectie.</div>')
P('</div>')  # page Taller

# ================= CULTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">★</span><span class="pk">Cultura · El horario español</span>')
P('<div class="intro"><b>ES:</b> En España se come y se cena <b>más tarde</b> que en Bélgica, y la famosa <b>siesta</b> es más mito que realidad. <span class="gloss">In Spanje eet men later dan in België; de siësta is meer mythe dan realiteit.</span></div>')
P(lpd(("5","kenmerkende aspecten van de cultuur"), ("2","relevante info uit een tekst")))
P('</div>')
P('<div class="fams" style="margin-top:6mm">')
P(pcard("Las comidas 🍽️", '<div class="ej"><b>desayuno</b> (~8 u, licht) · <b>almuerzo/comida</b> (~14–15 u, de hoofdmaaltijd!) · <b>merienda</b> (~18 u) · <b>cena</b> (~21–22 u).</div><div class="anchor gloss">In België eet men rond 12 u en 18 u — een paar uur vroeger.</div>'))
P(pcard("El instituto 🏫", '<div class="ej">Veel scholen: van ~<b>8:30</b> tot ~<b>14:30</b>, soms met een pauze. \'s Middags: deberes, deporte, amigos.</div><div class="t2">Andere ritme dan een lange schooldag met middagpauze.</div>'))
P('</div>')
P('<p style="font-size:9.6pt">① <b>La siesta — ¿mito o realidad?</b></p>')
P(vpairs([("Mito: todos duermen la siesta","Realidad: pocos, sobre todo mayores"),("comida = 14–15 h","cena = 21–22 h"),("tiendas cierran al mediodía","abren hasta tarde"),("España: cena tarde","Bélgica: cena ~18 h")]))
P('<div class="truc"><b>🟡 ¿Y tú?</b> Compara: ¿a qué hora comes y cenas <b>tú</b> en Bélgica? La hora dice mucho de una cultura.</div>')
P(actx(1, "Comprensión — verdadero o falso",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p><i>juist/fout + verbeteren.</i> Waar of niet waar? Verbeter de foute.</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Corrección</th></tr></thead><tbody>'
  '<tr><td>En España se cena a las seis.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>La comida principal es al mediodía.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Todos los españoles duermen la siesta.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="MODELO (tekst boven)"))
P(actx(2, "Compara España ↔ Bélgica",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p>Vul de vergelijking in en zeg hardop wat anders is. <span class="gloss">bemiddelen: cultuur uitleggen.</span></p>'
  '<table class="wtab mp"><thead><tr><th>¿A qué hora…?</th><th>España</th><th>Bélgica (tú)</th></tr></thead><tbody>'
  '<tr><td>se almuerza / comida</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>se cena</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>'
  '<p style="margin-left:12.5mm">La diferencia más grande: <span class="wl full"></span></p>', apoyo="PISTA → SIN AYUDA"))
P('<div class="truc"><b>🟡 Curiosidad:</b> el reloj de la <b>Puerta del Sol</b> en Madrid marca las <b>12 campanadas</b> de Nochevieja; con cada una se come <b>una uva</b> (¡doce uvas de la suerte!). El tiempo también es fiesta.</div>')
P(actx(3, "Tu horario ideal — mini-proyecto",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>transfer cultureel.</i> Si vivieras en España: ¿a qué hora comerías y cenarías? Schrijf jouw «Spaanse» dagritme (3 tijden) en vergelijk het met nu.</p>'
  '<p style="margin-left:12.5mm">Desayuno: <span class="wl sm"></span> · Comida: <span class="wl sm"></span> · Cena: <span class="wl sm"></span></p>'
  '<p style="margin-left:12.5mm">¿Te gusta más el horario español o el belga? <span class="wl full"></span></p>', apoyo="PISTA → SIN AYUDA"))
P(mispal("Mi mochila cultural — el tiempo en España", 2))
P('</div>')  # page Cultura

# ================= TAREA FINAL =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num">✦</span><span class="pk" style="background:var(--gd)">Tarea final · Un día en mi vida</span>')
P('<div class="intro"><b>ES:</b> Crea tu <b>«Un día en mi vida»</b>: un vlog o un texto con horario sobre un día tuyo. <span class="gloss">Maak je «een dag uit mijn leven»: vlog of tekst met dagindeling.</span></div>')
P('<div class="route-note">🎯 <b>Communicatieve taak:</b> afzender = jij · ontvanger = de klas/Lucía · doel = je dag vertellen · situatie = een dag meelopen in Barcelona · resultaat = horario + vlog/tekst + gesproken presentatie.</div>')
P(lpd(("3","doelgericht schrijven met een voorbeeld"), ("4","zich mondeling voorstellen"), ("7","woordenschat: hora/rutina"), ("8","reflexivos + presente irregular")))
P('</div>')
P('<ol class="pasos">'
  '<li><b>Haz tu horario.</b> Vul de tabel hieronder in met de uren van jouw dag.</li>'
  '<li><b>Escribe tu día</b> (6–8 frases) met uren, reflexieve werkwoorden én conectores (primero, después…).</li>'
  '<li><b>Di con qué frecuencia</b> haces algo (siempre, a veces, nunca).</li>'
  '<li><b>Preséntalo</b> a la clase (of neem een vlog/audio op via de digitale pagina).</li>'
  '<li><b>Pregunta</b> a un compañero por su día y presenta a esa persona en 3ª persona.</li></ol>')
P('<table class="horario"><thead><tr><th>Hora</th><th>Acción</th><th>Hora</th><th>Acción</th></tr></thead><tbody>'
  '<tr><td class="hh"><span class="wl sm"></span></td><td>me despierto / me levanto</td><td class="hh"><span class="wl sm"></span></td><td>almuerzo</td></tr>'
  '<tr><td class="hh"><span class="wl sm"></span></td><td>me ducho / me visto</td><td class="hh"><span class="wl sm"></span></td><td>hago los deberes</td></tr>'
  '<tr><td class="hh"><span class="wl sm"></span></td><td>desayuno / salgo de casa</td><td class="hh"><span class="wl sm"></span></td><td>ceno</td></tr>'
  '<tr><td class="hh"><span class="wl sm"></span></td><td>empiezan las clases</td><td class="hh"><span class="wl sm"></span></td><td>me acuesto</td></tr></tbody></table>')
P('<div class="se" style="margin-top:5mm">Un día en mi vida <span class="gloss" style="font-size:8pt">· 6–8 frases: hora + reflexivos + presente irregular + conectores</span></div><div class="wbox"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba tu vlog «Un día en mi vida»</b> en la página digital (recorder + rúbrica).</div>',
           qr("Escanea y graba", "Tarea · Un día en mi vida", seed=141)))
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Ik gebruik <b>la hora</b> correct (es la / son las)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>verbos reflexivos</b> (me/te/se) juist</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>presente irregular</b> (empiezo, puedo, hago…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik verbind met <b>conectores</b> en gebruik <b>frecuencia</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>presenteer</b> mijn dag mondeling en versta een klasgenoot</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="se" style="margin-top:5mm">Paso 5 · Presenta el día de un compañero/a <span class="gloss" style="font-size:8pt">— interview + presenteer in de 3e persoon</span></div>')
P('<table class="wtab mp"><thead><tr><th>¿A qué hora se levanta?</th><th>¿Qué hace por la tarde?</th><th>¿Con qué frecuencia?</th></tr></thead><tbody>'
  '<tr><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>'
  '<p style="margin-left:0mm">Mi presentación (3ª persona): <span class="wl full"></span></p>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — el día de mi compañero/a</div>'
  '<table><thead><tr><th>Lo que está muy bien</th><th>Un consejo (una cosa)</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('</div>')  # page Tarea

# ================= REPASO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">✓</span><span class="pk">Repaso · lo esencial</span>')
P('<div class="intro"><b>ES:</b> Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, 24 juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag.</span></div>')
P('</div>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>La hora:</b> Es la una · Son las dos… · y cuarto/media · menos cuarto · en punto · ¿A qué hora? a las…</li>'
  '<li><b>Reflexivos:</b> me/te/se/nos/os/se + verbo (me levanto, se acuesta). Pronombre <b>vóór</b> het werkwoord.</li>'
  '<li><b>Presente irregular:</b> o→ue (puedo, duermo), e→ie (empiezo, quiero), e→i (pido) · hago · voy · salgo. NIET bij nosotros/vosotros.</li>'
  '<li><b>Frecuencia:</b> siempre · normalmente · a menudo · a veces · casi nunca · nunca.</li>'
  '<li><b>Las trampas:</b> 🔴 Es la una / Son las… · 🔴 me levanto (niet levanto me) · 🔴 podemos (geen ue) · 🔴 días/meses klein.</li></ul></div>')
P(guide("Repasa jugando (online):", "— 24 spelletjes met zelfcorrectie en spreiding op de digitale pagina.", "🎮"))
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td>de <b>hora</b> zeggen en vragen</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>mijn <b>rutina</b> vertellen met reflexieve werkwoorden</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>het <b>presente irregular</b> (o→ue, e→ie, e→i) gebruiken</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>zeggen met welke <b>frecuencia</b> ik iets doe</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>de <b>días, meses en estaciones</b> herkennen</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil de U3: <span class="wl md"></span> · Lo más difícil: <span class="wl md"></span></i></div>')
P('<div class="bridge"><b>» Siguiente parada: València / la costa (U4).</b> Ya sabes contar tu día; en <b>U4 «Me gusta»</b> hablas de tus <b>gustos</b> y aficiones (me gusta / me encanta) en creas tu playlist. <span class="gloss">In U4 vertel je wat je leuk vindt aan de kust.</span></div>')
P('</div>')  # page Repaso

# ================= §V VOCABULARIO =================
import json
VOC = json.load(open(f"{HERE}/u3_vocab.json", encoding="utf-8"))
GRP = [("hora","La hora / el reloj"),("rutina","La rutina diaria (verbos reflexivos)"),
       ("verbos","Verbos irregulares (cambio de raíz)"),("frecuencia","Adverbios de frecuencia"),
       ("tiempo","Días, meses y estaciones")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (receptief & productief)")))
P('</div>')
P('<p style="font-size:9.6pt">Het thema <b>«el día a día»</b> als netwerk — van de klok tot het seizoen:</p>')
P(clusters([
  ("🕐","El reloj",["¿Qué hora es?","y media · y cuarto","de la mañana/tarde/noche"],"De tijd zeggen."),
  ("🔁","La rutina",["me levanto · me ducho","desayuno · almuerzo · ceno","me acuesto"],"Je dag beschrijven."),
  ("📆","El tiempo",["lunes … domingo","enero … diciembre","primavera · verano · otoño · invierno"],"Wanneer?"),
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
  '<p>Schrijf de vertaling. en punto = <span class="wl md"></span> · levantarse = <span class="wl md"></span> · a veces = <span class="wl md"></span> · el jueves = <span class="wl md"></span></p>', apoyo="MODELO"))
P(actx("V.2", "Distinguir — sorteer per thema",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Sorteer: <span class="words"><b>y media · ducharse · siempre · agosto · empezar · el reloj</b></span></p>'
  + sortcols([("la hora",""),("rutina/verbo",""),("frecuencia/tiempo","")], eigen=False), apoyo="BANCO"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het Spaanse woord aan (beginletter gegeven). opstaan = <b>l</b>___ · slapen = <b>d</b>___ · altijd = <b>s</b>___ · de zomer = <b>v</b>___<br><span class="wl full"></span></p>', apoyo="LETRA INICIAL"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p><i>verplichte-woorden-zin.</i> Maak één correcte zin met <b>hora · levantarse · frecuencia</b>.</p><div class="wbox sm"></div>', apoyo="SIN AYUDA"))
P(actx("V.5", "Comunicar — mi rutina en tres pasos",
  [{"t":"🎙️ Hablar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>vrije productie · spreiding.</i> Combineer een tijd, een reflexief werkwoord én een frequentiebijwoord in drie zinnen over jouw dag. Zeg ze daarna hardop.</p>'
  '<p style="margin-left:12.5mm">1) <span class="wl full"></span>2) <span class="wl full"></span>3) <span class="wl full"></span></p>', apoyo="SIN AYUDA"))
P(mispal("Mis palabras de la unidad", 5))
P('<p style="font-size:9.6pt;margin-top:4mm"><b>Tu red de palabras.</b> Kies uit elk cluster twee woorden en verbind ze in één zin over jouw dag — zo blijft de woordenschat plakken:</p>')
P(vpairs([("la hora ↔ una acción","Son las 8 y desayuno."),("un día ↔ una frecuencia","El sábado casi nunca…"),("un reflexivo ↔ una hora","Me acuesto a las 11."),("un verbo irregular ↔ un momento","Por la tarde juego.")]))
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Sigue en la página digital:</span> <span class="g">flip cards (ES↔NL), audio en de 24 spellen bouwen de steun verder af.</span></div></div>')
P('<div class="bridge"><b>» ¡Hasta la próxima parada!</b> Con la hora, tu rutina y el presente irregular ya puedes contar tu día. En <b>U4 «Me gusta»</b> viajas a <b>València</b> y hablas de tus gustos. <span class="gloss">Je kan nu je dag vertellen — op naar València!</span></div>')
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
   a.href=URL.createObjectURL(blob); a.download='U3_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Español en la práctica · U3 El tiempo vuela</title><style>'
        + CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/U3.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes")
