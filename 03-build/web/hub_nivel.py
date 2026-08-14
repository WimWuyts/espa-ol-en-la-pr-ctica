#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Drie sporen op één digitale pagina: «Con ayuda · Normal · Reto».

WAAROM
De cursus heeft één moeilijkheidsspoor. De steunladder uit `apoyo.py` bestaat
wel (modelo → banco → marco → primera letra → sin ayuda), maar de auteur kiest
per oefening één trede en daar blijft het bij. In een klas met zij-instromers
naast leerlingen die het vierde jaar gedaan hebben, is dat voor de ene te snel
en voor de andere te traag.

Dit zet er een schakelaar bij, boven aan de pagina, die drie dingen tegelijk
verzet. Niet als nieuwe inhoud — er komt geen letter oefening bij — maar als
een andere hoeveelheid steun op wat er al staat:

    Con ayuda   de letterpista staat open · accenten mogen wegvallen ·
                het rollenspel start bij «Elegir» · woordkaarten ES → NL
    Normal      zoals de auteur het schreef
    Reto        geen pista · accenten tellen mee · het rollenspel start bij
                «Escribir» · woordkaarten NL → ES

DE KEUZE ACHTER DE KEUZE
Het had ook per oefening gekund, met een knopje naast elke opgave. Dat is
zeventien generatoren aanpassen en honderd keuzes per unit maken, en het maakt
van elke oefening een onderhandeling. Eén schakelaar boven aan de pagina is
één beslissing, geldt meteen voor alle ~100 oefeningen van de unit, en blijft
staan (localStorage) zodat een leerling hem één keer zet.

WAT ER BEWUST NIET IN ZIT
De oplossingsknop. «Ver solución» komt pas na twee pogingen, in alle drie de
sporen — ophalen vóór opnieuw tonen (CLAUDE.md §14) is geen steunniveau maar
de didactiek zelf, en die staat niet ter keuze.

Als nabewerking en niet in de generatoren, om dezelfde reden als
`hub_post_iconos.py`: één plek in plaats van eenendertig.

    python3 hub_nivel.py          # alle hubs
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import enlaces as EN          # noqa: E402

MARCA = "<!-- hub_nivel.py -->"

CONTROL = (MARCA + '<div class="nivelsel" role="group" aria-label="Nivel de ayuda">'
           '<span class="nivellab">Nivel</span>'
           '<button type="button" data-nivel="ayuda">Con ayuda</button>'
           '<button type="button" data-nivel="normal" class="on">Normal</button>'
           '<button type="button" data-nivel="reto">Reto</button>'
           '</div>')

CSS = """
/* ── drie sporen · hub_nivel.py ─────────────────────────────────────────── */
.nivelsel{display:flex;align-items:center;gap:4px;margin-left:auto}
.nivellab{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
          color:var(--mut);margin-right:4px}
.nivelsel button{font:inherit;font-size:12px;font-weight:700;border:1.5px solid var(--line);
                 background:var(--card);color:inherit;border-radius:999px;padding:4px 11px;
                 cursor:pointer;white-space:nowrap}
.nivelsel button:hover{border-color:var(--g)}
.nivelsel button.on{background:var(--g);color:#fff;border-color:var(--g)}
.nivelsel button:focus-visible{outline:2px solid var(--g);outline-offset:2px}
@media (max-width:720px){.nivellab{display:none}.nivelsel button{padding:4px 8px}}

/* Con ayuda: de letterpista staat open in plaats van achter een knop. De knop
   blijft bestaan (hij sluit de pista weer), maar de hint is er meteen. */
body.nivel-ayuda .typista{background:var(--gt);border-color:var(--g);color:var(--gd)}
/* Reto: geen pista. Hem verbergen is eerlijker dan hem laten staan en niets
   laten doen — een knop die niets doet leest als een fout. */
body.nivel-reto .typista{display:none}
.nivelnota{font-size:12px;color:var(--mut);margin:6px 0 0}
"""

JS = r"""
/* ── drie sporen · hub_nivel.py ─────────────────────────────────────────── */
var NIVEL='normal';
try{NIVEL=localStorage.getItem('sjb_nivel')||'normal';}catch(e){}

/* De accentregel hangt normaal aan de oefening (`accents:'strict'|'soft'`), en
   die staat vast op het moment dat de oefening gebouwd wordt. Om hem later nog
   te kunnen verzetten leest de vergelijker het spoor: «con ayuda» vergeeft een
   ontbrekende tilde altijd, «reto» nooit, «normal» laat de oefening beslissen.
   Zonder deze omweg zou de schakelaar de hele pagina moeten herbouwen. */
if(typeof tyOk==='function'){
  var _tyOk=tyOk;
  tyOk=function(val,it,mode){
    if(NIVEL==='ayuda')mode='soft';
    else if(NIVEL==='reto')mode='strict';
    return _tyOk(val,it,mode);};
}

function nivelPistas(){
  /* Con ayuda: toon elke pista meteen. Reto: haal getoonde pista's weg. */
  document.querySelectorAll('.tyq').forEach(function(r){
    var b=r.querySelector('.typista'),w=r.querySelector('.exwhy');
    if(!b||!w)return;
    if(w.classList.contains('g')||w.classList.contains('b'))return;   // al beoordeeld
    if(NIVEL==='ayuda'){b.click();}
    else if(NIVEL==='reto'&&w.classList.contains('n')){w.className='exwhy';w.innerHTML='';}
  });
}

function nivelRol(){
  var quiere=NIVEL==='ayuda'?'elegir':(NIVEL==='reto'?'escribir':null);
  if(!quiere)return;
  document.querySelectorAll('.rol .modo button[data-modo="'+quiere+'"]').forEach(function(b){
    if(!b.classList.contains('on'))b.click();});
}

function nivelFichas(){
  var d=document.getElementById('fcdir');
  if(!d)return;
  var quiere=NIVEL==='ayuda'?'es':(NIVEL==='reto'?'nl':null);
  if(!quiere||d.value===quiere)return;
  d.value=quiere;
  if(typeof renderFC==='function')renderFC();
}

function aplicaNivel(n){
  NIVEL=n;
  try{localStorage.setItem('sjb_nivel',n);}catch(e){}
  document.body.classList.remove('nivel-ayuda','nivel-normal','nivel-reto');
  document.body.classList.add('nivel-'+n);
  document.querySelectorAll('.nivelsel button').forEach(function(b){
    var on=b.getAttribute('data-nivel')===n;
    b.classList.toggle('on',on);
    b.setAttribute('aria-pressed',on?'true':'false');});
  nivelPistas();nivelRol();nivelFichas();
}

addEventListener('load',function(){
  document.querySelectorAll('.nivelsel button').forEach(function(b){
    b.onclick=function(){aplicaNivel(b.getAttribute('data-nivel'));};});
  /* de componenten bouwen zichzelf op `load`; even wachten tot ze er staan */
  setTimeout(function(){aplicaNivel(NIVEL);},450);
});
"""


