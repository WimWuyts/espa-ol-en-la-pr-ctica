#!/usr/bin/env python3
"""De «Kit»-tab voor U11–U14: woordenschat · uitspraak · gramática · tarea.

Zelfde vorm als `gen_c4uN_kgt.py` van U1–U10, maar één generator in plaats van
vier: de inhoud staat in `kit_data.py`, hier staat alleen hoe ze eruitziet.

De volgorde van de vier blokken is niet willekeurig — ze volgt de beweging uit
CLAUDE.md §14: eerst de woorden ontmoeten (clusters), dan hóren hoe ze klinken
(Suena bien), dan het patroon zien (gramática), en pas daarna er iets mee doen
(tarea). Regel omkeren en je krijgt een grammaticales met woordjes erbij.

    C4_UNIT=11 python3 gen_c4_kit.py
"""
import base64
import html
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)

import kit_data as KD          # noqa: E402


def b64(p):
    return base64.b64encode(open(p, "rb").read()).decode()


def face(f, p, w):
    return ("@font-face{font-family:'%s';src:url(data:font/woff2;base64,%s) "
            "format('woff2');font-weight:%s;font-display:swap}"
            % (f, b64("%s/02-huisstijl/fonts/%s" % (ROOT, p)), w))


FONTS = "".join([
    face("Bricolage Grotesque", "BricolageGrotesque-700.woff2", "700"),
    face("Bricolage Grotesque", "BricolageGrotesque-800.woff2", "800"),
    face("Inter", "Inter-400.woff2", "400"),
    face("Inter", "Inter-600.woff2", "600"),
    face("Caveat", "Caveat-700.woff2", "700")])


def esc(s):
    return html.escape(s, quote=True)


# ── woordenschat ────────────────────────────────────────────────────────────
def tarjeta(es, nl):
    return ('<div class="cc" data-es="%s"><span class="cc-es">%s</span>'
            '<span class="cc-nl">%s</span>'
            '<button class="cc-spk" title="luister">🔊</button></div>'
            % (esc(es), esc(es), esc(nl)))


def cluster(nombre, sub, ic, items):
    return ('<div class="clu"><div class="clu-h"><span class="clu-ic">%s</span>'
            '<span><b>%s</b><i>%s</i></span></div><div class="cc-grid">%s</div></div>'
            % (ic, esc(nombre), esc(sub), "".join(tarjeta(*i) for i in items)))


# ── uitspraak ───────────────────────────────────────────────────────────────
def suena(unit):
    tit, expl, palabras, (atit, aexpl, acentos) = KD.SUENA[unit]
    chips = "".join('<button class="shchip" data-w="%s">🔊 %s</button>'
                    % (esc(p.replace("_", " ")), esc(p)) for p in palabras)
    filas = "".join('<button class="acchip" data-w="%s">🔊 <b>%s</b> '
                    '<span>%s</span></button>' % (esc(w), esc(w), esc(d))
                    for w, d in acentos)
    return ('<div class="suena">'
            '<div class="sh"><span class="sic">🎧</span><div><b>Suena bien</b>'
            '<i>uitspraak van deze unidad</i></div></div>'
            '<h4>%s</h4><p>%s</p><div class="chips">%s</div>'
            '<h4>%s</h4><p>%s</p><div class="chips">%s</div>'
            '<p class="hint">💡 Pulsa una palabra para oírla. Después dila <b>tú</b>, '
            'en voz alta: mirar un sonido no enseña nada. '
            '<span class="stn">klik, luister en zeg het zelf hardop</span></p></div>'
            % (tit, esc(expl), chips, esc(atit), esc(aexpl), filas))


