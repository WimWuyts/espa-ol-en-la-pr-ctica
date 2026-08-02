#!/usr/bin/env python3
"""Externe bronnen per unit — de inhoud van het tabblad «Extra».

Tot nu toe stond daar «de leerkracht vult de links aan» en «link volgt». Dat is
precies het soort meta-tekst dat CLAUDE.md §18 uit de leerlingeneditie verbant:
ofwel de links staan er, ofwel het kader verdwijnt.

De lijst is door de auteur aangeleverd en per onderwerp geordend, in dezelfde
volgorde als de unit zelf: eerst het taalsysteem (§1–§4), dan de woordenschat-
clusters. Eén bron kan bij meerdere onderwerpen horen — dat is geen fout maar
een gevolg van hoe de bronsites hun oefeningen bundelen (een pagina over
persoonlijke informatie dekt zowel *presentarse* als *la edad*).

Structuur:  BRONNEN[(cursus, unit)] = [ (onderwerp, [ (bron, titel, url), … ]), … ]
Een `url` die op youtube.com wijst wordt automatisch als video herkend.
"""

# Vaste herkenningskleur/afkorting per bronsite.
SITES = {
    "ProfeDeELE":       ("PDE", "🎬"),
    "Arche-ELE":        ("ARE", "🧩"),
    "My Daily Spanish": ("MDS", "📺"),
    # mas.profedeele.es is de downloadafdeling van ProfeDeELE: pdf's en het
    # A1-handboek in plaats van online-oefeningen. Eigen badge, want voor de
    # leerling is het verschil merkbaar — hier moet hij iets openen of afdrukken.
    "Más ProfeDeELE":   ("MPD", "📄"),
}

BRONNEN = {}

# ── Uitgelichte spellen: tijdelijk UIT (auteur 2026-08-02) ────────────────────
# De spelsite leverde nog niet wat ze belooft, dus voorlopig verschijnt er in de
# hubs géén verwijzing naar chatgpt.site. De adressen en titels blijven hieronder
# staan — ze zijn door de auteur bevestigd en het zou zonde zijn ze weg te
# gooien. Zet deze schakelaar op True zodra de site wél levert; er hoeft verder
# niets aan de code te veranderen, enkel de hubs opnieuw bouwen.
TOON_DESTACADO = False

DESTACADO = {
    # Uitgelicht materiaal dat de héle unidad bestrijkt en dus niet onder één
    # onderwerp thuishoort. Staat bovenaan het tabblad, vóór de themalijsten.
    #
    # Per unit een LIJST: sinds 2026-08-02 levert de auteur meerdere spellen per
    # unidad aan, elk met een eigen adres op c5-ruta-digital. Eén spel blijft
    # gewoon een lijst van één.
    #
    # ── Over de titels ────────────────────────────────────────────────────────
    # De C5-titels zijn door de auteur bevestigd (2026-08-02, uit het overzicht
    # van de spelsite zelf) en staan hier letterlijk zoals daar, hoofdletters
    # inbegrepen. Niet «verbeteren»: «BCN Ahora» en «Mercado Nocturno CDMX»
    # horen zo.
    # De pagina's kunnen vanuit deze omgeving niet ingekeken worden
    # (chatgpt.site geeft 403), dus de omschrijvingen eronder komen uit de
    # leerstof van de unidad, niet van de pagina.
    ("C5", 0): [
        {
            "titel": "El Museo de las Palabras Perdidas",
            "soort": "Escape room",
            "ico": "🗝️",
            "url": "https://c5-ruta-digital.wim-wuyts1979.chatgpt.site/u0/museo",
            "es": "Un museo ha perdido sus palabras. Solo sales si superas las pruebas: "
                  "los sonidos, la tilde, los números, el género y los saludos.",
            "nl": "Een museum is zijn woorden kwijt. Je raakt er alleen uit door de proeven te "
                  "doorstaan: de klanken, de tilde, de getallen, het geslacht en de saludos.",
        },
        {
            "titel": "Archivo Cero",
            "soort": "Juego",
            "ico": "🎮",
            "url": "https://c5-ruta-digital.wim-wuyts1979.chatgpt.site/u0/archivo-cero",
            "es": "El archivo del principio: el alfabeto, los sonidos difíciles, los números y "
                  "las primeras palabras de clase.",
            "nl": "Het archief van het begin: het alfabet, de moeilijke klanken, de getallen en "
                  "de eerste klaswoorden.",
        },
    ],
    ("C5", 1): [
        {
            "titel": "Línea 0 · Kilómetro Cero",
            "soort": "Escape room",
            "ico": "🗝️",
            "url": "https://c5-ruta-digital.wim-wuyts1979.chatgpt.site/u1/linea-cero",
            "es": "Estás en el metro de Madrid, en una línea que no existe en el plano. Para "
                  "volver a la superficie tienes que conjugar en presente, decidir entre ser y "
                  "tener, hacer las preguntas correctas y saber de dónde es cada pasajero.",
            "nl": "Je zit in de metro van Madrid, op een lijn die niet op het plan staat. Om weer "
                  "boven te raken moet je vervoegen in het presente, kiezen tussen ser en tener, "
                  "de juiste vragen stellen en van elke passagier weten waar die vandaan komt.",
        },
        {
            "titel": "Madrid, primer día · cómic",
            "soort": "Juego",
            "ico": "🎮",
            "url": "https://c5-ruta-digital.wim-wuyts1979.chatgpt.site/u1/comic-madrid",
            "es": "Presentarse en viñetas: el nombre, la edad, de dónde eres y las preguntas "
                  "que abren una conversación.",
            "nl": "Jezelf voorstellen in stripkaders: je naam, je leeftijd, waar je vandaan komt "
                  "en de vragen waarmee een gesprek begint.",
        },
    ],
    ("C5", 2): [
        {
            "titel": "El casting de la persona borrada",
            "soort": "Juego",
            "ico": "🎮",
            "url": "https://c5-ruta-digital.wim-wuyts1979.chatgpt.site/u2/casting-persona-borrada",
            "es": "Alguien ha desaparecido de la foto de familia. Descríbelo para recuperarlo: "
                  "el físico, el carácter y la concordancia del adjetivo.",
            "nl": "Er is iemand van de familiefoto verdwenen. Beschrijf die persoon om hem terug "
                  "te krijgen: het uiterlijk, het karakter en de overeenkomst van het adjectief.",
        },
        {
            "titel": "De Sevilla en familia",
            "soort": "Juego",
            "ico": "🎮",
            "url": "https://c5-ruta-digital.wim-wuyts1979.chatgpt.site/u2/boardgame-sevilla",
            "es": "Una partida por Sevilla, en familia: el verbo tener, los posesivos, ser "
                  "frente a estar y los demostrativos.",
            "nl": "Een spelronde door Sevilla, met de familie erbij: het werkwoord tener, de "
                  "posesivos, ser tegenover estar en de demostrativos.",
        },
    ],
    ("C5", 3): [
        {
            "titel": "Barcelona en 24 horas",
            "soort": "Juego",
            "ico": "🎮",
            "url": "https://c5-ruta-digital.wim-wuyts1979.chatgpt.site/u3/barcelona-24-horas",
            "es": "Un día entero en Barcelona, hora por hora: decir la hora y ordenar la rutina.",
            "nl": "Een hele dag in Barcelona, uur na uur: het uur zeggen en de dagindeling op "
                  "volgorde zetten.",
        },
        {
            "titel": "BCN Ahora",
            "soort": "Juego",
            "ico": "🎮",
            "url": "https://c5-ruta-digital.wim-wuyts1979.chatgpt.site/u3/bcn-ahora",
            "es": "¿Qué pasa en la ciudad en este momento? El presente, también el irregular.",
            "nl": "Wat gebeurt er op dit ogenblik in de stad? Het presente, ook de onregelmatige "
                  "vormen.",
        },
        {
            "titel": "Barcelona paso a paso",
            "soort": "Juego",
            "ico": "🎮",
            "url": "https://c5-ruta-digital.wim-wuyts1979.chatgpt.site/u3/barcelona-paso-a-paso",
            "es": "La rutina con los verbos reflexivos y las expresiones de frecuencia, "
                  "paso a paso.",
            "nl": "De dagindeling met de reflexieve werkwoorden en de frequentiewoorden, "
                  "stap voor stap.",
        },
    ],
    ("C5", 4): [
        {
            "titel": "Malvarrosa Sound Lab",
            "soort": "Juego",
            "ico": "🎮",
            "url": "https://c5-ruta-digital.wim-wuyts1979.chatgpt.site/u4/malvarrosa-sound-lab",
            "es": "En la playa de la Malvarrosa: qué te gusta y qué te encanta, y por qué la "
                  "cosa manda sobre el verbo (gusta ↔ gustan).",
            "nl": "Op het strand van de Malvarrosa: wat je graag hoort en wat je geweldig vindt, "
                  "en waarom het ding de vorm bepaalt (gusta ↔ gustan).",
        },
        {
            "titel": "Match Valencia",
            "soort": "Juego",
            "ico": "🎮",
            "url": "https://c5-ruta-digital.wim-wuyts1979.chatgpt.site/u4/match-valencia",
            "es": "¿Coincidís o no? También, tampoco, a mí sí y a mí no: reaccionar a lo que "
                  "dice el otro.",
            "nl": "Zijn jullie het eens of niet? También, tampoco, a mí sí en a mí no: reageren "
                  "op wat de ander zegt.",
        },
        {
            "titel": "Una tarde · Playlist Draft",
            "soort": "Juego",
            "ico": "🎮",
            "url": "https://c5-ruta-digital.wim-wuyts1979.chatgpt.site/u4/una-tarde-playlist",
            "es": "Montar un plan con querer y poder + infinitivo, y quedar con alguien.",
            "nl": "Een plan maken met querer en poder + infinitief, en met iemand afspreken.",
        },
    ],
    ("C5", 5): [
        {
            "titel": "Mercado Nocturno CDMX",
            "soort": "Juego",
            "ico": "🎮",
            "url": "https://c5-ruta-digital.wim-wuyts1979.chatgpt.site/u5/mercado-nocturno",
            "es": "De noche en el mercado de la CDMX: las cantidades (mucho · poco · un poco de) "
                  "y la comida.",
            "nl": "'s Avonds op de markt van Mexico-Stad: de hoeveelheden (mucho · poco · un "
                  "poco de) en het eten.",
        },
        {
            "titel": "Mesa 13",
            "soort": "Juego",
            "ico": "🎮",
            "url": "https://c5-ruta-digital.wim-wuyts1979.chatgpt.site/u5/mesa-13",
            "es": "Pedir en el restaurante con cortesía, hablar de lo que vas a tomar "
                  "(ir a + infinitivo) y usar lo · la · los · las.",
            "nl": "Bestellen in het restaurant met de juiste beleefdheid, zeggen wat je gaat "
                  "nemen (ir a + infinitief) en lo · la · los · las gebruiken.",
        },
    ],
    # ── C6+ ───────────────────────────────────────────────────────────────────
    # Deze twee staan nog op de óude adressen. De auteur gaf op 2026-08-02 enkel
    # nieuwe adressen voor C5 door (het nieuwe domein heet dan ook c5-ruta-
    # digital), dus deze blijven staan tot hij ze doorgeeft. Nooit zelf verzinnen.
    ("C6+", 0): [
        {
            "titel": "El vuelo 69",
            "soort": "Escape room",
            "ico": "🗝️",
            "url": "https://el-vuelo-69.wim-wuyts1979.chatgpt.site/",
            "es": "Estás a bordo del vuelo 69 y no despega sin ti. Para salir tienes que "
                  "conjugar en presente, elegir entre ser y estar, acertar el género y decir de "
                  "dónde es cada pasajero.",
            "nl": "Je zit aan boord van vlucht 69 en die vertrekt niet zonder jou. Om eruit te "
                  "raken moet je vervoegen in het presente, kiezen tussen ser en estar, het "
                  "juiste geslacht treffen en van elke passagier zeggen waar die vandaan komt.",
        },
    ],
    ("C6+", 1): [
        {
            "titel": "El martes desaparecido",
            "soort": "Escape room",
            "ico": "🗝️",
            "url": "https://martes-desaparecido.wim-wuyts1979.chatgpt.site/",
            "es": "Un martes entero ha desaparecido del calendario. Para recuperarlo tienes que "
                  "reconstruir la rutina hora por hora: los verbos reflexivos, qué le gusta a "
                  "cada uno y cuándo se usa ser o estar.",
            "nl": "Er is een hele dinsdag uit de kalender verdwenen. Om hem terug te krijgen moet "
                  "je de dagindeling uur na uur reconstrueren: de reflexieve werkwoorden, wie "
                  "waarvan houdt, en wanneer je ser of estar gebruikt.",
        },
    ],
}

