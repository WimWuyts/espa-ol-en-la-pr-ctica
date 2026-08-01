#!/usr/bin/env python3
"""Leesteksten per cursus en unit — één bron voor print én hub.

De leesroute volgt CLAUDE.md §14bis:
  voorspellen -> globaal begrip -> scannen -> juist/fout MET BEWIJS ->
  betekenis uit context -> productieve reactie.

Tekstsoort is per unit gekozen bij het thema en verschilt bewust van de
tekstsoort van het luisterfragment van diezelfde unit (afspraak auteur
2026-07-30: één leestekst én één luisterfragment per unit, met verschillende
inhoud, elk op twee dragers).

`texto` is een lijst blokken; elk blok is (soort, inhoud) zodat print en hub
dezelfde structuur kunnen renderen zonder HTML in de data te zetten.
"""

# ---------------------------------------------------------------------------
# C5 · U0 — anuncio (aanplakbiljet op school). Recycleert: getallen, dagen,
# saludos, países, el mundo hispano. Luisterfragment van U0 is een dialoog.
# ---------------------------------------------------------------------------
C5_U0 = {
    "id": "C5-U0-LEC-01",
    "ancla": "c5-u0-lec-01",
    "titulo": "El Club de Español",
    "tipo": "anuncio (cartel del instituto)",
    "emisor": "El club de español del instituto",
    "receptor": "Los alumnos del primer año",
    "objetivo": "Convencerte de apuntarte al club",
    "prediccion": {
        "q": "Kijk eerst alleen naar de titel, de vlaggen en de getallen. Wat verwacht je?",
        "opts": ["Een uitnodiging om mee te doen", "Een examenrooster", "Een nieuwsbericht uit Spanje"],
        "ans": "Een uitnodiging om mee te doen",
        "why": "Een cartel met dagen, uren en «¡Apúntate!» nodigt uit.",
    },
    "texto": [
        ("titulo", "¡APÚNTATE AL CLUB DE ESPAÑOL! 🇪🇸🇲🇽🇨🇴🇵🇪"),
        ("lema", "Un idioma, veinte países, una ruta."),
        ("p", "¿Hablas un poco de español? ¿O cero español? ¡No importa! "
              "En el club hablamos, cantamos y jugamos en español."),
        ("lista", [
            "¿Cuándo? Los martes y los jueves, de cuatro a cinco.",
            "¿Dónde? En el aula catorce, primera planta.",
            "¿Cuánto cuesta? ¡Cero euros!",
            "¿Cuántos somos? Ahora somos dieciocho. Hay sitio para veinte.",
        ]),
        ("p", "Este año viajamos por el mundo hispano: España, México, Colombia y Perú. "
              "Cada mes, un país y una fiesta."),
        ("firma", "Escribe a: club.espanol@instituto.be — o habla con la señora Ortega."),
    ],
    "traduccion": "Word lid van de Spaanse club! Eén taal, twintig landen, één route. "
                  "Spreek je een beetje Spaans? Of geen woord? Maakt niet uit! In de club praten, "
                  "zingen en spelen we in het Spaans. Wanneer? Dinsdag en donderdag, van vier tot vijf. "
                  "Waar? In lokaal veertien, eerste verdieping. Wat kost het? Nul euro! Met hoeveel zijn we? "
                  "Nu zijn we achttien. Er is plaats voor twintig. Dit jaar reizen we door de Spaanstalige "
                  "wereld: Spanje, Mexico, Colombia en Peru. Elke maand een land en een feest.",
    "global": {
        "q": "¿Para qué es este texto?",
        "opts": ["Para invitarte al club", "Para explicar un examen", "Para vender billetes"],
        "ans": "Para invitarte al club",
    },
    # scannen: informatie snel terugvinden, niet begrijpen-in-detail
    "escanear": [
        {"q": "¿En qué aula es el club?", "ans": "14", "alt": ["catorce", "el aula 14", "aula catorce"],
         "why": "«En el aula catorce»"},
        {"q": "¿Cuántos alumnos hay ahora en el club?", "ans": "18",
         "alt": ["dieciocho"], "why": "«Ahora somos dieciocho»"},
        {"q": "¿Cuánto cuesta? (en cifras)", "ans": "0", "alt": ["cero", "0 euros", "cero euros"],
         "why": "«¡Cero euros!»"},
        {"q": "¿Cuántos países visita el club este año?", "ans": "4",
         "alt": ["cuatro"], "why": "España, México, Colombia y Perú"},
    ],
    "vf": [
        {"q": "El club es gratis.", "ans": True, "prueba": "¡Cero euros!"},
        {"q": "El club es solo para alumnos que ya hablan español.", "ans": False,
         "prueba": "¿O cero español? ¡No importa!"},
        {"q": "El club se reúne dos días por semana.", "ans": True,
         "prueba": "Los martes y los jueves"},
        {"q": "Todavía hay sitio en el club.", "ans": True, "prueba": "Hay sitio para veinte"},
    ],
    # betekenis uit context: het woord staat in de tekst, de leerling leidt af
    "contexto": [
        {"q": "«¡Apúntate!» — ¿qué significa aquí?",
         "opts": ["Schrijf je in", "Wijs aan", "Let op"], "ans": "Schrijf je in",
         "why": "Het is een oproep aan het eind van een uitnodiging."},
        {"q": "«Hay sitio para veinte» — ¿qué es «sitio»?",
         "opts": ["plaats", "website", "tijd"], "ans": "plaats",
         "why": "Er zijn er nu 18 en er kunnen er 20 bij → plaats."},
        {"q": "«No importa» — ¿qué significa?",
         "opts": ["Het maakt niet uit", "Het is belangrijk", "Het is verboden"],
         "ans": "Het maakt niet uit",
         "why": "Reactie op «¿O cero español?» — het is geen bezwaar."},
    ],
    "produccion": {
        "prompt": "Escribe un mensaje corto a la señora Ortega (3–4 frases): saluda, "
                  "di cómo te llamas, de dónde eres y por qué quieres entrar en el club.",
        "modelo": "Buenos días, señora Ortega. Me llamo… Soy de… Quiero entrar en el club "
                  "porque me gusta el español. ¡Gracias!",
    },
}

