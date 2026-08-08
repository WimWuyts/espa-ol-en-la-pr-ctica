#!/usr/bin/env python3
"""Retos — de out-of-the-box oefeningen, één bron voor print, hub en PowerPoint.

Het reguliere oefenpakket is didactisch degelijk maar formeel eentonig: geteld
over de zeventien units staan er 63× «completa», 53× «escribe», 35× «empareja»
en 33× «clasifica». De retos vermijden die jassen bewust en werken met acht
ontwerplenzen (zie `02-huisstijl/reservoir/OEFENINGEN_OUT_OF_THE_BOX.md`).

Elke reto kiest ZELF zijn drager — niet alles hoort overal:

    soporte="print"  de oefening heeft papier nodig (info-gap met twee helften,
                     knipfiches, een noteertabel die je meeneemt naar buiten);
    soporte="hub"    de oefening heeft techniek nodig (opnemen en terugluisteren,
                     directe zelfcorrectie, een kaart die meekleurt);
    soporte="ppt"    de oefening is klassikaal en leeft op het grote scherm
                     (veiling, spelshow, bewegingsspel op signaal).

De niet-primaire dragers krijgen wél een verwijzing, nooit een halve kopie: een
veiling op papier naspelen werkt niet, een opnameoefening in print evenmin.

VELDEN
    id/num        C5-U0-RETO-03 · volgnummer in de doorlopende oefeningenrij
    seccion       waar de reto inhoudelijk thuishoort (bepaalt de plaats in print)
    ancla         sleutel voor het invoegpunt in de printcursus
    lente         de ontwerplens (zie het voorstel)
    forma/skill/tiempo/dificultad   badges, zoals bij elke activiteit
    gancho        het haakje — Spaans eerst, Nederlands eronder (CLAUDE.md §4)
    consigna      de opdracht zelf
    regla         DE beperking; zonder die regel is het een gewone oefening
    pasos         het verloop, [(es, nl), …]
    datos         de eigen inhoud (loten, fiches, items, woorden)
    clave         antwoordsleutel — docentendossier, nooit de leerlingpagina
    nota          aandachtspunt voor de leerkracht
"""

CURSO, UNIDAD = "C5", 0


# ---------------------------------------------------------------------------
# §1 · El alfabeto y la pronunciación
# ---------------------------------------------------------------------------

RETO_06 = {
    "id": "C5-U0-RETO-06", "num": 6, "curso": CURSO, "unidad": UNIDAD,
    "seccion": "§1.1", "ancla": "alfabeto", "soporte": "ppt",
    "nombre": "Radio Nombres",
    "lente": "📻 mediaformat",
    "forma": "🏫 Toda la clase", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Bienvenidos a Radio Nombres, el concurso donde solo cuentan las letras.",
    "gancho_nl": "Welkom bij Radio Namen — de spelshow waarin alleen de letters tellen.",
    "consigna_es": "Deletrea el nombre en diez segundos. Un punto por letra correcta, "
                   "menos un punto por cada duda.",
    "consigna_nl": "Spel de naam binnen tien seconden. Eén punt per correcte letternaam, "
                   "één punt aftrek per hapering.",
    "regla": "Je zegt de lettersnamen (efe, hache, uve doble), nooit de klanken. "
             "Wie «ffff» zegt in plaats van «efe», verliest de beurt.",
    "pasos": [
        ("Ronda 1 — los compañeros: deletrea el nombre de alguien de la clase.",
         "Ronde 1 — klasgenoten: spel de naam van iemand uit de klas."),
        ("Ronda 2 — las ciudades: el/la profe dice la ciudad, tú la deletreas.",
         "Ronde 2 — steden: de leerkracht zegt de stad, jij spelt ze."),
        ("Ronda 3 — las trampas: nombres flamencos con w, y, ij, j.",
         "Ronde 3 — de valstrikken: Vlaamse namen met w, y, ij, j."),
        ("Final — el nombre más largo de la clase, sin errores.",
         "Finale — de langste naam van de klas, foutloos."),
    ],
    "datos": {
        "ciudades": ["Zaragoza", "Cuenca", "Jaén", "Guadalajara", "Vigo", "Huelva"],
        "trampas": ["Wouter", "Yara", "Lieze", "Jeroen", "Xavier"],
        "letras_dificiles": [
            ("W", "uve doble", "in Wouter"), ("Y", "i griega / ye", "in Yara"),
            ("J", "jota", "in Jeroen"), ("H", "hache — zwijgt!", "in Huelva"),
            ("Z", "zeta", "in Zaragoza"), ("X", "equis", "in Xavier"),
        ],
    },
    "clave": [
        "Zaragoza = zeta-a-erre-a-ge-o-zeta-a  ·  Jaén = jota-a-e con tilde-ene",
        "Huelva = hache-u-e-ele-uve-a (de hache zwijgt, maar je spélt ze wél)",
        "Wouter = uve doble-o-u-te-e-erre  ·  Yara = i griega-a-erre-a",
        "Veelgemaakte fout: «be» en «uve» verwisselen. Laat leerlingen «be de burro» "
        "en «uve de vaca» zeggen zoals in Latijns-Amerika.",
    ],
    "nota": "Werkt het best met een echte timer op het scherm. De aftrek voor haperen "
            "klinkt streng, maar maakt juist dat leerlingen eerst denken en dan spreken.",
}

RETO_09 = {
    "id": "C5-U0-RETO-09", "num": 9, "curso": CURSO, "unidad": UNIDAD,
    "seccion": "§1.1", "ancla": "alfabeto", "soporte": "hub",
    "nombre": "Mi firma sonora",
    "lente": "✍️ creatieve beperking",
    "forma": "👤 Solo → 🏫 clase", "skill": "🗣️ Hablar",
    "tiempo": "± 8 min", "dificultad": "★★☆",
    "gancho_es": "Tu nombre también suena. Conviértelo en una firma de cinco segundos.",
    "gancho_nl": "Je naam klínkt ook. Maak er een geluidshandtekening van vijf seconden van.",
    "consigna_es": "Graba tu nombre deletreado, con ritmo, y alarga un solo sonido. "
                   "La clase adivina de quién es.",
    "consigna_nl": "Neem je gespelde naam op, met ritme, en rek precies één klank uit. "
                   "De klas raadt van wie ze is.",
    "regla": "Exact vijf seconden en precies één uitgerekte klank. Je mag je naam "
             "niet gewoon uitspreken — alleen spellen.",
    "pasos": [
        ("Escucha el modelo: «ese — a — eme… Sssssam».",
         "Luister naar het model: «ese — a — eme… Sssssam»."),
        ("Elige qué sonido alargas. ¿El más raro? ¿El más bonito?",
         "Kies welke klank je uitrekt. De vreemdste? De mooiste?"),
        ("Graba, escúchate, vuelve a grabar. Mínimo dos intentos.",
         "Neem op, luister terug, neem opnieuw op. Minstens twee pogingen."),
        ("La clase escucha las firmas en orden aleatorio y adivina.",
         "De klas beluistert de handtekeningen door elkaar en raadt."),
    ],
    "datos": {
        "modelos": [
            ("Sam", "ese — a — eme… Sssssam"),
            ("Lucía", "ele — u — ce — i con tilde — a… Luthííía"),
            ("Jeroen", "jota — e — erre — o — e — ene… Jjjjeroen"),
        ],
    },
    "clave": [
        "Er is geen fout antwoord. Beoordeel op: (1) correcte letternamen, "
        "(2) hoorbaar ritme, (3) één — en maar één — uitgerekte klank.",
        "Wie zijn naam gewoon uitspreekt in plaats van spelt, doet het opnieuw.",
    ],
    "nota": "Dit is de eerste opname van het jaar. Hou het licht: de opdracht is "
            "speels genoeg dat niemand zich blootgeeft, en iedereen hoort meteen "
            "zijn eigen stem in het Spaans.",
}

