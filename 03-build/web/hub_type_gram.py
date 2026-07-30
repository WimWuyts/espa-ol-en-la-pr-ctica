#!/usr/bin/env python3
"""Getypte grammatica-drills voor het paneel «Gramática» van elke hub.

Waar `hub_type_sets` de woordenschat automatisch uit `u<N>_vocab.json` haalt, is
grammatica per unit anders: de items worden hier met de hand geschreven en
nagerekend. Dit bestand is de enige plaats waar dat gebeurt — de generatoren
roepen alleen `js(cursus, unit)` aan en krijgen niets terug zolang een unit nog
niet is uitgeschreven. Zo kan de bouw unit per unit aangroeien zonder dat er
ooit nog aan de zeventien generatoren geraakt moet worden.

Beleid:
  * `accents:'strict'` bij werkwoordsvormen en bij de tilde-regel zelf — daar ís
    het accent de leerstof (hablo ≠ habló, cafe ≠ café).
  * `accents:'soft'` bij lidwoorden en losse woordenschatvormen.
  * Elke set bevat de klassieke cloze uit CLAUDE.md §14bis: de leerling vult
    zelf de correcte vorm in, zonder keuzelijst.
  * Scope III-Spa-d: presente de indicativo. Géén futuro simple, condicional of
    subjuntivo — ook niet als afleider.
"""
import json

# --------------------------------------------------------------------------- #
#  Slots — worden in het paneel Gramática gezet, ná de bestaande oefeningen.
# --------------------------------------------------------------------------- #
SLOTS_HTML = """    <h3 class="subh">✍️ Escribe tú — la gramática sin opciones</h3>
    <p class="lead">Geen keuzelijst: je <b>schrijft</b> de vorm zelf. <span class="gloss">Bij
    werkwoorden en bij de tilde tellen de accenten mee — dat ís hier de leerstof.</span></p>
    <div class="card ex escribe" id="gt_1"></div>
    <div class="card ex escribe" id="gt_2"></div>
    <div class="card ex escribe" id="gt_3"></div>
"""

# --------------------------------------------------------------------------- #
#  De sets, per (cursus, unit). Slot 1-2-3 in volgorde van de leerladder.
# --------------------------------------------------------------------------- #
SETS = {}

