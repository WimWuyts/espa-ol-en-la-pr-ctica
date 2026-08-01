#!/usr/bin/env python3
"""Luisterfragmenten per cursus en unit — één bron, drie afnemers.

Hetzelfde `guion` voedt drie dingen:
  * de mp3 (`gen_audio_elevenlabs.py`, per spreker een vaste stem);
  * het meelees-transcript in de hub (klik-om-te-horen per regel);
  * de browser-TTS-terugval zolang er nog geen mp3 is.

De begripstaken staan hier ook, zodat print en hub dezelfde vragen stellen: de
printcursus geeft ze met antwoordruimte + QR, de hub zelfcorrigerend.

De ladder heeft zes treden (VIER_VAARDIGHEDEN_GEINTEGREERD.md):
situatie vooraf -> globaal begrip -> vijf detailvragen -> juist/fout met bewijs
-> transcript pas NA de taken -> productieve reactie.

Afspraak met de auteur (2026-07-30): per unit één leestekst EN één
luisterfragment, met verschillende inhoud, elk op twee dragers (print + hub).
Het luisterfragment is dus geen voorgelezen versie van de leestekst.
"""

# ---------------------------------------------------------------------------
# C5 · U0 — parada: El mundo hispano -> España
# Tekstsoort: dialoog. De leestekst van deze unit is een aanplakbiljet, zodat
# de twee vaardigheden een ander tekstgenre oefenen.
# ---------------------------------------------------------------------------
C5_U0 = {
    "id": "C5-U0-ESC-01",
    "ancla": "c5-u0-esc-01",
    "titulo": "En la puerta de embarque",
    "audio": "audio/C5_U0.mp3",
    "situacion": {
        "lugar": "El aeropuerto de Barajas, Madrid — puerta B12",
        "quien": "Lucía (de Sevilla) y tú",
        "que": "Esperáis el mismo vuelo y os presentáis",
        "claves": ["¿Cómo te llamas?", "Soy de…", "¿Cómo se escribe?"],
    },
    "guion": [
        {"who": "Lucía", "es": "¡Hola! Perdona… ¿este es el vuelo a Sevilla?",
         "nl": "Hallo! Sorry… is dit de vlucht naar Sevilla?"},
        {"who": "Tú", "es": "Sí, la puerta B doce. ¡Hola!",
         "nl": "Ja, gate B twaalf. Hallo!"},
        {"who": "Lucía", "es": "¡Qué bien! Me llamo Lucía. ¿Y tú? ¿Cómo te llamas?",
         "nl": "Wat fijn! Ik heet Lucía. En jij? Hoe heet jij?"},
        {"who": "Tú", "es": "Me llamo Sam. Encantado.",
         "nl": "Ik heet Sam. Aangenaam."},
        {"who": "Lucía", "es": "¿Sam? ¿Cómo se escribe?",
         "nl": "Sam? Hoe schrijf je dat?"},
        {"who": "Tú", "es": "Ese, a, eme. Sam.",
         "nl": "S, a, m. Sam."},
        {"who": "Lucía", "es": "Vale. Yo soy de Sevilla. ¿De dónde eres tú?",
         "nl": "Oké. Ik kom uit Sevilla. Waar kom jij vandaan?"},
        {"who": "Tú", "es": "Soy de Bélgica, de Gante. Hablo neerlandés y un poco de español.",
         "nl": "Ik kom uit België, uit Gent. Ik spreek Nederlands en een beetje Spaans."},
        {"who": "Lucía", "es": "¡Muy bien! ¿Y cuántos años tienes?",
         "nl": "Heel goed! En hoe oud ben je?"},
        {"who": "Tú", "es": "Tengo dieciséis años. ¿Y tú?",
         "nl": "Ik ben zestien. En jij?"},
        {"who": "Lucía", "es": "Diecisiete. Oye, el vuelo sale a las once.",
         "nl": "Zeventien. Zeg, de vlucht vertrekt om elf uur."},
        {"who": "Tú", "es": "Entonces tenemos tiempo. ¡Hasta luego, Lucía!",
         "nl": "Dan hebben we tijd. Tot straks, Lucía!"},
    ],
    "global": {
        "q": "¿De qué hablan Lucía y Sam?",
        "opts": ["Se presentan antes del vuelo", "Compran billetes de avión",
                 "Hablan del tiempo en Sevilla"],
        "ans": "Se presentan antes del vuelo",
        "why": "nombre + origen + edad = presentarse",
    },
    "detalle": [
        {"q": "¿Cuál es la puerta de embarque?", "opts": ["B12", "B2", "B20"], "ans": "B12",
         "why": "«la puerta B doce»"},
        {"q": "¿De dónde es Lucía?", "opts": ["De Sevilla", "De Madrid", "De Gante"], "ans": "De Sevilla"},
        {"q": "¿Cuántos años tiene Sam?", "opts": ["16", "17", "11"], "ans": "16",
         "why": "«Tengo dieciséis años»"},
        {"q": "¿Cuántos años tiene Lucía?", "opts": ["17", "16", "12"], "ans": "17"},
        {"q": "¿A qué hora sale el vuelo?", "opts": ["A las once", "A las doce", "A las diez"],
         "ans": "A las once"},
    ],
    "vf": [
        {"q": "Sam habla dos lenguas.", "ans": True, "prueba": "Hablo neerlandés y un poco de español"},
        {"q": "Lucía es de Madrid.", "ans": False, "prueba": "Yo soy de Sevilla"},
        {"q": "Sam deletrea su nombre.", "ans": True, "prueba": "Ese, a, eme"},
    ],
    "produccion": {
        "prompt": "Lucía te pregunta: «¿Y tú, cómo te llamas y de dónde eres?» "
                  "Contesta en tres frases: nombre · origen · edad.",
        "modo": "escribir", "min": 15,
    },
}

# ---------------------------------------------------------------------------
# C6+ · U0 — repaso: presente, concordancia, países
# Tekstsoort: dialoog op school. De leestekst is een prikbord-aankondiging.
# ---------------------------------------------------------------------------
C6P_U0 = {
    "id": "C6P-U0-ESC-01",
    "ancla": "c6p-u0-esc-01",
    "titulo": "El primer día de curso",
    "audio": "audio/C6plus_U0.mp3",
    "situacion": {
        "lugar": "El patio del instituto, primera semana de septiembre",
        "quien": "Diego (de México) y Valen (de Cartagena, Colombia)",
        "que": "Se reencuentran y hablan de sus clases y de un compañero nuevo",
        "claves": ["¿Qué tal el verano?", "somos / estamos", "el compañero nuevo"],
    },
    "guion": [
        {"who": "Diego", "es": "¡Valen! ¿Qué tal el verano?",
         "nl": "Valen! Hoe was de zomer?"},
        {"who": "Valen", "es": "¡Genial! Estoy muy contenta. Estuve en Cartagena con mi familia.",
         "nl": "Geweldig! Ik ben heel blij. Ik was in Cartagena met mijn familie."},
        {"who": "Diego", "es": "¡Qué suerte! Yo estoy un poco cansado. El viaje desde México es largo.",
         "nl": "Wat een geluk! Ik ben een beetje moe. De reis vanuit Mexico is lang."},
        {"who": "Valen", "es": "Oye, ¿sabes que hay un compañero nuevo? Se llama Mateo.",
         "nl": "Zeg, weet je dat er een nieuwe klasgenoot is? Hij heet Mateo."},
        {"who": "Diego", "es": "¿Mateo? ¿De dónde es?",
         "nl": "Mateo? Waar komt hij vandaan?"},
        {"who": "Valen", "es": "Es argentino, de Buenos Aires. Es muy simpático y habla rapidísimo.",
         "nl": "Hij is Argentijn, uit Buenos Aires. Hij is heel aardig en praat razendsnel."},
        {"who": "Diego", "es": "¿Y en qué clase está?",
         "nl": "En in welke klas zit hij?"},
        {"who": "Valen", "es": "Está en nuestra clase. Somos veinticuatro este año.",
         "nl": "Hij zit in onze klas. We zijn dit jaar met vierentwintig."},
        {"who": "Diego", "es": "¡Veinticuatro! Somos muchos. ¿Y la profesora de español?",
         "nl": "Vierentwintig! We zijn met veel. En de lerares Spaans?"},
        {"who": "Valen", "es": "Es la misma, la señora Ortega. Sus clases son los martes y los jueves.",
         "nl": "Dezelfde, mevrouw Ortega. Haar lessen zijn op dinsdag en donderdag."},
        {"who": "Diego", "es": "Perfecto. Entonces estamos listos. ¡Vamos!",
         "nl": "Perfect. Dan zijn we er klaar voor. Kom!"},
    ],
    "global": {
        "q": "¿De qué hablan Diego y Valen?",
        "opts": ["Del nuevo curso y de un compañero nuevo", "De un examen de español",
                 "De un viaje a Argentina"],
        "ans": "Del nuevo curso y de un compañero nuevo",
        "why": "verano + clase + compañero nuevo + horario",
    },
    "detalle": [
        {"q": "¿Cómo se llama el compañero nuevo?", "opts": ["Mateo", "Diego", "Ortega"], "ans": "Mateo"},
        {"q": "¿De dónde es Mateo?", "opts": ["De Buenos Aires", "De Cartagena", "De México"],
         "ans": "De Buenos Aires"},
        {"q": "¿Cuántos alumnos son este año?", "opts": ["24", "14", "22"], "ans": "24",
         "why": "«Somos veinticuatro»"},
        {"q": "¿Cómo está Diego?", "opts": ["Cansado", "Contento", "Nervioso"], "ans": "Cansado",
         "why": "estar + estado: «estoy un poco cansado»"},
        {"q": "¿Qué días hay clase de español?", "opts": ["Martes y jueves", "Lunes y miércoles",
                                                          "Jueves y viernes"], "ans": "Martes y jueves"},
    ],
    "vf": [
        {"q": "Valen pasó el verano en Colombia.", "ans": True, "prueba": "Estuve en Cartagena"},
        {"q": "Mateo está en otra clase.", "ans": False, "prueba": "Está en nuestra clase"},
        {"q": "La profesora de español es nueva.", "ans": False, "prueba": "Es la misma"},
    ],
    "produccion": {
        "prompt": "Eres el compañero nuevo. Preséntate a Diego y a Valen en cuatro frases: "
                  "nombre · origen · cómo estás hoy · una cosa que te gusta.",
        "modo": "grabar",
    },
}

