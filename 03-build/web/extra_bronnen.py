#!/usr/bin/env python3
"""Externe bronnen per unit — de inhoud van het tabblad «Extra».

Tot nu toe stond daar «de leerkracht vult de links aan» en «link volgt». Dat is
precies het soort meta-tekst dat CLAUDE.md §18 uit de leerlingeneditie verbant:
ofwel de links staan er, ofwel het kader verdwijnt.

De lijst is door de auteur aangeleverd en per onderwerp geordend, in dezelfde
volgorde als de unit zelf: eerst het taalsysteem (§1–§4), dan de woordenschat-
clusters. Eén bron kan bij meerdere onderwerpen horen — dat is geen fout maar
een gevolg van hoe de bronsites hun oefeningen bundelen (een pagina over
persoonlijke informatie dekt zowel *presentarse* als *la edad*).

Structuur:  BRONNEN[(cursus, unit)] = [ (onderwerp, [ (bron, titel, url), … ]), … ]
Een `url` die op youtube.com wijst wordt automatisch als video herkend.
"""

# Vaste herkenningskleur/afkorting per bronsite.
SITES = {
    "ProfeDeELE":       ("PDE", "🎬"),
    "Arche-ELE":        ("ARE", "🧩"),
    "My Daily Spanish": ("MDS", "📺"),
}

BRONNEN = {}

# Eén uitgelicht geheel per unit: materiaal dat de héle unidad bestrijkt en dus
# niet onder één onderwerp thuishoort. Het staat bovenaan, vóór de themalijsten.
DESTACADO = {
    ("C5", 0): {
        "kicker": "Repaso de toda la unidad",
        "titel": "El museo de las palabras perdidas",
        "soort": "Escape room",
        "url": "https://museo-palabras-perdidas.wim-wuyts1979.chatgpt.site/",
        "es": "Un museo ha perdido sus palabras. Solo sales si superas las pruebas: "
              "los sonidos, la tilde, los números, el género y los saludos.",
        "nl": "Een museum is zijn woorden kwijt. Je raakt er alleen uit door de proeven te "
              "doorstaan: de klanken, de tilde, de getallen, het geslacht en de saludos. "
              "Álle leerstof van deze unidad in één spel.",
        "tip": "Doe hem als afsluiting, nadat je de oefeningen hierboven hebt gemaakt — "
               "of samen met een klasgenoot, om beurten.",
    },
}

