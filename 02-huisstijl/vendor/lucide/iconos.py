#!/usr/bin/env python3
"""Lucide-iconen als inline SVG, in de maat en kleur van onze eigen huisstijl.

CLAUDE.md §15 koos Lucide als iconenset («open lijniconenset, als basis»), maar
de set stond niet in de repo en de units gebruiken emoji. Dit bestand maakt de
keuze bruikbaar.

WAAROM INLINE SVG EN GEEN FONT OF PLAATJE
Print en scherm komen uit één bron. Een inline SVG erft `currentColor`, dus een
icoon kleurt vanzelf mee met de cursuskleur (C5 groen, C6 blauw…) en met de
functionele taalkleuren uit §13. Het schaalt scherp op 300 dpi, het heeft geen
extern bestand nodig — belangrijk, want de hubs moeten offline werken — en de
lijndikte kan mee-ademen met de tekst eromheen.

    from iconos import icono, badge
    icono("headphones", mm=4.4)          → '<svg …>…</svg>'
    badge("👂")                          → hetzelfde icoon, voor die emoji

EMOJI → ICOON
`BADGE` vertaalt de emoji die nú in de cursus staan naar hun Lucide-tegenhanger.
Dat is bewust een beperkte lijst: alleen de vaardigheids- en werkvormlabels, de
elementen die op elke bladzijde terugkeren. Tekens die géén emoji zijn maar
typografie — ★ ☆ voor moeilijkheid, ☐ voor een aankruisvak, → in een keten —
staan er niet in. Die doen hun werk al en zouden er als lijnicoon slechter
uitzien, niet beter.
"""
import json
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
_DATOS = None

# maten in millimeter, afgestemd op de tekstgroottes van cursus-print.css
MM_BADGE = 3.5          # in een vaardigheids-/werkvormlabel (8,4 pt tekst)
MM_TEXTO = 4.2          # tussen lopende tekst (10,3 pt)
MM_KOP = 6.0            # naast een sectiekop
MM_GRANDE = 9.0         # in een kaart (QR, gids, audio)


def _iconos():
    global _DATOS
    if _DATOS is None:
        with open(os.path.join(AQUI, "lucide.json"), encoding="utf-8") as f:
            _DATOS = json.load(f)
    return _DATOS


def existe(nombre):
    return nombre in _iconos()


def icono(nombre, mm=MM_TEXTO, trazo=1.9, color="currentColor", clase="ic"):
    """Eén icoon als inline SVG.

    `trazo` is de lijndikte in het 24×24-raster van Lucide. De standaard staat
    op 1,9 in plaats van de 2 van Lucide zelf: op de kleine maten die wij
    gebruiken (3,5–4,2 mm) oogt 2 net iets te zwaar naast Inter.
    """
    datos = _iconos()
    if nombre not in datos:
        cerca = [k for k in datos if nombre.split("-")[0] in k][:6]
        raise KeyError("geen Lucide-icoon «%s»%s"
                       % (nombre, (" — bedoelde je: " + ", ".join(cerca)) if cerca else ""))
    return ('<svg class="%s" width="%.2fmm" height="%.2fmm" viewBox="0 0 24 24" '
            'fill="none" stroke="%s" stroke-width="%.2f" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true" '
            'style="vertical-align:-.14em">%s</svg>'
            % (clase, mm, mm, color, trazo, datos[nombre]))


# De emoji die nu in de cursus staan, met hun tegenhanger. Alleen wat op élke
# bladzijde terugkomt: de vaardigheden, de werkvormen en de dragers.
BADGE = {
    # vaardigheden
    "👂": "ear",              # escuchar
    "🎧": "headphones",       # audio
    "🔍": "search",           # leer / escanea
    "📖": "book-open",        # lectura
    "✍": "pen-line",          # escribir
    "✏": "pencil",
    "🎙": "mic",              # hablar / grabar
    "🗣": "messages-square",  # interacción
    "👁": "eye",              # observar
    # werkvormen
    "👤": "user",             # solo
    "👥": "users",            # en parejas / en grupo
    "🤝": "handshake",        # co-evaluación
    "🔁": "repeat",           # otra vez / recycling
    "🎭": "drama",            # rollenspel
    "🕵": "search-check",     # zoekopdracht
    "🎯": "target",           # reto
    "🎮": "gamepad-2",        # juego
    # dragers en wegwijzers
    "📊": "presentation",     # verwijzing naar de PowerPoint
    "📍": "map-pin",          # parada op de ruta
    "🌍": "globe",            # el mundo hispano
    "🔗": "link",             # verwijzing
    "🎒": "backpack",         # la mochila
    "🎵": "music",            # canción
    "🍽": "utensils",
    "👕": "shirt",
    "🏠": "house",
}


def badge(emoji, mm=MM_BADGE, **kw):
    """Het icoon dat bij een emoji uit de cursus hoort, of None als het er niet is."""
    nombre = BADGE.get(emoji)
    return icono(nombre, mm=mm, **kw) if nombre else None


def sin_traducir(ruta_repo="/home/user/espa-ol-en-la-pr-ctica"):
    """Welke emoji in de gebouwde cursus nog geen tegenhanger hebben.

    Puur informatief: veel ervan hóéven er geen te krijgen (een vlag, een
    gerecht, een land). Het is bedoeld om te zien of een veelgebruikt label
    over het hoofd gezien is.
    """
    import collections
    import glob
    import re
    emo = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF]")
    cuenta = collections.Counter()
    for f in glob.glob(os.path.join(ruta_repo, "01-cursussen", "*", "U*", "[UC]*.html")):
        if "BEWERKBAAR" in f:
            continue
        for ch in emo.findall(open(f, encoding="utf-8").read()):
            if ch not in BADGE:
                cuenta[ch] += 1
    return cuenta.most_common()


if __name__ == "__main__":
    d = _iconos()
    print("%d Lucide-iconen beschikbaar · %d emoji vertaald" % (len(d), len(BADGE)))
    faltan = [e for e, n in BADGE.items() if n not in d]
    print("ontbrekende namen:", faltan or "geen")
