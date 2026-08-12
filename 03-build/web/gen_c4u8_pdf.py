#!/usr/bin/env python3
# C4 · Unidad 8 — PRINT (HTML=bron → PDF via Chromium). Golden-sample print-kit, C4-rood.
# Thema: La hora y los días · ¿qué hora es? (es la una/son las…) · ¿a qué hora? · el/los lunes · quedar.
# NB: de video komt uit Google Drive → de QR verwijst (zoals altijd) naar de HTML-hub, niet naar Drive.
import base64, os, re, io, sys, math
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
from funciones_print import print_section
FUNCIONES_SEC=print_section(8)
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
HUB_URL=EN.url("C4", 8)
import comprension_print
COMPR_SEC=comprension_print.print_section(8, HUB_URL)
SPOTIFY="https://open.spotify.com/playlist/37i9dQZF1DXaxEKcoCdWHD"

# print-klokjes (SVG, grijswaarden-veilig: ook de cijfertijd staat erbij)
def pclock(h,m,label,digital):
    hx=50+26*math.sin(math.radians((h%12)*30+m*0.5)); hy=50-26*math.cos(math.radians((h%12)*30+m*0.5))
    mx=50+36*math.sin(math.radians(m*6)); my=50-36*math.cos(math.radians(m*6))
    return (f'<div class="pclk"><svg viewBox="0 0 100 100" aria-label="{label}">'
            f'<circle cx="50" cy="50" r="46" fill="#fff" stroke="#C9C3C0" stroke-width="3"/>'
            f'<circle cx="50" cy="50" r="2.6" fill="#A8323B"/>'
            f'<line x1="50" y1="50" x2="{hx:.1f}" y2="{hy:.1f}" stroke="#20242E" stroke-width="4.6" stroke-linecap="round"/>'
            f'<line x1="50" y1="50" x2="{mx:.1f}" y2="{my:.1f}" stroke="#D64550" stroke-width="3.2" stroke-linecap="round"/>'
            f'</svg><b>{digital}</b><i>{label}</i></div>')

SCENES=[
 ("Escena 1 · La llamada (falsa)",[
  ("Julio","¿Sí? Laura, ¿cómo estás? ¿Qué? No te oigo nada."),
  ("Julio","¿Esta noche? ¿Quieres quedar esta noche?"),
  ("Julio","Estoy en una fiesta. No sé si puedo. ¿Puedes hablar más despacio?"),
  ("Julio","Ahora estoy en una fiesta. Más tarde sí, más tarde puede ser."),
  ("Julio","Entonces, quedamos en mi casa. ¿A qué hora?"),
  ("Julio","No, a las once no, mejor a las doce."),
  ("Julio","¿Qué hora es ahora? ¿Las ocho y media?"),
  ("Julio","No, ahora mismo no puedo quedar."),
  ("Julio","Pues no sé, un cine, un restaurante. Pero es un poco pronto para eso, ¿no?"),
  ("Julio","Te veo en veinte minutos. Hasta ahora. Un beso."),
  ("Julio","Bueno, me voy, es un poco tarde."),
 ]),
 ("Escena 2 · «Venga, vámonos»",[
  ("María","Sí. Venga, vámonos."),
  ("Julio","¿Cómo, tú y yo?"),
  ("Julio","¿A dónde?"),
  ("María","A tomar una cerveza."),
  ("Julio","Vámonos, sí."),
 ]),
]
CH=["¿Qué hora es?","las ocho y media","¿A qué hora?","a las once","a las doce","¿Quieres quedar","quedamos en mi casa","esta noche","Más tarde","ahora mismo","un poco tarde","un poco pronto","en veinte minutos","Hasta ahora","No te oigo nada","¿Puedes hablar más despacio?","puede ser","un cine","un restaurante","vámonos","Un beso"]
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
 ("¿Qué hora es?",[("¿Qué hora es?","Hoe laat is het?"),("Es la una","Het is één uur"),("Son las ocho","Het is acht uur"),
   ("y cuarto · y media","kwart over · half"),("menos cuarto · en punto","kwart voor · precies")]),
 ("Los días de la semana",[("lunes · martes · miércoles","ma · di · wo"),("jueves · viernes","do · vr"),
   ("sábado · domingo","za · zo"),("el fin de semana","het weekend"),("hoy · mañana","vandaag · morgen")]),
 ("Los momentos del día",[("por la mañana","'s ochtends"),("por la tarde · por la noche","'s middags · 's avonds"),
   ("esta noche","vanavond"),("más tarde · ahora mismo","later · nu meteen"),("pronto · tarde","vroeg · laat")]),
 ("Quedar · afspreken",[("¿Quieres quedar?","Wil je afspreken?"),("¿A qué hora?","Hoe laat?"),
   ("Quedamos a las…","We spreken af om…"),("¿Dónde quedamos?","Waar spreken we af?"),("Vale · perfecto","Oké · perfect")]),
 ("Por teléfono",[("¿Sí?","Ja? (opnemen)"),("No te oigo (nada)","Ik hoor je (helemaal) niet"),
   ("¿Puedes hablar más despacio?","Kan je langzamer spreken?"),("Hasta ahora · un beso","Tot straks · kusje")]),
]
def kitrow(es,nl):
    return f'<tr><td class="k-es">{es}</td><td class="k-nl gloss">{nl}</td><td class="k-ck"><span class="chk"></span></td></tr>'
