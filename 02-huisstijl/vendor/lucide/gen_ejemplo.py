#!/usr/bin/env python3
"""Bouwt de vergelijkingsbladzijde «emoji ↔ Lucide», met de echte componenten.

Een iconenkeuze beoordeel je niet op een rasterblad met losse iconen, maar op de
plek waar ze staan: in de badge van een oefening, in de audiokaart, in de
verwijzing naar de PowerPoint. Daarom staan hieronder de componenten uit
`cursus-print.css`, letterlijk, twee keer naast elkaar — links wat er nu staat,
rechts hetzelfde met Lucide.

De cursuskleuren en de fonts komen uit `02-huisstijl/tokens/` en
`02-huisstijl/fonts/`, zodat de proef klopt met het drukwerk.

    python3 02-huisstijl/vendor/lucide/gen_ejemplo.py
        → 02-huisstijl/vendor/lucide/ejemplo_iconos.html
"""
import base64
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(AQUI)))
ROOT = "/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, AQUI)

from iconos import BADGE, icono                      # noqa: E402
sys.path.insert(0, os.path.join(ROOT, "03-build", "web"))
from qr_codigo import qr_svg                         # noqa: E402

TOKENS = json.load(open(os.path.join(ROOT, "02-huisstijl", "tokens", "tokens.json"),
                        encoding="utf-8"))
CURSO = TOKENS["color"]["course"]
NEU = TOKENS["color"]["neutral"]


def fuente(archivo, familia, peso):
    ruta = os.path.join(ROOT, "02-huisstijl", "fonts", archivo)
    b64 = base64.b64encode(open(ruta, "rb").read()).decode()
    return ("@font-face{font-family:'%s';font-weight:%s;font-style:normal;"
            "font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}"
            % (familia, peso, b64))


FUENTES = "".join([
    fuente("BricolageGrotesque-700.woff2", "Bricolage Grotesque", 700),
    fuente("BricolageGrotesque-800.woff2", "Bricolage Grotesque", 800),
    fuente("Inter-400.woff2", "Inter", 400),
    fuente("Inter-600.woff2", "Inter", 600),
])


# ─────────────────────────────────────────────────────────────────────────────
# De componenten, precies zoals ze in de cursus staan. `ic` is een functie die
# ofwel de emoji teruggeeft (zoals nu) ofwel het Lucide-icoon.
# ─────────────────────────────────────────────────────────────────────────────
def acthead(ic):
    return ('<div class="act"><div class="acthead"><span class="anum">1</span><div>'
            '<div class="h">Los números que necesito para la hora</div>'
            '<div class="badges">'
            '<span class="badge skill">%s Escribir</span>'
            '<span class="badge">%s Solo</span>'
            '<span class="badge">± 4 min</span>'
            '<span class="badge">★☆☆</span></div></div></div></div>'
            % (ic("✍"), ic("👤")))


def acthead2(ic):
    return ('<div class="act"><div class="acthead"><span class="anum">7</span><div>'
            '<div class="h">Entrevista a tu compañero/a</div>'
            '<div class="badges">'
            '<span class="badge skill">%s Hablar</span>'
            '<span class="badge skill">%s Escuchar</span>'
            '<span class="badge">%s En parejas</span>'
            '<span class="badge">± 8 min</span>'
            '<span class="badge">★★★</span></div></div></div></div>'
            % (ic("🎙"), ic("👂"), ic("👥")))


def audiorow(ic):
    return ('<div class="audiorow"><div class="call"><div class="icb">%s</div>'
            '<div><b>Escucha el diálogo</b> y marca la hora que oyes. '
            '<span class="gloss">Luister en kruis de juiste klok aan.</span></div></div>'
            '<div class="qr"><div class="qrbox">%s</div>'
            '<div class="lab">Escanea y escucha</div>'
            '<div class="meta">Audio 3.1 · La hora · 0:45</div></div></div>'
            % (ic("🎧", 9), ic("qr", 14)))


def guide(ic):
    return ('<div class="guide"><div class="icb">%s</div><div>'
            '<span class="hand">Repasa jugando:</span> '
            '<span class="g">29 spellen met zelfcorrectie op de digitale pagina.</span>'
            "</div></div>" % ic("🎮", 9))


def route(ic):
    return ('<div class="route-note"><span class="icb">%s</span><b>Parada 3 · Barcelona.</b> '
            "Lucía te presenta a su amigo <b>Pau</b>. Con él sigues su <b>rutina diaria</b>."
            "</div>"
            '<div class="route-note"><span class="icb">%s</span><b>En clase:</b> '
            "diapositiva 12 — «¿Qué hora es?».</div>" % (ic("📍"), ic("📊")))


