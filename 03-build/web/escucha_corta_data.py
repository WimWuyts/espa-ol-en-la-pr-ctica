#!/usr/bin/env python3
"""Korte luisterfragmenten (audiotaken) per cursus en unit — C5 en C6+.

Naast het lange luisterfragment per unit (`escucha_data.py`, de zesdelige
begripsladder) staan er in élke unit kortere audiotaken: microdictados,
klankreeksen, mini-dialogen, weerberichten, wegbeschrijvingen. In print zijn
dat de `audiorow`-blokken met de QR-kaart; op de hub de losse spelers.

Tot nu toe hadden die blokken alleen een etiket («Audio 3.2 · Microdictado ·
0:40») en géén tekst. Dit bestand levert die tekst, met hetzelfde datacontract
als `escucha_data.py`, zodat dezelfde afnemers hem kunnen gebruiken:

  * `gen_audio_elevenlabs.py` / `gen_audio.py` → de mp3 (stem per spreker);
  * de hub → speler + meelees-transcript + browser-TTS-terugval;
  * het docentendossier → de antwoordsleutel (`clave`), die nooit op de
    leerlingpagina hoort (CLAUDE.md §14).

VELDEN per fragment
    id        C5-U3-AUD-02 — cursus, unit, volgnummer
    ancla     ankerpunt op de hub; de QR op papier wijst hiernaartoe
    curso     "C5" | "C6+"          unidad  0–8
    seccion   de sectie in het boek waar het blok staat
    etiqueta  het etiket zoals het NU in de printunit staat (letterlijk, zodat
              print en audio te matchen zijn tijdens de hosting-sweep)
    titulo    korte naam
    tipo      dictado | dialogo | seleccion | lista | indicaciones | informativo
    tarea     wat de leerling doet (NL, kort)
    audio     doelbestand van de mp3
    guion     [{who, es, nl}] — dezelfde vorm als in escucha_data.py
    clave     antwoordsleutel voor het docentendossier
    nota      optioneel: afwijking/waarschuwing voor wie de unit herbouwt

NIVEAU (CLAUDE.md §2). C5 blijft binnen A1 + eerste A2 t.e.m. het perfecto
compuesto. C6+ mag indefinido, imperfecto, por/para, se lo/se la, imperativo en
mening met indicativo. In geen van beide cursussen staat futuro simple,
condicional of subjuntivo — ook niet terloops in een audio.
"""

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def L(who, es, nl):
    """Eén regel van een guion — dezelfde vorm als in escucha_data.py."""
    return {"who": who, "es": es, "nl": nl}


_ORDINAL = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho"]


def _dos_veces(items, who="Narradora"):
    """Dicteerregels: elk item twee keer, met de nummering ertussen.

    Het nummer wordt voluit gezegd («Número tres»), niet als cijfer: TTS-stemmen
    lezen «3.» in een Spaanse context soms als «tercero» of slaan het over.
    """
    guion = []
    for i, (es, nl) in enumerate(items, 1):
        guion.append(L(who, "Número %s." % _ORDINAL[i], "Nummer %d." % i))
        guion.append(L(who, es, nl))
        guion.append(L(who, es, nl))
    return guion


# ===========================================================================
# C5 · U0 — ¡Empezamos!  (parada: el mundo hispano → España)
# ===========================================================================

_ABECEDARIO = [
    ("A", "a", "Ana, casa"), ("B", "be", "Bélgica"), ("C", "ce", "casa, cine"),
    ("D", "de", "dos, dedo"), ("E", "e", "mesa"), ("F", "efe", "foto, café"),
    ("G", "ge", "gato, gente"), ("H", "hache", "hola"), ("I", "i", "isla, sí"),
    ("J", "jota", "Juan, jamón"), ("K", "ka", "kilo"), ("L", "ele", "luna, sol"),
    ("M", "eme", "mamá, mesa"), ("N", "ene", "no, nada"), ("Ñ", "eñe", "España, niño"),
    ("O", "o", "oso, ocho"), ("P", "pe", "papá, Perú"), ("Q", "cu", "queso, aquí"),
    ("R", "erre", "pero, perro"), ("S", "ese", "sí, mesa"), ("T", "te", "té, tú"),
    ("U", "u", "uno, luna"), ("V", "uve", "vino, Sevilla"), ("W", "uve doble", "wifi"),
    ("X", "equis", "taxi, examen"), ("Y", "ye", "yo, hoy"), ("Z", "zeta", "zapato, luz"),
]

C5_U0_01 = {
    "id": "C5-U0-AUD-01", "ancla": "c5-u0-aud-01", "curso": "C5", "unidad": 0,
    "seccion": "§1 · El alfabeto y la pronunciación",
    "etiqueta": "Audio 1.1 · Abecedario · 0:40",
    "titulo": "El abecedario — letra, nombre y ejemplo",
    "tipo": "lista",
    "tarea": "Luister één keer en volg met je vinger; nog niet schrijven.",
    "audio": "audio/C5_U0_01.mp3",
    "guion": [L("Narradora", "El abecedario español. Veintisiete letras.",
                "Het Spaanse alfabet. Zevenentwintig letters.")]
             # geen NL-steun per letter: «A — heet a — Ana, casa» voegt niets toe
             # en zou het transcript op de hub met een kolom ruis vullen
             + [L("Narradora", "%s — se llama «%s» — %s." % (le, nom, ej), "")
                for le, nom, ej in _ABECEDARIO]
             + [L("Narradora", "Y recuerda: la hache no suena. Hola, hasta luego.",
                  "En denk eraan: de h hoor je niet. Hola, hasta luego.")],
    "clave": ["Geen schrijfopdracht — enkel meelezen; de tabel in §1 is het antwoord."],
    "nota": "Volgorde en voorbeelden komen letterlijk uit de alfabettabel in §1; "
            "wijzigt de tabel, wijzig dan ook dit guion.",
}

C5_U0_02 = {
    "id": "C5-U0-AUD-02", "ancla": "c5-u0-aud-02", "curso": "C5", "unidad": 0,
    "seccion": "§1.3 · Microdictado",
    "etiqueta": "Audio 1.3 · Microdictado · 0:50",
    "titulo": "Microdictado — seis palabras",
    "tipo": "dictado",
    "tarea": "Zes woorden, elk twee keer, met een pauze. De beginletter staat in het boek.",
    "audio": "audio/C5_U0_02.mp3",
    "guion": [L("Narradora", "Microdictado. Seis palabras. Cada palabra, dos veces.",
                "Microdictee. Zes woorden. Elk woord twee keer.")]
             + _dos_veces([
                 ("jamón", "ham"), ("gente", "mensen"), ("guitarra", "gitaar"),
                 ("España", "Spanje"), ("queso", "kaas"), ("plaza", "plein"),
             ]),
    "clave": ["1. jamón", "2. gente", "3. guitarra", "4. España", "5. queso", "6. plaza"],
    "nota": "De zes woorden zijn gekozen op de beginletters die in het boek al gedrukt "
            "staan (j · g · g · E · q · p) én dekken samen de klankregels van §1.2: "
            "j-keelklank, ge = jota, gui = harde g, ñ, que = k, za = th/s.",
}

C5_U0_03 = {
    "id": "C5-U0-AUD-03", "ancla": "c5-u0-aud-03", "curso": "C5", "unidad": 0,
    "seccion": "§2 · Taller de lengua — el acento",
    "etiqueta": "Audio 2.1 · Acento — contexto · 0:35",
    "titulo": "La sílaba tónica — siente el golpe",
    "tipo": "lista",
    "tarea": "Luister en klap op de sterke lettergreep; nog geen regel lezen.",
    "audio": "audio/C5_U0_03.mp3",
    "guion": [L("Narradora", "Escucha y siente el golpe. Cada palabra, dos veces.",
                "Luister en voel de klap. Elk woord twee keer.")]
             + _dos_veces([
                 ("café", "koffie"), ("casa", "huis"), ("México", "Mexico"),
                 ("teléfono", "telefoon"), ("Perú", "Peru"), ("número", "getal"),
             ])
             + [L("Narradora", "Cada palabra tiene una sílaba fuerte. Solo una.",
                  "Elk woord heeft één sterke lettergreep. Maar één.")],
    "clave": ["café → fé (laatste)", "casa → ca (voorlaatste)", "México → Mé (derde van achteren)",
              "teléfono → lé (derde van achteren)", "Perú → rú (laatste)",
              "número → nú (derde van achteren)"],
    "nota": "Dezelfde zes woorden als de tabel in §2, in dezelfde volgorde.",
}

C5_U0_04 = {
    "id": "C5-U0-AUD-04", "ancla": "c5-u0-aud-04", "curso": "C5", "unidad": 0,
    "seccion": "§3 · Números 0–100",
    "etiqueta": "Audio 3.1 · Números 0–100 · 1:10",
    "titulo": "Los números en tres capas",
    "tipo": "lista",
    "tarea": "Luister eerst naar het getal, kijk daarna pas naar de vertaling.",
    "audio": "audio/C5_U0_04.mp3",
    "guion": [
        L("Narradora", "Capa uno: del cero al quince.", "Laag één: van nul tot vijftien."),
        L("Narradora", "Cero, uno, dos, tres, cuatro, cinco.", "Nul, één, twee, drie, vier, vijf."),
        L("Narradora", "Seis, siete, ocho, nueve, diez.", "Zes, zeven, acht, negen, tien."),
        L("Narradora", "Once, doce, trece, catorce, quince.", "Elf, twaalf, dertien, veertien, vijftien."),
        L("Narradora", "Capa dos: del dieciséis al veintinueve. Todo junto, una sola palabra.",
          "Laag twee: van zestien tot negenentwintig. Aan elkaar, één woord."),
        L("Narradora", "Dieciséis, diecisiete, dieciocho, diecinueve, veinte.",
          "Zestien, zeventien, achttien, negentien, twintig."),
        L("Narradora", "Veintiuno, veintidós, veintitrés, veinticuatro, veinticinco.",
          "Eenentwintig, tweeëntwintig, drieëntwintig, vierentwintig, vijfentwintig."),
        L("Narradora", "Veintiséis, veintisiete, veintiocho, veintinueve.",
          "Zesentwintig, zevenentwintig, achtentwintig, negenentwintig."),
        L("Narradora", "Capa tres: las decenas, desde treinta.", "Laag drie: de tientallen, vanaf dertig."),
        L("Narradora", "Treinta, cuarenta, cincuenta, sesenta.", "Dertig, veertig, vijftig, zestig."),
        L("Narradora", "Setenta, ochenta, noventa, cien.", "Zeventig, tachtig, negentig, honderd."),
        L("Narradora", "Y la máquina: decena, «y», unidad.", "En de machine: tiental, «y», eenheid."),
        L("Narradora", "Treinta y cinco. Cuarenta y dos. Noventa y nueve.",
          "Vijfendertig. Tweeënveertig. Negenennegentig."),
    ],
    "clave": ["Geen schrijfopdracht — de tabellen in §3 zijn het antwoord."],
}

C5_U0_05 = {
    "id": "C5-U0-AUD-05", "ancla": "c5-u0-aud-05", "curso": "C5", "unidad": 0,
    "seccion": "§4 · Saludos, presentarse y lengua de clase",
    "etiqueta": "Audio 4.1 · Saludos & chunks · 1:10",
    "titulo": "Los chunks: saludar, presentarse, lengua de clase",
    "tipo": "lista",
    "tarea": "Luister naar elke rij en herhaal hardop; eerst het ritme, dan het woord.",
    "audio": "audio/C5_U0_05.mp3",
    "guion": [
        L("Narradora", "Bloque a: saludar y despedirse.", "Blok a: groeten en afscheid nemen."),
        L("Lucía", "¡Hola!", "Hallo!"),
        L("Lucía", "Buenos días.", "Goedemorgen."),
        L("Lucía", "Buenas tardes.", "Goeiemiddag."),
        L("Lucía", "Buenas noches.", "Goedenavond."),
        L("Lucía", "¿Qué tal? ¿Cómo estás?", "Hoe gaat het? Hoe gaat het met je?"),
        L("Diego", "Muy bien, gracias. ¿Y tú?", "Heel goed, dank je. En jij?"),
        L("Diego", "Adiós. Hasta luego. Hasta mañana.", "Dag. Tot straks. Tot morgen."),
        L("Diego", "Chao.", "Doei."),
        L("Narradora", "Bloque b: presentarse.", "Blok b: jezelf voorstellen."),
        L("Lucía", "Me llamo Lucía. Soy Lucía.", "Ik heet Lucía. Ik ben Lucía."),
        L("Lucía", "¿Cómo te llamas?", "Hoe heet jij?"),
        L("Diego", "Encantado.", "Aangenaam. (jongen)"),
        L("Lucía", "Encantada. Mucho gusto. Igualmente.", "Aangenaam. (meisje) Aangenaam. Insgelijks."),
        L("Lucía", "Este es Diego. Esta es Lucía.", "Dit is Diego. Dit is Lucía."),
        L("Diego", "Soy de Bélgica.", "Ik kom uit België."),
        L("Narradora", "Bloque c: la lengua de clase.", "Blok c: de klastaal."),
        L("Diego", "¿Cómo se dice «rugzak» en español?", "Hoe zeg je «rugzak» in het Spaans?"),
        L("Lucía", "¿Qué significa «mochila»?", "Wat betekent «mochila»?"),
        L("Diego", "No entiendo.", "Ik begrijp het niet."),
        L("Lucía", "¿Puedes repetir, por favor?", "Kun je herhalen, alsjeblieft?"),
        L("Diego", "Más despacio, por favor.", "Trager, alsjeblieft."),
        L("Lucía", "No sé. ¿Cómo se escribe?", "Ik weet het niet. Hoe schrijf je dat?"),
        L("Diego", "Tengo una pregunta.", "Ik heb een vraag."),
    ],
    "clave": ["Geen schrijfopdracht — nazeggen. De drie tabellen in §4 zijn het antwoord."],
}

