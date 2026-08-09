#!/usr/bin/env python3
"""De rollenspellen: één gesprek per unit, met een doel en een einde.

WAAROM EEN GESLOTEN SCÈNE EN GEEN VRIJE CHAT
Een open gesprek met een taalmodel loopt op A1 binnen tien minuten vast op
hetzelfde: de leerling typt Nederlands, krijgt vlekkeloos Spaans terug ver boven
zijn niveau, en er wordt niets geleerd — het lijkt alleen zo. Daar helpt maar
één ding tegen, en dat is de vórm: een scène met een rol, een doel en een
einde. De ober vraagt wat je wil drinken; daar zijn maar zoveel antwoorden op.

Bovendien staat er hier geen model achter (auteur 2026-08-09: offline, geen
leerlingtekst die de school verlaat). De partner kent dus alleen wat hieronder
staat — en juist omdat de scène gesloten is, valt dat niet op.

HOE EEN STAP WERKT
Elke `paso` is één beurt van de ober plus wat de leerling daarop kan zeggen:

  di       wat de ober zegt (Spaans) + `nl` als steun eronder
  meta     wat de leerling in deze beurt moet klaarspelen (staat op het scherm)
  hueco    het invulkader: een zin met twee gaten die de leerling zelf typt,
           plus een woordbank als steun. Dit is de bélangrijkste stand — bij
           aanklikken kan een leerling gokken, bij twee gaten moet hij de vorm
           produceren. `respuestas` geeft per gat de aanvaarde antwoorden;
           `mal` legt uit wat er misgaat bij de fout die hier het meest gemaakt
           wordt.
  opciones antwoorden om uit te kiezen — precies één is goed (in één beurt twee,
           omdat afslaan er ook bij hoort). De foute zijn niet willekeurig: het
           zijn de fouten die déze leerling maakt, zoals een verkeerd lidwoord.
           **Twee opties mag.** Waar er maar één zinnige afleider bestaat, is een
           derde erbij verzinnen erger dan niets: een stroman met een Nederlands
           woord erin herkent de leerling meteen als «die zal het niet zijn», en
           dan oefent hij het uitsluiten van onzin in plaats van Spaans.
  acepta   voor wie zelf typt: de patronen die als goed gelden. **Eén ervan
           volstaat** — het zijn alternatieven, geen eisen die allemaal moeten
           kloppen. Ruim genomen, want «quiero una sopa», «para mí una sopa» en
           «una sopa, por favor» zijn alle drie juist en het zou pijnlijk zijn
           ze af te keuren. Wat er verder nog aan schort (kortaf, verkeerd
           lidwoord) vangt de corrector op; die staat los en zwijgt niet omdat
           de beurt geslaagd is.
  pista    de hint na een misser — nooit meteen het antwoord
  modelo   het modelantwoord, pas te zien ná een poging of via «muéstrame»

De patronen zijn JavaScript-regex; ze worden hoofdletter- en accentongevoelig
toegepast (zie `gen_rol.py`, functie `normaliza`), zodat «cafe» ook telt.
"""

