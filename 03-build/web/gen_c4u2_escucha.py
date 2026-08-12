#!/usr/bin/env python3
# C4 · Unidad 2 — «Escucha»-blok: Sitcom-video 2 (Saludos y despedidas) ingebed + interactief meelees-transcript
# (ES + NL-toggle, klik-om-te-horen, chunks gemarkeerd). Zelfde patroon/pijplijn als U1.
import base64, os, json, re
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

# videobron: ("youtube", id) of ("drive", id). U2 → YouTube: «Episodio 2 · Saludos» (Spanish Sitcom, Habla con Eñe / Hablamétodo).
# Door de auteur aangeleverd. YouTube = geen deelrechten nodig, werkt voor iedereen.
VIDEO_SRC=("youtube","2E51CKpanmU")
ALLOW="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen; web-share"
def video_iframe(src):
    kind,vid=src
    if kind=="youtube":
        return (f'<iframe src="https://www.youtube-nocookie.com/embed/{vid}?rel=0&playsinline=1" '
                f'title="Sitcom · Episodio 2" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" '
                f'allow="{ALLOW}" allowfullscreen></iframe>')
    return f'<iframe src="https://drive.google.com/file/d/{vid}/preview" allow="{ALLOW}" allowfullscreen></iframe>'
IFRAME=video_iframe(VIDEO_SRC)
# rechtstreekse fallback-link (werkt ook wanneer de embed genest in de hub zit)
YT_WATCH="https://www.youtube.com/watch?v="+VIDEO_SRC[1] if VIDEO_SRC[0]=="youtube" else "https://drive.google.com/file/d/"+VIDEO_SRC[1]+"/view"
# hoogfrequente chunks om te markeren (survival — focus U2: saludos/despedidas per moment van de dag + estar + estado)
CHUNKS=["Buenos días","Buenas tardes","Buenas noches","¿Cómo estás?","¿Cómo está","Bien, bien","Bien","Muy ocupada","ocupada","Un poco nerviosa","nerviosa","está enfermo","estoy enferma","enferma","muy cansada","cansada","Demasiado","muy cansado","Hasta luego","Adiós","la verdad","pues nada"]
# ── TRANSCRIPT = exact aangeleverd door de auteur (Episodio 2 · Saludos). 3 scènes op 09.00 / 16.00 / 21.05 u.
SCENES=[
 ("Escena 1 · Por la mañana (09.00 h)","Julio entra y saluda a Josefina; quiere presentarle a María, pero Josefina está ocupada.",[
  ("Julio","Josefina… Buenos días.","Josefina… Goedemorgen."),
  ("Josefina","Buenos días.","Goedemorgen."),
  ("Julio","Yo es que…","Ik… het zit zo…"),
  ("Josefina","¿Cómo estás?","Hoe gaat het?"),
  ("Julio","Bien, bien. Pero es María, la nueva profesora.","Goed, goed. Maar het gaat om María, de nieuwe lerares."),
  ("Josefina","Yo estoy ocupada.","Ik heb het druk."),
  ("Julio","Ya. ¿Muy ocupada?","Juist. Heel druk?"),
  ("Josefina","Muy ocupada.","Heel druk."),
 ]),
 ("Escena 2 · Por la tarde (16.00 h)","Por la tarde María habla con Josefina; resulta que todo el mundo está «un poco» algo.",[
  ("María","Josefina.","Josefina."),
  ("Josefina","Buenas tardes.","Goedemiddag."),
  ("María","Buenas tardes. Josefina, Julio es…","Goedemiddag. Josefina, Julio is…"),
  ("Josefina","¿Cómo estás?","Hoe gaat het?"),
  ("María","Un poco nerviosa, la verdad. Julio está mal, está enfermo.","Een beetje nerveus, eerlijk gezegd. Julio is niet lekker, hij is ziek."),
  ("Josefina","Yo estoy enferma. Un poco enferma.","Ik ben ziek. Een beetje ziek."),
  ("María","Ya. Bueno. Bueno, pues nada. Hasta luego. Adiós.","Juist. Goed. Wel, niets aan te doen. Tot straks. Dag."),
  ("Josefina","Adiós.","Dag."),
 ]),
 ("Escena 3 · Por la noche (21.05 h)","Por la noche el director Fernando pregunta cómo está cada uno; Josefina está agotada.",[
  ("Fernando","Qué.","Zeg."),
  ("Josefina","Ay… buenas noches.","Ay… goedenavond."),
  ("Fernando","¿Cómo está María? Y cómo está Julio.","Hoe gaat het met María? En hoe gaat het met Julio."),
  ("Fernando","Y tú, ¿cómo estás?","En jij, hoe gaat het met jou?"),
  ("Josefina","Uf, cansada, muy cansada.","Oef, moe, heel moe."),
  ("Fernando","¿Mucho trabajo?","Veel werk?"),
  ("Josefina","Demasiado. Todos con problemas. Es muy cansado.","Te veel. Iedereen met problemen. Het is heel vermoeiend."),
 ]),
]