SETS[("C5", 0)] = [
    dict(title="Escribe la palabra con tilde", accents="strict",
         desc="Het woord staat er zónder accent. Schrijf het <b>juist</b>: met tilde als de regel "
              "het vraagt, zonder als ze dat niet doet.",
         items=[
             {"q": "cafe", "ans": "café", "hint": "c___", "why": "aguda op klinker → tilde"},
             {"q": "casa", "ans": "casa", "hint": "c___", "why": "llana op klinker → géén tilde"},
             {"q": "adios", "ans": "adiós", "hint": "a____", "why": "aguda op -s → tilde"},
             {"q": "Mexico", "ans": "México", "hint": "M_____", "why": "esdrújula → altijd tilde"},
             {"q": "musica", "ans": "música", "hint": "m_____", "why": "esdrújula → altijd tilde"},
             {"q": "lunes", "ans": "lunes", "hint": "l____", "why": "llana op -s → géén tilde"},
             {"q": "jamon", "ans": "jamón", "hint": "j____", "why": "aguda op -n → tilde"},
             {"q": "arbol", "ans": "árbol", "hint": "á____", "why": "llana op -l → tilde"},
             {"q": "telefono", "ans": "teléfono", "hint": "t_______", "why": "esdrújula → altijd tilde"},
             {"q": "reloj", "ans": "reloj", "hint": "r____", "why": "aguda op -j → géén tilde"},
             {"q": "silaba", "ans": "sílaba", "hint": "s_____", "why": "esdrújula → altijd tilde"},
             {"q": "Peru", "ans": "Perú", "hint": "P___", "why": "aguda op klinker → tilde"},
         ]),
    dict(title="¿el o la? — escribe el artículo", accents="soft",
         desc="Schrijf het lidwoord voluit. Let op de valstrikken: niet elk woord op <b>-a</b> is "
              "vrouwelijk, en niet elk woord op <b>-o</b> is mannelijk.",
         items=[
             {"q": "___ mapa", "ans": "el", "why": "el mapa — valstrik: -a maar masculino"},
             {"q": "___ casa", "ans": "la", "why": "la casa"},
             {"q": "___ problema", "ans": "el", "why": "-ma (Grieks) → masculino"},
             {"q": "___ ciudad", "ans": "la", "why": "-dad → femenino"},
             {"q": "___ día", "ans": "el", "why": "el día — valstrik"},
             {"q": "___ mano", "ans": "la", "why": "la mano — valstrik: -o maar femenino"},
             {"q": "___ idioma", "ans": "el", "why": "-ma → masculino"},
             {"q": "___ letra", "ans": "la", "why": "la letra"},
             {"q": "___ país", "ans": "el", "why": "el país"},
             {"q": "___ sílaba", "ans": "la", "why": "la sílaba"},
             {"q": "___ número", "ans": "el", "why": "el número"},
             {"q": "___ clase", "ans": "la", "why": "la clase"},
         ]),
    dict(title="Escribe el número en letras", accents="strict",
         desc="Schrijf het getal voluit. De accenten van <b>dieciséis</b> en <b>veintidós</b> "
              "horen erbij.",
         items=[
             {"q": "0 =", "ans": "cero", "hint": "c___"},
             {"q": "5 =", "ans": "cinco", "hint": "c____"},
             {"q": "11 =", "ans": "once", "hint": "o___"},
             {"q": "13 =", "ans": "trece", "hint": "t____"},
             {"q": "15 =", "ans": "quince", "hint": "q_____"},
             {"q": "16 =", "ans": "dieciséis", "hint": "d________", "why": "16–29 = één woord, met tilde"},
             {"q": "20 =", "ans": "veinte", "hint": "v_____"},
             {"q": "21 =", "ans": "veintiuno", "hint": "v________", "why": "één woord"},
             {"q": "22 =", "ans": "veintidós", "hint": "v________", "why": "aguda op -s → tilde"},
             {"q": "30 =", "ans": "treinta", "hint": "t______"},
             {"q": "45 =", "ans": "cuarenta y cinco", "hint": "c_______ y c____", "why": "vanaf 31 met «y»"},
             {"q": "100 =", "ans": "cien", "hint": "c___", "why": "100 alleen = cien"},
         ]),
]

