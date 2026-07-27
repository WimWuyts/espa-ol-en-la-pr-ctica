#!/usr/bin/env python3
# Genereert de motor-content-JSON's voor C6+ · U0 «¡Volvemos!» (reencuentro · diagnostische repaso).
# Templates: classify·match·memory·cloze·order·point·tetris·speak (receptief -> productief -> hablar).
# Pools >=12 waar zinvol; options.rounds lager zodat elke herspeling een ANDERE reeks trekt.
# Werkwoordsvormen (presente reg. + ser/estar/tener/ir/hacer/venir/dar) nagerekend/geverifieerd.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2))
    print("wrote", os.path.basename(p))

G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0"}
PRE = "es-c6plus-u0-"

# ============================ ① RECONOCER · woordenschat ============================
# 1 · MEMORY — saludos/presentarse ES ↔ NL (pool 14)
w({"id":PRE+"saludos-memoria","title":"Memoria del reencuentro","subtitle":"U0 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om en zoek het woord + de vertaling","pairs":[
  {"a":"hola","b":"hallo"},{"a":"buenos días","b":"goedemorgen"},{"a":"adiós","b":"tot ziens"},
  {"a":"me llamo","b":"ik heet"},{"a":"soy de","b":"ik kom uit"},{"a":"tengo … años","b":"ik ben … jaar"},
  {"a":"¿cómo te llamas?","b":"hoe heet je?"},{"a":"encantado","b":"aangenaam"},{"a":"gracias","b":"dank je"},
  {"a":"la lengua","b":"de taal"},{"a":"el amigo","b":"de vriend"},{"a":"vivo en","b":"ik woon in"},
  {"a":"¿de dónde eres?","b":"waar kom je vandaan?"},{"a":"hasta luego","b":"tot straks"}]}})

# 2 · MEMORY — bandera ↔ país (pool 12)
w({"id":PRE+"paises-memoria","title":"Banderas y países","subtitle":"U0 · zoek de vlag bij het land",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: vlag + land","pairs":[
  {"a":"🇪🇸","b":"España"},{"a":"🇲🇽","b":"México"},{"a":"🇨🇴","b":"Colombia"},
  {"a":"🇵🇪","b":"Perú"},{"a":"🇦🇷","b":"Argentina"},{"a":"🇧🇪","b":"Bélgica"},
  {"a":"🇨🇱","b":"Chile"},{"a":"🇨🇺","b":"Cuba"},{"a":"🇻🇪","b":"Venezuela"},
  {"a":"🇪🇨","b":"Ecuador"},{"a":"🇺🇾","b":"Uruguay"},{"a":"🇬🇹","b":"Guatemala"}]}})

# 3 · MATCH — país ↔ nacionalidad (pool 12, blokjes van 6)
w({"id":PRE+"pais-nacionalidad","title":"País y nacionalidad","subtitle":"U0 · koppel het land aan de nationaliteit",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind het land met de nationaliteit","pairs":[
  {"a":"España","b":"español/a 🇪🇸"},{"a":"México","b":"mexicano/a 🇲🇽"},
  {"a":"Colombia","b":"colombiano/a 🇨🇴"},{"a":"Perú","b":"peruano/a 🇵🇪"},
  {"a":"Argentina","b":"argentino/a 🇦🇷"},{"a":"Bélgica","b":"belga 🇧🇪"},
  {"a":"Chile","b":"chileno/a 🇨🇱"},{"a":"Cuba","b":"cubano/a 🇨🇺"},
  {"a":"Venezuela","b":"venezolano/a 🇻🇪"},{"a":"Ecuador","b":"ecuatoriano/a 🇪🇨"},
  {"a":"Alemania","b":"alemán/alemana 🇩🇪"},{"a":"Francia","b":"francés/francesa 🇫🇷"}]}})