COMPONENTES = [
    ("De oefeningkop met vaardigheidslabels",
     "Het element dat het vaakst terugkomt: elke oefening in de cursus heeft er een. "
     "Zeshonderd keer in C5 alleen al.", acthead),
    ("Een oefening met drie labels",
     "Bij een spreek- of luistertaak staan er meerdere naast elkaar. Daar valt het "
     "verschil in uitlijning het meest op.", acthead2),
    ("De luisterkaart met QR",
     "Hier staat het icoon groot, in een gekleurd vlak. De QR-code ernaast is de echte "
     "code uit U3: hij wijst naar dat luisterfragment op de digitale pagina.", audiorow),
    ("De mochila-gids en de verwijzingen",
     "De verwijzing naar de spellen, naar de parada op de ruta, en naar de dia in de "
     "PowerPoint.", lambda ic: guide(ic) + route(ic)),
]


# een echte code, met de eigen encoder — zo staat er in de proef wat er in het
# boek staat, en niet een symbool dat erop lijkt
_QR = qr_svg("https://espanol-en-la-practica.wim-wuyts1979.chatgpt.site/"
             "c5-u3.html#c5-u3-aud-01", mm=17, nivel="Q")


def emoji(nombre, mm=None):
    return nombre if nombre != "qr" else _QR


def lucide(nombre, mm=None):
    if nombre == "qr":
        return _QR
    n = BADGE.get(nombre)
    return icono(n, mm=mm or 3.6) if n else nombre


def tabla_badges():
    filas = []
    for e, n in BADGE.items():
        filas.append('<div class="par"><span class="pe">%s</span>'
                     '<span class="pi">%s</span><code>%s</code></div>'
                     % (e, icono(n, mm=4.6), n))
    return '<div class="pares">%s</div>' % "".join(filas)


def colores():
    cel = []
    for k, v in CURSO.items():
        cel.append('<div class="col" style="--c:%s;--ct:%s">'
                   '<div class="chip">%s%s%s</div><code>%s</code></div>'
                   % (v["primary"], v["tint"],
                      icono("headphones", mm=5), icono("mic", mm=5),
                      icono("book-open", mm=5), v["name"]))
    return '<div class="cols">%s</div>' % "".join(cel)


