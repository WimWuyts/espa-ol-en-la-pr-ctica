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


TODOS = {("C5", 0): C5_U0, ("C6+", 0): C6P_U0,
         ("C5", 1): C5_U1, ("C6+", 1): C6P_U1,
         ("C5", 2): C5_U2}


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
