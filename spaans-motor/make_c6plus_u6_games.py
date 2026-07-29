#!/usr/bin/env python3
# Motor-content-JSON's voor C6+ · U6 «Cuando era pequeño» (infancia · imperfecto · contraste · comparativos).
# Templates: memory·match·classify·cloze·tetris·order·point·speak. Pools >=12; rounds lager => andere reeks.
# Imperfecto-vormen nagerekend (3 irr: era/iba/veía). Slug-prefix = es-c6plus-u6-.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")
def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2)); print("wrote", os.path.basename(p))
G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0","magenta":"#B4309A"}
PRE = "es-c6plus-u6-"

# 1 · MEMORY — infancia ES ↔ NL (pool 14)
w({"id":PRE+"infancia-memoria","title":"Memoria de la infancia","subtitle":"U6 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: infancia + vertaling","pairs":[
  {"a":"el recuerdo","b":"de herinnering"},{"a":"el juguete","b":"het speelgoed"},{"a":"la escuela","b":"de school"},
  {"a":"el patio","b":"de speelplaats"},{"a":"el recreo","b":"de pauze"},{"a":"la maestra","b":"de juf"},
  {"a":"los abuelos","b":"de grootouders"},{"a":"el pueblo","b":"het dorp"},{"a":"la mascota","b":"het huisdier"},
  {"a":"jugar","b":"spelen"},{"a":"soñar","b":"dromen"},{"a":"la infancia","b":"de kindertijd"},
  {"a":"el vecino","b":"de buur"},{"a":"aprender","b":"leren"}]}})

# 2 · MEMORY — antes/ahora + adjetivos (pool 12)
w({"id":PRE+"antes-memoria","title":"Memoria: antes y ahora","subtitle":"U6 · koppel het woord aan de vertaling",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: tiempo + vertaling","pairs":[
  {"a":"antes","b":"vroeger"},{"a":"ahora","b":"nu"},{"a":"ya no","b":"niet meer"},
  {"a":"todavía","b":"nog steeds"},{"a":"siempre","b":"altijd"},{"a":"a menudo","b":"vaak"},
  {"a":"feliz","b":"gelukkig"},{"a":"tranquilo","b":"rustig"},{"a":"diferente","b":"anders"},
  {"a":"echar de menos","b":"missen"},{"a":"la época","b":"het tijdperk"},{"a":"el lugar","b":"de plek"}]}})

# 3 · MATCH — infinitivo ↔ imperfecto (yo/él) (pool 14)
w({"id":PRE+"verbo-imperfecto","title":"Verbo e imperfecto","subtitle":"U6 · koppel de infinitief aan het imperfecto",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind de infinitief met het imperfecto (yo/él)","pairs":[
  {"a":"jugar","b":"jugaba"},{"a":"comer","b":"comía"},{"a":"vivir","b":"vivía"},
  {"a":"ser","b":"era ⭐"},{"a":"ir","b":"iba ⭐"},{"a":"ver","b":"veía ⭐"},
  {"a":"tener","b":"tenía"},{"a":"hacer","b":"hacía"},{"a":"haber","b":"había"},
  {"a":"estudiar","b":"estudiaba"},{"a":"soñar","b":"soñaba"},{"a":"vivir (nos.)","b":"vivíamos"},
  {"a":"cuidar","b":"cuidaba"},{"a":"aprender","b":"aprendía"}]}})

