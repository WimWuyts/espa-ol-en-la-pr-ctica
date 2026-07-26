#!/usr/bin/env python3
# Genereert de 24 motor-content-JSON's voor C5 · U3 «El tiempo vuela».
# Templates: match·memory·classify·cloze·tetris·tap·order·point·sim·speak (10 · receptief→productief).
# Grammaticale vormen (presente irregular) nagerekend: stamwissel via de motor-generator (verbo),
# reflexieve/onregelmatige vormen handmatig geverifieerd.
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2))
    print("wrote", os.path.basename(p))

G = {"blue":"#3D74D6","red":"#C4402C","green":"#2E8E68","amber":"#E0A22F","purple":"#8B5E9E","teal":"#2FA8A0"}

# ========== ① RECONOCER ==========
# 1 · MATCH — hora escrita ↔ reloj (dígitos)
w({"id":"es-u3-hora-reloj","title":"¿Qué hora es?","subtitle":"U3 · koppel de tijd aan de digitale klok",
 "lang":"es","template":"match","options":{"chunk":6,"audio":False},
 "match":{"prompt":"Verbind de gesproken tijd met de klok","pairs":[
  {"a":"Es la una","b":"1:00"},{"a":"Son las dos y media","b":"2:30"},{"a":"Son las tres y cuarto","b":"3:15"},
  {"a":"Son las cinco menos cuarto","b":"4:45"},{"a":"Son las nueve en punto","b":"9:00"},
  {"a":"Son las seis y diez","b":"6:10"},{"a":"Es la una y media","b":"1:30"},{"a":"Son las ocho menos cuarto","b":"7:45"}]}})

# 2 · MEMORY — rutina ES ↔ NL
w({"id":"es-u3-rutina-memoria","title":"Memoria de la rutina","subtitle":"U3 · zoek het paar español ↔ nederlands",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes: actie + vertaling","pairs":[
  {"a":"despertarse","b":"wakker worden"},{"a":"levantarse","b":"opstaan"},{"a":"ducharse","b":"douchen"},
  {"a":"vestirse","b":"zich aankleden"},{"a":"desayunar","b":"ontbijten"},{"a":"almorzar","b":"lunchen"},
  {"a":"cenar","b":"avondmalen"},{"a":"acostarse","b":"gaan slapen"},{"a":"hacer los deberes","b":"huiswerk maken"},
  {"a":"descansar","b":"uitrusten"}]}})

# 3 · MEMORY — verbo irregular ↔ betekenis
w({"id":"es-u3-verbo-memoria","title":"Verbos irregulares","subtitle":"U3 · zoek het werkwoord bij de betekenis",
 "lang":"es","template":"memory","options":{"pairs":6,"audio":False},
 "memory":{"prompt":"Draai twee kaartjes: werkwoord + betekenis","pairs":[
  {"a":"empezar","b":"beginnen"},{"a":"querer","b":"willen"},{"a":"poder","b":"kunnen"},
  {"a":"dormir","b":"slapen"},{"a":"volver","b":"terugkeren"},{"a":"pedir","b":"vragen/bestellen"},
  {"a":"jugar","b":"spelen"},{"a":"hacer","b":"doen/maken"},{"a":"salir","b":"uitgaan"},{"a":"preferir","b":"verkiezen"}]}})

# ========== ② DISTINGUIR ==========
# 4 · CLASSIFY — reflexivo vs no reflexivo
w({"id":"es-u3-reflexivo-no","title":"¿Reflexivo o no?","subtitle":"U3 · draagt het werkwoord een pronombre (me/te/se)?",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"Reflexief (me/te/se) of gewoon werkwoord?","categories":[
  {"id":"ref","label":"Reflexivo<br><small>me levanto</small>","glaze":G["purple"]},
  {"id":"no","label":"No reflexivo<br><small>desayuno</small>","glaze":G["green"]}],
 "items":[
  {"stimulus":"levantarse","answer":"ref","tag":"ref","sub":"me levanto"},
  {"stimulus":"desayunar","answer":"no","tag":"no","sub":"desayuno"},
  {"stimulus":"ducharse","answer":"ref","tag":"ref","sub":"me ducho"},
  {"stimulus":"cenar","answer":"no","tag":"no","sub":"ceno"},
  {"stimulus":"acostarse","answer":"ref","tag":"ref","sub":"me acuesto"},
  {"stimulus":"hacer los deberes","answer":"no","tag":"no","sub":"hago"},
  {"stimulus":"vestirse","answer":"ref","tag":"ref","sub":"me visto"},
  {"stimulus":"almorzar","answer":"no","tag":"no","sub":"almuerzo"},
  {"stimulus":"despertarse","answer":"ref","tag":"ref","sub":"me despierto"},
  {"stimulus":"descansar","answer":"no","tag":"no","sub":"descanso"},
  {"stimulus":"peinarse","answer":"ref","tag":"ref","sub":"me peino"},
  {"stimulus":"estudiar","answer":"no","tag":"no","sub":"estudio"}]}})

