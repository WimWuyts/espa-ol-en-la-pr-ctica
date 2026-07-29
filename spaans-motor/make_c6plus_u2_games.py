#!/usr/bin/env python3
# Motor-content-JSON's voor C6+ · U2 «Aquí vivo» (casa · hay/estar+prep · estar+gerundio · OD lo/la).
# Templates: memory·match·classify·cloze·tetris·order·point·speak. Pools >=12; rounds lager => andere reeks.
# Werkwoords-/gerundiovormen nagerekend. Slug-prefix = es-c6plus-u2-.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")
def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2)); print("wrote", os.path.basename(p))
G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0","magenta":"#B4309A"}
PRE = "es-c6plus-u2-"

# 1 · MEMORY — muebles/habitaciones ES ↔ NL (pool 14)
w({"id":PRE+"casa-memoria","title":"Memoria de la casa","subtitle":"U2 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: casa + vertaling","pairs":[
  {"a":"la cama","b":"het bed"},{"a":"el sofá","b":"de zetel"},{"a":"la cocina","b":"de keuken"},
  {"a":"el dormitorio","b":"de slaapkamer"},{"a":"el armario","b":"de kast"},{"a":"la nevera","b":"de koelkast"},
  {"a":"el salón","b":"de woonkamer"},{"a":"la mesa","b":"de tafel"},{"a":"la silla","b":"de stoel"},
  {"a":"el baño","b":"de badkamer"},{"a":"la ventana","b":"het raam"},{"a":"el espejo","b":"de spiegel"},
  {"a":"la estantería","b":"de boekenkast"},{"a":"la lámpara","b":"de lamp"}]}})

# 2 · MEMORY — el barrio / lugares ES ↔ NL (pool 12)
w({"id":PRE+"barrio-memoria","title":"Memoria del barrio","subtitle":"U2 · zoek de plek + de vertaling",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: lugar + vertaling","pairs":[
  {"a":"la plaza","b":"het plein"},{"a":"el parque","b":"het park"},{"a":"la tienda","b":"de winkel"},
  {"a":"la farmacia","b":"de apotheek"},{"a":"el banco","b":"de bank"},{"a":"la parada","b":"de halte"},
  {"a":"el supermercado","b":"de supermarkt"},{"a":"la calle","b":"de straat"},{"a":"la esquina","b":"de hoek"},
  {"a":"la estación","b":"het station"},{"a":"el semáforo","b":"het verkeerslicht"},{"a":"el centro","b":"het centrum"}]}})

# 3 · MATCH — lugar ↔ función (pool 12)
w({"id":PRE+"lugar-funcion","title":"Lugar y función","subtitle":"U2 · koppel de plek aan wat je er doet",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind de plek met de functie","pairs":[
  {"a":"la farmacia","b":"comprar medicinas 💊"},{"a":"el supermercado","b":"comprar comida 🛒"},
  {"a":"la parada","b":"coger el autobús 🚌"},{"a":"el parque","b":"pasear 🌳"},
  {"a":"el banco","b":"sacar dinero 💰"},{"a":"la estación","b":"coger el tren 🚆"},
  {"a":"la plaza","b":"quedar con amigos 🟨"},{"a":"la cocina","b":"cocinar 🍳"},
  {"a":"el dormitorio","b":"dormir 🛏️"},{"a":"el baño","b":"ducharse 🚿"},
  {"a":"la panadería","b":"comprar pan 🥖"},{"a":"el garaje","b":"aparcar el coche 🚗"}]}})