RETO_02 = {
    "id": "C5-U0-RETO-02", "num": 2, "curso": CURSO, "unidad": UNIDAD,
    "seccion": "§1.2", "ancla": "sonidos", "soporte": "ppt",
    "nombre": "La subasta de sonidos",
    "lente": "🔓 puzzel & escape",
    "forma": "👨‍👩‍👧 En equipos", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Cada equipo tiene cien puntos. Se subastan ocho lotes de sonidos.",
    "gancho_nl": "Elk team heeft honderd punten. Er worden acht klankloten geveild.",
    "consigna_es": "Puja por un lote. Si lo ganas, pronuncia las dos palabras y di si "
                   "suenan igual o diferente. ¿Acertáis? Ganáis el valor del lote. "
                   "¿Falláis? Perdéis lo que pujasteis.",
    "consigna_nl": "Bied op een lot. Win je het, dan spreek je beide woorden uit en zeg je "
                   "of ze hetzelfde of verschillend klinken. Juist? Je wint de waarde van "
                   "het lot. Fout? Je verliest je bod.",
    "regla": "Je mag pas bieden ná het horen van het lot, en je mag niet overleggen "
             "terwijl je biedt. De duurste loten zijn de valstrikken.",
    "pasos": [
        ("El/la profe lee el lote en voz alta, una sola vez.",
         "De leerkracht leest het lot één keer hardop voor."),
        ("Los equipos pujan por turnos. El más alto se lo lleva.",
         "De teams bieden om beurten. De hoogste bieder krijgt het lot."),
        ("El equipo pronuncia y decide: ¿igual o diferente?",
         "Het team spreekt uit en beslist: gelijk of verschillend?"),
        ("Se revela la respuesta y la regla que hay detrás.",
         "Het antwoord wordt onthuld, samen met de regel erachter."),
    ],
    "datos": {
        # (lot, woord A, woord B, klinkt gelijk?, regel, waarde)
        "lotes": [
            (1, "gato", "gente", False, "g + a/o/u = harde g · g + e/i = keelklank (jota)", 10),
            (2, "queso", "cero", False, "qu = k · c + e/i = th (Spanje) of s (Amerika)", 10),
            (3, "hola", "ola", True, "de hache zwijgt altijd — de twee woorden klinken identiek", 25),
            (4, "perro", "pero", False, "rr = rollende r · r = één tik", 15),
            (5, "vino", "bino", True, "v en b klinken in het Spaans hetzelfde", 25),
            (6, "guitarra", "gitano", False, "gui = harde g (u zwijgt) · gi = keelklank", 15),
            (7, "año", "ano", False, "ñ is een eigen letter met een eigen klank (nj)", 20),
            (8, "casa", "caza", False, "s = s · z = th (Spanje). In Amerika klinken ze wél gelijk", 20),
        ],
    },
    "clave": [
        "Lot 1 diferente · 2 diferente · 3 IGUAL · 4 diferente · 5 IGUAL · "
        "6 diferente · 7 diferente · 8 diferente in Spanje, gelijk in Amerika",
        "De twee duurste loten (3 en 5) zijn precies de twee die Nederlandstaligen "
        "het vaakst fout hebben: zij hóren een h en een v die er niet zijn.",
        "Lot 8 heeft geen enkel juist antwoord zonder de vraag «waar?» — accepteer "
        "beide, mits het team zijn keuze motiveert.",
    ],
    "nota": "Zet het puntentotaal zichtbaar op het bord. De spanning zit in lot 3 en 5: "
            "teams die daar hoog bieden zonder de regel te kennen, verliezen alles.",
}

RETO_04 = {
    "id": "C5-U0-RETO-04", "num": 4, "curso": CURSO, "unidad": UNIDAD,
    "seccion": "§1.3", "ancla": "sonido_letra", "soporte": "hub",
    "nombre": "El detector de mentiras ortográficas",
    "lente": "🕵️ forensisch",
    "forma": "👥 En parejas", "skill": "👁️ Leer",
    "tiempo": "± 10 min", "dificultad": "★★★",
    "gancho_es": "Catorce palabras. Algunas rompen una regla del español. ¿Cuáles?",
    "gancho_nl": "Veertien woorden. Sommige breken een Spaanse spellingsregel. Welke?",
    "consigna_es": "Marca las palabras imposibles y di QUÉ regla rompen. No basta con "
                   "señalar: hay que acusar con pruebas.",
    "consigna_nl": "Kruis de onmogelijke woorden aan en zeg WELKE regel ze breken. "
                   "Aanwijzen volstaat niet — je moet je beschuldiging bewijzen.",
    "regla": "Bij elk woord dat je onmogelijk noemt, moet je de regel erbij zeggen. "
             "Een beschuldiging zonder regel telt als fout, ook als het woord echt fout is.",
    "pasos": [
        ("Solo: marca las que te parecen imposibles.",
         "Alleen: kruis aan wat je onmogelijk lijkt."),
        ("En parejas: comparad y buscad la regla de cada una.",
         "Per twee: vergelijk en zoek bij elk de regel."),
        ("Cuidado: hay una palabra que parece falsa y es correcta.",
         "Let op: er zit één woord bij dat vals lijkt maar juist is."),
    ],
    "datos": {
        # (woord, is_mogelijk, regel/uitleg)
        "items": [
            ("queso", True, "qu + e — correct"),
            ("qeso", False, "de q staat in het Spaans altijd met een u: qu"),
            ("ghitarra", False, "de combinatie gh bestaat niet; het is guitarra"),
            ("guitarra", True, "gui = harde g, de u zwijgt — correct"),
            ("jamón", True, "aguda op -n draagt een tilde — correct"),
            ("jamon", False, "een aguda die op -n eindigt, moet een tilde krijgen"),
            ("España", True, "ñ — correct"),
            ("Espanña", False, "nñ bestaat niet; de ñ is één letter"),
            ("plaza", True, "z + a — correct"),
            ("plassa", False, "de dubbele s bestaat niet in het Spaans"),
            ("cinco", True, "c + i — correct"),
            ("kinco", False, "de k komt alleen voor in leenwoorden (kilo, kiwi)"),
            ("hola", True, "de hache zwijgt maar wordt geschreven — correct"),
            ("ola", True, "VALSTRIK: bestaat écht en betekent «golf»"),
        ],
    },
    "clave": [
        "Onmogelijk (6): qeso · ghitarra · jamon · Espanña · plassa · kinco",
        "Mogelijk (8): queso · guitarra · jamón · España · plaza · cinco · hola · ola",
        "«ola» is de valstrik: het lijkt «hola» zonder h, maar het is een echt woord "
        "(golf). Wie het aankruist, leert de duurste les van deze oefening.",
    ],
    "nota": "De regel-eis is de kern. Zonder die eis wordt het gokken; mét die eis "
            "moeten leerlingen de klanktabel van §1.2 echt gebruiken.",
}


# ---------------------------------------------------------------------------
# §2 · El acento
# ---------------------------------------------------------------------------

RETO_05 = {
    "id": "C5-U0-RETO-05", "num": 5, "curso": CURSO, "unidad": UNIDAD,
    "seccion": "§2.3", "ancla": "acento", "soporte": "ppt",
    "nombre": "La tilde en el semáforo",
    "lente": "🔓 puzzel & escape",
    "forma": "🏫 Toda la clase · de pie", "skill": "👂 Escuchar",
    "tiempo": "± 10 min", "dificultad": "★★☆",
    "gancho_es": "De pie. La clase es un semáforo: izquierda, centro, derecha.",
    "gancho_nl": "Rechtstaan. De klas is een verkeerslicht: links, midden, rechts.",
    "consigna_es": "Oyes una palabra. Vas a la izquierda si es aguda, al centro si es "
                   "llana, a la derecha si es esdrújula. Tienes tres segundos.",
    "consigna_nl": "Je hoort een woord. Links = aguda, midden = llana, rechts = esdrújula. "
                   "Je hebt drie seconden.",
    "regla": "Je beslist op wat je hóórt, niet op wat je ziet — het woord staat pas "
             "op het scherm ná de beslissing. Wie te laat is, gaat zitten.",
    "pasos": [
        ("Calentamiento: tres palabras con el escrito a la vista.",
         "Opwarming: drie woorden mét het schriftbeeld erbij."),
        ("El juego: solo la voz. Tres segundos por palabra.",
         "Het spel: alleen de stem. Drie seconden per woord."),
        ("Ronda final: los que quedan de pie deciden a la vez.",
         "Finaleronde: wie nog rechtstaat, beslist tegelijk."),
        ("Después: ¿qué palabras engañaron a más gente? ¿Por qué?",
         "Achteraf: welke woorden misleidden de meesten? Waarom?"),
    ],
    "datos": {
        # (woord, type, klemtoonlettergreep)
        "palabras": [
            ("café", "aguda", "fé"), ("casa", "llana", "ca"), ("México", "esdrújula", "Mé"),
            ("teléfono", "esdrújula", "lé"), ("Perú", "aguda", "rú"), ("número", "esdrújula", "nú"),
            ("mesa", "llana", "me"), ("jamón", "aguda", "món"), ("sábado", "esdrújula", "sá"),
            ("papel", "aguda", "pel"), ("lápiz", "llana", "lá"), ("música", "esdrújula", "mú"),
            ("reloj", "aguda", "loj"), ("ventana", "llana", "ta"), ("plátano", "esdrújula", "plá"),
        ],
    },
    "clave": [
        "aguda (links): café · Perú · jamón · papel · reloj",
        "llana (midden): casa · mesa · lápiz · ventana",
        "esdrújula (rechts): México · teléfono · número · sábado · música · plátano",
        "De twee lastigste: «papel» en «reloj» dragen géén tilde maar zijn wél aguda "
        "(ze eindigen niet op klinker, -n of -s). «lápiz» draagt er wél een en is llana.",
    ],
    "nota": "Het lichaam onthoudt wat het hoofd vergeet. Speel minstens twee rondes: "
            "in de tweede ronde zie je de klemtoon al door de klas heen bewegen.",
}


