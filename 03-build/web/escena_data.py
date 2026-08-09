#!/usr/bin/env python3
"""De scènes van U11–U14 — de échte afleveringen, woord voor woord.

WAAROM DIT BESTAAT
C4 is gebouwd op veertien videolessen: de video is de leidraad, het transcript
staat exact in de unit. U1–U10 hebben elk hun eigen generator; deze vier delen
er één, omdat ze in één keer gebouwd zijn. De inhoud staat hier, de vorm in
`gen_c4_escena.py`.

Deze vier scènes zijn een tijdlang eigen materiaal geweest, gebouwd op de
kernwoordenschat, omdat de transcripten er nog niet waren (`HANDOVER_C4.md`
voorziet die situatie uitdrukkelijk). Op 2026-08-09 leverde de auteur ze alle
vier, en zijn ze vervangen door wat er in de video's gezegd wórdt — inclusief
het thema, dat op twee plaatsen anders bleek dan de oorspronkelijke themalijst
voorzag.

DE SPREKERSLABELS
In de aangeleverde transcripten van aflevering 11 en 13 stonden regels op de
verkeerde naam. Bij 11 gaf de auteur het startsein om dat recht te zetten; bij
13 wees het bewijs in de tekst zelf (María die «no soy vegetariano» zegt) op
dezelfde soort verschuiving, en is ze op dezelfde manier hersteld. Wat er
hieronder staat is dus de gesproken tekst, met de beurten toegekend zoals ze
in beeld lopen. Klopt er iets niet met de video, dan is dit de enige plaats
waar het aangepast hoeft te worden: de oefeningen, de print en de PowerPoint
volgen mee.
"""