BRONNEN[("C5", 0)] = [
    ("§1 · Klanksysteem — letters, klanken en uitspraak", [
        ("ProfeDeELE", "Letras y sonidos del español",
         "https://www.profedeele.es/actividad/letras-sonidos-espanol/"),
        ("ProfeDeELE", "El abecedario · alfabeto español",
         "https://www.profedeele.es/actividad/abecedario-alfabeto-espanol/"),
        ("ProfeDeELE", "Ortografía — verzamelpagina",
         "https://www.profedeele.es/ortografia/"),
        ("Arche-ELE", "El alfabeto · letras y sonidos",
         "https://arche-ele.com/el-alfabeto-abecedario-letras-y-sonidos"),
        ("My Daily Spanish", "Het alfabet en de uitspraak (video)",
         "https://www.youtube.com/watch?v=KwpdV3aLddw"),
        ("My Daily Spanish", "Uitgebreide uitspraakgids",
         "https://mydailyspanish.com/spanish-pronunciation-guide/"),
    ]),
    ("§2 · Acentuación — aguda, llana, esdrújula en de tilde", [
        ("ProfeDeELE", "Acentos y tildes — hoofdoefening",
         "https://www.profedeele.es/actividad/actividad-de-acentos-tildes/"),
        ("ProfeDeELE", "Palabras agudas",
         "https://www.profedeele.es/actividad/palabras-agudas/"),
        ("ProfeDeELE", "Palabras llanas",
         "https://www.profedeele.es/actividad/palabras-llanas/"),
        ("ProfeDeELE", "Palabras esdrújulas",
         "https://www.profedeele.es/actividad/acentos-palabras-esdrujulas/"),
        ("ProfeDeELE", "Acentos — verzamelpagina",
         "https://www.profedeele.es/ortografia/acentos/"),
        ("Arche-ELE", "La acentuación · aguda, llana, esdrújula, la tilde",
         "https://arche-ele.com/la-acentuacion-aguda-llana-esdrujula-la-tilde"),
        ("My Daily Spanish", "De accentregels (video)",
         "https://www.youtube.com/watch?v=iVgA3FGJVLI"),
    ]),
    ("§3 · Números 0–100", [
        ("ProfeDeELE", "Los números en español — todos",
         "https://www.profedeele.es/actividad/numeros-espanol-todos/"),
        ("ProfeDeELE", "Los números del 0 al 9 — basis",
         "https://www.profedeele.es/actividad/numeros-del-0-al-9/"),
        ("Arche-ELE", "Los números — interactieve oefeningen",
         "https://arche-ele.com/los-numeros-numbers-in-spanish-ele-actividades"),
        ("My Daily Spanish", "De getallen 1–100 (video)",
         "https://www.youtube.com/watch?v=dffV7FSFzCM"),
    ]),
    ("§4 · Género y artículos — el of la", [
        ("ProfeDeELE", "Género masculino / femenino",
         "https://www.profedeele.es/actividad/genero-masculino-femenino/"),
        ("ProfeDeELE", "El artículo definido e indefinido",
         "https://www.profedeele.es/actividad/articulo-definido-indefinido/"),
        ("Arche-ELE", "El género — regels en uitzonderingen",
         "https://arche-ele.com/el-genero-masculino-femenino-aprende-espanol-spanish"),
        ("Arche-ELE", "Infografiek «El género» (pdf)",
         "https://arche-ele.com/wp-content/uploads/2020/11/Infografia-Genero.pdf"),
        ("Arche-ELE", "El artículo — nivel A1",
         "https://arche-ele.com/el-articulo-nivel-a1-indeterminado-determinado"),
        ("My Daily Spanish", "El of la? (video)",
         "https://www.youtube.com/watch?v=2bJy0ehC0i8"),
    ]),
    ("Saludos y despedidas", [
        ("ProfeDeELE", "Saludos y despedidas",
         "https://www.profedeele.es/actividad/saludos-despedidas/"),
        ("Arche-ELE", "Saludos y despedidas",
         "https://arche-ele.com/saludos-y-despedidas-aprende-espanol-learn-spanish"),
        ("My Daily Spanish", "Begroeten en jezelf voorstellen (video)",
         "https://www.youtube.com/watch?v=i0uwQDZo0Ew"),
        ("My Daily Spanish", "Basiszinnen en begroetingen (video)",
         "https://www.youtube.com/watch?v=vyrXC5JDGTc"),
    ]),
    ("Lengua de clase — praten in de klas", [
        ("ProfeDeELE", "Dar y pedir información personal",
         "https://www.profedeele.es/actividad/dar-pedir-informacion-personal/"),
        ("Arche-ELE", "La clase — woordenschat en interactieve oefeningen",
         "https://arche-ele.com/la-clase-ele-vocabulario-actividades-interactivas"),
        ("Arche-ELE", "El primer día en la clase de español",
         "https://arche-ele.com/el-primer-dia-en-la-clase-de-espanol-aprender-espanol"),
        ("My Daily Spanish", "Bruikbare basiszinnen (video)",
         "https://www.youtube.com/watch?v=vyrXC5JDGTc"),
    ]),
    ("Presentarse y la edad — jezelf voorstellen", [
        ("ProfeDeELE", "Dar y pedir información personal",
         "https://www.profedeele.es/actividad/dar-pedir-informacion-personal/"),
        ("Arche-ELE", "Información personal",
         "https://arche-ele.com/informacion-personal-aprende-espanol-learn-spanish"),
        ("My Daily Spanish", "Jezelf voorstellen (video)",
         "https://www.youtube.com/watch?v=i0uwQDZo0Ew"),
    ]),
    ("El mundo hispano — landen en cultuur", [
        ("ProfeDeELE", "Países hispanohablantes",
         "https://www.profedeele.es/actividad/paises-hispanohablantes/"),
        ("ProfeDeELE", "Escape room · Google Maps y los países hispanohablantes",
         "https://www.profedeele.es/actividad/escape-room-google-maps-y-los-paises-hispanohablantes/"),
        ("Arche-ELE", "Países hispanohablantes — woordenschat",
         "https://arche-ele.com/paises-hispanohablantes-vocabulario-aprende-espanol"),
        ("My Daily Spanish", "De Spaanstalige wereld (video)",
         "https://www.youtube.com/watch?v=fuInQ1rJKrw"),
    ]),
    ("Países, lenguas y nacionalidades", [
        ("ProfeDeELE", "Países, lenguas y nacionalidades",
         "https://www.profedeele.es/actividad/paises-lenguas-nacionalidades/"),
        ("Arche-ELE", "Países y nacionalidades",
         "https://arche-ele.com/paises-y-nacionalidades-countries-nationalities"),
    ]),
]


