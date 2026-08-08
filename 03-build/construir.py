#!/usr/bin/env python3
"""Bouwt de hele cursus in de juiste volgorde — print, bruggen, PDF, hub, dossiers.

WAAROM DIT BESTAAT
Twee stappen moeten ná de printgeneratoren draaien en werden tot nu met de hand
gedaan: `add_puentes.py` (de verwijzingen boek → PowerPoint, die het dianummer
uit het deck haalt) en `add_qr_u0.py` (C5 U0 heeft geen generator). Wie dat
vergat, leverde een PDF zonder bruggen of met nep-QR's. Nu is de volgorde
vastgelegd:

    generator → hub → cijfers → bladspiegel → PDF → docentendossiers

    python3 03-build/construir.py              # alles
    python3 03-build/construir.py C5 3         # één unit
    python3 03-build/construir.py --sin-pdf    # zonder de trage PDF-stap
"""
import argparse
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "03-build", "web")
PDF = os.path.join(ROOT, "03-build", "pdf")


def chromium():
    c = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))
    return c[0] if c else None


def unidades(curso=None, unidad=None):
    """[(curso, unidad, map, generator|None, print-html, hub-generator)]"""
    out = []
    for u in range(9):
        d = os.path.join(ROOT, "01-cursussen", "05-a1", "U%d" % u)
        g = glob.glob(os.path.join(d, "gen_u%d_print.py" % u))
        out.append(("C5", u, d, g[0] if g else None,
                    os.path.join(d, "U%d.html" % u), "gen_u%d_web.py" % u))
    for u in range(8):
        d = os.path.join(ROOT, "01-cursussen", "06-vervolg", "U%d" % u)
        g = glob.glob(os.path.join(d, "gen_*print.py"))
        html = os.path.join(d, "C6plus_U%d.html" % u)
        if not os.path.exists(html):
            html = os.path.join(d, "U%d.html" % u)
        out.append(("C6+", u, d, g[0] if g else None, html, "gen_c6plus_u%d_web.py" % u))
    if curso:
        out = [x for x in out if x[0] == curso]
    if unidad is not None:
        out = [x for x in out if x[1] == unidad]
    return out


