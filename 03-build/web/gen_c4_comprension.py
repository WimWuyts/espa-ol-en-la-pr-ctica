#!/usr/bin/env python3
# C4 — HERBRUIKBAAR component «Lee y escucha» (leesvaardigheid + 2e luisterfragment).
# Rendert uit comprension_data.py: een leestekst + begripsladder (globaal→detalle→transfer) en
# een luisterfragment (TTS-play van het script + vragen). None = nette «binnenkort»-plek.
# Env: C4_UNIT=<n>  C4_COMPR_OUT=C4_U<n>_comprension.html  python3 gen_c4_comprension.py
import os, sys, json, base64, html
ROOT="/home/user/espa-ol-en-la-pr-ctica"
sys.path.insert(0, f"{ROOT}/03-build/web")
import comprension_data as CD

def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
def face(f,p,w): return f"@font-face{{font-family:'{f}';src:url(data:font/woff2;base64,{b64(f'{ROOT}/02-huisstijl/fonts/{p}')}) format('woff2');font-weight:{w};font-display:swap}}"
FONTS="".join([face("Bricolage Grotesque","BricolageGrotesque-700.woff2","700"),face("Bricolage Grotesque","BricolageGrotesque-800.woff2","800"),
 face("Inter","Inter-400.woff2","400"),face("Inter","Inter-600.woff2","600"),face("Caveat","Caveat-700.woff2","700")])
def esc(s): return html.escape(s, quote=True)

CSS=FONTS+"""
:root{--g:#D64550;--gd:#A8323B;--gt:#FBEAEC;--ink:#20242E;--mut:#6A6E78;--paper:#FCFBF8;--crema:#F3EEE4;--line:#E7E1DF;--card:#fff;--red:#DC2626;--ok:#2F9A4A;--disp:'Bricolage Grotesque',sans-serif;--body:'Inter',sans-serif;--hand:'Caveat',cursive}
[data-theme=dark]{--ink:#ECEAE3;--mut:#A6A29A;--paper:#181513;--crema:#241C1B;--gt:#3A1E20;--line:#3a302e;--card:#211a19}
*{box-sizing:border-box}body{margin:0;font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.55}
.wrap{max-width:900px;margin:0 auto;padding:20px 20px 44px}
.hero{background:linear-gradient(135deg,var(--g),var(--gd));color:#fff;border-radius:20px;padding:22px 26px;margin-bottom:6px}
.hero h1{font-family:var(--disp);font-weight:800;font-size:27px;margin:0 0 4px}
.hero p{margin:0;max-width:660px;opacity:.96}.hero .nl{font-family:var(--hand);font-size:18px;opacity:.95;margin-top:4px}
h2.sec{font-family:var(--disp);font-weight:700;color:var(--gd);font-size:21px;margin:24px 0 4px;display:flex;gap:8px;align-items:center}
.lead{color:var(--mut);max-width:720px;margin:0 0 10px}
.stn{color:var(--mut);font-style:italic;font-size:.9em;font-family:var(--body)}
.tipo{display:inline-block;background:var(--gt);color:var(--gd);border-radius:20px;padding:3px 11px;font-size:12px;font-weight:700}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin:12px 0}
.ph{border-style:dashed;text-align:center;color:var(--mut)}.ph .nl{font-family:var(--hand);font-size:17px;display:block;margin-top:4px;color:var(--gd)}
/* chat / tekst */
.chat{display:flex;flex-direction:column;gap:8px}
.bub{max-width:80%;padding:9px 13px;border-radius:14px;font-size:15px;position:relative}
.bub .who{display:block;font-size:11px;font-weight:700;color:var(--gd);margin-bottom:2px;font-family:var(--disp)}
.bub.l{align-self:flex-start;background:var(--gt);border-bottom-left-radius:4px}
.bub.r{align-self:flex-end;background:var(--crema);border-bottom-right-radius:4px}
.para{font-size:15px;margin:6px 0}
.toolbar{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0}
.btn{border:1.5px solid var(--line);background:var(--card);color:var(--ink);font-weight:700;border-radius:10px;padding:8px 13px;cursor:pointer;font-size:13px;font-family:var(--disp)}
.btn.on{background:var(--g);color:#fff;border-color:var(--g)}
.btn.play{background:var(--g);color:#fff;border-color:var(--g)}
/* vragen */
.q{margin:10px 0;padding:10px 12px;border:1px solid var(--line);border-radius:12px;background:var(--paper)}
.q .qt{font-weight:600;margin:0 0 6px;font-size:14.5px}
.opts{display:flex;gap:7px;flex-wrap:wrap}
.opt{border:1.5px solid var(--line);background:var(--card);border-radius:10px;padding:6px 12px;cursor:pointer;font-size:14px;font-weight:600}
.opt.ok{background:var(--ok);color:#fff;border-color:var(--ok)}.opt.no{background:#fde8e8;border-color:var(--red);color:var(--red)}
.vf{display:inline-flex;gap:6px}.vfb{border:1.5px solid var(--line);background:var(--card);border-radius:10px;width:34px;height:32px;cursor:pointer;font-weight:800;font-family:var(--disp)}
.vfb.ok{background:var(--ok);color:#fff;border-color:var(--ok)}.vfb.no{background:#fde8e8;border-color:var(--red);color:var(--red)}
.fb{font-size:12.5px;color:var(--gd);font-weight:600;margin-left:8px}
.ficha{border:1px solid var(--line);border-radius:10px;background:var(--crema);padding:8px 12px;font-size:13px;margin:8px 0}
.gloss{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.gloss span{background:var(--gt);color:var(--gd);border-radius:20px;padding:2px 10px;font-size:12px;font-weight:600}
.gloss b{color:var(--ink)}
.transfer{border-left:4px solid var(--g);background:var(--gt);border-radius:0 10px 10px 0;padding:8px 12px;margin-top:10px;font-weight:600}
.foot{color:var(--mut);font-size:12px;text-align:center;margin-top:30px}
"""