# 4 · CLASSIFY — ¿indefinido o imperfecto? (pool 16, rounds 10)
w({"id":PRE+"indef-imperf","title":"¿indefinido o imperfecto?","subtitle":"U6 · afgerond feit of achtergrond/gewoonte?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"Is het een afgerond feit (indefinido) of achtergrond/gewoonte (imperfecto)?","categories":[
  {"id":"indef","label":"indefinido<br><small>un día, de repente</small>","glaze":G["purple"]},
  {"id":"imperf","label":"imperfecto<br><small>siempre, era, jugaba</small>","glaze":G["teal"]}],
 "items":[
  {"stimulus":"De pequeño jugaba en la calle.","answer":"imperf","tag":"imperf","sub":"gewoonte"},
  {"stimulus":"Un día empezó a llover.","answer":"indef","tag":"indef","sub":"un día → feit"},
  {"stimulus":"Era de noche y llovía.","answer":"imperf","tag":"imperf","sub":"decor"},
  {"stimulus":"De repente, sonó el teléfono.","answer":"indef","tag":"indef","sub":"de repente → feit"},
  {"stimulus":"Siempre íbamos al parque.","answer":"imperf","tag":"imperf","sub":"siempre → gewoonte"},
  {"stimulus":"Ayer llegó mi abuela.","answer":"indef","tag":"indef","sub":"ayer + feit"},
  {"stimulus":"Mi casa era de adobe.","answer":"imperf","tag":"imperf","sub":"beschrijving"},
  {"stimulus":"En 2010 nació mi hermano.","answer":"indef","tag":"indef","sub":"en 2010 → feit"},
  {"stimulus":"Todos los días comía pan.","answer":"imperf","tag":"imperf","sub":"gewoonte"},
  {"stimulus":"Entonces ganó el partido.","answer":"indef","tag":"indef","sub":"feit"},
  {"stimulus":"Tenía cinco años.","answer":"imperf","tag":"imperf","sub":"beschrijving (leeftijd)"},
  {"stimulus":"Un día fuimos al circo.","answer":"indef","tag":"indef","sub":"un día → feit"},
  {"stimulus":"Mi abuela era muy amable.","answer":"imperf","tag":"imperf","sub":"beschrijving"},
  {"stimulus":"De repente, alguien gritó.","answer":"indef","tag":"indef","sub":"feit"},
  {"stimulus":"A menudo visitaba a mis primos.","answer":"imperf","tag":"imperf","sub":"gewoonte"},
  {"stimulus":"Aquel día conocí a Nina.","answer":"indef","tag":"indef","sub":"aquel día → feit"}]}})

# 5 · CLASSIFY — ¿más, menos o tan? (pool 15, rounds 10)
w({"id":PRE+"comparar","title":"¿más, menos o tan?","subtitle":"U6 · welk vergelijkingswoord?",
 "lang":"es","template":"classify","options":{"rounds":10,"audio":False},
 "classify":{"prompt":"más/menos … QUE of tan … COMO?","categories":[
  {"id":"masque","label":"más/menos … que","glaze":G["blue"]},
  {"id":"tancomo","label":"tan … como","glaze":G["green"]}],
 "items":[
  {"stimulus":"La ciudad es ___ grande ___ el pueblo. (groter)","answer":"masque","tag":"masque","sub":"más…que"},
  {"stimulus":"Es ___ alto ___ yo. (even)","answer":"tancomo","tag":"tancomo","sub":"tan…como"},
  {"stimulus":"Hoy hace ___ calor ___ ayer. (meer)","answer":"masque","tag":"masque","sub":"más…que"},
  {"stimulus":"Es ___ rápido ___ un tren. (even)","answer":"tancomo","tag":"tancomo","sub":"tan…como"},
  {"stimulus":"Antes era ___ tímido ___ ahora. (minder)","answer":"masque","tag":"masque","sub":"menos…que"},
  {"stimulus":"Mi perro es ___ grande ___ el tuyo. (even)","answer":"tancomo","tag":"tancomo","sub":"tan…como"},
  {"stimulus":"El pueblo es ___ tranquilo ___ la ciudad. (rustiger)","answer":"masque","tag":"masque","sub":"más…que"},
  {"stimulus":"Soy ___ alto ___ mi hermano. (even)","answer":"tancomo","tag":"tancomo","sub":"tan…como"},
  {"stimulus":"Este libro es ___ interesante ___ ese. (meer)","answer":"masque","tag":"masque","sub":"más…que"},
  {"stimulus":"Es ___ divertido ___ un juego. (even)","answer":"tancomo","tag":"tancomo","sub":"tan…como"},
  {"stimulus":"Hoy estoy ___ cansado ___ ayer. (minder)","answer":"masque","tag":"masque","sub":"menos…que"},
  {"stimulus":"Nina es ___ simpática ___ Diego. (even)","answer":"tancomo","tag":"tancomo","sub":"tan…como"},
  {"stimulus":"La casa nueva es ___ cara ___ la vieja. (duurder)","answer":"masque","tag":"masque","sub":"más…que"},
  {"stimulus":"Corre ___ rápido ___ yo. (even)","answer":"tancomo","tag":"tancomo","sub":"tan…como"},
  {"stimulus":"Antes había ___ coches ___ ahora. (minder)","answer":"masque","tag":"masque","sub":"menos…que"}]}})

