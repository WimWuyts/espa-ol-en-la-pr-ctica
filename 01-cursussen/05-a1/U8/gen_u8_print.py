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

# ================= BODY (U8 «¿Qué has hecho?» · parada Perú/Cusco · gastvrouw Nina) =================
BODY = []
def P(*x): BODY.extend(x)

# ---------- OPENER ----------
P(f'''
<div class="hero">
  <div class="tab">U8 · ¿QUÉ HAS HECHO?</div>
  <div class="eyebrow">UNIDAD 8 · LA RUTA · PARADA 8 — PERÚ / CUSCO · MACHU PICCHU 🇵🇪</div>
  <h1>¿Qué has hecho?</h1>
  <div class="sub">Última parada del viaje: <b>Perú</b>. Subimos a los <b>Andes</b>, a <b>Cusco</b> y a <b>Machu Picchu</b>. Hoy vertel je <b>wat je (net) gedaan hebt</b> en praat je over <b>el tiempo</b>. <span class="gloss">Laatste halte van de reis: Peru. Vandaag: vertellen wat je gedaan hebt (perfecto compuesto) en over het weer praten.</span></div>
  <div class="q">¿Qué has hecho este año? <span style="font-weight:400;opacity:.9">· Wat heb je dit jaar gedaan?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde estamos?</div>
  <div class="rutastrip">
    <div class="stop done"><div class="dot"></div><div class="lbl">U4 · València</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U5 · México</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U6 · Mercados</div></div>
    <div class="stop done"><div class="dot"></div><div class="lbl">U7 · Colombia</div></div>
    <div class="stop on"><div class="dot"></div><div class="lbl">U8 · Perú</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">C6 · sigue el viaje</div></div>
  </div>
  <div class="route-note">📍 <b>Parada 8 · Cusco · Machu Picchu (Perú).</b> Aquí <b>Nina</b> te lleva a los <b>Andes</b>. Aprendes a decir <b>qué has hecho</b> (pretérito perfecto compuesto), los <b>participios</b> y a hablar del <b>tiempo</b>. <span class="gloss">Nina neemt je mee de Andes in; je leert vertellen wat je gedaan hebt en over het weer praten.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> En <b>Cusco</b>, a 3400 metros, <b>Nina</b> te enseña su diario: «¡Mira todo lo que <b>he hecho</b>!». <b>Ha subido</b> a Machu Picchu, <b>ha visto</b> las llamas y <b>ha sacado</b> muchas fotos. «¿Y tú? ¿<b>Qué has hecho</b> este año?». Aprendes a contar tus <b>experiencias</b> y a decir qué <b>tiempo hace</b>.
      <span class="gloss">In Cusco, op 3400 m, toont Nina haar dagboek. Ze is naar Machu Picchu geklommen, heeft lama's gezien en veel foto's gemaakt. En jij? Wat heb jij dit jaar gedaan?</span></div>
      <div class="ojo"><b>¡Ojo! — de valstrik van vandaag:</b> «heb je gedaan?» = <b>has hecho</b> (haber + participio), <b>niet</b> <span class="trap">tienes hecho</span>. Het hulpwerkwoord is <b>haber</b> (he, has, ha…), nooit <i>tener</i>. En de participio verandert hier <b>niet</b>: <i>María ha comid<span class="trap">o</span></i> (niet comida).</div>
    </div>
    <div>
      <div class="se">La gente de la ruta</div>
      <div class="cast">
        <div class="pc"><div class="avw">{AV["nina"]}</div><div class="nm">Nina</div><div class="fr">Cusco 🇵🇪 · anfitriona</div></div>
        <div class="pc"><div class="avw">{AV["lucia"]}</div><div class="nm">Lucía</div><div class="fr">Sevilla 🇪🇸</div></div>
        <div class="pc"><div class="avw">{AV["diego"]}</div><div class="nm">Diego</div><div class="fr">CDMX 🇲🇽</div></div>
        <div class="pc"><div class="avw">{AV["valen"]}</div><div class="nm">Valen</div><div class="fr">Cartagena 🇨🇴</div></div>
        <div class="pc tu"><div class="avw">{TU}</div><div class="nm">Tú</div><div class="fr">Flandes 🇧🇪</div></div>
      </div>
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila de viajes</span><br><span class="gloss" style="font-size:8.5pt">In de Andes vul je je rugzak met de woorden van reizen & weer: el viaje, la maleta, ha llovido, hace frío, ¿qué has hecho?</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">contar qué has hecho</span> con el <b>pretérito perfecto compuesto</b> <span class="nl">vertellen wat je gedaan hebt</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">formar participios</span> (-ado/-ido + hecho, visto, dicho…) <span class="nl">deelwoorden vormen (ook onregelmatig)</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar marcadores</span> (ya · todavía no · hoy · alguna vez · nunca) <span class="nl">tijdmarkeerders gebruiken</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">hablar del tiempo</span> (hace sol/frío/calor · llueve · nieva) <span class="nl">over het weer praten</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">nombrar viajes y transporte</span> (el avión, el tren, la maleta) <span class="nl">reizen & vervoer benoemen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">escribir <b>«Mis vacaciones»</b></span> (reisverslag) <span class="nl">je reisverslag schrijven (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§0</b>Ponte al día</span><span><b>§1</b>He hecho…</span><span><b>§2</b>Participios</span><span><b>§3</b>Marcadores</span><span><b>§4</b>¿Qué tiempo hace?</span><span><b>§5</b>Lectura</span><span><b>Taller</b>Tilde diacrítica</span><span><b>Cultura</b>Machu Picchu</span><span><b>Tarea</b>Mis vacaciones</span><span><b>Repaso</b>Semáforo</span>
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
      <div class="ej" style="margin-top:2mm">📄 el libro · 🎮 la <b>página digital</b> (13 spellen, audio, flip cards) · 📊 el PowerPoint. De <b>QR</b>-codes brengen je naar de juiste online-oefening.</div>
      <div class="anchor gloss" style="margin-top:2mm">Print werkt <b>volledig zonder</b> scherm; het <b>repaso</b> staat online.</div></div>
  </div>
</div>
''')

# ---------- §0 Ponte al día ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">0</span><span class="pk">§0 · ¡Ponte al día!</span>')
P('<div class="intro"><b>ES:</b> Antes de contar tu viaje, recordamos lo que necesitas: el <b>presente</b> (para construir <b>haber</b>), los <b>participios</b> que ya conoces y las <b>actividades</b> de siempre. <span class="gloss">Voor je je reis vertelt: kort ophalen — presente, gekende deelwoorden en dagelijkse activiteiten.</span></div>')
P(lpd(("7","woordenschat inzetten"), ("8","presente ophalen (basis voor haber)"), ("9","strategieën / lengua de clase")))
P('</div>')
P('<p style="font-size:9.6pt">① <b>¿Qué tienes ya en la mochila?</b> Drie clusters die je vandaag inzet. <span class="gloss">Wat zit er al in je rugzak? — WV-018 geheugenraster.</span></p>')
P(clusters([
  ("🔤","Presente (U1/U3)",["yo hago · tú haces","nosotros vamos","ellos comen"],"De vormen die je al kent."),
  ("🎒","Actividades (U3/U4)",["comer · beber","estudiar · viajar","ver una película"],"Wat je doet op een dag."),
  ("🌍","La ruta hasta aquí",["España · México","Colombia · Perú","el mundo hispano"],"Waar je al geweest bent."),
]))
P(actx(1, "Calentamiento: ¿qué haces normalmente?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Zeg drie dingen die je vaak doet, in het <b>presente</b>. Je buur noteert. Wissel. <span class="gloss">Dit heb je nodig om straks «he hecho» te bouwen.</span></p>'
  '<p style="margin-left:12.5mm">Modelo: <i>«Normalmente estudio, veo la tele y hago deporte.»</i><br>Mi compañero/a hace: <span class="wl full"></span></p>', apoyo="MODELO → SIN AYUDA"))
