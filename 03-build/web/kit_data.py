#!/usr/bin/env python3
"""De inhoud van de «Kit»-tab van U11–U14 — woordenschat, gramática, uitspraak.

WAAROM ALS DATA EN NIET ALS VIER GENERATOREN
U1 tot U10 hebben elk een eigen `gen_c4uN_kgt.py` van ongeveer driehonderd
regels, waarvan het grootste deel CSS en JavaScript is die in alle tien
identiek is. Vier keer datzelfde kopiëren zou vier plaatsen opleveren waar een
verbetering apart doorgevoerd moet worden. De inhoud staat hier, de vorm in
`gen_c4_kit.py`.

DE UITSPRAAKLAAG
Volgt matrix A uit `01-cursussen/04-welcome/reservoir/C4_coverage.md`, die per
unit één klankfocus en één acentuación-laag vastlegt, met telkens een ándere
werkvorm. Voor deze vier:

  U11  klank **s** (altijd stemloos, nooit /z/)   · klemtoon in prijzen en getallen
  U12  **entonación** (¡qué frío!)                · de tekens ¡! ¿? en de melodie
  U13  **enlace** (woorden aaneen: en_el_hotel)   · vraagintonatie
  U14  álle klanken door elkaar (transfer)        · tilde-regels samengevat
"""

