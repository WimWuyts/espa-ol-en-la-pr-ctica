#!/usr/bin/env python3
# Genereert de motor-content-JSON's voor C5 · U8 «¿Qué has hecho?» (parada Perú/Cusco · Machu Picchu).
# Templates: memory·match·classify·cloze·tetris·order·point·sim·speak (receptief -> productief -> hablar).
# VERRIJKT: elke game heeft een POOL van >=12 items; options.rounds staat lager (~8-12)
#   zodat elke herspeling een ANDERE reeks trekt (variatie / herspeelwaarde).
# Werkwoordsvormen (pretérito perfecto compuesto = haber + participio, participios reg/irreg) nagerekend/geverifieerd.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2))
    print("wrote", os.path.basename(p))

G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0"}

# ============================ ① RECONOCER · woordenschat ============================
# 1 · MEMORY — viajes/transporte ES ↔ NL  (pool 14)
w({"id":"es-u8-viajes-memoria","title":"Memoria de los viajes","subtitle":"U8 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om en zoek het woord + de vertaling","pairs":[
  {"a":"el viaje","b":"de reis"},{"a":"la maleta","b":"de koffer"},{"a":"el billete","b":"het ticket"},
  {"a":"el pasaporte","b":"het paspoort"},{"a":"el avión","b":"het vliegtuig"},{"a":"el tren","b":"de trein"},
  {"a":"el hotel","b":"het hotel"},{"a":"la playa","b":"het strand"},{"a":"la montaña","b":"de berg"},
  {"a":"el barco","b":"de boot"},{"a":"la foto","b":"de foto"},{"a":"el recuerdo","b":"het souvenir"},
  {"a":"la excursión","b":"de excursie"},{"a":"la estación","b":"het station"}]}})

# 2 · MEMORY — clima ES ↔ NL  (pool 12)
w({"id":"es-u8-clima-memoria","title":"El tiempo y el clima","subtitle":"U8 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: woord + vertaling","pairs":[
  {"a":"hace sol","b":"het is zonnig"},{"a":"hace calor","b":"het is warm"},{"a":"hace frío","b":"het is koud"},
  {"a":"hace viento","b":"het waait"},{"a":"llueve","b":"het regent"},{"a":"nieva","b":"het sneeuwt"},
  {"a":"está nublado","b":"het is bewolkt"},{"a":"la lluvia","b":"de regen"},{"a":"la nieve","b":"de sneeuw"},
  {"a":"la tormenta","b":"de storm"},{"a":"el paraguas","b":"de paraplu"},{"a":"la nube","b":"de wolk"}]}})

# 3 · MATCH — participio ↔ infinitivo  (pool 14, blokjes van 6)
w({"id":"es-u8-participio-infinitivo","title":"Participio e infinitivo","subtitle":"U8 · koppel het deelwoord aan het werkwoord",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind het participio met de infinitief","pairs":[
  {"a":"hecho","b":"hacer"},{"a":"visto","b":"ver"},{"a":"dicho","b":"decir"},{"a":"escrito","b":"escribir"},
  {"a":"vuelto","b":"volver"},{"a":"puesto","b":"poner"},{"a":"abierto","b":"abrir"},{"a":"roto","b":"romper"},
  {"a":"viajado","b":"viajar"},{"a":"comido","b":"comer"},{"a":"vivido","b":"vivir"},{"a":"subido","b":"subir"},
  {"a":"estado","b":"estar"},{"a":"ido","b":"ir"}]}})

# 3b · MATCH — país ↔ clima/símbolo  (pool 12)
w({"id":"es-u8-pais-clima","title":"País y clima","subtitle":"U8 · welk weer/plek hoort bij het land?",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind de plek met het typische weer of symbool","pairs":[
  {"a":"Cusco (los Andes) 🇵🇪","b":"hace frío 🥶"},{"a":"la selva amazónica 🇵🇪","b":"llueve 🌧️"},
  {"a":"la costa de Lima 🇵🇪","b":"hace sol ☀️"},{"a":"Machu Picchu 🇵🇪","b":"las ruinas incas 🏔️"},
  {"a":"los Andes en invierno","b":"nieva ❄️"},{"a":"España en verano 🇪🇸","b":"hace calor 🔥"},
  {"a":"Cartagena 🇨🇴","b":"la playa 🏖️"},{"a":"CDMX 🇲🇽","b":"los tacos 🌮"},
  {"a":"la sierra de noche","b":"hace frío 🥶"},{"a":"un día de tormenta","b":"hay tormenta ⛈️"},
  {"a":"el cielo con nubes","b":"está nublado ☁️"},{"a":"el mar del Caribe","b":"hace calor 🔥"}]}})