def kittable(name,items):
    rows="".join(kitrow(*i) for i in items)
    return (f'<div class="kit"><div class="kit-h">{name}</div>'
      f'<table class="ktab"><thead><tr><th>Español</th><th>Nederlands</th><th>🔊 na</th></tr></thead><tbody>{rows}</tbody></table></div>')

def wl(cls=""): return f'<span class="wl {cls}"></span>'

CSS=FONTS+PRINTCSS+r"""
:root{ --g:#D64550; --gd:#A8323B; --gt:#FBEAEC; }
.gloss{ font-size:.9em; line-height:1.32; }   /* steun is steun: kleiner en dichter */
.p{color:#2563EB;font-weight:700}.v{color:#EA7317;font-weight:700}.o{color:#1E9E74;font-weight:700}.pl{color:#0E9E97;font-weight:700}.t{color:#7C3AED;font-weight:700}
.tl{display:flex;gap:3mm;padding:.55mm 0;font-size:9.5pt;break-inside:avoid}
.tl .sp{font-family:var(--disp);font-weight:700;color:var(--gd);width:20mm;flex:none}
.tl .tx b{background:var(--gt);border-radius:3pt;padding:.2mm 1.2mm;font-weight:700}
.twocol{column-count:2;column-gap:8mm}
.kitwrap{display:grid;grid-template-columns:1fr 1fr;gap:3mm 5mm;margin-top:2mm}
.kit{break-inside:avoid}
.kit-h{font-family:var(--disp);font-weight:700;font-size:9.6pt;color:var(--gd);margin:1mm 0 .5mm}
.ktab{font-size:8.8pt;width:100%}.ktab th{background:var(--gt);color:var(--gd);font-size:7.2pt;text-transform:uppercase;padding:.8mm 2mm;text-align:left}
.ktab td{border-bottom:1px solid var(--line);padding:.55mm 2mm}.k-es{font-weight:600}.k-ck{text-align:center;width:12mm}
.chk{display:inline-block;width:3.4mm;height:3.4mm;border:1.3px solid var(--mut);border-radius:1.5pt;vertical-align:middle}
.gt2{width:100%;font-size:9.2pt;margin:2mm 0}.gt2 td{border-bottom:1px solid var(--line);padding:1.5mm 2.5mm}
.gt2 .t{color:#7C3AED;font-family:var(--disp)}.gt2 .pl{color:#0E9E97;font-family:var(--disp)}.gt2 .ex{color:var(--mut);font-style:italic}
.mv2{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin:2mm 0}
.mv2 div{border-radius:8pt;padding:2.5mm 4mm;font-family:var(--disp)}
.mv2 .m{background:#EDE9FE;color:#5B21B6}.mv2 .f{background:#E6F7F5;color:#0B7A73}
.pclkrow{display:grid;grid-template-columns:repeat(6,1fr);gap:3mm;margin:2mm 0}
.pclk{border:1px solid var(--line);border-radius:8pt;padding:2mm 1mm;text-align:center;break-inside:avoid}
.pclk svg{width:100%;max-width:16mm;height:auto}
.pclk b{display:block;font-family:var(--disp);font-size:9pt;color:var(--gd)}
.pclk i{display:block;font-size:7pt;color:var(--mut);font-style:normal;line-height:1.2}
.wl{display:inline-block;border-bottom:1.4px solid var(--line2);min-width:38mm;height:5mm;vertical-align:bottom}
.wl.full{min-width:0;width:100%}.wl.lg{min-width:66mm}.wl.sm{min-width:22mm}
.wcols{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin-top:2mm}
.wcol{border:1px solid var(--line);border-radius:8pt;overflow:hidden;break-inside:avoid}
.wcol h4{font-family:var(--disp);font-size:8.6pt;margin:0;background:var(--gt);color:var(--gd);padding:1.5mm 2mm;text-align:center}
.wcol .fill{min-height:34mm;background:repeating-linear-gradient(transparent,transparent 6.2mm,var(--line) 6.2mm,var(--line) 6.4mm);}
.wbox{border:1px solid var(--line);border-radius:8pt;min-height:24mm;background:repeating-linear-gradient(transparent,transparent 6.2mm,var(--line) 6.2mm,var(--line) 6.4mm);margin-top:2mm}
.wtab{width:100%;font-size:9pt}.wtab th{background:var(--gt);color:var(--gd);font-size:7.6pt;text-transform:uppercase;padding:1.5mm}.wtab td{border:1px solid var(--line);height:9mm;padding:1mm 2mm}
.mtab{width:100%;font-size:9.4pt;margin-top:2mm}.mtab td{padding:1.8mm 2mm;border-bottom:1px dashed var(--line2)}.mtab .a{font-weight:600}.mtab .b{color:var(--mut)}.mtab .ln{width:8mm;border-bottom:1.4px solid var(--line2);display:inline-block}
.scramble{display:flex;flex-wrap:wrap;gap:2mm;margin:2mm 0}.scramble span{border:1px solid var(--line);border-radius:6pt;padding:1mm 3mm;font-weight:600;font-size:9pt;background:#fff}
.klemline{font-size:10pt;margin:3mm 0 0}.klemline .t{background:var(--gt);border-radius:4pt;padding:.3mm 1.6mm;font-weight:700;color:var(--gd)}
.cast2{display:grid;grid-template-columns:repeat(5,1fr);gap:3mm;margin:3mm 0}
.cast2 .m{border:1px solid var(--line);border-top:3px solid var(--g);border-radius:8pt;padding:2.5mm;text-align:center;break-inside:avoid}
.cast2 .nm{font-family:var(--disp);font-weight:700;font-size:10pt;color:var(--gd)}.cast2 .ro{font-size:7.6pt;color:var(--mut)}.cast2 .fl{font-size:12pt}
.cogn{display:flex;flex-wrap:wrap;gap:2mm;margin:2mm 0}.cogn span{background:var(--gt);border-radius:20pt;padding:.8mm 3mm;font-size:9.2pt;font-weight:600;color:var(--gd)}
.vf{width:100%;font-size:9.5pt;margin:2mm 0}.vf td{border-bottom:1px solid var(--line);padding:1.9mm 2mm}.vf .b{width:26mm;text-align:center;color:var(--mut);white-space:nowrap}
.modelo{border-left:3px solid var(--g);background:var(--gt);border-radius:0 8pt 8pt 0;padding:2.5mm 5mm;margin:2mm 0;font-size:9.7pt}
.modelo b{color:var(--gd)}
.rubric{width:100%;font-size:9pt;margin:2mm 0}.rubric th{background:var(--g);color:#fff;text-align:left;padding:1.6mm 2.4mm;font-size:8pt}.rubric td{border:1px solid var(--line);padding:1.6mm 2.4mm}
.bandas{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-top:3mm}
.banda{border:1px solid var(--line);border-radius:10pt;padding:3mm 4mm;break-inside:avoid}
.banda .ar{font-family:var(--disp);font-weight:700;font-size:10pt}.banda .sg{font-size:8.4pt;color:var(--mut)}.banda .ge{font-size:7.6pt;color:var(--gd)}
.musrow{display:grid;grid-template-columns:1fr auto;gap:5mm;align-items:center;margin-top:4mm}
.horario{width:100%;font-size:9pt;margin-top:2mm}
.horario th{background:var(--g);color:#fff;font-size:7.6pt;text-transform:uppercase;padding:1.4mm}
.horario td{border:1px solid var(--line);height:11mm;padding:1mm 2mm}
.horario td.h{background:var(--gt);color:var(--gd);font-family:var(--disp);font-weight:700;width:20mm;text-align:center;font-size:8.4pt}
.editbar{position:fixed;top:0;left:0;right:0;background:var(--gd);color:#fff;display:flex;gap:8px;align-items:center;padding:7px 12px;z-index:999;font-family:var(--body);font-size:13px;box-shadow:0 2px 10px #0003}
.editbar b{font-family:var(--disp)}.editbar button{border:0;background:#fff;color:var(--gd);font-weight:700;border-radius:8px;padding:6px 11px;cursor:pointer;font-size:12.5px}
.editbar button.on{background:#111;color:#fff}.editbar .sp{flex:1}.scr-spacer{height:44px}
body.editing .page{outline:1.5px dashed var(--g);outline-offset:-6px}
@media print{ .editbar,.scr-spacer{display:none!important} }
"""