# 6 · CLOZE — imperfecto (VERPLICHT, nagerekend) (pool 18, rounds 12)
w({"id":PRE+"imperfecto","title":"Completa: el imperfecto","subtitle":"U6 · ¿cómo era todo?",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm van het imperfecto","items":[
  {"stimulus":"De pequeña, Nina ___ (vivir) en un pueblo.","options":["vivía","vivió","vive"],"answer":"vivía","tag":"im","sub":"vivir → vivía"},
  {"stimulus":"(Ella) ___ (ser) muy tímida.","options":["era","fue","es"],"answer":"era","tag":"im","sub":"ser → era"},
  {"stimulus":"Todos los días ___ (ir, ella) a la escuela.","options":["iba","fue","va"],"answer":"iba","tag":"im","sub":"ir → iba"},
  {"stimulus":"(Ella) ___ (tener) un perro.","options":["tenía","tuvo","tiene"],"answer":"tenía","tag":"im","sub":"tener → tenía"},
  {"stimulus":"(Yo) ___ (jugar) en el patio.","options":["jugaba","jugué","juego"],"answer":"jugaba","tag":"im","sub":"jugar → jugaba"},
  {"stimulus":"Nosotros ___ (comer) en casa de la abuela.","options":["comíamos","comimos","comemos"],"answer":"comíamos","tag":"im","sub":"comer → comíamos"},
  {"stimulus":"Por la tarde (yo) ___ (ver) dibujos.","options":["veía","vi","veo"],"answer":"veía","tag":"im","sub":"ver → veía"},
  {"stimulus":"Mis amigos ___ (soñar) con ser futbolistas.","options":["soñaban","soñaron","sueñan"],"answer":"soñaban","tag":"im","sub":"soñar → soñaban"},
  {"stimulus":"___ (haber) menos coches antes.","options":["Había","Hubo","Hay"],"answer":"Había","tag":"im","sub":"haber → había"},
  {"stimulus":"El pueblo ___ (ser) tranquilo.","options":["era","fue","es"],"answer":"era","tag":"im","sub":"ser → era"},
  {"stimulus":"(Nosotros) ___ (ir) al parque.","options":["íbamos","fuimos","vamos"],"answer":"íbamos","tag":"im","sub":"ir → íbamos"},
  {"stimulus":"Mi abuela ___ (hacer) pan cada día.","options":["hacía","hizo","hace"],"answer":"hacía","tag":"im","sub":"hacer → hacía"},
  {"stimulus":"(Yo) ___ (tener) cinco años.","options":["tenía","tuve","tengo"],"answer":"tenía","tag":"im","sub":"tener → tenía"},
  {"stimulus":"¿(Tú) ___ (vivir) en la ciudad?","options":["vivías","viviste","vives"],"answer":"vivías","tag":"im","sub":"tú → vivías"},
  {"stimulus":"Los niños ___ (jugar) en la calle.","options":["jugaban","jugaron","juegan"],"answer":"jugaban","tag":"im","sub":"ellos → jugaban"},
  {"stimulus":"(Yo) ___ (aprender) a leer.","options":["aprendía","aprendí","aprendo"],"answer":"aprendía","tag":"im","sub":"aprender → aprendía"},
  {"stimulus":"Mi maestra ___ (ser) amable.","options":["era","fue","es"],"answer":"era","tag":"im","sub":"ser → era"},
  {"stimulus":"(Nosotros) ___ (cuidar) a los abuelos.","options":["cuidábamos","cuidamos","cuidaron"],"answer":"cuidábamos","tag":"im","sub":"cuidar → cuidábamos"}]}})

