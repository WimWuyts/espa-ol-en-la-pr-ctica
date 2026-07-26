#!/usr/bin/env python3
# Genereert de 24 motor-content-JSON's voor C5 · U2 «Mi gente» (parada Sevilla · Lucía).
# Templates: memory·match·classify·cloze·tetris·tap·order·point·sim·speak (10 · receptief→productief→hablar).
# Grammaticale vormen NAGEREKEND/GEVERIFIEERD (U2_bron.md §3):
#   tener: tengo·tienes·tiene·tenemos·tenéis·tienen · ser: soy·eres·es·somos·sois·son
#   estar: estoy·estás·está·estamos·estáis·están
# Speak = échte stemopname (MediaRecorder, offline). Cursuskleur = groen. Titels ZONDER <span>.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2))
    print("wrote", os.path.basename(p))

G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0"}

# ============================ ① RECONOCER · woordenschat ============================
# 1 · MEMORY — la familia ES ↔ NL
w({"id":"es-u2-familia-memoria","title":"Memoria de la familia","subtitle":"U2 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes om: familielid + vertaling","pairs":[
  {"a":"el padre","b":"de vader"},{"a":"la madre","b":"de moeder"},{"a":"el hermano","b":"de broer"},
  {"a":"la hermana","b":"de zus"},{"a":"el abuelo","b":"de opa"},{"a":"la abuela","b":"de oma"},
  {"a":"el tío","b":"de oom"},{"a":"la tía","b":"de tante"},{"a":"el primo","b":"de neef"},
  {"a":"la prima","b":"de nicht"},{"a":"el hijo","b":"de zoon"},{"a":"la hija","b":"de dochter"},
  {"a":"el sobrino","b":"het neefje"},{"a":"la sobrina","b":"het nichtje"}]}})

# 2 · MATCH — parentesco ↔ definición (español A1)
w({"id":"es-u2-parentesco","title":"El parentesco","subtitle":"U2 · koppel het familielid aan de omschrijving",
 "lang":"es","template":"match","options":{"chunk":4,"audio":False},
 "match":{"prompt":"Verbind het familielid met de juiste omschrijving","pairs":[
  {"a":"el abuelo","b":"el padre de mi padre"},{"a":"la abuela","b":"la madre de mi madre"},
  {"a":"el tío","b":"el hermano de mi padre"},{"a":"la tía","b":"la hermana de mi madre"},
  {"a":"el primo","b":"el hijo de mi tío"},{"a":"la prima","b":"la hija de mi tía"},
  {"a":"el sobrino","b":"el hijo de mi hermano"},{"a":"la sobrina","b":"la hija de mi hermana"},
  {"a":"el nieto","b":"el hijo de mi hijo"},{"a":"la nieta","b":"la hija de mi hija"},
  {"a":"los padres","b":"el padre y la madre"},{"a":"los abuelos","b":"el abuelo y la abuela"}]}})

# 3 · MATCH — colores ES ↔ NL
w({"id":"es-u2-colores-match","title":"Los colores del pelo y los ojos","subtitle":"U2 · koppel de kleur aan de vertaling",
 "lang":"es","template":"match","options":{"chunk":4,"audio":False},
 "match":{"prompt":"Verbind de Spaanse kleur met de Nederlandse vertaling","pairs":[
  {"a":"marrón","b":"bruin"},{"a":"negro","b":"zwart"},{"a":"castaño","b":"kastanjebruin"},
  {"a":"azul","b":"blauw"},{"a":"verde","b":"groen"},{"a":"gris","b":"grijs"},
  {"a":"rubio","b":"blond"},{"a":"pelirrojo","b":"roodharig"},{"a":"moreno","b":"donkerbruin"},
  {"a":"blanco","b":"wit"},{"a":"claro","b":"licht"},{"a":"oscuro","b":"donker"}]}})

# 4 · TAP — sílaba tónica op familia/física-woorden
w({"id":"es-u2-tonica-familia","title":"La tónica de la familia","subtitle":"U2 · tik de sterke lettergreep",
 "lang":"es","template":"tap","options":{"rounds":12,"audio":False},
 "tap":{"prompt":"Tik de sílaba tónica (de sterke lettergreep)","joiner":"·","items":[
  {"parts":["fa","mi","lia"],"answer":1,"tag":"llana","sub":"familia"},
  {"parts":["her","ma","no"],"answer":1,"tag":"llana","sub":"hermano"},
  {"parts":["a","bue","lo"],"answer":1,"tag":"llana","sub":"abuelo"},
  {"parts":["pri","mo"],"answer":0,"tag":"llana","sub":"primo"},
  {"parts":["sim","pá","ti","co"],"answer":1,"tag":"esdrujula","sub":"simpático · tilde"},
  {"parts":["tí","mi","do"],"answer":0,"tag":"esdrujula","sub":"tímido · tilde"},
  {"parts":["ma","rrón"],"answer":1,"tag":"aguda","sub":"marrón · tilde"},
  {"parts":["na","riz"],"answer":1,"tag":"aguda","sub":"nariz"},
  {"parts":["ca","be","za"],"answer":1,"tag":"llana","sub":"cabeza"},
  {"parts":["ma","yor"],"answer":1,"tag":"aguda","sub":"mayor"},
  {"parts":["her","ma","na"],"answer":1,"tag":"llana","sub":"hermana"},
  {"parts":["pe","li","rro","jo"],"answer":2,"tag":"llana","sub":"pelirrojo"}]}})

