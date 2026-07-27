#!/usr/bin/env python3
# Genereert de motor-content-JSON's voor C5 · U6 «De tiendas» (parada México/mercados).
# Templates: memory·match·classify·cloze·tetris·order·point·sim·speak (receptief -> productief -> hablar).
# Elke game heeft een POOL van >=12 items; options.rounds staat lager zodat herspeling een ANDERE reeks trekt.
# Grammatica (lo/la/los/las · acabar de + infinitivo · este/ese/aquel · concordancia) nagerekend/geverifieerd.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2))
    print("wrote", os.path.basename(p))

G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0"}

# ============================ ① RECONOCER · woordenschat ============================
# 1 · MEMORY — ropa ES ↔ NL  (pool 14)
w({"id":"es-u6-ropa-memoria","title":"Memoria de la ropa","subtitle":"U6 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om en zoek het woord + de vertaling","pairs":[
  {"a":"la camiseta","b":"T-shirt"},{"a":"los pantalones","b":"broek"},{"a":"el vestido","b":"jurk"},
  {"a":"la falda","b":"rok"},{"a":"los zapatos","b":"schoenen"},{"a":"las botas","b":"laarzen"},
  {"a":"la gorra","b":"pet"},{"a":"el abrigo","b":"jas"},{"a":"los vaqueros","b":"jeans"},
  {"a":"el jersey","b":"trui"},{"a":"la bufanda","b":"sjaal"},{"a":"el bolso","b":"handtas"},
  {"a":"las gafas de sol","b":"zonnebril"},{"a":"los calcetines","b":"sokken"}]}})

# 2 · MEMORY — tienda ↔ producto  (pool 12)
w({"id":"es-u6-tienda-producto-memoria","title":"Tienda y producto","subtitle":"U6 · welke winkel verkoopt wat?",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: winkel + product","pairs":[
  {"a":"la zapatería","b":"los zapatos"},{"a":"la panadería","b":"el pan"},{"a":"la carnicería","b":"la carne"},
  {"a":"la frutería","b":"la fruta"},{"a":"la farmacia","b":"las medicinas"},{"a":"la tienda de ropa","b":"los vestidos"},
  {"a":"el supermercado","b":"la compra"},{"a":"la joyería","b":"los anillos"},{"a":"la librería","b":"los libros"},
  {"a":"la pastelería","b":"los pasteles"},{"a":"la papelería","b":"los cuadernos"},{"a":"la perfumería","b":"los perfumes"}]}})

# 3 · MATCH — prenda ↔ tienda  (pool 12)
w({"id":"es-u6-prenda-tienda","title":"Prenda y tienda","subtitle":"U6 · waar koop je het?",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind de prenda/product met de winkel","pairs":[
  {"a":"los zapatos","b":"la zapatería 👟"},{"a":"el pan","b":"la panadería 🥖"},
  {"a":"una camiseta","b":"la tienda de ropa 👕"},{"a":"la carne","b":"la carnicería 🥩"},
  {"a":"las manzanas","b":"la frutería 🍎"},{"a":"un anillo","b":"la joyería 💍"},
  {"a":"un libro","b":"la librería 📚"},{"a":"una medicina","b":"la farmacia 💊"},
  {"a":"un pastel","b":"la pastelería 🍰"},{"a":"el pescado","b":"la pescadería 🐟"},
  {"a":"un cuaderno","b":"la papelería ✏️"},{"a":"un perfume","b":"la perfumería 🧴"}]}})

# 4 · MATCH — color + prenda (concordancia)  (pool 12)
w({"id":"es-u6-color-prenda","title":"Color y prenda","subtitle":"U6 · welke vorm van de kleur past?",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind de prenda met de juiste vorm van de kleur (m/v · ev/mv)","pairs":[
  {"a":"una camiseta (roja)","b":"roja"},{"a":"un vestido (rojo)","b":"rojo"},
  {"a":"unos zapatos (rojos)","b":"rojos"},{"a":"unas botas (rojas)","b":"rojas"},
  {"a":"unos vaqueros (azul)","b":"azules"},{"a":"una falda (azul)","b":"azul"},
  {"a":"un jersey (negro)","b":"negro"},{"a":"unas sandalias (negro)","b":"negras"},
  {"a":"una gorra (blanco)","b":"blanca"},{"a":"unos calcetines (verde)","b":"verdes"},
  {"a":"un abrigo (gris)","b":"gris"},{"a":"unas gafas (marrón)","b":"marrones"}]}})

