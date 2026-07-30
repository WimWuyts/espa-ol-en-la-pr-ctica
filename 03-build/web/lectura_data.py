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


TODOS = {("C5", 0): C5_U0, ("C6+", 0): C6P_U0,
         ("C5", 1): C5_U1, ("C6+", 1): C6P_U1}


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
