#!/usr/bin/env python3
"""Gedeelde JS-bouwers voor de hub-generatoren (`gen_*_web.py`).

Waarom dit bestand bestaat: `buildChoice`, `buildMatch`, `buildOrder` en `buildOdd`
stonden zestien keer letterlijk gekopieerd, één keer per generator. Elke verbetering
kostte daardoor zestien bestanden. Ze staan nu één keer hier.

Wat NIET hier staat: `buildInlineExercises` en `buildRecorders`. Die verschillen per
unit omdat ze de *inhoud* van die unit bevatten (de oefeningen zelf, de opnameopdrachten).
Dat is geen duplicatie maar data, en die blijft in de generator van de unit staan.

Naamgeving: C5 U0 is ouder en noemt dezelfde motoren `exChoice`/`exMatch`/`exOrder`/
`exOdd`, plus een eigen `buildMatch(el,title,pairs)` met positionele argumenten.
Beide varianten worden hier expliciet aangeboden — `engines(prefix="ex")` en
`MATCH_LEGACY_JS` — zodat U0 niet stilzwijgend wordt gelijkgetrokken.

Gebruik in een generator:

    import hub_drills
    JS = r'''…''' + hub_drills.HELPERS_JS + hub_drills.engines() + r'''…'''
"""

# --- TTS: spreekt een Spaanse string uit via de browser ---
SPEAK_JS = r"""function speak(t,rate){if(!('speechSynthesis'in window))return;const u=new SpeechSynthesisUtterance(t);u.lang='es-ES';u.rate=rate||.92;
  const vs=speechSynthesis.getVoices();const es=vs.find(v=>/^es/i.test(v.lang));if(es)u.voice=es;try{speechSynthesis.cancel();speechSynthesis.speak(u);}catch(e){}}"""

# --- MediaRecorder: opnemen → terugluisteren → opnieuw ---
RECORDER_JS = r"""function makeRecorder(elId, cfg){const el=document.getElementById(elId);if(!el)return;
 el.classList.add('rec');
 let idx=0, media=null, chunks=[], stream=null, curURL=null;
 const items=cfg.items;
 el.innerHTML='<h3>'+cfg.title+'</h3><p class="desc">'+cfg.desc+'</p>'+
   '<div class="scorebar"><span>Ítem <b class="pos">1</b>/'+items.length+'</span></div>'+
   '<div class="cue" id="'+elId+'_cue"></div><div class="target" id="'+elId+'_tg"></div>'+
   '<div class="rbtns">'+(TTS?'<button class="rbtn sec" id="'+elId+'_play">🔊 Escuchar</button>':'')+
   '<button class="rbtn" id="'+elId+'_rec">⏺ Grabar</button>'+
   '<button class="rbtn sec" id="'+elId+'_mine" disabled>▶ Mi grabación</button>'+
   '<button class="rbtn sec" id="'+elId+'_next">Siguiente ▸</button></div>'+
   '<div id="'+elId+'_au"></div><div class="moods" id="'+elId+'_mood"></div><div id="'+elId+'_fb" class="fb"></div>';
 const tg=el.querySelector('#'+elId+'_tg'),cue=el.querySelector('#'+elId+'_cue'),pos=el.querySelector('.pos');
 const bRec=el.querySelector('#'+elId+'_rec'),bMine=el.querySelector('#'+elId+'_mine'),bNext=el.querySelector('#'+elId+'_next'),bPlay=el.querySelector('#'+elId+'_play');
 const au=el.querySelector('#'+elId+'_au'),moodbox=el.querySelector('#'+elId+'_mood');
 function load(){const it=items[idx];pos.textContent=idx+1;cue.textContent=it.cue||'';tg.innerHTML=it.text;au.innerHTML='';bMine.disabled=true;moodbox.innerHTML='';el.querySelector('#'+elId+'_fb').className='fb';
   ['☹','😐','☺'].forEach((m,mi)=>{const b=document.createElement('div');b.className='mood';b.textContent=m;b.onclick=()=>{moodbox.querySelectorAll('.mood').forEach(x=>x.classList.remove('on'));b.classList.add('on');feedback(el.querySelector('#'+elId+'_fb'),true,(it.tip||'¡Bien! Prueba otra vez para mejorar.'));};moodbox.appendChild(b);});}
 if(bPlay)bPlay.onclick=()=>speak((items[idx].text||'').replace(/<[^>]+>/g,''));
 bNext.onclick=()=>{idx=(idx+1)%items.length;load();};
 async function start(){
   if(!navigator.mediaDevices||!window.MediaRecorder){warn();return;}
   try{stream=await navigator.mediaDevices.getUserMedia({audio:true});}catch(e){warn();return;}
   chunks=[];media=new MediaRecorder(stream);media.ondataavailable=e=>chunks.push(e.data);
   media.onstop=()=>{const blob=new Blob(chunks,{type:'audio/webm'});if(curURL)URL.revokeObjectURL(curURL);curURL=URL.createObjectURL(blob);
     au.innerHTML='<audio controls src="'+curURL+'"></audio>';bMine.disabled=false;stream.getTracks().forEach(t=>t.stop());};
   media.start();bRec.textContent='⏹ Parar';bRec.classList.add('rec-on');}
 function stop(){if(media&&media.state!=='inactive')media.stop();bRec.textContent='⏺ Grabar';bRec.classList.remove('rec-on');}
 bRec.onclick=()=>{if(media&&media.state==='recording')stop();else start();};
 bMine.onclick=()=>{const a=au.querySelector('audio');if(a)a.play();};
 function warn(){el.querySelector('#'+elId+'_fb').className='fb bad';el.querySelector('#'+elId+'_fb').innerHTML='🎙️ Micrófono no disponible — usa Chrome/Edge y permite el micrófono. Puedes escuchar el modelo (🔊) y practicar en voz alta.';}
 load();}"""