# ---------------------------------------------------------------------------
# C6+ · U0 — tablón de anuncios. Recycleert presente, ser/estar, concordancia,
# países en nacionalidades. Luisterfragment van U0 is een dialoog op de speelplaats.
# ---------------------------------------------------------------------------
C6P_U0 = {
    "id": "C6P-U0-LEC-01",
    "ancla": "c6p-u0-lec-01",
    "titulo": "El tablón de anuncios",
    "tipo": "tablón de anuncios (drie korte berichten)",
    "emisor": "Tres alumnos del instituto",
    "receptor": "Los demás alumnos",
    "objetivo": "Buscar compañeros, vender algo, invitar",
    "prediccion": {
        "q": "Kijk naar de drie kaders en de emoji. Wat verwacht je?",
        "opts": ["Drie losse berichtjes met een vraag", "Eén lange informatieve tekst",
                 "Een verslag van een uitstap"],
        "ans": "Drie losse berichtjes met een vraag",
        "why": "Een tablón bestaat uit korte, onafhankelijke aankondigingen.",
    },
    "texto": [
        ("titulo", "TABLÓN DE ANUNCIOS · Instituto Santa Clara"),
        ("aviso", ["🎸 BUSCO GRUPO DE MÚSICA",
                   "Me llamo Mateo, soy argentino y soy nuevo en el instituto. Toco la guitarra "
                   "desde los ocho años. Busco compañeros para tocar los viernes. "
                   "No soy profesional, pero soy constante. ¿Te animas?"]),
        ("aviso", ["📚 VENDO LIBROS DE SEGUNDA MANO",
                   "Los libros están en muy buen estado. Son de cuarto curso. "
                   "Cuestan diez euros cada uno, o quince los dos. "
                   "Estoy en el patio a la hora del recreo. Pregunta por Valen."]),
        ("aviso", ["🌎 INTERCAMBIO DE LENGUAS",
                   "Somos cinco alumnos de México, Colombia y Perú. Queremos hablar neerlandés "
                   "y vosotros queréis hablar español. Nos reunimos los miércoles en la biblioteca. "
                   "Es gratis y es divertido. ¡Todos sois bienvenidos!"]),
    ],
    "traduccion": "PRIKBORD · Ik zoek een muziekgroep: ik heet Mateo, ik ben Argentijn en ik ben "
                  "nieuw op school. Ik speel gitaar sinds mijn achtste. Ik zoek medespelers voor "
                  "op vrijdag. Ik ben geen professional, maar wel volhardend. Doe je mee? — "
                  "Ik verkoop tweedehands boeken: ze zijn in heel goede staat, van het vierde jaar. "
                  "Ze kosten tien euro per stuk, of vijftien voor twee. Ik sta op de speelplaats "
                  "tijdens de pauze. Vraag naar Valen. — Talenuitwisseling: we zijn met vijf "
                  "leerlingen uit Mexico, Colombia en Peru. Wij willen Nederlands spreken en jullie "
                  "willen Spaans spreken. We komen samen op woensdag in de bibliotheek. Het is "
                  "gratis en het is leuk. Iedereen is welkom!",
    "global": {
        "q": "¿Qué tienen en común los tres avisos?",
        "opts": ["Los tres buscan contacto con otros alumnos",
                 "Los tres anuncian un examen", "Los tres son de la misma persona"],
        "ans": "Los tres buscan contacto con otros alumnos",
    },
    "escanear": [
        {"q": "¿Cuánto cuestan dos libros? (en cifras)", "ans": "15",
         "alt": ["quince", "15 euros", "quince euros"], "why": "«o quince los dos»"},
        {"q": "¿Qué día se reúne el intercambio de lenguas?", "ans": "miércoles",
         "alt": ["los miércoles", "el miércoles"], "why": "«Nos reunimos los miércoles»"},
        {"q": "¿Desde qué edad toca Mateo la guitarra? (en cifras)", "ans": "8",
         "alt": ["ocho", "8 años"], "why": "«desde los ocho años»"},
        {"q": "¿Cuántos alumnos organizan el intercambio?", "ans": "5",
         "alt": ["cinco"], "why": "«Somos cinco alumnos»"},
    ],
    "vf": [
        {"q": "Mateo es un guitarrista profesional.", "ans": False, "prueba": "No soy profesional"},
        {"q": "Los libros de Valen están estropeados.", "ans": False,
         "prueba": "Los libros están en muy buen estado"},
        {"q": "El intercambio de lenguas no cuesta nada.", "ans": True, "prueba": "Es gratis"},
        {"q": "Mateo lleva poco tiempo en el instituto.", "ans": True, "prueba": "soy nuevo en el instituto"},
    ],
    "contexto": [
        {"q": "«¿Te animas?» — ¿qué quiere decir Mateo?",
         "opts": ["Heb je zin om mee te doen?", "Ben je boos?", "Kun je het uitleggen?"],
         "ans": "Heb je zin om mee te doen?",
         "why": "Het sluit een oproep af om samen te spelen."},
        {"q": "«de segunda mano» — ¿qué significa?",
         "opts": ["tweedehands", "met twee handen", "van de tweede verdieping"],
         "ans": "tweedehands",
         "why": "Het gaat om boeken die al gebruikt zijn en nu verkocht worden."},
        {"q": "«Nos reunimos» — ¿qué hacen?",
         "opts": ["Ze komen samen", "Ze studeren alleen", "Ze schrijven zich in"],
         "ans": "Ze komen samen",
         "why": "Er staat een dag en een plaats bij: woensdag, bibliotheek."},
    ],
    "produccion": {
        "prompt": "Escribe tu propio aviso para el tablón (4–5 frases): un título con emoji, "
                  "quién eres, qué buscas o qué ofreces, cuándo y dónde.",
        "modelo": "⚽ BUSCO EQUIPO DE FÚTBOL — Me llamo… Soy de… Juego desde los… años. "
                  "Nos vemos los… en… ¿Te animas?",
    },
}

