#!/usr/bin/env python3
"""De «Práctica»-tab voor U11–U14: zeven zelfcorrigerende oefeningen.

De oefeningen worden áfgeleid uit wat de unit al heeft — de clusters uit
`kit_data.py` en de scène uit `escena_data.py`. Dat is geen luiheid maar de
enige manier om te garanderen dat er niets geoefend wordt wat niet aangeboden
is, en dat er niets aangeboden wordt wat niet geoefend wordt. Bij vier
handgeschreven generatoren loopt dat binnen één correctieronde uit elkaar.

DE LADDER (CLAUDE.md §14: herkennen → onderscheiden → ophalen → gestuurd →
vrij). Elke oefening staat op één trede en zegt dat ook:

  1 Tarjetas      herkennen      · woord zien, betekenis oproepen
  2 ¿Qué oyes?    herkennen      · klank → schriftbeeld
  3 Clasifica     onderscheiden  · in welk veld hoort dit?
  4 Empareja      ophalen        · ES ↔ NL zonder de kaartjes
  5 Completa      gestuurd       · het gat in een zin uit de scène
  6 Ordena        gestuurd       · de woordvolgorde herstellen
  7 Grábate       vrij           · de tarea, opgenomen en teruggeluisterd

De opname-oefening is verplicht (§14bis) en werkt met MediaRecorder: opnemen,
terugluisteren, opnieuw. Offline, zonder server; er wordt niets verstuurd.

    C4_UNIT=11 python3 gen_c4_practica.py
"""
import base64
import html
import json
import os
import random
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)

import escena_data as ED          # noqa: E402
import kit_data as KD             # noqa: E402


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


# ── de gegevens waaruit de oefeningen groeien ───────────────────────────────
def datos(unit):
    """Alles wat de oefeningen nodig hebben, uit de unit zelf gehaald."""
    rnd = random.Random(unit)          # vast: dezelfde bouw geeft dezelfde volgorde
    clusters = KD.CLUSTERS[unit]
    pares = [(es, nl) for _n, _s, _i, items in clusters for es, nl in items]

    # zinnen uit de scène, lang genoeg om iets uit weg te laten
    lineas = [es for _sp, es in ED.guion(unit) if 4 <= len(es.split()) <= 11]
    rnd.shuffle(lineas)

    # de gaten: een chunk van de unit die écht in die zin staat
    chunks = sorted(ED.ESCENAS[unit]["chunks"], key=len, reverse=True)
    huecos = []
    for l in lineas:
        for c in chunks:
            m = re.search(re.escape(c), l, re.I)
            if m and len(huecos) < 8:
                huecos.append({"frase": l[:m.start()] + "___" + l[m.end():],
                               "sol": l[m.start():m.end()], "completa": l})
                break
    return {
        "clusters": [{"nombre": n, "items": [e for e, _ in items]}
                     for n, _s, _i, items in clusters],
        "pares": [{"es": e, "nl": n} for e, n in pares],
        "huecos": huecos,
        "ordena": [{"frase": l} for l in lineas[:8]],
        "tarea": {"titulo": KD.TAREA[unit][0], "pasos": KD.TAREA[unit][3]},
    }


