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


# ---------------------------------------------------------------------------
# C6+ · U3 «Conectados» — parada CDMX
# Tekstsoort: artículo de revista escolar met een enquête. Nieuw genre: hier
# staan cijfers én meningen naast elkaar, dus de leerling oefent scannen in een
# grafiekje én het herkennen van standpunten (creo que · me parece que).
# Het luisterfragment is een radiodebat — gesproken meningsvorming.
# ---------------------------------------------------------------------------
C6P_U3 = {
    "id": "C6P-U3-LEC-01",
    "ancla": "c6p-u3-lec-01",
    "titulo": "¿Cuántas horas de pantalla?",
    "tipo": "artículo de revista escolar (con encuesta)",
    "emisor": "La redacción de la revista del instituto",
    "receptor": "Los alumnos de cuarto, quinto y sexto",
    "objetivo": "Enseñar los resultados de una encuesta y hacer pensar",
    "prediccion": {
        "q": "Kijk eerst alleen naar de titel, de percentages en de twee citaten. "
             "Wat voor tekst is dit?",
        "opts": ["Een artikel met de uitslag van een enquête", "Een handleiding voor een app",
                 "Een advertentie voor een gsm"],
        "ans": "Een artikel met de uitslag van een enquête",
        "why": "Percentages + citaten van leerlingen = verslag van een bevraging.",
    },
    "texto": [
        ["titulo", "📱 ¿CUÁNTAS HORAS DE PANTALLA?"],
        ["lema", "Encuesta a 120 alumnos del instituto · marzo"],
        ["p", "Este mes preguntamos a ciento veinte alumnos cuánto tiempo pasan al día con "
              "el móvil. Estos son los resultados."],
        ["lista", [
            "Menos de dos horas al día: 15 %",
            "Entre dos y cuatro horas: 48 %",
            "Más de cuatro horas: 37 %",
            "Duermen con el móvil en la habitación: 71 %",
            "Apagan el móvil para estudiar: 22 %",
        ]],
        ["aviso", ["Rocío, 16 años",
                   "«Creo que exageramos con el tema. Yo uso el móvil para estudiar: veo vídeos "
                   "de mates y hablo con mis compañeras de los deberes. Me parece que el "
                   "problema no es la pantalla, es lo que haces con ella.»"]],
        ["aviso", ["Andrés, 17 años",
                   "«Pienso que sí es un problema. Yo acabo de borrar dos aplicaciones porque "
                   "me quitan demasiado tiempo. Ahora leo libros y duermo bien. No estoy "
                   "de acuerdo con Rocío: la pantalla también cansa.»"]],
        ["p", "La próxima semana vamos a organizar un debate en la biblioteca. Todos los cursos "
              "están invitados."],
        ["firma", "¿Quieres participar? Escribe a revista@instituto.mx antes del viernes."],
    ],
    "traduccion": "HOEVEEL SCHERMTIJD? Enquête bij 120 leerlingen van de school · maart. Deze "
                  "maand vragen we aan honderdtwintig leerlingen hoeveel tijd ze per dag met hun "
                  "gsm doorbrengen. Dit zijn de resultaten: minder dan twee uur per dag: 15 % · "
                  "tussen twee en vier uur: 48 % · meer dan vier uur: 37 % · slaapt met de gsm "
                  "op de kamer: 71 % · zet de gsm uit om te studeren: 22 %. — Rocío, 16 jaar: "
                  "«Ik vind dat we overdrijven. Ik gebruik mijn gsm om te studeren: ik kijk "
                  "wiskundefilmpjes en praat met mijn klasgenoten over het huiswerk. Volgens mij "
                  "is het scherm niet het probleem, wel wat je ermee doet.» — Andrés, 17 jaar: "
                  "«Ik denk dat het wél een probleem is. Ik heb net twee apps gewist omdat ze me "
                  "te veel tijd afnemen. Nu lees ik boeken en slaap ik goed. Ik ben het niet "
                  "eens met Rocío: een scherm vermoeit ook.» — Volgende week organiseren we een "
                  "debat in de bibliotheek. Alle jaren zijn uitgenodigd.",
    "global": {
        "q": "¿Para qué es este artículo?",
        "opts": ["Para enseñar los resultados de una encuesta y abrir un debate",
                 "Para vender una aplicación nueva",
                 "Para explicar cómo se configura un móvil"],
        "ans": "Para enseñar los resultados de una encuesta y abrir un debate",
    },
    "escanear": [
        {"q": "¿A cuántos alumnos preguntaron? (en cifras)", "ans": "120",
         "alt": ["ciento veinte", "120 alumnos"], "why": "«Encuesta a 120 alumnos»"},
        {"q": "¿Qué porcentaje pasa más de cuatro horas al día?", "ans": "37",
         "alt": ["37 %", "37%", "treinta y siete"], "why": "«Más de cuatro horas: 37 %»"},
        {"q": "¿Qué porcentaje duerme con el móvil en la habitación?", "ans": "71",
         "alt": ["71 %", "71%", "setenta y uno"], "why": "«Duermen con el móvil en la habitación: 71 %»"},
        {"q": "¿Cuántos años tiene Andrés? (en cifras)", "ans": "17",
         "alt": ["diecisiete", "17 años"], "why": "«Andrés, 17 años»"},
        {"q": "¿Dónde va a ser el debate?", "ans": "en la biblioteca",
         "alt": ["la biblioteca", "biblioteca"], "why": "«un debate en la biblioteca»"},
    ],
    "vf": [
        {"q": "Casi la mitad de los alumnos pasa entre dos y cuatro horas al día.", "ans": True,
         "prueba": "entre dos y cuatro horas: 48 %"},
        {"q": "Rocío piensa que la pantalla es el problema.", "ans": False,
         "prueba": "el problema no es la pantalla"},
        {"q": "Andrés ya no tiene dos de sus aplicaciones.", "ans": True,
         "prueba": "acabo de borrar dos aplicaciones"},
        {"q": "Rocío y Andrés opinan lo mismo.", "ans": False,
         "prueba": "no estoy de acuerdo con rocío"},
        {"q": "Solo una minoría apaga el móvil para estudiar.", "ans": True,
         "prueba": "apagan el móvil para estudiar: 22 %"},
    ],
    "contexto": [
        {"q": "«Me parece que…» — ¿qué hace Rocío con esas palabras?",
         "opts": ["Ze geeft haar mening", "Ze stelt een vraag", "Ze geeft een bevel"],
         "ans": "Ze geeft haar mening",
         "why": "Net als «creo que» en «pienso que» kondigt het een standpunt aan."},
        {"q": "«acabo de borrar dos aplicaciones» — ¿qué quiere decir «acabo de»?",
         "opts": ["Net, kort geleden", "Volgend jaar", "Elke dag"], "ans": "Net, kort geleden",
         "why": "«acabar de + infinitivo» = net iets gedaan hebben."},
        {"q": "«No estoy de acuerdo con Rocío» — ¿qué dice Andrés?",
         "opts": ["Hij is het niet met haar eens", "Hij kent haar niet", "Hij vindt haar aardig"],
         "ans": "Hij is het niet met haar eens",
         "why": "«estar de acuerdo» = het eens zijn."},
        {"q": "«Todos los cursos están invitados» — ¿quién puede ir al debate?",
         "opts": ["Alle jaren van de school", "Alleen de zesdejaars", "Alleen de redactie"],
         "ans": "Alle jaren van de school",
         "why": "«el curso» is hier het schooljaar, niet een cursus."},
    ],
    "produccion": {
        "prompt": "Escribe tu opinión para la revista (5–6 frases): cuántas horas pasas tú, si "
                  "te parece mucho o poco, con quién estás de acuerdo y por qué. Usa creo que · "
                  "me parece que · (no) estoy de acuerdo · por un lado… por otro…",
        "modelo": "Creo que… Yo paso … horas al día. Estoy de acuerdo con… porque… Por un lado…, "
                  "pero por otro… Acabo de…",
    },
}