# ============================ ② DISTINGUIR · gramática ============================
# 5 · CLASSIFY — forma de tener → persona
w({"id":"es-u2-tener-persona","title":"Tener: ¿quién?","subtitle":"U2 · welke persoon hoort bij deze vorm van tener?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Bij welke persoon hoort deze vorm van tener?","categories":[
  {"id":"yo","label":"yo","glaze":G["red"]},{"id":"tu","label":"tú","glaze":G["amber"]},
  {"id":"el","label":"él/ella","glaze":G["green"]},{"id":"nos","label":"nosotros","glaze":G["blue"]},
  {"id":"vos","label":"vosotros","glaze":G["purple"]},{"id":"ellos","label":"ellos","glaze":G["teal"]}],
 "items":[
  {"stimulus":"tengo","answer":"yo","tag":"yo","sub":"yo tengo"},
  {"stimulus":"tienes","answer":"tu","tag":"tu","sub":"tú tienes"},
  {"stimulus":"tiene","answer":"el","tag":"el","sub":"él/ella tiene"},
  {"stimulus":"tenemos","answer":"nos","tag":"nos","sub":"nosotros tenemos"},
  {"stimulus":"tenéis","answer":"vos","tag":"vos","sub":"vosotros tenéis"},
  {"stimulus":"tienen","answer":"ellos","tag":"ellos","sub":"ellos tienen"},
  {"stimulus":"tengo","answer":"yo","tag":"yo","sub":"Tengo dos hermanos"},
  {"stimulus":"tienes","answer":"tu","tag":"tu","sub":"¿Cuántos años tienes?"},
  {"stimulus":"tiene","answer":"el","tag":"el","sub":"Mi hermano tiene 15 años"},
  {"stimulus":"tenemos","answer":"nos","tag":"nos","sub":"Tenemos una mascota"},
  {"stimulus":"tenéis","answer":"vos","tag":"vos","sub":"¿Tenéis primos?"},
  {"stimulus":"tienen","answer":"ellos","tag":"ellos","sub":"Mis abuelos tienen un perro"}]}})

# 6 · CLASSIFY — masculino / femenino (-o / -a)
w({"id":"es-u2-masculino-femenino","title":"¿Masculino o femenino?","subtitle":"U2 · eindigt op -o (m.) of op -a (f.)?",
 "lang":"es","template":"classify","options":{"rounds":14,"audio":False},
 "classify":{"prompt":"Eindigt op -o (masculino) of op -a (femenino)?","categories":[
  {"id":"m","label":"Masculino<br><small>-o (el)</small>","glaze":G["blue"]},
  {"id":"f","label":"Femenino<br><small>-a (la)</small>","glaze":G["red"]}],
 "items":[
  {"stimulus":"el tío","answer":"m","tag":"m","sub":"-o"},{"stimulus":"la tía","answer":"f","tag":"f","sub":"-a"},
  {"stimulus":"el primo","answer":"m","tag":"m","sub":"-o"},{"stimulus":"la prima","answer":"f","tag":"f","sub":"-a"},
  {"stimulus":"el hermano","answer":"m","tag":"m","sub":"-o"},{"stimulus":"la hermana","answer":"f","tag":"f","sub":"-a"},
  {"stimulus":"el abuelo","answer":"m","tag":"m","sub":"-o"},{"stimulus":"la abuela","answer":"f","tag":"f","sub":"-a"},
  {"stimulus":"el hijo","answer":"m","tag":"m","sub":"-o"},{"stimulus":"la hija","answer":"f","tag":"f","sub":"-a"},
  {"stimulus":"alto","answer":"m","tag":"m","sub":"adj. -o"},{"stimulus":"alta","answer":"f","tag":"f","sub":"adj. -a"},
  {"stimulus":"simpático","answer":"m","tag":"m","sub":"adj. -o"},{"stimulus":"simpática","answer":"f","tag":"f","sub":"adj. -a"}]}})

# 7 · CLASSIFY — adjetivo físico vs carácter
w({"id":"es-u2-fisico-caracter","title":"¿Físico o carácter?","subtitle":"U2 · beschrijft het het uiterlijk of het karakter?",
 "lang":"es","template":"classify","options":{"rounds":16,"audio":False},
 "classify":{"prompt":"¿Descripción física (uiterlijk) o carácter (aard)?","categories":[
  {"id":"fis","label":"Físico<br><small>uiterlijk</small>","glaze":G["teal"]},
  {"id":"car","label":"Carácter<br><small>aard</small>","glaze":G["purple"]}],
 "items":[
  {"stimulus":"alto","answer":"fis","tag":"fis","sub":"lang"},{"stimulus":"simpático","answer":"car","tag":"car","sub":"aardig"},
  {"stimulus":"moreno","answer":"fis","tag":"fis","sub":"donkerharig"},{"stimulus":"tímido","answer":"car","tag":"car","sub":"verlegen"},
  {"stimulus":"rubio","answer":"fis","tag":"fis","sub":"blond"},{"stimulus":"gracioso","answer":"car","tag":"car","sub":"grappig"},
  {"stimulus":"delgado","answer":"fis","tag":"fis","sub":"slank"},{"stimulus":"hablador","answer":"car","tag":"car","sub":"praatgraag"},
  {"stimulus":"guapo","answer":"fis","tag":"fis","sub":"knap"},{"stimulus":"tranquilo","answer":"car","tag":"car","sub":"rustig"},
  {"stimulus":"pelirrojo","answer":"fis","tag":"fis","sub":"roodharig"},{"stimulus":"alegre","answer":"car","tag":"car","sub":"vrolijk"},
  {"stimulus":"bajo","answer":"fis","tag":"fis","sub":"klein"},{"stimulus":"inteligente","answer":"car","tag":"car","sub":"slim"},
  {"stimulus":"joven","answer":"fis","tag":"fis","sub":"jong"},{"stimulus":"majo","answer":"car","tag":"car","sub":"leuk (Sp.)"}]}})

