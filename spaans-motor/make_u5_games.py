#!/usr/bin/env python3
# Genereert de motor-content-JSON's voor C5 · U5 «¡Ñam!» (parada México/CDMX).
# Templates: memory·match·classify·cloze·tetris·order·point·sim·speak (receptief -> productief -> hablar).
# VERRIJKT (2026-07-26): elke game heeft een POOL van >=12 items; options.rounds staat lager (~8-12)
#   zodat elke herspeling een ANDERE reeks trekt (variatie / herspeelwaarde).
# Werkwoordsvormen (ir a + infinitivo, presente, imperativo tú) nagerekend/geverifieerd.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2))
    print("wrote", os.path.basename(p))

G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0"}

# ============================ ① RECONOCER · woordenschat ============================
# 1 · MEMORY — comida ES ↔ NL  (pool 14, 6 per bord)
w({"id":"es-u5-comida-memoria","title":"Memoria de la comida","subtitle":"U5 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om en zoek het woord + de vertaling","pairs":[
  {"a":"el pan","b":"brood"},{"a":"el queso","b":"kaas"},{"a":"la carne","b":"vlees"},
  {"a":"el pollo","b":"kip"},{"a":"el pescado","b":"vis"},{"a":"el arroz","b":"rijst"},
  {"a":"la sopa","b":"soep"},{"a":"el bocadillo","b":"broodje"},{"a":"el jamón","b":"ham"},
  {"a":"los huevos","b":"eieren"},{"a":"el taco","b":"de taco"},{"a":"el guacamole","b":"guacamole"},
  {"a":"el flan","b":"pudding"},{"a":"la ensalada","b":"salade"}]}})

# 2 · MEMORY — fruta/verdura ES ↔ NL  (pool 12)
w({"id":"es-u5-fruta-verdura-memoria","title":"Fruta y verdura","subtitle":"U5 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: woord + vertaling","pairs":[
  {"a":"la manzana","b":"appel"},{"a":"el plátano","b":"banaan"},{"a":"la naranja","b":"sinaasappel"},
  {"a":"las uvas","b":"druiven"},{"a":"la piña","b":"ananas"},{"a":"el tomate","b":"tomaat"},
  {"a":"la lechuga","b":"sla"},{"a":"la cebolla","b":"ui"},{"a":"el ajo","b":"knoflook"},
  {"a":"el maíz","b":"maïs"},{"a":"la fresa","b":"aardbei"},{"a":"la zanahoria","b":"wortel"}]}})

# 3 · MATCH — plato ↔ país  (pool 12, blokjes van 6)
w({"id":"es-u5-plato-pais","title":"Plato y país","subtitle":"U5 · koppel het typische gerecht aan het land",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind het gerecht met het land","pairs":[
  {"a":"los tacos","b":"México 🇲🇽"},{"a":"la paella","b":"España 🇪🇸"},
  {"a":"la arepa","b":"Colombia 🇨🇴"},{"a":"el ceviche","b":"Perú 🇵🇪"},
  {"a":"las empanadas","b":"Argentina 🇦🇷"},{"a":"los churros","b":"España 🇪🇸"},
  {"a":"el guacamole","b":"México 🇲🇽"},{"a":"el gazpacho","b":"España 🇪🇸"},
  {"a":"el pozole","b":"México 🇲🇽"},{"a":"la bandeja paisa","b":"Colombia 🇨🇴"},
  {"a":"el asado","b":"Argentina 🇦🇷"},{"a":"el lomo saltado","b":"Perú 🇵🇪"}]}})

# 3b · MATCH (NIEUW) — plato ↔ ingrediente principal  (pool 12)
w({"id":"es-u5-plato-ingrediente","title":"Plato e ingrediente","subtitle":"U5 · welk hoofdingrediënt hoort bij het gerecht?",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind het gerecht met zijn belangrijkste ingrediënt","pairs":[
  {"a":"el guacamole","b":"el aguacate 🥑"},{"a":"la paella","b":"el arroz 🍚"},
  {"a":"los tacos","b":"la tortilla 🫓"},{"a":"el ceviche","b":"el pescado 🐟"},
  {"a":"la tortilla española","b":"los huevos 🥚"},{"a":"el gazpacho","b":"el tomate 🍅"},
  {"a":"las quesadillas","b":"el queso 🧀"},{"a":"la arepa","b":"el maíz 🌽"},
  {"a":"el bocadillo","b":"el pan 🥖"},{"a":"la ensalada","b":"la lechuga 🥬"},
  {"a":"los churros","b":"el chocolate 🍫"},{"a":"la limonada","b":"el limón 🍋"}]}})

