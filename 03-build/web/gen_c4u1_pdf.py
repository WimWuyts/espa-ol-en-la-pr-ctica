#!/usr/bin/env python3
# C4 · Unidad 1 — PRINT (HTML=bron → PDF via Chromium). Golden-sample print-kit, C4-rood.
# Bevat: hero-bleed p1, secties op nieuwe pagina, ANTWOORDRUIMTE (schrijflijnen/-vlakken/-kolommen),
# QR naar de HTML-hub (segno), én een bewerkbare laag (editbar: bewerken / opslaan als PDF / bewaar).
import base64, os, re, segno, io
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w,fam=None):
    return f"@font-face{{font-family:'{fam or f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),
 face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Bricolage Grotesque XBold","BricolageGrotesque-800.woff2","800","Bricolage Grotesque XBold"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])
PRINTCSS=open(f"{ROOT}/02-huisstijl/templates/cursus-print.css").read()

def qr(data):
    buf=io.BytesIO(); segno.make(data,error='m').save(buf,kind='svg',scale=1,border=0,dark="#A8323B")
    svg=buf.getvalue().decode()
    svg=re.sub(r'<\?xml[^>]*\?>','',svg); svg=svg.replace('<svg ','<svg style="width:26mm;height:26mm" ',1)
    return svg
HUB_URL="https://hablacon-ene.local/C4/U1"   # placeholder → auteur vervangt door de gehoste hub-URL
SPOTIFY="https://open.spotify.com/playlist/37i9dQZF1DXaxEKcoCdWHD"

# ── data ──────────────────────────────────────────────────────────────────────
SCENES=[
 ("Escena 1 · Julio y María se despiertan",[
  ("María","Hola."),("Julio","Hola."),("María","¿Cómo estás?"),("Julio","Bien."),
  ("María","Bueno, encantada. ¿Cómo te llamas?"),("Julio","Yo soy Julio."),("María","Yo me llamo María."),
  ("Julio","Encantado. Perdona, pero yo me voy… al trabajo."),("María","Vale."),
  ("Julio","Bueno, hasta luego."),("María","Adiós."),
 ]),
 ("Escena 2 · En la academia",[
  ("Fernando","Ella es Josefina, la secretaria."),("Josefina","Hola, encantada. ¿Y tú cómo te llamas?"),
  ("María","Me llamo María."),("Fernando","Julio, os presento. María Torres, la nueva profesora."),
  ("María","¿Cómo está usted?"),("Julio","Encantado de conocerla."),("María","Igualmente, encantada."),
  ("María","Muchas gracias, Fernando, por el trabajo."),("Fernando","De nada. Bienvenida a la academia."),
 ]),
]
CH=["Hola","¿Cómo estás?","Bien","encantada","Encantado","¿Cómo te llamas?","me llamo","soy","hasta luego",
 "Adiós","Vale","¿Cómo está usted?","Igualmente","Encantado de conocerla","Me llamo","Muchas gracias","De nada","Bienvenida","Perdona"]
def mk(es):
    o=es
    for c in sorted(CH,key=len,reverse=True):
        o=re.sub("("+re.escape(c)+")",r'<b>\1</b>',o,count=1,flags=re.IGNORECASE)
    return o
def trline(sp,es):
    return f'<div class="tl"><span class="sp">{sp}</span><span class="tx">{mk(es)}</span></div>'
def scenehtml(t,lines):
    return f'<h3>{t}</h3>'+ "".join(trline(*l) for l in lines)

