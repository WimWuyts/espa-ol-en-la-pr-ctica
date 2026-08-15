#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Schrijft de inhoudstafel van de drie cursussen als één markdown-bestand.

WAAROM GEGENEREERD EN NIET GETYPT
Een met de hand geschreven inhoudstafel klopt op de dag dat je hem schrijft.
Deze leest de gebouwde units zelf: de titel uit de hero, de secties uit de
verborgen ankerlijst die `bladspiegel.py` legt (dezelfde lijst die de
bladwijzers in de PDF voedt), het aantal oefeningen uit de nummerbadges en het
aantal bladzijden uit de PDF. Verandert er een sectie, dan verandert de
inhoudstafel mee zodra je dit opnieuw draait.

    python3 03-build/gen_indice.py            # → 03-build/web/print/INHOUDSTAFEL.md
    python3 03-build/gen_indice.py --stdout   # naar het scherm
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AQUI = os.path.join(ROOT, "03-build")
sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(AQUI, "web"))

import enlaces as EN              # noqa: E402
import medir_bladspiegel as MB    # noqa: E402

SALIDA = os.path.join(AQUI, "web", "print", "INHOUDSTAFEL.md")

# Wat elke cursus is. Staat in CLAUDE.md §3; hier alleen wat de lezer van een
# inhoudstafel nodig heeft om te weten wélke cursus hij voor zich heeft.
CURSOS = {
    "C4": ("¡Bienvenidos al español!", "4 Moderne talen", "Rood",
           "pre-A1 → A1-mechaniek",
           "Buiten het leerplan, videogedreven. Leert klánk, accent en chunks — "
           "de mechaniek die het vijfde jaar versnelt zonder de leerplandoelen "
           "van dat jaar op te gebruiken. Elke unit hoort bij één aflevering "
           "van de sitcom."),
    "C5": ("Español en la práctica", "5de jaar", "Groen", "A1-kern + eerste A2",
           "De kerncursus, volgt het leerplan III-Spa-d. Vertrekt van nul — "
           "zij-instromers en leerlingen uit het vierde jaar beginnen samen. "
           "Loopt van Spanje via Mexico en Colombia naar Peru."),
    "C6+": ("Más español en la práctica · edición única", "6de jaar (huidige cohorte)",
            "Paars", "A2 → aanzet B1",
            "Eenmalig traject voor de leerlingen die uit de óude cursus komen: "
            "vult de hiaten en haalt de leerlijnen van het vijfde én het zesde "
            "jaar alsnog binnen."),
}

ORDEN = ("C4", "C5", "C6+")


def _limpio(html):
    html = re.sub(r"<svg.*?</svg>", "", html, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html)).strip()


def _hero(doc):
    """(eyebrow, titel) — beide uit het hero-blok, niet uit de CSS erboven.

    De eerste versie zocht `class="eyebrow"` in het hele bestand en vond de
    CSS-regel; in twee units stond de hero verder naar achter en kwam er onzin
    uit. Daarom eerst het hero-blok afbakenen.
    """
    # C4 zet zijn hero in een <section>, C5 en C6+ in een <div>
    m = re.search(r'<\w+ class="hero"[ >].{0,1400}?</h1>', doc, re.S)
    if not m:
        return "", ""
    bloque = m.group(0)
    eb = re.search(r'class="eyebrow"[^>]*>(.{0,120}?)</', bloque, re.S)
    h1 = re.search(r"<h1[^>]*>(.{0,160}?)</h1>", bloque, re.S)
    return (_limpio(eb.group(1)) if eb else "",
            _limpio(h1.group(1)) if h1 else "")


def _parada(doc, curso, u):
    """De bestemming van deze unit, zoals ze in de unit zelf staat.

    Niet uit de eyebrow: die staat in kapitalen («MÉXICO / CDMX») en daar valt
    geen nette mengvorm van te maken — «CDMX» moet hoofdletters houden en
    «Machu Picchu» niet. Het routebriefje onder de ruta-strook draagt dezelfde
    bestemming wél in gewone schrijfwijze: «Parada 5 · Ciudad de México (CDMX).»

    C4 heeft geen parada in die zin: daar hoort elke unit bij één aflevering
    van de sitcom, en dát is de nuttige aanduiding.
    De twee openers (C5 U0, C6+ U0) hebben geen genummerde parada; die staan
    hieronder met de naam die de hero ze geeft.
    """
    if curso == "C4":
        return "aflevering %d" % u
    m = re.search(r"<b>\s*Parada\s*\d*\s*·?\s*(.{0,90}?)</b>", doc, re.S)
    if m:
        return _limpio(m.group(1)).rstrip(".").strip()
    return {("C5", 0): "El mundo hispano → España",
            ("C6+", 0): "El reencuentro"}.get((curso, u), "")