# ---------------------------------------------------------------------------
# §3 · Los números
# ---------------------------------------------------------------------------

RETO_03 = {
    "id": "C5-U0-RETO-03", "num": 3, "curso": CURSO, "unidad": UNIDAD,
    "seccion": "§3.4", "ancla": "numeros", "soporte": "print",
    "nombre": "El GPS roto",
    "lente": "🎭 simulatie met beperking",
    "forma": "👥 En parejas (A + B)", "skill": "👂 Escuchar",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Tu GPS ya no dibuja el mapa. Solo dice números. Tu compañero/a sí "
                 "tiene el mapa, pero no oye nada.",
    "gancho_nl": "Je gps tekent geen kaart meer. Hij zegt alleen nog getallen. Je "
                 "partner heeft wél de kaart, maar hoort niets.",
    "consigna_es": "A lee la ruta en voz alta. B calcula y dice a qué ciudad llega. "
                   "Un número mal entendido y acabáis en otra provincia.",
    "consigna_nl": "A leest de route hardop. B rekent en zegt in welke stad je uitkomt. "
                   "Eén verkeerd verstaan getal en je zit in de verkeerde provincie.",
    "regla": "A mag de kaart niet zien en B mag de route niet lezen. Herhalen mag, "
             "maar alleen in het Spaans: «¿Puedes repetir, por favor?»",
    "pasos": [
        ("A lee: «Sal del kilómetro X, avanza Y kilómetros.»",
         "A leest: «Vertrek bij kilometer X, rijd Y kilometer verder.»"),
        ("B calcula en silencio y busca la ciudad en su mapa.",
         "B rekent in stilte en zoekt de stad op zijn kaart."),
        ("B dice la ciudad. A comprueba con su clave.",
         "B zegt de stad. A controleert met zijn sleutel."),
        ("Cambiad de papel después de tres rutas.",
         "Wissel van rol na drie routes."),
    ],
    "datos": {
        # de kilometerstrook die B krijgt
        "ciudades": [(7, "Sevilla"), (15, "Madrid"), (24, "Bilbao"), (38, "València"),
                     (46, "Zaragoza"), (59, "Málaga"), (71, "Toledo"), (88, "Granada"),
                     (96, "Barcelona")],
        # de routes die A voorleest: (start, verplaatsing, richting, doel)
        "rutas": [
            (7, 8, "adelante", 15, "Madrid"),
            (46, 13, "adelante", 59, "Málaga"),
            (88, 17, "atrás", 71, "Toledo"),
            (24, 22, "adelante", 46, "Zaragoza"),
            (96, 58, "atrás", 38, "València"),
            (15, 9, "adelante", 24, "Bilbao"),
        ],
    },
    "clave": [
        "Ruta 1: 7 + 8 = 15 → Madrid", "Ruta 2: 46 + 13 = 59 → Málaga",
        "Ruta 3: 88 − 17 = 71 → Toledo", "Ruta 4: 24 + 22 = 46 → Zaragoza",
        "Ruta 5: 96 − 58 = 38 → València", "Ruta 6: 15 + 9 = 24 → Bilbao",
        "Ruta 5 is de moeilijkste: «noventa y seis» en «cincuenta y ocho» in één zin.",
    ],
    "nota": "Knip het blad op de vouwlijn of laat de leerlingen rug aan rug zitten. "
            "Het rekenwerk is bewust licht — de moeilijkheid zit in het hóren.",
}

RETO_08 = {
    "id": "C5-U0-RETO-08", "num": 8, "curso": CURSO, "unidad": UNIDAD,
    "seccion": "§3.4", "ancla": "numeros", "soporte": "print",
    "nombre": "Números que salvan",
    "lente": "🔬 onderzoek & data",
    "forma": "👥 En parejas", "skill": "👂 Escuchar",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Un prefijo, un número. Con esos dos datos se llama a cualquier parte "
                 "del mundo hispano.",
    "gancho_nl": "Een landcode en een nummer. Met die twee gegevens bel je overal in "
                 "de Spaanstalige wereld.",
    "consigna_es": "Escucha los prefijos internacionales, anótalos y luego haz la "
                   "llamada: di de dónde llamas y deletrea tu nombre.",
    "consigna_nl": "Luister naar de landcodes, noteer ze en voer daarna het gesprek: "
                   "zeg vanwaar je belt en spel je naam.",
    "regla": "Je noteert de cijfers als woord, niet als cijfer: «más treinta y cuatro», "
             "niet «+34». Daarmee wordt getallen kennen ineens getallen schríjven.",
    "pasos": [
        ("Escucha y anota los ocho prefijos.",
         "Luister en noteer de acht landcodes."),
        ("Comprueba con tu compañero/a: ¿coinciden?",
         "Vergelijk met je partner: komen ze overeen?"),
        ("Simulación: A llama, B contesta. «Buenos días, llamo desde…»",
         "Simulatie: A belt, B neemt op. «Goedemorgen, ik bel vanuit…»"),
    ],
    "datos": {
        # internationale landnummers (ITU) — stabiel en verifieerbaar
        "prefijos": [("España", 34), ("México", 52), ("Colombia", 57), ("Perú", 51),
                     ("Argentina", 54), ("Chile", 56), ("Cuba", 53), ("Guatemala", 502)],
        "marco": ["Buenos días, llamo desde Bélgica.", "Me llamo… ¿Cómo se escribe?",
                  "Se escribe: …", "Mi prefijo es el más treinta y dos.", "¡Gracias! ¡Hasta luego!"],
    },
    "clave": [
        "España +34 · México +52 · Colombia +57 · Perú +51",
        "Argentina +54 · Chile +56 · Cuba +53 · Guatemala +502",
        "België = +32 — dat is het getal dat de leerling zelf moet kunnen zeggen.",
        "Guatemala (502) is de enige met drie cijfers: «quinientos dos» of "
        "«cinco-cero-dos». Beide mogen; laat leerlingen kiezen en motiveren.",
    ],
    "nota": "Landnummers zijn ITU-codes en veranderen niet. Wil je er ook noodnummers "
            "bij nemen, controleer die dan vlak vóór gebruik: die wijzigen wél.",
}


# ---------------------------------------------------------------------------
# §4 · Saludos y lengua de clase
# ---------------------------------------------------------------------------

RETO_01 = {
    "id": "C5-U0-RETO-01", "num": 1, "curso": CURSO, "unidad": UNIDAD,
    "seccion": "§4.3", "ancla": "saludos", "soporte": "hub",
    "nombre": "La cabina de doblaje",
    "lente": "🎭 simulatie met beperking",
    "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Cuatro situaciones, la misma frase. Solo cambia cómo la dices.",
    "gancho_nl": "Vier situaties, dezelfde zin. Alleen de manier waarop je hem zegt, verandert.",
    "consigna_es": "Graba «¡Hola! Buenos días» cuatro veces, una por situación. "
                   "La clase escucha y adivina cuál es cuál.",
    "consigna_nl": "Neem «¡Hola! Buenos días» vier keer op, één per situatie. "
                   "De klas luistert en raadt welke welke is.",
    "regla": "Je mag geen enkel ander woord gebruiken. Alleen toon, tempo en volume "
             "vertellen het verhaal. Wie iets toevoegt, begint opnieuw.",
    "pasos": [
        ("Lee las cuatro situaciones. No las digas en voz alta todavía.",
         "Lees de vier situaties. Zeg ze nog niet hardop."),
        ("Graba las cuatro versiones en orden desordenado.",
         "Neem de vier versies op, in willekeurige volgorde."),
        ("Escúchate. ¿Se distinguen? Si no, vuelve a grabar.",
         "Luister terug. Zijn ze te onderscheiden? Zo niet: opnieuw."),
        ("La clase escucha y numera. ¿Cuántas aciertan?",
         "De klas luistert en nummert. Hoeveel raden ze juist?"),
    ],
    "datos": {
        "situaciones": [
            ("Llegas tarde a clase y todos te miran.",
             "Je komt te laat binnen en iedereen kijkt.", "zacht, snel, verontschuldigend"),
            ("Ves a tu mejor amigo/a después de un verano entero.",
             "Je ziet je beste vriend(in) na een hele zomer.", "luid, hoog, uitgerekt"),
            ("Contestas al teléfono a las siete de la mañana.",
             "Je neemt de telefoon op om zeven uur 's ochtends.", "traag, laag, slaperig"),
            ("Eres el/la recepcionista de un hotel de lujo.",
             "Je bent receptionist(e) in een luxehotel.", "helder, neutraal, afgemeten"),
        ],
    },
    "clave": [
        "Er is geen juiste uitvoering, wel een herkenbare. Beoordeel op: kan de klas "
        "de vier uit elkaar houden zonder de situaties te kennen?",
        "Situatie 3 (telefoon) is de makkelijkste om te herkennen, situatie 1 en 4 "
        "worden het vaakst verwisseld — beide zijn stil en beheerst.",
        "Wijs erop dat het Spaans van «Buenos días» in situatie 4 volledig wordt "
        "uitgesproken, terwijl het in situatie 1 samenvalt tot «uenos días».",
    ],
    "nota": "Dit is de enige oefening van U0 waarin betekenis volledig los staat van "
            "woordenschat. Leerlingen die nog niets kunnen zeggen, kunnen hier al iets "
            "communiceren — dat is het punt.",
}

