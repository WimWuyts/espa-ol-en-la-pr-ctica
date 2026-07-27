#!/usr/bin/env python3
# C4 · Unidad 3 — PRINT (HTML=bron → PDF via Chromium). Golden-sample print-kit, C4-rood.
# Thema: ¿De dónde eres? · soy de + país · gentilicio m/v · idiomas. Zelfde pijplijn/CSS als U1/U2.
import base64, os, re, segno, io, sys
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
from funciones_print import print_section
FUNCIONES_SEC=print_section(3)
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
HUB_URL="https://hablacon-ene.local/C4/U3"   # placeholder → auteur vervangt door de gehoste hub-URL
SPOTIFY="https://open.spotify.com/playlist/37i9dQZF1DXaxEKcoCdWHD"

# ── data · transcript Episodio 3 (exact, door auteur aangeleverd) ──────────────
SCENES=[
 ("Escena 1 · ¿De dónde eres?",[
  ("Josefina","Bueno, buenas noches."),("Fernando","Buenas noches, Josefina."),
  ("Extranjera","Dinero. Dinero, por favor."),("Fernando","¿De dónde eres?"),("Extranjera","¿Cómo?"),
  ("Fernando","¿De dónde eres? ¿De qué país?"),("Extranjera","¡Ah! Yo soy Argelia."),
  ("Fernando","No. «Yo soy de Argelia». Eres argelina. Chica, argelina. Chico, argelino. Mira: alemán, alemana; portugués, portuguesa; colombiano, colombiana."),
 ]),
 ("Escena 2 · La nacionalidad y los idiomas",[
  ("Fernando","Se dice argelina, ¿no? De Argelia, argelino."),("Julio","O argelina, sí. Buenas noches."),
  ("Extranjera","Buenas noches."),("Julio","Habla bastante bien español."),
  ("Extranjera","No hablo mucho, pero entiendo un poco. El dinero."),
  ("Julio","¿Habla usted francés? ¡Qué maravilla! Tres idiomas, ¿no? Árabe, francés y español."),
 ]),
 ("Escena 3 · El dinero y los números",[
  ("Fernando","Veinte euros está bien, ¿no?"),("Extranjera","Veinte, diez…"),
  ("Fernando","Veinte, veinte. Uno, dos, tres, cinco, diez, veinte."),
  ("Julio","Yo no tengo. Un momento. ¡María, dinero!"),
  ("María","Tengo uno de veinte y dos de diez. Espera, tengo monedas."),("Julio","Aquí tiene."),
 ]),
]
CH=["¿De dónde eres?","¿De qué país?","soy de Argelia","Eres argelina","argelina","argelino","alemán","alemana","portugués","portuguesa","colombiano","colombiana","Buenas noches","por favor","Habla usted francés","Habla bastante bien","No hablo mucho","entiendo un poco","Tres idiomas","árabe","francés","español","Veinte euros","Veinte","diez"]
def mk(es):
    ph=[];o=es
    def grab(m):
        ph.append(m.group(1));return "\x00%d\x00"%(len(ph)-1)
    for c in sorted(CH,key=len,reverse=True):
        o=re.sub("("+re.escape(c)+")",grab,o,count=1,flags=re.IGNORECASE)
    return re.sub("\x00(\\d+)\x00",lambda m:'<b>'+ph[int(m.group(1))]+'</b>',o)
def trline(sp,es):
    return f'<div class="tl"><span class="sp">{sp}</span><span class="tx">{mk(es)}</span></div>'
def scenehtml(t,lines):
    return f'<h3>{t}</h3>'+ "".join(trline(*l) for l in lines)

CLUSTERS=[
 ("Preguntar el origen · vragen",[("¿De dónde eres?","Waar kom je vandaan?"),("¿De dónde es usted?","… komt u vandaan?"),
   ("¿De qué país?","Uit welk land?"),("¿Y tú?","En jij?")]),
 ("Decir de dónde soy · ser de",[("Soy de Bélgica","Ik kom uit België"),("Soy de España","Ik kom uit Spanje"),
   ("Soy de México","Ik kom uit Mexico"),("Soy de Flandes","Ik kom uit Vlaanderen")]),
 ("La nacionalidad · gentilicio",[("belga · belga","Belgisch (♂=♀)"),("español · española","Spaans"),
   ("mexicano · mexicana","Mexicaans"),("colombiano · colombiana","Colombiaans"),("argentino · argentina","Argentijns")]),
 ("Los idiomas · hablar",[("Hablo español","Ik spreek Spaans"),("Hablo neerlandés","Ik spreek Nederlands"),
   ("Hablo francés","Ik spreek Frans"),("¿Qué idiomas hablas?","Welke talen spreek je?"),("un poco","een beetje")]),
 ("Países del mundo hispano",[("España","Spanje"),("México","Mexico"),("Argentina","Argentinië"),("Colombia","Colombia"),("Perú","Peru")]),
]
def kitrow(es,nl):
    return f'<tr><td class="k-es">{es}</td><td class="k-nl gloss">{nl}</td><td class="k-ck"><span class="chk"></span></td></tr>'