# ============================ ② DISTINGUIR · gramática/léxico ============================
# 4 · CLASSIFY — ¿comida o bebida?  (pool 20, rounds 12)
w({"id":"es-u5-comida-bebida","title":"¿comida o bebida?","subtitle":"U5 · eten of drinken?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
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
  {"stimulus":"la naranja","answer":"comida","tag":"comida","sub":"fruit → eten"},
  {"stimulus":"el jamón","answer":"comida","tag":"comida","sub":"ham"},
  {"stimulus":"la horchata","answer":"bebida","tag":"bebida","sub":"horchata (drank)"},
  {"stimulus":"el flan","answer":"comida","tag":"comida","sub":"pudding → postre"},
  {"stimulus":"el batido","answer":"bebida","tag":"bebida","sub":"milkshake"},
  {"stimulus":"la ensalada","answer":"comida","tag":"comida","sub":"salade"},
  {"stimulus":"la limonada","answer":"bebida","tag":"bebida","sub":"limonade"}]}})

# 5 · CLASSIFY — mucho/mucha/muchos/muchas  (pool 20, rounds 12)
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
  {"stimulus":"___ gambas","answer":"muchas","tag":"muchas","sub":"las gambas (f pl)"},
  {"stimulus":"___ pescado","answer":"mucho","tag":"mucho","sub":"el pescado (m)"},
  {"stimulus":"___ carne","answer":"mucha","tag":"mucha","sub":"la carne (f)"},
  {"stimulus":"___ tacos","answer":"muchos","tag":"muchos","sub":"los tacos (m pl)"},
  {"stimulus":"___ verduras","answer":"muchas","tag":"muchas","sub":"las verduras (f pl)"},
  {"stimulus":"___ café","answer":"mucho","tag":"mucho","sub":"el café (m)"},
  {"stimulus":"___ sal","answer":"mucha","tag":"mucha","sub":"la sal (f)"},
  {"stimulus":"___ frijoles","answer":"muchos","tag":"muchos","sub":"los frijoles (m pl)"},
  {"stimulus":"___ naranjas","answer":"muchas","tag":"muchas","sub":"las naranjas (f pl)"}]}})

# 6 · CLASSIFY — ¿camarero o cliente?  (pool 18, rounds 10)
w({"id":"es-u5-camarero-cliente","title":"¿camarero o cliente?","subtitle":"U5 · wie zegt het in het restaurant?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
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
  {"stimulus":"Para mí, un agua sin gas.","answer":"cliente","tag":"cliente","sub":"klant bestelt"},
  {"stimulus":"Aquí tiene la carta.","answer":"camarero","tag":"camarero","sub":"ober geeft"},
  {"stimulus":"¿Qué me recomienda?","answer":"cliente","tag":"cliente","sub":"klant vraagt raad"},
  {"stimulus":"¿Tienen menú del día?","answer":"cliente","tag":"cliente","sub":"klant vraagt"},
  {"stimulus":"¿Está todo bien?","answer":"camarero","tag":"camarero","sub":"ober checkt"},
  {"stimulus":"¿Puedo pagar con tarjeta?","answer":"cliente","tag":"cliente","sub":"klant vraagt"},
  {"stimulus":"¿Van a pagar juntos?","answer":"camarero","tag":"camarero","sub":"ober vraagt"}]}})