# 4 · CLASSIFY — ¿hay o está(n)? (pool 16, rounds 10)
w({"id":PRE+"hay-estar","title":"¿hay o está(n)?","subtitle":"U2 · onbepaald (hay) of bepaald (está/están)?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Kies: hay (er is, onbepaald) of está/están (bepaald)?","categories":[
  {"id":"hay","label":"hay<br><small>un/dos/mucho</small>","glaze":G["purple"]},
  {"id":"esta","label":"está/están<br><small>el/la/mi</small>","glaze":G["teal"]}],
 "items":[
  {"stimulus":"En el salón ___ un sofá.","answer":"hay","tag":"hay","sub":"un → hay"},
  {"stimulus":"El sofá ___ delante de la tele.","answer":"esta","tag":"esta","sub":"el → está"},
  {"stimulus":"En mi barrio ___ dos parques.","answer":"hay","tag":"hay","sub":"dos → hay"},
  {"stimulus":"Los parques ___ cerca.","answer":"esta","tag":"esta","sub":"los → están"},
  {"stimulus":"¿___ una farmacia cerca?","answer":"hay","tag":"hay","sub":"una → hay"},
  {"stimulus":"La farmacia ___ en la esquina.","answer":"esta","tag":"esta","sub":"la → está"},
  {"stimulus":"En la cocina ___ una mesa.","answer":"hay","tag":"hay","sub":"una → hay"},
  {"stimulus":"Mi casa ___ en el centro.","answer":"esta","tag":"esta","sub":"mi → está"},
  {"stimulus":"___ muchas tiendas aquí.","answer":"hay","tag":"hay","sub":"muchas → hay"},
  {"stimulus":"Las tiendas ___ abiertas.","answer":"esta","tag":"esta","sub":"las → están"},
  {"stimulus":"Detrás de casa ___ un jardín.","answer":"hay","tag":"hay","sub":"un → hay"},
  {"stimulus":"El jardín ___ detrás de la casa.","answer":"esta","tag":"esta","sub":"el → está"},
  {"stimulus":"En el dormitorio ___ una cama.","answer":"hay","tag":"hay","sub":"una → hay"},
  {"stimulus":"La cama ___ al lado de la ventana.","answer":"esta","tag":"esta","sub":"la → está"},
  {"stimulus":"¿Cuántos baños ___ ?","answer":"hay","tag":"hay","sub":"cuántos → hay"},
  {"stimulus":"El banco ___ lejos.","answer":"esta","tag":"esta","sub":"el → está"}]}})

# 5 · CLASSIFY — ¿-ando o -iendo? (pool 16, rounds 10)
w({"id":PRE+"gerundio-tipo","title":"¿-ando o -iendo?","subtitle":"U2 · welke gerundio-uitgang?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Krijgt dit werkwoord -ando (-ar) of -iendo (-er/-ir)?","categories":[
  {"id":"ando","label":"-ando<br><small>-ar</small>","glaze":G["purple"]},
  {"id":"iendo","label":"-iendo<br><small>-er / -ir</small>","glaze":G["magenta"]}],
 "items":[
  {"stimulus":"cocinar","answer":"ando","tag":"ando","sub":"cocinando"},
  {"stimulus":"comer","answer":"iendo","tag":"iendo","sub":"comiendo"},
  {"stimulus":"estudiar","answer":"ando","tag":"ando","sub":"estudiando"},
  {"stimulus":"escribir","answer":"iendo","tag":"iendo","sub":"escribiendo"},
  {"stimulus":"hablar","answer":"ando","tag":"ando","sub":"hablando"},
  {"stimulus":"beber","answer":"iendo","tag":"iendo","sub":"bebiendo"},
  {"stimulus":"trabajar","answer":"ando","tag":"ando","sub":"trabajando"},
  {"stimulus":"vivir","answer":"iendo","tag":"iendo","sub":"viviendo"},
  {"stimulus":"limpiar","answer":"ando","tag":"ando","sub":"limpiando"},
  {"stimulus":"aprender","answer":"iendo","tag":"iendo","sub":"aprendiendo"},
  {"stimulus":"pasear","answer":"ando","tag":"ando","sub":"paseando"},
  {"stimulus":"abrir","answer":"iendo","tag":"iendo","sub":"abriendo"},
  {"stimulus":"cantar","answer":"ando","tag":"ando","sub":"cantando"},
  {"stimulus":"correr","answer":"iendo","tag":"iendo","sub":"corriendo"},
  {"stimulus":"jugar","answer":"ando","tag":"ando","sub":"jugando"},
  {"stimulus":"subir","answer":"iendo","tag":"iendo","sub":"subiendo"}]}})

