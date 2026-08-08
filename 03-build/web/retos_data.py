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


# ===========================================================================
# C5 · U2 — Mi gente  (parada: Andalucía · Sevilla)
# ===========================================================================

U2 = 2

U2_RETO_01 = {
    "id": "C5-U2-RETO-01", "num": 1, "curso": "C5", "unidad": U2,
    "seccion": "§1.3", "ancla": "familia", "soporte": "print",
    "nombre": "El árbol imposible",
    "lente": "🕵️ forensisch",
    "forma": "👨‍👩‍👧 En grupos", "skill": "👁️ Leer",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Cuatro testigos, una sola familia. Uno de ellos miente.",
    "gancho_nl": "Vier getuigen, één familie. Eén van hen liegt.",
    "consigna_es": "Reconstruye el árbol genealógico con las cuatro declaraciones y señala "
                   "quién miente, con la frase exacta como prueba.",
    "consigna_nl": "Reconstrueer de stamboom met de vier verklaringen en wijs aan wie liegt — "
                   "met de exacte zin als bewijs.",
    "regla": "Je beschuldiging telt alleen mét citaat. «Marco liegt» is geen antwoord; "
             "«Marco liegt, want hij zegt X en Ana zegt Y» wel.",
    "pasos": [
        ("Lee las cuatro declaraciones sin escribir nada.",
         "Lees de vier verklaringen zonder iets te schrijven."),
        ("Dibuja el árbol con lo que TODOS confirman.",
         "Teken de stamboom met wat álle vier bevestigen."),
        ("Busca la declaración que no encaja. Cita la frase.",
         "Zoek de verklaring die niet past. Citeer de zin."),
        ("Comparad en grupo: ¿habéis acusado a la misma persona?",
         "Vergelijk in groep: hebben jullie dezelfde persoon beschuldigd?"),
    ],
    "datos": {
        "declaraciones": [
            ("Rosa", "Tengo dos hijos: Carmen y Paco. Carmen tiene una hija, Lola."),
            ("Carmen", "Mi madre se llama Rosa. Mi hermano Paco no tiene hijos."),
            ("Paco", "Soy el tío de Lola. Mi hermana Carmen vive en Sevilla."),
            ("Lola", "Mi abuela Rosa tiene tres hijos y yo tengo dos primos."),
        ],
    },
    "clave": [
        "Wie liegt: Lola. Zij zegt «tres hijos» en «dos primos», terwijl Rosa zelf "
        "«dos hijos» zegt en Carmen bevestigt dat Paco geen kinderen heeft.",
        "De stamboom: Rosa → Carmen en Paco. Carmen → Lola. Paco is Lola's oom.",
        "Bewijs uit twee richtingen: Rosa's «Tengo dos hijos» én Carmen's «Paco no tiene "
        "hijos». Eén verklaring alleen volstaat niet.",
    ],
    "nota": "Laat de stamboom écht tekenen. Wie alleen leest, ziet de tegenspraak niet; "
            "wie tekent, botst er vanzelf op.",
}

U2_RETO_05 = {
    "id": "C5-U2-RETO-05", "num": 5, "curso": "C5", "unidad": U2,
    "seccion": "§1.3", "ancla": "familia", "soporte": "print",
    "nombre": "Familias del mundo hispano",
    "lente": "🔬 onderzoek & data",
    "forma": "👤 Solo", "skill": "👁️ Leer",
    "tiempo": "± 10 min", "dificultad": "★★☆",
    "gancho_es": "¿Cuántos sois en casa? En el mundo hispano la respuesta cambia mucho.",
    "gancho_nl": "Met hoeveel zijn jullie thuis? In de Spaanstalige wereld verschilt dat sterk.",
    "consigna_es": "Lee la tabla y escribe tres frases con «tener» que comparen los países "
                   "con Bélgica.",
    "consigna_nl": "Lees de tabel en schrijf drie zinnen met «tener» die de landen met "
                   "België vergelijken.",
    "regla": "Elke zin bevat een écht getal uit de tabel én het werkwoord tener. "
             "«En México las familias son grandes» telt niet — «En México una familia "
             "tiene 3,6 personas» wel.",
    "pasos": [
        ("Mira la tabla. ¿Qué país te sorprende?",
         "Bekijk de tabel. Welk land verrast je?"),
        ("Escribe tres frases con un número de verdad.",
         "Schrijf drie zinnen met een echt getal."),
        ("Y tu casa, ¿dónde encaja? Escribe una cuarta frase.",
         "En jouw gezin, waar past dat? Schrijf een vierde zin."),
    ],
    "datos": {
        # gemiddelde huishoudgrootte, afgerond — bron in de docentnota
        "tabla": [("México", 3.6), ("Guatemala", 4.4), ("Colombia", 3.1),
                  ("España", 2.5), ("Argentina", 3.0), ("Bélgica", 2.3)],
        "marco": ["En … una familia tiene … personas.",
                  "En … las familias tienen más/menos personas que en Bélgica.",
                  "En mi casa somos … : tengo …"],
    },
    "clave": [
        "Grootst: Guatemala (4,4) · kleinst: België (2,3) — dat verschil is bijna het "
        "dubbele en is meestal de verrassing.",
        "Modelzin: «En Guatemala una familia tiene cuatro coma cuatro personas; en "
        "Bélgica tiene dos coma tres.»",
        "Let op het decimaalteken: in het Spaans lees je «tres coma seis», niet «tres punto seis».",
    ],
    "nota": "Cijfers zijn afgeronde gemiddelden voor de huishoudgrootte en dienen om te "
            "vergelijken, niet om uit het hoofd te leren. Controleer ze vóór gebruik als je "
            "ze als feit presenteert.",
}

U2_RETO_06 = {
    "id": "C5-U2-RETO-06", "num": 6, "curso": "C5", "unidad": U2,
    "seccion": "§1.3", "ancla": "familia", "soporte": "print",
    "nombre": "Mi gente, sin la palabra «familia»",
    "lente": "✍️ creatieve beperking",
    "forma": "👤 Solo", "skill": "✍️ Escribir",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Escribe sobre las personas que cuentan para ti. Pero hay palabras prohibidas.",
    "gancho_nl": "Schrijf over de mensen die voor jou tellen. Maar er zijn verboden woorden.",
    "consigna_es": "Cinco frases sobre tu gente, sin usar «familia», «madre», «padre» ni "
                   "«hermano/a».",
    "consigna_nl": "Vijf zinnen over jouw mensen, zonder «familia», «madre», «padre» of "
                   "«hermano/a» te gebruiken.",
    "regla": "Die vier woorden zijn verboden. Je moet dus omschrijven: wie die persoon is, "
             "wat die doet, waarom die telt. Niet iedereen woont in hetzelfde huis — dat mag.",
    "pasos": [
        ("Piensa en tres personas. No escribas sus papeles todavía.",
         "Denk aan drie personen. Schrijf hun rol nog niet op."),
        ("Descríbelas: qué hacen, cómo son, dónde viven.",
         "Beschrijf ze: wat ze doen, hoe ze zijn, waar ze wonen."),
        ("Lee tu texto a tu compañero/a. ¿Adivina quién es quién?",
         "Lees je tekst voor aan je buur. Raadt die wie wie is?"),
    ],
    "datos": {
        "prohibidas": ["familia", "madre", "padre", "hermano", "hermana"],
        "marco": ["Vivo con …", "… trabaja en …", "… es muy … y siempre …",
                  "Para mí … es importante porque …", "Los domingos … "],
    },
    "clave": [
        "Er is geen juist antwoord — wel een meetbare beperking: staat er geen enkel "
        "verboden woord in, en herkent de buur de personen?",
        "Sterke omwegen die leerlingen vinden: «la persona que me despierta», «el que "
        "cocina los domingos», «la que vive arriba».",
        "Deze reto maakt ruimte voor gezinnen die niet in het standaardschema passen. "
        "Dat is de didactische winst, naast de woordenschat.",
    ],
    "nota": "Dwing niemand om voor te lezen. De beperking is talig bedoeld, niet als "
            "uitnodiging om over de thuissituatie te vertellen.",
}

U2_RETO_10 = {
    "id": "C5-U2-RETO-10", "num": 10, "curso": "C5", "unidad": U2,
    "seccion": "§3.3", "ancla": "adjetivos", "soporte": "print",
    "nombre": "El adjetivo prohibido",
    "lente": "✍️ creatieve beperking",
    "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 10 min", "dificultad": "★★☆",
    "gancho_es": "Describe a tres personas. Pero los tres adjetivos fáciles están prohibidos.",
    "gancho_nl": "Beschrijf drie personen. Maar de drie makkelijke bijvoeglijke naamwoorden "
                 "zijn verboden.",
    "consigna_es": "Describe a tres personas sin decir «simpático», «bueno» ni «grande». "
                   "Tu compañero/a adivina de quién hablas.",
    "consigna_nl": "Beschrijf drie personen zonder «simpático», «bueno» of «grande» te "
                   "zeggen. Je buur raadt over wie je het hebt.",
    "regla": "Die drie zijn verboden, en je mag ze ook niet omzeilen met «muy bueno» of "
             "«no es malo». Je moet naar een ánder woord grijpen.",
    "pasos": [
        ("Elige tres personas que los dos conocéis.",
         "Kies drie personen die jullie allebei kennen."),
        ("Escribe dos adjetivos por persona, sin los prohibidos.",
         "Schrijf twee bijvoeglijke naamwoorden per persoon, zonder de verboden woorden."),
        ("Describe. Tu compañero/a adivina. Cambiad.",
         "Beschrijf. Je buur raadt. Wissel."),
    ],
    "datos": {
        "prohibidas": ["simpático/-a", "bueno/-a", "grande"],
        "banco": ["divertido/-a", "tranquilo/-a", "hablador/-a", "generoso/-a", "tímido/-a",
                  "trabajador/-a", "cariñoso/-a", "despistado/-a", "valiente", "paciente"],
    },
    "clave": [
        "Let op de overeenkomst: trabajador → trabajadora, hablador → habladora. "
        "Adjectieven op -e (valiente, paciente) veranderen níét.",
        "Wie «no es malo» gebruikt, omzeilt de regel en doet het opnieuw.",
        "De bank is een steiger: laat sterke leerlingen zonder werken.",
    ],
    "nota": "Tien woorden in de bank is genoeg. Meer aanbieden maakt van de oefening "
            "een leeslijst in plaats van een spreekopdracht.",
}

U2_RETO_04 = {
    "id": "C5-U2-RETO-04", "num": 4, "curso": "C5", "unidad": U2,
    "seccion": "§3.3", "ancla": "adjetivos", "soporte": "hub",
    "nombre": "Retrato hablado",
    "lente": "🎭 simulatie met beperking",
    "forma": "👥 En parejas", "skill": "👂 Escuchar",
    "tiempo": "± 10 min", "dificultad": "★★☆",
    "gancho_es": "La policía busca a alguien. Solo tiene la descripción.",
    "gancho_nl": "De politie zoekt iemand. Ze hebben alleen de beschrijving.",
    "consigna_es": "Escucha la descripción y elige el retrato correcto. Después describe tú "
                   "uno y que tu compañero/a lo encuentre.",
    "consigna_nl": "Luister naar de beschrijving en kies het juiste portret. Beschrijf daarna "
                   "zelf iemand en laat je buur die vinden.",
    "regla": "Je mag geen vragen stellen tijdens het luisteren. Eén keer horen, dan kiezen. "
             "Wie het mis heeft, luistert opnieuw — maar verliest zijn punt.",
    "pasos": [
        ("Escucha la primera descripción. No mires los retratos todavía.",
         "Luister naar de eerste beschrijving. Kijk nog niet naar de portretten."),
        ("Ahora mira y elige. ¿Qué detalle decide?",
         "Kijk nu en kies. Welk detail geeft de doorslag?"),
        ("Te toca: describe uno sin decir el número.",
         "Jouw beurt: beschrijf er een zonder het nummer te zeggen."),
    ],
    "datos": {
        # (nummer, haar, ogen/bril, extra, adjetivo)
        "retratos": [
            (1, "pelo largo y rizado", "lleva gafas", "sonríe", "habladora"),
            (2, "pelo largo y liso", "sin gafas", "sonríe", "tranquila"),
            (3, "pelo corto y rizado", "lleva gafas", "serio", "tímido"),
            (4, "pelo corto y liso", "sin gafas", "serio", "trabajador"),
            (5, "pelo largo y rizado", "sin gafas", "serio", "valiente"),
            (6, "pelo corto y rizado", "sin gafas", "sonríe", "divertido"),
        ],
        "descripciones": [
            (3, "Tiene el pelo corto y rizado, lleva gafas y es bastante serio. Es tímido."),
            (5, "Tiene el pelo largo y rizado, no lleva gafas y no sonríe. Es valiente."),
            (6, "Tiene el pelo corto y rizado, no lleva gafas y sonríe mucho. Es divertido."),
        ],
    },
    "clave": [
        "Portret 3 · 5 · 6, in die volgorde.",
        "Portret 1 en 5 verschillen alleen in de bril; 3 en 6 alleen in bril én uitdrukking. "
        "Wie half luistert, kiest de buur ernaast.",
        "Het beslissende detail is bijna nooit het haar — dat delen er telkens twee.",
    ],
    "nota": "Zes portretten is het maximum: bij meer wordt het zoeken in plaats van luisteren.",
}

U2_RETO_07 = {
    "id": "C5-U2-RETO-07", "num": 7, "curso": "C5", "unidad": U2,
    "seccion": "Cultura", "ancla": "cultura_u2", "soporte": "hub",
    "nombre": "El podcast del abuelo",
    "lente": "📻 mediaformat",
    "forma": "👤 Solo", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Un abuelo de Sevilla te manda un mensaje de voz. Te toca contestar.",
    "gancho_nl": "Een opa uit Sevilla stuurt je een spraakbericht. Jij mag antwoorden.",
    "consigna_es": "Escucha la carta sonora del abuelo Curro y graba tu respuesta de treinta "
                   "segundos: preséntale a tu gente.",
    "consigna_nl": "Luister naar de geluidsbrief van abuelo Curro en neem je antwoord van "
                   "dertig seconden op: stel jouw mensen aan hem voor.",
    "regla": "Je antwoordt op wat hij écht vraagt — niet op wat je toevallig kunt zeggen. "
             "Zijn drie vragen moeten alle drie een antwoord krijgen.",
    "pasos": [
        ("Escucha una vez sin notas. ¿Qué te pregunta?",
         "Luister één keer zonder te noteren. Wat vraagt hij je?"),
        ("Escucha otra vez y anota sus tres preguntas.",
         "Luister opnieuw en noteer zijn drie vragen."),
        ("Graba treinta segundos. Contesta las tres.",
         "Neem dertig seconden op. Beantwoord alle drie."),
    ],
    "datos": {
        "guion": [
            ("Abuelo Curro", "¡Hola, muchacho! Soy Curro, el abuelo de Lucía, desde Sevilla."),
            ("Abuelo Curro", "Aquí en casa somos muchos: mis dos hijas, sus maridos y cinco nietos."),
            ("Abuelo Curro", "Dime una cosa: ¿cuántos sois en tu casa?"),
            ("Abuelo Curro", "¿Y tienes hermanos o eres hijo único?"),
            ("Abuelo Curro", "Ah, y lo más importante: ¿tenéis animales? Aquí tenemos dos gatos."),
            ("Abuelo Curro", "Cuéntamelo todo. ¡Hasta pronto!"),
        ],
        "marco": ["Hola, Curro. En mi casa somos …", "Tengo … / No tengo …",
                  "Sí, tenemos … / No, no tenemos animales."],
    },
    "clave": [
        "Zijn drie vragen: hoeveel zijn jullie thuis · heb je broers of zussen · hebben "
        "jullie huisdieren.",
        "Beoordeel op alle drie beantwoord, niet op vloeiendheid. Wie er twee doet, "
        "luistert opnieuw.",
        "Curro gebruikt «somos» en «tenemos» — precies de twee vormen die het antwoord "
        "nodig heeft.",
    ],
    "nota": "Het fragment staat als script in de hub en wordt voorgelezen door de "
            "computerstem zolang er geen opname is.",
}

U2_RETO_09 = {
    "id": "C5-U2-RETO-09", "num": 9, "curso": "C5", "unidad": U2,
    "seccion": "Cultura", "ancla": "cultura_u2", "soporte": "hub",
    "nombre": "Sevilla en tres voces",
    "lente": "🤝 bemiddelen",
    "forma": "👤 Solo", "skill": "🔀 Mediar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Tres sevillanos, tres opiniones sobre el mismo barrio.",
    "gancho_nl": "Drie inwoners van Sevilla, drie meningen over dezelfde buurt.",
    "consigna_es": "Escucha a los tres y resume para un amigo flamenco quién piensa qué. "
                   "No traduzcas: resume.",
    "consigna_nl": "Luister naar alle drie en vat voor een Vlaamse vriend samen wie wat "
                   "vindt. Niet vertalen: samenvatten.",
    "regla": "Je samenvatting is korter dan wat je hoorde. Je mag dus schrappen — maar niet "
             "verzinnen, en geen van de drie mag wegvallen.",
    "pasos": [
        ("Escucha las tres voces seguidas. No escribas.",
         "Luister de drie stemmen na elkaar. Schrijf niet."),
        ("Escucha otra vez y anota una palabra por persona.",
         "Luister opnieuw en noteer één woord per persoon."),
        ("Escribe tu resumen en tres frases, en neerlandés.",
         "Schrijf je samenvatting in drie zinnen, in het Nederlands."),
        ("Compara: ¿has dejado fuera algo importante?",
         "Vergelijk: heb je iets belangrijks weggelaten?"),
    ],
    "datos": {
        "voces": [
            ("Rosa, 71", "Mi barrio es tranquilo y todos nos conocemos. Los vecinos son "
                         "como mi familia: siempre hay alguien en la calle."),
            ("Javi, 17", "A mí el barrio me parece aburrido. No hay nada para los jóvenes: "
                         "ni cine, ni polideportivo. Los fines de semana voy al centro."),
            ("Amina, 34", "Es un barrio muy vivo pero caro. Mi piso es pequeño y cuesta "
                          "mucho. Lo bueno es que mi hija va al colegio a dos calles."),
        ],
    },
    "clave": [
        "Rosa: rustig, iedereen kent elkaar, buren als familie — positief.",
        "Javi: saai, niets voor jongeren, gaat naar het centrum — negatief.",
        "Amina: levendig maar duur, klein appartement, school dichtbij — gemengd.",
        "De valkuil is Amina: leerlingen maken haar positief óf negatief, terwijl ze "
        "allebei zegt. «Maar» in de samenvatting is het teken dat het gelukt is.",
    ],
    "nota": "Bemiddelen mag in het Nederlands: het doel is dat de informatie overkomt, "
            "niet dat de leerling het in het Spaans navertelt.",
}

U2_RETO_02 = {
    "id": "C5-U2-RETO-02", "num": 2, "curso": "C5", "unidad": U2,
    "seccion": "§2.3", "ancla": "posesivos", "soporte": "ppt",
    "nombre": "La familia de la telenovela",
    "lente": "🎭 simulatie met beperking",
    "forma": "🏫 Toda la clase", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "La clase escribe una telenovela. Pero primero hay que saber quién es de quién.",
    "gancho_nl": "De klas schrijft een telenovela. Maar eerst moet je weten wie van wie is.",
    "consigna_es": "Entre todos inventáis la familia. Cada personaje se conecta con otro "
                   "usando un posesivo.",
    "consigna_nl": "Samen verzinnen jullie de familie. Elk personage wordt met een bezittelijk "
                   "voornaamwoord aan een ander gekoppeld.",
    "regla": "Elk nieuw personage moet met minstens twee bezittelijke voornaamwoorden aan de "
             "bestaande familie hangen. Een personage dat aan niemand hangt, komt er niet in.",
    "pasos": [
        ("Empezamos con Rosalía, la abuela. Todo cuelga de ella.",
         "We beginnen met Rosalía, de oma. Alles hangt aan haar."),
        ("Cada alumno/a añade un personaje y lo conecta.",
         "Elke leerling voegt een personage toe en verbindt het."),
        ("El/la profe dibuja el árbol en la pizarra mientras tanto.",
         "De leerkracht tekent de stamboom ondertussen op het bord."),
        ("Al final: una frase de escándalo con «su» o «sus».",
         "Op het einde: één schandaalzin met «su» of «sus»."),
    ],
    "datos": {
        "semilla": [("Rosalía", "la abuela · 78 años · vive en Triana"),
                    ("Curro", "su marido · toca la guitarra")],
        "marco": ["… es mi/tu/su …", "Sus hijos se llaman …",
                  "Nuestra abuela vive en …", "Su perro se llama …"],
        "escandalo": ["¡Su marido no es su marido!", "¡Sus hijos no saben que …!",
                      "¡Nuestra abuela tiene un secreto!"],
    },
    "clave": [
        "De regel te bewaken: «su» hoort bij het bezeten ding, niet bij de bezitter — "
        "«sus hijos» is meervoud omdat er meer kinderen zijn, niet omdat er meer ouders zijn.",
        "«Nuestro/-a» beweegt wél mee in geslacht: nuestra abuela, nuestro abuelo.",
        "Laat de stamboom op het bord staan: bij de eindtaak «Álbum de familia» is hij "
        "het model.",
    ],
    "nota": "Werkt het best als de leerkracht meetekent. Zonder zichtbare stamboom "
            "verliest de klas na zes personages het overzicht.",
}

U2_RETO_03 = {
    "id": "C5-U2-RETO-03", "num": 3, "curso": "C5", "unidad": U2,
    "seccion": "§2.3", "ancla": "posesivos", "soporte": "ppt",
    "nombre": "Herencia con condiciones",
    "lente": "⚖️ onderhandeling & dilemma",
    "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "La tía Amparo deja cinco cosas. Y una nota que no aclara nada.",
    "gancho_nl": "Tante Amparo laat vijf dingen na. En een briefje dat niets verduidelijkt.",
    "consigna_es": "Decidid quién recibe qué. Cada decisión se defiende solo con una "
                   "relación de familia.",
    "consigna_nl": "Beslis wie wat krijgt. Elke beslissing verdedig je alleen met een "
                   "familierelatie.",
    "regla": "Alleen familieargumenten tellen. «Ik wil het» of «het past bij mij» is geen "
             "argument; «es de su hermana, no de la mía» wel.",
    "pasos": [
        ("Leed la nota de la tía. No decide nada.",
         "Lees het briefje van de tante. Het beslist niets."),
        ("Cada uno elige un objeto y prepara su argumento.",
         "Ieder kiest een voorwerp en bereidt zijn argument voor."),
        ("Negociad. Solo argumentos de parentesco.",
         "Onderhandel. Alleen verwantschapsargumenten."),
        ("¿No hay acuerdo? El objeto va al museo del pueblo.",
         "Geen akkoord? Het voorwerp gaat naar het dorpsmuseum."),
    ],
    "datos": {
        "objetos": [("la guitarra de Curro", "su marido la tocaba cada domingo"),
                    ("el anillo de la bisabuela", "pasa de madre a hija desde 1890"),
                    ("las fotos del pueblo", "las hizo su hermano Paco"),
                    ("la casa de Triana", "vale mucho dinero"),
                    ("el gato Manolo", "tiene catorce años y muerde")],
        "marco": ["Es de mi …, no de la tuya.", "Su … la tocaba, entonces …",
                  "Nuestros … la usaban.", "No estoy de acuerdo: sus … "],
    },
    "clave": [
        "Er is geen juiste verdeling. Beoordeel of élke toewijzing met een familierelatie "
        "verdedigd is en of de bezittelijke voornaamwoorden kloppen.",
        "De ring is de scherpste casus: «de madre a hija» sluit de zonen uit — laat de klas "
        "dat zelf ontdekken en betwisten.",
        "De kat is bewust de minst begeerde: daar hoor je «no lo quiero» en dus de "
        "ontkenning met pronomen.",
    ],
    "nota": "Zet een klok van acht minuten. Zonder tijdsdruk blijft de klas bij het eerste "
            "voorwerp hangen.",
}

U2_RETO_08 = {
    "id": "C5-U2-RETO-08", "num": 8, "curso": "C5", "unidad": U2,
    "seccion": "§4.3", "ancla": "ser_estar", "soporte": "ppt",
    "nombre": "La foto sin pie",
    "lente": "🕵️ forensisch",
    "forma": "👥 En parejas", "skill": "👁️ Leer",
    "tiempo": "± 10 min", "dificultad": "★★★",
    "gancho_es": "Una foto, tres pies de foto. Solo uno dice la verdad.",
    "gancho_nl": "Eén foto, drie onderschriften. Maar één ervan klopt.",
    "consigna_es": "Elige el pie correcto y di qué palabra lo delata. Casi siempre es «ser» "
                   "o «estar».",
    "consigna_nl": "Kies het juiste onderschrift en zeg welk woord het verraadt. Bijna altijd "
                   "is dat «ser» of «estar».",
    "regla": "Je moet het verraderlijke wóórd aanwijzen, niet het onderschrift. Wie het "
             "juiste kiest maar het woord niet vindt, heeft geraden.",
    "pasos": [
        ("Mira la escena. ¿Qué ves exactamente?",
         "Bekijk de scène. Wat zie je precies?"),
        ("Lee los tres pies. Dos chocan con la foto.",
         "Lees de drie onderschriften. Twee botsen met de foto."),
        ("Señala la palabra que decide.",
         "Wijs het woord aan dat beslist."),
    ],
    "datos": {
        "casos": [
            ("Una chica sonríe en una fiesta, rodeada de gente.",
             [("Está contenta porque es su cumpleaños.", True, "está = hoe ze zich nu voelt"),
              ("Es contenta porque está su cumpleaños.", False, "ser/estar omgewisseld"),
              ("Está simpática y es cansada.", False, "eigenschap met estar, toestand met ser")]),
            ("Un abuelo con delantal, en la cocina, cortando cebolla.",
             [("Es cocinero y está en la cocina.", True, "beroep = ser, plaats = estar"),
              ("Está cocinero y es en la cocina.", False, "allebei omgewisseld"),
              ("Es en la cocina y está cocinero.", False, "idem, andere volgorde")]),
            ("Dos hermanos idénticos, uno con gafas.",
             [("Son gemelos, pero uno está con gafas.", False, "bril dragen = llevar, niet estar"),
              ("Son gemelos y uno lleva gafas.", True, "llevar voor kleding en bril"),
              ("Están gemelos y uno es gafas.", False, "familieband is ser, en «es gafas» bestaat niet")]),
        ],
    },
    "clave": [
        "Casus 1: het eerste. Beslissend woord: «está» (gevoel van dit moment).",
        "Casus 2: het eerste. Beslissend woord: «es cocinero» (beroep gaat met ser).",
        "Casus 3: het tweede. Beslissend woord: «lleva» — een bril draag je, die ben of "
        "sta je niet.",
        "Casus 3 is de moeilijkste omdat geen van de drie fout is op ser/estar alleen: "
        "je moet zien dat het werkwoord zelf verkeerd gekozen is.",
    ],
    "nota": "De scènes worden op de dia beschreven, niet getoond: de leerling moet ze zich "
            "voorstellen en dan pas de zinnen toetsen. Dat maakt het een taaloefening en "
            "geen zoekplaatje.",
}


# ===========================================================================
# C5 · U3 — El tiempo vuela  (parada: Barcelona)
# ===========================================================================

U3 = 3

U3_RETO_01 = {
    "id": "C5-U3-RETO-01", "num": 1, "curso": "C5", "unidad": U3,
    "seccion": "§1.3", "ancla": "hora", "soporte": "print",
    "nombre": "El horario imposible",
    "lente": "🔓 puzzel & escape", "forma": "👥 En parejas", "skill": "👁️ Leer",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "El sábado de Pau no cabe en un día. Tres citas se pisan.",
    "gancho_nl": "De zaterdag van Pau past niet in één dag. Drie afspraken botsen.",
    "consigna_es": "Encuentra los choques y reescribe la agenda para que todo quepa.",
    "consigna_nl": "Vind de botsingen en herschrijf de agenda zodat alles past.",
    "regla": "Je mag niets schrappen: alle zeven afspraken moeten erin blijven. Je mag "
             "alleen verschuiven, en elke nieuwe tijd schrijf je voluit in het Spaans.",
    "pasos": [("Lee la agenda entera antes de tocar nada.", "Lees de hele agenda vóór je iets aanraakt."),
              ("Marca los tres choques con un color.", "Markeer de drie botsingen met een kleur."),
              ("Reescribe las horas. Todo tiene que caber.", "Herschrijf de uren. Alles moet passen."),
              ("Compara con tu compañero/a: ¿misma solución?", "Vergelijk met je buur: dezelfde oplossing?")],
    "datos": {
        "agenda": [("9:00", "clase de guitarra", "1 hora"),
                   ("9:30", "desayuno con Marta", "45 minutos"),
                   ("11:00", "entrenamiento de baloncesto", "2 horas"),
                   ("12:30", "comida en casa de la abuela", "1 hora y media"),
                   ("15:00", "deberes de mates", "1 hora"),
                   ("15:30", "cine con Jordi", "2 horas"),
                   ("20:00", "cena en familia", "1 hora")],
        "marco": ["La clase de guitarra es a las …", "El desayuno no puede ser a las …, "
                  "porque …", "Lo cambio a las …"],
    },
    "clave": [
        "Drie botsingen: guitarra 9:00–10:00 tegen desayuno 9:30 · entrenamiento 11:00–13:00 "
        "tegen comida 12:30 · deberes 15:00–16:00 tegen cine 15:30.",
        "Eén werkende oplossing: desayuno naar 10:15, comida naar 13:15, deberes naar 18:00. "
        "Andere verschuivingen mogen, zolang niets meer overlapt.",
        "Let op «y media» en «y cuarto» in de herschrijving — daar zit de eigenlijke oefening.",
    ],
    "nota": "Het rekenen is licht; de moeilijkheid is dat een botsing pas zichtbaar wordt als "
            "je de duur meetelt. Wijs daar niet vooraf op.",
}

U3_RETO_03 = {
    "id": "C5-U3-RETO-03", "num": 3, "curso": "C5", "unidad": U3,
    "seccion": "§2.3", "ancla": "rutina", "soporte": "print",
    "nombre": "La rutina al revés",
    "lente": "🕵️ forensisch", "forma": "👤 Solo", "skill": "👁️ Leer",
    "tiempo": "± 10 min", "dificultad": "★★☆",
    "gancho_es": "Este día está contado de atrás hacia adelante. Ponlo derecho.",
    "gancho_nl": "Deze dag is van achter naar voor verteld. Zet hem recht.",
    "consigna_es": "Numera las frases en el orden real y añade el conector que falta.",
    "consigna_nl": "Nummer de zinnen in de echte volgorde en voeg de ontbrekende conector toe.",
    "regla": "Je mag niet op de uren afgaan — die staan er niet. Alleen de logica van de dag "
             "en de reflexieve werkwoorden verraden de volgorde.",
    "pasos": [("Lee las ocho frases. No numeres todavía.", "Lees de acht zinnen. Nummer nog niet."),
              ("Busca la primera y la última. Esas son fáciles.", "Zoek de eerste en de laatste. Die zijn makkelijk."),
              ("Numera el resto y escribe el conector.", "Nummer de rest en schrijf de conector erbij.")],
    "datos": {
        "frases": ["Me acuesto sobre las once.", "Ceno con mi familia.",
                   "Hago los deberes en mi habitación.", "Vuelvo a casa en metro.",
                   "Como en el instituto.", "Empiezan las clases.",
                   "Me ducho y me visto.", "Me despierto con el móvil."],
        "conectores": ["primero", "luego", "después", "más tarde", "por último"],
    },
    "clave": [
        "Volgorde: 1 me despierto · 2 me ducho y me visto · 3 empiezan las clases · "
        "4 como en el instituto · 5 vuelvo a casa · 6 hago los deberes · 7 ceno · 8 me acuesto.",
        "De valstrik is «hago los deberes»: die kan vóór of ná het eten, maar niet vóór "
        "«vuelvo a casa» — het huiswerk gebeurt in de kamer.",
        "Conectoren zijn niet uniek: elke ketting die logisch loopt, telt.",
    ],
    "nota": "Zonder uren erbij wordt dit een redeneeroefening in plaats van een leesoefening. "
            "Voeg ze dus niet toe als steun.",
}

U3_RETO_06 = {
    "id": "C5-U3-RETO-06", "num": 6, "curso": "C5", "unidad": U3,
    "seccion": "§2.3", "ancla": "rutina", "soporte": "print",
    "nombre": "Rutinas de otros oficios",
    "lente": "🔬 onderzoek & data", "forma": "👨‍👩‍👧 En grupos", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Un panadero, una enfermera de noche, un futbolista. Sus días no se parecen al tuyo.",
    "gancho_nl": "Een bakker, een nachtverpleegkundige, een profvoetballer. Hun dagen lijken "
                 "niet op de jouwe.",
    "consigna_es": "Reconstruye el día de uno de los tres y compáralo con el tuyo.",
    "consigna_nl": "Reconstrueer de dag van één van de drie en vergelijk hem met de jouwe.",
    "regla": "Je moet minstens twee dingen vinden die op een ándere tijd gebeuren dan bij "
             "jou, en dat mét het uur zeggen. «Werkt 's nachts» volstaat niet.",
    "pasos": [("Elegid un oficio por grupo.", "Kies één beroep per groep."),
              ("Con las pistas, escribid su día en orden.", "Schrijf met de aanwijzingen zijn dag op volgorde."),
              ("Comparad con vuestro día: ¿qué choca?", "Vergelijk met jullie dag: wat botst?"),
              ("Presentad en un minuto.", "Presenteer in één minuut.")],
    "datos": {
        "oficios": [
            ("el panadero", ["Se levanta a las tres y media de la mañana.",
                             "El pan está listo a las siete.",
                             "Come a la una y duerme la siesta.",
                             "Se acuesta a las nueve de la noche."]),
            ("la enfermera de noche", ["Se despierta a las cuatro de la tarde.",
                                       "Empieza a trabajar a las ocho de la tarde.",
                                       "Cena a medianoche en el hospital.",
                                       "Vuelve a casa a las ocho de la mañana."]),
            ("el futbolista", ["Se levanta a las siete y desayuna mucho.",
                               "Entrena de nueve a doce.",
                               "Duerme la siesta después de comer.",
                               "El sábado juega a las nueve de la noche."]),
        ],
        "marco": ["… se levanta a las …, pero yo me levanto a las …",
                  "Yo ceno a las …; él/ella cena a las …", "Lo más raro para mí es que …"],
    },
    "clave": [
        "De verpleegkundige is de scherpste vergelijking: haar «ontbijt» is ons avondeten.",
        "Let op de reflexieven in de derde persoon: se levanta, se acuesta, se despierta — "
        "leerlingen vergeten het pronomen zodra ze over iemand anders praten.",
        "«Duerme la siesta» komt twee keer voor: bruikbaar als cultureel haakje.",
    ],
    "nota": "Laat elke groep een ánder beroep nemen; bij de presentatie hoort de klas dan "
            "drie contrasten in plaats van drie keer hetzelfde.",
}

U3_RETO_07 = {
    "id": "C5-U3-RETO-07", "num": 7, "curso": "C5", "unidad": U3,
    "seccion": "§3.3", "ancla": "irregular", "soporte": "print",
    "nombre": "La app que te juzga",
    "lente": "✍️ creatieve beperking", "forma": "👤 Solo", "skill": "✍️ Escribir",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Instalas una app que analiza tu día. Y tiene opinión.",
    "gancho_nl": "Je installeert een app die je dag analyseert. En die heeft een mening.",
    "consigna_es": "Escribe tres frases sobre tu día y luego la respuesta de la app.",
    "consigna_nl": "Schrijf drie zinnen over je dag en daarna het antwoord dat de app je zou geven.",
    "regla": "De app antwoordt altijd met een werkwoord met klankverandering (empezar, poder, "
             "dormir, querer, jugar). Zonder zo'n werkwoord is het geen antwoord van de app.",
    "pasos": [("Escribe tres frases verdaderas sobre tu día.", "Schrijf drie ware zinnen over je dag."),
              ("Ahora eres la app. Contesta a cada una.", "Nu ben jij de app. Antwoord op elke zin."),
              ("¿Es dura o amable tu app? Elige y sé constante.", "Is jouw app streng of vriendelijk? Kies en hou vol.")],
    "datos": {
        "modelos": [("Duermo cinco horas.", "No puedes dormir cinco horas. Empieza a las diez."),
                    ("Juego dos horas al móvil.", "¿Quieres jugar menos? Prueba una hora.")],
        "verbos": ["empezar (e→ie)", "poder (o→ue)", "dormir (o→ue)", "querer (e→ie)",
                   "jugar (u→ue)", "pedir (e→i)"],
    },
    "clave": [
        "Elk app-antwoord moet minstens één werkwoord met klankverandering bevatten, correct "
        "vervoegd. Dat is het toetsbare deel.",
        "Veelgemaakte fout: «podes» in plaats van «puedes», en «dormo» in plaats van «duermo».",
        "De nosotros-vorm verandert níét: «podemos», «dormimos» — laat dat opvallen als "
        "iemand de app in de wij-vorm laat spreken.",
    ],
    "nota": "De toon van de app is vrij. Laat leerlingen kiezen: dat is waar het plezier zit, "
            "en de grammatica ligt er los van.",
}

U3_RETO_05 = {
    "id": "C5-U3-RETO-05", "num": 5, "curso": "C5", "unidad": U3,
    "seccion": "§2.3", "ancla": "rutina", "soporte": "hub",
    "nombre": "El reloj de la ciudad",
    "lente": "📻 mediaformat", "forma": "👤 Solo", "skill": "👂 Escuchar",
    "tiempo": "± 10 min", "dificultad": "★★☆",
    "gancho_es": "Barcelona se despierta por partes. Escucha y di qué pasa a esa hora.",
    "gancho_nl": "Barcelona wordt in stukken wakker. Luister en zeg wat er op dat uur gebeurt.",
    "consigna_es": "Oyes una hora y una escena. Elige el verbo reflexivo que encaja.",
    "consigna_nl": "Je hoort een uur en een scène. Kies het reflexieve werkwoord dat past.",
    "regla": "Je kiest op wat je hoort, niet op wat logisch lijkt. Twee scènes passen bij "
             "hetzelfde werkwoord — daar beslist het uur.",
    "pasos": [("Escucha la escena entera antes de elegir.", "Luister de hele scène af vóór je kiest."),
              ("Elige el verbo. Fíjate en la hora.", "Kies het werkwoord. Let op het uur."),
              ("¿Fallas? Vuelve a escuchar antes de leer.", "Fout? Luister opnieuw vóór je leest.")],
    "datos": {
        "items": [
            ("Son las siete menos cuarto. Suena el despertador en toda la escalera.",
             "se despiertan", ["se despiertan", "se acuestan", "se duchan"]),
            ("Son las siete y media. Se oye el agua en todos los pisos.",
             "se duchan", ["se duchan", "se peinan", "se van"]),
            ("Son las ocho. La puerta del portal no para de abrirse.",
             "se van", ["se van", "se levantan", "se sientan"]),
            ("Son las dos. En el bar de abajo no cabe nadie más.",
             "se sientan", ["se sientan", "se duermen", "se lavan"]),
            ("Son las cuatro. En el parque casi nadie habla.",
             "se duermen", ["se duermen", "se despiertan", "se visten"]),
            ("Son las once de la noche. Se apagan las luces una a una.",
             "se acuestan", ["se acuestan", "se levantan", "se duchan"]),
        ],
    },
    "clave": [
        "se despiertan · se duchan · se van · se sientan · se duermen · se acuestan",
        "Item 1 en 6 delen het thema slapen; alleen het uur (7:45 tegenover 23:00) beslist.",
        "Alle werkwoorden staan in de derde persoon meervoud: het gaat over de stad, niet "
        "over één iemand.",
    ],
    "nota": "Zolang er geen opnames zijn, leest de computerstem de scènes voor. Dat werkt: "
            "de zinnen zijn kort en de klemtoon ligt op het uur.",
}

U3_RETO_04 = {
    "id": "C5-U3-RETO-04", "num": 4, "curso": "C5", "unidad": U3,
    "seccion": "§3.3", "ancla": "irregular", "soporte": "hub",
    "nombre": "Un día en 60 segundos",
    "lente": "🎭 simulatie met beperking", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Tu día entero en exactamente sesenta segundos. Ni más, ni menos.",
    "gancho_nl": "Je hele dag in exact zestig seconden. Niet meer, niet minder.",
    "consigna_es": "Graba tu día tres veces. Cada vez tienes que llegar más cerca del minuto.",
    "consigna_nl": "Neem je dag drie keer op. Elke keer moet je dichter bij de minuut komen.",
    "regla": "Exact zestig seconden. Te kort betekent dat je iets moet toevoegen, te lang dat "
             "je moet schrappen — niet dat je sneller mag praten.",
    "pasos": [("Primer intento: cuenta tu día sin preparar.", "Eerste poging: vertel je dag zonder voorbereiding."),
              ("Mira el tiempo. ¿Sobra o falta?", "Kijk naar de tijd. Te veel of te weinig?"),
              ("Segundo intento: ajusta el contenido, no la velocidad.", "Tweede poging: pas de inhoud aan, niet je tempo."),
              ("Tercer intento: el bueno.", "Derde poging: de goede.")],
    "datos": {
        "marco": ["Me levanto a las …", "Primero … , luego …", "A mediodía …",
                  "Por la tarde … porque …", "Y por último …"],
        "modelos": [("demasiado corto", "voeg een reden toe met «porque» of een frequentie "
                                        "met «siempre / a veces / nunca»"),
                    ("demasiado largo", "schrap de details van het ontbijt — die vertelt iedereen")],
    },
    "clave": [
        "Beoordeel de derde opname, niet de eerste. De winst zit in het aanpassen.",
        "Wie te kort zit, voegt meestal geen inhoud maar stopwoorden toe. Stuur naar «porque» "
        "en naar frequentiewoorden.",
        "Zestig seconden is ongeveer acht tot tien zinnen op dit niveau.",
    ],
    "nota": "De timer op de hub telt mee. Laat leerlingen niet naar de klok kijken tijdens "
            "het spreken — dat maakt van de oefening een leesbeurt.",
}

U3_RETO_09 = {
    "id": "C5-U3-RETO-09", "num": 9, "curso": "C5", "unidad": U3,
    "seccion": "Cultura", "ancla": "cultura_u3", "soporte": "hub",
    "nombre": "Subtítulos para la abuela",
    "lente": "🤝 bemiddelen", "forma": "👥 En parejas", "skill": "🔀 Mediar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Tu abuela no sigue el vídeo: van demasiado rápido.",
    "gancho_nl": "Je oma volgt de video niet: ze praten te snel.",
    "consigna_es": "Convierte cada frase rápida en un subtítulo corto y claro.",
    "consigna_nl": "Zet elke snelle zin om in een korte, heldere ondertitel.",
    "regla": "Maximaal acht woorden per ondertitel, en de betekenis moet heel blijven. "
             "Je comprimeert, je vertaalt niet.",
    "pasos": [("Escucha la frase entera.", "Luister de hele zin af."),
              ("¿Qué es lo esencial? Quita el resto.", "Wat is de kern? Schrap de rest."),
              ("Escribe el subtítulo. Cuenta las palabras.", "Schrijf de ondertitel. Tel je woorden.")],
    "datos": {
        "frases": [
            ("Pues mira, normalmente me levanto sobre las siete menos cuarto, aunque los "
             "viernes me quedo un ratito más en la cama.", "Me levanto a las siete menos cuarto."),
            ("La verdad es que no desayuno casi nunca porque no tengo hambre tan temprano "
             "por la mañana.", "Casi nunca desayuno."),
            ("Los martes por la tarde tengo clase de guitarra y luego, si me da tiempo, "
             "quedo con Jordi en la plaza.", "Los martes: guitarra y luego Jordi."),
            ("Suelo acostarme bastante tarde, sobre las once y media o incluso las doce si "
             "estoy viendo una serie.", "Me acuesto a las once y media."),
        ],
    },
    "clave": [
        "Modelondertitels staan hierboven; elke variant van acht woorden of minder die de "
        "kern behoudt, is goed.",
        "Zin 3 is de moeilijkste: er zitten twee gebeurtenissen in en beide moeten blijven.",
        "Wat mag sneuvelen: «pues mira», «la verdad es que», «suelo». Wat niet: het uur, "
        "de dag, en de ontkenning.",
    ],
    "nota": "De limiet van acht woorden is het hele punt. Zonder harde limiet schrijven "
            "leerlingen de zin gewoon over.",
}

U3_RETO_02 = {
    "id": "C5-U3-RETO-02", "num": 2, "curso": "C5", "unidad": U3,
    "seccion": "§1.3", "ancla": "hora", "soporte": "ppt",
    "nombre": "Zona horaria",
    "lente": "🔬 onderzoek & data", "forma": "👨‍👩‍👧 En grupos", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Una videollamada con Cusco, CDMX y Sevilla. Alguien siempre está durmiendo.",
    "gancho_nl": "Een videogesprek met Cusco, CDMX en Sevilla. Er slaapt altijd iemand.",
    "consigna_es": "Encontrad la única hora en la que los cuatro estáis despiertos.",
    "consigna_nl": "Zoek het enige uur waarop jullie alle vier wakker zijn.",
    "regla": "Iedereen moet tussen 8:00 en 22:00 lokale tijd zitten. Eén persoon buiten dat "
             "venster en het voorstel valt af.",
    "pasos": [("Mirad las cuatro zonas horarias.", "Bekijk de vier tijdzones."),
              ("Probad una hora. ¿Quién duerme?", "Probeer een uur. Wie slaapt er?"),
              ("Buscad la ventana común.", "Zoek het gemeenschappelijke venster."),
              ("Escribid la invitación con la hora de cada uno.", "Schrijf de uitnodiging met ieders lokale uur.")],
    "datos": {
        "zonas": [("Gante (Bélgica)", 0), ("Sevilla (España)", 0),
                  ("Ciudad de México", -7), ("Cusco (Perú)", -6)],
        "marco": ["En Gante son las …, en México son las … y en Cusco son las …",
                  "A las … de Bélgica, en México es demasiado temprano.",
                  "Quedamos a las … hora belga."],
    },
    "clave": [
        "Venster: 15:00–22:00 Belgische tijd. Dan is het 8:00–15:00 in Mexico en "
        "9:00–16:00 in Cusco.",
        "16:00 Belgisch is een veilige keuze: 9:00 in CDMX, 10:00 in Cusco, 16:00 in Sevilla.",
        "Sevilla en Gante delen de tijdzone — dat is de gratis vereenvoudiging die de klas "
        "meestal over het hoofd ziet.",
        "Verschillen zijn winterwaarden; met zomertijd schuift het één uur. Vermeld dat als "
        "een leerling ernaar vraagt.",
    ],
    "nota": "Reken met hele uren. Zodra de klas over zomertijd begint, wordt het een "
            "rekenles in plaats van een taalles.",
}

U3_RETO_08 = {
    "id": "C5-U3-RETO-08", "num": 8, "curso": "C5", "unidad": U3,
    "seccion": "§2.3", "ancla": "rutina", "soporte": "ppt",
    "nombre": "Negocia el despertador",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Dos compañeros de habitación, dos mañanas incompatibles. Una sola alarma.",
    "gancho_nl": "Twee kamergenoten, twee onverenigbare ochtenden. Eén wekker.",
    "consigna_es": "Negociad un horario común. Los dos tenéis que ceder en algo.",
    "consigna_nl": "Onderhandel één gezamenlijk schema. Jullie moeten allebei iets opgeven.",
    "regla": "Elk voorstel bevat een uur én een reden met «porque». Een voorstel zonder "
             "reden mag de ander zonder meer weigeren.",
    "pasos": [("Coge tu rol. No lo enseñes.", "Neem je rol. Laat hem niet zien."),
              ("Propón tu hora con una razón.", "Stel je uur voor met een reden."),
              ("Ceded hasta llegar a un acuerdo.", "Geef toe tot jullie akkoord zijn."),
              ("Escribid la hora final en la pizarra.", "Schrijf het eindresultaat op het bord.")],
    "datos": {
        "roles": [("Álex", "Entrenas a las siete de la mañana. Necesitas la ducha primero. "
                           "Te acuestas a las diez."),
                  ("Noa", "Estudias hasta la una de la madrugada. No puedes levantarte antes "
                          "de las nueve. La luz te despierta.")],
        "marco": ["Quiero levantarme a las … porque …", "No puedo … porque …",
                  "¿Y si … a las …?", "Vale, pero entonces tú …"],
    },
    "clave": [
        "Er is geen juiste uitkomst, wel een toetsbare: bevat elk voorstel een uur én "
        "«porque», en heeft élk van de twee iets opgegeven?",
        "De meest gevonden oplossing: wekker om 6:45 met de douche 's avonds voor Álex, en "
        "een slaapmasker voor Noa.",
        "Let op «poder»: «no puedo levantarme» — de o→ue-verandering zit precies in het "
        "werkwoord dat de hele onderhandeling draagt.",
    ],
    "nota": "Geef de rollen echt gescheiden. Zien de leerlingen elkaars kaart, dan verdwijnt "
            "de onderhandeling en blijft er een invuloefening over.",
}

U3_RETO_10 = {
    "id": "C5-U3-RETO-10", "num": 10, "curso": "C5", "unidad": U3,
    "seccion": "Cultura", "ancla": "cultura_u3", "soporte": "ppt",
    "nombre": "La coartada",
    "lente": "🕵️ forensisch", "forma": "🏫 Toda la clase", "skill": "🗣️ Hablar",
    "tiempo": "± 20 min", "dificultad": "★★★",
    "gancho_es": "Ha desaparecido la mascota de la clase. Todos tenéis que dar cuentas.",
    "gancho_nl": "De klasmascotte is verdwenen. Iedereen moet rekenschap geven.",
    "consigna_es": "En parejas inventáis una coartada con cinco horas. La clase os interroga.",
    "consigna_nl": "Per twee verzinnen jullie een alibi met vijf uren. De klas verhoort jullie.",
    "regla": "Jullie twee verhalen moeten op de vijf uren identiek zijn — maar jullie worden "
             "apart ondervraagd. Eén verschil en het alibi valt.",
    "pasos": [("En parejas: inventad vuestra tarde, hora por hora.", "Per twee: verzin jullie namiddag, uur per uur."),
              ("Memorizad. No podéis mirar notas en el interrogatorio.", "Onthoud het. Bij het verhoor geen notities."),
              ("Uno sale del aula. La clase interroga al otro.", "Eén verlaat het lokaal. De klas verhoort de ander."),
              ("Entra el segundo. ¿Coinciden?", "De tweede komt binnen. Komen ze overeen?")],
    "datos": {
        "preguntas": [("¿A qué hora salisteis del instituto?", "vertrek"),
                      ("¿Dónde estabais a las cinco?", "plaats"),
                      ("¿Qué hacíais a las seis?", "bezigheid"),
                      ("¿A qué hora volvisteis a casa?", "terugkeer"),
                      ("¿Con quién estabais?", "getuige")],
        "marco": ["A las … salimos del instituto.", "A las … estamos en …",
                  "Después vamos a … y volvemos a las …"],
    },
    "clave": [
        "Het alibi valt bijna altijd op vraag 3 of 5: de bezigheid en de getuige worden "
        "zelden even gedetailleerd afgesproken als de uren.",
        "Alles blijft in het presente: de vragen staan hier in de verleden tijd omdat de "
        "leerkracht ze stelt, maar de antwoorden mogen in het presente («a las cinco "
        "estamos en el parque»). Geen verleden tijd vragen van de leerlingen.",
        "Wie een detail vergeet, mag het niet verzinnen: dan valt het alibi. Dat is de motor.",
    ],
    "nota": "Werkt met maximaal zes duo's; daarna zakt de spanning. Laat de rest van de klas "
            "de tegenstrijdigheden noteren, dan luistert iedereen mee.",
}


# ===========================================================================
# C5 · U4 — Me gusta  (parada: València · la costa)
# ===========================================================================

U4 = 4

U4_RETO_04 = {
    "id": "C5-U4-RETO-04", "num": 4, "curso": "C5", "unidad": U4,
    "seccion": "§3.3", "ancla": "planes", "soporte": "print",
    "nombre": "Cita a ciegas de planes",
    "lente": "🎭 simulatie met beperking", "forma": "👨‍👩‍👧 En grupos", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Propones un plan a alguien que no ves. Solo pasan papelitos.",
    "gancho_nl": "Je stelt een plan voor aan iemand die je niet ziet. Alleen briefjes gaan heen en weer.",
    "consigna_es": "Tres rondas de notas: proponer, reaccionar, cerrar la cita. Sin hablar.",
    "consigna_nl": "Drie rondes briefjes: voorstellen, reageren, de afspraak sluiten. Zonder praten.",
    "regla": "Er wordt niet gesproken en niet gewezen. Alles gaat via het briefje, en elke "
             "reactie begint met «a mí también», «a mí tampoco», «a mí sí» of «a mí no».",
    "pasos": [("Ronda 1: escribe un plan y un gusto tuyo.", "Ronde 1: schrijf een plan en één eigen gusto."),
              ("Ronda 2: reacciona al plan que recibes.", "Ronde 2: reageer op het plan dat je krijgt."),
              ("Ronda 3: cerrad hora y lugar.", "Ronde 3: spreek uur en plaats af."),
              ("Y ahora sí: mirad quién era.", "En nu pas: kijk wie het was.")],
    "datos": {
        "marco_1": ["Me gusta … y quiero …", "¿Quieres … el sábado?"],
        "marco_2": ["A mí también, pero …", "A mí no. Prefiero …", "A mí tampoco me gusta …"],
        "marco_3": ["¿Quedamos a las … en …?", "Vale, pero mejor a las …"],
        "planes": ["ir a la playa", "ver una peli", "jugar al pádel", "ir al mercado",
                   "escuchar música en el parque", "hacer una ruta en bici"],
    },
    "clave": [
        "De vier reacties moeten alle vier ergens in de klas voorkomen. Vraag er achteraf "
        "naar: wie heeft «a mí tampoco» gebruikt?",
        "«A mí tampoco» kan alleen ná een ontkenning — dat is de valstrik. Wie het na een "
        "positieve zin schrijft, herschrijft het briefje.",
        "Ronde 3 dwingt «quedamos» af: het is de enige manier om uur én plaats in één zin te "
        "zetten.",
    ],
    "nota": "Briefjes anoniem houden tot het einde. Zodra leerlingen weten met wie ze "
            "schrijven, praten ze — en dan is de beperking weg.",
}

U4_RETO_05 = {
    "id": "C5-U4-RETO-05", "num": 5, "curso": "C5", "unidad": U4,
    "seccion": "§3.3", "ancla": "planes", "soporte": "print",
    "nombre": "El presupuesto del finde",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Veinticinco euros, cuatro planes, un fin de semana. No cabe todo.",
    "gancho_nl": "Vijfentwintig euro, vier plannen, één weekend. Alles past niet.",
    "consigna_es": "Elegid juntos qué hacéis. Cada uno tiene que renunciar a un plan propio.",
    "consigna_nl": "Kies samen wat jullie doen. Ieder moet één eigen plan opgeven.",
    "regla": "Het budget is hard: vijfentwintig euro voor de hele groep. En iedereen moet "
             "minstens één keer «a mí no me gusta» of «prefiero» gebruiken om iets te schrappen.",
    "pasos": [("Cada uno elige su plan favorito y su precio.", "Ieder kiest zijn favoriete plan en de prijs."),
              ("Sumad. ¿Cuánto os pasáis?", "Tel op. Hoeveel gaan jullie erover?"),
              ("Negociad hasta llegar a veinticinco.", "Onderhandel tot jullie op vijfentwintig zitten."),
              ("Escribid el plan final con horas.", "Schrijf het eindplan met uren.")],
    "datos": {
        "planes": [("entrada al cine", 8), ("bocadillo y bebida", 6), ("bus a la playa", 4),
                   ("alquilar una bici", 7), ("entrada al museo", 5), ("helado", 3),
                   ("pádel una hora", 10), ("mercado: fruta para todos", 6)],
        "marco": ["A mí me gustaría … , pero cuesta …", "Prefiero … porque es más barato.",
                  "Si quitamos …, nos quedan … euros.", "Entonces quedamos a las … en …"],
    },
    "clave": [
        "Er is geen juiste combinatie; er zijn er meerdere die op precies vijfentwintig "
        "uitkomen (bijvoorbeeld bus 4 + bocadillo 6 + helado 3 + museo 5 + fruta 6 = 24).",
        "Toets twee dingen: klopt de som, en heeft élk groepslid één keer geschrapt met een "
        "gusto-uitdrukking?",
        "«Me gustaría» staat bewust in het marco als chunk, niet als tijd om te leren — het "
        "is geen condicional-les.",
    ],
    "nota": "Vijfentwintig euro is krap gekozen. Bij een ruimer budget verdwijnt de "
            "onderhandeling en blijft er een boodschappenlijst over.",
}

U4_RETO_07 = {
    "id": "C5-U4-RETO-07", "num": 7, "curso": "C5", "unidad": U4,
    "seccion": "Cultura", "ancla": "cultura_u4", "soporte": "print",
    "nombre": "El anuncio que no miente",
    "lente": "✍️ creatieve beperking", "forma": "👥 En parejas", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Escribe un anuncio de València en el que todo sea verdad. También lo malo.",
    "gancho_nl": "Schrijf een reclame voor València waarin alles waar is. Ook het slechte.",
    "consigna_es": "Seis frases: tres cosas buenas, dos menos buenas, y una que sigue "
                   "convenciendo igual.",
    "consigna_nl": "Zes zinnen: drie goede dingen, twee minder goede, en één die tóch nog "
                   "overtuigt.",
    "regla": "Niets weglaten en niets overdrijven. «Siempre hace sol» mag niet — «en verano "
             "hace mucho calor, a veces demasiado» wel.",
    "pasos": [("Mirad los datos. Elegid tres cosas buenas.", "Bekijk de gegevens. Kies drie goede dingen."),
              ("Elegid dos menos buenas. No las suavicéis.", "Kies twee minder goede. Verzacht ze niet."),
              ("Escribid la frase final: ¿por qué venir igualmente?", "Schrijf de slotzin: waarom tóch komen?")],
    "datos": {
        "hechos": [("playa en la ciudad", "bueno"), ("paella valenciana", "bueno"),
                   ("bicis por todas partes", "bueno"), ("Ciudad de las Artes", "bueno"),
                   ("en agosto: 35 grados y mucha humedad", "menos bueno"),
                   ("en verano hay muchísimos turistas", "menos bueno"),
                   ("el centro es caro para comer", "menos bueno"),
                   ("las Fallas: ruido día y noche en marzo", "depende")],
        "marco": ["En València hay …", "Me gusta … porque …", "No me gusta … , pero …",
                  "Si te gusta … , València te encanta."],
    },
    "clave": [
        "«Las Fallas» is het scharnier: voor de één een reden om te komen, voor de ander om "
        "weg te blijven. Beide zijn juist, mits onderbouwd.",
        "Toets op de twee negatieve zinnen: staan ze er écht, en zonder «pero» meteen "
        "weggepoetst?",
        "Sterke slotzinnen gebruiken een voorwaarde met «si» plus gustar — dat is precies de "
        "structuur van de unit.",
    ],
    "nota": "De opdracht traint eerlijk schrijven én genuanceerd smaakgebruik. Laat de "
            "negatieve zinnen niet wegvallen in de correctie.",
}

U4_RETO_10 = {
    "id": "C5-U4-RETO-10", "num": 10, "curso": "C5", "unidad": U4,
    "seccion": "Cultura", "ancla": "cultura_u4", "soporte": "print",
    "nombre": "La encuesta de la costa",
    "lente": "🔬 onderzoek & data", "forma": "👤 Solo", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★☆",
    "gancho_es": "¿Playa o montaña? Pregúntalo de verdad y cuenta los votos.",
    "gancho_nl": "Strand of bergen? Vraag het echt en tel de stemmen.",
    "consigna_es": "Encuesta a tres compañeros, dibuja el diagrama y defiende una conclusión.",
    "consigna_nl": "Ondervraag drie klasgenoten, teken het diagram en verdedig één conclusie.",
    "regla": "Je conclusie moet een getal bevatten én een reactie met también of tampoco. "
             "Een conclusie zonder cijfer is een mening, geen resultaat.",
    "pasos": [("Haz las tres preguntas a tres personas.", "Stel de drie vragen aan drie personen."),
              ("Anota las respuestas tal cual.", "Noteer de antwoorden letterlijk."),
              ("Dibuja el diagrama y escribe la conclusión.", "Teken het diagram en schrijf de conclusie."),
              ("Léela a la clase. ¿Están de acuerdo?", "Lees ze voor. Is de klas het ermee eens?")],
    "datos": {
        "preguntas": [("¿Te gusta más la playa o la montaña?", "playa / montaña"),
                      ("¿Te gusta madrugar en vacaciones?", "sí / no"),
                      ("¿Qué prefieres: música o silencio?", "música / silencio")],
        "marco": ["A … de tres personas les gusta …", "A mí también / a mí no.",
                  "Solo a … le gusta …", "A nadie le gusta …"],
    },
    "clave": [
        "Let op de vorm: «A dos personas LES gusta» (meervoud) tegenover «A una persona LE "
        "gusta». Daar gaat het het vaakst mis.",
        "«A nadie le gusta» is enkelvoud — een geliefde valstrik.",
        "De cijfers verschillen per klas; toets de vorm en de aanwezigheid van een reactie.",
    ],
    "nota": "Drie respondenten is genoeg. Bij meer wordt het turven belangrijker dan het "
            "formuleren.",
}

U4_RETO_02 = {
    "id": "C5-U4-RETO-02", "num": 2, "curso": "C5", "unidad": U4,
    "seccion": "§1.3", "ancla": "gustar", "soporte": "hub",
    "nombre": "La playlist heredada",
    "lente": "🕵️ forensisch", "forma": "👤 Solo", "skill": "✍️ Escribir",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Encuentras un móvil con una playlist. ¿Quién es esta persona?",
    "gancho_nl": "Je vindt een gsm met een playlist erop. Wie is deze persoon?",
    "consigna_es": "Escucha los ocho títulos y deduce sus gustos. Escribe su perfil en cinco frases.",
    "consigna_nl": "Beluister de acht titels en leid haar smaak af. Schrijf haar profiel in vijf zinnen.",
    "regla": "Elke zin over die persoon moet met «le gusta» of «le encanta» — niet met «me». "
             "Je praat over iemand anders, niet over jezelf.",
    "pasos": [("Escucha la playlist entera.", "Beluister de hele playlist."),
              ("¿Qué se repite? ¿Qué falta?", "Wat komt terug? Wat ontbreekt?"),
              ("Escribe cinco frases sobre esa persona.", "Schrijf vijf zinnen over die persoon."),
              ("Compara con la clase: ¿misma persona?", "Vergelijk met de klas: dezelfde persoon?")],
    "datos": {
        "playlist": [("Flamenco de Jerez, vol. 2", "flamenco"),
                     ("Rosalía — grandes éxitos", "flamenco-pop"),
                     ("Sonidos del mar (para dormir)", "relajación"),
                     ("Reggaetón 2019", "reguetón"),
                     ("Camarón de la Isla", "flamenco"),
                     ("Clásicos de guitarra española", "clásica"),
                     ("Estudiar sin distracciones", "concentración"),
                     ("Salsa en la cocina", "salsa")],
        "marco": ["Le gusta …", "Le encanta … porque …", "No le gustan …",
                  "Creo que … porque tiene …", "Es una persona …"],
    },
    "clave": [
        "Vijf van de acht titels wijzen naar Spaanse en flamenco-muziek; twee naar rust en "
        "studeren; één (reguetón, van 2019) valt eruit — een oude playlist die is blijven staan.",
        "Sterke deducties: houdt van gitaar, studeert veel, luistert naar muziek om te slapen.",
        "Toets de vorm: «le gusta» enkelvoud, «le gustan» bij meervoud (los sonidos, los "
        "clásicos). Dat is de eigenlijke grammaticawinst.",
    ],
    "nota": "De titels zijn verzonnen behalve de artiestennamen; Camarón en Rosalía zijn "
            "echt en horen bij de Cultura-sectie van deze unit.",
}

U4_RETO_06 = {
    "id": "C5-U4-RETO-06", "num": 6, "curso": "C5", "unidad": U4,
    "seccion": "§1.3", "ancla": "gustar", "soporte": "hub",
    "nombre": "Gustos que cambian",
    "lente": "✍️ creatieve beperking", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 10 min", "dificultad": "★★☆",
    "gancho_es": "Lo que te gustaba a los diez años no es lo que te gusta hoy.",
    "gancho_nl": "Wat je op je tiende leuk vond, is niet wat je nu leuk vindt.",
    "consigna_es": "Graba cuatro contrastes: antes y ahora. Todo en presente.",
    "consigna_nl": "Neem vier contrasten op: vroeger en nu. Alles in het presente.",
    "regla": "Je mag geen verleden tijd gebruiken — die ken je nog niet. Je zegt dus «a los "
             "diez años me gusta…» met een tijdsbepaling, niet «me gustaba».",
    "pasos": [("Piensa en cuatro cosas que han cambiado.", "Denk aan vier dingen die veranderd zijn."),
              ("Formula cada una con una expresión de tiempo.", "Formuleer elk met een tijdsbepaling."),
              ("Graba los cuatro contrastes seguidos.", "Neem de vier contrasten na elkaar op."),
              ("Escúchate: ¿se entiende el cambio?", "Luister terug: is de verandering duidelijk?")],
    "datos": {
        "marco": ["A los diez años me gusta … ; ahora me gusta más …",
                  "Antes me encanta … ; hoy no tanto.",
                  "De pequeño/-a no me gusta … ; ahora sí."],
        "ejemplos": ["los dibujos animados", "el chocolate", "levantarme temprano",
                     "los videojuegos", "leer", "el deporte", "la música de mis padres"],
    },
    "clave": [
        "De opdracht bereidt het imperfecto voor zonder het te geven: leerlingen voelen dat "
        "er een vorm ontbreekt. Benoem dat — het komt in het zesde jaar.",
        "Toets alleen op presente plus tijdsbepaling. Wie «me gustaba» gebruikt omdat hij het "
        "ergens oppikte, corrigeer je niet, maar reken je ook niet aan.",
        "Vier contrasten is genoeg voor ongeveer veertig seconden.",
    ],
    "nota": "Hier zit de brug naar C6+ U6 «Cuando era pequeño». Zeg dat er hardop bij: "
            "leerlingen onthouden een tekort beter dan een regel.",
}

U4_RETO_09 = {
    "id": "C5-U4-RETO-09", "num": 9, "curso": "C5", "unidad": U4,
    "seccion": "§2.3", "ancla": "reacciones", "soporte": "hub",
    "nombre": "Traduce el gusto, no la palabra",
    "lente": "🤝 bemiddelen", "forma": "👥 En parejas", "skill": "🔀 Mediar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Cuatro frases flamencas que, traducidas palabra por palabra, no significan nada.",
    "gancho_nl": "Vier Vlaamse uitdrukkingen die, woord voor woord vertaald, niets betekenen.",
    "consigna_es": "Elige lo que dice de verdad un/a joven español/-a. Y di por qué la "
                   "traducción literal falla.",
    "consigna_nl": "Kies wat een Spaanse tiener écht zou zeggen. En zeg waarom de letterlijke "
                   "vertaling misloopt.",
    "regla": "Het juiste antwoord kiezen volstaat niet: je moet erbij zeggen wat er misgaat "
             "in de letterlijke versie. Zonder die uitleg telt het als gokken.",
    "pasos": [("Lee la frase flamenca. No traduzcas todavía.", "Lees de Vlaamse zin. Vertaal nog niet."),
              ("Elige la versión que suena natural.", "Kies de versie die natuurlijk klinkt."),
              ("Explica qué falla en la literal.", "Leg uit wat er misloopt in de letterlijke.")],
    "datos": {
        "items": [
            ("Ik heb er niks mee.", "No me dice nada.",
             ["No me dice nada.", "No tengo nada con eso.", "No tengo nada."],
             "«hebben met» bestaat niet als uitdrukking; het Spaans gebruikt «decir»"),
            ("Dat is echt mijn ding.", "Eso es lo mío.",
             ["Eso es lo mío.", "Eso es mi cosa.", "Eso es mi asunto."],
             "«mijn ding» wordt «lo mío», niet «mi cosa»"),
            ("Ik vind er niks aan.", "No me gusta nada.",
             ["No me gusta nada.", "No encuentro nada a eso.", "No hay nada para mí."],
             "«vinden» is hier smaak, geen zoeken — dus gustar, niet encontrar"),
            ("Daar kan ik niet tegen.", "No lo aguanto.",
             ["No lo aguanto.", "No puedo contra eso.", "No estoy contra eso."],
             "«tegen kunnen» is verdragen: aguantar, niet «poder contra»"),
        ],
    },
    "clave": [
        "No me dice nada · Eso es lo mío · No me gusta nada · No lo aguanto.",
        "De rode draad: het Nederlands gebruikt hebben, vinden en kunnen waar het Spaans een "
        "eigen werkwoord heeft (decir, gustar, aguantar).",
        "«No lo aguanto» sluit aan bij de escala uit de Cultura-sectie, tussen «no me gusta» "
        "en «odio».",
    ],
    "nota": "Dit is bemiddelen in de strikte zin: betekenis overzetten, niet woorden. Laat de "
            "letterlijke versies hardop lezen — het lachen is de didactiek.",
}

U4_RETO_01 = {
    "id": "C5-U4-RETO-01", "num": 1, "curso": "C5", "unidad": U4,
    "seccion": "§1.3", "ancla": "gustar", "soporte": "ppt",
    "nombre": "El termómetro de la clase",
    "lente": "🔬 onderzoek & data", "forma": "🏫 Toda la clase · de pie", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★☆",
    "gancho_es": "De pie. La clase es una escala: de «odio» a «me encanta».",
    "gancho_nl": "Rechtstaan. De klas is een schaal: van «odio» tot «me encanta».",
    "consigna_es": "Colócate en la línea según lo que sientas. Después contamos y sacamos "
                   "una conclusión.",
    "consigna_nl": "Ga op de lijn staan naargelang wat je vindt. Daarna tellen we en trekken "
                   "we een conclusie.",
    "regla": "Je mag niet in het midden blijven hangen: kies een van de vier plaatsen. En wie "
             "gevraagd wordt, verantwoordt zijn plek met «porque».",
    "pasos": [("El/la profe dice una cosa. Todos se colocan.", "De leerkracht noemt iets. Iedereen gaat staan."),
              ("Dos alumnos explican su sitio con «porque».", "Twee leerlingen verantwoorden hun plek met «porque»."),
              ("Contamos y anotamos el número.", "We tellen en noteren het getal."),
              ("Al final: tres conclusiones con «a … le gusta».", "Op het einde: drie conclusies met «a … le gusta».")],
    "datos": {
        "escala": ["odio", "no me gusta", "me gusta", "me encanta"],
        "temas": ["madrugar", "la playa", "el reguetón", "cocinar", "los lunes",
                  "los viajes en tren", "hablar en público", "el chocolate negro"],
        "marco": ["Estoy aquí porque …", "A … personas les encanta …",
                  "A nadie le gusta …", "Casi todos …"],
    },
    "clave": [
        "De conclusies zijn de eigenlijke opbrengst: «a doce personas les gusta la playa» "
        "vraagt les plus meervoud, en dat is precies wat leerlingen vergeten.",
        "«Hablar en público» geeft meestal de breedste spreiding en dus het interessantste "
        "gesprek.",
        "Tel echt en schrijf het getal op het bord: zonder cijfer wordt het een meningenronde.",
    ],
    "nota": "Werkt alleen als de klas fysiek kan bewegen. Lukt dat niet, laat de leerlingen "
            "dan met vier vingers stemmen — maar tel nog steeds.",
}

U4_RETO_03 = {
    "id": "C5-U4-RETO-03", "num": 3, "curso": "C5", "unidad": U4,
    "seccion": "§2.3", "ancla": "reacciones", "soporte": "ppt",
    "nombre": "Radio Valencia: la llamada",
    "lente": "📻 mediaformat", "forma": "🏫 Toda la clase", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Estás en directo. Pides una canción y dices por qué.",
    "gancho_nl": "Je bent live in de uitzending. Je vraagt een nummer aan en zegt waarom.",
    "consigna_es": "Llama a la radio, saluda, pide tu canción y explica. El presentador reacciona.",
    "consigna_nl": "Bel de radio, groet, vraag je nummer aan en licht toe. De presentator reageert.",
    "regla": "De presentator reageert altijd met también, tampoco, a mí sí of a mí no — en "
             "nooit twee keer dezelfde in één uitzending.",
    "pasos": [("El/la profe es el presentador. Empieza la emisión.", "De leerkracht is presentator. De uitzending begint."),
              ("Llamas: saludo, canción, razón.", "Je belt: groet, nummer, reden."),
              ("El presentador reacciona y pasa al siguiente.", "De presentator reageert en gaat door."),
              ("Cambio de presentador cada cuatro llamadas.", "Elke vier oproepen wisselt de presentator.")],
    "datos": {
        "marco_llamada": ["Hola, buenas tardes. Llamo desde …",
                          "Quiero pedir … porque me encanta …",
                          "Es para mi … , que hoy cumple años."],
        "marco_presentador": ["¡A mí también me encanta!", "Pues a mí no, pero la ponemos.",
                              "A mí tampoco me gusta mucho, la verdad.",
                              "¿Ah sí? A mí sí, y mucho."],
        "canciones": ["una de Rosalía", "algo de flamenco", "reguetón del verano",
                      "una canción tranquila", "la de la película", "algo para bailar"],
    },
    "clave": [
        "De regel «nooit twee keer dezelfde reactie» dwingt de presentator door alle vier de "
        "vormen. Dat is de didactische winst, niet het bellen.",
        "Bij «a mí tampoco» moet de beller iets negatiefs gezegd hebben — anders klopt de "
        "reactie niet en corrigeert de klas.",
        "Laat leerlingen presentator zijn: die rol oefent meer dan de belrol.",
    ],
    "nota": "Een echte jingle en een microfoon (of een pen als microfoon) tillen dit op. "
            "Zonder radio-inkleding wordt het een gewone beurtronde.",
}

U4_RETO_08 = {
    "id": "C5-U4-RETO-08", "num": 8, "curso": "C5", "unidad": U4,
    "seccion": "§2.3", "ancla": "reacciones", "soporte": "ppt",
    "nombre": "Cadena rota",
    "lente": "🔓 puzzel & escape", "forma": "🏫 Toda la clase", "skill": "🗣️ Hablar",
    "tiempo": "± 10 min", "dificultad": "★★★",
    "gancho_es": "La cadena da la vuelta a la clase. Si se rompe, vuelve a empezar.",
    "gancho_nl": "De ketting gaat de klas rond. Breekt hij, dan begin je opnieuw.",
    "consigna_es": "Reacciona a tu vecino/a y añade un gusto tuyo. Sin repetir reacciones.",
    "consigna_nl": "Reageer op je buur en voeg een eigen gusto toe. Zonder reacties te herhalen.",
    "regla": "Een reactie die al gebruikt is, breekt de ketting — ook als ze klopt. De klas "
             "moet dus bijhouden wat al voorbijkwam.",
    "pasos": [("El primero dice un gusto.", "De eerste zegt een gusto."),
              ("El siguiente reacciona y añade el suyo.", "De volgende reageert en voegt de zijne toe."),
              ("¿Reacción repetida? Se rompe: vuelta a empezar.", "Reactie herhaald? Gebroken: opnieuw."),
              ("Meta: dar la vuelta entera a la clase.", "Doel: één keer de hele klas rond.")],
    "datos": {
        "reacciones": ["A mí también.", "A mí tampoco.", "A mí sí.", "A mí no.",
                       "Yo igual.", "Pues yo no.", "A mí me encanta.", "A mí no me gusta nada."],
        "arranque": ["Me gusta la playa.", "No me gusta madrugar.",
                     "Me encantan los viajes.", "No me gustan los lunes."],
    },
    "clave": [
        "Acht reacties betekent dat de ketting minstens acht leerlingen ver kan komen. "
        "Daarna moet de klas ze hergebruiken — dan pas mag herhalen.",
        "De klassieke breuk: «a mí también» na een ontkenning. Dat moet «a mí tampoco» zijn.",
        "Noteer de gebruikte reacties zichtbaar; zonder dat spoor is de regel niet te "
        "handhaven.",
    ],
    "nota": "Speel maximaal drie rondes. Daarna wordt het onthouden belangrijker dan het "
            "spreken, en dat is niet het doel.",
}


# ===========================================================================
# C5 · U5 — ¡Ñam!  (parada: México · CDMX)
# ===========================================================================

U5 = 5

U5_RETO_02 = {
    "id": "C5-U5-RETO-02", "num": 2, "curso": "C5", "unidad": U5,
    "seccion": "§2.3", "ancla": "comida", "soporte": "print",
    "nombre": "El menú del país equivocado",
    "lente": "🕵️ forensisch", "forma": "👨‍👩‍👧 En grupos", "skill": "👁️ Leer",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Un restaurante «mexicano» con una carta que no cuadra.",
    "gancho_nl": "Een «Mexicaans» restaurant met een kaart die niet klopt.",
    "consigna_es": "Marca los platos que no son mexicanos y di de dónde son en realidad.",
    "consigna_nl": "Kruis de gerechten aan die niet Mexicaans zijn en zeg waar ze wél vandaan komen.",
    "regla": "Aanwijzen volstaat niet: bij elk fout gerecht zeg je het land. Wie een echt "
             "Mexicaans gerecht aankruist, verliest twee punten in plaats van er één te winnen.",
    "pasos": [("Leed la carta entera antes de marcar.", "Lees de hele kaart vóór je aankruist."),
              ("Marcad los intrusos y escribid su país.", "Kruis de indringers aan en schrijf hun land."),
              ("Cuidado: dos platos parecen extranjeros y son mexicanos.",
               "Let op: twee gerechten lijken buitenlands en zijn Mexicaans.")],
    "datos": {
        "carta": [("tacos al pastor", "México", True), ("paella valenciana", "España", False),
                  ("gazpacho andaluz", "España", False), ("mole poblano", "México", True),
                  ("ceviche", "Perú", False), ("chiles en nogada", "México", True),
                  ("tortilla de patatas", "España", False), ("pozole", "México", True),
                  ("empanadas argentinas", "Argentina", False), ("horchata de arroz", "México", True)],
    },
    "clave": [
        "Indringers (5): paella valenciana (Spanje) · gazpacho andaluz (Spanje) · ceviche "
        "(Peru) · tortilla de patatas (Spanje) · empanadas argentinas (Argentinië).",
        "Mexicaans, ook al klinkt het niet zo: chiles en nogada en horchata de arroz. "
        "Horchata bestaat óók in Spanje, maar dan van chufa — vandaar de verwarring.",
        "Mole poblano en pozole zijn de twee waar leerlingen het minst zeker over zijn; laat "
        "hen die opzoeken in plaats van te gokken.",
    ],
    "nota": "De strafpunten maken het spel. Zonder die regel kruist een groep gewoon alles "
            "aan wat ze niet kent.",
}

U5_RETO_03 = {
    "id": "C5-U5-RETO-03", "num": 3, "curso": "C5", "unidad": U5,
    "seccion": "§3.3", "ancla": "pedir", "soporte": "print",
    "nombre": "Reseña de una estrella",
    "lente": "✍️ creatieve beperking", "forma": "👤 Solo", "skill": "✍️ Escribir",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "La peor cena de tu vida. Y tienes que contarla con educación.",
    "gancho_nl": "Het slechtste avondmaal van je leven. En je moet het beleefd vertellen.",
    "consigna_es": "Escribe una reseña de una estrella sin una sola palabra fea.",
    "consigna_nl": "Schrijf een recensie van één ster zonder één lelijk woord.",
    "regla": "Geen scheldwoorden en geen «malo». Je beschikt alleen over «no me gusta», "
             "«un poco», «demasiado» en «no mucho». Beleefd vernietigend is de opdracht.",
    "pasos": [("Elige cinco cosas que salieron mal.", "Kies vijf dingen die misliepen."),
              ("Formula cada una en negativo suave.", "Formuleer elk in zacht negatief."),
              ("Cierra con una frase que suene amable y no lo sea.",
               "Sluit af met een zin die vriendelijk klinkt en het niet is.")],
    "datos": {
        "quejas": ["la sopa fría", "esperar cuarenta minutos", "el camarero no vuelve",
                   "demasiado picante", "la cuenta con un error", "música muy alta",
                   "no quedan tacos", "la mesa cerca de la puerta"],
        "marco": ["No me gusta mucho …", "… está un poco …", "… es demasiado … para mí",
                  "Todo bien, pero …", "Seguro que otro día …"],
    },
    "clave": [
        "Toets twee dingen: staat er geen enkel verboden woord, en is elke klacht toch "
        "herkenbaar als klacht?",
        "«Demasiado» is de sterkste: «demasiado picante para mí» klinkt beleefd en zegt alles.",
        "De slotzin is waar het vernuft zit — «seguro que otro día está mejor» is "
        "vriendelijk en vernietigend tegelijk.",
    ],
    "nota": "Deze reto oefent register, niet woordenschat. Wijs erop dat je in het Spaans "
            "zelden rechtstreeks klaagt in een recensie.",
}

U5_RETO_05 = {
    "id": "C5-U5-RETO-05", "num": 5, "curso": "C5", "unidad": U5,
    "seccion": "§1.3", "ancla": "cantidades", "soporte": "print",
    "nombre": "Precio justo",
    "lente": "🔬 onderzoek & data", "forma": "👥 En parejas", "skill": "✍️ Escribir",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "El mismo desayuno en CDMX y en Gante. ¿Cuánto cambia?",
    "gancho_nl": "Hetzelfde ontbijt in CDMX en in Gent. Hoeveel scheelt dat?",
    "consigna_es": "Convierte los precios, compara y escribe tres conclusiones con cantidades.",
    "consigna_nl": "Reken de prijzen om, vergelijk en schrijf drie conclusies met hoeveelheden.",
    "regla": "Elke conclusie bevat een hoeveelheid (un kilo de, una botella de, un paquete "
             "de) én een prijs. Alleen «es más barato» telt niet.",
    "pasos": [("Convertid los pesos a euros con el cambio de arriba.",
               "Reken de peso's om naar euro met de koers hierboven."),
              ("Comparad producto por producto.", "Vergelijk product per product."),
              ("Escribid tres conclusiones con cantidad y precio.",
               "Schrijf drie conclusies met hoeveelheid en prijs.")],
    "datos": {
        "cambio": "1 euro ≈ 20 pesos mexicanos (redondeamos para calcular)",
        "productos": [("un kilo de tomates", 30, 2.60), ("una botella de agua (1,5 l)", 18, 1.10),
                      ("un paquete de arroz (1 kg)", 26, 1.80), ("un kilo de aguacates", 60, 7.50),
                      ("una docena de tortillas", 20, 3.20), ("un café en el bar", 35, 2.40)],
        "marco": ["Un kilo de … cuesta … pesos, o sea … euros.",
                  "En Bélgica … cuesta … euros más.", "Lo más caro en México es …"],
    },
    "clave": [
        "Omgerekend: tomaten €1,50 tegen €2,60 · water €0,90 tegen €1,10 · rijst €1,30 "
        "tegen €1,80 · avocado's €3,00 tegen €7,50 · tortilla's €1,00 tegen €3,20 · "
        "koffie €1,75 tegen €2,40.",
        "Grootste verschil: avocado's en tortilla's — precies de twee producten die in "
        "Mexico lokaal zijn en bij ons ingevoerd.",
        "Wisselkoersen bewegen; deze is afgerond om te kunnen rekenen. Zeg dat erbij als een "
        "leerling het natrekt.",
    ],
    "nota": "Het rekenwerk is bewust deelbaar door twintig. De oefening gaat over de "
            "hoeveelheidsuitdrukking, niet over hoofdrekenen.",
}

U5_RETO_10 = {
    "id": "C5-U5-RETO-10", "num": 10, "curso": "C5", "unidad": U5,
    "seccion": "§4.3", "ancla": "pronombres_u5", "soporte": "print",
    "nombre": "¿Lo pido o no lo pido?",
    "lente": "🕵️ forensisch", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Doce platos, y en cada uno un ingrediente escondido.",
    "gancho_nl": "Twaalf gerechten, en in elk zit een verborgen ingrediënt.",
    "consigna_es": "Pregunta por el ingrediente con un pronombre, decide y justifica.",
    "consigna_nl": "Vraag naar het ingrediënt met een voornaamwoord, beslis en verantwoord.",
    "regla": "Je vraag moet het pronomen bevatten («¿lo lleva picante?»), en je beslissing "
             "ook («no lo pido»). Een vraag zonder pronomen wordt niet beantwoord.",
    "pasos": [("Elige un plato. No mires la columna del ingrediente.",
               "Kies een gerecht. Kijk niet in de ingrediëntkolom."),
              ("Pregunta a tu compañero/a con el pronombre.", "Vraag het je buur, met het voornaamwoord."),
              ("Decide: lo pido / no lo pido. Y di por qué.", "Beslis: ik bestel het of niet. En zeg waarom.")],
    "datos": {
        "platos": [("el mole poblano", "lleva chocolate"), ("los chiles en nogada", "llevan nuez"),
                   ("la sopa de tortilla", "lleva picante"), ("las quesadillas", "llevan queso"),
                   ("el pozole", "lleva carne de cerdo"), ("los tamales", "llevan manteca"),
                   ("la horchata", "lleva canela"), ("el guacamole", "lleva cebolla cruda"),
                   ("los tacos al pastor", "llevan piña"), ("las enchiladas", "llevan salsa verde"),
                   ("el flan", "lleva huevo"), ("el agua de jamaica", "lleva azúcar")],
        "marco": ["¿Lo/la/los/las lleva …?", "Sí, lo lleva. / No, no lo lleva.",
                  "Entonces lo pido. / Entonces no lo pido, porque …"],
    },
    "clave": [
        "De pronomina volgen het gerecht: el mole → lo · los chiles → los · la sopa → la · "
        "las quesadillas → las.",
        "Twee verrassingen die het gesprek dragen: chocolade in de mole en ananas op de tacos "
        "al pastor.",
        "Wie «¿lleva picante la sopa?» vraagt zonder pronomen, herformuleert. Dat is de regel "
        "en meteen de oefening.",
    ],
    "nota": "Laat de ingrediëntkolom afdekken met een blad. Zonder dat wordt het voorlezen.",
}

U5_RETO_01 = {
    "id": "C5-U5-RETO-01", "num": 1, "curso": "C5", "unidad": U5,
    "seccion": "§1.3", "ancla": "cantidades", "soporte": "hub",
    "nombre": "La cocina a ciegas",
    "lente": "🎭 simulatie met beperking", "forma": "👥 En parejas", "skill": "👂 Escuchar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Tú tienes los ingredientes. La receta la oyes, no la ves.",
    "gancho_nl": "Jij hebt de ingrediënten. Het recept hoor je, je ziet het niet.",
    "consigna_es": "Escucha cada paso y elige la cantidad correcta. Una mal y el plato se estropea.",
    "consigna_nl": "Luister naar elke stap en kies de juiste hoeveelheid. Eén fout en het "
                   "gerecht mislukt.",
    "regla": "Je kiest op wat je hóórt, niet op wat logisch lijkt. Twee stappen gebruiken "
             "hetzelfde product met een ándere hoeveelheid — daar gaat het mis.",
    "pasos": [("Escucha el paso entero antes de elegir.", "Luister de hele stap af vóór je kiest."),
              ("Elige la cantidad. Fíjate en la palabra, no en el producto.",
               "Kies de hoeveelheid. Let op het woord, niet op het product."),
              ("¿Fallas? Vuelve a escuchar.", "Fout? Luister opnieuw.")],
    "datos": {
        "pasos_receta": [
            ("Primero pon un kilo de tomates en la olla.", "un kilo de",
             ["un kilo de", "un poco de", "una botella de"]),
            ("Añade un poco de sal, no mucha.", "un poco de",
             ["un poco de", "un kilo de", "un paquete de"]),
            ("Ahora echa media cebolla, solo media.", "media",
             ["media", "una", "dos"]),
            ("Pon un paquete de arroz entero.", "un paquete de",
             ["un paquete de", "un poco de", "medio paquete de"]),
            ("Añade dos vasos de agua.", "dos vasos de",
             ["dos vasos de", "una botella de", "un vaso de"]),
            ("Y al final, muy poco picante.", "muy poco",
             ["muy poco", "mucho", "bastante"]),
        ],
    },
    "clave": [
        "un kilo de · un poco de · media · un paquete de · dos vasos de · muy poco",
        "Stap 1 en 2 gaan allebei over «poner» maar met tegengestelde hoeveelheden — daar "
        "vallen de snelle luisteraars.",
        "«Media cebolla» zonder «de» is de vormvalstrik: hoeveelheden met een breuk laten "
        "het voorzetsel vallen.",
    ],
    "nota": "Werkt ook klassikaal: laat de leerkracht voorlezen terwijl de klas op de hub kiest.",
}

U5_RETO_06 = {
    "id": "C5-U5-RETO-06", "num": 6, "curso": "C5", "unidad": U5,
    "seccion": "Cultura", "ancla": "cultura_u5", "soporte": "hub",
    "nombre": "La receta de la abuela, sin medidas",
    "lente": "🤝 bemiddelen", "forma": "👤 Solo", "skill": "🔀 Mediar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "«Un poquito», «al gusto», «un chorrito». ¿Y eso cuánto es?",
    "gancho_nl": "«Een beetje», «naar smaak», «een scheutje». En hoeveel is dat?",
    "consigna_es": "Convierte la receta de la abuela en medidas exactas para alguien que "
                   "nunca ha cocinado.",
    "consigna_nl": "Zet het recept van de oma om in exacte maten voor iemand die nooit "
                   "gekookt heeft.",
    "regla": "Elke vage maat wordt een getal met eenheid. Je mag niet «een beetje» laten "
             "staan, en je mag ook niets weglaten.",
    "pasos": [("Lee la receta. Marca lo que no es exacto.", "Lees het recept. Markeer wat niet exact is."),
              ("Elige la medida que mejor lo traduce.", "Kies de maat die het best vertaalt."),
              ("Comprueba: ¿puede cocinarlo alguien sin experiencia?",
               "Controleer: zou iemand zonder ervaring dit kunnen koken?")],
    "datos": {
        "items": [
            ("un poquito de sal", "una cucharadita",
             ["una cucharadita", "cien gramos", "medio kilo"],
             "«un poquito» bij zout is ongeveer een theelepel, geen honderd gram"),
            ("un chorrito de aceite", "dos cucharadas",
             ["dos cucharadas", "medio litro", "una gota"],
             "een scheutje olie is twee eetlepels — een halve liter is frituren"),
            ("harina, la que pida", "doscientos cincuenta gramos",
             ["doscientos cincuenta gramos", "un kilo", "una cucharadita"],
             "«la que pida» betekent tot het deeg samenhangt: voor dit recept 250 g"),
            ("azúcar al gusto", "cuatro cucharadas",
             ["cuatro cucharadas", "un kilo", "una pizca"],
             "«al gusto» is geen snufje: bij een dessert is het enkele eetlepels"),
            ("se hace hasta que esté", "veinte minutos",
             ["veinte minutos", "cinco horas", "dos minutos"],
             "«hasta que esté» is bij dit gerecht ongeveer twintig minuten"),
        ],
    },
    "clave": [
        "una cucharadita · dos cucharadas · doscientos cincuenta gramos · cuatro cucharadas · "
        "veinte minutos",
        "De kern van bemiddelen zit hier: je zet niet om van taal naar taal, maar van "
        "ervaringskennis naar instructie. Er gaat iets verloren, en dat mag.",
        "«Una pizca» bestaat wel degelijk, maar niet voor suiker in een dessert — dat is de "
        "valstrik in item 4.",
    ],
    "nota": "Sluit aan bij de eindtaak «La carta»: wie hier exacte maten leert, schrijft "
            "daarna een bruikbaar recept.",
}

U5_RETO_09 = {
    "id": "C5-U5-RETO-09", "num": 9, "curso": "C5", "unidad": U5,
    "seccion": "§2.3", "ancla": "comida", "soporte": "hub",
    "nombre": "Cocina en directo",
    "lente": "📻 mediaformat", "forma": "👤 Solo", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Treinta segundos en directo. La clase hace exactamente lo que dices.",
    "gancho_nl": "Dertig seconden live. De klas doet exact wat jij zegt.",
    "consigna_es": "Graba una instrucción de cocina de treinta segundos. Sin usar «poner».",
    "consigna_nl": "Neem een kookinstructie van dertig seconden op. Zonder «poner» te gebruiken.",
    "regla": "Het werkwoord «poner» is verboden — en dat is precies het werkwoord dat je "
             "wilt gebruiken. Je moet naar añadir, echar, cortar, mezclar, calentar grijpen.",
    "pasos": [("Elige un plato muy simple.", "Kies een heel eenvoudig gerecht."),
              ("Escribe los pasos sin «poner».", "Schrijf de stappen zonder «poner»."),
              ("Graba. Treinta segundos, ni uno más.", "Neem op. Dertig seconden, geen seconde meer."),
              ("La clase escucha y ejecuta. ¿Sale?", "De klas luistert en voert uit. Lukt het?")],
    "datos": {
        "verbos": ["añadir", "echar", "cortar", "mezclar", "calentar", "cocer", "servir"],
        "marco": ["Primero corta … en trozos.", "Después añade …", "Mezcla todo durante …",
                  "Calienta … minutos.", "Y ya está: sirve con …"],
    },
    "clave": [
        "Toets twee dingen: nul keer «poner», en kan iemand het uitvoeren zonder vragen te "
        "stellen?",
        "De meest gebruikte vervangers zijn añadir en echar. Wie ze alle twee gebruikt, "
        "heeft de opdracht begrepen.",
        "Dertig seconden is ongeveer vijf stappen. Wie er tien wil, moet schrappen.",
    ],
    "nota": "Het verbod op «poner» is niet willekeurig: het is het werkwoord dat alles "
            "afdekt, en dus het werkwoord dat de woordenschat tegenhoudt.",
}

U5_RETO_04 = {
    "id": "C5-U5-RETO-04", "num": 4, "curso": "C5", "unidad": U5,
    "seccion": "§3.3", "ancla": "pedir", "soporte": "ppt",
    "nombre": "El pedido imposible",
    "lente": "🎭 simulatie met beperking", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "El camarero dice que no a casi todo. Tú tienes que cenar igual.",
    "gancho_nl": "De ober zegt op bijna alles nee. Jij moet tóch eten.",
    "consigna_es": "Consigue un menú completo: primero, segundo, bebida y postre.",
    "consigna_nl": "Krijg een volledig menu binnen: voorgerecht, hoofdgerecht, drank en dessert.",
    "regla": "Elke «lo siento» dwingt je tot een nieuw voorstel — en je mag nooit twee keer "
             "dezelfde beleefdheidsformule gebruiken.",
    "pasos": [("El camarero coge su lista de «no hay».", "De ober neemt zijn lijst met «niet meer»."),
              ("Pides. Te dicen que no. Propón otra cosa.", "Je bestelt. Ze zeggen nee. Stel iets anders voor."),
              ("Sigue hasta tener los cuatro platos.", "Ga door tot je de vier gangen hebt."),
              ("Cambiad de papel.", "Wissel van rol.")],
    "datos": {
        "no_hay": ["No hay tacos de pollo.", "Se acabó el pozole.", "El flan está terminado.",
                   "No queda agua de jamaica.", "Hoy no hacemos mole.", "La sopa está fría."],
        "formulas": ["Para mí, …", "¿Me pone …?", "¿Me trae …?", "¿Y tienen …?",
                     "Entonces …, por favor.", "¿Qué me recomienda?"],
        "carta": ["sopa de tortilla", "quesadillas", "tacos al pastor", "enchiladas",
                  "pozole", "horchata", "agua de jamaica", "flan", "arroz con leche"],
    },
    "clave": [
        "Zes formules voor vier gangen: er is speling, maar niet veel. Wie herhaalt, "
        "begint opnieuw.",
        "«¿Qué me recomienda?» is de ontsnappingsroute — laat leerlingen die zelf ontdekken "
        "in plaats van hem aan te reiken.",
        "De ober mag niet op alles nee zeggen: minstens vier gerechten blijven beschikbaar, "
        "anders loopt het spel vast.",
    ],
    "nota": "Geef de «no hay»-lijst alleen aan de ober. Ziet de klant hem, dan verdwijnt het "
            "improviseren.",
}

U5_RETO_07 = {
    "id": "C5-U5-RETO-07", "num": 7, "curso": "C5", "unidad": U5,
    "seccion": "§1.3", "ancla": "cantidades", "soporte": "ppt",
    "nombre": "Cinco palabras para el mercado",
    "lente": "🔓 puzzel & escape", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Quieres comprar algo cuyo nombre no sabes. Tienes cinco palabras.",
    "gancho_nl": "Je wil iets kopen waarvan je de naam niet kent. Je hebt vijf woorden.",
    "consigna_es": "Consigue el producto usando como máximo cinco palabras por intento.",
    "consigna_nl": "Krijg het product te pakken met maximaal vijf woorden per poging.",
    "regla": "Vijf woorden per poging, gebaren mogen niet, en de naam van het product mag "
             "niet vallen — ook niet in het Nederlands of het Engels.",
    "pasos": [("Coge una tarjeta de producto. No la enseñes.", "Neem een productkaart. Laat ze niet zien."),
              ("Describe en cinco palabras. Cuenta en voz alta.", "Beschrijf in vijf woorden. Tel hardop mee."),
              ("¿No lo adivina? Otro intento, otras cinco.", "Raadt hij het niet? Nieuwe poging, vijf nieuwe woorden."),
              ("Máximo tres intentos por producto.", "Maximaal drie pogingen per product.")],
    "datos": {
        "productos": ["el aguacate", "la sandía", "el cilantro", "la calabaza", "el chile",
                      "la piña", "el maíz", "la cebolla", "el limón", "la tortilla"],
        "marco": ["Es verde y grande.", "Se come con sal.", "Es de color …",
                  "Está en la sopa.", "Cuesta poco.", "Es dulce, no salado."],
    },
    "clave": [
        "Sterke omschrijvingen gebruiken kleur, smaak en gebruik — precies de woordenschat "
        "van §1 en §2.",
        "«El chile» en «el cilantro» zijn de moeilijkste: beide vragen om smaak in plaats "
        "van vorm.",
        "Vijf woorden dwingt tot ser en estar zonder franje: «es verde», «está en la sopa».",
    ],
    "nota": "Tel de woorden echt. Zonder tellen wordt het een gewone omschrijfoefening en "
            "verdwijnt de druk die de zinnen kort houdt.",
}

U5_RETO_08 = {
    "id": "C5-U5-RETO-08", "num": 8, "curso": "C5", "unidad": U5,
    "seccion": "§3.3", "ancla": "pedir", "soporte": "ppt",
    "nombre": "La sobremesa",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Habéis cenado bien. Ahora llega la cuenta.",
    "gancho_nl": "Jullie hebben goed gegeten. Nu komt de rekening.",
    "consigna_es": "Repartid la cuenta. Cada uno tiene una instrucción secreta.",
    "consigna_nl": "Verdeel de rekening. Ieder heeft een geheime instructie.",
    "regla": "Je geheime instructie moet je volgen, maar je mag ze niet uitspreken. Wie zegt "
             "«ik heb weinig geld», heeft verloren — je moet het láten merken.",
    "pasos": [("Coge tu instrucción secreta. No la enseñes.", "Neem je geheime instructie. Laat ze niet zien."),
              ("Mirad la cuenta juntos.", "Bekijk de rekening samen."),
              ("Negociad hasta que todos paguen algo.", "Onderhandel tot iedereen iets betaalt."),
              ("Al final: ¿quién tenía qué instrucción?", "Op het einde: wie had welke instructie?")],
    "datos": {
        "cuenta": [("sopa de tortilla", 45), ("dos quesadillas", 120), ("tacos al pastor", 95),
                   ("tres horchatas", 75), ("flan", 40), ("propina", 40)],
        "roles": [("Diego", "Estás sin dinero, pero te da vergüenza decirlo."),
                  ("Valen", "Quieres invitar a todos, pero sin ofender a nadie."),
                  ("Nina", "Solo has comido el flan. No quieres pagar lo demás."),
                  ("Tú", "Has olvidado la cartera en casa. De verdad.")],
        "marco": ["Yo pago …", "Yo solo he tomado …", "¿Y si …?",
                  "No hace falta, de verdad.", "Entonces la próxima vez invito yo."],
    },
    "clave": [
        "Totaal: 415 pesos, ongeveer 21 euro. Eerlijk delen door vier is ruim 100 elk — "
        "precies wat de vier instructies onmogelijk maken.",
        "De spanning zit bij Nina en Diego: allebei willen minder betalen, maar om "
        "tegengestelde redenen.",
        "Toets of niemand zijn instructie heeft uitgesproken. Dat is de regel én de reden "
        "dat er echt onderhandeld wordt.",
    ],
    "nota": "«La sobremesa» is cultureel echt: in Mexico en Spanje blijft men na het eten "
            "aan tafel. Zeg dat erbij, dan is de scène niet alleen een rekensom.",
}


# ===========================================================================
# C5 · U6 — De tiendas  (parada: México · mercados)
# ===========================================================================

U6 = 6

U6_RETO_03 = {
    "id": "C5-U6-RETO-03", "num": 3, "curso": "C5", "unidad": U6,
    "seccion": "§4.3", "ancla": "concordancia_u6", "soporte": "print",
    "nombre": "La equipación",
    "lente": "🔓 puzzel & escape", "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Ocho camisetas, ocho clubes. Descríbelas sin decir el nombre.",
    "gancho_nl": "Acht truitjes, acht clubs. Beschrijf ze zonder de naam te noemen.",
    "consigna_es": "Describe la equipación por colores y detalles. Tu grupo adivina el club "
                   "y el país.",
    "consigna_nl": "Beschrijf het truitje op kleur en details. Je groep raadt de club en het land.",
    "regla": "De clubnaam en de stad zijn verboden. Alleen kleuren, strepen en kledingstukken. "
             "En elke beschrijving bevat minstens twee kledingwoorden.",
    "pasos": [("Coge una tarjeta de equipación.", "Neem een truitjeskaart."),
              ("Describe: colores, rayas, pantalón, medias.", "Beschrijf: kleuren, strepen, broek, kousen."),
              ("El grupo adivina club y país.", "De groep raadt club en land."),
              ("¿Acertáis los ocho? Sois de la casa.", "Alle acht juist? Dan horen jullie erbij.")],
    "datos": {
        "equipos": [("el Barça", "España", "camiseta azul y roja a rayas, pantalón azul"),
                    ("el Real Madrid", "España", "camiseta blanca, pantalón blanco, todo blanco"),
                    ("Boca Juniors", "Argentina", "camiseta azul con una raya amarilla ancha"),
                    ("el América", "México", "camiseta amarilla con azul, muy llamativa"),
                    ("el Nacional", "Uruguay", "camiseta blanca con una banda azul"),
                    ("Colo-Colo", "Chile", "camiseta blanca con una raya negra y un jefe indígena"),
                    ("el Cruz Azul", "México", "camiseta azul oscura con una cruz"),
                    ("Millonarios", "Colombia", "camiseta azul clara, pantalón azul")],
        "marco": ["La camiseta es … y …", "Lleva una raya …", "El pantalón es …",
                  "Las medias son …"],
    },
    "clave": [
        "Kleuren dragen de oefening: rayas azules y rojas (Barça) tegenover azul con raya "
        "amarilla (Boca).",
        "Colo-Colo is de moeilijkste en de mooiste: het embleem verwijst naar een Mapuche-"
        "leider, wat meteen een cultureel gesprek opent.",
        "Toets op twee kledingwoorden per beschrijving — anders blijft het bij kleuren.",
    ],
    "nota": "Deze reto komt uit de parels van het vorige project. Wie de clubs niet kent, "
            "kan nog steeds beschrijven — het raden mag met de kaart erbij.",
}

U6_RETO_04 = {
    "id": "C5-U6-RETO-04", "num": 4, "curso": "C5", "unidad": U6,
    "seccion": "§4.3", "ancla": "concordancia_u6", "soporte": "print",
    "nombre": "El armario del personaje",
    "lente": "🕵️ forensisch", "forma": "👤 Solo", "skill": "👁️ Leer",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Solo ves su armario. ¿Quién vive aquí?",
    "gancho_nl": "Je ziet alleen zijn kleerkast. Wie woont hier?",
    "consigna_es": "Deduce oficio, edad y país. Cada conclusión con la prenda que la prueba.",
    "consigna_nl": "Leid beroep, leeftijd en land af. Elke conclusie mét het kledingstuk dat "
                   "het bewijst.",
    "regla": "Elke conclusie heeft een bewijsstuk. «Ik denk dat hij jong is» telt niet; "
             "«es joven porque tiene cinco camisetas de grupos de música» wel.",
    "pasos": [("Lee el inventario entero.", "Lees de hele inventaris."),
              ("Busca lo que se repite y lo que falta.", "Zoek wat terugkeert en wat ontbreekt."),
              ("Escribe tres conclusiones con su prueba.", "Schrijf drie conclusies met hun bewijs.")],
    "datos": {
        "armario": ["tres delantales blancos, muy usados", "dos pantalones de cuadros",
                    "unos zapatos negros cómodos, sin tacón", "una chaqueta gruesa",
                    "cero corbatas", "un gorro blanco alto", "seis camisetas de conciertos",
                    "unas botas de montaña con barro", "un abrigo largo para el frío",
                    "ninguna ropa de playa"],
        "marco": ["Creo que es … porque tiene …", "No es … porque no hay …",
                  "Vive en un sitio … porque …"],
    },
    "clave": [
        "Beroep: kok — de schorten, de geblokte broek en vooral de hoge witte muts.",
        "Leeftijd: jong — zes concert-T-shirts en geen enkele das.",
        "Land: ergens koud en bergachtig — dikke jas, lange mantel, bergschoenen met modder, "
        "en géén strandkleding.",
        "Het sterkste bewijs is wat er níét is: zonder dassen en zonder strandkleding valt "
        "de helft van de mogelijkheden weg.",
    ],
    "nota": "Wijs op de negatieve bewijzen. Leerlingen kijken vanzelf naar wat er staat; "
            "de afwezigheid zien is de eigenlijke vaardigheid.",
}

U6_RETO_05 = {
    "id": "C5-U6-RETO-05", "num": 5, "curso": "C5", "unidad": U6,
    "seccion": "§2.3", "ancla": "acabar", "soporte": "print",
    "nombre": "Moda circular",
    "lente": "🔬 onderzoek & data", "forma": "👥 En parejas", "skill": "👁️ Leer",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Un vaquero necesita más agua de la que bebes en años.",
    "gancho_nl": "Eén jeans kost meer water dan jij in jaren drinkt.",
    "consigna_es": "Lee los datos y escribe tres frases con «acabar de» sobre tus últimas compras.",
    "consigna_nl": "Lees de gegevens en schrijf drie zinnen met «acabar de» over je laatste aankopen.",
    "regla": "Elke zin bevat «acabo de» plus een getal uit de tabel. Zonder cijfer is het "
             "een mening, geen conclusie.",
    "pasos": [("Leed la tabla. ¿Qué dato os sorprende?", "Lees de tabel. Welk cijfer verrast jullie?"),
              ("Pensad en vuestras tres últimas compras.", "Denk aan jullie drie laatste aankopen."),
              ("Escribid las frases con «acabar de» y el dato.", "Schrijf de zinnen met «acabar de» en het cijfer.")],
    "datos": {
        "tabla": [("un vaquero", "7 500 litros de agua"), ("una camiseta de algodón", "2 700 litros"),
                  ("ropa comprada al año, por persona en Europa", "unos 26 kilos"),
                  ("ropa tirada al año, por persona", "unos 11 kilos"),
                  ("veces que se lleva una prenda antes de tirarla", "unas 7"),
                  ("ropa que se recicla de verdad", "menos del 1 %")],
        "marco": ["Acabo de comprar … y ahora sé que …",
                  "Acabamos de leer que … litros …", "No acabo de entender por qué …"],
    },
    "clave": [
        "Het cijfer dat altijd blijft hangen: minder dan één procent wordt echt gerecycleerd.",
        "«Acabar de» is hier geen trucje: het zet de aankoop van net tegenover een cijfer, "
        "en dat contrast is de opdracht.",
        "Cijfers zijn orders of magnitude uit gangbare rapporten; ze dienen om te vergelijken. "
        "Wie ze als feit publiceert, controleert ze eerst.",
    ],
    "nota": "Deze reto raakt aan het thema van C6+ U7 (medio ambiente). Een vroege draad die "
            "je daar kunt oppakken.",
}

U6_RETO_07 = {
    "id": "C5-U6-RETO-07", "num": 7, "curso": "C5", "unidad": U6,
    "seccion": "§1.3", "ancla": "pronombres_u6", "soporte": "print",
    "nombre": "Escaparate en 30 palabras",
    "lente": "✍️ creatieve beperking", "forma": "👥 En parejas", "skill": "✍️ Escribir",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Un cartel de escaparate. Exactamente treinta palabras.",
    "gancho_nl": "Een etalageaffiche. Precies dertig woorden.",
    "consigna_es": "Escribe el cartel con treinta palabras exactas y al menos cuatro pronombres.",
    "consigna_nl": "Schrijf het affiche met exact dertig woorden en minstens vier voornaamwoorden.",
    "regla": "Precies dertig — niet negenentwintig, niet eenendertig — en minstens vier keer "
             "lo, la, los of las. Tel na afloop hardop.",
    "pasos": [("Elegid una prenda y su precio.", "Kies een kledingstuk en zijn prijs."),
              ("Escribid el cartel sin contar.", "Schrijf het affiche zonder te tellen."),
              ("Ahora contad. ¿Sobran o faltan?", "Tel nu. Te veel of te weinig?"),
              ("Ajustad hasta llegar a treinta exactas.", "Pas aan tot je precies op dertig zit.")],
    "datos": {
        "prendas": [("la camisa de flores", "25 €"), ("los vaqueros clásicos", "40 €"),
                    ("las botas de piel", "60 €"), ("el jersey de lana", "35 €")],
        "marco": ["¿Te gusta? Llévatela.", "La tienes en tres colores.",
                  "Los tenemos en todas las tallas.", "No lo pienses más."],
    },
    "clave": [
        "Toets exact dertig woorden en minstens vier pronomina. Beide zijn objectief te tellen.",
        "De vier voorbeeldzinnen in het marco bevatten samen precies vier pronomina — "
        "bruikbaar als model, niet als oplossing.",
        "Wie te veel woorden heeft, schrapt bijna altijd een pronomen. Wijs erop dat die "
        "juist moeten blijven.",
    ],
    "nota": "De harde telling is het hele punt: schrijven met een limiet dwingt tot kiezen, "
            "en kiezen is waar de taal zit.",
}

U6_RETO_06 = {
    "id": "C5-U6-RETO-06", "num": 6, "curso": "C5", "unidad": U6,
    "seccion": "§3.3", "ancla": "demostrativos", "soporte": "hub",
    "nombre": "La talla que no existe",
    "lente": "🤝 bemiddelen", "forma": "👤 Solo", "skill": "🔀 Mediar",
    "tiempo": "± 10 min", "dificultad": "★★☆",
    "gancho_es": "Tu talla en Bélgica no es tu talla en México. ¿Cuál pides?",
    "gancho_nl": "Jouw maat in België is niet jouw maat in Mexico. Welke vraag je?",
    "consigna_es": "Convierte la talla y elige lo que dices por teléfono.",
    "consigna_nl": "Reken de maat om en kies wat je door de telefoon zou zeggen.",
    "regla": "Je zegt niet het getal van je eigen systeem. Je moet omrekenen én de zin "
             "kiezen die in de winkel werkt.",
    "pasos": [("Mira las tres tablas.", "Bekijk de drie tabellen."),
              ("Convierte y elige la frase correcta.", "Reken om en kies de juiste zin."),
              ("¿Fallas? Mira qué sistema has usado.", "Fout? Kijk welk systeem je gebruikte.")],
    "datos": {
        "items": [
            ("Tu talla europea de camiseta es la 38. En México te dicen S, M o L. ¿Qué pides?",
             "Una mediana, por favor.",
             ["Una mediana, por favor.", "Una treinta y ocho, por favor.", "Una pequeña, por favor."],
             "EU 38 ≈ M (mediana); het Europese getal zegt daar niets"),
            ("Calzas un 40 europeo. En México usan el sistema mexicano. ¿Qué número pides?",
             "El siete, más o menos.",
             ["El siete, más o menos.", "El cuarenta.", "El once."],
             "EU 40 ≈ MX 7 voor dames; het Europese getal bestaat er niet"),
            ("Quieres unos vaqueros. En México las tallas van por pulgadas. ¿Qué preguntas?",
             "¿Qué talla es la treinta en centímetros?",
             ["¿Qué talla es la treinta en centímetros?", "¿Tienen la cuarenta?",
              "¿Es grande o pequeña?"],
             "bij inches vraag je om te vertalen, niet om een getal dat er niet is"),
            ("No estás seguro/-a de la talla. ¿Qué dices?",
             "¿Me la puedo probar?",
             ["¿Me la puedo probar?", "¿Cuánto cuesta?", "¿La tienen en azul?"],
             "passen lost het op als de tabellen niet helpen — met pronomen"),
        ],
    },
    "clave": [
        "Una mediana · el siete · ¿qué talla es la treinta en centímetros? · ¿me la puedo probar?",
        "De rode draad: bij een ander systeem vraag je om vertaling of om passen, je noemt "
        "niet je eigen getal.",
        "Item 4 brengt het pronomen terug: «me la puedo probar» — la verwijst naar de prenda.",
    ],
    "nota": "Maattabellen verschillen per merk. De omrekeningen hier zijn benaderingen, en "
            "juist dat maakt «¿me la puedo probar?» het beste antwoord.",
}

U6_RETO_09 = {
    "id": "C5-U6-RETO-09", "num": 9, "curso": "C5", "unidad": U6,
    "seccion": "§1.3", "ancla": "pronombres_u6", "soporte": "hub",
    "nombre": "Anuncio de radio de 20 segundos",
    "lente": "📻 mediaformat", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Veinte segundos de radio para vender una sola prenda.",
    "gancho_nl": "Twintig seconden radio om één kledingstuk te verkopen.",
    "consigna_es": "Graba un anuncio de veinte segundos con el pronombre repetido tres veces.",
    "consigna_nl": "Neem een spot van twintig seconden op waarin het voornaamwoord drie keer "
                   "terugkeert.",
    "regla": "Hetzelfde pronomen moet er drie keer in — en de naam van het kledingstuk mag "
             "maar één keer vallen. Daarna verwijs je er alleen nog naar.",
    "pasos": [("Elegid la prenda. Decid su nombre una sola vez.", "Kies het kledingstuk. Noem het één keer."),
              ("Escribid el texto con tres pronombres.", "Schrijf de tekst met drie voornaamwoorden."),
              ("Grabad. Veinte segundos.", "Neem op. Twintig seconden."),
              ("Escuchad: ¿se entiende de qué habláis?", "Luister: begrijp je waarover het gaat?")],
    "datos": {
        "marco": ["¿Buscas … ? La tenemos.", "La llevas en verano y en invierno.",
                  "Y la puedes lavar en casa.", "Los tenemos en tres colores.",
                  "No lo pienses más: es tuyo."],
        "prendas": ["la camisa de flores", "los vaqueros", "las botas", "el jersey"],
    },
    "clave": [
        "Toets drie dingen: één keer de naam, drie keer het pronomen, twintig seconden.",
        "Wie het kledingstuk blijft herhalen, hoort meteen waarom pronomina bestaan — dat is "
        "de didactische winst.",
        "Meervoud (los vaqueros, las botas) is moeilijker en dus interessanter: los/las moet "
        "meebewegen.",
    ],
    "nota": "Laat de spots klassikaal beluisteren. Het contrast tussen een spot mét en zonder "
            "pronomina hoor je onmiddellijk.",
}

U6_RETO_10 = {
    "id": "C5-U6-RETO-10", "num": 10, "curso": "C5", "unidad": U6,
    "seccion": "§1.3", "ancla": "pronombres_u6", "soporte": "hub",
    "nombre": "Lo compro / no lo compro",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Cuatro compras, cuatro dudas. Ninguna respuesta es fácil.",
    "gancho_nl": "Vier aankopen, vier twijfels. Geen enkel antwoord is makkelijk.",
    "consigna_es": "Decide en cada caso y justifica con un pronombre en la frase.",
    "consigna_nl": "Beslis per geval en verantwoord met een voornaamwoord in de zin.",
    "regla": "Je antwoord bevat altijd het pronomen: «lo compro porque…» of «no la compro "
             "porque…». Een antwoord zonder pronomen telt niet.",
    "pasos": [("Lee el caso. No decidas todavía.", "Lees de casus. Beslis nog niet."),
              ("Elige y di por qué, con el pronombre.", "Kies en zeg waarom, met het voornaamwoord."),
              ("Comparad en grupo: ¿todos igual?", "Vergelijk in groep: iedereen hetzelfde?")],
    "datos": {
        "items": [
            ("Una camiseta preciosa, pero cuesta 5 € y sabes cómo se fabrica.",
             "No la compro.", ["No la compro.", "La compro.", "Lo compro."],
             "camiseta is vrouwelijk: la, niet lo — en het dilemma is de prijs tegenover de herkomst"),
            ("Unos vaqueros de segunda mano, casi nuevos, a mitad de precio.",
             "Los compro.", ["Los compro.", "Lo compro.", "Las compro."],
             "vaqueros is mannelijk meervoud: los"),
            ("Un jersey de lana local, muy caro, que dura diez años.",
             "Lo compro.", ["Lo compro.", "La compro.", "Los compro."],
             "jersey is mannelijk enkelvoud: lo"),
            ("Unas botas que te encantan pero te quedan un poco pequeñas.",
             "No las compro.", ["No las compro.", "No los compro.", "No la compro."],
             "botas is vrouwelijk meervoud: las"),
        ],
    },
    "clave": [
        "no la compro · los compro · lo compro · no las compro",
        "De beslissing is vrij; de vórm niet. Daarom staat er telkens maar één antwoord met "
        "het juiste pronomen tussen de opties.",
        "Casus 1 en 3 zetten prijs tegenover duurzaamheid — laat het gesprek daar even lopen "
        "vóór je naar de vorm kijkt.",
    ],
    "nota": "De vier casussen sluiten aan bij Moda circular. Wie beide doet, heeft de cijfers "
            "én het dilemma.",
}

U6_RETO_01 = {
    "id": "C5-U6-RETO-01", "num": 1, "curso": "C5", "unidad": U6,
    "seccion": "§3.3", "ancla": "demostrativos", "soporte": "ppt",
    "nombre": "El regateo",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "En el mercado el primer precio nunca es el precio.",
    "gancho_nl": "Op de markt is de eerste prijs nooit de prijs.",
    "consigna_es": "Regatead hasta cerrar un trato. Cada uno tiene un límite secreto.",
    "consigna_nl": "Onderhandel tot jullie een deal hebben. Ieder heeft een geheime grens.",
    "regla": "De verkoper mag niet onder zijn bodemprijs, de koper niet boven zijn budget. "
             "En elk nieuw bod moet met een reden komen — een getal alleen telt niet.",
    "pasos": [("Coge tu tarjeta: precio mínimo o presupuesto.", "Neem je kaart: bodemprijs of budget."),
              ("El vendedor empieza. Siempre alto.", "De verkoper begint. Altijd hoog."),
              ("Regatead con razones, no solo con números.", "Onderhandel met redenen, niet alleen met getallen."),
              ("¿No hay trato? También es un resultado.", "Geen deal? Dat is ook een uitkomst.")],
    "datos": {
        "productos": [("un sombrero", 250, 120), ("una manta de lana", 600, 350),
                      ("unos aretes de plata", 400, 200), ("una bolsa bordada", 500, 260)],
        "marco_vendedor": ["Le hago un buen precio.", "Es hecho a mano, mire.",
                           "Se lo dejo en …", "No puedo bajar más."],
        "marco_cliente": ["¿Cuánto cuesta?", "Es un poco caro para mí.",
                          "¿Me lo deja en …?", "Entonces me lo llevo."],
    },
    "clave": [
        "Getallen zijn (vraagprijs, bodemprijs) in peso's. Een deal ligt altijd tussen de "
        "bodemprijs en het budget van de koper.",
        "De pronomina zitten in de formules: «se lo dejo en…», «me lo llevo». Wijs erop dat "
        "onderhandelen in het Spaans bijna niet kan zonder.",
        "«No puedo bajar más» is het sluitstuk: wie het te vroeg zegt, verliest zijn ruimte.",
    ],
    "nota": "Afdingen is op Mexicaanse markten gebruikelijk in ambachtelijke kramen, niet in "
            "winkels met vaste prijzen. Zeg dat erbij, anders leren leerlingen het verkeerd.",
}

U6_RETO_02 = {
    "id": "C5-U6-RETO-02", "num": 2, "curso": "C5", "unidad": U6,
    "seccion": "§2.3", "ancla": "acabar", "soporte": "ppt",
    "nombre": "Devolución imposible",
    "lente": "🎭 simulatie met beperking", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Quieres devolver algo. No tienes el ticket.",
    "gancho_nl": "Je wil iets terugbrengen. Je hebt geen kassabon.",
    "consigna_es": "Consigue el cambio. El vendedor tiene tres negativas y tú tres argumentos.",
    "consigna_nl": "Krijg de ruil rond. De verkoper heeft drie weigeringen en jij drie argumenten.",
    "regla": "Je mag elk argument maar één keer gebruiken. Op wie in herhaling valt, hoeft "
             "de verkoper niet meer te antwoorden.",
    "pasos": [("El cliente explica el problema.", "De klant legt het probleem uit."),
              ("El vendedor dice que no. Primera negativa.", "De verkoper zegt nee. Eerste weigering."),
              ("El cliente usa su siguiente argumento.", "De klant gebruikt zijn volgende argument."),
              ("¿Cambio, vale de tienda o nada?", "Ruil, tegoedbon of niets?")],
    "datos": {
        "negativas": ["Sin ticket no puedo hacer nada.",
                      "Ya la ha llevado, mire la etiqueta.",
                      "La política de la tienda es de quince días."],
        "argumentos": ["La he comprado aquí esta semana, me acuerdo del vendedor.",
                       "No la he llevado, solo me la he probado en casa.",
                       "Solo quiero cambiarla por otra talla, no el dinero."],
        "salidas": ["cambio por otra talla", "vale para la tienda", "nada de nada"],
    },
    "clave": [
        "Het sterkste argument is het derde: wie alleen een andere maat vraagt, ontwijkt het "
        "hele bonverhaal. Laat leerlingen dat zelf ontdekken.",
        "Alle drie de weigeringen en alle drie de argumenten bevatten een pronomen — dat is "
        "geen toeval maar het doel van de unit.",
        "«Vale para la tienda» is de realistische uitkomst en een prima compromis.",
    ],
    "nota": "Wissel de rollen halverwege. De verkoperrol oefent meer dan de klantrol, omdat "
            "die moet reageren op wat er komt.",
}

U6_RETO_08 = {
    "id": "C5-U6-RETO-08", "num": 8, "curso": "C5", "unidad": U6,
    "seccion": "Cultura", "ancla": "cultura_u6", "soporte": "ppt",
    "nombre": "El cliente imposible",
    "lente": "🎭 simulatie met beperking", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "El vendedor tiene que adivinar qué tipo de cliente le ha tocado.",
    "gancho_nl": "De verkoper moet raden wat voor klant hij tegenover zich heeft.",
    "consigna_es": "Interpreta tu tipo sin decirlo. El vendedor adivina al final.",
    "consigna_nl": "Speel je type zonder het te zeggen. De verkoper raadt op het einde.",
    "regla": "Je mag je type niet benoemen en niet overdrijven tot karikatuur. Het moet uit "
             "je vragen en je reacties blijken.",
    "pasos": [("Coge tu tarjeta de tipo. En secreto.", "Neem je typekaart. In het geheim."),
              ("Comprad algo. Cinco turnos como máximo.", "Koop iets. Maximaal vijf beurten."),
              ("El vendedor dice qué tipo cree que eres.", "De verkoper zegt welk type hij denkt."),
              ("¿Acierta? Cambiad de papel.", "Juist? Wissel van rol.")],
    "datos": {
        "tipos": [("el indeciso", "Todo te gusta y nada te convence. Preguntas mucho."),
                  ("el ahorrador", "Solo miras el precio. Siempre buscas algo más barato."),
                  ("el que tiene prisa", "Quieres salir en dos minutos. Nada de charla."),
                  ("el desconfiado", "Quieres saber de dónde viene todo y si se puede devolver."),
                  ("el que va a regalar", "No es para ti. No sabes la talla del otro.")],
        "marco_vendedor": ["¿Le ayudo?", "Este le queda muy bien.", "Se lo puedo enseñar en otro color.",
                           "¿Se lo envuelvo para regalo?"],
    },
    "clave": [
        "«El que va a regalar» is het makkelijkst te raden (die vraagt naar andermans maat), "
        "«el desconfiado» het moeilijkst.",
        "De verkoper oefent hier het meest: die moet vijf beurten lang blijven aanbieden met "
        "pronomina.",
        "Overdrijven bederft het spel én de taal: wie karikaturaal speelt, hoeft geen zinnen "
        "meer te bouwen.",
    ],
    "nota": "Vijf beurten is genoeg. Langer en de klant valt uit zijn rol.",
}


# --- register per unit ---
RETOS_U0 = [RETO_01, RETO_02, RETO_03, RETO_04, RETO_05,
            RETO_06, RETO_07, RETO_08, RETO_09, RETO_10]
RETOS_U1 = [U1_RETO_01, U1_RETO_02, U1_RETO_03, U1_RETO_04, U1_RETO_05,
            U1_RETO_06, U1_RETO_07, U1_RETO_08, U1_RETO_09, U1_RETO_10]
RETOS_U2 = [U2_RETO_01, U2_RETO_02, U2_RETO_03, U2_RETO_04, U2_RETO_05,
            U2_RETO_06, U2_RETO_07, U2_RETO_08, U2_RETO_09, U2_RETO_10]
RETOS_U3 = [U3_RETO_01, U3_RETO_02, U3_RETO_03, U3_RETO_04, U3_RETO_05,
            U3_RETO_06, U3_RETO_07, U3_RETO_08, U3_RETO_09, U3_RETO_10]
RETOS_U4 = [U4_RETO_01, U4_RETO_02, U4_RETO_03, U4_RETO_04, U4_RETO_05,
            U4_RETO_06, U4_RETO_07, U4_RETO_08, U4_RETO_09, U4_RETO_10]
RETOS_U5 = [U5_RETO_01, U5_RETO_02, U5_RETO_03, U5_RETO_04, U5_RETO_05,
            U5_RETO_06, U5_RETO_07, U5_RETO_08, U5_RETO_09, U5_RETO_10]
# ═══════════════════════════════════════════════════════════════════════════
# C5 · U7 «Mi casa y mi barrio» — parada Cartagena (Colombia), gastvrouw Valen
# ═══════════════════════════════════════════════════════════════════════════
U7 = 7

U7_RETO_01 = {
    "id": "C5-U7-RETO-01", "num": 1, "curso": "C5", "unidad": U7,
    "seccion": "§1.3", "ancla": "hay_estar", "soporte": "print",
    "nombre": "El plano que miente",
    "lente": "🕵️ forensisch", "forma": "👥 En parejas", "skill": "👁️ Leer",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "El anuncio dice una cosa. El plano dice otra. Tres veces.",
    "gancho_nl": "De advertentie zegt het ene. De plattegrond het andere. Drie keer.",
    "consigna_es": "Busca las tres mentiras y copia la frase exacta que las delata.",
    "consigna_nl": "Zoek de drie leugens en schrijf de zin over die ze verraadt.",
    "regla": "Aanwijzen telt niet: je citeert de zin uit de advertentie én je zegt wat het "
             "plan écht toont, met hay of está. Een leugen zonder bewijszin blijft staan.",
    "pasos": [("Leed el anuncio entero antes de mirar el plano.",
               "Lees de hele advertentie vóór je naar het plan kijkt."),
              ("Comparad habitación por habitación.", "Vergelijk kamer per kamer."),
              ("Copiad la frase que miente y escribid la verdad.",
               "Schrijf de leugenzin over en schrijf ernaast wat er echt is."),
              ("Cuidado: una frase es rara pero verdadera.",
               "Let op: één zin is vreemd maar wél waar.")],
    "datos": {
        # (zin uit de advertentie, klopt?, wat het plan toont)
        "anuncio": [
            ("El piso tiene tres habitaciones.", True, "efectivamente hay tres"),
            ("La cocina está al lado del salón.", True, "así es"),
            ("Hay dos baños completos.", False, "en el plano solo hay un baño; el segundo es un aseo sin ducha"),
            ("El balcón está en la habitación grande.", False, "el balcón sale del salón, no de la habitación"),
            ("La lavadora está en la cocina.", True, "sí, al lado de la nevera"),
            ("No hay ascensor, pero el piso está en el primero.", False, "el plano dice cuarto piso"),
            ("La habitación pequeña no tiene ventana.", True, "raro, pero el plano lo confirma"),
        ],
        "marco": ["El anuncio dice que … pero en el plano …",
                  "No hay …, hay …", "… no está en …, está en …",
                  "Aquí el anuncio dice la verdad, aunque parezca raro."],
    },
    "clave": [
        "De drie leugens: «dos baños completos» (het plan toont één badkamer + een toilet zonder "
        "douche), «el balcón está en la habitación grande» (het balkon hangt aan de salón) en "
        "«está en el primero» (het plan zegt vierde verdieping — en dan weegt «no hay ascensor»).",
        "De valstrik is «la habitación pequeña no tiene ventana»: dat klínkt als een fout maar "
        "staat zo op het plan. Wie hem aankruist, leest wat hij verwacht in plaats van wat er staat.",
        "Toets op de bewijszin, niet op het aantal gevonden leugens. «Er zijn er drie» weet de klas "
        "na dertig seconden; de zin citeren is het werk.",
    ],
    "nota": "Werkt ook als opwarmer voor de tarea final: wie een advertentie kan ontleden, "
            "schrijft er zelf een betere.",
}

U7_RETO_04 = {
    "id": "C5-U7-RETO-04", "num": 4, "curso": "C5", "unidad": U7,
    "seccion": "§1.3", "ancla": "hay_estar", "soporte": "print",
    "nombre": "Cartagena en tres capas",
    "lente": "🔬 onderzoek & data", "forma": "👤 Solo", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "La misma calle en 1600, en 1950 y hoy. ¿Qué ha desaparecido?",
    "gancho_nl": "Dezelfde straat in 1600, in 1950 en vandaag. Wat is er verdwenen?",
    "consigna_es": "Describe cada capa con hay y está, y di qué ya no existe.",
    "consigna_nl": "Beschrijf elke laag met hay en está, en zeg wat er niet meer is.",
    "regla": "Per laag minstens één zin met hay en één met está — en de laatste zin begint "
             "altijd met «Ya no hay…». Alles in het presente: je beschrijft een beeld, geen verleden.",
    "pasos": [("Mira las tres capas en orden.", "Bekijk de drie lagen op volgorde."),
              ("Describe qué hay y dónde está, capa por capa.",
               "Beschrijf wat er is en waar het staat, laag per laag."),
              ("Compara: ¿qué ha cambiado de sitio?", "Vergelijk: wat is van plaats veranderd?"),
              ("Cierra con «Ya no hay…».", "Sluit af met «Ya no hay…».")],
    "datos": {
        "capas": [
            ("1600", ["la muralla nueva", "el pozo en el centro de la plaza",
                      "las casas bajas de madera", "el mercado de pescado"]),
            ("1950", ["la muralla vieja", "una fuente donde estaba el pozo",
                      "las casas de colores", "el tranvía", "el mercado cubierto"]),
            ("hoy", ["la muralla, ahora para turistas", "una plaza sin fuente",
                     "las casas de colores, ahora hoteles", "los coches",
                     "los vendedores de fruta con carretilla"]),
        ],
        "marco": ["En 1600 hay … y está …", "En 1950 ya no hay …, ahora hay …",
                  "Hoy … está en el mismo sitio que en …", "Ya no hay …"],
    },
    "clave": [
        "De put (1600) → fontein (1950) → niets (nu): dat is de duidelijkste keten en de beste "
        "«ya no hay»-zin.",
        "De muur staat er in alle drie de lagen — hij verándert van functie, niet van plaats. "
        "Wie dat ziet, gebruikt está in plaats van hay, en dat is precies het onderscheid.",
        "Veelgemaakte fout: «en 1600 había…». Het imperfecto is C6-stof; stuur terug naar het "
        "presente («en la primera capa hay…»), dat is hier ook didactisch correct.",
    ],
    "nota": "Toont dat hay/está niet over grammatica gaat maar over bestaan en plaats — het "
            "verschil is zichtbaar op de tekening.",
}

U7_RETO_02 = {
    "id": "C5-U7-RETO-02", "num": 2, "curso": "C5", "unidad": U7,
    "seccion": "§2.3", "ancla": "preposiciones", "soporte": "print",
    "nombre": "Mudanza a ciegas",
    "lente": "🎭 simulatie met beperking", "forma": "👥 En parejas", "skill": "👂 Escuchar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Tú dictas dónde va cada mueble. Tu compañero/a no ve nada.",
    "gancho_nl": "Jij dicteert waar elk meubel komt. Je buur ziet niets.",
    "consigna_es": "Coloca los ocho muebles solo con lo que oyes. Después comparad los planos.",
    "consigna_nl": "Zet de acht meubels neer op wat je hoort. Vergelijk daarna de plannen.",
    "regla": "De ene helft van het paar mag niet kijken, de andere niet wijzen. Alleen "
             "voorzetsels: al lado de, enfrente de, debajo de, entre, en el rincón. «Daar» "
             "bestaat niet.",
    "pasos": [("A mira su plano. B tapa el suyo.", "A kijkt naar zijn plan. B dekt het zijne af."),
              ("A dicta mueble por mueble.", "A dicteert meubel per meubel."),
              ("B puede preguntar, pero solo en español.",
               "B mag vragen stellen, maar alleen in het Spaans."),
              ("Comparad. ¿Dónde se rompió la comunicación?",
               "Vergelijk. Waar liep de communicatie mis?")],
    "datos": {
        "muebles": ["el sofá", "la mesa", "las dos sillas", "la tele", "la lámpara",
                    "la estantería", "la planta", "la alfombra"],
        # (meubel, plaatsing zoals A ze moet dicteren)
        "plano_a": [
            ("el sofá", "contra la pared de la ventana"),
            ("la mesa", "delante del sofá, no debajo de la lámpara"),
            ("las dos sillas", "una a cada lado de la mesa"),
            ("la tele", "enfrente del sofá, en la estantería"),
            ("la lámpara", "en el rincón, detrás del sofá"),
            ("la estantería", "entre la puerta y la ventana"),
            ("la planta", "al lado de la puerta, no en el rincón"),
            ("la alfombra", "debajo de la mesa"),
        ],
        "marco": ["Pon … contra …", "… va delante de …", "¿Delante o detrás?",
                  "Repite, por favor: ¿al lado de qué?", "No, eso está debajo, no encima."],
    },
    "clave": [
        "De twee geplante verwarringen: de lamp staat achter de bank (niet erboven) en de tafel "
        "staat vóór de bank maar niet ónder de lamp. Wie snel werkt, zet ze samen.",
        "«La planta al lado de la puerta, no en el rincón» botst met de lamp die wél in de hoek "
        "staat — twee objecten die om dezelfde plek lijken te vechten.",
        "Toets niet op een perfect plan maar op de nabespreking: kunnen ze in het Spaans zéggen "
        "waar het misliep? Dat is de bemiddelingsvaardigheid.",
    ],
    "nota": "Laat B na afloop het plan van A dicteren voor de terugronde: dezelfde oefening, "
            "andere rol, geen nieuwe uitleg nodig.",
}

U7_RETO_06 = {
    "id": "C5-U7-RETO-06", "num": 6, "curso": "C5", "unidad": U7,
    "seccion": "§4.3", "ancla": "imperativo", "soporte": "print",
    "nombre": "Instrucciones para un robot",
    "lente": "🔓 puzzel & escape", "forma": "👥 En parejas", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "El robot hace exactamente lo que dices. Ni más, ni menos.",
    "gancho_nl": "De robot doet exact wat je zegt. Niet meer, niet minder.",
    "consigna_es": "Escribe la ruta en imperativos. Una orden vaga y el robot choca.",
    "consigna_nl": "Schrijf de route in gebiedende wijs. Eén vage opdracht en de robot botst.",
    "regla": "Elke stap is één imperatief met één handeling. «Ga naar de bakker» is verboden — "
             "de robot weet niet waar dat is. Getallen en straatnamen mogen, gebaren niet.",
    "pasos": [("Mirad el plano y la meta.", "Bekijk het plan en het doel."),
              ("Escribid la ruta, orden por orden.", "Schrijf de route, opdracht per opdracht."),
              ("Otra pareja «ejecuta» vuestras órdenes al pie de la letra.",
               "Een ander duo voert jullie opdrachten letterlijk uit."),
              ("¿Dónde choca? Corregid esa orden.", "Waar botst hij? Verbeter díe opdracht.")],
    "datos": {
        "ordenes": ["sigue", "gira", "cruza", "sube", "baja", "para", "entra", "sal"],
        "obstaculos": [
            ("una plaza redonda", "«sigue recto» no funciona: hay que decir cuántos metros y hacia dónde"),
            ("dos calles con el mismo nombre", "hace falta un número o un punto de referencia"),
            ("una escalera de doce escalones", "«sube» sin número deja al robot en el primero"),
            ("un semáforo", "el robot no espera si no se lo dices"),
            ("una puerta que se abre hacia fuera", "«entra» antes de «tira de la puerta» = choque"),
        ],
        "marco": ["Sigue … metros por la calle …", "Gira a la derecha en …",
                  "Sube … escalones.", "Para delante de …", "Entra por la puerta de …"],
    },
    "clave": [
        "De vijf hindernissen zijn elk één type vaagheid: richting zonder afstand, naam zonder "
        "nummer, werkwoord zonder aantal, ontbrekende wachtinstructie, en volgorde-omkering.",
        "De deur die naar buiten opengaat is de leukste: «entra» vóór «tira de la puerta» geeft "
        "gegarandeerd een botsing. Laat dat duo hardop uitvoeren.",
        "Toets de correctie, niet de eerste versie. De opdracht is pas gelukt als het uitvoerende "
        "duo de route foutloos loopt.",
    ],
    "nota": "Sluit rechtstreeks aan bij §4: de imperativo is hier geen tabel maar een "
            "gebruiksaanwijzing die je kunt zien mislukken.",
}

U7_RETO_05 = {
    "id": "C5-U7-RETO-05", "num": 5, "curso": "C5", "unidad": U7,
    "seccion": "§2.3", "ancla": "preposiciones", "soporte": "hub",
    "nombre": "Audioguía del barrio",
    "lente": "📻 mediaformat", "forma": "👤 Solo", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Tu calle, con voz de museo. Un minuto exacto.",
    "gancho_nl": "Jouw straat, met museumstem. Precies één minuut.",
    "consigna_es": "Graba una audioguía de tu calle con al menos cinco preposiciones de lugar.",
    "consigna_nl": "Neem een audiogids van je eigen straat op met minstens vijf plaatsvoorzetsels.",
    "regla": "Museumtoon: rustig, in de tweede persoon («ahora está usted delante de…»). Minstens "
             "vijf verschillende voorzetsels, en geen enkele twee keer.",
    "pasos": [("Escucha el modelo.", "Luister naar het model."),
              ("Apunta cinco puntos de tu calle y su preposición.",
               "Noteer vijf punten in je straat en hun voorzetsel."),
              ("Graba. Escucha. Vuelve a grabar.", "Neem op. Luister terug. Neem opnieuw op."),
              ("Marca las preposiciones que has usado.",
               "Vink de voorzetsels af die je gebruikt hebt.")],
    "datos": {
        "marco": ["Bienvenido a la calle …", "A su izquierda está …",
                  "Enfrente de … está …", "Debajo del … hay …",
                  "Entre … y … hay …", "Al final de la calle, a la derecha, está …"],
        "preposiciones": ["al lado de", "enfrente de", "debajo de", "encima de", "entre",
                          "detrás de", "delante de", "al final de", "a la izquierda de"],
    },
    "clave": [
        "Toets op vijf verschillende voorzetsels — de herhaling van «al lado de» is de standaard "
        "uitweg en telt maar één keer.",
        "De museumstem («está usted») is geen decor: het dwingt tot usted-vormen en tot traag, "
        "verstaanbaar spreken. Dat maakt de opname bruikbaar voor de klas.",
        "Beoordeel begrijpelijkheid en het aantal voorzetsels, niet het accent.",
    ],
    "nota": "Wie geen eigen straat wil delen, beschrijft de schoolomgeving — het doel is de "
            "ruimtelijke taal, niet het privéadres.",
}

U7_RETO_09 = {
    "id": "C5-U7-RETO-09", "num": 9, "curso": "C5", "unidad": U7,
    "seccion": "§3.3", "ancla": "gerundio", "soporte": "hub",
    "nombre": "¿De dónde viene el ruido?",
    "lente": "🕵️ forensisch", "forma": "👤 Solo", "skill": "👂 Escuchar",
    "tiempo": "± 10 min", "dificultad": "★★☆",
    "gancho_es": "Un piso en Cartagena, seis ruidos. ¿Quién está haciendo qué, y dónde?",
    "gancho_nl": "Een appartement in Cartagena, zes geluiden. Wie doet wat, en waar?",
    "consigna_es": "Elige qué está pasando y en qué habitación.",
    "consigna_nl": "Kies wat er gebeurt en in welke kamer.",
    "regla": "Je antwoordt altijd met estar + gerundio én met de kamer. «Cocina» alleen is geen "
             "antwoord; «alguien está cocinando en la cocina» wel.",
    "pasos": [("Escucha el ruido entero.", "Luister het geluid helemaal af."),
              ("Elige la acción, no el objeto.", "Kies de handeling, niet het voorwerp."),
              ("Comprueba: ¿la habitación encaja?", "Controleer: past de kamer erbij?")],
    "datos": {
        # (omschrijving van het geluid, juist antwoord, opties, waarom)
        "items": [
            ("Agua que cae y una voz que canta.",
             "Alguien está duchándose en el baño.",
             ["Alguien está duchándose en el baño.",
              "Alguien está fregando en la cocina.",
              "Está lloviendo en el balcón."],
             "het zingen verraadt de douche: bij de afwas zingt niemand met stromend water erbij"),
            ("Un chisporroteo y un olor imaginario a ajo.",
             "Alguien está cocinando en la cocina.",
             ["Alguien está cocinando en la cocina.",
              "Alguien está planchando en el salón.",
              "Alguien está fumando en el balcón."],
             "het sissen hoort bij de pan; strijken sist ook, maar zonder knal"),
            ("Un motor bajo, regular, y ropa que golpea.",
             "La lavadora está funcionando en la cocina.",
             ["La lavadora está funcionando en la cocina.",
              "Alguien está pasando la aspiradora en el salón.",
              "El aire acondicionado está funcionando en la habitación."],
             "kleren die tegen de trommel slaan: de stofzuiger heeft dat ritme niet"),
            ("Voces, risas y sillas que se mueven.",
             "Están comiendo en el comedor.",
             ["Están comiendo en el comedor.",
              "Están viendo la tele en el salón.",
              "Están estudiando en la habitación."],
             "stoelen die schuiven horen bij een tafel, niet bij een zetel"),
            ("Una escoba y algo que se arrastra.",
             "Alguien está barriendo en la terraza.",
             ["Alguien está barriendo en la terraza.",
              "Alguien está bailando en el salón.",
              "Alguien está moviendo la cama."],
             "het schrapende geluid op steen: binnenshuis klinkt vegen doffer"),
            ("Alguien sube y una puerta que se cierra dos veces.",
             "Alguien está entrando en el piso.",
             ["Alguien está entrando en el piso.",
              "Alguien está saliendo al balcón.",
              "Alguien está subiendo la persiana."],
             "twee deuren: die van beneden en die van het appartement"),
        ],
    },
    "clave": [
        "De vier moeilijkste: douche vs. afwas (zingen), wasmachine vs. stofzuiger (ritme), "
        "eten vs. tv (schuivende stoelen) en vegen buiten vs. binnen (steen).",
        "Elk antwoord moet het gerundio bevatten. Wie enkel de kamer noemt, heeft de "
        "grammatica-opdracht niet gedaan, ook al klopt de deductie.",
        "Op de hub geeft elke keuze de reden terug — die reden is de eigenlijke les: je hoort "
        "een hándeling, niet een voorwerp.",
    ],
    "nota": "Zolang er nog geen opnames zijn, leest de leerkracht de omschrijving voor of maakt "
            "het geluid zelf; de oefening werkt ook dan.",
}

U7_RETO_10 = {
    "id": "C5-U7-RETO-10", "num": 10, "curso": "C5", "unidad": U7,
    "seccion": "§5.3", "ancla": "ordinales", "soporte": "hub",
    "nombre": "Explícale a alguien que no ve",
    "lente": "🤝 bemiddelen", "forma": "👥 En parejas", "skill": "🔀 Bemiddelen",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Tu amigo no ve el edificio. Tiene que llegar igual.",
    "gancho_nl": "Je vriend ziet het gebouw niet. Hij moet er toch geraken.",
    "consigna_es": "Graba las instrucciones usando solo lo que se puede contar o tocar.",
    "consigna_nl": "Neem de instructies op met alleen wat je kunt tellen of voelen.",
    "regla": "Kleuren, «daar», «het grote gebouw» en wijzen bestaan niet. Wél: ordinaltallen "
             "(el tercer piso, la segunda puerta), aantallen treden, links/rechts en wat je hoort of voelt.",
    "pasos": [("Escucha el modelo y fíjate en lo que NO dice.",
               "Luister naar het model en let op wat het níet zegt."),
              ("Escribe tu ruta con números ordinales.",
               "Schrijf je route met rangtelwoorden."),
              ("Graba. Tu compañero/a la sigue con los ojos cerrados.",
               "Neem op. Je buur volgt ze met de ogen dicht."),
              ("¿Ha llegado? Si no, ¿en qué paso se perdió?",
               "Is hij aangekomen? Zo niet, bij welke stap ging het mis?")],
    "datos": {
        "marco": ["Entra por la primera puerta a la derecha.",
                  "Sube ocho escalones y para.",
                  "Es el tercer piso, la segunda puerta.",
                  "Vas a oír … a tu izquierda.",
                  "Debajo de la mano tienes … : es la señal correcta."],
        "prohibido": ["el edificio azul", "allí", "ese de ahí", "el grande",
                      "donde te dije", "mira"],
    },
    "clave": [
        "De apócope is hier functioneel, niet decoratief: «el tercer piso» en «el primer escalón» "
        "moeten kloppen, want de luisteraar telt echt mee.",
        "Wie «el edificio azul» zegt, verliest zijn hele route — kleur is voor deze luisteraar "
        "geen informatie. Dat is precies wat de reto laat voelen.",
        "Toets op aankomen, niet op mooie zinnen. De vraag «bij welke stap ging het mis?» levert "
        "de beste nabespreking.",
    ],
    "nota": "Voer dit uit met respect: het gaat om de ruimtelijke taal, niet om het naspelen van "
            "een beperking. Ogen dicht volstaat; blinddoeken hoeft niet.",
}

U7_RETO_03 = {
    "id": "C5-U7-RETO-03", "num": 3, "curso": "C5", "unidad": U7,
    "seccion": "Cultura", "ancla": "cultura_u7", "soporte": "ppt",
    "nombre": "Urbanistas por un día",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 18 min", "dificultad": "★★★",
    "gancho_es": "Una manzana vacía, doce puntos y un barrio que construir.",
    "gancho_nl": "Een leeg bouwblok, twaalf punten en een wijk om te bouwen.",
    "consigna_es": "Elegid qué construir y defended por qué sí el parque y por qué no el parking.",
    "consigna_nl": "Kies wat jullie bouwen en verdedig waarom wél het park en niet de parking.",
    "regla": "Twaalf punten, geen dertien. Elke keuze wordt verdedigd met «hay que…» of «es "
             "importante porque…» — een keuze zonder reden wordt geschrapt door de klas.",
    "pasos": [("Mirad la manzana vacía y la lista de precios.",
               "Bekijk het lege blok en de prijslijst."),
              ("Negociad: doce puntos, ni uno más.", "Onderhandel: twaalf punten, geen enkel meer."),
              ("Colocad cada cosa en el plano y decid dónde está.",
               "Plaats alles op het plan en zeg waar het staat."),
              ("Defended vuestro barrio ante la clase.", "Verdedig jullie wijk voor de klas."),
              ("La clase vota el barrio donde quiere vivir.",
               "De klas stemt over de wijk waar ze zou willen wonen.")],
    "datos": {
        "opciones": [("un parque", 4), ("un parking", 3), ("un supermercado", 3),
                     ("una escuela", 4), ("un centro de salud", 4), ("una cancha de fútbol", 2),
                     ("una biblioteca", 3), ("un mercado", 3), ("viviendas", 5),
                     ("una parada de bus", 1), ("una plaza con bancos", 2), ("un café", 1)],
        "marco": ["Nosotros ponemos … porque …", "Hay que tener … cerca de …",
                  "No hace falta …, ya hay uno en …", "Es importante porque la gente …",
                  "El … está entre … y …"],
        "dilemas": ["Sin viviendas no vive nadie en el barrio.",
                    "Sin parking los coches ocupan la plaza.",
                    "La escuela y el centro de salud juntos cuestan ocho puntos: casi todo."],
    },
    "clave": [
        "Twaalf punten dwingen tot een echt dilemma: woningen (5) plus school (4) laat maar drie "
        "punten over. Elke groep moet iets opgeven en dat hardop verantwoorden.",
        "De sterkste verdediging gebruikt plaatsbepaling: niet «wij hebben een park» maar «el "
        "parque está entre las viviendas y la escuela, para que los niños no crucen la calle».",
        "Toets de verdediging, niet de wijk. Er is geen juiste wijk; er is wel een wijk die "
        "in het Spaans overtuigend uitgelegd wordt.",
    ],
    "nota": "Sluit aan bij de Cultura-sectie over de plaza als hart van het barrio: de klas "
            "ontdekt zelf waarom die plek er is.",
}

U7_RETO_07 = {
    "id": "C5-U7-RETO-07", "num": 7, "curso": "C5", "unidad": U7,
    "seccion": "Cultura", "ancla": "cultura_u7", "soporte": "ppt",
    "nombre": "La casa del futuro sin futuro",
    "lente": "✍️ creatieve beperking", "forma": "👤 Solo", "skill": "✍️ Escribir",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Tu casa del año 2100. Y ni un solo verbo en futuro.",
    "gancho_nl": "Jouw huis van het jaar 2100. En geen enkel werkwoord in de toekomende tijd.",
    "consigna_es": "Describe tu casa del futuro solo en presente: en mi casa hay…",
    "consigna_nl": "Beschrijf je huis van de toekomst enkel in het presente: en mi casa hay…",
    "regla": "Alles in de tegenwoordige tijd, alsof je er nu rondloopt. Geen «zal», geen «gaat "
             "zijn». Wél «hay», «está», «tiene» en «se puede».",
    "pasos": [("Piensa en tres cosas que hoy no existen.",
               "Denk aan drie dingen die vandaag niet bestaan."),
              ("Descríbelas en presente, como en una foto de hoy.",
               "Beschrijf ze in het presente, als op een foto van vandaag."),
              ("Di dónde está cada una.", "Zeg waar elk ding staat."),
              ("Lee en voz alta. La clase busca un futuro escondido.",
               "Lees hardop voor. De klas zoekt een verstopte toekomende tijd.")],
    "datos": {
        "arranque": ["En mi casa hay …", "En el salón está …",
                     "Desde la ventana se ve …", "Debajo de la casa hay …",
                     "Lo mejor es que …"],
        "ejemplos": [("una cocina que cocina sola", "hoy no existe, pero se describe en presente"),
                     ("un jardín en el techo", "está encima, no arriba"),
                     ("una habitación que cambia de color", "tiene, no tendrá"),
                     ("un ascensor para la bici", "hay, no habrá")],
        "prohibido": ["será", "habrá", "tendré", "voy a tener", "estará"],
    },
    "clave": [
        "De beperking bewaakt de leerplangrens: futuro simple hoort niet in C5. Door de "
        "toekomst in het presente te beschrijven, is de oefening tegelijk creatief en conform.",
        "«Voy a tener» is de sluipweg — grammaticaal kent de klas hem uit U5, maar hij breekt "
        "de opdracht. Laat hem herformuleren naar «en mi casa hay».",
        "De sterkste teksten gebruiken plaatsbepaling: een huis beschrijven zonder «encima», "
        "«debajo» of «al lado» wordt een opsomming.",
    ],
    "nota": "Levert meteen materiaal voor de tarea final: wie zijn droomhuis kan beschrijven, "
            "beschrijft ook zijn echte barrio.",
}

U7_RETO_08 = {
    "id": "C5-U7-RETO-08", "num": 8, "curso": "C5", "unidad": U7,
    "seccion": "§4.3", "ancla": "imperativo", "soporte": "ppt",
    "nombre": "El vecino ruidoso",
    "lente": "🎭 simulatie met beperking", "forma": "👥 En parejas", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Una nota bajo la puerta. Y la respuesta, también por debajo.",
    "gancho_nl": "Een briefje onder de deur. En het antwoord, ook onder de deur.",
    "consigna_es": "Escribid las dos notas. Educadas las dos, con dos imperativos cada una.",
    "consigna_nl": "Schrijf beide briefjes. Allebei beleefd, elk met twee imperatieven.",
    "regla": "Geen scheldwoorden, geen dreigementen, geen uitroeptekens. Elke nota bevat twee "
             "imperatieven én één zin die de ander gelijk geeft («entiendo que…»).",
    "pasos": [("Leed la situación y elegid papel: vecino de arriba o de abajo.",
               "Lees de situatie en kies een rol: buur boven of beneden."),
              ("Escribid vuestra nota. Educada, con dos imperativos.",
               "Schrijf je briefje. Beleefd, met twee imperatieven."),
              ("Intercambiad las notas y contestad.", "Wissel de briefjes en antwoord."),
              ("¿Se resuelve? La clase decide qué nota funciona mejor.",
               "Is het opgelost? De klas beslist welk briefje het best werkt.")],
    "datos": {
        "situacion": [("el vecino de arriba", "Ensaya la batería a las once de la noche."),
                      ("el vecino de abajo", "Trabaja de noche y duerme de día. Le despierta todo.")],
        "imperativos": ["baja", "pon", "avisa", "llama", "espera", "ven", "dime", "perdona"],
        "cortesia": ["Entiendo que …", "No es nada personal, pero …",
                     "¿Te parece bien si …?", "Gracias por entenderlo.",
                     "Si te molesta algo mío, dímelo."],
    },
    "clave": [
        "De twee imperatieven en de begripszin zijn objectief te tellen — dat maakt de "
        "beleefdheid meetbaar in plaats van een gevoel.",
        "De sterkste briefjes gebruiken een imperatief als áánbod («llámame», «dime»), niet "
        "alleen als eis («baja la música»). Wijs daarop bij de nabespreking.",
        "Beide buren hebben gelijk: de drummer oefent, de nachtwerker slaapt. Er is geen schuldige — "
        "de opdracht is een oplossing, geen vonnis.",
    ],
    "nota": "Werkt uitstekend als échte briefwisseling: twee ronden heen en weer, en dan pas de "
            "klasbespreking.",
}

RETOS_U7 = [U7_RETO_01, U7_RETO_02, U7_RETO_03, U7_RETO_04, U7_RETO_05,
            U7_RETO_06, U7_RETO_07, U7_RETO_08, U7_RETO_09, U7_RETO_10]


# ═══════════════════════════════════════════════════════════════════════════
# C5 · U8 «¿Qué has hecho?» — parada Cusco / Machu Picchu (Perú), gastvrouw Nina
# ═══════════════════════════════════════════════════════════════════════════
U8 = 8

U8_RETO_01 = {
    "id": "C5-U8-RETO-01", "num": 1, "curso": "C5", "unidad": U8,
    "seccion": "§1.3", "ancla": "perfecto", "soporte": "print",
    "nombre": "La maleta perdida",
    "lente": "🕵️ forensisch", "forma": "👨‍👩‍👧 En grupos", "skill": "👁️ Leer",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Una maleta sin nombre en el aeropuerto de Cusco. Dentro, todo un viaje.",
    "gancho_nl": "Een koffer zonder naam op de luchthaven van Cusco. Erin: een hele reis.",
    "consigna_es": "Reconstruid dónde ha estado y qué ha hecho. Cada conclusión con su prueba.",
    "consigna_nl": "Reconstrueer waar hij geweest is en wat hij gedaan heeft. Elke conclusie mét bewijs.",
    "regla": "Elke conclusie staat in het perfecto compuesto én noemt het voorwerp dat haar "
             "bewijst. «Ha ido a la playa» zonder voorwerp telt niet.",
    "pasos": [("Vaciad la maleta: leed los quince objetos.",
               "Maak de koffer leeg: lees de vijftien voorwerpen."),
              ("Agrupad lo que va junto.", "Groepeer wat bij elkaar hoort."),
              ("Escribid cinco conclusiones con su prueba.",
               "Schrijf vijf conclusies met hun bewijs."),
              ("Un objeto no encaja. ¿Cuál, y qué significa?",
               "Eén voorwerp past niet. Welk, en wat betekent dat?")],
    "datos": {
        "objetos": [
            "un billete de bus Cusco–Puno, usado",
            "una entrada de Machu Picchu, sellada",
            "un gorro de lana con orejeras",
            "crema solar factor 50, casi vacía",
            "unas gafas de sol rayadas",
            "un cuaderno con dibujos de llamas",
            "tres monedas de dos soles",
            "un chubasquero mojado",
            "una bolsa de hojas de coca abierta",
            "un cargador de móvil con enchufe europeo",
            "una camiseta de un festival de Buenos Aires",
            "un mapa del Valle Sagrado, doblado mil veces",
            "una postal escrita pero sin sello",
            "un par de botas con barro rojo",
            "una llave de hotel de Lima, sin devolver",
        ],
        "marco": ["Ha estado en … porque hay …", "Ha visitado … : lo prueba …",
                  "Ha caminado mucho, porque …", "Todavía no ha … , porque …",
                  "Lo raro es …: eso significa que …"],
    },
    "clave": [
        "De sterkste ketens: Machu Picchu (afgestempeld ticket + modderige laarzen), de hoogte "
        "(muts + cocablad + zonnecrème: koud én fel), en Puno (busticket).",
        "«Todavía no ha enviado la postal» is de mooiste zin die de koffer toelaat — een "
        "ontkenning met marcador, precies §3.",
        "Het voorwerp dat niet past is de hotelsleutel van Lima: die is niet teruggegeven. "
        "Of de T-shirt van Buenos Aires — een ánder land. Beide antwoorden zijn te verdedigen, "
        "mits het bewijs klopt; dat is de bedoeling.",
    ],
    "nota": "Werkt het best als je de vijftien voorwerpen echt uitknipt en over de tafel legt: "
            "sorteren met de handen brengt de groep sneller tot ketens.",
}

U8_RETO_04 = {
    "id": "C5-U8-RETO-04", "num": 4, "curso": "C5", "unidad": U8,
    "seccion": "§1.3", "ancla": "perfecto", "soporte": "print",
    "nombre": "Diario de a bordo con una foto falsa",
    "lente": "✍️ creatieve beperking", "forma": "👤 Solo", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Escribe el diario de un viaje que no has hecho. Una frase te delata.",
    "gancho_nl": "Schrijf het dagboek van een reis die je niet gemaakt hebt. Eén zin verraadt je.",
    "consigna_es": "Escribe seis frases en perfecto. Cinco creíbles y una inventada de más.",
    "consigna_nl": "Schrijf zes zinnen in het perfecto. Vijf geloofwaardige en één te veel verzonnen.",
    "regla": "Alle zes de zinnen staan in het perfecto compuesto. Precies één zin is te mooi om "
             "waar te zijn — en jij weet welke. Niemand anders mag het horen aan je stem.",
    "pasos": [("Elige una de las cuatro fotos.", "Kies een van de vier foto's."),
              ("Escribe seis frases: qué has hecho allí.",
               "Schrijf zes zinnen: wat je daar gedaan hebt."),
              ("Una de las seis es demasiado. Sitúala en medio, no al final.",
               "Eén van de zes is te veel. Zet ze in het midden, niet op het einde."),
              ("Lee en voz alta. La clase vota cuál es.",
               "Lees hardop voor. De klas stemt welke het is.")],
    "datos": {
        "fotos": [("un mercado de Cusco al amanecer", "colores, mantas, mujeres con sombrero"),
                  ("un tren que sube entre montañas", "ventanas grandes, nubes debajo"),
                  ("una plaza con perros dormidos", "sol fuerte, sombra corta"),
                  ("una laguna verde a 4 000 metros", "nadie alrededor, viento")],
        "marco": ["He llegado a … a las …", "He probado … y …",
                  "He hablado con … sobre …", "He caminado … horas hasta …",
                  "No he podido … porque …", "Nunca he visto …"],
        "delatores": ["een cijfer dat te precies is", "een gevoel in plaats van een handeling",
                      "een zin zonder plaats", "een woord dat je nergens anders gebruikt"],
    },
    "clave": [
        "De verzonnen zin verraadt zich bijna altijd op één van vier manieren: te precies cijfer, "
        "gevoel in plaats van handeling, geen plaatsbepaling, of een woord dat de schrijver "
        "verder nergens gebruikt. Geef die vier pas ná de eerste ronde.",
        "«Nunca he visto…» is de mooiste val: hij klinkt oprecht en is grammaticaal precies wat "
        "§3 vraagt.",
        "Toets de zes perfecto-vormen, niet de leugen. De leugen is de motor; de participios "
        "zijn de leerstof.",
    ],
    "nota": "Geen enkele foto vraagt om een echte reis: wie nooit gereisd heeft, staat hier even "
            "sterk als wie de wereld rond is — dat is het punt van de opdracht.",
}

U8_RETO_05 = {
    "id": "C5-U8-RETO-05", "num": 5, "curso": "C5", "unidad": U8,
    "seccion": "Cultura", "ancla": "cultura_u8", "soporte": "print",
    "nombre": "Machu Picchu: ¿cuántos caben?",
    "lente": "🔬 onderzoek & data", "forma": "👥 En parejas", "skill": "👁️ Leer",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "La montaña no crece. Los visitantes sí.",
    "gancho_nl": "De berg groeit niet. De bezoekers wel.",
    "consigna_es": "Lee la tabla y escribe tres conclusiones con ha subido / ha bajado.",
    "consigna_nl": "Lees de tabel en schrijf drie conclusies met ha subido / ha bajado.",
    "regla": "Elke conclusie bevat een cijfer uit de tabel én een werkwoord in het perfecto. "
             "«Er komen te veel mensen» is een mening; «el número ha subido de … a …» is een conclusie.",
    "pasos": [("Leed la tabla entera antes de escribir.",
               "Lees de hele tabel vóór je schrijft."),
              ("Buscad la subida más grande y la única bajada.",
               "Zoek de grootste stijging en de enige daling."),
              ("Escribid tres conclusiones con cifra y perfecto.",
               "Schrijf drie conclusies met cijfer en perfecto."),
              ("¿El límite es justo? Una frase a favor, una en contra.",
               "Is de limiet rechtvaardig? Eén zin voor, één tegen.")],
    "datos": {
        # (jaar, bezoekers, dagelijkse limiet) — afgeronde, publiek bekende ordes van grootte
        "tabla": [("1990", "unos 100 000", "sin límite"),
                  ("2000", "unos 400 000", "sin límite"),
                  ("2010", "unos 700 000", "2 500 al día"),
                  ("2019", "más de 1 500 000", "5 900 al día"),
                  ("2020", "unos 200 000", "cerrado gran parte del año"),
                  ("2023", "unos 1 100 000", "4 500 al día")],
        "marco": ["El número de visitantes ha subido de … a …",
                  "En … ha bajado a …, porque …",
                  "El límite diario ha cambiado … veces.",
                  "Todavía no ha vuelto a …",
                  "Es justo / injusto porque …"],
    },
    "clave": [
        "De enige daling is 2020 (sluiting). De grootste stijging ligt tussen 2010 en 2019: "
        "van ongeveer 700 000 naar meer dan 1 500 000, meer dan een verdubbeling.",
        "«Todavía no ha vuelto al nivel de 2019» is de zin die tabel en grammatica samenbrengt — "
        "marcador plus perfecto plus cijfer.",
        "Het dilemma heeft geen juist antwoord: de limiet beschermt de site maar sluit mensen uit, "
        "onder wie Peruanen zelf. Beide zinnen moeten er staan.",
        "Cijfers zijn afgeronde ordes van grootte, geen officiële statistiek — dat mag je zeggen: "
        "een conclusie moet ook met een benadering kloppen.",
    ],
    "nota": "Sluit aan bij de Cultura-sectie: de klas leest niet over Machu Picchu, ze rekent erover.",
}

U8_RETO_08 = {
    "id": "C5-U8-RETO-08", "num": 8, "curso": "C5", "unidad": U8,
    "seccion": "§2.3", "ancla": "participios", "soporte": "print",
    "nombre": "Balance del año, sin «he sido»",
    "lente": "✍️ creatieve beperking", "forma": "👤 Solo", "skill": "✍️ Escribir",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Tu año en ocho frases. Y sin ser ni estar.",
    "gancho_nl": "Jouw jaar in acht zinnen. En zonder ser en zonder estar.",
    "consigna_es": "Escribe ocho frases en perfecto sobre tu año, con ocho participios distintos.",
    "consigna_nl": "Schrijf acht zinnen in het perfecto over je jaar, met acht verschillende participia.",
    "regla": "Ser en estar zijn verboden — dus geen «he sido feliz» en geen «he estado en». "
             "Alleen handelingswerkwoorden, en geen enkel participium twee keer.",
    "pasos": [("Piensa en ocho cosas que has hecho, no en cómo te has sentido.",
               "Denk aan acht dingen die je gedaan hebt, niet aan hoe je je voelde."),
              ("Escribe cada una con un participio distinto.",
               "Schrijf elke zin met een ander voltooid deelwoord."),
              ("Marca los irregulares: ¿cuántos has usado?",
               "Markeer de onregelmatige: hoeveel heb je er gebruikt?"),
              ("Cambia una frase floja por una concreta.",
               "Vervang één slappe zin door een concrete.")],
    "datos": {
        "banco": ["aprender", "empezar", "dejar", "descubrir", "escribir", "romper",
                  "ganar", "perder", "conocer", "volver", "abrir", "decir",
                  "hacer", "ver", "poner", "leer", "viajar", "cambiar"],
        "irregulares": [("escribir", "escrito"), ("descubrir", "descubierto"),
                        ("romper", "roto"), ("volver", "vuelto"), ("abrir", "abierto"),
                        ("decir", "dicho"), ("hacer", "hecho"), ("ver", "visto"),
                        ("poner", "puesto")],
        "marco": ["Este año he …", "Por fin he …", "Todavía no he …",
                  "He … dos veces.", "Ya he … , pero todavía no he …"],
    },
    "clave": [
        "Het verbod op ser en estar is de hele didactiek: «he sido feliz» is de zin die iedereen "
        "schrijft, en het is de enige zin die géén handeling bevat.",
        "De bank bevat negen onregelmatige participia. Wie er drie of meer gebruikt, heeft §2 "
        "actief toegepast in plaats van het rijtje herkend.",
        "«Nunca antes había…» in het marco is bewust een lokkertje: dat is pluscuamperfecto en "
        "hoort niet in C5. Wie het gebruikt, herformuleert naar «nunca he…» — een nuttige "
        "vergissing om klassikaal te bespreken.",
    ],
    "nota": "Iedereen heeft een jaar gehad; niemand hoeft het beste jaar te hebben gehad. "
            "«He dejado de…» is een even goede zin als «he ganado…».",
}

U8_RETO_03 = {
    "id": "C5-U8-RETO-03", "num": 3, "curso": "C5", "unidad": U8,
    "seccion": "§4.3", "ancla": "clima", "soporte": "hub",
    "nombre": "El parte del tiempo en directo",
    "lente": "📻 mediaformat", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Tres ciudades, un minuto, y la cámara está en directo.",
    "gancho_nl": "Drie steden, één minuut, en de camera staat live.",
    "consigna_es": "Graba el parte del tiempo de tres ciudades peruanas, con gestos y todo.",
    "consigna_nl": "Neem het weerbericht van drie Peruaanse steden op, gebaren inbegrepen.",
    "regla": "Eén minuut, drie steden, geen pauze langer dan drie seconden. Elke stad krijgt een "
             "temperatuur, een weertype en één advies («lleva…»).",
    "pasos": [("Escucha el modelo y fíjate en el ritmo.",
               "Luister naar het model en let op het tempo."),
              ("Reparte las ciudades: uno presenta, otro cronometra.",
               "Verdeel de steden: één presenteert, één klokt."),
              ("Graba de una vez. Sin cortes.", "Neem in één keer op. Zonder knippen."),
              ("Escucha: ¿has llegado al minuto? ¿Y los tres consejos?",
               "Luister terug: haalde je de minuut? En de drie adviezen?")],
    "datos": {
        "ciudades": [("Lima", "18 °C", "nublado, sin lluvia", "la costa"),
                     ("Cusco", "6 °C por la mañana, 19 °C a mediodía", "sol fuerte y frío",
                      "la sierra, 3 400 m"),
                     ("Iquitos", "31 °C", "calor y tormenta por la tarde", "la selva")],
        "marco": ["Buenos días, aquí el tiempo para hoy.",
                  "En … hace … y la temperatura es de … grados.",
                  "Por la tarde …", "Si sales, lleva …",
                  "Y hasta aquí el parte. ¡Hasta mañana!"],
    },
    "clave": [
        "Het echte leerpunt is dat Peru drie klimaten tegelijk heeft: kust, hooggebergte en "
        "jungle, op dezelfde dag. Wie dat benoemt, heeft de cultuurinhoud te pakken.",
        "Cusco is de moeilijkste: twee temperaturen op één dag. Dat dwingt tot «por la mañana» "
        "en «a mediodía» — precies de tijdsbepalingen van §3.",
        "Toets vloeiendheid en de drie adviezen, niet de uitspraak. Eén minuut zonder lange "
        "stiltes is voor A1/A2 een echte prestatie.",
    ],
    "nota": "Een groot scherm met de kaart erachter maakt het af; een blad papier met de drie "
            "steden werkt evengoed.",
}

U8_RETO_09 = {
    "id": "C5-U8-RETO-09", "num": 9, "curso": "C5", "unidad": U8,
    "seccion": "§3.3", "ancla": "marcadores", "soporte": "hub",
    "nombre": "Postal para el yo de septiembre",
    "lente": "✍️ creatieve beperking", "forma": "👤 Solo", "skill": "✍️ Escribir",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Escribe a quien eras en septiembre. Cuenta lo que no esperaba.",
    "gancho_nl": "Schrijf aan wie je in september was. Vertel wat die niet verwachtte.",
    "consigna_es": "Escribe la postal con ya, todavía no y nunca — cada uno una vez.",
    "consigna_nl": "Schrijf de kaart met ya, todavía no en nunca — elk één keer.",
    "regla": "Alle drie de marcadores komen erin, elk precies één keer, en elk in een zin die "
             "écht over jou gaat. Een lijstje met de drie woorden is geen kaart.",
    "pasos": [("Piensa: ¿qué es lo más inesperado que has hecho desde septiembre?",
               "Denk na: wat heb je gedaan dat je in september niet zag aankomen?"),
              ("Escribe cinco frases: saludo, tres noticias, despedida.",
               "Schrijf vijf zinnen: groet, drie nieuwtjes, afsluiting."),
              ("Coloca ya, todavía no y nunca, una vez cada uno.",
               "Plaats ya, todavía no en nunca, elk één keer."),
              ("Léela otra vez: ¿suena a ti?", "Lees ze nog eens: klinkt ze als jij?")],
    "datos": {
        "marco": ["Querido yo de septiembre:", "Ya he …", "Todavía no he …",
                  "Nunca he … , y eso me sorprende.", "Nos vemos en septiembre. Un abrazo,"],
        "temas": ["algo que has aprendido", "algo que has dejado", "alguien que has conocido",
                  "un sitio nuevo", "algo que te ha costado", "algo que te ha salido bien"],
    },
    "clave": [
        "Elk van de drie marcadores dwingt een ander zinstype af: «ya» een afgeronde handeling, "
        "«todavía no» een openstaande, «nunca» een ontkenning over je hele leven. Wie ze alle "
        "drie correct plaatst, beheerst §3.",
        "Veelgemaakte fout: «todavía no he ido nunca». De twee ontkenningen stapelen is in het "
        "Spaans niet fout, maar hier verspil je twee van je drie marcadores in één zin.",
        "Beoordeel de drie marcadores en de vijf zinnen. De inhoud is privé; niemand hoeft "
        "voor te lezen.",
    ],
    "nota": "De kaart hoeft niet ingeleverd te worden om te tellen: laat de leerling de drie "
            "marcadores markeren en enkel die tonen als hij dat wil.",
}

U8_RETO_10 = {
    "id": "C5-U8-RETO-10", "num": 10, "curso": "C5", "unidad": U8,
    "seccion": "Cultura", "ancla": "cultura_u8", "soporte": "hub",
    "nombre": "Traduce la aventura",
    "lente": "🤝 bemiddelen", "forma": "👥 En parejas", "skill": "🔀 Bemiddelen",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Un blog en neerlandés. Cuéntalo en español, más corto y más claro.",
    "gancho_nl": "Een blog in het Nederlands. Vertel het in het Spaans, korter en duidelijker.",
    "consigna_es": "Resume cada fragmento en dos frases de perfecto. No traduzcas palabra por palabra.",
    "consigna_nl": "Vat elk fragment samen in twee perfecto-zinnen. Vertaal niet woord voor woord.",
    "regla": "Twee zinnen per fragment, geen drie. Woord-voor-woord vertalen is fout, ook als het "
             "klopt: je vertelt wat er gebeurd is, niet hoe het er stond.",
    "pasos": [("Lee el fragmento entero.", "Lees het hele fragment."),
              ("Cierra el texto. ¿Qué ha pasado, en dos frases?",
               "Sluit de tekst. Wat is er gebeurd, in twee zinnen?"),
              ("Escríbelo en perfecto.", "Schrijf het in het perfecto."),
              ("Compara con la versión de tu compañero/a.",
               "Vergelijk met de versie van je buur.")],
    "datos": {
        # (Nederlands fragment, kernboodschap, valstrik bij letterlijk vertalen)
        "items": [
            ("Onze bus vertrok om vijf uur 's ochtends en het was ijskoud. Halverwege stopten "
             "we bij een klein dorp waar we soep aten.",
             "Hemos salido muy temprano y hemos parado en un pueblo a comer sopa.",
             ["Hemos salido muy temprano y hemos parado en un pueblo a comer sopa.",
              "Nuestro bus ha salido a las cinco de la mañana y ha hecho mucho frío y en el "
              "medio hemos parado en un pueblo pequeño donde hemos comido sopa.",
              "El bus sale a las cinco y hace frío."],
             "de tweede is een correcte vertaling maar geen samenvatting; de derde staat in het presente"),
            ("Ik had mijn regenjas thuisgelaten, dus ik ben doorweekt aangekomen. Gelukkig had "
             "het hostel warme douches.",
             "He olvidado el chubasquero y he llegado empapada. Por suerte, el hostal tenía duchas calientes.",
             ["He olvidado el chubasquero y he llegado empapada. Por suerte, el hostal tenía duchas calientes.",
              "Yo he dejado mi chaqueta de lluvia en casa así que yo he llegado muy mojada.",
              "Olvido el chubasquero."],
             "de tweede vertaalt «dus» en «mijn» letterlijk; in het Spaans zijn beide overbodig"),
            ("De gids sprak Quechua met de vrouwen op de markt. Ik verstond niets, maar ik "
             "begreep alles aan hun handen.",
             "El guía ha hablado quechua con las mujeres. No he entendido las palabras, pero sí los gestos.",
             ["El guía ha hablado quechua con las mujeres. No he entendido las palabras, pero sí los gestos.",
              "El guía ha hablado quechua con las mujeres en el mercado. Yo no he entendido nada "
              "pero yo he entendido todo con sus manos.",
              "El guía habla quechua y yo no entiendo."],
             "«alles aan hun handen» wordt in het Spaans «los gestos» — daar zit de bemiddeling"),
            ("We zijn niet tot boven geraakt. Het pad was gesloten door de regen en we moesten "
             "terug. Volgende keer beter.",
             "No hemos podido subir: han cerrado el camino por la lluvia. Todavía no hemos llegado arriba.",
             ["No hemos podido subir: han cerrado el camino por la lluvia. Todavía no hemos llegado arriba.",
              "Nosotros no hemos llegado hasta arriba porque el camino ha sido cerrado por la "
              "lluvia y hemos tenido que volver.",
              "No hemos subido nunca."],
             "«volgende keer beter» wordt «todavía no» — geen futuro, dat is C6-stof"),
        ],
    },
    "clave": [
        "Bij elk fragment is de tweede optie een corrécte vertaling — en toch fout, want te lang "
        "en te letterlijk. Dat is de hele les over bemiddelen.",
        "De vierde is de belangrijkste: «volgende keer beter» lokt een futuro uit. «Todavía no "
        "hemos llegado arriba» zegt hetzelfde binnen de leerplangrens.",
        "Wijs op de drie Nederlandse gewoontes die verdwijnen in het Spaans: het bezittelijk "
        "voornaamwoord («mijn jas» → «el chubasquero»), het overbodige onderwerp («ik heb» → «he») "
        "en «dus» als vulwoord.",
    ],
    "nota": "De blogfragmenten zijn geschreven in de taal van een klasgenoot, niet in "
            "boekentaal — precies daarom is samenvatten hier moeilijker dan vertalen.",
}

U8_RETO_02 = {
    "id": "C5-U8-RETO-02", "num": 2, "curso": "C5", "unidad": U8,
    "seccion": "§3.3", "ancla": "marcadores", "soporte": "ppt",
    "nombre": "Nunca he…",
    "lente": "🔓 puzzel & escape", "forma": "🏫 Toda la clase", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Cinco dedos arriba. Cada vez que tú sí lo has hecho, baja uno.",
    "gancho_nl": "Vijf vingers in de lucht. Elke keer dat jij het wél gedaan hebt, gaat er één omlaag.",
    "consigna_es": "Di algo que nunca has hecho pero que crees que otros sí.",
    "consigna_nl": "Zeg iets wat jij nooit gedaan hebt maar waarvan je denkt dat anderen het wél deden.",
    "regla": "Elke bewering begint met «Nunca he» plus een participium — en je moet zelf "
             "verliezen als je liegt. Wie een zin zonder perfecto zegt, verliest ook een vinger.",
    "pasos": [("Todos con cinco dedos arriba.", "Iedereen vijf vingers omhoog."),
              ("Por turnos: «Nunca he …».", "Om beurten: «Nunca he …»."),
              ("Quien sí lo ha hecho, baja un dedo y lo cuenta en una frase.",
               "Wie het wél gedaan heeft, doet één vinger omlaag en vertelt het in één zin."),
              ("Gana quien queda con dedos. Y la clase apunta los participios nuevos.",
               "Wie vingers overhoudt, wint. En de klas noteert de nieuwe participia.")],
    "datos": {
        "arranques": ["Nunca he montado …", "Nunca he comido …", "Nunca he visto …",
                      "Nunca he roto …", "Nunca he dicho …", "Nunca he perdido …",
                      "Nunca he escrito …", "Nunca he vuelto a …", "Nunca he hecho …"],
        "seguras": ["Nunca he montado en camello.", "Nunca he comido insectos.",
                    "Nunca he visto el mar en invierno.", "Nunca he roto un hueso.",
                    "Nunca he dormido en una tienda.", "Nunca he cantado en público.",
                    "Nunca he hecho un pastel yo solo/a."],
        "reaccion": ["Yo sí: he …", "Yo tampoco.", "¿En serio? ¿Cuándo?",
                     "Yo también, pero solo una vez."],
    },
    "clave": [
        "De negen aanzetten dekken samen zeven onregelmatige participia (visto, roto, dicho, "
        "escrito, vuelto, hecho, puesto). Het spel is dus een verkapte drill.",
        "«Yo sí: he …» is verplicht bij het zakken van een vinger — anders wordt het een spel "
        "zonder taal. Dat is de belangrijkste spelregel om te bewaken.",
        "Houd de beweringen onschuldig: dit is een klasspel, geen biecht. De lijst «seguras» "
        "geeft veilige voorbeelden voor wie niets bedenkt.",
    ],
    "nota": "Speel twee rondes: in de tweede mag niemand een werkwoord herhalen dat al gevallen "
            "is. Daar begint de echte woordenschat.",
}

U8_RETO_06 = {
    "id": "C5-U8-RETO-06", "num": 6, "curso": "C5", "unidad": U8,
    "seccion": "§2.3", "ancla": "participios", "soporte": "ppt",
    "nombre": "La entrevista al guía",
    "lente": "🎭 simulatie met beperking", "forma": "👨‍👩‍👧 En grupos", "skill": "👂 Escuchar",
    "tiempo": "± 18 min", "dificultad": "★★★",
    "gancho_es": "Treinta años subiendo la misma montaña. ¿Qué ha cambiado?",
    "gancho_nl": "Dertig jaar dezelfde berg op. Wat is er veranderd?",
    "consigna_es": "Preparad cinco preguntas en perfecto, escuchad y resumid lo que ha cambiado.",
    "consigna_nl": "Bereid vijf perfecto-vragen voor, luister en vat samen wat er veranderd is.",
    "regla": "Alle vijf de vragen staan in het perfecto compuesto en mogen niet met ja of nee te "
             "beantwoorden zijn. Een vraag die «sí» oplevert, telt niet mee.",
    "pasos": [("En grupo: escribid cinco preguntas en perfecto.",
               "In groep: schrijf vijf vragen in het perfecto."),
              ("Comprobad: ninguna se contesta con sí o no.",
               "Controleer: geen enkele is met ja of nee te beantwoorden."),
              ("Escuchad la entrevista y anotad las respuestas.",
               "Luister naar het interview en noteer de antwoorden."),
              ("Resumid en tres frases qué ha cambiado en treinta años.",
               "Vat in drie zinnen samen wat er in dertig jaar veranderd is.")],
    "datos": {
        "guia": [("nombre", "Rosa Quispe, guía en el Camino Inca desde 1994"),
                 ("antes", "grupos de seis personas, sin permiso, sin límite de días"),
                 ("ahora", "grupos de dieciséis, permiso con meses de antelación, cupo diario"),
                 ("lo mejor", "que ahora los guías son de la zona y cobran mejor"),
                 ("lo peor", "que ahora hay basura en todo el camino")],
        "preguntas_modelo": ["¿Qué ha cambiado más en estos años?",
                             "¿Qué ha desaparecido del camino?",
                             "¿Qué ha mejorado para la gente de aquí?",
                             "¿Cuántas veces ha subido usted?",
                             "¿Qué le ha sorprendido de los turistas?"],
        "cerradas": ["¿Le gusta su trabajo?", "¿Ha subido muchas veces?",
                     "¿Es difícil?", "¿Ha visto turistas?"],
    },
    "clave": [
        "De vier «cerradas» in de data zijn expres gesloten vragen: ze staan correct in het "
        "perfecto en leveren toch niets op. Laat de klas ze eerst herformuleren.",
        "«¿Cuántas veces ha subido usted?» is de brug tussen §2 en §3: perfecto plus telbaarheid.",
        "De samenvatting moet de tweeslag bevatten: er is iets beter geworden (lokale gidsen, "
        "betere lonen) én iets slechter (afval, drukte). Wie maar één kant noemt, heeft het "
        "interview half gehoord.",
    ],
    "nota": "Rosa Quispe is een samengesteld personage op basis van hoe het Camino Inca "
            "geregeld is; geen echte persoon.",
}

U8_RETO_07 = {
    "id": "C5-U8-RETO-07", "num": 7, "curso": "C5", "unidad": U8,
    "seccion": "§4.3", "ancla": "clima", "soporte": "ppt",
    "nombre": "El clima que decide",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Tres días, tres pronósticos, un solo permiso para subir.",
    "gancho_nl": "Drie dagen, drie voorspellingen, maar één vergunning om te klimmen.",
    "consigna_es": "Decidid juntos qué día salís y defended la decisión con el tiempo.",
    "consigna_nl": "Beslis samen op welke dag jullie vertrekken en verdedig het met het weer.",
    "regla": "Elke stem wordt verantwoord met een weerdetail én een gevolg («si llueve, el "
             "camino…»). Een stem zonder weerreden telt niet mee.",
    "pasos": [("Leed los tres pronósticos.", "Lees de drie voorspellingen."),
              ("Cada uno defiende un día. Con el tiempo, no con el gusto.",
               "Iedereen verdedigt één dag. Met het weer, niet met een voorkeur."),
              ("Negociad hasta que haya mayoría.", "Onderhandel tot er een meerderheid is."),
              ("Escribid la decisión en una frase, con la razón.",
               "Schrijf de beslissing in één zin, met de reden.")],
    "datos": {
        "dias": [("jueves", "sol por la mañana, tormenta a las tres",
                  "el camino de piedra se moja y resbala"),
                 ("viernes", "nublado todo el día, 4 °C, sin lluvia",
                  "frío pero seco; hay que llevar ropa de abrigo"),
                 ("sábado", "sol todo el día, 22 °C",
                  "perfecto, pero es el día con más gente y menos cupo")],
        "marco": ["Yo voto por el … porque …", "Si llueve, …",
                  "El problema del … es que …", "Prefiero pasar frío que …",
                  "Entonces salimos el …, ¿de acuerdo?"],
        "dilema": "El día con mejor tiempo es el día con más gente. No hay una respuesta correcta.",
    },
    "clave": [
        "Er is geen juiste dag: donderdag is mooi maar gevaarlijk na drieën, vrijdag is veilig "
        "maar koud, zaterdag is perfect én overvol. Elk antwoord is verdedigbaar.",
        "De sterkste argumenten koppelen weer aan gevolg: niet «llueve» maar «si llueve, el "
        "camino de piedra resbala». Dat is precies de conditionele zin met si + presente, die "
        "in C5 wél mag.",
        "Toets de verantwoording, niet de keuze. Een groep die unaniem zaterdag kiest zonder de "
        "drukte te noemen, heeft de tabel niet gelezen.",
    ],
    "nota": "Werkt ook als stemming met de voeten: drie hoeken in het lokaal, en verhuizen mag "
            "alleen ná een argument in het Spaans.",
}

RETOS_U8 = [U8_RETO_01, U8_RETO_02, U8_RETO_03, U8_RETO_04, U8_RETO_05,
            U8_RETO_06, U8_RETO_07, U8_RETO_08, U8_RETO_09, U8_RETO_10]


RETOS_U6 = [U6_RETO_01, U6_RETO_02, U6_RETO_03, U6_RETO_04, U6_RETO_05,
            U6_RETO_06, U6_RETO_07, U6_RETO_08, U6_RETO_09, U6_RETO_10]
# ═══════════════════════════════════════════════════════════════════════════
# C6+ · U0 «¡Volvemos!» — parada CDMX, terug bij nul mét de zij-instromers
# ═══════════════════════════════════════════════════════════════════════════
P0 = 0

P0_RETO_01 = {
    "id": "C6P-U0-RETO-01", "num": 1, "curso": "C6+", "unidad": P0,
    "seccion": "§2.4", "ancla": "presente_c6p", "soporte": "print",
    "nombre": "El test de nivel falso",
    "lente": "🕵️ forensisch", "forma": "👤 Solo", "skill": "👁️ Leer",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Diez frases de un test de nivel. Tú no lo haces: tú lo corriges.",
    "gancho_nl": "Tien zinnen uit een niveautest. Jij maakt hem niet: jij verbetert hem.",
    "consigna_es": "Marca las frases incorrectas, corrígelas y di qué regla falla.",
    "consigna_nl": "Kruis de foute zinnen aan, verbeter ze en zeg welke regel er misgaat.",
    "regla": "Verbeteren volstaat niet: bij elke fout schrijf je in één woord welke regel het "
             "betreft (persona · irregular · género · plural · ser/estar). Zonder die naam telt hij niet.",
    "pasos": [("Lee las diez frases de una vez.", "Lees de tien zinnen in één keer."),
              ("Marca las que no suenan bien.", "Kruis aan wat niet goed klinkt."),
              ("Corrige y nombra la regla.", "Verbeter en benoem de regel."),
              ("Cuenta: ¿cuántas has encontrado de las seis?",
               "Tel: hoeveel van de zes heb je gevonden?")],
    "datos": {
        # (zin, klopt?, correctie, regelnaam)
        "frases": [
            ("Yo soy de Bélgica y hablo neerlandés.", True, "", ""),
            ("Mi hermana tiene quince años y es muy simpática.", True, "", ""),
            ("Nosotros vivimos en Gante y estudiamos español.", True, "", ""),
            ("Ella son profesora de matemáticas.", False, "Ella es profesora de matemáticas.", "persona"),
            ("Los problemas es difíciles este año.", False, "Los problemas son difíciles este año.", "plural"),
            ("Yo tengo dieciséis años y estoy belga.", False, "…y soy belga.", "ser/estar"),
            ("Mi padre trabaja en un hospital grande.", True, "", ""),
            ("El mano de mi hermano está roto.", False, "La mano de mi hermano está rota.", "género"),
            ("Vosotros habláis muy rápido, no entiendo nada.", True, "", ""),
            ("Yo no puedo ir porque tiengo que estudiar.", False, "…porque tengo que estudiar.", "irregular"),
        ],
        "reglas": ["persona", "irregular", "género", "plural", "ser/estar"],
    },
    "clave": [
        "Zes fouten: «ella son» (persona), «los problemas es» (plural), «estoy belga» (ser/estar), "
        "«el mano … roto» (género, twee keer in één zin), «tiengo» (irregular: tener → tengo).",
        "Dat zijn er vijf zinnen met zes fouten — «el mano roto» bevat er twee. Wie op zes komt "
        "met vijf zinnen, heeft écht gelezen.",
        "«La mano» is de klassieke uitzondering: eindigt op -o en is vrouwelijk. Precies daarom "
        "staat hij erin.",
        "Het punt van de reto is diagnose zonder examenstress: de leerling ziet in tien minuten "
        "waar zijn eigen zwakke plek zit, zonder dat er een cijfer aan hangt.",
    ],
    "nota": "Ideaal in de eerste week: de zij-instromers merken dat ze meer herkennen dan ze "
            "dachten, en de eigen leerlingen zien dat ze niet alles nog paraat hebben.",
}

P0_RETO_02 = {
    "id": "C6P-U0-RETO-02", "num": 2, "curso": "C6+", "unidad": P0,
    "seccion": "§4.4", "ancla": "paises", "soporte": "print",
    "nombre": "Quién es quién del mundo hispano",
    "lente": "🔓 puzzel & escape", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★☆",
    "gancho_es": "Veinte personas, veinte países. Cinco preguntas para acertar.",
    "gancho_nl": "Twintig mensen, twintig landen. Vijf vragen om het te raden.",
    "consigna_es": "Adivina la ficha de tu compañero/a con preguntas de sí o no.",
    "consigna_nl": "Raad de fiche van je buur met ja-of-nee-vragen.",
    "regla": "Alleen ja/nee-vragen, en de landnaam mag pas in je láátste vraag vallen. Vraag je "
             "«¿es de México?» als tweede vraag, dan heb je gegokt in plaats van uitgesloten.",
    "pasos": [("Cada uno coge una ficha en secreto.", "Elk neemt in het geheim een fiche."),
              ("Preguntad por turnos. Solo sí o no.", "Vraag om beurten. Alleen ja of nee."),
              ("Apunta lo que descartas.", "Noteer wat je uitsluit."),
              ("¿Lo tienes en cinco? Cambiad de ficha.",
               "Heb je het in vijf? Wissel van fiche.")],
    "datos": {
        # (naam, land, continent/zone, extra taal, kenmerk om naar te vragen)
        "fichas": [
            ("Sofía", "México", "Norteamérica", "náhuatl en la familia", "vive junto al mar"),
            ("Mateo", "Argentina", "Cono Sur", "italiano de los abuelos", "usa «vos»"),
            ("Camila", "Colombia", "Andes/Caribe", "—", "vive en la costa"),
            ("Diego", "España", "Europa", "gallego", "vive en el noroeste"),
            ("Valentina", "Chile", "Cono Sur", "mapudungun cerca", "el país más largo"),
            ("Joaquín", "Perú", "Andes", "quechua", "vive a 3 000 metros"),
            ("Lucía", "Cuba", "Caribe", "—", "una isla"),
            ("Emilia", "Paraguay", "Cono Sur", "guaraní (oficial)", "dos lenguas oficiales"),
            ("Tomás", "Uruguay", "Cono Sur", "portugués en la frontera", "el país más pequeño del sur"),
            ("Isabela", "Venezuela", "Caribe", "wayuunaiki", "el salto de agua más alto"),
            ("Andrés", "Ecuador", "Andes", "quechua", "el país del centro del mundo"),
            ("Renata", "Bolivia", "Andes", "aymara y quechua", "dos capitales"),
            ("Gabriel", "Costa Rica", "Centroamérica", "—", "sin ejército"),
            ("Daniela", "Guatemala", "Centroamérica", "maya k'iche'", "muchos volcanes"),
            ("Nicolás", "Panamá", "Centroamérica", "—", "un canal famoso"),
            ("Marta", "Honduras", "Centroamérica", "garífuna", "ruinas mayas en Copán"),
            ("Sebastián", "El Salvador", "Centroamérica", "—", "el país más pequeño del continente"),
            ("Paula", "Nicaragua", "Centroamérica", "miskito", "el lago más grande de la zona"),
            ("Rodrigo", "República Dominicana", "Caribe", "—", "comparte isla con otro país"),
            ("Elena", "Guinea Ecuatorial", "África", "fang", "el único país hispanohablante de África"),
        ],
        "preguntas": [("¿Está en Europa?", "Ligt het in Europa?"),
                      ("¿Está en Centroamérica?", "Ligt het in Midden-Amerika?"),
                      ("¿Es una isla?", "Is het een eiland?"),
                      ("¿Tiene costa en el Caribe?", "Heeft het kust aan de Caraïben?"),
                      ("¿Se habla otra lengua oficial?", "Wordt er een andere officiële taal gesproken?"),
                      ("¿Está en los Andes?", "Ligt het in de Andes?"),
                      ("¿Es el país más grande de su zona?", "Is het het grootste land van zijn zone?")],
    },
    "clave": [
        "De slimste eerste vraag is «¿está en Centroamérica?»: zeven van de twintig fiches liggen "
        "daar. Wie met «¿es una isla?» begint, sluit er maar twee uit.",
        "Guinea Ecuatorial is de fiche die bijna niemand vindt — en precies daarom hoort hij erbij: "
        "de Spaanstalige wereld stopt niet in Amerika.",
        "Paraguay en Bolivia zijn de twee fiches met meerdere officiële talen; die vraag halveert "
        "de Andes-groep meteen.",
        "Toets het uitsluitblad, niet de winnaar. Wie noteert wat hij uitsluit, wint vanzelf.",
    ],
    "nota": "Werkt ook als hele klas met de fiches op de rug geplakt — dan moet iedereen rondlopen "
            "en Spaans praten met iedereen.",
}

P0_RETO_04 = {
    "id": "C6P-U0-RETO-04", "num": 4, "curso": "C6+", "unidad": P0,
    "seccion": "§4.4", "ancla": "paises", "soporte": "print",
    "nombre": "El mapa de las lenguas",
    "lente": "🔬 onderzoek & data", "forma": "👨‍👩‍👧 En grupos", "skill": "👁️ Leer",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "En el mundo hispano no solo se habla español. Ni de lejos.",
    "gancho_nl": "In de Spaanstalige wereld spreekt men niet alleen Spaans. Lang niet.",
    "consigna_es": "Lee la tabla y escribe tres frases con «se habla» y una cifra.",
    "consigna_nl": "Lees de tabel en schrijf drie zinnen met «se habla» en een cijfer.",
    "regla": "Elke zin bevat «se habla» of «se hablan» én een getal uit de tabel. En let op het "
             "meervoud: «se hablan dos lenguas» — het werkwoord volgt het aantal talen, niet de spreker.",
    "pasos": [("Leed la tabla entera.", "Lees de hele tabel."),
              ("Buscad la lengua con más hablantes que no es el español.",
               "Zoek de taal met de meeste sprekers die niet het Spaans is."),
              ("Escribid tres frases con «se habla(n)» y una cifra.",
               "Schrijf drie zinnen met «se habla(n)» en een cijfer."),
              ("¿Qué os sorprende más? Una frase.", "Wat verrast jullie het meest? Eén zin.")],
    "datos": {
        # (taal, waar, ongeveer aantal sprekers, status)
        "lenguas": [
            ("el quechua", "Perú, Bolivia, Ecuador", "unos 8 millones", "oficial en Perú y Bolivia"),
            ("el guaraní", "Paraguay", "unos 6 millones", "oficial, la habla casi todo el país"),
            ("el náhuatl", "México", "más de 1,5 millones", "lengua nacional reconocida"),
            ("el aymara", "Bolivia, Perú", "unos 2 millones", "oficial en Bolivia"),
            ("el maya yucateco", "México", "unos 800 000", "lengua nacional reconocida"),
            ("el catalán", "España, Andorra", "unos 9 millones", "cooficial; oficial en Andorra"),
            ("el gallego", "España", "unos 2,4 millones", "cooficial en Galicia"),
            ("el euskera", "España, Francia", "unos 750 000", "cooficial; no se parece a ninguna otra"),
            ("el mapudungun", "Chile, Argentina", "unos 250 000", "sin estatus oficial estatal"),
            ("el garífuna", "Honduras, Guatemala, Belice", "unos 200 000", "patrimonio de la UNESCO"),
        ],
        "marco": ["En … se habla … y también …",
                  "El … lo hablan unos … de personas.",
                  "En Paraguay se hablan dos lenguas oficiales: … y …",
                  "Lo que más nos sorprende es que …"],
    },
    "clave": [
        "Het quechua heeft de meeste sprekers van de inheemse talen (ongeveer 8 miljoen), maar "
        "het catalaans staat met ongeveer 9 miljoen bovenaan de hele tabel — dat verrast bijna "
        "elke klas.",
        "Paraguay is het enige land waar een inheemse taal door bijna de hele bevolking gesproken "
        "wordt. Dat is de sterkste «se hablan»-zin uit de tabel.",
        "Let op de vormfout: «se habla dos lenguas» hoort «se hablan» te zijn. Het is de enige "
        "grammaticale valstrik en hij komt bijna altijd voor.",
        "Cijfers zijn afgeronde ordes van grootte; verschillende bronnen tellen anders. Zeg dat "
        "erbij — een conclusie moet ook met een benadering kloppen.",
    ],
    "nota": "Sluit rechtstreeks aan bij de leerplancomponent «Identiteit in diversiteit»: de klas "
            "ontdekt dat eentaligheid de uitzondering is, niet de regel.",
}

P0_RETO_05 = {
    "id": "C6P-U0-RETO-05", "num": 5, "curso": "C6+", "unidad": P0,
    "seccion": "§3.4", "ancla": "genero", "soporte": "print",
    "nombre": "Adjetivos que cambian de sitio",
    "lente": "🕵️ forensisch", "forma": "👥 En parejas", "skill": "👁️ Leer",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "«Un gran hombre» y «un hombre grande» no son la misma persona.",
    "gancho_nl": "«Un gran hombre» en «un hombre grande» zijn niet dezelfde persoon.",
    "consigna_es": "Lee los seis pares en su contexto y deduce qué significa cada posición.",
    "consigna_nl": "Lees de zes paren in hun context en leid af wat elke plaats betekent.",
    "regla": "Je mag de regel niet opzoeken en niet vragen. Je leidt hem af uit de zes contexten "
             "en schrijft hem in één zin op. Pas dan vergelijk je met een ander duo.",
    "pasos": [("Leed los seis pares con su contexto.", "Lees de zes paren met hun context."),
              ("Escribid qué significa cada posición.", "Schrijf op wat elke plaats betekent."),
              ("Formulad la regla en una frase.", "Formuleer de regel in één zin."),
              ("Comparad con otra pareja. ¿Coincidís?", "Vergelijk met een ander duo. Komt het overeen?")],
    "datos": {
        # (voor, na, context die de betekenis verraadt)
        "pares": [
            ("un gran hombre", "un hombre grande",
             "Mandela fue … · Mi tío mide dos metros: es …"),
            ("un viejo amigo", "un amigo viejo",
             "Nos conocemos desde los seis años: es … · Tiene ochenta años: es …"),
            ("un pobre chico", "un chico pobre",
             "Hoy todo le sale mal: … · No tiene dinero para el bus: …"),
            ("una nueva casa", "una casa nueva",
             "Nos mudamos otra vez: es … · Solo tiene un año: es …"),
            ("el mismo libro", "el libro mismo",
             "Leemos … que ayer · No lo dice el profe, lo dice …"),
            ("cierta noticia", "una noticia cierta",
             "Me cuentan … · Está comprobado: es …"),
        ],
        "marco": ["Delante significa …", "Detrás significa …",
                  "Nuestra regla en una frase: …"],
    },
    "clave": [
        "De regel: vóór het zelfstandig naamwoord staat de betekenis subjectief of figuurlijk "
        "(een oordeel van de spreker); erna staat ze objectief en letterlijk (een eigenschap van "
        "het ding zelf).",
        "«Gran» is bovendien apocope: vóór een enkelvoudig zelfstandig naamwoord verliest «grande» "
        "zijn slot. Dat is een tweede vondst die de klas er gratis bij krijgt.",
        "«El mismo libro» (hetzelfde) tegenover «el libro mismo» (het boek zelf) is het paar dat "
        "het verst van het Nederlands ligt en dus het langst duurt.",
        "Toets de geformuleerde regel, niet de zes paren. Wie de paren juist heeft maar geen regel "
        "kan schrijven, heeft gegokt.",
    ],
    "nota": "Deze reto is bewust inductief: de klas ontdekt de regel zelf. Geef hem niet vooraf, "
            "ook niet als het stil wordt — de stilte is de oefening.",
}

P0_RETO_06 = {
    "id": "C6P-U0-RETO-06", "num": 6, "curso": "C6+", "unidad": P0,
    "seccion": "§3.4", "ancla": "genero", "soporte": "hub",
    "nombre": "Retrato en negativo",
    "lente": "✍️ creatieve beperking", "forma": "👤 Solo", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Descríbete sin decir ni una sola vez lo que sí eres.",
    "gancho_nl": "Beschrijf jezelf zonder één keer te zeggen wat je wél bent.",
    "consigna_es": "Graba seis frases que empiecen por «No soy…» o «Nunca…». La clase adivina quién eres.",
    "consigna_nl": "Neem zes zinnen op die beginnen met «No soy…» of «Nunca…». De klas raadt wie je bent.",
    "regla": "Elke zin is een ontkenning, en elk adjectief komt maar één keer voor. «No soy alto» "
             "en daarna «no soy bajo» mag niet: je moet echt kiezen wat je níet bent.",
    "pasos": [("Piensa en seis cosas que no eres o no haces.",
               "Denk aan zes dingen die je niet bent of niet doet."),
              ("Cuida la concordancia: no soy tímido / tímida.",
               "Let op de overeenkomst: no soy tímido / tímida."),
              ("Graba las seis frases seguidas.", "Neem de zes zinnen na elkaar op."),
              ("Escucha: ¿se adivina quién eres?", "Luister terug: is het te raden wie je bent?")],
    "datos": {
        "marco": ["No soy nada …", "Nunca llego …", "No me gusta …",
                  "No soy de los que …", "Nunca he sido …", "Y no, tampoco soy …"],
        "adjetivos": ["tímido/-a", "ruidoso/-a", "ordenado/-a", "puntual", "deportista",
                      "madrugador/-a", "hablador/-a", "paciente", "friolero/-a", "goloso/-a"],
    },
    "clave": [
        "De ontkenning dwingt tot precieze overeenkomst: «no soy ordenada» met -a, «no soy "
        "puntual» zonder. De adjectieven op -a/-o en die op medeklinker staan door elkaar in "
        "de lijst, precies daarom.",
        "«Nunca he sido…» is een perfecto en dus C5-herhaling: laat het staan, het is de brug "
        "naar wat de zij-instromers nog moeten leren.",
        "Beoordeel de zes ontkenningen en de overeenkomst. Wie geraden wordt, heeft bonus — maar "
        "het doel is de adjectiefvorm, niet het raadspel.",
    ],
    "nota": "Een negatief zelfportret is minder blootgevend dan een positief: je zegt wat je níet "
            "bent, en dat is voor veel leerlingen makkelijker in september.",
}

P0_RETO_07 = {
    "id": "C6P-U0-RETO-07", "num": 7, "curso": "C6+", "unidad": P0,
    "seccion": "§1.4", "ancla": "saludos_c6p", "soporte": "hub",
    "nombre": "Radio bienvenida",
    "lente": "📻 mediaformat", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Treinta segundos para que alguien que empieza de cero se sienta bienvenido.",
    "gancho_nl": "Dertig seconden om iemand die van nul begint welkom te laten voelen.",
    "consigna_es": "Graba un mensaje de bienvenida en español lento y claro.",
    "consigna_nl": "Neem een welkomstboodschap op in traag en helder Spaans.",
    "regla": "Dertig seconden, en je publiek kent nog geen Spaans. Dus: korte zinnen, geen "
             "jargon, en elk moeilijk woord meteen uitgelegd met een ander Spaans woord — niet "
             "met Nederlands.",
    "pasos": [("Pensad en quién os escucha: alguien que empieza hoy.",
               "Denk aan wie luistert: iemand die vandaag begint."),
              ("Escribid cinco frases cortas.", "Schrijf vijf korte zinnen."),
              ("Grabad despacio. Sin correr.", "Neem traag op. Niet haasten."),
              ("Escuchad: ¿lo entiende alguien que empieza de cero?",
               "Luister terug: zou iemand van nul het snappen?")],
    "datos": {
        "marco": ["¡Hola! Bienvenido a la clase de español.",
                  "Aquí no pasa nada si te equivocas — de verdad.",
                  "En esta clase … , es decir, …",
                  "Si no entiendes algo, dices: «¿puedes repetir, por favor?»",
                  "Nos vemos el … . ¡Hasta pronto!"],
        "trucos": [("habla despacio", "el ritmo importa más que el vocabulario"),
                   ("repite lo importante", "una vez al principio y otra al final"),
                   ("explica en español", "«el aula, es decir, la clase»"),
                   ("usa la voz", "una sonrisa se oye")],
    },
    "clave": [
        "«Es decir» is de sleutelchunk: uitleggen in het Spaans zelf in plaats van terugvallen op "
        "het Nederlands. Wie hem twee keer gebruikt, heeft de opdracht begrepen.",
        "Toets op tempo en begrijpelijkheid, niet op woordenschat. Een boodschap van vijf simpele "
        "zinnen die aankomt, is beter dan tien mooie die te snel gaan.",
        "De zin over fouten maken is er niet toevallig: hij zet meteen het veilige klimaat neer "
        "dat het leerplan vraagt — in het Spaans, door een medeleerling.",
    ],
    "nota": "Speel de beste opnames écht af in de eerste les van het volgende schooljaar. Dat "
            "maakt van de opdracht een echte, en de klas weet dat.",
}

P0_RETO_08 = {
    "id": "C6P-U0-RETO-08", "num": 8, "curso": "C6+", "unidad": P0,
    "seccion": "§1.4", "ancla": "saludos_c6p", "soporte": "hub",
    "nombre": "El intercambio",
    "lente": "🤝 bemiddelen", "forma": "👤 Solo", "skill": "🔀 Bemiddelen",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Un correo de Buenos Aires con tres preguntas que no entiendes del todo.",
    "gancho_nl": "Een mail uit Buenos Aires met drie vragen die je niet helemaal begrijpt.",
    "consigna_es": "Elige la mejor forma de pedir aclaración. En español, siempre.",
    "consigna_nl": "Kies de beste manier om verduidelijking te vragen. In het Spaans, altijd.",
    "regla": "Niet doen alsof je het begrijpt, en niet overschakelen op het Engels. Je vraagt in "
             "het Spaans wat je niet snapt — en je zegt erbij wát je wél begrepen hebt.",
    "pasos": [("Lee el correo entero.", "Lees de hele mail."),
              ("Marca lo que no entiendes.", "Markeer wat je niet begrijpt."),
              ("Elige cómo lo preguntas.", "Kies hoe je het vraagt.")],
    "datos": {
        # (zin uit de mail, beste reactie, opties, waarom)
        "items": [
            ("«¿Vos tenés clases los sábados?»",
             "¿«Vos tenés» es lo mismo que «tú tienes»?",
             ["¿«Vos tenés» es lo mismo que «tú tienes»?",
              "Sorry, I don't understand.",
              "Sí, sí, claro."],
             "je vraagt naar de vórm die je niet kent — en je toont dat je de rest wel snapte"),
            ("«Acá el cole empieza en marzo, ¿allá también?»",
             "Entiendo «empieza en marzo». ¿«El cole» es el instituto?",
             ["Entiendo «empieza en marzo». ¿«El cole» es el instituto?",
              "No entiendo nada.",
              "¿Puedes escribir en inglés?"],
             "zeggen wat je wél begreep maakt de vraag korter en beleefder"),
            ("«Te mando un audio, así practicás.»",
             "¿«Practicás» es «practicas»? Es que aquí no usamos «vos».",
             ["¿«Practicás» es «practicas»? Es que aquí no usamos «vos».",
              "Vale, gracias.",
              "¿Qué significa todo eso?"],
             "«¿qué significa todo eso?» is te vaag: de ander weet niet wat hij moet uitleggen"),
            ("«¿Qué onda con el finde?»",
             "¿«Qué onda» quiere decir «qué tal»? ¿Y «el finde»?",
             ["¿«Qué onda» quiere decir «qué tal»? ¿Y «el finde»?",
              "Sí, todo bien.",
              "No sé qué contestar."],
             "twee onbekende woorden in één zin: vraag ze allebei, in één keer"),
        ],
    },
    "clave": [
        "De sleutel is telkens hetzelfde: benoem wát je niet begrijpt en zeg wat je wél begreep. "
        "«No entiendo nada» is bijna altijd onwaar en helpt de ander niet.",
        "De mail is in Argentijns Spaans: «vos tenés», «practicás», «acá», «el cole», «el finde», "
        "«qué onda». Dat is geen fout maar een variëteit — en dat inzicht is de cultuurinhoud.",
        "Wie in het Engels antwoordt, heeft de reto verloren, ook al is de vraag correct. "
        "Bemiddelen is hier: binnen de taal blijven.",
    ],
    "nota": "Mateo uit Buenos Aires komt in C6 terug als vast castlid met voseo. Deze reto is "
            "zijn eerste optreden.",
}

P0_RETO_03 = {
    "id": "C6P-U0-RETO-03", "num": 3, "curso": "C6+", "unidad": P0,
    "seccion": "§2.4", "ancla": "presente_c6p", "soporte": "ppt",
    "nombre": "La entrevista de trabajo absurda",
    "lente": "🎭 simulatie met beperking", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Probador de camas. Cuidador de pandas. Catador de helados. Y hay que convencer.",
    "gancho_nl": "Beroepsslaper. Pandaverzorger. IJsproever. En je moet overtuigen.",
    "consigna_es": "Haz la entrevista. Todo en presente, y con un argumento por respuesta.",
    "consigna_nl": "Doe het sollicitatiegesprek. Alles in het presente, met één argument per antwoord.",
    "regla": "Alles in het presente — geen verleden, geen toekomst. En op elke vraag antwoord je "
             "met een reden («porque…»), nooit met alleen «sí».",
    "pasos": [("Elegid un trabajo absurdo.", "Kies een absurde baan."),
              ("El entrevistador elige cinco preguntas.", "De interviewer kiest vijf vragen."),
              ("El candidato contesta en presente, con porque.",
               "De kandidaat antwoordt in het presente, met porque."),
              ("Cambiad de papel.", "Wissel van rol."),
              ("La clase decide quién contrata a quién.",
               "De klas beslist wie wie aanneemt.")],
    "datos": {
        "trabajos": [("probador/-a de camas", "duermes ocho horas al día, por trabajo"),
                     ("cuidador/-a de pandas", "en China, con dos pandas de un año"),
                     ("catador/-a de helados", "veinte sabores al día, todo el año"),
                     ("paseador/-a de perros", "quince perros a la vez, en el centro"),
                     ("probador/-a de toboganes", "en parques acuáticos de todo el mundo"),
                     ("oledor/-a de perfumes", "y no puedes resfriarte nunca")],
        "preguntas": ["¿Por qué quiere este trabajo?", "¿Qué hace usted un día normal?",
                      "¿Cuál es su mayor defecto?", "¿Trabaja mejor solo o en equipo?",
                      "¿Qué hace si algo sale mal?", "¿Cuántas horas duerme?",
                      "¿Habla otras lenguas?", "¿Por qué usted y no otro?"],
        "marco": ["Quiero este trabajo porque …", "Normalmente … y después …",
                  "Mi defecto es que … , pero …", "Si algo sale mal, …",
                  "Soy la persona ideal porque …"],
    },
    "clave": [
        "De usted-vorm in de vragen tegenover de yo-vorm in de antwoorden is de eigenlijke drill: "
        "elke beurt oefent twee persoonsvormen tegelijk.",
        "«¿Cuál es su mayor defecto?» is de moeilijkste: het antwoord vraagt om een «pero»-zin, "
        "en dat is precies de conector die het leerplan wil.",
        "Het absurde is geen decor maar een didactisch middel: niemand kan een voorbereid antwoord "
        "uit het hoofd opzeggen over pandaverzorging, dus iedereen moet echt formuleren.",
    ],
    "nota": "Werkt sterk in de eerste weken: er is geen goed antwoord, dus zij-instromers en "
            "doorstromers staan even sterk.",
}

P0_RETO_09 = {
    "id": "C6P-U0-RETO-09", "num": 9, "curso": "C6+", "unidad": P0,
    "seccion": "§4.4", "ancla": "paises", "soporte": "ppt",
    "nombre": "Un país en cinco datos",
    "lente": "🔬 onderzoek & data", "forma": "👤 Solo", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Cinco cifras y ni una vez el nombre del país.",
    "gancho_nl": "Vijf cijfers en geen enkele keer de naam van het land.",
    "consigna_es": "Presenta tu país en cinco datos. La clase adivina cuál es.",
    "consigna_nl": "Presenteer je land in vijf cijfers. De klas raadt welk het is.",
    "regla": "De landnaam, de hoofdstad en de vlag zijn verboden. Alleen cijfers, en elk cijfer "
             "krijgt een zin met een werkwoord — een lijstje getallen is geen presentatie.",
    "pasos": [("Elige un país hispanohablante.", "Kies een Spaanstalig land."),
              ("Busca cinco cifras de verdad.", "Zoek vijf echte cijfers."),
              ("Escribe una frase por cifra.", "Schrijf één zin per cijfer."),
              ("Presenta. La clase adivina.", "Presenteer. De klas raadt."),
              ("¿Han acertado antes del quinto dato? Eran demasiado fáciles.",
               "Geraden vóór het vijfde cijfer? Dan waren ze te makkelijk.")],
    "datos": {
        "tipos_de_dato": ["habitantes", "kilómetros de costa", "número de lenguas oficiales",
                          "altura de la capital", "años de independencia",
                          "temperatura media en enero", "número de países vecinos",
                          "porcentaje del país que es selva o montaña"],
        "marco": ["En mi país viven … millones de personas.",
                  "Tiene … kilómetros de costa.", "Se hablan … lenguas oficiales.",
                  "La capital está a … metros.", "Limita con … países."],
        "ejemplo": [("dato 1", "Viven unos 6,5 millones de personas."),
                    ("dato 2", "Se hablan dos lenguas oficiales."),
                    ("dato 3", "No tiene costa."),
                    ("dato 4", "Limita con cinco países."),
                    ("dato 5", "El 90 % habla una lengua indígena.")],
    },
    "clave": [
        "Het voorbeeld is Paraguay: binnenland, twee officiële talen, guaraní bij bijna iedereen. "
        "Laat het pas zien ná de eerste ronde, anders kiest de halve klas datzelfde land.",
        "Van makkelijk naar moeilijk ordenen is de kunst: begin met het cijfer dat het minst "
        "verraadt en houd het meest kenmerkende voor het laatst.",
        "Toets de vijf zinnen (werkwoord plus cijfer), niet of het geraden wordt. Te snel geraden "
        "betekent alleen dat de volgorde beter kon.",
    ],
    "nota": "Laat elk land maar één keer kiezen: zo dekt de klas samen de hele Spaanstalige wereld "
            "af in één les.",
}

P0_RETO_10 = {
    "id": "C6P-U0-RETO-10", "num": 10, "curso": "C6+", "unidad": P0,
    "seccion": "Cultura", "ancla": "cultura_c6p0", "soporte": "ppt",
    "nombre": "La clase perfecta",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "🏫 Toda la clase", "skill": "🗣️ Hablar",
    "tiempo": "± 18 min", "dificultad": "★★★",
    "gancho_es": "Vosotros escribís las reglas de este curso. Pero en español.",
    "gancho_nl": "Jullie schrijven de afspraken van dit schooljaar. Maar in het Spaans.",
    "consigna_es": "Proponed, negociad y votad diez reglas. Cada propuesta con ser o estar.",
    "consigna_nl": "Stel voor, onderhandel en stem over tien afspraken. Elk voorstel met ser of estar.",
    "regla": "Elk voorstel bevat een zin met «es» of «está» — «es importante que hablemos "
             "español» mag niet, want dat is subjuntivo; «es importante hablar español» wel. "
             "Een voorstel zonder ser of estar komt niet op het bord.",
    "pasos": [("Cada uno escribe dos propuestas.", "Iedereen schrijft twee voorstellen."),
              ("Se leen en voz alta. Solo las que llevan ser o estar.",
               "Ze worden voorgelezen. Alleen die met ser of estar."),
              ("Se negocian las parecidas.", "De gelijkaardige worden samengevoegd."),
              ("Se vota. Diez reglas, ni una más.", "Er wordt gestemd. Tien afspraken, geen elf."),
              ("Se cuelgan en la pared, en español.", "Ze gaan aan de muur, in het Spaans.")],
    "datos": {
        "ejemplos": [("Es importante llegar a tiempo.", "una regla de todos"),
                     ("Está prohibido usar el móvil en los ejercicios orales.", "una prohibición"),
                     ("Es normal equivocarse: así se aprende.", "el clima de la clase"),
                     ("Estamos aquí para hablar, no solo para escribir.", "la prioridad"),
                     ("Es mejor preguntar que quedarse callado.", "una invitación")],
        "marco": ["Es importante …", "Está prohibido …", "Es mejor … que …",
                  "Estamos aquí para …", "No es justo que …"],
        "dilemas": ["¿Se corrige delante de toda la clase o no?",
                    "¿Se puede usar el traductor?",
                    "¿Qué pasa si alguien no ha estudiado nunca español?"],
    },
    "clave": [
        "De grammaticale grens is hier de leerstof: «es importante + infinitivo» werkt, «es "
        "importante que + subjuntivo» niet — en subjuntivo hoort niet in dit leerplan. Dat "
        "verschil is meteen een echte les.",
        "Het derde dilemma is voor deze groep het belangrijkste: de klas zit vol zij-instromers. "
        "Laat de afspraak daarover écht gemaakt worden, niet weggestemd.",
        "Toets de tien afspraken op vorm (ser of estar) en op het feit dat ze in het Spaans aan "
        "de muur hangen. De inhoud is van de klas, niet van de leerkracht.",
    ],
    "nota": "Hang ze echt op en verwijs er het hele jaar naar. Een afspraak die na één les "
            "verdwijnt, leert de klas dat de reto een spelletje was.",
}

RETOS_C6P_U0 = [P0_RETO_01, P0_RETO_02, P0_RETO_03, P0_RETO_04, P0_RETO_05,
                P0_RETO_06, P0_RETO_07, P0_RETO_08, P0_RETO_09, P0_RETO_10]


# ═══════════════════════════════════════════════════════════════════════════
# C6+ · U1 «El día a día» — parada España, het Spaanse dagritme
# ═══════════════════════════════════════════════════════════════════════════
P1 = 1

P1_RETO_01 = {
    "id": "C6P-U1-RETO-01", "num": 1, "curso": "C6+", "unidad": P1,
    "seccion": "§3.4", "ancla": "reflexivos", "soporte": "print",
    "nombre": "El turno de noche",
    "lente": "🔬 onderzoek & data", "forma": "👥 En parejas", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Se despierta a las seis. De la tarde. Todo lo demás también cambia.",
    "gancho_nl": "Hij wordt wakker om zes uur. 's Avonds. En al de rest schuift mee.",
    "consigna_es": "Reconstruye su día completo y marca qué reflexivos cambian de hora.",
    "consigna_nl": "Reconstrueer zijn hele dag en markeer welke reflexieve werkwoorden van uur veranderen.",
    "regla": "Je mag geen enkel uur verzinnen: elk uur volgt uit een gegeven. En elke zin bevat "
             "een reflexief werkwoord met het pronomen op de juiste plaats.",
    "pasos": [("Leed los ocho datos sueltos.", "Lees de acht losse gegevens."),
              ("Ordenad el día de las 18:00 a las 10:00.",
               "Zet de dag op volgorde, van 18 u tot 10 u."),
              ("Escribid cada paso con un verbo reflexivo.",
               "Schrijf elke stap met een reflexief werkwoord."),
              ("Comparad con vuestro propio día: ¿qué se invierte?",
               "Vergelijk met je eigen dag: wat draait om?")],
    "datos": {
        # (los gegeven, welk uur eruit volgt)
        "pistas": [
            ("Entra a trabajar a las diez de la noche.", "22:00"),
            ("Necesita cuatro horas entre despertarse y trabajar.", "se despierta a las 18:00"),
            ("Cena justo antes de salir de casa.", "cena sobre las 21:00"),
            ("Se ducha nada más levantarse, nunca antes de dormir.", "se ducha sobre las 18:15"),
            ("La pausa es a mitad del turno.", "sobre las 02:00"),
            ("Sale del trabajo ocho horas después de entrar.", "06:00"),
            ("Desayuna con su hija antes de que ella vaya al insti.", "07:30"),
            ("Se acuesta cuando la calle ya está llena de gente.", "sobre las 09:00"),
        ],
        "verbos": ["despertarse", "levantarse", "ducharse", "vestirse", "irse",
                   "sentarse", "acostarse", "dormirse", "peinarse", "afeitarse"],
        "marco": ["Se despierta a las … , cuando los demás …",
                  "Después de …, se …", "Mientras nosotros …, él …",
                  "Lo más raro es que se … a las …"],
    },
    "clave": [
        "De volgorde: 18:00 wakker · 18:15 douche · 21:00 avondeten · 22:00 start · 02:00 pauze · "
        "06:00 einde · 07:30 ontbijt met de dochter · 09:00 slapen.",
        "De omkering die de klas moet zien: hij ontbijt ná zijn werkdag en gaat slapen als "
        "iedereen begint. «Desayunar» blijft op zijn plaats in de vólgorde, niet op de klok.",
        "«Se ducha nada más levantarse» is de enige aanwijzing die twee uren tegelijk vastlegt — "
        "wie hem overslaat, komt er niet.",
        "Toets de plaats van het pronomen: «se despierta» maar «va a despertarse / se va a "
        "despertar». Beide zijn juist; «va a se despertar» niet.",
    ],
    "nota": "Ploegenarbeid is voor veel leerlingen thuis heel herkenbaar. Laat wie wil vertellen "
            "over de eigen thuissituatie, maar verplicht niemand.",
}

P1_RETO_03 = {
    "id": "C6P-U1-RETO-03", "num": 3, "curso": "C6+", "unidad": P1,
    "seccion": "§1.4", "ancla": "hora_c6p", "soporte": "print",
    "nombre": "La agenda saboteada",
    "lente": "🔓 puzzel & escape", "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Alguien ha cambiado cinco cosas en tu agenda. No sabes cuáles.",
    "gancho_nl": "Iemand heeft vijf dingen in je agenda veranderd. Je weet niet welke.",
    "consigna_es": "Descubre las cinco diferencias hablando con tres compañeros. No enseñes tu agenda.",
    "consigna_nl": "Ontdek de vijf verschillen door met drie klasgenoten te praten. Toon je agenda niet.",
    "regla": "Niemand mag zijn agenda laten zien. Alle uren worden hardop in woorden gezegd — "
             "«las siete y media», nooit «7.30» — en je noteert alleen wat je hóórt.",
    "pasos": [("Cada uno recibe una agenda. Cuatro son distintas.",
               "Elk krijgt een agenda. Vier zijn verschillend."),
              ("Preguntad y comparad, sin enseñar nada.",
               "Vraag en vergelijk, zonder iets te tonen."),
              ("Anotad cada diferencia con las dos horas.",
               "Noteer elk verschil met beide uren."),
              ("¿Cuál es la agenda original? Decidid en grupo.",
               "Welke is de originele agenda? Beslis in groep.")],
    "datos": {
        # (dag+moment, wat er in de "originele" agenda staat)
        "agenda": [("lunes, por la mañana", "clase de español a las nueve menos cuarto"),
                   ("lunes, por la tarde", "dentista a las cinco y media"),
                   ("martes", "entrenamiento de las siete a las nueve"),
                   ("miércoles", "examen de mates a las once en punto"),
                   ("jueves", "trabajo de grupo a las dos y cuarto"),
                   ("viernes", "cumpleaños de Lucía a las ocho de la tarde"),
                   ("sábado", "trabajo en el súper de nueve a una"),
                   ("domingo", "comida familiar a las tres")],
        "sabotajes": [("lunes, por la tarde", "dentista a las siete y media", "cambio de hora"),
                      ("miércoles", "examen de mates a las once y media", "media hora más tarde"),
                      ("viernes", "cumpleaños de Lucía a las ocho de la mañana", "mañana en vez de tarde"),
                      ("sábado", "trabajo en el súper de nueve a tres", "dos horas más"),
                      ("domingo", "comida familiar a la una", "dos horas antes")],
        "marco": ["¿A qué hora tienes …?", "Yo lo tengo a las …",
                  "Entonces no coincidimos: tú a las … y yo a las …",
                  "¿Estás seguro/-a? Repítelo, por favor.",
                  "La diferencia está en …"],
    },
    "clave": [
        "De vijf sabotages: tandarts 17:30 → 19:30, examen 11:00 → 11:30, verjaardag 20 u → 8 u "
        "'s ochtends, werk tot 13 u → 15 u, familiemaaltijd 15 u → 13 u.",
        "De lastigste is de verjaardag: «las ocho» klopt in beide agenda's — alleen «de la tarde» "
        "tegenover «de la mañana» verschilt. Wie het dagdeel niet uitspreekt, vindt hem nooit.",
        "«Las once y media» tegenover «las once en punto» is de tweede val: «en punto» wordt vaak "
        "weggelaten en dan lijken de agenda's gelijk.",
        "Toets het uitspreken van de uren in woorden. Wie «once treinta» zegt, heeft §1 omzeild.",
    ],
    "nota": "Print de vier agenda's apart en deel ze willekeurig uit; welke de echte is, weet "
            "alleen jij. De klas moet het beredeneren, niet vragen.",
}

P1_RETO_05 = {
    "id": "C6P-U1-RETO-05", "num": 5, "curso": "C6+", "unidad": P1,
    "seccion": "§2.4", "ancla": "rutina_c6p", "soporte": "print",
    "nombre": "El diario de un objeto",
    "lente": "✍️ creatieve beperking", "forma": "👤 Solo", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Tu móvil también tiene un día. Cuéntalo desde dentro.",
    "gancho_nl": "Je gsm heeft ook een dag. Vertel hem van binnenuit.",
    "consigna_es": "Escribe el día de tu objeto en primera persona, con seis verbos reflexivos.",
    "consigna_nl": "Schrijf de dag van je voorwerp in de ik-vorm, met zes reflexieve werkwoorden.",
    "regla": "Je bent het voorwerp: alles staat in de ik-vorm. Minstens zes reflexieve "
             "werkwoorden, en minstens twee ervan gebruik je figuurlijk («me apago», «me pierdo»).",
    "pasos": [("Elige tu objeto: móvil, bici, mochila, despertador…",
               "Kies je voorwerp: gsm, fiets, rugzak, wekker…"),
              ("Piensa en su día, hora por hora.", "Denk aan zijn dag, uur per uur."),
              ("Escribe en yo, con verbos reflexivos.", "Schrijf in de ik-vorm, met reflexieven."),
              ("Subraya los seis reflexivos.", "Onderstreep de zes reflexieve werkwoorden.")],
    "datos": {
        "objetos": [("el móvil", "se carga, se apaga, se cae, se raya"),
                    ("la bici", "se moja, se oxida, se aparca, se pierde"),
                    ("la mochila", "se llena, se abre, se rompe, se olvida"),
                    ("el despertador", "se enciende, se apaga, se retrasa, se calla"),
                    ("los auriculares", "se enredan, se caen, se quedan, se comparten")],
        "reflexivos": ["despertarse", "levantarse", "moverse", "quedarse", "perderse",
                       "caerse", "apagarse", "encenderse", "llenarse", "romperse",
                       "olvidarse", "callarse"],
        "marco": ["A las siete me … y ya empieza todo.",
                  "Durante la clase me … y no digo nada.",
                  "Por la tarde me … otra vez.",
                  "Lo peor del día es cuando me …",
                  "A las once me … , por fin."],
    },
    "clave": [
        "De figuurlijke reflexieven zijn het eigenlijke doel: «me apago» (ik val uit / ik geef er "
        "de brui aan) en «me pierdo» (ik raak zoek / ik haak af) werken voor een voorwerp én voor "
        "een mens. Dat dubbele leven is de literaire winst.",
        "Let op «me quedo» versus «quedo»: alleen de reflexieve vorm betekent «blijven». Dat is de "
        "meest voorkomende fout in deze reto.",
        "Toets de zes reflexieven en de consequente ik-vorm. Wie halverwege naar «él» overschakelt, "
        "is uit het personage gevallen — laat dat zien in plaats van het te rekenen als fout.",
    ],
    "nota": "Levert vaak de leukste teksten van het jaar. Bundel ze tot een «diario de los objetos "
            "de la clase» voor aan de muur.",
}

P1_RETO_09 = {
    "id": "C6P-U1-RETO-09", "num": 9, "curso": "C6+", "unidad": P1,
    "seccion": "§3.4", "ancla": "reflexivos", "soporte": "print",
    "nombre": "Instrucciones para mi sustituto",
    "lente": "✍️ creatieve beperking", "forma": "👥 En parejas", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Mañana alguien vive tu vida. Y no sabe nada.",
    "gancho_nl": "Morgen leeft iemand jouw leven. En hij weet niets.",
    "consigna_es": "Escribe el manual de tu día: horas exactas y verbos reflexivos.",
    "consigna_nl": "Schrijf de handleiding van je dag: exacte uren en reflexieve werkwoorden.",
    "regla": "Elke instructie heeft een uur én een reflexief werkwoord. En één regel is "
             "verplicht: «lo que no debes hacer» — precies één ding dat je vervanger absoluut "
             "níet mag doen.",
    "pasos": [("Escribe tu día de la mañana a la noche.",
               "Schrijf je dag van 's ochtends tot 's avonds."),
              ("Añade la hora a cada instrucción.", "Zet een uur bij elke instructie."),
              ("Añade la línea «lo que no debes hacer».",
               "Voeg de regel «wat je niet mag doen» toe."),
              ("Intercambiad. ¿Puede tu compañero/a vivir tu día?",
               "Wissel. Kan je buur jouw dag leven?")],
    "datos": {
        "bloques": [("por la mañana", "de las 6:30 a las 8:30"),
                    ("en el insti", "de las 8:30 a las 16:00"),
                    ("por la tarde", "de las 16:00 a las 19:00"),
                    ("por la noche", "de las 19:00 a las 23:00")],
        "verbos": ["despertarse", "levantarse", "ducharse", "vestirse", "desayunar",
                   "irse", "sentarse", "quedarse", "acostarse", "prepararse"],
        "marco": ["A las … te … y no lo dejes para después.",
                  "Antes de …, tienes que …", "No te olvides de …",
                  "Sobre las … te … , siempre en el mismo sitio.",
                  "Lo que NO debes hacer: …"],
    },
    "clave": [
        "De instructievorm dwingt tot de tú-imperatief mét pronomen: «levántate», «no te olvides». "
        "Dat is het lastigste stukje §3 en hier komt het vanzelf.",
        "Bevestigend gaat het pronomen vást aan het werkwoord («levántate», met accent), ontkennend "
        "ervóór («no te levantes»). Dat contrast is de kern van de nabespreking.",
        "De regel «lo que no debes hacer» levert altijd de beste zin op, en het is meteen de "
        "enige verplichte ontkennende imperatief.",
        "Toets of de vervanger de dag écht zou kunnen leven: een instructie zonder uur of zonder "
        "plaats is onbruikbaar, en dat merkt de buur meteen.",
    ],
    "nota": "Wie zijn eigen dag liever niet deelt, schrijft de handleiding voor een verzonnen "
            "persoon — de grammatica blijft dezelfde.",
}

P1_RETO_02 = {
    "id": "C6P-U1-RETO-02", "num": 2, "curso": "C6+", "unidad": P1,
    "seccion": "§4.4", "ancla": "ser_estar_c6p", "soporte": "hub",
    "nombre": "Es aburrido / está aburrido",
    "lente": "🕵️ forensisch", "forma": "👤 Solo", "skill": "👁️ Leer",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "La misma palabra, dos personas distintas. Solo la escena lo dice.",
    "gancho_nl": "Hetzelfde woord, twee verschillende mensen. Alleen het beeld beslist.",
    "consigna_es": "Elige ser o estar y di qué de la escena lo demuestra.",
    "consigna_nl": "Kies ser of estar en zeg wat in het beeld het bewijst.",
    "regla": "Kiezen volstaat niet: bij elke keuze hoort het detail uit de scène dat het bewijst. "
             "Wie kiest op gevoel, haalt de helft — en dat is precies de valstrik van dit paar.",
    "pasos": [("Lee la escena entera, no solo la frase.",
               "Lees de hele scène, niet alleen de zin."),
              ("Decide: ¿característica o momento?", "Beslis: eigenschap of moment?"),
              ("Comprueba con el detalle de la escena.",
               "Controleer met het detail uit de scène.")],
    "datos": {
        # (scène, juist antwoord, opties, waarom)
        "items": [
            ("Carla lleva veinte minutos mirando el reloj en clase de historia.",
             "Está aburrida.", ["Está aburrida.", "Es aburrida."],
             "het is dit moment, niet haar karakter: de klok verraadt de duur"),
            ("Nadie quiere sentarse al lado de Pablo: siempre cuenta lo mismo.",
             "Es aburrido.", ["Es aburrido.", "Está aburrido."],
             "«siempre» maakt er een eigenschap van"),
            ("Marta ha dormido tres horas y bosteza sin parar.",
             "Está cansada.", ["Está cansada.", "Es cansada."],
             "vermoeidheid is altijd een toestand; «es cansada» bestaat niet zo"),
            ("Este ejercicio tiene ocho pasos y cada uno depende del anterior.",
             "Es complicado.", ["Es complicado.", "Está complicado."],
             "de opbouw van de oefening is een eigenschap"),
            ("La sopa lleva media hora en la mesa.",
             "Está fría.", ["Está fría.", "Es fría."],
             "de soep is koud gewórden — een verandering, dus estar"),
            ("A Luis no le gusta hablar con desconocidos, nunca.",
             "Es callado.", ["Es callado.", "Está callado."],
             "«nunca» wijst op karakter"),
            ("Luis no ha dicho nada en toda la reunión, y eso que normalmente habla mucho.",
             "Está callado.", ["Está callado.", "Es callado."],
             "«normalmente habla mucho» maakt het uitzonderlijk, dus een moment"),
            ("El plátano tiene manchas negras por todas partes.",
             "Está malo.", ["Está malo.", "Es malo."],
             "«es malo» over eten betekent «van slechte kwaliteit», niet «bedorven»"),
            ("Mi abuelo tiene noventa años y todavía sale a caminar cada día.",
             "Está bien.", ["Está bien.", "Es bien."],
             "«es bien» bestaat niet: met bien gaat altijd estar"),
            ("Este bar abre a las seis de la mañana y cierra a las dos.",
             "Es abierto.", ["Está abierto.", "Es abierto."],
             "hier gaat het over de openingsuren als eigenschap — al is «está abierto» over "
             "dít moment ook correct Spaans, de scène beschrijft geen moment"),
            ("Sara sonríe a todo el mundo, incluso a las siete de la mañana.",
             "Es alegre.", ["Es alegre.", "Está alegre."],
             "«incluso a las siete» toont dat het altijd zo is"),
            ("Han aprobado todos y Sara no para de reírse.",
             "Está alegre.", ["Está alegre.", "Es alegre."],
             "de reden staat erbij: dus dit moment"),
        ],
    },
    "clave": [
        "De zes paren zijn bewust twee aan twee gebouwd: aburrido, callado en alegre komen elk "
        "twee keer voor, één keer als eigenschap en één keer als moment. Wie het paar ziet, "
        "heeft de regel.",
        "«Es bien» bestaat niet en «es cansada» betekent iets heel anders dan «está cansada». Die "
        "twee zijn geen keuze maar een vorm die je moet kennen.",
        "«El plátano está malo» (bedorven) tegenover «es malo» (van slechte kwaliteit) is de "
        "grappigste en blijft het langst hangen.",
        "Item tien is de moeilijkste en heeft geen absoluut fout alternatief: «está abierto» is "
        "correct Spaans, maar niet voor déze scène. Bespreek hem klassikaal.",
    ],
    "nota": "Op de hub geeft elke keuze zijn reden terug; laat de klas ná de twaalf items zelf de "
            "regel in één zin schrijven.",
}

P1_RETO_08 = {
    "id": "C6P-U1-RETO-08", "num": 8, "curso": "C6+", "unidad": P1,
    "seccion": "§2.4", "ancla": "rutina_c6p", "soporte": "hub",
    "nombre": "Podcast: cinco minutos de mi día",
    "lente": "📻 mediaformat", "forma": "👤 Solo", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "No pasa nada especial. Ese es el reto.",
    "gancho_nl": "Er gebeurt niets bijzonders. Dát is de uitdaging.",
    "consigna_es": "Graba dos minutos sobre cinco minutos cualquiera de tu día.",
    "consigna_nl": "Neem twee minuten op over vijf willekeurige minuten uit je dag.",
    "regla": "Er mag niets spannends gebeuren — geen ongeluk, geen verrassing. Wat het boeiend "
             "maakt zijn de conectoren: minstens zes verschillende, en geen twee keer dezelfde.",
    "pasos": [("Elige cinco minutos aburridos: la cola del súper, el bus, el pasillo.",
               "Kies vijf saaie minuten: de rij in de winkel, de bus, de gang."),
              ("Escribe qué pasa, en orden.", "Schrijf op wat er gebeurt, op volgorde."),
              ("Añade seis conectores distintos.", "Voeg zes verschillende conectoren toe."),
              ("Graba. Escucha. ¿Se sigue sin esfuerzo?",
               "Neem op. Luister terug. Volgt het vanzelf?")],
    "datos": {
        "conectores": ["primero", "luego", "mientras", "de repente", "entonces",
                       "al final", "por eso", "aunque", "además", "sin embargo",
                       "justo después", "en ese momento"],
        "escenarios": ["la cola del supermercado", "el bus de las ocho menos diez",
                       "el pasillo entre dos clases", "la sala de espera",
                       "los cinco minutos antes de dormir"],
        "marco": ["Son las … y estoy en …", "Primero … , luego …",
                  "Mientras …, alguien …", "Aunque no pasa nada, …",
                  "Al final … y ya está."],
    },
    "clave": [
        "«De repente» is de val: hij lokt een gebeurtenis uit, en die is verboden. Wie hem "
        "gebruikt, moet hem laten slaan op iets minuscuuls («de repente la fila avanza»).",
        "«Aunque» en «sin embargo» zijn de twee conectoren die het niveau optillen van A2 naar "
        "aanzet B1 — beloon wie ze correct gebruikt.",
        "Toets het aantal verschillende conectoren en de vlotheid, niet de inhoud. Saai is de "
        "opdracht, niet het probleem.",
    ],
    "nota": "Speel er twee af zonder te zeggen van wie. De klas hoort meteen dat de conectoren "
            "het verschil maken en niet het onderwerp.",
}

P1_RETO_10 = {
    "id": "C6P-U1-RETO-10", "num": 10, "curso": "C6+", "unidad": P1,
    "seccion": "Cultura", "ancla": "cultura_c6p1", "soporte": "hub",
    "nombre": "La cita imposible",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Cuatro agendas, un solo hueco. O ninguno.",
    "gancho_nl": "Vier agenda's, één gaatje. Of geen enkel.",
    "consigna_es": "Encuentra el único momento posible — o demuestra que no existe.",
    "consigna_nl": "Vind het enige mogelijke moment — of bewijs dat het niet bestaat.",
    "regla": "Niemand mag een afspraak schrappen of verzetten. Je zoekt binnen wat er is, en je "
             "verantwoordt elke uitsluiting met het uur én de reden.",
    "pasos": [("Leed las cuatro agendas.", "Lees de vier agenda's."),
              ("Descartad hora por hora, en voz alta.", "Sluit uur per uur uit, hardop."),
              ("Elegid el momento posible.", "Kies het mogelijke moment.")],
    "datos": {
        # (situatie, juist antwoord, opties, waarom)
        "items": [
            ("Ana entrena de 18:00 a 20:00 los martes y jueves. Beto trabaja los sábados de "
             "9:00 a 15:00. Carla tiene clase de música los miércoles a las 17:00. Dani no "
             "puede antes de las 17:00 ningún día. ¿Cuándo quedáis, si necesitáis dos horas?",
             "El sábado a las cinco de la tarde.",
             ["El sábado a las cinco de la tarde.",
              "El martes a las seis.",
              "El miércoles a las cinco."],
             "zaterdag na drie uur is Beto vrij, Dani kan vanaf vijf uur, en Ana traint niet"),
            ("Mismo grupo. Ahora solo tenéis una hora y tiene que ser entre semana. ¿Cuándo?",
             "El lunes a las cinco.",
             ["El lunes a las cinco.", "El jueves a las seis.", "El miércoles a las seis."],
             "maandag heeft niemand iets staan, en Dani kan vanaf vijf uur"),
            ("Beto cambia de turno: ahora trabaja los sábados de 15:00 a 21:00. ¿Sigue "
             "funcionando el sábado?",
             "No, ya no. Hay que buscar entre semana.",
             ["No, ya no. Hay que buscar entre semana.",
              "Sí, a las cinco igual.",
              "Sí, pero solo una hora."],
             "zijn nieuwe shift dekt precies het gaatje dat jullie hadden gevonden"),
            ("Carla dice: «Yo puedo el miércoles si empezamos a las siete.» ¿Es posible?",
             "Sí, si a Dani le va bien a las siete.",
             ["Sí, si a Dani le va bien a las siete.",
              "No, Carla tiene música.",
              "No, es demasiado tarde para todos."],
             "haar muziekles is óm zeven uur gedaan; het probleem verschuift naar Dani"),
        ],
    },
    "clave": [
        "Ronde één: zaterdag 17 u. Ronde twee: maandag 17 u. Ronde drie: het zaterdaggaatje valt "
        "weg door Beto's nieuwe shift. Ronde vier: woensdag 19 u kán, maar hangt van Dani af.",
        "De vierde is de belangrijkste: het antwoord is voorwaardelijk. «Sí, si…» met presente is "
        "precies de conditionele zin die binnen dit leerplan mag — geen condicional nodig.",
        "Toets het hardop uitsluiten. Een groep die meteen het juiste uur roept, heeft gegokt; de "
        "taal zit in «el martes no, porque Ana entrena hasta las ocho».",
        "Het Spaanse dagritme uit de Cultura-sectie speelt mee: zeven uur 's avonds is daar geen "
        "laat uur om af te spreken, hier wel. Benoem dat verschil.",
    ],
    "nota": "Sluit rechtstreeks aan bij «el horario español»: dezelfde agenda voelt in Madrid "
            "anders dan in Gent.",
}

P1_RETO_04 = {
    "id": "C6P-U1-RETO-04", "num": 4, "curso": "C6+", "unidad": P1,
    "seccion": "§3.4", "ancla": "reflexivos", "soporte": "ppt",
    "nombre": "Terapia de compañeros de piso",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 18 min", "dificultad": "★★★",
    "gancho_es": "Uno se levanta a las seis. El otro se acuesta a las tres. Viven juntos.",
    "gancho_nl": "De ene staat op om zes uur. De andere gaat slapen om drie uur. Ze wonen samen.",
    "consigna_es": "Dos exponen, uno media. El mediador resume las dos posturas antes de proponer.",
    "consigna_nl": "Twee leggen uit, één bemiddelt. De bemiddelaar vat beide standpunten samen vóór hij voorstelt.",
    "regla": "De bemiddelaar mag pas een oplossing voorstellen nadat hij béide standpunten heeft "
             "samengevat — in de derde persoon, met reflexieve werkwoorden. Vóór die samenvatting "
             "is elk voorstel ongeldig.",
    "pasos": [("Repartid los papeles: A, B y mediador/-a.",
               "Verdeel de rollen: A, B en bemiddelaar."),
              ("A y B cuentan su rutina y su queja.",
               "A en B vertellen hun routine en hun klacht."),
              ("El mediador resume las dos posturas en tercera persona.",
               "De bemiddelaar vat beide standpunten samen in de derde persoon."),
              ("Solo entonces: una propuesta concreta con horas.",
               "Pas dan: één concreet voorstel met uren."),
              ("¿Firman los dos? Cambiad de papel.", "Tekenen ze allebei? Wissel van rol.")],
    "datos": {
        "roles": [("Compañero/a A",
                   "Te levantas a las seis, te duchas con música y desayunas en la cocina. "
                   "A las diez de la noche ya estás dormido/-a."),
                  ("Compañero/a B",
                   "Te acuestas a las tres, te levantas a mediodía y estudias de noche. "
                   "La ducha de las seis te despierta cada día."),
                  ("Mediador/-a",
                   "No tomas partido. Resumes primero, propones después.")],
        "quejas": ["La ducha de las seis se oye en toda la casa.",
                   "La cocina está sucia a mediodía.",
                   "La luz del salón está encendida a las dos de la mañana.",
                   "Nadie se acuerda de sacar la basura."],
        "marco_mediador": ["Si te he entendido bien, tú te … a las …",
                           "Y tú, en cambio, te … a las …",
                           "Los dos tenéis razón en que …",
                           "¿Qué os parece si …?",
                           "¿Estáis de acuerdo con esto?"],
    },
    "clave": [
        "De samenvatting in de derde persoon is de eigenlijke oefening: «se levanta a las seis» "
        "tegenover «te levantas a las seis». Wie de rol van bemiddelaar goed speelt, vervoegt "
        "het hele reflexieve paradigma zonder dat het een drill lijkt.",
        "«Si te he entendido bien» is de sleutelchunk van bemiddelen en komt in elke ronde terug.",
        "Beide bewoners hebben gelijk: er is geen schuldige. Elk voorstel dat één van de twee "
        "vraagt zijn ritme volledig om te gooien, wordt niet getekend — en dat hoort zo.",
    ],
    "nota": "Drie ronden met wisselende rollen zorgt dat iedereen één keer bemiddelaar is. Dat is "
            "de rol waar het meeste Spaans in zit.",
}

P1_RETO_06 = {
    "id": "C6P-U1-RETO-06", "num": 6, "curso": "C6+", "unidad": P1,
    "seccion": "§4.4", "ancla": "ser_estar_c6p", "soporte": "ppt",
    "nombre": "El termómetro emocional",
    "lente": "🔬 onderzoek & data", "forma": "🏫 Toda la clase", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★☆",
    "gancho_es": "¿Cómo está la clase hoy? En cifras, y sin nombres.",
    "gancho_nl": "Hoe is de klas er vandaag aan toe? In cijfers, en zonder namen.",
    "consigna_es": "Votad en anónimo, haced el gráfico y describid la semana con estar.",
    "consigna_nl": "Stem anoniem, maak de grafiek en beschrijf de week met estar.",
    "regla": "Alles anoniem, en elke conclusie gebruikt «estar» met een percentage of een aantal. "
             "«La clase es cansada» is fout in twee opzichten — vorm én inhoud.",
    "pasos": [("Cada uno vota en anónimo: ¿cómo estás hoy, del uno al cinco?",
               "Iedereen stemt anoniem: hoe voel je je vandaag, van één tot vijf?"),
              ("Contad y haced el gráfico en la pizarra.",
               "Tel en maak de grafiek op het bord."),
              ("Escribid tres frases con estar y una cifra.",
               "Schrijf drie zinnen met estar en een cijfer."),
              ("Repetid el viernes. ¿Ha cambiado algo?",
               "Herhaal op vrijdag. Is er iets veranderd?")],
    "datos": {
        "escala": [("1", "fatal", "estoy fatal"), ("2", "regular", "estoy regular"),
                   ("3", "normal", "estoy bien"), ("4", "contento/-a", "estoy contento/-a"),
                   ("5", "genial", "estoy genial")],
        "marco": ["El … % de la clase está …",
                  "Hoy hay más gente … que el lunes.",
                  "Nadie está … , y eso es buena señal.",
                  "La media de la clase es de … sobre cinco.",
                  "El viernes la clase está … que el lunes."],
        "aviso": "Nadie tiene que decir por qué. El termómetro mide la clase, no a las personas.",
    },
    "clave": [
        "Het contrast dat de reto bewijst: «estoy» voor de stemming van vandaag, «es» alleen voor "
        "het gemiddelde als getal («la media es de 3,4»). Dat ene «es» temidden van al die "
        "«estoy»-vormen maakt de regel zichtbaar.",
        "«Está mejor que el lunes» introduceert de comparativo, die verderop in C6 terugkomt — een "
        "vooruitwijzing zonder er les van te maken.",
        "Toets de drie zinnen, niet het gemiddelde. En herhaal de meting: pas de tweéde keer zien "
        "leerlingen dat een klas een stemming heeft die verandert.",
    ],
    "nota": "Houd het anoniem en vraag nooit door. Wie zich slecht voelt, mag dat aangeven zonder "
            "dat er een gesprek volgt — dat is de afspraak die de reto veilig maakt.",
}

P1_RETO_07 = {
    "id": "C6P-U1-RETO-07", "num": 7, "curso": "C6+", "unidad": P1,
    "seccion": "§2.4", "ancla": "rutina_c6p", "soporte": "ppt",
    "nombre": "Rutinas extremas",
    "lente": "🎭 simulatie met beperking", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Astronauta, panadero de noche, nadadora olímpica. ¿Quién tiene el peor despertador?",
    "gancho_nl": "Astronaut, nachtbakker, olympisch zwemster. Wie heeft de ergste wekker?",
    "consigna_es": "Compara una rutina extrema con la tuya y di qué te parece imposible.",
    "consigna_nl": "Vergelijk een extreme routine met de jouwe en zeg wat jou onmogelijk lijkt.",
    "regla": "Elke vergelijking noemt twee uren: het zijne en het jouwe. «Se levanta muy "
             "temprano» telt niet; «se levanta a las cuatro y yo a las siete» wel.",
    "pasos": [("Elegid una rutina extrema.", "Kies een extreme routine."),
              ("Comparad hora por hora con la vuestra.",
               "Vergelijk uur per uur met die van jullie."),
              ("Decid qué os parece imposible y por qué.",
               "Zeg wat jullie onmogelijk lijkt en waarom."),
              ("¿Podéis vivir así una semana? Votad.",
               "Zouden jullie zo een week kunnen leven? Stem.")],
    "datos": {
        "rutinas": [("astronauta en la EEI",
                     "se despierta a las 6:00 UTC · hace deporte dos horas al día · "
                     "ve dieciséis amaneceres · se duerme atado"),
                    ("panadero/-a de noche",
                     "entra a las 23:00 · el primer pan sale a las 5:00 · "
                     "se acuesta a las 14:00 · libra los domingos"),
                    ("nadador/-a olímpico/-a",
                     "se levanta a las 4:45 · dos entrenamientos al día · "
                     "come cinco veces · se acuesta a las 21:00"),
                    ("médico/-a de urgencias",
                     "turnos de doce horas · come cuando puede · "
                     "duerme de día una semana de cada tres")],
        "marco": ["Se levanta a las … y yo a las …",
                  "Mientras él/ella …, yo …",
                  "Lo que me parece imposible es …",
                  "Yo no puedo … , porque …",
                  "En eso nos parecemos: los dos nos …"],
    },
    "clave": [
        "De astronaut is de leukste maar de zwemmer is didactisch de beste: zijn dag botst het "
        "hardst met een schooldag, dus de vergelijkingen komen vanzelf.",
        "«Mientras» plus presente is de conector die de reto binnenhaalt: twee handelingen op "
        "hetzelfde moment, twee verschillende personen.",
        "De vorm die op de tong ligt («yo no podría») is condicional en hoort niet in dit "
        "leerplan. Daarom geeft het marco «yo no puedo»; «para mí es imposible» werkt even goed.",
    ],
    "nota": "De zestien zonsopgangen per dag in het ruimtestation zorgen altijd voor discussie. "
            "Laat die even lopen: het is echte inhoud, in het Spaans.",
}

RETOS_C6P_U1 = [P1_RETO_01, P1_RETO_02, P1_RETO_03, P1_RETO_04, P1_RETO_05,
                P1_RETO_06, P1_RETO_07, P1_RETO_08, P1_RETO_09, P1_RETO_10]


# ═══════════════════════════════════════════════════════════════════════════
# C6+ · U2 «Aquí vivo» — parada Cartagena (Colombia), gastvrouw Valen
# ═══════════════════════════════════════════════════════════════════════════
P2 = 2

P2_RETO_01 = {
    "id": "C6P-U2-RETO-01", "num": 1, "curso": "C6+", "unidad": P2,
    "seccion": "§3.4", "ancla": "gerundio_c6p", "soporte": "print",
    "nombre": "La casa del crimen",
    "lente": "🕵️ forensisch", "forma": "👨‍👩‍👧 En grupos", "skill": "👁️ Leer",
    "tiempo": "± 18 min", "dificultad": "★★★",
    "gancho_es": "Ha desaparecido el portátil. Cuatro personas, cuatro coartadas, un plano.",
    "gancho_nl": "De laptop is verdwenen. Vier mensen, vier alibi's, één plattegrond.",
    "consigna_es": "Cruza las coartadas con el plano y di quién no pudo estar donde dice.",
    "consigna_nl": "Leg de alibi's naast de plattegrond en zeg wie niet kon zijn waar hij zegt.",
    "regla": "Elke beschuldiging staat in estar + gerundio én noemt de kamer. En je hebt twee "
             "verklaringen nodig die elkaar tegenspreken — één rare zin is geen bewijs.",
    "pasos": [("Leed las cuatro coartadas.", "Lees de vier alibi's."),
              ("Situadlas en el plano, habitación por habitación.",
               "Zet ze op het plan, kamer per kamer."),
              ("Buscad dos que no pueden ser verdad a la vez.",
               "Zoek er twee die niet tegelijk waar kunnen zijn."),
              ("Acusad, con las dos frases como prueba.",
               "Beschuldig, met de twee zinnen als bewijs.")],
    "datos": {
        "plano": ["el salón (con la ventana a la calle)", "la cocina (al lado del salón)",
                  "el baño (sin ventana)", "la habitación grande (con balcón)",
                  "la habitación pequeña (al fondo del pasillo)", "la terraza (arriba)"],
        # (persoon, alibi, in welke kamer, klopt het?)
        "coartadas": [
            ("Valen", "Estaba duchándome, por eso no oí nada.", "el baño", True),
            ("Andrés", "Estaba viendo pasar la gente por la ventana de la cocina.",
             "la cocina", False),
            ("Camila", "Estaba tendiendo la ropa arriba y saludé a Andrés, que estaba en el salón.",
             "la terraza", True),
            ("Tomás", "Estaba estudiando en la habitación del fondo con la puerta abierta.",
             "la habitación pequeña", True),
        ],
        "detalles": ["La cocina no tiene ventana a la calle: la ventana está en el salón.",
                     "Desde la terraza se ve el salón, no la cocina.",
                     "Del pasillo se ve la puerta del baño y la del salón.",
                     "El portátil estaba en el salón."],
        "marco": ["… dice que estaba … en …", "Pero desde … no se ve …",
                  "Los dos no pueden tener razón: uno dice … y el otro …",
                  "Creemos que … estaba … en el salón, porque …"],
    },
    "clave": [
        "Andrés is de dader: hij zegt dat hij door het keukenraam keek, maar de keuken heeft geen "
        "raam aan de straat — dat raam zit in de salón, waar de laptop lag.",
        "Camila levert onbewust het tweede bewijs: zij zag Andrés «en el salón». Twee verklaringen "
        "die elkaar tegenspreken, precies wat de regla eist.",
        "Valens alibi is niet te controleren (badkamer zonder raam) en juist daarom verdacht — "
        "dat is de val: onverifieerbaar is niet hetzelfde als vals.",
        "Toets de vorm: «estaba duchándome» is imperfecto en dat is C6-stof. In deze unit werkt "
        "het presente-alibi even goed: «Valen dice que está en el baño». Laat beide toe, maar "
        "eis dat het gerundio erin zit.",
    ],
    "nota": "De alibi's staan in het imperfecto omdat een verhoor nu eenmaal over het verleden "
            "gaat; de leerling hoeft die vorm alleen te herkennen, niet te produceren.",
}

P2_RETO_04 = {
    "id": "C6P-U2-RETO-04", "num": 4, "curso": "C6+", "unidad": P2,
    "seccion": "§2.4", "ancla": "hay_estar_c6p", "soporte": "print",
    "nombre": "Metros cuadrados reales",
    "lente": "🔬 onderzoek & data", "forma": "👥 En parejas", "skill": "👁️ Leer",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Tu habitación mide más que la casa entera de alguien.",
    "gancho_nl": "Jouw kamer is groter dan iemands hele huis.",
    "consigna_es": "Compara los datos y escribe tres conclusiones con hay y está.",
    "consigna_nl": "Vergelijk de cijfers en schrijf drie conclusies met hay en está.",
    "regla": "Elke conclusie bevat een cijfer én «hay» of «está». En één van de drie moet over "
             "jóuw eigen situatie gaan — anders blijft het een tabel in plaats van een inzicht.",
    "pasos": [("Leed la tabla entera.", "Lees de hele tabel."),
              ("Medid vuestra propia habitación, más o menos.",
               "Meet je eigen kamer, ongeveer."),
              ("Escribid tres conclusiones con cifra.", "Schrijf drie conclusies met een cijfer."),
              ("Una de las tres, sobre vosotros.", "Eén van de drie gaat over jullie zelf.")],
    "datos": {
        # (stad, m² per persoon, typische woning, opmerking)
        "tabla": [("Bruselas", "unos 40 m²", "un piso de dos habitaciones",
                   "muchas casas estrechas y altas"),
                  ("Madrid", "unos 32 m²", "un piso de tres habitaciones",
                   "se vive mucho fuera de casa"),
                  ("Bogotá", "unos 20 m²", "un apartamento pequeño",
                   "y en los barrios populares, menos"),
                  ("Cartagena", "unos 22 m²", "casa baja o apartamento",
                   "el patio cuenta como sala"),
                  ("Ciudad de México", "unos 18 m²", "un departamento",
                   "las distancias hacen el resto")],
        "marco": ["En … hay unos … metros cuadrados por persona.",
                  "Mi habitación está … y mide unos … metros.",
                  "En … la gente vive en …, y por eso …",
                  "La diferencia entre … y … es de … metros."],
    },
    "clave": [
        "Brussel tegenover Mexico-Stad is meer dan een verdubbeling: ongeveer 40 tegen 18 m² per "
        "persoon. Dat cijfer landt harder dan welke tekst ook.",
        "De opmerking bij Cartagena («el patio cuenta como sala») is het echte cultuurpunt: "
        "leefruimte is niet overal binnen. Wie dat oppikt, schrijft de beste derde zin.",
        "Let op «hay» tegenover «está»: «en Bogotá hay unos 20 m²» (bestaan/hoeveelheid) maar «mi "
        "habitación está arriba» (plaats). Verwarring hier is de meest voorkomende fout.",
        "Cijfers zijn ordes van grootte uit publieke woonstatistiek, geen exacte meting. Zeg dat "
        "erbij — de conclusie moet ook met een benadering kloppen.",
    ],
    "nota": "Vraag niet door naar de thuissituatie. Wie liever niet over zijn eigen kamer schrijft, "
            "neemt een kamer op school of een verzonnen kamer.",
}

P2_RETO_06 = {
    "id": "C6P-U2-RETO-06", "num": 6, "curso": "C6+", "unidad": P2,
    "seccion": "§1.4", "ancla": "casa_c6p", "soporte": "print",
    "nombre": "El cuarto sin objetos",
    "lente": "✍️ creatieve beperking", "forma": "👤 Solo", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Describe una habitación sin nombrar ni un solo mueble.",
    "gancho_nl": "Beschrijf een kamer zonder één meubel te noemen.",
    "consigna_es": "Escribe diez líneas usando solo luz, sonido, distancia y temperatura.",
    "consigna_nl": "Schrijf tien regels met alleen licht, geluid, afstand en temperatuur.",
    "regla": "Geen enkel voorwerp bij naam. Geen cama, geen mesa, geen ventana. Wél: waar het "
             "licht vandaan komt, wat je hoort, hoe ver iets is en of het er koud is.",
    "pasos": [("Cierra los ojos y piensa en una habitación real.",
               "Sluit je ogen en denk aan een echte kamer."),
              ("Apunta lo que se oye, no lo que se ve.",
               "Noteer wat je hoort, niet wat je ziet."),
              ("Escribe diez líneas, sin objetos.", "Schrijf tien regels, zonder voorwerpen."),
              ("Léela. ¿Adivinan qué habitación es?", "Lees voor. Raden ze welke kamer het is?")],
    "datos": {
        "permitido": ["la luz entra por…", "se oye…", "huele a…", "está a … pasos",
                      "hace frío / calor", "el suelo es duro / blando",
                      "el eco…", "desde fuera llega…", "aquí siempre está…"],
        "prohibido": ["la cama", "la mesa", "la silla", "el armario", "la ventana",
                      "la puerta", "la lámpara", "el sofá", "la tele"],
        "tipos": ["una cocina a las siete de la mañana", "un aula vacía a las cinco",
                  "un baño de una casa antigua", "una terraza en Cartagena a mediodía",
                  "el pasillo de un hospital"],
    },
    "clave": [
        "Het verbod op voorwerpen dwingt tot precies de taal die de unit oefent: plaatsbepalingen "
        "en «hay/está» zonder houvast van concrete zelfstandige naamwoorden.",
        "«La luz entra por…» is de zin die het lastigst is zonder «ventana» — leerlingen komen "
        "vanzelf uit op «por arriba», «desde la izquierda», «por una abertura». Dat is winst.",
        "Toets de tien regels en de nul voorwerpen. Eén meubel is één regel minder — hard, maar "
        "het is precies wat de opdracht meetbaar maakt.",
    ],
    "nota": "Lees er drie hardop voor zonder te zeggen welk soort kamer het is. Het raden is de "
            "bekroning, niet de oefening.",
}

P2_RETO_10 = {
    "id": "C6P-U2-RETO-10", "num": 10, "curso": "C6+", "unidad": P2,
    "seccion": "§4.4", "ancla": "pronombres_c6p2", "soporte": "print",
    "nombre": "Mudanza por etapas",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Os mudáis a un piso minúsculo. Solo caben diez cosas.",
    "gancho_nl": "Jullie verhuizen naar een piepklein appartement. Er passen maar tien dingen in.",
    "consigna_es": "Negociad las diez y hablad de ellas con pronombres, no con nombres.",
    "consigna_nl": "Onderhandel over de tien en praat erover met voornaamwoorden, niet met namen.",
    "regla": "Vanaf de tweede keer dat je iets noemt, gebruik je een pronomen: «la nevera → la "
             "llevamos». Wie het zelfstandig naamwoord blijft herhalen, verliest zijn beurt.",
    "pasos": [("Cada uno elige tres cosas de la lista.", "Elk kiest drie dingen uit de lijst."),
              ("Defended cada una en una frase.", "Verdedig elk in één zin."),
              ("A partir de la segunda mención: pronombre.",
               "Vanaf de tweede vermelding: voornaamwoord."),
              ("Negociad hasta llegar a diez exactas.", "Onderhandel tot je op precies tien zit."),
              ("Y ahora, ¿qué dejáis? Una frase por cosa.",
               "En wat laten jullie achter? Eén zin per ding.")],
    "datos": {
        "objetos": ["la nevera", "el sofá", "la mesa", "las sillas", "la cama",
                    "el armario", "la lavadora", "el escritorio", "la tele",
                    "la estantería", "las plantas", "la bici", "los libros",
                    "el microondas", "la alfombra", "las lámparas"],
        "marco": ["Yo me llevo … porque …", "¿La llevamos o la dejamos?",
                  "Los dejamos: no caben.", "Sin ella no se puede vivir.",
                  "Lo cambiamos por …", "Vale, la llevamos, pero entonces …"],
        "espacio": "Treinta metros cuadrados. Una habitación, una cocina pequeña y un baño.",
    },
    "clave": [
        "De pronomen-regel is de hele didactiek: zodra het voorwerp bekend is, moet het "
        "verdwijnen uit de zin. «¿La llevamos?» dwingt tot geslacht én getal in één beslissing.",
        "«Los libros → los dejamos» tegenover «la bici → la dejamos» is de plek waar de klas "
        "struikelt: meervoud en geslacht tegelijk.",
        "Er is geen juist lijstje. Wat telt is dat elke keuze verdedigd wordt en dat de "
        "voornaamwoorden kloppen — dat is objectief te horen.",
    ],
    "nota": "Werkt sterk na de leestekst over wonen in Cartagena: dertig vierkante meter is daar "
            "geen studentikoze uitzondering maar een gewoon gezinsappartement.",
}

P2_RETO_03 = {
    "id": "C6P-U2-RETO-03", "num": 3, "curso": "C6+", "unidad": P2,
    "seccion": "§3.4", "ancla": "gerundio_c6p", "soporte": "hub",
    "nombre": "La videollamada sospechosa",
    "lente": "🎭 simulatie met beperking", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Ves la habitación pero no a la persona. ¿Qué está pasando ahí?",
    "gancho_nl": "Je ziet de kamer maar niet de persoon. Wat gebeurt daar?",
    "consigna_es": "Graba tu descripción: qué se ve, qué se oye, qué está haciendo alguien.",
    "consigna_nl": "Neem je beschrijving op: wat je ziet, wat je hoort, wat iemand aan het doen is.",
    "regla": "Minstens vijf zinnen met estar + gerundio, en geen enkele met «creo que». Je "
             "beschrijft wat er gebeurt, je speculeert niet — dat komt pas op het einde.",
    "pasos": [("Escucha el modelo.", "Luister naar het model."),
              ("Describe lo que se ve y lo que se oye.",
               "Beschrijf wat je ziet en wat je hoort."),
              ("Cinco frases con estar + gerundio.", "Vijf zinnen met estar + gerundio."),
              ("Solo al final: una hipótesis.", "Pas op het einde: één hypothese.")],
    "datos": {
        "marco": ["En la pantalla se ve …", "Alguien está … , pero no lo veo.",
                  "Se oye a alguien que está …", "La luz viene de …",
                  "Al fondo hay … y encima está …",
                  "Y al final, mi hipótesis: creo que están …"],
        "gerundios": ["cocinando", "hablando", "estudiando", "buscando algo", "discutiendo",
                      "moviendo muebles", "escuchando música", "esperando a alguien"],
    },
    "clave": [
        "Het uitstel van «creo que» is de hele oefening: eerst waarnemen, dan pas interpreteren. "
        "Dat onderscheid tussen observatie en hypothese is een denkvaardigheid, geen taalregel — "
        "maar hij wordt hier taalkundig afdwingbaar.",
        "Onregelmatige gerundios («durmiendo», «diciendo», «leyendo») komen bijna altijd voor. "
        "Noteer welke de klas zelf produceert; die zijn geleerd, niet gedrild.",
        "Beoordeel de vijf gerundio's en de ene hypothese aan het eind. Zes hypotheses is de "
        "reto niet gedaan.",
    ],
    "nota": "Werkt ook zonder scherm: de leerkracht beschrijft een scène en de klas neemt op wat "
            "er volgens hen gebeurt.",
}

P2_RETO_07 = {
    "id": "C6P-U2-RETO-07", "num": 7, "curso": "C6+", "unidad": P2,
    "seccion": "§5.4", "ancla": "barrio_c6p", "soporte": "hub",
    "nombre": "Ruidos de vecinos",
    "lente": "🕵️ forensisch", "forma": "👤 Solo", "skill": "👂 Escuchar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Un edificio de cinco pisos y seis ruidos. ¿Quién, qué y en qué planta?",
    "gancho_nl": "Een gebouw van vijf verdiepingen en zes geluiden. Wie, wat en op welke verdieping?",
    "consigna_es": "Elige qué está pasando y en qué planta.",
    "consigna_nl": "Kies wat er gebeurt en op welke verdieping.",
    "regla": "Je antwoordt met estar + gerundio én met het rangtelwoord van de verdieping. En "
             "let op de apócope: «el tercer piso», niet «el tercero piso».",
    "pasos": [("Escucha el ruido entero.", "Luister het geluid helemaal af."),
              ("Piensa: ¿arriba o abajo? El sonido lo dice.",
               "Denk na: boven of beneden? Het geluid verraadt het."),
              ("Elige la acción y la planta.", "Kies de handeling en de verdieping.")],
    "datos": {
        "items": [
            ("Un golpe seco y luego algo que rueda, justo encima de tu cabeza.",
             "Alguien está moviendo muebles en el cuarto piso.",
             ["Alguien está moviendo muebles en el cuarto piso.",
              "Alguien está bajando la basura en el primer piso.",
              "Alguien está jugando en la calle."],
             "«justo encima» plus jouw derde verdieping geeft de vierde"),
            ("Música con mucho bajo que llega por el suelo, no por las paredes.",
             "Alguien está escuchando música en el segundo piso.",
             ["Alguien está escuchando música en el segundo piso.",
              "Alguien está escuchando música en el cuarto piso.",
              "Hay una fiesta en la terraza."],
             "bas door de vloer betekent van beneden, dus onder jou"),
            ("Un motor que arranca y una puerta metálica que sube.",
             "Alguien está sacando el coche del garaje.",
             ["Alguien está sacando el coche del garaje.",
              "Alguien está usando la lavadora en el primer piso.",
              "Alguien está subiendo en el ascensor."],
             "de metalen poort is de garage, dus onder de begane grond"),
            ("Voces que suben por el hueco de la escalera, cada vez más cerca.",
             "Alguien está subiendo por la escalera.",
             ["Alguien está subiendo por la escalera.",
              "Alguien está hablando en el quinto piso.",
              "Alguien está esperando el ascensor."],
             "«cada vez más cerca» is beweging, geen vaste plek"),
            ("Agua que corre en la pared, empieza y para tres veces.",
             "Alguien está fregando los platos en el piso de al lado.",
             ["Alguien está fregando los platos en el piso de al lado.",
              "Alguien está duchándose arriba.",
              "Está lloviendo."],
             "starten en stoppen hoort bij de afwas; een douche loopt door"),
            ("Un timbre, pasos rápidos y una puerta que se cierra en la planta baja.",
             "Alguien está recibiendo un paquete en la planta baja.",
             ["Alguien está recibiendo un paquete en la planta baja.",
              "Alguien está saliendo al patio.",
              "Alguien está llamando al ascensor."],
             "bel plus snelle stappen plus deur: een levering"),
        ],
    },
    "clave": [
        "Drie geluiden verraden de richting: van boven (klap door het plafond), van beneden (bas "
        "door de vloer) en van opzij (water in de muur). Dat onderscheid is de kern.",
        "Twee items hebben géén verdieping: de trap (beweging) en de garage (onder de grond). "
        "Wie overal een rangtelwoord bij plakt, valt daar door de mand.",
        "«El primer piso» in Spanje is niet de begane grond: «la planta baja» is gelijkvloers en "
        "«el primero» is er één hoger. Dat verschil met het Nederlands is een echte valstrik.",
    ],
    "nota": "Zolang er nog geen opnames zijn, leest de leerkracht de omschrijving voor of maakt "
            "het geluid zelf — de deductie werkt ook dan.",
}

P2_RETO_08 = {
    "id": "C6P-U2-RETO-08", "num": 8, "curso": "C6+", "unidad": P2,
    "seccion": "Cultura", "ancla": "cultura_c6p2", "soporte": "hub",
    "nombre": "Casa cartagenera, casa flamenca",
    "lente": "🤝 bemiddelen", "forma": "👥 En parejas", "skill": "🔀 Bemiddelen",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "¿Por qué las casas flamencas son tan estrechas? Explícaselo a Valen.",
    "gancho_nl": "Waarom zijn Vlaamse huizen zo smal? Leg het uit aan Valen.",
    "consigna_es": "Elige la explicación que Valen entiende de verdad.",
    "consigna_nl": "Kies de uitleg die Valen écht zou begrijpen.",
    "regla": "Je legt uit, je vertaalt niet. Geen Nederlandse woorden, en geen uitleg die "
             "veronderstelt dat de ander al weet hoe een Vlaams huis eruitziet.",
    "pasos": [("Lee lo que Valen no entiende.", "Lees wat Valen niet begrijpt."),
              ("Elige la mejor explicación.", "Kies de beste uitleg."),
              ("Fíjate: la más corta no siempre es la más clara.",
               "Let op: de kortste is niet altijd de duidelijkste.")],
    "datos": {
        "items": [
            ("Valen: «¿Por qué las casas son tan estrechas y tan altas?»",
             "Antes se pagaba impuesto por lo ancho de la fachada, y por eso se construía "
             "estrecho y alto.",
             ["Antes se pagaba impuesto por lo ancho de la fachada, y por eso se construía "
              "estrecho y alto.",
              "Porque hace frío.",
              "Es la tradición flamenca."],
             "«es la tradición» legt niets uit; de belastingreden is concreet en te snappen"),
            ("Valen: «¿Y dónde está el patio? Aquí todas las casas tienen patio.»",
             "En vez de patio hay un jardín detrás, y muchos días hace demasiado frío para "
             "estar fuera.",
             ["En vez de patio hay un jardín detrás, y muchos días hace demasiado frío para "
              "estar fuera.",
              "No hay patio.",
              "El patio está dentro."],
             "je vervangt het begrip door zijn equivalent, plus de reden waarom het anders werkt"),
            ("Valen: «¿La gente vive en la calle o dentro?»",
             "Aquí se vive más dentro: en invierno oscurece a las cinco y llueve mucho.",
             ["Aquí se vive más dentro: en invierno oscurece a las cinco y llueve mucho.",
              "Dentro, siempre.",
              "Depende de la persona."],
             "je geeft de reden, niet alleen het antwoord — dat is bemiddelen"),
            ("Valen: «¿Y por qué las ventanas son tan grandes si hace frío?»",
             "Justo por eso: hay poca luz, y las ventanas grandes dejan entrar la que hay.",
             ["Justo por eso: hay poca luz, y las ventanas grandes dejan entrar la que hay.",
              "Para ver la calle.",
              "No sé, siempre han sido así."],
             "de tegenintuïtieve reden is de juiste, en die moet je durven uitleggen"),
        ],
    },
    "clave": [
        "Alle vier de juiste antwoorden hebben dezelfde vorm: verschijnsel plus reden. De foute "
        "antwoorden zijn niet onwaar, ze zijn onvolledig — dat is het lastigste om te zien.",
        "«En vez de» is de sleutelchunk van bemiddelen: je vervangt een begrip dat de ander wél "
        "kent door zijn equivalent.",
        "Het vierde item is tegenintuïtief: grote ramen ondanks de kou, júist vanwege het weinige "
        "licht. Wie dat uitlegt, bemiddelt echt tussen twee leefwerelden.",
    ],
    "nota": "Draai het om als afsluiter: laat de klas vragen bedenken die Valen over Cartagena "
            "zou moeten beantwoorden. Bemiddelen gaat twee richtingen uit.",
}

P2_RETO_02 = {
    "id": "C6P-U2-RETO-02", "num": 2, "curso": "C6+", "unidad": P2,
    "seccion": "§1.4", "ancla": "casa_c6p", "soporte": "ppt",
    "nombre": "Airbnb honesto",
    "lente": "✍️ creatieve beperking", "forma": "👥 En parejas", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Todos los defectos tienen que salir. Y aún así hay que alquilarlo.",
    "gancho_nl": "Alle gebreken moeten erin. En tóch moet het verhuurd raken.",
    "consigna_es": "Escribid el anuncio con los seis defectos incluidos y sin mentir.",
    "consigna_nl": "Schrijf de advertentie met de zes gebreken erin, en zonder te liegen.",
    "regla": "Alle zes de gebreken staan erin, letterlijk. Je mag ze omkaderen maar niet "
             "weglaten, en je mag niets verzinnen dat er niet is.",
    "pasos": [("Leed el piso y sus seis defectos.", "Lees het appartement en zijn zes gebreken."),
              ("Buscad para cada defecto su lado bueno.",
               "Zoek bij elk gebrek de goede kant."),
              ("Escribid el anuncio: ocho frases.", "Schrijf de advertentie: acht zinnen."),
              ("La clase vota: ¿lo alquilan o no?", "De klas stemt: huren ze het of niet?")],
    "datos": {
        "piso": [("dónde", "en el centro, a dos minutos de la plaza"),
                 ("tamaño", "35 m², una habitación"),
                 ("precio", "450 € al mes")],
        "defectos": ["está en un cuarto piso y no hay ascensor",
                     "la ventana da a un patio interior: hay poca luz",
                     "el bar de abajo cierra a las dos de la mañana",
                     "no hay lavadora",
                     "la cocina está dentro del salón",
                     "las paredes son muy finas"],
        "marco": ["Se alquila … en …", "Es pequeño, pero …",
                  "No tiene …, aunque …", "Está en …, así que …",
                  "Ideal para quien …", "Lo mejor: …"],
    },
    "clave": [
        "De opdracht traint precies wat het leerplan «functioneel taalgebruik» noemt: dezelfde "
        "waarheid anders kaderen zonder te liegen. «No hay ascensor» wordt «un cuarto piso sin "
        "ascensor: subes las escaleras y ya has hecho deporte».",
        "«Aunque» en «así que» zijn de twee conectoren die het werk doen. Wie er geen enkele "
        "gebruikt, heeft een lijst geschreven, geen advertentie.",
        "De stemming aan het eind is de toets: als niemand het zou huren, is het te eerlijk "
        "geworden; als iedereen het zou huren, is er iets weggemoffeld. Kijk na welk gebrek.",
    ],
    "nota": "Vergelijk met een echte advertentie op het scherm. De klas ziet meteen welke "
            "gebreken daar níet in staan — en dat is het beste gesprek van de les.",
}

P2_RETO_05 = {
    "id": "C6P-U2-RETO-05", "num": 5, "curso": "C6+", "unidad": P2,
    "seccion": "§2.4", "ancla": "hay_estar_c6p", "soporte": "ppt",
    "nombre": "Reforma con 500 €",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 18 min", "dificultad": "★★★",
    "gancho_es": "Quinientos euros, una habitación fea y cuatro opiniones.",
    "gancho_nl": "Vijfhonderd euro, een lelijke kamer en vier meningen.",
    "consigna_es": "Decidid qué compráis y decid exactamente dónde va cada cosa.",
    "consigna_nl": "Beslis wat jullie kopen en zeg exact waar elk ding komt.",
    "regla": "Vijfhonderd euro, geen cent meer. En elke aankoop wordt verdedigd met een "
             "plaatsbepaling: «la estantería, encima del escritorio, porque…». Zonder plaats "
             "telt het voorstel niet.",
    "pasos": [("Mirad la habitación y la lista de precios.",
               "Bekijk de kamer en de prijslijst."),
              ("Cada uno propone dos cosas, con su sitio.",
               "Elk stelt twee dingen voor, met hun plaats."),
              ("Negociad hasta los 500 €.", "Onderhandel tot aan de 500 €."),
              ("Presentad la habitación nueva a la clase.",
               "Presenteer de nieuwe kamer aan de klas.")],
    "datos": {
        "habitacion": "Doce metros cuadrados. Paredes blancas, una ventana pequeña, "
                      "una cama y nada más.",
        "precios": [("una estantería", 60), ("un escritorio", 120), ("una silla de escritorio", 90),
                    ("una lámpara de pie", 45), ("una alfombra", 55), ("cortinas", 35),
                    ("pintura para una pared", 40), ("un espejo grande", 70),
                    ("plantas", 25), ("un armario pequeño", 150),
                    ("una mesita de noche", 40), ("cuadros o pósters", 20)],
        "marco": ["Yo pongo …", "Ponemos … encima de … porque …",
                  "Debajo de la ventana no cabe …",
                  "Sin … la habitación sigue igual.",
                  "Nos quedan … euros. ¿Qué hacemos?"],
    },
    "clave": [
        "De kamer is twaalf vierkante meter: de kast van 150 € vreet bijna een derde van het "
        "budget én de ruimte. Elke groep botst op die keuze.",
        "De plaatsbepaling is de taalopdracht; het budget is alleen de motor. Toets of elk "
        "voorstel een voorzetsel bevat.",
        "De vorm die op de tong ligt («yo pondría») is condicional en hoort niet in dit leerplan. "
        "Het marco geeft daarom «yo pongo»; «propongo poner» werkt even goed.",
    ],
    "nota": "Werk met echte prijzen van een echte winkel als je die bij de hand hebt. Het verschil "
            "in ernst is meteen hoorbaar.",
}

P2_RETO_09 = {
    "id": "C6P-U2-RETO-09", "num": 9, "curso": "C6+", "unidad": P2,
    "seccion": "§5.4", "ancla": "barrio_c6p", "soporte": "ppt",
    "nombre": "Tour de 40 segundos",
    "lente": "📻 mediaformat", "forma": "👤 Solo", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Cuarenta segundos, una sola toma, toda la casa.",
    "gancho_nl": "Veertig seconden, één take, het hele huis.",
    "consigna_es": "Haz el recorrido hablando: seis preposiciones y tres gerundios, sin parar.",
    "consigna_nl": "Doe de rondgang al pratend: zes voorzetsels en drie gerundio's, zonder te stoppen.",
    "regla": "Eén doorlopende take van veertig seconden. Stoppen mag niet, herbeginnen wel — maar "
             "dan vanaf nul. Zes verschillende voorzetsels en drie gerundio's.",
    "pasos": [("Planifica la ruta: de la puerta al último sitio.",
               "Plan de route: van de deur tot de laatste plek."),
              ("Escribe las seis preposiciones que vas a usar.",
               "Schrijf de zes voorzetsels op die je gaat gebruiken."),
              ("Graba de una vez, sin cortes.", "Neem in één keer op, zonder knippen."),
              ("¿Cuarenta segundos? ¿Seis y tres? Si no, otra vez.",
               "Veertig seconden? Zes en drie? Zo niet: opnieuw.")],
    "datos": {
        "preposiciones": ["al lado de", "enfrente de", "detrás de", "debajo de",
                          "encima de", "entre", "al final de", "a la derecha de"],
        "gerundios": ["entrando", "pasando", "subiendo", "girando", "saliendo", "llegando"],
        "marco": ["Empezamos aquí, entrando por …",
                  "A la derecha de … está …",
                  "Pasando por el pasillo llegamos a …",
                  "Entre … y … hay …",
                  "Y al final, saliendo a …, se ve …"],
    },
    "clave": [
        "De combinatie is de moeilijkheid: gerundio's om de beweging te dragen («pasando», "
        "«subiendo») en voorzetsels om de plaatsen vast te zetten. In één take betekent dat "
        "vooruit denken terwijl je praat.",
        "Veertig seconden is bewust krap: het dwingt tot een route in plaats van een opsomming.",
        "Wie zijn eigen huis niet wil filmen, doet de school, een verzonnen huis of alleen de "
        "audio. Beoordeeld wordt de taal, niet het beeld.",
    ],
    "nota": "Zonder camera werkt het even goed: ogen dicht en de rondgang alleen in woorden. "
            "Sommige leerlingen leveren dan hun beste Spaans.",
}

RETOS_C6P_U2 = [P2_RETO_01, P2_RETO_02, P2_RETO_03, P2_RETO_04, P2_RETO_05,
                P2_RETO_06, P2_RETO_07, P2_RETO_08, P2_RETO_09, P2_RETO_10]


# ═══════════════════════════════════════════════════════════════════════════
# C6+ · U3 «Conectados» — parada CDMX, gastheer Diego
# ═══════════════════════════════════════════════════════════════════════════
P3 = 3

P3_RETO_01 = {
    "id": "C6P-U3-RETO-01", "num": 1, "curso": "C6+", "unidad": P3,
    "seccion": "§3.4", "ancla": "oi_c6p", "soporte": "print",
    "nombre": "El hilo que se descontrola",
    "lente": "🕵️ forensisch", "forma": "👥 En parejas", "skill": "👁️ Leer",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Catorce mensajes en el grupo. Y nadie sabe ya quién le contestó a quién.",
    "gancho_nl": "Veertien berichten in de groep. En niemand weet nog wie aan wie antwoordde.",
    "consigna_es": "Reconstruye el hilo: quién le dice qué a quién, con le o les.",
    "consigna_nl": "Reconstrueer de draad: wie zegt wat tegen wie, met le of les.",
    "regla": "Elke reconstructie gebruikt «le» of «les» — en je moet kunnen aanwijzen waaruit "
             "blijkt wie de ontvanger is. Eén bericht is aan de héle groep gericht; dat wordt «les».",
    "pasos": [("Leed los catorce mensajes en orden.", "Lees de veertien berichten op volgorde."),
              ("Marcad a quién va dirigido cada uno.", "Markeer aan wie elk bericht gericht is."),
              ("Escribid siete frases con le o les.", "Schrijf zeven zinnen met le of les."),
              ("¿Dónde empezó el malentendido?", "Waar begon het misverstand?")],
    "datos": {
        # (afzender, bericht, aan wie)
        "hilo": [
            ("Diego", "Mañana a las seis en la cancha, ¿va?", "todos"),
            ("Camila", "Yo no puedo antes de las siete.", "Diego"),
            ("Andrés", "¿A las seis o a las siete? 😅", "todos"),
            ("Valen", "Yo le dije a Camila que llegábamos tarde.", "Andrés"),
            ("Diego", "Camila, ¿te va bien a las siete?", "Camila"),
            ("Camila", "Sí, perfecto.", "Diego"),
            ("Andrés", "Entonces ¿a las siete?", "todos"),
            ("Valen", "Yo llevo el balón.", "todos"),
            ("Diego", "Andrés, tú traes agua.", "Andrés"),
            ("Andrés", "Vale, pero ¿a qué hora?", "Diego"),
            ("Camila", "A las siete, ya lo dijimos tres veces 😭", "Andrés"),
            ("Valen", "Perdón, yo entendí seis.", "todos"),
            ("Diego", "Les repito: SIETE.", "todos"),
            ("Andrés", "Ahora sí. Nos vemos.", "todos"),
        ],
        "marco": ["Diego les dice a todos que …", "Camila le contesta a … que …",
                  "Valen le explica a … que …", "Andrés les pregunta … a …",
                  "El malentendido empieza cuando … le …"],
    },
    "clave": [
        "Zeven berichten zijn aan één persoon gericht (le), zeven aan de groep (les). De tekst "
        "verraadt het telkens: een naam in de aanhef, of «les repito».",
        "Het misverstand begint bij bericht 4: Valen antwoordt Andrés over wat zíj tegen Camila "
        "zei — een derde persoon in een tweede gesprek. Daar loopt de draad vast.",
        "«Yo le dije a Camila» is de zin die het dubbele gebruik toont: het pronomen «le» stáát er "
        "al én de ontvanger wordt herhaald met «a Camila». Dat is correct Spaans en verrast bijna "
        "elke Nederlandstalige.",
        "Toets de zeven zinnen op le/les én op die verdubbeling. Wie «dije a Camila» schrijft "
        "zonder «le», heeft de kern gemist.",
    ],
    "nota": "Het bericht met het huilende emoji is bewust het enige met gevoel: laat de klas zien "
            "dat de frustratie in de draad zelf te lezen is.",
}

P3_RETO_05 = {
    "id": "C6P-U3-RETO-05", "num": 5, "curso": "C6+", "unidad": P3,
    "seccion": "§1.4", "ancla": "movil_c6p", "soporte": "print",
    "nombre": "Mensajes sin emoji",
    "lente": "✍️ creatieve beperking", "forma": "👤 Solo", "skill": "✍️ Escribir",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Quita los emojis y el mensaje ya no significa nada. Escríbelo otra vez.",
    "gancho_nl": "Haal de emoji weg en het bericht betekent niets meer. Schrijf het opnieuw.",
    "consigna_es": "Reescribe los cinco mensajes en palabras, sin perder el tono.",
    "consigna_nl": "Herschrijf de vijf berichten in woorden, zonder de toon te verliezen.",
    "regla": "Nul emoji, nul hoofdletters om te schreeuwen, nul uitroeptekens-in-rijtjes. Alleen "
             "woorden — en de ontvanger moet dezelfde toon aanvoelen als in het origineel.",
    "pasos": [("Lee el mensaje con sus emojis.", "Lees het bericht met zijn emoji's."),
              ("Di en una palabra qué tono tiene.", "Zeg in één woord welke toon het heeft."),
              ("Reescríbelo en palabras.", "Herschrijf het in woorden."),
              ("Compara: ¿se entiende igual?", "Vergelijk: begrijp je het even goed?")],
    "datos": {
        # (bericht met emoji, toon, waar het om draait)
        "mensajes": [
            ("Vale 🙄", "resignatie met ergernis", "«vale» alleen klinkt neutraal; het oogrollen doet het werk"),
            ("Sí, claro 😂😂😂", "sarcasme", "zonder emoji lees je het als instemming — precies omgekeerd"),
            ("¿Vienes? 👀", "nieuwsgierig aandringen", "de ogen maken van een vraag een por-favor"),
            ("Ya te dije 🤷", "ik geef het op", "de schouderophaal zegt: ik herhaal het niet nog eens"),
            ("Buenísimo 🔥🔥", "enthousiasme", "de vlammen versterken; zonder hen klinkt het beleefd"),
        ],
        "banco": ["la verdad es que…", "no me apetece mucho, pero…", "lo digo en serio",
                  "te lo digo otra vez, porque…", "me hace mucha ilusión",
                  "no pasa nada, de verdad", "es broma", "lo digo de broma, ¿eh?"],
        "marco": ["Tono: …", "En palabras: …", "Lo que se pierde sin emoji es …"],
    },
    "clave": [
        "«Sí, claro 😂😂😂» is de belangrijkste: zonder emoji betekent hij het tegenovergestelde. "
        "Dat maakt zichtbaar dat toon informatie is, niet versiering.",
        "De bank bevat «es broma» en «lo digo en serio»: precies de expliciete markeerders die "
        "het Spaans gebruikt waar wij een emoji zetten.",
        "Toets of de toon overkomt, niet of de vertaling letterlijk is. Vraag een klasgenoot om "
        "de toon te benoemen zonder het origineel gezien te hebben — dat is de echte test.",
    ],
    "nota": "Sluit aan bij digitale geletterdheid: dezelfde tekst zonder emoji naar een leerkracht "
            "of een werkgever sturen is een vaardigheid, geen taalspelletje.",
}

P3_RETO_07 = {
    "id": "C6P-U3-RETO-07", "num": 7, "curso": "C6+", "unidad": P3,
    "seccion": "§4.4", "ancla": "acabar_c6p", "soporte": "print",
    "nombre": "Acabo de… y ahora voy a…",
    "lente": "🎭 simulatie met beperking", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Doce fotos de medio segundo. ¿Qué acaba de pasar y qué va a pasar?",
    "gancho_nl": "Twaalf foto's van een halve seconde. Wat is er net gebeurd en wat gaat er gebeuren?",
    "consigna_es": "Por cada escena: una frase con acabar de y otra con ir a.",
    "consigna_nl": "Per scène: één zin met acabar de en één met ir a.",
    "regla": "Altijd twee zinnen, altijd in die volgorde: eerst wat net gebeurd is, dan wat gaat "
             "komen. En het presente is verboden — die scène zíe je al.",
    "pasos": [("Mirad la escena.", "Bekijk de scène."),
              ("Uno dice qué acaba de pasar.", "De ene zegt wat er net gebeurd is."),
              ("El otro dice qué va a pasar.", "De andere zegt wat er gaat gebeuren."),
              ("Cambiad de papel en la escena siguiente.",
               "Wissel van rol bij de volgende scène.")],
    "datos": {
        # (scène, wat er net gebeurde, wat er gaat gebeuren)
        "escenas": [
            ("Un vaso en el aire, a diez centímetros del suelo.",
             "se le acaba de caer", "va a romperse"),
            ("Alguien con la boca abierta delante de una pantalla.",
             "acaba de leer algo", "va a contárselo a alguien"),
            ("Una puerta entreabierta y una maleta en el pasillo.",
             "acaba de llegar", "va a deshacer la maleta"),
            ("Un móvil con el 1 % de batería.",
             "acaba de avisar", "se va a apagar"),
            ("Dos personas de espaldas, una con el brazo levantado.",
             "acaba de despedirse", "va a irse"),
            ("Un plato vacío y un tenedor en la mesa.",
             "acaba de comer", "va a fregar"),
            ("Una bici en el suelo y una rueda girando todavía.",
             "acaba de caerse", "va a levantarse"),
            ("Una pantalla con «Enviado» y un dedo aún en el aire.",
             "acaba de mandar un mensaje", "va a esperar la respuesta"),
            ("Un paraguas cerrado y el suelo mojado.",
             "acaba de dejar de llover", "va a salir sin paraguas"),
            ("Alguien mirando el reloj en una parada vacía.",
             "acaba de perder el bus", "va a llegar tarde"),
            ("Un cuaderno abierto en una página en blanco y un boli en la mano.",
             "acaba de sentarse", "va a empezar"),
            ("Dos manos aplaudiendo y una persona de pie delante de la clase.",
             "acaba de terminar", "va a sentarse"),
        ],
        "marco": ["Acaba de … , se nota porque …", "Y ahora va a …",
                  "Se le acaba de …", "Dentro de un segundo va a …"],
    },
    "clave": [
        "«Se le acaba de caer» is de vorm die iedereen wil vermijden en die je juist moet oefenen: "
        "het onvrijwillige «se» plus het meewerkend voornaamwoord. Scène 1 en 7 lokken hem uit.",
        "Scène 9 («acaba de dejar de llover») stapelt twee perifrasen: acabar de plus dejar de. "
        "Dat is aanzet-B1-niveau en het mooiste wat deze reto kan opleveren.",
        "Toets de twee zinnen per scène en het verbod op het presente. Wie «hay un vaso en el "
        "aire» zegt, beschrijft in plaats van te concluderen.",
    ],
    "nota": "De twaalf scènes staan in woorden zodat de reto ook werkt zonder beeld; met eigen "
            "foto's erbij wordt hij sterker, maar hij hoeft ze niet.",
}

P3_RETO_10 = {
    "id": "C6P-U3-RETO-10", "num": 10, "curso": "C6+", "unidad": P3,
    "seccion": "Cultura", "ancla": "cultura_c6p3", "soporte": "print",
    "nombre": "La notificación falsa",
    "lente": "🕵️ forensisch", "forma": "👥 En parejas", "skill": "✍️ Escribir",
    "tiempo": "± 18 min", "dificultad": "★★★",
    "gancho_es": "Escribid el mensaje que engaña. Y después, el que lo desmonta.",
    "gancho_nl": "Schrijf het bericht dat misleidt. En daarna het bericht dat het ontmaskert.",
    "consigna_es": "Escribid los dos mensajes y marcad las cinco señales de alarma.",
    "consigna_nl": "Schrijf beide berichten en markeer de vijf alarmsignalen.",
    "regla": "Geen echte merknamen, geen echte links, geen echte telefoonnummers. Het valse "
             "bericht is een oefenmodel, geen werkend lokaas — en het tweede bericht moet elk "
             "van de vijf signalen bij naam noemen.",
    "pasos": [("Leed las cinco señales de alarma.", "Lees de vijf alarmsignalen."),
              ("Escribid el mensaje falso con las cinco dentro.",
               "Schrijf het valse bericht met de vijf erin."),
              ("Intercambiad con otra pareja.", "Wissel met een ander duo."),
              ("Escribid el mensaje que lo desmonta, señal por señal.",
               "Schrijf het ontmaskerende bericht, signaal per signaal.")],
    "datos": {
        "senales": [("la urgencia", "«tienes veinticuatro horas» — la prisa impide pensar"),
                    ("el premio inesperado", "nadie regala nada a quien no ha participado"),
                    ("los datos personales", "ningún banco los pide por mensaje"),
                    ("la dirección rara", "una letra cambiada en el nombre"),
                    ("los errores de lengua", "traducción automática, tildes que faltan")],
        "marco_falso": ["Estimado cliente: …", "Su cuenta va a …",
                        "Haga clic aquí antes de …", "Necesitamos confirmar …",
                        "Si no responde, …"],
        "marco_aviso": ["Ojo con este mensaje: …", "Primero, te pide … , y eso no lo hace nadie.",
                        "Además, dice … , pero …", "Fíjate en …",
                        "Lo que hay que hacer es … , y nunca …"],
    },
    "clave": [
        "De vijf signalen zijn precies de vijf die de politie ook noemt: urgentie, onverwachte "
        "prijs, gegevensvraag, vreemd adres, taalfouten. De reto is dus echte digitale "
        "geletterdheid, in het Spaans.",
        "Het valse bericht gebruikt vanzelf usted-vormen en de imperativo («haga clic»); het "
        "waarschuwende bericht staat in tú. Dat registercontrast is de grammaticale winst.",
        "Toets het tweede bericht: alle vijf de signalen bij naam. Het eerste bericht is alleen "
        "het materiaal.",
        "Laat geen echte merknamen of links toe, ook niet als grap. Een oefenmodel dat buiten de "
        "klas belandt, is geen oefenmodel meer.",
    ],
    "nota": "Werkt goed samen met de mediawijsheidsles: dezelfde inhoud, maar in het Spaans "
            "geformuleerd, blijft aantoonbaar beter hangen.",
}

P3_RETO_04 = {
    "id": "C6P-U3-RETO-04", "num": 4, "curso": "C6+", "unidad": P3,
    "seccion": "§1.4", "ancla": "movil_c6p", "soporte": "hub",
    "nombre": "Tiempo de pantalla real",
    "lente": "🔬 onderzoek & data", "forma": "🏫 Toda la clase", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★☆",
    "gancho_es": "Tu móvil ya lo sabe. Ahora lo sabe la clase — pero sin nombres.",
    "gancho_nl": "Je gsm weet het al. Nu weet de klas het ook — maar zonder namen.",
    "consigna_es": "Elige qué conclusión se puede sacar de verdad de cada dato.",
    "consigna_nl": "Kies welke conclusie je echt uit elk cijfer kunt trekken.",
    "regla": "Alles anoniem. En je conclusie mag niet verder gaan dan het cijfer: uit een "
             "gemiddelde volgt geen uitspraak over één persoon.",
    "pasos": [("Cada uno mira su tiempo de pantalla y lo apunta en anónimo.",
               "Iedereen bekijkt zijn schermtijd en noteert die anoniem."),
              ("La clase hace el gráfico.", "De klas maakt de grafiek."),
              ("Elegid qué se puede concluir y qué no.",
               "Kies wat je wél en niet kunt concluderen.")],
    "datos": {
        "items": [
            ("La media de la clase es de 5 horas al día.",
             "La mitad de la clase pasa más de cinco horas y la otra mitad menos… o no.",
             ["La mitad de la clase pasa más de cinco horas y la otra mitad menos… o no.",
              "Todos pasan cinco horas al día.",
              "Nadie pasa más de cinco horas."],
             "een gemiddelde zegt niets over de verdeling — dat is de valstrik van elk gemiddelde"),
            ("El día con más uso es el domingo.",
             "El domingo se usa más el móvil que los otros días.",
             ["El domingo se usa más el móvil que los otros días.",
              "El domingo la gente está más aburrida.",
              "El domingo nadie estudia."],
             "de reden staat niet in de data; de conclusie mag niet verder gaan dan het cijfer"),
            ("Tres personas pasan más de ocho horas.",
             "Hay tres casos muy por encima de la media.",
             ["Hay tres casos muy por encima de la media.",
              "Tres personas son adictas.",
              "La mayoría pasa ocho horas."],
             "«adicto» is een diagnose, geen conclusie uit een cijfer"),
            ("El 70 % dice que quiere bajar su tiempo de pantalla.",
             "La mayoría no está contenta con su tiempo de pantalla.",
             ["La mayoría no está contenta con su tiempo de pantalla.",
              "El 70 % va a bajar su tiempo de pantalla.",
              "El 30 % pasa poco tiempo."],
             "willen is niet gaan doen, en de andere 30 % zegt alleen dat ze niet willen minderen"),
        ],
    },
    "clave": [
        "De vier foute antwoorden zijn elk een ander type denkfout: het gemiddelde als norm, de "
        "reden verzinnen, een diagnose stellen, en intentie met gedrag verwarren.",
        "Het eerste item is het belangrijkste en het minst intuïtieve: uit een gemiddelde van vijf "
        "uur volgt niet dat de helft erboven zit. Laat de klas een tegenvoorbeeld bedenken.",
        "Toets de vier keuzes plus één eigen conclusie uit de echte klasgrafiek. Die laatste is "
        "waar de taal en het denken samenkomen.",
        "Houd het anoniem en vergelijk niemand. Wie zijn cijfer niet wil delen, doet niet mee aan "
        "de meting maar wel aan de conclusies.",
    ],
    "nota": "De grafiek van de eigen klas is altijd interessanter dan een cijfer uit een krant — "
            "en het is meteen een echte reden om Spaans te schrijven.",
}

P3_RETO_08 = {
    "id": "C6P-U3-RETO-08", "num": 8, "curso": "C6+", "unidad": P3,
    "seccion": "§4.4", "ancla": "acabar_c6p", "soporte": "hub",
    "nombre": "El podcast de dos opiniones",
    "lente": "📻 mediaformat", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Dos minutos, dos opiniones opuestas, y ni una sola voz alta.",
    "gancho_nl": "Twee minuten, twee tegengestelde meningen, en geen enkele verheven stem.",
    "consigna_es": "Grabad el debate sobre los móviles en clase. En desacuerdo, pero sin pelear.",
    "consigna_nl": "Neem het debat op over gsm's in de klas. Oneens, maar zonder ruzie.",
    "regla": "Je bent het écht oneens, en je onderbreekt nooit. Elke beurt begint met wat de "
             "ander gezegd heeft («entiendo que…», «tienes razón en que…») vóór je je eigen punt "
             "maakt.",
    "pasos": [("Repartid las posturas: a favor y en contra.",
               "Verdeel de standpunten: voor en tegen."),
              ("Cada uno escribe tres argumentos.", "Elk schrijft drie argumenten."),
              ("Grabad dos minutos, por turnos, sin interrumpir.",
               "Neem twee minuten op, om beurten, zonder onderbreken."),
              ("Escuchad: ¿se oye que os escucháis?",
               "Luister terug: hoor je dat jullie naar elkaar luisteren?")],
    "datos": {
        "posturas": [("a favor de los móviles en clase",
                      "sirven para buscar, traducir, grabar y organizarse"),
                     ("en contra",
                      "distraen, y el trabajo de grupo funciona peor con pantallas")],
        "marco": ["Entiendo que … , pero yo creo que …",
                  "Tienes razón en que … , aunque …",
                  "A mí me parece que … porque …",
                  "¿Y qué haces cuando …?",
                  "En eso estamos de acuerdo: …"],
        "prohibido": ["interrumpir", "subir la voz", "«eso es una tontería»",
                      "hablar más de treinta segundos seguidos"],
    },
    "clave": [
        "«Creo que» plus indicativo is precies wat deze unit aanbrengt en wat het leerplan "
        "toelaat: meningen zónder subjuntivo. Elke beurt levert er een.",
        "De verplichte opening («entiendo que…») is de bemiddelingsvaardigheid uit het leerplan: "
        "je moet de ander eerst correct samenvatten. Dat is moeilijker dan tegenspreken.",
        "De regel «geen beurt langer dan dertig seconden» dwingt vier beurten in twee minuten — "
        "dus echt gesprek in plaats van twee monologen.",
        "Toets de beurtwisseling en de openingszinnen, niet wie gelijk heeft.",
    ],
    "nota": "Laat de klas naar twee opnames luisteren en raden wie welk standpunt echt aanhangt. "
            "Meestal is dat niet te horen — en dat is precies het compliment.",
}

P3_RETO_09 = {
    "id": "C6P-U3-RETO-09", "num": 9, "curso": "C6+", "unidad": P3,
    "seccion": "§1.4", "ancla": "movil_c6p", "soporte": "hub",
    "nombre": "Términos que no se traducen",
    "lente": "🤝 bemiddelen", "forma": "👨‍👩‍👧 En grupos", "skill": "🔀 Bemiddelen",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "«Scrollear» existe. «Ghostear» también. Pero ¿es eso español?",
    "gancho_nl": "«Scrollear» bestaat. «Ghostear» ook. Maar is dat Spaans?",
    "consigna_es": "Elige el equivalente español que de verdad funciona.",
    "consigna_nl": "Kies het Spaanse equivalent dat echt werkt.",
    "regla": "Een equivalent telt alleen als een Spaanstalige het zou begrijpen zonder het "
             "Engelse woord te kennen. Mooi bedacht maar onbegrijpelijk is fout.",
    "pasos": [("Leed el término y lo que significa de verdad.",
               "Lees de term en wat hij echt betekent."),
              ("Elegid el equivalente que funciona.", "Kies het equivalent dat werkt."),
              ("Y decid por qué los otros no.", "En zeg waarom de andere niet werken.")],
    "datos": {
        "items": [
            ("scrollear — bajar por una pantalla sin buscar nada concreto",
             "deslizar (la pantalla)",
             ["deslizar (la pantalla)", "rodar", "bajar la computadora"],
             "«deslizar» bestaat al en wordt in heel LatAm zo gebruikt"),
            ("ghostear — dejar de contestar a alguien sin decir nada",
             "dejar en visto",
             ["dejar en visto", "hacer el fantasma", "desaparecer la persona"],
             "«dejar en visto» is de bestaande Spaanse uitdrukking en iedereen snapt hem"),
            ("postear — publicar algo en una red",
             "publicar",
             ["publicar", "postar", "poner un post"],
             "het gewone woord bestaat gewoon al; een leenwoord is hier niet nodig"),
            ("stalkear — mirar el perfil de alguien una y otra vez",
             "cotillear el perfil",
             ["cotillear el perfil", "acechar", "vigilar a alguien"],
             "«acechar» en «vigilar» klinken dreigend; «cotillear» treft de toon"),
            ("spoilear — contar el final de algo",
             "hacer un spoiler / destripar",
             ["hacer un spoiler / destripar", "arruinar", "contar el fin"],
             "«destripar» is het Spaanse woord dat er echt voor bestaat, naast het leenwoord"),
        ],
    },
    "clave": [
        "Twee van de vijf hebben een volwaardig Spaans woord dat al bestond («publicar», "
        "«destripar»); drie hebben een uitdrukking in plaats van een woord («dejar en visto»). "
        "Dat onderscheid is de eigenlijke ontdekking.",
        "«Acechar» tegenover «cotillear» is een register- en toonverschil, geen betekenisverschil. "
        "Precies daar is bemiddelen moeilijker dan vertalen.",
        "Er is geen academisch juist antwoord: talen lenen en dat is normaal. Toets de "
        "verantwoording, niet het woord.",
        "Sluit af met de omgekeerde vraag: welke Nederlandse woorden lenen wíj uit het Engels, en "
        "waarom stoort dat niemand?",
    ],
    "nota": "De Real Academia neemt sommige van deze woorden inmiddels op. Als een leerling dat "
            "aanhaalt: gelijk geven — een levende taal beslist door gebruik.",
}

P3_RETO_02 = {
    "id": "C6P-U3-RETO-02", "num": 2, "curso": "C6+", "unidad": P3,
    "seccion": "§2.4", "ancla": "ir_a_c6p", "soporte": "ppt",
    "nombre": "Detox de 24 horas",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 18 min", "dificultad": "★★★",
    "gancho_es": "Un día entero sin pantalla. Planificadlo hora por hora — y defendedlo.",
    "gancho_nl": "Een hele dag zonder scherm. Plan hem uur per uur — en verdedig hem.",
    "consigna_es": "Presentad el plan con voy a / vamos a y responded a los escépticos.",
    "consigna_nl": "Presenteer het plan met voy a / vamos a en antwoord de sceptici.",
    "regla": "Elk blok van de dag krijgt een «vamos a»-zin met een concrete activiteit. En je "
             "moet drie tegenwerpingen weerleggen — het plan telt pas als het de test doorstaat.",
    "pasos": [("Repartid el día en cinco bloques.", "Verdeel de dag in vijf blokken."),
              ("Cada bloque, una frase con vamos a.", "Elk blok één zin met vamos a."),
              ("Los escépticos ponen tres pegas.", "De sceptici werpen drie bezwaren op."),
              ("Contestad. El plan gana o pierde.", "Antwoord. Het plan wint of verliest."),
              ("La clase vota: ¿lo hacen o no?", "De klas stemt: doen ze het of niet?")],
    "datos": {
        "bloques": [("la mañana", "de 8:00 a 12:00"), ("la comida", "de 12:00 a 14:00"),
                    ("la tarde", "de 14:00 a 18:00"), ("la cena", "de 18:00 a 21:00"),
                    ("la noche", "de 21:00 a 23:00")],
        "pegas": ["¿Y si alguien tiene que avisar de algo urgente?",
                  "¿Cómo vais a quedar sin móvil?",
                  "¿Y el despertador?",
                  "¿Qué hacéis cuando os aburráis a las cuatro de la tarde?",
                  "¿Y si el plan no funciona a los veinte minutos?"],
        "marco": ["Por la mañana vamos a …", "Después de comer vamos a …",
                  "Para eso vamos a …, así no hace falta el móvil.",
                  "Tienes razón, por eso vamos a …",
                  "Si no funciona, vamos a …"],
    },
    "clave": [
        "«Vamos a» plus infinitief is de hele grammatica van §2, en de bezwaren dwingen tot "
        "hérgebruik: elk antwoord op een pega is opnieuw een «vamos a»-zin.",
        "De wekkervraag is de leukste: bijna niemand heeft nog een wekker die geen telefoon is. "
        "Daar wordt het plan concreet in plaats van principieel.",
        "De laatste pega («¿y si el plan no funciona?») is de belangrijkste: hij dwingt tot een "
        "si-zin met presente plus «vamos a» — de conditionele constructie die in dit leerplan mag.",
        "Toets de vijf blokken en de drie weerleggingen. Of de klas het écht zou doen, is bijzaak.",
    ],
    "nota": "Als een groep het daadwerkelijk uitprobeert, laat ze er de week erna over vertellen. "
            "Dan wordt de reto opeens een echte tarea.",
}

P3_RETO_03 = {
    "id": "C6P-U3-RETO-03", "num": 3, "curso": "C6+", "unidad": P3,
    "seccion": "Cultura", "ancla": "cultura_c6p3", "soporte": "ppt",
    "nombre": "El algoritmo explicado",
    "lente": "🤝 bemiddelen", "forma": "👥 En parejas", "skill": "🔀 Bemiddelen",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Explícale a tu abuela por qué el móvil «sabe» lo que le gusta. Sin palabras en inglés.",
    "gancho_nl": "Leg je grootmoeder uit waarom de gsm «weet» wat ze leuk vindt. Zonder Engelse woorden.",
    "consigna_es": "Explicad el algoritmo en cinco frases, en español sencillo y sin anglicismos.",
    "consigna_nl": "Leg het algoritme uit in vijf zinnen, in eenvoudig Spaans en zonder anglicismen.",
    "regla": "Geen enkel Engels woord — geen algorithm, geen feed, geen like, geen data. En geen "
             "enkele zin langer dan twaalf woorden. Wat je niet kunt uitleggen, heb je niet begrepen.",
    "pasos": [("Escribid qué hace un algoritmo, en una frase.",
               "Schrijf in één zin wat een algoritme doet."),
              ("Buscad una palabra española para cada anglicismo.",
               "Zoek een Spaans woord voor elk Engels woord."),
              ("Explicadlo en cinco frases cortas.", "Leg het uit in vijf korte zinnen."),
              ("Probadlo con alguien que no sepa nada.",
               "Test het op iemand die er niets van weet.")],
    "datos": {
        "prohibidas": [("algoritmo", "es una palabra española, pero hay que explicarla igual"),
                       ("feed", "→ lo que te sale / lo que ves"),
                       ("like", "→ me gusta"),
                       ("data / datos personales", "→ lo que el móvil sabe de ti"),
                       ("engagement", "→ el tiempo que te quedas mirando"),
                       ("recomendación personalizada", "→ lo que te enseña a ti y no a otro")],
        "pasos_explicacion": [("1", "El móvil apunta lo que miras y cuánto tiempo."),
                              ("2", "Lo compara con lo que miran otras personas parecidas."),
                              ("3", "Te enseña más de lo que te hace quedarte."),
                              ("4", "Por eso a ti y a mí no nos sale lo mismo."),
                              ("5", "Y por eso a veces parece que te lee la mente.")],
        "marco": ["Es como si … , pero con …", "No es magia: es que …",
                  "Cuanto más …, más …", "A ti te sale … y a mí …"],
    },
    "clave": [
        "De vijf stappen in de data zijn samen een correcte, volledige uitleg zonder één Engels "
        "woord. Toon ze pas ná de eerste poging — de klas komt er zelf verrassend dicht bij.",
        "«Cuanto más…, más…» is de constructie die de terugkoppeling uitdrukt en die op aanzet-B1 "
        "hoort. Wie hem gebruikt, heeft het mechanisme echt begrepen.",
        "«No es magia: es que…» is de sleutelzin van bemiddelen: eerst het misverstand wegnemen, "
        "dan uitleggen.",
        "Toets op begrijpelijkheid voor de gedachte grootmoeder, niet op technische juistheid. "
        "Een uitleg die klopt maar niet aankomt, is hier fout.",
    ],
    "nota": "Laat het echt testen op iemand buiten de klas, in het Nederlands of het Spaans. De "
            "vraag «snapte die persoon het?» is de eerlijkste beoordeling die er is.",
}

P3_RETO_06 = {
    "id": "C6P-U3-RETO-06", "num": 6, "curso": "C6+", "unidad": P3,
    "seccion": "§3.4", "ancla": "oi_c6p", "soporte": "ppt",
    "nombre": "La cadena de favores",
    "lente": "🔓 puzzel & escape", "forma": "🏫 Toda la clase", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Un favor recorre la clase entera. Y tiene que volver.",
    "gancho_nl": "Eén gunst gaat de hele klas rond. En hij moet terugkomen.",
    "consigna_es": "Pasa el favor con le y devuélvelo con les. Sin romper la cadena.",
    "consigna_nl": "Geef de gunst door met le en stuur hem terug met les. Zonder de ketting te breken.",
    "regla": "Heen gaat het altijd via «le» (aan één persoon), terug altijd via «les» (aan de "
             "groep). Wie de verkeerde vorm gebruikt, breekt de ketting en die begint opnieuw "
             "bij hem.",
    "pasos": [("En círculo. El primero pide un favor a su vecino.",
               "In een kring. De eerste vraagt zijn buur een gunst."),
              ("«Le pido a … que …» y pasa.", "«Le pido a … que …» en doorgeven."),
              ("Al llegar al final, vuelve: «Les digo a todos que …».",
               "Aan het eind keert het terug: «Les digo a todos que …»."),
              ("¿Ha llegado el favor entero? Contadlo.",
               "Is de gunst heel aangekomen? Vertel na.")],
    "datos": {
        "favores": ["prestar los apuntes de ayer", "explicar el ejercicio 4",
                    "cambiar el turno del viernes", "traer el cargador mañana",
                    "guardar un sitio en el comedor", "avisar cuando llegue el profe",
                    "compartir la foto del examen de prueba", "acompañar a secretaría"],
        "marco_ida": ["Le pido a … que me …", "Le digo a … que …",
                      "Le pregunto a … si puede …"],
        "marco_vuelta": ["Les digo a todos que …", "Les explico que …",
                         "Les cuento lo que ha pasado con el favor."],
        "trampa": "Si el favor va a dos personas, ya no es «le» sino «les». "
                  "Eso pasa al menos una vez por ronda.",
    },
    "clave": [
        "Het onderscheid le/les hangt niet aan het werkwoord maar aan het aantal ontvangers. De "
        "kettingvorm maakt dat fysiek zichtbaar: één buur is «le», de hele kring is «les».",
        "De trampa («als de gunst naar twee mensen gaat») komt elke ronde minstens één keer voor. "
        "Laat de kring die zelf betrappen in plaats van hem aan te wijzen.",
        "«Le pido que me preste» lokt de subjuntivo uit («preste»). Die hoort niet in dit "
        "leerplan: laat de kortere vorm toe, «le pido los apuntes», en stuur weg van «que».",
        "Toets of de ketting rondkomt. Twee volledige rondes is beter dan één foutloze — de "
        "tweede loopt altijd sneller.",
    ],
    "nota": "Een echt voorwerp dat rondgaat (een sleutel, een bal) helpt enorm: wie het vasthoudt, "
            "praat. De rest luistert, en dat is de helft van de oefening.",
}

RETOS_C6P_U3 = [P3_RETO_01, P3_RETO_02, P3_RETO_03, P3_RETO_04, P3_RETO_05,
                P3_RETO_06, P3_RETO_07, P3_RETO_08, P3_RETO_09, P3_RETO_10]


# ═══════════════════════════════════════════════════════════════════════════
# C6+ · U4 «De viaje» — parada Chile, het grote reizen
# ═══════════════════════════════════════════════════════════════════════════
P4 = 4

P4_RETO_02 = {
    "id": "C6P-U4-RETO-02", "num": 2, "curso": "C6+", "unidad": P4,
    "seccion": "§3.4", "ancla": "por_para", "soporte": "print",
    "nombre": "Sellos del pasaporte",
    "lente": "🕵️ forensisch", "forma": "👤 Solo", "skill": "👁️ Leer",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Ocho sellos, ninguna explicación. ¿Por dónde pasó y para qué fue?",
    "gancho_nl": "Acht stempels, geen enkele uitleg. Waarlangs ging hij en waarvoor?",
    "consigna_es": "Reconstruye la ruta y da la razón de cada viaje, con por y para.",
    "consigna_nl": "Reconstrueer de route en geef de reden van elke reis, met por en para.",
    "regla": "Elke etappe krijgt één zin met «por» (de weg, de doorgang) én één met «para» (het "
             "doel). Wie de twee door elkaar haalt, verliest die etappe — dat is precies de test.",
    "pasos": [("Ordena los ocho sellos por fecha.", "Zet de acht stempels op datum."),
              ("Marca los que son solo de paso.", "Markeer welke enkel doorreis zijn."),
              ("Escribe una frase con por y una con para por etapa.",
               "Schrijf per etappe één zin met por en één met para."),
              ("Un sello no encaja. ¿Cuál?", "Eén stempel past niet. Welke?")],
    "datos": {
        # (datum, plaats, type stempel, wat het verraadt)
        "sellos": [
            ("3 ENE", "Madrid–Barajas", "salida", "el punto de partida"),
            ("3 ENE", "Bogotá", "entrada, tránsito 4 h", "solo pasó por allí"),
            ("4 ENE", "Santiago de Chile", "entrada", "aquí empieza de verdad"),
            ("11 ENE", "Mendoza (Argentina)", "entrada por tierra", "cruzó los Andes en bus"),
            ("14 ENE", "Santiago de Chile", "entrada", "volvió"),
            ("22 ENE", "Punta Arenas", "vuelo nacional", "bajó al sur del todo"),
            ("28 ENE", "Lima", "entrada, tránsito 2 h", "otra vez solo de paso"),
            ("28 ENE", "Ámsterdam", "entrada", "y en Ámsterdam no vive nadie de esta historia"),
        ],
        "razones": ["para estudiar un semestre", "para ver a la familia",
                    "para hacer una ruta de senderismo", "para trabajar dos semanas",
                    "para un congreso", "para asistir a una boda"],
        "marco": ["Pasó por … para llegar a …", "Fue a … para …",
                  "En … solo estuvo … horas: fue un tránsito.",
                  "El sello de … no encaja porque …"],
    },
    "clave": [
        "Drie stempels zijn pure doorreis: Bogotá (4 u), Lima (2 u) en Amsterdam. Alleen bij die "
        "drie is «por» de enige juiste keuze.",
        "Mendoza is de mooiste etappe: «entrada por tierra» betekent dat hij de Andes over ging "
        "met de bus — «cruzó los Andes por tierra para llegar a Mendoza» gebruikt beide in één zin.",
        "De stempel die niet past is Amsterdam: alle andere liggen in de Spaanstalige wereld, en "
        "het is de enige plek zonder reden in de lijst. Het is een tussenlanding op de terugweg.",
        "Toets het onderscheid: «por» = de weg of de doorgang, «para» = het doel. Elke etappe "
        "levert dat contrast op, en één zin per etappe is genoeg om het te bewijzen.",
    ],
    "nota": "Werkt sterk met een echte (afgeplakte) paspoortpagina op het scherm. Wie er een heeft, "
            "mag zijn eigen stempels meebrengen — maar niemand moet.",
}

P4_RETO_04 = {
    "id": "C6P-U4-RETO-04", "num": 4, "curso": "C6+", "unidad": P4,
    "seccion": "§1.4", "ancla": "viaje_c6p", "soporte": "print",
    "nombre": "La reseña de un hostal",
    "lente": "✍️ creatieve beperking", "forma": "👥 En parejas", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Los mismos hechos. Cinco estrellas y una estrella.",
    "gancho_nl": "Dezelfde feiten. Vijf sterren en één ster.",
    "consigna_es": "Escribid las dos reseñas usando exactamente los mismos ocho datos.",
    "consigna_nl": "Schrijf beide recensies met exact dezelfde acht gegevens.",
    "regla": "Alle acht de feiten staan in béide recensies. Je mag niets weglaten en niets "
             "verzinnen — alleen de volgorde, de conectoren en de toon mag je veranderen.",
    "pasos": [("Leed los ocho datos del hostal.", "Lees de acht gegevens van de hostel."),
              ("Escribid la reseña de cinco estrellas.", "Schrijf de vijfsterrenrecensie."),
              ("Ahora la de una, con los mismos datos.",
               "Nu die van één ster, met dezelfde gegevens."),
              ("Comparad: ¿qué palabra hace el trabajo?",
               "Vergelijk: welk woord doet het werk?")],
    "datos": {
        "hostal": "Hostal Andino · Santiago de Chile · 14 € la noche",
        "datos": ["la habitación es compartida, con ocho camas",
                  "está a veinte minutos del centro, andando",
                  "el desayuno es pan, mermelada y café, siempre lo mismo",
                  "hay una terraza en el tejado",
                  "las paredes son finas",
                  "la dueña habla contigo media hora cada mañana",
                  "no hay ascensor y está en el cuarto piso",
                  "cierran la puerta a la una de la madrugada"],
        "marco_bien": ["Lo mejor es que …", "Además, …", "Y aunque … , la verdad es que …",
                       "Para el precio que tiene, …"],
        "marco_mal": ["El problema es que …", "Y encima …", "Sí, hay … , pero …",
                      "Por catorce euros no pides mucho, pero …"],
    },
    "clave": [
        "Elk gegeven is neutraal en kan beide kanten op. «La dueña habla contigo media hora» is "
        "gastvrijheid óf tijdverlies; «cierran a la una» is veiligheid óf avondklok.",
        "De conectoren doen het werk: «aunque» plaatst het nadeel eerst en het voordeel na, «y "
        "encima» stapelt het negatieve. Dezelfde feiten, andere volgorde.",
        "Toets of alle acht in béide teksten staan. Wie er één laat vallen, heeft niet "
        "geherformuleerd maar geselecteerd — en dat is precies wat echte recensies doen.",
        "Sluit af met de vraag: welke van de twee is «waar»? Beide. Dat inzicht is het doel.",
    ],
    "nota": "Vergelijk daarna met twee echte recensies van dezelfde plek op internet. De klas ziet "
            "meteen dezelfde techniek terug.",
}

P4_RETO_09 = {
    "id": "C6P-U4-RETO-09", "num": 9, "curso": "C6+", "unidad": P4,
    "seccion": "Cultura", "ancla": "cultura_c6p4", "soporte": "print",
    "nombre": "Turismo que hace daño",
    "lente": "🔬 onderzoek & data", "forma": "👥 En parejas", "skill": "👁️ Leer",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Barcelona tiene más camas de turista que habitantes en algunos barrios.",
    "gancho_nl": "Barcelona heeft in sommige wijken meer toeristenbedden dan inwoners.",
    "consigna_es": "Lee los datos y escribe tu postura en tres frases con cifras.",
    "consigna_nl": "Lees de gegevens en schrijf je standpunt in drie zinnen met cijfers.",
    "regla": "Elke zin van je standpunt bevat een cijfer uit de tabel. En één van de drie moet "
             "de ándere kant erkennen — een standpunt zonder tegenargument is een mening, geen positie.",
    "pasos": [("Leed la tabla de las dos ciudades.", "Lees de tabel van de twee steden."),
              ("Buscad el dato que más os choca.", "Zoek het cijfer dat jullie het meest raakt."),
              ("Escribid tres frases con cifra.", "Schrijf drie zinnen met een cijfer."),
              ("Una de las tres da la razón al otro lado.",
               "Eén van de drie geeft de andere kant gelijk.")],
    "datos": {
        "tabla": [("Barcelona", "1,6 millones de habitantes",
                   "unos 12 millones de visitantes al año", "el turismo es un 12 % de la economía"),
                  ("Cusco", "unos 430 000 habitantes",
                   "más de 3 millones de visitantes al año", "y casi todos suben a Machu Picchu"),
                  ("Barcelona · Barceloneta", "unos 15 000 vecinos",
                   "el barrio con más pisos turísticos", "los alquileres han subido mucho"),
                  ("Cusco · centro", "casi sin vecinos jóvenes",
                   "hoteles donde antes había casas", "el suelo cuesta más que el sueldo medio")],
        "voces": [("una vecina de la Barceloneta", "«Ya no conozco a nadie en mi escalera.»"),
                  ("un guía de Cusco", "«Mi trabajo existe gracias al turismo.»"),
                  ("un camarero", "«Sin turistas cierro en tres meses.»"),
                  ("un estudiante", "«No encuentro piso en mi propia ciudad.»")],
        "marco": ["En … hay … visitantes por cada habitante.",
                  "Por un lado, … ; por otro, …",
                  "Entiendo que … , pero …",
                  "Mi postura es que … , porque …"],
    },
    "clave": [
        "Barcelona telt ongeveer 7,5 bezoekers per inwoner per jaar, Cusco ongeveer 7. Bijna "
        "identiek — en dat verrast, want de steden lijken onvergelijkbaar.",
        "De vier stemmen zijn bewust niet te verzoenen: de gids en de kelner leven ervan, de buurvrouw "
        "en de student niet. Wie dat in één positie samenbrengt, doet het werk van de reto.",
        "«Por un lado…, por otro…» is de conector die het leerplan vraagt voor een genuanceerd "
        "standpunt, en die hier vanzelf nodig is.",
        "Cijfers zijn ordes van grootte uit publieke bronnen; noem dat. Een standpunt hoeft geen "
        "exacte statistiek, maar wel eerlijke cijfers.",
    ],
    "nota": "Trek de lijn door naar de eigen omgeving: Brugge en Gent kennen hetzelfde debat. Dat "
            "maakt het onmiddellijk minder ver weg.",
}

P4_RETO_10 = {
    "id": "C6P-U4-RETO-10", "num": 10, "curso": "C6+", "unidad": P4,
    "seccion": "§2.4", "ancla": "perfecto_c6p", "soporte": "print",
    "nombre": "He estado, no he estado",
    "lente": "🔓 puzzel & escape", "forma": "🏫 Toda la clase", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★☆",
    "gancho_es": "Bingo de experiencias. Pero una firma no basta: hay que preguntar más.",
    "gancho_nl": "Ervaringenbingo. Maar één handtekening volstaat niet: je moet doorvragen.",
    "consigna_es": "Llena el cartón, y por cada casilla haz una pregunta extra en perfecto.",
    "consigna_nl": "Vul de kaart, en stel bij elk vakje één extra vraag in het perfecto.",
    "regla": "Eén naam per vakje en niemand twee keer op je kaart. En bij elke handtekening stel "
             "je één doorvraag in het perfecto — het antwoord noteer je erbij, anders telt het vakje niet.",
    "pasos": [("Levantaos y preguntad: «¿Has …?»", "Sta op en vraag: «¿Has …?»"),
              ("Si dice que sí, firma y contesta tu pregunta extra.",
               "Bij ja: handtekening plus antwoord op je doorvraag."),
              ("Una persona, una casilla. Nadie repite.",
               "Eén persoon, één vakje. Niemand twee keer."),
              ("¿Cartón lleno? Contad las historias, no las firmas.",
               "Kaart vol? Vertel de verhalen, niet de handtekeningen.")],
    "datos": {
        "casillas": ["ha dormido en un tren", "ha perdido una maleta",
                     "ha viajado solo/-a", "ha comido algo que no sabía qué era",
                     "ha perdido un avión o un bus", "ha estado en tres países en un año",
                     "ha hablado español fuera de clase", "se ha perdido en una ciudad",
                     "ha hecho un viaje de más de diez horas", "ha dormido en un aeropuerto",
                     "ha ido a un sitio sin plan", "ha vuelto antes de tiempo"],
        "extra": ["¿Dónde ha sido?", "¿Con quién has ido?", "¿Cuánto tiempo has estado?",
                  "¿Y qué has hecho después?", "¿Lo has vuelto a hacer?",
                  "¿Se lo has contado a alguien?"],
        "marco": ["¿Has …?", "Sí, … / No, nunca he …",
                  "¿Y dónde ha sido?", "Firma aquí, por favor."],
    },
    "clave": [
        "De doorvraag is de hele didactiek: zonder haar is bingo een handtekeningenjacht. Met "
        "haar levert elk vakje twee perfecto-vormen op — de vraag en het antwoord.",
        "«Se lo has contado a alguien?» is de brug naar U5 (se lo/se la) en zit er bewust in als "
        "vooruitwijzing.",
        "Toets de genoteerde antwoorden, niet de handtekeningen. Wie twaalf namen heeft en nul "
        "antwoorden, heeft niet gepraat maar verzameld.",
        "Wie nooit gereisd heeft, kan bijna elk vakje toch invullen: «se ha perdido en una "
        "ciudad» of «ha comido algo que no sabía qué era» hoeft geen vliegtuig. Dat is bewust zo "
        "gekozen.",
    ],
    "nota": "Twaalf vakjes is meer dan een klas van twintig aankan in één ronde. Dat is de "
            "bedoeling: niemand vult alles, iedereen praat.",
}

P4_RETO_06 = {
    "id": "C6P-U4-RETO-06", "num": 6, "curso": "C6+", "unidad": P4,
    "seccion": "§2.4", "ancla": "perfecto_c6p", "soporte": "hub",
    "nombre": "El viaje que no hice",
    "lente": "🎭 simulatie met beperking", "forma": "👤 Solo", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★★",
    "gancho_es": "Cuenta un viaje que nunca hiciste. Y que no se note.",
    "gancho_nl": "Vertel een reis die je nooit maakte. En laat het niet merken.",
    "consigna_es": "Graba un minuto sobre un viaje inventado, todo en perfecto.",
    "consigna_nl": "Neem één minuut op over een verzonnen reis, alles in het perfecto.",
    "regla": "Alles in het perfecto compuesto, en minstens één detail dat niemand zou verzinnen. "
             "Maar geen enkele leugen over een echt bestaande plek die je fout beschrijft — dat "
             "is het gat dat de klas zoekt.",
    "pasos": [("Elige un destino que conoces solo de fotos.",
               "Kies een bestemming die je alleen van foto's kent."),
              ("Busca dos datos reales: el clima y el transporte.",
               "Zoek twee echte gegevens: het weer en het vervoer."),
              ("Graba un minuto, todo en perfecto.", "Neem één minuut op, alles in het perfecto."),
              ("La clase busca el hueco. ¿Lo encuentran?",
               "De klas zoekt het gat. Vinden ze het?")],
    "datos": {
        "marco": ["He estado en … este verano.",
                  "He llegado en … , porque no hay …",
                  "Lo que más me ha sorprendido ha sido …",
                  "He comido … , y no ha sido lo que esperaba.",
                  "No he podido … , y eso me ha dado rabia."],
        "detalles": ["el precio de algo pequeño", "un olor", "una cola inesperada",
                     "cómo se paga el bus", "a qué hora oscurece",
                     "qué te dijo alguien en la calle"],
    },
    "clave": [
        "De regel «minstens één detail dat niemand zou verzinnen» is wat het verhaal geloofwaardig "
        "maakt — en meteen de reden waarom leerlingen echte informatie gaan opzoeken.",
        "«No he podido…» is de zin die het vaakst ontbreekt en die het verhaal het meest echt "
        "maakt: elke reis heeft iets dat mislukte.",
        "Toets de perfecto-vormen en de vlotheid van één minuut. Of het gat gevonden wordt, is "
        "een spel, geen beoordeling.",
        "Niemand hoeft te doen alsof hij gereisd heeft: de opdracht ís fictie, en dat is voor de "
        "hele klas hetzelfde vertrekpunt.",
    ],
    "nota": "Laat de klas ná de opname vragen stellen. Wie zijn verzonnen reis kan verdedigen "
            "onder ondervraging, spreekt echt.",
}

P4_RETO_07 = {
    "id": "C6P-U4-RETO-07", "num": 7, "curso": "C6+", "unidad": P4,
    "seccion": "§1.4", "ancla": "viaje_c6p", "soporte": "hub",
    "nombre": "Anuncio de megafonía",
    "lente": "📻 mediaformat", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 10 min", "dificultad": "★★☆",
    "gancho_es": "«Señores pasajeros, el tren con destino…». Rápido, formal, y se entiende.",
    "gancho_nl": "«Señores pasajeros, el tren con destino…». Snel, formeel, en verstaanbaar.",
    "consigna_es": "Graba tres anuncios de estación con las fórmulas exactas.",
    "consigna_nl": "Neem drie stationsomroepen op met de exacte formules.",
    "regla": "Usted-vorm, geen enkel woord te veel, en de drie vaste onderdelen in deze volgorde: "
             "aanspreking, informatie, instructie. Wie «tú» gebruikt, is geen omroeper.",
    "pasos": [("Escucha el modelo dos veces.", "Luister het model twee keer."),
              ("Fíjate en el orden: quién, qué, qué hay que hacer.",
               "Let op de volgorde: wie, wat, wat te doen."),
              ("Graba los tres anuncios seguidos.", "Neem de drie omroepen na elkaar op."),
              ("Escucha: ¿se entiende a la primera?",
               "Luister terug: begrijp je het meteen?")],
    "datos": {
        "marco": ["Señores pasajeros, buenos días.",
                  "El tren con destino a … va a efectuar su salida por la vía …",
                  "Rogamos a los pasajeros que se dirijan a la puerta …",
                  "Última llamada para el vuelo … con destino a …",
                  "Disculpen las molestias."],
        "situaciones": [("un retraso de cuarenta minutos", "hay que explicar y disculparse"),
                        ("un cambio de vía a última hora", "hay que dar la nueva vía dos veces"),
                        ("un pasajero que no se ha presentado", "hay que llamarlo por su nombre")],
    },
    "clave": [
        "De drie vaste onderdelen (aanspreking · informatie · instructie) zitten in elke echte "
        "omroep. Wie ze in die volgorde zet, klinkt onmiddellijk professioneel.",
        "«Rogamos a los pasajeros que se dirijan» bevat subjuntivo. Die hoort niet in dit "
        "leerplan: het is een vaste formule om te herkénnen en na te zeggen, niet om te "
        "analyseren. Zeg dat er expliciet bij.",
        "Het wisselen van perron moet twee keer gezegd worden — dat is geen taalregel maar een "
        "beroepsregel, en het maakt de opdracht meteen echt.",
        "Toets verstaanbaarheid en de usted-vorm, niet de snelheid. Een omroep die niemand "
        "verstaat, is geen goede omroep, hoe snel ook.",
    ],
    "nota": "Speel een echte opname van Renfe of van een luchthaven vooraf. Het verschil in "
            "intonatie is meteen hoorbaar en heel leerzaam.",
}

P4_RETO_08 = {
    "id": "C6P-U4-RETO-08", "num": 8, "curso": "C6+", "unidad": P4,
    "seccion": "Cultura", "ancla": "cultura_c6p4", "soporte": "hub",
    "nombre": "Choque cultural",
    "lente": "🤝 bemiddelen", "forma": "👨‍👩‍👧 En grupos", "skill": "🔀 Bemiddelen",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Cuatro situaciones reales donde un belga mete la pata sin saberlo.",
    "gancho_nl": "Vier echte situaties waarin een Belg de bal misslaat zonder het te weten.",
    "consigna_es": "Elige qué se dice de verdad en cada situación.",
    "consigna_nl": "Kies wat je in elke situatie echt zegt.",
    "regla": "Geen enkele optie is grammaticaal fout. Je kiest op register en gewoonte — en dat "
             "is precies waarom letterlijk vertalen hier niet werkt.",
    "pasos": [("Lee la situación entera.", "Lees de hele situatie."),
              ("Piensa qué espera la otra persona.",
               "Denk na wat de ander verwacht."),
              ("Elige y comprueba por qué.", "Kies en controleer waarom.")],
    "datos": {
        "items": [
            ("Llegas a una comida familiar en Chile a la hora exacta. No hay nadie listo.",
             "No pasa nada, llegar veinte minutos tarde es lo normal.",
             ["No pasa nada, llegar veinte minutos tarde es lo normal.",
              "Has hecho bien: la puntualidad se agradece.",
              "Es mejor avisar antes."],
             "een uitnodiging om twee uur betekent in veel families half drie; te vroeg zetten "
             "gastheren onder druk"),
            ("En el hostal te ofrecen más comida y ya no puedes más. Dices «no, gracias».",
             "Añade una razón: «no, gracias, es que ya no me cabe más, estaba buenísimo».",
             ["Añade una razón: «no, gracias, es que ya no me cabe más, estaba buenísimo».",
              "«No, gracias» es suficiente.",
              "Hay que aceptar siempre."],
             "een kaal «nee bedankt» klinkt kortaf; de reden plus een compliment doet het werk"),
            ("Un camarero te tutea desde el primer momento. Tú le hablas de usted.",
             "Puedes pasar al tú: te lo está ofreciendo.",
             ["Puedes pasar al tú: te lo está ofreciendo.",
              "Sigue con usted, es más educado.",
              "Es una falta de respeto por su parte."],
             "de ander zet de toon; blijven usteden schept juist afstand"),
            ("Alguien te pregunta cuánto ganan tus padres. En Bélgica no se pregunta eso.",
             "Contesta en general y devuelve la pregunta: «depende, ¿y aquí?».",
             ["Contesta en general y devuelve la pregunta: «depende, ¿y aquí?».",
              "Contesta con la cifra exacta.",
              "Di que es una pregunta maleducada."],
             "de vraag is niet onbeleefd bedoeld; algemeen antwoorden plus terugkaatsen houdt "
             "het gesprek open"),
        ],
    },
    "clave": [
        "De vier situaties gaan over hetzelfde: het Vlaamse standaardgedrag is niet fout, maar "
        "het komt anders aan. Bemiddelen begint met dat inzien.",
        "Item 2 is didactisch het belangrijkste: «no, gracias» plus een reden is een taalpatroon "
        "dat leerlingen meteen kunnen toepassen, ook in het Nederlands.",
        "Item 4 heeft geen absoluut juist antwoord — in sommige kringen is de vraag wél "
        "ongepast. De verantwoording telt, niet de keuze.",
        "Vermijd te generaliseren over «de Chilenen» of «de Spanjaarden». Deze gewoontes "
        "verschillen per familie en per streek; benoem dat.",
    ],
    "nota": "Draai het om: welke Vlaamse gewoontes zouden een Chileense uitwisselingsstudent "
            "verbazen? Die lijst maakt de klas altijd graag.",
}

P4_RETO_01 = {
    "id": "C6P-U4-RETO-01", "num": 1, "curso": "C6+", "unidad": P4,
    "seccion": "§1.4", "ancla": "viaje_c6p", "soporte": "ppt",
    "nombre": "El vuelo cancelado",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 18 min", "dificultad": "★★★",
    "gancho_es": "Tú tienes derechos. El mostrador tiene normas. Los dos tenéis razón.",
    "gancho_nl": "Jij hebt rechten. De balie heeft regels. Jullie hebben allebei gelijk.",
    "consigna_es": "Negociad una solución. Cada uno tiene una instrucción secreta.",
    "consigna_nl": "Onderhandel over een oplossing. Elk heeft een geheime instructie.",
    "regla": "Je geheime instructie mag je niet voorlezen en niet vertalen — je moet ernaar "
             "hándelen. En niemand mag de stem verheffen: dit is een balie, geen ruzie.",
    "pasos": [("Repartid los papeles y leed la instrucción en secreto.",
               "Verdeel de rollen en lees je instructie in het geheim."),
              ("El pasajero empieza. El mostrador escucha antes de contestar.",
               "De passagier begint. De balie luistert vóór ze antwoordt."),
              ("Negociad hasta un acuerdo, o hasta el bloqueo.",
               "Onderhandel tot een akkoord, of tot een impasse."),
              ("Contad a la clase qué habéis acordado y por qué.",
               "Vertel de klas wat jullie afspraken en waarom.")],
    "datos": {
        "situacion": "Vuelo Santiago–Madrid, cancelado a las 22:40. El próximo es dentro de 26 horas.",
        "instruccion_pasajero": [
            "Tienes un examen pasado mañana a las nueve de la mañana.",
            "No te puedes permitir un hotel de tu bolsillo.",
            "Sabes que tienes derecho a comida y alojamiento, pero no sabes decirlo con esas palabras.",
        ],
        "instruccion_mostrador": [
            "Solo puedes dar un vale de comida de 12 €, salvo que el pasajero lo pida claramente.",
            "Tienes dos plazas en un vuelo de otra compañía, pero son para casos urgentes.",
            "Llevas nueve horas de turno y eres la única persona en el mostrador.",
        ],
        "marco_pasajero": ["Entiendo que no es culpa suya, pero …",
                           "Tengo que estar en … el … a las …",
                           "¿Qué opciones hay?", "¿Y si me pone en otro vuelo?"],
        "marco_mostrador": ["Lo siento mucho, en este momento …",
                            "Lo que sí puedo hacer es …", "Deme un momento, lo compruebo.",
                            "Si es urgente, tengo otra opción."],
    },
    "clave": [
        "De sleutel zit in de tweede instructie van de balie: er zijn twee plaatsen, maar alleen "
        "voor dringende gevallen. De passagier moet dus zijn examen noemen — en dat is een "
        "spreekhandeling, geen woordenschatoefening.",
        "«Lo que sí puedo hacer es…» is de belangrijkste chunk aan de baliekant: iets weigeren "
        "en tegelijk een uitweg bieden.",
        "De impasse is een geldig einde. Twee duo's die vastlopen maar beleefd blijven, hebben de "
        "reto beter gedaan dan een duo dat meteen alles krijgt.",
        "Toets de spreekhandelingen (klacht formuleren, alternatief vragen, weigeren met uitweg), "
        "niet wie wint.",
    ],
    "nota": "Draai daarna de rollen om met dezelfde instructies. De tweede ronde is altijd beter, "
            "en de klas hoort dat zelf.",
}

P4_RETO_03 = {
    "id": "C6P-U4-RETO-03", "num": 3, "curso": "C6+", "unidad": P4,
    "seccion": "§3.4", "ancla": "por_para", "soporte": "ppt",
    "nombre": "Presupuesto de mochilero",
    "lente": "🔬 onderzoek & data", "forma": "👨‍👩‍👧 En grupos", "skill": "✍️ Escribir",
    "tiempo": "± 18 min", "dificultad": "★★★",
    "gancho_es": "Diez días, tres países, seiscientos euros. Y hay que dormir en algún sitio.",
    "gancho_nl": "Tien dagen, drie landen, zeshonderd euro. En slapen moet ergens.",
    "consigna_es": "Montad el viaje dentro del presupuesto y justificad cada gasto con por o para.",
    "consigna_nl": "Stel de reis samen binnen het budget en verantwoord elke uitgave met por of para.",
    "regla": "Zeshonderd euro, geen cent meer, en tien nachten moeten gedekt zijn. Elke uitgave "
             "wordt verantwoord met «por» (het bedrag, de ruil) of «para» (het doel).",
    "pasos": [("Mirad los precios de los tres países.",
               "Bekijk de prijzen van de drie landen."),
              ("Decidid la ruta y contad las noches.",
               "Bepaal de route en tel de nachten."),
              ("Justificad cada gasto con por o para.",
               "Verantwoord elke uitgave met por of para."),
              ("¿Cabe en 600 €? Si no, ¿qué quitáis?",
               "Past het in 600 €? Zo niet, wat schrappen jullie?")],
    "datos": {
        "precios": [("Chile · hostal", "unos 18 € la noche"),
                    ("Chile · comida del día", "unos 9 €"),
                    ("Chile · bus largo (10 h)", "unos 30 €"),
                    ("Perú · hostal", "unos 11 € la noche"),
                    ("Perú · comida del día", "unos 6 €"),
                    ("Perú · bus largo (10 h)", "unos 18 €"),
                    ("Bolivia · hostal", "unos 8 € la noche"),
                    ("Bolivia · comida del día", "unos 5 €"),
                    ("Bolivia · bus largo (10 h)", "unos 12 €"),
                    ("entrada a un parque nacional", "entre 15 € y 40 €"),
                    ("vuelo interno", "entre 60 € y 120 €")],
        "marco": ["Vamos en bus por … euros.", "Reservamos … para dormir en …",
                  "Cambiamos el vuelo por el bus, porque …",
                  "Nos quedan … euros para …", "Por ese precio no vale la pena …"],
    },
    "clave": [
        "Het budget klopt alleen als de groep tijd inruilt tegen geld: de bus van tien uur in "
        "plaats van de binnenlandse vlucht. Dat is de kern van backpacken en meteen de beste "
        "«por»-zin: «cambiamos el vuelo por el bus».",
        "Chili is bijna dubbel zo duur als Bolivia. Wie de route van zuid naar noord legt, houdt "
        "geld over voor de parken; omgekeerd niet.",
        "«Por» voor het bedrag en de ruil, «para» voor het doel — het budget maakt dat verschil "
        "concreet in plaats van abstract.",
        "Toets de tien gedekte nachten, het bedrag, en of elke uitgave een por- of para-zin heeft.",
    ],
    "nota": "Prijzen zijn ordes van grootte. Wie actuele prijzen opzoekt, mag ze gebruiken — dan "
            "wordt de oefening alleen maar echter.",
}

P4_RETO_05 = {
    "id": "C6P-U4-RETO-05", "num": 5, "curso": "C6+", "unidad": P4,
    "seccion": "§3.4", "ancla": "por_para", "soporte": "ppt",
    "nombre": "Equipaje de mano",
    "lente": "⚖️ onderhandeling & dilemma", "forma": "👨‍👩‍👧 En grupos", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Siete kilos. Treinta días. Cuatro personas que no están de acuerdo.",
    "gancho_nl": "Zeven kilo. Dertig dagen. Vier mensen die het oneens zijn.",
    "consigna_es": "Decidid qué entra en la mochila. Cada objeto se defiende con para.",
    "consigna_nl": "Beslis wat de rugzak in gaat. Elk voorwerp wordt verdedigd met para.",
    "regla": "Zeven kilo, geen gram meer. Elk voorwerp krijgt een «para»-zin die zegt waarvóór "
             "het dient — «para el frío de la noche», niet «porque es útil». Zonder «para» blijft "
             "het thuis.",
    "pasos": [("Mirad la lista y los pesos.", "Bekijk de lijst en de gewichten."),
              ("Cada uno defiende tres objetos con para.",
               "Elk verdedigt drie voorwerpen met para."),
              ("Sumad. ¿Pasáis de siete kilos?", "Tel op. Zitten jullie boven zeven kilo?"),
              ("Negociad hasta llegar justo.", "Onderhandel tot het precies past."),
              ("Y ahora: ¿qué habéis dejado y os va a hacer falta?",
               "En nu: wat lieten jullie achter en gaan jullie missen?")],
    "datos": {
        "objetos": [("dos pantalones", 900), ("cuatro camisetas", 600),
                    ("un jersey de lana", 500), ("un chubasquero", 350),
                    ("botas de montaña", 1200), ("chanclas", 200),
                    ("saco de dormir fino", 700), ("toalla de microfibra", 150),
                    ("neceser completo", 600), ("botiquín", 300),
                    ("cargador y cables", 250), ("libro de papel", 400),
                    ("cámara pequeña", 450), ("candado y cuerda", 200),
                    ("bañador", 150), ("gorro y guantes", 250)],
        "destino": "Del desierto de Atacama a la Patagonia: 35 °C de día en el norte, "
                   "0 °C de noche en el sur.",
        "marco": ["Llevo … para …", "Sin … no puedo, porque …",
                  "Eso lo dejamos: para … ya tenemos …",
                  "¿Y para qué lo quieres exactamente?",
                  "Nos pasamos de … gramos. ¿Qué quitamos?"],
    },
    "clave": [
        "De volledige lijst weegt ongeveer 7,2 kilo: net te veel. Er móet dus geschrapt worden, "
        "en dat is opzet.",
        "De bestemming beslist: van Atacama naar Patagonië betekent 35 graden én nul graden. Wie "
        "de muts schrapt, heeft de opdracht niet gelezen; wie het boek houdt boven de "
        "regenjas, moet dat kunnen verdedigen.",
        "«¿Y para qué lo quieres exactamente?» is de vraag die de hele reto draagt: hij dwingt de "
        "ander tot een tweede, preciezere para-zin.",
        "Toets de para-zinnen en het eindgewicht. Welke voorwerpen meegaan, is aan de groep.",
    ],
    "nota": "Weeg het echt na als je een weegschaal hebt en de klas eigen spullen meebrengt. Het "
            "verschil tussen geschat en gewogen gewicht is altijd een verrassing.",
}

RETOS_C6P_U4 = [P4_RETO_01, P4_RETO_02, P4_RETO_03, P4_RETO_04, P4_RETO_05,
                P4_RETO_06, P4_RETO_07, P4_RETO_08, P4_RETO_09, P4_RETO_10]


# ═══════════════════════════════════════════════════════════════════════════
# C6+ · U5 «Érase una vez» — parada Buenos Aires, gastheer Mateo (voseo)
# ═══════════════════════════════════════════════════════════════════════════
P5 = 5

P5_RETO_02 = {
    "id": "C6P-U5-RETO-02", "num": 2, "curso": "C6+", "unidad": P5,
    "seccion": "§2.4", "ancla": "indefinido", "soporte": "print",
    "nombre": "La línea del tiempo saboteada",
    "lente": "🕵️ forensisch", "forma": "👥 En parejas", "skill": "👁️ Leer",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Ocho hechos de una vida. Dos no ocurrieron nunca.",
    "gancho_nl": "Acht feiten uit één leven. Twee gebeurden nooit.",
    "consigna_es": "Ordena los hechos y descarta los dos falsos, con un argumento.",
    "consigna_nl": "Zet de feiten op volgorde en gooi de twee valse eruit, met een argument.",
    "regla": "Aanwijzen volstaat niet: je zegt met welk ánder feit de valse botst. Een leugen die "
             "alleen «raar klinkt», blijft staan.",
    "pasos": [("Leed los ocho hechos.", "Lees de acht feiten."),
              ("Ordenadlos por fecha.", "Zet ze op datum."),
              ("Buscad los dos que chocan con otro hecho.",
               "Zoek de twee die botsen met een ander feit."),
              ("Escribid la línea del tiempo definitiva.",
               "Schrijf de definitieve tijdlijn.")],
    "datos": {
        # (jaar, gebeurtenis, klopt het?, waarom niet)
        "hechos": [
            ("1910", "Nació en un pueblo de la provincia de Buenos Aires.", True, ""),
            ("1928", "Se mudó a la capital y empezó a trabajar en una imprenta.", True, ""),
            ("1931", "Publicó su primer libro de poemas, con dinero prestado.", True, ""),
            ("1936", "Viajó a España y volvió justo antes de la guerra.", True, ""),
            ("1940", "Ganó un premio nacional que no existía hasta 1958.", False,
             "el premio se creó dieciocho años después"),
            ("1947", "Abrió una librería que sigue abierta hoy.", True, ""),
            ("1952", "Se fue a vivir a México y no volvió nunca.", False,
             "en 1968 dio una conferencia en Buenos Aires"),
            ("1968", "Dio una conferencia en Buenos Aires ante mil personas.", True, ""),
        ],
        "marco": ["Primero … y después …", "En … , … años más tarde, …",
                  "Este hecho no puede ser verdad, porque en … ya …",
                  "Choca con el hecho de …"],
    },
    "clave": [
        "De twee valse: de prijs van 1940 (bestond pas vanaf 1958) en het definitieve vertrek "
        "naar Mexico in 1952 (want in 1968 gaf hij een lezing in Buenos Aires).",
        "Alleen de tweede botst met een ánder feit uit de lijst — dat is de moeilijkste en de "
        "belangrijkste. De eerste botst met een gegeven dát in de zin zelf staat.",
        "De zin over Spanje stond eerst met een subjuntivo («antes de que empezara»). Die vorm "
        "hoort niet in dit leerplan en is vervangen door «justo antes de la guerra» — dezelfde "
        "informatie, binnen bereik.",
        "Toets het argument, niet het aanwijzen. Twee keer «die is vals» zonder botsing is nul.",
    ],
    "nota": "Het personage is fictief en samengesteld: zo kan niemand het antwoord opzoeken en "
            "moet de klas écht redeneren.",
}

P5_RETO_04 = {
    "id": "C6P-U5-RETO-04", "num": 4, "curso": "C6+", "unidad": P5,
    "seccion": "§1.4", "ancla": "biografia", "soporte": "print",
    "nombre": "Museo de una sola sala",
    "lente": "🎭 simulatie met beperking", "forma": "👨‍👩‍👧 En grupos", "skill": "✍️ Escribir",
    "tiempo": "± 18 min", "dificultad": "★★★",
    "gancho_es": "Una sala, cinco objetos. Toda una vida tiene que caber ahí.",
    "gancho_nl": "Eén zaal, vijf voorwerpen. Een heel leven moet daarin passen.",
    "consigna_es": "Elegid cinco objetos y escribid su cartela: qué es, de cuándo, por qué está aquí.",
    "consigna_nl": "Kies vijf voorwerpen en schrijf hun bijschrift: wat, van wanneer, waarom het hier staat.",
    "regla": "Vijf voorwerpen, niet zes. Elk bijschrift heeft drie regels — wat het is, uit welk "
             "jaar, en wat er met dat voorwerp gebeurde — en die derde regel staat altijd in het "
             "indefinido.",
    "pasos": [("Elegid una figura del mundo hispano.",
               "Kies een figuur uit de Spaanstalige wereld."),
              ("Buscad cinco momentos de su vida.", "Zoek vijf momenten uit haar leven."),
              ("Convertid cada momento en un objeto.",
               "Zet elk moment om in een voorwerp."),
              ("Escribid las cinco cartelas.", "Schrijf de vijf bijschriften."),
              ("Colocad los objetos en la sala. ¿Por dónde entra el visitante?",
               "Plaats de voorwerpen in de zaal. Waar komt de bezoeker binnen?")],
    "datos": {
        "figuras": [("Frida Kahlo", "México · pintora"),
                    ("Gabriel García Márquez", "Colombia · escritor"),
                    ("Rigoberta Menchú", "Guatemala · activista, Nobel de la Paz"),
                    ("Violeta Parra", "Chile · música y folclorista"),
                    ("Mercedes Sosa", "Argentina · cantante"),
                    ("Pau Casals", "Cataluña · violonchelista"),
                    ("José Martí", "Cuba · escritor y político"),
                    ("Chavela Vargas", "Costa Rica y México · cantante")],
        "tipos_objeto": ["algo que usó todos los días", "algo que perdió",
                         "algo que le regalaron", "algo que hizo con sus manos",
                         "algo que nunca llegó a usar"],
        "marco_cartela": ["Qué es: …", "Año: …",
                          "En … , … lo/la … y desde entonces …"],
    },
    "clave": [
        "De vijf voorwerptypes zijn zo gekozen dat ze verschillende werkwoorden uitlokken: usar, "
        "perder, regalar, hacer, llegar a. Samen dekken ze de onregelmatige indefinido-vormen af.",
        "«Algo que nunca llegó a usar» levert altijd het interessantste bijschrift op: het dwingt "
        "tot een verhaal over wat níet gebeurde.",
        "Toets de derde regel van elk bijschrift: staat er een indefinido in, en gaat het om één "
        "afgerond moment? Bijschriften in het presente zijn de meest voorkomende fout.",
        "Vijf is een harde grens. Een zesde voorwerp betekent één te weinig doordacht.",
    ],
    "nota": "Hang de vijf bijschriften echt op in de klas, elk op een A5. De klas loopt de zaal "
            "rond en dat is de presentatie — geen enkele spreekbeurt nodig.",
}

P5_RETO_08 = {
    "id": "C6P-U5-RETO-08", "num": 8, "curso": "C6+", "unidad": P5,
    "seccion": "§4.4", "ancla": "historia_c6p", "soporte": "print",
    "nombre": "Dos versiones del mismo hecho",
    "lente": "🕵️ forensisch", "forma": "👥 En parejas", "skill": "👁️ Leer",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Dos textos, un mismo día, y no coinciden en casi nada.",
    "gancho_nl": "Twee teksten, dezelfde dag, en ze komen bijna nergens overeen.",
    "consigna_es": "Separa lo que es hecho de lo que es interpretación, en las dos versiones.",
    "consigna_nl": "Scheid feit van interpretatie, in beide versies.",
    "regla": "Een feit is wat beide teksten zeggen of wat te controleren valt. Alles wat maar in "
             "één versie staat, is een claim tot bewijs van het tegendeel — ook als het waar klinkt.",
    "pasos": [("Leed las dos versiones enteras.", "Lees beide versies helemaal."),
              ("Subrayad lo que dicen las dos.", "Onderstreep wat beide zeggen."),
              ("Marcad lo que dice solo una.", "Markeer wat maar één zegt."),
              ("Escribid los tres hechos seguros.", "Schrijf de drie zekere feiten op.")],
    "datos": {
        "version_a": [
            "El 12 de octubre de 1954 se inauguró el puente.",
            "Vinieron más de cinco mil personas.",
            "El alcalde habló durante veinte minutos.",
            "Fue el día más importante de la historia del pueblo.",
            "Todo el mundo estaba feliz.",
        ],
        "version_b": [
            "El puente se abrió el 12 de octubre de 1954.",
            "Se calcula que asistieron unas dos mil personas.",
            "El alcalde dio un discurso largo.",
            "Muchos vecinos no fueron: llevaban meses protestando por el precio de la obra.",
            "Aquella tarde llovió y la fiesta terminó pronto.",
        ],
        "marco": ["Las dos versiones dicen que …", "Solo la A dice que …",
                  "Esto es un hecho, porque …", "Esto es interpretación, porque …",
                  "No se puede saber si …"],
    },
    "clave": [
        "Drie zekere feiten: de datum (12 oktober 1954), de opening van de brug, en de lange "
        "toespraak van de burgemeester. Meer is er niet.",
        "Het bezoekersaantal verschilt met een factor 2,5 en is dus geen feit maar een schatting — "
        "let op «se calcula que» in versie B: die tekst geeft zelf toe dat hij schat.",
        "«Todo el mundo estaba feliz» is de zuiverste interpretatie: onmeetbaar én weerlegd door "
        "de protesten in versie B.",
        "De regen staat maar in één versie en is toch waarschijnlijk waar. Bespreek dat: "
        "«alleen in één bron» betekent niet «vals», het betekent «niet bevestigd».",
    ],
    "nota": "Dezelfde oefening werkt met twee echte krantenartikels over vandaag. Doe dat één "
            "keer per jaar; het effect op hoe de klas nieuws leest, is blijvend.",
}

P5_RETO_09 = {
    "id": "C6P-U5-RETO-09", "num": 9, "curso": "C6+", "unidad": P5,
    "seccion": "§1.4", "ancla": "biografia", "soporte": "print",
    "nombre": "La biografía en datos",
    "lente": "🔬 onderzoek & data", "forma": "👥 En parejas", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★☆",
    "gancho_es": "Una vida en ocho cifras. Ni una sola frase bonita.",
    "gancho_nl": "Een leven in acht cijfers. Geen enkele mooie zin.",
    "consigna_es": "Convertid las cifras en una línea del tiempo y en cinco frases en indefinido.",
    "consigna_nl": "Zet de cijfers om in een tijdlijn en in vijf indefinido-zinnen.",
    "regla": "Elke zin bevat één cijfer en één werkwoord in het indefinido. Bijvoeglijke "
             "naamwoorden zijn verboden — geen «grande», geen «famosa». De cijfers doen het werk.",
    "pasos": [("Leed las ocho cifras.", "Lees de acht cijfers."),
              ("Dibujad la línea del tiempo.", "Teken de tijdlijn."),
              ("Escribid cinco frases con cifra e indefinido.",
               "Schrijf vijf zinnen met cijfer en indefinido."),
              ("¿Qué cifra dice más que las otras? ¿Por qué?",
               "Welk cijfer zegt meer dan de andere? Waarom?")],
    "datos": {
        # (soort cijfer, waarde) — een samengesteld portret op basis van
        # publiek bekende ordes van grootte
        "cifras": [("años que vivió", "47"),
                   ("años que pasó en el extranjero", "19"),
                   ("libros que publicó en vida", "6"),
                   ("libros que se publicaron después de morir", "11"),
                   ("lenguas a las que se tradujo", "34"),
                   ("años entre el primer y el segundo libro", "9"),
                   ("veces que cambió de país", "5"),
                   ("edad a la que publicó el primero", "21")],
        "marco": ["Publicó su primer libro a los … años.",
                  "Pasó … de sus … años fuera de su país.",
                  "Entre el primero y el segundo pasaron … años.",
                  "Después de morir se publicaron … libros más.",
                  "Se tradujo a … lenguas."],
    },
    "clave": [
        "Het veelzeggendste cijfer is elf boeken ná zijn dood tegenover zes tijdens zijn leven: "
        "meer dan de helft van zijn werk verscheen postuum. Dat vraagt geen enkel bijvoeglijk "
        "naamwoord.",
        "Negentien van de zevenenveertig jaar in het buitenland is bijna de helft — een tweede "
        "cijfer dat een heel leven samenvat.",
        "Negen jaar tussen boek één en twee is de stilte die de klas zelf moet opmerken. Vraag "
        "wat daar gebeurd kan zijn; er is geen antwoord en dat is het punt.",
        "Toets: vijf zinnen, vijf cijfers, vijf indefinido's, nul bijvoeglijke naamwoorden.",
    ],
    "nota": "Laat de klas daarna hun eigen leven in acht cijfers zetten. Het werkt verrassend "
            "goed en het is meteen de opwarming voor de tarea final.",
}

P5_RETO_03 = {
    "id": "C6P-U5-RETO-03", "num": 3, "curso": "C6+", "unidad": P5,
    "seccion": "§3.4", "ancla": "se_lo", "soporte": "hub",
    "nombre": "Se lo di a…",
    "lente": "🔓 puzzel & escape", "forma": "🏫 Toda la clase", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Cinco objetos recorren la clase. Al final nadie sabe dónde acabaron.",
    "gancho_nl": "Vijf voorwerpen gaan de klas rond. Op het eind weet niemand waar ze belandden.",
    "consigna_es": "Reconstruye quién se lo dio a quién.",
    "consigna_nl": "Reconstrueer wie het aan wie gaf.",
    "regla": "Altijd met «se lo», «se la», «se los» of «se las» — het voorwerp en de persoon "
             "verdwijnen allebei in het pronomen. Wie de naam van het voorwerp nog uitspreekt, "
             "geeft de puzzel weg.",
    "pasos": [("Fíjate en el objeto y en quién lo recibe.",
               "Let op het voorwerp en op wie het krijgt."),
              ("Reconstruye la cadena.", "Reconstrueer de ketting."),
              ("Elige la frase correcta.", "Kies de juiste zin.")],
    "datos": {
        "items": [
            ("Ana tenía el libro y ahora lo tiene Beto. ¿Qué pasó?",
             "Ana se lo dio a Beto.",
             ["Ana se lo dio a Beto.", "Ana lo se dio a Beto.", "Ana le lo dio a Beto."],
             "«le + lo» wordt altijd «se lo» — nooit «le lo», dat bestaat niet"),
            ("Beto tenía las llaves y ahora las tiene Carla.",
             "Beto se las dio a Carla.",
             ["Beto se las dio a Carla.", "Beto se lo dio a Carla.", "Beto las le dio a Carla."],
             "«las llaves» is vrouwelijk meervoud: se las"),
            ("Carla tenía los apuntes y ahora los tienen Diego y Elena.",
             "Carla se los dio a ellos.",
             ["Carla se los dio a ellos.", "Carla les los dio.", "Carla se les dio."],
             "twee ontvangers verandert niets aan «se»: alleen het voorwerp bepaalt lo/la/los/las"),
            ("Diego tenía la foto. Ya no la tiene y Elena tampoco.",
             "Se la dio a otra persona.",
             ["Se la dio a otra persona.", "La se dio a otra persona.",
              "Se lo dio a otra persona."],
             "«la foto» is vrouwelijk enkelvoud: se la"),
            ("Elena tenía el cargador y se lo pidió Ana. ¿Qué le contesta Elena?",
             "Ahora mismo te lo doy.",
             ["Ahora mismo te lo doy.", "Ahora mismo se lo doy.", "Ahora mismo lo te doy."],
             "tegen de persoon zelf is het «te lo», niet «se lo» — «se» is alleen derde persoon"),
            ("Al final del juego, ¿quién tiene el libro?",
             "No se sabe: hay que reconstruir toda la cadena.",
             ["No se sabe: hay que reconstruir toda la cadena.",
              "Beto, porque Ana se lo dio.",
              "Ana, porque era suyo."],
             "Beto kreeg het maar kon het doorgeven; alleen de volledige ketting geeft antwoord"),
        ],
    },
    "clave": [
        "De hele regel in één zin: «le/les + lo/la/los/las» wordt «se + lo/la/los/las». Item 1 "
        "en 3 bewijzen dat het aantal ontvangers niets verandert.",
        "Item 5 is de belangrijkste uitzondering: tegen de persoon zélf is het «te lo». Wie "
        "overal «se lo» zegt, heeft de regel te breed toegepast.",
        "Item 6 is geen grammatica maar logica: het spel is pas opgelost als de hele ketting "
        "klopt. Dat sluit de reto af zoals hij begon.",
    ],
    "nota": "Speel het eerst met echte voorwerpen in de klas, en doe daarna de hub-oefening. De "
            "volgorde maakt het verschil: eerst voelen, dan formaliseren.",
}

P5_RETO_07 = {
    "id": "C6P-U5-RETO-07", "num": 7, "curso": "C6+", "unidad": P5,
    "seccion": "§4.4", "ancla": "historia_c6p", "soporte": "hub",
    "nombre": "Efeméride del día",
    "lente": "📻 mediaformat", "forma": "👤 Solo", "skill": "🗣️ Hablar",
    "tiempo": "± 12 min", "dificultad": "★★☆",
    "gancho_es": "Un día como hoy, en algún sitio del mundo hispano, pasó algo.",
    "gancho_nl": "Op een dag als vandaag gebeurde er ergens in de Spaanstalige wereld iets.",
    "consigna_es": "Graba un flash informativo de treinta segundos sobre esa efeméride.",
    "consigna_nl": "Neem een nieuwsflits van dertig seconden op over die gebeurtenis.",
    "regla": "Dertig seconden, en de vier w's in de eerste zin: qué, quién, cuándo, dónde. De "
             "reden of het gevolg komt pas daarna — een nieuwsflits begint nooit met de uitleg.",
    "pasos": [("Busca qué pasó un día como hoy.",
               "Zoek wat er op een dag als vandaag gebeurde."),
              ("Escribe la primera frase con las cuatro w.",
               "Schrijf de eerste zin met de vier w's."),
              ("Añade dos frases: por qué importó.",
               "Voeg twee zinnen toe: waarom het uitmaakte."),
              ("Graba en treinta segundos. Ni más ni menos.",
               "Neem op in dertig seconden. Niet meer, niet minder.")],
    "datos": {
        "marco": ["Un día como hoy, en … , … .",
                  "Ocurrió en … , y lo protagonizó …",
                  "A partir de ese día, …",
                  "Y por eso hoy se recuerda como …",
                  "Han pasado … años."],
        "verbos": ["ocurrió", "empezó", "terminó", "nació", "murió", "se publicó",
                   "se estrenó", "se firmó", "se descubrió", "cambió"],
    },
    "clave": [
        "De volgorde is de didactiek: eerst het feit, dan de betekenis. Wie begint met «esto fue "
        "muy importante porque…», heeft een opstel gemaakt in plaats van een nieuwsbericht.",
        "De werkwoordenbank staat volledig in het indefinido, derde persoon. Dat is precies de "
        "vorm die de unit oefent, en een nieuwsflits gebruikt geen andere.",
        "«Han pasado … años» is de enige perfecto-zin in het frame en hij is verplicht: hij "
        "verbindt het verleden met vandaag. Dat contrast tussen indefinido en perfecto is de "
        "grammaticale winst.",
        "Toets de dertig seconden en de vier w's in de eerste zin. De rest is inhoud.",
    ],
    "nota": "Maak er een vast ritueel van: elke les één efeméride, één leerling, dertig seconden. "
            "Na twintig lessen heeft de klas een eigen kalender van de Spaanstalige wereld.",
}

P5_RETO_10 = {
    "id": "C6P-U5-RETO-10", "num": 10, "curso": "C6+", "unidad": P5,
    "seccion": "Cultura", "ancla": "cultura_c6p5", "soporte": "hub",
    "nombre": "Cuéntaselo a un niño",
    "lente": "🤝 bemiddelen", "forma": "👤 Solo", "skill": "🔀 Bemiddelen",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "La misma biografía, para alguien de ocho años. Sin mentir y sin aburrir.",
    "gancho_nl": "Dezelfde biografie, voor iemand van acht. Zonder te liegen en zonder te vervelen.",
    "consigna_es": "Elige la versión que un niño entiende sin perder la verdad.",
    "consigna_nl": "Kies de versie die een kind zou begrijpen zonder de waarheid te verliezen.",
    "regla": "Vereenvoudigen is niet weglaten. Elke versie die het moeilijke deel gewoon schrapt, "
             "is fout — ook als ze mooi klinkt.",
    "pasos": [("Lee la frase original.", "Lees de originele zin."),
              ("Piensa qué palabra es la difícil.", "Denk na welk woord het moeilijke is."),
              ("Elige la versión que la explica, no la que la esconde.",
               "Kies de versie die het uitlegt, niet die het verstopt.")],
    "datos": {
        "items": [
            ("«Se exilió en 1939 y no volvió a su país hasta 1977.»",
             "Tuvo que irse de su país porque allí ya no podía vivir seguro. Volvió treinta y "
             "ocho años después.",
             ["Tuvo que irse de su país porque allí ya no podía vivir seguro. Volvió treinta y "
              "ocho años después.",
              "Se fue de viaje muchos años.",
              "Vivió en otro país."],
             "«se fue de viaje» is niet waar: hij had geen keuze, en dat is precies de kern"),
            ("«Su obra fue censurada durante dos décadas.»",
             "Durante veinte años no se pudieron vender sus libros: el gobierno no dejaba.",
             ["Durante veinte años no se pudieron vender sus libros: el gobierno no dejaba.",
              "Sus libros no eran famosos.",
              "No escribió durante veinte años."],
             "de twee andere veranderen het feit; alleen de eerste vertaalt «censurada» in "
             "kindertaal"),
            ("«Recibió un reconocimiento póstumo.»",
             "Le dieron un premio, pero él murió antes.",
             ["Le dieron un premio, pero él murió antes.",
              "Ganó un premio muy tarde.",
              "Fue muy importante después."],
             "«póstumo» heeft geen kinderwoord; je legt het uit met een gewone zin"),
            ("«Fue una figura clave en la reivindicación de los derechos indígenas.»",
             "Trabajó mucho para conseguir los mismos derechos para su pueblo.",
             ["Trabajó mucho para conseguir los mismos derechos para su pueblo.",
              "Ayudó a mucha gente.",
              "Era muy conocida."],
             "«ayudó a mucha gente» klopt maar zegt niets; het waarvóór moet erin blijven"),
        ],
    },
    "clave": [
        "Het patroon van elke goede versie: het moeilijke woord wordt vervangen door een zin, "
        "niet door een vager woord. «Póstumo» → «pero él ya había muerto».",
        "De foute antwoorden zijn zelden onwaar — ze zijn leeg. Dat is het lastigste om te zien "
        "en meteen de belangrijkste vaardigheid van bemiddelen.",
        "De juiste versies staan bewust volledig binnen bereik van de leerling: indefinido plus "
        "infinitief. Vereenvoudigen mag de taal niet moeilijker maken dan het origineel — dat "
        "zou de hele oefening omkeren.",
        "Toets de vier keuzes plus één eigen omzetting van een zin uit de leestekst.",
    ],
    "nota": "Laat het echt uitproberen op een broer of zus van acht. Het antwoord op «snapte "
            "die het?» is eerlijker dan elke rubriek.",
}

P5_RETO_01 = {
    "id": "C6P-U5-RETO-01", "num": 1, "curso": "C6+", "unidad": P5,
    "seccion": "§1.4", "ancla": "biografia", "soporte": "ppt",
    "nombre": "El obituario del héroe anónimo",
    "lente": "✍️ creatieve beperking", "forma": "👤 Solo", "skill": "✍️ Escribir",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "Nunca salió en los periódicos. Y sin embargo cambió algo.",
    "gancho_nl": "Hij haalde nooit de krant. En tóch veranderde hij iets.",
    "consigna_es": "Escribe el obituario de alguien que no fue famoso, en ocho frases.",
    "consigna_nl": "Schrijf het overlijdensbericht van iemand die niet beroemd werd, in acht zinnen.",
    "regla": "Geen beroemdheid, geen uitvinder, geen held. Iemand uit een gewoon leven — en toch "
             "moet je in één zin kunnen zeggen wat er zonder deze persoon níet zou bestaan.",
    "pasos": [("Piensa en alguien real o inventado, pero corriente.",
               "Denk aan iemand echt of verzonnen, maar gewoon."),
              ("Escribe la frase «gracias a él/ella, …».",
               "Schrijf de zin «gracias a él/ella, …»."),
              ("Construye las otras siete alrededor.",
               "Bouw de andere zeven eromheen."),
              ("Léelo en voz alta. ¿Se nota que importó?",
               "Lees hardop voor. Merk je dat hij ertoe deed?")],
    "datos": {
        "ejemplos_de_vida": [("la mujer que abrió la primera biblioteca del barrio", ""),
                             ("el hombre que arregló bicicletas gratis durante cuarenta años", ""),
                             ("la maestra que enseñó a leer a tres generaciones", ""),
                             ("el vecino que plantó todos los árboles de la calle", ""),
                             ("la enfermera del turno de noche que nadie vio nunca", "")],
        "marco": ["Nació en … en …", "Trabajó … años en …",
                  "Nunca … , pero sí …", "Gracias a él/ella, …",
                  "Murió en … , y … personas fueron a despedirlo/-la.",
                  "Hoy … sigue …"],
        "verbos": ["nació", "creció", "empezó", "trabajó", "abrió", "enseñó",
                   "plantó", "arregló", "cuidó", "murió"],
    },
    "clave": [
        "De verplichte zin «gracias a él/ella, …» is het hart: hij dwingt tot een gevolg dat nog "
        "bestaat, en dus tot een contrast tussen indefinido (het leven) en presente (het gevolg).",
        "«Nunca… , pero sí…» is de tweede sleutelzin: hij maakt de anonimiteit expliciet in "
        "plaats van hem te verzwijgen.",
        "De vijf voorbeelden zijn expres alledaags. Wie toch een beroemdheid kiest, heeft de "
        "beperking gemist — en de beperking ís de opdracht.",
        "Toets de acht zinnen, de indefinido-vormen en de aanwezigheid van de gracias-zin.",
    ],
    "nota": "Sommige leerlingen schrijven over een eigen grootouder. Dat mag, en het levert de "
            "beste teksten op — maar niemand hoeft voor te lezen.",
}

P5_RETO_05 = {
    "id": "C6P-U5-RETO-05", "num": 5, "curso": "C6+", "unidad": P5,
    "seccion": "§4.4", "ancla": "historia_c6p", "soporte": "ppt",
    "nombre": "La leyenda mal contada",
    "lente": "✍️ creatieve beperking", "forma": "👥 En parejas", "skill": "🗣️ Hablar",
    "tiempo": "± 15 min", "dificultad": "★★★",
    "gancho_es": "La leyenda está bien. El orden, no.",
    "gancho_nl": "De legende klopt. De volgorde niet.",
    "consigna_es": "Ordenad las ocho partes y contadla con vuestras palabras.",
    "consigna_nl": "Zet de acht delen op volgorde en vertel ze in eigen woorden.",
    "regla": "Bij het navertellen mag je geen enkele zin letterlijk overnemen. Je gebruikt de "
             "conectoren van het verhaal — érase una vez, entonces, al final — en je eigen woorden.",
    "pasos": [("Leed las ocho partes, desordenadas.",
               "Lees de acht delen, door elkaar."),
              ("Ordenadlas. Dos pistas: quién aparece primero y qué causa qué.",
               "Zet ze op volgorde. Twee sporen: wie eerst verschijnt en wat wat veroorzaakt."),
              ("Contadla sin leer, con vuestras palabras.",
               "Vertel ze zonder lezen, in eigen woorden."),
              ("¿Qué explica esta leyenda?", "Wat verklaart deze legende?")],
    "datos": {
        # De legende van de Popocatépetl en de Iztaccíhuatl (México), vrij naverteld
        "partes": [
            ("A", "Érase una vez una princesa, Iztaccíhuatl, y un guerrero, Popocatépetl, "
                  "que se querían."),
            ("B", "El padre de ella aceptó, pero con una condición: volver vencedor de la guerra."),
            ("C", "Popocatépetl pidió permiso para casarse con ella."),
            ("D", "Mientras él estaba lejos, alguien mintió y dijo que había muerto."),
            ("E", "Iztaccíhuatl se murió de tristeza."),
            ("F", "Popocatépetl volvió vencedor y la encontró muerta."),
            ("G", "La llevó a la montaña y se quedó a su lado con una antorcha."),
            ("H", "Por eso hoy hay dos volcanes: uno dormido y otro que todavía echa humo."),
        ],
        "conectores": ["Érase una vez", "Un día", "Entonces", "Mientras tanto",
                       "Cuando volvió", "Desde entonces", "Al final", "Por eso"],
    },
    "clave": [
        "De juiste volgorde is A · C · B · D · E · F · G · H.",
        "De moeilijkste is C vóór B: eerst vraagt hij toestemming, dán stelt de vader zijn "
        "voorwaarde. Wie B eerst zet, keert oorzaak en gevolg om.",
        "H is het slot dat de legende zijn functie geeft: een verklaring voor twee echte vulkanen "
        "naast Mexico-Stad. Zonder H is het een liefdesverhaal, mét H is het een mythe.",
        "Toets het navertellen, niet het ordenen. Wie de volgorde heeft maar voorleest, heeft de "
        "reto niet gedaan.",
        "«Se querían» en «estaba lejos» staan in het imperfecto, de verteltijd van elke "
        "legende. Dat is U6-stof: hier alleen herkennen, en bij het navertellen mag de leerling "
        "ze als vaste formule overnemen. Vraag er geen analyse over.",
    ],
    "nota": "Toon een foto van de twee vulkanen ná het navertellen. De vorm van de Iztaccíhuatl — "
            "«la mujer dormida» — maakt het verhaal in één beeld af.",
}

P5_RETO_06 = {
    "id": "C6P-U5-RETO-06", "num": 6, "curso": "C6+", "unidad": P5,
    "seccion": "§2.4", "ancla": "indefinido", "soporte": "ppt",
    "nombre": "Entrevista al pasado",
    "lente": "🎭 simulatie met beperking", "forma": "🏫 Toda la clase", "skill": "🗣️ Hablar",
    "tiempo": "± 18 min", "dificultad": "★★★",
    "gancho_es": "Una silla, un personaje histórico y toda la clase con preguntas.",
    "gancho_nl": "Eén stoel, één historisch personage en de hele klas met vragen.",
    "consigna_es": "Entrevistad al personaje. Todas las respuestas en indefinido.",
    "consigna_nl": "Interview het personage. Alle antwoorden in het indefinido.",
    "regla": "Het personage antwoordt uitsluitend in het indefinido — hij vertelt afgeronde "
             "feiten, geen gewoontes en geen meningen. Wie «yo creo que» zegt, is uit zijn rol.",
    "pasos": [("Un/a voluntario/-a elige un personaje y se sienta.",
               "Een vrijwilliger kiest een personage en gaat zitten."),
              ("La clase prepara dos preguntas cada uno, en indefinido.",
               "De klas bereidt elk twee vragen voor, in het indefinido."),
              ("Entrevista de cinco minutos. Sin pausas largas.",
               "Interview van vijf minuten. Zonder lange stiltes."),
              ("Cambiad de personaje.", "Wissel van personage."),
              ("¿Qué pregunta ha sido la mejor? ¿Por qué?",
               "Welke vraag was de beste? Waarom?")],
    "datos": {
        "personajes": [("Frida Kahlo", "México, 1907–1954 · pintora"),
                       ("Simón Bolívar", "Venezuela, 1783–1830 · libertador"),
                       ("Rigoberta Menchú", "Guatemala, 1959 · Nobel de la Paz"),
                       ("Violeta Parra", "Chile, 1917–1967 · música"),
                       ("Bartolomé de las Casas", "España, 1484–1566 · cronista"),
                       ("Mercedes Sosa", "Argentina, 1935–2009 · cantante")],
        "preguntas_modelo": ["¿Cuándo salió usted de su país por primera vez?",
                             "¿Qué hizo el día más difícil de su vida?",
                             "¿Quién le ayudó cuando nadie más lo hizo?",
                             "¿De qué decisión se arrepintió después?",
                             "¿Cuándo supo que su trabajo importaba?"],
        "prohibido_al_personaje": ["yo creo que", "normalmente", "siempre hacía",
                                   "hoy en día", "en mi opinión"],
    },
    "clave": [
        "Het verbod op meningen dwingt tot feiten, en feiten dwingen tot het indefinido. Dat is "
        "de hele constructie: de rolregel produceert de grammatica.",
        "Elke modelvraag staat bewust in het indefinido, ook «¿de qué decisión se arrepintió?» — "
        "een vraag in het presente laat het personage meteen uit zijn tijd stappen.",
        "De beste vragen zijn die met «cuándo» en «qué hizo»: ze laten geen ontsnappingsroute "
        "naar het presente.",
        "Toets de vragen van de klas, niet het antwoord van het personage. Twee goede vragen per "
        "leerling is de opdracht.",
    ],
    "nota": "Bereid één personage zelf voor als de klas vastloopt. Vijf minuten in de stoel is "
            "langer dan het lijkt, en een leerkracht die het voordoet, breekt het ijs.",
}

RETOS_C6P_U5 = [P5_RETO_01, P5_RETO_02, P5_RETO_03, P5_RETO_04, P5_RETO_05,
                P5_RETO_06, P5_RETO_07, P5_RETO_08, P5_RETO_09, P5_RETO_10]


RETOS = (RETOS_U0 + RETOS_U1 + RETOS_U2 + RETOS_U3 + RETOS_U4
         + RETOS_U5 + RETOS_U6 + RETOS_U7 + RETOS_U8
         + RETOS_C6P_U0 + RETOS_C6P_U1 + RETOS_C6P_U2
         + RETOS_C6P_U3 + RETOS_C6P_U4 + RETOS_C6P_U5)

# Waar in de printcursus elke sectie eindigt — hier wordt een print-reto ingevoegd.
ANCLAS = ["alfabeto", "sonidos", "sonido_letra", "acento", "numeros", "saludos", "cultura",
          # C5 U1
          "datos", "ser", "presente", "preguntar", "cultura_u1",
          # C5 U2
          "familia", "posesivos", "adjetivos", "ser_estar", "cultura_u2",
          # C5 U3
          "hora", "rutina", "irregular", "cultura_u3",
          # C5 U4
          "gustar", "reacciones", "planes", "cultura_u4",
          # C5 U5 en U6
          "cantidades", "comida", "pedir", "pronombres_u5", "cultura_u5",
          "pronombres_u6", "acabar", "demostrativos", "concordancia_u6", "cultura_u6",
          # C5 U7 en U8
          "hay_estar", "preposiciones", "gerundio", "imperativo", "ordinales", "cultura_u7",
          "perfecto", "participios", "marcadores", "clima", "cultura_u8",
          # C6+ U0
          "saludos_c6p", "presente_c6p", "genero", "paises", "cultura_c6p0",
          # C6+ U1
          "hora_c6p", "rutina_c6p", "reflexivos", "ser_estar_c6p", "cultura_c6p1",
          # C6+ U2
          "casa_c6p", "hay_estar_c6p", "gerundio_c6p", "pronombres_c6p2",
          "barrio_c6p", "cultura_c6p2",
          # C6+ U3
          "movil_c6p", "ir_a_c6p", "oi_c6p", "acabar_c6p", "cultura_c6p3",
          # C6+ U4
          "viaje_c6p", "perfecto_c6p", "por_para", "cultura_c6p4",
          # C6+ U5
          "biografia", "indefinido", "se_lo", "historia_c6p", "cultura_c6p5"]


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
