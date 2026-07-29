#!/usr/bin/env python3
# Genereert de motor-content-JSON's voor C5 · U4 «Me gusta».
# Templates: memory·match·classify·cloze·tetris·order·tap·point·sim·speak (receptief -> productief -> hablar).
# Grammaticale vormen (gustar/encantar concord, querer/poder e>ie/o>ue) zijn nagerekend/geverifieerd;
# presente-reg via generator. Speak = échte stemopname (MediaRecorder, offline).
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2))
    print("wrote", os.path.basename(p))

G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0"}

# ============================ ① RECONOCER · woordenschat ============================
# 1 · MEMORY — gustos/ocio ES ↔ NL
w({"id":"es-u4-gustos-memoria","title":"Memoria de los gustos","subtitle":"U4 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om en zoek het woord + de vertaling","pairs":[
  {"a":"gustar","b":"leuk vinden"},{"a":"encantar","b":"geweldig vinden"},{"a":"el deporte","b":"de sport"},
  {"a":"bailar","b":"dansen"},{"a":"nadar","b":"zwemmen"},{"a":"la playa","b":"het strand"},
  {"a":"el tiempo libre","b":"de vrije tijd"},{"a":"salir con amigos","b":"met vrienden uitgaan"},
  {"a":"los videojuegos","b":"de videospellen"},{"a":"aburrido","b":"saai"},{"a":"divertido","b":"leuk/grappig"},
  {"a":"favorito","b":"favoriet"}]}})

# 2 · MEMORY — música/cine ES ↔ NL
w({"id":"es-u4-musica-memoria","title":"Música y cine","subtitle":"U4 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: woord + vertaling","pairs":[
  {"a":"la canción","b":"het liedje"},{"a":"el/la cantante","b":"de zanger(es)"},{"a":"el grupo","b":"de band"},
  {"a":"la película","b":"de film"},{"a":"la serie","b":"de serie"},{"a":"el cine","b":"de bioscoop"},
  {"a":"escuchar música","b":"muziek luisteren"},{"a":"tocar la guitarra","b":"gitaar spelen"},
  {"a":"la letra","b":"de songtekst"},{"a":"el/la artista","b":"de artiest"}]}})

# 3 · MATCH — frecuencia ↔ betekenis (NL)
w({"id":"es-u4-frecuencia-escala","title":"Adverbios de frecuencia","subtitle":"U4 · koppel het frequentiewoord aan de betekenis",
 "lang":"es","template":"match","options":{"chunk":5,"audio":False},
 "match":{"prompt":"Verbind het Spaanse frequentiewoord met de Nederlandse betekenis","pairs":[
  {"a":"siempre","b":"altijd"},{"a":"a menudo","b":"vaak"},{"a":"a veces","b":"soms"},
  {"a":"casi nunca","b":"bijna nooit"},{"a":"nunca","b":"nooit"},{"a":"todos los días","b":"elke dag"},
  {"a":"los fines de semana","b":"in het weekend"}]}})

# ============================ ② DISTINGUIR · gramática ============================
# 4 · CLASSIFY — gusta vs gustan
w({"id":"es-u4-gusta-gustan","title":"¿gusta o gustan?","subtitle":"U4 · één ding/infinitivo = gusta · meerdere = gustan",
 "lang":"es","template":"classify","options":{"rounds":14,"audio":False},
 "classify":{"prompt":"Welke vorm? (één ding of een infinitief = gusta · meervoud = gustan)","categories":[
  {"id":"gusta","label":"gusta<br><small>1 ding / infinitivo</small>","glaze":G["green"]},
  {"id":"gustan","label":"gustan<br><small>meerdere dingen</small>","glaze":G["blue"]}],
 "items":[
  {"stimulus":"Me ___ el fútbol.","answer":"gusta","tag":"gusta","sub":"el fútbol = 1"},
  {"stimulus":"Me ___ los deportes.","answer":"gustan","tag":"gustan","sub":"los deportes = mv."},
  {"stimulus":"Me ___ bailar.","answer":"gusta","tag":"gusta","sub":"infinitivo → gusta"},
  {"stimulus":"Me ___ las series.","answer":"gustan","tag":"gustan","sub":"las series = mv."},
  {"stimulus":"Me ___ la playa.","answer":"gusta","tag":"gusta","sub":"la playa = 1"},
  {"stimulus":"Me ___ los videojuegos.","answer":"gustan","tag":"gustan","sub":"mv."},
  {"stimulus":"Me ___ escuchar música.","answer":"gusta","tag":"gusta","sub":"infinitivo"},
  {"stimulus":"Me ___ las canciones.","answer":"gustan","tag":"gustan","sub":"mv."},
  {"stimulus":"Me ___ el cine.","answer":"gusta","tag":"gusta","sub":"el cine = 1"},
  {"stimulus":"Me ___ los conciertos.","answer":"gustan","tag":"gustan","sub":"mv."},
  {"stimulus":"Me ___ leer.","answer":"gusta","tag":"gusta","sub":"infinitivo"},
  {"stimulus":"Me ___ las películas.","answer":"gustan","tag":"gustan","sub":"mv."},
  {"stimulus":"Me ___ el mar.","answer":"gusta","tag":"gusta","sub":"1 ding"},
  {"stimulus":"Me ___ los animales.","answer":"gustan","tag":"gustan","sub":"mv."}]}})