def mc_block(qs, idp):
    out=""
    for i,q in enumerate(qs):
        opts="".join(f'<button class="opt" data-c="{1 if j==q["a"] else 0}">{esc(o)}</button>' for j,o in enumerate(q["opts"]))
        out+=f'<div class="q" data-mc><p class="qt">{i+1}. {esc(q["q"])}</p><div class="opts">{opts}</div><span class="fb"></span></div>'
    return out

def vf_block(qs):
    out=""
    for i,q in enumerate(qs):
        cor="V" if q["vf"] else "F"
        out+=(f'<div class="q" data-vf="{cor}"><p class="qt">{i+1}. {esc(q["q"])} '
              f'<span class="vf"><button class="vfb" data-v="V">V</button><button class="vfb" data-v="F">F</button></span>'
              f'<span class="fb"></span></p></div>')
    return out

def gloss_block(gl):
    if not gl: return ""
    return '<div class="gloss">'+"".join(f'<span><b>{esc(e)}</b> · {esc(n)}</span>' for e,n in gl)+'</div>'

def lectura_section(L):
    # tekst: chat-bubbles bij sprekers, anders paragrafen
    speakers=[t[0] for t in L["texto"] if t[0]]
    side={}
    for sp in speakers:
        if sp not in side: side[sp]="l" if len(side)==0 else ("r" if len(side)==1 else side.get(sp,"l"))
    body=""
    for who,line in L["texto"]:
        if who:
            body+=f'<div class="bub {side.get(who,"l")}"><span class="who">{esc(who)}</span>{esc(line)}</div>'
        else:
            body+=f'<p class="para">{esc(line)}</p>'
    return (f'<h2 class="sec">📖 Lee <span class="tipo">{esc(L["tipo"])}</span></h2>'
            f'<p class="lead">{esc(L["contexto_nl"])}</p>'
            f'<div class="card"><div class="toolbar"><button class="btn play" id="readTts">🔊 Escuchar el texto</button></div>'
            f'<div class="chat">{body}</div></div>'
            f'<div class="card"><b>Comprensión global</b>{mc_block(L["global"],"lg")}'
            f'<b>Comprensión detalle · ¿V o F?</b>{vf_block(L["detalle"])}'
            f'<div class="transfer">✍️ {esc(L["transfer"])} <span style="font-weight:400;color:var(--mut)">— schrijf of zeg je antwoord.</span></div>'
            f'{gloss_block(L["glosario"])}</div>')

