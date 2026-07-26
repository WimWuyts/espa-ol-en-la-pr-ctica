#!/usr/bin/env python3
# Parametrische flat-vector cast + mochila-mascotte in de C5-huisstijl.
# Elk personage: eigen huid/haar/accentkleur. Reusable buste + circulaire avatar.
# Output: losse SVG-strings via functies; test-HTML render onderaan.

INK="#20242E"; MUT="#6A6E78"; PAPER="#FCFBF8"; GT="#E4F4EE"; GD="#157355"; G="#1E9E74"
AMBER="#E8B04B"
LUC="#E07A5F"; DIE="#5B8DEF"; VAL="#2FA8A0"; NIN="#D69A2E"; TU="#8A7BE0"

SK={"light":"#F3CBA4","med":"#E0AC7E","tan":"#C88E62","deep":"#AA7248"}
SKD={"light":"#E0B084","med":"#C8945F","tan":"#AC7549","deep":"#8E5C36"}

# ---------- haarstijlen (achter- en voorlaag) ----------
def hair_long(c):
    back=f'<path d="M50 108 C 50 52, 150 52, 150 108 L152 182 C 152 150, 134 150, 128 152 L72 152 C 66 150, 48 150, 48 182 Z" fill="{c}"/>'
    front=f'<path d="M58 100 C 66 72, 134 72, 142 100 C 128 84, 112 80, 100 80 C 88 80, 72 84, 58 100 Z" fill="{c}"/>'
    return back, front
def hair_short(c):
    back=f'<path d="M56 96 C 56 56, 144 56, 144 96 L146 118 C 146 104, 140 100, 132 100 L68 100 C 60 100, 54 104, 54 118 Z" fill="{c}"/>'
    front=f'<path d="M58 98 C 62 66, 138 66, 142 98 C 130 82, 116 80, 100 80 C 84 80, 70 82, 58 98 Z" fill="{c}"/>'
    return back, front
def hair_curly(c):
    # wolkje van bolletjes rond de kruin
    bumps=""
    import math
    for i,(dx,dy,r) in enumerate([(-44,-2,20),(-38,-30,20),(-14,-46,22),(16,-48,22),(40,-30,21),(46,-2,19),(-30,-44,18),(30,-44,18),(0,-52,20)]):
        bumps+=f'<circle cx="{100+dx}" cy="{100+dy}" r="{r}" fill="{c}"/>'
    front=f'<path d="M60 96 C 64 74, 136 74, 140 96 C 128 86, 116 84, 100 84 C 84 84, 72 86, 60 96 Z" fill="{c}"/>'
    return bumps, front
def hair_braids(c):
    back=f'<path d="M56 100 C 56 54, 144 54, 144 100 L150 150 L138 150 L136 108 L64 108 L62 150 L50 150 Z" fill="{c}"/>'
    braids=(f'<g fill="{c}">'
            f'<ellipse cx="52" cy="150" rx="10" ry="16"/><ellipse cx="52" cy="176" rx="9" ry="14"/><ellipse cx="52" cy="198" rx="7" ry="11"/>'
            f'<ellipse cx="148" cy="150" rx="10" ry="16"/><ellipse cx="148" cy="176" rx="9" ry="14"/><ellipse cx="148" cy="198" rx="7" ry="11"/>'
            f'</g>')
    front=f'<path d="M58 98 C 64 70, 136 70, 142 98 C 128 84, 100 82, 100 82 C 72 84, 58 98, 58 98 Z" fill="{c}"/>'
    return back+braids, front

def face(skin, skd, expr="smile", jaw="round"):
    if jaw=="square":
        f=f'<path d="M62 100 C 62 70, 138 70, 138 100 C 138 138, 122 156, 100 156 C 78 156, 62 138, 62 100 Z" fill="{skin}"/>'
    else:
        f=f'<path d="M62 102 C 62 68, 138 68, 138 102 C 138 140, 118 158, 100 158 C 82 158, 62 140, 62 102 Z" fill="{skin}"/>'
    ears=f'<circle cx="62" cy="112" r="8" fill="{skin}"/><circle cx="138" cy="112" r="8" fill="{skin}"/>'
    eyes=(f'<ellipse cx="84" cy="108" rx="5.4" ry="6.4" fill="#fff"/><ellipse cx="116" cy="108" rx="5.4" ry="6.4" fill="#fff"/>'
          f'<circle cx="85" cy="109" r="3.1" fill="{INK}"/><circle cx="117" cy="109" r="3.1" fill="{INK}"/>'
          f'<circle cx="83.7" cy="107.4" r="1" fill="#fff"/><circle cx="115.7" cy="107.4" r="1" fill="#fff"/>')
    brows=f'<path d="M77 99 Q84 95 91 99" stroke="{INK}" stroke-width="2.2" fill="none" stroke-linecap="round" opacity=".8"/><path d="M109 99 Q116 95 123 99" stroke="{INK}" stroke-width="2.2" fill="none" stroke-linecap="round" opacity=".8"/>'
    nose=f'<path d="M100 112 L97 122 Q100 125 103 122" stroke="{skd}" stroke-width="2.2" fill="none" stroke-linecap="round"/>'
    if expr=="talk":
        mouth=f'<ellipse cx="100" cy="135" rx="7" ry="5" fill="#B5533F"/><path d="M94 133 Q100 130 106 133" stroke="#fff" stroke-width="0" fill="none"/>'
    else:
        mouth=f'<path d="M90 134 Q100 143 110 134" stroke="#B5533F" stroke-width="3" fill="none" stroke-linecap="round"/>'
    blush=f'<ellipse cx="78" cy="126" rx="6" ry="4" fill="{LUC}" opacity="0.35"/><ellipse cx="122" cy="126" rx="6" ry="4" fill="{LUC}" opacity="0.35"/>'
    return f + ears + eyes + brows + nose + mouth + blush

