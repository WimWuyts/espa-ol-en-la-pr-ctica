#!/usr/bin/env python3
# C4 · Unidad 3 — PRINT (HTML=bron → PDF via Chromium). Golden-sample print-kit, C4-rood.
# Thema: ¿De dónde eres? · soy de + país · gentilicio m/v · idiomas. Zelfde pijplijn/CSS als U1/U2.
import base64, os, re, io, sys
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
HUB_URL=EN.url("C4", 3)
import comprension_print
COMPR_SEC=comprension_print.print_section(3, HUB_URL)
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
/* De Nederlandse steun is steun, geen tweede cursus: kleiner en dichter dan de
   Spaanse regel erboven. Relatief (em), zodat een tabel met een kleinere letter
   niet ineens een grotere gloss krijgt. */
.gloss{ font-size:.9em; line-height:1.32; }
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
  <div class="sub">La pregunta clave del viaje: <b>¿De dónde eres?</b> Decir de dónde vienes, tu <b>nacionalidad</b> y qué <b>idiomas</b> hablas. <span class="gloss">waar je vandaan komt, je nationaliteit en je talen</span></div>
  <div class="q">¿De dónde eres? ¡Soy de Bélgica!</div>
</section>
<div class="page">
  <div class="obj"><div class="se">Al final de esta unidad <span class="gloss">op het einde van deze les</span></div>
    <ul>
      <li><span class="ck">✓</span> <span><span class="es">Preguntar y decir el origen</span> <span class="nl">— ¿de dónde eres? · soy de + país</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">La nacionalidad (gentilicio)</span> <span class="nl">— mexicano/a · español/a · belga</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Decir qué idiomas hablas</span> <span class="nl">— hablo español / neerlandés / francés</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Situar los <b>21 países</b> del mundo hispano</span> <span class="nl">— op de kaart</span></span></li>
    </ul>
  </div>
  <div class="guide"><span class="ic">🎒</span><div><span class="hand">¡Seguimos la ruta! Parada 3.</span><div class="g">En esta lección de «survival» aprendes la pregunta que abre todo viaje: <b>¿de dónde eres?</b>, y cómo responder con tu país, tu nacionalidad y tus idiomas. ¡Abre el mapa del mundo en la página digital! <span class="gloss">de vraag die elke reis opent</span></div></div></div>

  <div class="se" style="margin-top:6mm">La gente de la ruta · tus compañeros de viaje</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Viajas con cuatro jóvenes del mundo hispano, cada uno de un país y con una <i>nacionalidad</i> distinta. En la escena el director Fernando le enseña la pregunta clave a una viajera. <span class="gloss">elk uit een ander land</span></p>
  <div class="cast2">
    <div class="m"><div class="fl">🇪🇸</div><div class="nm">Lucía</div><div class="ro">española · Sevilla</div></div>
    <div class="m"><div class="fl">🇲🇽</div><div class="nm">Diego</div><div class="ro">mexicano · CDMX</div></div>
    <div class="m"><div class="fl">🇨🇴</div><div class="nm">Valen</div><div class="ro">colombiana · Cartagena</div></div>
    <div class="m"><div class="fl">🇵🇪</div><div class="nm">Nina</div><div class="ro">peruana · Cusco</div></div>
    <div class="m"><div class="fl">🇧🇪</div><div class="nm">Tú</div><div class="ro">belga · de reiziger</div></div>
  </div>

  <div class="truc" style="margin-top:5mm"><b>¿Qué reconoces ya?</b> Estas palabras del mundo se parecen al neerlandés o al inglés (<i>palabras transparentes</i>) — durf te gissen:
    <div class="cogn"><span>internacional</span><span>la nación</span><span>el continente</span><span>la capital</span><span>europeo</span><span>americano</span><span>africano</span><span>el mapa</span><span>la región</span><span>el/la turista</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Tip: veel landen &amp; talen herken je meteen — <b>Italia</b>, <b>Portugal</b>, <b>el inglés</b>, <b>el árabe</b>…</span>
  </div>