WEB=f"{ROOT}/03-build/web"
def audio_b64(A):
    """De opname van dit fragment, ingebed als data-URL.

    Het pad komt uit `comprension_data.AUDIO[..]["audio"]`, hetzelfde veld dat de
    generator gebruikt om het bestand te máken — zo kunnen speler en opname niet
    uit elkaar lopen. De gegevens noemen `.mp3`; op schijf staat voorlopig `.wav`,
    want er is geen omzetter in deze omgeving. Daarom probeert hij beide, en
    zet hij het juiste type erbij: een browser die `audio/mpeg` te horen krijgt
    waar WAV staat, speelt niets af.

    Ingebed en niet als los bestand, omdat de C4-hub standalone en offline moet
    werken (§16). Dat kost hier 0,5 à 1 MB per unit — bij C5/C6+ zou dat met
    zestig fragmenten niet gaan, en daar staat de audio dus wél naast de pagina.
    """
    rel=(A or {}).get("audio") or ""
    for p,mime in ((f"{WEB}/{rel}","audio/mpeg"),
                   (f"{WEB}/{rel[:-4]}.wav" if rel.endswith(".mp3") else None,"audio/wav")):
        if p and os.path.exists(p):
            return base64.b64encode(open(p,"rb").read()).decode(), mime
    return None, None

def audio_section(A, unit):
    transcript="".join(f'<div class="bub l"><span class="who">{esc(w)}</span>{esc(l)}</div>' for w,l in A["guion"])
    mp3,mime=audio_b64(A)
    if mp3:  # echte opname (onze acht Castiliaanse stemmen) → speelt op elk toestel
        player=(f'<audio id="aud" preload="metadata" src="data:{mime};base64,{mp3}"></audio>'
                f'<div class="toolbar"><button class="btn play" id="audPlay">▶ Reproducir</button>'
                f'<button class="btn" id="audSlow">🐢 Lento</button>'
                f'<button class="btn" id="audTr">👁️ Ver transcripción</button></div>')
    else:  # fallback: browser-TTS (per-spreker stem/toonhoogte) — kan robotisch of stil zijn afhankelijk van het toestel
        js_guion=json.dumps(A["guion"], ensure_ascii=False)
        player=(f'<div class="toolbar"><button class="btn play" id="audPlay" data-guion=\'{esc(js_guion)}\'>▶ Reproducir</button>'
                f'<button class="btn" id="audSlow">🐢 Lento</button>'
                f'<button class="btn" id="audTr">👁️ Ver transcripción</button></div>')
    return (f'<h2 class="sec">🎧 Escucha <span class="tipo">{esc(A["tipo"])}</span></h2>'
            f'<p class="lead"><b>{esc(A["tarea_nl"])}</b> — luister eerst zónder de tekst te lezen.</p>'
            f'<div class="card">{player}'
            f'<div class="chat" id="audText" style="display:none;margin-top:8px">{transcript}</div></div>'
            f'<div class="card"><b>Preguntas</b>{mc_block(A["preguntas"],"au")}{gloss_block(A["glosario"])}</div>')

def build(unit, out_name):
    L=CD.LECTURA.get(unit); A=CD.AUDIO.get(unit)
    if L or A:
        inner=(lectura_section(L) if L else "")+(audio_section(A, unit) if A else "")
    else:
        inner=('<div class="card ph">📖🎧 Pronto: una lectura y una audición nuevas para esta unidad.'
               '<span class="nl">Binnenkort: een nieuwe lees- en luisteroefening.</span></div>')
    html_doc=f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>C4 · U{unit} · Lee y escucha</title><style>{CSS}</style></head><body>
<div class="wrap">
 <div class="hero"><h1>📖🎧 Lee y escucha</h1>
   <p>Una lectura y una audición cortas — para entender el español que ya conoces.</p>
   <div class="nl">Una lectura y una escucha cortas: entiende el español que ya sabes. <span class="stn">korte lees- en luisteroefening</span></div></div>
 {inner}
 <div class="foot">C4 · «Bienvenidos al español» · Lee y escucha · comprensión (lezen &amp; luisteren)</div>
