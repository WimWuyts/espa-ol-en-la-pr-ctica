#!/usr/bin/env python3
# Genereert de motor-content-JSON's voor C5 · U7 «Mi casa y mi barrio» (parada Colombia/Cartagena).
# Templates: memory·match·classify·cloze·tetris·order·point·sim·speak (receptief -> productief -> hablar).
# Elke game heeft een POOL van >=12 items; options.rounds lager zodat herspeling een ANDERE reeks trekt.
# Werkwoordsvormen (estar + gerundio, imperativo tú) nagerekend/geverifieerd.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2))
    print("wrote", os.path.basename(p))

G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0"}

# ============================ ① RECONOCER · woordenschat ============================
# 1 · MEMORY — la casa ES ↔ NL  (pool 14, 6 per bord)
w({"id":"es-u7-casa-memoria","title":"Memoria de la casa","subtitle":"U7 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om en zoek het woord + de vertaling","pairs":[
  {"a":"la cocina","b":"keuken"},{"a":"el salón","b":"woonkamer"},{"a":"el baño","b":"badkamer"},
  {"a":"el dormitorio","b":"slaapkamer"},{"a":"la cama","b":"bed"},{"a":"el sofá","b":"bank"},
  {"a":"el armario","b":"kast"},{"a":"la mesa","b":"tafel"},{"a":"la silla","b":"stoel"},
  {"a":"la ventana","b":"raam"},{"a":"la puerta","b":"deur"},{"a":"la escalera","b":"trap"},
  {"a":"la nevera","b":"koelkast"},{"a":"la ducha","b":"douche"}]}})

# 3 · MATCH — habitación ↔ mueble/acción  (pool 12, blokjes van 6)
w({"id":"es-u7-habitacion-mueble","title":"Habitación y mueble","subtitle":"U7 · welk meubel/actie hoort bij de kamer?",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind de kamer met wat erbij hoort","pairs":[
  {"a":"la cocina","b":"la nevera 🧊"},{"a":"el dormitorio","b":"la cama 🛏️"},
  {"a":"el salón","b":"el sofá 🛋️"},{"a":"el baño","b":"la ducha 🚿"},
  {"a":"el comedor","b":"la mesa 🍽️"},{"a":"el estudio","b":"la estantería 📚"},
  {"a":"el pasillo","b":"el espejo 🪞"},{"a":"la terraza","b":"las plantas 🪴"},
  {"a":"el jardín","b":"los árboles 🌳"},{"a":"la entrada","b":"la puerta 🚪"},
  {"a":"el techo","b":"la lámpara 💡"},{"a":"el suelo","b":"la alfombra 🟫"}]}})

# 4 · MATCH — edificio ↔ función  (pool 12)
w({"id":"es-u7-edificio-funcion","title":"Edificio y función","subtitle":"U7 · waarvoor dient dit gebouw?",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind het gebouw met wat je er doet","pairs":[
  {"a":"la panadería","b":"comprar pan 🥖"},{"a":"la farmacia","b":"comprar medicinas 💊"},
  {"a":"el banco","b":"sacar dinero 🏦"},{"a":"el supermercado","b":"comprar comida 🛒"},
  {"a":"el parque","b":"pasear y jugar 🌳"},{"a":"el cine","b":"ver una película 🎬"},
  {"a":"la estación","b":"tomar el tren 🚉"},{"a":"el museo","b":"ver arte 🏛️"},
  {"a":"la iglesia","b":"rezar ⛪"},{"a":"el hospital","b":"ir al médico 🏥"},
  {"a":"la escuela","b":"estudiar ✏️"},{"a":"el restaurante","b":"comer fuera 🍽️"}]}})

# ============================ ② DISTINGUIR · gramática/léxico ============================
# 5 · CLASSIFY — ¿hay o está/están?  (pool 20, rounds 12)
w({"id":"es-u7-hay-esta","title":"¿hay o está?","subtitle":"U7 · er is (hay) of het staat (está/están)?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Nieuw (un/una/número) → hay. Bekend (el/la) + plaats → está/están.","categories":[
  {"id":"hay","label":"hay<br><small>er is/zijn</small>","glaze":G["green"]},
  {"id":"esta","label":"está / están<br><small>staat / staan</small>","glaze":G["blue"]}],
 "items":[
  {"stimulus":"En el salón ___ un sofá.","answer":"hay","tag":"hay","sub":"un sofá = nieuw"},
  {"stimulus":"El sofá ___ al lado.","answer":"esta","tag":"esta","sub":"el sofá = bekend"},
  {"stimulus":"___ tres habitaciones.","answer":"hay","tag":"hay","sub":"número = hay"},
  {"stimulus":"Los baños ___ arriba.","answer":"esta","tag":"esta","sub":"los baños = mv."},
  {"stimulus":"___ una plaza en mi barrio.","answer":"hay","tag":"hay","sub":"una plaza = nieuw"},
  {"stimulus":"La plaza ___ en el centro.","answer":"esta","tag":"esta","sub":"la plaza = bekend"},
  {"stimulus":"___ muchas tiendas.","answer":"hay","tag":"hay","sub":"muchas = nieuw"},
  {"stimulus":"La farmacia ___ en la esquina.","answer":"esta","tag":"esta","sub":"la farmacia = bekend"},
  {"stimulus":"___ un parque cerca.","answer":"hay","tag":"hay","sub":"un parque = nieuw"},
  {"stimulus":"El parque ___ cerca.","answer":"esta","tag":"esta","sub":"el parque = bekend"},
  {"stimulus":"___ dos ventanas.","answer":"hay","tag":"hay","sub":"número = hay"},
  {"stimulus":"Las ventanas ___ abiertas.","answer":"esta","tag":"esta","sub":"las ventanas = mv."},
  {"stimulus":"En la cocina ___ una nevera.","answer":"hay","tag":"hay","sub":"una nevera = nieuw"},
  {"stimulus":"La nevera ___ al lado del horno.","answer":"esta","tag":"esta","sub":"la nevera = bekend"},
  {"stimulus":"___ un museo famoso.","answer":"hay","tag":"hay","sub":"un museo = nieuw"},
  {"stimulus":"El museo ___ enfrente de la iglesia.","answer":"esta","tag":"esta","sub":"el museo = bekend"},
  {"stimulus":"___ mucha gente en la plaza.","answer":"hay","tag":"hay","sub":"mucha = nieuw"},
  {"stimulus":"Las llaves ___ encima de la mesa.","answer":"esta","tag":"esta","sub":"las llaves = mv."},
  {"stimulus":"¿Cuántas sillas ___ ?","answer":"hay","tag":"hay","sub":"¿cuántas? = hay"},
  {"stimulus":"El banco ___ al lado de la farmacia.","answer":"esta","tag":"esta","sub":"el banco = bekend"}]}})

