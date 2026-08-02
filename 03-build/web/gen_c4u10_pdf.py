#!/usr/bin/env python3
# C4 · Unidad 10 — PRINT (HTML=bron → PDF via Chromium). Golden-sample print-kit, C4-rood.
# Thema: Las tareas de casa · hay que ↔ tengo que · saber + infinitivo (↔ poder) · ofrecer/pedir ayuda.
# NB: de video komt (zoals U8–U9) uit Google Drive → de QR verwijst naar de HTML-hub, niet naar Drive.
import base64, os, re, segno, io, sys
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
from funciones_print import print_section
FUNCIONES_SEC=print_section(10)
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
HUB_URL="https://hablacon-ene.local/C4/U10"
import comprension_print
COMPR_SEC=comprension_print.print_section(10, HUB_URL)
SPOTIFY="https://open.spotify.com/playlist/37i9dQZF1DXaxEKcoCdWHD"

SCENES=[
 ("Escena 1 · «Yo te ayudo»",[
  ("Julio","Perdona, ¿qué haces?"),
  ("María","Limpiar el polvo, la asistenta está enferma. Hay que limpiar esto."),
  ("Julio","Yo te ayudo."),
  ("María","No tienes que molestarte."),
  ("Julio","No es molestia, te ayudo. ¿Qué tengo que hacer?"),
  ("María","Ah, pues puedes ordenar los armarios, las estanterías."),
  ("Julio","También puedo pasar la aspiradora."),
  ("Julio","Claro, yo no soy machista: los hombres también sabemos pasar la aspiradora."),
  ("María","Ahí está la aspiradora."),
 ]),
 ("Escena 2 · Llega Paul",[
  ("Paul","¿Qué hacéis?"),
  ("Julio","Limpiar un poco. Hoy no tenemos asistenta."),
  ("María","No puede venir en toda la semana, está enferma."),
  ("Paul","Déjame, lo hago yo."),
  ("Julio","Pero, ¿sabes pasar la aspiradora?"),
  ("María","¿Sabes cómo funciona?"),
  ("Paul","Claro que sé cómo funciona. Lo que pasa es que esto no funciona."),
  ("Paul","¡Ahí está!"),
 ]),
 ("Escena 3 · Fernando y Josefina observan",[
  ("Fernando","¿Qué hacen?"),
  ("Josefina","Julio quiere a María. María quiere a Julio, pero Paul es más guapo."),
  ("Josefina","Paul es inglés, así que nadie sabe exactamente qué quiere él."),
  ("Fernando","¿Y qué limpian? Van a dejar la academia muy muy limpia."),
 ]),
]
CH=["¿qué haces?","Limpiar el polvo","está enferma","Hay que limpiar","Yo te ayudo","No tienes que molestarte","No es molestia","¿Qué tengo que hacer?","puedes ordenar los armarios","las estanterías","puedo pasar la aspiradora","sabemos pasar la aspiradora","¿Qué hacéis?","no tenemos asistenta","No puede venir","Déjame, lo hago yo","¿sabes pasar la aspiradora?","¿Sabes cómo funciona?","sé cómo funciona","no funciona","¡Ahí está!"]
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
 ("Las tareas de casa",[("limpiar el polvo","afstoffen"),("pasar la aspiradora","stofzuigen"),
   ("fregar los platos","de vaat doen"),("ordenar los armarios","de kasten opruimen"),
   ("hacer la cama","het bed opmaken"),("planchar · cocinar","strijken · koken")]),
 ("Ofrecer ayuda · hulp aanbieden",[("Yo te ayudo","Ik help je"),("¿Te ayudo?","Help ik je?"),
   ("No es molestia","Het is geen moeite"),("Déjame, lo hago yo","Laat mij maar, ik doe het"),
   ("No tienes que molestarte","Je hoeft geen moeite te doen")]),
 ("Pedir instrucciones",[("¿Qué tengo que hacer?","Wat moet ik doen?"),("¿Y ahora?","En nu?"),
   ("¿Dónde está…?","Waar is…?"),("¿Sabes cómo funciona?","Weet je hoe het werkt?"),("¿Me ayudas?","Help je me?")]),
 ("Hay que… · het moet gebeuren",[("Hay que limpiar","Er moet gepoetst worden"),("Hay que ordenar esto","Dit moet opgeruimd"),
   ("Tengo que fregar","Ík moet de vaat doen"),("Tienes que planchar","Jíj moet strijken")]),
 ("Sé / no sé · wat je kunt",[("Sé pasar la aspiradora","Ik kan stofzuigen"),("Claro que sé","Natuurlijk kan ik dat"),
   ("No sé cocinar","Ik kan niet koken"),("Sabemos limpiar","Wij kunnen poetsen")]),
 ("En la academia · problemitas",[("está enferma","zij is ziek"),("no puede venir","zij kan niet komen"),
   ("no funciona","het werkt niet"),("¡Ahí está!","Daar is het! / Gelukt!"),("¡Qué desorden!","Wat een rommel!")]),
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
  <div class="eyebrow">EL DESPEGUE · PARADA 10 · SURVIVAL IN SPANISH</div>
  <h1>Las tareas de casa</h1>
  <div class="sub">Zeggen wat er <b>moet gebeuren</b>, wat <b>jij</b> kunt, en <b>hulp aanbieden</b>. <span class="gloss">Las tareas de casa — hay que + infinitivo · tengo que + infinitivo · saber + infinitivo · yo te ayudo</span></div>
  <div class="q">Hay que limpiar esto. — Yo te ayudo. ¿Qué tengo que hacer?</div>
