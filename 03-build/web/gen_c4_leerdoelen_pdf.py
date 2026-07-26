#!/usr/bin/env python3
# C4 · Leerdoelen & Evaluatiekader — Markdown → verzorgde PDF (C4-rood) via Chromium.
import base64, os, markdown
ROOT="/home/user/espa-ol-en-la-pr-ctica"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])

SRC=f"{ROOT}/01-cursussen/04-welcome/C4_LEERDOELEN_EVALUATIE.md"
md=open(SRC,encoding="utf-8").read()
# titel (H1) apart voor de cover; rest converteren
body_md=md.split("\n",1)[1] if md.startswith("# ") else md
html=markdown.markdown(body_md,extensions=["tables","sane_lists","attr_list"])

CSS=FONTS+r"""
@page{size:A4;margin:16mm 15mm 15mm}
@page:first{margin:0 0 15mm 0}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#fff;--crema:#F6F1EC;--line:#E7E1DF}
body{margin:0;font-family:'Inter',sans-serif;color:var(--ink);font-size:10.4pt;line-height:1.5;background:#fff}
.cover{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;padding:34mm 15mm 16mm}
.cover .eyebrow{font-size:9.5pt;letter-spacing:.18em;font-weight:600;opacity:.9;text-transform:uppercase}
.cover h1{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:34pt;line-height:1.03;margin:4mm 0 3mm}
.cover p{font-size:12pt;max-width:150mm;opacity:.97;margin:0}
.wrap{padding:0 0}
h2{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;color:var(--gd);font-size:16pt;margin:9mm 0 2mm;padding-bottom:1.5mm;border-bottom:2px solid var(--gt);break-after:avoid}
h3{font-family:'Bricolage Grotesque',sans-serif;font-weight:700;color:var(--ink);font-size:12pt;margin:6mm 0 1.5mm;break-after:avoid}
p{margin:2mm 0}
blockquote{background:var(--gt);border-left:3px solid var(--g);border-radius:0 8pt 8pt 0;margin:3mm 0;padding:2.5mm 5mm;font-size:9.7pt;color:var(--ink)}
blockquote p{margin:1.5mm 0}
ul,ol{margin:2mm 0;padding-left:6mm}li{margin:1mm 0}
strong{color:var(--gd)}
code{background:var(--crema);border-radius:4pt;padding:.3mm 1.4mm;font-family:'Bricolage Grotesque',sans-serif;font-size:9pt;color:var(--gd)}
table{border-collapse:collapse;width:100%;font-size:8.9pt;margin:3mm 0;break-inside:auto}
th{background:var(--g);color:#fff;text-align:left;padding:1.8mm 2.4mm;font-family:'Bricolage Grotesque',sans-serif;font-size:8.2pt}
td{border:1px solid var(--line);padding:1.6mm 2.4mm;vertical-align:top}
tr:nth-child(even) td{background:var(--crema)}
thead{display:table-header-group}
tr{break-inside:avoid}
hr{border:0;border-top:1px dashed #CFCEC8;margin:7mm 0}
h2,h3{page-break-after:avoid}
"""

HTML=f"""<!doctype html><html lang="nl"><head><meta charset="utf-8"><title>C4 · Leerdoelen &amp; Evaluatie</title><style>{CSS}</style></head><body>
<div class="cover">
  <div class="eyebrow">C4 · «Welcome to Spanish» · 4 Moderne talen</div>
  <h1>Leerdoelen &amp; Evaluatiekader</h1>
  <p>Het kader voor de rode cursus: wat leerlingen moeten kunnen om C5 met een voorsprong te starten — en hoe we dat evalueren.</p>
</div>
<div class="wrap">{html}</div>
</body></html>"""
os.makedirs(f"{ROOT}/03-build/web/print",exist_ok=True)
out=f"{ROOT}/03-build/web/print/C4_Leerdoelen_Evaluatie.html"
open(out,"w",encoding="utf-8").write(HTML)
print("geschreven:",out,len(HTML),"bytes")