# ---------------------------------------------------------------------------
# C5 · U1 «¿Quién eres?» — parada Madrid
# Tekstsoort bewust anders dan U0 (daar een cartel/anuncio): hier een perfil uit
# een uitwisselings-app, zodat de leerling een ándere leesstrategie oefent —
# scannen in een ingevuld formulier in plaats van in doorlopende reclametekst.
# ---------------------------------------------------------------------------
C5_U1 = {
    "id": "C5-U1-LEC-01",
    "ancla": "c5-u1-lec-01",
    "titulo": "Busco un compi de intercambio",
    "tipo": "perfil (app de intercambio lingüístico)",
    "emisor": "Álex, un chico de Madrid",
    "receptor": "Alumnos de español de toda Europa",
    "objetivo": "Encontrar a alguien para hablar español y neerlandés",
    "prediccion": {
        "q": "Kijk eerst alleen naar de kopjes, de vlaggen en de getallen. Wat voor tekst is dit?",
        "opts": ["Een profiel om iemand te leren kennen", "Een treinticket", "Een menukaart"],
        "ans": "Een profiel om iemand te leren kennen",
    },
    "texto": [
        ["titulo", "BUSCO COMPI DE INTERCAMBIO 🇪🇸 ↔ 🇧🇪"],
        ["lema", "Tú me hablas en neerlandés, yo te hablo en español."],
        ["lista", [
            "Nombre: Álex Moreno Gil",
            "Edad: tengo dieciséis años",
            "Ciudad: Madrid, España. Soy español.",
            "Instituto: IES Cervantes, cuarto curso",
            "Lenguas: hablo español e inglés. Estudio francés.",
        ]],
        ["p", "¡Hola! Me llamo Álex y vivo en Madrid, en el barrio de Lavapiés. "
              "Estudio en el IES Cervantes y este año aprendo francés."],
        ["p", "En mi tiempo libre escucho música, juego al baloncesto y leo cómics. "
              "Los sábados trabajo en la tienda de mi tía."],
        ["p", "Busco un compi de Bélgica o de los Países Bajos. Hablamos media hora en español "
              "y media hora en neerlandés. ¿Te apuntas?"],
        ["firma", "Escríbeme: alex.moreno@correo.es · ¿Cómo te llamas tú?"],
    ],
    "traduccion": "Ik zoek een taalmaatje. Jij spreekt Nederlands tegen mij, ik spreek Spaans "
                  "tegen jou. Hallo! Ik heet Álex en ik woon in Madrid, in de wijk Lavapiés. Ik "
                  "zit op het IES Cervantes en dit jaar leer ik Frans. In mijn vrije tijd luister "
                  "ik muziek, speel ik basket en lees ik strips. Op zaterdag werk ik in de winkel "
                  "van mijn tante. Ik zoek een maatje uit België of Nederland. We praten een half "
                  "uur Spaans en een half uur Nederlands. Doe je mee?",
    "global": {
        "q": "¿Para qué escribe Álex este perfil?",
        "opts": ["Para buscar a alguien con quien practicar lenguas",
                 "Para vender cómics", "Para invitarte a su instituto"],
        "ans": "Para buscar a alguien con quien practicar lenguas",
    },
    "escanear": [
        {"q": "¿Cuántos años tiene Álex?", "ans": "16",
         "alt": ["dieciséis", "dieciseis", "tiene dieciséis años", "16 años"],
         "why": "«tengo dieciséis años»"},
        {"q": "¿En qué ciudad vive?", "ans": "Madrid", "alt": ["en madrid"],
         "why": "«vivo en Madrid»"},
        {"q": "¿Cómo se llama su instituto?", "ans": "IES Cervantes",
         "alt": ["cervantes", "ies cervantes"], "why": "«Estudio en el IES Cervantes»"},
        {"q": "¿Qué lengua estudia este año?", "ans": "francés",
         "alt": ["el francés", "frances"], "why": "«este año aprendo francés»"},
        {"q": "¿Qué día trabaja?", "ans": "los sábados",
         "alt": ["sábados", "sabados", "el sábado", "los sabados"],
         "why": "«Los sábados trabajo en la tienda de mi tía»"},
    ],
    "vf": [
        {"q": "Álex es español.", "ans": True, "prueba": "soy español"},
        {"q": "Álex vive en Sevilla.", "ans": False, "prueba": "vivo en madrid"},
        {"q": "Álex habla inglés.", "ans": True, "prueba": "hablo español e inglés"},
        {"q": "Álex juega al fútbol.", "ans": False, "prueba": "juego al baloncesto"},
        {"q": "Álex trabaja en la tienda de su tía.", "ans": True,
         "prueba": "trabajo en la tienda de mi tía"},
    ],
    "contexto": [
        {"q": "«compi» — ¿qué es?", "opts": ["een maatje, een partner", "een boek", "een les"],
         "ans": "een maatje, een partner",
         "why": "Korte spreektaal voor «compañero» — de hele tekst gaat over samen oefenen."},
        {"q": "«¿Te apuntas?» — ¿qué te pide Álex?",
         "opts": ["Of je meedoet", "Of je opschrijft wat hij zegt", "Of je hem aanwijst"],
         "ans": "Of je meedoet", "why": "Het staat aan het eind, als uitnodiging."},
        {"q": "«en mi tiempo libre» — ¿cuándo?",
         "opts": ["Als hij geen school heeft", "Tijdens de les", "'s nachts"],
         "ans": "Als hij geen school heeft",
         "why": "Erna volgen hobby's, geen schoolvakken."},
    ],
    "produccion": {
        "prompt": "Escribe tu propio perfil para Álex (4–5 frases): cómo te llamas, cuántos años "
                  "tienes, de dónde eres, qué lenguas hablas y qué haces en tu tiempo libre.",
        "modelo": "Hola, Álex. Me llamo… Tengo… años. Soy de… y vivo en… Hablo… y estudio… "
                  "En mi tiempo libre…",
    },
}