# 5 · CLASSIFY — persona → pronombre OI
w({"id":"es-u4-pronombre-oi","title":"El pronombre OI","subtitle":"U4 · welk voornaamwoord (me/te/le…) hoort bij de persoon?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Bij welke persoon hoort dit OI-voornaamwoord?","categories":[
  {"id":"me","label":"a mí","glaze":G["red"]},{"id":"te","label":"a ti","glaze":G["amber"]},
  {"id":"le","label":"a él/ella","glaze":G["green"]},{"id":"nos","label":"a nosotros","glaze":G["blue"]},
  {"id":"os","label":"a vosotros","glaze":G["purple"]},{"id":"les","label":"a ellos","glaze":G["teal"]}],
 "items":[
  {"stimulus":"me","answer":"me","tag":"me","sub":"a mí me"},{"stimulus":"te","answer":"te","tag":"te","sub":"a ti te"},
  {"stimulus":"le","answer":"le","tag":"le","sub":"a él/ella le"},{"stimulus":"nos","answer":"nos","tag":"nos","sub":"a nosotros nos"},
  {"stimulus":"os","answer":"os","tag":"os","sub":"a vosotros os"},{"stimulus":"les","answer":"les","tag":"les","sub":"a ellos les"},
  {"stimulus":"me","answer":"me","tag":"me","sub":"a mí me"},{"stimulus":"le","answer":"le","tag":"le","sub":"a ella le"},
  {"stimulus":"te","answer":"te","tag":"te","sub":"a ti te"},{"stimulus":"les","answer":"les","tag":"les","sub":"a ellas les"},
  {"stimulus":"nos","answer":"nos","tag":"nos","sub":"a nosotras nos"},{"stimulus":"os","answer":"os","tag":"os","sub":"a vosotras os"}]}})

# 6 · CLASSIFY — reacción: también/tampoco/a mí sí/a mí no
w({"id":"es-u4-reaccion","title":"La reacción correcta","subtitle":"U4 · reageer akkoord op de spreker",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Wat zeg je om AKKOORD te gaan met de spreker?","categories":[
  {"id":"tambien","label":"A mí también<br><small>+ akkoord</small>","glaze":G["green"]},
  {"id":"tampoco","label":"A mí tampoco<br><small>– akkoord</small>","glaze":G["blue"]}],
 "items":[
  {"stimulus":"Me gusta el mar.","answer":"tambien","tag":"tambien","sub":"+ → también"},
  {"stimulus":"No me gusta el frío.","answer":"tampoco","tag":"tampoco","sub":"– → tampoco"},
  {"stimulus":"Me encanta bailar.","answer":"tambien","tag":"tambien","sub":"+ → también"},
  {"stimulus":"No me gustan los lunes.","answer":"tampoco","tag":"tampoco","sub":"– → tampoco"},
  {"stimulus":"Me gustan los videojuegos.","answer":"tambien","tag":"tambien","sub":"+ → también"},
  {"stimulus":"No me gusta madrugar.","answer":"tampoco","tag":"tampoco","sub":"– → tampoco"},
  {"stimulus":"Me gusta el cine.","answer":"tambien","tag":"tambien","sub":"+ → también"},
  {"stimulus":"No me gustan las mates.","answer":"tampoco","tag":"tampoco","sub":"– → tampoco"},
  {"stimulus":"Me encanta la playa.","answer":"tambien","tag":"tambien","sub":"+ → también"},
  {"stimulus":"No me gusta el ruido.","answer":"tampoco","tag":"tampoco","sub":"– → tampoco"},
  {"stimulus":"Me gusta leer.","answer":"tambien","tag":"tambien","sub":"+ → también"},
  {"stimulus":"No me gustan las series largas.","answer":"tampoco","tag":"tampoco","sub":"– → tampoco"}]}})