# ============================ ② DISTINGUIR · gramática/léxico ============================
# 4 · CLASSIFY — participio regular o irregular  (pool 20, rounds 12)
w({"id":"es-u8-regular-irregular","title":"¿Participio regular o irregular?","subtitle":"U8 · -ado/-ido of uit het hoofd?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Is de participio regelmatig (-ado/-ido) of onregelmatig?","categories":[
  {"id":"regular","label":"regular<br><small>-ado / -ido</small>","glaze":G["green"]},
  {"id":"irregular","label":"irregular<br><small>uit het hoofd</small>","glaze":G["red"]}],
 "items":[
  {"stimulus":"viajar → viajado","answer":"regular","tag":"regular","sub":"-ar → -ado"},
  {"stimulus":"comer → comido","answer":"regular","tag":"regular","sub":"-er → -ido"},
  {"stimulus":"hacer → hecho","answer":"irregular","tag":"irregular","sub":"irregular"},
  {"stimulus":"ver → visto","answer":"irregular","tag":"irregular","sub":"irregular"},
  {"stimulus":"vivir → vivido","answer":"regular","tag":"regular","sub":"-ir → -ido"},
  {"stimulus":"escribir → escrito","answer":"irregular","tag":"irregular","sub":"irregular"},
  {"stimulus":"estudiar → estudiado","answer":"regular","tag":"regular","sub":"-ar → -ado"},
  {"stimulus":"volver → vuelto","answer":"irregular","tag":"irregular","sub":"irregular"},
  {"stimulus":"subir → subido","answer":"regular","tag":"regular","sub":"-ir → -ido"},
  {"stimulus":"poner → puesto","answer":"irregular","tag":"irregular","sub":"irregular"},
  {"stimulus":"beber → bebido","answer":"regular","tag":"regular","sub":"-er → -ido"},
  {"stimulus":"abrir → abierto","answer":"irregular","tag":"irregular","sub":"irregular"},
  {"stimulus":"hablar → hablado","answer":"regular","tag":"regular","sub":"-ar → -ado"},
  {"stimulus":"decir → dicho","answer":"irregular","tag":"irregular","sub":"irregular"},
  {"stimulus":"visitar → visitado","answer":"regular","tag":"regular","sub":"-ar → -ado"},
  {"stimulus":"romper → roto","answer":"irregular","tag":"irregular","sub":"irregular"},
  {"stimulus":"llegar → llegado","answer":"regular","tag":"regular","sub":"-ar → -ado"},
  {"stimulus":"estar → estado","answer":"regular","tag":"regular","sub":"-ar → -ado"},
  {"stimulus":"sacar → sacado","answer":"regular","tag":"regular","sub":"-ar → -ado"},
  {"stimulus":"ir → ido","answer":"regular","tag":"regular","sub":"-ir → -ido (kort)"}]}})

# 5 · CLASSIFY — ¿qué tiempo hace? (hace / está / verbo)  (pool 18, rounds 12)
w({"id":"es-u8-que-tiempo","title":"¿Qué tiempo hace?","subtitle":"U8 · hace · está · un verbo (llueve/nieva)",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Welk woord hoort bij de weer-uitdrukking?","categories":[
  {"id":"hace","label":"hace…<br><small>sol/frío/calor</small>","glaze":G["amber"]},
  {"id":"esta","label":"está / hay…<br><small>nublado/tormenta</small>","glaze":G["blue"]},
  {"id":"verbo","label":"un verbo<br><small>llueve/nieva</small>","glaze":G["teal"]}],
 "items":[
  {"stimulus":"___ sol","answer":"hace","tag":"hace","sub":"hace sol"},
  {"stimulus":"___ calor","answer":"hace","tag":"hace","sub":"hace calor"},
  {"stimulus":"___ frío","answer":"hace","tag":"hace","sub":"hace frío"},
  {"stimulus":"___ viento","answer":"hace","tag":"hace","sub":"hace viento"},
  {"stimulus":"___ buen tiempo","answer":"hace","tag":"hace","sub":"hace buen tiempo"},
  {"stimulus":"___ mal tiempo","answer":"hace","tag":"hace","sub":"hace mal tiempo"},
  {"stimulus":"___ nublado","answer":"esta","tag":"esta","sub":"está nublado"},
  {"stimulus":"___ tormenta","answer":"esta","tag":"esta","sub":"hay tormenta"},
  {"stimulus":"___ nubes","answer":"esta","tag":"esta","sub":"hay nubes"},
  {"stimulus":"___ (regenen)","answer":"verbo","tag":"verbo","sub":"llueve"},
  {"stimulus":"___ (sneeuwen)","answer":"verbo","tag":"verbo","sub":"nieva"},
  {"stimulus":"___ 20 grados","answer":"hace","tag":"hace","sub":"hace 20 grados"},
  {"stimulus":"___ despejado","answer":"esta","tag":"esta","sub":"está despejado"},
  {"stimulus":"___ (het regent nu)","answer":"verbo","tag":"verbo","sub":"llueve"},
  {"stimulus":"___ sol y calor","answer":"hace","tag":"hace","sub":"hace sol y calor"},
  {"stimulus":"___ mucho viento","answer":"hace","tag":"hace","sub":"hace mucho viento"},
  {"stimulus":"___ nieve en la sierra","answer":"verbo","tag":"verbo","sub":"nieva"},
  {"stimulus":"___ muy nublado","answer":"esta","tag":"esta","sub":"está muy nublado"}]}})