# 6 · CLASSIFY — habitación · mueble · edificio  (pool 21, rounds 12)
w({"id":"es-u7-clasifica-lugar","title":"habitación · mueble · edificio","subtitle":"U7 · sorteer het woord",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"¿Qué es? una habitación, un mueble of un edificio del barrio","categories":[
  {"id":"habitacion","label":"habitación<br><small>kamer</small>","glaze":G["teal"]},
  {"id":"mueble","label":"mueble<br><small>meubel</small>","glaze":G["amber"]},
  {"id":"edificio","label":"edificio<br><small>gebouw</small>","glaze":G["blue"]}],
 "items":[
  {"stimulus":"la cocina","answer":"habitacion","tag":"habitacion","sub":"keuken"},
  {"stimulus":"el salón","answer":"habitacion","tag":"habitacion","sub":"woonkamer"},
  {"stimulus":"el baño","answer":"habitacion","tag":"habitacion","sub":"badkamer"},
  {"stimulus":"el dormitorio","answer":"habitacion","tag":"habitacion","sub":"slaapkamer"},
  {"stimulus":"el comedor","answer":"habitacion","tag":"habitacion","sub":"eetkamer"},
  {"stimulus":"la cama","answer":"mueble","tag":"mueble","sub":"bed"},
  {"stimulus":"el sofá","answer":"mueble","tag":"mueble","sub":"bank"},
  {"stimulus":"el armario","answer":"mueble","tag":"mueble","sub":"kast"},
  {"stimulus":"la mesa","answer":"mueble","tag":"mueble","sub":"tafel"},
  {"stimulus":"la silla","answer":"mueble","tag":"mueble","sub":"stoel"},
  {"stimulus":"la estantería","answer":"mueble","tag":"mueble","sub":"boekenkast"},
  {"stimulus":"la lámpara","answer":"mueble","tag":"mueble","sub":"lamp"},
  {"stimulus":"la panadería","answer":"edificio","tag":"edificio","sub":"bakkerij"},
  {"stimulus":"el banco","answer":"edificio","tag":"edificio","sub":"bank"},
  {"stimulus":"la farmacia","answer":"edificio","tag":"edificio","sub":"apotheek"},
  {"stimulus":"el museo","answer":"edificio","tag":"edificio","sub":"museum"},
  {"stimulus":"la estación","answer":"edificio","tag":"edificio","sub":"station"},
  {"stimulus":"el cine","answer":"edificio","tag":"edificio","sub":"bioscoop"},
  {"stimulus":"el supermercado","answer":"edificio","tag":"edificio","sub":"supermarkt"},
  {"stimulus":"la iglesia","answer":"edificio","tag":"edificio","sub":"kerk"},
  {"stimulus":"la nevera","answer":"mueble","tag":"mueble","sub":"koelkast"}]}})

# 7 · CLASSIFY — preposición: ¿dónde?  (pool 16, rounds 10)
w({"id":"es-u7-clasifica-prepo","title":"preposición: ¿dónde?","subtitle":"U7 · welke betekenis heeft de preposición?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Koppel de preposición aan zijn betekenis","categories":[
  {"id":"cerca","label":"cerca / al lado<br><small>dichtbij/naast</small>","glaze":G["green"]},
  {"id":"vertical","label":"encima / debajo<br><small>boven/onder</small>","glaze":G["amber"]},
  {"id":"frente","label":"delante / detrás / enfrente<br><small>voor/achter/tegenover</small>","glaze":G["purple"]}],
 "items":[
  {"stimulus":"al lado de","answer":"cerca","tag":"cerca","sub":"naast"},
  {"stimulus":"cerca de","answer":"cerca","tag":"cerca","sub":"dichtbij"},
  {"stimulus":"junto a","answer":"cerca","tag":"cerca","sub":"vlak bij"},
  {"stimulus":"encima de","answer":"vertical","tag":"vertical","sub":"boven op"},
  {"stimulus":"debajo de","answer":"vertical","tag":"vertical","sub":"onder"},
  {"stimulus":"sobre","answer":"vertical","tag":"vertical","sub":"op/boven"},
  {"stimulus":"delante de","answer":"frente","tag":"frente","sub":"vóór"},
  {"stimulus":"detrás de","answer":"frente","tag":"frente","sub":"achter"},
  {"stimulus":"enfrente de","answer":"frente","tag":"frente","sub":"tegenover"},
  {"stimulus":"al lado del parque","answer":"cerca","tag":"cerca","sub":"naast het park"},
  {"stimulus":"debajo de la cama","answer":"vertical","tag":"vertical","sub":"onder het bed"},
  {"stimulus":"encima de la mesa","answer":"vertical","tag":"vertical","sub":"op de tafel"},
  {"stimulus":"detrás de la casa","answer":"frente","tag":"frente","sub":"achter het huis"},
  {"stimulus":"cerca de la plaza","answer":"cerca","tag":"cerca","sub":"dichtbij het plein"},
  {"stimulus":"delante de la puerta","answer":"frente","tag":"frente","sub":"vóór de deur"},
  {"stimulus":"enfrente del museo","answer":"frente","tag":"frente","sub":"tegenover het museum"}]}})

