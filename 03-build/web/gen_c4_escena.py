#!/usr/bin/env python3
"""De «¡Escucha!»-tab voor de C4-units zónder sitcom-aflevering (U11–U14).

VERSCHIL MET `gen_c4uN_escucha.py`
Die tien bouwen hun tab rond de video: links het beeld, rechts het transcript
dat meeloopt. Hier is er geen video, dus staat op die plaats de opname zelf —
ingesproken met de acht Castiliaanse stemmen — met dezelfde didactiek eromheen:
meelezen, Nederlands aan/uit, een regel aanklikken om ze opnieuw te horen, en
de chunks in het geel.

Eén generator voor vier units, niet vier bijna-kopieën: de scènes staan in
`escena_data.py` en dít bestand is alleen de vorm. Komt er later alsnog een
transcript van een echte aflevering, dan is dat een wijziging in de gegevens.

De opname zit als data-URL in de pagina, net als bij het comprension-blok: de
C4-hub moet standalone werken (§16), en dat kan alleen als het geluid meereist.

    C4_UNIT=11 python3 gen_c4_escena.py
"""
import base64
import html
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)

import escena_data as ED          # noqa: E402


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

# Elke spreker een eigen kleur, zoals in de sitcom-units. De vier vaste
# personages houden hun kleur over U11–U14 heen; de bijrollen delen er een.
COL = {"Ana": "#D64550", "Nico": "#2563EB", "Alba": "#0E9E97", "Iván": "#7C3AED",
       "Dependienta": "#B45309", "Recepcionista": "#B45309"}


def esc(s):
    return html.escape(s, quote=True)


def marca(texto, chunks):
    """Zet de chunks in het geel — de langste eerst, anders knipt «hace frío»
    de langere «¡Qué frío hace!» doormidden."""
    guardado = []

    def coge(m):
        guardado.append(m.group(1))
        return "\x00%d\x00" % (len(guardado) - 1)

    out = texto
    for c in sorted(chunks, key=len, reverse=True):
        out = re.sub("(" + re.escape(c) + ")", coge, out, count=1, flags=re.I)
    out = esc(out)
    return re.sub("\x00(\\d+)\x00",
                  lambda m: '<span class="ch">%s</span>' % esc(guardado[int(m.group(1))]),
                  out)


def linea(sp, es, nl, chunks):
    c = COL.get(sp, "#A8323B")
    return ('<div class="ln" data-es="%s"><span class="who" style="background:%s22;color:%s">%s</span>'
            '<span class="es">%s</span><span class="nl">%s</span>'
            '<button class="spk" title="luister">🔊</button></div>'
            % (esc(es), c, c, esc(sp), marca(es, chunks), esc(nl)))


def escena(titulo, intro, lineas, chunks):
    return ('<div class="scene"><h3>%s</h3><p class="si">%s</p>%s</div>'
            % (esc(titulo), esc(intro),
               "".join(linea(sp, es, nl, chunks) for sp, es, nl in lineas)))


def audio_datos(unit):
    """De opname van deze scène, als data-URL. `.wav` zolang er geen omzetter is."""
    for ext, mime in ((".mp3", "audio/mpeg"), (".wav", "audio/wav")):
        p = os.path.join(AQUI, "audio", "C4_U%d_escena%s" % (unit, ext))
        if os.path.exists(p):
            return b64(p), mime
    return None, None


CSS = FONTS + """
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;
      --crema:#F3EEE4;--line:#E7E1DF;--card:#fff;--disp:'Bricolage Grotesque',sans-serif;
      --body:'Inter',sans-serif}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#181513;--crema:#241C1B;--gt:#3A1E20;
                  --line:#3a302e;--card:#211a19}
*{box-sizing:border-box}
body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
.top{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;padding:20px 22px}
.top h1{font-family:var(--disp);font-weight:800;margin:0;font-size:24px}
.top p{margin:4px 0 0;opacity:.95}
main{max-width:1080px;margin:0 auto;padding:18px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}
@media(max-width:820px){.grid{grid-template-columns:1fr}}
.aud{position:sticky;top:12px;align-self:start}
.audbox{border:1px solid var(--line);border-radius:14px;background:var(--card);padding:16px 18px}
.audbox h2{font-family:var(--disp);color:var(--gd);margin:0 0 4px;font-size:18px}
.audbox p{margin:0 0 12px;color:var(--mut);font-size:13.5px}
audio{width:100%}
.toolbar{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:12px 0}
.btn{border:1.5px solid var(--line);background:var(--card);color:var(--ink);font-weight:700;
     border-radius:10px;padding:8px 13px;cursor:pointer;font-size:13px;font-family:var(--disp)}
.btn.on{background:var(--g);color:#fff;border-color:var(--g)}
.legend{font-size:12px;color:var(--mut)}
.legend .ch{background:#FEF08A;border-radius:4px;padding:1px 5px;color:#20242E}
.pasos{margin:12px 0 0;padding-left:18px;font-size:13.5px;color:var(--mut)}
.pasos li{margin:3px 0}
.scene{margin:0 0 16px}
.scene h3{font-family:var(--disp);color:var(--gd);margin:14px 0 2px;font-size:17px}
.scene .si{color:var(--mut);font-size:13px;margin:0 0 8px}
.ln{display:flex;gap:8px;align-items:baseline;padding:6px 8px;border-radius:10px;flex-wrap:wrap}
.ln:hover{background:var(--gt)}
.who{font-family:var(--disp);font-weight:700;font-size:12px;border-radius:20px;padding:2px 9px;flex:none}
.es{font-size:15.5px;font-weight:500}
.es .ch{background:#FEF08A;border-radius:4px;padding:1px 4px;color:#20242E}
.nl{display:none;color:var(--mut);font-style:italic;font-size:13.5px;width:100%;margin-left:44px}
body.shownl .nl{display:block}
body.hidees .es{filter:blur(4px)}
.spk{border:none;background:transparent;cursor:pointer;font-size:14px;opacity:.5;margin-left:auto}
.foot{color:var(--mut);font-size:12px;text-align:center;margin:24px 0}
"""