def paginas():
    """De gebouwde hub-pagina's van C5 en C6+.

    C4 blijft er buiten, en dat is geen vergetelheid. Die pagina's zetten hun
    oefeningen in `srcdoc`-iframes en gebruiken de gedeelde oefenmotor niet: van
    de vier hendels hierboven zou alleen het rollenspel meebewegen. Een knop die
    voor een kwart werkt is slechter dan geen knop. Wil C4 hem ook, dan moet de
    schakelaar eerst dóór de iframes heen kunnen — dat is een eigen klus.
    """
    for curso, _u, _impreso, hub in EN.unidades():
        if curso != "C4" and os.path.exists(hub):
            yield hub


def procesar(ruta):
    doc = open(ruta, encoding="utf-8").read()
    if MARCA in doc:
        return False
    # 1 · de schakelaar naast de themaknop in de kopbalk
    m = re.search(r'<button class="themebtn"', doc)
    if not m:
        return False
    doc = doc[:m.start()] + CONTROL + doc[m.start():]
    # 2 · stijl als laatste in de <style>, zodat ze het laatste woord heeft
    i = doc.rfind("</style>")
    if i < 0:
        return False
    doc = doc[:i] + CSS + doc[i:]
    # 3 · gedrag als laatste in de laatste <script>, ná de componenten
    j = doc.rfind("</script>")
    if j < 0:
        return False
    doc = doc[:j] + JS + doc[j:]
    open(ruta, "w", encoding="utf-8").write(doc)
    return True


# ── en het boek moet het weten ─────────────────────────────────────────────
# Een schakelaar die niemand vindt, bestaat niet. De gedrukte unit opent met een
# routebriefje onder de ruta-strook; daar komt er één regel bij die zegt dat de
# digitale pagina drie sporen heeft. Eén keer per unit, in de opener — niet bij
# elke oefening, want dan is het ruis.
MARCA_NOTA = "<!-- hub_nivel.py · nota -->"

NOTA = (MARCA_NOTA + '<div class="route-note" style="margin-top:2mm">'
        '<b>Tres niveles en la página digital.</b> Arriba de la página eliges '
        '<b>Con ayuda</b>, <b>Normal</b> o <b>Reto</b>: cambian la pista, los '
        'acentos, el juego de rol y las fichas de vocabulario. '
        '<span class="gloss">Boven aan de digitale pagina kies je Con ayuda, '
        'Normal of Reto — dat verzet de pista, de accenten, het rollenspel en de '
        'woordkaarten. Kies wat jij vandaag nodig hebt; je keuze blijft staan.'
        '</span></div>')


def nota_impresa(ruta):
    """Zet de regel over de drie sporen onder het routebriefje van de opener."""
    doc = open(ruta, encoding="utf-8").read()
    if MARCA_NOTA in doc:
        return False
    i = doc.find('class="rutastrip"')
    if i >= 0:
        j = doc.find('<div class="route-note"', i)
        k = doc.find("</div>", j) if j >= 0 else -1
        if k >= 0:
            k += len("</div>")
            open(ruta, "w", encoding="utf-8").write(doc[:k] + NOTA + doc[k:])
            return True
    # C5 U0 is met de hand gebouwd en heeft geen ruta-strook in de opener; daar
    # gaat de regel vlak vóór de eerste genummerde sectie staan, wat op dezelfde
    # plaats uitkomt: onderaan de openingsbladzijde.
    k = doc.find('<div class="parada sec"')
    if k < 0:
        return False
    open(ruta, "w", encoding="utf-8").write(doc[:k] + NOTA + doc[k:])
    return True


def impresos():
    for curso, _u, impreso, _hub in EN.unidades():
        if curso != "C4" and os.path.exists(impreso):
            yield impreso


def main():
    hechas = 0
    for ruta in paginas():
        if procesar(ruta):
            hechas += 1
    notas = sum(1 for ruta in impresos() if nota_impresa(ruta))
    print("%d digitale pagina's kregen de niveauschakelaar (con ayuda · normal · reto), "
          "%d gedrukte units de verwijzing ernaar" % (hechas, notas))


if __name__ == "__main__":
    main()