def kittable(name,items):
    rows="".join(kitrow(*i) for i in items)
    return (f'<div class="kit"><div class="kit-h">{name}</div>'
      f'<table class="ktab"><thead><tr><th>Español</th><th>Nederlands</th><th>🔊 na</th></tr></thead><tbody>{rows}</tbody></table></div>')

def wl(cls=""): return f'<span class="wl {cls}"></span>'

CSS=FONTS+PRINTCSS+r"""
/* C4-rood override */
:root{ --g:#D64550; --gd:#A8323B; --gt:#FBEAEC; }
/* functionele kleursemantiek */
.p{color:#2563EB;font-weight:700}.v{color:#EA7317;font-weight:700}.pl{color:#0E9E97;font-weight:700}
/* Escucha transcript (print) */
.tl{display:flex;gap:3mm;padding:.55mm 0;font-size:9.5pt;break-inside:avoid}
.tl .sp{font-family:var(--disp);font-weight:700;color:var(--gd);width:22mm;flex:none}
.tl .tx b{background:var(--gt);border-radius:3pt;padding:.2mm 1.2mm;font-weight:700}
.twocol{column-count:2;column-gap:8mm}
/* Kit tabellen */
.kitwrap{display:grid;grid-template-columns:1fr 1fr;gap:3mm 5mm;margin-top:2mm}
.kit{break-inside:avoid}
.kit-h{font-family:var(--disp);font-weight:700;font-size:9.6pt;color:var(--gd);margin:1mm 0 .5mm}
.ktab{font-size:8.8pt;width:100%}.ktab th{background:var(--gt);color:var(--gd);font-size:7.2pt;text-transform:uppercase;padding:.8mm 2mm;text-align:left}
.ktab td{border-bottom:1px solid var(--line);padding:.55mm 2mm}.k-es{font-weight:600}.k-ck{text-align:center;width:12mm}
.chk{display:inline-block;width:3.4mm;height:3.4mm;border:1.3px solid var(--mut);border-radius:1.5pt;vertical-align:middle}
/* grammatica mini */
.gt2{width:100%;font-size:9.2pt;margin:2mm 0}.gt2 td{border-bottom:1px solid var(--line);padding:1.5mm 2.5mm}
.gt2 .p{color:#2563EB}.gt2 .v{color:#EA7317;font-family:var(--disp)}.gt2 .pl{color:#0E9E97}.gt2 .ex{color:var(--mut);font-style:italic}
.mv2{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin:2mm 0}
.mv2 div{border-radius:8pt;padding:2.5mm 4mm;font-family:var(--disp)}
.mv2 .m{background:#E8F0FE;color:#1E40AF}.mv2 .f{background:#FCE7F0;color:#9D174D}
.clock3{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin:2mm 0}
.clock3 div{border-radius:8pt;padding:2.5mm 3mm;font-family:var(--disp);text-align:center}
.clock3 b{color:var(--gd);display:block;margin-top:1mm}.clock3 .m{background:#FEF3E2}.clock3 .t{background:#FFF7DC}.clock3 .n{background:#E7ECFB}
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
.klemline{font-size:10pt;margin:3mm 0 0}.klemline .t{background:var(--gt);border-radius:4pt;padding:.3mm 1.6mm;font-weight:700;color:var(--gd)}
/* verrijking (bladspiegel: sectie vult pagina) */
.cast2{display:grid;grid-template-columns:repeat(5,1fr);gap:3mm;margin:3mm 0}
.cast2 .m{border:1px solid var(--line);border-top:3px solid var(--g);border-radius:8pt;padding:2.5mm;text-align:center;break-inside:avoid}
.cast2 .nm{font-family:var(--disp);font-weight:700;font-size:10pt;color:var(--gd)}.cast2 .ro{font-size:7.6pt;color:var(--mut)}.cast2 .fl{font-size:12pt}
.cogn{display:flex;flex-wrap:wrap;gap:2mm;margin:2mm 0}.cogn span{background:var(--gt);border-radius:20pt;padding:.8mm 3mm;font-size:9.2pt;font-weight:600;color:var(--gd)}
.vf{width:100%;font-size:9.5pt;margin:2mm 0}.vf td{border-bottom:1px solid var(--line);padding:1.9mm 2mm}.vf .b{width:26mm;text-align:center;color:var(--mut);white-space:nowrap}
.modelo{border-left:3px solid var(--g);background:var(--gt);border-radius:0 8pt 8pt 0;padding:2.5mm 5mm;margin:2mm 0;font-size:9.7pt}
.modelo b{color:var(--gd)}
.rubric{width:100%;font-size:9pt;margin:2mm 0}.rubric th{background:var(--g);color:#fff;text-align:left;padding:1.6mm 2.4mm;font-size:8pt}.rubric td{border:1px solid var(--line);padding:1.6mm 2.4mm}
.mapmini{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm;margin:2mm 0}
.mapmini .c{border:1px solid var(--line);border-left:3px solid var(--g);border-radius:8pt;padding:2.5mm 3mm;break-inside:avoid;font-size:9pt}
.mapmini .fl{font-size:15pt}.mapmini b{color:var(--gd);font-family:var(--disp)}
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
  <div class="eyebrow">EL DESPEGUE · PARADA 3 · SURVIVAL IN SPANISH</div>
  <h1>Nacionalidades y países</h1>
  <div class="sub">De kernvraag van de reis: <b>¿De dónde eres?</b> Zeggen waar je vandaan komt, je <b>nationaliteit</b> en welke <b>talen</b> je spreekt. <span class="gloss">Decir de dónde eres, tu nacionalidad y qué idiomas hablas — la pregunta que abre todo viaje.</span></div>
  <div class="q">¿De dónde eres? ¡Soy de Bélgica!</div>
</section>
<div class="page">
  <div class="obj"><div class="se">Al final de esta unidad · Op het einde van deze les</div>
    <ul>
      <li><span class="ck">✓</span> <span><span class="es">Preguntar y decir el origen</span> <span class="nl">— ¿de dónde eres? · soy de + país</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">La nacionalidad (gentilicio)</span> <span class="nl">— mexicano/a · español/a · belga</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Decir qué idiomas hablas</span> <span class="nl">— hablo español / neerlandés / francés</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Situar los <b>21 países</b> del mundo hispano</span> <span class="nl">— op de kaart</span></span></li>
    </ul>
  </div>
  <div class="guide"><span class="ic">🎒</span><div><span class="hand">¡Seguimos la ruta! Parada 3.</span><div class="g">In deze «survival»-les leer je de vraag die elke reis opent: <b>¿de dónde eres?</b> — en hoe je antwoordt met je land, je nationaliteit en je talen. Open de wereldkaart op de digitale hub!</div></div></div>

  <div class="se" style="margin-top:6mm">La gente de la ruta · je reisgenoten</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Je reist mee met vier jongeren uit de Spaanstalige wereld — élk uit een ander land met een andere <i>nacionalidad</i>. In de scène leert de directeur Fernando een reizigster de kernvraag.</p>
  <div class="cast2">
    <div class="m"><div class="fl">🇪🇸</div><div class="nm">Lucía</div><div class="ro">española · Sevilla</div></div>
    <div class="m"><div class="fl">🇲🇽</div><div class="nm">Diego</div><div class="ro">mexicano · CDMX</div></div>
    <div class="m"><div class="fl">🇨🇴</div><div class="nm">Valen</div><div class="ro">colombiana · Cartagena</div></div>
    <div class="m"><div class="fl">🇵🇪</div><div class="nm">Nina</div><div class="ro">peruana · Cusco</div></div>
    <div class="m"><div class="fl">🇧🇪</div><div class="nm">Tú</div><div class="ro">belga · de reiziger</div></div>
  </div>

  <div class="truc" style="margin-top:5mm"><b>¿Qué reconoces ya?</b> Deze «woorden van de wereld» lijken op het Nederlands of Engels (<i>palabras transparentes</i>) — durf te gissen:
    <div class="cogn"><span>internacional</span><span>la nación</span><span>el continente</span><span>la capital</span><span>europeo</span><span>americano</span><span>africano</span><span>el mapa</span><span>la región</span><span>el/la turista</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Tip: veel landen &amp; talen herken je meteen — <b>Italia</b>, <b>Portugal</b>, <b>el inglés</b>, <b>el árabe</b>…</span>
  </div>
</div>
"""