# --------------------------------------------------------------------------- #
def _esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def html(course, unit):
    """Het volledige Extra-paneel. Leeg als er voor deze unit geen lijst is."""
    groepen = BRONNEN.get((course, unit))
    if not groepen:
        return ""
    n = sum(len(v) for _t, v in groepen)
    uit = ['<h2 class="sec">Extra · bronnen</h2>',
           '<p class="lead">Wil je meer oefenen dan wat hier staat? Deze pagina\'s van '
           '<b>ProfeDeELE</b>, <b>Arche-ELE</b> en <b>My Daily Spanish</b> behandelen precies de '
           'onderwerpen van deze unidad. <span class="gloss">%d bronnen, geordend zoals de unit '
           'zelf. Ze openen in een nieuw tabblad.</span></p>' % n]

    d = DESTACADO.get((course, unit))
    if d:
        uit.append(
            '<a class="destacado" href="%s" target="_blank" rel="noopener">'
            '<span class="dest-ico" aria-hidden="true">🗝️</span>'
            '<span class="dest-tekst">'
            '<span class="dest-kicker">%s</span>'
            '<span class="dest-titel">%s</span>'
            '<span class="dest-es">%s</span>'
            '<span class="dest-nl">%s</span>'
            '<span class="dest-tip">💡 %s</span></span>'
            '<span class="dest-badge">%s</span></a>'
            % (_esc(d["url"]), _esc(d["kicker"]), _esc(d["titel"]), _esc(d["es"]),
               _esc(d["nl"]), _esc(d["tip"]), _esc(d["soort"])))
    for titel, items in groepen:
        uit.append('<div class="card brongroep"><h3>%s</h3><ul class="bronlijst">' % _esc(titel))
        for bron, naam, url in items:
            afk, ico = SITES.get(bron, ("", "🔗"))
            video = "youtube.com" in url or "youtu.be" in url
            uit.append(
                '<li><a href="%s" target="_blank" rel="noopener">%s %s</a>'
                '<span class="bronbadge %s">%s</span>%s</li>'
                % (_esc(url), ico, _esc(naam), afk.lower(), _esc(bron),
                   '<span class="bronsoort">video</span>' if video else ""))
        uit.append("</ul></div>")
    uit.append('<div class="card"><p>📄 In het boek verwijzen de QR-codes naar deze digitale '
               'pagina, telkens op het juiste ankerpunt.</p></div>')
    return "\n    ".join(uit)


CSS = r"""
/* Uitgelicht materiaal dat de hele unidad bestrijkt — mag opvallen, maar blijft
   binnen de cursuskleur; geen tweede accentkleur erbij. */
.destacado{display:flex;gap:16px;align-items:flex-start;text-decoration:none;color:var(--ink);
  background:linear-gradient(135deg,var(--gt),var(--card));border:2px solid var(--g);
  border-radius:16px;padding:18px 20px;margin:0 0 18px;position:relative}
.destacado:hover,.destacado:focus-visible{border-color:var(--gd);box-shadow:0 4px 18px rgba(0,0,0,.08)}
.destacado:focus-visible{outline:3px solid var(--gd);outline-offset:3px}
.dest-ico{font-size:34px;line-height:1;flex:none}
.dest-tekst{display:flex;flex-direction:column;gap:4px;min-width:0}
.dest-kicker{font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--gd)}
.dest-titel{font-family:var(--disp);font-size:21px;font-weight:800;color:var(--gd);line-height:1.15}
.dest-es{font-style:italic;font-size:14px}
.dest-nl{font-size:13px;color:var(--mut)}
.dest-tip{font-family:var(--hand,var(--body));font-size:13px;color:var(--gd);margin-top:4px}
.dest-badge{position:absolute;top:-11px;right:16px;background:var(--g);color:#fff;font-size:11px;
  font-weight:800;letter-spacing:.05em;padding:4px 12px;border-radius:999px;white-space:nowrap}
@media(max-width:520px){.destacado{flex-direction:column;gap:10px}.dest-badge{right:12px}}
.brongroep h3{font-family:var(--disp);color:var(--gd);margin:0 0 10px;font-size:16px}
.bronlijst{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:2px}
.bronlijst li{display:flex;align-items:center;gap:9px;flex-wrap:wrap;padding:7px 9px;border-radius:9px}
.bronlijst li:nth-child(odd){background:var(--gt)}
.bronlijst a{color:var(--ink);text-decoration:none;font-weight:600;flex:1 1 220px;min-width:0}
.bronlijst a:hover,.bronlijst a:focus-visible{color:var(--gd);text-decoration:underline}
.bronlijst a:focus-visible{outline:3px solid var(--gd);outline-offset:2px;border-radius:4px}
.bronbadge{font-size:10px;font-weight:800;letter-spacing:.04em;padding:3px 8px;border-radius:999px;
  background:var(--card);border:1.5px solid var(--line);color:var(--mut);white-space:nowrap;flex:none}
.bronsoort{font-size:10px;font-weight:700;color:var(--gd);background:var(--gt);
  border-radius:999px;padding:3px 8px;flex:none}
"""


if __name__ == "__main__":
    for (c, u), g in sorted(BRONNEN.items()):
        print("%s U%d — %d onderwerpen, %d bronnen" % (c, u, len(g), sum(len(v) for _t, v in g)))
        alle = [x[2] for _t, v in g for x in v]
        print("   unieke links: %d van %d" % (len(set(alle)), len(alle)))
