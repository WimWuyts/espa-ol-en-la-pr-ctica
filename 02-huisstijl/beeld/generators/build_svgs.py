#!/usr/bin/env python3
# Genereert de schematische huisstijl-SVG's voor U0 (grammatica-diagrammen + panelen).
# Kleuren = tokens. Grijswaarden-veilig: vorm/positie/label dragen info, niet enkel kleur.
import json, os

G="#1E9E74"; GD="#157355"; GT="#E4F4EE"; CREMA="#F3EEE4"; LINE="#E4E3DE"; LINE2="#CFCEC8"
INK="#20242E"; MUT="#6A6E78"; RED="#DC2626"; AMBER="#B7860B"; AMBERBG="#FBF3D6"; PAPER="#FCFBF8"
DISP="'Bricolage Grotesque',sans-serif"; BODY="'Inter',sans-serif"

def wrap(vb_w, vb_h, body, label):
    return (f'<svg viewBox="0 0 {vb_w} {vb_h}" width="100%" role="img" aria-label="{label}" '
            f'style="margin:3mm 0;font-family:{BODY}">'
            f'<defs><style>.d{{font-family:{DISP};font-weight:700}}</style></defs>{body}</svg>')

def cars(x, y, sylls, tonica, unit=1.0):
    """Teken een 'lettergreep-trein': afgeronde wagonnetjes, tónica groter+vetter+sombrero."""
    out=[]; cx=x
    for i,s in enumerate(sylls):
        strong = (i==tonica)
        w = 15 + len(s)*9.5 + (6 if strong else 0)
        h = 30 if strong else 24
        cy = y-(h-24)  # groter wagon iets hoger uitgelijnd op onderkant
        fill = GT if strong else "#fff"
        stroke = GD if strong else LINE
        sw = 2 if strong else 1.2
        out.append(f'<rect x="{cx:.1f}" y="{cy:.1f}" width="{w:.1f}" height="{h}" rx="7" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        # wielen
        out.append(f'<circle cx="{cx+7:.1f}" cy="{y+24+3:.1f}" r="2.6" fill="{MUT}"/>'
                   f'<circle cx="{cx+w-7:.1f}" cy="{y+24+3:.1f}" r="2.6" fill="{MUT}"/>')
        tcol = GD if strong else INK
        tw = "700" if strong else "500"
        fs = 14 if strong else 11.5
        out.append(f'<text x="{cx+w/2:.1f}" y="{y+24-8+(0 if strong else 0):.1f}" text-anchor="middle" '
                   f'font-size="{fs}" font-weight="{tw}" fill="{tcol}" class="{"d" if strong else ""}">{s}</text>')
        if strong:
            # sombrero (´) boven het wagon
            mx=cx+w/2
            out.append(f'<path d="M{mx-7:.1f} {cy-5:.1f} L{mx+3:.1f} {cy-12:.1f} L{mx+5:.1f} {cy-9:.1f} Z" fill="{AMBER}"/>')
        # koppeling
        if i < len(sylls)-1:
            out.append(f'<line x1="{cx+w:.1f}" y1="{y+12:.1f}" x2="{cx+w+6:.1f}" y2="{y+12:.1f}" stroke="{LINE2}" stroke-width="2.4"/>')
        cx += w + 6
    return "".join(out), cx

# ---------- 1. SílabaStrip ----------
def silabastrip():
    words=[(["ca","fé"],1),(["ca","sa"],0),(["mé","xi","co"],0),(["te","lé","fo","no"],1)]
    cells=[]
    W=360; H=96
    for idx,(syl,ton) in enumerate(words):
        col=idx%2; row=idx//2
        ox=col*W; oy=row*H
        body,_=cars(ox+16, oy+40, syl, ton)
        cells.append(f'<g>{body}</g>')
    body="".join(cells)
    return wrap(720, 200, body, "Vier woorden in lettergrepen; de sterke lettergreep (tónica) is groter en draagt een hoedje: café, casa, México, teléfono.")

# ---------- 2. TresFamiliasPoster ----------
def tresfamilias():
    cols=[("AGUDA","laatste","ca·FÉ",["ca","fé"],1,"1 van achteren"),
          ("LLANA","voorlaatste","CA·sa",["ca","sa"],0,"2 van achteren"),
          ("ESDRÚJULA","3de van achteren","MÉ·xi·co",["mé","xi","co"],0,"3 van achteren")]
    out=[]; W=236
    for i,(name,pos,lbl,syl,ton,cnt) in enumerate(cols):
        ox=6+i*W
        out.append(f'<rect x="{ox}" y="6" width="{W-12}" height="180" rx="12" fill="#fff" stroke="{LINE}"/>')
        out.append(f'<rect x="{ox}" y="6" width="{W-12}" height="30" rx="12" fill="{GT}"/>'
                   f'<rect x="{ox}" y="20" width="{W-12}" height="16" fill="{GT}"/>')
        out.append(f'<text x="{ox+14}" y="26" font-size="13" class="d" fill="{GD}">{name}</text>')
        out.append(f'<text x="{ox+(W-12)-14}" y="25" text-anchor="end" font-size="8.5" fill="{MUT}">klap: {pos}</text>')
        body,_=cars(ox+18, 78, syl, ton)
        out.append(body)
        out.append(f'<text x="{ox+(W-12)/2}" y="138" text-anchor="middle" font-size="9" fill="{MUT}">tónica = {cnt}</text>')
        out.append(f'<text x="{ox+(W-12)/2}" y="162" text-anchor="middle" font-size="13" class="d" fill="{INK}">{lbl}</text>')
    return wrap(720, 196, "".join(out), "Drie families naar de plaats van de klemtoon: aguda (laatste), llana (voorlaatste), esdrújula (derde van achteren).")

# ---------- 3. DosMontones ----------
def dosmontones():
    con=[("café","é"),("Perú","ú"),("jamón","n"),("adiós","s")]
    sin=[("Madrid","d"),("reloj","j"),("casa","a"),("lunes","s")]
    out=[]
    def stack(ox,title,items,con=True):
        out.append(f'<text x="{ox+120}" y="20" text-anchor="middle" font-size="12" class="d" fill="{GD if con else MUT}">{title}</text>')
        for i,(w,last) in enumerate(items):
            y=34+i*33; sk=GD if con else LINE2
            out.append(f'<rect x="{ox+10}" y="{y}" width="220" height="27" rx="7" fill="#fff" stroke="{sk}" stroke-width="{1.6 if con else 1.2}"/>')
            out.append(f'<text x="{ox+24}" y="{y+18}" font-size="13" fill="{INK}">{w}</text>')
            # laatste letter groot rechts
            box=GT if con else CREMA
            out.append(f'<rect x="{ox+188}" y="{y+4}" width="34" height="19" rx="5" fill="{box}"/>'
                       f'<text x="{ox+205}" y="{y+18}" text-anchor="middle" font-size="12" class="d" fill="{GD if con else MUT}">-{last}</text>')
            if con:
                out.append(f'<path d="M{ox+30} {y-4} L{ox+40} {y-11} L{ox+42} {y-8} Z" fill="{AMBER}"/>')
    stack(6,"CON sombrero (´)",con,True)
    out.append(f'<line x1="360" y1="20" x2="360" y2="170" stroke="{LINE}" stroke-dasharray="3 4"/>')
    stack(372,"SIN sombrero",sin,False)
    return wrap(720, 180, "".join(out), "Twee stapels woorden: links met accent (café, Perú, jamón, adiós), rechts zonder (Madrid, reloj, casa, lunes).")

# ---------- 4. Beslisboom ----------
def beslisboom():
    out=[]
    def node(x,y,w,h,txt,fill,stroke,tcol,fs=11,cls=""):
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>')
        out.append(f'<text x="{x+w/2}" y="{y+h/2+4}" text-anchor="middle" font-size="{fs}" fill="{tcol}" class="{cls}">{txt}</text>')
    def arrow(x1,y1,x2,y2,lbl="",lx=0,ly=0,col=MUT):
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="1.8"/>')
        out.append(f'<path d="M{x2-4} {y2-6} L{x2} {y2} L{x2+4} {y2-6}" fill="{col}"/>' if y2>y1 else
                   f'<path d="M{x2-5} {y2} L{x2} {y2} L{x2} {y2-5}" fill="none"/>')
        if lbl: out.append(f'<text x="{lx}" y="{ly}" font-size="9.5" font-weight="700" fill="{col}">{lbl}</text>')
    # start
    node(280,6,160,34,"¿Oyes la tónica?",GT,GD,GD,12,"d")
    arrow(360,40,360,58)
    node(270,58,180,30,"1. ¿En qué sílaba?",CREMA,LINE,INK)
    arrow(360,88,360,104)
    node(250,104,220,30,"2. ¿Es esdrújula? (3ª de atrás)",CREMA,LINE,INK)
    # sí -> tilde
    arrow(470,119,556,119,"SÍ",500,113,GD)
    node(556,104,158,30,"→ siempre ´",GT,GD,GD,11,"d")
    # no
    arrow(360,134,360,150,"NO",368,146,RED)
    node(232,150,256,30,"3. ¿Termina en -n, -s o vocal?",CREMA,LINE,INK)
    arrow(232,165,150,165,"AGUDA→SÍ ´",70,158,GD)
    node(6,150,140,30,"aguda: SÍ ´ / llana: NO",GT,GD,GD,9.5)
    arrow(488,165,600,165,"LLANA→NO",520,158,MUT)
    node(600,150,114,30,"llana: NO ´",CREMA,LINE2,MUT,10)
    return wrap(720, 194, "".join(out), "Beslisschema voor de tilde: hoor de klemtoon, bepaal de sílaba; esdrújula krijgt altijd een accent; anders hangt het af van de laatste letter (-n, -s of klinker).")

# ---------- 5. InfographicPanel drie lagen (números) ----------
def drielagen():
    out=[]
    def band(y,lbl,sub,chips,col):
        out.append(f'<rect x="6" y="{y}" width="708" height="54" rx="11" fill="#fff" stroke="{LINE}"/>')
        out.append(f'<rect x="6" y="{y}" width="150" height="54" rx="11" fill="{col}"/><rect x="120" y="{y}" width="36" height="54" fill="{col}"/>')
        out.append(f'<text x="18" y="{y+24}" font-size="12" class="d" fill="#fff">{lbl}</text>')
        out.append(f'<text x="18" y="{y+42}" font-size="8.5" fill="#EAF6F0">{sub}</text>')
        cx=172
        for c in chips:
            w=14+len(c)*8
            out.append(f'<rect x="{cx}" y="{y+15}" width="{w}" height="24" rx="6" fill="{CREMA}"/>'
                       f'<text x="{cx+w/2}" y="{y+31}" text-anchor="middle" font-size="11" fill="{INK}">{c}</text>')
            cx+=w+8
        return
    band(6,"CAPA 1","los cimientos · uit het hoofd",["cero","cinco","diez","quince"],G)
    band(68,"CAPA 2","16–29 · één woord, geen «y»",["dieciséis","veinte","veintidós","veintinueve"],GD)
    band(130,"CAPA 3","30–100 · decena + y + unidad",["treinta","cuarenta y dos","noventa y nueve"],AMBER)
    out.append(f'<text x="360" y="196" text-anchor="middle" font-size="9" fill="{MUT}">Vanaf 30: schrijf je drie losse woorden — decena + <tspan font-weight="700">y</tspan> + unidad.</text>')
    return wrap(720, 204, "".join(out), "De getallen in drie opbouwlagen: 0–15 uit het hoofd, 16–29 als één woord, 30–100 met decena plus y plus eenheid.")

# ---------- 7. RouteMap-mini (sectie-opener) ----------
def routemini():
    out=[]
    stops=[("España",56,"active"),("México",250,""),("Colombia",420,""),("Perú",620,"")]
    out.append(f'<path d="M40 46 C 150 18, 210 18, 250 42" stroke="{LINE2}" stroke-width="2.6" fill="none" stroke-dasharray="2 6"/>')
    out.append(f'<path d="M250 42 C 340 70, 520 70, 620 40" stroke="{LINE2}" stroke-width="2.6" fill="none" stroke-dasharray="2 6"/>')
    out.append(f'<text x="150" y="16" fill="{MUT}" font-size="10" font-style="italic">« el charco »</text>')
    for name,x,st in stops:
        if st=="active":
            out.append(f'<circle cx="{x}" cy="46" r="11" fill="{G}"/><circle cx="{x}" cy="46" r="18" fill="none" stroke="{G}" stroke-width="2" opacity=".4"/>')
            out.append(f'<path d="M{x-4} {46} l4 -6 l4 6 l-4 3 Z" fill="#fff"/>')  # sterretje-vorm klein
            out.append(f'<text x="{x}" y="74" fill="{GD}" font-size="12" font-weight="700" text-anchor="middle">{name} ★</text>')
        else:
            out.append(f'<circle cx="{x}" cy="46" r="8" fill="#fff" stroke="{LINE2}" stroke-width="2.6"/>')
            out.append(f'<text x="{x}" y="72" fill="{MUT}" font-size="11" text-anchor="middle">{name}</text>')
    # mochila op de kade bij España
    out.append(f'<text x="34" y="34" font-size="15">🎒</text>')
    return wrap(700, 88, "".join(out), "Mini-routekaart van La Ruta: we vertrekken bij España (halte gemarkeerd met een ster), daarna oversteek naar México, Colombia en Perú.")

# ---------- 8. La Ruta — sombrero-stickers ----------
def larutastickers():
    places=[("España",0),("Madrid",0),("Sevilla",0),("Barcelona",0),("València",0),
            ("México",1),("Cartagena",0),("Bogotá",1),("Cusco",0),("Perú",1),("Panamá",1)]
    out=[]; x=8; y=30
    for name,hat in places:
        w=22+len(name)*8.6
        if x+w>712: x=8; y+=42
        fill=GT if hat else "#fff"; sk=GD if hat else LINE
        out.append(f'<rect x="{x}" y="{y}" width="{w:.0f}" height="26" rx="13" fill="{fill}" stroke="{sk}"/>')
        out.append(f'<text x="{x+w/2:.0f}" y="{y+17}" text-anchor="middle" font-size="12" fill="{INK}">{name}</text>')
        if hat:
            mx=x+w/2
            out.append(f'<path d="M{mx-8:.0f} {y-3} L{mx+2:.0f} {y-11} L{mx+4:.0f} {y-8} Z" fill="{AMBER}"/>')
        x+=w+10
    out.append(f'<text x="8" y="18" font-size="9.5" font-weight="700" fill="{MUT}">LA RUTA · ¿qué nombres llevan sombrero?</text>')
    return wrap(720, y+42, "".join(out), "De tien haltes van de route; de plaatsnamen met een tilde (México, Bogotá, Perú, Panamá) dragen een hoedje-sticker.")

# ---------- 9. SummaryQuadrant (spiekkaart) ----------
def summaryquadrant():
    out=[]
    quads=[("🗺️","EL MUNDO","+20 países · España → México · Colombia · Perú","0,0"),
           ("🔊","EL SONIDO","h muda · b=v · j/ge/gi=jota · ll/y=«j» · ñ=«nj» · z/ce/ci=«th»","1,0"),
           ("＾","EL SOMBRERO","aguda/llana/esdrújula · esdrújula→siempre ´ · aguda -n/-s/vocal → ´","0,1"),
           ("123","NÚMEROS & SALUDOS","0–15 · 16–29 één woord · 30+ decena y unidad · Hola/¿Qué tal?","1,1")]
    W=326; GUT=56; H=100; RGUT=26
    xs=[6, 6+W+GUT]; ys=[6, 6+H+RGUT]
    for ic,ti,tx,pos in quads:
        c,r=[int(v) for v in pos.split(",")]
        ox=xs[c]; oy=ys[r]
        out.append(f'<rect x="{ox}" y="{oy}" width="{W}" height="{H}" rx="12" fill="#fff" stroke="{LINE}"/>')
        out.append(f'<circle cx="{ox+24}" cy="{oy+25}" r="14" fill="{GT}"/><text x="{ox+24}" y="{oy+30}" text-anchor="middle" font-size="14">{ic}</text>')
        out.append(f'<text x="{ox+46}" y="{oy+30}" font-size="12" class="d" fill="{GD}">{ti}</text>')
        words=tx.split(" · "); lines=[]; cur=""
        for w in words:
            if len(cur)+len(w)>40: lines.append(cur); cur=w
            else: cur=(cur+" · "+w) if cur else w
        lines.append(cur)
        for i,ln in enumerate(lines[:4]):
            out.append(f'<text x="{ox+15}" y="{oy+50+i*15}" font-size="9" fill="{INK}">{ln}</text>')
    # mochila in de kruis-gutter (raakt geen kwadrant-inhoud)
    cx=6+W+GUT/2; cy=6+H+RGUT/2
    out.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="22" fill="{G}"/><text x="{cx:.0f}" y="{cy+8:.0f}" text-anchor="middle" font-size="20">🎒</text>')
    return wrap(720, ys[1]+H+8, "".join(out), "Overzichtsplaat van Unidad 0 in vier vakken: de wereld, de klanken, het accent, en de getallen en groeten, met de mochila in het midden.")

svgs={
 "sectie-opener — kleine RouteMap": routemini(),
 "klein kaartje van La Ruta": larutastickers(),
 "SummaryQuadrant": summaryquadrant(),
 "SílabaStrip": silabastrip(),
 "TresFamiliasPoster": tresfamilias(),
 "DosMontones": dosmontones(),
 "beslisboompje": beslisboom(),
 'InfographicPanel «de drie lagen»': drielagen(),
}
d=os.path.dirname(os.path.abspath(__file__))
json.dump(svgs, open(os.path.join(d,"svg_map.json"),"w"))
for k,v in svgs.items():
    print(k, "->", len(v), "chars")