# 5 · CLASSIFY — cambio de raíz ie / ue / i
w({"id":"es-u3-cambio-raiz","title":"Cambio de raíz","subtitle":"U3 · welke stamwissel heeft dit werkwoord?",
 "lang":"es","template":"classify","options":{"rounds":15,"audio":False},
 "classify":{"prompt":"¿o→ue, e→ie of e→i?","categories":[
  {"id":"ue","label":"o → ue<br><small>puedo</small>","glaze":G["blue"]},
  {"id":"ie","label":"e → ie<br><small>quiero</small>","glaze":G["amber"]},
  {"id":"i","label":"e → i<br><small>pido</small>","glaze":G["teal"]}],
 "items":[
  {"stimulus":"poder","answer":"ue","tag":"ue","sub":"puedo"},{"stimulus":"querer","answer":"ie","tag":"ie","sub":"quiero"},
  {"stimulus":"pedir","answer":"i","tag":"i","sub":"pido"},{"stimulus":"dormir","answer":"ue","tag":"ue","sub":"duermo"},
  {"stimulus":"empezar","answer":"ie","tag":"ie","sub":"empiezo"},{"stimulus":"vestirse","answer":"i","tag":"i","sub":"me visto"},
  {"stimulus":"volver","answer":"ue","tag":"ue","sub":"vuelvo"},{"stimulus":"preferir","answer":"ie","tag":"ie","sub":"prefiero"},
  {"stimulus":"servir","answer":"i","tag":"i","sub":"sirvo"},{"stimulus":"almorzar","answer":"ue","tag":"ue","sub":"almuerzo"},
  {"stimulus":"despertarse","answer":"ie","tag":"ie","sub":"me despierto"},{"stimulus":"repetir","answer":"i","tag":"i","sub":"repito"},
  {"stimulus":"acostarse","answer":"ue","tag":"ue","sub":"me acuesto"},{"stimulus":"entender","answer":"ie","tag":"ie","sub":"entiendo"},
  {"stimulus":"encontrar","answer":"ue","tag":"ue","sub":"encuentro"}]}})

# 6 · CLASSIFY — de la vs por la
w({"id":"es-u3-de-por","title":"¿de la o por la?","subtitle":"U3 · concreet uur (de la) of deel van de dag (por la)",
 "lang":"es","template":"classify","options":{"rounds":12,"audio":False},
 "classify":{"prompt":"¿de la (uur) of por la (dagdeel)?","categories":[
  {"id":"de","label":"de la<br><small>a las 7 de la mañana</small>","glaze":G["blue"]},
  {"id":"por","label":"por la<br><small>por la mañana (geen uur)</small>","glaze":G["green"]}],
 "items":[
  {"stimulus":"Son las siete ___ mañana.","answer":"de","tag":"de","sub":"uur → de la"},
  {"stimulus":"___ tarde hago los deberes.","answer":"por","tag":"por","sub":"dagdeel → por la"},
  {"stimulus":"Ceno a las nueve ___ noche.","answer":"de","tag":"de","sub":"uur → de la"},
  {"stimulus":"___ mañana voy al instituto.","answer":"por","tag":"por","sub":"dagdeel → por la"},
  {"stimulus":"Me levanto a las ocho ___ mañana.","answer":"de","tag":"de","sub":"uur → de la"},
  {"stimulus":"Estudio ___ noche.","answer":"por","tag":"por","sub":"dagdeel → por la"},
  {"stimulus":"Almuerzo a las dos ___ tarde.","answer":"de","tag":"de","sub":"uur → de la"},
  {"stimulus":"___ tarde juego al fútbol.","answer":"por","tag":"por","sub":"dagdeel → por la"},
  {"stimulus":"Son las once ___ noche.","answer":"de","tag":"de","sub":"uur → de la"},
  {"stimulus":"Descanso ___ tarde.","answer":"por","tag":"por","sub":"dagdeel → por la"}]}})

