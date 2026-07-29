#!/usr/bin/env python3
# Motor-content-JSON's voor C6+ · U3 «Conectados» (media/redes · ir a + inf · le/les · acabar de · creo que).
# Templates: memory·match·classify·cloze·tetris·order·point·speak. Pools >=12; rounds lager => andere reeks.
# Werkwoordsvormen (ir a / acabar de / le-les / indicativo) nagerekend. Slug-prefix = es-c6plus-u3-.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")
def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2)); print("wrote", os.path.basename(p))
G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0","magenta":"#B4309A"}
PRE = "es-c6plus-u3-"

# 1 · MEMORY — aparatos/redes ES ↔ NL (pool 14)
w({"id":PRE+"digital-memoria","title":"Memoria digital","subtitle":"U3 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: mundo digital + vertaling","pairs":[
  {"a":"el móvil","b":"de gsm"},{"a":"el ordenador","b":"de computer"},{"a":"la tableta","b":"de tablet"},
  {"a":"la pantalla","b":"het scherm"},{"a":"los auriculares","b":"de oortjes"},{"a":"el cargador","b":"de oplader"},
  {"a":"la contraseña","b":"het wachtwoord"},{"a":"el perfil","b":"het profiel"},{"a":"el mensaje","b":"het bericht"},
  {"a":"el vídeo","b":"de video"},{"a":"la app","b":"de app"},{"a":"las redes sociales","b":"de sociale media"},
  {"a":"la videollamada","b":"het videogesprek"},{"a":"la wifi","b":"de wifi"}]}})

# 2 · MEMORY — acciones digitales ES ↔ NL (pool 12)
w({"id":PRE+"acciones-memoria","title":"Memoria de acciones","subtitle":"U3 · koppel het werkwoord aan de vertaling",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: verbo + vertaling","pairs":[
  {"a":"chatear","b":"chatten"},{"a":"navegar","b":"surfen"},{"a":"subir","b":"uploaden"},
  {"a":"descargar","b":"downloaden"},{"a":"compartir","b":"delen"},{"a":"seguir","b":"volgen"},
  {"a":"publicar","b":"posten"},{"a":"apagar","b":"uitzetten"},{"a":"encender","b":"aanzetten"},
  {"a":"mandar","b":"sturen"},{"a":"llamar","b":"bellen"},{"a":"contestar","b":"antwoorden"}]}})

# 3 · MATCH — verbo ↔ objeto (pool 12)
w({"id":PRE+"verbo-objeto","title":"Verbo y objeto","subtitle":"U3 · koppel de actie aan het juiste ding",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind het werkwoord met het logische object","pairs":[
  {"a":"subir","b":"un vídeo ⬆️"},{"a":"descargar","b":"una app 📲"},
  {"a":"cargar","b":"la batería 🔋"},{"a":"chatear","b":"con un amigo 💬"},
  {"a":"seguir","b":"a un artista ⭐"},{"a":"mandar","b":"un mensaje ✉️"},
  {"a":"hacer","b":"una videollamada 📹"},{"a":"escribir","b":"la contraseña 🔑"},
  {"a":"compartir","b":"una foto 🖼️"},{"a":"apagar","b":"el móvil 🌙"},
  {"a":"quedar","b":"en la plaza 📍"},{"a":"ver","b":"una serie 📺"}]}})