# 8 · CLASSIFY — posesivo singular / plural (getal)
w({"id":"es-u2-posesivo-numero","title":"¿mi o mis?","subtitle":"U2 · één ding (mi/tu/su) of meerdere (mis/tus/sus)?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Verwijst het bezit naar één ding of naar meerdere?","categories":[
  {"id":"sing","label":"mi · tu · su<br><small>1 cosa</small>","glaze":G["green"]},
  {"id":"plur","label":"mis · tus · sus<br><small>varias cosas</small>","glaze":G["blue"]}],
 "items":[
  {"stimulus":"mi hermano","answer":"sing","tag":"sing","sub":"1 → mi"},
  {"stimulus":"mis hermanos","answer":"plur","tag":"plur","sub":"mv. → mis"},
  {"stimulus":"tu prima","answer":"sing","tag":"sing","sub":"1 → tu"},
  {"stimulus":"tus primos","answer":"plur","tag":"plur","sub":"mv. → tus"},
  {"stimulus":"su abuelo","answer":"sing","tag":"sing","sub":"1 → su"},
  {"stimulus":"sus abuelos","answer":"plur","tag":"plur","sub":"mv. → sus"},
  {"stimulus":"mi familia","answer":"sing","tag":"sing","sub":"1 → mi"},
  {"stimulus":"mis padres","answer":"plur","tag":"plur","sub":"mv. → mis"},
  {"stimulus":"tu tío","answer":"sing","tag":"sing","sub":"1 → tu"},
  {"stimulus":"tus tías","answer":"plur","tag":"plur","sub":"mv. → tus"},
  {"stimulus":"su hija","answer":"sing","tag":"sing","sub":"1 → su"},
  {"stimulus":"sus hijos","answer":"plur","tag":"plur","sub":"mv. → sus"}]}})

# 9 · CLASSIFY — ser vs estar
w({"id":"es-u2-ser-estar","title":"¿ser o estar?","subtitle":"U2 · identiteit/beschrijving (ser) of toestand/plaats (estar)?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"¿Necesitas ser (identidad/descripción) o estar (estado/lugar)?","categories":[
  {"id":"ser","label":"ser<br><small>identidad · cómo es</small>","glaze":G["amber"]},
  {"id":"estar","label":"estar<br><small>estado · dónde está</small>","glaze":G["teal"]}],
 "items":[
  {"stimulus":"Mi madre ___ alta.","answer":"ser","tag":"ser","sub":"descripción → es"},
  {"stimulus":"Mi abuela ___ en casa.","answer":"estar","tag":"estar","sub":"lugar → está"},
  {"stimulus":"Mi hermano ___ cansado.","answer":"estar","tag":"estar","sub":"estado → está"},
  {"stimulus":"Lucía ___ morena.","answer":"ser","tag":"ser","sub":"descripción → es"},
  {"stimulus":"Mis primos ___ simpáticos.","answer":"ser","tag":"ser","sub":"carácter → son"},
  {"stimulus":"Mi padre ___ en Sevilla.","answer":"estar","tag":"estar","sub":"lugar → está"},
  {"stimulus":"Ana ___ tímida.","answer":"ser","tag":"ser","sub":"carácter → es"},
  {"stimulus":"Hoy ___ contentos.","answer":"estar","tag":"estar","sub":"estado → están"},
  {"stimulus":"Nosotros ___ de Andalucía.","answer":"ser","tag":"ser","sub":"origen → somos"},
  {"stimulus":"El abuelo ___ enfermo hoy.","answer":"estar","tag":"estar","sub":"estado → está"},
  {"stimulus":"Marco ___ delgado.","answer":"ser","tag":"ser","sub":"descripción → es"},
  {"stimulus":"La familia ___ en la cocina.","answer":"estar","tag":"estar","sub":"lugar → está"}]}})