# ---------------------------------------------------------------------------
# C6+ · U1 — la rutina diaria, parada España
# Tekstsoort: entrada de blog. Een doorlopend verhaal met tijdsaanduidingen,
# zodat het scannen naar úren gebeurt en de reflexieve werkwoorden in
# natuurlijke context terugkomen.
# ---------------------------------------------------------------------------
C6P_U1 = {
    "id": "C6P-U1-LEC-01",
    "ancla": "c6p-u1-lec-01",
    "titulo": "Un martes cualquiera",
    "tipo": "entrada de blog",
    "emisor": "Marta, estudiante en Salamanca",
    "receptor": "Los lectores de su blog «Mi vida en España»",
    "objetivo": "Contar cómo es un día normal para ella",
    "prediccion": {
        "q": "Kijk eerst alleen naar de titel en de uren die in de tekst staan. Waarover gaat dit?",
        "opts": ["Over een gewone dag van begin tot eind", "Over een reis naar Amerika",
                 "Over een examen"],
        "ans": "Over een gewone dag van begin tot eind",
    },
    "texto": [
        ["titulo", "UN MARTES CUALQUIERA ⏰"],
        ["lema", "Mi vida en España · entrada del 12 de marzo"],
        ["p", "Me despierto a las siete menos cuarto, pero no me levanto hasta las siete. "
              "Me ducho rápido, me visto y desayuno un café con tostadas."],
        ["p", "A las ocho salgo de casa. La facultad está lejos, así que voy en autobús. "
              "Las clases empiezan a las nueve y terminan a la una y media."],
        ["p", "Como con mis compañeros en la cafetería. Me gusta mucho la tortilla de patatas, "
              "pero no me gustan nada las lentejas."],
        ["lista", [
            "07:00 — me levanto",
            "08:00 — salgo de casa",
            "09:00 — empiezan las clases",
            "13:30 — termino y como",
            "17:00 — estudio en la biblioteca",
            "23:30 — me acuesto",
        ]],
        ["p", "Por la tarde estudio en la biblioteca hasta las siete. Después voy al gimnasio "
              "dos días por semana. Estoy cansada, pero estoy contenta."],
        ["firma", "Me acuesto a las once y media. ¿Y tú? ¿A qué hora te acuestas?"],
    ],
    "traduccion": "Een doordeweekse dinsdag. Ik word wakker om kwart voor zeven, maar ik sta pas "
                  "om zeven uur op. Ik douche snel, kleed me aan en ontbijt met koffie en "
                  "geroosterd brood. Om acht uur ga ik de deur uit. De faculteit is ver, dus ik "
                  "ga met de bus. De lessen beginnen om negen uur en eindigen om half twee. Ik eet "
                  "met mijn medestudenten in de cafetaria. Ik hou erg van aardappelomelet, maar ik "
                  "hou helemaal niet van linzen. 's Middags studeer ik tot zeven uur in de "
                  "bibliotheek. Daarna ga ik twee dagen per week naar de sportschool. Ik ben moe, "
                  "maar ik ben tevreden. Ik ga om half twaalf slapen. En jij? Hoe laat ga jij slapen?",
    "global": {
        "q": "¿De qué trata la entrada?",
        "opts": ["De la rutina diaria de Marta", "De sus vacaciones", "De un examen difícil"],
        "ans": "De la rutina diaria de Marta",
    },
    "escanear": [
        {"q": "¿A qué hora se levanta Marta?", "ans": "a las siete",
         "alt": ["siete", "las siete", "7:00", "07:00", "a las 7"],
         "why": "«no me levanto hasta las siete»"},
        {"q": "¿Cómo va a la facultad?", "ans": "en autobús",
         "alt": ["autobús", "autobus", "en autobus", "el autobús"], "why": "«voy en autobús»"},
        {"q": "¿A qué hora terminan las clases?", "ans": "a la una y media",
         "alt": ["la una y media", "una y media", "13:30", "1:30"],
         "why": "«terminan a la una y media»"},
        {"q": "¿Dónde estudia por la tarde?", "ans": "en la biblioteca",
         "alt": ["la biblioteca", "biblioteca"], "why": "«estudio en la biblioteca»"},
        {"q": "¿Cuántos días por semana va al gimnasio?", "ans": "dos",
         "alt": ["2", "dos días", "dos dias"], "why": "«dos días por semana»"},
    ],
    "vf": [
        {"q": "Marta se ducha por la mañana.", "ans": True, "prueba": "me ducho rápido"},
        {"q": "A Marta le gustan las lentejas.", "ans": False,
         "prueba": "no me gustan nada las lentejas"},
        {"q": "Marta come sola.", "ans": False, "prueba": "como con mis compañeros"},
        {"q": "Marta se acuesta a las once y media.", "ans": True,
         "prueba": "me acuesto a las once y media"},
        {"q": "Marta va a la facultad en coche.", "ans": False, "prueba": "voy en autobús"},
    ],
    "contexto": [
        {"q": "«no me levanto hasta las siete» — ¿qué significa «hasta»?",
         "opts": ["tot", "vanaf", "zonder"], "ans": "tot",
         "why": "Ze wordt eerder wakker, maar staat pas óm zeven uur op."},
        {"q": "«así que voy en autobús» — ¿qué expresa «así que»?",
         "opts": ["een gevolg (dus)", "een tegenstelling (maar)", "een reden (omdat)"],
         "ans": "een gevolg (dus)",
         "why": "De faculteit is ver → dáárom de bus. Let op: «dus» is nooit «luego»."},
        {"q": "«Estoy cansada, pero estoy contenta» — ¿por qué «estoy» y no «soy»?",
         "opts": ["Het is hoe ze zich nú voelt", "Het is haar karakter", "Het is haar beroep"],
         "ans": "Het is hoe ze zich nú voelt",
         "why": "Toestand van het moment → estar."},
    ],
    "produccion": {
        "prompt": "Escribe tu propio martes (5–6 frases): a qué hora te levantas, cómo vas al "
                  "instituto, cuándo empiezan y terminan las clases, qué te gusta comer y a qué "
                  "hora te acuestas.",
        "modelo": "Me levanto a las… Voy al instituto en… Las clases empiezan a las… y terminan "
                  "a las… Me gusta… pero no me gusta… Me acuesto a las…",
    },
}