# ── woordenschat, in clusters ───────────────────────────────────────────────
# (naam, ondertitel-NL, icoon, [(es, nl)])
CLUSTERS = {
 # ── U11 · gebouwd op aflevering 11 «Aquí hace demasiado calor» ────────────
 # De themalijst plande hier «De compras / la ropa», maar de aflevering gaat
 # over het weer, de vakantie en wat je graag doet. In C4 is de vídeo de
 # leidraad (CLAUDE.md), dus de unit volgt de aflevering — net zoals bij U10.
 # Het kleding-/winkelmateriaal staat onderaan dit bestand geparkeerd.
 11: [
  ("¿Qué tiempo hace?", "het weer", "🌤️", [
    ("hace buen tiempo", "het is mooi weer"), ("hace calor", "het is warm"),
    ("hace frío", "het is koud"), ("hace viento", "het waait"),
    ("hace sol", "het is zonnig"), ("llueve", "het regent"),
    ("nieva", "het sneeuwt"), ("hay niebla", "het is mistig")]),
  ("Las estaciones", "de seizoenen", "🍂", [
    ("la primavera", "de lente"), ("el verano", "de zomer"),
    ("el otoño", "de herfst"), ("el invierno", "de winter"),
    ("en verano · en invierno", "in de zomer · in de winter")]),
  ("¿Cómo vas?", "vervoer", "🚆", [
    ("en tren", "met de trein"), ("en avión", "met het vliegtuig"),
    ("en barco · en ferry", "met de boot · met de veerboot"),
    ("en coche", "met de auto"), ("en bici", "met de fiets"),
    ("en moto", "met de motor")]),
  ("¿Adónde vas?", "bestemmingen", "🏝️", [
    ("a la playa", "naar het strand"), ("a la montaña", "naar de bergen"),
    ("al mar", "naar de zee"), ("a una isla", "naar een eiland"),
    ("a la ciudad", "naar de stad"), ("al pueblo", "naar het dorp")]),
  ("¿Con qué frecuencia?", "hoe vaak", "🔁", [
    ("siempre", "altijd"), ("a menudo", "vaak"),
    ("a veces", "soms"), ("casi nunca", "bijna nooit"),
    ("nunca", "nooit"), ("todos los años", "elk jaar"),
    ("tres veces por semana", "drie keer per week")]),
  ("Tengo frío", "hoe jij je voelt", "🥶", [
    ("tengo frío", "ik heb het koud"), ("tengo calor", "ik heb het warm"),
    ("tengo sueño", "ik ben slaperig"), ("tengo hambre", "ik heb honger"),
    ("estoy cansado/a", "ik ben moe")]),
 ],
 12: [
  ("¿Qué tiempo hace?", "het weer", "🌤️", [
    ("hace sol", "het is zonnig"), ("hace calor", "het is warm"),
    ("hace frío", "het is koud"), ("hace viento", "het waait"),
    ("está nublado", "het is bewolkt"), ("llueve", "het regent"),
    ("nieva", "het sneeuwt"), ("hace buen/mal tiempo", "het is mooi/slecht weer")]),
  ("Las estaciones", "de seizoenen", "🍂", [
    ("la primavera", "de lente"), ("el verano", "de zomer"),
    ("el otoño", "de herfst"), ("el invierno", "de winter"),
    ("mi estación favorita", "mijn favoriete seizoen")]),
  ("¡Qué…!", "reageren", "❗", [
    ("¡Qué frío!", "Wat koud!"), ("¡Qué calor!", "Wat warm!"),
    ("¡Qué bien!", "Wat goed!"), ("¡Qué pena!", "Wat jammer!"),
    ("¡Qué bonito!", "Wat mooi!")]),
  ("Los grados", "temperatuur", "🌡️", [
    ("treinta grados", "dertig graden"), ("dos grados bajo cero", "twee graden onder nul"),
    ("ni frío ni calor", "noch koud noch warm"),
    ("va a llover", "het gaat regenen")]),
 ],
 13: [
  ("En el hotel", "in het hotel", "🏨", [
    ("la reserva", "de reservering"), ("la habitación doble", "de tweepersoonskamer"),
    ("la habitación individual", "de eenpersoonskamer"),
    ("la llave", "de sleutel"), ("la recepción", "de receptie"),
    ("el ascensor", "de lift"), ("las toallas", "de handdoeken")]),
  ("Reservar", "reserveren", "📅", [
    ("Tengo una reserva a nombre de…", "Ik heb een reservering op naam van…"),
    ("para dos noches", "voor twee nachten"),
    ("¿El desayuno está incluido?", "Is het ontbijt inbegrepen?"),
    ("¿Hay wifi?", "Is er wifi?"), ("gratis", "gratis")]),
  ("Preguntar con cortesía", "beleefd vragen", "🙏", [
    ("¿Puede repetir, por favor?", "Kunt u dat herhalen, alstublieft?"),
    ("Perdone…", "Excuseer…"), ("Muy amable", "Heel vriendelijk"),
    ("Lo siento", "Het spijt me"),
    ("¿A qué hora es la salida?", "Hoe laat is het uitchecken?")]),
  ("Un problema", "iets werkt niet", "🔧", [
    ("no funciona", "het werkt niet"), ("no hay toallas", "er zijn geen handdoeken"),
    ("¿Puede mirarlo?", "Kunt u ernaar kijken?"),
    ("ahora mismo", "meteen")]),
 ],
 14: [
  ("Yo, otra vez", "jezelf voorstellen", "🙋", [
    ("Me llamo…", "Ik heet…"), ("Soy de…", "Ik kom uit…"),
    ("Tengo … años", "Ik ben … jaar"), ("Vivo en…", "Ik woon in…"),
    ("Mi familia es…", "Mijn familie is…")]),
  ("Mi día", "mijn dag", "🕗", [
    ("me levanto a las…", "ik sta op om…"), ("voy al insti", "ik ga naar school"),
    ("tengo que…", "ik moet…"), ("voy a…", "ik ga…"),
    ("sé…", "ik kan…")]),
  ("Mi mundo", "mijn wereld", "🌍", [
    ("hace calor/frío", "het is warm/koud"), ("cerca de", "dicht bij"),
    ("me gusta", "ik vind leuk"), ("porque", "want/omdat"),
    ("¿Y tú?", "En jij?")]),
  ("Seguir hablando", "het gesprek gaande houden", "💬", [
    ("¿Puedes repetir?", "Kan je dat herhalen?"),
    ("No entiendo", "Ik begrijp het niet"),
    ("¿Cómo se dice…?", "Hoe zeg je…?"),
    ("¡Ahora te toca a ti!", "Nu is het jouw beurt!")]),
 ],
}