# 5b · CLASSIFY — marcador: ¿periodo abierto o experiencia?  (pool 16, rounds 10)
w({"id":"es-u8-marcador","title":"¿Periodo o experiencia?","subtitle":"U8 · sorteer de marcador (hoy… / nunca…)",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Is de marcador een lopende periode of een ervaring?","categories":[
  {"id":"periodo","label":"periodo abierto<br><small>hoy · este año</small>","glaze":G["green"]},
  {"id":"experiencia","label":"experiencia<br><small>nunca · alguna vez</small>","glaze":G["purple"]}],
 "items":[
  {"stimulus":"hoy","answer":"periodo","tag":"periodo","sub":"vandaag"},
  {"stimulus":"esta semana","answer":"periodo","tag":"periodo","sub":"deze week"},
  {"stimulus":"este mes","answer":"periodo","tag":"periodo","sub":"deze maand"},
  {"stimulus":"este año","answer":"periodo","tag":"periodo","sub":"dit jaar"},
  {"stimulus":"esta mañana","answer":"periodo","tag":"periodo","sub":"vanochtend"},
  {"stimulus":"últimamente","answer":"periodo","tag":"periodo","sub":"de laatste tijd"},
  {"stimulus":"nunca","answer":"experiencia","tag":"experiencia","sub":"nooit"},
  {"stimulus":"alguna vez","answer":"experiencia","tag":"experiencia","sub":"ooit"},
  {"stimulus":"muchas veces","answer":"experiencia","tag":"experiencia","sub":"vaak"},
  {"stimulus":"ya","answer":"experiencia","tag":"experiencia","sub":"al (klaar)"},
  {"stimulus":"todavía no","answer":"experiencia","tag":"experiencia","sub":"nog niet"},
  {"stimulus":"una vez","answer":"experiencia","tag":"experiencia","sub":"één keer"},
  {"stimulus":"este verano","answer":"periodo","tag":"periodo","sub":"deze zomer"},
  {"stimulus":"dos veces","answer":"experiencia","tag":"experiencia","sub":"twee keer"},
  {"stimulus":"hoy por la tarde","answer":"periodo","tag":"periodo","sub":"vanmiddag"},
  {"stimulus":"jamás","answer":"experiencia","tag":"experiencia","sub":"nooit (nadruk)"}]}})

# ============================ ③ PRODUCIR CON APOYO ============================
# 6 · CLOZE — haber + participio (VERPLICHT werkwoord-cloze, nagerekend)  (pool 20, rounds 12)
w({"id":"es-u8-haber-participio","title":"Completa: haber + participio","subtitle":"U8 · el pretérito perfecto compuesto (he viajado…)",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm van «haber + participio»","items":[
  {"stimulus":"(Yo) ___ a Machu Picchu.","options":["he subido","has subido","he subir"],"answer":"he subido","tag":"pc","sub":"yo → he + subido"},
  {"stimulus":"¿(Tú) ___ las llamas?","options":["has visto","he visto","has veído"],"answer":"has visto","tag":"pc","sub":"tú → has + visto (irreg.)"},
  {"stimulus":"(Nosotros) ___ muchas fotos.","options":["hemos sacado","han sacado","hemos sacar"],"answer":"hemos sacado","tag":"pc","sub":"nosotros → hemos + sacado"},
  {"stimulus":"Nina ___ un diario.","options":["ha escrito","ha escribido","han escrito"],"answer":"ha escrito","tag":"pc","sub":"ella → ha + escrito (irreg.)"},
  {"stimulus":"(Ellos) ___ en tren.","options":["han viajado","ha viajado","han viajar"],"answer":"han viajado","tag":"pc","sub":"ellos → han + viajado"},
  {"stimulus":"Hoy (yo) todavía no ___.","options":["he comido","has comido","he comer"],"answer":"he comido","tag":"pc","sub":"yo → he + comido"},
  {"stimulus":"¿(Vosotros) ___ la maleta?","options":["habéis hecho","han hecho","habéis hacido"],"answer":"habéis hecho","tag":"pc","sub":"vosotros → habéis + hecho (irreg.)"},
  {"stimulus":"Diego ___ del viaje.","options":["ha vuelto","ha volvido","han vuelto"],"answer":"ha vuelto","tag":"pc","sub":"él → ha + vuelto (irreg.)"},
  {"stimulus":"(Yo) ___ un ceviche.","options":["he comido","has comido","he comer"],"answer":"he comido","tag":"pc","sub":"yo → he + comido"},
  {"stimulus":"¿Qué ___ (tú) hoy?","options":["has hecho","he hecho","has hacido"],"answer":"has hecho","tag":"pc","sub":"tú → has + hecho (irreg.)"},
  {"stimulus":"(Nosotros) ___ el hotel.","options":["hemos abierto","han abierto","hemos abrido"],"answer":"hemos abierto","tag":"pc","sub":"nosotros → hemos + abierto (irreg.)"},
  {"stimulus":"Lucía ___ una postal.","options":["ha escrito","ha escribido","han escrito"],"answer":"ha escrito","tag":"pc","sub":"ella → ha + escrito"},
  {"stimulus":"(Ellos) ___ a la montaña.","options":["han subido","ha subido","han subir"],"answer":"han subido","tag":"pc","sub":"ellos → han + subido"},
  {"stimulus":"¿(Tú) ___ el mar alguna vez?","options":["has visto","he visto","has veído"],"answer":"has visto","tag":"pc","sub":"tú → has + visto"},
  {"stimulus":"(Yo) ___ el abrigo porque hace frío.","options":["me he puesto","me ha puesto","me he ponido"],"answer":"me he puesto","tag":"pc","sub":"yo → he + puesto (irreg.)"},
  {"stimulus":"Se ___ la maleta.","options":["ha roto","ha rompido","han roto"],"answer":"ha roto","tag":"pc","sub":"se ha + roto (irreg.)"},
  {"stimulus":"(Nosotros) ___ en avión.","options":["hemos viajado","han viajado","hemos viajar"],"answer":"hemos viajado","tag":"pc","sub":"nosotros → hemos + viajado"},
  {"stimulus":"Nina ___ la verdad.","options":["ha dicho","ha decido","han dicho"],"answer":"ha dicho","tag":"pc","sub":"ella → ha + dicho (irreg.)"},
  {"stimulus":"(Vosotros) ___ las ruinas.","options":["habéis visitado","han visitado","habéis visitar"],"answer":"habéis visitado","tag":"pc","sub":"vosotros → habéis + visitado"},
  {"stimulus":"Este año (yo) ___ mucho.","options":["he estudiado","has estudiado","he estudiar"],"answer":"he estudiado","tag":"pc","sub":"yo → he + estudiado"}]}})