SETS[("C5", 1)] = [
    dict(title="El presente regular — rellena el verbo", accents="strict",
         desc="De klassieke invuloefening: schrijf het werkwoord tussen haakjes in de juiste vorm. "
              "Alle werkwoorden hier zijn <b>regelmatig</b> — je hoeft niets uit het hoofd te "
              "kennen, alleen de uitgang te kiezen.",
         items=[
             {"q": "Yo ___ (hablar) español en clase.", "ans": "hablo", "hint": "h____", "why": "-ar · yo → -o"},
             {"q": "Tú ___ (estudiar) en Madrid.", "ans": "estudias", "hint": "e_______", "why": "-ar · tú → -as"},
             {"q": "Lucía ___ (vivir) en Sevilla.", "ans": "vive", "hint": "v___", "why": "-ir · ella → -e"},
             {"q": "Nosotros ___ (comer) en casa.", "ans": "comemos", "hint": "c______", "why": "-er · nosotros → -emos"},
             {"q": "Los alumnos ___ (escribir) un mensaje.", "ans": "escriben", "hint": "e_______", "why": "-ir · ellos → -en"},
             {"q": "Yo ___ (aprender) español este año.", "ans": "aprendo", "hint": "a______", "why": "-er · yo → -o"},
             {"q": "¿Tú ___ (trabajar) los sábados?", "ans": "trabajas", "hint": "t_______", "why": "-ar · tú → -as"},
             {"q": "Diego ___ (escuchar) música.", "ans": "escucha", "hint": "e______", "why": "-ar · él → -a"},
             {"q": "Nosotros ___ (leer) un libro.", "ans": "leemos", "hint": "l_____", "why": "-er · nosotros → -emos"},
             {"q": "Mis amigos ___ (bailar) muy bien.", "ans": "bailan", "hint": "b_____", "why": "-ar · ellos → -an"},
             {"q": "¿Dónde ___ (vivir) tú?", "ans": "vives", "hint": "v____", "why": "-ir · tú → -es"},
             {"q": "Nina ___ (beber) agua.", "ans": "bebe", "hint": "b___", "why": "-er · ella → -e"},
         ]),
    dict(title="¿ser o tener? — escribe la forma", accents="strict",
         desc="Let op de valstrik voor Nederlandstaligen: je <b>bent</b> geen vijftien in het "
              "Spaans, je <b>hebt</b> vijftien jaar — <i>tengo quince años</i>.",
         items=[
             {"q": "Yo ___ quince años.", "ans": "tengo", "why": "leeftijd → tener, nooit ser"},
             {"q": "Lucía ___ de Sevilla.", "ans": "es", "why": "herkomst → ser"},
             {"q": "Nosotros ___ estudiantes.", "ans": "somos", "why": "identiteit → ser"},
             {"q": "Diego ___ dieciséis años.", "ans": "tiene", "why": "leeftijd → tener"},
             {"q": "¿Cuántos años ___ tú?", "ans": "tienes", "why": "leeftijd vragen → tener"},
             {"q": "Tú ___ muy simpático.", "ans": "eres", "why": "eigenschap → ser"},
             {"q": "Mis padres ___ belgas.", "ans": "son", "why": "nationaliteit → ser"},
             {"q": "Yo ___ de Bélgica.", "ans": "soy", "why": "herkomst → ser"},
             {"q": "¿___ (tú) hermanos?", "ans": "tienes", "why": "bezit → tener"},
             {"q": "Valen ___ colombiana.", "ans": "es", "why": "nationaliteit → ser"},
             {"q": "Nosotros ___ catorce años.", "ans": "tenemos", "why": "leeftijd → tener"},
             {"q": "Ustedes ___ profesores.", "ans": "son", "why": "beroep → ser"},
         ]),
    dict(title="Las palabras interrogativas — escribe la pregunta", accents="strict",
         desc="Vul het vraagwoord in. <b>Elk vraagwoord draagt een accent</b> — dat is geen "
              "versiering maar het verschil tussen een vraag en een gewone zin.",
         items=[
             {"q": "¿___ te llamas? — Me llamo Nina.", "ans": "Cómo", "hint": "C___", "why": "cómo = hoe"},
             {"q": "¿De ___ eres? — Soy de Madrid.", "ans": "dónde", "hint": "d____", "why": "de dónde = waarvandaan"},
             {"q": "¿___ años tienes? — Tengo quince.", "ans": "Cuántos", "hint": "C______", "why": "cuántos = hoeveel (mv.)"},
             {"q": "¿___ es tu profesora? — La señora Ruiz.", "ans": "Quién", "hint": "Q____", "why": "quién = wie"},
             {"q": "¿___ estudias? — Español.", "ans": "Qué", "hint": "Q__", "why": "qué = wat"},
             {"q": "¿___ es tu cumpleaños? — En mayo.", "ans": "Cuándo", "hint": "C_____", "why": "cuándo = wanneer"},
             {"q": "¿___ vives? — En Sevilla.", "ans": "Dónde", "hint": "D____", "why": "dónde = waar"},
             {"q": "¿___ hermanos tienes? — Dos.", "ans": "Cuántos", "hint": "C______", "why": "cuántos hermanos"},
             {"q": "¿___ tal? — Bien, gracias.", "ans": "Qué", "hint": "Q__", "why": "¿Qué tal? = hoe gaat het?"},
             {"q": "¿___ se dice «mochila» en neerlandés?", "ans": "Cómo", "hint": "C___", "why": "cómo se dice = hoe zeg je"},
             {"q": "¿___ son ellos? — Son mis primos.", "ans": "Quiénes", "hint": "Q______", "why": "meervoud van quién"},
             {"q": "¿___ es tu número de teléfono?", "ans": "Cuál", "hint": "C___", "why": "cuál = welk(e), bij een keuze uit veel"},
         ]),
]

