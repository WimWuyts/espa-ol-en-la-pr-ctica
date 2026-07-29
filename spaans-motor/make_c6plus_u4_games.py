#!/usr/bin/env python3
# Motor-content-JSON's voor C6+ · U4 «De viaje» (transporte · perfecto compuesto · participios · por/para).
# Templates: memory·match·classify·cloze·tetris·order·point·speak. Pools >=12; rounds lager => andere reeks.
# Participios/perfecto-vormen nagerekend. Slug-prefix = es-c6plus-u4-.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")
def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2)); print("wrote", os.path.basename(p))
G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0","magenta":"#B4309A"}
PRE = "es-c6plus-u4-"

# 1 · MEMORY — transporte/alojamiento ES ↔ NL (pool 14)
w({"id":PRE+"viaje-memoria","title":"Memoria del viaje","subtitle":"U4 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: viaje + vertaling","pairs":[
  {"a":"el avión","b":"het vliegtuig"},{"a":"el tren","b":"de trein"},{"a":"el billete","b":"het ticket"},
  {"a":"la maleta","b":"de koffer"},{"a":"el hotel","b":"het hotel"},{"a":"la reserva","b":"de reservering"},
  {"a":"la llave","b":"de sleutel"},{"a":"la habitación","b":"de kamer"},{"a":"el aeropuerto","b":"de luchthaven"},
  {"a":"la estación","b":"het station"},{"a":"el vuelo","b":"de vlucht"},{"a":"la playa","b":"het strand"},
  {"a":"la montaña","b":"de berg"},{"a":"el equipaje","b":"de bagage"}]}})

# 2 · MEMORY — verbos del viaje ES ↔ NL (pool 12)
w({"id":PRE+"acciones-memoria","title":"Memoria de acciones","subtitle":"U4 · koppel het werkwoord aan de vertaling",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: verbo + vertaling","pairs":[
  {"a":"viajar","b":"reizen"},{"a":"visitar","b":"bezoeken"},{"a":"reservar","b":"reserveren"},
  {"a":"sacar fotos","b":"foto's maken"},{"a":"perder","b":"missen"},{"a":"quedarse","b":"verblijven"},
  {"a":"alquilar","b":"huren"},{"a":"volver","b":"terugkeren"},{"a":"probar","b":"proeven"},
  {"a":"coger","b":"nemen"},{"a":"subir","b":"omhoog gaan"},{"a":"llegar","b":"aankomen"}]}})

# 3 · MATCH — infinitivo ↔ participio (pool 14)
w({"id":PRE+"verbo-participio","title":"Verbo y participio","subtitle":"U4 · koppel de infinitief aan het deelwoord",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind de infinitief met het participio","pairs":[
  {"a":"viajar","b":"viajado"},{"a":"comer","b":"comido"},{"a":"salir","b":"salido"},
  {"a":"hacer","b":"hecho ⭐"},{"a":"ver","b":"visto ⭐"},{"a":"decir","b":"dicho ⭐"},
  {"a":"volver","b":"vuelto ⭐"},{"a":"poner","b":"puesto ⭐"},{"a":"escribir","b":"escrito ⭐"},
  {"a":"abrir","b":"abierto ⭐"},{"a":"romper","b":"roto ⭐"},{"a":"dormir","b":"dormido"},
  {"a":"beber","b":"bebido"},{"a":"subir","b":"subido"}]}})

# 4 · CLASSIFY — ¿participio regular o irregular? (pool 16, rounds 10)
w({"id":PRE+"participio-tipo","title":"¿regular o irregular?","subtitle":"U4 · welk soort participio?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Is het participio regelmatig (-ado/-ido) of onregelmatig?","categories":[
  {"id":"reg","label":"regular<br><small>-ado / -ido</small>","glaze":G["teal"]},
  {"id":"irr","label":"irregular<br><small>hecho, visto…</small>","glaze":G["purple"]}],
 "items":[
  {"stimulus":"viajar → viajado","answer":"reg","tag":"reg","sub":"-ar → -ado"},
  {"stimulus":"hacer → hecho","answer":"irr","tag":"irr","sub":"irregular"},
  {"stimulus":"comer → comido","answer":"reg","tag":"reg","sub":"-er → -ido"},
  {"stimulus":"ver → visto","answer":"irr","tag":"irr","sub":"irregular"},
  {"stimulus":"salir → salido","answer":"reg","tag":"reg","sub":"-ir → -ido"},
  {"stimulus":"decir → dicho","answer":"irr","tag":"irr","sub":"irregular"},
  {"stimulus":"reservar → reservado","answer":"reg","tag":"reg","sub":"-ar → -ado"},
  {"stimulus":"volver → vuelto","answer":"irr","tag":"irr","sub":"irregular"},
  {"stimulus":"dormir → dormido","answer":"reg","tag":"reg","sub":"-ir → -ido"},
  {"stimulus":"escribir → escrito","answer":"irr","tag":"irr","sub":"irregular"},
  {"stimulus":"beber → bebido","answer":"reg","tag":"reg","sub":"-er → -ido"},
  {"stimulus":"poner → puesto","answer":"irr","tag":"irr","sub":"irregular"},
  {"stimulus":"visitar → visitado","answer":"reg","tag":"reg","sub":"-ar → -ado"},
  {"stimulus":"abrir → abierto","answer":"irr","tag":"irr","sub":"irregular"},
  {"stimulus":"subir → subido","answer":"reg","tag":"reg","sub":"-ir → -ido"},
  {"stimulus":"romper → roto","answer":"irr","tag":"irr","sub":"irregular"}]}})

