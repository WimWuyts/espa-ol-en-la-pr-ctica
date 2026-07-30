#!/usr/bin/env python3
# C4 · Unidad 11 — §2 KIT + §4 GRAMÁTICA (functioneel) + §5 TAREA + §Suena bien.
# Thema: El tiempo y los gustos · hace + naamwoord (het weer, onveranderlijk) ↔ tengo frío (persoon) ·
# me gusta / me gustan (+ nombre of + infinitivo) · adverbios de frecuencia (siempre → nunca).
# Scope: «me/te/le gusta» = VASTE CHUNKS, géén volledig pronomensysteem (dat is C6).
import base64, os
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

CLUSTERS=[
 ("¿Qué tiempo hace?","het weer","🌤️",[
   ("Hace frío","Het is koud"),("Hace calor","Het is warm"),
   ("Hace sol","Het is zonnig"),("Hace viento","Het waait"),
   ("Hace buen tiempo","Het is mooi weer"),("Hace mal tiempo","Het is slecht weer"),
   ("Llueve · nieva","Het regent · het sneeuwt"),("¿Qué tiempo hace?","Wat voor weer is het?"),
 ]),
 ("Las estaciones","de seizoenen","🍂",[
   ("la primavera","de lente"),("el verano","de zomer"),
   ("el otoño","de herfst"),("el invierno","de winter"),
   ("en verano · en invierno","in de zomer · in de winter"),("demasiado calor","te warm"),
 ]),
 ("Me gusta…","zeggen wat je graag hebt","❤️",[
   ("Me gusta el cine","Ik hou van film"),("Me gusta hacer yoga","Ik doe graag yoga"),
   ("Me gustan los deportes","Ik hou van sport"),("No me gusta la ópera","Ik hou niet van opera"),
   ("Me gusta más el frío","Ik hou meer van de kou"),("¿Te gusta…?","Hou jij van…?"),
   ("A mí también","Ik ook"),("A mí no · a mí tampoco","Ik niet · ik ook niet"),
 ]),
 ("El ocio y los deportes","vrije tijd","🎬",[
   ("el cine · la ópera","de cinema · de opera"),("el gimnasio","de sportzaal"),
   ("hacer yoga","yoga doen"),("hacer submarinismo","duiken"),
   ("ir a la playa","naar het strand gaan"),("los deportes","de sport"),
 ]),
 ("¿Con qué frecuencia?","hoe vaak","🔁",[
   ("siempre","altijd"),("casi siempre","bijna altijd"),
   ("a veces","soms"),("casi nunca","bijna nooit"),
   ("nunca","nooit"),("tres veces por semana","drie keer per week"),
   ("todos los años","elk jaar"),("Voy mucho al cine","Ik ga veel naar de cinema"),
 ]),
 ("De vacaciones","op vakantie","🧳",[
   ("irse de vacaciones","op vakantie gaan"),("a la playa · al pueblo","naar het strand · naar het dorp"),
   ("las fiestas de Navidad","de kerstdagen"),("con los tuyos","bij de jouwen (je familie)"),
   ("en cambio","daarentegen"),("está cerca de…","het ligt dicht bij…"),
 ]),
]
def chunkcard(es,nl):
    return (f'<div class="cc" data-es="{es}"><span class="cc-es">{es}</span>'
            f'<span class="cc-nl">{nl}</span><button class="cc-spk" title="luister">🔊</button></div>')
def cluster(name,sub,ic,items):
    body="".join(chunkcard(*i) for i in items)
    return (f'<div class="clu"><div class="clu-h"><span class="clu-ic">{ic}</span>'
            f'<span><b>{name}</b><i>{sub}</i></span></div><div class="cc-grid">{body}</div></div>')
KIT="".join(cluster(*c) for c in CLUSTERS)