# ── gramática: één kernpunt per unit, visueel ───────────────────────────────
# (titel, ondertitel-NL, [(vorm, uitleg-ES, uitleg-NL)], valstrik)
GRAMATICA = {
 11: ("Me gusta · te gusta · le gusta",
      "zeggen wat je graag doet — en hoe graag",
      [("<b>A mí me</b> gusta el cine", "yo", "ík vind film leuk"),
       ("<b>A ti te</b> gusta el yoga", "tú", "jíj vindt yoga leuk"),
       ("<b>A él/ella le</b> gusta el submarinismo", "él · ella", "hij/zij duikt graag"),
       ("Me <b>encanta</b> la playa", "más fuerte", "ik vind het strand geweldig"),
       ("<b>No soporto</b> el frío", "lo contrario", "ik kan niet tegen de kou"),
       ("<b>Prefiero</b> el verano", "elegir", "ik verkies de zomer")],
      "Twee dingen tegelijk. Eén: het is <b>me gusta</b>, niet «yo gusto» — "
      "het Spaans zegt letterlijk «het bevalt mij». Twee: <b>hace frío</b> gaat "
      "over het wéér, <b>tengo frío</b> over jóú. «Estoy frío» bestaat niet."),
 12: ("Hace · está · llueve",
      "drie manieren om het weer te zeggen",
      [("<b>hace</b> sol / calor / frío / viento", "con un sustantivo",
        "met een zelfstandig naamwoord — «hace» is vast"),
       ("<b>está</b> nublado", "con un adjetivo", "met een bijvoeglijk naamwoord"),
       ("<b>llueve</b> · <b>nieva</b>", "un verbo solo", "één werkwoord, zonder onderwerp")],
      "«Hace frío» is niet «het maakt koud». Het is één vaste uitdrukking — "
      "leer ze als geheel, net als «het is koud» in het Nederlands."),
 13: ("Usted",
      "de beleefde vorm: praten mét iemand die u bent",
      [("¿<b>Puede</b> repetir?", "usted → 3ª persona", "u kunt → dezelfde vorm als hij/zij"),
       ("¿<b>Tiene</b> una habitación?", "usted", "hebt u"),
       ("¿<b>Puedes</b> repetir?", "tú", "kan jij (tegen een vriend)"),
       ("Aquí <b>tiene</b> la llave", "usted", "hier hebt u de sleutel")],
      "Usted gebruikt de híj/zij-vorm, niet de jij-vorm. Dat voelt vreemd, maar "
      "het is precies wat het beleefd maakt."),
 14: ("Todo junto",
      "alles van het jaar in één zin",
      [("<b>Me llamo</b> Ana y <b>soy</b> de Sevilla", "presentarse", "voorstellen"),
       ("<b>Vivo</b> en una casa <b>cerca del</b> mercado", "describir", "beschrijven"),
       ("<b>Tengo que</b> estudiar, pero <b>voy a</b> salir", "obligación + plan",
        "moeten + van plan zijn"),
       ("<b>Hace</b> calor, así que <b>me gusta</b> el verano", "tiempo + gusto",
        "weer + voorkeur")],
      "Let op de twee valstrikken van het hele jaar: «want» én «omdat» zijn allebei "
      "<b>porque</b>, en «dus» is <b>así que</b>, nooit «luego»."),
}

# ── Suena bien: klankfocus + acentuación (matrix A) ─────────────────────────
# (klanktitel, uitleg, [woorden om te horen], (acentuación-titel, uitleg, [(woord, gesplitst)]))
SUENA = {
 11: ("La <b>s</b> española — siempre sorda",
      "De Spaanse <b>s</b> is áltijd stemloos, zoals in het Nederlandse «sok». "
      "Nooit als de <b>z</b> in «zon» — ook niet tussen twee klinkers. Deze unidad "
      "zit er vol mee: <i>siempre</i>, <i>vacaciones</i>, <i>estaciones</i>.",
      ["siempre", "vacaciones", "las estaciones", "submarinismo",
       "casi nunca", "tres veces"],
      ("El acento en las estaciones y la frecuencia",
       "De klemtoon ligt vast. Klap mee terwijl je het zegt.",
       [("primavera", "pri·ma·VE·ra"), ("verano", "ve·RA·no"),
        ("otoño", "o·TO·ño"), ("invierno", "in·VIER·no"),
        ("siempre", "SIEM·pre"), ("a menudo", "a me·NU·do")])),
 12: ("La entonación — la música de la frase",
      "Spaans laat je hóren wat voor zin het is. Een uitroep gaat omhoog en "
      "dan kort omlaag; een mededeling zakt gewoon.",
      ["¡Qué frío!", "¡Qué calor!", "Hace frío.", "¡Qué bonito!", "Está nublado."],
      ("¡ … ! y ¿ … ?",
       "Het teken staat er twee keer: aan het begin ondersteboven, aan het eind gewoon. "
       "Zo weet je vóór het lezen al hoe de zin klinkt.",
       [("¡Qué frío hace!", "¡ … !"), ("¿Qué tiempo hace?", "¿ … ?"),
        ("Hace frío.", "geen teken")])),
 13: ("El enlace — las palabras se dan la mano",
      "Spanjaarden plakken woorden aaneen: het einde van het ene woord en het begin "
      "van het volgende worden één klank. Daarom klinkt het zo snel.",
      ["en_el_hotel", "una_habitación", "el_ascensor", "está_incluido", "los_otros"],
      ("La pregunta sube",
       "Een ja-neevraag gaat aan het eind omhoog; een vraag met een vraagwoord "
       "(¿dónde? ¿cuánto?) gaat juist omlaag.",
       [("¿Hay wifi?", "omhoog ↗"), ("¿Está incluido?", "omhoog ↗"),
        ("¿Dónde está la habitación?", "omlaag ↘")])),
 14: ("Todos los sonidos",
      "Alle klanken van dit jaar door elkaar: ñ · c/z · g/gu · j · ll/y · r/rr · s.",
      ["España", "cinco", "guitarra", "jugar", "llueve", "perro", "camiseta"],
      ("Aguda · llana · esdrújula",
       "Drie soorten woorden, en de tilde volgt daaruit. Klap de klemtoon, dan zie je het.",
       [("hotel", "a·GU·da (laatste)"), ("camiseta", "LLA·na (voorlaatste)"),
        ("teléfono", "es·DRÚ·ju·la (altijd tilde)"), ("está", "aguda mét tilde"),
        ("fácil", "llana mét tilde")])),
}