# ============================ ② DISTINGUIR · gramática/léxico ============================
# 4 · CLASSIFY — ¿formal o informal? (pool 16, rounds 10)
w({"id":PRE+"formal-informal","title":"¿formal o informal?","subtitle":"U0 · tú of usted?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Is deze uitdrukking formal (usted) of informal (tú)?","categories":[
  {"id":"formal","label":"formal<br><small>usted</small>","glaze":G["blue"]},
  {"id":"informal","label":"informal<br><small>tú</small>","glaze":G["green"]}],
 "items":[
  {"stimulus":"¿Cómo estás?","answer":"informal","tag":"informal","sub":"tú → estás"},
  {"stimulus":"¿Cómo está usted?","answer":"formal","tag":"formal","sub":"usted → está"},
  {"stimulus":"¿De dónde eres?","answer":"informal","tag":"informal","sub":"tú → eres"},
  {"stimulus":"¿De dónde es usted?","answer":"formal","tag":"formal","sub":"usted → es"},
  {"stimulus":"¿Cómo te llamas?","answer":"informal","tag":"informal","sub":"tú → te llamas"},
  {"stimulus":"¿Cómo se llama usted?","answer":"formal","tag":"formal","sub":"usted → se llama"},
  {"stimulus":"¡Hola! ¿Qué tal?","answer":"informal","tag":"informal","sub":"informele groet"},
  {"stimulus":"Buenos días, señor.","answer":"formal","tag":"formal","sub":"formeel, señor"},
  {"stimulus":"¿Tienes un boli?","answer":"informal","tag":"informal","sub":"tú → tienes"},
  {"stimulus":"¿Tiene usted hora?","answer":"formal","tag":"formal","sub":"usted → tiene"},
  {"stimulus":"¿Dónde vives?","answer":"informal","tag":"informal","sub":"tú → vives"},
  {"stimulus":"¿Dónde vive usted?","answer":"formal","tag":"formal","sub":"usted → vive"},
  {"stimulus":"Encantado de conocerle.","answer":"formal","tag":"formal","sub":"formeel/beleefd"},
  {"stimulus":"Oye, ¿me ayudas?","answer":"informal","tag":"informal","sub":"'oye' + tú"},
  {"stimulus":"¿Puede repetir, por favor?","answer":"formal","tag":"formal","sub":"usted → puede"},
  {"stimulus":"¿Me pasas el boli?","answer":"informal","tag":"informal","sub":"tú → pasas"}]}})

# 5 · CLASSIFY — ¿el o la? (género) (pool 20, rounds 12)
w({"id":PRE+"genero","title":"¿el o la?","subtitle":"U0 · masculino of femenino?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Welk lidwoord past: el (m) of la (v)?","categories":[
  {"id":"el","label":"el<br><small>masculino</small>","glaze":G["blue"]},
  {"id":"la","label":"la<br><small>femenino</small>","glaze":G["red"]}],
 "items":[
  {"stimulus":"___ libro","answer":"el","tag":"el","sub":"el libro (m)"},
  {"stimulus":"___ casa","answer":"la","tag":"la","sub":"la casa (f)"},
  {"stimulus":"___ chico","answer":"el","tag":"el","sub":"el chico (m)"},
  {"stimulus":"___ chica","answer":"la","tag":"la","sub":"la chica (f)"},
  {"stimulus":"___ familia","answer":"la","tag":"la","sub":"la familia (f)"},
  {"stimulus":"___ amigo","answer":"el","tag":"el","sub":"el amigo (m)"},
  {"stimulus":"___ profesora","answer":"la","tag":"la","sub":"la profesora (f)"},
  {"stimulus":"___ problema","answer":"el","tag":"el","sub":"el problema (m! -ma)"},
  {"stimulus":"___ mano","answer":"la","tag":"la","sub":"la mano (f! -o)"},
  {"stimulus":"___ día","answer":"el","tag":"el","sub":"el día (m! -a)"},
  {"stimulus":"___ ciudad","answer":"la","tag":"la","sub":"la ciudad (f, -dad)"},
  {"stimulus":"___ mapa","answer":"el","tag":"el","sub":"el mapa (m! -a)"},
  {"stimulus":"___ lengua","answer":"la","tag":"la","sub":"la lengua (f)"},
  {"stimulus":"___ país","answer":"el","tag":"el","sub":"el país (m)"},
  {"stimulus":"___ hermana","answer":"la","tag":"la","sub":"la hermana (f)"},
  {"stimulus":"___ padre","answer":"el","tag":"el","sub":"el padre (m)"},
  {"stimulus":"___ foto","answer":"la","tag":"la","sub":"la foto (f! -o)"},
  {"stimulus":"___ idioma","answer":"el","tag":"el","sub":"el idioma (m! -ma)"},
  {"stimulus":"___ nacionalidad","answer":"la","tag":"la","sub":"la nacionalidad (f, -dad)"},
  {"stimulus":"___ instituto","answer":"el","tag":"el","sub":"el instituto (m)"}]}})