# interactieve «gustómetro»: kies persoon + iets → juiste vorm (gusta ↔ gustan) verschijnt
REPARTO=r"""
<div class="builder">
  <div class="bh">❤️ <b>El gustómetro</b> · kies en klik — de juiste vorm verschijnt</div>
  <div class="brow">
    <div class="bcol"><span class="bl">1 · ¿a quién?</span>
      <button class="bopt on" data-slot="0" data-v="mi">a mí <i>(me gusta…)</i></button>
      <button class="bopt" data-slot="0" data-v="ti">a ti <i>(te gusta…)</i></button>
      <button class="bopt" data-slot="0" data-v="el">a él / a ella <i>(le gusta…)</i></button>
    </div>
    <div class="bcol"><span class="bl">2 · ¿qué?</span>
      <button class="bopt on" data-slot="1" data-v="0|el cine">el cine <i>(1 ding)</i></button>
      <button class="bopt" data-slot="1" data-v="0|la ópera">la ópera <i>(1 ding)</i></button>
      <button class="bopt" data-slot="1" data-v="1|los deportes">los deportes <i>(meervoud)</i></button>
      <button class="bopt" data-slot="1" data-v="1|las vacaciones">las vacaciones <i>(meervoud)</i></button>
      <button class="bopt" data-slot="1" data-v="0|hacer yoga">hacer yoga <i>(werkwoord)</i></button>
      <button class="bopt" data-slot="1" data-v="0|el frío">el frío <i>(1 ding)</i></button>
    </div>
  </div>
  <div class="bout" id="bout"></div>
  <p class="bhint">💡 <b>gusta</b> bij <b>één</b> ding of bij een <b>werkwoord</b> · <b>gustan</b> bij een <b>meervoud</b>. Het Spaans zegt letterlijk «het bevalt mij» — dus het ding is de baas over de vorm, niet jij.</p>
</div>
"""

