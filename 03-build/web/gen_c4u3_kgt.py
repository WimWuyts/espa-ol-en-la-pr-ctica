#!/usr/bin/env python3
# C4 · Unidad 3 — §2 KIT DE SUPERVIVENCIA (visueel chunk-netwerk) + §4 GRAMÁTICA EN LA
# PRÁCTICA (mini-nota, functioneel, GEEN kader) + §5 TAREA FINAL (communicatief) + §Suena bien.
# Thema: ¿De dónde eres? soy de + país · gentilicio m/v · idiomas. Español primero + NL-steun. C4-rood, TTS, standalone.
import base64, os
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

# ── §2 KIT · chunks per taalhandeling (functie → chunks: ES · NL) ──────────────
CLUSTERS=[
 ("Preguntar el origen","vragen waar iemand vandaan komt","❓",[
   ("¿De dónde eres?","Waar kom je vandaan? (jij)"),("¿De dónde es usted?","Waar komt u vandaan?"),
   ("¿De qué país?","Uit welk land?"),("¿Y tú?","En jij?"),("¿Y usted?","En u?"),
 ]),
 ("Decir de dónde soy","zeggen waar je vandaan komt · ser de + país","📍",[
   ("Soy de Bélgica","Ik kom uit België"),("Soy de España","Ik kom uit Spanje"),
   ("Soy de México","Ik kom uit Mexico"),("Soy de Flandes","Ik kom uit Vlaanderen"),
   ("Soy de aquí","Ik kom van hier"),
 ]),
 ("La nacionalidad","de nationaliteit · gentilicio (♂/♀)","🪪",[
   ("belga · belga","Belgisch (♂=♀)"),("español · española","Spaans"),
   ("mexicano · mexicana","Mexicaans"),("colombiano · colombiana","Colombiaans"),
   ("argentino · argentina","Argentijns"),("marroquí · marroquí","Marokkaans (♂=♀)"),
 ]),
 ("Los idiomas","de talen · hablar","🗣️",[
   ("Hablo español","Ik spreek Spaans"),("Hablo neerlandés","Ik spreek Nederlands"),
   ("Hablo francés e inglés","Ik spreek Frans en Engels"),("¿Qué idiomas hablas?","Welke talen spreek je?"),
   ("un poco","een beetje"),("bastante bien","best goed"),
 ]),
 ("Países del mundo hispano","landen waar men Spaans spreekt","🌍",[
   ("España","Spanje"),("México","Mexico"),("Argentina","Argentinië"),
   ("Colombia","Colombia"),("Perú","Peru"),("Bélgica","België (jouw land)"),
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

# ── §4 GRAMÁTICA EN LA PRÁCTICA — mini-nota's (functioneel, kleursemantiek) ────
# person=blauw (p), plaats=turquoise (pl), werkwoord=oranje (v). observeren → compacte regel.
GRAM=r"""
<div class="note">
  <div class="note-h">🔎 <b>Fíjate</b> · Kijk terug naar de scène — je hoorde dit al:</div>
  <div class="obs">«<span class="v">¿De dónde</span> <span class="v">eres</span>?» → «<span class="p">Yo</span> <span class="v">soy</span> <span class="pl">de Argelia</span>.» · «<span class="v">Eres</span> argelin<u>a</u> (chica) · argelin<u>o</u> (chico).» · «<span class="v">Hablo</span> español.»</div>
</div>

<div class="gcard">
  <h3><span class="v">soy de</span> + <span class="pl">país</span> — <i>waar je vandaan komt</i></h3>
  <p class="gp">Om te zeggen uit welk <b>land</b> je komt. Twee vaste vormen volstaan nu:</p>
  <table class="gt">
    <tr><td class="p">yo</td><td class="v">soy de</td><td>ik kom uit</td><td class="ex"><b>Soy de</b> <span class="pl">Bélgica</span>.</td></tr>
    <tr><td class="p">tú</td><td class="v">eres de</td><td>jij komt uit</td><td class="ex">¿<b>Eres de</b> <span class="pl">España</span>?</td></tr>
    <tr><td class="p">él/ella/usted</td><td class="v">es de</td><td>hij/zij komt · u komt uit</td><td class="ex">María <b>es de</b> <span class="pl">Sevilla</span>.</td></tr>
  </table>
  <p class="ojo">⚠️ <b>¡Ojo!</b> <span class="es">Zeg «soy <b>de</b> Argelia» (= ik kom <b>uit</b> Argelije), <b>niet</b> «soy Argelia».</span> De extranjera maakt net die fout in de video. Land = met <b>de</b>; nationaliteit = zónder <b>de</b> (soy argelina).</p>
</div>

<div class="gcard">
  <h3>El gentilicio — <i>man of vrouw</i> (de nationaliteit)</h3>
  <p class="gp">De nationaliteit past zich aan aan ♂/♀. Drie patronen:</p>
  <div class="mv">
    <div class="mv-c mv-m"><span class="mv-t">♂ un chico</span><span>mexican<b>o</b> · colombian<b>o</b></span><span>portugu<b>és</b> · franc<b>és</b> · ingl<b>és</b></span></div>
    <div class="mv-c mv-f"><span class="mv-t">♀ una chica</span><span>mexican<b>a</b> · colombian<b>a</b></span><span>portugu<b>esa</b> · franc<b>esa</b> · ingl<b>esa</b></span></div>
  </div>
  <p class="gp" style="margin-top:10px">Sommige blijven <b>gelijk</b> voor ♂ én ♀: <b>belga</b>, <b>marroquí</b>, <b>estadounidense</b>, <b>canadiense</b>.</p>
  <p class="ojo">⚠️ <b>¡Ojo!</b> <span class="es">In het Spaans schrijf je de nationaliteit en de taal met een <b>kleine letter</b>: soy <b>español</b>, hablo <b>neerlandés</b>.</span> (In het Nederlands/Engels net met een hoofdletter — een klassieke valstrik!)</p>
</div>

<div class="gcard">
  <h3><span class="v">hablo</span> + <i>idioma</i> — <i>welke talen je spreekt</i></h3>
  <p class="gp">De taal = vaak de nationaliteit «in het klein»: español → <b>el español</b>. Vaste vormen:</p>
  <table class="gt">
    <tr><td class="v">Hablo</td><td>ik spreek</td><td class="ex"><b>Hablo</b> neerlandés y un poco de español.</td></tr>
    <tr><td class="v">¿Hablas…?</td><td>spreek jij…?</td><td class="ex">¿<b>Hablas</b> francés?</td></tr>
    <tr><td class="v">¿Habla usted…?</td><td>spreekt u…?</td><td class="ex">¿<b>Habla usted</b> inglés?</td></tr>
  </table>
  <p class="ojo">💡 <span class="es">In de video spreekt de vrouw <b>tres idiomas</b>: árabe, francés y español.</span> Steun: «un poco» / «bastante bien» zeggen hoe góed je iets spreekt.</p>
</div>

<div class="gcard soft">
  <h3>tú <span class="v">↔</span> usted — <i>informeel of beleefd</i></h3>
  <p class="gp">Met vrienden/klasgenoten: <b>tú</b> → «¿De dónde <b>eres</b>?». Met een onbekende volwassene / formeel: <b>usted</b> → «¿De dónde <b>es</b> usted?». In de video vraagt Julio beleefd «¿<b>Habla usted</b> francés?». In de klas gebruiken we meestal <b>tú</b>.</p>
</div>
"""

# ── §5 TAREA FINAL — communicatief (afzender·ontvanger·doel·situatie·resultaat) ─
TAREA=r"""
<div class="tcard">
  <div class="tmeta">
    <span><b>👤 Wie</b> jij + 2 klasgenoten (of bekende personen)</span>
    <span><b>🎯 Doel</b> een mini-kaart maken: wie komt waarvandaan &amp; spreekt welke taal</span>
    <span><b>🗣️ Hoe</b> mondeling presenteren + op de kaart aanwijzen</span>
    <span><b>✅ Resultaat</b> «Mi mapa» ingevuld (3 personen) + kort voorgesteld</span>
  </div>
  <h3>Mi mapa · ¿De dónde eres? — <i>plaats 3 personen op de wereldkaart</i></h3>
  <ol class="pasos">
    <li><b>Elige a 3 personas.</b> Kies jezelf + 2 anderen (klasgenoten of bekende personen: cantantes, futbolistas…).</li>
    <li><b>Pregunta el origen.</b> Vraag (of bedenk) waar ze vandaan komen:
        <div class="frame">«¿De dónde eres? / ¿De qué país?»</div></li>
    <li><b>Escribe la ficha.</b> Vul per persoon in — let op de gentilicio (♂/♀) en de kleine letter:
        <div class="frame">«____ es de ____ (país). Es ____ (nacionalidad) y habla ____ (idioma).»</div></li>
    <li><b>Preséntalo.</b> Wijs het land aan op de kaart (Mapa-tab) en stel je 3 personen voor aan de klas.</li>
  </ol>
  <div class="carne">
    <div class="carne-h">MI MAPA · Academia «Bienvenidos al español»</div>
    <div class="carne-b diario">
      <div class="di-row"><span class="di-ic">🧍</span><div class="di-lines">
        <div><span>Nombre</span><i></i></div><div><span>Es de…</span><i></i></div><div><span>Es…/habla…</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">🧑</span><div class="di-lines">
        <div><span>Nombre</span><i></i></div><div><span>Es de…</span><i></i></div><div><span>Es…/habla…</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">👤</span><div class="di-lines">
        <div><span>Nombre</span><i></i></div><div><span>Es de…</span><i></i></div><div><span>Es…/habla…</span><i></i></div></div><span class="di-ok">☐</span></div>
    </div>
  </div>
  <p class="crit">🏁 <b>Klaar als…</b> je voor 3 personen zegt «<b>es de</b> + land» én de juiste <b>gentilicio</b> (♂/♀, kleine letter) en <b>taal</b> geeft, en het land op de kaart aanwijst — zónder af te lezen.</p>
</div>
"""

# ── §Suena bien · uitspraak (matrix A U3: ñ + c/z /θ/~/s/ + acentuación aguda -dad/-és) ──
# reservoir: DS-009 uitspraakpagina · SK-080 · SK-086 · SK-087 (discriminatie) · SK-088 (shadowing) · PPT-037/038
NWORDS=[("España","Spanje"),("español","Spaans"),("mañana","morgen/ochtend"),
 ("niño","kind"),("señor","meneer"),("año","jaar")]
CZWORDS=[("nacionalidad","nationaliteit"),("Francia","Frankrijk"),("Venezuela","Venezuela"),
 ("gracias","dank je"),("cinco","vijf"),("zona","zone")]
# data-ok=1 = heeft de zachte c/z-klank (/θ/ in Spanje, /s/ in LatAm): c+e, c+i of z
DISCRIM=[("cinco",1),("casa",0),("Venezuela",1),("gato",0),("gracias",1),("colombiano",0),("zapato",1),("país",0)]
ACENTO=[("nacionalidad","na·cio·na·li·<b>DAD</b>"),("portugués","por·tu·<b>GUÉS</b>"),("francés","fran·<b>CÉS</b>"),("inglés","in·<b>GLÉS</b>")]
def jcard(w,nl):
    return (f'<div class="cc" data-es="{w}"><span class="cc-es">{w}</span>'
            f'<span class="cc-nl">{nl}</span><button class="cc-spk">🔊</button></div>')
def dchip(w,ok): return f'<button class="dchip" data-ok="{ok}" data-w="{w}">🔊 {w}</button>'
def acchip(w,html): return f'<button class="shchip" data-w="{w}">🔊 {html}</button>'
SUENA=('<div class="suena">'
 '<div class="sblok"><h3>① La eñe · ñ — de klank van España</h3>'
 '<p class="sh">De <b>ñ</b> klinkt als de NL «nj» in «oranje» of «Spanje». Klik 🔊 en spreek na.</p>'
 f'<div class="cc-grid tight">{"".join(jcard(*n) for n in NWORDS)}</div>'
 '<p class="ojo2">⚠️ <b>¡Ojo!</b> <span>ñ ≠ n: «año» (jaar) klinkt anders dan «ano». Het streepje (~) verandert de klank én de betekenis!</span></p></div>'
 '<div class="sblok"><h3>② La c y la z · /θ/ ~ /s/</h3>'
 '<p class="sh">In Spanje klinken <b>z</b> en <b>c</b> (vóór e/i) als een zachte <b>th</b> (zoals Engels «think»); in Latijns-Amerika als <b>s</b>. Allebei goed!</p>'
 f'<div class="cc-grid tight">{"".join(jcard(*c) for c in CZWORDS)}</div>'
 '<p class="ojo2">⚠️ <b>¡Ojo!</b> <span>c + a/o/u = /k/ (<b>ca</b>sa, <b>co</b>lombiano) · maar c + e/i = /θ~s/ (<b>ci</b>nco, Fran<b>ci</b>a) — net als de z.</span></p></div>'
 '<div class="sblok"><h3>③ ¿c/z suave o no? · teken wat je hoort</h3>'
 '<p class="sh">Klik de woorden met de <b>zachte c/z</b>-klank /θ~s/ (groen = juist). Klik 🔊 om te horen.</p>'
 f'<div class="shrow">{"".join(dchip(*d) for d in DISCRIM)}</div>'
 '<p class="sfb" id="dfb"></p></div>'
 '<div class="sblok"><h3>④ El acento agudo · -dad / -és</h3>'
 '<p class="sh">Woorden op <b>-dad</b> en <b>-és</b> hebben de klemtoon op de <b>laatste</b> lettergreep (<i>aguda</i>). Klik 🔊 en herhaal met dezelfde melodie.</p>'
 f'<div class="shrow">{"".join(acchip(*a) for a in ACENTO)}</div></div>'
 '</div>')

CSS=FONTS+r"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--card:#fff;
--p:#2563EB;--v:#EA7317;--pl:#0E9E97;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#181513;--crema:#241C1B;--gt:#3A1E20;--line:#3a302e;--card:#211a19}
*{box-sizing:border-box}body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
.top{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;padding:22px}
.top h1{font-family:var(--disp);font-weight:800;margin:0;font-size:26px}.top p{margin:5px 0 0;opacity:.95;max-width:760px}
main{max-width:1000px;margin:0 auto;padding:18px}
.subh{font-family:var(--disp);color:var(--ink);font-size:20px;margin:30px 0 4px;padding-bottom:6px;border-bottom:2px solid var(--gt);display:flex;gap:10px;align-items:center}
.subh small{font-weight:400;color:var(--mut);font-size:13px;font-family:var(--body)}
/* §2 KIT */
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
/* §4 GRAM */
.note{background:var(--gt);border-radius:14px;padding:12px 16px;margin:14px 0}
.note-h{font-weight:700;margin-bottom:4px}
.obs{font-size:16px;font-family:var(--disp)}
.p{color:var(--p);font-weight:700}.v{color:var(--v);font-weight:700}.pl{color:var(--pl);font-weight:700}
.gcard{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:14px 0}
.gcard.soft{background:var(--crema)}
.gcard h3{font-family:var(--disp);margin:0 0 6px;font-size:18px}
.gp{margin:0 0 10px;font-size:14px;color:var(--ink)}
.gt{border-collapse:collapse;width:100%;font-size:14.5px}
.gt td{border-bottom:1px solid var(--line);padding:7px 10px}
.gt td.p{color:var(--p);font-weight:600}.gt td.v{color:var(--v);font-weight:700;font-family:var(--disp)}
.gt td.ex{color:var(--mut);font-style:italic}
.ojo{background:var(--gt);border-radius:10px;padding:9px 12px;font-size:13.5px;margin:12px 0 0}
.ojo .es{font-weight:600;color:var(--ink)}
.mv{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:8px 0}
.mv-c{border-radius:12px;padding:12px;display:flex;flex-direction:column;gap:4px;font-family:var(--disp);font-size:15px}
.mv-c b{color:var(--gd)}.mv-t{font-size:13px;font-weight:800;margin-bottom:4px}
.mv-m{background:#E8F0FE;color:#1E40AF}.mv-f{background:#FCE7F0;color:#9D174D}
[data-theme=dark] .mv-m{background:#1b2740;color:#bcd0f5}[data-theme=dark] .mv-f{background:#3a1c2b;color:#f3b8d0}
/* §5 TAREA */
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
.di-lines div{display:flex;gap:8px;align-items:baseline}.di-lines span{font-size:12px;color:var(--mut);width:64px}
.di-lines i{flex:1;border-bottom:1.5px solid var(--line);height:15px}
.di-ok{font-size:20px;color:var(--mut);flex:none}
.crit{background:var(--crema);border-radius:10px;padding:10px 14px;font-size:13.5px;margin-top:10px}
.foot{color:var(--mut);font-size:12px;text-align:center;margin:26px 0}
/* §Suena bien */
.suena{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:760px){.suena{grid-template-columns:1fr}}
.sblok{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 16px}
.sblok h3{font-family:var(--disp);color:var(--gd);margin:0 0 4px;font-size:16px}
.sh{color:var(--mut);font-size:12.5px;margin:0 0 10px}
.ojo2{background:var(--gt);border-radius:10px;padding:8px 12px;font-size:12.5px;margin:10px 0 0}.ojo2 b{color:#DC2626}
.shrow{display:flex;flex-wrap:wrap;gap:8px}
.shchip{border:1.5px solid var(--line);background:var(--paper);border-radius:20px;padding:8px 14px;font-weight:700;font-size:14px;cursor:pointer;font-family:var(--disp);color:var(--ink)}
.shchip:hover{background:var(--gt);border-color:var(--g)}
.dchip{border:1.5px solid var(--line);background:var(--paper);border-radius:20px;padding:8px 14px;font-weight:700;font-size:14px;cursor:pointer;font-family:var(--disp);color:var(--ink)}
.dchip:hover{background:var(--gt);border-color:var(--g)}
.dchip.ok{background:var(--g);color:#fff;border-color:var(--g)}
.dchip.no{background:#fde8e8;border-color:#DC2626;color:#DC2626;text-decoration:line-through}
.sfb{font-size:13px;color:var(--gd);font-weight:600;min-height:18px;margin:8px 0 0}
"""

HTML=f"""<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U3 · Kit · Gramática · Tarea</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 3 · Nacionalidades y países</h1><p>De <b>kit de supervivencia</b> (¿de dónde eres? · soy de + land · nationaliteit · talen), een korte <b>uitlegnota</b> waar het helpt, en je <b>eindtaak</b>. Klik 🔊 om woorden te horen.</p></div>
<main>
 <h2 class="subh">🔊 Suena bien <small>uitspraak — de ñ, de c/z &amp; de klemtoon (aguda)</small></h2>
 {SUENA}

 <h2 class="subh">§2 · Kit de supervivencia <small>de chunks per situatie — klik om te horen</small></h2>
 {KIT}

 <h2 class="subh">§4 · Gramática en la práctica <small>kort en functioneel — geen theorie om de theorie</small></h2>
 {GRAM}

 <h2 class="subh">§5 · Tarea final <small>jouw communicatieve opdracht</small></h2>
 {TAREA}

 <div class="foot">C4 · «Bienvenidos al español» · Unidad 3 · Nacionalidades y países</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.cc').forEach(function(c){{var es=c.getAttribute('data-es').replace(/·.*/,'').replace(/[…?¿!¡]/g,'');c.onclick=function(){{speak(es);}};}});
document.querySelectorAll('.shchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));}};}});
var dtot=document.querySelectorAll('.dchip[data-ok="1"]').length;
document.querySelectorAll('.dchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));var ok=b.getAttribute('data-ok')==='1';b.classList.remove('ok','no');b.classList.add(ok?'ok':'no');var n=document.querySelectorAll('.dchip.ok').length;var fb=document.getElementById('dfb');fb.textContent=ok?('¡Suave! /θ~s/ · '+n+'/'+dtot+' encontradas 👏'):'Esa es /k/ (c+a/o/u). Prueba otra.';}};}});
</script></body></html>"""
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U3_kgt.html","w").write(HTML)
print("C4_U3_kgt.html geschreven:",len(HTML),"bytes")