P(actx(2, "El presente de haber (base)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>vooruitblik.</i> Het werkwoord <b>haber</b> gebruik je straks als hulpwerkwoord. Vul aan (pista gegeven).</p>'
  '<table class="mp"><thead><tr><th>Persona</th><th>haber</th></tr></thead><tbody>'
  '<tr><td>yo</td><td>h<span class="wl sm"></span> <span class="gloss">(he)</span></td></tr>'
  '<tr><td>tú</td><td>h<span class="wl sm"></span> <span class="gloss">(has)</span></td></tr>'
  '<tr><td>él/ella</td><td>h<span class="wl sm"></span> <span class="gloss">(ha)</span></td></tr></tbody></table>', apoyo="LETRA INICIAL (h…)"))
P(actx(3, "Ordena tus experiencias",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>WV-020 ophaalladder.</i> Zet op een lijn van <b>nunca</b> (0) naar <b>muchas veces</b> (vaak).</p>'
  + scale(["nunca","alguna vez","a veces","muchas veces"]) +
  '<p style="margin-left:12.5mm">He viajado en avión: <span class="wl md"></span></p>', apoyo="MODELO (lijn gegeven)"))
P(actx(4, "Empareja: actividad con lugar",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Verbind (schrijf de letter). Repaso ruta + actividades.</p>'
  '<table class="mp"><thead><tr><th>Actividad</th><th></th><th>Lugar</th></tr></thead><tbody>'
  '<tr><td>1 · comer tacos</td><td><span class="wl sm"></span></td><td>A · Perú 🇵🇪</td></tr>'
  '<tr><td>2 · ver Machu Picchu</td><td><span class="wl sm"></span></td><td>B · España 🇪🇸</td></tr>'
  '<tr><td>3 · visitar la Sagrada Família</td><td><span class="wl sm"></span></td><td>C · México 🇲🇽</td></tr></tbody></table>', apoyo="BANCO"))
P(actx(5, "Dos cosas que haces hoy (presente)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>zin uitbreiden.</i> Schrijf twee ware zinnen in het <b>presente</b> over vandaag (met <b>hago</b> en <b>veo</b>).</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (hoy hago… / hoy veo…)"))
P(actx(6, "Verdadero para mí",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>waar/niet waar voor jou.</i> Zet ✔ als het klopt, ✘ als niet. Verbeter er één met een presente-zin.</p>'
  '<p style="margin-left:12.5mm">☐ Viajo mucho. &nbsp; ☐ Veo muchas series. &nbsp; ☐ Hago deporte cada día.<br>Mi corrección: <span class="wl full"></span></p>', apoyo="MODELO"))
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> presente, actividades en la ruta hasta aquí met zelfcorrectie op de digitale pagina.</div>')
P('</div>')  # close §0

# ================= §1 · PRETÉRITO PERFECTO COMPUESTO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">1</span><span class="pk">§1 · ¿Qué has hecho? · pretérito perfecto compuesto</span>')
P('<div class="route-note">📍 Parada 8 · Cusco — Nina te enseña su diario: «Mira todo lo que <b>he hecho</b>».</div>')
P('<div class="intro"><b>ES:</b> Para contar lo que <b>has hecho</b> (hoy, esta semana, en tu vida) usas el <b>pretérito perfecto compuesto</b>: <b>haber</b> (he, has, ha…) + <b>participio</b>. La ruta: contexto → línea del tiempo → observar → regla → practicar → comunicar. <span class="gloss">Om te vertellen wat je gedaan hebt: haber + deelwoord.</span></div>')
P(lpd(("8","taalsysteem: perfecto compuesto (A2)"), ("4","interactie: ervaringen delen"), ("3","doelgericht schrijven met steun"), ("1","luisteren naar ervaringen")))
P('</div>')
# §1.1 observar: tijdlijn + vraag-spiegel + haber-cirkel
P('<h3 style="margin-top:6mm">§1.1 · Descubrir — la línea del tiempo</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto.</b> Nina chat met jou over vandaag. Kijk wát ze al <b>gedaan heeft</b>. <span class="gloss">Let op: he/has/ha + participio.</span></p>')
P('<div class="chat">'
  '<div class="chatline you"><div class="bub">¡Hola! Hoy <span class="fx vb">he subido</span> a Machu Picchu. 😍</div><div class="who">Nina</div></div>'
  '<div class="chatline me"><div class="bub">¡Qué bien! ¿<span class="fx vb">Has visto</span> las llamas?</div><div class="who">Tú</div></div>'
  '<div class="chatline you"><div class="bub">Sí, y <span class="fx vb">he sacado</span> muchas fotos. ¿Y tú? ¿Qué <span class="fx vb">has hecho</span> hoy?</div><div class="who">Nina</div></div>'
  '<div class="chatline me"><div class="bub">Yo <span class="fx vb">he estudiado</span> español. ¡Todavía no <span class="fx vb">he comido</span>!</div><div class="who">Tú</div></div></div>')
P('<p style="font-size:9.6pt">② <b>La línea del tiempo (VG-008 / GT-003).</b> Het perfecto compuesto verbindt het <b>verleden</b> met <b>nu</b> (een periode die nog niet af is: hoy, esta semana…):</p>')
P('<div class="xray"><div class="xs">antes ─────●───── <span class="fx ti">HOY</span> ─────▶ ahora</div>'
  '<div class="xrow"><div><b>he subido</b>gebeurd, maar «vandaag» telt nog mee</div><div><b>ahora</b>je vertelt het nú</div></div></div>')
P('<p style="font-size:9.6pt">③ <b>La pregunta como espejo (VG-016) — ¿has…? → he…</b></p>')
P(mirror([("¿Qué <b>has hecho</b> hoy?","He estudiado español."),("¿<b>Has visto</b> Machu Picchu?","Sí, lo <b>he visto</b>."),("¿<b>Habéis viajado</b> en tren?","Sí, <b>hemos viajado</b> en tren.")]))
P('<p style="font-size:9.6pt">④ <b>El verbo <i>haber</i> (auxiliar) — la rueda (GT-008), nagerekend:</b></p>')
P('<div class="fams" style="margin-top:2mm">')
P(pcard("haber + participio", '<table class="conj"><thead><tr><th>persona</th><th>haber</th><th>+ participio</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">he</td><td class="end">hablado / comido / vivido</td></tr>'
  '<tr><td class="p">tú</td><td class="v">has</td><td class="end">hecho / visto…</td></tr>'
  '<tr><td class="p">él/ella</td><td class="v">ha</td><td class="end">estado…</td></tr>'
  '<tr><td class="p">nosotros</td><td class="v">hemos</td><td class="end">viajado…</td></tr>'
  '<tr><td class="p">vosotros</td><td class="v">habéis</td><td class="end">ido…</td></tr>'
  '<tr><td class="p">ellos</td><td class="v">han</td><td class="end">vuelto…</td></tr></tbody></table>'))
P(pcard("La fórmula", '<div class="ej"><b>haber</b> (he, has, ha, hemos, habéis, han) + <b>participio</b>.<br>'
  '<i>(Yo) <b>he comido</b> un ceviche.</i><br><i>(Nosotros) <b>hemos viajado</b> a Perú.</i><br><i>¿(Tú) <b>has visto</b> las ruinas?</i></div>'
  '<div class="t2">🔴 Het hulpwerkwoord is <b>haber</b>, niet <i>tener</i>. De participio blijft <b>gelijk</b>: María ha comid<b>o</b> (niet comida).</div>'))
P('</div>')
P(blocks([
  [("per","(Yo) he"),("vb","comido"),("opt","un ceviche")],
  [("per","(Tú) has"),("vb","visto"),("opt","las llamas")],
  [("per","(Nosotros) hemos"),("vb","subido"),("opt","a la montaña")],
  [("per","(Ellos) han"),("vb","viajado"),("opt","en tren")],
]))
P(regla("Regla · pretérito perfecto compuesto",
  '<p><b>haber</b> in het presente (he, has, ha, <b>hemos</b>, habéis, han) + <b>participio</b>. '
  'Je gebruikt het voor iets wat gebeurd is in een periode die nog <b>doorloopt</b> (hoy, esta semana, este año) of voor <b>ervaringen</b> (alguna vez, nunca). '
  '<br>🔴 Auxiliar = <b>haber</b> (niet tener). 🔴 Participio verandert niet van vorm: <i>ella ha comid<b>o</b></i>.</p>'))