# Boven de rij uitgelichte spellen. Eén regel, in de taal van de leerling.
DEST_KICKER = "Repaso de toda la unidad"
DEST_TIP = ("Doe ze als afsluiting, nadat je de oefeningen hierboven hebt gemaakt — "
            "of samen met een klasgenoot, om beurten.")

BRONNEN[("C5", 0)] = [
    ("§1 · Klanksysteem — letters, klanken en uitspraak", [
        ("ProfeDeELE", "Letras y sonidos del español",
         "https://www.profedeele.es/actividad/letras-sonidos-espanol/"),
        ("ProfeDeELE", "El abecedario · alfabeto español",
         "https://www.profedeele.es/actividad/abecedario-alfabeto-espanol/"),
        ("ProfeDeELE", "Ortografía — verzamelpagina",
         "https://www.profedeele.es/ortografia/"),
        ("Arche-ELE", "El alfabeto · letras y sonidos",
         "https://arche-ele.com/el-alfabeto-abecedario-letras-y-sonidos"),
        ("My Daily Spanish", "Het alfabet en de uitspraak (video)",
         "https://www.youtube.com/watch?v=KwpdV3aLddw"),
        ("My Daily Spanish", "Uitgebreide uitspraakgids",
         "https://mydailyspanish.com/spanish-pronunciation-guide/"),
    ]),
    ("§2 · Acentuación — aguda, llana, esdrújula en de tilde", [
        ("ProfeDeELE", "Acentos y tildes — hoofdoefening",
         "https://www.profedeele.es/actividad/actividad-de-acentos-tildes/"),
        ("ProfeDeELE", "Palabras agudas",
         "https://www.profedeele.es/actividad/palabras-agudas/"),
        ("ProfeDeELE", "Palabras llanas",
         "https://www.profedeele.es/actividad/palabras-llanas/"),
        ("ProfeDeELE", "Palabras esdrújulas",
         "https://www.profedeele.es/actividad/acentos-palabras-esdrujulas/"),
        ("ProfeDeELE", "Acentos — verzamelpagina",
         "https://www.profedeele.es/ortografia/acentos/"),
        ("Arche-ELE", "La acentuación · aguda, llana, esdrújula, la tilde",
         "https://arche-ele.com/la-acentuacion-aguda-llana-esdrujula-la-tilde"),
        ("My Daily Spanish", "De accentregels (video)",
         "https://www.youtube.com/watch?v=iVgA3FGJVLI"),
    ]),
    ("§3 · Números 0–100", [
        ("ProfeDeELE", "Los números en español — todos",
         "https://www.profedeele.es/actividad/numeros-espanol-todos/"),
        ("ProfeDeELE", "Los números del 0 al 9 — basis",
         "https://www.profedeele.es/actividad/numeros-del-0-al-9/"),
        ("Arche-ELE", "Los números — interactieve oefeningen",
         "https://arche-ele.com/los-numeros-numbers-in-spanish-ele-actividades"),
        ("My Daily Spanish", "De getallen 1–100 (video)",
         "https://www.youtube.com/watch?v=dffV7FSFzCM"),
    ]),
    ("§4 · Género y artículos — el of la", [
        ("ProfeDeELE", "Género masculino / femenino",
         "https://www.profedeele.es/actividad/genero-masculino-femenino/"),
        ("ProfeDeELE", "El artículo definido e indefinido",
         "https://www.profedeele.es/actividad/articulo-definido-indefinido/"),
        ("Arche-ELE", "El género — regels en uitzonderingen",
         "https://arche-ele.com/el-genero-masculino-femenino-aprende-espanol-spanish"),
        ("Arche-ELE", "Infografiek «El género» (pdf)",
         "https://arche-ele.com/wp-content/uploads/2020/11/Infografia-Genero.pdf"),
        ("Arche-ELE", "El artículo — nivel A1",
         "https://arche-ele.com/el-articulo-nivel-a1-indeterminado-determinado"),
        ("My Daily Spanish", "El of la? (video)",
         "https://www.youtube.com/watch?v=2bJy0ehC0i8"),
    ]),
    ("Saludos y despedidas", [
        ("ProfeDeELE", "Saludos y despedidas",
         "https://www.profedeele.es/actividad/saludos-despedidas/"),
        ("Arche-ELE", "Saludos y despedidas",
         "https://arche-ele.com/saludos-y-despedidas-aprende-espanol-learn-spanish"),
        ("My Daily Spanish", "Begroeten en jezelf voorstellen (video)",
         "https://www.youtube.com/watch?v=i0uwQDZo0Ew"),
        ("My Daily Spanish", "Basiszinnen en begroetingen (video)",
         "https://www.youtube.com/watch?v=vyrXC5JDGTc"),
    ]),
    ("Lengua de clase — praten in de klas", [
        ("ProfeDeELE", "Dar y pedir información personal",
         "https://www.profedeele.es/actividad/dar-pedir-informacion-personal/"),
        ("Arche-ELE", "La clase — woordenschat en interactieve oefeningen",
         "https://arche-ele.com/la-clase-ele-vocabulario-actividades-interactivas"),
        ("Arche-ELE", "El primer día en la clase de español",
         "https://arche-ele.com/el-primer-dia-en-la-clase-de-espanol-aprender-espanol"),
        ("My Daily Spanish", "Bruikbare basiszinnen (video)",
         "https://www.youtube.com/watch?v=vyrXC5JDGTc"),
    ]),
    ("Presentarse y la edad — jezelf voorstellen", [
        ("ProfeDeELE", "Dar y pedir información personal",
         "https://www.profedeele.es/actividad/dar-pedir-informacion-personal/"),
        ("Arche-ELE", "Información personal",
         "https://arche-ele.com/informacion-personal-aprende-espanol-learn-spanish"),
        ("My Daily Spanish", "Jezelf voorstellen (video)",
         "https://www.youtube.com/watch?v=i0uwQDZo0Ew"),
    ]),
    ("El mundo hispano — landen en cultuur", [
        ("ProfeDeELE", "Países hispanohablantes",
         "https://www.profedeele.es/actividad/paises-hispanohablantes/"),
        ("ProfeDeELE", "Escape room · Google Maps y los países hispanohablantes",
         "https://www.profedeele.es/actividad/escape-room-google-maps-y-los-paises-hispanohablantes/"),
        ("Arche-ELE", "Países hispanohablantes — woordenschat",
         "https://arche-ele.com/paises-hispanohablantes-vocabulario-aprende-espanol"),
        ("My Daily Spanish", "De Spaanstalige wereld (video)",
         "https://www.youtube.com/watch?v=fuInQ1rJKrw"),
    ]),
    ("Países, lenguas y nacionalidades", [
        ("ProfeDeELE", "Países, lenguas y nacionalidades",
         "https://www.profedeele.es/actividad/paises-lenguas-nacionalidades/"),
        ("Arche-ELE", "Países y nacionalidades",
         "https://arche-ele.com/paises-y-nacionalidades-countries-nationalities"),
    ]),
]