# ---------------------------------------------------------------------------
# C5 · U2 «Mi gente» — parada Sevilla
# Tekstsoort: correo electrónico. Nieuw genre naast anuncio (U0) en perfil (U1):
# een persoonlijke brief met een aanhef, een kop met velden en een afsluiting,
# zodat de leerling leert scannen in een mailkop én in doorlopend proza.
# Het luisterfragment van deze unit is een klassenquiz — andere inhoud, ander genre.
# ---------------------------------------------------------------------------
C5_U2 = {
    "id": "C5-U2-LEC-01",
    "ancla": "c5-u2-lec-01",
    "titulo": "Mi familia en una foto",
    "tipo": "correo electrónico (con una foto adjunta)",
    "emisor": "Lucía, desde Sevilla",
    "receptor": "Sam, su compi de intercambio en Bélgica",
    "objetivo": "Presentarte a toda su familia",
    "prediccion": {
        "q": "Kijk eerst alleen naar de kop (De · Para · Asunto) en de foto. Wat voor tekst is dit?",
        "opts": ["Een persoonlijk bericht aan één iemand", "Een affiche voor de hele school",
                 "Een krantenartikel"],
        "ans": "Een persoonlijk bericht aan één iemand",
        "why": "Een mail heeft één afzender en één ontvanger — dat staat bovenaan.",
    },
    "texto": [
        ["titulo", "✉️ ¡MI FAMILIA EN UNA FOTO!"],
        ["lista", [
            "De: lucia.ramirez@correo.es",
            "Para: sam@correo.be",
            "Asunto: mi familia",
            "Adjunto: familia.jpg",
        ]],
        ["p", "¡Hola, Sam! ¿Qué tal? Aquí te mando la foto de mi familia. "
              "Somos seis en casa: mis padres, mis dos hermanos, mi abuela y yo."],
        ["p", "Mi padre se llama Antonio y tiene cuarenta y ocho años. Es alto y moreno, "
              "y lleva barba. Es muy tranquilo. Mi madre se llama Carmen. Tiene cuarenta y "
              "cinco años, es baja y tiene el pelo rizado. Es profesora y es muy habladora."],
        ["p", "Mi hermano mayor se llama Pablo. Tiene diecinueve años y estudia en Granada. "
              "Mi hermana menor se llama Marta y tiene once años. Es pelirroja y es muy alegre."],
        ["p", "Mi abuela Rosario vive con nosotros. Tiene setenta y nueve años y es la más "
              "graciosa de la familia. También tenemos un perro pequeño. Se llama Curro."],
        ["firma", "¿Y tu familia? ¿Cuántos sois en casa? Un abrazo, Lucía"],
    ],
    "traduccion": "Mijn familie op één foto. Hallo Sam! Hoe gaat het? Hierbij stuur ik je de foto "
                  "van mijn familie. We zijn met zes thuis: mijn ouders, mijn twee broers en "
                  "zussen, mijn oma en ik. Mijn vader heet Antonio en is achtenveertig. Hij is "
                  "groot en donker, en hij heeft een baard. Hij is heel rustig. Mijn moeder heet "
                  "Carmen. Ze is vijfenveertig, ze is klein en heeft krullend haar. Ze is lerares "
                  "en ze praat heel veel. Mijn oudere broer heet Pablo. Hij is negentien en "
                  "studeert in Granada. Mijn jongere zus heet Marta en is elf. Ze heeft rood haar "
                  "en is heel vrolijk. Mijn oma Rosario woont bij ons. Ze is negenenzeventig en is "
                  "de grappigste van de familie. We hebben ook een kleine hond. Hij heet Curro. "
                  "En jouw familie? Met hoeveel zijn jullie thuis? Een dikke knuffel, Lucía.",
    "global": {
        "q": "¿Para qué escribe Lucía este correo?",
        "opts": ["Para presentar a su familia", "Para invitar a Sam a una fiesta",
                 "Para pedir ayuda con los deberes"],
        "ans": "Para presentar a su familia",
    },
    "escanear": [
        {"q": "¿Cuántas personas viven en casa de Lucía?", "ans": "6",
         "alt": ["seis", "somos seis", "6 personas"], "why": "«Somos seis en casa»"},
        {"q": "¿Cómo se llama el padre?", "ans": "Antonio",
         "alt": ["antonio", "se llama antonio"], "why": "«Mi padre se llama Antonio»"},
        {"q": "¿Cuántos años tiene la abuela? (en cifras)", "ans": "79",
         "alt": ["setenta y nueve", "79 años"], "why": "«Tiene setenta y nueve años»"},
        {"q": "¿Dónde estudia Pablo?", "ans": "en Granada", "alt": ["granada"],
         "why": "«estudia en Granada»"},
        {"q": "¿Cómo se llama el perro?", "ans": "Curro", "alt": ["curro"],
         "why": "«Se llama Curro»"},
    ],
    "vf": [
        {"q": "Lucía tiene dos hermanos.", "ans": True, "prueba": "mis dos hermanos"},
        {"q": "El padre de Lucía es rubio.", "ans": False, "prueba": "es alto y moreno"},
        {"q": "La madre de Lucía es profesora.", "ans": True, "prueba": "es profesora"},
        {"q": "Marta es la hermana mayor.", "ans": False,
         "prueba": "mi hermana menor se llama marta"},
        {"q": "La abuela vive con la familia.", "ans": True, "prueba": "vive con nosotros"},
    ],
    "contexto": [
        {"q": "«Somos seis en casa» — ¿qué cuenta Lucía aquí?",
         "opts": ["Cuántas personas viven allí", "Cuántos años tiene", "Cuántas habitaciones hay"],
         "ans": "Cuántas personas viven allí",
         "why": "Erna volgt de opsomming van de personen."},
        {"q": "«lleva barba» — ¿qué significa «lleva» aquí?",
         "opts": ["heeft (draagt)", "brengt", "neemt mee"], "ans": "heeft (draagt)",
         "why": "Het staat tussen twee uiterlijke kenmerken."},
        {"q": "«mi hermano mayor» ↔ «mi hermana menor» — ¿qué contrastan?",
         "opts": ["de leeftijd", "de lengte", "het karakter"], "ans": "de leeftijd",
         "why": "Pablo is 19, Marta is 11 — mayor/menor gaat over ouder/jonger, niet groter/kleiner."},
        {"q": "«la más graciosa de la familia» — ¿qué quiere decir?",
         "opts": ["de grappigste van allemaal", "de oudste van allemaal", "de kleinste van allemaal"],
         "ans": "de grappigste van allemaal",
         "why": "«la más + adjectief» = de -ste."},
    ],
    "produccion": {
        "prompt": "Contesta a Lucía (5–6 frases): cuántos sois en casa, quién es quién, "
                  "cómo son (dos detalles físicos y uno de carácter) y si tienes mascota.",
        "modelo": "Hola, Lucía. En casa somos… Mi… se llama… y tiene… años. Es… y tiene el pelo… "
                  "Mi… es muy… También tenemos…",
    },
}