# --- Hulpfuncties: steekproef uit een pool, HTML-escape, gaatjes renderen ---
HELPERS_JS = r"""function exSample(pool,n){const a=pool.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a.slice(0,Math.min(n,a.length));}
function exEsc(s){return String(s).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
function exFmt(s){return exEsc(s).replace(/___+/g,'<span class="gap">&nbsp;&nbsp;</span>');}"""

# --- De vier klik-motoren. Identiek in alle zestien nieuwere generatoren. ---
_ENGINES = {
 "Choice": r"""function buildChoice(id,cfg){
 const host=document.getElementById(id);if(!host)return;const per=cfg.per||Math.min(6,cfg.pool.length);
 function render(){const series=exSample(cfg.pool,per);let ok=0;
   host.innerHTML='<div class="exhead"><h3>'+cfg.title+'</h3><button class="otra" type="button">↻ otra serie</button></div><p class="desc">'+cfg.desc+'</p><div class="qlist"></div><div class="exscore">Juist: <b class="ok">0</b>/'+series.length+'</div>';
   host.querySelector('.otra').onclick=render;const list=host.querySelector('.qlist'),scoreEl=host.querySelector('.ok');
   series.forEach(it=>{const q=document.createElement('div');q.className='exq';
     q.innerHTML='<div class="qz">'+exFmt(it.q)+'</div><div class="exopts"></div><div class="exwhy"></div>';
     const opts=q.querySelector('.exopts'),why=q.querySelector('.exwhy');let locked=false;
     exSample(it.opts,it.opts.length).forEach(o=>{const b=document.createElement('button');b.className='exopt';b.type='button';b.textContent=o;
       b.onclick=()=>{if(locked)return;locked=true;const good=o===it.ans;
         opts.querySelectorAll('.exopt').forEach(x=>{x.disabled=true;if(x.textContent===it.ans)x.classList.add('ok');});
         if(good){ok++;scoreEl.textContent=ok;}else{b.classList.add('no');}
         why.className='exwhy show '+(good?'g':'b');why.innerHTML=(good?'✅ ¡correcto! ':'❌ → '+exEsc(it.ans)+'. ')+(it.why?exEsc(it.why):'');};
       opts.appendChild(b);});
     list.appendChild(q);});}
 render();}""",
 "Match":  r"""function buildMatch(id,cfg){
 const host=document.getElementById(id);if(!host)return;const per=cfg.per||Math.min(6,cfg.pool.length);
 function render(){const series=exSample(cfg.pool,per);let doneN=0;
   host.innerHTML='<div class="exhead"><h3>'+cfg.title+'</h3><button class="otra" type="button">↻ otra serie</button></div><p class="desc">'+cfg.desc+'</p><div class="mcol"><div class="mL"></div><div class="mR"></div></div><div class="exscore">Emparejados: <b class="ok">0</b>/'+series.length+'</div>';
   host.querySelector('.otra').onclick=render;const L=host.querySelector('.mL'),R=host.querySelector('.mR'),scoreEl=host.querySelector('.ok');
   const right=exSample(series.map((p,i)=>({p,i})),series.length);let selL=null,busy=false;
   series.forEach((p,i)=>{const c=document.createElement('div');c.className='mcell';c.textContent=p.a;c.dataset.i=i;
     c.onclick=()=>{if(busy||c.classList.contains('done'))return;if(selL)selL.classList.remove('sel');selL=c;c.classList.add('sel');};L.appendChild(c);});
   right.forEach(o=>{const c=document.createElement('div');c.className='mcell';c.textContent=o.p.b;c.dataset.i=o.i;
     c.onclick=()=>{if(busy||!selL||c.classList.contains('done'))return;busy=true;const good=selL.dataset.i===c.dataset.i;
       if(good){selL.classList.remove('sel');selL.classList.add('done');c.classList.add('done');doneN++;scoreEl.textContent=doneN;selL=null;busy=false;}
       else{c.classList.add('bad');const s=selL;setTimeout(()=>{c.classList.remove('bad');s.classList.remove('sel');selL=null;busy=false;},600);}};R.appendChild(c);});}
 render();}""",
 "Order":  r"""function buildOrder(id,cfg){
 const host=document.getElementById(id);if(!host)return;let ri=Math.floor(Math.random()*cfg.rounds.length);
 function render(){const round=cfg.rounds[ri];const sorted=round.items.slice().sort((a,b)=>a.key-b.key);let pos=0,mist=0;
   host.innerHTML='<div class="exhead"><h3>'+cfg.title+'</h3><button class="otra" type="button">↻ otra ronda</button></div><p class="desc">'+cfg.desc+' · <b>'+exEsc(round.sub||'')+'</b></p><div class="oslots"></div><div class="obank"></div><div class="exwhy"></div>';
   host.querySelector('.otra').onclick=()=>{ri=(ri+1)%cfg.rounds.length;render();};
   const slots=host.querySelector('.oslots'),bank=host.querySelector('.obank'),why=host.querySelector('.exwhy');
   sorted.forEach((_,i)=>{const s=document.createElement('div');s.className='oslot';s.textContent=(i+1);s.dataset.pos=i;slots.appendChild(s);});
   exSample(round.items,round.items.length).forEach(it=>{const b=document.createElement('button');b.className='ochip';b.type='button';b.textContent=it.label;
     b.onclick=()=>{if(b.classList.contains('used'))return;const exp=sorted[pos];
       if(it.key===exp.key){b.classList.add('used');const sl=slots.querySelector('.oslot[data-pos="'+pos+'"]');sl.classList.add('filled');sl.textContent=(pos+1)+'. '+it.label;pos++;
         if(pos>=sorted.length){why.className='exwhy show '+(mist===0?'g':'b');why.innerHTML=mist===0?'✅ ¡Perfecto! sin errores.':'✔ Completado con '+mist+' error(es). Prueba «otra ronda».';}}
       else{mist++;b.classList.remove('shake');void b.offsetWidth;b.classList.add('shake');why.className='exwhy show b';why.innerHTML='❌ Primero: <b>'+exEsc(exp.label)+'</b>';}};
     bank.appendChild(b);});}
 render();}""",
 "Odd":    r"""function buildOdd(id,cfg){
 const host=document.getElementById(id);if(!host)return;const per=cfg.per||Math.min(5,cfg.pool.length);
 function render(){const series=exSample(cfg.pool,per);let ok=0;
   host.innerHTML='<div class="exhead"><h3>'+cfg.title+'</h3><button class="otra" type="button">↻ otra serie</button></div><p class="desc">'+cfg.desc+'</p><div class="qlist"></div><div class="exscore">Juist: <b class="ok">0</b>/'+series.length+'</div>';
   host.querySelector('.otra').onclick=render;const list=host.querySelector('.qlist'),scoreEl=host.querySelector('.ok');
   series.forEach(it=>{const q=document.createElement('div');q.className='exq';q.innerHTML='<div class="exopts"></div><div class="exwhy"></div>';
     const opts=q.querySelector('.exopts'),why=q.querySelector('.exwhy');let locked=false;
     exSample(it.words.map((w,i)=>({w,i})),it.words.length).forEach(o=>{const b=document.createElement('button');b.className='exopt';b.type='button';b.textContent=o.w;
       b.onclick=()=>{if(locked)return;locked=true;const good=o.i===it.odd;opts.querySelectorAll('.exopt').forEach(x=>x.disabled=true);
         if(good){ok++;scoreEl.textContent=ok;b.classList.add('ok');}else{b.classList.add('no');opts.querySelectorAll('.exopt').forEach(x=>{if(x.textContent===it.words[it.odd])x.classList.add('ok');});}
         why.className='exwhy show '+(good?'g':'b');why.innerHTML=(good?'✅ ¡bien! ':'❌ → '+exEsc(it.words[it.odd])+'. ')+(it.why?exEsc(it.why):'');};
       opts.appendChild(b);});
     list.appendChild(q);});}
 render();}""",
}

