#!/usr/bin/env python3
# C4 · Unidad 7 — PRINT (HTML=bron → PDF via Chromium). Golden-sample print-kit, C4-rood.
# Thema: Las profesiones · ¿a qué te dedicas? · ser+profesión (sin un/una) · ser vs estar · trabajo/trabajas/trabaja. Zelfde pijplijn als U1–U6.
import base64, os, re, io, sys
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
from funciones_print import print_section
FUNCIONES_SEC=print_section(7)
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
HUB_URL=EN.url("C4", 7)
import comprension_print
COMPR_SEC=comprension_print.print_section(7, HUB_URL)
SPOTIFY="https://open.spotify.com/playlist/37i9dQZF1DXaxEKcoCdWHD"

SCENES=[
 ("Escena 1 · Trabajamos aquí",[
  ("Fernando","Yo trabajo aquí, tú trabajas aquí y él trabaja aquí."),
  ("María","Está todo bien, de verdad. Yo estoy bien. Él está bien. Estamos todos bien."),
  ("Fernando","Yo os veo… Si tú entras, él sale. No estáis bien."),
  ("María","De verdad, estamos bien. Puede parecer un poco raro."),
 ]),
 ("Escena 2 · Josefina lee las cartas",[
  ("Josefina","Silencio. Hay una mujer. Puede ser escritora."),
  ("Julio","No, no es escritora."),
  ("Josefina","Pero… dependienta. ¿Trabaja en una tienda?"),
  ("Josefina","¡Ya lo sé! Es una actriz."),
  ("Julio","Si es la que creo, es profesora."),
  ("Josefina","Es María, la nueva. Tú no estás bien, estás muy mal."),
 ]),
 ("Escenas 3–4 · ¡Qué tranquilidad!",[
  ("Fernando","Si tú estás tranquila, yo estoy tranquilo."),
  ("María","Él está tranquilo también."),
  ("Fernando","Entonces estamos todos tranquilos. ¡Qué tranquilidad!"),
  ("Josefina","Coge una carta. ¡Silencio! Hay un hombre."),
 ]),
]
CH=["Yo trabajo aquí","tú trabajas","él trabaja","Estamos todos bien","No estáis bien","escritora","dependienta","¿Trabaja en una tienda?","una actriz","es profesora","Puede ser","¡Ya lo sé!","estás muy mal","estoy tranquilo","tranquila","Estamos todos tranquilos","Hay una mujer","Hay un hombre"]
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
 ("Las profesiones",[("el profesor · la profesora","leraar · lerares"),("el escritor · la escritora","schrijver · schrijfster"),
   ("el actor · la actriz","acteur · actrice"),("el dependiente · la dependienta","winkelbediende"),
   ("el/la estudiante","student(e)"),("el médico · la médica","dokter")]),
 ("Los lugares de trabajo",[("la academia · la escuela","de (taal)school"),("la tienda","de winkel"),
   ("la oficina","het kantoor"),("el hospital","het ziekenhuis"),("el teatro","het theater")]),
 ("Preguntar por el trabajo",[("¿A qué te dedicas?","Wat doe je (voor werk)?"),("¿En qué trabajas?","Waarin werk je?"),
   ("¿Dónde trabajas?","Waar werk je?"),("¿Trabaja en una tienda?","Werkt hij/zij in een winkel?")]),
 ("Decir el trabajo",[("Soy profesor/a","Ik ben leraar/lerares"),("Trabajo en una oficina","Ik werk op kantoor"),
   ("Soy estudiante","Ik ben student(e)"),("trabajo · trabajas · trabaja","ik/jij/hij-zij werk(t)")]),
 ("¿Cómo estamos?",[("Estoy bien · tranquilo/a","Ik ben oké · rustig"),("Estamos todos bien","We zijn allemaal oké"),
   ("¿Estáis bien?","Zijn jullie oké?"),("Estás muy mal","Jij bent er erg aan toe")]),
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
.mv2 .m{background:#E8F0FE;color:#1E40AF}.mv2 .f{background:#FEF1E7;color:#B4530E}
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
.editbar{position:fixed;top:0;left:0;right:0;background:var(--gd);color:#fff;display:flex;gap:8px;align-items:center;padding:7px 12px;z-index:999;font-family:var(--body);font-size:13px;box-shadow:0 2px 10px #0003}
.editbar b{font-family:var(--disp)}.editbar button{border:0;background:#fff;color:var(--gd);font-weight:700;border-radius:8px;padding:6px 11px;cursor:pointer;font-size:12.5px}
.editbar button.on{background:#111;color:#fff}.editbar .sp{flex:1}.scr-spacer{height:44px}
body.editing .page{outline:1.5px dashed var(--g);outline-offset:-6px}
@media print{ .editbar,.scr-spacer{display:none!important} }
"""

HERO=f"""
<section class="hero">
  <div class="tab">C4 · LA RUTA</div>
  <div class="eyebrow">EL DESPEGUE · PARADA 7 · SURVIVAL IN SPANISH</div>
  <h1>Las profesiones</h1>
  <div class="sub">Vragen en zeggen wat iemand <b>doet</b> — en gissen zoals Josefina. <span class="gloss">Las profesiones — ¿a qué te dedicas? · soy profesor/a · trabajo en… · ser ↔ estar.</span></div>
  <div class="q">¿A qué te dedicas? — Soy profesora. Trabajo en una academia.</div>
</section>
<div class="page">
  <div class="obj"><div class="se">Al final de esta unidad · Op het einde van deze les</div>
    <ul>
      <li><span class="ck">✓</span> <span><span class="es">Preguntar por el trabajo</span> <span class="nl">— ¿a qué te dedicas? · ¿en qué trabajas? · ¿dónde trabajas?</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Decir la profesión con <b>ser</b> (zonder un/una)</span> <span class="nl">— soy profesor/a · es actriz · soy estudiante</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Usar <b>trabajo · trabajas · trabaja</b> + en</span> <span class="nl">— trabajo en una tienda · ¿trabaja en una oficina?</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Distinguir <b>ser ↔ estar</b></span> <span class="nl">— es profesora (wie) ↔ está tranquila (hoe)</span></span></li>
    </ul>
  </div>
  <div class="guide"><span class="ic">🎒</span><div><span class="hand">¡Seguimos la ruta! Parada 7.</span><div class="g">In deze «survival»-les leer je over werk praten. In de video «leest» Josefina de kaarten en gist ze naar een beroep — escritora, dependienta, actriz… — perfecte input voor ser + profesión.</div></div></div>

  <div class="se" style="margin-top:6mm">La gente de la ruta · je reisgenoten</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Je reist mee met vier jongeren uit de Spaanstalige wereld. In de scène werk je in de academia, met Fernando, María, Julio en waarzegster Josefina.</p>
  <div class="cast2">
    <div class="m"><div class="fl">🇪🇸</div><div class="nm">Lucía</div><div class="ro">Sevilla · familie</div></div>
    <div class="m"><div class="fl">🇲🇽</div><div class="nm">Diego</div><div class="ro">CDMX · eten & markt</div></div>
    <div class="m"><div class="fl">🇨🇴</div><div class="nm">Valen</div><div class="ro">Cartagena · wonen</div></div>
    <div class="m"><div class="fl">🇵🇪</div><div class="nm">Nina</div><div class="ro">Cusco · reizen</div></div>
    <div class="m"><div class="fl">🎒</div><div class="nm">Tú</div><div class="ro">jij, de reiziger</div></div>
  </div>

  <div class="truc" style="margin-top:5mm"><b>¿Qué reconoces ya?</b> Deze werk-woorden lijken op het Nederlands of Engels (<i>palabras transparentes</i>) — durf te gissen:
    <div class="cogn"><span>el actor</span><span>la actriz</span><span>el/la artista</span><span>el/la dentista</span><span>el policía</span><span>el/la periodista</span><span>la oficina</span><span>el hospital</span><span>el teatro</span><span>la academia</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Tip: veel beroepen herken je meteen — <b>actor</b>, <b>dentista</b>, <b>policía</b>…</span>
  </div>
</div>
"""

ESCUCHA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§1 · ¡Escucha!</div><h2>Bekijk de scène en lees mee</h2>
  <div class="audiorow">
    <div class="call"><span class="ic">🎬</span><div><b>Sitcom · Episodio 7 · Las profesiones.</b> Scan de code en bekijk de aflevering op de digitale pagina. Fernando ondervraagt María («yo trabajo aquí, tú trabajas aquí…»), en waarzegster Josefina <b>gist</b> beroepen uit de kaarten. Luister eerst zónder te lezen; daarna lees je mee. De <b>vetgedrukte</b> woorden zijn chunks om mee te nemen.</div></div>
    <div class="qr" data-url="{EN.url('C4', 7, EN.ancla_c4('escucha'))}"><div class="lab">Vídeo online</div>{qr(EN.url("C4", 7, EN.ancla_c4("escucha")))}<div class="meta">hub · Escucha</div></div>
  </div>
  <div class="truc"><b>Antes de escuchar · vóór je luistert.</b> Welke <b>beroepen</b> ga je horen, denk je? <span style="font-size:8.8pt;color:var(--mut)">(gis gerust)</span>
    <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.2">Una profesión: {wl('sm')} &nbsp;&nbsp; Otra profesión: {wl('sm')} &nbsp;&nbsp; Un lugar de trabajo: {wl('sm')}</div>
  </div>
  <div class="twocol">{scenehtml(*SCENES[0])}{scenehtml(*SCENES[1])}{scenehtml(*SCENES[2])}</div>
  <div class="ojo"><b>¡Ojo!</b> «<b>Es</b> profesora» (wie ze is — beroep, mét ser, zónder un/una) ↔ «No <b>estás</b> bien» (hoe je eraan toe bent — toestand, met estar).</div>

  <div class="se" style="margin-top:5mm">Después de escuchar · ¿Verdadero o falso?</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Kruis aan. Verbeter de <b>falsas</b> op de lijn.</p>
  <table class="vf">
    <tr><td>1. Fernando, María y Julio trabajan en el mismo lugar.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>2. Josefina dice primero: «puede ser actriz».</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>3. La mujer de las cartas es profesora.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>4. Al final, Josefina ve a una mujer para María.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
  </table>
</div>
"""

KIT=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Suena bien · pronunciación</div><h2>La c/qu = /k/ &amp; la esdrújula</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 1mm">Vóór a/o/u klinkt <b>c</b> als /k/ (casa, médico). Vóór e/i schrijf je <b>qu</b> — de u hoor je NIET: «queso» = «ke-so». Oefen online (QR §1).</p>
  <div class="cogn"><span>casa</span><span>cocina</span><span>médico</span><span>carta</span><span>queso</span><span>¿quién?</span><span>aquí</span><span>tranquilo</span></div>
  <div class="ojo"><b>¡Ojo!</b> que = «ke» (niet «kwe»!) · qui = «ki». Vergelijk: <b>c</b>asa /k/ ↔ <b>c</b>ine /θ/ (U3) — dáárom bestaat qu.</div>
  <div class="klemline"><b>La esdrújula · klemtoon op de 3de lettergreep van achter — áltijd een accent:</b> <span class="t">MÉ</span>·di·co · <span class="t">MÚ</span>·si·ca · <span class="t">SÁ</span>·ba·do · te·<span class="t">LÉ</span>·fo·no</div>

  <div class="se" style="margin-top:3mm">§2 · Kit de supervivencia</div><h2>De taal die je écht nodig hebt</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 2mm">Vink ☐ af telkens je een uitdrukking vlot kunt <b>naspreken</b>. Oefen ze online met audio.</p>
  <div class="kitwrap">{"".join(kittable(n,it) for n,it in CLUSTERS)}</div>
</div>
"""

GRAM=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§4 · Gramática en la práctica</div><h2>Kort en functioneel</h2>
  <div class="modelo"><b>🔎 Fíjate · kijk terug naar de scène.</b> Je hoorde het al: «Yo <b>trabajo</b> aquí, tú <b>trabajas</b> aquí y él <b>trabaja</b> aquí» · «<b>Es</b> profesora» · «Yo <b>estoy</b> bien. <b>Estamos</b> todos bien». Ontdek zelf het patroon — <i>eerst betekenis, dan de regel.</i></div>
  <div class="regla"><span class="tag">ser + profesión · zonder un/una</span>
    <table class="gt2"><tr><td class="v">Soy profesora.</td><td>Ik ben lerares.</td><td class="ex">niet: <s>soy una profesora</s></td></tr>
    <tr><td class="v">Es escritor.</td><td>Hij is schrijver.</td><td class="ex">¿Es actriz? — No, es profesora.</td></tr></table>
    <p style="font-size:9pt;margin:1mm 0 0">⚠️ ♂/♀: profesor/profesor<b>a</b> · escritor/escritor<b>a</b> · dependient<b>e</b>/dependient<b>a</b> · actor/<b>actriz</b> · gelijk: el/la estudiante.</p>
  </div>
  <div class="regla"><span class="tag">trabajo · trabajas · trabaja — chunks uit de scène (+ en)</span>
    <table class="gt2"><tr><td class="v">(yo) trabajo</td><td>ik werk</td><td class="ex">Trabajo <b>en</b> una tienda.</td></tr>
    <tr><td class="v">(tú) trabajas</td><td>jij werkt</td><td class="ex">¿Dónde trabajas?</td></tr>
    <tr><td class="v">(él/ella) trabaja</td><td>hij/zij werkt</td><td class="ex">¿Trabaja en una oficina?</td></tr></table>
    <p style="font-size:9pt;margin:1mm 0 0">💡 Leer ze als vaste chunks — het volledige werkwoordsysteem komt in het 5de jaar. Werkplek altijd met <b>en</b>.</p>
  </div>
  <div class="regla"><span class="tag">ser ↔ estar · wie je bent ↔ hoe je je voelt</span>
    <div class="mv2"><div class="m">SER — wie/wat: <b>es</b> profesora (beroep) · <b>soy</b> belga (afkomst)</div><div class="f">ESTAR — toestand: <b>estoy</b> bien · <b>estamos</b> todos tranquilos · ¿<b>estáis</b> bien?</div></div>
    <p style="font-size:9pt;margin:1mm 0 0">💡 estar ken je al: estoy cansado (U2) · ¿dónde está? (U6). Nieuw: <b>estamos</b> (wij) en <b>estáis</b> (jullie) — uit de scène.</p>
  </div>
  <div class="truc"><b>Mini-oefening 1 · ser + profesión.</b> Vul de vrouwelijke vorm in: a) el profesor → la {wl('sm')} &nbsp; b) el escritor → la {wl('sm')} &nbsp; c) el actor → la {wl('sm')}</div>
  <div class="truc"><b>Mini-oefening 2 · ¿ser of estar?</b> Kies: 1. María {wl('sm')} profesora (beroep). &nbsp; 2. Julio no {wl('sm')} bien (toestand). &nbsp; 3. Nosotros {wl('sm')} tranquilos.</div>
  <div class="truc"><b>Mini-oefening 3 · trabajo/trabajas/trabaja.</b> Vul aan: 1. Yo {wl('sm')} en una tienda. &nbsp; 2. ¿Dónde {wl('sm')} tú? &nbsp; 3. Ella {wl('sm')} en el hospital.</div>
</div>
"""

def act(n,title,badges,body):
    bh="".join(f'<span class="badge {c}">{t}</span>' for t,c in badges)
    return (f'<div class="act"><div class="acthead"><div class="anum">{n}</div><div><div class="h">{title}</div>'
            f'<div class="badges">{bh}</div></div></div>{body}</div>')

PRAC=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§3 · Práctica</div><h2>Oefen op papier — online verbeter je alles</h2>

  {act(1,"Clasifica: profesión, lugar o estado",[("receptief","skill"),("5 min","")],
    '<p style="margin-left:12.5mm">Schrijf elk woord in de juiste kolom. Voeg onderaan één eigen woord toe.<br><span class="gloss">escritora · la tienda · tranquilo · dependienta · la oficina · cansada · actriz · la academia</span></p>'
    +'<div class="wcols" style="margin-left:12.5mm"><div class="wcol"><h4>Profesión 💼</h4><div class="fill"></div></div><div class="wcol"><h4>Lugar 🏢</h4><div class="fill"></div></div><div class="wcol"><h4>Estado 😌</h4><div class="fill"></div></div><div class="wcol"><h4>Tu palabra</h4><div class="fill"></div></div></div>')}

  {act(2,"Relaciona · ¿dónde trabaja?",[("gestuurd","skill"),("★☆☆","")],
    '<p style="margin-left:12.5mm">Une con una línea la profesión y el lugar de trabajo. <span class="gloss">verbind beroep en werkplek</span></p>'
    +'<table class="mtab" style="margin-left:12.5mm"><tr><td class="a">1. la profesora</td><td><span class="ln"></span></td><td class="b">a. en una tienda</td></tr>'
    +'<tr><td class="a">2. el dependiente</td><td><span class="ln"></span></td><td class="b">b. en un teatro</td></tr>'
    +'<tr><td class="a">3. la médica</td><td><span class="ln"></span></td><td class="b">c. en una academia</td></tr>'
    +'<tr><td class="a">4. el actor</td><td><span class="ln"></span></td><td class="b">d. en un hospital</td></tr>'
    +'<tr><td class="a">5. la escritora</td><td><span class="ln"></span></td><td class="b">e. en casa, con sus libros</td></tr></table>')}

  {act(3,"Completa el diálogo",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Completa (dedicas · soy · trabajas · trabajo · estás). <span class="gloss">vul aan</span></p>'
    +f'<div style="margin-left:12.5mm;font-size:10pt;line-height:2.5">'
    +f'— ¿A qué te {wl("sm")}?<br>— {wl("sm")} profesora.<br>— ¿Y dónde {wl("sm")}?<br>— {wl("sm")} en una academia.<br>— ¿Y {wl("sm")} contenta?<br>— Sí, muy contenta.</div>')}

  {act(4,"Ordena · el juego de Josefina",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Numera la adivinanza de Josefina en el orden correcto (1–5). <span class="gloss">nummer het raadsel in de juiste volgorde</span></p>'
    +'<div class="scramble" style="margin-left:12.5mm"><span>___ ¿Trabaja en una tienda?</span><span>___ Silencio… hay una mujer.</span><span>___ No. ¡Es profesora!</span><span>___ ¿Puede ser escritora?</span><span>___ No, no es escritora.</span></div>')}

  {act(5,"¿ser o estar?",[("gestuurd","skill"),("★★☆","")],
    f'<p style="margin-left:12.5mm">Escribe la forma correcta (ser = quién eres o tu profesión · estar = cómo estás). <span class="gloss">ser voor wie je bent, estar voor hoe je bent</span></p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. María {wl("sm")} profesora. &nbsp; 2. Julio no {wl("sm")} bien. &nbsp; 3. Yo {wl("sm")} estudiante. &nbsp; 4. Nosotros {wl("sm")} todos tranquilos.</div>')}

  {act(6,"La forma femenina ♀",[("gestuurd","skill"),("★☆☆","")],
    f'<p style="margin-left:12.5mm">Escribe la forma femenina. <span class="gloss">schrijf de vrouwelijke vorm</span></p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. el profesor → {wl("sm")} &nbsp; 2. el escritor → {wl("sm")} &nbsp; 3. el actor → {wl("sm")} &nbsp; 4. el dependiente → {wl("sm")}</div>')}

  {act(7,"Tres pistas · escribe",[("productie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Elige en secreto una profesión y escribe tres pistas: «Trabajo en…», «Estoy…», «Trabajo con…». <span class="gloss">kies in het geheim een beroep en schrijf drie tips</span></p>'
    +'<div class="wbox" style="margin-left:12.5mm"></div>')}

  {act(8,"Entrevista · ¿a qué te dedicas?",[("interactie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Entrevista a tu compañero/a (elegid una profesión inventada) y anota. Después cambiad. <span class="gloss">interview je buur en wissel van rol</span></p>'
    +f'<table class="wtab" style="margin-left:12.5mm;margin-top:2mm"><thead><tr><th style="width:48mm">Pregunta</th><th>Respuesta</th></tr></thead>'
    +'<tr><td style="height:12mm">¿A qué te dedicas?</td><td></td></tr>'
    +'<tr><td style="height:12mm">¿Dónde trabajas?</td><td></td></tr>'
    +'<tr><td style="height:12mm">¿Estás contento/a?</td><td></td></tr></table>')}
</div>
"""

TAREA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§5 · Tarea final</div><h2>¿Quién soy? · adivina la profesión</h2>
  <div class="esen" style="margin-top:2mm"><b class="tt">Jouw opdracht.</b> Kies (geheim!) een <b>beroep + werkplek</b>. Geef <b>drie pistas</b> in het Spaans («trabajo en…», «estoy…», «trabajo con…»); de klas <b>gist</b> zoals Josefina («¿puede ser…?», «¿trabajas en…?», «¡ya lo sé!»). Wie raadt, is aan de beurt. <span class="gloss">Sin leer del papel — zonder van het blad af te lezen.</span></div>
  <div class="regla" style="margin-top:4mm"><span class="tag">Prepárate · vul eerst je fiche in</span>
    <div style="margin-top:2mm;font-size:9.7pt;line-height:2.4">Mi profesión (geheim): {wl('lg')}<br>Pista 1 · Trabajo en {wl('lg')}<br>Pista 2 · Estoy {wl('sm')} y trabajo con {wl('sm')}<br>Pista 3 · {wl('full')}</div>
  </div>
  <div class="modelo" style="margin-top:4mm"><b>Modelo · zo klinkt het:</b><br>
    — Trabajo en un hospital. Estoy con muchas personas. Trabajo de día y de noche.<br>
    — ¿Puede ser… médica? — ¡Sí! Soy médica.</div>
  <div class="regla" style="margin-top:3mm"><span class="tag">Para adivinar · om te gissen (zoals Josefina)</span>
    <p style="margin:1mm 0 0;font-size:9.6pt">¿Puede ser… (escritora · actor · médico)? · ¿Trabajas en una tienda / una oficina? · ¿O algo parecido? · ¡Ya lo sé! Eres… · Sí, soy… / No, no soy…</p>
  </div>
  <div style="margin-top:4mm"><div class="se">Mis notas · noteer hier wie wat is in de klas</div>
    <table class="wtab" style="margin-top:2mm"><thead><tr><th>Compañero/a</th><th>Profesión</th><th>¿Dónde trabaja?</th></tr></thead>
    <tr><td style="height:9mm"></td><td></td><td></td></tr>
    <tr><td style="height:9mm"></td><td></td><td></td></tr>
    <tr><td style="height:9mm"></td><td></td><td></td></tr></table>
  </div>
  <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div class="truc" style="margin:0"><b>🏁 Klaar als…</b> je 3 pistas geeft met «trabajo en…» + «estoy…», gist met «¿puede ser…?» en antwoordt met «sí, soy… / no, no soy…» — zónder af te lezen.</div>
    <table class="rubric"><thead><tr><th>Evaluatie</th><th style="text-align:center">🟢🟡🔴</th></tr></thead>
      <tr><td>pistas (trabajo en… · estoy…) correct</td><td></td></tr>
      <tr><td>adivinar (¿puede ser…?) + ser sin un/una</td><td></td></tr>
      <tr><td>uitspraak &amp; durf</td><td></td></tr></table>
  </div>
</div>
"""

BANDAS=[("Rosalía","La Perla","🇪🇸 España"),("Juanes","A Dios le Pido","🇨🇴 Colombia"),("Álvaro Soler","Sofía","🇪🇸 España"),
 ("Marc Anthony","Vivir Mi Vida","🇵🇷 Puerto Rico"),("Manu Chao","Me Gustas Tú","🇪🇸/🇫🇷"),("Shakira","Antología","🇨🇴 Colombia")]
def banda(a,s,g): return f'<div class="banda"><div class="ar">{a}</div><div class="sg">🎵 {s}</div><div class="ge">{g}</div></div>'
MUSICA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Cultura · Banda sonora</div><h2>El trabajo en el mundo hispano</h2>
  <p style="font-size:9.6pt">Over werk praten klinkt anders in elke cultuur. In het Spaans zeg je <b>soy profesor</b> — zónder «un/una». In Spanje bestaat het <b>horario partido</b>: winkels sluiten van 14 tot 17 u en men werkt tot ± 20 u. En de klassieke kennismakingsvraag is <b>¿A qué te dedicas?</b> Beroemde beroepen: Frida Kahlo <b>pintora</b>, García Márquez <b>escritor</b>, Messi <b>futbolista</b>, Rosalía <b>cantante</b>.</p>
  <div class="bandas">{"".join(banda(*b) for b in BANDAS)}</div>
  <div class="musrow">
    <div class="call"><span class="ic">🎧</span><div><b>Spotify · la playlist de la clase.</b> Scan en luister. Op de digitale pagina vind je ook <b>LyricsTraining</b> en de <b>wereldkaart</b>.</div></div>
    <div class="qr" data-url="{SPOTIFY}"><div class="lab">Playlist</div>{qr(SPOTIFY)}<div class="meta">Spotify</div></div>
  </div>
  <div class="truc" style="margin-top:5mm"><b>Profesiones famosas · ¿quién es quién?</b> Verbind (gis gerust):
    <table class="mtab" style="margin-top:1mm"><tr><td class="a">Frida Kahlo era…</td><td>{wl('sm')}</td><td class="b">a. escritor (Cien años de soledad)</td></tr>
    <tr><td class="a">García Márquez era…</td><td>{wl('sm')}</td><td class="b">b. pintora mexicana</td></tr>
    <tr><td class="a">Rosalía es…</td><td>{wl('sm')}</td><td class="b">c. cantante española</td></tr></table>
    <p style="font-size:8.6pt;color:var(--mut);margin-top:1mm">💡 Ook hier: <b>ser</b> + beroep zonder un/una — «es cantante», «era pintora».</p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:3mm;align-items:start">
    <div class="truc" style="margin:0"><b>Escucha y responde.</b> Kies één nummer van de playlist.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.3">Mi canción: {wl('lg')}<br>La profesión del artista: {wl('lg')}</div>
    </div>
    <div class="truc" style="margin:0"><b>¿Y tú?</b> Schrijf één zin: je (droom)beroep + waar je werkt.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.4">{wl('full')}<br>{wl('full')}</div>
    </div>
  </div>
</div>
"""

REPASO=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Repaso · Lo esencial de un vistazo</div><h2>Wat je nu kunt</h2>
  <div class="fams">
    <div class="pcard"><div class="t">Zo praat je over werk</div><div class="ej"><b>¿A qué te dedicas?</b> — <b>Soy</b> ____ (profesor/a…). <b>Trabajo en</b> ____.</div><div class="t2">ser + beroep zónder un/una · werkplek met en</div></div>
    <div class="pcard"><div class="t">Zo hou je ser ↔ estar uit elkaar</div><div class="ej"><b>Es</b> profesora (wie/wat) ↔ <b>Está</b> tranquila (hoe). <b>Estamos</b> todos bien.</div><div class="anchor">ser = identiteit/beroep &nbsp;|&nbsp; estar = toestand/plaats</div></div>
  </div>
  <div class="regla" style="margin:4mm 0"><span class="tag">Frases para la clase</span>
    <div class="cogn" style="margin-top:1mm"><span>¿Cómo se dice… ?</span><span>¿Qué significa… ?</span><span>Otra vez, por favor</span><span>No entiendo</span><span>¿Puedes repetir?</span><span>¿Puedo ir al baño?</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Handige klaszinnen — gebruik ze in het Spaans i.p.v. Nederlands.</span>
  </div>
  <table class="sem"><thead><tr><th style="text-align:left">Puedo… · Ik kan…</th><th>🟢</th><th>🟡</th><th>🔴</th></tr></thead>
    <tr><td>naar werk vragen (¿a qué te dedicas? · ¿dónde trabajas?)</td><td></td><td></td><td></td></tr>
    <tr><td>mijn beroep zeggen (soy… zonder un/una)</td><td></td><td></td><td></td></tr>
    <tr><td>trabajo/trabajas/trabaja + en gebruiken</td><td></td><td></td><td></td></tr>
    <tr><td>ser en estar uit elkaar houden</td><td></td><td></td><td></td></tr></table>
  <div class="regla" style="margin-top:5mm"><span class="tag">Mini-test · recuerda sin mirar</span>
    <p style="margin:1mm 0 0;font-size:9.4pt">Sluit de cursus en vertaal uit het hoofd (ophalen = het beste leren).</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3mm 8mm;margin-top:2mm;font-size:9.8pt;line-height:2.2">
      <div>1. wat doe je (voor werk)? → {wl('')}</div><div>2. ik ben lerares → {wl('')}</div>
      <div>3. ik werk in een winkel → {wl('')}</div><div>4. de actrice → {wl('')}</div>
      <div>5. we zijn allemaal oké → {wl('')}</div><div>6. misschien is ze schrijfster → {wl('')}</div>
    </div>
  </div>
  <div class="guide"><span class="ic">🎮</span><div><span class="hand">Repasa jugando</span><div class="g">Oefen alles online met spelletjes, flashcards en audio op de digitale hub (scan de QR bij §1).</div></div></div>
  <div class="bridge"><b>Próxima parada →</b> In de volgende unit: <i>la hora y los días</i> (¿qué hora es?). ¡Hasta pronto!</div>
</div>
"""

EDITBAR="""
<div class="editbar" id="eb">
  <b>✏️ C4 · U7</b>
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
document.getElementById('btnsave').onclick=function(){var html='<!doctype html>'+document.documentElement.outerHTML;var b=new Blob([html],{type:'text/html'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='C4_U7_Profesiones_bewerkt.html';a.click();};
</script>
"""

HTML=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 7 · Las profesiones</title><style>{CSS}</style></head><body class="c4">
{EDITBAR}
{HERO}{ESCUCHA}{COMPR_SEC}{KIT}{GRAM}{PRAC}{TAREA}{MUSICA}{FUNCIONES_SEC}{REPASO}
{SCRIPT}
</body></html>"""
os.makedirs(f"{ROOT}/03-build/web/print",exist_ok=True)
open(f"{ROOT}/03-build/web/print/C4_U7.html","w",encoding="utf-8").write(HTML)
print("C4_U7.html (print+editable) geschreven:",len(HTML),"bytes")