HERO=f"""
<section class="hero">
  <div class="tab">C4 · LA RUTA</div>
  <div class="eyebrow">EL DESPEGUE · PARADA 8 · SURVIVAL IN SPANISH</div>
  <h1>La hora y los días</h1>
  <div class="sub">Decir <b>qué hora</b> es y <b>quedar</b> con alguien. <span class="gloss">La hora y los días — ¿qué hora es? · son las ocho y media · ¿a qué hora? · el lunes · ¿quieres quedar?</span></div>
  <div class="q">¿Qué hora es? — Son las ocho y media.</div>
</section>
<div class="page">
  <div class="obj"><div class="se">Al final de esta unidad <span class="gloss">op het einde van deze les</span></div>
    <ul>
      <li><span class="ck">✓</span> <span><span class="es">Decir la hora</span> <span class="nl">— es la una · son las ocho · y media · menos cuarto</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Preguntar <b>¿a qué hora?</b></span> <span class="nl">— a la una · a las doce (om …)</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Los días de la semana</span> <span class="nl">— el lunes (op maandag) · los lunes (elke maandag)</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es"><b>Quedar</b> con alguien</span> <span class="nl">— ¿quieres quedar? · quedamos a las… · hasta ahora</span></span></li>
    </ul>
  </div>
  <div class="guide"><span class="ic">🎒</span><div><span class="hand">¡Seguimos la ruta! Parada 8.</span><div class="g">En esta lección de «survival» aprendes a decir la hora en español. En el vídeo Julio finge que habla por teléfono con «Laura» para poner celosa a María, y va nombrando <i>todas</i> las horas: a las once, a las doce, las ocho y media… <span class="gloss">klokkijken in het Spaans</span></div></div></div>

  <div class="se" style="margin-top:5mm">Los relojes · así suena la hora</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Kijk naar de klokjes en lees de Spaanse tijd. Let op de <b>y media</b>!</p>
  <div class="pclkrow">
    {pclock(1,0,"Es la una","1.00")}{pclock(3,15,"Son las tres y cuarto","3.15")}{pclock(8,30,"Son las ocho y media","8.30")}
    {pclock(6,45,"Son las siete menos cuarto","6.45")}{pclock(12,0,"Son las doce en punto","12.00")}{pclock(9,10,"Son las nueve y diez","9.10")}
  </div>

  <div class="truc" style="margin-top:4mm"><b>¿Qué reconoces ya?</b> Estas palabras del tiempo se parecen al neerlandés o al inglés, o ya las conoces (<i>palabras transparentes</i>):
    <div class="cogn"><span>el minuto</span><span>la hora</span><span>el momento</span><span>el calendario</span><span>la agenda</span><span>el fin de semana</span><span>el cine</span><span>el restaurante</span><span>la fiesta</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Tip: <b>minuto</b>, <b>momento</b>, <b>agenda</b> herken je meteen.</span>
  </div>
</div>
"""

