#!/usr/bin/env python3
# Motor-content-JSON's voor C6+ · U5 «Érase una vez» (biografía · indefinido · fuertes · se lo).
# Templates: memory·match·classify·cloze·tetris·order·point·speak. Pools >=12; rounds lager => andere reeks.
# Indefinido-vormen nagerekend. Slug-prefix = es-c6plus-u5-.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")
def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2)); print("wrote", os.path.basename(p))
G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0","magenta":"#B4309A"}
PRE = "es-c6plus-u5-"

# 1 · MEMORY — biografía ES ↔ NL (pool 14)
w({"id":PRE+"biografia-memoria","title":"Memoria de la vida","subtitle":"U5 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: biografía + vertaling","pairs":[
  {"a":"nacer","b":"geboren worden"},{"a":"crecer","b":"opgroeien"},{"a":"casarse","b":"trouwen"},
  {"a":"morir","b":"sterven"},{"a":"ganar","b":"winnen"},{"a":"escribir","b":"schrijven"},
  {"a":"pintar","b":"schilderen"},{"a":"descubrir","b":"ontdekken"},{"a":"el premio","b":"de prijs"},
  {"a":"el éxito","b":"het succes"},{"a":"la vida","b":"het leven"},{"a":"famoso","b":"beroemd"},
  {"a":"mudarse","b":"verhuizen"},{"a":"componer","b":"componeren"}]}})

# 2 · MEMORY — oficios ES ↔ NL (pool 12)
w({"id":PRE+"persona-memoria","title":"Memoria de oficios","subtitle":"U5 · koppel het beroep aan de vertaling",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: oficio + vertaling","pairs":[
  {"a":"el escritor","b":"de schrijver"},{"a":"la pintora","b":"de schilderes"},{"a":"el cantante","b":"de zanger"},
  {"a":"el futbolista","b":"de voetballer"},{"a":"el científico","b":"de wetenschapper"},{"a":"el artista","b":"de kunstenaar"},
  {"a":"el líder","b":"de leider"},{"a":"el personaje","b":"het personage"},{"a":"la leyenda","b":"de legende"},
  {"a":"la historia","b":"het verhaal"},{"a":"el premio","b":"de prijs"},{"a":"el éxito","b":"het succes"}]}})

# 3 · MATCH — infinitivo ↔ indefinido (él) (pool 14)
w({"id":PRE+"verbo-indefinido","title":"Verbo e indefinido","subtitle":"U5 · koppel de infinitief aan de él-vorm",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind de infinitief met de indefinido (él/ella)","pairs":[
  {"a":"nacer","b":"nació"},{"a":"escribir","b":"escribió"},{"a":"ganar","b":"ganó"},
  {"a":"ser / ir","b":"fue ⭐"},{"a":"hacer","b":"hizo ⭐"},{"a":"tener","b":"tuvo ⭐"},
  {"a":"estar","b":"estuvo ⭐"},{"a":"decir","b":"dijo ⭐"},{"a":"venir","b":"vino ⭐"},
  {"a":"dar","b":"dio ⭐"},{"a":"ver","b":"vio ⭐"},{"a":"vivir","b":"vivió"},
  {"a":"pintar","b":"pintó"},{"a":"estudiar","b":"estudió"}]}})

# 4 · CLASSIFY — ¿regular o irregular? (pool 16, rounds 10)
w({"id":PRE+"indef-tipo","title":"¿regular o irregular?","subtitle":"U5 · welk soort indefinido?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Is de indefinido regelmatig of een sterke vorm (irregular)?","categories":[
  {"id":"reg","label":"regular<br><small>-ó / -ió</small>","glaze":G["teal"]},
  {"id":"irr","label":"irregular<br><small>fue, hizo…</small>","glaze":G["purple"]}],
 "items":[
  {"stimulus":"nacer → nació","answer":"reg","tag":"reg","sub":"-er regular"},
  {"stimulus":"hacer → hizo","answer":"irr","tag":"irr","sub":"fuerte"},
  {"stimulus":"escribir → escribió","answer":"reg","tag":"reg","sub":"-ir regular"},
  {"stimulus":"ser → fue","answer":"irr","tag":"irr","sub":"fuerte"},
  {"stimulus":"ganar → ganó","answer":"reg","tag":"reg","sub":"-ar regular"},
  {"stimulus":"tener → tuvo","answer":"irr","tag":"irr","sub":"fuerte"},
  {"stimulus":"estudiar → estudió","answer":"reg","tag":"reg","sub":"-ar regular"},
  {"stimulus":"decir → dijo","answer":"irr","tag":"irr","sub":"fuerte"},
  {"stimulus":"vivir → vivió","answer":"reg","tag":"reg","sub":"-ir regular"},
  {"stimulus":"estar → estuvo","answer":"irr","tag":"irr","sub":"fuerte"},
  {"stimulus":"pintar → pintó","answer":"reg","tag":"reg","sub":"-ar regular"},
  {"stimulus":"venir → vino","answer":"irr","tag":"irr","sub":"fuerte"},
  {"stimulus":"componer → compuso","answer":"irr","tag":"irr","sub":"fuerte (poner)"},
  {"stimulus":"ir → fue","answer":"irr","tag":"irr","sub":"fuerte"},
  {"stimulus":"comer → comió","answer":"reg","tag":"reg","sub":"-er regular"},
  {"stimulus":"dar → dio","answer":"irr","tag":"irr","sub":"fuerte"}]}})