# 5 · CLASSIFY — ¿por o para? (pool 16, rounds 10)
w({"id":PRE+"por-para","title":"¿por o para?","subtitle":"U4 · doel/bestemming (para) of middel/duur/reden (por)?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Kies: para (doel/bestemming) of por (middel/duur/reden)?","categories":[
  {"id":"para","label":"para<br><small>doel/bestemming</small>","glaze":G["green"]},
  {"id":"por","label":"por<br><small>middel/duur/reden</small>","glaze":G["amber"]}],
 "items":[
  {"stimulus":"Salgo ___ Chile.","answer":"para","tag":"para","sub":"bestemming → para"},
  {"stimulus":"Viajo ___ avión.","answer":"por","tag":"por","sub":"middel → por"},
  {"stimulus":"Estudio ___ aprobar.","answer":"para","tag":"para","sub":"doel → para"},
  {"stimulus":"Me quedo ___ dos días.","answer":"por","tag":"por","sub":"duur → por"},
  {"stimulus":"Este regalo es ___ ti.","answer":"para","tag":"para","sub":"ontvanger → para"},
  {"stimulus":"Paseo ___ la playa.","answer":"por","tag":"por","sub":"doorheen → por"},
  {"stimulus":"La reserva es ___ el lunes.","answer":"para","tag":"para","sub":"deadline → para"},
  {"stimulus":"No salgo ___ el mal tiempo.","answer":"por","tag":"por","sub":"reden → por"},
  {"stimulus":"Voy ___ descansar.","answer":"para","tag":"para","sub":"om te → para"},
  {"stimulus":"Viajamos ___ la mañana.","answer":"por","tag":"por","sub":"deel v.d. dag → por"},
  {"stimulus":"El tren sale ___ Madrid.","answer":"para","tag":"para","sub":"bestemming → para"},
  {"stimulus":"Te llamo ___ teléfono.","answer":"por","tag":"por","sub":"middel → por"},
  {"stimulus":"Necesito el billete ___ mañana.","answer":"para","tag":"para","sub":"deadline → para"},
  {"stimulus":"Gracias ___ todo.","answer":"por","tag":"por","sub":"reden → por"},
  {"stimulus":"Estudio español ___ viajar.","answer":"para","tag":"para","sub":"doel → para"},
  {"stimulus":"Camino ___ el centro.","answer":"por","tag":"por","sub":"doorheen → por"}]}})

