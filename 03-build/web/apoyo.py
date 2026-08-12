#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""De steun onder een oefening — wat de leerling krijgt, niet hoe het heet.

WAAROM DIT ZO IS
Er stond «Steun · Marco» onder een oefening. De auteur: *«Wat bedoel je met
Steun Marco?»* en later *«Waar slaat die Marco op?»*. Marco is de naam van een
trede in de steunladder (modelo → banco → marco → primera letra → sin ayuda) uit
CLAUDE.md §14 — ontwerptaal, geen woord dat een leerling van vijftien kan raden.

De ladder blijft bestaan in het ontwerp en in het docentendossier, maar op de
leerlingbladzijde staat nu alleen nog **wat de hulp is**:

    Apoyo · steun: Creo que… porque…
    Apoyo · steun: las palabras que necesitas están en el recuadro

Dat maakte ook zichtbaar wat er misging: 77 oefeningen hadden `apoyo="Marco"`
zónder frame erachter. Die steunregel zei de leerling niets. Ze zijn ingevuld
met het échte frame; waar er geen zinvolle hulp bestond, is de regel geschrapt.

De Nederlandse detailteksten («tabel open», «onderstreep in de tekst») staan
hier vertaald, op één plaats, zodat alle 31 units meeveranderen.

GEBRUIK
    import apoyo
    apoyo.html("Marco: wat/waar/wanneer/waarom")   → <div class="steun">…</div>
    apoyo.texto("Pista")                            → platte tekst
    apoyo.nivel("Marco: …")                         → «Marco», voor het dossier