# ---------------------------------------------------------------------------
# C5 · U1 — diálogo. Andere tekstsoort dan de lectura van deze unit (een perfil),
# zodat lezen en luisteren niet twee keer hetzelfde vragen.
# ---------------------------------------------------------------------------
C5_U1 = {
    "id": "C5-U1-ESC-01",
    "ancla": "c5-u1-esc-01",
    "titulo": "El primer día en el instituto",
    "audio": "audio/C5_U1.mp3",
    "situacion": {
        "lugar": "El pasillo del IES Cervantes, Madrid",
        "quien": "Álex (de Madrid) y Sam, un alumno nuevo de Bélgica",
        "que": "Se conocen y se hacen preguntas",
        "claves": ["¿cómo te llamas?", "¿de dónde eres?", "¿cuántos años tienes?"],
    },
    "guion": [
        {"who": "Álex", "es": "¡Hola! Tú eres nuevo, ¿verdad? Yo soy Álex.",
         "nl": "Hallo! Jij bent nieuw, hè? Ik ben Álex."},
        {"who": "Sam", "es": "Sí, soy nuevo. Me llamo Sam.", "nl": "Ja, ik ben nieuw. Ik heet Sam."},
        {"who": "Álex", "es": "¿Cómo se escribe? ¿Con ce o con ese?",
         "nl": "Hoe schrijf je dat? Met een c of met een s?"},
        {"who": "Sam", "es": "Con ese: ese, a, eme.", "nl": "Met een s: s, a, m."},
        {"who": "Álex", "es": "Vale. ¿Y de dónde eres, Sam?", "nl": "Oké. En waar kom jij vandaan, Sam?"},
        {"who": "Sam", "es": "Soy de Bélgica, de Amberes. Soy belga.",
         "nl": "Ik kom uit België, uit Antwerpen. Ik ben Belg."},
        {"who": "Álex", "es": "¡Qué bien! ¿Y cuántos años tienes?", "nl": "Wat leuk! En hoe oud ben je?"},
        {"who": "Sam", "es": "Tengo quince años. ¿Y tú?", "nl": "Ik ben vijftien. En jij?"},
        {"who": "Álex", "es": "Yo tengo dieciséis. Estudio francés y tú, ¿qué estudias?",
         "nl": "Ik ben zestien. Ik studeer Frans, en jij, wat studeer je?"},
        {"who": "Sam", "es": "Estudio español, claro. Y también inglés.",
         "nl": "Spaans natuurlijk. En ook Engels."},
        {"who": "Álex", "es": "Oye, ¿tienes hermanos?", "nl": "Zeg, heb je broers of zussen?"},
        {"who": "Sam", "es": "Tengo una hermana. Se llama Anna y tiene doce años.",
         "nl": "Ik heb een zus. Ze heet Anna en ze is twaalf."},
    ],
    "global": {
        "q": "¿Qué hacen Álex y Sam?",
        "opts": ["Se presentan y se hacen preguntas", "Hablan de un examen",
                 "Compran material escolar"],
        "ans": "Se presentan y se hacen preguntas",
    },
    "detalle": [
        {"q": "¿Cómo se escribe el nombre de Sam?", "opts": ["Con ese", "Con ce", "Con zeta"],
         "ans": "Con ese", "why": "«Con ese: ese, a, eme»"},
        {"q": "¿De dónde es Sam?", "opts": ["De Amberes, Bélgica", "De Madrid", "De Sevilla"],
         "ans": "De Amberes, Bélgica", "why": "«Soy de Bélgica, de Amberes»"},
        {"q": "¿Cuántos años tiene Sam?", "opts": ["15", "16", "12"], "ans": "15",
         "why": "«Tengo quince años»"},
        {"q": "¿Qué lengua estudia Álex?", "opts": ["Francés", "Alemán", "Italiano"],
         "ans": "Francés", "why": "«Estudio francés»"},
        {"q": "¿Cuántos años tiene la hermana de Sam?", "opts": ["12", "15", "16"], "ans": "12",
         "why": "«tiene doce años»"},
    ],
    "vf": [
        {"q": "Álex tiene dieciséis años.", "ans": True, "prueba": "yo tengo dieciséis"},
        {"q": "Sam estudia alemán.", "ans": False, "prueba": "estudio español, claro"},
        {"q": "Sam tiene una hermana.", "ans": True, "prueba": "tengo una hermana"},
    ],
    "produccion": {
        "prompt": "Álex te pregunta a ti: «¿Cómo te llamas, de dónde eres y cuántos años tienes?» "
                  "Contesta en tres frases y añade una pregunta para él.",
        "modo": "escribir",
        "min": 3,
        "modelo": "Me llamo… Soy de… Tengo… años. Y tú, ¿…?",
    },
}


# ---------------------------------------------------------------------------
# C6+ · U1 — entrevista. De lectura van deze unit is een blog; het interview
# vraagt dezelfde leerstof (rutina, la hora, gustar) via een andere tekstsoort.
# ---------------------------------------------------------------------------
C6P_U1 = {
    "id": "C6P-U1-ESC-01",
    "ancla": "c6p-u1-esc-01",
    "titulo": "Entrevista a un deportista",
    "audio": "audio/C6plus_U1.mp3",
    "situacion": {
        "lugar": "La radio del instituto, Salamanca",
        "quien": "Una periodista escolar y Hugo, nadador de dieciocho años",
        "que": "Le pregunta por su rutina y por lo que le gusta",
        "claves": ["¿a qué hora?", "me levanto", "me gusta"],
    },
    "guion": [
        {"who": "Periodista", "es": "Hugo, gracias por venir. ¿A qué hora te levantas?",
         "nl": "Hugo, bedankt dat je er bent. Hoe laat sta je op?"},
        {"who": "Hugo", "es": "Me levanto a las cinco y media. Muy temprano, sí.",
         "nl": "Ik sta om half zes op. Heel vroeg, ja."},
        {"who": "Periodista", "es": "¿Y qué haces primero?", "nl": "En wat doe je eerst?"},
        {"who": "Hugo", "es": "Me ducho, desayuno mucho y voy a la piscina en bici.",
         "nl": "Ik douche, ontbijt veel en ga met de fiets naar het zwembad."},
        {"who": "Periodista", "es": "¿Cuántas horas entrenas al día?",
         "nl": "Hoeveel uur train je per dag?"},
        {"who": "Hugo", "es": "Entreno cuatro horas: dos por la mañana y dos por la tarde.",
         "nl": "Ik train vier uur: twee 's ochtends en twee 's middags."},
        {"who": "Periodista", "es": "¿Te gusta madrugar?", "nl": "Hou je ervan om vroeg op te staan?"},
        {"who": "Hugo", "es": "No, no me gusta nada. Pero me gustan mucho las carreras.",
         "nl": "Nee, helemaal niet. Maar ik hou wel erg van de wedstrijden."},
        {"who": "Periodista", "es": "¿Estudias también?", "nl": "Studeer je ook?"},
        {"who": "Hugo", "es": "Sí, estudio por la noche. Estoy cansado, pero estoy contento.",
         "nl": "Ja, ik studeer 's avonds. Ik ben moe, maar ik ben tevreden."},
        {"who": "Periodista", "es": "Última pregunta: ¿a qué hora te acuestas?",
         "nl": "Laatste vraag: hoe laat ga je slapen?"},
        {"who": "Hugo", "es": "Me acuesto a las diez. ¡Y me duermo en dos minutos!",
         "nl": "Ik ga om tien uur slapen. En ik val binnen twee minuten in slaap!"},
    ],
    "global": {
        "q": "¿De qué habla Hugo en la entrevista?",
        "opts": ["De su rutina y de sus gustos", "De un viaje al extranjero",
                 "De sus problemas en clase"],
        "ans": "De su rutina y de sus gustos",
    },
    "detalle": [
        {"q": "¿A qué hora se levanta Hugo?", "opts": ["A las cinco y media", "A las seis y media",
                                                       "A las siete"], "ans": "A las cinco y media",
         "why": "«Me levanto a las cinco y media»"},
        {"q": "¿Cómo va a la piscina?", "opts": ["En bici", "En autobús", "Andando"],
         "ans": "En bici", "why": "«voy a la piscina en bici»"},
        {"q": "¿Cuántas horas entrena al día?", "opts": ["Cuatro", "Dos", "Seis"],
         "ans": "Cuatro", "why": "«Entreno cuatro horas»"},
        {"q": "¿Cuándo estudia?", "opts": ["Por la noche", "Por la mañana", "No estudia"],
         "ans": "Por la noche", "why": "«estudio por la noche»"},
        {"q": "¿A qué hora se acuesta?", "opts": ["A las diez", "A las once", "A las nueve"],
         "ans": "A las diez", "why": "«Me acuesto a las diez»"},
    ],
    "vf": [
        {"q": "A Hugo le gusta madrugar.", "ans": False, "prueba": "no me gusta nada"},
        {"q": "A Hugo le gustan las carreras.", "ans": True, "prueba": "me gustan mucho las carreras"},
        {"q": "Hugo se ducha antes de desayunar.", "ans": True, "prueba": "me ducho, desayuno mucho"},
    ],
    "produccion": {
        "prompt": "Contesta tú a la periodista: ¿a qué hora te levantas, qué haces primero, "
                  "qué te gusta y qué no te gusta, y a qué hora te acuestas?",
        "modo": "escribir",
        "min": 4,
        "modelo": "Me levanto a las… Primero me… Me gusta… pero no me gusta… Me acuesto a las…",
    },
}


