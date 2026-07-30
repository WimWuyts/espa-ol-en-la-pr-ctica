#!/usr/bin/env python3
"""«Práctica extra en línea» — QR-pagina per unit naar externe oefenpagina's.

De auteur vraagt in de cursus naar de exacte deelpagina van *La página del español* te
verwijzen. Let op: beide blueprints verbieden dit oorspronkelijk («toon de naam of
vormgeving van de externe website niet aan leerlingen» — C5 §0, C6+ §6.1). De auteur heeft
die keuze bewust herzien; dit script voert de herziene keuze uit.

Uitgangspunten:
- **één pagina per unit**, niet dertien QR's verspreid door de cursus → één plek om te
  onderhouden als een link verdwijnt;
- **echte QR-codes** via `segno`, inline als SVG (geen externe beeldbestanden, geen
  afhankelijkheid van een QR-dienst);
- de oefeningen in de cursus blijven **zelf geschreven** — dit is enkel een verwijzing;
- expliciet gelabeld als **online**, ter onderscheid van de offline hub.

    python3 03-build/web/gen_qr_extra.py C5 0          # print-blok + hub-blok voor C5 U0
    python3 03-build/web/gen_qr_extra.py C6+ 0 1 2
    python3 03-build/web/gen_qr_extra.py --alle
    python3 03-build/web/gen_qr_extra.py --check       # controleer of de links nog leven

Uitvoer: `03-build/web/qr/<cursus>_U<n>_extra.html` — één zelfstandig blok dat zowel in de
printlaag als in de hub-tab «Extra · bronnen» kan worden ingevoegd.
"""
import argparse, os, ssl, sys, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "03-build", "web", "qr")
B = "https://paginadelespanol.com/"

# Bron: de twee blueprints (00-brondocumenten/gap-analyse/).
# Per BLUEPRINT-OEFENING de bijbehorende bronpagina → zo kan het QR-balkje pal naast de
# juiste oefening in de cursus staan, niet enkel gebundeld achteraan.
EJERCICIOS = {
    # id                        (cursus, unit, titel die de leerling ziet,      URL)
    "C5-U0-NAT-01":  ("C5", 0, "Los números del 0 al 10",        B + "los-numeros-del-0-al-10/"),
    "C5-U0-NAT-02":  ("C5", 0, "Los números del 10 al 20",       B + "los-numeros-del-10-al-20/"),
    "C5-U1-NAT-01":  ("C5", 1, "Nacionalidades del mundo hispano", B + "nacionalidades-de-los-paises-hispanohablantes/"),
    "C5-U2-NAT-01":  ("C5", 2, "Adjetivos posesivos",            B + "adjetivos-posesivos/"),
    "C5-U3-NAT-01":  ("C5", 3, "Verbos reflexivos",              B + "utiliza-estos-verbos-reflexivos/"),
    "C5-U4-NAT-01":  ("C5", 4, "El verbo gustar y similares",     B + "25-frases-para-practicar-el-verbo-gustar-y-similares/"),
    "C5-U5-NAT-01":  ("C5", 5, "Verbos para cocinar",            B + "20-verbos-cocinar-espanol/"),
    "C5-U5-NAT-02":  ("C5", 5, "Adjetivos sobre la comida",      B + "completa-frases-con-adjetivos-comida/"),
    "C5-U6-NAT-01":  ("C5", 6, "Verbos para hablar de la ropa",  B + "20-verbos-para-hablar-sobre-la-ropa/"),
    "C5-U6-NAT-02":  ("C5", 6, "Palabras de moda",               B + "25-palabras-relacionadas-con-la-moda/"),
    "C5-U7-NAT-01":  ("C5", 7, "Sopa de letras: la casa",        B + "sopa-de-letras-15-palabras-relacionadas-con-la-casa/"),
    "C5-U7-NAT-02":  ("C5", 7, "El imperativo",                  B + "25-frases-para-practicar-el-imperativo/"),
    "C5-U8-NAT-01":  ("C5", 8, "El pretérito perfecto",          B + "20-frases-para-practicar-el-preterito-perfecto/"),

    "c6p-u0-nationalities-20": ("C6+", 0, "Nacionalidades del mundo hispano", B + "nacionalidades-de-los-paises-hispanohablantes/"),
    "c6p-u1-ser-estar-30":     ("C6+", 1, "Ser y estar",              B + "30-frases-para-practicar-los-verbos-ser-y-estar/"),
    "c6p-u1-reflexives-20":    ("C6+", 1, "Verbos reflexivos",        B + "utiliza-estos-verbos-reflexivos/"),
    "c6p-u2-house-15":         ("C6+", 2, "Sopa de letras: la casa",  B + "sopa-de-letras-15-palabras-relacionadas-con-la-casa/"),
    "c6p-u3-ir-a-inf-25":      ("C6+", 3, "El futuro próximo (ir a + inf.)", B + "25-frases-para-practicar-el-futuro-proximo/"),
    "c6p-u4-perfecto-20":      ("C6+", 4, "El pretérito perfecto",    B + "20-frases-para-practicar-el-preterito-perfecto/"),
    "c6p-u4-participles-20":   ("C6+", 4, "Participios irregulares",  B + "20-participios-irregulares/"),
    "c6p-u5-indefinido-30":    ("C6+", 5, "El pretérito indefinido",  B + "30-frases-para-practicar-el-preterito-indefinido/"),
    "c6p-u6-imperfecto-25":    ("C6+", 6, "El pretérito imperfecto",  B + "25-frases-para-practicar-el-preterito-imperfecto/"),
    "c6p-u7-imperative-25":    ("C6+", 7, "El imperativo",            B + "25-frases-para-practicar-el-imperativo/"),
    "c6p-u7-climate-25":       ("C6+", 7, "Verbos del tiempo y el clima", B + "25-verbos-para-hablar-del-tiempo-y-el-clima/"),
}

