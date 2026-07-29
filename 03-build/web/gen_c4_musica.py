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
  "Rosalía es de España. Mezcla el flamenco tradicional con la música moderna.","Rosalía uit Spanje mengt traditionele flamenco met moderne muziek.",["familia","saludos","profesiones"]),
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
  "Manu Chao tiene raíces españolas y francesas.","Manu Chao heeft Spaanse en Franse roots.",["saludos","presentaciones","objetos","casa","tareas"]),
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
 "familia":{
   "intro":"De familie staat centraal in de Spaanstalige cultuur — vaak groot, warm en dichtbij. Zo praat men over «la familia».",
   "cards":[
     ("👨‍👩‍👧‍👦","La familia unida","In veel Spaanstalige landen wonen <b>drie generaties</b> dicht bij elkaar; <b>los abuelos</b> spelen een grote rol.",
      "In veel Spaanstalige landen leven <b>drie generaties</b> dicht bij elkaar; <b>grootouders</b> (los abuelos) zijn heel belangrijk."),
     ("🍚","La sobremesa","Na het eten blijft de familie lang aan tafel praten: <b>la sobremesa</b>.",
      "Na het eten blijft de familie lang napraten aan tafel — dat heet <b>la sobremesa</b>, een echte familietraditie."),
     ("💃","Frida &amp; su familia","La pintora <b>Frida Kahlo</b> pintó «Mi familia» (Mis abuelos, mis padres y yo).",
      "Schilderes <b>Frida Kahlo</b> maakte een beroemd schilderij van haar stamboom: «Mis abuelos, mis padres y yo»."),
     ("🇧🇪","¿Y tu familia?","Grande o pequeña, cada familia es especial. ¿Cómo es la tuya?",
      "Groot of klein, elke familie is bijzonder. Hoe ziet <b>jouw</b> familie eruit? (Straks maak je je eigen <i>árbol de familia</i>.)"),
   ],
   "dato":"¿Sabías que…? Casi todos tienen dos apellidos (del padre y de la madre) — así que el apellido de la madre nunca se pierde en la familia.",
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
 "objetos":{
   "intro":"Sommige alledaagse voorwerpen zijn echte iconen van de Spaanstalige cultuur. Elk voorwerp «sirve para» iets — en vertelt een verhaal.",
   "cards":[
     ("🎸","La guitarra española","La <b>guitarra española</b> (o flamenca) nació en España y sirve para tocar flamenco y muchos otros estilos.",
      "De <b>Spaanse (flamenco)gitaar</b> ontstond in Spanje en «sirve para» flamenco én talloze andere stijlen te spelen — een wereldwijd symbool."),
     ("🧉","El mate","En Argentina, Uruguay y Paraguay, el <b>mate</b> es una bebida que se comparte: la misma taza pasa de mano en mano.",
      "In Argentinië, Uruguay en Paraguay is de <b>mate</b> een drank die je <i>deelt</i>: dezelfde beker gaat van hand tot hand — «sirve para compartir»."),
     ("🪅","La piñata","En México, la <b>piñata</b> es un objeto de fiesta lleno de dulces; sirve para celebrar los cumpleaños.",
      "In Mexico is de <b>piñata</b> een feestvoorwerp vol snoep; «sirve para» verjaardagen te vieren — je slaat ze stuk met een stok."),
     ("🛖","La hamaca","La <b>hamaca</b> (una palabra taína del Caribe) sirve para descansar… ¡como el sofá de Julio!",
      "De <b>hangmat</b> (<i>hamaca</i>, een Taíno-woord uit de Cariben) «sirve para descansar» — net als de bank van Julio in de video."),
   ],
   "dato":"¿Sabías que…? Muchas palabras de objetos vienen de lenguas indígenas de América: «hamaca», «canoa» y «chocolate» pasaron del taíno y del náhuatl al español… y luego a medio mundo.",
 },
 "casa":{
   "intro":"Een huis vertelt veel over een cultuur: hoe men samenleeft, waar men rust, welke kleuren men kiest. Zo wonen mensen in de Spaanstalige wereld.",
   "cards":[
     ("🌿","El patio","In veel Spaanse en Latijns-Amerikaanse huizen is er een <b>patio</b>: een binnenkoer vol planten, het hart van het huis.",
      "In veel Spaanse en Latijns-Amerikaanse huizen is er een <b>patio</b> (binnenkoer) vol planten — de centrale, gezellige plek van het huis."),
     ("🎨","Casas de colores","In <b>Guanajuato</b> (🇲🇽), <b>Cartagena</b> (🇨🇴) en <b>Guatapé</b> schilderen mensen hun huizen in <b>felle kleuren</b>.",
      "In steden als <b>Guanajuato</b> (Mexico), <b>Cartagena</b> (Colombia) en <b>Guatapé</b> zijn de huizen geschilderd in <b>felle kleuren</b> — een kleurrijk straatbeeld."),
     ("🛋️","La sobremesa en casa","Thuis blijft men na het eten lang aan tafel praten: de <b>sobremesa</b> — het huis is een plek om samen te zijn.",
      "Thuis blijft de familie na het eten lang natafelen (<b>la sobremesa</b>): het huis draait om samenzijn, niet enkel om ruimtes."),
     ("😴","La siesta","In warme streken rust men midden op de dag — de <b>siesta</b>. Even alles dicht, dan weer open.",
      "In warme streken rust men midden op de dag: de <b>siesta</b>. Rond 14–17u sluiten sommige winkels; daarna gaat alles weer open."),
   ],
   "dato":"¿Sabías que…? «Estar en casa» (thuis zijn) en «ir a casa» (naar huis gaan) gebruik je zónder lidwoord — net als in het Nederlands zeg je «naar huis», niet «naar het huis».",
 },
 "profesiones":{
   "intro":"Werk en beroep klinken anders in elke cultuur — van de siësta-mythe tot wereldberoemde beroepen. Zo werkt de Spaanstalige wereld.",
   "cards":[
     ("💼","Soy profesor — sin «un»","En español dices <b>soy profesor</b>, <b>es actriz</b> — ¡sin «un/una»!",
      "In het Spaans zeg je <b>soy profesor</b>, <b>es actriz</b> — zónder «un/una» (anders dan in het Engels «I'm A teacher»)."),
     ("🎨","Profesiones famosas","Frida Kahlo era <b>pintora</b>, García Márquez <b>escritor</b>, Messi es <b>futbolista</b> y Rosalía es <b>cantante</b>.",
      "Beroemde Spaanstaligen per beroep: Frida Kahlo <b>pintora</b> (schilderes), García Márquez <b>escritor</b>, Messi <b>futbolista</b>, Rosalía <b>cantante</b>."),
     ("⏰","El horario partido","En España muchas tiendas cierran de 14 a 17 h (el <b>horario partido</b>) y se trabaja hasta las 20 h.",
      "In Spanje sluiten veel winkels tussen 14 en 17 u (de <b>gedeelde werkdag</b>) en werkt men daarna tot ± 20 u — dineren pas om 21–22 u!"),
     ("🗣️","¿A qué te dedicas?","La pregunta clásica al conocer a alguien: <b>¿A qué te dedicas?</b> o <b>¿En qué trabajas?</b>",
      "Dé klassieke kennismakingsvraag: <b>¿A qué te dedicas?</b> («waaraan wijd je je?») of <b>¿En qué trabajas?</b> — beleefd én nieuwsgierig."),
   ],
   "dato":"¿Sabías que…? Veel beroepsnamen hebben een eigen ♀-vorm: profesor/profesora · escritor/escritora · actor/actriz · dependiente/dependienta. Sommige blijven gelijk: el/la estudiante, el/la periodista.",
 },
 "horas":{
   "intro":"De klok tikt anders in de Spaanstalige wereld: later eten, later uitgaan, en een eigen manier om de tijd te zeggen. Zo werkt de dag.",
   "cards":[
     ("🍽️","Se come a las dos","En España se come a las <b>14 h</b> y se cena a las <b>21–22 h</b>. En México se almuerza fuerte a las 14–15 h.",
      "In Spanje eet men warm rond <b>14 u</b> en avondmaal pas om <b>21–22 u</b> — voor Vlamingen bijzonder laat! In Mexico is de lunch (14–15 u) de hoofdmaaltijd."),
     ("🕐","«La una» es especial","Solo la <b>una</b> va en singular: <b>es la</b> una. Todas las demás: <b>son las</b> dos, tres, cuatro…",
      "Alleen bij <b>één uur</b> gebruik je enkelvoud: <b>es la</b> una. Alle andere uren: <b>son las</b> dos, tres… (meervoud!)."),
     ("🌙","«Buenas noches» a las 22 h","La <b>tarde</b> dura hasta las 20–21 h; después empieza la <b>noche</b>. ¡La tarde es muy larga!",
      "De <b>tarde</b> loopt door tot 20–21 u; pas dan begint de <b>noche</b>. Daarom zeg je om 19 u nog «buenas tardes» — een lange namiddag dus."),
     ("📅","Los días en minúscula","Los días se escriben con <b>minúscula</b>: lunes, martes… Y «op maandag» = <b>el</b> lunes (sin «en»).",
      "Dagen schrijf je met een <b>kleine letter</b> (lunes, martes…). En «op maandag» is <b>el</b> lunes — géén «en» ervoor, anders dan je verwacht."),
   ],
   "dato":"¿Sabías que…? «Half negen» is in het Spaans <b>las ocho y media</b>: het Spaans kijkt <i>terug</i> naar het vorige uur (acht + dertig), terwijl het Nederlands vóóruit kijkt naar negen. Dé klassieke valstrik!",
 },
 "planes":{
   "intro":"Plannen maken klinkt anders in het Spaans — en het weekend begint er later. Zo ziet een <i>finde</i> in de Spaanstalige wereld eruit.",
   "cards":[
     ("🌙","Salir tarde","En España la gente <b>queda</b> a las 22–23 h para salir; los conciertos empiezan tarde.",
      "In Spanje spreekt men vaak pas om <b>22–23 u</b> af om uit te gaan; concerten beginnen laat en de nacht duurt lang."),
     ("🌉","Hacer puente","Si una fiesta cae en jueves, muchos <b>hacen puente</b>: también libran el viernes.",
      "Valt een feestdag op donderdag, dan «maakt men een brug» (<b>hacer puente</b>): ook de vrijdag vrij — een lang weekend."),
     ("🗓️","El «finde»","<b>El finde</b> = el fin de semana. Los jóvenes dicen: «¿Qué haces el finde?»",
      "<b>El finde</b> is de gewone spreektaalafkorting van <i>el fin de semana</i>. Jongeren zeggen: «¿Qué haces el finde?»"),
     ("👨‍👩‍👧","Planes en familia","El domingo suele ser el día de la <b>comida familiar</b> — un plan fijo para muchos.",
      "De zondag is bij veel families de dag van de <b>familiemaaltijd</b> — een vast plan, vaak met de hele familie samen."),
   ],
   "dato":"¿Sabías que…? Om een plan te maken gebruik je <b>ir a + infinitivo</b>: «voy a estudiar» = ik ga studeren — net zoals in het Nederlands. Maar «ik moet werken» wordt <b>tengo que trabajar</b>, letterlijk «ik heb te werken».",
 },
 "tareas":{
   "intro":"Wie doet wat in huis? Dat verschilt per gezin en per land — en het is aan het veranderen. Zo zit het in de Spaanstalige wereld.",
   "cards":[
     ("🧹","«Los hombres también»","En la escena Julio dice: «yo no soy machista, los hombres <b>también</b> sabemos pasar la aspiradora».",
      "In de scène zegt Julio: «ik ben niet machistisch, wij mannen kunnen óók stofzuigen». Het <b>verdelen van huistaken</b> is in Spanje sterk veranderd: jonge koppels delen veel meer dan hun grootouders — al is het nog niet overal gelijk."),
     ("📋","El reparto de tareas","Muchas familias hacen un <b>cuadro de tareas</b>: quién friega, quién ordena, quién pasa la aspiradora.",
      "Veel gezinnen maken een <b>takenschema</b> (cuadro de tareas): wie doet de vaat, wie ruimt op, wie stofzuigt. Precies wat jullie in de eindtaak gaan doen."),
     ("🧽","La asistenta","En la academia esperan a la <b>asistenta</b>. En varios países de Latinoamérica tener ayuda en casa es más habitual que en Bélgica.",
      "In de scène wachten ze op de <b>asistenta</b> (poetshulp). In verschillende Latijns-Amerikaanse landen is huishoudhulp gebruikelijker dan bij ons — vaak omdat lonen en kosten er anders liggen."),
     ("🇧🇪","¿Y en tu casa?","¿Quién limpia? ¿Quién cocina? ¿Sabes cocinar o planchar?",
      "En bij jou thuis? Wie poetst, wie kookt? En wat kan <b>jij</b> al: koken, strijken, stofzuigen? Daarover ga je straks in het Spaans praten."),
   ],
   "dato":"¿Sabías que…? Er zijn twee manieren om «moeten» te zeggen: <b>tengo que</b> limpiar (ík moet) is persoonlijk, <b>hay que</b> limpiar (er moet gepoetst worden) is algemeen — handig als je niet wil zeggen wíe het moet doen!",
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
