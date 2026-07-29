#!/usr/bin/env python3
# Genereert de 15 motor-content-JSON's voor C5 · U1 «¿Quién eres?».
# Templates: match·memory·classify·cloze·tetris·order·tap  (receptief -> productief).
# Grammaticale vormen (ser, presente) zijn nagerekend/geverifieerd; género & presente-reg via generator.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2))
    print("wrote", os.path.basename(p))

G = {  # cursorkleuren voor categorie-glazuur (azulejo behoudt eigen thema; dit is chip-tint)
 "blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0"}

# 1 · MATCH — país ↔ nacionalidad (gentilicio)  [receptief]
w({"id":"es-u1-pais-nacionalidad","title":"País y nacionalidad","subtitle":"U1 · koppel land aan nationaliteit",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind elk land met de juiste nationaliteit (gentilicio)","pairs":[
  {"a":"Bélgica","b":"belga"},{"a":"España","b":"español"},{"a":"México","b":"mexicano"},
  {"a":"Argentina","b":"argentino"},{"a":"Colombia","b":"colombiano"},{"a":"Perú","b":"peruano"},
  {"a":"Francia","b":"francés"},{"a":"Alemania","b":"alemán"},{"a":"Italia","b":"italiano"},
  {"a":"Portugal","b":"portugués"},{"a":"Estados Unidos","b":"estadounidense"},{"a":"Brasil","b":"brasileño"},
  {"a":"Japón","b":"japonés"},{"a":"Marruecos","b":"marroquí"},{"a":"Canadá","b":"canadiense"},
  {"a":"China","b":"chino"},{"a":"los Países Bajos","b":"neerlandés"},{"a":"Chile","b":"chileno"}]}})

# 2 · MEMORY — datos personales ES ↔ NL  [receptief]
w({"id":"es-u1-datos-memoria","title":"Memoria de los datos","subtitle":"U1 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om en zoek het woord + de vertaling","pairs":[
  {"a":"el nombre","b":"de voornaam"},{"a":"el apellido","b":"de achternaam"},{"a":"la edad","b":"de leeftijd"},
  {"a":"el país","b":"het land"},{"a":"la nacionalidad","b":"de nationaliteit"},{"a":"la dirección","b":"het adres"},
  {"a":"la ciudad","b":"de stad"},{"a":"el idioma","b":"de taal"},{"a":"el correo","b":"het e-mailadres"},
  {"a":"el teléfono","b":"het telefoonnummer"},{"a":"la firma","b":"de handtekening"},{"a":"el curso","b":"het leerjaar"}]}})

# 3 · CLASSIFY — ser vs tener (edad-valstrik)  [onderscheiden]
w({"id":"es-u1-ser-tener","title":"¿SER o TENER?","subtitle":"U1 · welk werkwoord? Let op de leeftijd-valstrik",
 "lang":"es","template":"classify","options":{"rounds":14,"audio":False},
 "classify":{"prompt":"Welk werkwoord past? (leeftijd = TENER, niet SER!)","categories":[
  {"id":"ser","label":"SER<br><small>zijn / afkomst</small>","glaze":G["amber"]},
  {"id":"tener","label":"TENER<br><small>hebben / leeftijd</small>","glaze":G["green"]}],
 "items":[
  {"stimulus":"Yo ___ de Bélgica.","answer":"ser","tag":"ser","sub":"soy — afkomst"},
  {"stimulus":"Yo ___ 15 años.","answer":"tener","tag":"tener","sub":"tengo — leeftijd!"},
  {"stimulus":"Ella ___ española.","answer":"ser","tag":"ser","sub":"es — nationaliteit"},
  {"stimulus":"¿Cuántos años ___?","answer":"tener","tag":"tener","sub":"tienes — leeftijd"},
  {"stimulus":"Nosotros ___ estudiantes.","answer":"ser","tag":"ser","sub":"somos"},
  {"stimulus":"Mi hermano ___ 12 años.","answer":"tener","tag":"tener","sub":"tiene — leeftijd"},
  {"stimulus":"Tú ___ de México, ¿verdad?","answer":"ser","tag":"ser","sub":"eres — afkomst"},
  {"stimulus":"Yo ___ un correo nuevo.","answer":"tener","tag":"tener","sub":"tengo — bezit"},
  {"stimulus":"¿De dónde ___ vosotros?","answer":"ser","tag":"ser","sub":"sois — afkomst"},
  {"stimulus":"Lucía ___ 16 años.","answer":"tener","tag":"tener","sub":"tiene — leeftijd"},
  {"stimulus":"El profesor ___ simpático.","answer":"ser","tag":"ser","sub":"es — eigenschap"},
  {"stimulus":"Ellos ___ dos apellidos.","answer":"tener","tag":"tener","sub":"tienen — bezit"},
  {"stimulus":"Madrid ___ la capital.","answer":"ser","tag":"ser","sub":"es"},
  {"stimulus":"Yo ___ una pregunta.","answer":"tener","tag":"tener","sub":"tengo — bezit"}]}})

