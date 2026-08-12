#!/usr/bin/env python3
# C4 · Unidad 4 — PRINT (HTML=bron → PDF via Chromium). Golden-sample print-kit, C4-rood.
# Thema: La familia · presentar & describir (mi/tu · ser+adjetivo · concordancia -o/-a). Zelfde pijplijn als U1–U3.
import base64, os, re, io, sys
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
from funciones_print import print_section
FUNCIONES_SEC=print_section(4)
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
HUB_URL=EN.url("C4", 4)
import comprension_print
COMPR_SEC=comprension_print.print_section(4, HUB_URL)
SPOTIFY="https://open.spotify.com/playlist/37i9dQZF1DXaxEKcoCdWHD"

SCENES=[
 ("Escena 1 · El interrogatorio",[
  ("Madre","Entonces, ¿es un chico?"),("María","Sí mamá, es un chico."),("Madre","Ya. ¿Y es simpático?"),
  ("María","Sí mamá, es simpático."),("Madre","¿Y es un amigo? ¿Es divertido?"),
  ("María","¡Mamá! Ya voy yo. ¡Que voy yo!"),("Madre","Sube, sube, ya abro."),
 ]),
 ("Escena 2 · El álbum de fotos",[
  ("Madre","Esta es mi madre, la abuela de María. Es muy elegante, pero un poco gorda."),
  ("Julio","Ahora María es una chica muy delgada y muy guapa."),
  ("Madre","Ahora es muy guapa y muy inteligente. El tío Fermín es el guapo de la familia: muy alto y muy fuerte."),
  ("Madre","¿Tú no eres muy alto, no?"),("Julio","No, la verdad es que no."),
  ("Madre","Paula es la hermana de María, vive en Londres. ¡Divertida, amable…! María no es así."),
 ]),
]
CH=["es un chico","es simpático","es divertido","muy elegante","un poco gorda","muy delgada","muy guapa","muy inteligente","muy alto","muy fuerte","la abuela","el tío","mi madre","la hermana","divertida","amable","guapo"]
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
 ("La familia · miembros",[("la madre · el padre","moeder · vader"),("el hermano · la hermana","broer · zus"),
   ("el abuelo · la abuela","opa · oma"),("el tío · la tía","oom · tante"),("el hijo · la hija","zoon · dochter")]),
 ("Presentar · voorstellen",[("Esta es mi madre","Dit is mijn moeder"),("Este es mi padre","Dit is mijn vader"),
   ("Es mi hermano/a","Mijn broer/zus"),("Se llama…","Hij/zij heet…")]),
 ("El físico · uiterlijk",[("alto/a · bajo/a","lang · klein"),("guapo/a","knap"),("delgado/a · gordo/a","slank · mollig"),
   ("fuerte","sterk"),("el pelo largo/corto","lang/kort haar")]),
 ("El carácter · karakter",[("simpático/a","aardig"),("divertido/a","grappig"),("amable","vriendelijk"),
   ("inteligente","intelligent"),("elegante","elegant")]),
 ("¿Dónde vive?",[("¿Dónde vives?","Waar woon je?"),("Vivo en…","Ik woon in…"),("Vive en Londres","Woont in Londen")]),
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
.p{color:#2563EB;font-weight:700}.v{color:#EA7317;font-weight:700}.pl{color:#0E9E97;font-weight:700}
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
.gt2 .p{color:#2563EB;font-family:var(--disp)}.gt2 .ex{color:var(--mut);font-style:italic}
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
.editbar{position:fixed;top:0;left:0;right:0;background:var(--gd);color:#fff;display:flex;gap:8px;align-items:center;padding:7px 12px;z-index:999;font-family:var(--body);font-size:13px;box-shadow:0 2px 10px #0003}
.editbar b{font-family:var(--disp)}.editbar button{border:0;background:#fff;color:var(--gd);font-weight:700;border-radius:8px;padding:6px 11px;cursor:pointer;font-size:12.5px}
.editbar button.on{background:#111;color:#fff}.editbar .sp{flex:1}.scr-spacer{height:44px}
body.editing .page{outline:1.5px dashed var(--g);outline-offset:-6px}
@media print{ .editbar,.scr-spacer{display:none!important} }
"""

HERO=f"""
<section class="hero">
  <div class="tab">C4 · LA RUTA</div>
  <div class="eyebrow">EL DESPEGUE · PARADA 4 · SURVIVAL IN SPANISH</div>
  <h1>La familia</h1>
  <div class="sub">Je <b>familie</b> voorstellen en mensen <b>beschrijven</b>. <span class="gloss">Presentar a la familia y describir a las personas — mi madre, mi hermano… es alto, guapa, simpático.</span></div>
  <div class="q">Esta es mi madre. Es muy elegante.</div>
</section>
<div class="page">
  <div class="obj"><div class="se">Al final de esta unidad <span class="gloss">op het einde van deze les</span></div>
    <ul>
      <li><span class="ck">✓</span> <span><span class="es">Presentar a tu familia</span> <span class="nl">— esta es mi madre · se llama…</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Describir el físico y el carácter</span> <span class="nl">— es alto/a · guapo/a · simpático/a</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Usar <b>mi / tu</b> y la concordancia <b>-o/-a</b></span> <span class="nl">— mi madre · alto/alta</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Graduar con <b>muy / un poco</b></span> <span class="nl">— muy guapa · un poco tímido</span></span></li>
    </ul>
  </div>
  <div class="guide"><span class="ic">🎒</span><div><span class="hand">¡Seguimos la ruta! Parada 4.</span><div class="g">En esta lección de «survival» aprendes a presentar a tu familia y a describir a la gente. En el vídeo una madre enseña su álbum de fotos y comenta a todo el mundo: adjetivos a raudales. <span class="gloss">perfecte input voor adjectieven</span></div></div></div>

  <div class="se" style="margin-top:6mm">La gente de la ruta · tus compañeros de viaje</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Viajas con cuatro jóvenes del mundo hispano. En la escena conoces a María, a su madre (¡muy directa!) y a Julio. <span class="gloss">je reist mee met vier jongeren</span></p>
  <div class="cast2">
    <div class="m"><div class="fl">🇪🇸</div><div class="nm">Lucía</div><div class="ro">Sevilla · familie</div></div>
    <div class="m"><div class="fl">🇲🇽</div><div class="nm">Diego</div><div class="ro">CDMX · eten & markt</div></div>
    <div class="m"><div class="fl">🇨🇴</div><div class="nm">Valen</div><div class="ro">Cartagena · wonen</div></div>
    <div class="m"><div class="fl">🇵🇪</div><div class="nm">Nina</div><div class="ro">Cusco · reizen</div></div>
    <div class="m"><div class="fl">🎒</div><div class="nm">Tú</div><div class="ro">jij, de reiziger</div></div>
  </div>

  <div class="truc" style="margin-top:5mm"><b>¿Qué reconoces ya?</b> Estos adjetivos para describir se parecen al neerlandés o al inglés (<i>palabras transparentes</i>) — durf te gissen:
    <div class="cogn"><span>la familia</span><span>elegante</span><span>inteligente</span><span>el álbum</span><span>la foto</span><span>moderno</span><span>favorito/a</span><span>normal</span><span>el carácter</span><span>sexy</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Tip: veel <i>adjetivos</i> herken je meteen — <b>elegante</b>, <b>inteligente</b>, <b>favorito</b>…</span>
  </div>
</div>
"""

ESCUCHA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§1 · ¡Escucha!</div><h2>Mira la escena y lee al mismo tiempo <span class="gloss" style="font-size:10pt;font-weight:400">bekijk en lees mee</span></h2>
  <div class="audiorow">
    <div class="call"><span class="ic">🎬</span><div><b>Sitcom · Episodio 4 · La familia.</b> Escanea el código y mira el episodio en la página digital. Una madre interroga a su hija sobre «un chico» y después saca el <b>álbum de fotos</b>, con una avalancha de adjetivos. Primero escucha sin leer; después lee al mismo tiempo. Las palabras en <b>negrita</b> son chunks para llevarte. <span class="gloss">eerst zónder te lezen, daarna lees je mee</span></div></div>
    <div class="qr" data-url="{EN.url('C4', 4, EN.ancla_c4('escucha'))}"><div class="lab">Vídeo online</div>{qr(EN.url("C4", 4, EN.ancla_c4("escucha")))}<div class="meta">hub · Escucha</div></div>
  </div>
  <div class="truc"><b>Antes de escuchar.</b> ¿Qué <b>familiares</b> y qué <b>adjetivos</b> crees que vas a oír? <span class="gloss">wat ga je horen, denk je?</span> <span style="font-size:8.8pt;color:var(--mut)">(gis gerust)</span>
    <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.2">Un familiar: {wl('sm')} &nbsp;&nbsp; Un adjetivo (físico): {wl('sm')} &nbsp;&nbsp; Un adjetivo (carácter): {wl('sm')}</div>
  </div>
  <div class="twocol">{scenehtml(*SCENES[0])}{scenehtml(*SCENES[1])}</div>
  <div class="ojo"><b>¡Ojo!</b> Para describir a alguien usas <b>ser</b> (es): «es guapa», «es simpático», no <i>estar</i>. Y el adjetivo cambia: una chica alt<b>a</b>, un chico alt<b>o</b>. <span class="gloss">beschrijven met ser; het adjectief past zich aan</span></div>

  <div class="se" style="margin-top:5mm">Después de escuchar · ¿Verdadero o falso?</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Kruis aan. Verbeter de <b>falsas</b> op de lijn.</p>
  <table class="vf">
    <tr><td>1. La abuela de María es muy elegante.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>2. El tío Fermín es bajo y débil.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>3. Paula es la hermana de María y vive en Londres.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>4. Ahora María es delgada y guapa.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
  </table>
</div>
"""

KIT=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Suena bien · pronunciación</div><h2>La ll, la y (yeísmo) &amp; el acento llano</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 1mm">De <b>ll</b> klinkt in de meeste landen als de NL «j»: «calle» ≈ «ca-je». Oefen online (QR §1).</p>
  <div class="cogn"><span>calle</span><span>llave</span><span>apellido</span><span>ella</span><span>silla</span><span>llamar</span></div>
  <div class="ojo"><b>¡Ojo!</b> «ll» is één klank, niet twee l'en: ca<b>ll</b>e, <b>ll</b>ave. En de <b>y</b> klinkt net zo (<i>yeísmo</i>): «yo» ≈ «jo», «playa» ≈ «pla-ja».</div>
  <div class="cogn"><span>yo</span><span>ya</span><span>playa</span><span>mayo</span><span>desayuno</span><span>leyenda</span></div>
  <div class="klemline"><b>El acento llano · de meeste woorden (klemtoon op de voorlaatste):</b> <span class="t">MA</span>·dre · her·<span class="t">MA</span>·no · a·<span class="t">BUE</span>·la · e·le·<span class="t">GAN</span>·te</div>

  <div class="se" style="margin-top:3mm">§2 · Kit de supervivencia</div><h2>La lengua que de verdad necesitas <span class="gloss" style="font-size:10pt;font-weight:400">de taal die je écht nodig hebt</span></h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 2mm">Marca ☐ cada vez que puedas <b>repetir</b> una expresión con soltura. Practícalas en línea con audio. <span class="gloss">vink af wat je vlot kunt naspreken</span></p>
  <div class="kitwrap">{"".join(kittable(n,it) for n,it in CLUSTERS)}</div>
</div>
"""

GRAM=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§4 · Gramática en la práctica</div><h2>Corta y funcional <span class="gloss" style="font-size:10pt;font-weight:400">kort en functioneel</span></h2>
  <div class="modelo"><b>🔎 Fíjate · vuelve a la escena.</b> Ya lo has oído: «Esta es <b>mi</b> madre» · «<b>Es</b> muy elegante» · «Es una chica muy delgad<b>a</b> y muy guap<b>a</b>». Descubre tú el patrón — <i>primero el significado, después la regla.</i> <span class="gloss">ontdek zelf het patroon</span></div>
  <div class="regla"><span class="tag">mi · tu · su · ¿de quién es? (posesivos) <span class="gloss">van wie is het?</span></span>
    <table class="gt2"><tr><td class="p">mi</td><td>mijn</td><td class="ex"><b>mi</b> madre · <b>mi</b> hermano</td></tr>
    <tr><td class="p">tu</td><td>jouw</td><td class="ex">¿Y <b>tu</b> familia?</td></tr>
    <tr><td class="p">su</td><td>zijn/haar</td><td class="ex"><b>su</b> padre</td></tr></table>
    <p style="font-size:9pt;margin:1mm 0 0">💡 Ook: <b>de</b> + naam → «la hermana <b>de</b> María». mi/tu blijven gelijk (geen -o/-a): mi madre én mi padre.</p>
  </div>
  <div class="regla"><span class="tag">es + adjetivo · iemand beschrijven (concordancia -o/-a)</span>
    <div class="mv2"><div class="m">♂ Un chico: es alt<b>o</b> · guap<b>o</b> · delgad<b>o</b> · simpátic<b>o</b> · divertid<b>o</b></div><div class="f">♀ Una chica: es alt<b>a</b> · guap<b>a</b> · delgad<b>a</b> · simpátic<b>a</b> · divertid<b>a</b></div></div>
    <p style="font-size:9pt;margin:1mm 0 0">Op <b>-e</b> blijven gelijk (♂=♀): <b>amable</b>, <b>inteligente</b>, <b>elegante</b>, <b>fuerte</b>. ⚠️ Beschrijven = <b>ser</b> (es), niet estar.</p>
  </div>
  <div class="regla"><span class="tag">muy · un poco</span>
    <p style="margin:1mm 0 0;font-size:9.6pt"><b>muy</b> = heel (versterkt): «muy alta». <b>un poco</b> = een beetje (verzacht, vaak iets negatiefs): «un poco gorda». In de scène: «muy elegante, <b>pero un poco</b> gorda».</p>
  </div>
  <div class="truc"><b>Mini-ejercicio 1 · mi/tu + ser.</b> Completa:
    <div style="margin-top:2mm;font-size:9.6pt;line-height:2.4">1. Esta es {wl('sm')} madre (de mí). &nbsp; 2. ¿Cómo {wl('sm')} tu hermano? &nbsp; 3. {wl('sm')} tía es muy amable (de mí). &nbsp; 4. ¿Y {wl('sm')} familia? (de ti)</div>
  </div>
  <div class="truc"><b>Mini-ejercicio 2 · adjetivo ♂/♀.</b> Escribe bien el adjetivo: a) Mi hermana (guapo) → {wl('sm')} &nbsp; b) Mi tío (alto) → {wl('sm')} &nbsp; c) María (divertido) → {wl('sm')}</div>
  <div class="truc"><b>Mini-ejercicio 3 · ¿muy o un poco?</b> Elige lo que tenga sentido y completa:
    <div style="margin-top:2mm;font-size:9.6pt;line-height:2.4">1. Einstein es {wl('sm')} inteligente. &nbsp; 2. Un ratón es {wl('sm')} pequeño (klein). &nbsp; 3. Un elefante es {wl('sm')} grande y {wl('sm')} fuerte.</div>
    <div style="margin-top:2mm;font-size:9.6pt">✍️ Describe a alguien de tu familia (naam + 2 adjectieven): {wl('full')}</div></div>
</div>
"""

def act(n,title,badges,body):
    bh="".join(f'<span class="badge {c}">{t}</span>' for t,c in badges)
    return (f'<div class="act"><div class="acthead"><div class="anum">{n}</div><div><div class="h">{title}</div>'
            f'<div class="badges">{bh}</div></div></div>{body}</div>')

PRAC=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§3 · Práctica</div><h2>Practica en papel · online se corrige solo <span class="gloss" style="font-size:10pt;font-weight:400">online verbetert het zichzelf</span></h2>

  {act(1,"Clasifica: familia, físico o carácter",[("receptief","skill"),("5 min","")],
    '<p style="margin-left:12.5mm">Schrijf elk woord in de juiste kolom. Voeg onderaan één eigen woord toe.<br><span class="gloss">la abuela · alto · simpático · el tío · guapo · divertido · la hermana · amable</span></p>'
    +'<div class="wcols" style="margin-left:12.5mm"><div class="wcol"><h4>Familia 👪</h4><div class="fill"></div></div><div class="wcol"><h4>Físico 🧍</h4><div class="fill"></div></div><div class="wcol"><h4>Carácter 😊</h4><div class="fill"></div></div><div class="wcol"><h4>Tu palabra</h4><div class="fill"></div></div></div>')}

  {act(2,"Relaciona · ¿quién es?",[("gestuurd","skill"),("★☆☆","")],
    '<p style="margin-left:12.5mm">Une con una línea el familiar y su descripción. <span class="gloss">verbind familielid en omschrijving</span></p>'
    +'<table class="mtab" style="margin-left:12.5mm"><tr><td class="a">1. la abuela</td><td><span class="ln"></span></td><td class="b">a. el padre de mi padre</td></tr>'
    +'<tr><td class="a">2. el tío</td><td><span class="ln"></span></td><td class="b">b. la madre de mi madre</td></tr>'
    +'<tr><td class="a">3. el abuelo</td><td><span class="ln"></span></td><td class="b">c. la hija de mis padres</td></tr>'
    +'<tr><td class="a">4. la hermana</td><td><span class="ln"></span></td><td class="b">d. el hermano de mi padre</td></tr>'
    +'<tr><td class="a">5. los padres</td><td><span class="ln"></span></td><td class="b">e. la madre y el padre</td></tr></table>')}

  {act(3,"Completa la descripción",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Completa (piensa en ser + adjetivo y en ♂/♀). <span class="gloss">ser + adjectief, let op ♂/♀</span></p>'
    +f'<div style="margin-left:12.5mm;font-size:10pt;line-height:2.5">'
    +f'— ¿Quién es esta chica?<br>— {wl("sm")} mi hermana. Es muy simpátic{wl("sm")} <span style="color:var(--mut);font-size:8.6pt">(♀)</span>.<br>— ¿Y este chico?<br>— Es {wl("sm")} hermano (van mij). Es alt{wl("sm")} <span style="color:var(--mut);font-size:8.6pt">(♂)</span> y un {wl("sm")} tímido.</div>')}

  {act(4,"Ordena la conversación",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Numera las frases en el orden correcto (1–5). <span class="gloss">nummer de zinnen</span></p>'
    +'<div class="scramble" style="margin-left:12.5mm"><span>___ Es muy elegante y amable.</span><span>___ ¿Quién es esta persona?</span><span>___ Vive en Madrid.</span><span>___ Es mi abuela.</span><span>___ ¿Y dónde vive?</span></div>')}

  {act(5,"El adjetivo · ¿-o o -a?",[("gestuurd","skill"),("★☆☆","")],
    f'<p style="margin-left:12.5mm">Escribe la letra correcta (♂ -o / ♀ -a). <span class="gloss">vul de juiste letter in</span></p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. Mi tío es guap{wl("sm")} &nbsp; 2. Mi hermana es alt{wl("sm")} &nbsp; 3. María es delgad{wl("sm")} &nbsp; 4. Mi abuelo es simpátic{wl("sm")}</div>')}

  {act(6,"Entrevista a un compañero",[("interactie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Pregunta por la familia de tu compañero/a y anota. Después cambiad. <span class="gloss">vraag naar de familie van je buur</span></p>'
    +f'<table class="wtab" style="margin-left:12.5mm;margin-top:2mm"><thead><tr><th style="width:40mm">Pregunta</th><th>Respuesta</th></tr></thead>'
    +'<tr><td style="height:12mm">¿Tienes hermanos/as?</td><td></td></tr>'
    +'<tr><td style="height:12mm">¿Cómo es tu madre/padre?</td><td></td></tr></table>')}

  {act(7,"Describe a 2 personas",[("productie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Escribe sobre 2 familiares (reales o inventados): «Est_ es mi ___. Es ___ y ___.» (2 frases cada uno). <span class="gloss">2 familieleden, 2 zinnen elk</span></p>'
    +'<div class="wbox" style="margin-left:12.5mm"></div>')}

  {act(8,"Escribe un mensaje",[("productie","skill"),("★★★","")],
    '<p style="margin-left:12.5mm">Escribe un mensaje corto a un amigo o una amiga hispanohablante sobre tu familia: quiénes son y cómo son. <span class="gloss">kort bericht over je familie</span></p>'
    +'<div class="wbox" style="margin-left:12.5mm;min-height:28mm"></div>')}

  {act(9,"¿Cómo es?",[("productie","skill"),("★★☆","")],
    f'<p style="margin-left:12.5mm">Escribe dos adjetivos por persona (¡ojo con ♂/♀!). ¡Rápido! <span class="gloss">twee adjectieven per persoon; let op de uitgang</span></p>'
    +f'<div style="margin-left:12.5mm;font-size:9.8pt;line-height:2.3">👩 mi madre → {wl("lg")} &nbsp;&nbsp; 👴 mi abuelo → {wl("lg")}<br>🧒 mi hermano → {wl("lg")} &nbsp;&nbsp; 👧 mi hermana → {wl("lg")}</div>')}
</div>
"""

TAREA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§5 · Tarea final</div><h2>Mi árbol de familia</h2>
  <div class="esen" style="margin-top:2mm"><b class="tt">Tu tarea.</b> Dibuja un <b>árbol de familia</b> con <b>4 personas</b> (real o inventada). Presenta a cada una («Est_ es mi…, se llama…») y <b>descríbela</b> con 2 adjetivos (ojo con ♂/♀ y con muy/un poco). Presenta tu árbol a la clase. <span class="gloss">Sin leer del papel — zonder van het blad af te lezen.</span></div>
  <div class="regla" style="margin-top:4mm"><span class="tag">Prepárate · vul eerst de frames in</span>
    <div style="margin-top:2mm;font-size:9.7pt;line-height:2.4">👩 Esta es mi {wl('sm')} . Se llama {wl('sm')} . Es {wl('sm')} y {wl('sm')} .<br>👨 Este es mi {wl('sm')} . Se llama {wl('sm')} . Es {wl('sm')} .<br>🧑 Est_ es mi {wl('sm')} . Es muy {wl('sm')} y un poco {wl('sm')} .</div>
  </div>
  <div class="modelo" style="margin-top:4mm"><b>Modelo · zo klinkt het:</b><br>
    — Esta es mi madre. Se llama Carmen. Es muy simpática y un poco elegante.<br>
    — Este es mi hermano. Se llama Tom. Es alto, guapo y muy divertido.</div>
  <div style="margin-top:4mm"><div class="se">Mi árbol · dibuja aquí tu árbol y anota a cada persona <span class="gloss">teken je stamboom en noteer per persoon</span></div>
    <div class="wbox" style="min-height:52mm;background:#fff"></div>
  </div>
  <div class="regla" style="margin-top:3mm"><span class="tag">Palabras y frases útiles</span>
    <p style="margin:1mm 0 0;font-size:9.6pt">mi madre/padre · hermano/a · abuelo/a · tío/a · Esta/Este es… · Se llama… · es alto/a · guapo/a · delgado/a · simpático/a · divertido/a · amable · inteligente · elegante · muy… · un poco…</p>
  </div>
  <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div class="truc" style="margin:0"><b>🏁 Está listo cuando…</b> presentas a 4 familiares con «est_ es mi…», cada uno con 2 adjetivos (♂/♀ correcto + muy/un poco), y señalas el árbol, sin leer. <span class="gloss">zónder af te lezen</span></div>
    <table class="rubric"><thead><tr><th>Evaluatie</th><th style="text-align:center">🟢🟡🔴</th></tr></thead>
      <tr><td>presentar (est_ es mi…) correct</td><td></td></tr>
      <tr><td>ser + adjetivo (♂/♀) correct</td><td></td></tr>
      <tr><td>uitspraak &amp; durf</td><td></td></tr></table>
  </div>
</div>
"""

BANDAS=[("Rosalía","La Perla","🇪🇸 España"),("Shakira","Antología","🇨🇴 Colombia"),("Juanes","La Camisa Negra","🇨🇴 Colombia"),
 ("Aitana","Los Ángeles","🇪🇸 España"),("Luis Fonsi","Despacito","🇵🇷 Puerto Rico"),("Rosalía","TKN","🇪🇸 España")]
def banda(a,s,g): return f'<div class="banda"><div class="ar">{a}</div><div class="sg">🎵 {s}</div><div class="ge">{g}</div></div>'
MUSICA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Cultura · Banda sonora</div><h2>La familia en el mundo hispano</h2>
  <p style="font-size:9.6pt">En la cultura hispana <b>la familia</b> suele ser grande, cercana y calurosa: a veces conviven <b>tres generaciones</b>, y después de comer se habla largo rato en la mesa (<b>la sobremesa</b>). La pintora <b>Frida Kahlo</b> hizo incluso un cuadro de su árbol de familia. Y cada unidad tiene su <b>banda sonora</b>. <span class="gloss">groot, warm en dichtbij</span></p>
  <div class="bandas">{"".join(banda(*b) for b in BANDAS)}</div>
  <div class="musrow">
    <div class="call"><span class="ic">🎧</span><div><b>Spotify · la playlist de la clase.</b> Escanea y escucha. En la página digital tienes también <b>LyricsTraining</b> y el <b>mapa del mundo</b>. <span class="gloss">scan en luister; online staat er meer</span></div></div>
    <div class="qr" data-url="{SPOTIFY}"><div class="lab">Playlist</div>{qr(SPOTIFY)}<div class="meta">Spotify</div></div>
  </div>
  <div class="truc" style="margin-top:5mm"><b>La familia · ¿sabías que…?</b> Verbind (gis gerust):
    <table class="mtab" style="margin-top:1mm"><tr><td class="a">La sobremesa es…</td><td>{wl('sm')}</td><td class="b">a. la madre de tu madre</td></tr>
    <tr><td class="a">La abuela es…</td><td>{wl('sm')}</td><td class="b">b. lang napraten aan tafel</td></tr>
    <tr><td class="a">Casi todos tienen…</td><td>{wl('sm')}</td><td class="b">c. dos apellidos</td></tr></table>
    <p style="font-size:8.6pt;color:var(--mut);margin-top:1mm">💡 El segundo apellido viene de la madre: así su nombre no desaparece nunca de la familia. <span class="gloss">het tweede achternaam komt van de moeder</span></p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:3mm;align-items:start">
    <div class="truc" style="margin:0"><b>Escucha y responde.</b> Kies één nummer van de playlist.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.3">Mi canción: {wl('lg')}<br>El/la artista es de: {wl('lg')}</div>
    </div>
    <div class="truc" style="margin:0"><b>¿Y tu familia?</b> Escribe una frase sobre un familiar con un adjetivo. <span class="gloss">één zin met een adjectief</span>
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.4">{wl('full')}<br>{wl('full')}</div>
    </div>
  </div>
</div>
"""

REPASO=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Repaso · Lo esencial de un vistazo</div><h2>Lo que ya sabes hacer <span class="gloss">wat je nu kunt</span></h2>
  <div class="fams">
    <div class="pcard"><div class="t">Así presentas a alguien <span class="gloss">zo stel je iemand voor</span></div><div class="ej"><b>Esta/Este es</b> mi ____ (madre/padre…). <b>Se llama</b> ____.</div><div class="t2">mi = de mí · tu = de ti · de + nombre <span class="gloss">van mij · van jou · van + naam</span></div></div>
    <div class="pcard"><div class="t">Así describes a alguien <span class="gloss">zo beschrijf je iemand</span></div><div class="ej"><b>Es</b> alt<b>o</b>/alt<b>a</b> · guap<b>o</b>/guap<b>a</b> · simpátic<b>o</b>/a · <b>muy</b>… · <b>un poco</b>…</div><div class="anchor"><b>-o</b> = ♂ · <b>-a</b> = ♀ &nbsp;|&nbsp; -e blijft gelijk (amable, inteligente)</div></div>
  </div>
  <div class="regla" style="margin:4mm 0"><span class="tag">Frases para la clase</span>
    <div class="cogn" style="margin-top:1mm"><span>¿Cómo se dice… ?</span><span>¿Qué significa… ?</span><span>Otra vez, por favor</span><span>No entiendo</span><span>¿Puedes repetir?</span><span>Más despacio, por favor</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Handige klaszinnen — gebruik ze in het Spaans i.p.v. Nederlands.</span>
  </div>
  <table class="sem"><thead><tr><th style="text-align:left">Puedo… · Ik kan…</th><th>🟢</th><th>🟡</th><th>🔴</th></tr></thead>
    <tr><td>mijn familie voorstellen (est_ es mi…)</td><td></td><td></td><td></td></tr>
    <tr><td>iemand beschrijven (ser + adjetivo, ♂/♀)</td><td></td><td></td><td></td></tr>
    <tr><td>mi/tu en muy/un poco juist gebruiken</td><td></td><td></td><td></td></tr>
    <tr><td>de familieleden benoemen</td><td></td><td></td><td></td></tr></table>
  <div class="regla" style="margin-top:5mm"><span class="tag">Mini-test · recuerda sin mirar</span>
    <p style="margin:1mm 0 0;font-size:9.4pt">Cierra el libro y traduce de memoria: recordar es la mejor manera de aprender. <span class="gloss">uit het hoofd — ophalen leert het best</span></p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3mm 8mm;margin-top:2mm;font-size:9.8pt;line-height:2.2">
      <div>1. mijn moeder → {wl('')}</div><div>2. mijn broer → {wl('')}</div>
      <div>3. dit is mijn oma → {wl('')}</div><div>4. hij is heel knap → {wl('')}</div>
      <div>5. ze is aardig → {wl('')}</div><div>6. een beetje verlegen → {wl('')}</div>
    </div>
  </div>
  <div class="guide"><span class="ic">🎮</span><div><span class="hand">Repasa jugando</span><div class="g">Oefen alles online met spelletjes, flashcards en audio op de digitale hub (scan de QR bij §1).</div></div></div>
  <div class="bridge"><b>Próxima parada →</b> In de volgende unit: <i>en clase / los objetos</i>. ¡Hasta pronto!</div>
</div>
"""

EDITBAR="""
<div class="editbar" id="eb">
  <b>✏️ C4 · U4</b>
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
document.getElementById('btnsave').onclick=function(){var html='<!doctype html>'+document.documentElement.outerHTML;var b=new Blob([html],{type:'text/html'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='C4_U4_Familia_bewerkt.html';a.click();};
</script>
"""

HTML=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 4 · La familia</title><style>{CSS}</style></head><body class="c4">
{EDITBAR}
{HERO}{ESCUCHA}{COMPR_SEC}{KIT}{GRAM}{PRAC}{TAREA}{MUSICA}{FUNCIONES_SEC}{REPASO}
{SCRIPT}
</body></html>"""
os.makedirs(f"{ROOT}/03-build/web/print",exist_ok=True)
open(f"{ROOT}/03-build/web/print/C4_U4.html","w",encoding="utf-8").write(HTML)
print("C4_U4.html (print+editable) geschreven:",len(HTML),"bytes")
