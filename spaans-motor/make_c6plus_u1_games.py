#!/usr/bin/env python3
# Genereert de motor-content-JSON's voor C6+ · U1 «El día a día» (rutina · reflexivos · ser/estar · gustar).
# Templates: memory·match·classify·cloze·tetris·order·point·speak (receptief -> productief -> hablar).
# Pools >=12 waar zinvol; options.rounds lager zodat elke herspeling een ANDERE reeks trekt.
# Werkwoordsvormen (reflexivos + gustar) nagerekend/geverifieerd. Slug-prefix = es-c6plus-u1-.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2))
    print("wrote", os.path.basename(p))

G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0","magenta":"#B4309A"}
PRE = "es-c6plus-u1-"

# ============================ ① RECONOCER · woordenschat ============================
# 1 · MEMORY — la rutina (reflexivos + acciones) ES ↔ NL (pool 14)
w({"id":PRE+"rutina-memoria","title":"Memoria de la rutina","subtitle":"U1 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: acción + vertaling","pairs":[
  {"a":"me levanto","b":"ik sta op"},{"a":"me ducho","b":"ik douche"},{"a":"desayuno","b":"ik ontbijt"},
  {"a":"me visto","b":"ik kleed me aan"},{"a":"como","b":"ik eet ('s middags)"},{"a":"me acuesto","b":"ik ga naar bed"},
  {"a":"me despierto","b":"ik word wakker"},{"a":"ceno","b":"ik eet 's avonds"},{"a":"hago los deberes","b":"ik maak huiswerk"},
  {"a":"me peino","b":"ik kam me"},{"a":"salgo de casa","b":"ik ga het huis uit"},{"a":"vuelvo a casa","b":"ik keer terug naar huis"},
  {"a":"me duermo","b":"ik val in slaap"},{"a":"descanso","b":"ik rust uit"}]}})

# 2 · MEMORY — sentimientos (estar + adj) ES ↔ NL (pool 12)
w({"id":PRE+"sentimientos-memoria","title":"¿Cómo estás?","subtitle":"U1 · zoek het gevoel + de vertaling",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: sentimiento + vertaling","pairs":[
  {"a":"contento","b":"blij"},{"a":"cansado","b":"moe"},{"a":"nervioso","b":"nerveus"},
  {"a":"triste","b":"verdrietig"},{"a":"aburrido","b":"verveeld"},{"a":"enfadado","b":"boos"},
  {"a":"relajado","b":"ontspannen"},{"a":"ocupado","b":"druk"},{"a":"feliz","b":"gelukkig"},
  {"a":"estresado","b":"gestrest"},{"a":"tranquilo","b":"rustig"},{"a":"emocionado","b":"opgewonden"}]}})

# 3 · MATCH — la acción ↔ la hora típica (pool 12)
w({"id":PRE+"accion-hora","title":"Acción y hora","subtitle":"U1 · koppel de actie aan een gebruikelijk uur",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind de actie met een logisch uur","pairs":[
  {"a":"me levanto","b":"a las 7:00 🌅"},{"a":"desayuno","b":"a las 7:30 🥐"},
  {"a":"empiezan las clases","b":"a las 8:30 🏫"},{"a":"como","b":"a las 14:00 🍽️"},
  {"a":"meriendo","b":"a las 17:00 🍪"},{"a":"hago los deberes","b":"a las 18:00 📓"},
  {"a":"ceno","b":"a las 21:00 🌙"},{"a":"me acuesto","b":"a las 23:00 🛏️"},
  {"a":"vuelvo a casa","b":"a las 16:00 🏠"},{"a":"me ducho","b":"a las 7:15 🚿"},
  {"a":"quedo con amigos","b":"el sábado 🎉"},{"a":"hago deporte","b":"los martes ⚽"}]}})

