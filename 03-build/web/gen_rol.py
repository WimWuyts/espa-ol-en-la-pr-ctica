#!/usr/bin/env python3
"""Bouwt het rollenspel-component voor in een unit-pagina.

WAT HET IS
Een gesprek met een rol, een doel en een einde: de leerling bestelt een
maaltijd, doet boodschappen, koopt kleren. De tegenspeler zegt zijn tekst, de
leerling antwoordt — eerst door te kiezen, daarna door zelf te typen — en het
loopt door tot de opdracht klaar is.

WAT HET NIET IS
Er zit geen taalmodel achter. Het draait volledig in de pagina, offline, en
kent alleen wat in `rol_data.py` en `corrector_data.py` staat. Dat is een
bewuste keuze (auteur 2026-08-09): leerlingtekst verlaat de school niet, er is
geen sleutel nodig, en het werkt op elk schoolnetwerk. De prijs is dat de
partner niet improviseert — en juist daarom is de scène gesloten, want dan valt
dat niet op.

DE REGEL DIE NERGENS GEBROKEN MAG WORDEN
De corrector kent alleen de fouten die wij erin gestopt hebben. Hij zegt dus
nooit «goed!», maar «ik zie geen fouten die ik ken». Zie de kop van
`corrector_data.py` voor het waarom.

DRIE MOEILIJKHEIDSGRADEN, EN «COMPLETAR» IS DE BELANGRIJKSTE
«Completar» geeft de zin met twee gaten en een woordbank: de leerling typt de
vorm zelf. Dat is bewust de eerste stand (auteur 2026-08-09) — bij aanklikken
kan hij gokken en heeft hij niets geproduceerd, bij een gat moet hij kiezen
tussen *un* en *una*, tussen *gusta* en *gustan*, en dat is precies waar het om
draait. «Elegir» blijft eronder staan als lichtere trede, en «Escribir» laat
hem de hele zin zelf maken; daar telt het patroon uit `acepta` en kijkt de
corrector mee. Wie vastloopt vraagt een pista of het model; dat wordt geteld,
zodat het slot eerlijk kan zeggen hoeveel er zelfstandig ging.

    python3 gen_rol.py C5 5            # → componentes/C5_U5_rol.html (los te bekijken)
"""
import html
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import corrector_data as CD                # noqa: E402
import rol_data as RD                      # noqa: E402


def esc(s):
    return html.escape(s, quote=True)


