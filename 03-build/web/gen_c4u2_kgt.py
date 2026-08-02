#!/usr/bin/env python3
# C4 · Unidad 2 — §2 KIT DE SUPERVIVENCIA (visueel chunk-netwerk) + §4 GRAMÁTICA EN LA
# PRÁCTICA (mini-nota, functioneel, GEEN kader) + §5 TAREA FINAL (communicatief) + §Suena bien.
# Thema: Saludos por momento del día + estar + estado. Español primero + NL-steun. C4-rood, TTS, standalone.
import base64, os
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

# ── §2 KIT · chunks per taalhandeling (functie → chunks: ES · NL) ──────────────
CLUSTERS=[
 ("Saludar por el día","begroeten volgens het moment","👋",[
   ("Buenos días","Goedemorgen (tot ~12u)"),("Buenas tardes","Goedemiddag (~12–20u)"),
   ("Buenas noches","Goedenavond / -nacht (na ~20u)"),("¡Hola!","Hallo! (altijd)"),
   ("¡Buenas!","Hoi! (informeel, elk moment)"),
 ]),
 ("Preguntar cómo va","vragen hoe het gaat","❓",[
   ("¿Qué tal?","Hoe gaat het? (informeel)"),("¿Cómo estás?","Hoe gaat het? (jij)"),
   ("¿Cómo está usted?","Hoe gaat het met u?"),("¿Y tú?","En jij?"),("¿Y usted?","En u?"),
 ]),
 ("Decir cómo estoy","zeggen hoe je je voelt · estar + estado","🙂",[
   ("Estoy bien","Ik voel me goed"),("Muy bien","Heel goed"),("Regular","Gaat wel"),
   ("Estoy cansado/a","Ik ben moe"),("Estoy ocupado/a","Ik heb het druk"),
   ("Estoy nervioso/a","Ik ben nerveus"),("Estoy enfermo/a","Ik ben ziek"),("Estoy fatal","Heel slecht"),
 ]),
 ("Cortesía","beleefdheid","🙏",[
   ("Por favor","Alsjeblieft (vragend)"),("Gracias","Dank je"),("Muchas gracias","Hartelijk dank"),
   ("De nada","Graag gedaan"),("Perdona","Sorry / pardon"),
 ]),
 ("Despedirse","afscheid nemen","👋",[
   ("Adiós","Dag / tot ziens"),("Hasta luego","Tot straks"),("Hasta mañana","Tot morgen"),
   ("¡Nos vemos!","We zien elkaar!"),("Chao","Doei"),("Hasta pronto","Tot gauw"),
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
# person=blauw, werkwoord=oranje. Steeds: observeren (uit de scène) → compacte regel.
GRAM=r"""
<div class="note">
  <div class="note-h">🔎 <b>Fíjate</b> · Kijk terug naar de scène — je hoorde dit al:</div>
  <div class="obs">«¿Cómo <span class="v">estás</span>?» → «<span class="p">Yo</span> <span class="v">estoy</span> ocupad<u>a</u>.» · «<span class="v">estoy</span> cansad<u>a</u>, muy cansad<u>a</u>.» · «Buen<u>os</u> días · Buen<u>as</u> tardes · Buen<u>as</u> noches.»</div>
</div>

<div class="gcard">
  <h3><span class="v">estar</span> — <i>hoe je je voelt</i> (tijdelijke toestand)</h3>
  <p class="gp">Om te zeggen <b>hoe het gaat / hoe je je voelt</b>. Drie vormen volstaan nu:</p>
  <table class="gt">
    <tr><td class="p">yo</td><td class="v">estoy</td><td>ik ben / voel me</td><td class="ex">Yo <b>estoy</b> bien.</td></tr>
    <tr><td class="p">tú</td><td class="v">estás</td><td>jij bent / voelt je</td><td class="ex">¿Cómo <b>estás</b>?</td></tr>
    <tr><td class="p">él/ella/usted</td><td class="v">está</td><td>hij/zij is · u bent</td><td class="ex">¿Cómo <b>está</b> María?</td></tr>
  </table>
  <p class="ojo">⚠️ <b>¡Ojo!</b> <span class="es">Hoe je je <b>voelt</b> = <b>estar</b>: «Estoy bien / cansada».</span> Zeg <b>niet</b> «Soy bien». (<b>ser</b> = wie je bent, uit U1; <b>estar</b> = hoe je je nu voelt.)</p>
</div>

<div class="gcard">
  <h3>Buenos días / tardes / noches — <i>groeten volgens de klok</i></h3>
  <p class="gp">Welke groet je kiest, hangt af van het <b>moment van de dag</b>. In de scène: 09.00 · 16.00 · 21.05.</p>
  <div class="clock">
    <div class="cl-c cl-m"><span class="cl-ic">🌅</span><b>la mañana</b><span>~6–12 u</span><i>Buen<u>os</u> días</i></div>
    <div class="cl-c cl-t"><span class="cl-ic">☀️</span><b>la tarde</b><span>~12–20 u</span><i>Buen<u>as</u> tardes</i></div>
    <div class="cl-c cl-n"><span class="cl-ic">🌙</span><b>la noche</b><span>~20–6 u</span><i>Buen<u>as</u> noches</i></div>
  </div>
  <p class="ojo">💡 <span class="es">Let op de uitgang: buen<b>os</b> día<b>s</b> (♂) maar buen<b>as</b> tarde<b>s</b> / noche<b>s</b> (♀).</span> «Buenas noches» = <b>goedenavond</b> (bij aankomst) én <b>goodnight</b> (bij vertrek).</p>
</div>

<div class="gcard">
  <h3>-o / -a — <i>man of vrouw</i> (nu op de estados)</h3>
  <p class="gp">De toestand past zich aan aan man/vrouw — net als «encantad__» in U1:</p>
  <div class="mv">
    <div class="mv-c mv-m"><span class="mv-t">♂ un chico</span><span>Estoy cansad<b>o</b></span><span>ocupad<b>o</b> · nervios<b>o</b> · enferm<b>o</b></span></div>
    <div class="mv-c mv-f"><span class="mv-t">♀ una chica</span><span>Estoy cansad<b>a</b></span><span>ocupad<b>a</b> · nervios<b>a</b> · enferm<b>a</b></span></div>
  </div>
  <p class="ojo">💡 <span class="es">Josefina dice «estoy cansad<b>a</b>»; Julio dice «estoy enferm<b>o</b>».</span> Jij kiest naargelang <b>jouw</b> geslacht.</p>
</div>

<div class="gcard soft">
  <h3>tú <span class="v">↔</span> usted — <i>informeel of beleefd</i></h3>
  <p class="gp">Met vrienden/klasgenoten: <b>tú</b> → «¿Cómo <b>estás</b>?». Met een onbekende volwassene / formeel: <b>usted</b> → «¿Cómo <b>está</b> usted?». In de scène tutoyeren de collega's; met de directeur Fernando klinkt het beleefder. In de klas gebruiken we meestal <b>tú</b>.</p>
</div>
"""

# ── §5 TAREA FINAL — communicatief (afzender·ontvanger·doel·situatie·resultaat) ─
TAREA=r"""
<div class="tcard">
  <div class="tmeta">
    <span><b>👤 Wie</b> jij + een klasgenoot (paar)</span>
    <span><b>🎯 Doel</b> gepast groeten op 3 momenten & zeggen hoe het gaat</span>
    <span><b>🗣️ Hoe</b> mondeling, om de beurt, zonder blad af te lezen</span>
    <span><b>✅ Resultaat</b> 3 mini-diálogos gespeeld + je «diario» ingevuld</span>
  </div>
  <h3>Un día de saludos — <i>groet volgens het uur van de dag</i></h3>
  <ol class="pasos">
    <li><b>Elige la hora.</b> Kies per rondje een moment: 🌅 mañana · ☀️ tarde · 🌙 noche.</li>
    <li><b>Saluda + pregunta.</b> Groet gepast en vraag hoe het gaat:
        <div class="frame">«Buen__ ____, ¿qué tal? / ¿cómo estás?»</div></li>
    <li><b>Responde con estar.</b> Zeg hoe je je voelt (let op -o/-a):
        <div class="frame">«Estoy ____ (bien · cansad_ · ocupad_ · nervios_…). ¿Y tú?»</div></li>
    <li><b>Despídete.</b> Sluit af volgens het uur: «Hasta luego / Hasta mañana / Adiós.»</li>
  </ol>
  <div class="carne">
    <div class="carne-h">DIARIO DE SALUDOS · Academia «Bienvenidos al español»</div>
    <div class="carne-b diario">
      <div class="di-row"><span class="di-ic">🌅</span><div class="di-lines">
        <div><span>Saludo</span><i></i></div><div><span>Estoy…</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">☀️</span><div class="di-lines">
        <div><span>Saludo</span><i></i></div><div><span>Estoy…</span><i></i></div></div><span class="di-ok">☐</span></div>
      <div class="di-row"><span class="di-ic">🌙</span><div class="di-lines">
        <div><span>Saludo</span><i></i></div><div><span>Estoy…</span><i></i></div></div><span class="di-ok">☐</span></div>
    </div>
  </div>
  <p class="crit">🏁 <b>Klaar als…</b> je op elk moment de <b>juiste</b> groet kiest (días/tardes/noches), met <b>estar</b> zegt hoe je je voelt (juiste -o/-a), en netjes afscheid neemt — zónder af te lezen.</p>
</div>
"""

# ── §Suena bien · uitspraak (matrix A U2: jota /x/ + h muda + acentuación saludos) ──
# reservoir: DS-009 uitspraakpagina · SK-080 · SK-086 · SK-087 (discriminatie) · SK-088 (shadowing) · PPT-037/038
JOTA=[("Josefina","de secretaresse"),("jueves","donderdag"),("gente","mensen"),
 ("gimnasio","sportzaal"),("trabajo","werk"),("mujer","vrouw")]
HMUDA=[("hola","hallo"),("hasta","tot"),("hija","dochter"),("ahora","nu"),("hombre","man"),("hospital","ziekenhuis")]
DISCRIM=[("gente",1),("gato",0),("jueves",1),("guitarra",0),("gimnasio",1),("lago",0),("trabajo",1),("agua",0)]
ACENTO=[("Buenos días","Bue·nos <b>DÍ</b>·as"),("Buenas tardes","Bue·nas <b>TAR</b>·des"),("Buenas noches","Bue·nas <b>NO</b>·ches")]
def jcard(w,nl):
    return (f'<div class="cc" data-es="{w}"><span class="cc-es">{w}</span>'
            f'<span class="cc-nl">{nl}</span><button class="cc-spk">🔊</button></div>')
def dchip(w,ok): return f'<button class="dchip" data-ok="{ok}" data-w="{w}">🔊 {w}</button>'
def acchip(w,html): return f'<button class="shchip" data-w="{w}">🔊 {html}</button>'
SUENA=('<div class="suena">'
 '<div class="sblok"><h3>① La jota /x/ · de klank van j en g+e,i</h3>'
 '<p class="sh">De Spaanse <b>j</b> (en <b>g</b> vóór e/i) is een <b>keelklank</b> — zoals de NL «g» in «gaan», maar krachtiger. Klik 🔊 en spreek na.</p>'
 f'<div class="cc-grid tight">{"".join(jcard(*j) for j in JOTA)}</div>'
 '<p class="ojo2">⚠️ <b>¡Ojo!</b> <span>g + a/o/u = /g/ (<b>ga</b>to, <b>gu</b>sto) · maar g + e/i = /x/ (<b>ge</b>nte, <b>gi</b>mnasio) — net als de j.</span></p></div>'
 '<div class="sblok"><h3>② La h muda · de stille h</h3>'
 '<p class="sh">De <b>h</b> schrijf je wél, maar je <b>hoort</b> ze niet. «hola» klinkt als «ola».</p>'
 f'<div class="cc-grid tight">{"".join(jcard(*h) for h in HMUDA)}</div></div>'
 '<div class="sblok"><h3>③ ¿Jota o no? · teken wat je hoort</h3>'
 '<p class="sh">Klik de woorden met de <b>jota-klank</b> /x/ (groen = juist). Klik 🔊 om te horen.</p>'
 f'<div class="shrow">{"".join(dchip(*d) for d in DISCRIM)}</div>'
 '<p class="sfb" id="dfb"></p></div>'
 '<div class="sblok"><h3>④ El acento en los saludos · klemtoon</h3>'
 '<p class="sh">De <b>dikke</b> lettergreep klinkt het sterkst. Klik 🔊 en herhaal met dezelfde melodie (shadowing).</p>'
 f'<div class="shrow">{"".join(acchip(*a) for a in ACENTO)}</div></div>'
 '</div>')

CSS=FONTS+r"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--card:#fff;
--p:#2563EB;--v:#EA7317;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif}
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
.p{color:var(--p);font-weight:700}.v{color:var(--v);font-weight:700}
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
.clock{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:8px 0}
.cl-c{border-radius:12px;padding:12px;display:flex;flex-direction:column;gap:2px;text-align:center}
.cl-ic{font-size:26px}.cl-c b{font-family:var(--disp)}.cl-c span{font-size:12px;color:var(--mut)}
.cl-c i{font-family:var(--disp);font-weight:700;font-style:normal;color:var(--gd);font-size:15px;margin-top:4px}
.cl-m{background:#FEF3E2}.cl-t{background:#FFF7DC}.cl-n{background:#E7ECFB}
[data-theme=dark] .cl-m{background:#3a2c1a}[data-theme=dark] .cl-t{background:#3a341a}[data-theme=dark] .cl-n{background:#1c2440}
.mv{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:8px 0}
.mv-c{border-radius:12px;padding:12px;display:flex;flex-direction:column;gap:4px;font-family:var(--disp);font-size:16px}
.mv-c b{color:var(--gd)}.mv-t{font-size:13px;font-weight:800;margin-bottom:4px}
.mv-m{background:#E8F0FE;color:#1E40AF}.mv-f{background:#FCE7F0;color:#9D174D}
[data-theme=dark] .mv-m{background:#1b2740;color:#bcd0f5}[data-theme=dark] .mv-f{background:#3a1c2b;color:#f3b8d0}
/* §5 TAREA */
.tcard{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:14px 0}
.tcard h3{font-family:var(--disp);font-size:19px;margin:8px 0 10px}
.tmeta{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px;background:var(--gt);border-radius:12px;padding:12px;font-size:13px}
.pasos{margin:6px 0 12px;padding-left:22px}.pasos li{margin:8px 0}
.frame{border:1.5px dashed var(--g);border-radius:10px;padding:8px 12px;margin:6px 0;font-family:var(--disp);color:var(--gd);background:var(--gt)}
.carne{max-width:420px;border:2px solid var(--g);border-radius:14px;overflow:hidden;margin:14px 0}
.carne-h{background:var(--g);color:#fff;font-family:var(--disp);font-weight:700;font-size:12.5px;padding:6px 12px}
.diario{display:flex;flex-direction:column;padding:6px 12px 12px}
.di-row{display:flex;gap:12px;align-items:center;padding:10px 0;border-bottom:1px solid var(--line)}
.di-row:last-child{border-bottom:none}
.di-ic{font-size:26px;flex:none}
.di-lines{flex:1;display:flex;flex-direction:column;gap:10px}
.di-lines div{display:flex;gap:8px;align-items:baseline}.di-lines span{font-size:12px;color:var(--mut);width:52px}
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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U2 · Kit · Gramática · Tarea</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 2 · Saludos</h1><p>De <b>kit de supervivencia</b> (groeten + zeggen hoe je je voelt), een korte <b>uitlegnota</b> waar het helpt, en je <b>eindtaak</b>. Klik 🔊 om woorden te horen.</p></div>
<main>
 <h2 class="subh">🔊 Suena bien <small>uitspraak — de jota /x/, de stille h &amp; de klemtoon</small></h2>
 {SUENA}

 <h2 class="subh">§2 · Kit de supervivencia <small>de chunks per situatie — klik om te horen</small></h2>
 {KIT}

 <h2 class="subh">§4 · Gramática en la práctica <small>kort en functioneel — geen theorie om de theorie</small></h2>
 {GRAM}

 <h2 class="subh">§5 · Tarea final <small>jouw communicatieve opdracht</small></h2>
 {TAREA}

 <div class="foot">C4 · «Bienvenidos al español» · Unidad 2 · Saludos</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.cc').forEach(function(c){{var es=c.getAttribute('data-es').replace(/[…?¿!¡]/g,'');c.onclick=function(){{speak(es);}};}});
document.querySelectorAll('.shchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));}};}});
var dtot=document.querySelectorAll('.dchip[data-ok="1"]').length;
document.querySelectorAll('.dchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));var ok=b.getAttribute('data-ok')==='1';b.classList.remove('ok','no');b.classList.add(ok?'ok':'no');var n=document.querySelectorAll('.dchip.ok').length;var fb=document.getElementById('dfb');fb.textContent=ok?('¡Con jota! /x/ · '+n+'/'+dtot+' encontradas 👏'):'Esa no tiene jota — es /g/. Prueba otra.';}};}});
</script></body></html>"""
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U2_kgt.html","w").write(HTML)
print("C4_U2_kgt.html geschreven:",len(HTML),"bytes")