# ── gramática ───────────────────────────────────────────────────────────────
def gramatica(unit):
    tit, sub, filas, trampa = KD.GRAMATICA[unit]
    cuerpo = "".join(
        '<div class="gr"><span class="gf">%s</span><span class="ge">%s</span>'
        '<span class="gn">%s</span></div>' % (forma, esc(es), esc(nl))
        for forma, es, nl in filas)
    return ('<div class="gram"><div class="gh"><span class="gic">🧩</span>'
            '<div><b>%s</b><i>%s</i></div></div>%s'
            '<div class="trampa"><b>¡Ojo!</b> %s</div></div>'
            % (esc(tit), esc(sub), cuerpo, trampa))


# ── tarea ───────────────────────────────────────────────────────────────────
def tarea(unit):
    tit, ses, snl, pasos = KD.TAREA[unit]
    lis = "".join('<li>%s</li>' % p for p in pasos)
    return ('<div class="tarea"><div class="th"><span class="tic">🎯</span>'
            '<div><b>Tarea final · %s</b><i>%s</i></div></div>'
            '<p class="tes">%s</p><p class="tnl">%s</p><ol>%s</ol>'
            '<p class="hint">¿Listo/a? Graba tu escena en la pestaña '
            '<b>Práctica</b> y escúchala. '
            '<span class="stn">neem op en luister terug</span></p></div>'
            % (esc(tit), esc(snl), esc(ses), esc(snl), lis))


CSS = FONTS + """
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;
      --crema:#F3EEE4;--line:#E7E1DF;--card:#fff;--amber:#B45309;--amberbg:#FEF3C7;
      --disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif;--hand:'Caveat',cursive}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#181513;--crema:#241C1B;--gt:#3A1E20;
                  --line:#3a302e;--card:#211a19;--amberbg:#3A2A0A}
*{box-sizing:border-box}
body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
.stn{color:var(--mut);font-style:italic;font-size:.9em;font-family:var(--body)}
.top{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;padding:20px 22px}
.top h1{font-family:var(--disp);font-weight:800;margin:0;font-size:24px}
.top p{margin:4px 0 0;opacity:.95}
main{max-width:1000px;margin:0 auto;padding:18px 18px 44px}
h2.sec{font-family:var(--disp);font-weight:700;color:var(--gd);font-size:21px;margin:26px 0 6px}
.lead{color:var(--mut);margin:0 0 12px}
.clu{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 16px;margin:12px 0}
.clu-h{display:flex;gap:10px;align-items:center;margin-bottom:8px}
.clu-ic{font-size:22px}
.clu-h b{font-family:var(--disp);font-size:17px;display:block}
.clu-h i{color:var(--mut);font-style:normal;font-size:13px}
.cc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:8px}
.cc{display:flex;flex-direction:column;background:var(--crema);border-radius:11px;padding:8px 11px;position:relative;cursor:pointer}
.cc-es{font-weight:600}
.cc-nl{color:var(--mut);font-size:13px}
.cc-spk{position:absolute;top:6px;right:8px;border:none;background:transparent;cursor:pointer;opacity:.45;font-size:13px}
.suena{background:var(--amberbg);border-left:4px solid var(--amber);border-radius:16px;padding:14px 18px;margin:12px 0}
.suena h4{font-family:var(--disp);color:var(--amber);margin:12px 0 2px;font-size:16px}
.suena p{margin:0 0 8px;font-size:14px}
.sh{display:flex;gap:10px;align-items:center}
.sic{font-size:22px}
.sh b{font-family:var(--disp);font-size:17px;display:block}
.sh i{color:var(--mut);font-style:normal;font-size:13px}
.chips{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:6px}
.shchip,.acchip{border:1.5px solid var(--line);background:var(--card);border-radius:20px;
                padding:6px 13px;cursor:pointer;font-family:var(--body);font-size:14px;color:var(--ink)}
.acchip span{color:var(--mut);font-size:12.5px;margin-left:5px}
.shchip:hover,.acchip:hover{border-color:var(--amber)}
.gram{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 18px;margin:12px 0}
.gh{display:flex;gap:10px;align-items:center;margin-bottom:10px}
.gic{font-size:22px}
.gh b{font-family:var(--disp);font-size:17px;display:block}
.gh i{color:var(--mut);font-style:normal;font-size:13px}
.gr{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;padding:7px 0;border-bottom:1px solid var(--line);font-size:14.5px}
.gr:last-of-type{border-bottom:none}
.gf{font-weight:600}
.ge{color:var(--gd);font-size:13px}
.gn{color:var(--mut);font-size:13px}
@media(max-width:700px){.gr{grid-template-columns:1fr}}
.trampa{background:var(--gt);border-radius:11px;padding:9px 13px;margin-top:10px;font-size:14px}
.tarea{background:var(--card);border:2px solid var(--g);border-radius:16px;padding:14px 18px;margin:12px 0}
.th{display:flex;gap:10px;align-items:center}
.tic{font-size:22px}
.th b{font-family:var(--disp);font-size:17px;display:block;color:var(--gd)}
.th i{color:var(--mut);font-style:normal;font-size:13px}
.tes{font-weight:600;margin:10px 0 2px}
.tnl{color:var(--mut);font-family:var(--hand);font-size:17px;margin:0 0 8px}
.tarea ol{margin:0;padding-left:20px}
.tarea li{margin:5px 0}
.hint{color:var(--mut);font-size:13px;margin-top:10px}
.foot{color:var(--mut);font-size:12px;text-align:center;margin:26px 0 0}
"""