# per-unit-bundel, afgeleid uit EJERCICIOS (geen dubbele waarheid)
LINKS = {}
for _eid, (_c, _u, _t, _url) in EJERCICIOS.items():
    LINKS.setdefault((_c, _u), [])
    if (_t, _url) not in LINKS[(_c, _u)]:
        LINKS[(_c, _u)].append((_t, _url))

KLEUR = {"C5": "#1E9E74", "C6+": "#7C3AED", "C4": "#C4402C"}


def qr_svg(url, kleur):
    try:
        import segno
    except ImportError:
        sys.exit("segno ontbreekt:  pip install segno")
    import io
    buf = io.BytesIO()                      # segno schrijft SVG als bytes
    segno.make(url, error="m").save(buf, kind="svg", scale=4, dark=kleur,
                                    light=None, omitsize=True, xmldecl=False, svgns=True)
    return buf.getvalue().decode("utf-8")


def blok(course, unit):
    items = list(LINKS.get((course, unit)) or [])
    for t, u in _extra_links(course, unit):          # door de auteur toegevoegd
        if (t, u) not in items:
            items.append((t, u))
    if not items:
        return None
    kleur = KLEUR.get(course, "#1E9E74")
    kaarten = "".join(
        '<figure class="qx-card">%s<figcaption><span class="qx-t">%s</span>'
        '<span class="qx-u">paginadelespanol.com</span></figcaption></figure>'
        % (qr_svg(url, kleur), titel) for titel, url in items)
    return """<section class="qx" style="--qx:%s">
  <h3 class="qx-h">Práctica extra en línea <span class="qx-nl">· extra online oefenen</span></h3>
  <p class="qx-p">Escanea el código con el móvil. Estas actividades están <strong>en otra web</strong>
     y necesitan internet — los ejercicios de tu curso funcionan también sin conexión.
     <span class="qx-nl">Scan met je gsm. Deze oefeningen staan op een andere website en vragen internet.</span></p>
  <div class="qx-grid">%s</div>
</section>
<style>
.qx{border:1px solid #E4E3DE;border-left:5px solid var(--qx);border-radius:6px;padding:14px 16px;margin:14px 0;background:#FCFBF8}
.qx-h{margin:0 0 4px;font-size:16px;color:#20242E}
.qx-nl{font-weight:400;font-style:italic;color:#6A6E78;font-size:12.5px}
.qx-p{margin:0 0 12px;font-size:13px;color:#4A4E58;max-width:70ch}
.qx-grid{display:flex;flex-wrap:wrap;gap:14px}
.qx-card{margin:0;width:150px;text-align:center;background:#fff;border:1px solid #E4E3DE;border-radius:5px;padding:10px}
.qx-card svg{width:118px;height:118px}
.qx-card figcaption{display:block;margin-top:6px;line-height:1.25}
.qx-t{display:block;font-weight:600;font-size:12.5px;color:#20242E}
.qx-u{display:block;font-size:10px;color:#8A8F99;margin-top:2px}
@media print{.qx{break-inside:avoid}}
</style>""" % (kleur, kaarten)


def balkje(eid):
    """Compacte strook om PAL NAAST de oefening in de cursus te zetten.

    Klein (±58 px QR), één regel hoog, breekt niet over een paginagrens. Draagt het
    oefening-ID als anker zodat print, PDF en hub naar hetzelfde punt verwijzen.
    """
    if eid not in EJERCICIOS:
        return None
    course, unit, titel, url = EJERCICIOS[eid]
    kleur = KLEUR.get(course, "#1E9E74")
    return ('<aside class="qb" id="qr-%s" style="--qb:%s">'
            '<span class="qb-qr">%s</span>'
            '<span class="qb-tx"><b class="qb-t">Más práctica: %s</b>'
            '<span class="qb-s">Escanea y practica en línea '
            '<span class="qb-nl">· scan voor extra online oefening</span></span></span>'
            '<span class="qb-id">%s</span></aside>') % (eid.lower(), kleur, qr_svg(url, kleur), titel, eid)