# 7 · CLOZE — contraste indef/imperf (pool 14, rounds 10)
w({"id":PRE+"contraste","title":"Completa: indef ↔ imperf","subtitle":"U6 · achtergrond of gebeurtenis?",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies de juiste tijd (achtergrond → imperfecto, gebeurtenis → indefinido)","items":[
  {"stimulus":"(Yo) ___ en el patio cuando llegó mi madre.","options":["jugaba","jugué","juego"],"answer":"jugaba","tag":"ct","sub":"achtergrond → imperfecto"},
  {"stimulus":"Jugaba cuando, de repente, ___ a llover.","options":["empezó","empezaba","empieza"],"answer":"empezó","tag":"ct","sub":"gebeurtenis → indefinido"},
  {"stimulus":"___ de noche y llovía.","options":["Era","Fue","Es"],"answer":"Era","tag":"ct","sub":"decor → imperfecto"},
  {"stimulus":"Nina vivía en Cusco cuando ___ su hermano.","options":["nació","nacía","nace"],"answer":"nació","tag":"ct","sub":"gebeurtenis → indefinido"},
  {"stimulus":"Todos los días ___ al parque.","options":["iba","fui","voy"],"answer":"iba","tag":"ct","sub":"gewoonte → imperfecto"},
  {"stimulus":"Ayer ___ a mi abuela.","options":["visité","visitaba","visito"],"answer":"visité","tag":"ct","sub":"ayer → indefinido"},
  {"stimulus":"Mientras (yo) ___, sonó el teléfono.","options":["estudiaba","estudié","estudio"],"answer":"estudiaba","tag":"ct","sub":"mientras → imperfecto"},
  {"stimulus":"Un día ___ un concurso de dibujo.","options":["gané","ganaba","gano"],"answer":"gané","tag":"ct","sub":"un día → indefinido"},
  {"stimulus":"La casa ___ grande y bonita.","options":["era","fue","es"],"answer":"era","tag":"ct","sub":"beschrijving → imperfecto"},
  {"stimulus":"De repente, ___ mi tío con una bici.","options":["llegó","llegaba","llega"],"answer":"llegó","tag":"ct","sub":"de repente → indefinido"},
  {"stimulus":"Siempre ___ (nosotros) en la calle.","options":["jugábamos","jugamos","jugaron"],"answer":"jugábamos","tag":"ct","sub":"siempre → imperfecto"},
  {"stimulus":"Aquel verano ___ a Perú.","options":["viajé","viajaba","viajo"],"answer":"viajé","tag":"ct","sub":"aquel verano → indefinido"},
  {"stimulus":"(Ella) ___ tímida de pequeña.","options":["era","fue","es"],"answer":"era","tag":"ct","sub":"beschrijving → imperfecto"},
  {"stimulus":"Entonces ___ (ellos) la casa.","options":["vendieron","vendían","venden"],"answer":"vendieron","tag":"ct","sub":"gebeurtenis → indefinido"}]}})

