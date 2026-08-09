#!/usr/bin/env python3
"""De fouten die Nederlandstalige leerlingen écht maken, als regels.

WAAROM DIT BESTAAT
De oefenpartner op de digitale pagina werkt offline: er zit geen taalmodel
achter, alleen wat wij er zelf in stoppen. Dat is een bewuste keuze (auteur
2026-08-09: leerlingtekst verlaat de school niet, en op de gekozen host is er
geen plaats voor een geheime sleutel). De prijs ervan is dat de partner alleen
herkent wat hier staat.

DE REGEL DIE DAARUIT VOLGT — EN DIE BINDEND IS
Een verbeteraar die niet alles kent, mag **nooit «goed!» zeggen**. Doet hij dat
toch, dan leert een leerling dat een foute zin juist is, en dat is erger dan
geen feedback. Hij zegt dus: «ik zie hier geen fouten die ik ken.» Iets minder
bevredigend, maar het is wat waar is. `gen_rol.py` houdt zich daaraan.

WAT HIER WÉL EN NIET IN HOORT
Wél: de valstrikken die uit het Nederlands komen en die in élke unit terug
kunnen komen (CLAUDE.md §4 noemt er een paar met naam). Niet: fouten tegen
leerstof die pas later aan bod komt — anders wordt een leerling verbeterd op
iets wat hij nog niet gezien heeft.

Elke regel: (id, patroon, wat er misgaat, hoe het wél moet, vanaf welke unit).
`desde` is per cursus, want de leerstof loopt niet gelijk: ("C5", 2) betekent
dat de regel pas meedoet vanaf C5 unidad 2. Een regel zonder `desde` geldt
altijd.

Het patroon is JavaScript-regex (de partner draait in de browser), zonder
schuine strepen, en wordt hoofdletterongevoelig toegepast.
"""

# ── de valstrikken ──────────────────────────────────────────────────────────
# (id, patroon, uitleg-NL, voorbeeld-goed, desde)
REGLAS = [
 # ── gustar: het klassieke struikelblok ────────────────────────────────────
 ("gustar-yo", r"\byo\s+gust",
  "«Ik vind leuk» is in het Spaans omgekeerd: het ding bevalt <b>mij</b>. "
  "Dus niet «yo gusto» maar <b>me gusta</b>.",
  "Me gusta el chocolate.", None),
 ("gustar-tu", r"\bt[uú]\s+gustas\b",
  "Ook hier omgekeerd: niet «tú gustas» maar <b>te gusta</b>.",
  "¿Te gusta la paella?", None),
 ("gustar-concordancia", r"\bme\s+gusta\s+los\b|\bme\s+gusta\s+las\b",
  "Meervoud: bij meer dan één ding wordt het <b>me gustan</b>.",
  "Me gustan los tacos.", None),

 # ── ser ↔ estar ───────────────────────────────────────────────────────────
 ("estar-frio-persoon", r"\b(estoy|est[aá]s|est[aá])\s+(fr[ií]o|calor)\b",
  "Over jezelf gebruik je <b>tener</b>: «tengo frío». «Estoy frío» betekent dat "
  "je lichaam koud aanvoelt — dat is iets heel anders.",
  "Tengo frío. · Hace frío.", None),
 ("hacer-tiempo", r"\b(es|est[aá])\s+(fr[ií]o|calor|sol|viento)\b",
  "Het weer krijgt <b>hacer</b>: «hace frío», «hace sol».",
  "Hoy hace mucho calor.", None),
 ("ser-lugar", r"\bes\s+en\s+(la|el|mi|tu)\b",
  "Waar iets is, zeg je met <b>estar</b>, niet met «ser».",
  "El libro está en la mesa.", None),
 ("soy-anos", r"\bsoy\s+\w*\s*a[ñn]os\b|\bsoy\s+\d+\s*a[ñn]os\b",
  "Leeftijd krijgt <b>tener</b>: je «hébt» jaren in het Spaans.",
  "Tengo dieciséis años.", None),
 ("soy-de-ciudad-vivir", r"\bsoy\s+en\s+\w+",
  "«Ik kom uit» is <b>soy de</b>; «ik woon in» is <b>vivo en</b>.",
  "Soy de Gante y vivo en Brujas.", None),

 # ── voegwoorden: de twee die CLAUDE.md §4 met naam noemt ──────────────────
 ("luego-dus", r"\bluego\b",
  "«Dus» is <b>así que</b> of <b>por eso</b>. <i>Luego</i> betekent «later».",
  "Hace calor, así que voy a la playa.", None),
 ("porque-pregunta", r"\bporque\s+(no\s+)?(vas|vienes|comes|quieres|est[aá]s)\b\s*\?",
  "In een vráág schrijf je <b>por qué</b>: twee woorden, met accent. "
  "<i>Porque</i> (aan elkaar) is het antwoord.",
  "¿Por qué no vienes? — Porque estoy enfermo.", None),
 ("want-omdat", r"\b(want|omdat|dus)\b",
  "Er staat een Nederlands woord in je zin. «Want» én «omdat» zijn allebei "
  "<b>porque</b>; «dus» is <b>así que</b>.",
  "No como carne porque soy vegetariano.", None),

 # ── werkwoorden die een vast voorzetsel hebben ────────────────────────────
 ("ir-a", r"\bvoy\s+(el|la|los|las)\b",
  "Na <b>ir</b> hoort <b>a</b>: «voy a la playa», «voy al mercado».",
  "Voy a la escuela.", None),
 ("tener-que", r"\btengo\s+(de|a)\s+\w+ar\b|\btengo\s+(de|a)\s+\w+er\b",
  "«Ik moet» is <b>tengo que</b> + hele werkwoord.",
  "Tengo que estudiar.", None),
 ("ir-a-inf", r"\bvoy\s+\w+ar\b(?!\s)",
  "Een plan maak je met <b>voy a</b> + hele werkwoord.",
  "Voy a comer.", None),

 # ── woordgeslacht en overeenkomst ─────────────────────────────────────────
 ("el-agua-la", r"\bla\s+agua\b",
  "<b>El agua</b> — het is wél vrouwelijk, maar krijgt <i>el</i> omdat het met "
  "een beklemtoonde a begint. Het bijvoeglijk naamwoord blijft vrouwelijk.",
  "El agua está fría.", None),
 ("un-una-comida", r"\bun\s+(sopa|carta|cuenta|mesa|servilleta|cuchara|manzana|naranja|piña|lechuga|cebolla)\b",
  "Dit woord is vrouwelijk: <b>una</b>, niet «un».",
  "Una sopa, por favor.", None),
 ("una-masculino", r"\buna\s+(pan|queso|pollo|pescado|arroz|plato|vaso|tenedor|cuchillo|caf[eé]|men[uú])\b",
  "Dit woord is mannelijk: <b>un</b>, niet «una».",
  "Un café, por favor.", None),

 # ── beleefdheid in een transactie ─────────────────────────────────────────
 # Let op de negatieve vooruitblik: staat «por favor» ergens in de zin, dan is
 # ze al beleefd en zwijgt de regel. Zonder dat sloeg ze alarm op «Quiero una
 # sopa, por favor» — precies de zin die we willen uitlokken.
 ("quiero-seco", r"^(?!.*por\s+favor)\s*(quiero|dame|trae)\b[^?]*$",
  "Dit klinkt kortaf. Zet er <b>por favor</b> bij, of gebruik "
  "<b>¿me pone…?</b> of <b>para mí…</b>.",
  "¿Me pone un café, por favor?", None),

 # ── typische spelfouten ───────────────────────────────────────────────────
 ("acento-que", r"\bque\s+(quiere|quieres|va|tal)\b\s*\?",
  "In een vraag draagt <b>qué</b> een accent.",
  "¿Qué quiere tomar?", None),
 ("apertura", r"^[^¿¡]*\w[^.!?]*\?\s*$",
  "In het Spaans staat het vraagteken er <b>twee keer</b>: ¿ aan het begin en "
  "? aan het eind.",
  "¿Cuánto cuesta?", None),
 ("nn-ñ", r"\b(anos|manana|nino|espanol|senor)\b",
  "Hier hoort een <b>ñ</b>: años · mañana · niño · español · señor.",
  "Tengo dieciséis años.", None),
]