ESCUCHA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§1 · ¡Escucha!</div><h2>Mira la escena y lee al mismo tiempo <span class="gloss" style="font-size:10pt;font-weight:400">bekijk en lees mee</span></h2>
  <div class="audiorow">
    <div class="call"><span class="ic">🎬</span><div><b>Sitcom · Episodio 8 · Las horas.</b> Escanea el código y mira el episodio en la página digital. En una fiesta Julio finge hablar con «Laura» para poner celosa a María. Escucha <i>todas</i> las <b>horas</b> que nombra. Primero escucha sin leer; después lee al mismo tiempo. Las palabras en <b>negrita</b> son chunks para llevarte. <span class="gloss">eerst zónder te lezen, daarna lees je mee</span></div></div>
    <div class="qr" data-url="{EN.url('C4', 8, EN.ancla_c4('escucha'))}"><div class="lab">Vídeo online</div>{qr(EN.url("C4", 8, EN.ancla_c4("escucha")))}<div class="meta">hub · Escucha</div></div>
  </div>
  <div class="truc"><b>Antes de escuchar.</b> ¿Qué <b>horas</b> crees que vas a oír? ¿Y a qué hora quedan? <span class="gloss">welke uren, denk je?</span> <span style="font-size:8.8pt;color:var(--mut)">(gis gerust)</span>
    <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.2">Una hora: {wl('sm')} &nbsp;&nbsp; Otra hora: {wl('sm')} &nbsp;&nbsp; ¿A qué hora quedan? {wl('sm')}</div>
  </div>
  <div class="twocol">{scenehtml(*SCENES[0])}{scenehtml(*SCENES[1])}</div>
  <div class="ojo"><b>¡Ojo!</b> «Son las ocho y media» = <b>half negen</b>. Het Spaans kijkt <b>terug</b> (acht + dertig), het Nederlands <b>vooruit</b> (negen). En «a las doce» = <b>om</b> twaalf uur (afspraak).</div>

  <div class="se" style="margin-top:5mm">Después de escuchar · ¿Verdadero o falso?</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Kruis aan. Verbeter de <b>falsas</b> op de lijn.</p>
  <table class="vf">
    <tr><td>1. Julio quiere quedar a las once.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>2. Cuando habla, son las ocho y media.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>3. Julio dice que ve a Laura en veinte minutos.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>4. Al final, María y Julio van a tomar una cerveza.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
  </table>
</div>
"""

KIT=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Suena bien · pronunciación</div><h2>La d suave &amp; el acento en los números</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 1mm">Tussen klinkers is de <b>d</b> héél zacht, bijna als de Engelse «th» in <i>this</i>: «na-da», «me-dia». Aan het begin is ze steviger: «<b>d</b>ía», «<b>d</b>oce». Oefen online (QR §1).</p>
  <div class="cogn"><span>nada</span><span>cada</span><span>media</span><span>sábado</span><span>quedar</span><span>adiós</span></div>
  <div class="ojo"><b>¡Ojo!</b> Zeg «me<b>d</b>ia» zacht — niet als de harde NL «d». Vergelijk: <b>d</b>oce (stevig) ↔ na<b>d</b>a (zacht).</div>
  <div class="cogn"><span>día</span><span>dos</span><span>doce</span><span>domingo</span><span>después</span><span>despacio</span></div>
  <div class="klemline"><b>El acento en los números · ¿dónde cae?</b> die·ci·<span class="t">SÉIS</span> · vein·ti·<span class="t">DÓS</span> (con tilde) &nbsp;↔&nbsp; ca·<span class="t">TOR</span>·ce · cua·<span class="t">REN</span>·ta (sin tilde) <span class="gloss">waar valt de klemtoon?</span></div>

  <div class="se" style="margin-top:3mm">§2 · Kit de supervivencia</div><h2>La lengua que de verdad necesitas <span class="gloss" style="font-size:10pt;font-weight:400">de taal die je écht nodig hebt</span></h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 2mm">Marca ☐ cada vez que puedas <b>repetir</b> una expresión con soltura. Practícalas en línea con audio. <span class="gloss">vink af wat je vlot kunt naspreken</span></p>
  <div class="kitwrap">{"".join(kittable(n,it) for n,it in CLUSTERS)}</div>
</div>
"""