C5_U0_06 = {
    "id": "C5-U0-AUD-06", "ancla": "c5-u0-aud-06", "curso": "C5", "unidad": 0,
    "seccion": "§4.3 · La dialoogkaart",
    "etiqueta": "Audio 4.3 · Diálogo modelo · 0:35",
    "titulo": "Lucía y Tú se conocen",
    "tipo": "dialogo",
    "tarea": "Waar begint en eindigt het gesprek? Onderstreep de chunk waarmee Lucía "
             "op «Soy Tom» reageert.",
    "audio": "audio/C5_U0_06.mp3",
    "guion": [
        L("Lucía", "¡Hola! Buenos días. Me llamo Lucía. ¿Y tú, cómo te llamas?",
          "Hallo! Goedemorgen. Ik heet Lucía. En jij, hoe heet jij?"),
        L("Tú", "Hola, buenos días. Soy Tom. Soy de Bélgica.",
          "Hallo, goedemorgen. Ik ben Tom. Ik kom uit België."),
        L("Lucía", "¡Encantada, Tom!", "Aangenaam, Tom!"),
        L("Tú", "Igualmente. ¿Qué tal?", "Insgelijks. Hoe gaat het?"),
        L("Lucía", "Muy bien, gracias. ¡Hasta luego!", "Heel goed, dank je. Tot straks!"),
        L("Tú", "¡Adiós!", "Dag!"),
    ],
    "clave": ["Begin: «¡Hola! Buenos días.» — Einde: «¡Adiós!»",
              "Reactie op «Soy Tom» = «¡Encantada, Tom!»",
              "Route: saludar → presentarse → preguntar el nombre → reaccionar → despedirse"],
    "nota": "Letterlijk het dialoogje dat in §4.3 gedrukt staat.",
}

C5_U0_07 = {
    "id": "C5-U0-AUD-07", "ancla": "c5-u0-aud-07", "curso": "C5", "unidad": 0,
    "seccion": "Cultura viva · A.2 — el seseo",
    "etiqueta": "Audio A.2 · seseo/ceceo · 0:25",
    "titulo": "Las mismas palabras, dos pronunciaciones",
    "tipo": "lista",
    "tarea": "Dezelfde drie woorden twee keer: eerst met /θ/, dan met /s/. Kies er één "
             "en blijf consequent.",
    "audio": "audio/C5_U0_07.mp3",
    "guion": [
        L("Narradora", "Primero, el centro y el norte de España.",
          "Eerst het midden en het noorden van Spanje."),
        L("Voz_España", "Gracias. Cinco. Plaza.", "Gracias. Cinco. Plaza. (met th-klank)"),
        L("Narradora", "Ahora, América y el sur de España.",
          "Nu Latijns-Amerika en het zuiden van Spanje."),
        L("Voz_América", "Gracias. Cinco. Plaza.", "Gracias. Cinco. Plaza. (met s-klank)"),
        L("Narradora", "Las dos son correctas. Elige una y sé constante.",
          "Allebei zijn correct. Kies er één en blijf consequent."),
    ],
    "clave": ["Geen fout antwoord — het vakje ☐ «gra-th-ias» of ☐ «gra-s-ias» is een keuze, "
              "geen toets."],
    "nota": "Vergt twee verschillende stemmen: één peninsulaire (es-ES) en één "
            "Latijns-Amerikaanse (es-MX/es-US). Zet dat zo in de stemtoewijzing.",
}

C5_U0_08 = {
    "id": "C5-U0-AUD-08", "ancla": "c5-u0-aud-08", "curso": "C5", "unidad": 0,
    "seccion": "Tarea final · A.3 — modelo",
    "etiqueta": "Audio A.3 · Modelo tarjeta · 0:35",
    "titulo": "Modelo — «Tú» en la puerta de embarque",
    "tipo": "dialogo",
    "tarea": "Volg de drie stappen: deletrear · saludar · una pregunta de clase.",
    "audio": "audio/C5_U0_08.mp3",
    "guion": [
        L("Lucía", "¡Hola! Buenos días. Yo soy Lucía. ¿Y tú?",
          "Hallo! Goedemorgen. Ik ben Lucía. En jij?"),
        L("Tú", "¡Hola! Buenos días. Yo soy Sam.", "Hallo! Goedemorgen. Ik ben Sam."),
        L("Lucía", "¿Cómo se escribe?", "Hoe schrijf je dat?"),
        L("Tú", "Ese, a, eme. Sam.", "S, a, m. Sam."),
        L("Tú", "Una pregunta: ¿cómo se dice «rugzak» en español?",
          "Een vraag: hoe zeg je «rugzak» in het Spaans?"),
        L("Lucía", "Se dice «la mochila».", "Dat is «la mochila»."),
        L("Tú", "¡Gracias! ¡Hasta luego!", "Dank je! Tot straks!"),
    ],
    "clave": ["De drie doelen van de tarea zitten in het model: spellen («Ese, a, eme»), "
              "groeten («¡Hola! Buenos días»), klasvraag («¿cómo se dice…?»)."],
    "nota": "Letterlijk het model dat in de tarea final gedrukt staat.",
}


def _deck_vocab(curso, unidad, path, etiqueta, ancla, ident, seccion, audio):
    """Vocabulariodeck: het guion is de woordenlijst zelf — woord + voorbeeldzin.

    Niet met de hand overgeschreven: de lijst staat al in `u<N>_vocab.json` en
    zou anders twee keer onderhouden moeten worden.
    """
    with open(path, encoding="utf-8") as fh:
        items = json.load(fh)
    guion = []
    grupo_actual = None
    for it in items:
        if it.get("grp") != grupo_actual:
            grupo_actual = it.get("grp")
            guion.append(L("Narradora", "Bloque: %s." % grupo_actual,
                           "Blok: %s." % grupo_actual))
        guion.append(L("Narradora", it["es"], it["nl"]))
        if it.get("ej"):
            guion.append(L("Narradora", it["ej"], ""))
    return {
        "id": ident, "ancla": ancla, "curso": curso, "unidad": unidad,
        "seccion": seccion, "etiqueta": etiqueta,
        "titulo": "Decks de vocabulario", "tipo": "lista",
        "tarea": "Luister eerst het hele bloque, dan pas woord per woord.",
        "audio": audio,
        "guion": guion,
        "clave": ["Geen schrijfopdracht — de vocabulariotabellen zijn het antwoord."],
        "nota": "Guion wordt bij import opgebouwd uit %s (%d items); pas de json aan, "
                "niet dit bestand." % (os.path.basename(path), len(items)),
    }


C5_U0_09 = _deck_vocab(
    "C5", 0, os.path.join(ROOT, "01-cursussen", "05-a1", "U0", "u0_vocab.json"),
    "Audio V · Decks A–E · 5:00", "c5-u0-aud-09", "C5-U0-AUD-09",
    "§V · Vocabulario", "audio/C5_U0_09.mp3")


# ===========================================================================
# C5 · U1 — ¿Quién eres?  (parada: Madrid)
# ===========================================================================

C5_U1_01 = {
    "id": "C5-U1-AUD-01", "ancla": "c5-u1-aud-01", "curso": "C5", "unidad": 1,
    "seccion": "§1 · Tus datos personales",
    "etiqueta": "Audio 1.1 · Datos · 0:55",
    "titulo": "Cuatro personas, un dato que falta",
    "tipo": "seleccion",
    "tarea": "Vier korte voorstellingen. Elke persoon vergeet één gegeven — noteer welk.",
    "audio": "audio/C5_U1_01.mp3",
    "guion": [
        L("Narradora", "Cuatro personas se presentan. ¿Qué dato falta?",
          "Vier personen stellen zich voor. Welk gegeven ontbreekt?"),
        L("Narradora", "Número uno.", "Nummer één."),
        L("Marta", "Hola, me llamo Marta. Tengo quince años y vivo en Madrid.",
          "Hallo, ik heet Marta. Ik ben vijftien en ik woon in Madrid."),
        L("Narradora", "Número dos.", "Nummer twee."),
        L("Andrés", "Buenas. Soy Andrés, soy de Colombia y vivo en Cartagena.",
          "Hoi. Ik ben Andrés, ik kom uit Colombia en ik woon in Cartagena."),
        L("Narradora", "Número tres.", "Nummer drie."),
        L("Yuki", "Hola. Me llamo Yuki, tengo diecisiete años y hablo japonés y español.",
          "Hallo. Ik heet Yuki, ik ben zeventien en ik spreek Japans en Spaans."),
        L("Narradora", "Número cuatro.", "Nummer vier."),
        L("Tom", "¡Hola! Soy Tom, soy de Bélgica y vivo en Gante.",
          "Hallo! Ik ben Tom, ik kom uit België en ik woon in Gent."),
    ],
    "clave": [
        "1. Marta — falta el país (nombre ✓ edad 15 ✓ ciudad Madrid ✓)",
        "2. Andrés — falta la edad (nombre ✓ país Colombia ✓ ciudad Cartagena ✓)",
        "3. Yuki — falta el país (nombre ✓ edad 17 ✓ lenguas japonés/español ✓)",
        "4. Tom — falta la edad (nombre ✓ país Bélgica ✓ ciudad Gante ✓)",
    ],
    "nota": "Bewust afwisselend país / edad / país / edad, zodat de leerling écht moet "
            "luisteren en niet één patroon kan doorzetten.",
}

C5_U1_02 = {
    "id": "C5-U1-AUD-02", "ancla": "c5-u1-aud-02", "curso": "C5", "unidad": 1,
    "seccion": "§2 · El verbo SER + los pronombres",
    "etiqueta": "Audio 2.1 · Ser · 0:45",
    "titulo": "Seis frases con «ser» — ¿qué persona?",
    "tipo": "seleccion",
    "tarea": "Kruis per zin aan welke persoon je hoort.",
    "audio": "audio/C5_U1_02.mp3",
    "guion": [
        L("Narradora", "Seis frases. ¿Qué persona oyes?", "Zes zinnen. Welke persoon hoor je?"),
        L("Narradora", "Uno.", "Eén."),
        L("Voz", "Soy de Bélgica.", "Ik kom uit België."),
        L("Narradora", "Dos.", "Twee."),
        L("Voz", "Marta es española.", "Marta is Spaans."),
        L("Narradora", "Tres.", "Drie."),
        L("Voz", "Somos estudiantes.", "Wij zijn studenten."),
        L("Narradora", "Cuatro.", "Vier."),
        L("Voz", "¿Eres de Madrid?", "Kom jij uit Madrid?"),
        L("Narradora", "Cinco.", "Vijf."),
        L("Voz", "Mis primos son de Perú.", "Mijn neven komen uit Peru."),
        L("Narradora", "Seis.", "Zes."),
        L("Voz", "Soy alumna de cuarto.", "Ik ben leerlinge van het vierde jaar."),
    ],
    "clave": ["1. yo", "2. él/ella", "3. nosotros", "4. tú", "5. ellos", "6. yo"],
    "nota": "Het rooster van oefening 3 telt zes rijen, gelijk aan de zes zinnen hier "
            "(rechtgezet 2026-08-08; het stond eerder op vier).",
}

C5_U1_03 = {
    "id": "C5-U1-AUD-03", "ancla": "c5-u1-aud-03", "curso": "C5", "unidad": 1,
    "seccion": "§3 · El presente regular",
    "etiqueta": "Audio 3.2 · Microdictado · 0:40",
    "titulo": "Microdictado — tres frases en presente",
    "tipo": "dictado",
    "tarea": "Reconstrueer de drie zinnen; maak daarna één eigen variant.",
    "audio": "audio/C5_U1_03.mp3",
    "guion": [L("Narradora", "Microdictado. Tres frases, cada una dos veces.",
                "Microdictee. Drie zinnen, elk twee keer.")]
             + _dos_veces([
                 ("Hablo neerlandés y un poco de español.",
                  "Ik spreek Nederlands en een beetje Spaans."),
                 ("Mi hermana estudia en Madrid.", "Mijn zus studeert in Madrid."),
                 ("Vivimos en una ciudad pequeña.", "Wij wonen in een kleine stad."),
             ]),
    "clave": ["1. Hablo neerlandés y un poco de español.",
              "2. Mi hermana estudia en Madrid.",
              "3. Vivimos en una ciudad pequeña."],
    "nota": "Eén zin per vervoegingsgroep: -ar (hablar), -ar (estudiar, 3e p.) en -ir (vivir, "
            "1e p. mv.), zodat het dictee de tabel van §3 dekt.",
}