# 7 · CLOZE — participio irregular  (pool 14, rounds 10)
w({"id":"es-u8-participio-irregular","title":"El participio irregular","subtitle":"U8 · schrijf de onregelmatige participio",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies de juiste onregelmatige participio","items":[
  {"stimulus":"hacer → he ___","options":["hecho","hacido","hacado"],"answer":"hecho","tag":"irr","sub":"hacer → hecho"},
  {"stimulus":"ver → has ___","options":["visto","veído","vido"],"answer":"visto","tag":"irr","sub":"ver → visto"},
  {"stimulus":"decir → ha ___","options":["dicho","decido","dijido"],"answer":"dicho","tag":"irr","sub":"decir → dicho"},
  {"stimulus":"escribir → hemos ___","options":["escrito","escribido","escribto"],"answer":"escrito","tag":"irr","sub":"escribir → escrito"},
  {"stimulus":"volver → habéis ___","options":["vuelto","volvido","volto"],"answer":"vuelto","tag":"irr","sub":"volver → vuelto"},
  {"stimulus":"poner → han ___","options":["puesto","ponido","posto"],"answer":"puesto","tag":"irr","sub":"poner → puesto"},
  {"stimulus":"abrir → he ___","options":["abierto","abrido","abrto"],"answer":"abierto","tag":"irr","sub":"abrir → abierto"},
  {"stimulus":"romper → has ___","options":["roto","rompido","rompto"],"answer":"roto","tag":"irr","sub":"romper → roto"},
  {"stimulus":"hacer → ¿qué has ___?","options":["hecho","hacido","hacto"],"answer":"hecho","tag":"irr","sub":"hacer → hecho"},
  {"stimulus":"ver → nunca he ___ el mar","options":["visto","veído","vido"],"answer":"visto","tag":"irr","sub":"ver → visto"},
  {"stimulus":"escribir → he ___ una postal","options":["escrito","escribido","escrivido"],"answer":"escrito","tag":"irr","sub":"escribir → escrito"},
  {"stimulus":"volver → ya hemos ___","options":["vuelto","volvido","vueltado"],"answer":"vuelto","tag":"irr","sub":"volver → vuelto"},
  {"stimulus":"poner → me he ___ el abrigo","options":["puesto","ponido","puestado"],"answer":"puesto","tag":"irr","sub":"poner → puesto"},
  {"stimulus":"decir → me ha ___ la verdad","options":["dicho","decido","dichado"],"answer":"dicho","tag":"irr","sub":"decir → dicho"}]}})