# 6 · CLASSIFY — ¿ser (soy) o estar (estoy)? (pool 16, rounds 10)
w({"id":PRE+"ser-estar","title":"¿soy o estoy?","subtitle":"U0 · ser (wie/wat) of estar (waar/hoe)?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Kies: soy (identiteit) of estoy (plaats/gevoel)?","categories":[
  {"id":"soy","label":"soy<br><small>ser · wie/wat</small>","glaze":G["purple"]},
  {"id":"estoy","label":"estoy<br><small>estar · waar/hoe</small>","glaze":G["teal"]}],
 "items":[
  {"stimulus":"___ de Bélgica.","answer":"soy","tag":"soy","sub":"herkomst → ser"},
  {"stimulus":"___ en clase.","answer":"estoy","tag":"estoy","sub":"plaats → estar"},
  {"stimulus":"___ estudiante.","answer":"soy","tag":"soy","sub":"identiteit → ser"},
  {"stimulus":"Hoy ___ contento.","answer":"estoy","tag":"estoy","sub":"gevoel → estar"},
  {"stimulus":"___ alto y moreno.","answer":"soy","tag":"soy","sub":"eigenschap → ser"},
  {"stimulus":"___ muy bien, gracias.","answer":"estoy","tag":"estoy","sub":"toestand → estar"},
  {"stimulus":"___ belga.","answer":"soy","tag":"soy","sub":"nationaliteit → ser"},
  {"stimulus":"___ en casa.","answer":"estoy","tag":"estoy","sub":"plaats → estar"},
  {"stimulus":"___ simpático.","answer":"soy","tag":"soy","sub":"karakter → ser"},
  {"stimulus":"___ cansado hoy.","answer":"estoy","tag":"estoy","sub":"gevoel → estar"},
  {"stimulus":"___ el hermano de Nina.","answer":"soy","tag":"soy","sub":"identiteit → ser"},
  {"stimulus":"___ en el mercado.","answer":"estoy","tag":"estoy","sub":"plaats → estar"},
  {"stimulus":"___ profesor de español.","answer":"soy","tag":"soy","sub":"beroep → ser"},
  {"stimulus":"___ nervioso antes del examen.","answer":"estoy","tag":"estoy","sub":"gevoel → estar"},
  {"stimulus":"___ de Sevilla.","answer":"soy","tag":"soy","sub":"herkomst → ser"},
  {"stimulus":"___ aquí, en la parada.","answer":"estoy","tag":"estoy","sub":"plaats → estar"}]}})