# ============================ ② DISTINGUIR · gramática/léxico ============================
# 5 · CLASSIFY — ¿arriba, abajo, calzado o complemento?  (pool 20, rounds 12)
w({"id":"es-u6-ropa-tipo","title":"¿Dónde va la prenda?","subtitle":"U6 · arriba · abajo · calzado · complemento",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Sorteer de prenda: bovenlijf · onderlijf · schoeisel · accessoire","categories":[
  {"id":"arriba","label":"arriba<br><small>bovenlijf</small>","glaze":G["blue"]},
  {"id":"abajo","label":"abajo<br><small>onderlijf</small>","glaze":G["green"]},
  {"id":"calzado","label":"calzado<br><small>schoeisel</small>","glaze":G["amber"]},
  {"id":"complemento","label":"complemento<br><small>accessoire</small>","glaze":G["purple"]}],
 "items":[
  {"stimulus":"la camiseta","answer":"arriba","tag":"arriba","sub":"T-shirt"},
  {"stimulus":"la camisa","answer":"arriba","tag":"arriba","sub":"hemd"},
  {"stimulus":"el jersey","answer":"arriba","tag":"arriba","sub":"trui"},
  {"stimulus":"la sudadera","answer":"arriba","tag":"arriba","sub":"sweater"},
  {"stimulus":"la chaqueta","answer":"arriba","tag":"arriba","sub":"vest"},
  {"stimulus":"los pantalones","answer":"abajo","tag":"abajo","sub":"broek"},
  {"stimulus":"los vaqueros","answer":"abajo","tag":"abajo","sub":"jeans"},
  {"stimulus":"la falda","answer":"abajo","tag":"abajo","sub":"rok"},
  {"stimulus":"el vestido","answer":"abajo","tag":"abajo","sub":"jurk (onderlijf-groep)"},
  {"stimulus":"el bañador","answer":"abajo","tag":"abajo","sub":"zwembroek"},
  {"stimulus":"los zapatos","answer":"calzado","tag":"calzado","sub":"schoenen"},
  {"stimulus":"las zapatillas","answer":"calzado","tag":"calzado","sub":"sportschoenen"},
  {"stimulus":"las botas","answer":"calzado","tag":"calzado","sub":"laarzen"},
  {"stimulus":"las sandalias","answer":"calzado","tag":"calzado","sub":"sandalen"},
  {"stimulus":"los calcetines","answer":"calzado","tag":"calzado","sub":"sokken"},
  {"stimulus":"la gorra","answer":"complemento","tag":"complemento","sub":"pet"},
  {"stimulus":"la bufanda","answer":"complemento","tag":"complemento","sub":"sjaal"},
  {"stimulus":"el cinturón","answer":"complemento","tag":"complemento","sub":"riem"},
  {"stimulus":"el bolso","answer":"complemento","tag":"complemento","sub":"handtas"},
  {"stimulus":"las gafas de sol","answer":"complemento","tag":"complemento","sub":"zonnebril"}]}})

# 6 · CLASSIFY — ¿lo, la, los o las?  (pool 18, rounds 12)
w({"id":"es-u6-lo-la-los-las","title":"¿lo, la, los o las?","subtitle":"U6 · welk pronomen vervangt de prenda?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Welk pronomen vervangt de prenda? (m/v · ev/mv)","categories":[
  {"id":"lo","label":"lo<br><small>m. ev.</small>","glaze":G["blue"]},
  {"id":"la","label":"la<br><small>v. ev.</small>","glaze":G["red"]},
  {"id":"los","label":"los<br><small>m. mv.</small>","glaze":G["green"]},
  {"id":"las","label":"las<br><small>v. mv.</small>","glaze":G["amber"]}],
 "items":[
  {"stimulus":"la falda","answer":"la","tag":"la","sub":"v. ev."},
  {"stimulus":"el jersey","answer":"lo","tag":"lo","sub":"m. ev."},
  {"stimulus":"los zapatos","answer":"los","tag":"los","sub":"m. mv."},
  {"stimulus":"las botas","answer":"las","tag":"las","sub":"v. mv."},
  {"stimulus":"la camisa","answer":"la","tag":"la","sub":"v. ev."},
  {"stimulus":"el abrigo","answer":"lo","tag":"lo","sub":"m. ev."},
  {"stimulus":"los vaqueros","answer":"los","tag":"los","sub":"m. mv."},
  {"stimulus":"las sandalias","answer":"las","tag":"las","sub":"v. mv."},
  {"stimulus":"el cinturón","answer":"lo","tag":"lo","sub":"m. ev."},
  {"stimulus":"la gorra","answer":"la","tag":"la","sub":"v. ev."},
  {"stimulus":"los calcetines","answer":"los","tag":"los","sub":"m. mv."},
  {"stimulus":"las gafas","answer":"las","tag":"las","sub":"v. mv."},
  {"stimulus":"el vestido","answer":"lo","tag":"lo","sub":"m. ev."},
  {"stimulus":"la bufanda","answer":"la","tag":"la","sub":"v. ev."},
  {"stimulus":"los guantes","answer":"los","tag":"los","sub":"m. mv."},
  {"stimulus":"las zapatillas","answer":"las","tag":"las","sub":"v. mv."},
  {"stimulus":"el sombrero","answer":"lo","tag":"lo","sub":"m. ev."},
  {"stimulus":"la chaqueta","answer":"la","tag":"la","sub":"v. ev."}]}})

# 7 · CLASSIFY — masculino o femenino (concordancia)  (pool 18, rounds 12)
w({"id":"es-u6-genero-adjetivo","title":"Masculino o femenino","subtitle":"U6 · concordantie van kleur/adjectief",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Is de prenda masculino of femenino? (kies de juiste kleurvorm)","categories":[
  {"id":"masc","label":"masculino<br><small>-o / los</small>","glaze":G["blue"]},
  {"id":"fem","label":"femenino<br><small>-a / las</small>","glaze":G["red"]}],
 "items":[
  {"stimulus":"un vestido roj__","answer":"masc","tag":"masc","sub":"vestido (m) → rojo"},
  {"stimulus":"una camiseta roj__","answer":"fem","tag":"fem","sub":"camiseta (v) → roja"},
  {"stimulus":"un jersey negr__","answer":"masc","tag":"masc","sub":"jersey (m) → negro"},
  {"stimulus":"una falda negr__","answer":"fem","tag":"fem","sub":"falda (v) → negra"},
  {"stimulus":"un abrigo blanc__","answer":"masc","tag":"masc","sub":"abrigo (m) → blanco"},
  {"stimulus":"una blusa blanc__","answer":"fem","tag":"fem","sub":"blusa (v) → blanca"},
  {"stimulus":"un bolso amarill__","answer":"masc","tag":"masc","sub":"bolso (m) → amarillo"},
  {"stimulus":"una gorra amarill__","answer":"fem","tag":"fem","sub":"gorra (v) → amarilla"},
  {"stimulus":"un sombrero morad__","answer":"masc","tag":"masc","sub":"sombrero (m) → morado"},
  {"stimulus":"una chaqueta morad__","answer":"fem","tag":"fem","sub":"chaqueta (v) → morada"},
  {"stimulus":"un cinturón roj__","answer":"masc","tag":"masc","sub":"cinturón (m) → rojo"},
  {"stimulus":"una bufanda roj__","answer":"fem","tag":"fem","sub":"bufanda (v) → roja"},
  {"stimulus":"un traje negr__","answer":"masc","tag":"masc","sub":"traje (m) → negro"},
  {"stimulus":"una camisa blanc__","answer":"fem","tag":"fem","sub":"camisa (v) → blanca"},
  {"stimulus":"un pañuelo roj__","answer":"masc","tag":"masc","sub":"pañuelo (m) → rojo"},
  {"stimulus":"una corbata amarill__","answer":"fem","tag":"fem","sub":"corbata (v) → amarilla"},
  {"stimulus":"un pijama blanc__","answer":"masc","tag":"masc","sub":"pijama (m) → blanco"},
  {"stimulus":"una sudadera negr__","answer":"fem","tag":"fem","sub":"sudadera (v) → negra"}]}})

