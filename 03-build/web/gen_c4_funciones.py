#!/usr/bin/env python3
# C4 — HERBRUIKBAAR component «Mis funciones comunicativas» (doorlopende, groeiende ruggengraat).
# Toont: (1) video-noticing «¿Qué hacen con el idioma?» van deze unit · (2) wat deze unit toevoegt ·
# (3) het cumulatieve repertoire (banco) met exponentes per unit + zelf-semáforo. Env-gestuurd:
#   C4_UNIT=<n>  C4_FUNC_OUT=C4_U<n>_funciones.html  python3 gen_c4_funciones.py
import os, sys, base64
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
import funciones_data as FD

def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

CSS=FONTS+"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--card:#fff;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif;--hand:'Caveat',cursive}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#181513;--crema:#241C1B;--gt:#3A1E20;--line:#3a302e;--card:#211a19}
*{box-sizing:border-box}body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
.wrap{max-width:920px;margin:0 auto;padding:20px 20px 44px}
.hero{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;border-radius:20px;padding:22px 26px;margin-bottom:6px}
.hero h1{font-family:var(--disp);font-weight:800;font-size:27px;margin:0 0 4px}
.hero p{margin:0;max-width:660px;opacity:.96}.hero .nl{font-family:var(--hand);font-size:18px;opacity:.95;margin-top:4px}
h2.sec{font-family:var(--disp);font-weight:700;color:var(--gd);font-size:21px;margin:24px 0 4px}
.lead{color:var(--mut);max-width:720px;margin:0 0 12px}
.grow{display:flex;gap:6px;align-items:center;flex-wrap:wrap;margin:6px 0 0;font-size:13px;color:var(--mut)}
.grow b{color:var(--gd)}.grow .dot{width:9px;height:9px;border-radius:50%;background:var(--line)}.grow .dot.on{background:var(--g)}
/* noticing */
.noti{display:grid;grid-template-columns:repeat(auto-fill,minmax(255px,1fr));gap:10px;margin-top:8px}
.nc{border:1.5px solid var(--line);border-left:4px solid var(--g);border-radius:12px;padding:11px 13px;background:var(--card);cursor:pointer}
.nc .cita{font-family:var(--disp);font-weight:700;font-size:14.5px}
.nc .hint{font-size:11.5px;color:var(--mut);margin-top:3px}
.nc .fun{display:none;margin-top:6px;font-size:12.5px;color:var(--gd);font-weight:700}
.nc.open{background:var(--gt)}.nc.open .fun{display:block}.nc.open .hint{display:none}
/* esta unidad */
.chips{display:flex;flex-wrap:wrap;gap:7px;margin-top:6px}
.chip{border-radius:20px;padding:4px 11px;font-size:12.5px;font-weight:700}
.chip.nueva{background:var(--g);color:#fff}.chip.nivel{background:var(--gt);color:var(--gd);border:1px solid var(--g)}
.chip.tar{background:var(--crema);color:var(--ink);border:1px solid var(--line)}
/* banco */
.banco{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:8px}
@media(max-width:720px){.banco{grid-template-columns:1fr}}
.fc{border:1px solid var(--line);border-radius:16px;padding:14px 16px;background:var(--card);position:relative}
.fc.hl{border-color:var(--g);box-shadow:0 0 0 2px var(--gt)}
.fc h3{font-family:var(--disp);font-size:16.5px;margin:0 0 1px;color:var(--ink)}
.fc .gl{font-size:12px;color:var(--mut);font-style:italic;margin-bottom:6px}
.fc .cefr{display:inline-block;background:var(--gt);color:var(--gd);border-radius:20px;padding:2px 9px;font-size:10.5px;font-weight:700;margin-left:6px;vertical-align:middle}
.badge{display:inline-block;font-size:9.5px;font-weight:800;border-radius:6px;padding:1px 6px;margin-left:6px;vertical-align:middle}
.badge.nueva{background:var(--g);color:#fff}.badge.nivel{background:var(--gt);color:var(--gd);border:1px solid var(--g)}
.urow{display:flex;gap:8px;align-items:flex-start;margin:5px 0}
.ub{flex:none;font-family:var(--disp);font-weight:800;font-size:10.5px;background:var(--crema);color:var(--gd);border-radius:6px;padding:2px 7px;margin-top:2px}
.ub.now{background:var(--g);color:#fff}
.exps{display:flex;flex-wrap:wrap;gap:5px}
.exp{background:var(--paper);border:1px solid var(--line);border-radius:9px;padding:4px 9px 4px 26px;font-size:12.5px;font-weight:600;position:relative;cursor:pointer}
.exp:hover{background:var(--gt)}
.exp:before{content:"🔊";position:absolute;left:7px;top:4px;font-size:11px;opacity:.5}
.sem{display:flex;gap:6px;align-items:center;margin-top:9px;padding-top:8px;border-top:1px dashed var(--line);font-size:11.5px;color:var(--mut)}
.sem .s{width:15px;height:15px;border-radius:50%;border:1.5px solid var(--mut);cursor:pointer}
.sem .s.g{border-color:#2F9A4A}.sem .s.y{border-color:#B7860B}.sem .s.r{border-color:#DC2626}
.sem .s.on.g{background:#2F9A4A}.sem .s.on.y{background:#B7860B}.sem .s.on.r{background:#DC2626}
.foot{color:var(--mut);font-size:12px;text-align:center;margin-top:30px}
"""

def noticing_block(unit):
    items=FD.NOTICING.get(unit,[])
    def nc(cita,fid):
        f=FD.FMAP[fid]
        return (f'<div class="nc" onclick="this.classList.toggle(\'open\')"><div class="cita">{cita}</div>'
                f'<div class="hint">👆 ¿qué función? · klik</div>'
                f'<div class="fun">🗣️ {f["es"]} <span style="color:var(--mut);font-weight:400">· {f["nl"]}</span></div></div>')
    return '<div class="noti">'+"".join(nc(*i) for i in items)+'</div>'

def esta_unidad(unit):
    fs=FD.funciones_hasta(unit)
    nuevas=[f for f in fs if FD.status(f,unit)=="nueva"]
    nivel=[f for f in fs if FD.status(f,unit)=="nivel"]
    ch=""
    if nuevas: ch+="".join(f'<span class="chip nueva">＋ {f["es"]}</span>' for f in nuevas)
    if nivel:  ch+="".join(f'<span class="chip nivel">▲ {f["es"]}</span>' for f in nivel)
    return f'<div class="chips">{ch}</div>'

def banco_block(unit):
    cards=[]
    for f in FD.funciones_hasta(unit):
        st=FD.status(f,unit)
        badge=(f'<span class="badge nueva">NUEVA</span>' if st=="nueva" else
               f'<span class="badge nivel">▲ NIVEL +</span>' if st=="nivel" else "")
        rows=""
        for u in sorted(k for k in f["exp"] if k<=unit):
            now=" now" if u==unit else ""
            exps="".join(f'<span class="exp" data-w="{e.split(" · ")[0].replace("…","")}">{e}</span>' for e in f["exp"][u])
            rows+=f'<div class="urow"><span class="ub{now}">U{u}</span><span class="exps">{exps}</span></div>'
        sem=('<div class="sem">¿Ya lo sé decir? '
             '<span class="s g" onclick="this.classList.toggle(\'on\')"></span>'
             '<span class="s y" onclick="this.classList.toggle(\'on\')"></span>'
             '<span class="s r" onclick="this.classList.toggle(\'on\')"></span></div>')
        hl=" hl" if st in ("nueva","nivel") else ""
        cards.append(f'<div class="fc{hl}"><h3>{f["es"]}{badge}<span class="cefr">{f["cefr"]}</span></h3>'
                     f'<div class="gl">{f["nl"]}</div>{rows}{sem}</div>')
    return '<div class="banco">'+"".join(cards)+'</div>'

def tarea_block(unit):
    ids=FD.TAREA_FUN.get(unit,[])
    if not ids: return ""
    ch="".join(f'<span class="chip tar">🗣️ {FD.FMAP[i]["es"]}</span>' for i in ids)
    tt=FD.TAREA_TITEL.get(unit,"")
    return (f'<h2 class="sec">En la tarea de esta unidad usas… 🎯</h2>'
            f'<p class="lead">De eindtaak <b>«{tt}»</b> combineert deze functies — oude én nieuwe. Zo herhaal je zonder het te merken.</p>'
            f'<div class="chips">{ch}</div>')

def build(unit, out_name):
    total=len(FD.FUNCIONES)
    have=len(FD.funciones_hasta(unit))
    dots="".join(f'<span class="dot{" on" if i<have else ""}"></span>' for i in range(total))
    html=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U{unit} · Funciones comunicativas</title><style>{CSS}</style></head><body>
<div class="wrap">
 <div class="hero">
   <h1>🗣️ Mis funciones comunicativas</h1>
   <p>No solo palabras: lo que <b>puedes hacer</b> con el español. Y crece en cada unidad.</p>
   <div class="nl">Niet enkel woorden — wat je met het Spaans kunt <b>dóen</b>. En het groeit elke unit.</div>
 </div>
 <div class="grow"><b>Tu repertorio:</b> {have} / {total} funciones {dots} <span>· hoe verder op de ruta, hoe meer je kunt zeggen</span></div>

 <h2 class="sec">¿Qué hacen con el idioma? 🎬</h2>
 <p class="lead">Kijk terug naar de scène. Wat <b>doen</b> de personages met taal? Klik elke zin en ontdek de <i>función</i>.</p>
 {noticing_block(unit)}

 <h2 class="sec">Esta unidad añade… ✨</h2>
 <p class="lead"><span style="color:var(--g);font-weight:700">＋ nieuw</span> = een nieuwe functie · <span style="color:var(--gd);font-weight:700">▲ niveau +</span> = een functie die je al kende, nu met méér manieren om ze te zeggen.</p>
 {esta_unidad(unit)}

 <h2 class="sec">Mi repertorio · lo que ya sé hacer 📚</h2>
 <p class="lead">Alles wat je tot nu toe kunt — met de <i>exponentes</i> (vaste formules) per unit. Klik 🔊 om te horen; zet je <b>semáforo</b> per functie.</p>
 {banco_block(unit)}

 {tarea_block(unit)}

 <div class="foot">C4 · «Welcome to Spanish» · Funciones comunicativas — één groeiende ruggengraat over alle unidades</div>
</div>
<script>
function speak(t){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}}
document.querySelectorAll('.exp').forEach(function(e){{e.onclick=function(){{speak(e.getAttribute('data-w'));}};}});
</script></body></html>"""
    outp=f"{ROOT}/03-build/web/componentes/{out_name}"
    open(outp,"w",encoding="utf-8").write(html)
    print(f"{out_name} geschreven: {len(html)} bytes · U{unit} · {have}/{total} functies")
    return outp

if __name__=="__main__":
    unit=int(os.environ.get("C4_UNIT","3"))
    out=os.environ.get("C4_FUNC_OUT",f"C4_U{unit}_funciones.html")
    build(unit, out)
