#!/usr/bin/env python3
# C4 — HERBRUIKBARE muziek-/cultuurcomponent «Música en español».
# Bevat: Los artistas (fiches, foto's gelift uit de U4-pagina), de klas-Spotify-playlist,
# LyricsTraining-spellen, en een thema-mapping zodat élke survival-les het juiste nummer
# eruit haalt (banda_block(tema)). Standalone HTML (C4-rood) + herbruikbaar blok per les.
import json, base64, os
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])
FOTOS=json.load(open(f"{ROOT}/03-build/web/componentes/c4_musica_fotos.json"))

SPOTIFY="37i9dQZF1DXaxEKcoCdWHD"   # klas-playlist (embed)
# LyricsTraining (klaar): song -> url
LT={"la-perla":"https://lyricstraining.com/es/play/glzhbWmial","me-gustas-tu":"https://lyricstraining.com/es/play/HhbW8nMHwh"}

# artiesten: key(=fotonaam), vlag, país, género, canción, dato, bio_es, bio_nl, temas
ART=[
 ("Bad Bunny","🇵🇷","Puerto Rico","urbano · reguetón/trap","«Baile inolvidable»","Es el artista más escuchado del mundo en Spotify (¡tres veces!).",
  "Bad Bunny es de Puerto Rico. Su música urbana (reguetón y trap) suena en todo el mundo.","Bad Bunny komt uit Puerto Rico; zijn urban muziek (reggaetón & trap) klinkt wereldwijd.",["ropa","restaurante"]),
 ("Rosalía","🇪🇸","España","flamenco + pop moderno","«La Perla» (LUX, 2025)","«La Perla» fue número 1 en España.",
  "Rosalía es de España. Mezcla el flamenco tradicional con la música moderna.","Rosalía uit Spanje mengt traditionele flamenco met moderne muziek.",["familia","saludos"]),
 ("Karol G","🇨🇴","Colombia","reguetón","«Si antes te hubiera conocido»","Es una de las artistas más famosas de Latinoamérica.",
  "Karol G es de Colombia y canta reguetón.","Karol G komt uit Colombia en zingt reggaetón.",["ropa","nacionalidades"]),
 ("Aitana","🇪🇸","España","pop","«6 de febrero»","Es muy popular entre los jóvenes.",
  "Aitana es una cantante de pop de España.","Aitana is een popzangeres uit Spanje, populair bij jongeren.",["presentaciones","planes"]),
 ("Quevedo","🇪🇸","España","urbano","«Bzrp Music Session #52»","Su sesión con Bizarrap fue número 1 mundial en Spotify.",
  "Quevedo es de España (Canarias) y hace música urbana.","Quevedo (Canarische Eilanden) maakt urban muziek.",["planes","horas"]),
 ("Feid","🇨🇴","Colombia","reguetón","«Luna»","Su color es el verde: «Ferxxo».",
  "Feid es de Colombia; su música es reguetón.","Feid uit Colombia; reggaetón, herkenbaar aan de kleur groen.",["ropa"]),
 ("Rauw Alejandro","🇵🇷","Puerto Rico","urbano · pop","«Todo de ti»","Mezcla reguetón con pop y baile.",
  "Rauw Alejandro es de Puerto Rico.","Rauw Alejandro komt uit Puerto Rico; mengt reggaetón met pop.",["ropa","tiempo"]),
 ("Shakira","🇨🇴","Colombia","pop latino","«Hips Don't Lie»","Es una superestrella desde hace más de 20 años.",
  "Shakira es de Colombia y canta en español e inglés.","Shakira uit Colombia zingt in het Spaans én Engels.",["nacionalidades","familia"]),
 ("Enrique Iglesias","🇪🇸","España","pop latino","«Bailando»","Uno de los cantantes españoles más famosos del mundo.",
  "Enrique Iglesias es de España; «Bailando» es un éxito mundial.","Enrique Iglesias uit Spanje; «Bailando» is een wereldhit.",["tiempo","ropa"]),
 ("Luis Fonsi","🇵🇷","Puerto Rico","pop latino","«Despacito»","«Despacito» fue un éxito mundial gigantesco.",
  "Luis Fonsi es de Puerto Rico; su canción «Despacito» fue un éxito mundial.","Luis Fonsi uit Puerto Rico; «Despacito» was een enorme wereldhit.",["tiempo","saludos"]),
 ("Juanes","🇨🇴","Colombia","rock/pop latino","«La Camisa Negra»","Ha ganado muchos premios Grammy Latinos.",
  "Juanes es de Colombia; mezcla rock y ritmos latinos.","Juanes uit Colombia; mengt rock met Latijnse ritmes.",["ropa","nacionalidades"]),
 ("Manu Chao","🇪🇸","España/Francia","mestizo/rock","«Me gustas tú»","«Me gustas tú» repite todo el tiempo «me gusta…»: ideal para practicar.",
  "Manu Chao tiene raíces españolas y francesas.","Manu Chao heeft Spaanse en Franse roots.",["saludos","presentaciones"]),
]
# thema -> aanbevolen nummer(s) (survival-lessen halen hieruit)
TEMA_TITELS={"presentaciones":"Presentaciones","saludos":"Saludos","nacionalidades":"Nacionalidades y países","familia":"La familia",
 "objetos":"Objetos cotidianos","casa":"La casa","profesiones":"Las profesiones","horas":"Las horas","planes":"Planes y obligaciones",
 "tareas":"En casa (tareas)","tiempo":"El tiempo","ropa":"La ropa / fiesta","mercado":"En el mercado","restaurante":"En el restaurante","hotel":"En el hotel"}

