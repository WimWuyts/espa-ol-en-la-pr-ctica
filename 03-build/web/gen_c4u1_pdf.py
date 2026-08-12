#!/usr/bin/env python3
# C4 · Unidad 1 — PRINT (HTML=bron → PDF via Chromium). Golden-sample print-kit, C4-rood.
# Bevat: hero-bleed p1, secties op nieuwe pagina, ANTWOORDRUIMTE (schrijflijnen/-vlakken/-kolommen),
# QR naar de HTML-hub (eigen encoder, qr_codigo.py), én een bewerkbare laag (editbar: bewerken / opslaan als PDF / bewaar).
import base64, os, re, io, sys
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
from funciones_print import print_section
FUNCIONES_SEC=print_section(1)
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w,fam=None):
    return f"@font-face{{font-family:'{fam or f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),
 face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Bricolage Grotesque XBold","BricolageGrotesque-800.woff2","800","Bricolage Grotesque XBold"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])
PRINTCSS=open(f"{ROOT}/02-huisstijl/templates/cursus-print.css").read()
# Het bladspiegel-blok uit de gedeelde kit hoort NIET in C4, en dat is geen
# uitzondering-om-de-uitzondering. Dat blok is geschreven voor C5 en C6+, waar
# `.sec` het kópblok van een sectie is en de inhoud eronder als broer volgt. In
# C4 is `.sec` de héle bladzijde (`<div class="page sec">`), en dan doen
# dezelfde regels het omgekeerde van wat ze moeten doen: break-inside:avoid op
# een blok van een volle bladzijde duwt dat blok vooruit en laat een blanco
# blad achter. Gemeten toen het er wél in stond: C4 U1 ging van elf naar twaalf
# bladzijden, met blad 4 op 1 % vulling.
#
# C4 houdt bewust zijn eigen bladspiegelregel (CLAUDE.md §3): elke sectie opent
# een blad en is verrijkt tot ze dat blad vult. De meting geeft die regel
# gelijk — 88 tot 94 % vulling, nul halflege bladzijden — dus ze blijft.
PRINTCSS=re.sub(r"/\* @bladspiegel:ini.*?@bladspiegel:fin \*/", "", PRINTCSS, flags=re.S)

def qr(data):
    """Een echte QR-code, met onze eigen encoder.

    Niet met `segno`: PyPI is in deze bouwomgeving geblokkeerd, dus die
    bibliotheek is er niet en zal er niet komen. `qr_codigo.py` is daarom in
    huis geschreven (ISO/IEC 18004, byte-modus) en is dezelfde encoder die C5
    en C6+ gebruiken — één soort code in de hele cursus.

    Niveau Q: een schoolboek krijgt vouwen, vingers en kopieerstreepjes te
    verduren, en op Q blijft een code leesbaar tot ongeveer een kwart van het
    oppervlak beschadigd is.
    """
    from qr_codigo import qr_svg
    return qr_svg(data, mm=26, nivel="Q", color="#A8323B")
# Het adres van de hub van deze unit komt uit `enlaces.py`, net als bij C5/C6+ —
# één plaats voor alle verwijzingen, zodat boek en site niet uit elkaar lopen.
import enlaces as EN
HUB_URL=EN.url("C4", 1)
import comprension_print
COMPR_SEC=comprension_print.print_section(1, HUB_URL)
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
      f'<table class="ktab"><thead><tr><th>Español</th><th>Nederlands</th><th>🔊 repite</th></tr></thead><tbody>{rows}</tbody></table></div>')

def wl(cls=""): return f'<span class="wl {cls}"></span>'
def numlines(n,cls="full"):
    return '<ol class="nl">'+"".join(f'<li>{wl(cls)}</li>' for _ in range(n))+'</ol>'