# 10 · CLASSIFY — demostrativos: este (cerca) / ese (lejos)
w({"id":"es-u2-este-ese","title":"¿este o ese?","subtitle":"U2 · este/esta = dichtbij · ese/esa = verderaf",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"¿Es este/esta (aquí, cerca) o ese/esa (allí, lejos)?","categories":[
  {"id":"cerca","label":"este · esta<br><small>aquí (cerca)</small>","glaze":G["green"]},
  {"id":"lejos","label":"ese · esa<br><small>allí (lejos)</small>","glaze":G["amber"]}],
 "items":[
  {"stimulus":"esta foto","answer":"cerca","tag":"cerca","sub":"esta → cerca"},
  {"stimulus":"esa niña","answer":"lejos","tag":"lejos","sub":"esa → lejos"},
  {"stimulus":"este chico","answer":"cerca","tag":"cerca","sub":"este → cerca"},
  {"stimulus":"ese señor","answer":"lejos","tag":"lejos","sub":"ese → lejos"},
  {"stimulus":"estos primos","answer":"cerca","tag":"cerca","sub":"estos → cerca"},
  {"stimulus":"esas fotos","answer":"lejos","tag":"lejos","sub":"esas → lejos"},
  {"stimulus":"estas gafas","answer":"cerca","tag":"cerca","sub":"estas → cerca"},
  {"stimulus":"esos abuelos","answer":"lejos","tag":"lejos","sub":"esos → lejos"},
  {"stimulus":"este es mi hermano","answer":"cerca","tag":"cerca","sub":"aquí a mi lado"},
  {"stimulus":"esa es mi tía","answer":"lejos","tag":"lejos","sub":"allí, en la foto"},
  {"stimulus":"esta mascota","answer":"cerca","tag":"cerca","sub":"esta → cerca"},
  {"stimulus":"ese hombre","answer":"lejos","tag":"lejos","sub":"ese → lejos"}]}})

# ============================ ③ PRODUCIR CON APOYO ============================
# 11 · CLOZE — tener (vormen geverifieerd)
w({"id":"es-u2-tener-cloze","title":"Completa: tener","subtitle":"U2 · vul de juiste vorm van tener in",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm van tener","items":[
  {"stimulus":"Yo ___ dos hermanos.","options":["tengo","tienes","tiene"],"answer":"tengo","tag":"t","sub":"yo → tengo"},
  {"stimulus":"¿Cuántos primos ___ tú?","options":["tienes","tienen","tengo"],"answer":"tienes","tag":"t","sub":"tú → tienes"},
  {"stimulus":"Mi hermano ___ quince años.","options":["tiene","tienes","tengo"],"answer":"tiene","tag":"t","sub":"él → tiene"},
  {"stimulus":"Nosotros ___ una mascota.","options":["tenemos","tienen","tengo"],"answer":"tenemos","tag":"t","sub":"nosotros → tenemos"},
  {"stimulus":"Mis abuelos ___ un perro.","options":["tienen","tiene","tenéis"],"answer":"tienen","tag":"t","sub":"ellos → tienen"},
  {"stimulus":"¿Vosotros ___ primos en Madrid?","options":["tenéis","tienen","tenemos"],"answer":"tenéis","tag":"t","sub":"vosotros → tenéis"},
  {"stimulus":"Lucía ___ el pelo largo.","options":["tiene","tienes","tengo"],"answer":"tiene","tag":"t","sub":"ella → tiene"},
  {"stimulus":"Yo ___ una hermana menor.","options":["tengo","tiene","tienes"],"answer":"tengo","tag":"t","sub":"yo → tengo"},
  {"stimulus":"¿Tú ___ mascota?","options":["tienes","tiene","tenéis"],"answer":"tienes","tag":"t","sub":"tú → tienes"},
  {"stimulus":"Mi tía ___ dos hijos.","options":["tiene","tienen","tengo"],"answer":"tiene","tag":"t","sub":"ella → tiene"},
  {"stimulus":"Mis primos ___ un gato.","options":["tienen","tiene","tenéis"],"answer":"tienen","tag":"t","sub":"ellos → tienen"},
  {"stimulus":"Mi sobrino ___ cinco años.","options":["tiene","tienes","tengo"],"answer":"tiene","tag":"t","sub":"él → tiene"}]}})

# 12 · CLOZE — verbo-cloze VERPLICHT (tener + ser + estar · nagerekend §4 bron)
w({"id":"es-u2-ser-estar-cloze","title":"Completa el verbo: ser · estar · tener","subtitle":"U2 · vul de juiste vorm in (vormen nagerekend)",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Kies de juiste werkwoordsvorm","items":[
  {"stimulus":"Mi abuela ___ (ser) simpática.","options":["es","está","tiene"],"answer":"es","tag":"ser","sub":"ser · ella → es"},
  {"stimulus":"Hoy mi abuela ___ (estar) en Sevilla.","options":["está","es","tiene"],"answer":"está","tag":"estar","sub":"estar · ella → está"},
  {"stimulus":"Yo ___ (tener) dos primos.","options":["tengo","soy","estoy"],"answer":"tengo","tag":"tener","sub":"tener · yo → tengo"},
  {"stimulus":"Mis padres ___ (ser) de Andalucía.","options":["son","están","tienen"],"answer":"son","tag":"ser","sub":"ser · ellos → son"},
  {"stimulus":"Nosotros ___ (estar) en casa.","options":["estamos","somos","tenemos"],"answer":"estamos","tag":"estar","sub":"estar · nosotros → estamos"},
  {"stimulus":"¿Cuántos hermanos ___ (tener) tú?","options":["tienes","eres","estás"],"answer":"tienes","tag":"tener","sub":"tener · tú → tienes"},
  {"stimulus":"Lucía ___ (tener) el pelo largo.","options":["tiene","es","está"],"answer":"tiene","tag":"tener","sub":"tener · ella → tiene"},
  {"stimulus":"Lucía ___ (ser) morena.","options":["es","está","tiene"],"answer":"es","tag":"ser","sub":"ser · ella → es"},
  {"stimulus":"Mi hermano ___ (estar) cansado.","options":["está","es","tiene"],"answer":"está","tag":"estar","sub":"estar · él → está"},
  {"stimulus":"Vosotros ___ (ser) muy majos.","options":["sois","estáis","tenéis"],"answer":"sois","tag":"ser","sub":"ser · vosotros → sois"},
  {"stimulus":"Mi tío ___ (estar) en el trabajo.","options":["está","es","tiene"],"answer":"está","tag":"estar","sub":"estar · él → está"},
  {"stimulus":"Ana ___ (ser) muy graciosa.","options":["es","está","tiene"],"answer":"es","tag":"ser","sub":"ser · ella → es"}]}})