# 6b · CLASSIFY (NIEUW) — en el mercado: ¿fruta, verdura o carne/pescado?  (pool 18, rounds 12)
w({"id":"es-u5-en-el-mercado","title":"En el mercado","subtitle":"U5 · sorteer het product: fruta · verdura · carne/pescado",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"¿Qué es? fruta · verdura · carne o pescado","categories":[
  {"id":"fruta","label":"fruta<br><small>fruit</small>","glaze":G["red"]},
  {"id":"verdura","label":"verdura<br><small>groente</small>","glaze":G["green"]},
  {"id":"proteina","label":"carne / pescado<br><small>vlees/vis</small>","glaze":G["amber"]}],
 "items":[
  {"stimulus":"la manzana","answer":"fruta","tag":"fruta","sub":"appel"},
  {"stimulus":"el plátano","answer":"fruta","tag":"fruta","sub":"banaan"},
  {"stimulus":"la naranja","answer":"fruta","tag":"fruta","sub":"sinaasappel"},
  {"stimulus":"las uvas","answer":"fruta","tag":"fruta","sub":"druiven"},
  {"stimulus":"la piña","answer":"fruta","tag":"fruta","sub":"ananas"},
  {"stimulus":"la fresa","answer":"fruta","tag":"fruta","sub":"aardbei"},
  {"stimulus":"el tomate","answer":"verdura","tag":"verdura","sub":"tomaat (culinair verdura)"},
  {"stimulus":"la lechuga","answer":"verdura","tag":"verdura","sub":"sla"},
  {"stimulus":"la cebolla","answer":"verdura","tag":"verdura","sub":"ui"},
  {"stimulus":"el ajo","answer":"verdura","tag":"verdura","sub":"knoflook"},
  {"stimulus":"el maíz","answer":"verdura","tag":"verdura","sub":"maïs"},
  {"stimulus":"la zanahoria","answer":"verdura","tag":"verdura","sub":"wortel"},
  {"stimulus":"el pollo","answer":"proteina","tag":"proteina","sub":"kip"},
  {"stimulus":"la carne","answer":"proteina","tag":"proteina","sub":"vlees"},
  {"stimulus":"el pescado","answer":"proteina","tag":"proteina","sub":"vis"},
  {"stimulus":"el jamón","answer":"proteina","tag":"proteina","sub":"ham"},
  {"stimulus":"las gambas","answer":"proteina","tag":"proteina","sub":"garnalen"},
  {"stimulus":"el chorizo","answer":"proteina","tag":"proteina","sub":"chorizo (worst)"}]}})

# ============================ ③ PRODUCIR CON APOYO ============================
# 7 · CLOZE — ir a + infinitivo (VERPLICHT werkwoord-cloze, nagerekend)  (pool 18, rounds 12)
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
  {"stimulus":"(Yo) ___ probar el guacamole.","options":["voy a","vas a","va a"],"answer":"voy a","tag":"ir","sub":"yo → voy a"},
  {"stimulus":"Este finde (nosotros) ___ visitar un mercado.","options":["vamos a","van a","voy a"],"answer":"vamos a","tag":"ir","sub":"nosotros → vamos a"},
  {"stimulus":"¿(Vosotros) ___ probar la comida picante?","options":["vais a","van a","vamos a"],"answer":"vais a","tag":"ir","sub":"vosotros → vais a"},
  {"stimulus":"Mañana (yo) ___ cocinar una paella.","options":["voy a","va a","vas a"],"answer":"voy a","tag":"ir","sub":"yo → voy a"},
  {"stimulus":"Valen y Nina ___ preparar arepas.","options":["van a","vamos a","vais a"],"answer":"van a","tag":"ir","sub":"ellas → van a"},
  {"stimulus":"¿(Tú) no ___ comer postre hoy?","options":["vas a","va a","voy a"],"answer":"vas a","tag":"ir","sub":"tú → vas a"},
  {"stimulus":"Él ___ pedir un agua sin gas.","options":["va a","van a","vas a"],"answer":"va a","tag":"ir","sub":"él → va a"}]}})

# 8 · CLOZE — cantidad (un kilo de / un poco de / una botella de / mucho…)  (pool 16, rounds 10)
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
  {"stimulus":"Compro ___ huevos.","options":["muchos","muchas","mucho"],"answer":"muchos","tag":"c","sub":"los huevos (m pl)"},
  {"stimulus":"Pon ___ sal en la sopa.","options":["un poco de","un kilo de","una botella de"],"answer":"un poco de","tag":"c","sub":"niet-telbaar → un poco de"},
  {"stimulus":"___ zumo de naranja, por favor.","options":["una botella de","un kilo de","un paquete de"],"answer":"una botella de","tag":"c","sub":"vloeistof → botella"},
  {"stimulus":"Quiero ___ uvas.","options":["un kilo de","una botella de","un poco de"],"answer":"un kilo de","tag":"c","sub":"fruta → kilo"},
  {"stimulus":"En el mercado hay ___ verduras.","options":["muchas","muchos","mucha"],"answer":"muchas","tag":"c","sub":"las verduras (f pl)"},
  {"stimulus":"Hoy hay ___ gente en el mercado.","options":["mucha","mucho","muchas"],"answer":"mucha","tag":"c","sub":"la gente (f)"},
  {"stimulus":"Necesito ___ harina para el pan.","options":["un poco de","un kilo de","una botella de"],"answer":"un poco de","tag":"c","sub":"niet-telbaar → un poco de"}]}})

