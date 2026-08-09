#!/usr/bin/env python3
"""Zet de interface-emoji van de gedrukte cursus om naar Lucide-iconen.

WAAROM NA DE BOUW EN NIET IN DE GENERATOREN
Om dezelfde reden als `bladspiegel.py` en `limpia_jerga.py`: er zijn
zevenentwintig units en achtentwintig generatoren, en C5 U0 heeft er helemaal
geen. Eén nabewerking is te overzien; achtentwintig keer dezelfde bewerking
inbouwen is dat niet.

DE REGEL — één zin, en ze bepaalt alles
**Een icoon is interface, een emoji is betekenis.** (CLAUDE.md §15.)

Een badge «✍️ Escribir» zegt de leerling *wat voor soort oefening* dit is: dat
is interface, en interface hoort er strak en eenvormig uit te zien. Een
woordkaartje met 🍎 náást *la manzana* zegt de leerling *wat het woord
betekent*: daar is de kleur en de herkenbaarheid van de emoji juist de
geheugensteun, en een grijs lijnicoon zou dat kapotmaken.

Daartussen zit een derde categorie die er als emoji uitziet maar het niet is:
★☆ voor moeilijkheid, ☐ om aan te kruisen, → in een keten, ①②③ voor de stappen,
het semáforo, de vlaggen. Dat is typografie. Die blijft ook.

De drie lijsten staan niet hier maar in `02-huisstijl/vendor/lucide/iconos.py`
(`BADGE` en `NO_TRADUCIR`), naast de iconen zelf.

WAT DIT SCRIPT NIET AANRAAKT
  · alles in <style>, <script> en in attribuutwaarden — een icoon in een
    `placeholder=` of een `title=` wordt een letterlijke `<svg>` in beeld;
  · de §V-woordenschattabellen en de flashcards;
  · alles wat in `NO_TRADUCIR` staat.

Inline SVG, geen CSS-masker: op de hub kleuren de iconen mee met de knop
waarin ze staan, maar print heeft geen knoppen en Chromium moet ze rechtstreeks
in de PDF kunnen tekenen. `currentColor` doet de rest — een icoon in een groene
badge wordt groen.

Herhaalbaar: wat al omgezet is, staat er als <svg> en wordt niet nog eens
aangeraakt.

    python3 03-build/web/print_iconos.py            # alles
    python3 03-build/web/print_iconos.py --contar   # alleen tellen
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "02-huisstijl", "vendor", "lucide"))

import enlaces as EN          # noqa: E402
import iconos as IC           # noqa: E402

# Waar een emoji staat, bepaalt hoe groot zijn icoon moet zijn. In een badge
# staat hij naast tekst van 7,4 pt, in een sectiekop naast 14 pt.
#
# De maten zijn naar beneden bijgesteld nadat de meting liet zien dat de iconen
# C4 U1 en U10 net over een blad duwden: een emoji zit binnen de regelhoogte,
# een SVG van 3,3 mm rekte haar op. Met 2,9 mm en `line-height:0` op de svg
# blijft de regel even hoog als voorheen.
MM_BADGE = 2.9
MM_TEXTO = 3.5
MM_KOP = 4.2

# Blokken die met rust gelaten worden. De woordenschat is de belangrijkste: daar
# ís de emoji de betekenis (zie de kop van dit bestand).
INTOCABLE = re.compile(
    r"<style>.*?</style>"
    r"|<script.*?</script>"
    r"|<table class=\"[^\"]*\bvoc\b[^\"]*\">.*?</table>"
    r"|<div class=\"[^\"]*\b(?:flash|vocab|mispal|voctab)\b[^\"]*\">.*?</div>",
    re.S)

# Een tag met zijn attributen: daar staat een emoji in een waarde, niet in beeld.
ETIQUETA = re.compile(r"<[^>]*>")

VARIACION = "️︎"


def _emoji_re():
    """Alleen de emoji waarvoor we een icoon hébben — niets anders raken we aan."""
    claves = sorted(IC.BADGE, key=len, reverse=True)
    return re.compile("(?:%s)[%s]?" % ("|".join(re.escape(k) for k in claves),
                                       VARIACION))


EMOJI = _emoji_re()


def _tamano(antes):
    """De maat, afgeleid uit het element waar de emoji in staat."""
    cola = antes[-160:]
    if re.search(r'class="[^"]*\bbadge\b[^"]*"[^>]*>[^<]*$', cola):
        return MM_BADGE
    if re.search(r'<(?:h2|h3|h4)[^>]*>[^<]*$|class="[^"]*\b(?:pk|se|divider)\b',
                 cola):
        return MM_KOP
    return MM_TEXTO


def procesar(ruta, contar=False):
    doc = open(ruta, encoding="utf-8").read()
    n = [0]

    def en_texto(trozo, desplazamiento):
        """Vervangt de emoji in één stuk gewone tekst (dus buiten de tags)."""
        partes, ultimo = [], 0
        for m in ETIQUETA.finditer(trozo):
            partes.append((trozo[ultimo:m.start()], ultimo))
            partes.append((m.group(0), None))       # tag: onaangeroerd
            ultimo = m.end()
        partes.append((trozo[ultimo:], ultimo))

        salida = []
        for texto, pos in partes:
            if pos is None:
                salida.append(texto)
                continue
            def rep(m, base=len("".join(salida))):
                clave = m.group(0).rstrip(VARIACION)
                nombre = IC.BADGE.get(clave)
                if not nombre:
                    return m.group(0)
                n[0] += 1
                if contar:
                    return m.group(0)
                antes = "".join(salida) + texto[:m.start()]
                return IC.icono(nombre, mm=_tamano(antes))
            salida.append(EMOJI.sub(rep, texto))
        return "".join(salida)

    salida, ultimo = [], 0
    for m in INTOCABLE.finditer(doc):
        salida.append(en_texto(doc[ultimo:m.start()], ultimo))
        salida.append(m.group(0))
        ultimo = m.end()
    salida.append(en_texto(doc[ultimo:], ultimo))

    nuevo = "".join(salida)
    if not contar and nuevo != doc:
        open(ruta, "w", encoding="utf-8").write(nuevo)
    return n[0]


def main():
    contar = "--contar" in sys.argv
    tot = 0
    for curso, u, impreso, _hub in EN.unidades():
        k = procesar(impreso, contar=contar)
        tot += k
        print("%-4s U%-2d %4d interface-iconen" % (curso, u, k))
    print("\n%d emoji omgezet naar Lucide%s; de woordkaartjes, het semáforo, "
          "de vlaggen en de typografie (★☆ ☐ → ①) bleven staan"
          % (tot, " (niets weggeschreven)" if contar else ""))


if __name__ == "__main__":
    main()
