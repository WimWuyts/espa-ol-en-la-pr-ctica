#!/usr/bin/env python3
"""De voordeur van de site: één pagina met de drie cursussen.

WAAROM DIT ER IS
Er waren 31 losse unit-pagina's en geen enkele plek die ze samenbracht. Dat
betekent dat een leerling 31 links moet krijgen en zelf moet onthouden welke bij
zijn jaar hoort. CLAUDE.md §16 voorziet daarom één pagina met een tabblad per
cursus en daarin het overzicht van de unidades. Dit is die pagina.

WAT ZE WÉL EN NIET DOET
Ze linkt; ze bevat geen leerstof. Alles wat een leerling doet, gebeurt in de
unit-pagina zelf. Daardoor weegt ze niets (geen audio, geen spellen) en kan ze
zonder risico als eerste geüpload worden — de links naar nog niet geüploade
units werken dan gewoon nog niet.

DE NAMEN KOMEN UIT ÉÉN BRON
`enlaces.py` bepaalt onder welke naam elke unit op de site staat. Deze pagina
leest datzelfde bestand, dus portaal en QR-codes kunnen niet uit elkaar lopen.

    python3 gen_portal.py            # → 03-build/web/portal.html
"""
import base64
import html
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)

import enlaces as EN                       # noqa: E402

TOKENS = json.load(open("%s/02-huisstijl/tokens/tokens.json" % ROOT, encoding="utf-8"))
COL = TOKENS["color"]["course"]
NEU = TOKENS["color"]["neutral"]["light"]


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


# ── de drie cursussen ────────────────────────────────────────────────────────
# (code, naam, ondertitel, doelgroep, kleurtoken, etappe uit §12)
CURSOS = [
    ("C4", "¡Bienvenidos al español!", "De vertrekhal — klanken, chunks en je eerste gesprekken.",
     "4 Moderne talen", "c4", "El despegue"),
    ("C5", "Español en la práctica", "Het dagelijks leven: van España naar México, Colombia en Perú.",
     "5de jaar", "c5", "El día a día"),
    ("C6+", "Más español en la práctica · edición única", "Het vervolg: verhalen, het verleden en je eigen mening.",
     "6de jaar", "c6plus", "Historias y mundos"),
]


def titulo_unidad(curso, u):
    """De titel van een unit, uit de gebouwde pagina zelf gelezen.

    Zo staat er op het portaal wat er ook in de unit staat, en hoeft er niets
    met de hand bijgehouden te worden.
    """
    ruta = os.path.join(AQUI, EN.fuente(curso, u))
    if not os.path.exists(ruta):
        return None
    with open(ruta, encoding="utf-8") as fh:
        cabeza = fh.read(4000)
    m = re.search(r"<title>(.*?)</title>", cabeza, re.S)
    if not m:
        return "Unidad %d" % u
    t = html.unescape(re.sub(r"\s+", " ", m.group(1))).strip()
    # de hubs schrijven hun titel elk net anders; hou het deel ná het unitnummer
    t = re.sub(r"\s*—\s*Hub$", "", t)
    m = re.search(r"[Uu](?:nidad)?\s*%d\s*[·:]?\s*(.+)$" % u, t)
    return (m.group(1) if m else t).strip(" ·")


# Uitzonderingen: een unit die ergens ánders staat dan naast dit portaal krijgt
# hier zijn volledige adres. Normaal blijft dit leeg — alles staat op één site
# en de korte bestandsnaam volstaat.
#
# LEEG, EN DAT IS EEN BESLISSING (auteur 2026-08-09). Er is even een proef
# geweest met de pagina's op claude.ai. Die is afgevoerd: **een leerling mag
# geen account of abonnement nodig hebben om bij zijn cursus te kunnen.** Het
# portaal en de units horen dus op de eigen site, en niets hier mag naar een
# platform wijzen waar eerst ingelogd moet worden.
PUBLICADO = {}


def enlace(curso, u):
    return PUBLICADO.get((curso, u)) or EN.pagina(curso, u)


def tarjetas(curso):
    filas = ""
    for u in range(0, 15):
        tit = titulo_unidad(curso, u)
        if tit is None:
            continue
        vivo = (curso, u) in PUBLICADO
        filas += ('<a class="u%s" href="%s"%s><span class="n">%d</span>'
                  '<span class="t">%s</span></a>'
                  % (" vivo" if vivo else "", esc(enlace(curso, u)),
                     ' target="_blank" rel="noopener"' if vivo else "",
                     u, esc(tit)))
    return filas