# 8 · CLASSIFY — ¿diptongo o hiato?  (pool 18, rounds 12)
w({"id":"es-u7-diptongo-hiato","title":"¿diptongo o hiato?","subtitle":"U7 · ortografía: één lettergreep of apart?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Diptongo = twee klinkers samen · hiato = apart (vaak met tilde op í/ú)","categories":[
  {"id":"diptongo","label":"diptongo<br><small>bue-no</small>","glaze":G["blue"]},
  {"id":"hiato","label":"hiato<br><small>dí-a</small>","glaze":G["red"]}],
 "items":[
  {"stimulus":"puerta","answer":"diptongo","tag":"diptongo","sub":"puer-ta (ue samen)"},
  {"stimulus":"día","answer":"hiato","tag":"hiato","sub":"dí-a (tilde op í)"},
  {"stimulus":"país","answer":"hiato","tag":"hiato","sub":"pa-ís (tilde op í)"},
  {"stimulus":"bueno","answer":"diptongo","tag":"diptongo","sub":"bue-no (ue samen)"},
  {"stimulus":"panadería","answer":"hiato","tag":"hiato","sub":"...rí-a (tilde op í)"},
  {"stimulus":"seis","answer":"diptongo","tag":"diptongo","sub":"seis (ei samen)"},
  {"stimulus":"tiene","answer":"diptongo","tag":"diptongo","sub":"tie-ne (ie samen)"},
  {"stimulus":"frío","answer":"hiato","tag":"hiato","sub":"frí-o (tilde op í)"},
  {"stimulus":"agua","answer":"diptongo","tag":"diptongo","sub":"a-gua (ua samen)"},
  {"stimulus":"María","answer":"hiato","tag":"hiato","sub":"Ma-rí-a (tilde op í)"},
  {"stimulus":"ciudad","answer":"diptongo","tag":"diptongo","sub":"ciu-dad (iu samen)"},
  {"stimulus":"cafetería","answer":"hiato","tag":"hiato","sub":"...rí-a (tilde op í)"},
  {"stimulus":"aire","answer":"diptongo","tag":"diptongo","sub":"ai-re (ai samen)"},
  {"stimulus":"tía","answer":"hiato","tag":"hiato","sub":"tí-a (tilde op í)"},
  {"stimulus":"cuatro","answer":"diptongo","tag":"diptongo","sub":"cua-tro (ua samen)"},
  {"stimulus":"río","answer":"hiato","tag":"hiato","sub":"rí-o (tilde op í)"},
  {"stimulus":"veinte","answer":"diptongo","tag":"diptongo","sub":"vein-te (ei samen)"},
  {"stimulus":"librería","answer":"hiato","tag":"hiato","sub":"...rí-a (tilde op í)"}]}})

# ============================ ③ PRODUCIR CON APOYO ============================
# 9 · CLOZE — estar + gerundio (VERPLICHT werkwoord-cloze, nagerekend)  (pool 18, rounds 12)
w({"id":"es-u7-gerundio-cloze","title":"Completa: estar + gerundio","subtitle":"U7 · ¿qué pasa ahora? (estoy cocinando…)",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm van «estar + gerundio»","items":[
  {"stimulus":"(Yo) ___ en la cocina.","options":["estoy cocinando","estás cocinando","estoy cocinar"],"answer":"estoy cocinando","tag":"ger","sub":"yo → estoy + cocinando"},
  {"stimulus":"¿(Tú) ___ la tele?","options":["estás viendo","estoy viendo","estás veiendo"],"answer":"estás viendo","tag":"ger","sub":"ver → viendo"},
  {"stimulus":"(Nosotros) ___ en el comedor.","options":["estamos comiendo","están comiendo","estamos comer"],"answer":"estamos comiendo","tag":"ger","sub":"comer → comiendo"},
  {"stimulus":"Valen ___ una carta.","options":["está escribiendo","están escribiendo","está escribir"],"answer":"está escribiendo","tag":"ger","sub":"escribir → escribiendo"},
  {"stimulus":"(Ellos) ___ en el dormitorio.","options":["están durmiendo","están dormiendo","está durmiendo"],"answer":"están durmiendo","tag":"ger","sub":"dormir → durmiendo"},
  {"stimulus":"(Yo) ___ un libro en el salón.","options":["estoy leyendo","estoy leiendo","estás leyendo"],"answer":"estoy leyendo","tag":"ger","sub":"leer → leyendo"},
  {"stimulus":"¿(Vosotros) ___ música?","options":["estáis escuchando","estás escuchando","estáis escuchendo"],"answer":"estáis escuchando","tag":"ger","sub":"escuchar → escuchando"},
  {"stimulus":"Mi madre ___ la casa.","options":["está limpiando","están limpiando","está limpiendo"],"answer":"está limpiando","tag":"ger","sub":"limpiar → limpiando"},
  {"stimulus":"Los niños ___ en el parque.","options":["están jugando","está jugando","están jugendo"],"answer":"están jugando","tag":"ger","sub":"jugar → jugando"},
  {"stimulus":"(Yo) ___ para el examen.","options":["estoy estudiando","estás estudiando","estoy estudiar"],"answer":"estoy estudiando","tag":"ger","sub":"estudiar → estudiando"},
  {"stimulus":"La gente ___ por la plaza.","options":["está paseando","están paseando","está paseendo"],"answer":"está paseando","tag":"ger","sub":"pasear → paseando"},
  {"stimulus":"¿Qué ___ (tú) ahora?","options":["estás haciendo","estoy haciendo","estás hacer"],"answer":"estás haciendo","tag":"ger","sub":"hacer → haciendo"},
  {"stimulus":"(Nosotros) ___ la mesa.","options":["estamos poniendo","están poniendo","estamos poner"],"answer":"estamos poniendo","tag":"ger","sub":"poner → poniendo"},
  {"stimulus":"Diego ___ por teléfono.","options":["está hablando","están hablando","está hablar"],"answer":"está hablando","tag":"ger","sub":"hablar → hablando"},
  {"stimulus":"(Yo) ___ una ducha.","options":["me estoy duchando","me estás duchando","me estoy duchar"],"answer":"me estoy duchando","tag":"ger","sub":"ducharse → duchando"},
  {"stimulus":"Las chicas ___ en la habitación.","options":["están cantando","está cantando","están cantiendo"],"answer":"están cantando","tag":"ger","sub":"cantar → cantando"},
  {"stimulus":"¿(Tú) ___ la comida?","options":["estás preparando","estoy preparando","estás preparendo"],"answer":"estás preparando","tag":"ger","sub":"preparar → preparando"},
  {"stimulus":"Papá ___ en el jardín.","options":["está trabajando","están trabajando","está trabajendo"],"answer":"está trabajando","tag":"ger","sub":"trabajar → trabajando"}]}})