def corre(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return r.returncode == 0, (r.stdout + r.stderr).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("curso", nargs="?", choices=["C5", "C6+"])
    ap.add_argument("unidad", nargs="?", type=int)
    ap.add_argument("--sin-pdf", action="store_true", help="sla de PDF-render over")
    ap.add_argument("--sin-hub", action="store_true")
    a = ap.parse_args()

    trabajo = unidades(a.curso, a.unidad)
    fallos = []

    print("── 1 · printgeneratoren ─────────────────────────────────────────")
    for curso, u, d, gen, html, _ in trabajo:
        if gen is None:
            print("   %-4s U%d  (met de hand gebouwd, wordt niet hergenereerd)" % (curso, u))
            continue
        ok, salida = corre(["python3", os.path.basename(gen)], cwd=d)
        print("   %-4s U%d  %s" % (curso, u, "ok" if ok else "MISLUKT"))
        if not ok:
            fallos.append("print %s U%d: %s" % (curso, u, salida[-300:]))

    print("── 2 · C5 U0: echte QR-codes in de handgebouwde HTML ────────────")
    d0 = os.path.join(ROOT, "01-cursussen", "05-a1", "U0")
    if os.path.exists(os.path.join(d0, "add_qr_u0.py")):
        ok, salida = corre(["python3", "add_qr_u0.py"], cwd=d0)
        print("   %s" % (salida.splitlines()[0] if salida else "ok"))

    print("── 3 · bruggen boek → PowerPoint ────────────────────────────────")
    ok, salida = corre(["python3", "add_puentes.py"], cwd=WEB)
    print("   %s" % (salida.splitlines()[-1] if salida else "ok"))
    if not ok:
        fallos.append("bruggen: " + salida[-300:])

    if not a.sin_hub:
        print("── 4 · digitale pagina's ────────────────────────────────────────")
        for curso, u, d, gen, html, hub in trabajo:
            if not os.path.exists(os.path.join(WEB, hub)):
                continue
            ok, salida = corre(["python3", hub], cwd=WEB)
            print("   %-4s U%d  %s" % (curso, u, "ok" if ok else "MISLUKT"))
            if not ok:
                fallos.append("hub %s U%d: %s" % (curso, u, salida[-300:]))

        print("── 4b · Lucide-iconen in de hub-interface ───────────────────────")
        ok, salida = corre(["python3", "hub_post_iconos.py"], cwd=WEB)
        print("   %s" % (salida.splitlines()[-1] if salida else "ok"))
        if not ok:
            fallos.append("hub-iconen: " + salida[-300:])

    print("── 5 · aantallen gelijk aan de hub ──────────────────────────────")
    ok, salida = corre(["python3", "add_cifras.py"], cwd=WEB)
    print("   %s" % (salida.splitlines()[-1] if salida else "ok"))
    if not ok:
        fallos.append("cijfers: " + salida[-300:])

    print("── 6 · bouwtaal van de leerlingpagina ──────────────────────────")
    ok, salida = corre(["python3", "limpia_jerga.py"], cwd=WEB)
    print("   %s" % (salida.splitlines()[-1] if salida else "ok"))
    if not ok:
        fallos.append("jargon: " + salida[-300:])

    print("── 7 · bladspiegel: mijlpaalsecties + gedeelde breukregels ───────")
    ok, salida = corre(["python3", "bladspiegel.py"], cwd=WEB)
    print("   %s" % (salida.splitlines()[-1] if salida else "ok"))
    if not ok:
        fallos.append("bladspiegel: " + salida[-300:])

    if not a.sin_pdf:
        print("── 8 · PDF (als laatste: alle HTML-bewerkingen zitten erin) ──────")
        chrome = chromium()
        if not chrome:
            print("   geen Chromium gevonden — PDF overgeslagen")
        else:
            os.makedirs(PDF, exist_ok=True)
            for curso, u, d, gen, html, _ in trabajo:
                if not os.path.exists(html):
                    continue
                salida_pdf = os.path.join(
                    PDF, "%s_U%d.pdf" % ("C5" if curso == "C5" else "C6plus", u))
                ok, _s = corre([chrome, "--headless", "--no-sandbox", "--disable-gpu",
                                "--no-pdf-header-footer",
                                "--print-to-pdf=" + salida_pdf, html])
                n = 0
                if os.path.exists(salida_pdf):
                    datos = open(salida_pdf, "rb").read()
                    n = len(re.findall(rb"/Type\s*/Page[^s]", datos))
                print("   %-4s U%d  %2d bladzijden" % (curso, u, n))

        print("── 9 · bladzijdenummers in de PDF ───────────────────────────────")
        ok, salida = corre(["python3", "paginar.py"], cwd=os.path.join(ROOT, "03-build"))
        hechas = sum(1 for l in salida.splitlines() if "genummerd" in l and "al " not in l)
        print("   %d PDF's genummerd" % hechas)
        if not ok:
            fallos.append("paginering: " + salida[-300:])

    print("── 10 · docentendossiers ─────────────────────────────────────────")
    for script in ("gen_docente_retos.py", "gen_docente_audio.py",
                   "gen_guiones_elevenlabs.py"):
        ok, salida = corre(["python3", script], cwd=WEB)
        print("   %-24s %s" % (script, "ok" if ok else "MISLUKT"))

    print()
    if fallos:
        print("MISLUKT (%d):" % len(fallos))
        for f in fallos:
            print("  ·", f)
        sys.exit(1)
    print("klaar — alles gebouwd in de juiste volgorde")


if __name__ == "__main__":
    main()