# ---------------------------------------------------------------------------
# C6+ · U2 «Aquí vivo» — parada Cartagena
# Tekstsoort: reseñas (beoordelingen op een boekingssite). Nieuw genre naast
# tablón (U0) en blog (U1): twee tegengestelde meningen over dezelfde woning,
# zodat de leerling niet alleen feiten zoekt maar ook standpunten vergelijkt.
# Het luisterfragment van deze unit is een telefoongesprek met een routebeschrijving.
# ---------------------------------------------------------------------------
C6P_U2 = {
    "id": "C6P-U2-LEC-01",
    "ancla": "c6p-u2-lec-01",
    "titulo": "«Casa Azul» — dos reseñas",
    "tipo": "reseñas (web de alojamiento)",
    "emisor": "Dos viajeros: Marta y Tomás",
    "receptor": "Quien busca dónde dormir en Cartagena",
    "objetivo": "Contar cómo es la casa de verdad",
    "prediccion": {
        "q": "Kijk eerst alleen naar de sterren, het cijfer en de namen. Wat voor tekst is dit?",
        "opts": ["Meningen van gasten over een woning", "Een routebeschrijving", "Een menukaart"],
        "ans": "Meningen van gasten over een woning",
        "why": "Sterren + een gemiddelde + namen van personen = beoordelingen.",
    },
    "texto": [
        ["titulo", "⭐ RESEÑAS · «Casa Azul» — Centro Histórico, Cartagena"],
        ["lema", "4,6 sobre 5 · 128 opiniones · Anfitriona: Valen"],
        ["aviso", ["★★★★★ Marta, de Madrid — «Un balcón lleno de flores»",
                   "El apartamento está en la calle de la Iglesia, muy cerca de la muralla. "
                   "Hay dos dormitorios, un salón grande y una cocina pequeña. Encima de la cama "
                   "hay un ventilador, y eso es importante: en Cartagena hace mucho calor. "
                   "El balcón está lleno de flores. El barrio es antiguo y por la mañana está "
                   "muy tranquilo."]],
        ["aviso", ["★★★☆☆ Tomás, de Lima — «Bonito, pero ruidoso»",
                   "La casa es bonita y está muy limpia. El problema es el ruido: debajo del "
                   "balcón hay un bar y la música no para hasta las dos. Si duermes poco, pide "
                   "la habitación de detrás. La parada del bus está a cinco minutos a pie."]],
        ["p", "Respuesta de la anfitriona: «¡Gracias por vuestros comentarios! Es verdad que el "
              "centro es ruidoso los fines de semana. Entre semana está mucho más tranquilo. "
              "La habitación de detrás no da a la calle.»"],
        ["firma", "Solo puedes escribir una reseña si duermes una noche en la casa."],
    ],
    "traduccion": "BEOORDELINGEN · «Casa Azul», historisch centrum, Cartagena. 4,6 op 5 · 128 "
                  "meningen · Gastvrouw: Valen. ★★★★★ Marta, uit Madrid — «Een balkon vol "
                  "bloemen»: het appartement ligt in de calle de la Iglesia, vlak bij de "
                  "stadsmuur. Er zijn twee slaapkamers, een grote woonkamer en een kleine keuken. "
                  "Boven het bed hangt een ventilator, en dat is belangrijk: in Cartagena is het "
                  "erg warm. Het balkon staat vol bloemen. De buurt is oud en 's ochtends heel "
                  "rustig. ★★★☆☆ Tomás, uit Lima — «Mooi, maar lawaaierig»: het huis is mooi en "
                  "heel proper. Het probleem is het lawaai: onder het balkon is een café en de "
                  "muziek stopt pas om twee uur. Als je weinig slaapt, vraag dan de kamer "
                  "achteraan. De bushalte ligt op vijf minuten te voet. Antwoord van de "
                  "gastvrouw: «Bedankt voor jullie commentaar! Het klopt dat het centrum in het "
                  "weekend lawaaierig is. Doordeweeks is het veel rustiger. De kamer achteraan "
                  "kijkt niet uit op de straat.»",
    "global": {
        "q": "¿Qué son estos textos?",
        "opts": ["Opiniones de viajeros sobre un apartamento",
                 "Un anuncio de venta de una casa",
                 "Un artículo sobre la historia de Cartagena"],
        "ans": "Opiniones de viajeros sobre un apartamento",
    },
    "escanear": [
        {"q": "¿En qué calle está el apartamento?", "ans": "la calle de la Iglesia",
         "alt": ["calle de la iglesia", "de la iglesia", "la iglesia"],
         "why": "«está en la calle de la Iglesia»"},
        {"q": "¿Cuántos dormitorios hay? (en cifras)", "ans": "2", "alt": ["dos", "2 dormitorios"],
         "why": "«Hay dos dormitorios»"},
        {"q": "¿Qué hay encima de la cama?", "ans": "un ventilador", "alt": ["ventilador", "el ventilador"],
         "why": "«Encima de la cama hay un ventilador»"},
        {"q": "¿Hasta qué hora hay música?", "ans": "hasta las dos", "alt": ["las dos", "dos", "2"],
         "why": "«la música no para hasta las dos»"},
        {"q": "¿A cuántos minutos está la parada del bus? (en cifras)", "ans": "5",
         "alt": ["cinco", "cinco minutos", "5 minutos"], "why": "«a cinco minutos a pie»"},
    ],
    "vf": [
        {"q": "El apartamento tiene dos dormitorios.", "ans": True, "prueba": "hay dos dormitorios"},
        {"q": "La casa está lejos de la muralla.", "ans": False, "prueba": "muy cerca de la muralla"},
        {"q": "Debajo del balcón hay un bar.", "ans": True, "prueba": "debajo del balcón hay un bar"},
        {"q": "Tomás dice que la casa está sucia.", "ans": False, "prueba": "está muy limpia"},
        {"q": "La parada del bus está a cinco minutos andando.", "ans": True,
         "prueba": "está a cinco minutos a pie"},
    ],
    "contexto": [
        {"q": "«El balcón está lleno de flores» — ¿qué significa «lleno de»?",
         "opts": ["vol met", "ver van", "zonder"], "ans": "vol met",
         "why": "Het gaat over hoeveel bloemen er staan."},
        {"q": "«la música no para hasta las dos» — ¿qué quiere decir «no para»?",
         "opts": ["ze stopt niet", "ze staat niet stil", "ze begint niet"], "ans": "ze stopt niet",
         "why": "«parar» = stoppen; het is de klacht over lawaai."},
        {"q": "«pide la habitación de detrás» — ¿por qué lo aconseja Tomás?",
         "opts": ["Omdat die niet aan de straat ligt", "Omdat die groter is", "Omdat die goedkoper is"],
         "ans": "Omdat die niet aan de straat ligt",
         "why": "De gastvrouw legt het uit: «no da a la calle»."},
        {"q": "«Entre semana está mucho más tranquilo» — ¿cuándo?",
         "opts": ["Van maandag tot vrijdag", "In het weekend", "In de vakantie"],
         "ans": "Van maandag tot vrijdag",
         "why": "Het staat tegenover «los fines de semana»."},
    ],
    "produccion": {
        "prompt": "Escribe tu propia reseña de tu casa o de tu barrio (5–6 frases): cuántas "
                  "estrellas le das, qué hay, dónde está cada cosa, qué es lo mejor y qué es "
                  "lo peor.",
        "modelo": "★★★★☆ — En mi casa hay… El/La… está… Lo mejor es que… Lo peor es que… "
                  "La parada está a … minutos.",
    },
}