# 10 · CLOZE — preposición de lugar  (pool 16, rounds 10)
w({"id":"es-u7-preposicion-cloze","title":"Completa la preposición","subtitle":"U7 · ¿dónde está? (encima de, al lado de…)",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies de preposición die bij de betekenis (haakjes) past","items":[
  {"stimulus":"La lámpara está ___ la mesa (boven op).","options":["encima de","debajo de","entre"],"answer":"encima de","tag":"prep","sub":"boven op"},
  {"stimulus":"El gato está ___ la cama (onder).","options":["debajo de","encima de","al lado de"],"answer":"debajo de","tag":"prep","sub":"onder"},
  {"stimulus":"El banco está ___ la farmacia (naast).","options":["al lado de","delante de","entre"],"answer":"al lado de","tag":"prep","sub":"naast"},
  {"stimulus":"El cine está ___ el banco y el parque.","options":["entre","encima de","detrás de"],"answer":"entre","tag":"prep","sub":"tussen A y B"},
  {"stimulus":"El jardín está ___ la casa (achter).","options":["detrás de","delante de","dentro de"],"answer":"detrás de","tag":"prep","sub":"achter"},
  {"stimulus":"Hay un árbol ___ la casa (vóór).","options":["delante de","detrás de","encima de"],"answer":"delante de","tag":"prep","sub":"vóór"},
  {"stimulus":"La ropa está ___ armario (binnen in).","options":["dentro del","encima del","entre"],"answer":"dentro del","tag":"prep","sub":"binnen in + del"},
  {"stimulus":"El museo está ___ la iglesia (tegenover).","options":["enfrente de","al lado de","debajo de"],"answer":"enfrente de","tag":"prep","sub":"tegenover"},
  {"stimulus":"El parque está ___ mi casa (dichtbij).","options":["cerca de","lejos de","dentro de"],"answer":"cerca de","tag":"prep","sub":"dichtbij"},
  {"stimulus":"La estación está ___ (ver).","options":["lejos","cerca","entre"],"answer":"lejos","tag":"prep","sub":"ver"},
  {"stimulus":"El espejo está ___ la pared (aan/tegen).","options":["en","debajo de","entre"],"answer":"en","tag":"prep","sub":"en la pared"},
  {"stimulus":"La alfombra está ___ el sofá (onder).","options":["debajo de","encima de","enfrente de"],"answer":"debajo de","tag":"prep","sub":"onder"},
  {"stimulus":"La farmacia está ___ (op de hoek).","options":["en la esquina","entre","encima de"],"answer":"en la esquina","tag":"prep","sub":"op de hoek"},
  {"stimulus":"Los libros están ___ la estantería (in).","options":["en","debajo de","delante de"],"answer":"en","tag":"prep","sub":"in de kast"},
  {"stimulus":"El coche está ___ la casa (vóór).","options":["delante de","dentro de","encima de"],"answer":"delante de","tag":"prep","sub":"vóór"},
  {"stimulus":"El supermercado está ___ mi barrio (in).","options":["en","entre","debajo de"],"answer":"en","tag":"prep","sub":"in de buurt"}]}})

