#!/usr/bin/env python3
"""De Lucide-iconen voor de interface van de digitale pagina.

WAT WEL EN WAT NIET
Op de hub staan twee soorten beeld door elkaar, en dat is precies het probleem:

  * **betekenis** — de kleur-emoji op de woordkaartjes (🍅 🥑 🇲🇽). Die blijven.
    Ze zijn een bewuste keuze (`vocab_emoji.py`, vastgelegd bij U5): een
    woordkaart toont een díng, en daar is kleur een geheugensteun. 415 woorden
    hebben er een.
  * **interface** — de tabbladen, de knoppen, goed/fout, geluid, transcript.
    Dáár was het rommelig: drie van de negen tabbladen hadden een emoji en zes
    niet, en er stonden ✓ én ✅ door elkaar, ✗ én ❌ door elkaar.

Dit bestand doet alleen het tweede. De regel die eruit volgt is makkelijk vol te
houden: **een icoon is interface, een emoji is betekenis.**

De SVG's worden één keer in de pagina gezet, als JavaScript-object `IC`, zodat
de componenten `IC.check` kunnen schrijven waar eerst '✓' stond. Ze erven
`currentColor`, dus ze kleuren mee met de knop of de melding waar ze in staan —
groen bij goed, rood bij fout, zonder een tweede set iconen.
"""
import json
import os
import sys
from urllib.parse import quote

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(AQUI)),
                                "02-huisstijl", "vendor", "lucide"))
sys.path.insert(0, "/home/user/espa-ol-en-la-pr-ctica/02-huisstijl/vendor/lucide")

from iconos import _iconos                       # noqa: E402

# De iconen die de interface nodig heeft. Kort houden: elk icoon is ±300 bytes
# in élke unit-pagina, en de hub moet offline in één bestand passen.
USADOS = {
    # tabbladen
    "vocab": "book-a", "gram": "blocks", "lectura": "book-open",
    "escuchar": "headphones", "juegos": "gamepad-2", "retos": "target",
    "hablar": "mic", "cultura": "globe", "extra": "external-link",
    # meldingen en knoppen
    "check": "check", "x": "x",
    "bien": "circle-check", "mal": "circle-x",
    "sound": "volume-2", "doc": "file-text", "lock": "lock",
    "again": "rotate-ccw", "search": "search", "star": "sparkles",
    "rec": "mic", "play": "play", "stop": "square",
    "edit": "pencil", "save": "download",
}

def _uri(nombre):
    """Het icoon als data-URI voor een CSS-masker."""
    datos = _iconos()
    svg = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' "
           "stroke='black' stroke-width='2' stroke-linecap='round' "
           "stroke-linejoin='round'>%s</svg>" % datos[nombre].replace('"', "'"))
    return "data:image/svg+xml," + quote(svg, safe="")


def _css():
    """Eén regel per icoon.

    Als masker en niet als `background-image`: een masker neemt de vórm van het
    icoon en vult die met `currentColor`, dus het icoon kleurt mee met de knop of
    de melding waar het in staat — groen bij goed, rood bij fout, zonder een
    tweede set bestanden. Een gewone achtergrondafbeelding kan dat niet.

    En als `<i class="ic ic-check">` in plaats van inline SVG: dan zit er geen
    enkel aanhalingsteken in de HTML, en kan hetzelfde stukje markup zowel in een
    JavaScript-tekenreeks als in gewone HTML staan zonder te breken.
    """
    # Eén selectorlijst voor de gedeelde eigenschappen, zodat de markup met
    # één klasse toekan: `<i class=ic-check>` — zónder aanhalingstekens en
    # zonder spatie. Dat stukje kan daardoor even veilig in een JS-tekenreeks
    # met enkele als met dubbele aanhalingstekens staan, en dat is precies waar
    # het terechtkomt: de hub bouwt haar meldingen in JavaScript.
    todas = ",".join(".ic-%s" % k for k in sorted(USADOS))
    filas = ["""
%s{display:inline-block;width:1.05em;height:1.05em;vertical-align:-.16em;flex:none;
 background-color:currentColor;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;
 -webkit-mask-position:center;mask-position:center;-webkit-mask-size:contain;
 mask-size:contain}
.tab i[class^=ic-],button i[class^=ic-]{margin-right:.32em}
""" % todas]
    for clave, nombre in sorted(USADOS.items()):
        u = _uri(nombre)
        filas.append(".ic-%s{-webkit-mask-image:url(\"%s\");mask-image:url(\"%s\")}"
                     % (clave, u, u))
    return "\n".join(filas)


CSS = _css()


def svg(clave):
    """Het icoon als markup — bruikbaar in HTML én in een JS-tekenreeks."""
    if clave not in USADOS:
        raise KeyError("geen interface-icoon «%s»" % clave)
    return '<i class=ic-%s></i>' % clave


def js():
    """Het `IC`-object voor de JavaScript-kant van de hub."""
    tabla = {k: svg(k) for k in USADOS}
    return "const IC=%s;\n" % json.dumps(tabla, ensure_ascii=False, separators=(",", ":"))


if __name__ == "__main__":
    print("%d interface-iconen · CSS %d bytes · JS %d bytes"
          % (len(USADOS), len(CSS), len(js())))