# 8 · TETRIS — imperfecto: -aba / -ía / irregular (pool 16)
w({"id":PRE+"imperf-tetris","title":"Imperfecto: topos","subtitle":"U6 · aporrea la forma correcta · mep de juiste vorm",
 "lang":"es","template":"mole","options":{"rounds":16,"audio":False},
 "classify":{"categories":[
  {"id":"aba","label":"-aba (-ar)","glaze":G["blue"]},{"id":"ia","label":"-ía (-er/-ir)","glaze":G["green"]},
  {"id":"irr","label":"era/iba/veía","glaze":G["magenta"]}],
 "items":[
  {"stimulus":"jugar","answer":"aba","tag":"aba","sub":"jugaba"},{"stimulus":"comer","answer":"ia","tag":"ia","sub":"comía"},
  {"stimulus":"ser","answer":"irr","tag":"irr","sub":"era"},{"stimulus":"vivir","answer":"ia","tag":"ia","sub":"vivía"},
  {"stimulus":"ir","answer":"irr","tag":"irr","sub":"iba"},{"stimulus":"estudiar","answer":"aba","tag":"aba","sub":"estudiaba"},
  {"stimulus":"ver","answer":"irr","tag":"irr","sub":"veía"},{"stimulus":"tener","answer":"ia","tag":"ia","sub":"tenía"},
  {"stimulus":"soñar","answer":"aba","tag":"aba","sub":"soñaba"},{"stimulus":"hacer","answer":"ia","tag":"ia","sub":"hacía"},
  {"stimulus":"cuidar","answer":"aba","tag":"aba","sub":"cuidaba"},{"stimulus":"aprender","answer":"ia","tag":"ia","sub":"aprendía"},
  {"stimulus":"jugar (nos.)","answer":"aba","tag":"aba","sub":"jugábamos"},{"stimulus":"salir","answer":"ia","tag":"ia","sub":"salía"},
  {"stimulus":"cantar","answer":"aba","tag":"aba","sub":"cantaba"},{"stimulus":"leer","answer":"ia","tag":"ia","sub":"leía"}]}})

# 9 · ORDER — ordena el recuerdo / la frase (8 rondes)
w({"id":PRE+"recuerdo-order","title":"Ordena la frase","subtitle":"U6 · zet het verhaal/de zin in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik in de logische volgorde","rounds":[
  {"tag":"imperf","sub":"beschrijving","items":[
    {"label":"De pequeña","key":1},{"label":"Nina","key":2},{"label":"vivía","key":3},{"label":"en un pueblo.","key":4}]},
  {"tag":"contraste","sub":"achtergrond + gebeurtenis","items":[
    {"label":"Jugaba en el patio","key":1},{"label":"cuando,","key":2},{"label":"de repente,","key":3},{"label":"empezó a llover.","key":4}]},
  {"tag":"comparar","sub":"vergelijking","items":[
    {"label":"El pueblo","key":1},{"label":"era más","key":2},{"label":"tranquilo","key":3},{"label":"que la ciudad.","key":4}]},
  {"tag":"relativo","sub":"que","items":[
    {"label":"El niño","key":1},{"label":"que","key":2},{"label":"jugaba en la calle","key":3},{"label":"era yo.","key":4}]},
  {"tag":"imperf","sub":"gewoonte","items":[
    {"label":"Todos los días","key":1},{"label":"íbamos","key":2},{"label":"al parque","key":3},{"label":"a jugar.","key":4}]},
  {"tag":"comparar","sub":"tan … como","items":[
    {"label":"Mi hermano","key":1},{"label":"era tan","key":2},{"label":"alto","key":3},{"label":"como yo.","key":4}]},
  {"tag":"contraste","sub":"un día","items":[
    {"label":"Un día,","key":1},{"label":"mientras comíamos,","key":2},{"label":"llegó","key":3},{"label":"mi tío.","key":4}]},
  {"tag":"antes","sub":"antes ↔ ahora","items":[
    {"label":"Antes","key":1},{"label":"vivía en un pueblo;","key":2},{"label":"en cambio,","key":3},{"label":"ahora vivo en la ciudad.","key":4}]}]}})

