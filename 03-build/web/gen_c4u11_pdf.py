#!/usr/bin/env python3
# C4 · Unidad 11 — PRINT (HTML=bron → PDF via Chromium). Golden-sample print-kit, C4-rood.
# Thema: El tiempo y los gustos · hace + naamwoord (↔ tengo frío) · me gusta ↔ me gustan · frecuencia.
# NB: de video komt (zoals U8–U10) uit Google Drive → de QR verwijst naar de HTML-hub, niet naar Drive.
import base64, os, re, segno, io, sys
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
from funciones_print import print_section
FUNCIONES_SEC=print_section(11)
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
HUB_URL="https://hablacon-ene.local/C4/U11"
import comprension_print
COMPR_SEC=comprension_print.print_section(11, HUB_URL)
SPOTIFY="https://open.spotify.com/playlist/37i9dQZF1DXaxEKcoCdWHD"

SCENES=[
 ("Escena 1 · En el bar",[
  ("Camarero","Ella se va de vacaciones a la playa, a Canarias. Siempre hace buen tiempo en Canarias."),
  ("Camarero","Viaja con unos amigos; con un amigo, un inglés."),
  ("Camarero","Son cuatro cincuenta."),
  ("Julio","Yo no, yo voy al pueblo de mis padres, en Ávila. Está cerca de Madrid."),
  ("Camarero","Es bonito, Ávila."),
  ("Julio","Pero hace un frío. Nunca hace ese frío en Madrid."),
  ("Camarero","Lo bueno es que puedes estar con tu familia: pasas las fiestas de Navidad con los tuyos — tus padres, tus tíos, tus cuñados."),
  ("Julio","Exacto. A veces te cansas de restaurantes y playas y hoteles. En cambio, la familia es para siempre. ¿Y tú te quedas en Madrid?"),
  ("Camarero","Yo voy todos los años al Caribe. Es que me gusta hacer submarinismo."),
  ("Camarero","A ella también le gusta hacer submarinismo. ¿Por qué no lo intentas?"),
  ("Julio","En Ávila es difícil, ¿sabes? Yo voy mucho al cine."),
  ("Clienta","Me gusta el cine y me gusta la ópera."),
  ("Julio","Casi nunca voy a la ópera."),
  ("Clienta","Y los deportes: voy al gimnasio tres veces por semana y hago yoga."),
 ]),
 ("Escena 2 · En la calle",[
  ("Clienta","¡Uh, hace mucho viento! En invierno hace frío."),
  ("Clienta","Sí. En verano, en cambio, hace calor."),
  ("Julio","A mí me gusta más el frío."),
  ("Clienta","En mi casa hace calor."),
 ]),
]
CH=["se va de vacaciones","a la playa","Siempre hace buen tiempo","Son cuatro cincuenta","voy al pueblo de mis padres","hace un frío","Nunca hace ese frío","con los tuyos","tus cuñados","A veces te cansas","en cambio","para siempre","te quedas en Madrid","voy todos los años","me gusta hacer submarinismo","también le gusta","voy mucho al cine","Me gusta el cine","me gusta la ópera","Casi nunca voy","los deportes","Voy al gimnasio","tres veces por semana","Hago yoga","hace mucho viento","En invierno hace frío","En verano","hace calor","me gusta más el frío"]
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
 ("¿Qué tiempo hace?",[("Hace frío · hace calor","Het is koud · het is warm"),("Hace sol · hace viento","Het is zonnig · het waait"),
   ("Hace buen / mal tiempo","Het is mooi / slecht weer"),("Llueve · nieva","Het regent · het sneeuwt"),
   ("¿Qué tiempo hace?","Wat voor weer is het?"),("demasiado calor","te warm")]),
 ("Las estaciones y las vacaciones",[("la primavera · el verano","de lente · de zomer"),("el otoño · el invierno","de herfst · de winter"),
   ("en verano · en invierno","in de zomer · in de winter"),("irse de vacaciones","op vakantie gaan"),
   ("a la playa · al pueblo","naar het strand · naar het dorp"),("las fiestas de Navidad","de kerstdagen"),
   ("con los tuyos","bij de jouwen (je familie)"),("en cambio","daarentegen")]),
 ("Me gusta… · el ocio",[("Me gusta el cine","Ik hou van film"),("Me gusta hacer yoga","Ik doe graag yoga"),
   ("Me gustan los deportes","Ik hou van sport"),("No me gusta la ópera","Ik hou niet van opera"),
   ("el gimnasio · hacer submarinismo","de sportzaal · duiken"),("¿Te gusta…?","Hou jij van…?")]),
 ("Reaccionar",[("A mí también · a mí no","Ik ook · ik niet"),("A mí tampoco · a mí sí","Ik ook niet · ik wel"),
   ("¡Qué bien!","Wat goed!")]),
 ("¿Con qué frecuencia?",[("siempre · casi siempre","altijd · bijna altijd"),("a veces","soms"),
   ("casi nunca · nunca","bijna nooit · nooit"),("tres veces por semana","drie keer per week"),
   ("todos los años","elk jaar"),("Voy mucho al cine","Ik ga veel naar de cinema")]),
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
.p{color:#2563EB;font-weight:700}.v{color:#EA7317;font-weight:700}.o{color:#1E9E74;font-weight:700}.pl{color:#0E9E97;font-weight:700}.t{color:#7C3AED;font-weight:700}
.tl{display:flex;gap:3mm;padding:.45mm 0;font-size:9.3pt;break-inside:avoid}
.tl .sp{font-family:var(--disp);font-weight:700;color:var(--gd);width:20mm;flex:none}
.tl .tx b{background:var(--gt);border-radius:3pt;padding:.2mm 1.2mm;font-weight:700}
.twocol{column-count:2;column-gap:8mm}
.kitwrap{columns:2;column-gap:5mm;margin-top:2mm}
.kit{margin:0 0 3mm}
.kit{break-inside:avoid}
.kit-h{font-family:var(--disp);font-weight:700;font-size:9.6pt;color:var(--gd);margin:1mm 0 .5mm}
.ktab{font-size:8.8pt;width:100%}.ktab th{background:var(--gt);color:var(--gd);font-size:7.2pt;text-transform:uppercase;padding:.8mm 2mm;text-align:left}
.ktab td{border-bottom:1px solid var(--line);padding:.55mm 2mm}.k-es{font-weight:600}.k-ck{text-align:center;width:12mm}
.chk{display:inline-block;width:3.4mm;height:3.4mm;border:1.3px solid var(--mut);border-radius:1.5pt;vertical-align:middle}
.gt2{width:100%;font-size:9.2pt;margin:2mm 0}.gt2 td{border-bottom:1px solid var(--line);padding:1.5mm 2.5mm}
.gt2 .v{color:#EA7317;font-family:var(--disp)}.gt2 .ex{color:var(--mut);font-style:italic}
.mv2{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin:2mm 0}
.mv2 div{border-radius:8pt;padding:2.5mm 4mm;font-family:var(--disp)}
.mv2 .m{background:#FEF1E7;color:#B4530E}.mv2 .f{background:#E8F0FE;color:#1E40AF}
.maq{display:grid;grid-template-columns:auto auto auto;gap:0;align-items:stretch;margin:2mm 0;max-width:150mm}
.maq div{border:1.5px solid var(--line);padding:2.5mm 4mm;font-family:var(--disp);font-size:10pt;text-align:center}
.maq .m1{background:#FEF1E7;color:#B4530E;border-radius:8pt 0 0 8pt}
.maq .m2{background:var(--gt);color:var(--gd);border-left:none;border-right:none}
.maq .m3{background:#fff;border-radius:0 8pt 8pt 0}
.maq small{display:block;font-family:var(--body);font-size:7pt;color:var(--mut);font-weight:400}
.stackp{display:grid;grid-template-columns:repeat(5,1fr);gap:2.5mm;margin:2mm 0}
.stackp div{border:1px solid var(--line);border-left:3px solid var(--g);border-radius:0 7pt 7pt 0;padding:2mm 3mm;font-size:9pt;font-family:var(--disp);break-inside:avoid}
.stackp div i{display:block;font-family:var(--body);font-style:normal;font-size:7.2pt;color:var(--mut);font-weight:400}
.dial2{display:flex;flex-direction:column;gap:1.5mm;margin:2mm 0}
.dial2 .db,.dial2 .da{border-radius:8pt;padding:1.8mm 3.5mm;font-size:9.4pt;max-width:82%}
.dial2 .db{background:var(--crema);align-self:flex-start}
.dial2 .da{background:var(--gt);align-self:flex-end}
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
.cogn{display:flex;flex-wrap:wrap;gap:2mm;margin:2mm 0}.cogn span{background:var(--gt);border-radius:20pt;padding:.8mm 3mm;font-size:9.2pt;font-weight:600;color:var(--gd)}
.vf{width:100%;font-size:9.5pt;margin:2mm 0}.vf td{border-bottom:1px solid var(--line);padding:1.9mm 2mm}.vf .b{width:26mm;text-align:center;color:var(--mut);white-space:nowrap}
.modelo{border-left:3px solid var(--g);background:var(--gt);border-radius:0 8pt 8pt 0;padding:2.5mm 5mm;margin:2mm 0;font-size:9.7pt}
.modelo b{color:var(--gd)}
.rubric{width:100%;font-size:9pt;margin:2mm 0}.rubric th{background:var(--g);color:#fff;text-align:left;padding:1.6mm 2.4mm;font-size:8pt}.rubric td{border:1px solid var(--line);padding:1.6mm 2.4mm}
.bandas{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-top:3mm}
.banda{border:1px solid var(--line);border-radius:10pt;padding:3mm 4mm;break-inside:avoid}
.banda .ar{font-family:var(--disp);font-weight:700;font-size:10pt}.banda .sg{font-size:8.4pt;color:var(--mut)}.banda .ge{font-size:7.6pt;color:var(--gd)}
.musrow{display:grid;grid-template-columns:1fr auto;gap:5mm;align-items:center;margin-top:4mm}
.cuadro{width:100%;font-size:9pt;margin-top:2mm}
.cuadro th{background:var(--g);color:#fff;font-size:7.6pt;text-transform:uppercase;padding:1.4mm}
.cuadro td{border:1px solid var(--line);height:12mm;padding:1mm 2mm}
.cuadro td.h{background:var(--gt);color:var(--gd);font-family:var(--disp);font-weight:700;width:12mm;font-size:11pt;text-align:center}
.editbar{position:fixed;top:0;left:0;right:0;background:var(--gd);color:#fff;display:flex;gap:8px;align-items:center;padding:7px 12px;z-index:999;font-family:var(--body);font-size:13px;box-shadow:0 2px 10px #0003}
.editbar b{font-family:var(--disp)}.editbar button{border:0;background:#fff;color:var(--gd);font-weight:700;border-radius:8px;padding:6px 11px;cursor:pointer;font-size:12.5px}
.editbar button.on{background:#111;color:#fff}.editbar .sp{flex:1}.scr-spacer{height:44px}
body.editing .page{outline:1.5px dashed var(--g);outline-offset:-6px}
@media print{ .editbar,.scr-spacer{display:none!important} }
"""

HERO=f"""
<section class="hero">
  <div class="tab">C4 · LA RUTA</div>
  <div class="eyebrow">EL DESPEGUE · PARADA 11 · SURVIVAL IN SPANISH</div>
  <h1>El tiempo y los gustos</h1>
  <div class="sub">Praten over het <b>weer</b>, over wat je <b>graag doet</b> en <b>hoe vaak</b>. <span class="gloss">El tiempo y los gustos — hace frío/calor · me gusta / me gustan · siempre · a veces · casi nunca</span></div>
  <div class="q">¡Uh, hace mucho viento! — A mí me gusta más el frío.</div>
</section>
<div class="page">
  <div class="obj"><div class="se">Al final de esta unidad · Op het einde van deze les</div>
    <ul>
      <li><span class="ck">✓</span> <span><span class="es">Hablar del <b>tiempo</b> con <b>hace</b> + sustantivo</span> <span class="nl">— hace frío · hace calor · hace viento · ¿qué tiempo hace?</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Nombrar las <b>estaciones</b></span> <span class="nl">— la primavera · el verano · el otoño · el invierno</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Expresar <b>gustos</b>: me gusta ↔ me gustan</span> <span class="nl">— me gusta el cine · me gustan los deportes · a mí también</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Decir con qué <b>frecuencia</b></span> <span class="nl">— siempre · a veces · casi nunca · tres veces por semana</span></span></li>
    </ul>
  </div>
  <div class="guide"><span class="ic">🎒</span><div><span class="hand">¡Seguimos la ruta! Parada 11.</span><div class="g">In een bar praten Julio en de camarero over de vakantie: zij gaat naar de Canarische Eilanden, waar het <i>siempre hace buen tiempo</i>; hij gaat naar Ávila, waar het ijskoud is. Een clienta mengt zich in het gesprek en vertelt wat ze allemaal graag doet. Precies de taal die je nodig hebt om over het weer én over je smaak te praten.</div></div></div>

  <div class="se" style="margin-top:5mm">La máquina de frases · zo praat je over weer en smaak</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Twee vaste formules. De eerste verandert <b>nooit</b>; bij de tweede kiest <b>het ding</b> de vorm:</p>
  <div class="maq">
    <div class="m1">Hace<small>het weer «doet» iets</small></div><div class="m2">+ sustantivo<small>een naamwoord</small></div><div class="m3">frío · calor · viento<small>→ Hace frío.</small></div>
  </div>
  <div class="maq">
    <div class="m1">Me gusta<small>één ding / een werkwoord</small></div><div class="m2">+ el/la · infinitivo<small>enkelvoud</small></div><div class="m3">el cine · hacer yoga<small>→ Me gusta el cine.</small></div>
  </div>
  <div class="maq">
    <div class="m1">Me gustan<small>meer dan één ding</small></div><div class="m2">+ los/las<small>meervoud</small></div><div class="m3">los deportes<small>→ Me gustan los deportes.</small></div>
  </div>

  <div class="truc" style="margin-top:4mm"><b>¿Qué reconoces ya?</b> Deze woorden lijken op het Nederlands/Engels of ken je al (<i>palabras transparentes</i>):
    <div class="cogn"><span>el cine</span><span>la ópera</span><span>el gimnasio</span><span>el yoga</span><span>los deportes</span><span>las vacaciones</span><span>flexible</span><span>el restaurante</span><span>el hotel</span><span>la familia</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Tip: <b>el gimnasio</b> ≈ gymnasium · <b>los deportes</b> ≈ sport · <b>las vacaciones</b> ≈ vakantie.</span>
  </div>
</div>
"""

ESCUCHA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§1 · ¡Escucha!</div><h2>Bekijk de scène en lees mee</h2>
  <div class="audiorow">
    <div class="call"><span class="ic">🎬</span><div><b>Sitcom · Episodio 11 · Aquí hace demasiado calor.</b> Scan de code en bekijk de aflevering. Luister eerst zónder te lezen; daarna lees je mee. Let op elk <b>hace…</b>, elk <b>me gusta / me gustan</b> en elk frequentiewoord.</div></div>
    <div class="qr"><div class="lab">Vídeo online</div>{qr(HUB_URL+"#escucha")}<div class="meta">hub · Escucha</div></div>
  </div>
  <div class="truc"><b>Antes de escuchar.</b> Welk weer is het vandaag bij jou? En wat doe je graag? Weer: {wl('sm')} &nbsp; Me gusta: {wl('sm')}</div>
  <div class="twocol">{scenehtml(*SCENES[0])}{scenehtml(*SCENES[1])}</div>
  <div class="ojo"><b>¡Ojo!</b> «<b>Hace</b> frío» = het ís koud (het weer) — «<b>Tengo</b> frío» = <i>ík</i> heb het koud (U9). En «<b>Me gusta</b> el cine» betekent letterlijk «de cinema <i>bevalt mij</i>»: daarom nooit <s>yo gusto el cine</s>.</div>

  <div class="se" style="margin-top:5mm">Después de escuchar · ¿Verdadero o falso?</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Kruis aan. Verbeter de <b>falsas</b> op de lijn.</p>
  <table class="vf">
    <tr><td>1. En Canarias siempre hace buen tiempo.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>2. En Ávila hace mucho calor.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>3. Al camarero le gusta hacer submarinismo.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>4. A Julio le gusta más el calor.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
  </table>
</div>
"""

KIT=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Suena bien · pronunciación</div><h2>La <i>s</i> siempre es sorda</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 1mm">De Spaanse <b>s</b> is <b>altijd</b> scherp (zoals in «sok») — <b>nooit</b> zoals onze <b>z</b> in «zomer». Oefen online (QR §1).</p>
  <div class="cogn"><span>siempre</span><span>casi</span><span>gusta</span><span>estaciones</span><span>vacaciones</span><span>submarinismo</span></div>
  <p style="font-size:9.4pt;margin:1.5mm 0 1mm">Ook in de <b>-s</b> van het meervoud blijft ze scherp: <span class="cogn" style="display:inline-flex;margin:0"><span>los años</span><span>tres veces</span><span>mis primos</span><span>dos cosas</span></span></p>
  <div class="ojo"><b>¡Ojo!</b> Nederlandstaligen maken van «lo<b>s</b> año<b>s</b>» vaak «lo<b>z</b> año<b>z</b>». Houd de s scherp — dat is meteen hoorbaar. Herhaling U3: <b>c+e/i</b> en <b>z</b> klinken in Spanje als /θ/ (tong tussen de tanden): <b>c</b>ielo · <b>c</b>inco · do<b>c</b>e · <b>z</b>ona.</div>
  <div class="klemline"><b>El acento en los precios · uit de scène:</b> cua·<span class="t">TRO</span> cin·<span class="t">CUEN</span>·ta · vein·ti·<span class="t">CIN</span>·co · <span class="t">TREIN</span>·ta y <span class="t">DOS</span> · <span class="t">SEIS</span> <span class="t">EU</span>·ros</div>

  <div class="truc" style="margin-top:4mm"><b>① ¿/s/ o /θ/? · markeer wat je hoort.</b> Onderstreep in elk woord de letter die je als <b>/s/</b> hoort en omkring die met de <b>/θ/</b>-klank (c+e/i · z).
    <div class="cogn" style="margin-top:1.5mm"><span>cielo</span><span>siempre</span><span>zona</span><span>sol</span><span>cinco</span><span>casi</span><span>doce</span><span>seis</span><span>gracias</span><span>estación</span></div>
    <div style="margin-top:1.5mm;font-size:9.4pt">Schrijf twee woorden met <b>beide</b> klanken: {wl('lg')}</div>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:3mm;align-items:start">
    <div class="truc" style="margin:0"><b>② Dictado de precios.</b> Beluister de prijzen op de digitale pagina en schrijf ze in cijfers.
      <div style="margin-top:1.5mm;font-size:9.8pt;line-height:2.4">a) {wl('sm')} € &nbsp; b) {wl('sm')} €<br>c) {wl('sm')} € &nbsp; d) {wl('sm')} €<br>e) {wl('sm')} € &nbsp; f) {wl('sm')} €</div>
    </div>
    <div class="truc" style="margin:0"><b>③ Lee en voz alta · met je buur.</b> Lees elke zin luidop; je buur controleert de scherpe s. Zet ☐ als het lukt.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.2">☐ Siempre hace sol en las islas.<br>☐ Los sábados voy al gimnasio.<br>☐ Me gustan las estaciones secas.<br>☐ Son cuatro cincuenta, gracias.</div>
    </div>
  </div>

  <div class="truc" style="margin-top:3mm"><b>④ Escribe el precio en palabras.</b> Let op de klemtoon (die zetten we in <span class="t">kleur</span> als je hem hardop zegt).
    <table class="mtab" style="margin-top:1mm"><tr><td class="a" style="width:22mm">4,50 €</td><td>{wl('lg')}</td><td class="a" style="width:22mm">25 €</td><td>{wl('lg')}</td></tr>
    <tr><td class="a">32 €</td><td>{wl('lg')}</td><td class="a">6 €</td><td>{wl('lg')}</td></tr></table>
  </div>

  <div class="truc" style="margin-top:3mm"><b>⑤ Trabalenguas · de s-tongbreker.</b> Zeg deze zin drie keer, elke keer sneller — en houd élke s scherp. Zet ☐ per poging.
    <div style="margin-top:1mm;font-size:11pt;font-family:var(--disp);color:var(--gd)">«Los seis sábados de septiembre siempre hace sol.»</div>
    <div style="margin-top:1mm;font-size:9.6pt">☐ despacio &nbsp;&nbsp; ☐ normal &nbsp;&nbsp; ☐ rápido &nbsp;&nbsp; Mijn eigen s-zin: {wl('lg')}</div>
  </div>
</div>

<div class="page sec" style="break-before:page">
  <div class="se">§2 · Kit de supervivencia</div><h2>De taal die je écht nodig hebt</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 2mm">Vink ☐ af telkens je een uitdrukking vlot kunt <b>naspreken</b>. Oefen ze online met audio.</p>
  <div class="kitwrap">{"".join(kittable(n,it) for n,it in CLUSTERS)}</div>
  <div class="truc" style="margin-top:4mm"><b>Mi semana en cuatro frases.</b> Schrijf met de kit hierboven vier zinnen over jouw week: één over het <b>weer</b>, één met <b>me gusta</b>, één met <b>me gustan</b>, één met een <b>frequentiewoord</b>.
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1mm 6mm;margin-top:1.5mm;font-size:9.6pt;line-height:1.9">
      <div>🌤️ {wl('full')}</div><div>❤️ {wl('full')}</div>
      <div>❤️ {wl('full')}</div><div>🔁 {wl('full')}</div>
    </div>
    <div style="margin-top:1mm;font-size:9.2pt;color:var(--mut)">👥 Lees ze daarna voor aan je buur; hij/zij reageert met <b>a mí también · a mí tampoco · a mí no · a mí sí</b>.</div>
  </div>
</div>
"""

GRAM=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§4 · Gramática en la práctica</div><h2>Kort en functioneel</h2>
  <div class="modelo"><b>🔎 Fíjate · kijk terug naar de scène.</b> Je hoorde het al: «Siempre <b>hace</b> buen tiempo en Canarias» · «¡<b>Hace</b> mucho viento!» · «<b>Me gusta</b> el cine y <b>me gusta</b> la ópera» · «<b>Casi nunca</b> voy a la ópera». Ontdek zelf het patroon — <i>eerst betekenis, dan de regel.</i></div>
  <div class="regla"><span class="tag">hace + sustantivo · zo praat je over het weer</span>
    <table class="gt2"><tr><td class="v">hace frío / calor</td><td>het is koud / warm</td><td class="ex">En invierno <b>hace frío</b>.</td></tr>
    <tr><td class="v">hace viento / sol</td><td>het waait / het is zonnig</td><td class="ex">¡<b>Hace</b> mucho <b>viento</b>!</td></tr>
    <tr><td class="v">hace buen/mal tiempo</td><td>het is mooi/slecht weer</td><td class="ex">Siempre <b>hace buen tiempo</b> en Canarias.</td></tr></table>
    <div class="mv2" style="margin-top:1.5mm"><div class="m">🌤️ het <b>weer</b> → <b>hace</b> frío<br><i>het is koud (buiten)</i></div><div class="f">🙋 een <b>persoon</b> → <b>tengo</b> frío<br><i>ík heb het koud (U9)</i></div></div>
    <p style="font-size:9pt;margin:1mm 0 0">⚠️ <b>Dé valstrik:</b> nooit <s>es frío</s> of <s>está frío</s> voor het weer. De vorm <b>hace</b> verandert nooit — net als <b>hay</b> en <b>hay que</b>.</p>
  </div>
  <div class="regla"><span class="tag">me gusta ↔ me gustan · «het bevalt mij»</span>
    <div class="mv2"><div class="m">☝️ één ding of een werkwoord → <b>gusta</b><br><b>Me gusta</b> el cine. · <b>Me gusta</b> hacer yoga.</div><div class="f">✌️ meervoud → <b>gustan</b><br><b>Me gustan</b> los deportes.</div></div>
    <p style="font-size:9pt;margin:1mm 0 0">💡 Het Spaans draait de zin om: niet «ik hou van X», maar «X <b>bevalt mij</b>» — daarom kiest <b>het ding</b> de vorm, niet jij. ⚠️ Nooit <s>yo gusto el cine</s> (dat betekent «ik val in de smaak»!). Iemand anders? <b>te gusta</b> (jij) · <b>le gusta</b> (hij/zij): «A ella también <b>le gusta</b> hacer submarinismo.»</p>
  </div>
  <div class="regla"><span class="tag">Reaccionar · a mí también / a mí tampoco</span>
    <div class="dial2"><div class="db">— Me gusta el cine.</div><div class="da">— <b>A mí también.</b> (ik ook)</div><div class="db">— No me gusta la ópera.</div><div class="da">— <b>A mí tampoco.</b> (ik ook niet)</div></div>
    <p style="font-size:9pt;margin:1mm 0 0">💡 Bij een <b>positieve</b> zin: <b>a mí también</b> (ik ook) / <b>a mí no</b> (ik niet). Bij een <b>negatieve</b> zin: <b>a mí tampoco</b> (ik ook niet) / <b>a mí sí</b> (ik wel).</p>
  </div>
  <div class="truc"><b>Descubre el patrón · onderstreep en ontdek.</b> Onderstreep in elke zin wat de vorm van «gusta/gustan» bepaalt, en schrijf ernaast <b>1</b> (enkelvoud/werkwoord) of <b>+</b> (meervoud).
    <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.3">1. Me gustan las vacaciones. → {wl('sm')} &nbsp; 2. Me gusta hacer yoga. → {wl('sm')}<br>3. No me gustan los hoteles. → {wl('sm')} &nbsp; 4. Me gusta el frío. → {wl('sm')}</div>
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

  {act(1,"Clasifica: el tiempo, los gustos o la frecuencia",[("receptief","skill"),("5 min","")],
    '<p style="margin-left:12.5mm">Schrijf elke uitdrukking in de juiste kolom. Voeg onderaan één eigen voorbeeld toe.<br><span class="gloss">hace calor · me gustan los deportes · casi nunca · hace viento · me gusta el cine · tres veces por semana</span></p>'
    +'<div class="wcols" style="margin-left:12.5mm"><div class="wcol"><h4>El tiempo 🌤️</h4><div class="fill"></div></div><div class="wcol"><h4>Los gustos ❤️</h4><div class="fill"></div></div><div class="wcol"><h4>La frecuencia 🔁</h4><div class="fill"></div></div><div class="wcol"><h4>Tu ejemplo</h4><div class="fill"></div></div></div>')}

  {act(2,"¿gusta o gustan?",[("gestuurd","skill"),("★☆☆","")],
    f'<p style="margin-left:12.5mm">Vul <b>gusta</b> of <b>gustan</b> in. Kijk naar wat erna komt.</p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. Me {wl("sm")} el cine. &nbsp; 2. Me {wl("sm")} los deportes. &nbsp; 3. Me {wl("sm")} hacer yoga.<br>4. No me {wl("sm")} las vacaciones en hotel. &nbsp; 5. Me {wl("sm")} más el frío.</div>')}

  {act(3,"¿hace o tengo?",[("gestuurd","skill"),("★★☆","")],
    f'<p style="margin-left:12.5mm">Het <b>weer</b> → <b>hace</b> · een <b>persoon</b> → <b>tengo</b>. Vul aan.</p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. En invierno {wl("sm")} frío en Ávila. &nbsp; 2. ¡Brr! Yo {wl("sm")} frío.<br>3. Aquí {wl("sm")} demasiado calor. &nbsp; 4. Yo {wl("sm")} calor, ¿abrimos la ventana?<br>5. Hoy {wl("sm")} buen tiempo.</div>')}

  {act(4,"Relaciona · estación ↔ tiempo",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Trek een lijn tussen het seizoen (of de plek) en het passende weer.</p>'
    +'<table class="mtab" style="margin-left:12.5mm"><tr><td class="a">1. el invierno</td><td><span class="ln"></span></td><td class="b">a. hace mucho calor ☀️</td></tr>'
    +'<tr><td class="a">2. el verano</td><td><span class="ln"></span></td><td class="b">b. hace buen tiempo todo el año 🏝️</td></tr>'
    +'<tr><td class="a">3. el otoño</td><td><span class="ln"></span></td><td class="b">c. hace frío y nieva ❄️</td></tr>'
    +'<tr><td class="a">4. Canarias</td><td><span class="ln"></span></td><td class="b">d. hace un frío terrible 🥶</td></tr>'
    +'<tr><td class="a">5. Ávila en Navidad</td><td><span class="ln"></span></td><td class="b">e. hace viento y llueve 🍂</td></tr></table>')}

</div>

<div class="page sec" style="break-before:page">
  <div class="se">§3 · Práctica · sigue</div><h2>Van gestuurd naar zelf zeggen</h2>

  {act(5,"La escalera de frecuencia",[("gestuurd","skill"),("★☆☆","")],
    '<p style="margin-left:12.5mm">Nummer van <b>100 %</b> (1) naar <b>0 %</b> (5).</p>'
    +'<div class="scramble" style="margin-left:12.5mm"><span>___ a veces</span><span>___ nunca</span><span>___ siempre</span><span>___ casi nunca</span><span>___ casi siempre</span></div>')}

  {act(6,"Completa el diálogo",[("gestuurd","skill"),("★★☆","")],
    f'<p style="margin-left:12.5mm">Vul aan met: <i>hace · gusta · gustan · veces · también</i>.</p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.5">'
    +f'— ¡Uf! Aquí {wl("sm")} demasiado calor.<br>— A mí me {wl("sm")} más el frío.<br>— ¿Y los deportes? — Sí, me {wl("sm")} mucho. Voy al gimnasio tres {wl("sm")} por semana.<br>— ¡A mí {wl("sm")}!</div>')}

  {act(7,"¿Cómo reaccionas?",[("gestuurd","skill"),("★★☆","")],
    f'<p style="margin-left:12.5mm">Reageer met <b>a mí también · a mí tampoco · a mí no · a mí sí</b>. Let op + of −.</p><div style="margin-left:12.5mm;font-size:9.8pt;line-height:2.4">'
    +f'1. — Me gusta el cine. (jij ook) → {wl("lg")}<br>2. — No me gusta la ópera. (jij ook niet) → {wl("lg")}<br>3. — Me gustan los deportes. (jij niet) → {wl("lg")}<br>4. — No me gusta el calor. (jij wel) → {wl("lg")}</div>')}

  {act(8,"Mi semana · escribe la verdad",[("productie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Schrijf per activiteit hoe vaak je die doet — en of je ze graag doet.</p>'
    +f'<table class="wtab" style="margin-left:12.5mm;margin-top:2mm"><thead><tr><th style="width:46mm">La actividad</th><th style="width:46mm">¿Con qué frecuencia?</th><th>¿Te gusta? (me gusta / no me gusta)</th></tr></thead>'
    +'<tr><td style="height:10mm">ir al cine</td><td></td><td></td></tr>'
    +'<tr><td style="height:10mm">hacer deporte</td><td></td><td></td></tr>'
    +'<tr><td style="height:10mm">ir a la playa</td><td></td><td></td></tr>'
    +'<tr><td style="height:10mm">escuchar música</td><td></td><td></td></tr>'
    +'<tr><td style="height:10mm">…(tu actividad)</td><td></td><td></td></tr></table>')}


</div>
"""

TAREA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§5 · Tarea final</div><h2>Mi estación favorita</h2>
  <div class="esen" style="margin-top:2mm"><b class="tt">Jouw opdracht.</b> Maak je <b>ficha «El tiempo y yo»</b>: kies je <b>favoriete seizoen</b>, zeg welk <b>weer</b> het dan is (<b>hace…</b>), noem <b>twee smaken</b> (één met <b>me gusta</b>, één met <b>me gustan</b>) en zeg <b>hoe vaak</b> je iets doet. Doe daarna de <b>enquête</b>: vraag drie klasgenoten «¿Te gusta…?», reageer met «a mí también / a mí tampoco» en zoek iemand met dezelfde smaak. <span class="gloss">Sin leer del papel — zonder van het blad af te lezen.</span></div>
  <div style="margin-top:4mm"><div class="se">Mi ficha · El tiempo y yo</div>
    <table class="cuadro"><thead><tr><th style="width:12mm"></th><th style="width:52mm">Mi respuesta</th><th>La frase completa en español</th></tr></thead>
      <tr><td class="h">🌤️</td><td>Mi estación favorita</td><td></td></tr>
      <tr><td class="h">🌡️</td><td>En … hace…</td><td></td></tr>
      <tr><td class="h">❤️</td><td>Me gusta… (1 ding)</td><td></td></tr>
      <tr><td class="h">❤️</td><td>Me gustan… (meervoud)</td><td></td></tr>
      <tr><td class="h">🔁</td><td>¿Con qué frecuencia?</td><td></td></tr></table>
  </div>
  <div class="regla" style="margin-top:4mm"><span class="tag">Prepárate · vul eerst de frames in</span>
    <div style="margin-top:2mm;font-size:9.7pt;line-height:2.4">1. Mi estación favorita es {wl('sm')} . En {wl('sm')} <b>hace</b> {wl('sm')} .<br>2. <b>Me gusta</b> {wl('sm')} y <b>me gustan</b> {wl('sm')} . Pero no me gusta {wl('sm')} .<br>3. {wl('sm')} (siempre · a veces · casi nunca) voy a {wl('sm')} , {wl('sm')} veces por semana.</div>
  </div>
  <div class="modelo" style="margin-top:4mm"><b>Modelo · zo klinkt het:</b><br>
    — Mi estación favorita es el verano. En verano hace calor y hace sol.<br>
    — Me gusta ir a la playa y me gustan los deportes. Pero no me gusta la ópera.<br>
    — Casi siempre voy al gimnasio, tres veces por semana. ¿Y a ti? ¿Te gusta el deporte? — Sí. — ¡A mí también!</div>
  <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div class="truc" style="margin:0"><b>🏁 Klaar als…</b> je het weer van je seizoen zegt met «hace + naamwoord», twee smaken geeft (één keer <b>gusta</b>, één keer <b>gustan</b>), minstens één frequentiewoord gebruikt en in de enquête één keer «a mí también / a mí tampoco» zegt — zónder af te lezen.</div>
    <table class="rubric"><thead><tr><th>Evaluatie</th><th style="text-align:center">🟢🟡🔴</th></tr></thead>
      <tr><td>hace + naamwoord correct (het weer)</td><td></td></tr>
      <tr><td>me gusta ↔ me gustan correct</td><td></td></tr>
      <tr><td>frecuencia + reageren in de enquête</td><td></td></tr></table>
  </div>
</div>
"""

BANDAS=[("Manu Chao","Me Gustas Tú","🇪🇸/🇫🇷"),("Álvaro Soler","El Mismo Sol","🇪🇸 España"),("Juan Luis Guerra","Ojalá Que Llueva Café","🇩🇴 R. Dominicana"),
 ("Carlos Vives & Shakira","La Bicicleta","🇨🇴 Colombia"),("Jarabe de Palo","Bonito","🇪🇸 España"),("Gente de Zona & Marc Anthony","La Gozadera","🇨🇺 Cuba")]
def banda(a,s,g): return f'<div class="banda"><div class="ar">{a}</div><div class="sg">🎵 {s}</div><div class="ge">{g}</div></div>'
MUSICA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Cultura · Banda sonora</div><h2>Un idioma, 21 climas</h2>
  <p style="font-size:9.6pt">Julio heeft gelijk: op de <b>Canarias</b> is het het hele jaar 20–24 °C — en <b>Guatemala</b> heet zelfs «het land van de eeuwige lente». Maar <b>Ávila</b>, waar zijn ouders wonen, is de <b>koudste provincie van Spanje</b> (1.130 m hoog): «nunca hace ese frío en Madrid». In <b>Argentinië, Chili en Uruguay</b> staan de seizoenen <b>omgekeerd</b>: daar is december <b>zomer</b> en viert men Kerstmis in de hitte. En in <b>Costa Rica</b> of <b>El Salvador</b> betekent «invierno» niet koud, maar <b>regenseizoen</b>. Elke unit heeft ook een <b>banda sonora</b> — «Me gustas tú» van Manu Chao is één lange me-gusta-oefening.</p>
  <div class="bandas">{"".join(banda(*b) for b in BANDAS)}</div>
  <div class="musrow">
    <div class="call"><span class="ic">🎧</span><div><b>Spotify · la playlist de la clase.</b> Scan en luister. Op de digitale pagina vind je ook <b>LyricsTraining</b> («Me gustas tú») en de <b>wereldkaart</b> met het klimaat per land.</div></div>
    <div class="qr"><div class="lab">Playlist</div>{qr(SPOTIFY)}<div class="meta">Spotify</div></div>
  </div>
  <div class="truc" style="margin-top:5mm"><b>El clima del mundo hispano · ¿sabías que…?</b> Verbind (gis gerust):
    <table class="mtab" style="margin-top:1mm"><tr><td class="a">Canarias / Guatemala…</td><td>{wl('sm')}</td><td class="b">a. daar is december zomer</td></tr>
    <tr><td class="a">Argentina y Chile…</td><td>{wl('sm')}</td><td class="b">b. «eterna primavera», 20–24 °C</td></tr>
    <tr><td class="a">En Costa Rica «invierno» es…</td><td>{wl('sm')}</td><td class="b">c. het regenseizoen (geen kou)</td></tr></table>
    <p style="font-size:8.6pt;color:var(--mut);margin-top:1mm">💡 In het Spaans <b>doet</b> het weer iets: <b>hace</b> frío · <b>hace</b> calor. Maar als jíj het koud hebt: <b>tengo</b> frío.</p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:3mm;align-items:start">
    <div class="truc" style="margin:0"><b>Escucha y responde.</b> Kies één nummer van de playlist.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.3">Mi canción: {wl('lg')}<br>La escucho cuando hace: {wl('lg')}</div>
    </div>
    <div class="truc" style="margin:0"><b>¿Y tú?</b> Schrijf welk weer je graag hebt en wat je dan doet.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.4">{wl('full')}<br>{wl('full')}</div>
    </div>
  </div>
</div>
"""

REPASO=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Repaso · Lo esencial de un vistazo</div><h2>Wat je nu kunt</h2>
  <div class="fams">
    <div class="pcard"><div class="t">Zo praat je over het weer</div><div class="ej"><b>Hace</b> frío · calor · viento · sol · buen/mal tiempo · ¿Qué tiempo <b>hace</b>?</div><div class="t2">hace verandert nooit — net als hay</div></div>
    <div class="pcard"><div class="t">Zo zeg je wat je graag hebt</div><div class="ej"><b>Me gusta</b> el cine / hacer yoga · <b>Me gustan</b> los deportes</div><div class="anchor">het ding kiest de vorm · a mí también / a mí tampoco</div></div>
  </div>
  <div class="regla" style="margin:4mm 0"><span class="tag">La escalera de frecuencia · van 100 % naar 0 %</span>
    <div class="stackp">
      <div><b>siempre</b><i>altijd · 100 %</i></div>
      <div><b>casi siempre</b><i>bijna altijd</i></div>
      <div><b>a veces</b><i>soms</i></div>
      <div><b>casi nunca</b><i>bijna nooit</i></div>
      <div><b>nunca</b><i>nooit · 0 %</i></div>
    </div>
    <p style="font-size:9pt;margin:1mm 0 0">Precies zeggen? Achteraan: <b>tres veces por semana</b> · <b>todos los años</b> · <b>voy mucho al cine</b>.</p>
  </div>
  <div class="regla" style="margin:4mm 0"><span class="tag">Frases para la clase</span>
    <div class="cogn" style="margin-top:1mm"><span>¿Qué tiempo hace?</span><span>¿Te gusta…?</span><span>A mí también</span><span>A mí tampoco</span><span>¡Qué bien!</span><span>En cambio…</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Handige klaszinnen — gebruik ze in het Spaans i.p.v. Nederlands.</span>
  </div>
  <table class="sem"><thead><tr><th style="text-align:left">Puedo… · Ik kan…</th><th>🟢</th><th>🟡</th><th>🔴</th></tr></thead>
    <tr><td>over het weer praten (hace frío · hace calor)</td><td></td><td></td><td></td></tr>
    <tr><td>de seizoenen benoemen (verano · invierno…)</td><td></td><td></td><td></td></tr>
    <tr><td>zeggen wat ik graag heb (me gusta ↔ me gustan)</td><td></td><td></td><td></td></tr>
    <tr><td>reageren op iemands smaak (a mí también/tampoco)</td><td></td><td></td><td></td></tr>
    <tr><td>zeggen hoe vaak (siempre · a veces · casi nunca)</td><td></td><td></td><td></td></tr></table>
  <div class="regla" style="margin-top:5mm"><span class="tag">Mini-test · recuerda sin mirar</span>
    <p style="margin:1mm 0 0;font-size:9.4pt">Sluit de cursus en vertaal uit het hoofd (ophalen = het beste leren).</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3mm 8mm;margin-top:2mm;font-size:9.8pt;line-height:2.2">
      <div>1. het is koud → {wl('')}</div><div>2. ik heb het koud → {wl('')}</div>
      <div>3. ik hou van film → {wl('')}</div><div>4. ik hou van sport → {wl('')}</div>
      <div>5. ik ook (niet) → {wl('')}</div><div>6. drie keer per week → {wl('')}</div>
    </div>
  </div>
  <div class="guide"><span class="ic">🎮</span><div><span class="hand">Repasa jugando</span><div class="g">Oefen alles online met spelletjes, flashcards en audio op de digitale hub (scan de QR bij §1).</div></div></div>
  <div class="bridge"><b>Próxima parada →</b> Seguimos la ruta: más español para sobrevivir. ¡Hasta pronto!</div>
</div>
"""

EDITBAR="""
<div class="editbar" id="eb">
  <b>✏️ C4 · U11</b>
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
document.getElementById('btnsave').onclick=function(){var html='<!doctype html>'+document.documentElement.outerHTML;var b=new Blob([html],{type:'text/html'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='C4_U11_Tiempo_bewerkt.html';a.click();};
</script>
"""

HTML=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 11 · El tiempo y los gustos</title><style>{CSS}</style></head><body>
{EDITBAR}
{HERO}{ESCUCHA}{COMPR_SEC}{KIT}{GRAM}{PRAC}{TAREA}{MUSICA}{FUNCIONES_SEC}{REPASO}
{SCRIPT}
</body></html>"""
os.makedirs(f"{ROOT}/03-build/web/print",exist_ok=True)
open(f"{ROOT}/03-build/web/print/C4_U11.html","w",encoding="utf-8").write(HTML)
print("C4_U11.html (print+editable) geschreven:",len(HTML),"bytes")