# ---------------------------------------------------------------------------
# C5 · U4 «Me gusta» — parada València
# Tekstsoort: programa de festival. Nieuw genre: een uurrooster met daarnaast
# korte aanprijzingen, dus de leerling schakelt tussen snel scannen (uren,
# namen) en lezen om te kiezen — precies wat «me gusta / prefiero» vraagt.
# Het luisterfragment is een straatenquête met drie verschillende stemmen.
# ---------------------------------------------------------------------------
C5_U4 = {
    "id": "C5-U4-LEC-01",
    "ancla": "c5-u4-lec-01",
    "titulo": "Fiesta de la Música · València",
    "tipo": "programa de un festival",
    "emisor": "La organización del festival",
    "receptor": "Los jóvenes de la ciudad",
    "objetivo": "Ayudarte a elegir a qué concierto vas",
    "prediccion": {
        "q": "Kijk eerst alleen naar de uren, de namen in hoofdletters en de muziekstijlen "
             "tussen haakjes. Wat voor tekst is dit?",
        "opts": ["Het programma van een festival", "Een liedtekst", "Een treinregeling"],
        "ans": "Het programma van een festival",
        "why": "Uren + artiestennamen + podia = een programma.",
    },
    "texto": [
        ["titulo", "🎶 FIESTA DE LA MÚSICA · València"],
        ["lema", "Sábado 21 de junio · Playa de la Malvarrosa · Entrada gratuita"],
        ["lista", [
            "17:00 · Escenario del Mar — LOS ALMENDROS (pop en valenciano)",
            "19:00 · Escenario del Mar — LA NIÑA DEL SUR (flamenco urbano)",
            "21:00 · Escenario Grande — TROPICANA (cumbia y salsa)",
            "23:00 · Escenario Grande — DJ MARÍA (electrónica)",
        ]],
        ["p", "¿Te gusta bailar? Entonces tu grupo es TROPICANA: ocho músicos de Colombia y de "
              "Cuba que no paran en toda la noche."],
        ["p", "¿Prefieres escuchar tranquilo? LOS ALMENDROS tocan la guitarra y cantan en "
              "valenciano. Es un concierto relajante, perfecto para empezar la tarde."],
        ["p", "¿Te encanta el flamenco? Entonces te interesa LA NIÑA DEL SUR: mezcla flamenco y "
              "música electrónica. Sus letras hablan de la costa y del mar."],
        ["aviso", ["🍹 ZONA DE COMIDA",
                   "Hay paella, horchata y bocadillos desde las cinco. No se puede entrar con "
                   "botellas de cristal."]],
        ["firma", "Programa completo y letras de las canciones: fiestamusica.valencia.es"],
    ],
    "traduccion": "MUZIEKFEEST · Valencia. Zaterdag 21 juni · Malvarrosastrand · Gratis toegang. "
                  "17:00 Zeepodium — LOS ALMENDROS (pop in het Valenciaans) · 19:00 Zeepodium — "
                  "LA NIÑA DEL SUR (urban flamenco) · 21:00 Groot podium — TROPICANA (cumbia en "
                  "salsa) · 23:00 Groot podium — DJ MARÍA (electro). Hou je van dansen? Dan is "
                  "TROPICANA jouw groep: acht muzikanten uit Colombia en Cuba die de hele nacht "
                  "doorgaan. Luister je liever rustig? LOS ALMENDROS spelen gitaar en zingen in "
                  "het Valenciaans. Een ontspannen concert, ideaal om de avond mee te beginnen. "
                  "Ben je gek op flamenco? Dan is LA NIÑA DEL SUR iets voor jou: ze mengt "
                  "flamenco met electro. Haar teksten gaan over de kust en de zee. ETENSZONE: er "
                  "is paella, horchata en broodjes vanaf vijf uur. Glazen flessen mogen niet "
                  "binnen.",
    "global": {
        "q": "¿Para qué es este texto?",
        "opts": ["Para informar sobre los conciertos y ayudarte a elegir",
                 "Para vender instrumentos de música",
                 "Para explicar la historia de València"],
        "ans": "Para informar sobre los conciertos y ayudarte a elegir",
    },
    "escanear": [
        {"q": "¿Qué día es el festival?", "ans": "el 21 de junio",
         "alt": ["21 de junio", "sábado 21 de junio", "21/6", "21"], "why": "«Sábado 21 de junio»"},
        {"q": "¿Dónde es?", "ans": "en la playa de la Malvarrosa",
         "alt": ["la malvarrosa", "malvarrosa", "playa de la malvarrosa"],
         "why": "«Playa de la Malvarrosa»"},
        {"q": "¿A qué hora toca TROPICANA?", "ans": "21:00",
         "alt": ["a las nueve", "las nueve", "21h", "9"], "why": "«21:00 · Escenario Grande — TROPICANA»"},
        {"q": "¿Cuántos músicos tiene TROPICANA? (en cifras)", "ans": "8",
         "alt": ["ocho", "ocho músicos"], "why": "«ocho músicos de Colombia y de Cuba»"},
        {"q": "¿Desde qué hora hay comida?", "ans": "desde las cinco",
         "alt": ["las cinco", "cinco", "17:00", "5"], "why": "«desde las cinco»"},
    ],
    "vf": [
        {"q": "El festival es gratis.", "ans": True, "prueba": "entrada gratuita"},
        {"q": "TROPICANA es un grupo de cumbia y salsa.", "ans": True,
         "prueba": "tropicana (cumbia y salsa)"},
        {"q": "LOS ALMENDROS cantan en castellano.", "ans": False, "prueba": "cantan en valenciano"},
        {"q": "Se puede entrar con botellas de cristal.", "ans": False,
         "prueba": "no se puede entrar con botellas de cristal"},
        {"q": "Las letras de LA NIÑA DEL SUR hablan del mar.", "ans": True,
         "prueba": "hablan de la costa y del mar"},
    ],
    "contexto": [
        {"q": "«Entrada gratuita» — ¿cuánto cuesta?",
         "opts": ["Nada", "Cinco euros", "Depende del escenario"], "ans": "Nada",
         "why": "«gratuito» = gratis."},
        {"q": "«que no paran en toda la noche» — ¿qué quiere decir?",
         "opts": ["Ze spelen de hele nacht door", "Ze stoppen na één lied", "Ze komen niet"],
         "ans": "Ze spelen de hele nacht door", "why": "«parar» = stoppen."},
        {"q": "«mezcla flamenco y música electrónica» — ¿qué hace?",
         "opts": ["Ze combineert twee stijlen", "Ze kiest er één", "Ze speelt geen muziek"],
         "ans": "Ze combineert twee stijlen", "why": "«mezclar» = mengen."},
        {"q": "«Sus letras hablan de la costa» — ¿qué son «las letras»?",
         "opts": ["de songteksten", "de letters van het alfabet", "de brieven"],
         "ans": "de songteksten",
         "why": "In muziek is «la letra» de tekst van een lied — een valstrik voor wie aan "
                "letters denkt."},
    ],
    "produccion": {
        "prompt": "Elige un concierto y escríbele un mensaje a un amigo (4–5 frases): a cuál "
                  "vas, a qué hora, por qué te gusta ese grupo y qué no te gusta del programa.",
        "modelo": "Voy a… a las… Me encanta… porque… No me gusta nada… ¿Quieres venir? "
                  "¿Podemos quedar a las…?",
    },
}