BRONNEN[("C5", 1)] = [
    ("§1 · El presente regular (-ar · -er · -ir)", [
        ("ProfeDeELE", "Presente regular",
         "https://www.profedeele.es/actividad/presente-regular/"),
        ("Arche-ELE", "El presente regular de indicativo · conjugaciones",
         "https://arche-ele.com/el-presente-regular-de-indicativo-conjugaciones"),
    ]),
    ("§2 · ¿ser o tener? — la edad se «tiene»", [
        ("Arche-ELE", "Ser y tener · nivel A1",
         "https://arche-ele.com/ser-y-tener-nivel-a1-actividades"),
    ]),
    ("§3 · Las palabras interrogativas", [
        ("ProfeDeELE", "Pronombres interrogativos — qué · quién · dónde · cómo · cuándo · cuál",
         "https://www.profedeele.es/actividad/pronombres-interrogativos/"),
    ]),
    ("§4 · El género y los artículos", [
        ("ProfeDeELE", "Género masculino / femenino",
         "https://www.profedeele.es/actividad/genero-masculino-femenino/"),
        ("Arche-ELE", "El género — el y la",
         "https://arche-ele.com/el-genero-masculino-femenino-aprende-espanol-spanish"),
        ("ProfeDeELE", "El artículo definido e indefinido",
         "https://www.profedeele.es/actividad/articulo-definido-indefinido/"),
        ("Arche-ELE", "El artículo — nivel A1",
         "https://arche-ele.com/el-articulo-nivel-a1-indeterminado-determinado"),
        ("My Daily Spanish", "El of la kiezen (video)",
         "https://www.youtube.com/watch?v=2bJy0ehC0i8"),
    ]),
    ("Países, lenguas y nacionalidades", [
        ("ProfeDeELE", "Países, lenguas y nacionalidades",
         "https://www.profedeele.es/actividad/paises-lenguas-nacionalidades/"),
        ("Arche-ELE", "País ↔ nacionalidad",
         "https://arche-ele.com/paises-y-nacionalidades-countries-nationalities"),
    ]),
    ("Datos personales · presentarse (tarea «Mi pasaporte»)", [
        ("ProfeDeELE", "Dar y pedir información personal",
         "https://www.profedeele.es/actividad/dar-pedir-informacion-personal/"),
        ("Arche-ELE", "Información personal",
         "https://arche-ele.com/informacion-personal-aprende-espanol-learn-spanish"),
        ("My Daily Spanish", "Jezelf voorstellen (video)",
         "https://www.youtube.com/watch?v=i0uwQDZo0Ew"),
    ]),
    ("La familia", [
        ("ProfeDeELE", "La familia", "https://www.profedeele.es/actividad/la-familia/"),
        ("Arche-ELE", "La familia — woordenschat en stamboom",
         "https://arche-ele.com/la-familia-vocabulario-family-spanish-vocabulary"),
    ]),
    ("El instituto y la clase", [
        ("ProfeDeELE", "El material escolar",
         "https://www.profedeele.es/actividad/material-escolar/"),
        ("Arche-ELE", "La clase — woordenschat en interactieve oefeningen",
         "https://arche-ele.com/la-clase-ele-vocabulario-actividades-interactivas"),
    ]),
    ("Describir personas — físico y carácter", [
        ("ProfeDeELE", "La descripción física",
         "https://www.profedeele.es/actividad/descripcion-fisico-espanol/"),
        ("ProfeDeELE", "Adjetivos de carácter y personalidad",
         "https://www.profedeele.es/actividad/adjetivos-caracter-personalidad/"),
        ("Arche-ELE", "Descripciones A1 — físicas y de carácter",
         "https://arche-ele.com/descripciones-a1-fisicasydecaracter-en-espanol"),
    ]),
    ("Saludos y despedidas", [
        ("ProfeDeELE", "Saludos y despedidas",
         "https://www.profedeele.es/actividad/saludos-despedidas/"),
        ("Arche-ELE", "Saludos y despedidas",
         "https://arche-ele.com/saludos-y-despedidas-aprende-espanol-learn-spanish"),
    ]),
]