# 6 · CLOZE — perfecto compuesto (VERPLICHT, nagerekend) (pool 18, rounds 12)
w({"id":PRE+"perfecto","title":"Completa: el perfecto","subtitle":"U4 · haber + participio",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm van het pretérito perfecto","items":[
  {"stimulus":"(Yo) ___ a Chile.","options":["he viajado","has viajado","ha viajado"],"answer":"he viajado","tag":"pf","sub":"yo → he viajado"},
  {"stimulus":"¿(Tú) ___ ya?","options":["has comido","he comido","han comido"],"answer":"has comido","tag":"pf","sub":"tú → has comido"},
  {"stimulus":"Nosotros ___ el museo.","options":["hemos visitado","habéis visitado","han visitado"],"answer":"hemos visitado","tag":"pf","sub":"nosotros → hemos visitado"},
  {"stimulus":"El avión ___ tarde.","options":["ha llegado","han llegado","has llegado"],"answer":"ha llegado","tag":"pf","sub":"él → ha llegado"},
  {"stimulus":"(Yo) ___ las maletas.","options":["he hecho","he hacido","he hacho"],"answer":"he hecho","tag":"pf","sub":"hacer → hecho"},
  {"stimulus":"¿(Tú) ___ el mar?","options":["has visto","has veído","has vido"],"answer":"has visto","tag":"pf","sub":"ver → visto"},
  {"stimulus":"Nosotros ___ del viaje.","options":["hemos vuelto","hemos volvido","hemos vueltado"],"answer":"hemos vuelto","tag":"pf","sub":"volver → vuelto"},
  {"stimulus":"(Yo) ___ una postal.","options":["he escrito","he escribido","he escrivido"],"answer":"he escrito","tag":"pf","sub":"escribir → escrito"},
  {"stimulus":"Mis amigos ___ un hostal.","options":["han reservado","ha reservado","habéis reservado"],"answer":"han reservado","tag":"pf","sub":"ellos → han reservado"},
  {"stimulus":"¿Vosotros ___ fotos?","options":["habéis sacado","han sacado","hemos sacado"],"answer":"habéis sacado","tag":"pf","sub":"vosotros → habéis sacado"},
  {"stimulus":"Nina ___ a la montaña.","options":["ha subido","has subido","han subido"],"answer":"ha subido","tag":"pf","sub":"ella → ha subido"},
  {"stimulus":"(Yo) ___ mal.","options":["he dormido","he durmido","he dormado"],"answer":"he dormido","tag":"pf","sub":"dormir → dormido"},
  {"stimulus":"El guía nos ___ la hora.","options":["ha dicho","ha decido","ha dijido"],"answer":"ha dicho","tag":"pf","sub":"decir → dicho"},
  {"stimulus":"Han ___ el museo.","options":["abierto","abrido","aberto"],"answer":"abierto","tag":"pf","sub":"abrir → abierto"},
  {"stimulus":"(Yo) ___ la paella.","options":["he probado","he probido","he prueba"],"answer":"he probado","tag":"pf","sub":"probar → probado"},
  {"stimulus":"El viaje ___ genial.","options":["ha sido","ha seído","ha estado sido"],"answer":"ha sido","tag":"pf","sub":"ser → sido"},
  {"stimulus":"(Nosotros) ___ en Perú.","options":["hemos estado","habéis estado","han estado"],"answer":"hemos estado","tag":"pf","sub":"nosotros → hemos estado"},
  {"stimulus":"¿(Tú) ___ el tren?","options":["has perdido","has perdo","has perdiendo"],"answer":"has perdido","tag":"pf","sub":"perder → perdido"}]}})

# 7 · CLOZE — por/para (pool 14, rounds 10)
w({"id":PRE+"por-para-cloze","title":"Completa: por / para","subtitle":"U4 · kies por of para",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies por of para","items":[
  {"stimulus":"Salgo ___ Chile mañana.","options":["para","por","de"],"answer":"para","tag":"pp","sub":"bestemming → para"},
  {"stimulus":"Viajo ___ avión.","options":["por","para","en"],"answer":"por","tag":"pp","sub":"middel → por"},
  {"stimulus":"Estudio ___ aprobar el examen.","options":["para","por","a"],"answer":"para","tag":"pp","sub":"doel → para"},
  {"stimulus":"Me quedo ___ una semana.","options":["por","para","en"],"answer":"por","tag":"pp","sub":"duur → por"},
  {"stimulus":"Este billete es ___ ti.","options":["para","por","de"],"answer":"para","tag":"pp","sub":"ontvanger → para"},
  {"stimulus":"Paseamos ___ la costa.","options":["por","para","en"],"answer":"por","tag":"pp","sub":"doorheen → por"},
  {"stimulus":"No viajo ___ el mal tiempo.","options":["por","para","con"],"answer":"por","tag":"pp","sub":"reden → por"},
  {"stimulus":"La reserva es ___ el lunes.","options":["para","por","en"],"answer":"para","tag":"pp","sub":"deadline → para"},
  {"stimulus":"Voy al hotel ___ descansar.","options":["para","por","a"],"answer":"para","tag":"pp","sub":"om te → para"},
  {"stimulus":"Salimos ___ la mañana.","options":["por","para","en"],"answer":"por","tag":"pp","sub":"deel v.d. dag → por"},
  {"stimulus":"Gracias ___ el viaje.","options":["por","para","de"],"answer":"por","tag":"pp","sub":"reden → por"},
  {"stimulus":"El tren sale ___ Barcelona.","options":["para","por","a"],"answer":"para","tag":"pp","sub":"bestemming → para"},
  {"stimulus":"Necesito la maleta ___ el viernes.","options":["para","por","en"],"answer":"para","tag":"pp","sub":"deadline → para"},
  {"stimulus":"Te llamo ___ teléfono.","options":["por","para","con"],"answer":"por","tag":"pp","sub":"middel → por"}]}})