# 4 · CLASSIFY — ¿presente (ahora) o ir a (después)? (pool 16, rounds 10)
w({"id":PRE+"presente-futuro","title":"¿ahora o después?","subtitle":"U3 · presente (nu) of ir a + inf (straks)?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Gebeurt het nu/gewoonlijk (presente) of straks (ir a + inf)?","categories":[
  {"id":"pres","label":"ahora / siempre<br><small>presente</small>","glaze":G["teal"]},
  {"id":"futuro","label":"después<br><small>ir a + inf.</small>","glaze":G["purple"]}],
 "items":[
  {"stimulus":"Cada día chateo con mis amigos.","answer":"pres","tag":"pres","sub":"cada día → presente"},
  {"stimulus":"Mañana voy a subir un vídeo.","answer":"futuro","tag":"futuro","sub":"mañana → ir a"},
  {"stimulus":"Este finde vamos a quedar.","answer":"futuro","tag":"futuro","sub":"este finde → ir a"},
  {"stimulus":"Normalmente navego por la noche.","answer":"pres","tag":"pres","sub":"normalmente → presente"},
  {"stimulus":"Luego voy a llamar a Diego.","answer":"futuro","tag":"futuro","sub":"luego → ir a"},
  {"stimulus":"Ahora subo las fotos.","answer":"pres","tag":"pres","sub":"ahora + presente"},
  {"stimulus":"El sábado van a salir.","answer":"futuro","tag":"futuro","sub":"el sábado → ir a"},
  {"stimulus":"Siempre apago el móvil por la noche.","answer":"pres","tag":"pres","sub":"siempre → presente"},
  {"stimulus":"Pronto voy a comprar una tableta.","answer":"futuro","tag":"futuro","sub":"pronto → ir a"},
  {"stimulus":"Los domingos veo series.","answer":"pres","tag":"pres","sub":"los domingos → presente"},
  {"stimulus":"El próximo año vamos a viajar.","answer":"futuro","tag":"futuro","sub":"el próximo año → ir a"},
  {"stimulus":"Diego sigue a muchos artistas.","answer":"pres","tag":"pres","sub":"acción habitual → presente"},
  {"stimulus":"Esta tarde vas a estudiar.","answer":"futuro","tag":"futuro","sub":"esta tarde → ir a"},
  {"stimulus":"Comparto vídeos cada semana.","answer":"pres","tag":"pres","sub":"cada semana → presente"},
  {"stimulus":"Más tarde voy a descansar.","answer":"futuro","tag":"futuro","sub":"más tarde → ir a"},
  {"stimulus":"Mis amigos van a ver una peli.","answer":"futuro","tag":"futuro","sub":"van a + inf"}]}})

# 5 · CLASSIFY — ¿le o les? (pool 16, rounds 10)
w({"id":PRE+"le-les","title":"¿le o les?","subtitle":"U3 · aan één persoon (le) of aan meer (les)?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Kies: le (aan één persoon) of les (aan meer personen)?","categories":[
  {"id":"le","label":"le<br><small>a él/ella/usted</small>","glaze":G["blue"]},
  {"id":"les","label":"les<br><small>a ellos/ellas</small>","glaze":G["magenta"]}],
 "items":[
  {"stimulus":"___ escribo a mi amiga.","answer":"le","tag":"le","sub":"a mi amiga → le"},
  {"stimulus":"___ mando fotos a mis padres.","answer":"les","tag":"les","sub":"a mis padres → les"},
  {"stimulus":"___ cuento un secreto a Diego.","answer":"le","tag":"le","sub":"a Diego → le"},
  {"stimulus":"___ regalo auriculares a mis hermanos.","answer":"les","tag":"les","sub":"a mis hermanos → les"},
  {"stimulus":"___ pregunto la hora a Valen.","answer":"le","tag":"le","sub":"a Valen → le"},
  {"stimulus":"___ muestro mi perfil a mis amigos.","answer":"les","tag":"les","sub":"a mis amigos → les"},
  {"stimulus":"___ digo la verdad a mi madre.","answer":"le","tag":"le","sub":"a mi madre → le"},
  {"stimulus":"___ envío un mensaje a los profes.","answer":"les","tag":"les","sub":"a los profes → les"},
  {"stimulus":"___ llamo a mi abuela los domingos.","answer":"le","tag":"le","sub":"a mi abuela → le"},
  {"stimulus":"___ cuento las noticias a mis primos.","answer":"les","tag":"les","sub":"a mis primos → les"},
  {"stimulus":"___ escribo a mi profesor.","answer":"le","tag":"le","sub":"a mi profesor → le"},
  {"stimulus":"___ mando la ubicación a mis amigas.","answer":"les","tag":"les","sub":"a mis amigas → les"},
  {"stimulus":"___ pregunto la contraseña a Diego.","answer":"le","tag":"le","sub":"a Diego → le"},
  {"stimulus":"___ regalo una app a mi hermana.","answer":"le","tag":"le","sub":"a mi hermana → le"},
  {"stimulus":"___ enseño las fotos a mis abuelos.","answer":"les","tag":"les","sub":"a mis abuelos → les"},
  {"stimulus":"___ respondo a mis compañeros.","answer":"les","tag":"les","sub":"a mis compañeros → les"}]}})

