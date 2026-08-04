#!/usr/bin/env python3
"""Docentendossier «Guion y clave» — alle audioscripts en antwoordsleutels van één cursus.

Waarom een apart dossier en niet in de cursus zelf: de antwoordsleutel mag niet
op de leerlingpagina staan (CLAUDE.md §14) en de hub geeft alleen zelfcorrectie,
geen lijst met oplossingen. De leerkracht heeft die lijst wél nodig — zeker nu de
mp3's nog niet bestaan: dan is het `guion` meteen het voorleesscript.

Het dossier bundelt per unit:
  * het lange luisterfragment (`escucha_data.py`) — guion + de sleutel van de
    zes treden (globaal, vijf detailvragen, juist/fout met bewijs);
  * de korte audiotaken (`escucha_corta_data.py`) — guion + `clave` + `nota`.

    python3 03-build/web/gen_docente_audio.py            # C5 en C6+
    python3 03-build/web/gen_docente_audio.py C5         # enkel C5

Uitvoer: 03-build/web/print/<cursus>_docente_audio.html (+ .pdf als Chromium er is).
Render zelf:
    chromium --headless --no-sandbox --disable-gpu --no-pdf-header-footer \\
      --print-to-pdf=03-build/web/print/C5_docente_audio.pdf \\
      "file://…/03-build/web/print/C5_docente_audio.html"
"""
import base64
import html
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(HERE, "print")
sys.path.insert(0, HERE)

import escucha_data as ED           # noqa: E402
import escucha_corta_data as EC     # noqa: E402

E = lambda s: html.escape(s or "")

# Cursuskleur volgt de huisstijl: C5 groen, C6+ paars (CLAUDE.md §6).
CURSOS = {
    "C5":  {"slug": "C5", "nombre": "Español en la práctica",
            "sub": "C5 · 5de jaar", "g": "#1E9E74", "gd": "#157355", "gt": "#E4F4EE",
            "unidades": range(0, 9)},
    "C6+": {"slug": "C6plus", "nombre": "Más español en la práctica · edición única",
            "sub": "C6+ · 6de jaar", "g": "#7C5CBF", "gd": "#5B3F96", "gt": "#EEE9F9",
            "unidades": range(0, 8)},
}

PARADA = {
    ("C5", 0): "El mundo hispano → España", ("C5", 1): "Madrid",
    ("C5", 2): "Andalucía · Sevilla", ("C5", 3): "Barcelona",
    ("C5", 4): "València · la costa", ("C5", 5): "México · CDMX",
    ("C5", 6): "México · mercados", ("C5", 7): "Colombia · Cartagena",
    ("C5", 8): "Perú · Cusco",
}


def _face(fam, fichero, peso):
    ruta = os.path.join(ROOT, "02-huisstijl", "fonts", fichero)
    b64 = base64.b64encode(open(ruta, "rb").read()).decode()
    return ("@font-face{font-family:'%s';src:url(data:font/woff2;base64,%s) "
            "format('woff2');font-weight:%s;font-display:swap}" % (fam, b64, peso))


FONTS = "".join([
    _face("Bricolage Grotesque", "BricolageGrotesque-700.woff2", "700"),
    _face("Bricolage Grotesque", "BricolageGrotesque-800.woff2", "800"),
    _face("Inter", "Inter-400.woff2", "400"),
    _face("Inter", "Inter-600.woff2", "600"),
    _face("Caveat", "Caveat-700.woff2", "700"),
])