# C5 U0 gebruikt hiernaast nog een oudere matching-motor met positionele argumenten:
# buildMatch(el, title, pairs). Bewust behouden, niet gelijkgetrokken.
MATCH_LEGACY_JS = r"""function buildMatch(el,title,pairs){let pt=0,st=0,sel=null,done=0;
 const L=pairs.map(p=>p[0]),Rr=pairs.map(p=>p[1]).slice().sort(()=>Math.random()-.5);
 el.innerHTML='<h3>'+title+'</h3><p class="desc">Klik een kaart links, dan de juiste rechts.</p>'+scoreBar('m'+title.length)+
  '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px"><div class="chips" style="flex-direction:column" id="mL"></div><div class="chips" style="flex-direction:column" id="mR"></div></div><div class="fb" id="mfb"></div>';
 const sb=el.querySelector('.scorebar');const cL=el.querySelector('#mL'),cR=el.querySelector('#mR');
 L.forEach((t,i)=>{const c=document.createElement('div');c.className='chip';c.textContent=t;c.dataset.i=i;c.onclick=()=>{cL.querySelectorAll('.chip').forEach(z=>z.classList.remove('sel'));c.classList.add('sel');sel=i};cL.appendChild(c);});
 Rr.forEach(t=>{const c=document.createElement('div');c.className='chip';c.textContent=t;c.onclick=()=>{if(sel==null){return}const want=pairs[sel][1];const ok=t===want;
   if(ok){c.classList.add('ok');cL.querySelector('.chip[data-i="'+sel+'"]').classList.add('ok');pt++;st++;done++;feedback(el.querySelector('#mfb'),true,pairs[sel][0]+' → '+t);
     if(done===pairs.length)feedback(el.querySelector('#mfb'),true,'¡Completado! '+pt+' correct.');}
   else{st=0;c.classList.add('no');setTimeout(()=>c.classList.remove('no'),500);feedback(el.querySelector('#mfb'),false,'Probeer opnieuw.');}
   setScore(sb,pt,st);sel=null;cL.querySelectorAll('.chip').forEach(z=>z.classList.remove('sel'));};cR.appendChild(c);});}"""