# 4 · CLASSIFY — forma de SER -> persona  (ser nagerekend: soy/eres/es/somos/sois/son)  [vorm]
w({"id":"es-u1-ser-persona","title":"El verbo SER","subtitle":"U1 · welke persoon hoort bij deze vorm van ser?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Bij welke persoon hoort de vorm van SER?","categories":[
  {"id":"yo","label":"yo","glaze":G["red"]},{"id":"tu","label":"tú","glaze":G["amber"]},
  {"id":"el","label":"él / ella","glaze":G["green"]},{"id":"nos","label":"nosotros","glaze":G["blue"]},
  {"id":"vos","label":"vosotros","glaze":G["purple"]},{"id":"ellos","label":"ellos/-as","glaze":G["teal"]}],
 "items":[
  {"stimulus":"soy","answer":"yo","tag":"yo","sub":"yo soy"},{"stimulus":"eres","answer":"tu","tag":"tu","sub":"tú eres"},
  {"stimulus":"es","answer":"el","tag":"el","sub":"él/ella es"},{"stimulus":"somos","answer":"nos","tag":"nos","sub":"nosotros somos"},
  {"stimulus":"sois","answer":"vos","tag":"vos","sub":"vosotros sois"},{"stimulus":"son","answer":"ellos","tag":"ellos","sub":"ellos son"},
  {"stimulus":"soy","answer":"yo","tag":"yo","sub":"yo soy"},{"stimulus":"es","answer":"el","tag":"el","sub":"él/ella es"},
  {"stimulus":"eres","answer":"tu","tag":"tu","sub":"tú eres"},{"stimulus":"son","answer":"ellos","tag":"ellos","sub":"ellos son"},
  {"stimulus":"somos","answer":"nos","tag":"nos","sub":"nosotros somos"},{"stimulus":"sois","answer":"vos","tag":"vos","sub":"vosotros sois"}]}})

# 5 · TETRIS — presente regular (generator: nagerekend)  [productief]
w({"id":"es-u1-presente-regular","title":"Presente regular","subtitle":"U1 · laat de vorm in de juiste persoon vallen",
 "lang":"es","template":"tetris","options":{"rows":9,"speed":1250,"audio":False},
 "generator":{"kind":"conjugation","tense":"pres","pool":"reg","persons":["yo","tu","el","nos","vos","ellos"]},
 "classify":{"categories":[
  {"id":"yo","label":"yo","glaze":G["red"]},{"id":"tu","label":"tú","glaze":G["amber"]},
  {"id":"el","label":"él/ella","glaze":G["green"]},{"id":"nos","label":"nosotros","glaze":G["blue"]},
  {"id":"vos","label":"vosotros","glaze":G["purple"]},{"id":"ellos","label":"ellos","glaze":G["teal"]}]}})