CSS = """
.rol{--rb:var(--gt);}
.rol .esc{background:var(--crema);border-radius:14px;padding:14px;min-height:120px;
  max-height:340px;overflow-y:auto;display:flex;flex-direction:column;gap:10px}
.rol .b{display:flex;gap:9px;align-items:flex-start;max-width:86%;
  animation:rolin .22s ease-out}
@keyframes rolin{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.rol .b.yo{align-self:flex-end;flex-direction:row-reverse}
.rol .av{width:30px;height:30px;border-radius:50%;background:var(--gt);flex:0 0 auto;
  display:flex;align-items:center;justify-content:center;font-size:16px}
.rol .b.yo .av{background:var(--g);color:#fff;font-size:13px;font-weight:700}
.rol .tx{background:var(--card);border:1px solid var(--line);border-radius:13px;
  padding:9px 12px;font-size:14.5px;line-height:1.45}
.rol .b.yo .tx{background:var(--g);color:#fff;border-color:transparent}
.rol .tx .nl{display:block;font-size:12.5px;opacity:.72;font-style:italic;margin-top:3px}
.rol .meta{margin:12px 0 8px;font-weight:600;font-size:14px}
.rol .meta .pill{margin-right:7px}
.rol .ops{display:grid;gap:8px}
.rol .op{text-align:left;border:1.5px solid var(--line);background:var(--card);
  border-radius:12px;padding:10px 13px;font:inherit;font-size:14.5px;cursor:pointer;
  transition:.14s;color:inherit}
.rol .op:hover:not(:disabled){border-color:var(--g);background:var(--gt)}
.rol .op:disabled{cursor:default;opacity:.55}
.rol .op.mal{border-color:#C0392B;background:#C0392B12}
.rol .op.bien{border-color:var(--g);background:var(--gt)}
.rol .hue{font-size:16px;line-height:2.1;margin:2px 0 10px}
.rol .gap{display:inline-block;width:7.5em;border:none;border-bottom:2px solid var(--g);
  background:transparent;font:inherit;font-size:16px;text-align:center;padding:1px 3px;
  color:inherit}
.rol .gap:focus{outline:none;background:var(--gt)}
.rol .gap.bien{border-color:var(--g);background:var(--gt);font-weight:700}
.rol .gap.mal{border-color:#C0392B;background:#C0392B14}
.rol .gap:disabled{opacity:1}
.rol .banco{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 10px}
.rol .banco b{font-size:12.5px;color:var(--mut);font-weight:600;align-self:center;
  margin-right:2px}
.rol .banco span{background:var(--crema);border:1px solid var(--line);border-radius:16px;
  padding:3px 11px;font-size:13.5px;cursor:pointer;user-select:none}
.rol .banco span:hover{background:var(--gt);border-color:var(--g)}
.rol .esc-in{display:flex;gap:8px;flex-wrap:wrap}
.rol input.tec{flex:1 1 260px;border:1.5px solid var(--line);border-radius:12px;
  padding:10px 13px;font:inherit;font-size:15px;background:var(--card);color:inherit}
.rol input.tec:focus{outline:none;border-color:var(--g)}
.rol .fb{margin-top:10px;border-radius:12px;padding:10px 13px;font-size:14px;
  border:1px solid var(--line);background:var(--card)}
.rol .fb.mal{border-color:#C0392B;background:#C0392B0f}
.rol .fb.ok{border-color:var(--g);background:var(--gt)}
.rol .fb b{font-weight:700}
.rol .fb .mod{display:block;margin-top:6px;font-family:var(--disp);font-size:15px}
.rol .barra{display:flex;gap:4px;margin:0 0 12px}
.rol .barra i{flex:1;height:5px;border-radius:3px;background:var(--line)}
.rol .barra i.on{background:var(--g)}
.rol .modo{display:flex;gap:6px;margin:0 0 12px}
.rol .modo button{border:1.5px solid var(--line);background:var(--card);color:inherit;
  border-radius:10px;padding:6px 13px;font:inherit;font-size:13.5px;font-weight:600;
  cursor:pointer}
.rol .modo button.on{background:var(--g);color:#fff;border-color:var(--g)}
.rol .fin{text-align:center;padding:6px 0}
.rol .fin .grande{font-family:var(--disp);font-size:20px;font-weight:800;margin:6px 0}
.rol .tally{list-style:none;padding:0;margin:10px 0 0;font-size:14px;text-align:left}
.rol .tally li{padding:4px 0;border-bottom:1px dashed var(--line)}
@media (prefers-reduced-motion:reduce){.rol .b{animation:none}}
"""

