#!/usr/bin/env python3
"""De schrijfcoach: kijkt de eindtaak na vóór de leerling ze inlevert.

WAT HET DOET
De leerling schrijft zijn tarea final in het venster en drukt op «Nakijken».
Hij krijgt terug, in een vaste vorm:

  1. wat er al in staat — per onderdeel van de opdracht
  2. wat er nog ontbreekt
  3. **één** ding om te verbeteren, niet tien
  4. de zin waarin dat zit, om te herschrijven

Die vorm is niet willekeurig. Een leerling die twaalf rode strepen krijgt,
herschrijft niets; wie er één krijgt met de zin erbij, wel. Daarom houdt de
coach zich in: één correctie per beurt, net als de oefenpartner.

WAAR DE CRITERIA VANDAAN KOMEN
Uit het rollenspel van dezelfde unit (`rol_data.py`): elke beurt daar is
precies «de leerling moet dit kunnen zeggen», mét het patroon om het te
herkennen. Wat de scène niet dekt, staat in `tarea_data.py`. Zo kan de
schriftelijke taak niet iets anders vragen dan de mondelinge oefent.

DE HONESTHEIDSREGEL, ALWEER
De coach kent alleen de fouten die in `corrector_data.py` staan. Hij zegt dus
nooit «goed», maar «ik zie geen fouten die ik ken». En hij zet er altijd bij dat
de leerkracht het laatste woord heeft — een leerling mag niet denken dat een
groen vinkje een cijfer is.

OFFLINE, EN DE TEKST BLIJFT VAN DE LEERLING
Geen server, geen model, niets dat verstuurd wordt. De tekst staat in de
pagina; met «Bewaar» downloadt hij ze als tekstbestand naar zijn eigen toestel.

    python3 gen_coach.py C5 5      # → componentes/C5_U5_coach.html
"""
import html
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import corrector_data as CD                # noqa: E402
import rol_data as RD                      # noqa: E402
import tarea_data as TD                    # noqa: E402


def esc(s):
    return html.escape(s, quote=True)


CSS = """
.coach .brief{background:var(--gt);border-radius:14px;padding:13px 16px;margin:0 0 12px}
.coach .brief b{font-weight:700}
.coach .brief dl{display:grid;grid-template-columns:auto 1fr;gap:3px 10px;margin:8px 0 0;
  font-size:14px}
.coach .brief dt{font-weight:600;color:var(--gd)}
.coach .brief dd{margin:0}
.coach textarea{width:100%;min-height:190px;border:1.5px solid var(--line);
  border-radius:13px;padding:12px 14px;font:inherit;font-size:15.5px;line-height:1.6;
  background:var(--card);color:inherit;resize:vertical}
.coach textarea:focus{outline:none;border-color:var(--g)}
.coach .barra2{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:10px 0 0}
.coach .cuenta{font-size:13px;color:var(--mut);margin-left:auto}
.coach .cuenta b{color:var(--ink)}
.coach .res{margin-top:14px}
.coach .bloque{border:1px solid var(--line);border-radius:13px;padding:12px 14px;
  margin:0 0 10px;background:var(--card)}
.coach .bloque h4{margin:0 0 7px;font-size:14px;font-family:var(--disp);font-weight:700}
.coach ul.chk{list-style:none;margin:0;padding:0;font-size:14.5px}
.coach ul.chk li{padding:3px 0 3px 24px;position:relative}
.coach ul.chk li:before{position:absolute;left:0;top:3px;font-weight:700}
.coach ul.chk li.si:before{content:"✓";color:var(--g)}
.coach ul.chk li.no:before{content:"○";color:var(--mut)}
.coach ul.chk li.no{color:var(--mut)}
.coach .uno{border-color:#C0392B;background:#C0392B0d}
.coach .uno .zin{display:block;margin-top:7px;padding:8px 11px;background:var(--card);
  border-radius:9px;border:1px dashed var(--line);font-size:14.5px}
.coach .arreglo{width:100%;margin-top:8px;border:1.5px solid var(--line);
  border-radius:10px;padding:9px 12px;font:inherit;font-size:15px;background:var(--card);
  color:inherit}
.coach .arreglo:focus{outline:none;border-color:var(--g)}
.coach .nota{font-size:12.5px;color:var(--mut);margin:10px 0 0}
"""