# 6 · CLASSIFY — infinitivo -> clase -ar/-er/-ir  [onderscheiden]
w({"id":"es-u1-ar-er-ir","title":"-ar · -er · -ir","subtitle":"U1 · sorteer de infinitieven per klasse",
 "lang":"es","template":"classify","options":{"rounds":15,"audio":False},
 "classify":{"prompt":"Welke vervoegingsklasse? Kijk naar de uitgang.","categories":[
  {"id":"ar","label":"-ar","glaze":G["blue"]},{"id":"er","label":"-er","glaze":G["amber"]},{"id":"ir","label":"-ir","glaze":G["green"]}],
 "items":[
  {"stimulus":"hablar","answer":"ar","tag":"ar","sub":"spreken"},{"stimulus":"estudiar","answer":"ar","tag":"ar","sub":"studeren"},
  {"stimulus":"trabajar","answer":"ar","tag":"ar","sub":"werken"},{"stimulus":"llamar","answer":"ar","tag":"ar","sub":"noemen/bellen"},
  {"stimulus":"rellenar","answer":"ar","tag":"ar","sub":"invullen"},{"stimulus":"aprender","answer":"er","tag":"er","sub":"leren"},
  {"stimulus":"comer","answer":"er","tag":"er","sub":"eten"},{"stimulus":"leer","answer":"er","tag":"er","sub":"lezen"},
  {"stimulus":"beber","answer":"er","tag":"er","sub":"drinken"},{"stimulus":"comprender","answer":"er","tag":"er","sub":"begrijpen"},
  {"stimulus":"vivir","answer":"ir","tag":"ir","sub":"wonen/leven"},{"stimulus":"escribir","answer":"ir","tag":"ir","sub":"schrijven"},
  {"stimulus":"abrir","answer":"ir","tag":"ir","sub":"openen"},{"stimulus":"recibir","answer":"ir","tag":"ir","sub":"ontvangen"},
  {"stimulus":"decidir","answer":"ir","tag":"ir","sub":"beslissen"}]}})

# 7 · CLOZE — interrogativos  [gestuurd]
w({"id":"es-u1-interrogativos","title":"Palabras interrogativas","subtitle":"U1 · kies het juiste vraagwoord",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Vul het juiste vraagwoord in","items":[
  {"stimulus":"¿___ te llamas?","options":["Cómo","Dónde","Quién"],"answer":"Cómo","tag":"q","sub":"Hoe heet je?"},
  {"stimulus":"¿De ___ eres?","options":["dónde","cómo","qué"],"answer":"dónde","tag":"q","sub":"Waarvandaan ben je?"},
  {"stimulus":"¿___ vives?","options":["Dónde","Quién","Cuál"],"answer":"Dónde","tag":"q","sub":"Waar woon je?"},
  {"stimulus":"¿Cuántos ___ tienes?","options":["años","edad","tiempo"],"answer":"años","tag":"q","sub":"Hoe oud ben je?"},
  {"stimulus":"¿___ es tu correo?","options":["Cuál","Qué","Cómo"],"answer":"Cuál","tag":"q","sub":"Wat is je e-mail?"},
  {"stimulus":"¿___ es ella?","options":["Quién","Dónde","Cuál"],"answer":"Quién","tag":"q","sub":"Wie is zij?"},
  {"stimulus":"¿___ idiomas hablas?","options":["Qué","Cuál","Cómo"],"answer":"Qué","tag":"q","sub":"Welke talen spreek je?"},
  {"stimulus":"¿___ se escribe tu apellido?","options":["Cómo","Qué","Quién"],"answer":"Cómo","tag":"q","sub":"Hoe schrijf je …?"},
  {"stimulus":"¿___ es tu número de teléfono?","options":["Cuál","Quién","Dónde"],"answer":"Cuál","tag":"q","sub":"Wat is je nummer?"},
  {"stimulus":"¿De ___ país eres?","options":["qué","dónde","cómo"],"answer":"qué","tag":"q","sub":"Uit welk land?"}]}})