def reglas_para(curso, unidad):
    """De regels die op dit punt in de leerlijn mogen meedoen.

    Een leerling verbeteren op iets wat hij nog niet gezien heeft, is geen
    feedback maar ontmoediging. Regels met een `desde` doen pas mee vanaf daar.
    """
    out = []
    for rid, patron, expl, bien, desde in REGLAS:
        if desde is not None:
            c, u = desde
            if c != curso or unidad < u:
                continue
        out.append({"id": rid, "re": patron, "nl": expl, "bien": bien})
    return out


if __name__ == "__main__":
    import re
    print("%d regels" % len(REGLAS))
    malas = []
    for rid, patron, _e, _b, _d in REGLAS:
        try:
            re.compile(patron)
        except re.error as e:                       # noqa: PERF203
            malas.append((rid, e))
    print("ongeldige patronen:", malas or "geen")
    # een paar zinnen die fout MOETEN worden gevonden, en een paar die mogen blijven
    prueba = [("Yo gusto el chocolate.", True), ("Me gusta el chocolate.", False),
              ("Estoy frío.", True), ("Tengo frío.", False),
              ("Hace calor, luego voy a la playa.", True),
              ("Hace calor, así que voy a la playa.", False),
              ("Tengo dieciseis anos.", True), ("Tengo dieciséis años.", False),
              ("La agua está fría.", True), ("El agua está fría.", False),
              ("Un sopa, por favor.", True), ("Una sopa, por favor.", False)]
    # Vals alarm is erger dan een gemiste fout: een leerling die op een góéde
    # zin verbeterd wordt, gelooft de partner daarna niet meer. Dit zijn de
    # zinnen die het rollenspel juist wil uitlokken; ze moeten stil blijven.
    prueba += [(f, False) for f in (
        "Quiero una sopa, por favor.", "Para mí, un café.", "¿Me pone un agua?",
        "¿Me trae la cuenta, por favor?", "Una mesa para dos, por favor.",
        "Quiero un taco de pollo, por favor.", "De postre, los churros.",
        "Voy a tomar un refresco.", "Sí, gracias.", "¿Cuánto cuesta?",
        "Me gustan los tacos.", "Buenas tardes.", "La cuenta, por favor.")]
    prueba += [(f, True) for f in ("Quiero una sopa.", "Dame un café.")]

    fallos = 0
    for frase, debe in prueba:
        hits = [rid for rid, p, _e, _b, _d in REGLAS
                if re.search(p, frase, re.I)]
        ok = bool(hits) == debe
        fallos += not ok
        print("   %s %-42s %s" % ("ok " if ok else "MIS", frase,
                                  ", ".join(hits) or "—"))
    print("%d van de %d proefzinnen kloppen%s"
          % (len(prueba) - fallos, len(prueba),
             "" if not fallos else "  ← NAKIJKEN"))