# 7 · CLASSIFY — forma → querer o poder
w({"id":"es-u4-querer-poder","title":"¿querer o poder?","subtitle":"U4 · welke stamwissel: e>ie (querer) of o>ue (poder)?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Van welk werkwoord komt deze vorm?","categories":[
  {"id":"querer","label":"querer<br><small>e → ie (willen)</small>","glaze":G["amber"]},
  {"id":"poder","label":"poder<br><small>o → ue (kunnen)</small>","glaze":G["teal"]}],
 "items":[
  {"stimulus":"quiero","answer":"querer","tag":"querer","sub":"yo quiero"},{"stimulus":"puedo","answer":"poder","tag":"poder","sub":"yo puedo"},
  {"stimulus":"quieres","answer":"querer","tag":"querer","sub":"tú quieres"},{"stimulus":"puedes","answer":"poder","tag":"poder","sub":"tú puedes"},
  {"stimulus":"quiere","answer":"querer","tag":"querer","sub":"él quiere"},{"stimulus":"puede","answer":"poder","tag":"poder","sub":"él puede"},
  {"stimulus":"queremos","answer":"querer","tag":"querer","sub":"nosotros (sin wissel)"},{"stimulus":"podemos","answer":"poder","tag":"poder","sub":"nosotros (sin wissel)"},
  {"stimulus":"quieren","answer":"querer","tag":"querer","sub":"ellos quieren"},{"stimulus":"pueden","answer":"poder","tag":"poder","sub":"ellos pueden"},
  {"stimulus":"queréis","answer":"querer","tag":"querer","sub":"vosotros (sin wissel)"},{"stimulus":"podéis","answer":"poder","tag":"poder","sub":"vosotros (sin wissel)"}]}})

# 8 · CLASSIFY — ¿por qué? vs porque
w({"id":"es-u4-porque","title":"¿por qué o porque?","subtitle":"U4 · vraag (¿por qué?) of reden (porque)?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Vraag (twee woorden + tilde) of reden (één woord)?","categories":[
  {"id":"porqueq","label":"¿por qué?<br><small>waarom (vraag)</small>","glaze":G["blue"]},
  {"id":"porque","label":"porque<br><small>want/omdat (reden)</small>","glaze":G["green"]}],
 "items":[
  {"stimulus":"¿___ te gusta Rosalía?","answer":"porqueq","tag":"porqueq","sub":"vraag"},
  {"stimulus":"Me gusta ___ es divertido.","answer":"porque","tag":"porque","sub":"reden"},
  {"stimulus":"¿___ no quieres ir?","answer":"porqueq","tag":"porqueq","sub":"vraag"},
  {"stimulus":"No puedo ___ trabajo.","answer":"porque","tag":"porque","sub":"reden"},
  {"stimulus":"¿___ estudias español?","answer":"porqueq","tag":"porqueq","sub":"vraag"},
  {"stimulus":"Me encanta ___ es relajante.","answer":"porque","tag":"porque","sub":"reden"},
  {"stimulus":"¿___ no te gusta?","answer":"porqueq","tag":"porqueq","sub":"vraag"},
  {"stimulus":"Bailo ___ me gusta la música.","answer":"porque","tag":"porque","sub":"reden"},
  {"stimulus":"¿___ quieres quedar?","answer":"porqueq","tag":"porqueq","sub":"vraag"},
  {"stimulus":"Voy a la playa ___ hace sol.","answer":"porque","tag":"porque","sub":"reden"},
  {"stimulus":"¿___ te gusta el mar?","answer":"porqueq","tag":"porqueq","sub":"vraag"},
  {"stimulus":"Me gusta ___ es genial.","answer":"porque","tag":"porque","sub":"reden"}]}})

