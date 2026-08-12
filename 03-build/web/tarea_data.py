#!/usr/bin/env python3
"""De eindtaken, voor de schrijfcoach.

WAAROM DIT ZO KLEIN IS
De coach moet weten wát er in de tekst hoort. Dat staat grotendeels al ergens:
elke beurt van het rollenspel (`rol_data.py`) is precies «de leerling moet dit
kunnen zeggen», mét de patronen om het te herkennen. De eindtaak is in wezen
diezelfde inhoud, maar dan in één geschreven tekst. De criteria worden daarom
uit het rollenspel afgeleid en hoeven hier niet nog eens te staan.

Wat hier wél staat, is wat een eindtaak tot een eindtaak maakt (CLAUDE.md §14):
**afzender · ontvanger · doel · situatie · resultaat**. Een opdracht als
«gebruik tien woorden en vijf werkwoorden» is geen communicatieve taak; «schrijf
een kaartje aan je klasgenoten zodat ze weten wie je bent» wel.

  titulo     de naam zoals ze in het boek staat
  para       aan wie de leerling schrijft (de ontvanger)
  objetivo   waarvoor — wat de lezer daarna weet of doet
  palabras   (minimum, streefgetal) — geen maximum, want te veel schrijven is
             geen fout
  extra      criteria die het rollenspel níet dekt, als (label, [patronen])
"""