# ---------------------------------------------------------------------------
# C5 · U2 — concurso de clase «¿Quién es quién?». De leestekst van deze unit is
# een mail over Lucía's familie; hier gaat het over het beschríjven van onbekende
# gezichten. Andere inhoud, andere personen, ander genre (spelprogramma in plaats
# van gesprek): de leerling moet écht luisteren naar het uiterlijk, niet naar de
# familiebanden.
# ---------------------------------------------------------------------------
C5_U2 = {
    "id": "C5-U2-ESC-01",
    "ancla": "c5-u2-esc-01",
    "titulo": "¿Quién es quién? — el concurso de la clase",
    "audio": "audio/C5_U2.mp3",
    "situacion": {
        "lugar": "El aula de español — diez fotos en la pizarra",
        "quien": "La profesora y dos concursantes: Diego y Nina",
        "que": "La profesora describe a una persona y ellos adivinan quién es",
        "claves": ["tiene el pelo…", "lleva gafas / barba", "es tímido / hablador"],
    },
    "guion": [
        {"who": "Profesora", "es": "¡Bienvenidos al concurso «¿Quién es quién?»! Diego, Nina: "
                                   "tenéis diez fotos delante.",
         "nl": "Welkom bij de quiz «Wie is wie?»! Diego, Nina: jullie hebben tien foto's voor je."},
        {"who": "Diego", "es": "¡Estamos listos!", "nl": "We zijn er klaar voor!"},
        {"who": "Profesora", "es": "Número uno. Es alta, tiene el pelo largo y rizado y lleva gafas.",
         "nl": "Nummer één. Ze is groot, ze heeft lang krullend haar en ze draagt een bril."},
        {"who": "Diego", "es": "¿Es Rocío?", "nl": "Is het Rocío?"},
        {"who": "Profesora", "es": "No. Rocío tiene el pelo corto. Segunda pista: es muy habladora.",
         "nl": "Nee. Rocío heeft kort haar. Tweede aanwijzing: ze praat heel veel."},
        {"who": "Nina", "es": "¡Es Elena!", "nl": "Het is Elena!"},
        {"who": "Profesora", "es": "¡Correcto! Un punto para Nina. Número dos: es un chico moreno "
                                   "y lleva barba.",
         "nl": "Juist! Een punt voor Nina. Nummer twee: het is een donkere jongen met een baard."},
        {"who": "Diego", "es": "¿Cuántos años tiene?", "nl": "Hoe oud is hij?"},
        {"who": "Profesora", "es": "Tiene veintidós años. Es tímido, pero es muy simpático.",
         "nl": "Hij is tweeëntwintig. Hij is verlegen, maar heel aardig."},
        {"who": "Diego", "es": "¡Es Javi!", "nl": "Het is Javi!"},
        {"who": "Profesora", "es": "¡Muy bien, Diego! Uno a uno. Y la última foto: es pelirroja, "
                                   "es baja y es muy graciosa.",
         "nl": "Heel goed, Diego! Eén-één. En de laatste foto: ze heeft rood haar, ze is klein "
               "en ze is heel grappig."},
        {"who": "Nina", "es": "¿Es la abuela de Elena?", "nl": "Is het de oma van Elena?"},
        {"who": "Profesora", "es": "Sí, es Rosario. ¡Dos a uno! Gana Nina.",
         "nl": "Ja, het is Rosario. Twee-één! Nina wint."},
    ],
    "global": {
        "q": "¿Qué hacen en el concurso?",
        "opts": ["Adivinan quién es cada persona por la descripción",
                 "Cuentan su rutina de la mañana", "Preparan un examen de gramática"],
        "ans": "Adivinan quién es cada persona por la descripción",
        "why": "descripción física + carácter → adivinar",
    },
    "detalle": [
        {"q": "¿Cómo tiene el pelo la persona número uno?",
         "opts": ["Largo y rizado", "Corto y liso", "Largo y liso"], "ans": "Largo y rizado",
         "why": "«tiene el pelo largo y rizado»"},
        {"q": "¿Quién es la persona número uno?", "opts": ["Elena", "Rocío", "Rosario"],
         "ans": "Elena", "why": "Rocío valt af: die heeft kort haar."},
        {"q": "¿Cuántos años tiene Javi?", "opts": ["22", "20", "12"], "ans": "22",
         "why": "«Tiene veintidós años»"},
        {"q": "¿Cómo es Javi de carácter?", "opts": ["Tímido pero simpático", "Hablador", "Antipático"],
         "ans": "Tímido pero simpático", "why": "«Es tímido, pero es muy simpático»"},
        {"q": "¿Quién gana el concurso?", "opts": ["Nina", "Diego", "Nadie"], "ans": "Nina",
         "why": "«¡Dos a uno! Gana Nina»"},
    ],
    "vf": [
        {"q": "Rocío tiene el pelo largo.", "ans": False, "prueba": "rocío tiene el pelo corto"},
        {"q": "Elena habla mucho.", "ans": True, "prueba": "es muy habladora"},
        {"q": "Javi lleva barba.", "ans": True, "prueba": "es un chico moreno y lleva barba"},
    ],
    "produccion": {
        "prompt": "Juega tú. Describe a alguien de tu clase sin decir su nombre, en cuatro frases: "
                  "el pelo · los ojos · alto o bajo · el carácter. Tus compañeros adivinan.",
        "modo": "grabar",
        "modelo": "Es… Tiene el pelo… y los ojos… Lleva… Es muy… ¿Quién es?",
    },
}


# ---------------------------------------------------------------------------
# C6+ · U2 — llamada de teléfono. De leestekst van deze unit beoordeelt een
# woning; hier moet de leerling een wég volgen. Andere inhoud, andere taalhandeling
# (instructies opvolgen in plaats van meningen wegen), en luisteren naar
# richtingen kan alleen mét het oor: op papier zou de leerling terugbladeren.
# ---------------------------------------------------------------------------
C6P_U2 = {
    "id": "C6P-U2-ESC-01",
    "ancla": "c6p-u2-esc-01",
    "titulo": "Estoy perdido en Cartagena",
    "audio": "audio/C6plus_U2.mp3",
    "situacion": {
        "lugar": "Por teléfono — Sam está en algún lugar del centro histórico",
        "quien": "Sam (perdido) y Valen (en su casa)",
        "que": "Valen le explica el camino paso a paso",
        "claves": ["sigue recto", "gira a la derecha", "está a … minutos"],
    },
    "guion": [
        {"who": "Valen", "es": "¿Sí? ¿Sam? ¿Dónde estás?", "nl": "Ja? Sam? Waar ben je?"},
        {"who": "Sam", "es": "Estoy perdido. Estoy buscando tu calle, pero no la encuentro.",
         "nl": "Ik ben verdwaald. Ik zoek jouw straat, maar ik vind hem niet."},
        {"who": "Valen", "es": "Tranquilo. ¿Qué ves?", "nl": "Rustig maar. Wat zie je?"},
        {"who": "Sam", "es": "Hay una plaza grande con muchos coches amarillos. Y hay una torre "
                             "con un reloj.",
         "nl": "Er is een groot plein met veel gele auto's. En er is een toren met een klok."},
        {"who": "Valen", "es": "¡Ah! Estás en la Plaza de los Coches, debajo de la Torre del "
                               "Reloj. Estás muy cerca.",
         "nl": "Ah! Je staat op de Plaza de los Coches, onder de Torre del Reloj. Je bent vlakbij."},
        {"who": "Sam", "es": "¿Sí? ¡Qué bien!", "nl": "Echt? Wat fijn!"},
        {"who": "Valen", "es": "Mira: sigue recto por la calle grande y en el segundo semáforo "
                               "gira a la derecha.",
         "nl": "Kijk: ga rechtdoor de grote straat in en sla bij het tweede stoplicht rechts af."},
        {"who": "Sam", "es": "Vale… a la derecha en el segundo semáforo.",
         "nl": "Oké… rechts bij het tweede stoplicht."},
        {"who": "Valen", "es": "Después cruza la plaza pequeña. Mi calle está a la izquierda, "
                               "al lado de una farmacia verde.",
         "nl": "Steek daarna het kleine plein over. Mijn straat ligt links, naast een groene apotheek."},
        {"who": "Sam", "es": "¿Y tu casa?", "nl": "En jouw huis?"},
        {"who": "Valen", "es": "Es la casa azul, entre la farmacia y una tienda de sombreros. "
                               "Está a cinco minutos a pie.",
         "nl": "Het is het blauwe huis, tussen de apotheek en een hoedenwinkel. Het is vijf "
               "minuten te voet."},
        {"who": "Sam", "es": "Perfecto. Ya estoy andando. ¡Hasta ahora!",
         "nl": "Perfect. Ik ben al onderweg. Tot zo!"},
        {"who": "Valen", "es": "¡Te espero en el balcón!", "nl": "Ik wacht op je op het balkon!"},
    ],
    "global": {
        "q": "¿Qué hace Valen por teléfono?",
        "opts": ["Le explica a Sam cómo llegar a su casa", "Le invita a una fiesta",
                 "Le describe su habitación"],
        "ans": "Le explica a Sam cómo llegar a su casa",
        "why": "sigue · gira · cruza = het pad, niet de woning",
    },
    "detalle": [
        {"q": "¿Dónde está Sam al principio?",
         "opts": ["En la Plaza de los Coches", "En el parque", "En la estación"],
         "ans": "En la Plaza de los Coches", "why": "«Estás en la Plaza de los Coches»"},
        {"q": "¿Qué monumento ve Sam?", "opts": ["La Torre del Reloj", "La catedral", "La muralla"],
         "ans": "La Torre del Reloj", "why": "«una torre con un reloj»"},
        {"q": "¿En qué semáforo tiene que girar?", "opts": ["En el segundo", "En el primero", "En el tercero"],
         "ans": "En el segundo", "why": "«en el segundo semáforo gira a la derecha»"},
        {"q": "¿Qué hay al lado de la calle de Valen?",
         "opts": ["Una farmacia verde", "Un banco", "Un supermercado"], "ans": "Una farmacia verde",
         "why": "«al lado de una farmacia verde»"},
        {"q": "¿A cuántos minutos está la casa?", "opts": ["Cinco", "Quince", "Dos"], "ans": "Cinco",
         "why": "«Está a cinco minutos a pie»"},
    ],
    "vf": [
        {"q": "Sam sabe dónde está su calle.", "ans": False,
         "prueba": "estoy buscando tu calle, pero no la encuentro"},
        {"q": "La casa de Valen es azul.", "ans": True, "prueba": "es la casa azul"},
        {"q": "Valen espera a Sam en el balcón.", "ans": True, "prueba": "te espero en el balcón"},
    ],
    "produccion": {
        "prompt": "Ahora tú. Alguien está en la parada de tu barrio y quiere llegar a tu casa. "
                  "Explícale el camino en cuatro frases: sigue recto · gira · cruza · "
                  "está a … minutos.",
        "modo": "grabar",
        "modelo": "Sigue recto por la calle… En el… semáforo gira a la… Cruza… Mi casa está "
                  "al lado de… Está a … minutos a pie.",
    },
}