CSS=FONTS+PRINTCSS+r"""
/* C4-rood override */
:root{ --g:#D64550; --gd:#A8323B; --gt:#FBEAEC; }
/* De Nederlandse steun is steun, geen tweede cursus: kleiner en dichter dan de
   Spaanse regel erboven. Relatief (em), zodat een tabel met een kleinere letter
   niet ineens een grotere gloss krijgt. */
.gloss{ font-size:.9em; line-height:1.32; }
/* functionele kleursemantiek */
.p{color:#2563EB;font-weight:700}.v{color:#EA7317;font-weight:700}
/* Escucha transcript (print) */
.tl{display:flex;gap:3mm;padding:1mm 0;font-size:9.6pt;break-inside:avoid}
.tl .sp{font-family:var(--disp);font-weight:700;color:var(--gd);width:22mm;flex:none}
.tl .tx b{background:var(--gt);border-radius:3pt;padding:.2mm 1.2mm;font-weight:700}
.twocol{column-count:2;column-gap:8mm}
/* Kit tabellen */
.kitwrap{display:grid;grid-template-columns:1fr 1fr;gap:3mm 5mm;margin-top:2mm}
.kit{break-inside:avoid}
.kit-h{font-family:var(--disp);font-weight:700;font-size:9.6pt;color:var(--gd);margin:.6mm 0 .4mm}
.ktab{font-size:8.8pt;width:100%}.ktab th{background:var(--gt);color:var(--gd);font-size:7.2pt;text-transform:uppercase;padding:.8mm 2mm;text-align:left}
.ktab td{border-bottom:1px solid var(--line);padding:.42mm 2mm}.k-es{font-weight:600}.k-ck{text-align:center;width:12mm}
.chk{display:inline-block;width:3.4mm;height:3.4mm;border:1.3px solid var(--mut);border-radius:1.5pt;vertical-align:middle}
/* grammatica mini */
.gt2{width:100%;font-size:9.2pt;margin:2mm 0}.gt2 td{border-bottom:1px solid var(--line);padding:1.5mm 2.5mm}
.gt2 .p{color:#2563EB}.gt2 .v{color:#EA7317;font-family:var(--disp)}.gt2 .ex{color:var(--mut);font-style:italic}
.mv2{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin:2mm 0}
.mv2 div{border-radius:8pt;padding:2.5mm 4mm;font-family:var(--disp)}
.mv2 .m{background:#E8F0FE;color:#1E40AF}.mv2 .f{background:#FCE7F0;color:#9D174D}
/* woordenbank bij een oefening: de woorden die je mag gebruiken */
.bancopal{display:inline-block;margin-top:1mm;font-size:9pt;font-weight:600;color:var(--gd);background:var(--gt);border-radius:6pt;padding:1mm 3mm}
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
/* U1 heeft twee volle secties (de frases de supervivencia en de leespagina).
   Met de Spaanse instructie erbij liepen ze een paar millimeter over hun blad;
   dit haalt ze terug binnen zonder aan de inhoud te raken. */
.ktab{ font-size:8.5pt; }
.ktab td{ padding:.35mm 2mm; }
.chk{ width:3mm; height:3mm; }
.vc{ padding:2mm; }
.kitwrap{ gap:2mm 5mm; margin-top:1mm; }
.klemline{ margin-top:1.5mm; font-size:9.6pt; }
.ktab th{ padding:.6mm 2mm; }
.ktab td{ padding:.28mm 2mm; }
.vc .vl{ font-size:18pt; }
.tl{ padding:.6mm 0; }
.twocol .tl{ padding:.25mm 0; }
.vf td{ padding:1.45mm 2mm; }
.cogn span{ font-size:8.6pt; padding:.6mm 2.4mm; }
.regla{ padding:2.5mm 4mm; }
.audiorow{ margin:2mm 0; }
.vf td{ padding:1.7mm 2mm; }
"""