GRAM=r"""
<div class="note">
  <div class="note-h">🔎 <b>Fíjate</b> · Kijk terug naar de scène — je hoorde dit al:</div>
  <div class="obs">«Siempre <span class="v">hace</span> buen tiempo en Canarias.» · «¡<span class="v">Hace</span> mucho viento!» · «<span class="v">Me gusta</span> el cine y <span class="v">me gusta</span> la ópera.» · «<span class="t">Casi nunca</span> voy a la ópera.»</div>
</div>

<div class="gcard">
  <h3><span class="v">hace</span> + het weer — <i>één vaste vorm</i></h3>
  <p class="gp">Over het weer praat je in het Spaans met <b>hace</b> + een <b>naamwoord</b>. Die vorm verandert <b>nooit</b>:</p>
  <table class="gt">
    <tr><td class="v">hace frío</td><td>het is koud</td><td class="ex">En invierno <b>hace frío</b>.</td></tr>
    <tr><td class="v">hace calor</td><td>het is warm</td><td class="ex">Aquí <b>hace demasiado calor</b>.</td></tr>
    <tr><td class="v">hace viento · sol</td><td>het waait · het is zonnig</td><td class="ex">¡<b>Hace</b> mucho <b>viento</b>!</td></tr>
    <tr><td class="v">hace buen/mal tiempo</td><td>het is mooi/slecht weer</td><td class="ex">Siempre <b>hace buen tiempo</b> en Canarias.</td></tr>
  </table>
  <p class="ojo">⚠️ <b>¡Ojo!</b> <span class="es">Nooit <s>es frío</s> of <s>está frío</s> voor het weer. En let op wie het koud heeft: <b>hace frío</b> = het ís koud (buiten) ↔ <b>tengo frío</b> = <i>ík</i> heb het koud (U9: tener + naamwoord). Twee héél verschillende zinnen!</span></p>
</div>

<div class="gcard">
  <h3><span class="v">me gusta</span> ↔ <span class="v">me gustan</span> — <i>het bevalt mij</i></h3>
  <p class="gp">Het Spaans draait de zin om: niet «ik hou van X», maar «X <b>bevalt mij</b>». Daarom kiest <b>het ding</b> de vorm:</p>
  <div class="mv">
    <div class="mv-c mv-m"><span class="mv-t">☝️ één ding of een werkwoord → <b>gusta</b></span><span><b>Me gusta</b> el cine.</span><span><b>Me gusta</b> hacer yoga.</span><span><i>ik hou van film · ik doe graag yoga</i></span></div>
    <div class="mv-c mv-f"><span class="mv-t">✌️ meervoud → <b>gustan</b></span><span><b>Me gustan</b> los deportes.</span><span>No <b>me gustan</b> los hoteles.</span><span><i>ik hou van sport · ik hou niet van hotels</i></span></div>
  </div>
  <p class="ojo">⚠️ <b>¡Ojo!</b> <span class="es">Nooit <s>yo gusto el cine</s> (dat betekent «ik val in de smaak»!). Zeg altijd <b>me gusta</b> / <b>me gustan</b>. Wil je iemand anders? <b>te gusta</b> (jij) · <b>le gusta</b> (hij/zij) — «A ella también <b>le gusta</b> hacer submarinismo.»</span></p>
</div>

<div class="gcard soft">
  <h3>Reaccionar: <span class="v">a mí también</span> · <span class="v">a mí no</span></h3>
  <p class="gp">Zo zeg je in één chunk of je het <b>eens</b> bent met iemands smaak:</p>
  <div class="stack">
    <div class="st"><b>A mí también.</b><i>ik ook (bij een + zin)</i></div>
    <div class="st"><b>A mí no.</b><i>ik niet (bij een + zin)</i></div>
    <div class="st"><b>A mí tampoco.</b><i>ik ook niet (bij een − zin)</i></div>
    <div class="st"><b>A mí sí.</b><i>ik wel (bij een − zin)</i></div>
  </div>
  <p class="ojo">💡 <span class="es">— «Me gusta el cine.» → <b>«A mí también.»</b> &nbsp;·&nbsp; — «No me gusta la ópera.» → <b>«A mí tampoco.»</b> Perfect voor de enquête in de eindtaak.</span></p>
</div>

<div class="gcard">
  <h3><span class="t">¿Con qué frecuencia?</span> — <i>de frecuencia-ladder</i></h3>
  <p class="gp">Van 100 % naar 0 %. Deze woorden staan meestal <b>vóór</b> het werkwoord:</p>
  <div class="stack">
    <div class="st"><b>siempre</b> — Siempre hace buen tiempo.<i>altijd · 100 %</i></div>
    <div class="st"><b>casi siempre</b> — Casi siempre voy al gimnasio.<i>bijna altijd</i></div>
    <div class="st"><b>a veces</b> — A veces te cansas de hoteles.<i>soms</i></div>
    <div class="st"><b>casi nunca</b> — Casi nunca voy a la ópera.<i>bijna nooit</i></div>
    <div class="st"><b>nunca</b> — Nunca hace ese frío en Madrid.<i>nooit · 0 %</i></div>
  </div>
  <p class="ojo">💡 <span class="es">Wil je het <b>precies</b> zeggen? Dat komt achteraan: «Voy al gimnasio <b>tres veces por semana</b>» · «Voy <b>todos los años</b> al Caribe» · «Voy <b>mucho</b> al cine». En <b>en cambio</b> = daarentegen: «En verano, <b>en cambio</b>, hace calor.»</span></p>
</div>
"""

