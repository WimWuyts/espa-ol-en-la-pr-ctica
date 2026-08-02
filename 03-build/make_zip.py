#!/usr/bin/env python3
"""Bouwt een leverings-zip van een cursus UIT DE HUIDIGE BESTANDEN.

Waarom dit script bestaat: een zip is een momentopname. Zodra een hub, PDF of
PowerPoint opnieuw gegenereerd wordt, is een oudere zip stil verouderd (dat is
één keer gebeurd: de C6+-zip bevatte nog de tetris-versies nadat de arcade-
rotatie was doorgevoerd). Dit script leest altijd de bestanden zoals ze NU op
schijf staan en zet er een MANIFEST.md bij met de datum en de inhoud, zodat je
achteraf kan zien waarvan de zip een foto is.

Gebruik:
    python3 03-build/make_zip.py C5            # alle units van C5
    python3 03-build/make_zip.py C6+           # idem C6+
    python3 03-build/make_zip.py C4            # idem C4
    python3 03-build/make_zip.py C5 --units 3 4 5
    python3 03-build/make_zip.py C5 --out /pad/naar/eigen.zip

De zip krijgt per unit een map (U0/, U1/, …) met de vier formaten:
print-PDF · bewerkbare HTML-laag · digitale hub · PowerPoints (docente+alumno).
Ontbrekende bestanden worden gemeld, niet stilgehouden.
"""
import argparse, os, sys, zipfile, datetime, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def p(*parts):
    return os.path.join(ROOT, *parts)

# Per cursus: welke bestanden horen bij unit N, en onder welke naam in de zip.
# Elke waarde is (pad-op-schijf, naam-in-de-zip). {n} = unitnummer.
COURSES = {
    "C4": {
        "label": "C4 · «Bienvenidos al español» (4 Moderne talen)",
        "units": range(1, 15),
        "files": [
            ("03-build/web/print/C4_U{n}.pdf",              "C4_U{n}.pdf"),
            ("03-build/web/print/C4_U{n}.html",             "C4_U{n}_BEWERKBAAR.html"),
            ("03-build/web/componentes/C4_U{n}_hub.html",   "C4_U{n}_hub.html"),
            ("03-build/pptx/C4_U{n}_docente.pptx",          "C4_U{n}_docente.pptx"),
            ("03-build/pptx/C4_U{n}_alumno.pptx",           "C4_U{n}_alumno.pptx"),
        ],
        # losse componenten (comprension, escucha, funciones, kgt, mapa, musica, practica)
        "globs": [("03-build/web/componentes/C4_U{n}_*.html", "componentes/")],
    },
    "C5": {
        "label": "C5 · «Español en la práctica» — kerncursus 5de jaar",
        "units": range(0, 9),
        "files": [
            ("03-build/pdf/C5_U{n}.pdf",                    "C5_U{n}.pdf"),
            ("01-cursussen/05-a1/U{n}/U{n}.html",            "C5_U{n}_BEWERKBAAR.html"),
            ("03-build/web/U{n}_web.html",                  "C5_U{n}_hub.html"),
            ("03-build/pptx/C5_U{n}_docente.pptx",          "C5_U{n}_docente.pptx"),
            ("03-build/pptx/C5_U{n}_alumno.pptx",           "C5_U{n}_alumno.pptx"),
            ("01-cursussen/05-a1/U{n}/LEESMIJ.md",           "LEESMIJ.md"),
        ],
        "globs": [],
    },
    "C6+": {
        "label": "C6+ · vervolgcursus 6de jaar (huidige cohorte)",
        "units": range(0, 8),
        "files": [
            ("01-cursussen/06-vervolg/U{n}/C6plus_U{n}.pdf",             "C6plus_U{n}.pdf"),
            ("01-cursussen/06-vervolg/U{n}/C6plus_U{n}_BEWERKBAAR.html", "C6plus_U{n}_BEWERKBAAR.html"),
            ("03-build/web/C6plus_U{n}_web.html",                        "C6plus_U{n}_hub.html"),
            ("03-build/pptx/C6plus_U{n}_docente.pptx",                   "C6plus_U{n}_docente.pptx"),
            ("03-build/pptx/C6plus_U{n}_alumno.pptx",                    "C6plus_U{n}_alumno.pptx"),
            ("01-cursussen/06-vervolg/U{n}/LEESMIJ.md",                  "LEESMIJ.md"),
        ],
        "globs": [],
    },
}
ALIAS = {"c4":"C4","c5":"C5","c6+":"C6+","c6plus":"C6+","C6plus":"C6+"}


