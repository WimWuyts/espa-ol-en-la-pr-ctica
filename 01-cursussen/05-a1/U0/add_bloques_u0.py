#!/usr/bin/env python3
"""Voegt de nieuwe blokken van ronde 1 toe aan de printcursus van C5 U0.

C5 U0 heeft geen printgenerator: `U0.html` is met de hand samengesteld (de
golden sample). Dit script vult die aan in plaats van hem te vervangen, want de
afspraak is bindend: in de cursuslaag wordt **alleen toegevoegd, nooit
weggelaten**. Bestaande secties, oefeningen en nummering blijven ongemoeid; de
nieuwe oefeningen krijgen een eigen subsectienummer erachter.

Wat erbij komt, elk op een eigen bladzijde (§14: elke hoofdsectie begint op een
nieuwe bladzijde):
  §3.4  Los números — de twee blueprint-reeksen, met echte QR-balkjes;
  §5    Lectura — «El Club de Español», volledige leesroute;
  §6    Escucha — «En la puerta de embarque», zes treden.

De inhoud komt uit dezelfde bron als de hub (`nat_data`, `lectura_data`,
`escucha_data`), zodat papier en scherm niet uit elkaar kunnen lopen.

Het script is herhaalbaar: het herkent zijn eigen markering en vervangt dan het
eerder ingevoegde blok in plaats van er een tweede bij te zetten.
"""
import os
import re
import sys

ROOT = "/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
import print_bloques as PB           # noqa: E402
import nat_data, lectura_data, escucha_data   # noqa: E402

DOEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "U0.html")
INICIO = "<!-- ===== ronde 1 · toegevoegde blokken (begin) ===== -->"
FIN = "<!-- ===== ronde 1 · toegevoegde blokken (einde) ===== -->"


def bloques():
    n = 51   # de bestaande cursus telt vijftig activiteiten; hier gaat de rij verder
    p = []
    p.append('<div class="page">')
    p.append('<div class="divider">§3.4 · Los números — series completas</div>')
    p.append('<h3 style="font-size:14pt;color:var(--gd)">§3.4 · Los números — de volledige reeksen</h3>')
    p.append('<div class="intro" style="margin-top:1mm">Ya sabes contar. Ahora <b>escribe</b> los números, '
             'sin mirar. <span class="gloss">Je kunt al tellen. Nu schrijf je de getallen zelf op, zonder te '
             'spieken — schrijven is iets anders dan herkennen.</span></div>')
    p.append(PB.nat_print(nat_data.C5_U0_NAT_01, n,
                          opgave_tekst="Escribe la palabra que corresponde a cada cifra.",
                          klasse="wl md", per_rij=3))
    p.append(PB.nat_print(nat_data.C5_U0_NAT_02, n + 1,
                          opgave_tekst="Lee el número y escribe la cifra.",
                          klasse="wl sm", per_rij=6))
    p.append('</div>')

    p.append('<div class="page">')
    p.append('<div class="divider">§5 · Lectura</div>')
    p.append('<h3 style="font-size:14pt;color:var(--gd)">§5 · Lectura — «El Club de Español»</h3>')
    p.append('<div class="intro" style="margin-top:1mm">Un cartel de verdad, del pasillo del instituto. '
             '<b>No hace falta entenderlo todo</b> para sacar la información. '
             '<span class="gloss">Een echt aanplakbiljet uit de gang. Je hoeft niet alles te begrijpen om de '
             'informatie eruit te halen — dat is precies wat lezen is.</span></div>')
    p.append(PB.lectura_print(lectura_data.C5_U0, n + 2))
    p.append('</div>')

    p.append('<div class="page">')
    p.append('<div class="divider">§6 · Escucha</div>')
    p.append('<h3 style="font-size:14pt;color:var(--gd)">§6 · Escucha — «En la puerta de embarque»</h3>')
    p.append('<div class="intro" style="margin-top:1mm">Lucía y tú esperáis el mismo vuelo. '
             '<b>Escucha primero, escribe después.</b> '
             '<span class="gloss">Lucía en jij wachten op dezelfde vlucht. Eerst luisteren, dan pas schrijven; '
             'het transcript staat online en gaat pas open ná de taken.</span></div>')
    p.append(PB.escucha_print(escucha_data.C5_U0, n + 3))
    p.append('</div>')
    return "\n".join(p)


def main():
    s = open(DOEL, encoding="utf-8").read()

    # de eigen stijlregels één keer meenemen
    if ".qb{display:flex" not in s:
        s = s.replace("</style>", PB.CSS + "\n</style>", 1)

    nieuw = INICIO + "\n" + bloques() + "\n" + FIN + "\n"
    if INICIO in s:
        s = re.sub(re.escape(INICIO) + r".*?" + re.escape(FIN) + r"\n?", nieuw, s, flags=re.S)
        actie = "vervangen"
    else:
        # vóór de Cultura-bladzijde: de nieuwe secties horen bij de leerstof,
        # Cultura en de Tarea sluiten de unit af
        anker = "<!-- ===== cultura ===== -->"
        assert anker in s, "ankerpunt voor Cultura niet gevonden"
        s = s.replace(anker, nieuw + anker, 1)
        actie = "toegevoegd"

    open(DOEL, "w", encoding="utf-8").write(s)
    acts = s.count('<div class="act">')
    print("U0.html %s · %d activiteiten · %d bytes" % (actie, acts, len(s)))


if __name__ == "__main__":
    main()