TAREA=r"""
<div class="tcard">
  <div class="tmeta">
    <span><b>👤 Wie</b> jij + de klas</span>
    <span><b>🎯 Doel</b> iemand vinden met dezelfde smaak</span>
    <span><b>🗣️ Hoe</b> weer + gustos + hoe vaak</span>
    <span><b>✅ Resultaat</b> «Mi estación favorita» — een ficha + een enquête</span>
  </div>
  <h3>Mi estación favorita — <i>jouw seizoen, jouw smaak</i></h3>
  <ol class="pasos">
    <li><b>Elige tu estación.</b> Kies je favoriete seizoen en zeg welk weer het dan is:
        <div class="frame">«Mi estación favorita es <b>el verano</b>. En verano <b>hace</b> ____ .»</div></li>
    <li><b>¿Qué te gusta hacer?</b> Noem <b>twee</b> dingen — één met <i>gusta</i>, één met <i>gustan</i>:
        <div class="frame">«<b>Me gusta</b> ____ .» · «<b>Me gustan</b> ____ .» · «No <b>me gusta</b> ____ .»</div></li>
    <li><b>¿Con qué frecuencia?</b> Zeg hoe vaak:
        <div class="frame">«Voy ____ (siempre · a veces · casi nunca) · ____ veces por semana.»</div></li>
    <li><b>La encuesta.</b> Vraag het aan <b>drie</b> klasgenoten en reageer telkens:
        <div class="frame">«¿<b>Te gusta</b> ____ ?» — «Sí, me gusta.» → «<b>A mí también.</b>» / «No me gusta.» → «<b>A mí tampoco.</b>»</div></li>
    <li><b>Presenta.</b> «Somos dos: a Sara y a mí nos gusta el cine» — zeg wie dezelfde smaak heeft, zónder af te lezen.</li>
  </ol>
  <div class="carne">
    <div class="carne-h">MI FICHA · El tiempo y yo</div>
    <div class="carne-b diario">
      <div class="di-row"><span class="di-ic">🌤️</span><div class="di-lines">
        <div><span>Mi estación</span><i></i></div><div><span>Hace…</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">❤️</span><div class="di-lines">
        <div><span>Me gusta…</span><i></i></div><div><span>Me gustan…</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">🔁</span><div class="di-lines">
        <div><span>¿Cuántas veces?</span><i></i></div><div><span>Igual que…</span><i></i></div></div><span class="di-ok">☐</span></div>
    </div>
  </div>
  <p class="crit">🏁 <b>Klaar als…</b> je het weer van je seizoen zegt met «hace + naamwoord», twee smaken geeft (één keer <b>gusta</b>, één keer <b>gustan</b>), één frecuencia-woord gebruikt en in de enquête minstens één keer «a mí también / a mí tampoco» zegt — zónder af te lezen.</p>
</div>
"""

# §Suena bien · matrix A U11: de s is ALTIJD stemloos (/s/, nooit /z/) + klemtoon in getallen/prijzen
SWORDS=[("siempre","altijd"),("casi","bijna"),("gusta","bevallen"),("estaciones","seizoenen"),("vacaciones","vakantie"),("submarinismo","duiken")]
PLWORDS=[("los deportes","de sporten"),("tres veces","drie keer"),("mis primos","mijn kozijns"),("las gafas","de bril"),("los años","de jaren"),("dos cosas","twee dingen")]
DISCRIM=[("cielo",1),("siempre",0),("zona",1),("sol",0),("cinco",1),("casi",0),("doce",1),("seis",0)]
ACENTO=[("cuatro cincuenta","cua·<b>TRO</b> cin·<b>CUEN</b>·ta"),("veinticinco","vein·ti·<b>CIN</b>·co"),("treinta y dos","<b>TREIN</b>·ta y <b>DOS</b>"),("seis euros","<b>SEIS</b> <b>EU</b>·ros")]
def jcard(w,nl):
    return (f'<div class="cc" data-es="{w}"><span class="cc-es">{w}</span>'
            f'<span class="cc-nl">{nl}</span><button class="cc-spk">🔊</button></div>')