CSS = FONTS + """
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;
      --crema:#F3EEE4;--line:#E7E1DF;--card:#fff;--ok:#2F9A4A;--no:#DC2626;
      --disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#181513;--crema:#241C1B;--gt:#3A1E20;
                  --line:#3a302e;--card:#211a19}
*{box-sizing:border-box}
body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
.top{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;padding:20px 22px}
.top h1{font-family:var(--disp);font-weight:800;margin:0;font-size:24px}
.top p{margin:4px 0 0;opacity:.95}
main{max-width:960px;margin:0 auto;padding:18px 18px 44px}
.subh{font-family:var(--disp);color:var(--gd);font-size:20px;margin:26px 0 8px;
      display:flex;align-items:center;gap:9px}
.pill{background:var(--gt);color:var(--gd);border-radius:20px;padding:2px 11px;font-size:12px;font-weight:700}
.game{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 18px;margin:12px 0}
.game h3{font-family:var(--disp);margin:0 0 2px;font-size:17px}
.game .d{color:var(--mut);font-size:13.5px;margin:0 0 10px}
.score{float:right;font-size:13px;color:var(--mut)}
.score b{color:var(--ok)}
.opts{display:flex;flex-wrap:wrap;gap:7px}
.opt{border:1.5px solid var(--line);background:var(--card);border-radius:11px;padding:7px 13px;
     cursor:pointer;font-family:var(--body);font-size:14.5px;color:var(--ink)}
.opt:hover{border-color:var(--g)}
.opt.ok{border-color:var(--ok);background:#EAF7EE;color:#166534}
.opt.no{border-color:var(--no);background:#FEECEC;color:#991B1B}
.q{padding:9px 0;border-bottom:1px solid var(--line)}
.q:last-child{border-bottom:none}
.qz{font-weight:600;margin-bottom:6px}
.fb{font-size:13.5px;margin-top:5px;min-height:19px}
.fb.g{color:var(--ok)}.fb.b{color:var(--no)}
input.ty{border:1.5px solid var(--line);border-radius:10px;padding:7px 11px;font-family:var(--body);
         font-size:14.5px;background:var(--card);color:var(--ink);min-width:220px}
input.ty.good{border-color:var(--ok)}input.ty.bad{border-color:var(--no)}
.btn{border:1.5px solid var(--line);background:var(--card);color:var(--ink);font-weight:700;
     border-radius:10px;padding:7px 13px;cursor:pointer;font-size:13.5px;font-family:var(--disp)}
.btn.on{background:var(--g);color:#fff;border-color:var(--g)}
.btn:disabled{opacity:.45;cursor:default}
.flip{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:9px}
.card{background:var(--crema);border-radius:12px;padding:14px 12px;text-align:center;cursor:pointer;
      min-height:74px;display:flex;align-items:center;justify-content:center;font-weight:600}
.card.rev{background:var(--gt);color:var(--gd)}
.drop{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:9px;margin-top:9px}
.bin{border:1.5px dashed var(--line);border-radius:12px;padding:9px;min-height:78px}
.bin h4{margin:0 0 6px;font-family:var(--disp);font-size:13.5px;color:var(--gd)}
.bin.over{border-color:var(--g);background:var(--gt)}
.tok{display:inline-block;background:var(--crema);border-radius:9px;padding:5px 10px;margin:3px;
     cursor:grab;font-size:14px}
.tok.ok{background:#EAF7EE;color:#166534}
.rec{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:9px 0}
.rec audio{height:34px}
.foot{color:var(--mut);font-size:12px;text-align:center;margin:26px 0 0}
"""

