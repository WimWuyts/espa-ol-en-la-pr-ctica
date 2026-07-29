#!/usr/bin/env python3
# Motor-content-JSON's voor C6+ · U7 «¡Opina y cuídate!» (salud · medio ambiente · imperativo · opinar · conectores).
# Templates: memory·match·classify·cloze·tetris·order·point·speak. Pools >=12; rounds lager => andere reeks.
# Imperativo-vormen (tú) nagerekend (8 irr: ten/ven/pon/haz/di/sal/sé/ve). Slug-prefix = es-c6plus-u7-.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")
def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2)); print("wrote", os.path.basename(p))
G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0","magenta":"#B4309A"}
PRE = "es-c6plus-u7-"

# 1 · MEMORY — salud ES ↔ NL (pool 14)
w({"id":PRE+"salud-memoria","title":"Memoria de la salud","subtitle":"U7 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: salud + vertaling","pairs":[
  {"a":"la salud","b":"de gezondheid"},{"a":"sano","b":"gezond"},{"a":"enfermo","b":"ziek"},
  {"a":"el cuerpo","b":"het lichaam"},{"a":"el ejercicio","b":"de beweging"},{"a":"dormir","b":"slapen"},
  {"a":"descansar","b":"rusten"},{"a":"la dieta","b":"de voeding"},{"a":"el estrés","b":"de stress"},
  {"a":"cuidarse","b":"voor zichzelf zorgen"},{"a":"la fruta","b":"het fruit"},{"a":"el consejo","b":"de tip"},
  {"a":"evitar","b":"vermijden"},{"a":"relajarse","b":"ontspannen"}]}})

# 2 · MEMORY — medio ambiente + conectores (pool 12)
w({"id":PRE+"planeta-memoria","title":"Memoria: el planeta","subtitle":"U7 · koppel het woord aan de vertaling",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: medio ambiente + vertaling","pairs":[
  {"a":"el medio ambiente","b":"het milieu"},{"a":"el planeta","b":"de planeet"},{"a":"reciclar","b":"recyclen"},
  {"a":"la basura","b":"het afval"},{"a":"contaminar","b":"vervuilen"},{"a":"ahorrar","b":"besparen"},
  {"a":"la energía","b":"de energie"},{"a":"proteger","b":"beschermen"},{"a":"el árbol","b":"de boom"},
  {"a":"porque","b":"omdat/want"},{"a":"además","b":"bovendien"},{"a":"por eso","b":"daarom"}]}})

# 3 · MATCH — infinitivo ↔ imperativo (tú) (pool 14, nagerekend)
w({"id":PRE+"verbo-imperativo","title":"Verbo e imperativo","subtitle":"U7 · koppel de infinitief aan de imperativo (tú)",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind de infinitief met de imperativo (tú)","pairs":[
  {"a":"comer","b":"come"},{"a":"beber","b":"bebe"},{"a":"reciclar","b":"recicla"},
  {"a":"hacer","b":"haz ⭐"},{"a":"ir","b":"ve ⭐"},{"a":"decir","b":"di ⭐"},
  {"a":"tener","b":"ten ⭐"},{"a":"venir","b":"ven ⭐"},{"a":"poner","b":"pon ⭐"},
  {"a":"ser","b":"sé ⭐"},{"a":"salir","b":"sal ⭐"},{"a":"dormir","b":"duerme"},
  {"a":"cuidar","b":"cuida"},{"a":"ahorrar","b":"ahorra"}]}})