"""

import re

# ── de vijf niveaus + hun Nederlandse woord ────────────────────────────────
# De volgorde is die van de steunladder: van veel hulp naar geen.
NIVELES = [
    ("Modelo",            "voorbeeld"),
    ("Banco de palabras", "woordenbank"),
    ("Marco",             "zinsframe"),
    ("Primera letra",     "eerste letter"),
    ("Letra inicial",     "eerste letter"),
    ("Pista",             "tip"),
    ("Sin ayuda",         "zonder hulp"),
]
_NIV = dict(NIVELES)

# ── de detailtekst achter het niveau ───────────────────────────────────────
# Wat hier stond was half Nederlands. Elke regel: Nederlands → (Spaans, Nederlands).
# Staat een detail hier niet in, dan gaat het ongewijzigd door (het is dan al
# Spaans of het is een modelzin).
DETALLE = {
    "tabel open": ("la tabla queda abierta", "de tabel blijft open"),
    "tabel ser open": ("la tabla de ser queda abierta", "de tabel van ser blijft open"),
    "tabel §3.1": ("la tabla del §3.1", "de tabel uit §3.1"),
    "tabel §3.1 open → PISTA": ("la tabla del §3.1 queda abierta",
                                "de tabel uit §3.1 blijft open"),
    "tabla boven": ("la tabla de arriba", "de tabel hierboven"),
    "tabla arriba": ("la tabla de arriba", "de tabel hierboven"),
    "tekst boven": ("el texto de arriba", "de tekst hierboven"),
    "anuncio boven": ("el anuncio de arriba", "de advertentie hierboven"),
    "menús boven": ("los menús de arriba", "de menu's hierboven"),
    "escala boven": ("la escala de arriba", "de schaal hierboven"),
    "de escala boven": ("la escala de arriba", "de schaal hierboven"),
    "plano gegeven": ("tienes el plano", "je krijgt het plattegrondje"),
    "labels gegeven": ("las etiquetas están puestas", "de labels staan er al"),
    "haber gegeven": ("tienes la forma de haber", "de vorm van haber staat er"),
    "infinitief gegeven": ("tienes el infinitivo", "het infinitief staat erbij"),
    "werkwoord gegeven": ("tienes el verbo", "het werkwoord staat erbij"),
    "pronombre gegeven": ("tienes el pronombre", "het pronomen staat erbij"),
    "lijn gegeven": ("la línea está marcada", "de lijn staat er al"),
    "vier opties open": ("las cuatro opciones quedan a la vista",
                         "de vier opties blijven zichtbaar"),
    "vier reacties": ("cuatro reacciones posibles", "vier mogelijke reacties"),
    "twee keer beluisteren": ("puedes escuchar dos veces", "je mag twee keer luisteren"),
    "audio 2×": ("puedes escuchar dos veces", "je mag twee keer luisteren"),
    "2×": ("dos veces", "twee keer"),
    "ronde 2 uit het hoofd": ("la segunda ronda, de memoria",
                              "ronde twee uit het hoofd"),
    "onderstreep in de tekst": ("subraya en el texto", "onderstreep in de tekst"),
    "onderstreep in de carta": ("subraya en la carta", "onderstreep in de kaart"),
    "valstrikken gemarkeerd": ("las trampas están marcadas", "de valstrikken staan gemarkeerd"),
    "de bewijszinnen staan gemarkeerd": ("las frases-prueba están marcadas",
                                         "de bewijszinnen staan gemarkeerd"),
    "de bewijszinnen staan gemarkeerd in de tekst":
        ("las frases-prueba están marcadas en el texto",
         "de bewijszinnen staan gemarkeerd in de tekst"),
    "namen zijn vetgedrukt": ("los nombres están en negrita", "de namen staan vet"),
    "ficha zichtbaar": ("la ficha queda a la vista", "de fiche blijft zichtbaar"),
    "regel zichtbaar": ("la regla queda a la vista", "de regel blijft zichtbaar"),
    "regel §1.1": ("la regla del §1.1", "de regel uit §1.1"),
    "regel §1.1 zichtbaar": ("la regla del §1.1 queda a la vista",
                             "de regel uit §1.1 blijft zichtbaar"),
    "regel §2.1": ("la regla del §2.1", "de regel uit §2.1"),
    "regel §3.1": ("la regla del §3.1", "de regel uit §3.1"),
    "regel §4.1": ("la regla del §4.1", "de regel uit §4.1"),
    "regel §5.1": ("la regla del §5.1", "de regel uit §5.1"),
    "kijk naar de persoon": ("fíjate en la persona", "kijk naar de persoon"),
    "kijk naar de persoon → juist pronomen":
        ("fíjate en la persona → así eliges el pronombre",
         "kijk naar de persoon: die bepaalt het pronomen"),
    "kijk naar de hele zin": ("fíjate en la frase entera", "kijk naar de hele zin"),
    "kijk naar geslacht + getal": ("fíjate en el género y el número",
                                   "kijk naar geslacht en getal"),
    "kijk of het meervoud is": ("fíjate si es plural", "kijk of het meervoud is"),
    "tel de dingen": ("cuenta las cosas", "tel de dingen"),
    "de klok helpt": ("el reloj te ayuda", "de klok helpt"),
    "de tientallen ken je uit U1": ("las decenas ya las sabes de la U1",
                                    "de tientallen ken je uit U1"),
    "de vormen van ir staan in §2.1": ("las formas de ir están en el §2.1",
                                       "de vormen van ir staan in §2.1"),
    "kleine letter": ("en minúscula", "met kleine letter"),
    "het rangtelwoord eindigt op -o": ("el ordinal acaba en -o",
                                       "het rangtelwoord eindigt op -o"),
    "begin met het onderwerp": ("empieza por el sujeto", "begin bij het onderwerp"),
    "cita = kopieer een zin": ("cita = copia una frase del texto",
                               "citeren = een zin uit de tekst overschrijven"),
    "vorm van acabar": ("la forma de acabar", "de vorm van acabar"),
    "zoek de prenda ervoor": ("busca antes la prenda", "zoek eerst het kledingstuk"),
    "wat/waar/wanneer/waarom": ("qué · dónde · cuándo · por qué",
                                "wat · waar · wanneer · waarom"),
    "persoon/vraag/ja/meer": ("persona · pregunta · sí · más",
                              "persoon · vraag · ja · meer"),
    "uur → de la": ("la hora → de la mañana / de la tarde",
                    "bij een uur: de la mañana / de la tarde"),
    "OI-tabel": ("la tabla del objeto indirecto", "de tabel van het meewerkend voorwerp"),
    "a + één persoon → le · a + meer → les":
        ("a + una persona → le · a + varias → les",
         "aan één persoon → le · aan meer → les"),
    "vraag je af of de handeling het decor is of de gebeurtenis":
        ("pregúntate si la acción es el decorado o el hecho",
         "vraag je af of de handeling het decor is of de gebeurtenis"),
    "werkwoord + pronomen = één woord; het accent blijft op de klemtoon van het werkwoord":
        ("verbo + pronombre = una palabra; el acento se queda donde estaba",
         "werkwoord + pronomen worden één woord; de klemtoon blijft waar ze stond"),
    "mañana/finde → ir a · ahora mismo/ya → acabar de":
        ("mañana/finde → ir a · ahora mismo/ya → acabar de",
         "toekomst → ir a · net gebeurd → acabar de"),
    "MODELO-correctie": ("con el modelo delante", "met het voorbeeld erbij"),
    "docent leest voor": ("lo lee el profe", "de leerkracht leest voor"),
    "docent/audio": ("lo lee el profe o el audio", "leerkracht of audio"),
    "docent/audio leest voor": ("lo lee el profe o el audio",
                                "leerkracht of audio leest voor"),
    "eerste letter": ("tienes la primera letra", "je krijgt de eerste letter"),
    # de twee gedeelde blokken (lectura · escucha) geven hun steun in het Spaans
    "el texto queda a la vista": ("el texto queda a la vista",
                                  "de tekst blijft zichtbaar"),
    "16–29 = één woord": ("del 16 al 29 se escribe en una palabra",
                          "16–29 schrijf je als één woord"),
    "schrijf als één woord, zonder «y»": ("en una sola palabra, sin «y»",
                                          "als één woord, zonder «y»"),
}

_RE_NIV = re.compile(r"^\s*(%s)\s*(?::\s*(.*))?$"
                     % "|".join(re.escape(n) for n, _ in NIVELES), re.I)


def _parte(txt):
    """(niveau_es, niveau_nl, detalle_es, detalle_nl) uit de ruwe tekst."""
    txt = (txt or "").strip()
    if not txt:
        return None
    m = _RE_NIV.match(txt)
    if m:
        nivel = next(n for n, _ in NIVELES if n.lower() == m.group(1).lower())
        detalle = (m.group(2) or "").strip()
    else:
        nivel, detalle = "", txt
    des, dnl = DETALLE.get(detalle, (detalle, ""))
    return (nivel, _NIV.get(nivel, ""), des, dnl)


# Wat een kaal niveau betekent, in gewone taal. Voor «Modelo», «Banco de
# palabras» en «Primera letra» valt dat te zeggen zonder de oefening te kennen:
# het beschrijft wat er op de bladzijde staat. Voor «Marco» en «Pista» niet —
# een frame en een tip zijn per oefening anders — dus die staan in de generator
# zelf, en een kale «Marco» levert géén steunregel meer op.
KALO = {
    "Modelo":            ("arriba tienes un ejemplo hecho", "er staat een voorbeeld boven"),
    "Banco de palabras": ("las palabras que necesitas están en el recuadro",
                          "de woorden die je nodig hebt, staan in het kader"),
    "Primera letra":     ("tienes la primera letra", "je krijgt de eerste letter"),
    "Sin ayuda":         ("sin ayuda", "zonder hulp"),
}


def nivel(txt):
    """De naam van de trede — voor het docentendossier, niet voor het boek."""
    p = _parte(txt)
    return p[0] if p else ""


def _piezas(txt):
    """(spaans, nederlands) van de hulp zelf, of None als er niets te zeggen valt."""
    p = _parte(txt)
    if not p:
        return None
    niv, _nl, des, dnl = p
    if des:
        return (des, dnl)
    return KALO.get(niv)


def texto(txt):
    """Platte tekst — voor de docentendossiers en de controle."""
    piezas = _piezas(txt)
    if not piezas:
        return ""
    es, nl = piezas
    return "Apoyo (steun): %s%s" % (es, " — %s" % nl if nl else "")


def html(txt, margen="12.5mm"):
    """Het steunregeltje onder een oefening."""
    piezas = _piezas(txt)
    if not piezas:
        return ""
    es, nl = piezas
    cuerpo = '<b>Apoyo</b> <span class="gloss">steun</span>: %s' % es
    if nl:
        cuerpo += ' <span class="gloss">— %s</span>' % nl
    estilo = ' style="margin-left:%s"' % margen if margen else ""
    return '<div class="steun"%s>%s</div>' % (estilo, cuerpo)


if __name__ == "__main__":
    for t in ("Marco", "Marco: wat/waar/wanneer/waarom", "Pista", "Modelo: tabel open",
              "Banco de palabras: tabel open", "Primera letra: h…",
              "Marco: Vivo en… / En mi ciudad hay…", "docent leest voor", ""):
        print("%-42s → %s" % ('"%s"' % t, texto(t)))