def dchip(w,ok): return f'<button class="dchip" data-ok="{ok}" data-w="{w}">🔊 {w}</button>'
def acchip(w,html): return f'<button class="shchip" data-w="{w}">🔊 {html}</button>'
SUENA=('<div class="suena">'
 '<div class="sblok"><h3>① La s es siempre sorda</h3>'
 '<p class="sh">De Spaanse <b>s</b> is <b>altijd</b> scherp (zoals in «sok»), <b>nooit</b> zoals onze <b>z</b> in «zomer». Klik 🔊 en spreek na.</p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in SWORDS)}</div></div>'
 '<div class="sblok"><h3>② Ook de -s van het meervoud</h3>'
 '<p class="sh">Ook tussen twee klinkers blijft de <b>s</b> scherp: «lo<b>s</b> año<b>s</b>», «tre<b>s</b> vece<b>s</b>» — nooit /z/.</p>'
 f'<div class="cc-grid tight">{"".join(jcard(*w) for w in PLWORDS)}</div>'
 '<p class="ojo2">⚠️ <b>¡Ojo!</b> <span>Nederlandstaligen maken van «lo<b>s</b> año<b>s</b>» vaak «lo<b>z</b> año<b>z</b>». Houd de s scherp — dat is meteen hoorbaar.</span></p></div>'
 '<div class="sblok"><h3>③ ¿s o c/z? · klik wat je hoort</h3>'
 '<p class="sh">Herhaling van U3: in Spanje klinken <b>c+e/i</b> en <b>z</b> als /θ/ (tong tussen de tanden). Klik de woorden met díe klank.</p>'
 f'<div class="shrow">{"".join(dchip(*d) for d in DISCRIM)}</div>'
 '<p class="sfb" id="dfb"></p></div>'
 '<div class="sblok"><h3>④ El acento en los precios</h3>'
 '<p class="sh">Waar valt de klemtoon in prijzen en getallen? Klik 🔊 en herhaal — uit de scène: «Son cuatro cincuenta».</p>'
 f'<div class="shrow">{"".join(acchip(*a) for a in ACENTO)}</div></div>'
 '</div>')