# 6 · CLOZE — ir a + infinitivo (VERPLICHT ww-cloze, nagerekend) (pool 18, rounds 12)
w({"id":PRE+"ir-a","title":"Completa: ir a + infinitivo","subtitle":"U3 · ¿qué vas a hacer?",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm van ir a + infinitivo","items":[
  {"stimulus":"(Yo) ___ un vídeo esta tarde.","options":["voy a subir","vas a subir","va a subir"],"answer":"voy a subir","tag":"f","sub":"yo → voy a subir"},
  {"stimulus":"¿(Tú) ___ el sábado?","options":["vas a salir","voy a salir","van a salir"],"answer":"vas a salir","tag":"f","sub":"tú → vas a salir"},
  {"stimulus":"Diego ___ con nosotros luego.","options":["va a chatear","vas a chatear","voy a chatear"],"answer":"va a chatear","tag":"f","sub":"él → va a chatear"},
  {"stimulus":"(Nosotros) ___ en la plaza.","options":["vamos a quedar","van a quedar","vais a quedar"],"answer":"vamos a quedar","tag":"f","sub":"nosotros → vamos a quedar"},
  {"stimulus":"Mis amigos ___ una serie.","options":["van a ver","va a ver","vamos a ver"],"answer":"van a ver","tag":"f","sub":"ellos → van a ver"},
  {"stimulus":"¿(Vosotros) ___ mañana?","options":["vais a estudiar","van a estudiar","vamos a estudiar"],"answer":"vais a estudiar","tag":"f","sub":"vosotros → vais a estudiar"},
  {"stimulus":"(Yo) ___ a mi abuela.","options":["voy a llamar","va a llamar","vas a llamar"],"answer":"voy a llamar","tag":"f","sub":"yo → voy a llamar"},
  {"stimulus":"Valen ___ las fotos.","options":["va a compartir","van a compartir","vas a compartir"],"answer":"va a compartir","tag":"f","sub":"ella → va a compartir"},
  {"stimulus":"(Nosotros) ___ tacos.","options":["vamos a comer","van a comer","voy a comer"],"answer":"vamos a comer","tag":"f","sub":"nosotros → vamos a comer"},
  {"stimulus":"¿Qué ___ (tú) este finde?","options":["vas a hacer","va a hacer","voy a hacer"],"answer":"vas a hacer","tag":"f","sub":"tú → vas a hacer"},
  {"stimulus":"Ellos ___ un vídeo nuevo.","options":["van a publicar","va a publicar","vais a publicar"],"answer":"van a publicar","tag":"f","sub":"ellos → van a publicar"},
  {"stimulus":"(Yo) ___ una app.","options":["voy a descargar","vas a descargar","va a descargar"],"answer":"voy a descargar","tag":"f","sub":"yo → voy a descargar"},
  {"stimulus":"Diego y yo ___ pronto.","options":["vamos a quedar","van a quedar","voy a quedar"],"answer":"vamos a quedar","tag":"f","sub":"nosotros → vamos a quedar"},
  {"stimulus":"Mi madre ___ un móvil nuevo.","options":["va a comprar","van a comprar","vas a comprar"],"answer":"va a comprar","tag":"f","sub":"ella → va a comprar"},
  {"stimulus":"¿(Tú) me ___ luego?","options":["vas a llamar","va a llamar","van a llamar"],"answer":"vas a llamar","tag":"f","sub":"tú → vas a llamar"},
  {"stimulus":"Los niños ___ al parque.","options":["van a ir","va a ir","vamos a ir"],"answer":"van a ir","tag":"f","sub":"ellos → van a ir"},
  {"stimulus":"(Nosotros) ___ una peli esta noche.","options":["vamos a ver","van a ver","vais a ver"],"answer":"vamos a ver","tag":"f","sub":"nosotros → vamos a ver"},
  {"stimulus":"(Yo) ___ con mis primos.","options":["voy a chatear","vas a chatear","va a chatear"],"answer":"voy a chatear","tag":"f","sub":"yo → voy a chatear"}]}})