RETO_10 = {
    "id": "C5-U0-RETO-10", "num": 10, "curso": CURSO, "unidad": UNIDAD,
    "seccion": "§4.3", "ancla": "saludos", "soporte": "print",
    "nombre": "El pasaporte secreto",
    "lente": "🕵️ forensisch",
    "forma": "🏫 Toda la clase · de pie", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Llevas una ciudad en el bolsillo. Nadie puede verla.",
    "gancho_nl": "Je draagt een stad op zak. Niemand mag ze zien.",
    "consigna_es": "Descubre la ciudad de tu compañero/a solo con preguntas de sí o no "
                   "sobre letras y números. Máximo ocho preguntas.",
    "consigna_nl": "Ontdek de stad van je klasgenoot met alleen ja/nee-vragen over "
                   "letters en getallen. Maximaal acht vragen.",
    "regla": "Je mag niet vragen in welk land de stad ligt, en je mag geen letter "
             "raden die je nog niet hebt uitgesloten. Alleen tellen en spellen.",
    "pasos": [
        ("Coge una ficha. No la enseñes a nadie.",
         "Neem een fiche. Laat ze aan niemand zien."),
        ("Busca una pareja. Preguntad por turnos.",
         "Zoek een partner. Vraag om beurten."),
        ("Anota cada respuesta: así se descarta, no se adivina.",
         "Noteer elk antwoord: zo sluit je uit in plaats van te gokken."),
        ("¿Ocho preguntas y sin respuesta? Tu compañero/a gana.",
         "Acht vragen en nog geen antwoord? Je partner wint."),
    ],
    "datos": {
        "fichas": ["Sevilla", "Madrid", "Bogotá", "Lima", "Quito", "La Habana",
                   "Montevideo", "Asunción", "San José", "Ciudad de México",
                   "Buenos Aires", "Santiago"],
        "banco_preguntas": [
            ("¿Tiene más de siete letras?", "Heeft ze meer dan zeven letters?"),
            ("¿Empieza por vocal?", "Begint ze met een klinker?"),
            ("¿Lleva tilde?", "Draagt ze een accent?"),
            ("¿Son dos palabras?", "Zijn het twee woorden?"),
            ("¿Tiene una eñe?", "Zit er een ñ in?"),
            ("¿Tiene doble ele?", "Zit er een dubbele l in?"),
            ("¿Termina en a?", "Eindigt ze op een a?"),
            ("¿Tiene menos de seis letras?", "Heeft ze minder dan zes letters?"),
        ],
    },
    "clave": [
        "Met tilde: Bogotá · Asunción · San José · Ciudad de México",
        "Twee of meer woorden: La Habana · San José · Ciudad de México · Buenos Aires",
        "Met ñ: Asunción — met dubbele l: Sevilla",
        "Kortste: Lima en Quito (4 en 5 letters) · langste: Ciudad de México",
        "Efficiëntste openingsvraag: «¿Son dos palabras?» — die halveert het veld meteen.",
    ],
    "nota": "Print de fiches op de laatste bladzijde van de sectie, om uit te knippen. "
            "Twaalf fiches volstaan voor een klas van vierentwintig: twee leerlingen "
            "per stad maakt het spel juist spannender.",
}

RETO_07 = {
    "id": "C5-U0-RETO-07", "num": 7, "curso": CURSO, "unidad": UNIDAD,
    "seccion": "Cultura · A.2", "ancla": "cultura", "soporte": "hub",
    "nombre": "El mapa que crece",
    "lente": "🤝 bemiddelen · coöperatief",
    "forma": "🏫 Toda la clase", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "El mapa está gris. Cada país que alguien pronuncia bien, se enciende.",
    "gancho_nl": "De kaart is grijs. Elk land dat iemand goed uitspreekt, licht op.",
    "consigna_es": "Entre toda la clase, encended los veintiún países hispanohablantes "
                   "en una sola clase. No hay puntuación individual.",
    "consigna_nl": "Doe samen als klas de eenentwintig Spaanstalige landen oplichten, "
                   "in één les. Er is geen individuele score.",
    "regla": "Niemand mag twee landen na elkaar doen, en een land telt pas als "
             "iemand anders uit de klas bevestigt dat het correct klonk. "
             "Het doel is van de klas, niet van jou.",
    "pasos": [
        ("Haz clic en un país gris. Aparece su nombre.",
         "Klik op een grijs land. De naam verschijnt."),
        ("Dilo en voz alta. Otra persona confirma.",
         "Zeg het hardop. Iemand anders bevestigt."),
        ("El país se enciende y el contador sube.",
         "Het land licht op en de teller gaat omhoog."),
        ("¿Veintiuno de veintiuno? La clase lo ha conseguido.",
         "Eenentwintig op eenentwintig? Dan heeft de klas het gehaald."),
    ],
    "datos": {
        # ISO3 zoals in mundo_map_real.svg + de klemtoon die leerlingen missen
        "paises": [
            ("ESP", "España", "Es-PA-ña"), ("MEX", "México", "MÉ-xi-co"),
            ("GTM", "Guatemala", "Gua-te-MA-la"), ("HND", "Honduras", "Hon-DU-ras"),
            ("SLV", "El Salvador", "El Sal-va-DOR"), ("NIC", "Nicaragua", "Ni-ca-RA-gua"),
            ("CRI", "Costa Rica", "Cos-ta RI-ca"), ("PAN", "Panamá", "Pa-na-MÁ"),
            ("CUB", "Cuba", "CU-ba"), ("DOM", "República Dominicana", "Do-mi-ni-CA-na"),
            ("PRI", "Puerto Rico", "Puer-to RI-co"), ("VEN", "Venezuela", "Ve-ne-ZUE-la"),
            ("COL", "Colombia", "Co-LOM-bia"), ("ECU", "Ecuador", "E-cua-DOR"),
            ("PER", "Perú", "Pe-RÚ"), ("BOL", "Bolivia", "Bo-LI-via"),
            ("PRY", "Paraguay", "Pa-ra-GUAY"), ("URY", "Uruguay", "U-ru-GUAY"),
            ("ARG", "Argentina", "Ar-gen-TI-na"), ("CHL", "Chile", "CHI-le"),
            ("GNQ", "Guinea Ecuatorial", "Gui-NE-a E-cua-to-RIAL"),
        ],
    },
    "clave": [
        "Eenentwintig landen waar Spaans een officiële taal is. Puerto Rico telt mee "
        "als Spaanstalig gebied, al is het geen onafhankelijk land.",
        "De drie die het vaakst fout gaan: Guinea Ecuatorial (het enige in Afrika), "
        "Paraguay/Uruguay (klemtoon op -GUAY, niet op GUA-) en Panamá (tilde!).",
        "Vergeet niet: in de Verenigde Staten wonen meer Spaanstaligen dan in Spanje, "
        "maar het is er geen officiële taal — daarom licht dat land niet op.",
    ],
    "nota": "Zet de teller op het scherm. De coöperatieve vorm is bewust: in de eerste "
            "les van het jaar wil je dat de klas iets sámen haalt, niet dat er al een "
            "ranglijst ontstaat.",
}


# ---------------------------------------------------------------------------
# Register + zelfcontrole
# ---------------------------------------------------------------------------

# ===========================================================================
# C5 · U1 — ¿Quién eres?  (parada: Madrid)
# ===========================================================================

U1 = 1

# ---------------------------------------------------------------------------
# §1 · Tus datos personales
# ---------------------------------------------------------------------------

