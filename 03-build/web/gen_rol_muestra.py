#!/usr/bin/env python3
"""Alle rollenspellen van één cursus op één pagina, om na te kijken.

WAAROM APART
De componenten zitten normaal ín de unit-pagina's, en die wegen 2,4 tot 7,8 MB
omdat de audio en de spellen erin gebakken zitten. Wie alleen de oefenpartner
wil beoordelen, moet daar niet doorheen. Deze pagina bevat álle scènes van een
cursus en verder niets — een paar honderd kilobyte in plaats van dertig
megabyte.

Dit is een kijkpagina voor de auteur, geen leerlingmateriaal: ze staat niet op
de uploadlijst in `enlaces.py` en er staat geen leerstof op die niet ook in de
unit zelf staat.

    python3 gen_rol_muestra.py C5      # → componentes/C5_roles.html
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import gen_rol                                # noqa: E402
import rol_data as RD                         # noqa: E402

# de cursuskleur bepaalt de opmaak; dezelfde tokens als overal
COLORES = {
    "C4":  ("#D64550", "#A8323B", "#FBEAEC"),
    "C5":  ("#1E9E74", "#157355", "#E4F4EE"),
    "C6+": ("#7C56A9", "#5B3E83", "#EEE8F5"),
}

BASE = """
:root{--g:%(g)s;--gd:%(gd)s;--gt:%(gt)s;--ink:#20242E;--mut:#6A6E78;
  --line:#E4E3DE;--card:#fff;--crema:#F3EEE4;--paper:#FCFBF8;
  --disp:system-ui,-apple-system,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ink:#ECEBE6;--mut:#9BA0AA;--line:#2C2E36;--card:#1C1E24;--crema:#1E2026;
  --paper:#15161A;--gt:#12352A}}
:root[data-theme="dark"]{--ink:#ECEBE6;--mut:#9BA0AA;--line:#2C2E36;
  --card:#1C1E24;--crema:#1E2026;--paper:#15161A;--gt:#12352A}
*{box-sizing:border-box}
body{font-family:system-ui,-apple-system,sans-serif;background:var(--paper);
  color:var(--ink);margin:0;padding:22px 18px 60px;line-height:1.55}
.wrap{max-width:760px;margin:0 auto}
h1{font-family:var(--disp);font-weight:800;font-size:26px;margin:0 0 4px;
  letter-spacing:-.01em}
.sub{color:var(--mut);margin:0 0 18px;font-size:15px}
.nav{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 18px}
.nav button{border:1.5px solid var(--line);background:var(--card);color:inherit;
  border-radius:10px;padding:7px 13px;font:inherit;font-size:14px;font-weight:600;
  cursor:pointer}
.nav button.on{background:var(--g);color:#fff;border-color:var(--g)}
.nav button:focus-visible{outline:3px solid var(--g);outline-offset:2px}
.uno{display:none}.uno.on{display:block}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;
  padding:18px 20px;margin:14px 0}
.lead{color:var(--mut);margin:0 0 14px}
.gloss{color:var(--mut);font-style:italic}
.pill{display:inline-block;background:var(--gt);color:var(--gd);border-radius:20px;
  padding:3px 10px;font-size:12px;font-weight:600}
.btn{border:none;background:var(--g);color:#fff;font-weight:700;border-radius:10px;
  padding:9px 16px;cursor:pointer;font-size:14px;font-family:inherit}
.btn.sec{background:var(--crema);color:var(--ink)}
.btn.small{padding:6px 11px;font-size:13px}
.btn:focus-visible{outline:3px solid var(--gd);outline-offset:2px}
footer{color:var(--mut);font-size:12.5px;margin-top:28px;text-align:center}
"""


def main():
    curso = sys.argv[1] if len(sys.argv) > 1 else "C5"
    unidades = sorted(u for (c, u) in RD.ROLES if c == curso)
    if not unidades:
        sys.exit("geen rollenspellen voor %s" % curso)
    g, gd, gt = COLORES[curso]

    nav, cuerpo, css_uno, js = "", "", "", ""
    for i, u in enumerate(unidades):
        r = RD.ROLES[(curso, u)]
        html, css, script = gen_rol.componente(curso, u)
        css_uno = css                      # voor alle scènes identiek: één keer
        nav += ('<button data-ir="%d" class="%s">U%d</button>'
                % (u, "on" if i == 0 else "", u))
        cuerpo += ('<section class="uno %s" data-uno="%d">%s</section>'
                   % ("on" if i == 0 else "", u, html))
        js += script

    doc = """<!doctype html><html lang="nl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(curso)s · de oefenpartner per unidad</title>
<style>%(base)s%(comp)s</style></head><body>
<div class="wrap">
  <h1>De oefenpartner van %(curso)s</h1>
  <p class="sub">%(n)d scènes, één per unidad. Kies een unidad en speel ze uit.
    Elke scène heeft drie standen: <b>invullen</b> (twee gaten en een woordbank),
    <b>kiezen</b> en <b>zelf typen</b>. Alles werkt zonder internet.</p>
  <nav class="nav">%(nav)s</nav>
  %(cuerpo)s
  <footer>Kijkpagina voor de auteur — in de cursus staat elke scène in het
    tabblad «Hablar» van haar eigen unidad.</footer>
</div>
<script>
document.querySelectorAll('.nav button').forEach(function(b){
  b.onclick=function(){
    document.querySelectorAll('.nav button').forEach(function(x){
      x.classList.toggle('on',x===b);});
    document.querySelectorAll('.uno').forEach(function(s){
      s.classList.toggle('on',s.dataset.uno===b.dataset.ir);});
    window.scrollTo({top:0,behavior:'smooth'});
  };
});
%(js)s
</script></body></html>""" % {
        "curso": curso, "n": len(unidades), "nav": nav, "cuerpo": cuerpo,
        "js": js, "comp": css_uno,
        "base": BASE % {"g": g, "gd": gd, "gt": gt}}

    ruta = os.path.join(AQUI, "componentes",
                        "%s_roles.html" % curso.replace("+", "plus"))
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    open(ruta, "w", encoding="utf-8").write(doc)
    print("%s geschreven: %d scènes · %d beurten · %.0f kB"
          % (os.path.basename(ruta), len(unidades),
             sum(len(RD.ROLES[(curso, u)]["pasos"]) for u in unidades),
             len(doc.encode()) / 1024))


if __name__ == "__main__":
    main()
