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
     q.innerHTML='<div class="qz">'+(it.say?'<button class="exsay" type="button" aria-label="Escuchar la palabra">'+IC.sound+'</button> ':'')+exFmt(it.q)+'</div><div class="exopts"></div><div class="exwhy"></div>';
     const opts=q.querySelector('.exopts'),why=q.querySelector('.exwhy');let locked=false;
     const bs=q.querySelector('.exsay');if(bs)bs.onclick=()=>speak(it.say);
     exSample(it.opts,it.opts.length).forEach(o=>{const b=document.createElement('button');b.className='exopt';b.type='button';b.textContent=o;
       b.onclick=()=>{if(locked)return;locked=true;const good=o===it.ans;
         opts.querySelectorAll('.exopt').forEach(x=>{x.disabled=true;if(x.textContent===it.ans)x.classList.add('ok');});
         if(good){ok++;scoreEl.textContent=ok;}else{b.classList.add('no');}
         why.className='exwhy show '+(good?'g':'b');why.innerHTML=(good?IC.bien+' ¡correcto! ':IC.mal+' → '+exEsc(it.ans)+'. ')+(it.why?exEsc(it.why):'');};
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
         if(pos>=sorted.length){why.className='exwhy show '+(mist===0?'g':'b');why.innerHTML=mist===0?IC.bien+' ¡Perfecto! sin errores.':'✔ Completado con '+mist+' error(es). Prueba «otra ronda».';}}
       else{mist++;b.classList.remove('shake');void b.offsetWidth;b.classList.add('shake');why.className='exwhy show b';why.innerHTML=IC.mal+' Primero: <b>'+exEsc(exp.label)+'</b>';}};
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
         why.className='exwhy show '+(good?'g':'b');why.innerHTML=(good?IC.bien+' ¡bien! ':IC.mal+' → '+exEsc(it.words[it.odd])+'. ')+(it.why?exEsc(it.why):'');};
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
 host.innerHTML='<div class="exhead"><h3>'+cfg.title+'</h3><span class="tymode">'+(mode==='strict'?'acentos obligatorios':'acentos tolerantes')+'</span></div><p class="desc">'+cfg.desc+'</p><div class="tywrap"></div><div class="tybar"><button class="otra tycheck" type="button">'+IC.check+' Comprobar</button><button class="otra tyagain" type="button" hidden>↻ Reintentar</button><button class="otra tysol" type="button" hidden>👁 Ver solución</button><span class="exscore" role="status" aria-live="polite">Juist: <b class="ok">0</b>/'+n+'</span></div>';
 const wrap=host.querySelector('.tywrap'),bChk=host.querySelector('.tycheck'),bAgn=host.querySelector('.tyagain'),bSol=host.querySelector('.tysol'),scoreEl=host.querySelector('.ok');
 let blk=null;
 items.forEach((it,i)=>{
   if(i%per===0){blk=document.createElement('div');blk.className='tyblok';
     if(n>per)blk.innerHTML='<div class="tyblokkop">'+(i+1)+'–'+Math.min(i+per,n)+'</div>';
     wrap.appendChild(blk);}
   const row=document.createElement('div');row.className='exq tyq';
   const hoor=(cfg.speak&&it.say&&typeof speak==='function')?'<button class="tyspk" type="button" aria-label="Luister naar item '+(i+1)+'">\U0001F50A</button>':'';
   row.innerHTML='<div class="qz"><span class="tynum">'+(i+1)+'</span>'+hoor+'<span>'+exFmt(it.q)+'</span></div>'+
     '<div class="tyin"><input type="text" class="tyfield" autocomplete="off" autocapitalize="none" spellcheck="false" aria-label="Vraag '+(i+1)+' van '+n+'">'+
     (it.hint?'<button class="typista" type="button" aria-label="Toon een letterhint bij vraag '+(i+1)+'">pista</button>':'')+'</div>'+
     '<div class="exwhy" role="status" aria-live="polite"></div>';
   const inp=row.querySelector('.tyfield'),why=row.querySelector('.exwhy'),pista=row.querySelector('.typista');
   if(pista)pista.onclick=()=>{why.className='exwhy show n';why.innerHTML='<b>pista</b> · '+exEsc(it.hint);};
   const spk=row.querySelector('.tyspk');
   if(spk){spk.onclick=()=>speak(it.say);setTimeout(()=>{if(i===0&&cfg.autoplay)speak(it.say);},300);}
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
       why.innerHTML='<b>'+IC.bien+' correcto</b>'+(exact?'':' · schrijfwijze: <b>'+exEsc(it.ans)+'</b>')+(it.why?' · '+exEsc(it.why):'');}
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
.tyspk{border:none;background:var(--gt);color:var(--gd);border-radius:8px;padding:3px 9px;font-size:14px;cursor:pointer;flex:none}
.tyspk:focus-visible{outline:3px solid var(--gd);outline-offset:2px}
/* De typ-oefeningen zijn de kern van de productieve fase: geef ze een eigen,
   herkenbare rand zodat de leerling meteen ziet dat hier geschreven wordt. */
.card.ex.escribe{border-left:5px solid var(--g)}
"""


# ---------------------------------------------------------------------------
# buildEscucha — luisterblok met verwisselbare audiobron
#
# De meting van 2026-07-29 was hard: C5 heeft 9/9 units met een Lectura-paneel en
# 0/9 met een luisterpaneel. Wat er stond waren losse TTS-knopjes die één woord
# uitspreken — geen luisterbegrip. Dit component vult die leemte.
#
# De audiobron is verwisselbaar, zodat de bouw nergens op wacht:
#   * geen mp3 aanwezig  -> browser-TTS leest het guion voor, met een eigen
#                           stemprofiel (toonhoogte/tempo) per spreker;
#   * mp3 aanwezig       -> die wordt automatisch gebruikt, zonder de oefeningen
#                           opnieuw te bouwen. cfg.audioLineas (van --split) geeft
#                           bovendien klik-om-te-horen per regel.
# Het component probeert de mp3 te laden en valt bij een laadfout terug op TTS.
#
# De luisterladder heeft zes treden (VIER_VAARDIGHEDEN_GEINTEGREERD.md):
#   1 situatie vooraf   2 globaal begrip   3 vijf detailvragen
#   4 juist/fout met bewijs   5 transcript pas NA de taken   6 productieve reactie
#
#   buildEscucha('esc_c5u0', {
#     title:'En el aeropuerto', audio:'audio/C5_U0.mp3',
#     situacion:{lugar:'Barajas, Madrid', quien:'Lucia y tu',
#                que:'Se presentan en la puerta de embarque', claves:['hola','me llamo','de donde']},
#     guion:[{who:'Lucia', es:'Hola, me llamo Lucia.', nl:'Hallo, ik heet Lucia.'}],
#     global:{q:'Waar gaat het fragment over?', opts:[...], ans:'...'},
#     detalle:[{q, opts, ans, why} x5],
#     vf:[{q:'Lucia es de Sevilla.', ans:true, prueba:'Soy de Sevilla'}],
#     produccion:{prompt:'Contesta a Lucia...', modo:'escribir'}
#   });
# ---------------------------------------------------------------------------
ESCUCHA_JS = r"""
function escPerfil(i){const p=[{rate:.92,pitch:1.12},{rate:.88,pitch:.85},{rate:.95,pitch:1.0},{rate:.9,pitch:1.25}];return p[i%p.length];}
function escReproductor(cfg,onEstado){
 // Verwisselbare bron: probeer de mp3, val bij een laadfout terug op browser-TTS.
 const guion=cfg.guion||[],hablantes=[];
 guion.forEach(g=>{if(hablantes.indexOf(g.who)<0)hablantes.push(g.who);});
 let modo=cfg.audio?'mp3':'tts',el=null,idx=0,parado=true;
 // het etiket start op «voz del navegador» en gaat pas naar «audio grabado»
 // als de mp3 werkelijk begint te spelen (zie reproducir)
 // De mp3 wordt pas bij de eerste klik geladen. Zou het component het bestand al
 // bij het openen van de pagina proberen, dan logt de browser een netwerkfout
 // zolang er nog geen opname bestaat — en dan is «geen consolefouten» geen
 // bruikbare rooktest meer bij het bouwen van een unit.
 // Het pad in de gegevens zegt .mp3, maar de opnames zijn wav (er is geen
 // ffmpeg in de bouwomgeving). In plaats van de gegevens te laten liegen over
 // wat er staat, probeert de speler beide: eerst het opgegeven pad, dan dezelfde
 // naam met de andere extensie, en pas dán de stem van de browser. Zo werkt het
 // vóór én na een omzetting naar mp3, zonder dat er iets bijgewerkt moet worden.
 let alternado=false;
 function otraExtension(u){return /\.mp3$/i.test(u)?u.replace(/\.mp3$/i,'.wav')
                                                  :u.replace(/\.wav$/i,'.mp3');}
 function fuente(){if(el||!cfg.audio)return el;
   el=new Audio(cfg.audio);el.preload='none';
   el.addEventListener('error',()=>{
     if(!alternado){alternado=true;el.src=otraExtension(cfg.audio);
       if(!parado)el.play().catch(()=>{});return;}
     modo='tts';onEstado&&onEstado(modo,!parado);if(!parado){idx=0;ttsSecuencia();}});
   el.addEventListener('ended',()=>{parado=true;onEstado&&onEstado(modo,false);});
   return el;}
 function ttsLinea(i,despues){
   if(!('speechSynthesis'in window)){parado=true;onEstado&&onEstado(modo,false);return;}
   const g=guion[i];if(!g){parado=true;onEstado&&onEstado(modo,false);return;}
   const perf=escPerfil(hablantes.indexOf(g.who)),u=new SpeechSynthesisUtterance(g.es);
   u.lang='es-ES';u.rate=perf.rate;u.pitch=perf.pitch;
   const vs=speechSynthesis.getVoices(),es=vs.find(v=>/^es/i.test(v.lang));if(es)u.voice=es;
   u.onend=()=>{if(despues)despues();};
   try{speechSynthesis.speak(u);}catch(e){}}
 function ttsSecuencia(){if(parado)return;if(idx>=guion.length){parado=true;idx=0;onEstado&&onEstado(modo,false);return;}
   const i=idx++;ttsLinea(i,ttsSecuencia);}
 return {
  get modo(){return modo;},
  reproducir(){parado=false;onEstado&&onEstado(modo,true);
    const a=modo==='mp3'?fuente():null;
    if(a){a.play().then(()=>{onEstado&&onEstado('mp3',true);}).catch(()=>{modo='tts';onEstado&&onEstado(modo,true);idx=0;ttsSecuencia();});}
    else{try{speechSynthesis.cancel();}catch(e){}idx=0;ttsSecuencia();}},
  parar(){parado=true;if(el){el.pause();el.currentTime=0;}try{speechSynthesis.cancel();}catch(e){}onEstado&&onEstado(modo,false);},
  linea(i){const u=(cfg.audioLineas||[])[i];
    if(u){const a=new Audio(u);a.play().catch(()=>ttsLinea(i));return;}
    try{speechSynthesis.cancel();}catch(e){}ttsLinea(i);}
 };}
function buildEscucha(id,cfg){
 const host=document.getElementById(id);if(!host)return;
 const G=cfg.guion||[],det=cfg.detalle||[],vf=cfg.vf||[],S=cfg.situacion||{};
 if(cfg.expectDetalle)console.assert(det.length===cfg.expectDetalle,'buildEscucha '+id+': '+det.length+' detailvragen, verwacht '+cfg.expectDetalle);
 const estado={glob:false,det:0,vf:0};
 host.innerHTML=
  '<div class="exhead"><h3>🎧 '+cfg.title+'</h3><span class="escfuente" role="status" aria-live="polite"></span></div>'+
  '<ol class="escladder">'+
   '<li class="escpaso" data-p="1"><h4>1 · Antes de escuchar</h4><div class="escsit"></div></li>'+
   '<li class="escpaso" data-p="2"><h4>2 · Escucha global</h4><div class="escplay"></div><div class="escglob"></div></li>'+
   '<li class="escpaso" data-p="3"><h4>3 · Escucha con detalle</h4><div class="escdet"></div></li>'+
   '<li class="escpaso" data-p="4"><h4>4 · Verdadero o falso — con prueba</h4><div class="escvf"></div></li>'+
   '<li class="escpaso" data-p="5"><h4>5 · Transcripción</h4><div class="esctr"></div></li>'+
   '<li class="escpaso" data-p="6"><h4>6 · Tu reacción</h4><div class="escprod"></div></li>'+
  '</ol>';
 // Het anker uit `escucha_data`: de QR-code in het boek komt hier uit
 // (#c5-u1-esc-01). De korte fragmenten hadden zo'n anker al, deze — de langste
 // luistertaak van de unit, twintig minuten les — kreeg er nooit een, dus wees
 // er geen enkele code naartoe. Als los spannetje en niet als id op de host:
 // `buildAudioCortos` zoekt die host meteen daarna op bij zijn oude naam.
 if(cfg.ancla){const an=document.createElement('span');an.id=cfg.ancla;
   an.className='ancla';an.setAttribute('aria-hidden','true');
   host.insertBefore(an,host.firstChild);}
 const $=s=>host.querySelector(s);
 const fuente=$('.escfuente');
 const player=escReproductor(cfg,(modo,sonando)=>{
   fuente.textContent=modo==='mp3'?'audio grabado':'voz del navegador';
   const b=$('.escbtn-play');if(b)b.textContent=sonando?'⏹ Parar':'▶ Escuchar';});
 fuente.textContent='voz del navegador';
 // 1 · situatie vooraf
 $('.escsit').innerHTML='<div class="escficha">'+
   (S.lugar?'<p><b>¿Dónde?</b> '+exEsc(S.lugar)+'</p>':'')+
   (S.quien?'<p><b>¿Quién habla?</b> '+exEsc(S.quien)+'</p>':'')+
   (S.que?'<p><b>¿Qué pasa?</b> '+exEsc(S.que)+'</p>':'')+
   '</div><p class="desc">Drie sleutelwoorden vooraf — klik om ze te horen:</p><div class="escclaves"></div>';
 (S.claves||[]).forEach(w=>{const b=document.createElement('button');b.type='button';b.className='escclave';
   b.innerHTML='🔊 '+exEsc(w);b.onclick=()=>speak(w);$('.escclaves').appendChild(b);});
 // 2 · afspelen + globaal begrip
 $('.escplay').innerHTML='<button class="escbtn escbtn-play" type="button">▶ Escuchar</button>'+
   '<button class="escbtn escbtn-stop" type="button">↺ Otra vez</button>'+
   '<span class="desc escnota">Luister eerst één keer helemaal. Nog niet meelezen.</span>';
 let sonando=false;
 $('.escbtn-play').onclick=()=>{if(sonando){player.parar();sonando=false;}else{player.reproducir();sonando=true;}};
 $('.escbtn-stop').onclick=()=>{player.parar();sonando=false;player.reproducir();sonando=true;};
 function preguntaMC(cont,it,alContestar){
   const q=document.createElement('div');q.className='exq';
   q.innerHTML='<div class="qz">'+exFmt(it.q)+'</div><div class="exopts"></div><div class="exwhy" role="status" aria-live="polite"></div>';
   const opts=q.querySelector('.exopts'),why=q.querySelector('.exwhy');let cerrado=false;
   exSample(it.opts,it.opts.length).forEach(o=>{const b=document.createElement('button');b.className='exopt';b.type='button';b.textContent=o;
     b.onclick=()=>{if(cerrado)return;cerrado=true;const bien=o===it.ans;
       opts.querySelectorAll('.exopt').forEach(x=>{x.disabled=true;if(x.textContent===it.ans)x.classList.add('ok');});
       if(!bien)b.classList.add('no');
       why.className='exwhy show '+(bien?'g':'b');
       why.innerHTML=(bien?'<b>'+IC.bien+' correcto</b>':'<b>'+IC.mal+' no</b> → '+exEsc(it.ans))+(it.why?' · '+exEsc(it.why):'');
       alContestar&&alContestar(bien);};
     opts.appendChild(b);});
   cont.appendChild(q);}
 if(cfg.global)preguntaMC($('.escglob'),cfg.global,()=>{estado.glob=true;revisa();});
 // 3 · vijf detailvragen
 $('.escdet').innerHTML='<p class="desc">Luister opnieuw en let op de details (getallen, tijd, plaats, naam). <span class="escscore">Juist: <b class="okd">0</b>/'+det.length+'</span></p>';
 let okd=0;
 det.forEach(it=>preguntaMC($('.escdet'),it,bien=>{if(bien){okd++;$('.okd').textContent=okd;}estado.det++;revisa();}));
 // 4 · juist/fout met bewijs uit het fragment
 vf.forEach((it,i)=>{const q=document.createElement('div');q.className='exq';
   q.innerHTML='<div class="qz"><span class="tynum">'+(i+1)+'</span><span>'+exFmt(it.q)+'</span></div>'+
     '<div class="exopts"><button class="exopt" type="button">Verdadero</button><button class="exopt" type="button">Falso</button></div>'+
     '<div class="escprueba" hidden><label>Bewijs uit het fragment: <input type="text" class="tyfield escpr" autocomplete="off" aria-label="Bewijs bij stelling '+(i+1)+'"></label><button class="otra escprbtn" type="button">'+IC.check+' Comprobar prueba</button></div>'+
     '<div class="exwhy" role="status" aria-live="polite"></div>';
   const opts=q.querySelector('.exopts'),why=q.querySelector('.exwhy'),pr=q.querySelector('.escprueba');
   let cerrado=false;
   opts.querySelectorAll('.exopt').forEach(b=>{b.onclick=()=>{if(cerrado)return;cerrado=true;
     const dicho=b.textContent==='Verdadero',bien=dicho===!!it.ans;
     opts.querySelectorAll('.exopt').forEach(x=>{x.disabled=true;
       if((x.textContent==='Verdadero')===!!it.ans)x.classList.add('ok');});
     if(!bien)b.classList.add('no');
     why.className='exwhy show '+(bien?'g':'b');
     why.innerHTML=(bien?'<b>'+IC.bien+' correcto</b>':'<b>'+IC.mal+' no</b> → '+(it.ans?'verdadero':'falso'))+' · Schrijf nu wáár je dat hoort.';
     pr.hidden=false;};});
   q.querySelector('.escprbtn').onclick=()=>{const v=q.querySelector('.escpr').value.trim();
     const a=tyNorm(v,'soft'),b=tyNorm(it.prueba||'','soft');
     const bien=a.length>2&&(b.indexOf(a)>-1||a.indexOf(b)>-1);
     why.className='exwhy show '+(bien?'g':'b');
     why.innerHTML=bien?'<b>✓ buena prueba</b> · «'+exEsc(it.prueba)+'»':'<b>'+IC.mal+' esa prueba no está</b> · en el fragment: «'+exEsc(it.prueba)+'»';
     q.querySelector('.escprbtn').disabled=true;q.querySelector('.escpr').disabled=true;
     estado.vf++;revisa();};
   $('.escvf').appendChild(q);});
 // 5 · transcript, pas ná de taken
 $('.esctr').innerHTML='<p class="desc esctrslot">Het transcript blijft dicht tot je de taken hierboven hebt gedaan — anders lees je mee in plaats van te luisteren.</p><button class="escbtn esctrbtn" type="button" disabled>🔒 Ver transcripción</button><div class="esctrbody" hidden></div>';
 function revisa(){const listo=(!cfg.global||estado.glob)&&estado.det>=det.length&&estado.vf>=vf.length;
   const b=$('.esctrbtn');if(!b)return;
   b.disabled=!listo;b.textContent=listo?IC.doc+' Ver transcripción':IC.lock+' Ver transcripción';
   if(listo)$('.esctrslot').textContent='Klaar — nu mag je meelezen. Klik een regel om ze opnieuw te horen.';}
 revisa();
 $('.esctrbtn').onclick=()=>{const body=$('.esctrbody');
   if(!body.dataset.hecho){body.dataset.hecho='1';
     G.forEach((g,i)=>{const r=document.createElement('div');r.className='esctrl';
       r.innerHTML='<button class="esctrsay" type="button" aria-label="Regel '+(i+1)+' opnieuw horen">'+IC.sound+'</button>'+
         '<div><b class="esctrwho">'+exEsc(g.who||'')+'</b><span class="esctres">'+exEsc(g.es)+'</span>'+
         (g.nl?'<span class="esctrnl">'+exEsc(g.nl)+'</span>':'')+'</div>';
       r.querySelector('.esctrsay').onclick=()=>player.linea(i);body.appendChild(r);});
     body.insertAdjacentHTML('afterbegin','<button class="otra esctrnlbtn" type="button">🇳🇱 vertaling aan/uit</button>');
     body.querySelector('.esctrnlbtn').onclick=()=>body.classList.toggle('sinnl');}
   body.hidden=!body.hidden;};
 // 6 · productieve reactie
 const P=cfg.produccion||{};
 $('.escprod').innerHTML='<p class="desc">'+exEsc(P.prompt||'Reageer op het fragment.')+'</p>'+
   (P.modo==='grabar'?'<div id="'+id+'_rec"></div>':'<textarea class="escta" rows="4" aria-label="Jouw reactie op het fragment"></textarea><p class="desc escconteo">0 palabras</p>');
 const ta=$('.escta');
 if(ta)ta.addEventListener('input',()=>{const n=ta.value.trim()?ta.value.trim().split(/\s+/).length:0;
   $('.escconteo').textContent=n+' palabra'+(n===1?'':'s')+(P.min?' · mínimo '+P.min:'');});
 if(P.modo==='grabar'&&typeof makeRecorder==='function')
   makeRecorder(id+'_rec',{title:'Tu respuesta hablada',desc:P.prompt||'',items:[{text:P.prompt||'',cue:'graba tu respuesta'}]});
}
// ── buildAudioCortos — de korte audiotaken van dezelfde unit ────────────────
// Het grote luisterblok hierboven is één fragment met zes treden. Daarnaast
// heeft elke unit kortere audiotaken (microdictado, klankreeks, mini-dialoog,
// weerbericht, wegbeschrijving) die in print als QR-kaart staan. Die krijgen
// hier hun speler en hun transcript.
//
// Dezelfde afspraak als bij het grote blok: het transcript blijft dicht tot de
// leerling twee keer geluisterd heeft. Meelezen bij de eerste beurt is geen
// luisteren meer. De antwoordsleutel staat hier NIET — die hoort in het
// docentendossier (CLAUDE.md 14).
//
// Het blok maakt zijn eigen kaart aan, direct na het grote luisterblok, zodat
// de unit-generatoren geen extra container in hun HTML nodig hebben.
function buildAudioCortos(idEscucha,cfg){
 const ancla=document.getElementById(idEscucha);if(!ancla)return;
 const frags=(cfg.fragmentos||[]).filter(f=>f.guion&&f.guion.length);
 if(!frags.length)return;
 const caja=document.createElement('div');
 caja.className='card ex audcortos';caja.id=idEscucha+'_cortos';
 caja.innerHTML='<div class="exhead"><h3>🎧 Los otros audios de la unidad</h3>'+
   '<span class="escfuente">'+frags.length+(frags.length===1?' fragmento':' fragmentos')+'</span></div>'+
   '<p class="desc">De korte audiotaken uit het boek — dezelfde die op papier achter een QR-code staan. '+
   'Luister <b>twee keer</b> voor je het transcript opent.</p><div class="audlista"></div>';
 ancla.parentNode.insertBefore(caja,ancla.nextSibling);
 const lista=caja.querySelector('.audlista');
 frags.forEach((f,n)=>{
   const it=document.createElement('div');it.className='audit';
   // stabiel anker: de QR-code in het boek wijst hierheen (#c5-u0-aud-03)
   if(f.ancla)it.id=f.ancla;
   const idt=idEscucha+'_c'+n;
   it.innerHTML=
     '<div class="audcab"><span class="audet">'+exEsc(f.etiqueta||'')+'</span>'+
       '<span class="audsec">'+exEsc(f.seccion||'')+'</span></div>'+
     '<h4>'+exEsc(f.titulo||'')+'</h4>'+
     '<p class="desc audtarea">'+exEsc(f.tarea||'')+'</p>'+
     '<div class="escplay">'+
       '<button class="escbtn audplay" type="button">▶ Escuchar</button>'+
       '<button class="escbtn escbtn-stop audotra" type="button">↺ Otra vez</button>'+
       '<span class="escfuente audfuente" role="status" aria-live="polite"></span>'+
       '<span class="desc audveces">0 × geluisterd</span>'+
     '</div>'+
     '<button class="escbtn esctrbtn audtr" type="button" disabled '+
       'aria-controls="'+idt+'_tr">🔒 Ver transcripción</button>'+
     '<div class="esctrbody" id="'+idt+'_tr" hidden></div>';
   lista.appendChild(it);
   const q=s=>it.querySelector(s);
   const fuente=q('.audfuente'),btn=q('.audplay'),tr=q('.audtr'),body=q('#'+idt+'_tr');
   let veces=0,sonando=false;
   const player=escReproductor(f,(modo,activo)=>{
     fuente.textContent=modo==='mp3'?'audio grabado':'voz del navegador';
     btn.textContent=activo?'⏹ Parar':'▶ Escuchar';
     if(!activo)sonando=false;});
   fuente.textContent='voz del navegador';
   function cuenta(){veces++;q('.audveces').textContent=veces+' × geluisterd';
     if(veces>=2){tr.disabled=false;tr.textContent=IC.doc+' Ver transcripción';}}
   btn.onclick=()=>{if(sonando){player.parar();sonando=false;}
     else{player.reproducir();sonando=true;cuenta();}};
   q('.audotra').onclick=()=>{player.parar();player.reproducir();sonando=true;cuenta();};
   tr.onclick=()=>{
     if(!body.dataset.hecho){body.dataset.hecho='1';
       f.guion.forEach((g,i)=>{const r=document.createElement('div');r.className='esctrl';
         r.innerHTML='<button class="esctrsay" type="button" aria-label="Regel '+(i+1)+' opnieuw horen">'+IC.sound+'</button>'+
           '<div><b class="esctrwho">'+exEsc(g.who||'')+'</b><span class="esctres">'+exEsc(g.es)+'</span>'+
           (g.nl?'<span class="esctrnl">'+exEsc(g.nl)+'</span>':'')+'</div>';
         r.querySelector('.esctrsay').onclick=()=>player.linea(i);body.appendChild(r);});
       body.insertAdjacentHTML('afterbegin','<button class="otra audnlbtn" type="button">🇳🇱 vertaling aan/uit</button>');
       body.querySelector('.audnlbtn').onclick=()=>body.classList.toggle('sinnl');}
     body.hidden=!body.hidden;};
 });
}
"""

ESCUCHA_CSS = r"""
.escfuente{font-size:11px;font-weight:700;color:var(--gd);background:var(--gt);border-radius:999px;padding:3px 9px;white-space:nowrap}
.escladder{list-style:none;margin:0;padding:0;counter-reset:esc}
.escpaso{border-left:3px solid var(--gt);padding:2px 0 2px 14px;margin:0 0 18px}
.escpaso h4{font-family:var(--disp);font-size:15px;margin:0 0 8px;color:var(--gd)}
.escficha{background:var(--gt);border-radius:12px;padding:11px 14px}
.escficha p{margin:2px 0;font-size:14px}
.escclaves{display:flex;gap:8px;flex-wrap:wrap}
.escclave{border:1.5px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:6px 13px;cursor:pointer;font-size:14px;font-weight:600;font-family:var(--body)}
.escplay{display:flex;gap:9px;align-items:center;flex-wrap:wrap;margin-bottom:10px}
.escbtn{border:none;background:var(--g);color:#fff;border-radius:10px;padding:9px 16px;font-weight:700;cursor:pointer;font-family:var(--disp);font-size:14px}
.escbtn-stop{background:var(--gt);color:var(--gd)}
.escbtn[disabled]{opacity:.55;cursor:default}
.escnota{margin:0}
.escscore{color:var(--mut)}.escscore b{color:var(--gd)}
.escprueba{margin-top:9px;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.escprueba label{display:flex;gap:7px;align-items:center;flex:1 1 220px;min-width:0;font-size:13px;color:var(--mut)}
.esctrbody{margin-top:10px;border:1px solid var(--line);border-radius:12px;padding:9px 11px;background:var(--card)}
.esctrl{display:flex;gap:9px;align-items:flex-start;padding:6px 0;border-bottom:1px solid var(--gt)}
.esctrl:last-child{border-bottom:none}
.esctrsay{border:none;background:var(--gt);color:var(--gd);border-radius:8px;padding:4px 8px;cursor:pointer;flex:none}
.esctrwho{display:block;font-size:11px;color:var(--gd);letter-spacing:.05em;text-transform:uppercase}
.esctres{display:block;font-size:15px}
.esctrnl{display:block;font-size:13px;color:var(--mut);font-style:italic}
.esctrbody.sinnl .esctrnl{display:none}
.escta{width:100%;max-width:100%;box-sizing:border-box;border:1.5px solid var(--line);border-radius:10px;padding:9px 11px;font-family:var(--body);font-size:15px;background:var(--card);color:var(--ink)}
.escta:focus-visible,.escbtn:focus-visible,.escclave:focus-visible,.esctrsay:focus-visible{outline:3px solid var(--gd);outline-offset:2px}
.escconteo{margin:4px 0 0}

/* ── de korte audiotaken van de unit (escucha_corta_data.py) ─────────────────
   Zelfde speler en transcript als het grote luisterblok, maar zonder de zes
   treden: dit zijn microdictados en mini-dialogen van 30-60 s. Het transcript
   gaat pas open na twee keer luisteren — anders leest de leerling mee. */
.audcortos{margin-top:16px}
.audit{border:1px solid var(--line);border-radius:14px;padding:12px 14px;margin:0 0 12px;background:var(--card)}
.audit:last-child{margin-bottom:0}
.audcab{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:5px}
.audet{font-size:11px;font-weight:700;color:#fff;background:var(--g);border-radius:999px;padding:3px 10px}
.audsec{font-size:11px;color:var(--mut);font-weight:600}
.audit h4{font-family:var(--disp);font-size:16px;margin:0 0 4px;color:var(--gd)}
.audtarea{margin:0 0 9px}
.audveces{color:var(--mut);font-size:12px}
.audtr{margin-top:2px}
"""


# ---------------------------------------------------------------------------
# buildLectura — leesblok volgens de route van CLAUDE.md 14bis
#
# De hubs hadden per unit wel een Lectura, maar meestal als «tekst + een paar
# meerkeuzevragen». De route eist meer, en vooral: scannen en bewijs.
#
#   voorspellen (vóór het lezen) -> globaal begrip -> scannen (getypt, want
#   informatie terugvinden is ophalen, niet herkennen) -> juist/fout MET BEWIJS
#   -> betekenis uit context -> productieve reactie.
#
# De tekst blijft de hele tijd zichtbaar: scannen zonder tekst is geheugenwerk,
# en dat is een andere vaardigheid dan lezen.
# ---------------------------------------------------------------------------
LECTURA_JS = r"""
function lecTexto(bloques){let h='';
 bloques.forEach(b=>{const soort=b[0],c=b[1];
  if(soort==='titulo')h+='<h4 class="lectitulo">'+exEsc(c)+'</h4>';
  else if(soort==='lema')h+='<p class="leclema">'+exEsc(c)+'</p>';
  else if(soort==='firma')h+='<p class="lecfirma">'+exEsc(c)+'</p>';
  else if(soort==='lista')h+='<ul class="leclista">'+c.map(x=>'<li>'+exEsc(x)+'</li>').join('')+'</ul>';
  else if(soort==='aviso')h+='<div class="lecaviso"><b>'+exEsc(c[0])+'</b><p>'+exEsc(c[1])+'</p></div>';
  else h+='<p>'+exEsc(c)+'</p>';});
 return h;}
function buildLectura(id,cfg){
 const host=document.getElementById(id);if(!host)return;
 const esc=cfg.escanear||[],vf=cfg.vf||[],ctx=cfg.contexto||[];
 host.innerHTML=
  '<div class="exhead"><h3>📄 '+cfg.titulo+'</h3><span class="lectipo">'+exEsc(cfg.tipo)+'</span></div>'+
  '<div class="lecficha"><span><b>Afzender</b> '+exEsc(cfg.emisor)+'</span><span><b>Ontvanger</b> '+exEsc(cfg.receptor)+'</span><span><b>Leesdoel</b> '+exEsc(cfg.objetivo)+'</span></div>'+
  '<ol class="escladder">'+
   '<li class="escpaso"><h4>1 · Antes de leer — predice</h4><div class="lecpred"></div></li>'+
   '<li class="escpaso"><h4>2 · El texto</h4><div class="lectexto">'+lecTexto(cfg.texto)+'</div>'+
     '<button class="otra lecnl" type="button">🇳🇱 vertaling aan/uit</button><div class="lectrad" hidden>'+exEsc(cfg.traduccion||'')+'</div></li>'+
   '<li class="escpaso"><h4>3 · Comprensión global</h4><div class="lecglob"></div></li>'+
   '<li class="escpaso"><h4>4 · Escanea — busca el dato</h4><div class="lecesc"></div></li>'+
   '<li class="escpaso"><h4>5 · Verdadero o falso — con prueba</h4><div class="lecvf"></div></li>'+
   '<li class="escpaso"><h4>6 · El significado por el contexto</h4><div class="lecctx"></div></li>'+
   '<li class="escpaso"><h4>7 · Tu reacción</h4><div class="lecprod"></div></li>'+
  '</ol>';
 const $=s=>host.querySelector(s);
 $('.lecnl').onclick=()=>{const t=$('.lectrad');t.hidden=!t.hidden;};
 function mc(cont,it){const q=document.createElement('div');q.className='exq';
   q.innerHTML='<div class="qz">'+exFmt(it.q)+'</div><div class="exopts"></div><div class="exwhy" role="status" aria-live="polite"></div>';
   const opts=q.querySelector('.exopts'),why=q.querySelector('.exwhy');let cerrado=false;
   exSample(it.opts,it.opts.length).forEach(o=>{const b=document.createElement('button');b.className='exopt';b.type='button';b.textContent=o;
     b.onclick=()=>{if(cerrado)return;cerrado=true;const bien=o===it.ans;
       opts.querySelectorAll('.exopt').forEach(x=>{x.disabled=true;if(x.textContent===it.ans)x.classList.add('ok');});
       if(!bien)b.classList.add('no');
       why.className='exwhy show '+(bien?'g':'b');
       why.innerHTML=(bien?'<b>'+IC.bien+' correcto</b>':'<b>'+IC.mal+' no</b> → '+exEsc(it.ans))+(it.why?' · '+exEsc(it.why):'');};
     opts.appendChild(b);});
   cont.appendChild(q);}
 if(cfg.prediccion)mc($('.lecpred'),cfg.prediccion);
 if(cfg.global)mc($('.lecglob'),cfg.global);
 ctx.forEach(it=>mc($('.lecctx'),it));
 // Scannen is getypt: het antwoord staat in de tekst, dus opzoeken en
 // overschrijven — geen keuzemenu waarin het antwoord al meekijkt.
 buildTypeEn($('.lecesc'),esc);
 function buildTypeEn(cont,items){
   cont.innerHTML='<p class="desc">Zoek het gegeven in de tekst en schrijf het op. <span class="escscore">Juist: <b class="oke">0</b>/'+items.length+'</span></p>';
   let ok=0;
   items.forEach((it,i)=>{const r=document.createElement('div');r.className='exq tyq';
     r.innerHTML='<div class="qz"><span class="tynum">'+(i+1)+'</span><span>'+exFmt(it.q)+'</span></div>'+
       '<div class="tyin"><input type="text" class="tyfield" autocomplete="off" aria-label="Scanvraag '+(i+1)+'"><button class="otra lecchk" type="button">✓</button></div>'+
       '<div class="exwhy" role="status" aria-live="polite"></div>';
     const inp=r.querySelector('.tyfield'),why=r.querySelector('.exwhy'),btn=r.querySelector('.lecchk');
     function comprueba(){if(inp.disabled)return;const v=inp.value.trim();
       const bien=v&&[it.ans].concat(it.alt||[]).some(a=>tyNorm(a,'soft')===tyNorm(v,'soft'));
       if(bien){ok++;cont.querySelector('.oke').textContent=ok;inp.disabled=true;btn.disabled=true;
         inp.classList.add('good');inp.setAttribute('aria-invalid','false');
         why.className='exwhy show g';why.innerHTML='<b>'+IC.bien+' correcto</b>'+(it.why?' · '+exEsc(it.why):'');}
       else{inp.classList.add('bad');inp.setAttribute('aria-invalid','true');
         why.className='exwhy show b';why.innerHTML='<b>✗ todavía no</b> · zoek nog eens in de tekst';}}
     btn.onclick=comprueba;
     inp.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();comprueba();}});
     cont.appendChild(r);});}
 vf.forEach((it,i)=>{const q=document.createElement('div');q.className='exq';
   q.innerHTML='<div class="qz"><span class="tynum">'+(i+1)+'</span><span>'+exFmt(it.q)+'</span></div>'+
     '<div class="exopts"><button class="exopt" type="button">Verdadero</button><button class="exopt" type="button">Falso</button></div>'+
     '<div class="escprueba" hidden><label>Bewijs uit de tekst: <input type="text" class="tyfield lecpr" autocomplete="off" aria-label="Bewijs bij stelling '+(i+1)+'"></label><button class="otra lecprbtn" type="button">'+IC.check+' Comprobar prueba</button></div>'+
     '<div class="exwhy" role="status" aria-live="polite"></div>';
   const opts=q.querySelector('.exopts'),why=q.querySelector('.exwhy'),pr=q.querySelector('.escprueba');let cerrado=false;
   opts.querySelectorAll('.exopt').forEach(b=>{b.onclick=()=>{if(cerrado)return;cerrado=true;
     const bien=(b.textContent==='Verdadero')===!!it.ans;
     opts.querySelectorAll('.exopt').forEach(x=>{x.disabled=true;if((x.textContent==='Verdadero')===!!it.ans)x.classList.add('ok');});
     if(!bien)b.classList.add('no');
     why.className='exwhy show '+(bien?'g':'b');
     why.innerHTML=(bien?'<b>'+IC.bien+' correcto</b>':'<b>'+IC.mal+' no</b> → '+(it.ans?'verdadero':'falso'))+' · Kopieer nu de zin die het bewijst.';
     pr.hidden=false;};});
   q.querySelector('.lecprbtn').onclick=()=>{const v=q.querySelector('.lecpr').value.trim();
     const a=tyNorm(v,'soft'),b=tyNorm(it.prueba,'soft');
     const bien=a.length>2&&(b.indexOf(a)>-1||a.indexOf(b)>-1);
     why.className='exwhy show '+(bien?'g':'b');
     why.innerHTML=bien?'<b>✓ buena prueba</b> · «'+exEsc(it.prueba)+'»':'<b>'+IC.mal+' esa prueba no está</b> · en el texto: «'+exEsc(it.prueba)+'»';
     q.querySelector('.lecprbtn').disabled=true;q.querySelector('.lecpr').disabled=true;};
   $('.lecvf').appendChild(q);});
 const P=cfg.produccion||{};
 $('.lecprod').innerHTML='<p class="desc">'+exEsc(P.prompt||'')+'</p>'+
   '<textarea class="escta" rows="5" aria-label="Jouw geschreven reactie"></textarea>'+
   '<p class="desc escconteo">0 palabras</p>'+
   (P.modelo?'<button class="otra lecmod" type="button">👁 Ver modelo</button><p class="lecmodelo" hidden>'+exEsc(P.modelo)+'</p>':'');
 const ta=$('.escta');
 if(ta)ta.addEventListener('input',()=>{const n=ta.value.trim()?ta.value.trim().split(/\s+/).length:0;
   $('.escconteo').textContent=n+' palabra'+(n===1?'':'s');});
 const bm=$('.lecmod');
 if(bm)bm.onclick=()=>{const m=$('.lecmodelo');m.hidden=!m.hidden;};

}
"""

LECTURA_CSS = r"""
.lectipo{font-size:11px;font-weight:700;color:var(--gd);background:var(--gt);border-radius:999px;padding:3px 9px}
.lecficha{display:flex;gap:14px;flex-wrap:wrap;background:var(--gt);border-radius:10px;padding:8px 12px;margin:8px 0 14px;font-size:12px}
.lecficha b{display:block;font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--gd)}
.lectexto{border:1px solid var(--line);border-left:4px solid var(--g);border-radius:12px;padding:14px 17px;background:var(--card)}
.lectitulo{font-family:var(--disp);color:var(--gd);margin:0 0 4px;font-size:17px}
.leclema{font-family:var(--hand,inherit);color:var(--mut);margin:0 0 10px}
.leclista{margin:8px 0;padding-left:20px}
.leclista li{margin:3px 0}
.lecaviso{border:1px dashed var(--line);border-radius:10px;padding:9px 12px;margin:9px 0;background:var(--gt)}
.lecaviso p{margin:4px 0 0}
.lecfirma{font-size:13px;color:var(--mut);margin:10px 0 0}
.lectrad{font-size:13px;color:var(--mut);font-style:italic;margin-top:9px;border-left:3px solid var(--line);padding-left:10px}
.lecmodelo{font-size:13px;background:var(--gt);color:var(--gd);border-radius:9px;padding:8px 11px;margin-top:8px}
.lecchk{flex:none}
"""


# ---------------------------------------------------------------------------
# buildRetos — de out-of-the-box oefeningen op de hub
#
# Niet elke reto hoort hier. Een veiling en een bewegingsspel leven op het grote
# scherm, een info-gap op papier; die krijgen in print en hub alleen een
# verwijzing. Hier staan de vier die techniek nodig hebben: opnemen en
# terugluisteren, directe zelfcorrectie, en een kaart die meekleurt.
#
# Drie soorten lichaam, gekozen op `tipo`:
#   grabar    -> makeRecorder met één item per situatie
#   detector  -> zelfcorrectie waarbij je niet alleen aanduidt maar ook de
#                regel moet kiezen; aanduiden zonder regel telt als fout
#   mapa      -> haakt in op de bestaande wereldkaart en houdt een klasteller bij
#
# De antwoordsleutel komt hier NIET binnen (CLAUDE.md §14); wat de leerling ziet
# is feedback per item, geen lijst met oplossingen.
# ---------------------------------------------------------------------------
RETOS_CSS = r"""
.retos{display:grid;gap:16px}
.reto{border:1px solid var(--line);border-radius:16px;padding:16px 18px;background:var(--card)}
.reto .rcab{display:flex;gap:9px;align-items:center;flex-wrap:wrap;margin-bottom:4px}
.reto .rnum{background:var(--g);color:#fff;font-family:var(--disp);font-weight:700;
  width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none}