# 8 · CLASSIFY — cerca · ahí · lejos (este/ese/aquel)  (pool 18, rounds 12)
w({"id":"es-u6-este-ese-aquel","title":"Cerca, ahí o lejos","subtitle":"U6 · este (cerca) · ese (ahí) · aquel (lejos)",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Bij welke afstand hoort het aanwijswoord?","categories":[
  {"id":"cerca","label":"este/esta<br><small>cerca · aquí</small>","glaze":G["green"]},
  {"id":"ahi","label":"ese/esa<br><small>ahí</small>","glaze":G["amber"]},
  {"id":"lejos","label":"aquel/aquella<br><small>lejos · allí</small>","glaze":G["purple"]}],
 "items":[
  {"stimulus":"este jersey","answer":"cerca","tag":"cerca","sub":"aquí"},
  {"stimulus":"esta falda","answer":"cerca","tag":"cerca","sub":"aquí"},
  {"stimulus":"estos zapatos","answer":"cerca","tag":"cerca","sub":"aquí"},
  {"stimulus":"estas botas","answer":"cerca","tag":"cerca","sub":"aquí"},
  {"stimulus":"ese abrigo","answer":"ahi","tag":"ahi","sub":"ahí"},
  {"stimulus":"esa gorra","answer":"ahi","tag":"ahi","sub":"ahí"},
  {"stimulus":"esos vaqueros","answer":"ahi","tag":"ahi","sub":"ahí"},
  {"stimulus":"esas sandalias","answer":"ahi","tag":"ahi","sub":"ahí"},
  {"stimulus":"aquel vestido","answer":"lejos","tag":"lejos","sub":"allí"},
  {"stimulus":"aquella camisa","answer":"lejos","tag":"lejos","sub":"allí"},
  {"stimulus":"aquellos calcetines","answer":"lejos","tag":"lejos","sub":"allí"},
  {"stimulus":"aquellas gafas","answer":"lejos","tag":"lejos","sub":"allí"},
  {"stimulus":"este cinturón","answer":"cerca","tag":"cerca","sub":"aquí"},
  {"stimulus":"esa bufanda","answer":"ahi","tag":"ahi","sub":"ahí"},
  {"stimulus":"aquel sombrero","answer":"lejos","tag":"lejos","sub":"allí"},
  {"stimulus":"estas zapatillas","answer":"cerca","tag":"cerca","sub":"aquí"},
  {"stimulus":"ese traje","answer":"ahi","tag":"ahi","sub":"ahí"},
  {"stimulus":"aquellas botas","answer":"lejos","tag":"lejos","sub":"allí"}]}})

# ============================ ③ PRODUCIR CON APOYO ============================
# 9 · CLOZE — lo/la/los/las  (pool 18, rounds 12)
w({"id":"es-u6-pronombre-od-cloze","title":"Completa: lo/la/los/las","subtitle":"U6 · vervang de prenda (la falda → la compro)",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies het juiste pronomen (lo/la/los/las)","items":[
  {"stimulus":"¿La falda? —Sí, ___ compro.","options":["la","lo","las"],"answer":"la","tag":"od","sub":"la falda (v ev)"},
  {"stimulus":"¿El jersey? —___ quiero.","options":["Lo","La","Los"],"answer":"Lo","tag":"od","sub":"el jersey (m ev)"},
  {"stimulus":"¿Los zapatos? —Sí, ___ llevo.","options":["los","las","lo"],"answer":"los","tag":"od","sub":"los zapatos (m pl)"},
  {"stimulus":"¿Las botas? —___ me pruebo.","options":["Las","Los","La"],"answer":"Las","tag":"od","sub":"las botas (v pl)"},
  {"stimulus":"¿La camisa? —Ahora ___ busco.","options":["la","lo","las"],"answer":"la","tag":"od","sub":"la camisa (v ev)"},
  {"stimulus":"¿El abrigo? —Sí, ___ compro.","options":["lo","la","los"],"answer":"lo","tag":"od","sub":"el abrigo (m ev)"},
  {"stimulus":"¿Los vaqueros? —___ llevo hoy.","options":["Los","Las","Lo"],"answer":"Los","tag":"od","sub":"los vaqueros (m pl)"},
  {"stimulus":"¿Las gafas? —___ veo en el escaparate.","options":["Las","Los","La"],"answer":"Las","tag":"od","sub":"las gafas (v pl)"},
  {"stimulus":"¿El cinturón? —___ compro también.","options":["Lo","La","Los"],"answer":"Lo","tag":"od","sub":"el cinturón (m ev)"},
  {"stimulus":"¿La gorra? —___ quiero roja.","options":["La","Lo","Las"],"answer":"La","tag":"od","sub":"la gorra (v ev)"},
  {"stimulus":"¿Los calcetines? —___ pago en la caja.","options":["Los","Las","Lo"],"answer":"Los","tag":"od","sub":"los calcetines (m pl)"},
  {"stimulus":"¿Las sandalias? —___ me llevo.","options":["Las","Los","La"],"answer":"Las","tag":"od","sub":"las sandalias (v pl)"},
  {"stimulus":"¿El vestido? —Voy a comprar___.","options":["lo","la","los"],"answer":"lo","tag":"od","sub":"comprarlo (achter infinitief)"},
  {"stimulus":"¿La chaqueta? —Quiero probár___la.","options":["me","te","se"],"answer":"me","tag":"od","sub":"probármela (me + la)"},
  {"stimulus":"¿Los guantes? —Sí, ___ necesito.","options":["los","las","lo"],"answer":"los","tag":"od","sub":"los guantes (m pl)"},
  {"stimulus":"¿La bufanda? —___ llevo en invierno.","options":["La","Lo","Las"],"answer":"La","tag":"od","sub":"la bufanda (v ev)"},
  {"stimulus":"¿El sombrero? —___ compro en el tianguis.","options":["Lo","La","Los"],"answer":"Lo","tag":"od","sub":"el sombrero (m ev)"},
  {"stimulus":"¿Las camisetas? —___ tienen en rebajas.","options":["Las","Los","La"],"answer":"Las","tag":"od","sub":"las camisetas (v pl)"}]}})