# ---------------------------------------------------------------------------
# C6+ · U4 «De viaje» — parada Chile
# Tekstsoort: postal + diario de viaje. Nieuw genre: een handgeschreven kaart met
# een kort dagboekje erbij. Het perfecto compuesto zit er natuurlijk in («he
# estado», «he visto») en de leerling leest twee stemmen over dezelfde reis.
# Het luisterfragment is een gesprek aan de balie van een hostal.
# ---------------------------------------------------------------------------
C6P_U4 = {
    "id": "C6P-U4-LEC-01",
    "ancla": "c6p-u4-lec-01",
    "titulo": "Una postal desde Valparaíso",
    "tipo": "postal + diario de viaje",
    "emisor": "Nina, de viaje por Chile",
    "receptor": "Su clase en Bélgica",
    "objetivo": "Contar lo que ha hecho y lo que le falta por ver",
    "prediccion": {
        "q": "Kijk eerst alleen naar het postzegeltje, de aanhef en de datums in het "
             "dagboekje. Wat voor tekst is dit?",
        "opts": ["Een kaartje van iemand op reis", "Een reisgids", "Een hotelrekening"],
        "ans": "Een kaartje van iemand op reis",
        "why": "Een aanhef, een groet en een adres = een postkaart.",
    },
    "texto": [
        ["titulo", "📮 POSTAL DESDE VALPARAÍSO"],
        ["lema", "Para: 6ª clase de español · Instituto Santa Clara · Bélgica"],
        ["p", "¡Hola a todos! Os escribo desde un café en el cerro Alegre. He estado tres días "
              "en Valparaíso y todavía no he visto todos los murales. ¡La ciudad entera es un "
              "museo al aire libre!"],
        ["p", "He subido en los ascensores antiguos, he comido pescado en el mercado y he "
              "sacado doscientas fotos. Lo mejor ha sido el atardecer desde el cerro. "
              "Lo peor: he perdido el autobús dos veces."],
        ["aviso", ["📓 MI DIARIO — lunes 14",
                   "Hemos llegado a Santiago por la mañana. Hemos cogido un bus para "
                   "Valparaíso. Cuatro horas por la carretera de la costa. Estoy cansada pero "
                   "muy contenta."]],
        ["aviso", ["📓 MI DIARIO — miércoles 16",
                   "Hoy no he hecho nada especial y ha sido perfecto. He escrito estas "
                   "postales, he hablado con una señora del barrio y he aprendido dos palabras "
                   "nuevas: «micro» (el autobús) y «cachai» (¿entiendes?)."]],
        ["p", "Mañana vamos para el sur, al lago Llanquihue. Nunca he visto un volcán de cerca."],
        ["firma", "Un abrazo enorme, Nina · P.D.: todavía no he probado el pastel de choclo."],
    ],
    "traduccion": "POSTKAART UIT VALPARAÍSO. Voor: 6de klas Spaans · Instituto Santa Clara · "
                  "België. Hallo allemaal! Ik schrijf jullie vanuit een café op de cerro Alegre. "
                  "Ik ben hier drie dagen en ik heb nog niet alle muurschilderingen gezien. De "
                  "hele stad is een openluchtmuseum! Ik ben met de oude liften naar boven "
                  "gegaan, ik heb vis gegeten op de markt en ik heb tweehonderd foto's gemaakt. "
                  "Het mooiste was de zonsondergang vanaf de heuvel. Het ergste: ik heb de bus "
                  "twee keer gemist. — DAGBOEK maandag 14: we zijn 's ochtends in Santiago "
                  "aangekomen. We hebben een bus naar Valparaíso genomen. Vier uur over de "
                  "kustweg. Ik ben moe maar heel tevreden. — DAGBOEK woensdag 16: vandaag heb ik "
                  "niets bijzonders gedaan en dat was perfect. Ik heb deze kaarten geschreven, "
                  "ik heb met een buurvrouw gepraat en ik heb twee nieuwe woorden geleerd: "
                  "«micro» (de bus) en «cachai» (snap je?). — Morgen gaan we naar het zuiden, "
                  "naar het Llanquihuemeer. Ik heb nog nooit een vulkaan van dichtbij gezien. "
                  "Een dikke knuffel, Nina. P.S.: ik heb de pastel de choclo nog niet geproefd.",
    "global": {
        "q": "¿De qué trata la postal?",
        "opts": ["De lo que Nina ha hecho en Chile y de lo que le falta",
                 "De cómo se reserva un hotel en Chile",
                 "De la historia de los ascensores de Valparaíso"],
        "ans": "De lo que Nina ha hecho en Chile y de lo que le falta",
    },
    "escanear": [
        {"q": "¿Cuántos días ha estado Nina en Valparaíso? (en cifras)", "ans": "3",
         "alt": ["tres", "tres días"], "why": "«He estado tres días en Valparaíso»"},
        {"q": "¿Cuántas fotos ha sacado? (en cifras)", "ans": "200",
         "alt": ["doscientas", "doscientas fotos"], "why": "«he sacado doscientas fotos»"},
        {"q": "¿Cuánto dura el viaje de Santiago a Valparaíso?", "ans": "cuatro horas",
         "alt": ["4 horas", "cuatro"], "why": "«Cuatro horas por la carretera de la costa»"},
        {"q": "¿Qué significa «micro» en Chile?", "ans": "el autobús",
         "alt": ["autobús", "autobus", "el bus", "bus"], "why": "«micro» (el autobús)"},
        {"q": "¿Adónde va Nina mañana?", "ans": "al sur, al lago Llanquihue",
         "alt": ["al sur", "el sur", "lago llanquihue", "llanquihue"],
         "why": "«Mañana vamos para el sur, al lago Llanquihue»"},
    ],
    "vf": [
        {"q": "Nina ya ha visto todos los murales.", "ans": False,
         "prueba": "todavía no he visto todos los murales"},
        {"q": "Nina ha perdido el autobús más de una vez.", "ans": True,
         "prueba": "he perdido el autobús dos veces"},
        {"q": "El miércoles Nina ha hecho una excursión larga.", "ans": False,
         "prueba": "hoy no he hecho nada especial"},
        {"q": "Nina ha aprendido palabras del español de Chile.", "ans": True,
         "prueba": "he aprendido dos palabras nuevas"},
        {"q": "Nina ya ha probado el pastel de choclo.", "ans": False,
         "prueba": "todavía no he probado el pastel de choclo"},
    ],
    "contexto": [
        {"q": "«un museo al aire libre» — ¿qué quiere decir Nina?",
         "opts": ["De kunst hangt buiten, op straat", "Het museum heeft geen dak nodig",
                  "Het museum is gratis"],
         "ans": "De kunst hangt buiten, op straat",
         "why": "Ze heeft het over de murales op de gevels."},
        {"q": "«Lo mejor ha sido el atardecer» — ¿qué expresa «lo mejor»?",
         "opts": ["het beste van alles", "de beste persoon", "de beste foto"],
         "ans": "het beste van alles",
         "why": "«lo + adjectief» maakt er een algemeen begrip van: het beste, het ergste."},
        {"q": "«todavía no he probado…» — ¿qué significa «todavía no»?",
         "opts": ["nog niet", "nooit meer", "meteen"], "ans": "nog niet",
         "why": "Het staat tegenover «ya» (al)."},
        {"q": "«P.D.» al final — ¿qué es?",
         "opts": ["een naschrift, iets wat ze nog snel toevoegt", "haar handtekening",
                  "het adres van de school"],
         "ans": "een naschrift, iets wat ze nog snel toevoegt",
         "why": "«posdata» = het Nederlandse P.S."},
    ],
    "produccion": {
        "prompt": "Escribe tu propia postal (5–6 frases) desde un viaje real o inventado: dónde "
                  "has estado, tres cosas que has hecho, lo mejor, lo peor y algo que todavía "
                  "no has hecho.",
        "modelo": "¡Hola! Te escribo desde… He estado… He visto… y he comido… Lo mejor ha "
                  "sido… Lo peor… Todavía no he…",
    },
}


