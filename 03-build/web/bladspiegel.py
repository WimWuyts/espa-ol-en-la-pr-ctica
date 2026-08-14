#!/usr/bin/env python3
"""Zet de bladspiegel van de zeventien printunits recht — na de bouw, in één keer.

WAAROM DIT BESTAAT
De oude regel «elke hoofdsectie start op een nieuwe bladzijde» (CLAUDE.md §14)
botst met de regel «geen halflege pagina's» (§13). Gemeten in de gebouwde units:
58 tot 75 % van alle verspilde bladruimte kwam uit die ene regel, en in C6+ U1
was een op de drie bladzijden halfleeg. Een sectie van vier regels kreeg een
eigen blad; de sectie erna begon weer bovenaan.

De nieuwe regel: **een nieuwe bladzijde is voor de mijlpalen**, niet voor elke
sectie. §0 ¡Ponte al día!, Taller de lengua, Cultura, Tarea final, Repaso en
§V Vocabulario openen een blad; de genummerde inhoudssecties vloeien door en
worden herkenbaar gemaakt door hun bovenmarge en de gekleurde parada-lijn.

Dit script doet twee dingen aan élke gebouwde unit-HTML:

  1. het zet `major` op de secties die wél een blad mogen openen;
  2. het plakt het bladspiegel-blok uit `cursus-print.css` als láátste regels in
     de `<style>`, zodat het de oudere breukregels in de generatoren overstemt.

Als nabewerking en niet in de zeventien generatoren, om dezelfde reden als
`add_puentes.py`: één plek in plaats van zeventien, en C5 U0 heeft geen
generator maar wel dezelfde bladspiegel nodig.

Herhaalbaar: draai het zo vaak je wilt, het resultaat is hetzelfde.

    python3 03-build/web/bladspiegel.py            # alle units, met meting
    python3 03-build/web/bladspiegel.py --medir    # alleen meten, niets wijzigen
"""
import os
import re
import sys

ROOT = "/home/user/espa-ol-en-la-pr-ctica"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import enlaces as EN          # noqa: E402

KIT = os.path.join(ROOT, "02-huisstijl", "templates", "cursus-print.css")

MARCA = "/* bladspiegel.py — gedeelde kit, laatste woord */"

# Secties die een nieuwe bladzijde openen. Alles wat hier niet in staat, vloeit
# door. Getest op de kopteksten zoals ze in de `pk`-span staan.
#
# §0 ¡Ponte al día! staat er bewust NIET bij: die volgt direct op de opener
# (ruta-strook + inleiding) en die twee vullen samen precies één bladzijde.
# Los van elkaar bleef de openingsbladzijde in vijftien van de zeventien units
# op ongeveer de helft steken.
MOJONES = (
    "Taller de lengua",
    "Cultura",
    "Tarea final",
    "Repaso",
    "Vocabulario",
)


def bloque():
    """Het bladspiegel-blok uit de gedeelde kit — de enige bron van waarheid."""
    css = open(KIT, encoding="utf-8").read()
    m = re.search(r"/\* @bladspiegel:ini.*?@bladspiegel:fin \*/", css, re.S)
    if not m:
        sys.exit("de markeringen @bladspiegel:ini/fin staan niet meer in %s" % KIT)
    return m.group(0)


def unidades():
    """(curso, unidad, print-HTML) — de lijst staat in enlaces.py, zie daar."""
    for curso, u, impreso, _hub in EN.unidades():
        yield (curso, u, impreso)


# De zeventien units schrijven hun sectiekop op twee manieren: C5 zet het
# nummer in een <span class="num">, de handgebouwde U0 in een <div>, met
# regeleinden ertussen. Daarom: het openingsdiv, dan alles tot de eerste
# `pk`-span, zolang er geen tweede sectie tussen zit.
# De sectiekop staat in twee gedaanten in de repo, en dat is geen slordigheid:
# C5 en C6+ zetten hem in een <span class="pk"> naast een achtergrondcijfer, C4
# in een strakkere <div class="se"> zonder cijfer. Eén patroon voor beide zou
# onleesbaar worden, dus het zijn er twee die dezelfde bewerking delen.
SECCION = re.compile(
    r'<div class="(?P<cls>[^"]*\bsec\b[^"]*)"(?P<resto>[^>]*)>'
    r'(?P<medio>(?:(?!<div class="[^"]*\bsec\b).){0,400}?)'
    r'<span class="pk"(?P<pkat>[^>]*)>(?P<tit>[^<]+)</span>', re.S)

