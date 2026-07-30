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
 // De mp3 wordt pas bij de eerste klik geladen. Zou het component het bestand al
 // bij het openen van de pagina proberen, dan logt de browser een netwerkfout
 // zolang er nog geen opname bestaat — en dan is «geen consolefouten» geen
 // bruikbare rooktest meer bij het bouwen van een unit.
 function fuente(){if(el||!cfg.audio)return el;
   el=new Audio(cfg.audio);el.preload='none';
   el.addEventListener('error',()=>{modo='tts';onEstado&&onEstado(modo,!parado);if(!parado){idx=0;ttsSecuencia();}});
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
    if(a){a.play().catch(()=>{modo='tts';onEstado&&onEstado(modo,true);idx=0;ttsSecuencia();});}
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
 const $=s=>host.querySelector(s);
 const fuente=$('.escfuente');
 const player=escReproductor(cfg,(modo,sonando)=>{
   fuente.textContent=modo==='mp3'?'audio grabado':'voz del navegador';
   const b=$('.escbtn-play');if(b)b.textContent=sonando?'⏹ Parar':'▶ Escuchar';});
 fuente.textContent=cfg.audio?'audio grabado':'voz del navegador';
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
       why.innerHTML=(bien?'<b>✓ correcto</b>':'<b>✗ no</b> → '+exEsc(it.ans))+(it.why?' · '+exEsc(it.why):'');
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
     '<div class="escprueba" hidden><label>Bewijs uit het fragment: <input type="text" class="tyfield escpr" autocomplete="off" aria-label="Bewijs bij stelling '+(i+1)+'"></label><button class="otra escprbtn" type="button">✓ Comprobar prueba</button></div>'+
     '<div class="exwhy" role="status" aria-live="polite"></div>';
   const opts=q.querySelector('.exopts'),why=q.querySelector('.exwhy'),pr=q.querySelector('.escprueba');
   let cerrado=false;
   opts.querySelectorAll('.exopt').forEach(b=>{b.onclick=()=>{if(cerrado)return;cerrado=true;
     const dicho=b.textContent==='Verdadero',bien=dicho===!!it.ans;
     opts.querySelectorAll('.exopt').forEach(x=>{x.disabled=true;
       if((x.textContent==='Verdadero')===!!it.ans)x.classList.add('ok');});
     if(!bien)b.classList.add('no');
     why.className='exwhy show '+(bien?'g':'b');
     why.innerHTML=(bien?'<b>✓ correcto</b>':'<b>✗ no</b> → '+(it.ans?'verdadero':'falso'))+' · Schrijf nu wáár je dat hoort.';
     pr.hidden=false;};});
   q.querySelector('.escprbtn').onclick=()=>{const v=q.querySelector('.escpr').value.trim();
     const a=tyNorm(v,'soft'),b=tyNorm(it.prueba||'','soft');
     const bien=a.length>2&&(b.indexOf(a)>-1||a.indexOf(b)>-1);
     why.className='exwhy show '+(bien?'g':'b');
     why.innerHTML=bien?'<b>✓ buena prueba</b> · «'+exEsc(it.prueba)+'»':'<b>✗ esa prueba no está</b> · en el fragment: «'+exEsc(it.prueba)+'»';
     q.querySelector('.escprbtn').disabled=true;q.querySelector('.escpr').disabled=true;
     estado.vf++;revisa();};
   $('.escvf').appendChild(q);});
 // 5 · transcript, pas ná de taken
 $('.esctr').innerHTML='<p class="desc esctrslot">Het transcript blijft dicht tot je de taken hierboven hebt gedaan — anders lees je mee in plaats van te luisteren.</p><button class="escbtn esctrbtn" type="button" disabled>🔒 Ver transcripción</button><div class="esctrbody" hidden></div>';
 function revisa(){const listo=(!cfg.global||estado.glob)&&estado.det>=det.length&&estado.vf>=vf.length;
   const b=$('.esctrbtn');if(!b)return;
   b.disabled=!listo;b.textContent=listo?'📄 Ver transcripción':'🔒 Ver transcripción';
   if(listo)$('.esctrslot').textContent='Klaar — nu mag je meelezen. Klik een regel om ze opnieuw te horen.';}
 revisa();
 $('.esctrbtn').onclick=()=>{const body=$('.esctrbody');
   if(!body.dataset.hecho){body.dataset.hecho='1';
     G.forEach((g,i)=>{const r=document.createElement('div');r.className='esctrl';
       r.innerHTML='<button class="esctrsay" type="button" aria-label="Regel '+(i+1)+' opnieuw horen">🔊</button>'+
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
"""
