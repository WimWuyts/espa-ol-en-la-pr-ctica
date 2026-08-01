#!/usr/bin/env python3
"""Vervangt de elf productienotities in C5 U0 door echte leerlinginhoud.

Waarom: `U0.html` bevatte nog elf `<div class="asset">`-kaders met regieaanwijzingen
voor de bouw — «[AUDIO: …]», «[BEELD: …]», «[ICOON: …]». Die staan in klein grijs
cursief en worden dus gewoon meegedrukt. CLAUDE.md §18 verbant precies dat uit de
leerlingeneditie: ontbrekende inhoud wordt *gegenereerd*, niet aangekondigd.

Eén van die kaders lekte bovendien de oplossing van het dictee («veintidós …
catorce … sesenta y ocho»); oplossingen horen volgens §14 niet op de
leerlingpagina.

Elk kader is vervangen door iets wat de leerling op díé plaats echt kan
gebruiken: een luisterstrategie, een uitspraakvergelijking, een invultabel met
schrijfruimte, een instructie voor het werk per twee, of de legende bij de
semáforo — die drie kolommen stonden er tot nu toe zonder uitleg bij.

Het script werkt op de sleuteltekst van elk kader en is herhaalbaar: staat de
nieuwe inhoud er al, dan doet het niets. Er wordt alleen vervangen, nooit iets
weggelaten dat de leerling nodig heeft.

Naast `U0.html` stond er een map `_html/` met een oudere momentopname van
dezelfde secties. Die had geen enkele consument — geen enkel script bouwde de
cursus eruit — en was intussen 4 tot 40 % van `U0.html` weg gedreven, dus als
«bron» was ze vooral een valstrik. Ze is verwijderd; `U0.html` is de bron.
Terughalen kan met `git show 69536af:01-cursussen/05-a1/U0/_html/<naam>.html`.

    python3 01-cursussen/05-a1/U0/vervang_assets_u0.py
    python3 01-cursussen/05-a1/U0/vervang_assets_u0.py --check   # alleen tellen
"""
import argparse
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
DOEL = os.path.join(HIER, "U0.html")

