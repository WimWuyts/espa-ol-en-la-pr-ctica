#!/usr/bin/env python3
# C4 · Unidad 9 — «Escucha»-blok: Sitcom-video 9 (Planes y obligaciones) + interactief meelees-transcript.
# BRON = GOOGLE DRIVE (zoals U8): «Spanish Sitcom 9_1080p.mp4»
#   file-id 1YlBRdAs4L4fOvmXylmQLlRSJMoRto7Kb · deelrechten gecontroleerd (role=reader / type=anyone).
import base64, os, json, re
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

VIDEO_SRC=("drive","1YlBRdAs4L4fOvmXylmQLlRSJMoRto7Kb")   # «9. Planes y obligaciones» — Drive
ALLOW="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen; web-share"
def video_iframe(src):
    kind,vid=src
    if kind=="youtube":
        return (f'<iframe src="https://www.youtube-nocookie.com/embed/{vid}?rel=0&playsinline=1" '
                f'title="Sitcom · Episodio 9" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" '
                f'allow="{ALLOW}" allowfullscreen></iframe>')
    return (f'<iframe src="https://drive.google.com/file/d/{vid}/preview" title="Sitcom · Episodio 9" '
            f'loading="lazy" allow="{ALLOW}" allowfullscreen></iframe>')
IFRAME=video_iframe(VIDEO_SRC)
WATCH=("https://www.youtube.com/watch?v="+VIDEO_SRC[1]) if VIDEO_SRC[0]=="youtube" else ("https://drive.google.com/file/d/"+VIDEO_SRC[1]+"/view")
WATCH_LABEL="▶ Op YouTube" if VIDEO_SRC[0]=="youtube" else "▶ Openen in Drive"
CHUNKS=["Voy a preparar café","¿Quieres desayunar?","no tengo mucha hambre","Tengo sueño","¿No tienes sueño?","Vamos a dormir","Tengo cosas que hacer","¿quedamos para ir al cine?","no puedo","Tengo que pasear al perro","¿Vamos a pasear","tengo que lavarme el pelo","¿Tienes que hacer algo?","voy a quedar con unas amigas","Tengo que trabajar","tengo que dormir","voy a dar unas clases","el próximo fin de semana","esta noche","esta tarde","Mañana es domingo","Hasta luego"]
SCENES=[
 ("Escena 1 · Un sábado por la mañana","Julio wil plannen maken; María heeft… «cosas que hacer». Let op elk **plan** (voy a) en elke **verplichting** (tengo que).",[
  ("María","Buenos días.","Goeiemorgen."),
  ("Julio","Buenos días. Voy a preparar café. ¿Quieres desayunar?","Goeiemorgen. Ik ga koffie zetten. Wil je ontbijten?"),
  ("María","Ah… no tengo mucha hambre.","Ah… ik heb niet veel honger."),
  ("Julio","Pero es sábado. Tengo sueño. ¿No tienes sueño? Vamos a dormir un poquito más.","Maar het is zaterdag. Ik ben slaperig. Ben jij niet slaperig? Laten we nog een beetje slapen."),
  ("María","Tengo cosas que hacer.","Ik heb dingen te doen."),
 ]),
 ("Escena 2 · «Tengo que…» (excuus na excuus)","Elke uitnodiging van Julio botst op een verplichting van María.",[
  ("Julio","Y esta noche, ¿quedamos para ir al cine?","En vanavond, spreken we af om naar de cinema te gaan?"),
  ("María","Eh… no puedo. Tengo que pasear al perro de mi madre.","Eh… ik kan niet. Ik moet de hond van mijn moeder uitlaten."),
  ("Julio","¿Y esta tarde? ¿Vamos a pasear, a comprar cosas?","En vanmiddag? Gaan we wandelen, dingen kopen?"),
  ("María","Mmm…, tengo que lavarme el pelo.","Mmm… ik moet mijn haar wassen."),
  ("Julio","Entiendo, es importante tener el pelo limpio para pasear al perro. ¿Y mañana?","Ik begrijp het, schoon haar is belangrijk om de hond uit te laten. En morgen?"),
  ("María","Mañana es domingo.","Morgen is het zondag."),
  ("Julio","¿Tienes que hacer algo?","Moet je iets doen?"),
  ("María","El domingo voy a quedar con unas amigas.","Zondag ga ik afspreken met wat vriendinnen."),
 ]),
 ("Escena 3 · ¿Y la semana? ¿Y el próximo finde?","Julio blijft proberen — tot en met «la India en globo».",[
  ("Julio","¿El lunes, el martes, el miércoles?","Maandag, dinsdag, woensdag?"),
  ("María","Tengo que trabajar.","Ik moet werken."),
  ("Julio","¿Por las noches?","'s Avonds?"),
  ("María","Por las noches tengo que dormir.","'s Avonds moet ik slapen."),
  ("Julio","El jueves voy a dar unas clases de baile flamenco.","Donderdag ga ik flamencolessen geven."),
  ("María","Ah…, no.","Ah… nee."),
  ("Julio","El próximo fin de semana. ¿Tienes que ir a la India en globo?","Volgend weekend. Moet je met een luchtballon naar India?"),
  ("María","No, el próximo fin de semana estoy aquí, pero tengo cosas que hacer.","Nee, volgend weekend ben ik hier, maar ik heb dingen te doen."),
  ("Julio","¿Qué cosas?","Welke dingen?"),
  ("María","Cosas. Adiós.","Dingen. Dag."),
  ("Julio","Hasta luego.","Tot later."),
 ]),
]
def mark(es):
    ph=[]; out=es
    def grab(m):
        ph.append(m.group(1)); return "\x00%d\x00"%(len(ph)-1)
    for c in sorted(CHUNKS,key=len,reverse=True):
        out=re.sub("("+re.escape(c)+")", grab, out, count=1, flags=re.IGNORECASE)
    return re.sub("\x00(\\d+)\x00", lambda m:'<span class="ch">'+ph[int(m.group(1))]+'</span>', out)