# 11 · CLOZE — imperativo (el camino, nagerekend)  (pool 16, rounds 10)
w({"id":"es-u7-imperativo-cloze","title":"El camino: imperativo","subtitle":"U7 · explica el camino (gira, sigue, cruza…)",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies het juiste imperativo (tú)","items":[
  {"stimulus":"___ todo recto.","options":["Sigue","Sige","Sigues"],"answer":"Sigue","tag":"imp","sub":"seguir → sigue (e→i)"},
  {"stimulus":"___ a la derecha.","options":["Gira","Gire","Giras"],"answer":"Gira","tag":"imp","sub":"girar → gira"},
  {"stimulus":"___ la calle.","options":["Cruza","Cruce","Cruzas"],"answer":"Cruza","tag":"imp","sub":"cruzar → cruza"},
  {"stimulus":"___ la primera calle.","options":["Toma","Tome","Tomas"],"answer":"Toma","tag":"imp","sub":"tomar → toma"},
  {"stimulus":"___ por la escalera.","options":["Sube","Suba","Subes"],"answer":"Sube","tag":"imp","sub":"subir → sube"},
  {"stimulus":"___ a la plaza.","options":["Ve","Va","Vas"],"answer":"Ve","tag":"imp","sub":"ir → ve"},
  {"stimulus":"___ el autobús número 5.","options":["Coge","Coja","Coges"],"answer":"Coge","tag":"imp","sub":"coger → coge"},
  {"stimulus":"___ en el semáforo.","options":["Para","Pare","Paras"],"answer":"Para","tag":"imp","sub":"parar → para"},
  {"stimulus":"___ a la izquierda.","options":["Dobla","Doble","Doblas"],"answer":"Dobla","tag":"imp","sub":"doblar → dobla"},
  {"stimulus":"___ hasta el final de la calle.","options":["Camina","Camine","Caminas"],"answer":"Camina","tag":"imp","sub":"caminar → camina"},
  {"stimulus":"___ por el puente.","options":["Pasa","Pase","Pasas"],"answer":"Pasa","tag":"imp","sub":"pasar → pasa"},
  {"stimulus":"___ la puerta, por favor.","options":["Abre","Abra","Abres"],"answer":"Abre","tag":"imp","sub":"abrir → abre"},
  {"stimulus":"___ a la derecha en el banco.","options":["Gira","Gire","Giras"],"answer":"Gira","tag":"imp","sub":"girar → gira"},
  {"stimulus":"___ recto y luego cruza.","options":["Sigue","Sige","Sigues"],"answer":"Sigue","tag":"imp","sub":"seguir → sigue"},
  {"stimulus":"___ por la calle Real.","options":["Baja","Baje","Bajas"],"answer":"Baja","tag":"imp","sub":"bajar → baja"},
  {"stimulus":"___ el metro en la estación.","options":["Toma","Tome","Tomas"],"answer":"Toma","tag":"imp","sub":"tomar → toma"}]}})

# 12 · TETRIS — preposiciones (valt in de juiste kolom)  (pool 18)
w({"id":"es-u7-preposicion-tetris","title":"Preposiciones Tetris","subtitle":"U7 · laat elke preposición in de juiste betekenis vallen",
 "lang":"es","template":"tetris","options":{"rows":9,"speed":1300,"audio":False},
 "classify":{"categories":[
  {"id":"cerca","label":"cerca/naast","glaze":G["green"]},{"id":"vertical","label":"boven/onder","glaze":G["amber"]},
  {"id":"frente","label":"voor/achter","glaze":G["purple"]}],
 "items":[
  {"stimulus":"al lado de","answer":"cerca","tag":"cerca","sub":"naast"},
  {"stimulus":"cerca de","answer":"cerca","tag":"cerca","sub":"dichtbij"},
  {"stimulus":"junto a","answer":"cerca","tag":"cerca","sub":"vlak bij"},
  {"stimulus":"encima de","answer":"vertical","tag":"vertical","sub":"boven op"},
  {"stimulus":"debajo de","answer":"vertical","tag":"vertical","sub":"onder"},
  {"stimulus":"sobre","answer":"vertical","tag":"vertical","sub":"op"},
  {"stimulus":"delante de","answer":"frente","tag":"frente","sub":"vóór"},
  {"stimulus":"detrás de","answer":"frente","tag":"frente","sub":"achter"},
  {"stimulus":"enfrente de","answer":"frente","tag":"frente","sub":"tegenover"},
  {"stimulus":"al lado del banco","answer":"cerca","tag":"cerca","sub":"naast de bank"},
  {"stimulus":"debajo de la mesa","answer":"vertical","tag":"vertical","sub":"onder de tafel"},
  {"stimulus":"encima del armario","answer":"vertical","tag":"vertical","sub":"boven op de kast"},
  {"stimulus":"detrás de la casa","answer":"frente","tag":"frente","sub":"achter het huis"},
  {"stimulus":"cerca del parque","answer":"cerca","tag":"cerca","sub":"dichtbij het park"},
  {"stimulus":"delante de la puerta","answer":"frente","tag":"frente","sub":"vóór de deur"},
  {"stimulus":"enfrente del cine","answer":"frente","tag":"frente","sub":"tegenover de bioscoop"},
  {"stimulus":"sobre la cama","answer":"vertical","tag":"vertical","sub":"op het bed"},
  {"stimulus":"junto a la ventana","answer":"cerca","tag":"cerca","sub":"bij het raam"}]}})

# 13 · ORDER — ordena las instrucciones (la ruta)  (6 rondes)
w({"id":"es-u7-ordena-ruta","title":"Ordena las instrucciones","subtitle":"U7 · zet de route in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik de instructies in de logische volgorde van de route","rounds":[
  {"tag":"ruta","sub":"a la plaza","items":[
    {"label":"Sal de casa.","key":1},{"label":"Sigue todo recto.","key":2},
    {"label":"Gira a la derecha en el semáforo.","key":3},{"label":"La plaza está a la izquierda.","key":4}]},
  {"tag":"ruta","sub":"a la panadería","items":[
    {"label":"Cruza la calle.","key":1},{"label":"Sigue recto por la calle Real.","key":2},
    {"label":"Gira a la izquierda.","key":3},{"label":"La panadería está en la esquina.","key":4}]},
  {"tag":"ruta","sub":"al parque","items":[
    {"label":"Toma la primera calle.","key":1},{"label":"Pasa por delante del banco.","key":2},
    {"label":"Cruza el puente.","key":3},{"label":"El parque está al final.","key":4}]},
  {"tag":"ruta","sub":"a la estación","items":[
    {"label":"Baja por la calle.","key":1},{"label":"Gira a la derecha.","key":2},
    {"label":"Sigue todo recto.","key":3},{"label":"La estación está enfrente.","key":4}]},
  {"tag":"ruta","sub":"al museo","items":[
    {"label":"Sal del hotel.","key":1},{"label":"Toma el autobús número 5.","key":2},
    {"label":"Baja en la plaza.","key":3},{"label":"El museo está al lado de la iglesia.","key":4}]},
  {"tag":"ruta","sub":"al supermercado","items":[
    {"label":"Camina hasta el final de la calle.","key":1},{"label":"Gira a la izquierda.","key":2},
    {"label":"Pasa por el parque.","key":3},{"label":"El supermercado está a la derecha.","key":4}]}]}})