# ---------------------------------------------------------------------------
# C5 · U3 — mensajes de voz. De leestekst van deze unit is een chat waarin twee
# klasgenoten een gaatje zoeken; hier vertelt Pau één zaterdag van begin tot eind.
# Ander genre (gesproken monoloog in plaats van geschreven beurten) en andere
# inhoud: daar plannen, hier vertellen.
# ---------------------------------------------------------------------------
C5_U3 = {
    "id": "C5-U3-ESC-01",
    "ancla": "c5-u3-esc-01",
    "titulo": "Mi sábado en Barcelona",
    "audio": "audio/C5_U3.mp3",
    "situacion": {
        "lugar": "En el móvil: unos audios entre Bélgica y Barcelona",
        "quien": "Sam (Bélgica) y Pau (Barcelona)",
        "que": "Pau le cuenta cómo es un sábado normal para él",
        "claves": ["me levanto / me despierto", "primero… después…", "una vez por semana"],
    },
    "guion": [
        {"who": "Sam", "es": "¡Hola, Pau! Una pregunta para la clase de español: ¿cómo es un "
                             "sábado normal para ti?",
         "nl": "Hallo Pau! Een vraag voor de Spaanse les: hoe ziet een gewone zaterdag er bij "
               "jou uit?"},
        {"who": "Pau", "es": "¡Buena pregunta! Pues mira: entre semana me levanto a las siete, "
                             "pero el sábado no. El sábado me despierto a las nueve.",
         "nl": "Goede vraag! Kijk: doordeweeks sta ik om zeven uur op, maar op zaterdag niet. "
               "Op zaterdag word ik om negen uur wakker."},
        {"who": "Pau", "es": "Me ducho, desayuno con mi hermana y a las once salgo de casa.",
         "nl": "Ik douche, ontbijt met mijn zus en om elf uur ga ik de deur uit."},
        {"who": "Pau", "es": "Voy en metro hasta la Sagrada Familia. Allí trabajo tres horas: "
                             "enseño el barrio a los turistas.",
         "nl": "Ik ga met de metro naar de Sagrada Família. Daar werk ik drie uur: ik laat "
               "toeristen de wijk zien."},
        {"who": "Pau", "es": "Almuerzo tarde, sobre las tres. En España almorzamos muy tarde, "
                             "¿sabes?",
         "nl": "Ik eet laat, rond drie uur. In Spanje eten we heel laat, weet je."},
        {"who": "Pau", "es": "Por la tarde tengo ensayo de castellers. Es una vez por semana, "
                             "siempre los sábados, de cinco a siete.",
         "nl": "'s Namiddags heb ik repetitie van de castellers. Dat is één keer per week, "
               "altijd op zaterdag, van vijf tot zeven."},
        {"who": "Pau", "es": "¿Castellers? Son las torres humanas de Cataluña. Yo estoy casi "
                             "arriba porque soy bajito.",
         "nl": "Castellers? Dat zijn de menselijke torens van Catalonië. Ik sta bijna bovenaan, "
               "want ik ben klein."},
        {"who": "Pau", "es": "Después vuelvo a casa, ceno a las nueve y media y juego un rato "
                             "con el ordenador.",
         "nl": "Daarna ga ik naar huis, eet ik om half tien en speel ik nog even op de computer."},
        {"who": "Pau", "es": "Me acuesto a las doce. ¡Los domingos duermo hasta tarde!",
         "nl": "Ik ga om twaalf uur slapen. Op zondag slaap ik uit!"},
        {"who": "Sam", "es": "¡Qué envidia! Yo el sábado me levanto a las diez y no hago nada.",
         "nl": "Wat jaloers! Ik sta op zaterdag om tien uur op en doe niets."},
        {"who": "Pau", "es": "Pues descansar también está bien. ¿Y a qué hora cenáis vosotros?",
         "nl": "Uitrusten is ook goed hoor. En hoe laat eten jullie 's avonds?"},
        {"who": "Sam", "es": "A las seis y media. ¡Muy temprano para ti!",
         "nl": "Om half zeven. Heel vroeg voor jou!"},
    ],
    "global": {
        "q": "¿De qué habla Pau?",
        "opts": ["De cómo es su sábado, hora por hora", "De sus vacaciones de verano",
                 "De un examen difícil"],
        "ans": "De cómo es su sábado, hora por hora",
        "why": "van het opstaan tot het slapengaan, met uren",
    },
    "detalle": [
        {"q": "¿A qué hora se despierta Pau el sábado?",
         "opts": ["A las nueve", "A las siete", "A las once"], "ans": "A las nueve",
         "why": "«El sábado me despierto a las nueve»"},
        {"q": "¿Qué hace Pau en la Sagrada Familia?",
         "opts": ["Enseña el barrio a los turistas", "Estudia en la biblioteca", "Juega al fútbol"],
         "ans": "Enseña el barrio a los turistas", "why": "«enseño el barrio a los turistas»"},
        {"q": "¿A qué hora almuerza?", "opts": ["Sobre las tres", "Sobre la una", "Sobre las cinco"],
         "ans": "Sobre las tres", "why": "«Almuerzo tarde, sobre las tres»"},
        {"q": "¿Cuántas veces por semana tiene ensayo de castellers?",
         "opts": ["Una", "Dos", "Tres"], "ans": "Una", "why": "«Es una vez por semana»"},
        {"q": "¿A qué hora se acuesta?", "opts": ["A las doce", "A las diez", "A las nueve y media"],
         "ans": "A las doce", "why": "«Me acuesto a las doce»"},
    ],
    "vf": [
        {"q": "Entre semana Pau se levanta a las siete.", "ans": True,
         "prueba": "entre semana me levanto a las siete"},
        {"q": "Pau está abajo del todo en la torre humana.", "ans": False,
         "prueba": "yo estoy casi arriba"},
        {"q": "Sam cena a las seis y media.", "ans": True, "prueba": "a las seis y media"},
    ],
    "produccion": {
        "prompt": "Contesta a Pau con un mensaje de voz: ¿cómo es tu sábado? A qué hora te "
                  "levantas, qué haces por la mañana y por la tarde, y a qué hora te acuestas. "
                  "Usa primero · después · normalmente.",
        "modo": "grabar",
        "modelo": "El sábado me levanto a las… Primero… Después… Por la tarde… Ceno a las… "
                  "y me acuesto a las…",
    },
}


# ---------------------------------------------------------------------------
# C6+ · U3 — tutorial hablado. De leestekst van deze unit weegt meningen over
# schermtijd; hier moet de leerling een reeks stappen volgen en onthouden in
# welke volgorde ze komen. Ander genre (instructie) en andere inhoud (een app
# instellen in plaats van erover discussiëren).
# ---------------------------------------------------------------------------
C6P_U3 = {
    "id": "C6P-U3-ESC-01",
    "ancla": "c6p-u3-esc-01",
    "titulo": "Cómo hacer una videollamada con la abuela",
    "audio": "audio/C6plus_U3.mp3",
    "situacion": {
        "lugar": "En la cocina, en Ciudad de México — con la tableta en la mesa",
        "quien": "Diego y su abuela Elvira, que no usa mucho la tecnología",
        "que": "Diego le explica paso a paso cómo llamar a la familia por vídeo",
        "claves": ["primero… luego…", "vas a ver", "acabas de…"],
    },
    "guion": [
        {"who": "Abuela", "es": "Diego, mi amor, yo con estas cosas no puedo. ¿Me enseñas?",
         "nl": "Diego, schat, met die dingen kan ik niet overweg. Leer je het me?"},
        {"who": "Diego", "es": "Claro, abuela. Es fácil. Primero enciende la tableta con este "
                               "botón de arriba.",
         "nl": "Natuurlijk, oma. Het is makkelijk. Zet eerst de tablet aan met deze knop bovenaan."},
        {"who": "Abuela", "es": "Ya está. Veo muchos cuadritos de colores.",
         "nl": "Klaar. Ik zie allemaal gekleurde vierkantjes."},
        {"who": "Diego", "es": "Esas son las aplicaciones. Luego toca la verde, la del teléfono "
                               "blanco.",
         "nl": "Dat zijn de apps. Raak daarna de groene aan, die met de witte telefoon."},
        {"who": "Abuela", "es": "¿Esta? Me pide una contraseña.",
         "nl": "Deze? Hij vraagt me een wachtwoord."},
        {"who": "Diego", "es": "No, esa es la wifi. La contraseña es la fecha de tu cumpleaños, "
                               "sin espacios.",
         "nl": "Nee, dat is de wifi. Het wachtwoord is je geboortedatum, zonder spaties."},
        {"who": "Abuela", "es": "Listo. Ahora veo la lista de la familia.",
         "nl": "Klaar. Nu zie ik de lijst van de familie."},
        {"who": "Diego", "es": "Perfecto. Busca a mi tía Rosa y toca el icono de la cámara, no "
                               "el del teléfono.",
         "nl": "Perfect. Zoek tante Rosa en raak het camera-icoontje aan, niet dat van de telefoon."},
        {"who": "Abuela", "es": "¿Y por qué la cámara?", "nl": "En waarom de camera?"},
        {"who": "Diego", "es": "Porque con la cámara vas a ver su cara. Con el teléfono solo la "
                               "vas a oír.",
         "nl": "Omdat je met de camera haar gezicht gaat zien. Met de telefoon ga je haar alleen horen."},
        {"who": "Abuela", "es": "¡Ay, ya suena! ¿Y si no contesta?",
         "nl": "Ah, hij gaat al over! En als ze niet opneemt?"},
        {"who": "Diego", "es": "Entonces cuelgas y le mandas un mensaje. Acabas de aprender lo "
                               "más difícil, abuela.",
         "nl": "Dan hang je op en stuur je haar een bericht. Je hebt net het moeilijkste geleerd, oma."},
        {"who": "Abuela", "es": "¡Rosa! ¡Te veo! Mañana voy a llamar yo sola.",
         "nl": "Rosa! Ik zie je! Morgen ga ik zelf bellen."},
    ],
    "global": {
        "q": "¿Qué hace Diego en este audio?",
        "opts": ["Le explica a su abuela cómo hacer una videollamada",
                 "Le vende una tableta nueva", "Le cuenta un viaje a México"],
        "ans": "Le explica a su abuela cómo hacer una videollamada",
        "why": "primero · luego · busca · toca = stappen",
    },
    "detalle": [
        {"q": "¿Qué hay que hacer primero?",
         "opts": ["Encender la tableta", "Tocar el icono verde", "Buscar a la tía Rosa"],
         "ans": "Encender la tableta", "why": "«Primero enciende la tableta»"},
        {"q": "¿De qué color es la aplicación?", "opts": ["Verde", "Azul", "Roja"], "ans": "Verde",
         "why": "«toca la verde, la del teléfono blanco»"},
        {"q": "¿Cuál es la contraseña de la wifi?",
         "opts": ["La fecha de su cumpleaños", "El nombre de su nieto", "Cuatro ceros"],
         "ans": "La fecha de su cumpleaños", "why": "«La contraseña es la fecha de tu cumpleaños»"},
        {"q": "¿A quién llama la abuela?", "opts": ["A la tía Rosa", "A Diego", "A la vecina"],
         "ans": "A la tía Rosa", "why": "«Busca a mi tía Rosa»"},
        {"q": "¿Qué hay que hacer si la otra persona no contesta?",
         "opts": ["Colgar y mandar un mensaje", "Llamar otra vez enseguida", "Apagar la tableta"],
         "ans": "Colgar y mandar un mensaje", "why": "«cuelgas y le mandas un mensaje»"},
    ],
    "vf": [
        {"q": "Hay que tocar el icono del teléfono para ver la cara.", "ans": False,
         "prueba": "toca el icono de la cámara, no el del teléfono"},
        {"q": "La abuela quiere llamar sola la próxima vez.", "ans": True,
         "prueba": "mañana voy a llamar yo sola"},
        {"q": "Diego dice que es fácil.", "ans": True, "prueba": "es fácil"},
    ],
    "produccion": {
        "prompt": "Ahora tú: explica en cuatro pasos cómo se hace algo con el móvil (subir una "
                  "foto, cambiar la contraseña, apagar las notificaciones). Usa primero · "
                  "luego · después · al final.",
        "modo": "grabar",
        "modelo": "Primero enciende… Luego toca… Después escribe… Al final vas a ver…",
    },
}