P('</div>')  # page §1.1

# §1.2 práctica + CLOZE (verplicht)
P('<div class="page">')
P('<div class="divider">Practicar · §1.2</div>')
P(actx(1, "Conjuga haber",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>substitutie-drill.</i> Vul de vorm van <b>haber</b> in.</p>'
  '<p style="margin-left:12.5mm">yo <span class="wl sm"></span> · tú <span class="wl sm"></span> · él <span class="wl sm"></span> · nosotros <span class="wl sm"></span> · vosotros <span class="wl sm"></span> · ellos <span class="wl sm"></span></p>', apoyo="PISTA (h-e, h-a-s…)"))
P(actx(2, "Substitutie: cambia la persona",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>substitutietabel.</i> Herschrijf <b>«he viajado»</b> voor elke persoon.</p>'
  '<table class="mp"><thead><tr><th>Persona</th><th>… viajado</th></tr></thead><tbody>'
  '<tr><td>tú</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>nosotros</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>ella</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>ellos</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="MARCO (tabla haber) → SIN AYUDA"))
P(actx(3, "Completa con haber + participio (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 7 min"},{"t":"★★☆"}],
  '<p><i>cloze klassiek (VERPLICHT — vormen nagerekend).</i> Vul <b>haber + participio</b> aan (persoon + infinitief tussen haakjes). <span class="gloss">Let op de onregelmatige participios (hacer→hecho, ver→visto…).</span></p>'
  '<p style="margin-left:12.5mm">1. (Yo) <span class="wl md"></span> a Machu Picchu. <i>(subir)</i><br>'
  '2. ¿(Tú) <span class="wl md"></span> las llamas? <i>(ver)</i><br>'
  '3. (Nosotros) <span class="wl md"></span> muchas fotos. <i>(sacar)</i><br>'
  '4. Nina <span class="wl md"></span> un diario de viaje. <i>(escribir)</i><br>'
  '5. (Ellos) <span class="wl md"></span> en tren. <i>(viajar)</i><br>'
  '6. Hoy (yo) todavía no <span class="wl md"></span>. <i>(comer)</i><br>'
  '7. ¿(Vosotros) <span class="wl md"></span> la maleta? <i>(hacer)</i><br>'
  '8. Diego <span class="wl md"></span> del viaje. <i>(volver)</i></p>'
  '<p style="margin-left:12.5mm" class="gloss">[antwoord-laag online] 1 he subido · 2 has visto · 3 hemos sacado · 4 ha escrito · 5 han viajado · 6 he comido · 7 habéis hecho · 8 ha vuelto</p>', apoyo="PISTA (haber gegeven) → SIN AYUDA"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha: ¿qué han hecho?</b> Cuatro personas cuentan qué han hecho este verano. Escucha y marca. <span class="gloss">Luisteren — 1ª globaal, 2ª detail.</span></div>',
           qr("Escanea y escucha", "Audio 8.1 · ¿Qué han hecho? · 0:55", seed=81)))