# 7 · CLASSIFY — día / mes / estación
w({"id":"es-u3-dia-mes","title":"¿Día, mes o estación?","subtitle":"U3 · sorteer dag, maand of seizoen",
 "lang":"es","template":"classify","options":{"rounds":15,"audio":False},
 "classify":{"prompt":"¿Es un día, un mes o una estación?","categories":[
  {"id":"dia","label":"Día<br><small>lunes</small>","glaze":G["blue"]},
  {"id":"mes","label":"Mes<br><small>enero</small>","glaze":G["amber"]},
  {"id":"est","label":"Estación<br><small>verano</small>","glaze":G["green"]}],
 "items":[
  {"stimulus":"lunes","answer":"dia","tag":"dia","sub":"maandag"},{"stimulus":"agosto","answer":"mes","tag":"mes","sub":"augustus"},
  {"stimulus":"verano","answer":"est","tag":"est","sub":"zomer"},{"stimulus":"domingo","answer":"dia","tag":"dia","sub":"zondag"},
  {"stimulus":"marzo","answer":"mes","tag":"mes","sub":"maart"},{"stimulus":"invierno","answer":"est","tag":"est","sub":"winter"},
  {"stimulus":"viernes","answer":"dia","tag":"dia","sub":"vrijdag"},{"stimulus":"julio","answer":"mes","tag":"mes","sub":"juli"},
  {"stimulus":"primavera","answer":"est","tag":"est","sub":"lente"},{"stimulus":"miércoles","answer":"dia","tag":"dia","sub":"woensdag"},
  {"stimulus":"diciembre","answer":"mes","tag":"mes","sub":"december"},{"stimulus":"otoño","answer":"est","tag":"est","sub":"herfst"},
  {"stimulus":"sábado","answer":"dia","tag":"dia","sub":"zaterdag"},{"stimulus":"mayo","answer":"mes","tag":"mes","sub":"mei"},
  {"stimulus":"martes","answer":"dia","tag":"dia","sub":"dinsdag"}]}})

# ========== ③ PRODUCIR CON APOYO ==========
# 8 · CLOZE — la hora
w({"id":"es-u3-la-hora","title":"La hora","subtitle":"U3 · vul de juiste tijd-uitdrukking in",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Kies de juiste vorm","items":[
  {"stimulus":"___ una. (1:00)","options":["Es la","Son las","Es las"],"answer":"Es la","tag":"h","sub":"1 uur = Es la"},
  {"stimulus":"___ tres. (3:00)","options":["Son las","Es la","Son la"],"answer":"Son las","tag":"h","sub":"vanaf 2 = Son las"},
  {"stimulus":"Son las dos ___. (2:30)","options":["y media","y cuarto","menos cuarto"],"answer":"y media","tag":"h","sub":"half = y media"},
  {"stimulus":"Son las cuatro ___. (4:15)","options":["y cuarto","y media","en punto"],"answer":"y cuarto","tag":"h","sub":"kwart over"},
  {"stimulus":"Son las ocho ___. (7:45)","options":["menos cuarto","y cuarto","y media"],"answer":"menos cuarto","tag":"h","sub":"kwart voor"},
  {"stimulus":"Son las seis ___. (6:00)","options":["en punto","y media","de la"],"answer":"en punto","tag":"h","sub":"precies"},
  {"stimulus":"Me levanto a las siete ___ mañana.","options":["de la","por la","en"],"answer":"de la","tag":"h","sub":"concreet uur"},
  {"stimulus":"___ tarde hago deporte.","options":["Por la","De la","A la"],"answer":"Por la","tag":"h","sub":"dagdeel"},
  {"stimulus":"¿___ empiezas las clases?","options":["A qué hora","Qué hora","Cuál hora"],"answer":"A qué hora","tag":"h","sub":"om hoe laat"},
  {"stimulus":"Empiezo ___ ocho.","options":["a las","son las","de las"],"answer":"a las","tag":"h","sub":"a las + uur"}]}})