# ===========================================================================
# C5 · U2 — Mi gente  (parada: Andalucía / Sevilla)
# ===========================================================================

C5_U2_01 = {
    "id": "C5-U2-AUD-01", "ancla": "c5-u2-aud-01", "curso": "C5", "unidad": 2,
    "seccion": "§1 · La familia + tener",
    "etiqueta": "Audio 1 · Mi familia · 0:45",
    "titulo": "Lucía presenta a su familia",
    "tipo": "informativo",
    "tarea": "Noteer hoeveel broers/zussen, neven/nichten, huisdieren en grootouders ze heeft.",
    "audio": "audio/C5_U2_01.mp3",
    "guion": [
        L("Lucía", "¡Hola! Soy Lucía y vivo en Sevilla. Esta es mi familia.",
          "Hallo! Ik ben Lucía en ik woon in Sevilla. Dit is mijn familie."),
        L("Lucía", "En mi casa somos cinco: mi madre, mi padre, mis dos hermanos y yo.",
          "Bij ons thuis zijn we met vijf: mijn moeder, mijn vader, mijn twee broers en ik."),
        L("Lucía", "Mis hermanos se llaman Marco y Ana. Marco tiene veinte años y Ana tiene ocho.",
          "Mijn broer en zus heten Marco en Ana. Marco is twintig en Ana is acht."),
        L("Lucía", "Tengo cuatro primos: tres en Sevilla y uno en Málaga.",
          "Ik heb vier neven en nichten: drie in Sevilla en één in Málaga."),
        L("Lucía", "También tengo una mascota, un perro pequeño. Se llama Curro.",
          "Ik heb ook een huisdier, een klein hondje. Hij heet Curro."),
        L("Lucía", "Y mis abuelos: tengo tres. Mi abuela Rosa vive con nosotros.",
          "En mijn grootouders: ik heb er drie. Mijn oma Rosa woont bij ons."),
        L("Lucía", "¿Y tú? ¿Cuántos hermanos tienes?", "En jij? Hoeveel broers en zussen heb jij?"),
    ],
    "clave": ["hermanos: 2 (Marco 20, Ana 8)", "primos: 4", "mascota: 1 perro (Curro)",
              "abuelos: 3 (abuela Rosa woont bij hen in)"],
}

C5_U2_02 = {
    "id": "C5-U2-AUD-02", "ancla": "c5-u2-aud-02", "curso": "C5", "unidad": 2,
    "seccion": "§1 · Dictado preparado",
    "etiqueta": "Audio 1b · Dictado · 0:40",
    "titulo": "Dictado preparado — la familia de Lucía",
    "tipo": "dictado",
    "tarea": "Schrijf de vier zinnen; luister daarna opnieuw en herhaal elke zin hardop.",
    "audio": "audio/C5_U2_02.mp3",
    "guion": [L("Narradora", "Cuatro frases. Cada frase, dos veces.",
                "Vier zinnen. Elke zin twee keer.")]
             + _dos_veces([
                 ("Lucía tiene dos hermanos.", "Lucía heeft twee broers en zussen."),
                 ("Su abuela se llama Rosa.", "Haar oma heet Rosa."),
                 ("Tienen un perro pequeño.", "Ze hebben een klein hondje."),
                 ("Mis primos viven en Málaga.", "Mijn neven en nichten wonen in Málaga."),
             ]),
    "clave": ["1. Lucía tiene dos hermanos.", "2. Su abuela se llama Rosa.",
              "3. Tienen un perro pequeño.", "4. Mis primos viven en Málaga."],
    "nota": "Dezelfde opname dient twee blokken: het dictee (oefening 10) en het «repite en "
            "voz alta»-blok eronder. Namen met klemtoon (Lucía, Rosa, Málaga) zitten er "
            "bewust in.",
}


# ===========================================================================
# C5 · U3 — El tiempo vuela  (parada: Barcelona)
# ===========================================================================

C5_U3_01 = {
    "id": "C5-U3-AUD-01", "ancla": "c5-u3-aud-01", "curso": "C5", "unidad": 3,
    "seccion": "§1 · La hora",
    "etiqueta": "Audio 1.2 · La hora · 0:50",
    "titulo": "Cinco horas",
    "tipo": "dictado",
    "tarea": "Teken de wijzers of noteer de vijf tijden.",
    "audio": "audio/C5_U3_01.mp3",
    "guion": [L("Narradora", "Cinco horas. Cada hora, dos veces.",
                "Vijf tijdstippen. Elk tijdstip twee keer.")]
             + _dos_veces([
                 ("Son las tres y media.", "Het is half vier."),
                 ("Es la una y cuarto.", "Het is kwart over één."),
                 ("Son las nueve menos cuarto.", "Het is kwart voor negen."),
                 ("Son las siete en punto.", "Het is precies zeven uur."),
                 ("Son las diez y veinte.", "Het is tien over tien."),
             ]),
    "clave": ["1. 3:30 — son las tres y media", "2. 1:15 — es la una y cuarto",
              "3. 8:45 — son las nueve menos cuarto", "4. 7:00 — son las siete en punto",
              "5. 10:20 — son las diez y veinte"],
    "nota": "Item 2 staat er bewust in: «es la una» is de enige enkelvoudsvorm — dat is de "
            "valstrik die oefening 6 («¿es la o son las?») nodig heeft.",
}

C5_U3_02 = {
    "id": "C5-U3-AUD-02", "ancla": "c5-u3-aud-02", "curso": "C5", "unidad": 3,
    "seccion": "§3 · Presente irregular — cambio de raíz",
    "etiqueta": "Audio 3.3 · Microdictado · 0:45",
    "titulo": "Microdictado — el día de Pau",
    "tipo": "dictado",
    "tarea": "Reconstrueer de drie zinnen over de dag van Pau; maak daarna je eigen variant.",
    "audio": "audio/C5_U3_02.mp3",
    "guion": [L("Narradora", "Tres frases sobre el día de Pau. Cada frase, dos veces.",
                "Drie zinnen over de dag van Pau. Elke zin twee keer.")]
             + _dos_veces([
                 ("Pau empieza las clases a las ocho.", "Pau begint de les om acht uur."),
                 ("Después de comer puede descansar un poco.",
                  "Na het eten kan hij een beetje rusten."),
                 ("Por la noche duerme ocho horas.", "'s Nachts slaapt hij acht uur."),
             ]),
    "clave": ["1. Pau empieza las clases a las ocho.  (e → ie)",
              "2. Después de comer puede descansar un poco.  (o → ue)",
              "3. Por la noche duerme ocho horas.  (o → ue)"],
    "nota": "Dekt twee van de drie «botas» uit §3 (e→ie, o→ue). De derde (e→i, pedir) komt in "
            "oefening 7 aan bod, niet in het dictee — anders wordt het te dicht voor 45 s.",
}


# ===========================================================================
# C5 · U4 — Me gusta  (parada: València / la costa)
# ===========================================================================

C5_U4_01 = {
    "id": "C5-U4-AUD-01", "ancla": "c5-u4-aud-01", "curso": "C5", "unidad": 4,
    "seccion": "§1 · Me gusta(n) · gustar & encantar",
    "etiqueta": "Audio 4.1 · Gustos · 0:55",
    "titulo": "Tres jóvenes y sus gustos",
    "tipo": "informativo",
    "tarea": "Noteer per persoon één gusto.",
    "audio": "audio/C5_U4_01.mp3",
    "guion": [
        L("Narradora", "Tres jóvenes hablan de sus gustos.",
          "Drie jongeren praten over wat ze leuk vinden."),
        L("Narradora", "Número uno: Bea.", "Nummer één: Bea."),
        L("Bea", "A mí me encantan los conciertos. También me gusta la playa, "
                "pero no me gusta madrugar.",
          "Ik ben dol op concerten. Ik hou ook van het strand, maar vroeg opstaan vind ik niets."),
        L("Narradora", "Número dos: Diego.", "Nummer twee: Diego."),
        L("Diego", "A mí me gusta mucho el fútbol. Me encanta jugar los sábados. "
                  "No me gustan las series largas.",
          "Ik hou heel erg van voetbal. Ik vind het geweldig om op zaterdag te spelen. "
          "Lange series vind ik niets."),
        L("Narradora", "Número tres: Nina.", "Nummer drie: Nina."),
        L("Nina", "A mí me gusta escuchar música y me encantan las montañas. "
                 "No me gusta el ruido de la ciudad.",
          "Ik hou van muziek luisteren en ik ben dol op de bergen. "
          "Het lawaai van de stad vind ik niets."),
    ],
    "clave": ["Bea → los conciertos (me encantan) / la playa (me gusta)",
              "Diego → el fútbol, jugar los sábados",
              "Nina → escuchar música, las montañas",
              "Extra: elke spreker zegt ook één «no me gusta» — bruikbaar als tweede ronde."],
    "nota": "Elke spreker gebruikt bewust zowel een enkelvoud (gusta) als een meervoud "
            "(gustan), zodat de opname ook oefening 4 (concordancia) voedt.",
}

C5_U4_02 = {
    "id": "C5-U4-AUD-02", "ancla": "c5-u4-aud-02", "curso": "C5", "unidad": 4,
    "seccion": "§2 · también / tampoco · a mí sí / a mí no",
    "etiqueta": "Audio 4.2 · Reacciones · 0:50",
    "titulo": "Seis mini-diálogos — ¿qué reacción?",
    "tipo": "seleccion",
    "tarea": "Kruis per dialoog aan: también / tampoco / a mí sí / a mí no.",
    "audio": "audio/C5_U4_02.mp3",
    "guion": [
        L("Narradora", "Seis mini-diálogos. ¿Qué reacción oyes?",
          "Zes minidialogen. Welke reactie hoor je?"),
        L("Narradora", "Uno.", "Eén."),
        L("Bea", "Me gusta el mar.", "Ik hou van de zee."),
        L("Diego", "A mí también.", "Ik ook."),
        L("Narradora", "Dos.", "Twee."),
        L("Diego", "No me gusta el frío.", "Ik hou niet van kou."),
        L("Nina", "A mí tampoco.", "Ik ook niet."),
        L("Narradora", "Tres.", "Drie."),
        L("Nina", "Me gustan las mates.", "Ik hou van wiskunde."),
        L("Bea", "A mí no.", "Ik niet."),
        L("Narradora", "Cuatro.", "Vier."),
        L("Bea", "No me gustan los lunes.", "Ik hou niet van maandagen."),
        L("Diego", "Pues a mí sí.", "Nou, ik wel."),
        L("Narradora", "Cinco.", "Vijf."),
        L("Diego", "Me encanta bailar.", "Ik ben dol op dansen."),
        L("Nina", "A mí también.", "Ik ook."),
        L("Narradora", "Seis.", "Zes."),
        L("Nina", "No me gusta madrugar.", "Ik hou niet van vroeg opstaan."),
        L("Bea", "A mí sí, me encanta la mañana.", "Ik wel, ik ben dol op de ochtend."),
    ],
    "clave": ["1. también", "2. tampoco", "3. a mí no", "4. a mí sí",
              "5. también", "6. a mí sí"],
    "nota": "Het rooster van oefening 3 telt zes rijen, gelijk aan de zes mini-dialogen hier "
            "(rechtgezet 2026-08-08; het stond eerder op vier).",
}

C5_U4_03 = {
    "id": "C5-U4-AUD-03", "ancla": "c5-u4-aud-03", "curso": "C5", "unidad": 4,
    "seccion": "§3 · Proponer un plan · querer / poder + quedar",
    "etiqueta": "Audio 4.3 · Planes · 0:45",
    "titulo": "Microdictado — tres propuestas",
    "tipo": "dictado",
    "tarea": "Schrijf de drie voorstellen op.",
    "audio": "audio/C5_U4_03.mp3",
    "guion": [L("Narradora", "Tres propuestas. Cada una, dos veces.",
                "Drie voorstellen. Elk twee keer.")]
             + _dos_veces([
                 ("¿Quieres ir a la playa el sábado?", "Wil je zaterdag naar het strand?"),
                 ("¿Podemos quedar a las seis?", "Kunnen we om zes uur afspreken?"),
                 ("Quiero ver una peli en mi casa.", "Ik wil een film kijken bij mij thuis."),
             ]),
    "clave": ["1. ¿Quieres ir a la playa el sábado?", "2. ¿Podemos quedar a las seis?",
              "3. Quiero ver una peli en mi casa."],
    "nota": "Dekt querer + poder + quedar, precies de drie vormen van oefening 5 en 6.",
}