def paneles():
    out = ""
    for i, (code, nombre, sub, publico, tok, etapa) in enumerate(CURSOS):
        c = COL[tok]
        out += """
<section class="panel%(act)s" id="p-%(tok)s" data-panel="%(tok)s"
         style="--c:%(pri)s;--cd:%(dark)s;--ct:%(tint)s">
  <header class="ph">
    <div class="eyebrow">%(code)s · %(publico)s · La Ruta — %(etapa)s</div>
    <h2>%(nombre)s</h2>
    <p>%(sub)s</p>
  </header>
  <div class="ulist">%(filas)s</div>
</section>""" % {"act": " on" if i == 0 else "", "tok": tok, "code": esc(code),
                 "pri": c["primary"], "dark": c["dark"], "ct": c["tint"],
                 "tint": c["tint"], "publico": esc(publico), "etapa": esc(etapa),
                 "nombre": esc(nombre), "sub": esc(sub), "filas": tarjetas(code)}
    return out


def pestañas():
    return "".join(
        '<button class="tab%s" data-ir="%s" style="--c:%s;--ct:%s">'
        '<span class="pt">%s</span><span class="pn">%s</span></button>'
        % (" on" if i == 0 else "", tok, COL[tok]["primary"], COL[tok]["tint"],
           esc(code), esc(publico))
        for i, (code, _n, _s, publico, tok, _e) in enumerate(CURSOS))


# De kleuren staan als variabelen op :root en worden drie keer gezet: één keer
# licht, één keer voor wie zijn toestel op donker heeft staan, en één keer voor
# wie het expliciet omzet. Dat laatste is nodig zodra de pagina ergens gehost
# staat waar de lezer zelf een thema kiest — zet je een kleur alléén in het
# media-blok, dan valt ze in de derde toestand weg en staat er zwarte tekst op
# een zwarte grond.
CSS = """
:root{
  --paper:%(paper)s; --ink:%(ink)s; --panel:%(panel)s;
  --grey:%(grey)s; --line:%(line)s; --crema:%(crema)s;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --paper:%(dpaper)s; --ink:%(dink)s; --panel:%(dpanel)s;
    --grey:%(dgrey)s; --line:%(dline)s; --crema:%(dcrema)s;
  }
}
:root[data-theme="dark"]{
  --paper:%(dpaper)s; --ink:%(dink)s; --panel:%(dpanel)s;
  --grey:%(dgrey)s; --line:%(dline)s; --crema:%(dcrema)s;
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
     font-family:Inter,system-ui,sans-serif;line-height:1.55;
     -webkit-text-size-adjust:100%%}
.wrap{max-width:980px;margin:0 auto;padding:0 20px 64px}
header.top{padding:44px 0 26px;text-align:center}
.kicker{font-family:Caveat,cursive;font-size:26px;color:var(--grey);margin:0 0 2px}
h1{font-family:'Bricolage Grotesque',system-ui,sans-serif;font-weight:800;
   font-size:clamp(30px,5.4vw,46px);line-height:1.05;margin:0 0 8px;
   letter-spacing:-.02em}
.lead{max-width:56ch;margin:0 auto;color:var(--grey);font-size:16px}
.tabs{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:28px 0 22px}
.tab{cursor:pointer;border:1.5px solid var(--line);background:var(--panel);
     border-radius:14px;padding:9px 16px;font:inherit;font-weight:600;
     color:var(--ink);display:flex;flex-direction:column;align-items:center;
     min-width:118px;transition:.15s}
.tab:hover{border-color:var(--c)}
.tab.on{background:var(--ct);border-color:var(--c);color:var(--cd)}
.tab:focus-visible,.u:focus-visible{outline:3px solid var(--c);outline-offset:2px}
.pt{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:17px}
.pn{font-size:12px;color:var(--grey);font-weight:400}
.tab.on .pn{color:var(--cd)}
.panel{display:none}
.panel.on{display:block;animation:in .18s ease-out}
@keyframes in{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
.ph{border-left:5px solid var(--c);padding:2px 0 2px 16px;margin:0 0 20px}
.eyebrow{font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;
         color:var(--cd);font-weight:600}
.ph h2{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;
       font-size:clamp(22px,3.6vw,30px);margin:3px 0 5px;letter-spacing:-.015em}
.ph p{margin:0;color:var(--grey);font-size:15px}
.ulist{display:grid;gap:11px;grid-template-columns:repeat(auto-fill,minmax(258px,1fr))}
.u{display:flex;align-items:center;gap:13px;text-decoration:none;color:inherit;
   background:var(--panel);border:1.5px solid var(--line);border-radius:14px;
   padding:13px 15px;transition:.15s}
.u:hover{border-color:var(--c);background:var(--ct);transform:translateY(-1px)}
.u .n{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:19px;
      color:#fff;background:var(--c);border-radius:10px;min-width:38px;height:38px;
      display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.u .t{font-weight:600;font-size:14.5px;line-height:1.3}
/* al online: een klein bolletje in de cursuskleur, geen tweede kleur */
.u.vivo .t:after{content:'';display:inline-block;width:7px;height:7px;
  border-radius:50%%;background:var(--c);margin-left:7px;vertical-align:middle}
.tools{margin:34px 0 0;border-top:1px solid var(--line);padding-top:22px}
.tools h3{font-family:'Bricolage Grotesque',sans-serif;font-weight:700;
          font-size:16px;margin:0 0 10px}
.tools .u .n{background:var(--grey);font-size:15px}
footer{margin-top:40px;text-align:center;color:var(--grey);font-size:12.5px}
@media (prefers-reduced-motion:reduce){
  .panel.on{animation:none}
  .u:hover{transform:none}
}
""" % {"paper": NEU["paper"], "ink": NEU["ink"], "grey": NEU["grey"],
       "line": NEU["line"], "panel": NEU["panel"], "crema": NEU["crema"],
       "dcrema": TOKENS["color"]["neutral"]["dark"]["crema"],
       "dpaper": TOKENS["color"]["neutral"]["dark"]["paper"],
       "dink": TOKENS["color"]["neutral"]["dark"]["ink"],
       "dpanel": TOKENS["color"]["neutral"]["dark"]["panel"],
       "dline": TOKENS["color"]["neutral"]["dark"]["line"],
       "dgrey": TOKENS["color"]["neutral"]["dark"]["grey"]}