BRONNEN[("C5", 2)] = [
    ("§1 · La familia y el verbo tener", [
        ("ProfeDeELE", "La familia — vocabulario y relaciones familiares",
         "https://www.profedeele.es/actividad/la-familia/"),
        ("Arche-ELE", "La familia — vocabulario, árbol genealógico y audios · "
                      "sirve también para los posesivos y para la tarea final",
         "https://arche-ele.com/la-familia-vocabulario-family-spanish-vocabulary"),
        ("Más ProfeDeELE", "La familia — material extra y árboles genealógicos",
         "https://mas.profedeele.es/descarga-66"),
        ("Arche-ELE", "Ser y tener · nivel A1",
         "https://arche-ele.com/ser-y-tener-nivel-a1-actividades"),
        ("ProfeDeELE", "Presente irregular — tener y los demás",
         "https://www.profedeele.es/actividad/presente-irregular/"),
    ]),
    ("§2 · Los posesivos — mi, tu, su, nuestro", [
        ("Arche-ELE", "Los posesivos — mi, tu, su · sirve también para la tarea final",
         "https://arche-ele.com/los-posesivos-mi-tu-su-ele-aprender-espanol"),
        ("Más ProfeDeELE", "Los posesivos — ficha de gramática",
         "https://mas.profedeele.es/descarga-320"),
    ]),
    ("§3 · Los adjetivos — el físico y el carácter", [
        ("ProfeDeELE", "Descripción física",
         "https://www.profedeele.es/actividad/descripcion-fisico-espanol/"),
        ("ProfeDeELE", "Adjetivos de carácter y personalidad",
         "https://www.profedeele.es/actividad/adjetivos-caracter-personalidad/"),
        ("Arche-ELE", "Descripciones A1 — el físico, el carácter y la concordancia",
         "https://arche-ele.com/descripciones-a1-fisicasydecaracter-en-espanol"),
    ]),
    ("§4 · Ser o estar — la gran trampa del «zijn»", [
        ("Arche-ELE", "Ser y estar — la diferencia, explicada paso a paso",
         "https://arche-ele.com/ser-y-estar-gramatica-cognitiva-ele-diferencia"),
        ("My Daily Spanish", "Ser frente a estar — el vídeo",
         "https://www.youtube.com/watch?v=X-7k7R3Ca9U"),
        ("ProfeDeELE", "Haber, estar y tener — distinguirlos",
         "https://www.profedeele.es/actividad/haber-estar-tener/"),
        ("Más ProfeDeELE", "Haber, estar y tener — test extra",
         "https://mas.profedeele.es/descarga-69"),
    ]),
    ("§5 · Los demostrativos — este y ese", [
        ("Arche-ELE", "Los demostrativos — este, ese, aquel",
         "https://arche-ele.com/los-demostrativos-ele-este-ese-aquel"),
        ("Más ProfeDeELE", "Los demostrativos — explicación y ejercicios (A1–A2)",
         "https://mas.profedeele.es/descarga-293-demostrativos-materiales-gramatica-a1-a2-ele"),
    ]),
    ("Taller de lengua — la acentuación, los conectores y el correo", [
        ("Arche-ELE", "La acentuación — agudas, llanas y esdrújulas",
         "https://arche-ele.com/la-acentuacion-en-espanol-agudas-llanas-esdrujulas"),
        ("Más ProfeDeELE", "Manual de nivel A1 — conectores, ortografía y escribir un correo",
         "https://mas.profedeele.es/curso-nivel-a1"),
    ]),
    ("El cuerpo humano", [
        ("Arche-ELE", "El cuerpo humano",
         "https://arche-ele.com/el-cuerpo-humano-human-body-espanol-spanish-ele"),
        ("Más ProfeDeELE", "El cuerpo humano — ficha",
         "https://mas.profedeele.es/descarga-125"),
    ]),
    ("Los colores", [
        ("Arche-ELE", "Los colores",
         "https://arche-ele.com/los-colores-ele-aprende-espanol-arche-ele"),
        ("Más ProfeDeELE", "Los colores — ficha",
         "https://mas.profedeele.es/descarga-120"),
    ]),
    ("Cultura · Frida Kahlo", [
        ("Más ProfeDeELE", "Frida Kahlo — material de cultura",
         "https://mas.profedeele.es/descarga-164"),
    ]),
]

BRONNEN[("C5", 3)] = [
    ("§1 · La hora — es la una / son las…", [
        ("ProfeDeELE", "La hora — ¿qué hora es?",
         "https://www.profedeele.es/actividad/la-hora/"),
        ("Arche-ELE", "La hora — es la una frente a son las…, y los horarios de tren",
         "https://arche-ele.com/la-hora-time-que-hora-es-tienes-hora-ele"),
    ]),
    ("§2 · La rutina y los verbos reflexivos", [
        ("ProfeDeELE", "Las acciones habituales — ponerlas en orden cronológico · "
                       "sirve también para la lectura, la cultura y la tarea final",
         "https://www.profedeele.es/actividad/acciones-habituales/"),
        ("Arche-ELE", "La rutina diaria con los verbos reflexivos · sirve también para la "
                      "frecuencia, para la escucha y para la tarea final",
         "https://arche-ele.com/la-rutina-daily-routine-aprende-espanol-learn-spanish"),
        ("Arche-ELE", "Los pronombres reflexivos · nivel A1",
         "https://arche-ele.com/pronombres-reflexivos-1-nivel-a1"),
    ]),
    ("§3 · El presente irregular — el cambio de raíz", [
        ("Arche-ELE", "El presente irregular — e→ie, o→ue, e→i, y también hacer, ir y salir",
         "https://arche-ele.com/presente-irregular-indicativo-verbos-espanol"),
        ("Más ProfeDeELE", "El presente irregular — explicación, audio y ejercicios de conjugación",
         "https://mas.profedeele.es/descarga-101"),
    ]),
    ("§3b · hacer · ir · salir", [
        ("Más ProfeDeELE", "Los verbos irregulares — juegos de mesa",
         "https://mas.profedeele.es/descarga-92"),
    ]),
    ("§4 · La frecuencia, los días y los meses", [
        ("Más ProfeDeELE", "Adverbios de frecuencia — siempre, normalmente, a veces, nunca · "
                           "sirve también para leer un horario semanal",
         "https://mas.profedeele.es/descarga-286-adverbios-frecuencia-juegos-tarjetas"),
        ("Arche-ELE", "Los días de la semana y los meses · sirve también para el chat de la lectura",
         "https://arche-ele.com/los-dias-y-los-meses-tiempo-semana-ano"),
        ("Más ProfeDeELE", "Días, meses y estaciones",
         "https://mas.profedeele.es/descarga-206"),
    ]),
    ("Taller de lengua — la acentuación", [
        ("Arche-ELE", "La acentuación — agudas, llanas y esdrújulas",
         "https://arche-ele.com/la-acentuacion-en-espanol-agudas-llanas-esdrujulas"),
        ("Más ProfeDeELE", "Manual de nivel A1 — la hora, el presente irregular, los días "
                           "y la ortografía",
         "https://mas.profedeele.es/curso-nivel-a1"),
    ]),
    ("Cultura · el horario español", [
        ("Más ProfeDeELE", "Veranos y relojes",
         "https://mas.profedeele.es/descarga-200"),
    ]),
]