</div>
"""

ESCUCHA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§1 · ¡Escucha!</div><h2>Mira la escena y lee al mismo tiempo <span class="gloss" style="font-size:10pt;font-weight:400">bekijk en lees mee</span></h2>
  <div class="audiorow">
    <div class="call"><span class="ic">🎬</span><div><b>Sitcom · Episodio 3 · Nacionalidades y países.</b> Escanea el código y mira el episodio en la página digital. Fernando le enseña a una viajera la pregunta clave <b>¿de dónde eres?</b>, y de paso la trampa «soy Argelia» → «soy <b>de</b> Argelia». Primero escucha sin leer; después lee al mismo tiempo. Las palabras en <b>negrita</b> son chunks para llevarte. <span class="gloss">eerst zónder te lezen, daarna lees je mee</span></div></div>
    <div class="qr" data-url="{EN.url('C4', 3, EN.ancla_c4('escucha'))}"><div class="lab">Vídeo online</div>{qr(EN.url("C4", 3, EN.ancla_c4("escucha")))}<div class="meta">hub · Escucha</div></div>
  </div>
  <div class="truc"><b>Antes de escuchar.</b> ¿Qué países e idiomas crees que vas a oír? <span class="gloss">welke landen en talen, denk je?</span> <span style="font-size:8.8pt;color:var(--mut)">(gis gerust)</span>
    <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.2">Un país: {wl('sm')} &nbsp;&nbsp; Una nacionalidad: {wl('sm')} &nbsp;&nbsp; Un idioma: {wl('sm')}</div>
  </div>
  <div class="twocol">{scenehtml(*SCENES[0])}{scenehtml(*SCENES[1])}{scenehtml(*SCENES[2])}</div>
  <div class="ojo"><b>¡Ojo!</b> La viajera dice «Yo soy Argelia», que significa «yo <i>soy</i> Argelia». Lo correcto es «Yo soy <b>de</b> Argelia». País = con <b>de</b>; nacionalidad = sin <b>de</b>: «soy argelin<b>a</b>». <span class="gloss">land met «de», nationaliteit zonder</span></div>

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

  <div class="se" style="margin-top:3mm">§2 · Kit de supervivencia</div><h2>La lengua que de verdad necesitas <span class="gloss" style="font-size:10pt;font-weight:400">de taal die je écht nodig hebt</span></h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 2mm">Marca ☐ cada vez que puedas <b>repetir</b> una expresión con soltura. Practícalas en línea con audio. <span class="gloss">vink af wat je vlot kunt naspreken</span></p>
  <div class="kitwrap">{"".join(kittable(n,it) for n,it in CLUSTERS)}</div>
</div>
"""