</div>
<script>
function esVoice(u){{var v=speechSynthesis.getVoices().find(function(x){{return /^es/i.test(x.lang)}});if(v)u.voice=v;}}
function speak(t,rate){{if(!('speechSynthesis'in window))return;var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=rate||.9;esVoice(u);speechSynthesis.cancel();speechSynthesis.speak(u);}}
if('speechSynthesis'in window)speechSynthesis.getVoices();
// meerkeuze-zelfcorrectie
document.querySelectorAll('.q[data-mc]').forEach(function(q){{q.querySelectorAll('.opt').forEach(function(b){{b.onclick=function(){{
  var ok=b.getAttribute('data-c')==='1';q.querySelectorAll('.opt').forEach(function(z){{if(z.getAttribute('data-c')==='1')z.classList.add('ok');else z.classList.remove('no');}});
  if(!ok)b.classList.add('no');q.querySelector('.fb').textContent=ok?'¡Correcto! 👏':'Mira la respuesta en verde.';}};}});}});
// V/F-zelfcorrectie
document.querySelectorAll('.q[data-vf]').forEach(function(q){{var cor=q.getAttribute('data-vf');q.querySelectorAll('.vfb').forEach(function(b){{b.onclick=function(){{
  var ok=b.getAttribute('data-v')===cor;b.classList.add(ok?'ok':'no');q.querySelector('.fb').textContent=ok?'✓':'✗ es '+cor;}};}});}});
// lees-tekst voorlezen
var rt=document.getElementById('readTts');
if(rt)rt.onclick=function(){{var t=[];document.querySelectorAll('.chat .bub, .para').forEach(function(e){{if(!e.closest('#audText'))t.push(e.textContent);}});speak(t.join('. '),.9);}};
// audio afspelen: echte mp3 (element #aud) heeft voorrang; anders browser-TTS-fallback
var au=document.getElementById('aud');
var slow=false,sl=document.getElementById('audSlow');
if(sl)sl.onclick=function(){{slow=!slow;sl.classList.toggle('on',slow);if(au)au.playbackRate=slow?.75:1;}};
var ap=document.getElementById('audPlay');
if(ap)ap.onclick=function(){{
  if(au){{au.playbackRate=slow?.75:1;try{{au.currentTime=0;}}catch(e){{}}au.play();return;}}
  var G=JSON.parse(ap.getAttribute('data-guion'));
  var voces=speechSynthesis.getVoices().filter(function(v){{return /^es/i.test(v.lang)}});
  var pitches=[1.18,0.82,1.02,0.9,1.1];var spk={{}},ord=0;
  function conf(s){{if(!(s in spk)){{spk[s]=ord;ord++;}}return spk[s];}}
  var i=0;function nx(){{if(i>=G.length)return;var s=G[i][0],t=G[i][1];var k=conf(s);
    var u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=slow?.66:.92;u.pitch=pitches[k%pitches.length];
    if(voces.length>1)u.voice=voces[k%voces.length];else if(voces.length===1)u.voice=voces[0];
    u.onend=function(){{i++;setTimeout(nx,360);}};speechSynthesis.speak(u);}}
  speechSynthesis.cancel();nx();}};
var at=document.getElementById('audTr');
if(at)at.onclick=function(){{var t=document.getElementById('audText');var show=t.style.display==='none';t.style.display=show?'flex':'none';at.classList.toggle('on',show);}};
</script></body></html>"""
    outp=f"{ROOT}/03-build/web/componentes/{out_name}"
    open(outp,"w",encoding="utf-8").write(html_doc)
    state=("lectura+audio" if (L and A) else "lectura" if L else "audio" if A else "leeg (placeholder)")
    print(f"{out_name} geschreven: {len(html_doc)} bytes · U{unit} · {state}")
    return outp

if __name__=="__main__":
    unit=int(os.environ.get("C4_UNIT","1"))
    out=os.environ.get("C4_COMPR_OUT",f"C4_U{unit}_comprension.html")
    build(unit, out)
