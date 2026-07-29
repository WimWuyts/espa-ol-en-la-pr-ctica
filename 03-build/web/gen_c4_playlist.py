#!/usr/bin/env python3
# C4 — «La playlist de la clase» — DEFINITIEVE Top 100 Spaanstalige liedjes.
# Bron van waarheid (één lijst) → HTML-pagina (huisstijl, offline, zoekbaar) + Markdown.
# Curatie: (1) nummers die al in «Welcome to Spanish» staan · (2) Spaanstalige Ultratop-
# hits 2005-nu (BE) · (3) viraal in de laatste ~3 jaar · (4) tijdloze klassiekers.
# School-context 14-18 j.: expliciete/grove nummers gefilterd; ⚠️ = kies een clean/radio-versie.
import base64, os, json
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

# placeholder tot de auteur zijn eigen Spotify-playlist deelt (dan hier de echte id/url zetten)
SPOTIFY_URL="https://open.spotify.com/playlist/37i9dQZF1DXaxEKcoCdWHD"

# categorie-labels
CATS={
 "cursus":  ("🎬 Ya en el curso","Deze staan al in «Welcome to Spanish» (banda sonora per unit)."),
 "ultratop":("📈 Greatest hits · Ultratop BE (2005–nu)","Spaanstalige nummers die de Belgische hitlijsten haalden."),
 "viral":   ("🔥 Virales de hoy (2022–2025)","Recent viraal via TikTok/Reels/Spotify — herkenbaar voor tieners."),
 "clasico": ("🌟 Clásicos imprescindibles","Tijdloze nummers die (ook in Vlaanderen) iedereen kent."),
}

