#!/usr/bin/env python3
"""Zet de retos van C5 U0 op hun plaats in de printcursus.

Zelfde afspraak als `add_bloques_u0.py`: in de cursuslaag wordt **alleen
toegevoegd, nooit weggelaten**. Bestaande secties, oefeningen en nummering
blijven ongemoeid.

Waar komt wat? Niet achteraan op een hoop, maar in de sectie waar de reto
inhoudelijk thuishoort — een spellingsreto hoort bij §1, een accentreto bij §2.
Elke reto wordt daarom ingevoegd vlak vóór de sectie die erop volgt:

    §1 alfabeto/sonidos   → retos 6, 9, 2, 4   (ingevoegd vóór §2)
    §2 acento             → reto 5             (ingevoegd vóór §3)
    §3 números            → retos 3, 8         (ingevoegd vóór §4)
    §4 saludos            → retos 1, 10        (ingevoegd vóór het ronde-1-blok)
    Cultura A.2           → reto 7             (idem, sluit aan bij de wereldkaart)

De drie retos met soporte="print" komen er voluit in staan, mét schrijfruimte.
De zeven andere krijgen een verwijskaartje van vier regels: wat het is, wat de
beperking is, en waar het staat. Een veiling of een opnameoefening half op
papier zetten helpt niemand.

Herhaalbaar: het script herkent zijn eigen markeringen en vervangt dan het
eerder ingevoegde blok in plaats van er een tweede bij te zetten.
"""
import os
import re
import sys

ROOT = "/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
import retos_data as RD          # noqa: E402
import retos_print as RP         # noqa: E402

DOEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "U0.html")
MARCA = "<!-- ===== retos · %s (%s) ===== -->"

# Per invoegpunt: (welke retos, titel van het blok, het anker waarvóór het komt).
# Het anker is een letterlijk stukje van de bestaande cursus; de retos komen er
# vlak vóór, zodat ze nog binnen hun eigen sectie vallen.
BLOQUES = [
    ("sonidos", [6, 9, 2, 4], "§1.4 · Retos — el sonido puesto a prueba",
     'Ya sabes reconocer los sonidos. Ahora los vas a <b>usar bajo presión</b>: en un '
     'concurso, en una subasta y en una investigación.',
     'Je kunt de klanken herkennen. Nu ga je ze gebruiken onder druk: in een spelshow, '
     'op een veiling en in een onderzoek.'),
    ("acento", [5], "§2.4 · Reto — el acento en movimiento",
     'La tilde no se aprende sentado. Este reto se juega <b>de pie</b>.',
     'De klemtoon leer je niet zittend. Deze reto speel je rechtstaand.'),
    ("numeros", [3, 8], "§3.5 · Retos — los números en el mundo real",
     'Los números sirven para algo: para <b>llegar</b> a un sitio y para <b>llamar</b> '
     'a alguien. Aquí los usas de verdad.',
     'Getallen dienen ergens toe: om ergens te geráken en om iemand te béllen. '
     'Hier gebruik je ze echt.'),
    ("saludos", [1, 10, 7], "§4.4 · Retos — hablar sin saber todavía",
     'Todavía sabes pocas palabras. Estos tres retos demuestran que ya puedes '
     '<b>comunicar</b> igualmente.',
     'Je kent nog weinig woorden. Deze drie retos bewijzen dat je nu al kunt communiceren.'),
]

# Waarvóór elk blok komt te staan. Voor de secties nemen we de sectiekop als
# herkenningspunt en schuiven we terug naar het begin van diens bladzijde: zo
# valt het retoblok binnen de vórige sectie en blijft de regel «elke hoofdsectie
# begint op een nieuwe bladzijde» (§14) overeind.
ANCLAS_PK = {
    "sonidos": "§2 · Taller de lengua",
    "acento": "§3 · Números",
    "numeros": "§4 · Saludos",
}
ANCLA_LITERAL = {
    "saludos": "<!-- ===== ronde 1 · toegevoegde blokken (begin) ===== -->",
}


def punto_de_insercion(doc, clave):
    """Het teken waarvóór het blok komt — begin van de bladzijde van die sectie."""
    if clave in ANCLA_LITERAL:
        i = doc.find(ANCLA_LITERAL[clave])
        return i if i >= 0 else None
    marca = '<span class="pk">%s' % ANCLAS_PK[clave]
    i = doc.find(marca)
    if i < 0:
        return None
    inicio = doc.rfind('<div class="page">', 0, i)
    return inicio if inicio >= 0 else i


def bloque_html(clave, nums, titulo, intro_es, intro_nl):
    # per unit lopen de nummers van 1 tot 10, dus zonder deze afbakening
    # zou U0 de retos van U1 oppikken
    retos = {r["num"]: r for r in RD.de("C5", 0)}
    p = ['<div class="page">',
         '<div class="divider">%s</div>' % titulo,
         '<div class="intro" style="margin-top:1mm"><b>ES:</b> %s '
         '<span class="gloss">%s</span></div>' % (intro_es, intro_nl)]
    for n in nums:
        r = retos[n]
        p.append(RP.reto_print(r) if r["soporte"] == "print" else RP.reto_puntero(r))
    p.append('</div>')
    return MARCA % (clave, "begin") + "\n".join(p) + MARCA % (clave, "einde")


def css_erbij(doc):
    """De reto-CSS één keer aan de bestaande <style> hangen."""
    if ".regla-reto{" in doc:
        return doc
    i = doc.rindex("</style>")
    return doc[:i] + RP.CSS + doc[i:]


def main():
    doc = open(DOEL, encoding="utf-8").read()
    doc = css_erbij(doc)

    for clave, nums, titulo, i_es, i_nl in BLOQUES:
        nuevo = bloque_html(clave, nums, titulo, i_es, i_nl)
        patron = re.compile(re.escape(MARCA % (clave, "begin")) + ".*?"
                            + re.escape(MARCA % (clave, "einde")), re.S)
        if patron.search(doc):
            doc = patron.sub(lambda _m: nuevo, doc)      # herbouw, geen tweede kopie
            actie = "vervangen"
        else:
            i = punto_de_insercion(doc, clave)
            if i is None:
                sys.exit("Invoegpunt niet gevonden voor «%s»" % clave)
            doc = doc[:i] + nuevo + "\n" + doc[i:]
            actie = "ingevoegd"
        print("  %-10s %-10s retos %s" % (clave, actie, nums))

    open(DOEL, "w", encoding="utf-8").write(doc)
    print("U0.html bijgewerkt: %d KB" % (len(doc) / 1024))


if __name__ == "__main__":
    main()
