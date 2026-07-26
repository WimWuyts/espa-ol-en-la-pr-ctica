#!/usr/bin/env python3
# Genereert de motor-content-JSON's voor C5 · U5 «¡Ñam!» (parada México/CDMX).
# Templates: memory·match·classify·cloze·tetris·order·point·sim·speak (receptief -> productief -> hablar).
# Werkwoordsvormen (ir a + infinitivo, presente) nagerekend/geverifieerd. Speak = échte opname (MediaRecorder, offline).
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2))
    print("wrote", os.path.basename(p))

G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0"}

# ============================ ① RECONOCER · woordenschat ============================
# 1 · MEMORY — comida ES ↔ NL
w({"id":"es-u5-comida-memoria","title":"Memoria de la comida","subtitle":"U5 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om en zoek het woord + de vertaling","pairs":[
  {"a":"el pan","b":"brood"},{"a":"el queso","b":"kaas"},{"a":"la carne","b":"vlees"},
  {"a":"el pollo","b":"kip"},{"a":"el pescado","b":"vis"},{"a":"el arroz","b":"rijst"},
  {"a":"la sopa","b":"soep"},{"a":"el bocadillo","b":"broodje"},{"a":"el jamón","b":"ham"},
  {"a":"los huevos","b":"eieren"},{"a":"el taco","b":"de taco"},{"a":"el guacamole","b":"guacamole"}]}})

# 2 · MEMORY — fruta/verdura ES ↔ NL
w({"id":"es-u5-fruta-verdura-memoria","title":"Fruta y verdura","subtitle":"U5 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: woord + vertaling","pairs":[
  {"a":"la manzana","b":"appel"},{"a":"el plátano","b":"banaan"},{"a":"la naranja","b":"sinaasappel"},
  {"a":"las uvas","b":"druiven"},{"a":"la piña","b":"ananas"},{"a":"el tomate","b":"tomaat"},
  {"a":"la lechuga","b":"sla"},{"a":"la cebolla","b":"ui"},{"a":"el ajo","b":"knoflook"},
  {"a":"el maíz","b":"maïs"}]}})

# 3 · MATCH — plato ↔ país
w({"id":"es-u5-plato-pais","title":"Plato y país","subtitle":"U5 · koppel het typische gerecht aan het land",
 "lang":"es","template":"match","options":{"chunk":5,"audio":False},
 "match":{"prompt":"Verbind het gerecht met het land","pairs":[
  {"a":"los tacos","b":"México 🇲🇽"},{"a":"la paella","b":"España 🇪🇸"},
  {"a":"la arepa","b":"Colombia 🇨🇴"},{"a":"el ceviche","b":"Perú 🇵🇪"},
  {"a":"las empanadas","b":"Argentina 🇦🇷"},{"a":"los churros","b":"España 🇪🇸"},
  {"a":"el guacamole","b":"México 🇲🇽"},{"a":"el gazpacho","b":"España 🇪🇸"}]}})

# ============================ ② DISTINGUIR · gramática/léxico ============================
# 4 · CLASSIFY — ¿comida o bebida?
w({"id":"es-u5-comida-bebida","title":"¿comida o bebida?","subtitle":"U5 · eten of drinken?",
 "lang":"es","template":"classify","options":{"rounds":14,"audio":False},
 "classify":{"prompt":"Is het comida (eten) of bebida (drinken)?","categories":[
  {"id":"comida","label":"comida<br><small>eten</small>","glaze":G["green"]},
  {"id":"bebida","label":"bebida<br><small>drinken</small>","glaze":G["blue"]}],
 "items":[
  {"stimulus":"el pan","answer":"comida","tag":"comida","sub":"brood"},
  {"stimulus":"el agua","answer":"bebida","tag":"bebida","sub":"water"},
  {"stimulus":"el pollo","answer":"comida","tag":"comida","sub":"kip"},
  {"stimulus":"el zumo","answer":"bebida","tag":"bebida","sub":"sap"},
  {"stimulus":"la manzana","answer":"comida","tag":"comida","sub":"appel"},
  {"stimulus":"el café","answer":"bebida","tag":"bebida","sub":"koffie"},
  {"stimulus":"la sopa","answer":"comida","tag":"comida","sub":"soep"},
  {"stimulus":"el refresco","answer":"bebida","tag":"bebida","sub":"frisdrank"},
  {"stimulus":"el queso","answer":"comida","tag":"comida","sub":"kaas"},
  {"stimulus":"la leche","answer":"bebida","tag":"bebida","sub":"melk"},
  {"stimulus":"los tacos","answer":"comida","tag":"comida","sub":"taco's"},
  {"stimulus":"el té","answer":"bebida","tag":"bebida","sub":"thee"},
  {"stimulus":"el arroz","answer":"comida","tag":"comida","sub":"rijst"},
  {"stimulus":"la naranja","answer":"comida","tag":"comida","sub":"fruit → eten"}]}})