GRAM=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§4 · Gramática en la práctica</div><h2>Corta y funcional <span class="gloss" style="font-size:10pt;font-weight:400">kort en functioneel</span></h2>
  <div class="modelo"><b>🔎 Fíjate · vuelve a la escena.</b> Ya lo has oído: «<b>¿Qué hora es?</b> ¿<b>Las ocho y media</b>?» · «<b>¿A qué hora?</b> No, <b>a las once</b> no, mejor <b>a las doce</b>» · «¿<b>Quieres quedar</b> esta noche? — <b>Quedamos</b> en mi casa». Descubre tú el patrón — <i>primero el significado, después la regla.</i> <span class="gloss">ontdek zelf het patroon</span></div>
  <div class="regla"><span class="tag">¿Qué hora es? · es la una ↔ son las dos</span>
    <div class="mv2"><div class="m">🕐 alleen 1 uur: <b>Es la</b> una · <b>Es la</b> una y media</div><div class="f">🕑 alle andere: <b>Son las</b> dos · tres · ocho · doce</div></div>
    <p style="font-size:9pt;margin:1mm 0 0">⚠️ <b>Valstrik:</b> «half negen» = <b>las ocho y media</b> (8 + 30). Spaans kijkt <b>terug</b>, Nederlands <b>vooruit</b>. Dus half tien = las nueve y media.</p>
  </div>
  <div class="regla"><span class="tag">y cuarto · y media · menos cuarto · en punto</span>
    <table class="gt2"><tr><td class="t">Son las tres y cuarto</td><td>3.15</td><td class="ex">kwart over drie</td></tr>
    <tr><td class="t">Son las tres y media</td><td>3.30</td><td class="ex">half vier (!)</td></tr>
    <tr><td class="t">Son las cuatro menos cuarto</td><td>3.45</td><td class="ex">kwart voor vier (volgend uur!)</td></tr>
    <tr><td class="t">Son las tres en punto</td><td>3.00</td><td class="ex">precies drie uur</td></tr></table>
    <p style="font-size:9pt;margin:1mm 0 0">💡 Tot :30 → <b>y</b> (erbij). Daarna → <b>menos</b> (eraf) mét het <b>volgende</b> uur.</p>
  </div>
  <div class="regla"><span class="tag">¿A qué hora? · a la una · a las doce &nbsp;|&nbsp; el lunes · los lunes</span>
    <table class="gt2"><tr><td class="t">Son las ocho.</td><td>Het <b>is</b> 8 u.</td><td class="ex">(qué hora es ahora) <span class="gloss">hoe laat het nú is</span></td></tr>
    <tr><td class="t">A las ocho.</td><td><b>Om</b> 8 u.</td><td class="ex">(wanneer iets gebeurt)</td></tr>
    <tr><td class="pl">el lunes</td><td>op maandag</td><td class="ex">niet: <s>en lunes</s></td></tr>
    <tr><td class="pl">los lunes</td><td>elke maandag</td><td class="ex">Los lunes estudio español.</td></tr></table>
    <p style="font-size:9pt;margin:1mm 0 0">⚠️ Los días van en <b>minúscula</b>: lunes, martes, sábado… <span class="gloss">met een kleine letter</span></p>
  </div>
  <div class="truc"><b>Mini-ejercicio 1 · ¿es la o son las?</b> Completa: 1. {wl('sm')} una y cuarto. &nbsp; 2. {wl('sm')} siete. &nbsp; 3. {wl('sm')} doce en punto. &nbsp; 4. {wl('sm')} cuatro y media.</div>
  <div class="truc"><b>Mini-ejercicio 2 · escribe la hora en español.</b>
    <div style="margin-top:2mm;font-size:9.6pt;line-height:2.4">a) 2.30 → {wl('lg')} &nbsp; b) 5.45 → {wl('lg')}<br>c) 1.15 → {wl('lg')} &nbsp; d) 9.00 → {wl('lg')}</div></div>
  <div class="truc"><b>Mini-ejercicio 3 · a las / el.</b> Completa: 1. Quedamos {wl('sm')} siete. &nbsp; 2. {wl('sm')} sábado voy al cine. &nbsp; 3. ¿{wl('sm')} qué hora comes?</div>