# 8 · CLASSIFY — mayúscula vs minúscula (país vs gentilicio)  [ortografía]
w({"id":"es-u1-mayuscula-minuscula","title":"¿Mayúscula o minúscula?","subtitle":"U1 · landen mét hoofdletter, nationaliteiten zónder",
 "lang":"es","template":"classify","options":{"rounds":14,"audio":False},
 "classify":{"prompt":"Hoofdletter (país) of kleine letter (nacionalidad/idioma)?","categories":[
  {"id":"may","label":"MAYÚSCULA<br><small>país (España)</small>","glaze":G["blue"]},
  {"id":"min","label":"minúscula<br><small>gentilicio (español)</small>","glaze":G["green"]}],
 "items":[
  {"stimulus":"España","answer":"may","tag":"may","sub":"land → hoofdletter"},
  {"stimulus":"español","answer":"min","tag":"min","sub":"nationaliteit/taal → klein"},
  {"stimulus":"México","answer":"may","tag":"may","sub":"land → hoofdletter"},
  {"stimulus":"mexicano","answer":"min","tag":"min","sub":"nationaliteit → klein"},
  {"stimulus":"Bélgica","answer":"may","tag":"may","sub":"land → hoofdletter"},
  {"stimulus":"belga","answer":"min","tag":"min","sub":"nationaliteit → klein"},
  {"stimulus":"Francia","answer":"may","tag":"may","sub":"land → hoofdletter"},
  {"stimulus":"francés","answer":"min","tag":"min","sub":"nationaliteit → klein"},
  {"stimulus":"Colombia","answer":"may","tag":"may","sub":"land → hoofdletter"},
  {"stimulus":"colombiano","answer":"min","tag":"min","sub":"nationaliteit → klein"},
  {"stimulus":"Madrid","answer":"may","tag":"may","sub":"stad → hoofdletter"},
  {"stimulus":"neerlandés","answer":"min","tag":"min","sub":"taal → klein"},
  {"stimulus":"Perú","answer":"may","tag":"may","sub":"land → hoofdletter"},
  {"stimulus":"peruano","answer":"min","tag":"min","sub":"nationaliteit → klein"}]}})

# 9 · CLASSIFY — género el/la (generator: nagerekend)  [vorm]
w({"id":"es-u1-genero-articulo","title":"El o la","subtitle":"U1 · kies het juiste bepaald lidwoord",
 "lang":"es","template":"classify","options":{"rounds":18,"audio":False},
 "generator":{"kind":"gender"},
 "classify":{"prompt":"¿masculino (el) o femenino (la)?","categories":[
  {"id":"m","label":"el<br><small>masculino</small>","glaze":G["blue"]},
  {"id":"f","label":"la<br><small>femenino</small>","glaze":G["red"]}]}})

# 10 · MATCH — pregunta ↔ respuesta  [interactie]
w({"id":"es-u1-pregunta-respuesta","title":"Pregunta y respuesta","subtitle":"U1 · koppel de vraag aan het juiste antwoord",
 "lang":"es","template":"match","options":{"chunk":5,"audio":False},
 "match":{"prompt":"Verbind elke vraag met het passende antwoord","pairs":[
  {"a":"¿Cómo te llamas?","b":"Me llamo Leo."},
  {"a":"¿De dónde eres?","b":"Soy de Bélgica."},
  {"a":"¿Dónde vives?","b":"Vivo en Gante."},
  {"a":"¿Cuántos años tienes?","b":"Tengo 15 años."},
  {"a":"¿Cuál es tu correo?","b":"Es leo@mail.com."},
  {"a":"¿Qué idiomas hablas?","b":"Hablo dos idiomas."},
  {"a":"¿Quién es ella?","b":"Es Lucía, de Sevilla."},
  {"a":"¿Cuál es tu nacionalidad?","b":"Soy belga."}]}})

# 11 · ORDER — presentación op de juiste volgorde  [productief]
w({"id":"es-u1-presentacion-orden","title":"Ordena la presentación","subtitle":"U1 · zet de zelfvoorstelling in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik de zinnen in de logische volgorde van een presentación",
  "rounds":[
  {"tag":"pres","sub":"saluda → nombre → origen → edad → despedida","items":[
    {"label":"¡Hola! Buenos días.","key":1},{"label":"Me llamo Leo García.","key":2},
    {"label":"Soy de Bélgica, soy belga.","key":3},{"label":"Tengo 15 años.","key":4},{"label":"¡Encantado! Adiós.","key":5}]},
  {"tag":"pres","sub":"saluda → nombre → ciudad → idiomas → cierre","items":[
    {"label":"¡Buenas! ¿Qué tal?","key":1},{"label":"Me llamo Sara.","key":2},
    {"label":"Vivo en Amberes.","key":3},{"label":"Hablo neerlandés y español.","key":4},{"label":"¡Gracias!","key":5}]},
  {"tag":"pres","sub":"pregunta → nombre → origen → edad","items":[
    {"label":"¿Cómo te llamas?","key":1},{"label":"Me llamo Diego.","key":2},
    {"label":"Soy de México.","key":3},{"label":"Tengo 16 años.","key":4}]},
  {"tag":"pres","sub":"nombre → apellido → país → correo","items":[
    {"label":"Mi nombre es Nina.","key":1},{"label":"Mi apellido es Quispe.","key":2},
    {"label":"Soy de Perú.","key":3},{"label":"Mi correo es nina@mail.com.","key":4}]}]}})

