#!/usr/bin/env python3
# C4 · Unidad 11 — «Escucha»-blok: Sitcom-video 11 (Aquí hace demasiado calor) + meelees-transcript.
# BRON = GOOGLE DRIVE (zoals U8-U11): «Spanish Sitcom 11_1080p.mp4»
#   file-id 1saLd6_-eTVUTVbv1v8KbKwfYp3Ale6-D · deelrechten gecontroleerd (role=reader / type=anyone).
# NB: in het bronscript waren de sprekerlabels van escena 1 deels verwisseld (bijna alles stond op
# «Julio»). De beurten zijn hier gereconstrueerd tot een coherente drieluik-scène (Julio · camarero ·
# clienta) op basis van de inhoud; zie de docentnotitie in de PPT.
import base64, os, json, re
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

VIDEO_SRC=("drive","1saLd6_-eTVUTVbv1v8KbKwfYp3Ale6-D")   # «11. Aquí hace demasiado calor» — Drive
ALLOW="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen; web-share"
def video_iframe(src):
    kind,vid=src
    if kind=="youtube":
        return (f'<iframe src="https://www.youtube-nocookie.com/embed/{vid}?rel=0&playsinline=1" '
                f'title="Sitcom · Episodio 11" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" '
                f'allow="{ALLOW}" allowfullscreen></iframe>')
    return (f'<iframe src="https://drive.google.com/file/d/{vid}/preview" title="Sitcom · Episodio 11" '
            f'loading="lazy" allow="{ALLOW}" allowfullscreen></iframe>')
IFRAME=video_iframe(VIDEO_SRC)
WATCH=("https://www.youtube.com/watch?v="+VIDEO_SRC[1]) if VIDEO_SRC[0]=="youtube" else ("https://drive.google.com/file/d/"+VIDEO_SRC[1]+"/view")
WATCH_LABEL="▶ Op YouTube" if VIDEO_SRC[0]=="youtube" else "▶ Openen in Drive"
CHUNKS=["se va de vacaciones","a la playa","Siempre hace buen tiempo","Viaja con unos amigos","Son cuatro cincuenta","voy al pueblo de mis padres","Está cerca de Madrid","hace un frío","Nunca hace ese frío","puedes estar con tu familia","las fiestas de Navidad","con los tuyos","tus tíos","tus cuñados","A veces te cansas","la familia es para siempre","te quedas en Madrid","voy todos los años","me gusta hacer submarinismo","también le gusta","Yo voy mucho al cine","Me gusta el cine","me gusta la ópera","Casi nunca voy","los deportes","Voy al gimnasio","tres veces por semana","Hago yoga","¿Te gusta el yoga?","hace mucho viento","En invierno hace frío","En verano","en cambio","hace calor","me gusta más el frío","En mi casa hace calor"]
SCENES=[
 ("Escena 1 · En el bar","Julio neemt iets in een bar en praat met de camarero over de vakantie. Een clienta luistert mee… en heeft interesse. Let op elk **hace + weer**, elk **me gusta** en elk **frecuencia**-woord.",[
  ("Camarero","Ella se va de vacaciones a la playa, a Canarias. Siempre hace buen tiempo en Canarias.","Zij gaat op vakantie naar het strand, naar de Canarische Eilanden. Daar is het altijd mooi weer."),
  ("Camarero","Viaja con unos amigos; con un amigo, un inglés.","Ze reist met wat vrienden; met één vriend, een Engelsman."),
  ("Camarero","Son cuatro cincuenta.","Dat is vier vijftig."),
  ("Julio","Yo no, yo voy al pueblo de mis padres, Cabezas de Bonilla, en Ávila. Está cerca de Madrid.","Ik niet, ik ga naar het dorp van mijn ouders, Cabezas de Bonilla, in Ávila. Dat ligt dicht bij Madrid."),
  ("Camarero","Es bonito, Ávila.","Ávila is mooi."),
  ("Julio","Pero hace un frío… Nunca hace ese frío en Madrid.","Maar het is er zó koud… Zo koud is het nooit in Madrid."),
  ("Camarero","Lo bueno es que, por lo menos, puedes estar con tu familia.","Het goede is dat je tenminste bij je familie kunt zijn."),
  ("Camarero","Pasas las fiestas de Navidad con los tuyos: con tus padres, tus tíos, tus hermanos…","Je viert Kerstmis met de jouwen: met je ouders, je tantes en nonkels, je broers en zussen…"),
  ("Camarero","Tus cuñados.","Je schoonbroers en schoonzussen."),
  ("Julio","Exacto. A veces te cansas de restaurantes y playas y hoteles. En cambio, la familia…","Precies. Soms word je moe van restaurants en stranden en hotels. De familie daarentegen…"),
  ("Camarero","¿Qué?","Wat?"),
  ("Julio","No, digo que la familia es para siempre.","Nee, ik zeg dat familie voor altijd is."),
  ("Julio","¿Y tú te quedas en Madrid?","En jij, blijf jij in Madrid?"),
  ("Camarero","Yo voy todos los años al Caribe.","Ik ga elk jaar naar de Caraïben."),
  ("Julio","¿Y la familia?","En de familie?"),
  ("Camarero","Es que me gusta hacer submarinismo.","Ik hou nu eenmaal van duiken."),
  ("Camarero","A ella también le gusta hacer submarinismo. ¿Por qué no lo intentas?","Zij houdt óók van duiken. Waarom probeer je het niet?"),
  ("Julio","Bueno, es que en Ávila es difícil, ¿sabes? Yo voy mucho al cine.","Tja, in Ávila is dat moeilijk, weet je. Ik ga veel naar de cinema."),
  ("Clienta","Me gusta el cine y me gusta la ópera.","Ik hou van film en ik hou van opera."),
  ("Julio","Casi nunca voy a la ópera.","Ik ga bijna nooit naar de opera."),
  ("Clienta","Y los deportes. Voy al gimnasio tres veces por semana. Hago yoga.","En sport. Ik ga drie keer per week naar de sportzaal. Ik doe yoga."),
  ("Julio","¡Qué bien!","Wat goed!"),
  ("Clienta","¿Te gusta el yoga? Soy muy flexible.","Hou jij van yoga? Ik ben heel soepel."),
  ("Julio","Ya veo, ya.","Dat zie ik, ja."),
 ]),
 ("Escena 2 · En la calle","Julio en de clienta stappen buiten. Het weer is het gespreksonderwerp — en de clienta heeft een plan.",[
  ("Clienta","¡Uh, hace mucho viento!","Oei, het waait hard!"),
  ("Julio","Sí.","Ja."),
  ("Clienta","En invierno hace frío.","In de winter is het koud."),
  ("Julio","Y viento.","En het waait."),
  ("Clienta","Sí. En verano, en cambio, hace calor.","Ja. In de zomer daarentegen is het warm."),
  ("Julio","A mí me gusta más el frío.","Ik hou meer van de kou."),
  ("Clienta","¿Sí?","Echt?"),
  ("Julio","Sí.","Ja."),
  ("Clienta","En mi casa hace calor.","Bij mij thuis is het warm."),
  ("Julio","Je, je… ¿Eh?","Eh… hè?"),
 ]),
]
def mark(es):
    ph=[]; out=es
    def grab(m):
        ph.append(m.group(1)); return "\x00%d\x00"%(len(ph)-1)
    for c in sorted(CHUNKS,key=len,reverse=True):
        out=re.sub("("+re.escape(c)+")", grab, out, count=1, flags=re.IGNORECASE)
    return re.sub("\x00(\\d+)\x00", lambda m:'<span class="ch">'+ph[int(m.group(1))]+'</span>', out)