# ---------------------------------------------------------------------------
# C5 · U4 — encuesta callejera. Anders dan de entrevista van C6+ U1: daar volgt
# de leerling één verhaal, hier moet hij drie stemmen naast elkaar leggen en
# onthouden wie wát graag doet. De leestekst van deze unit is een festivalprogramma
# — daar kiest de leerling, hier vergelijkt hij.
# ---------------------------------------------------------------------------
C5_U4 = {
    "id": "C5-U4-ESC-01",
    "ancla": "c5-u4-esc-01",
    "titulo": "¿Qué haces en tu tiempo libre?",
    "audio": "audio/C5_U4.mp3",
    "situacion": {
        "lugar": "En la calle, delante del instituto de València",
        "quien": "Marta (radio del instituto) y tres personas: un chico, una señora y una chica",
        "que": "Les pregunta qué les gusta hacer en su tiempo libre",
        "claves": ["me gusta / me encanta", "a mí también / a mí tampoco", "los fines de semana"],
    },
    "guion": [
        {"who": "Marta", "es": "Buenos días. Somos la radio del instituto. ¿Qué haces tú en tu "
                               "tiempo libre?",
         "nl": "Goedemorgen. Wij zijn de schoolradio. Wat doe jij in je vrije tijd?"},
        {"who": "Chico", "es": "Yo juego al baloncesto tres veces por semana. Me encanta el deporte.",
         "nl": "Ik speel drie keer per week basket. Ik ben gek op sport."},
        {"who": "Marta", "es": "¿Y la música? ¿Te gusta?", "nl": "En muziek? Vind je dat leuk?"},
        {"who": "Chico", "es": "Sí, pero no toco ningún instrumento. Solo escucho.",
         "nl": "Ja, maar ik speel geen enkel instrument. Ik luister alleen."},
        {"who": "Marta", "es": "Gracias. Y usted, señora, ¿qué le gusta hacer?",
         "nl": "Bedankt. En u, mevrouw, wat doet u graag?"},
        {"who": "Señora", "es": "A mí me gusta mucho leer. Voy a la biblioteca los martes. "
                                "No me gustan nada los videojuegos.",
         "nl": "Ik lees heel graag. Ik ga op dinsdag naar de bibliotheek. Videospelletjes vind "
               "ik helemaal niets."},
        {"who": "Marta", "es": "A mí tampoco. ¿Y ve series?", "nl": "Ik ook niet. En kijkt u series?"},
        {"who": "Señora", "es": "Sí, veo una serie española por la noche. Es muy divertida.",
         "nl": "Ja, ik kijk 's avonds naar een Spaanse serie. Ze is heel grappig."},
        {"who": "Marta", "es": "Última pregunta, para ti: ¿qué haces los fines de semana?",
         "nl": "Laatste vraag, voor jou: wat doe jij in het weekend?"},
        {"who": "Chica", "es": "Los sábados quedo con mis amigas en la playa. Nadamos y bailamos.",
         "nl": "Op zaterdag spreek ik af met mijn vriendinnen op het strand. We zwemmen en dansen."},
        {"who": "Marta", "es": "¿Y no os aburrís?", "nl": "En vervelen jullie je niet?"},
        {"who": "Chica", "es": "¡Qué va! A mí me encanta el mar. Pero mi hermana prefiere el "
                               "cine: a ella no le gusta la playa.",
         "nl": "Welnee! Ik ben gek op de zee. Maar mijn zus gaat liever naar de film: zij houdt "
               "niet van het strand."},
        {"who": "Marta", "es": "¡Gracias a los tres! Y ahora, música.",
         "nl": "Bedankt alle drie! En nu: muziek."},
    ],
    "global": {
        "q": "¿Qué hace Marta en este audio?",
        "opts": ["Pregunta a tres personas qué les gusta hacer",
                 "Presenta un concierto en la playa", "Explica un examen de música"],
        "ans": "Pregunta a tres personas qué les gusta hacer",
        "why": "drie keer dezelfde vraag, drie verschillende antwoorden",
    },
    "detalle": [
        {"q": "¿Cuántas veces por semana juega al baloncesto el chico?",
         "opts": ["Tres", "Dos", "Cinco"], "ans": "Tres", "why": "«tres veces por semana»"},
        {"q": "¿Toca el chico algún instrumento?",
         "opts": ["No, solo escucha", "Sí, la guitarra", "Sí, el piano"], "ans": "No, solo escucha",
         "why": "«no toco ningún instrumento. Solo escucho»"},
        {"q": "¿Qué día va la señora a la biblioteca?",
         "opts": ["Los martes", "Los lunes", "Los sábados"], "ans": "Los martes",
         "why": "«Voy a la biblioteca los martes»"},
        {"q": "¿Qué no le gusta nada a la señora?",
         "opts": ["Los videojuegos", "Las series", "Leer"], "ans": "Los videojuegos",
         "why": "«No me gustan nada los videojuegos»"},
        {"q": "¿Qué prefiere la hermana de la chica?",
         "opts": ["El cine", "La playa", "El baloncesto"], "ans": "El cine",
         "why": "«mi hermana prefiere el cine»"},
    ],
    "vf": [
        {"q": "A Marta tampoco le gustan los videojuegos.", "ans": True, "prueba": "a mí tampoco"},
        {"q": "La chica queda con sus amigas los domingos.", "ans": False,
         "prueba": "los sábados quedo con mis amigas"},
        {"q": "A la hermana de la chica le gusta la playa.", "ans": False,
         "prueba": "a ella no le gusta la playa"},
    ],
    "produccion": {
        "prompt": "Contesta tú a la radio del instituto en cuatro frases: qué te gusta hacer, "
                  "qué te encanta, qué no te gusta nada y con quién quedas los fines de semana.",
        "modo": "grabar",
        "modelo": "En mi tiempo libre… Me encanta… No me gusta nada… Los fines de semana quedo "
                  "con… y…",
    },
}


# ---------------------------------------------------------------------------
# C6+ · U4 — trámite en la recepción. De leestekst van deze unit is een postkaart
# vol «he visto, he comido»; hier moet de leerling een échte transactie volgen:
# een reservering die niet klopt. Cijfers, dagen en een probleem dat opgelost
# wordt — heel andere luistertaak dan een verhaal.
# ---------------------------------------------------------------------------
C6P_U4 = {
    "id": "C6P-U4-ESC-01",
    "ancla": "c6p-u4-esc-01",
    "titulo": "En la recepción del hostal",
    "audio": "audio/C6plus_U4.mp3",
    "situacion": {
        "lugar": "La recepción de un hostal en Valparaíso, a las once de la noche",
        "quien": "Un recepcionista y Nina, que llega con su reserva",
        "que": "La reserva no coincide y hay que arreglarlo",
        "claves": ["tengo una reserva", "a nombre de…", "¿por cuántas noches?"],
    },
    "guion": [
        {"who": "Recepcionista", "es": "Buenas noches. ¿En qué puedo ayudarla?",
         "nl": "Goedenavond. Waarmee kan ik u helpen?"},
        {"who": "Nina", "es": "Buenas noches. Tengo una reserva a nombre de Nina Quispe.",
         "nl": "Goedenavond. Ik heb een reservering op naam van Nina Quispe."},
        {"who": "Recepcionista", "es": "A ver… Quispe, sí. Una habitación doble para dos noches.",
         "nl": "Even kijken… Quispe, ja. Een tweepersoonskamer voor twee nachten."},
        {"who": "Nina", "es": "No, perdone. He reservado una individual para tres noches.",
         "nl": "Nee, sorry. Ik heb een eenpersoonskamer voor drie nachten geboekt."},
        {"who": "Recepcionista", "es": "Un momento… Tiene razón, hay dos reservas con el mismo "
                                       "apellido. La suya es la 204.",
         "nl": "Een momentje… U hebt gelijk, er staan twee reserveringen met dezelfde "
               "achternaam. De uwe is 204."},
        {"who": "Nina", "es": "Menos mal. ¿Y el desayuno está incluido?",
         "nl": "Gelukkig. En is het ontbijt inbegrepen?"},
        {"who": "Recepcionista", "es": "Sí, de siete a diez, en el patio. Y hay wifi gratis en "
                                       "todo el hostal.",
         "nl": "Ja, van zeven tot tien, op het binnenplein. En er is gratis wifi in het hele hostel."},
        {"who": "Nina", "es": "Perfecto. Una cosa más: mañana salgo muy temprano para el sur. "
                              "¿Puedo dejar la maleta aquí?",
         "nl": "Perfect. Nog iets: morgen vertrek ik heel vroeg naar het zuiden. Mag ik mijn "
               "koffer hier laten?"},
        {"who": "Recepcionista", "es": "Claro. Detrás de la recepción, sin problema. ¿Ya ha "
                                       "cenado?",
         "nl": "Natuurlijk. Achter de receptie, geen probleem. Hebt u al gegeten?"},
        {"who": "Nina", "es": "No, todavía no. ¿Hay algo abierto a esta hora?",
         "nl": "Nee, nog niet. Is er iets open op dit uur?"},
        {"who": "Recepcionista", "es": "La cocina del hostal está cerrada, pero hay una picada "
                                       "en la esquina. Está abierta hasta la una.",
         "nl": "De keuken van het hostel is gesloten, maar er is een eethuisje op de hoek. "
               "Dat is open tot één uur."},
        {"who": "Nina", "es": "Gracias por todo. Aquí tiene mi pasaporte.",
         "nl": "Bedankt voor alles. Hier is mijn paspoort."},
        {"who": "Recepcionista", "es": "Gracias a usted. Aquí tiene la llave. Que descanse.",
         "nl": "Ik dank u. Hier is uw sleutel. Slaap wel."},
    ],
    "global": {
        "q": "¿Qué pasa en la recepción?",
        "opts": ["La reserva no coincide y el recepcionista lo arregla",
                 "Nina quiere cambiar de hostal", "Nina paga la cuenta y se va"],
        "ans": "La reserva no coincide y el recepcionista lo arregla",
        "why": "twee reserveringen met dezelfde naam",
    },
    "detalle": [
        {"q": "¿Qué habitación ha reservado Nina?",
         "opts": ["Una individual para tres noches", "Una doble para dos noches",
                  "Una doble para tres noches"], "ans": "Una individual para tres noches",
         "why": "«He reservado una individual para tres noches»"},
        {"q": "¿Cuál es el número de su habitación?", "opts": ["204", "240", "104"], "ans": "204",
         "why": "«La suya es la 204»"},
        {"q": "¿A qué hora es el desayuno?", "opts": ["De siete a diez", "De ocho a once",
                                                       "De seis a nueve"], "ans": "De siete a diez",
         "why": "«de siete a diez, en el patio»"},
        {"q": "¿Dónde puede dejar la maleta?",
         "opts": ["Detrás de la recepción", "En la habitación", "En el patio"],
         "ans": "Detrás de la recepción", "why": "«Detrás de la recepción, sin problema»"},
        {"q": "¿Hasta qué hora está abierta la picada de la esquina?",
         "opts": ["Hasta la una", "Hasta las once", "Hasta las doce"], "ans": "Hasta la una",
         "why": "«Está abierta hasta la una»"},
    ],
    "vf": [
        {"q": "La wifi del hostal cuesta dinero.", "ans": False, "prueba": "hay wifi gratis"},
        {"q": "Nina ya ha cenado.", "ans": False, "prueba": "no, todavía no"},
        {"q": "Hay dos reservas con el mismo apellido.", "ans": True,
         "prueba": "hay dos reservas con el mismo apellido"},
    ],
    "produccion": {
        "prompt": "Ahora tú llegas al hostal. Graba el diálogo (cuatro turnos): saluda, di a "
                  "nombre de quién está la reserva, cuántas noches y qué tipo de habitación, y "
                  "pregunta una cosa práctica (desayuno, wifi, maleta).",
        "modo": "grabar",
        "modelo": "Buenas noches. Tengo una reserva a nombre de… He reservado una… para … "
                  "noches. ¿Está incluido…? ¿Puedo…?",
    },
}