# ── de eindtaak van de unit ────────────────────────────────────────────────
# (titel, situatie-ES, situatie-NL, [pasos])
TAREA = {
 11: ("El tiempo y mis vacaciones",
      "Cuenta qué tiempo hace, adónde vas y qué te gusta hacer.",
      "Vertel wat voor weer het is, waar je heen gaat en wat je graag doet.",
      ["Zeg wat voor weer het vandaag is: <b>hace…</b> of <b>está…</b>",
       "Kies een bestemming en zeg hoe je er geraakt: <b>voy a… en…</b>",
       "Zeg wat je daar graag doet met <b>me gusta</b> of <b>me encanta</b>.",
       "Voeg één woord toe dat zegt hóé vaak: <b>siempre · a veces · nunca</b>.",
       "Vraag het je buur: «¿Y a ti? ¿Qué te gusta hacer en vacaciones?»"]),
 12: ("El parte del tiempo de mi ciudad",
      "Eres el hombre o la mujer del tiempo. Presenta el tiempo de hoy.",
      "Jij bent de weerman of weervrouw. Presenteer het weer van vandaag.",
      ["Teken of print een kaartje van je streek.",
       "Noteer per plaats: <b>hace…</b> / <b>está…</b> / <b>llueve</b> + graden.",
       "Voeg één uitroep toe: «¡Qué frío!» of «¡Qué calor!»",
       "Zeg welk seizoen je favoriet is, mét <b>porque</b>.",
       "Presenteer staand, in dertig seconden."]),
 13: ("Reservo mi habitación",
      "Llegas a un hotel en Salamanca. Habla con la recepción.",
      "Je komt aan in een hotel in Salamanca. Praat met de receptie.",
      ["Schrijf je reservering: naam, soort kamer, aantal nachten.",
       "Bereid drie vragen voor met <b>usted</b>.",
       "Speel de scène: één van jullie is de receptionist.",
       "Verwerk één probleem («no funciona…») en los het beleefd op.",
       "Noteer achteraf: kamernummer, verdieping, ontbijturen."]),
 14: ("Mi mundo hispano",
      "Un minuto sobre ti, en español, delante de la clase.",
      "Eén minuut over jezelf, in het Spaans, voor de klas.",
      ["Stel jezelf voor: naam, leeftijd, waar je woont.",
       "Vertel iets over je familie of je huis.",
       "Beschrijf één gewone dag, met een uur erin.",
       "Zeg wat voor weer het vandaag is en welk seizoen je liefst hebt.",
       "Eindig met een vraag aan de klas: «¿Y tú?»"]),
}


if __name__ == "__main__":
    for u in sorted(CLUSTERS):
        n = sum(len(c[3]) for c in CLUSTERS[u])
        print("U%-3d %2d chunks in %d clusters · gramática: %-28s · tarea: %s"
              % (u, n, len(CLUSTERS[u]), GRAMATICA[u][0], TAREA[u][0]))


