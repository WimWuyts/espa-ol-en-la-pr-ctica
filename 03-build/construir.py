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


# ── C4 ───────────────────────────────────────────────────────────────────────
# C4 wordt anders gebouwd dan C5/C6+: geen map per unit, maar generatoren die
# naast elkaar in 03-build/web staan, plus vier gedeelde componenten die hun
# unit uit een omgevingsvariabele halen. Het thema hoort daar ook bij — het
# bepaalt welke banda sonora de unit krijgt — en stond tot nu alleen in de
# hand-getypte bouwregels in HANDOVER_C4.md. Nu staat het hier.
C4_TEMA = {
    1: "presentaciones", 2: "saludos", 3: "nacionalidades", 4: "familia",
    5: "objetos", 6: "casa", 7: "profesiones", 8: "horas", 9: "planes",
    # De laatste vier volgen hun aflevering en niet de oorspronkelijke
    # themalijst: 11 gaat over het weer (niet «ropa»), 13 over de markt (niet
    # «hotel») en 14 over het restaurant (niet «repaso»). In C4 is de vídeo de
    # leidraad (CLAUDE.md §3), dus het thema volgt wat er gezegd wordt.
    10: "tareas", 11: "tiempo", 12: "ropa", 13: "mercado", 14: "restaurante",
}


def unidades_c4():
    """De C4-units die gebouwd kunnen worden.

    U1–U10 hebben elk hun eigen generatoren, gebouwd op de sitcom-aflevering.
    Voor U11–U14 bestaat die aflevering niet in de repo — geen video, geen
    transcript — dus die draaien op de gedeelde generatoren met eigen scènes
    (`escena_data.py`, `kit_data.py`). Zie `gen_c4_escena.py` voor het waarom.
    """
    return ([u for u in range(1, 11)
             if os.path.exists(os.path.join(WEB, "gen_c4u%d_pdf.py" % u))]
            + [u for u in range(11, 15)
               if os.path.exists(os.path.join(WEB, "gen_c4_pdf.py"))])


# U11–U14 delen hun generatoren; hun unitnummer gaat via de omgeving mee.
C4_COMPARTIDAS = {
    "escucha":   ("gen_c4_escena.py", "C4_ESCENA_OUT", "C4_U%d_escucha.html"),
    "kit":       ("gen_c4_kit.py", "C4_KIT_OUT", "C4_U%d_kgt.html"),
    "practica":  ("gen_c4_practica.py", "C4_PRACTICA_OUT", "C4_U%d_practica.html"),
}


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


def corre(cmd, cwd=None, entorno=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                       env=dict(os.environ, **entorno) if entorno else None)
    return r.returncode == 0, (r.stdout + r.stderr).strip()