# 5 · CLASSIFY — ¿presente o pasado? (pool 16, rounds 10)
w({"id":PRE+"presente-pasado","title":"¿presente o pasado?","subtitle":"U5 · nu (presente) of afgerond verleden (indefinido)?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Is de zin in het presente of in de indefinido (verleden)?","categories":[
  {"id":"pres","label":"presente<br><small>ahora</small>","glaze":G["teal"]},
  {"id":"pas","label":"indefinido<br><small>ayer, en 1919</small>","glaze":G["purple"]}],
 "items":[
  {"stimulus":"Ayer estudié mucho.","answer":"pas","tag":"pas","sub":"ayer → indefinido"},
  {"stimulus":"Hoy estudio en casa.","answer":"pres","tag":"pres","sub":"hoy → presente"},
  {"stimulus":"Nació en 1927.","answer":"pas","tag":"pas","sub":"en 1927 → indefinido"},
  {"stimulus":"Vive en Buenos Aires.","answer":"pres","tag":"pres","sub":"presente"},
  {"stimulus":"Ganó el Mundial en 2022.","answer":"pas","tag":"pas","sub":"en 2022 → indefinido"},
  {"stimulus":"Escribo una carta.","answer":"pres","tag":"pres","sub":"presente"},
  {"stimulus":"El año pasado viajé a Perú.","answer":"pas","tag":"pas","sub":"año pasado → indefinido"},
  {"stimulus":"Trabaja de periodista.","answer":"pres","tag":"pres","sub":"presente"},
  {"stimulus":"Se casó joven.","answer":"pas","tag":"pas","sub":"indefinido"},
  {"stimulus":"Come tacos cada día.","answer":"pres","tag":"pres","sub":"cada día → presente"},
  {"stimulus":"Murió en 1954.","answer":"pas","tag":"pas","sub":"en 1954 → indefinido"},
  {"stimulus":"Hace deporte los lunes.","answer":"pres","tag":"pres","sub":"presente"},
  {"stimulus":"De repente, todo cambió.","answer":"pas","tag":"pas","sub":"de repente → indefinido"},
  {"stimulus":"Estudia medicina ahora.","answer":"pres","tag":"pres","sub":"ahora → presente"},
  {"stimulus":"Hace dos años me mudé.","answer":"pas","tag":"pas","sub":"hace dos años → indefinido"},
  {"stimulus":"Pinta cuadros modernos.","answer":"pres","tag":"pres","sub":"presente"}]}})