# 8 · CLOZE — ya / todavía no / marcadores  (pool 14, rounds 10)
w({"id":"es-u8-ya-todavia","title":"¿ya, todavía no o…?","subtitle":"U8 · kies de juiste marcador",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies de marcador die past","items":[
  {"stimulus":"___ he hecho la maleta. ✅","options":["Ya","Todavía no","Nunca"],"answer":"Ya","tag":"mc","sub":"klaar → ya"},
  {"stimulus":"___ he reservado el hotel. ⏳","options":["Todavía no","Ya","Muchas veces"],"answer":"Todavía no","tag":"mc","sub":"nog niet → todavía no"},
  {"stimulus":"¿Has viajado ___ en barco? (ooit)","options":["alguna vez","ya","hoy"],"answer":"alguna vez","tag":"mc","sub":"ooit → alguna vez"},
  {"stimulus":"___ he estado en Perú. (nooit)","options":["Nunca","Ya","Esta semana"],"answer":"Nunca","tag":"mc","sub":"nooit → nunca"},
  {"stimulus":"___ he estudiado dos horas. (vandaag)","options":["Hoy","Nunca","Alguna vez"],"answer":"Hoy","tag":"mc","sub":"vandaag → hoy"},
  {"stimulus":"He visto esa peli ___. (vaak)","options":["muchas veces","todavía no","hoy"],"answer":"muchas veces","tag":"mc","sub":"vaak → muchas veces"},
  {"stimulus":"___ hemos ido dos veces. (deze week)","options":["Esta semana","Nunca","Alguna vez"],"answer":"Esta semana","tag":"mc","sub":"deze week → esta semana"},
  {"stimulus":"—¿Has comido? —No, ___.","options":["todavía no","ya","alguna vez"],"answer":"todavía no","tag":"mc","sub":"nog niet"},
  {"stimulus":"—¿Has hecho los deberes? —Sí, ___.","options":["ya","nunca","todavía no"],"answer":"ya","tag":"mc","sub":"al klaar → ya"},
  {"stimulus":"___ he viajado a México. (dit jaar)","options":["Este año","Nunca","Alguna vez"],"answer":"Este año","tag":"mc","sub":"dit jaar → este año"},
  {"stimulus":"¿Has probado el ceviche ___? (ooit)","options":["alguna vez","ya","hoy"],"answer":"alguna vez","tag":"mc","sub":"ooit"},
  {"stimulus":"___ he visto la nieve. (nog nooit)","options":["Nunca","Ya","Hoy"],"answer":"Nunca","tag":"mc","sub":"nooit → nunca"},
  {"stimulus":"___ he leído mucho. (de laatste tijd)","options":["Últimamente","Nunca","Todavía no"],"answer":"Últimamente","tag":"mc","sub":"de laatste tijd"},
  {"stimulus":"¿___ has llegado? ¡Qué rápido!","options":["Ya","Nunca","Todavía no"],"answer":"Ya","tag":"mc","sub":"al → ya"}]}})

# 9 · TETRIS — haber (he/has/ha/hemos/habéis/han)  (pool 18)
w({"id":"es-u8-haber-tetris","title":"Haber Tetris","subtitle":"U8 · laat elke persoon in de juiste vorm van «haber» vallen",
 "lang":"es","template":"tetris","options":{"rows":9,"speed":1300,"audio":False},
 "classify":{"categories":[
  {"id":"he","label":"he","glaze":G["blue"]},{"id":"has","label":"has","glaze":G["red"]},
  {"id":"ha","label":"ha","glaze":G["green"]},{"id":"hemos","label":"hemos","glaze":G["amber"]},
  {"id":"han","label":"han","glaze":G["purple"]}],
 "items":[
  {"stimulus":"yo","answer":"he","tag":"he","sub":"yo he"},
  {"stimulus":"tú","answer":"has","tag":"has","sub":"tú has"},
  {"stimulus":"él","answer":"ha","tag":"ha","sub":"él ha"},
  {"stimulus":"ella","answer":"ha","tag":"ha","sub":"ella ha"},
  {"stimulus":"nosotros","answer":"hemos","tag":"hemos","sub":"nosotros hemos"},
  {"stimulus":"nosotras","answer":"hemos","tag":"hemos","sub":"nosotras hemos"},
  {"stimulus":"ellos","answer":"han","tag":"han","sub":"ellos han"},
  {"stimulus":"ellas","answer":"han","tag":"han","sub":"ellas han"},
  {"stimulus":"Nina","answer":"ha","tag":"ha","sub":"Nina ha"},
  {"stimulus":"Diego y Nina","answer":"han","tag":"han","sub":"ellos han"},
  {"stimulus":"tú y yo","answer":"hemos","tag":"hemos","sub":"nosotros hemos"},
  {"stimulus":"usted","answer":"ha","tag":"ha","sub":"usted ha"},
  {"stimulus":"mi madre","answer":"ha","tag":"ha","sub":"ella ha"},
  {"stimulus":"mis amigos","answer":"han","tag":"han","sub":"ellos han"},
  {"stimulus":"yo (otra vez)","answer":"he","tag":"he","sub":"yo he"},
  {"stimulus":"la profesora","answer":"ha","tag":"ha","sub":"ella ha"},
  {"stimulus":"tú (otra vez)","answer":"has","tag":"has","sub":"tú has"},
  {"stimulus":"el grupo","answer":"ha","tag":"ha","sub":"el grupo ha (ev.)"}]}})