JS = """
(function(){
const D=%(datos)s, R=%(reglas)s;
const raiz=document.getElementById('%(id)s');
if(!raiz) return;
const ta=raiz.querySelector('textarea'), res=raiz.querySelector('.res'),
      cuenta=raiz.querySelector('.cuenta');

function palabras(t){ return (t.trim().match(/[\\wáéíóúñü]+/gi)||[]).length; }
function pinta(){
  const n=palabras(ta.value);
  cuenta.innerHTML='<b>'+n+'</b> woorden · streefdoel '+D.min+'–'+D.meta;
}
ta.addEventListener('input',pinta); pinta();

// De zin waarin de fout staat, zodat de leerling weet wélke hij herschrijft.
function fraseCon(txt,re){
  const partes=txt.split(/(?<=[.!?¿¡\\n])\\s+/).filter(Boolean);
  for(const f of partes){ if(new RegExp(re,'i').test(f)) return f.trim(); }
  return txt.trim().slice(0,120);
}

raiz.querySelector('[data-rev]').onclick=function(){
  const t=ta.value.trim();
  if(!t){ res.innerHTML='<div class="bloque">Schrijf eerst je tekst hierboven.</div>'; return; }
  const n=palabras(t);
  const hechos=[], faltan=[];
  D.criterios.forEach(function(c){
    (c.re.some(function(p){return new RegExp(p,'i').test(t);}) ? hechos : faltan).push(c.nl);
  });
  // één ding om te verbeteren — nooit een hele lijst
  let fallo=null;
  for(const g of R){ if(new RegExp(g.re,'i').test(t)){ fallo=g; break; } }

  let h='';
  h+='<div class="bloque"><h4>Onderdelen die ik terugvind</h4><ul class="chk">'+
     (hechos.map(function(x){return '<li class="si">'+x+'</li>';}).join('')
      || '<li class="no">nog geen enkel onderdeel van de opdracht</li>')+'</ul></div>';
  if(faltan.length){
    h+='<div class="bloque"><h4>Onderdelen die ik nog niet vind</h4><ul class="chk">'+
       faltan.map(function(x){return '<li class="no">'+x+'</li>';}).join('')+'</ul></div>';
  }
  if(n<D.min){
    h+='<div class="bloque"><h4>Lengte</h4>Je tekst telt <b>'+n+'</b> woorden. '+
       'Voor deze taak zijn er minstens <b>'+D.min+'</b> nodig — er mag dus nog iets bij.</div>';
  }
  if(fallo){
    h+='<div class="bloque uno"><h4>Eén ding om te verbeteren</h4>'+fallo.nl+
       '<span class="zin">'+fraseCon(t,fallo.re).replace(/</g,'&lt;')+'</span>'+
       '<input class="arreglo" type="text" placeholder="Herschrijf die ene zin hier…" '+
       'aria-label="Herschrijf de zin">'+
       '<div class="nota">Zo kan het: <b>'+fallo.bien+'</b></div></div>';
  }else{
    // bewust géén «goed» — de coach kent niet alles
    h+='<div class="bloque"><h4>Fouten</h4>Ik zie hier geen fouten die ik ken. '+
       'Dat betekent niet dat er geen zijn — laat je tekst nog aan je leerkracht zien.</div>';
  }
  res.innerHTML=h;
  const arr=res.querySelector('.arreglo'); if(arr) arr.focus();
};

raiz.querySelector('[data-guarda]').onclick=function(){
  const t=ta.value;
  if(!t.trim()) return;
  const b=new Blob([D.titulo+'\\n\\n'+t+'\\n'],{type:'text/plain;charset=utf-8'});
  const a=document.createElement('a');
  a.href=URL.createObjectURL(b);
  a.download=D.archivo+'.txt'; a.click();
  URL.revokeObjectURL(a.href);
};
})();
"""


def criterios(curso, unidad):
    """Wat er in de tekst hoort: uit het rollenspel plus wat daar niet in past."""
    out = []
    r = RD.rol(curso, unidad)
    if r:
        for p in r["pasos"]:
            # alleen de eerste zin: «Kies een hoofdgerecht. Zeg er iets bij…»
            # is in de scène een instructie, maar in dit lijstje een
            # onderdeel dat er wel of niet in staat.
            etiqueta = re.split(r"(?<=[.!?])\s", p["meta"])[0].rstrip(".")
            out.append({"nl": etiqueta, "re": p["acepta"]})
    for label, pats in TD.tarea(curso, unidad)["extra"]:
        out.append({"nl": label, "re": pats})
    return out