# ---------------------------------------------------------------------------
# C5 · U5 — en el restaurante. De leestekst van deze unit geeft cijfers over een
# markt; hier moet de leerling een bestelling volgen en er een probleem in horen
# (het gerecht is uitverkocht). Andere plaats, andere taalhandeling: daar lezen
# om te weten, hier luisteren om te bestellen.
# ---------------------------------------------------------------------------
C5_U5 = {
    "id": "C5-U5-ESC-01",
    "ancla": "c5-u5-esc-01",
    "titulo": "Una mesa para tres",
    "audio": "audio/C5_U5.mp3",
    "situacion": {
        "lugar": "Un restaurante pequeño en el centro de Ciudad de México, a las dos",
        "quien": "Un camarero, Diego y dos amigos",
        "que": "Piden la comida, pero un plato ya no queda",
        "claves": ["¿qué va a tomar?", "para mí…", "¿me trae…?"],
    },
    "guion": [
        {"who": "Camarero", "es": "Buenas tardes. ¿Una mesa para tres?",
         "nl": "Goedemiddag. Een tafel voor drie?"},
        {"who": "Diego", "es": "Sí, por favor. ¿Nos trae la carta?",
         "nl": "Ja, graag. Brengt u ons de kaart?"},
        {"who": "Camarero", "es": "Aquí tienen. Hoy el menú del día cuesta ciento veinte pesos: "
                                  "sopa, plato fuerte y postre.",
         "nl": "Alstublieft. Vandaag kost het dagmenu honderdtwintig peso: soep, hoofdgerecht "
               "en dessert."},
        {"who": "Diego", "es": "Perfecto. Para mí, la sopa de tortilla y los tacos de pollo.",
         "nl": "Perfect. Voor mij de tortillasoep en de kiptaco's."},
        {"who": "Camarero", "es": "Lo siento, de tacos de pollo ya no quedan. ¿De carne o de "
                                  "pescado?",
         "nl": "Het spijt me, kiptaco's zijn er niet meer. Met vlees of met vis?"},
        {"who": "Diego", "es": "De pescado, entonces. ¿Pican mucho?",
         "nl": "Dan met vis. Zijn ze erg pikant?"},
        {"who": "Camarero", "es": "Un poco. La salsa verde pica bastante; la roja casi nada.",
         "nl": "Een beetje. De groene saus is redelijk pikant, de rode bijna niet."},
        {"who": "Diego", "es": "Vale, con salsa roja. Y de postre, flan.",
         "nl": "Oké, met rode saus. En als dessert, flan."},
        {"who": "Camarero", "es": "¿Y para beber?", "nl": "En om te drinken?"},
        {"who": "Diego", "es": "Un agua de horchata y dos refrescos, por favor.",
         "nl": "Een horchata en twee frisdranken, alstublieft."},
        {"who": "Camarero", "es": "Muy bien. Ahora se los traigo. ¡Que aproveche!",
         "nl": "Heel goed. Ik breng ze zo. Smakelijk!"},
        {"who": "Diego", "es": "Gracias. Ah, ¿nos trae también la cuenta con el postre? "
                               "Tenemos prisa.",
         "nl": "Bedankt. Ah, brengt u ook de rekening bij het dessert? We hebben haast."},
        {"who": "Camarero", "es": "Claro que sí. ¿Todo junto o por separado?",
         "nl": "Zeker. Alles samen of apart?"},
    ],
    "global": {
        "q": "¿Qué pasa en el restaurante?",
        "opts": ["Piden la comida y un plato ya no queda", "Reservan una mesa por teléfono",
                 "Se quejan de la comida"],
        "ans": "Piden la comida y un plato ya no queda",
        "why": "«de tacos de pollo ya no quedan»",
    },
    "detalle": [
        {"q": "¿Cuánto cuesta el menú del día?", "opts": ["120 pesos", "112 pesos", "150 pesos"],
         "ans": "120 pesos", "why": "«cuesta ciento veinte pesos»"},
        {"q": "¿Qué plato ya no queda?", "opts": ["Los tacos de pollo", "La sopa de tortilla",
                                                   "El flan"], "ans": "Los tacos de pollo",
         "why": "«de tacos de pollo ya no quedan»"},
        {"q": "¿Qué salsa pide Diego?", "opts": ["La roja", "La verde", "Las dos"], "ans": "La roja",
         "why": "«Vale, con salsa roja»"},
        {"q": "¿Qué beben?", "opts": ["Una horchata y dos refrescos", "Tres aguas", "Dos cafés"],
         "ans": "Una horchata y dos refrescos", "why": "«Un agua de horchata y dos refrescos»"},
        {"q": "¿Por qué piden la cuenta con el postre?",
         "opts": ["Porque tienen prisa", "Porque no les gusta el sitio", "Porque no hay postre"],
         "ans": "Porque tienen prisa", "why": "«Tenemos prisa»"},
    ],
    "vf": [
        {"q": "La salsa verde pica más que la roja.", "ans": True,
         "prueba": "la salsa verde pica bastante; la roja casi nada"},
        {"q": "El menú del día no incluye postre.", "ans": False,
         "prueba": "sopa, plato fuerte y postre"},
        {"q": "Son tres personas.", "ans": True, "prueba": "una mesa para tres"},
    ],
    "produccion": {
        "prompt": "Ahora pides tú. Graba cuatro turnos: pide la carta, pide un primer plato y "
                  "un segundo, pregunta si pica, y pide la cuenta. Usa: para mí… · ¿me trae…? · "
                  "¿me pone…?",
        "modo": "grabar",
        "modelo": "Buenas tardes, ¿nos trae la carta? Para mí… y de segundo… ¿Pica mucho? "
                  "¿Nos trae la cuenta, por favor?",
    },
}


# ---------------------------------------------------------------------------
# C6+ · U5 — visita guiada. De leestekst van deze unit is een leyenda: fictie,
# met een moraal. Hier hoort de leerling ware geschiedenis met jaartallen en
# moet hij die aan elkaar knopen — hetzelfde indefinido, een heel ander soort
# vertellen. Ander genre: een gids die vragen krijgt uit de groep.
# ---------------------------------------------------------------------------
C6P_U5 = {
    "id": "C6P-U5-ESC-01",
    "ancla": "c6p-u5-esc-01",
    "titulo": "Los que llegaron en barco",
    "audio": "audio/C6plus_U5.mp3",
    "situacion": {
        "lugar": "Museo de la Inmigración, Buenos Aires — sala 2",
        "quien": "Una guía y dos alumnos de intercambio",
        "que": "La guía cuenta cómo llegaron los inmigrantes y de dónde salió el tango",
        "claves": ["llegaron en barco", "entre 1880 y 1930", "por eso"],
    },
    "guion": [
        {"who": "Guía", "es": "Bienvenidos a la sala dos. Aquí estamos en el antiguo Hotel de "
                              "Inmigrantes.",
         "nl": "Welkom in zaal twee. We staan hier in het vroegere Immigrantenhotel."},
        {"who": "Guía", "es": "Entre mil ochocientos ochenta y mil novecientos treinta llegaron "
                              "a Argentina millones de personas. La mayoría vino de Italia y de "
                              "España.",
         "nl": "Tussen 1880 en 1930 kwamen er miljoenen mensen naar Argentinië. De meesten "
               "kwamen uit Italië en Spanje."},
        {"who": "Alumno", "es": "¿Y dónde durmieron al llegar?",
         "nl": "En waar sliepen ze als ze aankwamen?"},
        {"who": "Guía", "es": "Aquí mismo. El Estado les dio cama y comida durante cinco días. "
                              "Después buscaron trabajo y se mudaron a los conventillos.",
         "nl": "Hier ter plaatse. De staat gaf hun vijf dagen lang bed en eten. Daarna zochten "
               "ze werk en verhuisden ze naar de conventillos."},
        {"who": "Alumna", "es": "¿Qué es un conventillo?", "nl": "Wat is een conventillo?"},
        {"who": "Guía", "es": "Una casa grande con muchas familias. Cada familia tuvo una sola "
                              "habitación, y todos compartieron el patio y la cocina.",
         "nl": "Een groot huis met veel gezinnen. Elk gezin had één enkele kamer, en iedereen "
               "deelde de binnenplaats en de keuken."},
        {"who": "Guía", "es": "En ese patio nació buena parte del tango. Los vecinos "
                              "escucharon la música de los otros y la mezclaron con la suya.",
         "nl": "Op die binnenplaats is een groot deel van de tango ontstaan. De buren hoorden "
               "elkaars muziek en mengden die met de hunne."},
        {"who": "Alumno", "es": "¿Y el idioma? ¿No fue un problema?",
         "nl": "En de taal? Was dat geen probleem?"},
        {"who": "Guía", "es": "Fue un problema y una oportunidad. De esa mezcla salió el "
                              "lunfardo. «Laburo», por ejemplo, es trabajo, y viene del italiano.",
         "nl": "Het was een probleem én een kans. Uit die mengeling ontstond het lunfardo. "
               "«Laburo» bijvoorbeeld betekent werk en komt uit het Italiaans."},
        {"who": "Alumna", "es": "¿Y «pibe»?", "nl": "En «pibe»?"},
        {"who": "Guía", "es": "Chico, muchacho. Todavía se usa todos los días en Buenos Aires.",
         "nl": "Jongen, gast. Dat wordt nog elke dag gebruikt in Buenos Aires."},
        {"who": "Guía", "es": "Por eso decimos que este museo no habla del pasado, sino de la "
                              "ciudad de hoy. Pasamos a la sala tres.",
         "nl": "Daarom zeggen we dat dit museum niet over het verleden gaat, maar over de stad "
               "van vandaag. We gaan door naar zaal drie."},
    ],
    "global": {
        "q": "¿De qué habla la guía?",
        "opts": ["De cómo llegaron los inmigrantes y qué dejaron en la ciudad",
                 "De cómo se construyó el puerto", "De un cantante de tango famoso"],
        "ans": "De cómo llegaron los inmigrantes y qué dejaron en la ciudad",
        "why": "aankomst → conventillo → tango → lunfardo",
    },
    "detalle": [
        {"q": "¿Entre qué años llegaron millones de personas?",
         "opts": ["Entre 1880 y 1930", "Entre 1780 y 1830", "Entre 1930 y 1980"],
         "ans": "Entre 1880 y 1930", "why": "«Entre mil ochocientos ochenta y mil novecientos treinta»"},
        {"q": "¿De qué dos países vino la mayoría?",
         "opts": ["De Italia y de España", "De Francia y de Portugal", "De Alemania y de Polonia"],
         "ans": "De Italia y de España", "why": "«vino de Italia y de España»"},
        {"q": "¿Cuántos días les dio el Estado cama y comida?",
         "opts": ["Cinco", "Quince", "Cincuenta"], "ans": "Cinco",
         "why": "«durante cinco días»"},
        {"q": "¿Qué compartieron las familias del conventillo?",
         "opts": ["El patio y la cocina", "La habitación", "El trabajo"],
         "ans": "El patio y la cocina", "why": "«todos compartieron el patio y la cocina»"},
        {"q": "¿Qué significa «laburo»?", "opts": ["Trabajo", "Chico", "Casa"], "ans": "Trabajo",
         "why": "«Laburo», por ejemplo, es trabajo"},
    ],
    "vf": [
        {"q": "Cada familia tuvo su propia cocina.", "ans": False,
         "prueba": "todos compartieron el patio y la cocina"},
        {"q": "El lunfardo nació de la mezcla de idiomas.", "ans": True,
         "prueba": "de esa mezcla salió el lunfardo"},
        {"q": "La palabra «pibe» ya no se usa.", "ans": False,
         "prueba": "todavía se usa todos los días"},
    ],
    "produccion": {
        "prompt": "Sé tú la guía de una sala sobre tu propia ciudad o familia. Graba cinco "
                  "frases en indefinido: quién llegó, cuándo, de dónde, dónde vivió y qué dejó "
                  "(una comida, una palabra, una costumbre).",
        "modo": "grabar",
        "modelo": "Mi… llegó en… Vino de… Vivió en… Trabajó de… Por eso, hoy en mi casa…",
    },
}