# (artiest, titel, jaar, vlag(gen), categorie, flag)  flag: ""=clean · "chk"=⚠️ kies clean-versie
SONGS=[
 # ── 1) Cursus (in Welcome to Spanish) ──
 ("Manu Chao","Me Gustas Tú",2001,"🇪🇸🇫🇷","cursus",""),
 ("Juanes","La Camisa Negra",2005,"🇨🇴","cursus",""),
 ("Luis Fonsi ft. Daddy Yankee","Despacito",2017,"🇵🇷","cursus","chk"),
 ("Enrique Iglesias","Bailando",2014,"🇪🇸","cursus",""),
 ("Shakira","Antología",1996,"🇨🇴","cursus",""),
 ("Rosalía","La Perla",2025,"🇪🇸","cursus",""),
 ("Rosalía","Despechá",2022,"🇪🇸","cursus",""),
 ("Rosalía","TKN",2020,"🇪🇸","cursus","chk"),
 ("Karol G","Provenza",2022,"🇨🇴","cursus",""),
 ("Karol G ft. Shakira","TQG",2023,"🇨🇴","cursus","chk"),
 ("Karol G","Si Antes Te Hubiera Conocido",2024,"🇨🇴","cursus",""),
 ("Aitana","Las Babys",2023,"🇪🇸","cursus",""),
 ("Aitana","6 de febrero",2024,"🇪🇸","cursus",""),
 ("Bad Bunny","Baile Inolvidable",2025,"🇵🇷","cursus",""),
 ("Bad Bunny","Tití Me Preguntó",2022,"🇵🇷","cursus","chk"),
 ("Quevedo & Bizarrap","BZRP Music Sessions #52",2022,"🇪🇸🇦🇷","cursus",""),
 ("Quevedo","Columbia",2023,"🇪🇸","cursus",""),
 ("Shakira & Bizarrap","BZRP Music Sessions #53",2023,"🇨🇴🇦🇷","cursus","chk"),
 ("Feid","Luna",2024,"🇨🇴","cursus",""),
 ("Rauw Alejandro","Todo de Ti",2021,"🇵🇷","cursus",""),
 # ── 2) Ultratop greatest hits 2005-nu ──
 ("Aventura","Obsesión",2004,"🇩🇴","ultratop",""),
 ("Shakira ft. Alejandro Sanz","La Tortura",2005,"🇨🇴🇪🇸","ultratop",""),
 ("Shakira","Waka Waka",2010,"🇨🇴","ultratop",""),
 ("Don Omar & Lucenzo","Danza Kuduro",2010,"🇵🇷🇫🇷","ultratop",""),
 ("Carlos Baute & Marta Sánchez","Colgando en tus Manos",2009,"🇻🇪🇪🇸","ultratop",""),
 ("Álvaro Soler","El Mismo Sol",2015,"🇪🇸","ultratop",""),
 ("Álvaro Soler","Sofía",2016,"🇪🇸","ultratop",""),
 ("Álvaro Soler","La Cintura",2018,"🇪🇸","ultratop",""),
 ("Marc Anthony","Vivir Mi Vida",2013,"🇵🇷","ultratop",""),
 ("Gente de Zona ft. Marc Anthony","La Gozadera",2015,"🇨🇺","ultratop",""),
 ("Carlos Vives & Shakira","La Bicicleta",2016,"🇨🇴","ultratop",""),
 ("Shakira ft. Maluma","Chantaje",2016,"🇨🇴","ultratop","chk"),
 ("J Balvin & Willy William","Mi Gente",2017,"🇨🇴🇫🇷","ultratop",""),
 ("Enrique Iglesias ft. Nicky Jam","El Perdón",2015,"🇪🇸🇵🇷","ultratop",""),
 ("Luis Fonsi & Demi Lovato","Échame la Culpa",2017,"🇵🇷🇺🇸","ultratop",""),
 ("Daddy Yankee & Snow","Con Calma",2019,"🇵🇷","ultratop",""),
 ("Karol G","Hawái",2020,"🇨🇴","ultratop",""),
 ("Rosalía & J Balvin","Con Altura",2019,"🇪🇸🇨🇴","ultratop",""),
 ("Manuel Turizo","La Bachata",2022,"🇨🇴","ultratop",""),
 ("Deorro ft. Elvis Crespo","Bailar",2016,"🇺🇸🇵🇷","ultratop",""),
 ("Ricky Martin & Maluma","Vente Pa' Ca",2016,"🇵🇷🇨🇴","ultratop","chk"),
 ("Enrique Iglesias","Súbeme la Radio",2017,"🇪🇸","ultratop",""),
 ("J Balvin","Ay Vamos",2014,"🇨🇴","ultratop",""),
 ("Nicky Jam","El Amante",2017,"🇵🇷","ultratop","chk"),
 ("CNCO","Reggaetón Lento",2016,"🌎","ultratop",""),
 ("Maluma","Felices los 4",2017,"🇨🇴","ultratop","chk"),
 ("Sebastián Yatra","Traicionera",2016,"🇨🇴","ultratop",""),
 ("Reik ft. Ozuna & Wisin","Me Niego",2018,"🇲🇽","ultratop",""),
 ("Pedro Capó & Farruko","Calma",2019,"🇵🇷","ultratop",""),
 ("Farruko","Pepas",2021,"🇵🇷","ultratop","chk"),
 # ── 3) Viraal 2022-2025 ──
 ("Grupo Frontera & Bad Bunny","Un x100to",2023,"🇲🇽🇵🇷","viral",""),
 ("Rauw Alejandro & Rosalía","Beso",2023,"🇵🇷🇪🇸","viral",""),
 ("Feid & Young Miko","Classy 101",2023,"🇨🇴","viral","chk"),
 ("Myke Towers","LALA",2023,"🇵🇷","viral","chk"),
 ("Peso Pluma & Eslabon Armado","Ella Baila Sola",2023,"🇲🇽","viral","chk"),
 ("Manuel Turizo & Grupo Frontera","El Merengue",2023,"🇨🇴🇲🇽","viral",""),
 ("Tini","Cupido",2023,"🇦🇷","viral",""),
 ("Emilia ft. Tini","La_Original.mp3",2023,"🇦🇷","viral",""),
 ("Lola Índigo & Quevedo","El Tonto",2023,"🇪🇸","viral","chk"),
 ("Bad Bunny","Mónaco",2023,"🇵🇷","viral","chk"),
 ("Bad Bunny","DtMF (DeBÍ TiRAR MáS FoToS)",2025,"🇵🇷","viral",""),
 ("Bad Bunny","NUEVAYoL",2025,"🇵🇷","viral",""),
 ("Karol G","Mi Ex Tenía Razón",2024,"🇨🇴","viral","chk"),
 ("Shakira","Puntería",2024,"🇨🇴","viral",""),
 ("Kapo","Uwaie",2024,"🇨🇴","viral",""),
 ("Beéle","Si Te Pudiera Mentir",2024,"🇨🇴","viral",""),
 ("Xavi","La Diabla",2023,"🇲🇽🇺🇸","viral","chk"),
 ("Bizarrap & Milo J","BZRP Music Sessions #57",2024,"🇦🇷","viral",""),
 ("Lola Índigo & Belén Aguilera","La Niña de la Escuela",2023,"🇪🇸","viral",""),
 ("Aitana & Sebastián Yatra","Akureyri",2024,"🇪🇸🇨🇴","viral",""),
 ("Sebastián Yatra","Tacones Rojos",2021,"🇨🇴","viral",""),
 ("Camilo","Vida de Rico",2020,"🇨🇴","viral",""),
 ("Morat","Cómo Te Atreves",2016,"🇨🇴","viral",""),
 ("María Becerra","Automático",2021,"🇦🇷","viral",""),
 ("Quevedo","Vista al Mar",2022,"🇪🇸","viral",""),
 # ── 4) Klassiekers & didactische parels ──
 ("Gipsy Kings","Bamboléo",1987,"🇫🇷","clasico",""),
 ("Los del Río","Macarena",1993,"🇪🇸","clasico",""),
 ("Buena Vista Social Club","Chan Chan",1997,"🇨🇺","clasico",""),
 ("Jarabe de Palo","La Flaca",1996,"🇪🇸","clasico",""),
 ("Manu Chao","Clandestino",1998,"🇪🇸🇫🇷","clasico",""),
 ("Santana ft. Maná","Corazón Espinado",1999,"🇲🇽","clasico",""),
 ("Maná","Rayando el Sol",1992,"🇲🇽","clasico",""),
 ("Ricky Martin","María",1995,"🇵🇷","clasico",""),
 ("Ricky Martin","La Copa de la Vida",1998,"🇵🇷","clasico",""),
 ("Chayanne","Torero",2002,"🇵🇷","clasico",""),
 ("Café Tacvba","Eres",2003,"🇲🇽","clasico",""),
 ("Julieta Venegas","Limón y Sal",2006,"🇲🇽","clasico",""),
 ("Julieta Venegas","Me Voy",2006,"🇲🇽","clasico",""),
 ("La Oreja de Van Gogh","Rosas",2004,"🇪🇸","clasico",""),
 ("Jesse & Joy","¡Corre!",2011,"🇲🇽","clasico",""),
 ("Alejandro Sanz","Corazón Partío",1997,"🇪🇸","clasico",""),
 ("Pablo Alborán","Solamente Tú",2011,"🇪🇸","clasico",""),
 ("Estopa","La Raja de tu Falda",1999,"🇪🇸","clasico",""),
 ("Chambao","Ahí Estás Tú",2005,"🇪🇸","clasico",""),
 ("Juanes","A Dios le Pido",2002,"🇨🇴","clasico",""),
 ("Juanes","Fotografía",2002,"🇨🇴","clasico",""),
 ("Shakira","Estoy Aquí",1996,"🇨🇴","clasico",""),
 ("Enrique Iglesias","Experiencia Religiosa",1994,"🇪🇸","clasico",""),
 ("Camilo","Tutu",2019,"🇨🇴","clasico",""),
 ("Jarabe de Palo","Depende",1998,"🇪🇸","clasico",""),
]
assert len(SONGS)==100, f"verwacht 100, kreeg {len(SONGS)}"