CSS = r"""
@page{ size:A4; margin:14mm 12mm; }
@page:first{ margin:0 0 14mm 0; }
*{ box-sizing:border-box; }
html{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }
body{ margin:0; font-family:'Inter',sans-serif; color:var(--ink); font-size:10.5pt; line-height:1.45; }
h1,h2,h3,h4{ font-family:'Bricolage Grotesque',sans-serif; margin:0; }

/* omslag */
.tapa{ background:var(--g); color:#fff; padding:26mm 16mm 16mm; margin-bottom:10mm; }
.tapa .kicker{ font-size:11pt; letter-spacing:.14em; text-transform:uppercase; opacity:.88; }
.tapa h1{ font-size:34pt; font-weight:800; line-height:1.05; margin:4mm 0 3mm; }
.tapa .sub{ font-size:13pt; opacity:.95; }
.tapa .aviso{ background:#ffffff26; border-radius:5mm; padding:5mm 6mm; margin-top:8mm; font-size:10pt; }
.tapa .aviso b{ color:#fff; }

.wrap{ padding:0 2mm; }
.intro{ background:var(--gt); border-radius:4mm; padding:5mm 6mm; margin:0 0 8mm; }
.intro h3{ font-size:12pt; color:var(--gd); margin-bottom:2mm; }
.intro ul{ margin:2mm 0 0; padding-left:5mm; }
.intro li{ margin:1mm 0; }

/* overzichtstabel */
table.res{ width:100%; border-collapse:collapse; font-size:9pt; margin:0 0 8mm; }
table.res th{ background:var(--gt); color:var(--gd); text-align:left; padding:2mm 2.5mm; font-size:8.5pt;
  text-transform:uppercase; letter-spacing:.06em; }
table.res td{ border-bottom:1px solid var(--line); padding:2mm 2.5mm; vertical-align:top; }
table.res tr{ break-inside:avoid; }

/* unit */
.unidad{ break-before:page; }
.uhead{ display:flex; align-items:baseline; gap:4mm; border-bottom:2.5px solid var(--g);
  padding-bottom:2mm; margin-bottom:5mm; }
.uhead .num{ font-family:'Bricolage Grotesque',sans-serif; font-weight:800; font-size:26pt;
  color:var(--g); line-height:1; }
.uhead h2{ font-size:16pt; color:var(--gd); }
.uhead .parada{ margin-left:auto; font-size:9pt; color:var(--mut); font-style:italic; }

/* fragment */
.frag{ border:1px solid var(--line); border-radius:4mm; padding:4mm 5mm; margin:0 0 6mm;
  break-inside:avoid; }
.frag.largo{ border-left:4mm solid var(--g); }
.frag.corto{ border-left:4mm solid var(--gt); }
.fcab{ display:flex; gap:2.5mm; align-items:center; flex-wrap:wrap; margin-bottom:1.5mm; }
.et{ background:var(--g); color:#fff; border-radius:999px; padding:1mm 3mm; font-size:8pt; font-weight:700; }
.et.b{ background:var(--gd); }
.sec{ font-size:8.5pt; color:var(--mut); font-weight:600; }
.tipo{ font-size:8pt; color:var(--mut); border:1px solid var(--line); border-radius:999px; padding:.6mm 2.5mm; }
.frag h3{ font-size:12.5pt; color:var(--ink); margin:0 0 1mm; }
.tarea{ font-size:9.5pt; color:var(--mut); margin:0 0 3mm; }

table.gui{ width:100%; border-collapse:collapse; font-size:9.5pt; margin:0 0 3mm; }
table.gui td{ padding:1.4mm 2mm; border-bottom:1px solid var(--line); vertical-align:top; }
table.gui tr:last-child td{ border-bottom:none; }
td.who{ width:26mm; font-size:8pt; font-weight:700; color:var(--gd); text-transform:uppercase;
  letter-spacing:.04em; padding-top:2mm; }
td.es{ }
td.nl{ width:38%; color:var(--mut); font-style:italic; font-size:9pt; }

.clave{ background:var(--gt); border-radius:3mm; padding:3mm 4mm; font-size:9.5pt; }
.clave h4{ font-size:9pt; color:var(--gd); text-transform:uppercase; letter-spacing:.07em;
  margin-bottom:1.5mm; }
.clave ol,.clave ul{ margin:0; padding-left:5mm; }
.clave li{ margin:.8mm 0; }
.nota{ border-left:3px solid var(--amber); background:var(--amberbg); border-radius:0 3mm 3mm 0;
  padding:2.5mm 4mm; font-size:9pt; margin-top:3mm; }
.nota b{ color:#8A6508; }
.sinaudio{ border-left:3px solid var(--red); background:#FEF2F2; border-radius:0 3mm 3mm 0;
  padding:2.5mm 4mm; font-size:9pt; }
.pie{ margin-top:8mm; padding-top:3mm; border-top:1px solid var(--line); font-size:8.5pt; color:var(--mut); }
"""

TOKENS = ":root{--ink:#20242E;--mut:#6A6E78;--line:#E4E3DE;--red:#DC2626;--amber:#B7860B;" \
         "--amberbg:#FBF3D6;--g:%s;--gd:%s;--gt:%s;}"