C5_U4_04 = {
    "id": "C5-U4-AUD-04", "ancla": "c5-u4-aud-04", "curso": "C5", "unidad": 4,
    "seccion": "Cultura · Banda sonora",
    "etiqueta": "Banda sonora · playlist U4",
    "titulo": "«La Perla» — Rosalía",
    "tipo": "cancion",
    "tarea": "Luister; noteer drie woorden die je herkent.",
    "audio": None,
    "guion": [],
    "clave": ["Open opdracht — elk herkend woord telt; de leerkracht controleert of het "
              "woord écht in het fragment zit."],
    "nota": "GEEN EIGEN SCRIPT EN GEEN EIGEN MP3. Dit is een bestaand, auteursrechtelijk "
            "beschermd nummer: we nemen de tekst niet over en genereren er geen audio van. "
            "Bij de hosting-sweep (CLAUDE.md §18) wordt dit blok een link naar de officiële "
            "streamingversie of naar LyricsTraining; de cloze-oefening werkt op die "
            "externe speler.",
}


# ===========================================================================
# C5 · U5 — ¡Ñam!  (parada: México / CDMX)
# ===========================================================================

C5_U5_01 = {
    "id": "C5-U5-AUD-01", "ancla": "c5-u5-aud-01", "curso": "C5", "unidad": 5,
    "seccion": "§1 · Cantidades · mucho / poco / un poco de",
    "etiqueta": "Audio 5.1 · La lista · 0:50",
    "titulo": "El dictado de la compra",
    "tipo": "dictado",
    "tarea": "Schrijf de zes producten met hun hoeveelheid, één per regel.",
    "audio": "audio/C5_U5_01.mp3",
    "guion": [L("Diego", "Te dicto la lista de la compra. Seis cosas, dos veces cada una.",
                "Ik dicteer je het boodschappenlijstje. Zes dingen, elk twee keer.")]
             + _dos_veces([
                 ("un kilo de tomates", "een kilo tomaten"),
                 ("una botella de agua", "een fles water"),
                 ("un paquete de arroz", "een pak rijst"),
                 ("doscientos gramos de queso", "tweehonderd gram kaas"),
                 ("un poco de leche", "een beetje melk"),
                 ("muchas manzanas", "veel appels"),
             ], who="Diego")
             + [L("Diego", "Y ya está. ¡Gracias!", "En dat is het. Bedankt!")],
    "clave": ["1. un kilo de tomates", "2. una botella de agua", "3. un paquete de arroz",
              "4. doscientos gramos de queso", "5. un poco de leche", "6. muchas manzanas"],
    "nota": "De items 1–4 zijn precies de cantidades van de matching-oefening 7; item 5 en 6 "
            "zetten «un poco de» (niet telbaar) tegenover «muchas» (telbaar, vrouwelijk mv.), "
            "de valstrik van oefening 6.",
}

C5_U5_02 = {
    "id": "C5-U5-AUD-02", "ancla": "c5-u5-aud-02", "curso": "C5", "unidad": 5,
    "seccion": "§3 · Pedir en el restaurante · la cortesía",
    "etiqueta": "Audio 5.2 · En el restaurante · 1:05",
    "titulo": "Pedir en el restaurante — camarero y cliente",
    "tipo": "dialogo",
    "tarea": "Volg met je vinger: 1ª globaal, 2ª detail. Wie zegt wat?",
    "audio": "audio/C5_U5_02.mp3",
    "guion": [
        L("Camarero", "Buenas tardes, ¿qué va a tomar?", "Goedemiddag, wat gaat u nemen?"),
        L("Cliente", "Para mí, una ensalada de primero.", "Voor mij een salade als voorgerecht."),
        L("Camarero", "Muy bien. ¿Y de segundo?", "Heel goed. En als hoofdgerecht?"),
        L("Cliente", "Para mí, de segundo, pollo.", "Voor mij, als hoofdgerecht, kip."),
        L("Camarero", "¿Y para beber?", "En om te drinken?"),
        L("Cliente", "¿Me pone un refresco, por favor?", "Doet u mij een frisdrank, alstublieft?"),
        L("Camarero", "Enseguida. ¿Algo de postre?", "Komt eraan. Iets als dessert?"),
        L("Cliente", "No, gracias. La cuenta, por favor.", "Nee, dank u. De rekening, alstublieft."),
        L("Camarero", "Aquí tiene. ¡Que aproveche!", "Alstublieft. Smakelijk!"),
    ],
    "clave": [
        "Oefening 1 (¿camarero o cliente?): ¿Qué va a tomar? = camarero · Para mí, una "
        "ensalada = cliente · ¿Me pone un refresco? = cliente · ¿Y para beber? = camarero · "
        "La cuenta, por favor = cliente",
        "Oefening 2 (ordena 1–6): 1 Buenas tardes, ¿qué va a tomar? · 2 Para mí, una "
        "ensalada de primero · 3 Para mí, de segundo, pollo · 4 ¿Y para beber? · "
        "5 ¿Me pone un refresco? · 6 La cuenta, por favor.",
    ],
    "nota": "Bewust een ándere scène dan het lange luisterfragment «Una mesa para tres» "
            "(escucha_data.py): daar bestellen drie mensen samen en is er een probleem met "
            "de tacos; hier bestelt één klant vlot. Zo is dit geen voorgelezen versie van "
            "het andere fragment. De regels zijn letterlijk die van oefening 1 en 2.",
}

C5_U5_03 = {
    "id": "C5-U5-AUD-03", "ancla": "c5-u5-aud-03", "curso": "C5", "unidad": 5,
    "seccion": "§4 · lo / la / los / las",
    "etiqueta": "Audio 5.3 · ¿lo/la/los/las? · 0:40",
    "titulo": "Cuatro respuestas cortas del camarero",
    "tipo": "seleccion",
    "tarea": "Kruis aan welk pronomen je in het antwoord hoort.",
    "audio": "audio/C5_U5_03.mp3",
    "guion": [
        L("Narradora", "Cuatro preguntas y cuatro respuestas. ¿Qué pronombre oyes?",
          "Vier vragen en vier antwoorden. Welk voornaamwoord hoor je?"),
        L("Narradora", "Uno.", "Eén."),
        L("Cliente", "¿Me trae la carta?", "Brengt u mij de kaart?"),
        L("Camarero", "Sí, la traigo ahora mismo.", "Ja, ik breng hem meteen."),
        L("Narradora", "Dos.", "Twee."),
        L("Cliente", "¿Y los tacos?", "En de taco's?"),
        L("Camarero", "Los preparo en cinco minutos.", "Die maak ik binnen vijf minuten klaar."),
        L("Narradora", "Tres.", "Drie."),
        L("Cliente", "¿Me pone el postre?", "Doet u mij het dessert?"),
        L("Camarero", "Claro, lo traigo enseguida.", "Natuurlijk, ik breng het meteen."),
        L("Narradora", "Cuatro.", "Vier."),
        L("Cliente", "¿Tienen las bebidas frías?", "Hebt u de drankjes koud?"),
        L("Camarero", "Sí, las tenemos en la nevera.", "Ja, we hebben ze in de koelkast."),
    ],
    "clave": ["1. la  (la carta)", "2. los  (los tacos)", "3. lo  (el postre)",
              "4. las  (las bebidas)"],
    "nota": "De vier vormen komen elk precies één keer voor, in een andere volgorde dan het "
            "rooster — zo valt er niets te gokken.",
}


# ===========================================================================
# C5 · U6 — De tiendas  (parada: México — mercados)
# ===========================================================================

C5_U6_01 = {
    "id": "C5-U6-AUD-01", "ancla": "c5-u6-aud-01", "curso": "C5", "unidad": 6,
    "seccion": "§1 · lo / la / los / las · ¿la falda? → la compro",
    "etiqueta": "Audio 6.1 · En la tienda · 1:05",
    "titulo": "En la tienda — dependienta y cliente",
    "tipo": "dialogo",
    "tarea": "1ª globaal, 2ª detail: welk voornaamwoord gebruiken ze?",
    "audio": "audio/C5_U6_01.mp3",
    "guion": [
        L("Dependienta", "¡Hola! ¿Te puedo ayudar?", "Hallo! Kan ik je helpen?"),
        L("Cliente", "Sí, busco una camisa blanca.", "Ja, ik zoek een wit hemd."),
        L("Dependienta", "Mira, esta es muy bonita. ¿Te gusta?",
          "Kijk, deze is heel mooi. Vind je hem leuk?"),
        L("Cliente", "Sí, la quiero. ¿Cuánto cuesta?", "Ja, die wil ik. Hoeveel kost hij?"),
        L("Dependienta", "Veinticinco euros. ¿Y los vaqueros? Están de oferta.",
          "Vijfentwintig euro. En de jeans? Die zijn in de aanbieding."),
        L("Cliente", "No, no los necesito, gracias.", "Nee, die heb ik niet nodig, dank je."),
        L("Dependienta", "¿Y este jersey? Es de algodón.", "En deze trui? Hij is van katoen."),
        L("Cliente", "Mmm… lo veo un poco grande. ¿Tiene la talla mediana?",
          "Mmm… hij lijkt me een beetje groot. Hebt u maat medium?"),
        L("Dependienta", "Un momento… Sí, aquí están las medianas.",
          "Een momentje… Ja, hier zijn de medium maten."),
        L("Cliente", "Perfecto, las miro un segundo. Al final me llevo la camisa.",
          "Perfect, ik bekijk ze even. Uiteindelijk neem ik het hemd."),
        L("Dependienta", "Muy bien. Son veinticinco euros. ¿Cómo lo pagas?",
          "Heel goed. Dat is vijfentwintig euro. Hoe betaal je?"),
        L("Cliente", "Con tarjeta, por favor.", "Met kaart, alstublieft."),
    ],
    "clave": ["1. la  (la camisa → la quiero)", "2. los  (los vaqueros → no los necesito)",
              "3. lo  (el jersey → lo veo grande)", "4. las  (las medianas → las miro)"],
    "nota": "De vier pronomina zitten in de volgorde la · los · lo · las in het gesprek, wat "
            "de vier rijen van oefening 5 voedt. «Me llevo la camisa» aan het einde geeft de "
            "tarea comunicativa «¿Te lo llevas?» meteen zijn model.",
}


# ===========================================================================
# C5 · U7 — Mi casa y mi barrio  (parada: Colombia / Cartagena)
# ===========================================================================

C5_U7_01 = {
    "id": "C5-U7-AUD-01", "ancla": "c5-u7-aud-01", "curso": "C5", "unidad": 7,
    "seccion": "§1 · Hay / estar",
    "etiqueta": "Audio 7.1 · El barrio de Valen · 1:00",
    "titulo": "Valen describe su barrio",
    "tipo": "informativo",
    "tarea": "1ª: ¿qué hay? — 2ª: ¿dónde está? Kruis aan en noteer waar.",
    "audio": "audio/C5_U7_01.mp3",
    "guion": [
        L("Valen", "¡Hola! Soy Valen y vivo en Cartagena, en Colombia. Te enseño mi barrio.",
          "Hallo! Ik ben Valen en ik woon in Cartagena, in Colombia. Ik laat je mijn buurt zien."),
        L("Valen", "En mi barrio hay una plaza grande. La plaza está en el centro, "
                  "delante de la iglesia.",
          "In mijn buurt is er een groot plein. Het plein ligt in het centrum, vóór de kerk."),
        L("Valen", "También hay un supermercado. Está al lado de mi casa, muy cerca.",
          "Er is ook een supermarkt. Die ligt naast mijn huis, heel dichtbij."),
        L("Valen", "Farmacia no hay. La farmacia está en el otro barrio, a diez minutos.",
          "Een apotheek is er niet. De apotheek ligt in de andere wijk, op tien minuten."),
        L("Valen", "Y hay un parque pequeño. Está detrás del colegio, entre dos calles.",
          "En er is een klein park. Dat ligt achter de school, tussen twee straten."),
        L("Valen", "Me gusta mucho mi barrio porque hay mucha vida. ¿Y en tu barrio qué hay?",
          "Ik hou heel veel van mijn buurt want er is veel leven. En wat is er in jouw buurt?"),
    ],
    "clave": ["una plaza — SÍ — en el centro, delante de la iglesia",
              "un supermercado — SÍ — al lado de su casa",
              "una farmacia — NO — está en otro barrio",
              "un parque — SÍ — detrás del colegio, entre dos calles"],
    "nota": "De farmacia ontbreekt bewust: zonder één «no hay» is het ☐-vakje van oefening 4 "
            "gratis. Valen gebruikt telkens eerst «hay» (nieuw) en dan «está» (bekend) — "
            "precies het contrast van de regla.",
}

