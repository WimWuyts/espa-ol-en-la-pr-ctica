#!/usr/bin/env python3
# C4 — HERBRUIKBAAR kaart-component «El mundo hispano» (La Ruta).
# Toont de echte mundo-hispano-kaart (Natural Earth); klik op een land → fiche met
# vaste data (vlag·capital·población·moneda·gentilicio·idioma + «¿Sabías que…?») +
# één themafeit dat meebeweegt met de unidad + een ★ ¡Estás aquí!-markering.
# Feitenlaag = GEDEELDE bron paises_data.py (cursus-onafhankelijk).
# Standalone HTML (C4-rood), bedoeld als extra tab in de C4-hub. Env-gestuurd:
#   C4_UNIT=<n>  C4_MAPA_OUT=C4_U<n>_mapa.html  python3 gen_c4_mapa.py
import os, sys, base64
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
import paises_data as PD

def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

MAPSVG=open(f"{ROOT}/02-huisstijl/beeld/generators/mundo_map_real.svg",encoding="utf-8").read()

# ---- C4-mappings (route + themalagen) --------------------------------------
# themalaag per unit (thema_key MOET in PD.TEMAS bestaan). C4 = motiverende laag,
# géén A2-leerstof (overlap met C5 bewust klein). Elke unit een ander thema.
UNIT_TEMA = {
 1: ("persona", "⭐ Alguien de aquí"),   # Presentaciones — een bekende persoon per land
 2: ("simbolo", "🌎 Un símbolo"),         # Saludos — een symbool/icoon per land
 3: ("musica",  "🎵 Su música"),          # Nacionalidades/países — een muziekweetje per land
 4: ("familia", "👪 En familia"),
 5: ("compras", "🛍️ Un producto típico"),   # objetos → een typisch product per land
 6: ("lugar",   "🏠 Casas y lugares"),        # la casa y los lugares → een typische plek/woning per land
 # U7 hergebruikt bewust «persona» (spaced recycling, §14): in U1 was de vraag «wie komt hier vandaan?»,
 # in U7 is de invalshoek «wat is zijn/haar BEROEP?» (Frida Kahlo, pintora · Nadal, tenista).
 7: ("persona", "💼 Su profesión"),           # las profesiones → bekende persoon + beroep per land
 8: ("rutina",  "⏰ ¿A qué hora?"),            # la hora y los días → dag-/maaltijdritme per land
 9: ("viaje",   "✈️ ¿Qué vas a visitar?"),     # planes → «voy a visitar…» per land (ir a + infinitivo)
 # U10 hergebruikt bewust «familia» (spaced recycling, §14): in U4 was de vraag «hoe is de familie?»,
 # in U10 is de invalshoek «wie helpt er in huis?» — zelfde feiten, andere didactische hoek.
 10:("familia", "🏠 ¿Quién ayuda en casa?"),    # tareas domésticas → rollen in het gezin per land
}
# de route: C4 = «vertrekhal». De sitcom (Julio & María) speelt in Madrid → España is
# het thuisbasis-vertrekpunt vanaf U1. {code: (start_unit, "rango", "NL/ES-beschrijving")}
PARADAS = {
 "ESP": (1, "U1→", "España — aquí empieza todo · hier begint de reis (Julio y María viven en Madrid)"),
}

# per-unit intro (ES + NL-steun)
INTRO = {
 1: ("Cada persona viene de un país. Haz clic en un país del mundo hispano y descúbrelo.",
     "Iedereen komt ergens vandaan. Klik op een land van de Spaanstalige wereld en ontdek het."),
 2: ("Un saludo suena distinto en cada país. Explora el mapa y su símbolo.",
     "Een groet klinkt anders in elk land. Verken de kaart en het symbool van elk land."),
 3: ("¿De dónde eres? 21 países, un idioma. Haz clic en un país: bandera, capital, gentilicio e idioma.",
     "Waar kom je vandaan? 21 landen, één taal. Klik op een land: vlag, hoofdstad, nationaliteit en taal."),
 6: ("Cada país tiene sus casas y sus lugares. Haz clic en un país y descubre cómo se vive.",
     "Elk land heeft zijn eigen huizen en plekken. Klik op een land en ontdek hoe men er woont."),
 7: ("¿A qué se dedican? Haz clic en un país y descubre a alguien famoso… y su profesión.",
     "Wat doen ze voor werk? Klik op een land en ontdek een bekende persoon… én zijn/haar beroep."),
 8: ("¿A qué hora se come? Cada país tiene su ritmo. Haz clic en un país y descúbrelo.",
     "Hoe laat eet men er? Elk land heeft zijn eigen ritme. Klik op een land en ontdek het."),
 9: ("¿Qué vas a visitar? Haz clic en un país y di: «Voy a visitar…».",
     "Wat ga je bezoeken? Klik op een land en zeg: «Voy a visitar…» — zo oefen je ir a + infinitivo."),
 10:("En casa, ¿quién ayuda? Haz clic en un país y descubre cómo se vive en familia.",
     "Wie helpt er in huis? Klik op een land en ontdek hoe men er in familie samenleeft."),
}
DEFAULT_INTRO = ("Haz clic en un país del mundo hispano para leer su ficha.",
                 "Klik op een land van de Spaanstalige wereld voor zijn fiche.")