BRONNEN[("C5", 4)] = [
    ("§1 · El verbo gustar — gusta / gustan", [
        ("Arche-ELE", "Gustar, encantar e interesar — la frase al revés · sirve también para el "
                      "ocio y para el repaso final",
         "https://arche-ele.com/me-gusta-gustar-verbos-aprende-espanol"),
        ("ProfeDeELE", "Me gustas tú — gustar con personas",
         "https://www.profedeele.es/actividad/me-gustas-tu/"),
    ]),
    ("§2 · Reaccionar — también, tampoco, a mí sí, a mí no", [
        ("Más ProfeDeELE", "Me gusta / no me gusta — comparar gustos y reaccionar",
         "https://mas.profedeele.es/descarga-062"),
        ("Más ProfeDeELE", "Manual de nivel A1 — también, tampoco, a mí sí, a mí no",
         "https://mas.profedeele.es/curso-nivel-a1"),
    ]),
    ("§3 · Querer y poder + infinitivo", [
        ("Arche-ELE", "Querer y poder en presente — verbos irregulares",
         "https://arche-ele.com/presente-irregular-indicativo-verbos-espanol"),
        ("Más ProfeDeELE", "Querer / poder + infinitivo — ejercicios",
         "https://mas.profedeele.es/descarga-101"),
    ]),
    ("Los pronombres OI — me, te, le, nos, os, les", [
        ("ProfeDeELE", "Pronombres de objeto indirecto",
         "https://www.profedeele.es/actividad/pronombres-objeto-indirecto/"),
        ("Más ProfeDeELE", "Los pronombres OI — forma y uso",
         "https://mas.profedeele.es/descarga-269"),
    ]),
    ("El ocio y el tiempo libre", [
        ("Arche-ELE", "Las aficiones y los hobbies",
         "https://arche-ele.com/aficiones-hobbies-vocabulario-aprende-espanol"),
    ]),
    ("La música y el cine", [
        ("Arche-ELE", "La música — instrumentos y géneros · sirve también para la tarea "
                      "«Mi playlist»",
         "https://arche-ele.com/la-musica-vocabulario-instrumentos-generos-musicales"),
        ("Arche-ELE", "El cine — películas y géneros",
         "https://arche-ele.com/el-cine-vocabulario-peliculas-generos"),
    ]),
    ("Cultura · Rosalía y «La fama»", [
        ("Más ProfeDeELE", "Rosalía — «La fama»",
         "https://mas.profedeele.es/descarga-188"),
    ]),
]

BRONNEN[("C5", 5)] = [
    ("§1 · Las cantidades — mucho, poco, un poco de", [
        ("Arche-ELE", "Muy o mucho — la diferencia y la concordancia",
         "https://arche-ele.com/muy-o-mucho-diferencias-aprende-espanol"),
        ("Más ProfeDeELE", "Manual de nivel A1 — las cantidades y el futuro próximo con ir a",
         "https://mas.profedeele.es/curso-nivel-a1"),
    ]),
    ("§2 · Ir a + infinitivo — el futuro próximo", [
        ("Arche-ELE", "Ir a + infinitivo",
         "https://arche-ele.com/ir-a-infinitivo-futuro-proximo"),
    ]),
    ("§3 · Pedir en el restaurante — la cortesía", [
        ("Arche-ELE", "En el restaurante — vocabulario, la mesa y diálogos · sirve también para "
                      "la tarea «La carta»",
         "https://arche-ele.com/en-el-restaurante-vocabulario-dialogos-aprende-espanol"),
        ("ProfeDeELE", "En el restaurante — pedir con cortesía",
         "https://www.profedeele.es/actividad/en-el-restaurante/"),
    ]),
    ("§4 · Los pronombres lo / la / los / las", [
        ("ProfeDeELE", "Pronombres de objeto directo",
         "https://www.profedeele.es/actividad/pronombres-objeto-directo/"),
        ("Arche-ELE", "El objeto directo — lo, la, los, las",
         "https://arche-ele.com/el-objeto-directo-od-pronombres"),
        ("Más ProfeDeELE", "Manual de nivel A2 — pronombres OD y OI, y la fruta y la verdura",
         "https://mas.profedeele.es/curso-nivel-a2"),
    ]),
    ("La comida, la fruta y la bebida", [
        ("Arche-ELE", "La comida — vocabulario",
         "https://arche-ele.com/la-comida-vocabulario-aprende-espanol-ele"),
        ("ProfeDeELE", "Alimentos, comida y bebida",
         "https://www.profedeele.es/actividad/alimentos-comida-bebida/"),
        ("Más ProfeDeELE", "La fruta — ficha",
         "https://mas.profedeele.es/descarga-252"),
    ]),
    ("Cultura · México", [
        ("Más ProfeDeELE", "Cultureta — material de cultura hispana",
         "https://mas.profedeele.es/pack-ahorro-profe-cultureta"),
    ]),
]

BRONNEN[("C5", 6)] = [
    ("§1 · Los pronombres lo / la / los / las", [
        ("ProfeDeELE", "Pronombres de objeto directo",
         "https://www.profedeele.es/actividad/pronombres-objeto-directo/"),
        ("Arche-ELE", "El objeto directo — evitar la repetición",
         "https://arche-ele.com/el-objeto-directo-od-pronombres"),
        ("Más ProfeDeELE", "Manual de nivel A2 — pronombres OD y OI",
         "https://mas.profedeele.es/curso-nivel-a2"),
    ]),
    ("§2 · Acabar de + infinitivo", [
        ("ProfeDeELE", "Acabar de + infinitivo",
         "https://www.profedeele.es/actividad/acabar-de-infinitivo/"),
        ("Arche-ELE", "Las perífrasis verbales",
         "https://arche-ele.com/perifrasis-verbales-aprende-espanol"),
    ]),
    ("§3 · Los demostrativos — este, ese, aquel", [
        ("Arche-ELE", "Este, ese y aquel — según la distancia",
         "https://arche-ele.com/los-demostrativos-ele-este-ese-aquel"),
        ("Más ProfeDeELE", "Los demostrativos — explicación y ejercicios (A1–A2)",
         "https://mas.profedeele.es/descarga-293-demostrativos-materiales-gramatica-a1-a2-ele"),
    ]),
    ("§4 · La concordancia — el color y la prenda", [
        ("Arche-ELE", "Los colores",
         "https://arche-ele.com/los-colores-ele-aprende-espanol-arche-ele"),
        ("Más ProfeDeELE", "Los colores — ficha",
         "https://mas.profedeele.es/descarga-120"),
        ("Arche-ELE", "La ropa — y la concordancia entre el color y la prenda",
         "https://arche-ele.com/la-ropa-clothes-vocabulario-aprende-espanol"),
    ]),
    ("La ropa, el calzado y la tienda", [
        ("ProfeDeELE", "La ropa y los complementos",
         "https://www.profedeele.es/actividad/la-ropa/"),
        ("Más ProfeDeELE", "La ropa — ejercicios extra, diálogo y en la tienda: tallas, "
                           "probador y caja",
         "https://mas.profedeele.es/descarga-159"),
        ("Arche-ELE", "Listas de vocabulario — el calzado y los accesorios",
         "https://arche-ele.com/listas-de-vocabulario-list-of-vocabulary-espanol"),
    ]),
    ("Cultura · las rebajas y el consumo", [
        ("ProfeDeELE", "La desaparición de lo cutre — consumo y tendencias",
         "https://www.profedeele.es/actividad/la-desaparicion-de-lo-cutre/"),
        ("Más ProfeDeELE", "Las rebajas — ficha",
         "https://mas.profedeele.es/descarga-243"),
    ]),
]