JS = r"""
var D=__DATOS__;
function speak(t){if(!('speechSynthesis'in window))return;
 var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.85;
 var v=speechSynthesis.getVoices().find(function(x){return /^es/i.test(x.lang)});
 if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}
if('speechSynthesis'in window)speechSynthesis.getVoices();
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'')
 .replace(/[^a-z0-9ñ ]/g,'').replace(/\s+/g,' ').trim();}
function baraja(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));
 var t=a[i];a[i]=a[j];a[j]=t;}return a;}
function marco(id,tit,desc,n){var h=document.getElementById(id);
 h.innerHTML='<span class="score">Juist: <b>0</b>/'+n+'</span><h3>'+tit+'</h3><p class="d">'+desc+'</p><div class="cuerpo"></div>';
 return {host:h,cuerpo:h.querySelector('.cuerpo'),ok:0,
  punto:function(){this.ok++;h.querySelector('.score b').textContent=this.ok;}};}

/* 1 · tarjetas — woord zien, betekenis oproepen, dan omdraaien */
(function(){var m=marco('g_cards','① Tarjetas · ¿qué significa?',
 'Zeg de betekenis hardop vóór je omdraait. Klik om te draaien, klik 🔊 om te horen.',D.pares.length);
 var g=document.createElement('div');g.className='flip';
 baraja(D.pares).forEach(function(p){var c=document.createElement('div');c.className='card';
  c.textContent=p.es;var vuelta=false;
  c.onclick=function(){vuelta=!vuelta;c.textContent=vuelta?p.nl:p.es;c.classList.toggle('rev',vuelta);
   if(!vuelta)speak(p.es);else if(!c.dataset.contado){c.dataset.contado='1';m.punto();}};
  g.appendChild(c);});
 m.cuerpo.appendChild(g);})();

/* 2 · ¿qué oyes? — klank naar schriftbeeld */
(function(){var items=baraja(D.pares).slice(0,8);
 var m=marco('g_escucha','② ¿Qué oyes? · luister en kies',
  'Klik ▶, luister en kies wat je hoort. Twijfel je? Luister nog eens.',items.length);
 items.forEach(function(it){
  var otras=baraja(D.pares.filter(function(p){return p.es!==it.es;})).slice(0,2);
  var ops=baraja([it].concat(otras));
  var q=document.createElement('div');q.className='q';
  q.innerHTML='<div class="qz"><button class="btn">▶ Escuchar</button></div><div class="opts"></div><div class="fb"></div>';
  q.querySelector('.btn').onclick=function(){speak(it.es);};
  var cont=q.querySelector('.opts'),fb=q.querySelector('.fb'),cerrado=false;
  ops.forEach(function(o){var b=document.createElement('button');b.className='opt';b.textContent=o.es;
   b.onclick=function(){if(cerrado)return;cerrado=true;var bien=o.es===it.es;
    cont.querySelectorAll('.opt').forEach(function(x){if(x.textContent===it.es)x.classList.add('ok');});
    if(!bien)b.classList.add('no');
    fb.className='fb '+(bien?'g':'b');fb.textContent=bien?'¡Correcto! '+it.nl:'Era: '+it.es+' — '+it.nl;
    if(bien)m.punto();};
   cont.appendChild(b);});
  m.cuerpo.appendChild(q);});})();

/* 3 · clasifica — in welk veld hoort dit woord? */
(function(){var m=marco('g_clasifica','③ Clasifica · ¿a qué grupo pertenece?',
 'Sleep elk woord naar het juiste veld. Fout? Het springt terug.',
 D.clusters.reduce(function(a,c){return a+Math.min(c.items.length,3);},0));
 var pool=document.createElement('div');pool.style.margin='6px 0';
 var bins=document.createElement('div');bins.className='drop';
 var todos=[];
 D.clusters.forEach(function(c,i){
  var b=document.createElement('div');b.className='bin';b.dataset.i=i;
  b.innerHTML='<h4>'+c.nombre+'</h4>';
  b.ondragover=function(e){e.preventDefault();b.classList.add('over');};
  b.ondragleave=function(){b.classList.remove('over');};
  b.ondrop=function(e){e.preventDefault();b.classList.remove('over');
   var id=e.dataTransfer.getData('text');var t=document.getElementById(id);
   if(!t)return;
   if(t.dataset.i===b.dataset.i){t.classList.add('ok');t.draggable=false;b.appendChild(t);m.punto();}};
  bins.appendChild(b);
  baraja(c.items).slice(0,3).forEach(function(w,k){
   var t=document.createElement('span');t.className='tok';t.textContent=w;
   t.id='t'+i+'_'+k;t.draggable=true;t.dataset.i=i;
   t.ondragstart=function(e){e.dataTransfer.setData('text',t.id);};
   t.onclick=function(){speak(w);};
   todos.push(t);});});
 baraja(todos).forEach(function(t){pool.appendChild(t);});
 m.cuerpo.appendChild(pool);m.cuerpo.appendChild(bins);})();

/* 4 · empareja — ES naar NL, zonder de kaartjes erbij */
(function(){var items=baraja(D.pares).slice(0,8);
 var m=marco('g_match','④ Empareja · español → nederlands',
  'Kies de juiste vertaling. Nu zonder kaartjes: uit je hoofd.',items.length);
 items.forEach(function(it){
  var otras=baraja(D.pares.filter(function(p){return p.nl!==it.nl;})).slice(0,2);
  var ops=baraja([it].concat(otras));
  var q=document.createElement('div');q.className='q';
  q.innerHTML='<div class="qz">'+it.es+'</div><div class="opts"></div><div class="fb"></div>';
  var cont=q.querySelector('.opts'),fb=q.querySelector('.fb'),cerrado=false;
  ops.forEach(function(o){var b=document.createElement('button');b.className='opt';b.textContent=o.nl;
   b.onclick=function(){if(cerrado)return;cerrado=true;var bien=o.nl===it.nl;
    cont.querySelectorAll('.opt').forEach(function(x){if(x.textContent===it.nl)x.classList.add('ok');});
    if(!bien)b.classList.add('no');
    fb.className='fb '+(bien?'g':'b');fb.textContent=bien?'¡Bien!':'Era: '+it.nl;
    if(bien)m.punto();};
   cont.appendChild(b);});
  m.cuerpo.appendChild(q);});})();

/* 5 · completa — het gat in een zin uit de scène */
(function(){var m=marco('g_completa','⑤ Completa · rellena el hueco',
 'Vul de ontbrekende chunk in. Accenten mogen wegblijven.',D.huecos.length);
 D.huecos.forEach(function(h){
  var q=document.createElement('div');q.className='q';
  q.innerHTML='<div class="qz">'+h.frase+'</div>'+
   '<input class="ty" type="text" autocomplete="off" aria-label="vul aan">'+
   ' <button class="btn">Comprobar</button> <button class="btn">🔊</button><div class="fb"></div>';
  var inp=q.querySelector('.ty'),bs=q.querySelectorAll('.btn'),fb=q.querySelector('.fb');
  bs[1].onclick=function(){speak(h.completa);};
  function comprueba(){if(inp.disabled)return;
   var bien=norm(inp.value)===norm(h.sol);
   if(bien){inp.disabled=true;bs[0].disabled=true;inp.classList.add('good');
    fb.className='fb g';fb.textContent='¡Correcto! '+h.completa;m.punto();speak(h.completa);}
   else{inp.classList.add('bad');fb.className='fb b';fb.textContent='Todavía no — escucha la frase.';}}
  bs[0].onclick=comprueba;
  inp.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();comprueba();}});
  m.cuerpo.appendChild(q);});})();

/* 6 · ordena — de woordvolgorde herstellen */
(function(){var m=marco('g_ordena','⑥ Ordena · pon las palabras en orden',
 'Klik de woorden in de juiste volgorde. Nog eens klikken haalt er een weg.',D.ordena.length);
 D.ordena.forEach(function(o){
  var pal=o.frase.replace(/[¿¡.,!?]/g,'').split(/\s+/);
  var q=document.createElement('div');q.className='q';
  q.innerHTML='<div class="opts"></div><div class="qz" style="margin:7px 0"></div>'+
   '<button class="btn">Comprobar</button><div class="fb"></div>';
  var cont=q.querySelector('.opts'),linea=q.querySelector('.qz'),fb=q.querySelector('.fb');
  var puestas=[];
  baraja(pal).forEach(function(w){var b=document.createElement('button');b.className='opt';b.textContent=w;
   b.onclick=function(){if(b.classList.contains('ok')){b.classList.remove('ok');
     puestas.splice(puestas.indexOf(w),1);}else{b.classList.add('ok');puestas.push(w);}
    linea.textContent=puestas.join(' ');};
   cont.appendChild(b);});
  q.querySelector('.btn').onclick=function(){
   var bien=norm(puestas.join(' '))===norm(pal.join(' '));
   fb.className='fb '+(bien?'g':'b');
   fb.textContent=bien?'¡Correcto!':'Nog niet — luister eens: '+o.frase;
   if(bien){m.punto();speak(o.frase);this.disabled=true;}else{speak(o.frase);}};
  m.cuerpo.appendChild(q);});})();

/* 7 · grábate — de eindtaak, opgenomen en teruggeluisterd */
(function(){var h=document.getElementById('g_grabate');
 var pasos=D.tarea.pasos.map(function(p){return '<li>'+p+'</li>';}).join('');
 h.innerHTML='<h3>⑦ Grábate · '+D.tarea.titulo+'</h3>'+
  '<p class="d">Doe de eindtaak hardop en neem jezelf op. Luister terug: versta jíj jezelf? '+
  'Neem daarna nog eens op — de tweede keer is altijd beter.</p><ol>'+pasos+'</ol>'+
  '<div class="rec"><button class="btn" id="rgo">⏺ Grabar</button>'+
  '<button class="btn" id="rst" disabled>⏹ Parar</button><audio id="rau" controls></audio></div>'+
  '<p class="d" id="rmsg">De opname blijft op je toestel — er wordt niets verstuurd.</p>';
 var go=h.querySelector('#rgo'),st=h.querySelector('#rst'),au=h.querySelector('#rau'),
     msg=h.querySelector('#rmsg'),rec=null,trozos=[];
 go.onclick=function(){
  if(!navigator.mediaDevices||!window.MediaRecorder){
   msg.textContent='Dit toestel kan niet opnemen in de browser. Neem op met je telefoon en luister zo terug.';return;}
  navigator.mediaDevices.getUserMedia({audio:true}).then(function(s){
   trozos=[];rec=new MediaRecorder(s);
   rec.ondataavailable=function(e){trozos.push(e.data);};
   rec.onstop=function(){au.src=URL.createObjectURL(new Blob(trozos,{type:'audio/webm'}));
    s.getTracks().forEach(function(t){t.stop();});
    msg.textContent='Klaar. Luister terug en neem gerust nog eens op.';};
   rec.start();go.disabled=true;st.disabled=false;go.classList.add('on');
   msg.textContent='Aan het opnemen…';})
  .catch(function(){msg.textContent='Geen toegang tot de microfoon. Zet ze aan in je browser.';});};
 st.onclick=function(){if(rec)rec.stop();go.disabled=false;st.disabled=true;go.classList.remove('on');};})();
"""


