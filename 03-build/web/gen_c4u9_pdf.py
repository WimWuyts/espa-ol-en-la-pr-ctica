#!/usr/bin/env python3
# C4 · Unidad 9 — PRINT (HTML=bron → PDF via Chromium). Golden-sample print-kit, C4-rood.
# Thema: Planes y obligaciones · ir a + infinitivo · tener que + infinitivo · tener + naamwoord · rechazar.
# NB: de video komt (zoals U8) uit Google Drive → de QR verwijst naar de HTML-hub, niet naar Drive.
import base64, os, re, io, sys
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
from funciones_print import print_section
FUNCIONES_SEC=print_section(9)
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
HUB_URL=EN.url("C4", 9)
import comprension_print
COMPR_SEC=comprension_print.print_section(9, HUB_URL)
SPOTIFY="https://open.spotify.com/playlist/37i9dQZF1DXaxEKcoCdWHD"

SCENES=[
 ("Escena 1 · Un sábado por la mañana",[
  ("María","Buenos días."),
  ("Julio","Buenos días. Voy a preparar café. ¿Quieres desayunar?"),
  ("María","Ah… no tengo mucha hambre."),
  ("Julio","Pero es sábado. Tengo sueño. ¿No tienes sueño? Vamos a dormir un poquito más."),
  ("María","Tengo cosas que hacer."),
 ]),
 ("Escena 2 · «Tengo que…»",[
  ("Julio","Y esta noche, ¿quedamos para ir al cine?"),
  ("María","Eh… no puedo. Tengo que pasear al perro de mi madre."),
  ("Julio","¿Y esta tarde? ¿Vamos a pasear, a comprar cosas?"),
  ("María","Mmm…, tengo que lavarme el pelo."),
  ("Julio","¿Y mañana? ¿Tienes que hacer algo?"),
  ("María","El domingo voy a quedar con unas amigas."),
 ]),
 ("Escena 3 · ¿Y el próximo finde?",[
  ("Julio","¿El lunes, el martes, el miércoles?"),
  ("María","Tengo que trabajar."),
  ("Julio","¿Por las noches?"),
  ("María","Por las noches tengo que dormir."),
  ("Julio","El jueves voy a dar unas clases de baile flamenco."),
  ("Julio","El próximo fin de semana. ¿Tienes que ir a la India en globo?"),
  ("María","No, estoy aquí, pero tengo cosas que hacer. Cosas. Adiós."),
 ]),
]
CH=["Voy a preparar café","¿Quieres desayunar?","no tengo mucha hambre","Tengo sueño","¿No tienes sueño?","Vamos a dormir","Tengo cosas que hacer","¿quedamos para ir al cine?","no puedo","Tengo que pasear al perro","¿Vamos a pasear","tengo que lavarme el pelo","¿Tienes que hacer algo?","voy a quedar con unas amigas","Tengo que trabajar","tengo que dormir","voy a dar unas clases","el próximo fin de semana","esta noche","esta tarde"]
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
 ("Los planes · voy a…",[("Voy a + infinitivo","Ik ga + werkwoord"),("Voy a preparar café","Ik ga koffie zetten"),
   ("Vamos a dormir","We gaan / laten we slapen"),("¿Vamos a pasear?","Gaan we wandelen?"),("¿Qué vas a hacer?","Wat ga je doen?")]),
 ("Las obligaciones · tengo que…",[("Tengo que + infinitivo","Ik moet + werkwoord"),("Tengo que trabajar","Ik moet werken"),
   ("Tengo que estudiar","Ik moet studeren"),("¿Tienes que hacer algo?","Moet je iets doen?"),("Tengo cosas que hacer","Ik heb dingen te doen")]),
 ("Actividades del finde",[("ir al cine","naar de cinema gaan"),("pasear al perro","de hond uitlaten"),
   ("quedar con amigos/as","afspreken met vrienden"),("ver una película","een film kijken"),("tomar algo","iets gaan drinken")]),
 ("Con tener · geen «ser»!",[("Tengo hambre","Ik heb honger"),("Tengo sueño","Ik ben slaperig"),
   ("Tengo sed","Ik heb dorst"),("Tengo prisa","Ik heb haast")]),
 ("Aceptar o rechazar",[("¡Vale! · ¡Perfecto!","Oké! · Perfect!"),("No puedo","Ik kan niet"),
   ("¡Qué pena!","Wat jammer!"),("Estoy libre","Ik ben vrij"),("Otro día, ¿vale?","Een andere dag, oké?")]),
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
.agenda{width:100%;font-size:9pt;margin-top:2mm}
.agenda th{background:var(--g);color:#fff;font-size:7.6pt;text-transform:uppercase;padding:1.4mm}
.agenda td{border:1px solid var(--line);height:12mm;padding:1mm 2mm}
.agenda td.h{background:var(--gt);color:var(--gd);font-family:var(--disp);font-weight:700;width:26mm;font-size:8.4pt}
.editbar{position:fixed;top:0;left:0;right:0;background:var(--gd);color:#fff;display:flex;gap:8px;align-items:center;padding:7px 12px;z-index:999;font-family:var(--body);font-size:13px;box-shadow:0 2px 10px #0003}
.editbar b{font-family:var(--disp)}.editbar button{border:0;background:#fff;color:var(--gd);font-weight:700;border-radius:8px;padding:6px 11px;cursor:pointer;font-size:12.5px}
.editbar button.on{background:#111;color:#fff}.editbar .sp{flex:1}.scr-spacer{height:44px}
body.editing .page{outline:1.5px dashed var(--g);outline-offset:-6px}
@media print{ .editbar,.scr-spacer{display:none!important} }
"""

HERO=f"""
<section class="hero">
  <div class="tab">C4 · LA RUTA</div>
  <div class="eyebrow">EL DESPEGUE · PARADA 9 · SURVIVAL IN SPANISH</div>
  <h1>Planes y obligaciones</h1>
  <div class="sub">Zeggen wat je <b>gaat doen</b> en wat je <b>moet</b> doen — en beleefd «nee» zeggen. <span class="gloss">Planes y obligaciones — voy a + infinitivo · tengo que + infinitivo · no puedo, tengo que…</span></div>
  <div class="q">Voy a preparar café. — Eh… tengo cosas que hacer.</div>
</section>
<div class="page">
  <div class="obj"><div class="se">Al final de esta unidad · Op het einde van deze les</div>
    <ul>
      <li><span class="ck">✓</span> <span><span class="es">Hablar de planes con <b>ir a</b> + infinitivo</span> <span class="nl">— voy a estudiar · vamos a dormir · ¿qué vas a hacer?</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Expresar obligación con <b>tener que</b> + infinitivo</span> <span class="nl">— tengo que trabajar · ¿tienes que hacer algo?</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Usar <b>tener</b> + sustantivo</span> <span class="nl">— tengo hambre · tengo sueño (niet «ik ben»!)</span></span></li>
      <li><span class="ck">✓</span> <span><span class="es">Aceptar y <b>rechazar</b> una invitación</span> <span class="nl">— ¡vale! · no puedo, tengo que… · ¡qué pena!</span></span></li>
    </ul>
  </div>
  <div class="guide"><span class="ic">🎒</span><div><span class="hand">¡Seguimos la ruta! Parada 9.</span><div class="g">In deze «survival»-les leer je plannen maken. In de video probeert Julio de hele week een afspraak te maken — en María heeft élke keer iets anders te doen («tengo que pasear al perro», «tengo que lavarme el pelo»). Perfecte input voor plannen én excuses.</div></div></div>

  <div class="se" style="margin-top:5mm">La máquina de frases · zo bouw je een plan of een verplichting</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Twee bouwstenen, altijd in dezelfde volgorde. Ná <b>voy a</b> of <b>tengo que</b> komt <b>áltijd</b> het hele werkwoord:</p>
  <div class="maq">
    <div class="m1">Voy a<small>plan · ik ga</small></div><div class="m2">+ infinitivo<small>het hele werkwoord</small></div><div class="m3">estudiar · ir al cine<small>→ Voy a estudiar.</small></div>
  </div>
  <div class="maq">
    <div class="m1">Tengo que<small>moeten · ik moet</small></div><div class="m2">+ infinitivo<small>het hele werkwoord</small></div><div class="m3">trabajar · dormir<small>→ Tengo que trabajar.</small></div>
  </div>

  <div class="truc" style="margin-top:4mm"><b>¿Qué reconoces ya?</b> Deze plan-woorden lijken op het Nederlands/Engels of ken je al (<i>palabras transparentes</i>):
    <div class="cogn"><span>el plan</span><span>el cine</span><span>la película</span><span>el concierto</span><span>el fútbol</span><span>la clase</span><span>el flamenco</span><span>el finde</span><span>la India</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Tip: <b>el plan</b>, <b>el cine</b>, <b>el concierto</b> herken je meteen.</span>
  </div>
</div>
"""

ESCUCHA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§1 · ¡Escucha!</div><h2>Bekijk de scène en lees mee</h2>
  <div class="audiorow">
    <div class="call"><span class="ic">🎬</span><div><b>Sitcom · Episodio 9 · Planes y obligaciones.</b> Scan de code en bekijk de aflevering op de digitale pagina. Julio stelt de hele week plannen voor; María heeft élke keer iets te doen. Luister eerst zónder te lezen; daarna lees je mee. Let op elk <b>voy a…</b> (plan) en elk <b>tengo que…</b> (moeten) — de <b>vetgedrukte</b> woorden zijn chunks om mee te nemen.</div></div>
    <div class="qr" data-url="{EN.url('C4', 9, EN.ancla_c4('escucha'))}"><div class="lab">Vídeo online</div>{qr(EN.url("C4", 9, EN.ancla_c4("escucha")))}<div class="meta">hub · Escucha</div></div>
  </div>
  <div class="truc"><b>Antes de escuchar · vóór je luistert.</b> Welke <b>excuses</b> zou jij verzinnen om niet af te spreken? <span style="font-size:8.8pt;color:var(--mut)">(gis gerust, in het Spaans of het Nederlands)</span>
    <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.2">Excusa 1: {wl('lg')} &nbsp;&nbsp; Excusa 2: {wl('lg')}</div>
  </div>
  <div class="twocol">{scenehtml(*SCENES[0])}{scenehtml(*SCENES[1])}{scenehtml(*SCENES[2])}</div>
  <div class="ojo"><b>¡Ojo!</b> «<b>Tengo sueño</b>» = ik ben slaperig (letterlijk: ik <i>heb</i> slaap) — niet <s>estoy sueño</s>. En «<b>tengo que</b> trabajar»: de <b>que</b> mag nooit weg.</div>

  <div class="se" style="margin-top:5mm">Después de escuchar · ¿Verdadero o falso?</div>
  <p style="font-size:9.4pt;margin:0 0 1mm">Kruis aan. Verbeter de <b>falsas</b> op de lijn.</p>
  <table class="vf">
    <tr><td>1. Julio va a preparar café.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>2. María tiene que pasear al perro de su madre.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>3. El domingo María va a quedar con unas amigas.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
    <tr><td>4. El próximo fin de semana María va a la India en globo.</td><td class="b">☐ V ☐ F</td><td>{wl('')}</td></tr>
  </table>
</div>
"""

KIT=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Suena bien · pronunciación</div><h2>Los diptongos <i>ie</i> &amp; <i>ue</i></h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 1mm">Twee klinkers samen vormen <b>één</b> lettergreep (een <i>diptongo</i>): «qu<b>ie</b>-ro» = 2 stukken, niet 3. Oefen online (QR §1).</p>
  <div class="cogn"><span>quiero</span><span>tienes</span><span>bien</span><span>siete</span><span>fiesta</span><span>viernes</span></div>
  <div class="ojo"><b>¡Ojo!</b> Splits ze niet: «pu-e-do» klinkt fout — zeg «pue-do» in één beweging. En in <b>que/qui</b> is de u <b>stil</b> (U7): daar is het géén diptongo.</div>
  <div class="cogn"><span>puedo</span><span>bueno</span><span>luego</span><span>fuera</span><span>juego</span><span>cuenta</span></div>
  <div class="klemline"><b>La tilde en el diptongo · het accent komt op de tweede klinker:</b> a·di<span class="t">ÓS</span> · des·p<span class="t">UÉS</span> · tam·b<span class="t">IÉN</span> · can·c<span class="t">IÓN</span></div>

  <div class="se" style="margin-top:3mm">§2 · Kit de supervivencia</div><h2>De taal die je écht nodig hebt</h2>
  <p style="font-size:9.4pt;color:var(--mut);margin:0 0 2mm">Vink ☐ af telkens je een uitdrukking vlot kunt <b>naspreken</b>. Oefen ze online met audio.</p>
  <div class="kitwrap">{"".join(kittable(n,it) for n,it in CLUSTERS)}</div>
</div>
"""

GRAM=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§4 · Gramática en la práctica</div><h2>Kort en functioneel</h2>
  <div class="modelo"><b>🔎 Fíjate · kijk terug naar de scène.</b> Je hoorde het al: «<b>Voy a</b> preparar café» · «<b>Vamos a</b> dormir un poquito más» · «<b>Tengo que</b> pasear al perro» · «<b>Tengo</b> sueño». Ontdek zelf het patroon — <i>eerst betekenis, dan de regel.</i></div>
  <div class="regla"><span class="tag">ir a + infinitivo · plannen («ik ga…»)</span>
    <table class="gt2"><tr><td class="v">voy a</td><td>ik ga</td><td class="ex"><b>Voy a</b> preparar café.</td></tr>
    <tr><td class="v">vas a</td><td>jij gaat</td><td class="ex">¿Qué <b>vas a</b> hacer?</td></tr>
    <tr><td class="v">vamos a</td><td>we gaan / laten we</td><td class="ex"><b>Vamos a</b> dormir un poquito más.</td></tr></table>
    <p style="font-size:9pt;margin:1mm 0 0">💡 Net als in het Nederlands («ik <b>ga</b> koffie zetten»). Vergeet de <b>a</b> niet: voy <b>a</b> estudiar.</p>
  </div>
  <div class="regla"><span class="tag">tener que + infinitivo (moeten) &nbsp;↔&nbsp; tener + sustantivo</span>
    <table class="gt2"><tr><td class="v">tengo que</td><td>ik moet</td><td class="ex"><b>Tengo que</b> trabajar.</td></tr>
    <tr><td class="v">tienes que</td><td>jij moet</td><td class="ex">¿<b>Tienes que</b> hacer algo?</td></tr></table>
    <div class="mv2" style="margin-top:1.5mm"><div class="m">✅ Spaans: <b>Tengo</b> hambre · <b>sueño</b> · <b>prisa</b> <i>(zonder «que»)</i></div><div class="f">🇳🇱 wij: ik <b>heb</b> honger · ik <b>ben</b> slaperig · ik <b>heb</b> haast</div></div>
    <p style="font-size:9pt;margin:1mm 0 0">⚠️ Vóór een <b>werkwoord</b> hoort er <b>que</b> bij (tengo <b>que</b> trabajar); vóór een <b>naamwoord</b> niet (tengo hambre). <b>Dé valstrik:</b> «ik ben slaperig» = <b>tengo sueño</b>, nooit <s>estoy sueño</s>.</p>
  </div>
  <div class="regla"><span class="tag">Rechazar con educación · zo zegt María «nee»</span>
    <div class="dial2"><div class="db">— ¿Quedamos para ir al cine?</div><div class="da">— <b>No puedo. Tengo que</b> pasear al perro. ¡Qué pena!</div></div>
    <p style="font-size:9pt;margin:1mm 0 0">💡 Twee stappen: <b>nee</b> + <b>reden</b>. Verzachters: <b>¡Qué pena!</b> · <b>Otro día, ¿vale?</b></p>
  </div>
  <div class="truc"><b>Mini-oefening · ir a &amp; tener que.</b> Vul aan (let op de <b>a</b> en de <b>que</b>):
    <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.3">1. Yo {wl('sm')} estudiar (plan). &nbsp; 2. ¿Qué {wl('sm')} hacer tú? &nbsp; 3. Nosotros {wl('sm')} dormir más.<br>4. Tengo {wl('sm')} trabajar. &nbsp; 5. Tengo {wl('sm')} (honger). &nbsp; 6. Tengo {wl('sm')} (slaap).</div>
    <div style="margin-top:1.5mm;font-size:9.6pt">✍️ Rechazar: «¿Vamos al cine el viernes?» → {wl('full')}</div></div>
</div>
"""

def act(n,title,badges,body):
    bh="".join(f'<span class="badge {c}">{t}</span>' for t,c in badges)
    return (f'<div class="act"><div class="acthead"><div class="anum">{n}</div><div><div class="h">{title}</div>'
            f'<div class="badges">{bh}</div></div></div>{body}</div>')

PRAC=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§3 · Práctica</div><h2>Oefen op papier — online verbeter je alles</h2>

  {act(1,"Clasifica: plan, obligación o tener + sustantivo",[("receptief","skill"),("5 min","")],
    '<p style="margin-left:12.5mm">Schrijf elke uitdrukking in de juiste kolom. Voeg onderaan één eigen voorbeeld toe.<br><span class="gloss">voy a estudiar · tengo que trabajar · tengo hambre · vamos a pasear · tengo sueño · tienes que dormir · tengo prisa · ¿qué vas a hacer?</span></p>'
    +'<div class="wcols" style="margin-left:12.5mm"><div class="wcol"><h4>Plan 🗓️</h4><div class="fill"></div></div><div class="wcol"><h4>Obligación ✅</h4><div class="fill"></div></div><div class="wcol"><h4>tener + nw. 🙋</h4><div class="fill"></div></div><div class="wcol"><h4>Tu ejemplo</h4><div class="fill"></div></div></div>')}

  {act(2,"¿voy a · vas a · vamos a?",[("gestuurd","skill"),("★☆☆","")],
    f'<p style="margin-left:12.5mm">Vul de juiste vorm van «ir a» in.</p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. Yo {wl("sm")} preparar café. &nbsp; 2. ¿Qué {wl("sm")} hacer tú? &nbsp; 3. Nosotros {wl("sm")} dormir más.<br>4. Yo {wl("sm")} quedar con amigas. &nbsp; 5. ¿{wl("sm")} pasear? (nosotros)</div>')}

  {act(3,"Con «que» o sin «que»?",[("gestuurd","skill"),("★★☆","")],
    f'<p style="margin-left:12.5mm">Vóór een <b>werkwoord</b> → tengo <b>que</b>… · vóór een <b>naamwoord</b> → tengo… Vul aan.</p><div style="margin-left:12.5mm;font-size:10pt;line-height:2.4">'
    +f'1. Tengo {wl("sm")} estudiar. &nbsp; 2. Tengo {wl("sm")} (honger). &nbsp; 3. Tengo {wl("sm")} trabajar.<br>4. Tengo {wl("sm")} (slaap). &nbsp; 5. ¿Tienes {wl("sm")} hacer algo?</div>')}

  {act(4,"Relaciona · invitación ↔ respuesta",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Une con una línea cada invitación con su respuesta. <span class="gloss">verbind de uitnodiging met het antwoord</span></p>'
    +'<table class="mtab" style="margin-left:12.5mm"><tr><td class="a">1. ¿Vamos al cine esta noche?</td><td><span class="ln"></span></td><td class="b">a. Vale, el domingo estoy libre.</td></tr>'
    +'<tr><td class="a">2. ¿Quedamos el sábado?</td><td><span class="ln"></span></td><td class="b">b. No tengo hambre, gracias.</td></tr>'
    +'<tr><td class="a">3. ¿Desayunamos juntos?</td><td><span class="ln"></span></td><td class="b">c. No puedo. Tengo que estudiar.</td></tr>'
    +'<tr><td class="a">4. ¿Tomamos algo el domingo?</td><td><span class="ln"></span></td><td class="b">d. El sábado tengo que trabajar.</td></tr></table>')}

  {act(5,"Ordena la conversación",[("gestuurd","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Numera las frases (1–5): invitación → excusa → nueva propuesta. <span class="gloss">nummer de zinnen in die volgorde</span></p>'
    +'<div class="scramble" style="margin-left:12.5mm"><span>___ ¿Y mañana?</span><span>___ ¿Quedamos para ir al cine esta noche?</span><span>___ ¡Qué pena! Otro día, ¿vale?</span><span>___ No puedo. Tengo que pasear al perro.</span><span>___ Mañana voy a quedar con unas amigas.</span></div>')}

  {act(6,"Mis planes de la semana",[("productie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Escribe por cada día un plan (voy a…) o una obligación (tengo que…). <span class="gloss">één plan of verplichting per dag</span></p>'
    +f'<div style="margin-left:12.5mm;font-size:9.8pt;line-height:2.3">📅 El lunes {wl("lg")}<br>📅 El miércoles {wl("lg")}<br>📅 El viernes {wl("lg")}<br>📅 El domingo {wl("lg")}</div>')}

  {act(7,"Invita y rechaza · en parejas",[("interactie","skill"),("★★☆","")],
    '<p style="margin-left:12.5mm">Invita a tu compañero/a tres veces: dos las rechaza con una excusa y una la acepta. Anótalo. <span class="gloss">nodig drie keer uit; twee keer een excuus, één keer ja</span></p>'
    +f'<table class="wtab" style="margin-left:12.5mm;margin-top:2mm"><thead><tr><th style="width:52mm">Mi invitación</th><th>Su respuesta</th></tr></thead>'
    +'<tr><td style="height:11mm">¿Vamos a…?</td><td></td></tr>'
    +'<tr><td style="height:11mm">¿Quedamos para…?</td><td></td></tr>'
    +'<tr><td style="height:11mm">¿Tomamos algo el…?</td><td></td></tr></table>')}

  {act(8,"Escribe un mensaje",[("productie","skill"),("★★★","")],
    '<p style="margin-left:12.5mm">Escribe un mensaje corto a un amigo o una amiga hispanohablante: dos planes, una obligación y una propuesta para quedar. <span class="gloss">kort bericht met plannen en een voorstel</span></p>'
    +'<div class="wbox" style="margin-left:12.5mm;min-height:46mm"></div>')}

</div>
"""

TAREA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">§5 · Tarea final</div><h2>Mi finde</h2>
  <div class="esen" style="margin-top:2mm"><b class="tt">Jouw opdracht.</b> Vul je <b>weekend-agenda</b> in met <b>3 planes</b> (voy a…) en <b>2 obligaciones</b> (tengo que…). <b>Nodig</b> dan een klasgenoot uit voor één van je plannen; hij/zij <b>wijst één keer beleefd af</b> met een echt excuus. Zoek samen tóch één moment dat past en <b>maak de afspraak</b> (dag + uur). <span class="gloss">Sin leer del papel — zonder van het blad af te lezen.</span></div>
  <div style="margin-top:4mm"><div class="se">Mi agenda del finde · vul in</div>
    <table class="agenda"><thead><tr><th>¿Cuándo?</th><th>Voy a… (plan)</th><th>Tengo que… (obligación)</th></tr></thead>
      <tr><td class="h">El sábado por la mañana</td><td></td><td></td></tr>
      <tr><td class="h">El sábado por la tarde</td><td></td><td></td></tr>
      <tr><td class="h">El sábado por la noche</td><td></td><td></td></tr>
      <tr><td class="h">El domingo</td><td></td><td></td></tr></table>
  </div>
  <div class="regla" style="margin-top:4mm"><span class="tag">Prepárate · vul eerst de frames in</span>
    <div style="margin-top:2mm;font-size:9.7pt;line-height:2.4">1. Mi invitación: ¿<b>Vamos a</b> {wl('sm')} el {wl('sm')} ?<br>2. Mi excusa: <b>No puedo. Tengo que</b> {wl('lg')} .<br>3. Nuestro plan final: Quedamos el {wl('sm')} <b>a las</b> {wl('sm')} en {wl('sm')} .</div>
  </div>
  <div class="modelo" style="margin-top:4mm"><b>Modelo · zo klinkt het:</b><br>
    — El sábado por la tarde voy a jugar al fútbol, pero el domingo tengo que estudiar.<br>
    — ¿Vamos al cine el sábado por la noche? — No puedo. Tengo que cuidar a mi hermano. ¡Qué pena!<br>
    — ¿Y el domingo por la tarde? — Vale, el domingo estoy libre. Quedamos a las cinco.</div>
  <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:6mm;margin-top:4mm;align-items:start">
    <div class="truc" style="margin:0"><b>🏁 Klaar als…</b> je 3 plannen zegt met «voy a + infinitivo», 2 verplichtingen met «tengo que + infinitivo», één uitnodiging beleefd afwijst («no puedo, tengo que…») en samen één afspraak vastlegt — zónder af te lezen.</div>
    <table class="rubric"><thead><tr><th>Evaluatie</th><th style="text-align:center">🟢🟡🔴</th></tr></thead>
      <tr><td>ir a + infinitivo correct (planes)</td><td></td></tr>
      <tr><td>tener que + infinitivo correct</td><td></td></tr>
      <tr><td>rechazar met excuus &amp; durf</td><td></td></tr></table>
  </div>
</div>
"""

BANDAS=[("Quevedo","Bzrp #52","🇪🇸 España"),("Karol G","Provenza","🇨🇴 Colombia"),("Aitana","Las Babys","🇪🇸 España"),
 ("Manu Chao","Me Gustas Tú","🇪🇸/🇫🇷"),("Álvaro Soler","El Mismo Sol","🇪🇸 España"),("Camilo","Vida de Rico","🇨🇴 Colombia")]
def banda(a,s,g): return f'<div class="banda"><div class="ar">{a}</div><div class="sg">🎵 {s}</div><div class="ge">{g}</div></div>'
MUSICA=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Cultura · Banda sonora</div><h2>El «finde» en el mundo hispano</h2>
  <p style="font-size:9.6pt">Plannen maken klinkt anders — en het weekend begint er later. In <b>Spanje</b> spreekt men vaak pas om <b>22–23 u</b> af om uit te gaan. Valt een feestdag op donderdag, dan «maakt men een brug» (<b>hacer puente</b>): ook de vrijdag vrij. Jongeren zeggen <b>el finde</b> (van <i>el fin de semana</i>), en de <b>zondag</b> is bij veel families de dag van de familiemaaltijd. Elke unit heeft ook een <b>banda sonora</b>.</p>
  <div class="bandas">{"".join(banda(*b) for b in BANDAS)}</div>
  <div class="musrow">
    <div class="call"><span class="ic">🎧</span><div><b>Spotify · la playlist de la clase.</b> Scan en luister. Op de digitale pagina vind je ook <b>LyricsTraining</b> en de <b>wereldkaart</b>.</div></div>
    <div class="qr" data-url="{SPOTIFY}"><div class="lab">Playlist</div>{qr(SPOTIFY)}<div class="meta">Spotify</div></div>
  </div>
  <div class="truc" style="margin-top:5mm"><b>El finde hispano · ¿sabías que…?</b> Verbind (gis gerust):
    <table class="mtab" style="margin-top:1mm"><tr><td class="a">«Hacer puente» is…</td><td>{wl('sm')}</td><td class="b">a. de dag van de familiemaaltijd</td></tr>
    <tr><td class="a">«El finde» betekent…</td><td>{wl('sm')}</td><td class="b">b. ook de brugdag vrij nemen</td></tr>
    <tr><td class="a">El domingo suele ser…</td><td>{wl('sm')}</td><td class="b">c. het weekend (spreektaal)</td></tr></table>
    <p style="font-size:8.6pt;color:var(--mut);margin-top:1mm">💡 «Voy a estudiar» = ik ga studeren (net als bij ons) — maar «ik moet werken» wordt <b>tengo que trabajar</b>, letterlijk «ik heb te werken».</p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:3mm;align-items:start">
    <div class="truc" style="margin:0"><b>Escucha y responde.</b> Kies één nummer van de playlist.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.3">Mi canción: {wl('lg')}<br>La escucho cuando voy a: {wl('lg')}</div>
    </div>
    <div class="truc" style="margin:0"><b>¿Y tú?</b> Schrijf één plan en één verplichting voor dit weekend.
      <div style="margin-top:1.5mm;font-size:9.6pt;line-height:2.4">{wl('full')}<br>{wl('full')}</div>
    </div>
  </div>
</div>
"""

REPASO=f"""
<div class="page sec" style="break-before:page">
  <div class="se">Repaso · Lo esencial de un vistazo</div><h2>Wat je nu kunt</h2>
  <div class="fams">
    <div class="pcard"><div class="t">Zo maak je een plan</div><div class="ej"><b>Voy a</b> + infinitivo · <b>Vamos a</b> + infinitivo · ¿Qué <b>vas a</b> hacer?</div><div class="t2">altijd <b>a</b> + het hele werkwoord</div></div>
    <div class="pcard"><div class="t">Zo zeg je wat je moet</div><div class="ej"><b>Tengo que</b> + infinitivo · <b>Tengo</b> hambre/sueño (zonder «que»)</div><div class="anchor">«que» vóór een werkwoord · géén «que» vóór een naamwoord</div></div>
  </div>
  <div class="regla" style="margin:4mm 0"><span class="tag">Frases para la clase</span>
    <div class="cogn" style="margin-top:1mm"><span>¿Qué vamos a hacer?</span><span>¿Tengo que escribir?</span><span>No entiendo</span><span>¿Puedes repetir?</span><span>Otra vez, por favor</span><span>Tengo una pregunta</span></div>
    <span style="font-size:8.6pt;color:var(--mut)">Handige klaszinnen — gebruik ze in het Spaans i.p.v. Nederlands.</span>
  </div>
  <table class="sem"><thead><tr><th style="text-align:left">Puedo… · Ik kan…</th><th>🟢</th><th>🟡</th><th>🔴</th></tr></thead>
    <tr><td>plannen zeggen (voy a / vamos a + infinitivo)</td><td></td><td></td><td></td></tr>
    <tr><td>verplichtingen zeggen (tengo que + infinitivo)</td><td></td><td></td><td></td></tr>
    <tr><td>tener + naamwoord gebruiken (hambre · sueño)</td><td></td><td></td><td></td></tr>
    <tr><td>een uitnodiging aannemen én beleefd afwijzen</td><td></td><td></td><td></td></tr></table>
  <div class="regla" style="margin-top:5mm"><span class="tag">Mini-test · recuerda sin mirar</span>
    <p style="margin:1mm 0 0;font-size:9.4pt">Sluit de cursus en vertaal uit het hoofd (ophalen = het beste leren).</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3mm 8mm;margin-top:2mm;font-size:9.8pt;line-height:2.2">
      <div>1. ik ga studeren → {wl('')}</div><div>2. ik moet werken → {wl('')}</div>
      <div>3. wat ga je doen? → {wl('')}</div><div>4. ik ben slaperig → {wl('')}</div>
      <div>5. ik kan niet → {wl('')}</div><div>6. ik heb dingen te doen → {wl('')}</div>
    </div>
  </div>
  <div class="guide"><span class="ic">🎮</span><div><span class="hand">Repasa jugando</span><div class="g">Oefen alles online met spelletjes, flashcards en audio op de digitale hub (scan de QR bij §1).</div></div></div>
  <div class="bridge"><b>Próxima parada →</b> In de volgende unit: <i>la comida / en el bar</i> (¿qué quieres tomar?). ¡Hasta pronto!</div>
</div>
"""

EDITBAR="""
<div class="editbar" id="eb">
  <b>✏️ C4 · U9</b>
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
document.getElementById('btnsave').onclick=function(){var html='<!doctype html>'+document.documentElement.outerHTML;var b=new Blob([html],{type:'text/html'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='C4_U9_Planes_bewerkt.html';a.click();};
</script>
"""

HTML=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 9 · Planes y obligaciones</title><style>{CSS}</style></head><body class="c4">
{EDITBAR}
{HERO}{ESCUCHA}{COMPR_SEC}{KIT}{GRAM}{PRAC}{TAREA}{MUSICA}{FUNCIONES_SEC}{REPASO}
{SCRIPT}
</body></html>"""
os.makedirs(f"{ROOT}/03-build/web/print",exist_ok=True)
open(f"{ROOT}/03-build/web/print/C4_U9.html","w",encoding="utf-8").write(HTML)
print("C4_U9.html (print+editable) geschreven:",len(HTML),"bytes")