# 11 · ORDER — ordena el diario de viaje  (7 rondes)
w({"id":"es-u8-diario-order","title":"Ordena el diario de viaje","subtitle":"U8 · zet de reisdag in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik de zinnen in de logische volgorde van een reisdag","rounds":[
  {"tag":"viaje","sub":"el día de Nina · llegar → subir → fotos → volver","items":[
    {"label":"He llegado a Cusco en avión.","key":1},{"label":"He cogido el tren a Machu Picchu.","key":2},
    {"label":"He subido y he sacado muchas fotos.","key":3},{"label":"Al final, he vuelto al hotel.","key":4}]},
  {"tag":"viaje","sub":"preparar el viaje","items":[
    {"label":"He comprado el billete de avión.","key":1},{"label":"He hecho la maleta.","key":2},
    {"label":"He llegado al aeropuerto.","key":3},{"label":"He viajado a Perú.","key":4}]},
  {"tag":"viaje","sub":"un día en la playa","items":[
    {"label":"Me he levantado temprano.","key":1},{"label":"He ido a la playa a pie.","key":2},
    {"label":"He nadado en el mar.","key":3},{"label":"He vuelto porque ha empezado a llover.","key":4}]},
  {"tag":"viaje","sub":"la excursión a la montaña","items":[
    {"label":"Me he puesto el abrigo (hace frío).","key":1},{"label":"He empezado la excursión.","key":2},
    {"label":"He visto las llamas.","key":3},{"label":"He llegado a la cima.","key":4}]},
  {"tag":"relato","sub":"conectores: primero → luego → después → al final","items":[
    {"label":"Primero, he desayunado.","key":1},{"label":"Luego, he visitado el museo.","key":2},
    {"label":"Después, he comido en un restaurante.","key":3},{"label":"Al final, he escrito en mi diario.","key":4}]},
  {"tag":"relato","sub":"la postal","items":[
    {"label":"He comprado una postal.","key":1},{"label":"He escrito el mensaje.","key":2},
    {"label":"He puesto el sello.","key":3},{"label":"La he enviado a mi familia.","key":4}]},
  {"tag":"viaje","sub":"el mal tiempo","items":[
    {"label":"Por la mañana ha hecho sol.","key":1},{"label":"Luego se ha nublado.","key":2},
    {"label":"Después ha empezado la tormenta.","key":3},{"label":"Al final ha llovido mucho.","key":4}]}]}})

# 12 · POINT — señala el transporte / el clima  (10 rondes)
w({"id":"es-u8-senala-viaje","title":"Señala en el viaje","subtitle":"U8 · klik het juiste woord",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het gevraagde woord","mode":"one","rounds":[
  {"tag":"transporte","sub":"señala el transporte por aire","targets":[
    {"label":"el tren"},{"label":"el avión ✈️","hit":True},{"label":"el barco"},{"label":"la bici"}]},
  {"tag":"transporte","sub":"señala el transporte por agua","targets":[
    {"label":"el barco 🚢","hit":True},{"label":"el coche"},{"label":"el metro"},{"label":"el avión"}]},
  {"tag":"clima","sub":"señala «hace frío»","targets":[
    {"label":"hace calor"},{"label":"hace frío 🥶","hit":True},{"label":"hace sol"},{"label":"está nublado"}]},
  {"tag":"clima","sub":"señala «llueve»","targets":[
    {"label":"nieva"},{"label":"hace sol"},{"label":"llueve 🌧️","hit":True},{"label":"hace viento"}]},
  {"tag":"viajes","sub":"señala lo que llevas en el viaje","targets":[
    {"label":"la maleta 🧳","hit":True},{"label":"el mar"},{"label":"la nube"},{"label":"la estación"}]},
  {"tag":"clima","sub":"señala «nieva»","targets":[
    {"label":"nieva ❄️","hit":True},{"label":"hace calor"},{"label":"llueve"},{"label":"hace sol"}]},
  {"tag":"participio","sub":"señala el participio de «hacer»","targets":[
    {"label":"hacido"},{"label":"hecho","hit":True},{"label":"hago"},{"label":"hacer"}]},
  {"tag":"participio","sub":"señala el participio de «ver»","targets":[
    {"label":"veído"},{"label":"visto","hit":True},{"label":"veo"},{"label":"vido"}]},
  {"tag":"marcador","sub":"señala «nog niet»","targets":[
    {"label":"ya"},{"label":"todavía no","hit":True},{"label":"muchas veces"},{"label":"hoy"}]},
  {"tag":"lugar","sub":"señala el país del ceviche y Machu Picchu","targets":[
    {"label":"México"},{"label":"Perú 🇵🇪","hit":True},{"label":"España"},{"label":"Colombia"}]}]}})