</section>
<div class="page">
  <div class="obj"><div class="se">Al final de esta unidad · Op het einde van deze les</div>
    <ul>
      <li><span class="ck">✓</span> <span><span class="es">Nombrar las <b>tareas de casa</b></span> <span class="nl">— limpiar el polvo · pasar la aspiradora · fregar los platos</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Decir lo que hay que hacer con <b>hay que</b> + infinitivo</span> <span class="nl">— hay que limpiar (algemeen) ↔ tengo que limpiar (ík)</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Decir lo que sé hacer con <b>saber</b> + infinitivo</span> <span class="nl">— sé pasar la aspiradora · no sé cocinar</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es"><b>Ofrecer</b> y <b>pedir</b> ayuda</span> <span class="nl">— yo te ayudo · ¿qué tengo que hacer? · no es molestia</span></span></li>
    </ul>
  </div>
  <div class="guide"><span class="ic">🎒</span><div><span class="hand">¡Seguimos la ruta! Parada 10.</span><div class="g">De poetshulp van de academie is ziek — <i>la asistenta está enferma</i> — dus moeten Julio, María en Paul het zélf doen. In de video hoor je precies de taal die je nodig hebt om samen werk te verdelen: wat moet er gebeuren, wie doet wat, en wie kán wat.</div></div></div>

  <div class="se" style="margin-top:5mm">La máquina de frases · drie manieren, één patroon</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Drie vaste formules, en ná élk komt <b>het hele werkwoord</b> (de <i>infinitivo</i>). Het verschil zit in <b>wie</b>:</p>
  <div class="maq">
    <div class="m1">Hay que<small>het moet gebeuren</small></div><div class="m2">+ infinitivo<small>het hele werkwoord</small></div><div class="m3">limpiar · fregar<small>→ Hay que limpiar.</small></div>
  </div>
  <div class="maq">
    <div class="m1">Tengo que<small>ík moet</small></div><div class="m2">+ infinitivo<small>het hele werkwoord</small></div><div class="m3">fregar · planchar<small>→ Tengo que fregar.</small></div>
  </div>
  <div class="maq">
    <div class="m1">Sé<small>ik kán het (geleerd)</small></div><div class="m2">+ infinitivo<small>het hele werkwoord</small></div><div class="m3">cocinar · planchar<small>→ Sé cocinar.</small></div>
  </div>

  <div class="truc" style="margin-top:4mm"><b>¿Qué reconoces ya?</b> Deze huis-woorden lijken op het Nederlands/Engels of ken je al (<i>palabras transparentes</i>):
    <div class="cogn"><span>la aspiradora</span><span>el armario</span><span>la academia</span><span>el polvo</span><span>la asistenta</span><span>funcionar</span><span>ordenar</span><span>el problema</span><span>el orden</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Tip: <b>funcionar</b> ≈ functioneren · <b>ordenar</b> ≈ ordenen · <b>el armario</b> ≈ armoire/kast.</span>
  </div>