U1_RETO_02 = {
    "id": "C5-U1-RETO-02", "num": 2, "curso": "C5", "unidad": U1,
    "seccion": "§1.2", "ancla": "datos", "soporte": "print",
    "nombre": "Identidad prestada",
    "lente": "🎭 simulatie met beperking",
    "forma": "🏫 Toda la clase", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Hoy no eres tú. Coge una ficha y preséntate como esa persona.",
    "gancho_nl": "Vandaag ben jij het niet. Neem een fiche en stel je voor als die persoon.",
    "consigna_es": "Preséntate en primera persona con los datos de la ficha. La clase "
                   "escucha y busca quién eres entre las doce fichas de la pared.",
    "consigna_nl": "Stel je voor in de ik-vorm met de gegevens van de fiche. De klas "
                   "luistert en zoekt wie je bent tussen de twaalf fiches op het bord.",
    "regla": "Alles in de ik-vorm, ook al ben jij het niet, en je mag de naam op je "
             "fiche niet zeggen. Eén keer «él es» of «ella vive» en je bent ontmaskerd.",
    "pasos": [
        ("Coge una ficha al azar. No la enseñes.",
         "Neem een willekeurige fiche. Laat ze niet zien."),
        ("Prepara cinco frases: nombre no, pero sí edad, país, ciudad y lenguas.",
         "Bereid vijf zinnen voor: geen naam, wel leeftijd, land, stad en talen."),
        ("Preséntate a la clase. La clase señala la ficha que cree que es.",
         "Stel je voor aan de klas. De klas wijst de fiche aan waarvan ze denkt dat het is."),
        ("¿Te han encontrado? Di por fin tu nombre prestado.",
         "Gevonden? Zeg dan eindelijk je geleende naam."),
    ],
    "datos": {
        "fichas": [
            ("Aitana", 16, "España", "Madrid", "español, inglés"),
            ("Bilal", 17, "Marruecos", "Tánger", "árabe, francés, español"),
            ("Camila", 15, "Colombia", "Medellín", "español"),
            ("Dries", 16, "Bélgica", "Amberes", "neerlandés, inglés, español"),
            ("Elena", 18, "Argentina", "Rosario", "español, italiano"),
            ("Fabio", 15, "Italia", "Nápoles", "italiano, español"),
            ("Gabriela", 17, "México", "Puebla", "español, náhuatl"),
            ("Hugo", 16, "Perú", "Arequipa", "español, quechua"),
            ("Inés", 14, "España", "Bilbao", "español, euskera"),
            ("Joaquín", 18, "Chile", "Valparaíso", "español, inglés"),
            ("Karim", 17, "Bélgica", "Gante", "neerlandés, árabe, francés"),
            ("Lucía", 16, "España", "Sevilla", "español, inglés"),
        ],
        "marco": ["Me llamo…  (¡no lo digas!)", "Tengo … años.", "Soy de …",
                  "Vivo en …", "Hablo … y …"],
    },
    "clave": [
        "Er is geen fout antwoord — wel een fout perspectief. Let bij het luisteren "
        "vooral op: valt de leerling terug in de derde persoon?",
        "Fiches met dezelfde leeftijd (Aitana/Dries/Lucía = 16) dwingen de klas om "
        "door te luisteren tot het land of de stad valt.",
        "Karim en Dries zijn allebei Belgen: alleen de stad en de talen onderscheiden ze.",
    ],
    "nota": "Hang de twaalf fiches vooraf op het bord, zodat de klas iets heeft om naar "
            "te wijzen. Zonder dat visuele anker wordt het gokken in plaats van luisteren.",
}

U1_RETO_03 = {
    "id": "C5-U1-RETO-03", "num": 3, "curso": "C5", "unidad": U1,
    "seccion": "§1.2", "ancla": "datos", "soporte": "print",
    "nombre": "El censo de la clase",
    "lente": "🔬 onderzoek & data",
    "forma": "👨‍👩‍👧 En grupos", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★☆",
    "gancho_es": "¿Quiénes sois, en números? Haced el censo de vuestra propia clase.",
    "gancho_nl": "Wie zijn jullie, in cijfers? Maak de volkstelling van je eigen klas.",
    "consigna_es": "Recoged los datos, dibujad el gráfico y escribid tres conclusiones "
                   "con «somos» y «son».",
    "consigna_nl": "Verzamel de gegevens, teken de grafiek en schrijf drie conclusies "
                   "met «somos» en «son».",
    "regla": "Elke conclusie moet een écht getal uit jullie grafiek bevatten en met "
             "«somos» of «son» beginnen. «Muchos alumnos hablan inglés» telt niet — "
             "«Somos catorce que hablamos inglés» wel.",
    "pasos": [
        ("Elegid una pregunta por grupo: edad, lenguas, ciudad o transporte.",
         "Kies één vraag per groep: leeftijd, talen, stad of vervoer."),
        ("Preguntad a toda la clase en español. Anotad con palitos.",
         "Bevraag de hele klas in het Spaans. Turf de antwoorden."),
        ("Dibujad el gráfico de barras con los números reales.",
         "Teken de staafgrafiek met de echte cijfers."),
        ("Escribid tres conclusiones y presentadlas en treinta segundos.",
         "Schrijf drie conclusies en presenteer ze in dertig seconden."),
    ],
    "datos": {
        "preguntas": [
            ("¿Cuántos años tienes?", "14 · 15 · 16 · 17 · 18"),
            ("¿Qué lenguas hablas?", "neerlandés · francés · inglés · español · otra"),
            ("¿Dónde vives?", "en la ciudad · en un pueblo · en el campo"),
            ("¿Cómo vienes al instituto?", "en bici · a pie · en bus · en coche · en tren"),
        ],
        "marco": ["Somos … alumnos en total.", "Somos … que …",
                  "… alumnos son de …", "La mayoría son …", "Solo … es …"],
    },
    "clave": [
        "De cijfers zijn per klas anders — controleer niet het antwoord maar de vórm.",
        "Veelgemaakte fout: «somos» met een enkelvoudig getal («somos uno»). "
        "Bij één persoon hoort «solo uno es…» of «solo una alumna…».",
        "Tweede valstrik: «son» vergeten te laten meebewegen — «cinco alumnos ES de "
        "Gante» in plaats van «SON de Gante».",
        "Wiskundig: laat de staven optellen tot het klastotaal; klopt het niet, dan is "
        "er iemand vergeten of dubbel geteld.",
    ],
    "nota": "Dit is de eerste keer dat de klas met echte eigen data werkt. De grafiek "
            "mag met de hand: het gaat om de conclusie, niet om de vormgeving.",
}

U1_RETO_09 = {
    "id": "C5-U1-RETO-09", "num": 9, "curso": "C5", "unidad": U1,
    "seccion": "§1.2", "ancla": "datos", "soporte": "ppt",
    "nombre": "Perfil para el algoritmo",
    "lente": "⚖️ onderhandeling & dilemma",
    "forma": "🏫 Toda la clase", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Escribe tu perfil. Hoy la clase es el algoritmo, y tiene que justificarse.",
    "gancho_nl": "Schrijf je profiel. Vandaag is de klas het algoritme — en het moet zich "
                 "verantwoorden.",
    "consigna_es": "El algoritmo propone parejas de intercambio. Cada propuesta se defiende "
                   "con «son… porque…». Sin razón, no hay pareja.",
    "consigna_nl": "Het algoritme stelt uitwisselingsduo's voor. Elk voorstel wordt verdedigd "
                   "met «son… porque…». Zonder reden geen match.",
    "regla": "Het algoritme mag niemand koppelen op naam of op wie bevriend is. Alleen "
             "gegevens uit de profielen tellen, en de reden moet met «son» of «tienen» "
             "geformuleerd worden.",
    "pasos": [
        ("Escribe tu perfil en cuatro frases. Sin nombre.",
         "Schrijf je profiel in vier zinnen. Zonder naam."),
        ("Los perfiles van al azar a la pizarra, numerados.",
         "De profielen gaan willekeurig en genummerd op het bord."),
        ("El algoritmo (tres alumnos) propone parejas y las justifica.",
         "Het algoritme (drie leerlingen) stelt duo's voor en verantwoordt ze."),
        ("La clase acepta o rechaza. ¿Rechazo? Hay que dar una razón mejor.",
         "De klas aanvaardt of verwerpt. Verworpen? Dan moet er een beter argument komen."),
    ],
    "datos": {
        "marco_perfil": ["Tengo … años.", "Soy de … y vivo en …",
                         "Hablo … y estudio …", "En mi tiempo libre …"],
        "marco_algoritmo": ["El uno y el siete son pareja porque los dos son de …",
                            "… porque tienen la misma edad.",
                            "… porque los dos hablan …",
                            "No, porque uno vive en la ciudad y el otro en un pueblo."],
        "ejemplos": [
            ("Perfil 3", "Tengo 16 años. Soy de Bélgica y vivo en un pueblo. "
                         "Hablo neerlandés e inglés."),
            ("Perfil 8", "Tengo 16 años. Soy de Bélgica y vivo en Gante. "
                         "Hablo neerlandés, francés y un poco de español."),
        ],
    },
    "clave": [
        "De didactische winst zit in het weigeren: wie «nee» zegt, moet een béter "
        "argument geven, en dus opnieuw een zin met ser of tener bouwen.",
        "Model: «El tres y el ocho son pareja porque los dos son belgas y tienen "
        "dieciséis años.» — «No, porque uno vive en un pueblo y el otro en la ciudad.»",
        "Let op de valstrik van §2: nationaliteit met kleine letter (belgas, no Belgas).",
    ],
    "nota": "Werkt alleen anoniem. Zodra er namen bij komen, gaat het over vriendschappen "
            "in plaats van over gegevens — en dan verdwijnt het Spaans.",
}


# ---------------------------------------------------------------------------
# §2 · El verbo SER + los pronombres
# ---------------------------------------------------------------------------

