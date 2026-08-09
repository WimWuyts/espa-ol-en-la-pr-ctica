#!/usr/bin/env python3
"""De scènes van U11–U14 — eigen materiaal, want er is geen sitcom-aflevering.

WAAROM DIT BESTAAT
C4 is gebouwd op veertien videolessen: de video is de leidraad, het transcript
staat exact in de unit. Voor aflevering 11 tot 14 is dat transcript er niet, en
`00-brondocumenten/videos-jaar4/` is leeg. Een transcript verzinnen van een
video die wél bestaat is geen optie — dan staat er straks iets in de cursus dat
de leerling niet hoort.

`HANDOVER_C4.md` voorziet die situatie: *«Zonder transcript: bouw native op de
kernwoordenschat.»* Dat is wat hier gebeurt. Elke unit krijgt een eigen scène
met dezelfde vorm als de sitcom — twee tot drie escenas, personages die
terugkomen, chunks om mee te nemen — ingesproken met de acht Castiliaanse
stemmen uit `voces.py`.

Komt het transcript er later alsnog, dan is dit bestand de plek waar de scène
vervangen wordt; de generator, de oefeningen en de print veranderen niet mee.

De personages zijn dezelfde vier die ook in `comprension_data` optreden — Ana,
Nico, Alba en Iván — zodat de leerling ze door de laatste vier units heen leert
kennen in plaats van elke keer nieuwe namen te krijgen.
"""

# ── de sitcom-afleveringen ──────────────────────────────────────────────────
# De video's stáán er wel (Google Drive, gedeeld als «iedereen met de link mag
# lezen» — nagekeken op 2026-08-09); alleen de transcripten ontbreken nog. De
# video is dus ingebouwd en de leerling kan kijken; de scène hieronder is
# voorlopig het materiaal om mee te lezen en mee te oefenen.
#
# Zodra een transcript er is: zet het in `escenas` van die unit, precies zoals
# U1–U10 het doen, en de meelees-laag hangt vanzelf onder de video.
VIDEO = {
 11: ("drive", "1saLd6_-eTVUTVbv1v8KbKwfYp3Ale6-D"),   # Spanish Sitcom 11
 12: ("drive", "1RYpXlOwL3g5FBwSviROpE0AvkwNlh5fZ"),   # Spanish Sitcom 12
 13: ("drive", "1ic6FvmvjPQsM05DsiMY0DVlPBBlMsNYK"),   # Spanish Sitcom 13
 14: ("drive", "1Vuh5f76hi_hnuMaCMLroSUMEDnJ3t3kZ"),   # Spanish Sitcom 14
}

# Er is ook een aflevering 15 (1OMxB9gRZ9LdYYDGOl5_JiiGEAkXPsxfi). C4 heeft
# veertien thema's, dus die blijft voorlopig ongebruikt.