</div>
"""

def act(n,title,badges,body):
    bh="".join(f'<span class="badge {c}">{t}</span>' for t,c in badges)
    return (f'<div class="act"><div class="acthead"><div class="anum">{n}</div><div><div class="h">{title}</div>'
            f'<div class="badges">{bh}</div></div></div>{body}</div>')

PRAC=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§3 · Práctica</div><h2>Practica en papel · online se corrige solo <span class="gloss" style="font-size:10pt;font-weight:400">online verbetert het zichzelf</span></h2>

  {act(1,"Clasifica: hora, día o momento",[("receptief","skill"),("5 min","")],
    '<p style="margin-left:12.5mm">Schrijf elk woord in de juiste kolom. Voeg onderaan één eigen woord toe.<br><span class="gloss">y media · martes · por la mañana · menos cuarto · domingo · esta noche · en punto · más tarde</span></p>'
    +'<div class="wcols" style="margin-left:12.5mm"><div class="wcol"><h4>La hora 🕐</h4><div class="fill"></div></div><div class="wcol"><h4>El día 📅</h4><div class="fill"></div></div><div class="wcol"><h4>Momento 🌗</h4><div class="fill"></div></div><div class="wcol"><h4>Tu palabra</h4><div class="fill"></div></div></div>')}

  {act(2,"Del reloj a las palabras",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Escribe la hora completa en español (es la… / son las…). <span class="gloss">schrijf het uur voluit</span></p>'
    +f'<div style="margin-left:12.5mm;font-size:9.8pt;line-height:2.4">🕐 1.00 → {wl("lg")} &nbsp;&nbsp; 🕞 3.30 → {wl("lg")}<br>🕡 6.30 → {wl("lg")} &nbsp;&nbsp; 🕗 8.45 → {wl("lg")}</div>')}

  {act(3,"Relaciona · hora ↔ palabras",[("gestuurd","skill"),("★☆☆","")],
    '<p style="margin-left:12.5mm">Une con una línea la hora en cifras y la frase en español. <span class="gloss">verbind het uur met de zin</span></p>'
    +'<table class="mtab" style="margin-left:12.5mm"><tr><td class="a">1. 1.00</td><td><span class="ln"></span></td><td class="b">a. Son las ocho y media</td></tr>'
    +'<tr><td class="a">2. 8.30</td><td><span class="ln"></span></td><td class="b">b. Son las diez menos cuarto</td></tr>'
    +'<tr><td class="a">3. 9.45</td><td><span class="ln"></span></td><td class="b">c. Es la una</td></tr>'
    +'<tr><td class="a">4. 4.15</td><td><span class="ln"></span></td><td class="b">d. Son las doce en punto</td></tr>'
    +'<tr><td class="a">5. 12.00</td><td><span class="ln"></span></td><td class="b">e. Son las cuatro y cuarto</td></tr></table>')}

  {act(4,"Los días · ordena",[("gestuurd","skill"),("★☆☆","")],
    '<p style="margin-left:12.5mm">Numera los días del 1 (lunes) al 7 (domingo). <span class="gloss">nummer de dagen</span></p>'
    +'<div class="scramble" style="margin-left:12.5mm"><span>___ viernes</span><span>___ lunes</span><span>___ domingo</span><span>___ miércoles</span><span>___ sábado</span><span>___ martes</span><span>___ jueves</span></div>')}

  {act(5,"Completa el diálogo · quedar",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Completa (quedar · hora · las · media · ahora). <span class="gloss">vul aan</span></p>'
    +f'<div style="margin-left:12.5mm;font-size:10pt;line-height:2.5">'
    +f'— ¿Quieres {wl("sm")} esta noche?<br>— Sí, vale. ¿A qué {wl("sm")}?<br>— ¿A {wl("sm")} nueve?<br>— Mejor a las nueve y {wl("sm")} <span style="color:var(--mut);font-size:8.6pt">(9.30)</span>.<br>— Perfecto. ¡Hasta {wl("sm")}!</div>')}

  {act(6,"Mi día · ¿a qué hora?",[("productie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Escribe la hora en español junto a cada actividad (a las…). <span class="gloss">schrijf het uur in het Spaans</span></p>'
    +f'<div style="margin-left:12.5mm;font-size:9.8pt;line-height:2.3">🌅 Me levanto {wl("lg")}<br>🏫 Voy a clase {wl("lg")}<br>🍽️ Como {wl("lg")}<br>😴 Me acuesto {wl("lg")}</div>')}

  {act(7,"Entrevista · ¿a qué hora?",[("interactie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Pregunta a tu compañero/a por sus horarios y anota. Después cambiad. <span class="gloss">vraag naar de uren van je buur</span></p>'
    +f'<table class="wtab" style="margin-left:12.5mm;margin-top:2mm"><thead><tr><th style="width:50mm">Pregunta</th><th>Respuesta</th></tr></thead>'
    +'<tr><td style="height:12mm">¿A qué hora empiezas la clase?</td><td></td></tr>'
    +'<tr><td style="height:12mm">¿A qué hora comes?</td><td></td></tr>'
    +'<tr><td style="height:12mm">¿Qué haces el sábado?</td><td></td></tr></table>')}

  {act(8,"Queda con un compañero",[("productie","skill"),("★★★","")],
    '<p style="margin-left:12.5mm">Escribe un diálogo corto para quedar (cuatro frases): día, hora y lugar. <span class="gloss">korte afspraakdialoog</span></p>'
    +'<div class="wbox" style="margin-left:12.5mm"></div>')}
</div>
"""

