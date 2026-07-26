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
"""

# ---------------- component-helpers ----------------
def qr(lab, meta, seed=0):
    # decoratieve QR (verwijst in de digitale flow naar de HTML-hub op het juiste anker)
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
    stars = ""
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
  <div class="route-note">📍 <b>Parada 1 · Madrid.</b> Vertrek van de reis in España. Je ontmoet <b>Lucía</b> en leert jezelf voorstellen — de basis voor élke volgende parada. <span class="gloss">We beginnen echt: je stelt jezelf voor en dat gebruik je de hele reis.</span></div>

  <div class="lead" style="margin-top:7mm">
    <div>
      <div class="se">La historia</div>
      <div class="hist"><b>ES:</b> En Madrid conoces a <b>Lucía</b>. Ella te pregunta: «¿Quién eres?». Aprendes a decir tu <b>nombre</b>, tu <b>edad</b>, tu <b>país</b> y los <b>idiomas</b> que hablas — y a preguntar lo mismo a los demás.
      <span class="gloss">In Madrid ontmoet je Lucía. Zij vraagt: «Wie ben jij?». Je leert je naam, leeftijd, land en talen zeggen — en hetzelfde aan anderen vragen.</span></div>
      <div class="ojo"><b>¡Ojo! — valstrik:</b> leeftijd zeg je met <b>tener</b>, niet met <i>ser</i>: <b>Tengo</b> 15 años (✔), niet <span class="trap">Soy 15 años</span> (✘). NL zegt «ik <i>ben</i> 15», Spaans «ik <i>heb</i> 15 jaar».</div>
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

  <div class="obj" style="margin-top:8mm">
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

  <div class="se" style="margin-top:8mm">Cómo trabajar esta unidad · leeswijzer</div>
  <div class="fams" style="margin-top:2mm">
    <div class="pcard"><div class="t" style="font-size:10.5pt">Las etiquetas de cada actividad</div>
      <div class="ej" style="margin-top:2mm"><span class="badge skill">👂 Escuchar</span> <span class="badge skill">🎙️ Hablar</span> <span class="badge skill">🔍 Analizar</span> <span class="badge">👤 Solo</span> <span class="badge">👥 En parejas</span> <span class="badge">± 5 min</span> <span class="stars">★★☆</span></div>
      <div class="anchor gloss" style="margin-top:2mm">Elke oefening toont de <b>vaardigheid</b>, de <b>werkvorm</b>, de <b>tijd</b> en de <b>moeilijkheid</b> (sterren).</div></div>
    <div class="pcard"><div class="t" style="font-size:10.5pt">El apoyo baja poco a poco</div>
      <div class="ej" style="margin-top:2mm"><span class="steun">Modelo</span> → <span class="steun">Banco</span> → <span class="steun">Marco</span> → <span class="steun">Pista</span> → <span class="steun">Sin ayuda</span></div>
      <div class="anchor gloss" style="margin-top:2mm">De <b>steun bouwt af</b>: eerst een model, dan een woordenbank/zinsframe, ten slotte zónder hulp. Zo produceer je écht zelf.</div></div>
  </div>
  <div class="fams" style="margin-top:4mm">
    <div class="pcard"><div class="t" style="font-size:10.5pt">Dos capas de color</div>
      <div class="ej" style="margin-top:2mm"><b>1 · groen</b> = de cursus/unit (koppen, kaders). <b>2 · función</b>: <span class="fx per">persoon</span> <span class="fx vb">werkwoord</span> <span class="fx ob">voorwerp</span> <span class="fx ti">tijd</span> <span class="fx pl">plaats</span> <span style="color:var(--red);font-weight:700">🔴 valstrik</span>.</div>
      <div class="anchor gloss" style="margin-top:2mm">Kleur is <b>nooit</b> de enige drager — altijd óók een label of vorm (grijswaarden-veilig).</div></div>
    <div class="pcard"><div class="t" style="font-size:10.5pt">Papel + pantalla</div>
      <div class="ej" style="margin-top:2mm">📄 el libro (dit boek) · 🎮 la <b>página digital</b> (spellen, audio, flip cards) · 📊 el PowerPoint. De <b>QR</b>-codes brengen je naar de juiste online-oefening.</div>
      <div class="anchor gloss" style="margin-top:2mm">Print werkt <b>volledig zonder</b> scherm; online voegt audio, opname en zelfcorrectie toe. Het <b>repaso</b> (herhaling) staat online.</div></div>
  </div>
</div>
''')

# ---------- §0 Ponte al día ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">0</span><span class="pk">§0 · ¡Ponte al día!</span>')
P('<div class="intro"><b>ES:</b> Antes de empezar, recordamos lo que ya sabes de la Unidad 0 y que necesitas hoy: <b>saludar</b>, <b>deletrear</b> y los <b>números</b> (para la edad y el teléfono). <span class="gloss">Voor we starten: kort ophalen wat je al kent uit U0 en vandaag nodig hebt — groeten, spellen en getallen (voor je leeftijd en telefoon).</span></div>')
P(lpd(("7","woordenschat inzetten"), ("9","strategieën / lengua de clase")))
P('</div>')  # close parada
P('<div class="fams three" style="margin-top:6mm">')
P(pcard("Saludar", '<div class="ej"><b>¡Hola!</b> · <b>Buenos días</b> · <b>¿Qué tal?</b> · <b>Encantado/-a</b> · <b>Adiós</b></div><div class="anchor gloss">groeten, kennismaken, afscheid</div>'))
P(pcard("Deletrear", '<div class="ej">a·be·ce… <b>¿Cómo se escribe?</b> · <b>con hache</b> / <b>sin hache</b> · <b>una arroba (@)</b></div><div class="anchor gloss">je naam en e-mail spellen</div>'))
P(pcard("Números 0–100", '<div class="ej"><b>catorce · quince · dieciséis</b> · <b>veintiuno</b> · <b>treinta y cinco</b></div><div class="anchor gloss">voor leeftijd & telefoonnummer</div>'))
P('</div>')
P(act(1, "Calentamiento: preséntate como en U0",
      [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★☆☆"}],
      '<p>Zeg tegen je buur: <span class="words"><b>¡Hola!</b></span> + je naam + spel je voornaam. Je buur schrijft ze op de lijn. Wissel daarna.</p>'
      '<p style="margin-left:12.5mm">Mi nombre: <span class="wl lg"></span> &nbsp; El nombre de mi compañero/a: <span class="wl lg"></span></p>'))
P(act(2, "Los números que necesito hoy",
      [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
      '<p>Schrijf het getal in letters (recyclen U0). <span class="gloss">Nodig voor je leeftijd en telefoonnummer.</span></p>'
      '<table class="mp"><thead><tr><th>Cifra</th><th>En letras</th><th>Cifra</th><th>En letras</th></tr></thead>'
      '<tbody><tr><td>14</td><td><span class="wl md"></span></td><td>30</td><td><span class="wl md"></span></td></tr>'
      '<tr><td>16</td><td><span class="wl md"></span></td><td>0470…</td><td><span class="wl md"></span></td></tr></tbody></table>'))
P(guide("Repasa jugando (online):", "— números, saludos en spellen staan als spelletjes op de digitale pagina. Eén QR verder oefen je alles met zelfcorrectie."))
P('</div>')  # close page

# ---------- §1 Tus datos personales ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">1</span><span class="pk">§1 · Tus datos personales</span>')
P('<div class="route-note">📍 Parada 1 · Madrid — Lucía te pregunta quién eres.</div>')
P('<div class="intro"><b>ES:</b> Estos son tus <b>datos personales</b>: nombre, apellido, edad, país, idiomas. Primero los <b>reconoces</b> en una ficha, después los <b>usas</b> para presentarte. <span class="gloss">Dit zijn je persoonsgegevens. Eerst herken je ze op een fiche, daarna gebruik je ze om jezelf voor te stellen.</span></div>')
P(lpd(("7","woordenschat: datos personales"), ("2","relevante info in een ficha"), ("3","doelgericht schrijven met steun")))
P('</div>')  # parada
# woordscene = ficha
P('<h3 style="margin-top:6mm">La ficha de Lucía — observa y descubre</h3>')
P('<div class="fichacard">'
  '<div><div class="row"><span class="k">el nombre</span><span class="v">Lucía <span class="nl">voornaam</span></span></div>'
  '<div class="row"><span class="k">el apellido</span><span class="v">Ramírez García <span class="nl">achternaam (×2!)</span></span></div>'
  '<div class="row"><span class="k">la edad</span><span class="v">16 años <span class="nl">leeftijd</span></span></div>'
  '<div class="row"><span class="k">el país</span><span class="v">España <span class="nl">land</span></span></div></div>'
  '<div><div class="row"><span class="k">la nacionalidad</span><span class="v">española <span class="nl">nationaliteit</span></span></div>'
  '<div class="row"><span class="k">la ciudad</span><span class="v">Sevilla <span class="nl">stad</span></span></div>'
  '<div class="row"><span class="k">los idiomas</span><span class="v">español, inglés <span class="nl">talen</span></span></div>'
  '<div class="row"><span class="k">el correo</span><span class="v">lucia@mail.com <span class="nl">e-mail</span></span></div></div></div>')
P(guide("Observa:", "— ¿qué palabras entiendes sin traducción? (nombre, dirección, correo…). De vertaling staat klein; probeer eerst zónder.", "🔎"))
# presentarse chunks (chat, color semantics)
P('<h3 style="margin-top:6mm">Presentarse — las frases clave</h3>')
P('<div class="chat">'
  '<div class="chatline you"><div class="bub">¡Hola! ¿Quién eres?</div><div class="who">Lucía</div></div>'
  '<div class="chatline me"><div class="bub"><span class="fx per">Yo</span> <span class="fx vb">me llamo</span> Leo. <span class="fx vb">Soy</span> <span class="fx pl">de Bélgica</span> y <span class="fx vb">tengo</span> <span class="fx ti">15 años</span>.</div><div class="who">Tú</div></div>'
  '<div class="chatline you"><div class="bub">¿Y dónde vives?</div><div class="who">Lucía</div></div>'
  '<div class="chatline me"><div class="bub"><span class="fx vb">Vivo</span> <span class="fx pl">en Gante</span> y <span class="fx vb">hablo</span> neerlandés y español.</div><div class="who">Tú</div></div>'
  '</div>'
  '<div class="leg"><span class="fx per">persoon</span> <span class="fx vb">werkwoord</span> <span class="fx pl">plaats/afkomst</span> <span class="fx ti">tijd/leeftijd</span> · <span class="gloss">kleur = taalfunctie (ook zónder kleur herkenbaar aan de vorm)</span></div>')
P(regla("Regla · presentarse",
  '<p><b>Me llamo</b> + naam · <b>Soy de</b> + land · <b>Soy</b> + nationaliteit · <b>Tengo</b> + getal + <b>años</b> · <b>Vivo en</b> + stad · <b>Hablo</b> + taal. '
  '<br>🔴 <b>Leeftijd = tener</b>: <i>Tengo 15 años</i> (niet <span class="trap">soy 15</span>). 🔴 <b>Nationaliteit met kleine letter</b>: <i>belga, español</i>.</p>'))
P(act(1, "Empareja el dato con el ejemplo",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Verbind het gegeven met het juiste voorbeeld (schrijf de letter). <span class="gloss">receptief — herkennen.</span></p>'
  '<table class="mp"><thead><tr><th>Dato</th><th>Letra</th><th></th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td>1 · el apellido</td><td><span class="wl sm"></span></td><td>A</td><td>16 años</td></tr>'
  '<tr><td>2 · la edad</td><td><span class="wl sm"></span></td><td>B</td><td>española</td></tr>'
  '<tr><td>3 · la nacionalidad</td><td><span class="wl sm"></span></td><td>C</td><td>García</td></tr>'
  '<tr><td>4 · el correo</td><td><span class="wl sm"></span></td><td>D</td><td>lucia@mail.com</td></tr>'
  '</tbody></table>'))
P(act(2, "Completa tu ficha",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p>Vul je <b>eigen</b> ficha in (echt of fictief, dat kies je zelf voor de eindtaak). <span class="gloss">gestuurd produceren — zinsframe.</span></p>'
  '<div class="fichacard"><div>'
  '<div class="row"><span class="k">Nombre</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Apellido</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Edad</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">País</span><span class="v"><span class="wl md"></span></span></div></div><div>'
  '<div class="row"><span class="k">Nacionalidad</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Ciudad</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Idiomas</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Correo</span><span class="v"><span class="wl md"></span></span></div></div></div>'))
P(act(3, "Preséntate en cuatro frases",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 7 min"},{"t":"★★☆"}],
  '<p>Schrijf vier zinnen met het frame, en zeg ze daarna hardop tegen je buur. <span class="gloss">Me llamo… · Soy de… · Tengo… · Vivo en…</span></p>'
  '<p style="margin-left:12.5mm"><span class="wl full"></span><span class="wl full"></span><span class="wl full"></span><span class="wl full"></span></p>'))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha a cuatro personas y anota su país.</b> <span class="gloss">Luister naar vier mensen en noteer hun land — selectief luisteren.</span></div>',
           qr("Escanea y escucha", "Audio 1.1 · Se presentan · 0:50", seed=11)))
P('</div>')  # page

# ---------- §2 El verbo SER + pronombres ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2 · El verbo SER + los pronombres</span>')
P('<div class="intro"><b>ES:</b> Para decir <b>quién eres</b> y <b>de dónde eres</b> usas el verbo <b>ser</b>. Es <b>irregular</b> pero cortísimo y lo vas a usar todo el año. <span class="gloss">Om te zeggen wie je bent en waar je vandaan komt, gebruik je «ser». Onregelmatig, maar heel kort — en je gebruikt het het hele jaar.</span></div>')
P(lpd(("8","taalsysteem: ser + pronombres"), ("3","zich voorstellen (productief)")))
P('</div>')  # parada
# noticing
P('<h3 style="margin-top:6mm">Observa — ¿qué forma usa cada persona?</h3>')
P('<div class="chat">'
  '<div class="chatline you"><div class="bub"><span class="fx per">Yo</span> <b>soy</b> Lucía. ¿Y tú? ¿<span class="fx per">Tú</span> <b>eres</b> de Bélgica?</div><div class="who">Lucía</div></div>'
  '<div class="chatline me"><div class="bub">Sí. <span class="fx per">Nosotros</span> <b>somos</b> de Flandes. <span class="fx per">Diego</span> <b>es</b> de México.</div><div class="who">Tú</div></div></div>')
P('<table class="conj"><thead><tr><th>Persona</th><th>ser</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">soy</td><td>Soy Leo, soy belga.</td></tr>'
  '<tr><td class="p">tú</td><td class="v">eres</td><td>¿De dónde eres?</td></tr>'
  '<tr><td class="p">él / ella / usted</td><td class="v">es</td><td>Lucía es española.</td></tr>'
  '<tr><td class="p">nosotros/-as</td><td class="v">somos</td><td>Somos de Bélgica.</td></tr>'
  '<tr><td class="p">vosotros/-as</td><td class="v">sois</td><td>¿Sois estudiantes?</td></tr>'
  '<tr><td class="p">ellos/-as / ustedes</td><td class="v">son</td><td>Son de México.</td></tr>'
  '</tbody></table>')
P(regla("Regla · SER (irregular)",
  '<p><b>soy · eres · es · somos · sois · son.</b> Gebruik <b>ser</b> voor: <b>identiteit</b> (soy Leo), <b>afkomst</b> (soy de Bélgica), <b>nationaliteit</b> (soy belga), <b>eigenschap</b> (es simpático). '
  '<br>🔴 Onderwerpwoorden (<i>yo, tú…</i>) mag je <b>weglaten</b> — de vorm zegt al wie het is: <i>(Yo) soy Leo</i>.</p>'))
P('<div class="truc"><b>🟡 Truc — tú vs. usted:</b> tegen leeftijdsgenoten: <b>tú eres</b>. Beleefd/tegen een onbekende volwassene: <b>usted es</b> (3e persoon!). In España veel <i>tú</i>; in delen van Latijns-Amerika vaker <i>usted</i> (→ Cultura).</div>')
P('<h3 style="margin-top:6mm">Los cuatro usos de ser</h3>')
P('<div class="fams" style="margin-top:2mm">')
P(pcard("Identidad + origen", '<div class="ej"><b>Soy</b> Leo. · <b>Soy de</b> Bélgica.</div><div class="anchor gloss">wie je bent · waar je vandaan komt</div>'))
P(pcard("Nacionalidad + cualidad", '<div class="ej"><b>Soy</b> belga. · Lucía <b>es</b> simpática.</div><div class="anchor gloss">nationaliteit · een eigenschap</div>'))
P('</div>')
P(act(1, "Elige la forma de ser",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Vul de juiste vorm van <b>ser</b> in. <span class="gloss">gestuurd — de vormtabel mag open.</span></p>'
  '<p style="margin-left:12.5mm">a) Yo <span class="wl sm"></span> de Gante. &nbsp; b) ¿Tú <span class="wl sm"></span> español? &nbsp; c) Lucía <span class="wl sm"></span> de Sevilla.<br>'
  'd) Nosotros <span class="wl sm"></span> belgas. &nbsp; e) Diego y Nina <span class="wl sm"></span> de América.</p>'))
P(act(2, "Preséntate a ti y a un compañero",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p>Zeg één zin over jezelf (<i>Soy…</i>) en één over je buur in de 3e persoon (<i>Él/Ella es…</i>). <span class="gloss">productie — steun bouwt af: eerst met tabel, dan zonder.</span></p>'
  '<p style="margin-left:12.5mm">Yo: <span class="wl lg"></span><br>Mi compañero/a: <span class="wl lg"></span></p>'))
P(guide("Juega online:", "— «El verbo SER» (welke persoon?) en «Presente Tetris» op de digitale pagina; laat de vormen op hun plek vallen."))
P('</div>')  # page

# ---------- §3 El presente regular ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3 · El presente regular (-ar · -er · -ir)</span>')
P('<div class="intro"><b>ES:</b> Casi todos los verbos siguen un <b>patrón</b>. Aprende las tres familias — <b>-ar</b>, <b>-er</b>, <b>-ir</b> — y podrás hablar de lo que <b>haces</b>: hablar, estudiar, vivir, aprender. <span class="gloss">Bijna alle werkwoorden volgen een patroon. Leer de drie families en je kunt vertellen wat je doet.</span></div>')
P(lpd(("8","taalsysteem: presente regular"), ("3","vertellen over jezelf (productief)")))
P('</div>')
P('<h3 style="margin-top:6mm">Observa — quita la terminación, añade la nueva</h3>')
P('<div class="fams three" style="margin-top:4mm">')
P(pcard("hablar (-ar)", '<table class="conj"><tbody>'
  '<tr><td class="p">yo</td><td>habl<span class="end">o</span></td></tr>'
  '<tr><td class="p">tú</td><td>habl<span class="end">as</span></td></tr>'
  '<tr><td class="p">él/ella</td><td>habl<span class="end">a</span></td></tr>'
  '<tr><td class="p">nosotros</td><td>habl<span class="end">amos</span></td></tr>'
  '<tr><td class="p">vosotros</td><td>habl<span class="end">áis</span></td></tr>'
  '<tr><td class="p">ellos</td><td>habl<span class="end">an</span></td></tr></tbody></table>'))
P(pcard("aprender (-er)", '<table class="conj"><tbody>'
  '<tr><td class="p">yo</td><td>aprend<span class="end">o</span></td></tr>'
  '<tr><td class="p">tú</td><td>aprend<span class="end">es</span></td></tr>'
  '<tr><td class="p">él/ella</td><td>aprend<span class="end">e</span></td></tr>'
  '<tr><td class="p">nosotros</td><td>aprend<span class="end">emos</span></td></tr>'
  '<tr><td class="p">vosotros</td><td>aprend<span class="end">éis</span></td></tr>'
  '<tr><td class="p">ellos</td><td>aprend<span class="end">en</span></td></tr></tbody></table>'))
P(pcard("vivir (-ir)", '<table class="conj"><tbody>'
  '<tr><td class="p">yo</td><td>viv<span class="end">o</span></td></tr>'
  '<tr><td class="p">tú</td><td>viv<span class="end">es</span></td></tr>'
  '<tr><td class="p">él/ella</td><td>viv<span class="end">e</span></td></tr>'
  '<tr><td class="p">nosotros</td><td>viv<span class="end">imos</span></td></tr>'
  '<tr><td class="p">vosotros</td><td>viv<span class="end">ís</span></td></tr>'
  '<tr><td class="p">ellos</td><td>viv<span class="end">en</span></td></tr></tbody></table>'))
P('</div>')
P(regla("Regla · presente regular",
  '<p><b>-er</b> en <b>-ir</b> zijn bijna gelijk — alleen bij <b>nosotros/vosotros</b> verschillen ze (-emos/-éis vs. -imos/-ís). '
  'De <b>yo</b>-vorm eindigt altijd op <b>-o</b>. 🟡 <b>Truc:</b> ken je de yo-vorm, dan ken je de rest van het patroon.</p>'))
P('<div class="truc"><b>🔴 Valstrik NL:</b> <i>vivir</i> = <b>wonen</b> én leven; hier meestal <b>wonen</b> (Vivo en Brujas). En het onderwerp mag weg: <i>(Yo) hablo español</i>.</div>')
P(act(1, "Conjuga en presente",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Vervoeg. <span class="gloss">gestuurd — de kaarten hierboven mogen open.</span></p>'
  '<table class="mp"><thead><tr><th>Infinitivo</th><th>yo</th><th>tú</th><th>nosotros</th></tr></thead><tbody>'
  '<tr><td>hablar</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>aprender</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>vivir</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>estudiar</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '</tbody></table>'))
P(act(2, "Habla de ti",
  [{"t":"🎙️ Hablar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p>Schrijf drie ware zinnen over jezelf met <b>hablar</b>, <b>estudiar</b> en <b>vivir</b>. <span class="gloss">Hablo… · Estudio… · Vivo en…</span></p>'
  '<p style="margin-left:12.5mm"><span class="wl full"></span><span class="wl full"></span><span class="wl full"></span></p>'))
P(guide("Ojo — conjugador online:", "— alle vervoegingen (nagerekend, ~1000 werkwoorden) staan in de aparte cursus-tool «Conjugador», niet hier. Hier oefen je met «Presente Tetris».", "🔁"))
P('</div>')

# ---------- §4 Preguntar: interrogativos + género/número + artículos ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4 · Preguntar: interrogativos + el/la</span>')
P('<div class="intro"><b>ES:</b> Ya sabes presentarte; ahora aprende a <b>preguntar</b> a los demás — y a poner el <b>artículo</b> correcto (el/la, un/una). <span class="gloss">Je kunt je voorstellen; nu leer je vragen stellen — en het juiste lidwoord kiezen.</span></div>')
P(lpd(("8","taalsysteem: interrogativos, género/número, artículos"), ("4","mondelinge interactie: vragen stellen")))
P('</div>')
P('<h3 style="margin-top:6mm">Las palabras interrogativas</h3>')
P('<table class="mp"><thead><tr><th>Pregunta</th><th>Sirve para…</th><th>Respuesta modelo</th></tr></thead><tbody>'
  '<tr><td><b>¿Cómo</b> te llamas?</td><td>de naam</td><td>Me llamo Leo.</td></tr>'
  '<tr><td><b>¿De dónde</b> eres?</td><td>de afkomst</td><td>Soy de Bélgica.</td></tr>'
  '<tr><td><b>¿Dónde</b> vives?</td><td>de woonplaats</td><td>Vivo en Gante.</td></tr>'
  '<tr><td><b>¿Cuántos años</b> tienes?</td><td>de leeftijd</td><td>Tengo 15 años.</td></tr>'
  '<tr><td><b>¿Cuál</b> es tu correo?</td><td>een gegeven (keuze)</td><td>Es leo@mail.com.</td></tr>'
  '<tr><td><b>¿Qué</b> idiomas hablas?</td><td>info (open)</td><td>Hablo dos idiomas.</td></tr>'
  '<tr><td><b>¿Quién</b> es ella?</td><td>een persoon</td><td>Es Lucía.</td></tr>'
  '</tbody></table>')
P('<div class="truc"><b>🔴 ¿Cuál? vs ¿Qué?</b> vóór <i>ser</i> + gegeven kies je <b>¿Cuál?</b>: <i>¿<b>Cuál</b> es tu nombre?</i> (niet <span class="trap">¿Qué es tu nombre?</span>). En vraagwoorden dragen een <b>tilde</b>: cómo, dónde, cuál…</div>')
P('<h3 style="margin-top:6mm">Género y número — el/la/los/las · un/una</h3>')
P('<div class="fams" style="margin-top:4mm">')
P(pcard("Masculino → el / un", '<div class="ej"><b>el</b> nombre · <b>el</b> país · <b>el</b> correo · <b>el</b> apellido</div><div class="t2">🔴 valstrik: <b>el</b> idioma, <b>el</b> día, <b>el</b> mapa (op -a, tóch mannelijk!)</div>'))
P(pcard("Femenino → la / una", '<div class="ej"><b>la</b> ciudad · <b>la</b> edad · <b>la</b> dirección · <b>la</b> nacionalidad</div><div class="t2">meestal -a, -ción, -dad → femenino</div>'))
P('</div>')
P(regla("Regla · artículos",
  '<p><b>Bepaald:</b> el / la · meervoud <b>los / las</b>. <b>Onbepaald:</b> un / una. '
  'Het lidwoord past zich aan aan <b>geslacht</b> én <b>getal</b>: <i>el país → los países</i>, <i>la ciudad → las ciudades</i>. '
  '🟡 Leer een substantief <b>altijd mét lidwoord</b> (el/la) — dan ken je meteen het geslacht.</p>'))
P(act(1, "¿el o la?",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Schrijf het juiste lidwoord. <span class="gloss">Let op de valstrikken (el idioma, el día).</span></p>'
  '<p style="margin-left:12.5mm">___ ciudad · ___ país · ___ dirección · ___ idioma · ___ edad · ___ nombre · ___ nacionalidad · ___ correo<br>'
  '<span class="wl full"></span></p>'))
P(act(2, "Haz la pregunta",
  [{"t":"✍️ Escribir","skill":True},{"t":"👥 Interacción","skill":True},{"t":"± 6 min"},{"t":"★★★"}],
  '<p>Bij dit antwoord — welke vraag stel je? <span class="gloss">productie — cue → geen steun.</span></p>'
  '<table class="mp"><thead><tr><th>Respuesta</th><th>Tu pregunta</th></tr></thead><tbody>'
  '<tr><td>Soy de Colombia.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Tengo 14 años.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Me llamo Nina.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Vivo en Madrid.</td><td><span class="wl md"></span></td></tr>'
  '</tbody></table>'))
P(act(3, "Encuesta: busca a alguien que…",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 Toda la clase"},{"t":"± 10 min"},{"t":"★★★"}],
  '<p>Interview drie klasgenoten (nombre, edad, ciudad, idiomas) en rapporteer in de 3e persoon. <span class="gloss">communicatief — geen steun. «Tom tiene 15 años y vive en…».</span></p>'
  '<table class="wtab mp"><thead><tr><th>Nombre</th><th>Edad</th><th>Ciudad</th><th>Idiomas</th></tr></thead><tbody>'
  '<tr><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '</tbody></table>'))
P(guide("Juega online:", "— «Palabras interrogativas», «Pregunta y respuesta» en «El o la» (met zelfcorrectie) op de digitale pagina."))
P('</div>')

# ---------- TALLER DE LENGUA ----------
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num" style="color:var(--crema)">✎</span><span class="pk" style="background:var(--gd)">Taller de lengua</span>')
P('<div class="intro"><b>ES:</b> Dos herramientas para escribir bien: la <b>mayúscula</b> (¿cuándo?) y los <b>conectores</b> (y, o, porque). <span class="gloss">Twee schrijfgereedschappen: hoofdletters (wanneer?) en verbindingswoorden.</span></div>')
P(lpd(("8","taalsysteem: ortografía + conectoren")))
P('</div>')
P('<h3 style="margin-top:6mm">Ortografía · mayúscula o minúscula</h3>')
P('<div class="fams" style="margin-top:4mm">')
P(pcard("MAYÚSCULA", '<div class="ej"><b>Países y ciudades:</b> España, Bélgica, Madrid, Sevilla · <b>nombres:</b> Lucía, Leo</div>'))
P(pcard("minúscula 🔴", '<div class="ej"><b>Nacionalidades e idiomas:</b> español, belga, francés · <b>días/meses</b> (→ U3)</div><div class="t2">NL schrijft «Spaans, Belg» mét hoofdletter — Spaans niet!</div>'))
P('</div>')
P(regla("Regla · mayúsculas",
  '<p><b>Land/stad/naam = hoofdletter</b> (España, Madrid). <b>Nationaliteit/taal = kleine letter</b> (español, belga). '
  '🟡 Ezelsbrug: <i>«el país grita, la nacionalidad susurra»</i> — het land «roept» (groot), de nationaliteit «fluistert» (klein).</p>'))
P('<h3 style="margin-top:6mm">Conectores · y · e · o · u · porque</h3>')
P('<table class="mp"><thead><tr><th>Conector</th><th>Uso</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td><b>y</b></td><td>en</td><td>Soy belga <b>y</b> hablo español.</td></tr>'
  '<tr><td><b>e</b></td><td>«en» vóór i-/hi-</td><td>español <b>e</b> inglés (niet <span class="trap">y inglés</span>)</td></tr>'
  '<tr><td><b>o</b> / <b>u</b></td><td>of (u vóór o-/ho-)</td><td>siete <b>u</b> ocho</td></tr>'
  '<tr><td><b>porque</b></td><td>want / omdat</td><td>Aprendo español <b>porque</b> me gusta.</td></tr>'
  '</tbody></table>')
P('<div class="truc"><b>🔴 Valstrik NL:</b> <i>want</i> én <i>omdat</i> = <b>porque</b> (één woord!). En «dus» = <b>así que / por eso</b>, niet <i>luego</i>.</div>')
P(act(1, "Corrige las mayúsculas",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Onderstreep de fout en herschrijf correct. <span class="gloss">«soy Español y vivo en bélgica».</span></p>'
  '<p style="margin-left:12.5mm">1) soy Español y vivo en bélgica → <span class="wl lg"></span><br>'
  '2) Ella habla Francés e Inglés → <span class="wl lg"></span></p>'))
P(act(2, "Une con y / e / o / u / porque",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het juiste verbindingswoord in.</p>'
  '<p style="margin-left:12.5mm">a) Hablo neerlandés ___ inglés. &nbsp; b) ¿Tienes siete ___ ocho años? &nbsp; c) Estudio español ___ me gusta viajar. &nbsp; d) español ___ italiano.<br><span class="wl full"></span></p>'))
P('</div>')

# ---------- CULTURA ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">★</span><span class="pk">Cultura · Madrid y los nombres hispanos</span>')
P('<div class="intro"><b>ES:</b> En el mundo hispano la gente tiene <b>dos apellidos</b> — uno del padre y uno de la madre. Y tratamos de <b>tú</b> o de <b>usted</b> según la situación. <span class="gloss">In de Spaanstalige wereld heeft men twee achternamen — één van vader, één van moeder. En je zegt «tú» of «usted» naargelang de situatie.</span></div>')
P(lpd(("5","kenmerkende aspecten van de Spaanstalige cultuur"), ("2","relevante info uit een tekst")))
P('</div>')
P('<div class="fams" style="margin-top:6mm">')
P(pcard("Madrid 🇪🇸", '<div class="ej">De hoofdstad van España, ~3,3 miljoen inwoners. Bekend: la <b>Puerta del Sol</b>, el <b>Prado</b>, el <b>Retiro</b>, el <b>Real Madrid</b>.</div><div class="anchor gloss">Onze eerste parada: het vertrekpunt van La Ruta.</div>'))
P(pcard("Los dos apellidos", '<div class="ej"><b>Lucía Ramírez García</b>: <i>Ramírez</i> (padre) + <i>García</i> (madre). Bij trouwen verander je je naam <b>niet</b>.</div><div class="t2">NL heeft één achternaam — hier zijn er twee.</div>'))
P('</div>')
P('<div class="truc"><b>🟡 Tú of usted?</b> Met vrienden/leeftijdsgenoten: <b>tú</b>. Beleefd of tegen een onbekende volwassene: <b>usted</b> (+ ser = <i>es</i>). In Colombia/Perú hoor je vaker <i>usted</i>; in España overheerst <i>tú</i>. Later (C6) ontmoet je Mateo uit Argentina met <b>vos</b>.</div>')
P(act(1, "Escribe tres nombres a la manera hispana",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p>Bedenk drie namen met <b>nombre + apellido del padre + apellido de la madre</b>.</p>'
  '<p style="margin-left:12.5mm"><span class="wl full"></span><span class="wl full"></span><span class="wl full"></span></p>'))
P(act(2, "¿Tú o usted?",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p>Kies per situatie <b>tú</b> of <b>usted</b> en zeg de begroeting. <span class="gloss">a) een klasgenoot · b) de directeur · c) een kind · d) een oude mevrouw.</span></p>'
  '<p style="margin-left:12.5mm">a) <span class="wl md"></span> &nbsp; b) <span class="wl md"></span> &nbsp; c) <span class="wl md"></span> &nbsp; d) <span class="wl md"></span></p>'))
P('</div>')

# ---------- TAREA FINAL ----------
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num">✦</span><span class="pk" style="background:var(--gd)">Tarea final · Mi pasaporte</span>')
P('<div class="intro"><b>ES:</b> Crea tu <b>pasaporte de La Ruta</b> y preséntate. Puedes usar tu identidad real o una <b>identidad nueva</b> (nombre, país, edad). <span class="gloss">Maak je La Ruta-paspoort en stel je voor — echt of met een nieuwe, fictieve identiteit.</span></div>')
P('<div class="route-note">🎯 <b>Communicatieve taak:</b> afzender = jij · ontvanger = de klas/Lucía · doel = jezelf voorstellen · situatie = aankomst in Madrid · resultaat = een ingevuld paspoort + een gesproken/geschreven voorstelling.</div>')
P(lpd(("3","doelgericht schrijven met een voorbeeld"), ("4","zich mondeling voorstellen"), ("7","woordenschat"), ("8","ser/presente/artículos")))
P('</div>')
P('<ol class="pasos">'
  '<li><b>Elige tu identidad.</b> Nombre + dos apellidos, país, ciudad, edad, idiomas. <span class="gloss">Kies je (fictieve) identiteit.</span></li>'
  '<li><b>Rellena el pasaporte</b> hieronder (in hele woorden).</li>'
  '<li><b>Escribe tu presentación</b> (5–6 frases) met ser + presente + conectoren.</li>'
  '<li><b>Preséntate</b> a la clase (of neem een filmpje/audio op via de digitale pagina).</li>'
  '<li><b>Pregunta</b> a un compañero y presenta a esa persona en 3ª persona.</li>'
  '</ol>')
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
P(audiorow('<div class="ic">🎬</div><div><b>Graba tu presentación</b> en la página digital (recorder + rúbrica).<span class="gloss"> Neem je voorstelling op via de digitale pagina — met opnameknop en zelfevaluatie.</span></div>',
           qr("Escanea y graba", "Tarea · Mi pasaporte", seed=41)))
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré? <span class="gloss" style="font-size:8pt">— evalueer je eigen paspoort</span></div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Mijn paspoort heeft <b>alle gegevens</b> (nombre, país, edad, ciudad, idiomas)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>ser</b> en het <b>presente</b> correct</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik verbind met <b>y / porque</b> en schrijf <b>mayúsculas</b> juist</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>stel mezelf mondeling voor</b> en versta een klasgenoot</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '</table>')
P('</div>')

# ---------- REPASO ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">✓</span><span class="pk">Repaso · lo esencial</span>')
P('<div class="intro"><b>ES:</b> Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag. De volledige herhaling met spelletjes staat online.</span></div>')
P('</div>')
P('<div class="esen"><b class="tt">Lo esencial de un vistazo</b><ul>'
  '<li><b>Presentarse:</b> Me llamo… · Soy de… · Soy + nationaliteit · Tengo … años · Vivo en… · Hablo…</li>'
  '<li><b>Ser:</b> soy · eres · es · somos · sois · son. <b>Presente reg.:</b> -o/-as/-a/-amos/-áis/-an (-ar).</li>'
  '<li><b>Preguntar:</b> ¿Cómo? ¿De dónde? ¿Dónde? ¿Cuántos años? ¿Cuál? ¿Qué? ¿Quién?</li>'
  '<li><b>Artículos:</b> el/la · los/las · un/una (leer met lidwoord!).</li>'
  '<li><b>Las trampas:</b> 🔴 edad = <b>tener</b> · 🔴 nationaliteit = <b>kleine letter</b> · 🔴 ¿Cuál? vóór ser · 🔴 want/omdat = <b>porque</b>.</li>'
  '</ul></div>')
P(guide("Repasa jugando (online):", "— 18 spelletjes op de digitale pagina: país↔nacionalidad, ser/tener, interrogativos, ¡Preséntate!, Caza de mayúsculas… met zelfcorrectie en spreiding.", "🎮"))
P('<div class="se" style="margin-top:6mm">Semáforo — ¿cómo lo llevas?</div>')
P('<table class="sem"><tr class="semrow"><th>Puedo…</th><th>🔴 nog niet</th><th>🟠 met steun</th><th>🟢 zelfstandig</th></tr>'
  '<tr><td>mezelf <b>voorstellen</b> (naam, land, leeftijd, stad)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>het verbo <b>ser</b> en het presente regular gebruiken</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>iemand <b>vragen</b> stellen (¿Cómo? ¿De dónde?…)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>het juiste <b>lidwoord</b> (el/la, un/una) kiezen</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>landen & nationaliteiten <b>herkennen</b> (mayúsculas)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '</table>')
P('<div class="bridge"><b>» Siguiente parada: Sevilla (U2).</b> Ya sabes decir quién eres; en <b>U2 «Mi gente»</b> presentas a tu <b>familia</b> con Lucía en Andalucía — con <i>tener</i>, los posesivos y describir a las personas. <span class="gloss">Je kunt zeggen wie je bent; in U2 stel je je familie voor in Sevilla.</span></div>')
P('</div>')

# ---------- §V VOCABULARIO ----------
import json
VOC = json.load(open(f"{HERE}/u1_vocab.json", encoding="utf-8"))
GRP = [("datos","Datos personales"),("ficha","La ficha / el formulario"),("interrog","Palabras interrogativas"),
       ("saludos","Saludos (recyclen U0)"),("pais","Países y nacionalidades — mundo hispano"),("mundo","Países del mundo")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Alle woorden van de unit. Online: flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (receptief & productief)")))
P('</div>')
for key, titel in GRP:
    items = [v for v in VOC if v.get("grp") == key]
    if not items: continue
    P(f'<h3 style="margin-top:6mm">{titel} <span class="gloss" style="font-size:8pt">· {len(items)} woorden</span></h3>')
    rows = "".join(f'<tr><td><b>{v["es"]}</b></td><td>{v["nl"]}</td><td class="gloss">{v["soort"]}</td><td class="gloss">{v["ej"]}</td></tr>' for v in items)
    P(f'<table class="alf"><thead><tr><th>Español</th><th>Nederlands</th><th>ERK/soort</th><th>Ejemplo</th></tr></thead><tbody>{rows}</tbody></table>')
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Oefenladder online:</span> <span class="g">herkennen → onderscheiden → ophalen → gestuurd → vrij. De flip cards en spellen bouwen de steun af tot je álles zonder hulp kent.</span></div></div>')
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Mi palabra favorita de U1: <span class="wl md"></span> · Una difícil: <span class="wl md"></span></i></div>')
P('</div>')

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
 var SEL='h1,h2,h3,h4,p,td,th,li,.intro,.hist,.gloss,.ojo,.anchor,.ej,.q,.sub,.route-note,.pk,.se,.divider,.t,.t2,.nl,.es,.lpdchip,.lpdlab,.wcol .ch,.bub,.k,.v';
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
        + CSS + '</style></head><body>\n' + "".join(BODY) + EDITBAR + '\n</body></html>')
OUT = f"{HERE}/U1.html"
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, "·", len(HTML), "bytes")