SETS[("C6+", 1)] = [
    dict(title="Los verbos reflexivos — rellena", accents="strict",
         desc="Vergeet het <b>pronombre</b> niet: bij een reflexief werkwoord horen er twee "
              "woorden in het gat — <i>me levanto</i>, niet <i>levanto</i>.",
         items=[
             {"q": "Yo ___ (levantarse) a las siete.", "ans": "me levanto", "hint": "m_ l______", "why": "yo → me"},
             {"q": "Diego ___ (ducharse) por la mañana.", "ans": "se ducha", "hint": "s_ d____", "why": "él → se"},
             {"q": "Nosotros ___ (acostarse) a las once.", "ans": "nos acostamos", "hint": "n__ a________",
              "why": "nosotros → nos · en géén o→ue bij nosotros"},
             {"q": "¿A qué hora ___ (despertarse) tú?", "ans": "te despiertas", "hint": "t_ d_________", "why": "tú → te · e→ie"},
             {"q": "Lucía ___ (vestirse) rápido.", "ans": "se viste", "hint": "s_ v____", "why": "e→i"},
             {"q": "Yo ___ (despertarse) muy temprano.", "ans": "me despierto", "hint": "m_ d________", "why": "e→ie"},
             {"q": "Mis hermanos ___ (peinarse) delante del espejo.", "ans": "se peinan", "hint": "s_ p_____", "why": "ellos → se"},
             {"q": "Nosotros ___ (lavarse) las manos.", "ans": "nos lavamos", "hint": "n__ l______", "why": "regelmatig"},
             {"q": "Nina ___ (acostarse) tarde.", "ans": "se acuesta", "hint": "s_ a______", "why": "o→ue"},
             {"q": "¿Tú ___ (afeitarse) todos los días?", "ans": "te afeitas", "hint": "t_ a______", "why": "tú → te"},
             {"q": "Yo ___ (llamarse) Valen.", "ans": "me llamo", "hint": "m_ l____", "why": "llamarse is ook reflexief"},
             {"q": "Los niños ___ (dormirse) en el sofá.", "ans": "se duermen", "hint": "s_ d______", "why": "o→ue"},
         ]),
    dict(title="El verbo gustar — ¿gusta o gustan?", accents="strict",
         desc="Bij <i>gustar</i> is het onderwerp niet de persoon maar het <b>ding</b>. Schrijf het "
              "pronombre én de juiste vorm: <i>me gusta el libro</i> · <i>me gustan los libros</i>.",
         items=[
             {"q": "A mí ___ el chocolate.", "ans": "me gusta", "hint": "m_ g____", "why": "één ding → gusta"},
             {"q": "A ti ___ los deportes.", "ans": "te gustan", "hint": "t_ g_____", "why": "meervoud → gustan"},
             {"q": "A Lucía ___ bailar.", "ans": "le gusta", "hint": "l_ g____", "why": "infinitivo telt als enkelvoud"},
             {"q": "A nosotros ___ las películas españolas.", "ans": "nos gustan", "hint": "n__ g_____", "why": "meervoud → gustan"},
             {"q": "A Diego y a Nina ___ la música.", "ans": "les gusta", "hint": "l__ g____", "why": "twee personen → les, maar la música → gusta"},
             {"q": "A mí ___ los libros de aventuras.", "ans": "me gustan", "hint": "m_ g_____", "why": "meervoud → gustan"},
             {"q": "¿___ el español? (a ti)", "ans": "te gusta", "hint": "t_ g____", "why": "el español → gusta"},
             {"q": "A mi hermana ___ los perros.", "ans": "le gustan", "hint": "l_ g_____", "why": "één persoon, meervoud ding"},
             {"q": "A nosotros ___ el fútbol.", "ans": "nos gusta", "hint": "n__ g____", "why": "enkelvoud → gusta"},
             {"q": "A mis padres ___ viajar.", "ans": "les gusta", "hint": "l__ g____", "why": "infinitivo → gusta"},
             {"q": "A ti ___ las matemáticas.", "ans": "te gustan", "hint": "t_ g_____", "why": "meervoud → gustan"},
             {"q": "A mí no ___ madrugar.", "ans": "me gusta", "hint": "m_ g____", "why": "infinitivo → gusta"},
         ]),
    dict(title="La hora — escríbela en letras", accents="soft",
         desc="Schrijf het uur voluit. Eén uur is <b>es la una</b>, alle andere uren zijn "
              "<b>son las…</b> — dat verschil is de hele oefening.",
         items=[
             {"q": "3:00 →", "ans": "Son las tres", "hint": "S__ l__ t___"},
             {"q": "1:00 →", "ans": "Es la una", "hint": "E_ l_ u__", "why": "enkelvoud: es la una"},
             {"q": "3:15 →", "ans": "Son las tres y cuarto", "hint": "S__ l__ t___ y c_____"},
             {"q": "5:30 →", "ans": "Son las cinco y media", "hint": "S__ l__ c____ y m____"},
             {"q": "8:45 →", "ans": "Son las nueve menos cuarto", "hint": "S__ l__ n____ m____ c_____",
              "why": "vanaf 31 minuten reken je terug naar het volgende uur"},
             {"q": "2:10 →", "ans": "Son las dos y diez", "hint": "S__ l__ d__ y d___"},
             {"q": "7:50 →", "ans": "Son las ocho menos diez", "hint": "S__ l__ o___ m____ d___"},
             {"q": "12:00 →", "ans": "Son las doce", "hint": "S__ l__ d___"},
             {"q": "6:20 →", "ans": "Son las seis y veinte", "hint": "S__ l__ s___ y v_____"},
             {"q": "10:40 →", "ans": "Son las once menos veinte", "hint": "S__ l__ o___ m____ v_____"},
             {"q": "1:30 →", "ans": "Es la una y media", "hint": "E_ l_ u__ y m____", "why": "één uur blijft «es la»"},
             {"q": "4:05 →", "ans": "Son las cuatro y cinco", "hint": "S__ l__ c_____ y c____"},
         ]),
]