ESCUCHA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§1 · ¡Escucha!</div><h2>Bekijk de scène en lees mee</h2>
  <div class="audiorow">
    <div class="call"><span class="ic">🎬</span><div><b>Sitcom · Episodio 3 · Nacionalidades y países.</b> Scan de code en bekijk de aflevering op de digitale pagina. Fernando leert een reizigster de kernvraag <b>¿de dónde eres?</b> — en meteen de valstrik «soy Argelia» → «soy <b>de</b> Argelia». Luister eerst zónder te lezen; daarna lees je mee. De <b>vetgedrukte</b> woorden zijn chunks om mee te nemen.</div></div>
    <div class="qr"><div class="lab">Vídeo online</div>{qr(HUB_URL+"#escucha")}<div class="meta">hub · Escucha</div></div>
  </div>
  <div class="truc"><b>Antes de escuchar · vóór je luistert.</b> Welke landen en talen ga je horen, denk je? <span style="font-size:8.8pt;color:var(--mut)">(gis gerust)</span>
    <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.2">Un país: {wl('sm')} &nbsp;&nbsp; Una nacionalidad: {wl('sm')} &nbsp;&nbsp; Un idioma: {wl('sm')}</div>
  </div>
  <div class="twocol">{scenehtml(*SCENES[0])}{scenehtml(*SCENES[1])}{scenehtml(*SCENES[2])}</div>
  <div class="ojo"><b>¡Ojo!</b> De reizigster zegt «Yo soy Argelia» — maar dat betekent «ik <i>ben</i> Algerije». Juist is «Yo soy <b>de</b> Argelia» (ik kom <b>uit</b> Algerije). Land = met <b>de</b>; nationaliteit = zónder <b>de</b>: «soy argelin<b>a</b>».</div>

  <div class="se" style="margin-top:5mm">Después de escuchar · ¿Verdadero o falso?</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Kruis aan. Verbeter de <b>falsas</b> op de lijn.</p>
  <table class="vf">
    <tr><td>1. La mujer es de Argelia.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>2. Una chica de Argelia es «argelino».</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>3. La mujer habla tres idiomas: árabe, francés y español.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>4. Fernando cuenta: uno, dos, tres, cinco, diez, veinte.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
  </table>