# ============================ ② DISTINGUIR · gramática ============================
# 4 · CLASSIFY — ¿reflexivo o no? (pool 16, rounds 10)
w({"id":PRE+"reflexivo-o-no","title":"¿reflexivo o no?","subtitle":"U1 · keert de actie terug naar jezelf?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Is dit werkwoord reflexief (jezelf) of niet?","categories":[
  {"id":"refl","label":"reflexivo<br><small>me/te/se…</small>","glaze":G["purple"]},
  {"id":"no","label":"no reflexivo","glaze":G["teal"]}],
 "items":[
  {"stimulus":"ducharse","answer":"refl","tag":"refl","sub":"me ducho"},
  {"stimulus":"desayunar","answer":"no","tag":"no","sub":"desayuno"},
  {"stimulus":"levantarse","answer":"refl","tag":"refl","sub":"me levanto"},
  {"stimulus":"comer","answer":"no","tag":"no","sub":"como"},
  {"stimulus":"vestirse","answer":"refl","tag":"refl","sub":"me visto"},
  {"stimulus":"hacer los deberes","answer":"no","tag":"no","sub":"hago los deberes"},
  {"stimulus":"peinarse","answer":"refl","tag":"refl","sub":"me peino"},
  {"stimulus":"cenar","answer":"no","tag":"no","sub":"ceno"},
  {"stimulus":"acostarse","answer":"refl","tag":"refl","sub":"me acuesto"},
  {"stimulus":"estudiar","answer":"no","tag":"no","sub":"estudio"},
  {"stimulus":"despertarse","answer":"refl","tag":"refl","sub":"me despierto"},
  {"stimulus":"volver a casa","answer":"no","tag":"no","sub":"vuelvo"},
  {"stimulus":"lavarse los dientes","answer":"refl","tag":"refl","sub":"me lavo los dientes"},
  {"stimulus":"merendar","answer":"no","tag":"no","sub":"meriendo"},
  {"stimulus":"sentarse","answer":"refl","tag":"refl","sub":"me siento"},
  {"stimulus":"salir de casa","answer":"no","tag":"no","sub":"salgo"}]}})

# 5 · CLASSIFY — ¿ser o estar? (pool 18, rounds 12)
w({"id":PRE+"ser-estar","title":"¿ser o estar?","subtitle":"U1 · identiteit/karakter (ser) of plaats/gevoel (estar)?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Kies: ser (permanent) of estar (plaats/gevoel)?","categories":[
  {"id":"ser","label":"ser<br><small>soy/eres/es…</small>","glaze":G["purple"]},
  {"id":"estar","label":"estar<br><small>estoy/estás…</small>","glaze":G["teal"]}],
 "items":[
  {"stimulus":"Lucía ___ de Sevilla.","answer":"ser","tag":"ser","sub":"herkomst → ser"},
  {"stimulus":"Hoy ___ cansado.","answer":"estar","tag":"estar","sub":"gevoel → estar"},
  {"stimulus":"___ simpático.","answer":"ser","tag":"ser","sub":"karakter → ser"},
  {"stimulus":"La mochila ___ en clase.","answer":"estar","tag":"estar","sub":"plaats → estar"},
  {"stimulus":"___ estudiante.","answer":"ser","tag":"ser","sub":"identiteit → ser"},
  {"stimulus":"Diego ___ contento.","answer":"estar","tag":"estar","sub":"gevoel → estar"},
  {"stimulus":"Nosotros ___ de Bélgica.","answer":"ser","tag":"ser","sub":"herkomst → ser"},
  {"stimulus":"¿Cómo ___ (tú)?","answer":"estar","tag":"estar","sub":"toestand → estar"},
  {"stimulus":"El profesor ___ alto.","answer":"ser","tag":"ser","sub":"eigenschap → ser"},
  {"stimulus":"La ventana ___ abierta.","answer":"estar","tag":"estar","sub":"toestand → estar"},
  {"stimulus":"Son las dos: ___ mediodía.","answer":"ser","tag":"ser","sub":"tijd → ser"},
  {"stimulus":"___ nervioso por el examen.","answer":"estar","tag":"estar","sub":"gevoel → estar"},
  {"stimulus":"Mi hermana ___ profesora.","answer":"ser","tag":"ser","sub":"beroep → ser"},
  {"stimulus":"El café ___ caliente.","answer":"estar","tag":"estar","sub":"toestand → estar"},
  {"stimulus":"___ alegre y hablador.","answer":"ser","tag":"ser","sub":"karakter → ser"},
  {"stimulus":"Los alumnos ___ en el patio.","answer":"estar","tag":"estar","sub":"plaats → estar"},
  {"stimulus":"La paella ___ rica hoy.","answer":"estar","tag":"estar","sub":"smaak nu → estar"},
  {"stimulus":"Sevilla ___ en el sur.","answer":"estar","tag":"estar","sub":"ligging → estar"}]}})

