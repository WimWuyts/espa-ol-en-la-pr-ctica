#!/usr/bin/env python3
"""Canonieke inhoud van de blueprint-oefeningen (`00-brondocumenten/gap-analyse/`).

Eén bron voor beide dragers: de hub-generator maakt er een zelfcorrigerende
oefening van, de printgenerator een oefening met antwoordruimte. Zo kunnen de
twee niet uit elkaar lopen.

De ID's uit de blueprints worden ongewijzigd overgenomen — ze zijn het anker
tussen print, PDF, hub en de QR-balkjes. Het itemaantal staat er expliciet bij
(`aantal`) zodat de generator er een `console.assert` op kan zetten en de
blueprint-eis «exact N» meetbaar is in plaats van hoopvol.

CORRECTIES op de canonieke inhoud, goedgekeurd door de auteur
(BOUWPLAN_SWEEP.md fase 2). Ze staan hier bij het item zelf, zodat ze niet
opnieuw kunnen wegglippen wanneer die unit later gebouwd wordt:

  1. C5-U3-NAT-01 item 12   `ponerse de pie` stond als «no reflexivo», maar
                            *ponerse* IS pronominaal -> vervangen door `desayunar`.
  2. C6+ 5.9 item 15        het antwoord stond letterlijk verderop in de zin
                            -> tweede helft herschreven.
  3. C6+ 5.10 item 25       cue `compartirlo` bevatte het pronomen al
                            -> cue wordt `compartir`.
  4. C5-U5/U6-NAT-01        woordgroepen blijven klikoefening, niet getypt.
  5. C5-U1-NAT-01           20 nationaliteiten -> accents='soft'.
  6. C5-U4-NAT-01           twee dropdowns waren selecteren -> buildType.

Correcties 1-6 raken units die in ronde 2 en later gebouwd worden; ze zijn hier
al vastgelegd zodat die ronden ze niet opnieuw hoeven te ontdekken.
"""

# ---------------------------------------------------------------------------
# C5 · U0 — Los números
# ---------------------------------------------------------------------------

_NUM_0_10 = [("0", "cero"), ("1", "uno"), ("2", "dos"), ("3", "tres"), ("4", "cuatro"),
             ("5", "cinco"), ("6", "seis"), ("7", "siete"), ("8", "ocho"),
             ("9", "nueve"), ("10", "diez")]

_NUM_10_20 = [("diez", "10"), ("once", "11"), ("doce", "12"), ("trece", "13"),
              ("catorce", "14"), ("quince", "15"), ("dieciséis", "16"),
              ("diecisiete", "17"), ("dieciocho", "18"), ("diecinueve", "19"),
              ("veinte", "20")]


def _afleiders(correcto, alle, n=3):
    """Drie afleiders uit dezelfde set — de blueprint eist expliciet dat de
    afleiders uit de eigen reeks komen, niet uit een willekeurige woordenbak.

    Vaste offsets (-4, +1, +6) in plaats van de naaste buren: met een venster van
    buren krijgen item 1, 2 en 3 exact dezelfde vier opties, en dan kan de
    leerling het patroon spelen in plaats van het getal te lezen. Zo krijgt elk
    item een eigen optieset, met één naaste buur erin om echt te moeten
    onderscheiden. De offsets hebben bewust wisselend teken: met alleen positieve
    offsets is het juiste antwoord binnen elk item altijd het laagste getal, en
    dan wint gokken het van lezen."""
    i, m = alle.index(correcto), len(alle)
    return [alle[(i + d) % m] for d in (-4, 1, 6)][:n]


C5_U0_NAT_01 = {
    "id": "C5-U0-NAT-01",
    "ancla": "c5-u0-nat-01",
    "titulo": "Los números del 0 al 10",
    "instruccion_es": "Elige la palabra correcta para cada número.",
    "instruccion_nl": "Kies bij elk cijfer het juiste woord.",
    "aantal": 11,
    "feedback_fout": "Mira otra vez la forma escrita del número.",
    "items": [
        {"q": cifra, "ans": palabra,
         "opts": sorted([palabra] + _afleiders(palabra, [p for _, p in _NUM_0_10])),
         "why": "%s = %s" % (cifra, palabra)}
        for cifra, palabra in _NUM_0_10
    ],
}