# ============================ ④ ANALIZAR & COMUNICAR ============================
# 13 · SIM — ¡Cuenta tu viaje! (productie met bouwsteen-check)  (6 rondes)
w({"id":"es-u8-cuenta-viaje","title":"¡Cuenta tu viaje!","subtitle":"U8 · schrijf tu experiencia — met alle bouwstenen",
 "lang":"es","template":"sim","options":{"audio":False},
 "sim":{"prompt":"Tarea comunicativa · contar qué has hecho","rounds":[
  {"scenario":"Cuenta qué has hecho hoy (mín. 2 cosas, perfecto compuesto).","tag":"contar","sub":"gebruik: he + participio · hoy","min":10,
   "need":[{"re":"he ","label":"he + participio"},{"re":"hoy|esta","label":"hoy / esta…"},{"re":"visto|hecho|comido|estudiado|ido|viajado","label":"un participio"}],
   "bank":["Hoy","he","he visto","he comido","he estudiado","y","también","una serie"],
   "model":"Hoy he estudiado español y he visto una serie."},
  {"scenario":"Cuenta un viaje: adónde has ido y cómo has viajado.","tag":"viaje","sub":"gebruik: he ido a · he viajado en","min":9,
   "need":[{"re":"he ido|hemos ido","label":"he ido a…"},{"re":"en (avión|tren|coche|barco|bus|autobús)","label":"en + transporte"},{"re":"a ","label":"a + destino"}],
   "bank":["He ido a","Perú","he viajado en","avión","tren","con mi familia"],
   "model":"He ido a Perú. He viajado en avión con mi familia."},
  {"scenario":"Di qué tiempo ha hecho en tu viaje.","tag":"clima","sub":"gebruik: ha hecho · ha llovido · ha nevado","min":8,
   "need":[{"re":"ha hecho|ha llovido|ha nevado|ha estado","label":"weer in perfecto"},{"re":"sol|calor|frío|viento|nublado|lluvia","label":"un tiempo"}],
   "bank":["Ha hecho","sol","frío","ha llovido","por la tarde","ha estado nublado"],
   "model":"Por la mañana ha hecho sol, pero por la tarde ha llovido."},
  {"scenario":"Pregunta a un amigo qué ha hecho estas vacaciones (con marcadores).","tag":"preguntar","sub":"gebruik: ¿qué has hecho? · ¿has …? · alguna vez","min":8,
   "need":[{"re":"has ","label":"¿has …?"},{"re":"qué|alguna vez|dónde","label":"qué / alguna vez / dónde"},{"re":"\\?","label":"een vraag (¿…?)"}],
   "bank":["¿Qué has hecho","estas vacaciones","¿Has viajado","alguna vez","¿Adónde has ido","?"],
   "model":"¿Qué has hecho estas vacaciones? ¿Has viajado alguna vez a otro país?"},
  {"scenario":"Cuenta una experiencia con «nunca» o «ya».","tag":"experiencia","sub":"gebruik: nunca he · ya he","min":7,
   "need":[{"re":"nunca|ya","label":"nunca / ya"},{"re":"he ","label":"he + participio"}],
   "bank":["Nunca he","Ya he","visto la nieve","estado en Perú","comido ceviche"],
   "model":"Nunca he visto la nieve, pero ya he estado en la montaña."},
  {"scenario":"Recomienda un destino y di por qué (perfecto compuesto).","tag":"recomendar","sub":"gebruik: te recomiendo · he estado · porque","min":9,
   "need":[{"re":"recomiendo|recomienda","label":"te recomiendo"},{"re":"he estado|he visitado|he ido","label":"he estado/visitado"},{"re":"porque","label":"porque …"}],
   "bank":["Te recomiendo","Cusco","he estado allí","porque","he visto Machu Picchu","es increíble"],
   "model":"Te recomiendo Cusco porque he estado allí y he visto Machu Picchu."}]}})

# ============================ ⑤ HABLAR · grábate 🎙️ ============================
# 14 · SPEAK repeat — escucha y repite: el tiempo y el viaje  (8 items)
w({"id":"es-u8-repite-tiempo","title":"Escucha y repite: el viaje","subtitle":"U8 · escucha el modelo, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite en voz alta · grábate ⏺","items":[
  {"text":"Hoy he subido a Machu Picchu.","sub":"vandaag ben ik naar Machu Picchu geklommen","tag":"pc","tip":"¡Bien! Ahora dilo sin leer. <span class='nl'>zeg het nu zonder te lezen.</span>"},
  {"text":"He viajado en avión desde Lima.","sub":"ik heb met het vliegtuig gereisd vanuit Lima","tag":"viaje"},
  {"text":"Aquí hace frío y está nublado.","sub":"hier is het koud en bewolkt","tag":"clima"},
  {"text":"¿Qué has hecho hoy?","sub":"wat heb je vandaag gedaan?","tag":"pregunta"},
  {"text":"Nunca he visto la nieve.","sub":"ik heb nog nooit sneeuw gezien","tag":"marcador"},
  {"text":"He sacado muchas fotos.","sub":"ik heb veel foto's gemaakt","tag":"pc"},
  {"text":"Todavía no he comido.","sub":"ik heb nog niet gegeten","tag":"marcador"},
  {"text":"He escrito una postal para mi familia.","sub":"ik heb een kaart geschreven voor mijn familie","tag":"pc"}]}})