# 7 · CLOZE — le/les + verbo comunicación (pool 16, rounds 10)
w({"id":PRE+"le-les-cloze","title":"Completa: le/les","subtitle":"U3 · ¿a quién? le of les",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies het juiste OI-pronomen","items":[
  {"stimulus":"¿Escribes a Diego? — Sí, ___ escribo.","options":["le","les","la"],"answer":"le","tag":"oi","sub":"a Diego (1) → le"},
  {"stimulus":"¿Mandas fotos a tus amigos? — Sí, ___ mando fotos.","options":["les","le","los"],"answer":"les","tag":"oi","sub":"a tus amigos → les"},
  {"stimulus":"¿Cuentas el secreto a Valen? — Sí, ___ cuento.","options":["le","les","lo"],"answer":"le","tag":"oi","sub":"a Valen (1) → le"},
  {"stimulus":"¿Preguntas la hora a tus padres? — Sí, ___ pregunto.","options":["les","le","las"],"answer":"les","tag":"oi","sub":"a tus padres → les"},
  {"stimulus":"¿Regalas auriculares a tu hermana? — Sí, ___ regalo unos.","options":["le","les","la"],"answer":"le","tag":"oi","sub":"a tu hermana (1) → le"},
  {"stimulus":"¿Muestras el perfil a los profes? — Sí, ___ muestro.","options":["les","le","lo"],"answer":"les","tag":"oi","sub":"a los profes → les"},
  {"stimulus":"¿Llamas a tu abuela? — Sí, ___ llamo.","options":["le","les","la"],"answer":"le","tag":"oi","sub":"a tu abuela (1) → le"},
  {"stimulus":"¿Envías la ubicación a tus amigas? — Sí, ___ envío.","options":["les","le","las"],"answer":"les","tag":"oi","sub":"a tus amigas → les"},
  {"stimulus":"¿Dices la verdad a tu madre? — Sí, ___ digo la verdad.","options":["le","les","la"],"answer":"le","tag":"oi","sub":"a tu madre (1) → le"},
  {"stimulus":"¿Respondes a tus compañeros? — Sí, ___ respondo.","options":["les","le","los"],"answer":"les","tag":"oi","sub":"a compañeros → les"},
  {"stimulus":"¿Escribes a tu profesor? — Sí, ___ escribo.","options":["le","les","lo"],"answer":"le","tag":"oi","sub":"a tu profesor (1) → le"},
  {"stimulus":"¿Enseñas las fotos a tus abuelos? — Sí, ___ enseño.","options":["les","le","las"],"answer":"les","tag":"oi","sub":"a tus abuelos → les"},
  {"stimulus":"¿Mandas un audio a Diego? — Sí, ___ mando un audio.","options":["le","les","lo"],"answer":"le","tag":"oi","sub":"a Diego (1) → le"},
  {"stimulus":"¿Cuentas las noticias a tus primos? — Sí, ___ cuento.","options":["les","le","las"],"answer":"les","tag":"oi","sub":"a tus primos → les"},
  {"stimulus":"¿Preguntas la contraseña a Valen? — Sí, ___ pregunto.","options":["le","les","la"],"answer":"le","tag":"oi","sub":"a Valen (1) → le"},
  {"stimulus":"¿Regalas una app a tus hermanos? — Sí, ___ regalo una.","options":["les","le","los"],"answer":"les","tag":"oi","sub":"a tus hermanos → les"}]}})

