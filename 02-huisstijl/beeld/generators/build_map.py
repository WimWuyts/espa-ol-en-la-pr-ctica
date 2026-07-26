#!/usr/bin/env python3
# Echte wereldkaart uit Natural Earth (public domain), equirectangular, huisstijl.
# Highlight: alle landen waar Spaans officiële taal is + de 4 paradas met cast-avatars.
import json, os, sys
sys.path.insert(0,"/tmp/claude-0/-home-user-espa-ol-en-la-pr-ctica/c4f0edbd-dbbb-5710-a740-e04235ccd8ef/scratchpad")
import cast_gen as C

G="#1E9E74"; GD="#157355"; GT="#E4F4EE"; INK="#20242E"; MUT="#6A6E78"; AMBER="#E8B04B"
LAND="#E7E4DC"; LANDB="#FBFAF7"; OCEAN="#DCEFF2"; AMBERL="#F6E4BE"

SPA={"ESP","GNQ","MEX","GTM","HND","SLV","NIC","CRI","PAN","CUB","DOM","PRI",
     "COL","VEN","ECU","PER","BOL","PRY","URY","ARG","CHL"}
USA={"USA"}

# venster op de Spaanstalige wereld
LON0,LON1,LAT1,LAT0 = -119.0, 20.0, 45.0, -56.0
W = 760
H = W*(LAT1-LAT0)/(LON1-LON0)

def X(lon): return (lon-LON0)/(LON1-LON0)*W
def Y(lat): return (LAT1-lat)/(LAT1-LAT0)*H

def ring_to_path(ring):
    pts=[]
    for lon,lat in ring:
        pts.append(f"{X(lon):.1f} {Y(lat):.1f}")
    if not pts: return ""
    return "M"+" L".join(pts)+"Z"

def geom_paths(geom):
    t=geom["type"]; coords=geom["coordinates"]; d=""
    if t=="Polygon":
        for ring in coords: d+=ring_to_path(ring)
    elif t=="MultiPolygon":
        for poly in coords:
            for ring in poly: d+=ring_to_path(ring)
    return d

def bbox_in_window(geom):
    def it(c):
        # flatten alle punten
        if isinstance(c[0],(int,float)):
            yield c
        else:
            for x in c:
                yield from it(x)
    xs=[]; ys=[]
    for lon,lat in it(geom["coordinates"]):
        xs.append(lon); ys.append(lat)
    if not xs: return False
    return not (max(xs)<LON0 or min(xs)>LON1 or max(ys)<LAT0 or min(ys)>LAT1)

def iso(props):
    for k in ("ISO_A3_EH","ISO_A3","ADM0_A3","SOV_A3"):
        v=props.get(k)
        if v and v not in ("-99","-1"): return v
    return props.get("NAME","")

gj=json.load(open("/tmp/world.geojson"))
paths=[]
for f in gj["features"]:
    g=f["geometry"]
    if not g: continue
    if not bbox_in_window(g): continue
    code=iso(f["properties"])
    d=geom_paths(g)
    if not d: continue
    if code in SPA:
        fill=G; stroke=LANDB; sw=0.7; cls=' class="spa" data-c="%s"'%code
    elif code in USA:
        fill=AMBERL; stroke=LANDB; sw=0.7; cls=' class="usa" data-c="USA"'
    else:
        fill=LAND; stroke=LANDB; sw=0.6; cls=''
    paths.append(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{cls}/>')

def av_at(name, lon, lat, r=13):
    s=C.make(name,"avatar",2*r); inner=s.split(">",1)[1].rsplit("</svg>",1)[0]
    x=X(lon); y=Y(lat)
    return (f'<path d="M{x:.1f} {y+r*1.5:.1f} l-{r*0.8:.1f} -{r*1.5:.1f} a{r} {r} 0 1 1 {r*1.6:.1f} 0 Z" fill="{GD}"/>'
            f'<g transform="translate({x-r:.1f},{y-r:.1f}) scale({2*r/200})">{inner}</g>')

def label(lon,lat,txt,dy=26):
    x=X(lon); y=Y(lat)
    w=len(txt)*6.2+16
    return (f'<rect x="{x-w/2:.1f}" y="{y+dy:.1f}" width="{w:.1f}" height="16" rx="8" fill="#fff"/>'
            f'<text x="{x:.1f}" y="{y+dy+11.5:.1f}" text-anchor="middle" font-size="9.5" font-weight="700" fill="{GD}">{txt} ★</text>')

paradas=[("lucia",-3.70,40.42,"España"),("diego",-99.13,19.43,"México"),
         ("valen",-75.51,10.42,"Colombia"),("nina",-71.97,-13.53,"Perú")]
markers=""
# route-lijn tussen paradas (over de kaart)
pts=[(-3.70,40.42),(-99.13,19.43),(-75.51,10.42),(-71.97,-13.53)]
route="M"+" L".join(f"{X(a):.1f} {Y(b):.1f}" for a,b in pts)
markers+=f'<path d="{route}" stroke="{GD}" stroke-width="2" fill="none" stroke-dasharray="2 6" opacity=".8"/>'
for n,lo,la,nm in paradas: markers+=label(lo,la,nm)
for n,lo,la,nm in paradas: markers+=av_at(n,lo,la)

legend=(f'<g transform="translate({W-250},{H-56})">'
        f'<rect x="0" y="0" width="244" height="48" rx="10" fill="#fff" opacity="0.95"/>'
        f'<rect x="12" y="12" width="14" height="10" rx="2" fill="{G}"/><text x="32" y="21" font-size="9" fill="{INK}">español lengua oficial (+20 países)</text>'
        f'<rect x="12" y="28" width="14" height="10" rx="2" fill="{AMBERL}"/><text x="32" y="37" font-size="9" fill="{INK}">EE. UU. · muchos hispanohablantes</text>'
        f'</g>')

svg=(f'<svg viewBox="0 0 {W:.0f} {H:.0f}" width="100%" role="img" '
     f'aria-label="Echte wereldkaart met alle landen waar Spaans een officiële taal is opgelicht (Spanje, Equatoriaal-Guinea en heel Latijns-Amerika), en de vier reishaltes España, México, Colombia en Perú gemarkeerd met de personages." '
     f'xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">'
     f'<rect x="0" y="0" width="{W:.0f}" height="{H:.0f}" rx="14" fill="{OCEAN}"/>'
     f'<g>{"".join(paths)}</g>{markers}{legend}</svg>')

d=os.path.dirname(os.path.abspath(__file__))
open(os.path.join(d,"mundo_map_real.svg"),"w").write(svg)
# test-html
open(os.path.join(d,"map_test.html"),"w").write(
    f'<!doctype html><meta charset=utf-8><body style="background:#FCFBF8;padding:8mm;margin:0">'
    f'<div style="max-width:190mm">{svg}</div></body>')
print("SVG bytes:", len(svg), "| paden:", len(paths), "| viewBox", int(W), int(H))