# ============================ ③ PRODUCIR CON APOYO ============================
# 7 · CLOZE — presente (VERPLICHT werkwoord-cloze, nagerekend) (pool 20, rounds 12)
w({"id":PRE+"presente","title":"Completa: el presente","subtitle":"U0 · vervoeg in het presente (regular + ser/estar/tener/ir…)",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm in het presente","items":[
  {"stimulus":"(Yo) ___ de Bélgica.","options":["soy","eres","es"],"answer":"soy","tag":"ser","sub":"yo → soy"},
  {"stimulus":"¿(Tú) ___ en Gante?","options":["vives","vivo","vive"],"answer":"vives","tag":"vivir","sub":"tú → vives"},
  {"stimulus":"Nina ___ dieciséis años.","options":["tiene","tienes","tengo"],"answer":"tiene","tag":"tener","sub":"ella → tiene"},
  {"stimulus":"(Nosotros) ___ español en clase.","options":["hablamos","habláis","hablan"],"answer":"hablamos","tag":"hablar","sub":"nosotros → hablamos"},
  {"stimulus":"Diego ___ al mercado.","options":["va","vas","voy"],"answer":"va","tag":"ir","sub":"él → va"},
  {"stimulus":"(Yo) ___ muy bien, gracias.","options":["estoy","está","estás"],"answer":"estoy","tag":"estar","sub":"yo → estoy"},
  {"stimulus":"¿(Vosotros) ___ los deberes?","options":["hacéis","hacen","hago"],"answer":"hacéis","tag":"hacer","sub":"vosotros → hacéis"},
  {"stimulus":"(Ellos) ___ de México.","options":["vienen","venís","viene"],"answer":"vienen","tag":"venir","sub":"ellos → vienen"},
  {"stimulus":"(Yo) ___ estudiante.","options":["soy","estoy","tengo"],"answer":"soy","tag":"ser","sub":"identiteit → soy"},
  {"stimulus":"¿Cómo te ___ ?","options":["llamas","llama","llamo"],"answer":"llamas","tag":"llamarse","sub":"tú → te llamas"},
  {"stimulus":"(Nosotros) ___ en Flandes.","options":["vivimos","vivís","viven"],"answer":"vivimos","tag":"vivir","sub":"nosotros → vivimos"},
  {"stimulus":"Lucía ___ española.","options":["es","eres","soy"],"answer":"es","tag":"ser","sub":"ella → es"},
  {"stimulus":"(Yo) ___ dos hermanas.","options":["tengo","tienes","tiene"],"answer":"tengo","tag":"tener","sub":"yo → tengo"},
  {"stimulus":"¿(Tú) ___ contento hoy?","options":["estás","está","estoy"],"answer":"estás","tag":"estar","sub":"tú → estás"},
  {"stimulus":"(Ellos) ___ mucho español.","options":["hablan","habláis","hablamos"],"answer":"hablan","tag":"hablar","sub":"ellos → hablan"},
  {"stimulus":"(Yo) ___ al instituto en bici.","options":["voy","vas","va"],"answer":"voy","tag":"ir","sub":"yo → voy"},
  {"stimulus":"Mateo ___ de Argentina.","options":["viene","vienes","vengo"],"answer":"viene","tag":"venir","sub":"él → viene"},
  {"stimulus":"(Nosotros) ___ amigos.","options":["somos","sois","son"],"answer":"somos","tag":"ser","sub":"nosotros → somos"},
  {"stimulus":"¿(Vosotros) ___ en Bruselas?","options":["vivís","viven","vivimos"],"answer":"vivís","tag":"vivir","sub":"vosotros → vivís"},
  {"stimulus":"(Yo) ___ los deberes por la tarde.","options":["hago","haces","hace"],"answer":"hago","tag":"hacer","sub":"yo → hago"}]}})

