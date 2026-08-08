#!/usr/bin/env python3
"""Zet de laatste interface-emoji van de digitale pagina om naar Lucide.

De tabbalk en de gedeelde componenten zijn in hun eigen bron omgezet. Wat
overbleef zat verspreid over de zeventien unit-generatoren, telkens net iets
anders geschreven: een luidsprekerknop hier, een zoekveld daar, een
transcriptknop verderop. Zeventien bestanden nalopen voor hetzelfde teken is
vragen om er één te missen, dus gebeurt het hier, ná de bouw, op de gebouwde
pagina — dezelfde aanpak als `limpia_jerga.py` voor het drukwerk.

WAT NIET WORDT AANGERAAKT
De woordkaartjes. De emoji dáár zijn de betekenis van het woord (🍅 🥑 🇲🇽) en
een bewuste keuze uit `vocab_emoji.py`. Ze staan in het `VOCAB`-blok en in de
speldata, en die twee blokken worden overgeslagen.

Ook niet: → ↔ ★ ☆ ✓ in een oefeningtekst. Dat is typografie, geen interface.
Alleen tekens die als knop of melding dienen, gaan om.

Herhaalbaar: een pagina die al om is, blijft ongemoeid.
"""
import glob
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import hub_iconos as HI          # noqa: E402

# emoji → sleutel in hub_iconos.USADOS. Alleen interface.
CAMBIOS = {
    "🔊": "sound",
    "📄": "doc",
    "🔒": "lock",
    "🔎": "search",
    "🎙️": "rec", "🎙": "rec",
    "🎧": "escuchar",
    "🎯": "retos",
    "🎮": "juegos",
    "🧩": "gram",
    "↻": "again",
    "✅": "bien",
    "❌": "mal",
    "✏️": "edit", "✏": "edit",
    "💾": "save",
}

# De blokken waar emoji juist wél horen: de woordenschat en de speldata.
SALTAR = (
    re.compile(r"const VOCAB=\[.*?\n\];", re.S),
    re.compile(r"GAMES=\{.*?\};", re.S),
    re.compile(r"const BANDAS=\[.*?\];", re.S),
)


def _zonas_protegidas(doc):
    """[(begin, eind)] van de stukken die niet aangeraakt worden."""
    zonas = []
    for pat in SALTAR:
        for m in pat.finditer(doc):
            zonas.append((m.start(), m.end()))
    return sorted(zonas)


def procesar(ruta):
    doc = open(ruta, encoding="utf-8").read()
    zonas = _zonas_protegidas(doc)

    def protegido(i):
        return any(a <= i < b for a, b in zonas)

    def en_atributo(i):
        """Staat dit teken binnen een tag, dus in een attribuutwaarde?

        In `placeholder="🔎 zoek"` mag geen markup: daar zou `<i class=ic-search>`
        letterlijk in het invulveld verschijnen — en dat deed het ook, tot dit
        erbij kwam. Terugkijken naar het dichtstbijzijnde `<` en `>`: staat het
        haakje-openen dichterbij, dan zitten we binnen een tag.
        """
        abre = doc.rfind("<", 0, i)
        cierra = doc.rfind(">", 0, i)
        return abre > cierra

    salida = []
    ultimo = 0
    n = 0
    for m in re.finditer("|".join(re.escape(e) for e in CAMBIOS), doc):
        if protegido(m.start()) or en_atributo(m.start()):
            continue
        salida.append(doc[ultimo:m.start()])
        salida.append(HI.svg(CAMBIOS[m.group(0)]))
        ultimo = m.end()
        n += 1
    salida.append(doc[ultimo:])
    if n:
        open(ruta, "w", encoding="utf-8").write("".join(salida))
    return n


def main():
    tot = 0
    for ruta in sorted(glob.glob(os.path.join(AQUI, "U*_web.html")) +
                       glob.glob(os.path.join(AQUI, "C6plus_U*_web.html"))):
        n = procesar(ruta)
        tot += n
        print("%-22s %3d interface-iconen" % (os.path.basename(ruta), n))
    print("\n%d emoji omgezet; de woordkaartjes en de spellen bleven ongemoeid" % tot)


if __name__ == "__main__":
    main()