# ============================ ③ PRODUCIR CON APOYO ============================
# 9 · CLOZE — gusta/gustan (concord)
w({"id":"es-u4-gusta-cloze","title":"Completa: gusta o gustan","subtitle":"U4 · kies de juiste vorm van gustar",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Vul gusta of gustan in","items":[
  {"stimulus":"Me ___ los deportes.","options":["gustan","gusta"],"answer":"gustan","tag":"g","sub":"mv."},
  {"stimulus":"Me ___ la música.","options":["gusta","gustan"],"answer":"gusta","tag":"g","sub":"1 ding"},
  {"stimulus":"Me ___ nadar.","options":["gusta","gustan"],"answer":"gusta","tag":"g","sub":"infinitivo"},
  {"stimulus":"¿Te ___ las series?","options":["gustan","gusta"],"answer":"gustan","tag":"g","sub":"mv."},
  {"stimulus":"Nos ___ el mar.","options":["gusta","gustan"],"answer":"gusta","tag":"g","sub":"1 ding"},
  {"stimulus":"Le ___ los videojuegos.","options":["gustan","gusta"],"answer":"gustan","tag":"g","sub":"mv."},
  {"stimulus":"Me ___ bailar y cantar.","options":["gusta","gustan"],"answer":"gusta","tag":"g","sub":"infinitivos → gusta"},
  {"stimulus":"¿Os ___ el cine?","options":["gusta","gustan"],"answer":"gusta","tag":"g","sub":"1 ding"},
  {"stimulus":"Les ___ las canciones.","options":["gustan","gusta"],"answer":"gustan","tag":"g","sub":"mv."},
  {"stimulus":"Me ___ la playa.","options":["gusta","gustan"],"answer":"gusta","tag":"g","sub":"1 ding"}]}})

# 10 · CLOZE — verbo-cloze (VERPLICHT: gustar + querer + poder, nagerekend)
w({"id":"es-u4-verbo-cloze","title":"Completa el verbo","subtitle":"U4 · vul de juiste vorm in (gustar · querer · poder)",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies de juiste werkwoordsvorm","items":[
  {"stimulus":"A nosotros nos ___ las playas.","options":["gustan","gusta","gustamos"],"answer":"gustan","tag":"gustar","sub":"las playas = mv."},
  {"stimulus":"¿___ quedar el sábado?","options":["Quieres","Quiero","Queréis"],"answer":"Quieres","tag":"querer","sub":"querer · tú (e>ie)"},
  {"stimulus":"(A mí) me ___ la música.","options":["encanta","encantan","encanto"],"answer":"encanta","tag":"encantar","sub":"la música = 1"},
  {"stimulus":"Yo no ___ hoy, lo siento.","options":["puedo","puede","pueden"],"answer":"puedo","tag":"poder","sub":"poder · yo (o>ue)"},
  {"stimulus":"¿A ti te ___ los videojuegos?","options":["gustan","gusta","gustas"],"answer":"gustan","tag":"gustar","sub":"mv."},
  {"stimulus":"Nosotros ___ ir al cine.","options":["queremos","queréis","quieren"],"answer":"queremos","tag":"querer","sub":"nosotros (sin wissel)"},
  {"stimulus":"Ella ___ tocar la guitarra.","options":["puede","puedo","podemos"],"answer":"puede","tag":"poder","sub":"poder · ella"},
  {"stimulus":"A ellos les ___ bailar.","options":["gusta","gustan","gustamos"],"answer":"gusta","tag":"gustar","sub":"infinitivo → gusta"},
  {"stimulus":"¿___ venir a la playa?","options":["Podéis","Puedes","Podemos"],"answer":"Podéis","tag":"poder","sub":"poder · vosotros"},
  {"stimulus":"(A mí) me ___ la horchata.","options":["gusta","gustan","gusto"],"answer":"gusta","tag":"gustar","sub":"la horchata = 1"},
  {"stimulus":"Tú ___ ir a la playa, ¿no?","options":["quieres","quiere","queréis"],"answer":"quieres","tag":"querer","sub":"querer · tú"},
  {"stimulus":"¿A vosotros os ___ el reguetón?","options":["gusta","gustan","gustáis"],"answer":"gusta","tag":"gustar","sub":"el reguetón = 1"}]}})