# 9 · CLOZE — lo/la/los/las  (pool 16, rounds 10)
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
  {"stimulus":"¿Las manzanas? —___ como de postre.","options":["Las","Los","La"],"answer":"Las","tag":"od","sub":"las manzanas (f pl)"},
  {"stimulus":"¿El guacamole? —___ preparo yo.","options":["Lo","La","Los"],"answer":"Lo","tag":"od","sub":"el guacamole (m ev)"},
  {"stimulus":"¿La ensalada? —___ traigo enseguida.","options":["La","Lo","Las"],"answer":"La","tag":"od","sub":"la ensalada (f ev)"},
  {"stimulus":"¿Los churros? —___ compro en la calle.","options":["Los","Las","Lo"],"answer":"Los","tag":"od","sub":"los churros (m pl)"},
  {"stimulus":"¿Las bebidas? —___ pongo en la mesa.","options":["Las","Los","La"],"answer":"Las","tag":"od","sub":"las bebidas (f pl)"},
  {"stimulus":"¿El flan? —Sí, ___ quiero de postre.","options":["lo","la","los"],"answer":"lo","tag":"od","sub":"el flan (m ev)"},
  {"stimulus":"¿La propina? —___ dejo en la mesa.","options":["La","Lo","Las"],"answer":"La","tag":"od","sub":"la propina (f ev)"}]}})

# 10 · TETRIS — cantidades (concordantie, valt in de juiste kolom)  (pool 18)
w({"id":"es-u5-cantidad-tetris","title":"Cantidades: cinta","subtitle":"U5 · clasifica «mucho» en la cinta · sorteer op de band",
 "lang":"es","template":"belt","options":{"rounds":16,"audio":False},
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
  {"stimulus":"pescado","answer":"mucho","tag":"mucho","sub":"el pescado"},
  {"stimulus":"carne","answer":"mucha","tag":"mucha","sub":"la carne"},
  {"stimulus":"tacos","answer":"muchos","tag":"muchos","sub":"los tacos"},
  {"stimulus":"verduras","answer":"muchas","tag":"muchas","sub":"las verduras"},
  {"stimulus":"café","answer":"mucho","tag":"mucho","sub":"el café"},
  {"stimulus":"sal","answer":"mucha","tag":"mucha","sub":"la sal"},
  {"stimulus":"naranjas","answer":"muchas","tag":"muchas","sub":"las naranjas"}]}})

# 11 · ORDER — ordena el diálogo del restaurante  (8 rondes, geschud per speling)
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
  {"tag":"pedir","sub":"carta → recomendar → elegir → confirmar","items":[
    {"label":"¿Me trae la carta, por favor?","key":1},{"label":"¿Qué me recomienda?","key":2},
    {"label":"Entonces, para mí el ceviche.","key":3},{"label":"Muy bien, enseguida se lo traigo.","key":4}]},
  {"tag":"pedir","sub":"saludar → mesa → beber → comer","items":[
    {"label":"Buenas noches, ¿tienen mesa para tres?","key":1},{"label":"Sí, por aquí, por favor.","key":2},
    {"label":"De beber, tres refrescos.","key":3},{"label":"Y de comer, una paella para compartir.","key":4}]},
  {"tag":"pedir","sub":"pedir → esperar → servir → desear","items":[
    {"label":"Para mí, una sopa de tomate.","key":1},{"label":"Muy bien, ¿algo más?","key":2},
    {"label":"Aquí tiene su sopa.","key":3},{"label":"Gracias. ¡Que aproveche!","key":4}]},
  {"tag":"receta","sub":"receta guacamole: primero → luego → después → por último","items":[
    {"label":"Primero, corta el aguacate.","key":1},{"label":"Luego, añade el tomate y la cebolla.","key":2},
    {"label":"Después, exprime la lima.","key":3},{"label":"Por último, mezcla y añade sal.","key":4}]},
  {"tag":"receta","sub":"la comida del día: desayuno → comida → merienda → cena","items":[
    {"label":"Por la mañana: el desayuno.","key":1},{"label":"A las 14:00: la comida.","key":2},
    {"label":"Por la tarde: la merienda.","key":3},{"label":"Por la noche: la cena.","key":4}]}]}})