.reto h3{margin:0;font-family:var(--disp);font-size:19px;color:var(--gd)}
.reto .rlente{font-size:11px;font-weight:700;color:var(--gd);background:var(--gt);
  border-radius:999px;padding:3px 9px}
.reto .rgancho{margin:2px 0 0;font-size:15px}
.reto .rnl{margin:2px 0 10px;font-size:13px;color:var(--mut);font-style:italic}
.rregla{border-left:4px solid var(--amber,#B7860B);background:var(--amberbg,#FBF3D6);
  border-radius:0 10px 10px 0;padding:9px 13px;margin:0 0 12px;font-size:13.5px;color:#20242E}
.rregla b{display:block;font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:#8A6508}
.rsit{border:1px solid var(--line);border-radius:12px;padding:10px 12px;margin:0 0 10px}
.rsit b{color:var(--gd)}
.rsit .rpista{display:block;font-size:12.5px;color:var(--mut);margin-top:3px}
.det{display:grid;gap:8px}
.detit{border:1px solid var(--line);border-radius:12px;padding:9px 12px}
.detit .dpal{font-family:var(--disp);font-size:18px}
.detbtns{display:flex;gap:8px;margin:6px 0}
.detbtn{border:1.5px solid var(--line);background:var(--card);color:var(--ink);border-radius:9px;
  padding:6px 13px;cursor:pointer;font-weight:600;font-size:14px}
.detbtn.ok{background:#DCFCE7;border-color:#16A34A}.detbtn.no{background:#FEE2E2;border-color:#DC2626}
.detrule{margin-top:6px}
.detrule select{width:100%;max-width:100%;border:1.5px solid var(--line);border-radius:9px;
  padding:7px 9px;font-family:var(--body);font-size:14px;background:var(--card);color:var(--ink)}
.detfb{margin-top:6px;font-size:13.5px;display:none}
.detfb.show{display:block}.detfb.g{color:#166534}.detfb.b{color:#991B1B}
.rmarca{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin:0 0 10px}
.rbarra{flex:1 1 200px;height:12px;border-radius:999px;background:var(--gt);overflow:hidden;min-width:160px}
.rbarra i{display:block;height:100%;width:0;background:var(--g);transition:width .4s}
.rcuenta{font-family:var(--disp);font-weight:700;color:var(--gd)}
.rpais{display:flex;flex-wrap:wrap;gap:6px}
.rpais button{border:1.5px solid var(--line);background:var(--card);color:var(--ink);
  border-radius:999px;padding:5px 11px;cursor:pointer;font-size:13.5px}
.rpais button.hecho{background:var(--g);border-color:var(--g);color:#fff}
.rpais button .sil{font-size:11px;opacity:.8;margin-left:5px}
.escenas{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:640px){.escenas{grid-template-columns:1fr}}
.esc{margin:0;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:var(--card)}
.esc figcaption{padding:8px 12px;font-size:13px;background:var(--gt);color:var(--gd)}
.esc figcaption b{font-family:var(--disp);font-size:15px;margin-right:6px}
.esc svg{display:block;width:100%;height:auto}
.escnom{margin:0;padding:8px 12px;font-size:14px;border-top:1px solid var(--line);min-height:38px}
.retratos{display:grid;grid-template-columns:repeat(6,1fr);gap:10px}
@media(max-width:640px){.retratos{grid-template-columns:repeat(3,1fr)}}
.retrato{position:relative;border:2px solid var(--line);border-radius:12px;background:var(--card);
  cursor:pointer;padding:4px}
.retrato svg{width:100%;height:auto;display:block}
.retrato.ok{border-color:#16A34A;background:#DCFCE7}.retrato.no{border-color:#DC2626;background:#FEE2E2}
.rnum2{position:absolute;top:4px;left:6px;font-family:var(--disp);font-weight:700;color:var(--gd);font-size:13px}
.rtanteo{color:var(--mut)}
.voces{display:grid;gap:9px;margin-bottom:10px}
.voz{display:flex;gap:10px;align-items:flex-start;border:1px solid var(--line);border-radius:12px;padding:9px 11px}
.voz b{color:var(--gd);display:block;font-size:13px}
.vozt{font-size:14px}
.opplay{margin-bottom:6px}
"""

RETOS_JS = r"""
function buildRetos(id,cfg){
 const host=document.getElementById(id);if(!host)return;
 host.innerHTML='<div class="retos"></div>';
 const lista=host.querySelector('.retos');
 (cfg.retos||[]).forEach((r,n)=>{
  const c=document.createElement('div');c.className='reto';
  // stabiel anker voor de verwijzing vanuit boek en PowerPoint (#reto-c5-u5-01)
  if(r.ancla)c.id=r.ancla;
  c.innerHTML='<div class="rcab"><span class="rnum">'+r.num+'</span><h3>'+exEsc(r.nombre)+'</h3>'+
    '<span class="rlente">'+exEsc(r.lente)+'</span></div>'+
    '<p class="rgancho"><b>'+exEsc(r.gancho_es)+'</b></p>'+
    '<p class="rnl">'+exEsc(r.gancho_nl)+'</p>'+
    '<p class="desc">'+exEsc(r.consigna_nl)+'</p>'+
    '<div class="rregla"><b>La regla del reto</b>'+exEsc(r.regla)+'</div>'+
    '<div class="rcuerpo" id="'+id+'_c'+n+'"></div>';
  lista.appendChild(c);
  const cuerpo=c.querySelector('.rcuerpo');
  if(r.tipo==='grabar')retoGrabar(cuerpo,r,id+'_c'+n);
  else if(r.tipo==='detector')retoDetector(cuerpo,r);
  else if(r.tipo==='mapa')retoMapa(cuerpo,r);
  else if(r.tipo==='articulo')retoArticulo(cuerpo,r);
  else if(r.tipo==='escena')retoEscena(cuerpo,r);
  else if(r.tipo==='retrato')retoRetrato(cuerpo,r);
  else if(r.tipo==='voces')retoVoces(cuerpo,r);
  else if(r.tipo==='opciones')retoOpciones(cuerpo,r);
 });
}

function retoGrabar(cont,r,idBase){
 (r.situaciones||[]).forEach(s=>{
   const d=document.createElement('div');d.className='rsit';
   d.innerHTML='<b>'+exEsc(s.es)+'</b><span class="rpista">'+exEsc(s.nl)+
     (s.pista?' · <i>'+exEsc(s.pista)+'</i>':'')+'</span>';
   cont.appendChild(d);});
 const rec=document.createElement('div');rec.id=idBase+'_rec';cont.appendChild(rec);
 if(typeof makeRecorder==='function')
   makeRecorder(idBase+'_rec',{title:r.nombre,desc:r.consigna_es,
     items:(r.items||[]).map(t=>({text:t.text,cue:t.cue}))});
}

function retoDetector(cont,r){
 const caja=document.createElement('div');caja.className='det';cont.appendChild(caja);
 const reglas=r.reglas||[];
 (r.items||[]).forEach((it,i)=>{
   const d=document.createElement('div');d.className='detit';
   const opts=reglas.map((g,k)=>'<option value="'+k+'">'+exEsc(g)+'</option>').join('');
   d.innerHTML='<div class="dpal">'+exEsc(it.palabra)+'</div>'+
     '<div class="detbtns"><button class="detbtn" type="button" data-v="1">✓ posible</button>'+
     '<button class="detbtn" type="button" data-v="0">✗ imposible</button></div>'+
     '<div class="detrule" hidden><label class="desc">¿Qué regla rompe?</label>'+
     '<select><option value="-1">— elige la regla —</option>'+opts+'</select></div>'+
     '<div class="detfb" role="status" aria-live="polite"></div>';
   const fb=d.querySelector('.detfb'),rule=d.querySelector('.detrule'),sel=d.querySelector('select');
   let cerrado=false;
   d.querySelectorAll('.detbtn').forEach(b=>{b.onclick=()=>{
     if(cerrado)return;
     const dicho=b.dataset.v==='1';
     if(!dicho){rule.hidden=false;sel.focus();
       fb.className='detfb show';fb.textContent='Ahora acusa con pruebas: ¿qué regla rompe?';
       cerrado=false;
       sel.onchange=()=>{cerrado=true;
         const bien=(!it.posible)&&(Number(sel.value)===it.regla);
         d.querySelectorAll('.detbtn').forEach(x=>x.disabled=true);sel.disabled=true;
         b.classList.add(bien?'ok':'no');
         fb.className='detfb show '+(bien?'g':'b');
         fb.innerHTML=bien?'<b>✓ acusación correcta</b> · '+exEsc(it.porque)
           :(it.posible?'<b>✗ esta palabra sí existe</b> · '+exEsc(it.porque)
                       :'<b>✗ la regla no es esa</b> · '+exEsc(it.porque));};
       return;}
     cerrado=true;
     const bien=it.posible;
     d.querySelectorAll('.detbtn').forEach(x=>x.disabled=true);
     b.classList.add(bien?'ok':'no');
     fb.className='detfb show '+(bien?'g':'b');
     fb.innerHTML=(bien?'<b>✓ correcto</b> · ':'<b>✗ no</b> · ')+exEsc(it.porque);};});
   caja.appendChild(d);});
}

// ── artículo: el/la op verzonnen woorden ───────────────────────────────────
// Het lidwoord alléén zegt niets: wie «la» kiest bij een -ma-woord heeft geraden,
// ook als het toevallig klopt. Daarom moet de leerling er de regel bij kiezen, en
// telt het pas als het allebei klopt.
// ── retrato hablado: luister en kies het juiste portret ────────────────────
// De portretten worden getekend, niet beschreven: stonden de kenmerken in
// woorden op de kaart, dan werd het woorden matchen in plaats van luisteren.
function retoCara(x,y,r,p){
 const pelo = p.pelo.indexOf('largo')>=0
   ? (p.pelo.indexOf('rizado')>=0
      ? '<path d="M'+(x-r-4)+' '+(y+r+6)+' q-6,-'+(r+18)+' '+(r+6)+',-'+(r+14)+' q'+r+',-8 '+(r+6)+','+(r+14)+' q6,'+(r+8)+' -4,'+(r+2)+' q-'+r+',-14 -'+(2*r-4)+',0 Z" fill="#5C4433"/>'
      : '<path d="M'+(x-r-2)+' '+(y+r+8)+' l0,-'+(r+16)+' q'+(r+2)+',-14 '+(2*r+4)+',0 l0,'+(r+16)+' l-8,0 l0,-'+r+' q-'+r+',-10 -'+(2*r-8)+',0 l0,'+r+' Z" fill="#5C4433"/>')
   : (p.pelo.indexOf('rizado')>=0
      ? '<path d="M'+(x-r-2)+' '+y+' q2,-'+(r+14)+' '+(r+2)+',-'+(r+10)+' q'+r+',-6 '+(r+2)+','+(r+10)+' q2,10 -6,6 q-'+r+',-14 -'+(2*r-8)+',0 q-8,4 -6,-6 Z" fill="#5C4433"/>'
      : '<path d="M'+(x-r-2)+' '+(y-2)+' q0,-'+(r+12)+' '+(r+2)+',-'+(r+12)+' q'+(r+2)+',0 '+(r+2)+','+(r+12)+' l-6,2 q-'+r+',-12 -'+(2*r-4)+',0 Z" fill="#5C4433"/>');
 const gafas = p.gafas
   ? '<g fill="none" stroke="#20242E" stroke-width="2.4"><circle cx="'+(x-r/2.4)+'" cy="'+(y+2)+'" r="'+(r/3.4)+'"/>'
     +'<circle cx="'+(x+r/2.4)+'" cy="'+(y+2)+'" r="'+(r/3.4)+'"/>'
     +'<line x1="'+(x-r/2.4+r/3.4)+'" y1="'+(y+2)+'" x2="'+(x+r/2.4-r/3.4)+'" y2="'+(y+2)+'"/></g>'
   : '<circle cx="'+(x-r/2.4)+'" cy="'+(y+1)+'" r="2.6" fill="#20242E"/>'
     +'<circle cx="'+(x+r/2.4)+'" cy="'+(y+1)+'" r="2.6" fill="#20242E"/>';
 const boca = p.sonrie
   ? '<path d="M'+(x-r/2.6)+' '+(y+r/2.2)+' q'+(r/2.6)+','+(r/3.2)+' '+(r/1.3)+',0" stroke="#20242E" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
   : '<line x1="'+(x-r/3)+'" y1="'+(y+r/1.9)+'" x2="'+(x+r/3)+'" y2="'+(y+r/1.9)+'" stroke="#20242E" stroke-width="2.4" stroke-linecap="round"/>';
 return '<circle cx="'+x+'" cy="'+y+'" r="'+r+'" fill="#F2D3B6"/>'+pelo+gafas+boca;
}

function retoRetrato(cont,r){
 const rs=r.retratos||[], ds=r.descripciones||[];
 let i=0, aciertos=0;
 cont.innerHTML='<div class="rmarca"><button class="escbtn rplay" type="button">▶ Escuchar la descripción</button>'+
   '<span class="rcuenta rvuelta">1 / '+ds.length+'</span>'+
   '<span class="desc rtanteo">aciertos: 0</span></div>'+
   '<div class="retratos"></div><div class="detfb rfb" role="status" aria-live="polite"></div>';
 const caja=cont.querySelector('.retratos');
 rs.forEach(p=>{
   const b=document.createElement('button');b.type='button';b.className='retrato';b.dataset.n=p.n;
   b.innerHTML='<svg viewBox="0 0 100 100" aria-hidden="true">'+retoCara(50,52,26,p)+'</svg>'+
     '<span class="rnum2">'+p.n+'</span>';
   b.onclick=()=>{
     if(!ds[i])return;
     const fb=cont.querySelector('.rfb'), bien=Number(b.dataset.n)===ds[i].correcto;
     b.classList.add(bien?'ok':'no');
     fb.className='detfb show rfb '+(bien?'g':'b');
     fb.innerHTML=bien?'<b>✓ correcto</b> · '+exEsc(ds[i].texto)
       :'<b>✗ no</b> · era el '+ds[i].correcto+' — '+exEsc(ds[i].texto);
     if(bien)aciertos++;
     cont.querySelector('.rtanteo').textContent='aciertos: '+aciertos;
     i++;
     setTimeout(()=>{caja.querySelectorAll('.retrato').forEach(x=>x.classList.remove('ok','no'));
       if(i<ds.length){cont.querySelector('.rvuelta').textContent=(i+1)+' / '+ds.length;fb.className='detfb rfb';}
       else{cont.querySelector('.rvuelta').textContent='hecho';
         fb.className='detfb show rfb g';fb.innerHTML='<b>Listo</b> · ahora describe tú uno a tu compañero/a.';}},1400);};
   caja.appendChild(b);});
 cont.querySelector('.rplay').onclick=()=>{if(ds[i]&&typeof speak==='function')speak(ds[i].texto);};
}

// ── drie stemmen, één samenvatting: bemiddelen ─────────────────────────────
// ── opciones: kies uit N, mét verplichte uitleg ────────────────────────────
// Breed inzetbaar: welk werkwoord past bij dit uur, welke Spaanse uitdrukking
// dekt deze Vlaamse. Er is telkens één juist antwoord, en de feedback zegt niet
// alleen wát maar ook waarom — anders leert een gokker niets.
function retoOpciones(cont,r){
 const caja=document.createElement('div');caja.className='det';cont.appendChild(caja);
 (r.items||[]).forEach(it=>{
   const d=document.createElement('div');d.className='detit';
   d.innerHTML=(it.audio?'<button class="escbtn opplay" type="button">▶ Escuchar</button>':'')+
     '<div class="dpal">'+exEsc(it.enunciado)+'</div>'+
     '<div class="detbtns"></div>'+
     '<div class="detfb" role="status" aria-live="polite"></div>';
   const btns=d.querySelector('.detbtns'), fb=d.querySelector('.detfb');
   let cerrado=false;
   (it.opciones||[]).forEach(o=>{
     const b=document.createElement('button');b.type='button';b.className='detbtn';b.textContent=o;
     b.onclick=()=>{if(cerrado)return;cerrado=true;
       const bien=o===it.correcta;
       btns.querySelectorAll('.detbtn').forEach(x=>{x.disabled=true;
         if(x.textContent===it.correcta)x.classList.add('ok');});
       if(!bien)b.classList.add('no');
       fb.className='detfb show '+(bien?'g':'b');
       fb.innerHTML=(bien?'<b>'+IC.bien+' correcto</b>':'<b>✗ es «'+exEsc(it.correcta)+'»</b>')+
         (it.porque?' · '+exEsc(it.porque):'');};
     btns.appendChild(b);});
   const pl=d.querySelector('.opplay');
   if(pl)pl.onclick=()=>{if(typeof speak==='function')speak(it.enunciado);};
   caja.appendChild(d);});
}

function retoVoces(cont,r){
 cont.innerHTML='<div class="voces"></div>'+
   '<p class="desc">Schrijf je samenvatting in drie zinnen — korter dan wat je hoorde, en niemand mag wegvallen.</p>'+
   '<textarea class="escta" rows="5" aria-label="Jouw samenvatting" placeholder="1. Rosa vindt…"></textarea>';
 const caja=cont.querySelector('.voces');
 (r.voces||[]).forEach(v=>{
   const d=document.createElement('div');d.className='voz';
   d.innerHTML='<button class="escbtn vozbtn" type="button">▶</button>'+
     '<div><b>'+exEsc(v.quien)+'</b><span class="vozt">'+exEsc(v.texto)+'</span></div>';
   d.querySelector('.vozbtn').onclick=()=>{if(typeof speak==='function')speak(v.texto);};
   caja.appendChild(d);});
}

function retoArticulo(cont,r){
 const caja=document.createElement('div');caja.className='det';cont.appendChild(caja);
 const reglas=r.reglas||[];
 (r.objetos||[]).forEach(it=>{
   const d=document.createElement('div');d.className='detit';
   const opts=reglas.map((g,k)=>'<option value="'+g.clave+'">'+exEsc(g.texto)+'</option>').join('');
   d.innerHTML='<div class="dpal">¿… '+exEsc(it.palabra)+'?</div>'+
     '<div class="detbtns"><button class="detbtn" type="button" data-a="el">el</button>'+
     '<button class="detbtn" type="button" data-a="la">la</button></div>'+
     '<div class="detrule" hidden><label class="desc">¿Qué regla usas?</label>'+
     '<select><option value="">— elige la regla —</option>'+opts+'</select></div>'+
     '<div class="detfb" role="status" aria-live="polite"></div>';
   const fb=d.querySelector('.detfb'),rule=d.querySelector('.detrule'),sel=d.querySelector('select');
   let elegido=null;
   d.querySelectorAll('.detbtn').forEach(b=>{b.onclick=()=>{
     if(elegido)return;
     elegido=b.dataset.a;rule.hidden=false;sel.focus();
     fb.className='detfb show';fb.textContent='¿Y por qué? Elige la regla.';};});
   sel.onchange=()=>{
     if(!sel.value)return;
     const bienArt=elegido===it.articulo, bienRegla=sel.value===it.regla;
     d.querySelectorAll('.detbtn').forEach(x=>x.disabled=true);sel.disabled=true;
     const b=d.querySelector('.detbtn[data-a="'+elegido+'"]');
     b.classList.add(bienArt&&bienRegla?'ok':'no');
     fb.className='detfb show '+(bienArt&&bienRegla?'g':'b');
     if(bienArt&&bienRegla)fb.innerHTML='<b>✓ correcto</b> · '+exEsc(it.porque);
     else if(bienArt)fb.innerHTML='<b>✗ el artículo sí, la regla no</b> · '+exEsc(it.porque)+
       ' — con la regla equivocada, has adivinado.';
     else fb.innerHTML='<b>✗ es «'+exEsc(it.articulo)+' '+exEsc(it.palabra)+'»</b> · '+exEsc(it.porque);};
   caja.appendChild(d);});
}

// ── escena: dezelfde plek, twee tijden ─────────────────────────────────────
// Twee panelen naast elkaar; klik een voorwerp en je hoort en ziet hoe het heet.
// De twee voorwerpen die in beide scènes staan, zijn de controle: wie die als
// verschil noteert, heeft te snel gekeken.
function retoEscena(cont,r){
 const items=r.escena||[];
 function panel(cual,titulo,sub){
   const propios=items.filter(i=>i.cuando===cual||i.cuando==='ambas');
   const formas=propios.map((i,k)=>i.forma==='circ'
     ? '<circle class="eob" data-k="'+k+'" data-c="'+cual+'" cx="'+(i.x+i.w/2)+'" cy="'+(i.y+i.h/2)+
       '" r="'+(i.w/2)+'" fill="'+i.color+'"/>'
     : '<rect class="eob" data-k="'+k+'" data-c="'+cual+'" x="'+i.x+'" y="'+i.y+'" width="'+i.w+
       '" height="'+i.h+'" rx="1.5" fill="'+i.color+'"/>').join('');
   return '<figure class="esc"><figcaption><b>'+exEsc(titulo)+'</b> <span>'+exEsc(sub)+'</span></figcaption>'+
     '<svg viewBox="0 0 100 84" role="img" aria-label="'+exEsc(titulo)+'">'+
     '<rect x="0" y="0" width="100" height="52" fill="#E8F1F7"/>'+          // lucht
     '<rect x="0" y="52" width="100" height="32" fill="#EDE7DC"/>'+          // plein
     '<rect x="0" y="30" width="100" height="22" fill="#D8CFC0"/>'+          // gevelrij
     '<rect x="6" y="24" width="16" height="28" fill="#C6B9A6"/>'+
     '<rect x="44" y="20" width="18" height="32" fill="#C6B9A6"/>'+
     '<rect x="76" y="26" width="18" height="26" fill="#C6B9A6"/>'+
     formas+'</svg><p class="escnom" role="status" aria-live="polite">Klik een voorwerp.</p></figure>';
 }
 cont.innerHTML='<div class="escenas">'+panel('antes','1985','la misma plaza, hace cuarenta años')+
   panel('ahora','ahora','la plaza hoy')+'</div>'+
   '<p class="desc">De twee dingen die in <b>allebei</b> de scènes staan, zijn de controle: die zijn géén verschil.</p>';
 cont.querySelectorAll('.eob').forEach(el=>{
   el.style.cursor='pointer';
   el.addEventListener('click',()=>{
     const cual=el.dataset.c, k=Number(el.dataset.k);
     const propios=items.filter(i=>i.cuando===cual||i.cuando==='ambas');
     const it=propios[k];if(!it)return;
     const fig=el.closest('figure');
     fig.querySelector('.escnom').innerHTML='<b>'+exEsc(it.es)+'</b> — '+exEsc(it.nl)+
       (it.cuando==='ambas'?' <i>(en las dos escenas)</i>':'');
     el.style.stroke='#157355';el.style.strokeWidth='1.4';
     if(typeof speak==='function')speak(it.es);});});
 const marco=document.createElement('div');marco.className='rsit';
 marco.innerHTML='<b>Tu marco</b><span class="rpista">'+
   (r.marco||[]).map(exEsc).join(' · ')+'</span>';
 cont.appendChild(marco);
 const ta=document.createElement('textarea');ta.className='escta';ta.rows=5;
 ta.setAttribute('aria-label','Jouw vijf zinnen');ta.placeholder='1. En la plaza de ahora hay…';
 cont.appendChild(ta);
}

function retoMapa(cont,r){
 const paises=r.paises||[];
 cont.innerHTML='<div class="rmarca"><span class="rcuenta">0 / '+paises.length+'</span>'+
   '<div class="rbarra"><i></i></div>'+
   '<button class="otra rreset" type="button">↺ empezar de nuevo</button></div>'+
   '<p class="desc">Klik een land, zeg het hardop, laat iemand bevestigen — dan pas aanklikken. '+
   'De teller is van de klas, niet van jou.</p><div class="rpais"></div>';
 const cont2=cont.querySelector('.rpais'),cuenta=cont.querySelector('.rcuenta'),
       barra=cont.querySelector('.rbarra i');
 let hechos=0;
 function pinta(iso){ // laat het land op de grote kaart meekleuren, als die er is
   const svg=document.querySelector('#mapwrap svg');if(!svg)return;
   const p=svg.querySelector('[data-c="'+iso+'"]');if(p)p.style.filter='saturate(1.6) brightness(1.05)';}
 paises.forEach(p=>{
   const b=document.createElement('button');b.type='button';
   b.innerHTML=exEsc(p.nombre)+'<span class="sil">'+exEsc(p.silabas)+'</span>';
   b.onclick=()=>{if(b.classList.contains('hecho'))return;
     b.classList.add('hecho');hechos++;pinta(p.iso);
     cuenta.textContent=hechos+' / '+paises.length;
     barra.style.width=Math.round(hechos/paises.length*100)+'%';
     if(typeof speak==='function')speak(p.nombre);
     if(hechos===paises.length)cuenta.textContent='¡'+paises.length+' / '+paises.length+' — lo habéis conseguido!';};
   cont2.appendChild(b);});
 cont.querySelector('.rreset').onclick=()=>{hechos=0;cuenta.textContent='0 / '+paises.length;
   barra.style.width='0';cont2.querySelectorAll('button').forEach(x=>x.classList.remove('hecho'));};
}
"""