JS = """
var tabs=document.querySelectorAll('.tab'),pans=document.querySelectorAll('.panel');
function ir(tok,push){
  tabs.forEach(function(t){t.classList.toggle('on',t.dataset.ir===tok);});
  pans.forEach(function(p){p.classList.toggle('on',p.dataset.panel===tok);});
  if(push&&history.replaceState)history.replaceState(null,'','#'+tok);
}
tabs.forEach(function(t){t.onclick=function(){ir(t.dataset.ir,true);};});
// #c5 in het adres opent meteen het juiste tabblad — handig om per klas te delen
var h=(location.hash||'').replace('#','');
if(h)ir(h,false);
"""


def main():
    doc = """<!doctype html><html lang="nl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Español en la práctica · de drie cursussen</title>
<meta name="description" content="Digitale pagina's bij de cursussen Spaans: oefeningen, audio, woordkaarten en spellen.">
<style>%(fonts)s%(css)s</style></head><body>
<div class="wrap">
  <header class="top">
    <p class="kicker">¡Hola!</p>
    <h1>Español en la práctica</h1>
    <p class="lead">Kies je cursus en daarna je unidad. Elke unidad heeft
      luisterfragmenten, woordkaarten, zelfcorrigerende oefeningen en spellen.
      Alles werkt in de browser — je hoeft niets te installeren.</p>
  </header>
  <nav class="tabs">%(tabs)s</nav>
  %(paneles)s
  <section class="tools" style="--c:%(gris)s;--ct:%(crema)s">
    <h3>Voor alle jaren</h3>
    <div class="ulist">
      <a class="u" href="conjugador.html"><span class="n">▦</span>
        <span class="t">Conjugador · werkwoorden opzoeken en zelf vervoegen</span></a>
    </div>
  </section>
  <footer>Español en la práctica · cursusmateriaal Spaans, doorstroomfinaliteit</footer>
</div>
<script>%(js)s</script>
</body></html>""" % {"fonts": FONTS, "css": CSS, "tabs": pestañas(),
                     "paneles": paneles(), "js": JS,
                     "gris": NEU["grey"], "crema": NEU["crema"]}
    ruta = os.path.join(AQUI, "portal.html")
    open(ruta, "w", encoding="utf-8").write(doc)
    n = doc.count('class="u"') + doc.count('class="u vivo"')
    print("portal.html geschreven: %.2f MB · %d links (%d unidades + 1 tool)"
          % (len(doc.encode()) / 1e6, n, n - 1))


if __name__ == "__main__":
    main()