# ── content ──────────────────────────────────────────────────────────────────
HERO=f"""
<section class="hero">
  <div class="tab">C4 · LA RUTA</div>
  <div class="eyebrow">EL DESPEGUE · PARADA 1 · SURVIVAL IN SPANISH</div>
  <h1>Presentaciones</h1>
  <div class="sub">Tus primeras palabras en español: <b>saludar</b>, <b>presentarte</b> y <b>despedirte</b>. <span class="gloss">Je allereerste Spaans: groeten, jezelf voorstellen en afscheid nemen — alles wat je hoort, gebruik je meteen.</span></div>
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
  <div class="guide"><span class="ic">🎒</span><div><span class="hand">¡Vamos! Empieza el viaje.</span><div class="g">En esta lección de supervivencia aprendes el español que necesitas enseguida: escucha, repite y pruébalo tú. <span class="gloss">In deze «survival»-les leer je de taal die je meteen nodig hebt: luisteren, nazeggen, zelf proberen.</span></div></div></div>

  <div class="se" style="margin-top:6mm">La gente de la ruta</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Viajas con cuatro jóvenes del mundo hispano. Los conoces por el camino. <span class="gloss">Je reist mee met vier jongeren uit de Spaanstalige wereld; onderweg leer je hen kennen.</span></p>
  <div class="cast2">
    <div class="m"><div class="fl">🇪🇸</div><div class="nm">Lucía</div><div class="ro">Sevilla · la familia</div></div>
    <div class="m"><div class="fl">🇲🇽</div><div class="nm">Diego</div><div class="ro">Ciudad de México · la comida</div></div>
    <div class="m"><div class="fl">🇨🇴</div><div class="nm">Valen</div><div class="ro">Cartagena · la casa</div></div>
    <div class="m"><div class="fl">🇵🇪</div><div class="nm">Nina</div><div class="ro">Cusco · los viajes</div></div>
    <div class="m"><div class="fl">🎒</div><div class="nm">Tú</div><div class="ro">el viajero · jij</div></div>
  </div>

  <div class="truc" style="margin-top:5mm"><b>¿Qué reconoces ya?</b> Ya entiendes mucho español: estas palabras se parecen al neerlandés o al inglés (<i>palabras transparentes</i>). <span class="gloss">Je begrijpt nu al véél Spaans — deze woorden lijken op het Nederlands of Engels.</span>
    <div class="cogn"><span>la familia</span><span>la música</span><span>el teléfono</span><span>el restaurante</span><span>el profesor</span><span>el hospital</span><span>el chocolate</span><span>el animal</span><span>la información</span><span>el problema</span><span>importante</span><span>diferente</span></div>
    <span style="font-size:8.6pt"><b>Consejo:</b> atrévete a adivinar — el español se parece más de lo que crees. <span class="gloss">Durf te gissen: Spaans lijkt vaker op wat je al kent dan je denkt.</span></span>
  </div>
</div>
"""

ESCUCHA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§1 · ¡Escucha!</div><h2>Mira la escena y lee a la vez <span class="gloss" style="font-size:10pt;font-weight:400">bekijk de scène en lees mee</span></h2>
  <div class="audiorow">
    <div class="call"><span class="ic">🎬</span><div><b>Sitcom · Episodio 1.</b> Escanea el código y mira el episodio en la página digital. Escucha primero <b>sin leer</b>; después lee a la vez. Las palabras en <b>negrita</b> son chunks para llevarte. <span class="gloss">Eerst zónder te lezen, daarna lees je mee.</span></div></div>
    <div class="qr" data-url="{EN.url('C4', 1, EN.ancla_c4('escucha'))}"><div class="lab">Vídeo online</div>{qr(EN.url("C4", 1, EN.ancla_c4("escucha")))}<div class="meta">hub · Escucha</div></div>
  </div>
  <div class="truc"><b>Antes de escuchar.</b> Mira la escena <b>sin sonido</b>. ¿Qué piensas? Adivina. <span class="gloss">Bekijk eerst zónder geluid — gis gerust.</span>
    <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.2">¿Dónde están? {wl('lg')}<br>¿Cuántas personas hablan? {wl('sm')}</div>
  </div>
  <div class="twocol">{scenehtml(*SCENES[0])}{scenehtml(*SCENES[1])}</div>
  <div class="ojo"><b>¡Ojo!</b> <b>Encantado</b> (un chico) / <b>Encantada</b> (una chica). Para decir tu nombre tienes <b>tres</b> formas: <i>Me llamo</i> Ana · <i>Yo soy</i> Ana · <i>Mi nombre es</i> Ana. <span class="gloss">Jongen ↔ meisje; je naam zeggen kan op drie manieren.</span></div>

  <div class="se" style="margin-top:5mm">Después de escuchar · ¿verdadero o falso?</div>
  <p style="font-size:9.4pt;margin:0 0 1mm"><b>Marca V o F. Corrige las frases falsas en la línea.</b> <span class="gloss">Kruis aan; verbeter de valse op de lijn.</span></p>
  <table class="vf">
    <tr><td>1. María es la nueva profesora.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>2. Julio se llama Fernando.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>3. Josefina es la secretaria.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>4. María dice «muchas gracias».</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
  </table>