# 14 · ORDER — ordena de fuera a dentro / de abajo a arriba  (5 rondes)
w({"id":"es-u7-ordena-casa","title":"Ordena de fuera a dentro","subtitle":"U7 · ruimtes en verdiepingen op volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik de items in de juiste volgorde","rounds":[
  {"tag":"casa","sub":"de fuera a dentro","items":[
    {"label":"la calle","key":1},{"label":"la puerta","key":2},{"label":"el pasillo","key":3},{"label":"el salón","key":4}]},
  {"tag":"casa","sub":"los pisos (de abajo a arriba)","items":[
    {"label":"la planta baja","key":1},{"label":"el primer piso","key":2},{"label":"el segundo piso","key":3},{"label":"el tercer piso","key":4}]},
  {"tag":"casa","sub":"poner la mesa","items":[
    {"label":"el mantel","key":1},{"label":"el plato","key":2},{"label":"el tenedor","key":3},{"label":"el vaso","key":4}]},
  {"tag":"casa","sub":"los ordinales","items":[
    {"label":"primero","key":1},{"label":"segundo","key":2},{"label":"tercero","key":3},{"label":"cuarto","key":4}]},
  {"tag":"casa","sub":"la ficha del anuncio","items":[
    {"label":"Tercer piso con ascensor","key":1},{"label":"2 habitaciones","key":2},{"label":"Terraza con vistas","key":3},{"label":"600 €/mes","key":4}]}]}})

# 15 · POINT — señala en la habitación  (10 rondes)
w({"id":"es-u7-senala-habitacion","title":"Señala en la habitación","subtitle":"U7 · klik het juiste mueble/lugar",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het gevraagde item","mode":"one","rounds":[
  {"tag":"cama","sub":"señala dónde duermes","targets":[
    {"label":"la cama 🛏️","hit":True},{"label":"el sofá"},{"label":"la mesa"},{"label":"el armario"}]},
  {"tag":"cocina","sub":"señala dónde cocinas","targets":[
    {"label":"el baño"},{"label":"la cocina 🍳","hit":True},{"label":"el salón"},{"label":"el jardín"}]},
  {"tag":"nevera","sub":"señala dónde está la leche","targets":[
    {"label":"la lámpara"},{"label":"la nevera 🧊","hit":True},{"label":"el espejo"},{"label":"la silla"}]},
  {"tag":"ducha","sub":"señala dónde te duchas","targets":[
    {"label":"la ducha 🚿","hit":True},{"label":"la cama"},{"label":"el sofá"},{"label":"la mesa"}]},
  {"tag":"sofa","sub":"señala dónde ves la tele","targets":[
    {"label":"la cama"},{"label":"la ducha"},{"label":"el sofá 🛋️","hit":True},{"label":"el armario"}]},
  {"tag":"armario","sub":"señala dónde está la ropa","targets":[
    {"label":"el armario 🚪","hit":True},{"label":"la nevera"},{"label":"la mesa"},{"label":"la ventana"}]},
  {"tag":"ventana","sub":"señala por dónde entra la luz","targets":[
    {"label":"la ventana 🪟","hit":True},{"label":"la pared"},{"label":"el suelo"},{"label":"el techo"}]},
  {"tag":"escalera","sub":"señala cómo subes al piso","targets":[
    {"label":"la escalera 🪜","hit":True},{"label":"la puerta"},{"label":"la alfombra"},{"label":"la mesa"}]},
  {"tag":"estanteria","sub":"señala dónde están los libros","targets":[
    {"label":"la estantería 📚","hit":True},{"label":"la cama"},{"label":"la ducha"},{"label":"el sofá"}]},
  {"tag":"espejo","sub":"señala dónde te miras","targets":[
    {"label":"el espejo 🪞","hit":True},{"label":"la lámpara"},{"label":"la nevera"},{"label":"la silla"}]}]}})

# 16 · POINT — señala en el plano del barrio  (10 rondes)
w({"id":"es-u7-senala-plano","title":"Señala en el plano del barrio","subtitle":"U7 · klik het juiste edificio/lugar",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het gevraagde gebouw","mode":"one","rounds":[
  {"tag":"pan","sub":"¿dónde compras pan?","targets":[
    {"label":"la panadería 🥖","hit":True},{"label":"el banco"},{"label":"el cine"},{"label":"el museo"}]},
  {"tag":"dinero","sub":"¿dónde sacas dinero?","targets":[
    {"label":"la farmacia"},{"label":"el banco 🏦","hit":True},{"label":"el parque"},{"label":"la iglesia"}]},
  {"tag":"medicina","sub":"¿dónde compras medicinas?","targets":[
    {"label":"la farmacia 💊","hit":True},{"label":"la panadería"},{"label":"la estación"},{"label":"el cine"}]},
  {"tag":"tren","sub":"¿dónde tomas el tren?","targets":[
    {"label":"el museo"},{"label":"la estación 🚉","hit":True},{"label":"el parque"},{"label":"la iglesia"}]},
  {"tag":"pelicula","sub":"¿dónde ves una película?","targets":[
    {"label":"el cine 🎬","hit":True},{"label":"el banco"},{"label":"la farmacia"},{"label":"el hospital"}]},
  {"tag":"pasear","sub":"¿dónde paseas y juegas?","targets":[
    {"label":"el parque 🌳","hit":True},{"label":"el supermercado"},{"label":"la estación"},{"label":"el banco"}]},
  {"tag":"comida","sub":"¿dónde compras comida?","targets":[
    {"label":"el supermercado 🛒","hit":True},{"label":"el museo"},{"label":"el cine"},{"label":"la iglesia"}]},
  {"tag":"arte","sub":"¿dónde ves arte?","targets":[
    {"label":"el museo 🏛️","hit":True},{"label":"la panadería"},{"label":"el banco"},{"label":"la estación"}]},
  {"tag":"esquina","sub":"¿qué está en la esquina?","targets":[
    {"label":"la farmacia (en la esquina)","hit":True},{"label":"el centro de la plaza"},{"label":"el parque grande"},{"label":"el río"}]},
  {"tag":"plaza","sub":"¿dónde se reúne la gente?","targets":[
    {"label":"la plaza ⛲","hit":True},{"label":"el armario"},{"label":"el pasillo"},{"label":"la nevera"}]}]}})