# 8 · CLOZE — creo que + indicativo (pool 14, rounds 10)
w({"id":PRE+"creo-que","title":"Completa: creo que + indicativo","subtitle":"U3 · tu opinión (gewone tijd, geen subjuntivo)",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies de indicativo-vorm na «creo que…»","items":[
  {"stimulus":"Creo que las redes ___ útiles.","options":["son","sean","es"],"answer":"son","tag":"op","sub":"las redes → son (indicativo)"},
  {"stimulus":"Pienso que Diego ___ razón.","options":["tiene","tenga","tienen"],"answer":"tiene","tag":"op","sub":"Diego → tiene"},
  {"stimulus":"Me parece que (nosotros) ___ mucho tiempo online.","options":["pasamos","pasemos","pasan"],"answer":"pasamos","tag":"op","sub":"nosotros → pasamos"},
  {"stimulus":"Creo que el móvil ___ a estudiar.","options":["ayuda","ayude","ayudan"],"answer":"ayuda","tag":"op","sub":"el móvil → ayuda"},
  {"stimulus":"Pienso que los videojuegos ___ ser adictivos.","options":["pueden","puedan","puede"],"answer":"pueden","tag":"op","sub":"los videojuegos → pueden"},
  {"stimulus":"Creo que la wifi de aquí ___ rápida.","options":["es","sea","son"],"answer":"es","tag":"op","sub":"la wifi → es"},
  {"stimulus":"Me parece que (tú) ___ demasiado en el móvil.","options":["estás","estés","está"],"answer":"estás","tag":"op","sub":"tú → estás"},
  {"stimulus":"Pienso que las apps ___ prácticas.","options":["son","sean","es"],"answer":"son","tag":"op","sub":"las apps → son"},
  {"stimulus":"Creo que (nosotros) ___ que apagar el móvil a veces.","options":["tenemos","tengamos","tienen"],"answer":"tenemos","tag":"op","sub":"nosotros → tenemos"},
  {"stimulus":"Me parece que internet ___ peligroso a veces.","options":["es","sea","son"],"answer":"es","tag":"op","sub":"internet → es"},
  {"stimulus":"Creo que Valen ___ muchos seguidores.","options":["tiene","tenga","tienen"],"answer":"tiene","tag":"op","sub":"Valen → tiene"},
  {"stimulus":"Pienso que (yo) ___ demasiadas fotos.","options":["subo","suba","sube"],"answer":"subo","tag":"op","sub":"yo → subo"},
  {"stimulus":"Creo que las videollamadas ___ geniales.","options":["son","sean","es"],"answer":"son","tag":"op","sub":"las videollamadas → son"},
  {"stimulus":"Me parece que la gente ___ mucho en las redes.","options":["comparte","comparta","comparten"],"answer":"comparte","tag":"op","sub":"la gente → comparte"}]}})

# 9 · TETRIS — ir a: la persona correcta (voy/vas/va/vamos/vais/van) (pool 16)
w({"id":PRE+"ir-a-tetris","title":"ir a Tetris","subtitle":"U3 · laat de juiste vorm van ir vallen",
 "lang":"es","template":"tetris","options":{"rows":9,"speed":1300,"audio":False},
 "classify":{"categories":[
  {"id":"voy","label":"voy a","glaze":G["blue"]},{"id":"vas","label":"vas a","glaze":G["red"]},
  {"id":"va","label":"va a","glaze":G["green"]},{"id":"van","label":"van a","glaze":G["amber"]}],
 "items":[
  {"stimulus":"yo … subir","answer":"voy","tag":"voy","sub":"yo → voy a"},{"stimulus":"tú … salir","answer":"vas","tag":"vas","sub":"tú → vas a"},
  {"stimulus":"Diego … chatear","answer":"va","tag":"va","sub":"él → va a"},{"stimulus":"ellos … ver","answer":"van","tag":"van","sub":"ellos → van a"},
  {"stimulus":"yo … llamar","answer":"voy","tag":"voy","sub":"yo → voy a"},{"stimulus":"tú … estudiar","answer":"vas","tag":"vas","sub":"tú → vas a"},
  {"stimulus":"Valen … compartir","answer":"va","tag":"va","sub":"ella → va a"},{"stimulus":"mis amigos … quedar","answer":"van","tag":"van","sub":"ellos → van a"},
  {"stimulus":"yo … descargar","answer":"voy","tag":"voy","sub":"yo → voy a"},{"stimulus":"¿tú … venir?","answer":"vas","tag":"vas","sub":"tú → vas a"},
  {"stimulus":"mi madre … comprar","answer":"va","tag":"va","sub":"ella → va a"},{"stimulus":"los niños … jugar","answer":"van","tag":"van","sub":"ellos → van a"},
  {"stimulus":"yo … apagar","answer":"voy","tag":"voy","sub":"yo → voy a"},{"stimulus":"tú … contestar","answer":"vas","tag":"vas","sub":"tú → vas a"},
  {"stimulus":"él … publicar","answer":"va","tag":"va","sub":"él → va a"},{"stimulus":"ellas … viajar","answer":"van","tag":"van","sub":"ellas → van a"}]}})

