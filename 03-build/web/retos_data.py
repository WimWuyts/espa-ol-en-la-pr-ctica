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
    "consigna_es": "Escribe tres frases sobre tu día y luego la respuesta que te daría la app.",
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
    "consigna_es": "Elige lo que diría de verdad un/a joven español/-a. Y di por qué la "
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
RETOS = RETOS_U0 + RETOS_U1 + RETOS_U2 + RETOS_U3 + RETOS_U4

# Waar in de printcursus elke sectie eindigt — hier wordt een print-reto ingevoegd.
ANCLAS = ["alfabeto", "sonidos", "sonido_letra", "acento", "numeros", "saludos", "cultura",
          # C5 U1
          "datos", "ser", "presente", "preguntar", "cultura_u1",
          # C5 U2
          "familia", "posesivos", "adjetivos", "ser_estar", "cultura_u2",
          # C5 U3
          "hora", "rutina", "irregular", "cultura_u3",
          # C5 U4
          "gustar", "reacciones", "planes", "cultura_u4"]


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