</div>
"""

KIT=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Suena bien · pronunciación</div><h2>La ñ, la c/z &amp; el acento agudo</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 1mm">De <b>ñ</b> klinkt als de NL «nj» in «Spanje». Oefen online (QR §1): luister en spreek na.</p>
  <div class="cogn"><span>España</span><span>español</span><span>mañana</span><span>niño</span><span>señor</span><span>año</span></div>
  <div class="ojo"><b>¡Ojo!</b> ñ ≠ n: «a<b>ñ</b>o» (jaar) klinkt anders dan «ano». Het streepje (~) verandert de klank én de betekenis!</div>
  <p style="font-size:9.4pt;color:var(--mut);margin:2mm 0 1mm"><b>La c y la z:</b> in Spanje klinken <b>z</b> en <b>c</b> (vóór e/i) als een zachte <b>th</b>; in Latijns-Amerika als <b>s</b>. Allebei goed!</p>
  <div class="cogn"><span>nacionalidad</span><span>Francia</span><span>Venezuela</span><span>gracias</span><span>cinco</span><span>zona</span></div>
  <div class="ojo"><b>¡Ojo!</b> c + a/o/u = /k/ (<b>ca</b>sa, <b>co</b>lombiano) · maar c + e/i = /θ~s/ (<b>ci</b>nco, Fran<b>ci</b>a) — net als de z.</div>
  <div class="klemline"><b>El acento agudo · klemtoon op de laatste lettergreep (-dad / -és):</b> na·cio·na·li·<span class="t">DAD</span> · por·tu·<span class="t">GUÉS</span> · fran·<span class="t">CÉS</span> · in·<span class="t">GLÉS</span></div>

  <div class="se" style="margin-top:3mm">§2 · Kit de supervivencia</div><h2>De taal die je écht nodig hebt</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 2mm">Vink ☐ af telkens je een uitdrukking vlot kunt <b>naspreken</b>. Oefen ze online met audio.</p>
  <div class="kitwrap">{"".join(kittable(n,it) for n,it in CLUSTERS)}</div>
</div>
"""