CLUSTERS=[
 ("Saludar · begroeten",[("¡Hola!","Hallo"),("Buenos días","Goedemorgen"),("Buenas tardes","Goedemiddag"),
   ("Buenas noches","Goedenavond"),("¿Qué tal?","Hoe gaat het?"),("¿Cómo estás?","Hoe gaat het? (jij)"),("¿Cómo está usted?","… met u?")]),
 ("Presentarse · jezelf voorstellen",[("Me llamo…","Ik heet…"),("Yo soy…","Ik ben…"),("Soy de…","Ik kom uit…"),
   ("Encantado","Aangenaam (m)"),("Encantada","Aangenaam (v)"),("Igualmente","Insgelijks")]),
 ("Preguntar · vragen",[("¿Cómo te llamas?","Hoe heet je?"),("¿Y tú?","En jij?"),("¿De dónde eres?","Waar kom je vandaan?")]),
 ("Responder & cortesía",[("Bien, ¿y tú?","Goed, en jij?"),("Muy bien","Heel goed"),("Por favor","Alsjeblieft"),
   ("Gracias","Dank je"),("Muchas gracias","Hartelijk dank"),("De nada","Graag gedaan"),("Perdona","Sorry")]),
 ("Despedirse · afscheid",[("Adiós","Dag"),("Hasta luego","Tot straks"),("Hasta mañana","Tot morgen"),("Vale","Oké"),("¡Nos vemos!","We zien elkaar!")]),
]
def kitrow(es,nl):
    return f'<tr><td class="k-es">{es}</td><td class="k-nl gloss">{nl}</td><td class="k-ck"><span class="chk"></span></td></tr>'
def kittable(name,items):
    rows="".join(kitrow(*i) for i in items)
    return (f'<div class="kit"><div class="kit-h">{name}</div>'
      f'<table class="ktab"><thead><tr><th>Español</th><th>Nederlands</th><th>🔊 na</th></tr></thead><tbody>{rows}</tbody></table></div>')

def wl(cls=""): return f'<span class="wl {cls}"></span>'
def numlines(n,cls="full"):
    return '<ol class="nl">'+"".join(f'<li>{wl(cls)}</li>' for _ in range(n))+'</ol>'

