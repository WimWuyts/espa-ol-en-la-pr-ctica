#!/usr/bin/env python3
# C4 · Unidad 5 — PRINT (HTML=bron → PDF via Chromium). Golden-sample print-kit, C4-rood.
# Thema: Objetos cotidianos · identificar (¿qué es esto?) · hay · para qué sirve (un/una · género). Zelfde pijplijn als U1–U4.
import base64, os, re, io, sys
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
from funciones_print import print_section
FUNCIONES_SEC=print_section(5)
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
HUB_URL=EN.url("C4", 5)
import comprension_print
COMPR_SEC=comprension_print.print_section(5, HUB_URL)
SPOTIFY="https://open.spotify.com/playlist/37i9dQZF1DXaxEKcoCdWHD"

SCENES=[
 ("Escena 1 · La casa de Julio",[
  ("María","¡Qué!"),
  ("Julio","Esto son mis llaves, que sirven para abrir la puerta."),
  ("María","Muy bien."),
  ("Julio","Y esto son dos botellas de vino, que sirven para estar contentos."),
  ("María","¿Qué es esto?"),
  ("Julio","Esto es un sofá, que sirve para descansar."),
  ("Julio","Y eso es una televisión. Y eso es un libro, y un vaso que sirve para beber."),
  ("Julio","Ahí está la cocina, y ahí está el cuarto de baño."),
  ("Julio","Y esto es una ventana, que sirve para mirar la luna y las estrellas."),
 ]),
 ("Escena 2 · ¿Hay un ordenador?",[
  ("María","¿Éstas son las llaves?"),
  ("Julio","Las de la puerta de casa, sí."),
  ("María","Y ordenador, ¿hay un ordenador?"),
  ("Julio","No, no hay un ordenador. Perdóname, sí que hay un ordenador."),
 ]),
]
CH=["¿Qué es esto?","Esto son","Esto es un","que sirve para","que sirven para","un sofá","una televisión","un libro","un vaso","la cocina","el cuarto de baño","una ventana","las llaves","hay un ordenador","no hay","sí que hay","la puerta","descansar","beber"]
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
 ("Objetos de la clase",[("el libro · el cuaderno","het boek · het schrift"),("el boli · el lápiz","de pen · het potlood"),
   ("la mochila","de rugzak"),("la mesa · la silla","de tafel · de stoel"),("el móvil","de gsm")]),
 ("Objetos de casa",[("el sofá","de bank"),("la televisión","de tv"),("la ventana · la puerta","het raam · de deur"),
   ("el ordenador","de computer"),("las llaves","de sleutels"),("el vaso","het glas")]),
 ("Identificar · ¿qué es esto?",[("¿Qué es esto?","Wat is dit?"),("Esto es un/una…","Dit is een…"),
   ("Esto son…","Dit zijn…"),("un libro · una mesa","een boek · een tafel")]),
 ("¿Para qué sirve?",[("¿Para qué sirve?","Waarvoor dient het?"),("Sirve para + inf.","Het dient om te…"),
   ("para abrir · beber","om te openen · drinken"),("para descansar · estudiar","om te rusten · studeren")]),
 ("¿Qué hay?",[("¿Hay…?","Is/zijn er…?"),("(No) hay…","Er is (geen)…"),("Sí que hay…","Jawel, er is…"),
   ("aquí · ahí","hier · daar")]),
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
.p{color:#2563EB;font-weight:700}.v{color:#EA7317;font-weight:700}.o{color:#1E9E74;font-weight:700}.pl{color:#0E9E97;font-weight:700}
.tl{display:flex;gap:3mm;padding:.55mm 0;font-size:9.5pt;break-inside:avoid}
.tl .sp{font-family:var(--disp);font-weight:700;color:var(--gd);width:22mm;flex:none}
.tl .tx b{background:var(--gt);border-radius:3pt;padding:.2mm 1.2mm;font-weight:700}
.twocol{column-count:2;column-gap:8mm}
.kitwrap{display:grid;grid-template-columns:1fr 1fr;gap:3mm 5mm;margin-top:2mm}
.kit{break-inside:avoid}
.kit-h{font-family:var(--disp);font-weight:700;font-size:9.6pt;color:var(--gd);margin:1mm 0 .5mm}
.ktab{font-size:8.8pt;width:100%}.ktab th{background:var(--gt);color:var(--gd);font-size:7.2pt;text-transform:uppercase;padding:.8mm 2mm;text-align:left}
.ktab td{border-bottom:1px solid var(--line);padding:.55mm 2mm}.k-es{font-weight:600}.k-ck{text-align:center;width:12mm}
.chk{display:inline-block;width:3.4mm;height:3.4mm;border:1.3px solid var(--mut);border-radius:1.5pt;vertical-align:middle}
.gt2{width:100%;font-size:9.2pt;margin:2mm 0}.gt2 td{border-bottom:1px solid var(--line);padding:1.5mm 2.5mm}
.gt2 .v{color:#EA7317;font-family:var(--disp)}.gt2 .ex{color:var(--mut);font-style:italic}
.mv2{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin:2mm 0}
.mv2 div{border-radius:8pt;padding:2.5mm 4mm;font-family:var(--disp)}
.mv2 .m{background:#E8F0FE;color:#1E40AF}.mv2 .f{background:#FCE7F0;color:#9D174D}
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
.objgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm;margin:2mm 0}
.objcard{border:1px solid var(--line);border-radius:8pt;padding:2.5mm 3mm;break-inside:avoid;text-align:center}
.objcard .em{font-size:20pt}.objcard .lb{font-size:7.6pt;color:var(--mut);margin-top:1mm}.objcard .wl{min-width:0;width:100%;margin-top:1mm}
.editbar{position:fixed;top:0;left:0;right:0;background:var(--gd);color:#fff;display:flex;gap:8px;align-items:center;padding:7px 12px;z-index:999;font-family:var(--body);font-size:13px;box-shadow:0 2px 10px #0003}
.editbar b{font-family:var(--disp)}.editbar button{border:0;background:#fff;color:var(--gd);font-weight:700;border-radius:8px;padding:6px 11px;cursor:pointer;font-size:12.5px}
.editbar button.on{background:#111;color:#fff}.editbar .sp{flex:1}.scr-spacer{height:44px}
body.editing .page{outline:1.5px dashed var(--g);outline-offset:-6px}
@media print{ .editbar,.scr-spacer{display:none!important} }
"""

HERO=f"""
<section class="hero">
  <div class="tab">C4 · LA RUTA</div>
  <div class="eyebrow">EL DESPEGUE · PARADA 5 · SURVIVAL IN SPANISH</div>
  <h1>Objetos cotidianos</h1>
  <div class="sub">Voorwerpen <b>benoemen</b> en zeggen waarvoor ze <b>dienen</b>. <span class="gloss">Identificar objetos y decir para qué sirven — ¿qué es esto? · esto es un… · sirve para…</span></div>
  <div class="q">¿Qué es esto? — Esto es un sofá, que sirve para descansar.</div>
</section>
<div class="page">
  <div class="obj"><div class="se">Al final de esta unidad · Op het einde van deze les</div>
    <ul>
      <li><span class="ck">✓</span> <span><span class="es">Identificar objetos</span> <span class="nl">— ¿qué es esto? · esto es un/una… · esto son…</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Usar <b>un/una</b> y el género</span> <span class="nl">— un libro · una mesa · el / la</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Decir qué <b>hay</b></span> <span class="nl">— hay · no hay · ¿hay…? · sí que hay</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Decir para qué <b>sirve</b></span> <span class="nl">— sirve para + infinitivo (beber, descansar…)</span></span></li>
    </ul>
  </div>
  <div class="guide"><span class="ic">🎒</span><div><span class="hand">¡Seguimos la ruta! Parada 5.</span><div class="g">In deze «survival»-les leer je alles om je heen benoemen. In de video toont Julio zijn huis aan María en zegt bij elk voorwerp waarvoor het dient — perfecte input voor «esto es un… que sirve para…».</div></div></div>

  <div class="se" style="margin-top:6mm">La gente de la ruta · je reisgenoten</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Je reist mee met vier jongeren uit de Spaanstalige wereld. In de scène ben je te gast bij Julio thuis, samen met María.</p>
  <div class="cast2">
    <div class="m"><div class="fl">🇪🇸</div><div class="nm">Lucía</div><div class="ro">Sevilla · familie</div></div>
    <div class="m"><div class="fl">🇲🇽</div><div class="nm">Diego</div><div class="ro">CDMX · eten & markt</div></div>
    <div class="m"><div class="fl">🇨🇴</div><div class="nm">Valen</div><div class="ro">Cartagena · wonen</div></div>
    <div class="m"><div class="fl">🇵🇪</div><div class="nm">Nina</div><div class="ro">Cusco · reizen</div></div>
    <div class="m"><div class="fl">🎒</div><div class="nm">Tú</div><div class="ro">jij, de reiziger</div></div>
  </div>

  <div class="truc" style="margin-top:5mm"><b>¿Qué reconoces ya?</b> Deze voorwerpen lijken op het Nederlands of Engels (<i>palabras transparentes</i>) — durf te gissen:
    <div class="cogn"><span>el sofá</span><span>la televisión</span><span>el ordenador</span><span>la radio</span><span>el móvil</span><span>la foto</span><span>el vídeo</span><span>la guitarra</span><span>la pizza</span><span>el chocolate</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Tip: veel voorwerpen herken je meteen — <b>televisión</b>, <b>radio</b>, <b>móvil</b>…</span>
  </div>
</div>
"""

ESCUCHA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§1 · ¡Escucha!</div><h2>Bekijk de scène en lees mee</h2>
  <div class="audiorow">
    <div class="call"><span class="ic">🎬</span><div><b>Sitcom · Episodio 5 · Objetos cotidianos.</b> Scan de code en bekijk de aflevering op de digitale pagina. Julio toont María zijn huis en zegt bij elk voorwerp <b>waarvoor het dient</b>. Luister eerst zónder te lezen; daarna lees je mee. De <b>vetgedrukte</b> woorden zijn chunks om mee te nemen.</div></div>
    <div class="qr" data-url="{EN.url('C4', 5, EN.ancla_c4('escucha'))}"><div class="lab">Vídeo online</div>{qr(EN.url("C4", 5, EN.ancla_c4("escucha")))}<div class="meta">hub · Escucha</div></div>
  </div>
  <div class="truc"><b>Antes de escuchar · vóór je luistert.</b> Welke <b>voorwerpen</b> in een huis ga je horen, denk je? <span style="font-size:8.8pt;color:var(--mut)">(gis gerust)</span>
    <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.2">Un objeto: {wl('sm')} &nbsp;&nbsp; Otro objeto: {wl('sm')} &nbsp;&nbsp; ¿Para qué sirve? {wl('sm')}</div>
  </div>
  <div class="twocol">{scenehtml(*SCENES[0])}{scenehtml(*SCENES[1])}</div>
  <div class="ojo"><b>¡Ojo!</b> «Esto <b>es</b> un sofá» (één ding) maar «Esto <b>son</b> mis llaves» (meer dingen). En <b>hay</b> verandert nooit: hay un vaso, hay dos botellas.</div>

  <div class="se" style="margin-top:5mm">Después de escuchar · ¿Verdadero o falso?</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Kruis aan. Verbeter de <b>falsas</b> op de lijn.</p>
  <table class="vf">
    <tr><td>1. Las llaves sirven para abrir la puerta.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>2. El sofá sirve para beber.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>3. La ventana sirve para mirar la luna y las estrellas.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>4. Al final, sí que hay un ordenador.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
  </table>
</div>
"""

KIT=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Suena bien · pronunciación</div><h2>La r suave, la rr fuerte &amp; la tilde</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 1mm">Tussen klinkers is de <b>r</b> zacht (één tikje): «pe-ro», «ca-ra». De <b>rr</b> (en de begin-r) rolt sterk: «pe-rro», «rojo». Oefen online (QR §1).</p>
  <div class="cogn"><span>pero</span><span>cara</span><span>para</span><span>ahora</span><span>mira</span><span>hora</span></div>
  <div class="ojo"><b>¡Ojo!</b> pe<b>r</b>o (maar) ≠ pe<b>rr</b>o (hond)! De dubbele r verandert de <b>betekenis</b>. Rol de rr: <b>rr</b>ojo, guita<b>rr</b>a, <b>r</b>atón.</div>
  <div class="cogn"><span>perro</span><span>rojo</span><span>guitarra</span><span>rosa</span><span>arriba</span><span>ratón</span></div>
  <div class="klemline"><b>La tilde · het accent staat op de sterkste lettergreep:</b> so·<span class="t">FÁ</span> · te·le·vi·<span class="t">SIÓN</span> · <span class="t">MÚ</span>·si·ca · bo·<span class="t">LÍ</span>·gra·fo</div>

  <div class="se" style="margin-top:3mm">§2 · Kit de supervivencia</div><h2>De taal die je écht nodig hebt</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 2mm">Vink ☐ af telkens je een uitdrukking vlot kunt <b>naspreken</b>. Oefen ze online met audio.</p>
  <div class="kitwrap">{"".join(kittable(n,it) for n,it in CLUSTERS)}</div>
</div>
"""

GRAM=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§4 · Gramática en la práctica</div><h2>Kort en functioneel</h2>
  <div class="modelo"><b>🔎 Fíjate · kijk terug naar de scène.</b> Je hoorde het al: «¿Qué <b>es</b> esto? — Esto es <b>un</b> sofá, que <b>sirve para</b> descansar» · «¿<b>Hay</b> un ordenador? — No <b>hay</b>… sí que <b>hay</b>». Ontdek zelf het patroon — <i>eerst betekenis, dan de regel.</i></div>
  <div class="regla"><span class="tag">un · una · el · la — género (♂/♀)</span>
    <p style="font-size:9pt;margin:0 0 1mm">Elk voorwerp is ♂ of ♀. Meestal: <b>-o = ♂</b> (un libr<b>o</b>), <b>-a = ♀</b> (una mes<b>a</b>).</p>
    <div class="mv2"><div class="m">♂ masculino: <b>un</b> libro · <b>un</b> vaso · <b>el</b> boli · <b>el</b> ordenador</div><div class="f">♀ femenino: <b>una</b> mesa · <b>una</b> silla · <b>la</b> ventana · <b>la</b> mochila</div></div>
    <p style="font-size:9pt;margin:1mm 0 0">⚠️ Uitzonderingen leer je er gewoon bij: <b>el</b> sofá, <b>la</b> televisión, <b>el</b> día, <b>la</b> mano.</p>
  </div>
  <div class="regla"><span class="tag">¿Qué es esto? · esto es… / esto son…</span>
    <table class="gt2"><tr><td class="v">¿Qué es esto/eso?</td><td>wat is dit/dat?</td><td class="ex">Esto <b>es</b> un libro. (één)</td></tr>
    <tr><td class="v">Esto son…</td><td>dit zijn…</td><td class="ex">Esto <b>son</b> las llaves. (meer)</td></tr></table>
    <p style="font-size:9pt;margin:1mm 0 0">💡 <b>esto</b> = dit · <b>eso</b> = dat. Eén ding → «es»; meer dingen → «son».</p>
  </div>
  <div class="regla"><span class="tag">hay · er is / er zijn (verandert nooit)</span>
    <table class="gt2"><tr><td class="v">Hay…</td><td>er is / er zijn</td><td class="ex"><b>Hay</b> un sofá y dos sillas.</td></tr>
    <tr><td class="v">¿Hay…?</td><td>is/zijn er…?</td><td class="ex">¿<b>Hay</b> un ordenador?</td></tr>
    <tr><td class="v">No hay…</td><td>er is geen…</td><td class="ex"><b>No hay</b> televisión.</td></tr></table>
  </div>
  <div class="regla"><span class="tag">… que sirve para + infinitivo</span>
    <p style="margin:1mm 0 0;font-size:9.6pt">Waarvoor iets dient: <b>sirve para</b> + hele werkwoord. «un vaso que <b>sirve para</b> beber», «un sofá que <b>sirve para</b> descansar». Meer dingen: «que <b>sirven</b> para…».</p>
  </div>
  <div class="truc"><b>Mini-oefening 1 · un/una + es/son.</b> Vul un/una in bij de voorwerpen, en kies es of son bij de zinnen:
    <div style="margin-top:2mm;font-size:9.6pt;line-height:2.4">1. {wl('sm')} libro &nbsp; 2. {wl('sm')} mesa &nbsp; 3. {wl('sm')} silla &nbsp; 4. {wl('sm')} vaso &nbsp;|&nbsp; a) Esto {wl('sm')} un libro. &nbsp; b) Esto {wl('sm')} mis llaves.</div>
  </div>
  <div class="truc"><b>Mini-oefening 2 · sirve para…</b> Verbind (el vaso · la ventana · el sofá → beber · mirar · descansar) en schrijf één zin: ✍️ Un {wl('lg')} sirve para {wl('lg')} .</div>
</div>
"""

def act(n,title,badges,body):
    bh="".join(f'<span class="badge {c}">{t}</span>' for t,c in badges)
    return (f'<div class="act"><div class="acthead"><div class="anum">{n}</div><div><div class="h">{title}</div>'
            f'<div class="badges">{bh}</div></div></div>{body}</div>')

PRAC=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§3 · Práctica</div><h2>Oefen op papier — online verbeter je alles</h2>

  {act(1,"Clasifica: clase, casa o función",[("receptief","skill"),("5 min","")],
    '<p style="margin-left:12.5mm">Schrijf elk woord in de juiste kolom. Voeg onderaan één eigen woord toe.<br><span class="gloss">el boli · el sofá · beber · la mochila · la televisión · descansar · el cuaderno · las llaves</span></p>'
    +'<div class="wcols" style="margin-left:12.5mm"><div class="wcol"><h4>De la clase 📚</h4><div class="fill"></div></div><div class="wcol"><h4>De casa 🏠</h4><div class="fill"></div></div><div class="wcol"><h4>Función 🔧</h4><div class="fill"></div></div><div class="wcol"><h4>Tu palabra</h4><div class="fill"></div></div></div>')}

  {act(2,"Relaciona · ¿para qué sirve?",[("gestuurd","skill"),("★☆☆","")],
    '<p style="margin-left:12.5mm">Trek een lijn tussen het voorwerp en waarvoor het dient.</p>'
    +'<table class="mtab" style="margin-left:12.5mm"><tr><td class="a">1. las llaves</td><td><span class="ln"></span></td><td class="b">a. para beber</td></tr>'
    +'<tr><td class="a">2. el vaso</td><td><span class="ln"></span></td><td class="b">b. para abrir la puerta</td></tr>'
    +'<tr><td class="a">3. el sofá</td><td><span class="ln"></span></td><td class="b">c. para mirar la luna</td></tr>'
    +'<tr><td class="a">4. la ventana</td><td><span class="ln"></span></td><td class="b">d. para descansar</td></tr>'
    +'<tr><td class="a">5. el ordenador</td><td><span class="ln"></span></td><td class="b">e. para trabajar y jugar</td></tr></table>')}

  {act(3,"Completa el diálogo",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Vul aan (es/son · un/una · sirve · hay).</p>'
    +f'<div style="margin-left:12.5mm;font-size:10pt;line-height:2.5">'
    +f'— ¿Qué es esto?<br>— Esto {wl("sm")} {wl("sm")} sofá. {wl("sm")} para descansar.<br>— ¿Y esto?<br>— Esto {wl("sm")} mis llaves.<br>— ¿{wl("sm")} un ordenador?<br>— Sí, sí que hay.</div>')}

  {act(4,"Ordena la conversación",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Nummer de zinnen in de juiste volgorde (1–5).</p>'
    +'<div class="scramble" style="margin-left:12.5mm"><span>___ Sirve para beber.</span><span>___ ¿Qué es esto?</span><span>___ ¿Y hay un ordenador?</span><span>___ Esto es un vaso.</span><span>___ Sí, sí que hay.</span></div>')}

  {act(5,"El género · ¿un o una?",[("gestuurd","skill"),("★☆☆","")],
    f'<p style="margin-left:12.5mm">Vul un of una in (♂ -o / ♀ -a; let op de uitzonderingen).</p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. {wl("sm")} libro &nbsp; 2. {wl("sm")} silla &nbsp; 3. {wl("sm")} ventana &nbsp; 4. {wl("sm")} vaso &nbsp; 5. {wl("sm")} mochila &nbsp; 6. {wl("sm")} sofá</div>')}

  {act(6,"Mi habitación · ¿qué hay?",[("productie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Teken 6 voorwerpen uit je kamer en benoem ze met un/una.</p>'
    +'<div class="objgrid" style="margin-left:12.5mm"><div class="objcard"><div class="em">🛏️</div><span class="wl"></span></div><div class="objcard"><div class="em">📚</div><span class="wl"></span></div><div class="objcard"><div class="em">🪑</div><span class="wl"></span></div><div class="objcard"><div class="em">💻</div><span class="wl"></span></div><div class="objcard"><div class="em">🎒</div><span class="wl"></span></div><div class="objcard"><div class="em">🪟</div><span class="wl"></span></div></div>')}

  {act(7,"Describe 2 objetos",[("productie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Schrijf voor 2 voorwerpen: «Esto es un/una ___, que sirve para ___.» (2 zinnen).</p>'
    +'<div class="wbox" style="margin-left:12.5mm"></div>')}

  {act(8,"Entrevista · ¿qué hay en tu mochila?",[("interactie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Vraag je buur wat er in zijn/haar tas of kamer is en noteer. Wissel van rol. Sluit af met «¿Qué es esto?» over 2 voorwerpen.</p>'
    +f'<table class="wtab" style="margin-left:12.5mm;margin-top:2mm"><thead><tr><th style="width:45mm">Pregunta</th><th>Respuesta</th></tr></thead>'
    +'<tr><td style="height:12mm">¿Qué hay en tu mochila?</td><td></td></tr>'
    +'<tr><td style="height:12mm">¿Para qué sirve?</td><td></td></tr>'
    +'<tr><td style="height:12mm">¿Qué es esto? (🛋️ 📺 🔑 🪟)</td><td></td></tr></table>')}
</div>
"""

TAREA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§5 · Tarea final</div><h2>Diccionario de la clase</h2>
  <div class="esen" style="margin-top:2mm"><b class="tt">Jouw opdracht.</b> Maak een <b>mini-woordenboek</b> van <b>5 voorwerpen</b> (uit de klas of van thuis). Teken elk, benoem het met <b>un/una</b> («esto es…») en zeg waarvoor het <b>dient</b> («sirve para…»). Presenteer je woordenboek aan de klas. <span class="gloss">Sin leer del papel — zonder van het blad af te lezen.</span></div>
  <div class="regla" style="margin-top:4mm"><span class="tag">Prepárate · vul eerst de frames in</span>
    <div style="margin-top:2mm;font-size:9.7pt;line-height:2.4">1. Esto es {wl('sm')} {wl('sm')} , que sirve para {wl('sm')} .<br>2. Esto es {wl('sm')} {wl('sm')} , que sirve para {wl('sm')} .<br>3. Esto son {wl('sm')} , que sirven para {wl('sm')} .</div>
  </div>
  <div class="modelo" style="margin-top:4mm"><b>Modelo · zo klinkt het:</b><br>
    — Esto es un boli, que sirve para escribir.<br>
    — Esto son mis llaves, que sirven para abrir la puerta.</div>
  <div style="margin-top:4mm"><div class="se">Mi diccionario · teken hier 5 voorwerpen + noteer per voorwerp</div>
    <div class="objgrid" style="margin-top:2mm"><div class="objcard" style="min-height:30mm"><div class="lb">1 · Esto es…</div></div><div class="objcard" style="min-height:30mm"><div class="lb">2 · Esto es…</div></div><div class="objcard" style="min-height:30mm"><div class="lb">3 · Esto es…</div></div><div class="objcard" style="min-height:30mm"><div class="lb">4 · Esto es…</div></div><div class="objcard" style="min-height:30mm"><div class="lb">5 · Esto son…</div></div><div class="objcard" style="min-height:30mm"><div class="lb">+ · sirve para…</div></div></div>
  </div>
  <div class="regla" style="margin-top:3mm"><span class="tag">Palabras y frases útiles</span>
    <p style="margin:1mm 0 0;font-size:9.6pt">un/una · el/la · Esto es… · Esto son… · ¿qué es esto? · sirve para + infinitivo (abrir · beber · descansar · estudiar · escribir · mirar) · hay · no hay</p>
  </div>
  <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div class="truc" style="margin:0"><b>🏁 Klaar als…</b> je 5 voorwerpen benoemt met «esto es un/una…» (juiste ♂/♀) en per voorwerp zegt «sirve para + werkwoord» — zónder af te lezen.</div>
    <table class="rubric"><thead><tr><th>Evaluatie</th><th style="text-align:center">🟢🟡🔴</th></tr></thead>
      <tr><td>identificar (esto es un/una…) correct</td><td></td></tr>
      <tr><td>sirve para + infinitivo correct</td><td></td></tr>
      <tr><td>uitspraak &amp; durf</td><td></td></tr></table>
  </div>
</div>
"""

BANDAS=[("Rosalía","Despechá","🇪🇸 España"),("Bad Bunny","Tití Me Preguntó","🇵🇷 Puerto Rico"),("Shakira","Bzrp Session 53","🇨🇴 Colombia"),
 ("Karol G","Provenza","🇨🇴 Colombia"),("Manu Chao","Me Gustas Tú","🇪🇸/🇫🇷"),("Quevedo","Columbia","🇪🇸 España")]
def banda(a,s,g): return f'<div class="banda"><div class="ar">{a}</div><div class="sg">🎵 {s}</div><div class="ge">{g}</div></div>'
MUSICA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Cultura · Banda sonora</div><h2>Objetos con historia en el mundo hispano</h2>
  <p style="font-size:9.6pt">Sommige <b>voorwerpen</b> zijn echte iconen van de Spaanstalige cultuur: de <b>guitarra española</b>, de <b>maraca</b> uit de Caraïben, de <b>mate</b>-beker uit Argentinië en de kleurrijke <b>hamaca</b> (hangmat) uit Latijns-Amerika. En elke unit heeft een <b>banda sonora</b>.</p>
  <div class="bandas">{"".join(banda(*b) for b in BANDAS)}</div>
  <div class="musrow">
    <div class="call"><span class="ic">🎧</span><div><b>Spotify · la playlist de la clase.</b> Scan en luister. Op de digitale pagina vind je ook <b>LyricsTraining</b> en de <b>wereldkaart</b>.</div></div>
    <div class="qr" data-url="{SPOTIFY}"><div class="lab">Playlist</div>{qr(SPOTIFY)}<div class="meta">Spotify</div></div>
  </div>
  <div class="truc" style="margin-top:5mm"><b>Objetos típicos · ¿de dónde son?</b> Verbind (gis gerust):
    <table class="mtab" style="margin-top:1mm"><tr><td class="a">El mate…</td><td>{wl('sm')}</td><td class="b">a. una guitarra flamenca de España</td></tr>
    <tr><td class="a">La guitarra española…</td><td>{wl('sm')}</td><td class="b">b. una bebida típica de Argentina</td></tr>
    <tr><td class="a">La hamaca…</td><td>{wl('sm')}</td><td class="b">c. para descansar en el Caribe</td></tr></table>
    <p style="font-size:8.6pt;color:var(--mut);margin-top:1mm">💡 «Sirve para…» werkt ook voor cultuur: el mate sirve para compartir con amigos.</p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:3mm;align-items:start">
    <div class="truc" style="margin:0"><b>Escucha y responde.</b> Kies één nummer van de playlist.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.3">Mi canción: {wl('lg')}<br>El/la artista es de: {wl('lg')}</div>
    </div>
    <div class="truc" style="margin:0"><b>¿Y en tu casa?</b> Schrijf één voorwerp uit je kamer + waarvoor het dient.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.4">{wl('full')}<br>{wl('full')}</div>
    </div>
  </div>
</div>
"""

REPASO=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Repaso · Lo esencial de un vistazo</div><h2>Wat je nu kunt</h2>
  <div class="fams">
    <div class="pcard"><div class="t">Zo benoem je een voorwerp</div><div class="ej"><b>¿Qué es esto?</b> — Esto <b>es un/una</b> ____. / Esto <b>son</b> ____.</div><div class="t2">un/el = ♂ · una/la = ♀ · es (één) · son (meer)</div></div>
    <div class="pcard"><div class="t">Zo zeg je wat er is / waarvoor</div><div class="ej"><b>Hay</b> ____. / <b>No hay</b> ____. · Sirve <b>para</b> + infinitivo.</div><div class="anchor"><b>hay</b> verandert nooit &nbsp;|&nbsp; para + hele werkwoord (beber, descansar)</div></div>
  </div>
  <div class="regla" style="margin:4mm 0"><span class="tag">Frases para la clase</span>
    <div class="cogn" style="margin-top:1mm"><span>¿Cómo se dice… ?</span><span>¿Qué significa… ?</span><span>Otra vez, por favor</span><span>No entiendo</span><span>¿Puedes repetir?</span><span>Más despacio, por favor</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Handige klaszinnen — gebruik ze in het Spaans i.p.v. Nederlands.</span>
  </div>
  <table class="sem"><thead><tr><th style="text-align:left">Puedo… · Ik kan…</th><th>🟢</th><th>🟡</th><th>🔴</th></tr></thead>
    <tr><td>voorwerpen benoemen (¿qué es esto? · esto es un/una…)</td><td></td><td></td><td></td></tr>
    <tr><td>un/una en el/la juist gebruiken (género)</td><td></td><td></td><td></td></tr>
    <tr><td>zeggen wat er is (hay · no hay · ¿hay…?)</td><td></td><td></td><td></td></tr>
    <tr><td>zeggen waarvoor iets dient (sirve para + inf.)</td><td></td><td></td><td></td></tr></table>
  <div class="regla" style="margin-top:5mm"><span class="tag">Mini-test · recuerda sin mirar</span>
    <p style="margin:1mm 0 0;font-size:9.4pt">Sluit de cursus en vertaal uit het hoofd (ophalen = het beste leren).</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3mm 8mm;margin-top:2mm;font-size:9.8pt;line-height:2.2">
      <div>1. wat is dit? → {wl('')}</div><div>2. dit is een boek → {wl('')}</div>
      <div>3. er is een bank → {wl('')}</div><div>4. er is geen tv → {wl('')}</div>
      <div>5. het dient om te drinken → {wl('')}</div><div>6. dit zijn mijn sleutels → {wl('')}</div>
    </div>
  </div>
  <div class="guide"><span class="ic">🎮</span><div><span class="hand">Repasa jugando</span><div class="g">Oefen alles online met spelletjes, flashcards en audio op de digitale hub (scan de QR bij §1).</div></div></div>
  <div class="bridge"><b>Próxima parada →</b> In de volgende unit: <i>de compras / la comida</i>. ¡Hasta pronto!</div>
</div>
"""

EDITBAR="""
<div class="editbar" id="eb">
  <b>✏️ C4 · U5</b>
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
document.getElementById('btnsave').onclick=function(){var html='<!doctype html>'+document.documentElement.outerHTML;var b=new Blob([html],{type:'text/html'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='C4_U5_Objetos_bewerkt.html';a.click();};
</script>
"""

HTML=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 5 · Objetos cotidianos</title><style>{CSS}</style></head><body class="c4">
{EDITBAR}
{HERO}{ESCUCHA}{COMPR_SEC}{KIT}{GRAM}{PRAC}{TAREA}{MUSICA}{FUNCIONES_SEC}{REPASO}
{SCRIPT}
</body></html>"""
os.makedirs(f"{ROOT}/03-build/web/print",exist_ok=True)
open(f"{ROOT}/03-build/web/print/C4_U5.html","w",encoding="utf-8").write(HTML)
print("C4_U5.html (print+editable) geschreven:",len(HTML),"bytes")
