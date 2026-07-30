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

TODOS = {("C5", 0): C5_U0, ("C6+", 0): C6P_U0}


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