U1_RETO_06 = {
    "id": "C5-U1-RETO-06", "num": 6, "curso": "C5", "unidad": U1,
    "seccion": "§2.1", "ancla": "ser", "soporte": "print",
    "nombre": "La cola del aeropuerto",
    "lente": "🔓 puzzel & escape",
    "forma": "🏫 Toda la clase · de pie", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Ocho pasajeros, ocho tarjetas de embarque. Una sola es la tuya.",
    "gancho_nl": "Acht passagiers, acht instapkaarten. Eén ervan is de jouwe.",
    "consigna_es": "Busca por la clase a la persona cuyos datos coinciden con tu tarjeta. "
                   "Solo puedes preguntar con «¿eres…?» y «¿de dónde…?».",
    "consigna_nl": "Zoek in de klas de persoon van wie de gegevens bij jouw instapkaart "
                   "passen. Je mag alleen vragen met «¿eres…?» en «¿de dónde…?».",
    "regla": "Je mag je rolkaart nooit laten lezen en niet in het Nederlands vragen. "
             "Twee passagiers verschillen maar op één gegeven — die vind je alleen door "
             "door te vragen.",
    "pasos": [
        ("Coge una tarjeta de embarque y una ficha de pasajero.",
         "Neem één instapkaart en één passagiersfiche."),
        ("Levántate y pregunta. Anota a quién ya has descartado.",
         "Sta op en vraag rond. Noteer wie je al hebt uitgesloten."),
        ("¿Coincidís en los tres datos? Sentaos juntos: sois pareja de vuelo.",
         "Kloppen de drie gegevens? Ga samen zitten: jullie zijn vluchtgenoten."),
        ("Al final: presenta a tu pareja a la clase, en tercera persona.",
         "Op het einde: stel je partner voor aan de klas, in de derde persoon."),
    ],
    "datos": {
        # (nombre, nacionalidad, ciudad, asiento)
        "pasajeros": [
            ("Ana", "española", "Madrid", "12A"), ("Bruno", "italiano", "Roma", "12B"),
            ("Clara", "española", "Bilbao", "14C"), ("Diego", "mexicano", "Puebla", "14D"),
            ("Eva", "belga", "Gante", "16E"), ("Farid", "belga", "Amberes", "16F"),
            ("Gala", "colombiana", "Cali", "18A"), ("Hugo", "peruano", "Lima", "18B"),
        ],
        "preguntas": [("¿Eres español/-a?", "Ben je Spaans?"),
                      ("¿De dónde eres?", "Waar kom je vandaan?"),
                      ("¿Eres de Madrid o de Bilbao?", "Kom je uit Madrid of uit Bilbao?"),
                      ("¿Cuál es tu asiento?", "Wat is je stoelnummer?")],
    },
    "clave": [
        "Eva (Gante) en Farid (Amberes) zijn allebei belga — alleen de stad scheidt ze. "
        "Ana en Clara zijn allebei española — idem.",
        "Het stoelnummer staat alleen op de instapkaart, niet op de passagiersfiche: "
        "niemand kent dus zijn eigen stoel en de puzzel valt niet op te lossen door "
        "nummers te vergelijken.",
        "Slotpresentatie in de derde persoon is het echte doel: «Ella es Eva, es belga, "
        "es de Gante.»",
    ],
    "nota": "Knip de fiches en de instapkaarten vooraf uit en hou ze gescheiden. Bij een "
            "klas van meer dan zestien: druk het blad twee keer af en speel in twee rondes.",
}

U1_RETO_08 = {
    "id": "C5-U1-RETO-08", "num": 8, "curso": "C5", "unidad": U1,
    "seccion": "§2.2", "ancla": "ser", "soporte": "print",
    "nombre": "El error caro",
    "lente": "🕵️ forensisch",
    "forma": "👨‍👩‍👧 En equipos", "skill": "👁️ Leer",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Cada equipo tiene cinco vidas. Cazar errores cuesta caro… si te equivocas.",
    "gancho_nl": "Elk team heeft vijf levens. Op foutenjacht gaan kost duur… als je zelf "
                 "misslaat.",
    "consigna_es": "Encuentra los errores de «ser» y «tener» del equipo rival. Cada error "
                   "real le cuesta una vida. Cada acusación falsa te cuesta una a ti.",
    "consigna_nl": "Zoek de ser- en tener-fouten van het andere team. Elke echte fout kost "
                   "hun een leven. Elke valse beschuldiging kost jou er een.",
    "regla": "Je moet zeggen wát er fout is én de juiste vorm geven. «Dat klopt niet» "
             "telt als een valse beschuldiging, ook als de zin écht fout is.",
    "pasos": [
        ("Ronda 0 — kalentamiento: caza los errores del banco de abajo.",
         "Ronde 0 — opwarming: jaag op de fouten in de bank hieronder."),
        ("Cada equipo escribe seis frases sobre sí mismo: cuatro correctas, dos con "
         "trampa.", "Elk team schrijft zes zinnen over zichzelf: vier correcte, twee met "
         "een valstrik."),
        ("Intercambiad las hojas. Buscad y acusad, con la corrección.",
         "Wissel de bladen. Zoek en beschuldig, mét de verbetering."),
        ("Contad las vidas. ¿Empate? Gana quien mejor explicó el porqué.",
         "Tel de levens. Gelijkspel? Wint wie het waarom het best uitlegde."),
    ],
    "datos": {
        # (zin, is_correct, correctie/uitleg)
        "banco": [
            ("Soy 15 años.", False, "Tengo 15 años — leeftijd gaat met tener"),
            ("Yo es de Bélgica.", False, "Yo soy de Bélgica — eerste persoon"),
            ("Nosotros somos Español.", False, "Somos españoles — kleine letter én meervoud"),
            ("Mi hermana tiene catorce años.", True, "correct"),
            ("Ellos son de Madrid.", True, "correct"),
            ("Tú eres belga, ¿verdad?", True, "correct"),
            ("Ella tiene profesora.", False, "Ella es profesora — beroep gaat met ser"),
            ("Vosotros tenéis razón.", True, "correct — «gelijk hebben» gaat wél met tener"),
        ],
    },
    "clave": [
        "Fout: 1 (soy 15 → tengo), 2 (yo es → yo soy), 3 (somos Español → somos españoles), "
        "7 (tiene profesora → es profesora).",
        "Correct: 4, 5, 6, 8. Zin 8 is de valstrik in de andere richting: «tener razón» "
        "is wél met tener, en wie die aankruist verliest een leven.",
        "Zin 3 heeft twéé fouten (hoofdletter én enkelvoud) — reken het als één vondst, "
        "maar vraag beide correcties.",
    ],
    "nota": "De straf op valse beschuldigingen is de motor: zonder die regel kruist een team "
            "gewoon alles aan. Hou de levens zichtbaar op het bord.",
}


# ---------------------------------------------------------------------------
# §3 · El presente regular
# ---------------------------------------------------------------------------

U1_RETO_07 = {
    "id": "C5-U1-RETO-07", "num": 7, "curso": "C5", "unidad": U1,
    "seccion": "§3.2", "ancla": "presente", "soporte": "hub",
    "nombre": "Madrid: entonces y ahora",
    "lente": "🔬 onderzoek & data",
    "forma": "👥 En parejas", "skill": "✍️ Escribir",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "La misma plaza de Madrid, con cuarenta años de diferencia.",
    "gancho_nl": "Hetzelfde plein in Madrid, veertig jaar uit elkaar.",
    "consigna_es": "Busca las diferencias y descríbelas en presente: qué hay ahora y qué "
                   "ya no hay.",
    "consigna_nl": "Zoek de verschillen en beschrijf ze in het presente: wat er nu is en "
                   "wat er niet meer is.",
    "regla": "Alles in het presente, ook als je over 1985 praat. Je zegt dus «en la foto "
             "antigua hay…», niet «había». Die verleden tijd leer je pas in het zesde.",
    "pasos": [
        ("Mira las dos escenas sin escribir. ¿Qué te llama la atención?",
         "Bekijk de twee scènes zonder te schrijven. Wat valt je op?"),
        ("Haz clic en un objeto para ver cómo se llama en español.",
         "Klik op een voorwerp om te zien hoe het in het Spaans heet."),
        ("Escribe cinco frases: tres con «hay» y dos con «ya no hay».",
         "Schrijf vijf zinnen: drie met «hay» en twee met «ya no hay»."),
        ("Compara con tu compañero/a: ¿habéis visto lo mismo?",
         "Vergelijk met je partner: hebben jullie hetzelfde gezien?"),
    ],
    "datos": {
        # (x, y, breedte, hoogte, vorm, kleur, es, nl, in welke scène)
        "escena": [
            (14, 58, 12, 22, "rect", "#B07A4E", "la cabina de teléfono", "de telefooncel", "antes"),
            (36, 62, 20, 18, "rect", "#C9A227", "el quiosco de prensa", "de krantenkiosk", "antes"),
            (64, 66, 24, 12, "rect", "#8E5B4A", "el coche antiguo", "de oude auto", "antes"),
            (90, 44, 5, 36, "rect", "#6A6E78", "la farola", "de straatlantaarn", "ambas"),
            (14, 60, 12, 20, "rect", "#2FA8A0", "el carril bici", "het fietspad", "ahora"),
            (36, 60, 22, 20, "rect", "#E07A5F", "la terraza", "het terras", "ahora"),
            (66, 68, 10, 12, "rect", "#157355", "el patinete eléctrico", "de e-step", "ahora"),
            (82, 52, 14, 10, "rect", "#1E9E74", "el panel solar", "het zonnepaneel", "ahora"),
            (52, 40, 8, 8, "circ", "#D69A2E", "el reloj de la plaza", "de pleinklok", "ambas"),
        ],
        "marco": ["En la plaza de ahora hay …", "Ya no hay …",
                  "Ahora la gente … (usar, mirar, tomar)", "Antes la gente …"],
    },
    "clave": [
        "Alleen vroeger: la cabina de teléfono · el quiosco de prensa · el coche antiguo",
        "Alleen nu: el carril bici · la terraza · el patinete eléctrico · el panel solar",
        "In beide: la farola · el reloj de la plaza — die twee zijn de controle: wie ze "
        "als verschil noteert, heeft te snel gekeken.",
        "Modelzinnen: «En la plaza de ahora hay un carril bici.» · «Ya no hay cabina de "
        "teléfono.» · «Ahora la gente toma algo en la terraza.»",
    ],
    "nota": "«Ya no hay» is nieuw maar kost niets: het is een chunk, geen tijd. Het geeft "
            "de leerling wél meteen iets om over verandering te praten zónder verleden tijd.",
}