</div>
"""

VOC=[("a","als in ‘bal’","casa"),("e","als in ‘bed’","mesa"),("i","als in ‘kiwi’","sí"),("o","als in ‘pot’","hola"),("u","als in ‘boek’","tú")]
def vc(l,a,e): return f'<div class="vc"><div class="vl">{l}</div><span class="vas">{a}</span><span class="vej">{e}</span></div>'
KIT=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Suena bien · pronunciación</div><h2>Las cinco vocales y la sílaba tónica</h2>
  <p style="font-size:9.4pt;margin:0 0 1mm">Las vocales españolas son <b>cortas y puras</b>: siempre suenan igual. Practícalas en la página digital: escucha y repite. <span class="gloss">Kort en zuiver, altijd dezelfde klank. Oefen online: luister en zeg na.</span></p>
  <div class="vrow">{"".join(vc(*v) for v in VOC)}</div>
  <div class="ojo"><b>¡Ojo!</b> La <b>e</b> es siempre /e/ y la <b>o</b> siempre /o/: en español no hay diptongo. <span class="gloss">Géén «ei/ou»-glijder: a·e·i·o·oe.</span></div>
  <div class="klemline"><b>La sílaba tónica</b> — ¿dónde está el acento? Escucha y subraya <span class="gloss">(waar ligt de klemtoon?)</span>: <span class="t">HO</span>·la · me·<span class="t">LLA</span>·mo · en·can·<span class="t">TA</span>·do · a·<span class="t">DIÓS</span> · <span class="t">GRA</span>·cias</div>

  <div class="se" style="margin-top:3mm">§2 · Frases de supervivencia</div><h2>El español que necesitas hoy</h2>
  <p style="font-size:9.4pt;margin:0 0 2mm">Marca ☐ cuando puedas <b>repetir</b> la expresión con soltura. Practícalas con audio en la página digital. <span class="gloss">Vink af zodra je ze vlot kunt <b>nazeggen</b>.</span></p>
  <div class="kitwrap">{"".join(kittable(n,it) for n,it in CLUSTERS)}</div>
</div>
"""

GRAM=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§4 · Gramática en la práctica</div><h2>Corta y funcional <span class="gloss" style="font-size:10pt;font-weight:400">alleen wat je vandaag nodig hebt</span></h2>
  <div class="modelo"><b>🔎 Fíjate · vuelve a la escena.</b> Ya lo has oído: «<b>Yo soy</b> Julio.» · «<b>Me llamo</b> María.» · «Encantad<b>o</b> / Encantad<b>a</b>.» Descubre tú el patrón en los cuadros de abajo: <i>primero el significado, después la regla</i>. <span class="gloss">Eerst betekenis, dan de regel.</span></div>
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
  <div class="regla"><span class="tag">-o / -a · un chico o una chica</span>
    <div class="mv2"><div class="m">♂ Un chico: encantad<b>o</b> · bienvenid<b>o</b></div><div class="f">♀ Una chica: encantad<b>a</b> · bienvenid<b>a</b></div></div>
    <p style="font-size:9pt;margin:1mm 0 0">Elige la forma que va contigo. <span class="gloss">Kies de vorm die bij jou past.</span></p>
  </div>
  <div class="regla"><span class="tag">tú ↔ usted</span>
    <p style="margin:1mm 0 0;font-size:9.6pt">Con amigos y compañeros: <b>tú</b> — <span class="ex" style="color:var(--mut)">¿Cómo estás? · ¿Cómo te llamas?</span><br>Con una persona adulta que no conoces: <b>usted</b> — <span class="ex" style="color:var(--mut)">¿Cómo está usted? · ¿Cómo se llama?</span><br><span class="gloss">tú = vrienden · usted = beleefd.</span></p>
  </div>
  <div class="truc"><b>Mini-ejercicio 1 · Completa con <i>ser</i> o <i>llamarse</i>.</b> <span class="gloss">Vul aan met de juiste vorm van ser of llamarse.</span>
    <div style="margin-top:2mm;font-size:9.6pt;line-height:2.4">1. Yo {wl('sm')} de Bélgica. &nbsp;&nbsp; 2. ¿Cómo {wl('sm')} llamas? &nbsp;&nbsp; 3. Me {wl('sm')} ____. &nbsp;&nbsp; 4. Ella {wl('sm')} profesora. &nbsp;&nbsp; 5. ¿{wl('sm')} tú Leo? &nbsp;&nbsp; 6. Él {wl('sm')} llama Pablo.</div>
  </div>
  <div class="truc"><b>Mini-ejercicio 2 · ¿tú o usted?</b> Elige y escribe la pregunta correcta. <span class="gloss">Kies en schrijf de juiste vraag.</span>
    <div style="margin-top:2mm;font-size:9.6pt;line-height:2.4">a) a un compañero de clase → {wl('lg')}<br>b) al director del instituto → {wl('lg')}</div>
  </div>