# 6 · CLASSIFY — ¿gusta o gustan? (pool 16, rounds 10)
w({"id":PRE+"gusta-gustan","title":"¿gusta o gustan?","subtitle":"U1 · 1 ding/infinitivo (gusta) of meerdere (gustan)?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Kies gusta (1 ding/infinitivo) of gustan (meerdere)?","categories":[
  {"id":"gusta","label":"gusta<br><small>1 ding / inf.</small>","glaze":G["purple"]},
  {"id":"gustan","label":"gustan<br><small>meervoud</small>","glaze":G["magenta"]}],
 "items":[
  {"stimulus":"Me ___ el fútbol.","answer":"gusta","tag":"gusta","sub":"el fútbol (1)"},
  {"stimulus":"Me ___ los perros.","answer":"gustan","tag":"gustan","sub":"los perros (varios)"},
  {"stimulus":"Me ___ bailar.","answer":"gusta","tag":"gusta","sub":"infinitivo → gusta"},
  {"stimulus":"Me ___ las películas.","answer":"gustan","tag":"gustan","sub":"las películas (varias)"},
  {"stimulus":"Me ___ la música.","answer":"gusta","tag":"gusta","sub":"la música (1)"},
  {"stimulus":"Me ___ los videojuegos.","answer":"gustan","tag":"gustan","sub":"los videojuegos (varios)"},
  {"stimulus":"Me ___ cantar y bailar.","answer":"gusta","tag":"gusta","sub":"infinitivos → gusta"},
  {"stimulus":"Me ___ las vacaciones.","answer":"gustan","tag":"gustan","sub":"las vacaciones (varias)"},
  {"stimulus":"Me ___ el chocolate.","answer":"gusta","tag":"gusta","sub":"el chocolate (1)"},
  {"stimulus":"Me ___ los deportes.","answer":"gustan","tag":"gustan","sub":"los deportes (varios)"},
  {"stimulus":"Me ___ leer.","answer":"gusta","tag":"gusta","sub":"infinitivo → gusta"},
  {"stimulus":"Me ___ las flores.","answer":"gustan","tag":"gustan","sub":"las flores (varias)"},
  {"stimulus":"Me ___ el reguetón.","answer":"gusta","tag":"gusta","sub":"el reguetón (1)"},
  {"stimulus":"Me ___ los fines de semana.","answer":"gustan","tag":"gustan","sub":"varios"},
  {"stimulus":"Me ___ la comida española.","answer":"gusta","tag":"gusta","sub":"la comida (1)"},
  {"stimulus":"Me ___ los lunes… ¡no!","answer":"gustan","tag":"gustan","sub":"los lunes (varios)"}]}})