# 9 · CLOZE — verbo reflexivo (vormen geverifieerd)
w({"id":"es-u3-reflexivo-cloze","title":"Verbos reflexivos","subtitle":"U3 · kies de juiste reflexieve vorm",
 "lang":"es","template":"cloze","options":{"rounds":10,"audio":False},
 "cloze":{"prompt":"Vul de reflexieve vorm in (pronombre + werkwoord)","items":[
  {"stimulus":"Yo ___ a las siete. (despertarse)","options":["me despierto","me despierta","despierto"],"answer":"me despierto","tag":"r","sub":"yo → me despierto"},
  {"stimulus":"Pau ___ por la mañana. (ducharse)","options":["se ducha","me ducho","te duchas"],"answer":"se ducha","tag":"r","sub":"él → se ducha"},
  {"stimulus":"¿Tú ___ rápido? (vestirse)","options":["te vistes","se viste","me visto"],"answer":"te vistes","tag":"r","sub":"tú → te vistes (e→i)"},
  {"stimulus":"Nosotros ___ temprano. (levantarse)","options":["nos levantamos","se levantan","me levanto"],"answer":"nos levantamos","tag":"r","sub":"nosotros → nos levantamos"},
  {"stimulus":"Mis amigos ___ tarde. (acostarse)","options":["se acuestan","nos acostamos","se acuesta"],"answer":"se acuestan","tag":"r","sub":"ellos → se acuestan (o→ue)"},
  {"stimulus":"Yo ___ los dientes. (lavarse)","options":["me lavo","se lava","te lavas"],"answer":"me lavo","tag":"r","sub":"yo → me lavo"},
  {"stimulus":"Lucía ___ delante del espejo. (peinarse)","options":["se peina","me peino","se peinan"],"answer":"se peina","tag":"r","sub":"ella → se peina"},
  {"stimulus":"¿A qué hora ___ tú? (levantarse)","options":["te levantas","se levanta","me levanto"],"answer":"te levantas","tag":"r","sub":"tú → te levantas"},
  {"stimulus":"Yo ___ a las once. (acostarse)","options":["me acuesto","me acosto","se acuesta"],"answer":"me acuesto","tag":"r","sub":"yo → me acuesto (o→ue)"},
  {"stimulus":"Nosotros ___ pronto. (despertarse)","options":["nos despertamos","me despierto","se despiertan"],"answer":"nos despertamos","tag":"r","sub":"nosotros → geen wissel"}]}})

# 10 · CLOZE — presente irregular (vormen geverifieerd)
w({"id":"es-u3-irregular-cloze","title":"Presente irregular","subtitle":"U3 · kies de juiste onregelmatige vorm",
 "lang":"es","template":"cloze","options":{"rounds":12,"audio":False},
 "cloze":{"prompt":"Vul de juiste presente-vorm in","items":[
  {"stimulus":"Las clases ___ a las nueve. (empezar)","options":["empiezan","empezan","empiezen"],"answer":"empiezan","tag":"v","sub":"ellos → empiezan"},
  {"stimulus":"Yo ___ dormir más. (querer)","options":["quiero","quero","queno"],"answer":"quiero","tag":"v","sub":"yo → quiero"},
  {"stimulus":"¿Tú ___ la tarde? (preferir)","options":["prefieres","preferes","prefires"],"answer":"prefieres","tag":"v","sub":"tú → prefieres"},
  {"stimulus":"Pau ___ un café. (pedir)","options":["pide","pede","piede"],"answer":"pide","tag":"v","sub":"él → pide (e→i)"},
  {"stimulus":"Nosotros ___ a las ocho. (empezar)","options":["empezamos","empiezamos","empezáis"],"answer":"empezamos","tag":"v","sub":"nosotros → geen wissel"},
  {"stimulus":"Yo no ___ salir hoy. (poder)","options":["puedo","podo","puede"],"answer":"puedo","tag":"v","sub":"yo → puedo"},
  {"stimulus":"Pau ___ ocho horas. (dormir)","options":["duerme","dorme","duermo"],"answer":"duerme","tag":"v","sub":"él → duerme"},
  {"stimulus":"Yo ___ los deberes. (hacer)","options":["hago","haco","hazo"],"answer":"hago","tag":"v","sub":"yo → hago"},
  {"stimulus":"Yo ___ al instituto. (ir)","options":["voy","vo","iro"],"answer":"voy","tag":"v","sub":"yo → voy"},
  {"stimulus":"Yo ___ de casa a las ocho. (salir)","options":["salgo","salo","saljo"],"answer":"salgo","tag":"v","sub":"yo → salgo"},
  {"stimulus":"Pau ___ al fútbol. (jugar)","options":["juega","juga","jueja"],"answer":"juega","tag":"v","sub":"él → juega (u→ue)"},
  {"stimulus":"¿Vosotros ___ al parque? (volver)","options":["volvéis","vuelvéis","volváis"],"answer":"volvéis","tag":"v","sub":"vosotros → geen wissel"}]}})