# 10 · CLOZE — acabar de + infinitivo (VERPLICHT, nagerekend)  (pool 18, rounds 12)
w({"id":"es-u6-acabar-de-cloze","title":"Completa: acabar de + infinitivo","subtitle":"U6 · net iets gedaan (acabo de comprar…)",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm van «acabar de»","items":[
  {"stimulus":"(Yo) ___ comprar una gorra.","options":["acabo de","acaba de","acabas de"],"answer":"acabo de","tag":"ac","sub":"yo → acabo de"},
  {"stimulus":"¿(Tú) ___ probarte el vestido?","options":["acabas de","acabo de","acaban de"],"answer":"acabas de","tag":"ac","sub":"tú → acabas de"},
  {"stimulus":"(Nosotros) ___ pagar en la caja.","options":["acabamos de","acaban de","acabáis de"],"answer":"acabamos de","tag":"ac","sub":"nosotros → acabamos de"},
  {"stimulus":"Diego ___ llegar al mercado.","options":["acaba de","acaban de","acabas de"],"answer":"acaba de","tag":"ac","sub":"él → acaba de"},
  {"stimulus":"(Ellos) ___ ver el escaparate.","options":["acaban de","acaba de","acabamos de"],"answer":"acaban de","tag":"ac","sub":"ellos → acaban de"},
  {"stimulus":"Lucía ___ encontrar unas botas.","options":["acaba de","acaban de","acabas de"],"answer":"acaba de","tag":"ac","sub":"ella → acaba de"},
  {"stimulus":"¿(Vosotros) ___ entrar en la tienda?","options":["acabáis de","acaban de","acabamos de"],"answer":"acabáis de","tag":"ac","sub":"vosotros → acabáis de"},
  {"stimulus":"(Yo) ___ elegir la talla M.","options":["acabo de","acaba de","acabas de"],"answer":"acabo de","tag":"ac","sub":"yo → acabo de"},
  {"stimulus":"Acabo ___ comprar una camisa.","options":["de","a","que"],"answer":"de","tag":"ac","sub":"acabar DE + infinitivo"},
  {"stimulus":"Valen y Nina ___ salir de la tienda.","options":["acaban de","acabamos de","acabáis de"],"answer":"acaban de","tag":"ac","sub":"ellas → acaban de"},
  {"stimulus":"¿Qué ___ comprar (tú)?","options":["acabas de","acaba de","acabo de"],"answer":"acabas de","tag":"ac","sub":"tú → acabas de"},
  {"stimulus":"(Nosotros) ___ regatear el precio.","options":["acabamos de","acaban de","acabo de"],"answer":"acabamos de","tag":"ac","sub":"nosotros → acabamos de"},
  {"stimulus":"Él ___ probarse los zapatos.","options":["acaba de","acaban de","acabas de"],"answer":"acaba de","tag":"ac","sub":"él → acaba de"},
  {"stimulus":"(Yo) ___ pagar con tarjeta.","options":["acabo de","acaba de","acabáis de"],"answer":"acabo de","tag":"ac","sub":"yo → acabo de"},
  {"stimulus":"Mis amigos ___ abrir una tienda.","options":["acaban de","acaba de","acabamos de"],"answer":"acaban de","tag":"ac","sub":"ellos → acaban de"},
  {"stimulus":"¿(Tú) ___ ver las rebajas?","options":["acabas de","acaba de","acabo de"],"answer":"acabas de","tag":"ac","sub":"tú → acabas de"},
  {"stimulus":"La dependienta ___ abrir la caja.","options":["acaba de","acaban de","acabas de"],"answer":"acaba de","tag":"ac","sub":"ella → acaba de"},
  {"stimulus":"(Nosotros) ___ encontrar un descuento.","options":["acabamos de","acaban de","acabo de"],"answer":"acabamos de","tag":"ac","sub":"nosotros → acabamos de"}]}})