# 5 · CLASSIFY — mucho/mucha/muchos/muchas
w({"id":"es-u5-cantidad","title":"¿mucho, mucha, muchos o muchas?","subtitle":"U5 · concordantie van cantidad",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Welke vorm past bij het woord? (m/v · ev/mv)","categories":[
  {"id":"mucho","label":"mucho<br><small>m. ev.</small>","glaze":G["blue"]},
  {"id":"mucha","label":"mucha<br><small>v. ev.</small>","glaze":G["red"]},
  {"id":"muchos","label":"muchos<br><small>m. mv.</small>","glaze":G["green"]},
  {"id":"muchas","label":"muchas<br><small>v. mv.</small>","glaze":G["amber"]}],
 "items":[
  {"stimulus":"___ pan","answer":"mucho","tag":"mucho","sub":"el pan (m)"},
  {"stimulus":"___ fruta","answer":"mucha","tag":"mucha","sub":"la fruta (f)"},
  {"stimulus":"___ tomates","answer":"muchos","tag":"muchos","sub":"los tomates (m pl)"},
  {"stimulus":"___ manzanas","answer":"muchas","tag":"muchas","sub":"las manzanas (f pl)"},
  {"stimulus":"___ arroz","answer":"mucho","tag":"mucho","sub":"el arroz (m)"},
  {"stimulus":"___ leche","answer":"mucha","tag":"mucha","sub":"la leche (f)"},
  {"stimulus":"___ huevos","answer":"muchos","tag":"muchos","sub":"los huevos (m pl)"},
  {"stimulus":"___ uvas","answer":"muchas","tag":"muchas","sub":"las uvas (f pl)"},
  {"stimulus":"___ queso","answer":"mucho","tag":"mucho","sub":"el queso (m)"},
  {"stimulus":"___ agua","answer":"mucha","tag":"mucha","sub":"el agua (f: mucha agua)"},
  {"stimulus":"___ churros","answer":"muchos","tag":"muchos","sub":"los churros (m pl)"},
  {"stimulus":"___ gambas","answer":"muchas","tag":"muchas","sub":"las gambas (f pl)"}]}})

# 6 · CLASSIFY — ¿camarero o cliente?
w({"id":"es-u5-camarero-cliente","title":"¿camarero o cliente?","subtitle":"U5 · wie zegt het in het restaurant?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Wie zegt deze zin: de ober of de klant?","categories":[
  {"id":"camarero","label":"el camarero<br><small>de ober</small>","glaze":G["amber"]},
  {"id":"cliente","label":"el cliente<br><small>de klant</small>","glaze":G["teal"]}],
 "items":[
  {"stimulus":"¿Qué va a tomar?","answer":"camarero","tag":"camarero","sub":"ober vraagt"},
  {"stimulus":"Para mí, una sopa.","answer":"cliente","tag":"cliente","sub":"klant bestelt"},
  {"stimulus":"¿Y para beber?","answer":"camarero","tag":"camarero","sub":"ober vraagt"},
  {"stimulus":"¿Me pone un refresco?","answer":"cliente","tag":"cliente","sub":"klant bestelt"},
  {"stimulus":"¡Que aproveche!","answer":"camarero","tag":"camarero","sub":"ober wenst"},
  {"stimulus":"La cuenta, por favor.","answer":"cliente","tag":"cliente","sub":"klant vraagt"},
  {"stimulus":"¿Algo de postre?","answer":"camarero","tag":"camarero","sub":"ober vraagt"},
  {"stimulus":"De segundo, pollo.","answer":"cliente","tag":"cliente","sub":"klant bestelt"},
  {"stimulus":"Enseguida se lo traigo.","answer":"camarero","tag":"camarero","sub":"ober antwoordt"},
  {"stimulus":"¿Me trae pan, por favor?","answer":"cliente","tag":"cliente","sub":"klant vraagt"},
  {"stimulus":"¿Van a tomar entrante?","answer":"camarero","tag":"camarero","sub":"ober vraagt"},
  {"stimulus":"Para mí, un agua sin gas.","answer":"cliente","tag":"cliente","sub":"klant bestelt"}]}})