# 4 · CLASSIFY — ¿consejo de salud o de medio ambiente? (pool 16, rounds 10)
w({"id":PRE+"salud-planeta","title":"¿salud o medio ambiente?","subtitle":"U7 · waarover gaat de tip?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Is de tip voor de gezondheid of voor het milieu?","categories":[
  {"id":"salud","label":"salud<br><small>el cuerpo, el deporte</small>","glaze":G["red"]},
  {"id":"planeta","label":"medio ambiente<br><small>reciclar, ahorrar</small>","glaze":G["green"]}],
 "items":[
  {"stimulus":"Come más fruta y verdura.","answer":"salud","tag":"salud","sub":"dieta"},
  {"stimulus":"Recicla el papel y el vidrio.","answer":"planeta","tag":"planeta","sub":"residuos"},
  {"stimulus":"Duerme ocho horas.","answer":"salud","tag":"salud","sub":"descanso"},
  {"stimulus":"Ahorra agua: cierra el grifo.","answer":"planeta","tag":"planeta","sub":"agua"},
  {"stimulus":"Haz deporte tres veces por semana.","answer":"salud","tag":"salud","sub":"ejercicio"},
  {"stimulus":"Apaga las luces que no usas.","answer":"planeta","tag":"planeta","sub":"energía"},
  {"stimulus":"Bebe dos litros de agua al día.","answer":"salud","tag":"salud","sub":"hidratación"},
  {"stimulus":"Usa la bici en vez del coche.","answer":"planeta","tag":"planeta","sub":"transporte"},
  {"stimulus":"Relájate para evitar el estrés.","answer":"salud","tag":"salud","sub":"estrés"},
  {"stimulus":"No tires basura al suelo.","answer":"planeta","tag":"planeta","sub":"residuos"},
  {"stimulus":"Evita el azúcar y la comida rápida.","answer":"salud","tag":"salud","sub":"dieta"},
  {"stimulus":"Planta un árbol.","answer":"planeta","tag":"planeta","sub":"naturaleza"},
  {"stimulus":"Muévete más: sube por las escaleras.","answer":"salud","tag":"salud","sub":"ejercicio"},
  {"stimulus":"Protege los bosques.","answer":"planeta","tag":"planeta","sub":"naturaleza"},
  {"stimulus":"Ve al médico una vez al año.","answer":"salud","tag":"salud","sub":"prevención"},
  {"stimulus":"Usa energía solar en casa.","answer":"planeta","tag":"planeta","sub":"energía"}]}})

# 5 · CLASSIFY — ¿a favor o en contra? (del coche) (pool 14, rounds 10)
w({"id":PRE+"favor-contra","title":"¿a favor o en contra?","subtitle":"U7 · sorteer het argument",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Argument vóór of tégen het gebruik van de auto in de stad?","categories":[
  {"id":"favor","label":"a favor 👍","glaze":G["blue"]},
  {"id":"contra","label":"en contra 👎","glaze":G["amber"]}],
 "items":[
  {"stimulus":"Es rápido.","answer":"favor","tag":"favor","sub":"vóór"},
  {"stimulus":"Contamina el aire.","answer":"contra","tag":"contra","sub":"tégen"},
  {"stimulus":"Es cómodo cuando llueve.","answer":"favor","tag":"favor","sub":"vóór"},
  {"stimulus":"Hace mucho ruido.","answer":"contra","tag":"contra","sub":"tégen"},
  {"stimulus":"Gasta mucha gasolina.","answer":"contra","tag":"contra","sub":"tégen"},
  {"stimulus":"Protege de la lluvia y el frío.","answer":"favor","tag":"favor","sub":"vóór"},
  {"stimulus":"Provoca atascos en la ciudad.","answer":"contra","tag":"contra","sub":"tégen"},
  {"stimulus":"Puedes llevar cosas pesadas.","answer":"favor","tag":"favor","sub":"vóór"},
  {"stimulus":"Ocupa mucho espacio para aparcar.","answer":"contra","tag":"contra","sub":"tégen"},
  {"stimulus":"Es útil para largas distancias.","answer":"favor","tag":"favor","sub":"vóór"},
  {"stimulus":"Es caro de mantener.","answer":"contra","tag":"contra","sub":"tégen"},
  {"stimulus":"Da libertad para viajar.","answer":"favor","tag":"favor","sub":"vóór"},
  {"stimulus":"Aumenta la contaminación.","answer":"contra","tag":"contra","sub":"tégen"},
  {"stimulus":"Es práctico con niños pequeños.","answer":"favor","tag":"favor","sub":"vóór"}]}})