C5_U7_02 = {
    "id": "C5-U7-AUD-02", "ancla": "c5-u7-aud-02", "curso": "C5", "unidad": 7,
    "seccion": "§4 · ¿Cómo se va? · el imperativo",
    "etiqueta": "Audio 7.2 · ¿Cómo se va? · 0:50",
    "titulo": "Sigue las indicaciones",
    "tipo": "indicaciones",
    "tarea": "Volg de instructies op je plano. Waar kom je uit?",
    "audio": "audio/C5_U7_02.mp3",
    "guion": [
        L("Turista", "Perdona, ¿cómo se va desde la plaza?", "Sorry, hoe geraak ik vanaf het plein?"),
        L("Valen", "Muy fácil. Sal de la plaza por la calle grande.",
          "Heel makkelijk. Verlaat het plein via de grote straat."),
        L("Valen", "Sigue todo recto dos calles.", "Ga twee straten rechtdoor."),
        L("Valen", "Gira a la derecha en el semáforo.", "Sla rechtsaf bij het verkeerslicht."),
        L("Valen", "Cruza la avenida con cuidado.", "Steek voorzichtig de laan over."),
        L("Valen", "Y está allí mismo, a la izquierda, al lado del banco.",
          "En het is daar meteen, aan de linkerkant, naast de bank."),
        L("Turista", "¿Está lejos?", "Is het ver?"),
        L("Valen", "No, cinco minutos a pie. No tiene pérdida.",
          "Nee, vijf minuten te voet. Je kunt het niet missen."),
    ],
    "clave": ["Bestemming = el museo (al lado del banco, a la izquierda).",
              "Werkwoorden in imperativo: sal · sigue · gira · cruza — de vier vormen van §4."],
    "nota": "Het eindpunt hangt af van het plano dat in de unit gedrukt staat: controleer bij "
            "de hosting-sweep dat «al lado del banco, a la izquierda» op dát plano inderdaad "
            "el museo is, en pas anders de laatste regel aan (niet de sleutel).",
}


# ===========================================================================
# C5 · U8 — ¿Qué has hecho?  (parada: Perú / Cusco)
# ===========================================================================

C5_U8_01 = {
    "id": "C5-U8-AUD-01", "ancla": "c5-u8-aud-01", "curso": "C5", "unidad": 8,
    "seccion": "§1 · pretérito perfecto compuesto",
    "etiqueta": "Audio 8.1 · ¿Qué han hecho? · 0:55",
    "titulo": "Cuatro personas cuentan su verano",
    "tipo": "seleccion",
    "tarea": "Kruis aan wie het gedaan heeft.",
    "audio": "audio/C5_U8_01.mp3",
    "guion": [
        L("Narradora", "Cuatro personas cuentan qué han hecho este verano.",
          "Vier personen vertellen wat ze deze zomer gedaan hebben."),
        L("Nina", "Yo he subido a la montaña con mi tío. He sacado muchas fotos del valle.",
          "Ik ben de berg op geklommen met mijn oom. Ik heb veel foto's van de vallei gemaakt."),
        L("Diego", "Pues yo he comido un ceviche riquísimo en la costa. ¡Qué rico!",
          "Nou, ik heb een heerlijke ceviche gegeten aan de kust. Wat lekker!"),
        L("Lucía", "Yo he visto el mar por primera vez este año. He estado en Cádiz una semana.",
          "Ik heb dit jaar voor het eerst de zee gezien. Ik ben een week in Cádiz geweest."),
        L("Valen", "Yo no he viajado. He trabajado en la tienda de mi madre todo el verano.",
          "Ik heb niet gereisd. Ik heb de hele zomer in de winkel van mijn moeder gewerkt."),
    ],
    "clave": ["ha subido a la montaña → Nina", "ha comido un ceviche → Diego",
              "ha visto el mar → Lucía", "ha sacado muchas fotos → Nina",
              "Valen is de afleider: haar zinnen staan niet in het rooster."],
    "nota": "Vier sprekers (zoals de instructie zegt) maar drie kolommen in het rooster: Nina "
            "doet er twee, Valen is de afleider. Zo klopt «cuatro personas» én het rooster "
            "Nina/Diego/Lucía.",
}

C5_U8_02 = {
    "id": "C5-U8-AUD-02", "ancla": "c5-u8-aud-02", "curso": "C5", "unidad": 8,
    "seccion": "§4 · ¿Qué tiempo hace? · el clima",
    "etiqueta": "Audio 8.2 · El parte del tiempo · 0:50",
    "titulo": "El parte del tiempo — Perú",
    "tipo": "dictado",
    "tarea": "Noteer per stad het weer (ciudad + tiempo), één per regel.",
    "audio": "audio/C5_U8_02.mp3",
    "guion": [
        L("Presentador", "Buenos días. El tiempo para hoy en Perú. Escucha con atención.",
          "Goedemorgen. Het weer voor vandaag in Peru. Luister aandachtig."),
        L("Presentador", "En Lima está nublado y estamos a dieciocho grados.",
          "In Lima is het bewolkt en het is achttien graden."),
        L("Presentador", "En Cusco hace sol, pero hace frío: nueve grados.",
          "In Cusco is het zonnig, maar koud: negen graden."),
        L("Presentador", "En Iquitos, en la selva, llueve mucho y hace calor.",
          "In Iquitos, in het regenwoud, regent het veel en is het warm."),
        L("Presentador", "Y en Arequipa hace viento, con veinte grados.",
          "En in Arequipa waait het, met twintig graden."),
        L("Presentador", "Repito: Lima, nublado. Cusco, sol y frío. Iquitos, lluvia y calor. "
                        "Arequipa, viento.",
          "Ik herhaal: Lima, bewolkt. Cusco, zon en koud. Iquitos, regen en warm. "
          "Arequipa, wind."),
    ],
    "clave": ["1. Lima — está nublado, 18 grados", "2. Cusco — hace sol, hace frío, 9 grados",
              "3. Iquitos (la selva) — llueve, hace calor", "4. Arequipa — hace viento, 20 grados"],
    "nota": "Vier steden, gelijk aan wat het openingsblok aankondigt en wat dictee-oefening 3 "
            "vraagt (rechtgezet 2026-08-08; het blok sprak eerder van drie). De drie "
            "constructies uit de regla (hace / está / werkwoord alleen) komen alle drie voor.",
}


# ===========================================================================
# C6+ · U0 — ¡De vuelta!  (repaso: presente, concordancia, países)
# ===========================================================================

C6P_U0_01 = {
    "id": "C6P-U0-AUD-01", "ancla": "c6p-u0-aud-01", "curso": "C6+", "unidad": 0,
    "seccion": "§1 · Saludos y presentaciones",
    "etiqueta": "§1 · Diálogo",
    "titulo": "Nina se presenta — y un diálogo modelo",
    "tipo": "dialogo",
    "tarea": "Nummer de zinnen 1–5 in de juiste volgorde; sluit daarna het boek en groet "
             "je buur.",
    "audio": "audio/C6plus_U0_01.mp3",
    "guion": [
        L("Narradora", "Primera parte: Nina se presenta.", "Eerste deel: Nina stelt zich voor."),
        L("Nina", "¡Hola!", "Hallo!"),
        L("Nina", "Me llamo Nina.", "Ik heet Nina."),
        L("Nina", "Soy de Perú.", "Ik kom uit Peru."),
        L("Nina", "Tengo dieciséis años.", "Ik ben zestien."),
        L("Nina", "Vivo en Cusco.", "Ik woon in Cusco."),
        L("Narradora", "Segunda parte: el diálogo completo. Escucha y repite.",
          "Tweede deel: het volledige gesprek. Luister en herhaal."),
        L("Nina", "¡Hola! Buenos días. Me llamo Nina, ¿y tú?",
          "Hallo! Goedemorgen. Ik heet Nina, en jij?"),
        L("Mateo", "Buenos días. Yo soy Mateo. Encantado.",
          "Goedemorgen. Ik ben Mateo. Aangenaam."),
        L("Nina", "Igualmente. ¿De dónde eres?", "Insgelijks. Waar kom je vandaan?"),
        L("Mateo", "Soy de Argentina, de Buenos Aires. ¿Y tú?",
          "Ik kom uit Argentinië, uit Buenos Aires. En jij?"),
        L("Nina", "Yo soy peruana, vivo en Cusco. ¿Cuántos años tienes?",
          "Ik ben Peruaanse, ik woon in Cusco. Hoe oud ben jij?"),
        L("Mateo", "Tengo diecisiete. Oye, ¡hasta luego! La clase empieza.",
          "Ik ben zeventien. Zeg, tot straks! De les begint."),
        L("Nina", "¡Hasta luego, Mateo!", "Tot straks, Mateo!"),
    ],
    "clave": ["Volgorde zoals ze in het boek staan: «Tengo dieciséis años» = 4 · «¡Hola!» = 1 · "
              "«Vivo en Cusco» = 5 · «Me llamo Nina» = 2 · «Soy de Perú» = 3.",
              "Beurten in het diálogo: saludar → presentarse → preguntar → despedirse."],
}

C6P_U0_02 = {
    "id": "C6P-U0-AUD-02", "ancla": "c6p-u0-aud-02", "curso": "C6+", "unidad": 0,
    "seccion": "§1 · Suena bien / Preséntate",
    "etiqueta": "§1 · Suena bien / Preséntate",
    "titulo": "Shadowing — el alfabeto y los saludos",
    "tipo": "lista",
    "tarea": "Luister en herhaal (shadowing); neem daarna je eigen voorstelling op (20–30 s).",
    "audio": "audio/C6plus_U0_02.mp3",
    "guion": [
        L("Narradora", "El alfabeto. Repite después de mí.", "Het alfabet. Herhaal na mij."),
        L("Narradora", "a, be, ce, de, e, efe, ge, hache, i.",
          "a, be, ce, de, e, efe, ge, hache, i."),
        L("Narradora", "jota, ka, ele, eme, ene, eñe, o, pe, cu.",
          "jota, ka, ele, eme, ene, eñe, o, pe, cu."),
        L("Narradora", "erre, ese, te, u, uve, uve doble, equis, ye, zeta.",
          "erre, ese, te, u, uve, uve doble, equis, ye, zeta."),
        L("Narradora", "Ahora los saludos.", "Nu de begroetingen."),
        L("Narradora", "¡Hola! Buenos días. Buenas tardes. Buenas noches.",
          "Hallo! Goedemorgen. Goeiemiddag. Goedenavond."),
        L("Narradora", "¿Qué tal? ¿Cómo estás? Muy bien, gracias. ¿Y tú?",
          "Hoe gaat het? Hoe gaat het met je? Heel goed, dank je. En jij?"),
        L("Narradora", "Encantado. Encantada. Mucho gusto. Igualmente.",
          "Aangenaam (jongen). Aangenaam (meisje). Aangenaam. Insgelijks."),
        L("Narradora", "Adiós. Hasta luego. Hasta mañana.", "Dag. Tot straks. Tot morgen."),
        L("Narradora", "Y el modelo de tu mensaje de voz. Escucha una vez.",
          "En het model voor je spraakbericht. Luister één keer."),
        L("Nina", "¡Hola! Me llamo Nina, tengo dieciséis años, soy de Perú y vivo en Cusco. "
                 "Hablo español y quechua. ¡Hasta luego!",
          "Hallo! Ik heet Nina, ik ben zestien, ik kom uit Peru en ik woon in Cusco. "
          "Ik spreek Spaans en Quechua. Tot straks!"),
    ],
    "clave": ["Geen schrijfopdracht — shadowing. De opname van de leerling wordt beoordeeld op "
              "verstaanbaarheid en op de vijf gegevens (naam, leeftijd, land, stad, taal), "
              "niet op accentloosheid."],
    "nota": "Pauzes tussen de regels zijn hier functioneel: bij het renderen minstens één "
            "seconde stilte tussen de blokken laten, anders kan de leerling niet nazeggen.",
}

C6P_U0_03 = {
    "id": "C6P-U0-AUD-03", "ancla": "c6p-u0-aud-03", "curso": "C6+", "unidad": 0,
    "seccion": "§4 · Países · nacionalidades · lenguas",
    "etiqueta": "§4 · Presentaciones",
    "titulo": "Tres presentaciones — país, nacionalidad y lengua",
    "tipo": "informativo",
    "tarea": "1ª: ¿de qué país? — 2ª: nacionalidad y lengua. Vul je ficha aan.",
    "audio": "audio/C6plus_U0_03.mp3",
    "guion": [
        L("Diego", "Hola, soy Diego. Soy de México, de la Ciudad de México. "
                  "Soy mexicano y hablo español. En el insti también estudio inglés.",
          "Hallo, ik ben Diego. Ik kom uit Mexico, uit Mexico-Stad. "
          "Ik ben Mexicaan en ik spreek Spaans. Op school studeer ik ook Engels."),
        L("Lucía", "¡Hola! Me llamo Lucía. Soy de España, vivo en Sevilla. "
                  "Soy española y hablo español e inglés.",
          "Hallo! Ik heet Lucía. Ik kom uit Spanje, ik woon in Sevilla. "
          "Ik ben Spaanse en ik spreek Spaans en Engels."),
        L("Mateo", "Buenas. Yo soy Mateo, de Argentina. Vivo en Buenos Aires. "
                  "Soy argentino y hablo español e italiano, porque mi abuela es de Italia.",
          "Hoi. Ik ben Mateo, uit Argentinië. Ik woon in Buenos Aires. "
          "Ik ben Argentijn en ik spreek Spaans en Italiaans, want mijn oma komt uit Italië."),
    ],
    "clave": ["Diego — país: México · ciudad: Ciudad de México · nacionalidad: mexicano · "
              "lenguas: español (+ inglés)",
              "Lucía — país: España · ciudad: Sevilla · nacionalidad: española · "
              "lenguas: español, inglés",
              "Mateo — país: Argentina · ciudad: Buenos Aires · nacionalidad: argentino · "
              "lenguas: español, italiano"],
    "nota": "Alle drie de nationaliteiten met kleine letter — dat is precies de valstrik uit "
            "§4. «e» in plaats van «y» vóór i- (español e inglés / e italiano) staat er "
            "bewust in als noticing-materiaal.",
}