# 11 · CLOZE — frecuencia
w({"id":"es-u3-frecuencia","title":"Adverbios de frecuencia","subtitle":"U3 · kies het juiste frequentiebijwoord",
 "lang":"es","template":"cloze","options":{"rounds":8,"audio":False},
 "cloze":{"prompt":"Welk frequentiebijwoord past?","items":[
  {"stimulus":"___ desayuno (100%).","options":["Siempre","Nunca","A veces"],"answer":"Siempre","tag":"f","sub":"altijd"},
  {"stimulus":"___ llego tarde (0%).","options":["Nunca","Siempre","A menudo"],"answer":"Nunca","tag":"f","sub":"nooit"},
  {"stimulus":"___ ceno tarde (50%).","options":["A veces","Siempre","Nunca"],"answer":"A veces","tag":"f","sub":"soms"},
  {"stimulus":"___ juego al fútbol (80%).","options":["A menudo","Nunca","Casi nunca"],"answer":"A menudo","tag":"f","sub":"vaak"},
  {"stimulus":"___ me levanto pronto (meestal).","options":["Normalmente","Nunca","A veces"],"answer":"Normalmente","tag":"f","sub":"gewoonlijk"},
  {"stimulus":"Voy al cine una ___ por semana.","options":["vez","día","hora"],"answer":"vez","tag":"f","sub":"una vez por semana"},
  {"stimulus":"Estudio ___ los días.","options":["todos","cada","siempre"],"answer":"todos","tag":"f","sub":"todos los días"},
  {"stimulus":"El ___ de semana descanso.","options":["fin","día","hora"],"answer":"fin","tag":"f","sub":"el fin de semana"}]}})

# 12 · TETRIS — presente irregular (generator: stamwissel, nagerekend)
w({"id":"es-u3-irregular-tetris","title":"Presente irregular Tetris","subtitle":"U3 · laat de vorm in de juiste persoon vallen",
 "lang":"es","template":"tetris","options":{"rows":9,"speed":1300,"audio":False},
 "generator":{"kind":"verbo","mode":"person","classes":["ie","ue","i","uue"],"persons":["yo","tu","el","nos","vos","ellos"]},
 "classify":{"categories":[
  {"id":"yo","label":"yo","glaze":G["red"]},{"id":"tu","label":"tú","glaze":G["amber"]},
  {"id":"el","label":"él/ella","glaze":G["green"]},{"id":"nos","label":"nosotros","glaze":G["blue"]},
  {"id":"vos","label":"vosotros","glaze":G["purple"]},{"id":"ellos","label":"ellos","glaze":G["teal"]}]}})

# 13 · TAP — sílaba tónica op rutina-woorden
w({"id":"es-u3-tonica-rutina","title":"La tónica de la rutina","subtitle":"U3 · tik de sterke lettergreep",
 "lang":"es","template":"tap","options":{"rounds":12,"audio":False},
 "tap":{"prompt":"Tik de sílaba tónica (de sterke lettergreep)","joiner":"·","items":[
  {"parts":["des","pier","to"],"answer":1,"tag":"llana","sub":"despierto"},
  {"parts":["me","dio","dí","a"],"answer":2,"tag":"con tilde","sub":"mediodía · hiato"},
  {"parts":["miér","co","les"],"answer":0,"tag":"esdrujula","sub":"miércoles"},
  {"parts":["sá","ba","do"],"answer":0,"tag":"esdrujula","sub":"sábado"},
  {"parts":["ru","ti","na"],"answer":1,"tag":"llana","sub":"rutina"},
  {"parts":["de","sa","yu","no"],"answer":2,"tag":"llana","sub":"desayuno"},
  {"parts":["re","loj"],"answer":1,"tag":"aguda","sub":"reloj"},
  {"parts":["es","ta","ción"],"answer":2,"tag":"aguda","sub":"estación"},
  {"parts":["ve","ra","no"],"answer":1,"tag":"llana","sub":"verano"},
  {"parts":["des","pués"],"answer":1,"tag":"aguda","sub":"después"},
  {"parts":["a","cos","tar","se"],"answer":2,"tag":"llana","sub":"acostarse"},
  {"parts":["fe","bre","ro"],"answer":1,"tag":"llana","sub":"febrero"}]}})

