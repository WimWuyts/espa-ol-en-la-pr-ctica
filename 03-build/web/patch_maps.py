# -*- coding: utf-8 -*-
# Bakt de gedeelde landkaart-fiche (paises_data.py) in elke gen_u<N>_web.py:
#   1) vervangt het literal `const INFO={...};`-blok door de per-unit versie
#      (vaste fiche + themafeit dat meebeweegt met de unidad);
#   2) vervangt de render-regel (box.innerHTML=...) door de volledige fiche-render.
# Idempotent: herdraaien = zelfde resultaat (matcht ook de reeds gepatchte vorm).
import re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paises_data as PD

WEB = os.path.dirname(os.path.abspath(__file__))
INFO_RE   = re.compile(r"const INFO=\{.*?\n \};", re.S)
RENDER_RE = re.compile(r"box\.innerHTML='<h3>'\+d\.fl\+[^\n]*;")

done = []
for u in range(9):
    f = os.path.join(WEB, f"gen_u{u}_web.py")
    if not os.path.exists(f):
        continue
    src = open(f, encoding="utf-8").read()
    orig = src
    # info_block_js() levert al `const INFO={...};` (compleet, met sluit-} en ;).
    # Behoud de originele 1-spatie-inspringing; GEEN extra `};` toevoegen.
    src, n1 = INFO_RE.subn(lambda m: " " + PD.info_block_js(u), src, count=1)
    src, n2 = RENDER_RE.subn(lambda m: PD.RENDER_JS, src, count=1)
    if n1 != 1 or n2 != 1:
        print(f"  ⚠ U{u}: INFO-match={n1} render-match={n2}  (verwacht 1/1)")
    if src != orig:
        open(f, "w", encoding="utf-8").write(src)
    done.append((u, n1, n2))

print("gepatcht:", ", ".join(f"U{u}(info={a},render={b})" for u,a,b in done))