# unit → het rollenspel
# (titel, wie de leerling is, wie de partner is, de opdracht, [pasos], slot)
ROLES = {
 ("C5", 5): {
  "titulo": "En el restaurante",
  "lugar": "Ciudad de México · un restaurante en la Roma",
  "tu": "Tú, de klant",
  "otro": "El mesero",
  "otro_avatar": "🧑‍🍳",
  "mision": "Bestel een volledige maaltijd: een tafel, iets te drinken, een "
            "eerste gerecht, een hoofdgerecht en een nagerecht. Vraag daarna "
            "de rekening.",
  "mision_es": "Pide una comida completa y, al final, la cuenta.",
  "pasos": [
   {"di": "¡Buenas tardes! Bienvenido. ¿Mesa para cuántas personas?",
    "nl": "Goedemiddag! Welkom. Een tafel voor hoeveel personen?",
    "meta": "Vraag een tafel voor twee.",
    "hueco": {"marco": "___ mesa ___ dos, por favor.",
              "respuestas": [["una"], ["para"]],
              "banco": ["un", "una", "para", "por", "de"],
              "mal": ["<b>Mesa</b> is vrouwelijk — het lidwoord moet meeveranderen.",
                      "«Voor twee personen» is <b>para</b> dos. <i>Por</i> betekent iets anders."]},
    "opciones": [
      ("Una mesa para dos, por favor.", True, None),
      ("Un mesa para dos, por favor.", False,
       "<b>Mesa</b> is vrouwelijk: <i>una</i> mesa."),
    ],
    "acepta": [r"(una\s+)?mesa\s+para\s+(dos|2)", r"para\s+(dos|2)\s+personas",
               r"somos\s+(dos|2)"],
    "pista": "Begin met «Una mesa para…» en zeg hoeveel personen.",
    "modelo": "Una mesa para dos, por favor."},

   {"di": "Perfecto, por aquí. Aquí tienen la carta. ¿Qué van a tomar?",
    "nl": "Prima, deze kant op. Hier is de kaart. Wat wilt u drinken?",
    "meta": "Bestel iets te drinken. Beleefd graag.",
    "hueco": {"marco": "¿___ ___ un agua, por favor?",
              "respuestas": [["me"], ["pone", "trae"]],
              "banco": ["me", "yo", "pone", "trae", "gusta"],
              "mal": ["Het is <b>me</b> pone — «zet u míj». «Yo pone» bestaat niet.",
                      "Gebruik <b>pone</b> (zet u me) of <b>trae</b> (brengt u me)."]},
    "opciones": [
      ("¿Me pone un agua, por favor?", True, None),
      ("Quiero un agua.", False,
       "Inhoudelijk juist, maar het klinkt kortaf. Zet er <b>por favor</b> bij, "
       "of gebruik <b>¿me pone…?</b>"),
      ("Yo gusto un refresco.", False,
       "«Ik wil» is niet «yo gusto». Gebruik <b>quiero</b>, <b>para mí</b> of "
       "<b>¿me pone…?</b> — en <i>me gusta</i> betekent «ik vind lekker»."),
    ],
    "acepta": [r"(me\s+pone|me\s+trae|quiero|para\s+m[ií]|voy\s+a\s+tomar)",
               r"(un|una|el|la)\s+(agua|refresco|zumo|caf[eé]|t[eé]|leche)"],
    "pista": "Kies uit: el agua · el refresco · el zumo · el café · el té. "
             "Zeg het met «¿Me pone…?» of «Para mí…».",
    "modelo": "¿Me pone un agua, por favor?"},

   {"di": "Muy bien. De primer plato tenemos sopa, ensalada y guacamole con totopos.",
    "nl": "Heel goed. Als voorgerecht hebben we soep, salade en guacamole met chips.",
    "meta": "Kies een voorgerecht.",
    "hueco": {"marco": "Para ___, ___ sopa.",
              "respuestas": [["mi", "mí"], ["la"]],
              "banco": ["mí", "yo", "la", "el", "una"],
              "mal": ["Na een voorzetsel wordt <i>yo</i> → <b>mí</b>: «para mí».",
                      "<b>La sopa</b> — dit woord is vrouwelijk."]},
    "opciones": [
      ("Para mí, la sopa.", True, None),
      ("Para mí, el sopa.", False,
       "<b>La sopa</b> — dit woord is vrouwelijk."),
      ("Yo quiero la sopa porque tengo hambre y la sopa está muy rico.",
       False,
       "Bijna! Maar <b>la sopa</b> is vrouwelijk, dus: «está muy <i>rica</i>»."),
    ],
    "acepta": [r"(para\s+m[ií]|quiero|me\s+pone|voy\s+a\s+tomar)",
               r"(la\s+)?(sopa|ensalada|guacamole)"],
    "pista": "Zeg «Para mí, …» en kies: la sopa · la ensalada · el guacamole.",
    "modelo": "Para mí, la sopa, por favor."},

   {"di": "¿Y de plato fuerte? Hay tacos de pollo, pescado a la plancha y arroz con verduras.",
    "nl": "En als hoofdgerecht? Er zijn kiptaco's, gegrilde vis en rijst met groenten.",
    "meta": "Kies een hoofdgerecht. Zeg er iets bij: waarom, of hoe je het wil.",
    "hueco": {"marco": "Quiero los tacos de pollo. Me ___ mucho ___ son ricos.",
              "respuestas": [["gustan"], ["porque"]],
              "banco": ["gusta", "gustan", "porque", "por qué", "luego"],
              "mal": ["Meer dan één ding → <b>me gustan</b>, met -n.",
                      "«Want» én «omdat» zijn allebei <b>porque</b>, aan elkaar en zonder accent."]},
    "opciones": [
      ("Quiero los tacos de pollo, por favor. Me gustan mucho.", True, None),
      ("Quiero los tacos de pollo. Yo gusto mucho.", False,
       "Bijna. «Ik vind ze lekker» is <b>me gustan</b> — bij meerdere dingen "
       "wordt het <i>gustan</i>."),
      ("Quiero el pescado, luego no como carne.", False,
       "«Dus» is niet <i>luego</i> (= later). Hier past <b>porque</b>: "
       "«…porque no como carne»."),
    ],
    "acepta": [r"(quiero|para\s+m[ií]|me\s+pone|voy\s+a\s+tomar)",
               r"(tacos|pescado|arroz|pollo)"],
    "pista": "Kies: los tacos de pollo · el pescado · el arroz. Voeg er iets "
             "aan toe met «me gusta(n)» of «porque…».",
    "modelo": "Quiero los tacos de pollo, por favor. Me gustan mucho."},

   {"di": "¡Que aproveche!  …  ¿Todo bien? ¿Van a tomar postre? Hay churros y fruta.",
    "nl": "Eet smakelijk!  …  Alles goed? Neemt u een nagerecht? Er zijn churros en fruit.",
    "meta": "Zeg dat het lekker was en kies een nagerecht — of sla het beleefd af.",
    "hueco": {"marco": "___ muy rico, gracias. De postre, ___ churros.",
              "respuestas": [["esta", "está"], ["los"]],
              "banco": ["está", "es", "los", "el", "las"],
              "mal": ["Hoe iets nú smaakt is <b>está</b>, niet <i>es</i>.",
                      "<b>Los churros</b> — meervoud."]},
    "opciones": [
      ("Está muy rico, gracias. De postre, los churros.", True, None),
      ("Está muy rico, gracias. De postre, el churros.", False,
       "<b>Los churros</b> — het is meervoud."),
      ("No, gracias. Estoy lleno.", True, None),
    ],
    "acepta": [r"(churros|fruta|manzana|pl[aá]tano|fresa|uvas|pi[ñn]a)",
               r"no,?\s*gracias"],
    "pista": "Zeg eerst dat het lekker is («está muy rico») en kies dan: "
             "los churros · la fruta. Of sla af met «No, gracias».",
    "modelo": "Está muy rico, gracias. De postre, los churros."},

   {"di": "Claro que sí. ¿Algo más?",
    "nl": "Natuurlijk. Nog iets anders?",
    "meta": "Vraag de rekening.",
    "hueco": {"marco": "¿Me ___ ___ cuenta, por favor?",
              "respuestas": [["trae", "pone"], ["la"]],
              "banco": ["trae", "pone", "la", "el", "una"],
              "mal": ["<b>Trae</b> = brengt u me. Dat is wat je hier vraagt.",
                      "<b>La cuenta</b> — vrouwelijk."]},
    "opciones": [
      ("¿Me trae la cuenta, por favor?", True, None),
      ("¿Me trae el cuenta, por favor?", False,
       "<b>La cuenta</b> — vrouwelijk."),
    ],
    "acepta": [r"(la\s+)?cuenta"],
    "pista": "Het woord dat je zoekt staat bij «restaurante» in je woordenlijst: "
             "la c___.",
    "modelo": "¿Me trae la cuenta, por favor?"},
  ],
  "final": "Son doscientos ochenta pesos. ¡Muchas gracias y hasta pronto!",
  "final_nl": "Dat is tweehonderdtachtig peso. Hartelijk dank en tot ziens!",
 },
}