# 6 · CLOZE — indefinido (VERPLICHT, nagerekend) (pool 18, rounds 12)
w({"id":PRE+"indefinido","title":"Completa: el indefinido","subtitle":"U5 · una biografía",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm van de indefinido","items":[
  {"stimulus":"García Márquez ___ en Colombia.","options":["nació","nacío","naceó"],"answer":"nació","tag":"if","sub":"nacer → nació"},
  {"stimulus":"___ «Cien años de soledad».","options":["escribió","escribó","escrivió"],"answer":"escribió","tag":"if","sub":"escribir → escribió"},
  {"stimulus":"Frida Kahlo ___ autorretratos.","options":["pintó","pintió","pintaba"],"answer":"pintó","tag":"if","sub":"pintar → pintó"},
  {"stimulus":"Messi ___ el Mundial.","options":["ganó","ganió","gané"],"answer":"ganó","tag":"if","sub":"ganar → ganó"},
  {"stimulus":"(Yo) ___ mucho ayer.","options":["estudié","estudó","estudié"],"answer":"estudié","tag":"if","sub":"yo → estudié"},
  {"stimulus":"Nosotros ___ en el centro.","options":["comimos","comemos","comió"],"answer":"comimos","tag":"if","sub":"nosotros → comimos"},
  {"stimulus":"Gardel ___ en Buenos Aires.","options":["vivió","vivó","vivía"],"answer":"vivió","tag":"if","sub":"vivir → vivió"},
  {"stimulus":"Evita ___ muy importante.","options":["fue","fui","fué"],"answer":"fue","tag":"if","sub":"ser → fue"},
  {"stimulus":"Maradona ___ el «gol del siglo».","options":["hizo","hació","hizió"],"answer":"hizo","tag":"if","sub":"hacer → hizo"},
  {"stimulus":"(Yo) ___ un buen día.","options":["tuve","tení","tenió"],"answer":"tuve","tag":"if","sub":"tener → tuve"},
  {"stimulus":"Gardel ___ a París.","options":["fue","fui","fué"],"answer":"fue","tag":"if","sub":"ir → fue"},
  {"stimulus":"El equipo ___ en la final.","options":["estuvo","estó","estuvió"],"answer":"estuvo","tag":"if","sub":"estar → estuvo"},
  {"stimulus":"Ella me ___ un regalo.","options":["dio","dió","daba"],"answer":"dio","tag":"if","sub":"dar → dio"},
  {"stimulus":"El artista ___ la verdad.","options":["dijo","dició","dijió"],"answer":"dijo","tag":"if","sub":"decir → dijo"},
  {"stimulus":"¿(Tú) ___ el año pasado?","options":["viajaste","viajastes","viajó"],"answer":"viajaste","tag":"if","sub":"tú → viajaste"},
  {"stimulus":"Ellos ___ una familia.","options":["tuvieron","tenieron","tuvíeron"],"answer":"tuvieron","tag":"if","sub":"ellos → tuvieron"},
  {"stimulus":"(Yo) ___ a la ciudad.","options":["vine","viné","venió"],"answer":"vine","tag":"if","sub":"venir → vine"},
  {"stimulus":"Ella ___ un concierto.","options":["dio","dió","daba"],"answer":"dio","tag":"if","sub":"dar → dio"}]}})

# 7 · CLOZE — se lo/se la (pool 14, rounds 10)
w({"id":PRE+"se-lo","title":"Completa: se lo / se la","subtitle":"U5 · le/les + lo/la → se lo/se la",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies de juiste combinatie se + lo/la/los/las","items":[
  {"stimulus":"¿El libro a Mateo? — ___ di.","options":["Se lo","Le lo","Se la"],"answer":"Se lo","tag":"od","sub":"el libro → se lo"},
  {"stimulus":"¿La carta a Nina? — ___ mandé.","options":["Se la","Le la","Se lo"],"answer":"Se la","tag":"od","sub":"la carta → se la"},
  {"stimulus":"¿Los discos a Diego? — ___ presté.","options":["Se los","Le los","Se las"],"answer":"Se los","tag":"od","sub":"los discos → se los"},
  {"stimulus":"¿Las fotos a Valen? — ___ enseñé.","options":["Se las","Le las","Se los"],"answer":"Se las","tag":"od","sub":"las fotos → se las"},
  {"stimulus":"¿El secreto a ella? — ___ conté.","options":["Se lo","Le lo","Se la"],"answer":"Se lo","tag":"od","sub":"el secreto → se lo"},
  {"stimulus":"¿La noticia a él? — ___ dije.","options":["Se la","Le la","Se lo"],"answer":"Se la","tag":"od","sub":"la noticia → se la"},
  {"stimulus":"¿El regalo a tu madre? — ___ di.","options":["Se lo","Le lo","Se la"],"answer":"Se lo","tag":"od","sub":"el regalo → se lo"},
  {"stimulus":"¿Las llaves a tu hermano? — ___ dejé.","options":["Se las","Le las","Se los"],"answer":"Se las","tag":"od","sub":"las llaves → se las"},
  {"stimulus":"¿La verdad a ellos? — ___ conté.","options":["Se la","Les la","Se lo"],"answer":"Se la","tag":"od","sub":"les+la → se la"},
  {"stimulus":"¿El vídeo a tus amigos? — ___ mandé.","options":["Se lo","Les lo","Se la"],"answer":"Se lo","tag":"od","sub":"les+lo → se lo"},
  {"stimulus":"¿Las cartas a Frida? — ___ escribí.","options":["Se las","Le las","Se los"],"answer":"Se las","tag":"od","sub":"las cartas → se las"},
  {"stimulus":"¿El premio a la científica? — ___ dieron.","options":["Se lo","Le lo","Se la"],"answer":"Se lo","tag":"od","sub":"el premio → se lo"},
  {"stimulus":"¿La foto a Mateo? — ___ enseñé.","options":["Se la","Le la","Se lo"],"answer":"Se la","tag":"od","sub":"la foto → se la"},
  {"stimulus":"¿Los libros a Nina? — ___ presté.","options":["Se los","Le los","Se las"],"answer":"Se los","tag":"od","sub":"los libros → se los"}]}})