JS = """
(function(){
const D=%(datos)s, R=%(reglas)s;
const raiz=document.getElementById('%(id)s');
if(!raiz) return;

// accenten en hoofdletters mogen niet uitmaken: een leerling die «cafe» typt
// bedoelt «café», en daar is deze oefening het moment niet voor.
function normaliza(s){
  return (s||'').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'')
         .replace(/\\s+/g,' ').trim();
}
function casa(txt,pats){
  const t=normaliza(txt);
  return pats.some(function(p){
    return new RegExp(p.normalize('NFD').replace(/[\\u0300-\\u036f]/g,''),'i').test(t);
  });
}
// De corrector kent alleen wat in corrector_data.py staat. Hij mag daarom
// nooit «goed!» zeggen — zie de kop van dat bestand.
function corrige(txt){
  const out=[];
  R.forEach(function(r){
    if(new RegExp(r.re,'i').test(txt)) out.push(r);
  });
  return out;
}

let paso=0, modo='completar', ayudas=0, solos=0, avisos=[];
const esc=raiz.querySelector('.esc'), zona=raiz.querySelector('.zona'),
      barra=raiz.querySelector('.barra');

function burbuja(quien,txt,nl){
  const b=document.createElement('div');
  b.className='b'+(quien==='yo'?' yo':'');
  b.innerHTML='<div class="av">'+(quien==='yo'?'TÚ':D.avatar)+'</div>'+
    '<div class="tx">'+txt+(nl?'<span class="nl">'+nl+'</span>':'')+'</div>';
  esc.appendChild(b); esc.scrollTop=esc.scrollHeight;
}
function pinta(){
  barra.innerHTML=D.pasos.map(function(_,i){
    return '<i class="'+(i<paso?'on':'')+'"></i>';}).join('');
}

function avanza(dicho){
  burbuja('yo',dicho);
  paso++; pinta();
  if(paso>=D.pasos.length){ return fin(); }
  setTimeout(muestra,340);
}

function fin(){
  const p=D.pasos.length;
  burbuja('otro',D.final,D.final_nl);
  let li='';
  li+='<li>Beurten zonder hulp: <b>'+solos+' van de '+p+'</b></li>';
  li+='<li>Hulp gevraagd: <b>'+ayudas+'×</b></li>';
  if(avisos.length){
    li+='<li>Waar je op mag letten:<br>'+
        avisos.filter(function(v,i,a){return a.indexOf(v)===i;})
              .map(function(v){return '• '+v;}).join('<br>')+'</li>';
  }
  zona.innerHTML='<div class="fin"><div class="grande">¡Ya está! 🎉</div>'+
    '<p class="lead" style="margin:0 auto">Je hebt de hele scène afgewerkt.</p>'+
    '<ul class="tally">'+li+'</ul>'+
    '<button class="btn" style="margin-top:12px" data-otra>Otra vez</button></div>';
  zona.querySelector('[data-otra]').onclick=function(){
    paso=0;ayudas=0;solos=0;avisos=[];esc.innerHTML='';pinta();muestra();};
}

function muestra(){
  const p=D.pasos[paso];
  let usado=false;                       // hulp gebruikt in déze beurt
  burbuja('otro',p.di,p.nl);
  let h='<div class="meta"><span class="pill">Tu turno</span>'+p.meta+'</div>';
  if(modo==='completar'){
    // de zin met gaten; het aantal invulvakken volgt uit het kader zelf
    const trozos=p.hueco.marco.split('___');
    let frase='';
    trozos.forEach(function(t,i){
      frase+=t.replace(/</g,'&lt;');
      if(i<trozos.length-1)
        frase+='<input class="gap" data-g="'+i+'" type="text" autocomplete="off" '+
               'spellcheck="false" aria-label="Vul woord '+(i+1)+' in">';
    });
    h+='<div class="banco"><b>Banco:</b>'+p.hueco.banco.map(function(w){
         return '<span>'+w+'</span>';}).join('')+'</div>';
    h+='<div class="hue">'+frase+'</div>';
    h+='<div class="esc-in"><button class="btn" data-comp>Comprobar</button>'+
       '<button class="btn sec small" data-modelo>Muéstrame</button></div>';
  }else if(modo==='elegir'){
    h+='<div class="ops">'+p.opciones.map(function(o,i){
      return '<button class="op" data-i="'+i+'">'+o[0]+'</button>';}).join('')+'</div>';
  }else{
    h+='<div class="esc-in"><input class="tec" type="text" autocomplete="off" '+
       'placeholder="Escribe tu respuesta en español…" aria-label="Jouw antwoord">'+
       '<button class="btn" data-env>Decir</button>'+
       '<button class="btn sec small" data-pista>Pista</button>'+
       '<button class="btn sec small" data-modelo>Muéstrame</button></div>';
  }
  h+='<div class="fb" hidden></div>';
  zona.innerHTML=h;
  const fb=zona.querySelector('.fb');
  function di(clase,texto){fb.hidden=false;fb.className='fb '+clase;fb.innerHTML=texto;}

  if(modo==='completar'){
    const gaps=[].slice.call(zona.querySelectorAll('.gap'));
    // een woord uit de bank zetten we in het vak waar de cursor staat
    let foco=gaps[0];
    gaps.forEach(function(g){g.addEventListener('focus',function(){foco=g;});});
    zona.querySelectorAll('.banco span').forEach(function(ch){
      ch.onclick=function(){
        if(!foco||foco.disabled) foco=gaps.filter(function(g){return !g.disabled;})[0];
        if(!foco) return;
        foco.value=ch.textContent; foco.focus();
      };
    });
    zona.querySelector('[data-modelo]').onclick=function(){
      usado=true; ayudas++;
      di('','<b>Zo kan het:</b><span class="mod">'+p.modelo+'</span>');};
    function comprueba(){
      let todo=true, primerFallo=-1;
      gaps.forEach(function(g,i){
        const bien=p.hueco.respuestas[i].some(function(r){
          return normaliza(r)===normaliza(g.value);});
        g.classList.toggle('bien',bien);
        g.classList.toggle('mal',!bien&&g.value.trim()!=='');
        if(bien){ g.disabled=true; }
        else { todo=false; if(primerFallo<0&&g.value.trim()!=='') primerFallo=i; }
      });
      if(todo){
        if(!usado) solos++;
        let dicho=p.hueco.marco;
        p.hueco.respuestas.forEach(function(r){dicho=dicho.replace('___',r[r.length-1]);});
        di('ok','<b>Klopt.</b> Zo zeg je het.');
        setTimeout(function(){avanza(dicho.charAt(0).toUpperCase()+dicho.slice(1));},700);
      }else{
        usado=true;
        if(primerFallo>=0){
          avisos.push(p.hueco.mal[primerFallo].replace(/<[^>]+>/g,''));
          di('mal','<b>Nog niet.</b> '+p.hueco.mal[primerFallo]);
        }else{
          di('mal','Vul allebei de vakjes in. '+p.pista);
        }
      }
    }
    zona.querySelector('[data-comp]').onclick=comprueba;
    gaps.forEach(function(g){g.addEventListener('keydown',function(e){
      if(e.key==='Enter'){e.preventDefault();comprueba();}});});
    gaps[0].focus();
  }else if(modo==='elegir'){
    zona.querySelectorAll('.op').forEach(function(b){
      b.onclick=function(){
        const o=p.opciones[+b.dataset.i];
        if(o[1]){
          b.classList.add('bien');
          zona.querySelectorAll('.op').forEach(function(x){x.disabled=true;});
          if(!usado) solos++;
          setTimeout(function(){avanza(o[0]);},420);
        }else{
          b.classList.add('mal'); b.disabled=true; usado=true;
          avisos.push(o[2].replace(/<[^>]+>/g,''));
          di('mal','<b>Nog niet.</b> '+o[2]);
        }
      };
    });
  }else{
    const inp=zona.querySelector('.tec');
    zona.querySelector('[data-pista]').onclick=function(){
      usado=true; ayudas++; di('','<b>Pista.</b> '+p.pista);};
    zona.querySelector('[data-modelo]').onclick=function(){
      usado=true; ayudas++;
      di('','<b>Zo kan het:</b><span class="mod">'+p.modelo+'</span>');};
    function enviar(){
      const t=inp.value.trim();
      if(!t) return;
      const notas=corrige(t);
      if(casa(t,p.acepta)){
        if(notas.length){
          avisos.push(notas[0].nl.replace(/<[^>]+>/g,''));
          di('ok','<b>Begrepen!</b> Eén ding nog: '+notas[0].nl+
             '<span class="mod">'+notas[0].bien+'</span>');
        }else{
          // bewust géén «goed!»: de corrector kent niet alles
          di('ok','<b>Begrepen.</b> Ik zie hier geen fouten die ik ken.');
        }
        if(!usado) solos++;
        inp.disabled=true;
        setTimeout(function(){avanza(t);},notas.length?1500:700);
      }else{
        usado=true;
        if(notas.length){
          avisos.push(notas[0].nl.replace(/<[^>]+>/g,''));
          di('mal','<b>Nog niet.</b> '+notas[0].nl+
             '<span class="mod">'+notas[0].bien+'</span>');
        }else{
          di('mal','<b>Dat verstaat de mesero niet.</b> '+p.pista);
        }
      }
    }
    zona.querySelector('[data-env]').onclick=enviar;
    inp.addEventListener('keydown',function(e){if(e.key==='Enter')enviar();});
    inp.focus();
  }
}

raiz.querySelectorAll('.modo button').forEach(function(b){
  b.onclick=function(){
    modo=b.dataset.modo;
    raiz.querySelectorAll('.modo button').forEach(function(x){
      x.classList.toggle('on',x===b);});
    paso=0;ayudas=0;solos=0;avisos=[];esc.innerHTML='';pinta();muestra();
  };
});
pinta(); muestra();
})();
"""