# 8 · CLOZE — concordancia adjetivo (pool 16, rounds 10)
w({"id":PRE+"concordancia","title":"Completa: concordancia","subtitle":"U0 · laat het adjectief overeenkomen (m/v · ev/mv)",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm van het adjectief","items":[
  {"stimulus":"La chica es ___ .","options":["simpática","simpático","simpáticas"],"answer":"simpática","tag":"c","sub":"la chica (f ev)"},
  {"stimulus":"El chico es ___ .","options":["alto","alta","altos"],"answer":"alto","tag":"c","sub":"el chico (m ev)"},
  {"stimulus":"Los libros son ___ .","options":["rojos","rojas","rojo"],"answer":"rojos","tag":"c","sub":"los libros (m pl)"},
  {"stimulus":"Las casas son ___ .","options":["blancas","blancos","blanca"],"answer":"blancas","tag":"c","sub":"las casas (f pl)"},
  {"stimulus":"Nina es ___ .","options":["peruana","peruano","peruanas"],"answer":"peruana","tag":"c","sub":"ella → peruana"},
  {"stimulus":"Diego es ___ .","options":["mexicano","mexicana","mexicanos"],"answer":"mexicano","tag":"c","sub":"él → mexicano"},
  {"stimulus":"Mis amigas son ___ .","options":["alegres","alegre","alegras"],"answer":"alegres","tag":"c","sub":"alegre → alegres (pl)"},
  {"stimulus":"La profesora es ___ .","options":["trabajadora","trabajador","trabajadoras"],"answer":"trabajadora","tag":"c","sub":"la profesora (f ev)"},
  {"stimulus":"El coche es ___ .","options":["nuevo","nueva","nuevos"],"answer":"nuevo","tag":"c","sub":"el coche (m ev)"},
  {"stimulus":"Las chicas son ___ .","options":["morenas","morenos","morena"],"answer":"morenas","tag":"c","sub":"las chicas (f pl)"},
  {"stimulus":"Los perros son ___ .","options":["pequeños","pequeñas","pequeño"],"answer":"pequeños","tag":"c","sub":"los perros (m pl)"},
  {"stimulus":"Mi madre es ___ .","options":["española","español","españolas"],"answer":"española","tag":"c","sub":"ella → española"},
  {"stimulus":"El profesor es ___ .","options":["simpático","simpática","simpáticos"],"answer":"simpático","tag":"c","sub":"el profesor (m ev)"},
  {"stimulus":"Las mochilas son ___ .","options":["rojas","rojos","roja"],"answer":"rojas","tag":"c","sub":"las mochilas (f pl)"},
  {"stimulus":"Valen es ___ .","options":["colombiana","colombiano","colombianas"],"answer":"colombiana","tag":"c","sub":"ella → colombiana"},
  {"stimulus":"Mis hermanos son ___ .","options":["altos","altas","alto"],"answer":"altos","tag":"c","sub":"los hermanos (m pl)"}]}})

# 9 · TETRIS — concordancia adjetivo (valt in de juiste kolom) (pool 16)
w({"id":PRE+"concordancia-tetris","title":"Concordancia Tetris","subtitle":"U0 · laat elk woord in de juiste vorm vallen",
 "lang":"es","template":"tetris","options":{"rows":9,"speed":1300,"audio":False},
 "classify":{"categories":[
  {"id":"alto","label":"alto","glaze":G["blue"]},{"id":"alta","label":"alta","glaze":G["red"]},
  {"id":"altos","label":"altos","glaze":G["green"]},{"id":"altas","label":"altas","glaze":G["amber"]}],
 "items":[
  {"stimulus":"el chico","answer":"alto","tag":"alto","sub":"m ev"},
  {"stimulus":"la chica","answer":"alta","tag":"alta","sub":"f ev"},
  {"stimulus":"los chicos","answer":"altos","tag":"altos","sub":"m pl"},
  {"stimulus":"las chicas","answer":"altas","tag":"altas","sub":"f pl"},
  {"stimulus":"el profesor","answer":"alto","tag":"alto","sub":"m ev"},
  {"stimulus":"la profesora","answer":"alta","tag":"alta","sub":"f ev"},
  {"stimulus":"los amigos","answer":"altos","tag":"altos","sub":"m pl"},
  {"stimulus":"las amigas","answer":"altas","tag":"altas","sub":"f pl"},
  {"stimulus":"el hermano","answer":"alto","tag":"alto","sub":"m ev"},
  {"stimulus":"la hermana","answer":"alta","tag":"alta","sub":"f ev"},
  {"stimulus":"los padres","answer":"altos","tag":"altos","sub":"m pl"},
  {"stimulus":"las madres","answer":"altas","tag":"altas","sub":"f pl"},
  {"stimulus":"el niño","answer":"alto","tag":"alto","sub":"m ev"},
  {"stimulus":"la niña","answer":"alta","tag":"alta","sub":"f ev"},
  {"stimulus":"los perros","answer":"altos","tag":"altos","sub":"m pl"},
  {"stimulus":"las gatas","answer":"altas","tag":"altas","sub":"f pl"}]}})

