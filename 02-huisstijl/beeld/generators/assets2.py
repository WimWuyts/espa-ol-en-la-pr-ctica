#!/usr/bin/env python3
# Composite flat-vector illustraties (concrete items) in de C5-huisstijl.
# Bouwt voort op cast_gen. Levert svg_map2.json (key = substring van [BEELD]-placeholder).
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cast_gen as C

G="#1E9E74"; GD="#157355"; GT="#E4F4EE"; CREMA="#F3EEE4"; LINE="#E4E3DE"; LINE2="#CFCEC8"
INK="#20242E"; MUT="#6A6E78"; AMBER="#E8B04B"; RED="#DC2626"; PAPER="#FCFBF8"; OCEAN="#DCEFF0"
LUC=C.LUC; DIE=C.DIE; VAL=C.VAL; NIN=C.NIN

def _inner(svg):
    return svg.split(">",1)[1].rsplit("</svg>",1)[0]

def av(name, x, y, r):
    s=C.make(name,"avatar",2*r)
    inner=_inner(s)
    return f'<g transform="translate({x-r},{y-r}) scale({2*r/200})">{inner}</g>'

# ---------- 1. Cast quote-strip (§4 groeten) ----------
def quote_strip():
    people=[("lucia","¡Hola!"),("diego","¡Buenos días!"),("valen","¿Qué tal?"),("nina","¡Buenas!")]
    out=[f'<svg viewBox="0 0 720 150" width="100%" role="img" aria-label="De vier reisgenoten groeten je: ¡Hola!, ¡Buenos días!, ¿Qué tal?, ¡Buenas!" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">']
    W=180
    for i,(n,txt) in enumerate(people):
        ox=i*W+30
        # tekstballon
        out.append(f'<rect x="{ox-4}" y="8" width="150" height="40" rx="20" fill="#fff" stroke="{C.CAST[n]["acc"]}" stroke-width="2"/>')
        out.append(f'<path d="M{ox+24} 46 l10 12 l6 -12 Z" fill="#fff" stroke="{C.CAST[n]["acc"]}" stroke-width="2"/>')
        out.append(f'<path d="M{ox+25} 47 h18" stroke="#fff" stroke-width="3"/>')
        out.append(f'<text x="{ox+71}" y="33" text-anchor="middle" font-size="15" font-weight="700" font-family="Bricolage Grotesque,sans-serif" fill="{GD}">{txt}</text>')
        out.append(av(n, ox+42, 105, 40))
    out.append('</svg>')
    return "".join(out)

# ---------- 2. mochila zet sombrero op «café» (§2) ----------
def cafe_sombrero():
    m=_inner(C.mochila(1))  # niet gebruikt; we tekenen los
    return f'''<svg viewBox="0 0 460 150" width="100%" role="img" aria-label="De mochila zet een klein hoedje (tilde) op de é van café." xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">
  <g transform="translate(6,4) scale(0.56)">{_inner(C.mochila(1,'star'))}</g>
  <text x="250" y="96" text-anchor="middle" font-size="58" font-weight="700" font-family="Bricolage Grotesque,sans-serif" fill="{INK}">caf<tspan fill="{GD}">é</tspan></text>
  <path d="M300 40 l16 -15 l5 7 Z" fill="{AMBER}"/>
  <path d="M170 70 q26 -14 44 0" stroke="{LINE2}" stroke-width="2.5" fill="none" stroke-dasharray="2 5"/>
  <path d="M214 70 l-6 -3 l1 7 Z" fill="{LINE2}"/>
</svg>'''