def componente(curso, unidad, id_base=None):
    """Het component als (html, css, js) — klaar om in een hub-paneel te zetten."""
    r = RD.rol(curso, unidad)
    if not r:
        return None
    ident = id_base or ("rol_%s_u%d" % (curso.replace("+", "plus").lower(), unidad))

    datos = {
        "avatar": r["otro_avatar"],
        "final": r["final"], "final_nl": r["final_nl"],
        "pasos": [{"di": p["di"], "nl": p["nl"], "meta": p["meta"],
                   "opciones": [[t, ok, w or ""] for t, ok, w in p["opciones"]],
                   "hueco": p["hueco"],
                   "acepta": p["acepta"], "pista": p["pista"],
                   "modelo": p["modelo"]} for p in r["pasos"]],
    }
    html_out = """
<div class="card rol" id="%(id)s">
  <div style="display:flex;justify-content:space-between;align-items:baseline;
              flex-wrap:wrap;gap:8px">
    <h3 style="margin:0;font-family:var(--disp)">%(tit)s</h3>
    <span class="gloss" style="font-size:13px">%(lugar)s</span>
  </div>
  <p class="lead" style="margin:6px 0 12px"><b>%(tu)s</b> tegenover <b>%(otro)s</b>.
    %(mision)s <span class="gloss">%(mision_es)s</span></p>
  <div class="modo">
    <button data-modo="completar" class="on">Completar · invullen</button>
    <button data-modo="elegir">Elegir · kiezen</button>
    <button data-modo="escribir">Escribir · zelf typen</button>
  </div>
  <div class="barra"></div>
  <div class="esc" aria-live="polite"></div>
  <div class="zona" style="margin-top:12px"></div>
  <p class="gloss" style="font-size:12.5px;margin:10px 0 0">Deze partner werkt
    zonder internet en kent alleen de fouten die erin zitten. Twijfel je over
    iets wat hij níet aanstipt? Vraag het aan je leerkracht.</p>
</div>"""  % {"id": ident, "tit": esc(r["titulo"]), "lugar": esc(r["lugar"]),
              "tu": esc(r["tu"]), "otro": esc(r["otro"]),
              "mision": esc(r["mision"]), "mision_es": esc(r["mision_es"])}

    js = JS % {"datos": json.dumps(datos, ensure_ascii=False),
               "reglas": json.dumps(CD.reglas_para(curso, unidad), ensure_ascii=False),
               "id": ident}
    return html_out, CSS, js


