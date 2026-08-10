#!/usr/bin/env python3
"""Rekent alle rollenspellen na vóór ze in een cursus terechtkomen.

Een oefening die vastloopt is erger dan geen oefening: de leerling denkt dat
híj het fout doet. Deze controle vangt de fouten die je met het blote oog mist
in vijfhonderd regels data.

Wat er nagekeken wordt, en waarom:

  gaten        het aantal ___ in het kader moet gelijk zijn aan het aantal
               antwoordlijsten én aan het aantal uitleg-teksten, anders krijgt
               een gat geen beoordeling of een uitleg geen gat
  bank         elk juist antwoord moet in de woordbank staan — staat het er
               niet, dan zoekt de leerling zich blind
  model        het modelantwoord moet zijn eigen patroon halen, anders keurt de
               oefening haar eigen voorbeeld af
  juist        elk als juist gemarkeerd keuze-antwoord moet er ook doorkomen
  fout         elk fout keuze-antwoord moet uitleg hebben (anders leert de
               leerling niets van zijn misser)
  corrector    de goede antwoorden mogen géén corrector-regel doen afgaan —
               vals alarm op je eigen modelzin is het ergste wat er is
  regex        alle patronen moeten geldig zijn
  invullen     **de belangrijkste.** Vul het kader in met het eerste (canonieke)
               antwoord van elk gat: dat moet létterlijk het modelantwoord
               opleveren. Anders klopt de oefening niet met wat «muéstrame»
               toont, en in het ergste geval levert ze een onmogelijke zin op.
               Zo kwam «una botella ___ agua» aan het licht: twee gaten, maar
               het woordje *de* stond nergens, dus het juiste antwoord viel
               niet in te vullen. Twaalf kaders bleken zo scheef te staan.

    python3 rol_check.py
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import corrector_data as CD                # noqa: E402
import rol_data as RD                      # noqa: E402


def normaliza(s):
    import unicodedata
    s = unicodedata.normalize("NFD", (s or "").lower())
    return re.sub(r"\s+", " ", "".join(c for c in s if not unicodedata.combining(c))).strip()


def _plano(s):
    """Alleen de woorden — leestekens en hoofdletters doen er niet toe."""
    return re.sub(r"[^a-z0-9 ]", "", normaliza(s))


def revisa(curso, unidad, r):
    fallos = []
    for i, p in enumerate(r["pasos"], 1):
        marca = "%s U%d beurt %d" % (curso, unidad, i)
        h = p.get("hueco")
        if not h:
            fallos.append("%s: geen invulkader" % marca)
        else:
            n = h["marco"].count("___")
            if not (n == len(h["respuestas"]) == len(h["mal"])):
                fallos.append("%s: %d gaten, %d antwoordlijsten, %d uitleggen"
                              % (marca, n, len(h["respuestas"]), len(h["mal"])))
            for j, alt in enumerate(h["respuestas"]):
                if not alt:
                    fallos.append("%s: gat %d heeft geen antwoord" % (marca, j + 1))
                elif not any(normaliza(a) in [normaliza(b) for b in h["banco"]]
                             for a in alt):
                    fallos.append("%s: gat %d — geen enkel antwoord (%s) staat in "
                                  "de bank" % (marca, j + 1, "/".join(alt)))
        # het ingevulde kader moet het modelantwoord zijn
        if h:
            lleno = h["marco"]
            for alt in h["respuestas"]:
                lleno = lleno.replace("___", alt[0] if alt else "?", 1)
            if _plano(lleno) != _plano(p["modelo"]):
                fallos.append("%s: het ingevulde kader geeft niet het model\n"
                              "        ingevuld: %s\n        model   : %s"
                              % (marca, lleno, p["modelo"]))
        for pat in p["acepta"]:
            try:
                re.compile(pat)
            except re.error as e:
                fallos.append("%s: ongeldig patroon %r (%s)" % (marca, pat, e))
        if not any(re.search(pat, normaliza(p["modelo"]), re.I) for pat in p["acepta"]):
            fallos.append("%s: het modelantwoord haalt geen enkel patroon" % marca)
        if not any(ok for _t, ok, _w in p["opciones"]):
            fallos.append("%s: geen juist keuze-antwoord" % marca)
        for t, ok, w in p["opciones"]:
            if ok and not any(re.search(pat, normaliza(t), re.I) for pat in p["acepta"]):
                fallos.append("%s: «%s» staat als juist maar haalt geen patroon"
                              % (marca, t[:40]))
            if not ok and not w:
                fallos.append("%s: «%s» is fout maar heeft geen uitleg" % (marca, t[:40]))
        # de corrector mag niet afgaan op wat wij zelf als juist aanbieden
        reglas = CD.reglas_para(curso, unidad)
        for texto in [p["modelo"]] + [t for t, ok, _w in p["opciones"] if ok]:
            for g in reglas:
                if re.search(g["re"], texto, re.I):
                    fallos.append("%s: corrector-regel «%s» gaat af op het juiste "
                                  "antwoord «%s»" % (marca, g["id"], texto[:40]))
    return fallos


def main():
    todos, malos = 0, []
    for (curso, unidad), r in sorted(RD.ROLES.items(), key=lambda x: (x[0][0], x[0][1])):
        todos += 1
        f = revisa(curso, unidad, r)
        malos += f
        print("%-4s U%-2d %-24s %d beurten · %s"
              % (curso, unidad, r["titulo"][:24], len(r["pasos"]),
                 "ok" if not f else "%d PROBLEEM" % len(f)))
    print("\n%d rollenspellen nagekeken" % todos)
    if malos:
        print("\n%d probleem(en):" % len(malos))
        for m in malos:
            print("   " + m)
        sys.exit(1)
    print("geen problemen")


if __name__ == "__main__":
    main()