BRONNEN[("C5", 7)] = [
    ("§1 · Hay o está(n)", [
        ("ProfeDeELE", "Haber, estar y tener — distinguirlos",
         "https://www.profedeele.es/actividad/haber-estar-tener/"),
        ("Arche-ELE", "Ser, estar y hay — describir lugares",
         "https://arche-ele.com/ser-estar-hay-describir-lugares"),
    ]),
    ("§2 · Las preposiciones de lugar", [
        ("Arche-ELE", "Las preposiciones de lugar · nivel A1",
         "https://arche-ele.com/preposiciones-de-lugar-a1"),
    ]),
    ("§3 · Estar + gerundio", [
        ("Arche-ELE", "Estar + gerundio — las perífrasis de gerundio",
         "https://arche-ele.com/estar-gerundio-perifrasis-verbales-de-gerundio"),
        ("Más ProfeDeELE", "Gramática — estar + gerundio y el imperativo",
         "https://mas.profedeele.es/gramatica"),
    ]),
    ("§4 · El imperativo — dar direcciones", [
        ("Arche-ELE", "El imperativo afirmativo",
         "https://arche-ele.com/el-imperativo-afirmativo-aprende-espanol"),
    ]),
    ("§5 · Los números ordinales", [
        ("Más ProfeDeELE", "Pack de números — los ordinales y los pisos",
         "https://mas.profedeele.es/pack-numeros"),
    ]),
    ("La casa y los muebles", [
        ("Arche-ELE", "La casa — vocabulario",
         "https://arche-ele.com/la-casa-vocabulario-aprende-espanol"),
        ("Más ProfeDeELE", "Los muebles — ficha",
         "https://mas.profedeele.es/descarga-63"),
        ("Más ProfeDeELE", "Manual de nivel A2 — la casa, las preposiciones de lugar y dar "
                           "direcciones",
         "https://mas.profedeele.es/curso-nivel-a2"),
    ]),
    ("La ciudad y el barrio", [
        ("Arche-ELE", "La ciudad — vocabulario · sirve también para la tarea «Mapa de mi barrio»",
         "https://arche-ele.com/la-ciudad-en-espanol-vocabulario"),
    ]),
    ("El transporte", [
        ("Arche-ELE", "Los medios de transporte",
         "https://arche-ele.com/los-medios-de-transporte-vocabulario-ele"),
        ("Más ProfeDeELE", "Medios de transporte — ficha",
         "https://mas.profedeele.es/descarga-002"),
    ]),
]

BRONNEN[("C5", 8)] = [
    ("§1–§3 · El pretérito perfecto, los participios y los marcadores", [
        ("Arche-ELE", "El pretérito perfecto — haber + participio, los participios irregulares "
                      "y los marcadores ya · todavía no · alguna vez · nunca · sirve también "
                      "para la tarea final",
         "https://arche-ele.com/el-preterito-perfecto-pasados-aprende-espanol"),
        ("Más ProfeDeELE", "Los participios irregulares — para practicar",
         "https://mas.profedeele.es/pack-ahorro-profe-online"),
        ("Más ProfeDeELE", "Manual de nivel A2 — el perfecto, los participios y el repaso de "
                           "toda la ruta",
         "https://mas.profedeele.es/curso-nivel-a2"),
    ]),
    ("§4 · El tiempo y el clima", [
        ("Arche-ELE", "El tiempo atmosférico",
         "https://arche-ele.com/el-tiempo-atmosferico-weather-aprende-espanol"),
        ("Más ProfeDeELE", "Describir el tiempo — ficha",
         "https://mas.profedeele.es/descarga-131"),
    ]),
    ("Los viajes y el transporte", [
        ("Arche-ELE", "Los medios de transporte",
         "https://arche-ele.com/los-medios-de-transporte-vocabulario-ele"),
        ("Más ProfeDeELE", "Medios de transporte — ficha",
         "https://mas.profedeele.es/descarga-002"),
    ]),
    ("Las vacaciones", [
        ("ProfeDeELE", "Las vacaciones de verano",
         "https://www.profedeele.es/actividad/vacaciones-verano/"),
        ("Más ProfeDeELE", "Superpack de verano",
         "https://mas.profedeele.es/superpack-verano-ahorro"),
    ]),
    ("Cultura · viajes y experiencias", [
        ("Más ProfeDeELE", "Viajes y experiencias de vacaciones",
         "https://mas.profedeele.es/descarga-191"),
    ]),
]

BRONNEN[("C6+", 1)] = [
    ("§1 · Los verbos reflexivos y la rutina", [
        ("Arche-ELE", "Pronombres reflexivos · nivel A1 — la posición del pronombre",
         "https://arche-ele.com/pronombres-reflexivos-1-nivel-a1"),
        ("Arche-ELE", "La rutina — reflexieve werkwoorden in context",
         "https://arche-ele.com/la-rutina-daily-routine-aprende-espanol-learn-spanish"),
        ("ProfeDeELE", "Acciones habituales — dagelijkse handelingen",
         "https://www.profedeele.es/actividad/acciones-habituales/"),
    ]),
    ("§2 · El verbo gustar", [
        ("Arche-ELE", "Me gusta · gustar — me · te · le · nos · les",
         "https://arche-ele.com/me-gusta-gustar-verbos-aprende-espanol"),
        ("ProfeDeELE", "Me gustas tú — gusta tegenover gustan",
         "https://www.profedeele.es/actividad/me-gustas-tu/"),
        ("ProfeDeELE", "Gustos y preferencias — me gusta / no me gusta (download)",
         "https://mas.profedeele.es/descarga-062"),
    ]),
    ("§3 · ¿ser o estar?", [
        ("Arche-ELE", "Ser y estar — het verschil, cognitief uitgelegd",
         "https://arche-ele.com/ser-y-estar-gramatica-cognitiva-ele-diferencia"),
        ("My Daily Spanish", "Ser of estar? (video)",
         "https://www.youtube.com/watch?v=X-7k7R3Ca9U"),
        ("ProfeDeELE", "Haber · estar · tener — plaats en toestand",
         "https://www.profedeele.es/actividad/haber-estar-tener/"),
    ]),
    ("§4 · La hora", [
        ("ProfeDeELE", "La hora — es la una · son las… · y cuarto · y media · menos cuarto",
         "https://www.profedeele.es/actividad/la-hora/"),
        ("Arche-ELE", "La hora — ¿qué hora es? · ¿tienes hora?",
         "https://arche-ele.com/la-hora-time-que-hora-es-tienes-hora-ele"),
    ]),
    ("Las comidas y la alimentación", [
        ("Arche-ELE", "La comida — woordenschat",
         "https://arche-ele.com/la-comida-vocabulario-aprende-espanol-ele"),
    ]),
]