# 12 · CLOZE — artículo indefinido un/una  [gestuurd]
w({"id":"es-u1-un-una","title":"¿un o una?","subtitle":"U1 · onbepaald lidwoord, let op het geslacht",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies un (m.) of una (f.)","items":[
  {"stimulus":"___ ciudad","options":["una","un"],"answer":"una","tag":"a","sub":"la ciudad → una"},
  {"stimulus":"___ país","options":["un","una"],"answer":"un","tag":"a","sub":"el país → un"},
  {"stimulus":"___ pregunta","options":["una","un"],"answer":"una","tag":"a","sub":"la pregunta → una"},
  {"stimulus":"___ nombre","options":["un","una"],"answer":"un","tag":"a","sub":"el nombre → un"},
  {"stimulus":"___ dirección","options":["una","un"],"answer":"una","tag":"a","sub":"la dirección → una"},
  {"stimulus":"___ correo","options":["un","una"],"answer":"un","tag":"a","sub":"el correo → un"},
  {"stimulus":"___ nacionalidad","options":["una","un"],"answer":"una","tag":"a","sub":"la nacionalidad → una"},
  {"stimulus":"___ idioma","options":["un","una"],"answer":"un","tag":"a","sub":"el idioma → un (valstrik!)"},
  {"stimulus":"___ firma","options":["una","un"],"answer":"una","tag":"a","sub":"la firma → una"},
  {"stimulus":"___ apellido","options":["un","una"],"answer":"un","tag":"a","sub":"el apellido → un"}]}})

# 13 · MEMORY — bandera ↔ país  [receptief]
w({"id":"es-u1-bandera-pais","title":"Banderas","subtitle":"U1 · zoek de vlag bij het land",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes: vind de vlag bij het land","pairs":[
  {"a":"🇪🇸","b":"España"},{"a":"🇲🇽","b":"México"},{"a":"🇦🇷","b":"Argentina"},
  {"a":"🇨🇴","b":"Colombia"},{"a":"🇵🇪","b":"Perú"},{"a":"🇧🇪","b":"Bélgica"},
  {"a":"🇨🇱","b":"Chile"},{"a":"🇻🇪","b":"Venezuela"},{"a":"🇨🇺","b":"Cuba"},
  {"a":"🇪🇨","b":"Ecuador"},{"a":"🇵🇷","b":"Puerto Rico"},{"a":"🇬🇶","b":"Guinea Ecuatorial"}]}})

# 14 · TAP — sílaba tónica op U1-woorden (recycling U0)  [ortografía]
w({"id":"es-u1-tonica-datos","title":"La tónica de los datos","subtitle":"U1 · tik de sterke lettergreep (recyclen U0)",
 "lang":"es","template":"tap","options":{"rounds":14,"audio":False},
 "tap":{"prompt":"Tik de sílaba tónica (de sterke lettergreep)","joiner":"·","items":[
  {"parts":["pa","ís"],"answer":1,"tag":"aguda","sub":"país · hiato + tilde"},
  {"parts":["ciu","dad"],"answer":1,"tag":"aguda","sub":"ciudad"},
  {"parts":["na","cio","na","li","dad"],"answer":4,"tag":"aguda","sub":"nacionalidad"},
  {"parts":["e","dad"],"answer":1,"tag":"aguda","sub":"edad"},
  {"parts":["es","pa","ñol"],"answer":2,"tag":"aguda","sub":"español"},
  {"parts":["a","pe","lli","do"],"answer":2,"tag":"llana","sub":"apellido"},
  {"parts":["nom","bre"],"answer":0,"tag":"llana","sub":"nombre"},
  {"parts":["i","dio","ma"],"answer":1,"tag":"llana","sub":"idioma"},
  {"parts":["ar","gen","ti","na"],"answer":2,"tag":"llana","sub":"Argentina"},
  {"parts":["te","lé","fo","no"],"answer":1,"tag":"esdrujula","sub":"teléfono"},
  {"parts":["Mé","xi","co"],"answer":0,"tag":"esdrujula","sub":"México"},
  {"parts":["di","rec","ción"],"answer":2,"tag":"aguda","sub":"dirección"},
  {"parts":["Bél","gi","ca"],"answer":0,"tag":"esdrujula","sub":"Bélgica"},
  {"parts":["Pe","rú"],"answer":1,"tag":"aguda","sub":"Perú"}]}})