# 11 · CLOZE — pronombre OI in de zin
w({"id":"es-u4-pronombre-cloze","title":"¿me, te, le, nos, os o les?","subtitle":"U4 · vul het juiste OI-voornaamwoord in",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies het juiste voornaamwoord","items":[
  {"stimulus":"(A mí) ___ gusta el mar.","options":["me","te","le"],"answer":"me","tag":"oi","sub":"a mí → me"},
  {"stimulus":"(A ti) ¿___ gusta bailar?","options":["te","me","os"],"answer":"te","tag":"oi","sub":"a ti → te"},
  {"stimulus":"A Bea ___ gusta la playa.","options":["le","les","te"],"answer":"le","tag":"oi","sub":"a ella → le"},
  {"stimulus":"(A nosotros) ___ gustan los conciertos.","options":["nos","os","les"],"answer":"nos","tag":"oi","sub":"a nosotros → nos"},
  {"stimulus":"(A vosotros) ¿___ gusta el cine?","options":["os","nos","le"],"answer":"os","tag":"oi","sub":"a vosotros → os"},
  {"stimulus":"A ellos ___ gusta la música.","options":["les","le","nos"],"answer":"les","tag":"oi","sub":"a ellos → les"},
  {"stimulus":"(A mí) ___ encanta nadar.","options":["me","te","le"],"answer":"me","tag":"oi","sub":"a mí → me"},
  {"stimulus":"A Diego ___ gustan los videojuegos.","options":["le","les","te"],"answer":"le","tag":"oi","sub":"a él → le"},
  {"stimulus":"(A ti) ¿qué ___ gusta hacer?","options":["te","me","os"],"answer":"te","tag":"oi","sub":"a ti → te"},
  {"stimulus":"A mis padres ___ gusta el jazz.","options":["les","le","nos"],"answer":"les","tag":"oi","sub":"a ellos → les"}]}})

# 12 · CLOZE — conectores
w({"id":"es-u4-conectores","title":"Conectores de opinión","subtitle":"U4 · kies y también · pero · además · sobre todo",
 "lang":"es","template":"cloze","options":{"rounds":8,"audio":False},
 "cloze":{"prompt":"Kies het juiste verbindingswoord","items":[
  {"stimulus":"Me gusta el cine, ___ no las series.","options":["pero","y también","además"],"answer":"pero","tag":"c","sub":"tegenstelling"},
  {"stimulus":"Me gusta nadar ___ bailar.","options":["y también","pero","sobre todo"],"answer":"y también","tag":"c","sub":"toevoegen"},
  {"stimulus":"Es divertido; ___, es barato.","options":["además","pero","sobre todo"],"answer":"además","tag":"c","sub":"bovendien"},
  {"stimulus":"Me gusta la música, ___ el pop.","options":["sobre todo","pero","además"],"answer":"sobre todo","tag":"c","sub":"vooral"},
  {"stimulus":"Toco la guitarra ___ canto.","options":["y también","pero","sobre todo"],"answer":"y también","tag":"c","sub":"toevoegen"},
  {"stimulus":"Me gusta el deporte, ___ no el fútbol.","options":["pero","además","y también"],"answer":"pero","tag":"c","sub":"tegenstelling"},
  {"stimulus":"Canta bien; ___, escribe sus letras.","options":["además","pero","sobre todo"],"answer":"además","tag":"c","sub":"bovendien"},
  {"stimulus":"Me encantan los viajes, ___ a la playa.","options":["sobre todo","pero","además"],"answer":"sobre todo","tag":"c","sub":"vooral"}]}})

# 13 · TETRIS — presente regular (actividades) via generator (nagerekend)
w({"id":"es-u4-presente-tetris","title":"Presente regular: serpiente","subtitle":"U4 · lleva la serpiente a la persona correcta · stuur naar de juiste persoon",
 "lang":"es","template":"snake","options":{"rounds":16,"audio":False},
 "generator":{"kind":"conjugation","tense":"pres","pool":"reg","persons":["yo","tu","el","nos","vos","ellos"]},
 "classify":{"categories":[
  {"id":"yo","label":"yo","glaze":G["red"]},{"id":"tu","label":"tú","glaze":G["amber"]},
  {"id":"el","label":"él/ella","glaze":G["green"]},{"id":"nos","label":"nosotros","glaze":G["blue"]},
  {"id":"vos","label":"vosotros","glaze":G["purple"]},{"id":"ellos","label":"ellos","glaze":G["teal"]}]}})