# ---------------------------------------------------------------------------
# §4 · Preguntar: interrogativos + el/la
# ---------------------------------------------------------------------------

U1_RETO_01 = {
    "id": "C5-U1-RETO-01", "num": 1, "curso": "C5", "unidad": U1,
    "seccion": "§4.1", "ancla": "preguntar", "soporte": "ppt",
    "nombre": "Rueda de prensa",
    "lente": "🎭 simulatie met beperking",
    "forma": "🏫 Toda la clase", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Silencio, empieza la rueda de prensa. Tenéis tres minutos con la estrella.",
    "gancho_nl": "Stilte, de persconferentie begint. Jullie krijgen drie minuten met de ster.",
    "consigna_es": "La prensa pregunta, la estrella contesta. Solo cuentan las preguntas "
                   "con palabra interrogativa.",
    "consigna_nl": "De pers vraagt, de ster antwoordt. Alleen vragen mét een vraagwoord tellen.",
    "regla": "Een ja/nee-vraag kost je je beurt. Je moet dus met qué, quién, dónde, "
             "cuándo, cómo, cuánto of por qué beginnen — en niemand mag hetzelfde "
             "vraagwoord twee keer gebruiken.",
    "pasos": [
        ("La estrella coge una ficha secreta y se sienta delante.",
         "De ster neemt een geheime fiche en gaat vooraan zitten."),
        ("La prensa levanta la mano. Una pregunta por periodista.",
         "De pers steekt de hand op. Eén vraag per journalist."),
        ("El/la profe tacha el interrogativo usado: ya no se puede repetir.",
         "De leerkracht schrapt het gebruikte vraagwoord: dat mag niet meer terug."),
        ("Al final la prensa escribe el titular en una frase.",
         "Op het einde schrijft de pers de krantenkop in één zin."),
    ],
    "datos": {
        "interrogativos": [("¿Qué…?", "wat"), ("¿Quién…?", "wie"), ("¿Dónde…?", "waar"),
                           ("¿Cuándo…?", "wanneer"), ("¿Cómo…?", "hoe"),
                           ("¿Cuántos…?", "hoeveel"), ("¿Por qué…?", "waarom")],
        "estrellas": [
            ("una futbolista del Real Madrid", "speelt sinds haar zesde, woont in Madrid, "
                                               "spreekt drie talen"),
            ("un cantante de Sevilla", "zingt flamenco-pop, twintig jaar, woont bij zijn oma"),
            ("una astronauta mexicana", "werkt in Houston, spreekt Spaans en Engels, "
                                        "heeft twee kinderen"),
            ("un cocinero peruano", "restaurant in Lima, kookt ceviche, veertig jaar"),
        ],
        "titular": "TITULAR:  «… es … y vive en …»",
    },
    "clave": [
        "De zeven vraagwoorden zijn precies die van §4.1 — het spel dwingt de klas ze "
        "alle zeven te gebruiken in plaats van drie keer «¿qué?».",
        "«¿Por qué…?» is de moeilijkste en blijft meestal tot het laatst over. Hou hem "
        "bewust achter de hand voor de sterkste leerling.",
        "Valstrik: «¿Cuántos años tienes?» — leerlingen zeggen vaak «¿Cuánto años?». "
        "Cuántos beweegt mee met años.",
    ],
    "nota": "Het verbod op herhaling is wat het spel maakt. Zet de zeven vraagwoorden op "
            "het scherm en streep ze zichtbaar door — de spanning stijgt met elke doorhaling.",
}

U1_RETO_04 = {
    "id": "C5-U1-RETO-04", "num": 4, "curso": "C5", "unidad": U1,
    "seccion": "§4.1", "ancla": "preguntar", "soporte": "ppt",
    "nombre": "Preguntas prohibidas",
    "lente": "✍️ creatieve beperking",
    "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 10 min", "dificultad": "★★★",
    "gancho_es": "Necesitas la misma información. Pero tres preguntas están prohibidas.",
    "gancho_nl": "Je hebt dezelfde informatie nodig. Maar drie vragen zijn verboden.",
    "consigna_es": "Averigua la edad, la ciudad y las lenguas de tu compañero/a sin usar "
                   "«¿cuántos años…?», «¿dónde…?» ni «¿qué lenguas…?».",
    "consigna_nl": "Achterhaal leeftijd, stad en talen van je partner zónder «¿cuántos "
                   "años…?», «¿dónde…?» of «¿qué lenguas…?» te gebruiken.",
    "regla": "De drie rechtstreekse vragen zijn verboden. Je moet er dus omheen: met een "
             "voorstel, een vergelijking of een gok die je laat bevestigen.",
    "pasos": [
        ("Mira las tres preguntas prohibidas. Piensa un rodeo para cada una.",
         "Bekijk de drie verboden vragen. Bedenk voor elk een omweg."),
        ("Pregunta. Tu compañero/a solo contesta lo que le preguntas de verdad.",
         "Stel je vraag. Je partner antwoordt alleen op wat je écht vraagt."),
        ("Anota los tres datos. ¿Los tienes todos? Cambiad de papel.",
         "Noteer de drie gegevens. Alle drie? Wissel van rol."),
        ("Comparad: ¿qué rodeo ha funcionado mejor?",
         "Vergelijk: welke omweg werkte het best?"),
    ],
    "datos": {
        "prohibidas": [("¿Cuántos años tienes?", "de leeftijd"),
                       ("¿Dónde vives?", "de stad"),
                       ("¿Qué lenguas hablas?", "de talen")],
        "rodeos": [
            ("¿Eres del dos mil nueve?", "gok het geboortejaar en laat bevestigen"),
            ("¿Tienes la misma edad que yo?", "vergelijk met jezelf"),
            ("¿Vienes al instituto en bici o en tren?", "vervoer verraadt de afstand"),
            ("¿Tu ciudad es grande?", "eigenschap in plaats van naam"),
            ("¿Hablas español en casa?", "test één taal per keer"),
            ("¿Ves series en inglés sin subtítulos?", "gewoonte verraadt het niveau"),
        ],
    },
    "clave": [
        "Er is geen enkel juist antwoord — wel een meetbaar resultaat: heb je de drie "
        "gegevens binnen zonder de verboden vragen?",
        "De sterkste omweg is meestal de gok met bevestiging («¿Eres del dos mil nueve?»): "
        "die levert een getal op zonder ernaar te vragen.",
        "Deze reto bereidt de omweg-strategie voor die in U2 terugkomt bij «Mi gente, sin "
        "la palabra familia».",
    ],
    "nota": "Kort houden. Tien minuten is genoeg; daarna wordt de beperking een spel op "
            "zich en verdwijnt het luisteren.",
}