C5_U0_NAT_02 = {
    "id": "C5-U0-NAT-02",
    "ancla": "c5-u0-nat-02",
    "titulo": "Los números del 10 al 20",
    "instruccion_es": "Escucha o lee el número y elige la cifra correcta.",
    "instruccion_nl": "Luister of lees het getalwoord en kies het juiste cijfer.",
    "aantal": 11,
    "feedback_fout": "Vergelijk de vorm: dieciséis draagt een tilde, diecisiete niet.",
    "items": [
        {"q": palabra, "say": palabra, "ans": cifra,
         "opts": sorted([cifra] + _afleiders(cifra, [c for _, c in _NUM_10_20]), key=int),
         "why": "%s = %s" % (palabra, cifra)}
        for palabra, cifra in _NUM_10_20
    ],
}

# ---------------------------------------------------------------------------
# C6+ · U0 — Países y nacionalidades (blueprint 5.1)
# ---------------------------------------------------------------------------

C6P_U0_NAC = {
    "id": "c6p-u0-nationalities-20",
    "ancla": "c6p-u0-nationalities-20",
    "titulo": "Países y nacionalidades",
    "instruccion_es": "Relaciona cada país con la nacionalidad correcta.",
    "instruccion_nl": "Koppel elk land aan de juiste nationaliteit.",
    "aantal": 20,
    "modelo": "Soy de Perú. Soy peruana / peruano.",
    "pares": [
        ("España", "español / española"),
        ("México", "mexicano / mexicana"),
        ("Guatemala", "guatemalteco / guatemalteca"),
        ("Honduras", "hondureño / hondureña"),
        ("El Salvador", "salvadoreño / salvadoreña"),
        ("Nicaragua", "nicaragüense"),
        ("Costa Rica", "costarricense"),
        ("Panamá", "panameño / panameña"),
        ("Cuba", "cubano / cubana"),
        ("República Dominicana", "dominicano / dominicana"),
        ("Puerto Rico", "puertorriqueño / puertorriqueña"),
        ("Colombia", "colombiano / colombiana"),
        ("Venezuela", "venezolano / venezolana"),
        ("Ecuador", "ecuatoriano / ecuatoriana"),
        ("Perú", "peruano / peruana"),
        ("Bolivia", "boliviano / boliviana"),
        ("Paraguay", "paraguayo / paraguaya"),
        ("Chile", "chileno / chilena"),
        ("Argentina", "argentino / argentina"),
        ("Uruguay", "uruguayo / uruguaya"),
    ],
}

# De getypte tweelingversie: dezelfde twintig, maar nu produceren in plaats van
# koppelen. Correctie 5 van de auteur geldt hier al: woordenschat -> 'soft',
# zodat puertorriqueño en nicaragüense niet op één accent stranden. De correctie
# toont daarna wél de juiste schrijfwijze.
C6P_U0_NAC_TYPE = {
    "id": "c6p-u0-nationalities-20-type",
    "ancla": "c6p-u0-nationalities-20-type",
    # De getypte versie oefent dezelfde twintig als de koppelversie en deelt dus
    # het QR-balkje; er is maar één externe oefenpagina voor dit onderwerp.
    "qr_id": "c6p-u0-nationalities-20",
    "titulo": "Países y nacionalidades — escríbelas",
    "instruccion_nl": "Typ de mannelijke vorm van de nationaliteit.",
    "aantal": 20,
    "accents": "soft",
    "items": [
        {"q": "%s → Soy ___" % pais,
         "ans": nac.split(" / ")[0],
         "hint": nac.split(" / ")[0][:2] + "_" * (len(nac.split(" / ")[0]) - 2),
         "why": nac}
        for pais, nac in C6P_U0_NAC["pares"]
    ],
}


def assert_aantallen():
    """Zelfcontrole bij import — de blueprints eisen exacte aantallen."""
    for bloque in (C5_U0_NAT_01, C5_U0_NAT_02, C6P_U0_NAC_TYPE):
        n = len(bloque["items"])
        assert n == bloque["aantal"], "%s: %d items, verwacht %d" % (bloque["id"], n, bloque["aantal"])
    assert len(C6P_U0_NAC["pares"]) == C6P_U0_NAC["aantal"], C6P_U0_NAC["id"]
    # afleiders: vier opties, correcte erbij, geen duplicaten
    for bloque in (C5_U0_NAT_01, C5_U0_NAT_02):
        for it in bloque["items"]:
            assert len(it["opts"]) == 4, (bloque["id"], it["q"], it["opts"])
            assert len(set(it["opts"])) == 4, (bloque["id"], it["q"], it["opts"])
            assert it["ans"] in it["opts"], (bloque["id"], it["q"])


assert_aantallen()