SECCION_C4 = re.compile(
    r'<div class="(?P<cls>[^"]*\bsec\b[^"]*)"(?P<resto>[^>]*)>'
    r'(?P<medio>(?:(?!<div class="[^"]*\bsec\b).){0,400}?)'
    r'<div class="se"(?P<pkat>[^>]*)>(?P<tit>[^<]+)</div>', re.S)


def es_mojon(titulo):
    return any(m in titulo for m in MOJONES)


def procesar(ruta, curso="C5"):
    """Zet de mijlpaalsecties op een nieuwe bladzijde en legt de ankers.

    C4 wijkt hier bewust af, en dat is geen inconsistentie maar een gemeten
    keuze. In C5/C6+ was «elke sectie een eigen blad» de hoofdoorzaak van 198
    halflege bladzijden, dus daar openen alleen de mijlpalen nog een blad. In
    C4 is diezelfde regel opgelost met verrijking: elke sectie is aangevuld tot
    ze een blad vult, en de meting geeft 88 tot 94 % vulling met nul halflege
    bladzijden. Daar iets aan veranderen zou een werkende oplossing kapotmaken.
    C4 houdt dus zijn strikte regel; wat het overneemt zijn de ankers, want die
    zijn de motor van de bladwijzers in de PDF.

    De gedeelde breukregels gaan om diezelfde reden niet mee naar C4. `.sec`
    betekent er iets anders: in C5/C6+ is het het kopblok, in C4 de hele
    bladzijde. `break-inside:avoid` op een blok van een volle bladzijde duwt dat
    blok vooruit en laat een leeg blad achter — precies wat er gebeurde toen ik
    het blok wél injecteerde: C4 U1 ging van elf naar twaalf bladzijden met een
    blanco blad 4.
    """
    estricto = (curso == "C4")
    doc = open(ruta, encoding="utf-8").read()
    puestos, corridos = [], []

    indice = []

    def sustituir(m, envoltura="pk"):
        cls = m.group("cls")
        tit = m.group("tit").strip()
        if estricto:
            # C4 beslist zelf. U1–U10 zetten `break-before:page` als inline
            # stijl op elke sectie; U11–U14 worden gegenereerd en zetten
            # `major` alleen op de mijlpalen. Hier iets overschrijven zou een
            # van beide kapotmaken — dit script legt in C4 alleen de ankers.
            (puestos if "major" in cls or "break-before:page" in m.group("resto")
             else corridos).append(tit)
        else:
            cls = cls.replace(" major", "")
            if es_mojon(tit):
                cls += " major"
                puestos.append(tit)
            else:
                corridos.append(tit)
        # Een anker per sectie, en verderop een verborgen lijst die ernaar linkt.
        # Chromium schrijft van élk gelinkt anker een /Dests-ingang in de PDF, mét
        # de bladzijde waarop het beland is — en dát is de enige manier om ná de
        # opmaak te weten waar een sectie begint. Zonder link geen ingang, dus de
        # verborgen lijst is geen sierstuk maar de motor van de bladwijzers.
        ancla = "sec-%d" % (len(indice) + 1)
        indice.append((ancla, tit))
        resto = m.group("resto")
        if "id=" not in resto:
            resto = ' id="%s"%s' % (ancla, resto)
        if envoltura == "se":
            return ('<div class="%s"%s>%s<div class="se"%s>%s</div>'
                    % (cls, resto, m.group("medio"), m.group("pkat"), m.group("tit")))
        return ('<div class="%s"%s>%s<span class="pk"%s>%s</span>'
                % (cls, resto, m.group("medio"), m.group("pkat"), m.group("tit")))

    # de oude index eerst weg — de nav draagt attributen, dus [^>]* is nodig;
    # zonder dat stapelde elke bouwronde er een verborgen kopie bovenop
    doc = re.sub(r'<nav class="indice-pdf"[^>]*>.*?</nav>', "", doc, flags=re.S)
    doc = SECCION.sub(sustituir, doc)
    doc = SECCION_C4.sub(lambda m: sustituir(m, "se"), doc)

    if indice:
        enlaces = "".join('<a href="#%s">%s</a>' % (a, t) for a, t in indice)
        # laat staan in de opmaak (anders schrijft Chromium geen bestemming),
        # maar zonder hoogte, zonder breedte en niet te zien
        nav = ('<nav class="indice-pdf" aria-hidden="true" style="position:absolute;'
               'width:0;height:0;overflow:hidden;visibility:hidden">%s</nav>' % enlaces)
        i = doc.rfind("</body>")
        doc = doc[:i] + nav + doc[i:] if i > 0 else doc + nav

    # het blok als laatste in de <style>; een oude versie wordt vervangen
    # ook de lege regel ervóór mee, anders groeit het bestand elke ronde met één
    doc = re.sub(r"\n*" + re.escape(MARCA) + r".*?/\* @bladspiegel:fin \*/",
                 "", doc, flags=re.S)
    if not estricto:
        i = doc.rfind("</style>")
        if i < 0:
            sys.exit("%s heeft geen </style>" % ruta)
        doc = doc[:i] + "\n" + MARCA + "\n" + bloque() + "\n" + doc[i:]

    open(ruta, "w", encoding="utf-8").write(doc)
    return puestos, corridos