GRAM=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§4 · Gramática en la práctica</div><h2>Corta y funcional <span class="gloss" style="font-size:10pt;font-weight:400">kort en functioneel</span></h2>
  <div class="modelo"><b>🔎 Fíjate · vuelve a la escena.</b> Ya lo has oído: «¿De dónde <b>eres</b>?» → «<b>Soy de</b> Argelia» · «Eres argelin<b>a</b> (chica) · argelin<b>o</b> (chico)» · «<b>Hablo</b> español». Descubre tú el patrón — <i>primero el significado, después la regla.</i> <span class="gloss">ontdek zelf het patroon</span></div>
  <div class="regla"><span class="tag">soy de + país · de dónde eres <span class="gloss">waar je vandaan komt</span></span>
    <table class="gt2"><tr><td class="p">yo</td><td class="v">soy de</td><td>ik kom uit</td><td class="ex"><b>Soy de</b> <span class="pl">Bélgica</span>.</td></tr>
    <tr><td class="p">tú</td><td class="v">eres de</td><td>jij komt uit</td><td class="ex">¿<b>Eres de</b> <span class="pl">España</span>?</td></tr>
    <tr><td class="p">él/ella/usted</td><td class="v">es de</td><td>hij/zij komt · u komt uit</td><td class="ex">María <b>es de</b> <span class="pl">Sevilla</span>.</td></tr></table>
    <p style="font-size:9pt;margin:1mm 0 0">⚠️ Di «soy <b>de</b> Argelia», no «soy Argelia». País = con <b>de</b>; nacionalidad = sin <b>de</b> (soy argelina). <span class="gloss">land met «de», nationaliteit zonder</span></p>
  </div>
  <div class="regla"><span class="tag">El gentilicio · man of vrouw (de nationaliteit)</span>
    <div class="mv2"><div class="m">♂ Un chico: mexican<b>o</b> · colombian<b>o</b> · portugu<b>és</b> · franc<b>és</b> · ingl<b>és</b></div><div class="f">♀ Una chica: mexican<b>a</b> · colombian<b>a</b> · portugu<b>esa</b> · franc<b>esa</b> · ingl<b>esa</b></div></div>
    <p style="font-size:9pt;margin:1mm 0 0">Algunas no cambian (♂=♀): <b>belga</b>, <b>marroquí</b>, <b>estadounidense</b>, <b>canadiense</b>. ⚠️ En español van en <b>minúscula</b>: soy <b>español</b>, hablo <b>neerlandés</b>. <span class="gloss">in het Nederlands net met een hoofdletter</span></p>
  </div>
  <div class="regla"><span class="tag">hablo + idioma · welke talen je spreekt</span>
    <table class="gt2"><tr><td class="v">Hablo</td><td>ik spreek</td><td class="ex"><b>Hablo</b> neerlandés y un poco de español.</td></tr>
    <tr><td class="v">¿Hablas…?</td><td>spreek jij…?</td><td class="ex">¿<b>Hablas</b> francés?</td></tr>
    <tr><td class="v">¿Habla usted…?</td><td>spreekt u…?</td><td class="ex">¿<b>Habla usted</b> inglés?</td></tr></table>
    <p style="font-size:9pt;margin:1mm 0 0">De vrouw in de video spreekt <b>tres idiomas</b>: árabe, francés y español. Steun: «un poco» / «bastante bien».</p>
  </div>
  <div class="regla"><span class="tag">tú ↔ usted</span>
    <p style="margin:1mm 0 0;font-size:9.6pt">Con amigos y compañeros: <b>tú</b> — <span class="ex" style="color:var(--mut)">¿De dónde eres?</span><br>En situación formal, con un adulto desconocido: <b>usted</b> — <span class="ex" style="color:var(--mut)">¿De dónde es usted? / ¿Habla usted francés?</span> <span class="gloss">tú of usted, naar de situatie</span></p>
  </div>
  <div class="truc"><b>Mini-ejercicio 1 · soy de.</b> Completa con <i>soy de · eres de · es de</i>:
    <div style="margin-top:2mm;font-size:9.6pt;line-height:2.4">1. Yo {wl('sm')} Bélgica. &nbsp; 2. ¿{wl('sm')} (tú) España? &nbsp; 3. Diego {wl('sm')} México. &nbsp; 4. ¿De dónde {wl('sm')} usted?</div>
  </div>
  <div class="truc"><b>Mini-ejercicio 2 · país → gentilicio.</b> Escribe la nacionalidad (♂/♀, en minúscula): a) México (chico) → {wl('sm')} &nbsp; b) Colombia (chica) → {wl('sm')} &nbsp; c) Francia (chica) → {wl('sm')}</div>