# ---------------------------------------------------------------------------
# C5 · U6 — en el probador. De leestekst van deze unit geeft tips om te wégen;
# hier hoort de leerling twee vriendinnen die van mening verschíllen over wat
# staat en wat niet. Geen transactie zoals in U5 (bestellen), maar meningen,
# maten en een beslissing.
# ---------------------------------------------------------------------------
C5_U6 = {
    "id": "C5-U6-ESC-01",
    "ancla": "c5-u6-esc-01",
    "titulo": "En el probador",
    "audio": "audio/C5_U6.mp3",
    "situacion": {
        "lugar": "Una tienda de ropa en el centro, primer día de rebajas",
        "quien": "Nina y Valen, y la dependienta",
        "que": "Nina se prueba ropa y Valen le da su opinión",
        "claves": ["¿me queda bien?", "esta / esa", "¿tienes una talla más?"],
    },
    "guion": [
        {"who": "Nina", "es": "Valen, ¿me queda bien esta chaqueta verde?",
         "nl": "Valen, staat dit groene jasje me goed?"},
        {"who": "Valen", "es": "El color sí, pero te queda un poco ancha. ¿No hay una talla menos?",
         "nl": "De kleur wel, maar hij zit een beetje wijd. Is er geen kleinere maat?"},
        {"who": "Nina", "es": "Es la treinta y ocho. Voy a probarme la treinta y seis.",
         "nl": "Dit is maat 38. Ik ga de 36 passen."},
        {"who": "Dependienta", "es": "De la treinta y seis solo queda en negro y en rosa.",
         "nl": "In maat 36 hebben we alleen nog zwart en roze."},
        {"who": "Nina", "es": "En negro, entonces. ¿Y esos pantalones de rayas de ahí?",
         "nl": "Dan zwart. En die gestreepte broek daar bij jou?"},
        {"who": "Valen", "es": "¿Estos? Acabo de verlos. Cuestan veinticinco euros con el "
                               "descuento.",
         "nl": "Deze? Ik heb ze net gezien. Ze kosten vijfentwintig euro met de korting."},
        {"who": "Nina", "es": "No están mal. Pero aquella falda del escaparate me gusta más.",
         "nl": "Niet slecht. Maar dat rokje in de etalage vind ik mooier."},
        {"who": "Valen", "es": "Esa es carísima y no está rebajada. Yo me llevo los pantalones.",
         "nl": "Dat is peperduur en niet afgeprijsd. Ik neem de broek."},
        {"who": "Nina", "es": "Vale. La chaqueta negra y los pantalones. ¿Cuánto es todo?",
         "nl": "Oké. Het zwarte jasje en de broek. Hoeveel is dat samen?"},
        {"who": "Dependienta", "es": "Cuarenta y siete euros. ¿En efectivo o con tarjeta?",
         "nl": "Zevenenveertig euro. Cash of met de kaart?"},
        {"who": "Nina", "es": "En efectivo. Es un truco: así veo lo que gasto.",
         "nl": "Cash. Dat is een truc: zo zie ik wat ik uitgeef."},
        {"who": "Valen", "es": "¡Y a ti todavía te queda dinero para un helado!",
         "nl": "En jij houdt nog genoeg over voor een ijsje!"},
    ],
    "global": {
        "q": "¿Qué hacen Nina y Valen?",
        "opts": ["Nina se prueba ropa y Valen le aconseja", "Devuelven una chaqueta rota",
                 "Buscan trabajo en la tienda"],
        "ans": "Nina se prueba ropa y Valen le aconseja",
        "why": "«¿me queda bien?» → opinie → beslissing",
    },
    "detalle": [
        {"q": "¿Qué problema tiene la chaqueta verde?",
         "opts": ["Le queda ancha", "Le queda corta", "El color no le gusta"],
         "ans": "Le queda ancha", "why": "«te queda un poco ancha»"},
        {"q": "¿En qué colores queda la talla treinta y seis?",
         "opts": ["En negro y en rosa", "En verde y en negro", "Solo en verde"],
         "ans": "En negro y en rosa", "why": "«solo queda en negro y en rosa»"},
        {"q": "¿Cuánto cuestan los pantalones con el descuento?",
         "opts": ["25 euros", "35 euros", "47 euros"], "ans": "25 euros",
         "why": "«Cuestan veinticinco euros con el descuento»"},
        {"q": "¿Cuánto paga Nina en total?", "opts": ["47 euros", "25 euros", "38 euros"],
         "ans": "47 euros", "why": "«Cuarenta y siete euros»"},
        {"q": "¿Cómo paga?", "opts": ["En efectivo", "Con tarjeta", "No paga"], "ans": "En efectivo",
         "why": "«En efectivo. Es un truco»"},
    ],
    "vf": [
        {"q": "Nina se lleva la chaqueta verde.", "ans": False, "prueba": "la chaqueta negra y los pantalones"},
        {"q": "La falda del escaparate está rebajada.", "ans": False, "prueba": "no está rebajada"},
        {"q": "Valen le aconseja los pantalones.", "ans": True, "prueba": "yo me llevo los pantalones"},
    ],
    "produccion": {
        "prompt": "Estás en el probador con un amigo. Graba cuatro turnos: pregunta si te queda "
                  "bien, pide otra talla o otro color, compara dos prendas (esta / esa / "
                  "aquella) y decide qué te llevas.",
        "modo": "grabar",
        "modelo": "¿Me queda bien esta…? ¿Tienes una talla…? Prefiero esa… que aquella… "
                  "Me llevo…",
    },
}