# ── de bladbreuk die zichzelf niet waard is ────────────────────────────────
# Een mijlpaal opent een blad. Dat is de regel, en meestal klopt hij. Maar loopt
# de mijlpaal ervóór net over een bladovergang — Cultura is in de meeste units
# 1,3 blad — dan blijft dat laatste blad op 30 of 40 % staan, want de volgende
# mijlpaal begint sowieso bovenaan. Zestien van de vijftig halflege bladzijden
# kwamen daarvandaan, en het waren telkens dezelfde secties.
#
# De oplossing is niet «de regel afschaffen» maar «de regel meten»: waar een
# breuk een bijna leeg blad achterlaat, gaat die ene breuk weg en vloeit de
# volgende mijlpaal door. Waar hij wél iets oplevert, blijft hij staan. Dat kan
# alleen ná de opmaak, want de hoogte van een sectie is pas dan bekend.
CHROME = sorted(__import__("glob").glob(
    "/opt/pw-browsers/chromium-*/chrome-linux/chrome"))
UTIL_MM = 273.0          # bruikbare bladhoogte, A4 min de @page-marges
LLENO = 0.55             # onder deze vulling noemen we een blad halfleeg


def _medir(ruta):
    """[(id, top in mm)] van elke mijlpaal + de totale hoogte, uit Chromium."""
    if not CHROME:
        return None
    import subprocess
    import tempfile
    src = open(ruta, encoding="utf-8").read()
    js = ("<script>window.addEventListener('load',function(){var o=[];"
          "document.querySelectorAll('.sec.major').forEach(function(p){"
          "o.push((p.id||'?')+'|'+Math.round(p.getBoundingClientRect().top*25.4/96));});"
          "o.push('EINDE|'+Math.round(document.body.getBoundingClientRect().height*25.4/96));"
          "var d=document.createElement('div');d.id='MEDIDA';d.textContent=o.join('\\n');"
          "document.body.appendChild(d);});</script>")
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False,
                                      dir=os.path.dirname(ruta))
    tmp.write(src.replace("</body>", js + "</body>"))
    tmp.close()
    try:
        salida = subprocess.run(
            [CHROME[0], "--headless", "--no-sandbox", "--disable-gpu",
             "--virtual-time-budget=6000", "--dump-dom", tmp.name],
            capture_output=True, text=True).stdout
    finally:
        os.unlink(tmp.name)
    m = re.search(r'<div id="MEDIDA">(.*?)</div>', salida, re.S)
    if not m:
        return None
    out = []
    for linea in m.group(1).split("\n"):
        if "|" in linea:
            ident, mm = linea.rsplit("|", 1)
            out.append((ident, int(mm)))
    return out