# 14 · TAP — sílaba tónica op U4-woorden
w({"id":"es-u4-tonica","title":"La tónica de los gustos","subtitle":"U4 · tik de sterke lettergreep",
 "lang":"es","template":"tap","options":{"rounds":14,"audio":False},
 "tap":{"prompt":"Tik de sílaba tónica (de sterke lettergreep)","joiner":"·","items":[
  {"parts":["mú","si","ca"],"answer":0,"tag":"esdrujula","sub":"música"},
  {"parts":["can","ción"],"answer":1,"tag":"aguda","sub":"canción · tilde"},
  {"parts":["gui","ta","rra"],"answer":1,"tag":"llana","sub":"guitarra"},
  {"parts":["pe","lí","cu","la"],"answer":1,"tag":"esdrujula","sub":"película"},
  {"parts":["de","por","te"],"answer":1,"tag":"llana","sub":"deporte"},
  {"parts":["fút","bol"],"answer":0,"tag":"llana","sub":"fútbol · tilde"},
  {"parts":["ba","lon","ces","to"],"answer":2,"tag":"llana","sub":"baloncesto"},
  {"parts":["vi","de","o","jue","go"],"answer":3,"tag":"llana","sub":"videojuego"},
  {"parts":["hor","cha","ta"],"answer":1,"tag":"llana","sub":"horchata"},
  {"parts":["pa","e","lla"],"answer":1,"tag":"llana","sub":"paella"},
  {"parts":["fa","vo","ri","to"],"answer":2,"tag":"llana","sub":"favorito"},
  {"parts":["re","gue","tón"],"answer":2,"tag":"aguda","sub":"reguetón · tilde"},
  {"parts":["Va","len","cia"],"answer":1,"tag":"llana","sub":"Valencia"},
  {"parts":["in","te","re","san","te"],"answer":3,"tag":"llana","sub":"interesante"}]}})

# 15 · ORDER — proponer/quedar op de juiste volgorde
w({"id":"es-u4-plan-orden","title":"Ordena el plan","subtitle":"U4 · zet de conversatie (proponer & quedar) in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik de zinnen in de logische volgorde van een plan","rounds":[
  {"tag":"plan","sub":"proponer → aceptar → hora → confirmar","items":[
    {"label":"¿Quieres ir a la playa el sábado?","key":1},{"label":"¡Vale! ¿A qué hora quedamos?","key":2},
    {"label":"¿Podemos quedar a las once?","key":3},{"label":"De acuerdo, ¡hasta el sábado!","key":4}]},
  {"tag":"plan","sub":"gusto → propuesta → aceptar","items":[
    {"label":"Me encanta el cine.","key":1},{"label":"¿Quieres ver una película?","key":2},
    {"label":"Sí, ¿por qué no vamos hoy?","key":3},{"label":"¡Genial! Quedamos a las seis.","key":4}]},
  {"tag":"plan","sub":"pregunta → gusto → reacción → plan","items":[
    {"label":"¿Te gusta la música en directo?","key":1},{"label":"Sí, me encanta.","key":2},
    {"label":"A mí también. ¿Quieres ir a un concierto?","key":3},{"label":"¡Vale! ¿Cuándo?","key":4}]},
  {"tag":"plan","sub":"proponer → no puede → alternativa","items":[
    {"label":"¿Quieres quedar el viernes?","key":1},{"label":"No puedo el viernes.","key":2},
    {"label":"¿Podemos el sábado?","key":3},{"label":"Sí, ¡perfecto!","key":4}]}]}})

# ============================ ④ ANALIZAR & COMUNICAR ============================
# 16 · POINT — foutenjacht: klik de FOUTE gustar-vorm
w({"id":"es-u4-caza-gustar","title":"Caza del error (gustar)","subtitle":"U4 · klik de zin met de FOUTE vorm van gustar",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik de zin waar gustar FOUT is (gusta/gustan)","mode":"one","rounds":[
  {"tag":"gustar","sub":"meervoud → gustan","targets":[
    {"label":"Me gusta el cine"},{"label":"Me gustan los deportes"},{"label":"Me gusta los videojuegos","hit":True},{"label":"Me gusta bailar"}]},
  {"tag":"gustar","sub":"infinitivo → gusta","targets":[
    {"label":"Me gustan las series"},{"label":"Me gustan leer","hit":True},{"label":"Me gusta la playa"},{"label":"Me gustan los conciertos"}]},
  {"tag":"gustar","sub":"1 ding → gusta","targets":[
    {"label":"Me gusta la música"},{"label":"Me gustan la canción","hit":True},{"label":"Me gustan los animales"},{"label":"Me gusta nadar"}]},
  {"tag":"gustar","sub":"OI: a mí → me","targets":[
    {"label":"A mí me gusta el mar"},{"label":"A ti te gustan las pelis"},{"label":"A mí te gusta el cine","hit":True},{"label":"A Bea le gusta la playa"}]},
  {"tag":"gustar","sub":"meervoud → gustan","targets":[
    {"label":"Nos gustan las playas"},{"label":"Nos gusta las montañas","hit":True},{"label":"Nos gusta el sol"},{"label":"Nos gustan los helados"}]}]}})