# 14 · ORDER — mi rutina (volgorde)
w({"id":"es-u3-orden-rutina","title":"Ordena mi rutina","subtitle":"U3 · zet de dagacties in de juiste volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik de acties in de logische volgorde van de dag","rounds":[
  {"tag":"rutina","sub":"la mañana","items":[
    {"label":"Me despierto.","key":1},{"label":"Me levanto.","key":2},
    {"label":"Me ducho.","key":3},{"label":"Me visto.","key":4},{"label":"Desayuno.","key":5}]},
  {"tag":"rutina","sub":"el día entero","items":[
    {"label":"Salgo de casa.","key":1},{"label":"Empiezan las clases.","key":2},
    {"label":"Almuerzo al mediodía.","key":3},{"label":"Hago los deberes.","key":4},{"label":"Me acuesto.","key":5}]},
  {"tag":"rutina","sub":"con conectores","items":[
    {"label":"Primero me despierto.","key":1},{"label":"Después desayuno.","key":2},
    {"label":"Luego voy al instituto.","key":3},{"label":"Por fin me acuesto.","key":4}]}]}})

# ========== ④ ANALIZAR & COMUNICAR ==========
# 15 · POINT — caza del reflexivo (klik het reflexieve werkwoord)
w({"id":"es-u3-caza-reflexivo","title":"Caza del reflexivo","subtitle":"U3 · klik ALLE reflexieve werkwoorden",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik ALLE reflexieve werkwoorden (me/te/se)","mode":"all","rounds":[
  {"tag":"ref","sub":"2 reflexivos","targets":[
    {"label":"me levanto","hit":True},{"label":"desayuno"},{"label":"me ducho","hit":True},{"label":"estudio"}]},
  {"tag":"ref","sub":"2 reflexivos","targets":[
    {"label":"ceno"},{"label":"se acuesta","hit":True},{"label":"hago"},{"label":"te vistes","hit":True}]},
  {"tag":"ref","sub":"3 reflexivos","targets":[
    {"label":"me despierto","hit":True},{"label":"almuerzo"},{"label":"se peina","hit":True},{"label":"nos levantamos","hit":True},{"label":"juego"}]},
  {"tag":"ref","sub":"1 reflexivo","targets":[
    {"label":"salgo"},{"label":"voy"},{"label":"me acuesto","hit":True},{"label":"hago"}]}]}})

# 16 · POINT — señala la mañana (dagdeel / hora de la mañana)
w({"id":"es-u3-senala-manana","title":"Señala la mañana","subtitle":"U3 · klik alles wat bij de OCHTEND hoort",
 "lang":"es","template":"point","options":{"audio":False},
 "point":{"prompt":"Klik ALLES wat bij «por la mañana» past","mode":"all","rounds":[
  {"tag":"manana","sub":"acciones de la mañana","targets":[
    {"label":"me levanto","hit":True},{"label":"desayuno","hit":True},{"label":"ceno"},{"label":"me acuesto"}]},
  {"tag":"manana","sub":"horas de la mañana","targets":[
    {"label":"las 7:00","hit":True},{"label":"las 23:00"},{"label":"las 8:15","hit":True},{"label":"las 21:00"}]},
  {"tag":"manana","sub":"acciones de la mañana","targets":[
    {"label":"me ducho","hit":True},{"label":"me visto","hit":True},{"label":"la cena"},{"label":"salgo de casa","hit":True}]}]}})

# 17 · MATCH — hora escrita ↔ hora digital (de la mañana/tarde/noche)
w({"id":"es-u3-hora-digital","title":"El reloj de 24 horas","subtitle":"U3 · koppel de zin aan het 24-uursformaat",
 "lang":"es","template":"match","options":{"chunk":5,"audio":False},
 "match":{"prompt":"Verbind de gesproken tijd met de digitale klok","pairs":[
  {"a":"Son las siete de la mañana","b":"07:00"},{"a":"Son las tres de la tarde","b":"15:00"},
  {"a":"Son las nueve de la noche","b":"21:00"},{"a":"Es la una de la tarde","b":"13:00"},
  {"a":"Son las ocho de la mañana","b":"08:00"},{"a":"Son las once de la noche","b":"23:00"},
  {"a":"Son las cuatro y media de la tarde","b":"16:30"}]}})