# 15 · SPEAK shadowing — con Nina (afbouwende fasen)  (6 items)
w({"id":"es-u8-shadowing-nina","title":"Shadowing con Nina","subtitle":"U8 · praat mee met Nina, steeds minder tekst",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"shadowing","prompt":"Escucha ▶ · habla al mismo tiempo · grábate ⏺","phases":["Texto completo","Palabras clave","Sin texto","Tu versión"],"items":[
  {"text":"Esta semana he viajado a Perú y he visto Machu Picchu.","sub":"deze week ben ik naar Peru gereisd en heb ik Machu Picchu gezien","tag":"pc"},
  {"text":"He cogido el tren muy pronto y ha hecho sol toda la mañana.","sub":"ik heb heel vroeg de trein genomen en het was de hele ochtend zonnig","tag":"viaje"},
  {"text":"En Cusco hace frío, así que me he puesto el abrigo.","sub":"in Cusco is het koud, dus heb ik mijn jas aangedaan","tag":"clima"},
  {"text":"He comido un plato típico y he bebido un mate.","sub":"ik heb een typisch gerecht gegeten en mate gedronken","tag":"pc"},
  {"text":"¿Alguna vez has estado en la montaña?","sub":"ben je ooit in de bergen geweest?","tag":"marcador"},
  {"text":"Al final del día he escrito todo en mi diario.","sub":"aan het eind van de dag heb ik alles in mijn dagboek geschreven","tag":"relato","tip":"Ahora cuenta tu propio día. <span class='nl'>vertel nu je eigen dag.</span>"}]}})

# 16 · SPEAK voicemessage — mensaje de voz: tu viaje  (3 items)
w({"id":"es-u8-mensaje-viaje","title":"Mensaje de voz: tu viaje","subtitle":"U8 · neem een spraakbericht op over je reis",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz (30 s)","items":[
  {"text":"Cuenta qué has hecho estas vacaciones (¿adónde has ido? ¿qué has visto?).","cue":"las vacaciones","tag":"viaje",
   "sub":"gebruik: he ido a · he visto · he viajado en · perfecto compuesto",
   "tip":"Heb je 3 dingen in perfecto compuesto gezegd? Neem opnieuw op. <span class='nl'>3 zinnen met perfecto compuesto? herneem.</span>"},
  {"text":"Deja un mensaje sobre el tiempo de hoy en tu ciudad.","cue":"el tiempo","tag":"clima",
   "sub":"gebruik: hoy hace · está · llueve/nieva · estamos a … grados",
   "tip":"Weer + temperatuur genoemd? Herneem. <span class='nl'>weer + temperatuur? herneem.</span>"},
  {"text":"Cuéntale a un amigo tres experiencias con «alguna vez» o «nunca».","cue":"experiencias","tag":"marcador",
   "sub":"gebruik: (nunca) he … · (alguna vez) he …",
   "tip":"3 ervaringen met marcador? Herneem. <span class='nl'>3 ervaringen met marker? herneem.</span>"}]}})

# 17 · SPEAK repeat — describe tus vacaciones  (6 items)
w({"id":"es-u8-describe-vacaciones","title":"Describe tus vacaciones","subtitle":"U8 · beschrijf je vakantie, grábate",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · describe tus vacaciones · grábate ⏺","items":[
  {"cue":"Modelo · Nina 🇵🇪","text":"Estas vacaciones he ido a Perú.","sub":"deze vakantie ben ik naar Peru gegaan","tag":"describir"},
  {"cue":"¿cómo?","text":"He viajado en avión y en tren.","sub":"ik heb met het vliegtuig en de trein gereisd","tag":"describir"},
  {"cue":"¿qué has visto?","text":"He visto Machu Picchu y muchas llamas.","sub":"ik heb Machu Picchu en veel lama's gezien","tag":"describir"},
  {"cue":"¿qué tiempo?","text":"Ha hecho frío en la montaña, pero sol en la costa.","sub":"in de bergen was het koud, aan de kust zonnig","tag":"describir"},
  {"cue":"¿te ha gustado?","text":"Me ha encantado. ¡Nunca he estado tan feliz!","sub":"ik vond het geweldig. Nog nooit zo blij geweest!","tag":"describir"},
  {"cue":"tu versión","text":"Estas vacaciones he ido a ___ . He visto ___ .","sub":"jouw versie — vul in en zeg ze","tag":"describir",
   "tip":"Ahora describe las vacaciones de un amigo. <span class='nl'>beschrijf nu de vakantie van een vriend(in).</span>"}]}})

print("\n17 U8-spellen geschreven (9 templates: memory·match·classify·cloze·tetris·order·point·sim·speak).")
print("Pools >=12 per game; options.rounds lager => herspeling geeft een andere reeks.")