# 6 · CLOZE — estar + gerundio (VERPLICHT, nagerekend) (pool 18, rounds 12)
w({"id":PRE+"gerundio","title":"Completa: estar + gerundio","subtitle":"U2 · ¿qué está pasando ahora?",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies de juiste estar + gerundio-vorm","items":[
  {"stimulus":"Valen ___ en la cocina.","options":["está cocinando","estoy cocinando","están cocinando"],"answer":"está cocinando","tag":"g","sub":"ella → está cocinando"},
  {"stimulus":"(Yo) ___ para el examen.","options":["estoy estudiando","estás estudiando","está estudiando"],"answer":"estoy estudiando","tag":"g","sub":"yo → estoy estudiando"},
  {"stimulus":"Los niños ___ ahora.","options":["están durmiendo","está durmiendo","estamos durmiendo"],"answer":"están durmiendo","tag":"g","sub":"ellos → durmiendo (o→u)"},
  {"stimulus":"¿(Tú) ___ un libro?","options":["estás leyendo","estoy leyendo","está leyendo"],"answer":"estás leyendo","tag":"g","sub":"tú → leyendo (i→y)"},
  {"stimulus":"(Nosotros) ___ en la terraza.","options":["estamos comiendo","estáis comiendo","están comiendo"],"answer":"estamos comiendo","tag":"g","sub":"nosotros → comiendo"},
  {"stimulus":"Mamá ___ un mensaje.","options":["está escribiendo","estás escribiendo","estoy escribiendo"],"answer":"está escribiendo","tag":"g","sub":"ella → escribiendo"},
  {"stimulus":"Diego ___ una pizza.","options":["está pidiendo","está pediendo","está pidiando"],"answer":"está pidiendo","tag":"g","sub":"pedir → pidiendo (e→i)"},
  {"stimulus":"(Yo) ___ la tele.","options":["estoy viendo","estoy veiendo","estoy vidiendo"],"answer":"estoy viendo","tag":"g","sub":"ver → viendo"},
  {"stimulus":"¿(Vosotros) ___ música?","options":["estáis escuchando","están escuchando","estamos escuchando"],"answer":"estáis escuchando","tag":"g","sub":"vosotros → escuchando"},
  {"stimulus":"El bebé ___ .","options":["está durmiendo","está dormiendo","está durmando"],"answer":"está durmiendo","tag":"g","sub":"dormir → durmiendo"},
  {"stimulus":"(Nosotros) ___ la casa.","options":["estamos limpiando","estáis limpiando","están limpiando"],"answer":"estamos limpiando","tag":"g","sub":"nosotros → limpiando"},
  {"stimulus":"Valen ___ por el parque.","options":["está paseando","estás paseando","estoy paseando"],"answer":"está paseando","tag":"g","sub":"ella → paseando"},
  {"stimulus":"(Yo) ___ un correo.","options":["estoy escribiendo","estoy escribando","estoy escribiendo"],"answer":"estoy escribiendo","tag":"g","sub":"yo → escribiendo"},
  {"stimulus":"Los amigos ___ al fútbol.","options":["están jugando","está jugando","estamos jugando"],"answer":"están jugando","tag":"g","sub":"ellos → jugando"},
  {"stimulus":"¿Qué ___ (tú) ahora?","options":["estás haciendo","estás haciando","estás hacando"],"answer":"estás haciendo","tag":"g","sub":"hacer → haciendo"},
  {"stimulus":"El profe ___ algo.","options":["está diciendo","está deciendo","está dijiendo"],"answer":"está diciendo","tag":"g","sub":"decir → diciendo"},
  {"stimulus":"(Yo) ___ agua.","options":["estoy bebiendo","estoy bebando","estoy biebiendo"],"answer":"estoy bebiendo","tag":"g","sub":"beber → bebiendo"},
  {"stimulus":"Ellos ___ la maleta.","options":["están abriendo","están abrando","está abriendo"],"answer":"están abriendo","tag":"g","sub":"abrir → abriendo"}]}})