# ---------------------------------------------------------------------------
# C5 · U5 «¡Ñam!» — parada México (CDMX)
# Tekstsoort: infografía. De unit heeft zelf al een menukaart en een mini-recept
# in §5; een tweede recept zou dezelfde leeshouding vragen. Een infografie doet
# iets anders: cijfers aflezen en ze in verband brengen met een lopende tekst.
# Het luisterfragment speelt aan tafel in een restaurant.
# ---------------------------------------------------------------------------
C5_U5 = {
    "id": "C5-U5-LEC-01",
    "ancla": "c5-u5-lec-01",
    "titulo": "El mercado de La Merced en cinco datos",
    "tipo": "infografía (datos + texto)",
    "emisor": "La revista de viajes «Sabores»",
    "receptor": "Quien visita Ciudad de México por primera vez",
    "objetivo": "Enseñarte de un vistazo cómo es el mercado más grande del país",
    "prediccion": {
        "q": "Kijk eerst alleen naar de vijf genummerde cijfers en de kop. Wat voor tekst is dit?",
        "opts": ["Een infografie met feiten over een markt", "Een recept", "Een menukaart"],
        "ans": "Een infografie met feiten over een markt",
        "why": "Genummerde cijfers met een korte uitleg erbij = feiten in beeld.",
    },
    "texto": [
        ["titulo", "🌽 EL MERCADO DE LA MERCED EN CINCO DATOS"],
        ["lema", "Ciudad de México · el mercado de comida más grande del país"],
        ["lista", [
            "1 · Ocupa cuatro edificios y más de tres mil puestos.",
            "2 · Abre todos los días a las seis de la mañana.",
            "3 · Aquí hay más de sesenta clases de chile.",
            "4 · Cada día entran unas ochenta mil personas.",
            "5 · El puesto más antiguo tiene más de cien años.",
        ]],
        ["p", "En el pasillo de la fruta hay pirámides de naranjas, piñas y plátanos. "
              "Los vendedores gritan los precios y te dan a probar un trozo: «¡Pruebe, pruebe!»"],
        ["p", "En la zona de comida preparada puedes comer por muy poco dinero. Un taco cuesta "
              "entre quince y veinticinco pesos. Con cien pesos comes muchísimo."],
        ["aviso", ["🌶️ EL CHILE · dato curioso",
                   "El chile habanero es el más picante del mercado. El poblano casi no pica. "
                   "Si eres nuevo, empieza con poco: aquí «un poquito» ya es mucho."]],
        ["p", "El mercado no es solo comida: es el lugar donde la ciudad se encuentra. "
              "Muchas familias compran aquí desde hace tres generaciones."],
        ["firma", "Datos: Gobierno de la Ciudad de México · Fotos: Diego"],
    ],
    "traduccion": "DE MARKT VAN LA MERCED IN VIJF CIJFERS. Mexico-Stad · de grootste "
                  "voedingsmarkt van het land. 1 · Ze beslaat vier gebouwen en meer dan "
                  "drieduizend kraampjes. 2 · Ze opent elke dag om zes uur \u2019s ochtends. "
                  "3 · Er zijn hier meer dan zestig soorten chilipeper. 4 · Elke dag komen er "
                  "zo\u2019n tachtigduizend mensen binnen. 5 · Het oudste kraam bestaat meer dan "
                  "honderd jaar. — In het fruitgangpad liggen piramides van sinaasappels, "
                  "ananassen en bananen. De verkopers roepen de prijzen en geven je een stukje "
                  "om te proeven: «Proef eens, proef eens!» In de zone met bereide gerechten kun "
                  "je voor heel weinig geld eten. Een taco kost tussen vijftien en vijfentwintig "
                  "peso. Met honderd peso eet je heel veel. DE CHILI: de habanero is de "
                  "pikantste van de markt. De poblano prikt bijna niet. Ben je nieuw, begin dan "
                  "met weinig: hier is «een beetje» al veel. — De markt is niet alleen eten: het "
                  "is de plek waar de stad elkaar tegenkomt. Veel families kopen hier al drie "
                  "generaties lang.",
    "global": {
        "q": "¿Qué tipo de texto es?",
        "opts": ["Una infografía con datos sobre un mercado", "Una receta de cocina",
                 "La carta de un restaurante"],
        "ans": "Una infografía con datos sobre un mercado",
    },
    "escanear": [
        {"q": "¿Cuántos puestos hay? (en cifras)", "ans": "3000",
         "alt": ["tres mil", "más de tres mil", "3.000", "3 000"], "why": "«más de tres mil puestos»"},
        {"q": "¿A qué hora abre el mercado?", "ans": "a las seis de la mañana",
         "alt": ["a las seis", "seis", "6", "las seis"], "why": "«a las seis de la mañana»"},
        {"q": "¿Cuántas personas entran cada día? (en cifras)", "ans": "80000",
         "alt": ["ochenta mil", "80.000", "80 000", "unas ochenta mil"],
         "why": "«unas ochenta mil personas»"},
        {"q": "¿Cuánto cuesta un taco?", "ans": "entre 15 y 25 pesos",
         "alt": ["15 y 25", "entre quince y veinticinco pesos", "quince y veinticinco"],
         "why": "«entre quince y veinticinco pesos»"},
        {"q": "¿Cuál es el chile más picante del mercado?", "ans": "el habanero",
         "alt": ["habanero", "el chile habanero"], "why": "«El chile habanero es el más picante»"},
    ],
    "vf": [
        {"q": "El mercado abre solo los fines de semana.", "ans": False,
         "prueba": "abre todos los días"},
        {"q": "Hay más de sesenta clases de chile.", "ans": True,
         "prueba": "más de sesenta clases de chile"},
        {"q": "Comer en el mercado es caro.", "ans": False,
         "prueba": "puedes comer por muy poco dinero"},
        {"q": "El chile poblano es muy picante.", "ans": False, "prueba": "el poblano casi no pica"},
        {"q": "El puesto más antiguo tiene más de cien años.", "ans": True,
         "prueba": "más de cien años"},
    ],
    "contexto": [
        {"q": "«los puestos» — ¿qué son?",
         "opts": ["de kraampjes", "de posities in een rij", "de brievenbussen"],
         "ans": "de kraampjes", "why": "Het staat naast «cuatro edificios» — het gaat over de markt."},
        {"q": "«te dan a probar un trozo» — ¿qué te ofrecen?",
         "opts": ["een stukje om te proeven", "een korting", "een zak"],
         "ans": "een stukje om te proeven", "why": "Erna volgt de roep «¡Pruebe, pruebe!»"},
        {"q": "«casi no pica» — ¿pica mucho o poco?",
         "opts": ["Bijna niet", "Heel erg", "Alleen als hij rood is"], "ans": "Bijna niet",
         "why": "Het staat tegenover «el más picante»."},
        {"q": "«el lugar donde la ciudad se encuentra» — ¿qué quiere decir?",
         "opts": ["De plek waar iedereen elkaar tegenkomt", "De plek waar de stad ligt",
                  "De plek waar je iets verliest"],
         "ans": "De plek waar iedereen elkaar tegenkomt",
         "why": "Erna volgt: families die er al drie generaties komen."},
    ],
    "produccion": {
        "prompt": "Escribe cinco datos sobre un mercado o un supermercado de tu ciudad "
                  "(5–6 frases): cuándo abre, qué hay, qué cuesta poco, qué cuesta mucho y "
                  "qué compras tú allí. Usa mucho/mucha/muchos/poco.",
        "modelo": "1 · Abre… 2 · Hay muchos… y poca… 3 · Un/Una … cuesta… 4 · Lo más caro es… "
                  "5 · Yo compro… porque…",
    },
}