ORDER=["cursus","ultratop","viral","clasico"]
def num_map():
    n=0; out=[]
    for a,t,y,fl,c,g in SONGS:
        n+=1; out.append((n,a,t,y,fl,c,g))
    return out
NUM=num_map()

# ---------------- HTML ----------------
def card(n,a,t,y,fl,c,g):
    warn='<span class="warn" title="Kies een clean/radio-versie — check de tekst voor 14-18 j.">⚠️</span>' if g=="chk" else ""
    q=(a+" "+t).replace('"',"")
    return (f'<div class="song" data-s="{(a+" "+t+" "+fl).lower()}" data-c="{c}">'
            f'<span class="n">{n}</span>'
            f'<span class="body"><span class="ti">{t} {warn}</span><span class="ar">{a}</span></span>'
            f'<span class="meta"><span class="fl">{fl}</span><span class="yr">{y}</span></span>'
            f'<a class="play" href="https://www.youtube.com/results?search_query={q.replace(" ","+")}" target="_blank" rel="noopener" title="zoek op YouTube">▶</a>'
            f'</div>')
def section(c):
    title,sub=CATS[c]
    items="".join(card(*r) for r in NUM if r[5]==c)
    cnt=sum(1 for r in NUM if r[5]==c)
    return (f'<section class="cat" data-cat="{c}"><div class="cath"><h2>{title}</h2><span class="cnt">{cnt}</span></div>'
            f'<p class="csub">{sub}</p><div class="list">{items}</div></section>')