TAREA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§5 · Tarea final</div><h2>Mi horario</h2>
  <div class="esen" style="margin-top:2mm"><b class="tt">Tu tarea.</b> Rellena tu <b>horario semanal</b>: elige <b>4 días</b> y escribe una actividad por día con <b>día + hora</b> («el lunes a las…»). Di las horas en voz alta. <b>Después queda</b> con un compañero/a en un momento en el que estéis los dos libres. Presenta tu semana y la cita. <span class="gloss">Sin leer del papel — zonder van het blad af te lezen.</span></div>
  <div style="margin-top:4mm"><div class="se">Mi horario · rellénalo</div>
    <table class="horario"><thead><tr><th>Hora</th><th>lunes</th><th>miércoles</th><th>viernes</th><th>sábado</th></tr></thead>
      <tr><td class="h">por la mañana</td><td></td><td></td><td></td><td></td></tr>
      <tr><td class="h">por la tarde</td><td></td><td></td><td></td><td></td></tr>
      <tr><td class="h">por la noche</td><td></td><td></td><td></td><td></td></tr></table>
  </div>
  <div class="regla" style="margin-top:4mm"><span class="tag">Prepárate · vul eerst de frames in</span>
    <div style="margin-top:2mm;font-size:9.7pt;line-height:2.4">1. <b>El</b> {wl('sm')} <b>a las</b> {wl('sm')} {wl('lg')} .<br>2. <b>El</b> {wl('sm')} <b>a las</b> {wl('sm')} {wl('lg')} .<br>3. Mi afspraak: ¿Quieres quedar <b>el</b> {wl('sm')} ? Quedamos <b>a las</b> {wl('sm')} en {wl('sm')} .</div>
  </div>
  <div class="modelo" style="margin-top:4mm"><b>Modelo · zo klinkt het:</b><br>
    — El lunes a las cinco juego al fútbol. El sábado por la mañana no hago nada.<br>
    — ¿Quieres quedar el sábado? — ¿A qué hora? — Quedamos a las once y media en el centro. — ¡Vale, hasta el sábado!</div>
  <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div class="truc" style="margin:0"><b>🏁 Está listo cuando…</b> dices 4 momentos con «el + día» y «a las + hora» (es la/son las correcto) y quedáis con «¿quieres quedar?», sin leer. <span class="gloss">zónder af te lezen</span></div>
    <table class="rubric"><thead><tr><th>Evaluatie</th><th style="text-align:center">🟢🟡🔴</th></tr></thead>
      <tr><td>la hora correct (es la/son las · y media)</td><td></td></tr>
      <tr><td>el + día · a las + hora correct</td><td></td></tr>
      <tr><td>quedar (afspraak maken) &amp; durf</td><td></td></tr></table>
  </div>
</div>
"""

BANDAS=[("Quevedo","Bzrp #52","🇪🇸 España"),("Rosalía","Despechá","🇪🇸 España"),("Manuel Turizo","La Bachata","🇨🇴 Colombia"),
 ("Marc Anthony","Vivir Mi Vida","🇵🇷 Puerto Rico"),("Álvaro Soler","Sofía","🇪🇸 España"),("Camilo","Vida de Rico","🇨🇴 Colombia")]
def banda(a,s,g): return f'<div class="banda"><div class="ar">{a}</div><div class="sg">🎵 {s}</div><div class="ge">{g}</div></div>'
MUSICA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Cultura · Banda sonora</div><h2>Los horarios en el mundo hispano</h2>
  <p style="font-size:9.6pt">El reloj va distinto en el mundo hispano. En <b>España</b> se come sobre las <b>14</b> y se cena a las <b>21–22</b>; en <b>México</b> la comida de las 14–15 es la principal. La <b>tarde</b> dura hasta las 20–21: por eso a las 19 todavía se dice «buenas tardes». Y los días van en <b>minúscula</b>: lunes, martes… Cada unidad tiene además su <b>banda sonora</b>. <span class="gloss">later eten, langere namiddag</span></p>
  <div class="bandas">{"".join(banda(*b) for b in BANDAS)}</div>
  <div class="musrow">
    <div class="call"><span class="ic">🎧</span><div><b>Spotify · la playlist de la clase.</b> Escanea y escucha. En la página digital tienes también <b>LyricsTraining</b> y el <b>mapa del mundo</b>. <span class="gloss">scan en luister; online staat er meer</span></div></div>
    <div class="qr" data-url="{SPOTIFY}"><div class="lab">Playlist</div>{qr(SPOTIFY)}<div class="meta">Spotify</div></div>
  </div>
  <div class="truc" style="margin-top:5mm"><b>Los horarios · ¿sabías que…?</b> Verbind (gis gerust):
    <table class="mtab" style="margin-top:1mm"><tr><td class="a">En España se come…</td><td>{wl('sm')}</td><td class="b">a. tot 20–21 u (daarna «noche»)</td></tr>
    <tr><td class="a">La «tarde» dura…</td><td>{wl('sm')}</td><td class="b">b. rond 14 u (en cenar om 21–22 u)</td></tr>
    <tr><td class="a">Los días se escriben…</td><td>{wl('sm')}</td><td class="b">c. en minúscula</td></tr></table>
    <p style="font-size:8.6pt;color:var(--mut);margin-top:1mm">💡 «Half negen» = las ocho y media: el español cuenta desde la hora anterior. Es la trampa clásica. <span class="gloss">het Spaans kijkt terug</span></p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:3mm;align-items:start">
    <div class="truc" style="margin:0"><b>Escucha y responde.</b> Kies één nummer van de playlist.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.3">Mi canción: {wl('lg')}<br>La escucho (¿cuándo?): {wl('lg')}</div>
    </div>
    <div class="truc" style="margin:0"><b>¿Y tú?</b> Escribe una frase: qué día y a qué hora haces algo. <span class="gloss">dag en uur</span>
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.4">{wl('full')}<br>{wl('full')}</div>
    </div>
  </div>
</div>
"""