CSS = """
%(fuentes)s
*{box-sizing:border-box}
:root{
 --g:%(g)s; --gd:%(gd)s; --gt:%(gt)s;
 --ink:%(ink)s; --mut:%(grey)s; --paper:%(paper)s; --crema:%(crema)s; --line:%(line)s;
 --fondo:#F7F5F0; --panel:#FFFFFF; --texto:#20242E; --suave:%(grey)s; --borde:%(line)s;
 --disp:'Bricolage Grotesque',ui-sans-serif,system-ui,sans-serif;
 --body:Inter,ui-sans-serif,system-ui,sans-serif;
}
@media (prefers-color-scheme:dark){
 :root:not([data-theme="light"]){
  --fondo:#14161A; --panel:#1C1F25; --texto:#ECEBE6; --suave:#9BA0AA; --borde:#2C2F37;
 }
}
:root[data-theme="dark"]{
 --fondo:#14161A; --panel:#1C1F25; --texto:#ECEBE6; --suave:#9BA0AA; --borde:#2C2F37;
}
body{margin:0;background:var(--fondo);color:var(--texto);font-family:var(--body);
 font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.wrap{max-width:1080px;margin:0 auto;padding:56px 24px 96px;display:flex;
 flex-direction:column;gap:56px}
header{display:flex;flex-direction:column;gap:14px;max-width:62ch}
.eyebrow{font-size:12px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;
 color:var(--g)}
h1{font-family:var(--disp);font-weight:800;font-size:clamp(30px,4.4vw,46px);line-height:1.05;
 margin:0;text-wrap:balance;letter-spacing:-.015em}
.lead{font-size:17px;color:var(--suave);margin:0;max-width:60ch}
h2{font-family:var(--disp);font-weight:700;font-size:22px;margin:0 0 4px;letter-spacing:-.01em}
.sub{font-size:14px;color:var(--suave);margin:0 0 20px;max-width:64ch}
section{display:flex;flex-direction:column}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:20px}
@media(max-width:860px){.duo{grid-template-columns:1fr}}
.lado{display:flex;flex-direction:column;gap:8px;min-width:0}
.tag{font-size:11px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;
 color:var(--suave)}
.tag.nu{color:var(--suave)}
.tag.new{color:var(--g)}

/* ── de drukproef: hier gelden de kleuren van het papier, in beide thema's,
      want zo komt de bladzijde uit de printer ── */
.hoja{background:var(--paper);color:var(--ink);border:1px solid var(--line);
 border-radius:14px;padding:22px 22px 24px;overflow-x:auto}
.hoja .act{margin:0}
.acthead{display:flex;gap:13px;align-items:center}
.anum{width:34px;height:34px;border-radius:50%%;background:var(--g);color:#fff;
 font-family:var(--disp);font-weight:800;font-size:15px;display:flex;align-items:center;
 justify-content:center;flex:none}
.h{font-family:var(--disp);font-weight:700;font-size:15.5px;line-height:1.25}
.badges{display:flex;flex-wrap:wrap;gap:6px;margin-top:5px}
.badge{font-size:10.5px;font-weight:600;border-radius:20px;padding:3px 10px;
 background:var(--crema);color:var(--ink);display:inline-flex;align-items:center;gap:5px;
 white-space:nowrap}
.badge.skill{background:var(--gt);color:var(--gd)}
.audiorow{display:grid;grid-template-columns:1fr auto;gap:16px;align-items:stretch}
@media(max-width:520px){.audiorow{grid-template-columns:1fr}}
.call{display:flex;gap:14px;align-items:flex-start;background:var(--gt);border-radius:14px;
 padding:15px 18px;font-size:14px;color:var(--ink)}
.icb{flex:none;display:flex;align-items:center;justify-content:center;color:var(--gd);
 font-size:22px;line-height:1}
.qr{background:#fff;border:1px solid var(--line);border-radius:14px;padding:11px 14px;
 text-align:center;width:132px;flex:none}
.qrbox{display:flex;align-items:center;justify-content:center;height:56px;color:var(--ink);
 font-size:38px;line-height:1}
.qr .lab{font-size:11px;font-weight:600;margin-top:4px}
.qr .meta{font-size:9.5px;color:var(--mut)}
.guide{display:flex;gap:14px;align-items:center;background:#fff;border:1.5px dashed var(--g);
 border-radius:16px;padding:13px 18px;font-size:14px;color:var(--ink)}
.hand{font-weight:600;color:var(--gd)}
.g{color:var(--ink)}
.route-note{font-size:12.5px;color:var(--gd);background:var(--gt);border-radius:9px;
 padding:9px 16px;margin-top:12px}
.route-note .icb{display:inline-flex;margin-right:5px;font-size:14px}
.gloss{color:var(--mut);font-style:italic}

/* ── het overzicht van de 26 labels ── */
.pares{display:grid;grid-template-columns:repeat(auto-fill,minmax(178px,1fr));gap:2px;
 background:var(--borde);border:1px solid var(--borde);border-radius:12px;overflow:hidden}
.par{display:flex;align-items:center;gap:11px;background:var(--panel);padding:11px 14px}
.pe{font-size:17px;width:22px;text-align:center;flex:none}
.pi{color:var(--g);display:flex;flex:none}
.par code{font-size:11.5px;color:var(--suave);font-family:ui-monospace,SFMono-Regular,
 Menlo,monospace;overflow:hidden;text-overflow:ellipsis}

/* ── meekleuren met de cursuskleur ── */
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px}
.col{display:flex;flex-direction:column;gap:7px;align-items:flex-start}
.chip{display:flex;gap:12px;background:var(--ct);color:var(--c);border-radius:12px;
 padding:14px 16px;width:100%%;justify-content:center}
.col code{font-size:12px;color:var(--suave);font-family:ui-monospace,Menlo,monospace}

.nota{background:var(--panel);border:1px solid var(--borde);border-left:3px solid var(--g);
 border-radius:12px;padding:18px 22px;font-size:14.5px;color:var(--texto)}
.nota b{font-weight:600}
.nota + .nota{margin-top:12px}
ul{margin:8px 0 0;padding-left:20px}
li{margin:5px 0;font-size:14.5px}
.behouden{display:flex;gap:26px;flex-wrap:wrap;align-items:center;background:var(--paper);
 color:var(--ink);border:1px solid var(--line);border-radius:14px;padding:18px 22px}
.behouden div{display:flex;flex-direction:column;gap:3px;align-items:center}
.behouden .t{font-size:23px;line-height:1}
.behouden .n{font-size:11px;color:var(--mut)}
footer{font-size:13px;color:var(--suave);border-top:1px solid var(--borde);padding-top:22px}
code.inl{font-family:ui-monospace,Menlo,monospace;font-size:.9em;background:var(--crema);
 color:var(--ink);padding:1px 5px;border-radius:4px}
"""


