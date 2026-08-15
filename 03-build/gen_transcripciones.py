#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Haalt de veertien C4-videotranscripten uit de cursus en zet ze apart.

WAAROM
De transcripten zitten in de units — als meeleestekst naast de video, met een
Nederlandse regel die de leerling aan- en uitzet. Wie ze los nodig heeft (om
na te lezen, om er een toets op te maken, om ze aan een collega te geven) moet
ze nu uit veertien pagina's plukken. Dit zet ze in één document, in dezelfde
volgorde als de cursus, mét de link naar de aflevering.

TWEE BRONNEN, ÉÉN UITVOER
U1–U10 hebben elk hun eigen «escucha»-generator met een `SCENES`-lijst; U11–U14
delen er één en halen hun scènes uit `escena_data.py`. Dat verschil is
historisch (zie `gen_c4_escena.py`) en hoeft de lezer niet te interesseren, dus
het wordt hier weggewerkt.

De tien eerste worden met `ast` gelezen en niet geïmporteerd: die scripts
schrijven bij het importeren hun HTML-bestand weg, en een leesopdracht hoort
niets te veranderen. `SCENES` is een letterlijke lijst, dus `literal_eval`
volstaat.

    python3 03-build/gen_transcripciones.py          # → …/print/C4_TRANSCRIPCIONES.md
    python3 03-build/gen_transcripciones.py --sueltos  # + één bestand per unit
"""
import ast
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AQUI = os.path.join(ROOT, "03-build")
WEB = os.path.join(AQUI, "web")
sys.path.insert(0, WEB)

import escena_data as EE          # noqa: E402

SALIDA = os.path.join(WEB, "print", "C4_TRANSCRIPCIONES.md")
SUELTOS = os.path.join(WEB, "print", "transcripciones")

# De titel van elke aflevering zoals ze in de cursus heet. U11–U14 dragen hem
# in `escena_data`; voor U1–U10 staat hij in de kop van de escucha-pagina, maar
# daar zit hij verweven met opmaak — deze lijst is korter en leest beter.
TITULOS = {
    1: "Presentaciones", 2: "Saludos", 3: "Nacionalidades y países",
    4: "La familia", 5: "Objetos cotidianos", 6: "La casa y los lugares",
    7: "Las profesiones", 8: "La hora y los días", 9: "Planes y obligaciones",
    10: "Las tareas de casa",
}


def _literal(ruta, nombre):
    """De waarde van één toewijzing op moduleniveau, zonder het script te draaien."""
    arbol = ast.parse(open(ruta, encoding="utf-8").read())
    for nodo in arbol.body:
        if (isinstance(nodo, ast.Assign) and isinstance(nodo.targets[0], ast.Name)
                and nodo.targets[0].id == nombre):
            return ast.literal_eval(nodo.value)
    return None


def enlace(fuente):
    """(«youtube»|«drive», id) → een adres dat je kunt aanklikken."""
    if not fuente:
        return ""
    tipo, vid = fuente
    if tipo == "youtube":
        return "https://www.youtube.com/watch?v=" + vid
    return "https://drive.google.com/file/d/%s/view" % vid


def unidades():
    """[(unit, titel, videolink, [(scènetitel, situatie, [(wie, es, nl)])])]"""
    out = []
    for u in range(1, 11):
        ruta = os.path.join(WEB, "gen_c4u%d_escucha.py" % u)
        if not os.path.exists(ruta):
            continue
        escenas = _literal(ruta, "SCENES") or []
        out.append((u, TITULOS.get(u, ""), enlace(_literal(ruta, "VIDEO_SRC")),
                    [(t, s, list(lineas)) for t, s, lineas in escenas]))
    for u in sorted(EE.ESCENAS):
        d = EE.ESCENAS[u]
        out.append((u, d["titulo"], enlace(EE.VIDEO.get(u)),
                    [(t, s, [tuple(l) for l in lineas]) for t, s, lineas in d["escenas"]]))
    return out


def markdown(datos):
    n_esc = sum(len(e) for _u, _t, _l, e in datos)
    n_lin = sum(len(li) for _u, _t, _l, e in datos for _t2, _s, li in e)
    out = ["# C4 · «¡Bienvenidos al español!» — de transcripten van de veertien afleveringen",
           "",
           "Wat er in beeld gezegd wordt, zoals het in de cursus naast de video "
           "staat: elke regel in het Spaans met de Nederlandse vertaling eronder. "
           "%d afleveringen, %d scènes, %d spreekbeurten." % (len(datos), n_esc, n_lin),
           "",
           "> Gegenereerd uit de cursus zelf (`03-build/gen_transcripciones.py`). "
           "Wijzigt een transcript in een unit, dan wijzigt het hier mee.",
           "",
           "| aflevering | thema | scènes | beurten |",
           "|---|---|---:|---:|"]
    for u, tit, _enl, esc in datos:
        out.append("| **%d** | %s | %d | %d |"
                   % (u, tit, len(esc), sum(len(li) for _t, _s, li in esc)))
    out.append("")

    for u, tit, enl, esc in datos:
        out += ["---", "", "## Aflevering %d · %s" % (u, tit), ""]
        if enl:
            out += ["🎬 [de aflevering bekijken](%s)" % enl, ""]
        for titulo, situacion, lineas in esc:
            out += ["### %s" % titulo, ""]
            if situacion:
                out += ["*%s*" % situacion, ""]
            for quien, es, nl in lineas:
                out.append("**%s** — %s" % (quien, es))
                if nl:
                    out.append("> %s" % nl)
                out.append("")
    return "\n".join(out)


def suelto(u, tit, enl, esc):
    out = ["# Aflevering %d · %s" % (u, tit), ""]
    if enl:
        out += ["🎬 [de aflevering bekijken](%s)" % enl, ""]
    for titulo, situacion, lineas in esc:
        out += ["## %s" % titulo, ""]
        if situacion:
            out += ["*%s*" % situacion, ""]
        for quien, es, nl in lineas:
            out.append("**%s** — %s" % (quien, es))
            if nl:
                out.append("> %s" % nl)
            out.append("")
    return "\n".join(out)


def main():
    datos = unidades()
    faltan = [u for u, _t, enl, _e in datos if not enl]
    os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
    open(SALIDA, "w", encoding="utf-8").write(markdown(datos))
    print("→ %s · %d afleveringen, %d scènes, %d beurten"
          % (SALIDA, len(datos),
             sum(len(e) for _u, _t, _l, e in datos),
             sum(len(li) for _u, _t, _l, e in datos for _t2, _s, li in e)))
    if faltan:
        print("   zonder videolink: %s" % faltan)
    if "--sueltos" in sys.argv:
        os.makedirs(SUELTOS, exist_ok=True)
        for u, tit, enl, esc in datos:
            p = os.path.join(SUELTOS, "C4_aflevering_%02d.md" % u)
            open(p, "w", encoding="utf-8").write(suelto(u, tit, enl, esc))
        print("   + %d losse bestanden in %s" % (len(datos), SUELTOS))


if __name__ == "__main__":
    main()
