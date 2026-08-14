#!/usr/bin/env python3
"""De laatste halflege bladzijden — gemeten op de PDF zelf, niet op een model.

WAAROM NOG EEN STAP
`bladspiegel.py` haalt al de bladbreuken weg die alleen een halfleeg blad
opleveren, maar het rekent op de dóórlopende pagina: hoogte van de inhoud
gedeeld door de bladhoogte. Dat klopt bijna altijd — en soms niet. Een kader
dat niet mag breken schuift in zijn geheel naar het volgende blad en verschuift
daarmee álles erna; in C5 U8 liep de rekensom twee bladzijden achter op de
werkelijkheid, en precies daar bleef een blad op 19 % staan.

Wat hier gebeurt is dus geen tweede model maar een meting: de PDF is gebouwd,
dus de bladzijden liggen vast. Van élk blad is de vulling te meten
(`medir_bladspiegel`) en van élke mijlpaalsectie is te zien op welk blad ze
begint (de `/Dests`-tabel, via `paginar`). Staat er vóór een mijlpaal een blad
op minder dan 55 %, dan is het die ene bladbreuk die het leeg houdt: weg ermee,
opnieuw renderen, opnieuw meten. Twee, drie rondes en het is uit.

Blijft een blad halfleeg zónder mijlpaal erachter, dan ligt het niet aan een
breuk maar aan de inhoud — dat wordt gemeld, niet stilzwijgend weggepoetst.

    python3 03-build/afinar_pdf.py            # alle C5/C6+-units
    python3 03-build/afinar_pdf.py C5_U8      # één unit
"""
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AQUI = os.path.join(ROOT, "03-build")
PDF = os.path.join(AQUI, "pdf")

sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(AQUI, "web"))
import medir_bladspiegel as MB      # noqa: E402
import paginar as PG                # noqa: E402
import enlaces as EN                # noqa: E402

CHROME = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))
# Elke ronde herschikt de bladzijden, dus de meting erna is een nieuwe meting:
# in C5 U8 kwam pas in ronde vier het laatste blad boven water. Zes is ruim —
# de lus stopt vanzelf zodra er niets meer te halen valt.
RONDAS = 6


def unidades(filtro=None):
    """[(naam, print-HTML, PDF)] — C5 en C6+; C4 gaat door `encoger`.

    Een breuk weghalen werkt niet in C4. Daar opent élke sectie een blad, dus
    de sectie die doorvloeit duwt haar eigen staart naar het volgende blad, en
    dáár verdwijnt de volgende breuk — geprobeerd op C4 U2: één weggehaalde
    breuk werd er drie, en de halve unit was zijn sectie-per-blad kwijt. In C4
    is een te vol blad geen breukprobleem maar een millimeterprobleem: zie
    `encoger`.
    """
    out = []
    for curso, u, impreso, _hub in EN.unidades():
        if curso == "C4":
            continue
        nombre = "%s_U%d" % ("C5" if curso == "C5" else "C6plus", u)
        pdf = os.path.join(PDF, nombre + ".pdf")
        if filtro and nombre != filtro:
            continue
        out.append((nombre, impreso, pdf))
    return out


def render(html, pdf):
    subprocess.run([CHROME[0], "--headless", "--no-sandbox", "--disable-gpu",
                    "--no-pdf-header-footer", "--print-to-pdf=" + pdf, html],
                   capture_output=True)


def mojones(pdf):
    """{ankernaam: bladzijdenummer} van elke sectie, uit de /Dests-tabel."""
    datos = open(pdf, "rb").read()
    objs = PG.objetos(datos)
    orden = PG.orden_paginas(datos, objs)
    indice = {obj: i + 1 for i, obj in enumerate(orden)}
    return {nombre.decode("latin1") if isinstance(nombre, bytes) else nombre:
            indice.get(obj, 0)
            for nombre, obj in PG._destinos(datos, objs).items()}


def quitar_corte(html, ancla):
    """Haalt de bladbreuk vóór de sectie met dit anker weg.

    Drie gedaanten, want de repo heeft er drie: `major` in de klasse (C5, C6+
    en de gegenereerde C4-units), diezelfde klasse maar met het id ervóór, en
    `break-before:page` als inline stijl (C4 U1–U10, met de hand gebouwd).
    """
    doc = open(html, encoding="utf-8").read()
    for pat, rep in (
            (r'(<div class="[^"]*)\bmajor\b([^"]*"[^>]*\bid="%s")' % re.escape(ancla), r"\1\2"),
            (r'(<div class="[^"]*?)\s+major(\s*"[^>]*)(?=[^>]*id="%s")' % re.escape(ancla), r"\1\2"),
            (r'(\bid="%s"[^>]*?style="[^"]*?)break-before:page;?' % re.escape(ancla), r"\1"),
            (r'(<div[^>]*?style="[^"]*?)break-before:page;?([^"]*"[^>]*\bid="%s")'
             % re.escape(ancla), r"\1\2")):
        nuevo, n = re.subn(pat, rep, doc)
        if n:
            open(html, "w", encoding="utf-8").write(nuevo)
            return True
    return False