def componente(curso, unidad, id_base=None):
    t = TD.tarea(curso, unidad)
    if not t:
        return None
    ident = id_base or ("coach_%s_u%d"
                        % (curso.replace("+", "plus").lower(), unidad))
    crit = criterios(curso, unidad)
    datos = {"titulo": t["titulo"], "min": t["palabras"][0], "meta": t["palabras"][1],
             "criterios": crit,
             "archivo": "%s_U%d_%s" % (curso.replace("+", "plus"), unidad,
                                       t["titulo"].split()[0].lower())}
    cuerpo = """
<div class="card coach" id="%(id)s">
  <h3 style="margin:0 0 4px;font-family:var(--disp)">Antes de entregar · %(tit)s</h3>
  <p class="lead" style="margin:0 0 10px">Schrijf je eindtaak hier en laat ze
    nakijken vóór je ze afgeeft. De coach werkt zonder internet en je tekst
    blijft op je eigen toestel.</p>
  <div class="brief">
    <b>De opdracht</b>
    <dl><dt>Aan wie</dt><dd>%(para)s</dd>
        <dt>Waarvoor</dt><dd>%(obj)s</dd>
        <dt>Hoe lang</dt><dd>%(min)d tot %(meta)d woorden</dd></dl>
  </div>
  <textarea aria-label="Jouw tekst" placeholder="Escribe aquí tu tarea…"></textarea>
  <div class="barra2">
    <button class="btn" data-rev>Nakijken</button>
    <button class="btn sec small" data-guarda>Bewaar als tekstbestand</button>
    <span class="cuenta"></span>
  </div>
  <div class="res"></div>
  <p class="nota">De coach kijkt naar de onderdelen van de opdracht en naar een
    vaste lijst met veelgemaakte fouten. Hij geeft geen cijfer en ziet niet
    alles — je leerkracht heeft het laatste woord.</p>
</div>""" % {"id": ident, "tit": esc(t["titulo"]), "para": esc(t["para"]),
             "obj": esc(t["objetivo"]), "min": t["palabras"][0],
             "meta": t["palabras"][1]}
    js = JS % {"datos": json.dumps(datos, ensure_ascii=False),
               "reglas": json.dumps(CD.reglas_para(curso, unidad), ensure_ascii=False),
               "id": ident}
    return cuerpo, CSS, js


COLORES = {"C4": ("#D64550", "#A8323B", "#FBEAEC"),
           "C5": ("#1E9E74", "#157355", "#E4F4EE"),
           "C6+": ("#7C56A9", "#5B3E83", "#EEE8F5")}


def suelto(curso, unidad):
    """Het component als losstaande pagina (voor de C4-hubs en om te bekijken)."""
    hecho = componente(curso, unidad)
    if not hecho:
        return None
    cuerpo, css, js = hecho
    g, gd, gt = COLORES[curso]
    doc = """<!doctype html><html lang="nl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s U%d · schrijfcoach</title><style>
:root{--g:%s;--gd:%s;--gt:%s;--ink:#20242E;--mut:#6A6E78;--line:#E4E3DE;
      --card:#fff;--crema:#F3EEE4;--disp:system-ui,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ink:#ECEBE6;--mut:#9BA0AA;--line:#2C2E36;--card:#1C1E24;--crema:#1E2026}}
:root[data-theme="dark"]{--ink:#ECEBE6;--mut:#9BA0AA;--line:#2C2E36;
  --card:#1C1E24;--crema:#1E2026}
body{font-family:system-ui,sans-serif;background:var(--card);color:var(--ink);
     margin:0;padding:24px;line-height:1.55}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;
      padding:18px 20px;margin:0 auto;max-width:720px}
.lead{color:var(--mut);margin:0 0 14px}
.btn{border:none;background:var(--g);color:#fff;font-weight:700;border-radius:10px;
     padding:9px 16px;cursor:pointer;font-size:14px;font-family:inherit}
.btn.sec{background:var(--crema);color:var(--ink)}
.btn.small{padding:6px 11px;font-size:13px}
.btn:focus-visible{outline:3px solid var(--gd);outline-offset:2px}
%s</style></head><body>%s<script>%s</script></body></html>""" % (
        curso, unidad, g, gd, gt, css, cuerpo, js)
    ruta = os.path.join(AQUI, "componentes",
                        "%s_U%d_coach.html" % (curso.replace("+", "plus"), unidad))
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    open(ruta, "w", encoding="utf-8").write(doc)
    return ruta


def main():
    curso = sys.argv[1] if len(sys.argv) > 1 else "C5"
    unidad = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    ruta = suelto(curso, unidad)
    if not ruta:
        sys.exit("geen eindtaak voor %s U%d" % (curso, unidad))
    print("%s geschreven: %d criteria · %d corrector-regels · %.0f kB"
          % (os.path.basename(ruta), len(criterios(curso, unidad)),
             len(CD.reglas_para(curso, unidad)), os.path.getsize(ruta) / 1024))


if __name__ == "__main__":
    main()