def engines(prefix="build", include=("Choice", "Match", "Order", "Odd")):
    """Geeft de gevraagde motoren als JS-string terug.

    prefix="build" levert buildChoice/buildMatch/buildOrder/buildOdd (zestien hubs);
    prefix="ex" levert exChoice/exMatch/exOrder/exOdd (C5 U0).
    """
    js = "\n".join(_ENGINES[n] for n in include)
    if prefix != "build":
        for n in include:
            js = js.replace("build" + n, prefix + n)
    return js


CHOICE_JS = _ENGINES["Choice"]
MATCH_JS  = _ENGINES["Match"]
ORDER_JS  = _ENGINES["Order"]
ODD_JS    = _ENGINES["Odd"]


def one(name, prefix="build"):
    """Eén motor, eventueel onder de oude `ex`-naam van C5 U0."""
    return engines(prefix, (name,))


# ---------------------------------------------------------------------------
# buildType — getypte drill (fase 4-5 van de ladder: ophalen en produceren)
#
# De panelen bevatten tot nu toe alleen klik- en koppelwerk: de leerling herkent,
# maar schrijft niets. Deze motor sluit dat gat.
#
#   buildType('gx_perfecto', {
#     title:'Experiencias', desc:'Vul de juiste vorm in.',
#     perBlock:10,          // visuele blokken; nummering en score lopen door
#     accents:'strict',     // 'strict' bij werkwoordsvormen, 'soft' bij woordenschat
#     expect:30,            // console.assert op het itemaantal
#     items:[{q:'Hoy Lucia ___ (visitar) el Prado.', ans:'ha visitado',
#             alt:[], why:'haber + participio', hint:'h_ v_______'}]
#   });
#
# Accentbeleid (beslissing C): 'strict' rekent hablo/hablo-met-accent als verschillend
# af; 'soft' laat de eerste poging zonder accent toe en toont het accent in de
# correctie. De n-tilde blijft in beide standen betekenisdragend — anno en ano
# worden dus nooit gelijkgesteld aan het woord met de tilde.
# ---------------------------------------------------------------------------
TYPE_JS = r"""
function tyNorm(s,mode){
 s=String(s).toLowerCase().trim().replace(/[¿?¡!.,;:]/g,'').replace(/\s+/g,' ');
 if(mode==='soft'){s=s.replace(/\u00f1/g,'\u0001').normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/\u0001/g,'\u00f1');}
 return s;}
function tyOk(val,it,mode){return [it.ans].concat(it.alt||[]).some(a=>tyNorm(a,mode)===tyNorm(val,mode));}
function buildType(id,cfg){
 const host=document.getElementById(id);if(!host)return;
 const items=cfg.items||[],n=items.length,mode=cfg.accents||'soft',per=cfg.perBlock||10;
 if(cfg.expect)console.assert(n===cfg.expect,'buildType '+id+': '+n+' items, verwacht '+cfg.expect);
 let done=false;
 host.innerHTML='<div class="exhead"><h3>'+cfg.title+'</h3><span class="tymode">'+(mode==='strict'?'acentos obligatorios':'acentos tolerantes')+'</span></div><p class="desc">'+cfg.desc+'</p><div class="tywrap"></div><div class="tybar"><button class="otra tycheck" type="button">✓ Comprobar</button><button class="otra tyagain" type="button" hidden>↻ Reintentar</button><button class="otra tysol" type="button" hidden>👁 Ver solución</button><span class="exscore" role="status" aria-live="polite">Juist: <b class="ok">0</b>/'+n+'</span></div>';
 const wrap=host.querySelector('.tywrap'),bChk=host.querySelector('.tycheck'),bAgn=host.querySelector('.tyagain'),bSol=host.querySelector('.tysol'),scoreEl=host.querySelector('.ok');
 let blk=null;
 items.forEach((it,i)=>{
   if(i%per===0){blk=document.createElement('div');blk.className='tyblok';
     if(n>per)blk.innerHTML='<div class="tyblokkop">'+(i+1)+'–'+Math.min(i+per,n)+'</div>';
     wrap.appendChild(blk);}
   const row=document.createElement('div');row.className='exq tyq';
   row.innerHTML='<div class="qz"><span class="tynum">'+(i+1)+'</span><span>'+exFmt(it.q)+'</span></div>'+
     '<div class="tyin"><input type="text" class="tyfield" autocomplete="off" autocapitalize="none" spellcheck="false" aria-label="Vraag '+(i+1)+' van '+n+'">'+
     (it.hint?'<button class="typista" type="button" aria-label="Toon een letterhint bij vraag '+(i+1)+'">pista</button>':'')+'</div>'+
     '<div class="exwhy" role="status" aria-live="polite"></div>';
   const inp=row.querySelector('.tyfield'),why=row.querySelector('.exwhy'),pista=row.querySelector('.typista');
   if(pista)pista.onclick=()=>{why.className='exwhy show n';why.innerHTML='<b>pista</b> · '+exEsc(it.hint);};
   inp.addEventListener('keydown',e=>{if(e.key!=='Enter')return;e.preventDefault();
     const all=[].slice.call(wrap.querySelectorAll('.tyfield:not([disabled])')),p=all.indexOf(inp);
     if(p>-1&&p<all.length-1)all[p+1].focus();else bChk.click();});
   row._it=it;row._inp=inp;row._why=why;blk.appendChild(row);});
 function rows(){return [].slice.call(wrap.querySelectorAll('.tyq'));}
 function check(){let ok=0;
   rows().forEach(r=>{const it=r._it,inp=r._inp,why=r._why;
     if(inp.disabled){ok++;return;}
     const val=inp.value.trim();
     if(val&&tyOk(val,it,mode)){ok++;inp.disabled=true;inp.classList.add('good');inp.setAttribute('aria-invalid','false');
       r.classList.add('tygood');why.className='exwhy show g';
       const exact=[it.ans].concat(it.alt||[]).indexOf(val)>-1;
       why.innerHTML='<b>✓ correcto</b>'+(exact?'':' · schrijfwijze: <b>'+exEsc(it.ans)+'</b>')+(it.why?' · '+exEsc(it.why):'');}
     else{inp.classList.add('bad');inp.setAttribute('aria-invalid','true');
       r.classList.add('tybad');why.className='exwhy show b';
       why.innerHTML='<b>✗ nog niet</b>'+(val?' · jij schreef «'+exEsc(val)+'»':' · nog leeg')+(done?' · antwoord: <b>'+exEsc(it.ans)+'</b>':'')+(done&&it.why?' · '+exEsc(it.why):'');}});
   scoreEl.textContent=ok;return ok;}
 let rondes=0;
 bChk.onclick=()=>{const ok=check();rondes++;
   if(ok===n){bChk.disabled=true;bAgn.hidden=true;bSol.hidden=true;
     if(!host.querySelector('.tyklaar'))host.querySelector('.tybar').insertAdjacentHTML('beforeend','<span class="tyklaar">✓ ¡Completo! '+n+'/'+n+'</span>');
     return;}
   // Ophalen vóór opnieuw tonen: de leerling mag blijven proberen; de oplossing
   // komt er pas op verzoek, en pas na een tweede poging.
   bAgn.hidden=false;bSol.hidden=rondes<2;};
 bAgn.onclick=()=>{rows().forEach(r=>{if(r._inp.disabled)return;
     r._inp.classList.remove('bad');r._inp.removeAttribute('aria-invalid');r._inp.value='';
     r.classList.remove('tybad');r._why.className='exwhy';});
   bAgn.hidden=true;
   const f=wrap.querySelector('.tyfield:not([disabled])');if(f)f.focus();};
 bSol.onclick=()=>{done=true;check();
   rows().forEach(r=>{if(!r._inp.disabled)r._inp.disabled=true;});
   bChk.disabled=true;bAgn.hidden=true;bSol.hidden=true;};
}
"""