</div>
"""

ESCUCHA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§1 · ¡Escucha!</div><h2>Bekijk de scène en lees mee</h2>
  <div class="audiorow">
    <div class="call"><span class="ic">🎬</span><div><b>Sitcom · Episodio 10 · ¡No tenemos asistenta!</b> Scan de code en bekijk de aflevering op de digitale pagina. De poetshulp is ziek, dus de academie moet zélf schoongemaakt worden. Luister eerst zónder te lezen; daarna lees je mee. Let op elk <b>hay que…</b> (het moet), elk <b>tengo que…</b> (ík moet) en elk <b>sé / ¿sabes…?</b> (kunnen).</div></div>
    <div class="qr"><div class="lab">Vídeo online</div>{qr(HUB_URL+"#escucha")}<div class="meta">hub · Escucha</div></div>
  </div>
  <div class="truc"><b>Antes de escuchar.</b> Welke <b>huistaken</b> ken je al in het Spaans — of kun je raden? Tarea 1: {wl('sm')} &nbsp; Tarea 2: {wl('sm')}</div>
  <div class="twocol">{scenehtml(*SCENES[0])}{scenehtml(*SCENES[1])}{scenehtml(*SCENES[2])}</div>
  <div class="ojo"><b>¡Ojo!</b> «<b>Hay que</b> limpiar» = het moet gepoetst worden (je zegt niet wie) — «<b>Tengo que</b> limpiar» = ík moet poetsen. En «<b>sé</b> pasar la aspiradora» = ik kán het (ik heb het geleerd), niet <s>puedo</s> in die betekenis.</div>

  <div class="se" style="margin-top:5mm">Después de escuchar · ¿Verdadero o falso?</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Kruis aan. Verbeter de <b>falsas</b> op de lijn.</p>
  <table class="vf">
    <tr><td>1. La asistenta está enferma y no puede venir.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>2. Julio no quiere ayudar a María.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>3. Julio dice que los hombres también saben pasar la aspiradora.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>4. Paul dice que no sabe cómo funciona la aspiradora.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
  </table>
</div>
"""

KIT=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Suena bien · pronunciación</div><h2>La <i>g</i> fuerte &amp; la <i>u</i> muda: <i>gue · gui</i></h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 1mm">Vóór <b>a, o, u</b> klinkt de <b>g</b> zoals in «goal»: «<b>g</b>uapo», «a<b>g</b>ua», «lue<b>g</b>o». Oefen online (QR §1).</p>
  <div class="cogn"><span>guapo</span><span>agua</span><span>luego</span><span>gato</span><span>algo</span><span>amigo</span></div>
  <p style="font-size:9.4pt;margin:2mm 0 1mm">Vóór <b>e</b> en <b>i</b> schrijf je <b>gue/gui</b> voor diezelfde /g/-klank — de <b>u</b> hóór je niet: «<b>gui</b>tarra» = «gi-tarra».</p>
  <div class="cogn"><span>guitarra</span><span>seguir</span><span>juguete</span><span>guerra</span><span>Miguel</span><span>hoguera</span></div>
  <div class="ojo"><b>¡Ojo!</b> Precies zoals bij <b>qu</b> (U7): de <b>u</b> is een <i>schrijftruc</i>. Laat je die u weg, dan wordt het de <b>jota</b> /x/ (U2): <b>ge</b>nte · <b>gi</b>mnasio · <b>ge</b>neral.</div>
  <div class="klemline"><b>Repaso · aguda o llana?</b> as·pi·ra·<span class="t">DO</span>·ra (llana) · or·de·<span class="t">NAR</span> (aguda) · ar·<span class="t">MA</span>·rio (llana) · lim·<span class="t">PIAR</span> (aguda)</div>

  <div class="se" style="margin-top:3mm">§2 · Kit de supervivencia</div><h2>De taal die je écht nodig hebt</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 2mm">Vink ☐ af telkens je een uitdrukking vlot kunt <b>naspreken</b>. Oefen ze online met audio.</p>
  <div class="kitwrap">{"".join(kittable(n,it) for n,it in CLUSTERS)}</div>
