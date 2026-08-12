#!/usr/bin/env python3
"""De verwijzing boek → PowerPoint — in het docentendossier, niet in het boek.

DE VERWIJZING STOND OP DE VERKEERDE BLADZIJDE
Ze stond onder elke sectiekop van de leerlingcursus: «En clase: diapositiva 6 —
El verbo SER». De auteur streepte ze door bij het nalezen van C5 U1 en schreef
erbij: «Weglaten» · «Moet dat in de leerlingencursus?». Nee: welk dianummer bij
welke sectie hoort, is lesorganisatie — dat hoort bij de leerkracht, niet bij de
leerling. CLAUDE.md §16 vraagt de kruisverwijzing wél, dus ze verdwijnt niet:
ze verhuist naar `03-build/web/print/PUENTES_docente.md`.

Waarom als nabewerking en niet in de zeventien generatoren: het dianummer komt
uit het deck, en dat deck verandert (de reto-dia's kwamen er later bij). Door de
brug ná de bouw te leggen, klopt hij altijd met het deck dat er op dat moment
ligt — en één script vervangt zeventien keer handwerk.

Secties waarvoor geen dia bestaat, krijgen niets: liever geen verwijzing dan een
verwijzing naar een dia die er niet is.

Herhaalbaar: oude bruggen die nog in een gebouwde bladzijde staan, worden
verwijderd.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import enlaces as EN          # noqa: E402

import puentes as PU          # noqa: E402

ROOT = "/home/user/espa-ol-en-la-pr-ctica"
MARCA_INI = "<!-- puente-ppt -->"

# Welk gebouwd bestand hoort bij welke unit.
def unidades():
    """(curso, unidad, print-HTML) — de lijst staat in enlaces.py, zie daar."""
    for curso, u, impreso, _hub in EN.unidades():
        yield (curso, u, impreso)


# De sectiekop ziet er zo uit: <span class="pk">§2 · El verbo SER …</span>
# gevolgd door <div class="intro">…</div>. Daarachter zetten we de brug.
SECCION = re.compile(
    r'(<span class="pk"[^>]*>(?P<tit>[^<]+)</span>'
    r'(?:<div class="lpd">.*?</div>)?'
    r'<div class="intro">.*?</div>)', re.S)

# Secties waar een dia-verwijzing niets toevoegt.
SALTAR = ("Vocabulario", "Repaso", "Taller de lengua", "¡Ponte al día!")


def clave_de(titulo):
    """Van «§2 · El verbo SER + los pronombres» naar de zoekwoorden voor het deck.

    Staat de titel van de tekst tussen guillemets — «El primer día en el
    instituto» — dan is dát het beste zoekwoord: de dia draagt dezelfde naam."""
    cita = re.search(r"«([^»]{4,44})»", titulo)
    if cita:
        return [cita.group(1)]
    t = re.sub(r"^[§\w.]+\s*·\s*", "", titulo).strip()
    t = re.sub(r"\s*[·—-]\s*.*$", "", t).strip()      # alleen het eerste deel
    # de kernwoorden: laat lidwoorden en voorzetsels vallen
    palabras = [w for w in re.split(r"[\s/]+", t)
                if len(w) > 2 and w.lower() not in
                ("los", "las", "del", "con", "por", "para", "que", "una", "uno")]
    return palabras[:2] or [t]


def procesar(curso, unidad, ruta):
    original = open(ruta, encoding="utf-8").read()
    # oude bruggen eruit, zodat het script herhaalbaar is
    doc = re.sub(re.escape(MARCA_INI) + r'<div class="route-note">.*?</div>', "",
                 original)

    puestos, saltados = [], []

    def sustituir(m):
        titulo = m.group("tit")
        if any(s in titulo for s in SALTAR):
            return m.group(1)
        pal = clave_de(titulo)
        if "Tarea final" in titulo:
            n = PU.dia(curso, unidad, "Tarea final") or PU.dia(curso, unidad, *pal)
        else:
            n = PU.dia(curso, unidad, *pal)
        if n is None and len(pal) > 1:
            n = PU.dia(curso, unidad, pal[0])
        if n is None:
            saltados.append(titulo)
            return m.group(1)
        dtit = dict(PU.titulos(curso, unidad))[n].strip("«»")
        puestos.append((titulo, n, dtit))
        # niets meer in de leerlingbladzijde; alleen noteren voor het dossier
        return m.group(1)

    nuevo = SECCION.sub(sustituir, doc)
    if nuevo != original:
        open(ruta, "w", encoding="utf-8").write(nuevo)
    return puestos, saltados


DOSSIER = os.path.join(ROOT, "03-build", "web", "print", "PUENTES_docente.md")


def main():
    tot_p = tot_s = 0
    md = ["# Boek ↔ PowerPoint — welke dia hoort bij welke sectie",
          "",
          "> Voor de leerkracht. In de leerlingcursus staat deze verwijzing niet:",
          "> welk dianummer bij welke sectie hoort is lesorganisatie (auteur 2026-08-12).",
          "> Wordt bij elke build herschreven, dus altijd gelijk aan het deck dat er nu ligt.",
          ""]
    for curso, unidad, ruta in unidades():
        p, s = procesar(curso, unidad, ruta)
        tot_p += len(p); tot_s += len(s)
        print("%-4s U%d  %2d bruggen, %d secties zonder dia" % (curso, unidad, len(p), len(s)))
        md.append("## %s · Unidad %d" % (curso, unidad))
        md.append("")
        md.append("| Sectie | Dia | Titel van de dia |")
        md.append("|---|---|---|")
        for tit, n, dtit in p:
            md.append("| %s | %d | %s |" % (tit, n, dtit))
        for tit in s:
            md.append("| %s | — | *geen dia gevonden* |" % tit)
        md.append("")
    open(DOSSIER, "w", encoding="utf-8").write("\n".join(md) + "\n")
    print("\n%d bruggen in het docentendossier, %d secties zonder dia" % (tot_p, tot_s))
    print("→ %s" % os.path.relpath(DOSSIER, ROOT))


if __name__ == "__main__":
    main()