TYPE_CSS = r"""
.tymode{font-size:11px;font-weight:700;color:var(--gd);background:var(--gt);border-radius:999px;padding:3px 9px;white-space:nowrap}
.tyblokkop{font-family:var(--disp);font-size:12px;font-weight:700;color:var(--mut);letter-spacing:.06em;margin:14px 0 2px}
.tyq .qz{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}
.tynum{display:inline-flex;align-items:center;justify-content:center;min-width:22px;height:22px;border-radius:7px;background:var(--gt);color:var(--gd);font-size:12px;font-weight:800;flex:none}
.tyin{display:flex;gap:8px;align-items:center;margin-top:8px;flex-wrap:wrap}
.tyfield{flex:1 1 160px;min-width:0;max-width:100%;border:1.5px solid var(--line);border-radius:10px;padding:8px 11px;font-size:15px;font-family:var(--body);background:var(--card);color:var(--ink)}
.tyfield:focus-visible,.typista:focus-visible,.otra:focus-visible,.escbtn:focus-visible{outline:3px solid var(--gd);outline-offset:2px}
.tyfield.good{border-color:var(--g);background:var(--gt);color:var(--gd);font-weight:700}
.tyfield.bad{border-color:var(--red);background:#fdeaea}
.typista{border:1.5px dashed var(--line);background:transparent;color:var(--mut);border-radius:9px;padding:7px 11px;font-size:12px;font-weight:700;cursor:pointer;font-family:var(--disp);flex:none}
.exwhy.n{background:#fff7e6;color:#8a5a00}
.tybar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-top:14px}
.tybar .exscore{margin-top:0}
.tycheck{background:var(--g);color:#fff}
.tycheck[disabled]{opacity:.5;cursor:default}
.tyklaar{font-size:13px;font-weight:800;color:var(--gd)}
"""