CSS=FONTS+PRINTCSS+r"""
/* C4-rood override */
:root{ --g:#D64550; --gd:#A8323B; --gt:#FBEAEC; }
/* functionele kleursemantiek */
.p{color:#2563EB;font-weight:700}.v{color:#EA7317;font-weight:700}
/* Escucha transcript (print) */
.tl{display:flex;gap:3mm;padding:1mm 0;font-size:9.6pt;break-inside:avoid}
.tl .sp{font-family:var(--disp);font-weight:700;color:var(--gd);width:22mm;flex:none}
.tl .tx b{background:var(--gt);border-radius:3pt;padding:.2mm 1.2mm;font-weight:700}
.twocol{column-count:2;column-gap:8mm}
/* Kit tabellen */
.kitwrap{display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin-top:3mm}
.kit{break-inside:avoid}
.kit-h{font-family:var(--disp);font-weight:700;font-size:10pt;color:var(--gd);margin:2mm 0 1mm}
.ktab{font-size:9pt;width:100%}.ktab th{background:var(--gt);color:var(--gd);font-size:7.4pt;text-transform:uppercase;padding:1.2mm 2mm;text-align:left}
.ktab td{border-bottom:1px solid var(--line);padding:1.2mm 2mm}.k-es{font-weight:600}.k-ck{text-align:center;width:12mm}
.chk{display:inline-block;width:3.4mm;height:3.4mm;border:1.3px solid var(--mut);border-radius:1.5pt;vertical-align:middle}
/* grammatica mini */
.gt2{width:100%;font-size:9.2pt;margin:2mm 0}.gt2 td{border-bottom:1px solid var(--line);padding:1.5mm 2.5mm}
.gt2 .p{color:#2563EB}.gt2 .v{color:#EA7317;font-family:var(--disp)}.gt2 .ex{color:var(--mut);font-style:italic}
.mv2{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin:2mm 0}
.mv2 div{border-radius:8pt;padding:2.5mm 4mm;font-family:var(--disp)}
.mv2 .m{background:#E8F0FE;color:#1E40AF}.mv2 .f{background:#FCE7F0;color:#9D174D}
/* ANTWOORDRUIMTE */
.wl{display:inline-block;border-bottom:1.4px solid var(--line2);min-width:38mm;height:5mm;vertical-align:bottom}
.wl.full{min-width:0;width:100%}.wl.lg{min-width:66mm}.wl.sm{min-width:22mm}
ol.nl{margin:2mm 0;padding-left:7mm}ol.nl li{margin:2.6mm 0}
.wcols{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin-top:2mm}
.wcol{border:1px solid var(--line);border-radius:8pt;overflow:hidden;break-inside:avoid}
.wcol h4{font-family:var(--disp);font-size:8.6pt;margin:0;background:var(--gt);color:var(--gd);padding:1.5mm 2mm;text-align:center}
.wcol .fill{min-height:34mm;background:repeating-linear-gradient(transparent,transparent 6.2mm,var(--line) 6.2mm,var(--line) 6.4mm);}
.wbox{border:1px solid var(--line);border-radius:8pt;min-height:24mm;background:repeating-linear-gradient(transparent,transparent 6.2mm,var(--line) 6.2mm,var(--line) 6.4mm);margin-top:2mm}
.wtab{width:100%;font-size:9pt}.wtab th{background:var(--gt);color:var(--gd);font-size:7.6pt;text-transform:uppercase;padding:1.5mm}.wtab td{border:1px solid var(--line);height:9mm;padding:1mm 2mm}
.mtab{width:100%;font-size:9.4pt;margin-top:2mm}.mtab td{padding:1.8mm 2mm;border-bottom:1px dashed var(--line2)}.mtab .a{font-weight:600}.mtab .b{color:var(--mut)}.mtab .ln{width:8mm;border-bottom:1.4px solid var(--line2);display:inline-block}
.scramble{display:flex;flex-wrap:wrap;gap:2mm;margin:2mm 0}.scramble span{border:1px solid var(--line);border-radius:6pt;padding:1mm 3mm;font-weight:600;font-size:9pt;background:#fff}
/* uitspraak (Suena bien) print */
.vrow{display:grid;grid-template-columns:repeat(5,1fr);gap:3mm;margin:2mm 0}
.vc{border:1px solid var(--line);border-top:3px solid var(--g);border-radius:8pt;padding:2.5mm;text-align:center;break-inside:avoid}
.vc .vl{font-family:var(--dispx);font-size:20pt;color:var(--gd);line-height:1}
.vc .vas{font-size:7.6pt;color:var(--mut);display:block}
.vc .vej{font-size:8.6pt;font-weight:600;display:block;margin-top:1mm}
.klemline{font-size:10pt;margin:3mm 0 0}.klemline .t{background:var(--gt);border-radius:4pt;padding:.3mm 1.6mm;font-weight:700;color:var(--gd)}
/* música print */
.bandas{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-top:3mm}
.banda{border:1px solid var(--line);border-radius:10pt;padding:3mm 4mm;break-inside:avoid}
.banda .ar{font-family:var(--disp);font-weight:700;font-size:10pt}.banda .sg{font-size:8.4pt;color:var(--mut)}.banda .ge{font-size:7.6pt;color:var(--gd)}
.musrow{display:grid;grid-template-columns:1fr auto;gap:5mm;align-items:center;margin-top:4mm}
/* editbar (scherm) — verdwijnt in print */
.editbar{position:fixed;top:0;left:0;right:0;background:var(--gd);color:#fff;display:flex;gap:8px;align-items:center;padding:7px 12px;z-index:999;font-family:var(--body);font-size:13px;box-shadow:0 2px 10px #0003}
.editbar b{font-family:var(--disp)}.editbar button{border:0;background:#fff;color:var(--gd);font-weight:700;border-radius:8px;padding:6px 11px;cursor:pointer;font-size:12.5px}
.editbar button.on{background:#111;color:#fff}
.editbar .sp{flex:1}
.scr-spacer{height:44px}
body.editing .page{outline:1.5px dashed var(--g);outline-offset:-6px}
@media print{ .editbar,.scr-spacer{display:none!important} }
"""