GRAM=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§4 · Gramática en la práctica</div><h2>Kort en functioneel</h2>
  <div class="modelo"><b>🔎 Fíjate · kijk terug naar de scène.</b> Je hoorde het al: «¿De dónde <b>eres</b>?» → «<b>Soy de</b> Argelia» · «Eres argelin<b>a</b> (chica) · argelin<b>o</b> (chico)» · «<b>Hablo</b> español». Ontdek zelf het patroon — <i>eerst betekenis, dan de regel.</i></div>
  <div class="regla"><span class="tag">soy de + país · waar je vandaan komt</span>
    <table class="gt2"><tr><td class="p">yo</td><td class="v">soy de</td><td>ik kom uit</td><td class="ex"><b>Soy de</b> <span class="pl">Bélgica</span>.</td></tr>
    <tr><td class="p">tú</td><td class="v">eres de</td><td>jij komt uit</td><td class="ex">¿<b>Eres de</b> <span class="pl">España</span>?</td></tr>
    <tr><td class="p">él/ella/usted</td><td class="v">es de</td><td>hij/zij komt · u komt uit</td><td class="ex">María <b>es de</b> <span class="pl">Sevilla</span>.</td></tr></table>
    <p style="font-size:9pt;margin:1mm 0 0">⚠️ Zeg «soy <b>de</b> Argelia» (= ik kom <b>uit</b>), niet «soy Argelia». Land = met <b>de</b>; nationaliteit = zónder <b>de</b> (soy argelina).</p>
  </div>
  <div class="regla"><span class="tag">El gentilicio · man of vrouw (de nationaliteit)</span>
    <div class="mv2"><div class="m">♂ Un chico: mexican<b>o</b> · colombian<b>o</b> · portugu<b>és</b> · franc<b>és</b> · ingl<b>és</b></div><div class="f">♀ Una chica: mexican<b>a</b> · colombian<b>a</b> · portugu<b>esa</b> · franc<b>esa</b> · ingl<b>esa</b></div></div>
    <p style="font-size:9pt;margin:1mm 0 0">Sommige blijven gelijk (♂=♀): <b>belga</b>, <b>marroquí</b>, <b>estadounidense</b>, <b>canadiense</b>. ⚠️ In het Spaans met een <b>kleine letter</b>: soy <b>español</b>, hablo <b>neerlandés</b> (in het NL/Engels net met hoofdletter!).</p>
  </div>
  <div class="regla"><span class="tag">hablo + idioma · welke talen je spreekt</span>
    <table class="gt2"><tr><td class="v">Hablo</td><td>ik spreek</td><td class="ex"><b>Hablo</b> neerlandés y un poco de español.</td></tr>
    <tr><td class="v">¿Hablas…?</td><td>spreek jij…?</td><td class="ex">¿<b>Hablas</b> francés?</td></tr>
    <tr><td class="v">¿Habla usted…?</td><td>spreekt u…?</td><td class="ex">¿<b>Habla usted</b> inglés?</td></tr></table>
    <p style="font-size:9pt;margin:1mm 0 0">De vrouw in de video spreekt <b>tres idiomas</b>: árabe, francés y español. Steun: «un poco» / «bastante bien».</p>
  </div>
  <div class="regla"><span class="tag">tú ↔ usted</span>
    <p style="margin:1mm 0 0;font-size:9.6pt">Met vrienden/klasgenoten: <b>tú</b> — <span class="ex" style="color:var(--mut)">¿De dónde eres?</span><br>Formeel, met een onbekende volwassene: <b>usted</b> — <span class="ex" style="color:var(--mut)">¿De dónde es usted? / ¿Habla usted francés?</span></p>
  </div>
  <div class="truc"><b>Mini-oefening 1 · soy de.</b> Vul aan met <i>soy de · eres de · es de</i>:
    <div style="margin-top:2mm;font-size:9.6pt;line-height:2.4">1. Yo {wl('sm')} Bélgica. &nbsp; 2. ¿{wl('sm')} (tú) España? &nbsp; 3. Diego {wl('sm')} México. &nbsp; 4. ¿De dónde {wl('sm')} usted?</div>
  </div>
  <div class="truc"><b>Mini-oefening 2 · país → gentilicio.</b> Schrijf de nationaliteit (♂/♀, kleine letter): a) México (chico) → {wl('sm')} &nbsp; b) Colombia (chica) → {wl('sm')} &nbsp; c) Francia (chica) → {wl('sm')}</div>