</div>
"""

def act(n,title,badges,body):
    bh="".join(f'<span class="badge {c}">{t}</span>' for t,c in badges)
    return (f'<div class="act"><div class="acthead"><div class="anum">{n}</div><div><div class="h">{title}</div>'
            f'<div class="badges">{bh}</div></div></div>{body}</div>')

PRAC=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§3 · Práctica</div><h2>Practica en papel · online se corrige solo <span class="gloss" style="font-size:10pt;font-weight:400">online verbetert het zichzelf</span></h2>

  {act(1,"Clasifica: país, gentilicio o idioma",[("receptief","skill"),("5 min","")],
    '<p style="margin-left:12.5mm">Schrijf elk woord in de juiste kolom. Voeg onderaan één eigen woord toe.<br><span class="gloss">España · mexicana · el árabe · Colombia · belga · el inglés · Argentina · francés (idioma)</span></p>'
    +'<div class="wcols" style="margin-left:12.5mm"><div class="wcol"><h4>País 🌍</h4><div class="fill"></div></div><div class="wcol"><h4>Gentilicio 🪪</h4><div class="fill"></div></div><div class="wcol"><h4>Idioma 🗣️</h4><div class="fill"></div></div><div class="wcol"><h4>Tu palabra</h4><div class="fill"></div></div></div>')}

  {act(2,"Relaciona país ↔ nacionalidad",[("gestuurd","skill"),("★☆☆","")],
    '<p style="margin-left:12.5mm">Une con una línea el país y la nacionalidad (♂/♀). <span class="gloss">verbind land en nationaliteit</span></p>'
    +'<table class="mtab" style="margin-left:12.5mm"><tr><td class="a">1. España</td><td><span class="ln"></span></td><td class="b">a. mexicano / mexicana</td></tr>'
    +'<tr><td class="a">2. México</td><td><span class="ln"></span></td><td class="b">b. colombiano / colombiana</td></tr>'
    +'<tr><td class="a">3. Colombia</td><td><span class="ln"></span></td><td class="b">c. español / española</td></tr>'
    +'<tr><td class="a">4. Argentina</td><td><span class="ln"></span></td><td class="b">d. belga</td></tr>'
    +'<tr><td class="a">5. Bélgica</td><td><span class="ln"></span></td><td class="b">e. argentino / argentina</td></tr></table>')}

  {act(3,"Completa el diálogo",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Completa la conversación (piensa en <i>soy de</i> + país, y en el gentilicio). <span class="gloss">gebruik soy de + land en de gentilicio</span></p>'
    +f'<div style="margin-left:12.5mm;font-size:10pt;line-height:2.5">'
    +f'— Hola, ¿de dónde {wl("sm")}?<br>— {wl("sm")} de México. Soy {wl("sm")} <span style="color:var(--mut);font-size:8.6pt">(un chico)</span>.<br>— ¿Qué idiomas {wl("sm")}?<br>— {wl("sm")} español e inglés.</div>')}

  {act(4,"Ordena la conversación",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Numera las frases en el orden correcto (1–5). <span class="gloss">nummer de zinnen</span></p>'
    +'<div class="scramble" style="margin-left:12.5mm"><span>___ Hablo español y un poco de inglés.</span><span>___ Hola, ¿de dónde eres?</span><span>___ ¡Encantado! Hasta luego.</span><span>___ Soy de Colombia, de Cartagena.</span><span>___ ¡Qué bien! ¿Y qué idiomas hablas?</span></div>')}

  {act(5,"La nacionalidad · ¿-o o -a?",[("gestuurd","skill"),("★☆☆","")],
    f'<p style="margin-left:12.5mm">Escribe la letra correcta (♂ -o / ♀ -a). <span class="gloss">vul de juiste letter in</span></p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. Diego (chico) es mexican{wl("sm")} &nbsp; 2. Valen (chica) es colombian{wl("sm")} &nbsp; 3. Mateo (chico) es argentin{wl("sm")} &nbsp; 4. Nina (chica) es peruan{wl("sm")}</div>')}

  {act(6,"Entrevista a un compañero",[("interactie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Pregúntaselo a tres compañeros y anota la respuesta. Después cambiad. <span class="gloss">vraag het aan drie klasgenoten</span></p>'
    +f'<table class="wtab" style="margin-left:12.5mm;margin-top:2mm"><thead><tr><th style="width:38mm">Pregunta</th><th>Compañero/a 1</th><th>Compañero/a 2</th><th>Compañero/a 3</th></tr></thead>'
    +'<tr><td style="height:12mm">¿De dónde eres?</td><td></td><td></td><td></td></tr>'
    +'<tr><td style="height:12mm">¿Qué idiomas hablas?</td><td></td><td></td><td></td></tr></table>')}

  {act(7,"Escribe tres fichas",[("productie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Escribe sobre 3 personas (reales o inventadas): «X es de ___. Es ___ y habla ___.» (2 frases cada una). <span class="gloss">3 personen, 2 zinnen elk</span></p>'
    +'<div class="wbox" style="margin-left:12.5mm"></div>')}

  {act(8,"Escribe un mensaje",[("productie","skill"),("★★★","")],
    '<p style="margin-left:12.5mm">Escribe un mensaje corto (WhatsApp) a un amigo o una amiga hispanohablante nuevo/a: preséntate con tu país, tu nacionalidad y tus idiomas. <span class="gloss">stel je voor met land, nationaliteit en talen</span></p>'
    +'<div class="wbox" style="margin-left:12.5mm;min-height:28mm"></div>')}

  {act(9,"¿De qué país?",[("productie","skill"),("★★☆","")],
    f'<p style="margin-left:12.5mm">Escribe el país y la nacionalidad (♂) junto a cada bandera. ¡Rápido! <span class="gloss">land én nationaliteit bij elke vlag</span></p>'
    +f'<div style="margin-left:12.5mm;font-size:9.8pt;line-height:2.3">🇲🇽 → {wl("lg")} &nbsp;&nbsp; 🇪🇸 → {wl("lg")}<br>🇨🇴 → {wl("lg")} &nbsp;&nbsp; 🇦🇷 → {wl("lg")}</div>')}
</div>
"""