# 18 · SIM — describe tu día (vrije productie met bouwstenen)
w({"id":"es-u3-describe-dia","title":"Describe tu día","subtitle":"U3 · schrijf je dag — met alle bouwstenen",
 "lang":"es","template":"sim","options":{"audio":False},
 "sim":{"prompt":"Tarea comunicativa · vertel je dag","rounds":[
  {"scenario":"Cuéntale tu mañana a Pau por chat.","tag":"dia","sub":"gebruik: me levanto · a las … · desayuno","min":10,
   "need":[{"re":"me levanto|me despierto","label":"me levanto/despierto"},{"re":"a las ","label":"a las … (hora)"},{"re":"desayun|me ducho|me visto","label":"una acción más"}],
   "bank":["Me levanto","a las siete","me ducho","desayuno","a las ocho","salgo de casa","primero","después"],
   "model":"Me levanto a las siete, me ducho y desayuno. Después salgo de casa a las ocho."},
  {"scenario":"Describe tu tarde: instituto, deberes, deporte.","tag":"dia","sub":"hora + verbo irregular + conector","min":12,
   "need":[{"re":"empiez|almuerzo|salgo|hago","label":"un verbo del día"},{"re":"a las |por la","label":"cuándo"},{"re":"despu[eé]s|luego|primero","label":"un conector"}],
   "bank":["Las clases empiezan","a las nueve","almuerzo","al mediodía","hago los deberes","por la tarde","luego","juego al fútbol"],
   "model":"Las clases empiezan a las nueve. Al mediodía almuerzo y por la tarde hago los deberes. Luego juego al fútbol."},
  {"scenario":"«¿Qué haces cada día?» Cuenta tu día entero.","tag":"dia","sub":"mañana + tarde + noche + frecuencia","min":14,
   "need":[{"re":"me levanto|me despierto","label":"inicio del día"},{"re":"siempre|a veces|normalmente|nunca|a menudo","label":"frecuencia"},{"re":"me acuesto|ceno","label":"final del día"}],
   "bank":["Normalmente","me levanto a las siete","voy al instituto","almuerzo","por la tarde","hago los deberes","ceno a las nueve","me acuesto a las once"],
   "model":"Normalmente me levanto a las siete y voy al instituto. Almuerzo al mediodía y por la tarde hago los deberes. Ceno a las nueve y me acuesto a las once."}]}})

# ========== ⑤ HABLAR · GRÁBATE ==========
# 19 · SPEAK repeat — la hora
w({"id":"es-u3-repite-hora","title":"Escucha y repite: la hora","subtitle":"U3 · escucha el modelo, repite y GRÁBATE",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · repite la hora · grábate ⏺","items":[
  {"text":"Es la una en punto.","sub":"het is één uur precies","tag":"hora"},
  {"text":"Son las dos y media.","sub":"het is half drie","tag":"hora"},
  {"text":"Son las cinco menos cuarto.","sub":"het is kwart voor vijf","tag":"hora"},
  {"text":"Son las siete de la mañana.","sub":"het is zeven uur 's ochtends","tag":"hora"},
  {"text":"Son las nueve de la noche.","sub":"het is negen uur 's avonds","tag":"hora",
   "tip":"Ahora di la hora que es AHORA, sin leer. <span class='nl'>zeg de tijd van nu, zonder te lezen.</span>"}]}})

# 20 · SPEAK shadowing — la rutina de Pau
w({"id":"es-u3-shadowing-rutina","title":"Shadowing: la rutina de Pau","subtitle":"U3 · imita a Pau — de texto completo a tu versión",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"shadowing","prompt":"Escucha a Pau y ve quitando apoyo, paso a paso",
  "phases":["Texto completo","Palabras clave","Sin texto","Tu versión"],"items":[
  {"text":"Me despierto a las siete y me levanto.","keywords":["Me despierto","a las siete","me levanto"],"sub":"ik word om 7 uur wakker en sta op","tag":"rutina"},
  {"text":"Me ducho, me visto y desayuno.","keywords":["Me ducho","me visto","desayuno"],"sub":"ik douche, kleed me aan en ontbijt","tag":"rutina"},
  {"text":"Salgo de casa a las ocho y voy al instituto.","keywords":["Salgo","a las ocho","voy al instituto"],"sub":"ik vertrek om 8 uur en ga naar school","tag":"rutina"},
  {"text":"Por la tarde hago los deberes y juego al fútbol.","keywords":["Por la tarde","los deberes","juego"],"sub":"'s middags maak ik huiswerk en speel ik voetbal","tag":"rutina"}]}})