BALK_CSS = """<style>
.qb{display:flex;align-items:center;gap:12px;margin:10px 0;padding:8px 12px;background:#FCFBF8;
    border:1px solid #E4E3DE;border-left:4px solid var(--qb);border-radius:5px;position:relative}
.qb-qr svg{width:58px;height:58px;display:block}
.qb-tx{display:flex;flex-direction:column;gap:2px;min-width:0}
.qb-t{font-size:13px;color:#20242E;line-height:1.2}
.qb-s{font-size:11.5px;color:#6A6E78}
.qb-nl{font-style:italic}
.qb-id{margin-left:auto;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:9px;
       color:#B6BAC2;letter-spacing:.04em;align-self:flex-start}
@media print{.qb{break-inside:avoid;page-break-inside:avoid}}
@media (max-width:420px){.qb-id{display:none}}
</style>"""


# ---------------------------------------------------------------------------
# Uitbreidbaar linkregister: 03-build/web/qr_links.json
# Alle onderwerpen van de cursus (196) staan daar met een lege `urls`-lijst. Vul je er een
# URL in, dan pikt dit script hem automatisch op — zonder code te wijzigen.
# ---------------------------------------------------------------------------
REG = os.path.join(ROOT, "03-build", "web", "qr_links.json")


def _register():
    import json
    if not os.path.exists(REG):
        return []
    return json.load(open(REG, encoding="utf-8"))


def _extra_links(course, unit):
    """URL's die de auteur in qr_links.json heeft ingevuld."""
    uit = []
    for blok in _register():
        if blok["curso"] == course and blok["unidad"] == unit:
            for o in blok["onderwerpen"]:
                for u in o.get("urls", []):
                    titel = u.get("titulo") or o["onderwerp"]
                    uit.append((titel, u["url"]))
    return uit


def dekking():
    """Welke onderwerpen hebben al een link, welke nog niet?"""
    reg = _register()
    if not reg:
        sys.exit("qr_links.json ontbreekt.")
    tot = met = 0
    print("%-9s %-5s %-7s %s" % ("cursus", "unit", "gelinkt", "onderwerpen zonder link"))
    for b in reg:
        o_met = [o for o in b["onderwerpen"] if o.get("urls")]
        o_zon = [o["onderwerp"] for o in b["onderwerpen"] if not o.get("urls")]
        tot += len(b["onderwerpen"]); met += len(o_met)
        print("%-9s U%-4d %2d/%-4d %s" % (b["curso"], b["unidad"], len(o_met), len(b["onderwerpen"]),
              ", ".join(o_zon[:6]) + (" …" if len(o_zon) > 6 else "")))
    print("\n%d van %d onderwerpen heeft een link (%d%%)." % (met, tot, round(met / tot * 100)))
    print("Blueprint-oefeningen met vaste link: %d (staan los in EJERCICIOS)." % len(EJERCICIOS))