# 8 · TETRIS — participio: -ado / -ido / irregular (pool 16)
w({"id":PRE+"participio-tetris","title":"Participio Tetris","subtitle":"U4 · laat het juiste participio-type vallen",
 "lang":"es","template":"tetris","options":{"rows":9,"speed":1300,"audio":False},
 "classify":{"categories":[
  {"id":"ado","label":"-ado","glaze":G["blue"]},{"id":"ido","label":"-ido","glaze":G["green"]},
  {"id":"irr","label":"irregular","glaze":G["magenta"]}],
 "items":[
  {"stimulus":"viajar","answer":"ado","tag":"ado","sub":"viajado"},{"stimulus":"comer","answer":"ido","tag":"ido","sub":"comido"},
  {"stimulus":"hacer","answer":"irr","tag":"irr","sub":"hecho"},{"stimulus":"salir","answer":"ido","tag":"ido","sub":"salido"},
  {"stimulus":"ver","answer":"irr","tag":"irr","sub":"visto"},{"stimulus":"reservar","answer":"ado","tag":"ado","sub":"reservado"},
  {"stimulus":"volver","answer":"irr","tag":"irr","sub":"vuelto"},{"stimulus":"dormir","answer":"ido","tag":"ido","sub":"dormido"},
  {"stimulus":"visitar","answer":"ado","tag":"ado","sub":"visitado"},{"stimulus":"escribir","answer":"irr","tag":"irr","sub":"escrito"},
  {"stimulus":"beber","answer":"ido","tag":"ido","sub":"bebido"},{"stimulus":"poner","answer":"irr","tag":"irr","sub":"puesto"},
  {"stimulus":"probar","answer":"ado","tag":"ado","sub":"probado"},{"stimulus":"subir","answer":"ido","tag":"ido","sub":"subido"},
  {"stimulus":"decir","answer":"irr","tag":"irr","sub":"dicho"},{"stimulus":"cantar","answer":"ado","tag":"ado","sub":"cantado"}]}})

# 9 · ORDER — ordena la frase / el viaje (8 rondes)
w({"id":PRE+"viaje-order","title":"Ordena la frase","subtitle":"U4 · zet de zin/het verhaal in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik in de logische volgorde","rounds":[
  {"tag":"perfecto","sub":"haber + participio","items":[
    {"label":"Este año","key":1},{"label":"he","key":2},{"label":"viajado","key":3},{"label":"a Chile.","key":4}]},
  {"tag":"relato","sub":"el orden del viaje","items":[
    {"label":"He hecho la maleta,","key":1},{"label":"he cogido el avión,","key":2},{"label":"he visitado el desierto","key":3},{"label":"y he vuelto a casa.","key":4}]},
  {"tag":"porpara","sub":"por/para","items":[
    {"label":"Viajo","key":1},{"label":"por avión","key":2},{"label":"para","key":3},{"label":"visitar Chile.","key":4}]},
  {"tag":"pregunta","sub":"pregunta con perfecto","items":[
    {"label":"¿Has","key":1},{"label":"estado","key":2},{"label":"alguna vez","key":3},{"label":"en Perú?","key":4}]},
  {"tag":"perfecto","sub":"irregular","items":[
    {"label":"(Yo)","key":1},{"label":"he","key":2},{"label":"visto","key":3},{"label":"el mar.","key":4}]},
  {"tag":"opinion","sub":"lo mejor","items":[
    {"label":"Lo mejor","key":1},{"label":"ha sido","key":2},{"label":"el paisaje","key":3},{"label":"de la Patagonia.","key":4}]},
  {"tag":"marcador","sub":"todavía no","items":[
    {"label":"Todavía","key":1},{"label":"no","key":2},{"label":"he estado","key":3},{"label":"en Rapa Nui.","key":4}]},
  {"tag":"relato","sub":"el vuelo","items":[
    {"label":"Primero","key":1},{"label":"he ido al aeropuerto,","key":2},{"label":"luego he facturado","key":3},{"label":"y al final he embarcado.","key":4}]}]}})