REPASO=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Repaso · Lo esencial de un vistazo</div><h2>Lo que ya sabes hacer <span class="gloss">wat je nu kunt</span></h2>
  <div class="fams">
    <div class="pcard"><div class="t">Así dices qué hora es <span class="gloss">zeggen hoe laat het is</span></div><div class="ej"><b>¿Qué hora es?</b> — <b>Es la</b> una / <b>Son las</b> ocho <b>y media</b> · <b>menos cuarto</b> · <b>en punto</b>.</div><div class="t2">alleen 1 uur = enkelvoud · half negen = las ocho y media</div></div>
    <div class="pcard"><div class="t">Así quedas con alguien <span class="gloss">zo maak je een afspraak</span></div><div class="ej">¿<b>Quieres quedar el</b> sábado? — ¿<b>A qué hora</b>? — <b>Quedamos a las</b> siete.</div><div class="anchor"><b>a las</b> + uur (om…) &nbsp;|&nbsp; <b>el</b> lunes (op maandag) · <b>los</b> lunes (elke maandag)</div></div>
  </div>
  <div class="regla" style="margin:4mm 0"><span class="tag">Frases para la clase</span>
    <div class="cogn" style="margin-top:1mm"><span>¿Cómo se dice… ?</span><span>¿Qué significa… ?</span><span>Otra vez, por favor</span><span>No entiendo</span><span>¿Puedes hablar más despacio?</span><span>¿A qué hora terminamos?</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Handige klaszinnen — gebruik ze in het Spaans i.p.v. Nederlands.</span>
  </div>
  <table class="sem"><thead><tr><th style="text-align:left">Puedo… · Ik kan…</th><th>🟢</th><th>🟡</th><th>🔴</th></tr></thead>
    <tr><td>de tijd zeggen (es la una · son las ocho y media)</td><td></td><td></td><td></td></tr>
    <tr><td>y cuarto · y media · menos cuarto gebruiken</td><td></td><td></td><td></td></tr>
    <tr><td>de dagen zeggen (el lunes · los lunes)</td><td></td><td></td><td></td></tr>
    <tr><td>een afspraak maken (¿quieres quedar? · a las…)</td><td></td><td></td><td></td></tr></table>
  <div class="regla" style="margin-top:5mm"><span class="tag">Mini-test · recuerda sin mirar</span>
    <p style="margin:1mm 0 0;font-size:9.4pt">Cierra el libro y traduce de memoria: recordar es la mejor manera de aprender. <span class="gloss">uit het hoofd — ophalen leert het best</span></p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3mm 8mm;margin-top:2mm;font-size:9.8pt;line-height:2.2">
      <div>1. ¿qué hora es? → {wl('')}</div><div>2. het is één uur → {wl('')}</div>
      <div>3. half negen → {wl('')}</div><div>4. kwart voor vier → {wl('')}</div>
      <div>5. om zeven uur → {wl('')}</div><div>6. wil je zaterdag afspreken? → {wl('')}</div>
    </div>
  </div>
  <div class="guide"><span class="ic">🎮</span><div><span class="hand">Repasa jugando</span><div class="g">Oefen alles online met spelletjes, flashcards en audio op de digitale hub (scan de QR bij §1).</div></div></div>
  <div class="bridge"><b>Próxima parada →</b> In de volgende unit: <i>planes y obligaciones</i> (¿qué quieres hacer?). ¡Hasta pronto!</div>
</div>
"""

EDITBAR="""
<div class="editbar" id="eb">
  <b>✏️ C4 · U8</b>
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
document.getElementById('btnsave').onclick=function(){var html='<!doctype html>'+document.documentElement.outerHTML;var b=new Blob([html],{type:'text/html'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='C4_U8_Horas_bewerkt.html';a.click();};
</script>
"""

HTML=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 8 · La hora y los días</title><style>{CSS}</style></head><body class="c4">
{EDITBAR}
{HERO}{ESCUCHA}{COMPR_SEC}{KIT}{GRAM}{PRAC}{TAREA}{MUSICA}{FUNCIONES_SEC}{REPASO}
{SCRIPT}
</body></html>"""
os.makedirs(f"{ROOT}/03-build/web/print",exist_ok=True)
open(f"{ROOT}/03-build/web/print/C4_U8.html","w",encoding="utf-8").write(HTML)
print("C4_U8.html (print+editable) geschreven:",len(HTML),"bytes")