# (cursus, unit) → de eindtaak
TAREAS = {
 # ── C4 · ¡Bienvenidos al español! ──────────────────────────────────────────
 ("C4", 1): {"titulo": "Mi presentación", "para": "je nieuwe klasgenoten",
             "objetivo": "zodat ze weten hoe je heet", "palabras": (12, 25),
             "extra": []},
 ("C4", 2): {"titulo": "Un día de saludos", "para": "een Spaanse vriend",
             "objetivo": "een kort berichtje sturen", "palabras": (15, 30),
             "extra": []},
 ("C4", 3): {"titulo": "Mi mapa · ¿de dónde eres?", "para": "de klasmuur",
             "objetivo": "zodat iedereen ziet waar je vandaan komt",
             "palabras": (15, 30), "extra": []},
 ("C4", 4): {"titulo": "Mi árbol de familia", "para": "je uitwisselingspartner",
             "objetivo": "zodat hij je familie leert kennen", "palabras": (20, 40),
             "extra": []},
 ("C4", 5): {"titulo": "Diccionario de la clase", "para": "de klas",
             "objetivo": "drie voorwerpen benoemen en uitleggen",
             "palabras": (20, 40), "extra": []},
 ("C4", 6): {"titulo": "Plano de mi casa", "para": "een gast die langskomt",
             "objetivo": "zodat hij alles terugvindt", "palabras": (20, 40),
             "extra": []},
 ("C4", 7): {"titulo": "¿Quién soy? · adivina", "para": "de klas",
             "objetivo": "laten raden welk beroep je beschrijft",
             "palabras": (20, 40), "extra": []},
 ("C4", 8): {"titulo": "Mi horario", "para": "een vriend die wil afspreken",
             "objetivo": "zodat hij weet wanneer je kan", "palabras": (20, 40),
             "extra": []},
 ("C4", 9): {"titulo": "Mi finde", "para": "je Spaanse vriend",
             "objetivo": "vertellen wat je gaat doen", "palabras": (25, 45),
             "extra": []},
 ("C4", 10): {"titulo": "¿Quién hace qué?", "para": "je huisgenoten",
              "objetivo": "de taken verdelen", "palabras": (25, 45), "extra": []},
 ("C4", 11): {"titulo": "El tiempo y mis vacaciones", "para": "je klasgenoten",
              "objetivo": "vertellen waar je heen gaat en waarom",
              "palabras": (25, 45), "extra": []},
 ("C4", 12): {"titulo": "El desfile de la clase", "para": "de klas",
              "objetivo": "iemand beschrijven zodat ze raden wie het is",
              "palabras": (25, 45), "extra": []},
 ("C4", 13): {"titulo": "Mi lista de la compra", "para": "wie mee gaat winkelen",
              "objetivo": "zodat hij weet wat en waar te kopen",
              "palabras": (25, 45), "extra": []},
 ("C4", 14): {"titulo": "La cena del año", "para": "de ober",
              "objetivo": "een volledig menu bestellen", "palabras": (30, 55),
              "extra": []},

 # ── C5 · Español en la práctica ────────────────────────────────────────────
 ("C5", 0): {"titulo": "Tarjeta de embarque", "para": "je klasgenoten",
             "objetivo": "jezelf voorstellen aan de groep", "palabras": (30, 55),
             "extra": [("Je begroet iemand",
                        [r"hola", r"buenos\s+d[ií]as", r"buenas\s+(tardes|noches)"])]},
 ("C5", 1): {"titulo": "Mi pasaporte", "para": "de administratie van een uitwisseling",
             "objetivo": "je gegevens doorgeven", "palabras": (35, 60),
             "extra": [("Je vermeldt je leeftijd", [r"tengo\s+\w+\s*a[ñn]os"])]},
 ("C5", 2): {"titulo": "Álbum de familia", "para": "je Spaanse gastgezin",
             "objetivo": "zodat ze je familie kennen vóór je aankomt",
             "palabras": (45, 80),
             "extra": [("Je beschrijft iemands karakter",
                        [r"(simp[aá]tic|maj|gracios|trabajador|inteligente|habladora?|tranquil|t[ií]mid)"])]},
 ("C5", 3): {"titulo": "Un día en mi vida", "para": "je uitwisselingspartner",
             "objetivo": "zodat hij weet hoe jouw dag loopt", "palabras": (45, 80),
             "extra": [("Je noemt minstens één uur", [r"a\s+las?\s+\w+"]),
                       ("Je gebruikt een woord voor hoe vaak",
                        [r"(siempre|normalmente|a\s+veces|a\s+menudo|casi\s+nunca|nunca|todos\s+los\s+d[ií]as)"])]},
 ("C5", 4): {"titulo": "Mi playlist", "para": "de klas",
             "objetivo": "je muziek voorstellen en zeggen waarom",
             "palabras": (45, 80),
             "extra": [("Je geeft een reden met porque", [r"porque\s+\w+"])]},
 ("C5", 5): {"titulo": "La carta", "para": "de gasten van je restaurant",
             "objetivo": "een kaart die iemand echt kan bestellen",
             "palabras": (45, 80),
             "extra": [("Je noemt een prijs", [r"\d+\s*(euros?|pesos?|€)"])]},
 ("C5", 6): {"titulo": "Abre tu tienda", "para": "je klanten",
             "objetivo": "je winkel voorstellen met prijzen en maten",
             "palabras": (45, 80),
             "extra": [("Je noemt een kleur",
                        [r"(rojo|roja|negro|negra|blanco|blanca|azul|verde|gris|amarill|marr[oó]n|morad)"])]},
 ("C5", 7): {"titulo": "Mapa de mi barrio", "para": "iemand die op bezoek komt",
             "objetivo": "zodat hij de weg vindt", "palabras": (45, 80),
             "extra": [("Je gebruikt een plaatsbepaling",
                        [r"(al\s+lado|cerca|lejos|enfrente|encima|debajo|entre|detr[aá]s|delante)"])]},
 ("C5", 8): {"titulo": "Diario de viaje", "para": "wie je reis volgt",
             "objetivo": "vertellen wat je gedaan hebt", "palabras": (50, 90),
             "extra": [("Je gebruikt de voltooide tijd", [r"h[ea]\s+\w+[ai]do",
                                                          r"h[ea]\s+(hecho|visto|dicho|escrito|vuelto|puesto|roto|abierto)"])]},

 # ── C6+ · Más español en la práctica · edición única ───────────────────────
 ("C6+", 0): {"titulo": "Tarjeta de reencuentro", "para": "de klasmuur",
              "objetivo": "jezelf opnieuw voorstellen na de zomer",
              "palabras": (40, 70), "extra": []},
 ("C6+", 1): {"titulo": "Mi día a día", "para": "je uitwisselingspartner",
              "objetivo": "zodat hij jouw dag kan volgen", "palabras": (50, 90),
              "extra": [("Je gebruikt een volgordewoord",
                         [r"(primero|luego|despu[eé]s|por\s+[uú]ltimo|antes\s+de)"])]},
 ("C6+", 2): {"titulo": "Mapa de mi barrio", "para": "iemand die je kamer huurt",
              "objetivo": "zodat hij weet waar alles ligt", "palabras": (50, 90),
              "extra": [("Je vergelijkt twee dingen",
                         [r"m[aá]s\s+\w+\s+que", r"menos\s+\w+\s+que", r"tan\s+\w+\s+como",
                          r"(mejor|peor|mayor|menor)\s+que"])]},
 ("C6+", 3): {"titulo": "Mi plan de fin de semana", "para": "je vrienden",
              "objetivo": "een plan voorstellen en verdedigen", "palabras": (50, 90),
              "extra": [("Je geeft je mening",
                         [r"(creo|pienso|me\s+parece)\s+que", r"en\s+mi\s+opini[oó]n"])]},
 ("C6+", 4): {"titulo": "Mi mejor viaje", "para": "de lezers van je reisblog",
              "objetivo": "één reis vertellen", "palabras": (60, 100),
              "extra": [("Je gebruikt por of para", [r"\bpor\b", r"\bpara\b"])]},
 ("C6+", 5): {"titulo": "Una biografía", "para": "de klas",
              "objetivo": "het leven van iemand vertellen", "palabras": (60, 110),
              "extra": [("Je gebruikt de verleden tijd",
                         [r"\w+[óo]\b", r"\b(fue|tuvo|hizo|estuvo|dijo|vino|pudo|dio|vio|naci[oó]|muri[oó])\b"]),
                        ("Je noemt een jaartal of een tijdsbepaling",
                         [r"\b(18|19|20)\d{2}\b", r"hace\s+\w+\s+a[ñn]os",
                          r"(el\s+a[ñn]o\s+pasado|ayer|entonces)"])]},
 ("C6+", 6): {"titulo": "Cuando era pequeño/a", "para": "je klasgenoten",
              "objetivo": "vertellen hoe het vroeger was", "palabras": (60, 110),
              "extra": [("Je gebruikt de vorm voor vroeger",
                         [r"\w+(aba|ía)\b", r"\b(era|iba|ten[ií]a|hab[ií]a|sol[ií]a)\b"]),
                        ("Je zet vroeger tegenover nu",
                         [r"\bantes\b", r"\bahora\b", r"ya\s+no"])]},
 ("C6+", 7): {"titulo": "Mi cartel de opinión", "para": "de school",
              "objetivo": "anderen overtuigen met een raad", "palabras": (55, 100),
              "extra": [("Je geeft een raad in de gebiedende wijs",
                         [r"\b(cuida|come|bebe|haz|ven|di|s[eé]|recicla|apaga|duerme|mu[eé]vete|evita)\b"]),
                        ("Je verbindt je argumenten",
                         [r"(porque|adem[aá]s|por\s+eso|sin\s+embargo|por\s+un\s+lado)"])]},
}


def tarea(curso, unidad):
    return TAREAS.get((curso, unidad))


if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import rol_data as RD
    print("%-4s %-3s %-30s %-6s %s" % ("", "", "eindtaak", "woorden", "criteria"))
    for (c, u), t in sorted(TAREAS.items(), key=lambda x: (x[0][0], x[0][1])):
        r = RD.rol(c, u)
        n = (len(r["pasos"]) if r else 0) + len(t["extra"])
        print("%-4s U%-2d %-30s %3d–%-3d %d%s"
              % (c, u, t["titulo"][:30], t["palabras"][0], t["palabras"][1], n,
                 "" if r else "   ← geen rollenspel om uit te putten"))
    print("\n%d eindtaken" % len(TAREAS))