# ── content ──────────────────────────────────────────────────────────────────
HERO=f"""
<section class="hero">
  <div class="tab">C4 · LA RUTA</div>
  <div class="eyebrow">EL DESPEGUE · PARADA 1 · SURVIVAL IN SPANISH</div>
  <h1>Presentaciones</h1>
  <div class="sub">Je allereerste Spaans: <b>groeten</b>, <b>jezelf voorstellen</b> en <b>afscheid nemen</b>. <span class="gloss">Tus primeras palabras en español — todo lo que oyes, lo puedes usar enseguida.</span></div>
  <div class="q">¡Hola! ¿Cómo te llamas?</div>
</section>
<div class="page">
  <div class="obj"><div class="se">Al final de esta unidad · Op het einde van deze les</div>
    <ul>
      <li><span class="ck">✓</span> <span><span class="es">Saludar y despedirte</span> <span class="nl">— groeten en afscheid nemen</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Decir tu nombre y de dónde eres</span> <span class="nl">— zeggen hoe je heet en waar je vandaan komt</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Preguntar el nombre a otra persona</span> <span class="nl">— iemand naar zijn naam vragen</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Distinguir <b>-o/-a</b> y <b>tú/usted</b></span> <span class="nl">— man/vrouw & informeel/beleefd</span></span></li>
    </ul>
  </div>
  <div class="guide"><span class="ic">🎒</span><div><span class="hand">¡Vamos! We beginnen te reizen.</span><div class="g">In deze «survival»-les leer je de taal die je meteen nodig hebt. Luister, spreek na, en probeer het zelf.</div></div></div>
</div>
"""

ESCUCHA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§1 · ¡Escucha!</div><h2>Bekijk de scène en lees mee</h2>
  <div class="audiorow">
    <div class="call"><span class="ic">🎬</span><div><b>Sitcom · Episodio 1.</b> Scan de code en bekijk de aflevering op de digitale pagina. Luister eerst zónder te lezen; daarna lees je mee. De <b>vetgedrukte</b> woorden zijn chunks om mee te nemen.</div></div>
    <div class="qr"><div class="lab">Vídeo online</div>{qr(HUB_URL+"#escucha")}<div class="meta">hub · Escucha</div></div>
  </div>
  <div class="twocol">{scenehtml(*SCENES[0])}{scenehtml(*SCENES[1])}</div>
  <div class="ojo"><b>¡Ojo!</b> <b>encantado</b> (jongen) / <b>encantada</b> (meisje). Zeg <i>me llamo…</i>, niet «yo soy me llamo».</div>
</div>
"""

VOC=[("a","als in ‘bal’","casa"),("e","als in ‘bed’","mesa"),("i","als in ‘kiwi’","sí"),("o","als in ‘pot’","hola"),("u","als in ‘boek’","tú")]
def vc(l,a,e): return f'<div class="vc"><div class="vl">{l}</div><span class="vas">{a}</span><span class="vej">{e}</span></div>'
KIT=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Suena bien · pronunciación</div><h2>De 5 klinkers &amp; de klemtoon</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 1mm">Spaanse klinkers zijn <b>kort en zuiver</b> — altijd dezelfde klank. Oefen ze online (QR §1): luister en spreek na.</p>
  <div class="vrow">{"".join(vc(*v) for v in VOC)}</div>
  <div class="ojo"><b>¡Ojo!</b> e blijft /e/ en o blijft /o/ — géén Nederlandse «ei/ou»-glijder (denk: a·e·i·o·oe).</div>
  <div class="klemline"><b>La sílaba tónica</b> — waar ligt de klemtoon? Onderstreep/hoor: <span class="t">HO</span>·la · me·<span class="t">LLA</span>·mo · en·can·<span class="t">TA</span>·do · a·<span class="t">DIÓS</span> · <span class="t">GRA</span>·cias</div>

  <div class="se" style="margin-top:6mm">§2 · Kit de supervivencia</div><h2>De taal die je écht nodig hebt</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 2mm">Vink ☐ af telkens je een uitdrukking vlot kunt <b>naspreken</b>. Oefen ze online met audio.</p>
  <div class="kitwrap">{"".join(kittable(n,it) for n,it in CLUSTERS)}</div>
</div>
"""