def bust(skinkey, hairfn, haircol, accent, extra="", expr="smile", jaw="round", w=200):
    skin=SK[skinkey]; skd=SKD[skinkey]
    hb, hf = hairfn(haircol)
    return f'''<svg viewBox="0 0 200 250" width="{w}" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">
  <ellipse cx="100" cy="242" rx="58" ry="6" fill="#000" opacity="0.05"/>
  <path d="M30 250 C 32 198, 66 178, 100 178 C 134 178, 168 198, 170 250 Z" fill="{accent}"/>
  <path d="M100 178 L100 250" stroke="#00000010" stroke-width="6"/>
  <path d="M88 150 h24 v20 a12 12 0 0 1 -24 0 Z" fill="{skd}"/>
  {hb}
  {face(skin,skd,expr,jaw)}
  {hf}
  {extra}
</svg>'''

def avatar(skinkey, hairfn, haircol, accent, extra="", w=120):
    # circulaire avatar: accentcirkel + bust geclipt
    inner=bust(skinkey,hairfn,haircol,accent,extra,w=200)
    inner=inner.split(">",1)[1].rsplit("</svg>",1)[0]  # strip outer svg tag
    return f'''<svg viewBox="0 0 200 200" width="{w}" xmlns="http://www.w3.org/2000/svg">
  <defs><clipPath id="c{accent.replace('#','')}"><circle cx="100" cy="100" r="96"/></clipPath></defs>
  <circle cx="100" cy="100" r="98" fill="{GT}"/>
  <g clip-path="url(#c{accent.replace('#','')})"><g transform="translate(0,26)">{inner}</g></g>
  <circle cx="100" cy="100" r="96" fill="none" stroke="{accent}" stroke-width="4"/>
</svg>'''

# accessoires
FLOWER=lambda col=LUC: f'<g transform="translate(130,90)"><g fill="{col}"><ellipse cx="0" cy="-7" rx="3.2" ry="4.6"/><ellipse cx="0" cy="7" rx="3.2" ry="4.6"/><ellipse cx="-7" cy="0" rx="4.6" ry="3.2"/><ellipse cx="7" cy="0" rx="4.6" ry="3.2"/></g><circle r="2.3" fill="{AMBER}"/></g>'

CAST={
 "lucia": dict(skin="light", hair=hair_long, hc="#3A2A22", acc=LUC, extra=FLOWER(LUC), jaw="round"),
 "diego": dict(skin="med",   hair=hair_short,hc="#1C1610", acc=DIE, extra="", jaw="square"),
 "valen": dict(skin="tan",   hair=hair_curly,hc="#241813", acc=VAL, extra="", jaw="round"),
 "nina":  dict(skin="deep",  hair=hair_braids,hc="#140F0C", acc=NIN, extra="", jaw="round"),
}

def make(name, kind="bust", w=None):
    c=CAST[name]
    if kind=="avatar":
        return avatar(c["skin"], c["hair"], c["hc"], c["acc"], c["extra"], w=w or 120)
    return bust(c["skin"], c["hair"], c["hc"], c["acc"], c["extra"], jaw=c["jaw"], w=w or 200)

def tu_avatar(w=120):
    # «Tú» = de leerling: neutrale vriendelijke avatar, streepjesrand
    inner=bust("med", hair_short, "#2A2320", TU, w=200).split(">",1)[1].rsplit("</svg>",1)[0]
    return f'''<svg viewBox="0 0 200 200" width="{w}" xmlns="http://www.w3.org/2000/svg">
  <defs><clipPath id="ctu"><circle cx="100" cy="100" r="94"/></clipPath></defs>
  <circle cx="100" cy="100" r="98" fill="#fff"/>
  <g clip-path="url(#ctu)"><g transform="translate(0,26)">{inner}</g></g>
  <circle cx="100" cy="100" r="95" fill="none" stroke="{TU}" stroke-width="3.5" stroke-dasharray="7 6"/>
</svg>'''