# 11b · ORDER (NIEUW) — ordena la receta (recepten stap voor stap)  (6 rondes)
w({"id":"es-u5-receta-order","title":"Ordena la receta","subtitle":"U5 · zet de bereidingsstappen in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik de stappen van het recept in de juiste volgorde","rounds":[
  {"tag":"tacos","sub":"los tacos 🌮","items":[
    {"label":"Calienta la tortilla.","key":1},{"label":"Pon la carne encima.","key":2},
    {"label":"Añade salsa y cebolla.","key":3},{"label":"Come el taco con las manos.","key":4}]},
  {"tag":"limonada","sub":"la limonada 🍋","items":[
    {"label":"Exprime los limones.","key":1},{"label":"Añade agua y azúcar.","key":2},
    {"label":"Mezcla bien.","key":3},{"label":"Sirve con hielo.","key":4}]},
  {"tag":"bocadillo","sub":"el bocadillo 🥖","items":[
    {"label":"Corta el pan.","key":1},{"label":"Pon el jamón y el queso.","key":2},
    {"label":"Añade tomate.","key":3},{"label":"Cierra el bocadillo.","key":4}]},
  {"tag":"cafe","sub":"el café con leche ☕","items":[
    {"label":"Calienta la leche.","key":1},{"label":"Prepara el café.","key":2},
    {"label":"Mezcla café y leche.","key":3},{"label":"Bebe caliente.","key":4}]},
  {"tag":"ensalada","sub":"la ensalada 🥗","items":[
    {"label":"Lava la lechuga.","key":1},{"label":"Corta el tomate y la cebolla.","key":2},
    {"label":"Añade aceite y sal.","key":3},{"label":"Mezcla todo.","key":4}]},
  {"tag":"quesadilla","sub":"la quesadilla 🫓","items":[
    {"label":"Pon queso en la tortilla.","key":1},{"label":"Dobla la tortilla.","key":2},
    {"label":"Calienta en la sartén.","key":3},{"label":"Corta y sirve.","key":4}]}]}})

# 12 · POINT — señala en el mercado  (10 rondes)
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
    {"label":"la paella"},{"label":"el guacamole","hit":True},{"label":"los churros"},{"label":"el gazpacho"}]},
  {"tag":"proteina","sub":"señala la carne o el pescado","targets":[
    {"label":"la manzana"},{"label":"el pollo","hit":True},{"label":"el pan"},{"label":"el zumo"}]},
  {"tag":"postre","sub":"señala el postre","targets":[
    {"label":"la sopa"},{"label":"el flan","hit":True},{"label":"la ensalada"},{"label":"el pescado"}]},
  {"tag":"pais","sub":"señala el país del ceviche","targets":[
    {"label":"México"},{"label":"Perú","hit":True},{"label":"España"},{"label":"Colombia"}]},
  {"tag":"bebida","sub":"señala la bebida caliente","targets":[
    {"label":"el café","hit":True},{"label":"el zumo"},{"label":"el agua"},{"label":"el refresco"}]},
  {"tag":"picante","sub":"señala lo que es picante","targets":[
    {"label":"el chile","hit":True},{"label":"el pan"},{"label":"la leche"},{"label":"el arroz"}]}]}})

# 12b · POINT (NIEUW) — pon la mesa (dek de tafel: bestek & servies)  (8 rondes)
w({"id":"es-u5-pon-la-mesa","title":"Pon la mesa","subtitle":"U5 · klik het juiste item van la mesa",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het gevraagde item van de tafel","mode":"one","rounds":[
  {"tag":"tenedor","sub":"señala el tenedor (vork)","targets":[
    {"label":"el tenedor 🍴","hit":True},{"label":"el vaso"},{"label":"el plato"},{"label":"la servilleta"}]},
  {"tag":"cuchillo","sub":"señala el cuchillo (mes)","targets":[
    {"label":"el cuchillo 🔪","hit":True},{"label":"la cuchara"},{"label":"la taza"},{"label":"el mantel"}]},
  {"tag":"cuchara","sub":"señala la cuchara (para la sopa)","targets":[
    {"label":"la cuchara 🥄","hit":True},{"label":"el tenedor"},{"label":"el vaso"},{"label":"el plato"}]},
  {"tag":"vaso","sub":"señala el vaso (para el agua)","targets":[
    {"label":"el vaso 🥛","hit":True},{"label":"el plato"},{"label":"el cuchillo"},{"label":"la servilleta"}]},
  {"tag":"servilleta","sub":"señala la servilleta (servet)","targets":[
    {"label":"la servilleta","hit":True},{"label":"el tenedor"},{"label":"la taza"},{"label":"el plato"}]},
  {"tag":"plato","sub":"señala el plato (bord)","targets":[
    {"label":"el plato 🍽️","hit":True},{"label":"el vaso"},{"label":"la cuchara"},{"label":"el mantel"}]},
  {"tag":"taza","sub":"señala la taza (para el café)","targets":[
    {"label":"la taza ☕","hit":True},{"label":"el vaso"},{"label":"el tenedor"},{"label":"el plato"}]},
  {"tag":"mantel","sub":"señala el mantel (tafelkleed)","targets":[
    {"label":"el mantel","hit":True},{"label":"la servilleta"},{"label":"el plato"},{"label":"el vaso"}]}]}})