# 10 · ORDER — ordena la presentación (8 rondes, geschud per speling)
w({"id":PRE+"presentacion-order","title":"Ordena la presentación","subtitle":"U0 · zet de zinnen in de logische volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik de zinnen in de logische volgorde van een presentatie","rounds":[
  {"tag":"pres","sub":"saludar → nombre → origen → edad","items":[
    {"label":"¡Hola! ¿Qué tal?","key":1},{"label":"Me llamo Nina.","key":2},
    {"label":"Soy de Perú.","key":3},{"label":"Tengo dieciséis años.","key":4}]},
  {"tag":"pres","sub":"saludar → nombre → dónde vives → lengua","items":[
    {"label":"Buenos días.","key":1},{"label":"Me llamo Diego.","key":2},
    {"label":"Vivo en Ciudad de México.","key":3},{"label":"Hablo español.","key":4}]},
  {"tag":"pres","sub":"pregunta → respuesta → repregunta → respuesta","items":[
    {"label":"¿Cómo te llamas?","key":1},{"label":"Me llamo Lucía, ¿y tú?","key":2},
    {"label":"Yo soy Mateo.","key":3},{"label":"¡Mucho gusto, Mateo!","key":4}]},
  {"tag":"pres","sub":"origen → nacionalidad → lengua → carácter","items":[
    {"label":"Soy de Cartagena.","key":1},{"label":"Soy colombiana.","key":2},
    {"label":"Hablo español.","key":3},{"label":"Soy muy alegre.","key":4}]},
  {"tag":"pres","sub":"saludar → cómo estás → responder → despedir","items":[
    {"label":"¡Hola, Lucía!","key":1},{"label":"¿Cómo estás?","key":2},
    {"label":"Muy bien, gracias.","key":3},{"label":"¡Hasta luego!","key":4}]},
  {"tag":"pres","sub":"formal: saludar → nombre → usted → despedir","items":[
    {"label":"Buenos días, señora.","key":1},{"label":"Me llamo Ana García.","key":2},
    {"label":"¿Y cómo se llama usted?","key":3},{"label":"Encantada.","key":4}]},
  {"tag":"pres","sub":"clase: pedir → responder → repetir → gracias","items":[
    {"label":"Perdón, ¿cómo se dice 'boekentas'?","key":1},{"label":"Se dice «la mochila».","key":2},
    {"label":"¿Puedes repetir, por favor?","key":3},{"label":"«La mochila». ¡Gracias!","key":4}]},
  {"tag":"pres","sub":"números: presentar edad y clase","items":[
    {"label":"Me llamo Tom.","key":1},{"label":"Tengo quince años.","key":2},
    {"label":"Estoy en 6º año.","key":3},{"label":"Vivo cerca del instituto.","key":4}]}]}})

# 11 · POINT — señala (repaso gemengd) (10 rondes)
w({"id":PRE+"senala","title":"Señala","subtitle":"U0 · klik het juiste antwoord",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het gevraagde item","mode":"one","rounds":[
  {"tag":"pais","sub":"señala el país (no la nacionalidad)","targets":[
    {"label":"español"},{"label":"México","hit":True},{"label":"peruano"},{"label":"belga"}]},
  {"tag":"nacionalidad","sub":"señala la nacionalidad","targets":[
    {"label":"España"},{"label":"Perú"},{"label":"colombiano","hit":True},{"label":"Chile"}]},
  {"tag":"saludo","sub":"señala el saludo (begroeting)","targets":[
    {"label":"adiós"},{"label":"buenos días","hit":True},{"label":"hasta luego"},{"label":"gracias"}]},
  {"tag":"verbo","sub":"señala la forma de «yo» (ser)","targets":[
    {"label":"eres"},{"label":"es"},{"label":"soy","hit":True},{"label":"somos"}]},
  {"tag":"verbo","sub":"señala la forma de «tú» (tener)","targets":[
    {"label":"tengo"},{"label":"tienes","hit":True},{"label":"tiene"},{"label":"tienen"}]},
  {"tag":"genero","sub":"señala la palabra femenina (la)","targets":[
    {"label":"libro"},{"label":"problema"},{"label":"casa","hit":True},{"label":"día"}]},
  {"tag":"adjetivo","sub":"señala el adjetivo femenino","targets":[
    {"label":"alto"},{"label":"simpática","hit":True},{"label":"trabajador"},{"label":"morenos"}]},
  {"tag":"lengua","sub":"señala una lengua","targets":[
    {"label":"España"},{"label":"el quechua","hit":True},{"label":"Madrid"},{"label":"belga"}]},
  {"tag":"despedida","sub":"señala la despedida (afscheid)","targets":[
    {"label":"hola"},{"label":"buenas tardes"},{"label":"adiós","hit":True},{"label":"encantado"}]},
  {"tag":"numero","sub":"señala el número cien (100)","targets":[
    {"label":"veinte"},{"label":"cincuenta"},{"label":"cien","hit":True},{"label":"catorce"}]}]}})