def rol(curso, unidad):
    return ROLES.get((curso, unidad))


if __name__ == "__main__":
    import re
    for (c, u), r in sorted(ROLES.items()):
        n_op = sum(len(p["opciones"]) for p in r["pasos"])
        buenas = sum(1 for p in r["pasos"] for _t, ok, _w in p["opciones"] if ok)
        print("%s U%-2d %-22s %d beurten · %d keuzes (%d goed)"
              % (c, u, r["titulo"], len(r["pasos"]), n_op, buenas))
        # elk patroon moet geldig zijn, en het modelantwoord moet zichzelf halen
        for i, p in enumerate(r["pasos"], 1):
            for pat in p["acepta"]:
                re.compile(pat)
            # één patroon volstaat — maar het modelantwoord moet er minstens
            # één halen, anders keurt de oefening haar eigen voorbeeld af
            texto = p["modelo"].lower()
            if not any(re.search(pat, texto, re.I) for pat in p["acepta"]):
                print("   ⚠ beurt %d: het modelantwoord haalt géén enkel "
                      "patroon" % i)
            # en elk juist keuze-antwoord moet er ook doorkomen
            for t, ok, _w in p["opciones"]:
                if ok and not any(re.search(pat, t.lower(), re.I)
                                  for pat in p["acepta"]):
                    print("   ⚠ beurt %d: «%s» staat als juist maar haalt geen "
                          "patroon" % (i, t))
            if not any(ok for _t, ok, _w in p["opciones"]):
                print("   ⚠ beurt %d heeft geen juist antwoord" % i)