# 7 · CLOZE — lo/la/los/las (OD) (pool 16, rounds 10)
w({"id":PRE+"lo-la","title":"Completa: lo/la/los/las","subtitle":"U2 · vervang het voorwerp",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies het juiste OD-pronomen","items":[
  {"stimulus":"¿El sofá? ___ pongo aquí.","options":["Lo","La","Los"],"answer":"Lo","tag":"od","sub":"el sofá (m ev) → lo"},
  {"stimulus":"¿La cama? ___ pongo aquí.","options":["La","Lo","Las"],"answer":"La","tag":"od","sub":"la cama (v ev) → la"},
  {"stimulus":"¿Los platos? ___ lavo.","options":["Los","Las","Lo"],"answer":"Los","tag":"od","sub":"los platos (m pl) → los"},
  {"stimulus":"¿Las sillas? ___ pongo en la cocina.","options":["Las","Los","La"],"answer":"Las","tag":"od","sub":"las sillas (v pl) → las"},
  {"stimulus":"¿La tele? ___ veo por la noche.","options":["La","Lo","Las"],"answer":"La","tag":"od","sub":"la tele (v) → la"},
  {"stimulus":"¿El coche? ___ aparco en el garaje.","options":["Lo","La","Los"],"answer":"Lo","tag":"od","sub":"el coche (m) → lo"},
  {"stimulus":"¿Las ventanas? ___ limpio.","options":["Las","Los","La"],"answer":"Las","tag":"od","sub":"las ventanas → las"},
  {"stimulus":"¿Los libros? ___ leo en el salón.","options":["Los","Las","Lo"],"answer":"Los","tag":"od","sub":"los libros → los"},
  {"stimulus":"¿La plaza? ___ veo desde el balcón.","options":["La","Lo","Las"],"answer":"La","tag":"od","sub":"la plaza → la"},
  {"stimulus":"¿El armario? ___ abro.","options":["Lo","La","Los"],"answer":"Lo","tag":"od","sub":"el armario → lo"},
  {"stimulus":"¿El autobús? ___ cojo en la parada.","options":["Lo","La","Los"],"answer":"Lo","tag":"od","sub":"el autobús → lo"},
  {"stimulus":"¿La comida? Mamá ___ prepara.","options":["la","lo","las"],"answer":"la","tag":"od","sub":"la comida → la"},
  {"stimulus":"¿Los muebles? ___ compro en la tienda.","options":["Los","Las","Lo"],"answer":"Los","tag":"od","sub":"los muebles → los"},
  {"stimulus":"¿La lámpara? ___ pongo encima de la mesa.","options":["La","Lo","Las"],"answer":"La","tag":"od","sub":"la lámpara → la"},
  {"stimulus":"¿Las flores? ___ pongo en el balcón.","options":["Las","Los","La"],"answer":"Las","tag":"od","sub":"las flores → las"},
  {"stimulus":"¿El espejo? ___ pongo en el baño.","options":["Lo","La","Los"],"answer":"Lo","tag":"od","sub":"el espejo → lo"}]}})

