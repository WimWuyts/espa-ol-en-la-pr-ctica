#!/usr/bin/env python3
"""Docentendossier «Retos · clave y montaje» — de tien retos per unit, mét sleutel.

De retos leven op drie dragers: in het boek (volledige oefening), op de digitale
pagina (zelfcorrigerend) en in de PowerPoint (klik-onthulling). De antwoordsleutel
staat op géén van de drie — dat mag niet (CLAUDE.md §14). Voor de PowerPoint-retos
zit ze in de spreker-notities; voor print en hub bestond ze tot nu enkel in de
bron. Dit dossier maakt ze leesbaar voor wie voor de klas staat.

Per reto: waar hij leeft, de lens, de beperking («la regla del reto»), het verloop,
het materiaal dat de leerling krijgt, en de clave — inclusief de valstrikken die
de reto expres legt.

    python3 03-build/web/gen_docente_retos.py          # C5 en C6+
    python3 03-build/web/gen_docente_retos.py C5       # enkel C5

Uitvoer: 03-build/web/print/<cursus>_docente_retos.html (+ .pdf als Chromium er is).
"""
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(HERE, "print")
sys.path.insert(0, HERE)

import retos_data as RD                 # noqa: E402
from gen_docente_audio import (         # noqa: E402
    CURSOS, FONTS, TOKENS, CSS as CSS_BASE, PARADA, a_pdf)

E = lambda s: html.escape(s or "")

DONDE = {"print": ("📄", "In het boek", "de volledige oefening staat in de printcursus"),
         "hub": ("🎮", "Op de digitale pagina", "tabblad «Retos», met zelfcorrectie"),
         "ppt": ("📊", "In de PowerPoint", "klassikaal, met klik-onthulling")}

CSS = CSS_BASE + r"""
/* ── retodossier ─────────────────────────────────────────────────────────── */
.reto{ border:1px solid var(--line); border-radius:4mm; padding:4mm 5mm; margin:0 0 6mm;
  break-inside:avoid; }
.reto.print{ border-left:4mm solid var(--g); }
.reto.hub{ border-left:4mm solid var(--gd); }
.reto.ppt{ border-left:4mm solid var(--gt); }
.rc{ display:flex; gap:2.5mm; align-items:center; flex-wrap:wrap; margin-bottom:1.5mm; }
.rc .n{ background:var(--g); color:#fff; width:7mm; height:7mm; border-radius:50%;
  display:flex; align-items:center; justify-content:center; font-weight:700; font-size:9pt;
  font-family:'Bricolage Grotesque',sans-serif; flex:none; }
.reto h3{ font-size:12.5pt; color:var(--ink); margin:0; }
.rdonde{ margin-left:auto; font-size:8.5pt; color:var(--mut); }
.rmeta{ font-size:8.5pt; color:var(--mut); margin:0 0 2.5mm; }
.rgancho{ font-size:10.5pt; margin:0 0 .6mm; }
.rgancho b{ color:var(--gd); }
.rnl{ font-size:9pt; color:var(--mut); font-style:italic; margin:0 0 2.5mm; }
.regla{ border-left:3px solid var(--amber); background:var(--amberbg); border-radius:0 3mm 3mm 0;
  padding:2.5mm 4mm; font-size:9.5pt; margin:0 0 3mm; }
.regla b{ color:#8A6508; text-transform:uppercase; letter-spacing:.06em; font-size:8pt; }
.pasos{ margin:0 0 3mm; padding-left:5mm; font-size:9.5pt; }
.pasos li{ margin:.8mm 0; }
.pasos .nl{ color:var(--mut); font-style:italic; font-size:8.6pt; }
.mat{ font-size:8.8pt; color:var(--mut); margin:0 0 2.5mm; }
.mat b{ color:var(--ink); }
"""


def reto_html(r):
    icono, donde, uitleg = DONDE[r["soporte"]]
    pasos = "".join("<li>%s <span class='nl'>%s</span></li>" % (E(es), E(nl))
                    for es, nl in r["pasos"])
    # wat de leerling in handen krijgt — handig bij het klaarzetten van de les
    mat = " · ".join("%s (%d)" % (k, len(v)) if isinstance(v, (list, tuple)) else str(k)
                     for k, v in r["datos"].items())
    clave = "".join("<li>%s</li>" % E(c) for c in r["clave"])
    nota = ("<div class='nota'><b>Nota:</b> %s</div>" % E(r["nota"])) if r.get("nota") else ""
    return (
        "<div class='reto %s'>"
        "<div class='rc'><span class='n'>%d</span><h3>%s</h3>"
        "<span class='rdonde'>%s %s — %s</span></div>"
        "<p class='rmeta'>%s · %s · %s · %s · %s</p>"
        "<p class='rgancho'><b>%s</b></p><p class='rnl'>%s</p>"
        "<div class='regla'><b>La regla del reto</b><br>%s</div>"
        "<ol class='pasos'>%s</ol>"
        "<p class='mat'><b>Materiaal:</b> %s</p>"
        "<div class='clave'><h4>Clave — en wat de reto expres verstopt</h4><ul>%s</ul></div>"
        "%s</div>"
        % (r["soporte"], r["num"], E(r["nombre"]), icono, E(donde), E(uitleg),
           E(r["seccion"]), E(r["lente"]), E(r["skill"]), E(r["forma"]),
           "%s · %s" % (E(r["tiempo"]), E(r["dificultad"])),
           E(r["gancho_es"]), E(r["gancho_nl"]), E(r["regla"]), pasos, E(mat), clave, nota))