</div>
"""

def act(n,title,badges,body):
    bh="".join(f'<span class="badge {c}">{t}</span>' for t,c in badges)
    return (f'<div class="act"><div class="acthead"><div class="anum">{n}</div><div><div class="h">{title}</div>'
            f'<div class="badges">{bh}</div></div></div>{body}</div>')

PRAC=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§3 · Práctica</div><h2>Oefen op papier — online verbeter je alles</h2>

  {act(1,"Clasifica: país, gentilicio o idioma",[("receptief","skill"),("5 min","")],
    '<p style="margin-left:12.5mm">Schrijf elk woord in de juiste kolom. Voeg onderaan één eigen woord toe.<br><span class="gloss">España · mexicana · el árabe · Colombia · belga · el inglés · Argentina · francés (idioma)</span></p>'
    +'<div class="wcols" style="margin-left:12.5mm"><div class="wcol"><h4>País 🌍</h4><div class="fill"></div></div><div class="wcol"><h4>Gentilicio 🪪</h4><div class="fill"></div></div><div class="wcol"><h4>Idioma 🗣️</h4><div class="fill"></div></div><div class="wcol"><h4>Tu palabra</h4><div class="fill"></div></div></div>')}

  {act(2,"Relaciona país ↔ nacionalidad",[("gestuurd","skill"),("★☆☆","")],
    '<p style="margin-left:12.5mm">Trek een lijn tussen het land en de nationaliteit (♂/♀).</p>'
    +'<table class="mtab" style="margin-left:12.5mm"><tr><td class="a">1. España</td><td><span class="ln"></span></td><td class="b">a. mexicano / mexicana</td></tr>'
    +'<tr><td class="a">2. México</td><td><span class="ln"></span></td><td class="b">b. colombiano / colombiana</td></tr>'
    +'<tr><td class="a">3. Colombia</td><td><span class="ln"></span></td><td class="b">c. español / española</td></tr>'
    +'<tr><td class="a">4. Argentina</td><td><span class="ln"></span></td><td class="b">d. belga</td></tr>'
    +'<tr><td class="a">5. Bélgica</td><td><span class="ln"></span></td><td class="b">e. argentino / argentina</td></tr></table>')}

  {act(3,"Completa el diálogo",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Vul het gesprek aan (denk aan <i>soy de</i> + land, en de gentilicio).</p>'
    +f'<div style="margin-left:12.5mm;font-size:10pt;line-height:2.5">'
    +f'— Hola, ¿de dónde {wl("sm")}?<br>— {wl("sm")} de México. Soy {wl("sm")} <span style="color:var(--mut);font-size:8.6pt">(un chico)</span>.<br>— ¿Qué idiomas {wl("sm")}?<br>— {wl("sm")} español e inglés.</div>')}

  {act(4,"Ordena la conversación",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Nummer de zinnen in de juiste volgorde (1–5).</p>'
    +'<div class="scramble" style="margin-left:12.5mm"><span>___ Hablo español y un poco de inglés.</span><span>___ Hola, ¿de dónde eres?</span><span>___ ¡Encantado! Hasta luego.</span><span>___ Soy de Colombia, de Cartagena.</span><span>___ ¡Qué bien! ¿Y qué idiomas hablas?</span></div>')}

  {act(5,"La nacionalidad · ¿-o o -a?",[("gestuurd","skill"),("★☆☆","")],
    f'<p style="margin-left:12.5mm">Vul de juiste letter in (♂ -o / ♀ -a).</p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. Diego (chico) es mexican{wl("sm")} &nbsp; 2. Valen (chica) es colombian{wl("sm")} &nbsp; 3. Mateo (chico) es argentin{wl("sm")} &nbsp; 4. Nina (chica) es peruan{wl("sm")}</div>')}

  {act(6,"Entrevista a un compañero",[("interactie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Vraag het aan drie klasgenoten en noteer het antwoord. Wissel van rol.</p>'
    +f'<table class="wtab" style="margin-left:12.5mm;margin-top:2mm"><thead><tr><th style="width:38mm">Pregunta</th><th>Compañero/a 1</th><th>Compañero/a 2</th><th>Compañero/a 3</th></tr></thead>'
    +'<tr><td style="height:12mm">¿De dónde eres?</td><td></td><td></td><td></td></tr>'
    +'<tr><td style="height:12mm">¿Qué idiomas hablas?</td><td></td><td></td><td></td></tr></table>')}

  {act(7,"Escribe tres fichas",[("productie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Schrijf voor 3 personen (bekend of verzonnen): «X es de ___. Es ___ y habla ___.» (2 zinnen elk).</p>'
    +'<div class="wbox" style="margin-left:12.5mm"></div>')}

  {act(8,"Escribe un mensaje",[("productie","skill"),("★★★","")],
    '<p style="margin-left:12.5mm">Schrijf een kort chatbericht (WhatsApp) aan een nieuwe Spaanstalige vriend(in): stel je voor met land, nationaliteit en talen.</p>'
    +'<div class="wbox" style="margin-left:12.5mm;min-height:28mm"></div>')}

  {act(9,"¿De qué país?",[("productie","skill"),("★★☆","")],
    f'<p style="margin-left:12.5mm">Schrijf bij elke vlag het land én de nationaliteit (♂). Snel!</p>'
    +f'<div style="margin-left:12.5mm;font-size:9.8pt;line-height:2.3">🇲🇽 → {wl("lg")} &nbsp;&nbsp; 🇪🇸 → {wl("lg")}<br>🇨🇴 → {wl("lg")} &nbsp;&nbsp; 🇦🇷 → {wl("lg")}</div>')}
</div>
"""