</div>
"""

GRAM=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§4 · Gramática en la práctica</div><h2>Kort en functioneel</h2>
  <div class="modelo"><b>🔎 Fíjate · kijk terug naar de scène.</b> Je hoorde het al: «<b>Hay que</b> limpiar esto» · «¿Qué <b>tengo que</b> hacer?» · «¿<b>Sabes</b> pasar la aspiradora?» — «Claro que <b>sé</b>». Ontdek zelf het patroon — <i>eerst betekenis, dan de regel.</i></div>
  <div class="regla"><span class="tag">hay que + infinitivo &nbsp;↔&nbsp; tener que + infinitivo</span>
    <div class="mv2" style="margin-top:1.5mm"><div class="m">🌐 <b>Hay que</b> limpiar esto.<br><i>Er moet gepoetst worden</i> — je zegt níet wie.</div><div class="f">🙋 <b>Tengo que</b> fregar. · <b>Tienes que</b> ordenar.<br><i>Ík moet · jíj moet</i> — wél een persoon.</div></div>
    <p style="font-size:9pt;margin:1mm 0 0">💡 <b>hay que</b> verandert nooit — net als <b>hay</b> (er is/er zijn). Handig als je taken opsomt zonder iemand aan te wijzen: <i>Hay que limpiar, hay que fregar, hay que planchar…</i></p>
  </div>
  <div class="regla"><span class="tag">saber + infinitivo (iets kúnnen) &nbsp;↔&nbsp; poder + infinitivo</span>
    <table class="gt2"><tr><td class="v">sé</td><td>ik kan / ik weet</td><td class="ex"><b>Sé</b> pasar la aspiradora.</td></tr>
    <tr><td class="v">¿sabes…?</td><td>kan jij…?</td><td class="ex">¿<b>Sabes</b> cómo funciona?</td></tr>
    <tr><td class="v">sabemos</td><td>wij kunnen</td><td class="ex">Los hombres también <b>sabemos</b> limpiar.</td></tr></table>
    <p style="font-size:9pt;margin:1mm 0 0">⚠️ Het Nederlands zegt <b>één</b> woord — «kunnen». Spaans kiest: <b>saber</b> = je hebt het <i>geleerd</i> (sé cocinar) · <b>poder</b> = het <i>lukt/mag</i> nu (no <b>puede</b> venir, está enferma). <b>Dé valstrik:</b> «ik kan koken» = <b>sé cocinar</b>, niet <s>puedo cocinar</s> (dat betekent: het lukt me vandaag).</p>
  </div>
  <div class="regla"><span class="tag">Ofrecer ayuda · zo bied je hulp aan</span>
    <div class="dial2"><div class="db">— ¿Qué haces? <b>Yo te ayudo.</b></div><div class="da">— <b>No tienes que molestarte.</b></div><div class="db">— <b>No es molestia.</b> ¿Qué <b>tengo que</b> hacer?</div><div class="da">— Pues <b>puedes</b> ordenar los armarios.</div></div>
    <p style="font-size:9pt;margin:1mm 0 0">👂 In de scène hoor je Paul ook «<b>Déjame</b>, lo hago yo» zeggen. Zulke bevelvormen mag je <b>herkennen</b> — je hoeft ze nog niet zelf te maken.</p>
  </div>
  <div class="truc"><b>Descubre el patrón · onderstreep en ontdek.</b> Onderstreep in elke zin het <b>hele werkwoord</b> (de infinitivo) en schrijf ernaast <i>wie</i> het moet doen: <b>algemeen</b>, <b>yo</b> of <b>tú</b>.
    <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.3">1. Hay que fregar los platos. → {wl('sm')} &nbsp; 2. Tienes que planchar. → {wl('sm')}<br>3. Tengo que hacer la cama. → {wl('sm')} &nbsp; 4. Hay que ordenar los armarios. → {wl('sm')}</div>
    <div style="margin-top:1.5mm;font-size:9.6pt">✍️ <b>Transforma:</b> «Hay que pasar la aspiradora» → maak er <i>ík moet</i> van: {wl('lg')}</div>
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

  {act(1,"Clasifica: tarea, ofrecer ayuda o «sé / no sé»",[("receptief","skill"),("5 min","")],
    '<p style="margin-left:12.5mm">Schrijf elke uitdrukking in de juiste kolom. Voeg onderaan één eigen voorbeeld toe.<br><span class="gloss">pasar la aspiradora · yo te ayudo · claro que sé · fregar los platos · no es molestia · no sé cocinar</span></p>'
    +'<div class="wcols" style="margin-left:12.5mm"><div class="wcol"><h4>Una tarea 🧹</h4><div class="fill"></div></div><div class="wcol"><h4>Ofrecer ayuda 🤝</h4><div class="fill"></div></div><div class="wcol"><h4>sé / no sé 💡</h4><div class="fill"></div></div><div class="wcol"><h4>Tu ejemplo</h4><div class="fill"></div></div></div>')}

  {act(2,"¿hay que · tengo que · tienes que?",[("gestuurd","skill"),("★☆☆","")],
    f'<p style="margin-left:12.5mm">Vul de juiste formule in. Let op de aanwijzing tussen ( ).</p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. ¡Qué desorden! {wl("sm")} ordenar. (algemeen) &nbsp; 2. Yo {wl("sm")} planchar. (ík)<br>3. María, {wl("sm")} hacer la cama. (jíj) &nbsp; 4. Hoy {wl("sm")} limpiar la academia. (algemeen)<br>5. Yo {wl("sm")} fregar los platos. (ík)</div>')}

  {act(3,"¿saber o poder?",[("gestuurd","skill"),("★★☆","")],
    f'<p style="margin-left:12.5mm"><b>saber</b> = je hebt het geléérd · <b>poder</b> = het lukt/mag nú. Vul aan met <i>sé · sabes · puedo · puede</i>.</p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. Yo {wl("sm")} planchar, mi madre me enseñó. &nbsp; 2. La asistenta no {wl("sm")} venir, está enferma.<br>3. ¿{wl("sm")} cocinar tú? &nbsp; 4. Hoy no {wl("sm")} ayudar, tengo que estudiar.</div>')}

  {act(4,"Relaciona · tarea ↔ objeto o lugar",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Trek een lijn tussen de taak en wat je ervoor nodig hebt (of waar je het doet).</p>'
    +'<table class="mtab" style="margin-left:12.5mm"><tr><td class="a">1. pasar la aspiradora</td><td><span class="ln"></span></td><td class="b">a. los platos 🍽️</td></tr>'
    +'<tr><td class="a">2. fregar</td><td><span class="ln"></span></td><td class="b">b. el dormitorio 🛏️</td></tr>'
    +'<tr><td class="a">3. planchar</td><td><span class="ln"></span></td><td class="b">c. la aspiradora 🧹</td></tr>'
    +'<tr><td class="a">4. hacer la cama</td><td><span class="ln"></span></td><td class="b">d. los armarios 🚪</td></tr>'
    +'<tr><td class="a">5. ordenar</td><td><span class="ln"></span></td><td class="b">e. la plancha 👕</td></tr></table>')}
</div>

<div class="page sec" style="break-before:page">
  <div class="se">§3 · Práctica · sigue</div><h2>Van gestuurd naar zelf zeggen</h2>

  {act(5,"Ordena la conversación",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Nummer de zinnen (1–5): probleem → wat moet gebeuren → hulp → taak → ¡gelukt!</p>'
    +'<div class="scramble" style="margin-left:12.5mm"><span>___ Yo te ayudo. ¿Qué tengo que hacer?</span><span>___ La asistenta está enferma y no puede venir.</span><span>___ Claro que sé. ¡Ahí está!</span><span>___ Entonces hay que limpiar nosotros.</span><span>___ ¿Sabes pasar la aspiradora?</span></div>')}

  {act(6,"Completa el diálogo · ofrecer ayuda",[("gestuurd","skill"),("★★☆","")],
    f'<p style="margin-left:12.5mm">Vul aan met: <i>Hay · ayudo · tengo · Sabes · sé · molestia</i>.</p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.5">'
    +f'— ¡Qué desorden! {wl("sm")} que limpiar esto.<br>— Yo te {wl("sm")}. ¿Qué {wl("sm")} que hacer?<br>— No tienes que molestarte. — No es {wl("sm")}.<br>— ¿{wl("sm")} pasar la aspiradora? — Claro que {wl("sm")}.</div>')}

  {act(7,"En mi casa · escribe la verdad",[("productie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Schrijf per taak wie het bij jou thuis doet — en of jíj het kunt.</p>'
    +f'<table class="wtab" style="margin-left:12.5mm;margin-top:2mm"><thead><tr><th style="width:50mm">La tarea</th><th style="width:44mm">¿Quién la hace?</th><th>¿Y yo? (sé / no sé)</th></tr></thead>'
    +'<tr><td style="height:10mm">fregar los platos</td><td></td><td></td></tr>'
    +'<tr><td style="height:10mm">pasar la aspiradora</td><td></td><td></td></tr>'
    +'<tr><td style="height:10mm">cocinar</td><td></td><td></td></tr>'
    +'<tr><td style="height:10mm">planchar</td><td></td><td></td></tr></table>')}

  {act(8,"Ofrece ayuda · en parejas",[("interactie","skill"),("★★★","")],
    '<p style="margin-left:12.5mm">Je buur is aan het poetsen. Bied 3× hulp aan; hij/zij weigert 1× («no tienes que molestarte») en geeft 2× een taak. Noteer wat jullie afspreken en zeg het daarna hardop.</p>'
    +f'<div style="margin-left:12.5mm;font-size:9.8pt;line-height:2.4;margin-top:1mm">1. Mi oferta: {wl("lg")} → Su respuesta: {wl("sm")}<br>2. Mi oferta: {wl("lg")} → Su respuesta: {wl("sm")}<br>3. Mi oferta: {wl("lg")} → Su respuesta: {wl("sm")}<br>☐ Lo hemos dicho en voz alta · we hebben het hardop gezegd</div>')}


</div>
"""