# 10 · POINT — señala (repaso gemengd) (10 rondes)
w({"id":PRE+"senala","title":"Señala","subtitle":"U4 · klik het juiste antwoord",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het gevraagde item","mode":"one","rounds":[
  {"tag":"viaje","sub":"señala un transporte","targets":[
    {"label":"el avión","hit":True},{"label":"la playa"},{"label":"el hotel"},{"label":"la llave"}]},
  {"tag":"viaje","sub":"señala un alojamiento","targets":[
    {"label":"el hostal","hit":True},{"label":"el billete"},{"label":"el museo"},{"label":"la maleta"}]},
  {"tag":"part","sub":"hacer → participio","targets":[
    {"label":"hecho","hit":True},{"label":"hacido"},{"label":"hacho"},{"label":"hació"}]},
  {"tag":"part","sub":"ver → participio","targets":[
    {"label":"visto","hit":True},{"label":"veído"},{"label":"vido"},{"label":"veyó"}]},
  {"tag":"perfecto","sub":"«ik heb gereisd» = ?","targets":[
    {"label":"he viajado","hit":True},{"label":"tengo viajado"},{"label":"he viajar"},{"label":"has viajado"}]},
  {"tag":"porpara","sub":"«Salgo ___ Chile»","targets":[
    {"label":"para","hit":True},{"label":"por"},{"label":"de"},{"label":"en"}]},
  {"tag":"porpara","sub":"«Viajo ___ avión»","targets":[
    {"label":"por","hit":True},{"label":"para"},{"label":"en"},{"label":"a"}]},
  {"tag":"marcador","sub":"«nog niet» = ?","targets":[
    {"label":"todavía no","hit":True},{"label":"ya"},{"label":"siempre"},{"label":"nunca"}]},
  {"tag":"part","sub":"volver → participio","targets":[
    {"label":"vuelto","hit":True},{"label":"volvido"},{"label":"vueltado"},{"label":"volto"}]},
  {"tag":"viaje","sub":"«het ticket» = ?","targets":[
    {"label":"el billete","hit":True},{"label":"la reserva"},{"label":"la llave"},{"label":"el equipaje"}]}]}})

# 11 · SPEAK repeat — experiencias de viaje (8 items)
w({"id":PRE+"repite-viaje","title":"Escucha y repite: mi viaje","subtitle":"U4 · escucha, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite en voz alta · grábate ⏺","items":[
  {"text":"Este año he viajado a Chile.","sub":"dit jaar ben ik naar Chile gereisd","tag":"pf","tip":"¡Bien! Ahora dilo sin leer."},
  {"text":"He visto el desierto de Atacama.","sub":"ik heb de Atacama-woestijn gezien","tag":"pf"},
  {"text":"He hecho muchas fotos.","sub":"ik heb veel foto's gemaakt","tag":"pf"},
  {"text":"¿Has estado alguna vez en Perú?","sub":"ben je ooit in Peru geweest?","tag":"pf"},
  {"text":"Todavía no he ido a la playa.","sub":"ik ben nog niet naar het strand geweest","tag":"marc"},
  {"text":"Viajo por avión para descansar.","sub":"ik reis per vliegtuig om te rusten","tag":"pp"},
  {"text":"Lo mejor ha sido el paisaje.","sub":"het beste was het landschap","tag":"op"},
  {"text":"Ha sido un viaje inolvidable.","sub":"het was een onvergetelijke reis","tag":"op"}]}})

# 12 · SPEAK voicemessage — cuenta un viaje (3 items)
w({"id":PRE+"mensaje-viaje","title":"Mensaje de voz: mi viaje","subtitle":"U4 · neem een spraakbericht op",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz (30–40 s)","items":[
  {"text":"Cuenta un viaje real o inventado (usa 3 veces el perfecto: he ido, he visto, he hecho).","cue":"mi viaje","tag":"pf",
   "sub":"gebruik: he viajado a… · he visto… · he probado…",
   "tip":"3× el perfecto (haber + participio)? Neem opnieuw op."},
  {"text":"Di cómo has viajado y para qué (usa por y para).","cue":"por / para","tag":"pp",
   "sub":"gebruik: he viajado por avión · para visitar…",
   "tip":"por én para gebruikt? Herneem."},
  {"text":"Da tu opinión sobre el viaje (lo mejor / lo peor ha sido…).","cue":"mi opinión","tag":"op",
   "sub":"gebruik: lo mejor ha sido… porque… · ha sido inolvidable",
   "tip":"una opinión met «ha sido»? Herneem."}]}})

print("\n12 C6+·U4-spellen geschreven (8 templates: memory·match·classify·cloze·tetris·order·point·speak).")
