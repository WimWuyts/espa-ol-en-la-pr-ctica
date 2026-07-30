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

# Bron: de twee blueprints (00-brondocumenten/gap-analyse/). Titel = wat de leerling ziet.
LINKS = {
    ("C5", 0): [("Los números del 0 al 10", B + "los-numeros-del-0-al-10/"),
                ("Los números del 10 al 20", B + "los-numeros-del-10-al-20/")],
    ("C5", 1): [("Nacionalidades del mundo hispano", B + "nacionalidades-de-los-paises-hispanohablantes/")],
    ("C5", 2): [("Adjetivos posesivos", B + "adjetivos-posesivos/")],
    ("C5", 3): [("Verbos reflexivos", B + "utiliza-estos-verbos-reflexivos/")],
    ("C5", 4): [("El verbo gustar y similares", B + "25-frases-para-practicar-el-verbo-gustar-y-similares/")],
    ("C5", 5): [("Verbos para cocinar", B + "20-verbos-cocinar-espanol/"),
                ("Adjetivos sobre la comida", B + "completa-frases-con-adjetivos-comida/")],
    ("C5", 6): [("Verbos para hablar de la ropa", B + "20-verbos-para-hablar-sobre-la-ropa/"),
                ("Palabras de moda", B + "25-palabras-relacionadas-con-la-moda/")],
    ("C5", 7): [("Sopa de letras: la casa", B + "sopa-de-letras-15-palabras-relacionadas-con-la-casa/"),
                ("El imperativo", B + "25-frases-para-practicar-el-imperativo/")],
    ("C5", 8): [("El pretérito perfecto", B + "20-frases-para-practicar-el-preterito-perfecto/")],

    ("C6+", 0): [("Nacionalidades del mundo hispano", B + "nacionalidades-de-los-paises-hispanohablantes/")],
    ("C6+", 1): [("Ser y estar", B + "30-frases-para-practicar-los-verbos-ser-y-estar/"),
                 ("Verbos reflexivos", B + "utiliza-estos-verbos-reflexivos/")],
    ("C6+", 2): [("Sopa de letras: la casa", B + "sopa-de-letras-15-palabras-relacionadas-con-la-casa/")],
    ("C6+", 3): [("El futuro próximo (ir a + inf.)", B + "25-frases-para-practicar-el-futuro-proximo/")],
    ("C6+", 4): [("El pretérito perfecto", B + "20-frases-para-practicar-el-preterito-perfecto/"),
                 ("Participios irregulares", B + "20-participios-irregulares/")],
    ("C6+", 5): [("El pretérito indefinido", B + "30-frases-para-practicar-el-preterito-indefinido/")],
    ("C6+", 6): [("El pretérito imperfecto", B + "25-frases-para-practicar-el-preterito-imperfecto/")],
    ("C6+", 7): [("El imperativo", B + "25-frases-para-practicar-el-imperativo/"),
                 ("Verbos del tiempo y el clima", B + "25-verbos-para-hablar-del-tiempo-y-el-clima/")],
}
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
    items = LINKS.get((course, unit))
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
    a = ap.parse_args()
    if a.check:
        sys.exit(check())
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