# ============================ ⑤ HABLAR · grábate 🎙️ ============================
# 12 · SPEAK repeat — escucha y repite: saludos y presentación (8 items)
w({"id":PRE+"repite-saludos","title":"Escucha y repite: saludos","subtitle":"U0 · escucha el modelo, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite en voz alta · grábate ⏺","items":[
  {"text":"¡Hola! Me llamo Diego.","sub":"hallo, ik heet Diego","tag":"pres","tip":"¡Bien! Ahora dilo sin leer. <span class='nl'>zeg het nu zonder te lezen.</span>"},
  {"text":"Soy de Bélgica y tengo dieciséis años.","sub":"ik kom uit België en ben 16","tag":"pres"},
  {"text":"Vivo en Gante y hablo neerlandés y español.","sub":"ik woon in Gent en spreek NL en ES","tag":"pres"},
  {"text":"Encantado, ¿cómo te llamas?","sub":"aangenaam, hoe heet je?","tag":"pres"},
  {"text":"Buenos días, ¿qué tal?","sub":"goedemorgen, hoe gaat het?","tag":"saludo"},
  {"text":"Soy estudiante y soy muy alegre.","sub":"ik ben student en heel vrolijk","tag":"pres"},
  {"text":"¿De dónde eres tú?","sub":"waar kom jij vandaan?","tag":"pres"},
  {"text":"¡Hasta luego!","sub":"tot straks!","tag":"despedida"}]}})

# 13 · SPEAK voicemessage — preséntate (3 items)
w({"id":PRE+"mensaje-presentate","title":"Mensaje de voz: preséntate","subtitle":"U0 · neem een spraakbericht op met je presentación",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz (20–30 s)","items":[
  {"text":"Preséntate: nombre, edad, de dónde eres, dónde vives y una lengua.","cue":"tu presentación","tag":"pres",
   "sub":"gebruik: me llamo · tengo … años · soy de · vivo en · hablo",
   "tip":"Heb je 5 gegevens gezegd? Neem opnieuw op. <span class='nl'>5 gegevens? herneem.</span>"},
  {"text":"Describe a un compañero/a: ¿cómo es? (carácter y físico).","cue":"describir","tag":"describir",
   "sub":"gebruik: es · tiene · alto/a · simpático/a · moreno/a",
   "tip":"2 eigenschappen + 1 fysiek? Herneem. <span class='nl'>2 karakter + 1 uiterlijk? herneem.</span>"},
  {"text":"Deja un saludo formal para tu profe (usted).","cue":"formal","tag":"formal",
   "sub":"gebruik: buenos días · ¿cómo está usted? · soy … · hasta luego",
   "tip":"Heb je 'usted' gebruikt? Herneem. <span class='nl'>usted gebruikt? herneem.</span>"}]}})

print("\n13 C6+·U0-spellen geschreven (8 templates: memory·match·classify·cloze·tetris·order·point·speak).")
print("Pools >=12 waar zinvol; options.rounds lager => herspeling geeft een andere reeks.")