TAREA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§5 · Tarea final</div><h2>Mi mapa · ¿De dónde eres?</h2>
  <div class="esen" style="margin-top:2mm"><b class="tt">Jouw opdracht.</b> Maak een <b>mini-kaart</b> met <b>3 personen</b> (jezelf + 2 anderen: klasgenoten of bekende personen). Zeg per persoon uit welk <b>land</b> ze komen (soy/es de), hun <b>nationaliteit</b> en welke <b>talen</b> ze spreken. Wijs het land aan op de wereldkaart (Mapa-tab) en stel ze voor. <span class="gloss">Sin leer del papel — zonder van het blad af te lezen.</span></div>
  <div class="regla" style="margin-top:4mm"><span class="tag">Prepárate · vul eerst de frames in (jouw versie)</span>
    <div style="margin-top:2mm;font-size:9.7pt;line-height:2.4">🧍 Yo soy de {wl('sm')} . Soy {wl('sm')} y hablo {wl('sm')} .<br>🧑 ____ es de {wl('sm')} . Es {wl('sm')} y habla {wl('sm')} .<br>👤 ____ es de {wl('sm')} . Es {wl('sm')} y habla {wl('sm')} .</div>
  </div>
  <div style="margin-top:4mm"><div class="se">Mi mapa · noteer je 3 fichas</div>
    <table class="wtab" style="margin-top:2mm"><thead><tr><th style="width:30mm">Nombre</th><th>Es de… (país)</th><th>Es… (nacionalidad)</th><th>Habla… (idiomas)</th></tr></thead>
      <tr><td style="height:15mm">🧍 (yo)</td><td></td><td></td><td></td></tr>
      <tr><td style="height:15mm">🧑</td><td></td><td></td><td></td></tr>
      <tr><td style="height:15mm">👤</td><td></td><td></td><td></td></tr></table>
  </div>
  <div class="regla" style="margin-top:4mm"><span class="tag">Palabras y frases útiles</span>
    <p style="margin:1mm 0 0;font-size:9.6pt">¿De dónde eres? · Soy de + país · Es de + país · Soy/es + nacionalidad (mexicano-a, español-a, belga…) · Hablo/habla + idioma (español, neerlandés, francés, inglés, árabe) · un poco · bastante bien</p>
  </div>
  <div class="modelo" style="margin-top:4mm"><b>Modelo · zo klinkt het:</b><br>
    — Yo soy de Bélgica. Soy belga y hablo neerlandés y un poco de español.<br>
    — Ella es de México. Es mexicana y habla español e inglés.</div>
  <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div class="truc" style="margin:0"><b>🏁 Klaar als…</b> je voor 3 personen «es de + land» zegt én de juiste <b>gentilicio</b> (♂/♀, kleine letter) en <b>talen</b> geeft, en het land op de kaart aanwijst — zónder af te lezen.</div>
    <table class="rubric"><thead><tr><th>Evaluatie</th><th style="text-align:center">🟢🟡🔴</th></tr></thead>
      <tr><td>soy/es de + país correct</td><td></td></tr>
      <tr><td>gentilicio (♂/♀) correct</td><td></td></tr>
      <tr><td>idiomas + uitspraak &amp; durf</td><td></td></tr></table>
  </div>
  <p style="font-size:9pt;color:var(--mut);margin-top:3mm">Reflexión · <b>¿Qué me costó?</b> Wat vond je moeilijk? {wl('lg')}</p>
</div>
"""

BANDAS=[("Shakira","Hips Don't Lie","🇨🇴 Colombia"),("Bad Bunny","Baile inolvidable","🇵🇷 Puerto Rico"),("Rosalía","La Perla","🇪🇸 España"),
 ("Karol G","TQG","🇨🇴 Colombia"),("Quevedo","Bzrp #52","🇪🇸 España"),("Rauw Alejandro","Todo de ti","🇵🇷 Puerto Rico")]
def banda(a,s,g): return f'<div class="banda"><div class="ar">{a}</div><div class="sg">🎵 {s}</div><div class="ge">{g}</div></div>'
MUSICA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Cultura · Banda sonora</div><h2>El mundo hispano &amp; su música</h2>
  <p style="font-size:9.6pt">El <b>español</b> is één taal die <b>21 landen</b> verbindt en door meer dan <b>490 miljoen</b> mensen wordt gesproken — de op één na meest gesproken moedertaal ter wereld. Eén taal, veel accenten en culturen. Zelfs in Afrika: <b>Guinea Ecuatorial</b>. En de artiesten van de banda sonora komen uit heel die wereld:</p>
  <div class="bandas">{"".join(banda(*b) for b in BANDAS)}</div>
  <div class="musrow">
    <div class="call"><span class="ic">🎧</span><div><b>Spotify · la playlist de la clase.</b> Scan en luister. Op de digitale pagina vind je ook <b>LyricsTraining</b> en de <b>wereldkaart</b> (klik op elk land voor zijn fiche).</div></div>
    <div class="qr"><div class="lab">Playlist</div>{qr(SPOTIFY)}<div class="meta">Spotify</div></div>
  </div>

  <div class="truc" style="margin-top:5mm"><b>El mundo hispano · sabías que…?</b> Verbind (gis gerust):
    <table class="mtab" style="margin-top:1mm"><tr><td class="a">El único país hispanohablante en África…</td><td>{wl('sm')}</td><td class="b">a. México (~130 millones)</td></tr>
    <tr><td class="a">El país con más hispanohablantes…</td><td>{wl('sm')}</td><td class="b">b. Guinea Ecuatorial</td></tr>
    <tr><td class="a">El gentilicio se escribe con…</td><td>{wl('sm')}</td><td class="b">c. minúscula (soy belga)</td></tr></table>
    <p style="font-size:8.6pt;color:var(--mut);margin-top:1mm">💡 «americano» betekent niet enkel «uit de VS»: héél América (Noord, Midden én Zuid) is <b>América</b>.</p>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div><div class="se">¿De qué país? · verbind de artiest</div>
      <table class="mtab"><tr><td class="a">Shakira · Karol G</td><td>{wl('sm')}</td><td class="b">a. Puerto Rico</td></tr>
      <tr><td class="a">Bad Bunny · Rauw Alejandro</td><td>{wl('sm')}</td><td class="b">b. España</td></tr>
      <tr><td class="a">Rosalía · Quevedo</td><td>{wl('sm')}</td><td class="b">c. Colombia</td></tr></table>
    </div>
    <div class="truc" style="margin:0"><b>Escucha y responde.</b> Kies één nummer van de playlist.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.3">Mi canción: {wl('lg')}<br>El/la artista es de: {wl('lg')}</div>
    </div>
  </div>
</div>
"""