# ============================ ③ PRODUCIR CON APOYO ============================
# 7 · CLOZE — los reflexivos (VERPLICHT werkwoord-cloze, nagerekend) (pool 20, rounds 12)
w({"id":PRE+"reflexivos","title":"Completa: los reflexivos","subtitle":"U1 · pronombre + verbo (me levanto, te duchas…)",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies de juiste reflexieve vorm","items":[
  {"stimulus":"(Yo) ___ a las siete.","options":["me levanto","te levantas","se levanta"],"answer":"me levanto","tag":"levantarse","sub":"yo → me levanto"},
  {"stimulus":"¿(Tú) ___ por la mañana?","options":["te duchas","me ducho","se ducha"],"answer":"te duchas","tag":"ducharse","sub":"tú → te duchas"},
  {"stimulus":"Lucía ___ muy temprano.","options":["se despierta","me despierto","te despiertas"],"answer":"se despierta","tag":"despertarse","sub":"ella → se despierta"},
  {"stimulus":"(Nosotros) ___ a las once.","options":["nos acostamos","os acostáis","se acuestan"],"answer":"nos acostamos","tag":"acostarse","sub":"nosotros → nos acostamos"},
  {"stimulus":"Diego ___ rápido.","options":["se viste","me visto","te vistes"],"answer":"se viste","tag":"vestirse","sub":"él → se viste"},
  {"stimulus":"(Yo) ___ enseguida.","options":["me duermo","te duermes","se duerme"],"answer":"me duermo","tag":"dormirse","sub":"yo → me duermo"},
  {"stimulus":"¿(Vosotros) ___ aquí?","options":["os sentáis","se sientan","nos sentamos"],"answer":"os sentáis","tag":"sentarse","sub":"vosotros → os sentáis"},
  {"stimulus":"Mis hermanos ___ delante del espejo.","options":["se peinan","nos peinamos","os peináis"],"answer":"se peinan","tag":"peinarse","sub":"ellos → se peinan"},
  {"stimulus":"(Tú) ___ los dientes.","options":["te lavas","me lavo","se lava"],"answer":"te lavas","tag":"lavarse","sub":"tú → te lavas"},
  {"stimulus":"(Yo) ___ a las siete y cuarto.","options":["me levanto","me levantas","me levanta"],"answer":"me levanto","tag":"levantarse","sub":"yo → me levanto"},
  {"stimulus":"Ella ___ por la noche.","options":["se ducha","te duchas","me ducho"],"answer":"se ducha","tag":"ducharse","sub":"ella → se ducha"},
  {"stimulus":"(Nosotros) ___ temprano.","options":["nos despertamos","os despertáis","se despiertan"],"answer":"nos despertamos","tag":"despertarse","sub":"nosotros → nos despertamos"},
  {"stimulus":"(Yo) ___ a las once.","options":["me acuesto","te acuestas","se acuesta"],"answer":"me acuesto","tag":"acostarse","sub":"yo → me acuesto"},
  {"stimulus":"¿(Tú) ___ elegante?","options":["te vistes","me visto","se viste"],"answer":"te vistes","tag":"vestirse","sub":"tú → te vistes"},
  {"stimulus":"Los niños ___ a las nueve.","options":["se acuestan","nos acostamos","os acostáis"],"answer":"se acuestan","tag":"acostarse","sub":"ellos → se acuestan"},
  {"stimulus":"(Vosotros) ___ tarde.","options":["os levantáis","nos levantamos","se levantan"],"answer":"os levantáis","tag":"levantarse","sub":"vosotros → os levantáis"},
  {"stimulus":"Mi madre ___ a las seis.","options":["se despierta","me despierto","te despiertas"],"answer":"se despierta","tag":"despertarse","sub":"ella → se despierta"},
  {"stimulus":"(Yo) ___ en el sofá.","options":["me siento","te sientas","se sienta"],"answer":"me siento","tag":"sentarse","sub":"yo → me siento"},
  {"stimulus":"¿(Vosotros) ___ pronto?","options":["os duchais","nos duchamos","se duchan"],"answer":"os duchais","tag":"ducharse","sub":"vosotros → os ducháis"},
  {"stimulus":"Diego y yo ___ deporte y luego ___.","options":["hacemos … nos duchamos","hago … me ducho","hacéis … os ducháis"],"answer":"hacemos … nos duchamos","tag":"nosotros","sub":"nosotros → nos duchamos"}]}})