# 13 · CLOZE — posesivos mi/tu/su + getal
w({"id":"es-u2-posesivo-cloze","title":"Completa: mi · tu · su","subtitle":"U2 · vul het juiste bezittelijk voornaamwoord in",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies het juiste bezittelijk voornaamwoord","items":[
  {"stimulus":"___ hermanos son altos. (yo · 2)","options":["Mis","Mi","Su"],"answer":"Mis","tag":"pos","sub":"mv. → mis"},
  {"stimulus":"___ prima se llama Julia. (yo · 1)","options":["Mi","Mis","Tu"],"answer":"Mi","tag":"pos","sub":"1 → mi"},
  {"stimulus":"¿Cómo se llama ___ padre? (tú)","options":["tu","tus","su"],"answer":"tu","tag":"pos","sub":"1 → tu"},
  {"stimulus":"___ abuelos viven en Sevilla. (yo · 2)","options":["Mis","Mi","Sus"],"answer":"Mis","tag":"pos","sub":"mv. → mis"},
  {"stimulus":"Lucía y ___ familia son de Sevilla. (ella)","options":["su","sus","tu"],"answer":"su","tag":"pos","sub":"1 → su"},
  {"stimulus":"¿Tienes fotos de ___ primos? (tú · 2)","options":["tus","tu","sus"],"answer":"tus","tag":"pos","sub":"mv. → tus"},
  {"stimulus":"___ madre es habladora. (yo · 1)","options":["Mi","Mis","Su"],"answer":"Mi","tag":"pos","sub":"1 → mi"},
  {"stimulus":"Marco y Ana son ___ hermanos. (yo)","options":["mis","mi","tus"],"answer":"mis","tag":"pos","sub":"mv. → mis"},
  {"stimulus":"¿Dónde están ___ gafas? (tú)","options":["tus","tu","sus"],"answer":"tus","tag":"pos","sub":"gafas = mv. → tus"},
  {"stimulus":"___ tía tiene dos hijos. (ella)","options":["Su","Sus","Mi"],"answer":"Su","tag":"pos","sub":"1 → su"},
  {"stimulus":"___ casa está en Sevilla. (nosotros · 1)","options":["Nuestra","Nuestro","Nuestros"],"answer":"Nuestra","tag":"pos","sub":"la casa (f) → nuestra"},
  {"stimulus":"___ abuelos son mayores. (nosotros · 2)","options":["Nuestros","Nuestro","Nuestras"],"answer":"Nuestros","tag":"pos","sub":"mv. m → nuestros"}]}})

# 14 · CLOZE — congruencia del adjetivo (género/número)
w({"id":"es-u2-adjetivo-concuerda","title":"El adjetivo concuerda","subtitle":"U2 · pas het adjectief aan (género + número)",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm van het adjectief","items":[
  {"stimulus":"Mi hermana es ___. (alto)","options":["alta","alto","altos"],"answer":"alta","tag":"c","sub":"fem. sing. → alta"},
  {"stimulus":"Mis primos son ___. (simpático)","options":["simpáticos","simpática","simpático"],"answer":"simpáticos","tag":"c","sub":"masc. pl. → simpáticos"},
  {"stimulus":"Lucía es ___. (moreno)","options":["morena","moreno","morenas"],"answer":"morena","tag":"c","sub":"fem. sing. → morena"},
  {"stimulus":"Mi padre es ___. (tranquilo)","options":["tranquilo","tranquila","tranquilos"],"answer":"tranquilo","tag":"c","sub":"masc. sing. → tranquilo"},
  {"stimulus":"Mis abuelas son ___. (bajo)","options":["bajas","bajos","baja"],"answer":"bajas","tag":"c","sub":"fem. pl. → bajas"},
  {"stimulus":"Ana es muy ___. (gracioso)","options":["graciosa","gracioso","graciosas"],"answer":"graciosa","tag":"c","sub":"fem. sing. → graciosa"},
  {"stimulus":"Mis hermanos son ___. (rubio)","options":["rubios","rubias","rubio"],"answer":"rubios","tag":"c","sub":"masc. pl. → rubios"},
  {"stimulus":"Mi tía es ___. (hablador)","options":["habladora","hablador","habladoras"],"answer":"habladora","tag":"c","sub":"fem. sing. → habladora"},
  {"stimulus":"Las primas son ___. (guapo)","options":["guapas","guapos","guapa"],"answer":"guapas","tag":"c","sub":"fem. pl. → guapas"},
  {"stimulus":"Mi abuelo es ___. (alto)","options":["alto","alta","altos"],"answer":"alto","tag":"c","sub":"masc. sing. → alto"},
  {"stimulus":"Mis sobrinas son ___. (pequeño)","options":["pequeñas","pequeños","pequeña"],"answer":"pequeñas","tag":"c","sub":"fem. pl. → pequeñas"},
  {"stimulus":"El bebé es ___. (gracioso)","options":["gracioso","graciosa","graciosos"],"answer":"gracioso","tag":"c","sub":"masc. sing. → gracioso"}]}})

