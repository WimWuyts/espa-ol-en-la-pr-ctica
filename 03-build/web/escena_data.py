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
  "titulo": "Aquí hace demasiado calor",
  "tema": "El tiempo · las vacaciones · lo que me gusta",
  "intro": "Julio zit in een bar en praat over vakantie. Let op elke "
           "<b>weersuitdrukking</b>, op <b>me gusta / le gusta</b> en op de woorden "
           "die zeggen <b>hoe vaak</b> iets gebeurt.",
  "chunks": ["se va de vacaciones", "hace buen tiempo", "hace un frío",
             "nunca hace ese frío", "me gusta hacer submarinismo", "le gusta",
             "a veces", "casi nunca", "todos los años", "tres veces por semana",
             "voy mucho al cine", "hace mucho viento", "hace calor", "en invierno",
             "en verano", "¡Qué bien!"],
  "escenas": [
   ("Escena 1 · En el bar",
    "Julio gaat naar het dorp van zijn ouders, de ober naar de Caraïben. "
    "Een klant luistert mee.",
    [("Julio", "Ella se va de vacaciones a la playa, a Canarias. Siempre hace buen tiempo en Canarias. Viaja con unos amigos; con un amigo, un inglés.",
      "Zij gaat op vakantie naar het strand, naar de Canarische Eilanden. Daar is het altijd mooi weer. Ze reist met wat vrienden; met een vriend, een Engelsman."),
     ("Camarero", "Son cuatro cincuenta.",
      "Dat is vier vijftig."),
     ("Julio", "Yo no, yo voy al pueblo de mis padres, Cabezas de Bonilla, en Ávila. Está cerca de Madrid.",
      "Ik niet, ik ga naar het dorp van mijn ouders, Cabezas de Bonilla, in Ávila. Dat ligt dicht bij Madrid."),
     ("Camarero", "Es bonito Ávila.",
      "Ávila is mooi."),
     ("Julio", "Pero hace un frío… Nunca hace ese frío en Madrid.",
      "Maar wat is het daar koud… Zo koud is het nooit in Madrid."),
     ("Camarero", "Lo bueno es que, por lo menos, puedes estar con tu familia.",
      "Het goede is dat je tenminste bij je familie kan zijn."),
     ("Julio", "Pasas las fiestas de Navidad con los tuyos. Con tus padres, tus tíos, tus hermanos.",
      "Je brengt de kerstdagen door met de jouwen. Met je ouders, je ooms en tantes, je broers en zussen."),
     ("Camarero", "Tus cuñados.",
      "Je schoonbroers en schoonzussen."),
     ("Julio", "Exacto. A veces te cansas de restaurantes y playas y hoteles. Amigos, amantes, copas, vino, fiesta. En cambio la familia…",
      "Precies. Soms word je moe van restaurants en stranden en hotels. Vrienden, geliefden, drankjes, wijn, feest. De familie daarentegen…"),
     ("Camarero", "¿Qué?",
      "Wat?"),
     ("Julio", "No, digo que la familia es para siempre.",
      "Nee, ik zeg dat familie voor altijd is."),
     ("Julio", "Ya. ¿Y tú te quedas en Madrid?",
      "Juist. En jij, blijf jij in Madrid?"),
     ("Camarero", "Yo voy todos los años al Caribe.",
      "Ik ga elk jaar naar de Caraïben."),
     ("Julio", "¿Y la familia?",
      "En de familie?"),
     ("Camarero", "Es que me gusta hacer submarinismo.",
      "Het is gewoon dat ik graag ga duiken."),
     ("Julio", "Ya. A ella también le gusta hacer submarinismo.",
      "Juist. Zij duikt ook graag."),
     ("Camarero", "¿Por qué no lo intentas?",
      "Waarom probeer je het niet?"),
     ("Julio", "Bueno, es que en Ávila es difícil, ¿sabes? Yo voy mucho al cine.",
      "Tja, in Ávila is dat moeilijk, weet je. Ik ga veel naar de film."),
     ("Clienta", "Me gusta el cine y me gusta la ópera.",
      "Ik hou van film en ik hou van opera."),
     ("Julio", "Casi nunca voy a la ópera.",
      "Ik ga bijna nooit naar de opera."),
     ("Clienta", "Y los deportes. Voy al gimnasio tres veces por semana. Hago yoga.",
      "En sport. Ik ga drie keer per week naar de sportschool. Ik doe yoga."),
     ("Julio", "¡Qué bien!",
      "Wat goed!"),
     ("Clienta", "¿Te gusta el yoga? Mira, mira lo que hago con la pierna. Soy muy flexible.",
      "Hou jij van yoga? Kijk, kijk wat ik met mijn been kan. Ik ben heel lenig."),
     ("Julio", "Ya veo, ya.",
      "Dat zie ik, ja.")]),
   ("Escena 2 · En la calle",
    "Julio en de klant komen buiten. Het weer beslist mee.",
    [("Clienta", "¡Uh, hace mucho viento!",
      "Oe, wat waait het hard!"),
     ("Julio", "Sí.",
      "Ja."),
     ("Clienta", "En invierno hace frío.",
      "In de winter is het koud."),
     ("Julio", "Y viento.",
      "En winderig."),
     ("Clienta", "Sí. En verano, en cambio, hace calor.",
      "Ja. In de zomer daarentegen is het warm."),
     ("Julio", "A mí me gusta más el frío.",
      "Ik hou meer van de kou."),
     ("Clienta", "¿Sí?",
      "Echt?"),
     ("Julio", "Sí.",
      "Ja."),
     ("Clienta", "En mi casa hace calor y tengo una botella de vino.",
      "Bij mij thuis is het warm en ik heb een fles wijn.")]),
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