def resumen_html(curso, cfg):
    filas = []
    for u in cfg["unidades"]:
        retos = RD.de(curso, u)
        if not retos:
            continue
        por = {s: [str(r["num"]) for r in retos if r["soporte"] == s]
               for s in ("print", "hub", "ppt")}
        filas.append(
            "<tr><td><b>U%d</b></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
            % (u, E(PARADA.get((curso, u), "—")),
               ", ".join(por["print"]) or "—", ", ".join(por["hub"]) or "—",
               ", ".join(por["ppt"]) or "—"))
    if not filas:
        return ""
    return ("<table class='res'><thead><tr><th>Unit</th><th>Parada</th>"
            "<th>📄 In het boek</th><th>🎮 Digitale pagina</th><th>📊 PowerPoint</th>"
            "</tr></thead><tbody>%s</tbody></table>" % "".join(filas))


def build(curso):
    cfg = CURSOS[curso]
    unidades, total = [], 0
    for u in cfg["unidades"]:
        retos = RD.de(curso, u)
        if not retos:
            continue
        total += len(retos)
        unidades.append(
            "<section class='unidad'><div class='uhead'><span class='num'>%d</span>"
            "<h2>Unidad %d · retos</h2><span class='parada'>%s</span></div>%s</section>"
            % (u, u, E(PARADA.get((curso, u), "")), "".join(reto_html(r) for r in retos)))
    if not unidades:
        print("%-4s — nog geen retos" % curso)
        return None

    doc = (
        "<!doctype html><html lang='nl'><head><meta charset='utf-8'>"
        "<title>%s — Retos, clave y montaje (docentendossier)</title>"
        "<style>%s%s%s</style></head><body>"
        "<div class='tapa'><div class='kicker'>Docentendossier · retos</div>"
        "<h1>Retos · clave y montaje</h1>"
        "<div class='sub'>%s · %s</div>"
        "<div class='aviso'><b>Niet voor de leerling.</b> Elke reto heeft één harde "
        "beperking en meestal een valstrik die je niet mag verklappen. Hier staat wat die "
        "valstrik is, wat het juiste antwoord is, en waar de reto leeft: in het boek, op de "
        "digitale pagina of in de PowerPoint. Van de PowerPoint-retos vind je dezelfde "
        "sleutel ook in de spreker-notities van de dia.</div></div>"
        "<div class='wrap'>"
        "<div class='intro'><h3>Hoe je dit leest</h3><ul>"
        "<li><b>%d retos</b> over %d units — tien per unit, verdeeld over drie dragers.</li>"
        "<li>Een reto staat <b>op één drager voluit</b>. In de twee andere formaten staat "
        "alleen een verwijskaartje: een veiling of een opnameoefening half op papier zetten "
        "helpt niemand.</li>"
        "<li><b>La regla del reto</b> is de beperking die de oefening zijn scherpte geeft. "
        "Laat ze vallen en de oefening wordt een gewone invuloefening.</li>"
        "<li>De <b>clave</b> geeft naast het antwoord ook waar de klas normaal struikelt.</li>"
        "</ul></div>%s%s"
        "<p class='pie'>Bron: <code>03-build/web/retos_data.py</code> — dezelfde bron als "
        "print, hub en PowerPoint. Dit dossier wordt gegenereerd; pas de bron aan, niet dit "
        "bestand.</p></div></body></html>"
        % (E(cfg["nombre"]), FONTS, TOKENS % (cfg["g"], cfg["gd"], cfg["gt"]), CSS,
           E(cfg["nombre"]), E(cfg["sub"]), total, len(unidades),
           resumen_html(curso, cfg), "".join(unidades)))

    os.makedirs(OUT, exist_ok=True)
    ruta = os.path.join(OUT, "%s_docente_retos.html" % cfg["slug"])
    open(ruta, "w", encoding="utf-8").write(doc)
    print("%-4s → %s (%d KB · %d retos)"
          % (curso, os.path.relpath(ruta, ROOT), len(doc) / 1024, total))
    return ruta


if __name__ == "__main__":
    for c in (sys.argv[1:] or list(CURSOS)):
        if c not in CURSOS:
            sys.exit("Onbekende cursus: %s (kies uit %s)" % (c, ", ".join(CURSOS)))
        ruta = build(c)
        if ruta:
            a_pdf(ruta)