CSS=FONTS+r"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--card:#fff;--spot:#1DB954;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif;--hand:'Caveat',cursive}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#181513;--crema:#241C1B;--gt:#3A1E20;--line:#3a302e;--card:#211a19}
*{box-sizing:border-box}body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.5}
.hero{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;padding:26px 22px 22px}
.hero .kick{display:inline-block;background:#ffffff22;border:1px solid #ffffff44;border-radius:20px;padding:3px 12px;font-size:12px;font-weight:700;margin-bottom:8px}
.hero h1{font-family:var(--disp);font-weight:800;margin:0;font-size:30px}
.hero p{margin:8px 0 0;opacity:.96;max-width:760px}
.hero .spotbtn{display:inline-flex;gap:8px;align-items:center;background:var(--spot);color:#04170c;font-weight:800;border-radius:30px;padding:10px 18px;text-decoration:none;margin-top:14px;font-family:var(--disp)}
main{max-width:900px;margin:0 auto;padding:16px 16px 60px}
.toolbar{position:sticky;top:0;z-index:5;background:var(--paper);padding:12px 0 8px;display:flex;gap:8px;flex-wrap:wrap;align-items:center;border-bottom:1px solid var(--line)}
.search{flex:1;min-width:180px;border:1.5px solid var(--line);background:var(--card);color:var(--ink);border-radius:12px;padding:10px 14px;font-size:15px;font-family:var(--body)}
.fbtn{border:1.5px solid var(--line);background:var(--card);color:var(--ink);font-family:var(--disp);font-weight:700;font-size:13px;border-radius:20px;padding:7px 13px;cursor:pointer}
.fbtn.on{background:var(--g);color:#fff;border-color:var(--g)}
.legend{font-size:12px;color:var(--mut);margin:10px 2px}
.cat{margin-top:22px}
.cath{display:flex;align-items:center;gap:10px}
.cath h2{font-family:var(--disp);color:var(--gd);font-size:21px;margin:0}
.cnt{background:var(--gt);color:var(--gd);border-radius:20px;font-size:12px;font-weight:800;padding:2px 10px}
.csub{color:var(--mut);font-size:13px;margin:2px 0 10px}
.list{display:flex;flex-direction:column;gap:6px}
.song{display:flex;align-items:center;gap:12px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:8px 12px}
.song .n{font-family:var(--disp);font-weight:800;color:var(--g);width:30px;flex:none;text-align:right;font-size:15px}
.song .body{flex:1;min-width:0}
.song .ti{display:block;font-family:var(--disp);font-weight:700;font-size:15px}
.song .ar{display:block;color:var(--mut);font-size:12.5px}
.song .meta{display:flex;flex-direction:column;align-items:flex-end;flex:none}
.song .fl{font-size:15px}.song .yr{font-size:11px;color:var(--mut)}
.song .play{flex:none;width:34px;height:34px;border-radius:50%;background:var(--gt);color:var(--gd);display:flex;align-items:center;justify-content:center;text-decoration:none;font-size:13px;font-weight:700}
.song .play:hover{background:var(--g);color:#fff}
.warn{font-size:12px}
.none{display:none;color:var(--mut);text-align:center;padding:30px}
.foot{color:var(--mut);font-size:12px;text-align:center;margin-top:34px}
.note{background:var(--gt);border:1px solid var(--line);border-radius:14px;padding:12px 16px;font-size:13px;margin-top:16px}
.dk{position:fixed;right:14px;bottom:14px;border:1.5px solid var(--line);background:var(--card);color:var(--ink);border-radius:50%;width:44px;height:44px;font-size:18px;cursor:pointer;box-shadow:0 4px 14px #0002}
"""

FILTERS=('<button class="fbtn on" data-f="all">Todas (100)</button>'
 '<button class="fbtn" data-f="cursus">🎬 Curso</button>'
 '<button class="fbtn" data-f="ultratop">📈 Ultratop</button>'
 '<button class="fbtn" data-f="viral">🔥 Viral</button>'
 '<button class="fbtn" data-f="clasico">🌟 Clásicos</button>')

HTML=f"""<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>La playlist de la clase · Top 100</title><style>{CSS}</style></head><body>
<div class="hero">
  <span class="kick">🎧 Música en español · C4 «Welcome to Spanish»</span>
  <h1>La playlist de la clase — Top 100</h1>
  <p>Honderd Spaanstalige nummers: de liedjes uit de cursus, de <b>greatest hits</b> die in de Belgische Ultratop stonden (2005–nu), de <b>virale</b> nummers van vandaag en de <b>tijdloze klassiekers</b>. Zoek, filter en klik ▶ om op YouTube te beluisteren.</p>
  <a class="spotbtn" href="{SPOTIFY_URL}" target="_blank" rel="noopener">▶ Abrir en Spotify</a>
</div>
<main>
  <div class="toolbar">
    <input class="search" id="q" placeholder="🔎 Zoek artiest of titel…">
  </div>
  <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:10px">{FILTERS}</div>
  <div class="legend">⚠️ = kies een <b>clean/radio-versie</b> en check de tekst vóór klasgebruik (14–18 j.). · 🔎 zoekt live · ▶ opent een YouTube-zoekopdracht.</div>
  {"".join(section(c) for c in ORDER)}
  <div class="none" id="none">Geen resultaten — probeer een andere zoekterm.</div>
  <div class="note">💡 <b>Voor de leerkracht:</b> deze lijst is de <b>bronlijst</b> voor de officiële Spotify-playlist. Maak de playlist aan in je eigen Spotify-account (zoek elk nummer of importeer de titels), zet ze op «openbaar», en deel de link — dan draad ik die overal in de cursus in (nu staat er nog een placeholder). Een handvol nummers (⚠️) heeft een expliciete origineel; kies daar de clean-versie.</div>
  <div class="foot">C4 · «Welcome to Spanish» · La playlist de la clase — 100 canciones · {sum(1 for r in NUM if r[6]=="chk")} met ⚠️ (clean-versie kiezen)</div>
</main>
<button class="dk" id="dk" title="licht/donker">🌙</button>
<script>
var q=document.getElementById('q'),songs=[].slice.call(document.querySelectorAll('.song')),cats=[].slice.call(document.querySelectorAll('.cat')),cur='all';
function apply(){{var t=(q.value||'').toLowerCase().trim();var vis=0;
  songs.forEach(function(s){{var okc=cur==='all'||s.getAttribute('data-c')===cur;var okt=!t||s.getAttribute('data-s').indexOf(t)>=0;var show=okc&&okt;s.style.display=show?'':'none';if(show)vis++;}});
  cats.forEach(function(c){{var any=c.querySelectorAll('.song:not([style*="none"])').length>0;c.style.display=any?'':'none';}});
  document.getElementById('none').style.display=vis?'none':'block';}}
q.oninput=apply;
document.querySelectorAll('.fbtn').forEach(function(b){{b.onclick=function(){{cur=b.getAttribute('data-f');document.querySelectorAll('.fbtn').forEach(function(x){{x.classList.toggle('on',x===b);}});apply();}};}});
var dark=false;document.getElementById('dk').onclick=function(){{dark=!dark;document.documentElement.setAttribute('data-theme',dark?'dark':'light');this.textContent=dark?'☀️':'🌙';}};
</script></body></html>"""

os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
open(f"{ROOT}/03-build/web/componentes/C4_playlist.html","w",encoding="utf-8").write(HTML)

# ---------------- Markdown bronlijst ----------------
md=["# La playlist de la clase — Top 100 (Spaanstalige liedjes)",
"",
"> Bronlijst voor de officiële Spotify-playlist van «Welcome to Spanish» (C4).",
"> Curatie: cursusnummers · Ultratop-hits BE 2005–nu · viraal 2022–2025 · klassiekers.",
"> **⚠️ = kies een clean/radio-versie** (check de tekst voor 14–18 j.). Vlaggen = land van de artiest.",
""]
for c in ORDER:
    title,sub=CATS[c]
    md.append(f"## {title}")
    md.append(f"*{sub}*")
    md.append("")
    for n,a,t,y,fl,cc,g in NUM:
        if cc!=c: continue
        w=" ⚠️" if g=="chk" else ""
        md.append(f"{n}. **{a}** — *{t}* ({y}, {fl}){w}")
    md.append("")
md.append("---")
md.append(f"**Totaal: 100 nummers** · {sum(1 for r in NUM if r[6]=='chk')} met ⚠️ (clean-versie kiezen).")
md.append("")
md.append("### Bewust niet opgenomen (te expliciet / narco-thematiek voor de klas)")
md.append("Bad Gyal ft. Tokischa – *Chulo*; Yng Lvcas & Peso Pluma – *La Bebe (remix)*; "
         "Fuerza Regida / Junior H – corridos; Bad Bunny – *Callaíta*; Daddy Yankee – *Gasolina*. "
         "En overwegend Engelstalig (dus geen Spaanse oefening): *Hips Don't Lie*, *Taki Taki*.")
md.append("")
md.append("### De playlist aanmaken")
md.append("1. Maak in Spotify een nieuwe **openbare** playlist «Welcome to Spanish — La playlist de la clase».")
md.append("2. Voeg de nummers hierboven toe (zoek titel + artiest).")
md.append("3. Stuur mij de **officiële deel-link** → ik vervang de placeholder in de Música-tab, de PDF-QR's en de PowerPoints.")
open(f"{ROOT}/01-cursussen/04-welcome/PLAYLIST_TOP100.md","w",encoding="utf-8").write("\n".join(md)+"\n")

nchk=sum(1 for r in NUM if r[6]=="chk")
print(f"C4_playlist.html + PLAYLIST_TOP100.md geschreven · 100 nummers · {nchk} met ⚠️")