TAREA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§5 · Tarea final</div><h2>¿Quién hace qué?</h2>
  <div class="esen" style="margin-top:2mm"><b class="tt">Jouw opdracht.</b> Maak met je groep een <b>cuadro de tareas</b> voor de academie «Bienvenidos al español». Noteer <b>4 taken</b> die gedaan moeten worden (<b>hay que…</b>), zeg wat elk van jullie <b>kan</b> (<b>sé / no sé…</b>) en <b>verdeel</b> ze eerlijk (<b>tengo que… · tienes que… · yo te ayudo</b>). Stel jullie schema daarna voor aan de klas. <span class="gloss">Sin leer del papel — zonder van het blad af te lezen.</span></div>
  <div style="margin-top:4mm"><div class="se">Nuestro cuadro de tareas · vul in</div>
    <table class="cuadro"><thead><tr><th style="width:12mm"></th><th>Hay que… (la tarea)</th><th>¿Quién? (tengo/tienes que…)</th><th style="width:44mm">¿Sabe hacerlo? (sé / no sé)</th></tr></thead>
      <tr><td class="h">🧹</td><td></td><td></td><td></td></tr>
      <tr><td class="h">🍽️</td><td></td><td></td><td></td></tr>
      <tr><td class="h">👕</td><td></td><td></td><td></td></tr>
      <tr><td class="h">🚪</td><td></td><td></td><td></td></tr></table>
  </div>
  <div class="regla" style="margin-top:4mm"><span class="tag">Prepárate · vul eerst de frames in</span>
    <div style="margin-top:2mm;font-size:9.7pt;line-height:2.4">1. Lo que hay que hacer: <b>Hay que</b> {wl('sm')} y <b>hay que</b> {wl('sm')} .<br>2. Lo que sé hacer: <b>Yo sé</b> {wl('lg')} . &nbsp; Pero <b>no sé</b> {wl('sm')} .<br>3. El reparto: Tú <b>tienes que</b> {wl('sm')} y yo <b>tengo que</b> {wl('sm')} . <b>Yo te ayudo.</b></div>
  </div>
  <div class="modelo" style="margin-top:4mm"><b>Modelo · zo klinkt het:</b><br>
    — Hay que limpiar el polvo y hay que fregar los platos. ¿Qué sabes hacer tú?<br>
    — Yo sé fregar, pero no sé planchar. — Vale: tú tienes que fregar y yo tengo que planchar.<br>
    — ¿Y la aspiradora? — Yo te ayudo. Claro que sé pasar la aspiradora. ¡No es molestia!</div>
  <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div class="truc" style="margin:0"><b>🏁 Klaar als…</b> je 4 taken noemt met «hay que + werkwoord», zegt wat je wél/niet kunt met «(no) sé + werkwoord», de taken verdeelt met «tengo/tienes que» en één keer hulp aanbiedt met «yo te ayudo» — zónder af te lezen.</div>
    <table class="rubric"><thead><tr><th>Evaluatie</th><th style="text-align:center">🟢🟡🔴</th></tr></thead>
      <tr><td>hay que + infinitivo correct</td><td></td></tr>
      <tr><td>saber + infinitivo correct (sé / no sé)</td><td></td></tr>
      <tr><td>hulp aanbieden &amp; taken verdelen</td><td></td></tr></table>
  </div>