# 17 · MATCH — pregunta ↔ respuesta (gustos)
w({"id":"es-u4-pregunta-respuesta","title":"Pregunta y respuesta","subtitle":"U4 · koppel de vraag aan het passende antwoord",
 "lang":"es","template":"match","options":{"chunk":5,"audio":False},
 "match":{"prompt":"Verbind elke vraag met het passende antwoord","pairs":[
  {"a":"¿Qué te gusta hacer?","b":"Me gusta nadar."},
  {"a":"¿Te gusta el fútbol?","b":"No, no me gusta."},
  {"a":"¿Por qué te gusta Rosalía?","b":"Porque canta muy bien."},
  {"a":"¿Quieres ir a la playa?","b":"¡Vale! ¿A qué hora?"},
  {"a":"¿A qué hora quedamos?","b":"A las once."},
  {"a":"Me encanta bailar.","b":"A mí también."},
  {"a":"No me gustan los lunes.","b":"A mí tampoco."},
  {"a":"¿Puedes quedar el sábado?","b":"Sí, puedo por la tarde."}]}})

# 18 · MATCH — frase ↔ reacción correcta
w({"id":"es-u4-reaccion-match","title":"El espejo de reacciones","subtitle":"U4 · koppel elke uitspraak aan de logische reactie (akkoord)",
 "lang":"es","template":"match","options":{"chunk":4,"audio":False},
 "match":{"prompt":"Koppel elke uitspraak aan de reactie waarmee je AKKOORD gaat","pairs":[
  {"a":"Me gusta el mar. (+)","b":"A mí también."},
  {"a":"No me gusta el frío. (–)","b":"A mí tampoco."},
  {"a":"Me encanta el cine. (jij niet)","b":"A mí no."},
  {"a":"No me gustan las mates. (jij wél)","b":"A mí sí."},
  {"a":"Me gustan los videojuegos. (+)","b":"¡A mí también!"},
  {"a":"No me gusta madrugar. (–)","b":"¡A mí tampoco!"}]}})

# 19 · SIM — opina (vrije productie met bouwsteen-check)
w({"id":"es-u4-opina","title":"Da tu opinión","subtitle":"U4 · schrijf je smaak — met alle bouwstenen",
 "lang":"es","template":"sim","options":{"audio":False},
 "sim":{"prompt":"Tarea comunicativa · gustos & opinión","rounds":[
  {"scenario":"Escríbele a Bea qué te gusta y qué no.","tag":"opinar","sub":"gebruik: me gusta(n) · no me gusta · porque","min":10,
   "need":[{"re":"me gusta","label":"me gusta(n) …"},{"re":"no me gusta","label":"no me gusta …"},{"re":"porque","label":"porque …"}],
   "bank":["Me gusta","Me gustan","Me encanta","No me gusta","porque","es divertido","los deportes","la música","bailar","y también"],
   "model":"Me encanta la música y me gustan los deportes, pero no me gusta el fútbol porque es aburrido."},
  {"scenario":"Reacciona: «Me gusta bailar. ¿Y a ti?»","tag":"opinar","sub":"reageer + geef een reden","min":8,
   "need":[{"re":"a mí (también|tampoco|sí|no)","label":"a mí también/tampoco/sí/no"},{"re":"me gusta|me encanta|no me gusta","label":"un gusto propio"},{"re":"porque","label":"porque …"}],
   "bank":["A mí también","A mí no","me gusta","me encanta","porque","es genial","nadar","la playa","también"],
   "model":"A mí también me gusta bailar, y me encanta nadar porque es relajante."},
  {"scenario":"Propón un plan a un amigo para el sábado.","tag":"planes","sub":"proponer + hora","min":8,
   "need":[{"re":"quieres|podemos|por qué no","label":"propuesta (querer/poder)"},{"re":"quedamos|a las","label":"hora / quedar"},{"re":"playa|cine|concierto|parque","label":"un lugar/plan"}],
   "bank":["¿Quieres","¿Podemos","ir a la playa","ver una película","quedamos","a las cinco","¿por qué no","el sábado"],
   "model":"¿Quieres ir a la playa el sábado? ¿Podemos quedar a las cinco?"}]}})