def pagina():
    partes = []
    for titulo, sub, fn in COMPONENTES:
        partes.append(
            '<section><h2>%s</h2><p class="sub">%s</p><div class="duo">'
            '<div class="lado"><span class="tag nu">Nu · emoji</span>'
            '<div class="hoja">%s</div></div>'
            '<div class="lado"><span class="tag new">Met Lucide</span>'
            '<div class="hoja">%s</div></div></div></section>'
            % (titulo, sub, fn(emoji), fn(lucide)))

    css = CSS % {"fuentes": FUENTES, "g": CURSO["c5"]["primary"],
                 "gd": CURSO["c5"]["dark"], "gt": CURSO["c5"]["tint"],
                 "ink": NEU["light"]["ink"], "grey": NEU["light"]["grey"],
                 "paper": NEU["light"]["paper"], "crema": NEU["light"]["crema"],
                 "line": NEU["light"]["line"]}

    return """<!doctype html><html lang="nl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lucide in de cursus — een drukproef</title>
<style>%s</style></head><body><div class="wrap">
<header>
  <span class="eyebrow">Español en la práctica · huisstijl</span>
  <h1>Lucide in de cursus</h1>
  <p class="lead">CLAUDE.md §15 koos Lucide als iconenset, maar de set stond niet in de
  repo en de units gebruiken emoji. Hier staat dezelfde bladzijde twee keer: links wat
  er nu gedrukt wordt, rechts hetzelfde met Lucide. De componenten, kleuren en fonts
  komen uit de cursus zelf — de witte vlakken houden hun papierkleur, ook in een donker
  thema, want zo komen ze uit de printer.</p>
</header>
%s
<section><h2>De 26 labels die vertaald zijn</h2>
<p class="sub">Alleen wat op elke bladzijde terugkeert: de vaardigheden, de werkvormen
en de dragers. De naam eronder is de naam in Lucide.</p>
%s</section>

<section><h2>Wat een lijnicoon kan en een emoji niet</h2>
<p class="sub">Een emoji is een plaatje met vaste kleuren. Een Lucide-icoon is een lijn
die <code class="inl">currentColor</code> erft — dus het kleurt vanzelf mee met de cursus.</p>
%s
<div class="nota" style="margin-top:18px"><b>Drie dingen die daarmee vanzelf goedkomen.</b>
<ul>
<li><b>Grijswaarden.</b> Een cursus wordt gekopieerd. Emoji worden dan modderige vlekjes;
een lijnicoon blijft een lijn.</li>
<li><b>Lijndikte.</b> Het icoon staat op 1,9 in plaats van Lucide's eigen 2 — op 3,5 mm
naast Inter oogt 2 net te zwaar. Dat is een knop die bij een emoji niet bestaat.</li>
<li><b>Eén beeldtaal.</b> Emoji zien er op Windows, Mac en Android anders uit. Wat jij
in de PDF ziet, is niet noodzakelijk wat de leerling op de digitale pagina ziet.</li>
</ul></div></section>

<section><h2>Wat níét verandert</h2>
<p class="sub">Deze tekens zijn typografie, geen emoji. Ze doen hun werk en zouden als
lijnicoon slechter worden, niet beter.</p>
<div class="behouden">
<div><span class="t">★★☆</span><span class="n">moeilijkheid · 2871×</span></div>
<div><span class="t">☐</span><span class="n">aankruisvak · 1697×</span></div>
<div><span class="t">→</span><span class="n">in een keten · 1582×</span></div>
<div><span class="t">🔴🟠🟢</span><span class="n">semáforo · 343×</span></div>
<div><span class="t">🇪🇸 🇲🇽</span><span class="n">vlaggen op de ruta</span></div>
</div></section>

<section><h2>Wat het kost</h2>
<div class="nota"><b>Het is een zichtbare ingreep op zestien afgewerkte units.</b>
De iconen staan in ongeveer 2400 badges verspreid over C5 en C6+, plus de digitale
pagina's en de PowerPoints. Technisch is het één doorloop — de vertaaltabel staat klaar
en de generatoren draaien opnieuw. Maar het verandert wél hoe elke bladzijde eruitziet,
en dat is een keuze die jij maakt, niet ik.</div>
<div class="nota"><b>Een tussenweg.</b> Alleen de vaardigheidslabels omzetten
(Escribir · Escuchar · Hablar · Leer) en de rest laten staan. Dat is het element dat
het vaakst terugkeert en waar de winst het grootst is, zonder dat de hele cursus
van uitzicht verandert.</div></section>

<footer>Iconen: <b>Lucide</b>, ISC-licentie, 1766 stuks — in de repo onder
<code class="inl">02-huisstijl/vendor/lucide/</code> met de licentie en de herkomst.
Fonts: Bricolage Grotesque en Inter, uit de huisstijl van het project.</footer>
</div></body></html>""" % (css, "".join(partes), tabla_badges(), colores())


if __name__ == "__main__":
    salida = os.path.join(AQUI, "ejemplo_iconos.html")
    open(salida, "w", encoding="utf-8").write(pagina())
    print("geschreven: %s (%.0f kB)" % (salida, os.path.getsize(salida) / 1024))