def suelto(curso, unidad):
    """Het component als losstaande pagina — voor de C4-hubs, die hun
    tabbladen als aparte bestanden inladen, en om los te bekijken."""
    hecho = componente(curso, unidad)
    if not hecho:
        return None
    cuerpo, css, js = hecho
    # los bekijkbaar, met een minimale schil zodat de klassen van de hub bestaan
    COL = {"C4": ("#D64550", "#A8323B", "#FBEAEC"),
           "C5": ("#1E9E74", "#157355", "#E4F4EE"),
           "C6+": ("#7C56A9", "#5B3E83", "#EEE8F5")}[curso]
    demo = """<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s U%d · rollenspel</title><style>
:root{--g:%s;--gd:%s;--gt:%s;--ink:#20242E;--mut:#6A6E78;
      --line:#E4E3DE;--card:#fff;--crema:#F3EEE4;--disp:system-ui,sans-serif}
body{font-family:system-ui,sans-serif;background:#FCFBF8;color:var(--ink);
     margin:0;padding:24px;line-height:1.55}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;
      padding:18px 20px;margin:14px auto;max-width:720px}
.lead{color:var(--mut);margin:0 0 14px}.gloss{color:var(--mut);font-style:italic}
.pill{display:inline-block;background:var(--gt);color:var(--gd);border-radius:20px;
      padding:3px 10px;font-size:12px;font-weight:600}
.btn{border:none;background:var(--g);color:#fff;font-weight:700;border-radius:10px;
     padding:9px 16px;cursor:pointer;font-size:14px}
.btn.sec{background:var(--crema);color:var(--ink)}.btn.small{padding:6px 11px;font-size:13px}
%s</style></head><body>%s<script>%s</script></body></html>""" % (
        curso, unidad, COL[0], COL[1], COL[2], css, cuerpo, js)
    ruta = os.path.join(AQUI, "componentes",
                        "%s_U%d_rol.html" % (curso.replace("+", "plus"), unidad))
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    open(ruta, "w", encoding="utf-8").write(demo)
    return ruta


def main():
    curso = sys.argv[1] if len(sys.argv) > 1 else "C5"
    unidad = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    ruta = suelto(curso, unidad)
    if not ruta:
        sys.exit("geen rollenspel voor %s U%d" % (curso, unidad))
    r = RD.rol(curso, unidad)
    print("%s geschreven: %d beurten · %d corrector-regels · %.0f kB"
          % (os.path.basename(ruta), len(r["pasos"]),
             len(CD.reglas_para(curso, unidad)),
             os.path.getsize(ruta) / 1024))


if __name__ == "__main__":
    main()