# ---------------------------------------------------------------------------
# C5 · U3 «El tiempo vuela» — parada Barcelona
# Tekstsoort: chat de móvil. Nieuw genre: de tekst bestaat uit korte beurten met
# een tijdstempel, dus de leerling leert lezen mét de tijdlijn erbij — precies wat
# deze unit nodig heeft (uren, dagen, frequentie).
# Het luisterfragment is een reeks spraakberichten over één zaterdag.
# ---------------------------------------------------------------------------
C5_U3 = {
    "id": "C5-U3-LEC-01",
    "ancla": "c5-u3-lec-01",
    "titulo": "¿Quedamos esta semana?",
    "tipo": "chat de móvil (conversación escrita)",
    "emisor": "Marc, alumno en Barcelona",
    "receptor": "Júlia, su compañera de clase",
    "objetivo": "Encontrar un hueco libre para estudiar juntos",
    "prediccion": {
        "q": "Kijk eerst alleen naar de uren links van elk bericht en naar de dagen. "
             "Waarover gaat dit?",
        "opts": ["Over een afspraak zoeken in een drukke week", "Over een reis naar Barcelona",
                 "Over een verjaardagsfeest"],
        "ans": "Over een afspraak zoeken in een drukke week",
        "why": "Korte beurten met tijdstempels + dagen van de week = plannen.",
    },
    "texto": [
        ["titulo", "💬 CHAT · Marc y Júlia (Barcelona)"],
        ["lema", "Jueves, 17:00 — «¿Quedamos esta semana?»"],
        ["aviso", ["Marc · 17:02",
                   "¡Hola, Júlia! ¿Quedamos esta semana para estudiar el examen de mates? "
                   "Yo puedo casi todos los días."]],
        ["aviso", ["Júlia · 17:09",
                   "¡Vale! Pero esta semana tengo poco tiempo. Los martes y los jueves voy a "
                   "natación de seis a siete y media. Y los lunes salgo tarde del instituto."]],
        ["aviso", ["Marc · 17:11",
                   "¿Y el miércoles? Yo termino a las cinco y no hago nada por la tarde."]],
        ["aviso", ["Júlia · 17:14",
                   "El miércoles perfecto. ¿A las cinco y media en la biblioteca de la plaza? "
                   "Cierra a las ocho."]],
        ["aviso", ["Marc · 17:15",
                   "Genial. Yo normalmente llego cinco minutos tarde… ¡pero el miércoles no! 😄"]],
        ["firma", "Júlia · 17:16 — «Te espero con los apuntes. ¡Hasta el miércoles!»"],
    ],
    "traduccion": "CHAT · Marc en Júlia (Barcelona). Donderdag 17:00 — «Spreken we deze week af?» "
                  "Marc: Hallo Júlia! Spreken we deze week af om voor het wiskunde-examen te "
                  "studeren? Ik kan bijna elke dag. — Júlia: Oké! Maar deze week heb ik weinig "
                  "tijd. Op dinsdag en donderdag ga ik zwemmen van zes tot half acht. En op "
                  "maandag kom ik laat van school. — Marc: En woensdag? Ik ben om vijf uur klaar "
                  "en 's namiddags doe ik niets. — Júlia: Woensdag is perfect. Om half zes in de "
                  "bibliotheek op het plein? Ze sluit om acht uur. — Marc: Top. Ik kom normaal "
                  "vijf minuten te laat… maar woensdag niet! — Júlia: Ik wacht op je met de "
                  "notities. Tot woensdag!",
    "global": {
        "q": "¿Para qué es este chat?",
        "opts": ["Para buscar un momento libre para verse", "Para hablar de las vacaciones",
                 "Para pedir ayuda con el móvil"],
        "ans": "Para buscar un momento libre para verse",
    },
    "escanear": [
        {"q": "¿A qué hora va Júlia a natación?", "ans": "de seis a siete y media",
         "alt": ["seis a siete y media", "de 6 a 7:30", "a las seis"],
         "why": "«voy a natación de seis a siete y media»"},
        {"q": "¿Qué día quedan?", "ans": "el miércoles", "alt": ["miércoles", "miercoles"],
         "why": "«El miércoles perfecto»"},
        {"q": "¿A qué hora quedan?", "ans": "a las cinco y media",
         "alt": ["cinco y media", "5:30", "17:30", "las cinco y media"],
         "why": "«¿A las cinco y media en la biblioteca…?»"},
        {"q": "¿Dónde quedan?", "ans": "en la biblioteca de la plaza",
         "alt": ["la biblioteca", "biblioteca", "en la biblioteca"],
         "why": "«en la biblioteca de la plaza»"},
        {"q": "¿Para qué examen estudian?", "ans": "de mates",
         "alt": ["mates", "matemáticas", "el examen de mates"], "why": "«el examen de mates»"},
    ],
    "vf": [
        {"q": "Júlia va a natación dos días por semana.", "ans": True,
         "prueba": "los martes y los jueves voy a natación"},
        {"q": "Quedan el martes.", "ans": False, "prueba": "el miércoles perfecto"},
        {"q": "La biblioteca cierra a las ocho.", "ans": True, "prueba": "cierra a las ocho"},
        {"q": "Marc tiene actividades el miércoles por la tarde.", "ans": False,
         "prueba": "no hago nada por la tarde"},
        {"q": "Marc suele llegar puntual.", "ans": False,
         "prueba": "normalmente llego cinco minutos tarde"},
    ],
    "contexto": [
        {"q": "«¿Quedamos esta semana?» — ¿qué propone Marc?",
         "opts": ["Afspreken om elkaar te zien", "Blijven zitten waar hij zit", "Iets kopen"],
         "ans": "Afspreken om elkaar te zien",
         "why": "Erna volgt meteen een dag en een uur."},
        {"q": "«salgo tarde del instituto» — ¿qué es «tarde» aquí?",
         "opts": ["laat op de dag", "de namiddag", "een taart"], "ans": "laat op de dag",
         "why": "Als zelfstandig naamwoord is «la tarde» de namiddag; hier staat het bij een "
                "werkwoord en betekent het «laat» — tegenover «temprano»."},
        {"q": "«Cierra a las ocho» — ¿quién o qué cierra?",
         "opts": ["La biblioteca", "Júlia", "El instituto"], "ans": "La biblioteca",
         "why": "Het staat pal na de plaats van afspraak."},
        {"q": "«Te espero con los apuntes» — ¿qué son «los apuntes»?",
         "opts": ["de notities", "de afspraken", "de punten van een toets"], "ans": "de notities",
         "why": "Ze gaan samen studeren voor een examen."},
    ],
    "produccion": {
        "prompt": "Contesta tú a Marc (4–5 frases): di qué días no puedes y por qué, propón un "
                  "día y una hora, y di dónde quedáis. Usa: los lunes… · de … a … · a las …",
        "modelo": "Hola, Marc. Los… tengo… de … a … El… puedo. ¿Quedamos a las … en …? "
                  "Normalmente llego…",
    },
}