def mark(es):
    # markeer chunks overlap-veilig: langste eerst; reeds gemarkeerde stukken worden als placeholder
    # beschermd zodat een kortere chunk niet binnen een langere hermarkeert (bv. «¿Cómo está» in «¿Cómo estás?»).
    ph=[]; out=es
    def grab(m):
        ph.append(m.group(1)); return "\x00%d\x00"%(len(ph)-1)
    for c in sorted(CHUNKS,key=len,reverse=True):
        out=re.sub("("+re.escape(c)+")", grab, out, count=1, flags=re.IGNORECASE)
    return re.sub("\x00(\\d+)\x00", lambda m:'<span class="ch">'+ph[int(m.group(1))]+'</span>', out)

COL={"María":"#D64550","Julio":"#2563EB","Fernando":"#7C4DE0","Josefina":"#0E9E97"}
def line(sp,es,nl):
    c=COL.get(sp,"#A8323B")
    return (f'<div class="ln" data-es="{es.replace(chr(34),"&quot;")}"><span class="who" style="background:{c}22;color:{c}">{sp}</span>'
      f'<span class="es">{mark(es)}</span><span class="nl">{nl}</span><button class="spk" title="luister">🔊</button></div>')

def scene(title,intro,lines):
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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 2 · Escucha</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 2 · Saludos — ¡Escucha!</h1><p>Mira la escena y <b>lee al mismo tiempo</b>. Pulsa una frase para oírla; activa o desactiva el neerlandés. Las palabras en <span style="background:#FEF08A;color:#20242E;border-radius:4px;padding:0 4px">amarillo</span> son los chunks útiles. <span class="stn">lees mee; de gele woorden zijn de chunks</span></p></div>
<main>
 <div class="grid">
  <div class="vid">
    <div class="vidbox">{IFRAME}</div>
    <div class="toolbar">
      <button class="btn" id="tgnl">🇳🇱 Neerlandés ON</button>
      <a class="btn" href="{YT_WATCH}" target="_blank" rel="noopener">▶ Op YouTube</a>
      <span class="legend">💡 <span class="ch">geel</span> = chunk om mee te nemen</span>
    </div>
    <p class="vidhint">¿No se reproduce el vídeo? Pulsa <a href="{YT_WATCH}" target="_blank" rel="noopener">aquí para abrirlo en YouTube</a>.</p>
  </div>
  <div class="tr">{BODY}</div>
 </div>
 <div class="foot">C4 · «Bienvenidos al español» · Unidad 2 · Saludos</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.ln').forEach(function(l){{var b=l.querySelector('.spk');var es=l.getAttribute('data-es');b.onclick=function(){{speak(es);}};l.addEventListener('click',function(e){{if(e.target!==b)speak(es);}});}});
var nlon=false;document.getElementById('tgnl').onclick=function(){{nlon=!nlon;document.body.classList.toggle('shownl',nlon);this.classList.toggle('on',nlon);this.textContent=nlon?'🇳🇱 Neerlandés OFF':'🇳🇱 Neerlandés ON';}};
</script></body></html>"""
os.makedirs(f"{ROOT}/01-cursussen/04-welcome/U2",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U2_escucha.html","w").write(HTML)
print("C4_U2_escucha.html geschreven:",len(HTML),"bytes")