# 15 · ORDER — árbol genealógico / presentar a la familia
w({"id":"es-u2-arbol-genealogico","title":"El árbol genealógico","subtitle":"U2 · zet de familie in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik de tegels in de juiste volgorde","rounds":[
  {"tag":"generacion","sub":"de mayor a menor (generaciones)","items":[
    {"label":"los abuelos","key":1},{"label":"el padre y la madre","key":2},
    {"label":"yo y mi hermano","key":3}]},
  {"tag":"edad","sub":"por edad (mayor → menor)","items":[
    {"label":"el abuelo (70)","key":1},{"label":"mi madre (45)","key":2},
    {"label":"mi hermano mayor (19)","key":3},{"label":"yo (16)","key":4},{"label":"mi hermana menor (8)","key":5}]},
  {"tag":"presentar","sub":"presenta a tu familia (orden lógico)","items":[
    {"label":"Esta es mi familia.","key":1},{"label":"Somos cinco en casa.","key":2},
    {"label":"Mi padre se llama Antonio.","key":3},{"label":"Y yo soy el menor.","key":4}]}]}})

# 16 · TETRIS — persona de tener / ser / estar (vormen geverifieerd, hardcoded)
w({"id":"es-u2-familia-tetris","title":"Tetris: ser, estar y tener","subtitle":"U2 · laat elke vorm in de juiste persoon vallen",
 "lang":"es","template":"tetris","options":{"rows":9,"speed":1300,"audio":False},
 "classify":{"categories":[
  {"id":"yo","label":"yo","glaze":G["red"]},{"id":"tu","label":"tú","glaze":G["amber"]},
  {"id":"el","label":"él/ella","glaze":G["green"]},{"id":"nos","label":"nosotros","glaze":G["blue"]},
  {"id":"vos","label":"vosotros","glaze":G["purple"]},{"id":"ellos","label":"ellos","glaze":G["teal"]}],
 "items":[
  {"stimulus":"tengo","answer":"yo","tag":"yo","sub":"tener"},{"stimulus":"tienes","answer":"tu","tag":"tu","sub":"tener"},
  {"stimulus":"tiene","answer":"el","tag":"el","sub":"tener"},{"stimulus":"tenemos","answer":"nos","tag":"nos","sub":"tener"},
  {"stimulus":"tenéis","answer":"vos","tag":"vos","sub":"tener"},{"stimulus":"tienen","answer":"ellos","tag":"ellos","sub":"tener"},
  {"stimulus":"soy","answer":"yo","tag":"yo","sub":"ser"},{"stimulus":"eres","answer":"tu","tag":"tu","sub":"ser"},
  {"stimulus":"es","answer":"el","tag":"el","sub":"ser"},{"stimulus":"somos","answer":"nos","tag":"nos","sub":"ser"},
  {"stimulus":"sois","answer":"vos","tag":"vos","sub":"ser"},{"stimulus":"son","answer":"ellos","tag":"ellos","sub":"ser"},
  {"stimulus":"estoy","answer":"yo","tag":"yo","sub":"estar"},{"stimulus":"estás","answer":"tu","tag":"tu","sub":"estar"},
  {"stimulus":"está","answer":"el","tag":"el","sub":"estar"},{"stimulus":"estamos","answer":"nos","tag":"nos","sub":"estar"},
  {"stimulus":"estáis","answer":"vos","tag":"vos","sub":"estar"},{"stimulus":"están","answer":"ellos","tag":"ellos","sub":"estar"}]}})

# ============================ ④ ANALIZAR & COMUNICAR ============================
# 17 · POINT — señala la parte del cuerpo
w({"id":"es-u2-cuerpo-point","title":"Señala la parte del cuerpo","subtitle":"U2 · klik het gevraagde lichaamsdeel",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik het lichaamsdeel dat gevraagd wordt","mode":"one","rounds":[
  {"tag":"cuerpo","sub":"la cabeza","targets":[
    {"label":"la cabeza","hit":True},{"label":"la mano"},{"label":"la nariz"},{"label":"la boca"}]},
  {"tag":"cuerpo","sub":"la nariz","targets":[
    {"label":"la cara"},{"label":"la nariz","hit":True},{"label":"la boca"},{"label":"la mano"}]},
  {"tag":"cuerpo","sub":"la boca","targets":[
    {"label":"la boca","hit":True},{"label":"la cabeza"},{"label":"los ojos"},{"label":"la nariz"}]},
  {"tag":"cuerpo","sub":"la mano","targets":[
    {"label":"la mano","hit":True},{"label":"la cara"},{"label":"la cabeza"},{"label":"la boca"}]},
  {"tag":"cuerpo","sub":"los ojos","targets":[
    {"label":"los ojos","hit":True},{"label":"la nariz"},{"label":"la boca"},{"label":"la mano"}]}]}})