# ============================ ③ PRODUCIR CON APOYO ============================
# 7 · CLOZE — ir a + infinitivo (VERPLICHT werkwoord-cloze, nagerekend)
w({"id":"es-u5-voy-a","title":"Completa: ir a + infinitivo","subtitle":"U5 · el futuro próximo (voy a comer…)",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm van «ir a»","items":[
  {"stimulus":"(Yo) ___ comer un taco.","options":["voy a","va a","vas a"],"answer":"voy a","tag":"ir","sub":"yo → voy a"},
  {"stimulus":"¿(Tú) ___ tomar un café?","options":["vas a","voy a","van a"],"answer":"vas a","tag":"ir","sub":"tú → vas a"},
  {"stimulus":"(Nosotros) ___ pedir la cuenta.","options":["vamos a","van a","vais a"],"answer":"vamos a","tag":"ir","sub":"nosotros → vamos a"},
  {"stimulus":"Diego ___ probar el ceviche.","options":["va a","vas a","voy a"],"answer":"va a","tag":"ir","sub":"él → va a"},
  {"stimulus":"(Ellos) ___ reservar una mesa.","options":["van a","vamos a","va a"],"answer":"van a","tag":"ir","sub":"ellos → van a"},
  {"stimulus":"(Yo) no ___ beber refresco.","options":["voy a","va a","vais a"],"answer":"voy a","tag":"ir","sub":"yo → voy a"},
  {"stimulus":"¿(Vosotros) ___ cenar en casa?","options":["vais a","van a","vamos a"],"answer":"vais a","tag":"ir","sub":"vosotros → vais a"},
  {"stimulus":"Lucía ___ preparar una tortilla.","options":["va a","van a","vas a"],"answer":"va a","tag":"ir","sub":"ella → va a"},
  {"stimulus":"(Nosotros) ___ comprar fruta.","options":["vamos a","voy a","vais a"],"answer":"vamos a","tag":"ir","sub":"nosotros → vamos a"},
  {"stimulus":"¿Qué ___ tomar tú?","options":["vas a","va a","voy a"],"answer":"vas a","tag":"ir","sub":"tú → vas a"},
  {"stimulus":"Los niños ___ comer churros.","options":["van a","va a","vamos a"],"answer":"van a","tag":"ir","sub":"ellos → van a"},
  {"stimulus":"(Yo) ___ probar el guacamole.","options":["voy a","vas a","va a"],"answer":"voy a","tag":"ir","sub":"yo → voy a"}]}})

# 8 · CLOZE — cantidad (un kilo de / un poco de / una botella de)
w({"id":"es-u5-cantidad-cloze","title":"Completa la cantidad","subtitle":"U5 · un kilo de · un poco de · una botella de",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies de juiste cantidad","items":[
  {"stimulus":"___ agua, por favor.","options":["una botella de","un kilo de","un poco de"],"answer":"una botella de","tag":"c","sub":"vloeistof → botella"},
  {"stimulus":"___ tomates para la salsa.","options":["un kilo de","una botella de","un poco de"],"answer":"un kilo de","tag":"c","sub":"fruta/verdura → kilo"},
  {"stimulus":"Solo ___ queso, gracias.","options":["un poco de","un kilo de","una botella de"],"answer":"un poco de","tag":"c","sub":"niet-telbaar → un poco de"},
  {"stimulus":"___ arroz para la paella.","options":["un paquete de","una botella de","un poco de"],"answer":"un paquete de","tag":"c","sub":"droog → paquete"},
  {"stimulus":"___ leche para el café.","options":["un poco de","un kilo de","un paquete de"],"answer":"un poco de","tag":"c","sub":"niet-telbaar"},
  {"stimulus":"___ manzanas, por favor.","options":["un kilo de","una botella de","un poco de"],"answer":"un kilo de","tag":"c","sub":"fruta → kilo"},
  {"stimulus":"___ refresco bien frío.","options":["una botella de","un kilo de","un poco de"],"answer":"una botella de","tag":"c","sub":"vloeistof → botella"},
  {"stimulus":"Hay ___ pan en la mesa.","options":["mucho","mucha","muchas"],"answer":"mucho","tag":"c","sub":"el pan (m)"},
  {"stimulus":"Hay ___ fruta en el mercado.","options":["mucha","mucho","muchos"],"answer":"mucha","tag":"c","sub":"la fruta (f)"},
  {"stimulus":"Compro ___ huevos.","options":["muchos","muchas","mucho"],"answer":"muchos","tag":"c","sub":"los huevos (m pl)"}]}})