# unit → (titel, ondertitel-NL, [(kop, intro-NL, [(spreker, es, nl)])], [chunks])
ESCENAS = {
 11: {
  "titulo": "¡Vamos de rebajas!",
  "tema": "De compras · la ropa",
  "intro": "Ana en Nico gaan winkelen in de solden. Let op elke <b>prijs</b>, "
           "elke <b>talla</b> en op wat je zegt aan de kassa.",
  "chunks": ["¿Cuánto cuesta", "está de rebajas", "¿Qué talla", "la talla mediana",
             "¿Puedo probármela", "el probador", "me lo llevo", "a mitad de precio",
             "es un poco caro", "¿Tiene una talla más grande", "en efectivo o con tarjeta",
             "¿Me hace un descuento"],
  "escenas": [
   ("Escena 1 · En el escaparate",
    "Voor de etalage: wat kost wat?",
    [("Ana", "¡Mira, Nico! Todo está de rebajas.",
      "Kijk, Nico! Alles is in de solden."),
     ("Nico", "¿Cuánto cuesta esa camiseta azul?",
      "Hoeveel kost dat blauwe T-shirt?"),
     ("Ana", "Antes quince euros, ahora nueve. ¡Qué bien!",
      "Eerst vijftien euro, nu negen. Wat goed!"),
     ("Nico", "¿Y los pantalones vaqueros? Son bonitos.",
      "En de jeans? Die zijn mooi."),
     ("Ana", "Veinticinco. Y el segundo, a mitad de precio.",
      "Vijfentwintig. En de tweede voor de helft van de prijs.")]),
   ("Escena 2 · En la tienda",
    "Binnen: maat vragen en passen.",
    [("Nico", "Buenas. ¿Qué talla tiene esta camiseta?",
      "Hallo. Welke maat heeft dit T-shirt?"),
     ("Dependienta", "Pequeña, mediana y grande. ¿Cuál necesitas?",
      "Small, medium en large. Welke heb je nodig?"),
     ("Nico", "La talla mediana. ¿Puedo probármela?",
      "Medium. Mag ik ze passen?"),
     ("Dependienta", "Claro. El probador está al fondo a la derecha.",
      "Natuurlijk. Het paskamertje is achteraan rechts."),
     ("Nico", "Gracias. ¿Tiene una talla más grande?",
      "Dank u. Hebt u een grotere maat?"),
     ("Dependienta", "Sí, aquí tienes la grande.",
      "Ja, hier is de large.")]),
   ("Escena 3 · En la caja",
    "Aan de kassa: betalen en beslissen.",
    [("Nico", "Me la llevo. ¿Cuánto es todo?",
      "Ik neem ze. Hoeveel is het samen?"),
     ("Dependienta", "Treinta y cuatro euros. ¿En efectivo o con tarjeta?",
      "Vierendertig euro. Cash of met kaart?"),
     ("Nico", "Con tarjeta. Es un poco caro, pero me gusta mucho.",
      "Met kaart. Het is een beetje duur, maar ik vind het heel mooi."),
     ("Ana", "¿Me hace un descuento? ¡Somos estudiantes!",
      "Geeft u ons korting? We zijn studenten!"),
     ("Dependienta", "Lo siento, en rebajas no. ¡Pero ya es barato!",
      "Sorry, in de solden niet. Maar het is al goedkoop!")]),
  ],
 },
 12: {
  "titulo": "¡Qué frío hace!",
  "tema": "El tiempo y las estaciones",
  "intro": "Alba belt met Iván. Zij zit in de zon, hij in de sneeuw. Let op elke "
           "<b>weersuitdrukking</b> en op de <b>uitroepen</b> met ¡qué…!",
  "chunks": ["¿Qué tiempo hace", "hace sol", "hace calor", "hace frío", "está nublado",
             "llueve", "nieva", "hace viento", "¡Qué frío", "¡Qué calor", "¡Qué bien",
             "mi estación favorita", "en invierno", "en verano", "va a llover"],
  "escenas": [
   ("Escena 1 · Dos ciudades, dos tiempos",
    "Twee steden, twee soorten weer — tegelijk.",
    [("Alba", "¡Hola, Iván! ¿Qué tiempo hace en Bariloche?",
      "Hallo, Iván! Wat voor weer is het in Bariloche?"),
     ("Iván", "¡Qué frío hace! Nieva desde ayer. Dos grados.",
      "Wat koud! Het sneeuwt sinds gisteren. Twee graden."),
     ("Alba", "Aquí en Cartagena hace sol y calor: treinta y uno.",
      "Hier in Cartagena is het zonnig en warm: eenendertig."),
     ("Iván", "¡Qué calor! Aquí en invierno todo está blanco.",
      "Wat warm! Hier is in de winter alles wit."),
     ("Alba", "Y en verano, ¿hace buen tiempo?",
      "En in de zomer, is het dan mooi weer?"),
     ("Iván", "Sí, pero hace mucho viento en la montaña.",
      "Ja, maar het waait hard in de bergen.")]),
   ("Escena 2 · Los planes de hoy",
    "Het weer bepaalt de plannen.",
    [("Alba", "Hoy voy a la playa. ¿Y tú?",
      "Vandaag ga ik naar het strand. En jij?"),
     ("Iván", "Yo no salgo. Está nublado y creo que va a llover.",
      "Ik ga niet naar buiten. Het is bewolkt en ik denk dat het gaat regenen."),
     ("Alba", "¡Qué pena! ¿Y mañana?",
      "Wat jammer! En morgen?"),
     ("Iván", "Mañana hace mejor tiempo. Voy a esquiar.",
      "Morgen is het beter weer. Ik ga skiën."),
     ("Alba", "¡Qué bien! Yo no sé esquiar.",
      "Wat leuk! Ik kan niet skiën.")]),
   ("Escena 3 · ¿Cuál es tu estación favorita?",
    "Ieder zijn seizoen — en zijn reden.",
    [("Iván", "¿Cuál es tu estación favorita, Alba?",
      "Wat is jouw favoriete seizoen, Alba?"),
     ("Alba", "El verano, porque hace sol todos los días.",
      "De zomer, want dan is het elke dag zonnig."),
     ("Iván", "La mía es el otoño: no hace ni frío ni calor.",
      "De mijne is de herfst: dan is het noch koud noch warm."),
     ("Alba", "¿Y la primavera? Llueve mucho, pero es bonita.",
      "En de lente? Het regent veel, maar ze is mooi."),
     ("Iván", "Sí. Cuatro estaciones, cuatro tiempos.",
      "Ja. Vier seizoenen, vier soorten weer.")]),
  ],
 },
 13: {
  "titulo": "Una habitación, por favor",
  "tema": "En el hotel · viajar",
  "intro": "Ana en Nico komen aan in het hotel. Let op de <b>beleefde vormen</b> "
           "met <i>usted</i> en op alles wat je aan de receptie vraagt.",
  "chunks": ["Tengo una reserva", "a nombre de", "una habitación doble",
             "para dos noches", "¿El desayuno está incluido", "¿Hay wifi",
             "aquí tiene la llave", "en el tercer piso", "¿A qué hora es la salida",
             "¿Puede repetir", "el ascensor", "¿Dónde está"],
  "escenas": [
   ("Escena 1 · En la recepción",
    "Aankomen en inchecken.",
    [("Ana", "Buenas tardes. Tengo una reserva a nombre de Ana Ruiz.",
      "Goedemiddag. Ik heb een reservering op naam van Ana Ruiz."),
     ("Recepcionista", "Buenas tardes. Sí: una habitación doble para dos noches.",
      "Goedemiddag. Ja: een tweepersoonskamer voor twee nachten."),
     ("Ana", "Exacto. ¿El desayuno está incluido?",
      "Precies. Is het ontbijt inbegrepen?"),
     ("Recepcionista", "Sí, de siete a diez, en el primer piso.",
      "Ja, van zeven tot tien, op de eerste verdieping."),
     ("Nico", "Perdone, ¿puede repetir? ¿De siete a…?",
      "Sorry, kunt u dat herhalen? Van zeven tot…?"),
     ("Recepcionista", "De siete a diez. Aquí tienen la llave: habitación trescientos dos.",
      "Van zeven tot tien. Hier is uw sleutel: kamer driehonderd twee.")]),
   ("Escena 2 · ¿Dónde está todo?",
    "De weg vinden in het hotel.",
    [("Nico", "¿Dónde está la habitación?",
      "Waar is de kamer?"),
     ("Recepcionista", "En el tercer piso. Hay ascensor al fondo.",
      "Op de derde verdieping. Er is een lift achteraan."),
     ("Ana", "¿Y hay wifi en la habitación?",
      "En is er wifi op de kamer?"),
     ("Recepcionista", "Sí, gratis. La contraseña está en la puerta.",
      "Ja, gratis. Het wachtwoord staat op de deur."),
     ("Nico", "¿A qué hora es la salida?",
      "Hoe laat is het uitchecken?"),
     ("Recepcionista", "Antes de las doce del mediodía.",
      "Voor twaalf uur 's middags.")]),
   ("Escena 3 · Un pequeño problema",
    "Iets werkt niet — en dat moet je kunnen zeggen.",
    [("Ana", "Perdone, en la habitación no hay toallas.",
      "Excuseer, er zijn geen handdoeken op de kamer."),
     ("Recepcionista", "Lo siento mucho. Ahora mismo se las llevo.",
      "Het spijt me zeer. Ik breng ze meteen."),
     ("Nico", "Y el aire acondicionado no funciona.",
      "En de airco werkt niet."),
     ("Recepcionista", "¿No funciona? Voy a mirarlo esta tarde.",
      "Werkt hij niet? Ik kom er vanmiddag naar kijken."),
     ("Ana", "Muchas gracias. Muy amable.",
      "Hartelijk dank. Heel vriendelijk.")]),
  ],
 },
 14: {
  "titulo": "Mi mundo hispano",
  "tema": "Repaso · alles van het jaar",
  "intro": "De vier komen samen online. Alles van dit jaar keert terug: "
           "<b>voorstellen</b>, <b>familie</b>, <b>huis</b>, <b>uur</b>, "
           "<b>plannen</b>, <b>weer</b> en <b>reizen</b>.",
  "chunks": ["Me llamo", "soy de", "tengo dieciséis años", "vivo en",
             "mi familia", "a las ocho", "voy a", "tengo que", "sé nadar",
             "hace calor", "me gusta", "¿Y tú"],
  "escenas": [
   ("Escena 1 · ¿Quién eres?",
    "Voorstellen — zoals in unidad 1, maar nu vlot.",
    [("Ana", "Hola a todos. Me llamo Ana, soy de Sevilla y tengo dieciséis años.",
      "Hallo allemaal. Ik heet Ana, ik kom uit Sevilla en ik ben zestien."),
     ("Nico", "Yo soy Nico, soy mexicano. Vivo en una casa cerca del mercado.",
      "Ik ben Nico, ik ben Mexicaan. Ik woon in een huis dicht bij de markt."),
     ("Alba", "Me llamo Alba, soy colombiana. Mi familia es grande: somos seis.",
      "Ik heet Alba, ik ben Colombiaanse. Mijn familie is groot: we zijn met zes."),
     ("Iván", "Y yo soy Iván, argentino. Vivo en Bariloche, en la montaña.",
      "En ik ben Iván, Argentijn. Ik woon in Bariloche, in de bergen.")]),
   ("Escena 2 · Un día normal",
    "Uur, routine en plannen — alles samen.",
    [("Ana", "Me levanto a las siete y voy al insti a las ocho.",
      "Ik sta om zeven uur op en ga om acht uur naar school."),
     ("Nico", "Yo tengo que ayudar en casa: friego los platos.",
      "Ik moet thuis helpen: ik doe de vaat."),
     ("Alba", "Esta tarde voy a la playa. Sé nadar muy bien.",
      "Vanmiddag ga ik naar het strand. Ik kan heel goed zwemmen."),
     ("Iván", "Aquí no. ¡Hace frío y nieva! Tengo que llevar abrigo.",
      "Hier niet. Het is koud en het sneeuwt! Ik moet een jas dragen.")]),
   ("Escena 3 · ¿Y tú?",
    "De beurt is aan de leerling.",
    [("Ana", "Oye, ¿y tú? ¿Cómo te llamas?",
      "Zeg, en jij? Hoe heet jij?"),
     ("Nico", "¿De dónde eres y dónde vives?",
      "Waar kom je vandaan en waar woon je?"),
     ("Alba", "¿Qué tiempo hace hoy en tu ciudad?",
      "Wat voor weer is het vandaag in jouw stad?"),
     ("Iván", "¿Y qué vas a hacer este fin de semana?",
      "En wat ga je dit weekend doen?"),
     ("Ana", "¡Ahora te toca a ti! Cuéntanos.",
      "Nu is het jouw beurt! Vertel het ons.")]),
  ],
 },
}


def guion(unit):
    """Het volledige script als [(spreker, es)] — voor de TTS-generator."""
    e = ESCENAS.get(unit)
    if not e:
        return []
    return [(sp, es) for _t, _i, lineas in e["escenas"] for sp, es, _nl in lineas]


if __name__ == "__main__":
    for u in sorted(ESCENAS):
        e = ESCENAS[u]
        n = sum(len(x[2]) for x in e["escenas"])
        quien = sorted({sp for sp, _ in guion(u)})
        print("U%-3d %-26s %d escenas · %2d regels · %s"
              % (u, e["titulo"], len(e["escenas"]), n, ", ".join(quien)))