REPASO=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Repaso · Lo esencial de un vistazo</div><h2>Wat je nu kunt</h2>
  <div class="fams">
    <div class="pcard"><div class="t">Zo vraag &amp; zeg je het origen</div><div class="ej">¿<b>De dónde eres</b>? → <b>Soy de</b> + país (Soy de Bélgica).</div><div class="t2">Land = met <b>de</b> · nationaliteit = zónder de (soy belga).</div></div>
    <div class="pcard"><div class="t">Nationaliteit &amp; talen</div><div class="ej">Soy mexican<b>o</b>/mexican<b>a</b> · Hablo español, neerlandés…</div><div class="anchor"><b>-o</b> = ♂ · <b>-a</b> = ♀ &nbsp;|&nbsp; kleine letter: <b>belga</b>, <b>francés</b></div></div>
  </div>
  <div class="regla" style="margin:4mm 0"><span class="tag">Frases para la clase</span>
    <div class="cogn" style="margin-top:1mm"><span>¿Cómo se dice… ?</span><span>¿Qué significa… ?</span><span>Otra vez, por favor</span><span>No entiendo</span><span>¿Puedes repetir?</span><span>Más despacio, por favor</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Handige klaszinnen — gebruik ze in het Spaans i.p.v. Nederlands.</span>
  </div>
  <table class="sem"><thead><tr><th style="text-align:left">Puedo… · Ik kan…</th><th>🟢</th><th>🟡</th><th>🔴</th></tr></thead>
    <tr><td>vragen en zeggen waar iemand vandaan komt (soy de + país)</td><td></td><td></td><td></td></tr>
    <tr><td>de nationaliteit geven (♂/♀, kleine letter)</td><td></td><td></td><td></td></tr>
    <tr><td>zeggen welke talen ik spreek (hablo…)</td><td></td><td></td><td></td></tr>
    <tr><td>landen van het mundo hispano op de kaart situeren</td><td></td><td></td><td></td></tr></table>
  <div class="regla" style="margin-top:5mm"><span class="tag">Mini-test · recuerda sin mirar</span>
    <p style="margin:1mm 0 0;font-size:9.4pt">Sluit de cursus en vertaal uit het hoofd (ophalen = het beste leren).</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3mm 8mm;margin-top:2mm;font-size:9.8pt;line-height:2.2">
      <div>1. waar kom je vandaan? → {wl('')}</div><div>2. ik kom uit België → {wl('')}</div>
      <div>3. ik ben Belgisch → {wl('')}</div><div>4. welke talen spreek je? → {wl('')}</div>
      <div>5. ik spreek Nederlands → {wl('')}</div><div>6. zij is Mexicaanse → {wl('')}</div>
    </div>
  </div>
  <div class="guide"><span class="ic">🎮</span><div><span class="hand">Repasa jugando</span><div class="g">Oefen alles online met spelletjes, flashcards, de <b>wereldkaart</b> en audio op de digitale hub (scan de QR bij §1).</div></div></div>
  <div class="bridge"><b>Próxima parada →</b> In de volgende unit stel je je familie voor: <i>la familia</i>. ¡Hasta pronto!</div>
</div>
"""

EDITBAR="""
<div class="editbar" id="eb">
  <b>✏️ C4 · U3</b>
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
document.getElementById('btnsave').onclick=function(){var html='<!doctype html>'+document.documentElement.outerHTML;var b=new Blob([html],{type:'text/html'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='C4_U3_Nacionalidades_bewerkt.html';a.click();};
</script>
"""

HTML=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 3 · Nacionalidades y países</title><style>{CSS}</style></head><body>
{EDITBAR}
{HERO}{ESCUCHA}{KIT}{GRAM}{PRAC}{TAREA}{MUSICA}{FUNCIONES_SEC}{REPASO}
{SCRIPT}
</body></html>"""
os.makedirs(f"{ROOT}/03-build/web/print",exist_ok=True)
open(f"{ROOT}/03-build/web/print/C4_U3.html","w",encoding="utf-8").write(HTML)
print("C4_U3.html (print+editable) geschreven:",len(HTML),"bytes")