GRAM=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§4 · Gramática en la práctica</div><h2>Kort en functioneel</h2>
  <div class="regla"><span class="tag">ser · zijn</span>
    <table class="gt2"><tr><td class="p">yo</td><td class="v">soy</td><td>ik ben</td><td class="ex">Yo <b>soy</b> Ana.</td></tr>
    <tr><td class="p">tú</td><td class="v">eres</td><td>jij bent</td><td class="ex">¿<b>Eres</b> Leo?</td></tr>
    <tr><td class="p">él/ella/usted</td><td class="v">es</td><td>hij/zij is · u bent</td><td class="ex">Ella <b>es</b> María.</td></tr></table>
  </div>
  <div class="regla"><span class="tag">llamarse · heten</span>
    <table class="gt2"><tr><td class="p">(yo) me</td><td class="v">llamo</td><td>ik heet</td><td class="ex"><b>Me llamo</b> Sara.</td></tr>
    <tr><td class="p">(tú) te</td><td class="v">llamas</td><td>jij heet</td><td class="ex">¿Cómo <b>te llamas</b>?</td></tr>
    <tr><td class="p">(usted) se</td><td class="v">llama</td><td>u heet</td><td class="ex">¿Cómo <b>se llama</b> usted?</td></tr></table>
  </div>
  <div class="regla"><span class="tag">-o / -a</span>
    <div class="mv2"><div class="m">♂ Un chico: encantad<b>o</b> · bienvenid<b>o</b></div><div class="f">♀ Una chica: encantad<b>a</b> · bienvenid<b>a</b></div></div>
    <p style="font-size:9pt;margin:1mm 0 0">Kies de vorm die past bij <b>jou</b>. Met vrienden gebruik je <b>tú</b>; formeel <b>usted</b>.</p>
  </div>
  <div class="truc"><b>Mini-oefening.</b> Vul aan met de juiste vorm van <i>ser</i> of <i>llamarse</i>:
    <div style="margin-top:2mm;font-size:9.6pt;line-height:2.3">1. Yo {wl('sm')} de Bélgica. &nbsp;&nbsp; 2. ¿Cómo {wl('sm')} llamas? &nbsp;&nbsp; 3. Me {wl('sm')} ____. &nbsp;&nbsp; 4. Ella {wl('sm')} profesora.</div>
  </div>
</div>
"""

def act(n,title,badges,body):
    bh="".join(f'<span class="badge {c}">{t}</span>' for t,c in badges)
    return (f'<div class="act"><div class="acthead"><div class="anum">{n}</div><div><div class="h">{title}</div>'
            f'<div class="badges">{bh}</div></div></div>{body}</div>')

PRAC=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§3 · Práctica</div><h2>Oefen op papier — online verbeter je alles</h2>

  {act(1,"Clasifica las expresiones",[("receptief","skill"),("5 min","")],
    '<p style="margin-left:12.5mm">Schrijf elke uitdrukking in de juiste kolom. Voeg onderaan één eigen woord toe.<br><span class="gloss">Hola · Adiós · Gracias · ¿Cómo te llamas? · Hasta luego · De nada · Buenos días · Encantado</span></p>'
    +'<div class="wcols" style="margin-left:12.5mm"><div class="wcol"><h4>Saludar</h4><div class="fill"></div></div><div class="wcol"><h4>Preguntar</h4><div class="fill"></div></div><div class="wcol"><h4>Cortesía</h4><div class="fill"></div></div><div class="wcol"><h4>Despedirse</h4><div class="fill"></div></div></div>')}

  {act(2,"Relaciona · verbind",[("gestuurd","skill"),("★☆☆","")],
    '<p style="margin-left:12.5mm">Trek een lijn tussen het Spaans en de betekenis.</p>'
    +'<table class="mtab" style="margin-left:12.5mm"><tr><td class="a">1. ¡Hola!</td><td><span class="ln"></span></td><td class="b">a. graag gedaan</td></tr>'
    +'<tr><td class="a">2. ¿Cómo te llamas?</td><td><span class="ln"></span></td><td class="b">b. tot straks</td></tr>'
    +'<tr><td class="a">3. De nada</td><td><span class="ln"></span></td><td class="b">c. hallo</td></tr>'
    +'<tr><td class="a">4. Hasta luego</td><td><span class="ln"></span></td><td class="b">d. aangenaam</td></tr>'
    +'<tr><td class="a">5. Encantada</td><td><span class="ln"></span></td><td class="b">e. hoe heet je?</td></tr></table>')}

  {act(3,"Completa el diálogo",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Vul het gesprek aan.</p>'
    +f'<div style="margin-left:12.5mm;font-size:10pt;line-height:2.5">'
    +f'— ¡Hola! ¿Cómo {wl("sm")} llamas?<br>— Me {wl("sm")} Ana. ¿Y {wl("sm")}?<br>— Yo {wl("sm")} Leo. {wl("sm")} de Madrid.<br>— ¡{wl("sm")}! Hasta {wl("sm")}.</div>')}

  {act(4,"Ordena la conversación",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Nummer de zinnen in de juiste volgorde (1–5).</p>'
    +'<div class="scramble" style="margin-left:12.5mm"><span>___ Yo soy Leo. Encantado.</span><span>___ ¡Hola! ¿Cómo te llamas?</span><span>___ ¡Hasta luego!</span><span>___ Me llamo Ana. ¿Y tú?</span><span>___ Igualmente. ¡Adiós!</span></div>')}

  {act(5,"¿-o o -a?",[("gestuurd","skill"),("★☆☆","")],
    f'<p style="margin-left:12.5mm">Vul de juiste letter in (♂ -o / ♀ -a).</p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. (chico) Encantad{wl("sm")} &nbsp; 2. (chica) Encantad{wl("sm")} &nbsp; 3. (chica) Bienvenid{wl("sm")} &nbsp; 4. (chico) Bienvenid{wl("sm")}</div>')}

  {act(6,"Preséntate por escrito",[("productie","skill"),("★★★","")],
    '<p style="margin-left:12.5mm">Stel jezelf voor in 3–4 zinnen: groet, naam, herkomst, afscheid. Gebruik de kit.</p>'
    +'<div class="wbox" style="margin-left:12.5mm"></div>')}
</div>
"""