</div>
"""

def act(n,title,badges,body):
    bh="".join(f'<span class="badge {c}">{t}</span>' for t,c in badges)
    return (f'<div class="act"><div class="acthead"><div class="anum">{n}</div><div><div class="h">{title}</div>'
            f'<div class="badges">{bh}</div></div></div>{body}</div>')

PRAC=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§3 · Práctica</div><h2>Practica en papel <span class="gloss" style="font-size:10pt;font-weight:400">— online verbeter je alles</span></h2>

  {act(1,"Clasifica las expresiones",[("reconocer · herkennen","skill"),("5 min","")],
    '<p style="margin-left:12.5mm">Escribe cada expresión en la columna correcta. Añade abajo una palabra tuya. <span class="gloss">In de juiste kolom; voeg één eigen woord toe.</span><br><span class="bancopal">Hola · Adiós · Gracias · ¿Cómo te llamas? · Hasta luego · De nada · Buenos días · Encantado</span></p>'
    +'<div class="wcols" style="margin-left:12.5mm"><div class="wcol"><h4>Saludar</h4><div class="fill"></div></div><div class="wcol"><h4>Preguntar</h4><div class="fill"></div></div><div class="wcol"><h4>Cortesía</h4><div class="fill"></div></div><div class="wcol"><h4>Despedirse</h4><div class="fill"></div></div></div>')}

  {act(2,"Relaciona · verbind",[("con apoyo · met steun","skill"),("★☆☆","")],
    '<p style="margin-left:12.5mm">Une con una línea el español y su significado. <span class="gloss">Une con una línea el español y su significado. <span class="gloss">verbind Spaans en betekenis</span></span></p>'
    +'<table class="mtab" style="margin-left:12.5mm"><tr><td class="a">1. ¡Hola!</td><td><span class="ln"></span></td><td class="b">a. graag gedaan</td></tr>'
    +'<tr><td class="a">2. ¿Cómo te llamas?</td><td><span class="ln"></span></td><td class="b">b. tot straks</td></tr>'
    +'<tr><td class="a">3. De nada</td><td><span class="ln"></span></td><td class="b">c. hallo</td></tr>'
    +'<tr><td class="a">4. Hasta luego</td><td><span class="ln"></span></td><td class="b">d. aangenaam</td></tr>'
    +'<tr><td class="a">5. Encantada</td><td><span class="ln"></span></td><td class="b">e. hoe heet je?</td></tr></table>')}

  {act(3,"Completa el diálogo",[("con apoyo · met steun","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Completa el diálogo. <span class="gloss">Vul het gesprek aan.</span></p>'
    +f'<div style="margin-left:12.5mm;font-size:10pt;line-height:2.5">'
    +f'— ¡Hola! ¿Cómo {wl("sm")} llamas?<br>— Me {wl("sm")} Ana. ¿Y {wl("sm")}?<br>— Yo {wl("sm")} Leo. {wl("sm")} de Madrid.<br>— ¡{wl("sm")}! Hasta {wl("sm")}.</div>')}

  {act(4,"Ordena la conversación",[("con apoyo · met steun","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Numera las frases en el orden correcto (1–5). <span class="gloss">Nummer de zinnen in de juiste volgorde.</span></p>'
    +'<div class="scramble" style="margin-left:12.5mm"><span>___ Yo soy Leo. Encantado.</span><span>___ ¡Hola! ¿Cómo te llamas?</span><span>___ ¡Hasta luego!</span><span>___ Me llamo Ana. ¿Y tú?</span><span>___ Igualmente. ¡Adiós!</span></div>')}

  {act(5,"¿-o o -a?",[("con apoyo · met steun","skill"),("★☆☆","")],
    f'<p style="margin-left:12.5mm">Escribe la letra correcta (♂ -o / ♀ -a). <span class="gloss">Vul de juiste letter in.</span></p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. (chico) Encantad{wl("sm")} &nbsp; 2. (chica) Encantad{wl("sm")} &nbsp; 3. (chica) Bienvenid{wl("sm")} &nbsp; 4. (chico) Bienvenid{wl("sm")}</div>')}

  {act(6,"Entrevista a un compañero",[("en parejas · per twee","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Pregunta a tu compañero/a y anota su respuesta. Después cambiad de papel. <span class="gloss">Vraag het aan je buur en wissel van rol.</span></p>'
    +f'<div style="margin-left:12.5mm;font-size:9.8pt;line-height:2.5">— ¿Cómo te llamas? &nbsp;→ {wl("lg")}<br>— ¿De dónde eres? &nbsp;→ {wl("lg")}<br>— ¿Qué tal? &nbsp;→ {wl("lg")}</div>')}

  {act(7,"Preséntate por escrito",[("producir · zelf schrijven","skill"),("★★★","")],
    '<p style="margin-left:12.5mm">Preséntate en 3–4 frases: saludo, nombre, origen y despedida. Usa las frases de supervivencia. <span class="gloss">3–4 zinnen: groet, naam, herkomst, afscheid.</span></p>'
    +'<div class="wbox" style="margin-left:12.5mm"></div>')}

  {act(8,"Escribe un mensaje",[("producir · zelf schrijven","skill"),("★★★","")],
    '<p style="margin-left:12.5mm">Escribe un mensaje corto (WhatsApp) para presentarte a un amigo o una amiga nueva. <span class="gloss">Kort chatbericht aan een nieuwe Spaanstalige vriend(in).</span></p>'
    +'<div class="wbox" style="margin-left:12.5mm;min-height:28mm"></div>')}
</div>
"""