def collect(course, units):
    """→ (entries, missing). entries = [(pad-op-schijf, naam-in-zip)]"""
    spec = COURSES[course]
    entries, missing = [], []
    for n in units:
        folder = "U%d" % n
        # Unit die nog helemaal niet gebouwd is: één regel, geen lijst per bestand.
        if not any(os.path.exists(p(src.format(n=n))) for src, _ in spec["files"]):
            missing.append("%s %s — nog niet gebouwd" % (course, folder))
            continue
        found_any = False
        for src, dst in spec["files"]:
            sp = p(src.format(n=n))
            if os.path.exists(sp):
                entries.append((sp, "%s/%s" % (folder, dst.format(n=n))))
                found_any = True
            else:
                missing.append(src.format(n=n))
        for gpat, sub in spec["globs"]:
            for sp in sorted(glob.glob(p(gpat.format(n=n)))):
                base = os.path.basename(sp)
                # de hub zelf zit al bij "files" — niet dubbel opnemen
                if base.endswith("_hub.html"):
                    continue
                entries.append((sp, "%s/%s%s" % (folder, sub, base)))
                found_any = True
        if not found_any:
            missing.append("%s %s: geen enkel bestand gevonden" % (course, folder))
    return entries, missing


def manifest(course, units, entries, missing, stamp):
    spec = COURSES[course]
    per_unit = {}
    for _, dst in entries:
        u = dst.split("/")[0]
        per_unit.setdefault(u, []).append(dst.split("/", 1)[1])
    lines = [
        "# %s — leverings-zip" % spec["label"], "",
        "**Gebouwd op:** %s" % stamp,
        "**Units in deze zip:** %s" % ", ".join(sorted(per_unit, key=lambda u: int(u[1:]))),
        "**Bestanden:** %d" % len(entries), "",
        "> Deze zip is een **momentopname** van de bestanden op het moment hierboven.",
        "> Wordt een hub, PDF of PowerPoint later opnieuw gegenereerd, maak dan een",
        "> nieuwe zip met `python3 03-build/make_zip.py %s`." % course, "",
        "## Inhoud per unit", "",
    ]
    for u in sorted(per_unit, key=lambda x: int(x[1:])):
        lines.append("**%s**" % u)
        for f in sorted(per_unit[u]):
            lines.append("- `%s`" % f)
        lines.append("")
    if missing:
        lines += ["## Ontbrekende bestanden (niet in de zip)", ""]
        lines += ["- `%s`" % m for m in missing] + [""]
    lines += [
        "## De formaten", "",
        "| Bestand | Wat |",
        "|---|---|",
        "| `*.pdf` | print-klaar, om af te drukken |",
        "| `*_BEWERKBAAR.html` | dezelfde cursus, wél bewerkbaar (open in de browser, pas aan, «Opslaan als PDF») |",
        "| `*_hub.html` | de digitale pagina: audio, flip cards, oefeningen en de motor-spellen — werkt offline |",
        "| `*_docente.pptx` | PowerPoint voor de klas (met oplossingen) |",
        "| `*_alumno.pptx` | leerlingversie (F5 voor de diavoorstelling) |",
        "",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Bouwt een leverings-zip van een cursus uit de huidige bestanden.")
    ap.add_argument("course", help="C4 | C5 | C6+")
    ap.add_argument("--units", nargs="*", type=int, help="alleen deze units (standaard: alle)")
    ap.add_argument("--out", help="pad van de zip (standaard: 03-build/<cursus>_<datum>.zip)")
    a = ap.parse_args()

    course = ALIAS.get(a.course, a.course)
    if course not in COURSES:
        sys.exit("Onbekende cursus %r — kies uit: %s" % (a.course, ", ".join(COURSES)))

    units = a.units if a.units else list(COURSES[course]["units"])
    entries, missing = collect(course, units)
    if not entries:
        sys.exit("Geen bestanden gevonden voor %s — niets om te zippen." % course)

    now = datetime.datetime.now()
    stamp = now.strftime("%d/%m/%Y %H:%M")
    slug = course.replace("+", "plus")
    out = a.out or p("03-build", "%s_levering_%s.zip" % (slug, now.strftime("%Y-%m-%d")))

    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for src, dst in entries:
            z.write(src, dst)
        z.writestr("MANIFEST.md", manifest(course, units, entries, missing, stamp))

    mb = os.path.getsize(out) / 1048576.0
    print("✓ %s" % out)
    print("  %d bestanden · %.1f MB · gebouwd %s" % (len(entries) + 1, mb, stamp))
    if missing:
        print("  ⚠ %d ontbrekend (zie MANIFEST.md):" % len(missing))
        for m in missing[:8]:
            print("      - %s" % m)
        if len(missing) > 8:
            print("      … en %d meer" % (len(missing) - 8))


if __name__ == "__main__":
    main()