def _paginas(curso, u):
    nombre = ("C4_U%d" % u if curso == "C4" else
              "%s_U%d" % ("C5" if curso == "C5" else "C6plus", u))
    ruta = (os.path.join(AQUI, "web", "print", nombre + ".pdf") if curso == "C4"
            else os.path.join(AQUI, "pdf", nombre + ".pdf"))
    if not os.path.exists(ruta):
        return 0
    return len(MB.paginas(ruta))


def unidad(curso, u, impreso, hub):
    doc = open(impreso, encoding="utf-8", errors="replace").read()
    _eyebrow, titulo = _hero(doc)
    secciones = [_limpio(t) for _a, t in
                 re.findall(r'<a href="#(sec-\d+)">([^<]*)</a>', doc)]
    web = open(hub, encoding="utf-8", errors="replace").read() if os.path.exists(hub) else ""
    return {
        "titulo": titulo,
        "parada": _parada(doc, curso, u),
        "secciones": secciones,
        # de nummerbadge is een <span> in C5/C6+ en een <div> in C4
        "ejercicios": len(re.findall(r'<\w+ class="anum"', doc)),
        "paginas": _paginas(curso, u),
        "audios": len(re.findall(r"data:audio/(?:mpeg|mp3|wav);base64,", web)),
    }


def markdown():
    datos = {c: [] for c in ORDEN}
    for curso, u, impreso, hub in EN.unidades():
        datos[curso].append((u, unidad(curso, u, impreso, hub)))

    out = ["# Inhoudstafel · «Español en la práctica»",
           "",
           "De drie gebouwde cursussen, unit per unit. Gegenereerd uit de units "
           "zelf (`03-build/gen_indice.py`) — de sectielijsten zijn dezelfde die "
           "de bladwijzers in de PDF voeden, dus wat hier staat, staat er ook.",
           ""]

    tot_p = sum(d["paginas"] for c in ORDEN for _u, d in datos[c])
    tot_e = sum(d["ejercicios"] for c in ORDEN for _u, d in datos[c])
    tot_a = sum(d["audios"] for c in ORDEN for _u, d in datos[c])
    out += ["| cursus | jaar | units | bladzijden | genummerde oefeningen | opnames |",
            "|---|---|---:|---:|---:|---:|"]
    for c in ORDEN:
        nom = CURSOS[c][0]
        out.append("| **%s** · %s | %s | %d | %d | %d | %d |"
                   % (c, nom, CURSOS[c][1], len(datos[c]),
                      sum(d["paginas"] for _u, d in datos[c]),
                      sum(d["ejercicios"] for _u, d in datos[c]),
                      sum(d["audios"] for _u, d in datos[c])))
    out += ["| | | **%d** | **%d** | **%d** | **%d** |"
            % (sum(len(datos[c]) for c in ORDEN), tot_p, tot_e, tot_a), ""]

    for c in ORDEN:
        nom, jaar, color, nivel, texto = CURSOS[c]
        out += ["---", "", "## %s · «%s»" % (c, nom), "",
                "**%s** · huiskleur %s · richtniveau **%s**" % (jaar, color.lower(), nivel),
                "", texto, "",
                "| unit | titel | parada | blz. | oef. | audio |",
                "|---|---|---|---:|---:|---:|"]
        for u, d in datos[c]:
            # Nul oefeningen betekent hier «niet te tellen», niet «geen»: de vier
            # gegenereerde C4-units nummeren hun opgaven zonder nummerbadge.
            out.append("| **U%d** | %s | %s | %d | %s | %d |"
                       % (u, d["titulo"] or "—", d["parada"] or "—",
                          d["paginas"], d["ejercicios"] or "—", d["audios"]))
        if any(not d["ejercicios"] for _u, d in datos[c]):
            out += ["", "> De units met «—» bij *oef.* tellen niet mee in die kolom: "
                    "ze zetten hun opgaven zonder nummerbadge en zijn dus niet op "
                    "dezelfde manier te tellen. Ze hebben er evenveel."]
        out += ["", "### De secties per unit", ""]
        for u, d in datos[c]:
            out.append("**U%d · %s**%s"
                       % (u, d["titulo"], (" — %s" % d["parada"]) if d["parada"] else ""))
            out.append("")
            for s in d["secciones"]:
                out.append("- %s" % s)
            if not d["secciones"]:
                out.append("- *(geen sectiekoppen gevonden)*")
            out.append("")
    out += ["---", "",
            "*Elke unit bestaat in vier formaten: de gedrukte PDF met zijn "
            "bewerkbare HTML-laag, de digitale pagina met zelfcorrectie en "
            "ingebakken audio, en twee PowerPoints (docent + leerling).*", ""]
    return "\n".join(out)


def main():
    texto = markdown()
    if "--stdout" in sys.argv:
        print(texto)
        return
    os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
    open(SALIDA, "w", encoding="utf-8").write(texto)
    print("→ %s (%d regels)" % (SALIDA, texto.count("\n") + 1))


if __name__ == "__main__":
    main()