# ---------------------------------------------------------------------------
# C6+ · U5 «Érase una vez» — parada Buenos Aires
# Tekstsoort: leyenda. Nieuw genre en precies het genre waar het indefinido thuis
# is: een verhaal met een keten van gebeurtenissen. Bewust een traditionele
# leyenda en geen biografie van een echte persoon — echte figuren horen in
# Cultura (CLAUDE.md §12). Het luisterfragment is een rondleiding in een museum.
# Let op: het imperfecto komt pas in U6, dus het verhaal staat volledig in het
# indefinido, met de tegenwoordige tijd voor de omkadering.
# ---------------------------------------------------------------------------
C6P_U5 = {
    "id": "C6P-U5-LEC-01",
    "ancla": "c6p-u5-lec-01",
    "titulo": "La leyenda de la yerba mate",
    "tipo": "leyenda guaraní",
    "emisor": "La tradición oral guaraní, recogida por escrito",
    "receptor": "Quien quiere saber de dónde viene el mate",
    "objetivo": "Explicar el origen de una planta y de una costumbre",
    "prediccion": {
        "q": "Kijk eerst alleen naar de titel, de aanhef «Érase una vez» en het slot. "
             "Wat voor tekst is dit?",
        "opts": ["Een oude vertelling die iets verklaart", "Een nieuwsbericht",
                 "Een gebruiksaanwijzing"],
        "ans": "Een oude vertelling die iets verklaart",
        "why": "«Érase una vez» is de vaste opening van een verhaal.",
    },
    "texto": [
        ["titulo", "🌿 LA LEYENDA DE LA YERBA MATE"],
        ["lema", "Un relato guaraní · Argentina y Paraguay"],
        ["p", "Érase una vez, en el monte, un viejo cazador y su hija. Un día, todos los "
              "vecinos se fueron a buscar tierras nuevas, pero el cazador no quiso dejar solo "
              "el monte y se quedó allí con la niña."],
        ["p", "Una tarde, Yasí, la luna, bajó del cielo con su amiga Araí, la nube. Las dos "
              "tomaron forma de mujer y caminaron por el monte para ver de cerca aquel lugar."],
        ["p", "De repente, un yaguareté salió de entre los árboles. El viejo cazador oyó el "
              "ruido, corrió hacia las dos mujeres y las salvó. Después volvió a su casa y no "
              "dijo nada a nadie."],
        ["aviso", ["🌙 EL REGALO DE YASÍ",
                   "Esa noche, Yasí entró en el sueño del cazador y le habló: «Nos salvaste la "
                   "vida y no pediste nada. Por eso te dejo una planta nueva. Sus hojas dan una "
                   "bebida que une a las personas.»"]],
        ["p", "A la mañana siguiente, el cazador y su hija encontraron delante de la casa un "
              "árbol pequeño de hojas verdes. Prepararon la primera infusión y la compartieron "
              "con todos los que pasaron por allí."],
        ["p", "Por eso, hasta hoy, el mate no se toma solo: se pasa de mano en mano. "
              "Compartirlo es el regalo, no la bebida."],
        ["firma", "Relato tradicional guaraní · versión escolar"],
    ],
    "traduccion": "DE LEGENDE VAN DE YERBA MATE — een Guaraní-verhaal uit Argentinië en "
                  "Paraguay. Er was eens, in het bos, een oude jager en zijn dochter. Op een dag "
                  "trokken alle buren weg om nieuw land te zoeken, maar de jager wilde het bos "
                  "niet alleen laten en bleef er met het meisje. Op een namiddag daalde Yasí, de "
                  "maan, uit de hemel af met haar vriendin Araí, de wolk. De twee namen de "
                  "gedaante van een vrouw aan en liepen door het bos om die plek van dichtbij te "
                  "zien. Plots kwam er een jaguar tussen de bomen vandaan. De oude jager hoorde "
                  "het geluid, liep naar de twee vrouwen toe en redde hen. Daarna ging hij naar "
                  "huis en zei niets tegen niemand. HET GESCHENK VAN YASÍ: die nacht kwam Yasí "
                  "in de droom van de jager en sprak hem toe: «Je hebt ons leven gered en je hebt "
                  "niets gevraagd. Daarom laat ik je een nieuwe plant. Haar bladeren geven een "
                  "drank die mensen verbindt.» De volgende ochtend vonden de jager en zijn "
                  "dochter voor het huis een kleine boom met groene bladeren. Ze zetten het "
                  "eerste aftreksel en deelden het met iedereen die voorbijkwam. Daarom wordt de "
                  "mate tot vandaag niet alleen gedronken: hij gaat van hand tot hand. Het delen "
                  "is het geschenk, niet de drank.",
    "global": {
        "q": "¿Qué explica esta leyenda?",
        "opts": ["De dónde viene la yerba mate y por qué se comparte",
                 "Cómo se cultiva la yerba mate hoy",
                 "Por qué los guaraníes se fueron del monte"],
        "ans": "De dónde viene la yerba mate y por qué se comparte",
    },
    "escanear": [
        {"q": "¿Con quién vive el cazador?", "ans": "con su hija",
         "alt": ["su hija", "la niña", "con la niña", "hija"], "why": "«un viejo cazador y su hija»"},
        {"q": "¿Quién es Yasí?", "ans": "la luna", "alt": ["luna", "la luna"],
         "why": "«Yasí, la luna»"},
        {"q": "¿Quién es Araí?", "ans": "la nube", "alt": ["nube", "la nube"], "why": "«Araí, la nube»"},
        {"q": "¿Qué animal aparece de repente?", "ans": "un yaguareté",
         "alt": ["yaguareté", "yaguarete", "un jaguar", "jaguar"],
         "why": "«un yaguareté salió de entre los árboles»"},
        {"q": "¿Cuándo encontraron el árbol?", "ans": "a la mañana siguiente",
         "alt": ["la mañana siguiente", "al día siguiente", "por la mañana"],
         "why": "«A la mañana siguiente… encontraron… un árbol pequeño»"},
    ],
    "vf": [
        {"q": "El cazador se fue con los vecinos.", "ans": False, "prueba": "se quedó allí con la niña"},
        {"q": "El cazador contó a todo el mundo lo que pasó.", "ans": False,
         "prueba": "no dijo nada a nadie"},
        {"q": "Yasí le habló al cazador mientras dormía.", "ans": True,
         "prueba": "yasí entró en el sueño del cazador"},
        {"q": "El cazador pidió un regalo.", "ans": False, "prueba": "no pediste nada"},
        {"q": "Compartieron la primera infusión con otras personas.", "ans": True,
         "prueba": "la compartieron con todos los que pasaron"},
    ],
    "contexto": [
        {"q": "«Érase una vez» — ¿cómo empieza este texto?",
         "opts": ["Als een verhaal uit de oude doos", "Als een krantenbericht",
                  "Als een uitnodiging"],
         "ans": "Als een verhaal uit de oude doos",
         "why": "Het is de vaste openingsformule, zoals ons «Er was eens»."},
        {"q": "«tomaron forma de mujer» — ¿qué hicieron la luna y la nube?",
         "opts": ["Ze veranderden in vrouwen", "Ze namen een foto", "Ze gaven iets weg"],
         "ans": "Ze veranderden in vrouwen",
         "why": "Erna lopen ze door het bos — ze hebben een lichaam gekregen."},
        {"q": "«De repente» — ¿cómo pasó?",
         "opts": ["plots, onverwacht", "langzaam", "elke dag opnieuw"], "ans": "plots, onverwacht",
         "why": "Het markeert de omslag in het verhaal."},
        {"q": "«se pasa de mano en mano» — ¿qué hacen con el mate?",
         "opts": ["Ze geven hem aan elkaar door", "Ze verkopen hem", "Ze verbergen hem"],
         "ans": "Ze geven hem aan elkaar door",
         "why": "De laatste zin legt het uit: het delen is het geschenk."},
    ],
    "produccion": {
        "prompt": "Escribe una leyenda corta (6–8 frases) que explique el origen de algo de tu "
                  "región (una fiesta, una comida, un río, un nombre). Usa el indefinido y los "
                  "conectores: érase una vez · un día · de repente · entonces · por eso.",
        "modelo": "Érase una vez… Un día… De repente… Entonces… Al final… Por eso, hasta hoy…",
    },
}