# 8 · TETRIS — el pronombre OD (lo/la/los/las) (pool 16)
w({"id":PRE+"lo-la-tetris","title":"lo/la Tetris","subtitle":"U2 · laat het juiste pronomen vallen",
 "lang":"es","template":"tetris","options":{"rows":9,"speed":1300,"audio":False},
 "classify":{"categories":[
  {"id":"lo","label":"lo","glaze":G["blue"]},{"id":"la","label":"la","glaze":G["red"]},
  {"id":"los","label":"los","glaze":G["green"]},{"id":"las","label":"las","glaze":G["amber"]}],
 "items":[
  {"stimulus":"el sofá","answer":"lo","tag":"lo","sub":"m ev"},{"stimulus":"la cama","answer":"la","tag":"la","sub":"v ev"},
  {"stimulus":"los libros","answer":"los","tag":"los","sub":"m pl"},{"stimulus":"las sillas","answer":"las","tag":"las","sub":"v pl"},
  {"stimulus":"el espejo","answer":"lo","tag":"lo","sub":"m ev"},{"stimulus":"la tele","answer":"la","tag":"la","sub":"v ev"},
  {"stimulus":"los platos","answer":"los","tag":"los","sub":"m pl"},{"stimulus":"las ventanas","answer":"las","tag":"las","sub":"v pl"},
  {"stimulus":"el coche","answer":"lo","tag":"lo","sub":"m ev"},{"stimulus":"la mesa","answer":"la","tag":"la","sub":"v ev"},
  {"stimulus":"los muebles","answer":"los","tag":"los","sub":"m pl"},{"stimulus":"las flores","answer":"las","tag":"las","sub":"v pl"},
  {"stimulus":"el armario","answer":"lo","tag":"lo","sub":"m ev"},{"stimulus":"la plaza","answer":"la","tag":"la","sub":"v ev"},
  {"stimulus":"los parques","answer":"los","tag":"los","sub":"m pl"},{"stimulus":"las tiendas","answer":"las","tag":"las","sub":"v pl"}]}})

# 9 · ORDER — da las direcciones / ordena (8 rondes)
w({"id":PRE+"direcciones-order","title":"Ordena la ruta","subtitle":"U2 · zet de weg/zin in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik in de logische volgorde","rounds":[
  {"tag":"ruta","sub":"cómo llegar a la plaza","items":[
    {"label":"Sal de casa.","key":1},{"label":"Sigue recto.","key":2},{"label":"Gira a la derecha.","key":3},{"label":"La plaza está a la izquierda.","key":4}]},
  {"tag":"frase","sub":"una frase con preposición","items":[
    {"label":"La lámpara","key":1},{"label":"está","key":2},{"label":"encima de","key":3},{"label":"la mesa.","key":4}]},
  {"tag":"frase","sub":"hay + lugar","items":[
    {"label":"En mi barrio","key":1},{"label":"hay","key":2},{"label":"un parque","key":3},{"label":"muy grande.","key":4}]},
  {"tag":"frase","sub":"estar + gerundio","items":[
    {"label":"Valen","key":1},{"label":"está","key":2},{"label":"cocinando","key":3},{"label":"en la cocina.","key":4}]},
  {"tag":"frase","sub":"pronombre OD","items":[
    {"label":"¿El sofá?","key":1},{"label":"Lo","key":2},{"label":"pongo","key":3},{"label":"en el salón.","key":4}]},
  {"tag":"ruta","sub":"cómo llegar a la farmacia","items":[
    {"label":"Cruza la calle.","key":1},{"label":"Sigue recto.","key":2},{"label":"Gira a la izquierda.","key":3},{"label":"La farmacia está en la esquina.","key":4}]},
  {"tag":"frase","sub":"de casa al insti","items":[
    {"label":"Cojo el autobús","key":1},{"label":"en la parada,","key":2},{"label":"bajo en el centro","key":3},{"label":"y ando cinco minutos.","key":4}]},
  {"tag":"frase","sub":"describe la habitación","items":[
    {"label":"En mi dormitorio","key":1},{"label":"la cama está","key":2},{"label":"al lado de","key":3},{"label":"la ventana.","key":4}]}]}})