def construye_c4(u):
    """Eén C4-unit: eerst de zeven onderdelen, dan de hub, dan de print.

    De volgorde is niet vrij. De hub bundelt de zeven componenten als
    srcdoc-iframes, dus die moeten er ál zijn; en de print-PDF haalt zijn
    «Lee y escucha»-sectie uit dezelfde gegevens als het comprension-onderdeel,
    dus die twee mogen niet uit elkaar lopen.
    """
    propio = os.path.exists(os.path.join(WEB, "gen_c4u%d_pdf.py" % u))
    if propio:
        primeros = [(["python3", "gen_c4u%d_escucha.py" % u], None),
                    (["python3", "gen_c4u%d_kgt.py" % u], None),
                    (["python3", "gen_c4u%d_practica.py" % u], None)]
    else:
        primeros = [(["python3", script], {"C4_UNIT": str(u), var: patron % u})
                    for script, var, patron in C4_COMPARTIDAS.values()]
    pasos = primeros + [
        (["python3", "gen_c4_comprension.py"],
         {"C4_UNIT": str(u), "C4_COMPR_OUT": "C4_U%d_comprension.html" % u}),
        (["python3", "gen_c4_mapa.py"],
         {"C4_UNIT": str(u), "C4_MAPA_OUT": "C4_U%d_mapa.html" % u}),
        (["python3", "gen_c4_funciones.py"],
         {"C4_UNIT": str(u), "C4_FUNC_OUT": "C4_U%d_funciones.html" % u}),
        (["python3", "gen_c4_musica.py"],
         {"C4_TEMA": C4_TEMA.get(u, "presentaciones"),
          "C4_MUSICA_OUT": "C4_U%d_musica.html" % u}),
        # De offline oefenpartner. In C4 is dit een eigen tabblad (de hub laadt
        # zijn tabbladen als aparte bestanden in), in C5 en C6+ zit hij in het
        # Hablar-paneel van de pagina zelf.
        (["python3", "gen_rol.py", "C4", str(u)], None),
        (["python3", "gen_coach.py", "C4", str(u)], None),
    ]
    pasos += ([(["python3", "gen_c4u%d_hub.py" % u], None),   # ná de zeven onderdelen
                (["python3", "gen_c4u%d_pdf.py" % u], None)] if propio else
              [(["python3", "gen_c4_hub.py"], {"C4_UNIT": str(u)}),
               (["python3", "gen_c4_pdf.py"], {"C4_UNIT": str(u)})])
    for cmd, ent in pasos:
        if not os.path.exists(os.path.join(WEB, cmd[1])):
            return False, "ontbreekt: " + cmd[1]
        ok, salida = corre(cmd, cwd=WEB, entorno=ent)
        if not ok:
            return False, "%s: %s" % (cmd[1], salida[-260:])
    return True, ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("curso", nargs="?", choices=["C4", "C5", "C6+"])
    ap.add_argument("unidad", nargs="?", type=int)
    ap.add_argument("--sin-pdf", action="store_true", help="sla de PDF-render over")
    ap.add_argument("--sin-hub", action="store_true")
    a = ap.parse_args()

    trabajo = [] if a.curso == "C4" else unidades(a.curso, a.unidad)
    c4 = ([] if a.curso in ("C5", "C6+") else
          [u for u in unidades_c4() if a.unidad is None or u == a.unidad])
    fallos = []

    if c4:
        print("── 0 · C4: onderdelen → hub → print ─────────────────────────────")
        for u in c4:
            ok, salida = construye_c4(u)
            print("   C4   U%-2d %s" % (u, "ok" if ok else "MISLUKT — " + salida))
            if not ok:
                fallos.append("C4 U%d: %s" % (u, salida))

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

        print("── 4b · luisterfragmenten in de pagina bakken ───────────────────")
        ok, salida = corre(["python3", "hub_audio.py"], cwd=WEB)
        print("   %s" % (salida.splitlines()[-1] if salida else "ok"))
        if not ok:
            fallos.append("hub-audio: " + salida[-300:])

        print("── 4c · Lucide-iconen in de hub-interface ───────────────────────")
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

    print("── 6b · Lucide-iconen in de gedrukte cursus ─────────────────────")
    ok, salida = corre(["python3", "print_iconos.py"], cwd=WEB)
    print("   %s" % (salida.splitlines()[-1] if salida else "ok"))
    if not ok:
        fallos.append("print-iconen: " + salida[-300:])

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
            paginas = [("C4", u, os.path.join(WEB, "print", "C4_U%d.html" % u),
                        os.path.join(WEB, "print", "C4_U%d.pdf" % u)) for u in c4]
            paginas += [(curso, u, html,
                         os.path.join(PDF, "%s_U%d.pdf" % (
                             "C5" if curso == "C5" else "C6plus", u)))
                        for curso, u, d, gen, html, _ in trabajo]
            for curso, u, html, salida_pdf in paginas:
                if not os.path.exists(html):
                    continue
                ok, _s = corre([chrome, "--headless", "--no-sandbox", "--disable-gpu",
                                "--no-pdf-header-footer",
                                "--print-to-pdf=" + salida_pdf, html])
                n = 0
                if os.path.exists(salida_pdf):
                    datos = open(salida_pdf, "rb").read()
                    n = len(re.findall(rb"/Type\s*/Page[^s]", datos))
                print("   %-4s U%-2d %2d bladzijden" % (curso, u, n))

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