# 18 · POINT — caza del adjetivo (klik ALLE adjetivos)
w({"id":"es-u2-caza-adjetivo","title":"Caza del adjetivo","subtitle":"U2 · klik ALLE adjectieven (geen zelfstandige naamwoorden)",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik ALLE adjectieven (woorden die iemand beschrijven)","mode":"all","rounds":[
  {"tag":"adj","sub":"2 adjetivos","targets":[
    {"label":"alto","hit":True},{"label":"el padre"},{"label":"simpática","hit":True},{"label":"la mano"}]},
  {"tag":"adj","sub":"2 adjetivos","targets":[
    {"label":"moreno","hit":True},{"label":"el primo"},{"label":"tímido","hit":True},{"label":"la abuela"}]},
  {"tag":"adj","sub":"3 adjetivos","targets":[
    {"label":"alta","hit":True},{"label":"guapo","hit":True},{"label":"la tía"},{"label":"gracioso","hit":True},{"label":"los ojos"}]},
  {"tag":"adj","sub":"2 adjetivos","targets":[
    {"label":"rubia","hit":True},{"label":"la nariz"},{"label":"tranquilo","hit":True},{"label":"la hermana"}]}]}})

# 19 · SIM — describe a un familiar (vrije productie met bouwsteen-check)
w({"id":"es-u2-describe-persona","title":"Describe a un familiar","subtitle":"U2 · beschrijf een familielid — met alle bouwstenen",
 "lang":"es","template":"sim","options":{"audio":False},
 "sim":{"prompt":"Tarea comunicativa · beschrijf iemand uit je familie","rounds":[
  {"scenario":"Preséntale un familiar a Lucía por chat.","tag":"describir","sub":"gebruik: mi … · se llama · es …","min":10,
   "need":[{"re":"mi (padre|madre|hermano|hermana|abuelo|abuela|t[íi]o|t[íi]a|primo|prima)","label":"mi + familielid"},{"re":"se llama","label":"se llama …"},{"re":"\\bes\\b","label":"es + descripción"}],
   "bank":["Mi hermano","Mi hermana","se llama","es alto","es simpática","tiene el pelo largo","y","también"],
   "model":"Mi hermano se llama Marco. Es alto y moreno, y es muy simpático."},
  {"scenario":"Describe el físico Y el carácter de un familiar.","tag":"describir","sub":"uiterlijk + karakter + porque","min":12,
   "need":[{"re":"alto|baj|moren|rubi|delgad|guap|pelo|ojos","label":"un rasgo físico"},{"re":"simp[áa]tic|t[íi]mid|gracios|hablador|tranquil|alegre|majo","label":"un rasgo de carácter"},{"re":"porque","label":"porque …"}],
   "bank":["Mi tía","es baja","tiene los ojos verdes","es muy habladora","porque","habla mucho","pero","alegre"],
   "model":"Mi tía es baja y tiene los ojos verdes. Es muy habladora porque habla mucho, pero es muy alegre."},
  {"scenario":"«¿Cómo es tu familia?» Presenta a dos personas.","tag":"describir","sub":"tener + ser + estar","min":14,
   "need":[{"re":"tengo|tiene|tenemos","label":"tener (número/edad)"},{"re":"\\b(es|son|soy|somos)\\b","label":"ser (cómo es)"},{"re":"est[áa]|estamos|estoy","label":"estar (estado/lugar)"}],
   "bank":["Tengo dos hermanos","Mi madre es","muy simpática","Mi padre está","en el trabajo","tiene el pelo corto","somos cinco","hoy"],
   "model":"Somos cinco en casa. Tengo dos hermanos. Mi madre es muy simpática y hoy está en casa. Mi padre tiene el pelo corto y está en el trabajo."}]}})

# ============================ ⑤ HABLAR · grábate 🎙️ ============================
# 20 · SPEAK substitution — carrusel de la familia
w({"id":"es-u2-carrusel-familia","title":"Carrusel: mi familia","subtitle":"U2 · één zin, wisselende bouwstenen — grábate en cada vuelta",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"substitution","prompt":"Di la frase con el familiar nuevo y grábate ⏺",
  "frame":"Mi ___ se llama ___ y es ___.","frameLabel":"Modelo · vul de gemarkeerde delen in","items":[
  {"fills":["hermano","Marco","alto"],"sub":"broer · Marco · lang","tag":"carrusel"},
  {"fills":["madre","Rosa","habladora"],"sub":"moeder · Rosa · praatgraag","tag":"carrusel"},
  {"fills":["prima","Julia","pelirroja"],"sub":"nicht · Julia · roodharig","tag":"carrusel"},
  {"fills":["abuelo","Pepe","tranquilo"],"sub":"opa · Pepe · rustig","tag":"carrusel"},
  {"fills":["___","___","___"],"sub":"nu met JOUW echte familie — ¡cuéntalo tú!","tag":"carrusel",
   "tip":"¡Ahora tú de verdad! Grábate con un familiar real. <span class='nl'>neem jezelf op met een echt familielid.</span>"}]}})