TAREA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§5 · Tarea final</div><h2>El carné de la clase</h2>
  <div class="esen" style="margin-top:2mm"><b class="tt">Jouw opdracht.</b> Maak je klaskaartje en stel je mondeling voor aan <b>3 klasgenoten</b>. Vraag hun naam en herkomst, en noteer ze. <span class="gloss">Sin leer del papel — zonder van het blad af te lezen.</span></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div>
      <div class="regla" style="margin:0"><span class="tag">Mi carné</span>
        <table class="wtab" style="margin-top:3mm"><tr><td style="width:32mm">Me llamo</td><td></td></tr><tr><td>Soy de</td><td></td></tr><tr><td>Mi emoji / dibujo</td><td></td></tr></table>
      </div>
      <p style="font-size:9pt;color:var(--mut);margin-top:2mm">Zeg: «¡Hola! Me llamo ___. Soy de ___. ¡Encantad_!»</p>
    </div>
    <div>
      <div class="se">3 compañeros</div>
      <table class="wtab"><thead><tr><th>#</th><th>¿Cómo te llamas?</th><th>¿De dónde eres?</th></tr></thead>
      <tr><td style="width:8mm;text-align:center">1</td><td></td><td></td></tr>
      <tr><td style="text-align:center">2</td><td></td><td></td></tr>
      <tr><td style="text-align:center">3</td><td></td><td></td></tr></table>
    </div>
  </div>
  <div class="truc" style="margin-top:4mm"><b>🏁 Klaar als…</b> je jezelf vlot voorstelt zónder af te lezen, de juiste vorm (-o/-a) gebruikt en 3 namen genoteerd hebt.</div>
</div>
"""

BANDAS=[("Aitana","Las Babys","pop 🇪🇸"),("Quevedo","Bzrp #52","urban 🇪🇸"),("Manu Chao","Me gustas tú","clásico 🌎"),
 ("Karol G","TQG","reggaetón 🇨🇴"),("Bad Bunny","Tití me preguntó","🇵🇷"),("Rosalía","La Perla","🇪🇸")]
def banda(a,s,g): return f'<div class="banda"><div class="ar">{a}</div><div class="sg">🎵 {s}</div><div class="ge">{g}</div></div>'
MUSICA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Cultura · Banda sonora</div><h2>Leer Spaans via muziek die jullie kennen</h2>
  <p style="font-size:9.6pt">Elke unit heeft een <b>banda sonora</b>: nummers van artiesten die nu populair zijn. Luister, zing mee en pik nieuwe woorden op. Voor deze les rond <i>presentarse</i> passen <b>«Me gustas tú»</b> (Manu Chao) en <b>«Las Babys»</b> (Aitana).</p>
  <div class="bandas">{"".join(banda(*b) for b in BANDAS)}</div>
  <div class="musrow">
    <div class="call"><span class="ic">🎧</span><div><b>Spotify · la playlist de la clase.</b> Scan en luister. Op de digitale pagina vind je ook <b>LyricsTraining</b> (vul de tekst aan terwijl je luistert) en de video's.</div></div>
    <div class="qr"><div class="lab">Playlist</div>{qr(SPOTIFY)}<div class="meta">Spotify</div></div>
  </div>
</div>
"""