# ---------- 3. Vocabulary opener (§V): mochila + flip-cards ----------
def vocab_opener():
    cards=""
    words=[("hola",LUC),("café",VAL),("uno",DIE),("mapa",NIN)]
    for i,(w,col) in enumerate(words):
        x=250+ (i%2)*115; y=18+(i//2)*66
        cards+=(f'<g transform="rotate({-4 if i%2 else 4} {x+50} {y+26})">'
                f'<rect x="{x}" y="{y}" width="100" height="52" rx="9" fill="#fff" stroke="{col}" stroke-width="2"/>'
                f'<text x="{x+50}" y="{y+33}" text-anchor="middle" font-size="17" font-weight="700" font-family="Bricolage Grotesque,sans-serif" fill="{col}">{w}</text></g>')
    return f'''<svg viewBox="0 0 480 168" width="100%" role="img" aria-label="De mochila met woordkaarten: je woordenschat van Unidad 0 als flashcards." xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">
  <g transform="translate(20,-6) scale(0.72)">{_inner(C.mochila(1,'map'))}</g>
  {cards}
</svg>'''

# ---------- 4. PhotoCards → concrete telbare items (§3) ----------
def _cactus(x,y,s,col="#3E8E5A"):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-5" y="-24" width="10" height="34" rx="5" fill="{col}"/><rect x="-16" y="-14" width="8" height="7" rx="3.5" fill="{col}"/><rect x="-16" y="-20" width="8" height="10" rx="4" fill="{col}"/><rect x="8" y="-18" width="8" height="7" rx="3.5" fill="{col}"/><rect x="8" y="-24" width="8" height="10" rx="4" fill="{col}"/></g>'
def _palm(x,y,s):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-3" y="-20" width="6" height="30" rx="3" fill="#9A6B3F"/><g fill="#3E8E5A"><ellipse cx="0" cy="-22" rx="4" ry="12" transform="rotate(0 0 -22)"/><ellipse cx="0" cy="-22" rx="4" ry="12" transform="rotate(55 0 -22)"/><ellipse cx="0" cy="-22" rx="4" ry="12" transform="rotate(-55 0 -22)"/><ellipse cx="0" cy="-22" rx="4" ry="12" transform="rotate(110 0 -22)"/><ellipse cx="0" cy="-22" rx="4" ry="12" transform="rotate(-110 0 -22)"/></g></g>'
def _tapa(x,y,s):
    return f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="0" cy="4" rx="18" ry="5" fill="#E9DEC8"/><ellipse cx="0" cy="0" rx="18" ry="6" fill="#fff" stroke="{LINE}"/><circle cx="0" cy="-1" r="7" fill="#D98B4A"/><circle cx="0" cy="-3" r="3" fill="{RED}"/></g>'
def _sello(x,y,s):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-14" y="-16" width="28" height="32" rx="2" fill="#fff" stroke="{MUT}" stroke-dasharray="2 2"/><rect x="-9" y="-11" width="18" height="16" fill="{GT}"/><circle cx="0" cy="-3" r="4" fill="{AMBER}"/><rect x="-9" y="7" width="18" height="4" fill="{VAL}"/></g>'
def item_cards():
    # aantal getekend = het echte aantal (telkaart klopt): kleine, telbare hoeveelheden
    data=[(3,"cactus",_cactus),(5,"palmeras",_palm),(4,"tapas",_tapa),(6,"sellos",_sello)]
    out=[f'<svg viewBox="0 0 720 150" width="100%" role="img" aria-label="Telkaarten met telbare items: 3 cactussen, 5 palmbomen, 4 tapas, 6 postzegels." xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">']
    W=176
    for i,(num,lbl,fn) in enumerate(data):
        ox=i*W+8
        out.append(f'<rect x="{ox}" y="8" width="{W-16}" height="134" rx="12" fill="#fff" stroke="{LINE}"/>')
        for k in range(num):
            ix=ox+26+(k%3)*45; iy=52+(k//3)*46
            out.append(fn(ix,iy,0.78))
        out.append(f'<text x="{ox+(W-16)/2}" y="132" text-anchor="middle" font-size="10" fill="{MUT}">{lbl}</text>')
    out.append('</svg>')
    return "".join(out)

# ---------- 5. Bingo 4x4 (§3) ----------
def bingo():
    import itertools
    nums=[7,42,15,90, 33,61,4,88, 20,55,12,99, 3,71,46,28]
    out=[f'<svg viewBox="0 0 300 300" width="60%" role="img" aria-label="Bingokaart met zestien getallen tussen 0 en 100." xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">']
    out.append(f'<rect x="4" y="4" width="292" height="292" rx="16" fill="#fff" stroke="{GD}" stroke-width="3"/>')
    out.append(f'<rect x="4" y="4" width="292" height="44" rx="16" fill="{G}"/><rect x="4" y="30" width="292" height="18" fill="{G}"/>')
    out.append(f'<text x="150" y="34" text-anchor="middle" font-size="20" font-weight="700" font-family="Bricolage Grotesque,sans-serif" fill="#fff">¡BINGO!</text>')
    for i,n in enumerate(nums):
        r=i//4; c=i%4; x=20+c*66; y=64+r*56
        out.append(f'<rect x="{x}" y="{y}" width="58" height="48" rx="9" fill="{CREMA if (r+c)%2 else GT}"/>')
        out.append(f'<text x="{x+29}" y="{y+31}" text-anchor="middle" font-size="18" font-weight="700" font-family="Bricolage Grotesque,sans-serif" fill="{INK}">{n}</text>')
    out.append('</svg>')
    return "".join(out)

# ---------- 6. Chat mockup (§4) ----------
def chat():
    msgs=[("in","Lucía","¡Hola! ¿Qué tal?"),("out","Tú","¡Hola! Bien, ¿y tú?"),("in","Lucía","Muy bien. ¿Cómo te llamas?"),("out","Tú","Me llamo…")]
    out=[f'<svg viewBox="0 0 340 300" width="62%" role="img" aria-label="Chatgesprek: Lucía en jij groeten elkaar en stellen je voor." xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">']
    out.append(f'<rect x="4" y="4" width="332" height="292" rx="22" fill="#fff" stroke="{LINE}" stroke-width="2"/>')
    out.append(f'<rect x="4" y="4" width="332" height="42" rx="22" fill="{GT}"/><rect x="4" y="24" width="332" height="22" fill="{GT}"/>')
    out.append(av("lucia",30,25,15))
    out.append(f'<text x="54" y="30" font-size="12" font-weight="700" fill="{GD}">Lucía</text>')
    y=60
    for kind,who,txt in msgs:
        w=12+len(txt)*7.2
        if kind=="in":
            out.append(f'<rect x="16" y="{y}" width="{w}" height="34" rx="16" fill="{GT}"/><text x="{16+w/2}" y="{y+22}" text-anchor="middle" font-size="13" fill="{INK}">{txt}</text>')
        else:
            out.append(f'<rect x="{324-w}" y="{y}" width="{w}" height="34" rx="16" fill="{G}"/><text x="{324-w/2}" y="{y+22}" text-anchor="middle" font-size="13" fill="#fff">{txt}</text>')
        y+=46
    out.append('</svg>')
    return "".join(out)

# ---------- 7. Poster «Cartel de la clase» (§4) ----------
def poster():
    rows=["¿Cómo se dice … en español?","¿Puedes repetir, por favor?","Más despacio, por favor.","No entiendo. / No sé.","¿Cómo se escribe?"]
    out=[f'<svg viewBox="0 0 360 300" width="66%" role="img" aria-label="Klasposter: la lengua de clase — nuttige zinnen om hulp te vragen." xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">']
    out.append(f'<rect x="6" y="6" width="348" height="288" rx="14" fill="#fff" stroke="{GD}" stroke-width="3"/>')
    out.append(f'<rect x="6" y="6" width="348" height="50" rx="14" fill="{G}"/><rect x="6" y="34" width="348" height="22" fill="{G}"/>')
    out.append(f'<text x="180" y="38" text-anchor="middle" font-size="19" font-weight="700" font-family="Bricolage Grotesque,sans-serif" fill="#fff">LA LENGUA DE CLASE</text>')
    # pin
    out.append(f'<circle cx="180" cy="14" r="7" fill="{RED}"/><circle cx="180" cy="14" r="3" fill="#fff"/>')
    for i,t in enumerate(rows):
        y=76+i*42
        out.append(f'<circle cx="30" cy="{y+9}" r="6" fill="{[LUC,DIE,VAL,NIN,AMBER][i]}"/>')
        out.append(f'<text x="46" y="{y+14}" font-size="14" fill="{INK}">{t}</text>')
    out.append('</svg>')
    return "".join(out)

# ---------- 8. Social profile mockups (§3 teléfonos) ----------
def profiles():
    data=[("lucia","Lucía","Sevilla","611 24 30 ··"),("diego","Diego","CDMX","55 18 07 ··")]
    out=[f'<svg viewBox="0 0 560 190" width="100%" role="img" aria-label="Twee profielkaartjes van de cast met telefoonnummers." xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">']
    for i,(n,nm,city,tel) in enumerate(data):
        ox=i*290+6
        out.append(f'<rect x="{ox}" y="8" width="264" height="172" rx="16" fill="#fff" stroke="{LINE}"/>')
        out.append(f'<rect x="{ox}" y="8" width="264" height="52" rx="16" fill="{C.CAST[n]["acc"]}" opacity="0.16"/><rect x="{ox}" y="40" width="264" height="20" fill="{C.CAST[n]["acc"]}" opacity="0.16"/>')
        out.append(av(n, ox+52, 58, 34))
        out.append(f'<text x="{ox+100}" y="44" font-size="16" font-weight="700" font-family="Bricolage Grotesque,sans-serif" fill="{GD}">{nm}</text>')
        out.append(f'<text x="{ox+100}" y="62" font-size="10" fill="{MUT}">{city}</text>')
        out.append(f'<text x="{ox+22}" y="110" font-size="11" fill="{MUT}">📞 teléfono</text>')
        out.append(f'<rect x="{ox+22}" y="120" width="220" height="34" rx="9" fill="{GT}"/><text x="{ox+34}" y="142" font-size="16" font-weight="700" font-family="Bricolage Grotesque,sans-serif" fill="{INK}">{tel}</text>')
    out.append('</svg>')
    return "".join(out)

# ---------- 9. Mapa del mundo hispano (Cultura) ----------
def mundo_map():
    # gestileerde reiskaart: zachte oceaan, twee vereenvoudigde landmassa's, pins + cast op paradas, legenda
    W,H=720,300
    out=[f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Kaart van de Spaanstalige wereld: España en heel Hispanoamérica opgelicht, met de vier reishaltes España, México, Colombia en Perú." xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">']
    out.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="16" fill="{OCEAN}"/>')
    # Amerika-strip (links, verticaal golvend blob)
    out.append(f'<path d="M60 40 C 150 40, 150 90, 120 120 C 100 140, 150 170, 130 210 C 115 250, 150 270, 110 285 L60 285 Z" fill="#CFE6C9"/>')
    # Iberia + Afrika-hoekje (rechts boven)
    out.append(f'<path d="M560 60 C 620 50, 690 70, 680 110 C 670 140, 610 140, 590 120 C 575 105, 545 90, 560 60 Z" fill="#CFE6C9"/>')
    out.append(f'<path d="M640 150 C 680 150, 690 190, 665 210 C 645 225, 625 200, 630 175 Z" fill="#D8E8CD"/>')  # Afrika-hoek (Guinea Ecuatorial)
    # paradas met cast-avatars
    paradas=[("España",620,95,"lucia"),("México",95,95,"diego"),("Colombia",118,175,"valen"),("Perú",100,235,"nina")]
    # route-lijn España -> Amerika
    out.append(f'<path d="M600 100 C 420 40, 250 70, 120 95" stroke="{GD}" stroke-width="2.6" fill="none" stroke-dasharray="2 7"/>')
    # opgelichte landen-labels (Hispanoamérica) als kleine pins
    others=[("Guatemala",70,120),("Cuba",150,110),("Venezuela",150,150),("Ecuador",95,200),
            ("Bolivia",135,255),("Chile",95,270),("Argentina",140,278),("Panamá",120,150),("Uruguay",150,272),("Paraguay",145,240)]
    for nm,x,y in others:
        out.append(f'<circle cx="{x}" cy="{y}" r="3.2" fill="{G}"/>')
    for nm,x,y,who in paradas:
        out.append(f'<path d="M{x} {y+14} l-9 -14 a11 11 0 1 1 18 0 Z" fill="{GD}"/>')
        out.append(av(who,x,y-6,12))
        out.append(f'<rect x="{x-30}" y="{y+16}" width="60" height="16" rx="8" fill="#fff"/><text x="{x}" y="{y+28}" text-anchor="middle" font-size="9.5" font-weight="700" fill="{GD}">{nm} ★</text>')
    # EE.UU. markering
    out.append(f'<rect x="40" y="46" width="70" height="16" rx="8" fill="#fff" opacity="0.9"/><text x="75" y="58" text-anchor="middle" font-size="8" fill="{MUT}">EE. UU. · muchos</text>')
    # legenda
    out.append(f'<g transform="translate(452,246)"><rect x="0" y="0" width="260" height="46" rx="10" fill="#fff" opacity="0.95"/>'
               f'<circle cx="16" cy="15" r="4" fill="{G}"/><text x="26" y="19" font-size="9" fill="{INK}">lengua oficial</text>'
               f'<path d="M126 19 l-5 -8 a6 6 0 1 1 10 0 Z" fill="{GD}"/><text x="138" y="19" font-size="9" fill="{INK}">nuestras paradas ★</text>'
               f'<text x="16" y="36" font-size="8.4" fill="{MUT}">+20 países oficiales · España · Guinea Ecuatorial · LatAm</text></g>')
    out.append('</svg>')
    return "".join(out)

MAP={
 "de mochila viajera zet een klein sombrero": cafe_sombrero(),
 "CharacterQuote-strip": quote_strip(),
 "PosterMockup": poster(),
 "ChatMockup": chat(),
 "8 kleine PhotoCards": item_cards(),
 "FormMockup bingokaart": bingo(),
 "SocialProfileMockup": profiles(),
 "mapa del mundo hispano": mundo_map(),
 "VocabularyOpener": vocab_opener(),
}

if __name__=="__main__":
    d=os.path.dirname(os.path.abspath(__file__))
    json.dump(MAP, open(os.path.join(d,"svg_map2.json"),"w"))
    # QA-sheet
    html=f'<!doctype html><meta charset=utf-8><style>body{{background:{PAPER};font-family:Inter;padding:10mm}}h4{{color:{GD};margin:8mm 0 2mm}}.wrap{{max-width:190mm}}</style><div class=wrap>'
    for k,v in MAP.items():
        html+=f'<h4>{k}</h4>{v}'
    html+='</div>'
    open(os.path.join(d,"assets2_test.html"),"w").write(html)
    for k,v in MAP.items(): print(k,"->",len(v))