# 21 · SPEAK substitution — carrusel: mi día
w({"id":"es-u3-carrusel-dia","title":"Carrusel: cambia la hora","subtitle":"U3 · zelfde zin, andere tijd — grábate en cada vuelta",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"substitution","prompt":"Di la frase con la hora nueva y grábate",
  "frame":"Me levanto a las ___ y ___.","frameLabel":"Modelo · vul de gemarkeerde delen in","items":[
  {"fills":["siete","desayuno"],"sub":"7 uur · ontbijten","tag":"carrusel"},
  {"fills":["seis y media","me ducho"],"sub":"6:30 · douchen","tag":"carrusel"},
  {"fills":["ocho","voy al instituto"],"sub":"8 uur · naar school","tag":"carrusel"},
  {"fills":["diez","el sábado descanso"],"sub":"10 uur · zaterdag","tag":"carrusel"},
  {"fills":["___","___"],"sub":"nu met JOUW echte dag — ¡cuéntalo tú!","tag":"carrusel",
   "tip":"¡Ahora tú de verdad! Grábate con tu hora real. <span class='nl'>neem jezelf op met je échte uur.</span>"}]}})

# 22 · SPEAK voicemessage — mensaje de voz: mi día
w({"id":"es-u3-mensaje-dia","title":"Mensaje de voz: mi día","subtitle":"U3 · graba UN mensaje sobre tu día",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"voicemessage","prompt":"Graba un mensaje de voz · spraakbericht opnemen","items":[
  {"to":"Pau, de Barcelona","situation":"Pau te pregunta cómo es un día tuyo.","goal":"Cuéntale tu rutina con horas.",
   "blocks":["saludo (¡Hola, Pau!)","me levanto a las …","por la mañana …","por la tarde …","me acuesto a las …"],
   "sub":"Pau — vertel je routine met tijden","tag":"mensaje"},
  {"to":"Tu familia de acogida en España","situation":"Vas de intercambio y les explicas tu horario.","goal":"Diles a qué hora te levantas, comes y te acuestas.",
   "blocks":["saludo","me despierto a las …","almuerzo a las …","ceno a las …","normalmente / a veces …","despedida"],
   "sub":"je gastgezin — je uren van de dag","tag":"mensaje",
   "tip":"Escucha tu mensaje: ¿se entienden las horas? Vuelve a grabar más despacio. <span class='nl'>beluister jezelf; herneem rustiger.</span>"}]}})

# 23 · SPEAK repeat — describe la rutina de Pau (3ª persona)
w({"id":"es-u3-describe-pau","title":"Describe la rutina de Pau","subtitle":"U3 · escucha, describe a Pau en 3ª persona, y grábate",
 "lang":"es","template":"speak","options":{"audio":False},
 "speak":{"mode":"repeat","prompt":"Escucha ▶ · describe a Pau (él) · grábate ⏺","items":[
  {"cue":"Pau · Barcelona 🇪🇸","text":"Pau se despierta a las siete.","sub":"hij wordt om 7 uur wakker — «se despierta»","tag":"describir"},
  {"cue":"Pau · Barcelona 🇪🇸","text":"Se ducha y desayuna un bocadillo.","sub":"hij doucht en ontbijt een broodje","tag":"describir"},
  {"cue":"Pau · Barcelona 🇪🇸","text":"Va al instituto en metro.","sub":"hij gaat met de metro naar school","tag":"describir"},
  {"cue":"Pau · Barcelona 🇪🇸","text":"Por la tarde hace los deberes y juega al fútbol.","sub":"'s middags maakt hij huiswerk en speelt hij voetbal","tag":"describir"},
  {"cue":"Pau · Barcelona 🇪🇸","text":"Se acuesta a las once.","sub":"hij gaat om 11 uur slapen","tag":"describir",
   "tip":"Ahora describe la rutina de un amigo tuyo. <span class='nl'>beschrijf nu de dag van een echte vriend(in).</span>"}]}})

# 24 · ORDER — mi día (horario completo)
w({"id":"es-u3-orden-dia","title":"Ordena el día de Pau","subtitle":"U3 · zet Pau's dag op de juiste tijd-volgorde",
 "lang":"es","template":"order","options":{"audio":False},
 "order":{"prompt":"Tik de momenten in de juiste volgorde van de klok","rounds":[
  {"tag":"dia","sub":"según la hora","items":[
    {"label":"7:00 · se despierta","key":1},{"label":"8:00 · sale de casa","key":2},
    {"label":"9:00 · empiezan las clases","key":3},{"label":"14:30 · almuerza","key":4},{"label":"23:00 · se acuesta","key":5}]},
  {"tag":"dia","sub":"según la hora","items":[
    {"label":"6:30 · me levanto","key":1},{"label":"7:15 · desayuno","key":2},
    {"label":"13:00 · como","key":3},{"label":"18:00 · hago deporte","key":4},{"label":"22:00 · ceno","key":5}]}]}})

print("\n24 U3-spellen geschreven (10 templates: match·memory·classify·cloze·tetris·tap·order·point·sim·speak).")
