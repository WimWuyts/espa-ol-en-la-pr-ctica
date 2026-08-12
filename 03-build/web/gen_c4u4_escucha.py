#!/usr/bin/env python3
# C4 · Unidad 4 — «Escucha»-blok: Sitcom-video 4 (La familia) ingebed + interactief meelees-transcript.
import base64, os, json, re
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

VIDEO_SRC=("youtube","guCpaHfy7VQ")   # «4. La familia en español» (Spanish Sitcom A1)
ALLOW="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen; web-share"
def video_iframe(src):
    kind,vid=src
    if kind=="youtube":
        return (f'<iframe src="https://www.youtube-nocookie.com/embed/{vid}?rel=0&playsinline=1" '
                f'title="Sitcom · Episodio 4" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" '
                f'allow="{ALLOW}" allowfullscreen></iframe>')
    return f'<iframe src="https://drive.google.com/file/d/{vid}/preview" allow="{ALLOW}" allowfullscreen></iframe>'
IFRAME=video_iframe(VIDEO_SRC)
YT_WATCH="https://www.youtube.com/watch?v="+VIDEO_SRC[1]
CHUNKS=["es un chico","es simpático","es divertido","es un amigo","muy elegante","un poco gorda","muy delgada","muy guapa","muy inteligente","muy alto","muy fuerte","la abuela","el tío","mi madre","mi padre","la hermana","¿dónde vives?","Vivo en","divertida","amable","guapo","de pequeña"]
SCENES=[
 ("Escena 1 · El interrogatorio","La madre de María la interroga sobre «un chico»: ¿es simpático, es divertido, es un amigo?",[
  ("Madre","Entonces, ¿es un chico?","Dus, is het een jongen?"),
  ("María","Sí mamá, es un chico.","Ja mama, het is een jongen."),
  ("Madre","Ya. ¿Y es simpático?","Juist. En is hij aardig?"),
  ("María","Sí mamá, es simpático.","Ja mama, hij is aardig."),
  ("Madre","¿Y es un amigo?","En is het een vriend?"),
  ("María","Sí mamá, es un amigo.","Ja mama, het is een vriend."),
  ("Madre","¿Y es muy amigo? ¿Es divertido?","En een goede vriend? Is hij leuk?"),
  ("María","¡Mamá! Ya voy yo. ¡Que voy yo!","Mama! Ik ga wel. Ik ga al!"),
  ("Madre","Sube, sube, ya abro. Sube.","Kom boven, ik doe open. Kom."),
 ]),
 ("Escena 2 · El álbum de fotos","La madre le enseña a Julio las fotos de la familia y describe a todo el mundo, con muchos adjetivos.",[
  ("Madre","Esta es mi madre, la abuela de María. Es muy elegante, pero un poco gorda.","Dit is mijn moeder, de oma van María. Ze is heel elegant, maar een beetje mollig."),
  ("Madre","Esta es María, de pequeña. En esta foto está muy, muy gorda.","Dit is María als klein meisje. Op deze foto is ze heel, heel dik."),
  ("Julio","Ahora es una chica muy delgada y muy guapa.","Nu is ze een heel slank en heel knap meisje."),
  ("Madre","Ahora sí, ahora es muy guapa y muy inteligente. Pero elegante no es.","Nu wel, nu is ze heel knap en heel intelligent. Maar elegant is ze niet."),
  ("Madre","¡Ah! El tío Fermín. Él sí que es guapo, el guapo de la familia. Muy alto y muy fuerte.","Ah! Oom Fermín. Híj is knap, de knapperd van de familie. Heel lang en heel sterk."),
  ("Madre","¿Tú no eres muy alto, no?","Jij bent niet erg lang, hè?"),
  ("Julio","No, la verdad es que no.","Nee, eerlijk gezegd niet."),
  ("Madre","¿Andrés, dónde vives?","Andrés, waar woon je? (ze zegt zijn naam fout!)"),
  ("Julio","¿Yo? Vivo en la calle de los…","Ik? Ik woon in de straat van de…"),
  ("Madre","Este es mi padre, un hombre maravilloso. Los chicos de ahora no son así.","Dit is mijn vader, een geweldige man. De jongens van nu zijn niet zo."),
  ("Madre","Paula es la hermana de María, vive en Londres. ¡Divertida, amable…! María no es así.","Paula is de zus van María, ze woont in Londen. Grappig, lief…! María is niet zo."),
 ]),
]
def mark(es):
    ph=[]; out=es
    def grab(m):
        ph.append(m.group(1)); return "\x00%d\x00"%(len(ph)-1)
    for c in sorted(CHUNKS,key=len,reverse=True):
        out=re.sub("("+re.escape(c)+")", grab, out, count=1, flags=re.IGNORECASE)
    return re.sub("\x00(\\d+)\x00", lambda m:'<span class="ch">'+ph[int(m.group(1))]+'</span>', out)
COL={"María":"#D64550","Julio":"#2563EB","Madre":"#7C4DE0"}
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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 4 · Escucha</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 4 · La familia — ¡Escucha!</h1><p>Mira la escena y <b>lee al mismo tiempo</b>. Pulsa una frase para oírla; activa o desactiva el neerlandés. Las palabras en <span style="background:#FEF08A;color:#20242E;border-radius:4px;padding:0 4px">amarillo</span> son los chunks útiles. <span class="stn">lees mee; de gele woorden zijn de chunks</span></p></div>
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
 <div class="foot">C4 · «Bienvenidos al español» · Unidad 4 · La familia</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.ln').forEach(function(l){{var b=l.querySelector('.spk');var es=l.getAttribute('data-es');b.onclick=function(){{speak(es);}};l.addEventListener('click',function(e){{if(e.target!==b)speak(es);}});}});
var nlon=false;document.getElementById('tgnl').onclick=function(){{nlon=!nlon;document.body.classList.toggle('shownl',nlon);this.classList.toggle('on',nlon);this.textContent=nlon?'🇳🇱 Neerlandés OFF':'🇳🇱 Neerlandés ON';}};
</script></body></html>"""
os.makedirs(f"{ROOT}/01-cursussen/04-welcome/U4",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U4_escucha.html","w").write(HTML)
print("C4_U4_escucha.html geschreven:",len(HTML),"bytes")
