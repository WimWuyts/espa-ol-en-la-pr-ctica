#!/usr/bin/env python3
"""Vervangt de nep-QR's in de handgebouwde U0.html door echte, gerichte codes.

U0 is de enige unit zonder generator — ze is met de hand gebouwd en daarna met
`add_bloques_u0.py` en `add_retos_u0.py` aangevuld. Dit script doet voor de
QR-codes wat `qr_print.py` voor de zestien andere units doet: het zoekt per
kaart het juiste anker op de hub en tekent er een echte code voor.

Herhaalbaar: een kaart die al een echte code bevat, wordt overgeslagen.
"""
import os
import re
import sys

ROOT = "/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, os.path.join(ROOT, "03-build", "web"))

import enlaces as EN          # noqa: E402
import qr_print as QRP        # noqa: E402

DOEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "U0.html")

# Twee kaarten wijzen niet naar een audiofragment; die krijgen hun doel hier.
MANUAL = {
    "Página U0 · repaso · juegos": EN.ancla_panel("juegos"),
    "Audio V · Decks A–E · 5:00": EN.ancla_panel("vocab"),
}

# Matcht zowel de oorspronkelijke nep-kaart als een al vervangen kaart die nog
# geen `data-url` draagt, zodat het script ook na een eerdere ronde nog werkt.
PATRON = re.compile(
    r'<div class="qr">\s*<svg.*?</svg>\s*'
    r'<div class="lab">(?P<lab>.*?)</div><div class="meta">(?P<meta>.*?)</div></div>',
    re.S)


def escucha(doc):
    """Zet de code naar het lange fragment op de plaats van de tekstverwijzing.

    De zestien units met generator krijgen die kaart uit `print_bloques`; U0
    heeft geen generator, dus staat ze hier. Waarom ze er hoort: alle korte
    audiotaken hadden hun eigen code, maar «En la puerta de embarque» — de
    luistertaak van twintig minuten — had alleen de zin «zie de digitale
    pagina». Herhaalbaar: staat de code er al, dan gebeurt er niets.
    """
    import escucha_data as ED
    import print_bloques as PB
    if ED.C5_U0["ancla"] in doc:
        return doc, False
    patron = re.compile(
        r'<div class="qb"[^>]*>(?:(?!</div>\s*</div>).)*?het fragment beluisteren'
        r'.*?</span>\s*</div>', re.S)
    nuevo, n = patron.subn(lambda _m: PB._qr_escucha(ED.C5_U0), doc, count=1)
    return nuevo, bool(n)


def dictado(doc):
    """Zet de code naar het cijferdictee boven de oefening.

    «Dictado de números» stond in het boek met «la mochila lee un listado» en
    verder niets: wie thuis oefende had een luisteroefening zonder geluid. Het
    fragment bestaat nu (C5-U0-AUD-10); dit legt de code ernaartoe.
    """
    import escucha_corta_data as EC
    frag = [f for f in EC.CORTOS[("C5", 0)] if f["id"] == "C5-U0-AUD-10"][0]
    if frag["ancla"] in doc:
        return doc, False
    llamada = ('<div class="ic">🎧</div><div><b>Escanea y escribe.</b> El dictado está '
               'en la página digital: <b>1ª vez</b> la frase entera, <b>2ª vez</b> por '
               'trozos. <span class="gloss">Het dictee staat online: eerst de hele zin, '
               'dan in stukken.</span></div>')
    fila = ('<div class="audiorow"><div class="call">%s</div>%s</div>\n\n  '
            % (llamada, EN.tarjeta_qr(EN.url("C5", 0, frag["ancla"]),
                                      "Escanea y escucha", frag["etiqueta"])))
    i = doc.find("Dictado de números")
    if i < 0:
        return doc, False
    j = doc.rfind('<div class="act">', 0, i)
    if j < 0:
        return doc, False
    return doc[:j] + fila + doc[j:], True


def main():
    QRP.fijar("C5", 0)
    doc = open(DOEL, encoding="utf-8").read()
    if 'data-url=' in doc:
        doc, cambiado = escucha(doc)
        doc, cambiado2 = dictado(doc)
        cambiado = cambiado or cambiado2
        if cambiado:
            open(DOEL, "w", encoding="utf-8").write(doc)
            print("U0.html: codes naar het lange fragment en het cijferdictee gelegd")
        else:
            print("U0.html is al bijgewerkt — niets gedaan")
        return

    hechos = []

    def sustituir(m):
        lab, meta = m.group("lab"), m.group("meta")
        if meta in MANUAL:
            destino = EN.url("C5", 0, MANUAL[meta])
            hoe = "handmatig"
        else:
            destino, hoe = QRP.destino_de(lab, meta)
        hechos.append((lab, meta, destino.split("/")[-1], hoe))
        return EN.tarjeta_qr(destino, lab, meta)

    nuevo, n = PATRON.subn(sustituir, doc)
    if n == 0:
        sys.exit("geen QR-kaarten gevonden — is het patroon veranderd?")
    open(DOEL, "w", encoding="utf-8").write(nuevo)

    print("U0.html: %d codes vervangen\n" % n)
    for lab, meta, destino, hoe in hechos:
        marca = "  " if hoe != "GEEN MATCH" else "! "
        print("%s%-20s %-34s → %-28s %s" % (marca, lab, meta[:34], destino, hoe))


if __name__ == "__main__":
    main()