# 9 · CLOZE — lo/la/los/las
w({"id":"es-u5-pronombre-cloze","title":"¿lo, la, los o las?","subtitle":"U5 · vervang het voorwerp (la cuenta → la traigo)",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies het juiste pronomen (lo/la/los/las)","items":[
  {"stimulus":"¿La cuenta? —Sí, ___ traigo.","options":["la","lo","las"],"answer":"la","tag":"od","sub":"la cuenta (f ev)"},
  {"stimulus":"¿El pan? —___ traigo ahora.","options":["Lo","La","Los"],"answer":"Lo","tag":"od","sub":"el pan (m ev)"},
  {"stimulus":"¿Los tacos? —Sí, ___ quiero.","options":["los","las","lo"],"answer":"los","tag":"od","sub":"los tacos (m pl)"},
  {"stimulus":"¿Las gambas? —___ pido.","options":["Las","Los","La"],"answer":"Las","tag":"od","sub":"las gambas (f pl)"},
  {"stimulus":"¿La carta? —Ahora ___ traigo.","options":["la","lo","las"],"answer":"la","tag":"od","sub":"la carta (f ev)"},
  {"stimulus":"¿El postre? —Sí, ___ quiero.","options":["lo","la","los"],"answer":"lo","tag":"od","sub":"el postre (m ev)"},
  {"stimulus":"¿Los refrescos? —___ traigo.","options":["Los","Las","Lo"],"answer":"Los","tag":"od","sub":"los refrescos (m pl)"},
  {"stimulus":"¿La sopa? —___ pido de primero.","options":["La","Lo","Las"],"answer":"La","tag":"od","sub":"la sopa (f ev)"},
  {"stimulus":"¿El café? —___ tomo con leche.","options":["Lo","La","Los"],"answer":"Lo","tag":"od","sub":"el café (m ev)"},
  {"stimulus":"¿Las manzanas? —___ como de postre.","options":["Las","Los","La"],"answer":"Las","tag":"od","sub":"las manzanas (f pl)"}]}})

# 10 · TETRIS — cantidades (concordantie, valt in de juiste kolom)
w({"id":"es-u5-cantidad-tetris","title":"Cantidades Tetris","subtitle":"U5 · laat elk woord in de juiste vorm van «mucho» vallen",
 "lang":"es","template":"tetris","options":{"rows":9,"speed":1300,"audio":False},
 "classify":{"categories":[
  {"id":"mucho","label":"mucho","glaze":G["blue"]},{"id":"mucha","label":"mucha","glaze":G["red"]},
  {"id":"muchos","label":"muchos","glaze":G["green"]},{"id":"muchas","label":"muchas","glaze":G["amber"]}],
 "items":[
  {"stimulus":"pan","answer":"mucho","tag":"mucho","sub":"el pan"},
  {"stimulus":"fruta","answer":"mucha","tag":"mucha","sub":"la fruta"},
  {"stimulus":"tomates","answer":"muchos","tag":"muchos","sub":"los tomates"},
  {"stimulus":"manzanas","answer":"muchas","tag":"muchas","sub":"las manzanas"},
  {"stimulus":"arroz","answer":"mucho","tag":"mucho","sub":"el arroz"},
  {"stimulus":"leche","answer":"mucha","tag":"mucha","sub":"la leche"},
  {"stimulus":"huevos","answer":"muchos","tag":"muchos","sub":"los huevos"},
  {"stimulus":"uvas","answer":"muchas","tag":"muchas","sub":"las uvas"},
  {"stimulus":"queso","answer":"mucho","tag":"mucho","sub":"el queso"},
  {"stimulus":"churros","answer":"muchos","tag":"muchos","sub":"los churros"},
  {"stimulus":"gambas","answer":"muchas","tag":"muchas","sub":"las gambas"},
  {"stimulus":"pescado","answer":"mucho","tag":"mucho","sub":"el pescado"}]}})

