#!/usr/bin/env python3
# C4 · Unidad 10 — HTML-HUB (tabbladen, srcdoc-iframes). C4-rood. Zelfde pijplijn als U1–U9.
# NB: de video van U10 komt (zoals U8–U9) uit Google Drive (/preview-embed) i.p.v. YouTube.
import base64, os
ROOT="/home/user/espa-ol-en-la-pr-ctica"
CMP=f"{ROOT}/03-build/web/componentes"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

def srcdoc(path):
    h=open(path,encoding="utf-8").read()
    return h.replace("&","&amp;").replace('"',"&quot;")

TABS=[
 ("escucha","🎬 Escucha","C4_U10_escucha.html","Bekijk de scène en lees mee — de chunks komen uit je oren."),
 ("comprension","📖 Lee y escucha","C4_U10_comprension.html","Een korte lees- en luisteroefening — begrijp het Spaans dat je al kent."),
 ("mapa","🗺️ Mapa","C4_U10_mapa.html","La Ruta — klik op een land en ontdek hoe men er in familie samenleeft."),
 ("funciones","🗣️ Funciones","C4_U10_funciones.html","Wat je met het Spaans kunt DOEN — je repertoire groeit elke unit."),
 ("kit","🧰 Kit","C4_U10_kgt.html","Uitspraak (g/gu), de taakverdeler, de taal per situatie, gramática (hay que ↔ tengo que · saber + inf.) & tarea."),
 ("practica","✍️ Práctica","C4_U10_practica.html","Oefen zelfcorrigerend: herkennen → kiezen → zelf zeggen."),
 ("rol","🎭 Ensaya","C4_U10_rol.html",
  "Speel de scène zelf: de partner verbetert je en werkt zonder internet."),
 ("musica","🎧 Música","C4_U10_musica.html","Cultura (el reparto de tareas) + banda sonora — leer Spaans via muziek."),
]

def tabbtn(i,t):
    key,label,_,_=t
    on=" on" if i==0 else ""
    return f'<button class="tab{on}" data-t="{key}">{label}</button>'
def panel(i,t):
    key,label,fn,sub=t
    on=" show" if i==0 else ""
    doc=srcdoc(f"{CMP}/{fn}")
    return (f'<section class="panel{on}" id="p_{key}"><p class="psub">{sub}</p>'
            f'<div class="fw"><iframe class="frame" loading="lazy" '
            f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen; web-share" '
            f'allowfullscreen srcdoc="{doc}"></iframe></div></section>')

CSS=FONTS+r"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--card:#fff;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#181513;--crema:#241C1B;--gt:#3A1E20;--line:#3a302e;--card:#211a19}
*{box-sizing:border-box}body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper)}
.hero{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;padding:26px 22px 20px}
.hero .ruta{display:inline-block;background:#ffffff22;border:1px solid #ffffff44;border-radius:20px;padding:3px 12px;font-size:12px;font-weight:700;margin-bottom:8px}
.hero h1{font-family:var(--disp);font-weight:800;margin:0;font-size:30px}
.hero p{margin:6px 0 0;opacity:.95;max-width:720px}
.tabbar{position:sticky;top:0;z-index:5;background:var(--paper);border-bottom:1px solid var(--line);display:flex;gap:6px;flex-wrap:wrap;padding:10px 16px}
.tab{border:1.5px solid var(--line);background:var(--card);color:var(--ink);font-family:var(--disp);font-weight:700;font-size:14px;border-radius:12px;padding:8px 14px;cursor:pointer}
.tab.on{background:var(--g);color:#fff;border-color:var(--g)}
main{max-width:1120px;margin:0 auto;padding:14px 16px 30px}
.panel{display:none}.panel.show{display:block}
.psub{color:var(--mut);font-size:14px;margin:6px 2px 10px;font-style:italic}
.fw{border:1px solid var(--line);border-radius:16px;overflow:hidden;background:var(--card)}
.frame{width:100%;height:82vh;min-height:560px;border:0;display:block}
.foot{color:var(--mut);font-size:12px;text-align:center;margin:22px 0 6px}
.dk{position:fixed;right:14px;bottom:14px;border:1.5px solid var(--line);background:var(--card);color:var(--ink);border-radius:50%;width:44px;height:44px;font-size:18px;cursor:pointer;box-shadow:0 4px 14px #0002}
"""

HTML=f"""<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Unidad 10 · Las tareas de casa — Hub</title><style>{CSS}</style></head><body>
<div class="hero">
  <span class="ruta">🗺️ La Ruta · C4 «El despegue» · Parada 10</span>
  <h1>Unidad 10 · Las tareas de casa</h1>
  <p>De asistenta is ziek — dus <b>hay que limpiar</b>. Zeg wat er móet gebeuren, wat <b>jij</b> moet doen, en bied hulp aan: <b>yo te ayudo</b> · <b>¿qué tengo que hacer?</b> · <b>¿sabes pasar la aspiradora?</b> <i>Survival in Spanish.</i></p>
</div>
<nav class="tabbar">{"".join(tabbtn(i,t) for i,t in enumerate(TABS))}</nav>
<main>
{"".join(panel(i,t) for i,t in enumerate(TABS))}
  <div class="foot">C4 · «Bienvenidos al español» · Unidad 10 · Las tareas de casa</div>
</main>
<button class="dk" id="dk" title="licht/donker">🌙</button>
<script>
var tabs=document.querySelectorAll('.tab'),panels=document.querySelectorAll('.panel');
// tabbladen · het adres volgt mee, zodat een QR-code meteen goed opent
function toonTab(k){{var g=false;
  tabs.forEach(function(x){{if(x.getAttribute('data-t')===k)g=true;}});
  if(!g)return false;   // eerst kijken, dan pas schakelen: een onbekend anker
                        // mag de hub nooit zonder opgelicht tabblad achterlaten
  tabs.forEach(function(x){{x.classList.toggle('on',x.getAttribute('data-t')===k);}});
  panels.forEach(function(p){{p.classList.toggle('show',p.id==='p_'+k);}});return true;}}
function vanAdres(){{var h='';
  try{{h=decodeURIComponent((location.hash||'').slice(1));}}catch(e){{h=(location.hash||'').slice(1);}}
  if(!h)return true;
  if(toonTab(h)){{window.scrollTo(0,0);return true;}}
  var d=document.getElementById(h);
  if(d){{var p=d.closest?d.closest('.panel'):null;
    if(p&&p.id.indexOf('p_')===0)toonTab(p.id.slice(2));
    d.scrollIntoView({{behavior:'smooth',block:'start'}});return true;}}
  return false;}}
tabs.forEach(function(b){{b.onclick=function(){{var k=b.getAttribute('data-t');
  if((location.hash||'').slice(1)===k){{toonTab(k);window.scrollTo(0,0);}}
  else location.hash=k;}};}});
addEventListener('hashchange',vanAdres);
if(!vanAdres())addEventListener('load',vanAdres);
var dark=false;document.getElementById('dk').onclick=function(){{dark=!dark;document.documentElement.setAttribute('data-theme',dark?'dark':'light');this.textContent=dark?'☀️':'🌙';document.querySelectorAll('iframe.frame').forEach(function(f){{try{{f.contentDocument.documentElement.setAttribute('data-theme',dark?'dark':'light');}}catch(e){{}}}});}};
</script></body></html>"""
open(f"{CMP}/C4_U10_hub.html","w",encoding="utf-8").write(HTML)
print("C4_U10_hub.html geschreven:",len(HTML),"bytes")
