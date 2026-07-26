#!/usr/bin/env bash
# Herstelt de build-/render-omgeving in een VERSE sessie (container is telkens nieuw).
# Gebruik:  bash scripts/setup-build.sh
set -e
echo "== 1. Python-libraries voor build/render =="
python3 -m pip install --break-system-packages -q python-docx python-pptx fonttools brotli pymupdf 2>/dev/null || \
python3 -m pip install -q python-docx python-pptx fonttools brotli pymupdf

echo "== 2. Huisstijl-fonts installeren (woff2 -> ttf, nette familienamen) =="
python3 - <<'PY'
import os, glob
from fontTools.ttLib import TTFont
out=os.path.expanduser("~/.fonts"); os.makedirs(out,exist_ok=True)
for f in glob.glob(os.path.join(out,"*.ttf")): os.remove(f)
src="02-huisstijl/fonts"
mapping=[("BricolageGrotesque-700.woff2","Bricolage Grotesque","Bricolage-700"),
         ("BricolageGrotesque-800.woff2","Bricolage Grotesque XBold","Bricolage-800"),
         ("Inter-400.woff2","Inter","Inter-400"),
         ("Inter-600.woff2","Inter SemiBold","Inter-600"),
         ("Caveat-700.woff2","Caveat","Caveat-700")]
def rename(font,fam,sub="Regular"):
    n=font["name"]; ps=fam.replace(" ","")
    for nid,val in [(1,fam),(2,sub),(4,fam),(6,ps),(16,fam),(17,sub)]:
        n.setName(val,nid,3,1,0x409); n.setName(val,nid,1,0,0)
    if "OS/2" in font: font["OS/2"].fsSelection=(font["OS/2"].fsSelection&~0x21)|0x40
    font["head"].macStyle=0
for wf,fam,base in mapping:
    p=os.path.join(src,wf)
    if not os.path.exists(p): print("  ontbreekt:",wf); continue
    ft=TTFont(p); ft.flavor=None; rename(ft,fam); ft.save(os.path.join(out,base+".ttf")); print("  +",fam)
PY
fc-cache -f ~/.fonts >/dev/null 2>&1 || true

echo "== 3. Chromium (voor HTML -> PDF) =="
CHROME=$(ls /opt/pw-browsers/chromium-*/chrome-linux/chrome 2>/dev/null | head -1)
echo "  Chromium: ${CHROME:-NIET GEVONDEN}"
echo
echo "KLAAR. Render een unit met:"
echo "  \"\$CHROME\" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \\"
echo "     --print-to-pdf=U0.pdf 01-cursussen/05-a1/U0/U0.html"