# 11 · ORDER — ordena el diálogo del restaurante
w({"id":"es-u5-orden-restaurante","title":"Ordena el diálogo","subtitle":"U5 · zet de bestel-dialoog in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik de zinnen in de logische volgorde van een restaurantbezoek","rounds":[
  {"tag":"pedir","sub":"begroeten → bestellen → beber → cuenta","items":[
    {"label":"Buenas tardes, ¿qué va a tomar?","key":1},{"label":"Para mí, de segundo, pollo.","key":2},
    {"label":"¿Y para beber?","key":3},{"label":"¿Me pone agua? Y la cuenta, por favor.","key":4}]},
  {"tag":"pedir","sub":"entrante → fuerte → postre → cuenta","items":[
    {"label":"De entrante, guacamole con nachos.","key":1},{"label":"De plato fuerte, tacos de pollo.","key":2},
    {"label":"De postre, flan.","key":3},{"label":"¡Que aproveche! ... La cuenta, por favor.","key":4}]},
  {"tag":"pedir","sub":"reservar → llegar → pedir → pagar","items":[
    {"label":"Quiero reservar una mesa para dos.","key":1},{"label":"Buenas, tenemos una reserva.","key":2},
    {"label":"Para mí, una sopa y pescado.","key":3},{"label":"La cuenta, por favor. Aquí tiene la propina.","key":4}]},
  {"tag":"receta","sub":"receta: primero → luego → después → por último","items":[
    {"label":"Primero, abre el aguacate.","key":1},{"label":"Luego, añade el tomate y la cebolla.","key":2},
    {"label":"Después, exprime la lima.","key":3},{"label":"Por último, ¡que aproveche!","key":4}]}]}})

# ============================ ④ ANALIZAR & COMUNICAR ============================
# 12 · POINT — señala en el mercado
w({"id":"es-u5-senala-mercado","title":"Señala en el mercado","subtitle":"U5 · klik het juiste producto",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het gevraagde product","mode":"one","rounds":[
  {"tag":"fruta","sub":"señala la fruta","targets":[
    {"label":"el tomate"},{"label":"la manzana","hit":True},{"label":"el pan"},{"label":"el queso"}]},
  {"tag":"verdura","sub":"señala la verdura","targets":[
    {"label":"la naranja"},{"label":"el pollo"},{"label":"la lechuga","hit":True},{"label":"el café"}]},
  {"tag":"bebida","sub":"señala la bebida","targets":[
    {"label":"el arroz"},{"label":"el zumo","hit":True},{"label":"la carne"},{"label":"la pasta"}]},
  {"tag":"mesa","sub":"señala el cubierto (bestek)","targets":[
    {"label":"el tenedor","hit":True},{"label":"la sopa"},{"label":"la fruta"},{"label":"el taco"}]},
  {"tag":"mexico","sub":"señala el plato mexicano","targets":[
    {"label":"la paella"},{"label":"el guacamole","hit":True},{"label":"los churros"},{"label":"el gazpacho"}]}]}})

# 13 · SIM — ¡Pide en el restaurante! (productie met bouwsteen-check)
w({"id":"es-u5-pide","title":"¡Pide en el restaurante!","subtitle":"U5 · schrijf je bestelling — met alle bouwstenen",
 "lang":"es","template":"sim","options":{"audio":False},
 "sim":{"prompt":"Tarea comunicativa · pedir en el restaurante","rounds":[
  {"scenario":"El camarero dice: «¿Qué va a tomar?» — pide de primero y de segundo.","tag":"pedir","sub":"gebruik: para mí · de primero · de segundo","min":10,
   "need":[{"re":"para mí","label":"para mí …"},{"re":"de primero","label":"de primero …"},{"re":"de segundo","label":"de segundo …"}],
   "bank":["Para mí","de primero","de segundo","una sopa","pollo","por favor","¿me pone","de postre"],
   "model":"Para mí, de primero una sopa y de segundo pollo, por favor."},
  {"scenario":"Pide agua y la cuenta con cortesía.","tag":"pedir","sub":"gebruik: ¿me pone…? / ¿me trae…? / la cuenta","min":8,
   "need":[{"re":"me pone|me trae","label":"¿me pone/trae…?"},{"re":"agua|refresco","label":"una bebida"},{"re":"cuenta","label":"la cuenta"}],
   "bank":["¿Me pone","¿Me trae","una botella de agua","por favor","la cuenta","gracias"],
   "model":"¿Me pone una botella de agua, por favor? Y la cuenta, por favor."},
  {"scenario":"Di qué vas a comer y beber hoy (ir a + infinitivo).","tag":"planes","sub":"gebruik: voy a + infinitivo","min":8,
   "need":[{"re":"voy a","label":"voy a + infinitivo"},{"re":"comer|tomar|probar|beber","label":"un verbo (comer/tomar…)"},{"re":"taco|pollo|fruta|refresco|guacamole","label":"comida/bebida"}],
   "bank":["Voy a","comer","tomar","probar","un taco","guacamole","un refresco","fruta"],
   "model":"Hoy voy a comer un taco y voy a probar el guacamole."}]}})