def match(bestand):
    """Stelt links voor door een URL-lijst (sitemap.xml of platte tekst) te matchen op trefwoord.

    De auteur levert de lijst aan — ik kan de site zelf niet bereiken (egress-proxy 403).
    Voorstellen worden in qr_links.json gezet als `urls` met bron «voorstel», zodat je ze
    enkel nog hoeft na te kijken.
    """
    import json, re, unicodedata
    ruw = open(bestand, encoding="utf-8", errors="ignore").read()
    urls = sorted(set(re.findall(r"https?://[^\s<>\"']+", ruw)))
    urls = [u.rstrip("/") + "/" for u in urls if "paginadelespanol" in u]
    print("%d URL's gelezen uit %s" % (len(urls), os.path.basename(bestand)))
    if not urls:
        sys.exit("Geen paginadelespanol-URL's gevonden in dat bestand.")

    def norm(t):
        t = unicodedata.normalize("NFD", t.lower())
        t = "".join(c for c in t if unicodedata.category(c) != "Mn")
        return re.sub(r"[^a-z0-9]+", " ", t).strip()

    STOP = {"de", "la", "el", "los", "las", "y", "con", "para", "del", "en", "un", "una"}
    reg = _register()
    voorstellen = 0
    for b in reg:
        for o in b["onderwerpen"]:
            if o.get("urls"):
                continue
            woorden = [w for w in norm(o["onderwerp"]).split() if len(w) > 3 and w not in STOP]
            if not woorden:
                continue
            beste, score = None, 0
            for u in urls:
                slug = " " + norm(u.split("paginadelespanol.com/")[-1]) + " "
                # heel woord in de slug telt zwaar; deelwoord telt licht
                tref = 0
                for w in woorden:
                    if " " + w + " " in slug:
                        tref += 2
                    elif w in slug and len(w) >= 7:
                        tref += 1
                if tref > score:
                    beste, score = u, tref
            # drempel: minstens één VOLLEDIG woord raak, anders geen voorstel
            if beste and score >= 2:
                o["urls"] = [{"titulo": o["onderwerp"], "url": beste, "bron": "voorstel"}]
                voorstellen += 1
    json.dump(reg, open(REG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("%d voorstellen weggeschreven naar qr_links.json (bron: «voorstel» — nakijken!)" % voorstellen)


def check():
    ctx = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt") \
        if os.path.exists("/root/.ccr/ca-bundle.crt") else ssl.create_default_context()
    h = [urllib.request.HTTPSHandler(context=ctx)]
    px = os.environ.get("HTTPS_PROXY")
    if px:
        h.append(urllib.request.ProxyHandler({"https": px, "http": px}))
    op = urllib.request.build_opener(*h)
    gezien, stuk = set(), []
    for (c, u), items in sorted(LINKS.items()):
        for titel, url in items:
            if url in gezien:
                continue
            gezien.add(url)
            try:
                req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
                with op.open(req, timeout=20) as r:
                    print("  %3d  %s" % (r.status, url))
            except Exception as e:
                stuk.append((url, str(e)[:60]))
                print("  ✗    %s — %s" % (url, str(e)[:60]))
    print("\n%d unieke links · %d onbereikbaar" % (len(gezien), len(stuk)))
    return 1 if stuk else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("course", nargs="?")
    ap.add_argument("units", nargs="*", type=int)
    ap.add_argument("--alle", action="store_true")
    ap.add_argument("--check", action="store_true", help="controleer of de links nog leven")
    ap.add_argument("--balkjes", action="store_true", help="compacte strook per OEFENING (naast de oefening in de cursus)")
    ap.add_argument("--oefening", help="één balkje voor dit oefening-ID")
    ap.add_argument("--dekking", action="store_true", help="welke onderwerpen hebben al een link?")
    ap.add_argument("--match", metavar="BESTAND", help="stel links voor uit een sitemap/URL-lijst")
    a = ap.parse_args()
    if a.dekking:
        dekking(); sys.exit(0)
    if a.match:
        match(a.match); sys.exit(0)
    if a.check:
        sys.exit(check())
    if a.oefening or a.balkjes:
        os.makedirs(OUT, exist_ok=True)
        ids = [a.oefening] if a.oefening else sorted(EJERCICIOS)
        onbekend = [i for i in ids if i not in EJERCICIOS]
        if onbekend:
            sys.exit("Onbekend oefening-ID: %s" % ", ".join(onbekend))
        stukken = []
        for eid in ids:
            html = balkje(eid)
            p = os.path.join(OUT, "balk_%s.html" % eid.replace("+", "plus"))
            open(p, "w", encoding="utf-8").write(html + BALK_CSS)
            stukken.append(html)
            print("  ✓ %-26s → %s" % (eid, os.path.relpath(p, ROOT)))
        # één overzichtsbestand om de vormgeving in één keer te bekijken
        prev = os.path.join(OUT, "_balkjes_overzicht.html")
        open(prev, "w", encoding="utf-8").write(
            "<h2 style='font:600 18px system-ui;margin:16px 0 4px'>QR-balkjes per oefening</h2>"
            "<p style='font:13px system-ui;color:#6A6E78;margin:0 0 14px'>%d stuks — zo staan ze straks "
            "naast de oefening in de cursus.</p>%s%s" % (len(stukken), "".join(stukken), BALK_CSS))
        print("  → overzicht: %s" % os.path.relpath(prev, ROOT))
        sys.exit(0)
    taken = sorted(LINKS) if a.alle else [(a.course, u) for u in a.units]
    if not taken or not taken[0][0]:
        sys.exit("Gebruik: gen_qr_extra.py C5 0 [1 2 …]  |  --alle  |  --check")
    os.makedirs(OUT, exist_ok=True)
    for course, unit in taken:
        html = blok(course, unit)
        if not html:
            print("  – geen links voor %s U%s" % (course, unit)); continue
        p = os.path.join(OUT, "%s_U%d_extra.html" % (course.replace("+", "plus"), unit))
        open(p, "w", encoding="utf-8").write(html)
        print("  ✓ %s U%d → %s (%d link(s))"
              % (course, unit, os.path.relpath(p, ROOT), len(LINKS[(course, unit)])))


if __name__ == "__main__":
    main()