</div>
"""

BANDAS=[("Rosalía","Malamente","🇪🇸 España"),("Bebe","Ella","🇪🇸 España"),("Ana Tijoux","1977","🇨🇱 Chile"),
 ("Manu Chao","Me Gustas Tú","🇪🇸/🇫🇷"),("Natalia Lafourcade","Hasta la Raíz","🇲🇽 México"),("Juanes","La Camisa Negra","🇨🇴 Colombia")]
def banda(a,s,g): return f'<div class="banda"><div class="ar">{a}</div><div class="sg">🎵 {s}</div><div class="ge">{g}</div></div>'
MUSICA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Cultura · Banda sonora</div><h2>El reparto de las tareas</h2>
  <p style="font-size:9.6pt">Julio zegt het zelf in de scène: «<b>yo no soy machista: los hombres también sabemos pasar la aspiradora</b>». Dat is geen toeval — in Spanje en Latijns-Amerika is de eerlijke verdeling van huistaken (<b>el reparto de las tareas</b>) een levend gespreksonderwerp. Officiële cijfers laten zien dat vrouwen er nog altijd méér uren huishouden doen dan mannen, maar bij jonge koppels loopt het verschil zichtbaar terug. Een <b>asistenta</b> (poetshulp) is er trouwens gewoner dan bij ons, ook in gewone gezinnen. Elke unit heeft ook een <b>banda sonora</b>.</p>
  <div class="bandas">{"".join(banda(*b) for b in BANDAS)}</div>
  <div class="musrow">
    <div class="call"><span class="ic">🎧</span><div><b>Spotify · la playlist de la clase.</b> Scan en luister. Op de digitale pagina vind je ook <b>LyricsTraining</b> en de <b>wereldkaart</b>.</div></div>
    <div class="qr"><div class="lab">Playlist</div>{qr(SPOTIFY)}<div class="meta">Spotify</div></div>
  </div>
  <div class="truc" style="margin-top:5mm"><b>Las tareas en el mundo hispano · ¿sabías que…?</b> Verbind (gis gerust):
    <table class="mtab" style="margin-top:1mm"><tr><td class="a">«La asistenta» es…</td><td>{wl('sm')}</td><td class="b">a. het verdelen van de huistaken</td></tr>
    <tr><td class="a">«El reparto de las tareas» es…</td><td>{wl('sm')}</td><td class="b">b. de poetshulp</td></tr>
    <tr><td class="a">«Ser machista» es…</td><td>{wl('sm')}</td><td class="b">c. vrouwen als minderwaardig behandelen</td></tr></table>
    <p style="font-size:8.6pt;color:var(--mut);margin-top:1mm">💡 «Hay que limpiar» klinkt neutraal — precies daarom gebruik je het als je níet wil zeggen wie het moet doen. Wil je het wél duidelijk maken: <b>tengo que</b> / <b>tienes que</b>.</p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:3mm;align-items:start">
    <div class="truc" style="margin:0"><b>Escucha y responde.</b> Kies één nummer van de playlist.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.3">Mi canción: {wl('lg')}<br>La escucho cuando tengo que: {wl('lg')}</div>
    </div>
    <div class="truc" style="margin:0"><b>¿Y en tu casa?</b> Schrijf één taak die moet gebeuren en één die jij kunt.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.4">{wl('full')}<br>{wl('full')}</div>
    </div>
  </div>
</div>
"""