# ===========================================================================
# C6+ · U1 — la hora, la rutina, los gustos
# ===========================================================================

C6P_U1_01 = {
    "id": "C6P-U1-AUD-01", "ancla": "c6p-u1-aud-01", "curso": "C6+", "unidad": 1,
    "seccion": "§1 · ¿Qué hora es?",
    "etiqueta": "§1 · Dictado de horas",
    "titulo": "Dictado de horas — seis veces",
    "tipo": "dictado",
    "tarea": "1ª ronde: het hele uur. 2ª ronde: hetzelfde uur met minuten. Noteer zes tijden.",
    "audio": "audio/C6plus_U1_01.mp3",
    "guion": [
        L("Narradora", "Primera ronda: la hora en punto.", "Eerste ronde: het hele uur."),
        L("Narradora", "a) Son las ocho.", "a) Het is acht uur."),
        L("Narradora", "b) Es la una.", "b) Het is één uur."),
        L("Narradora", "c) Son las cuatro.", "c) Het is vier uur."),
        L("Narradora", "d) Son las once.", "d) Het is elf uur."),
        L("Narradora", "e) Son las seis.", "e) Het is zes uur."),
        L("Narradora", "f) Son las doce.", "f) Het is twaalf uur."),
        L("Narradora", "Segunda ronda: la misma hora, con minutos.",
          "Tweede ronde: hetzelfde uur, met minuten."),
        L("Narradora", "a) Son las ocho y cuarto.", "a) Het is kwart over acht."),
        L("Narradora", "b) Es la una y media.", "b) Het is half twee."),
        L("Narradora", "c) Son las cuatro menos diez.", "c) Het is tien voor vier."),
        L("Narradora", "d) Son las once y veinticinco.", "d) Het is vijfentwintig over elf."),
        L("Narradora", "e) Son las seis menos cuarto.", "e) Het is kwart voor zes."),
        L("Narradora", "f) Son las doce y cinco.", "f) Het is vijf over twaalf."),
    ],
    "clave": ["a) 8:15 — las ocho y cuarto", "b) 1:30 — la una y media",
              "c) 3:50 — las cuatro menos diez", "d) 11:25 — las once y veinticinco",
              "e) 5:45 — las seis menos cuarto", "f) 12:05 — las doce y cinco"],
    "nota": "Item b staat op de tweede plaats zodat «es la una» (enige enkelvoudsvorm) vroeg "
            "opduikt. Item c en e oefenen «menos», die Nederlandstaligen het vaakst missen.",
}

C6P_U1_02 = {
    "id": "C6P-U1-AUD-02", "ancla": "c6p-u1-aud-02", "curso": "C6+", "unidad": 1,
    "seccion": "§2 · Mi día a día — la rutina",
    "etiqueta": "§2 · Un día con Lucía",
    "titulo": "Un día con Lucía",
    "tipo": "informativo",
    "tarea": "1ª: hoe laat staat ze op? — 2ª: wat doet ze 's namiddags? Vertel daarna je "
             "eigen dag.",
    "audio": "audio/C6plus_U1_02.mp3",
    "guion": [
        L("Lucía", "Hola, soy Lucía. Te cuento un día normal en Sevilla.",
          "Hallo, ik ben Lucía. Ik vertel je over een gewone dag in Sevilla."),
        L("Lucía", "Me levanto a las siete menos cuarto. Siempre me despierto antes, "
                  "pero me quedo cinco minutos en la cama.",
          "Ik sta op om kwart voor zeven. Ik word altijd eerder wakker, "
          "maar ik blijf nog vijf minuten in bed."),
        L("Lucía", "Primero me ducho, luego desayuno con mi hermana y después me visto.",
          "Eerst douche ik, daarna ontbijt ik met mijn zus en vervolgens kleed ik me aan."),
        L("Lucía", "Salgo de casa a las ocho y voy al instituto en autobús. "
                  "Las clases empiezan a las ocho y media.",
          "Ik ga om acht uur van huis en ik ga met de bus naar school. "
          "De lessen beginnen om half negen."),
        L("Lucía", "Como en el instituto a las dos. Por la tarde hago los deberes "
                  "y a veces entreno con el equipo de baloncesto.",
          "Ik eet om twee uur op school. 's Namiddags maak ik mijn huiswerk "
          "en soms train ik met het basketbalteam."),
        L("Lucía", "Los martes por la tarde nunca entreno: voy a clase de guitarra.",
          "Op dinsdagnamiddag train ik nooit: dan ga ik naar gitaarles."),
        L("Lucía", "Ceno sobre las nueve y media y me acuesto a las once.",
          "Ik avondmaal rond half tien en ik ga om elf uur slapen."),
        L("Lucía", "¿Y tú? ¿A qué hora te levantas?", "En jij? Hoe laat sta jij op?"),
    ],
    "clave": ["Se levanta a las 6:45 (las siete menos cuarto).",
              "Por la tarde: hace los deberes · a veces entrena baloncesto · "
              "los martes va a clase de guitarra.",
              "Reflexieve werkwoorden in het fragment: me levanto · me despierto · me quedo · "
              "me ducho · me visto · me acuesto."],
    "nota": "Bevat de drie conectoren van §2 (primero · luego · después) en de drie "
            "frequentiewoorden (siempre · a veces · nunca), zodat dit fragment ook het "
            "noticing voor die twee rijtjes levert.",
}

C6P_U1_03 = {
    "id": "C6P-U1-AUD-03", "ancla": "c6p-u1-aud-03", "curso": "C6+", "unidad": 1,
    "seccion": "§5.3 · La escala + «me gusta… porque»",
    "etiqueta": "§5 · Canción «La Perla»",
    "titulo": "«La Perla» — Rosalía",
    "tipo": "cancion",
    "tarea": "Luister en vul de cloze aan; zeg daarna wat voor muziek het is en of je het "
             "leuk vindt.",
    "audio": None,
    "guion": [],
    "clave": ["De cloze wordt op de externe speler ingevuld; de opvolgvragen (¿qué tipo de "
              "música? ¿te gusta? ¿por qué?) zijn open en worden mondeling beoordeeld."],
    "nota": "GEEN EIGEN SCRIPT EN GEEN EIGEN MP3 — bestaand, auteursrechtelijk beschermd "
            "nummer (zie ook C5-U4-AUD-04). Bij de hosting-sweep wordt dit een link naar de "
            "officiële streamingversie of LyricsTraining.",
}


# ===========================================================================
# C6+ · U2 — la casa, el barrio, estar + gerundio
# ===========================================================================

C6P_U2_01 = {
    "id": "C6P-U2-AUD-01", "ancla": "c6p-u2-aud-01", "curso": "C6+", "unidad": 2,
    "seccion": "§2.3 · Practicar hay/estar + preposiciones",
    "etiqueta": "§2 · La casa de Valen",
    "titulo": "La casa de Valen",
    "tipo": "informativo",
    "tarea": "1ª: welke kamers zijn er? — 2ª: waar staat elk meubel?",
    "audio": "audio/C6plus_U2_01.mp3",
    "guion": [
        L("Valen", "Te enseño mi casa en Cartagena. No es grande, pero me encanta.",
          "Ik laat je mijn huis in Cartagena zien. Het is niet groot, maar ik ben er dol op."),
        L("Valen", "Abajo hay un salón, una cocina y un baño pequeño.",
          "Beneden zijn er een woonkamer, een keuken en een kleine badkamer."),
        L("Valen", "En el salón hay un sofá azul. El sofá está debajo de la ventana.",
          "In de woonkamer staat een blauwe zitbank. De bank staat onder het raam."),
        L("Valen", "La mesa está en el medio, entre el sofá y la cocina.",
          "De tafel staat in het midden, tussen de bank en de keuken."),
        L("Valen", "Arriba hay dos habitaciones. Mi habitación está al lado de la de mi madre.",
          "Boven zijn er twee slaapkamers. Mijn kamer ligt naast die van mijn moeder."),
        L("Valen", "En mi habitación tengo una cama, un armario y un escritorio. "
                  "El escritorio está delante de la ventana y el armario, detrás de la puerta.",
          "In mijn kamer heb ik een bed, een kast en een bureau. "
          "Het bureau staat vóór het raam en de kast achter de deur."),
        L("Valen", "Ah, y no hay garaje. La bici está en el patio, al lado de las plantas.",
          "Ah, en er is geen garage. De fiets staat op de binnenkoer, naast de planten."),
    ],
    "clave": ["Habitaciones: salón · cocina · baño (abajo) · dos habitaciones (arriba) · "
              "patio. NO hay garaje.",
              "sofá → debajo de la ventana · mesa → en el medio, entre el sofá y la cocina · "
              "escritorio → delante de la ventana · armario → detrás de la puerta · "
              "bici → en el patio, al lado de las plantas."],
    "nota": "Zes verschillende preposiciones (debajo de · entre · al lado de · delante de · "
            "detrás de · en) en één «no hay», zodat het contrast hay ↔ estar hoorbaar is.",
}

C6P_U2_02 = {
    "id": "C6P-U2-AUD-02", "ancla": "c6p-u2-aud-02", "curso": "C6+", "unidad": 2,
    "seccion": "§5 · El barrio y cómo llegar",
    "etiqueta": "§5 · ¿Cómo llego?",
    "titulo": "¿Cómo llego a la plaza?",
    "tipo": "indicaciones",
    "tarea": "1ª: waar gaat hij naartoe? — 2ª: noteer de aanwijzingen en volg de route op "
             "het plano.",
    "audio": "audio/C6plus_U2_02.mp3",
    "guion": [
        L("Turista", "Perdona, ¿cómo llego a la plaza principal? Estoy perdido.",
          "Sorry, hoe geraak ik op het hoofdplein? Ik ben verdwaald."),
        L("Valen", "Tranquilo, está cerca. Mira: sigue esta calle todo recto.",
          "Rustig, het is dichtbij. Kijk: volg deze straat rechtdoor."),
        L("Turista", "¿Hasta el final?", "Tot het einde?"),
        L("Valen", "Hasta el semáforo, sí. Allí gira a la izquierda.",
          "Tot het verkeerslicht, ja. Sla daar linksaf."),
        L("Valen", "Después cruza el puente pequeño y toma la segunda calle a la derecha.",
          "Daarna steek je het kleine brugje over en neem je de tweede straat rechts."),
        L("Turista", "La segunda, vale. ¿Y luego?", "De tweede, oké. En dan?"),
        L("Valen", "Luego pasa por delante de la iglesia amarilla. La plaza está justo detrás.",
          "Dan loop je vóór de gele kerk langs. Het plein ligt er vlak achter."),
        L("Turista", "¿Está lejos a pie?", "Is het ver te voet?"),
        L("Valen", "No, unos diez minutos. Y si te pierdes otra vez, pregunta en el quiosco.",
          "Nee, een minuut of tien. En als je opnieuw verdwaalt, vraag het in de kiosk."),
        L("Turista", "¡Muchas gracias!", "Heel erg bedankt!"),
    ],
    "clave": ["Bestemming: la plaza principal.",
              "Route: sigue todo recto → gira a la izquierda en el semáforo → cruza el puente "
              "→ toma la segunda calle a la derecha → pasa por delante de la iglesia amarilla "
              "→ la plaza está detrás. Unos diez minutos a pie.",
              "Imperativos: sigue · gira · cruza · toma · pasa · pregunta."],
}


# ===========================================================================
# C6+ · U3 — planes, futuro próximo, le/les
# ===========================================================================

C6P_U3_01 = {
    "id": "C6P-U3-AUD-01", "ancla": "c6p-u3-aud-01", "curso": "C6+", "unidad": 3,
    "seccion": "§2.3 · Practicar el futuro próximo",
    "etiqueta": "§2 · Planes de finde",
    "titulo": "¿Qué vas a hacer el finde?",
    "tipo": "dialogo",
    "tarea": "1ª: wat gaan ze doen? — 2ª: wanneer? Noteer de gegevens.",
    "audio": "audio/C6plus_U3_01.mp3",
    "guion": [
        L("Sofía", "Diego, ¿qué vas a hacer este finde?", "Diego, wat ga je dit weekend doen?"),
        L("Diego", "El viernes por la noche voy a ver una peli con mi hermano. "
                  "Vamos a pedir pizza también.",
          "Vrijdagavond ga ik een film kijken met mijn broer. We gaan ook pizza bestellen."),
        L("Sofía", "¡Qué bien! Yo el sábado por la mañana voy a estudiar, "
                  "porque tengo examen el lunes.",
          "Wat leuk! Ik ga zaterdagochtend studeren, want ik heb maandag examen."),
        L("Diego", "¿Y por la tarde?", "En 's namiddags?"),
        L("Sofía", "Por la tarde voy a jugar al fútbol con el equipo. ¿Vas a venir a vernos?",
          "'s Namiddags ga ik voetballen met de ploeg. Kom je kijken?"),
        L("Diego", "Sí, voy a ir. Y el domingo mi familia y yo vamos a comer "
                  "en casa de mis abuelos.",
          "Ja, ik ga komen. En zondag gaan mijn familie en ik bij mijn grootouders eten."),
        L("Sofía", "Entonces el domingo no vas a salir.", "Dan ga je zondag niet uit."),
        L("Diego", "No, el domingo por la noche voy a descansar. La semana va a ser larga.",
          "Nee, zondagavond ga ik rusten. De week wordt lang."),
    ],
    "clave": ["viernes por la noche — Diego: ver una peli + pedir pizza",
              "sábado por la mañana — Sofía: estudiar (examen el lunes)",
              "sábado por la tarde — Sofía: jugar al fútbol; Diego va a verla",
              "domingo — Diego: comer en casa de sus abuelos; por la noche, descansar"],
    "nota": "Uitsluitend «ir a + infinitivo» — geen futuro simple, conform de scope-grens uit "
            "CLAUDE.md §2. Elke plan-zin draagt een tijdsbepaling, zodat de tweede "
            "luisterronde («¿cuándo?») ook echt iets te halen heeft.",
}