TAREA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§5 · Tarea final</div><h2>El carné de la clase</h2>
  <div class="esen" style="margin-top:2mm"><b class="tt">Tu tarea.</b> Haz tu carné de clase y preséntate a <b>3 compañeros</b>. Pregúntales su nombre y de dónde son, y anótalo. <b>Sin leer del papel.</b> <span class="gloss">Kaartje maken, jezelf voorstellen aan drie klasgenoten, naam en herkomst noteren.</span></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div>
      <div class="regla" style="margin:0"><span class="tag">Mi carné</span>
        <table class="wtab" style="margin-top:3mm"><tr><td style="width:32mm">Me llamo</td><td></td></tr><tr><td>Soy de</td><td></td></tr><tr><td>Mi emoji / dibujo</td><td></td></tr></table>
      </div>
      <div class="truc" style="margin-top:2mm"><b>Ejercicio · Escribe y ensaya tu presentación.</b>
        <span class="gloss">Schrijf ze en zeg ze daarna zónder te kijken.</span>
        <div style="margin-top:1mm;font-size:9.6pt;line-height:2.3">
          ¡Hola! Me llamo {wl('sm')} . Soy de {wl('sm')} . ¡Encantad{wl('sm')}!<br>
          <span class="chk"></span> Lo digo <b>sin mirar</b> el papel.</div></div>
    </div>
    <div>
      <div class="se">3 compañeros</div>
      <table class="wtab"><thead><tr><th>#</th><th>¿Cómo te llamas?</th><th>¿De dónde eres?</th></tr></thead>
      <tr><td style="width:8mm;text-align:center;height:11mm">1</td><td></td><td></td></tr>
      <tr><td style="text-align:center;height:11mm">2</td><td></td><td></td></tr>
      <tr><td style="text-align:center;height:11mm">3</td><td></td><td></td></tr>
      <tr><td style="text-align:center;height:11mm">4</td><td></td><td></td></tr></table>
    </div>
  </div>
  <div style="margin-top:4mm"><div class="se">Dibuja tu carné <span class="gloss">— foto of emoji, en versier het</span></div>
    <div class="wbox" style="min-height:15mm"></div></div>
  <div class="regla" style="margin-top:4mm"><span class="tag">Palabras y frases útiles</span>
    <p style="margin:1mm 0 0;font-size:9.6pt">¡Hola! · Buenos días · Me llamo… · Soy de… · Encantado/a · ¿Y tú? · ¿Cómo te llamas? · ¿De dónde eres? · Igualmente · Mucho gusto · Adiós · ¡Hasta luego!</p>
  </div>
  <div class="modelo" style="margin-top:4mm"><b>Modelo · así suena.</b> <span class="gloss">zo klinkt het</span><br>
    — ¡Hola! Me llamo Sara. Soy de Amberes. ¡Encantada! ¿Y tú, cómo te llamas?<br>
    — Yo soy Tom. Soy de Gante. Igualmente. ¡Hasta luego!</div>
  <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div class="truc" style="margin:0"><b>🏁 Está listo cuando…</b> te presentas con soltura sin leer, usas la forma correcta (-o/-a) y tienes tres nombres anotados. <span class="gloss">Vlot, zónder af te lezen, juiste vorm, drie namen.</span></div>
    <table class="rubric"><thead><tr><th>¿Cómo ha ido? <span class="gloss">evaluatie</span></th><th style="text-align:center">🟢🟡🔴</th></tr></thead>
      <tr><td>Tarea completa <span class="gloss">opdracht volbracht</span></td><td></td></tr>
      <tr><td>Frases correctas <span class="gloss">juiste uitdrukkingen</span></td><td></td></tr>
      <tr><td>Pronunciación y atrevimiento <span class="gloss">uitspraak &amp; durf</span></td><td></td></tr></table>
  </div>
  <p style="font-size:9pt;margin-top:3mm">Reflexión · <b>¿Qué me ha costado más?</b> <span class="gloss">Wat vond je moeilijk?</span> {wl('lg')}</p>
