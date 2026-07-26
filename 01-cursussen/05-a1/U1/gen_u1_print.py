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

def steun(niveau):
    return f'<div class="steun" style="margin-left:12.5mm">Apoyo: {niveau}</div>'

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
      <div class="ojo"><b>¡Ojo! — valstrik:</b> leeftijd zeg je met <b>tener</b>, niet met <i>ser</i>: <b>Tengo</b> 15 años (✔), niet <span class="trap">Soy 15 años</span> (✘). NL zegt «ik <i>ben</i> 15 jaar», Spaans «ik <i>heb</i> 15 jaar».</div>
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
      <div class="ej" style="margin-top:2mm">📄 el libro (dit boek) · 🎮 la <b>página digital</b> (18 spellen, audio, flip cards) · 📊 el PowerPoint. De <b>QR</b>-codes brengen je naar de juiste online-oefening.</div>
      <div class="anchor gloss" style="margin-top:2mm">Print werkt <b>volledig zonder</b> scherm; online voegt audio, opname en zelfcorrectie toe. Het <b>repaso</b> (herhaling) staat online.</div></div>
  </div>
</div>
''')

# ---------- §0 Ponte al día ----------
P('<div class="page"><div class="parada sec">')
P('<span class="num">0</span><span class="pk">§0 · ¡Ponte al día!</span>')
P('<div class="intro"><b>ES:</b> Antes de empezar, recordamos lo que ya sabes de la Unidad 0 y que necesitas hoy: <b>saludar</b>, <b>deletrear</b> y los <b>números</b> (para la edad y el teléfono). <span class="gloss">Voor we starten: kort ophalen wat je al kent uit U0 en vandaag nodig hebt — groeten, spellen en getallen.</span></div>')
P(lpd(("7","woordenschat inzetten"), ("9","strategieën / lengua de clase")))
P('</div>')
P('<div class="fams three" style="margin-top:6mm">')
P(pcard("Saludar", '<div class="ej"><b>¡Hola!</b> · <b>Buenos días</b> · <b>¿Qué tal?</b> · <b>Encantado/-a</b> · <b>Adiós</b></div><div class="anchor gloss">groeten, kennismaken, afscheid</div>'))
P(pcard("Deletrear", '<div class="ej">a·be·ce… <b>¿Cómo se escribe?</b> · <b>con hache</b> / <b>sin hache</b> · <b>una arroba (@)</b></div><div class="anchor gloss">je naam en e-mail spellen</div>'))
P(pcard("Números 0–100", '<div class="ej"><b>catorce · quince · dieciséis</b> · <b>veintiuno</b> · <b>treinta y cinco</b></div><div class="anchor gloss">voor leeftijd & telefoonnummer</div>'))
P('</div>')
P(actx(1, "Calentamiento: preséntate como en U0",
      [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 4 min"},{"t":"★☆☆"}],
      '<p>Zeg tegen je buur: <span class="words"><b>¡Hola!</b></span> + je naam + spel je voornaam. Je buur schrijft ze op de lijn. Wissel daarna.</p>'
      '<p style="margin-left:12.5mm">Mi nombre: <span class="wl lg"></span> &nbsp; El nombre de mi compañero/a: <span class="wl lg"></span></p>', apoyo="MODELO → SIN AYUDA"))
P(actx(2, "Los números que necesito hoy",
      [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
      '<p>Schrijf het getal in letters (recyclen U0). <span class="gloss">Nodig voor je leeftijd en telefoonnummer.</span></p>'
      '<table class="mp"><thead><tr><th>Cifra</th><th>En letras</th><th>Cifra</th><th>En letras</th></tr></thead>'
      '<tbody><tr><td>14</td><td><span class="wl md"></span></td><td>30</td><td><span class="wl md"></span></td></tr>'
      '<tr><td>16</td><td><span class="wl md"></span></td><td>21</td><td><span class="wl md"></span></td></tr></tbody></table>', apoyo="PISTA (16–29 = één woord)"))
P(actx(3, "¿Qué se dice en clase?",
      [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 3 min"},{"t":"★☆☆"}],
      '<p>Verbind de klaszin met zijn functie (schrijf de letter). <span class="gloss">lengua de clase — recyclen U0.</span></p>'
      '<table class="mp"><thead><tr><th>Frase</th><th></th><th>Función</th></tr></thead><tbody>'
      '<tr><td>1 · ¿Cómo se dice…?</td><td><span class="wl sm"></span></td><td>A · niet begrepen</td></tr>'
      '<tr><td>2 · ¿Puedes repetir?</td><td><span class="wl sm"></span></td><td>B · hoe zeg je…?</td></tr>'
      '<tr><td>3 · No entiendo.</td><td><span class="wl sm"></span></td><td>C · herhaal a.u.b.</td></tr></tbody></table>', apoyo="BANCO"))
P(guide("Repasa jugando (online):", "— números, saludos en spellen staan als spelletjes op de digitale pagina. Eén QR verder oefen je alles met zelfcorrectie."))
P('</div>')  # close page

# ================= §1 · TUS DATOS PERSONALES =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">1</span><span class="pk">§1 · Tus datos personales</span>')
P('<div class="route-note">📍 Parada 1 · Madrid — Lucía te pregunta quién eres.</div>')
P('<div class="intro"><b>ES:</b> Primero <b>reconoces</b> los datos en una ficha, después los <b>usas</b> para presentarte. La ruta: observar → practicar con apoyo → comunicar. <span class="gloss">Eerst herken je de gegevens op een fiche, daarna gebruik je ze om jezelf voor te stellen.</span></div>')
P(lpd(("7","woordenschat: datos personales"), ("2","relevante info in een ficha"), ("3","doelgericht schrijven met steun"), ("4","mondelinge interactie")))
P('</div>')

# ---- §1.1 los datos (gelabelde scène → reconocer/onderscheiden/ophalen) ----
P('<h3 style="margin-top:6mm">§1.1 · Los datos — observa la ficha</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto.</b> Esta es la ficha de Lucía. Léela y adivina las palabras <b>sin</b> mirar la traducción (está pequeña). <span class="gloss">Lees de fiche; raad de woorden zónder de kleine vertaling.</span></p>')
P('<div class="fichacard">'
  '<div><div class="row"><span class="k">el nombre</span><span class="v">Lucía <span class="nl">voornaam</span></span></div>'
  '<div class="row"><span class="k">el apellido</span><span class="v">Ramírez García <span class="nl">achternaam (×2!)</span></span></div>'
  '<div class="row"><span class="k">la edad</span><span class="v">16 años <span class="nl">leeftijd</span></span></div>'
  '<div class="row"><span class="k">el país</span><span class="v">España <span class="nl">land</span></span></div></div>'
  '<div><div class="row"><span class="k">la nacionalidad</span><span class="v">española <span class="nl">nationaliteit</span></span></div>'
  '<div class="row"><span class="k">la ciudad</span><span class="v">Sevilla <span class="nl">stad</span></span></div>'
  '<div class="row"><span class="k">los idiomas</span><span class="v">español, inglés <span class="nl">talen</span></span></div>'
  '<div class="row"><span class="k">el correo</span><span class="v">lucia@mail.com <span class="nl">e-mail</span></span></div></div></div>')
P('<p style="font-size:9.4pt">② <b>Observa.</b> ¿Qué palabras entiendes sin traducción? <span class="gloss">nombre · dirección · correo… (cognaten). Welke lijken op het Nederlands/Engels?</span></p>')
P(regla("Regla · los datos",
  '<p><b>el nombre</b> = voornaam · <b>el apellido</b> = achternaam (in España <b>dos apellidos</b>: van vader én moeder → Cultura). '
  '<b>la nacionalidad</b> ≠ el país: <i>España</i> (land) → <i>español/española</i> (nationaliteit). 🔴 <b>la dirección</b> = adres (geen «directie»).</p>'))
P(actx(1, "Empareja el dato con el ejemplo",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p><i>werkvorm: beeld-/woordkoppeling.</i> Verbind het gegeven met het juiste voorbeeld (schrijf de letter).</p>'
  '<table class="mp"><thead><tr><th>Dato</th><th>Letra</th><th></th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td>1 · el apellido</td><td><span class="wl sm"></span></td><td>A</td><td>16 años</td></tr>'
  '<tr><td>2 · la edad</td><td><span class="wl sm"></span></td><td>B</td><td>española</td></tr>'
  '<tr><td>3 · la nacionalidad</td><td><span class="wl sm"></span></td><td>C</td><td>García</td></tr>'
  '<tr><td>4 · el correo</td><td><span class="wl sm"></span></td><td>D</td><td>lucia@mail.com</td></tr>'
  '<tr><td>5 · la ciudad</td><td><span class="wl sm"></span></td><td>E</td><td>Sevilla</td></tr>'
  '</tbody></table>', apoyo="MODELO (ficha zichtbaar)"))
P(actx(2, "Clasifica: ¿dato, país o pregunta?",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: semantisch sorteren.</i> Schrijf elk woord in de juiste kolom. <span class="words"><b>nombre · España · ¿Cómo? · edad · Bélgica · ¿Dónde? · apellido · México</b></span></p>'
  + sortcols([("dato personal","(nombre…)"),("país","(España…)"),("interrogativo","(¿…?)")]), apoyo="BANCO → voeg eigen woord toe"))
P(actx(3, "Completa tu ficha",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: gelabelde ficha afbouwen.</i> Vul je <b>eigen</b> ficha in (echt of fictief, kies je voor de eindtaak).</p>'
  '<div class="fichacard"><div>'
  '<div class="row"><span class="k">Nombre</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Apellido</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Edad</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">País</span><span class="v"><span class="wl md"></span></span></div></div><div>'
  '<div class="row"><span class="k">Nacionalidad</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Ciudad</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Idiomas</span><span class="v"><span class="wl md"></span></span></div>'
  '<div class="row"><span class="k">Correo</span><span class="v"><span class="wl md"></span></span></div></div></div>', apoyo="MARCO (labels gegeven)"))
P(actx(4, "Completa las palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: onvolledige woorden.</i> Vul de ontbrekende letters aan (spellinggevoelige datos).</p>'
  '<p style="margin-left:12.5mm">na__ona__dad · ap__l__do · di__ec__ión · i__ioma · c__rr__o<br><span class="wl full"></span></p>'
  '<p style="margin-left:12.5mm" class="gloss">[antwoord-laag online] nacionalidad · apellido · dirección · idioma · correo</p>', apoyo="PISTA (aantal letters)"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha a cuatro personas y anota su dato que falta.</b> <span class="gloss">Luister; noteer per persoon het ontbrekende gegeven (país of edad) — selectief luisteren.</span></div>',
           qr("Escanea y escucha", "Audio 1.1 · Datos · 0:55", seed=11)))
P('</div>')  # page §1.1

# ---- §1.2 presentarse (gestuurd → vrij → comunicar) ----
P('<div class="page">')
P('<div class="divider">Presentarse · §1.2</div>')
P('<h3>§1.2 · Presentarse — de zin, kleur per functie</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto.</b> Lucía te escribe por chat. Observa cómo se presenta ella y cómo respondes tú. <span class="gloss">Observeer de kleuren: elke kleur = een taalfunctie.</span></p>')
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
P(actx(5, "Construye con la tabla de sustitución",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: substitutietabel.</i> Combineer een correcte zin uit elke rij en schrijf ze op.</p>'
  '<table class="mp"><thead><tr><th>Persona</th><th>Verbo</th><th>Aanvulling</th></tr></thead><tbody>'
  '<tr><td>(Yo)</td><td>me llamo / soy de / vivo en / tengo / hablo</td><td>Leo · Bélgica · Gante · 15 años · español</td></tr></tbody></table>'
  '<p style="margin-left:12.5mm">1) <span class="wl full"></span>2) <span class="wl full"></span>3) <span class="wl full"></span></p>', apoyo="MARCO → SIN AYUDA"))
P(actx(6, "Cue → frase completa",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: cue naar volledige zin.</i> Maak een hele zin van de aanwijzingen.</p>'
  '<table class="mp"><thead><tr><th>Cue</th><th>Frase</th></tr></thead><tbody>'
  '<tr><td>yo / llamarse / Sara</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>yo / ser de / México</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>yo / tener / 14 años</td><td><span class="wl lg"></span></td></tr>'
  '<tr><td>yo / vivir en / Madrid</td><td><span class="wl lg"></span></td></tr></tbody></table>', apoyo="PISTA (werkwoord gegeven)"))
P(actx(7, "Preséntate en cinco frases",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 7 min"},{"t":"★★★"}],
  '<p><i>werkvorm: onderschrift/vrije productie klein.</i> Schrijf vijf ware zinnen over jezelf en zeg ze hardop tegen je buur.</p>'
  '<div class="wbox"></div>', apoyo="SIN AYUDA (ronde 2 uit het hoofd)"))
# Tarea comunicativa §1
P(tarea_com("Tarea comunicativa · «Busca a alguien que…»",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 Toda la clase"},{"t":"± 10 min"},{"t":"★★★"}],
  '<p><b>Afzender/ontvanger/doel/situatie/resultaat:</b> jij interviewt klasgenoten om iemand te vinden per voorwaarde, en <b>rapporteert</b> in de 3e persoon. <span class="gloss">«Busca a alguien que… vive en una ciudad grande / tiene 15 años / habla tres idiomas.»</span></p>'
  '<table class="wtab mp"><thead><tr><th>Busca a alguien que…</th><th>Nombre</th><th>Nota (3ª pers.)</th></tr></thead><tbody>'
  '<tr><td>…tiene 15 años</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>…vive en una ciudad grande</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>…habla más de dos idiomas</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '</tbody></table>'
  '<p style="margin-left:12.5mm">Resultado (rapport): <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: SIN AYUDA · [CROSS: HTML «¡Preséntate!» + recorder]</div>'))
P(guide("Juega online:", "— «Memoria de los datos», «país ↔ nacionalidad» en «¡Preséntate!» met zelfcorrectie op de digitale pagina."))
P('</div>')  # page §1.2

# ================= §2 · EL VERBO SER =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">2</span><span class="pk">§2 · El verbo SER + los pronombres</span>')
P('<div class="intro"><b>ES:</b> Para decir <b>quién eres</b> y <b>de dónde eres</b> usas <b>ser</b>. Es irregular pero cortísimo y lo usas todo el año. <span class="gloss">Om te zeggen wie je bent en waar je vandaan komt, gebruik je «ser». Onregelmatig, maar heel kort.</span></div>')
P(lpd(("8","taalsysteem: ser + pronombres"), ("3","zich voorstellen (productief)"), ("4","interactie")))
P('</div>')
# §2.1 vorm
P('<h3 style="margin-top:6mm">§2.1 · La forma — observa quién usa qué</h3>')
P('<p style="font-size:9.6pt">① <b>Contexto (input flood).</b> Lee el mini-diálogo y <b>subraya</b> cada forma de <i>ser</i>. <span class="gloss">Onderstreep elke vorm van ser.</span></p>')
P('<div class="chat">'
  '<div class="chatline you"><div class="bub"><span class="fx per">Yo</span> <b>soy</b> Lucía. ¿<span class="fx per">Tú</span> <b>eres</b> de Bélgica? <span class="fx per">Diego</span> <b>es</b> de México.</div><div class="who">Lucía</div></div>'
  '<div class="chatline me"><div class="bub">Sí. <span class="fx per">Nosotros</span> <b>somos</b> de Flandes. Y vosotros, ¿<b>sois</b> estudiantes? Ellas <b>son</b> profesoras.</div><div class="who">Tú</div></div></div>')
P('<table class="conj"><thead><tr><th>Persona</th><th>ser</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td class="p">yo</td><td class="v">soy</td><td>Soy Leo, soy belga.</td></tr>'
  '<tr><td class="p">tú</td><td class="v">eres</td><td>¿De dónde eres?</td></tr>'
  '<tr><td class="p">él / ella / usted</td><td class="v">es</td><td>Lucía es española.</td></tr>'
  '<tr><td class="p">nosotros/-as</td><td class="v">somos</td><td>Somos de Bélgica.</td></tr>'
  '<tr><td class="p">vosotros/-as</td><td class="v">sois</td><td>¿Sois estudiantes?</td></tr>'
  '<tr><td class="p">ellos/-as / ustedes</td><td class="v">son</td><td>Son de México.</td></tr>'
  '</tbody></table>')
P(regla("Regla · SER (irregular)",
  '<p><b>soy · eres · es · somos · sois · son.</b> Voor: <b>identiteit</b> (soy Leo), <b>afkomst</b> (soy de Bélgica), <b>nationaliteit</b> (soy belga), <b>eigenschap</b> (es simpático). '
  '🔴 Onderwerpwoorden (<i>yo, tú…</i>) mag je <b>weglaten</b>: <i>(Yo) soy Leo</i>.</p>'))
P('<div class="truc"><b>🟡 Truc — tú vs. usted:</b> tegen leeftijdsgenoten <b>tú eres</b>; beleefd/onbekende volwassene <b>usted es</b> (3e persoon!). España veel <i>tú</i>; delen van LatAm vaker <i>usted</i> (→ Cultura).</div>')
P(actx(1, "Rueda de personas: elige la forma",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p><i>werkvorm: vervoegingswiel.</i> Vul de juiste vorm van <b>ser</b> in.</p>'
  '<p style="margin-left:12.5mm">a) Yo <span class="wl sm"></span> de Gante. &nbsp; b) ¿Tú <span class="wl sm"></span> español? &nbsp; c) Lucía <span class="wl sm"></span> de Sevilla.<br>'
  'd) Nosotros <span class="wl sm"></span> belgas. &nbsp; e) Diego y Nina <span class="wl sm"></span> de América. &nbsp; f) ¿Vosotros <span class="wl sm"></span> amigos?</p>', apoyo="BANCO (tabel open)"))
P(actx(2, "Una cosa cambia",
  [{"t":"🔍 Analizar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: één verandering tegelijk.</i> Begin met <b>«Yo soy de Bélgica.»</b> en pas telkens <b>één</b> ding aan.</p>'
  '<p style="margin-left:12.5mm">→ maak <b>tú</b>: <span class="wl lg"></span><br>→ maak <b>nosotros</b>: <span class="wl lg"></span><br>→ maak <b>ella</b> + España: <span class="wl lg"></span></p>', apoyo="PISTA"))
P(audiorow('<div class="ic">🎧</div><div><b>Escucha seis frases con «ser» y marca la persona.</b> <span class="gloss">Luister; kruis per zin de persoon aan (yo/tú/él/nosotros…) — receptief, klank van de vorm.</span></div>',
           qr("Escanea y escucha", "Audio 2.1 · Ser · 0:45", seed=21)))
P(actx(4, "Escucha y marca la persona",
  [{"t":"👂 Escuchar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: luisteren en aanwijzen.</i> Kruis aan wélke persoon je hoort.</p>'
  '<table class="mp"><thead><tr><th>#</th><th>yo</th><th>tú</th><th>él/ella</th><th>nosotros</th><th>ellos</th></tr></thead><tbody>'
  '<tr><td>1</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>2</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>3</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>4</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr></tbody></table>', apoyo="MODELO (tabel ser open)"))
# §2.2 usos + foutenkliniek
P('<div class="divider">Los usos + práctica · §2.2</div>')
P('<div class="fams" style="margin-top:2mm">')
P(pcard("Identidad + origen", '<div class="ej"><b>Soy</b> Leo. · <b>Soy de</b> Bélgica.</div><div class="anchor gloss">wie · waar vandaan</div>'))
P(pcard("Nacionalidad + cualidad", '<div class="ej"><b>Soy</b> belga. · Lucía <b>es</b> simpática.</div><div class="anchor gloss">nationaliteit · eigenschap</div>'))
P('</div>')
P(actx(3, "Clínica de errores",
  [{"t":"🔍 Analizar","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>werkvorm: foutenkliniek.</i> Zoek de fout, verbeter, en leg uit <b>waarom</b> (het correcte model staat als laatste).</p>'
  '<p style="margin-left:12.5mm">1) <span class="trap">Soy 15 años.</span> → <span class="wl lg"></span> <span class="gloss">(waarom? )</span><br>'
  '2) <span class="trap">Yo es de Bélgica.</span> → <span class="wl lg"></span><br>'
  '3) <span class="trap">Nosotros somos Español.</span> → <span class="wl lg"></span></p>', apoyo="MODELO-correctie → SIN AYUDA"))
P(tarea_com("Tarea comunicativa · Entrevista con marco",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p>Interview je buur met <b>ser</b> (naam, afkomst, nationaliteit) en presenteer die persoon daarna in de 3e persoon aan de klas. <span class="gloss">«Ella es Sara, es de Amberes, es belga.»</span></p>'
  '<p style="margin-left:12.5mm">Mi compañero/a: <span class="wl full"></span></p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: MARCO (¿Cómo…? ¿De dónde…?) → SIN AYUDA</div>'))
P(guide("Juega online:", "— «El verbo SER» (welke persoon?) en «Presente Tetris» op de digitale pagina."))
P('</div>')  # page §2

# ================= §3 · EL PRESENTE REGULAR =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">3</span><span class="pk">§3 · El presente regular (-ar · -er · -ir)</span>')
P('<div class="intro"><b>ES:</b> Casi todos los verbos siguen un <b>patrón</b>. Aprende las tres familias y podrás hablar de lo que <b>haces</b>. <span class="gloss">Bijna alle werkwoorden volgen een patroon; leer de drie families.</span></div>')
P(lpd(("8","taalsysteem: presente regular"), ("3","vertellen over jezelf")))
P('</div>')
# §3.1 patroon
P('<h3 style="margin-top:6mm">§3.1 · El patrón — quita y añade</h3>')
P('<p style="font-size:9.6pt">① <b>Observa (bouwstroken).</b> De stam blijft, de <b>uitgang</b> verandert per persoon. <span class="gloss">De oranje uitgang is het enige dat wisselt.</span></p>')
P('<div class="fams three" style="margin-top:4mm">')
for inf, ends in [("hablar (-ar)", ["o","as","a","amos","áis","an"]),
                  ("aprender (-er)", ["o","es","e","emos","éis","en"]),
                  ("vivir (-ir)", ["o","es","e","imos","ís","en"])]:
    stem = inf.split()[0][:-2]
    rows = "".join(f'<tr><td class="p">{p}</td><td>{stem}<span class="end">{e}</span></td></tr>'
                   for p, e in zip(["yo","tú","él/ella","nosotros","vosotros","ellos"], ends))
    P(pcard(inf, f'<table class="conj"><tbody>{rows}</tbody></table>'))
P('</div>')
P(regla("Regla · presente regular",
  '<p><b>-er</b> en <b>-ir</b> zijn bijna gelijk — alleen bij <b>nosotros/vosotros</b> verschillen ze (-emos/-éis vs. -imos/-ís). De <b>yo</b>-vorm eindigt altijd op <b>-o</b>. 🟡 Ken je de yo-vorm, dan ken je het patroon.</p>'))
P(actx(1, "Ordena por familia",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: patroon sorteren.</i> Sorteer de infinitieven per klasse. <span class="words"><b>hablar · comer · vivir · estudiar · aprender · escribir · trabajar · beber · abrir</b></span></p>'
  + sortcols([("-ar",""),("-er",""),("-ir","")]), apoyo="BANCO → +1 eigen woord"))
P(actx(2, "Conjuga en presente",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: substitutietabel.</i> Vervoeg (de kaarten mogen open).</p>'
  '<table class="mp"><thead><tr><th>Infinitivo</th><th>yo</th><th>tú</th><th>nosotros</th></tr></thead><tbody>'
  '<tr><td>hablar</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>aprender</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>vivir</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '<tr><td>estudiar</td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '</tbody></table>', apoyo="MODELO → PISTA"))
# §3.2 gebruik
P('<div class="divider">Usar el presente · §3.2</div>')
P(actx(3, "Cadena de transformación",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★★"}],
  '<p><i>werkvorm: transformatieketting.</i> Begin met <b>«Yo hablo español.»</b> en voer elke opdracht uit (schrijf telkens de hele zin).</p>'
  '<p style="margin-left:12.5mm">→ maak <b>ontkennend</b>: <span class="wl lg"></span><br>→ maak er een <b>vraag</b> van: <span class="wl lg"></span><br>→ verander onderwerp naar <b>nosotros</b>: <span class="wl lg"></span><br>→ voeg <b>«en el instituto»</b> toe: <span class="wl lg"></span></p>', apoyo="PISTA → SIN AYUDA"))
P(actx(4, "Amplía la frase",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: zin uitbreiden.</i> Start met <b>«Estudio.»</b> en voeg stap voor stap toe: <span class="gloss">wat · waar · wanneer · waarom.</span></p>'
  '<div class="wbox sm"></div>', apoyo="MARCO (wat/waar/wanneer/waarom)"))
P(audiorow('<div class="ic">🎧</div><div><b>Microdictado.</b> Escucha dos veces y escribe. 1ª ronda: ¿de qué trata? · 2ª ronda: escribe las frases. <span class="gloss">Luister 2×: eerst betekenis, dan schrijf je de zinnen.</span></div>',
           qr("Escanea y escucha", "Audio 3.2 · Microdictado · 0:40", seed=31)))
P(actx(5, "Microdictado con reconstrucción",
  [{"t":"👂 Escuchar","skill":True},{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 6 min"},{"t":"★★★"}],
  '<p><i>werkvorm: microdictogloss.</i> Reconstrueer de drie zinnen die je hoort en maak daarna één <b>eigen</b> variant.</p>'
  '<p style="margin-left:12.5mm">1) <span class="wl full"></span>2) <span class="wl full"></span>3) <span class="wl full"></span></p>'
  '<p style="margin-left:12.5mm">Mi variante: <span class="wl full"></span></p>', apoyo="eerste letter → SIN AYUDA (retrieval vóór model)"))
P(tarea_com("Tarea comunicativa · 4/3/2 «Un día en mi vida»",
  [{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 8 min"},{"t":"★★★"}],
  '<p>Vertel in <b>4/3/2</b>-ronden (telkens sneller, andere partner) drie dingen die je doet, met <b>hablar · estudiar · vivir</b>. <span class="gloss">Doel: vlotter worden, niet meer inhoud.</span></p>'
  '<p style="margin-left:12.5mm">Mis notas: <span class="wl full"></span> ☐ 4 min ☐ 3 min ☐ 2 min</p>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: notas → SIN AYUDA</div>'))
P(guide("Ojo — conjugador online:", "— alle vervoegingen (nagerekend, ~1000 werkwoorden) staan in de aparte cursus-tool «Conjugador», niet hier. Hier oefen je met «Presente Tetris».", "🔁"))
P('</div>')  # page §3

# ================= §4 · PREGUNTAR + GÉNERO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">4</span><span class="pk">§4 · Preguntar: interrogativos + el/la</span>')
P('<div class="intro"><b>ES:</b> Ya sabes presentarte; ahora aprende a <b>preguntar</b> a los demás — y a poner el <b>artículo</b> correcto. <span class="gloss">Je kunt je voorstellen; nu leer je vragen stellen en het juiste lidwoord kiezen.</span></div>')
P(lpd(("8","taalsysteem: interrogativos, género/número, artículos"), ("4","mondelinge interactie: vragen stellen")))
P('</div>')
# §4.1 interrogativos
P('<h3 style="margin-top:6mm">§4.1 · Las palabras interrogativas</h3>')
P('<p style="font-size:9.6pt">① <b>Observa (spiegel).</b> Elk vraagwoord «zoekt» een soort antwoord. <span class="gloss">¿De dónde? → origen · ¿Cuántos años? → edad.</span></p>')
P('<table class="mp"><thead><tr><th>Pregunta</th><th>Sirve para…</th><th>Respuesta modelo</th></tr></thead><tbody>'
  '<tr><td><b>¿Cómo</b> te llamas?</td><td>de naam</td><td>Me llamo Leo.</td></tr>'
  '<tr><td><b>¿De dónde</b> eres?</td><td>de afkomst</td><td>Soy de Bélgica.</td></tr>'
  '<tr><td><b>¿Dónde</b> vives?</td><td>de woonplaats</td><td>Vivo en Gante.</td></tr>'
  '<tr><td><b>¿Cuántos años</b> tienes?</td><td>de leeftijd</td><td>Tengo 15 años.</td></tr>'
  '<tr><td><b>¿Cuál</b> es tu correo?</td><td>een gegeven (keuze)</td><td>Es leo@mail.com.</td></tr>'
  '<tr><td><b>¿Qué</b> idiomas hablas?</td><td>info (open)</td><td>Hablo dos idiomas.</td></tr>'
  '<tr><td><b>¿Quién</b> es ella?</td><td>een persoon</td><td>Es Lucía.</td></tr>'
  '</tbody></table>')
P('<div class="truc"><b>🔴 ¿Cuál? vs ¿Qué?</b> vóór <i>ser</i> + gegeven kies je <b>¿Cuál?</b>: <i>¿<b>Cuál</b> es tu nombre?</i> (niet <span class="trap">¿Qué es tu nombre?</span>). Vraagwoorden dragen een <b>tilde</b>.</div>')
P(actx(1, "Haz la pregunta",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: vraag bij het antwoord.</i> Welke vraag past bij dit antwoord?</p>'
  '<table class="mp"><thead><tr><th>Respuesta</th><th>Tu pregunta</th></tr></thead><tbody>'
  '<tr><td>Soy de Colombia.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Tengo 14 años.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Me llamo Nina.</td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Es nina@mail.com.</td><td><span class="wl md"></span></td></tr>'
  '</tbody></table>', apoyo="CUE → SIN AYUDA"))
P(actx(2, "Entrevista relámpago",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: interview met zinsframes.</i> Stel je buur de zes vragen; noteer kort. Wissel.</p>'
  '<table class="wtab mp"><thead><tr><th>¿Cómo?</th><th>¿De dónde?</th><th>¿Cuántos años?</th><th>¿Qué idiomas?</th></tr></thead><tbody>'
  '<tr><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td><td><span class="wl sm"></span></td></tr>'
  '</tbody></table>', apoyo="MARCO (vraagwoorden) → alleen vraagwoorden"))
# §4.2 género
P('<div class="divider">Género y artículos · §4.2</div>')
P('<p style="font-size:9.6pt">② <b>Observa (overeenkomst).</b> Het lidwoord past bij <b>geslacht</b> én <b>getal</b>. <span class="gloss">el país → los países · la ciudad → las ciudades.</span></p>')
P('<div class="fams" style="margin-top:2mm">')
P(pcard("Masculino → el / un", '<div class="ej"><b>el</b> nombre · <b>el</b> país · <b>el</b> correo · <b>el</b> apellido</div><div class="t2">🔴 <b>el</b> idioma, <b>el</b> día, <b>el</b> mapa (op -a, tóch mannelijk!)</div>'))
P(pcard("Femenino → la / una", '<div class="ej"><b>la</b> ciudad · <b>la</b> edad · <b>la</b> dirección · <b>la</b> nacionalidad</div><div class="t2">meestal -a, -ción, -dad → femenino · 🔴 <b>la</b> mano</div>'))
P('</div>')
P(regla("Regla · artículos",
  '<p><b>Bepaald:</b> el/la · meervoud <b>los/las</b>. <b>Onbepaald:</b> un/una. Het lidwoord past zich aan aan <b>geslacht</b> + <b>getal</b>. 🟡 Leer een substantief altijd <b>mét lidwoord</b> — dan ken je het geslacht.</p>'))
P(actx(3, "Clasifica el/la (beslisboom)",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: patroon sorteren.</i> Zet elk woord in de juiste kolom (let op de valstrikken). <span class="words"><b>ciudad · país · idioma · edad · correo · dirección · día · mano · nombre</b></span></p>'
  + sortcols([("el (m.)","-o, valstrik -a"),("la (f.)","-a, -ción, -dad")]), apoyo="PISTA (valstrikken gemarkeerd)"))
P(actx(4, "Concordancia — singular ↔ plural",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: overeenkomst zichtbaar maken.</i> Zet in het meervoud (lidwoord + woord).</p>'
  '<p style="margin-left:12.5mm">el país → <span class="wl md"></span> &nbsp; la ciudad → <span class="wl md"></span> &nbsp; el idioma → <span class="wl md"></span> &nbsp; la nacionalidad → <span class="wl md"></span></p>', apoyo="MODELO (los/las)"))
P(tarea_com("Tarea comunicativa · Tarjetas de rol",
  [{"t":"🎙️ Interacción","skill":True},{"t":"👥 En parejas"},{"t":"± 10 min"},{"t":"★★★"}],
  '<p><i>werkvorm: rollenkaarten.</i> Krijg een <b>nieuwe identiteit</b> (naam, land, leeftijd) en stel elkaar vragen om die te achterhalen. Presenteer je partner daarna. <span class="gloss">recycling in nieuwe context.</span></p>'
  '<div class="fams" style="margin-top:2mm"><div class="pcard"><div class="t" style="font-size:10pt">Mi tarjeta</div><div class="ej">Nombre: <span class="wl sm"></span><br>País: <span class="wl sm"></span> · Edad: <span class="wl sm"></span></div></div>'
  '<div class="pcard"><div class="t" style="font-size:10pt">Mi compañero/a (notas)</div><div class="ej"><span class="wl full"></span></div></div></div>'
  '<div class="steun" style="margin-left:12.5mm">Apoyo: SIN AYUDA · [CROSS: HTML «Pregunta ↔ respuesta»]</div>'))
P(guide("Juega online:", "— «Palabras interrogativas», «Pregunta ↔ respuesta» en «El o la» (met zelfcorrectie) op de digitale pagina."))
P('</div>')  # page §4

# ================= TALLER DE LENGUA =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num" style="color:var(--crema)">✎</span><span class="pk" style="background:var(--gd)">Taller de lengua</span>')
P('<div class="intro"><b>ES:</b> Dos herramientas para escribir bien: la <b>mayúscula</b> y los <b>conectores</b>. <span class="gloss">Twee schrijfgereedschappen: hoofdletters en verbindingswoorden.</span></div>')
P(lpd(("8","taalsysteem: ortografía + conectoren")))
P('</div>')
P('<h3 style="margin-top:6mm">Ortografía · mayúscula o minúscula</h3>')
P('<div class="fams" style="margin-top:4mm">')
P(pcard("MAYÚSCULA", '<div class="ej"><b>Países y ciudades:</b> España, Bélgica, Madrid · <b>nombres:</b> Lucía, Leo</div>'))
P(pcard("minúscula 🔴", '<div class="ej"><b>Nacionalidades e idiomas:</b> español, belga, francés</div><div class="t2">NL schrijft «Spaans, Belg» mét hoofdletter — Spaans niet!</div>'))
P('</div>')
P(regla("Regla · mayúsculas", '<p><b>Land/stad/naam = hoofdletter</b> · <b>nationaliteit/taal = kleine letter</b>. 🟡 <i>«el país grita, la nacionalidad susurra»</i>.</p>'))
P(actx(1, "Clínica de mayúsculas",
  [{"t":"🔍 Analizar","skill":True},{"t":"👤 Solo"},{"t":"± 5 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: foutenkliniek.</i> Onderstreep de fout en herschrijf correct.</p>'
  '<p style="margin-left:12.5mm">1) <span class="trap">soy Español y vivo en bélgica</span> → <span class="wl lg"></span><br>'
  '2) <span class="trap">Ella habla Francés e Inglés</span> → <span class="wl lg"></span><br>'
  '3) <span class="trap">diego es de méxico, es Mexicano</span> → <span class="wl lg"></span></p>', apoyo="MODELO → SIN AYUDA"))
P('<h3 style="margin-top:6mm">Conectores · y · e · o · u · porque</h3>')
P('<table class="mp"><thead><tr><th>Conector</th><th>Uso</th><th>Ejemplo</th></tr></thead><tbody>'
  '<tr><td><b>y</b></td><td>en</td><td>Soy belga <b>y</b> hablo español.</td></tr>'
  '<tr><td><b>e</b></td><td>«en» vóór i-/hi-</td><td>español <b>e</b> inglés</td></tr>'
  '<tr><td><b>o</b> / <b>u</b></td><td>of (u vóór o-/ho-)</td><td>siete <b>u</b> ocho</td></tr>'
  '<tr><td><b>porque</b></td><td>want / omdat</td><td>Aprendo español <b>porque</b> me gusta.</td></tr>'
  '</tbody></table>')
P('<div class="truc"><b>🔴 Valstrik NL:</b> <i>want</i> én <i>omdat</i> = <b>porque</b> (één woord!). «dus» = <b>así que / por eso</b>, niet <i>luego</i>.</div>')
P(actx(2, "Une con y / e / o / u / porque",
  [{"t":"✍️ Escribir","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p><i>werkvorm: gap-fill met betekenis.</i> Vul het juiste verbindingswoord in.</p>'
  '<p style="margin-left:12.5mm">a) Hablo neerlandés ___ inglés. &nbsp; b) ¿Tienes siete ___ ocho años? &nbsp; c) Estudio español ___ me gusta viajar. &nbsp; d) español ___ italiano.<br><span class="wl full"></span></p>', apoyo="BANCO"))
P('</div>')  # page Taller

# ================= CULTURA =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">★</span><span class="pk">Cultura · Madrid y los nombres hispanos</span>')
P('<div class="intro"><b>ES:</b> En el mundo hispano la gente tiene <b>dos apellidos</b> y trata de <b>tú</b> o de <b>usted</b> según la situación. <span class="gloss">Men heeft twee achternamen en zegt «tú» of «usted» naargelang de situatie.</span></div>')
P(lpd(("5","kenmerkende aspecten van de cultuur"), ("2","relevante info uit een tekst")))
P('</div>')
P('<div class="fams" style="margin-top:6mm">')
P(pcard("Madrid 🇪🇸", '<div class="ej">Hoofdstad van España (~3,3 mln). <b>Puerta del Sol</b>, el <b>Prado</b>, el <b>Retiro</b>, el <b>Real Madrid</b>.</div><div class="anchor gloss">Onze eerste parada: vertrekpunt van La Ruta.</div>'))
P(pcard("Los dos apellidos", '<div class="ej"><b>Lucía Ramírez García</b>: <i>Ramírez</i> (padre) + <i>García</i> (madre). Bij trouwen verandert de naam <b>niet</b>.</div><div class="t2">NL heeft één achternaam — hier twee.</div>'))
P('</div>')
P('<div class="truc"><b>🟡 ¿Tú of usted?</b> Vrienden/leeftijdsgenoten: <b>tú</b>. Beleefd/onbekende volwassene: <b>usted</b> (+ es). Colombia/Perú vaker <i>usted</i>; España overwegend <i>tú</i>. C6: Mateo (Argentina) met <b>vos</b>.</div>')
P(actx(1, "Comprensión — la ficha cultural",
  [{"t":"🔍 Leer","skill":True},{"t":"👤 Solo"},{"t":"± 4 min"},{"t":"★☆☆"}],
  '<p><i>werkvorm: juist/fout + verbeteren.</i> Waar of niet waar? Verbeter de foute.</p>'
  '<table class="mp"><thead><tr><th>Afirmación</th><th>V/F</th><th>Corrección</th></tr></thead><tbody>'
  '<tr><td>En España se usa un solo apellido.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>«Usted» es más formal que «tú».</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '<tr><td>Madrid es la capital de México.</td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>'
  '</tbody></table>', apoyo="MODELO (tekst boven)"))
P(actx(2, "Escribe y elige tú/usted",
  [{"t":"✍️ Escribir","skill":True},{"t":"🎙️ Hablar","skill":True},{"t":"👥 En parejas"},{"t":"± 6 min"},{"t":"★★☆"}],
  '<p>Bedenk 3 namen «à la hispana» (nombre + 2 apellidos) én kies per situatie <b>tú/usted</b> + de begroeting.</p>'
  '<p style="margin-left:12.5mm">Nombres: <span class="wl full"></span></p>'
  '<p style="margin-left:12.5mm">a) een klasgenoot: <span class="wl md"></span> &nbsp; b) de directeur: <span class="wl md"></span> &nbsp; c) een oude mevrouw: <span class="wl md"></span></p>', apoyo="PISTA → SIN AYUDA"))
P('</div>')  # page Cultura

# ================= TAREA FINAL =================
P('<div class="page"><div class="parada sec" style="border-top-color:var(--gd)">')
P('<span class="num">✦</span><span class="pk" style="background:var(--gd)">Tarea final · Mi pasaporte</span>')
P('<div class="intro"><b>ES:</b> Crea tu <b>pasaporte de La Ruta</b> y preséntate. Puedes usar tu identidad real o una <b>identidad nueva</b>. <span class="gloss">Maak je La Ruta-paspoort en stel je voor — echt of fictief.</span></div>')
P('<div class="route-note">🎯 <b>Communicatieve taak:</b> afzender = jij · ontvanger = de klas/Lucía · doel = jezelf voorstellen · situatie = aankomst in Madrid · resultaat = een ingevuld paspoort + een gesproken/geschreven voorstelling.</div>')
P(lpd(("3","doelgericht schrijven met een voorbeeld"), ("4","zich mondeling voorstellen"), ("7","woordenschat"), ("8","ser/presente/artículos")))
P('</div>')
P('<ol class="pasos">'
  '<li><b>Elige tu identidad.</b> Nombre + dos apellidos, país, ciudad, edad, idiomas.</li>'
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
P(audiorow('<div class="ic">🎬</div><div><b>Graba tu presentación</b> en la página digital (recorder + rúbrica).<span class="gloss"> Neem je voorstelling op via de digitale pagina.</span></div>',
           qr("Escanea y graba", "Tarea · Mi pasaporte", seed=41)))
P('<div class="se" style="margin-top:5mm">Rúbrica · ¿lo logré? <span class="gloss" style="font-size:8pt">— evalueer je eigen paspoort</span></div>')
P('<table class="sem"><tr class="semrow"><th>Criterio</th><th>🔴 todavía no</th><th>🟠 casi</th><th>🟢 ¡sí!</th></tr>'
  '<tr><td>Mijn paspoort heeft <b>alle gegevens</b> (nombre, país, edad, ciudad, idiomas)</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik gebruik <b>ser</b> en het <b>presente</b> correct</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik verbind met <b>y / porque</b> en schrijf <b>mayúsculas</b> juist</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '<tr><td>Ik <b>stel mezelf mondeling voor</b> en versta een klasgenoot</td><td>☐</td><td>☐</td><td>☐</td></tr>'
  '</table>')
P('</div>')  # page Tarea

# ================= REPASO =================
P('<div class="page"><div class="parada sec">')
P('<span class="num">✓</span><span class="pk">Repaso · lo esencial</span>')
P('<div class="intro"><b>ES:</b> Lo más importante de un vistazo. El <b>repaso completo</b> (quiz, drills, 18 juegos) está <b>online</b>. <span class="gloss">Het belangrijkste in één oogopslag; de volledige herhaling staat online.</span></div>')
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
P('<div class="truc"><b>✍️ Reflexión (mochila):</b> <i>Lo más fácil de U1: <span class="wl md"></span> · Lo más difícil: <span class="wl md"></span></i></div>')
P('<div class="bridge"><b>» Siguiente parada: Sevilla (U2).</b> Ya sabes decir quién eres; en <b>U2 «Mi gente»</b> presentas a tu <b>familia</b> con Lucía en Andalucía — met <i>tener</i>, los posesivos y describir a las personas. <span class="gloss">Je kunt zeggen wie je bent; in U2 stel je je familie voor in Sevilla.</span></div>')
P('</div>')  # page Repaso

# ================= §V VOCABULARIO =================
import json
VOC = json.load(open(f"{HERE}/u1_vocab.json", encoding="utf-8"))
GRP = [("datos","Datos personales"),("ficha","La ficha / el formulario"),("interrog","Palabras interrogativas"),
       ("saludos","Saludos (recyclen U0)"),("pais","Países y nacionalidades — mundo hispano"),("mundo","Países del mundo")]
P('<div class="page"><div class="parada sec">')
P('<span class="num">V</span><span class="pk">§V · Vocabulario</span>')
P('<div class="intro"><b>ES:</b> Todas las palabras de la unidad. En la página digital: <b>flip cards</b> (ES↔NL), audio (TTS) y buscador. <span class="gloss">Alle woorden; online flip cards, audio en zoekfunctie.</span></div>')
P(lpd(("7","woordenschat inzetten (receptief & productief)")))
P('</div>')
for key, titel in GRP:
    items = [v for v in VOC if v.get("grp") == key]
    if not items: continue
    P(f'<h3 style="margin-top:6mm">{titel} <span class="gloss" style="font-size:8pt">· {len(items)} woorden</span></h3>')
    rows = "".join(f'<tr><td><b>{v["es"]}</b></td><td>{v["nl"]}</td><td class="gloss">{v["soort"]}</td><td class="gloss">{v["ej"]}</td></tr>' for v in items)
    P(f'<table class="alf"><thead><tr><th>Español</th><th>Nederlands</th><th>ERK/soort</th><th>Ejemplo</th></tr></thead><tbody>{rows}</tbody></table>')
# print-oefenladder V.1-V.4 (receptief -> gestuurd)
P('<div class="divider">Escalera de práctica · V.1–V.4</div>')
P(actx("V.1", "Reconocer — ES → NL",
  [{"t":"🔍 Leer","skill":True},{"t":"± 3 min"},{"t":"★☆☆"}],
  '<p>Schrijf de vertaling. <span class="gloss">herkennen.</span> el apellido = <span class="wl md"></span> · la edad = <span class="wl md"></span> · el idioma = <span class="wl md"></span> · la dirección = <span class="wl md"></span></p>', apoyo="MODELO"))
P(actx("V.2", "Distinguir — sorteer per thema",
  [{"t":"🔍 Analizar","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Sorteer: <span class="words"><b>correo · Perú · ¿Cuál? · nacionalidad · Chile · edad</b></span></p>'
  + sortcols([("dato",""),("país",""),("interrogativo","")], eigen=False), apoyo="BANCO"))
P(actx("V.3", "Recordar — NL → ES (con letra)",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★☆"}],
  '<p>Vul het Spaanse woord aan (beginletter gegeven). het land = <b>p</b>___ · de stad = <b>c</b>___ · de taal = <b>i</b>___ · de nationaliteit = <b>n</b>___<br><span class="wl full"></span></p>', apoyo="LETRA INICIAL"))
P(actx("V.4", "Producir — una frase con tres palabras",
  [{"t":"✍️ Escribir","skill":True},{"t":"± 4 min"},{"t":"★★★"}],
  '<p><i>verplichte-woorden-zin.</i> Maak één correcte zin met <b>nombre · país · edad</b>.</p><div class="wbox sm"></div>', apoyo="SIN AYUDA"))
P('<div class="guide"><div class="ic">🎴</div><div><span class="hand">Sigue en la página digital:</span> <span class="g">flip cards (ES↔NL), audio en de 18 spellen bouwen de steun verder af tot je álles zonder hulp kent.</span></div></div>')
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