def build(unit, out_name):
    intro_es, intro_nl = INTRO.get(unit, DEFAULT_INTRO)
    info_js = PD.info_block_js(unit, unit_tema=UNIT_TEMA, paradas=PARADAS)
    tema_key, tema_label = UNIT_TEMA.get(unit, ("", ""))
    CSS=FONTS+"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--card:#fff;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif;--hand:'Caveat',cursive}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#181513;--crema:#241C1B;--gt:#3A1E20;--line:#3a302e;--card:#211a19}
*{box-sizing:border-box}body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
.wrap{max-width:900px;margin:0 auto;padding:20px 20px 40px}
.hero{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;border-radius:20px;padding:22px 26px;margin-bottom:8px}
.hero h1{font-family:var(--disp);font-weight:800;font-size:28px;margin:0 0 4px}
.hero p{margin:0;max-width:640px;opacity:.96}.hero .nl{font-family:var(--hand);font-size:18px;opacity:.95;margin-top:4px}
h2.sec{font-family:var(--disp);font-weight:700;color:var(--gd);font-size:22px;margin:22px 0 6px}
.lead{color:var(--mut);max-width:720px;margin:0 0 12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:14px 0}
#mapwrap svg{width:100%;height:auto;border-radius:12px;display:block}
#mapwrap path.spa,#mapwrap path.usa{transition:opacity .12s}
.mapinfo{margin-top:14px;padding:15px 17px;background:var(--gt);border-radius:14px;min-height:70px;transition:background .15s}
.mapinfo h3{margin:0 0 8px;font-family:var(--disp);color:var(--gd);font-size:20px}
.mapinfo .mrow{font-size:14px;margin:3px 0}
.gloss{font-size:13px;color:var(--mut);font-style:italic}
.legend{display:flex;gap:14px;flex-wrap:wrap;font-size:12.5px;color:var(--mut);margin:10px 2px 0}
.legend b{color:var(--gd)}
.foot{color:var(--mut);font-size:12px;text-align:center;margin-top:30px}
"""
    html=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>El mundo hispano · La Ruta</title><style>{CSS}</style></head><body>
<div class="wrap">
 <div class="hero">
   <h1>🗺️ El mundo hispano · La Ruta</h1>
   <p>{intro_es}</p>
   <div class="nl">{intro_nl}</div>
 </div>
 <h2 class="sec">Haz clic en un país 👆</h2>
 <p class="lead">Los países en color son los <b>21 países</b> donde el español es lengua oficial. La <b>★</b> marca dónde estamos en la ruta.{(' Esta unidad añade: <b>'+tema_label+'</b>.') if tema_key else ''}</p>
 <div class="card" id="mapwrap">{MAPSVG}
   <div class="mapinfo" id="mapinfo"><p class="gloss" style="margin:0">👆 Klik op een gekleurd land (of de halte ★) om de fiche te lezen — vlag, hoofdstad, nationaliteit, taal en een weetje.</p></div>
 </div>
 <div class="legend"><span><b>★</b> = ¡Estás aquí! (parada de la ruta)</span><span>🗣️ Gentilicio = de nationaliteit</span><span>🌐 Idioma = de taal</span></div>
 <div class="foot">C4 · «Welcome to Spanish» · El mundo hispano — feitenlaag gedeeld over C4·C5·C6·C6+</div>
</div>
<script>
(function(){{
 {info_js}
 const wrap=document.getElementById('mapwrap');const svg=wrap.querySelector('svg');const box=document.getElementById('mapinfo');
 if(!svg)return;
 svg.querySelectorAll('path.spa, path.usa').forEach(p=>{{p.style.cursor='pointer';
   p.addEventListener('mouseenter',()=>{{p.style.opacity='.72'}});
   p.addEventListener('mouseleave',()=>{{p.style.opacity=''}});
   p.addEventListener('click',()=>{{const c=p.getAttribute('data-c');const d=INFO[c];if(!d)return;
     {PD.RENDER_JS}
     box.scrollIntoView({{behavior:'smooth',block:'nearest'}});}});
 }});
}})();
</script></body></html>"""
    outp=f"{ROOT}/03-build/web/componentes/{out_name}"
    open(outp,"w",encoding="utf-8").write(html)
    nstar=info_js.count('"star": 1')
    print(f"{out_name} geschreven: {len(html)} bytes · unit U{unit} · tema={tema_key or '—'} · {nstar} parada-land(en) met ★")
    return outp

if __name__=="__main__":
    unit=int(os.environ.get("C4_UNIT","3"))
    out=os.environ.get("C4_MAPA_OUT",f"C4_U{unit}_mapa.html")
    build(unit, out)