# ============================ ⑤ HABLAR · grábate 🎙️ ============================
# 14 · SPEAK repeat — escucha y repite: la comida
w({"id":"es-u5-repite-comida","title":"Escucha y repite: la comida","subtitle":"U5 · escucha el modelo, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite en voz alta · grábate ⏺","items":[
  {"text":"Para mí, una sopa, por favor.","sub":"voor mij, een soep","tag":"pedir","tip":"¡Bien! Ahora dilo sin leer. <span class='nl'>zeg het nu zonder te lezen.</span>"},
  {"text":"¿Me pone una botella de agua?","sub":"mag ik een fles water? — cortesía","tag":"pedir"},
  {"text":"Voy a comer un taco.","sub":"ik ga een taco eten — ir a + infinitivo","tag":"futuro"},
  {"text":"La cuenta, por favor.","sub":"de rekening, alstublieft","tag":"pedir"},
  {"text":"¡Que aproveche!","sub":"eet smakelijk!","tag":"cortesia"}]}})

# 15 · SPEAK shadowing — con Diego (afbouwende fasen)
w({"id":"es-u5-shadowing-diego","title":"Shadowing con Diego","subtitle":"U5 · praat mee met Diego, steeds minder tekst",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"shadowing","prompt":"Escucha ▶ · habla al mismo tiempo · grábate ⏺","phases":["Texto completo","Palabras clave","Sin texto","Tu versión"],"items":[
  {"text":"En el mercado hay mucha fruta y muchas verduras.","sub":"op de markt is veel fruit en veel groenten","tag":"mercado"},
  {"text":"Voy a comprar un kilo de tomates y un poco de queso.","sub":"ik ga een kilo tomaten en een beetje kaas kopen","tag":"cantidad"},
  {"text":"Hoy vamos a comer tacos y guacamole.","sub":"vandaag gaan we taco's en guacamole eten","tag":"futuro"},
  {"text":"¿Vas a probar el ceviche conmigo?","sub":"ga jij de ceviche met mij proeven?","tag":"futuro","tip":"Ahora invita a un amigo de verdad. <span class='nl'>nodig nu een echte vriend uit.</span>"}]}})

# 16 · SPEAK voicemessage — pide comida (mensaje de voz)
w({"id":"es-u5-mensaje-pedido","title":"Mensaje de voz: pide comida","subtitle":"U5 · neem één spraakbericht op met je pedido",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz (30 s)","items":[
  {"text":"Pide comida para una fiesta (¿qué vas a comprar? ¿cuánta cantidad?).","cue":"para · la fiesta","tag":"pedir",
   "sub":"gebruik: voy a comprar · un kilo de · una botella de · un poco de",
   "tip":"Heb je 3 productos + cantidad gezegd? Neem opnieuw op. <span class='nl'>3 producten + hoeveelheid? herneem.</span>"}]}})

# 17 · SPEAK repeat — describe tu plato favorito
w({"id":"es-u5-describe-plato","title":"Describe tu plato","subtitle":"U5 · beschrijf je lievelingsgerecht, grábate",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · describe tu plato · grábate ⏺","items":[
  {"cue":"Modelo · Diego 🇲🇽","text":"Mi plato favorito son los tacos.","sub":"mijn lievelingsgerecht zijn taco's","tag":"describir"},
  {"cue":"¿qué lleva?","text":"Llevan carne, verdura y salsa.","sub":"ze bevatten vlees, groente en saus","tag":"describir"},
  {"cue":"¿por qué?","text":"Me encantan porque están muy ricos.","sub":"ik ben er dol op want ze zijn heel lekker","tag":"describir"},
  {"cue":"tu versión","text":"Mi plato favorito es ___ . Lleva ___ .","sub":"jouw versie — vul in en zeg ze","tag":"describir",
   "tip":"Ahora describe el plato de un amigo. <span class='nl'>beschrijf nu het gerecht van een vriend(in).</span>"}]}})

print("\n17 U5-spellen geschreven (10 templates: memory·match·classify·cloze·tetris·order·point·sim·speak).")