def guion_html(guion):
    filas = "".join(
        "<tr><td class='who'>%s</td><td class='es'>%s</td><td class='nl'>%s</td></tr>"
        % (E(l["who"]), E(l["es"]), E(l["nl"])) for l in guion)
    return "<table class='gui'>%s</table>" % filas


def clave_html(items, titulo="Clave"):
    return ("<div class='clave'><h4>%s</h4><ul>%s</ul></div>"
            % (E(titulo), "".join("<li>%s</li>" % E(x) for x in items)))


def largo_html(frag):
    """Het lange luisterfragment: guion + de sleutel van de zes treden."""
    S = frag["situacion"]
    clave = ["Globaal: %s — %s" % (frag["global"]["q"], frag["global"]["ans"])]
    for i, d in enumerate(frag["detalle"], 1):
        clave.append("Detail %d: %s — %s%s"
                     % (i, d["q"], d["ans"], "  (%s)" % d["why"] if d.get("why") else ""))
    for v in frag["vf"]:
        clave.append("V/F: %s — %s · bewijs: «%s»"
                     % (v["q"], "verdadero" if v["ans"] else "falso", v["prueba"]))
    clave.append("Productie: %s" % frag["produccion"]["prompt"])
    return (
        "<div class='frag largo'>"
        "<div class='fcab'><span class='et b'>%s</span>"
        "<span class='sec'>§ Escucha · begripsladder</span>"
        "<span class='tipo'>lang fragment</span></div>"
        "<h3>%s</h3>"
        "<p class='tarea'><b>¿Dónde?</b> %s · <b>¿Quién?</b> %s · <b>¿Qué?</b> %s</p>"
        "%s%s</div>"
        % (E(frag["id"]), E(frag["titulo"]), E(S["lugar"]), E(S["quien"]), E(S["que"]),
           guion_html(frag["guion"]), clave_html(clave, "Clave — de zes treden")))


def corto_html(frag):
    if not frag["guion"]:
        return ("<div class='frag corto'>"
                "<div class='fcab'><span class='et'>%s</span><span class='sec'>%s</span>"
                "<span class='tipo'>%s</span></div><h3>%s</h3>"
                "<p class='tarea'>%s</p>"
                "<div class='sinaudio'><b>Geen script en geen opname.</b> %s</div>"
                "%s</div>"
                % (E(frag["etiqueta"]), E(frag["seccion"]), E(frag["tipo"]), E(frag["titulo"]),
                   E(frag["tarea"]), E(frag.get("nota", "")), clave_html(frag["clave"])))
    nota = ("<div class='nota'><b>Nota voor de bouw:</b> %s</div>" % E(frag["nota"])) \
        if frag.get("nota") else ""
    return ("<div class='frag corto'>"
            "<div class='fcab'><span class='et'>%s</span><span class='sec'>%s</span>"
            "<span class='tipo'>%s</span></div><h3>%s</h3>"
            "<p class='tarea'>%s</p>%s%s%s</div>"
            % (E(frag["etiqueta"]), E(frag["seccion"]), E(frag["tipo"]), E(frag["titulo"]),
               E(frag["tarea"]), guion_html(frag["guion"]),
               clave_html(frag["clave"]), nota))


def resumen_html(curso, cfg):
    filas = []
    for u in cfg["unidades"]:
        largo = ED.TODOS.get((curso, u))
        cortos = EC.CORTOS.get((curso, u), [])
        con = [c for c in cortos if c["guion"]]
        filas.append(
            "<tr><td><b>U%d</b></td><td>%s</td><td>%s</td><td>%d</td><td>%d</td></tr>"
            % (u, E(PARADA.get((curso, u), "—")), E(largo["titulo"] if largo else "—"),
               len(con), sum(len(c["guion"]) for c in con) + (len(largo["guion"]) if largo else 0)))
    return ("<table class='res'><thead><tr><th>Unit</th><th>Parada</th>"
            "<th>Lang fragment</th><th>Korte taken</th><th>Regels totaal</th></tr></thead>"
            "<tbody>%s</tbody></table>" % "".join(filas))