# 11 · CLOZE — este/ese/aquel  (pool 16, rounds 10)
w({"id":"es-u6-demostrativo-cloze","title":"Completa: este/ese/aquel","subtitle":"U6 · cerca · ahí · lejos (concordantie)",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm (cerca=este · ahí=ese · lejos=aquel)","items":[
  {"stimulus":"Me gusta ___ camiseta (aquí).","options":["esta","esa","aquella"],"answer":"esta","tag":"d","sub":"cerca (v) → esta"},
  {"stimulus":"¿Cuánto cuesta ___ gorra (ahí)?","options":["esa","esta","aquella"],"answer":"esa","tag":"d","sub":"ahí (v) → esa"},
  {"stimulus":"___ abrigo (allí) es caro.","options":["Aquel","Este","Ese"],"answer":"Aquel","tag":"d","sub":"lejos (m) → aquel"},
  {"stimulus":"___ zapatos (aquí) son cómodos.","options":["estos","esos","aquellos"],"answer":"estos","tag":"d","sub":"cerca (m pl) → estos"},
  {"stimulus":"Prefiero ___ vestido (ahí).","options":["ese","este","aquel"],"answer":"ese","tag":"d","sub":"ahí (m) → ese"},
  {"stimulus":"___ botas (allí) son de cuero.","options":["aquellas","estas","esas"],"answer":"aquellas","tag":"d","sub":"lejos (v pl) → aquellas"},
  {"stimulus":"¿Te gusta ___ jersey (aquí)?","options":["este","ese","aquel"],"answer":"este","tag":"d","sub":"cerca (m) → este"},
  {"stimulus":"___ falda (ahí) es de cuadros.","options":["esa","esta","aquella"],"answer":"esa","tag":"d","sub":"ahí (v) → esa"},
  {"stimulus":"Mira ___ pantalones (allí).","options":["aquellos","estos","esos"],"answer":"aquellos","tag":"d","sub":"lejos (m pl) → aquellos"},
  {"stimulus":"Quiero ___ sandalias (aquí).","options":["estas","esas","aquellas"],"answer":"estas","tag":"d","sub":"cerca (v pl) → estas"},
  {"stimulus":"¿Cuánto es ___ cinturón (ahí)?","options":["ese","este","aquel"],"answer":"ese","tag":"d","sub":"ahí (m) → ese"},
  {"stimulus":"___ camisa (allí) es blanca.","options":["Aquella","Esta","Esa"],"answer":"Aquella","tag":"d","sub":"lejos (v) → aquella"},
  {"stimulus":"Me llevo ___ gafas (aquí).","options":["estas","esas","aquellas"],"answer":"estas","tag":"d","sub":"cerca (v pl) → estas"},
  {"stimulus":"___ sombrero (ahí) es bonito.","options":["Ese","Este","Aquel"],"answer":"Ese","tag":"d","sub":"ahí (m) → ese"},
  {"stimulus":"¿Ves ___ calcetines (allí)?","options":["aquellos","estos","esos"],"answer":"aquellos","tag":"d","sub":"lejos (m pl) → aquellos"},
  {"stimulus":"Compro ___ bufanda (aquí).","options":["esta","esa","aquella"],"answer":"esta","tag":"d","sub":"cerca (v) → esta"}]}})

# 12 · TETRIS — concordancia (la kleurvorm valt in de juiste kolom)  (pool 18)
w({"id":"es-u6-concordancia-tetris","title":"Concordancia Tetris","subtitle":"U6 · laat de prenda in de juiste kleurvorm vallen",
 "lang":"es","template":"tetris","options":{"rows":9,"speed":1300,"audio":False},
 "classify":{"categories":[
  {"id":"o","label":"-o (m.ev.)","glaze":G["blue"]},{"id":"a","label":"-a (v.ev.)","glaze":G["red"]},
  {"id":"os","label":"-os (m.mv.)","glaze":G["green"]},{"id":"as","label":"-as (v.mv.)","glaze":G["amber"]}],
 "items":[
  {"stimulus":"vestido roj_","answer":"o","tag":"o","sub":"el vestido (m)"},
  {"stimulus":"camiseta roj_","answer":"a","tag":"a","sub":"la camiseta (v)"},
  {"stimulus":"zapatos roj_","answer":"os","tag":"os","sub":"los zapatos (m pl)"},
  {"stimulus":"botas roj_","answer":"as","tag":"as","sub":"las botas (v pl)"},
  {"stimulus":"jersey negr_","answer":"o","tag":"o","sub":"el jersey (m)"},
  {"stimulus":"falda negr_","answer":"a","tag":"a","sub":"la falda (v)"},
  {"stimulus":"calcetines negr_","answer":"os","tag":"os","sub":"los calcetines (m pl)"},
  {"stimulus":"sandalias negr_","answer":"as","tag":"as","sub":"las sandalias (v pl)"},
  {"stimulus":"abrigo blanc_","answer":"o","tag":"o","sub":"el abrigo (m)"},
  {"stimulus":"blusa blanc_","answer":"a","tag":"a","sub":"la blusa (v)"},
  {"stimulus":"pantalones blanc_","answer":"os","tag":"os","sub":"los pantalones (m pl)"},
  {"stimulus":"camisas blanc_","answer":"as","tag":"as","sub":"las camisas (v pl)"},
  {"stimulus":"bolso amarill_","answer":"o","tag":"o","sub":"el bolso (m)"},
  {"stimulus":"gorra amarill_","answer":"a","tag":"a","sub":"la gorra (v)"},
  {"stimulus":"zapatos amarill_","answer":"os","tag":"os","sub":"los zapatos (m pl)"},
  {"stimulus":"gafas amarill_","answer":"as","tag":"as","sub":"las gafas (v pl)"},
  {"stimulus":"sombrero morad_","answer":"o","tag":"o","sub":"el sombrero (m)"},
  {"stimulus":"chaqueta morad_","answer":"a","tag":"a","sub":"la chaqueta (v)"}]}})