def construir(unit):
    d = datos(unit)
    tema = ED.ESCENAS[unit]["tema"]
    js = JS.replace("__DATOS__", json.dumps(d, ensure_ascii=False))
    return """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>C4 · Unidad %(u)d · Práctica</title><style>%(css)s</style></head><body>
<div class="top"><h1>Unidad %(u)d · %(tema)s — Práctica</h1>
<p>Van <b>herkennen</b> naar <b>zelf zeggen</b>. Alles verbetert zichzelf; klik 🔊 om te horen.</p></div>
<main>
 <h2 class="subh">① Reconocer <span class="pill">je ziet het en herkent het</span></h2>
 <div class="game" id="g_cards"></div>
 <div class="game" id="g_escucha"></div>
 <div class="game" id="g_clasifica"></div>
 <h2 class="subh">② Practicar <span class="pill">met steun</span></h2>
 <div class="game" id="g_match"></div>
 <div class="game" id="g_completa"></div>
 <div class="game" id="g_ordena"></div>
 <h2 class="subh">③ Producir <span class="pill">zonder steun</span></h2>
 <div class="game" id="g_grabate"></div>
 <div class="foot">C4 · «Bienvenidos al español» · Unidad %(u)d · %(tema)s</div>
</main>
<script>%(js)s</script></body></html>""" % {
        "u": unit, "css": CSS, "js": js, "tema": esc(tema)}


def main():
    unit = int(os.environ.get("C4_UNIT", "11"))
    salida = os.environ.get("C4_PRACTICA_OUT", "C4_U%d_practica.html" % unit)
    if unit not in KD.CLUSTERS:
        sys.exit("geen gegevens voor unidad %d" % unit)
    doc = construir(unit)
    ruta = os.path.join(AQUI, "componentes", salida)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    open(ruta, "w", encoding="utf-8").write(doc)
    d = datos(unit)
    print("%s geschreven: %d bytes · U%d · %d kaartjes · %d gaten · %d zinnen"
          % (salida, len(doc), unit, len(d["pares"]), len(d["huecos"]), len(d["ordena"])))


if __name__ == "__main__":
    main()