# 8 · TETRIS — indefinido: -ó / -ió / irregular (pool 16)
w({"id":PRE+"indef-tetris","title":"Indefinido Tetris","subtitle":"U5 · laat het juiste type vallen",
 "lang":"es","template":"tetris","options":{"rows":9,"speed":1300,"audio":False},
 "classify":{"categories":[
  {"id":"o","label":"-ó (-ar)","glaze":G["blue"]},{"id":"io","label":"-ió (-er/-ir)","glaze":G["green"]},
  {"id":"irr","label":"irregular","glaze":G["magenta"]}],
 "items":[
  {"stimulus":"ganar","answer":"o","tag":"o","sub":"ganó"},{"stimulus":"escribir","answer":"io","tag":"io","sub":"escribió"},
  {"stimulus":"hacer","answer":"irr","tag":"irr","sub":"hizo"},{"stimulus":"nacer","answer":"io","tag":"io","sub":"nació"},
  {"stimulus":"ser/ir","answer":"irr","tag":"irr","sub":"fue"},{"stimulus":"pintar","answer":"o","tag":"o","sub":"pintó"},
  {"stimulus":"tener","answer":"irr","tag":"irr","sub":"tuvo"},{"stimulus":"vivir","answer":"io","tag":"io","sub":"vivió"},
  {"stimulus":"estudiar","answer":"o","tag":"o","sub":"estudió"},{"stimulus":"decir","answer":"irr","tag":"irr","sub":"dijo"},
  {"stimulus":"comer","answer":"io","tag":"io","sub":"comió"},{"stimulus":"estar","answer":"irr","tag":"irr","sub":"estuvo"},
  {"stimulus":"cantar","answer":"o","tag":"o","sub":"cantó"},{"stimulus":"salir","answer":"io","tag":"io","sub":"salió"},
  {"stimulus":"venir","answer":"irr","tag":"irr","sub":"vino"},{"stimulus":"trabajar","answer":"o","tag":"o","sub":"trabajó"}]}})

# 9 · ORDER — ordena la biografía / la frase (8 rondes)
w({"id":PRE+"biografia-order","title":"Ordena la frase","subtitle":"U5 · zet het verhaal/de zin in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik in de logische volgorde","rounds":[
  {"tag":"bio","sub":"la vida de una figura","items":[
    {"label":"Nació en 1927.","key":1},{"label":"Estudió periodismo.","key":2},{"label":"Escribió novelas.","key":3},{"label":"Murió en 2014.","key":4}]},
  {"tag":"frase","sub":"indefinido regular","items":[
    {"label":"Frida","key":1},{"label":"pintó","key":2},{"label":"muchos","key":3},{"label":"autorretratos.","key":4}]},
  {"tag":"frase","sub":"forma fuerte","items":[
    {"label":"Messi","key":1},{"label":"fue","key":2},{"label":"campeón","key":3},{"label":"del Mundo.","key":4}]},
  {"tag":"selo","sub":"se lo","items":[
    {"label":"El libro,","key":1},{"label":"se lo","key":2},{"label":"di","key":3},{"label":"a Mateo.","key":4}]},
  {"tag":"bio","sub":"conectores","items":[
    {"label":"Primero nació,","key":1},{"label":"después estudió,","key":2},{"label":"entonces triunfó","key":3},{"label":"y al final murió famoso.","key":4}]},
  {"tag":"frase","sub":"pregunta","items":[
    {"label":"¿Qué","key":1},{"label":"hiciste","key":2},{"label":"el año","key":3},{"label":"pasado?","key":4}]},
  {"tag":"selo","sub":"se las","items":[
    {"label":"Las fotos,","key":1},{"label":"se las","key":2},{"label":"mandé","key":3},{"label":"a Nina.","key":4}]},
  {"tag":"frase","sub":"marcador + indefinido","items":[
    {"label":"En 1986","key":1},{"label":"Maradona","key":2},{"label":"hizo","key":3},{"label":"historia.","key":4}]}]}})