# 21 · SPEAK shadowing — la familia de Lucía
w({"id":"es-u2-shadowing-lucia","title":"Shadowing: la familia de Lucía","subtitle":"U2 · imita a Lucía — de texto completo a tu versión",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"shadowing","prompt":"Escucha a Lucía y ve quitando apoyo, paso a paso",
  "phases":["Texto completo","Palabras clave","Sin texto","Tu versión"],"items":[
  {"text":"Esta es mi familia de Sevilla. Somos cinco.","keywords":["Esta es mi familia","Sevilla","Somos cinco"],"sub":"dit is mijn familie uit Sevilla, we zijn met vijf","tag":"familia"},
  {"text":"Mi padre es alto, moreno y muy tranquilo.","keywords":["Mi padre","alto, moreno","tranquilo"],"sub":"mijn vader is lang, donkerharig en heel rustig","tag":"familia"},
  {"text":"Mi madre es baja, rubia y muy habladora.","keywords":["Mi madre","baja, rubia","habladora"],"sub":"mijn moeder is klein, blond en heel praatgraag","tag":"familia"},
  {"text":"También tengo una prima, Julia, muy simpática.","keywords":["También tengo","una prima","simpática"],"sub":"ik heb ook een nicht, Julia, heel aardig","tag":"familia",
   "tip":"Ahora presenta a TU familia. <span class='nl'>stel nu je eigen familie voor.</span>"}]}})

# 22 · SPEAK repeat — describe a un familiar (3ª persona)
w({"id":"es-u2-describe-familiar","title":"Describe a un familiar","subtitle":"U2 · escucha, describe a la persona en 3ª persona, y grábate",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · describe a la persona (él/ella) · grábate ⏺","items":[
  {"cue":"Antonio · el padre de Lucía","text":"Antonio es alto y moreno.","sub":"hij is lang en donkerharig — «es»","tag":"describir"},
  {"cue":"Rosa · la madre de Lucía","text":"Rosa es baja y muy habladora.","sub":"zij is klein en heel praatgraag","tag":"describir"},
  {"cue":"Marco · el hermano mayor","text":"Marco tiene diecinueve años y lleva gafas.","sub":"hij is 19 en draagt een bril — «tiene»","tag":"describir"},
  {"cue":"Ana · la hermana menor","text":"Ana es pequeña, graciosa y un poco tímida.","sub":"zij is klein, grappig en een beetje verlegen","tag":"describir"},
  {"cue":"Julia · la prima","text":"Julia es pelirroja y muy simpática.","sub":"zij is roodharig en heel aardig","tag":"describir",
   "tip":"Ahora describe a un familiar tuyo de verdad. <span class='nl'>beschrijf nu een echt familielid.</span>"}]}})

# 23 · SPEAK voicemessage — mensaje de voz: mi familia
w({"id":"es-u2-mensaje-familia","title":"Mensaje de voz: mi familia","subtitle":"U2 · graba UN mensaje presentando a tu familia",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz · spraakbericht opnemen","items":[
  {"to":"Lucía, de Sevilla","situation":"Lucía te enseña su álbum de familia y te pregunta por la tuya.","goal":"Preséntale tu familia: cuántos sois y cómo son.",
   "blocks":["saludo (¡Hola, Lucía!)","en mi familia somos …","tengo … hermanos/as","mi madre/padre es …","despedida"],
   "sub":"Lucía — stel je familie voor (aantal + hoe ze zijn)","tag":"mensaje"},
  {"to":"Tu familia de acogida en España","situation":"Vas de intercambio y les hablas de tu familia.","goal":"Diles quién es quién y cómo es cada persona.",
   "blocks":["saludo","somos … en casa","mi hermano/a se llama …","es … (físico + carácter)","también tengo …","despedida"],
   "sub":"je gastgezin — wie is wie en hoe ze zijn","tag":"mensaje",
   "tip":"Escucha tu mensaje: ¿se entiende quién es quién? Vuelve a grabar más despacio. <span class='nl'>beluister jezelf; herneem rustiger.</span>"}]}})

# 24 · SPEAK voicemessage — ¿Quién es? (describe → adivina)
w({"id":"es-u2-quien-es","title":"¿Quién es? Descríbelo","subtitle":"U2 · beschrijf een persoon zodat de klas raadt — grábate",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Describe a la persona sin decir el nombre · graba tu descripción ⏺","items":[
  {"to":"La clase (juego «¿Quién es?»)","situation":"Es el juego de la tarea final: describes a alguien y los demás adivinan.","goal":"Describe a un familiar SIN decir el nombre (físico + carácter).",
   "blocks":["Es un chico / una chica de mi familia.","Es … (alto/a, moren@, rubi@ …).","Tiene el pelo … y los ojos …","Es muy … (simpátic@, gracios@ …).","¿Quién es?"],
   "sub":"beschrijf zonder naam · uiterlijk + karakter","tag":"quien",
   "tip":"¿Dijiste el pelo, los ojos Y el carácter? Si no, vuelve a grabar. <span class='nl'>haar, ogen én karakter genoemd? zo niet, herneem.</span>"},
  {"to":"La clase (segunda ronda)","situation":"Ahora describes a otra persona, más difícil.","goal":"Describe a otro familiar con MÁS detalles para que sea un buen reto.",
   "blocks":["Esta persona es mi …","Es … y …","Lleva gafas / tiene barba …","Su carácter es …","¿Quién es?"],
   "sub":"tweede ronde · meer details","tag":"quien"}]}})

print("\n24 U2-spellen geschreven (10 templates: memory·match·classify·cloze·tetris·tap·order·point·sim·speak).")
