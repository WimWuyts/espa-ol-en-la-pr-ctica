#!/usr/bin/env python3
# C4 · Unidad 1 — §2 KIT DE SUPERVIVENCIA (visueel chunk-netwerk) + §4 GRAMÁTICA EN LA
# PRÁCTICA (mini-nota, functioneel, GEEN kader) + §5 TAREA FINAL (communicatief).
# Español primero + NL-steun. C4-rood, TTS, standalone. Geen didactische kaders — wél uitlegnota's.
import base64, os
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

# ── §2 KIT · chunks per taalhandeling (functie → chunks: ES · NL) ──────────────
CLUSTERS=[
 ("Saludar","begroeten","👋",[
   ("¡Hola!","Hallo!"),("Buenos días","Goedemorgen"),("Buenas tardes","Goedemiddag"),
   ("Buenas noches","Goedenavond"),("¿Qué tal?","Hoe gaat het? (informeel)"),
   ("¿Cómo estás?","Hoe gaat het? (jij)"),("¿Cómo está usted?","Hoe gaat het met u?"),
 ]),
 ("Responder","antwoorden hoe het gaat","🙂",[
   ("Bien","Goed"),("Muy bien","Heel goed"),("Bien, ¿y tú?","Goed, en jij?"),
   ("Regular","Gaat wel"),("Todo bien","Alles goed"),
 ]),
 ("Presentarse","jezelf voorstellen","🪪",[
   ("Me llamo…","Ik heet…"),("Yo soy…","Ik ben…"),("Soy de…","Ik kom uit…"),
   ("Encantado","Aangenaam (man)"),("Encantada","Aangenaam (vrouw)"),
   ("Igualmente","Insgelijks"),
 ]),
 ("Preguntar","naar de ander vragen","❓",[
   ("¿Cómo te llamas?","Hoe heet je?"),("¿Y tú?","En jij?"),
   ("¿De dónde eres?","Waar kom je vandaan?"),("¿Cómo se llama usted?","Hoe heet u?"),
 ]),
 ("Cortesía","beleefdheid","🙏",[
   ("Por favor","Alsjeblieft (vragend)"),("Gracias","Dank je"),("Muchas gracias","Hartelijk dank"),
   ("De nada","Graag gedaan"),("Perdona","Sorry / pardon"),("Bienvenido/a","Welkom"),
 ]),
 ("Despedirse","afscheid nemen","👋",[
   ("Adiós","Dag / tot ziens"),("Hasta luego","Tot straks"),("Hasta mañana","Tot morgen"),
   ("Vale","Oké"),("¡Nos vemos!","We zien elkaar!"),
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
  <div class="note-h">🔎 <b>Fíjate</b> · vuelve a la escena: ya lo has oído. <span class="stn">je hoorde dit al</span></div>
  <div class="obs">«<span class="p">Yo</span> <span class="v">soy</span> Julio.» · «<span class="p">Me</span> <span class="v">llamo</span> María.» · «Encantad<u>o</u> / Encantad<u>a</u>.»</div>
</div>

<div class="gcard">
  <h3><span class="p">ser</span> — <i>quién eres</i> <span class="stn">zijn: wie je bent</span></h3>
  <p class="gp">Om te zeggen <b>wie</b> je bent. Drie vormen volstaan nu:</p>
  <table class="gt">
    <tr><td class="p">yo</td><td class="v">soy</td><td>ik ben</td><td class="ex">Yo <b>soy</b> Ana.</td></tr>
    <tr><td class="p">tú</td><td class="v">eres</td><td>jij bent</td><td class="ex">¿<b>Eres</b> Leo?</td></tr>
    <tr><td class="p">él/ella/usted</td><td class="v">es</td><td>hij/zij is · u bent</td><td class="ex">Ella <b>es</b> María.</td></tr>
  </table>
</div>

<div class="gcard">
  <h3><span class="p">llamarse</span> — <i>cómo te llamas</i> <span class="stn">heten</span></h3>
  <p class="gp">Fíjate en la palabrita de delante (<b>me / te / se</b>): cambia con la persona. <span class="stn">me/te/se verandert mee</span></p>
  <table class="gt">
    <tr><td class="p">(yo) me</td><td class="v">llamo</td><td>ik heet</td><td class="ex"><b>Me llamo</b> Sara.</td></tr>
    <tr><td class="p">(tú) te</td><td class="v">llamas</td><td>jij heet</td><td class="ex">¿Cómo <b>te llamas</b>?</td></tr>
    <tr><td class="p">(él/ella/ud.) se</td><td class="v">llama</td><td>hij/zij heet · u heet</td><td class="ex">¿Cómo <b>se llama</b> usted?</td></tr>
  </table>
  <p class="ojo">⚠️ <b>¡Ojo!</b> <span class="es">«Me llamo» = «Ik heet», letterlijk «ik noem mezelf».</span> Zeg <b>niet</b> «Yo soy me llamo».</p>
</div>

<div class="gcard">
  <h3>-o / -a — <i>man of vrouw</i></h3>
  <p class="gp">Muchas palabras cambian según ♂/♀. Ya lo oíste en <b>encantad__</b>: <span class="stn">de vorm past zich aan aan man/vrouw</span></p>
  <div class="mv">
    <div class="mv-c mv-m"><span class="mv-t">♂ chico</span><span>Encantad<b>o</b></span><span>bienvenid<b>o</b></span></div>
    <div class="mv-c mv-f"><span class="mv-t">♀ chica</span><span>Encantad<b>a</b></span><span>bienvenid<b>a</b></span></div>
  </div>
  <p class="ojo">💡 <span class="es">Un chico dice «encantad<b>o</b>»; una chica dice «encantad<b>a</b>».</span> Jij past dit toe naargelang <b>jouw</b> geslacht.</p>
</div>

<div class="gcard soft">
  <h3>tú <span class="v">↔</span> usted — <i>informeel of beleefd</i></h3>
  <p class="gp">Con amigos y compañeros: <b>tú</b> (¿Cómo estás? · ¿Cómo te llamas?). Con un adulto desconocido o en situación formal: <b>usted</b> (¿Cómo está usted? · ¿Cómo se llama usted?). En clase usamos casi siempre <b>tú</b>. <span class="stn">tú met leeftijdsgenoten, usted formeel</span></p>
</div>
"""

# ── §5 TAREA FINAL — communicatief (afzender·ontvanger·doel·situatie·resultaat) ─
TAREA=r"""
<div class="tcard">
  <div class="tmeta">
    <span><b>👤 Quién</b> tú (nuevo/a en la clase)</span>
    <span><b>🎯 Objetivo</b> presentarte y conocer a 3 compañeros</span>
    <span><b>🗣️ Cómo</b> oralmente, sin leer la hoja</span>
    <span><b>✅ Resultado</b> un «carné» relleno y 3 nombres anotados</span>
  </div>
  <h3>El carné de la clase — <i>haz tu carné y preséntate</i> <span class="stn">maak je klaskaartje en stel je voor</span></h3>
  <ol class="pasos">
    <li><b>Rellena tu carné.</b> Completa tu carné (nombre · de dónde eres · un emoji que te pega). <span class="stn">naam, herkomst, een emoji</span></li>
    <li><b>Preséntate.</b> Ponte de pie, saluda y di quién eres y de dónde eres: <span class="stn">sta recht, groet en stel je voor</span>
        <div class="frame">«¡Hola! Me llamo ____. Soy de ____. ¡Encantad_!»</div></li>
    <li><b>Pregunta.</b> Pregunta a 3 compañeros su nombre y su origen («¿Cómo te llamas? ¿De dónde eres?») y anótalos. <span class="stn">drie klasgenoten, en noteer</span></li>
    <li><b>Despídete.</b> Termina cada minidiálogo con «¡Encantad_! Hasta luego.» <span class="stn">sluit elk gesprekje af</span></li>
  </ol>
  <div class="carne">
    <div class="carne-h">CARNÉ · Academia «Bienvenidos al español»</div>
    <div class="carne-b">
      <div class="carne-foto">🙂</div>
      <div class="carne-lines">
        <div><span>Me llamo</span><i></i></div>
        <div><span>Soy de</span><i></i></div>
        <div><span>Mi emoji</span><i></i></div>
      </div>
    </div>
  </div>
  <table class="tab3">
    <tr><th>#</th><th>¿Cómo te llamas?</th><th>¿De dónde eres?</th></tr>
    <tr><td>1</td><td></td><td></td></tr>
    <tr><td>2</td><td></td><td></td></tr>
    <tr><td>3</td><td></td><td></td></tr>
  </table>
  <p class="crit">🏁 <b>Está listo cuando…</b> te presentas con soltura sin leer, usas la forma correcta (-o/-a) y has anotado 3 nombres. <span class="stn">vlot, met de juiste vorm, en 3 namen genoteerd</span></p>
</div>
"""

# ── §Suena bien · uitspraak (matrix A: klinkers a·e·i·o·u + sílaba tónica) ──────
# reservoir: DS-009 uitspraakpagina · SK-080 uitspraakkaart · SK-087 klankdiscriminatie · SK-088 shadowing
VOCALS=[("a","als in ‘bal’","casa · mañana"),("e","als in ‘bed’ (kort)","mesa · café"),
 ("i","als in ‘kiwi’","sí · Lucía"),("o","als in ‘pot’","hola · oso"),("u","als in ‘boek’","tú · uno")]
SHADOW=["Hola","Buenos días","Me llamo","Encantado","Muchas gracias"]
KLEM=[(["Ho","la"],0),(["me","lla","mo"],1),(["en","can","ta","do"],2),(["a","diós"],1),(["gra","cias"],0)]
def voccard(l,as_,ej):
    return (f'<div class="voc" data-w="{ej.split(" · ")[0]}"><span class="vl">{l}</span>'
            f'<span class="vas">{as_}</span><span class="vej">{ej}</span><button class="vspk">🔊</button></div>')
def shchip(w): return f'<button class="shchip" data-w="{w}">🔊 {w}</button>'
def klemword(i,syls,ton):
    chips="".join(f'<span class="syl" data-ok="{1 if j==ton else 0}">{s}</span>' for j,s in enumerate(syls))
    return f'<div class="klemword" data-w="{"".join(syls)}"><button class="kspk">🔊</button>{chips}</div>'
SUENA=('<div class="suena">'
 '<div class="sblok"><h3>① Las cinco vocales · de 5 klinkers</h3>'
 '<p class="sh">Las vocales españolas son <b>cortas y puras</b>: siempre el mismo sonido, nunca «arrastrado». Pulsa 🔊 y repite. <span class="gloss">klinkers zijn kort en zuiver</span></p>'
 f'<div class="vocgrid">{"".join(voccard(*v) for v in VOCALS)}</div>'
 '<p class="ojo2">⚠️ <b>¡Ojo!</b> <span>e blijft /e/ en o blijft /o/ — géén NL «ei/ou»-glijder. Denk: a·e·i·o·oe.</span></p></div>'
 '<div class="sblok"><h3>② Repite · spreek na (shadowing)</h3>'
 '<p class="sh">Escucha y repite enseguida: imita la melodía. <span class="gloss">herhaal meteen en imiteer de melodie</span></p>'
 f'<div class="shrow">{"".join(shchip(w) for w in SHADOW)}</div></div>'
 '<div class="sblok"><h3>③ ¿Dónde está el acento? <span class="stn">waar ligt de klemtoon?</span></h3>'
 '<p class="sh">Pulsa la sílaba que oyes más <b>fuerte</b>; pulsa 🔊 para comprobar. <span class="gloss">klik de sterkste lettergreep</span></p>'
 f'<div class="klemgrid">{"".join(klemword(i,*k) for i,k in enumerate(KLEM))}</div>'
 '<p class="sfb" id="sfb"></p></div></div>')

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
.carne{max-width:360px;border:2px solid var(--g);border-radius:14px;overflow:hidden;margin:14px 0}
.carne-h{background:var(--g);color:#fff;font-family:var(--disp);font-weight:700;font-size:12.5px;padding:6px 12px}
.carne-b{display:flex;gap:14px;padding:14px}
.carne-foto{width:70px;height:70px;border-radius:12px;background:var(--gt);display:flex;align-items:center;justify-content:center;font-size:34px;flex:none}
.carne-lines{flex:1;display:flex;flex-direction:column;justify-content:center;gap:12px}
.carne-lines div{display:flex;gap:8px;align-items:baseline}.carne-lines span{font-size:12px;color:var(--mut);width:60px}
.carne-lines i{flex:1;border-bottom:1.5px solid var(--line);height:16px}
.tab3{border-collapse:collapse;width:100%;margin:10px 0;font-size:14px}
.tab3 th{background:var(--gt);color:var(--gd);text-align:left;padding:8px 10px;font-family:var(--disp)}
.tab3 td{border:1px solid var(--line);padding:12px 10px;height:34px}.tab3 td:first-child{text-align:center;width:34px;color:var(--mut)}
.crit{background:var(--crema);border-radius:10px;padding:10px 14px;font-size:13.5px;margin-top:10px}
.tools{display:flex;gap:8px;margin:10px 0}
.btn{border:1.5px solid var(--line);background:var(--card);color:var(--ink);font-weight:700;border-radius:10px;padding:7px 13px;cursor:pointer;font-family:var(--disp);font-size:13px}
.btn.on{background:var(--g);color:#fff;border-color:var(--g)}
.foot{color:var(--mut);font-size:12px;text-align:center;margin:26px 0}
/* §Suena bien */
.suena{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:760px){.suena{grid-template-columns:1fr}}
.sblok{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 16px}
.suena .sblok:first-child{grid-row:span 2}
.sblok h3{font-family:var(--disp);color:var(--gd);margin:0 0 4px;font-size:16px}
.sh{color:var(--mut);font-size:12.5px;margin:0 0 10px}
.vocgrid{display:grid;grid-template-columns:1fr 1fr;gap:9px}
.voc{position:relative;border:1.5px solid var(--line);border-left:4px solid var(--g);border-radius:12px;padding:8px 34px 8px 12px;cursor:pointer}
.voc:hover{background:var(--gt)}
.vl{display:block;font-family:var(--disp);font-weight:800;font-size:22px;color:var(--gd);line-height:1.1}
.vas{display:block;font-size:11.5px;color:var(--mut)}.vej{display:block;font-size:13px;font-weight:600}
.vspk{position:absolute;right:8px;top:8px;border:none;background:transparent;cursor:pointer;font-size:14px;opacity:.55}
.ojo2{background:var(--gt);border-radius:10px;padding:8px 12px;font-size:12.5px;margin:10px 0 0}.ojo2 b{color:#DC2626}
.shrow{display:flex;flex-wrap:wrap;gap:8px}
.shchip{border:1.5px solid var(--line);background:var(--paper);border-radius:20px;padding:8px 14px;font-weight:700;font-size:14px;cursor:pointer;font-family:var(--disp);color:var(--ink)}
.shchip:hover{background:var(--gt);border-color:var(--g)}
.klemgrid{display:flex;flex-direction:column;gap:8px}
.klemword{display:flex;align-items:center;gap:4px}
.kspk{border:none;background:transparent;cursor:pointer;font-size:14px;opacity:.55;margin-right:2px}
.syl{border:1.5px solid var(--line);border-radius:8px;padding:5px 11px;font-family:var(--disp);font-weight:700;font-size:15px;cursor:pointer;user-select:none}
.syl:hover{background:var(--gt)}.syl.ok{background:var(--g);color:#fff;border-color:var(--g)}.syl.no{background:#fde8e8;border-color:#DC2626;color:#DC2626}
.sfb{font-size:13px;color:var(--gd);font-weight:600;min-height:18px;margin:8px 0 0}
"""

HTML=f"""<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U1 · Kit · Gramática · Tarea</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 1 · Presentaciones</h1><p>El <b>kit de supervivencia</b> (la lengua que de verdad necesitas), una <b>nota breve</b> donde ayuda, y tu <b>tarea final</b>. Pulsa 🔊 para oír las palabras. <span class="stn">de taal die je nodig hebt, kort uitgelegd, plus je eindtaak</span></p></div>
<main>
 <h2 class="subh">🔊 Suena bien <small>pronunciación — las 5 vocales y el acento</small></h2>
 {SUENA}

 <h2 class="subh">§2 · Kit de supervivencia <small>los chunks por situación — pulsa para oírlos</small></h2>
 {KIT}

 <h2 class="subh">§4 · Gramática en la práctica <small>kort en functioneel — geen theorie om de theorie</small></h2>
 {GRAM}

 <h2 class="subh">§5 · Tarea final <small>jouw communicatieve opdracht</small></h2>
 {TAREA}

 <div class="foot">C4 · «Bienvenidos al español» · Unidad 1 · Presentaciones</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.cc').forEach(function(c){{var es=c.getAttribute('data-es').replace(/[…?¿!¡]/g,'');c.onclick=function(){{speak(es);}};}});
document.querySelectorAll('.voc').forEach(function(v){{v.onclick=function(){{speak(v.getAttribute('data-w'));}};}});
document.querySelectorAll('.shchip').forEach(function(b){{b.onclick=function(){{speak(b.getAttribute('data-w'));}};}});
document.querySelectorAll('.kspk').forEach(function(b){{b.onclick=function(){{speak(b.parentNode.getAttribute('data-w'));}};}});
document.querySelectorAll('.klemword .syl').forEach(function(s){{s.onclick=function(){{var ok=s.getAttribute('data-ok')==='1';var sib=s.parentNode.querySelectorAll('.syl');sib.forEach(function(x){{x.classList.remove('ok','no');}});s.classList.add(ok?'ok':'no');var fb=document.getElementById('sfb');fb.textContent=ok?'¡Muy bien! Dat is de tónica. 👏':'Bijna — probeer een andere lettergreep.';}};}});
</script></body></html>"""
os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U1_kgt.html","w").write(HTML)
print("C4_U1_kgt.html geschreven:",len(HTML),"bytes")