# 13 · ORDER — ordena el diálogo de la tienda  (8 rondes)
w({"id":"es-u6-orden-tienda","title":"Ordena el diálogo","subtitle":"U6 · zet de winkel-dialoog in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik de zinnen in de logische volgorde van een winkelbezoek","rounds":[
  {"tag":"tienda","sub":"entrar → buscar → probar → comprar","items":[
    {"label":"Buenas, ¿qué desea?","key":1},{"label":"Busco una camisa azul.","key":2},
    {"label":"¿Puedo probármela?","key":3},{"label":"Me queda bien, me la llevo.","key":4}]},
  {"tag":"tienda","sub":"talla → probador → precio → pago","items":[
    {"label":"¿La tienen en talla M?","key":1},{"label":"Sí, el probador está allí.","key":2},
    {"label":"¿Cuánto cuesta?","key":3},{"label":"Son 20 €. Pago con tarjeta.","key":4}]},
  {"tag":"tianguis","sub":"regateo: precio → caro → descuento → trato","items":[
    {"label":"¿Cuánto cuesta este poncho?","key":1},{"label":"Cuesta 300 pesos.","key":2},
    {"label":"Es un poco caro, ¿me hace un descuento?","key":3},{"label":"Vale, 250. ¡Me lo llevo!","key":4}]},
  {"tag":"tienda","sub":"saludar → mostrar → color → decidir","items":[
    {"label":"Hola, ¿me enseña esa chaqueta?","key":1},{"label":"Claro, ¿de qué color la quiere?","key":2},
    {"label":"La quiero negra o gris.","key":3},{"label":"Esta negra le queda genial.","key":4}]},
  {"tag":"rebajas","sub":"rebajas → elegir → probar → pagar","items":[
    {"label":"¡Hay rebajas! −50 % en vaqueros.","key":1},{"label":"Quiero estos vaqueros azules.","key":2},
    {"label":"Me los pruebo en el probador.","key":3},{"label":"Perfecto, pago en la caja.","key":4}]},
  {"tag":"tienda","sub":"escaparate → entrar → preguntar → probar","items":[
    {"label":"Me gusta el vestido del escaparate.","key":1},{"label":"Entro en la tienda.","key":2},
    {"label":"¿Lo tienen en mi talla?","key":3},{"label":"Sí, ¿quiere probárselo?","key":4}]},
  {"tag":"devolucion","sub":"comprar → no queda → volver → cambiar","items":[
    {"label":"Acabo de comprar esta camisa.","key":1},{"label":"Pero no me queda bien.","key":2},
    {"label":"Vuelvo a la tienda.","key":3},{"label":"¿Puedo cambiarla por otra talla?","key":4}]},
  {"tag":"complementos","sub":"combinar el look","items":[
    {"label":"Primero, la camiseta blanca.","key":1},{"label":"Luego, los vaqueros azules.","key":2},
    {"label":"Después, las zapatillas.","key":3},{"label":"Por último, la gorra roja.","key":4}]}]}})

# 14 · ORDER — ordena los pasos de la compra  (6 rondes)
w({"id":"es-u6-pasos-compra","title":"Ordena los pasos","subtitle":"U6 · zet de stappen van het winkelen op volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik de stappen in de juiste volgorde","rounds":[
  {"tag":"compra","sub":"la compra 🛍️","items":[
    {"label":"Entrar en la tienda","key":1},{"label":"Elegir una prenda","key":2},
    {"label":"Probarse en el probador","key":3},{"label":"Pagar en la caja","key":4}]},
  {"tag":"precios","sub":"de barato a caro (Moda Diego)","items":[
    {"label":"Camiseta — 5 €","key":1},{"label":"Vestido de lunares — 20 €","key":2},
    {"label":"Vaqueros — 25 €","key":3},{"label":"Zapatillas — 39 €","key":4}]},
  {"tag":"distancia","sub":"cerca → lejos","items":[
    {"label":"esta camiseta (aquí)","key":1},{"label":"esa gorra (ahí)","key":2},
    {"label":"aquel abrigo (allí)","key":3}]},
  {"tag":"tallas","sub":"de pequeño a grande","items":[
    {"label":"talla S (pequeña)","key":1},{"label":"talla M (mediana)","key":2},
    {"label":"talla L (grande)","key":3},{"label":"talla XL (muy grande)","key":4}]},
  {"tag":"rebajas","sub":"del descuento pequeño al grande","items":[
    {"label":"−10 %","key":1},{"label":"−25 %","key":2},{"label":"−50 %","key":3},{"label":"−70 %","key":4}]},
  {"tag":"look","sub":"vestirse de arriba abajo","items":[
    {"label":"la gorra (cabeza)","key":1},{"label":"la camiseta (arriba)","key":2},
    {"label":"los pantalones (abajo)","key":3},{"label":"los zapatos (pies)","key":4}]}]}})