# ---------------------------------------------------------------------------
# C5 · U6 «De tiendas» — parada México (los mercados)
# Tekstsoort: artículo de consejos (listicle) uit een jeugdblad. Nieuw genre:
# genummerde tips die de leerling moet wégen — welke tip past bij mij? — in
# plaats van gegevens opzoeken. De tips staan bewust met «hay que», «es mejor»
# en «puedes» + infinitivo: de imperativo komt pas in U7.
# Het luisterfragment speelt in het pashokje: meningen, geen transactie.
# ---------------------------------------------------------------------------
C5_U6 = {
    "id": "C5-U6-LEC-01",
    "ancla": "c5-u6-lec-01",
    "titulo": "Cinco trucos para ir de rebajas",
    "tipo": "artículo de consejos (revista juvenil)",
    "emisor": "La revista «Joven y Listo»",
    "receptor": "Jóvenes que van de compras con poco dinero",
    "objetivo": "Que gastes menos y compres mejor",
    "prediccion": {
        "q": "Kijk eerst alleen naar de titel en de vijf nummers. Wat gaat deze tekst doen?",
        "opts": ["Tips geven", "Iets verkopen", "Een verhaal vertellen"],
        "ans": "Tips geven",
        "why": "«Cinco trucos» + genummerde punten = advies.",
    },
    "texto": [
        ["titulo", "🛍️ CINCO TRUCOS PARA IR DE REBAJAS"],
        ["lema", "Sin gastar de más · Joven y Listo · enero"],
        ["p", "Llegan las rebajas y todo parece barato. Pero atención: no todo lo que está "
              "rebajado es una buena compra. Estos cinco trucos funcionan."],
        ["lista", [
            "1 · Hay que mirar la etiqueta vieja. Si el precio antiguo no está, el descuento "
            "no es real.",
            "2 · Es mejor no comprar el primer día. Las tiendas bajan más los precios en la "
            "segunda semana.",
            "3 · Puedes probarte la ropa siempre, también en rebajas. Una talla no es igual "
            "en todas las tiendas.",
            "4 · Hay que llevar una lista. Con lista gastas menos; sin lista compras cosas "
            "que no usas.",
            "5 · Es mejor pagar en efectivo. Con tarjeta no ves el dinero y gastas más.",
        ]],
        ["aviso", ["♻️ UN TRUCO EXTRA: LA SEGUNDA MANO",
                   "En el mercadillo y en las tiendas de segunda mano hay ropa buena y barata. "
                   "Además es moda sostenible: una camiseta usada no gasta agua nueva."]],
        ["p", "Y el truco más importante: si una prenda no te queda bien en la tienda, tampoco "
              "te va a quedar bien en casa. Ese vestido barato que no te pones nunca es el más "
              "caro de tu armario."],
        ["firma", "¿Tienes otro truco? Escríbenos a trucos@jovenylisto.es"],
    ],
    "traduccion": "VIJF TRUCS VOOR DE SOLDEN — zonder te veel uit te geven. De solden komen "
                  "eraan en alles lijkt goedkoop. Maar opgelet: niet alles wat afgeprijsd is, is "
                  "een goede aankoop. Deze vijf trucs werken. 1 · Je moet naar het oude "
                  "prijskaartje kijken. Staat de oude prijs er niet, dan is de korting niet echt. "
                  "2 · Koop beter niet de eerste dag. Winkels verlagen de prijzen meer in de "
                  "tweede week. 3 · Je mag altijd passen, ook in de solden. Een maat is niet in "
                  "elke winkel hetzelfde. 4 · Je moet een lijstje meenemen. Met een lijstje geef "
                  "je minder uit; zonder lijstje koop je dingen die je niet gebruikt. 5 · Betaal "
                  "beter cash. Met de kaart zie je het geld niet en geef je meer uit. EXTRA TRUC: "
                  "TWEEDEHANDS — op de rommelmarkt en in tweedehandswinkels vind je goede en "
                  "goedkope kleren. Bovendien is het duurzame mode: een gedragen T-shirt "
                  "verbruikt geen nieuw water. En de belangrijkste truc: als een kledingstuk je "
                  "in de winkel niet goed staat, zal het je thuis ook niet goed staan. Dat "
                  "goedkope kleedje dat je nooit draagt, is het duurste van je kast.",
    "global": {
        "q": "¿Para qué es este artículo?",
        "opts": ["Para ayudarte a comprar mejor y gastar menos",
                 "Para presentar la moda de este año",
                 "Para explicar dónde están las tiendas"],
        "ans": "Para ayudarte a comprar mejor y gastar menos",
    },
    "escanear": [
        {"q": "¿Cuántos trucos da el artículo? (en cifras)", "ans": "5",
         "alt": ["cinco", "5 trucos"], "why": "«CINCO TRUCOS PARA IR DE REBAJAS»"},
        {"q": "¿En qué semana bajan más los precios?", "ans": "en la segunda",
         "alt": ["la segunda", "segunda", "la segunda semana", "2"],
         "why": "«bajan más los precios en la segunda semana»"},
        {"q": "¿Qué hay que llevar a la tienda?", "ans": "una lista",
         "alt": ["lista", "una lista de la compra"], "why": "«Hay que llevar una lista»"},
        {"q": "¿Cómo es mejor pagar?", "ans": "en efectivo",
         "alt": ["efectivo", "con dinero", "en cash"], "why": "«Es mejor pagar en efectivo»"},
        {"q": "¿Dónde hay ropa buena y barata según el recuadro?", "ans": "en el mercadillo y en las tiendas de segunda mano",
         "alt": ["el mercadillo", "mercadillo", "segunda mano", "tiendas de segunda mano"],
         "why": "«En el mercadillo y en las tiendas de segunda mano»"},
    ],
    "vf": [
        {"q": "Todo lo que está rebajado es una buena compra.", "ans": False,
         "prueba": "no todo lo que está rebajado es una buena compra"},
        {"q": "En rebajas no puedes probarte la ropa.", "ans": False,
         "prueba": "puedes probarte la ropa siempre, también en rebajas"},
        {"q": "Con tarjeta la gente gasta más.", "ans": True,
         "prueba": "con tarjeta no ves el dinero y gastas más"},
        {"q": "La ropa de segunda mano es cara.", "ans": False,
         "prueba": "hay ropa buena y barata"},
        {"q": "Una talla es igual en todas las tiendas.", "ans": False,
         "prueba": "una talla no es igual en todas las tiendas"},
    ],
    "contexto": [
        {"q": "«la etiqueta vieja» — ¿para qué sirve mirarla?",
         "opts": ["Om te zien of de korting echt is", "Om de maat te vinden",
                  "Om te weten van welke stof het is"],
         "ans": "Om te zien of de korting echt is",
         "why": "Er staat: zonder de oude prijs is de korting niet echt."},
        {"q": "«no te queda bien» — ¿qué quiere decir?",
         "opts": ["Het staat je niet", "Het blijft niet liggen", "Het is niet meer over"],
         "ans": "Het staat je niet",
         "why": "«quedar bien» over kleding = goed staan."},
        {"q": "«moda sostenible» — ¿qué es?",
         "opts": ["mode die het milieu spaart", "dure merkkleding", "mode die lang meegaat in de kast"],
         "ans": "mode die het milieu spaart",
         "why": "Het kader legt het uit: geen nieuw water."},
        {"q": "«es el más caro de tu armario» — ¿por qué lo dice?",
         "opts": ["Omdat je het nooit draagt, is elke euro weggegooid",
                  "Omdat het uit een dure winkel komt",
                  "Omdat het veel plaats inneemt"],
         "ans": "Omdat je het nooit draagt, is elke euro weggegooid",
         "why": "Het gaat over «ese vestido barato que no te pones nunca»."},
    ],
    "produccion": {
        "prompt": "Escribe tus propios tres trucos para comprar ropa (5–6 frases). Usa: hay que "
                  "+ infinitivo · es mejor + infinitivo · puedes + infinitivo. Añade un truco "
                  "sobre la ropa de segunda mano.",
        "modelo": "1 · Hay que… 2 · Es mejor no… 3 · Puedes… Y un truco extra: en el mercadillo…",
    },
}