# ============================ ④ ANALIZAR & COMUNICAR ============================
# 13 · SIM — ¡Pide en el restaurante! (productie met bouwsteen-check)  (6 rondes)
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
   "model":"Hoy voy a comer un taco y voy a probar el guacamole."},
  {"scenario":"Reserva una mesa para dos personas para esta noche.","tag":"reservar","sub":"gebruik: quiero reservar · una mesa · para","min":8,
   "need":[{"re":"reservar|reserva","label":"reservar"},{"re":"mesa","label":"una mesa"},{"re":"para","label":"para (dos / esta noche)"}],
   "bank":["Quiero reservar","una mesa","para dos personas","para esta noche","por favor","a las ocho"],
   "model":"Quiero reservar una mesa para dos personas para esta noche, por favor."},
  {"scenario":"Pregunta el precio de un plato y di cómo vas a pagar.","tag":"pagar","sub":"gebruik: ¿cuánto cuesta? · pagar · tarjeta","min":8,
   "need":[{"re":"cuánto|cuanto|precio","label":"¿cuánto…?"},{"re":"cuesta|es","label":"cuesta / es"},{"re":"pagar|tarjeta|efectivo","label":"pagar (tarjeta/efectivo)"}],
   "bank":["¿Cuánto cuesta","el ceviche","¿puedo pagar","con tarjeta","en efectivo","la cuenta"],
   "model":"¿Cuánto cuesta el ceviche? ¿Puedo pagar con tarjeta?"},
  {"scenario":"Recomienda tu plato favorito a un amigo y di por qué.","tag":"recomendar","sub":"gebruik: te recomiendo · porque · está rico","min":9,
   "need":[{"re":"recomiendo|recomienda","label":"te recomiendo"},{"re":"porque","label":"porque …"},{"re":"rico|bueno|delicioso|encanta","label":"está rico / me encanta"}],
   "bank":["Te recomiendo","los tacos","porque","están muy ricos","me encanta","el guacamole"],
   "model":"Te recomiendo los tacos porque están muy ricos."}]}})

# ============================ ⑤ HABLAR · grábate 🎙️ ============================
# 14 · SPEAK repeat — escucha y repite: la comida  (8 items)
w({"id":"es-u5-repite-comida","title":"Escucha y repite: la comida","subtitle":"U5 · escucha el modelo, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite en voz alta · grábate ⏺","items":[
  {"text":"Para mí, una sopa, por favor.","sub":"voor mij, een soep","tag":"pedir","tip":"¡Bien! Ahora dilo sin leer. <span class='nl'>zeg het nu zonder te lezen.</span>"},
  {"text":"¿Me pone una botella de agua?","sub":"mag ik een fles water? — cortesía","tag":"pedir"},
  {"text":"Voy a comer un taco.","sub":"ik ga een taco eten — ir a + infinitivo","tag":"futuro"},
  {"text":"La cuenta, por favor.","sub":"de rekening, alstublieft","tag":"pedir"},
  {"text":"¡Que aproveche!","sub":"eet smakelijk!","tag":"cortesia"},
  {"text":"¿Me trae la carta, por favor?","sub":"mag ik het menu? — cortesía","tag":"pedir"},
  {"text":"De postre, un flan.","sub":"als dessert, een flan","tag":"pedir"},
  {"text":"¿Cuánto cuesta el ceviche?","sub":"hoeveel kost de ceviche?","tag":"pagar"}]}})