# 15 · POINT — señala en el escaparate  (10 rondes)
w({"id":"es-u6-senala-escaparate","title":"Señala en el escaparate","subtitle":"U6 · klik het juiste artikel",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het gevraagde artikel","mode":"one","rounds":[
  {"tag":"arriba","sub":"señala una prenda de arriba","targets":[
    {"label":"la falda"},{"label":"la camiseta","hit":True},{"label":"los zapatos"},{"label":"la gorra"}]},
  {"tag":"abajo","sub":"señala una prenda de abajo","targets":[
    {"label":"el jersey"},{"label":"los pantalones","hit":True},{"label":"las botas"},{"label":"el bolso"}]},
  {"tag":"calzado","sub":"señala el calzado","targets":[
    {"label":"la camisa"},{"label":"las zapatillas","hit":True},{"label":"la bufanda"},{"label":"el cinturón"}]},
  {"tag":"complemento","sub":"señala un complemento","targets":[
    {"label":"el vestido"},{"label":"las gafas de sol","hit":True},{"label":"los calcetines"},{"label":"la falda"}]},
  {"tag":"color","sub":"señala algo rojo","targets":[
    {"label":"una camiseta roja","hit":True},{"label":"un vestido azul"},{"label":"unos zapatos negros"},{"label":"una gorra verde"}]},
  {"tag":"patron","sub":"señala algo de rayas","targets":[
    {"label":"una camisa de rayas","hit":True},{"label":"una falda de lunares"},{"label":"un jersey liso"},{"label":"unos vaqueros"}]},
  {"tag":"tienda","sub":"señala dónde compras zapatos","targets":[
    {"label":"la panadería"},{"label":"la zapatería","hit":True},{"label":"la farmacia"},{"label":"la frutería"}]},
  {"tag":"caja","sub":"señala dónde se paga","targets":[
    {"label":"el probador"},{"label":"la caja","hit":True},{"label":"el escaparate"},{"label":"la etiqueta"}]},
  {"tag":"probador","sub":"señala dónde te pruebas la ropa","targets":[
    {"label":"el probador","hit":True},{"label":"la bolsa","hit":False},{"label":"la caja"},{"label":"el recibo"}]},
  {"tag":"rebajas","sub":"señala el descuento","targets":[
    {"label":"las rebajas","hit":True},{"label":"la talla"},{"label":"la tarjeta"},{"label":"el probador"}]}]}})

# ============================ ④ ANALIZAR & COMUNICAR ============================
# 16 · SIM — ¡Vas de compras! (regateo, met bouwsteen-check)  (6 rondes)
w({"id":"es-u6-de-compras","title":"¡Vas de compras!","subtitle":"U6 · schrijf je zin — met alle bouwstenen",
 "lang":"es","template":"sim","options":{"audio":False},
 "sim":{"prompt":"Tarea comunicativa · de compras","rounds":[
  {"scenario":"El/la dependiente/-a dice: «¿Qué desea?» — pide una prenda con color.","tag":"pedir","sub":"gebruik: busco · una/un · + color","min":8,
   "need":[{"re":"busco|quiero","label":"busco / quiero"},{"re":"camiseta|camisa|falda|vestido|jersey|vaqueros|abrigo","label":"una prenda"},{"re":"roj|azul|negr|blanc|verde|amarill|gris","label":"un color"}],
   "bank":["Busco","una camiseta","azul","roja","¿La tienen","en talla M?","por favor"],
   "model":"Busco una camiseta azul en talla M, por favor."},
  {"scenario":"Pregunta si te lo puedes probar y dónde está el probador.","tag":"probar","sub":"gebruik: ¿puedo probármelo/la? · el probador","min":8,
   "need":[{"re":"probár|probar","label":"probarme"},{"re":"lo|la|los|las","label":"pronomen (lo/la…)"},{"re":"probador","label":"el probador"}],
   "bank":["¿Puedo","probármela","probármelo","¿Dónde está","el probador","por favor"],
   "model":"¿Puedo probármela? ¿Dónde está el probador?"},
  {"scenario":"Regatea en el tianguis: el precio es alto, pide un descuento.","tag":"regateo","sub":"gebruik: ¿cuánto cuesta? · es caro · ¿me hace un descuento?","min":9,
   "need":[{"re":"cuánto|cuanto|precio","label":"¿cuánto cuesta?"},{"re":"caro","label":"es caro"},{"re":"descuento|rebaja","label":"un descuento"}],
   "bank":["¿Cuánto cuesta","este poncho?","Es un poco caro","¿me hace","un descuento?","me lo llevo"],
   "model":"¿Cuánto cuesta este poncho? Es un poco caro, ¿me hace un descuento?"},
  {"scenario":"Di qué acabas de comprar y de qué color es.","tag":"acabar","sub":"gebruik: acabo de comprar · + color","min":8,
   "need":[{"re":"acabo de","label":"acabo de"},{"re":"comprar","label":"comprar"},{"re":"roj|azul|negr|blanc|verde|gris|amarill","label":"un color"}],
   "bank":["Acabo de","comprar","unos vaqueros","azules","una camiseta","roja"],
   "model":"Acabo de comprar unos vaqueros azules y una camiseta roja."},
  {"scenario":"Señala una prenda lejos (en el escaparate) y pregunta el precio.","tag":"demostrativo","sub":"gebruik: aquel/aquella · ¿cuánto cuesta?","min":8,
   "need":[{"re":"aquel|aquella|aquellos|aquellas","label":"aquel/aquella…"},{"re":"cuánto|cuanto","label":"¿cuánto…?"},{"re":"cuesta|es","label":"cuesta / es"}],
   "bank":["¿Cuánto cuesta","aquel abrigo","aquella chaqueta","del escaparate?","por favor"],
   "model":"¿Cuánto cuesta aquel abrigo del escaparate?"},
  {"scenario":"Recomienda una prenda a un amigo y di por qué.","tag":"recomendar","sub":"gebruik: te recomiendo · porque · me queda bien","min":9,
   "need":[{"re":"recomiendo|recomienda","label":"te recomiendo"},{"re":"porque","label":"porque …"},{"re":"queda|bonit|gusta|barat","label":"me queda bien / es bonito"}],
   "bank":["Te recomiendo","esta chaqueta","porque","me queda bien","es bonita","y barata"],
   "model":"Te recomiendo esta chaqueta porque me queda bien y es barata."}]}})