SETS[("C6+", 0)] = [
    dict(title="El presente — rellena el verbo", accents="strict",
         desc="De klassieke invuloefening: schrijf het werkwoord tussen haakjes in de juiste vorm "
              "van het <b>presente</b>. Accenten tellen mee.",
         items=[
             {"q": "Yo ___ (hablar) español en clase.", "ans": "hablo", "hint": "h____", "why": "-ar, yo → -o"},
             {"q": "Nosotros ___ (comer) a las dos.", "ans": "comemos", "hint": "c______", "why": "-er, nosotros → -emos"},
             {"q": "Diego ___ (vivir) en México.", "ans": "vive", "hint": "v___", "why": "-ir, él → -e"},
             {"q": "¿Tú ___ (estudiar) francés?", "ans": "estudias", "hint": "e_______", "why": "-ar, tú → -as"},
             {"q": "Ellos ___ (escribir) un mensaje.", "ans": "escriben", "hint": "e_______", "why": "-ir, ellos → -en"},
             {"q": "Yo ___ (ser) de Bélgica.", "ans": "soy", "hint": "s__", "why": "ser is onregelmatig"},
             {"q": "Valen ___ (tener) quince años.", "ans": "tiene", "hint": "t____", "why": "tener: e → ie"},
             {"q": "Nosotros ___ (ir) al instituto.", "ans": "vamos", "hint": "v____", "why": "ir is onregelmatig"},
             {"q": "¿Qué ___ (hacer) tú los sábados?", "ans": "haces", "hint": "h____", "why": "hacer: yo hago, tú haces"},
             {"q": "Mis amigos ___ (venir) a las seis.", "ans": "vienen", "hint": "v_____", "why": "venir: e → ie"},
             {"q": "La profesora ___ (dar) los deberes.", "ans": "da", "hint": "d_", "why": "dar: yo doy, ella da"},
             {"q": "Yo ___ (estar) en casa.", "ans": "estoy", "hint": "e____", "why": "estar is onregelmatig"},
         ]),
    dict(title="¿ser o estar? — escribe la forma", accents="strict",
         desc="Geen keuze tussen twee knoppen: schrijf de <b>vorm</b> zelf. Denk aan wat je zegt — "
              "wie of wat iets ís (ser), of waar en hoe iets ís (estar).",
         items=[
             {"q": "Lucía ___ de Sevilla.", "ans": "es", "why": "herkomst → ser"},
             {"q": "Hoy yo ___ cansado.", "ans": "estoy", "why": "gevoel/toestand → estar"},
             {"q": "Nosotros ___ estudiantes.", "ans": "somos", "why": "identiteit → ser"},
             {"q": "El libro ___ encima de la mesa.", "ans": "está", "why": "plaats → estar (mét tilde)"},
             {"q": "Diego y Nina ___ simpáticos.", "ans": "son", "why": "eigenschap → ser"},
             {"q": "¿Dónde ___ tú?", "ans": "estás", "why": "plaats → estar (mét tilde)"},
             {"q": "Madrid ___ en España.", "ans": "está", "why": "plaats → estar"},
             {"q": "Yo ___ belga.", "ans": "soy", "why": "nationaliteit → ser"},
             {"q": "La ventana ___ abierta.", "ans": "está", "why": "toestand → estar"},
             {"q": "¿Ustedes ___ de Colombia?", "ans": "son", "why": "herkomst → ser"},
             {"q": "Mi madre ___ profesora.", "ans": "es", "why": "beroep → ser"},
             {"q": "Los niños ___ en el parque.", "ans": "están", "why": "plaats → estar (mét tilde)"},
         ]),
    dict(title="Concordancia — escribe la forma correcta", accents="strict",
         desc="Schrijf het woord tussen haakjes in de vorm die <b>overeenkomt</b> met het onderwerp: "
              "mannelijk of vrouwelijk, enkelvoud of meervoud.",
         items=[
             {"q": "Nina es del Perú. Es ___ (peruano).", "ans": "peruana", "hint": "p______", "why": "vrouwelijk enkelvoud"},
             {"q": "Diego es de México. Es ___ (mexicano).", "ans": "mexicano", "hint": "m_______", "why": "mannelijk enkelvoud"},
             {"q": "Lucía y su hermana son ___ (español).", "ans": "españolas", "hint": "e________", "why": "vrouwelijk meervoud"},
             {"q": "Los chicos son ___ (colombiano).", "ans": "colombianos", "hint": "c__________", "why": "mannelijk meervoud"},
             {"q": "La casa es ___ (bonito).", "ans": "bonita", "hint": "b_____", "why": "la casa → -a"},
             {"q": "Los libros son ___ (interesante).", "ans": "interesantes", "hint": "i___________", "why": "-e → alleen +s in het meervoud"},
             {"q": "Mi amiga es ___ (belga).", "ans": "belga", "hint": "b____", "why": "belga verandert niet van vorm"},
             {"q": "Las ciudades son ___ (grande).", "ans": "grandes", "hint": "g______", "why": "-e → +s"},
             {"q": "El profesor es ___ (simpático).", "ans": "simpático", "hint": "s________", "why": "mannelijk enkelvoud, mét tilde"},
             {"q": "Las profesoras son ___ (simpático).", "ans": "simpáticas", "hint": "s_________", "why": "vrouwelijk meervoud, mét tilde"},
             {"q": "Valen es ___ (alto).", "ans": "alta", "hint": "a___", "why": "Valen is een meisje → -a"},
             {"q": "Mis primos son ___ (argentino).", "ans": "argentinos", "hint": "a_________", "why": "mannelijk meervoud"},
         ]),
]