# ---------------------------------------------------------------------------
# C6+ · U6 — pódcast escolar. De leestekst van deze unit is een brief van één
# oma over hoe het vroeger wás; hier vergelijken twee jongeren hun eigen
# kindertijd met elkaar — dezelfde tijd, maar nu als discussie tussen
# leeftijdsgenoten, mét comparativos. Nieuw genre.
# ---------------------------------------------------------------------------
C6P_U6 = {
    "id": "C6P-U6-ESC-01",
    "ancla": "c6p-u6-esc-01",
    "titulo": "Pódcast «Antes y ahora»",
    "audio": "audio/C6plus_U6.mp3",
    "situacion": {
        "lugar": "El estudio del pódcast del instituto, episodio 7",
        "quien": "Mateo (presentador) y dos invitados: Sofía y Aarón",
        "que": "Comparan cómo era su infancia con la de ahora",
        "claves": ["cuando era pequeño", "antes… ahora…", "más … que"],
    },
    "guion": [
        {"who": "Mateo", "es": "Bienvenidos al episodio siete. Hoy hablamos de la infancia. "
                               "Sofía, ¿cómo era la tuya?",
         "nl": "Welkom bij aflevering zeven. Vandaag hebben we het over de kindertijd. Sofía, "
               "hoe was die van jou?"},
        {"who": "Sofía", "es": "Yo crecí en un pueblo pequeño. No teníamos parque, pero "
                               "jugábamos en la calle hasta las nueve.",
         "nl": "Ik groeide op in een klein dorp. We hadden geen park, maar we speelden op "
               "straat tot negen uur."},
        {"who": "Mateo", "es": "¿Y tú, Aarón?", "nl": "En jij, Aarón?"},
        {"who": "Aarón", "es": "Yo vivía en la ciudad. Tenía más juguetes que Sofía, seguro, "
                               "pero salía mucho menos.",
         "nl": "Ik woonde in de stad. Ik had zeker meer speelgoed dan Sofía, maar ik ging veel "
               "minder buiten."},
        {"who": "Sofía", "es": "Eso es. Yo no tenía consola, y me daba igual.",
         "nl": "Precies. Ik had geen spelconsole, en dat kon me niet schelen."},
        {"who": "Mateo", "es": "¿Recordáis algún día concreto?",
         "nl": "Herinneren jullie je een bepaalde dag?"},
        {"who": "Aarón", "es": "Sí. Un día, con siete años, me perdí en el metro. Mi madre me "
                               "encontró dos horas después. Nunca lo olvidé.",
         "nl": "Ja. Op een dag, toen ik zeven was, verdwaalde ik in de metro. Mijn moeder vond "
               "me twee uur later. Ik ben het nooit vergeten."},
        {"who": "Sofía", "es": "El mío es más tonto: el día que llegó internet al pueblo. "
                               "Toda la escuela fue a ver la pantalla.",
         "nl": "Het mijne is dommer: de dag dat het internet in het dorp kwam. De hele school "
               "ging naar het scherm kijken."},
        {"who": "Mateo", "es": "Última pregunta: ¿se vivía mejor antes?",
         "nl": "Laatste vraag: leefde men vroeger beter?"},
        {"who": "Aarón", "es": "No. Se vivía distinto. Ahora tenemos más cosas y menos tiempo.",
         "nl": "Nee. Men leefde anders. Nu hebben we meer spullen en minder tijd."},
        {"who": "Sofía", "es": "Yo echo de menos el aburrimiento. Cuando te aburrías, "
                               "inventabas algo.",
         "nl": "Ik mis de verveling. Als je je verveelde, verzon je iets."},
        {"who": "Mateo", "es": "Buena frase para terminar. ¡Hasta el próximo episodio!",
         "nl": "Mooie zin om mee af te sluiten. Tot de volgende aflevering!"},
    ],
    "global": {
        "q": "¿De qué trata el episodio?",
        "opts": ["De comparar la infancia de antes con la de ahora",
                 "De cómo se hace un pódcast", "De un viaje escolar"],
        "ans": "De comparar la infancia de antes con la de ahora",
        "why": "twee gasten, twee kindertijden, telkens vergeleken",
    },
    "detalle": [
        {"q": "¿Dónde creció Sofía?", "opts": ["En un pueblo pequeño", "En la ciudad",
                                                "En el extranjero"], "ans": "En un pueblo pequeño",
         "why": "«Yo crecí en un pueblo pequeño»"},
        {"q": "¿Hasta qué hora jugaba Sofía en la calle?",
         "opts": ["Hasta las nueve", "Hasta las siete", "Hasta las once"], "ans": "Hasta las nueve",
         "why": "«jugábamos en la calle hasta las nueve»"},
        {"q": "¿Qué tenía Aarón más que Sofía?", "opts": ["Juguetes", "Amigos", "Tiempo libre"],
         "ans": "Juguetes", "why": "«Tenía más juguetes que Sofía»"},
        {"q": "¿Qué le pasó a Aarón a los siete años?",
         "opts": ["Se perdió en el metro", "Se rompió una pierna", "Se mudó de ciudad"],
         "ans": "Se perdió en el metro", "why": "«con siete años, me perdí en el metro»"},
        {"q": "¿Cuál es el recuerdo de Sofía?",
         "opts": ["El día que llegó internet al pueblo", "Su primer día de escuela",
                  "Un viaje a Cusco"], "ans": "El día que llegó internet al pueblo",
         "why": "«el día que llegó internet al pueblo»"},
    ],
    "vf": [
        {"q": "Sofía tenía una consola de pequeña.", "ans": False, "prueba": "yo no tenía consola"},
        {"q": "Aarón salía más que Sofía.", "ans": False, "prueba": "salía mucho menos"},
        {"q": "Según Aarón, ahora tenemos menos tiempo.", "ans": True,
         "prueba": "ahora tenemos más cosas y menos tiempo"},
    ],
    "produccion": {
        "prompt": "Eres el tercer invitado del pódcast. Graba cinco frases: cómo era tu "
                  "infancia (imperfecto), un día concreto que recuerdas (indefinido) y una "
                  "comparación antes/ahora (más… que · menos… que · tan… como).",
        "modo": "grabar",
        "modelo": "Cuando era pequeño/-a, yo… y siempre… Un día… Ahora tengo más… que antes, "
                  "pero menos…",
    },
}


# ---------------------------------------------------------------------------
# C5 · U7 — la visita a un piso. De leestekst van deze unit is een advertentie:
# daar staat alles wat er wél is. Hier moet de leerling juist horen wat er
# ontbreekt en wat er niet werkt — luisteren naar het gat in de belofte. Bewust
# géén routebeschrijving: die staat al in C6+ U2 en zou hier hetzelfde vragen.
# ---------------------------------------------------------------------------
C5_U7 = {
    "id": "C5-U7-ESC-01",
    "ancla": "c5-u7-esc-01",
    "titulo": "La visita al piso",
    "audio": "audio/C5_U7.mp3",
    "situacion": {
        "lugar": "Un piso vacío en Cartagena, un sábado por la mañana",
        "quien": "Una agente inmobiliaria, Sam y su madre",
        "que": "Visitan el piso y descubren que no todo es como en el anuncio",
        "claves": ["¿qué hay en…?", "está / están", "no hay"],
    },
    "guion": [
        {"who": "Agente", "es": "Pasen, pasen. Este es el salón. Como ven, es muy luminoso.",
         "nl": "Komt u binnen. Dit is de woonkamer. Zoals u ziet, is ze heel licht."},
        {"who": "Madre", "es": "Sí, la ventana es grande. ¿Y qué hay detrás de esa puerta?",
         "nl": "Ja, het raam is groot. En wat is er achter die deur?"},
        {"who": "Agente", "es": "La cocina. Es pequeña, pero tiene de todo: nevera, horno y "
                                "lavadora.",
         "nl": "De keuken. Ze is klein, maar er is alles: koelkast, oven en wasmachine."},
        {"who": "Sam", "es": "Perdone, aquí no hay lavadora. Está el hueco, pero está vacío.",
         "nl": "Sorry, hier is geen wasmachine. De ruimte is er, maar hij is leeg."},
        {"who": "Agente", "es": "Ah, tiene razón. La lavadora llega la semana que viene.",
         "nl": "Ah, u hebt gelijk. De wasmachine komt volgende week."},
        {"who": "Madre", "es": "¿Y los dormitorios?", "nl": "En de slaapkamers?"},
        {"who": "Agente", "es": "Al final del pasillo. El grande está a la derecha; el pequeño, "
                                "enfrente.",
         "nl": "Aan het einde van de gang. De grote is rechts, de kleine ertegenover."},
        {"who": "Sam", "es": "En el pequeño no hay armario.", "nl": "In de kleine is geen kast."},
        {"who": "Agente", "es": "No, pero debajo de la cama hay dos cajones muy grandes.",
         "nl": "Nee, maar onder het bed zitten twee heel grote laden."},
        {"who": "Madre", "es": "¿Y el ruido? El anuncio dice «zona tranquila».",
         "nl": "En het lawaai? De advertentie zegt «rustige buurt»."},
        {"who": "Agente", "es": "De día sí. Los viernes y los sábados hay música en la plaza "
                                "hasta las dos.",
         "nl": "Overdag wel. Op vrijdag en zaterdag is er muziek op het plein tot twee uur."},
        {"who": "Sam", "es": "A mí eso me gusta. Mamá, ¿qué opinas?",
         "nl": "Mij bevalt dat wel. Mama, wat vind jij?"},
        {"who": "Madre", "es": "Que el piso está bien, pero primero quiero ver la lavadora.",
         "nl": "Dat het appartement goed is, maar dat ik eerst de wasmachine wil zien."},
    ],
    "global": {
        "q": "¿Qué pasa durante la visita?",
        "opts": ["Descubren que faltan cosas del anuncio", "Firman el contrato",
                 "La agente les enseña el barrio"],
        "ans": "Descubren que faltan cosas del anuncio",
        "why": "geen wasmachine, geen kast, wel lawaai",
    },
    "detalle": [
        {"q": "¿Qué falta en la cocina?", "opts": ["La lavadora", "La nevera", "El horno"],
         "ans": "La lavadora", "why": "«aquí no hay lavadora»"},
        {"q": "¿Cuándo llega la lavadora?", "opts": ["La semana que viene", "Hoy mismo",
                                                      "El mes que viene"],
         "ans": "La semana que viene", "why": "«La lavadora llega la semana que viene»"},
        {"q": "¿Dónde está el dormitorio grande?", "opts": ["A la derecha", "A la izquierda",
                                                             "Al lado del salón"],
         "ans": "A la derecha", "why": "«El grande está a la derecha»"},
        {"q": "¿Qué hay debajo de la cama del dormitorio pequeño?",
         "opts": ["Dos cajones grandes", "Un armario", "Una alfombra"],
         "ans": "Dos cajones grandes", "why": "«debajo de la cama hay dos cajones muy grandes»"},
        {"q": "¿Qué días hay música en la plaza?",
         "opts": ["Los viernes y los sábados", "Todos los días", "Los domingos"],
         "ans": "Los viernes y los sábados", "why": "«Los viernes y los sábados hay música»"},
    ],
    "vf": [
        {"q": "El salón tiene poca luz.", "ans": False, "prueba": "es muy luminoso"},
        {"q": "En el dormitorio pequeño hay un armario.", "ans": False,
         "prueba": "en el pequeño no hay armario"},
        {"q": "A Sam el ruido de la plaza no le molesta.", "ans": True,
         "prueba": "a mí eso me gusta"},
    ],
    "produccion": {
        "prompt": "Enseña tú tu casa a alguien que la visita. Graba cinco frases: qué hay en "
                  "cada habitación, dónde está cada mueble (encima de · debajo de · al lado de) "
                  "y qué falta o qué no funciona.",
        "modo": "grabar",
        "modelo": "Este es… Aquí hay… El/La … está … de … En … no hay… y … no funciona.",
    },
}


TODOS = {("C5", 0): C5_U0, ("C6+", 0): C6P_U0,
         ("C5", 1): C5_U1, ("C6+", 1): C6P_U1,
         ("C5", 2): C5_U2, ("C6+", 2): C6P_U2,
         ("C5", 3): C5_U3, ("C6+", 3): C6P_U3,
         ("C5", 4): C5_U4, ("C6+", 4): C6P_U4,
         ("C5", 5): C5_U5, ("C6+", 5): C6P_U5,
         ("C5", 6): C5_U6, ("C6+", 6): C6P_U6,
         ("C5", 7): C5_U7}


def controla():
    """De ladder eist vijf detailvragen; laat het hier falen, niet in de klas."""
    for clave, f in TODOS.items():
        assert len(f["detalle"]) == 5, "%s: %d detailvragen, verwacht 5" % (f["id"], len(f["detalle"]))
        assert len(f["vf"]) >= 2, f["id"]
        assert len(f["situacion"]["claves"]) == 3, f["id"]
        for v in f["vf"]:
            # het bewijs moet letterlijk in het fragment staan, anders is «met
            # bewijs» een lege eis
            texto = " ".join(g["es"] for g in f["guion"]).lower()
            assert v["prueba"].lower() in texto, (f["id"], v["prueba"])
        for d in f["detalle"]:
            assert d["ans"] in d["opts"], (f["id"], d["q"])


controla()
