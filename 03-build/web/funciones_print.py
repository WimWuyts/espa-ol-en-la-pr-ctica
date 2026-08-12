#!/usr/bin/env python3
# C4 — GEDEELDE print-render van de functielaag (matrix C). Levert één <div class="page sec">
# voor de PDF-generatoren (U1..U14), zodat de «funciones comunicativas»-spiekkaart uit één bron
# komt en per unit meegroeit. Gebruikt de print-CSS-klassen van cursus-print.css / de pdf-generator.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import funciones_data as FD

def _wl(cls=""): return f'<span class="wl {cls}"></span>'

def print_section(unit):
    fs = FD.funciones_hasta(unit)
    have = len(fs); total = len(FD.FUNCIONES)
    # ── banco-spiekkaart: función · exponentes (per unit) · semáforo ──
    # volle spiekkaart → trapsgewijs compacter zodat alles op één blad blijft
    tight   = have >= 15   # zeer vol (≥15): exponentes op dezelfde regel als de functienaam
    compact = have >= 13   # vol (13-14): kleinere letter + minder exponentes
    exp_fs = "6.8pt" if tight else ("7.0pt" if compact else "7.6pt")
    rows = ""
    for f in fs:
        allexp = [e for u in sorted(k for k in f["exp"] if k <= unit) for e in f["exp"][u]]
        cap = 3 if tight else (4 if compact else (5 if have >= 11 else 99))
        exps = " · ".join(allexp[:cap]) + (" …" if len(allexp) > cap else "")
        st = FD.status(f, unit)
        mark = ' <span style="font-size:6.6pt;font-weight:800;color:var(--gd)">NUEVA</span>' if st=="nueva" else (' <span style="font-size:6.6pt;font-weight:800;color:var(--gd)">▲</span>' if st=="nivel" else "")
        br = " — " if tight else "<br>"
        rows += (f'<tr><td style="text-align:left"><b>{f["es"]}</b>{mark}{br}'
                 f'<span style="font-size:{exp_fs};color:var(--mut)">{exps}</span></td><td></td><td></td><td></td></tr>')
    # compacte units krijgen een td-override zodat de lange tabel op één blad blijft
    if tight:
        compact_style = '<style>.fbanco td{padding:.4mm 1.8mm!important;font-size:8.2pt}.fbanco th{padding:.8mm 1.8mm!important}</style>'
    elif compact:
        compact_style = '<style>.fbanco td{padding:.55mm 2mm!important}.fbanco th{padding:.9mm 2mm!important}</style>'
    else:
        compact_style = ''
    banco = (compact_style + '<table class="sem fbanco" style="margin-top:2mm"><thead><tr>'
             '<th style="text-align:left">Función · exponentes <span class="gloss">wat ik al kan zeggen</span></th><th>🟢</th><th>🟡</th><th>🔴</th></tr></thead>'
             f'{rows}</table>')
    # ── noticing (compacte 2-koloms-oefening: cita → función) ──
    noti = FD.NOTICING.get(unit, [])
    n_cells = "".join(f'<div style="display:flex;gap:2mm;align-items:baseline"><span style="flex:1;font-size:8.8pt">{c}</span>{_wl("sm")}</div>' for c, fid in noti)
    used_ids = sorted({fid for _, fid in noti})
    bank = " · ".join(FD.FMAP[i]["es"] for i in used_ids)
    noticing = (f'<div class="regla"><span class="tag">¿Qué hacen con el idioma? · uit de scène</span>'
                f'<p style="margin:1mm 0;font-size:8.8pt"><b>¿Qué función tiene cada frase? Escríbela al lado.</b> '
                f'<span class="gloss">welke functie voert elke zin uit?</span> '
                f'<span style="color:var(--mut)">Banco: {bank}.</span></p>'
                f'<div style="columns:2;column-gap:8mm;line-height:1.75">{n_cells}</div></div>')
    # ── tarea-tags + mini-reto (productie; wbox-hoogte schaalt met #functies → volle bladspiegel) ──
    ids = FD.TAREA_FUN.get(unit, [])
    tt = FD.TAREA_TITEL.get(unit, "")
    tar_chips = "".join(f'<span>{FD.FMAP[i]["es"]}</span>' for i in ids)
    tarea = (f'<div class="regla" style="margin-top:3mm"><span class="tag">En la tarea «{tt}» usas…</span>'
             f'<div class="cogn" style="margin-top:1mm">{tar_chips}</div></div>')
    # lichte units (weinig functies) krijgen een extra ophaal-blokje → volle bladspiegel zonder U3 te overladen
    extra = ""
    if have <= 4:
        extra = ('<div class="regla" style="margin-top:3mm"><span class="tag">Recuerda sin mirar</span>'
                 '<p style="font-size:9pt;margin:1mm 0">Traduce de memoria, sin mirar. '
                 '<span class="gloss">Vertaal uit het hoofd — ophalen is de beste manier om te leren.</span></p>'
                 f'<div style="font-size:9.6pt;line-height:2.5">a) hallo / tot ziens → {_wl("lg")}<br>'
                 f'b) hoe heet je? → {_wl("lg")}<br>c) ik heet… / ik ben… → {_wl("lg")}</div></div>')
    # de mini-reto vult lichte units; bij 9-14 functies is het banco al vol → geen reto (anders overloop).
    # In tight-modus is elke banco-rij één regel → tot 16 functies past er nog een kleine reto bij;
    # vanaf 17 is het blad ook zó vol → geen reto meer (gemeten op de U8-build).
    reto = ""
    if have <= 8 or (tight and have <= 16):
        reto_h = 22 if tight else max(14, int(42 - have * 3.2))
        reto = (f'<div class="truc" style="margin-top:3mm"><b>Mini-reto ✍️</b> Escribe una conversación corta en la que uses '
                f'<b>al menos 3 funciones</b> de arriba. Subraya cada una. '
                f'<span class="gloss">korte conversatie met drie functies; onderstreep welke</span>'
                f'<div class="wbox" style="min-height:{reto_h}mm"></div></div>')
    return (f'<div class="page sec" style="break-before:page">'
            f'<div class="se">Funciones comunicativas · lo que ya sé decir</div>'
            f'<h2>Lo que ya puedes hacer con el español <span class="gloss" style="font-size:10pt;font-weight:400">'
            f'wat je met het Spaans kunt dóen</span></h2>'
            f'<p style="font-size:9.4pt;margin:0 0 2mm">No solo palabras: <b>funciones</b> — lo que puedes hacer con el español. '
            f'<span class="gloss">groeit elke unit: nu <b>{have}/{total}</b> functies</span></p>'
            f'{noticing}'
            f'<div class="se" style="margin-top:3mm">Mi repertorio · pon tu semáforo</div>'
            f'<p style="font-size:8.8pt;margin:0 0 1mm">Todo lo que ya sabes decir. Colorea cada función: '
            f'🟢 con soltura · 🟡 con esfuerzo · 🔴 todavía no. '
            f'<span class="gloss">alles wat je al kunt zeggen</span></p>'
            f'{banco}{tarea}{extra}{reto}</div>')

if __name__ == "__main__":
    for u in (1, 2, 3):
        h = print_section(u)
        print(f"U{u}: print-sectie {len(h)} bytes · {len(FD.funciones_hasta(u))} functies")
