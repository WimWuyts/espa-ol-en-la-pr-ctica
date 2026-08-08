#!/usr/bin/env python3
"""De opnameklare transcripten van álle luisterfragmenten, in één document.

WAAROM
De auteur neemt de audio zelf op met ElevenLabs. Dan heeft hij per fragment drie
dingen nodig, en niet meer: **wat** er gezegd wordt (regel per regel, met wie het
zegt), **hoe het moet heten** als het klaar is, en **waar het in de cursus
staat** zodat hij weet wat hij aan het opnemen is.

Dat derde is geen luxe: de hub zoekt het bestand op een exact pad — `audio/…mp3`
onder `03-build/web/` — en valt terug op de browserstem zolang dat er niet is.
Eén letter verschil en de opname wordt nooit gevonden. Daarom staat de
bestandsnaam bij elk fragment.

De Nederlandse vertaling staat er als grijze regel bij; die wordt níét ingelezen.
Ze staat er alleen zodat de auteur bij het opnemen ziet wat er bedoeld wordt.

    python3 03-build/web/gen_guiones_elevenlabs.py
        → 03-build/web/print/GUIONES_AUDIO.md   (om te lezen of te printen)
        → 03-build/web/print/GUIONES_AUDIO.html (zelfde inhoud, in de huisstijl)

Twee bronnen, één formaat: `escucha_data.py` (het lange fragment per unit) en
`escucha_corta_data.py` (de korte audiotaken). Beide leveren `guion` = een rij
van {who, es, nl}.
"""
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import escucha_corta_data as EC     # noqa: E402
import escucha_data as ED           # noqa: E402

SALIDA = os.path.join(HERE, "print")


def _largos():
    """[(curso, unidad, fragment)] — het lange fragment per unit."""
    out = []
    for nombre in dir(ED):
        if not nombre.startswith(("C5_U", "C6P_U")):
            continue
        v = getattr(ED, nombre)
        if not isinstance(v, dict) or "guion" not in v:
            continue
        curso = "C5" if nombre.startswith("C5") else "C6+"
        unidad = int(nombre.split("_U")[1])
        out.append((curso, unidad, v))
    return sorted(out, key=lambda x: (x[0], x[1]))


def _cortos():
    out = []
    for (curso, unidad), lista in sorted(EC.CORTOS.items()):
        for f in lista:
            out.append((curso, unidad, f))
    return out


def _hablantes(guion):
    vistos = []
    for g in guion:
        if g["who"] not in vistos:
            vistos.append(g["who"])
    return vistos


def fragmentos():
    """Alles op één hoop, in de volgorde waarin de leerling ze tegenkomt."""
    todo = []
    for curso, unidad, f in _cortos():
        # een «canción» verwijst naar een bestaand nummer van een artiest: daar
        # valt niets aan op te nemen, en de leerling luistert het via de playlist
        if f.get("tipo") == "cancion" or not f.get("guion"):
            continue
        todo.append({
            "curso": curso, "unidad": unidad, "tipo": "kort",
            "titulo": f.get("titulo", ""), "donde": f.get("seccion", ""),
            "etiqueta": f.get("etiqueta", ""), "archivo": f.get("audio") or "",
            "tarea": f.get("tarea", ""), "guion": f["guion"],
        })
    for curso, unidad, f in _largos():
        s = f.get("situacion", {})
        todo.append({
            "curso": curso, "unidad": unidad, "tipo": "lang",
            "titulo": f.get("titulo", ""), "donde": "Escucha (begripsladder)",
            "etiqueta": "", "archivo": f.get("audio") or "",
            "tarea": s.get("que", ""), "guion": f["guion"],
        })
    orden = {"C5": 0, "C6+": 1}
    return sorted(todo, key=lambda x: (orden[x["curso"]], x["unidad"],
                                       0 if x["tipo"] == "kort" else 1))


def markdown(todo):
    L = ["# Opnamescripts · alle luisterfragmenten van C5 en C6+", "",
         "Voor de opname met ElevenLabs. **De Nederlandse regel wordt niet ingelezen** —",
         "die staat er alleen bij als betekenis.", "",
         "> **De bestandsnaam is niet vrij te kiezen.** De digitale pagina zoekt het",
         "> bestand op precies dat pad, onder `03-build/web/`. Klopt de naam niet, dan",
         "> blijft de browserstem spelen en merk je het pas in de klas.", ""]
    total_lineas = sum(len(f["guion"]) for f in todo)
    L += ["%d fragmenten · %d regels in totaal." % (len(todo), total_lineas), ""]

    curso_actual = None
    for f in todo:
        if f["curso"] != curso_actual:
            curso_actual = f["curso"]
            L += ["", "---", "", "## %s" % ("C5 · «Español en la práctica»" if curso_actual == "C5"
                                            else "C6+ · «Más español en la práctica · edición única»"), ""]
        L += ["### %s U%d · %s" % (f["curso"], f["unidad"], f["titulo"] or f["etiqueta"])]
        L += ["", "| | |", "|---|---|",
              "| **Bestandsnaam** | `%s` |" % (f["archivo"] or "— nog geen naam —"),
              "| **Waar in de cursus** | %s |" % (f["donde"] or "—"),
              "| **Sprekers** | %s |" % " · ".join(_hablantes(f["guion"]))]
        if f["tarea"]:
            L += ["| **Wat de leerling doet** | %s |" % f["tarea"]]
        L += ["", "```"]
        for g in f["guion"]:
            L.append("%s: %s" % (g["who"], g["es"]))
        L += ["```", ""]
        L.append("<sub>" + " · ".join(g["nl"] for g in f["guion"] if g.get("nl")) + "</sub>")
        L.append("")
    return "\n".join(L)