BRONNEN[("C6+", 0)] = [
    ("§2.1 · El presente — los verbos regulares (-ar · -er · -ir)", [
        ("ProfeDeELE", "Presente regular",
         "https://www.profedeele.es/actividad/presente-regular/"),
        ("Arche-ELE", "El presente regular de indicativo · conjugaciones",
         "https://arche-ele.com/el-presente-regular-de-indicativo-conjugaciones"),
        ("My Daily Spanish", "De regelmatige werkwoorden (video)",
         "https://www.youtube.com/watch?v=YSQmaik54jI"),
    ]),
    ("§2.2 · El presente — los verbos irregulares", [
        ("ProfeDeELE", "Verbos en presente irregular",
         "https://www.profedeele.es/actividad/verbo-presente-irregular/"),
        ("Arche-ELE", "Presente irregular de indicativo",
         "https://arche-ele.com/presente-irregular-indicativo-verbos-espanol"),
        ("Arche-ELE", "Infografiek «Presente irregular» (pdf)",
         "https://arche-ele.com/wp-content/uploads/2020/12/PRESENTE-IRREGULAR-info.pdf"),
        ("Arche-ELE", "Tableros de conjugación — conjugatiespel (Genially)",
         "https://arche-ele.com/tableros-conjugacion-genially-gamificacion-ele"),
    ]),
    ("Los verbos clave — ser · estar · tener · ir · venir", [
        ("My Daily Spanish", "De meest frequente Spaanse werkwoorden",
         "https://mydailyspanish.com/common-spanish-verbs/"),
        ("My Daily Spanish", "De essentiële werkwoorden vervoegd (video)",
         "https://www.youtube.com/watch?v=gcSQBS1fZm4"),
        ("ProfeDeELE", "Ir · venir · llevar · traer",
         "https://www.profedeele.es/actividad/ir-venir-llevar-traer/"),
        ("Arche-ELE", "El verbo ir · ir a + infinitivo",
         "https://arche-ele.com/el-verbo-ir-ir-a-infinitivo-ele-actividades"),
    ]),
    ("Ser o estar — y también hay", [
        ("Arche-ELE", "Ser y estar — het verschil, cognitief uitgelegd",
         "https://arche-ele.com/ser-y-estar-gramatica-cognitiva-ele-diferencia"),
        ("My Daily Spanish", "Ser en estar — uitleg en voorbeelden",
         "https://mydailyspanish.com/ser-estar/"),
        ("My Daily Spanish", "Ser of estar? (video)",
         "https://www.youtube.com/watch?v=X-7k7R3Ca9U"),
        ("Arche-ELE", "Describir lugares con ser · estar · hay",
         "https://arche-ele.com/describir-lugares-con-ser-estar-hay-learn-spanish"),
        ("ProfeDeELE", "Haber · estar · tener — plaats, toestand en bezit",
         "https://www.profedeele.es/actividad/haber-estar-tener/"),
    ]),
    ("§3 · Género, artículos, número y concordancia", [
        ("ProfeDeELE", "Género masculino / femenino",
         "https://www.profedeele.es/actividad/genero-masculino-femenino/"),
        ("Arche-ELE", "El género — regels en uitzonderingen",
         "https://arche-ele.com/el-genero-masculino-femenino-aprende-espanol-spanish"),
        ("My Daily Spanish", "El of la? (video)",
         "https://www.youtube.com/watch?v=2bJy0ehC0i8"),
        ("ProfeDeELE", "El artículo definido e indefinido",
         "https://www.profedeele.es/actividad/articulo-definido-indefinido/"),
        ("Arche-ELE", "El artículo — nivel A1",
         "https://arche-ele.com/el-articulo-nivel-a1-indeterminado-determinado"),
        ("ProfeDeELE", "Número — singular y plural",
         "https://www.profedeele.es/actividad/numero-singular-plural-en-espanol/"),
        ("ProfeDeELE", "Adjetivos ilustrados 1–40",
         "https://www.profedeele.es/actividad/adjetivos-ilustrados-1-40/"),
        ("ProfeDeELE", "Adjetivos ilustrados 41–80",
         "https://www.profedeele.es/actividad/adjetivos-ilustrados-41-80/"),
    ]),
    ("Suena bien — sonidos y pronunciación", [
        ("ProfeDeELE", "Letras y sonidos del español",
         "https://www.profedeele.es/actividad/letras-sonidos-espanol/"),
        ("Arche-ELE", "El alfabeto · letras y sonidos",
         "https://arche-ele.com/el-alfabeto-abecedario-letras-y-sonidos"),
        ("My Daily Spanish", "Het alfabet en de uitspraak (video)",
         "https://www.youtube.com/watch?v=KwpdV3aLddw"),
        ("My Daily Spanish", "Moeilijke Spaanse woorden uitspreken (video)",
         "https://www.youtube.com/watch?v=RUWFjkELA9k"),
        ("My Daily Spanish", "Uitgebreide uitspraakgids",
         "https://mydailyspanish.com/spanish-pronunciation-guide/"),
    ]),
    ("Taller de lengua · 1 — la acentuación", [
        ("ProfeDeELE", "Acentos y tildes — hoofdoefening",
         "https://www.profedeele.es/actividad/actividad-de-acentos-tildes/"),
        ("ProfeDeELE", "Palabras agudas",
         "https://www.profedeele.es/actividad/palabras-agudas/"),
        ("ProfeDeELE", "Palabras llanas",
         "https://www.profedeele.es/actividad/palabras-llanas/"),
        ("ProfeDeELE", "Palabras esdrújulas",
         "https://www.profedeele.es/actividad/acentos-palabras-esdrujulas/"),
        ("Arche-ELE", "La acentuación · aguda, llana, esdrújula, la tilde",
         "https://arche-ele.com/la-acentuacion-aguda-llana-esdrujula-la-tilde"),
    ]),
    ("Taller de lengua · 2 — los conectores", [
        ("ProfeDeELE", "Marcadores discursivos y conectores",
         "https://www.profedeele.es/actividad/marcadores-discursivos-conectores/"),
        ("My Daily Spanish", "y · pero · porque · aunque (video)",
         "https://www.youtube.com/watch?v=x4gQYsh9eBs"),
        ("My Daily Spanish", "Zinnen aan elkaar verbinden (video)",
         "https://www.youtube.com/watch?v=yTTyTlEREA4"),
    ]),
    ("Presentarse · datos personales", [
        ("ProfeDeELE", "Dar y pedir información personal",
         "https://www.profedeele.es/actividad/dar-pedir-informacion-personal/"),
        ("Arche-ELE", "Información personal",
         "https://arche-ele.com/informacion-personal-aprende-espanol-learn-spanish"),
        ("My Daily Spanish", "Jezelf voorstellen (video)",
         "https://www.youtube.com/watch?v=i0uwQDZo0Ew"),
    ]),
    ("Saludos y despedidas", [
        ("ProfeDeELE", "Saludos y despedidas",
         "https://www.profedeele.es/actividad/saludos-despedidas/"),
        ("Arche-ELE", "Saludos y despedidas",
         "https://arche-ele.com/saludos-y-despedidas-aprende-espanol-learn-spanish"),
        ("My Daily Spanish", "Begroetingen en basisuitdrukkingen (video)",
         "https://www.youtube.com/watch?v=vyrXC5JDGTc"),
    ]),
    ("En clase — woordenschat en klastaal", [
        ("ProfeDeELE", "El material escolar",
         "https://www.profedeele.es/actividad/material-escolar/"),
        ("Arche-ELE", "La clase — woordenschat en interactieve oefeningen",
         "https://arche-ele.com/la-clase-ele-vocabulario-actividades-interactivas"),
        ("Arche-ELE", "El primer día en la clase de español",
         "https://arche-ele.com/el-primer-dia-en-la-clase-de-espanol-aprender-espanol"),
        ("My Daily Spanish", "Dagelijkse basisuitdrukkingen (video)",
         "https://www.youtube.com/watch?v=6_5FnCLLYoA"),
    ]),
    ("Países, nacionalidades y lenguas · el mundo hispano", [
        ("ProfeDeELE", "Países, lenguas y nacionalidades",
         "https://www.profedeele.es/actividad/paises-lenguas-nacionalidades/"),
        ("Arche-ELE", "Países y nacionalidades",
         "https://arche-ele.com/paises-y-nacionalidades-countries-nationalities"),
        ("ProfeDeELE", "Países hispanohablantes",
         "https://www.profedeele.es/actividad/paises-hispanohablantes/"),
        ("ProfeDeELE", "Escape room · Google Maps y los países hispanohablantes",
         "https://www.profedeele.es/actividad/escape-room-google-maps-y-los-paises-hispanohablantes/"),
        ("Arche-ELE", "Países hispanohablantes — woordenschat",
         "https://arche-ele.com/paises-hispanohablantes-vocabulario-aprende-espanol"),
        ("My Daily Spanish", "De Spaanstalige wereld (video)",
         "https://www.youtube.com/watch?v=fuInQ1rJKrw"),
    ]),
    ("Describir personas — físico y carácter", [
        ("ProfeDeELE", "La descripción física",
         "https://www.profedeele.es/actividad/descripcion-fisico-espanol/"),
        ("ProfeDeELE", "Adjetivos de carácter y personalidad",
         "https://www.profedeele.es/actividad/adjetivos-caracter-personalidad/"),
        ("Arche-ELE", "Descripciones A1 — físicas y de carácter",
         "https://arche-ele.com/descripciones-a1-fisicasydecaracter-en-espanol"),
    ]),
    ("Verbos frecuentes en presente — acciones y rutinas", [
        ("ProfeDeELE", "Acciones habituales",
         "https://www.profedeele.es/actividad/acciones-habituales/"),
        ("Arche-ELE", "La rutina — dagelijkse routine",
         "https://arche-ele.com/la-rutina-daily-routine-aprende-espanol-learn-spanish"),
    ]),
    ("La familia", [
        ("ProfeDeELE", "La familia",
         "https://www.profedeele.es/actividad/la-familia/"),
        ("Arche-ELE", "La familia — woordenschat en stamboom",
         "https://arche-ele.com/la-familia-vocabulario-family-spanish-vocabulary"),
    ]),
    ("Números y datos", [
        ("ProfeDeELE", "Los números en español — todos",
         "https://www.profedeele.es/actividad/numeros-espanol-todos/"),
        ("Arche-ELE", "Los números 0–100",
         "https://arche-ele.com/los-numeros-numbers-in-spanish-ele-actividades"),
        ("My Daily Spanish", "De getallen 1–100 (video)",
         "https://www.youtube.com/watch?v=dffV7FSFzCM"),
    ]),
]


