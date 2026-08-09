#!/usr/bin/env python3
"""Bakt de luisterfragmenten in de digitale pagina's van C5 en C6+.

WAAROM
Er zijn twee manieren om een webpagina geluid te geven: het geluid staat ín het
bestand, of het staat in een map ernaast waar de pagina naar verwijst. C4 deed
het eerste, C5 en C6+ het tweede.

Dat tweede heeft twee zwakke plekken. De map móét mee geüpload worden en op de
juiste plaats belanden — vergeet dat, en elke luisteroefening valt stil zonder
dat iemand het merkt tot een leerling het meldt. En een leerling die de pagina
bewaart om thuis te werken, houdt een pagina zonder geluid over.

Ingebakken lost allebei op: één bestand per unit, dat overal werkt.

WAAROM HET NU PAS KAN
Met de onbewerkte WAV's was het onbetaalbaar: C5 U0 alleen al zou een pagina van
34 MB worden. Sinds `wav_a_mp3.js` de fragmenten vijf keer kleiner maakt, komen
zestien van de zeventien units uit rond 2,5 tot 3,3 MB. C5 U0 blijft de
uitzondering — tien fragmenten, negen minuten — en landt rond 8 MB.

WAAROM ALS NABEWERKING
Zelfde reden als `bladspiegel.py` en `print_iconos.py`: het zijn zeventien
generatoren, en één plek is te overzien. Bovendien werkt dit op wat er écht in
de gebouwde pagina staat, niet op wat een generator dénkt te schrijven.

Herhaalbaar: een pad dat al een data-URL is, wordt overgeslagen.

    python3 03-build/web/hub_audio.py            # alle hubs
    python3 03-build/web/hub_audio.py --contar   # alleen tellen, niets wijzigen
"""
import base64
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import enlaces as EN          # noqa: E402

# «audio/C5_U5.mp3» zoals het in de gebouwde pagina staat, binnen een JS-string.
RUTA = re.compile(r'audio/([A-Za-z0-9_]+)\.(mp3|wav)')

MIME = {"mp3": "audio/mpeg", "wav": "audio/wav"}


def datos(nombre, ext):
    """De opname als data-URL. MP3 heeft voorrang: die is vijf keer kleiner."""
    for e in ("mp3", ext):
        p = os.path.join(AQUI, "audio", "%s.%s" % (nombre, e))
        if os.path.exists(p):
            return ("data:%s;base64,%s"
                    % (MIME[e], base64.b64encode(open(p, "rb").read()).decode()),
                    os.path.getsize(p), e)
    return None, 0, None


def procesar(ruta, contar=False):
    doc = open(ruta, encoding="utf-8").read()
    puestos, faltan, bytes_audio = [], [], 0

    def sustituir(m):
        nonlocal bytes_audio
        url, tam, ext = datos(m.group(1), m.group(2))
        if url is None:
            faltan.append(m.group(0))
            return m.group(0)
        puestos.append(m.group(1))
        bytes_audio += tam
        return m.group(0) if contar else url

    nuevo = RUTA.sub(sustituir, doc)
    if not contar and nuevo != doc:
        open(ruta, "w", encoding="utf-8").write(nuevo)
    return puestos, faltan, len(nuevo), bytes_audio


def main():
    contar = "--contar" in sys.argv
    tot_f = tot_falta = 0
    print("%-14s %5s %10s %10s" % ("unit", "frag", "pagina", "waarvan audio"))
    for curso, u, _impreso, hub in EN.unidades(("C5", "C6+")):
        if not os.path.exists(hub):
            continue
        puestos, faltan, largo, audio = procesar(hub, contar=contar)
        tot_f += len(puestos)
        tot_falta += len(faltan)
        aviso = ""
        if faltan:
            aviso = "  ← %d opname(s) niet gevonden: %s" % (
                len(faltan), ", ".join(faltan[:3]))
        print("%-4s U%-8d %5d %7.1f MB %7.1f MB%s"
              % (curso, u, len(puestos), largo / 1e6, audio * 4 / 3 / 1e6, aviso))
    print("\n%d fragmenten ingebakken%s%s"
          % (tot_f, " (niets weggeschreven)" if contar else "",
             (" · %d ontbraken" % tot_falta) if tot_falta else ""))
    if tot_falta:
        sys.exit(1)


if __name__ == "__main__":
    main()