def afinar(nombre, html, pdf, verboso=True):
    """(aantal weggehaalde breuken, de bladzijden die halfleeg blijven)"""
    quitados = []
    for _ronda in range(RONDAS):
        llenos = [f for f, _y in MB.paginas(pdf)]
        if not llenos:
            return 0, []
        # de laatste bladzijde van een unit telt niet mee: die eindigt waar de
        # unit eindigt, en dat is bijna nooit onderaan een blad
        flacas = [i + 1 for i, f in enumerate(llenos[:-1]) if f < MB.VACIA]
        if not flacas:
            break
        donde = mojones(pdf)
        cambio = False
        for p in flacas:
            siguiente = [a for a, pag in donde.items() if pag == p + 1]
            for ancla in siguiente:
                if ancla in quitados:
                    continue
                if quitar_corte(html, ancla):
                    quitados.append(ancla)
                    cambio = True
                    if verboso:
                        print("   %-12s blz %d op %.0f %% → breuk vóór %s weg"
                              % (nombre, p, 100 * llenos[p - 1], ancla))
                    break
        if not cambio:
            break
        render(html, pdf)
    llenos = [f for f, _y in MB.paginas(pdf)]
    quedan = [i + 1 for i, f in enumerate(llenos[:-1]) if f < MB.VACIA]
    return len(quitados), quedan


# ── C4: de laatste centimeters ─────────────────────────────────────────────
# In C4 opent elke sectie een blad en is elke sectie verrijkt tot ze dat blad
# vult. Loopt er één er net overheen, dan valt een handvol regels op het blad
# erna, en omdat de sectie dáárna sowieso bovenaan begint blijft dat blad op
# 3 tot 9 % staan. Drie bladzijden in de hele cursus.
#
# Hoevéél te veel is niet te schatten uit de sectiehoogte — een sluitende
# ondermarge telt daarin mee maar valt bij een bladovergang weg, en dat is
# precies het verschil tussen «past» en «past niet». Op de PDF is het wél te
# zien: het blad dat overloopt staat op x % vulling, dus x % van een blad is
# te veel. Een sectie die twee bladen beslaat en er 3 % overheen gaat, moet
# 1,5 % krimpen; dat is één regel en op papier onzichtbaar. Boven de vijf
# procent stopt het rekenwerk en begint het redactiewerk — dan is de sectie
# niet te hoog opgemaakt maar te vol geschreven, en dat is een beslissing van
# de auteur, niet van een script.
MARCA_ZOOM = "/* afinar_pdf.py — de laatste centimeters, gemeten */"
MAX_ENCOGE = 0.95


def unidades_c4(filtro=None):
    out = []
    for curso, u, impreso, _hub in EN.unidades():
        if curso != "C4":
            continue
        nombre = "C4_U%d" % u
        if filtro and nombre != filtro:
            continue
        out.append((nombre, impreso,
                    os.path.join(AQUI, "web", "print", nombre + ".pdf")))
    return out


def encoger(nombre, html, pdf, verboso=True):
    """(gekrompen secties, de secties die te vol geschreven zijn)"""
    doc = open(html, encoding="utf-8").read()
    limpio = re.sub(r"\n*" + re.escape(MARCA_ZOOM) + r".*?/\* fin \*/", "",
                    doc, flags=re.S)
    if limpio != doc:
        open(html, "w", encoding="utf-8").write(limpio)
        render(html, pdf)

    llenos = [f for f, _y in MB.paginas(pdf)]
    flacas = [i + 1 for i, f in enumerate(llenos[:-1]) if f < MB.VACIA]
    if not flacas:
        return [], []
    donde = mojones(pdf)
    empieza = sorted((p, a) for a, p in donde.items())
    ajustes, tercos = [], []
    for p in flacas:
        # de sectie die op dit blad overloopt, is de laatste die vóór p begon
        previa = [a for q, a in empieza if q <= p]
        if not previa:
            continue
        ancla = previa[-1]
        q = donde[ancla]
        blados = p - q                     # volle bladen die de sectie al vult
        if blados < 1:
            continue
        factor = blados / (blados + llenos[p - 1])
        (ajustes if factor >= MAX_ENCOGE else tercos).append(
            (ancla, factor, p, llenos[p - 1]))
    if ajustes:
        css = "".join("#%s{zoom:%.4f}" % (a, f) for a, f, _p, _l in ajustes)
        doc = open(html, encoding="utf-8").read()
        i = doc.rfind("</style>")
        if i > 0:
            open(html, "w", encoding="utf-8").write(
                doc[:i] + "\n" + MARCA_ZOOM + css + "/* fin */\n" + doc[i:])
            render(html, pdf)
        if verboso:
            for a, f, p, l in ajustes:
                print("   %-12s blz %d op %.0f %% → %s %.1f %% kleiner"
                      % (nombre, p, 100 * l, a, 100 * (1 - f)))
    for a, f, p, l in tercos:
        print("   %-12s blz %d op %.0f %% → %s loopt %.0f %% over: te veel "
              "inhoud voor één blad, dat is redactiewerk"
              % (nombre, p, 100 * l, a, 100 * (1 / f - 1)))
    return ajustes, tercos


def main():
    if not CHROME:
        sys.exit("geen Chromium — deze stap heeft een render nodig")
    filtro = sys.argv[1] if len(sys.argv) > 1 else None
    total = 0
    restantes = []
    for nombre, html, pdf in unidades(filtro):
        if not (os.path.exists(html) and os.path.exists(pdf)):
            continue
        n, quedan = afinar(nombre, html, pdf)
        total += n
        for p in quedan:
            restantes.append("%s blz %d" % (nombre, p))
    encogidas = 0
    for nombre, html, pdf in unidades_c4(filtro):
        if not (os.path.exists(html) and os.path.exists(pdf)):
            continue
        ajustes, _tercos = encoger(nombre, html, pdf)
        encogidas += len(ajustes)
    print("%d bladbreuken weg op de gemeten PDF, %d C4-secties bijgesteld"
          % (total, encogidas))
    if restantes:
        print("nog halfleeg (geen breuk erachter — inhoud, geen bladspiegel): %s"
              % ", ".join(restantes))


if __name__ == "__main__":
    main()
