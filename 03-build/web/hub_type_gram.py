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