CSS=FONTS+r"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--card:#fff;
--p:#2563EB;--v:#EA7317;--o:#1E9E74;--pl:#0E9E97;--t:#7C3AED;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#181513;--crema:#241C1B;--gt:#3A1E20;--line:#3a302e;--card:#211a19}
*{box-sizing:border-box}body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
.top{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;padding:22px}
.top h1{font-family:var(--disp);font-weight:800;margin:0;font-size:26px}.top p{margin:5px 0 0;opacity:.95;max-width:760px}
main{max-width:1000px;margin:0 auto;padding:18px}
.subh{font-family:var(--disp);color:var(--ink);font-size:20px;margin:30px 0 4px;padding-bottom:6px;border-bottom:2px solid var(--gt);display:flex;gap:10px;align-items:center}
.subh small{font-weight:400;color:var(--mut);font-size:13px;font-family:var(--body)}
.clu{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 16px;margin:14px 0}
.clu-h{display:flex;gap:10px;align-items:center;margin-bottom:10px}
.clu-ic{font-size:22px}.clu-h b{font-family:var(--disp);font-size:17px}.clu-h i{display:block;color:var(--mut);font-size:12.5px;font-style:normal}
.cc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:10px}
.cc-grid.tight{grid-template-columns:repeat(auto-fill,minmax(150px,1fr))}
.cc{position:relative;border:1.5px solid var(--line);border-left:4px solid var(--g);border-radius:12px;padding:9px 34px 9px 12px;cursor:pointer;background:var(--paper)}
.cc:hover{background:var(--gt)}
.cc-es{display:block;font-family:var(--disp);font-weight:700;font-size:15.5px}
.cc-nl{display:block;color:var(--mut);font-size:12.5px}
.cc-spk{position:absolute;right:8px;top:50%;transform:translateY(-50%);border:none;background:transparent;cursor:pointer;font-size:15px;opacity:.55}
.note{background:var(--gt);border-radius:14px;padding:12px 16px;margin:14px 0}
.note-h{font-weight:700;margin-bottom:4px}.obs{font-size:16px;font-family:var(--disp)}
.p{color:var(--p);font-weight:700}.v{color:var(--v);font-weight:700}.o{color:var(--o);font-weight:700}.pl{color:var(--pl);font-weight:700}.t{color:var(--t);font-weight:700}
.gcard{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:14px 0}
.gcard.soft{background:var(--crema)}
.gcard h3{font-family:var(--disp);margin:0 0 6px;font-size:18px}
.gp{margin:0 0 10px;font-size:14px;color:var(--ink)}
.gt{border-collapse:collapse;width:100%;font-size:14.5px}
.gt td{border-bottom:1px solid var(--line);padding:7px 10px}
.gt td.v{color:var(--v);font-weight:700;font-family:var(--disp)}.gt td.ex{color:var(--mut);font-style:italic}
.ojo{background:var(--gt);border-radius:10px;padding:9px 12px;font-size:13.5px;margin:12px 0 0}
.ojo .es{font-weight:600;color:var(--ink)}
.mv{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:8px 0}
.mv-c{border-radius:12px;padding:12px;display:flex;flex-direction:column;gap:4px;font-family:var(--disp);font-size:14.5px}
.mv-c b{color:var(--gd)}.mv-t{font-size:13px;font-weight:800;margin-bottom:4px}
.mv-c i{font-family:var(--body);font-size:12px;font-style:italic;opacity:.85}
.mv-m{background:#E6F7F5;color:#0B7A73}.mv-f{background:#FEF1E7;color:#B4530E}
[data-theme=dark] .mv-m{background:#123a37;color:#7fd8cf}[data-theme=dark] .mv-f{background:#3a2415;color:#f3c39a}
.stack{display:flex;flex-direction:column;gap:6px;margin:8px 0}
.st{background:var(--paper);border:1.5px solid var(--line);border-left:4px solid var(--v);border-radius:10px;padding:8px 12px;font-family:var(--disp);font-size:15px}
.st i{float:right;font-family:var(--body);font-size:12px;color:var(--mut);font-style:normal}
.dial{display:flex;flex-direction:column;gap:6px;margin:6px 0}
.db,.da{border-radius:12px;padding:8px 12px;font-size:14.5px;max-width:88%}
.db{background:var(--crema);align-self:flex-start}
.da{background:var(--gt);align-self:flex-end;text-align:right}
.builder{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 16px;margin:14px 0}
.bh{font-family:var(--disp);font-size:15px;color:var(--gd);margin-bottom:8px}
.brow{display:grid;grid-template-columns:1fr 1fr;gap:12px}@media(max-width:760px){.brow{grid-template-columns:1fr}}
.bcol{display:flex;flex-direction:column;gap:6px}
.bl{font-size:11.5px;font-weight:700;color:var(--mut);text-transform:uppercase}
.bopt{border:1.5px solid var(--line);background:var(--paper);border-radius:10px;padding:7px 10px;font-size:14px;font-weight:600;cursor:pointer;text-align:left;color:var(--ink);font-family:var(--body)}
.bopt i{color:var(--mut);font-size:11.5px;font-style:normal}
.bopt.on{border-color:var(--g);background:var(--gt);color:var(--gd)}
.bout{margin-top:12px;background:var(--gt);border-radius:12px;padding:12px 14px;font-family:var(--disp);font-size:19px;color:var(--gd);text-align:center;min-height:26px}
.bhint{font-size:12.5px;color:var(--mut);margin:8px 0 0}
.tcard{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:14px 0}
.tcard h3{font-family:var(--disp);font-size:19px;margin:8px 0 10px}
.tmeta{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px;background:var(--gt);border-radius:12px;padding:12px;font-size:13px}
.pasos{margin:6px 0 12px;padding-left:22px}.pasos li{margin:8px 0}
.frame{border:1.5px dashed var(--g);border-radius:10px;padding:8px 12px;margin:6px 0;font-family:var(--disp);color:var(--gd);background:var(--gt)}
.carne{max-width:460px;border:2px solid var(--g);border-radius:14px;overflow:hidden;margin:14px 0}
.carne-h{background:var(--g);color:#fff;font-family:var(--disp);font-weight:700;font-size:12.5px;padding:6px 12px}
.diario{display:flex;flex-direction:column;padding:6px 12px 12px}
.di-row{display:flex;gap:12px;align-items:center;padding:10px 0;border-bottom:1px solid var(--line)}
.di-row:last-child{border-bottom:none}
.di-ic{font-size:26px;flex:none}
.di-lines{flex:1;display:flex;flex-direction:column;gap:10px}
.di-lines div{display:flex;gap:8px;align-items:baseline}.di-lines span{font-size:12px;color:var(--mut);width:74px}
.di-lines i{flex:1;border-bottom:1.5px solid var(--line);height:15px}
.di-ok{font-size:20px;color:var(--mut);flex:none}
.crit{background:var(--crema);border-radius:10px;padding:10px 14px;font-size:13.5px;margin-top:10px}
.foot{color:var(--mut);font-size:12px;text-align:center;margin:26px 0}
.suena{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:760px){.suena{grid-template-columns:1fr}}
.sblok{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 16px}
.sblok h3{font-family:var(--disp);color:var(--gd);margin:0 0 4px;font-size:16px}
.sh{color:var(--mut);font-size:12.5px;margin:0 0 10px}
.ojo2{background:var(--gt);border-radius:10px;padding:8px 12px;font-size:12.5px;margin:10px 0 0}.ojo2 b{color:#DC2626}
.shrow{display:flex;flex-wrap:wrap;gap:8px}
.shchip,.dchip{border:1.5px solid var(--line);background:var(--paper);border-radius:20px;padding:8px 14px;font-weight:700;font-size:14px;cursor:pointer;font-family:var(--disp);color:var(--ink)}
.shchip:hover,.dchip:hover{background:var(--gt);border-color:var(--g)}
.dchip.ok{background:var(--g);color:#fff;border-color:var(--g)}
.dchip.no{background:#fde8e8;border-color:#DC2626;color:#DC2626;text-decoration:line-through}
.sfb{font-size:13px;color:var(--gd);font-weight:600;min-height:18px;margin:8px 0 0}
"""

HTML=f"""<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U11 · Kit · Gramática · Tarea</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 11 · El tiempo y los gustos</h1><p>De <b>kit de supervivencia</b> (het weer, de seizoenen, zeggen wat je graag doet en hoe vaak), een korte <b>uitlegnota</b> waar het helpt, en je <b>eindtaak</b>. Klik 🔊 om woorden te horen.</p></div>
<main>
 <h2 class="subh">🔊 Suena bien <small>uitspraak — de s is altijd scherp</small></h2>
 {SUENA}
 <h2 class="subh">❤️ El gustómetro <small>klik en zie de juiste vorm</small></h2>
 {REPARTO}
 <h2 class="subh">§2 · Kit de supervivencia <small>de chunks per situatie — klik om te horen</small></h2>
 {KIT}
 <h2 class="subh">§4 · Gramática en la práctica <small>kort en functioneel — geen theorie om de theorie</small></h2>
 {GRAM}
 <h2 class="subh">§5 · Tarea final <small>jouw communicatieve opdracht</small></h2>
 {TAREA}
 <div class="foot">C4 · «Welcome to Spanish» · Unidad 11 · El tiempo y los gustos</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.cc').forEach(function(c){{var es=c.getAttribute('data-es').replace(/·.*/,'').replace(/[…?¿!¡]/g,'');c.onclick=function(){{speak(es);}};}});
document.querySelectorAll('.shchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));}};}});
var dtot=document.querySelectorAll('.dchip[data-ok="1"]').length;
document.querySelectorAll('.dchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));var ok=b.getAttribute('data-ok')==='1';b.classList.remove('ok','no');b.classList.add(ok?'ok':'no');var n=document.querySelectorAll('.dchip.ok').length;var fb=document.getElementById('dfb');fb.textContent=ok?('¡/θ/ con c o z! · '+n+'/'+dtot+' 👏'):'Die heeft de scherpe /s/. Prueba otra.';}};}});
// taakverdeler
var FORM={{mi:["Me gusta","Me gustan"],ti:["Te gusta","Te gustan"],el:["Le gusta","Le gustan"]}};
var pick=["mi","0|el cine"];
function frase(){{var pl=pick[1].split("|")[0]==="1";var cosa=pick[1].split("|")[1];return FORM[pick[0]][pl?1:0]+" "+cosa+".";}}
function render(){{document.getElementById('bout').textContent=frase();}}
document.querySelectorAll('.bopt').forEach(function(b){{b.onclick=function(){{var s=+b.getAttribute('data-slot');pick[s]=b.getAttribute('data-v');
 document.querySelectorAll('.bopt[data-slot="'+s+'"]').forEach(function(x){{x.classList.toggle('on',x===b);}});render();speak(frase());}};}});
render();
</script></body></html>"""
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U11_kgt.html","w").write(HTML)
print("C4_U11_kgt.html geschreven:",len(HTML),"bytes")