def construir(unit):
    kit = "".join(cluster(*c) for c in KD.CLUSTERS[unit])
    return """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>C4 · Unidad %(u)d · Kit</title><style>%(css)s</style></head><body>
<div class="top"><h1>Unidad %(u)d · Kit</h1>
<p>Todo lo que necesitas en esta unidad: las <b>palabras</b>, cómo <b>suenan</b>,
el <b>patrón</b> que hay detrás y la <b>tarea</b> en la que lo usas.
<span class="stn">woorden, klank, patroon en taak</span></p></div>
<main>
 <h2 class="sec">Las palabras</h2>
 <p class="lead">Pulsa una tarjeta para oírla y lee en voz alta: una palabra que
 nunca has dicho tampoco te sale en una conversación.
 <span class="stn">lees hardop mee</span></p>
 %(kit)s
 <h2 class="sec">Suena bien</h2>
 %(suena)s
 <h2 class="sec">El patrón</h2>
 %(gram)s
 <h2 class="sec">La tarea</h2>
 %(tarea)s
 <div class="foot">C4 · «Bienvenidos al español» · Unidad %(u)d</div>
</main>
<script>
function speak(t){if(!('speechSynthesis'in window))return;
 var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.85;
 var v=speechSynthesis.getVoices().find(function(x){return /^es/i.test(x.lang)});
 if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}
if('speechSynthesis'in window)speechSynthesis.getVoices();
document.querySelectorAll('.cc').forEach(function(c){
 c.onclick=function(){speak(c.getAttribute('data-es'));};});
document.querySelectorAll('.shchip,.acchip').forEach(function(b){
 b.onclick=function(){speak(b.getAttribute('data-w'));};});
</script></body></html>""" % {
        "u": unit, "css": CSS, "kit": kit,
        "suena": suena(unit), "gram": gramatica(unit), "tarea": tarea(unit)}


def main():
    unit = int(os.environ.get("C4_UNIT", "11"))
    salida = os.environ.get("C4_KIT_OUT", "C4_U%d_kgt.html" % unit)
    if unit not in KD.CLUSTERS:
        sys.exit("geen kit-gegevens voor unidad %d in kit_data.py" % unit)
    doc = construir(unit)
    ruta = os.path.join(AQUI, "componentes", salida)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    open(ruta, "w", encoding="utf-8").write(doc)
    print("%s geschreven: %d bytes · U%d · %d chunks"
          % (salida, len(doc), unit, sum(len(c[3]) for c in KD.CLUSTERS[unit])))


if __name__ == "__main__":
    main()