# ── de opener van de gedrukte unit ─────────────────────────────────────────
# (parada-nr, titel, ondertitel-NL, ondertitel-ES, citaat uit de scène,
#  [can-do's: (es, nl)], gids-tekst, [transparante woorden])
PORTADA = {
 11: (11, "Aquí hace demasiado calor",
      "Praten over het weer, over vakantie, en over wat je graag doet.",
      "el tiempo · las estaciones · me gusta · siempre y nunca",
      "Siempre hace buen tiempo en Canarias. — Pero hace un frío…",
      [("Decir <b>qué tiempo hace</b>", "hace sol · hace frío · llueve · hay niebla"),
       ("Hablar de <b>vacaciones</b>", "voy a la playa en avión · al pueblo en coche"),
       ("Decir lo que <b>te gusta</b>", "me gusta · me encanta · no soporto · prefiero"),
       ("Decir <b>con qué frecuencia</b>", "siempre · a menudo · a veces · casi nunca")],
      "Julio zit in een bar en hoort dat iedereen ergens anders heen gaat: zij naar "
      "de Canarische Eilanden, hij naar het dorp van zijn ouders in Ávila, waar het "
      "ijskoud is. Alles wat ze zeggen heb je zelf nodig zodra iemand vraagt waar "
      "jij naartoe gaat — en wat voor weer het daar is.",
      ["las vacaciones", "el clima", "la temperatura", "el hotel", "el restaurante",
       "flexible", "el gimnasio", "la ópera"]),
 12: (12, "El tiempo", "Zeggen wat voor weer het is — en erop reageren.",
      "hace sol · está nublado · llueve · las estaciones",
      "¡Qué frío hace! Nieva desde ayer. — Aquí hace sol y calor.",
      [("Decir <b>qué tiempo hace</b>", "hace sol · hace frío · está nublado · llueve"),
       ("Nombrar las <b>estaciones</b>", "primavera · verano · otoño · invierno"),
       ("Reaccionar con <b>¡Qué…!</b>", "¡Qué frío! · ¡Qué bonito!"),
       ("Decir tu <b>preferencia</b> con porque", "mi estación favorita es… porque…")],
      "Alba zit in de zon in Cartagena, Iván in de sneeuw in Bariloche — op hetzelfde "
      "moment. De Spaanstalige wereld ligt op beide halfronden, dus «zomer» betekent "
      "er niet overal hetzelfde.",
      ["el clima", "la temperatura", "los grados", "la estación", "el sol",
       "el viento", "la primavera", "el invierno"]),
 13: (13, "En el hotel", "Aankomen, vragen en oplossen — beleefd, met usted.",
      "la reserva · la habitación · ¿está incluido? · usted",
      "Tengo una reserva a nombre de Ana Ruiz. — ¿El desayuno está incluido?",
      [("Hacer y confirmar una <b>reserva</b>", "tengo una reserva · para dos noches"),
       ("Preguntar por los <b>servicios</b>", "¿el desayuno está incluido? · ¿hay wifi?"),
       ("Usar la forma de cortesía <b>usted</b>", "¿puede repetir? · aquí tiene"),
       ("Decir que algo <b>no funciona</b>", "no hay toallas · no funciona")],
      "Ana en Nico komen aan in een hotel. Dit is de eerste unidad waarin je met "
      "een volwassen vreemde praat, en dan gaat het Spaans over op <i>usted</i> — "
      "een andere werkwoordsvorm, niet alleen een ander woord.",
      ["la reserva", "el hotel", "la recepción", "el ascensor", "incluido",
       "el problema", "individual", "el wifi"]),
 14: (14, "Mi mundo hispano", "Alles van dit jaar, in één minuut over jezelf.",
      "repaso · presentarse · describir · contar",
      "Me llamo Ana, soy de Sevilla y tengo dieciséis años. ¿Y tú?",
      [("<b>Presentarte</b> con soltura", "nombre · edad · país · dónde vives"),
       ("<b>Describir</b> tu casa, tu familia y tu día", "hay · está · me levanto a las…"),
       ("Hablar de <b>planes</b> y <b>obligaciones</b>", "voy a… · tengo que…"),
       ("Contar el <b>tiempo</b> y tus <b>gustos</b>", "hace calor · me gusta… porque…")],
      "De laatste parada. Alles wat je dit jaar verzameld hebt komt hier samen in één "
      "taak: één minuut over jezelf, in het Spaans, zonder blad. Je zult merken hoeveel "
      "je al kunt zeggen.",
      ["la presentación", "la familia", "la casa", "el mundo hispano",
       "favorito", "el momento", "la persona", "el país"]),
}