# 10 · POINT — señala (repaso gemengd) (10 rondes)
w({"id":PRE+"senala","title":"Señala","subtitle":"U5 · klik het juiste antwoord",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het gevraagde item","mode":"one","rounds":[
  {"tag":"bio","sub":"señala una etapa de la vida","targets":[
    {"label":"nacer","hit":True},{"label":"ganar"},{"label":"el escritor"},{"label":"famoso"}]},
  {"tag":"bio","sub":"señala un oficio","targets":[
    {"label":"el pintor","hit":True},{"label":"crecer"},{"label":"el premio"},{"label":"morir"}]},
  {"tag":"indef","sub":"hacer → indefinido (él)","targets":[
    {"label":"hizo","hit":True},{"label":"hació"},{"label":"hace"},{"label":"hizió"}]},
  {"tag":"indef","sub":"ser/ir → indefinido (él)","targets":[
    {"label":"fue","hit":True},{"label":"fui"},{"label":"fué"},{"label":"era"}]},
  {"tag":"indef","sub":"«escribió» = ?","targets":[
    {"label":"hij/zij schreef","hit":True},{"label":"hij schrijft"},{"label":"hij gaat schrijven"},{"label":"hij heeft geschreven"}]},
  {"tag":"selo","sub":"«¿El libro a él? ___ di»","targets":[
    {"label":"Se lo","hit":True},{"label":"Le lo"},{"label":"Se la"},{"label":"Lo le"}]},
  {"tag":"selo","sub":"«¿Las fotos a ella? ___ mandé»","targets":[
    {"label":"Se las","hit":True},{"label":"Le las"},{"label":"Se los"},{"label":"Las le"}]},
  {"tag":"marc","sub":"marcador del indefinido","targets":[
    {"label":"ayer","hit":True},{"label":"hoy"},{"label":"esta semana"},{"label":"mañana"}]},
  {"tag":"indef","sub":"tener → indefinido (él)","targets":[
    {"label":"tuvo","hit":True},{"label":"tenió"},{"label":"tiene"},{"label":"tení"}]},
  {"tag":"conector","sub":"«uiteindelijk» = ?","targets":[
    {"label":"al final","hit":True},{"label":"primero"},{"label":"entonces"},{"label":"érase una vez"}]}]}})

# 11 · SPEAK repeat — biografía (8 items)
w({"id":PRE+"repite-bio","title":"Escucha y repite: una biografía","subtitle":"U5 · escucha, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite en voz alta · grábate ⏺","items":[
  {"text":"Nació en Argentina en 1987.","sub":"hij werd geboren in Argentinië in 1987","tag":"if","tip":"¡Bien! Ahora dilo sin leer."},
  {"text":"De joven jugó en un equipo local.","sub":"als jongere speelde hij in een lokaal team","tag":"if"},
  {"text":"Ganó muchos títulos.","sub":"hij won veel titels","tag":"if"},
  {"text":"En 2022 fue campeón del Mundo.","sub":"in 2022 was hij wereldkampioen","tag":"if"},
  {"text":"Frida pintó autorretratos famosos.","sub":"Frida schilderde beroemde zelfportretten","tag":"if"},
  {"text":"El libro se lo di a Mateo.","sub":"het boek gaf ik aan Mateo","tag":"selo"},
  {"text":"Primero estudió, después triunfó.","sub":"eerst studeerde hij, daarna slaagde hij","tag":"conector"},
  {"text":"Creo que fue un genio.","sub":"ik denk dat hij een genie was","tag":"opinion"}]}})

# 12 · SPEAK voicemessage — biografía + opinión (3 items)
w({"id":PRE+"mensaje-bio","title":"Mensaje de voz: una biografía","subtitle":"U5 · neem een spraakbericht op",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz (30–40 s)","items":[
  {"text":"Cuenta la vida de una persona famosa (usa 3 veces el indefinido: nació, hizo, ganó/escribió).","cue":"una biografía","tag":"if",
   "sub":"gebruik: nació en… · estudió… · escribió/ganó…",
   "tip":"3× el indefinido (afgeronde feiten)? Neem opnieuw op."},
  {"text":"Usa conectores para ordenar la vida (primero, después, entonces, al final).","cue":"conectores","tag":"conector",
   "sub":"gebruik: primero… después… entonces… al final…",
   "tip":"conectoren gebruikt? Herneem."},
  {"text":"Da tu opinión sobre esa figura (creo que fue… porque…).","cue":"mi opinión","tag":"opinion",
   "sub":"gebruik: creo que fue… porque… · lo más importante fue…",
   "tip":"una opinión met «fue»? Herneem."}]}})

print("\n12 C6+·U5-spellen geschreven (8 templates: memory·match·classify·cloze·tetris·order·point·speak).")