def _sobra(cortes):
    """De id's van de mijlpalen wier bladbreuk een bijna leeg blad achterlaat.

    Loopt de inhoud vóór mijlpaal M tot vlak na een bladovergang, dan is het
    de breuk van M die dat laatste blad leeg houdt. De láátste sectie telt niet
    mee: die eindigt op de laatste bladzijde van de unit, en die is nooit vol.

    Ook een korte mijlpaal telt mee, en dat is niet vanzelfsprekend: eerst
    keken we alleen naar secties die over een bladovergang liepen. Maar een
    Repaso van 52 mm gevolgd door §V Vocabulario levert net zo goed een blad
    van 19 % op — dat waren de laatste drie in C5. Eén blok inhoud is één blok
    inhoud, of het nu een halve bladzijde of anderhalve beslaat.
    """
    fuera = []
    anterior = 0
    for ident, top in cortes:
        alto = top - anterior
        anterior = top
        if ident == "EINDE" or alto <= 0:
            continue
        blados = max(1, int(-(-alto // UTIL_MM)))
        resto = (alto - (blados - 1) * UTIL_MM) / UTIL_MM
        if resto < LLENO:
            fuera.append(ident)
    return fuera


# ── het blok dat niet op een blad past ─────────────────────────────────────
# `break-inside:avoid` betekent «snijd dit kader niet doormidden», en dat klopt
# voor een onthoudkaart van 40 mm. Voor een blok van 492 mm betekent het iets
# anders: de browser kán het niet heel houden, dus schuift ze het in zijn geheel
# naar de volgende bladzijde — en snijdt het daarna alsnog door. Het blad ervóór
# blijft halfleeg achter. Dat was de oorzaak van de laatste zestien.
#
# Welke blokken dat zijn valt niet met de hand te weten: het hangt van de inhoud
# af, en die verandert bij elke bouwronde. Dus meten. Chromium legt de bladzijde
# op, wij lezen de hoogte én de berekende `break-inside` terug, en wie boven een
# bladhoogte uitkomt krijgt `suelto` — breken mag, mét volledige omranding aan
# beide helften (`box-decoration-break:clone`, zie de kit).

def _bloques_altos(ruta, minimo=UTIL_MM):
    """[(class-attribuut, hoeveelste, hoogte in mm)] van de te hoge kaders.

    Het adres van een blok is «het n-de element met precies dít class-attribuut».
    Ids zijn er niet op elk kader, en een positie in de DOM-boom overleeft de
    volgende bouwronde niet; het class-attribuut wél, en bronvolgorde is
    DOM-volgorde. De teller loopt over álle elementen met een class, niet enkel
    over de gevonden — anders wijst het adres na de eerste treffer al mis.
    """
    if not CHROME:
        return []
    import html as HT
    import subprocess
    import tempfile
    js = ("<script>window.addEventListener('load',function(){var o=[],c={};"
          "document.querySelectorAll('*').forEach(function(e){"
          "var k=e.getAttribute('class'); if(!k) return;"
          "var n=(c[k]=(c[k]||0)+1)-1; var s=getComputedStyle(e);"
          "if(s.breakInside!=='avoid'&&s.pageBreakInside!=='avoid') return;"
          "var h=e.getBoundingClientRect().height*25.4/96; if(h<%d) return;"
          "o.push(k+'\\t'+n+'\\t'+Math.round(h));});"
          "var d=document.createElement('div');d.id='ALTOS';d.textContent=o.join('\\n');"
          "document.body.appendChild(d);});</script>" % int(minimo))
    src = open(ruta, encoding="utf-8").read()
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False,
                                      dir=os.path.dirname(ruta))
    tmp.write(src.replace("</body>", js + "</body>"))
    tmp.close()
    try:
        salida = subprocess.run(
            [CHROME[0], "--headless", "--no-sandbox", "--disable-gpu",
             "--virtual-time-budget=6000", "--dump-dom", tmp.name],
            capture_output=True, text=True).stdout
    finally:
        os.unlink(tmp.name)
    m = re.search(r'<div id="ALTOS">(.*?)</div>', salida, re.S)
    if not m:
        return []
    out = []
    for linea in m.group(1).split("\n"):
        piezas = linea.split("\t")
        if len(piezas) != 3:
            continue
        cls, n, alto = piezas
        out.append((HT.unescape(cls), int(n), int(alto)))
    return out


def soltar(ruta, minimo=UTIL_MM):
    """Zet `suelto` op elk onbreekbaar kader dat hoger is dan een bladzijde."""
    altos = _bloques_altos(ruta, minimo)
    if not altos:
        return []
    doc = open(ruta, encoding="utf-8").read()
    hecho = []
    # van achter naar voren per class: een vervanging haalt die voorkomst uit de
    # telling, dus een lager volgnummer blijft alleen kloppen als het later komt
    for cls, n, alto in sorted(altos, key=lambda x: (x[0], -x[1])):
        aguja = 'class="%s"' % cls
        pos = -1
        for _ in range(n + 1):
            pos = doc.find(aguja, pos + 1)
            if pos < 0:
                break
        if pos < 0:
            continue
        doc = doc[:pos] + 'class="%s suelto"' % cls + doc[pos + len(aguja):]
        hecho.append((cls, alto))
    if hecho:
        open(ruta, "w", encoding="utf-8").write(doc)
    return hecho


def afinar(ruta, rondas=3):
    """Haalt de bladbreuken weg die alleen een halfleeg blad opleveren."""
    quitados = []
    for _ronda in range(rondas):
        cortes = _medir(ruta)
        if not cortes:
            return quitados
        sobran = [i for i in _sobra(cortes) if i not in quitados and i != "?"]
        if not sobran:
            break
        doc = open(ruta, encoding="utf-8").read()
        cambio = False
        for ident in sobran:
            pat = re.compile(r'(<div class="[^"]*)\bmajor\b([^"]*"[^>]*\bid="%s")'
                             % re.escape(ident))
            nuevo, n = pat.subn(r"\1\2", doc)
            if not n:                       # id staat vóór de class
                pat = re.compile(r'(<div class="[^"]*?)\s+major(\s*"[^>]*)'
                                 r'(?=[^>]*id="%s")' % re.escape(ident))
                nuevo, n = pat.subn(r"\1\2", doc)
            if n:
                doc, cambio = nuevo, True
                quitados.append(ident)
        if not cambio:
            break
        open(ruta, "w", encoding="utf-8").write(doc)
    return quitados


def main():
    solo_medir = "--medir" in sys.argv
    tot_p = tot_c = tot_q = tot_s = 0
    for curso, u, ruta in unidades():
        if solo_medir:
            doc = open(ruta, encoding="utf-8").read()
            tit = [m.group("tit") for m in SECCION.finditer(doc)]
            p = [t for t in tit if es_mojon(t)]
            c = [t for t in tit if not es_mojon(t)]
        else:
            p, c = procesar(ruta, curso)
            # C4 beslist zijn eigen breuken (zie procesar); daar niets afnemen.
            if curso != "C4":
                # eerst de te hoge kaders losmaken, dan pas de breuken bijstellen:
                # een blok dat nog in zijn geheel doorschuift, verplaatst elke
                # mijlpaal erna en zou `afinar` op verkeerde hoogtes laten meten
                tot_s += len(soltar(ruta))
                q = afinar(ruta)
                if q:
                    tot_q += len(q)
                    p = [x for x in p]      # de telling blijft de gezette mijlpalen
        tot_p += len(p); tot_c += len(c)
        print("%-4s U%d  %2d nieuwe bladzijde, %2d doorlopend" % (curso, u, len(p), len(c)))
    print("\n%d secties openen een blad, %d vloeien door" % (tot_p, tot_c))
    if tot_s:
        print("%d kaders losgemaakt: hoger dan een bladzijde, dus niet heel te houden"
              % tot_s)
    if tot_q:
        print("%d bladbreuken teruggenomen: ze lieten alleen een halfleeg blad achter"
              % tot_q)


if __name__ == "__main__":
    main()
