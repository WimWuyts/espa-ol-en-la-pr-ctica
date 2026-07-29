#!/usr/bin/env python3
# C4 · Unidad 6 — PRINT (HTML=bron → PDF via Chromium). Golden-sample print-kit, C4-rood.
# Thema: La casa y los lugares · preposiciones de lugar · ¿dónde está? · hay/está · poder (permiso). Zelfde pijplijn als U1–U5.
import base64, os, re, segno, io, sys
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
from funciones_print import print_section
FUNCIONES_SEC=print_section(6)
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
HUB_URL="https://hablacon-ene.local/C4/U6"
import comprension_print
COMPR_SEC=comprension_print.print_section(6, HUB_URL)
SPOTIFY="https://open.spotify.com/playlist/37i9dQZF1DXaxEKcoCdWHD"

SCENES=[
 ("Escena 1 · La casa y las cosas de María",[
  ("Fernando","¡Qué frío! Buenos días."),
  ("Julio","Buenos días. Necesito café urgente, tengo mucho sueño. Estoy nervioso."),
  ("Julio","María es maravillosa, pero veo cómo entra en mi casa."),
  ("Julio","Deja su crema en el cuarto de baño, se olvida el bolso en la cocina."),
  ("Julio","Hay cosas encima de todas las sillas, debajo de la cama."),
  ("Julio","Dentro del frigorífico tengo tres botellas de leche."),
  ("Julio","Ella quiere una casa, un nido."),
  ("Julio","Quiero fumar. ¿Puedo fumar?"),
  ("Fernando","Aquí dentro no, pero puedes ir fuera."),
 ]),
 ("Escena 2 · ¿Quién es Paul?",[
  ("Julio","¿Tú puedes hablar con María?"),
  ("Fernando","No sé qué hace con Paul."),
  ("Julio","¿Quién es Paul?"),
  ("Fernando","Un alumno de primero. Un empresario inglés con mucho éxito."),
  ("María","Buenos días."),
  ("Julio","Buenos días."),
 ]),
]
CH=["encima de","debajo de","dentro del","el cuarto de baño","la cocina","la cama","el frigorífico","¿Puedo fumar?","puedes ir fuera","tengo mucho sueño","Estoy nervioso","una casa","un nido","la crema","el bolso","las sillas","tres botellas de leche"]
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
 ("Las habitaciones",[("la cocina","de keuken"),("el salón","de woonkamer"),("el dormitorio","de slaapkamer"),
   ("el cuarto de baño","de badkamer"),("la entrada · el pasillo","de hal · de gang")]),
 ("En casa · muebles y cosas",[("la cama","het bed"),("el sofá · la mesa","de bank · de tafel"),("el armario","de kast"),
   ("el frigorífico","de koelkast"),("la ventana · la puerta","het raam · de deur")]),
 ("¿Dónde está? · preposiciones",[("encima de","op / boven"),("debajo de","onder"),("dentro de","in / binnen"),
   ("al lado de","naast"),("delante de · detrás de","voor · achter")]),
 ("Situar · hay & está",[("¿Dónde está…?","Waar is…?"),("está en…","het is in/op…"),
   ("hay … en la cocina","er is … in de keuken"),("aquí · ahí · fuera","hier · daar · buiten")]),
 ("Pedir permiso · poder",[("¿Puedo…?","Mag/kan ik…?"),("¿Puedes…?","Kan/mag jij…?"),
   ("Sí, puedes… · Aquí no","Ja, je mag… · Hier niet"),("puedes ir fuera","je mag naar buiten")]),
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
.prep2{display:grid;grid-template-columns:repeat(4,1fr);gap:2.5mm;margin:2mm 0}
.prep2 div{background:#E6F7F5;border-radius:7pt;padding:2mm;font-family:var(--disp);text-align:center}
.prep2 b{display:block;color:#0B7A73;font-size:9.4pt}.prep2 i{font-size:7.4pt;color:var(--mut);font-style:normal}
.mv2{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin:2mm 0}
.mv2 div{border-radius:8pt;padding:2.5mm 4mm;font-family:var(--disp)}
.mv2 .m{background:#FEF1E7;color:#B4530E}.mv2 .f{background:#E9F7EF;color:#1E7A4E}
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
.plano{display:grid;grid-template-columns:1fr 1fr;gap:0;border:2px solid var(--g);border-radius:8pt;overflow:hidden;margin:2mm 0}
.plano div{border:1px solid var(--line);min-height:26mm;padding:2mm;font-family:var(--disp);font-size:8.4pt;color:var(--mut)}
.editbar{position:fixed;top:0;left:0;right:0;background:var(--gd);color:#fff;display:flex;gap:8px;align-items:center;padding:7px 12px;z-index:999;font-family:var(--body);font-size:13px;box-shadow:0 2px 10px #0003}
.editbar b{font-family:var(--disp)}.editbar button{border:0;background:#fff;color:var(--gd);font-weight:700;border-radius:8px;padding:6px 11px;cursor:pointer;font-size:12.5px}
.editbar button.on{background:#111;color:#fff}.editbar .sp{flex:1}.scr-spacer{height:44px}
body.editing .page{outline:1.5px dashed var(--g);outline-offset:-6px}
@media print{ .editbar,.scr-spacer{display:none!important} }
"""

HERO=f"""
<section class="hero">
  <div class="tab">C4 · LA RUTA</div>
  <div class="eyebrow">EL DESPEGUE · PARADA 6 · SURVIVAL IN SPANISH</div>
  <h1>La casa y los lugares</h1>
  <div class="sub">De <b>kamers</b> van een huis benoemen en zeggen <b>waar</b> alles staat. <span class="gloss">La casa y los lugares — ¿dónde está? · encima de · debajo de · hay · ¿puedo…?</span></div>
  <div class="q">¿Dónde está el bolso? — Está encima de la mesa.</div>
</section>
<div class="page">
  <div class="obj"><div class="se">Al final de esta unidad · Op het einde van deze les</div>
    <ul>
      <li><span class="ck">✓</span> <span><span class="es">Benoemen: de kamers &amp; meubels</span> <span class="nl">— la cocina · el salón · la cama · el armario</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Situeren met <b>preposiciones de lugar</b></span> <span class="nl">— encima de · debajo de · al lado de · dentro de</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Vragen &amp; zeggen waar iets is (<b>hay</b> / <b>está</b>)</span> <span class="nl">— ¿dónde está? · hay un sofá · está en…</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Beleefd om iets vragen (<b>poder</b>)</span> <span class="nl">— ¿puedo…? · ¿puedes…? · sí, puedes…</span></span></li>
    </ul>
  </div>
  <div class="guide"><span class="ic">🎒</span><div><span class="hand">¡Seguimos la ruta! Parada 6.</span><div class="g">In deze «survival»-les leer je een huis beschrijven. In de video is Julio zenuwachtig omdat María's spullen overal in zijn huis liggen — encima, debajo, dentro… — perfecte input voor de plaats-woorden.</div></div></div>

  <div class="se" style="margin-top:6mm">La gente de la ruta · je reisgenoten</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Je reist mee met vier jongeren uit de Spaanstalige wereld. In de scène ben je bij Julio thuis, samen met zijn vriend Fernando.</p>
  <div class="cast2">
    <div class="m"><div class="fl">🇪🇸</div><div class="nm">Lucía</div><div class="ro">Sevilla · familie</div></div>
    <div class="m"><div class="fl">🇲🇽</div><div class="nm">Diego</div><div class="ro">CDMX · eten & markt</div></div>
    <div class="m"><div class="fl">🇨🇴</div><div class="nm">Valen</div><div class="ro">Cartagena · wonen</div></div>
    <div class="m"><div class="fl">🇵🇪</div><div class="nm">Nina</div><div class="ro">Cusco · reizen</div></div>
    <div class="m"><div class="fl">🎒</div><div class="nm">Tú</div><div class="ro">jij, de reiziger</div></div>
  </div>

  <div class="truc" style="margin-top:5mm"><b>¿Qué reconoces ya?</b> Deze woon-woorden lijken op het Nederlands of Engels (<i>palabras transparentes</i>) — durf te gissen:
    <div class="cogn"><span>el apartamento</span><span>el balcón</span><span>la terraza</span><span>el garaje</span><span>el sofá</span><span>la lámpara</span><span>el jardín</span><span>la villa</span><span>el hotel</span><span>moderno</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Tip: veel woon-woorden herken je meteen — <b>apartamento</b>, <b>balcón</b>, <b>garaje</b>…</span>
  </div>
</div>
"""

ESCUCHA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§1 · ¡Escucha!</div><h2>Bekijk de scène en lees mee</h2>
  <div class="audiorow">
    <div class="call"><span class="ic">🎬</span><div><b>Sitcom · Episodio 6 · La casa.</b> Scan de code en bekijk de aflevering op de digitale pagina. Julio is nerveus: María's spullen liggen <b>encima</b>, <b>debajo</b> en <b>dentro</b> van alles in zijn huis. Luister eerst zónder te lezen; daarna lees je mee. De <b>vetgedrukte</b> woorden zijn chunks om mee te nemen.</div></div>
    <div class="qr"><div class="lab">Vídeo online</div>{qr(HUB_URL+"#escucha")}<div class="meta">hub · Escucha</div></div>
  </div>
  <div class="truc"><b>Antes de escuchar · vóór je luistert.</b> Welke <b>kamers</b> en <b>plaats-woorden</b> ga je horen, denk je? <span style="font-size:8.8pt;color:var(--mut)">(gis gerust)</span>
    <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.2">Una habitación: {wl('sm')} &nbsp;&nbsp; Un mueble: {wl('sm')} &nbsp;&nbsp; Una preposición (waar?): {wl('sm')}</div>
  </div>
  <div class="twocol">{scenehtml(*SCENES[0])}{scenehtml(*SCENES[1])}</div>
  <div class="ojo"><b>¡Ojo!</b> «Hay cosas <b>encima de</b> las sillas» = er liggen dingen <i>op</i> de stoelen. En <b>de + el = del</b>: dentro <b>del</b> frigorífico (niet «de el»).</div>

  <div class="se" style="margin-top:5mm">Después de escuchar · ¿Verdadero o falso?</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Kruis aan. Verbeter de <b>falsas</b> op de lijn.</p>
  <table class="vf">
    <tr><td>1. María deja su crema en el cuarto de baño.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>2. Dentro del frigorífico hay tres botellas de leche.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>3. Julio puede fumar dentro de casa.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>4. Paul es un empresario inglés.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
  </table>
</div>
"""

KIT=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Suena bien · pronunciación</div><h2>La b = la v (betacismo) &amp; llana/aguda</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 1mm">In het Spaans klinken <b>b</b> en <b>v</b> <b>net hetzelfde</b>: «bien» en «vino» beginnen met dezelfde klank. Oefen online (QR §1).</p>
  <div class="cogn"><span>bien</span><span>vino</span><span>bueno</span><span>vivir</span><span>beber</span><span>ventana</span></div>
  <div class="ojo"><b>¡Ojo!</b> Je hóórt geen verschil tussen b en v, dus let op de <b>schrijfwijze</b>: <b>b</b>aca (imperiaal) klinkt als <b>v</b>aca (koe)!</div>
  <div class="klemline"><b>La fuerza · llana (meeste woorden, voorlaatste) vs. aguda (laatste):</b> ca·<span class="t">SA</span> · co·<span class="t">CI</span>·na (llana) &nbsp;↔&nbsp; sa·<span class="t">LÓN</span> · so·<span class="t">FÁ</span> (aguda)</div>

  <div class="se" style="margin-top:3mm">§2 · Kit de supervivencia</div><h2>De taal die je écht nodig hebt</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 2mm">Vink ☐ af telkens je een uitdrukking vlot kunt <b>naspreken</b>. Oefen ze online met audio.</p>
  <div class="kitwrap">{"".join(kittable(n,it) for n,it in CLUSTERS)}</div>
</div>
"""

GRAM=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§4 · Gramática en la práctica</div><h2>Kort en functioneel</h2>
  <div class="modelo"><b>🔎 Fíjate · kijk terug naar de scène.</b> Je hoorde het al: «Hay cosas <b>encima de</b> las sillas, <b>debajo de</b> la cama. <b>Dentro del</b> frigorífico…» · «¿<b>Puedo</b> fumar? — Aquí no, pero <b>puedes</b> ir fuera». Ontdek zelf het patroon — <i>eerst betekenis, dan de regel.</i></div>
  <div class="regla"><span class="tag">las preposiciones de lugar · waar is het? (plaats = turquoise)</span>
    <div class="prep2"><div><b>encima de</b><i>op/boven</i></div><div><b>debajo de</b><i>onder</i></div><div><b>dentro de</b><i>in/binnen</i></div><div><b>al lado de</b><i>naast</i></div>
    <div><b>delante de</b><i>voor</i></div><div><b>detrás de</b><i>achter</i></div><div><b>entre</b><i>tussen</i></div><div><b>en</b><i>in/op</i></div></div>
    <p style="font-size:9pt;margin:1mm 0 0">⚠️ <b>de + el = del</b>: encima <b>del</b> sofá · al lado <b>del</b> armario (niet «de el»).</p>
  </div>
  <div class="regla"><span class="tag">hay vs. está · er is / het staat</span>
    <table class="gt2"><tr><td class="v">hay</td><td>er is / er zijn (iets nieuw)</td><td class="ex">En el salón <b>hay</b> un sofá.</td></tr>
    <tr><td class="v">¿Dónde está…?</td><td>waar is…? (iets bekend)</td><td class="ex">¿Dónde <b>está</b> el bolso?</td></tr>
    <tr><td class="v">está / están</td><td>het staat / ze staan</td><td class="ex"><b>Está</b> encima de la mesa.</td></tr></table>
    <p style="font-size:9pt;margin:1mm 0 0">💡 <b>hay</b> = er bestaat iets (onbekend) · <b>está</b> = waar dat bekende ding zich bevindt.</p>
  </div>
  <div class="regla"><span class="tag">poder · ¿puedo…? / ¿puedes…? — permiso</span>
    <div class="mv2"><div class="m">🙋 vragen: ¿<b>Puedo</b> fumar? (ik) · ¿<b>Puedes</b> venir? (jij)</div><div class="f">✅ antwoorden: Sí, <b>puedes</b>… · Aquí no, pero <b>puedes</b> ir fuera.</div></div>
    <p style="font-size:9pt;margin:1mm 0 0"><b>puedo</b> (ik) · <b>puedes</b> (jij) · <b>puede</b> (hij/zij) — altijd + een werkwoord in de hele vorm.</p>
  </div>
  <div class="truc"><b>Mini-oefening 1 · preposiciones.</b> Vul een plaats-woord in (kijk naar de tekening in je hoofd):
    <div style="margin-top:2mm;font-size:9.6pt;line-height:2.4">1. El gato está {wl('sm')} la cama (onder). &nbsp; 2. La lámpara está {wl('sm')} la mesa (op). &nbsp; 3. El armario está {wl('sm')} la ventana (naast).</div>
  </div>
  <div class="truc"><b>Mini-oefening 2 · hay of está?</b> a) En la cocina {wl('sm')} un frigorífico. &nbsp; b) El bolso {wl('sm')} encima del sofá. &nbsp; c) ¿Qué {wl('sm')} en tu dormitorio?</div>
  <div class="truc"><b>Mini-oefening 3 · ¿puedo of puedes?</b> Vul aan: 1. ¿{wl('sm')} abrir la ventana? (ik vraag) &nbsp; 2. Sí, {wl('sm')} abrirla (jij mag). &nbsp; 3. ¿{wl('sm')} ir al baño? (ik)</div>
</div>
"""

def act(n,title,badges,body):
    bh="".join(f'<span class="badge {c}">{t}</span>' for t,c in badges)
    return (f'<div class="act"><div class="acthead"><div class="anum">{n}</div><div><div class="h">{title}</div>'
            f'<div class="badges">{bh}</div></div></div>{body}</div>')

PRAC=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§3 · Práctica</div><h2>Oefen op papier — online verbeter je alles</h2>

  {act(1,"Clasifica: habitación, mueble o posición",[("receptief","skill"),("5 min","")],
    '<p style="margin-left:12.5mm">Schrijf elk woord in de juiste kolom. Voeg onderaan één eigen woord toe.<br><span class="gloss">la cocina · la cama · encima de · el salón · el armario · debajo de · el dormitorio · al lado de</span></p>'
    +'<div class="wcols" style="margin-left:12.5mm"><div class="wcol"><h4>Habitación 🏠</h4><div class="fill"></div></div><div class="wcol"><h4>Mueble 🛋️</h4><div class="fill"></div></div><div class="wcol"><h4>Posición 📍</h4><div class="fill"></div></div><div class="wcol"><h4>Tu palabra</h4><div class="fill"></div></div></div>')}

  {act(2,"Relaciona · ¿qué hacemos ahí?",[("gestuurd","skill"),("★☆☆","")],
    '<p style="margin-left:12.5mm">Trek een lijn tussen de kamer en wat je er doet.</p>'
    +'<table class="mtab" style="margin-left:12.5mm"><tr><td class="a">1. la cocina</td><td><span class="ln"></span></td><td class="b">a. dormir</td></tr>'
    +'<tr><td class="a">2. el dormitorio</td><td><span class="ln"></span></td><td class="b">b. ducharse</td></tr>'
    +'<tr><td class="a">3. el cuarto de baño</td><td><span class="ln"></span></td><td class="b">c. cocinar y comer</td></tr>'
    +'<tr><td class="a">4. el salón</td><td><span class="ln"></span></td><td class="b">d. entrar en casa</td></tr>'
    +'<tr><td class="a">5. la entrada</td><td><span class="ln"></span></td><td class="b">e. ver la tele</td></tr></table>')}

  {act(3,"Completa el diálogo",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Vul aan (está · debajo · puedes).</p>'
    +f'<div style="margin-left:12.5mm;font-size:10pt;line-height:2.5">'
    +f'— ¿Dónde {wl("sm")} mi bolso?<br>— {wl("sm")} encima del sofá.<br>— ¿Y las llaves?<br>— Están {wl("sm")} de la mesa <span style="color:var(--mut);font-size:8.6pt">(onder)</span>.<br>— ¿Puedo mirar en la cocina?<br>— Sí, {wl("sm")}.</div>')}

  {act(4,"Ordena la conversación",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Nummer de zinnen in de juiste volgorde (1–5).</p>'
    +'<div class="scramble" style="margin-left:12.5mm"><span>___ No, debajo de la mesa.</span><span>___ ¿Dónde está mi bolso?</span><span>___ ¡Ah, gracias!</span><span>___ Está en el salón.</span><span>___ ¿Encima del sofá?</span></div>')}

  {act(5,"¿hay o está?",[("gestuurd","skill"),("★☆☆","")],
    f'<p style="margin-left:12.5mm">Vul hay of está in (hay = er is iets nieuw · está = waar het bekende ding staat).</p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. En el salón {wl("sm")} un sofá. &nbsp; 2. El libro {wl("sm")} debajo de la cama. &nbsp; 3. ¿{wl("sm")} un frigorífico? &nbsp; 4. El bolso {wl("sm")} encima de la mesa.</div>')}

  {act(6,"Sitúa las cosas de tu cuarto",[("productie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Teken 4 dingen in je kamer en schrijf waar ze staan met een plaats-woord.</p>'
    +f'<div style="margin-left:12.5mm;font-size:9.8pt;line-height:2.3">🛏️ La cama está {wl("lg")}<br>💻 El ordenador está {wl("lg")}<br>🪟 La ventana está {wl("lg")}<br>🎒 La mochila está {wl("lg")}</div>')}

  {act(7,"Describe una habitación",[("productie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Schrijf 2 zinnen over één kamer: wat er is (hay) en waar het staat (está + preposición).</p>'
    +'<div class="wbox" style="margin-left:12.5mm"></div>')}

  {act(8,"Entrevista · ¿cómo es tu casa?",[("interactie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Vraag je buur naar zijn/haar huis en noteer. Wissel van rol. Vraag ook «¿Puedo…?».</p>'
    +f'<table class="wtab" style="margin-left:12.5mm;margin-top:2mm"><thead><tr><th style="width:48mm">Pregunta</th><th>Respuesta</th></tr></thead>'
    +'<tr><td style="height:12mm">¿Cuántas habitaciones hay?</td><td></td></tr>'
    +'<tr><td style="height:12mm">¿Dónde está tu dormitorio?</td><td></td></tr>'
    +'<tr><td style="height:12mm">¿Puedo ver una foto?</td><td></td></tr></table>')}
</div>
"""

TAREA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§5 · Tarea final</div><h2>Plano de mi casa</h2>
  <div class="esen" style="margin-top:2mm"><b class="tt">Jouw opdracht.</b> Teken de <b>plattegrond</b> van je huis met <b>4 kamers</b> (echt of droomhuis). Benoem elke kamer, en zeg per kamer <b>wat er is</b> (hay) en <b>waar</b> het staat (met een plaats-woord). Presenteer je plattegrond aan de klas. <span class="gloss">Sin leer del papel — zonder van het blad af te lezen.</span></div>
  <div class="regla" style="margin-top:4mm"><span class="tag">Prepárate · vul eerst de frames in</span>
    <div style="margin-top:2mm;font-size:9.7pt;line-height:2.4">1. Aquí está {wl('sm')} (la cocina…). En {wl('sm')} hay {wl('sm')} .<br>2. El/la {wl('sm')} está {wl('sm')} (encima de · al lado de…) {wl('sm')} .<br>3. En mi casa también hay {wl('sm')} . ¿Puedo enseñártela? Sí, {wl('sm')} .</div>
  </div>
  <div class="modelo" style="margin-top:4mm"><b>Modelo · zo klinkt het:</b><br>
    — Aquí está el salón. En el salón hay un sofá y una tele. La tele está encima de una mesa.<br>
    — Y aquí está la cocina. Al lado de la cocina está el cuarto de baño.</div>
  <div style="margin-top:4mm"><div class="se">Mi plano · teken hier je plattegrond + benoem de kamers</div>
    <div class="plano" style="margin-top:2mm"><div>1 · La habitación:</div><div>2 · La habitación:</div><div>3 · La habitación:</div><div>4 · La habitación:</div></div>
  </div>
  <div class="regla" style="margin-top:3mm"><span class="tag">Palabras y frases útiles</span>
    <p style="margin:1mm 0 0;font-size:9.6pt">la cocina · el salón · el dormitorio · el cuarto de baño · la cama · el sofá · el armario · hay… · está… · encima de · debajo de · al lado de · dentro de · delante de · detrás de · ¿puedo…? · sí, puedes…</p>
  </div>
  <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div class="truc" style="margin:0"><b>🏁 Klaar als…</b> je 4 kamers benoemt en per kamer zegt wat er is (hay) én waar het staat (met een plaats-woord) — zónder af te lezen.</div>
    <table class="rubric"><thead><tr><th>Evaluatie</th><th style="text-align:center">🟢🟡🔴</th></tr></thead>
      <tr><td>habitaciones benoemen correct</td><td></td></tr>
      <tr><td>hay/está + preposición correct</td><td></td></tr>
      <tr><td>uitspraak &amp; durf</td><td></td></tr></table>
  </div>
</div>
"""

BANDAS=[("Manu Chao","Me Gustas Tú","🇪🇸/🇫🇷"),("Álvaro Soler","Sofía","🇪🇸 España"),("Camilo","Vida de Rico","🇨🇴 Colombia"),
 ("Marc Anthony","Vivir Mi Vida","🇵🇷 Puerto Rico"),("Juanes","La Camisa Negra","🇨🇴 Colombia"),("Rosalía","Despechá","🇪🇸 España")]
def banda(a,s,g): return f'<div class="banda"><div class="ar">{a}</div><div class="sg">🎵 {s}</div><div class="ge">{g}</div></div>'
MUSICA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Cultura · Banda sonora</div><h2>La casa en el mundo hispano</h2>
  <p style="font-size:9.6pt">Een huis vertelt veel over een cultuur. In veel Spaanse en Latijns-Amerikaanse huizen is er een <b>patio</b> (binnenkoer vol planten), het hart van het huis. In steden als <b>Guanajuato</b> (🇲🇽), <b>Cartagena</b> (🇨🇴) en <b>Guatapé</b> schilderen mensen hun huizen in <b>felle kleuren</b>. En midden op de dag rust men soms even: <b>la siesta</b>. Elke unit heeft ook een <b>banda sonora</b>.</p>
  <div class="bandas">{"".join(banda(*b) for b in BANDAS)}</div>
  <div class="musrow">
    <div class="call"><span class="ic">🎧</span><div><b>Spotify · la playlist de la clase.</b> Scan en luister. Op de digitale pagina vind je ook <b>LyricsTraining</b> en de <b>wereldkaart</b>.</div></div>
    <div class="qr"><div class="lab">Playlist</div>{qr(SPOTIFY)}<div class="meta">Spotify</div></div>
  </div>
  <div class="truc" style="margin-top:5mm"><b>La casa hispana · ¿sabías que…?</b> Verbind (gis gerust):
    <table class="mtab" style="margin-top:1mm"><tr><td class="a">El patio es…</td><td>{wl('sm')}</td><td class="b">a. casas pintadas de mil colores</td></tr>
    <tr><td class="a">Guanajuato y Cartagena tienen…</td><td>{wl('sm')}</td><td class="b">b. het hart van veel huizen (planten)</td></tr>
    <tr><td class="a">La siesta es…</td><td>{wl('sm')}</td><td class="b">c. een korte rust midden op de dag</td></tr></table>
    <p style="font-size:8.6pt;color:var(--mut);margin-top:1mm">💡 «estar en casa» (thuis zijn) en «ir a casa» (naar huis) gebruik je zónder lidwoord — net als in het Nederlands.</p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:3mm;align-items:start">
    <div class="truc" style="margin:0"><b>Escucha y responde.</b> Kies één nummer van de playlist.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.3">Mi canción: {wl('lg')}<br>El/la artista es de: {wl('lg')}</div>
    </div>
    <div class="truc" style="margin:0"><b>¿Y tu casa?</b> Schrijf één zin over een kamer + waar iets staat.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.4">{wl('full')}<br>{wl('full')}</div>
    </div>
  </div>
</div>
"""

REPASO=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Repaso · Lo esencial de un vistazo</div><h2>Wat je nu kunt</h2>
  <div class="fams">
    <div class="pcard"><div class="t">Zo zeg je waar iets is</div><div class="ej"><b>¿Dónde está</b> ____? — <b>Está</b> ____ (encima de · debajo de · al lado de) ____.</div><div class="t2">de+el = <b>del</b> · a+el = <b>al</b></div></div>
    <div class="pcard"><div class="t">Zo zeg je wat er is / vraag je iets</div><div class="ej"><b>Hay</b> ____ en ____. · ¿<b>Puedo</b> ____? — Sí, <b>puedes</b> ____.</div><div class="anchor"><b>hay</b> = nieuw ding · <b>está</b> = waar het staat &nbsp;|&nbsp; poder + hele werkwoord</div></div>
  </div>
  <div class="regla" style="margin:4mm 0"><span class="tag">Frases para la clase</span>
    <div class="cogn" style="margin-top:1mm"><span>¿Cómo se dice… ?</span><span>¿Qué significa… ?</span><span>Otra vez, por favor</span><span>No entiendo</span><span>¿Puedes repetir?</span><span>¿Puedo ir al baño?</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Handige klaszinnen — gebruik ze in het Spaans i.p.v. Nederlands.</span>
  </div>
  <table class="sem"><thead><tr><th style="text-align:left">Puedo… · Ik kan…</th><th>🟢</th><th>🟡</th><th>🔴</th></tr></thead>
    <tr><td>de kamers &amp; meubels benoemen</td><td></td><td></td><td></td></tr>
    <tr><td>zeggen waar iets is (preposiciones de lugar)</td><td></td><td></td><td></td></tr>
    <tr><td>hay en está juist gebruiken</td><td></td><td></td><td></td></tr>
    <tr><td>beleefd om iets vragen (¿puedo…? · puedes…)</td><td></td><td></td><td></td></tr></table>
  <div class="regla" style="margin-top:5mm"><span class="tag">Mini-test · recuerda sin mirar</span>
    <p style="margin:1mm 0 0;font-size:9.4pt">Sluit de cursus en vertaal uit het hoofd (ophalen = het beste leren).</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3mm 8mm;margin-top:2mm;font-size:9.8pt;line-height:2.2">
      <div>1. de keuken → {wl('')}</div><div>2. waar is de tas? → {wl('')}</div>
      <div>3. op de tafel → {wl('')}</div><div>4. onder het bed → {wl('')}</div>
      <div>5. er is een bank → {wl('')}</div><div>6. mag ik roken? → {wl('')}</div>
    </div>
  </div>
  <div class="guide"><span class="ic">🎮</span><div><span class="hand">Repasa jugando</span><div class="g">Oefen alles online met spelletjes, flashcards en audio op de digitale hub (scan de QR bij §1).</div></div></div>
  <div class="bridge"><b>Próxima parada →</b> In de volgende unit: <i>las profesiones</i> (¿a qué te dedicas?). ¡Hasta pronto!</div>
</div>
"""

EDITBAR="""
<div class="editbar" id="eb">
  <b>✏️ C4 · U6</b>
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
document.getElementById('btnsave').onclick=function(){var html='<!doctype html>'+document.documentElement.outerHTML;var b=new Blob([html],{type:'text/html'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='C4_U6_Casa_bewerkt.html';a.click();};
</script>
"""

HTML=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 6 · La casa y los lugares</title><style>{CSS}</style></head><body>
{EDITBAR}
{HERO}{ESCUCHA}{COMPR_SEC}{KIT}{GRAM}{PRAC}{TAREA}{MUSICA}{FUNCIONES_SEC}{REPASO}
{SCRIPT}
</body></html>"""
os.makedirs(f"{ROOT}/03-build/web/print",exist_ok=True)
open(f"{ROOT}/03-build/web/print/C4_U6.html","w",encoding="utf-8").write(HTML)
print("C4_U6.html (print+editable) geschreven:",len(HTML),"bytes")