P(actx(4, "Escucha: ¿quién lo ha hecho?",
  [{"t":"👂 Escuchar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>luisteren en aanwijzen.</i> Kruis aan wie het gedaan heeft.</p>'
  '<table class="mp"><thead><tr><th>Ha…</th><th>Nina</th><th>Diego</th><th>Lucía</th></tr></thead><tbody>'
  '<tr><td>ha subido a la montaña</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>ha comido un ceviche</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>ha visto el mar</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>ha sacado muchas fotos</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="MODELO (audio 2×)"))
P(actx(5, "Transforma: presente → perfecto compuesto",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>transformatieketting.</i> Zet in het perfecto compuesto (voeg <b>hoy</b> toe).</p>'
  '<table class="mp"><thead><tr><th>Presente</th><th>Hoy… (perfecto)</th></tr></thead><tbody>'
  '<tr><td>Como un ceviche.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Viajamos en tren.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Ves las ruinas.</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="PISTA (haber + participio) → SIN AYUDA"))
P(actx(6, "¿Qué has hecho hoy? — escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>gestuurde productie.</i> Schrijf drie ware zinnen over vandaag met <b>he + participio</b>.</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (Hoy he… / Todavía no he…)"))
P(tarea_com("Tarea comunicativa · «¿Qué has hecho esta semana?»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b>Afzender·ontvanger·doel·situatie·resultaat:</b> vraag elkaar wat je <b>deze week gedaan hebt</b> (perfecto compuesto) en noteer twee dingen van je buur. <span class="gloss">«¿Qué has hecho esta semana? —He estudiado y he visto una serie.»</span></p>'
  '<p style="margin-left:12.5mm">Mi compañero/a ha…: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: MARCO (¿Qué has hecho? · He…) → SIN AYUDA · [CROSS: HTML «haber + participio» cloze + recorder]</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «haber + participio (cloze)», «haber Tetris» en de vraag-spiegel met zelfcorrectie.</div>')
P('</div>')  # page §1.2

# ================= §2 · PARTICIPIOS =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2 · Los participios · -ado / -ido (+ irregulares)</span>')
P('<div class="intro"><b>ES:</b> El <b>participio</b> es la segunda parte del perfecto compuesto. Los regulares terminan en <b>-ado</b> (-ar) o <b>-ido</b> (-er/-ir). Pero hay <b>irregulares</b> que debes memorizar. La ruta: máquina → árbol de decisión → irregulares → practicar. <span class="gloss">Deelwoorden vormen: regelmatig -ado/-ido + de onregelmatige uit het hoofd.</span></div>')
P(lpd(("8","taalsysteem: participio (vorming)"), ("3","doelgericht schrijven"), ("7","woordenschat: werkwoorden")))
P('</div>')
# §2.1 machine + beslisboom + irregulares
P('<h3 style="margin-top:6mm">§2.1 · La máquina de participios</h3>')
P('<p style="font-size:9.6pt">① <b>Observa la máquina (VG-004 / GT-007).</b> Neem de infinitief, verwijder de uitgang, plak <b>-ado</b> of <b>-ido</b>:</p>')
P(machine([("infinitivo","viajar"),("raíz","viaj-"),("+ terminación",'-<span class="end">ado</span>'),("participio","viajado")]))
P(machine([("infinitivo","comer"),("raíz","com-"),("+ terminación",'-<span class="end">ido</span>'),("participio","comido")]))
P('<p style="font-size:9.6pt">② <b>El árbol de decisión (VG-012 / GT-020):</b></p>')
P(tree([
  '¿El verbo termina en <b>-ar</b>? <span class="yes">SÍ</span> → raíz + <span class="res">-ado</span> <span class="gloss">(viajar → viajado, estar → estado)</span>',
  '¿Termina en <b>-er</b> o <b>-ir</b>? <span class="yes">SÍ</span> → raíz + <span class="res">-ido</span> <span class="gloss">(comer → comido, vivir → vivido)</span>',
  '¿Es un verbo <b>irregular</b>? <span class="no">¡OJO!</span> → memorízalo <span class="gloss">(hacer → hecho, ver → visto…)</span>',
]))
P('<p style="font-size:9.6pt">③ <b>Los irregulares (VG-026 · memorizar) — los 8 más frecuentes:</b></p>')
P('<table class="mp"><thead><tr><th>Infinitivo</th><th>Participio</th><th>Infinitivo</th><th>Participio</th></tr></thead><tbody>'
  '<tr><td>hacer</td><td class="trap">hecho</td><td>volver</td><td class="trap">vuelto</td></tr>'
  '<tr><td>ver</td><td class="trap">visto</td><td>poner</td><td class="trap">puesto</td></tr>'
  '<tr><td>decir</td><td class="trap">dicho</td><td>abrir</td><td class="trap">abierto</td></tr>'
  '<tr><td>escribir</td><td class="trap">escrito</td><td>romper</td><td class="trap">roto</td></tr></tbody></table>')
P('<div class="truc"><b>🔴 Truco:</b> muchos irregulares acaban en <b>-to</b> (visto, puesto, abierto, roto, vuelto, escrito) of <b>-cho</b> (hecho, dicho). ¡Memoriza estos 8!</div>')
P(regla("Regla · el participio",
  '<p><b>Regelmatig:</b> -ar → <b>-ado</b> (hablar → hablado) · -er/-ir → <b>-ido</b> (comer → comido, vivir → vivido). '
  '<b>Onregelmatig (uit het hoofd):</b> hacer→<b>hecho</b>, ver→<b>visto</b>, decir→<b>dicho</b>, escribir→<b>escrito</b>, volver→<b>vuelto</b>, poner→<b>puesto</b>, abrir→<b>abierto</b>, romper→<b>roto</b>.</p>'))
P('</div>')  # page §2.1
# §2.2 práctica
P('<div class="page">')
P('<div class="divider">Practicar · §2.2</div>')
P(actx(1, "¿-ado o -ido?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p><i>vorm herkennen.</i> Schrijf de regelmatige participio.</p>'
  '<p style="margin-left:12.5mm">viajar → <span class="wl sm"></span> · comer → <span class="wl sm"></span> · vivir → <span class="wl sm"></span> · estudiar → <span class="wl sm"></span> · beber → <span class="wl sm"></span> · subir → <span class="wl sm"></span></p>', apoyo="MODELO (regel §2.1)"))
P(actx(2, "Clasifica: regular o irregular",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>sorteren.</i> Sorteer de infinitieven: krijgt de participio de <b>gewone</b> uitgang (-ado/-ido) of is hij <b>irregular</b>? '
  '<span class="words"><b>comer · hacer · viajar · ver · vivir · escribir · estudiar · volver</b></span></p>'
  + sortcols([("regular","-ado / -ido"),("irregular","uit het hoofd")]), apoyo="BANCO → +1 eigen woord"))
P(actx(3, "Escribe el participio irregular (cloze)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>cloze klassiek.</i> Vul de <b>onregelmatige</b> participio in.</p>'
  '<p style="margin-left:12.5mm">a) hacer → he <span class="wl sm"></span> &nbsp; b) ver → has <span class="wl sm"></span> &nbsp; c) escribir → ha <span class="wl sm"></span><br>'
  'd) volver → hemos <span class="wl sm"></span> &nbsp; e) poner → habéis <span class="wl sm"></span> &nbsp; f) abrir → han <span class="wl sm"></span><br><span class="gloss">[online] a hecho · b visto · c escrito · d vuelto · e puesto · f abierto</span></p>', apoyo="PISTA (-to / -cho) → SIN AYUDA"))
P(actx(4, "Empareja: infinitivo ↔ participio",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>matching.</i> Verbind (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Infinitivo</th><th></th><th>Participio</th></tr></thead><tbody>'
  '<tr><td>1 · decir</td><td><span class="wl sm"></span></td><td>A · roto</td></tr>'
  '<tr><td>2 · romper</td><td><span class="wl sm"></span></td><td>B · dicho</td></tr>'
  '<tr><td>3 · poner</td><td><span class="wl sm"></span></td><td>C · abierto</td></tr>'
  '<tr><td>4 · abrir</td><td><span class="wl sm"></span></td><td>D · puesto</td></tr></tbody></table>', apoyo="BANCO"))
P(actx(5, "¿Es correcto? — ejemplo o no-ejemplo",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>voorbeeld of niet-voorbeeld.</i> Kruis ✔ (goed) of ✘ (fout) aan en verbeter de foute participio.</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>✔ / ✘</th><th>Corrección</th></tr></thead><tbody>'
  '<tr><td>He <span class="trap">hacido</span> la maleta.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Has viajado a Perú.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Ha <span class="trap">veido</span> las llamas.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Hemos comido ceviche.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="PISTA (irregular?) → SIN AYUDA"))
P(tarea_com("Tarea comunicativa · «Cadena de experiencias»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p><b>Afzender·ontvanger·doel·situatie·resultaat:</b> in een ketting: A zegt «He viajado», B herhaalt + voegt toe «He viajado y he comido…», enz. Gebruik zoveel mogelijk <b>irregulares</b>. <span class="gloss">He hecho, he visto, he vuelto…</span></p>'
  '<p style="margin-left:12.5mm">Nuestra cadena más larga: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: BANCO (lista de participios) → SIN AYUDA · [CROSS: HTML «participio ↔ infinitivo» + «participio irregular»]</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «participio ↔ infinitivo» (match), «regular o irregular» (classify) en «participio irregular» (cloze).</div>')
P('</div>')  # page §2.2

# ================= §3 · MARCADORES =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3 · Marcadores · ya · todavía no · hoy · alguna vez · nunca</span>')
P('<div class="intro"><b>ES:</b> Los <b>marcadores</b> dicen <b>cuándo</b> y avisan que toca perfecto compuesto: <b>hoy, esta semana, este año</b> (periodo abierto) y <b>ya, todavía no, alguna vez, nunca, muchas veces</b> (experiencia). La ruta: contraste → rails → practicar. <span class="gloss">Tijdmarkeerders die bij het perfecto compuesto passen.</span></div>')
P(lpd(("8","taalsysteem: marcadores temporales"), ("4","interactie: ervaringen"), ("3","zinnen schrijven met steun")))
P('</div>')
P('<h3 style="margin-top:6mm">§3.1 · El contraste — ya ↔ todavía no</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto.</b> Nina maakt haar checklist voor de reis. <span class="gloss">Ya = al gedaan · todavía no = nog niet gedaan.</span></p>')
P('<div class="chat">'
  '<div class="chatline you"><div class="bub"><span class="fx ti">Ya</span> he hecho la maleta y <span class="fx ti">ya</span> he comprado el billete. ✅</div><div class="who">Nina</div></div>'
  '<div class="chatline me"><div class="bub">¿Y el hotel?</div><div class="who">Tú</div></div>'
  '<div class="chatline you"><div class="bub"><span class="fx ti">Todavía no</span> he reservado el hotel. 😅</div><div class="who">Nina</div></div></div>')
P('<p style="font-size:9.6pt">② <b>Contrastes mínimos (GT-011):</b></p>')
P(vpairs([("ya + he hecho","todavía no + he hecho"),("ya (klaar ✅)","todavía no (nog niet ⏳)"),("¿Ya has comido?","No, todavía no."),("alguna vez (ooit)","nunca (nooit)")]))
P('<p style="font-size:9.6pt">③ <b>Los marcadores en rieles (VG-023) — ¿experiencia o periodo abierto?</b></p>')
P('<table class="conj"><thead><tr><th>Periodo abierto (nog bezig)</th><th>Experiencia (in je leven)</th></tr></thead><tbody>'
  '<tr><td class="v">hoy · esta semana</td><td class="v">alguna vez · nunca</td></tr>'
  '<tr><td class="v">este mes · este año</td><td class="v">muchas veces · ya · todavía no</td></tr>'
  '<tr><td>Hoy he estudiado.</td><td>¿Has viajado alguna vez en avión?</td></tr></tbody></table>')
P('<div class="truc"><b>🔴 NL ↔ ES:</b> <b>ya</b> = «al / reeds», <b>todavía no</b> = «nog niet». Let op: <b>nunca</b> + he… = «ik heb nooit…»: <i>Nunca he estado en Perú.</i></div>')
P(regla("Regla · marcadores",
  '<p>Deze marcadores kondigen het <b>perfecto compuesto</b> aan: <b>hoy, esta semana, este mes, este año</b> (periode die nog loopt) en <b>ya, todavía no, alguna vez, nunca, muchas veces</b> (ervaring). '
  '<br><b>ya</b> (al ✅) ↔ <b>todavía no</b> (nog niet ⏳). <b>¿Alguna vez has…?</b> = «Heb je ooit…?».</p>'))
P('</div>')  # page §3.1
# §3.2 práctica
P('<div class="page">')
P('<div class="divider">Practicar · §3.2</div>')
P(actx(1, "¿ya o todavía no?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>vorm kiezen.</i> Kruis aan volgens ✅ (klaar) of ⏳ (nog niet).</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>ya</th><th>todavía no</th></tr></thead><tbody>'
  '<tr><td>___ he hecho la maleta ✅</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ he reservado el hotel ⏳</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ hemos comprado los billetes ✅</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ he visto Machu Picchu ⏳</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="MODELO (regel §3.1)"))
P(actx(2, "Gap-fill: el marcador correcto",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>cloze klassiek.</i> Vul de marcador in (hoy · esta semana · alguna vez · nunca · ya).</p>'
  '<p style="margin-left:12.5mm">a) ___ he estudiado dos horas (vandaag).<br>'
  'b) ¿Has viajado ___ en barco? (ooit)<br>'
  'c) ___ he estado en Perú (nooit).<br>'
  'd) ___ hemos ido al cine dos veces (deze week).<br><span class="gloss">banco: hoy · alguna vez · nunca · esta semana</span></p>', apoyo="BANCO"))
P(actx(3, "Clasifica el marcador",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>sorteren.</i> Periode-die-loopt of ervaring? '
  '<span class="words"><b>hoy · nunca · esta semana · alguna vez · este año · muchas veces</b></span></p>'
  + sortcols([("periodo abierto","hoy, este año…"),("experiencia","nunca, alguna vez…")], eigen=False), apoyo="BANCO"))
P(actx(4, "Mi lista de experiencias",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>gestuurde productie.</i> Schrijf twee zinnen met <b>alguna vez / nunca</b> over jouw leven.</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (Nunca he… / Alguna vez he…) → SIN AYUDA"))
P(tarea_com("Tarea comunicativa · «¿Lo has hecho alguna vez?»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 7 min"},{"t":"★★★"}],
  '<p><b>Afzender·ontvanger·doel·situatie·resultaat:</b> stel elkaar drie vragen met <b>alguna vez</b> (viajar en avión, comer ceviche, ver la nieve…). Antwoord met <b>ya / nunca / muchas veces</b>. <span class="gloss">«¿Has visto la nieve alguna vez? —Sí, ya la he visto. / No, nunca.»</span></p>'
  '<p style="margin-left:12.5mm">Una respuesta interesante de mi compañero/a: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: MARCO (¿Has…? · Sí, ya… / No, nunca…) → SIN AYUDA · [CROSS: HTML «ya / todavía no» cloze]</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «ya o todavía no» (cloze) en «experiencia o periodo» (classify) met zelfcorrectie.</div>')
P('</div>')  # page §3.2

# ================= §4 · ¿QUÉ TIEMPO HACE? =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4 · ¿Qué tiempo hace? · el clima</span>')
P('<div class="intro"><b>ES:</b> En Perú hay tres climas: <b>costa</b>, <b>sierra</b> (los Andes) y <b>selva</b>. Aprendes a decir qué <b>tiempo hace</b>: hace sol, hace frío, llueve, nieva, está nublado. La ruta: infografía → pares → practicar → comunicar. <span class="gloss">Het volledige weerthema: over het weer praten.</span></div>')
P(lpd(("8","taalsysteem: expresiones del tiempo"), ("7","woordenschat: el clima"), ("5","cultuur: klimaatzones"), ("1","luisteren: el parte del tiempo")))
P('</div>')
P('<h3 style="margin-top:6mm">§4.1 · La infografía del tiempo (VS-017)</h3>')
P('<p style="font-size:9.6pt">① <b>Observa.</b> Met <b>hacer</b> (hace…) of een werkwoord (llueve, nieva) of <b>estar</b> (está nublado):</p>')
P(clusters([
  ("☀️","Hace…",["hace sol","hace calor","hace frío","hace viento","hace buen/mal tiempo"],"met het werkwoord hacer."),
  ("🌧️","Verbo solo",["llueve (la lluvia)","nieva (la nieve)"],"één werkwoord = het weer."),
  ("☁️","Está…",["está nublado","hay tormenta","hay nubes"],"met estar / hay."),
]))
P('<p style="font-size:9.6pt">② <b>Pares de opuestos (VS-007):</b></p>')
P(vpairs([("hace calor 🥵","hace frío 🥶"),("hace sol ☀️","está nublado ☁️"),("hace buen tiempo","hace mal tiempo"),("llueve 🌧️","nieva ❄️")]))
P('<p style="font-size:9.6pt">③ <b>La temperatura:</b> <i>Estamos a 20 grados. Hace 5 grados en Cusco.</i></p>')
P(audiorow('<div class="ic">🎧</div><div><b>El parte del tiempo.</b> Escucha el pronóstico de tres ciudades (Lima, Cusco, la selva) y anota el tiempo. <span class="gloss">Weerbericht — 1ª betekenis, 2ª schrijven.</span></div>',
           qr("Escanea y escucha", "Audio 8.2 · El parte del tiempo · 0:50", seed=82)))
P(regla("Regla · ¿qué tiempo hace?",
  '<p>Drie manieren: (1) <b>hace</b> + sol / calor / frío / viento / buen tiempo / mal tiempo · (2) een werkwoord alleen: <b>llueve</b> (la lluvia) · <b>nieva</b> (la nieve) · (3) <b>está</b> nublado / <b>hay</b> tormenta. '
  '<br>🔴 «Het is warm (weer)» = <b>hace calor</b> (niet <span class="trap">es caliente</span>). Voor de temperatuur: <i>estamos a … grados</i>.</p>'))
P('</div>')  # page §4.1
# §4.2 práctica
P('<div class="page">')
P('<div class="divider">Practicar · §4.2</div>')
P(actx(1, "¿hace, está o un verbo?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>vorm kiezen.</i> Kruis aan welk woord de zin nodig heeft.</p>'
  '<table class="mp"><thead><tr><th>Frase</th><th>hace</th><th>está</th><th>llueve/nieva</th></tr></thead><tbody>'
  '<tr><td>___ sol</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ nublado</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ (regenen)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ frío</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>___ (sneeuwen)</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="MODELO (regel §4.1)"))
P(actx(2, "Empareja: símbolo ↔ tiempo",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>matching.</i> Verbind het symbool met de uitdrukking (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Símbolo</th><th></th><th>Tiempo</th></tr></thead><tbody>'
  '<tr><td>1 · ☀️</td><td><span class="wl sm"></span></td><td>A · nieva</td></tr>'
  '<tr><td>2 · 🌧️</td><td><span class="wl sm"></span></td><td>B · hace sol</td></tr>'
  '<tr><td>3 · ❄️</td><td><span class="wl sm"></span></td><td>C · está nublado</td></tr>'
  '<tr><td>4 · ☁️</td><td><span class="wl sm"></span></td><td>D · llueve</td></tr></tbody></table>', apoyo="BANCO"))
P(actx(3, "Dictado: el parte del tiempo",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>dictee.</i> Schrijf het weer van vier steden (ciudad + tiempo), één per regel.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl lg"></span> 2. <span class="wl lg"></span><br>'
  '3. <span class="wl lg"></span> 4. <span class="wl lg"></span></p>', apoyo="MODELO (2×)"))
P(actx(4, "¿Qué tiempo hace hoy? — escribe",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>gestuurde productie.</i> Schrijf drie zinnen over het weer van vandaag bij jou.</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (Hoy hace… / Está…)"))
P(tarea_com("Tarea comunicativa · «El tiempo en tu ciudad»",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p><b>Keten luisteren → spreken.</b> A is de weerman/-vrouw en vertelt het weer van een stad (verzonnen); B tekent het symbool en zegt of hij/zij daar naartoe wil. Wissel. <span class="gloss">«Hoy en Cusco hace frío y está nublado.»</span></p>'
  '<p style="margin-left:12.5mm">El tiempo de mi compañero/a: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: MARCO (Hoy hace… · está…) → SIN AYUDA · [CROSS: HTML «¿qué tiempo hace?» + recorder «repite el tiempo»]</div>'))
P('<div class="route-note">🎮 <b>Juega online:</b> «¿qué tiempo hace?» (classify), «símbolo ↔ tiempo» (match) en el parte del tiempo (audio).</div>')
P('</div>')  # page §4.2

# ================= §5 · LECTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">📖</span><span class="pk">§5 · Lectura — «El diario de viaje de Nina»</span>')
P('<div class="intro"><b>ES:</b> Vas a leer el <b>diario de viaje</b> de Nina en Perú. Primero <b>predices</b> desde el título y la foto, después lees con un <b>objetivo</b>. <span class="gloss">Je leest het reisdagboek van Nina: eerst voorspellen, dan doelgericht lezen. SK-011/SK-018.</span></div>')
P(lpd(("1","onderwerp/hoofdgedachte bij lezen"), ("2","relevante info selecteren"), ("3","doelgericht schrijven met steun")))
P('</div>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> diario de viaje / blog</span><span class="tm"><b>De:</b> Nina (Cusco 🇵🇪)</span><span class="tm">🎯 seguir un viaje</span></div>')
P(actx(1, "Antes de leer: predice",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★☆☆"}],
  '<p><i>voorspellen vanuit titel/beeld (SK-011).</i> Titel = «El diario de viaje de Nina». ¿Qué crees que ha hecho Nina?</p>'
  '<p style="margin-left:12.5mm">Creo que Nina ha…: <span class="wl full"></span></p>', apoyo="MODELO (ha subido, ha visto…)"))
P('<div class="ptexts">'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["nina"]}</div><div><div class="nm">Nina · día 1 (Cusco)</div><div class="fr">diario de viaje 🇵🇪</div></div></div>'
  '<p><b>Lunes.</b> ¡Por fin <span class="evi">he llegado</span> a Cusco! <span class="evi">He viajado</span> en avión desde Lima. Aquí, a 3400 metros, <span class="evi">hace frío</span> y <span class="evi">está nublado</span>. Esta tarde <span class="evi">he visto</span> la Plaza de Armas y <span class="evi">he comido</span> un plato típico. Todavía no <span class="evi">he subido</span> a la montaña.</p></div>'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["nina"]}</div><div><div class="nm">Nina · día 2 (Machu Picchu)</div><div class="fr">diario de viaje 🇵🇪</div></div></div>'
  '<p><b>Martes.</b> ¡Qué día! <span class="evi">He cogido</span> el tren muy pronto y <span class="evi">he subido</span> a <span class="evi">Machu Picchu</span>. <span class="evi">Ha hecho sol</span> toda la mañana. <span class="evi">He visto</span> las llamas y <span class="evi">he sacado</span> mil fotos. <span class="evi">He escrito</span> una postal para mi familia. ¡Nunca <span class="evi">he estado</span> tan feliz!</p></div></div>')
P('<div class="lecdoel">🎯 <b>Objetivo de lectura:</b> lees om te volgen <b>wat Nina wél en nog niet gedaan heeft</b> en <b>welk weer</b> het was — je hoeft niet élk woord te begrijpen.</div>')
P('</div>')  # page §5a
P('<div class="page">')
P(actx(2, "Escanea: ¿qué ha hecho Nina?",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>scannen → informatieraster (SK-014/SK-021).</i> Zoek de gegevens in het dagboek.</p>'
  '<table class="mp"><thead><tr><th></th><th>Transporte</th><th>Tiempo (clima)</th><th>Una cosa que ha hecho</th></tr></thead><tbody>'
  '<tr><td><b>Día 1 · Cusco</b></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td><b>Día 2 · Machu Picchu</b></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '</tbody></table>', apoyo="MODELO (tekst boven)"))
P(actx(3, "¿Verdadero o falso? + prueba",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>juist/fout + bewijs (SK-018).</i> Waar of niet waar? Noteer de <b>woorden uit het dagboek</b> die het bewijzen.</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba (del texto)</th></tr></thead><tbody>'
  '<tr><td>Nina ha viajado en avión a Cusco.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>En Machu Picchu ha llovido todo el día.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Nina ha escrito una postal.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>El día 1 ya ha subido a la montaña.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '</tbody></table>', apoyo="PISTA (onderstreep in de tekst)"))
P(actx(4, "Del contexto: ¿qué significa?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>betekenis uit context (SK-020).</i> Wat betekent <b>«he cogido el tren»</b> en <b>«una postal»</b>? Kies + leg uit welke aanwijzing hielp.</p>'
  '<p style="margin-left:12.5mm">he cogido = ☐ ik heb genomen ☐ ik heb gekocht &nbsp;·&nbsp; una postal = ☐ een ansichtkaart ☐ een koffer<br>Pista que me ayudó: <span class="wl lg"></span></p>', apoyo="PISTA"))
P(actx(5, "Ordena el viaje de Nina",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>zinnen ordenen (1–5).</i> Zet de reis van Nina in de juiste volgorde.</p>'
  '<p style="margin-left:12.5mm">___ Ha subido a Machu Picchu. &nbsp; ___ Ha llegado a Cusco en avión. &nbsp; ___ Ha visto la Plaza de Armas.<br>'
  '___ Ha cogido el tren muy pronto. &nbsp; ___ Ha escrito una postal.</p>', apoyo="BANCO (día 1 → día 2)"))
P(tarea_com("Tarea comunicativa · «Tu propio día de viaje» (keten lezen→schrijven)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p><b>Keten lezen → schrijven.</b> Schrijf, zoals Nina, één dagboekdag over een (echte of verzonnen) reis. Gebruik minstens <b>vier</b> keer perfecto compuesto + één marcador + het weer. <span class="gloss">«Hoy he llegado a… He visto… Ha hecho…»</span></p>'
  '<div class="wbox sm"></div>'
  '<div class="steun" style="margin-left:0mm">Apoyo: MARCO (Hoy he… · He visto… · Ha hecho…) → SIN AYUDA · [CROSS: HTML «describe tus vacaciones» — recorder]</div>'))
P('<div class="route-note">🎮 <b>Sigue online:</b> luister het diario (TTS), doe de begripsquiz en neem je eigen dag op (recorder) op de digitale pagina.</div>')
P('</div>')  # page §5b

# ================= TALLER DE LENGUA =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num" style="color:var(--crema)">✎</span><span class="pk" style="background:var(--gd)">Taller de lengua</span>')
P('<div class="intro"><b>ES:</b> Dos herramientas: la <b>tilde diacrítica</b> (dezelfde letters, ander streepje = andere betekenis) en los <b>conectores del relato</b> (primero/luego/al final — ¡para tu diario!). <span class="gloss">Accentstreepje dat betekenis verandert + verteltekst-conectoren.</span></div>')
P(lpd(("8","taalsysteem: ortografía (tilde diacrítica)"), ("3","tekst ordenen met conectoren")))
P('</div>')
P('<h3 style="margin-top:6mm">La tilde diacrítica · mismo sonido, tilde ≠ significado</h3>')
P('<p style="font-size:9.6pt">① <b>Observa (VG-019 pares):</b> hetzelfde woordbeeld, mét of zónder streepje:</p>')
P('<table class="mp"><thead><tr><th>Con tilde</th><th>uso</th><th>Sin tilde</th><th>uso</th></tr></thead><tbody>'
  '<tr><td class="trap">tú</td><td>jij (persoon)</td><td>tu</td><td>jouw (bezit)</td></tr>'
  '<tr><td class="trap">él</td><td>hij (persoon)</td><td>el</td><td>de/het (lidwoord)</td></tr>'
  '<tr><td class="trap">qué</td><td>wat? (vraag)</td><td>que</td><td>dat/die (verbinding)</td></tr>'
  '<tr><td class="trap">sí</td><td>ja</td><td>si</td><td>als/indien</td></tr>'
  '<tr><td class="trap">más</td><td>meer</td><td>mas</td><td>maar (literair)</td></tr></tbody></table>')
P('<div class="truc"><b>🔴 Truco:</b> het <b>streepje (tilde diacrítica)</b> zit meestal op het woord met de <b>«sterkste» betekenis</b>: de persoon (tú, él), de vraag (qué), het antwoord ja (sí), de vergelijking (más).</div>')
P(actx(1, "¿Con tilde o sin tilde?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>ortografía.</i> Kies de juiste vorm.</p>'
  '<p style="margin-left:12.5mm">a) ¿(Tú / Tu) ___ has hecho la maleta?<br>'
  'b) Este es (él / el) ___ tren a Cusco.<br>'
  'c) ¿(Qué / Que) ___ has visto hoy?<br>'
  'd) —¿Has comido? —(Sí / Si) ___ .<br>'
  'e) Quiero ver (más / mas) ___ ruinas.<br><span class="gloss">[online] a Tú · b el · c Qué · d Sí · e más</span></p>', apoyo="MODELO (tabla boven) → SIN AYUDA"))
P(actx(2, "Corrige las tildes",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>foutenkliniek.</i> Zet het streepje waar het hoort en herschrijf.</p>'
  '<p style="margin-left:12.5mm">1) <span class="trap">¿Que has hecho tu hoy?</span> → <span class="wl lg"></span><br>'
  '2) <span class="trap">El ha viajado en el tren.</span> → <span class="wl lg"></span><br>'
  '3) <span class="trap">Si, quiero mas fotos.</span> → <span class="wl lg"></span></p>', apoyo="PISTA (persoon/vraag/ja/meer) → SIN AYUDA"))
P('<h3 style="margin-top:6mm">Conectores del relato · primero · luego · después · al final</h3>')
P('<p style="font-size:9.6pt">② <b>Voor je reisverslag — la secuencia del día:</b></p>')
P(scale(["primero","luego","después","al final"]))
P(actx(3, "Ordena el diario con conectores",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>gap-fill met betekenis.</i> Vul het verbindingswoord in (primero/luego/después/al final).</p>'
  '<p style="margin-left:12.5mm">___ , he cogido el tren. ___ , he subido a Machu Picchu. ___ , he sacado fotos. ___ , he vuelto al hotel.<br><span class="wl full"></span></p>', apoyo="BANCO"))
P(actx(4, "Dictado corto del viaje",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>dictee (reconstrueren).</i> Escucha y escribe cuatro palabras del viaje (con tilde donde toca).</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl md"></span> 2. <span class="wl md"></span> 3. <span class="wl md"></span> 4. <span class="wl md"></span></p>', apoyo="MODELO (2×)"))
P(actx(5, "Escribe tres frases del diario",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>vrije productie.</i> Schrijf drie zinnen van jouw reisdag met <b>primero · luego · al final</b> + perfecto compuesto.</p>'
  '<div class="wbox sm"></div>', apoyo="SIN AYUDA"))
P('<div class="route-note">🎮 <b>Practica online:</b> «tilde diacrítica» en «ordena el diario» met zelfcorrectie.</div>')
P('</div>')  # page Taller

# ================= CULTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">★</span><span class="pk">Cultura · Machu Picchu y el clima andino</span>')
P('<div class="intro"><b>ES:</b> Perú tiene <b>tres climas</b> en un solo país. Descubre <b>Machu Picchu</b>, los <b>Andes</b> y por qué el tiempo cambia tanto. <span class="gloss">Ontdek Machu Picchu, de Andes en de drie klimaatzones van Peru.</span></div>')
P(lpd(("5","kenmerkende aspecten van de cultuur"), ("2","relevante info uit een tekst")))
P('</div>')
P('<div class="fams" style="margin-top:6mm">')
P(pcard("🏔️ Machu Picchu 🇵🇪", '<div class="ej">La ciudad <b>inca</b>, a 2430 m. Se llega en <b>tren</b> y luego a pie. Una de las <b>siete maravillas</b> del mundo. Nina la <b>ha visitado</b> hoy.</div><div class="anchor gloss">Machu Picchu = het symbool van Peru.</div>'))
P(pcard("🦙 Los Andes y las llamas", '<div class="ej">La <b>sierra</b> (los Andes) es alta y fría. Allí viven las <b>llamas</b> y las <b>alpacas</b>. En <b>Cusco</b>, la antigua capital inca, hace frío por la noche.</div><div class="t2">Cusco = 3400 m → hace frío incluso en verano.</div>'))
P('</div>')
P('<p style="font-size:9.6pt">① <b>Los tres climas de Perú (VG-020 mapa) — un país, tres tiempos:</b></p>')
P('<table class="mp"><thead><tr><th>Zona</th><th>¿Dónde?</th><th>El tiempo</th></tr></thead><tbody>'
  '<tr><td><b>la costa</b></td><td>Lima, el mar 🌊</td><td>seco, hace sol, poca lluvia</td></tr>'
  '<tr><td><b>la sierra</b></td><td>Cusco, los Andes 🏔️</td><td>hace frío, a veces nieva</td></tr>'
  '<tr><td><b>la selva</b></td><td>el Amazonas 🌴</td><td>hace calor y llueve mucho</td></tr></tbody></table>')
P('<div class="truc"><b>🟡 Dato:</b> en Perú puedes tener <b>tres climas en un día</b>: sol en la costa, frío en la sierra y lluvia en la selva. Por eso Nina siempre lleva un abrigo <b>y</b> un paraguas.</div>')
P('<p style="font-size:9.6pt">② <b>Un símbolo por país (repaso de la ruta):</b></p>')
P(vpairs([("la Sagrada Família 🇪🇸","los tacos 🇲🇽"),("Cartagena 🇨🇴","Machu Picchu 🇵🇪"),("el flamenco 🇪🇸","las llamas 🇵🇪")]))
P(actx(1, "Comprensión — verdadero o falso",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p><i>juist/fout + verbeteren.</i> Waar of niet waar? Verbeter de foute.</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Corrección</th></tr></thead><tbody>'
  '<tr><td>En Cusco hace frío.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>En la selva nieva mucho.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>A Machu Picchu se llega en tren.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="MODELO (tekst boven)"))
P(actx(2, "El clima de mi país / mi región",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>productie + spreken.</i> Schrijf 2–3 zinnen over het weer waar jij woont in verschillende seizoenen (¿qué tiempo hace en verano/invierno?). Presenteer aan je buur.</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (En verano hace… · En invierno…) → SIN AYUDA"))
P(actx(3, "Empareja: zona ↔ clima",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>matching.</i> Verbind de zone met het weer (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Zona</th><th></th><th>Clima</th></tr></thead><tbody>'
  '<tr><td>1 · la costa</td><td><span class="wl sm"></span></td><td>A · hace frío, nieva</td></tr>'
  '<tr><td>2 · la sierra</td><td><span class="wl sm"></span></td><td>B · hace calor, llueve</td></tr>'
  '<tr><td>3 · la selva</td><td><span class="wl sm"></span></td><td>C · seco, hace sol</td></tr></tbody></table>', apoyo="BANCO"))
P('<div class="route-note">🎮 <b>Sigue online:</b> «país ↔ clima» (match) en de kaart van de Spaanstalige wereld op de digitale pagina.</div>')
P('</div>')  # page Cultura

# ================= TAREA FINAL =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num">✦</span><span class="pk" style="background:var(--gd)">Tarea final · Mis vacaciones</span>')
P('<div class="intro"><b>ES:</b> Escribe (o graba en vlog) el <b>diario de tus vacaciones</b>: ¿qué has hecho, dónde, con qué transporte y qué tiempo ha hecho? Usa el <b>perfecto compuesto</b>. <span class="gloss">Maak je reisverslag met perfecto compuesto — als tekst of vlog.</span></div>')
P('<div class="route-note">🎯 <b>Communicatieve taak:</b> afzender = jij (de reiziger) · ontvanger = je familie/vrienden · doel = je reis navertellen · situatie = terug van vakantie · resultaat = een reisverslag (of vlog) met perfecto compuesto.</div>')
P(lpd(("3","doelgericht schrijven met een voorbeeld"), ("4","mondeling vertellen (vlog)"), ("7","woordenschat viajes/clima"), ("8","perfecto compuesto · marcadores · el tiempo")))
P('</div>')
P('<ol class="pasos">'
  '<li><b>Elige un destino</b> (echt of verzonnen) en het reismoment. ¿Adónde has ido?</li>'
  '<li><b>Rellena la ficha</b> hieronder: transporte · tiempo · tres cosas que has hecho.</li>'
  '<li><b>Escribe el diario</b> (mín. 5 zinnen) met <b>perfecto compuesto</b> + marcadores (primero/luego/al final) + het weer.</li>'
  '<li><b>Graba un vlog</b> (of lees voor) op de digitale pagina — of doe het in pareja.</li>'
  '<li><b>Añade una foto/dibujo</b> del viaje met een korte onderschrift («He visto…»).</li></ol>')
P('<div class="se" style="margin-top:4mm">La ficha de mi viaje <span class="gloss" style="font-size:8pt">· vul in</span></div>')
P('<table class="alf"><thead><tr><th>Dato</th><th>Mi viaje</th></tr></thead><tbody>'
  '<tr><td>Destino (¿adónde has ido?)</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>Transporte (¿cómo has viajado?)</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>El tiempo (¿qué tiempo ha hecho?)</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>Tres cosas que has hecho</td><td><span class="wl lg"></span></td></tr></tbody></table>')
P('<div class="se" style="margin-top:5mm">Mi diario de vacaciones <span class="gloss" style="font-size:8pt">· mín. 5 frases con perfecto compuesto</span></div><div class="wbox"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba tu vlog</b> en la página digital (recorder + rúbrica).</div>',
           qr("Escanea y graba", "Tarea · Mis vacaciones", seed=84)))
P('<div class="se" style="margin-top:5mm">Mini-encuesta: ¿adónde ha viajado la clase? <span class="gloss" style="font-size:8pt">— vraag 5 klasgenoten, teken de balken</span></div>')
P(gustobars([("a la playa", 60), ("a la montaña", 40), ("a otra ciudad", 50), ("a otro país", 30)]))
P('<p style="font-size:8.6pt" class="gloss">↳ vervang de voorbeeld-balken door je eigen resultaten (aantal /5 → %).</p>')
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Ik gebruik minstens <b>5×</b> perfecto compuesto</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>participios</b> correct (ook irregular)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik vertel het <b>weer</b> en het <b>transporte</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>marcadores/conectores</b> (primero/ya…)</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — el diario de mi compañero/a</div>'
  '<table><thead><tr><th>Lo que me gusta de su viaje</th><th>Un consejo (una cosa)</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('</div>')  # page Tarea

# ================= REPASO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">✓</span><span class="pk">Repaso · lo esencial</span>')
P('<div class="intro"><b>ES:</b> Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, 13 juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag.</span></div>')
P('</div>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>Perfecto compuesto:</b> <b>haber</b> (he, has, ha, hemos, habéis, han) + <b>participio</b>: <i>He viajado. ¿Has visto?</i></li>'
  '<li><b>Participios:</b> -ar → <b>-ado</b> · -er/-ir → <b>-ido</b>. Irregular: hecho, visto, dicho, escrito, vuelto, puesto, abierto, roto.</li>'
  '<li><b>Marcadores:</b> hoy · esta semana · este año (periode) · ya ↔ todavía no · alguna vez · nunca · muchas veces (ervaring).</li>'
  '<li><b>El tiempo:</b> hace sol/calor/frío/viento · llueve · nieva · está nublado · estamos a … grados.</li>'
  '<li><b>Las trampas:</b> 🔴 <b>haber</b> ≠ tener (has hecho, niet tienes hecho) · 🔴 participio blijft gelijk (ha comid<b>o</b>) · 🔴 tilde diacrítica (tú/tu · qué/que).</li></ul></div>')
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> 13 spelletjes met zelfcorrectie en spreiding op de digitale pagina.</div>')
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td>vertellen wat ik <b>gedaan heb</b> (perfecto compuesto)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>participios</b> vormen (regelmatig + onregelmatig)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>marcadores</b> gebruiken (ya · todavía no · nunca)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>over het <b>weer</b> praten (hace sol · llueve)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>viajes/transporte</b> benoemen (el tren, la maleta)</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil de U8: <span class="wl md"></span> · Lo más difícil: <span class="wl md"></span></i></div>')
P('<div class="bridge"><b>» Fin del viaje de 5º… ¡pero la ruta sigue!</b> Ya sabes contar qué <b>has hecho</b>. En <b>6º (C6)</b> el viaje continúa hacia el <b>pasado</b> (historias y biografías) con nieuwe verhalen en nieuwe paradas. <span class="gloss">Einde van de reis van jaar 5 — in het 6de gaat de route verder.</span></div>')
P('</div>')  # page Repaso

# ================= §V VOCABULARIO =================
import json
VOC = json.load(open(f"{HERE}/u8_vocab.json", encoding="utf-8"))
GRP = [("viajes","Viajes y vacaciones"),("clima","El tiempo · el clima"),("transporte","El transporte"),
       ("experiencias","Experiencias y marcadores"),("participios","Los participios"),("peru","Perú · la ruta")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (receptief & productief)")))
P('</div>')
P('<p style="font-size:9.6pt">El <b>viaje</b> als netwerk — drie families die de hele unit dragen:</p>')
P(clusters([
  ("🧳","La maleta (viajes)",["el billete · el pasaporte","el hotel · la excursión","el avión · el tren"],"Wat je meeneemt & neemt."),
  ("🌦️","El tiempo",["hace sol · hace frío","llueve · nieva","está nublado"],"Hoe het weer is."),
  ("✅","¿Qué has hecho?",["he viajado · he visto","hecho · dicho · vuelto","ya · todavía no · nunca"],"Wat je gedaan hebt."),
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
  '<p>Schrijf de vertaling. el viaje = <span class="wl md"></span> · la maleta = <span class="wl md"></span> · hace frío = <span class="wl md"></span> · he visto = <span class="wl md"></span></p>', apoyo="MODELO"))
P(actx("V.2", "Distinguir — sorteer per familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Sorteer: <span class="words"><b>el avión · hace sol · la maleta · nieva · el tren · el pasaporte</b></span></p>'
  + sortcols([("viajes",""),("clima",""),("transporte","")], eigen=False), apoyo="BANCO"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het Spaanse woord aan (beginletter gegeven). de koffer = <b>m</b>___ · het weer/de regen = <b>ll</b>___ · het vliegtuig = <b>a</b>___ · gedaan = <b>h</b>___<br><span class="wl full"></span></p>', apoyo="LETRA INICIAL"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p><i>verplichte-woorden-zin.</i> Maak één correcte zin met <b>he viajado · en tren · hace frío</b>.</p><div class="wbox sm"></div>', apoyo="SIN AYUDA"))
P(actx("V.5", "Comunicar — mi mejor viaje",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>vrije productie → transfer.</i> Schrijf drie zinnen over je beste reis met <b>he + participio</b> + het weer. Zeg het daarna hardop tegen je buur.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>', apoyo="MARCO (He ido a… · He visto… · Ha hecho…) → SIN AYUDA"))
P(mispal("Mis palabras de la unidad", 4))
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Sigue en la página digital:</span> <span class="g">flip cards (ES↔NL), audio en de 13 spellen bouwen de steun verder af.</span></div></div>')
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
   a.href=URL.createObjectURL(blob); a.download='U8_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Español en la práctica · U8 ¿Qué has hecho?</title><style>'
        + CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/U8.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes")