# ============================ ⑤ HABLAR · grábate 🎙️ ============================
# 17 · SPEAK repeat — escucha y repite: en la tienda  (8 items)
w({"id":"es-u6-repite-tienda","title":"Escucha y repite: en la tienda","subtitle":"U6 · escucha el modelo, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite en voz alta · grábate ⏺","items":[
  {"text":"¿Cuánto cuesta esta camiseta?","sub":"hoeveel kost dit T-shirt?","tag":"precio","tip":"¡Bien! Ahora dilo sin leer. <span class='nl'>zeg het nu zonder te lezen.</span>"},
  {"text":"¿Puedo probármelo?","sub":"mag ik het passen? — probarse","tag":"probar"},
  {"text":"¿La tienen en talla M?","sub":"hebben jullie het in maat M?","tag":"talla"},
  {"text":"Me queda bien. Me lo llevo.","sub":"het staat me goed. ik neem het.","tag":"comprar"},
  {"text":"Acabo de comprar unos vaqueros.","sub":"ik heb net een jeans gekocht — acabar de","tag":"acabar"},
  {"text":"¿Me hace un descuento?","sub":"geeft u me korting? — regatear","tag":"regateo"},
  {"text":"Pago con tarjeta, por favor.","sub":"ik betaal met kaart","tag":"pago"},
  {"text":"Me gusta aquel abrigo del escaparate.","sub":"ik vind die jas in de etalage mooi","tag":"demostrativo"}]}})

# 18 · SPEAK shadowing — con Diego (afbouwende fasen)  (6 items)
w({"id":"es-u6-shadowing-diego","title":"Shadowing con Diego","subtitle":"U6 · praat mee met Diego, steeds minder tekst",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"shadowing","prompt":"Escucha ▶ · habla al mismo tiempo · grábate ⏺","phases":["Texto completo","Palabras clave","Sin texto","Tu versión"],"items":[
  {"text":"En el mercado hay mucha ropa de todos los colores.","sub":"op de markt is veel kleding in alle kleuren","tag":"mercado"},
  {"text":"Acabo de comprar una camiseta roja y unos vaqueros azules.","sub":"ik heb net een rood T-shirt en een blauwe jeans gekocht","tag":"acabar"},
  {"text":"¿Te gusta esta chaqueta o prefieres aquella?","sub":"vind je dit vest mooi of verkies je dat daar?","tag":"demostrativo"},
  {"text":"En el tianguis puedes regatear el precio.","sub":"op de tianguis kun je afdingen","tag":"regateo"},
  {"text":"¿La camisa azul? Sí, la compro. Me queda muy bien.","sub":"het blauwe hemd? ja, ik koop het. het staat me goed","tag":"od"},
  {"text":"Voy a pagar en la caja con tarjeta.","sub":"ik ga aan de kassa met kaart betalen","tag":"pago","tip":"Ahora invita a un amigo de verdad. <span class='nl'>nodig nu een echte vriend uit.</span>"}]}})

# 19 · SPEAK voicemessage — regatea (mensaje de voz)  (3 items)
w({"id":"es-u6-mensaje-regateo","title":"Mensaje de voz: regatea","subtitle":"U6 · neem een spraakbericht op met je regateo",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz (30 s)","items":[
  {"text":"Regatea el precio de una prenda en el tianguis (¿cuánto cuesta? ¿es caro? ¿un descuento?).","cue":"el regateo","tag":"regateo",
   "sub":"gebruik: ¿cuánto cuesta? · es caro · ¿me hace un descuento? · me lo llevo",
   "tip":"Prijs + «es caro» + descuento vragen? Neem opnieuw op. <span class='nl'>prijs + te duur + korting vragen? herneem.</span>"},
  {"text":"Deja un mensaje para describir tu outfit de hoy (prendas + colores).","cue":"mi look","tag":"describir",
   "sub":"gebruik: llevo · una/un · + color · de (rayas/algodón)",
   "tip":"3 prendas + kleur? Herneem. <span class='nl'>3 kledingstukken + kleur? herneem.</span>"},
  {"text":"Cuéntale a un amigo qué acabas de comprar y por qué te gusta.","cue":"la compra","tag":"acabar",
   "sub":"gebruik: acabo de comprar · me queda bien · porque",
   "tip":"Prenda + acabar de + reden? Herneem. <span class='nl'>kledingstuk + acabar de + reden? herneem.</span>"}]}})

# 20 · SPEAK repeat — describe tu ropa  (6 items)
w({"id":"es-u6-describe-ropa","title":"Describe tu ropa","subtitle":"U6 · beschrijf je outfit, grábate",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · describe tu ropa · grábate ⏺","items":[
  {"cue":"Modelo · Diego 🇲🇽","text":"Hoy llevo una camiseta verde y unos vaqueros.","sub":"vandaag draag ik een groen T-shirt en een jeans","tag":"describir"},
  {"cue":"¿de qué color?","text":"Mis zapatillas son blancas y negras.","sub":"mijn sneakers zijn wit en zwart","tag":"describir"},
  {"cue":"¿el patrón?","text":"Me gusta la ropa de rayas, no de lunares.","sub":"ik hou van gestreepte kleding, niet met stippen","tag":"describir"},
  {"cue":"¿por qué?","text":"Me queda bien porque es cómoda.","sub":"het staat me goed want het is comfortabel","tag":"describir"},
  {"cue":"¿nueva?","text":"Acabo de comprar esta gorra en las rebajas.","sub":"ik heb deze pet net in de solden gekocht","tag":"describir"},
  {"cue":"tu versión","text":"Hoy llevo ___ . Es ___ (color) y de ___ .","sub":"jouw versie — vul in en zeg ze","tag":"describir",
   "tip":"Ahora describe la ropa de un amigo. <span class='nl'>beschrijf nu de kleren van een vriend(in).</span>"}]}})

print("\n20 U6-spellen geschreven (10 templates: memory·match·classify·cloze·tetris·order·point·sim·speak).")
print("Pools >=12 per game; options.rounds lager => herspeling geeft een andere reeks.")