def mochila(w=200, pose="compass"):
    detail={"compass":f'<circle cx="110" cy="180" r="15" fill="#fff" stroke="{GD}" stroke-width="2.5"/><path d="M110 170 L114 180 L110 190 L106 180 Z" fill="{LUC}"/><circle cx="110" cy="180" r="2.4" fill="{GD}"/>',
            "map":f'<rect x="90" y="166" width="40" height="28" rx="3" fill="#fff" stroke="{GD}" stroke-width="2"/><path d="M95 172 q8 -4 16 0 t16 0" stroke="{VAL}" stroke-width="1.6" fill="none"/><circle cx="120" cy="184" r="2.4" fill="{LUC}"/>',
            "star":f'<path d="M110 168 l4 9 10 1 -7.5 7 2 10 -8.5 -5 -8.5 5 2 -10 -7.5 -7 10 -1 Z" fill="{AMBER}"/>'}[pose]
    return f'''<svg viewBox="0 0 220 250" width="{w}" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="110" cy="238" rx="66" ry="8" fill="#000" opacity="0.06"/>
  <path d="M74 60 C 58 90, 58 150, 74 200" stroke="{GD}" stroke-width="13" fill="none" stroke-linecap="round"/>
  <path d="M146 60 C 162 90, 162 150, 146 200" stroke="{GD}" stroke-width="13" fill="none" stroke-linecap="round"/>
  <rect x="42" y="70" width="136" height="158" rx="40" fill="{G}"/>
  <rect x="42" y="70" width="136" height="158" rx="40" fill="none" stroke="{GD}" stroke-width="3"/>
  <path d="M42 118 Q110 150 178 118 L178 96 Q110 60 42 96 Z" fill="{GD}"/>
  <path d="M92 66 Q110 50 128 66" stroke="{GD}" stroke-width="9" fill="none" stroke-linecap="round"/>
  <rect x="70" y="150" width="80" height="60" rx="18" fill="{GT}"/>
  <rect x="70" y="150" width="80" height="60" rx="18" fill="none" stroke="{GD}" stroke-width="2.5"/>
  {detail}
  <circle cx="90" cy="112" r="6.5" fill="#fff"/><circle cx="130" cy="112" r="6.5" fill="#fff"/>
  <circle cx="91" cy="113" r="3.3" fill="{INK}"/><circle cx="131" cy="113" r="3.3" fill="{INK}"/>
  <circle cx="88.5" cy="111" r="1.1" fill="#fff"/><circle cx="128.5" cy="111" r="1.1" fill="#fff"/>
  <path d="M96 126 Q110 138 124 126" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/>
  <ellipse cx="80" cy="122" rx="6" ry="4" fill="{LUC}" opacity="0.5"/><ellipse cx="140" cy="122" rx="6" ry="4" fill="{LUC}" opacity="0.5"/>
  <path d="M150 74 l10 -9 l3 4 Z" fill="{AMBER}"/>
</svg>'''

if __name__=="__main__":
    import os,json
    d=os.path.dirname(os.path.abspath(__file__))
    # test-lineup
    parts=['<div class="row">']
    labels={"lucia":"Lucía · Sevilla","diego":"Diego · CDMX","valen":"Valen · Cartagena","nina":"Nina · Cusco"}
    for n in ["lucia","diego","valen","nina"]:
        parts.append(f'<div class=c>{make(n,"bust",150)}<div class=nm>{labels[n]}</div></div>')
    parts.append(f'<div class=c>{tu_avatar(150)}<div class=nm>Tú · Flandes</div></div>')
    parts.append(f'<div class=c>{mochila(150)}<div class=nm>Mochila</div></div>')
    parts.append('</div><div class="row">')
    for n in ["lucia","diego","valen","nina"]:
        parts.append(f'<div class=c>{make(n,"avatar",96)}<div class=nm>avatar</div></div>')
    parts.append(f'<div class=c>{mochila(96,"map")}</div><div class=c>{mochila(96,"star")}</div>')
    parts.append('</div>')
    html=f'<!doctype html><meta charset=utf-8><style>body{{background:{PAPER};font-family:Inter,sans-serif;padding:12mm}}.row{{display:flex;gap:12mm;align-items:flex-end;margin-bottom:10mm;flex-wrap:wrap}}.c{{text-align:center}}.nm{{color:{GD};font-weight:700;font-size:10pt;margin-top:3mm}}</style>'+"".join(parts)
    open(os.path.join(d,"cast_lineup.html"),"w").write(html)
    print("wrote cast_lineup.html")