TAREA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§5 · Tarea final</div><h2>Mi mapa · ¿De dónde eres?</h2>
  <div class="esen" style="margin-top:2mm"><b class="tt">Tu tarea.</b> Haz un <b>minimapa</b> con <b>3 personas</b> (tú y 2 más: compañeros o gente conocida). Di de qué <b>país</b> es cada una (soy/es de), su <b>nacionalidad</b> y qué <b>idiomas</b> habla. Señala el país en el mapa del mundo (pestaña Mapa) y preséntalas. <span class="gloss">Sin leer del papel — zonder van het blad af te lezen.</span></div>
  <div class="regla" style="margin-top:4mm"><span class="tag">Prepárate · rellena primero los marcos (tu versión) <span class="gloss">vul eerst de frames in</span></span>
    <div style="margin-top:2mm;font-size:9.7pt;line-height:2.4">🧍 Yo soy de {wl('sm')} . Soy {wl('sm')} y hablo {wl('sm')} .<br>🧑 ____ es de {wl('sm')} . Es {wl('sm')} y habla {wl('sm')} .<br>👤 ____ es de {wl('sm')} . Es {wl('sm')} y habla {wl('sm')} .</div>
  </div>
  <div style="margin-top:4mm"><div class="se">Mi mapa · anota tus 3 fichas</div>
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
    <div class="truc" style="margin:0"><b>🏁 Está listo cuando…</b> dices de 3 personas «es de + país», das el <b>gentilicio</b> correcto (♂/♀, en minúscula) y los <b>idiomas</b>, y señalas el país en el mapa, sin leer. <span class="gloss">zónder af te lezen</span></div>
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
  <p style="font-size:9.6pt">El <b>español</b> une <b>21 países</b> y lo hablan más de <b>490 millones</b> de personas: es la segunda lengua materna más hablada del mundo. Una lengua, muchos acentos y culturas. Hasta en África: <b>Guinea Ecuatorial</b>. Y los artistas de la banda sonora vienen de todo ese mundo: <span class="gloss">één taal, 21 landen, veel accenten</span></p>
  <div class="bandas">{"".join(banda(*b) for b in BANDAS)}</div>
  <div class="musrow">
    <div class="call"><span class="ic">🎧</span><div><b>Spotify · la playlist de la clase.</b> Escanea y escucha. En la página digital tienes también <b>LyricsTraining</b> y el <b>mapa del mundo</b> (pulsa cada país para ver su ficha). <span class="gloss">scan en luister; online staat er meer</span></div></div>
    <div class="qr" data-url="{SPOTIFY}"><div class="lab">Playlist</div>{qr(SPOTIFY)}<div class="meta">Spotify</div></div>
  </div>

  <div class="truc" style="margin-top:5mm"><b>El mundo hispano · sabías que…?</b> Verbind (gis gerust):
    <table class="mtab" style="margin-top:1mm"><tr><td class="a">El único país hispanohablante en África…</td><td>{wl('sm')}</td><td class="b">a. México (~130 millones)</td></tr>
    <tr><td class="a">El país con más hispanohablantes…</td><td>{wl('sm')}</td><td class="b">b. Guinea Ecuatorial</td></tr>
    <tr><td class="a">El gentilicio se escribe con…</td><td>{wl('sm')}</td><td class="b">c. minúscula (soy belga)</td></tr></table>
    <p style="font-size:8.6pt;color:var(--mut);margin-top:1mm">💡 «americano» betekent niet enkel «uit de VS»: héél América (Noord, Midden én Zuid) is <b>América</b>.</p>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div><div class="se">¿De qué país? · relaciona al artista</div>
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
  <div class="se">Repaso · Lo esencial de un vistazo</div><h2>Lo que ya sabes hacer <span class="gloss">wat je nu kunt</span></h2>
  <div class="fams">
    <div class="pcard"><div class="t">Así preguntas y dices el origen <span class="gloss">vragen en zeggen waar je vandaan komt</span></div><div class="ej">¿<b>De dónde eres</b>? → <b>Soy de</b> + país (Soy de Bélgica).</div><div class="t2">Land = met <b>de</b> · nationaliteit = zónder de (soy belga).</div></div>
    <div class="pcard"><div class="t">Nacionalidad e idiomas <span class="gloss">nationaliteit en talen</span></div><div class="ej">Soy mexican<b>o</b>/mexican<b>a</b> · Hablo español, neerlandés…</div><div class="anchor"><b>-o</b> = ♂ · <b>-a</b> = ♀ &nbsp;|&nbsp; kleine letter: <b>belga</b>, <b>francés</b></div></div>
  </div>
  <div class="regla" style="margin:4mm 0"><span class="tag">Frases para la clase</span>
    <div class="cogn" style="margin-top:1mm"><span>¿Cómo se dice… ?</span><span>¿Qué significa… ?</span><span>Otra vez, por favor</span><span>No entiendo</span><span>¿Puedes repetir?</span><span>Más despacio, por favor</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Handige klaszinnen — gebruik ze in het Spaans i.p.v. Nederlands.</span>
  </div>
  <table class="sem"><thead><tr><th style="text-align:left">Puedo… · Ik kan…</th><th>🟢</th><th>🟡</th><th>🔴</th></tr></thead>
    <tr><td>vragen en zeggen waar iemand vandaan komt (soy de + país)</td><td></td><td></td><td></td></tr>
    <tr><td>de nationaliteit geven (♂/♀, kleine letter)</td><td></td><td></td><td></td></tr>
    <tr><td>zeggen welke talen ik spreek (hablo…)</td><td></td><td></td><td></td></tr>
    <tr><td>situar en el mapa los países del mundo hispano <span class="gloss">de landen op de kaart situeren</span></td><td></td><td></td><td></td></tr></table>
  <div class="regla" style="margin-top:5mm"><span class="tag">Mini-test · recuerda sin mirar</span>
    <p style="margin:1mm 0 0;font-size:9.4pt">Cierra el libro y traduce de memoria: recordar es la mejor manera de aprender. <span class="gloss">uit het hoofd — ophalen leert het best</span></p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3mm 8mm;margin-top:2mm;font-size:9.8pt;line-height:2.2">
      <div>1. ¿de dónde eres? → {wl('')}</div><div>2. ik kom uit België → {wl('')}</div>
      <div>3. ik ben Belgisch → {wl('')}</div><div>4. welke talen spreek je? → {wl('')}</div>
      <div>5. ik spreek Nederlands → {wl('')}</div><div>6. zij is Mexicaanse → {wl('')}</div>
    </div>
  </div>
  <div class="guide"><span class="ic">🎮</span><div><span class="hand">Repasa jugando</span><div class="g">Oefen alles online met spelletjes, flashcards, de <b>wereldkaart</b> en audio op de digitale hub (scan de QR bij §1).</div></div></div>
  <div class="bridge"><b>Próxima parada →</b> En la unidad siguiente presentas a tu familia: <i>la familia</i>. ¡Hasta pronto! <span class="gloss">volgende halte: de familie</span></div>