def build(curso):
    cfg = CURSOS[curso]
    unidades = []
    for u in cfg["unidades"]:
        largo = ED.TODOS.get((curso, u))
        cortos = EC.CORTOS.get((curso, u), [])
        if not largo and not cortos:
            continue
        cuerpo = (largo_html(largo) if largo else "") + \
                 "".join(corto_html(c) for c in cortos)
        unidades.append(
            "<section class='unidad'><div class='uhead'><span class='num'>%d</span>"
            "<h2>Unidad %d</h2><span class='parada'>%s</span></div>%s</section>"
            % (u, u, E(PARADA.get((curso, u), "")), cuerpo))

    n_frag = sum(1 for u in cfg["unidades"]
                 for _ in EC.CORTOS.get((curso, u), [])) + \
        sum(1 for u in cfg["unidades"] if ED.TODOS.get((curso, u)))

    doc = (
        "<!doctype html><html lang='nl'><head><meta charset='utf-8'>"
        "<title>%s — Guion y clave (docentendossier)</title>"
        "<style>%s%s%s</style></head><body>"
        "<div class='tapa'><div class='kicker'>Docentendossier · audio</div>"
        "<h1>Guion y clave</h1>"
        "<div class='sub'>%s · %s</div>"
        "<div class='aviso'><b>Niet voor de leerling.</b> Dit dossier bevat de volledige "
        "audioteksten én de antwoordsleutels. Zolang er nog geen opnames zijn, is het "
        "<i>guion</i> meteen het voorleesscript: lees het tempo rustig, elk dictee-item "
        "twee keer, met een pauze. De leerling hoort dezelfde tekst op de digitale pagina "
        "via de computerstem, en krijgt het transcript daar pas te zien ná twee keer "
        "luisteren.</div></div>"
        "<div class='wrap'>"
        "<div class='intro'><h3>Wat staat hierin</h3><ul>"
        "<li><b>%d fragmenten</b> over %d units: per unit het lange luisterfragment "
        "(begripsladder) en de korte audiotaken die op papier achter een QR-code staan.</li>"
        "<li>Elk fragment: het <b>etiket zoals het in het boek staat</b>, de opdracht, "
        "het volledige guion (Spaans + Nederlandse steun) en de <b>clave</b>.</li>"
        "<li>Een <b>nota</b> in oker is een aandachtspunt voor wie de unit herbouwt — "
        "meestal een plek waar de gedrukte oefening niet klopt met haar eigen instructie.</li>"
        "<li>Een <b>rood kader</b> betekent: bewust geen eigen script en geen opname "
        "(bestaande muziek — extern afspelen).</li>"
        "</ul></div>%s%s"
        "<p class='pie'>Bron: <code>03-build/web/escucha_data.py</code> en "
        "<code>03-build/web/escucha_corta_data.py</code>. Dit dossier wordt gegenereerd — "
        "pas de bron aan, niet dit bestand.</p>"
        "</div></body></html>"
        % (E(cfg["nombre"]), FONTS, TOKENS % (cfg["g"], cfg["gd"], cfg["gt"]), CSS,
           E(cfg["nombre"]), E(cfg["sub"]),
           n_frag, len(list(cfg["unidades"])),
           resumen_html(curso, cfg), "".join(unidades)))

    os.makedirs(OUT, exist_ok=True)
    ruta = os.path.join(OUT, "%s_docente_audio.html" % cfg["slug"])
    open(ruta, "w", encoding="utf-8").write(doc)
    print("%-4s → %s (%d KB · %d fragmenten)"
          % (curso, os.path.relpath(ruta, ROOT), len(doc) / 1024, n_frag))
    return ruta


def a_pdf(ruta_html):
    import glob
    candidatos = ["chromium", "chromium-browser", "google-chrome"]
    # De sandbox heeft geen chromium op het pad, wel de Playwright-build.
    candidatos += sorted(glob.glob("/opt/pw-browsers/chromium*/chrome-linux/chrome"))
    chrome = next((c for c in candidatos if shutil.which(c) or os.path.exists(c)), None)
    if not chrome:
        print("     (geen Chromium gevonden — render de PDF zelf, zie de docstring)")
        return
    pdf = ruta_html[:-5] + ".pdf"
    subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu",
                    "--no-pdf-header-footer", "--print-to-pdf=" + pdf,
                    "file://" + ruta_html], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("     → %s (%d KB)" % (os.path.relpath(pdf, ROOT), os.path.getsize(pdf) / 1024))


if __name__ == "__main__":
    cursos = sys.argv[1:] or list(CURSOS)
    for c in cursos:
        if c not in CURSOS:
            sys.exit("Onbekende cursus: %s (kies uit %s)" % (c, ", ".join(CURSOS)))
        a_pdf(build(c))