# 6 · CLOZE — imperativo (tú) (VERPLICHT, nagerekend) (pool 18, rounds 12)
w({"id":PRE+"imperativo","title":"Completa: el imperativo","subtitle":"U7 · da el consejo (tú)",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies de juiste imperativo (tú)","items":[
  {"stimulus":"___ (comer) más verdura.","options":["Come","Comes","Comer"],"answer":"Come","tag":"im","sub":"comer → come"},
  {"stimulus":"___ (beber) dos litros de agua.","options":["Bebe","Bebes","Beber"],"answer":"Bebe","tag":"im","sub":"beber → bebe"},
  {"stimulus":"___ (hacer) deporte.","options":["Haz","Hace","Haces"],"answer":"Haz","tag":"im","sub":"hacer → haz ⭐"},
  {"stimulus":"___ (dormir) ocho horas.","options":["Duerme","Dormes","Duermes"],"answer":"Duerme","tag":"im","sub":"dormir → duerme"},
  {"stimulus":"___ (reciclar) el plástico.","options":["Recicla","Reciclas","Reciclar"],"answer":"Recicla","tag":"im","sub":"reciclar → recicla"},
  {"stimulus":"___ (ahorrar) energía.","options":["Ahorra","Ahorras","Ahorrar"],"answer":"Ahorra","tag":"im","sub":"ahorrar → ahorra"},
  {"stimulus":"___ (ir) al médico.","options":["Ve","Va","Ir"],"answer":"Ve","tag":"im","sub":"ir → ve ⭐"},
  {"stimulus":"___ (ser) responsable con la basura.","options":["Sé","Ser","Eres"],"answer":"Sé","tag":"im","sub":"ser → sé ⭐"},
  {"stimulus":"___ (decir) siempre la verdad.","options":["Di","Dice","Dices"],"answer":"Di","tag":"im","sub":"decir → di ⭐"},
  {"stimulus":"___ (poner) la basura en su sitio.","options":["Pon","Pone","Pones"],"answer":"Pon","tag":"im","sub":"poner → pon ⭐"},
  {"stimulus":"___ (venir) al parque conmigo.","options":["Ven","Viene","Vienes"],"answer":"Ven","tag":"im","sub":"venir → ven ⭐"},
  {"stimulus":"___ (tener) cuidado con el sol.","options":["Ten","Tiene","Tienes"],"answer":"Ten","tag":"im","sub":"tener → ten ⭐"},
  {"stimulus":"___ (cuidar) tu salud.","options":["Cuida","Cuidas","Cuidar"],"answer":"Cuida","tag":"im","sub":"cuidar → cuida"},
  {"stimulus":"___ (evitar) el estrés.","options":["Evita","Evitas","Evitar"],"answer":"Evita","tag":"im","sub":"evitar → evita"},
  {"stimulus":"___ (proteger) los árboles.","options":["Protege","Proteges","Proteger"],"answer":"Protege","tag":"im","sub":"proteger → protege"},
  {"stimulus":"___ (salir) a caminar cada día.","options":["Sal","Sale","Sales"],"answer":"Sal","tag":"im","sub":"salir → sal ⭐"},
  {"stimulus":"___ (usar) el transporte público.","options":["Usa","Usas","Usar"],"answer":"Usa","tag":"im","sub":"usar → usa"},
  {"stimulus":"___ (apagar) las luces.","options":["Apaga","Apagas","Apagar"],"answer":"Apaga","tag":"im","sub":"apagar → apaga"}]}})

# 7 · CLOZE — opinar + conector (pool 14, rounds 10)
w({"id":PRE+"opinar","title":"Completa: opinar y conectar","subtitle":"U7 · mening + verbindingswoord",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies het juiste woord (mening / conector)","items":[
  {"stimulus":"___ que el deporte es importante.","options":["Creo","Creer","Creía"],"answer":"Creo","tag":"op","sub":"creo que + indicativo"},
  {"stimulus":"Reciclo ___ es importante.","options":["porque","por qué","porqué"],"answer":"porque","tag":"con","sub":"porque = reden"},
  {"stimulus":"Es sano; ___, es barato.","options":["además","porque","sin embargo"],"answer":"además","tag":"con","sub":"además = toevoeging"},
  {"stimulus":"El coche contamina; ___ voy en bici.","options":["por eso","porque","además"],"answer":"por eso","tag":"con","sub":"por eso = gevolg"},
  {"stimulus":"En mi ___, hay mucha basura.","options":["opinión","opino","opinar"],"answer":"opinión","tag":"op","sub":"en mi opinión"},
  {"stimulus":"Es caro; ___, funciona bien.","options":["sin embargo","por eso","además"],"answer":"sin embargo","tag":"con","sub":"sin embargo = echter"},
  {"stimulus":"___ de acuerdo contigo.","options":["Estoy","Soy","Tengo"],"answer":"Estoy","tag":"op","sub":"estar de acuerdo"},
  {"stimulus":"Me ___ que tienes razón.","options":["parece","pareces","parecer"],"answer":"parece","tag":"op","sub":"me parece que"},
  {"stimulus":"Como fruta ___ es sana.","options":["porque","por eso","sin embargo"],"answer":"porque","tag":"con","sub":"reden"},
  {"stimulus":"Tienes ___: hay que reciclar.","options":["razón","razones","derecho"],"answer":"razón","tag":"op","sub":"tener razón"},
  {"stimulus":"Pienso ___ debemos ahorrar agua.","options":["que","de","por"],"answer":"que","tag":"op","sub":"pienso que"},
  {"stimulus":"Es útil; ___, contamina un poco.","options":["sin embargo","por eso","porque"],"answer":"sin embargo","tag":"con","sub":"tegenstelling"},
  {"stimulus":"Ahorro energía; ___ apago las luces.","options":["por eso","porque","además"],"answer":"por eso","tag":"con","sub":"gevolg"},
  {"stimulus":"___ un lado es cómodo; por otro, contamina.","options":["Por","Para","Con"],"answer":"Por","tag":"con","sub":"por un lado"}]}})

