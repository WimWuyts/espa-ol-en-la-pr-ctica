#!/usr/bin/env python3
"""Vergelijkt de huidige hubs met de baseline — vangnet voor de oefeningen-sweep.

Waarom: de sweep raakt 17 hub-generators. Een hub opnieuw genereren duurt seconden,
dus «herbouwen» is goedkoop; het risico is **stille regressie** — een spel of een
oefenblok dat verdwijnt zonder dat iemand het merkt. Dat is in dit project al één
keer gebeurd (17 gebouwde spellen stonden in géén hub).

Draai dit na elke stap van de sweep:

    python3 03-build/check_regressie.py              # vergelijk met de baseline
    python3 03-build/check_regressie.py --herijk     # nieuwe baseline vastleggen
                                                     # (alleen ná goedgekeurde wijziging)

Uitgangspunt: er mag van alles BIJ komen, er mag niets WEG.
"""
import argparse, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "03-build", ".baseline", "hubs_voor_sweep.json")

HUBS = ([("C5 U%d" % u, "03-build/web/U%d_web.html" % u) for u in range(9)] +
        [("C6+ U%d" % u, "03-build/web/C6plus_U%d_web.html" % u) for u in range(8)])


def scan(path):
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        return None
    h = open(full, encoding="utf8", errors="ignore").read()
    m = re.search(r'const MOTOR=(\[.*?\]);\n', h, re.S)
    motor = json.loads(m.group(1)) if m else []
    slugs = sorted(g[0] for grp in motor for g in grp[1])
    builders = re.findall(r"\b(build[A-Z]\w+)\s*\(", h)
    return {
        "bestand": os.path.basename(path),
        "bytes": len(h),
        "spellen": len(slugs),
        "spel_slugs": slugs,
        "bouwers": {b: builders.count(b) for b in set(builders)},
        "oefenblokken": sorted(set(re.findall(r'id="((?:vx|gx)_[\w-]+)"', h))),
    }


def huidig():
    return {label: s for label, path in HUBS if (s := scan(path))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--herijk", action="store_true", help="leg de huidige stand vast als nieuwe baseline")
    a = ap.parse_args()
    now = huidig()

    if a.herijk or not os.path.exists(BASE):
        os.makedirs(os.path.dirname(BASE), exist_ok=True)
        json.dump(now, open(BASE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("Baseline vastgelegd voor %d hubs." % len(now))
        return 0

    old = json.load(open(BASE, encoding="utf-8"))
    problemen, groei = [], []

    for label in sorted(set(old) | set(now)):
        o, n = old.get(label), now.get(label)
        if o and not n:
            problemen.append("%s — HUB VERDWENEN" % label); continue
        if n and not o:
            groei.append("%s — nieuwe hub (%d spellen)" % (label, n["spellen"])); continue

        weg = sorted(set(o["spel_slugs"]) - set(n["spel_slugs"]))
        bij = sorted(set(n["spel_slugs"]) - set(o["spel_slugs"]))
        if weg:
            problemen.append("%s — spel(len) WEG: %s" % (label, ", ".join(weg)))
        if bij:
            groei.append("%s — spel(len) erbij: %s" % (label, ", ".join(bij)))

        blok_weg = sorted(set(o["oefenblokken"]) - set(n["oefenblokken"]))
        blok_bij = sorted(set(n["oefenblokken"]) - set(o["oefenblokken"]))
        if blok_weg:
            problemen.append("%s — oefenblok(ken) WEG: %s" % (label, ", ".join(blok_weg)))
        if blok_bij:
            groei.append("%s — oefenblok(ken) erbij: %s" % (label, ", ".join(blok_bij)))

        for b, cnt in o["bouwers"].items():
            nu = n["bouwers"].get(b, 0)
            if nu < cnt:
                problemen.append("%s — %s: %d → %d (minder)" % (label, b, cnt, nu))

        if n["bytes"] < o["bytes"] * 0.85:
            problemen.append("%s — bestand %d%% kleiner (%d → %d bytes)"
                             % (label, round((1 - n["bytes"] / o["bytes"]) * 100), o["bytes"], n["bytes"]))

    if groei:
        print("Toegevoegd (%d):" % len(groei))
        for g in groei[:40]:
            print("   + " + g)
        if len(groei) > 40:
            print("   … en %d meer" % (len(groei) - 40))
        print()
    if problemen:
        print("REGRESSIE (%d):" % len(problemen))
        for p in problemen:
            print("   ✗ " + p)
        print("\nNiets verwijderen is de regel. Herstel dit, of leg een bewuste wijziging")
        print("vast met --herijk nadat de auteur ze heeft goedgekeurd.")
        return 1
    print("Geen regressie: alles uit de baseline is er nog (%d hubs gecontroleerd)." % len(now))
    return 0


if __name__ == "__main__":
    sys.exit(main())
