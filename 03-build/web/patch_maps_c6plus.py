# -*- coding: utf-8 -*-
# patch_maps_c6plus.py — bakt de gedeelde landkaart-fiche (paises_data.py) in de
# C6+-hubs (gen_c6plus_u<N>_web.py) met de C6+-mappings (mapa_c6plus.py):
#   1) vervangt `const INFO={...};` door de per-unit versie (vaste fiche + themafeit);
#   2) vervangt de render-regel (box.innerHTML=...) door de volledige fiche-render.
# Idempotent: herdraaien = zelfde resultaat (matcht ook de reeds gepatchte vorm).
# Draai daarna gen_c6plus_u<N>_web.py opnieuw om de HTML-hubs te regenereren.
import re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paises_data as PD
import mapa_c6plus as M

WEB = os.path.dirname(os.path.abspath(__file__))
# matcht zowel het originele blok (`const INFO={ … \n };`) als de reeds-gepatchte
# platte vorm (`const INFO={ … }};`). `};` komt maar één keer voor (op het einde),
# dus non-greedy `.*?\};` is veilig. Idempotent: herdraaien geeft hetzelfde resultaat.
INFO_RE   = re.compile(r"const INFO=\{.*?\};", re.S)
RENDER_RE = re.compile(r"box\.innerHTML='<h3>'\+d\.fl\+[^\n]*;")

done = []
for u in M.UNIT_TEMA:                              # enkel C6+-units met een themalaag
    f = os.path.join(WEB, f"gen_c6plus_u{u}_web.py")
    if not os.path.exists(f):
        continue
    src = open(f, encoding="utf-8").read()
    orig = src
    # info_block_js() levert al `const INFO={...};` (compleet, met sluit-} en ;).
    # Behoud de originele 1-spatie-inspringing; GEEN extra `};` toevoegen.
    info_js = PD.info_block_js(u, unit_tema=M.UNIT_TEMA, paradas=M.PARADAS)
    src, n1 = INFO_RE.subn(lambda m: " " + info_js, src, count=1)
    src, n2 = RENDER_RE.subn(lambda m: PD.RENDER_JS, src, count=1)
    if n1 != 1 or n2 != 1:
        print(f"  ⚠ U{u}: INFO-match={n1} render-match={n2}  (verwacht 1/1)")
    if src != orig:
        open(f, "w", encoding="utf-8").write(src)
    done.append((u, n1, n2))

print("gepatcht:", ", ".join(f"U{u}(info={a},render={b})" for u, a, b in done) or "(geen C6+-web-gens gevonden)")