# ============================ ⑤ HABLAR · grábate 🎙️ ============================
# 20 · SPEAK repeat — escucha y repite: mis gustos
w({"id":"es-u4-repite-gustos","title":"Escucha y repite: mis gustos","subtitle":"U4 · escucha el modelo, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite en voz alta · grábate ⏺","items":[
  {"text":"Me gusta la música.","sub":"ik vind muziek leuk","tag":"gusto","tip":"¡Bien! Ahora dilo sin leer. <span class='nl'>zeg het nu zonder te lezen.</span>"},
  {"text":"Me gustan los deportes.","sub":"ik vind sport leuk — let op: gusta<b>n</b> (mv.)","tag":"gusto"},
  {"text":"Me encanta bailar.","sub":"ik ben dol op dansen — infinitivo → encanta","tag":"gusto"},
  {"text":"No me gusta el fútbol.","sub":"ik hou niet van voetbal","tag":"gusto"},
  {"text":"¿Y a ti, qué te gusta?","sub":"en jij, wat vind jij leuk?","tag":"interaccion"}]}})

# 21 · SPEAK shadowing — con Bea (afbouwende fasen)
w({"id":"es-u4-shadowing-bea","title":"Shadowing con Bea","subtitle":"U4 · praat mee met Bea, steeds minder tekst",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"shadowing","prompt":"Escucha ▶ · habla al mismo tiempo · grábate ⏺","phases":["Texto completo","Palabras clave","Sin texto","Tu versión"],"items":[
  {"text":"A mí me encanta la música pop.","sub":"ik ben dol op popmuziek","tag":"gusto"},
  {"text":"Los fines de semana voy a la playa.","sub":"in het weekend ga ik naar het strand","tag":"ocio"},
  {"text":"Me gusta bailar, pero no me gustan los videojuegos.","sub":"ik hou van dansen maar niet van videospellen","tag":"gusto"},
  {"text":"¿Quieres ir a un concierto conmigo?","sub":"wil je met mij naar een concert?","tag":"planes","tip":"Ahora invita a un amigo de verdad. <span class='nl'>nodig nu een echte vriend uit.</span>"}]}})

# 22 · SPEAK substitution — carrusel de gustos
w({"id":"es-u4-carrusel-gustos","title":"Carrusel: mis gustos","subtitle":"U4 · één zin, wisselende bouwstenen — grábate",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"substitution","prompt":"Bouw de zin, spreek ze in, grábate ⏺","frame":"Me gusta(n) ___ porque es/son ___.","items":[
  {"text":"Me gusta la playa porque es relajante.","cue":"ronda 1","tag":"gusto"},
  {"text":"Me gustan los conciertos porque son divertidos.","cue":"ronda 2","tag":"gusto"},
  {"text":"Me encanta el cine porque es emocionante.","cue":"ronda 3","tag":"gusto"},
  {"text":"Me gusta(n) ___ porque es/son ___.","cue":"jouw versie","tag":"gusto"}]}})

# 23 · SPEAK voicemessage — propón un plan
w({"id":"es-u4-mensaje-plan","title":"Mensaje de voz: propón un plan","subtitle":"U4 · neem één spraakbericht op met een plan",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz (30 s)","items":[
  {"text":"Propón un plan a Lucía o a Diego para el fin de semana.","cue":"para · Lucía / Diego","tag":"planes",
   "sub":"gebruik: ¿Quieres…? · ¿Podemos…? · quedamos a las…",
   "tip":"Heb je een plan + een uur gezegd? Neem opnieuw op. <span class='nl'>plan + uur? herneem.</span>"}]}})

# 24 · SPEAK repeat — describe los gustos de un personaje (3ª pers.)
w({"id":"es-u4-describe-gustos","title":"Describe los gustos","subtitle":"U4 · beschrijf wat Lucía en Diego leuk vinden, grábate",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · describe a la persona (3ª pers.) · grábate ⏺","items":[
  {"cue":"Lucía · Sevilla 🇪🇸","text":"A Lucía le encanta la música.","sub":"Lucía is dol op muziek — «le encanta»","tag":"describir"},
  {"cue":"Lucía · Sevilla 🇪🇸","text":"Le gusta bailar flamenco.","sub":"ze houdt van flamenco dansen","tag":"describir"},
  {"cue":"Diego · CDMX 🇲🇽","text":"A Diego le gusta el reguetón.","sub":"Diego houdt van reggaeton","tag":"describir"},
  {"cue":"Diego · CDMX 🇲🇽","text":"Le encantan los videojuegos.","sub":"hij is dol op videospellen — «le encantan» (mv.)","tag":"describir",
   "tip":"Ahora describe los gustos de un amigo tuyo. <span class='nl'>beschrijf nu de smaak van een echte vriend(in).</span>"}]}})

print("\n24 U4-spellen geschreven (10 templates: memory·match·classify·cloze·tetris·tap·order·point·sim·speak).")