REPASO=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Repaso · Lo esencial de un vistazo</div><h2>Wat je nu kunt</h2>
  <div class="fams">
    <div class="pcard"><div class="t">Zo zeg je wat moet gebeuren</div><div class="ej"><b>Hay que</b> + infinitivo <i>(algemeen)</i> · <b>Tengo/Tienes que</b> + infinitivo <i>(persoon)</i></div><div class="t2">altijd <b>que</b> + het hele werkwoord</div></div>
    <div class="pcard"><div class="t">Zo zeg je wat je kunt</div><div class="ej"><b>Sé</b> + infinitivo · ¿<b>Sabes</b>…? · <b>No sé</b> + infinitivo</div><div class="anchor">saber = geleerd · poder = het lukt/mag nu</div></div>
  </div>
  <div class="regla" style="margin:4mm 0"><span class="tag">Cinco fórmulas, un patrón: + infinitivo</span>
    <p style="font-size:9pt;margin:0">Je kent er nu al een hele rij — en ze werken <b>allemaal</b> hetzelfde: vaste vorm + <b>het hele werkwoord</b>.</p>
    <div class="stackp">
      <div><b>voy a</b> limpiar<i>plan · U9</i></div>
      <div><b>tengo que</b> limpiar<i>ik moet · U9</i></div>
      <div><b>hay que</b> limpiar<i>het moet · nieuw</i></div>
      <div><b>sé</b> limpiar<i>ik kan het · nieuw</i></div>
      <div><b>puedo</b> limpiar<i>ik mag/kan · U6</i></div>
    </div>
  </div>
  <div class="regla" style="margin:4mm 0"><span class="tag">Frases para la clase</span>
    <div class="cogn" style="margin-top:1mm"><span>¿Te ayudo?</span><span>¿Qué tengo que hacer?</span><span>No es molestia</span><span>¿Sabes cómo funciona?</span><span>No funciona</span><span>¡Ahí está!</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Handige klaszinnen — gebruik ze in het Spaans i.p.v. Nederlands.</span>
  </div>
  <table class="sem"><thead><tr><th style="text-align:left">Puedo… · Ik kan…</th><th>🟢</th><th>🟡</th><th>🔴</th></tr></thead>
    <tr><td>de huistaken benoemen (limpiar el polvo · fregar…)</td><td></td><td></td><td></td></tr>
    <tr><td>zeggen wat moet gebeuren (hay que + infinitivo)</td><td></td><td></td><td></td></tr>
    <tr><td>zeggen wat ik kan (sé / no sé + infinitivo)</td><td></td><td></td><td></td></tr>
    <tr><td>hulp aanbieden en om instructies vragen</td><td></td><td></td><td></td></tr></table>
  <div class="regla" style="margin-top:5mm"><span class="tag">Mini-test · recuerda sin mirar</span>
    <p style="margin:1mm 0 0;font-size:9.4pt">Sluit de cursus en vertaal uit het hoofd (ophalen = het beste leren).</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3mm 8mm;margin-top:2mm;font-size:9.8pt;line-height:2.2">
      <div>1. er moet gepoetst worden → {wl('')}</div><div>2. ik help je → {wl('')}</div>
      <div>3. wat moet ik doen? → {wl('')}</div><div>4. ik kan stofzuigen → {wl('')}</div>
      <div>5. ik kan niet koken → {wl('')}</div><div>6. het werkt niet → {wl('')}</div>
    </div>
  </div>
  <div class="guide"><span class="ic">🎮</span><div><span class="hand">Repasa jugando</span><div class="g">Oefen alles online met spelletjes, flashcards en audio op de digitale hub (scan de QR bij §1).</div></div></div>
  <div class="bridge"><b>Próxima parada →</b> Seguimos la ruta: más español para sobrevivir. ¡Hasta pronto!</div>
</div>
"""

EDITBAR="""
<div class="editbar" id="eb">
  <b>✏️ C4 · U10</b>
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
document.getElementById('btnsave').onclick=function(){var html='<!doctype html>'+document.documentElement.outerHTML;var b=new Blob([html],{type:'text/html'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='C4_U10_Tareas_bewerkt.html';a.click();};
</script>
"""

HTML=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 10 · Las tareas de casa</title><style>{CSS}</style></head><body>
{EDITBAR}
{HERO}{ESCUCHA}{COMPR_SEC}{KIT}{GRAM}{PRAC}{TAREA}{MUSICA}{FUNCIONES_SEC}{REPASO}
{SCRIPT}
</body></html>"""
os.makedirs(f"{ROOT}/03-build/web/print",exist_ok=True)
open(f"{ROOT}/03-build/web/print/C4_U10.html","w",encoding="utf-8").write(HTML)
print("C4_U10.html (print+editable) geschreven:",len(HTML),"bytes")