REPASO=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Repaso · Lo esencial de un vistazo</div><h2>Wat je nu kunt</h2>
  <div class="fams">
    <div class="pcard"><div class="t">Zo groet & stel je je voor</div><div class="ej">¡Hola! <b>Me llamo</b> ___. <b>Soy de</b> ___. <b>Encantad_</b>. ¿Y tú, <b>cómo te llamas</b>?</div><div class="t2">Afscheid: Adiós · Hasta luego · ¡Nos vemos!</div></div>
    <div class="pcard"><div class="t">Onthou</div><div class="ej"><b>ser</b>: soy · eres · es &nbsp; | &nbsp; <b>llamarse</b>: me/te/se llamo/llamas/llama</div><div class="anchor"><b>-o</b> = ♂ · <b>-a</b> = ♀ &nbsp; | &nbsp; <b>tú</b> = vriend · <b>usted</b> = beleefd</div></div>
  </div>
  <table class="sem"><thead><tr><th style="text-align:left">Puedo… · Ik kan…</th><th>🟢</th><th>🟡</th><th>🔴</th></tr></thead>
    <tr><td>groeten en afscheid nemen</td><td></td><td></td><td></td></tr>
    <tr><td>mezelf voorstellen (naam + herkomst)</td><td></td><td></td><td></td></tr>
    <tr><td>iemand naar zijn naam vragen</td><td></td><td></td><td></td></tr>
    <tr><td>-o/-a en tú/usted juist kiezen</td><td></td><td></td><td></td></tr></table>
  <div class="guide"><span class="ic">🎮</span><div><span class="hand">Repasa jugando</span><div class="g">Oefen alles online met spelletjes, flashcards en audio op de digitale hub (scan de QR bij §1).</div></div></div>
  <div class="bridge"><b>Próxima parada →</b> In de volgende unit bestel je iets en overleef je je eerste gesprek in een café. ¡Hasta pronto!</div>
</div>
"""

EDITBAR="""
<div class="editbar" id="eb">
  <b>✏️ C4 · U1</b>
  <button id="btnedit">Bewerken aan</button>
  <button id="btnpdf">🖨️ Opslaan als PDF</button>
  <button id="btnsave">💾 Bewaar (.html)</button>
  <span class="sp"></span>
  <span style="opacity:.85;font-size:12px">Tip: zet «Bewerken» aan, pas de tekst aan, en sla op als PDF.</span>
</div><div class="scr-spacer"></div>
"""
SCRIPT="""
<script>
var editing=false;var be=document.getElementById('btnedit');
be.onclick=function(){editing=!editing;document.querySelectorAll('.page,.hero').forEach(function(p){p.contentEditable=editing;});document.body.classList.toggle('editing',editing);be.classList.toggle('on',editing);be.textContent=editing?'Bewerken uit':'Bewerken aan';};
document.getElementById('btnpdf').onclick=function(){window.print();};
document.getElementById('btnsave').onclick=function(){var html='<!doctype html>'+document.documentElement.outerHTML;var b=new Blob([html],{type:'text/html'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='C4_U1_Presentaciones_bewerkt.html';a.click();};
</script>
"""

HTML=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 1 · Presentaciones</title><style>{CSS}</style></head><body>
{EDITBAR}
{HERO}{ESCUCHA}{KIT}{GRAM}{PRAC}{TAREA}{MUSICA}{REPASO}
{SCRIPT}
</body></html>"""
os.makedirs(f"{ROOT}/03-build/web/print",exist_ok=True)
open(f"{ROOT}/03-build/web/print/C4_U1.html","w",encoding="utf-8").write(HTML)
print("C4_U1.html (print+editable) geschreven:",len(HTML),"bytes")