# 10 · POINT — señala (repaso gemengd) (10 rondes)
w({"id":PRE+"senala","title":"Señala","subtitle":"U6 · klik het juiste antwoord",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het gevraagde item","mode":"one","rounds":[
  {"tag":"inf","sub":"señala algo de la escuela","targets":[
    {"label":"el patio","hit":True},{"label":"los abuelos"},{"label":"el juguete"},{"label":"antes"}]},
  {"tag":"inf","sub":"señala algo de la infancia","targets":[
    {"label":"el juguete","hit":True},{"label":"la maestra"},{"label":"el vecino"},{"label":"la época"}]},
  {"tag":"im","sub":"ser → imperfecto (él)","targets":[
    {"label":"era","hit":True},{"label":"fue"},{"label":"es"},{"label":"sería"}]},
  {"tag":"im","sub":"ir → imperfecto (yo)","targets":[
    {"label":"iba","hit":True},{"label":"fui"},{"label":"voy"},{"label":"iría"}]},
  {"tag":"im","sub":"«jugaba» = ?","targets":[
    {"label":"hij/zij speelde (gewoonte)","hit":True},{"label":"hij speelde één keer"},{"label":"hij speelt"},{"label":"hij zal spelen"}]},
  {"tag":"ct","sub":"achtergrond of feit? «Era de noche»","targets":[
    {"label":"imperfecto (achtergrond)","hit":True},{"label":"indefinido (feit)"},{"label":"presente"},{"label":"futuro"}]},
  {"tag":"comp","sub":"«groter dan» = ?","targets":[
    {"label":"más grande que","hit":True},{"label":"tan grande como"},{"label":"menos grande que"},{"label":"el más grande"}]},
  {"tag":"comp","sub":"«beter dan» (irregular) = ?","targets":[
    {"label":"mejor que","hit":True},{"label":"más bueno que"},{"label":"tan bueno como"},{"label":"peor que"}]},
  {"tag":"rel","sub":"«de plek waar» = ?","targets":[
    {"label":"el lugar donde","hit":True},{"label":"el lugar que"},{"label":"el lugar como"},{"label":"el lugar cuando"}]},
  {"tag":"antes","sub":"«niet meer» = ?","targets":[
    {"label":"ya no","hit":True},{"label":"todavía"},{"label":"siempre"},{"label":"a menudo"}]}]}})

# 11 · SPEAK repeat — mi infancia (8 items)
w({"id":PRE+"repite-infancia","title":"Escucha y repite: mi infancia","subtitle":"U6 · escucha, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite en voz alta · grábate ⏺","items":[
  {"text":"De pequeña vivía en un pueblo.","sub":"als kind woonde ik in een dorp","tag":"im","tip":"¡Bien! Ahora dilo sin leer."},
  {"text":"Tenía un perro y jugaba en la calle.","sub":"ik had een hond en speelde op straat","tag":"im"},
  {"text":"Todos los días iba a la escuela a pie.","sub":"elke dag ging ik te voet naar school","tag":"im"},
  {"text":"Mi abuela era muy amable.","sub":"mijn oma was heel lief","tag":"im"},
  {"text":"Jugaba cuando, de repente, empezó a llover.","sub":"ik speelde toen het plots begon te regenen","tag":"ct"},
  {"text":"Antes el pueblo era más tranquilo que la ciudad.","sub":"vroeger was het dorp rustiger dan de stad","tag":"comp"},
  {"text":"El niño que jugaba en el patio era yo.","sub":"het kind dat op de speelplaats speelde was ik","tag":"rel"},
  {"text":"Creo que antes era mejor.","sub":"ik denk dat het vroeger beter was","tag":"opinion"}]}})

# 12 · SPEAK voicemessage — infancia + comparación (3 items)
w({"id":PRE+"mensaje-infancia","title":"Mensaje de voz: mi infancia","subtitle":"U6 · neem een spraakbericht op",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz (30–40 s)","items":[
  {"text":"Cuenta cómo era tu infancia (usa 3 veces el imperfecto: vivía, tenía, jugaba).","cue":"mi infancia","tag":"im",
   "sub":"gebruik: de pequeño/a vivía… tenía… iba…",
   "tip":"3× het imperfecto (achtergrond/gewoonte)? Neem opnieuw op."},
  {"text":"Cuenta algo que pasó un día (indefinido) con el fondo (imperfecto).","cue":"un recuerdo","tag":"ct",
   "sub":"gebruik: Era… cuando, de repente, … pasó",
   "tip":"achtergrond (imperf.) + gebeurtenis (indef.)? Herneem."},
  {"text":"Compara antes y ahora y da tu opinión (más/menos… que · creo que antes…).","cue":"antes ↔ ahora","tag":"comp",
   "sub":"gebruik: antes era más… que ahora · creo que…",
   "tip":"una comparación + una opinión? Herneem."}]}})

print("\n12 C6+·U6-spellen geschreven (8 templates: memory·match·classify·cloze·tetris·order·point·speak).")
