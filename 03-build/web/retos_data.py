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

RETOS = [RETO_01, RETO_02, RETO_03, RETO_04, RETO_05,
         RETO_06, RETO_07, RETO_08, RETO_09, RETO_10]

# Waar in de printcursus elke sectie eindigt — hier wordt een print-reto ingevoegd.
ANCLAS = ["alfabeto", "sonidos", "sonido_letra", "acento", "numeros", "saludos", "cultura"]


def por_soporte(soporte):
    return [r for r in RETOS if r["soporte"] == soporte]


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
    nums = sorted(r["num"] for r in RETOS)
    assert nums == list(range(1, 11)), nums


controla()


if __name__ == "__main__":
    print("%-16s %-34s %-7s %-26s %s" % ("id", "nombre", "drager", "lens", "sectie"))
    for r in sorted(RETOS, key=lambda x: x["num"]):
        print("%-16s %-34s %-7s %-26s %s"
              % (r["id"], r["nombre"], r["soporte"], r["lente"], r["seccion"]))
    from collections import Counter
    print("\ndragers:", dict(Counter(r["soporte"] for r in RETOS)))