# ── de sitcom-afleveringen ──────────────────────────────────────────────────
# De video's staan in Google Drive, gedeeld als «iedereen met de link mag
# lezen» (nagekeken op 2026-08-09), en zijn ingebouwd met hetzelfde
# /preview-kader als U8–U10. De scène hieronder is de meelees-laag eronder.
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
     ("Camarero", "Pasas las fiestas de Navidad con los tuyos. Con tus padres, tus tíos, tus hermanos.",
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
  "titulo": "La ropa y los colores",
  "tema": "La ropa · los colores · describir a alguien",
  "intro": "Julio geeft les en neemt Paul als voorbeeld. Let op alles wat Paul "
           "<b>draagt</b> (<i>lleva…</i>), op de <b>kleuren</b>, en op de "
           "<b>wederkerende werkwoorden</b> (<i>se afeita, se ducha, se peina</i>).",
  "chunks": ["¿Te levantas, por favor?", "¿Cómo estás?", "¿Les gusta?",
             "¿Les parece guapo?", "tiene los ojos azules", "está fuerte",
             "lleva una chaqueta negra", "llevo un jersey verde", "lleva corbata",
             "le queda muy bien", "unos zapatos modernos", "unas zapatillas viejas",
             "¿se afeita?", "se ducha", "se peina", "os ducháis",
             "los verbos reflexivos", "en cambio"],
  "escenas": [
   ("Escena 1 · La clase de Julio",
    "Julio geeft les en roept Paul naar voren. Hij vergelijkt punt voor punt: "
    "Paul, en dan hijzelf.",
    [("Julio", "¿Te levantas, por favor? Y vienes aquí, por favor. ¿Cómo estás?",
      "Sta je even op, alsjeblieft? En kom je hier, alsjeblieft. Hoe gaat het?"),
     ("Paul", "Bien.",
      "Goed."),
     ("Julio", "¿No me preguntas cómo estoy yo?",
      "Vraag je mij niet hoe het met míj gaat?"),
     ("Paul", "¿Cómo estás, Julio?",
      "Hoe gaat het, Julio?"),
     ("Julio", "Estoy mal, pero gracias por preguntar. ¿Qué les parece Paul? ¿Les gusta? ¿Les parece guapo? Muy bien, es guapo, es verdad.",
      "Slecht, maar bedankt voor het vragen. Wat vinden jullie van Paul? Vinden jullie hem leuk? Vinden jullie hem knap? Heel goed, hij is knap, dat is waar."),
     ("Paul", "Gracias.",
      "Dank je."),
     ("Julio", "Paul es alto y yo no. Paul tiene los ojos azules, y yo no. Paul está fuerte. Y yo, en cambio, no estoy tan fuerte.",
      "Paul is groot en ik niet. Paul heeft blauwe ogen, en ik niet. Paul is gespierd. En ik daarentegen ben niet zo gespierd."),
     ("Julio", "Paul lleva una chaqueta negra, buena. Yo, en cambio, llevo un jersey verde, barato. Paul lleva corbata. Yo no tengo corbatas.",
      "Paul draagt een zwarte jas, een goede. Ik daarentegen draag een groene trui, een goedkope. Paul draagt een das. Ik heb geen dassen."),
     ("Julio", "A Paul la ropa le queda muy bien. A mí, en cambio, no me queda tan bien la ropa.",
      "Paul staat de kleding heel goed. Mij daarentegen staat kleding niet zo goed."),
     ("Julio", "Paul lleva unos zapatos modernos. Yo en cambio llevo unas zapatillas viejas y blancas. ¿Alguien sabe decirme alguna diferencia más entre Paul y yo?",
      "Paul draagt moderne schoenen. Ik daarentegen draag oude witte sportschoenen. Weet iemand mij nog een verschil te noemen tussen Paul en mij?"),
     ("Alumna", "¿Paul se afeita?",
      "Scheert Paul zich?"),
     ("Julio", "Exacto, muy bien. Los verbos reflexivos son acciones dirigidas a uno mismo. Yo, por ejemplo, me voy a matar.",
      "Precies, heel goed. Wederkerende werkwoorden zijn handelingen die op jezelf gericht zijn. Ik bijvoorbeeld ga mezelf van kant maken."),
     ("Julio", "La gente por las mañanas se ducha, se peina. Vosotros os ducháis, os peináis. Yo no, claro.",
      "'s Ochtends doucht men zich en kamt men zich. Jullie douchen je, kammen je. Ik niet, natuurlijk."),
     ("Julio", "Los pronombres de los verbos reflexivos y los pronombres del complemento indirecto son los mismos. Me gusta, me enamoro. Te gusta, te enamoras. Os gusta, os enamoráis.",
      "De voornaamwoorden van de wederkerende werkwoorden en die van het meewerkend voorwerp zijn dezelfde. Me gusta, me enamoro. Te gusta, te enamoras. Os gusta, os enamoráis."),
     ("Julio", "Menos en la tercera persona. No le gusta, no se enamora. Porque si no le gusta, ¿por qué se va enamorar? ¿Eh?",
      "Behalve in de derde persoon. No le gusta, no se enamora. Want als hij het niet leuk vindt, waarom zou hij dan verliefd worden? Hè?")]),
   ("Escena 2 · Por la ventana",
    "Josefina en María gluren door het raam van Julio's klas.",
    [("María", "¿Qué pasa?",
      "Wat is er?"),
     ("Josefina", "¡Shh…! ¡Ven, ven!",
      "Sst…! Kom, kom!"),
     ("Julio", "¡No!",
      "Nee!")]),
  ],
 },
 13: {
  "titulo": "En el mercado",
  "tema": "La comida · las tiendas · los precios",
  "intro": "Julio en María komen elkaar tegen op de markt. Zij doet de "
           "boodschappen, hij is met heel iets anders bezig. Let op de "
           "<b>etenswaren</b>, op de vraag naar de <b>prijs</b> "
           "(<i>¿cuánto cuesta?</i>) en op <b>¿por qué?</b>",
  "chunks": ["No tienes muy buen aspecto", "Estoy enfermo", "por eso",
             "Tienes que cuidarte", "buenísima", "una lata de atún",
             "es una oferta", "son baratas", "¿Son caras?",
             "¿Cuántas quieres, un kilo?", "¿Cuánto cuestan los tomates?",
             "dos con veinte el kilo", "te vas a llevar",
             "nos falta pasar por la carnicería", "¿Dónde venden pescado fresco?",
             "ahí hay una pescadería", "¿Por qué? No lo sé", "algo de verdura"],
  "escenas": [
   ("Escena 1 · Julio y María se encuentran en el mercado",
    "María inspecteert wat er in Julio's mandje ligt. Hij probeert het uit te "
    "leggen — en denkt intussen aan iets heel anders.",
    [("María", "¡Julio! ¿Cómo estás?",
      "Julio! Hoe gaat het?"),
     ("Julio", "Muy bien, muy bien, muy bien.",
      "Heel goed, heel goed, heel goed."),
     ("María", "No tienes muy buen aspecto.",
      "Je ziet er niet zo goed uit."),
     ("Julio", "Estoy enfermo. Estoy enfermo, por eso no voy a la academia.",
      "Ik ben ziek. Ik ben ziek, daarom ga ik niet naar de academie."),
     ("María", "Ya. Tienes que cuidarte.",
      "Juist. Je moet voor jezelf zorgen."),
     ("Julio", "Eso intento. Vitamina C, es muy buena, buenísima.",
      "Dat probeer ik. Vitamine C, dat is heel goed, ontzettend goed."),
     ("María", "Una cebolla.",
      "Een ui."),
     ("Julio", "Es… Intento seguir una dieta mediterránea, una dieta sana.",
      "Het is… Ik probeer een mediterraan dieet te volgen, een gezond dieet."),
     ("María", "Ya.",
      "Juist."),
     ("María", "Y una lata de atún.",
      "En een blikje tonijn."),
     ("Julio", "Es importante comer pescado. No soy vegetariano, no como mucha carne. Me gusta cuidarme.",
      "Het is belangrijk om vis te eten. Ik ben geen vegetariër, ik eet niet veel vlees. Ik zorg graag voor mezelf."),
     ("María", "Y seis tabletas de chocolate.",
      "En zes repen chocolade."),
     ("Julio", "Es una oferta, son baratas. Hay que saber dónde comprar.",
      "Dat is een aanbieding, ze zijn goedkoop. Je moet weten waar je moet kopen.")]),
   ("Escena 2 · La compra",
    "María stelt de boodschappenlijst samen. Julio hoort de helft niet.",
    [("María", "Te recomiendo las manzanas. Son baratas y son muy buenas. ¿Cuántas quieres, un kilo?",
      "Ik raad je de appels aan. Ze zijn goedkoop en heel lekker. Hoeveel wil je, een kilo?"),
     ("Julio", "Un kilo está bien. ¿Son caras?",
      "Een kilo is goed. Zijn ze duur?"),
     ("María", "No son caras, son baratas. Naranjas, plátanos, algo de verdura. Tienes que comer algo de verdura. ¿Cuánto cuestan los tomates?",
      "Ze zijn niet duur, ze zijn goedkoop. Sinaasappels, bananen, wat groenten. Je moet wat groenten eten. Hoeveel kosten de tomaten?"),
     ("Julio", "Dos con veinte el kilo.",
      "Twee twintig de kilo."),
     ("María", "Te vas a llevar un kilo de tomates y una lechuga.",
      "Je neemt een kilo tomaten en een krop sla mee."),
     ("Julio", "Te quiero.",
      "Ik hou van je."),
     ("María", "Nos falta pasar por la carnicería: pollo, ternera, carne picada…",
      "We moeten nog langs de slagerij: kip, kalfsvlees, gehakt…"),
     ("Julio", "Te quiero.",
      "Ik hou van je."),
     ("María", "¿Dónde venden pescado fresco?",
      "Waar verkopen ze verse vis?"),
     ("Julio", "Quiero pasar mi vida contigo. Es cursi, pero es la verdad. ¿Por qué? No lo sé. Para tener hijos, para discutir en IKEA. ¿Cuánto tiempo? Pues no lo sé. A lo mejor son diez minutos, pero van a ser los diez mejores minutos de mi vida. Quiero ser el abuelo de tus nietos.",
      "Ik wil mijn leven met jou doorbrengen. Het is kitsch, maar het is waar. Waarom? Ik weet het niet. Om kinderen te krijgen, om ruzie te maken in de IKEA. Hoe lang? Tja, dat weet ik niet. Misschien tien minuten, maar het worden de tien beste minuten van mijn leven. Ik wil de grootvader van jouw kleinkinderen zijn."),
     ("María", "Y huevos y leche. Y pan. El pan integral es el mejor.",
      "En eieren en melk. En brood. Volkorenbrood is het lekkerst."),
     ("Julio", "Te quiero.",
      "Ik hou van je."),
     ("María", "¿Dónde venden pescado fresco?",
      "Waar verkopen ze verse vis?"),
     ("Julio", "Ahí hay una pescadería.",
      "Daar is een viswinkel.")]),
  ],
 },
 14: {
  "titulo": "En el restaurante",
  "tema": "El restaurante · pedir · los gustos",
  "intro": "María gaat voor het eerst uit eten met de ouders van Julio. Let op "
           "wat ze <b>bestellen</b>, op <b>yo también / yo tampoco</b>, en op de "
           "woorden op <b>-ísimo</b> (<i>simpatiquísimos, buenísima</i>).",
  "chunks": ["Estoy nerviosa", "Tienes que estar tranquila", "simpatiquísimos",
             "Mesa para cuatro", "la mesa que nos gusta", "Encantada",
             "Encantado de conocerte", "Yo también", "Yo tampoco",
             "¿Quieren algo de beber?", "una botella de agua",
             "les recomiendo el cordero", "buenísima",
             "¿Van a tomar algo de postre?", "¡Qué rica!", "algo dulce",
             "café solo", "café con leche", "café cortado"],
  "escenas": [
   ("Escena 1 · Llegar al restaurante",
    "María ontmoet de ouders van Julio. De moeder neemt meteen de leiding.",
    [("María", "Estoy nerviosa, ¿no vamos muy rápido? Quiero decir… llevamos juntos tres meses, no es tanto tiempo…",
      "Ik ben zenuwachtig. Gaan we niet te snel? Ik bedoel… we zijn drie maanden samen, dat is niet zo lang…"),
     ("Julio", "Tienes que estar tranquila. Mis padres son muy simpáticos, simpatiquísimos.",
      "Je moet rustig blijven. Mijn ouders zijn heel aardig, ontzettend aardig."),
     ("Madre", "Chica… Bonita… Mesa para cuatro. Esa, si puede ser.",
      "Meisje… Schat… Een tafel voor vier. Die daar, als het kan."),
     ("María", "¿Qué?",
      "Wat?"),
     ("Madre", "Ésa es la mesa que nos gusta. Vamos a cenar cuatro personas. Somos cuatro personas que van a cenar.",
      "Dát is de tafel die we graag hebben. We komen met vier personen eten. We zijn met vier personen die gaan eten."),
     ("Julio", "Mamá. María, estos son mis padres. Mamá, papá…, ella es María.",
      "Mama. María, dit zijn mijn ouders. Mama, papa…, dit is María."),
     ("María", "Encantada.",
      "Aangenaam."),
     ("Padre", "Encantado de conocerte.",
      "Aangenaam kennis te maken."),
     ("Julio", "¿Mamá?",
      "Mama?"),
     ("Madre", "Sí, claro… Yo también estoy encantada.",
      "Ja, natuurlijk… Ik ben ook verheugd.")]),
   ("Escena 2 · La comida",
    "Bestellen: eerst iets te drinken, dan het eten.",
    [("Camarero", "¿Quieren algo de beber mientras miran el menú?",
      "Wilt u iets drinken terwijl u de kaart bekijkt?"),
     ("María", "¿Queréis vino? Aquí hay un Rioja estupendo y no es muy caro.",
      "Willen jullie wijn? Ze hebben hier een prima Rioja en die is niet duur."),
     ("Madre", "Yo quiero agua.",
      "Ik wil water."),
     ("Padre", "Yo tampoco quiero vino, tengo el estómago… Agua también.",
      "Ik wil ook geen wijn, mijn maag… Ook water."),
     ("Madre", "Pero tú puedes pedir vino, si quieres.",
      "Maar jij mag wijn bestellen, als je wil."),
     ("María", "No quizás… Mejor, una botella de agua.",
      "Nee, misschien niet… Doe maar een fles water."),
     ("Camarero", "¿Agua para cuatro?",
      "Water voor vier?"),
     ("Julio", "No, yo quiero una cerveza.",
      "Nee, ik wil een biertje."),
     ("María", "Dos cervezas.",
      "Twee biertjes."),
     ("Madre", "¿Qué sabes de Sandra?",
      "Wat weet je van Sandra?"),
     ("Julio", "Nada.",
      "Niets."),
     ("Madre", "Su primera novia. Una chica muy lista y muy guapa. Guapísima. Tú también eres guapísima.",
      "Zijn eerste vriendin. Een heel slim en heel knap meisje. Beeldschoon. Jij bent ook beeldschoon."),
     ("Camarero", "De carne les recomiendo el cordero. De pescado, la merluza. Además de lo que hay en el menú, tenemos también sopa, buenísima. Paella, excelente, y calamares buenísimos.",
      "Van het vlees raad ik u het lam aan. Van de vis de heek. Naast wat op de kaart staat hebben we ook soep, ontzettend lekker. Paella, uitstekend, en inktvisringen, heel lekker.")]),
   ("Escena 3 · El postre",
    "Het nagerecht — en wie wat kiest.",
    [("Camarero", "¿Van a tomar algo de postre?",
      "Neemt u nog een nagerecht?"),
     ("Madre", "Uff… Yo no, gracias.",
      "Oef… Ik niet, dank u."),
     ("María", "¿Quieres algo para compartir? ¿Una fruta?",
      "Wil je iets om te delen? Een stuk fruit?"),
     ("Julio", "Yo prefiero algo dulce.",
      "Ik heb liever iets zoets."),
     ("Camarero", "Tenemos flan y tarta de chocolate casera.",
      "We hebben flan en zelfgemaakte chocoladetaart."),
     ("María", "Tarta de chocolate, ¡qué rica!",
      "Chocoladetaart, wat lekker!"),
     ("Julio", "Muy bien, una tarta de chocolate.",
      "Heel goed, één chocoladetaart.")]),
   ("Escena 4 · El café",
    "Drie soorten koffie — en de moeder begint opnieuw over Sandra.",
    [("Camarero", "¿Café cortado?",
      "Koffie met een wolkje melk?"),
     ("Padre", "Sí, aquí.",
      "Ja, hier."),
     ("Camarero", "¿Café solo?",
      "Zwarte koffie?"),
     ("Julio", "Yo, aquí. Gracias.",
      "Voor mij, hier. Dank u."),
     ("Camarero", "¿Café con leche?",
      "Koffie met melk?"),
     ("Madre", "Sandra es muy divertida. Sandra es la chica que siempre anima una reunión.",
      "Sandra is heel grappig. Sandra is het meisje dat elk samenzijn opvrolijkt.")]),
   ("Escena 5 · En la calle",
    "Buiten. Julio kijkt terug op de avond — en trekt een verrassende conclusie.",
    [("Julio", "¡Qué tensión, qué desagradable!",
      "Wat een spanning, wat onaangenaam!"),
     ("María", "Sí.",
      "Ja."),
     ("Julio", "No puedes tratar así a mi madre, es una señora muy sensible. ¿Te cuesta mucho ser amable?",
      "Je kan mijn moeder zo niet behandelen, ze is een heel gevoelige vrouw. Kost het je zoveel moeite om vriendelijk te zijn?")]),
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