# 15 · SPEAK shadowing — con Diego (afbouwende fasen)  (6 items)
w({"id":"es-u5-shadowing-diego","title":"Shadowing con Diego","subtitle":"U5 · praat mee met Diego, steeds minder tekst",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"shadowing","prompt":"Escucha ▶ · habla al mismo tiempo · grábate ⏺","phases":["Texto completo","Palabras clave","Sin texto","Tu versión"],"items":[
  {"text":"En el mercado hay mucha fruta y muchas verduras.","sub":"op de markt is veel fruit en veel groenten","tag":"mercado"},
  {"text":"Voy a comprar un kilo de tomates y un poco de queso.","sub":"ik ga een kilo tomaten en een beetje kaas kopen","tag":"cantidad"},
  {"text":"Hoy vamos a comer tacos y guacamole.","sub":"vandaag gaan we taco's en guacamole eten","tag":"futuro"},
  {"text":"En México comemos muchos tacos al pastor.","sub":"in Mexico eten we veel tacos al pastor","tag":"mexico"},
  {"text":"¿Vas a probar el guacamole picante?","sub":"ga jij de pittige guacamole proeven?","tag":"futuro"},
  {"text":"Después vamos a pedir la cuenta y pagar.","sub":"daarna gaan we de rekening vragen en betalen","tag":"pedir","tip":"Ahora invita a un amigo de verdad. <span class='nl'>nodig nu een echte vriend uit.</span>"}]}})

# 16 · SPEAK voicemessage — pide comida (mensaje de voz)  (3 items)
w({"id":"es-u5-mensaje-pedido","title":"Mensaje de voz: pide comida","subtitle":"U5 · neem een spraakbericht op met je pedido",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz (30 s)","items":[
  {"text":"Pide comida para una fiesta (¿qué vas a comprar? ¿cuánta cantidad?).","cue":"para · la fiesta","tag":"pedir",
   "sub":"gebruik: voy a comprar · un kilo de · una botella de · un poco de",
   "tip":"Heb je 3 productos + cantidad gezegd? Neem opnieuw op. <span class='nl'>3 producten + hoeveelheid? herneem.</span>"},
  {"text":"Deja un mensaje para reservar una mesa (día, hora, personas).","cue":"la reserva","tag":"reservar",
   "sub":"gebruik: quiero reservar · una mesa · para … personas · a las …",
   "tip":"Día, hora y número de personas? Herneem. <span class='nl'>dag, uur, aantal personen? herneem.</span>"},
  {"text":"Cuéntale a un amigo qué vas a cocinar hoy y con qué ingredientes.","cue":"la receta","tag":"receta",
   "sub":"gebruik: voy a cocinar/preparar · lleva · primero… luego…",
   "tip":"Plato + 2 ingredientes + 1 paso? Herneem. <span class='nl'>gerecht + 2 ingrediënten + 1 stap? herneem.</span>"}]}})

# 17 · SPEAK repeat — describe tu plato favorito  (6 items)
w({"id":"es-u5-describe-plato","title":"Describe tu plato","subtitle":"U5 · beschrijf je lievelingsgerecht, grábate",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · describe tu plato · grábate ⏺","items":[
  {"cue":"Modelo · Diego 🇲🇽","text":"Mi plato favorito son los tacos.","sub":"mijn lievelingsgerecht zijn taco's","tag":"describir"},
  {"cue":"¿qué lleva?","text":"Llevan carne, verdura y salsa.","sub":"ze bevatten vlees, groente en saus","tag":"describir"},
  {"cue":"¿por qué?","text":"Me encantan porque están muy ricos.","sub":"ik ben er dol op want ze zijn heel lekker","tag":"describir"},
  {"cue":"¿cuándo?","text":"Los como los fines de semana con mi familia.","sub":"ik eet ze in het weekend met mijn familie","tag":"describir"},
  {"cue":"¿picante?","text":"A veces con un poco de chile, pero no muy picante.","sub":"soms met wat chili, maar niet te pittig","tag":"describir"},
  {"cue":"tu versión","text":"Mi plato favorito es ___ . Lleva ___ .","sub":"jouw versie — vul in en zeg ze","tag":"describir",
   "tip":"Ahora describe el plato de un amigo. <span class='nl'>beschrijf nu het gerecht van een vriend(in).</span>"}]}})

print("\n21 U5-spellen geschreven (10 templates: memory·match·classify·cloze·tetris·order·point·sim·speak).")
print("Pools >=12 per game; options.rounds lager => herspeling geeft een andere reeks.")
