#!/usr/bin/env python3
"""Alle onderlinge verwijzingen op één plaats: boek → hub → PowerPoint.

WAAROM ÉÉN BESTAND
Een QR-code die naar de homepage wijst is bijna even nutteloos als geen QR-code:
de leerling staat dan alsnog te zoeken. Elke code hoort naar de *oefening* te
wijzen. Dat kan alleen als er één plek is waar de adressen vandaan komen, anders
lopen boek en hub binnen twee units uit elkaar.

DE AFSPRAAK
  basis        https://espanol-en-la-practica.wim-wuyts1979.chatgpt.site/
  bladzijde    c5-u0.html … c5-u8.html  ·  c6plus-u0.html … c6plus-u7.html
  anker        het id van het element op de hub (#c5-u0-aud-01, #retos_u0, …)

De hub kent al hash-navigatie: `#<id>` opent het juiste tabblad én scrolt naar
het element. Er is dus geen aparte landingspagina per oefening nodig — het anker
volstaat, en het blijft werken als de hub herbouwd wordt.

Welke bestanden onder welke naam op de site moeten, staat in `manifiesto()`.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(HERE))          # de wortel van de repo
sys.path.insert(0, HERE)

BASE = "https://espanol-en-la-practica.wim-wuyts1979.chatgpt.site/"

# Hoe de gebouwde hub op de site heet. Links zijn de bron in de repo, rechts de
# naam waaronder het bestand geüpload wordt — kort, kleine letters, voorspelbaar.
_SLUG = {"C4": "c4", "C5": "c5", "C6+": "c6plus"}


def pagina(curso, unidad):
    """De bestandsnaam van de hub van één unit, zoals ze op de site staat."""
    return "%s-u%d.html" % (_SLUG[curso], unidad)


def fuente(curso, unidad):
    """Het gebouwde bestand in de repo dat daarheen geüpload moet worden."""
    if curso == "C4":
        return os.path.join("componentes", "C4_U%d_hub.html" % unidad)
    return ("U%d_web.html" % unidad if curso == "C5"
            else "C6plus_U%d_web.html" % unidad)


def url(curso, unidad, ancla=None):
    """Het volledige adres, met anker als het gegeven is."""
    u = BASE + pagina(curso, unidad)
    return u + "#" + ancla if ancla else u


# ── de ankers ───────────────────────────────────────────────────────────────
# Eén functie per soort verwijzing, zodat een naamswijziging op de hub hier
# gerepareerd wordt en niet in zeventien generatoren.

def ancla_audio_largo(curso, unidad):
    """Het grote luisterfragment met de begripsladder."""
    return "esc_u%d" % unidad if curso == "C5" else "esc_c6p_u%d" % unidad


def ancla_audio_corto(frag_id):
    """Een korte audiotaak; `frag_id` is de id uit escucha_corta_data."""
    return frag_id.lower()


def ancla_reto(reto_id):
    """Eén reto op de hub — «C5-U5-RETO-01» → «reto-c5-u5-01»."""
    return "reto-" + reto_id.lower().replace("-reto", "")


def ancla_retos(curso, unidad):
    """Het hele reto-paneel van een unit."""
    return "retos_u%d" % unidad if curso == "C5" else "retos_c6p_u%d" % unidad


def ancla_lectura(curso, unidad):
    return "lec_u%d" % unidad if curso == "C5" else "lec_c6p_u%d" % unidad


def ancla_panel(nombre):
    """Een heel tabblad: vocab · gram · lectura · escuchar · juegos · retos ·
    hablar · cultura · extra."""
    return nombre


def ancla_juego(slug):
    """Een motor-spel op de hub; de generatoren gebruiken id «g_<slug>»."""
    return "g_" + slug


# ── C4 ──────────────────────────────────────────────────────────────────────
# De C4-hub is anders gebouwd dan die van C5/C6+: zeven tabbladen, elk een
# `srcdoc`-iframe, zodat de pagina offline werkt zonder losse bestanden. Een
# adres kán daarom niet dieper reiken dan het tabblad — een anker binnen een
# srcdoc-iframe is van buitenaf niet aanspreekbaar. Dat is geen slordigheid
# maar de prijs van «standalone»; het tabblad opent wél meteen op de juiste
# oefening, want elk tabblad ís één oefening.
C4_TABS = ("escucha", "comprension", "mapa", "funciones", "kit", "practica", "musica")


def ancla_c4(tab):
    """Eén tabblad van de C4-hub. Onbekende naam = programmeerfout, geen stille
    terugval naar de paginatop: dan zou een QR-code het weer niet weten."""
    if tab not in C4_TABS:
        raise ValueError("onbekend C4-tabblad %r — ken: %s" % (tab, ", ".join(C4_TABS)))
    return tab


# ── de QR-kaart voor in het boek ────────────────────────────────────────────

def tarjeta_qr(destino, etiqueta, meta="", mm=17, nivel="Q"):
    """De QR-kaart zoals ze in de printcursus staat.

    `destino` is een volledig adres (gebruik `url(...)`). Foutcorrectieniveau Q
    is bewust: een schoolboek krijgt vouwen, vingers en kopieerstreepjes te
    verduren, en op Q blijft een code leesbaar tot ongeveer een kwart van het
    oppervlak beschadigd is.
    """
    from qr_codigo import qr_svg
    svg = qr_svg(destino, mm=mm, nivel=nivel)
    m = ('<div class="meta">%s</div>' % meta) if meta else ""
    # het doel staat ook als attribuut in de HTML: onzichtbaar op papier, maar
    # zo is bij elke bouw na te gaan waar elke code heen wijst zonder hem te
    # moeten scannen (zie `informe_qr.py`)
    return ('<div class="qr" data-url="%s">%s<div class="lab">%s</div>%s</div>'
            % (destino, svg, etiqueta, m))


def impreso(curso, unidad):
    """De gebouwde print-HTML van één unit — de bron van de PDF.

    C4 schrijft naar `03-build/web/print/`, C5 en C6+ naar hun eigen unitmap.
    C6+ heeft twee namen in omloop (de oudste units heten nog `U<n>.html`).
    """
    if curso == "C4":
        return os.path.join(HERE, "print", "C4_U%d.html" % unidad)
    if curso == "C5":
        return os.path.join(RAIZ, "01-cursussen", "05-a1",
                            "U%d" % unidad, "U%d.html" % unidad)
    d = os.path.join(RAIZ, "01-cursussen", "06-vervolg", "U%d" % unidad)
    p = os.path.join(d, "C6plus_U%d.html" % unidad)
    return p if os.path.exists(p) else os.path.join(d, "U%d.html" % unidad)


def unidades(cursos=("C4", "C5", "C6+")):
    """(curso, unidad, print-HTML, hub-HTML) voor alles wat gebouwd is.

    Zes nabewerkingsscripts hadden elk hun eigen kopie van deze lijst. Dat gaat
    goed tot er een cursus bijkomt — dan moet je zes keer dezelfde regel
    toevoegen en vergeet je er één. Daarom staat ze hier, naast de adressen
    waar ze bij hoort.
    """
    rangos = {"C4": range(1, 15), "C5": range(9), "C6+": range(8)}
    for curso in cursos:
        for u in rangos[curso]:
            p = impreso(curso, u)
            if os.path.exists(p):
                yield (curso, u, p, os.path.join(HERE, fuente(curso, u)))


def manifiesto():
    """Wat er waarheen moet op de site — de uploadlijst voor de auteur."""
    filas = []
    for curso, unidades in (("C4", range(1, 15)), ("C5", range(9)), ("C6+", range(8))):
        for u in unidades:
            src = os.path.join("03-build", "web", fuente(curso, u))
            if not os.path.exists(os.path.join(HERE, fuente(curso, u))):
                continue          # nog niet gebouwd — niet op de uploadlijst zetten
            filas.append((src, pagina(curso, u), "%s · unidad %d" % (curso, u)))
    return filas


if __name__ == "__main__":
    print("Basis: %s\n" % BASE)
    print("%-34s → %-18s %s" % ("bestand in de repo", "naam op de site", "wat"))
    print("-" * 78)
    for src, dst, wat in manifiesto():
        print("%-34s → %-18s %s" % (src, dst, wat))
    print("\nVoorbeeld van een diep adres:")
    print(" ", url("C5", 0, ancla_audio_corto("C5-U0-AUD-03")))
    print(" ", url("C6+", 7, ancla_retos("C6+", 7)))