# --------------------------------------------------------------------------- #
def _esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def html(course, unit):
    """Het volledige Extra-paneel. Leeg als er voor deze unit geen lijst is."""
    groepen = BRONNEN.get((course, unit))
    if not groepen:
        # Nog geen bronnenlijst voor deze unit. Géén «link volgt» op de leerlingpagina
        # (CLAUDE.md §18): dan liever een kader dat de leerling écht ergens heen stuurt.
        return (
            '<h2 class="sec">Extra · seguir practicando</h2>\n    '
            '<p class="lead">Nog niet genoeg geoefend? Alles wat je nodig hebt staat al op deze '
            'pagina. <span class="gloss">Zo haal je er het meeste uit.</span></p>\n    '
            '<div class="card"><ul class="bronlijst">'
            '<li>🃏 <b>Vocabulario</b> — eerst de flashcards, dan «✍️ Escribe tú»: daar '
            'schrijf je de woorden zelf, zonder keuzelijst.</li>'
            '<li>🧠 <b>Gramática</b> — de visuele uitleg bovenaan, de invuloefeningen onderaan.</li>'
            '<li>🕹️ <b>Juegos</b> — elk spel trekt telkens een nieuwe reeks; opnieuw spelen '
            'levert dus andere items op.</li>'
            '<li>🎙️ <b>Hablar</b> — neem jezelf op, luister terug, doe het nog eens.</li>'
            '<li>📖 <b>Lectura</b> en 🎧 <b>Escuchar</b> — lees en luister met de taken erbij.</li>'
            '</ul></div>\n    '
            '<div class="card"><p>📄 In het boek verwijzen de QR-codes naar deze digitale '
            'pagina, telkens op het juiste ankerpunt.</p></div>')
    n = sum(len(v) for _t, v in groepen)
    uit = ['<h2 class="sec">Extra · bronnen</h2>',
           '<p class="lead">Wil je meer oefenen dan wat hier staat? Deze pagina\'s van '
           '<b>ProfeDeELE</b>, <b>Arche-ELE</b> en <b>My Daily Spanish</b> behandelen precies de '
           'onderwerpen van deze unidad. <span class="gloss">%d bronnen, geordend zoals de unit '
           'zelf. Ze openen in een nieuw tabblad.</span></p>' % n]

    spellen = (DESTACADO.get((course, unit)) or []) if TOON_DESTACADO else []
    for i, d in enumerate(spellen):
        uit.append(
            '<a class="destacado" href="%s" target="_blank" rel="noopener">'
            '<span class="dest-ico" aria-hidden="true">%s</span>'
            '<span class="dest-tekst">%s'
            '<span class="dest-titel">%s</span>'
            '<span class="dest-es">%s</span>'
            '<span class="dest-nl">%s</span>%s</span>'
            '<span class="dest-badge">%s</span></a>'
            % (_esc(d["url"]), d.get("ico", "🗝️"),
               # kicker en tip staan bij het eerste en het laatste spel: bij vier
               # kaarten onder elkaar wordt dezelfde regel vier keer herhalen ruis.
               ('<span class="dest-kicker">%s</span>' % _esc(d.get("kicker", DEST_KICKER))) if i == 0 else "",
               _esc(d["titel"]), _esc(d["es"]), _esc(d["nl"]),
               ('<span class="dest-tip">💡 %s</span>' % _esc(d.get("tip", DEST_TIP)))
               if i == len(spellen) - 1 else "",
               _esc(d["soort"])))
    for titel, items in groepen:
        uit.append('<div class="card brongroep"><h3>%s</h3><ul class="bronlijst">' % _esc(titel))
        for bron, naam, url in items:
            afk, ico = SITES.get(bron, ("", "🔗"))
            video = "youtube.com" in url or "youtu.be" in url
            uit.append(
                '<li><a href="%s" target="_blank" rel="noopener">%s %s</a>'
                '<span class="bronbadge %s">%s</span>%s</li>'
                % (_esc(url), ico, _esc(naam), afk.lower(), _esc(bron),
                   '<span class="bronsoort">video</span>' if video else ""))
        uit.append("</ul></div>")
    uit.append('<div class="card"><p>📄 In het boek verwijzen de QR-codes naar deze digitale '
               'pagina, telkens op het juiste ankerpunt.</p></div>')
    return "\n    ".join(uit)


CSS = r"""
/* Uitgelicht materiaal dat de hele unidad bestrijkt — mag opvallen, maar blijft
   binnen de cursuskleur; geen tweede accentkleur erbij. */
.destacado{display:flex;gap:16px;align-items:flex-start;text-decoration:none;color:var(--ink);
  background:linear-gradient(135deg,var(--gt),var(--card));border:2px solid var(--g);
  border-radius:16px;padding:18px 20px;margin:0 0 18px;position:relative}
.destacado:hover,.destacado:focus-visible{border-color:var(--gd);box-shadow:0 4px 18px rgba(0,0,0,.08)}
.destacado:focus-visible{outline:3px solid var(--gd);outline-offset:3px}
.dest-ico{font-size:34px;line-height:1;flex:none}
.dest-tekst{display:flex;flex-direction:column;gap:4px;min-width:0}
.dest-kicker{font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--gd)}
.dest-titel{font-family:var(--disp);font-size:21px;font-weight:800;color:var(--gd);line-height:1.15}
.dest-es{font-style:italic;font-size:14px}
.dest-nl{font-size:13px;color:var(--mut)}
.dest-tip{font-family:var(--hand,var(--body));font-size:13px;color:var(--gd);margin-top:4px}
.dest-badge{position:absolute;top:-11px;right:16px;background:var(--g);color:#fff;font-size:11px;
  font-weight:800;letter-spacing:.05em;padding:4px 12px;border-radius:999px;white-space:nowrap}
@media(max-width:520px){.destacado{flex-direction:column;gap:10px}.dest-badge{right:12px}}
.brongroep h3{font-family:var(--disp);color:var(--gd);margin:0 0 10px;font-size:16px}
.bronlijst{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:2px}
.bronlijst li{display:flex;align-items:center;gap:9px;flex-wrap:wrap;padding:7px 9px;border-radius:9px}
.bronlijst li:nth-child(odd){background:var(--gt)}
.bronlijst a{color:var(--ink);text-decoration:none;font-weight:600;flex:1 1 220px;min-width:0}
.bronlijst a:hover,.bronlijst a:focus-visible{color:var(--gd);text-decoration:underline}
.bronlijst a:focus-visible{outline:3px solid var(--gd);outline-offset:2px;border-radius:4px}
.bronbadge{font-size:10px;font-weight:800;letter-spacing:.04em;padding:3px 8px;border-radius:999px;
  background:var(--card);border:1.5px solid var(--line);color:var(--mut);white-space:nowrap;flex:none}
.bronsoort{font-size:10px;font-weight:700;color:var(--gd);background:var(--gt);
  border-radius:999px;padding:3px 8px;flex:none}
"""


if __name__ == "__main__":
    for (c, u), g in sorted(BRONNEN.items()):
        print("%s U%d — %d onderwerpen, %d bronnen" % (c, u, len(g), sum(len(v) for _t, v in g)))
        alle = [x[2] for _t, v in g for x in v]
        print("   unieke links: %d van %d" % (len(set(alle)), len(alle)))