# 8 · CLOZE — gustar (gusta/gustan + pronombres) (pool 16, rounds 10)
w({"id":PRE+"gustar","title":"Completa: gustar","subtitle":"U1 · me/te/le… + gusta/gustan",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm van gustar","items":[
  {"stimulus":"A mí ___ el fútbol.","options":["me gusta","me gustan","te gusta"],"answer":"me gusta","tag":"g","sub":"a mí → me · el fútbol (1)"},
  {"stimulus":"A mí ___ los perros.","options":["me gustan","me gusta","le gustan"],"answer":"me gustan","tag":"g","sub":"me · los perros (varios)"},
  {"stimulus":"A Lucía ___ bailar.","options":["le gusta","le gustan","les gusta"],"answer":"le gusta","tag":"g","sub":"a Lucía → le · inf."},
  {"stimulus":"¿A ti ___ los deportes?","options":["te gustan","te gusta","os gustan"],"answer":"te gustan","tag":"g","sub":"a ti → te · varios"},
  {"stimulus":"A nosotros ___ viajar.","options":["nos gusta","nos gustan","les gusta"],"answer":"nos gusta","tag":"g","sub":"nosotros → nos · inf."},
  {"stimulus":"A mis padres ___ los domingos.","options":["les gustan","le gustan","les gusta"],"answer":"les gustan","tag":"g","sub":"a ellos → les · varios"},
  {"stimulus":"A ella no ___ nada el terror.","options":["le gusta","le gustan","les gusta"],"answer":"le gusta","tag":"g","sub":"le · el terror (1)"},
  {"stimulus":"A mí ___ la música latina.","options":["me gusta","me gustan","te gusta"],"answer":"me gusta","tag":"g","sub":"me · la música (1)"},
  {"stimulus":"¿A vosotros ___ las comedias?","options":["os gustan","os gusta","nos gustan"],"answer":"os gustan","tag":"g","sub":"a vosotros → os · varias"},
  {"stimulus":"A Diego ___ los videojuegos.","options":["le gustan","le gusta","les gustan"],"answer":"le gustan","tag":"g","sub":"le · los videojuegos (varios)"},
  {"stimulus":"A mí ___ leer y cantar.","options":["me gusta","me gustan","le gusta"],"answer":"me gusta","tag":"g","sub":"me · infinitivos → gusta"},
  {"stimulus":"A ti ___ el chocolate.","options":["te gusta","te gustan","le gusta"],"answer":"te gusta","tag":"g","sub":"te · el chocolate (1)"},
  {"stimulus":"A nosotros ___ las vacaciones.","options":["nos gustan","nos gusta","os gustan"],"answer":"nos gustan","tag":"g","sub":"nos · las vacaciones (varias)"},
  {"stimulus":"A los niños ___ el helado.","options":["les gusta","les gustan","le gusta"],"answer":"les gusta","tag":"g","sub":"les · el helado (1)"},
  {"stimulus":"A mí me ___ mucho las flores.","options":["gustan","gusta","encanta"],"answer":"gustan","tag":"g","sub":"las flores (varias) → gustan"},
  {"stimulus":"A ti ___ los lunes… ¡qué raro!","options":["te gustan","te gusta","le gustan"],"answer":"te gustan","tag":"g","sub":"te · los lunes (varios)"}]}})

# 9 · TETRIS — el pronombre reflexivo (valt in de juiste kolom) (pool 18)
w({"id":PRE+"pronombre-tetris","title":"Pronombre Tetris","subtitle":"U1 · laat het juiste pronomen (me/te/se…) vallen",
 "lang":"es","template":"tetris","options":{"rows":9,"speed":1300,"audio":False},
 "classify":{"categories":[
  {"id":"me","label":"me","glaze":G["blue"]},{"id":"te","label":"te","glaze":G["red"]},
  {"id":"se","label":"se","glaze":G["green"]},{"id":"nos","label":"nos","glaze":G["amber"]}],
 "items":[
  {"stimulus":"yo ___ levanto","answer":"me","tag":"me","sub":"yo → me"},
  {"stimulus":"tú ___ duchas","answer":"te","tag":"te","sub":"tú → te"},
  {"stimulus":"ella ___ despierta","answer":"se","tag":"se","sub":"ella → se"},
  {"stimulus":"nosotros ___ acostamos","answer":"nos","tag":"nos","sub":"nosotros → nos"},
  {"stimulus":"yo ___ visto","answer":"me","tag":"me","sub":"yo → me"},
  {"stimulus":"tú ___ peinas","answer":"te","tag":"te","sub":"tú → te"},
  {"stimulus":"él ___ acuesta","answer":"se","tag":"se","sub":"él → se"},
  {"stimulus":"nosotros ___ duchamos","answer":"nos","tag":"nos","sub":"nosotros → nos"},
  {"stimulus":"yo ___ despierto","answer":"me","tag":"me","sub":"yo → me"},
  {"stimulus":"tú ___ acuestas","answer":"te","tag":"te","sub":"tú → te"},
  {"stimulus":"ellos ___ levantan","answer":"se","tag":"se","sub":"ellos → se"},
  {"stimulus":"nosotros ___ vestimos","answer":"nos","tag":"nos","sub":"nosotros → nos"},
  {"stimulus":"yo ___ acuesto","answer":"me","tag":"me","sub":"yo → me"},
  {"stimulus":"tú ___ sientas","answer":"te","tag":"te","sub":"tú → te"},
  {"stimulus":"usted ___ ducha","answer":"se","tag":"se","sub":"usted → se"},
  {"stimulus":"nosotros ___ peinamos","answer":"nos","tag":"nos","sub":"nosotros → nos"},
  {"stimulus":"yo ___ duermo","answer":"me","tag":"me","sub":"yo → me"},
  {"stimulus":"María ___ maquilla","answer":"se","tag":"se","sub":"ella → se"}]}})

