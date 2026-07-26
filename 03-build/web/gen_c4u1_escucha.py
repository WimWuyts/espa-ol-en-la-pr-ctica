#!/usr/bin/env python3
# C4 · Unidad 1 — «Escucha»-blok: Drive-video (Sitcom 1) ingebed + interactief meelees-transcript
# (ES + NL-toggle, klik-om-te-horen, chunks gemarkeerd). Vervangt «ondertitels in de video».
import base64, os, json, re
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

VIDEO_ID="1weD712f-pk6ovkynMzIHrfiuzzeg9Rj6"  # Spanish Sitcom 1 = Unidad 1
# hoogfrequente chunks om te markeren (survival)
CHUNKS=["Hola","¿Cómo estás?","Bien","encantada","Encantado","Encantado de conocerla","¿Cómo te llamas?","me llamo","Yo soy","soy","hasta luego","Adiós","Vale","¿Cómo está usted?","Igualmente","muy bien","¿Qué tal","Sí, claro","muchas gracias","De nada","Bienvenida","Perdona"]
SCENES=[
 ("Escena 1 · Julio y María se despiertan","Julio en María worden wakker en moeten zich haasten naar hun werk.",[
  ("María","Hola.","Hallo."),("Julio","Hola.","Hallo."),
  ("María","¿Cómo estás?","Hoe gaat het?"),("Julio","Bien.","Goed."),
  ("María","Bueno, encantada. ¿Cómo te llamas?","Wel, aangenaam. Hoe heet je?"),
  ("Julio","Yo soy Julio.","Ik ben Julio."),("María","Yo me llamo María.","Ik heet María."),
  ("Julio","Encantado. Perdona, pero yo me voy… al trabajo.","Aangenaam. Sorry, maar ik ga… naar het werk."),
  ("María","Vale.","Oké."),("Julio","Bueno, hasta luego.","Wel, tot straks."),("María","Adiós.","Dag."),
 ]),
 ("Escena 2 · En la academia","María komt aan op haar nieuwe werk; Fernando stelt haar voor aan Josefina en Julio.",[
  ("Fernando","Las aulas, mi despacho. Ella es Josefina, la secretaria.","De klaslokalen, mijn kantoor. Zij is Josefina, de secretaresse."),
  ("Josefina","Hola, encantada. ¿Y tú cómo te llamas?","Hallo, aangenaam. En hoe heet jij?"),
  ("María","Me llamo María.","Ik heet María."),
  ("Fernando","Julio, os presento. Julio Fernández, profesor; María Torres, la nueva profesora.","Julio, ik stel jullie voor. Julio Fernández, leraar; María Torres, de nieuwe lerares."),
  ("María","¿Cómo está usted?","Hoe gaat het met u?"),("Julio","Encantado de conocerla.","Aangenaam kennis te maken."),
  ("María","Igualmente, encantada.","Insgelijks, aangenaam."),("Julio","Qué bien, qué bien.","Wat goed, wat goed."),
  ("Josefina","¿Conoces a Julio?","Ken je Julio?"),("Julio","No. ¿Conoce a Fernando, el director?","Nee. Kent u Fernando, de directeur?"),
  ("María","Sí, claro.","Ja, natuurlijk."),("Fernando","Ya, claro.","Ja, natuurlijk."),
  ("Julio","Pues… muy bien, muy bien. ¿Qué tal la academia?","Wel… heel goed, heel goed. Hoe bevalt de academie?"),
  ("María","Bien, muy bien.","Goed, heel goed."),("Fernando","Julio, ¿estás bien?","Julio, ben je oké?"),
  ("Julio","Claro, muy bien, muy bien.","Natuurlijk, heel goed, heel goed."),
  ("María","Bueno, muchas gracias, Fernando, por el trabajo.","Wel, hartelijk dank, Fernando, voor het werk."),
  ("Fernando","De nada. Bienvenida a la academia Habla con Eñe.","Graag gedaan. Welkom op de academie Habla con Eñe."),
 ]),
]

def mark(es):
    out=es
    for c in sorted(CHUNKS,key=len,reverse=True):
        # markeer de chunk (hoofdletter-ongevoelig, hele-woord-achtig)
        out=re.sub("("+re.escape(c)+")", r'<span class="ch">\1</span>', out, count=1, flags=re.IGNORECASE)
    return out

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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 1 · Escucha</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 1 · Presentaciones — ¡Escucha!</h1><p>Bekijk de scène en <b>lees mee</b>. Klik een zin om ze te horen; zet Nederlands aan/uit; de <span style="background:#FEF08A;color:#20242E;border-radius:4px;padding:0 4px">gele</span> woorden zijn de bruikbare chunks.</p></div>
<main>
 <div class="grid">
  <div class="vid">
    <div class="vidbox"><iframe src="https://drive.google.com/file/d/{VIDEO_ID}/preview" allow="autoplay" allowfullscreen></iframe></div>
    <div class="toolbar">
      <button class="btn" id="tgnl">🇳🇱 Nederlands aan</button>
      <span class="legend">💡 <span class="ch">geel</span> = chunk om mee te nemen</span>
    </div>
  </div>
  <div class="tr">{BODY}</div>
 </div>
 <div class="foot">C4 · «Welcome to Spanish» · Unidad 1 — meelees-transcript (rood). Video ingebed vanaf Google Drive (besloten klasgebruik).</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.ln').forEach(function(l){{var b=l.querySelector('.spk');var es=l.getAttribute('data-es');b.onclick=function(){{speak(es);}};l.addEventListener('click',function(e){{if(e.target!==b)speak(es);}});}});
var nlon=false;document.getElementById('tgnl').onclick=function(){{nlon=!nlon;document.body.classList.toggle('shownl',nlon);this.classList.toggle('on',nlon);this.textContent=nlon?'🇳🇱 Nederlands uit':'🇳🇱 Nederlands aan';}};
</script></body></html>"""
os.makedirs(f"{ROOT}/01-cursussen/04-welcome/U1",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U1_escucha.html","w").write(HTML)
print("C4_U1_escucha.html geschreven:",len(HTML),"bytes")