# 10 · ORDER — ordena la frase / el plan (8 rondes)
w({"id":PRE+"plan-order","title":"Ordena la frase","subtitle":"U3 · zet de zin/het plan in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik in de logische volgorde","rounds":[
  {"tag":"futuro","sub":"ir a + infinitivo","items":[
    {"label":"Este finde","key":1},{"label":"voy a","key":2},{"label":"quedar","key":3},{"label":"con mis amigos.","key":4}]},
  {"tag":"oi","sub":"le + verbo","items":[
    {"label":"Le","key":1},{"label":"escribo","key":2},{"label":"un mensaje","key":3},{"label":"a Diego.","key":4}]},
  {"tag":"acabar","sub":"acabar de + infinitivo","items":[
    {"label":"Acabo","key":1},{"label":"de","key":2},{"label":"subir","key":3},{"label":"una foto.","key":4}]},
  {"tag":"opinion","sub":"creo que + porque","items":[
    {"label":"Creo que","key":1},{"label":"las redes","key":2},{"label":"son útiles","key":3},{"label":"porque conectan.","key":4}]},
  {"tag":"futuro","sub":"expresión de tiempo","items":[
    {"label":"Mañana","key":1},{"label":"Diego","key":2},{"label":"va a","key":3},{"label":"llamar a su abuela.","key":4}]},
  {"tag":"plan","sub":"el plan del sábado","items":[
    {"label":"Primero voy a estudiar,","key":1},{"label":"después voy a quedar,","key":2},{"label":"luego vamos a comer","key":3},{"label":"y por la noche voy a descansar.","key":4}]},
  {"tag":"oi","sub":"les + verbo","items":[
    {"label":"Les","key":1},{"label":"mando","key":2},{"label":"fotos","key":3},{"label":"a mis amigos.","key":4}]},
  {"tag":"futuro","sub":"pregunta con ir a","items":[
    {"label":"¿Qué","key":1},{"label":"vas a","key":2},{"label":"hacer","key":3},{"label":"el fin de semana?","key":4}]}]}})

