#!/usr/bin/env python3
# C4 · Unidad 3 — «Escucha»-blok: Sitcom-video 3 (Nacionalidades y países) ingebed + interactief
# meelees-transcript (ES + NL-toggle, klik-om-te-horen, chunks gemarkeerd). Zelfde patroon/pijplijn als U1/U2.
import base64, os, json, re
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

# videobron: «3. Nacionalidades y países en español» (Spanish Sitcom A1, Habla con Eñe / Hablamétodo).
VIDEO_SRC=("youtube","62GTD0QXbiI")
ALLOW="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen; web-share"
def video_iframe(src):
    kind,vid=src
    if kind=="youtube":
        return (f'<iframe src="https://www.youtube-nocookie.com/embed/{vid}?rel=0&playsinline=1" '
                f'title="Sitcom · Episodio 3" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" '
                f'allow="{ALLOW}" allowfullscreen></iframe>')
    return f'<iframe src="https://drive.google.com/file/d/{vid}/preview" allow="{ALLOW}" allowfullscreen></iframe>'
IFRAME=video_iframe(VIDEO_SRC)
YT_WATCH="https://www.youtube.com/watch?v="+VIDEO_SRC[1] if VIDEO_SRC[0]=="youtube" else "https://drive.google.com/file/d/"+VIDEO_SRC[1]+"/view"
# hoogfrequente chunks om te markeren (survival — focus U3: ¿de dónde eres?/soy de + país + gentilicio + idiomas + getallen)
CHUNKS=["¿De dónde eres?","¿De qué país?","soy de Argelia","soy de","Eres argelina","argelina","argelino","alemán","alemana","portugués","portuguesa","colombiano","colombiana","Buenas noches","por favor","Habla usted francés","Habla bastante bien","No hablo mucho","entiendo un poco","Tres idiomas","árabe","francés","español","Veinte euros","Veinte","diez"]
# ── TRANSCRIPT = exact aangeleverd door de auteur (Episodio 3 · Nacionalidades/Países). 3 scènes.
SCENES=[
 ("Escena 1 · La pregunta clave: ¿De dónde eres?","Fernando ontmoet een vrouw die om geld vraagt en leert haar de kernvraag van de reis — én de valstrik «soy Argelia» → «soy de Argelia».",[
  ("Josefina","Bueno, buenas noches.","Goed, goedenavond."),
  ("Fernando","Buenas noches, Josefina.","Goedenavond, Josefina."),
  ("Extranjera","Dinero. Dinero, por favor.","Geld. Geld, alstublieft."),
  ("Fernando","¿De dónde eres?","Waar kom je vandaan?"),
  ("Extranjera","¿Cómo?","Wat/Hoezo?"),
  ("Fernando","¿De dónde eres? ¿De qué país?","Waar kom je vandaan? Uit welk land?"),
  ("Extranjera","¡Ah! Yo soy Argelia.","Ah! Ik ben Algerije. (fout!)"),
  ("Fernando","No. «Yo soy de Argelia». Eres argelina. Chica, argelina. Chico, argelino. Mira: alemán, alemana; portugués, portuguesa; colombiano, colombiana. Julio.","Nee. «Ik kom uit Algerije.» Je bent Algerijns. Meisje: argelina. Jongen: argelino. Kijk: Duits(e), Portugees/Portugese, Colombiaan(se). Julio."),
 ]),
 ("Escena 2 · La nacionalidad y los idiomas","Julio komt erbij; ze bevestigen de gentilicio en ontdekken dat de vrouw drie talen spreekt.",[
  ("Julio","¿Sí?","Ja?"),
  ("Fernando","Se dice argelina, ¿no? De Argelia, argelino.","Je zegt argelina, toch? Uit Algerije: argelino."),
  ("Julio","O argelina, sí. Buenas noches.","Of argelina, ja. Goedenavond."),
  ("Extranjera","Buenas noches.","Goedenavond."),
  ("Julio","Habla bastante bien español.","U spreekt vrij goed Spaans."),
  ("Extranjera","No hablo mucho, pero entiendo un poco. El dinero.","Ik spreek niet veel, maar ik versta een beetje. Het geld."),
  ("Julio","¿Habla usted francés? ¡Qué maravilla! Tres idiomas, ¿no? Árabe, francés y español.","Spreekt u Frans? Wat geweldig! Drie talen, toch? Arabisch, Frans en Spaans."),
 ]),
 ("Escena 3 · El dinero y los números","Ze regelen het geld — met de getallen die je op reis nodig hebt.",[
  ("Extranjera","El dinero.","Het geld."),
  ("Julio","¿Qué dinero?","Welk geld?"),
  ("Fernando","Veinte euros está bien, ¿no?","Twintig euro is goed, niet?"),
  ("Extranjera","Veinte, diez…","Twintig, tien…"),
  ("Fernando","Veinte, veinte. Uno, dos, tres, cinco, diez, veinte.","Twintig, twintig. Eén, twee, drie, vijf, tien, twintig."),
  ("Julio","Yo no tengo. Un momento. ¡María, dinero!","Ik heb niks. Een momentje. María, geld!"),
  ("Fernando","Qué maravilla el norte de África, ¿no? ¡El Magreb!","Wat prachtig, Noord-Afrika, hè? De Maghreb!"),
  ("María","Tengo uno de veinte y dos de diez. Hola. Espera, tengo monedas.","Ik heb er één van twintig en twee van tien. Hallo. Wacht, ik heb muntjes."),
  ("Julio","Aquí tiene.","Alstublieft."),
 ]),
]