# 10 · ORDER — ordena tu rutina (8 rondes)
w({"id":PRE+"rutina-order","title":"Ordena tu día","subtitle":"U1 · zet de acties in de logische volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik de acties in de logische volgorde van een dag","rounds":[
  {"tag":"dia","sub":"la mañana","items":[
    {"label":"Me despierto a las 7:00.","key":1},{"label":"Me ducho.","key":2},
    {"label":"Desayuno.","key":3},{"label":"Salgo de casa.","key":4}]},
  {"tag":"dia","sub":"el día completo","items":[
    {"label":"Me levanto.","key":1},{"label":"Como a las dos.","key":2},
    {"label":"Hago los deberes.","key":3},{"label":"Me acuesto.","key":4}]},
  {"tag":"dia","sub":"con conectores","items":[
    {"label":"Primero me levanto.","key":1},{"label":"Luego me visto.","key":2},
    {"label":"Después desayuno.","key":3},{"label":"Por último, voy al insti.","key":4}]},
  {"tag":"hora","sub":"de menor a mayor (la hora)","items":[
    {"label":"Es la una.","key":1},{"label":"Son las tres y cuarto.","key":2},
    {"label":"Son las seis y media.","key":3},{"label":"Son las nueve.","key":4}]},
  {"tag":"dia","sub":"la tarde y la noche","items":[
    {"label":"Vuelvo a casa a las seis.","key":1},{"label":"Meriendo.","key":2},
    {"label":"Ceno a las nueve.","key":3},{"label":"Me duermo.","key":4}]},
  {"tag":"opinion","sub":"una opinión (me gusta… porque)","items":[
    {"label":"Me gusta el fin de semana","key":1},{"label":"porque","key":2},
    {"label":"no hay clase","key":3},{"label":"y quedo con amigos.","key":4}]},
  {"tag":"dia","sub":"la rutina de Lucía","items":[
    {"label":"Lucía se despierta a las siete.","key":1},{"label":"Se ducha.","key":2},
    {"label":"Desayuna tostadas.","key":3},{"label":"Va al instituto.","key":4}]},
  {"tag":"frecuencia","sub":"de + a − (frecuencia)","items":[
    {"label":"siempre","key":1},{"label":"normalmente","key":2},
    {"label":"a veces","key":3},{"label":"nunca","key":4}]}]}})

# 11 · POINT — señala (repaso gemengd) (10 rondes)
w({"id":PRE+"senala","title":"Señala","subtitle":"U1 · klik het juiste antwoord",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het gevraagde item","mode":"one","rounds":[
  {"tag":"refl","sub":"señala el verbo reflexivo","targets":[
    {"label":"desayunar"},{"label":"ducharse","hit":True},{"label":"comer"},{"label":"estudiar"}]},
  {"tag":"pron","sub":"¿qué pronombre va con «yo»?","targets":[
    {"label":"te"},{"label":"se"},{"label":"me","hit":True},{"label":"nos"}]},
  {"tag":"serestar","sub":"señala la frase con «estar»","targets":[
    {"label":"Soy de Sevilla"},{"label":"Estoy cansado","hit":True},{"label":"Soy alto"},{"label":"Es profesor"}]},
  {"tag":"gustar","sub":"señala la forma correcta: «Me ___ los perros»","targets":[
    {"label":"gusta"},{"label":"gustan","hit":True},{"label":"gusto"},{"label":"gustas"}]},
  {"tag":"hora","sub":"señala «son las tres y media»","targets":[
    {"label":"3:15"},{"label":"3:45"},{"label":"3:30","hit":True},{"label":"2:30"}]},
  {"tag":"sentim","sub":"señala un sentimiento","targets":[
    {"label":"cansado","hit":True},{"label":"lunes"},{"label":"ducharse"},{"label":"a veces"}]},
  {"tag":"frecuencia","sub":"señala un adverbio de frecuencia","targets":[
    {"label":"primero"},{"label":"siempre","hit":True},{"label":"contento"},{"label":"cuarto"}]},
  {"tag":"conector","sub":"señala un conector de secuencia","targets":[
    {"label":"porque"},{"label":"luego","hit":True},{"label":"también"},{"label":"pero"}]},
  {"tag":"gustar","sub":"señala «a mí también» (bij +)","targets":[
    {"label":"a mí tampoco"},{"label":"a mí también","hit":True},{"label":"a mí no"},{"label":"yo también"}]},
  {"tag":"refl","sub":"señala la forma «nosotros» de levantarse","targets":[
    {"label":"me levanto"},{"label":"nos levantamos","hit":True},{"label":"os levantáis"},{"label":"se levantan"}]}]}})

