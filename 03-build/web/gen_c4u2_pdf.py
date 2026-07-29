#!/usr/bin/env python3
# C4 · Unidad 2 — PRINT (HTML=bron → PDF via Chromium). Golden-sample print-kit, C4-rood.
# Thema: Saludos por el día + estar + estado. Zelfde pijplijn/CSS als U1.
import base64, os, re, segno, io, sys
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
from funciones_print import print_section
FUNCIONES_SEC=print_section(2)
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
HUB_URL="https://hablacon-ene.local/C4/U2"   # placeholder → auteur vervangt door de gehoste hub-URL
import comprension_print
COMPR_SEC=comprension_print.print_section(2, HUB_URL)
SPOTIFY="https://open.spotify.com/playlist/37i9dQZF1DXaxEKcoCdWHD"

# ── data · transcript Episodio 2 (exact, door auteur aangeleverd) ──────────────
SCENES=[
 ("Escena 1 · Por la mañana (09.00 h)",[
  ("Julio","Josefina… Buenos días."),("Josefina","Buenos días."),("Julio","Yo es que…"),
  ("Josefina","¿Cómo estás?"),("Julio","Bien, bien. Pero es María, la nueva profesora."),
  ("Josefina","Yo estoy ocupada."),("Julio","Ya. ¿Muy ocupada?"),("Josefina","Muy ocupada."),
 ]),
 ("Escena 2 · Por la tarde (16.00 h)",[
  ("María","Josefina."),("Josefina","Buenas tardes."),("María","Buenas tardes. Josefina, Julio es…"),
  ("Josefina","¿Cómo estás?"),("María","Un poco nerviosa, la verdad. Julio está mal, está enfermo."),
  ("Josefina","Yo estoy enferma. Un poco enferma."),("María","Ya. Bueno, pues nada. Hasta luego. Adiós."),("Josefina","Adiós."),
 ]),
 ("Escena 3 · Por la noche (21.05 h)",[
  ("Fernando","¿Qué?"),("Josefina","Ay… buenas noches."),("Fernando","¿Cómo está María? ¿Y cómo está Julio?"),
  ("Fernando","Y tú, ¿cómo estás?"),("Josefina","Uf, cansada, muy cansada."),
  ("Fernando","¿Mucho trabajo?"),("Josefina","Demasiado. Todos con problemas. Es muy cansado."),
 ]),
]
CH=["Buenos días","Buenas tardes","Buenas noches","¿Cómo estás?","¿Cómo está","estoy ocupada","Muy ocupada",
 "está enfermo","estoy enferma","cansada","muy cansada","Hasta luego","Adiós","Bien, bien","la verdad","Demasiado","muy cansado"]
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
 ("Saludar por el día · begroeten",[("Buenos días","Goedemorgen"),("Buenas tardes","Goedemiddag"),
   ("Buenas noches","Goedenavond"),("¡Hola!","Hallo"),("¡Buenas!","Hoi (informeel)")]),
 ("Preguntar cómo va · vragen",[("¿Qué tal?","Hoe gaat het?"),("¿Cómo estás?","Hoe gaat het? (jij)"),
   ("¿Cómo está usted?","… met u?"),("¿Y tú?","En jij?")]),
 ("Decir cómo estoy · estar",[("Estoy bien","Ik voel me goed"),("Muy bien","Heel goed"),("Regular","Gaat wel"),
   ("Estoy cansado/a","Ik ben moe"),("Estoy ocupado/a","Ik heb het druk"),("Estoy nervioso/a","Ik ben nerveus"),("Estoy enfermo/a","Ik ben ziek")]),
 ("Cortesía · beleefdheid",[("Por favor","Alsjeblieft"),("Gracias","Dank je"),("Muchas gracias","Hartelijk dank"),
   ("De nada","Graag gedaan"),("Perdona","Sorry")]),
 ("Despedirse · afscheid",[("Adiós","Dag"),("Hasta luego","Tot straks"),("Hasta mañana","Tot morgen"),("¡Nos vemos!","We zien elkaar!"),("Chao","Doei")]),
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
.p{color:#2563EB;font-weight:700}.v{color:#EA7317;font-weight:700}
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
.gt2 .p{color:#2563EB}.gt2 .v{color:#EA7317;font-family:var(--disp)}.gt2 .ex{color:var(--mut);font-style:italic}
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
  <div class="eyebrow">EL DESPEGUE · PARADA 2 · SURVIVAL IN SPANISH</div>
  <h1>Saludos</h1>
  <div class="sub">Groeten volgens het <b>moment van de dag</b> en zeggen <b>hoe je je voelt</b>. <span class="gloss">Saludar según la hora y decir cómo estás — todo lo que oyes, lo puedes usar enseguida.</span></div>
  <div class="q">¡Buenos días! ¿Qué tal?</div>
</section>
<div class="page">
  <div class="obj"><div class="se">Al final de esta unidad · Op het einde van deze les</div>
    <ul>
      <li><span class="ck">✓</span> <span><span class="es">Saludar según el momento del día</span> <span class="nl">— días / tardes / noches</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Preguntar y decir cómo estás</span> <span class="nl">— estar + estado (bien, cansado…)</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Despedirte</span> <span class="nl">— adiós · hasta luego · hasta mañana</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Distinguir <b>-o/-a</b> y <b>tú/usted</b></span> <span class="nl">— man/vrouw & informeel/beleefd</span></span></li>
    </ul>
  </div>
  <div class="guide"><span class="ic">🎒</span><div><span class="hand">¡Seguimos la ruta! Parada 2.</span><div class="g">In deze «survival»-les leer je begroeten op elk moment van de dag én zeggen hoe je je voelt. Luister, spreek na, en probeer het zelf.</div></div></div>

  <div class="se" style="margin-top:6mm">La gente de la ruta · je reisgenoten</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Je reist mee met vier jongeren uit de Spaanstalige wereld. In de scène ontmoet je de academia: Julio, María, Josefina en de directeur Fernando.</p>
  <div class="cast2">
    <div class="m"><div class="fl">🇪🇸</div><div class="nm">Lucía</div><div class="ro">Sevilla · familie</div></div>
    <div class="m"><div class="fl">🇲🇽</div><div class="nm">Diego</div><div class="ro">CDMX · eten & markt</div></div>
    <div class="m"><div class="fl">🇨🇴</div><div class="nm">Valen</div><div class="ro">Cartagena · wonen</div></div>
    <div class="m"><div class="fl">🇵🇪</div><div class="nm">Nina</div><div class="ro">Cusco · reizen</div></div>
    <div class="m"><div class="fl">🎒</div><div class="nm">Tú</div><div class="ro">jij, de reiziger</div></div>
  </div>

  <div class="truc" style="margin-top:5mm"><b>¿Qué reconoces ya?</b> Deze «woorden om je te voelen» lijken op het Nederlands of Engels (<i>palabras transparentes</i>) — durf te gissen:
    <div class="cogn"><span>nervioso</span><span>el problema</span><span>el hospital</span><span>ocupado (occupied)</span><span>fatal</span><span>regular</span><span>la persona</span><span>importante</span><span>el momento</span><span>el trabajo (travail)</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Tip: veel <i>estados</i> herken je meteen — <b>nervioso</b>, <b>fatal</b>, <b>regular</b>…</span>
  </div>
</div>
"""

ESCUCHA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§1 · ¡Escucha!</div><h2>Bekijk de scène en lees mee</h2>
  <div class="audiorow">
    <div class="call"><span class="ic">🎬</span><div><b>Sitcom · Episodio 2 · Saludos.</b> Scan de code en bekijk de aflevering op de digitale pagina. De scène speelt op <b>drie momenten</b>: 09.00 · 16.00 · 21.05 u. Luister eerst zónder te lezen; daarna lees je mee. De <b>vetgedrukte</b> woorden zijn chunks om mee te nemen.</div></div>
    <div class="qr"><div class="lab">Vídeo online</div>{qr(HUB_URL+"#escucha")}<div class="meta">hub · Escucha</div></div>
  </div>
  <div class="truc"><b>Antes de escuchar · vóór je luistert.</b> Kijk naar de klok. Welke groet hoor je op elk moment? <span style="font-size:8.8pt;color:var(--mut)">(gis gerust)</span>
    <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.2">09.00 → {wl('sm')} &nbsp;&nbsp; 16.00 → {wl('sm')} &nbsp;&nbsp; 21.05 → {wl('sm')}</div>
  </div>
  <div class="twocol">{scenehtml(*SCENES[0])}{scenehtml(*SCENES[1])}{scenehtml(*SCENES[2])}</div>
  <div class="ojo"><b>¡Ojo!</b> Iedereen is «un poco» iets: <b>ocupada</b> (druk), <b>nerviosa</b> (nerveus), <b>enferma</b> (ziek), <b>cansada</b> (moe). Hoe je je voelt = <b>estar</b>: «estoy cansada», niet «soy cansada».</div>

  <div class="se" style="margin-top:5mm">Después de escuchar · ¿Verdadero o falso?</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Kruis aan. Verbeter de <b>falsas</b> op de lijn.</p>
  <table class="vf">
    <tr><td>1. Por la mañana, Josefina está muy ocupada.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>2. Por la tarde, María está tranquila y muy bien.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>3. Julio está enfermo.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>4. Por la noche, Josefina está cansada.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
  </table>
</div>
"""

KIT=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Suena bien · pronunciación</div><h2>La jota /x/, la h muda &amp; el acento</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 1mm">De <b>j</b> (en <b>g</b> vóór e/i) is een <b>keelklank</b> /x/ — zoals de NL «g», maar krachtiger. Oefen online (QR §1): luister en spreek na.</p>
  <div class="cogn"><span>Josefina</span><span>jueves</span><span>gente</span><span>gimnasio</span><span>trabajo</span><span>mujer</span></div>
  <div class="ojo"><b>¡Ojo!</b> g + a/o/u = /g/ (<b>ga</b>to, <b>gu</b>sto) · maar g + e/i = /x/ (<b>ge</b>nte, <b>gi</b>mnasio) — net als de j.</div>
  <p style="font-size:9.4pt;color:var(--mut);margin:2mm 0 1mm"><b>La h muda:</b> je schrijft de <b>h</b> wél, maar je hóórt ze niet. «hola» klinkt als «ola».</p>
  <div class="cogn"><span>hola</span><span>hasta</span><span>hija</span><span>ahora</span><span>hombre</span><span>hospital</span></div>
  <div class="klemline"><b>El acento · klemtoon in de saludos:</b> bue·nos <span class="t">DÍ</span>·as · bue·nas <span class="t">TAR</span>·des · bue·nas <span class="t">NO</span>·ches</div>

  <div class="se" style="margin-top:3mm">§2 · Kit de supervivencia</div><h2>De taal die je écht nodig hebt</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 2mm">Vink ☐ af telkens je een uitdrukking vlot kunt <b>naspreken</b>. Oefen ze online met audio.</p>
  <div class="kitwrap">{"".join(kittable(n,it) for n,it in CLUSTERS)}</div>
</div>
"""

GRAM=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§4 · Gramática en la práctica</div><h2>Kort en functioneel</h2>
  <div class="modelo"><b>🔎 Fíjate · kijk terug naar de scène.</b> Je hoorde het al: «¿Cómo <b>estás</b>?» → «<b>estoy</b> ocupada» · «<b>estoy</b> cansada» · «Buen<b>os</b> días · Buen<b>as</b> tardes». Ontdek zelf het patroon — <i>eerst betekenis, dan de regel.</i></div>
  <div class="regla"><span class="tag">estar · hoe je je voelt</span>
    <table class="gt2"><tr><td class="p">yo</td><td class="v">estoy</td><td>ik ben / voel me</td><td class="ex">Yo <b>estoy</b> bien.</td></tr>
    <tr><td class="p">tú</td><td class="v">estás</td><td>jij bent / voelt je</td><td class="ex">¿Cómo <b>estás</b>?</td></tr>
    <tr><td class="p">él/ella/usted</td><td class="v">está</td><td>hij/zij is · u bent</td><td class="ex">¿Cómo <b>está</b> María?</td></tr></table>
    <p style="font-size:9pt;margin:1mm 0 0">⚠️ Hoe je je <b>voelt</b> = <b>estar</b> (niet <i>ser</i>): «Estoy bien», niet «Soy bien».</p>
  </div>
  <div class="regla"><span class="tag">Buenos días / tardes / noches · groeten volgens de klok</span>
    <div class="clock3"><div class="m">🌅 la mañana · ~6–12 u<b>Buenos días</b></div><div class="t">☀️ la tarde · ~12–20 u<b>Buenas tardes</b></div><div class="n">🌙 la noche · ~20–6 u<b>Buenas noches</b></div></div>
    <p style="font-size:9pt;margin:1mm 0 0">Let op de uitgang: buen<b>os</b> día<b>s</b> (♂) maar buen<b>as</b> tarde<b>s</b>/noche<b>s</b> (♀). «Buenas noches» = goedenavond én goodnight.</p>
  </div>
  <div class="regla"><span class="tag">-o / -a · man of vrouw (op de estados)</span>
    <div class="mv2"><div class="m">♂ Un chico: estoy cansad<b>o</b> · ocupad<b>o</b> · nervios<b>o</b> · enferm<b>o</b></div><div class="f">♀ Una chica: estoy cansad<b>a</b> · ocupad<b>a</b> · nervios<b>a</b> · enferm<b>a</b></div></div>
    <p style="font-size:9pt;margin:1mm 0 0">Josefina zegt «estoy cansad<b>a</b>»; Julio zegt «estoy enferm<b>o</b>».</p>
  </div>
  <div class="regla"><span class="tag">tú ↔ usted</span>
    <p style="margin:1mm 0 0;font-size:9.6pt">Met vrienden/klasgenoten: <b>tú</b> — <span class="ex" style="color:var(--mut)">¿Cómo estás?</span><br>Formeel, met een onbekende volwassene / de directeur: <b>usted</b> — <span class="ex" style="color:var(--mut)">¿Cómo está usted?</span></p>
  </div>
  <div class="truc"><b>Mini-oefening 1 · estar.</b> Vul aan met <i>estoy · estás · está</i>:
    <div style="margin-top:2mm;font-size:9.6pt;line-height:2.4">1. Yo {wl('sm')} bien. &nbsp;&nbsp; 2. ¿Cómo {wl('sm')} (tú)? &nbsp;&nbsp; 3. María {wl('sm')} cansada. &nbsp;&nbsp; 4. Julio {wl('sm')} enfermo. &nbsp;&nbsp; 5. ¿Cómo {wl('sm')} usted?</div>
  </div>
  <div class="truc"><b>Mini-oefening 2 · ¿qué saludo?</b> Schrijf de juiste groet bij het uur.
    <div style="margin-top:2mm;font-size:9.6pt;line-height:2.4">a) 08.30 → {wl('lg')}<br>b) 17.00 → {wl('lg')}<br>c) 22.15 → {wl('lg')}</div>
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
    '<p style="margin-left:12.5mm">Schrijf elke uitdrukking in de juiste kolom. Voeg onderaan één eigen woord toe.<br><span class="gloss">Buenos días · Adiós · Gracias · ¿Cómo estás? · Estoy cansada · Hasta luego · De nada · Buenas noches</span></p>'
    +'<div class="wcols" style="margin-left:12.5mm"><div class="wcol"><h4>Saludar</h4><div class="fill"></div></div><div class="wcol"><h4>Estado (¿cómo?)</h4><div class="fill"></div></div><div class="wcol"><h4>Cortesía</h4><div class="fill"></div></div><div class="wcol"><h4>Despedirse</h4><div class="fill"></div></div></div>')}

  {act(2,"Relaciona · verbind",[("gestuurd","skill"),("★☆☆","")],
    '<p style="margin-left:12.5mm">Trek een lijn tussen het Spaans en de betekenis.</p>'
    +'<table class="mtab" style="margin-left:12.5mm"><tr><td class="a">1. Buenos días</td><td><span class="ln"></span></td><td class="b">a. ik ben moe</td></tr>'
    +'<tr><td class="a">2. ¿Cómo estás?</td><td><span class="ln"></span></td><td class="b">b. tot morgen</td></tr>'
    +'<tr><td class="a">3. Estoy cansada</td><td><span class="ln"></span></td><td class="b">c. goedemorgen</td></tr>'
    +'<tr><td class="a">4. Hasta mañana</td><td><span class="ln"></span></td><td class="b">d. graag gedaan</td></tr>'
    +'<tr><td class="a">5. De nada</td><td><span class="ln"></span></td><td class="b">e. hoe gaat het?</td></tr></table>')}

  {act(3,"Completa el diálogo",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Vul het gesprek aan (denk aan <i>estar</i>).</p>'
    +f'<div style="margin-left:12.5mm;font-size:10pt;line-height:2.5">'
    +f'— Buenos {wl("sm")}, ¿cómo {wl("sm")}?<br>— {wl("sm")} bien, gracias. ¿Y tú?<br>— Regular… {wl("sm")} un poco cansada.<br>— Vaya. ¡Hasta {wl("sm")}!</div>')}

  {act(4,"Ordena la conversación",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Nummer de zinnen in de juiste volgorde (1–5).</p>'
    +'<div class="scramble" style="margin-left:12.5mm"><span>___ Regular, estoy un poco cansado.</span><span>___ Buenos días, ¿qué tal?</span><span>___ Adiós, hasta mañana.</span><span>___ Muy bien, ¿y tú?</span><span>___ Mucho trabajo. ¡Hasta luego!</span></div>')}

  {act(5,"Estoy… ¿-o o -a?",[("gestuurd","skill"),("★☆☆","")],
    f'<p style="margin-left:12.5mm">Vul de juiste letter in (♂ -o / ♀ -a).</p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. (Julio) estoy cansad{wl("sm")} &nbsp; 2. (Josefina) estoy ocupad{wl("sm")} &nbsp; 3. (María) estoy nervios{wl("sm")} &nbsp; 4. (un chico) estoy enferm{wl("sm")}</div>')}

  {act(6,"Entrevista a un compañero",[("interactie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Vraag het aan je buur op 3 momenten en noteer het antwoord. Wissel daarna van rol.</p>'
    +f'<div style="margin-left:12.5mm;font-size:9.8pt;line-height:2.5">🌅 — Buenos días, ¿cómo estás? &nbsp;→ {wl("lg")}<br>☀️ — Buenas tardes, ¿qué tal? &nbsp;→ {wl("lg")}<br>🌙 — Buenas noches, ¿cómo estás? &nbsp;→ {wl("lg")}</div>')}

  {act(7,"Escribe tres saludos",[("productie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Schrijf voor elk moment een korte begroeting + hoe je je voelt (2 zinnen elk).</p>'
    +'<div class="wbox" style="margin-left:12.5mm"></div>')}

  {act(8,"Escribe un mensaje",[("productie","skill"),("★★★","")],
    '<p style="margin-left:12.5mm">Schrijf een kort chatbericht (WhatsApp) aan een Spaanstalige vriend(in): groet volgens het uur en zeg hoe je je voelt.</p>'
    +'<div class="wbox" style="margin-left:12.5mm;min-height:28mm"></div>')}

  {act(9,"Saludo relámpago · bliksemgroet",[("productie","skill"),("★★☆","")],
    f'<p style="margin-left:12.5mm">Kijk naar het uur, schrijf de <b>juiste groet</b> én een <b>estado</b> (estar). Snel!</p>'
    +f'<div style="margin-left:12.5mm;font-size:9.8pt;line-height:2.5">07.45 → {wl("lg")}<br>15.30 → {wl("lg")}<br>23.10 → {wl("lg")}<br>12.00 → {wl("lg")}</div>')}
</div>
"""

TAREA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§5 · Tarea final</div><h2>Un día de saludos</h2>
  <div class="esen" style="margin-top:2mm"><b class="tt">Jouw opdracht.</b> Speel met een klasgenoot <b>3 mini-gesprekjes</b>, één per moment van de dag (🌅 mañana · ☀️ tarde · 🌙 noche). Groet gepast, vraag hoe het gaat, zeg met <b>estar</b> hoe je je voelt en neem afscheid. <span class="gloss">Sin leer del papel — zonder van het blad af te lezen.</span></div>
  <div class="regla" style="margin-top:4mm"><span class="tag">Prepárate · vul eerst de frames in (jouw versie)</span>
    <div style="margin-top:2mm;font-size:9.7pt;line-height:2.4">🌅 Buenos días, ¿qué tal? — Estoy {wl('sm')} , ¿y tú? &nbsp; Despedida: {wl('sm')}<br>☀️ Buenas tardes, ¿cómo estás? — Estoy {wl('sm')} . &nbsp; Despedida: {wl('sm')}<br>🌙 Buenas noches, ¿cómo estás? — Estoy {wl('sm')} . &nbsp; Despedida: {wl('sm')}</div>
  </div>
  <div style="margin-top:4mm"><div class="se">Mi diario de saludos · noteer je gesprekjes tijdens het spelen</div>
    <table class="wtab" style="margin-top:2mm"><thead><tr><th style="width:26mm">Momento</th><th>Saludo + pregunta</th><th>Estoy… (estado)</th><th style="width:30mm">Despedida</th></tr></thead>
      <tr><td style="height:15mm">🌅 mañana</td><td></td><td></td><td></td></tr>
      <tr><td style="height:15mm">☀️ tarde</td><td></td><td></td><td></td></tr>
      <tr><td style="height:15mm">🌙 noche</td><td></td><td></td><td></td></tr>
      <tr><td style="height:15mm">🔄 libre</td><td></td><td></td><td></td></tr></table>
  </div>
  <div class="regla" style="margin-top:4mm"><span class="tag">Palabras y frases útiles</span>
    <p style="margin:1mm 0 0;font-size:9.6pt">Buenos días · Buenas tardes · Buenas noches · ¿Qué tal? · ¿Cómo estás? · Estoy bien / cansado-a / ocupado-a / nervioso-a · Regular · ¿Y tú? · Gracias · Adiós · Hasta luego · Hasta mañana</p>
  </div>
  <div class="modelo" style="margin-top:4mm"><b>Modelo · zo klinkt het (por la mañana):</b><br>
    — ¡Buenos días! ¿Qué tal? &nbsp; — Buenos días. Estoy bien, ¿y tú?<br>
    — Regular, estoy un poco cansado. &nbsp; — Vaya. ¡Hasta luego!</div>
  <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div class="truc" style="margin:0"><b>🏁 Klaar als…</b> je op elk moment de <b>juiste</b> groet kiest (días/tardes/noches), met <b>estar</b> zegt hoe je je voelt (juiste -o/-a) en netjes afscheid neemt — zónder af te lezen.</div>
    <table class="rubric"><thead><tr><th>Evaluatie</th><th style="text-align:center">🟢🟡🔴</th></tr></thead>
      <tr><td>Juiste groet per moment</td><td></td></tr>
      <tr><td>estar + estado correct</td><td></td></tr>
      <tr><td>Uitspraak & durf</td><td></td></tr></table>
  </div>
  <p style="font-size:9pt;color:var(--mut);margin-top:3mm">Reflexión · <b>¿Qué me costó?</b> Wat vond je moeilijk? {wl('lg')}</p>
</div>
"""

BANDAS=[("Rosalía","La Perla","🇪🇸 flamenco+pop"),("Luis Fonsi","Despacito","🇵🇷 pop latino"),("Manu Chao","Me gustas tú","🌎 mestizo"),
 ("Aitana","6 de febrero","🇪🇸 pop"),("Karol G","TQG","🇨🇴 reggaetón"),("Quevedo","Bzrp #52","🇪🇸 urban")]
def banda(a,s,g): return f'<div class="banda"><div class="ar">{a}</div><div class="sg">🎵 {s}</div><div class="ge">{g}</div></div>'
MUSICA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Cultura · Banda sonora</div><h2>Saludos &amp; música en español</h2>
  <p style="font-size:9.6pt">In de Spaanstalige wereld groet je warm: een <b>«¡Buenos días!»</b>, vaak met <b>dos besos</b> (twee kussen) of een <b>abrazo</b>. Elke unit heeft ook een <b>banda sonora</b>. Voor deze les schittert <b>«La Perla»</b> van <b>Rosalía</b> (nr. 1 in Spanje).</p>
  <div class="bandas">{"".join(banda(*b) for b in BANDAS)}</div>
  <div class="musrow">
    <div class="call"><span class="ic">🎧</span><div><b>Spotify · la playlist de la clase.</b> Scan en luister. Op de digitale pagina vind je ook <b>LyricsTraining</b> (vul de tekst aan terwijl je luistert) en de video's.</div></div>
    <div class="qr"><div class="lab">Playlist</div>{qr(SPOTIFY)}<div class="meta">Spotify</div></div>
  </div>

  <div class="truc" style="margin-top:5mm"><b>Los saludos por el mundo hispano.</b> Weet je het? Verbind (gis gerust):
    <table class="mtab" style="margin-top:1mm"><tr><td class="a">Entre amigos/familia (España)…</td><td>{wl('sm')}</td><td class="b">a. un apretón de manos (formeel)</td></tr>
    <tr><td class="a">En una situación formal…</td><td>{wl('sm')}</td><td class="b">b. dos besos (una mejilla y otra)</td></tr>
    <tr><td class="a">En muchos países de Latinoamérica…</td><td>{wl('sm')}</td><td class="b">c. a veces un solo beso o un abrazo</td></tr></table>
    <p style="font-size:8.6pt;color:var(--mut);margin-top:1mm">💡 Un <b>saludo</b> zegt veel over een cultuur: warm, dichtbij, met contact. In Vlaanderen geef je vaak één kus of een hand — in Spanje meestal <b>dos besos</b>.</p>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div><div class="se">¿De qué país? · verbind</div>
      <table class="mtab"><tr><td class="a">Rosalía</td><td>{wl('sm')}</td><td class="b">a. Puerto Rico</td></tr>
      <tr><td class="a">Luis Fonsi</td><td>{wl('sm')}</td><td class="b">b. Colombia</td></tr>
      <tr><td class="a">Karol G</td><td>{wl('sm')}</td><td class="b">c. España</td></tr></table>
    </div>
    <div class="truc" style="margin:0"><b>Escucha y responde.</b> Kies één nummer van de playlist.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.3">Mi canción: {wl('lg')}<br>Una palabra que reconozco: {wl('lg')}</div>
    </div>
  </div>
</div>
"""

REPASO=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Repaso · Lo esencial de un vistazo</div><h2>Wat je nu kunt</h2>
  <div class="fams">
    <div class="pcard"><div class="t">Zo groet je volgens het uur</div><div class="ej">🌅 <b>Buenos días</b> · ☀️ <b>Buenas tardes</b> · 🌙 <b>Buenas noches</b></div><div class="t2">Afscheid: Adiós · Hasta luego · Hasta mañana · ¡Nos vemos!</div></div>
    <div class="pcard"><div class="t">Zo zeg je hoe het gaat</div><div class="ej">¿Cómo <b>estás</b>? → <b>Estoy</b> bien / cansad_ / ocupad_ / nervios_.</div><div class="anchor"><b>estar</b>: estoy · estás · está &nbsp; | &nbsp; <b>-o</b> = ♂ · <b>-a</b> = ♀</div></div>
  </div>
  <div class="regla" style="margin:4mm 0"><span class="tag">Frases para la clase</span>
    <div class="cogn" style="margin-top:1mm"><span>¿Cómo se dice… ?</span><span>¿Qué significa… ?</span><span>Otra vez, por favor</span><span>No entiendo</span><span>¿Puedes repetir?</span><span>Más despacio, por favor</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Handige klaszinnen — gebruik ze in het Spaans i.p.v. Nederlands.</span>
  </div>
  <table class="sem"><thead><tr><th style="text-align:left">Puedo… · Ik kan…</th><th>🟢</th><th>🟡</th><th>🔴</th></tr></thead>
    <tr><td>groeten volgens het moment van de dag</td><td></td><td></td><td></td></tr>
    <tr><td>vragen en zeggen hoe het gaat (estar)</td><td></td><td></td><td></td></tr>
    <tr><td>afscheid nemen</td><td></td><td></td><td></td></tr>
    <tr><td>-o/-a en tú/usted juist kiezen</td><td></td><td></td><td></td></tr></table>
  <div class="regla" style="margin-top:5mm"><span class="tag">Mini-test · recuerda sin mirar</span>
    <p style="margin:1mm 0 0;font-size:9.4pt">Sluit de cursus en vertaal uit het hoofd (ophalen = het beste leren).</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:4mm 8mm;margin-top:2mm;font-size:9.8pt;line-height:2.4">
      <div>1. goedemorgen → {wl('')}</div><div>2. hoe gaat het? → {wl('')}</div>
      <div>3. ik ben moe → {wl('')}</div><div>4. ik heb het druk → {wl('')}</div>
      <div>5. goedenavond → {wl('')}</div><div>6. tot morgen → {wl('')}</div>
      <div>7. gaat wel → {wl('')}</div><div>8. ik ben ziek → {wl('')}</div>
    </div>
  </div>
  <div class="guide"><span class="ic">🎮</span><div><span class="hand">Repasa jugando</span><div class="g">Oefen alles online met spelletjes, flashcards en audio op de digitale hub (scan de QR bij §1).</div></div></div>
  <div class="bridge"><b>Próxima parada →</b> In de volgende unit zeg je uit welk land je komt en welke talen je spreekt: <i>nacionalidades y países</i>. ¡Hasta pronto!</div>
</div>
"""

EDITBAR="""
<div class="editbar" id="eb">
  <b>✏️ C4 · U2</b>
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
document.getElementById('btnsave').onclick=function(){var html='<!doctype html>'+document.documentElement.outerHTML;var b=new Blob([html],{type:'text/html'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='C4_U2_Saludos_bewerkt.html';a.click();};
</script>
"""

HTML=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 2 · Saludos</title><style>{CSS}</style></head><body>
{EDITBAR}
{HERO}{ESCUCHA}{COMPR_SEC}{KIT}{GRAM}{PRAC}{TAREA}{MUSICA}{FUNCIONES_SEC}{REPASO}
{SCRIPT}
</body></html>"""
os.makedirs(f"{ROOT}/03-build/web/print",exist_ok=True)
open(f"{ROOT}/03-build/web/print/C4_U2.html","w",encoding="utf-8").write(HTML)
print("C4_U2.html (print+editable) geschreven:",len(HTML),"bytes")