</div>
"""

BANDAS=[("Aitana","Las Babys","pop 🇪🇸"),("Quevedo","Bzrp #52","urban 🇪🇸"),("Manu Chao","Me gustas tú","clásico 🌎"),
 ("Karol G","TQG","reggaetón 🇨🇴"),("Bad Bunny","Tití me preguntó","🇵🇷"),("Rosalía","La Perla","🇪🇸")]
def banda(a,s,g): return f'<div class="banda"><div class="ar">{a}</div><div class="sg">🎵 {s}</div><div class="ge">{g}</div></div>'
MUSICA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Cultura · Banda sonora</div><h2>Aprende español con la música que ya escuchas</h2>
  <p style="font-size:9.6pt">Cada unidad tiene su <b>banda sonora</b>: canciones de artistas que suenan ahora. Escucha, canta y quédate con palabras nuevas. Para esta lección sobre <i>presentarse</i> van bien <b>«Me gustas tú»</b> (Manu Chao) y <b>«Las Babys»</b> (Aitana). <span class="gloss">Elke unit heeft zijn nummers: luister, zing mee, pik woorden op.</span></p>
  <div class="bandas">{"".join(banda(*b) for b in BANDAS)}</div>
  <div class="musrow">
    <div class="call"><span class="ic">🎧</span><div><b>Spotify · la playlist de la clase.</b> Escanea y escucha. En la página digital tienes también <b>LyricsTraining</b> (completa la letra mientras escuchas) y los vídeos. <span class="gloss">Online ook LyricsTraining en de video's.</span></div></div>
    <div class="qr" data-url="{SPOTIFY}"><div class="lab">Playlist</div>{qr(SPOTIFY)}<div class="meta">Spotify</div></div>
  </div>

  <div class="regla" style="margin-top:5mm"><span class="tag">Completa la canción</span>
    <p style="margin:1mm 0 0;font-size:9.7pt">«Me gustas tú» (Manu Chao) repite todo el rato <b>me gusta(n)…</b>. Escucha y escribe lo que oyes. <span class="gloss">Luister en vul in wat je hoort.</span></p>
    <div style="margin-top:2mm;font-size:10pt;line-height:2.4">Me gustan los {wl('')} , me gustas {wl('sm')} .<br>Me gusta la {wl('')} , me gustas {wl('sm')} .</div>
    <p style="font-size:8.6pt;margin-top:1mm">🔎 <i>me gusta</i> = algo me parece bien. <span class="gloss">«Ik vind … leuk / ik hou van …» — een makkelijke chunk om te onthouden.</span></p>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div><div class="se">¿De qué país? · relaciona</div>
      <table class="mtab"><tr><td class="a">Karol G</td><td>{wl('sm')}</td><td class="b">a. España</td></tr>
      <tr><td class="a">Bad Bunny</td><td>{wl('sm')}</td><td class="b">b. Colombia</td></tr>
      <tr><td class="a">Rosalía</td><td>{wl('sm')}</td><td class="b">c. Puerto Rico</td></tr></table>
    </div>
    <div class="truc" style="margin:0"><b>Escucha y responde.</b> Elige una canción de la playlist. <span class="gloss">Kies één nummer uit de playlist.</span>
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.3">Mi canción: {wl('lg')}<br>Una palabra que reconozco: {wl('lg')}</div>
    </div>
  </div>
</div>
"""