# ============================ ⑤ HABLAR · grábate 🎙️ ============================
# 12 · SPEAK repeat — escucha y repite: mi rutina y mis gustos (8 items)
w({"id":PRE+"repite-dia","title":"Escucha y repite: mi día","subtitle":"U1 · escucha el modelo, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite en voz alta · grábate ⏺","items":[
  {"text":"Me levanto a las siete y cuarto.","sub":"ik sta op om kwart over zeven","tag":"rutina","tip":"¡Bien! Ahora dilo sin leer. <span class='nl'>zeg het nu zonder te lezen.</span>"},
  {"text":"Primero me ducho y luego desayuno.","sub":"eerst douche ik, dan ontbijt ik","tag":"rutina"},
  {"text":"Como a las dos y ceno a las nueve.","sub":"ik eet om twee en negen uur","tag":"hora"},
  {"text":"Me gusta bailar porque es divertido.","sub":"ik dans graag want het is leuk","tag":"opinion"},
  {"text":"No me gustan nada los lunes.","sub":"ik vind maandagen helemaal niet leuk","tag":"gustar"},
  {"text":"Hoy estoy contento porque es viernes.","sub":"vandaag ben ik blij want het is vrijdag","tag":"serestar"},
  {"text":"Normalmente me acuesto a las once.","sub":"meestal ga ik om elf uur slapen","tag":"frecuencia"},
  {"text":"¿A qué hora te levantas tú?","sub":"hoe laat sta jij op?","tag":"interaccion"}]}})

# 13 · SPEAK voicemessage — describe tu día y tus gustos (3 items)
w({"id":PRE+"mensaje-dia","title":"Mensaje de voz: mi día a día","subtitle":"U1 · neem een spraakbericht op over je dag",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz (30–40 s)","items":[
  {"text":"Describe tu rutina: usa 5 verbos reflexivos + la hora + conectores.","cue":"mi día","tag":"rutina",
   "sub":"gebruik: me levanto · me ducho · a las… · primero · luego · después",
   "tip":"5 reflexieve werkwoorden + de hora? Neem opnieuw op. <span class='nl'>5 reflexieven + uur? herneem.</span>"},
  {"text":"Di qué te gusta y qué no, con «porque».","cue":"mis gustos","tag":"opinion",
   "sub":"gebruik: me gusta · me encanta · no me gusta nada · porque",
   "tip":"2 gustos + 1 porque? Herneem. <span class='nl'>2 smaken + reden? herneem.</span>"},
  {"text":"Di cómo te sientes hoy y por qué (ser/estar).","cue":"¿cómo estás?","tag":"serestar",
   "sub":"gebruik: estoy contento/cansado… porque…",
   "tip":"estar + gevoel + porque gebruikt? Herneem. <span class='nl'>estar + gevoel + reden? herneem.</span>"}]}})

print("\n13 C6+·U1-spellen geschreven (8 templates: memory·match·classify·cloze·tetris·order·point·speak).")
print("Pools >=12 waar zinvol; options.rounds lager => herspeling geeft een andere reeks.")
