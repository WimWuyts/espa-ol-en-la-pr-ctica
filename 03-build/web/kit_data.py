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

  U11  klank **s** (altijd stemloos, nooit /z/)   · klemtoon in de seizoenen
  U12  **entonación** (vraag · uitroep · zin)     · de tekens ¡! ¿? en de melodie
  U13  **enlace** (woorden aaneen: en_el_mercado) · vraagintonatie
  U14  álle klanken door elkaar (transfer)        · tilde-regels samengevat

De klankfocus per unit ligt vast in matrix A en is dus níet mee veranderd toen
de thema's van U12–U14 op de echte afleveringen werden gezet; alleen de
voorbeeldwoorden komen nu uit de nieuwe scène. Zo blijft elke klank precies één
keer aan de beurt over de veertien units.
"""

# ── woordenschat, in clusters ───────────────────────────────────────────────
# (naam, ondertitel-NL, icoon, [(es, nl)])
CLUSTERS = {
 # ── U11 · gebouwd op aflevering 11 «Aquí hace demasiado calor» ────────────
 # De themalijst plande hier «De compras / la ropa», maar de aflevering gaat
 # over het weer, de vakantie en wat je graag doet. In C4 is de vídeo de
 # leidraad (CLAUDE.md), dus de unit volgt de aflevering — net zoals bij U10.
 # De kleding kwam één aflevering later alsnog: ze staat nu in U12, waar de
 # video ze behandelt, en het winkelen in U13.
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
 # ── U12 · gebouwd op aflevering 12 «La ropa y los colores» ────────────────
 12: [
  ("La ropa", "de kleren", "👕", [
    ("la chaqueta", "de jas · het jasje"), ("el jersey", "de trui"),
    ("la camisa", "het hemd"), ("la camiseta", "het T-shirt"),
    ("la blusa", "de bloes"), ("los pantalones", "de broek"),
    ("la falda", "de rok"), ("el vestido", "de jurk"),
    ("la corbata", "de das"), ("el abrigo", "de winterjas")]),
  ("Los zapatos", "schoenen en de rest", "👟", [
    ("los zapatos", "de schoenen"), ("las zapatillas", "de sportschoenen"),
    ("las botas", "de laarzen"), ("los calcetines", "de kousen"),
    ("la gorra", "de pet"), ("el bolso", "de handtas")]),
  ("Los colores", "de kleuren", "🎨", [
    ("negro/a", "zwart"), ("blanco/a", "wit"), ("verde", "groen"),
    ("azul", "blauw"), ("rojo/a", "rood"), ("amarillo/a", "geel"),
    ("gris", "grijs"), ("marrón", "bruin")]),
  ("¿Cómo es?", "iemand beschrijven", "🧑", [
    ("alto/a · bajo/a", "groot · klein"), ("guapo/a", "knap"),
    ("fuerte", "sterk · gespierd"), ("delgado/a · gordo/a", "slank · dik"),
    ("tiene los ojos azules", "hij/zij heeft blauwe ogen"),
    ("moderno/a · viejo/a", "modern · oud"),
    ("bueno/a · barato/a", "goed · goedkoop")]),
  ("Cada mañana", "wederkerende werkwoorden", "🪥", [
    ("levantarse", "opstaan"), ("ducharse", "zich douchen"),
    ("peinarse", "zich kammen"), ("afeitarse", "zich scheren"),
    ("vestirse", "zich aankleden"), ("ponerse la chaqueta", "de jas aandoen")]),
  ("¿Cómo te queda?", "over kleren oordelen", "💬", [
    ("llevar", "dragen · aanhebben"),
    ("me queda bien", "het staat me goed"),
    ("me queda ancho", "het zit me te wijd"),
    ("me queda estrecho", "het zit me te strak"),
    ("en cambio", "daarentegen")]),
 ],
 # ── U13 · gebouwd op aflevering 13 «En el mercado» ────────────────────────
 13: [
  ("La fruta y la verdura", "fruit en groenten", "🍎", [
    ("la manzana", "de appel"), ("la naranja", "de sinaasappel"),
    ("el plátano", "de banaan"), ("el tomate", "de tomaat"),
    ("la lechuga", "de sla"), ("la cebolla", "de ui"),
    ("la verdura", "de groenten"), ("la fruta", "het fruit")]),
  ("Carne y pescado", "vlees en vis", "🐟", [
    ("el pollo", "de kip"), ("la ternera", "het kalfsvlees"),
    ("la carne picada", "het gehakt"), ("el pescado", "de vis"),
    ("el atún", "de tonijn"), ("pescado fresco", "verse vis"),
    ("una lata de atún", "een blikje tonijn")]),
  ("Y además", "de rest van het mandje", "🥖", [
    ("el pan", "het brood"), ("el pan integral", "het volkorenbrood"),
    ("los huevos", "de eieren"), ("la leche", "de melk"),
    ("el chocolate", "de chocolade"), ("una tableta de chocolate", "een reep chocolade")]),
  ("Las tiendas", "waar je wat koopt", "🏪", [
    ("el mercado", "de markt"), ("la pescadería", "de viswinkel"),
    ("la carnicería", "de slagerij"), ("la panadería", "de bakkerij"),
    ("la frutería", "de fruitwinkel"), ("el supermercado", "de supermarkt")]),
  ("¿Cuánto cuesta?", "de prijs", "💶", [
    ("¿Cuánto cuesta?", "Hoeveel kost het?"),
    ("¿Cuánto cuestan?", "Hoeveel kosten ze?"),
    ("dos con veinte el kilo", "twee twintig de kilo"),
    ("caro/a · barato/a", "duur · goedkoop"),
    ("es una oferta", "het is een aanbieding"),
    ("un kilo · medio kilo", "een kilo · een halve kilo")]),
  ("¿Por qué?", "naar de reden vragen", "❓", [
    ("¿Por qué?", "Waarom?"), ("porque…", "omdat · want"),
    ("por eso", "daarom · dus"), ("No lo sé", "Ik weet het niet"),
    ("¿Cuántos? · ¿Cuántas?", "Hoeveel?"), ("¿Dónde venden…?", "Waar verkopen ze…?")]),
 ],
 # ── U14 · gebouwd op aflevering 14 «En el restaurante» ────────────────────
 14: [
  ("En el restaurante", "in het restaurant", "🍽️", [
    ("el camarero · la camarera", "de ober · de serveerster"),
    ("la mesa", "de tafel"), ("el menú · la carta", "het menu · de kaart"),
    ("la cuenta", "de rekening"), ("la reserva", "de reservering"),
    ("mesa para cuatro", "een tafel voor vier")]),
  ("Los platos", "de gerechten", "🥘", [
    ("el primer plato", "het voorgerecht"),
    ("el segundo plato", "het hoofdgerecht"),
    ("el postre", "het nagerecht"), ("la sopa", "de soep"),
    ("la paella", "de paella"), ("la tortilla", "de tortilla"),
    ("los calamares", "de inktvisringen"), ("el cordero", "het lam"),
    ("la merluza", "de heek"), ("la tarta de chocolate", "de chocoladetaart"),
    ("el flan", "de flan (pudding)")]),
  ("Para beber", "om te drinken", "🥤", [
    ("el agua", "het water"), ("una botella de agua", "een fles water"),
    ("el vino", "de wijn"), ("la cerveza", "het bier"),
    ("el café solo", "de zwarte koffie"),
    ("el café con leche", "de koffie met melk"),
    ("el café cortado", "de koffie met een wolkje melk")]),
  ("Pedir", "bestellen", "🙋", [
    ("¿Quiere(n) algo de beber?", "Wilt u iets drinken?"),
    ("Yo quiero…", "Ik wil…"), ("Yo prefiero…", "Ik heb liever…"),
    ("¿Van a tomar postre?", "Neemt u een nagerecht?"),
    ("Les recomiendo…", "Ik raad u … aan"),
    ("La cuenta, por favor", "De rekening, alstublieft")]),
  ("Yo también · yo tampoco", "het eens of oneens zijn", "🤝", [
    ("Yo también", "Ik ook"), ("Yo tampoco", "Ik ook niet"),
    ("Yo sí", "Ik wel"), ("Yo no", "Ik niet"),
    ("Encantado/a", "Aangenaam"),
    ("Encantado de conocerte", "Aangenaam kennis te maken")]),
  ("¡Qué rico!", "smaak en superlatief", "😋", [
    ("¡Qué rico!", "Wat lekker!"), ("buenísimo/a", "ontzettend lekker"),
    ("guapísimo/a", "beeldschoon"), ("simpatiquísimo/a", "ontzettend aardig"),
    ("está muy bueno", "het is heel lekker"), ("algo dulce", "iets zoets")]),
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
 12: ("Me ducho · llevo · es y está",
      "handelingen op jezelf — en wat je aanhebt",
      [("Yo <b>me</b> ducho, yo <b>me</b> peino", "yo", "ik douche mij, ik kam mij"),
       ("Tú <b>te</b> duchas, tú <b>te</b> peinas", "tú", "jij doucht je"),
       ("Él <b>se</b> afeita", "él · ella", "hij scheert zich"),
       ("Vosotros <b>os</b> ducháis", "vosotros", "jullie douchen je"),
       ("Paul <b>lleva</b> una chaqueta negra", "ahora mismo",
        "wat hij nú aanheeft → llevar"),
       ("Yo no <b>tengo</b> corbatas", "posesión", "wat je bezit → tener"),
       ("Paul <b>es</b> alto y guapo", "ser · cómo es siempre",
        "hoe hij áltijd is → ser"),
       ("Paul <b>está</b> fuerte", "estar · cómo está ahora",
        "hoe hij er nú aan toe is → estar")],
      "Drie valstrikken op één bladzijde. Eén: <b>me</b> ducho, niet «yo ducho» — "
      "de handeling komt op jezelf terug. Twee: wat je <b>aanhebt</b> is "
      "<b>llevar</b>, niet «tener» en zeker niet «dragen» in de zin van sjouwen. "
      "Drie: <b>es</b> guapo is wie hij is, <b>está</b> fuerte is hoe hij er nu "
      "bij loopt."),
 13: ("¿Cuánto cuesta? · o → ue",
      "vragen naar prijs en reden — en de klinker die springt",
      [("cost<b>a</b>r → ¿Cuánto c<b>ue</b>sta?", "o → ue", "kosten → hoeveel kost het?"),
       ("cost<b>a</b>r → ¿Cuánto c<b>ue</b>stan?", "plural", "hoeveel kosten ze?"),
       ("p<b>o</b>der → ¿P<b>ue</b>do…?", "o → ue", "kunnen → mag ik…?"),
       ("v<b>o</b>lver → v<b>ue</b>lvo mañana", "o → ue", "terugkomen → ik kom morgen terug"),
       ("¿<b>Por qué</b> no vas?", "la pregunta", "waarom ga je niet? (twee woorden)"),
       ("<b>Porque</b> estoy enfermo", "la respuesta", "omdat ik ziek ben (één woord)"),
       ("Estoy enfermo, <b>por eso</b> no voy", "la consecuencia", "daarom ga ik niet")],
      "<b>Por qué</b> (twee woorden, met accent) is de vraag; <b>porque</b> (één "
      "woord, zonder accent) is het antwoord. En let op: «want» én «omdat» zijn "
      "in het Spaans allebei <b>porque</b>. «Dus» is <b>por eso</b> of "
      "<b>así que</b> — nooit «luego»."),
 14: ("…que… · o · -ísimo",
      "twee zinnen aaneen, kiezen, en overdrijven",
      [("Ésa es la mesa <b>que</b> nos gusta", "relativo",
        "dát is de tafel díe we graag hebben"),
       ("Somos cuatro personas <b>que</b> van a cenar", "relativo",
        "we zijn met vier die gaan eten"),
       ("¿Vino <b>o</b> agua?", "elegir", "wijn of water?"),
       ("¿Café solo <b>o</b> con leche?", "elegir", "zwarte koffie of met melk?"),
       ("guapa → guap<b>ísima</b>", "-ísimo", "knap → beeldschoon"),
       ("bueno → buen<b>ísimo</b>", "-ísimo", "lekker → ontzettend lekker"),
       ("simpáticos → simpatiqu<b>ísimos</b>", "c → qu",
        "aardig → ontzettend aardig (spelling!)")],
      "Twee dingen. Eén: <b>que</b> is hier «die» of «dat», niet «wat» — en het "
      "valt in het Spaans nóóit weg, ook al doen wij dat wel («de tafel <i>die</i> "
      "we graag hebben»). Twee: bij <b>-ísimo</b> valt de laatste klinker weg "
      "(buen<i>o</i> → buenísimo) en verandert de <b>c</b> in <b>qu</b> "
      "(simpáti<i>c</i>o → simpatiquísimo), anders klinkt het niet meer."),
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
      "Spaans laat je hóren wat voor zin het is. Een vraag krult omhoog, een "
      "uitroep gaat omhoog en dan kort omlaag, een mededeling zakt gewoon. In deze "
      "aflevering staan alle drie naast elkaar, in één les van Julio.",
      ["¿Te levantas, por favor?", "¿Les parece guapo?", "Paul lleva corbata.",
       "¡Muy bien!", "¿Paul se afeita?"],
      ("¡ … ! y ¿ … ?",
       "Het teken staat er twee keer: aan het begin ondersteboven, aan het eind gewoon. "
       "Zo weet je vóór het lezen al hoe de zin klinkt.",
       [("¿Cómo estás?", "¿ … ?"), ("¡Qué guapo!", "¡ … !"),
        ("Llevo un jersey verde.", "geen teken")])),
 13: ("El enlace — las palabras se dan la mano",
      "Spanjaarden plakken woorden aaneen: het einde van het ene woord en het begin "
      "van het volgende worden één klank. Daarom klinkt een marktgesprek zo snel.",
      ["en_el_mercado", "una_lata_de_atún", "los_huevos", "el_atún",
       "dos_con_veinte"],
      ("La pregunta sube",
       "Een ja-neevraag gaat aan het eind omhoog; een vraag met een vraagwoord "
       "(¿dónde? ¿cuánto? ¿por qué?) gaat juist omlaag.",
       [("¿Son caras?", "omhoog ↗"), ("¿Es una oferta?", "omhoog ↗"),
        ("¿Cuánto cuestan los tomates?", "omlaag ↘"),
        ("¿Dónde venden pescado fresco?", "omlaag ↘")])),
 14: ("Todos los sonidos",
      "Alle klanken van dit jaar door elkaar, en allemaal op één menukaart: "
      "ñ · c/z · g/gu · j · ll/y · r/rr · s.",
      ["España", "cerveza", "merluza", "jamón", "paella", "cordero", "postre"],
      ("Aguda · llana · esdrújula",
       "Drie soorten woorden, en de tilde volgt daaruit. Klap de klemtoon, dan zie je het.",
       [("café", "a·GU·da (laatste) — mét tilde"),
        ("menú", "a·GU·da — mét tilde"),
        ("postre", "POS·tre · LLA·na (voorlaatste)"),
        ("camarero", "ca·ma·RE·ro · LLA·na"),
        ("buenísimo", "bue·NÍ·si·mo · es·DRÚ·ju·la (altijd tilde)")])),
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
 12: ("El desfile de la clase",
      "Describe a un compañero como Julio describe a Paul: ropa, colores y una "
      "diferencia contigo.",
      "Beschrijf een klasgenoot zoals Julio Paul beschrijft: kleren, kleuren en "
      "één verschil met jezelf.",
      ["Kies iemand uit de klas (of een foto) en noteer wat hij/zij aanheeft: "
       "<b>lleva…</b> + kleur.",
       "Voeg twee beschrijvingen toe met <b>ser</b>: <i>es alto, es simpático</i>.",
       "Voeg één met <b>estar</b> toe: <i>hoy está cansado</i>.",
       "Zet er één verschil met jezelf naast, met <b>en cambio</b>: "
       "«Él lleva zapatos; yo, en cambio, llevo zapatillas.»",
       "Eindig met één wederkerend werkwoord over jouw ochtend: "
       "<i>Yo me levanto a las siete y me ducho.</i>"]),
 13: ("Mi lista de la compra",
      "Vas al mercado con veinte euros. Haz tu lista y regatea el precio.",
      "Je gaat met twintig euro naar de markt. Maak je lijst en vraag de prijs.",
      ["Schrijf zes producten op, elk bij de juiste winkel "
       "(<i>pescadería · carnicería · frutería · panadería</i>).",
       "Zet er per product een hoeveelheid bij: <i>un kilo, medio kilo, una lata…</i>",
       "Bereid twee prijsvragen voor: <b>¿Cuánto cuesta…?</b> en <b>¿Cuánto cuestan…?</b>",
       "Speel de scène in tweetallen: één is de verkoper, één de klant.",
       "Zeg tot slot waarom je iets níet koopt, met <b>porque</b>: "
       "«No compro el cordero <i>porque</i> es muy caro.»"]),
 14: ("La cena del año",
      "Cuatro personas, un restaurante, un menú entero: de la bebida al café.",
      "Vier personen, één restaurant, een volledig menu: van het drankje tot de koffie.",
      ["Verdeel de rollen: twee klanten, één ober, één die de rekening vraagt.",
       "Bestel iets te drinken; minstens één iemand antwoordt met "
       "<b>yo también</b> of <b>yo tampoco</b>.",
       "Bestel een voorgerecht, een hoofdgerecht en een nagerecht van de kaart.",
       "De ober beveelt iets aan met <b>les recomiendo…</b> en één <b>-ísimo</b>.",
       "Reageer op het eten met <b>¡Qué rico!</b> en vraag daarna de rekening."]),
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
 12: (12, "La ropa y los colores",
      "Zeggen wat iemand aanheeft, hoe hij eruitziet — en wat je elke ochtend doet.",
      "la ropa · los colores · llevar · los verbos reflexivos",
      "Paul lleva una chaqueta negra, buena. Yo, en cambio, llevo un jersey verde, barato.",
      [("Nombrar la <b>ropa</b> y los <b>colores</b>", "una chaqueta negra · un jersey verde"),
       ("Decir qué <b>lleva</b> alguien", "lleva corbata · llevo zapatillas viejas"),
       ("<b>Describir</b> a una persona", "es alto · tiene los ojos azules · está fuerte"),
       ("Hablar de tu <b>rutina</b> con verbos reflexivos", "me ducho · me peino · se afeita")],
      "Julio geeft les en zet Paul vooraan als levend voorbeeld: Paul is groot, "
      "hij niet; Paul heeft een goede jas, hij een goedkope trui. Terwijl hij "
      "zichzelf de grond in praat, leer jij precies wat je nodig hebt om iemand "
      "te beschrijven — en om te zeggen wat je zelf elke ochtend doet.",
      ["la chaqueta", "el jersey", "los pantalones", "moderno", "el color",
       "azul", "flexible", "diferente"]),
 13: (13, "En el mercado",
      "Boodschappen doen: producten, winkels, prijzen — en waarom.",
      "la fruta · la carne · el pescado · ¿cuánto cuesta?",
      "¿Cuánto cuestan los tomates? — Dos con veinte el kilo.",
      [("Nombrar la <b>comida</b>", "manzanas · tomates · pollo · atún · pan"),
       ("Decir en qué <b>tienda</b> se compra", "la pescadería · la carnicería · la frutería"),
       ("Preguntar el <b>precio</b> y decir si es caro", "¿cuánto cuesta? · es una oferta"),
       ("Preguntar y dar una <b>razón</b>", "¿por qué? · porque… · por eso…")],
      "Julio en María komen elkaar tegen op de markt. Zij zet zijn mandje recht — "
      "een ui, een blikje tonijn en zes repen chocolade — en stelt intussen de hele "
      "boodschappenlijst samen. Hij hoort er ongeveer niets van, want hij is met "
      "iets heel anders bezig. Alles wat zij zegt, heb jij nodig zodra je zelf op "
      "een Spaanse markt staat.",
      ["el tomate", "el chocolate", "la fruta", "el kilo", "la dieta",
       "mediterránea", "vegetariano", "la vitamina"]),
 14: (14, "En el restaurante",
      "Een heel menu bestellen — van het drankje tot de koffie.",
      "el menú · pedir · yo también · -ísimo",
      "De carne les recomiendo el cordero. Paella, excelente, y calamares buenísimos.",
      [("Pedir en un <b>restaurante</b>", "mesa para cuatro · yo quiero… · la cuenta"),
       ("Nombrar los <b>platos</b> y las <b>bebidas</b>", "sopa · paella · flan · café solo"),
       ("Mostrar <b>acuerdo</b> o desacuerdo", "yo también · yo tampoco · yo sí"),
       ("<b>Valorar</b> con -ísimo", "buenísimo · guapísima · ¡qué rico!")],
      "De laatste parada. María gaat voor het eerst uit eten met de ouders van "
      "Julio, en het loopt zoals zulke avonden lopen: de moeder kiest de tafel, "
      "praat over de vórige vriendin, en niemand durft wijn te bestellen. Jij "
      "leert intussen een volledig menu bestellen — en dat is precies wat je in "
      "Spanje het eerst nodig hebt.",
      ["el restaurante", "el menú", "la paella", "el chocolate", "excelente",
       "la fruta", "el café", "la persona"]),
}