# 15 · CLOZE — ¿qué verbo? ser/vivir/tener/llamarse  [gestuurd]
w({"id":"es-u1-que-verbo","title":"¿Qué verbo?","subtitle":"U1 · kies het juiste werkwoord in de zin",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Welke werkwoordsvorm past in de zin?","items":[
  {"stimulus":"Me ___ Leo.","options":["llamo","soy","tengo"],"answer":"llamo","tag":"v","sub":"llamarse → me llamo"},
  {"stimulus":"___ de Bélgica.","options":["Soy","Tengo","Vivo"],"answer":"Soy","tag":"v","sub":"ser → afkomst"},
  {"stimulus":"___ en Gante.","options":["Vivo","Soy","Me llamo"],"answer":"Vivo","tag":"v","sub":"vivir → wonen"},
  {"stimulus":"___ 15 años.","options":["Tengo","Soy","Vivo"],"answer":"Tengo","tag":"v","sub":"tener → leeftijd"},
  {"stimulus":"¿Cómo te ___?","options":["llamas","eres","vives"],"answer":"llamas","tag":"v","sub":"llamarse"},
  {"stimulus":"¿De dónde ___?","options":["eres","tienes","vives"],"answer":"eres","tag":"v","sub":"ser → origen"},
  {"stimulus":"¿Dónde ___?","options":["vives","eres","tienes"],"answer":"vives","tag":"v","sub":"vivir"},
  {"stimulus":"Ella ___ española.","options":["es","tiene","vive"],"answer":"es","tag":"v","sub":"ser → nationaliteit"},
  {"stimulus":"Diego ___ en México.","options":["vive","es","tiene"],"answer":"vive","tag":"v","sub":"vivir"},
  {"stimulus":"Nosotros ___ estudiantes.","options":["somos","tenemos","vivimos"],"answer":"somos","tag":"v","sub":"ser"},
  {"stimulus":"¿Cuántos años ___?","options":["tienes","eres","vives"],"answer":"tienes","tag":"v","sub":"tener → leeftijd"},
  {"stimulus":"Mi amiga se ___ Sara.","options":["llama","es","tiene"],"answer":"llama","tag":"v","sub":"llamarse (3ª)"}]}})

# 16 · POINT — foutenjacht: klik het woord met de FOUTE hoofd-/kleine letter  [analyseren]
w({"id":"es-u1-caza-mayusculas","title":"Caza de mayúsculas","subtitle":"U1 · klik het woord dat verkeerd geschreven is",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het woord dat FOUT geschreven is","mode":"one","rounds":[
  {"tag":"orto","sub":"landen = hoofdletter, talen/nationaliteiten = klein","targets":[
    {"label":"España"},{"label":"Bélgica"},{"label":"Español","hit":True},{"label":"Madrid"}]},
  {"tag":"orto","sub":"nationaliteit met kleine letter","targets":[
    {"label":"belga"},{"label":"Mexicano","hit":True},{"label":"francés"},{"label":"peruano"}]},
  {"tag":"orto","sub":"talen met kleine letter","targets":[
    {"label":"neerlandés"},{"label":"español"},{"label":"Italiano","hit":True},{"label":"inglés"}]},
  {"tag":"orto","sub":"land = hoofdletter","targets":[
    {"label":"méxico","hit":True},{"label":"Colombia"},{"label":"Perú"},{"label":"Chile"}]},
  {"tag":"orto","sub":"stad = hoofdletter","targets":[
    {"label":"sevilla","hit":True},{"label":"Madrid"},{"label":"Barcelona"},{"label":"Cartagena"}]},
  {"tag":"orto","sub":"nationaliteit met kleine letter","targets":[
    {"label":"Argentino","hit":True},{"label":"chileno"},{"label":"cubano"},{"label":"colombiano"}]}]}})

