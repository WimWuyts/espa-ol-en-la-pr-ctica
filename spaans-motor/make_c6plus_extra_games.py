#!/usr/bin/env python3
"""Extra motor-spellen voor C6+ U1–U7 — de sjablonen die C5 wél had en C6+ niet.

C6+ bleef op twaalf spellen per unit steken tegenover achttien à negenentwintig
bij C5. Wat ontbrak waren niet zomaar aantallen maar hele sjablonen: er stond
geen enkele `tap`, geen enkele `sim`, en per unit maar twee classify en twee
speak. Dit script vult dat aan met zeven spellen per unit:

    classify ×2 · match ×1 · tap ×1 · order ×1 · sim ×1 · speak ×1

Samen met de vijf typ-spellen uit `make_vocab_type_games.py` brengt dat elke
C6+-unit op vierentwintig — hetzelfde niveau als C5.

Inhoud: de leerstof van C6+ zelf, unit per unit. Werkwoordsvormen zijn
overgenomen uit `hub_type_gram.SETS[("C6+", n)]`, waar ze al nagerekend zijn,
of anders uit de vocabulairelijst van de unit.

Gebruik:  python3 make_c6plus_extra_games.py      (schrijft naar content/)
          node build.mjs                          (bouwt ze tot losse HTML)
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "content")

G = {"blue": "#3D74D6", "red": "#C4402C", "green": "#2E8E68", "amber": "#E0A22F",
     "purple": "#8B5E9E", "teal": "#2FA8A0", "magenta": "#B4309A"}


def w(obj):
    p = os.path.join(D, obj["id"] + ".json")
    open(p, "w", encoding="utf-8").write(json.dumps(obj, ensure_ascii=False, indent=2))
    return obj["id"]


def pre(n):
    return "es-c6plus-u%d-" % n


def classify(n, slug, title, sub, prompt, cats, items, rounds=10):
    return w({"id": pre(n) + slug, "title": title, "subtitle": sub, "lang": "es",
              "template": "classify", "options": {"rounds": rounds, "audio": False},
              "classify": {"prompt": prompt, "categories": cats, "items": items}})


def match(n, slug, title, sub, prompt, pairs, chunk=6):
    return w({"id": pre(n) + slug, "title": title, "subtitle": sub, "lang": "es",
              "template": "match", "options": {"chunk": chunk, "audio": False},
              "match": {"prompt": prompt, "pairs": pairs}})


def tap(n, slug, title, sub, prompt, items, rounds=12, joiner=" · "):
    return w({"id": pre(n) + slug, "title": title, "subtitle": sub, "lang": "es",
              "template": "tap", "options": {"rounds": rounds, "audio": False},
              "tap": {"prompt": prompt, "joiner": joiner, "items": items}})


def order(n, slug, title, sub, prompt, rounds):
    return w({"id": pre(n) + slug, "title": title, "subtitle": sub, "lang": "es",
              "template": "order", "options": {"audio": False},
              "order": {"prompt": prompt, "rounds": rounds}})


def sim(n, slug, title, sub, prompt, rounds):
    return w({"id": pre(n) + slug, "title": title, "subtitle": sub, "lang": "es",
              "template": "sim", "options": {"audio": False},
              "sim": {"prompt": prompt, "rounds": rounds}})


def speak(n, slug, title, sub, prompt, frame, label, items):
    return w({"id": pre(n) + slug, "title": title, "subtitle": sub, "lang": "es",
              "template": "speak", "options": {"audio": False},
              "speak": {"mode": "substitution", "prompt": prompt, "frame": frame,
                        "frameLabel": label, "items": items}})


gemaakt = []
def M(x): gemaakt.append(x)


# ══════════════════════════════════════════════════════════════════════════════
# U1 · «El día a día» — reflexivos · gustar · ser/estar · la hora
# ══════════════════════════════════════════════════════════════════════════════
M(tap(1, "tilde-reflexivo", "¿Dónde va la tilde?", "U1 · de tilde in de dagindeling",
  "Tik de lettergreep die de klemtoon draagt",
  [{"parts": ["des", "pier", "to"], "answer": 1, "tag": "llana", "sub": "me despierto"},
   {"parts": ["du", "cho"], "answer": 0, "tag": "llana", "sub": "me ducho"},
   {"parts": ["des", "a", "yu", "no"], "answer": 2, "tag": "llana", "sub": "desayuno"},
   {"parts": ["te", "lé", "fo", "no"], "answer": 1, "tag": "esdrújula", "sub": "teléfono · tilde"},
   {"parts": ["ca", "fé"], "answer": 1, "tag": "aguda", "sub": "café · tilde"},
   {"parts": ["clá", "si", "ca"], "answer": 0, "tag": "esdrújula", "sub": "clásica · tilde"},
   {"parts": ["re", "loj"], "answer": 1, "tag": "aguda", "sub": "reloj"},
   {"parts": ["ma", "ña", "na"], "answer": 1, "tag": "llana", "sub": "mañana"},
   {"parts": ["sá", "ba", "do"], "answer": 0, "tag": "esdrújula", "sub": "sábado · tilde"},
   {"parts": ["a", "cos", "tar"], "answer": 2, "tag": "aguda", "sub": "acostar"},
   {"parts": ["miér", "co", "les"], "answer": 0, "tag": "esdrújula", "sub": "miércoles · tilde"},
   {"parts": ["ves", "tir", "se"], "answer": 1, "tag": "llana", "sub": "vestirse"}]))

M(sim(1, "mi-dia", "Cuenta tu día", "U1 · vertel je eigen dag",
  "Tarea comunicativa · schrijf in het Spaans",
  [{"scenario": "Un amigo español te pregunta: ¿cómo es un día normal para ti?",
    "tag": "rutina", "sub": "gebruik minstens twee reflexieve werkwoorden en een uur",
    "min": 12, "need": [{"re": "me (levanto|despierto|ducho|acuesto)"}, {"re": "las? \\w+"}]},
   {"scenario": "Escribe qué te gusta y qué no te gusta de las mañanas.",
    "tag": "gustar", "sub": "gebruik gusta én gustan", "min": 10,
    "need": [{"re": "gusta"}, {"re": "gustan"}]},
   {"scenario": "Tu corresponsal pregunta a qué hora comes en Bélgica.",
    "tag": "hora", "sub": "antwoord met een uur voluit", "min": 8,
    "need": [{"re": "(a la|a las)"}]},
   {"scenario": "Describe a un compañero: ¿cómo es y cómo está hoy?",
    "tag": "serestar", "sub": "gebruik ser én estar", "min": 10,
    "need": [{"re": "\\bes\\b"}, {"re": "está"}]}]))

M(speak(1, "carrusel-rutina", "Carrusel · mi rutina", "U1 · zeg de zin met nieuwe gegevens",
  "Di la frase con los datos nuevos y grábate",
  "Me ___ a ___ y luego ___.", "Modelo · vul de gemarkeerde delen in",
  [{"fills": ["despierto", "las siete", "desayuno"], "sub": "07.00 · ontbijten", "tag": "carr"},
   {"fills": ["levanto", "las siete y media", "me ducho"], "sub": "07.30 · douchen", "tag": "carr"},
   {"fills": ["ducho", "las ocho", "me visto"], "sub": "08.00 · aankleden", "tag": "carr"},
   {"fills": ["acuesto", "las once", "me duermo"], "sub": "23.00 · slapen", "tag": "carr"},
   {"fills": ["despierto", "las seis y cuarto", "hago deporte"], "sub": "06.15 · sporten", "tag": "carr"},
   {"fills": ["levanto", "las nueve", "desayuno con mi familia"], "sub": "09.00 · weekend", "tag": "carr"},
   {"fills": ["ducho", "las siete menos cuarto", "salgo de casa"], "sub": "06.45 · vertrekken", "tag": "carr"},
   {"fills": ["acuesto", "medianoche", "leo un poco"], "sub": "00.00 · lezen", "tag": "carr"}]))


# ══════════════════════════════════════════════════════════════════════════════
# U2 · «Aquí vivo» — casa · hay/está(n) · preposiciones · gerundio · lo/la
# ══════════════════════════════════════════════════════════════════════════════
M(classify(2, "dentro-fuera", "Dentro o fuera de casa", "U2 · waar hoort het thuis?",
  "Hoort dit woord bij het huis of bij de wijk?",
  [{"id": "casa", "label": "la casa<br><small>binnen</small>", "glaze": G["purple"]},
   {"id": "barrio", "label": "el barrio<br><small>buiten</small>", "glaze": G["teal"]}],
  [{"stimulus": "el dormitorio", "answer": "casa", "tag": "casa", "sub": "de slaapkamer"},
   {"stimulus": "la farmacia", "answer": "barrio", "tag": "barrio", "sub": "de apotheek"},
   {"stimulus": "la nevera", "answer": "casa", "tag": "casa", "sub": "de koelkast"},
   {"stimulus": "el semáforo", "answer": "barrio", "tag": "barrio", "sub": "het verkeerslicht"},
   {"stimulus": "el armario", "answer": "casa", "tag": "casa", "sub": "de kast"},
   {"stimulus": "la parada", "answer": "barrio", "tag": "barrio", "sub": "de halte"},
   {"stimulus": "el salón", "answer": "casa", "tag": "casa", "sub": "de woonkamer"},
   {"stimulus": "la plaza", "answer": "barrio", "tag": "barrio", "sub": "het plein"},
   {"stimulus": "la ducha", "answer": "casa", "tag": "casa", "sub": "de douche"},
   {"stimulus": "la esquina", "answer": "barrio", "tag": "barrio", "sub": "de hoek"},
   {"stimulus": "la estantería", "answer": "casa", "tag": "casa", "sub": "de boekenkast"},
   {"stimulus": "el supermercado", "answer": "barrio", "tag": "barrio", "sub": "de supermarkt"}]))

M(match(2, "preposicion-dibujo", "¿Dónde está el gato?", "U2 · de preposities van plaats",
  "Verbind de preposición met de betekenis",
  [{"a": "encima de", "b": "op · bovenop ⬆️"}, {"a": "debajo de", "b": "onder ⬇️"},
   {"a": "delante de", "b": "vóór ➡️"}, {"a": "detrás de", "b": "achter ⬅️"},
   {"a": "al lado de", "b": "naast ↔️"}, {"a": "entre", "b": "tussen ⇄"},
   {"a": "dentro de", "b": "binnenin 📦"}, {"a": "fuera de", "b": "buiten 🚪"},
   {"a": "enfrente de", "b": "tegenover 🔁"}, {"a": "a la derecha de", "b": "rechts van ➡️"},
   {"a": "a la izquierda de", "b": "links van ⬅️"}, {"a": "cerca de", "b": "dichtbij 📍"}]))

M(tap(2, "pronombre-tap", "¿Qué sustituye el pronombre?", "U2 · waar slaat lo/la/los/las op?",
  "Tik het woord dat het pronombre vervangt",
  [{"parts": ["Compro", "el pan", "aquí"], "answer": 1, "tag": "lo", "sub": "el pan → lo compro"},
   {"parts": ["Veo", "la tele", "por la noche"], "answer": 1, "tag": "la", "sub": "la tele → la veo"},
   {"parts": ["Hago", "los deberes", "ahora"], "answer": 1, "tag": "los", "sub": "los deberes → los hago"},
   {"parts": ["Limpio", "las ventanas", "el sábado"], "answer": 1, "tag": "las", "sub": "las ventanas → las limpio"},
   {"parts": ["Busco", "el móvil", "en el salón"], "answer": 1, "tag": "lo", "sub": "el móvil → lo busco"},
   {"parts": ["Riego", "las plantas", "cada día"], "answer": 1, "tag": "las", "sub": "las plantas → las riego"},
   {"parts": ["Abro", "la ventana", "por la mañana"], "answer": 1, "tag": "la", "sub": "la ventana → la abro"},
   {"parts": ["Guardo", "los platos", "en el armario"], "answer": 1, "tag": "los", "sub": "los platos → los guardo"},
   {"parts": ["Escucho", "la radio", "en la cocina"], "answer": 1, "tag": "la", "sub": "la radio → la escucho"},
   {"parts": ["Pinto", "el dormitorio", "de azul"], "answer": 1, "tag": "lo", "sub": "el dormitorio → lo pinto"},
   {"parts": ["Ordeno", "las sillas", "del salón"], "answer": 1, "tag": "las", "sub": "las sillas → las ordeno"},
   {"parts": ["Cierro", "los armarios", "siempre"], "answer": 1, "tag": "los", "sub": "los armarios → los cierro"}]))

M(sim(2, "describe-casa", "Describe tu casa", "U2 · beschrijf waar je woont",
  "Tarea comunicativa · schrijf in het Spaans",
  [{"scenario": "Un amigo colombiano quiere saber cómo es tu casa.",
    "tag": "casa", "sub": "gebruik hay én está(n)", "min": 12,
    "need": [{"re": "\\bhay\\b"}, {"re": "est[áa]n?"}]},
   {"scenario": "Explica dónde está la cocina respecto al salón.",
    "tag": "prep", "sub": "gebruik een preposición de lugar", "min": 8,
    "need": [{"re": "(al lado|enfrente|entre|detrás|delante|encima|debajo)"}]},
   {"scenario": "Son las ocho de la tarde: ¿qué está haciendo tu familia ahora?",
    "tag": "gerundio", "sub": "gebruik estar + gerundio", "min": 10,
    "need": [{"re": "est(á|án|oy|amos)\\s+\\w+(ando|iendo)"}]},
   {"scenario": "Un turista te pregunta cómo llegar a la plaza.",
    "tag": "camino", "sub": "geef minstens twee aanwijzingen", "min": 10,
    "need": [{"re": "(gira|sigue|cruza|toma|pasa)"}]}]))

M(speak(2, "carrusel-donde", "Carrusel · ¿dónde está?", "U2 · zeg waar het staat",
  "Di dónde está el objeto y grábate",
  "El ___ está ___ del ___.", "Modelo · vul de gemarkeerde delen in",
  [{"fills": ["sofá", "delante", "televisor"], "sub": "zetel vóór de tv", "tag": "carr"},
   {"fills": ["espejo", "encima", "lavabo"], "sub": "spiegel boven de wastafel", "tag": "carr"},
   {"fills": ["perro", "debajo", "sofá"], "sub": "hond onder de zetel", "tag": "carr"},
   {"fills": ["armario", "al lado", "cama"], "sub": "kast naast het bed", "tag": "carr"},
   {"fills": ["parque", "detrás", "colegio"], "sub": "park achter de school", "tag": "carr"},
   {"fills": ["banco", "enfrente", "supermercado"], "sub": "bank tegenover de winkel", "tag": "carr"},
   {"fills": ["libro", "dentro", "cajón"], "sub": "boek in de lade", "tag": "carr"},
   {"fills": ["coche", "fuera", "garaje"], "sub": "auto buiten de garage", "tag": "carr"}]))


# ══════════════════════════════════════════════════════════════════════════════
# U3 · «Conectados» — móvil/redes · ir a + inf · le/les · creo que · acabar de
# ══════════════════════════════════════════════════════════════════════════════
M(classify(3, "ya-o-todavia", "¿Ya lo hiciste o vas a hacerlo?", "U3 · net gedaan of straks",
  "Is het net gebeurd (acabar de) of komt het nog (ir a)?",
  [{"id": "acabar", "label": "acabar de<br><small>net gedaan</small>", "glaze": G["amber"]},
   {"id": "ir", "label": "ir a<br><small>straks</small>", "glaze": G["blue"]}],
  [{"stimulus": "Acabo de mandarle un mensaje.", "answer": "acabar", "tag": "ac", "sub": "net verstuurd"},
   {"stimulus": "Voy a llamarte esta noche.", "answer": "ir", "tag": "ir", "sub": "vanavond"},
   {"stimulus": "Acabamos de colgar el vídeo.", "answer": "acabar", "tag": "ac", "sub": "net online"},
   {"stimulus": "Vamos a quedar el sábado.", "answer": "ir", "tag": "ir", "sub": "zaterdag"},
   {"stimulus": "Acaba de conectarse.", "answer": "acabar", "tag": "ac", "sub": "net online gekomen"},
   {"stimulus": "Van a publicar las fotos.", "answer": "ir", "tag": "ir", "sub": "gaan posten"},
   {"stimulus": "Acabo de ver tu historia.", "answer": "acabar", "tag": "ac", "sub": "net gezien"},
   {"stimulus": "Voy a apagar el móvil.", "answer": "ir", "tag": "ir", "sub": "ga uitzetten"},
   {"stimulus": "Acabas de escribirme.", "answer": "acabar", "tag": "ac", "sub": "net geschreven"},
   {"stimulus": "Vais a subir el vídeo, ¿no?", "answer": "ir", "tag": "ir", "sub": "gaan uploaden"},
   {"stimulus": "Acaban de responder al grupo.", "answer": "acabar", "tag": "ac", "sub": "net geantwoord"},
   {"stimulus": "Voy a contestarle mañana.", "answer": "ir", "tag": "ir", "sub": "morgen"}]))

M(match(3, "movil-acciones", "El móvil y las redes", "U3 · koppel het woord aan wat je doet",
  "Verbind het woord met de handeling",
  [{"a": "la pantalla", "b": "lo que miras 📱"}, {"a": "la contraseña", "b": "la escribes para entrar 🔒"},
   {"a": "el enlace", "b": "lo pinchas para abrir 🔗"}, {"a": "el mensaje", "b": "lo mandas 💬"},
   {"a": "la batería", "b": "se acaba y cargas ⚡"}, {"a": "la foto", "b": "la subes 📷"},
   {"a": "el grupo", "b": "escribes a todos a la vez 👥"}, {"a": "la llamada", "b": "la contestas ☎️"},
   {"a": "el vídeo", "b": "lo publicas 🎬"}, {"a": "la aplicación", "b": "la descargas ⬇️"},
   {"a": "el wifi", "b": "te conectas 📶"}, {"a": "la historia", "b": "dura 24 horas ⏱️"}]))

M(tap(3, "infinitivo-tap", "¿Qué verbo va detrás?", "U3 · na ir a en acabar de komt de infinitief",
  "Tik het werkwoord dat in de infinitief blijft staan",
  [{"parts": ["Voy", "a", "llamar", "a Marta"], "answer": 2, "tag": "inf", "sub": "llamar blijft infinitief"},
   {"parts": ["Acabo", "de", "colgar", "el vídeo"], "answer": 2, "tag": "inf", "sub": "colgar"},
   {"parts": ["Vamos", "a", "quedar", "el viernes"], "answer": 2, "tag": "inf", "sub": "quedar"},
   {"parts": ["Acaban", "de", "conectarse", "al grupo"], "answer": 2, "tag": "inf", "sub": "conectarse"},
   {"parts": ["¿Vas", "a", "subir", "las fotos?"], "answer": 2, "tag": "inf", "sub": "subir"},
   {"parts": ["Acabamos", "de", "ver", "tu historia"], "answer": 2, "tag": "inf", "sub": "ver"},
   {"parts": ["Van", "a", "publicar", "el resultado"], "answer": 2, "tag": "inf", "sub": "publicar"},
   {"parts": ["Acabo", "de", "cargar", "el móvil"], "answer": 2, "tag": "inf", "sub": "cargar"},
   {"parts": ["Voy", "a", "escribirle", "esta noche"], "answer": 2, "tag": "inf", "sub": "escribirle"},
   {"parts": ["Acaba", "de", "contestar", "al mensaje"], "answer": 2, "tag": "inf", "sub": "contestar"},
   {"parts": ["Vais", "a", "descargar", "la aplicación"], "answer": 2, "tag": "inf", "sub": "descargar"},
   {"parts": ["Acabas", "de", "apagar", "la pantalla"], "answer": 2, "tag": "inf", "sub": "apagar"}]))

M(sim(3, "chat-plan", "Organiza el finde", "U3 · maak een plan via chat",
  "Tarea comunicativa · schrijf in het Spaans",
  [{"scenario": "Escribe a un amigo para proponer un plan para el sábado.",
    "tag": "plan", "sub": "gebruik ir a + infinitivo", "min": 10,
    "need": [{"re": "(voy|vas|vamos|van) a \\w+"}]},
   {"scenario": "Dile a tu grupo lo que acabas de hacer hoy.",
    "tag": "acabar", "sub": "gebruik acabar de + infinitivo", "min": 8,
    "need": [{"re": "acab(o|as|a|amos|an) de \\w+"}]},
   {"scenario": "Da tu opinión sobre pasar mucho tiempo en el móvil.",
    "tag": "opinion", "sub": "begin met creo que…", "min": 12,
    "need": [{"re": "creo que"}]},
   {"scenario": "Cuenta qué le vas a regalar a tu mejor amigo y por qué.",
    "tag": "oi", "sub": "gebruik le", "min": 10, "need": [{"re": "\\ble\\b"}]}]))

M(speak(3, "carrusel-plan", "Carrusel · el plan", "U3 · zeg het plan met nieuwe gegevens",
  "Di el plan con los datos nuevos y grábate",
  "El ___ voy a ___ con ___.", "Modelo · vul de gemarkeerde delen in",
  [{"fills": ["sábado", "ver una peli", "mis amigos"], "sub": "zaterdag · film", "tag": "carr"},
   {"fills": ["domingo", "jugar al fútbol", "mi hermano"], "sub": "zondag · voetbal", "tag": "carr"},
   {"fills": ["viernes", "quedar en la plaza", "Lucía"], "sub": "vrijdag · plein", "tag": "carr"},
   {"fills": ["lunes", "estudiar", "mi compañera"], "sub": "maandag · studeren", "tag": "carr"},
   {"fills": ["miércoles", "subir un vídeo", "mi grupo"], "sub": "woensdag · video", "tag": "carr"},
   {"fills": ["jueves", "llamar", "mis abuelos"], "sub": "donderdag · bellen", "tag": "carr"},
   {"fills": ["martes", "entrenar", "el equipo"], "sub": "dinsdag · trainen", "tag": "carr"},
   {"fills": ["finde", "descansar", "mi familia"], "sub": "weekend · rusten", "tag": "carr"}]))


# ══════════════════════════════════════════════════════════════════════════════
# U4 · «De viaje» — perfecto compuesto · participios · por/para · marcadores
# ══════════════════════════════════════════════════════════════════════════════
M(match(4, "viaje-lugar", "El viaje · palabra y lugar", "U4 · koppel het woord aan de plek",
  "Verbind het woord met waar je het gebruikt",
  [{"a": "la maleta", "b": "la haces antes de salir 🧳"},
   {"a": "el billete", "b": "lo enseñas al subir 🎫"},
   {"a": "el andén", "b": "esperas el tren allí 🚉"},
   {"a": "la puerta de embarque", "b": "esperas el avión allí ✈️"},
   {"a": "el albergue", "b": "duermes barato allí 🛏️"},
   {"a": "la recepción", "b": "recoges la llave allí 🔑"},
   {"a": "el equipaje", "b": "lo facturas 🧳"},
   {"a": "la reserva", "b": "la haces por internet 💻"},
   {"a": "el pasaporte", "b": "lo necesitas para volar 🛂"},
   {"a": "la estación", "b": "coges el tren allí 🚆"},
   {"a": "el mapa", "b": "lo miras si te pierdes 🗺️"},
   {"a": "la mochila", "b": "la llevas a la espalda 🎒"}]))

M(tap(4, "participio-tap", "Tik het participio", "U4 · welk deel is het participio?",
  "Tik het woord dat het participio is",
  [{"parts": ["He", "visto", "el mar"], "answer": 1, "tag": "irr", "sub": "visto · ver"},
   {"parts": ["Hemos", "viajado", "en tren"], "answer": 1, "tag": "reg", "sub": "viajado"},
   {"parts": ["Has", "escrito", "una postal"], "answer": 1, "tag": "irr", "sub": "escrito"},
   {"parts": ["Ha", "perdido", "el billete"], "answer": 1, "tag": "reg", "sub": "perdido"},
   {"parts": ["Han", "hecho", "la maleta"], "answer": 1, "tag": "irr", "sub": "hecho"},
   {"parts": ["He", "dormido", "en un albergue"], "answer": 1, "tag": "reg", "sub": "dormido"},
   {"parts": ["Hemos", "vuelto", "hoy"], "answer": 1, "tag": "irr", "sub": "vuelto"},
   {"parts": ["Has", "reservado", "el hotel"], "answer": 1, "tag": "reg", "sub": "reservado"},
   {"parts": ["Ha", "puesto", "las fotos"], "answer": 1, "tag": "irr", "sub": "puesto"},
   {"parts": ["Han", "subido", "al volcán"], "answer": 1, "tag": "reg", "sub": "subido"},
   {"parts": ["He", "dicho", "la verdad"], "answer": 1, "tag": "irr", "sub": "dicho"},
   {"parts": ["Hemos", "visitado", "el museo"], "answer": 1, "tag": "reg", "sub": "visitado"}]))

M(sim(4, "diario-viaje", "Tu diario de viaje", "U4 · vertel wat je gedaan hebt",
  "Tarea comunicativa · schrijf in het Spaans",
  [{"scenario": "Escribe qué has hecho hoy en Chile.",
    "tag": "perfecto", "sub": "gebruik het perfecto compuesto", "min": 12,
    "need": [{"re": "h(e|as|a|emos|an) \w+"}]},
   {"scenario": "Cuenta tres cosas que todavía no has hecho en tu vida.",
    "tag": "marcador", "sub": "gebruik todavía no", "min": 10,
    "need": [{"re": "todav[ií]a no"}]},
   {"scenario": "Explica por qué viajas y para qué sirve viajar.",
    "tag": "porpara", "sub": "gebruik por én para", "min": 12,
    "need": [{"re": "\\bpor\\b"}, {"re": "\\bpara\\b"}]},
   {"scenario": "Pregunta a un compañero si alguna vez ha estado en España.",
    "tag": "pregunta", "sub": "gebruik alguna vez", "min": 8,
    "need": [{"re": "alguna vez"}]}]))

M(speak(4, "carrusel-viaje", "Carrusel · lo que he hecho", "U4 · zeg wat je gedaan hebt",
  "Di la frase con los datos nuevos y grábate",
  "Esta semana he ___ y todavía no he ___.", "Modelo · vul de gemarkeerde delen in",
  [{"fills": ["viajado en tren", "visto el desierto"], "sub": "trein · woestijn", "tag": "carr"},
   {"fills": ["visitado un museo", "subido al volcán"], "sub": "museum · vulkaan", "tag": "carr"},
   {"fills": ["escrito una postal", "llamado a mis padres"], "sub": "kaart · bellen", "tag": "carr"},
   {"fills": ["dormido en un albergue", "probado el pescado"], "sub": "hostel · vis", "tag": "carr"},
   {"fills": ["hecho muchas fotos", "comprado recuerdos"], "sub": "fotos · souvenirs", "tag": "carr"},
   {"fills": ["perdido el mapa", "encontrado el hotel"], "sub": "kaart kwijt", "tag": "carr"},
   {"fills": ["comido en el mercado", "ido a la playa"], "sub": "markt · strand", "tag": "carr"},
   {"fills": ["vuelto tarde", "descansado bien"], "sub": "laat terug", "tag": "carr"}]))


# ══════════════════════════════════════════════════════════════════════════════
# U5 · «Érase una vez» — indefinido · pretéritos fuertes · se lo/se la · relato
# ══════════════════════════════════════════════════════════════════════════════
M(classify(5, "conector-relato", "Los conectores del relato", "U5 · begin, midden of einde",
  "Waar in het verhaal hoort dit conector?",
  [{"id": "ini", "label": "el principio", "glaze": G["blue"]},
   {"id": "med", "label": "el medio", "glaze": G["amber"]},
   {"id": "fin", "label": "el final", "glaze": G["purple"]}],
  [{"stimulus": "Érase una vez…", "answer": "ini", "tag": "ini", "sub": "er was eens"},
   {"stimulus": "Un día…", "answer": "ini", "tag": "ini", "sub": "op een dag"},
   {"stimulus": "Entonces…", "answer": "med", "tag": "med", "sub": "toen"},
   {"stimulus": "De repente…", "answer": "med", "tag": "med", "sub": "plots"},
   {"stimulus": "Al final…", "answer": "fin", "tag": "fin", "sub": "uiteindelijk"},
   {"stimulus": "Hace muchos años…", "answer": "ini", "tag": "ini", "sub": "lang geleden"},
   {"stimulus": "Después…", "answer": "med", "tag": "med", "sub": "daarna"},
   {"stimulus": "Y colorín colorado…", "answer": "fin", "tag": "fin", "sub": "slotformule"},
   {"stimulus": "Al principio…", "answer": "ini", "tag": "ini", "sub": "in het begin"},
   {"stimulus": "Más tarde…", "answer": "med", "tag": "med", "sub": "later"},
   {"stimulus": "Por fin…", "answer": "fin", "tag": "fin", "sub": "eindelijk"},
   {"stimulus": "Mientras tanto…", "answer": "med", "tag": "med", "sub": "ondertussen"}]))

M(match(5, "biografia-verbo", "Una vida en verbos", "U5 · koppel het werkwoord aan het moment",
  "Verbind het werkwoord met het moment in een leven",
  [{"a": "nacer", "b": "el primer día 👶"}, {"a": "crecer", "b": "hacerse mayor 📏"},
   {"a": "estudiar", "b": "ir a la escuela 📚"}, {"a": "mudarse", "b": "cambiar de casa 📦"},
   {"a": "casarse", "b": "la boda 💍"}, {"a": "trabajar", "b": "ganar dinero 💼"},
   {"a": "viajar", "b": "conocer el mundo ✈️"}, {"a": "ganar un premio", "b": "el reconocimiento 🏆"},
   {"a": "publicar", "b": "sacar un libro 📖"}, {"a": "jubilarse", "b": "dejar de trabajar 🌅"},
   {"a": "morir", "b": "el último día 🕯️"}, {"a": "conocer", "b": "el primer encuentro 🤝"}]))

M(tap(5, "acento-indefinido", "El acento del indefinido", "U5 · waar staat de tilde?",
  "Tik de lettergreep met de tilde",
  [{"parts": ["ha", "blé"], "answer": 1, "tag": "yo", "sub": "hablé · yo"},
   {"parts": ["ha", "bló"], "answer": 1, "tag": "el", "sub": "habló · él"},
   {"parts": ["co", "mí"], "answer": 1, "tag": "yo", "sub": "comí · yo"},
   {"parts": ["vi", "vió"], "answer": 1, "tag": "el", "sub": "vivió · él"},
   {"parts": ["es", "tu", "dié"], "answer": 2, "tag": "yo", "sub": "estudié"},
   {"parts": ["na", "ció"], "answer": 1, "tag": "el", "sub": "nació"},
   {"parts": ["es", "cri", "bí"], "answer": 2, "tag": "yo", "sub": "escribí"},
   {"parts": ["ga", "nó"], "answer": 1, "tag": "el", "sub": "ganó"},
   {"parts": ["vi", "a", "jé"], "answer": 2, "tag": "yo", "sub": "viajé"},
   {"parts": ["mu", "rió"], "answer": 1, "tag": "el", "sub": "murió"},
   {"parts": ["tra", "ba", "jó"], "answer": 2, "tag": "el", "sub": "trabajó"},
   {"parts": ["pu", "bli", "có"], "answer": 2, "tag": "el", "sub": "publicó"}]))

M(sim(5, "cuenta-historia", "Cuenta una historia", "U5 · vertel iets uit het verleden",
  "Tarea comunicativa · schrijf in het Spaans",
  [{"scenario": "Cuenta qué hiciste el fin de semana pasado.",
    "tag": "indef", "sub": "gebruik het indefinido", "min": 12,
    "need": [{"re": "\\w+(é|ó|í|ió|aste|amos|aron|ieron)\\b"}]},
   {"scenario": "Escribe la biografía corta de alguien que admiras.",
    "tag": "bio", "sub": "gebruik nació en minstens twee andere werkwoorden", "min": 14,
    "need": [{"re": "naci[óo]"}]},
   {"scenario": "Empieza un cuento con «Érase una vez» y escribe tres frases.",
    "tag": "cuento", "sub": "gebruik een conector van het midden", "min": 14,
    "need": [{"re": "[ÉE]rase una vez"}, {"re": "(entonces|de repente|después|mientras)"}]},
   {"scenario": "Un amigo te pidió el libro. Dile que ya se lo diste.",
    "tag": "selo", "sub": "gebruik se lo of se la", "min": 8,
    "need": [{"re": "se l(o|a|os|as)"}]}]))

M(speak(5, "carrusel-ayer", "Carrusel · lo que pasó", "U5 · zeg wat er gebeurde",
  "Di la frase con los datos nuevos y grábate",
  "___ ___ y después ___.", "Modelo · vul de gemarkeerde delen in",
  [{"fills": ["Ayer", "estudié mucho", "vi una serie"], "sub": "gisteren", "tag": "carr"},
   {"fills": ["El sábado", "fui al centro", "comí con mi familia"], "sub": "zaterdag", "tag": "carr"},
   {"fills": ["El año pasado", "viajé a España", "volví encantado"], "sub": "vorig jaar", "tag": "carr"},
   {"fills": ["Un día", "perdí el móvil", "lo encontré en casa"], "sub": "op een dag", "tag": "carr"},
   {"fills": ["Anoche", "tuve un sueño raro", "me desperté temprano"], "sub": "vannacht", "tag": "carr"},
   {"fills": ["En julio", "hice un curso", "conocí a mucha gente"], "sub": "in juli", "tag": "carr"},
   {"fills": ["El lunes", "estuve enfermo", "no fui a clase"], "sub": "maandag", "tag": "carr"},
   {"fills": ["Hace dos años", "me mudé", "empecé en este instituto"], "sub": "twee jaar geleden", "tag": "carr"}]))


# ══════════════════════════════════════════════════════════════════════════════
# U6 · «Cuando era pequeño» — imperfecto · contraste · comparativos · relativo
# ══════════════════════════════════════════════════════════════════════════════
M(match(6, "infancia-objeto", "La infancia", "U6 · koppel het woord aan de herinnering",
  "Verbind het woord met wat het betekent",
  [{"a": "el juguete", "b": "con lo que jugabas 🧸"}, {"a": "el columpio", "b": "en el parque 🛝"},
   {"a": "el recreo", "b": "el descanso en la escuela ⏰"}, {"a": "la mochila", "b": "la llevabas a clase 🎒"},
   {"a": "el cuento", "b": "te lo leían antes de dormir 📖"}, {"a": "la bici", "b": "aprendiste a montarla 🚲"},
   {"a": "el patio", "b": "jugabais allí 🏫"}, {"a": "los dibujos animados", "b": "los veías por la tarde 📺"},
   {"a": "el cromo", "b": "los cambiabais 🃏"}, {"a": "la merienda", "b": "comías a las cinco 🥪"},
   {"a": "el pueblo", "b": "ibas en verano 🏡"}, {"a": "los abuelos", "b": "te cuidaban 👵"}]))

M(tap(6, "imperfecto-tap", "Tik la forma del imperfecto", "U6 · welk woord staat in het imperfecto?",
  "Tik het werkwoord dat in het imperfecto staat",
  [{"parts": ["De niño", "vivía", "en Cusco"], "answer": 1, "tag": "imp", "sub": "vivía"},
   {"parts": ["Antes", "jugábamos", "en la calle"], "answer": 1, "tag": "imp", "sub": "jugábamos"},
   {"parts": ["Mi abuela", "cocinaba", "los domingos"], "answer": 1, "tag": "imp", "sub": "cocinaba"},
   {"parts": ["Siempre", "íbamos", "al pueblo"], "answer": 1, "tag": "imp", "sub": "íbamos · ir"},
   {"parts": ["La casa", "era", "muy grande"], "answer": 1, "tag": "imp", "sub": "era · ser"},
   {"parts": ["Nosotros", "teníamos", "un perro"], "answer": 1, "tag": "imp", "sub": "teníamos"},
   {"parts": ["Los sábados", "veíamos", "dibujos"], "answer": 1, "tag": "imp", "sub": "veíamos · ver"},
   {"parts": ["Yo", "llevaba", "una mochila roja"], "answer": 1, "tag": "imp", "sub": "llevaba"},
   {"parts": ["Mis padres", "trabajaban", "mucho"], "answer": 1, "tag": "imp", "sub": "trabajaban"},
   {"parts": ["El patio", "estaba", "lleno de niños"], "answer": 1, "tag": "imp", "sub": "estaba"},
   {"parts": ["Tú", "querías", "ser astronauta"], "answer": 1, "tag": "imp", "sub": "querías"},
   {"parts": ["En verano", "hacía", "mucho calor"], "answer": 1, "tag": "imp", "sub": "hacía"}]))

M(sim(6, "cuando-era", "Cuando era pequeño", "U6 · vertel over vroeger",
  "Tarea comunicativa · schrijf in het Spaans",
  [{"scenario": "Cuenta cómo era tu vida cuando tenías ocho años.",
    "tag": "imp", "sub": "gebruik het imperfecto", "min": 14,
    "need": [{"re": "\\w+(aba|ía)\\w*\\b"}]},
   {"scenario": "Compara tu pueblo o barrio de antes con el de ahora.",
    "tag": "comp", "sub": "gebruik más… que of menos… que", "min": 12,
    "need": [{"re": "(más|menos) \\w+ que"}]},
   {"scenario": "Describe un juguete que tenías y que te encantaba.",
    "tag": "rel", "sub": "gebruik een bijzin met que", "min": 10,
    "need": [{"re": "\\bque\\b"}]},
   {"scenario": "Cuenta algo que pasó un día concreto de tu infancia.",
    "tag": "contraste", "sub": "gebruik imperfecto én indefinido", "min": 14,
    "need": [{"re": "\\w+(aba|ía)\\w*\\b"}, {"re": "\\w+(é|ó|í|ió)\\b"}]}]))

M(speak(6, "carrusel-antes", "Carrusel · antes y ahora", "U6 · vergelijk vroeger en nu",
  "Di la frase con los datos nuevos y grábate",
  "Antes ___, pero ahora ___.", "Modelo · vul de gemarkeerde delen in",
  [{"fills": ["jugaba en la calle", "juego en casa"], "sub": "spelen", "tag": "carr"},
   {"fills": ["vivía en un pueblo", "vivo en la ciudad"], "sub": "wonen", "tag": "carr"},
   {"fills": ["veía dibujos animados", "veo series"], "sub": "kijken", "tag": "carr"},
   {"fills": ["iba en bici", "voy en autobús"], "sub": "vervoer", "tag": "carr"},
   {"fills": ["tenía mucho tiempo libre", "estudio mucho"], "sub": "tijd", "tag": "carr"},
   {"fills": ["comía en casa de mis abuelos", "como en el instituto"], "sub": "eten", "tag": "carr"},
   {"fills": ["era muy tímido", "hablo con todos"], "sub": "karakter", "tag": "carr"},
   {"fills": ["leía cuentos", "leo novelas"], "sub": "lezen", "tag": "carr"}]))


# ══════════════════════════════════════════════════════════════════════════════
# U7 · «¡Opina y cuídate!» — imperativo (+pronombres) · opinión · conectores
# ══════════════════════════════════════════════════════════════════════════════
M(classify(7, "consejo-o-opinion", "¿Consejo u opinión?", "U7 · raad geven of vinden",
  "Geeft de zin een raad (imperativo) of een mening?",
  [{"id": "consejo", "label": "consejo<br><small>imperativo</small>", "glaze": G["amber"]},
   {"id": "opinion", "label": "opinión<br><small>creo que…</small>", "glaze": G["purple"]}],
  [{"stimulus": "Bebe más agua.", "answer": "consejo", "tag": "con", "sub": "imperativo"},
   {"stimulus": "Creo que el reciclaje es necesario.", "answer": "opinion", "tag": "op", "sub": "creo que"},
   {"stimulus": "Duerme ocho horas.", "answer": "consejo", "tag": "con", "sub": "imperativo"},
   {"stimulus": "Me parece que comemos mal.", "answer": "opinion", "tag": "op", "sub": "me parece"},
   {"stimulus": "Recicla el plástico.", "answer": "consejo", "tag": "con", "sub": "imperativo"},
   {"stimulus": "Estoy de acuerdo contigo.", "answer": "opinion", "tag": "op", "sub": "instemmen"},
   {"stimulus": "Haz deporte tres veces por semana.", "answer": "consejo", "tag": "con", "sub": "haz"},
   {"stimulus": "No estoy de acuerdo con eso.", "answer": "opinion", "tag": "op", "sub": "oneens"},
   {"stimulus": "Ve al médico si te duele.", "answer": "consejo", "tag": "con", "sub": "ve · ir"},
   {"stimulus": "Pienso que el clima cambia.", "answer": "opinion", "tag": "op", "sub": "pienso que"},
   {"stimulus": "Apaga la luz al salir.", "answer": "consejo", "tag": "con", "sub": "imperativo"},
   {"stimulus": "En mi opinión, hay que actuar.", "answer": "opinion", "tag": "op", "sub": "en mi opinión"}]))

M(match(7, "cuerpo-dolor", "El cuerpo y el dolor", "U7 · koppel de klacht aan het lichaamsdeel",
  "Verbind de klacht met wat er pijn doet",
  [{"a": "me duele la cabeza", "b": "el dolor de cabeza 🤕"},
   {"a": "me duele la garganta", "b": "no puedo tragar 😷"},
   {"a": "me duelen las piernas", "b": "después de correr 🦵"},
   {"a": "me duele el estómago", "b": "he comido mal 🤢"},
   {"a": "me duele la espalda", "b": "la mochila pesa 🎒"},
   {"a": "me duelen los ojos", "b": "demasiada pantalla 👀"},
   {"a": "tengo fiebre", "b": "38 grados 🌡️"},
   {"a": "tengo tos", "b": "no paro de toser 😮‍💨"},
   {"a": "estoy cansado", "b": "he dormido poco 😴"},
   {"a": "me duele una muela", "b": "hay que ir al dentista 🦷"},
   {"a": "tengo catarro", "b": "me duele la nariz 🤧"},
   {"a": "me duele el pie", "b": "los zapatos son pequeños 🦶"}]))

M(tap(7, "imperativo-tilde", "El imperativo + pronombre", "U7 · waar valt de klemtoon?",
  "Tik de lettergreep die de klemtoon draagt",
  [{"parts": ["cuí", "da", "te"], "answer": 0, "tag": "tilde", "sub": "cuídate · tilde"},
   {"parts": ["re", "cí", "cla", "lo"], "answer": 1, "tag": "tilde", "sub": "recíclalo · tilde"},
   {"parts": ["bé", "be", "la"], "answer": 0, "tag": "tilde", "sub": "bébela · tilde"},
   {"parts": ["dí", "me", "lo"], "answer": 0, "tag": "tilde", "sub": "dímelo · tilde"},
   {"parts": ["a", "pá", "ga", "la"], "answer": 1, "tag": "tilde", "sub": "apágala · tilde"},
   {"parts": ["cóm", "pra", "lo"], "answer": 0, "tag": "tilde", "sub": "cómpralo · tilde"},
   {"parts": ["es", "cú", "cha", "me"], "answer": 1, "tag": "tilde", "sub": "escúchame · tilde"},
   {"parts": ["lá", "va", "te"], "answer": 0, "tag": "tilde", "sub": "lávate · tilde"},
   {"parts": ["se", "pá", "ra", "la"], "answer": 1, "tag": "tilde", "sub": "sepárala · tilde"},
   {"parts": ["hazlo"], "answer": 0, "tag": "geen", "sub": "hazlo · geen tilde nodig"},
   {"parts": ["po", "nlo"], "answer": 0, "tag": "geen", "sub": "ponlo · geen tilde"},
   {"parts": ["a", "yú", "da", "me"], "answer": 1, "tag": "tilde", "sub": "ayúdame · tilde"}]))

M(sim(7, "opina-cuidate", "Opina y aconseja", "U7 · geef je mening en je raad",
  "Tarea comunicativa · schrijf in het Spaans",
  [{"scenario": "Un amigo duerme muy poco. Dale tres consejos.",
    "tag": "imp", "sub": "gebruik de imperativo", "min": 12,
    "need": [{"re": "\\b(come|bebe|duerme|haz|ve|apaga|deja|sal)\\b"}]},
   {"scenario": "Da tu opinión sobre el reciclaje en tu instituto.",
    "tag": "op", "sub": "gebruik creo que of me parece que", "min": 12,
    "need": [{"re": "(creo que|me parece que|pienso que)"}]},
   {"scenario": "Escribe un consejo con un pronombre: la botella, el papel…",
    "tag": "pron", "sub": "gebruik imperativo + pronombre", "min": 8,
    "need": [{"re": "\\w+(lo|la|los|las|te|me)\\b"}]},
   {"scenario": "Explica por qué no estás de acuerdo con usar coche para todo.",
    "tag": "conect", "sub": "gebruik porque en por eso of sin embargo", "min": 14,
    "need": [{"re": "porque"}, {"re": "(por eso|sin embargo|además)"}]}]))

M(speak(7, "carrusel-consejo", "Carrusel · el consejo", "U7 · geef de raad met nieuwe gegevens",
  "Di el consejo con los datos nuevos y grábate",
  "Si ___, ___ y no ___.", "Modelo · vul de gemarkeerde delen in",
  [{"fills": ["te duele la cabeza", "bebe agua", "mires la pantalla"], "sub": "hoofdpijn", "tag": "carr"},
   {"fills": ["estás cansado", "duerme más", "tomes café"], "sub": "moe", "tag": "carr"},
   {"fills": ["tienes tos", "ve al médico", "salgas sin abrigo"], "sub": "hoest", "tag": "carr"},
   {"fills": ["quieres ayudar al planeta", "recicla", "uses plástico"], "sub": "milieu", "tag": "carr"},
   {"fills": ["te duele la espalda", "haz ejercicio", "lleves tanto peso"], "sub": "rugpijn", "tag": "carr"},
   {"fills": ["hace calor", "bebe mucha agua", "corras al mediodía"], "sub": "warm", "tag": "carr"},
   {"fills": ["tienes fiebre", "quédate en casa", "vayas a clase"], "sub": "koorts", "tag": "carr"},
   {"fills": ["gastas mucha luz", "apaga las lámparas", "dejes todo encendido"], "sub": "energie", "tag": "carr"}]))


# ══════════════════════════════════════════════════════════════════════════════
# U0 · «¡Volvemos!» — presente · ser/estar · género/concordancia · países
# U0 had al vijf typ-spellen maar geen tap, geen sim en maar één match.
# ══════════════════════════════════════════════════════════════════════════════
M(match(0, "verbo-yo", "El verbo y su yo", "U0 · koppel de infinitief aan de yo-vorm",
  "Verbind de infinitief met de vorm van yo",
  [{"a": "ser", "b": "soy"}, {"a": "estar", "b": "estoy"}, {"a": "tener", "b": "tengo"},
   {"a": "hacer", "b": "hago"}, {"a": "ir", "b": "voy"}, {"a": "dar", "b": "doy"},
   {"a": "venir", "b": "vengo"}, {"a": "hablar", "b": "hablo"}, {"a": "comer", "b": "como"},
   {"a": "vivir", "b": "vivo"}, {"a": "salir", "b": "salgo"}, {"a": "poner", "b": "pongo"}]))

M(tap(0, "acento-tap", "¿Dónde va el acento?", "U0 · de klemtoon in bekende woorden",
  "Tik de lettergreep die de klemtoon draagt",
  [{"parts": ["es", "pa", "ñol"], "answer": 2, "tag": "aguda", "sub": "español"},
   {"parts": ["mé", "xi", "co"], "answer": 0, "tag": "esdrújula", "sub": "México · tilde"},
   {"parts": ["ar", "gen", "ti", "na"], "answer": 2, "tag": "llana", "sub": "Argentina"},
   {"parts": ["pe", "rú"], "answer": 1, "tag": "aguda", "sub": "Perú · tilde"},
   {"parts": ["co", "lom", "bia"], "answer": 1, "tag": "llana", "sub": "Colombia"},
   {"parts": ["pá", "gi", "na"], "answer": 0, "tag": "esdrújula", "sub": "página · tilde"},
   {"parts": ["pro", "fe", "sor"], "answer": 2, "tag": "aguda", "sub": "profesor"},
   {"parts": ["mú", "si", "ca"], "answer": 0, "tag": "esdrújula", "sub": "música · tilde"},
   {"parts": ["a", "mi", "go"], "answer": 1, "tag": "llana", "sub": "amigo"},
   {"parts": ["ciu", "dad"], "answer": 1, "tag": "aguda", "sub": "ciudad"},
   {"parts": ["fá", "cil"], "answer": 0, "tag": "llana", "sub": "fácil · tilde"},
   {"parts": ["te", "lé", "fo", "no"], "answer": 1, "tag": "esdrújula", "sub": "teléfono · tilde"}]))

M(sim(0, "vuelve-presentate", "Preséntate otra vez", "U0 · stel jezelf opnieuw voor",
  "Tarea comunicativa · schrijf in het Spaans",
  [{"scenario": "Es el primer día del curso. Preséntate a un compañero nuevo.",
    "tag": "pres", "sub": "naam, leeftijd en herkomst", "min": 12,
    "need": [{"re": "me llamo"}, {"re": "(soy de|vivo en)"}]},
   {"scenario": "Describe a tu mejor amigo: cómo es y cómo está hoy.",
    "tag": "serestar", "sub": "gebruik ser én estar", "min": 12,
    "need": [{"re": "\\bes\\b"}, {"re": "está"}]},
   {"scenario": "Escribe de qué países son tres personas de tu clase.",
    "tag": "pais", "sub": "gebruik ser de + land", "min": 10,
    "need": [{"re": "es de|son de"}]},
   {"scenario": "Cuenta qué haces normalmente los fines de semana.",
    "tag": "presente", "sub": "gebruik minstens drie werkwoorden in het presente", "min": 12,
    "need": [{"re": "\\w+(o|as|a|amos|an|es|e|emos|en)\\b"}]}]))

M(speak(0, "carrusel-presentate", "Carrusel · preséntate", "U0 · zeg de zin met nieuwe gegevens",
  "Di la frase con los datos nuevos y grábate",
  "Me llamo ___, soy de ___ y tengo ___ años.", "Modelo · vul de gemarkeerde delen in",
  [{"fills": ["Lucía", "Sevilla", "diecisiete"], "sub": "Sevilla · 17", "tag": "carr"},
   {"fills": ["Diego", "México", "dieciséis"], "sub": "Mexico · 16", "tag": "carr"},
   {"fills": ["Valen", "Cartagena", "diecisiete"], "sub": "Cartagena · 17", "tag": "carr"},
   {"fills": ["Nina", "Cusco", "dieciocho"], "sub": "Cusco · 18", "tag": "carr"},
   {"fills": ["Mateo", "Buenos Aires", "diecisiete"], "sub": "Buenos Aires · 17", "tag": "carr"},
   {"fills": ["Sam", "Bélgica", "dieciséis"], "sub": "België · 16", "tag": "carr"},
   {"fills": ["Marta", "Salamanca", "quince"], "sub": "Salamanca · 15", "tag": "carr"},
   {"fills": ["Pau", "Barcelona", "dieciocho"], "sub": "Barcelona · 18", "tag": "carr"}]))


if __name__ == "__main__":
    print("%d contentpakketten geschreven naar %s" % (len(gemaakt), D))
    for x in gemaakt:
        print("   ", x)