# ---------------------------------------------------------------------------
# C6+ · U6 «Cuando era pequeño» — parada Cusco
# Tekstsoort: carta de una abuela. Nieuw genre: een handgeschreven brief van de
# oudere generatie aan de jongere. Precies de plaats van het imperfecto (hoe het
# vroeger wás) náást het indefinido (wat er één keer gebeurde), en het levert het
# «antes ↔ ahora»-contrast vanzelf. Het luisterfragment is een podcast.
# ---------------------------------------------------------------------------
C6P_U6 = {
    "id": "C6P-U6-LEC-01",
    "ancla": "c6p-u6-lec-01",
    "titulo": "Carta de la abuela Rosario",
    "tipo": "carta manuscrita (de la abuela a su nieta)",
    "emisor": "Rosario, 79 años, desde un pueblo cerca de Cusco",
    "receptor": "Su nieta, que vive en la ciudad",
    "objetivo": "Contarle cómo era su infancia y compararla con la de ahora",
    "prediccion": {
        "q": "Kijk eerst alleen naar de aanhef «Querida nieta», de plaats en de "
             "handtekening. Wat voor tekst is dit?",
        "opts": ["Een persoonlijke brief", "Een schoolopstel", "Een reclamefolder"],
        "ans": "Een persoonlijke brief",
        "why": "Aanhef + groet + handtekening = een brief aan één iemand.",
    },
    "texto": [
        ["titulo", "✉️ QUERIDA NIETA"],
        ["lema", "Ollantaytambo, cerca de Cusco · 12 de mayo"],
        ["p", "Me preguntas cómo era mi vida de pequeña. Pues mira: yo vivía en esta misma "
              "casa, pero todo era diferente. No había electricidad ni agua caliente. "
              "Nos levantábamos a las cinco y caminábamos una hora hasta la escuela."],
        ["p", "Éramos ocho hermanos. Mi madre cocinaba en el suelo, con leña, y siempre había "
              "sopa. Yo no tenía juguetes: jugaba con piedras y con una muñeca de trapo que "
              "me hizo mi tía."],
        ["aviso", ["📅 EL DÍA QUE TODO CAMBIÓ",
                   "En mil novecientos sesenta llegó la carretera. Un camión subió hasta la "
                   "plaza y todo el pueblo salió a mirar. Yo tenía catorce años. Aquel día vi "
                   "mi primera radio."]],
        ["p", "Ahora tú tienes internet, agua caliente y un colegio a diez minutos. Vives "
              "mejor que yo, eso está claro. Pero antes el pueblo era más tranquilo y todos "
              "nos conocíamos."],
        ["p", "Antes no era mejor. Era diferente. Lo que echo de menos no son las piedras: "
              "es la plaza llena de gente al atardecer."],
        ["firma", "Te espero en julio. Un beso enorme de tu abuela Rosario."],
    ],
    "traduccion": "LIEVE KLEINDOCHTER — Ollantaytambo, bij Cusco, 12 mei. Je vraagt me hoe mijn "
                  "leven als kind was. Kijk: ik woonde in ditzelfde huis, maar alles was anders. "
                  "Er was geen elektriciteit en geen warm water. We stonden om vijf uur op en "
                  "liepen een uur naar school. We waren met acht kinderen. Mijn moeder kookte op "
                  "de grond, op hout, en er was altijd soep. Ik had geen speelgoed: ik speelde "
                  "met steentjes en met een lappenpop die mijn tante voor me maakte. DE DAG DAT "
                  "ALLES VERANDERDE: in 1960 kwam de weg. Een vrachtwagen reed tot op het plein "
                  "en het hele dorp liep buiten om te kijken. Ik was veertien. Die dag zag ik "
                  "mijn eerste radio. — Nu heb jij internet, warm water en een school op tien "
                  "minuten. Jij leeft beter dan ik, dat is duidelijk. Maar vroeger was het dorp "
                  "rustiger en kenden we elkaar allemaal. Vroeger was niet beter. Het "
                  "was anders. Wat ik mis zijn niet de steentjes: het "
                  "is het plein vol mensen bij zonsondergang. Ik verwacht je in juli. Een dikke "
                  "kus van je oma Rosario.",
    "global": {
        "q": "¿De qué habla la abuela en su carta?",
        "opts": ["De cómo era su infancia y en qué se diferencia de la de ahora",
                 "De un viaje que quiere hacer", "De una fiesta del pueblo"],
        "ans": "De cómo era su infancia y en qué se diferencia de la de ahora",
    },
    "escanear": [
        {"q": "¿A qué hora se levantaban?", "ans": "a las cinco",
         "alt": ["las cinco", "cinco", "5"], "why": "«Nos levantábamos a las cinco»"},
        {"q": "¿Cuánto tiempo caminaban hasta la escuela?", "ans": "una hora",
         "alt": ["1 hora", "hora", "una"], "why": "«caminábamos una hora hasta la escuela»"},
        {"q": "¿Cuántos hermanos eran? (en cifras)", "ans": "8",
         "alt": ["ocho", "ocho hermanos"], "why": "«Éramos ocho hermanos»"},
        {"q": "¿En qué año llegó la carretera? (en cifras)", "ans": "1960",
         "alt": ["mil novecientos sesenta", "en 1960"], "why": "«En mil novecientos sesenta llegó la carretera»"},
        {"q": "¿Cuántos años tenía la abuela ese día? (en cifras)", "ans": "14",
         "alt": ["catorce", "catorce años"], "why": "«Yo tenía catorce años»"},
    ],
    "vf": [
        {"q": "En la casa había agua caliente.", "ans": False,
         "prueba": "no había electricidad ni agua caliente"},
        {"q": "La abuela tenía muchos juguetes.", "ans": False, "prueba": "yo no tenía juguetes"},
        {"q": "Su tía le hizo una muñeca.", "ans": True, "prueba": "una muñeca de trapo que me hizo mi tía"},
        {"q": "La abuela piensa que la vida de su nieta es más fácil.", "ans": True,
         "prueba": "vives mejor que yo"},
        {"q": "La abuela echa de menos las piedras.", "ans": False,
         "prueba": "lo que echo de menos no son las piedras"},
    ],
    "contexto": [
        {"q": "«con leña» — ¿con qué cocinaba su madre?",
         "opts": ["met hout", "met gas", "met elektriciteit"], "ans": "met hout",
         "why": "Er stond net dat er geen elektriciteit was."},
        {"q": "«una muñeca de trapo» — ¿de qué es?",
         "opts": ["van stof, zelfgemaakt", "van plastic", "van hout"],
         "ans": "van stof, zelfgemaakt", "why": "Haar tante maakte ze; er was geen speelgoed te koop."},
        {"q": "«echar de menos» — ¿qué hace la abuela?",
         "opts": ["Ze mist iets", "Ze gooit iets weg", "Ze telt iets"], "ans": "Ze mist iets",
         "why": "Vaste uitdrukking — één van de lastigste voor Nederlandstaligen."},
        {"q": "«Antes no era mejor. Era diferente.» — ¿qué hace aquí la abuela?",
         "opts": ["Ze nuanceert wat ze net zei", "Ze spreekt zichzelf tegen",
                  "Ze stelt een vraag"],
         "ans": "Ze nuanceert wat ze net zei",
         "why": "Ze zwakt «vroeger was alles beter» bewust af tot «anders»."},
    ],
    "produccion": {
        "prompt": "Contesta a la abuela (6–8 frases): cómo es tu vida ahora, qué hacías tú de "
                  "pequeño/-a, qué cambió y qué echas de menos. Usa el imperfecto para el "
                  "decorado, el indefinido para lo que pasó una vez, y una comparación "
                  "(más/menos… que · tan… como).",
        "modelo": "Querida abuela: ahora yo… De pequeño/-a yo… y siempre… Un día… Ahora mi vida "
                  "es más… que antes, pero echo de menos…",
    },
}


