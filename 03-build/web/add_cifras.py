#!/usr/bin/env python3
"""Zet de aantallen in het boek gelijk aan wat er écht op de digitale pagina staat.

WAAROM
In één unit stond drie keer een ander aantal: «20 spellen», «24 spelletjes» en
«18 spellen» — alle drie met de hand ingetypt toen de hub nog groeide. Een
leerling die telt, vindt de cursus onbetrouwbaar; en het aantal verandert elke
keer dat er een spel bijkomt.

Daarom wordt het aantal niet meer opgeschreven maar geteld, in de gebouwde hub
zelf, op het moment dat het boek klaarstaat. Zelfde aanpak als `puentes.py` voor
de dianummers: wat kan verschuiven, wordt opgezocht in plaats van ingetypt.

Draait ná de hub-generatoren en vóór de PDF.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import enlaces as EN          # noqa: E402


# «20 spellen», «24 spelletjes», «20 juegos», «20 spelletjes online»
CIFRA = re.compile(r"\b(\d{1,3})\s+(spellen|spelletjes|juegos)\b")


def unidades():
    """(curso, unidad, print-HTML, hub-HTML) — de lijst staat in enlaces.py."""
    return EN.unidades()


def cuenta(ruta_hub):
    """Hoeveel spellen zitten er echt in deze hub?"""
    if not os.path.exists(ruta_hub):
        return None
    d = open(ruta_hub, encoding="utf-8").read()
    m = re.search(r"GAMES=\{(.*?)\};", d, re.S)
    if not m:
        return None
    return len(re.findall(r'"[a-z0-9-]+":\s*"', m.group(1))) or None


def main():
    total = 0
    for curso, u, ruta, hub in unidades():
        n = cuenta(hub)
        if not n:
            print("%-4s U%d  geen hub gevonden — overgeslagen" % (curso, u))
            continue
        doc = open(ruta, encoding="utf-8").read()
        vistos = set()

        def sustituir(m):
            vistos.add(m.group(1))
            return "%d %s" % (n, m.group(2))

        nuevo, k = CIFRA.subn(sustituir, doc)
        if k:
            open(ruta, "w", encoding="utf-8").write(nuevo)
        total += k
        antes = ", ".join(sorted(vistos, key=int))
        print("%-4s U%d  %2d spellen  (%d vermeldingen%s)"
              % (curso, u, n, k, ("; stond er: " + antes) if len(vistos) > 1 else ""))
    print("\n%d aantallen gelijkgezet aan de hub" % total)


if __name__ == "__main__":
    main()