C6P_U3_02 = {
    "id": "C6P-U3-AUD-02", "ancla": "c6p-u3-aud-02", "curso": "C6+", "unidad": 3,
    "seccion": "§5 · Comunicar y hacer planes",
    "etiqueta": "§5 · Quedamos el sábado",
    "titulo": "Quedamos el sábado",
    "tipo": "dialogo",
    "tarea": "1ª: wat gaan ze doen? — 2ª: wanneer en waar spreken ze af?",
    "audio": "audio/C6plus_U3_02.mp3",
    "guion": [
        L("Sofía", "Diego, ¿quedamos el sábado? Quiero ver la expo del museo.",
          "Diego, spreken we zaterdag af? Ik wil de expo in het museum zien."),
        L("Diego", "Vale. ¿A qué hora? Por la mañana no puedo, tengo entrenamiento.",
          "Oké. Hoe laat? 's Ochtends kan ik niet, ik heb training."),
        L("Sofía", "¿Te va bien a las cinco?", "Past vijf uur je?"),
        L("Diego", "A las cinco, perfecto. ¿Dónde quedamos?",
          "Vijf uur, perfect. Waar spreken we af?"),
        L("Sofía", "En la puerta del museo, delante de la taquilla.",
          "Aan de deur van het museum, vóór de kassa."),
        L("Diego", "Vale. Voy a mandarle un mensaje a Nina, ¿le decimos que venga con nosotros?",
          "Oké. Ik ga Nina een berichtje sturen; zeggen we haar dat ze meekomt?"),
        L("Sofía", "Sí, y a Mateo y a Valen también. Les mando yo las fotos de la expo "
                  "para convencerlos.",
          "Ja, en Mateo en Valen ook. Ik stuur hun de foto's van de expo om ze te overtuigen."),
        L("Diego", "Genial. Entonces el sábado a las cinco, en el museo.",
          "Geweldig. Dus zaterdag om vijf uur, aan het museum."),
        L("Sofía", "Hecho. Si llego tarde, te llamo.",
          "Afgesproken. Als ik te laat ben, bel ik je."),
    ],
    "clave": ["Qué: ver la expo del museo.", "Cuándo: el sábado a las cinco (por la mañana "
              "Diego no puede — entrenamiento).",
              "Dónde: en la puerta del museo, delante de la taquilla.",
              "Pronombres OI: le (a Nina) · les (a Mateo y a Valen) · te (a Diego)."],
    "nota": "Bewust een ándere fase dan C6P-U3-AUD-01: daar wórden plannen opgesomd, hier "
            "wordt er één afspraak gemaakt (uur + plaats + bevestiging). Levert meteen het "
            "noticing-materiaal voor le/les uit §3.",
}


# ===========================================================================
# C6+ · U4 — el viaje, el perfecto, por/para
# ===========================================================================

C6P_U4_01 = {
    "id": "C6P-U4-AUD-01", "ancla": "c6p-u4-aud-01", "curso": "C6+", "unidad": 4,
    "seccion": "§2.3 · Practicar el perfecto",
    "etiqueta": "§2 · ¿Qué tal el viaje?",
    "titulo": "¿Qué tal el viaje? — Nina cuenta",
    "tipo": "dialogo",
    "tarea": "1ª: waar is ze naartoe geweest? — 2ª: wat heeft ze gedaan?",
    "audio": "audio/C6plus_U4_01.mp3",
    "guion": [
        L("Diego", "¡Nina! ¿Qué tal el viaje?", "Nina! Hoe was de reis?"),
        L("Nina", "¡Increíble! He estado dos semanas en Chile.",
          "Ongelooflijk! Ik ben twee weken in Chili geweest."),
        L("Diego", "¿Has ido en avión?", "Ben je met het vliegtuig gegaan?"),
        L("Nina", "Sí, he salido para Santiago por avión, y luego he viajado por el sur en bus.",
          "Ja, ik ben met het vliegtuig naar Santiago vertrokken en daarna heb ik met de bus "
          "door het zuiden gereisd."),
        L("Diego", "¿Y qué has hecho allí?", "En wat heb je daar gedaan?"),
        L("Nina", "He caminado por la Patagonia, he visto glaciares y he dormido en una "
                 "tienda de campaña.",
          "Ik heb door Patagonië gewandeld, ik heb gletsjers gezien en ik heb in een tent "
          "geslapen."),
        L("Nina", "También he comido mucho pescado y he aprendido algunas palabras nuevas.",
          "Ik heb ook veel vis gegeten en een paar nieuwe woorden geleerd."),
        L("Diego", "¿Has sacado fotos?", "Heb je foto's gemaakt?"),
        L("Nina", "Muchísimas. Todavía no las he ordenado, pero te las enseño mañana.",
          "Heel veel. Ik heb ze nog niet gesorteerd, maar ik laat ze je morgen zien."),
        L("Diego", "¡Qué envidia! Yo no he salido de la ciudad este año.",
          "Wat benijd ik je! Ik ben dit jaar de stad niet uit geweest."),
    ],
    "clave": ["Adónde: Chile — Santiago y el sur (la Patagonia), dos semanas.",
              "Qué ha hecho: ha caminado por la Patagonia · ha visto glaciares · ha dormido "
              "en una tienda · ha comido pescado · ha aprendido palabras nuevas · ha sacado "
              "muchas fotos (todavía no las ha ordenado).",
              "Participios irregulares in het fragment: ha visto · ha hecho · ha dormido "
              "(regelmatig, maar met o→u-valstrik in het presente)."],
    "nota": "«He salido para Santiago por avión» en «he viajado por el sur» staan er bewust in "
            "als noticing voor §3 (por/para), dat direct op deze sectie volgt.",
}

C6P_U4_02 = {
    "id": "C6P-U4-AUD-02", "ancla": "c6p-u4-aud-02", "curso": "C6+", "unidad": 4,
    "seccion": "§4 · Experiencias y lugares",
    "etiqueta": "§4 · Experiencias",
    "titulo": "Experiencias de viaje",
    "tipo": "seleccion",
    "tarea": "Kruis aan wat ze gedaan hebben; 2ª ronde: wie is waar geweest?",
    "audio": "audio/C6plus_U4_02.mp3",
    "guion": [
        L("Narradora", "Cuatro personas cuentan una experiencia de viaje.",
          "Vier personen vertellen over een reiservaring."),
        L("Lucía", "Yo he estado en Marruecos con mi familia. He montado en camello "
                  "y he probado el té con menta.",
          "Ik ben in Marokko geweest met mijn familie. Ik heb op een kameel gereden "
          "en muntthee geproefd."),
        L("Diego", "Yo nunca he salido de México, pero he visitado las pirámides de Teotihuacán "
                  "tres veces. Nunca he montado en avión.",
          "Ik ben nooit buiten Mexico geweest, maar ik heb de piramides van Teotihuacán "
          "drie keer bezocht. Ik heb nog nooit gevlogen."),
        L("Valen", "Yo he ido a Panamá en barco. He visto el canal y he nadado en el Caribe.",
          "Ik ben met de boot naar Panama gegaan. Ik heb het kanaal gezien en in de Caraïben "
          "gezwommen."),
        L("Mateo", "Yo he viajado a España para ver a mi tía. He caminado por Madrid "
                  "y he comido churros a las seis de la mañana.",
          "Ik ben naar Spanje gereisd om mijn tante te bezoeken. Ik heb door Madrid gewandeld "
          "en om zes uur 's ochtends churros gegeten."),
    ],
    "clave": ["Lucía → Marruecos: montar en camello, probar té con menta",
              "Diego → México (Teotihuacán): visitar las pirámides; NUNCA ha montado en avión "
              "ni ha salido del país",
              "Valen → Panamá: ver el canal, nadar en el Caribe (ha ido en barco)",
              "Mateo → España (Madrid): caminar por Madrid, comer churros"],
    "nota": "Diego is de negatieve casus («nunca he…»): zonder hem is «marca lo que han hecho» "
            "een rooster waar alles aangekruist moet worden.",
}


# ===========================================================================
# C6+ · U5 — biografías, el indefinido, se lo / se la
# ===========================================================================

C6P_U5_01 = {
    "id": "C6P-U5-AUD-01", "ancla": "c6p-u5-aud-01", "curso": "C6+", "unidad": 5,
    "seccion": "§2.3 · Practicar el indefinido",
    "etiqueta": "§2 · ¿Quién fue…?",
    "titulo": "¿Quién fue…? — una minibiografía misteriosa",
    "tipo": "informativo",
    "tarea": "1ª: over welk beroep gaat het? — 2ª: wat deed die persoon? Noteer de gegevens.",
    "audio": "audio/C6plus_U5_01.mp3",
    "guion": [
        L("Narradora", "Escucha. ¿De qué oficio hablamos? No decimos el nombre hasta el final.",
          "Luister. Over welk beroep hebben we het? De naam zeggen we pas op het einde."),
        L("Narradora", "Nació en un pueblo pequeño de Colombia en mil novecientos veintisiete.",
          "Hij werd geboren in een klein dorp in Colombia in 1927."),
        L("Narradora", "De niño vivió con sus abuelos, y su abuela le contó muchas historias "
                      "de fantasmas.",
          "Als kind woonde hij bij zijn grootouders, en zijn oma vertelde hem veel "
          "spookverhalen."),
        L("Narradora", "Estudió derecho, pero no terminó la carrera: prefirió escribir "
                      "en los periódicos.",
          "Hij studeerde rechten, maar maakte het niet af: hij schreef liever voor de kranten."),
        L("Narradora", "Trabajó como periodista en Bogotá, en París y en México.",
          "Hij werkte als journalist in Bogotá, in Parijs en in Mexico."),
        L("Narradora", "En mil novecientos sesenta y siete publicó su novela más famosa, "
                      "«Cien años de soledad».",
          "In 1967 publiceerde hij zijn beroemdste roman, «Cien años de soledad»."),
        L("Narradora", "En mil novecientos ochenta y dos recibió el Premio Nobel de Literatura.",
          "In 1982 kreeg hij de Nobelprijs voor Literatuur."),
        L("Narradora", "Murió en México en dos mil catorce. Sus amigos lo llamaban «Gabo».",
          "Hij stierf in Mexico in 2014. Zijn vrienden noemden hem «Gabo»."),
        L("Narradora", "¿Quién fue? Fue Gabriel García Márquez, escritor y periodista.",
          "Wie was het? Het was Gabriel García Márquez, schrijver en journalist."),
    ],
    "clave": ["Oficio: escritor (y periodista).",
              "Hechos: nació en Colombia en 1927 · vivió con sus abuelos · estudió derecho "
              "(no terminó) · trabajó de periodista · publicó «Cien años de soledad» en 1967 · "
              "recibió el Nobel en 1982 · murió en México en 2014.",
              "Indefinidos: nació · vivió · contó · estudió · terminó · prefirió · trabajó · "
              "publicó · recibió · murió · fue."],
    "nota": "Alle feiten zijn nagekeken en onomstreden. De naam valt pas in de laatste regel, "
            "zodat de raadstructuur werkt ook als de leerling het fragment twee keer hoort.",
}