# ============================ ④ ANALIZAR & COMUNICAR ============================
# 17 · SIM — ¡Explica el camino! (productie met bouwsteen-check)  (6 rondes)
w({"id":"es-u7-explica-camino","title":"¡Explica el camino!","subtitle":"U7 · schrijf de route — met alle bouwstenen",
 "lang":"es","template":"sim","options":{"audio":False},
 "sim":{"prompt":"Tarea comunicativa · explica el camino / describe tu casa","rounds":[
  {"scenario":"Un turista pregunta: «¿Cómo se va a la plaza?» — explícale el camino.","tag":"camino","sub":"gebruik: sigue · gira · todo recto","min":10,
   "need":[{"re":"sigue|sige","label":"sigue …"},{"re":"gira|dobla","label":"gira/dobla …"},{"re":"recto|derecha|izquierda","label":"recto/derecha/izquierda"}],
   "bank":["Sigue todo recto","gira a la derecha","gira a la izquierda","cruza la calle","la plaza está","al final"],
   "model":"Sigue todo recto y gira a la derecha. La plaza está al final de la calle."},
  {"scenario":"Describe tu salón: ¿qué hay y dónde está cada cosa?","tag":"describir","sub":"gebruik: hay · está · una preposición","min":10,
   "need":[{"re":"hay","label":"hay …"},{"re":"est[aá]","label":"está / están"},{"re":"al lado|encima|debajo|entre|delante|detrás|enfrente|cerca","label":"una preposición"}],
   "bank":["En mi salón hay","un sofá","una mesa","está al lado de","está enfrente de","la ventana"],
   "model":"En mi salón hay un sofá y una mesa. El sofá está al lado de la ventana."},
  {"scenario":"Di qué estás haciendo ahora en casa (estar + gerundio).","tag":"gerundio","sub":"gebruik: estoy + -ando/-iendo","min":8,
   "need":[{"re":"estoy|estamos","label":"estoy/estamos …"},{"re":"ando|iendo|yendo","label":"un gerundio (-ando/-iendo)"},{"re":"cocina|salón|salon|habitación|habitacion|casa|comedor","label":"un lugar de la casa"}],
   "bank":["Ahora estoy","cocinando","viendo la tele","en la cocina","en el salón","estudiando"],
   "model":"Ahora estoy cocinando en la cocina y mi hermano está viendo la tele."},
  {"scenario":"Describe una vivienda para un anuncio (habitaciones, piso, precio).","tag":"anuncio","sub":"gebruik: tiene · habitaciones · piso · euros","min":9,
   "need":[{"re":"tiene|hay","label":"tiene / hay"},{"re":"habitaci","label":"habitaciones"},{"re":"piso|planta","label":"piso / planta"}],
   "bank":["Se alquila piso","tiene dos habitaciones","tercer piso","con ascensor","cerca del parque","600 euros al mes"],
   "model":"Se alquila piso en el tercer piso. Tiene dos habitaciones y está cerca del parque. 600 euros al mes."},
  {"scenario":"¿Dónde está tu casa? Di qué hay cerca en tu barrio.","tag":"barrio","sub":"gebruik: cerca de · hay · al lado de","min":8,
   "need":[{"re":"cerca|al lado|enfrente","label":"cerca de / al lado de"},{"re":"hay","label":"hay …"},{"re":"parque|plaza|tienda|panadería|panaderia|banco|supermercado","label":"un lugar del barrio"}],
   "bank":["Mi casa está cerca de","hay una plaza","al lado de la panadería","enfrente del parque","el supermercado"],
   "model":"Mi casa está cerca de la plaza. Al lado hay una panadería y enfrente hay un parque."},
  {"scenario":"Invita a un amigo a tu casa y dile cómo llegar.","tag":"invitar","sub":"gebruik: ven a · toma · baja en","min":9,
   "need":[{"re":"ven|te invito","label":"ven a / te invito"},{"re":"toma|coge|autobús|autobus|metro","label":"toma el autobús/metro"},{"re":"baja|para|gira|sigue","label":"baja / gira / sigue"}],
   "bank":["Ven a mi casa","toma el autobús 5","baja en la plaza","gira a la derecha","vivo en el tercer piso"],
   "model":"Ven a mi casa. Toma el autobús 5 y baja en la plaza. Vivo en el tercer piso."}]}})