# 17 · POINT — señala TODOS los países hispanohablantes  [receptief · cultura]
w({"id":"es-u1-senala-hispano","title":"Señala el mundo hispano","subtitle":"U1 · klik ALLE Spaanstalige landen",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik ALLE landen waar Spaans een officiële taal is","mode":"all","rounds":[
  {"tag":"hispano","sub":"3 hispanohablantes","targets":[
    {"label":"México","hit":True},{"label":"Brasil"},{"label":"Perú","hit":True},{"label":"Portugal"},{"label":"España","hit":True}]},
  {"tag":"hispano","sub":"3 hispanohablantes","targets":[
    {"label":"Francia"},{"label":"Colombia","hit":True},{"label":"Argentina","hit":True},{"label":"Italia"},{"label":"Chile","hit":True}]},
  {"tag":"hispano","sub":"let op: ook in Afrika!","targets":[
    {"label":"Guinea Ecuatorial","hit":True},{"label":"Marruecos"},{"label":"Cuba","hit":True},{"label":"Egipto"},{"label":"Bolivia","hit":True}]},
  {"tag":"hispano","sub":"2 hispanohablantes","targets":[
    {"label":"Alemania"},{"label":"Venezuela","hit":True},{"label":"los Países Bajos"},{"label":"Ecuador","hit":True}]}]}})

# 18 · SIM — preséntate (vrije productie, zachte check op bouwstenen)  [productief · comunicar]
w({"id":"es-u1-presentate","title":"¡Preséntate!","subtitle":"U1 · schrijf je voorstelling — met alle bouwstenen",
 "lang":"es","template":"sim","options":{"audio":False},
 "sim":{"prompt":"Tarea comunicativa · zich voorstellen","rounds":[
  {"scenario":"Preséntate a Lucía por chat.","tag":"pres","sub":"gebruik: me llamo · soy de · tengo … años","min":8,
   "need":[{"re":"me llamo","label":"me llamo …"},{"re":"soy de","label":"soy de …"},{"re":"tengo .*(años|año)","label":"tengo … años"}],
   "bank":["¡Hola!","Me llamo","Soy de","Bélgica","tengo","15 años","y","Encantado","Vivo en","Gante"],
   "model":"¡Hola! Me llamo Leo, soy de Bélgica y tengo 15 años. Vivo en Gante. ¡Encantado!"},
  {"scenario":"Rellena tu perfil: nombre, origen, edad, ciudad.","tag":"pres","sub":"vier gegevens in hele zinnen","min":10,
   "need":[{"re":"me llamo|mi nombre","label":"nombre"},{"re":"soy de|soy [a-z]","label":"origen/nacionalidad"},{"re":"tengo .*(años|año)","label":"edad"},{"re":"vivo en","label":"ciudad (vivo en …)"}],
   "bank":["Me llamo","Mi nombre es","Soy de","Soy belga","tengo","14 años","Vivo en","Amberes","Hablo","dos idiomas"],
   "model":"Me llamo Sara, soy belga y tengo 14 años. Vivo en Amberes y hablo dos idiomas."},
  {"scenario":"Responde: «¿Quién eres?» Preséntate a la clase.","tag":"pres","sub":"saludo + 3 datos + despedida","min":10,
   "need":[{"re":"hola|buenos|buenas","label":"saludo"},{"re":"me llamo|soy","label":"nombre/ser"},{"re":"tengo .*(años|año)","label":"edad"},{"re":"gracias|adiós|encantad","label":"cierre"}],
   "bank":["¡Buenos días!","Me llamo","Soy de","España","tengo","16 años","Encantada","Gracias","Hablo español"],
   "model":"¡Buenos días! Me llamo Nina, soy de Perú y tengo 16 años. Hablo español. ¡Gracias!"}]}})

print("\n18 U1-spellen geschreven (9 templates: match·memory·classify·cloze·tetris·order·tap·point·sim).")