def mark(es):
    ph=[]; out=es
    def grab(m):
        ph.append(m.group(1)); return "\x00%d\x00"%(len(ph)-1)
    for c in sorted(CHUNKS,key=len,reverse=True):
        out=re.sub("("+re.escape(c)+")", grab, out, count=1, flags=re.IGNORECASE)
    return re.sub("\x00(\\d+)\x00", lambda m:'<span class="ch">'+ph[int(m.group(1))]+'</span>', out)

COL={"María":"#D64550","Julio":"#2563EB","Fernando":"#7C4DE0","Josefina":"#0E9E97","Extranjera":"#EA7317"}
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
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 3 · Escucha</title><style>{CSS}</style></head><body>
<div class="top"><h1>Unidad 3 · Nacionalidades y países — ¡Escucha!</h1><p>Bekijk de scène en <b>lees mee</b>. Klik een zin om ze te horen; zet Nederlands aan/uit; de <span style="background:#FEF08A;color:#20242E;border-radius:4px;padding:0 4px">gele</span> woorden zijn de bruikbare chunks.</p></div>
<main>
 <div class="grid">
  <div class="vid">
    <div class="vidbox">{IFRAME}</div>
    <div class="toolbar">
      <button class="btn" id="tgnl">🇳🇱 Neerlandés ON</button>
      <a class="btn" href="{YT_WATCH}" target="_blank" rel="noopener">▶ Op YouTube</a>
      <span class="legend">💡 <span class="ch">geel</span> = chunk om mee te nemen</span>
    </div>
    <p class="vidhint">Speelt de video niet af? Klik <a href="{YT_WATCH}" target="_blank" rel="noopener">hier om ze op YouTube te openen</a>.</p>
  </div>
  <div class="tr">{BODY}</div>
 </div>
 <div class="foot">C4 · «Bienvenidos al español» · Unidad 3 · Nacionalidades y países</div>
</main>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.ln').forEach(function(l){{var b=l.querySelector('.spk');var es=l.getAttribute('data-es');b.onclick=function(){{speak(es);}};l.addEventListener('click',function(e){{if(e.target!==b)speak(es);}});}});
var nlon=false;document.getElementById('tgnl').onclick=function(){{nlon=!nlon;document.body.classList.toggle('shownl',nlon);this.classList.toggle('on',nlon);this.textContent=nlon?'🇳🇱 Neerlandés OFF':'🇳🇱 Neerlandés ON';}};
</script></body></html>"""
os.makedirs(f"{ROOT}/01-cursussen/04-welcome/U3",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_U3_escucha.html","w").write(HTML)
print("C4_U3_escucha.html geschreven:",len(HTML),"bytes")