# thema -> unit-EIGEN cultuurluik (Español + NL). Maakt de Cultura-tab per unit onderscheidend
# (§12 La Ruta: elke parada verankert de cultuur in een echt thema/plek). Geen entry = geen blok
# (zo blijft U1 ongewijzigd). Elk item: (icoon, titel_es, tekst_es, tekst_nl).
CULTURA={
 "presentaciones":{
   "intro":"Als je je voorstelt, hoor je meteen iets over iemands achtergrond. Zo werken namen in de Spaanstalige wereld.",
   "cards":[
     ("📛","Dos apellidos","Casi todos tienen <b>dos apellidos</b>: el del padre y el de la madre (p. ej. García Márquez).",
      "Bijna iedereen heeft <b>twee achternamen</b>: die van de vader én die van de moeder (bv. García <i>Márquez</i>)."),
     ("🎉","El santo","Además del cumpleaños, muchos celebran <b>el día de su santo</b> (el santo con su nombre).",
      "Naast je verjaardag vieren velen ook <b>hun naamdag</b> (de heilige met dezelfde naam)."),
     ("🌍","Nombres del mundo","Nombres como <b>Sofía, Mateo, Lucía, Diego</b> son populares en España y Latinoamérica.",
      "Namen als <b>Sofía, Mateo, Lucía, Diego</b> zijn populair in heel de Spaanstalige wereld — je cast-reisgenoten dragen ze."),
     ("🤝","Mucho gusto","Al conocer a alguien: <b>«Encantado/a»</b> o <b>«Mucho gusto»</b> + a menudo dos besos.",
      "Bij een kennismaking: <b>«Encantado/a»</b> of <b>«Mucho gusto»</b>, vaak met twee kussen."),
   ],
   "dato":"¿Sabías que…? En español el apellido de la madre no desaparece: los dos apellidos pasan a los hijos. Por eso mucha gente comparte apellidos… ¡pero no siempre son familia!",
 },
 "nacionalidades":{
   "intro":"El español is één taal die 21 landen verbindt — van Europa tot Amerika en zelfs Afrika. Eén taal, veel accenten en culturen.",
   "cards":[
     ("🌍","21 países","El español es lengua oficial en <b>21 países</b> y lo hablan más de <b>490 millones</b> de personas.",
      "Spaans is officiële taal in <b>21 landen</b> en wordt door meer dan <b>490 miljoen</b> mensen gesproken — de op één na meest gesproken moedertaal ter wereld."),
     ("🇬🇶","¿Español en África?","<b>Guinea Ecuatorial</b> es el único país africano donde el español es oficial.",
      "<b>Equatoriaal-Guinea</b> is het enige Afrikaanse land waar Spaans officieel is — een verrassing voor velen."),
     ("🗣️","Un idioma, muchos acentos","Un mexicano, un argentino y un español hablan el mismo idioma… ¡pero suenan muy distinto!",
      "Een Mexicaan, een Argentijn en een Spanjaard spreken dezelfde taal… maar klinken heel verschillend (de <i>c/z</i>, de <i>ll</i>, het ritme)."),
     ("🇧🇪","¿Y tú?","En Bélgica hablamos neerlandés, francés y alemán — y ahora también <b>un poco de español</b>.",
      "In België spreken we Nederlands, Frans en Duits — en nu ook <b>een beetje Spaans</b>. Jij hoort er ook bij op de kaart!"),
   ],
   "dato":"¿Sabías que…? El gentilicio se escribe con minúscula: soy belga, hablo neerlandés. Y «americano» no significa solo «de EE. UU.»: ¡toda América (del Norte, Central y del Sur) es América!",
 },
 "saludos":{
   "intro":"Un saludo zegt veel over een cultuur: hoe dichtbij, hoe warm, hoeveel contact. Kijk hoe men groet in de Spaanstalige wereld.",
   "cards":[
     ("😘","Dos besos","En España, entre amigos y familia, se dan <b>dos besos</b> (primero en la mejilla izquierda).",
      "In Spanje geef je vrienden en familie <b>twee kussen</b> (eerst op de linkerwang). Twee jongens geven meestal een hand of een <i>abrazo</i>."),
     ("🤝","Formal o informal","Con desconocidos o personas mayores: <b>un apretón de manos</b> y <b>usted</b>.",
      "Met onbekenden of oudere mensen: een <b>handdruk</b> en je gebruikt <b>usted</b>. Onder jongeren: <i>tú</i> en losser."),
     ("🌎","En Latinoamérica","En muchos países se da <b>un solo beso</b> o <b>un abrazo</b>; cambia de país a país.",
      "In veel Latijns-Amerikaanse landen geef je <b>één kus</b> of een <b>knuffel</b> — het verschilt per land."),
     ("👋","«¡Buenas!»","Forma corta e informal de <b>buenos días / buenas tardes</b>, útil a cualquier hora.",
      "Korte, informele vorm van <i>buenos días/tardes</i> — handig op elk moment van de dag."),
   ],
   "dato":"¿Sabías que…? En español el saludo cambia con la hora: buenos días (mañana) · buenas tardes (tarde) · buenas noches (noche). ¡Y «buenas noches» sirve para llegar y para despedirse!",
 },
}
def cultura_block(tema):
    c=CULTURA.get(tema)
    if not c: return ""
    cards="".join(
      f'<div class="cult"><div class="cult-ic">{ic}</div><div class="cult-b">'
      f'<div class="cult-t">{t_es}</div><div class="cult-es">{es}</div><div class="cult-nl">{nl}</div></div></div>'
      for ic,t_es,es,nl in c["cards"])
    return (f'<h2 class="sec">Cultura · {TEMA_TITELS.get(tema,tema)} 🌍</h2>'
            f'<p class="lead">{c["intro"]}</p>'
            f'<div class="cultgrid">{cards}</div>'
            f'<div class="card cult-dato">💡 {c["dato"]}</div>')

