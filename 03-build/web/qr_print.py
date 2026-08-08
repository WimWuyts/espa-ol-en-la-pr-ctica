#!/usr/bin/env python3
"""De QR-kaart in het boek, met een adres dat écht ergens uitkomt.

Tot nu tekenden de generatoren een nep-code: willekeurige blokjes in de vorm van
een QR. Dit bestand vervangt die door een echte code (zie `qr_codigo.py`) en —
belangrijker — zoekt zélf uit waar de code heen moet.

HOE HET DOEL GEVONDEN WORDT
De aanroep in de cursus ziet er zo uit:

    qr("Escanea y escucha", "Audio 2.1 · Ser · 0:45", seed=21)

Die tweede string is het etiket van de luisteroefening, en datzelfde etiket staat
letterlijk in `escucha_corta_data.py`. Daar hangt een anker aan. De code komt dus
uit op precies dat fragment op de hub, niet op de startpagina. Lukt de match
niet, dan valt hij terug op het luisterpaneel of — bij een opnametaak — op het
spreekpaneel, en dat meldt `informe()` zodat het niet stilletjes misgaat.

Elke generator zet één keer bovenaan:

    import qr_print as QRP; QRP.fijar("C5", 1)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import enlaces as EN          # noqa: E402

_ACTUAL = {"curso": "C5", "unidad": 0}
_INFORME = []                 # wat er gematcht is, en wat niet


def fijar(curso, unidad):
    """Zeg voor welke unit deze generator draait."""
    _ACTUAL["curso"] = curso
    _ACTUAL["unidad"] = int(unidad)
    _INFORME.clear()


def _cortos():
    import escucha_corta_data as EC
    return EC.CORTOS.get((_ACTUAL["curso"], _ACTUAL["unidad"]), [])


def destino_de(lab, meta):
    """(adres, hoe gevonden) voor één QR-kaart."""
    curso, unidad = _ACTUAL["curso"], _ACTUAL["unidad"]

    # 1 · exacte match op het etiket van een korte audiotaak
    for f in _cortos():
        if f["etiqueta"] == meta:
            return EN.url(curso, unidad, f["ancla"]), "audio: " + f["id"]

    # 2 · een opnametaak wijst naar het spreekpaneel
    texto = (lab + " " + meta).lower()
    if "graba" in texto or "grabar" in texto:
        return EN.url(curso, unidad, EN.ancla_panel("hablar")), "spreekpaneel"

    # 3 · het lange luisterfragment
    if "escucha" in texto or "audio" in texto or "canción" in texto:
        return EN.url(curso, unidad, EN.ancla_audio_largo(curso, unidad)), "lang fragment"

    # 4 · anders: het luisterpaneel, en dat melden we
    return EN.url(curso, unidad, EN.ancla_panel("escuchar")), "GEEN MATCH"


def qr(lab, meta, seed=0, ancla=None):
    """De QR-kaart. `seed` blijft in de handtekening staan omdat de zeventien
    generatoren hem meegeven; hij doet niets meer — een echte code heeft geen
    toeval nodig."""
    if ancla:
        destino, hoe = EN.url(_ACTUAL["curso"], _ACTUAL["unidad"], ancla), "handmatig"
    else:
        destino, hoe = destino_de(lab, meta)
    _INFORME.append((lab, meta, destino, hoe))
    return EN.tarjeta_qr(destino, lab, meta)


def informe():
    """Wat deze generator aan codes gelegd heeft — voor de bouwcontrole."""
    return list(_INFORME)


def resumen():
    """Eén regel per code, met een sterretje bij wat niet gematcht kon worden."""
    out = []
    for lab, meta, destino, hoe in _INFORME:
        marca = "  " if hoe != "GEEN MATCH" else "! "
        out.append("%s%-22s %-42s %s" % (marca, lab, meta[:42], hoe))
    return "\n".join(out)