def construir(unit):
    e = ED.ESCENAS[unit]
    cuerpo = "".join(escena(t, i, l, e["chunks"]) for t, i, l in e["escenas"])
    datos, mime = audio_datos(unit)
    if datos:
        reproductor = ('<audio id="aud" controls preload="metadata" '
                       'src="data:%s;base64,%s"></audio>' % (mime, datos))
        nota = ""
    else:
        # Geen opname gevonden: dan leest de browserstem voor. Dat staat er
        # eerlijk bij in plaats van een dode knop te tonen.
        reproductor = '<button class="btn" id="leer">▶ Leer de escena</button>'
        nota = ('<p class="legend">De opname staat nog niet klaar; '
                'voorlopig leest de browserstem voor.</p>')

    return """<!doctype html><html lang="es" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>C4 · Unidad %(u)d · Escucha</title><style>%(css)s</style></head><body>
<div class="top"><h1>Unidad %(u)d · %(tit)s — ¡Escucha!</h1>
<p>%(intro)s</p></div>
<main>
 <div class="grid">
  <div class="aud">
    <div class="audbox">
      <h2>%(tit)s</h2>
      <p>%(tema)s</p>
      %(rep)s
      %(nota)s
      <ol class="pasos">
        <li>Luister één keer <b>zonder</b> mee te lezen.</li>
        <li>Luister opnieuw en lees mee.</li>
        <li>Zet het Nederlands aan als je vastzit.</li>
        <li>Klik op een regel om ze apart te horen.</li>
      </ol>
    </div>
    <div class="toolbar">
      <button class="btn" id="tgnl">🇳🇱 Nederlands aan</button>
      <button class="btn" id="tges">👁️ Tekst verbergen</button>
      <span class="legend">💡 <span class="ch">geel</span> = chunk om mee te nemen</span>
    </div>
  </div>
  <div class="tr">%(cuerpo)s</div>
 </div>
 <div class="foot">C4 · «Bienvenidos al español» · Unidad %(u)d · %(tema)s</div>
</main>
<script>
function speak(t){if(!('speechSynthesis'in window))return;
 var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=.9;
 var v=speechSynthesis.getVoices().find(function(x){return /^es/i.test(x.lang)});
 if(v)u.voice=v;speechSynthesis.cancel();speechSynthesis.speak(u);}
document.querySelectorAll('.ln').forEach(function(l){
 var b=l.querySelector('.spk'),es=l.getAttribute('data-es');
 b.onclick=function(e){e.stopPropagation();speak(es);};
 l.addEventListener('click',function(e){if(e.target!==b)speak(es);});});
var nlon=false;document.getElementById('tgnl').onclick=function(){
 nlon=!nlon;document.body.classList.toggle('shownl',nlon);this.classList.toggle('on',nlon);
 this.textContent=nlon?'🇳🇱 Nederlands uit':'🇳🇱 Nederlands aan';};
var esoff=false;document.getElementById('tges').onclick=function(){
 esoff=!esoff;document.body.classList.toggle('hidees',esoff);this.classList.toggle('on',esoff);
 this.textContent=esoff?'👁️ Tekst tonen':'👁️ Tekst verbergen';};
var leer=document.getElementById('leer');
if(leer)leer.onclick=function(){var i=0,ls=[].slice.call(document.querySelectorAll('.ln'));
 (function nx(){if(i>=ls.length)return;var u=new SpeechSynthesisUtterance(ls[i].getAttribute('data-es'));
  u.lang='es-ES';u.rate=.9;u.onend=function(){i++;setTimeout(nx,320);};speechSynthesis.speak(u);})();};
</script></body></html>""" % {
        "u": unit, "css": CSS, "tit": esc(e["titulo"]), "tema": esc(e["tema"]),
        "intro": e["intro"], "rep": reproductor, "nota": nota, "cuerpo": cuerpo}


def main():
    unit = int(os.environ.get("C4_UNIT", "11"))
    salida = os.environ.get("C4_ESCENA_OUT", "C4_U%d_escucha.html" % unit)
    if unit not in ED.ESCENAS:
        sys.exit("geen scène voor unidad %d in escena_data.py" % unit)
    doc = construir(unit)
    ruta = os.path.join(AQUI, "componentes", salida)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    open(ruta, "w", encoding="utf-8").write(doc)
    datos, _ = audio_datos(unit)
    print("%s geschreven: %d bytes · U%d · %s"
          % (salida, len(doc), unit, "met opname" if datos else "browserstem"))


if __name__ == "__main__":
    main()
