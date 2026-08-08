#!/usr/bin/env python3
# C4 — GEDEELDE print-render van «Lee y escucha». Levert één <div class="page sec"> voor de
# PDF-generatoren, of "" wanneer er (nog) geen data is (dan geen lege pagina in print).
import os, sys, re, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comprension_data as CD
from qr_codigo import qr_svg          # eigen encoder: PyPI is hier geblokkeerd

def _wl(cls=""): return f'<span class="wl {cls}"></span>'

def _qr(url):
    """Dezelfde code als in de rest van de cursus — zie qr_codigo.py."""
    return qr_svg(url, mm=22, nivel="Q", color="#A8323B") if url else ""

def _mc(qs):
    out = ""
    for i, q in enumerate(qs):
        opts = " &nbsp; ".join(f'☐ {o}' for o in q["opts"])
        out += f'<div style="font-size:9.4pt;margin:1.4mm 0">{i+1}. {q["q"]} &nbsp; <span style="color:var(--mut)">{opts}</span></div>'
    return out

def print_section(unit, hub_url=None):
    L = CD.LECTURA.get(unit); A = CD.AUDIO.get(unit)
    if not (L or A):
        return ""
    parts = ['<div class="page sec" style="break-before:page">',
             '<div class="se">Lee y escucha · comprensión</div><h2>Lezen &amp; luisteren</h2>']
    # ── LEZEN ──
    if L:
        # De chatregels staan strakker dan de `.tl` van het sitcom-transcript.
        # Reden: die leestekst is de énige die van unit tot unit sterk in lengte
        # verschilt — U1 heeft er acht, de meeste drie tot vijf — en de sectie
        # heeft in C4 precies één bladzijde (CLAUDE.md §3). Met de gewone
        # regelafstand liep U1 er een millimeter of acht overheen en kreeg blad 4
        # een sliver inhoud met de rest leeg. Een chat mag typografisch dicht
        # staan, dus dit kost niets aan leesbaarheid en houdt de regel intact.
        texto = "".join(
            (f'<div class="tl" style="padding:.35mm 0"><span class="sp">{w}</span>'
             f'<span class="tx">{ln}</span></div>' if w
             else f'<p style="font-size:9.6pt;margin:.8mm 0">{ln}</p>')
            for w, ln in L["texto"])
        det = "".join(
            f'<tr><td>{i+1}. {q["q"]}</td><td class="b">☐ V ☐ F</td><td>{_wl("")}</td></tr>'
            for i, q in enumerate(L["detalle"]))
        gloss = "".join(f'<span>{e} · {n}</span>' for e, n in L["glosario"])
        parts.append(
            f'<div class="regla"><span class="tag">📖 Lee · {L["tipo"]}</span>'
            f'<p style="font-size:8.8pt;color:var(--mut);margin:1mm 0">{L["contexto_nl"]}</p>'
            f'<div class="twocol">{texto}</div></div>'
            f'<div class="se" style="margin-top:2mm">Comprensión</div>'
            f'<p style="font-size:9pt;margin:0 0 1mm"><b>Globaal</b> — kruis aan:</p>{_mc(L["global"])}'
            f'<p style="font-size:9pt;margin:2mm 0 1mm"><b>Detail</b> — ¿V of F? Verbeter de valse op de lijn:</p>'
            f'<table class="vf">{det}</table>'
            f'<div class="truc" style="margin-top:2mm"><b>✍️ ¿Y tú?</b> {L["transfer"]} '
            f'<div style="margin-top:1mm">{_wl("full")}</div></div>'
            f'<div class="cogn" style="margin-top:2mm">{gloss}</div>')
    # ── LUISTEREN (audio online → begripsvragen op papier; luisteren gebeurt in de hub) ──
    if A:
        import enlaces as EN
        destino = EN.url("C4", unit, EN.ancla_c4("comprension"))
        qr = _qr(destino)
        parts.append(
            f'<div class="se" style="margin-top:3mm">🎧 Escucha · {A["tipo"]}</div>'
            f'<div class="audiorow"><div class="call"><span class="ic">🎧</span><div>'
            f'<b>{A["tarea_nl"]}</b> Scan de code, beluister het fragment online (▶ / 🐢 lento) en beantwoord dan de vragen.</div></div>'
            + (f'<div class="qr" data-url="{destino}"><div class="lab">Audio online</div>{qr}'
               f'<div class="meta">hub · Lee y escucha</div></div>' if qr else "")
            + '</div>'
            f'<p style="font-size:9pt;margin:2mm 0 1mm"><b>Preguntas</b> — kruis aan wat je hoort:</p>{_mc(A["preguntas"])}')
    parts.append('</div>')
    return "".join(parts)

if __name__ == "__main__":
    for u in (1, 2, 3):
        h = print_section(u, "https://hub.local/C4/U%d" % u)
        print(f"U{u}: print-sectie {len(h)} bytes" + ("" if h else " (leeg → overgeslagen)"))