U1_RETO_05 = {
    "id": "C5-U1-RETO-05", "num": 5, "curso": "C5", "unidad": U1,
    "seccion": "§4.2", "ancla": "preguntar", "soporte": "hub",
    "nombre": "La tienda de los objetos raros",
    "lente": "🕵️ forensisch",
    "forma": "👥 En parejas", "skill": "👁️ Leer",
    "tiempo": "± 10 min", "dificultad": "★★★",
    "gancho_es": "Doce objetos que no existen. Pero su artículo sí se puede saber.",
    "gancho_nl": "Twaalf voorwerpen die niet bestaan. Maar hun lidwoord valt wél te weten.",
    "consigna_es": "Elige «el» o «la» y di POR QUÉ. Ningún diccionario te va a ayudar: "
                   "solo la regla.",
    "consigna_nl": "Kies «el» of «la» en zeg WAAROM. Geen woordenboek helpt je hier — "
                   "alleen de regel.",
    "regla": "Bij elk woord moet je de regel kiezen die je gebruikt. Het juiste lidwoord "
             "met de verkeerde regel telt als fout: dan had je geraden.",
    "pasos": [
        ("Mira la terminación, no la palabra entera.",
         "Kijk naar de uitgang, niet naar het hele woord."),
        ("Elige el artículo y la regla que lo justifica.",
         "Kies het lidwoord én de regel die het verantwoordt."),
        ("Cuidado: hay cuatro palabras que rompen la regla fácil.",
         "Let op: vier woorden breken de makkelijke regel."),
    ],
    "datos": {
        # (woord, lidwoord, regelsleutel)
        "objetos": [
            ("nurbo", "el", "-o"), ("trepa", "la", "-a"), ("fartema", "el", "-ma"),
            ("glinda", "la", "-a"), ("zampo", "el", "-o"), ("nurbación", "la", "-ción"),
            ("clisma", "el", "-ma"), ("mosta", "la", "-a"), ("cluvo", "el", "-o"),
            ("vurtad", "la", "-dad"), ("pandema", "el", "-ma"), ("niebra", "la", "-a"),
        ],
        "reglas": [
            ("-o", "eindigt op -o → el"),
            ("-a", "eindigt op -a → la"),
            ("-ma", "eindigt op -ma → el (uitzondering, zoals el problema)"),
            ("-ción", "eindigt op -ción → la (zoals la dirección)"),
            ("-dad", "eindigt op -dad → la (zoals la ciudad)"),
        ],
    },
    "clave": [
        "el: nurbo · fartema · zampo · clisma · cluvo · pandema",
        "la: trepa · glinda · nurbación · mosta · vurtad · niebra",
        "De vier valstrikken zijn de -ma-woorden (fartema, clisma, pandema) plus vurtad: "
        "wie op de klank afgaat, kiest daar «la» en «el».",
        "Precies dezelfde uitgangen als in de echte woordenschat van §4.2: problema, "
        "dirección, ciudad, nacionalidad.",
    ],
    "nota": "Verzonnen woorden zijn hier geen grap maar het meetinstrument: op echte "
            "woorden kan een leerling het lidwoord uit het geheugen halen, hier niet.",
}


# ---------------------------------------------------------------------------
# Cultura · Madrid y los nombres hispanos
# ---------------------------------------------------------------------------

U1_RETO_10 = {
    "id": "C5-U1-RETO-10", "num": 10, "curso": "C5", "unidad": U1,
    "seccion": "Cultura", "ancla": "cultura_u1", "soporte": "hub",
    "nombre": "Un minuto sobre ti",
    "lente": "🤝 bemiddelen",
    "forma": "👥 En parejas", "skill": "🔀 Mediar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Tu compañero/a no habla español. Tú sí. Preséntalo tú.",
    "gancho_nl": "Je partner spreekt geen Spaans. Jij wel. Stel hem of haar voor.",
    "consigna_es": "Entrevista a tu compañero/a en neerlandés y graba un minuto en español "
                   "presentándolo a Lucía, que no entiende ni una palabra de neerlandés.",
    "consigna_nl": "Interview je partner in het Nederlands en neem één minuut Spaans op "
                   "waarin je hem voorstelt aan Lucía, die geen woord Nederlands verstaat.",
    "regla": "Je vertaalt niet, je vertélt. Alles in de derde persoon, en je laat weg wat "
             "je niet kunt zeggen — een minuut die klopt is beter dan twee die vastlopen.",
    "pasos": [
        ("Entrevista en neerlandés. Anota solo palabras clave, no frases.",
         "Interview in het Nederlands. Noteer alleen sleutelwoorden, geen zinnen."),
        ("Elige qué cuentas y qué dejas fuera. No cabe todo.",
         "Kies wat je vertelt en wat je weglaat. Alles past niet."),
        ("Graba un minuto en tercera persona. Escúchate.",
         "Neem één minuut op in de derde persoon. Luister terug."),
        ("Tu compañero/a escucha: ¿se reconoce en lo que has dicho?",
         "Je partner luistert: herkent die zich in wat je gezegd hebt?"),
    ],
    "datos": {
        "marco": ["Te presento a …", "Es de … y vive en …", "Tiene … años.",
                  "Habla … y estudia …", "En su tiempo libre …", "Creo que es una persona …"],
        "criterios": [
            ("Begrijpelijk voor iemand die geen Nederlands kent", "geen leenwoorden"),
            ("Derde persoon volgehouden", "es · tiene · habla · vive"),
            ("Bewust weggelaten wat niet lukt", "geen halve zinnen"),
        ],
    },
    "clave": [
        "Beoordeel niet op volledigheid maar op verstaanbaarheid: zou Lucía dit begrijpen?",
        "Meest voorkomende breuk: halverwege terugvallen op de ik-vorm, meestal bij de "
        "hobby's. Wijs erop dat «su tiempo libre» de vorm vasthoudt.",
        "Dit is de eerste echte bemiddelingsopdracht van de cursus: informatie uit taal A "
        "bruikbaar maken in taal B, met verlies — en dat verlies is toegestaan.",
    ],
    "nota": "Het weglaten expliciet toestaan is essentieel. Leerlingen die alles willen "
            "vertalen, lopen vast; wie durft te schrappen, spreekt een vlotte minuut.",
}


# --- register per unit ---
RETOS_U0 = [RETO_01, RETO_02, RETO_03, RETO_04, RETO_05,
            RETO_06, RETO_07, RETO_08, RETO_09, RETO_10]
RETOS_U1 = [U1_RETO_01, U1_RETO_02, U1_RETO_03, U1_RETO_04, U1_RETO_05,
            U1_RETO_06, U1_RETO_07, U1_RETO_08, U1_RETO_09, U1_RETO_10]
RETOS = RETOS_U0 + RETOS_U1

# Waar in de printcursus elke sectie eindigt — hier wordt een print-reto ingevoegd.
ANCLAS = ["alfabeto", "sonidos", "sonido_letra", "acento", "numeros", "saludos", "cultura",
          # C5 U1
          "datos", "ser", "presente", "preguntar", "cultura_u1"]


def de(curso, unidad):
    """De tien retos van één unit, op volgnummer."""
    return sorted((r for r in RETOS if r["curso"] == curso and r["unidad"] == unidad),
                  key=lambda r: r["num"])


def por_soporte(soporte, curso=None, unidad=None):
    return [r for r in RETOS if r["soporte"] == soporte
            and (curso is None or r["curso"] == curso)
            and (unidad is None or r["unidad"] == unidad)]


def por_ancla(ancla):
    return [r for r in RETOS if r["ancla"] == ancla]


def controla():
    vistos = set()
    for r in RETOS:
        for campo in ("id", "num", "seccion", "ancla", "soporte", "nombre", "lente",
                      "forma", "skill", "tiempo", "dificultad", "gancho_es", "gancho_nl",
                      "consigna_es", "consigna_nl", "regla", "pasos", "datos", "clave"):
            assert campo in r, "%s mist %s" % (r.get("id", "?"), campo)
        assert r["id"] not in vistos, "dubbele id %s" % r["id"]
        vistos.add(r["id"])
        assert r["soporte"] in ("print", "hub", "ppt"), r["id"]
        assert r["ancla"] in ANCLAS, (r["id"], r["ancla"])
        assert len(r["pasos"]) >= 3, "%s heeft te weinig stappen" % r["id"]
        assert all(len(p) == 2 for p in r["pasos"]), r["id"]
        assert r["clave"], "%s heeft geen antwoordsleutel" % r["id"]
        # de beperking is wat een reto een reto maakt
        assert len(r["regla"]) > 40, "%s: de regla is te dun" % r["id"]
    # elke unit telt tien retos, genummerd 1 t.e.m. 10
    for clave in {(r["curso"], r["unidad"]) for r in RETOS}:
        nums = sorted(r["num"] for r in de(*clave))
        assert nums == list(range(1, 11)), (clave, nums)
        # en de dragers zijn gespreid: geen unit die volledig op één drager leunt
        dragers = {r["soporte"] for r in de(*clave)}
        assert len(dragers) == 3, (clave, dragers)


def resumen():
    """Overzicht voor wie een unit gaat bouwen."""
    for clave in sorted({(r["curso"], r["unidad"]) for r in RETOS}):
        print("\n=== %s U%d ===" % clave)
        print("%-16s %-34s %-7s %-26s %s" % ("id", "nombre", "drager", "lens", "sectie"))
        for r in de(*clave):
            print("%-16s %-34s %-7s %-26s %s"
                  % (r["id"], r["nombre"], r["soporte"], r["lente"], r["seccion"]))
        from collections import Counter
        print("dragers:", dict(Counter(r["soporte"] for r in de(*clave))))


if __name__ == "__main__":
    resumen()