# ---------------------------------------------------------------------------
# C5 · U7 «Mi casa y mi barrio» — parada Cartagena
# Tekstsoort: anuncio de alquiler con plano. Nieuw genre: een advertentie mét
# een plattegrondbeschrijving, dus de leerling moet lezen én in zijn hoofd iets
# tekenen. Dat is precies wat hay/estar + preposiciones vragen.
# Het luisterfragment is een omroepbericht in de metro — luisteren zonder beeld.
# ---------------------------------------------------------------------------
C5_U7 = {
    "id": "C5-U7-LEC-01",
    "ancla": "c5-u7-lec-01",
    "titulo": "Se alquila apartamento en el centro",
    "tipo": "anuncio de alquiler (con descripción del plano)",
    "emisor": "La agencia «Casas del Caribe», Cartagena",
    "receptor": "Estudiantes que buscan piso",
    "objetivo": "Que te imagines el piso y lo vengas a ver",
    "prediccion": {
        "q": "Kijk eerst alleen naar de prijs, de m² en de opsomming. Wat voor tekst is dit?",
        "opts": ["Een advertentie voor een huurwoning", "Een reisverslag", "Een rekening"],
        "ans": "Een advertentie voor een huurwoning",
        "why": "Prijs + oppervlakte + kamers = een verhuuradvertentie.",
    },
    "texto": [
        ["titulo", "🏠 SE ALQUILA · APARTAMENTO EN GETSEMANÍ"],
        ["lema", "Cartagena de Indias · 62 m² · 900.000 pesos al mes"],
        ["lista", [
            "Segundo piso, sin ascensor",
            "Dos dormitorios y un baño",
            "Salón con balcón a la calle",
            "Cocina pequeña, nevera incluida",
            "Wifi y agua incluidos; luz aparte",
        ]],
        ["p", "El apartamento está en la calle del Pozo, en el barrio de Getsemaní. "
              "Cuando entras, el pasillo está delante de ti. La cocina está a la derecha y "
              "el baño, al lado de la cocina."],
        ["p", "Los dos dormitorios están al final del pasillo, uno enfrente del otro. "
              "En el dormitorio grande hay un armario empotrado y una cama de matrimonio. "
              "En el pequeño solo hay una cama y una estantería."],
        ["p", "El salón está a la izquierda de la entrada. Debajo de la ventana hay un sofá "
              "azul, y encima de la mesa dejamos una lámpara. El balcón da a la calle: "
              "por la noche se oye música."],
        ["aviso", ["📍 EL BARRIO",
                   "Getsemaní está muy cerca del centro histórico: a diez minutos a pie. "
                   "En la esquina hay una panadería y, dos calles más allá, un supermercado. "
                   "La parada del bus está enfrente de la iglesia."]],
        ["firma", "Visitas: de lunes a viernes, de 9 a 12. Escribe a casas@delcaribe.co"],
    ],
    "traduccion": "TE HUUR · APPARTEMENT IN GETSEMANÍ. Cartagena de Indias · 62 m² · 900.000 "
                  "peso per maand. Tweede verdieping, zonder lift · twee slaapkamers en één "
                  "badkamer · woonkamer met balkon aan de straat · kleine keuken, koelkast "
                  "inbegrepen · wifi en water inbegrepen, elektriciteit apart. Het appartement "
                  "ligt in de calle del Pozo, in de wijk Getsemaní. Als je binnenkomt, ligt de "
                  "gang recht voor je. De keuken is rechts en de badkamer ligt naast de keuken. "
                  "De twee slaapkamers liggen aan het einde van de gang, tegenover elkaar. In de "
                  "grote slaapkamer staat een ingebouwde kast en een tweepersoonsbed. In de "
                  "kleine staat alleen een bed en een boekenrek. De woonkamer is links van de "
                  "ingang. Onder het raam staat een blauwe zetel, en op de tafel laten we een "
                  "lamp staan. Het balkon geeft uit op de straat: 's nachts hoor je muziek. DE "
                  "WIJK: Getsemaní ligt heel dicht bij het historische centrum, op tien minuten "
                  "te voet. Op de hoek is een bakkerij en twee straten verder een supermarkt. De "
                  "bushalte ligt tegenover de kerk.",
    "global": {
        "q": "¿Para qué es este texto?",
        "opts": ["Para alquilar un apartamento", "Para vender muebles",
                 "Para explicar la historia del barrio"],
        "ans": "Para alquilar un apartamento",
    },
    "escanear": [
        {"q": "¿Cuántos metros cuadrados tiene? (en cifras)", "ans": "62",
         "alt": ["62 m2", "62 m²", "sesenta y dos"], "why": "«62 m²»"},
        {"q": "¿En qué piso está?", "ans": "en el segundo",
         "alt": ["segundo", "el segundo", "2", "segundo piso"], "why": "«Segundo piso, sin ascensor»"},
        {"q": "¿Cuántos dormitorios hay? (en cifras)", "ans": "2",
         "alt": ["dos", "dos dormitorios"], "why": "«Dos dormitorios y un baño»"},
        {"q": "¿Qué hay debajo de la ventana del salón?", "ans": "un sofá azul",
         "alt": ["un sofá", "sofá", "el sofá azul"], "why": "«Debajo de la ventana hay un sofá azul»"},
        {"q": "¿Dónde está la parada del bus?", "ans": "enfrente de la iglesia",
         "alt": ["enfrente de la iglesia", "la iglesia", "frente a la iglesia"],
         "why": "«La parada del bus está enfrente de la iglesia»"},
    ],
    "vf": [
        {"q": "El edificio tiene ascensor.", "ans": False, "prueba": "segundo piso, sin ascensor"},
        {"q": "La luz está incluida en el precio.", "ans": False, "prueba": "luz aparte"},
        {"q": "El baño está al lado de la cocina.", "ans": True, "prueba": "al lado de la cocina"},
        {"q": "Los dos dormitorios están uno al lado del otro.", "ans": False,
         "prueba": "uno enfrente del otro"},
        {"q": "El centro histórico está a diez minutos andando.", "ans": True,
         "prueba": "a diez minutos a pie"},
    ],
    "contexto": [
        {"q": "«Se alquila» — ¿qué se hace con el apartamento?",
         "opts": ["Het wordt verhuurd", "Het wordt verkocht", "Het wordt afgebroken"],
         "ans": "Het wordt verhuurd",
         "why": "Erna volgt een maandprijs, geen totaalprijs."},
        {"q": "«un armario empotrado» — ¿qué tipo de armario es?",
         "opts": ["een ingebouwde kast", "een kapotte kast", "een kast op wieltjes"],
         "ans": "een ingebouwde kast",
         "why": "Het staat in de lijst van wat vást in de kamer zit."},
        {"q": "«El balcón da a la calle» — ¿qué quiere decir «dar a»?",
         "opts": ["uitkijken op", "iets geven aan", "geven om"], "ans": "uitkijken op",
         "why": "Erna volgt: 's nachts hoor je muziek van beneden."},
        {"q": "«dos calles más allá» — ¿dónde está el supermercado?",
         "opts": ["twee straten verder", "twee verdiepingen hoger", "twee minuten geleden"],
         "ans": "twee straten verder",
         "why": "Het staat tegenover «en la esquina» — het gaat over afstand."},
    ],
    "produccion": {
        "prompt": "Escribe el anuncio de tu propia casa o habitación (6–8 frases): dónde está, "
                  "cuántas habitaciones hay, dónde está cada mueble (encima de · debajo de · al "
                  "lado de · enfrente de) y qué hay en el barrio.",
        "modelo": "Se alquila… Está en… Hay… El/La … está … de … En el barrio hay… "
                  "La parada está…",
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