C6P_U5_02 = {
    "id": "C6P-U5-AUD-02", "ancla": "c6p-u5-aud-02", "curso": "C6+", "unidad": 5,
    "seccion": "§4 · Contar una historia",
    "etiqueta": "§4 · Una leyenda",
    "titulo": "Una leyenda del tango",
    "tipo": "informativo",
    "tarea": "1ª: over wie gaat het? — 2ª: zet de gebeurtenissen van zijn leven op volgorde.",
    "audio": "audio/C6plus_U5_02.mp3",
    "guion": [
        L("Narradora", "En Buenos Aires todo el mundo conoce esta cara. Es una leyenda "
                      "del tango.",
          "In Buenos Aires kent iedereen dit gezicht. Het is een legende van de tango."),
        L("Narradora", "Nadie sabe con certeza dónde nació. Unos dicen que en Francia, "
                      "otros que en Uruguay, alrededor de mil ochocientos noventa.",
          "Niemand weet met zekerheid waar hij geboren is. Sommigen zeggen in Frankrijk, "
          "anderen in Uruguay, rond 1890."),
        L("Narradora", "Lo que sí es seguro: creció en un barrio de Buenos Aires y empezó "
                      "a cantar en los cafés del barrio.",
          "Wat wel zeker is: hij groeide op in een wijk van Buenos Aires en begon te zingen "
          "in de cafés van de buurt."),
        L("Narradora", "Grabó sus primeros discos y poco a poco se hizo famoso en toda "
                      "América Latina.",
          "Hij nam zijn eerste platen op en werd stilaan beroemd in heel Latijns-Amerika."),
        L("Narradora", "Viajó a París y a Nueva York, y también actuó en varias películas.",
          "Hij reisde naar Parijs en New York, en speelde ook in verschillende films."),
        L("Narradora", "Su canción «El día que me quieras» es todavía hoy un clásico.",
          "Zijn lied «El día que me quieras» is vandaag nog altijd een klassieker."),
        L("Narradora", "En mil novecientos treinta y cinco murió en un accidente de avión "
                      "en Medellín, en Colombia. Tenía cuarenta y cuatro años.",
          "In 1935 stierf hij bij een vliegtuigongeluk in Medellín, in Colombia. "
          "Hij was vierenveertig."),
        L("Narradora", "Se llamaba Carlos Gardel. En Buenos Aires dicen que «cada día canta "
                      "mejor».",
          "Hij heette Carlos Gardel. In Buenos Aires zeggen ze dat hij «elke dag beter zingt»."),
    ],
    "clave": ["¿De quién habla? Carlos Gardel.",
              "Orden de los hechos: 1 nació (h. 1890, lugar discutido) · 2 creció en Buenos "
              "Aires · 3 empezó a cantar en los cafés · 4 grabó sus primeros discos · "
              "5 se hizo famoso · 6 viajó a París y Nueva York y actuó en películas · "
              "7 murió en Medellín en 1935.",
              "Contrast indefinido/imperfecto: «murió… Tenía cuarenta y cuatro años» — "
              "bruikbaar als brug naar U6."],
    "nota": "De onzekere geboorteplaats is geen slordigheid maar historisch feit, en is hier "
            "juist het haakje voor «leyenda». Vermijd dus het «rechtzetten» van die regel.",
}


# ===========================================================================
# C6+ · U6 — el imperfecto, antes y ahora
# ===========================================================================

C6P_U6_01 = {
    "id": "C6P-U6-AUD-01", "ancla": "c6p-u6-aud-01", "curso": "C6+", "unidad": 6,
    "seccion": "§2.3 · ¿Cómo era tu vida?",
    "etiqueta": "§2 · ¿Cómo era tu infancia?",
    "titulo": "¿Cómo era tu infancia? — Nina",
    "tipo": "informativo",
    "tarea": "1ª: waar woonde ze? — 2ª: wat deed ze? Noteer de gegevens.",
    "audio": "audio/C6plus_U6_01.mp3",
    "guion": [
        L("Nina", "Cuando era pequeña, no vivía en Cusco. Vivíamos en un pueblo "
                 "en las montañas, a tres horas de la ciudad.",
          "Toen ik klein was, woonde ik niet in Cusco. We woonden in een dorp in de bergen, "
          "op drie uur van de stad."),
        L("Nina", "La casa era de piedra y siempre hacía frío por la noche.",
          "Het huis was van steen en 's nachts was het altijd koud."),
        L("Nina", "Mi abuela cocinaba en el fuego y nosotros comíamos todos juntos.",
          "Mijn oma kookte op het vuur en wij aten allemaal samen."),
        L("Nina", "Iba a la escuela a pie: eran cuarenta minutos, con lluvia o con sol.",
          "Ik ging te voet naar school: dat was veertig minuten, met regen of met zon."),
        L("Nina", "Por la tarde jugaba con mis primos en el campo y cuidábamos las llamas "
                 "de mi tío.",
          "'s Namiddags speelde ik met mijn neven en nichten op het veld en zorgden we voor "
          "de lama's van mijn oom."),
        L("Nina", "No teníamos internet. Los domingos mi padre leía el periódico en voz alta "
                 "y todos escuchábamos.",
          "We hadden geen internet. Op zondag las mijn vader de krant hardop voor en "
          "luisterden we allemaal."),
        L("Nina", "Me gustaba mucho esa vida, pero ahora también me gusta la ciudad.",
          "Ik hield heel veel van dat leven, maar nu vind ik de stad ook fijn."),
    ],
    "clave": ["Dónde vivía: en un pueblo en las montañas, a tres horas de Cusco "
              "(casa de piedra).",
              "Qué hacía: iba a la escuela a pie (40 min) · jugaba con sus primos en el campo · "
              "cuidaban las llamas de su tío · comían todos juntos · su abuela cocinaba en el "
              "fuego · los domingos su padre leía el periódico en voz alta.",
              "Imperfectos: era · vivía · vivíamos · hacía · cocinaba · comíamos · iba · eran · "
              "jugaba · cuidábamos · teníamos · leía · escuchábamos · gustaba."],
    "nota": "Uitsluitend imperfecto — géén indefinido. Het contrast tussen de twee tijden komt "
            "pas in §3; deze opname moet dus «zuiver» achtergrond zijn, anders werkt de "
            "noticing van §3.1 niet meer.",
}


# ===========================================================================
# C6+ · U7 — opinar, el medio ambiente, consejos
# ===========================================================================

C6P_U7_01 = {
    "id": "C6P-U7-AUD-01", "ancla": "c6p-u7-aud-01", "curso": "C6+", "unidad": 7,
    "seccion": "§2.3 · Un cartel de consejos",
    "etiqueta": "§2 · ¿Qué opinas del medio ambiente?",
    "titulo": "¿Qué opinas del medio ambiente? — Valen y Diego",
    "tipo": "dialogo",
    "tarea": "1ª: waarover praten ze? — 2ª: welke raad geven ze? Schrijf op.",
    "audio": "audio/C6plus_U7_01.mp3",
    "guion": [
        L("Valen", "Diego, ¿qué opinas del medio ambiente? En mi barrio casi nadie recicla.",
          "Diego, wat vind jij van het milieu? In mijn buurt recycleert bijna niemand."),
        L("Diego", "Creo que es el problema más importante de nuestra generación. "
                  "En mi opinión, tenemos que cambiar cosas pequeñas cada día.",
          "Ik denk dat het het belangrijkste probleem van onze generatie is. Volgens mij "
          "moeten we elke dag kleine dingen veranderen."),
        L("Valen", "Estoy de acuerdo. Pienso que el plástico es lo peor: en la playa de "
                  "Cartagena hay botellas por todas partes.",
          "Ik ben het ermee eens. Ik vind plastic het ergste: op het strand van Cartagena "
          "liggen overal flessen."),
        L("Diego", "Pues yo no estoy de acuerdo del todo. Me parece que el transporte "
                  "contamina más que el plástico.",
          "Nou, ik ben het er niet helemaal mee eens. Het lijkt me dat vervoer meer vervuilt "
          "dan plastic."),
        L("Valen", "Tienes razón en eso. ¿Y qué consejo das tú?",
          "Daarin heb je gelijk. En welke raad geef jij?"),
        L("Diego", "Muy fácil: usa la bici o el bus, y no cojas el coche para dos calles.",
          "Heel eenvoudig: gebruik de fiets of de bus, en neem de auto niet voor twee straten."),
        L("Valen", "Yo doy otro: lleva siempre una botella tuya y no compres agua en plástico.",
          "Ik geef er nog een: neem altijd je eigen fles mee en koop geen water in plastic."),
        L("Diego", "Y un tercero, para el instituto: apaga la luz cuando sales del aula.",
          "En een derde, voor op school: doe het licht uit als je het lokaal verlaat."),
        L("Valen", "Perfecto. Creo que ya tenemos nuestro cartel.",
          "Perfect. Ik denk dat we ons affiche al hebben."),
    ],
    "clave": ["Tema: el medio ambiente — el reciclaje, el plástico y el transporte.",
              "Consejos: 1 usa la bici o el bus / no cojas el coche para dos calles · "
              "2 lleva tu propia botella / no compres agua en plástico · "
              "3 apaga la luz cuando sales del aula.",
              "Opinar: creo que · en mi opinión · pienso que · me parece que — "
              "reageren: estoy de acuerdo · no estoy de acuerdo · tienes razón."],
    "nota": "Alles na «creo que / pienso que / me parece que» staat in de indicativo (es, "
            "tenemos, contamina) — dat is de harde regel van §3 en meteen de scope-grens uit "
            "CLAUDE.md §2: géén subjuntivo. De negatieve imperativos («no cojas», «no "
            "compres») zijn de enige subjuntivo-vórmen die het leerplan wél toelaat, omdat "
            "ze hier als imperativo-chunk worden aangeboden, niet als wijs.",
}


# ===========================================================================
# Register + zelfcontrole
# ===========================================================================

CORTOS = {
    ("C5", 0): [C5_U0_01, C5_U0_02, C5_U0_03, C5_U0_04, C5_U0_05,
                C5_U0_06, C5_U0_07, C5_U0_08, C5_U0_09],
    ("C5", 1): [C5_U1_01, C5_U1_02, C5_U1_03],
    ("C5", 2): [C5_U2_01, C5_U2_02],
    ("C5", 3): [C5_U3_01, C5_U3_02],
    ("C5", 4): [C5_U4_01, C5_U4_02, C5_U4_03, C5_U4_04],
    ("C5", 5): [C5_U5_01, C5_U5_02, C5_U5_03],
    ("C5", 6): [C5_U6_01],
    ("C5", 7): [C5_U7_01, C5_U7_02],
    ("C5", 8): [C5_U8_01, C5_U8_02],
    ("C6+", 0): [C6P_U0_01, C6P_U0_02, C6P_U0_03],
    ("C6+", 1): [C6P_U1_01, C6P_U1_02, C6P_U1_03],
    ("C6+", 2): [C6P_U2_01, C6P_U2_02],
    ("C6+", 3): [C6P_U3_01, C6P_U3_02],
    ("C6+", 4): [C6P_U4_01, C6P_U4_02],
    ("C6+", 5): [C6P_U5_01, C6P_U5_02],
    ("C6+", 6): [C6P_U6_01],
    ("C6+", 7): [C6P_U7_01],
}

TODOS = [f for lista in CORTOS.values() for f in lista]

# Fragmenten zonder eigen script: bestaande muziek, extern af te spelen.
SIN_GUION = {"C5-U4-AUD-04", "C6P-U1-AUD-03"}

# Woorden/vormen die in geen enkel fragment mogen opduiken (CLAUDE.md §2).
# Losse vormen, want een volledige morfologische check hoort in de motor, niet hier.
_PROHIBIDO = (
    " haré", " harás", " hará", " haremos", " harán",
    " seré", " serás", " será", " seremos", " serán",
    " iré", " irás", " irá", " iremos", " irán",
    " tendré", " tendrá", " tendremos", " tendrán",
    " sería", " serían", " haría", " harían", " gustaría", " podría", " podrían",
)


def controla():
    """Faalt hier, niet in de klas."""
    vistos = set()
    for (curso, unidad), lista in CORTOS.items():
        for f in lista:
            for campo in ("id", "ancla", "curso", "unidad", "seccion", "etiqueta",
                          "titulo", "tipo", "tarea", "guion", "clave"):
                assert campo in f, "%s mist het veld %s" % (f.get("id", "?"), campo)
            assert f["id"] not in vistos, "dubbele id: %s" % f["id"]
            vistos.add(f["id"])
            assert f["curso"] == curso and f["unidad"] == unidad, f["id"]
            assert f["ancla"] == f["id"].lower(), \
                "%s: ancla hoort de kleine-letterversie van de id te zijn" % f["id"]
            assert f["clave"], "%s heeft geen antwoordsleutel" % f["id"]

            if f["id"] in SIN_GUION:
                assert not f["guion"] and f["audio"] is None, \
                    "%s hoort géén guion/mp3 te hebben (auteursrecht)" % f["id"]
                assert "GEEN EIGEN SCRIPT" in f.get("nota", ""), f["id"]
                continue

            assert f["guion"], "%s heeft een leeg guion" % f["id"]
            assert f["audio"], "%s heeft geen doelbestand" % f["id"]
            for linea in f["guion"]:
                assert set(linea) == {"who", "es", "nl"}, (f["id"], linea)
                assert linea["who"] and linea["es"], (f["id"], linea)
                bajo = " " + linea["es"].lower()
                for mal in _PROHIBIDO:
                    assert mal not in bajo, \
                        "%s gebruikt een verboden tijd (%s): %s" % (f["id"], mal.strip(),
                                                                    linea["es"])


controla()


def resumen():
    """Overzicht voor wie de audio gaat renderen."""
    print("%-14s %-30s %5s %s" % ("id", "titulo", "regels", "audio"))
    for f in TODOS:
        print("%-14s %-30s %5d %s" % (f["id"], f["titulo"][:30], len(f["guion"]),
                                      f["audio"] or "— (extern)"))
    print("\n%d fragmenten · %d regels · %d zonder eigen script" % (
        len(TODOS), sum(len(f["guion"]) for f in TODOS), len(SIN_GUION)))


if __name__ == "__main__":
    resumen()