</div>
"""

EDITBAR="""
<div class="editbar" id="eb">
  <b>✏️ C4 · U3</b>
  <button id="btnedit">Editar</button>
  <button id="btnpdf">🖨️ Guardar como PDF</button>
  <button id="btnsave">💾 Guardar (.html)</button>
  <span class="sp"></span>
  <span style="opacity:.85;font-size:12px">Consejo: activa «Editar», cambia el texto y guárdalo como PDF. <span class="gloss">bewerken aanzetten, aanpassen, opslaan</span></span>
</div><div class="scr-spacer"></div>
"""
SCRIPT="""
<script>
var editing=false;var be=document.getElementById('btnedit');
be.onclick=function(){editing=!editing;document.querySelectorAll('.page,.hero').forEach(function(p){p.contentEditable=editing;});document.body.classList.toggle('editing',editing);be.classList.toggle('on',editing);be.textContent=editing?'Dejar de editar':'Editar';};
document.getElementById('btnpdf').onclick=function(){window.print();};
document.getElementById('btnsave').onclick=function(){var html='<!doctype html>'+document.documentElement.outerHTML;var b=new Blob([html],{type:'text/html'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='C4_U3_Nacionalidades_bewerkt.html';a.click();};
</script>
"""

HTML=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 3 · Nacionalidades y países</title><style>{CSS}</style></head><body class="c4">
{EDITBAR}
{HERO}{ESCUCHA}{COMPR_SEC}{KIT}{GRAM}{PRAC}{TAREA}{MUSICA}{FUNCIONES_SEC}{REPASO}
{SCRIPT}
</body></html>"""
os.makedirs(f"{ROOT}/03-build/web/print",exist_ok=True)
open(f"{ROOT}/03-build/web/print/C4_U3.html","w",encoding="utf-8").write(HTML)
print("C4_U3.html (print+editable) geschreven:",len(HTML),"bytes")