TODOS = {("C5", 0): C5_U0, ("C6+", 0): C6P_U0,
         ("C5", 1): C5_U1, ("C6+", 1): C6P_U1,
         ("C5", 2): C5_U2, ("C6+", 2): C6P_U2,
         ("C5", 3): C5_U3}


def _texto_plano(t):
    partes = []
    for soort, inhoud in t["texto"]:
        if isinstance(inhoud, list):
            partes.extend(inhoud)
        else:
            partes.append(inhoud)
    return " ".join(partes).lower()


def controla():
    """Zonder deze controle is «juist/fout met bewijs» een lege belofte: het
    bewijs moet letterlijk in de tekst staan die de leerling voor zich heeft."""
    for clave, t in TODOS.items():
        plano = _texto_plano(t)
        for v in t["vf"]:
            assert v["prueba"].lower() in plano, (t["id"], "bewijs niet in de tekst:", v["prueba"])
        for e in t["escanear"]:
            assert e["ans"], t["id"]
        assert len(t["escanear"]) >= 4, t["id"]
        assert len(t["vf"]) >= 4, t["id"]
        assert len(t["contexto"]) >= 3, t["id"]
        for c in t["contexto"] + [t["global"], t["prediccion"]]:
            assert c["ans"] in c["opts"], (t["id"], c["q"])


controla()