# Per kader: (herkenningstekst uit het oude kader, nieuwe HTML).
# De herkenningstekst is een fragment dat maar in één kader voorkomt.
VERVANGINGEN = [
    ("1.3 Microdictado", """<div class="ojo"><b>Antes de escuchar.</b> Mira primero las seis líneas vacías. Vas a oír cada palabra <b>dos veces</b>, con una pausa. Escribe solo lo que oyes; las tildes las corriges después. <span class="gloss">Kijk eerst naar de zes lege regels. Je hoort elk woord twee keer, met een pauze ertussen. Schrijf gewoon wat je hoort — de accenten verbeter je achteraf.</span></div>"""),

    ("minimal-pairs fragment", """<div class="ojo"><b>¿En qué te fijas?</b> <b>seis</b> ↔ <b>siete</b>: la <b>-s</b> del final. <b>doce</b> ↔ <b>trece</b>: la primera consonante, <b>d</b> o <b>t</b>. <b>sesenta</b> ↔ <b>setenta</b>: otra vez <b>s</b> o <b>t</b>, ahora en el medio. <span class="gloss">Let telkens op één klank: de eind-s bij seis/siete, en de d/t of s/t bij de andere paren. Verder klinken de woorden bijna hetzelfde — daarom is dit lastig.</span></div>"""),

    ("AUDIO 3.4b", """<div class="ojo"><b>Un truco para los números.</b> De <b>16</b> a <b>29</b> es <b>una sola palabra</b>: <i>dieciséis</i>, <i>veintidós</i>. A partir de <b>31</b> siempre oyes una <b>y</b>: <i>treinta y uno</i>, <i>sesenta y ocho</i>. <span class="gloss">Hoor je «y», dan is het getal groter dan dertig. Hoor je één lang woord, dan zit je tussen 16 en 29. Zo weet je meteen in welk gebied je zit, ook als je het woord zelf niet helemaal verstaat.</span></div>"""),

    ("SurveyAndReport", """<table class="mp"><thead><tr><th style="width:36%">Nombre</th><th style="width:20%">Edad</th><th>Teléfono</th></tr></thead><tbody>
      <tr><td><span class="wl"></span></td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>
      <tr><td><span class="wl"></span></td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>
      <tr><td><span class="wl"></span></td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr>
      <tr><td><span class="wl"></span></td><td><span class="wl sm"></span></td><td><span class="wl md"></span></td></tr></tbody></table>
    <div class="route-note">🎙️ <b>En línea:</b> graba tu resumen en la pestaña «Hablar» y escúchate. <span class="gloss">Neem je samenvatting op de digitale pagina op, tabblad Hablar, en luister jezelf terug.</span></div>"""),

    ("RouteMap-mini", """<div class="hist"><b>Y ahora, por escrito.</b> Escribe la frase que acabas de decir en voz alta: <span class="wl full"></span> <span class="gloss">Schrijf de zin op die je net hardop hebt gezegd. Wat je zegt én schrijft, blijft dubbel zo goed hangen.</span></div>"""),

    ("minipaar — dezelfde woorden", """<div class="ojo"><b>gracias · cinco · plaza</b> — las mismas palabras, dos pronunciaciones. En el <b>centro y el norte de España</b>, la <b>c</b> y la <b>z</b> suenan como la <i>th</i> inglesa. En <b>América</b> y en el <b>sur de España</b> suenan como una <b>s</b>. <b>Las dos son correctas.</b> <span class="gloss">Dezelfde woorden, twee uitspraken. Allebei goed — kies er één en blijf ze consequent gebruiken.</span><br>☐ Yo digo <b>gra·th·ias</b> &nbsp;&nbsp;&nbsp; ☐ Yo digo <b>gra·s·ias</b></div>"""),

    ("rima de las vocales", """<div class="ojo"><b>Dilo tres veces</b>, cada vez un poco más rápido — y sin cambiar las vocales: la <b>a</b> siempre suena <i>a</i>, la <b>e</b> siempre <i>e</i>. <span class="gloss">Zeg het rijmpje drie keer, telkens iets sneller. Het geheim: de klinkers blijven altijd precies hetzelfde klinken, ook als je snel praat. Dat is nu net het verschil met het Nederlands, waar klinkers vervagen.</span></div>"""),

    ("alfabet-referentie per letter", """<div class="hist"><b>En parejas.</b> Deletrea tu nombre a tu compañero/-a; él o ella lo escribe. Después, al revés. <span class="gloss">Per twee: spel jouw naam, de ander schrijft hem op. Daarna wisselen.</span><br>El nombre de mi compañero/-a: <span class="wl full"></span> ☐ correcto</div>"""),

    ("turn-taking", """<div class="ojo"><b>Lo que necesitas decir.</b> «¿Cómo <b>te llamas</b>?» → «Me llamo…» · «¿Cómo <b>se escribe</b>?» → «Se escribe…» · «¿<b>Puedes repetir</b>, por favor?» <span class="gloss">Met deze drie zinnetjes kun je allebei de beurten aan. «¿Puedes repetir?» is je redmiddel als je iets niet verstaat — gebruik het gerust, dat hoort erbij.</span></div>"""),

    ("opnamefunctie in de HTML-versie", """<div class="route-note">🎙️ <b>En línea:</b> en la pestaña «Hablar» puedes grabarte, escucharte y repetirlo. <span class="gloss">Op de digitale pagina, tabblad Hablar, kun je jezelf opnemen, terugluisteren en het nog eens doen. Op papier doe je het live aan de klas.</span></div>"""),

    ("TrafficLight per rij", """<div class="hist"><b>Las tres columnas:</b> 🔴 <b>todavía no</b> — necesito ayuda · 🟠 <b>casi</b> — lo hago con el libro delante · 🟢 <b>ya lo sé</b> — lo hago solo/-a. Marca <b>una</b> casilla por línea. <span class="gloss">Rood = nog niet, oranje = het lukt met het boek erbij, groen = ik kan het alleen. Kruis per rij één vakje aan. Dit is voor jou, niet voor een punt.</span></div>"""),
]

ASSET = re.compile(r'<div class="asset">.*?</div>', re.S)


def vervang(pad, meld=True):
    src = open(pad, encoding="utf-8").read()
    gedaan, over = 0, []
    for sleutel, nieuw in VERVANGINGEN:
        treffers = [m for m in ASSET.finditer(src) if sleutel in m.group(0)]
        if not treffers:
            continue
        if len(treffers) > 1:
            over.append("%s (%d keer gevonden — niet uniek)" % (sleutel, len(treffers)))
            continue
        m = treffers[0]
        src = src[:m.start()] + nieuw + src[m.end():]
        gedaan += 1
    resterend = len(ASSET.findall(src))
    if gedaan:
        open(pad, "w", encoding="utf-8").write(src)
    if meld:
        print("  %-46s %2d vervangen · %2d asset-kaders over%s"
              % (os.path.relpath(pad), gedaan, resterend,
                 (" · LET OP: " + "; ".join(over)) if over else ""))
    return gedaan, resterend


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="alleen tellen, niets schrijven")
    a = ap.parse_args()
    if a.check:
        n = len(ASSET.findall(open(DOEL, encoding="utf-8").read()))
        print("  %-46s %2d asset-kaders" % (os.path.relpath(DOEL), n))
        return 0
    _, over = vervang(DOEL)
    return 0 if over == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