# ============================ ⑤ HABLAR · grábate 🎙️ ============================
# 18 · SPEAK repeat — escucha y repite: en el barrio  (8 items)
w({"id":"es-u7-repite-barrio","title":"Escucha y repite: en el barrio","subtitle":"U7 · escucha el modelo, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite en voz alta · grábate ⏺","items":[
  {"text":"En mi barrio hay una plaza muy bonita.","sub":"in mijn buurt is een mooi plein","tag":"hay","tip":"¡Bien! Ahora dilo sin leer. <span class='nl'>zeg het nu zonder te lezen.</span>"},
  {"text":"La panadería está al lado del parque.","sub":"de bakkerij is naast het park","tag":"prep"},
  {"text":"Estoy cocinando en la cocina.","sub":"ik ben aan het koken in de keuken","tag":"gerundio"},
  {"text":"Sigue todo recto y gira a la derecha.","sub":"ga rechtdoor en sla rechtsaf","tag":"imperativo"},
  {"text":"Vivo en el tercer piso, con ascensor.","sub":"ik woon op de derde verdieping, met lift","tag":"ordinal"},
  {"text":"El baño está al final del pasillo.","sub":"de badkamer is aan het eind van de gang","tag":"prep"},
  {"text":"Hay muchas casas de colores.","sub":"er zijn veel kleurrijke huizen","tag":"hay"},
  {"text":"¿Cómo se va a la estación?","sub":"hoe kom ik bij het station?","tag":"camino"}]}})

# 19 · SPEAK shadowing — con Valen (afbouwende fasen)  (6 items)
w({"id":"es-u7-shadowing-valen","title":"Shadowing con Valen","subtitle":"U7 · praat mee met Valen, steeds minder tekst",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"shadowing","prompt":"Escucha ▶ · habla al mismo tiempo · grábate ⏺","phases":["Texto completo","Palabras clave","Sin texto","Tu versión"],"items":[
  {"text":"Vivo en un barrio de casas de colores en Cartagena.","sub":"ik woon in een buurt met kleurrijke huizen in Cartagena","tag":"barrio"},
  {"text":"Enfrente de mi casa hay una plaza con palmeras.","sub":"tegenover mijn huis is een plein met palmbomen","tag":"prep"},
  {"text":"Por la tarde, la gente está paseando por la plaza.","sub":"'s middags wandelen de mensen over het plein","tag":"gerundio"},
  {"text":"La panadería está al lado y el mar está cerca.","sub":"de bakkerij is naast en de zee is dichtbij","tag":"prep"},
  {"text":"Para llegar, sigue todo recto y cruza el semáforo.","sub":"om te komen: ga rechtdoor en steek over bij het licht","tag":"imperativo"},
  {"text":"¡Ven a visitar mi barrio! Te va a encantar.","sub":"kom mijn buurt bezoeken! je gaat het geweldig vinden","tag":"invitar","tip":"Ahora invita a un amigo de verdad. <span class='nl'>nodig nu een echte vriend uit.</span>"}]}})

# 20 · SPEAK voicemessage — explica el camino / describe habitación  (3 items)
w({"id":"es-u7-explica-camino-voz","title":"Mensaje de voz: explica el camino","subtitle":"U7 · neem een spraakbericht op",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz (30 s)","items":[
  {"text":"Explica el camino de la escuela a la plaza (usa sigue, gira, cruza).","cue":"el camino","tag":"camino",
   "sub":"gebruik: sigue todo recto · gira a la derecha/izquierda · cruza · está al final",
   "tip":"Heb je 4-5 instructies met imperativo gezegd? Neem opnieuw op. <span class='nl'>4-5 instructies met imperativo? herneem.</span>"},
  {"text":"Describe tu habitación (¿qué hay? ¿dónde está cada mueble?).","cue":"mi habitación","tag":"describir",
   "sub":"gebruik: hay · está · al lado de · encima de · debajo de",
   "tip":"Heb je hay, una preposición én un mueble gezegd? Herneem. <span class='nl'>hay + preposición + meubel? herneem.</span>"},
  {"text":"Deja un mensaje: ¿qué estás haciendo ahora en casa?","cue":"ahora mismo","tag":"gerundio",
   "sub":"gebruik: estoy + gerundio (-ando/-iendo) · en la cocina / el salón…",
   "tip":"2 acciones met estar+gerundio + un lugar? Herneem. <span class='nl'>2 acties met estar+gerundio + een plek? herneem.</span>"}]}})

# 21 · SPEAK repeat — describe tu habitación  (6 items)
w({"id":"es-u7-describe-habitacion","title":"Describe tu habitación","subtitle":"U7 · beschrijf je kamer, grábate",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · describe tu habitación · grábate ⏺","items":[
  {"cue":"Modelo · Valen 🇨🇴","text":"Mi habitación es pequeña pero bonita.","sub":"mijn kamer is klein maar mooi","tag":"describir"},
  {"cue":"¿qué hay?","text":"Hay una cama, un armario y una mesa.","sub":"er is een bed, een kast en een tafel","tag":"describir"},
  {"cue":"¿dónde?","text":"La cama está al lado de la ventana.","sub":"het bed staat naast het raam","tag":"describir"},
  {"cue":"¿y más?","text":"Encima de la mesa hay una lámpara.","sub":"op de tafel staat een lamp","tag":"describir"},
  {"cue":"¿ahora?","text":"Ahora estoy estudiando en mi habitación.","sub":"nu ben ik aan het studeren in mijn kamer","tag":"describir"},
  {"cue":"tu versión","text":"En mi habitación hay ___ . La cama está ___ .","sub":"jouw versie — vul in en zeg ze","tag":"describir",
   "tip":"Ahora describe la habitación de un amigo. <span class='nl'>beschrijf nu de kamer van een vriend(in).</span>"}]}})

print("\n21 U7-spellen geschreven (10 templates: memory·match·classify·cloze·tetris·order·point·sim·speak).")
print("Pools >=12 per game; options.rounds lager => herspeling geeft een andere reeks.")
