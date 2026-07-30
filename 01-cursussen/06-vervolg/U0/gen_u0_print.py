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

AV = {n: C.make(n, "avatar", 64) for n in ["lucia", "diego", "valen", "nina", "mateo"]}
TU = C.tu_avatar(64)
MOCH = C.mochila(84, "map")

# ---------- CSS: identiek aan golden sample U0/U1/U4 (cursus-print.css + schrijf-componenten) ----------
CSS = FONTS + r"""
@page{ size:A4; margin:12mm 0; }
@page:first{ margin:0 0 12mm 0; }
*{ box-sizing:border-box; }
html{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }
:root{
 --g:#7C56A9; --gd:#5B3E83; --gt:#EEE8F5; --ink:#20242E; --mut:#6A6E78; --paper:#FCFBF8; --crema:#F3EEE4; --line:#E4E3DE; --line2:#CFCEC8; --red:#DC2626; --amber:#B7860B; --amberbg:#FBF3D6;
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
.editbar{ position:fixed; right:14px; bottom:14px; z-index:9999; display:flex; gap:8px; align-items:center; background:#5B3E83; color:#fff; padding:8px 12px; border-radius:12px; box-shadow:0 6px 20px #0004; font-family:'Inter',sans-serif; font-size:13px; }
.editbar button{ border:none; border-radius:8px; padding:7px 12px; font-weight:700; cursor:pointer; font-family:inherit; font-size:13px; }
.editbar .b1{ background:#fff; color:#5B3E83; } .editbar .b2{ background:#ffffff22; color:#fff; } .editbar.on{ background:#B7860B; }
body.editing [contenteditable="true"]{ outline:1.4px dashed #B7860B; outline-offset:2px; border-radius:3px; }
body.editing [contenteditable="true"]:focus{ outline:2px solid #5B3E83; background:#FEF9E7; }
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

# ================= BODY =================
import sys as _sys
_sys.path.insert(0, "/home/user/espa-ol-en-la-pr-ctica/03-build/web")
import print_bloques as PB
import nat_data as ND, lectura_data as LD, escucha_data as ED

BODY = []
def P(*x): BODY.extend(x)
_AN=[0]
def AN():
    _AN[0]+=1
    return str(_AN[0])

# ---------- OPENER ----------
P(f'''
<div class="hero">
  <div class="tab">U0 · ¡VOLVEMOS!</div>
  <div class="eyebrow">UNIDAD 0 · LA RUTA · EL REENCUENTRO 🧭</div>
  <h1>¡Volvemos!</h1>
  <div class="sub">Otra vez juntos. Ya sabes <b>mucho</b> español: vamos a <b>activarlo</b>. Hoy: opnieuw <b>hola</b> zeggen, jezelf <b>voorstellen</b>, en checken waar je staat met het <b>presente</b>, het <b>geslacht</b> en de <b>nationaliteiten</b>. <span class="gloss">We zijn er weer. Je kent al veel Spaans — we maken het weer wakker: begroeten, jezelf voorstellen, en je basis opfrissen.</span></div>
  <div class="q">¿Quién eres… otra vez? <span style="font-weight:400;opacity:.9">· Wie ben je… opnieuw?</span></div>
</div>
<div class="page">
  <div class="se">La Ruta · ¿dónde empezamos?</div>
  <div class="rutastrip">
    <div class="stop on"><div class="dot"></div><div class="lbl">U0 · Reencuentro</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U1 · El día a día</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U2 · Aquí vivo</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U3 · Conectados</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U4 · De viaje</div></div>
    <div class="stop"><div class="dot"></div><div class="lbl">U5–U7 · el pasado</div></div>
  </div>
  <div class="route-note">📍 <b>Punto de partida · el mundo hispano.</b> Antes de viajar, volvemos a mirar el mapa: <b>21 países</b> hablan español. Tú vienes de <b>Flandes</b> 🇧🇪 y ya conoces a la cast. En esta unidad <b>activamos</b> lo que ya sabes; en U1 empezamos el viaje de verdad. <span class="gloss">Vóór we vertrekken, kijken we opnieuw naar de kaart: 21 landen spreken Spaans. We activeren wat je al kent; in U1 begint de reis echt.</span></div>
  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> Después del verano, <b>volvemos</b> a clase de español. <b>Diego</b>, <b>Lucía</b>, <b>Valen</b> y <b>Nina</b> también vuelven — y tú viajas con ellos. Primero nos <b>presentamos</b> otra vez: «¿Cómo te llamas? ¿De dónde eres? ¿Cuántos años tienes?». Luego repasamos el <b>presente</b> y las <b>nacionalidades</b>. Así, todos — también los <b>nuevos</b> — empezamos juntos.
      <span class="gloss">Na de zomer keren we terug naar de Spaanse les. De cast komt ook terug — en jij reist mee. Eerst stellen we ons opnieuw voor, daarna frissen we het presente en de nationaliteiten op. Zo starten we samen — ook de nieuwe leerlingen.</span></div>
      <div class="ojo"><b>¡Ojo! — twee valstrikken meteen scherp:</b> «want» én «omdat» = <b>porque</b> (nooit <span class="trap">por que / porqué</span> hier). En «ik ben»: <b>soy</b> (wie/wat je bent: <i>soy belga</i>) tegenover <b>estoy</b> (waar/hoe: <i>estoy en clase, estoy bien</i>). <span class="gloss">porque = want/omdat · soy = permanent, estoy = plaats/gevoel.</span></div>
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
      <div class="moch"><div class="ic">{MOCH}</div><div><span class="hand">Mi mochila, otra vez</span><br><span class="gloss" style="font-size:8.5pt">Haal je rugzak weer boven: hola, me llamo, soy de…, tengo … años, ¿de dónde eres? — de woorden om opnieuw te starten.</span></div></div>
    </div>
  </div>
  <div class="obj" style="margin-top:6mm">
    <div class="se">En esta unidad vas a…</div>
    <ul>
      <li><span class="ck">☐</span><div><span class="es">saludar y presentarte</span> (formeel/informeel) <span class="nl">begroeten & jezelf voorstellen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">usar el presente</span> (regular + ser/estar/tener/ir…) <span class="nl">het presente gebruiken (herhaling)</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">concordar género y adjetivos</span> (el chico alto / la chica alta) <span class="nl">geslacht & bijvoeglijk nw. laten overeenkomen</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">hablar de países y nacionalidades</span> (soy de… / soy…) <span class="nl">landen & nationaliteiten</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">leer perfiles</span> y reaccionar <span class="nl">profielen lezen (Lectura)</span></div></li>
      <li><span class="ck">☐</span><div><span class="es">crear tu <b>tarjeta de reencuentro</b></span> y presentarte en pareja <span class="nl">je terugkeer-kaartje maken (eindtaak)</span></div></li>
    </ul>
  </div>
  <div class="mini">
    <div class="se">Ruta de la unidad</div>
    <div class="steps">
      <span><b>§1</b>Saludos</span><span><b>§2</b>El presente</span><span><b>§3</b>Género y adj.</span><span><b>§4</b>Países · números</span><span><b>§5</b>Lectura</span><span><b>Taller</b>Acentos/conect.</span><span><b>Cultura</b>Mundo hispano</span><span><b>Tarea</b>Tarjeta</span><span><b>Repaso</b>Semáforo</span>
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
</div>
''')

# ================= §1 · SALUDOS Y PRESENTACIONES =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">1</span><span class="pk">§1 · Saludos y presentaciones</span>')
P('<div class="intro"><b>ES:</b> Volvemos a empezar por lo más importante: <b>saludar</b> y <b>presentarte</b>. ¿Formal o informal? ¿tú o usted? <span class="gloss">We beginnen opnieuw bij het belangrijkste: begroeten en jezelf voorstellen. Formeel of informeel?</span></div>')
P(lpd(("9","mondelinge interactie: begroeten"),("4","luisteren: korte boodschappen"),("5","lezen: korte teksten")))
P('</div>')
P(obsbox([
  '👋 <span class="hl">Hola</span>, ¿qué tal? — Bien, ¿y tú?',
  '🤝 <span class="hl">Buenos días</span>. ¿Cómo se llama <b>usted</b>?',
  '🙋 Me <span class="hl">llamo</span> Nina. <span class="hl">Soy</span> de Perú y <span class="hl">tengo</span> dieciséis años.',
], vragen='¿Cuál es <b>informal</b> (amigos) y cuál es <b>formal</b> (usted)? ¿Qué tres verbos usamos para presentarnos? <span class="gloss">Welke is informeel/formeel? Welke drie werkwoorden gebruik je om je voor te stellen?</span>'))
P(regla("Regla", '<p><b>Informal</b> (amigos, clase) → <b>tú</b>: <i>¿Cómo estás? ¿De dónde eres?</i> · <b>Formal</b> (usted) → <i>¿Cómo está usted? ¿De dónde es?</i><br>Presentarte: <b>me llamo</b> … · <b>soy</b> (de) … · <b>tengo</b> … años · <b>vivo</b> en …</p>'))
P('<div class="se" style="margin-top:6mm">Modelo · diálogo de reencuentro <span class="gloss" style="font-size:8pt">— Diego ↔ tú, primer día de clase</span></div>')
P('<div class="chat">'
  '<div class="chatline you"><div class="who">Diego</div><div class="bub">¡Hola! ¿Qué tal el verano? Yo soy Diego, ¿y tú? ¿Cómo te llamas?</div></div>'
  '<div class="chatline me"><div class="who">Tú</div><div class="bub">¡Hola, Diego! Muy bien. Me llamo <b>_______</b> y soy de <b>_______</b>.</div></div>'
  '<div class="chatline you"><div class="who">Diego</div><div class="bub">¡Mucho gusto! ¿Cuántos años tienes?</div></div>'
  '<div class="chatline me"><div class="who">Tú</div><div class="bub">Tengo <b>_______</b> años. Y vivo en <b>_______</b>.</div></div>'
  '</div>')
P(audiorow('<div class="ic">🎧</div><div><b>Escucha</b> el diálogo completo en la página digital (TTS) y repite. Luego cierra el libro y salúdate con tu compañero/a. <b>Turnos:</b> saluda → preséntate → pregunta → despídete.</div>',
           qr("Escanea y escucha", "§1 · Diálogo", seed=11)))
P(actx(AN(), "Escucha y ordena la presentación",
  [{"t":"👂 Escuchar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Luister naar de presentatie van Nina en <b>nummer</b> de zinnen (1–5) in de juiste volgorde.</p>'
  '<p style="margin-left:12.5mm">___ Tengo dieciséis años. &nbsp; ___ ¡Hola! &nbsp; ___ Vivo en Cusco. &nbsp; ___ Me llamo Nina. &nbsp; ___ Soy de Perú.</p>', apoyo="MODELO (audio)"))
P(actx(AN(), "Entrevista a tu compañero/a",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p><i>interview con marcos de frase.</i> Vraag en noteer. Gebruik de zinsframes en vul de antwoorden aan.</p>'
  '<table class="alf"><thead><tr><th>Pregunta (marco)</th><th>Respuesta de tu compañero/a</th></tr></thead><tbody>'
  '<tr><td>¿Cómo te llamas?</td><td>Se llama <span class="wl md"></span></td></tr>'
  '<tr><td>¿De dónde eres?</td><td>Es de <span class="wl md"></span></td></tr>'
  '<tr><td>¿Cuántos años tienes?</td><td>Tiene <span class="wl sm"></span> años</td></tr>'
  '<tr><td>¿Dónde vives?</td><td>Vive en <span class="wl md"></span></td></tr></tbody></table>', apoyo="MARCO"))
P(actx(AN(), "Busca a alguien que… (encuesta)",
  [{"t":"🗣️ Interacción","skill":True},{"t":"👥 Clase"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p><i>zoek iemand die… — sta op en vraag rond.</i> Schrijf de naam van een klasgenoot bij elke zin. Vraag in het Spaans: «¿Tienes… ? ¿Eres… ?»</p>'
  '<table class="alf"><thead><tr><th>Busca a alguien que…</th><th>Nombre</th><th>Dato extra</th></tr></thead><tbody>'
  '<tr><td>…tiene un hermano o una hermana</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>…es de otro país / otra ciudad</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>…habla tres lenguas</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>…vive cerca del instituto</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>', apoyo="SIN AYUDA"))
P(actx(AN(), "Completa la presentación",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>gap-fill (uit het banco).</i> Vul de voorstelling aan met: <span class="words"><b>me llamo · soy · tengo · hablo · vivo · estudio</b></span></p>'
  '<p style="margin-left:12.5mm">¡Hola! <span class="wl sm"></span> Marta. <span class="wl sm"></span> de Amberes. <span class="wl sm"></span> 16 años.<br>'
  '<span class="wl sm"></span> neerlandés y un poco de español. <span class="wl sm"></span> en Gante y <span class="wl sm"></span> en el colegio.</p>', apoyo="BANCO"))
P('<div class="regla" style="margin-top:6mm"><span class="tag">Mi modelo</span><p>Prepara tu presentación: <b>Hola, me llamo</b> <span class="wl md"></span> <b>. Soy de</b> <span class="wl md"></span> <b>y tengo</b> <span class="wl sm"></span> <b>años. Vivo en</b> <span class="wl md"></span> <b>. Soy</b> <span class="wl md"></span> (carácter) <b>y hablo</b> <span class="wl md"></span> <b>. ¡Mucho gusto!</b></p></div>')
P('<div class="guide"><div class="ic">🔗</div><div><span class="hand">Juego · cadena de nombres:</span> <span class="g">en círculo, cada persona repite a los anteriores y se añade: «Ella es Nina, él es Diego y yo soy…». ¡No pierdas el hilo!</span></div></div>')
P('<h3 style="margin-top:7mm">Suena bien · tres sonidos del español</h3>')
P('<p style="font-size:9.6pt">Antes de grabar, repasa la <b>pronunciación</b>. Escucha en la web y <b>repite</b> (shadowing). Estos sonidos son típicos:</p>')
P('<div class="fams three" style="margin-top:2mm">'
  '<div class="pcard"><div class="t">j · g+e/i</div><div class="ej">Gijón · jamón · gente</div><div class="t2">≈ NL «ch» van <i>lachen</i></div></div>'
  '<div class="pcard"><div class="t">ñ</div><div class="ej">España · niño · mañana</div><div class="t2">≈ NL «nj» van <i>oranje</i></div></div>'
  '<div class="pcard"><div class="t">ll · y</div><div class="ej">me llamo · yo · ella</div><div class="t2">≈ NL «j» van <i>jas</i></div></div>'
  '<div class="pcard"><div class="t">c+e/i · z</div><div class="ej">gracias · cinco · plaza</div><div class="t2">≈ scherpe «s» (of Castiliaanse «th»)</div></div>'
  '<div class="pcard"><div class="t">ca/co/cu · que/qui</div><div class="ej">casa · queso · aquí</div><div class="t2">harde «k»; «qu» = k</div></div>'
  '<div class="pcard"><div class="t">r · rr · h · v</div><div class="ej">pero/perro · hola (h zwijgt) · vivo (v≈b)</div><div class="t2">rr = rollende r; h stom; v klinkt als b</div></div></div>')
P(actx(AN(), "Clasifica el sonido",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p>Waar hoor je de <b>«ch»-klank</b> (j / g+e,i) en waar de <b>«k»-klank</b> (c+a/o/u · qu)? Sorteer: <span class="words"><b>gente · casa · jamón · queso · Gijón · aquí</b></span></p>'
  + sortcols([("«ch» (j · ge/gi)",""),("«k» (ca/co/cu · qu)","")], eigen=False), apoyo="BANCO"))
P('<div class="se" style="margin-top:5mm">Deletrea tu nombre <span class="gloss" style="font-size:8pt">— schrijf hoe je je naam spelt in het Spaans (a · be · ce · de…)</span></div>')
P('<p style="margin-left:0"><span class="wl full"></span></p>')
P(audiorow('<div class="ic">🔊</div><div><b>Escucha y repite</b> el alfabeto y los saludos en la web. Luego <b>graba tu presentación</b> (mensaje de voz, 20–30 s): saluda, di tu nombre, edad, de dónde eres y dónde vives. Escúchate y repite mejor.</div>',
           qr("Escanea · shadowing + graba", "§1 · Suena bien / Preséntate", seed=12)))
P('</div>')  # page §1

# ================= §2 · EL PRESENTE =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2 · El presente — el motor</span>')
P('<div class="intro"><b>ES:</b> El <b>presente</b> es el motor de todo. Es la <b>base</b>: aquí entrenamos <b>mucho</b>. Primero los <b>regulares</b> (-ar/-er/-ir), luego <b>ser</b>, luego los <b>irregulares clave</b>. <span class="gloss">Het presente is de basis — hier oefenen we véél: eerst de regelmatige werkwoorden, dan ser, dan de belangrijkste onregelmatige.</span></div>')
P(lpd(("8","taalsysteem: het presente (regelmatig + onregelmatig)"),("3","informatie geven over jezelf")))
P('</div>')

# ---------- §2.1 Los regulares ----------
P('<h3>§2.1 · Los regulares — raíz + terminación</h3>')
P('<p style="font-size:9.6pt">Un verbo regular = <b>raíz</b> (verandert niet) + <b>terminación</b> (verandert met de persoon):</p>')
P(machine([("infinitivo","hablar"),("raíz","habl-"),("+ terminación (yo)","habl-o")]))
P('<table class="conj"><thead><tr><th>—</th><th>hablar (-ar)</th><th>comer (-er)</th><th>vivir (-ir)</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">habl<span class="end">o</span></td><td class="v">com<span class="end">o</span></td><td class="v">viv<span class="end">o</span></td></tr>'
  '<tr><td class="p">tú</td><td class="v">habl<span class="end">as</span></td><td class="v">com<span class="end">es</span></td><td class="v">viv<span class="end">es</span></td></tr>'
  '<tr><td class="p">él/ella/usted</td><td class="v">habl<span class="end">a</span></td><td class="v">com<span class="end">e</span></td><td class="v">viv<span class="end">e</span></td></tr>'
  '<tr><td class="p">nosotros/as</td><td class="v">habl<span class="end">amos</span></td><td class="v">com<span class="end">emos</span></td><td class="v">viv<span class="end">imos</span></td></tr>'
  '<tr><td class="p">vosotros/as</td><td class="v">habl<span class="end">áis</span></td><td class="v">com<span class="end">éis</span></td><td class="v">viv<span class="end">ís</span></td></tr>'
  '<tr><td class="p">ellos/as/ustedes</td><td class="v">habl<span class="end">an</span></td><td class="v">com<span class="end">en</span></td><td class="v">viv<span class="end">en</span></td></tr></tbody></table>')
P('<div class="se" style="margin-top:4mm">Verbos frecuentes <span class="gloss" style="font-size:8pt">— uit de oude cursus</span></div>')
P('<div class="clusters" style="grid-template-columns:1fr 1fr 1fr">'
  '<div class="clu"><div class="ch">-ar</div><ul><li>hablar (spreken)</li><li>estudiar (studeren)</li><li>trabajar (werken)</li><li>escuchar (luisteren)</li><li>comprar (kopen)</li></ul></div>'
  '<div class="clu"><div class="ch">-er</div><ul><li>comer (eten)</li><li>beber (drinken)</li><li>leer (lezen)</li><li>aprender (leren)</li><li>comprender (begrijpen)</li></ul></div>'
  '<div class="clu"><div class="ch">-ir</div><ul><li>vivir (wonen)</li><li>escribir (schrijven)</li><li>abrir (openen)</li><li>recibir (ontvangen)</li><li>subir (omhoog)</li></ul></div></div>')
P(actx(AN(), "Práctica rápida · las terminaciones",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>vul de uitgangen aan uit het hoofd.</i></p>'
  '<table class="alf"><thead><tr><th>—</th><th>-ar · trabajar</th><th>-er · comer</th><th>-ir · escribir</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td>trabaj<b>__</b></td><td>com<b>__</b></td><td>escrib<b>__</b></td></tr>'
  '<tr><td class="p">tú</td><td>trabaj<b>__</b></td><td>com<b>__</b></td><td>escrib<b>__</b></td></tr>'
  '<tr><td class="p">nosotros</td><td>trabaj<b>__</b></td><td>com<b>__</b></td><td>escrib<b>__</b></td></tr>'
  '<tr><td class="p">ellos</td><td>trabaj<b>__</b></td><td>com<b>__</b></td><td>escrib<b>__</b></td></tr></tbody></table>', apoyo="MODELO (tabla arriba)"))
P(actx(AN(), "Completa (cloze) · verbos regulares",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>traditionele cloze.</i> Vul het werkwoord in het presente in (infinitivo tussen haakjes).</p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl sm"></span> (hablar) español. &nbsp; 2. ¿Tú <span class="wl sm"></span> (vivir) en Gante? &nbsp; 3. Nosotros <span class="wl sm"></span> (estudiar) mucho.<br>'
  '4. Ella <span class="wl sm"></span> (comer) a las dos. &nbsp; 5. Vosotros <span class="wl sm"></span> (escribir) un correo. &nbsp; 6. Ellos <span class="wl sm"></span> (trabajar) aquí.<br>'
  '7. Yo <span class="wl sm"></span> (leer) un libro. &nbsp; 8. ¿Tú <span class="wl sm"></span> (escuchar) música?</p>', apoyo="BANCO: hablo · vives · estudiamos · come · escribís · trabajan · leo · escuchas"))
P(actx(AN(), "¿Quién hace qué? · relaciona sujeto y forma",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>koppel elk onderwerp aan de juiste vorm (schrijf de letter). Uit de oude cursus.</i></p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Sujeto</div><div class="cb short">1. Yo &nbsp; 2. Mis abuelos &nbsp; 3. Tú &nbsp; 4. Mi hermana &nbsp; 5. Nosotros</div></div>'
  '<div class="wcol"><div class="ch">Forma</div><div class="cb short">a. comes pizza &nbsp; b. soy estudiante &nbsp; c. vive en Madrid &nbsp; d. hablamos dos lenguas &nbsp; e. viven en el campo</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span> 5-<span class="wl sm"></span></p>', apoyo="SIN AYUDA"))
P('</div>')  # page §2.1

# ---------- §2.2 El verbo ser ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2.2 · El verbo «ser»</span>')
P('<div class="intro"><b>ES:</b> <b>ser</b> es irregular y muy importante: para decir <b>quién eres</b>, <b>de dónde eres</b> y <b>a qué te dedicas</b>. <span class="gloss">ser gebruik je om te zeggen wie je bent, waar je vandaan komt en wat je doet.</span></div>')
P('</div>')
P(regla("ser · irregular · memorízalo", '<table class="conj" style="margin-top:1mm"><thead><tr><th>Singular</th><th></th><th>Plural</th><th></th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">soy</td><td class="p">nosotros/as</td><td class="v">somos</td></tr>'
  '<tr><td class="p">tú</td><td class="v">eres</td><td class="p">vosotros/as</td><td class="v">sois</td></tr>'
  '<tr><td class="p">él/ella/usted</td><td class="v">es</td><td class="p">ellos/ustedes</td><td class="v">son</td></tr></tbody></table>'
  '<p style="margin:2mm 0 0">soy de… <i>(origen)</i> · soy belga <i>(nacionalidad)</i> · soy estudiante <i>(profesión)</i></p>'))
P(actx(AN(), "Completa con «ser»",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>uit de oude cursus.</i> Vul de zinnen aan met de juiste vorm van <b>ser</b>.</p>'
  '<p style="margin-left:12.5mm">Yo <span class="wl sm"></span> de Bélgica. &nbsp; Tú <span class="wl sm"></span> español. &nbsp; María <span class="wl sm"></span> profesora.<br>'
  'Nosotros <span class="wl sm"></span> estudiantes. &nbsp; Vosotros <span class="wl sm"></span> de Madrid. &nbsp; Ellos <span class="wl sm"></span> italianos.</p>', apoyo="MODELO (tabla)"))
P(actx(AN(), "Conjuga «ser» · completa la tabla",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 2 min"},{"t":"★☆☆"}],
  '<p><i>vul de tabel uit het hoofd in.</i></p>'
  '<table class="alf"><tbody>'
  '<tr><td class="p">yo</td><td><span class="wl sm"></span></td><td class="p">nosotros/as</td><td><span class="wl sm"></span></td></tr>'
  '<tr><td class="p">tú</td><td><span class="wl sm"></span></td><td class="p">vosotros/as</td><td><span class="wl sm"></span></td></tr>'
  '<tr><td class="p">él/ella</td><td><span class="wl sm"></span></td><td class="p">ellos/as</td><td><span class="wl sm"></span></td></tr></tbody></table>', apoyo="SIN AYUDA"))
P('<div class="truc"><b>¡Ojo! soy ↔ estoy:</b> <b>soy</b> = wie/wat je bent (<i>soy belga, soy estudiante</i>) · <b>estoy</b> = waar/hoe je bent (<i>estoy en clase, estoy bien</i>). <span class="gloss">Het volledige ser/estar-contrast komt in U1.</span></div>')
P(actx(AN(), "¿soy o estoy?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>kies (soy = identiteit · estoy = plaats/gevoel).</i></p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl sm"></span> de Bélgica. &nbsp; 2. Yo <span class="wl sm"></span> en clase. &nbsp; 3. <span class="wl sm"></span> estudiante. &nbsp; 4. Hoy <span class="wl sm"></span> contento/a. &nbsp; 5. <span class="wl sm"></span> alto/a. &nbsp; 6. <span class="wl sm"></span> bien, gracias.</p>', apoyo="PISTA"))
P(actx(AN(), "★ Tarea comunicativa · entrevista",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p><i>afzender·ontvanger·doel·situatie·resultaat.</i> Interview je buur en noteer met de <b>3ª persona</b> (él/ella). Gebruik ser + regelmatige werkwoorden.</p>'
  '<p style="margin-left:12.5mm">Se llama <span class="wl md"></span> · Es de <span class="wl md"></span> · Habla <span class="wl md"></span> · Estudia/trabaja <span class="wl md"></span></p>', apoyo="MARCO"))
P('</div>')  # page §2.2

# ---------- §2.3 Los otros irregulares clave ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2.3 · Los otros irregulares clave</span>')
P('<div class="intro"><b>ES:</b> Seis verbos irregulares que usas cada día: <b>estar · tener · ir · hacer · venir · dar</b>. Fíjate en la forma de <b>yo</b>. <span class="gloss">Zes dagelijkse onregelmatige werkwoorden — let op de yo-vorm.</span></div>')
P('</div>')
P(obsbox([
  'Yo est<span class="hl">oy</span> · yo v<span class="hl">oy</span> · yo d<span class="hl">oy</span>',
  'Yo ten<span class="hl">go</span> · yo ha<span class="hl">go</span> · yo ven<span class="hl">go</span>',
], vragen='¿Qué tienen en común las formas de <b>yo</b>? <span class="gloss">Tip: veel eindigen op <b>-oy</b> of <b>-go</b> — een handig geheugensteuntje!</span>'))
P('<div class="fams" style="grid-template-columns:1fr 1fr;margin-top:3mm">'
  '<div><table class="conj"><thead><tr><th>—</th><th>estar</th><th>tener</th><th>ir</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">estoy</td><td class="v">tengo</td><td class="v">voy</td></tr>'
  '<tr><td class="p">tú</td><td class="v">estás</td><td class="v">tienes</td><td class="v">vas</td></tr>'
  '<tr><td class="p">él/ella</td><td class="v">está</td><td class="v">tiene</td><td class="v">va</td></tr>'
  '<tr><td class="p">nosotros</td><td class="v">estamos</td><td class="v">tenemos</td><td class="v">vamos</td></tr>'
  '<tr><td class="p">vosotros</td><td class="v">estáis</td><td class="v">tenéis</td><td class="v">vais</td></tr>'
  '<tr><td class="p">ellos</td><td class="v">están</td><td class="v">tienen</td><td class="v">van</td></tr></tbody></table></div>'
  '<div><table class="conj"><thead><tr><th>—</th><th>hacer</th><th>venir</th><th>dar</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">hago</td><td class="v">vengo</td><td class="v">doy</td></tr>'
  '<tr><td class="p">tú</td><td class="v">haces</td><td class="v">vienes</td><td class="v">das</td></tr>'
  '<tr><td class="p">él/ella</td><td class="v">hace</td><td class="v">viene</td><td class="v">da</td></tr>'
  '<tr><td class="p">nosotros</td><td class="v">hacemos</td><td class="v">venimos</td><td class="v">damos</td></tr>'
  '<tr><td class="p">vosotros</td><td class="v">hacéis</td><td class="v">venís</td><td class="v">dais</td></tr>'
  '<tr><td class="p">ellos</td><td class="v">hacen</td><td class="v">vienen</td><td class="v">dan</td></tr></tbody></table></div></div>')
P('<div class="truc"><b>tener</b> in vaste uitdrukkingen: <b>tengo … años</b> (leeftijd) · <b>tengo hambre/sed</b> (honger/dorst) · <b>tengo un hermano</b> (bezit).</div>')
P(actx(AN(), "Completa con el presente (cloze) · irregulares",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>de grote werkwoord-cloze.</i> Vul in het presente in (infinitivo tussen haakjes).</p>'
  '<p style="margin-left:12.5mm">1. Yo <span class="wl sm"></span> (estar) muy bien. &nbsp; 2. Nina <span class="wl sm"></span> (tener) 16 años. &nbsp; 3. Diego <span class="wl sm"></span> (ir) al mercado.<br>'
  '4. ¿Vosotros <span class="wl sm"></span> (hacer) los deberes? &nbsp; 5. Ellos <span class="wl sm"></span> (venir) de México. &nbsp; 6. Yo <span class="wl sm"></span> (hacer) mis deberes.<br>'
  '7. Nosotros <span class="wl sm"></span> (tener) hambre. &nbsp; 8. ¿Tú <span class="wl sm"></span> (ir) al instituto en bici?</p>', apoyo="BANCO: estoy · tiene · va · hacéis · vienen · hago · tenemos · vas"))
P(actx(AN(), "Sustitución · cambia la persona",
  [{"t":"🔁 Practicar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>substitutietabel.</i> Herschrijf <b>Yo tengo un hermano y voy al instituto</b> voor elke persoon.</p>'
  '<table class="alf"><thead><tr><th>Persona</th><th>Frase</th></tr></thead><tbody>'
  '<tr><td class="p">tú</td><td>Tú <span class="wl lg"></span></td></tr>'
  '<tr><td class="p">ella</td><td>Ella <span class="wl lg"></span></td></tr>'
  '<tr><td class="p">nosotros</td><td>Nosotros <span class="wl lg"></span></td></tr>'
  '<tr><td class="p">ellos</td><td>Ellos <span class="wl lg"></span></td></tr></tbody></table>', apoyo="MARCO"))
P(actx(AN(), "Cadena de transformación · yo → …",
  [{"t":"🔁 Practicar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>transformatieketting.</i> Eén verandering per stap. Begin: <b>Yo hago deporte.</b></p>'
  '<p style="margin-left:12.5mm">Yo hago deporte → tú <span class="wl md"></span> → nosotros <span class="wl md"></span> → ellos <span class="wl md"></span> → ella <span class="wl md"></span></p>', apoyo="LETRA (haces…)"))
P(actx(AN(), "Clínica de errores · busca y corrige",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★★★"}],
  '<p><i>foutenkliniek.</i> Elke zin heeft één fout in het werkwoord. Streep door en verbeter.</p>'
  '<p style="margin-left:12.5mm">1. Yo <b>es</b> de Bélgica. → <span class="wl md"></span><br>'
  '2. Nosotros <b>tenemos</b> quince años y ella <b>teno</b> catorce. → <span class="wl md"></span><br>'
  '3. ¿De dónde <b>vienís</b> vosotros? → <span class="wl md"></span><br>'
  '4. Ellos <b>va</b> al mercado. → <span class="wl md"></span></p>', apoyo="PISTA (kijk naar de persoon)"))
P(actx(AN(), "Escribe sobre ti · producción",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>vrije productie.</i> Schrijf 4 zinnen over jezelf met <b>ser · tener · vivir · hacer/ir</b> (elk minstens één keer).</p><div class="wbox sm"></div>', apoyo="SIN AYUDA"))
P(actx(AN(), "Pregunta y responde · en pareja",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>vraag-antwoord-spiegel.</i> Stel de vraag en antwoord met de juiste vorm. Noteer het antwoord van je buur.</p>'
  '<table class="alf"><thead><tr><th>Pregunta</th><th>Respuesta (tu compañero/a)</th></tr></thead><tbody>'
  '<tr><td>¿De dónde eres?</td><td>Soy de <span class="wl md"></span></td></tr>'
  '<tr><td>¿Cuántos años tienes?</td><td>Tengo <span class="wl sm"></span> años</td></tr>'
  '<tr><td>¿Qué lenguas hablas?</td><td>Hablo <span class="wl md"></span></td></tr>'
  '<tr><td>¿Cómo vas al instituto?</td><td>Voy <span class="wl md"></span></td></tr>'
  '<tr><td>¿Qué haces los fines de semana?</td><td>Hago <span class="wl md"></span></td></tr></tbody></table>', apoyo="MARCO"))
P(actx(AN(), "Dictado corto · escribe las frases",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>microdictee.</i> Luister en schrijf de vijf zinnen (met correct vervoegde werkwoorden).</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span>4. <span class="wl full"></span>5. <span class="wl full"></span></p>', apoyo="SIN AYUDA (docent leest voor)"))
P('<div class="guide"><div class="ic">🎡</div><div><span class="hand">Online:</span> <span class="g">de <b>rueda de conjugación</b> en de <b>Conjugador</b> geven je elk werkwoord in presente; + cloze-, substitutie- en tetris-spellen om de vormen te automatiseren.</span></div></div>')
P('</div>')  # page §2.3

# ================= §3 · GÉNERO, ARTÍCULOS Y NÚMERO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3 · Género · artículos · número · adjetivos</span>')
P('<div class="intro"><b>ES:</b> En español todo tiene <b>género</b> (m/v) y <b>número</b> (ev/mv). El <b>artículo</b> y el <b>adjetivo</b> tienen que <b>concordar</b>. <span class="gloss">Alles heeft een geslacht én getal; lidwoord én bijvoeglijk nw. moeten overeenkomen.</span></div>')
P(lpd(("8","taalsysteem: genus, getal & congruentie"),("7","woordenschat: personen")))
P('</div>')

# ---------- §3.1 El género ----------
P('<h3>§3.1 · El género — masculino / femenino</h3>')
P('<p style="font-size:9.6pt">Veel woorden maken <b>-o</b> (m) → <b>-a</b> (v). Het lidwoord verandert mee: <b>el/un</b> ↔ <b>la/una</b>.</p>')
P(zoom("masculino", "el / un chico", "femenino", "la / una chica"))
P('<div class="fams" style="grid-template-columns:1fr 1fr;margin-top:3mm">'
  '<div class="pcard"><div class="t" style="font-size:10.5pt">Masculino · el</div>'
  '<div class="ej" style="margin-top:1mm">el niño · el chico · el amigo · el hermano · el abuelo · el hijo</div></div>'
  '<div class="pcard"><div class="t" style="font-size:10.5pt">Femenino · la</div>'
  '<div class="ej" style="margin-top:1mm">la niña · la chica · la amiga · la hermana · la abuela · la hija</div></div></div>')
P('<div class="truc"><b>¡Ojo!</b> niet alles volgt -o/-a: <b>el padre / la madre</b> · <b>el hombre / la mujer</b>. En valstrikken: <b>el</b> problema · <b>el</b> día · <b>el</b> mapa (m ondanks -a) · <b>la</b> mano · <b>la</b> foto (v ondanks -o). <span class="gloss">Deze uit het hoofd leren.</span></div>')
P(actx(AN(), "Clasifica: el / la",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>patroon sorteren.</i> Zet het juiste lidwoord ervoor: <span class="words"><b>libro · casa · problema · mano · ciudad · mapa · día · foto</b></span></p>'
  + sortcols([("el (masculino)",""),("la (femenino)","")], eigen=True), apoyo="BANCO"))
P(actx(AN(), "Escribe la forma que falta (m ↔ f)",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>uit de oude cursus.</i> Schrijf de ontbrekende vorm.</p>'
  '<p style="margin-left:12.5mm">el amigo → la <span class="wl sm"></span> &nbsp; la niña → el <span class="wl sm"></span> &nbsp; la abuela → el <span class="wl sm"></span><br>'
  'el primo → la <span class="wl sm"></span> &nbsp; la madre → el <span class="wl sm"></span> &nbsp; el hombre → la <span class="wl sm"></span></p>', apoyo="PISTA (-o/-a of memoriseren)"))
P('</div>')  # page §3.1

# ---------- §3.2 El número ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3.2 · El número — el plural</span>')
P('<div class="intro"><b>ES:</b> Van enkelvoud naar meervoud, en het lidwoord wordt <b>los/las</b>. <span class="gloss">Meervoud vormen — en el/la wordt los/las.</span></div>')
P('</div>')
P(regla("Regla · el plural", '<p>Eindigt op een <b>klinker</b> → <b>+ s</b>: chico → chic<b>os</b> · casa → cas<b>as</b>.<br>'
  'Eindigt op een <b>medeklinker</b> → <b>+ es</b>: profesor → profesor<b>es</b> · ciudad → ciudad<b>es</b>.<br>'
  'Eindigt op <b>-z</b> → <b>-ces</b>: lápiz → lápi<b>ces</b> · vez → ve<b>ces</b>.<br>'
  '<span class="gloss">el/un → los/unos · la/una → las/unas.</span></p>'))
P(actx(AN(), "Escribe el plural con su artículo",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>uit de oude cursus.</i> Schrijf het meervoud met los/las.</p>'
  '<p style="margin-left:12.5mm">el chico → <span class="wl md"></span> &nbsp; la amiga → <span class="wl md"></span> &nbsp; el profesor → <span class="wl md"></span><br>'
  'la ciudad → <span class="wl md"></span> &nbsp; el lápiz → <span class="wl md"></span> &nbsp; la foto → <span class="wl md"></span></p>', apoyo="MODELO (regla)"))
P(actx(AN(), "Cadena · singular → plural",
  [{"t":"🔁 Practicar","skill":True},{"t":"👥 En parejas"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>transformatieketting.</i> Zet de hele groep in het meervoud (artículo + sustantivo + adjetivo).</p>'
  '<p style="margin-left:12.5mm">el amigo simpático → <span class="wl lg"></span><br>'
  'la casa blanca → <span class="wl lg"></span><br>'
  'la ciudad grande → <span class="wl lg"></span></p>', apoyo="LETRA (los amigos…)"))
P('</div>')  # page §3.2

# ---------- §3.3 Los adjetivos ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3.3 · Los adjetivos — concordancia y lugar</span>')
P('<div class="intro"><b>ES:</b> El adjetivo <b>concuerda</b> (m/v · ev/mv) y va <b>después</b> del sustantivo. <span class="gloss">Het bijvoeglijk nw. komt overeen én staat meestal ná het zelfstandig nw.</span></div>')
P('</div>')
P('<div class="agree"><div class="w">el chic<u>o</u> alt<u>o</u></div><div class="tie">m ev → -o … -o</div></div>')
P('<div class="agree"><div class="w">las chic<u>as</u> alt<u>as</u></div><div class="tie">v mv → -as … -as</div></div>')
P(regla("Regla · concordancia + lugar", '<p>Het <b>adjectief</b> volgt het zelfstandig nw. in <b>geslacht</b> én <b>getal</b> en staat er meestal <b>achter</b>: <i>una chica <b>simpática</b>, unos libros <b>rojos</b></i>.<br>'
  'Adjectieven op <b>-e</b> of medeklinker veranderen niet voor m/v: <i>alegre, azul, difícil</i> (wel +s/-es in het meervoud).<br>'
  '<b>Apócope:</b> <b>bueno→buen</b>, <b>malo→mal</b>, <b>grande→gran</b> vóór het zelfstandig nw.: <i>un <b>buen</b> amigo, una <b>gran</b> ciudad</i>.</p>'))
P(vpairs([("el profesor","la profe<b>sora</b>"),("simpático","simpátic<b>a</b>"),("trabajador","trabajador<b>a</b>"),("alemán","aleman<b>a</b>"),("alegre","alegre <i>(=)</i>"),("azul","azul <i>(=)</i>")]))
P(actx(AN(), "Concordancia · completa la terminación",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>gap-fill.</i> Vul lidwoord + uitgang aan zodat alles overeenkomt.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl sm"></span> chica es simpátic<b>__</b>. &nbsp; 2. Los libros son roj<b>__</b>. &nbsp; 3. <span class="wl sm"></span> profesoras son trabajador<b>__</b>.<br>'
  '4. Mi amig<b>__</b> Nina es peruan<b>__</b>. &nbsp; 5. Es un <b>buen/bueno</b> amigo. &nbsp; 6. <span class="wl sm"></span> problema es difícil.</p>', apoyo="PISTA (m/v · ev/mv)"))
P(actx(AN(), "Une con flechas · nombre ↔ adjetivo",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👥 En parejas"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>overeenkomst-pijlen / grammaticale paren.</i> Verbind elk zelfstandig nw. met het passende adjectief (let op m/v/getal) en schrijf de 4 combinaties.</p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">Sustantivo</div><div class="cb short">las casas · el coche · la mochila · los perros</div></div>'
  '<div class="wcol"><div class="ch">Adjetivo</div><div class="cb short">blancas · nuevo · roja · pequeños</div></div></div>'
  '<p style="margin-left:12.5mm" class="gloss">↳ <span class="wl full"></span></p>', apoyo="SIN AYUDA"))
P(actx(AN(), "¿Correcto o no? · voorbeeld / niet-voorbeeld",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★★"}],
  '<p><i>vink aan: klopt de concordancia? Verbeter waar nodig.</i></p>'
  '<p style="margin-left:12.5mm">☐ una chica simpático → <span class="wl md"></span><br>'
  '☐ los libros rojos → <span class="wl sm"></span> (✔/✘)<br>'
  '☐ un gran problema → <span class="wl sm"></span> (✔/✘)<br>'
  '☐ las casa blancas → <span class="wl md"></span></p>', apoyo="SIN AYUDA"))
P(actx(AN(), "Describe · tres personas de la clase",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>vrije productie met concordancia.</i> Schrijf voor drie klasgenoten een zin met artículo + sustantivo + <b>twee</b> adjectieven die overeenkomen (m/v · ev/mv).</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>'
  '<p style="margin-left:12.5mm" class="gloss">Modelo: <i>Lucía es una chica alta y simpática.</i></p>', apoyo="MARCO → SIN AYUDA"))
P('</div>')  # page §3.3

# ================= §4 · PAÍSES, NACIONALIDADES Y LENGUAS =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4 · Países · nacionalidades · lenguas</span>')
P('<div class="intro"><b>ES:</b> Para decir <b>de dónde eres</b>: <b>Soy de + país</b> (Soy de Bélgica) · <b>Soy + nacionalidad</b> (Soy belga). La nacionalidad <b>concuerda</b> (m/v · ev/mv). <span class="gloss">Waar kom je vandaan? De nationaliteit komt overeen met geslacht/getal — concordancia in actie.</span></div>')
P(lpd(("7","woordenschat: landen & nationaliteiten"),("8","taalsysteem: concordancia van gentilicios"),("5","cultuur: de wereld")))
P('</div>')
P('<div class="se">El mundo · países y gentilicios <span class="gloss" style="font-size:8pt">— overgenomen & uitgebreid uit de oude cursus</span></div>')
P('<div class="fams three" style="margin-top:2mm">'
  '<div class="pcard"><div class="t" style="font-size:10pt">Europa 🇪🇺</div><div class="ej" style="margin-top:1mm">España → español/a · Alemania → alemán/-ana · Francia → francés/-esa · Italia → italiano/a · Reino Unido → inglés/-esa · <b>Bélgica → belga</b></div></div>'
  '<div class="pcard"><div class="t" style="font-size:10pt">América 🌎</div><div class="ej" style="margin-top:1mm">México → mexicano/a · Colombia → colombiano/a · Perú → peruano/a · Argentina → argentino/a · Chile → chileno/a · EE. UU. → estadounidense</div></div>'
  '<div class="pcard"><div class="t" style="font-size:10pt">Otros continentes 🌍</div><div class="ej" style="margin-top:1mm">China → chino/a · Japón → japonés/-esa · Marruecos → marroquí · Egipto → egipcio/a · Australia → australiano/a · Canadá → canadiense</div></div></div>')
P('<div class="se" style="margin-top:5mm">El patrón del género <span class="gloss" style="font-size:8pt">— zo verandert de nationaliteit</span></div>')
P('<table class="alf"><thead><tr><th>Patrón</th><th>Masculino</th><th>Femenino</th><th>Ejemplo (país)</th></tr></thead><tbody>'
  '<tr><td><b>-o / -a</b></td><td>italian<b>o</b></td><td>italian<b>a</b></td><td class="gloss">Italia</td></tr>'
  '<tr><td><b>-és / -esa</b></td><td>franc<b>és</b></td><td>franc<b>esa</b></td><td class="gloss">Francia</td></tr>'
  '<tr><td><b>-ense</b></td><td>estadounid<b>ense</b></td><td>estadounid<b>ense</b></td><td class="gloss">EE. UU. (=)</td></tr>'
  '<tr><td><b>invariable</b></td><td>belga · marroquí</td><td>belga · marroquí</td><td class="gloss">Bélgica · Marruecos (=)</td></tr></tbody></table>')
P('<div class="truc"><b>Nacionalidad = idioma:</b> de taal heeft meestal dezelfde vorm als de mannelijke nationaliteit: <i>Soy español → Hablo español.</i> <b>¡Ojo!</b> in Bélgica: <b>neerlandés</b> y <b>francés</b> (niet «belga»); in Brasil: <b>portugués</b>. En nationaliteiten met <b>kleine letter</b> (español, no <span class="trap">Español</span>), landen met hoofdletter.</div>')
P(actx(AN(), "¿De dónde son? · completa con la nacionalidad",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>uit de oude cursus — ¡cuidado con el género!</i> Let op m/v.</p>'
  '<p style="margin-left:12.5mm">María es de España → es <span class="wl md"></span> &nbsp; Tom es de Bélgica → es <span class="wl md"></span><br>'
  'Hans es de Alemania → es <span class="wl md"></span> &nbsp; Sophie es de Francia → es <span class="wl md"></span><br>'
  'Los chicos son de México → son <span class="wl md"></span> &nbsp; Las chicas son de Perú → son <span class="wl md"></span></p>', apoyo="PISTA (patrón + género)"))
P(actx(AN(), "Une país y nacionalidad",
  [{"t":"🔗 Emparejar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p><i>matching.</i> Verbind (schrijf de letter).</p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">País</div><div class="cb short">1. Colombia &nbsp; 2. Alemania &nbsp; 3. Italia &nbsp; 4. Francia &nbsp; 5. Marruecos</div></div>'
  '<div class="wcol"><div class="ch">Nacionalidad</div><div class="cb short">a. alemán &nbsp; b. marroquí &nbsp; c. colombiano &nbsp; d. italiano &nbsp; e. francés</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span> 5-<span class="wl sm"></span></p>', apoyo="SIN AYUDA"))
P(actx(AN(), "Concordancia de la nacionalidad · la tabla",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>substitutietabel.</i> Vul de vier vormen aan (m ev · v ev · m mv · v mv).</p>'
  '<table class="alf"><thead><tr><th>País</th><th>m. ev.</th><th>v. ev.</th><th>m. mv.</th><th>v. mv.</th></tr></thead><tbody>'
  '<tr><td>México</td><td>mexicano</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>Francia</td><td><span class="wl sm"></span></td><td>francesa</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>Bélgica</td><td>belga</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>', apoyo="PISTA (patrón)"))
P(actx(AN(), "Dictado de números y datos",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>luisteren en noteren.</i> Luister naar de docent/audio en schrijf getallen en gegevens op.</p>'
  '<p style="margin-left:12.5mm">a) edad: <span class="wl sm"></span> &nbsp; b) teléfono: <span class="wl md"></span> &nbsp; c) año: <span class="wl sm"></span> &nbsp; d) código postal: <span class="wl sm"></span></p>', apoyo="MODELO (audio)"))
P(actx(AN(), "¿Y tú? · país, nacionalidad y lengua",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>cue → volledige zin (uit de oude cursus). </i> Schrijf drie zinnen over jezelf en zeg ze daarna hardop.</p>'
  '<p style="margin-left:12.5mm">Soy de <span class="wl md"></span>. Soy <span class="wl md"></span>. Hablo <span class="wl md"></span>.</p>'
  '<p style="margin-left:12.5mm" class="gloss">Plus: doe hetzelfde voor een klasgenoot (3ª pers.: es de… / es… / habla…). <span class="wl full"></span></p>', apoyo="MARCO → SIN AYUDA"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha 3 presentaciones</b> (Diego, Lucía, Mateo) en la web. <b>1ª vez:</b> ¿de qué país? · <b>2ª vez:</b> nacionalidad y lengua. Escribe los datos.</div>',
           qr("Escanea y escucha", "§4 · Presentaciones", seed=44)))
P('<div class="se" style="margin-top:5mm">Mi ficha · país, nacionalidad y lengua</div>')
P('<div class="fichacard"><div>'
  '<div class="row"><span class="k">País (soy de…)</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Nacionalidad (soy…)</span><span class="v"><span class="wl md"></span></span></div></div><div>'
  '<div class="row"><span class="k">Lengua(s) (hablo…)</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Ciudad (vivo en…)</span><span class="v"><span class="wl md"></span></span></div></div></div>')
P('</div>')  # page §4

# ================= §5 · LECTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">5</span><span class="pk">§5 · Lectura — «De vuelta al insti»</span>')
P('<div class="intro"><b>ES:</b> Dos perfiles de la cast. Lee, busca información y reacciona. <span class="gloss">Twee profielen van de cast. Lezen, informatie zoeken en reageren.</span></div>')
P(lpd(("4","leesvaardigheid: korte informatieve teksten"),("5","cultuur & identiteit")))
P('</div>')
P('<div class="lecdoel"><b>Antes de leer:</b> mira los títulos y las fotos. ¿Qué tipo de texto es? ¿Qué información esperas? <span class="gloss">Kijk vóór het lezen naar titel & beeld: welk soort tekst? Wat verwacht je?</span></div>')
P('<div class="txtmeta"><span class="tm"><b>Tipo:</b> perfil / presentación</span><span class="tm"><b>Fuente:</b> muro de clase</span><span class="tm"><b>Objetivo:</b> conocer a la cast</span></div>')
P(f'<div class="ptexts">'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["diego"]}</div><div><div class="nm">Diego</div><div class="fr">CDMX 🇲🇽</div></div></div>'
  f'<p>¡Hola! Me <span class="evi">llamo</span> Diego y <span class="evi">soy</span> de la Ciudad de México. <span class="evi">Tengo</span> dieciséis años. Vivo con mi madre y mi hermana. Me gusta el fútbol y la comida de mi barrio. En clase soy alegre y un poco hablador. Hablo español y estudio neerlandés — ¡es difícil!</p></div>'
  f'<div class="ptext"><div class="ph"><div class="av">{AV["nina"]}</div><div><div class="nm">Nina</div><div class="fr">Cusco 🇵🇪</div></div></div>'
  f'<p>Buenos días. Soy Nina, <span class="evi">peruana</span>, de Cusco. Tengo dieciséis años y tengo un hermano pequeño. Soy tranquila y trabajadora. Hablo español y un poco de quechua, la lengua de los Andes. Este año viajo con la clase por el mundo hispano. ¡Estoy contenta!</p></div></div>')
P(actx(AN(), "Verdadero o falso — con prueba",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Waar (V) of niet waar (F)? Onderstreep het <b>bewijs</b> in de tekst en noteer.</p>'
  '<table class="alf"><thead><tr><th>Afirmación</th><th>V/F</th><th>Prueba (cita del texto)</th></tr></thead><tbody>'
  '<tr><td>Diego tiene una hermana.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Nina habla tres lenguas.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Los dos tienen dieciséis años.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="MODELO"))
P(actx(AN(), "Escanea — completa la ficha",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★★☆"}],
  '<p><i>informatieraster.</i> Zoek de gegevens en vul in.</p>'
  '<table class="alf"><thead><tr><th>—</th><th>Diego</th><th>Nina</th></tr></thead><tbody>'
  '<tr><td>País / ciudad</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>Edad</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>Carácter (1 adj.)</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>Lenguas</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr></tbody></table>', apoyo="SIN AYUDA"))
P(actx(AN(), "Reacciona — ¿y tú?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>productieve reactie.</i> ¿Con quién tienes más en común, con Diego o con Nina? Schrijf 2–3 zinnen met <b>porque</b>.</p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (Tengo más en común con … porque …)"))
P('</div>')  # page §5

# ================= TALLER DE LENGUA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">T</span><span class="pk">Taller de lengua</span>')
P('<div class="intro"><b>ES:</b> Dos herramientas de la lengua: la <b>acentuación</b> (¿dónde va la tilde?) y los <b>conectores</b> para unir frases. <span class="gloss">Twee taalgereedschappen: klemtoon/accent en verbindingswoorden.</span></div>')
P('</div>')
P('<h3>1 · Ortografía — la acentuación</h3>')
P(regla("Aguda · llana · esdrújula", '<p><b>Aguda</b> = klemtoon op laatste lettergreep (ma-<b>drid</b>, es-pa-<b>ñol</b>). <b>Llana</b> = voorlaatste (<b>ca</b>-sa, <b>li</b>-bro). <b>Esdrújula</b> = derde van achter, <b>altijd</b> tilde (<b>mú</b>-si-ca, <b>mé</b>-xi-co).<br><span class="gloss">De meeste woorden zijn llana. Draagt het woord een tilde? Volg dan gewoon de tilde.</span></p>'))
P(actx(AN(), "Clasifica por el acento",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Sorteer: <span class="words"><b>México · español · casa · música · Madrid · teléfono · libro · reloj</b></span></p>'
  + sortcols([("aguda",""),("llana",""),("esdrújula","")], eigen=False), apoyo="BANCO"))
P('<h3 style="margin-top:6mm">2 · Conectores — unir frases</h3>')
P('<div class="colloc"><div class="cen">y · pero · porque · también</div><div class="brs">'
  '<span class="br">y = en</span><span class="br">pero = maar</span><span class="br">porque = want/omdat</span><span class="br">también = ook</span></div></div>')
P('<div class="truc"><b>¡Ojo!</b> «want» én «omdat» zijn allebei <b>porque</b>. «dus» = <b>así que / por eso</b> (nooit <span class="trap">luego</span>). «maar» = <b>pero</b>.</div>')
P(actx(AN(), "Completa con el conector correcto",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>gap-fill conectoren.</i> Kies uit <b>y · pero · porque · también</b>.</p>'
  '<p style="margin-left:12.5mm">1. Soy de Bélgica <span class="wl sm"></span> hablo neerlandés. &nbsp; 2. Estudio español <span class="wl sm"></span> me gusta mucho.<br>'
  '3. Nina es tranquila, <span class="wl sm"></span> Diego es hablador. &nbsp; 4. Tengo un hermano <span class="wl sm"></span> una hermana.</p>', apoyo="BANCO"))
P('</div>')  # page Taller

# ===== ronde 1 · toegevoegde blokken =====
# Alleen toegevoegd: bestaande secties en nummering blijven staan, deze krijgen
# een eigen nummer erachter. Inhoud uit dezelfde bron als de hub.
P('<div class="page"><div class="parada sec">')
P('<span class="num">4.3</span><span class="pk">§4.3 · Países y nacionalidades — la serie completa</span>')
P('<div class="intro"><b>ES:</b> Ya sabes emparejar. Ahora <b>escribe</b> la nacionalidad, sin mirar. <span class="gloss">Koppelen kun je al. Nu schrijf je de nationaliteit zelf — dat is een trede hoger dan herkennen.</span></div>')
P(PB.nat_print(ND.C6P_U0_NAC_TYPE, AN(),
  opgave_tekst="Escribe la nacionalidad (forma masculina) de cada país.",
  klasse="wl md", per_rij=2))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">5.2</span><span class="pk">§5.2 · Lectura — «El tablón de anuncios»</span>')
P('<div class="intro"><b>ES:</b> Tres avisos de verdad, del pasillo. <b>No hace falta entenderlo todo</b> para sacar la información. <span class="gloss">Drie echte prikbordberichtjes. Je hoeft niet alles te begrijpen om de informatie te vinden.</span></div>')
P(PB.lectura_print(LD.C6P_U0, AN()))
P('</div>')

P('<div class="page"><div class="parada sec">')
P('<span class="num">6</span><span class="pk">§6 · Escucha — «El primer día de curso»</span>')
P('<div class="intro"><b>ES:</b> Diego y Valen se reencuentran en el patio. <b>Escucha primero, escribe después.</b> <span class="gloss">Diego en Valen zien elkaar terug op de speelplaats. Eerst luisteren, dan schrijven; het transcript staat online en gaat pas open ná de taken.</span></div>')
P(PB.escucha_print(ED.C6P_U0, AN()))
P('</div>')

# ================= CULTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">C</span><span class="pk">Cultura · el mundo hispano</span>')
P('<div class="intro"><b>ES:</b> El español es la lengua de <b>21 países</b> y de más de <b>500 millones</b> de personas. Un viaje por cuatro continentes. <span class="gloss">Spaans is de taal van 21 landen en 500+ miljoen mensen — over vier continenten.</span></div>')
P(lpd(("5","identiteit in diversiteit: de Spaanstalige wereld")))
P('</div>')
P('<div class="fams three" style="margin-top:2mm">'
  '<div class="pcard"><div class="t">🇪🇸 Europa</div><div class="ej" style="margin-top:2mm"><b>España</b> is het enige Spaanstalige land in Europa. Naast het Spaans (castellano) spreekt men er ook <b>catalán</b>, <b>gallego</b> en <b>euskera</b>.</div><div class="anchor gloss">Madrid = de hoofdstad. ~47 miljoen inwoners.</div></div>'
  '<div class="pcard"><div class="t">🌎 América</div><div class="ej" style="margin-top:2mm">De meeste hispanohablantes wonen in <b>Latijns-Amerika</b>: van 🇲🇽 México tot 🇦🇷 Argentina. <b>México</b> is het grootste Spaanstalige land (~130 miljoen).</div><div class="anchor gloss">19 landen · veel accenten (voseo in Argentina!).</div></div>'
  '<div class="pcard"><div class="t">🌍 ¿Sabías que…?</div><div class="ej" style="margin-top:2mm">Ook in <b>Guinea Ecuatorial</b> (Afrika) is Spaans officieel. En in de <b>VS</b> wonen ~40 miljoen hispanohablantes — meer dan in Spanje!</div><div class="anchor gloss">Español = 2ª lengua materna del mundo.</div></div></div>')
P('<div class="route-note" style="margin-top:5mm">🗺️ <b>En la web:</b> el <b>mapa interactivo</b> del mundo hispano — haz clic en cada país para oír su nombre y ver la bandera. <span class="gloss">Online: klikbare kaart met vlaggen en audio.</span></div>')
P(actx(AN(), "El mapa — ¿qué país es?",
  [{"t":"🌍 Cultura","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Werk samen. Schrijf bij elke hoofdstad het land, en één land dat je wil bezoeken + waarom (met <b>porque</b>).</p>'
  '<p style="margin-left:12.5mm">Madrid → <span class="wl sm"></span> · Lima → <span class="wl sm"></span> · Bogotá → <span class="wl sm"></span> · Buenos Aires → <span class="wl sm"></span></p>'
  '<p style="margin-left:12.5mm">Quiero visitar <span class="wl md"></span> porque <span class="wl lg"></span></p>', apoyo="MARCO"))
P(actx(AN(), "Datos curiosos — une país y dato",
  [{"t":"🌍 Cultura","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>matching.</i> Verbind elk land met het juiste weetje (schrijf de letter).</p>'
  '<div class="wcols" style="grid-template-columns:1fr 1fr;margin-left:12.5mm">'
  '<div class="wcol"><div class="ch">País</div><div class="cb short">1. México &nbsp; 2. Guinea Ecuatorial &nbsp; 3. Perú &nbsp; 4. España</div></div>'
  '<div class="wcol"><div class="ch">Dato</div><div class="cb short">a. único país hispano de África &nbsp; b. aquí se habla quechua &nbsp; c. el país hispano más grande &nbsp; d. tiene catalán y gallego</div></div></div>'
  '<p style="margin-left:12.5mm">1-<span class="wl sm"></span> 2-<span class="wl sm"></span> 3-<span class="wl sm"></span> 4-<span class="wl sm"></span> · ¿Qué dato te sorprende más? <span class="wl md"></span></p>', apoyo="BANCO"))
P('</div>')  # page Cultura

# ================= TAREA FINAL =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">★</span><span class="pk">Tarea final · «Tarjeta de reencuentro»</span>')
P('<div class="intro"><b>ES:</b> Crea tu <b>tarjeta de reencuentro</b> para el muro de la clase y preséntate en pareja. <span class="gloss">Maak je terugkeer-kaartje voor de klasmuur en stel je voor in duo.</span></div>')
P('</div>')
P('<div class="fmu"><div class="fc"><div class="hd">¿Para quién?</div><div class="bd">tus compañeros de clase (el muro)</div></div>'
  '<div class="fc"><div class="hd">¿Para qué?</div><div class="bd">conoceros otra vez este curso</div></div>'
  '<div class="fc"><div class="hd">Resultado</div><div class="bd">una tarjeta + una presentación oral (30 s)</div></div></div>')
P('<ol class="pasos">'
  '<li><b>Planifica.</b> Anota tus datos: nombre, edad, ciudad/país, una lengua, un adjetivo de carácter, algo que te gusta.</li>'
  '<li><b>Escribe la tarjeta</b> (4–5 frases) con <b>me llamo / soy / tengo / vivo / hablo</b> y un conector (<b>y, pero, porque</b>).</li>'
  '<li><b>Preséntate en pareja</b>: lee tu tarjeta en voz alta; tu compañero/a anota un dato y hace una pregunta.</li>'
  '<li><b>Graba</b> tu presentación en la web y escúchate. ¿Suena bien? Repite mejor.</li></ol>')
P('<div class="se" style="margin-top:4mm">Mi tarjeta <span class="gloss" style="font-size:8pt">· vul in en versier</span></div>')
P('<div class="fichacard"><div>'
  '<div class="row"><span class="k">Nombre</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Edad</span><span class="v"><span class="wl sm"></span></span></div>'
  '<div class="row"><span class="k">Ciudad / país</span><span class="v"><span class="wl md"></span></span></div></div><div>'
  '<div class="row"><span class="k">Lengua(s)</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Soy… (carácter)</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Me gusta…</span><span class="v"><span class="wl md"></span></span></div></div></div>')
P('<div class="se" style="margin-top:4mm">Mi presentación <span class="gloss" style="font-size:8pt">· schrijf je 4–5 zinnen (geruit)</span></div><div class="wbox"></div>')
P(audiorow('<div class="ic">🎬</div><div><b>Graba tu presentación</b> en la página digital (recorder + rúbrica). Escucha, compara con el modelo y vuelve a grabar.</div>',
           qr("Escanea y graba", "Tarea · Tarjeta", seed=70)))
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré?</div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Mijn tarjeta heeft <b>naam, leeftijd, plaats, taal, karakter</b></td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik het <b>presente</b> correct (soy, tengo, vivo, hablo)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik minstens <b>één conector</b> (y/pero/porque)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>presenteer vlot</b> in pareja (30 s)</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="mispal" style="margin-top:3mm"><div class="mh">🤝 Co-evaluación — la tarjeta de mi compañero/a</div>'
  '<table><thead><tr><th>Lo que me gusta de su tarjeta</th><th>Una pregunta que le hago</th></tr></thead>'
  '<tbody><tr><td></td><td></td></tr></tbody></table></div>')
P('<div class="truc" style="margin-top:3mm"><b>✍️ Antes de colgar:</b> lees je tarjeta nog eens na — <i>presente correct? · concordancia? · un conector?</i> Verbeter één ding: <span class="wl lg"></span></div>')
P('</div>')  # page Tarea

# ================= REPASO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">✓</span><span class="pk">Repaso · lo esencial</span>')
P('<div class="intro"><b>ES:</b> Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag; de volledige herhaling staat online.</span></div>')
P('</div>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>Presentarte:</b> me llamo… · soy (de)… · tengo … años · vivo en… · hablo…</li>'
  '<li><b>Presente regular:</b> -ar → o/as/a/amos/áis/an · -er → o/es/e/emos/éis/en · -ir → o/es/e/imos/ís/en.</li>'
  '<li><b>7 irregulares:</b> ser (soy) · estar (estoy) · tener (tengo) · ir (voy) · hacer (hago) · venir (vengo) · dar (doy).</li>'
  '<li><b>Concordancia:</b> el chic<b>o</b> alt<b>o</b> / la chic<b>a</b> alt<b>a</b> · los/las + -os/-as.</li>'
  '<li><b>Las trampas:</b> 🔴 soy ≠ estoy · 🔴 porque = want én omdat · 🔴 nacionalidades met kleine letter · 🔴 belga = m/v gelijk.</li></ul></div>')
P('<div class="route-note">🎮 <b>Repasa jugando (online):</b> 9 spelletjes met zelfcorrectie en spreiding (presente, género, país↔nacionalidad, saludos…).</div>')
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td><b>saludar</b> en mezelf <b>voorstellen</b> (formeel/informeel)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>het <b>presente</b> gebruiken (regular + ser/estar/tener/ir)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td><b>género</b> en <b>adjectieven</b> laten overeenkomen</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>over <b>país, nacionalidad y lengua</b> praten</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>een korte <b>tekst</b> lezen en een <b>tarjeta</b> schrijven</td><td>☐</td><td>☐</td><td>☐</td></tr></table>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil para mí: <span class="wl md"></span> · Lo que quiero practicar más: <span class="wl md"></span></i></div>')
P('<div class="se" style="margin-top:6mm">Auto-test rápido · ¿lo sé? <span class="gloss" style="font-size:8pt">— dek de unit af en probeer uit het hoofd</span></div>')
P('<p style="margin-left:0">1. Dos saludos: <span class="wl md"></span><br>'
  '2. «ik ben 16 jaar» = <span class="wl md"></span><br>'
  '3. yo (ser · tener · ir) = <span class="wl sm"></span> / <span class="wl sm"></span> / <span class="wl sm"></span><br>'
  '4. la chica (alto) → la chica <span class="wl sm"></span><br>'
  '5. España → nacionalidad = <span class="wl md"></span></p>')
P('<div class="bridge"><b>» Siguiente parada: U1 «El día a día».</b> Ya sabes presentarte; en <b>U1</b> hablas de tu <b>rutina</b>, tus <b>gustos</b> (me gusta…) y usas <b>ser vs estar</b>. ¡Empieza el viaje! <span class="gloss">In U1 begint de reis echt: routine, smaken en ser/estar.</span></div>')
P('</div>')  # page Repaso

# ================= §V VOCABULARIO =================
import json
VOC = json.load(open(f"{HERE}/u0_vocab.json", encoding="utf-8"))
GRP = [("saludos","Saludos y despedidas"),("presentarse","Presentarse · datos personales"),
       ("clase","En clase · frases útiles"),("paises","Países del mundo hispano"),
       ("nacionalidades","Nacionalidades y lenguas"),("descripcion","Describir personas · adjetivos"),
       ("familia","La familia"),("numeros","Números y datos"),("verbos","Verbos frecuentes · presente")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (receptief & productief)")))
P('</div>')
P('<p style="font-size:9.6pt">Las palabras del <b>reencuentro</b> como red — tres familias que abren la unidad:</p>')
P(clusters([
  ("👋","Saludar y presentarse",["hola · buenos días","me llamo · soy de…","¿de dónde eres?"],"Hoe je contact legt."),
  ("🧍","Describir",["alto · bajo · moreno","simpático · alegre","¿cómo eres?"],"Hoe je iemand beschrijft."),
  ("🌍","El mundo hispano",["España · México · Perú","español · mexicano","la lengua · el idioma"],"Landen, nationaliteiten, talen."),
]))
for key, titel in GRP:
    items = [v for v in VOC if v.get("grp") == key]
    if not items: continue
    P(f'<h3 style="margin-top:6mm">{titel} <span class="gloss" style="font-size:8pt">· {len(items)} woorden</span></h3>')
    rows = "".join(f'<tr><td><b>{v["es"]}</b></td><td>{v["nl"]}</td><td class="gloss">{v["soort"]}</td><td class="gloss">{v["ej"]}</td></tr>' for v in items)
    P(f'<table class="alf"><thead><tr><th>Español</th><th>Nederlands</th><th>Soort</th><th>Ejemplo</th></tr></thead><tbody>{rows}</tbody></table>')
P('<div class="divider">Escalera de práctica · V.1–V.5</div>')
P(actx("V.1", "Reconocer — ES → NL",
  [{"t":"🔍 Leer","skill":True},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Schrijf de vertaling. soy de… = <span class="wl md"></span> · la lengua = <span class="wl md"></span> · alegre = <span class="wl md"></span> · el hermano = <span class="wl md"></span></p>', apoyo="MODELO"))
P(actx("V.2", "Distinguir — sorteer per familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Sorteer: <span class="words"><b>hola · español · la madre · simpático · adiós · peruano · alto · buenos días</b></span></p>'
  + sortcols([("saludos",""),("nacionalidad",""),("descripción/familia","")], eigen=False), apoyo="BANCO"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het Spaanse woord aan (beginletter gegeven). ik heet = <b>m</b>___ · vrolijk = <b>a</b>___ · de taal = <b>l</b>___ · hardwerkend = <b>t</b>___<br><span class="wl full"></span></p>', apoyo="LETRA INICIAL"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p><i>verplichte-woorden-zin.</i> Maak één correcte zin met <b>soy · porque · simpático/a</b>.</p><div class="wbox sm"></div>', apoyo="SIN AYUDA"))
P(actx("V.5", "Comunicar — mi mini-perfil",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>vrije productie → transfer.</i> Schrijf 3 zinnen over jezelf (nombre, origen, carácter) en zeg ze daarna hardop tegen je buur.</p>'
  '<p style="margin-left:12.5mm">1. <span class="wl full"></span>2. <span class="wl full"></span>3. <span class="wl full"></span></p>', apoyo="MARCO → SIN AYUDA"))
P('<div class="se" style="margin-top:6mm">Mi red de palabras <span class="gloss" style="font-size:8pt">— teken je woordennetwerk rond «YO»: origen, carácter, familia, lenguas</span></div>')
P('<div class="wbox lg"></div>')
P(mispal("Mis palabras de la unidad", 7))
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Sigue en la página digital:</span> <span class="g">flip cards (ES↔NL), audio en de 9 spellen bouwen de steun verder af.</span></div></div>')
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
   a.href=URL.createObjectURL(blob); a.download='C6plus_U0_mijn_versie.html'; a.click();};
})();
</script>'''

# ---------- ASSEMBLE ----------
HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Español en la práctica · C6+ U0 ¡Volvemos!</title><style>'
        + CSS + PB.CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/U0.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes")