# 10 · POINT — señala (repaso gemengd) (10 rondes)
w({"id":PRE+"senala","title":"Señala","subtitle":"U2 · klik het juiste antwoord",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het gevraagde item","mode":"one","rounds":[
  {"tag":"casa","sub":"señala un mueble","targets":[
    {"label":"la plaza"},{"label":"el sofá","hit":True},{"label":"la farmacia"},{"label":"la calle"}]},
  {"tag":"casa","sub":"señala una habitación","targets":[
    {"label":"la cocina","hit":True},{"label":"la cama"},{"label":"el parque"},{"label":"la silla"}]},
  {"tag":"prep","sub":"«op/boven» = ?","targets":[
    {"label":"debajo de"},{"label":"encima de","hit":True},{"label":"al lado de"},{"label":"detrás de"}]},
  {"tag":"prep","sub":"«naast» = ?","targets":[
    {"label":"al lado de","hit":True},{"label":"delante de"},{"label":"entre"},{"label":"lejos de"}]},
  {"tag":"hayest","sub":"¿«En el salón ___ un sofá»?","targets":[
    {"label":"hay","hit":True},{"label":"está"},{"label":"están"},{"label":"es"}]},
  {"tag":"ger","sub":"comer → gerundio","targets":[
    {"label":"comando"},{"label":"comiendo","hit":True},{"label":"comendo"},{"label":"comiando"}]},
  {"tag":"ger","sub":"leer → gerundio","targets":[
    {"label":"leiendo"},{"label":"leyendo","hit":True},{"label":"leendo"},{"label":"leando"}]},
  {"tag":"od","sub":"¿La casa? ___ veo","targets":[
    {"label":"lo"},{"label":"la","hit":True},{"label":"los"},{"label":"las"}]},
  {"tag":"od","sub":"¿Los muebles? ___ compro","targets":[
    {"label":"los","hit":True},{"label":"las"},{"label":"lo"},{"label":"la"}]},
  {"tag":"barrio","sub":"señala un lugar del barrio","targets":[
    {"label":"el armario"},{"label":"la plaza","hit":True},{"label":"la nevera"},{"label":"el espejo"}]}]}})

# 11 · SPEAK repeat — describe tu casa/barrio (8 items)
w({"id":PRE+"repite-casa","title":"Escucha y repite: mi casa","subtitle":"U2 · escucha, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite en voz alta · grábate ⏺","items":[
  {"text":"En mi casa hay tres habitaciones.","sub":"in mijn huis zijn drie kamers","tag":"casa","tip":"¡Bien! Ahora dilo sin leer."},
  {"text":"La cama está al lado de la ventana.","sub":"het bed staat naast het raam","tag":"prep"},
  {"text":"El sofá está delante de la tele.","sub":"de zetel staat vóór de tv","tag":"prep"},
  {"text":"Ahora mismo estoy estudiando.","sub":"op dit moment ben ik aan het studeren","tag":"ger"},
  {"text":"En mi barrio hay una plaza y un parque.","sub":"in mijn buurt zijn een plein en een park","tag":"barrio"},
  {"text":"Para ir a la plaza, sigue recto y gira a la derecha.","sub":"ga rechtdoor en sla rechts af","tag":"ruta"},
  {"text":"¿El supermercado? Lo tengo cerca.","sub":"de supermarkt? die heb ik dichtbij","tag":"od"},
  {"text":"Me gusta mi barrio porque es tranquilo.","sub":"ik hou van mijn buurt want het is rustig","tag":"opinion"}]}})

# 12 · SPEAK voicemessage — describe y da direcciones (3 items)
w({"id":PRE+"mensaje-barrio","title":"Mensaje de voz: mi barrio","subtitle":"U2 · neem een spraakbericht op",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz (30–40 s)","items":[
  {"text":"Describe tu habitación: qué hay y dónde está (usa 4 preposiciones).","cue":"mi habitación","tag":"prep",
   "sub":"gebruik: hay · está · encima de · al lado de · debajo de · entre",
   "tip":"4 preposiciones + hay/está? Neem opnieuw op."},
  {"text":"Da direcciones de tu casa a un lugar del barrio.","cue":"cómo llegar","tag":"ruta",
   "sub":"gebruik: sigue recto · gira a la derecha/izquierda · cruza · está a … minutos",
   "tip":"3 stappen + afstand? Herneem."},
  {"text":"Di qué está haciendo tu familia ahora mismo (3 personas).","cue":"estar + gerundio","tag":"ger",
   "sub":"gebruik: está cocinando · están viendo la tele · estoy …",
   "tip":"3 personen met estar+gerundio? Herneem."}]}})

print("\n12 C6+·U2-spellen geschreven (8 templates: memory·match·classify·cloze·tetris·order·point·speak).")