# 11 · POINT — señala (repaso gemengd) (10 rondes)
w({"id":PRE+"senala","title":"Señala","subtitle":"U3 · klik het juiste antwoord",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het gevraagde item","mode":"one","rounds":[
  {"tag":"digital","sub":"señala un aparato","targets":[
    {"label":"el móvil","hit":True},{"label":"chatear"},{"label":"útil"},{"label":"mañana"}]},
  {"tag":"digital","sub":"señala una acción (verbo)","targets":[
    {"label":"la pantalla"},{"label":"subir","hit":True},{"label":"el perfil"},{"label":"el cargador"}]},
  {"tag":"futuro","sub":"«ik ga eten» = ?","targets":[
    {"label":"voy comer"},{"label":"voy a comer","hit":True},{"label":"voy a como"},{"label":"va a comer"}]},
  {"tag":"futuro","sub":"«we gaan afspreken» = ?","targets":[
    {"label":"vamos a quedar","hit":True},{"label":"van a quedar"},{"label":"vamos quedar"},{"label":"vais a quedar"}]},
  {"tag":"oi","sub":"«___ escribo a Diego»","targets":[
    {"label":"le","hit":True},{"label":"les"},{"label":"lo"},{"label":"la"}]},
  {"tag":"oi","sub":"«___ mando fotos a mis amigos»","targets":[
    {"label":"les","hit":True},{"label":"le"},{"label":"los"},{"label":"las"}]},
  {"tag":"acabar","sub":"«ik heb net gegeten» = ?","targets":[
    {"label":"voy a comer"},{"label":"acabo de comer","hit":True},{"label":"acabo comer"},{"label":"acabo de como"}]},
  {"tag":"opinion","sub":"«Creo que las redes ___ útiles»","targets":[
    {"label":"son","hit":True},{"label":"sean"},{"label":"es"},{"label":"están"}]},
  {"tag":"tiempo","sub":"«dit weekend» = ?","targets":[
    {"label":"este fin de semana","hit":True},{"label":"ayer"},{"label":"siempre"},{"label":"ahora"}]},
  {"tag":"digital","sub":"«het wachtwoord» = ?","targets":[
    {"label":"la contraseña","hit":True},{"label":"el mensaje"},{"label":"la pantalla"},{"label":"el usuario"}]}]}})

# 12 · SPEAK repeat — planes, opinión, comunicar (8 items)
w({"id":PRE+"repite-planes","title":"Escucha y repite: mis planes","subtitle":"U3 · escucha, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite en voz alta · grábate ⏺","items":[
  {"text":"Este fin de semana voy a salir con mis amigos.","sub":"dit weekend ga ik uitgaan met mijn vrienden","tag":"futuro","tip":"¡Bien! Ahora dilo sin leer."},
  {"text":"Mañana voy a subir un vídeo nuevo.","sub":"morgen ga ik een nieuwe video uploaden","tag":"futuro"},
  {"text":"Le escribo a Diego cada día.","sub":"ik schrijf Diego elke dag","tag":"oi"},
  {"text":"Les mando fotos a mis amigos.","sub":"ik stuur foto's naar mijn vrienden","tag":"oi"},
  {"text":"Acabo de mandar un mensaje.","sub":"ik heb net een bericht gestuurd","tag":"acabar"},
  {"text":"Creo que las redes son útiles pero adictivas.","sub":"ik vind sociale media nuttig maar verslavend","tag":"opinion"},
  {"text":"Pienso que pasamos demasiado tiempo en el móvil.","sub":"ik denk dat we te veel tijd op de gsm zitten","tag":"opinion"},
  {"text":"¿Quedamos el sábado en la plaza?","sub":"spreken we zaterdag af op het plein?","tag":"plan"}]}})

# 13 · SPEAK voicemessage — plan + opinión (3 items)
w({"id":PRE+"mensaje-planes","title":"Mensaje de voz: mi finde","subtitle":"U3 · neem een spraakbericht op",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz (30–40 s)","items":[
  {"text":"Cuenta tu plan de fin de semana (usa 3 veces ir a + infinitivo).","cue":"mi plan","tag":"futuro",
   "sub":"gebruik: voy a … · vamos a … · el sábado voy a …",
   "tip":"3× ir a + infinitivo (met de a)? Neem opnieuw op."},
  {"text":"Di a quién escribes, llamas o mandas fotos (usa le y les).","cue":"le / les","tag":"oi",
   "sub":"gebruik: le escribo a … · les mando … a mis amigos",
   "tip":"le én les gebruikt? Herneem."},
  {"text":"Da tu opinión sobre las redes sociales (creo que … porque …).","cue":"mi opinión","tag":"opinion",
   "sub":"gebruik: creo que … es … porque … · por un lado … por otro …",
   "tip":"creo que + indicativo + porque? Herneem."}]}})

print("\n13 C6+·U3-spellen geschreven (8 templates: memory·match·classify·cloze·tetris·order·point·speak).")