# --------------------------------------------------------------------------- #
def heeft(course, unit):
    return (course, unit) in SETS


def js(course, unit, per=12):
    """JS-blok met de getypte grammatica-drills; leeg als de unit nog niet af is."""
    sets = SETS.get((course, unit))
    if not sets:
        return ""
    out = ["function buildGramType(){"]
    for i, s in enumerate(sets[:3], 1):
        out.append(" buildType('gt_%d',{title:%s,desc:%s,accents:'%s',perBlock:%d,expect:%d,items:%s});"
                   % (i, json.dumps(s["title"], ensure_ascii=False),
                      json.dumps(s["desc"], ensure_ascii=False), s.get("accents", "soft"),
                      per, len(s["items"]), json.dumps(s["items"], ensure_ascii=False)))
    out.append("}")
    out.append("buildGramType();")
    return "\n".join(out) + "\n"


def slots(course, unit):
    """Alleen slots plaatsen als er ook inhoud voor is — geen lege kaders."""
    return SLOTS_HTML if heeft(course, unit) else ""


if __name__ == "__main__":
    for (c, u), sets in sorted(SETS.items()):
        n = sum(len(s["items"]) for s in sets)
        print("%-4s U%d  %d drills · %d typvelden  (%s)"
              % (c, u, len(sets), n, " · ".join(s["title"] for s in sets)))