COL={"Julio":"#2563EB","María":"#D64550"}
def line(sp,es,nl):
    c=COL.get(sp,"#A8323B")
    return (f'<div class="ln" data-es="{es.replace(chr(34),"&quot;")}"><span class="who" style="background:{c}22;color:{c}">{sp}</span>'
      f'<span class="es">{mark(es)}</span><span class="nl">{nl}</span><button class="spk" title="luister">🔊</button></div>')
def scene(title,intro,lines):
    intro=intro.replace("**","")
    return (f'<div class="scene"><h3>{title}</h3><p class="si">{intro}</p>'+"".join(line(*l) for l in lines)+'</div>')

CSS=FONTS+"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--card:#fff;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#181513;--crema:#241C1B;--gt:#3A1E20;--line:#3a302e;--card:#211a19}
*{box-sizing:border-box}body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
.top{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;padding:20px 22px}
.top h1{font-family:var(--disp);font-weight:800;margin:0;font-size:24px}.top p{margin:4px 0 0;opacity:.95}
main{max-width:1080px;margin:0 auto;padding:18px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}@media(max-width:820px){.grid{grid-template-columns:1fr}}
.vid{position:sticky;top:12px;align-self:start}
.vidbox{position:relative;padding-top:56.25%;border-radius:14px;overflow:hidden;border:1px solid var(--line);background:#000}
.vidbox iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.toolbar{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:12px 0}
.btn{border:1.5px solid var(--line);background:var(--card);color:var(--ink);font-weight:700;border-radius:10px;padding:8px 13px;cursor:pointer;font-size:13px;font-family:var(--disp)}
.btn.on{background:var(--g);color:#fff;border-color:var(--g)}
a.btn{text-decoration:none;display:inline-flex;align-items:center;gap:5px}
.vidhint{font-size:12px;color:var(--mut);margin:8px 0 0}.vidhint a{color:var(--gd);font-weight:600}
.legend{font-size:12px;color:var(--mut)}.legend .ch{background:#FEF08A;border-radius:4px;padding:1px 5px}
.scene{margin:0 0 16px}.scene h3{font-family:var(--disp);color:var(--gd);margin:14px 0 2px;font-size:17px}.scene .si{color:var(--mut);font-size:13px;margin:0 0 8px}
.ln{display:flex;gap:8px;align-items:baseline;padding:6px 8px;border-radius:10px;flex-wrap:wrap}
.ln:hover{background:var(--gt)}
.who{font-family:var(--disp);font-weight:700;font-size:12px;border-radius:20px;padding:2px 9px;flex:none}
.es{font-size:15.5px;font-weight:500}.es .ch{background:#FEF08A;border-radius:4px;padding:1px 4px}
[data-theme=dark] .es .ch{color:#20242E}
.nl{display:none;color:var(--mut);font-style:italic;font-size:13.5px;width:100%;margin-left:44px}
body.shownl .nl{display:block}
.spk{border:none;background:transparent;cursor:pointer;font-size:14px;opacity:.5;margin-left:auto}
.foot{color:var(--mut);font-size:12px;text-align:center;margin:24px 0}
"""
BODY="".join(scene(*s) for s in SCENES)
HTML=f"""<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 9 · Escucha</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 9 · Planes y obligaciones — ¡Escucha!</h1><p>Bekijk de scène en <b>lees mee</b>. Klik een zin om ze te horen; zet Nederlands aan/uit. De <span style="background:#FEF08A;color:#20242E;border-radius:4px;padding:0 4px">gele</span> woorden zijn chunks: let op <b>voy a…</b> (plan) en <b>tengo que…</b> (moeten).</p></div>
<main>
 <div class="grid">
  <div class="vid">
    <div class="vidbox">{IFRAME}</div>
    <div class="toolbar">
      <button class="btn" id="tgnl">🇳🇱 Neerlandés ON</button>
      <a class="btn" href="{WATCH}" target="_blank" rel="noopener">{WATCH_LABEL}</a>
      <span class="legend">💡 <span class="ch">geel</span> = chunk om mee te nemen</span>
    </div>
    <p class="vidhint">Speelt de video niet af? Klik <a href="{WATCH}" target="_blank" rel="noopener">hier om ze in een nieuw tabblad te openen</a>.</p>
  </div>
  <div class="tr">{BODY}</div>
 </div>
 <div class="foot">C4 · «Bienvenidos al español» · Unidad 9 · Planes y obligaciones</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.ln').forEach(function(l){{var b=l.querySelector('.spk');var es=l.getAttribute('data-es');b.onclick=function(){{speak(es);}};l.addEventListener('click',function(e){{if(e.target!==b)speak(es);}});}});
var nlon=false;document.getElementById('tgnl').onclick=function(){{nlon=!nlon;document.body.classList.toggle('shownl',nlon);this.classList.toggle('on',nlon);this.textContent=nlon?'🇳🇱 Neerlandés OFF':'🇳🇱 Neerlandés ON';}};
</script></body></html>"""
os.makedirs(f"{ROOT}/01-cursussen/04-welcome/U9",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U9_escucha.html","w").write(HTML)
print("C4_U9_escucha.html geschreven:",len(HTML),"bytes · bron:",VIDEO_SRC[0],VIDEO_SRC[1])