COL={"Julio":"#2563EB","Camarero":"#1E9E74","Clienta":"#7C3AED"}
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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 11 · Escucha</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 11 · Aquí hace demasiado calor — ¡Escucha!</h1><p>Bekijk de scène en <b>lees mee</b>. Klik een zin om ze te horen; zet Nederlands aan/uit. De <span style="background:#FEF08A;color:#20242E;border-radius:4px;padding:0 4px">gele</span> woorden zijn chunks: let op <b>hace + weer</b>, <b>me gusta…</b> en <b>siempre · nunca · a veces</b>.</p></div>
<main>
 <div class="grid">
  <div class="vid">
    <div class="vidbox">{IFRAME}</div>
    <div class="toolbar">
      <button class="btn" id="tgnl">🇳🇱 Nederlands aan</button>
      <a class="btn" href="{WATCH}" target="_blank" rel="noopener">{WATCH_LABEL}</a>
      <span class="legend">💡 <span class="ch">geel</span> = chunk om mee te nemen</span>
    </div>
    <p class="vidhint">Speelt de video niet af? Klik <a href="{WATCH}" target="_blank" rel="noopener">hier om ze in een nieuw tabblad te openen</a>.</p>
  </div>
  <div class="tr">{BODY}</div>
 </div>
 <div class="foot">C4 · «Welcome to Spanish» · Unidad 11 · El tiempo y los gustos</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.ln').forEach(function(l){{var b=l.querySelector('.spk');var es=l.getAttribute('data-es');b.onclick=function(){{speak(es);}};l.addEventListener('click',function(e){{if(e.target!==b)speak(es);}});}});
var nlon=false;document.getElementById('tgnl').onclick=function(){{nlon=!nlon;document.body.classList.toggle('shownl',nlon);this.classList.toggle('on',nlon);this.textContent=nlon?'🇳🇱 Nederlands uit':'🇳🇱 Nederlands aan';}};
</script></body></html>"""
os.makedirs(f"{ROOT}/01-cursussen/04-welcome/U11",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U11_escucha.html","w").write(HTML)
print("C4_U11_escucha.html geschreven:",len(HTML),"bytes · bron:",VIDEO_SRC[0],VIDEO_SRC[1])