CSS=FONTS+"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--card:#fff;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif;--hand:'Caveat',cursive}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#181513;--crema:#241C1B;--gt:#3A1E20;--line:#3a302e;--card:#211a19}
*{box-sizing:border-box}body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
header.top{position:sticky;top:0;z-index:20;background:var(--g);color:#fff;box-shadow:0 2px 10px #0002}
.bar{max-width:1080px;margin:0 auto;padding:11px 18px;display:flex;align-items:center;gap:12px}
.brand{font-family:var(--disp);font-weight:800;font-size:20px}.brand small{font-weight:400;opacity:.9;font-size:12px}
.themebtn{margin-left:auto;border:none;background:#ffffff22;color:#fff;width:34px;height:34px;border-radius:50%;cursor:pointer;font-size:15px}
main{max-width:1080px;margin:0 auto;padding:0 18px 80px}
.hero{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;border-radius:20px;padding:24px 26px;margin:20px 0}
.hero h1{font-family:var(--disp);font-weight:800;font-size:30px;margin:0 0 4px}.hero p{margin:0;max-width:640px;opacity:.96}
h2.sec{font-family:var(--disp);font-weight:700;color:var(--gd);font-size:24px;margin:26px 0 6px}
.lead{color:var(--mut);max-width:720px;margin:0 0 12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin:14px 0}
.artgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}
.art{border:1px solid var(--line);border-radius:16px;padding:14px;background:var(--card);display:flex;flex-direction:column;gap:6px}
.art .top{display:flex;gap:12px;align-items:center}
.art img{width:64px;height:64px;border-radius:12px;object-fit:cover;flex:none}
.art .nm{font-family:var(--disp);font-weight:800;font-size:17px}
.art .meta{font-size:12px;color:var(--mut)}
.art .song{font-weight:700;color:var(--gd);font-size:14px}
.art .bio{font-size:13px}.art .bio .nl{color:var(--mut);font-style:italic;display:block;margin-top:2px}
.art .dato{font-size:12px;background:var(--gt);color:var(--gd);border-radius:8px;padding:6px 9px}
.art .tags{display:flex;gap:5px;flex-wrap:wrap;margin-top:auto}
.tag{font-size:10px;background:var(--crema);border-radius:20px;padding:2px 8px;color:var(--ink)}
.spotwrap{border-radius:14px;overflow:hidden;border:1px solid var(--line);margin:10px 0}
.btn{display:inline-flex;align-items:center;gap:8px;border:none;background:var(--g);color:#fff;font-weight:700;border-radius:10px;padding:9px 15px;cursor:pointer;font-family:var(--disp);font-size:14px;text-decoration:none}
.btn.lt{background:#1DB954}
.mapt{width:100%;border-collapse:collapse;font-size:13.5px;margin-top:6px}
.mapt th,.mapt td{border-bottom:1px solid var(--line);padding:7px 9px;text-align:left}.mapt th{background:var(--gt);color:var(--gd)}
.pill{display:inline-block;background:var(--gt);color:var(--gd);border-radius:20px;padding:3px 10px;font-size:12px;font-weight:700}
.foot{color:var(--mut);font-size:12px;text-align:center;margin-top:30px}
/* unit-eigen Cultura-luik */
.cultgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}
.cult{display:flex;gap:12px;background:var(--card);border:1px solid var(--line);border-left:4px solid var(--g);border-radius:16px;padding:14px 16px}
.cult-ic{font-size:30px;flex:none;line-height:1.1}
.cult-t{font-family:var(--disp);font-weight:800;font-size:16px;color:var(--gd);margin-bottom:2px}
.cult-es{font-size:13px}.cult-nl{font-size:12.5px;color:var(--mut);font-style:italic;margin-top:3px}
.cult-dato{background:var(--gt);border:1px solid var(--line);font-size:13.5px;color:var(--ink);margin-top:14px}
"""

def art_card(a):
    key,fl,pais,gen,song,dato,bes,bnl,temas=a
    foto=FOTOS.get(key,"")
    tags="".join(f'<span class="tag">{TEMA_TITELS.get(t,t)}</span>' for t in temas)
    return (f'<div class="art"><div class="top"><img src="{foto}" alt="{key}" loading="lazy">'
      f'<div><div class="nm">{fl} {key}</div><div class="meta">{pais} · {gen}</div><div class="song">🎵 {song}</div></div></div>'
      f'<div class="dato">💡 {dato}</div><div class="bio">{bes}<span class="nl">{bnl}</span></div><div class="tags">{tags}</div></div>')

def lt_button(song_key,label):
    return f'<a class="btn lt" href="{LT[song_key]}" target="_blank" rel="noopener">▶ Completar «{label}» en LyricsTraining</a>'

# ---- herbruikbaar blok per les ----
def banda_block(tema):
    """Geeft het «banda sonora»-blok voor één survival-les: aanbevolen nummer(s) + LyricsTraining/Spotify."""
    picks=[a for a in ART if tema in a[8]]
    if not picks: picks=[ART[0]]
    a=picks[0]
    lt=""
    if tema in ("familia","saludos") and "la-perla" in LT and a[0]=="Rosalía": lt=lt_button("la-perla","La Perla")
    if a[0]=="Manu Chao": lt=lt_button("me-gustas-tu","Me gustas tú")
    return (f'<div class="card"><span class="pill">La banda sonora 🎧</span>'
      f'<h3 style="font-family:var(--disp);color:var(--gd);margin:8px 0 4px">{a[3].split(" ")[0].title()} — {a[0]} · {a[4]}</h3>'
      f'<p class="lead" style="margin:0 0 8px">Luister het nummer van deze les op de klas-playlist. {a[7]}</p>'
      f'<div class="spotwrap"><iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/{SPOTIFY}" width="100%" height="152" frameborder="0" allow="encrypted-media"></iframe></div>'
      +(lt or "")+'</div>')

ARTGRID="".join(art_card(a) for a in ART)
MAProws="".join(f'<tr><td>{TEMA_TITELS[t]}</td><td>{", ".join(a[0]+" · "+a[4] for a in ART if t in a[8]) or "—"}</td></tr>' for t in TEMA_TITELS)

TEMA=os.environ.get("C4_TEMA","presentaciones")   # thema van deze unit → bepaalt de banda sonora van de les (per unit via env)
HTML=f"""<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · Música en español</title>
<style>{CSS}</style></head><body>
<header class="top"><div class="bar"><div class="brand">Música en español <small>· C4</small></div>
<button class="themebtn" onclick="document.documentElement.dataset.theme=document.documentElement.dataset.theme==='dark'?'light':'dark'">◐</button></div></header>
<main>
 <div class="hero"><h1>La banda sonora 🎧</h1><p>Spaanstalige muziek klinkt over de hele wereld. Ontdek de artiesten van het moment, luister de klas-playlist, en vul de liedjes aan in LyricsTraining.</p></div>

 {cultura_block(TEMA)}

 <h2 class="sec">La banda sonora de esta unidad 🎶</h2>
 <p class="lead">Het nummer bij deze les — luister mee en pik nieuwe woorden op.</p>
 {banda_block(TEMA)}

 <h2 class="sec">Los artistas 🎤</h2>
 <p class="lead">Lees de fiches (Spaans + Nederlands), bekijk de clips en beluister de playlist.</p>
 <div class="artgrid">{ARTGRID}</div>

 <h2 class="sec">La playlist de la clase 🎧</h2>
 <div class="spotwrap"><iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/{SPOTIFY}" width="100%" height="352" frameborder="0" allow="encrypted-media"></iframe></div>

 <h2 class="sec">Canta y completa · LyricsTraining ✍️</h2>
 <p class="lead">Luister en vul de ontbrekende woorden in — leuk om je oor te trainen.</p>
 <div class="card" style="display:flex;gap:10px;flex-wrap:wrap">{lt_button("la-perla","La Perla — Rosalía")}{lt_button("me-gustas-tu","Me gustas tú — Manu Chao")}</div>

 <div class="foot">C4 · «Welcome to Spanish» · Música en español 🎧</div>
</main></body></html>"""

os.makedirs(f"{ROOT}/03-build/web/componentes",exist_ok=True)
OUT=os.environ.get("C4_MUSICA_OUT","C4_musica.html")   # per unit via env; default = gedeeld U1-bestand
open(f"{ROOT}/03-build/web/componentes/{OUT}","w").write(HTML)
print(f"{OUT} geschreven:",len(HTML),"bytes ·",len(ART),"artiesten · tema=",TEMA)