# 8 · TETRIS — imperativo: regular -a / regular -e / irregular (pool 16)
w({"id":PRE+"imper-tetris","title":"Imperativo Tetris","subtitle":"U7 · laat het juiste type vallen",
 "lang":"es","template":"tetris","options":{"rows":9,"speed":1300,"audio":False},
 "classify":{"categories":[
  {"id":"a","label":"-a (-ar)","glaze":G["blue"]},{"id":"e","label":"-e (-er/-ir)","glaze":G["green"]},
  {"id":"irr","label":"irregular ⭐","glaze":G["magenta"]}],
 "items":[
  {"stimulus":"cuidar","answer":"a","tag":"a","sub":"cuida"},{"stimulus":"comer","answer":"e","tag":"e","sub":"come"},
  {"stimulus":"hacer","answer":"irr","tag":"irr","sub":"haz"},{"stimulus":"reciclar","answer":"a","tag":"a","sub":"recicla"},
  {"stimulus":"ir","answer":"irr","tag":"irr","sub":"ve"},{"stimulus":"beber","answer":"e","tag":"e","sub":"bebe"},
  {"stimulus":"decir","answer":"irr","tag":"irr","sub":"di"},{"stimulus":"ahorrar","answer":"a","tag":"a","sub":"ahorra"},
  {"stimulus":"escribir","answer":"e","tag":"e","sub":"escribe"},{"stimulus":"ser","answer":"irr","tag":"irr","sub":"sé"},
  {"stimulus":"proteger","answer":"e","tag":"e","sub":"protege"},{"stimulus":"tener","answer":"irr","tag":"irr","sub":"ten"},
  {"stimulus":"evitar","answer":"a","tag":"a","sub":"evita"},{"stimulus":"venir","answer":"irr","tag":"irr","sub":"ven"},
  {"stimulus":"usar","answer":"a","tag":"a","sub":"usa"},{"stimulus":"vivir","answer":"e","tag":"e","sub":"vive"}]}})

# 9 · ORDER — ordena el argumento / la frase (8 rondes)
w({"id":PRE+"argumento-order","title":"Ordena el argumento","subtitle":"U7 · zet de zin/het argument in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik in de logische volgorde","rounds":[
  {"tag":"consejo","sub":"imperativo","items":[
    {"label":"Recicla","key":1},{"label":"el papel","key":2},{"label":"y el vidrio","key":3},{"label":"cada semana.","key":4}]},
  {"tag":"opinion","sub":"mening + reden","items":[
    {"label":"Creo que","key":1},{"label":"debemos reciclar","key":2},{"label":"porque","key":3},{"label":"protege el planeta.","key":4}]},
  {"tag":"argumento","sub":"opinión → argumento → conclusie","items":[
    {"label":"La bici es genial.","key":1},{"label":"No contamina.","key":2},{"label":"Además, es sana.","key":3},{"label":"Por eso la uso.","key":4}]},
  {"tag":"consejo","sub":"imperativo + pronombre","items":[
    {"label":"El grifo:","key":1},{"label":"ciérralo","key":2},{"label":"cuando","key":3},{"label":"te laves los dientes.","key":4}]},
  {"tag":"salud","sub":"consejo de salud","items":[
    {"label":"Come sano,","key":1},{"label":"haz deporte","key":2},{"label":"y duerme","key":3},{"label":"ocho horas.","key":4}]},
  {"tag":"opinion","sub":"reageren","items":[
    {"label":"No estoy","key":1},{"label":"de acuerdo","key":2},{"label":"porque","key":3},{"label":"el coche contamina.","key":4}]},
  {"tag":"argumento","sub":"twee kanten","items":[
    {"label":"Por un lado","key":1},{"label":"es cómodo;","key":2},{"label":"por otro lado,","key":3},{"label":"contamina.","key":4}]},
  {"tag":"consejo","sub":"pura vida","items":[
    {"label":"Cuídate,","key":1},{"label":"relájate","key":2},{"label":"y disfruta:","key":3},{"label":"¡pura vida!","key":4}]}]}})

