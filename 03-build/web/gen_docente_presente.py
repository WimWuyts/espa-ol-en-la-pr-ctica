#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Docentendossier «Cien formas · clave» — de sleutel bij C5 U1 §3.3.

De honderd invulvormen staan in het boek (§3.3) en zelfcorrigerend op de
digitale pagina. De antwoordsleutel staat op geen van beide: oplossingen horen
niet op de leerlingbladzijde (CLAUDE.md §14). Dit blad is voor wie voor de klas
staat — of voor de leerling die achteraf zijn werk mag nakijken.

De honderd vormen zijn nagerekend tegen de uitgangen van het presente regular;
de sleutel hieronder komt uit dezelfde gegevens als het boek, dus ze kunnen niet
uit elkaar lopen.

    python3 03-build/web/gen_docente_presente.py

Uitvoer: 03-build/web/print/C5_U1_docente_presente.html (+ .pdf als Chromium er is).
"""
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(HERE, "print")
sys.path.insert(0, HERE)

import presente_data as PD              # noqa: E402
from gen_docente_audio import CURSOS, FONTS, TOKENS, CSS as CSS_BASE, a_pdf  # noqa: E402

E = lambda s: html.escape(s or "")
C5 = CURSOS["C5"]

CSS = CSS_BASE + r"""
/* ── clave van de honderd vormen ─────────────────────────────────────────── */
.clave{ display:grid; grid-template-columns:repeat(4,1fr); gap:0 6mm; margin:3mm 0 6mm; }
.clave div{ font-size:9.4pt; padding:.9mm 0; border-bottom:1px solid var(--line);
            display:flex; gap:3mm; }
.clave b{ color:var(--gd); min-width:8mm; text-align:right; font-variant-numeric:tabular-nums; }
.bloque{ margin:0 0 4mm; }
.bloque h3{ font-family:var(--disp); font-size:12pt; color:var(--gd); margin:5mm 0 1mm; }
.bloque p{ margin:0 0 1mm; font-size:9.6pt; }
.frase{ font-size:9.4pt; padding:.7mm 0 .7mm 8mm; text-indent:-8mm; }
.frase b{ color:var(--gd); }
.frase i{ color:var(--mut); }
.sol{ background:var(--gt); color:var(--gd); border-radius:2pt; padding:0 1.4mm; font-weight:700; }
"""


def portada():
    return (
        '<div class="hero"><div class="tab">C5 · UNIDAD 1 · DOCENTE</div>'
        '<h1>Cien formas · la clave</h1>'
        '<p>De honderd invulvormen van <b>§3.3 · Cien formas</b> met hun oplossing. '
        'Ze staan in het boek zonder sleutel en op de digitale pagina met zelfcorrectie; '
        'dit blad is het enige waar ze samen staan.</p></div>')


def resumen():
    return (
        '<div class="nota"><b>Waar het over gaat.</b> Alleen <b>presente regular</b>: '
        '-ar, -er en -ir, zonder één stamklinkerwisseling. Dat is met opzet — de <i>bota</i> '
        '(e→ie, o→ue, e→i) komt pas in U3, en wie die twee door elkaar oefent, leert geen van '
        'beide. De valstrik van deze reeks zit elders: <b>het onderwerp staat soms een zin '
        'eerder</b> (de tekstjes 61–100) of het is een groep die als enkelvoud telt '
        '(<i>la gente baila</i>, <i>el equipo entrena</i>).</div>')


def bloques():
    out = []
    for tit_es, tit_nl, items in PD.SUELTAS:
        out.append('<div class="bloque"><h3>%s</h3><p class="nl">%s</p>' % (E(tit_es), E(tit_nl)))
        for n, q, inf, a in items:
            out.append('<div class="frase"><b>%d.</b> %s <i>(%s)</i></div>'
                       % (n, E(q).replace("{}", '<span class="sol">%s</span>' % E(a)), E(inf)))
        out.append("</div>")
    for tit_es, tit_nl, cuerpo, huecos in PD.TEXTOS:
        out.append('<div class="bloque"><h3>%s</h3><p class="nl">%s</p>' % (E(tit_es), E(tit_nl)))
        partes = E(cuerpo).split("{}")
        texto = partes[0]
        for (n, inf, a), resto in zip(huecos, partes[1:]):
            texto += ('<b>(%d)</b> <span class="sol">%s</span> <i>(%s)</i>%s'
                      % (n, E(a), E(inf), resto))
        out.append('<div class="frase" style="text-indent:0;padding-left:0">%s</div></div>' % texto)
    return "".join(out)


def rejilla():
    filas = "".join('<div><b>%d</b> %s</div>' % (n, E(PD.CLAVE[n])) for n in sorted(PD.CLAVE))
    return ('<h2>De sleutel in één oogopslag</h2>'
            '<p class="nl">Handig om af te drukken en naast de bundel te leggen.</p>'
            '<div class="clave">%s</div>' % filas)


def build():
    doc = ("<!doctype html><html lang=\"nl\"><head><meta charset=\"utf-8\">"
           "<title>C5 · U1 · Cien formas — clave</title>"
           "<style>%s%s%s</style></head><body>%s%s<h2>Frase por frase</h2>%s%s</body></html>"
           % (FONTS, TOKENS % (C5["g"], C5["gd"], C5["gt"]), CSS,
             portada(), resumen(), bloques(), rejilla()))
    os.makedirs(OUT, exist_ok=True)
    ruta = os.path.join(OUT, "C5_U1_docente_presente.html")
    open(ruta, "w", encoding="utf-8").write(doc)
    print("C5   → %s (%d KB · %d vormen)"
          % (os.path.relpath(ruta, ROOT), len(doc) / 1024, len(PD.CLAVE)))
    return ruta


if __name__ == "__main__":
    a_pdf(build())