CSS = """
body{font-family:Inter,system-ui,sans-serif;max-width:190mm;margin:0 auto;padding:14mm;
 color:#20242E;background:#FCFBF8;font-size:10.4pt;line-height:1.55}
h1{font-size:22pt;margin:0 0 2mm;color:#157355}
h2{font-size:15pt;margin:9mm 0 3mm;padding-top:4mm;border-top:2px solid #1E9E74;color:#157355}
h3{font-size:11.6pt;margin:7mm 0 2mm;color:#20242E;break-after:avoid}
.meta{display:grid;grid-template-columns:38mm 1fr;gap:1mm 4mm;font-size:9.2pt;
 background:#F3EEE4;border-radius:8px;padding:3mm 4mm;margin:0 0 3mm}
.meta b{color:#6A6E78;font-weight:600}
.archivo{font-family:ui-monospace,Menlo,monospace;background:#E4F4EE;padding:.5mm 2mm;border-radius:4px}
.guion{border-left:3px solid #1E9E74;padding:2mm 0 2mm 5mm;margin:0 0 2mm}
.guion p{margin:0 0 1.6mm}
.who{display:inline-block;min-width:26mm;color:#157355;font-weight:600}
.nl{color:#6A6E78;font-style:italic;font-size:8.8pt;margin:0 0 6mm 5mm}
.aviso{background:#FBF3D6;border-left:4px solid #B7860B;padding:3mm 4mm;border-radius:6px;margin:4mm 0}
@media print{ .frag{break-inside:avoid} @page{size:A4;margin:14mm} }
"""


def pagina(todo):
    e = html.escape
    P = ['<!doctype html><html lang="nl"><head><meta charset="utf-8">',
         "<title>Opnamescripts · luisterfragmenten C5 en C6+</title>",
         "<style>%s</style></head><body>" % CSS,
         "<h1>Opnamescripts · alle luisterfragmenten</h1>",
         "<p>Voor de opname met ElevenLabs. De Nederlandse regel eronder wordt "
         "<b>niet</b> ingelezen — die staat er als betekenis.</p>",
         '<div class="aviso"><b>De bestandsnaam ligt vast.</b> De digitale pagina zoekt '
         "het bestand op precies dat pad, onder <code>03-build/web/</code>. Klopt de naam "
         "niet, dan blijft de browserstem spelen en merk je het pas in de klas.</div>",
         "<p>%d fragmenten · %d regels in totaal.</p>"
         % (len(todo), sum(len(f["guion"]) for f in todo))]
    curso_actual = None
    for f in todo:
        if f["curso"] != curso_actual:
            curso_actual = f["curso"]
            P.append("<h2>%s</h2>" % ("C5 · «Español en la práctica»" if curso_actual == "C5"
                                      else "C6+ · «Más español en la práctica · edición única»"))
        P.append('<div class="frag">')
        P.append("<h3>%s U%d · %s</h3>" % (f["curso"], f["unidad"],
                                           e(f["titulo"] or f["etiqueta"])))
        P.append('<div class="meta"><b>Bestandsnaam</b><span class="archivo">%s</span>'
                 "<b>Waar in de cursus</b><span>%s</span>"
                 "<b>Sprekers</b><span>%s</span>"
                 % (e(f["archivo"] or "— nog geen naam —"), e(f["donde"] or "—"),
                    e(" · ".join(_hablantes(f["guion"])))))
        if f["tarea"]:
            P.append("<b>Wat de leerling doet</b><span>%s</span>" % e(f["tarea"]))
        P.append("</div>")
        P.append('<div class="guion">')
        for g in f["guion"]:
            P.append('<p><span class="who">%s</span>%s</p>' % (e(g["who"]), e(g["es"])))
        P.append("</div>")
        nl = " · ".join(g["nl"] for g in f["guion"] if g.get("nl"))
        if nl:
            P.append('<p class="nl">%s</p>' % e(nl))
        P.append("</div>")
    P.append("</body></html>")
    return "\n".join(P)


def main():
    todo = fragmentos()
    os.makedirs(SALIDA, exist_ok=True)
    md = os.path.join(SALIDA, "GUIONES_AUDIO.md")
    ht = os.path.join(SALIDA, "GUIONES_AUDIO.html")
    open(md, "w", encoding="utf-8").write(markdown(todo))
    open(ht, "w", encoding="utf-8").write(pagina(todo))
    lineas = sum(len(f["guion"]) for f in todo)
    cortos = sum(1 for f in todo if f["tipo"] == "kort")
    print("%d fragmenten (%d kort, %d lang) · %d regels"
          % (len(todo), cortos, len(todo) - cortos, lineas))
    print("  %s" % md)
    print("  %s" % ht)


if __name__ == "__main__":
    main()