REPASO=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Repaso · Lo esencial de un vistazo</div><h2>Lo que ya sabes hacer <span class="gloss" style="font-size:10pt;font-weight:400">wat je nu kunt</span></h2>
  <div class="fams">
    <div class="pcard"><div class="t">Así saludas y te presentas</div><div class="ej">¡Hola! <b>Me llamo</b> ___. <b>Soy de</b> ___. <b>Encantad_</b>. ¿Y tú, <b>cómo te llamas</b>?</div><div class="t2">Despedirse: Adiós · Hasta luego · ¡Nos vemos! <span class="gloss">afscheid nemen</span></div></div>
    <div class="pcard"><div class="t">Recuerda</div><div class="ej"><b>ser</b>: soy · eres · es &nbsp; | &nbsp; <b>llamarse</b>: me/te/se llamo/llamas/llama</div><div class="anchor"><b>-o</b> = ♂ · <b>-a</b> = ♀ &nbsp; | &nbsp; <b>tú</b> = un amigo · <b>usted</b> = formal <span class="gloss">(vriend ↔ beleefd)</span></div></div>
  </div>
  <div class="regla" style="margin:4mm 0"><span class="tag">Frases para la clase</span>
    <div class="cogn" style="margin-top:1mm"><span>¿Cómo se dice… ?</span><span>¿Qué significa… ?</span><span>Otra vez, por favor</span><span>No entiendo</span><span>¿Puedes repetir?</span><span>Más despacio, por favor</span></div>
    <span style="font-size:8.6pt">Úsalas en español, no en neerlandés. <span class="gloss">Handige klaszinnen: gebruik ze in het Spaans in plaats van in het Nederlands.</span></span>
  </div>
  <table class="sem"><thead><tr><th style="text-align:left">Puedo… <span class="gloss">ik kan…</span></th><th>🟢</th><th>🟡</th><th>🔴</th></tr></thead>
    <tr><td>saludar y despedirme <span class="gloss">groeten en afscheid nemen</span></td><td></td><td></td><td></td></tr>
    <tr><td>presentarme (nombre + origen) <span class="gloss">mezelf voorstellen</span></td><td></td><td></td><td></td></tr>
    <tr><td>preguntar el nombre a otra persona <span class="gloss">iemand naar zijn naam vragen</span></td><td></td><td></td><td></td></tr>
    <tr><td>elegir bien -o/-a y tú/usted <span class="gloss">-o/-a en tú/usted juist kiezen</span></td><td></td><td></td><td></td></tr></table>
  <div class="regla" style="margin-top:5mm"><span class="tag">Mini-test · recuerda sin mirar</span>
    <p style="margin:1mm 0 0;font-size:9.4pt">Cierra el libro y traduce de memoria. <span class="gloss">Boek dicht: uit het hoofd vertalen leert het best.</span></p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:4mm 8mm;margin-top:2mm;font-size:9.8pt;line-height:2.4">
      <div>1. hallo → {wl('')}</div><div>2. dank je → {wl('')}</div>
      <div>3. hoe heet je? → {wl('')}</div><div>4. ik kom uit… → {wl('')}</div>
      <div>5. tot straks → {wl('')}</div><div>6. aangenaam (v) → {wl('')}</div>
      <div>7. graag gedaan → {wl('')}</div><div>8. tot morgen → {wl('')}</div>
    </div>
  </div>
  <div class="guide"><span class="ic">🎮</span><div><span class="hand">Repasa jugando</span><div class="g">Practícalo todo en la página digital: juegos, flashcards y audio (escanea el QR del §1). <span class="gloss">Online: spelletjes, flashcards en audio.</span></div></div></div>
  <div class="bridge"><b>Próxima parada →</b> En la próxima unidad pides algo y sobrevives a tu primera conversación en un café. ¡Hasta pronto! <span class="gloss">Volgende unit: iets bestellen in een café.</span></div>
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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 1 · Presentaciones</title><style>{CSS}</style></head><body class="c4">
{EDITBAR}
{HERO}{ESCUCHA}{COMPR_SEC}{KIT}{GRAM}{PRAC}{TAREA}{MUSICA}{FUNCIONES_SEC}{REPASO}
{SCRIPT}
</body></html>"""
os.makedirs(f"{ROOT}/03-build/web/print",exist_ok=True)
open(f"{ROOT}/03-build/web/print/C4_U1.html","w",encoding="utf-8").write(HTML)
print("C4_U1.html (print+editable) geschreven:",len(HTML),"bytes")