# 10 · POINT — señala (repaso gemengd) (10 rondes)
w({"id":PRE+"senala","title":"Señala","subtitle":"U7 · klik het juiste antwoord",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het gevraagde item","mode":"one","rounds":[
  {"tag":"voc","sub":"señala algo del medio ambiente","targets":[
    {"label":"reciclar","hit":True},{"label":"el cuerpo"},{"label":"dormir"},{"label":"la dieta"}]},
  {"tag":"voc","sub":"señala algo de la salud","targets":[
    {"label":"el ejercicio","hit":True},{"label":"la basura"},{"label":"la energía"},{"label":"el árbol"}]},
  {"tag":"im","sub":"hacer → imperativo (tú)","targets":[
    {"label":"haz","hit":True},{"label":"hace"},{"label":"haces"},{"label":"hacer"}]},
  {"tag":"im","sub":"ir → imperativo (tú)","targets":[
    {"label":"ve","hit":True},{"label":"va"},{"label":"vas"},{"label":"ir"}]},
  {"tag":"im","sub":"cuida + te = ?","targets":[
    {"label":"cuídate","hit":True},{"label":"cuidate"},{"label":"te cuida"},{"label":"cuidaste"}]},
  {"tag":"op","sub":"«ik ben het eens» = ?","targets":[
    {"label":"estoy de acuerdo","hit":True},{"label":"tengo acuerdo"},{"label":"soy de acuerdo"},{"label":"hago acuerdo"}]},
  {"tag":"op","sub":"na «creo que» komt…","targets":[
    {"label":"indicativo (es)","hit":True},{"label":"subjuntivo (sea)"},{"label":"infinitivo (ser)"},{"label":"imperativo (sé)"}]},
  {"tag":"con","sub":"«daarom» = ?","targets":[
    {"label":"por eso","hit":True},{"label":"porque"},{"label":"luego"},{"label":"sin embargo"}]},
  {"tag":"con","sub":"«want / omdat» = ?","targets":[
    {"label":"porque","hit":True},{"label":"por eso"},{"label":"además"},{"label":"para que"}]},
  {"tag":"cult","sub":"«pura vida» es de…","targets":[
    {"label":"Costa Rica","hit":True},{"label":"Perú"},{"label":"España"},{"label":"México"}]}]}})

# 11 · SPEAK repeat — consejos y opinión (8 items)
w({"id":PRE+"repite-consejos","title":"Escucha y repite: consejos","subtitle":"U7 · escucha, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite en voz alta · grábate ⏺","items":[
  {"text":"Come sano y bebe mucha agua.","sub":"eet gezond en drink veel water","tag":"im","tip":"¡Bien! Ahora dilo sin leer."},
  {"text":"Haz deporte y duerme ocho horas.","sub":"sport en slaap acht uur","tag":"im"},
  {"text":"Recicla el papel y ahorra energía.","sub":"recycle papier en bespaar energie","tag":"im"},
  {"text":"Cuídate y relájate: ¡pura vida!","sub":"zorg goed voor jezelf en ontspan","tag":"im"},
  {"text":"Creo que debemos proteger el planeta.","sub":"ik denk dat we de planeet moeten beschermen","tag":"op"},
  {"text":"En mi opinión, la bici es mejor que el coche.","sub":"volgens mij is de fiets beter dan de auto","tag":"op"},
  {"text":"Reciclo porque es importante; además, ahorra dinero.","sub":"ik recycle want het is belangrijk; bovendien bespaart het geld","tag":"con"},
  {"text":"Estoy de acuerdo, pero tenemos que hacer más.","sub":"ik ben het eens, maar we moeten meer doen","tag":"op"}]}})

# 12 · SPEAK voicemessage — consejo + opinión (3 items)
w({"id":PRE+"mensaje-opinion","title":"Mensaje de voz: tu opinión","subtitle":"U7 · neem een spraakbericht op",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz (30–40 s)","items":[
  {"text":"Da 3 consejos de salud (usa el imperativo: come, bebe, haz…).","cue":"consejos de salud","tag":"im",
   "sub":"gebruik: come sano, bebe agua, haz deporte…",
   "tip":"3× de imperativo (tú)? Neem opnieuw op."},
  {"text":"Da tu opinión sobre el medio ambiente (creo que… porque…).","cue":"mi opinión","tag":"op",
   "sub":"gebruik: creo que… porque… además…",
   "tip":"una opinión + un argumento (porque)? Herneem."},
  {"text":"Convence a alguien de reciclar (imperativo + opinión + conector).","cue":"convencer","tag":"con",
   "sub":"gebruik: Recicla… porque… Por eso…",
   "tip":"un consejo + un argumento + un conector? Herneem."}]}})

print("\n12 C6+·U7-spellen geschreven (8 templates: memory·match·classify·cloze·tetris·order·point·speak).")
